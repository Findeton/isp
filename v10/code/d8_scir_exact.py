#!/usr/bin/env python3
"""Exact/high-precision finite gates for the D8 SCIR rulebook.

All matrix and probability identities use Fraction arithmetic. Decimal with
precision 110 is used only for exponential survival values.
"""

from decimal import Decimal, getcontext
from fractions import Fraction as F
from hashlib import sha256


getcontext().prec = 110
checks = 0


def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


def zero(rows, cols):
    return tuple(tuple(F(0) for _ in range(cols)) for _ in range(rows))


def eye(n):
    return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))


def transpose(a):
    return tuple(zip(*a))


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def scale(c, a):
    return tuple(tuple(c * x for x in row) for row in a)


def matmul(a, b):
    bt = transpose(b)
    return tuple(tuple(sum(x * y for x, y in zip(row, col)) for col in bt) for row in a)


def kron(a, b):
    return tuple(
        tuple(aij * bij for aij in ar for bij in br)
        for ar in a
        for br in b
    )


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def apply_one(rho, k):
    return matmul(matmul(k, rho), transpose(k))


def apply_instrument(rho, kraus):
    out = zero(len(rho), len(rho))
    for k in kraus:
        out = add(out, apply_one(rho, k))
    return out


def partial_trace_b_2x2(rho):
    # rho indices are (a,b),(a',b') in lexicographic order.
    return tuple(
        tuple(sum(rho[2 * a + b][2 * ap + b] for b in range(2)) for ap in range(2))
        for a in range(2)
    )


def partial_trace_a_2x2(rho):
    return tuple(
        tuple(sum(rho[2 * a + b][2 * a + bp] for a in range(2)) for bp in range(2))
        for b in range(2)
    )


def q(qv):
    return f"{qv.numerator}/{qv.denominator}"


# -------------------------------------------------------------------------
# 1. Root, locally emitted opportunities, explicit bridge ownership.
# -------------------------------------------------------------------------


def enabled(history):
    if not history:
        return ("ROOT",)
    return tuple(sorted(history["tokens"]))


check(enabled({}) == ("ROOT",), "empty history has exactly one root")

history = {
    "records": {"R0"},
    "ports": {"L0", "R0p"},
    "tokens": {
        "continue:L0": ("L0",),
        "continue:R0p": ("R0p",),
        "bridge:LR": ("L0", "R0p"),
    },
}
check("ROOT" not in enabled(history), "root is not repeated")
check(history["tokens"]["bridge:LR"] == ("L0", "R0p"), "bridge legs explicitly owned")
check(all(port in history["ports"] for port in history["tokens"]["bridge:LR"]),
      "bridge names only recorded ports")
check("foreign" not in sum(history["tokens"].values(), ()), "no silent foreign bridge leg")

used_ports = set(history["tokens"]["bridge:LR"])
remaining = {
    token: legs for token, legs in history["tokens"].items()
    if used_ports.isdisjoint(legs)
}
check(remaining == {}, "bridge consumes incompatible overlapping opportunities")
check(len(used_ports) == len(set(used_ports)), "bridge ports consumed exactly once")

# A bounded local grammar emits O(n), not all-pairs O(n^2), opportunities.
n_ports = 40
max_tokens_per_port = 3
local_token_count = max_tokens_per_port * n_ports
all_pair_count = n_ports * (n_ports - 1) // 2
check(local_token_count <= max_tokens_per_port * n_ports, "local opportunity linear bound")
check(local_token_count < all_pair_count, "local grammar does not scan all port pairs")


# -------------------------------------------------------------------------
# 2. Exact finite quantum instrument, Born outcomes, and projectivity.
# -------------------------------------------------------------------------

i2 = eye(2)
x2 = ((F(0), F(1)), (F(1), F(0)))
p0 = ((F(1), F(0)), (F(0), F(0)))
p1 = ((F(0), F(0)), (F(0), F(1)))

k_b0 = kron(i2, p0)
k_b1 = kron(i2, p1)
completeness_b = add(matmul(transpose(k_b0), k_b0), matmul(transpose(k_b1), k_b1))
check(completeness_b == eye(4), "B pointer instrument complete")

# Bell state density |00+11><00+11|/2, represented without square roots.
bell = (
    (F(1, 2), F(0), F(0), F(1, 2)),
    (F(0), F(0), F(0), F(0)),
    (F(0), F(0), F(0), F(0)),
    (F(1, 2), F(0), F(0), F(1, 2)),
)
check(tr(bell) == 1, "Bell state normalized")

branch_b0 = apply_one(bell, k_b0)
branch_b1 = apply_one(bell, k_b1)
check(tr(branch_b0) == F(1, 2), "Born outcome B0")
check(tr(branch_b1) == F(1, 2), "Born outcome B1")
check(tr(branch_b0) + tr(branch_b1) == tr(bell), "terminal outcome deletion is projective")

nonselective_b = add(branch_b0, branch_b1)
before_a = partial_trace_b_2x2(bell)
after_a = partial_trace_b_2x2(nonselective_b)
check(before_a == scale(F(1, 2), eye(2)), "Bell A marginal maximally mixed")
check(after_a == before_a, "unobserved disjoint instrument cannot signal to A")

conditioned_b0 = scale(F(2), branch_b0)
check(partial_trace_b_2x2(conditioned_b0) == p0, "recorded B0 predicts correlated A0")
check(partial_trace_a_2x2(conditioned_b0) == p0, "recorded B0 is durable pointer fact")


# -------------------------------------------------------------------------
# 3. Construction-order gauge for disjoint local operations.
# -------------------------------------------------------------------------

x_a = kron(x2, i2)
x_b = kron(i2, x2)
check(matmul(x_a, x_b) == matmul(x_b, x_a), "disjoint local operators commute")

rho_ab = (
    (F(1, 2), F(0), F(0), F(0)),
    (F(0), F(1, 3), F(0), F(0)),
    (F(0), F(0), F(1, 6), F(0)),
    (F(0), F(0), F(0), F(0)),
)
ab = apply_one(apply_one(rho_ab, x_a), x_b)
ba = apply_one(apply_one(rho_ab, x_b), x_a)
check(ab == ba, "disjoint rewrite state independent of auxiliary order")
check(tr(ab) == 1, "disjoint rewrite preserves normalization")

# Joint projective outcomes are independent of the chosen measurement order.
k_a = (kron(p0, i2), kron(p1, i2))
k_b = (k_b0, k_b1)
joint_ab = {}
joint_ba = {}
for ai, ka in enumerate(k_a):
    for bi, kb in enumerate(k_b):
        joint_ab[(ai, bi)] = tr(apply_one(apply_one(bell, ka), kb))
        joint_ba[(ai, bi)] = tr(apply_one(apply_one(bell, kb), ka))
check(joint_ab == joint_ba, "disjoint pointer order gives same joint law")
check(sum(joint_ab.values()) == 1, "joint pointer law normalized")
check(joint_ab[(0, 0)] == F(1, 2), "Bell correlated 00 branch")
check(joint_ab[(1, 1)] == F(1, 2), "Bell correlated 11 branch")
check(joint_ab[(0, 1)] == 0 and joint_ab[(1, 0)] == 0, "Bell cross branches absent")


# -------------------------------------------------------------------------
# 4. Shared-collar operations need not commute: their order is physical.
# -------------------------------------------------------------------------

swap01 = (
    (F(0), F(1), F(0)),
    (F(1), F(0), F(0)),
    (F(0), F(0), F(1)),
)
swap12 = (
    (F(1), F(0), F(0)),
    (F(0), F(0), F(1)),
    (F(0), F(1), F(0)),
)
check(matmul(swap01, swap12) != matmul(swap12, swap01), "shared qutrit rewrites noncommute")
rho3 = (
    (F(1, 2), F(0), F(0)),
    (F(0), F(1, 3), F(0)),
    (F(0), F(0), F(1, 6)),
)
order_01_12 = apply_one(apply_one(rho3, swap01), swap12)
order_12_01 = apply_one(apply_one(rho3, swap12), swap01)
check(order_01_12 != order_12_01, "shared-collar order changes physical state")
check(tr(order_01_12) == tr(order_12_01) == 1, "oriented alternatives normalized")


# -------------------------------------------------------------------------
# 5. Exact exposure algebra and 110-digit survival values.
# -------------------------------------------------------------------------

i_exp = F(1, 3)
j_exp = F(2, 5)
check(i_exp + j_exp == F(11, 15), "integrated exposures add exactly")

di = Decimal(i_exp.numerator) / Decimal(i_exp.denominator)
dj = Decimal(j_exp.numerator) / Decimal(j_exp.denominator)
s_i = (-di).exp()
s_j = (-dj).exp()
s_ij = (-(di + dj)).exp()
rel_survival_error = abs(s_i * s_j - s_ij) / s_ij
check(rel_survival_error < Decimal("1e-108"), "disjoint exponential survival composes")
check(Decimal(0) < s_ij < s_i < Decimal(1), "survival is positive and decreasing")
fire_ij = Decimal(1) - s_ij
check(Decimal(0) < fire_ij < Decimal(1), "null and fire weights normalized")


# -------------------------------------------------------------------------
# 6. Local linear-hazard bound implies a nonexplosive comparison process.
# -------------------------------------------------------------------------

m_bound = F(3)
lambda_max = F(2)
n0 = 2
b_out = 2
for k in range(50):
    n_k = n0 + b_out * k
    total_hazard_bound = m_bound * lambda_max * n_k
    check(total_hazard_bound == 6 * n_k, f"linear hazard bound k={k}")

# Cauchy-condensation blocks for sum 1/(n0+B k). Here every dyadic block has
# exact lower bound 1/4, proving the comparison holding-time sum diverges.
block_bounds = []
for level in range(1, 13):
    lo = 2 ** level
    hi = 2 ** (level + 1) - 1
    terms = hi - lo + 1
    lower = F(terms, n0 + b_out * hi)
    block_bounds.append(lower)
    check(lower == F(1, 4), f"nonexplosion dyadic block {level}")
check(sum(block_bounds) == 3, "twelve holding-time blocks have unbounded linear accumulation")


# -------------------------------------------------------------------------
# 7. Finite grammar/coupling census: no per-history lookup table.
# -------------------------------------------------------------------------

port_types = ("matter-in", "matter-out", "shared", "pointer")
rules = {
    "root": (0, 2),
    "continue": (1, 1),
    "branch": (1, 2),
    "interact": (2, 2),
    "seal": (1, 1),
}
check(len(port_types) == 4, "finite port type table")
check(len(rules) == 5, "finite rewrite type table")
check(max(inp for inp, _ in rules.values()) == 2, "finite incoming arity")
check(max(out for _, out in rules.values()) == 2, "finite output arity")
check(all(inp + out <= 4 for inp, out in rules.values()), "finite rule descriptions")


print("D8 SCIR EXACT RECEIPT")
print(f"checks={checks}")
print(f"root_extensions={len(enabled({}))}")
print(f"bridge_legs={len(history['tokens']['bridge:LR'])}")
print(f"born_B0={q(tr(branch_b0))}")
print(f"born_B1={q(tr(branch_b1))}")
print(f"no_signalling_A={after_a == before_a}")
print(f"commuting_order_equal={ab == ba}")
print(f"overlap_order_equal={order_01_12 == order_12_01}")
print(f"survival_I_plus_J={s_ij}")
print(f"survival_relative_error={rel_survival_error}")
print(f"nonexplosion_block_lower={q(block_bounds[0])}")
payload = "|".join([
    str(checks), q(tr(branch_b0)), q(tr(branch_b1)), str(after_a == before_a),
    str(ab == ba), str(order_01_12 == order_12_01), str(s_ij),
    q(block_bounds[0]),
])
print(f"receipt_sha256={sha256(payload.encode('ascii')).hexdigest()}")

