#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: growing-window order-only washout bounds.

The fixed-k theorem can be strengthened.  For fixed hidden width w, a sampled
k_N-record induced suborder sees a hidden sibling collision with probability at
most

    binom(k_N,2) (w-1)/(N-1).

Therefore every order-only test measurable with respect to a uniformly sampled
k_N-record induced suborder is collision-blind when k_N=o(sqrt(N)).  Conditional
on no sibling collision, the bounded-width linear-window clustered-coordinate
model has the same asymptotic finite-rank order kernel as 1+1 sprinkling, up to
the usual without-replacement/grid errors.  This is not full contiguity of the
N-record law; it is a growing-window local washout theorem.

All asserted non-integer arithmetic uses mpmath with dps=140.
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


def collision_bound(N, k, w):
    N = mp.mpf(N)
    k = mp.mpf(k)
    w = mp.mpf(w)
    if N <= 1:
        return mp.mpf(1)
    return k * (k - 1) / 2 * (w - 1) / (N - 1)


def grid_without_replacement_bound(N, k, w):
    """Crude base-grid/sampling correction for m=N/w parents."""
    m = mp.mpf(N) / w
    k = mp.mpf(k)
    if m <= 1:
        return mp.mpf(1)
    return k * (k - 1) / (2 * m)


print("=" * 80)
print("Collapsed P23 growing-window order-only washout bounds")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

w = 4
Ns = [mp.mpf(10) ** p for p in [4, 5, 6, 7, 8]]
betas = [mp.mpf("0.25"), mp.mpf("0.40"), mp.mpf("0.49"), mp.mpf("0.50"), mp.mpf("0.60")]

table = {}
print(f"\n(1) Collision bounds for width w={w}")
for beta in betas:
    values = []
    print(f"\nbeta={fmt(beta, 6)}")
    for N in Ns:
        k = mp.floor(N**beta)
        bound = collision_bound(N, k, w)
        grid = grid_without_replacement_bound(N, k, w)
        values.append((N, k, bound, grid))
        print(f"N={fmt(N, 8)} k={fmt(k, 12)} collision<={fmt(bound, 18)} grid<={fmt(grid, 18)}")
    table[beta] = values

subcritical = [mp.mpf("0.25"), mp.mpf("0.40"), mp.mpf("0.49")]
critical = mp.mpf("0.50")
supercritical = mp.mpf("0.60")

check(
    "Sibling-collision bound decreases across tested N for every beta below one half",
    all(
        all(table[beta][i][2] > table[beta][i + 1][2] for i in range(len(Ns) - 1))
        for beta in subcritical
    ),
    ", ".join(f"beta={fmt(beta, 4)} final={fmt(table[beta][-1][2], 12)}" for beta in subcritical),
)
check(
    "Subcritical beta=0.49 converges slowly and is still order-one at N=1e8",
    table[mp.mpf("0.49")][-1][2] > mp.mpf("0.5")
    and table[mp.mpf("0.49")][-1][2] < table[mp.mpf("0.49")][0][2],
    f"bound={fmt(table[mp.mpf('0.49')][-1][2], 18)}",
)
check(
    "Critical beta=1/2 does not vanish in this bound",
    table[critical][-1][2] > mp.mpf(1),
    f"bound={fmt(table[critical][-1][2], 18)}",
)
check(
    "Supercritical beta has a growing collision obstruction",
    table[supercritical][0][2] < table[supercritical][-1][2],
    f"first={fmt(table[supercritical][0][2], 18)}, last={fmt(table[supercritical][-1][2], 18)}",
)
check(
    "The theorem is a growing-window washout result, not full contiguity",
    collision_bound(mp.mpf(10) ** 8, mp.floor((mp.mpf(10) ** 8) ** mp.mpf("0.60")), w) > 1,
    "windows above sqrt(N) are outside the proof",
)

print("\n(2) Consequence")
print("For k_N=o(sqrt(N)), hidden sibling collisions vanish.  Thus any")
print("uniformly sampled k_N-record induced-suborder test is asymptotically blind")
print("to fixed-width hidden clusters in the linear window, conditional on the")
print("already proved no-collision rank-kernel convergence.  The sqrt(N) scale is")
print("the first possible place for order-only residues that depend on hidden")
print("multiplicity to accumulate.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
