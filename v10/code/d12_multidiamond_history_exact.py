#!/usr/bin/env python3
"""D12 exact multi-diamond history, gauge, projectivity, and threshold model.

This repairs the one-cell limitations identified in hostile round 1.  It uses
only Q(sqrt(2),i) and rational arithmetic.  It is a bounded exact witness plus
an induction certificate, not a claim that its coupling is nature's coupling.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from fractions import Fraction as F
from functools import reduce
from hashlib import sha256
from itertools import product


CHECKS = 0


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
        return x if isinstance(x, Q2) else Q2(F(x), F(0))

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


ZERO, ONE = C2(), C2.make(1)
HALF = C2.make(F(1, 2))
II = C2(Q2(), Q2.make(1))
ROOT_HALF = C2.make(Q2(F(0), F(1, 2)))


def matrix(rows):
    return tuple(tuple(C2.make(x) for x in row) for row in rows)


def eye(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def dagger(a):
    return tuple(tuple(a[j][i].conj() for j in range(len(a)))
                 for i in range(len(a[0])))


def mul(a, b):
    bt = tuple(zip(*b))
    return tuple(tuple(sum((x * y for x, y in zip(row, col)), ZERO)
                       for col in bt) for row in a)


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(ar, br))
                 for ar, br in zip(a, b))


def mv(a, v):
    return tuple(sum((x * y for x, y in zip(row, v)), ZERO) for row in a)


def inner(v, w):
    return sum((x.conj() * y for x, y in zip(v, w)), ZERO)


def kron(a, b):
    return tuple(tuple(x * y for x in ar for y in br)
                 for ar in a for br in b)


def projector(n, index):
    return matrix([[int(i == index and j == index) for j in range(n)]
                   for i in range(n)])


def normalize(v):
    mass = inner(v, v)
    if mass == ONE:
        return v, mass
    if mass == HALF:
        return tuple(x / ROOT_HALF for x in v), mass
    raise AssertionError(f"unlicensed exact branch mass {mass}")


I2, I4 = eye(2), eye(4)
X = matrix(((0, 1), (1, 0)))
H = matrix(((ROOT_HALF, ROOT_HALF), (ROOT_HALF, -ROOT_HALF)))
SWAP = matrix(((1, 0, 0, 0),
               (0, 0, 1, 0),
               (0, 1, 0, 0),
               (0, 0, 0, 1)))
POINTER = tuple(projector(4, k) for k in range(4))


def iswap(cosine, sine):
    c, s = C2.make(cosine), II * sine
    return matrix(((1, 0, 0, 0),
                   (0, c, s, 0),
                   (0, s, c, 0),
                   (0, 0, 0, 1)))


U_QUARTER = iswap(ROOT_HALF, ROOT_HALF)
U_HALF = iswap(0, 1)
PSI = (ZERO, ONE, ZERO, ZERO)  # |01>
CONTRAST_LEDGER = (
    (F(1), F(-1), F(0), F(0)),
    (F(0), F(1), F(-1), F(0)),
    (F(0), F(0), F(1), F(-1)),
)


@dataclass(frozen=True)
class DiamondPacket:
    name: str
    interaction: tuple
    one_diamond_history_law: tuple
    positive_history_support: tuple
    rn_contrast_ratios_on_support: tuple
    history_atoms: tuple = (0, 1, 2, 3)
    reference_measure: tuple = (F(1, 4),) * 4
    contrast_ledger: tuple = CONTRAST_LEDGER
    evidence_survival: str = "exp(-I)"
    commitment_coefficient: str = "0.609377863436006231536803371168398695428539279312854..."
    incoming_types: tuple = ("q", "q")
    outgoing_types: tuple = ("q", "q")
    lower_screen: tuple = POINTER
    upper_screen: tuple = POINTER
    order_unit: tuple = I4
    eventless_collar: bool = True


PACKET_Q = DiamondPacket("quarter-iSWAP", U_QUARTER,
                         (ZERO, HALF, HALF, ZERO),
                         (1, 2), (ONE,))
PACKET_H = DiamondPacket("half-iSWAP", U_HALF,
                         (ZERO, ZERO, ONE, ZERO),
                         (2,), ())


@dataclass(frozen=True)
class Frame:
    name: str
    basis: tuple


@dataclass(frozen=True)
class Collar:
    collar_id: str
    types: tuple
    owners: tuple
    state: tuple
    frame: Frame
    order_unit: tuple
    lower_screen: tuple
    parent_record: str | None
    opportunities: tuple
    eventless: bool
    consumed: bool


@dataclass(frozen=True)
class DurableRecord:
    record_id: str
    diamond_id: str
    packet_name: str
    value: int
    owners: tuple
    input_collar: str
    output_collar: str
    lower_frame: str
    upper_frame: str
    transport: tuple
    output_effect: tuple
    conditional_mass: C2
    terminal: bool


@dataclass(frozen=True)
class QuantumHistory:
    values: tuple
    records: tuple
    open_collar: Collar
    cylinder_mass: C2


F_I = Frame("I", I4)
F_HL = Frame("H-left", kron(H, I2))
F_HR = Frame("H-right", kron(I2, H))
F_HH = Frame("H-both", kron(H, H))
F_S = Frame("swap", SWAP)


def transformed_pointer(frame):
    return tuple(mul(frame.basis, mul(p, dagger(frame.basis))) for p in POINTER)


def root_history(frame, packet):
    state = mv(frame.basis, PSI)
    collar = Collar(
        collar_id="c0",
        types=packet.incoming_types,
        owners=("left", "right"),
        state=state,
        frame=frame,
        order_unit=I4,
        lower_screen=transformed_pointer(frame),
        parent_record=None,
        opportunities=(("INTERACT", ("left", "right")),),
        eventless=True,
        consumed=False,
    )
    return QuantumHistory((), (), collar, ONE)


def eligible(collar, packet):
    expected_opportunity = (("INTERACT", collar.owners),)
    return (not collar.consumed and collar.eventless and
            collar.types == packet.incoming_types and
            collar.owners == ("left", "right") and
            collar.opportunities == expected_opportunity and
            mul(dagger(collar.frame.basis), collar.frame.basis) == I4 and
            collar.order_unit == I4 and
            collar.lower_screen == transformed_pointer(collar.frame) and
            inner(collar.state, collar.state) == ONE)


def fire(history, diamond_index, upper_frame, packet):
    """Execute commit plus output-collar birth for every nonzero outcome."""
    if not eligible(history.open_collar, packet):
        raise ValueError("ineligible, disconnected, stale, or wrong-type collar")
    if mul(dagger(upper_frame.basis), upper_frame.basis) != I4:
        raise ValueError("upper frame lies outside the stated unitary-frame domain")
    lower_frame = history.open_collar.frame
    link = mul(upper_frame.basis,
               mul(packet.interaction, dagger(lower_frame.basis)))
    upper_pointer = transformed_pointer(upper_frame)
    evolved = mv(link, history.open_collar.state)
    out = []
    for value, effect in enumerate(upper_pointer):
        projected = mv(effect, evolved)
        mass = inner(projected, projected)
        if mass == ZERO:
            continue
        state, conditional_mass = normalize(projected)
        values = history.values + (value,)
        suffix = "".join(map(str, values))
        record_id = f"r{diamond_index}:{suffix}"
        output_id = f"c{diamond_index + 1}:{suffix}"
        record = DurableRecord(
            record_id=record_id,
            diamond_id=f"d{diamond_index}:{history.open_collar.collar_id}",
            packet_name=packet.name,
            value=value,
            owners=history.open_collar.owners,
            input_collar=history.open_collar.collar_id,
            output_collar=output_id,
            lower_frame=lower_frame.name,
            upper_frame=upper_frame.name,
            transport=link,
            output_effect=effect,
            conditional_mass=conditional_mass,
            terminal=False,
        )
        collar = Collar(
            collar_id=output_id,
            types=history.open_collar.types,
            owners=history.open_collar.owners,
            state=state,
            frame=upper_frame,
            order_unit=I4,
            lower_screen=upper_pointer,
            parent_record=record_id,
            opportunities=(("INTERACT", history.open_collar.owners),),
            eventless=True,
            consumed=False,
        )
        out.append(QuantumHistory(
            values=values,
            records=history.records + (record,),
            open_collar=collar,
            cylinder_mass=history.cylinder_mass * conditional_mass,
        ))
    return tuple(out)


def generate(frames, packet):
    levels = [(root_history(frames[0], packet),)]
    for depth in range(len(frames) - 1):
        levels.append(tuple(child for history in levels[-1]
                            for child in fire(history, depth, frames[depth + 1], packet)))
    return tuple(levels)


def level_law(level):
    return {history.values: history.cylinder_mass for history in level}


DEPTH = 4
FRAME_SEQUENCE = (F_I, F_HL, F_HR, F_HH, F_S)
baseline = generate((F_I,) * (DEPTH + 1), PACKET_Q)
framed = generate(FRAME_SEQUENCE, PACKET_Q)
baseline_half = generate((F_I,) * (DEPTH + 1), PACKET_H)
framed_half = generate(FRAME_SEQUENCE, PACKET_H)

check(mul(dagger(U_QUARTER), U_QUARTER) == I4 and
      mul(dagger(U_HALF), U_HALF) == I4,
      "both local iSWAP packets are exact unitaries")
check(PACKET_Q.history_atoms == PACKET_H.history_atoms and
      PACKET_Q.reference_measure == PACKET_H.reference_measure and
      PACKET_Q.contrast_ledger == PACKET_H.contrast_ledger and
      PACKET_Q.evidence_survival == PACKET_H.evidence_survival and
      PACKET_Q.commitment_coefficient == PACKET_H.commitment_coefficient and
      PACKET_Q.incoming_types == PACKET_H.incoming_types and
      PACKET_Q.outgoing_types == PACKET_H.outgoing_types and
      PACKET_Q.lower_screen == PACKET_H.lower_screen and
      PACKET_Q.upper_screen == PACKET_H.upper_screen and
      PACKET_Q.order_unit == PACKET_H.order_unit and
      PACKET_Q.eventless_collar == PACKET_H.eventless_collar,
      "full packets share ambient atoms, reference, ledger, evidence, commitment, screens, and types")
minor = tuple(row[:3] for row in CONTRAST_LEDGER)
minor_det = (minor[0][0] * (minor[1][1] * minor[2][2] - minor[1][2] * minor[2][1])
             - minor[0][1] * (minor[1][0] * minor[2][2] - minor[1][2] * minor[2][0])
             + minor[0][2] * (minor[1][0] * minor[2][1] - minor[1][1] * minor[2][0]))
check(len(CONTRAST_LEDGER) == 3 and
      all(sum(row, F(0)) == 0 for row in CONTRAST_LEDGER) and minor_det == 1,
      "three primitive zero-sum contrasts span four pointer atoms modulo constants")
check(all(mul(dagger(frame.basis), frame.basis) == I4
          for frame in (F_I, F_HL, F_HR, F_HH, F_S)),
      "all independently assigned vertex frames are exact unitaries")
check(tuple(level_law(baseline[1]).get((atom,), ZERO)
            for atom in PACKET_Q.history_atoms) == PACKET_Q.one_diamond_history_law and
      tuple(level_law(baseline_half[1]).get((atom,), ZERO)
            for atom in PACKET_H.history_atoms) == PACKET_H.one_diamond_history_law,
      "both packets carry and reproduce their complete one-diamond history laws")
def reconstructed_rn_packet(packet):
    support = tuple(i for i, p in enumerate(packet.one_diamond_history_law)
                    if p != ZERO)
    if support != packet.positive_history_support:
        return False
    law_total = sum((packet.one_diamond_history_law[i] for i in support), ZERO)
    ref_total = sum((C2.make(packet.reference_measure[i]) for i in support), ZERO)
    rn = tuple((packet.one_diamond_history_law[i] / law_total) /
               (C2.make(packet.reference_measure[i]) / ref_total)
               for i in support)
    expected_ratios = tuple(rn[i] / rn[-1] for i in range(len(rn) - 1))
    return packet.rn_contrast_ratios_on_support == expected_ratios


check(reconstructed_rn_packet(PACKET_Q) and reconstructed_rn_packet(PACKET_H),
      "exact support-relative RN contrast ratios reconstruct both stored history laws")
check(not reconstructed_rn_packet(replace(
          PACKET_Q, rn_contrast_ratios_on_support=(C2.make(7),))),
      "false support-relative RN coordinate is rejected")
check(not reconstructed_rn_packet(replace(
          PACKET_Q, positive_history_support=(0, 3))),
      "false positive support is rejected")
root_collar = baseline[0][0].open_collar
check(eligible(root_collar, PACKET_Q), "recorded connected root collar is locally eligible")
check(not eligible(replace(root_collar, types=("wrong", "q")), PACKET_Q),
      "wrong-type collar is locally rejected")
check(not eligible(replace(root_collar, owners=("left",)), PACKET_Q),
      "disconnected one-owner collar is locally rejected")
check(not eligible(replace(root_collar, opportunities=()), PACKET_Q),
      "collar without emitted opportunity is locally rejected")
check(not eligible(replace(root_collar, consumed=True), PACKET_Q),
      "stale consumed collar is locally rejected")
bad_screen = tuple(reversed(root_collar.lower_screen))
check(not eligible(replace(root_collar, lower_screen=bad_screen), PACKET_Q),
      "corrupted collar screen is locally rejected")
check(not eligible(replace(root_collar, order_unit=POINTER[0]), PACKET_Q),
      "corrupted collar order unit is locally rejected")
NONUNITARY = Frame("nonunitary", matrix(((2, 0, 0, 0),
                                         (0, 1, 0, 0),
                                         (0, 0, 1, 0),
                                         (0, 0, 0, 1))))
check(not eligible(replace(root_collar, frame=NONUNITARY), PACKET_Q),
      "nonunitary frame is rejected at the stated unitary-frame scope")
try:
    fire(baseline[0][0], 0, NONUNITARY, PACKET_Q)
    upper_frame_rejected = False
except ValueError:
    upper_frame_rejected = True
check(upper_frame_rejected, "nonunitary newly supplied upper frame is rejected before firing")

for depth, level in enumerate(baseline):
    check(len(level) == 2 ** depth,
          f"depth {depth} explicitly contains every nonzero history")
    check(sum((h.cylinder_mass for h in level), ZERO) == ONE,
          f"depth {depth} cylinder masses normalize exactly")
    check(all(inner(h.open_collar.state, h.open_collar.state) == ONE for h in level),
          f"depth {depth} every emitted collar carries normalized state")
    if depth:
        check(all(len(h.records) == depth and
                  h.records[-1].output_collar == h.open_collar.collar_id and
                  h.open_collar.parent_record == h.records[-1].record_id and
                  h.open_collar.opportunities == (("INTERACT", ("left", "right")),) and
                  h.open_collar.eventless
                  for h in level),
              f"depth {depth} records and born collars are explicitly linked")
        check(all(not h.records[-1].terminal and
                  h.open_collar.types == ("q", "q") and
                  h.open_collar.owners == ("left", "right")
                  for h in level),
              f"depth {depth} every commit is continuing typed seal-and-birth")

# Explicit bonding maps and cylinder pushforwards at every adjacent depth.
for depth in range(1, DEPTH + 1):
    fine, coarse = level_law(baseline[depth]), level_law(baseline[depth - 1])
    pushed = {}
    for values, mass in fine.items():
        prefix = values[:-1]
        pushed[prefix] = pushed.get(prefix, ZERO) + mass
    check(pushed == coarse, f"depth {depth}->{depth - 1} prefix bonding map is projective")
    parent_by_value = {h.values: h for h in baseline[depth - 1]}
    check(all(h.records[:-1] == parent_by_value[h.values[:-1]].records
              for h in baseline[depth]),
          f"depth {depth} immutable earlier records persist byte-for-byte")
    check(all(tuple(record.value for record in h.records) == h.values
              for h in baseline[depth]),
          f"depth {depth} every durable record repeat-reads its sealed value")

# Nontrivial disintegration: every positive prefix at depths 0..3 has two
# next outcomes with mass 1/2 and the conditional distribution normalizes.
for depth in range(DEPTH):
    coarse, fine = level_law(baseline[depth]), level_law(baseline[depth + 1])
    for prefix, prefix_mass in coarse.items():
        conditionals = tuple(mass / prefix_mass for values, mass in fine.items()
                             if values[:-1] == prefix)
        check(conditionals == (HALF, HALF),
              f"prefix {prefix} has exact nontrivial next-record law (1/2,1/2)")

# Induction certificate: completeness of the pointer instrument and unitarity
# make every normalized input branch sum to one; output construction preserves
# types and normalized state.  The explicit depth-4 tower checks the carrier.
pointer_sum = tuple(tuple(ZERO for _ in range(4)) for _ in range(4))
for effect in POINTER:
    pointer_sum = add(pointer_sum, effect)
check(pointer_sum == I4,
      "complete pointer identity supplies the all-depth normalization induction")
check(all(h.open_collar.types == baseline[0][0].open_collar.types
          for level in baseline for h in level),
      "output type preservation supplies the all-depth continuation induction")

# Independent vertex-frame gauge: compare every cylinder mass and final collar
# state after transporting the baseline final state by the independently chosen
# final frame.  Instruments and links were transformed at every vertex.
for depth in range(DEPTH + 1):
    base_by_value = {h.values: h for h in baseline[depth]}
    framed_by_value = {h.values: h for h in framed[depth]}
    check({v: h.cylinder_mass for v, h in base_by_value.items()} ==
          {v: h.cylinder_mass for v, h in framed_by_value.items()},
          f"depth {depth} whole cylinder law is invariant under vertex-local frames")
    target_frame = framed[depth][0].open_collar.frame.basis
    check(all(framed_by_value[v].open_collar.state ==
              mv(target_frame, base_by_value[v].open_collar.state)
              for v in base_by_value),
          f"depth {depth} output collars transport covariantly to local frame")
    expected_frames = FRAME_SEQUENCE
    check(all(record.lower_frame == expected_frames[i].name and
              record.upper_frame == expected_frames[i + 1].name and
              record.transport == mul(expected_frames[i + 1].basis,
                                      mul(PACKET_Q.interaction,
                                          dagger(expected_frames[i].basis)))
              for v, history in framed_by_value.items()
              for i, record in enumerate(history.records)),
          f"depth {depth} generated records store correct endpoint frames and links")


def complete_model_audit(packet, plain_levels, framed_levels):
    """All bounded carrier/gauge/projective invariants for one packet."""
    normalization = all(sum((h.cylinder_mass for h in level), ZERO) == ONE
                        for level in plain_levels)
    births = all(
        len(h.records) == depth and
        (depth == 0 or (
            h.records[-1].packet_name == packet.name and
            not h.records[-1].terminal and
            h.records[-1].output_collar == h.open_collar.collar_id and
            h.open_collar.parent_record == h.records[-1].record_id and
            h.open_collar.types == packet.outgoing_types and
            h.open_collar.eventless and
            bool(h.open_collar.opportunities)))
        for depth, level in enumerate(plain_levels) for h in level)
    projective = True
    for depth in range(1, len(plain_levels)):
        pushed = {}
        for values, mass in level_law(plain_levels[depth]).items():
            pushed[values[:-1]] = pushed.get(values[:-1], ZERO) + mass
        projective = projective and pushed == level_law(plain_levels[depth - 1])
    gauge = all(level_law(plain_levels[d]) == level_law(framed_levels[d])
                for d in range(len(plain_levels)))
    transported_links = all(
        record.transport == mul(FRAME_SEQUENCE[i + 1].basis,
                                mul(packet.interaction,
                                    dagger(FRAME_SEQUENCE[i].basis)))
        for level in framed_levels for history in level
        for i, record in enumerate(history.records))
    screens_units = all(
        h.open_collar.order_unit == I4 and
        len(h.open_collar.lower_screen) == len(packet.history_atoms)
        for level in framed_levels for h in level)
    return normalization, births, projective, gauge, transported_links, screens_units


for packet, plain_levels, gauge_levels in (
        (PACKET_Q, baseline, framed),
        (PACKET_H, baseline_half, framed_half)):
    audit = complete_model_audit(packet, plain_levels, gauge_levels)
    check(all(audit), f"{packet.name} is a complete bounded typed/gauge/projective model")
    check(audit == (True,) * 6,
          f"{packet.name} separately passes normalization, birth, projective, frame, link, screen gates")

law_q1, law_h1 = level_law(baseline[1]), level_law(baseline_half[1])
check(law_q1.get((1,), ZERO) == HALF and law_h1.get((1,), ZERO) == ZERO,
      "two full models disagree on the same durable record probability 1/2 versus 0")

# Construction-order gauge on two disjoint diamonds.  Two auxiliary schedules
# push to the same canonical physical fiber and probability law.  We explicitly
# refuse to sum duplicate presentations as distinct physical histories.
PSI2 = tuple(x * y for x in PSI for y in PSI)


def disjoint_schedule(order, interaction):
    ua, ub = kron(interaction, I4), kron(I4, interaction)
    law = {}
    for a, b in product(range(4), repeat=2):
        pa, pb = kron(POINTER[a], I4), kron(I4, POINTER[b])
        state = PSI2
        for label in order:
            state = mv(pa, mv(ua, state)) if label == "A" else mv(pb, mv(ub, state))
        law[(a, b)] = inner(state, state)
    return law


for packet in (PACKET_Q, PACKET_H):
    packet_ab = disjoint_schedule(("A", "B"), packet.interaction)
    packet_ba = disjoint_schedule(("B", "A"), packet.interaction)
    check(packet_ab == packet_ba,
          f"{packet.name} disjoint schedule presentations push to one law")
    check(sum(packet_ab.values(), ZERO) == ONE,
          f"{packet.name} disjoint physical history law normalizes")

law_ab = disjoint_schedule(("A", "B"), U_QUARTER)
law_ba = disjoint_schedule(("B", "A"), U_QUARTER)
check(law_ab == law_ba, "disjoint auxiliary linearizations have identical exact laws")
check(sum(law_ab.values(), ZERO) == ONE, "one canonical disjoint physical law normalizes")
canonical_fibers = {}
for presentation, law in (("AB", law_ab), ("BA", law_ba)):
    for values, mass in law.items():
        key = tuple(sorted((('A', values[0]), ('B', values[1]))))
        if key in canonical_fibers:
            check(canonical_fibers[key] == mass,
                  f"fiber {key} presentation {presentation} has invariant weight")
        else:
            canonical_fibers[key] = mass
check(sum(canonical_fibers.values(), ZERO) == ONE,
      "canonical fiber pushforward does not double-count gauge presentations")

# Overlap control: same-collar operations do not commute and a downstream
# pointer record distinguishes their physical order.
X_LEFT = kron(X, I2)


def find_overlap_witness(interaction):
    for input_index, output_index in product(range(4), repeat=2):
        psi = tuple(ONE if k == input_index else ZERO for k in range(4))
        p = POINTER[output_index]
        ux = mv(p, mv(X_LEFT, mv(interaction, psi)))
        xu = mv(p, mv(interaction, mv(X_LEFT, psi)))
        p_ux, p_xu = inner(ux, ux), inner(xu, xu)
        if p_ux != p_xu:
            return input_index, output_index, p_ux, p_xu
    return None


for packet in (PACKET_Q, PACKET_H):
    check(mul(packet.interaction, X_LEFT) != mul(X_LEFT, packet.interaction),
          f"{packet.name} overlapping same-collar operations retain order")
    check(find_overlap_witness(packet.interaction) is not None,
          f"{packet.name} overlap order changes a downstream record probability")

overlap_witness = find_overlap_witness(U_QUARTER)

# Primitive non-Markov sealed-history process with explicit record/collar
# birth, full prefix tower, and exact conditional disintegration.
@dataclass(frozen=True)
class ClassicalCollar:
    collar_id: str
    block_phase: int
    block_memory: tuple
    parent_record: str | None


@dataclass(frozen=True)
class ClassicalRecord:
    record_id: str
    value: int
    input_collar: str
    output_collar: str


@dataclass(frozen=True)
class ClassicalHistory:
    values: tuple
    records: tuple
    collar: ClassicalCollar
    mass: F


def finite_collar_conditionals(collar, r):
    if collar.block_phase < 2:
        return {-1: F(1, 2), 1: F(1, 2)}
    x, y = collar.block_memory
    return {-1: (F(1) - r * x * y) / 2,
            1: (F(1) + r * x * y) / 2}


def advance_classical_collar(collar, value, collar_id, parent_record):
    if collar.block_phase == 0:
        phase, memory = 1, (value,)
    elif collar.block_phase == 1:
        phase, memory = 2, collar.block_memory + (value,)
    else:
        phase, memory = 0, ()
    return ClassicalCollar(collar_id, phase, memory, parent_record)


def finite_collar_from_prefix(prefix):
    collar = ClassicalCollar("probe0", 0, (), None)
    for i, value in enumerate(prefix):
        collar = advance_classical_collar(collar, value, f"probe{i + 1}", f"pr{i}")
    return collar


def all_level_block_mass(values, r):
    """Consistent law on every finite prefix: independent P_r triple blocks."""
    mass = F(1)
    full_blocks, remainder = divmod(len(values), 3)
    for block in range(full_blocks):
        x, y, z = values[3 * block:3 * block + 3]
        mass *= (F(1) + r * x * y * z) / 8
    mass *= F(1, 2 ** remainder)
    return mass


def all_level_block_conditionals(prefix, r):
    position = len(prefix) % 3
    if position < 2:
        return {-1: F(1, 2), 1: F(1, 2)}
    x, y = prefix[-2], prefix[-1]
    return {-1: (F(1) - r * x * y) / 2,
            1: (F(1) + r * x * y) / 2}


for label, r in (("half", F(1, 2)), ("third", F(1, 3))):
    all_level_laws = {
        n: {values: all_level_block_mass(values, r)
            for values in product((-1, 1), repeat=n)}
        for n in range(10)
    }
    check(all(sum(law.values(), F(0)) == 1 for law in all_level_laws.values()),
          f"P_r {label} all-level block cylinder family normalizes through depth 9")
    check(all(
        {prefix: all_level_laws[n + 1][prefix + (-1,)] +
                 all_level_laws[n + 1][prefix + (1,)]
         for prefix in all_level_laws[n]} == all_level_laws[n]
        for n in range(9)),
        f"P_r {label} all adjacent block-prefix bonding maps are projective")
    check(all(
        all(all_level_laws[n + 1][prefix + (value,)] /
            all_level_laws[n][prefix] == q
            for value, q in all_level_block_conditionals(prefix, r).items())
        for n in range(9) for prefix in all_level_laws[n]),
        f"P_r {label} all-level conditionals exactly disintegrate the cylinder family")
    check(all(
        len(finite_collar_from_prefix(prefix).block_memory) <= 2 and
        finite_collar_conditionals(finite_collar_from_prefix(prefix), r) ==
        all_level_block_conditionals(prefix, r)
        for n in range(9) for prefix in all_level_laws[n]),
        f"P_r {label} all-level law has an exact finite phase/two-sign collar realization")
    # The displayed formula is defined for arbitrary n; the two exact checks
    # cover complete-block and within-block bonding cases repeatedly.


def classical_tower(r):
    root = ClassicalHistory((), (), ClassicalCollar("k0", 0, (), None), F(1))
    levels = [(root,)]
    for depth in range(3):
        children = []
        for history in levels[-1]:
            for value, q in finite_collar_conditionals(history.collar, r).items():
                values = history.values + (value,)
                suffix = "".join("p" if x == 1 else "m" for x in values)
                rid, cid = f"kr{depth}:{suffix}", f"kc{depth + 1}:{suffix}"
                record = ClassicalRecord(rid, value, history.collar.collar_id, cid)
                collar = advance_classical_collar(history.collar, value, cid, rid)
                children.append(ClassicalHistory(values, history.records + (record,),
                                                 collar, history.mass * q))
        levels.append(tuple(children))
    return tuple(levels)


for label, r in (("half", F(1, 2)), ("third", F(1, 3))):
    tower = classical_tower(r)
    check(tuple(len(level) for level in tower) == (1, 2, 4, 8),
          f"P_r {label} emits every explicit sealed prefix and collar")
    check(all(sum((history.mass for history in level), F(0)) == 1 for level in tower),
          f"P_r {label} normalizes at every prefix depth")
    for depth in range(1, 4):
        pushed = {}
        for history in tower[depth]:
            pushed[history.values[:-1]] = pushed.get(history.values[:-1], F(0)) + history.mass
        coarse = {history.values: history.mass for history in tower[depth - 1]}
        check(pushed == coarse, f"P_r {label} depth {depth} bonding map is projective")
    terminal = {history.values: history.mass for history in tower[3]}
    expected = {h: (F(1) + r * h[0] * h[1] * h[2]) / 8
                for h in product((-1, 1), repeat=3)}
    check(terminal == expected, f"P_r {label} explicit process equals whole-history law")

tower_half = classical_tower(F(1, 2))
terminal_half = {h.values: h.mass for h in tower_half[3]}
q_plus = terminal_half[(1, 1, 1)] / (
    terminal_half[(1, 1, -1)] + terminal_half[(1, 1, 1)])
q_minus = terminal_half[(-1, 1, 1)] / (
    terminal_half[(-1, 1, -1)] + terminal_half[(-1, 1, 1)])
check((q_plus, q_minus) == (F(3, 4), F(1, 4)),
      "explicit next-click law depends non-Markovly on the earlier sealed record")

# Local exponential-threshold representation (architecture E) of exactly the
# same classical projective law.  Independent Exp(rate lambda_e) races choose
# e with lambda_e/sum(lambda); using the conditional masses as rates therefore
# reproduces, rather than replaces, the primitive whole-history law.
for prefix in ((), (1,), (1, 1), (1, 1, -1)):
    finite_collar = finite_collar_from_prefix(prefix)
    rates = finite_collar_conditionals(finite_collar, F(1, 2))
    total = sum(rates.values(), F(0))
    winner = {value: rate / total for value, rate in rates.items()}
    check(winner == rates, f"prefix {prefix} exponential race represents its exact conditional")
check(all(history.mass ==
          reduce(
              lambda acc, item: acc * item[1],
              ((value, finite_collar_conditionals(
                  finite_collar_from_prefix(history.values[:i]), F(1, 2))[value])
               for i, value in enumerate(history.values)),
              F(1))
          for history in tower_half[3]),
      "threshold conditional products reproduce every whole-history cylinder mass")
for label, r in (("half", F(1, 2)), ("third", F(1, 3))):
    check(all(
        all_level_block_mass(values, r) == reduce(
            lambda acc, item: acc * item[1],
            ((value, all_level_block_conditionals(values[:i], r)[value])
             for i, value in enumerate(values)),
            F(1))
        for n in range(10) for values in product((-1, 1), repeat=n)),
        f"P_r {label} all-level exponential-threshold products equal every cylinder mass")

# The two universe candidates work and satisfy the same architecture gates,
# but a supplied coupling still changes their law (certified in the sibling
# symmetric-family executable).  This file closes mechanics, not selection.
check(overlap_witness[2] != overlap_witness[3],
      "generated history machinery retains empirical interaction sensitivity")

EXPECTED_CHECKS = 145
if CHECKS != EXPECTED_CHECKS:
    raise AssertionError(f"expected {EXPECTED_CHECKS} checks, observed {CHECKS}")

summary = (
    "D12 MULTI-DIAMOND HISTORY EXACT RECEIPT\n"
    f"checks={CHECKS}\n"
    f"depth={DEPTH}\n"
    f"depth4_histories={len(baseline[4])}\n"
    "minimum_diamond_packet_fields=PASS\n"
    "support_relative_rn_reconstruction_and_mutation_refusal=PASS\n"
    "explicit_durable_records_and_output_collars=PASS\n"
    "record_repeat_read_and_persistence=PASS\n"
    "local_type_owner_opportunity_stale_eligibility=PASS\n"
    "depth_indexed_cylinder_projectivity=PASS_0_TO_4_PLUS_INDUCTION\n"
    "nontrivial_next_record_disintegration=PASS\n"
    "independent_vertex_frame_transport=PASS\n"
    "lower_and_upper_unitary_frame_domain_refusal=PASS\n"
    "canonical_disjoint_construction_fibers=PASS\n"
    "overlapping_order_control=PASS\n"
    "explicit_nonmarkov_sealed_history_process=PASS\n"
    "all_level_classical_projective_family=PASS\n"
    "finite_phase_two_sign_threshold_collar=PASS\n"
    "equivalent_local_exponential_threshold_representation=PASS\n"
    "continuation=EXPLICIT_DEPTH4_PLUS_TYPE_COMPLETENESS_INDUCTION\n"
    "two_full_models_shared_gates=PASS_WITH_DIFFERENT_RECORD_PROBABILITIES\n"
    "interaction_selection=REFUTED_FROM_SHARED_GATES\n"
    "verdict=WORKING_MULTI_DIAMOND_UNIVERSAL_FORM_NOT_UNIQUE_LAW\n"
)
print(summary, end="")
receipt = sha256(summary.encode()).hexdigest()
EXPECTED_RECEIPT = "d48f9a161dd3e7f850726225d9ea3faad8433fe35ede0c3957cbbb0963e691c6"
if receipt != EXPECTED_RECEIPT:
    raise AssertionError(f"receipt drift: {receipt}")
print("receipt_sha256=" + receipt)
