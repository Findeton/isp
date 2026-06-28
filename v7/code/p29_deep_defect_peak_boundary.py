#!/usr/bin/env python3
"""
Paper 29 receipt: deep near-top defect peak boundary.

The previous near-top receipt reached N=22 and found a widening boundary layer
with the maximizer at defect k=2.  This receipt pushes the exact defect method
to N=24 and N=26 for k=0..4.

The result falsifies the old working beta guard 0.65: at N=26,k=2 the exact
near-top beta is about 0.6766.  This does not falsify the coefficient-root
envelope; it falsifies a numerical guard inherited from the smaller audits.

All non-integer arithmetic uses mpmath with dps=140.
"""

from functools import lru_cache
from itertools import combinations
import sys

import mpmath as mp

from p29_matching_lib import falling, fmt, physical_delta

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


def near_top_betas(D, max_defect):
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
    for k in range(max_defect + 1):
        r = half - k
        defect_size = 2 * k
        if defect_size == 0:
            total = haf(full)
        else:
            total = mp.mpf(0)
            for defect in combinations(range(n), defect_size):
                total += haf(full ^ mask_from_subset(defect))
        rho = (mp.mpf(2) ** r) * mp.factorial(r) * total / falling(n, 2 * r)
        q = mp.binomial(half, r) * rho * rho
        beta = mp.mpf(n) * mp.power(abs(q), mp.mpf(1) / r)
        lam = mp.power(abs((mp.mpf(n) ** r) * rho) / mp.sqrt(mp.factorial(r)), mp.mpf(1) / r)
        out[k] = (r, beta, lam, rho)
    return out, haf.cache_info().currsize


print("=" * 80)
print("Paper 29 deep near-top defect peak boundary")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

rows = []
print("\n=== Deep near-top physical c=0.5 profile ===")
for n in [24, 26]:
    D = physical_delta(n, mp.mpf("0.5"), nodes=12)
    betas, cache_states = near_top_betas(D, max_defect=4)
    best_k = max(betas, key=lambda k: betas[k][1])
    best_r, best_beta, best_lambda, _rho = betas[best_k]
    rows.append((n, best_k, best_r, best_beta, betas))
    print(f"\nN={n}, cache_states={cache_states}")
    for k in range(5):
        r, beta, lam, rho = betas[k]
        print(
            f"  k={k}, r={r}, beta={fmt(beta, 24)}, "
            f"lambda={fmt(lam, 24)}, rho={fmt(rho, 10)}"
        )
    print(f"  best_deep_near_top: k={best_k}, r={best_r}, beta={fmt(best_beta, 24)}")

max_beta = max(row[3] for row in rows)
best_ks = [row[1] for row in rows]
n26_beta = rows[-1][3]
n26_profile = rows[-1][4]

check(
    "deep near-top peak remains at defect k=2 for N=24 and N=26",
    best_ks == [2, 2],
    f"best_ks={best_ks}",
)
check(
    "old 0.65 working guard is falsified at N=26",
    n26_beta > mp.mpf("0.65"),
    f"N26_peak_beta={fmt(n26_beta, 24)}",
)
check(
    "N=26 peak is bracketed by neighboring defect layers",
    n26_profile[1][1] < n26_profile[2][1] and n26_profile[3][1] < n26_profile[2][1],
    f"k1={fmt(n26_profile[1][1], 18)} k2={fmt(n26_profile[2][1], 18)} k3={fmt(n26_profile[3][1], 18)}",
)
check(
    "deep audited peak remains below a looser 0.7 guard",
    max_beta < mp.mpf("0.7"),
    f"max_beta={fmt(max_beta, 24)}",
)

print("\n=== Theorem status ===")
print(
    "The widening near-top boundary layer is real and the old 0.65 guard is "
    "false.  The coefficient-root program is not dead: the N=26 peak remains "
    "below 0.7 and is locally bracketed at k=2.  The next theorem must derive "
    "the moving defect saddle and its limiting beta, not assume a fixed guard."
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
