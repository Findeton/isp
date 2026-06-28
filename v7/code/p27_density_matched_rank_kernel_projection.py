#!/usr/bin/env python3
"""
Paper 27 receipt: density-matched one-pair rank kernel and unlabeled projection.

The previous Lemma M receipt found that the naive one-pair perturbation is the
wrong local object: it changes the one-record density.  The marginal-matched
Palm object is sharper.  This receipt derives its rank-level likelihood.

For one coordinate axis, let

    R = F_c(S + E),  S ~ Uniform[0,1],  E ~ Uniform[-c,c],

where F_c is the marginal CDF of S+E.  Each record has marginal R ~ Uniform[0,1].
Two hidden siblings share S but have independent E.  For N records, let
q_axis[a,b] be the probability that the two ordered siblings have coordinate
ranks a,b among all N records.

For a U-order permutation pi, the density-matched one-pair Palm law is

    q(pi) = sum_{a != b} q_axis[a,b] q_axis[pi[a],pi[b]] / (N-2)!.

This is exact over the N! permutation support once q_axis is computed.  The
receipt compares the labeled permutation second moment with the unlabeled
canonical-order second moment.  The result is deliberately allowed to go either
way: projection may erase the residue, or it may merely contract an already
small density-matched rank-copula residue.

All asserted non-integer arithmetic uses mpmath with dps=140.  The only
numerical integration is deterministic Gauss-Legendre quadrature, checked by
node-doubling convergence.
"""

from collections import Counter, defaultdict
from itertools import permutations, product
import math
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


def A(z, c):
    z = mp.mpf(z)
    c = mp.mpf(c)
    if z <= -c:
        return mp.mpf(0)
    if z < c:
        return (z + c) ** 2 / (4 * c)
    return z


def marginal_cdf(x, c):
    return A(x, c) - A(mp.mpf(x) - 1, c)


def legendre_nodes(n, left, right):
    xs, ws = mp.gauss_quadrature(n, "legendre")
    mid = (mp.mpf(left) + mp.mpf(right)) / 2
    half = (mp.mpf(right) - mp.mpf(left)) / 2
    return [(mid + half * xs[i], half * ws[i]) for i in range(n)]


def rank_kernel_values(n, low, high):
    """Conditional probabilities for ordered sibling ranks at fixed low<high."""
    out = []
    between = high - low
    above = 1 - high
    fact = mp.mpf(math.factorial(n - 2))
    for a in range(n - 1):
        for b in range(a + 1, n):
            coeff = fact / (
                mp.mpf(math.factorial(a))
                * mp.mpf(math.factorial(b - a - 1))
                * mp.mpf(math.factorial(n - 1 - b))
            )
            value = coeff * (low**a) * (between ** (b - a - 1)) * (above ** (n - 1 - b))
            out.append((a, b, value))
    return out


def clamp_unit(x):
    if x < 0:
        return mp.mpf(0)
    if x > 1:
        return mp.mpf(1)
    return x


def q_axis_matrix(n, c, nodes):
    c = mp.mpf(c)
    s_nodes = legendre_nodes(nodes, 0, 1)
    e0_nodes = legendre_nodes(nodes, -c, c)
    # Use a staggered node count for E1.  Identical tensor grids put artificial
    # positive quadrature weight on E0=E1, a measure-zero diagonal where the
    # ordered-rank formula has no contribution.
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
                else:
                    pass
    return matrix


def matrix_sum(matrix):
    return mp.fsum(mp.fsum(row) for row in matrix)


def matrix_linf_distance(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a)) if i != j)


def axis_second(matrix):
    n = len(matrix)
    return mp.mpf(n) * (n - 1) * mp.fsum(matrix[i][j] ** 2 for i in range(n) for j in range(n) if i != j)


def palm_weight_for_perm(perm, q_axis):
    n = len(perm)
    total = mp.mpf(0)
    for a in range(n):
        pa = perm[a]
        for b in range(n):
            if a == b:
                continue
            total += q_axis[a][b] * q_axis[pa][perm[b]]
    return total / mp.mpf(math.factorial(n - 2))


def exact_projection_stats(n, q_axis):
    factorial_n = mp.mpf(math.factorial(n))
    p_unlabeled_counts = Counter()
    q_unlabeled = defaultdict(mp.mpf)
    labeled_square_sum = mp.mpf(0)
    q_total = mp.mpf(0)
    for perm in permutations(range(n)):
        q = palm_weight_for_perm(perm, q_axis)
        q_total += q
        labeled_square_sum += q * q
        code = canonical_unlabeled_code(poset_from_permutation(perm))
        p_unlabeled_counts[code] += 1
        q_unlabeled[code] += q
    labeled_second = factorial_n * labeled_square_sum
    unlabeled_second = mp.mpf(0)
    top = []
    for code, count in p_unlabeled_counts.items():
        p = mp.mpf(count) / factorial_n
        q = q_unlabeled[code]
        term = q * q / p
        unlabeled_second += term
        top.append((term - p, term, p, q, code))
    top.sort(reverse=True, key=lambda row: row[0])
    return {
        "q_total": q_total,
        "labeled_second": labeled_second,
        "labeled_excess": labeled_second - 1,
        "unlabeled_second": unlabeled_second,
        "unlabeled_excess": unlabeled_second - 1,
        "support": len(p_unlabeled_counts),
        "top": top[:5],
    }


print("=" * 80)
print("Paper 27 density-matched rank-kernel projection receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

sizes = [5, 6, 7, 8]
cs = [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2")]
nodes_low = 18
nodes_high = 26
rows = {}
convergence = {}

for c in cs:
    print("\n" + "=" * 80)
    print(f"c={fmt(c, 8)}")
    print("=" * 80)
    for n in sizes:
        q_low = q_axis_matrix(n, c, nodes_low)
        q_high = q_axis_matrix(n, c, nodes_high)
        conv = matrix_linf_distance(q_low, q_high)
        convergence[(n, c)] = conv
        axis_second_value = axis_second(q_high)
        stats = exact_projection_stats(n, q_high)
        rows[(n, c)] = {
            **stats,
            "axis_second": axis_second_value,
            "axis_excess": axis_second_value - 1,
            "axis_sum": matrix_sum(q_high),
            "conv": conv,
        }
        ratio = (
            stats["unlabeled_excess"] / stats["labeled_excess"]
            if abs(stats["labeled_excess"]) > mp.mpf("1e-80")
            else mp.mpf(0)
        )
        print(
            f"N={n} support={stats['support']} axis_sum={fmt(rows[(n,c)]['axis_sum'], 20)} "
            f"axis_excess={fmt(rows[(n,c)]['axis_excess'], 18)} "
            f"labeled_excess={fmt(stats['labeled_excess'], 18)} "
            f"unlabeled_excess={fmt(stats['unlabeled_excess'], 18)} "
            f"projection_ratio={fmt(ratio, 18)} conv={fmt(conv, 8)}"
        )
        if n == 8:
            for rank, (contribution, term, p, q, code) in enumerate(stats["top"][:3]):
                print(
                    f"  top{rank}: contribution={fmt(contribution, 14)} "
                    f"p={fmt(p, 14)} q={fmt(q, 14)} code_prefix={code[:28]}"
                )

max_sum_error = max(abs(rows[(n, c)]["axis_sum"] - 1) for n in sizes for c in cs)
max_conv = max(convergence.values())
max_projection_violation = max(
    rows[(n, c)]["unlabeled_second"] - rows[(n, c)]["labeled_second"]
    for n in sizes
    for c in cs
)
max_unlabeled_n2 = max(abs((mp.mpf(n) ** 2) * rows[(n, c)]["unlabeled_excess"]) for n in sizes for c in cs)
max_unlabeled_excess_n8 = max(rows[(8, c)]["unlabeled_excess"] for c in cs)
max_ratio_n8 = max(
    rows[(8, c)]["unlabeled_excess"] / rows[(8, c)]["labeled_excess"]
    for c in cs
    if rows[(8, c)]["labeled_excess"] > 0
)

check(
    "Axis rank kernels are normalized",
    max_sum_error < mp.mpf("1e-40"),
    f"max_sum_error={fmt(max_sum_error, 18)}",
)
check(
    "Node-doubling convergence is adequate for the finite receipt",
    max_conv < mp.mpf("1e-3"),
    f"max_linf_delta={fmt(max_conv, 18)}",
)
check(
    "Labeled Palm residue is positive before quotienting",
    all(rows[(n, c)]["labeled_excess"] > 0 for n in sizes for c in cs),
    f"N8,c1 labeled_excess={fmt(rows[(8, mp.mpf('1'))]['labeled_excess'], 18)}",
)
check(
    "Unlabeled projection is an L2 contraction of the labeled likelihood",
    max_projection_violation < mp.mpf("1e-30"),
    f"max_unlabeled_minus_labeled={fmt(max_projection_violation, 18)}",
)
check(
    "At N=8 unlabeled projection contracts but does not erase the residue",
    mp.mpf("0.90") < max_ratio_n8 < mp.mpf("1.0"),
    f"max_projection_ratio_N8={fmt(max_ratio_n8, 18)}",
)
check(
    "Density-matched rank residue shrinks rapidly with mixing c",
    rows[(8, mp.mpf("2"))]["unlabeled_excess"] < rows[(8, mp.mpf("1"))]["unlabeled_excess"]
    and rows[(8, mp.mpf("1"))]["unlabeled_excess"] < rows[(8, mp.mpf("0.5"))]["unlabeled_excess"]
    and rows[(8, mp.mpf("2"))]["unlabeled_excess"] < mp.mpf("1e-6"),
    f"N8 c=.5={fmt(rows[(8, mp.mpf('0.5'))]['unlabeled_excess'], 18)} "
    f"c=1={fmt(rows[(8, mp.mpf('1'))]['unlabeled_excess'], 18)} "
    f"c=2={fmt(rows[(8, mp.mpf('2'))]['unlabeled_excess'], 18)}",
)
check(
    "Finite rank-kernel data do not prove the O(N^-1) norm bound",
    max_unlabeled_n2 > mp.mpf("0"),
    f"max_abs_N2_unlabeled_excess={fmt(max_unlabeled_n2, 18)}",
)

print("\n=== Consequence ===")
print("The density-matched one-pair Palm law has a real labeled rank residue.")
print("Canonical unlabeled projection contracts it, but only mildly in the tested")
print("N<=8 exact permutation support.  The important smallness is instead the")
print("rapid falloff of the density-matched rank-copula residue as c grows.")
print("So Lemma M should not rely on quotient projection erasing the signal; it")
print("should prove that the density-matched rank copula is already small enough,")
print("then prove nonshared-cycle neutrality.  The top projected classes remain")
print("the selected-class trail if the analytic bound fails.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
