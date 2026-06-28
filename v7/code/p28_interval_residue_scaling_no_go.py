#!/usr/bin/env python3
"""
Paper 28 receipt: proper-interval residue scaling no-go.

The interval-to-subset bridge campaign falsified exact coverage by proper
intervals.  This receipt attacks the possible rescue:

    maybe the uncovered subset mass is small enough that proper interval
    certificates still imply the coefficient-root envelope.

For contiguous proper intervals on N ordered records, all 2r-subsets with
both endpoints {0,N-1} are invisible to every proper interval.  Their exact
uniform mass is

    delta_{N,r} = binom(N-2,2r-2) / binom(N,2r)
                = (2r)(2r-1) / (N(N-1)).

The bounded witness f=1 on those uncovered subsets and f=0 elsewhere has
zero proper-interval averages but global average delta_{N,r}.  If this is
inserted into the matching coefficient shape q_{N,r}=binom(N/2,r) rho^2,
then

    N q_{N,r}^{1/r}

diverges for every r>2.  Therefore proper interval heredity plus a bounded
amplitude guard cannot imply the required all-order coefficient-root envelope.

All non-integer arithmetic uses mpmath with dps=140.
"""

from itertools import combinations
from math import comb
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


def mp_comb(n, k):
    if k < 0 or k > n:
        return mp.mpf(0)
    return mp.mpf(comb(n, k))


def delta_exact(n, r):
    k = 2 * r
    return mp_comb(n - 2, k - 2) / mp_comb(n, k)


def delta_closed(n, r):
    k = 2 * r
    return mp.mpf(k * (k - 1)) / (mp.mpf(n) * (n - 1))


def q_witness(n, r):
    rho = delta_exact(n, r)
    return mp_comb(n // 2, r) * rho * rho


def beta_root(n, r):
    q = q_witness(n, r)
    return mp.mpf(n) * mp.power(q, mp.mpf(1) / r)


def proper_interval_uncovered_bruteforce(n, r):
    k = 2 * r
    subsets = list(combinations(range(n), k))
    uncovered = []
    for subset in subsets:
        # A subset is contained in a proper contiguous interval iff its span is
        # strictly smaller than N.
        if subset[0] == 0 and subset[-1] == n - 1:
            uncovered.append(subset)
    return len(uncovered), len(subsets)


print("=" * 80)
print("Paper 28 proper-interval residue scaling no-go")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

print("\n=== Exact uncovered mass for proper contiguous intervals ===")
for r in [2, 3, 4, 5]:
    k = 2 * r
    n = 24
    d_formula = delta_exact(n, r)
    d_closed = delta_closed(n, r)
    print(
        f"r={r}, k={k}, N={n}, delta={fmt(d_formula, 24)}, "
        f"N^2 delta={fmt(mp.mpf(n) ** 2 * d_formula, 24)}"
    )
    check(
        f"closed uncovered-mass formula holds for r={r}",
        abs(d_formula - d_closed) < mp.mpf("1e-120"),
        f"error={fmt(abs(d_formula - d_closed), 12)}",
    )

print("\n=== Brute-force confirmation at small N ===")
for n, r in [(10, 2), (12, 3), (14, 4)]:
    count, total = proper_interval_uncovered_bruteforce(n, r)
    formula_count = comb(n - 2, 2 * r - 2)
    print(f"N={n}, r={r}, brute_uncovered={count}, formula={formula_count}, total={total}")
    check(
        f"brute uncovered count agrees for N={n}, r={r}",
        count == formula_count,
        f"count={count}",
    )

print("\n=== Coefficient-root residue growth ===")
ladder = [24, 48, 96, 192, 384]
beta_by_r = {}
for r in [2, 3, 4, 5, 6]:
    values = [beta_root(n, r) for n in ladder if n >= 2 * r and n % 2 == 0]
    beta_by_r[r] = values
    print(f"r={r}: " + ", ".join(f"N={n}: beta={fmt(v, 18)}" for n, v in zip(ladder, values)))

check(
    "r=2 endpoint residue has bounded root scale over the ladder",
    beta_by_r[2][-1] < 2 * beta_by_r[2][0],
    f"beta24={fmt(beta_by_r[2][0], 18)} beta384={fmt(beta_by_r[2][-1], 18)}",
)
for r in [3, 4, 5, 6]:
    check(
        f"r={r} endpoint residue root scale grows over the ladder",
        beta_by_r[r][-1] > 2 * beta_by_r[r][0],
        f"beta24={fmt(beta_by_r[r][0], 18)} beta384={fmt(beta_by_r[r][-1], 18)}",
    )

print("\n=== Asymptotic exponent check ===")
for r in [3, 4, 5, 6]:
    expected = mp.mpf(2) - mp.mpf(4) / r
    observed = mp.log(beta_by_r[r][-1] / beta_by_r[r][1]) / mp.log(mp.mpf(ladder[-1]) / ladder[1])
    print(f"r={r}, expected exponent={fmt(expected, 18)}, observed={fmt(observed, 18)}")
    check(
        f"r={r} observed growth is compatible with N^(2-4/r)",
        abs(observed - expected) < mp.mpf("0.15"),
        f"expected={fmt(expected, 12)} observed={fmt(observed, 12)}",
    )

print("\n=== Theorem status ===")
print("FALSIFIED AS A STANDALONE THEOREM: proper contiguous interval")
print("certificates plus a bounded-amplitude residue cannot imply the")
print("coefficient-root envelope for all r.  The endpoint-spanning invisible")
print("subsets have mass O(N^-2), which is too large for r>2 after the")
print("q_{N,r}=binom(N/2,r) rho^2 scaling.  Surviving routes must add a")
print("charged full/global sector, explicit all-subset certificates, or a")
print("new physical cancellation theorem for the missed residue.")

print("\n" + "=" * 80)
failed = [name for name, ok, _detail in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
