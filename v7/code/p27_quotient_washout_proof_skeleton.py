#!/usr/bin/env python3
"""
Paper 27 receipt: quotient-level washout proof attempt and fallback ledger.

The previous Paper 27 receipts narrowed the problem to this exact fork:

  1. Prove quotient-level washout for bounded-width linear-window clusters.
  2. If that fails, find a stable rare unlabeled order class.
  3. If that fails, find an unlabeled Palm/Mecke/bracket residue.

This receipt does not pretend to prove the missing theorem.  It records the
strongest conditional theorem currently available, identifies the exact missing
local factor lemma, and then follows the two fallbacks with high-precision
scaling checks.  All asserted non-integer arithmetic uses mpmath with dps=140.
"""

import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140


def fmt(x, n=32):
    return mp.nstr(x, n)


checks = []
open_items = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def open_item(name, detail):
    open_items.append((name, detail))
    print(f"[OPEN] {name} {detail}")


def A(z, c):
    """Antiderivative of P(E <= z), E uniform[-c,c]."""
    z = mp.mpf(z)
    c = mp.mpf(c)
    if z <= -c:
        return mp.mpf(0)
    if z < c:
        return (z + c) ** 2 / (4 * c)
    return z


def B_anti(z, c):
    """Antiderivative of A(z,c), continuous at +-c."""
    z = mp.mpf(z)
    c = mp.mpf(c)
    if z <= -c:
        return mp.mpf(0)
    if z < c:
        return (z + c) ** 3 / (12 * c)
    return z**2 / 2 + c**2 / 6


def marginal_cdf(x, c):
    """CDF of X=S+E, S uniform[0,1], E uniform[-c,c]."""
    return A(x, c) - A(mp.mpf(x) - 1, c)


def G(x, c):
    """Antiderivative of marginal_cdf(x,c)."""
    return B_anti(x, c) - B_anti(mp.mpf(x) - 1, c)


def conditional_rank_mean(s, c):
    """M_c(s)=E[F_c(S+E)|S=s]."""
    s = mp.mpf(s)
    c = mp.mpf(c)
    return (G(s + c, c) - G(s - c, c)) / (2 * c)


def split_points(c):
    c = mp.mpf(c)
    points = {mp.mpf(0), mp.mpf(1)}
    for value in [2 * c, 1 - 2 * c]:
        if 0 < value < 1:
            points.add(+value)
    return sorted(points)


def sibling_bracket(c):
    """B(c)=Var(E[F_c(S+E)|S]) for two siblings sharing S."""
    c = mp.mpf(c)
    total = mp.mpf(0)
    points = split_points(c)
    for left, right in zip(points[:-1], points[1:]):
        total += mp.quad(lambda s: (conditional_rank_mean(s, c) - mp.mpf("0.5")) ** 2, [left, right])
    return +total


def sibling_pair_fraction(N, width):
    return (mp.mpf(width) - 1) / (mp.mpf(N) - 1)


def hidden_sibling_pair_count(N, width):
    """Number of hidden sibling pairs for N records split into width-blocks."""
    return mp.mpf(N) * (mp.mpf(width) - 1) / 2


def random_pair_bracket(N, width, c):
    """Marked sibling bracket diluted by the chance an unrooted pair is hidden siblings."""
    return sibling_pair_fraction(N, width) * sibling_bracket(c)


def subsqrt_collision_bound(N, beta, width):
    k = mp.floor(mp.mpf(N) ** mp.mpf(beta))
    return k, mp.binomial(k, 2) * sibling_pair_fraction(N, width)


def sqrt_collision_mean(a, width):
    return mp.mpf(a) ** 2 * (mp.mpf(width) - 1) / 2


def conditional_diagonal_second_moment_bound(N, width, K):
    """
    Algebraic consequence of the missing local factor bound.

    If each hidden-pair quotient factor has centered L2 norm at most K/N and
    nonshared factors are neutral, then the diagonal contribution is bounded by

        M_N (K/N)^2,  M_N = N(width-1)/2.
    """
    return hidden_sibling_pair_count(N, width) * (mp.mpf(K) / mp.mpf(N)) ** 2


def nonneutral_cross_bound(N, width, K, exponent):
    """
    What happens if nonshared neutrality fails and every pair cross-term has
    size comparable to (K/N^exponent)^2.
    """
    M = hidden_sibling_pair_count(N, width)
    return M * (M - 1) * (mp.mpf(K) / (mp.mpf(N) ** mp.mpf(exponent))) ** 2


print("=" * 80)
print("Paper 27 quotient-level washout proof attempt and fallback ledger")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

print("\nRoute 1. Quotient-level proof attempt")
width = 2
c = mp.mpf(1)
K = mp.mpf(4)
B1 = sibling_bracket(c)
print(f"marked sibling bracket B(1)={fmt(B1, 40)}")
print("Diluted random-pair bracket:")
pair_rows = []
for exponent in [4, 6, 8, 10, 12]:
    N = mp.mpf(10) ** exponent
    value = random_pair_bracket(N, width, c)
    pair_rows.append((N, value))
    print(f"  N=1e{exponent}: sibling_mass={fmt(sibling_pair_fraction(N, width), 18)} "
          f"pair_bracket={fmt(value, 24)}")

print("\nConditional local-factor theorem scaling:")
diag_rows = []
cross_linear_rows = []
cross_sqrt_rows = []
for exponent in [4, 6, 8, 10, 12]:
    N = mp.mpf(10) ** exponent
    diag = conditional_diagonal_second_moment_bound(N, width, K)
    cross_linear = nonneutral_cross_bound(N, width, K, 1)
    cross_sqrt = nonneutral_cross_bound(N, width, K, mp.mpf("0.5"))
    diag_rows.append((N, diag))
    cross_linear_rows.append((N, cross_linear))
    cross_sqrt_rows.append((N, cross_sqrt))
    print(
        f"  N=1e{exponent}: diagonal_if_neutral={fmt(diag, 18)} "
        f"cross_if_K/N={fmt(cross_linear, 18)} cross_if_K/sqrtN={fmt(cross_sqrt, 18)}"
    )

open_item(
    "Route 1 missing lemma M",
    "Prove the projected hidden-pair quotient factor has L2 size O(1/N), "
    "and that nonshared factors are neutral after conditioning only on the unlabeled order.",
)

print("\nRoute 2. Rare-order fallback")
finite_constants = {
    "P8_largest_positive_linear": mp.mpf("0.00478171696739"),
    "N10_max_half_one_selected": mp.mpf("0.0540733337402"),
    "N12_max_selected_contribution": mp.mpf("0.0557631254196"),
    "N12_max_per_schedule_q_null_ratio": mp.mpf("1.50457317073"),
}
for name, value in finite_constants.items():
    print(f"  {name}={fmt(value, 18)}")
open_item(
    "Route 2 missing uniform selected-class bound",
    "The finite selected screens do not show a stable rare class, but they do not prove "
    "sup_N sum_C q_N(C)^2/p_N(C)=O(1) over exact selected families.",
)

print("\nRoute 3. Unlabeled bracket fallback")
for beta in [mp.mpf("0.25"), mp.mpf("0.40"), mp.mpf("0.49")]:
    N = mp.mpf(10) ** 12
    k, bound = subsqrt_collision_bound(N, beta, width)
    print(f"  sub-sqrt beta={fmt(beta, 6)} at N=1e12: k={fmt(k, 14)} collision_bound={fmt(bound, 18)}")
for a in [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2")]:
    print(f"  sqrt scale a={fmt(a, 4)} limiting_collision_mean={fmt(sqrt_collision_mean(a, width), 18)}")
open_item(
    "Route 3 remaining bracket target",
    "A random unrooted pair bracket is O(1/N), so any surviving residue must be an "
    "aggregate sparse-pair likelihood/bracket with non-neutral cycles or selected rare denominators.",
)

check(
    "Marked bracket is real but belongs to a marked refinement",
    B1 > mp.mpf("0.01"),
    f"B(1)={fmt(B1, 18)}",
)
check(
    "Random unrooted pair projection of the marked bracket decays as O(1/N)",
    all(pair_rows[i][1] > pair_rows[i + 1][1] for i in range(len(pair_rows) - 1))
    and pair_rows[-1][1] < mp.mpf("2e-14"),
    f"N=1e12 pair_bracket={fmt(pair_rows[-1][1], 18)}",
)
check(
    "Conditional local-factor theorem would force diagonal residue to vanish",
    all(diag_rows[i][1] > diag_rows[i + 1][1] for i in range(len(diag_rows) - 1))
    and diag_rows[-1][1] < mp.mpf("1e-10"),
    f"N=1e12 diagonal={fmt(diag_rows[-1][1], 18)}",
)
check(
    "If the local factor is only K/sqrt(N), cross terms can diverge",
    cross_sqrt_rows[-1][1] > cross_sqrt_rows[0][1] * mp.mpf("1e6"),
    f"N=1e4={fmt(cross_sqrt_rows[0][1], 18)} N=1e12={fmt(cross_sqrt_rows[-1][1], 18)}",
)
check(
    "Finite rare-order receipts do not currently show a large individual selected residue",
    finite_constants["P8_largest_positive_linear"] < mp.mpf("0.01")
    and finite_constants["N10_max_half_one_selected"] < mp.mpf("0.25")
    and finite_constants["N12_max_selected_contribution"] < mp.mpf("0.25"),
    f"N12 max selected={fmt(finite_constants['N12_max_selected_contribution'], 18)}",
)
check(
    "Finite aggregate selected ratio is order-one, not a divergence certificate",
    finite_constants["N12_max_per_schedule_q_null_ratio"] < mp.mpf("2"),
    f"N12 max Q/null ratio={fmt(finite_constants['N12_max_per_schedule_q_null_ratio'], 18)}",
)
check(
    "Sub-sqrt bracket tests remain asymptotically blind by collision counting",
    all(subsqrt_collision_bound(mp.mpf(10) ** 12, beta, width)[1] < mp.mpf("0.1")
        for beta in [mp.mpf("0.25"), mp.mpf("0.40")]),
    "beta=.25 and beta=.40 bounds below 0.1 at N=1e12",
)
check(
    "Square-root scale remains the first live bracket scale",
    sqrt_collision_mean(1, width) == mp.mpf("0.5"),
    f"a=1 mean={fmt(sqrt_collision_mean(1, width), 18)}",
)

print("\n=== Verdict ===")
print("Route 1 gives a conditional theorem, not a completed proof.  The exact")
print("missing step is the quotient local-factor/nonshared-neutrality lemma M.")
print("Because M is not proved here, the receipt follows routes 2 and 3.  The")
print("finite rare-order receipts still show no stable large selected residue,")
print("and the ordinary unrooted pair bracket decays as O(1/N).  Therefore the")
print("remaining enemy is very specific: a selected rare denominator or an")
print("aggregate sparse-pair bracket with non-neutral cycles.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print("\nOpen items:")
for name, detail in open_items:
    print(f"OPEN: {name}: {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
