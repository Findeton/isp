#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: square-root collision Poisson law.

The growing-window theorem proved washout for sampled k_N=o(sqrt(N)) induced
suborders.  The next scale is k_N=a sqrt(N).  At that scale hidden sibling
collisions no longer vanish; they form an order-one rare-collision field.

For N=m w records partitioned into m hidden clusters of fixed width w, let C_N
be the number of same-hidden-cluster record pairs in a uniformly sampled
k-record subset.  Then

    E C_N = binom(k,2) (w-1)/(N-1) -> a^2 (w-1)/2

when k=floor(a sqrt(N)).  The exact no-collision probability is

    P(C_N=0) = product_{i=0}^{k-1} (N-i w)/(N-i),

and the second factorial moment tends to lambda^2, so the first obstruction at
the square-root scale is a Poisson rare-collision field.

This is still marked: it says when hidden sibling collisions become numerous
enough to matter.  It does not prove they are observable from the order after
the hidden partition is forgotten.

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


def falling(x, r):
    x = mp.mpf(x)
    out = mp.mpf(1)
    for i in range(r):
        out *= x - i
    return out


def choose(n, r):
    return mp.binomial(mp.mpf(n), r)


def no_collision_probability(N, k, w):
    N = mp.mpf(N)
    k = int(k)
    w = mp.mpf(w)
    out = mp.mpf(1)
    for i in range(k):
        out *= (N - i * w) / (N - i)
    return +out


def collision_mean(N, k, w):
    N = mp.mpf(N)
    k = mp.mpf(k)
    w = mp.mpf(w)
    return choose(k, 2) * (w - 1) / (N - 1)


def collision_second_factorial(N, k, w):
    """Exact E[C_N(C_N-1)] for hidden sibling-pair count."""
    N = mp.mpf(N)
    k = mp.mpf(k)
    w = int(w)
    m = N / w
    hidden_pairs_per_cluster = choose(w, 2)

    # Ordered pairs of distinct hidden sibling-pairs.
    # If two sibling-pairs overlap in one record, their union has size 3.
    overlap_ordered = m * 6 * choose(w, 3)

    # If they are disjoint, their union has size 4.  This includes disjoint
    # pairs inside one hidden cluster and pairs from two different clusters.
    same_cluster_disjoint_ordered = m * 6 * choose(w, 4)
    different_cluster_ordered = m * (m - 1) * hidden_pairs_per_cluster**2

    return (
        overlap_ordered * falling(k, 3) / falling(N, 3)
        + (same_cluster_disjoint_ordered + different_cluster_ordered)
        * falling(k, 4)
        / falling(N, 4)
    )


def poisson_limit_lambda(a, w):
    return mp.mpf(a) ** 2 * (mp.mpf(w) - 1) / 2


print("=" * 80)
print("Collapsed P23 square-root collision Poisson law")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

w = 4
Ns = [mp.mpf(10) ** 4, mp.mpf(10) ** 6, mp.mpf(10) ** 8]
amplitudes = [mp.mpf("0.5"), mp.mpf("1.0"), mp.mpf("1.5")]

rows = []
print(f"\n(1) Exact critical collision law for width w={w}")
for a in amplitudes:
    print(f"\na={fmt(a, 6)}")
    limit_lam = poisson_limit_lambda(a, w)
    for N in Ns:
        k = int(mp.floor(a * mp.sqrt(N)))
        mean = collision_mean(N, k, w)
        second = collision_second_factorial(N, k, w)
        p0 = no_collision_probability(N, k, w)
        p0_poisson = mp.e ** (-mean)
        second_ratio = second / (mean**2) if mean else mp.mpf(0)
        p0_rel = abs(p0 / p0_poisson - 1)
        rows.append((a, N, k, mean, limit_lam, second, second_ratio, p0, p0_poisson, p0_rel))
        print(
            "N={N} k={k} mean={mean} limit={limit_lam} "
            "E2/mean^2={second_ratio} P0={p0} exp(-mean)={p0_poisson} rel={p0_rel}".format(
                N=fmt(N, 10),
                k=k,
                mean=fmt(mean, 18),
                limit_lam=fmt(limit_lam, 18),
                second_ratio=fmt(second_ratio, 18),
                p0=fmt(p0, 18),
                p0_poisson=fmt(p0_poisson, 18),
                p0_rel=fmt(p0_rel, 8),
            )
        )

last_by_a = {a: [row for row in rows if row[0] == a][-1] for a in amplitudes}

check(
    "The square-root mean tends to lambda=a^2(w-1)/2",
    all(abs(row[3] - row[4]) < mp.mpf("0.001") for row in last_by_a.values()),
    ", ".join(
        f"a={fmt(a, 4)} mean={fmt(row[3], 12)} limit={fmt(row[4], 12)}"
        for a, row in last_by_a.items()
    ),
)
check(
    "The second factorial moment is Poisson-like at the largest tested N",
    all(abs(row[6] - 1) < mp.mpf("0.002") for row in last_by_a.values()),
    ", ".join(f"a={fmt(a, 4)} E2/mean^2={fmt(row[6], 12)}" for a, row in last_by_a.items()),
)
check(
    "The exact no-collision probability is asymptotic to exp(-lambda)",
    all(row[9] < mp.mpf("0.002") for row in last_by_a.values()),
    ", ".join(f"a={fmt(a, 4)} rel={fmt(row[9], 12)}" for a, row in last_by_a.items()),
)
check(
    "The critical field is order-one, unlike the o(sqrt(N)) washout field",
    last_by_a[mp.mpf("1.0")][3] > 1 and last_by_a[mp.mpf("1.0")][7] < mp.mpf("0.3"),
    f"a=1 mean={fmt(last_by_a[mp.mpf('1.0')][3], 18)} P0={fmt(last_by_a[mp.mpf('1.0')][7], 18)}",
)
check(
    "This law is marked and therefore only locates the possible order-only residue scale",
    True,
    "hidden sibling collisions become Poisson at k=a sqrt(N), but observability is separate",
)

print("\n(2) Consequence")
print("Below sqrt(N), hidden sibling collisions vanish.  At k=a sqrt(N), they")
print("converge to a Poisson field with lambda=a^2(w-1)/2.  Therefore an")
print("order-only separation, if it exists, must either project this rare-collision")
print("field into the order or use an even more global Palm/Mecke/bracket identity.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
