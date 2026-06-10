#!/usr/bin/env python3
"""
v6_p19b: the triality-divisibility conjecture at scale (Paper 19).

Paper 17 observed that every minimal chiral base (size-3 stacks passing
the 2d anomaly predicates) has total charge divisible by 3, and Paper
18 explained the SUGGESTION (center neutrality); but is the
divisibility a THEOREM of the predicates or a small-charge accident?
Exhaustive scan: all genuinely chiral size-3 base pairs with charges up
to Q_max, bucketed by (sum q, sum q^2).
"""
from itertools import combinations_with_replacement
from collections import defaultdict

for QMAX in (8, 15, 25):
    buckets = defaultdict(list)
    for t in combinations_with_replacement(range(1, QMAX + 1), 3):
        buckets[(sum(t), sum(q * q for q in t))].append(t)
    total = 0
    bad = []
    for (S, S2), ts in buckets.items():
        if len(ts) < 2:
            continue
        for i in range(len(ts)):
            for j in range(i + 1, len(ts)):
                total += 1
                if S % 3 != 0:
                    bad.append((ts[i], ts[j], S))
    print(f"  Q_max = {QMAX}: chiral base pairs = {total};"
          f" with sum NOT divisible by 3: {len(bad)}")
    if bad:
        L, R, S = bad[0]
        print(f"    first counterexample: L = {list(L)}  R = {list(R)}"
              f"   (sum = {S})")
print("\n  -> verdict printed above: either the divisibility is exact at")
print("     all tested scales (conjecture strengthened toward a theorem)")
print("     or the first counterexample is exhibited and the Z_3 census")
print("     is demoted to a small-charge phenomenon - with Paper 18's")
print("     center derivation unaffected either way (it never relied on")
print("     the divisibility, only explained its appearance).")
print("== p19b done ==")
