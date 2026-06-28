#!/usr/bin/env python3
"""
Paper 27 receipt: linear-window polymer budget.

This receipt attacks the remaining fork directly in the labeled rank-copula
model that underlies the bounded-width linear hidden-cluster adversary.

Let A_N(c) be the density-matched one-axis copula excess after zero-row
projection.  The previous rank-copula receipt gives the same-hidden-pair
two-axis excess

    A_N(c)^2 / d_N,        d_N = N(N-3)/2.

For width two there are M=N/2 hidden pairs, so the first same-pair budget is

    M A_N(c)^2 / d_N.

For disjoint hidden pairs, let rho_r be the disjoint r-factor residue of the
zero-row one-axis factor g_e.  The truncated polymer budget is

    B_N^{(R)}(c)
      =
      M A_N(c)^2/d_N
      + sum_{r=2}^R binom(M,r) rho_r(c)^2.

This is not the unlabeled second moment S_N and not an asymptotic proof.  It is
a hostile finite check of the most likely washout mechanism:

  * if B_N^{(R)} stays small and the r-cycle tail decreases, ordinary polymer
    terms are not the visible obstruction;
  * if it grows, the washout theorem is probably false or missing a regularity
    hypothesis;
  * if it stays small, the remaining enemy is a quotient/unlabeled rare class or
    an all-orders polymer effect, not the first few local factors.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from collections import defaultdict
import math
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


def A_anti(z, c):
    z = mp.mpf(z)
    c = mp.mpf(c)
    if z <= -c:
        return mp.mpf(0)
    if z < c:
        return (z + c) ** 2 / (4 * c)
    return z


def marginal_cdf(x, c):
    return A_anti(x, c) - A_anti(mp.mpf(x) - 1, c)


def legendre_nodes(n, left, right):
    xs, ws = mp.gauss_quadrature(n, "legendre")
    mid = (mp.mpf(left) + mp.mpf(right)) / 2
    half = (mp.mpf(right) - mp.mpf(left)) / 2
    return [(mid + half * xs[i], half * ws[i]) for i in range(n)]


def clamp_unit(x):
    if x < 0:
        return mp.mpf(0)
    if x > 1:
        return mp.mpf(1)
    return x


def rank_kernel_values(n, low, high):
    between = high - low
    above = 1 - high
    fact = mp.mpf(math.factorial(n - 2))
    out = []
    for a in range(n - 1):
        low_pow = low**a
        for b in range(a + 1, n):
            coeff = fact / (
                mp.mpf(math.factorial(a))
                * mp.mpf(math.factorial(b - a - 1))
                * mp.mpf(math.factorial(n - 1 - b))
            )
            value = coeff * low_pow * (between ** (b - a - 1)) * (above ** (n - 1 - b))
            out.append((a, b, value))
    return out


def q_axis_matrix(n, c, nodes):
    c = mp.mpf(c)
    s_nodes = legendre_nodes(nodes, 0, 1)
    e0_nodes = legendre_nodes(nodes, -c, c)
    e1_nodes = legendre_nodes(nodes + 1, -c, c)
    matrix = [[mp.mpf(0) for _ in range(n)] for _ in range(n)]
    density_factor = 1 / (4 * c * c)
    for s, ws in s_nodes:
        for e0, we0 in e0_nodes:
            r0 = clamp_unit(marginal_cdf(s + e0, c))
            for e1, we1 in e1_nodes:
                r1 = clamp_unit(marginal_cdf(s + e1, c))
                weight = ws * we0 * we1 * density_factor
                if r0 < r1:
                    for a, b, value in rank_kernel_values(n, r0, r1):
                        matrix[a][b] += weight * value
                elif r1 < r0:
                    for b, a, value in rank_kernel_values(n, r1, r0):
                        matrix[a][b] += weight * value
    return matrix


def offdiag_sum(matrix):
    n = len(matrix)
    return mp.fsum(matrix[i][j] for i in range(n) for j in range(n) if i != j)


def sym_normalize_project(matrix):
    n = len(matrix)
    sym = [[mp.mpf(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                sym[i][j] = (matrix[i][j] + matrix[j][i]) / 2
    total = offdiag_sum(sym)
    for i in range(n):
        for j in range(n):
            if i != j:
                sym[i][j] /= total

    m = mp.mpf(n) * (n - 1)
    u = 1 / m
    delta = [[mp.mpf(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                delta[i][j] = sym[i][j] - u

    row = [mp.fsum(delta[i][j] for j in range(n) if i != j) for i in range(n)]
    total_row = mp.fsum(row)
    correction_constant = -total_row / ((n - 2) * (n - 1))
    corrected_delta = [[mp.mpf(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                h = (row[i] + row[j]) / (n - 2) + correction_constant
                corrected_delta[i][j] = delta[i][j] - h

    row_after = [
        mp.fsum(corrected_delta[i][j] for j in range(n) if i != j)
        for i in range(n)
    ]
    return corrected_delta, max(abs(value) for value in row_after)


def axis_excess(delta):
    n = len(delta)
    return mp.mpf(n) * (n - 1) * mp.fsum(
        delta[i][j] ** 2 for i in range(n) for j in range(n) if i != j
    )


def falling(n, k):
    out = mp.mpf(1)
    for value in range(k):
        out *= n - value
    return out


def pair_entries(delta):
    n = len(delta)
    scale = mp.mpf(n) * (n - 1)
    entries = []
    for i in range(n):
        for j in range(n):
            if i != j:
                entries.append(((1 << i) | (1 << j), scale * delta[i][j]))
    return entries


def disjoint_moments(delta, max_r):
    n = len(delta)
    max_possible = min(max_r, n // 2)
    entries = pair_entries(delta)
    dp = {0: mp.mpf(1)}
    out = {}
    for depth in range(1, max_possible + 1):
        next_dp = defaultdict(mp.mpf)
        for used, value in dp.items():
            for mask, edge_value in entries:
                if used & mask:
                    continue
                next_dp[used | mask] += value * edge_value
        total = mp.fsum(next_dp.values())
        out[depth] = total / falling(n, 2 * depth)
        dp = next_dp
    return out


def same_pair_budget(n, A):
    hidden_pairs = mp.mpf(n) / 2
    d_n = mp.mpf(n) * (n - 3) / 2
    return hidden_pairs * A * A / d_n


def aggregate_cycle_budget(n, r, moment):
    hidden_pairs = n // 2
    if hidden_pairs < r:
        return mp.mpf(0)
    return mp.mpf(math.comb(hidden_pairs, r)) * moment * moment


print("=" * 80)
print("Paper 27 linear-window polymer budget receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

nodes = 16
sizes = [8, 10, 12]
cs = [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2"), mp.mpf("4")]
max_r = 5
rows = []
max_row_after = mp.mpf(0)

for c in cs:
    print("\n" + "=" * 80)
    print(f"c={fmt(c, 8)}")
    print("=" * 80)
    for n in sizes:
        raw = q_axis_matrix(n, c, nodes)
        delta, row_after = sym_normalize_project(raw)
        max_row_after = max(max_row_after, row_after)
        A = axis_excess(delta)
        moments = disjoint_moments(delta, max_r)
        same = same_pair_budget(n, A)
        cycle_terms = {
            r: aggregate_cycle_budget(n, r, moments[r])
            for r in range(2, min(max_r, n // 2) + 1)
        }
        cycle_total = mp.fsum(cycle_terms.values())
        total = same + cycle_total
        same_fraction = same / total if total else mp.mpf(0)
        rows.append(
            {
                "n": n,
                "c": c,
                "A": A,
                "same": same,
                "cycle_terms": cycle_terms,
                "cycle_total": cycle_total,
                "total": total,
                "same_fraction": same_fraction,
            }
        )
        cycle_text = " ".join(
            f"r{r}={fmt(value, 12)}" for r, value in cycle_terms.items()
        )
        print(
            f"N={n} A={fmt(A, 18)} same={fmt(same, 18)} "
            f"cycles={fmt(cycle_total, 18)} total={fmt(total, 18)} "
            f"same_frac={fmt(same_fraction, 12)} {cycle_text}"
        )

max_total = max(row["total"] for row in rows)
max_total_by_c = {
    c: max(row["total"] for row in rows if row["c"] == c)
    for c in cs
}
max_cycle_share = max(row["cycle_total"] / row["total"] for row in rows)
hardest = max(rows, key=lambda row: row["total"])
max_r_tail = {
    r: max(
        row["cycle_terms"].get(r, mp.mpf(0))
        for row in rows
    )
    for r in range(2, max_r + 1)
}

print("\n=== Budget summary ===")
print(f"hardest = c={fmt(hardest['c'], 8)} N={hardest['n']} total={fmt(hardest['total'], 18)}")
print("max_total_by_c = " + ", ".join(f"c={fmt(c, 4)}:{fmt(max_total_by_c[c], 18)}" for c in cs))
print("max_cycle_terms = " + ", ".join(f"r={r}:{fmt(max_r_tail[r], 18)}" for r in range(2, max_r + 1)))
print(f"max_cycle_share = {fmt(max_cycle_share, 18)}")

check(
    "zero-row projection is enforced",
    max_row_after < mp.mpf("1e-80"),
    f"max_row_after={fmt(max_row_after, 18)}",
)
check(
    "truncated polymer budget is small in the tested linear window",
    max_total < mp.mpf("0.005"),
    f"max_total={fmt(max_total, 18)}",
)
check(
    "same-pair term dominates the tested budget",
    max_cycle_share < mp.mpf("0.15"),
    f"max_cycle_share={fmt(max_cycle_share, 18)}",
)
check(
    "cycle tail decreases after r=2 in the tested range",
    max_r_tail[2] > max_r_tail[3] > max_r_tail[4] > max_r_tail[5],
    ", ".join(f"r={r}:{fmt(max_r_tail[r], 12)}" for r in range(2, max_r + 1)),
)
check(
    "mixing window c suppresses the budget monotonically",
    max_total_by_c[mp.mpf("0.5")]
    > max_total_by_c[mp.mpf("1")]
    > max_total_by_c[mp.mpf("2")]
    > max_total_by_c[mp.mpf("4")],
    ", ".join(f"c={fmt(c, 4)}:{fmt(max_total_by_c[c], 12)}" for c in cs),
)
check(
    "hardest tested case is the least-mixed c=0.5 corner",
    hardest["c"] == mp.mpf("0.5"),
    f"hardest_c={fmt(hardest['c'], 8)} N={hardest['n']}",
)

print("\n=== Consequence ===")
print(
    "The first polymer terms do not expose a growing residue.  In the tested\n"
    "linear-window rank-copula model, the same-hidden-pair budget dominates,\n"
    "the disjoint r-cycle tail decreases rapidly after r=2, and wider mixing\n"
    "suppresses the whole budget.  This supports the washout proof path, but\n"
    "only conditionally: the true theorem still needs an all-orders cluster\n"
    "bound and a quotient-to-unlabeled argument.  If the theorem fails, the\n"
    "failure is more likely to be a selected rare-order/unlabeled-denominator\n"
    "effect than one of the first few local polymer terms."
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
