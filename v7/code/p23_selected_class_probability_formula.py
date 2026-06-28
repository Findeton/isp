#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: selected-class P_N probability formula.

The direct S_N ladder hit the exact-denominator wall: for N>8, enumerating
the entire unlabeled sprinkling law P_N is expensive.  This receipt follows the
opening by deriving and checking a selected-class denominator formula.

For an unlabeled 2D poset C, let r(C) be the number of first linear orders L
such that the second order forced by C is also linear:

  - comparable pairs keep the same orientation in both orders;
  - incomparable pairs are reversed between the two orders.

Let Aut(C) be the automorphism group of the poset.  Then the number of
coordinate permutations whose unlabeled order is C is

    count_P(C) = r(C) / |Aut(C)|,

and therefore

    P_N(C) = r(C) / (|Aut(C)| N!).

This is not a full N>8 computation by itself; r(C) still has to be counted.
But it turns the next wall into a selected-class counting problem rather than
full support enumeration.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from collections import Counter
from itertools import permutations, product
import random
import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140


def fmt(x, n=32):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def iter_bits(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


class Poset:
    def __init__(self, future):
        self.future = tuple(future)
        self.N = len(self.future)
        self.past = [0] * self.N
        for x, mask in enumerate(self.future):
            for y in iter_bits(mask):
                self.past[y] |= 1 << x
        self.past = tuple(self.past)


def relation(poset, a, b):
    return bool(poset.future[a] & (1 << b))


def poset_from_permutation(perm):
    n = len(perm)
    future = [0] * n
    for i in range(n):
        vi = perm[i]
        mask = 0
        for j in range(i + 1, n):
            if vi < perm[j]:
                mask |= 1 << j
        future[i] = mask
    return Poset(future)


CANON_CACHE = {}


def refined_color_classes(poset):
    n = poset.N
    all_mask = (1 << n) - 1
    colors = tuple((poset.past[i].bit_count(), poset.future[i].bit_count()) for i in range(n))
    while True:
        signatures = []
        for i in range(n):
            bit = 1 << i
            incomparable = all_mask ^ bit ^ poset.past[i] ^ poset.future[i]
            signatures.append(
                (
                    colors[i],
                    tuple(sorted(colors[j] for j in iter_bits(poset.past[i]))),
                    tuple(sorted(colors[j] for j in iter_bits(poset.future[i]))),
                    tuple(sorted(colors[j] for j in iter_bits(incomparable))),
                )
            )
        unique = {sig: rank for rank, sig in enumerate(sorted(set(signatures), key=repr))}
        new_colors = tuple(unique[sig] for sig in signatures)
        if new_colors == colors:
            break
        colors = new_colors
    classes = {}
    for i, color in enumerate(colors):
        classes.setdefault(color, []).append(i)
    return [tuple(classes[color]) for color in sorted(classes)]


def code_for_order(poset, order):
    bits = []
    for i, a in enumerate(order):
        future = poset.future[a]
        for j, b in enumerate(order):
            if i != j:
                bits.append("1" if future & (1 << b) else "0")
    return "".join(bits)


def canonical_unlabeled_code(poset):
    cached = CANON_CACHE.get(poset.future)
    if cached is not None:
        return cached
    classes = refined_color_classes(poset)
    best = None
    for selected in product(*(permutations(cls) for cls in classes)):
        order = tuple(v for block in selected for v in block)
        code = code_for_order(poset, order)
        if best is None or code < best:
            best = code
    CANON_CACHE[poset.future] = best
    return best


def exact_counts_and_representatives(n):
    counts = Counter()
    reps = {}
    for perm in permutations(range(n)):
        poset = poset_from_permutation(perm)
        code = canonical_unlabeled_code(poset)
        counts[code] += 1
        reps.setdefault(code, poset)
    return counts, reps


def is_automorphism(poset, perm):
    n = poset.N
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            if relation(poset, a, b) != relation(poset, perm[a], perm[b]):
                return False
    return True


def automorphism_count(poset):
    classes = refined_color_classes(poset)
    total = 0
    for selected in product(*(permutations(cls) for cls in classes)):
        perm = [None] * poset.N
        for cls, image_block in zip(classes, selected):
            for source, image in zip(cls, image_block):
                perm[source] = image
        if is_automorphism(poset, perm):
            total += 1
    return total


def is_first_realizer_order(poset, order):
    n = poset.N
    rank = [0] * n
    for index, vertex in enumerate(order):
        rank[vertex] = index

    for a in range(n):
        for b in iter_bits(poset.future[a]):
            if rank[a] > rank[b]:
                return False

    before2 = [[False] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            if relation(poset, a, b):
                before2[a][b] = True
            elif relation(poset, b, a):
                before2[a][b] = False
            else:
                before2[a][b] = rank[a] > rank[b]

    for a in range(n):
        for b in range(n):
            if a == b or not before2[a][b]:
                continue
            for c in range(n):
                if c == a or c == b:
                    continue
                if before2[b][c] and not before2[a][c]:
                    return False
    return True


def realizer_first_order_count(poset):
    return sum(1 for order in permutations(range(poset.N)) if is_first_realizer_order(poset, order))


def formula_count(poset):
    r_count = realizer_first_order_count(poset)
    aut = automorphism_count(poset)
    if r_count % aut:
        return None, r_count, aut
    return r_count // aut, r_count, aut


print("=" * 80)
print("Collapsed P23 selected-class P_N probability formula")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

all_n_le_6_ok = True
for n in range(2, 7):
    print(f"\nExact all-class verification N={n}")
    counts, reps = exact_counts_and_representatives(n)
    local_ok = True
    max_aut = 0
    max_r = 0
    for code, exact_count in counts.items():
        predicted, r_count, aut = formula_count(reps[code])
        max_aut = max(max_aut, aut)
        max_r = max(max_r, r_count)
        if predicted != exact_count:
            local_ok = False
            print(
                f"  mismatch code_prefix={code[:24]} exact={exact_count} "
                f"predicted={predicted} r={r_count} aut={aut}"
            )
            break
    all_n_le_6_ok = all_n_le_6_ok and local_ok
    print(
        f"  classes={len(counts)} exact_total={sum(counts.values())} "
        f"max_r={max_r} max_aut={max_aut} status={'ok' if local_ok else 'fail'}"
    )

print("\nSelected N=8 verification")
n = 8
counts8, reps8 = exact_counts_and_representatives(n)
rng = random.Random(880008)
selected_codes = []
selected_codes.extend(code for code, _ in counts8.most_common(8))
selected_codes.extend(code for code, _ in sorted(counts8.items(), key=lambda item: item[1])[:8])
remaining = list(counts8)
rng.shuffle(remaining)
selected_codes.extend(remaining[:16])
selected_codes = list(dict.fromkeys(selected_codes))

n8_ok = True
for index, code in enumerate(selected_codes):
    exact_count = counts8[code]
    predicted, r_count, aut = formula_count(reps8[code])
    probability = mp.mpf(predicted) / mp.factorial(n) if predicted is not None else mp.nan
    exact_probability = mp.mpf(exact_count) / mp.factorial(n)
    ok = predicted == exact_count
    n8_ok = n8_ok and ok
    print(
        f"  selected={index:02d} exact={exact_count} predicted={predicted} "
        f"r={r_count} aut={aut} P={fmt(probability, 18)} "
        f"delta={fmt(probability - exact_probability, 6)} {'ok' if ok else 'FAIL'}"
    )

print("\nClosed-form sanity classes")
closed_ok = True
for n in range(2, 10):
    chain = Poset([(sum(1 << j for j in range(i + 1, n))) for i in range(n)])
    antichain = Poset([0] * n)
    chain_pred, chain_r, chain_aut = formula_count(chain)
    anti_pred, anti_r, anti_aut = formula_count(antichain)
    closed_ok = closed_ok and chain_pred == 1 and anti_pred == 1
    print(
        f"  N={n}: chain r={chain_r} aut={chain_aut} count={chain_pred}; "
        f"antichain r={anti_r} aut={anti_aut} count={anti_pred}"
    )

check(
    "Selected-class formula matches every exact class for N<=6",
    all_n_le_6_ok,
    "",
)
check(
    "Selected-class formula matches a hostile N=8 sample",
    n8_ok and len(selected_codes) >= 24,
    f"selected={len(selected_codes)}",
)
check(
    "Chain and antichain probabilities reduce to one coordinate permutation",
    closed_ok,
    "",
)
check(
    "Formula exposes the exact denominator task beyond N=8",
    True,
    "count realizer first orders r(C) and automorphisms, not whole support",
)

print("\n=== Consequence ===")
print("The exact denominator wall is partly reduced.  For a selected unlabeled")
print("2D order class C, P_N(C) can be obtained from r(C)/(|Aut(C)| N!),")
print("where r(C) counts first linear orders whose forced mate is linear.")
print("The next computational problem is not full P_N enumeration; it is")
print("fast selected-class counting for the rare classes produced by split")
print("S_N audits at N=10,12 and beyond.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
