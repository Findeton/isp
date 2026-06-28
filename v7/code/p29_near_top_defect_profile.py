#!/usr/bin/env python3
"""
Paper 29 receipt: near-top defect profile.

Top order is not an exact dominance theorem: the all-order audits show the
largest beta one order below top.  This receipt computes the near-top defect
profile

    r = N/2 - k,  k=0,1,2,3,

without computing every lower order.  For each subset S of size 2r it computes
the perfect-matching sum Haf(D|_S), then sums over all such S:

    rho_{N,r} = 2^r r! sum_{|S|=2r} Haf(D|_S) / (N)_{2r}.

This agrees with the all-order DP where both are available and extends the
near-top beta audit to N=20,22.  It also falsifies fixed one-defect dominance:
the maximizer moves to k=2 in the deeper ladder.

All non-integer arithmetic uses mpmath with dps=140.
"""

from functools import lru_cache
from itertools import combinations
import sys

import mpmath as mp

from p29_matching_lib import coefficient_profile, falling, fmt, physical_delta

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def mask_from_subset(subset):
    mask = 0
    for i in subset:
        mask |= 1 << i
    return mask


def near_top_rhos(D, max_defect):
    n = len(D)
    half = n // 2
    full = (1 << n) - 1

    @lru_cache(maxsize=None)
    def haf(mask):
        if mask == 0:
            return mp.mpf(1)
        first_bit = mask & -mask
        i = first_bit.bit_length() - 1
        rest = mask ^ first_bit
        total = mp.mpf(0)
        m = rest
        while m:
            bit = m & -m
            j = bit.bit_length() - 1
            total += D[i][j] * haf(rest ^ bit)
            m ^= bit
        return total

    out = {}
    sums = {}
    for k in range(max_defect + 1):
        r = half - k
        if r < 1:
            continue
        size = 2 * r
        if size == n:
            total = haf(full)
        else:
            total = mp.mpf(0)
            # Sum over unmatched-defect complements; this is smaller near top.
            defect_size = n - size
            for defect in combinations(range(n), defect_size):
                mask = full ^ mask_from_subset(defect)
                total += haf(mask)
        rho = (mp.mpf(2) ** r) * mp.factorial(r) * total / falling(n, 2 * r)
        out[r] = rho
        sums[r] = total
    return out, sums, haf.cache_info().currsize


def beta_from_rho(n, r, rho):
    q = mp.binomial(n // 2, r) * rho * rho
    beta = mp.mpf(n) * mp.power(abs(q), mp.mpf(1) / r)
    lam = mp.power(abs((mp.mpf(n) ** r) * rho) / mp.sqrt(mp.factorial(r)), mp.mpf(1) / r)
    return beta, lam


print("=" * 80)
print("Paper 29 near-top defect profile")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

max_defect = 3
max_agreement_error = mp.mpf(0)
rows = []

print("\n=== Near-top physical c=0.5 profile ===")
for n in [14, 16, 18, 20, 22]:
    D = physical_delta(n, mp.mpf("0.5"), nodes=12)
    rhos, sums, cache_size = near_top_rhos(D, max_defect=max_defect)
    all_beta = None
    if n <= 18:
        _q, all_rho, all_beta = coefficient_profile(D)
    print(f"\nN={n}, cache_states={cache_size}")
    best = None
    for k in range(max_defect + 1):
        r = n // 2 - k
        rho = rhos[r]
        beta, lam = beta_from_rho(n, r, rho)
        if best is None or beta > best[2]:
            best = (k, r, beta)
        if all_beta is not None:
            err = abs(beta - all_beta[r])
            max_agreement_error = max(max_agreement_error, err)
        else:
            err = mp.nan
        print(
            f"  k={k}, r={r}, beta={fmt(beta, 24)}, "
            f"lambda={fmt(lam, 24)}, rho={fmt(rho, 12)}, "
            f"all_order_err={fmt(err, 8) if all_beta is not None else 'n/a'}"
        )
    rows.append((n, best[0], best[1], best[2], rhos[n // 2]))
    print(f"  best_near_top: k={best[0]}, r={best[1]}, beta={fmt(best[2], 24)}")

max_near_top_beta = max(row[3] for row in rows)
best_k_values = [row[1] for row in rows]
top_only_false_deep = all(row[1] != 0 for row in rows if row[0] >= 16)

check(
    "near-top defect method agrees with all-order beta through N=18",
    max_agreement_error < mp.mpf("1e-100"),
    f"max_agreement_error={fmt(max_agreement_error, 18)}",
)
check(
    "near-top beta remains below working guard through N=22",
    max_near_top_beta < mp.mpf("0.65"),
    f"max_near_top_beta={fmt(max_near_top_beta, 24)}",
)
check(
    "top-only dominance is false in the deeper near-top ladder",
    top_only_false_deep,
    f"best_k_values={best_k_values}",
)
check(
    "fixed one-defect dominance is falsified by deeper near-top ladder",
    max(best_k_values) == 2,
    f"best_k_values={best_k_values}",
)

print("\n=== Theorem status ===")
print(
    "The near-top layer can be computed directly by defect subsets.  Through "
    "N=22 the maximum audited near-top beta is still subcritical, but the "
    "maximizer moves from one-defect to two-defect at N=20.  The proof target "
    "is therefore a widening near-top boundary layer plus a bulk bound, not a "
    "fixed-defect theorem."
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
