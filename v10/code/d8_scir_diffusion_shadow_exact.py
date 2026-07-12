#!/usr/bin/env python3
"""Exact SCIR-to-V9 diffusion-shadow bridge.

This proves the algebraic connection between a local conservative quantum
transfer instrument and the continuous fractional leak used by the V9
round-cone builder. It does not derive the empirical coupling g.
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


def addv(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c * x for x in a)


def sumv(vectors):
    out = tuple(F(0) for _ in vectors[0])
    for vector in vectors:
        out = addv(out, vector)
    return out


def one_way_leak(victim, receiver, g):
    """Conservative split: an emitted fraction moves to the receiver."""
    emitted = scale(g, victim)
    return scale(1 - g, victim), addv(receiver, emitted)


def symmetric_partial_swap(left, right, g):
    """Classical diagonal shadow of a symmetric partial-swap channel."""
    return (
        addv(scale(1 - g, left), scale(g, right)),
        addv(scale(g, left), scale(1 - g, right)),
    )


g = F(9, 50)  # the V9 protocol point, treated here as a measured coupling
victim = (F(5), F(2), F(1), F(4))
receiver = (F(1), F(3), F(2), F(0))

v_after, r_after = one_way_leak(victim, receiver, g)
check(all(x >= 0 for x in v_after + r_after), "one-way leak remains positive")
check(addv(v_after, r_after) == addv(victim, receiver), "one-way leak conserves every channel")
check(v_after == scale(F(41, 50), victim), "victim retains one minus g")
check(r_after == addv(receiver, scale(F(9, 50), victim)), "receiver gets exactly g")

# Directional clocks decompose into monopole plus zero-sum dipole. A channelwise
# conservative leak preserves both global pieces exactly.
def monopole(x):
    return sum(x)


def centered(x):
    mean = F(sum(x), len(x))
    return tuple(v - mean for v in x)


check(monopole(v_after) + monopole(r_after) == monopole(victim) + monopole(receiver),
      "global monopole conserved")
check(addv(centered(v_after), centered(r_after)) == addv(centered(victim), centered(receiver)),
      "global dipole content conserved")


# Symmetric partial swap contracts a pair difference by exactly 1-2g.
l_after, rr_after = symmetric_partial_swap(victim, receiver, g)
before_difference = tuple(x - y for x, y in zip(victim, receiver))
after_difference = tuple(x - y for x, y in zip(l_after, rr_after))
check(after_difference == scale(1 - 2 * g, before_difference), "partial swap contracts anisotropy")
check(addv(l_after, rr_after) == addv(victim, receiver), "partial swap conserves content")
check(1 - 2 * g == F(16, 25), "g=0.18 contracts pair difference by 0.64")


# Sequential one-way leaks have the memoryless semigroup composition law.
g1, g2 = F(1, 5), F(1, 4)
zero = tuple(F(0) for _ in victim)
v1, sink1 = one_way_leak(victim, zero, g1)
v2, sink2 = one_way_leak(v1, sink1, g2)
g_eff = 1 - (1 - g1) * (1 - g2)
v_eff, sink_eff = one_way_leak(victim, zero, g_eff)
check(g_eff == F(2, 5), "leak semigroup effective coupling")
check(v2 == v_eff and sink2 == sink_eff, "two leaks equal one effective leak")


# Continuous parameterization g(s)=1-exp(-gamma*s) composes at 110 digits.
gamma = Decimal("0.73")
s = Decimal("0.31")
t = Decimal("0.47")
g_s = Decimal(1) - (-gamma * s).exp()
g_t = Decimal(1) - (-gamma * t).exp()
g_st = Decimal(1) - (-gamma * (s + t)).exp()
g_comp = Decimal(1) - (Decimal(1) - g_s) * (Decimal(1) - g_t)
semigroup_error = abs(g_st - g_comp)
check(semigroup_error < Decimal("1e-108"), "continuous leak semigroup")


# A locally scheduled chain of recorded transfer tokens propagates a mark to
# every slot; the free control never leaves its original slot.
slots = [F(0) for _ in range(8)]
slots[0] = F(1)
free = list(slots)
for i in range(7):
    emitted = g * slots[i]
    slots[i] -= emitted
    slots[i + 1] += emitted
check(sum(slots) == 1, "chain propagation conserves marked content")
check(all(x > 0 for x in slots), "recorded local transfers reach all eight slots")
check(sum(x > 0 for x in free) == 1, "free control remains on one slot")
check(sum(x > 0 for x in slots) == 8, "coupled influence support grows")


# Disjoint transfers commute; overlapping transfers record order.
state = [F(3), F(2), F(1), F(0)]


def transfer(values, source, target, coupling):
    out = list(values)
    moved = coupling * out[source]
    out[source] -= moved
    out[target] += moved
    return out


disjoint_ab = transfer(transfer(state, 0, 1, g), 2, 3, g)
disjoint_ba = transfer(transfer(state, 2, 3, g), 0, 1, g)
check(disjoint_ab == disjoint_ba, "disjoint leak tokens commute")

overlap_ab = transfer(transfer(state, 0, 1, g), 1, 2, g)
overlap_ba = transfer(transfer(state, 1, 2, g), 0, 1, g)
check(overlap_ab != overlap_ba, "overlapping leak tokens have physical order")
check(sum(overlap_ab) == sum(overlap_ba) == sum(state), "overlap orders conserve content")


print("D8 SCIR DIFFUSION SHADOW RECEIPT")
print(f"checks={checks}")
print(f"g={g.numerator}/{g.denominator}")
print(f"pair_contraction={(1 - 2 * g).numerator}/{(1 - 2 * g).denominator}")
print(f"effective_g={g_eff.numerator}/{g_eff.denominator}")
print(f"continuous_semigroup_error={semigroup_error}")
print(f"free_influence_slots={sum(x > 0 for x in free)}")
print(f"coupled_influence_slots={sum(x > 0 for x in slots)}")
payload = "|".join([
    str(checks), str(g), str(1 - 2 * g), str(g_eff),
    str(semigroup_error), str(sum(x > 0 for x in slots)),
])
print(f"receipt_sha256={sha256(payload.encode('ascii')).hexdigest()}")

