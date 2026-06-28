#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: exact local Palm-kernel integral.

The Monte Carlo Palm-kernel receipt found that pair comparability is exactly
null, while a sibling-plus-outsider triple kernel can be visible.  This receipt
replaces that Monte Carlo projection with a high-precision integral.

In one coordinate, let siblings be X_1=S+E_1 and X_2=S+E_2, with
S~Unif[0,1] and E_i~Unif[-c,c].  Let Z be an independent outsider with the
same marginal distribution F_c.  The one-coordinate relative order law is
determined by

    q(c) = P(Z lies between X_1 and X_2)
         = E |F_c(X_1)-F_c(X_2)|.

For a fixed parent S=s this conditional expectation has the exact integral

    c^{-2} int_{s-c}^{s+c} (t-s) F_c(t) dt.

The two lightcone coordinates are independent, so the 1+1 sibling-plus-outsider
triple law is obtained by drawing two independent permutations from this
one-coordinate law and enumerating the induced poset pattern.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

import itertools
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


def A(z, c):
    z = mp.mpf(z)
    c = mp.mpf(c)
    if z <= -c:
        return mp.mpf(0)
    if z < c:
        return (z + c) ** 2 / (4 * c)
    return z


def B_anti(z, c):
    """Antiderivative of A(z,c)."""
    z = mp.mpf(z)
    c = mp.mpf(c)
    if z <= -c:
        return mp.mpf(0)
    if z < c:
        return (z + c) ** 3 / (12 * c)
    return z**2 / 2 + c**2 / 6


def C_anti(z, c):
    """Antiderivative of z*A(z,c)."""
    z = mp.mpf(z)
    c = mp.mpf(c)
    if z <= -c:
        return mp.mpf(0)
    if z < c:
        y = z + c
        return y**4 / (16 * c) - y**3 / 12
    return z**3 / 3


def F(x, c):
    """CDF of S+E."""
    x = mp.mpf(x)
    return A(x, c) - A(x - 1, c)


def G(x, c):
    """Antiderivative of F."""
    x = mp.mpf(x)
    return B_anti(x, c) - B_anti(x - 1, c)


def K(x, c):
    """Antiderivative of x*F(x)."""
    x = mp.mpf(x)
    return C_anti(x, c) - C_anti(x - 1, c) - B_anti(x - 1, c)


def q_conditional_s(s, c):
    s = mp.mpf(s)
    c = mp.mpf(c)
    lo = s - c
    hi = s + c
    integral = (K(hi, c) - K(lo, c)) - s * (G(hi, c) - G(lo, c))
    return integral / (c**2)


def split_points_for_q(c):
    c = mp.mpf(c)
    breakpoints = {-c, c, 1 - c, 1 + c}
    points = {mp.mpf(0), mp.mpf(1)}
    for b in breakpoints:
        for s in [b - c, b + c]:
            if 0 < s < 1:
                points.add(+s)
    return sorted(points)


def q_between(c):
    c = mp.mpf(c)
    points = split_points_for_q(c)
    total = mp.mpf(0)
    for left, right in zip(points[:-1], points[1:]):
        if left != right:
            total += mp.quad(lambda s: q_conditional_s(s, c), [left, right])
    return +total


def one_axis_permutation_law(q):
    """Labels 0,1 are siblings; label 2 is outsider."""
    q = mp.mpf(q)
    law = {}
    for perm in itertools.permutations([0, 1, 2]):
        if perm in [(0, 2, 1), (1, 2, 0)]:
            law[perm] = q / 2
        else:
            law[perm] = (1 - q) / 4
    return law


def pattern_of_permutations(perm_u, perm_v):
    pos_u = {label: index for index, label in enumerate(perm_u)}
    pos_v = {label: index for index, label in enumerate(perm_v)}
    future = [set() for _ in range(3)]
    past = [set() for _ in range(3)]
    relations = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            if pos_u[i] < pos_u[j] and pos_v[i] < pos_v[j]:
                future[i].add(j)
                past[j].add(i)
                relations += 1
    if relations == 0:
        return "antichain"
    if relations == 1:
        return "one_relation"
    if relations == 3:
        return "chain"
    if relations != 2:
        raise ValueError(f"unexpected relation count {relations}")
    if sorted(len(row) for row in future) == [0, 0, 2]:
        return "vee"
    if sorted(len(row) for row in past) == [0, 0, 2]:
        return "wedge"
    raise ValueError("bad two-relation triple")


def triple_law_from_q(q):
    axis = one_axis_permutation_law(q)
    out = {name: mp.mpf(0) for name in ["antichain", "one_relation", "vee", "wedge", "chain"]}
    for pu, wu in axis.items():
        for pv, wv in axis.items():
            out[pattern_of_permutations(pu, pv)] += wu * wv
    return out


def iid_triple_law():
    return {
        "antichain": mp.mpf(1) / 6,
        "one_relation": mp.mpf(1) / 3,
        "vee": mp.mpf(1) / 6,
        "wedge": mp.mpf(1) / 6,
        "chain": mp.mpf(1) / 6,
    }


def l1(law_a, law_b):
    return sum(abs(law_a[name] - law_b[name]) for name in law_a)


print("=" * 80)
print("Collapsed P23 exact local Palm-kernel integral")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

exact_iid = iid_triple_law()
cs = [mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2"), mp.mpf("4"), mp.mpf("8")]
rows = []

print("\n(1) Exact q(c) and triple Palm law")
for c in cs:
    q = q_between(c)
    law = triple_law_from_q(q)
    gap = l1(law, exact_iid)
    rows.append((c, q, law, gap))
    print(f"\nc={fmt(c, 8)} q_between={fmt(q, 40)} L1={fmt(gap, 40)}")
    for name in ["antichain", "one_relation", "vee", "wedge", "chain"]:
        print(f"  {name:>13} = {fmt(law[name], 40)}")

print("\n(2) Boundary checks")
check(
    "Independent one-axis law is recovered when q=1/3",
    all(abs(triple_law_from_q(mp.mpf(1) / 3)[name] - exact_iid[name]) < mp.mpf("1e-80") for name in exact_iid),
    "q=1/3 gives the exact iid 1+1 triple law",
)
check(
    "Finite c has a nonzero exact local Palm triple residue",
    all(gap > mp.mpf("1e-8") for _c, _q, _law, gap in rows),
    ", ".join(f"c={fmt(c, 4)} L1={fmt(gap, 12)}" for c, _q, _law, gap in rows[:4]),
)
check(
    "The residue decreases along the tested large-mixing tail",
    all(rows[i][3] > rows[i + 1][3] for i in range(2, len(rows) - 1)),
    ", ".join(f"c={fmt(c, 4)} L1={fmt(gap, 12)}" for c, _q, _law, gap in rows[2:]),
)
check(
    "The exact c=0.5 signal matches the Monte Carlo Palm-kernel scale",
    abs(next(gap for c, _q, _law, gap in rows if c == mp.mpf("0.5")) - mp.mpf("0.0292833333333333333"))
    < mp.mpf("0.003"),
    f"exact={fmt(next(gap for c, _q, _law, gap in rows if c == mp.mpf('0.5')), 18)}",
)
check(
    "The exact c=1 residue is real but small enough to be hidden by the previous Monte Carlo control",
    next(gap for c, _q, _law, gap in rows if c == 1) < mp.mpf("0.01")
    and next(gap for c, _q, _law, gap in rows if c == 1) > mp.mpf("0.001"),
    f"L1(c=1)={fmt(next(gap for c, _q, _law, gap in rows if c == 1), 18)}",
)

print("\n(3) Consequence")
print("The pair kernel is exactly null, but the sibling-plus-outsider triple")
print("Palm kernel has a nonzero exact order-only residue for finite c.  The")
print("residue decays with mixing and is already small near c=1, which explains")
print("why direct finite pair ranking and Monte Carlo triple checks can miss it.")
print("The next theorem should decide whether square-root accumulation of this")
print("tiny local Palm residue yields a nontrivial order-only likelihood ratio.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
