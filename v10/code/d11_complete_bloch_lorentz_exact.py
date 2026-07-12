#!/usr/bin/env python3
"""D11 exact globally raced Bloch-Lorentz packet and bounded path kernel.

All theorem-critical calculations use Q(sqrt(2), i) exactly. Decimal is used
only to order exact algebraic positivity witnesses whose signs are separated
from zero by a disclosed margin.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from decimal import Decimal, getcontext
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import cos, pi, sin, sqrt


getcontext().prec = 120
CHECKS = 0
EXPECTED_CHECKS = 73


def check(condition, label):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1
    print(f"PASS {CHECKS:03d}: {label}")


@dataclass(frozen=True)
class Q2:
    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def make(x):
        if isinstance(x, Q2):
            return x
        return Q2(F(x), F(0))

    def __add__(self, other):
        other = Q2.make(other)
        return Q2(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-Q2.make(other))

    def __rsub__(self, other):
        return Q2.make(other) - self

    def __mul__(self, other):
        other = Q2.make(other)
        return Q2(self.a * other.a + 2 * self.b * other.b,
                  self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = Q2.make(other)
        den = other.a * other.a - 2 * other.b * other.b
        if den == 0:
            raise ZeroDivisionError
        return Q2((self.a * other.a - 2 * self.b * other.b) / den,
                  (self.b * other.a - self.a * other.b) / den)

    def dec(self):
        return (Decimal(self.a.numerator) / Decimal(self.a.denominator)
                + Decimal(self.b.numerator) / Decimal(self.b.denominator)
                * Decimal(2).sqrt())

    def sign(self):
        """Exact sign of a+b*sqrt(2), with no decimal ordering."""
        if self.a == 0:
            return (self.b > 0) - (self.b < 0)
        if self.b == 0:
            return (self.a > 0) - (self.a < 0)
        if self.a > 0 and self.b > 0:
            return 1
        if self.a < 0 and self.b < 0:
            return -1
        if self.a > 0:  # b < 0
            return 1 if self.a * self.a > 2 * self.b * self.b else -1
        # a < 0 < b; equality cannot occur for nonzero rationals.
        return 1 if 2 * self.b * self.b > self.a * self.a else -1

    def __lt__(self, other):
        return (self - Q2.make(other)).sign() < 0

    def __le__(self, other):
        return (self - Q2.make(other)).sign() <= 0


@dataclass(frozen=True)
class C2:
    re: Q2 = Q2()
    im: Q2 = Q2()

    @staticmethod
    def make(x):
        if isinstance(x, C2):
            return x
        if isinstance(x, Q2):
            return C2(x, Q2())
        return C2(Q2.make(x), Q2())

    def __add__(self, other):
        other = C2.make(other)
        return C2(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return C2(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-C2.make(other))

    def __rsub__(self, other):
        return C2.make(other) - self

    def __mul__(self, other):
        other = C2.make(other)
        return C2(self.re * other.re - self.im * other.im,
                  self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = C2.make(other)
        den = other.re * other.re + other.im * other.im
        if den == Q2():
            raise ZeroDivisionError
        return C2((self.re * other.re + self.im * other.im) / den,
                  (self.im * other.re - self.re * other.im) / den)

    def conj(self):
        return C2(self.re, -self.im)


ZERO = C2()
ONE = C2.make(1)
II = C2(Q2(), Q2.make(1))
INV_ROOT2 = Q2(F(0), F(1, 2))
check((Q2(F(3), F(-2))).sign() > 0 and
      (Q2(F(-3), F(2))).sign() < 0 and Q2().sign() == 0,
      "Q(sqrt(2)) ordering uses exact rational square comparisons")


def matrix(rows):
    return tuple(tuple(C2.make(x) for x in row) for row in rows)


def zeros(rows, cols):
    return matrix([[0 for _ in range(cols)] for _ in range(rows)])


def eye(n):
    return matrix([[1 if i == j else 0 for j in range(n)] for i in range(n)])


def dagger(a):
    return tuple(tuple(a[j][i].conj() for j in range(len(a)))
                 for i in range(len(a[0])))


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def neg(a):
    return tuple(tuple(-x for x in row) for row in a)


def sub(a, b):
    return add(a, neg(b))


def scale(c, a):
    c = C2.make(c)
    return tuple(tuple(c * x for x in row) for row in a)


def mul(a, b):
    bt = tuple(zip(*b))
    return tuple(tuple(sum((x * y for x, y in zip(row, col)), ZERO)
                       for col in bt) for row in a)


def tr(a):
    return sum((a[i][i] for i in range(len(a))), ZERO)


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def inv2(a):
    det = det2(a)
    return matrix(((a[1][1] / det, -a[0][1] / det),
                   (-a[1][0] / det, a[0][0] / det)))


def kron(a, b):
    return tuple(tuple(aij * bij for aij in ar for bij in br)
                 for ar in a for br in b)


def push(k, rho):
    return mul(mul(k, rho), dagger(k))


def probability(rho, effect):
    value = tr(mul(effect, rho))
    if value.im != Q2():
        raise AssertionError("probability not real")
    return value.re


def normalized(branch):
    p = tr(branch)
    if p.im != Q2() or p.re == Q2():
        raise ValueError("branch has nonpositive/complex weight")
    return scale(C2.make(Q2.make(1) / p.re), branch), p.re


def partial_trace_b(rho):
    return tuple(tuple(sum((rho[2 * a + b][2 * ap + b] for b in range(2)), ZERO)
                       for ap in range(2)) for a in range(2))


def partial_trace_a(rho):
    return tuple(tuple(sum((rho[2 * a + b][2 * a + bp] for a in range(2)), ZERO)
                       for bp in range(2)) for b in range(2))


def is_psd2(a):
    if dagger(a) != a:
        return False
    if any(a[i][i].im != Q2() for i in range(2)):
        return False
    determinant = det2(a)
    if determinant.im != Q2():
        return False
    return a[0][0].re >= Q2() and a[1][1].re >= Q2() and determinant.re >= Q2()


I2 = eye(2)
I4 = eye(4)
X = matrix(((0, 1), (1, 0)))
Y = matrix(((0, -II), (II, 0)))
Z = matrix(((1, 0), (0, -1)))
P0 = matrix(((1, 0), (0, 0)))
P1 = matrix(((0, 0), (0, 1)))
PPLUS = scale(F(1, 2), add(I2, X))
H = scale(INV_ROOT2, matrix(((1, 1), (1, -1))))
OMEGA = C2.make(INV_ROOT2) * (ONE + II)
T = matrix(((1, 0), (0, OMEGA)))


# -------------------------------------------------------------------------
# G0: dual SL(2,C) event/effect/order-unit gauge.
# -------------------------------------------------------------------------

boost = matrix(((2, 0), (0, F(1, 2))))
rotation = scale(II, X)  # determinant one
check(det2(boost) == ONE and det2(rotation) == ONE, "frame witnesses lie in SL(2,C)")

event = add(scale(3, I2), add(X, scale(2, Z)))
effect = P0
order_unit = I2


def gauge_event(a, x):
    return mul(mul(a, x), dagger(a))


def gauge_effect(a, e):
    ai = inv2(a)
    return mul(mul(dagger(ai), e), ai)


def born_ratio(x, e, unit):
    return probability(x, e) / probability(x, unit)


event_g = gauge_event(boost, event)
effect_g = gauge_effect(boost, effect)
unit_g = gauge_effect(boost, order_unit)
check(tr(mul(effect_g, event_g)) == tr(mul(effect, event)), "event/effect pairing boost invariant")
check(tr(mul(unit_g, event_g)) == tr(mul(order_unit, event)), "normalization pairing boost invariant")
check(born_ratio(event_g, effect_g, unit_g) == born_ratio(event, effect, order_unit),
      "Born ratio boost invariant")
check(born_ratio(event_g, effect, order_unit) != born_ratio(event, effect, order_unit),
      "physical-filter/no-dual-transform control changes probability")
check(det2(event_g) == det2(event), "SL(2,C) frame preserves event Lorentz determinant")

# Endpoint-order-unit instrument covariance.
k0, k1 = P0, P1
a_in, a_out = boost, rotation
ein_g = gauge_effect(a_in, I2)
eout_g = gauge_effect(a_out, I2)
k0_g = mul(mul(a_out, k0), inv2(a_in))
k1_g = mul(mul(a_out, k1), inv2(a_in))
complete_g = add(mul(mul(dagger(k0_g), eout_g), k0_g),
                 mul(mul(dagger(k1_g), eout_g), k1_g))
check(complete_g == ein_g, "endpoint-order-unit instrument completeness gauge covariant")

# Link/path/diamond covariance with noncommuting local frames.
l_ba, l_ca, l_db, l_dc = boost, rotation, rotation, boost
path_b = mul(l_db, l_ba)
path_c = mul(l_dc, l_ca)
v_a, v_b, v_c, v_d = rotation, boost, mul(rotation, boost), mul(boost, rotation)


def gauge_link(link, target_frame, source_frame):
    return mul(mul(target_frame, link), inv2(source_frame))


gb = mul(gauge_link(l_db, v_d, v_b), gauge_link(l_ba, v_b, v_a))
gc = mul(gauge_link(l_dc, v_d, v_c), gauge_link(l_ca, v_c, v_a))
check(gb == mul(mul(v_d, path_b), inv2(v_a)), "upper link path endpoint covariant")
check(gc == mul(mul(v_d, path_c), inv2(v_a)), "lower link path endpoint covariant")
hol = mul(inv2(path_c), path_b)
hol_g = mul(inv2(gc), gb)
check(hol_g == mul(mul(v_a, hol), inv2(v_a)), "diamond holonomy conjugation covariant")
check(tr(hol_g) == tr(hol), "diamond holonomy trace frame invariant")


# -------------------------------------------------------------------------
# G1: exact SPLIT, JOIN, and SEAL instruments.
# -------------------------------------------------------------------------

def append_zero(u):
    return (
        u[0],
        (ZERO, ZERO),
        u[1],
        (ZERO, ZERO),
    )


k_h = scale(INV_ROOT2, append_zero(H))
k_t = scale(INV_ROOT2, append_zero(T))
split_complete = add(mul(dagger(k_h), k_h), mul(dagger(k_t), k_t))
check(split_complete == I2, "SPLIT H/T isometry instrument complete")

for label, k, u in (("H", k_h, H), ("T", k_t, T)):
    branch = push(k, PPLUS)
    rho_ab, weight = normalized(branch)
    check(weight == Q2.make(F(1, 2)), f"SPLIT {label} outcome weight 1/2")
    check(partial_trace_b(rho_ab) == push(u, PPLUS), f"SPLIT {label} carrier child correct")
    check(partial_trace_a(rho_ab) == P0, f"SPLIT {label} ancilla child P0")

# Partial-iSWAP at pi/4 and measured/discarded second output.
c = C2.make(INV_ROOT2)
si = II * C2.make(INV_ROOT2)
u_ps = matrix((
    (1, 0, 0, 0),
    (0, c, si, 0),
    (0, si, c, 0),
    (0, 0, 0, 1),
))
check(mul(dagger(u_ps), u_ps) == I4, "JOIN partial-iSWAP exactly unitary")
j0 = (u_ps[0], u_ps[2])
j1 = (u_ps[1], u_ps[3])
check(add(mul(dagger(j0), j0), mul(dagger(j1), j1)) == I4,
      "JOIN measure/discard instrument complete")

rho_inputs = kron(PPLUS, P0)
join_weights = []
join_outputs = []
for b, j in enumerate((j0, j1)):
    branch = push(j, rho_inputs)
    weight = tr(branch).re
    join_weights.append(weight)
    if weight != Q2():
        out, _ = normalized(branch)
        join_outputs.append((b, out))
    check(weight >= Q2(), f"JOIN outcome {b} nonnegative")
check(sum(join_weights, Q2()) == Q2.make(1), "JOIN outcome weights normalized")

def join_nonselective(rhoa, rhob):
    joint = push(u_ps, kron(rhoa, rhob))
    return partial_trace_b(joint)


out_p0 = join_nonselective(P0, P0)
out_p1 = join_nonselective(P1, P0)
check(out_p0 != out_p1, "JOIN output depends on first input")
out_b0 = join_nonselective(P0, P0)
out_b1 = join_nonselective(P0, P1)
check(out_b0 != out_b1, "JOIN output depends on second input")
check(probability(out_p0, P0) != probability(out_p1, P0),
      "JOIN transfers intervention into later seal probability")

# The intervention and witness now follow the frozen owned root history:
# root P0 versus P+, identical H split, fresh P0 sibling, then sibling merge.
owned_base = join_nonselective(push(H, P0), P0)
owned_intervention = join_nonselective(push(H, PPLUS), P0)
check(probability(owned_base, P0) != probability(owned_intervention, P0),
      "owned root intervention transfers through sibling merge to seal law")

check(add(mul(dagger(P0), P0), mul(dagger(P1), P1)) == I2,
      "SEAL projective instrument complete")
seal0 = push(P0, PPLUS)
seal1 = push(P1, PPLUS)
check(tr(seal0).re == tr(seal1).re == Q2.make(F(1, 2)), "SEAL Born weights 1/2")
check(push(P0, seal0) == seal0 and push(P1, seal1) == seal1,
      "SEAL outcomes repeat-durable")


# -------------------------------------------------------------------------
# G4/G5 algebraic common future, controls, and influence distinctions.
# -------------------------------------------------------------------------

yo = zeros(2, 2)
rhoa = push(H, P0)
rhob = P0
ya = add(yo, scale(2, rhoa))
yb = add(yo, scale(2, rhob))
yc = sub(add(ya, yb), yo)
check(sub(yc, ya) == sub(yb, yo) and is_psd2(sub(yc, ya)),
      "JOIN common future positive from left")
check(sub(yc, yb) == sub(ya, yo) and is_psd2(sub(yc, yb)),
      "JOIN common future positive from right")
yo_g, ya_g, yb_g = (gauge_event(boost, item) for item in (yo, ya, yb))
yc_g = sub(add(ya_g, yb_g), yo_g)
check(yc_g == gauge_event(boost, yc), "JOIN common-future identity boost covariant")
check(is_psd2(sub(yc_g, ya_g)) and is_psd2(sub(yc_g, yb_g)),
      "boosted JOIN remains in both algebraic futures")
naive = ya
check(not is_psd2(sub(naive, yb)), "naive endpoint-copy JOIN violates other future control")

# Carrier influence versus ancilla non-influence after SPLIT.  Construct both
# intervention worlds explicitly so the negative control is not a tautology.
carrier0 = push(T, P0)
carrier_plus = push(T, PPLUS)
ancilla0 = partial_trace_a(normalized(push(k_t, P0))[0])
ancilla_plus = partial_trace_a(normalized(push(k_t, PPLUS))[0])
check(probability(carrier0, P0) != probability(carrier_plus, P0),
      "root intervention changes carrier-child seal law")
check(ancilla0 == ancilla_plus == P0 and
      probability(ancilla0, P0) == probability(ancilla_plus, P0),
      "fresh ancilla child seal law intervention independent")

# Search an independent ancilla-branch descendant which is positivity-related
# to the carrier record but has no state dependence on the root intervention.
def evolve_word(rho, word):
    y = scale(2, P0)  # ancilla child starts here
    state = rho
    for letter in word:
        u = H if letter == "H" else T
        state = push(u, state)
        y = add(y, scale(2, state))
    return state, y


independent_witness = None
for depth in range(1, 9):
    for letters in product("HT", repeat=depth):
        state_b, pos_b = evolve_word(P0, "".join(letters))
        if is_psd2(sub(pos_b, ya)):
            independent_witness = ("".join(letters), state_b, pos_b)
            break
    if independent_witness:
        break
check(independent_witness is not None, "positivity-related branch-disjoint witness found")
word_b, state_b, pos_b = independent_witness
state_b_intervened, pos_b_intervened = evolve_word(ancilla_plus, word_b)
check(state_b == state_b_intervened and pos_b == pos_b_intervened and
      probability(state_b, P0) == probability(state_b_intervened, P0),
      "positivity-related independent branch has zero intervention influence")


# -------------------------------------------------------------------------
# G6: independent finite H/T orbit reconstruction.
# -------------------------------------------------------------------------

def projector_key(rho):
    return tuple((z.re.a, z.re.b, z.im.a, z.im.b) for row in rho for z in row)


def bloch(rho):
    values = tuple(tr(mul(rho, s)) for s in (X, Y, Z))
    if not all(value.im == Q2() for value in values):
        raise AssertionError("Bloch coordinate is not real")
    return tuple(value.re for value in values)


orbit = {projector_key(P0): P0}
orbit_counts = []
orbit_units = True
depth12_rhos = ()
for depth in range(13):
    orbit_counts.append(len(orbit))
    if depth == 12:
        depth12_rhos = tuple(orbit.values())
    orbit_units &= all(sum((x * x for x in bloch(rho)), Q2()) == Q2.make(1)
                       for rho in orbit.values())
    enlarged = dict(orbit)
    for rho in orbit.values():
        for gate in (H, T):
            child = push(gate, rho)
            enlarged[projector_key(child)] = child
    orbit = enlarged

check(orbit_units, "all independent H/T orbit directions through depth 12 are unit")
check(tuple(orbit_counts[d] for d in (0, 2, 4, 6, 8, 10, 12)) ==
      (1, 3, 8, 19, 35, 64, 113), "independent H/T orbit reproduces D10 depth counts")
check(all(b >= a for a, b in zip(orbit_counts, orbit_counts[1:])),
      "independent H/T orbit is nested")


def sampled_support(rhos, samples=50000):
    directions = [tuple(float(x.dec()) for x in bloch(rho)) for rho in rhos]
    golden = pi * (3 - sqrt(5))
    worst = 2.0
    for k in range(samples):
        z = 1 - 2 * (k + 0.5) / samples
        radius = sqrt(max(0.0, 1 - z * z))
        az = golden * k
        point = (radius * cos(az), radius * sin(az), z)
        worst = min(worst, max(sum(a * b for a, b in zip(u, point))
                               for u in directions))
    return worst


depth12_support = sampled_support(depth12_rhos)
check(abs(depth12_support - 0.914143429015) < 5e-13,
      "independent H/T depth-12 Fibonacci support reproduces D10")


# -------------------------------------------------------------------------
# G2/G3: complete typed bounded-history path law.
# -------------------------------------------------------------------------

@dataclass(frozen=True)
class Port:
    pid: str
    owner: str
    rho: tuple
    position: tuple
    parents: tuple
    order_unit: tuple
    frame_link: tuple
    status: str = "OPEN"


@dataclass(frozen=True)
class JoinOpportunity:
    jid: str
    left: str
    right: str
    anchor: str
    anchor_position: tuple
    anchor_order_unit: tuple
    anchor_frame_link: tuple


@dataclass(frozen=True)
class Token:
    tid: str
    kind: str
    owners: tuple
    anchor: str
    activity: F
    packet: tuple


@dataclass(frozen=True)
class DurableOutcome:
    oid: str
    at_record: str
    owner_ports: tuple
    rule: str
    value: str
    effect: tuple
    terminal: bool


@dataclass
class History:
    ports: dict
    joins: dict
    records: dict
    outcomes: tuple = ()

    def clone(self):
        return History(dict(self.ports), dict(self.joins), dict(self.records),
                       tuple(self.outcomes))


def root_history(rho=P0):
    port = Port("r", "root", rho, zeros(2, 2), (), I2, I2)
    return History({"r": port}, {}, {"r": (zeros(2, 2), ())})


def enabled(history):
    tokens = [Token(f"S:{pid}", "SPLIT", (pid,), pid, F(1), (k_h, k_t))
              for pid in history.ports]
    tokens += [Token(f"Q:{pid}", "SEAL", (pid,), pid, F(1), (P0, P1))
               for pid in history.ports]
    tokens += [Token(f"J:{jid}", "JOIN", (jt.left, jt.right), jt.anchor,
                     F(1), (j0, j1))
               for jid, jt in history.joins.items()
               if jt.left in history.ports and jt.right in history.ports]
    return tuple(sorted(tokens, key=lambda token: token.tid))


def invalidate(history, consumed):
    for pid in consumed:
        history.ports.pop(pid, None)
    history.joins = {
        jid: jt for jid, jt in history.joins.items()
        if jt.left not in consumed and jt.right not in consumed
    }


def split_outcomes(history, pid):
    parent = history.ports[pid]
    results = []
    for label, u in (("H", H), ("T", T)):
        child = history.clone()
        invalidate(child, {pid})
        left, right = pid + label + "L", pid + label + "R"
        rho_left = push(u, parent.rho)
        rho_right = P0
        y_left = add(parent.position, scale(2, rho_left))
        y_right = add(parent.position, scale(2, rho_right))
        child.ports[left] = Port(
            left, pid, rho_left, y_left, (pid,), parent.order_unit,
            parent.frame_link)
        child.ports[right] = Port(
            right, pid, rho_right, y_right, (pid,), parent.order_unit,
            parent.frame_link)
        child.records[left] = (y_left, (pid,))
        child.records[right] = (y_right, (pid,))
        jid = pid + label + "J"
        child.joins[jid] = JoinOpportunity(
            jid, left, right, pid, parent.position, parent.order_unit,
            parent.frame_link)
        child.outcomes += (DurableOutcome(
            pid + label + "O", pid, (pid,), "SPLIT", label,
            mul(dagger(k_h if label == "H" else k_t),
                k_h if label == "H" else k_t), False),)
        results.append((child, Q2.make(F(1, 2))))
    return results


def seal_outcomes(history, pid):
    parent = history.ports[pid]
    results = []
    for outcome, projector in ((0, P0), (1, P1)):
        p = probability(parent.rho, projector)
        if p == Q2():
            continue
        child = history.clone()
        invalidate(child, {pid})
        child.outcomes += (DurableOutcome(
            pid + f"Q{outcome}", pid, (pid,), "TERMINAL_SEAL",
            str(outcome), projector, True),)
        results.append((child, p))
    return results


def join_outcomes(history, jid):
    token = history.joins[jid]
    left, right = history.ports[token.left], history.ports[token.right]
    joint = kron(left.rho, right.rho)
    results = []
    for outcome, j in ((0, j0), (1, j1)):
        branch = push(j, joint)
        p = tr(branch).re
        if p == Q2():
            continue
        rho_out, _ = normalized(branch)
        child = history.clone()
        invalidate(child, {token.left, token.right})
        child.joins.pop(jid, None)
        pid = jid + str(outcome) + "C"
        y_out = sub(add(left.position, right.position), token.anchor_position)
        child.ports[pid] = Port(
            pid, jid, rho_out, y_out, (token.left, token.right),
            token.anchor_order_unit, token.anchor_frame_link)
        child.records[pid] = (y_out, (token.left, token.right))
        child.outcomes += (DurableOutcome(
            jid + f"O{outcome}", pid, (token.left, token.right),
            "SIBLING_MERGE", str(outcome),
            mul(dagger(j0 if outcome == 0 else j1),
                j0 if outcome == 0 else j1),
            False),)
        results.append((child, p))
    return results


def fire(history, token):
    if token.kind == "SPLIT":
        return split_outcomes(history, token.owners[0])
    if token.kind == "SEAL":
        return seal_outcomes(history, token.owners[0])
    return join_outcomes(history, token.tid[2:])


KERNEL_LOCAL_NORMALIZED = True
KERNEL_RACE_NORMALIZED = True


def next_kernel(history):
    global KERNEL_LOCAL_NORMALIZED, KERNEL_RACE_NORMALIZED
    tokens = enabled(history)
    if not tokens:
        return ((history.clone(), Q2.make(1)),)
    total_activity = sum((token.activity for token in tokens), F(0))
    rows = []
    for token in tokens:
        outcomes = fire(history, token)
        local_ok = sum((p for _, p in outcomes), Q2()) == Q2.make(1)
        KERNEL_LOCAL_NORMALIZED &= local_ok
        if not local_ok:
            raise AssertionError(f"{token.tid} conditional instrument not normalized")
        activity_share = Q2.make(token.activity / total_activity)
        rows.extend((child, activity_share * p) for child, p in outcomes)
    race_ok = sum((p for _, p in rows), Q2()) == Q2.make(1)
    KERNEL_RACE_NORMALIZED &= race_ok
    if not race_ok:
        raise AssertionError("enabled-token race plus outcomes not normalized")
    return tuple(rows)


root = root_history()
check(tuple((token.kind, token.owners) for token in enabled(root)) ==
      (("SEAL", ("r",)), ("SPLIT", ("r",))), "root local tokens complete")
check(all(all(owner in root.ports for owner in token.owners)
          for token in enabled(root)), "root tokens exactly owned")
root_packets = {token.kind: token.packet for token in enabled(root)}
check(all(token.activity == F(1) for token in enabled(root)) and
      root_packets == {"SPLIT": (k_h, k_t), "SEAL": (P0, P1)},
      "root tokens carry activity and actual instrument matrices")

levels = [((root, Q2.make(1)),)]
for cutoff in range(1, 4):
    rows = []
    for history, mass in levels[-1]:
        rows.extend((child, mass * p) for child, p in next_kernel(history))
    check(sum((mass for _, mass in rows), Q2()) == Q2.make(1),
          f"cutoff-{cutoff} finite-prefix mass normalized")
    check(all(all(port.status == "OPEN" for port in history.ports.values())
              for history, _ in rows), f"cutoff-{cutoff} only open ports enabled")
    check(all(all(jt.left in history.ports and jt.right in history.ports
                      for jt in history.joins.values())
              for history, _ in rows), f"cutoff-{cutoff} no stale/silent join legs")
    levels.append(tuple(rows))

check(KERNEL_LOCAL_NORMALIZED, "all enumerated conditional instruments normalized")
check(KERNEL_RACE_NORMALIZED, "all enumerated activity races give normalized next law")
check(all(isinstance(outcome, DurableOutcome) and
          ((outcome.rule == "SPLIT" and outcome.value in ("H", "T") and
            len(outcome.effect) == 2 and
            outcome.effect == scale(F(1, 2), I2)) or
           (outcome.rule == "TERMINAL_SEAL" and len(outcome.effect) == 2 and
            outcome.effect == (P0 if outcome.value == "0" else P1)) or
           (outcome.rule == "SIBLING_MERGE" and len(outcome.effect) == 4 and
            outcome.effect == mul(dagger(j0 if outcome.value == "0" else j1),
                                  j0 if outcome.value == "0" else j1)))
          for level in levels for history, _ in level for outcome in history.outcomes),
      "all committed outcomes carry correct typed input-space effects")
check(tr(mul(scale(F(1, 2), I2), PPLUS)).re == Q2.make(F(1, 2)) and
      all(tr(mul(mul(dagger(j), j), rho_inputs)).re == weight
          for j, weight in zip((j0, j1), join_weights)) and
      tr(mul(P0, PPLUS)).re == tr(mul(P1, PPLUS)).re == Q2.make(F(1, 2)),
      "typed outcome effects reconstruct SPLIT/MERGE/SEAL Born weights")
check(all(all(owner not in history.ports for owner in outcome.owner_ports)
          for level in levels for history, _ in level for outcome in history.outcomes
          if outcome.terminal), "terminal seals consume every recorded owner port")
check(any({outcome.rule for outcome in history.outcomes} >=
          {"SPLIT", "TERMINAL_SEAL"}
          for history, _ in levels[2]),
      "continuing transition outcomes and terminal seals remain distinctly typed")

# Split root, then execute disjoint splits on its two children in both orders.
h_split = split_outcomes(root, "r")[0][0]
left0, right0 = sorted(h_split.ports)


def deterministic_split(history, pid, label):
    return split_outcomes(history, pid)[0 if label == "H" else 1][0]


lr = deterministic_split(deterministic_split(h_split, left0, "H"), right0, "T")
rl = deterministic_split(deterministic_split(h_split, right0, "T"), left0, "H")


def split_schedule_probability(history, schedule):
    probability_mass = Q2.make(1)
    current = history
    for pid, label in schedule:
        tokens = enabled(current)
        token = next(item for item in tokens
                     if item.kind == "SPLIT" and item.owners == (pid,))
        total = sum((item.activity for item in tokens), F(0))
        probability_mass *= Q2.make(token.activity / total) * Q2.make(F(1, 2))
        current = deterministic_split(current, pid, label)
    return current, probability_mass


_, p_lr = split_schedule_probability(h_split, ((left0, "H"), (right0, "T")))
_, p_rl = split_schedule_probability(h_split, ((right0, "T"), (left0, "H")))


def canonical(history):
    ports = tuple(sorted((pid, port.owner, port.rho, port.position, port.parents,
                          port.order_unit, port.frame_link)
                         for pid, port in history.ports.items()))
    joins = tuple(sorted((jid, jt.left, jt.right, jt.anchor, jt.anchor_position,
                          jt.anchor_order_unit, jt.anchor_frame_link)
                         for jid, jt in history.joins.items()))
    records = tuple(sorted(history.records.items()))
    # Disjoint auxiliary order is removed by sorting committed records.
    outcomes = tuple(sorted((o.oid, o.at_record, o.owner_ports, o.rule,
                             o.value, o.effect, o.terminal)
                            for o in history.outcomes))
    return ports, joins, records, outcomes


check(canonical(lr) == canonical(rl), "disjoint SPLIT schedules have same canonical history")
check(p_lr == p_rl == Q2.make(F(1, 140)),
      "disjoint SPLIT schedules have equal exact presentation probability")
join_id = next(iter(h_split.joins))
join_first = join_outcomes(h_split, join_id)[0][0]
check(next(iter(join_first.ports.values())).parents == tuple(sorted((left0, right0))),
      "sibling merge output retains both parent ports explicitly")
split_first = deterministic_split(h_split, left0, "H")
check(join_id not in split_first.joins, "overlapping SPLIT invalidates sibling JOIN")
check(canonical(join_first) != canonical(split_first), "overlapping JOIN/SPLIT order is physical")

# All recorded ancestry displacements in bounded histories are positive.
def ancestry_edges_positive(history):
    for rid, (position, parents) in history.records.items():
        for parent in parents:
            parent_position = history.records[parent][0]
            if not is_psd2(sub(position, parent_position)):
                return False
    return True


check(all(ancestry_edges_positive(history) for level in levels for history, _ in level),
      "all exhaustively enumerated ancestry edges lie in positive cone")

# Linear opportunity/output bound used by the nonexplosion comparison.
opportunity_bound = all(
    len(enabled(history)) <= 3 * max(1, len(history.ports))
    for level in levels for history, _ in level
)
check(opportunity_bound, "enabled opportunities linearly bounded by open ports")

# Equal activities imply an exact population theorem.  With p open ports and
# j enabled sibling joins there are p upward SPLIT tokens and p+j downward
# SEAL/JOIN tokens.  Since sibling joins are port-disjoint, 0 <= j <= p/2.
# The open-port count is therefore a nonnegative supermartingale, with a
# uniform seal chance at least 2/5 while nonzero.  Optional stopping at
# {0,M}, followed by the uniform bounded-region escape argument, gives almost
# sure extinction from the single root.  The finite checks below certify the
# rational identities; the stopping proof is stated in Paper 12.
population_rows = [
    (p, j, F(p, 2 * p + j), F(p + j, 2 * p + j))
    for p in range(1, 65) for j in range(0, p // 2 + 1)
]
check(all(up + down == 1 for _, _, up, down in population_rows),
      "population race probabilities normalize exactly")
check(all(up - down == -F(j, 2 * p + j)
          for p, j, up, down in population_rows),
      "open-port drift is exactly -j/(2p+j)")
check(all(F(p, 2 * p + j) >= F(2, 5)
          for p, j, _, _ in population_rows),
      "total SEAL chance is uniformly at least 2/5")
root_extinction = sum((mass for history, mass in next_kernel(root)
                       if not history.ports), Q2())
check(root_extinction == Q2.make(F(1, 2)),
      "root has exact one-half immediate-extinction probability")

if CHECKS != EXPECTED_CHECKS:
    raise AssertionError(f"expected {EXPECTED_CHECKS} checks, observed {CHECKS}")


summary = (
    "D11 GLOBALLY RACED BLOCH-LORENTZ PACKET EXACT RECEIPT\n"
    f"checks={CHECKS}\n"
    f"cutoff3_histories={len(levels[3])}\n"
    f"independent_branch_word={word_b}\n"
    f"depth12_orbit={orbit_counts[12]}\n"
    f"depth12_support={depth12_support:.12f}\n"
    "dual_sl2c_born_gauge=TEMPLATE_PASS_NOT_INTEGRATED_HISTORY\n"
    "split_sibling_merge_terminal_seal_instruments=PASS\n"
    "typed_complete_next_history_kernel=PASS\n"
    "disjoint_split_state_probability_commutation=PASS_ONE_CELL\n"
    "canonical_projective_pushforward=OPEN\n"
    "decentralized_local_click_law=OPEN\n"
    "ancestry_subset_positive_cone=PASS\n"
    "naive_join_negative_control=FIRED\n"
    "pairwise_positivity_equals_influence=FALSE\n"
    "cone_containment_is_construction_theorem=YES\n"
    "equal_activity_population=A_S_EXTINCTION_THEOREM\n"
)
print(summary, end="")
receipt = sha256(summary.encode()).hexdigest()
EXPECTED_RECEIPT = "c45eea0b4d50ec1644627a722bfa6f010f238ae581f66391eba7aeff4c32b62e"
if receipt != EXPECTED_RECEIPT:
    raise AssertionError(f"receipt drift: {receipt}")
print("receipt_sha256=" + receipt)
