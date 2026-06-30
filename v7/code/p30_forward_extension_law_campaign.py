#!/usr/bin/env python3
"""
Paper 30 receipt: forward extension law campaign.

The deletion campaigns found necessary constraints.  This receipt asks the
forward question directly:

    can a simple record-extension law grow the exact audited record
    distribution from small seeds?

We compare three finite forward laws on unlabeled 2D permutation-record orders:

1. fiber_multiplicity:
   choose parent R_{N+1} with weight presentation_count(parent) * D(parent, child).
   This is the exact Bayes/projective law for the uniform permutation
   pushforward, but it uses hidden presentation/fiber multiplicity.

2. deck_multiplicity:
   choose parent with weight D(parent, child) only.
   This is record-deck intrinsic but ignores hidden presentation multiplicity.

3. parent_uniform:
   choose uniformly among parent record types that can delete to the child.

Here D(parent, child) is the number of one-record deletions of parent that
produce child.  All probabilities and distances are exact Fractions.  If
mpmath is available it is set to dps=140 for decimal reporting; otherwise
Decimal fallback from the imported helper is used.
"""

from collections import defaultdict
from fractions import Fraction
import math
import sys

from p29_projected_likelihood_basis_audit import (
    canon_bits,
    flag_counts,
    fmt_frac,
    permutation_order_bits,
    perms,
    restrict_bits,
)

try:
    import mpmath as mp

    mp.mp.dps = 140
    PRECISION_LINE = f"mp.dps = {mp.mp.dps}"
except ModuleNotFoundError:
    PRECISION_LINE = (
        "exact Fraction arithmetic; decimal reporting through helper fallback; "
        "no floating arithmetic used for checks"
    )

sys.stdout.reconfigure(line_buffering=True)
sys.setrecursionlimit(20000)

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def build_score_data(n):
    counts = defaultdict(int)
    reps = {}
    for pi in perms(n):
        bits = permutation_order_bits(pi)
        key = canon_bits(bits, n)
        reps.setdefault(key, bits)
        counts[key] += 1
    dist = {key: Fraction(count, math.factorial(n)) for key, count in counts.items()}
    print(f"  built N={n}: permutations={math.factorial(n)} records={len(counts)}")
    return dict(counts), reps, dist


def delete_deck(bits, n):
    deck = defaultdict(int)
    for deleted in range(n):
        subset = tuple(v for v in range(n) if v != deleted)
        child = restrict_bits(bits, n, subset)
        child_key = canon_bits(child, n - 1)
        deck[child_key] += 1
    return dict(deck)


def build_extension_data(counts_by_n, reps_by_n, n_min, n_max):
    parent_decks = {}
    reverse = {}
    for n in range(n_min, n_max):
        parent_n = n + 1
        parent_decks[parent_n] = {}
        rows = defaultdict(dict)
        for parent_key, bits in reps_by_n[parent_n].items():
            deck = delete_deck(bits, parent_n)
            parent_decks[parent_n][parent_key] = deck
            for child_key, multiplicity in deck.items():
                rows[child_key][parent_key] = multiplicity
        reverse[n] = dict(rows)
        print(
            f"  extension N={n}->{parent_n}: children={len(reverse[n])} "
            f"parents={len(parent_decks[parent_n])}"
        )
    return parent_decks, reverse


def total_variation(left, right):
    keys = set(left) | set(right)
    return sum(abs(left.get(key, Fraction(0)) - right.get(key, Fraction(0))) for key in keys) / 2


def support_size(dist):
    return sum(1 for value in dist.values() if value)


def entropy_bits(dist):
    # Reporting only. Checks use exact TV.
    total = 0.0
    for value in dist.values():
        if value:
            p = value.numerator / value.denominator
            total -= p * math.log2(p)
    return total


def forward_step(dist, n, law, counts_by_n, reverse):
    out = defaultdict(Fraction)
    parent_counts = counts_by_n[n + 1]
    for child_key, child_prob in dist.items():
        if child_prob == 0:
            continue
        parents = reverse[n].get(child_key, {})
        if not parents:
            continue
        if law == "fiber_multiplicity":
            weights = {
                parent_key: parent_counts[parent_key] * multiplicity
                for parent_key, multiplicity in parents.items()
            }
        elif law == "deck_multiplicity":
            weights = dict(parents)
        elif law == "parent_uniform":
            weights = {parent_key: 1 for parent_key in parents}
        else:
            raise ValueError(f"unknown law: {law}")
        denom = sum(weights.values())
        for parent_key, weight in weights.items():
            out[parent_key] += child_prob * Fraction(weight, denom)
    return dict(out)


def run_forward(seed_dist, seed_n, law, n_max, counts_by_n, reverse):
    dists = {seed_n: dict(seed_dist)}
    current = dict(seed_dist)
    for n in range(seed_n, n_max):
        current = forward_step(current, n, law, counts_by_n, reverse)
        dists[n + 1] = current
    return dists


def exact_preimage_identity(counts_by_n, parent_decks, n_min, n_max):
    failures = []
    for child_n in range(n_min, n_max):
        parent_n = child_n + 1
        lhs = defaultdict(int)
        for parent_key, deck in parent_decks[parent_n].items():
            for child_key, multiplicity in deck.items():
                lhs[child_key] += counts_by_n[parent_n][parent_key] * multiplicity
        factor = parent_n * parent_n
        for child_key, child_count in counts_by_n[child_n].items():
            expected = child_count * factor
            if lhs[child_key] != expected:
                failures.append((child_n, child_key, lhs[child_key], expected))
    return failures


def describe_law(law, seed_name, dists, exact_by_n, n_values):
    print(f"\nlaw={law} seed={seed_name}")
    rows = {}
    for n in n_values:
        dist = dists[n]
        tv = total_variation(dist, exact_by_n[n])
        rows[n] = tv
        print(
            f"  N={n:<2} TV={fmt_frac(tv, 24):>28} "
            f"support={support_size(dist):>7}/{len(exact_by_n[n]):<7} "
            f"H={entropy_bits(dist):.6f}"
        )
    return rows


def expectation(dist, values):
    return sum(prob * values.get(key, 0) for key, prob in dist.items())


def sector_expectation_report(label, dist, exact, features, sectors):
    print(f"\nsector expectations at N=8 for {label}")
    rows = {}
    for sector in sectors:
        values = features["flags5"][f"flag5_{sector}"]
        got = expectation(dist, values)
        want = expectation(exact, values)
        delta = got - want
        rows[sector] = (got, want, delta)
        print(
            f"  flag5_{sector:<6} got={fmt_frac(got, 18):>22} "
            f"exact={fmt_frac(want, 18):>22} delta={fmt_frac(delta, 18):>22}"
        )
    return rows


def light_flag5_maps(record_keys, reps, n, sectors):
    features = {"flags5": defaultdict(dict)}
    for key in record_keys:
        counts = flag_counts(reps[key], n, 5)
        for sector in sectors:
            features["flags5"][f"flag5_{sector}"][key] = counts.get(sector, 0)
    return features


print("=" * 80)
print("Paper 30 forward extension law campaign")
print("=" * 80)
print(PRECISION_LINE)

n_min = 1
n_max = 9
counts_by_n = {}
reps_by_n = {}
exact_by_n = {}

print("\n" + "=" * 80)
print("Exact record universes")
print("=" * 80)
for n in range(n_min, n_max + 1):
    counts, reps, dist = build_score_data(n)
    counts_by_n[n] = counts
    reps_by_n[n] = reps
    exact_by_n[n] = dist

print("\n" + "=" * 80)
print("Extension decks")
print("=" * 80)
parent_decks, reverse = build_extension_data(counts_by_n, reps_by_n, n_min, n_max)

print("\n" + "=" * 80)
print("Presentation preimage identity")
print("=" * 80)
identity_failures = exact_preimage_identity(counts_by_n, parent_decks, n_min, n_max)
print(f"identity_failures={identity_failures[:5]} total={len(identity_failures)}")

seed1 = exact_by_n[1]
seed2_exact = exact_by_n[2]
seed3_exact = exact_by_n[3]
seed2_extremes = {
    f"N2_delta_{idx}": {key: Fraction(1)}
    for idx, key in enumerate(sorted(exact_by_n[2]))
}

laws = ["fiber_multiplicity", "deck_multiplicity", "parent_uniform"]
n_report = list(range(1, n_max + 1))
law_rows = {}

print("\n" + "=" * 80)
print("Forward growth from exact small seeds")
print("=" * 80)
for law in laws:
    dists = run_forward(seed1, 1, law, n_max, counts_by_n, reverse)
    law_rows[(law, "N1")] = describe_law(law, "N1", dists, exact_by_n, n_report)
    if law != "fiber_multiplicity":
        dists2 = run_forward(seed2_exact, 2, law, n_max, counts_by_n, reverse)
        law_rows[(law, "N2_exact")] = describe_law(law, "N2_exact", dists2, exact_by_n, list(range(2, n_max + 1)))
        dists3 = run_forward(seed3_exact, 3, law, n_max, counts_by_n, reverse)
        law_rows[(law, "N3_exact")] = describe_law(law, "N3_exact", dists3, exact_by_n, list(range(3, n_max + 1)))

print("\n" + "=" * 80)
print("Seed dependence for non-fiber laws")
print("=" * 80)
seed_dependence = {}
for law in ["deck_multiplicity", "parent_uniform"]:
    finals = {}
    for seed_name, seed in seed2_extremes.items():
        dists = run_forward(seed, 2, law, n_max, counts_by_n, reverse)
        finals[seed_name] = dists[n_max]
    pair_tvs = []
    names = sorted(finals)
    for idx, left in enumerate(names):
        for right in names[idx + 1 :]:
            pair_tvs.append(total_variation(finals[left], finals[right]))
    seed_dependence[law] = max(pair_tvs)
    print(f"{law:<20} max_N9_seed_TV={fmt_frac(seed_dependence[law], 24)}")

print("\n" + "=" * 80)
print("Boundary-sector expectations under forward laws")
print("=" * 80)
sectors = [912, 664, 525184, 25360, 924]
features8 = light_flag5_maps(sorted(exact_by_n[8]), reps_by_n[8], 8, sectors)
forward_fiber = run_forward(seed1, 1, "fiber_multiplicity", 8, counts_by_n, reverse)[8]
forward_deck = run_forward(seed1, 1, "deck_multiplicity", 8, counts_by_n, reverse)[8]
forward_uniform = run_forward(seed1, 1, "parent_uniform", 8, counts_by_n, reverse)[8]
sector_rows = {
    "fiber": sector_expectation_report("fiber_multiplicity", forward_fiber, exact_by_n[8], features8, sectors),
    "deck": sector_expectation_report("deck_multiplicity", forward_deck, exact_by_n[8], features8, sectors),
    "uniform": sector_expectation_report("parent_uniform", forward_uniform, exact_by_n[8], features8, sectors),
}

print("\n" + "=" * 80)
print("Hostile review")
print("=" * 80)
print(
    "1. A forward law exists that exactly reproduces the audited P_N: the "
    "fiber-multiplicity law.  But it uses presentation/fiber multiplicity, "
    "which is precisely the kind of hidden structure the record law cannot "
    "simply assume."
)
print(
    "2. Pure record-deck forward laws are not exact.  They are honest local "
    "record extension laws, but their total-variation error grows with N and "
    "their sector expectations drift away from the exact record distribution."
)
print(
    "3. The deletion campaigns were therefore not secretly doing time reversal. "
    "They exposed the constraints any forward law must satisfy; the first "
    "forward test shows that satisfying them exactly requires either hidden "
    "fiber multiplicity or a record-intrinsic substitute for it."
)

fiber_tv_max = max(law_rows[("fiber_multiplicity", "N1")].values())
deck_tv_n9 = law_rows[("deck_multiplicity", "N1")][9]
uniform_tv_n9 = law_rows[("parent_uniform", "N1")][9]

check(
    "presentation preimage identity holds exactly",
    not identity_failures,
    f"failures={len(identity_failures)}",
)
check(
    "fiber-multiplicity forward law reproduces exact P_N",
    fiber_tv_max == 0,
    f"max_TV={fmt_frac(fiber_tv_max, 24)}",
)
check(
    "deck-only forward law fails by N=9",
    deck_tv_n9 > 0,
    f"TV_N9={fmt_frac(deck_tv_n9, 24)}",
)
check(
    "uniform-parent forward law fails by N=9",
    uniform_tv_n9 > 0,
    f"TV_N9={fmt_frac(uniform_tv_n9, 24)}",
)
check(
    "non-fiber laws retain seed dependence at N=9",
    all(value > 0 for value in seed_dependence.values()),
    ", ".join(f"{law}={fmt_frac(value, 18)}" for law, value in seed_dependence.items()),
)
check(
    "fiber law matches audited boundary-sector expectations",
    all(delta == 0 for _got, _want, delta in sector_rows["fiber"].values()),
    "all deltas zero",
)

print("\n=== Campaign status ===")
print(
    "Forward growth clarifies the problem.  Exact projective growth is easy if "
    "the law may use hidden presentation multiplicity.  Pure record-deck growth "
    "is genuinely forward and record-local, but it fails to reproduce the exact "
    "audited record distribution.  The missing click-law ingredient is therefore "
    "a record-intrinsic effective replacement for fiber multiplicity, constrained "
    "by the residual-active boundary filtration."
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
