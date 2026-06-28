#!/usr/bin/env python3
"""
Paper 27 receipt: continuous copula envelope for A_N(c).

The polymer budget shows that the same-hidden-pair term dominates the tested
linear-window residue.  That pushes the proof target to the one-axis copula
energy A_N(c).  This receipt computes the continuous copula energy

    A_infty(c) = integral (h_c(r,s)-1)^2 dr ds

for the linear-jitter model after marginal rank normalization.

Writing X=S+E, with S uniform on [0,1] and E uniform on [-c,c], let f_c be the
density of X.  If r=F_c(x) and s=F_c(y), then the copula density is

    h_c(F_c(x),F_c(y))
      =
      |[0,1] cap [x-c,x+c] cap [y-c,y+c]|
      /
      (4 c^2 f_c(x) f_c(y)).

Therefore

    A_infty(c)
      =
      integral integral
      (h_c(F_c(x),F_c(y))-1)^2 f_c(x) f_c(y) dx dy.

The finite audit suggests a simple theorem target:

    A_N(c) <= K/c^2      for c >= 1/2,

with K near 0.073.  The receipt uses a deliberately loose guard K=0.075 and
checks it against deterministic Gauss-Legendre quadrature and the audited finite
A_N values from the previous polymer receipt.

This is not a proof.  It identifies the analytic inequality that would make the
same-pair part of the hidden-cluster second moment decay like O(1/N).

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
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def density_x(x, c):
    lo = max(mp.mpf("0"), x - c)
    hi = min(mp.mpf("1"), x + c)
    return max(mp.mpf("0"), hi - lo) / (2 * c)


def sibling_overlap(x, y, c):
    lo = max(mp.mpf("0"), x - c, y - c)
    hi = min(mp.mpf("1"), x + c, y + c)
    return max(mp.mpf("0"), hi - lo)


def continuous_copula_energy(c, nodes):
    c = mp.mpf(c)
    xs, ws = mp.gauss_quadrature(nodes, "legendre")
    left = -c
    right = 1 + c
    midpoint = (left + right) / 2
    half_width = (right - left) / 2
    points = [(midpoint + half_width * xs[i], half_width * ws[i]) for i in range(nodes)]
    total = mp.mpf(0)
    for x, wx in points:
        fx = density_x(x, c)
        if fx == 0:
            continue
        for y, wy in points:
            fy = density_x(y, c)
            if fy == 0:
                continue
            h = sibling_overlap(x, y, c) / (4 * c * c * fx * fy)
            total += wx * wy * (h - 1) ** 2 * fx * fy
    return total


def same_pair_envelope(n, c, k_guard):
    d_n = mp.mpf(n) * (n - 3) / 2
    hidden_pairs = mp.mpf(n) / 2
    return hidden_pairs * (k_guard / (c * c)) ** 2 / d_n


print("=" * 80)
print("Paper 27 continuous copula envelope receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

cs = [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2"), mp.mpf("4")]
nodes_low = 120
nodes_high = 160
k_guard = mp.mpf("0.075")

finite_audit = {
    mp.mpf("0.5"): {
        8: mp.mpf("0.131757536414055987"),
        10: mp.mpf("0.153119651711777049"),
        12: mp.mpf("0.168673563454979996"),
    },
    mp.mpf("1"): {
        8: mp.mpf("0.01887222461808774"),
        10: mp.mpf("0.0235234705670740888"),
        12: mp.mpf("0.0274091808823728681"),
    },
    mp.mpf("2"): {
        8: mp.mpf("0.00203366631307430952"),
        10: mp.mpf("0.00282679074652382992"),
        12: mp.mpf("0.0036090198268960836"),
    },
    mp.mpf("4"): {
        8: mp.mpf("0.000210077603727888357"),
        10: mp.mpf("0.000348151659639670912"),
        12: mp.mpf("0.00052256303061264918"),
    },
}

rows = []
print("\n=== Continuous envelope ===")
for c in cs:
    low = continuous_copula_energy(c, nodes_low)
    high = continuous_copula_energy(c, nodes_high)
    scaled = c * c * high
    refinement = abs(high - low)
    rows.append(
        {
            "c": c,
            "low": low,
            "high": high,
            "scaled": scaled,
            "refinement": refinement,
        }
    )
    print(
        f"c={fmt(c, 8)} Ainf_{nodes_low}={fmt(low, 24)} "
        f"Ainf_{nodes_high}={fmt(high, 24)} c2A={fmt(scaled, 24)} "
        f"refine={fmt(refinement, 12)}"
    )

print("\n=== Finite A_N audit against K/c^2 ===")
finite_ratios = []
for c in cs:
    bound = k_guard / (c * c)
    for n, value in finite_audit[c].items():
        ratio = value / bound
        finite_ratios.append(ratio)
        print(
            f"c={fmt(c, 8)} N={n} A_N={fmt(value, 24)} "
            f"K/c2={fmt(bound, 24)} ratio={fmt(ratio, 12)} "
            f"same_pair_envelope={fmt(same_pair_envelope(n, c, k_guard), 18)}"
        )

scaled_values = [row["scaled"] for row in rows]
max_refinement = max(row["refinement"] for row in rows)
scaled_spread = max(scaled_values) - min(scaled_values)
max_scaled = max(scaled_values)
max_finite_ratio = max(finite_ratios)

envelope_decreases = all(
    same_pair_envelope(8, c, k_guard)
    > same_pair_envelope(10, c, k_guard)
    > same_pair_envelope(12, c, k_guard)
    for c in cs
)

check(
    "continuous quadrature refinement is stable enough for envelope audit",
    max_refinement < mp.mpf("0.0001"),
    f"max_refinement={fmt(max_refinement, 18)}",
)
check(
    "scaled continuous energies are nearly c^{-2}",
    scaled_spread < mp.mpf("0.0002"),
    f"spread={fmt(scaled_spread, 18)} values="
    + ",".join(fmt(value, 12) for value in scaled_values),
)
check(
    "loose K=0.075 guard bounds continuous c^2 A_infty",
    max_scaled < k_guard,
    f"max_c2A={fmt(max_scaled, 18)} K={fmt(k_guard, 18)}",
)
check(
    "loose K=0.075 guard bounds audited finite A_N values",
    max_finite_ratio < 1,
    f"max_finite_ratio={fmt(max_finite_ratio, 18)}",
)
check(
    "K/c^2 envelope makes same-pair budget decay like O(1/N)",
    envelope_decreases,
    "same_pair_envelope proportional to 1/(N-3) for fixed c",
)

print("\n=== Consequence ===")
print(
    "The continuous copula calculation points to a concrete analytic lemma:\n"
    "prove A_N(c) <= K/c^2 for c >= 1/2, with K about 0.073 and safely below\n"
    "0.075 in this receipt.  That lemma would force the same-hidden-pair\n"
    "contribution to the width-2 linear-window second moment to decay like\n"
    "O(1/(N c^4)).  Combined with an all-orders cycle-tail bound and the\n"
    "unlabeled quotient argument, it would close the washout side of the fork."
)

print("\n" + "=" * 80)
failed = [name for name, ok, _ in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
