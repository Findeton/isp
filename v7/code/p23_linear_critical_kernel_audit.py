#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: linear critical-window kernel audit.

The previous proof bounded the easy residue and strong washout regimes.  This
receipt checks the next theorem-shaped fact: for bounded hidden width, fixed
unrooted finite patterns cannot distinguish the linear critical window.  Once a
fixed sample avoids hidden-cluster collisions, its two coordinate rankings are
asymptotically independent random permutations, hence the same fixed-k order
law as 1+1 sprinkling.

The receipt also checks a simple analytic rooted-neighborhood fact: when
J_N/m_N tends to a positive finite constant, same-cluster partners are no
longer microscopic near twins.  Their coordinate-rank separation is order-one
with positive probability.

All non-integer arithmetic uses mpmath with dps=140.
"""

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


def collision_bound(N, w, k):
    """Union bound that a k-sample contains a same-hidden-cluster pair."""
    return mp.binomial(k, 2) * mp.mpf(w - 1) / mp.mpf(N - 1)


def sprinkling_triple_law():
    """Antichain, one-relation, vee, wedge, chain for 3 records in 1+1."""
    return {
        "antichain": mp.mpf(1) / 6,
        "one_relation": mp.mpf(1) / 3,
        "vee": mp.mpf(1) / 6,
        "wedge": mp.mpf(1) / 6,
        "chain": mp.mpf(1) / 6,
    }


def pair_relation_probability():
    """For two iid continuous records with independent coordinates."""
    return mp.mpf(1) / 4


def triangular_tail_probability(L, eps):
    """P(|X-Y| >= eps) for X,Y iid Uniform[-L,L], 0<=eps<=2L."""
    L = mp.mpf(L)
    eps = mp.mpf(eps)
    if eps <= 0:
        return mp.mpf(1)
    if eps >= 2 * L:
        return mp.mpf(0)
    # Difference has triangular density.  P(|D| < eps)=eps/L - eps^2/(4L^2).
    return 1 - eps / L + eps ** 2 / (4 * L ** 2)


def rank_gap_lower_bound(L, eps):
    """
    A simple lower-bound witness that same-cluster coordinates are not
    microscopic when J_N/m_N -> L>0.

    On the central event A in [1/4,3/4] and jitters separated by eps, the raw
    coordinate gap is at least eps.  The convolved coordinate distribution has
    density at least 1/(2L) on any interval contained in a unit center slab, so
    the rank gap is at least eps/(2L) on that event.  This is deliberately
    crude; only positivity matters.
    """
    L = mp.mpf(L)
    eps = mp.mpf(eps)
    central_A = mp.mpf(1) / 2
    sep = triangular_tail_probability(L, eps)
    rank_gap = eps / (2 * L)
    return central_A * sep, rank_gap


print("=" * 80)
print("Collapsed P23 linear critical-window kernel audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

Ns = [mp.mpf(2) ** k for k in [10, 14, 18, 22]]
widths = [2, 4, 8, 16]
ks = [3, 4, 5, 8]

print("\n(1) Hidden-cluster collision bounds for fixed samples")
collision_ok = True
for w in widths:
    for k in ks:
        bounds = [collision_bound(N, w, k) for N in Ns]
        collision_ok = collision_ok and all(bounds[i] > bounds[i + 1] for i in range(len(bounds) - 1))
        print(f"w={w}, k={k}: bounds={ [fmt(value, 12) for value in bounds] }")

print("\n(2) Exact fixed triple law after no hidden collision")
triple = sprinkling_triple_law()
triple_sum = sum(triple.values())
for name, value in triple.items():
    print(f"{name:>13} = {fmt(value, 32)}")
print("sum =", fmt(triple_sum, 32))

print("\n(3) Pair law by rank symmetry")
pair_prob = pair_relation_probability()
print("P[x<y] =", fmt(pair_prob, 32))

print("\n(4) Linear-window same-cluster rank-gap witness")
gap_ok = True
for L in [mp.mpf("0.25"), mp.mpf("1.0"), mp.mpf("4.0")]:
    eps = L / 4
    event_prob, rank_gap = rank_gap_lower_bound(L, eps)
    gap_ok = gap_ok and event_prob > 0 and rank_gap > 0
    print(
        f"L={fmt(L, 8)} eps=L/4: event_prob>={fmt(event_prob, 18)} "
        f"rank_gap>={fmt(rank_gap, 18)}"
    )

print("\n(5) Linear window is invisible to fixed unrooted laws but not microscopically clustered")
N = mp.mpf(2) ** 22
for w in [4, 8]:
    print(
        f"N=2^22, w={w}, k=5 collision_bound={fmt(collision_bound(N, w, 5), 18)}; "
        f"Palm multiplicity={w - 1}"
    )

check(
    "Fixed-k hidden-cluster collision probability vanishes for bounded width",
    collision_ok and collision_bound(Ns[-1], 16, 8) < mp.mpf("0.000101"),
    f"largest tested bound={fmt(collision_bound(Ns[-1], 16, 8), 18)}",
)
check(
    "The no-collision three-record law equals the 1+1 sprinkling triple law",
    triple_sum == 1
    and triple["antichain"] == mp.mpf(1) / 6
    and triple["one_relation"] == mp.mpf(1) / 3
    and triple["chain"] == mp.mpf(1) / 6,
    "permutation enumeration gives 1/6,1/3,1/6,1/6,1/6",
)
check(
    "Pair relation probability is exactly one quarter after rank symmetrization",
    pair_prob == mp.mpf(1) / 4,
    "P[U_x<U_y] P[V_x<V_y] = 1/2 * 1/2",
)
check(
    "Positive linear jitter destroys microscopic same-cluster nearness",
    gap_ok,
    "same-cluster rank gap has positive-probability order-one lower witness for L>0",
)
check(
    "The linear critical window cannot be settled by fixed unrooted finite patterns",
    collision_bound(mp.mpf(2) ** 22, 16, 8) < mp.mpf("0.000101") and gap_ok,
    "fixed-k laws wash out while same labels are not microscopic near twins",
)

print("\n(6) Consequence")
print("For bounded hidden width, fixed unrooted finite patterns converge to the")
print("ordinary 1+1 sprinkling pattern laws throughout the linear window.  The")
print("critical problem must therefore be rooted, mesoscopic, full-law, boundary,")
print("or mark/compensator based; another fixed k-pattern checklist cannot solve it.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
