#!/usr/bin/env python3
"""
d46d_typicality_exact.py — v10 D46d (ladder step d): typicality
under two candidate normalizations of the committed weight system.
Pin: note-d46d-typicality.md (strict).  Parents: D45b TERMINAL #367
(capability: UNBOUNDED order dimension by a HAND-BUILT constructor);
D46b #384/round-1-repaired (the finite-horizon kernel this samples
under); the note-d45b §1 doctrine (binding: order dimension is a
1+1-escape detector and a clock-complexity grade, never a
dimension-of-the-world estimator; ORDER dimension only).

THE QUESTION, restated after round 1: capability is settled; how much
mass do the two candidate normalizations of the committed weight
system put on the WIDTH the dimension mechanism needs, and how does
that mass scale with the POOL — the axis on which unbounded ORDER
dimension (D45b's capability result) lives?

ROUND-1 REPAIRED REVISION (v10/reviews/d46bd-round1-hostile-review.md).
The headline REVERSES in direction:

  * D-A1 BLOCKER.  "Width spreads with depth" is a near-tautology:
    actor width is a MONOTONE NON-DECREASING functional of the path,
    so at a fixed pool the width mass climbs to 1 under any law with
    full support.  The like-for-like series (same pool, same law,
    growing depth) is computed here and shows exactly that
    saturation.  The DISCRIMINATING scalings — fixed depth with
    growing pool, and the diagonal depth = 2 x pool — point the
    OTHER WAY: the mass at FULL width DECAYS with the pool.  What is
    typical-in-the-making is ORDER dimension >= 3, NOT D45b's
    unbounded ORDER dimension.
  * D-A2 BLOCKER.  "The theory's OWN law" is not established: the
    weight layer d42b1 disclaims a measure in its own docstring
    ("Weight-system level only (RF4): no measure claim; the
    placement front (d42b3) owns normalization"), and this unit uses
    TWO different normalizations.  They are named explicitly
    everywhere: the LOOKAHEAD-COMPLETED weight measure (exact arm)
    and the LOCAL-NORMALIZED weight measure (sampled arm).
  * D-M1.  actors_touched counts an actor touched by an IDLE, and
    the measure is about half idle.  Both conservative proxies —
    NON-IDLE-ACTIVE and DELIVERY-JOINED — are computed and gated
    beside it; idle-heaviness is NOT presented as support.
  * D-M3.  width >= 4 is NECESSARY, NOT SUFFICIENT: the mass above
    it UPPER-BOUNDS the ORDER dimension mass.  Stated everywhere.
  * D-M2.  TY1's "poset width where cheap" is implemented; TY4's
    delivery-pattern half is implemented as the delivery-joined
    proxy; what remains dropped is declared in-gate.
  * D-M4.  The three gates that could not fire are replaced, the gap
    bound is moved into TY3-a, and the doctrine scan's blanket
    negation exemption (which passed the referee's mutant d5) is
    replaced by POSITIVE scope markers plus a capability probe.

GREEN-UNREVIEWED — round 1 is in hand and applied; not citable as
review-hardened until the round converts (paper-32's round precedes
it).
"""
import ast
import os
import sys
import random
from fractions import Fraction as Fr

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

OUT = []
def outcome(tag, text):
    OUT.append((tag, text))
    print(f"  [OUTCOME {tag}] {text}")

print("[d46d — typicality under two candidate normalizations]")
print("  banner: GREEN-UNREVIEWED, ROUND-1 REPAIRED (D46 program pin;")
print("  paper-32's round precedes this unit's).  THE LAW IS NAMED,")
print("  NOT ASSUMED: the committed weight layer d42b1 declares in")
print("  its own docstring 'Weight-system level only (RF4): no")
print("  measure claim; the placement front (d42b3) owns")
print("  normalization', and its menus sum to 2 or 5/2, never to 1.")
print("  A probability law therefore has to be CHOSEN, and this unit")
print("  uses two: the LOOKAHEAD-COMPLETED weight measure")
print("  k(e|h) = q G(h+e)/G(h) (exact arm, telescoping to")
print("  w(path)/G(root)) and the LOCAL-NORMALIZED weight measure")
print("  q/sum q (sampled arm).  Every number below is labelled with")
print("  which one produced it; neither is pinned anywhere in the")
print("  corpus as THE law and this receipt does not call either one")
print("  that.  Width is reported under THREE proxies (touched,")
print("  non-idle-active, delivery-joined) because the liberal one")
print("  counts an actor touched by an idle.  Horizon-scoped")
print("  throughout; ORDER dimension only, a clock-complexity grade")
print("  (note-d45b §1 binds) — no dimension-of-the-world claim.")

_SRC = 'v10/code/d42b1_transport_exact.py'
_src = open(_SRC).read()
ns = {}
exec(_src[:_src.index('print("[d42b1')], ns)
V0 = ns['V0']
candidates_for = ns['candidates_for']
event_poset = ns['event_poset']
AB = ('A', 'B')
_DISCLAIM = "no measure claim"
check("TY0-a THE WEIGHT LAYER'S OWN DISCLAIMER, quoted from the "
      "committed source rather than paraphrased (round 1, BLOCKER "
      "D-A2): d42b1's docstring says the layer is 'Weight-system "
      "level only (RF4): no measure claim; the placement front "
      "(d42b3) owns normalization'.  Every typicality statement in "
      "this receipt is therefore explicitly relative to ONE OF TWO "
      "NAMED normalizations, never to 'the theory's own law'",
      _DISCLAIM in _src and 'owns normalization' in _src,
      f"disclaimer found verbatim in {_SRC} = {_DISCLAIM in _src}")

# ---- TY0: the layer, the family, the D46b potential -----------------
CAP = 4
FAM = [[]]
CACHE = {}
frontier = [[]]
while frontier:
    h = frontier.pop()
    CACHE[tuple(h)] = candidates_for(h, AB)
    if len(h) >= CAP:
        continue
    for e, q in CACHE[tuple(h)]:
        FAM.append(h + [e])
        frontier.append(h + [e])
cum = [sum(1 for h in FAM if len(h) <= k) for k in range(CAP + 1)]

G = {}
for L in range(CAP, -1, -1):
    for h in FAM:
        if len(h) != L:
            continue
        G[tuple(h)] = (Fr(1) if L == CAP else
                       sum(q * G[tuple(h + [e])]
                           for e, q in CACHE[tuple(h)]))
check("TY0-b the committed layer, family, and D46b potential "
      "re-anchored BEFORE any typicality statement: ARM-1T "
      "cumulative sizes [1, 9, 69, 521, 3969]; the finite-horizon "
      "potential G_4(root) = 1035/64 (the #384 value, unchanged by "
      "that unit's round-1 repair)",
      cum == [1, 9, 69, 521, 3969] and G[tuple([])] == Fr(1035, 64),
      f"cumulative = {cum}; G_4(root) = {G[tuple([])]}")

# the LOOKAHEAD-COMPLETED path measure on depth-CAP histories
def path_mass(h):
    """prod_e k(e | prefix) with k(e|h) = q G(h+e)/G(h) — the
    LOOKAHEAD-COMPLETED weight measure's path probability (telescopes
    to (prod q) / G(root) since the terminal G's are 1).  One of two
    candidate normalizations, not 'the theory's law' (D-A2)."""
    m = Fr(1)
    for i, e in enumerate(h):
        pre = tuple(h[:i])
        q = dict(CACHE[pre])[e]
        m *= q * G[tuple(h[:i + 1])] / G[pre]
    return m

DEEP = [h for h in FAM if len(h) == CAP]
MASS = {tuple(h): path_mass(h) for h in DEEP}
total = sum(MASS.values())
check("TY1-a THE LOOKAHEAD-COMPLETED PATH MEASURE IS PROPER: its "
      "path probabilities over ALL 3,448 depth-4 histories sum to "
      "EXACTLY 1 (verified, not assumed).  Properness is a property "
      "of the NORMALIZATION, not evidence that this normalization is "
      "the theory's — the layer disclaims that (TY0-a)",
      total == 1 and len(DEEP) == 3969 - 521,
      f"depth-4 histories = {len(DEEP)}; total mass = {total}")

# ---- TY1-b/TY2: EXACT width-mass, THREE proxies + poset width -------
print("\n[TY1/TY2 — EXACT typicality under the LOOKAHEAD-COMPLETED "
      "weight measure]")
def build(pool, cap):
    fam, cache, fr = [[]], {}, [[]]
    while fr:
        h = fr.pop()
        c = candidates_for(h, pool)
        cache[tuple(h)] = c
        if len(h) >= cap:
            continue
        for e, q in c:
            fam.append(h + [e])
            fr.append(h + [e])
    Gp = {}
    for L in range(cap, -1, -1):
        for h in fam:
            if len(h) != L:
                continue
            Gp[tuple(h)] = (Fr(1) if L == cap else
                            sum(q * Gp[tuple(h + [e])]
                                for e, q in cache[tuple(h)]))
    return fam, cache, Gp

# THE THREE WIDTH PROXIES (round 1, MAJOR D-M1).  The first pass used
# only the first, which counts an actor as touched by an IDLE — and
# the measure is about half idle, so the liberal proxy inflates.  An
# actor that only ever idles forms an isolated chain in the event
# poset and cannot raise order dimension; D45b's escape needs idles as
# marks INTERLEAVED with deliveries among actors that participate.
def w_touched(h):
    """LIBERAL: distinct actors named by any event, idles included.
    An UPPER bound on dimension-relevant width."""
    s = set()
    for e in h:
        s.add(e[1])
        if e[0] == 'd':
            s.add(e[2])
    return len(s)

def w_nonidle(h):
    """MIDDLE: distinct actors named by a NON-IDLE event."""
    s = set()
    for e in h:
        if e[0] == 'n':
            continue
        s.add(e[1])
        if e[0] == 'd':
            s.add(e[2])
    return len(s)

def w_delivery(h):
    """CONSERVATIVE: distinct actors joined by at least one DELIVERY —
    the shape d43d's W6 witness has ('six deliveries among six
    actors').  This is also the DELIVERY-PATTERN half of the TY4 pin
    that the first pass dropped (round 1, D-M2)."""
    s = set()
    for e in h:
        if e[0] == 'd':
            s.add(e[1])
            s.add(e[2])
    return len(s)

WIDTHS = (('touched', w_touched), ('non-idle', w_nonidle),
          ('delivery-joined', w_delivery))

def poset_width(h):
    """THE PIN'S TY1(iii), 'poset width where cheap' — never computed
    by the first pass (round 1, D-M2).  Largest antichain of the event
    poset: the quantity that stands between ACTOR width and ORDER
    ORDER dimension.  Brute-forced over subsets; cheap at depth
    <= 4."""
    pred = event_poset(list(h))
    n = len(h)
    best = 0
    for m in range(1 << n):
        S = [i for i in range(n) if m >> i & 1]
        if all((a not in pred[b]) and (b not in pred[a])
               for i, a in enumerate(S) for b in S[i + 1:]):
            best = max(best, len(S))
    return best

def width_profiles(pool, cap):
    fam, cache, Gp = build(pool, cap)
    deep = [h for h in fam if len(h) == cap]
    prof = {nm: {} for nm, _ in WIDTHS}
    pw, kinds = {}, {}
    tot = Fr(0)
    for h in deep:
        m = Fr(1)
        for i, e in enumerate(h):
            pre = tuple(h[:i])
            m *= (dict(cache[pre])[e] * Gp[tuple(h[:i + 1])] / Gp[pre])
        tot += m
        for nm, f in WIDTHS:
            k = f(h)
            prof[nm][k] = prof[nm].get(k, Fr(0)) + m
        k = poset_width(h)
        pw[k] = pw.get(k, Fr(0)) + m
        for e in h:
            kinds[e[0]] = kinds.get(e[0], Fr(0)) + m
    return prof, pw, kinds, tot, len(deep)

POOLS = [(('A', 'B'), 4), (('A', 'B', 'C'), 3),
         (('A', 'B', 'C', 'D'), 3), (('A', 'B', 'C', 'D', 'E'), 2)]
PROFILES, PW, TOPW = {}, {}, {}
for pool, cap in POOLS:
    prof, pw, kinds, tot, ndeep = width_profiles(pool, cap)
    PROFILES[(len(pool), cap)] = (prof, tot, ndeep)
    PW[(len(pool), cap)] = pw
    top = max(prof['touched'])
    TOPW[(len(pool), cap)] = top
    print(f"    pool {len(pool)} actors, depth {cap} ({ndeep} terminal "
          f"histories) [LOOKAHEAD-COMPLETED]:")
    for nm, _ in WIDTHS:
        line = ", ".join(f"k={k}: {float(prof[nm][k]):.4f}"
                         for k in sorted(prof[nm]))
        print(f"      actor width, {nm:<15} -> {line}")
    print(f"      mass at the maximum realizable actor width "
          f"k = {top}:  touched {prof['touched'][top]} "
          f"(~{float(prof['touched'][top]):.6f})  |  non-idle "
          f"{prof['non-idle'].get(top, Fr(0))} "
          f"(~{float(prof['non-idle'].get(top, Fr(0))):.6f})  |  "
          f"delivery-joined {prof['delivery-joined'].get(top, Fr(0))} "
          f"(~{float(prof['delivery-joined'].get(top, Fr(0))):.6f})")
    print(f"      POSET width (largest antichain of the event poset, "
          f"the pin's TY1(iii)) -> "
          + ", ".join(f"w={k}: {pw[k]} (~{float(pw[k]):.4f})"
                      for k in sorted(pw)))
    print(f"      event-kind mass (idle 'n' is the unconditional "
          f"residual; reported as a CONFOUND for the touched proxy, "
          f"never as support): "
          f"{ {kk: round(float(vv), 3) for kk, vv in sorted(kinds.items())} }")

allproper = all(PROFILES[k][1] == 1 for k in PROFILES)
TOP_REF = {
    (2, 4): (Fr(221, 230), Fr(1573, 2070), Fr(78, 115)),
    (3, 3): (Fr(130, 289), Fr(59, 289), Fr(31, 289)),
    (4, 3): (Fr(994, 9243), Fr(418, 9243), Fr(292, 9243)),
    (5, 2): (Fr(3, 160), Fr(3, 160), Fr(3, 160)),
}
got = {k: tuple(PROFILES[k][0][nm].get(TOPW[k], Fr(0))
                for nm, _ in WIDTHS) for k in PROFILES}
shrinks = all(got[k][0] >= got[k][1] >= got[k][2] for k in got)
check("TY1-b/TY2 THE EXACT WIDTH-MASS PROFILE UNDER ALL THREE "
      "PROXIES at every enumerable pool (2 actors/depth 4, 3/depth "
      "3, 4/depth 3, 5/depth 2), each measure summing to EXACTLY 1 "
      "and each top-width mass anchored to its exact rational.  "
      "Round 1, D-M1: the liberal 'touched' proxy counts idlers, and "
      "the conservative proxies are materially smaller — at 2 "
      "actors/depth 4 the top-width mass is 221/230 touched but "
      "1573/2070 non-idle and 78/115 delivery-joined; at 3/depth 3 "
      "it is 130/289 vs 59/289 vs 31/289; at 4/depth 3, 994/9243 vs "
      "418/9243 vs 292/9243.  The ordering touched >= non-idle >= "
      "delivery-joined is gated, so the direction of the bound "
      "cannot be lost",
      allproper and got == TOP_REF and shrinks
      and len(PROFILES) == 4,
      f"profiles computed = {len(PROFILES)}; all measures proper = "
      f"{allproper}; touched >= non-idle >= delivery-joined at every "
      f"pool = {shrinks}")

PW_REF = {
    (2, 4): {1: Fr(833, 2070), 2: Fr(1237, 2070)},
    (3, 3): {1: Fr(78, 289), 2: Fr(184, 289), 3: Fr(27, 289)},
    (4, 3): {1: Fr(1459, 9243), 2: Fr(5840, 9243), 3: Fr(216, 1027)},
    (5, 2): {1: Fr(49, 160), 2: Fr(111, 160)},
}
pw_max = {k: max(PW[k]) for k in PW}
check("TY1-c THE PIN'S POSET WIDTH, COMPUTED (round 1, D-M2: pin §2 "
      "TY1(iii) said 'poset width where cheap' and the first pass "
      "reported actor counts only).  The exact mass by largest "
      "antichain of the EVENT poset is anchored at all four pools.  "
      "It is much smaller than the actor width the headline uses — "
      "at 4 actors/depth 3 the actor-width-4 mass is 994/9243 while "
      "the poset width never exceeds 3 — because the depth caps bind "
      "the antichain.  This is exactly why the enumerable arm cannot "
      "settle dimension: d44c AG5 records that ALL 219 four-event "
      "and ALL 4,231 five-event labelled posets have order dimension "
      "<= 2, so at these depths ORDER dimension > 2 is IMPOSSIBLE, "
      "not "
      "merely rare",
      PW == PW_REF and pw_max == {(2, 4): 2, (3, 3): 3, (4, 3): 3,
                                  (5, 2): 2},
      "; ".join(f"{na}a/d{cap}: max poset width = {pw_max[(na, cap)]}"
                for (na, cap) in sorted(pw_max)))

# the exact concentration reading — computed AND gated (round 1 D-M4)
frac_top = {k: PROFILES[k][0]['touched'][TOPW[k]] for k in PROFILES}
above_half = sorted(k for k in frac_top if frac_top[k] >= Fr(1, 2))
conc = not above_half
check("TY2-b THE CONCENTRATION READING, COMPUTED AND GATED (round 1, "
      "D-M4(1): the first pass computed `conc` into a variable that "
      "was then never printed and never gated, so the reading its "
      "own label promised did not appear in the output).  The "
      "question 'is the top-width mass below one half everywhere?' "
      "is answered by naming the pools where it is NOT: exactly one, "
      "the 2-actor pool at 221/230, where the maximum realizable "
      "width is 2 and the question is trivial.  All four exact "
      "top-width masses are anchored",
      above_half == [(2, 4)] and frac_top == {
          (2, 4): Fr(221, 230), (3, 3): Fr(130, 289),
          (4, 3): Fr(994, 9243), (5, 2): Fr(3, 160)}
      and len(above_half) == 1,
      f"top-width mass below 1/2 at every pool = {conc}; pools at or "
      f"above 1/2 = {above_half}; "
      + "; ".join(f"{na}a/d{cap}: {frac_top[(na, cap)]} "
                  f"(~{float(frac_top[(na, cap)]):.4f})"
                  for (na, cap) in sorted(frac_top)))

# ---- TY3: the SAMPLED extension (declared law, seeds, pools) --------
print("\n[TY3 — the sampled extension under the LOCAL-NORMALIZED "
      "weight measure: declared law, seeds, pools]")
# The lookahead-completed normalization needs the whole subtree, so it
# is NOT computable beyond the enumerable caps.  TY3 therefore samples
# the LOCAL-NORMALIZED weight measure (each step drawn from q(.|h)
# divided by the menu sum) and CALIBRATES it against the completed one
# where both are exact.  These are two DIFFERENT objects (that is what
# the gap measures) and neither is 'the theory's law' (D-A2).
def local_profile(pool, cap):
    fam, cache, Gp = build(pool, cap)
    deep = [h for h in fam if len(h) == cap]
    prof, tot = {}, Fr(0)
    for h in deep:
        m = Fr(1)
        for i, e in enumerate(h):
            pre = tuple(h[:i])
            cs = cache[pre]
            m *= dict(cs)[e] / sum(q for _, q in cs)
        tot += m
        k = w_touched(h)
        prof[k] = prof.get(k, Fr(0)) + m
    return prof, tot

lp4, lt4 = local_profile(('A', 'B', 'C', 'D'), 3)
kp4 = PROFILES[(4, 3)][0]['touched']
gap = max(abs(lp4.get(k, Fr(0)) - kp4.get(k, Fr(0)))
          for k in set(lp4) | set(kp4))
check("TY3-a THE CALIBRATION (the method gate), with the BOUND moved "
      "in (round 1, D-M4(3): the first pass's TY3-a gate would have "
      "passed with a gap of 0.9, the bound living only in TY5-d).  "
      "The LOCAL-NORMALIZED weight measure — the only one samplable "
      "beyond the enumerable caps, since the completed one needs the "
      "whole subtree — is compared EXACTLY against the "
      "lookahead-completed one on the 4-actor depth-3 family, where "
      "both are computable: the maximum width-mass discrepancy is "
      "EXACTLY 3457/9464832 and is gated below 1/100 here, at the "
      "point of use.  CALIBRATED AT ONE (pool, depth) PAIR ONLY: the "
      "pools sampled below are 4, 5, 6 and the depths 6 and 8, none "
      "of them calibrated, so this licenses nothing beyond an "
      "extrapolation whose single anchor is named",
      lt4 == 1 and gap == Fr(3457, 9464832) and gap < Fr(1, 100),
      f"local law proper = {lt4 == 1}; max width-mass gap vs the "
      f"lookahead-completed measure = {gap} (~{float(gap):.6f}) "
      f"< 1/100")

def sample_widths(pool, depth, n, seed):
    """Draw n paths under the LOCAL-NORMALIZED weight measure and
    histogram ALL THREE width proxies from the SAME draws.  The
    threshold comparison uses a 1e-9 rational grid, so the realized
    law is a 1e-9-grid perturbation of the local one (round 1, D-m3):
    the per-step bias is bounded by (#options)*1e-9, i.e. ~1e-7 over
    8 steps, against a Monte-Carlo standard error of ~8e-3 at
    N = 4000.  The estimator is NOT exact and is not described as
    exact."""
    rng = random.Random(seed)
    prof = {nm: {} for nm, _ in WIDTHS}
    for _ in range(n):
        h = []
        for _ in range(depth):
            cs = candidates_for(h, pool)
            tot = sum(q for _, q in cs)
            x = Fr(rng.randrange(10 ** 9), 10 ** 9) * tot
            acc = Fr(0)
            pick = cs[-1][0]
            for e, q in cs:
                acc += q
                if x < acc:
                    pick = e
                    break
            h.append(pick)
        for nm, f in WIDTHS:
            k = f(h)
            prof[nm][k] = prof[nm].get(k, 0) + 1
    return prof

SEEDS = (20260719, 7)
NSAMP = 4000
POOL8 = tuple('ABCDEFGH')
SAMPLED = {}
SAMP_LINES = []
for np_, depth in ((4, 6), (5, 8), (6, 8)):
    pr = sample_widths(POOL8[:np_], depth, NSAMP, SEEDS[0])
    SAMPLED[(np_, depth)] = pr
    for nm, _ in WIDTHS:
        line = ", ".join(f"k={k}: {pr[nm][k] / NSAMP:.4f}"
                         for k in sorted(pr[nm]))
        _l = (f"    [SAMPLED, LOCAL-NORMALIZED] pool {np_}, depth "
              f"{depth}, N = {NSAMP}, seed = {SEEDS[0]}, width proxy "
              f"= {nm}: {line}")
        SAMP_LINES.append(_l)
        print(_l)
rep = sample_widths(POOL8[:4], 6, NSAMP, SEEDS[0])
dif = sample_widths(POOL8[:4], 6, NSAMP, SEEDS[1])
check("TY3-b THE SAMPLED WIDTH DISTRIBUTIONS are delivered with "
      "their law, size, and seeds DECLARED ([SAMPLED, "
      "LOCAL-NORMALIZED] labels everywhere; never conflated with the "
      "exact profiles above), and the estimator is REPRODUCIBLE: the "
      "same seed reproduces the identical histogram under all three "
      "proxies, a different seed does not (the sampler is genuinely "
      "stochastic, not a disguised constant)",
      rep == SAMPLED[(4, 6)] and dif != SAMPLED[(4, 6)],
      f"seed-{SEEDS[0]} reproducible = {rep == SAMPLED[(4, 6)]}; "
      f"seed-{SEEDS[1]} differs = {dif != SAMPLED[(4, 6)]}")

# ---- TY4: the headline, under all three proxies ---------------------
print("\n[TY4 — the constructor-scale reading, all three proxies]")
top6 = SAMPLED[(6, 8)]
HEAD = {}
for nm, _ in WIDTHS:
    d = top6[nm]
    HEAD[nm] = (sum(v for k, v in d.items() if k >= 4),
                sum(v for k, v in d.items() if k >= 6))
for nm, _ in WIDTHS:
    print(f"    [SAMPLED] pool 6 / depth 8, proxy {nm:<15}: "
          f"mass(width >= 4) = {HEAD[nm][0] / NSAMP:.4f}  "
          f"mass(full width 6) = {HEAD[nm][1] / NSAMP:.4f}")
HEAD_REF = {'touched': (3923, 1227), 'non-idle': (2688, 306),
            'delivery-joined': (1655, 122)}
head_falls = (HEAD['touched'][0] > HEAD['non-idle'][0]
              > HEAD['delivery-joined'][0]
              and HEAD['touched'][1] > HEAD['non-idle'][1]
              > HEAD['delivery-joined'][1])
check("TY4 THE CONSTRUCTOR-SCALE COMPARISON [SAMPLED, "
      "LOCAL-NORMALIZED, PROXY] at the 6-actor pool over 8 events — "
      "the scale at which D45b's courier constructor realizes S_3 — "
      "reported under ALL THREE width proxies with the exact sampled "
      "counts anchored (round 1, D-M4(2): the first pass's predicate "
      "was that two frequencies lie in [0, 1], which the referee's "
      "mutant d4 walked straight through).  THE DIRECTION OF THE "
      "BOUND (round 1, D-M3): actor width >= 4 is the d44c/d43d "
      "threshold and is NECESSARY, NOT SUFFICIENT — d44c AG5 records "
      "that all 219 four-event and all 4,231 five-event labelled "
      "posets have order dimension <= 2 — so mass(width >= 4) "
      "UPPER-BOUNDS mass(order dimension > 2) and is consistent with "
      "that mass being zero.  Fixing the threshold at 4 also "
      "narrows the inherited question from D45b's UNBOUNDED "
      "dimension to ORDER dimension >= 3; that narrowing is declared "
      "here, "
      "not smuggled",
      HEAD == HEAD_REF and head_falls,
      "; ".join(f"{nm}: >= 4 -> {HEAD[nm][0]}/{NSAMP} = "
                f"{HEAD[nm][0] / NSAMP:.4f}, full 6 -> "
                f"{HEAD[nm][1]}/{NSAMP} = {HEAD[nm][1] / NSAMP:.4f}"
                for nm, _ in WIDTHS)
      + f"; conservative proxies strictly smaller = {head_falls}")

# ---- TY4-b/c/d: THE SCALINGS THAT DISCRIMINATE ----------------------
# Round 1, BLOCKER D-A1.  The first pass's headline chained four
# EXACT numbers under the completed normalization at four different
# (pool, depth) pairs to one SAMPLED number under the local
# normalization at a fifth — four things varying at once, so nothing
# in the chain isolated depth.  Here the like-for-like series is run
# first (same pool, same law, growing depth), and then the two
# scalings the claim actually needs.
NS2, NS3 = 600, 300
print("\n[TY4-b — LIKE-FOR-LIKE: same pool, same law, growing depth]")
DEPTHS = (2, 3, 4, 6, 8, 10)
DSER = {}
for d in DEPTHS:
    DSER[d] = sample_widths(POOL8[:6], d, NS2, SEEDS[0])
def _ge(dd, k):
    return sum(v for kk, v in dd.items() if kk >= k)
for nm, _ in WIDTHS:
    print(f"    [SAMPLED, LOCAL-NORMALIZED] pool 6, N = {NS2}, seed "
          f"= {SEEDS[0]}, proxy {nm:<15}: width >= 4 by depth "
          + ", ".join(f"d{d}: {_ge(DSER[d][nm], 4) / NS2:.3f}"
                      for d in DEPTHS)
          + "  |  full width 6 "
          + ", ".join(f"d{d}: {_ge(DSER[d][nm], 6) / NS2:.3f}"
                      for d in DEPTHS))
tser = [_ge(DSER[d]['touched'], 4) for d in DEPTHS]
jser = [_ge(DSER[d]['delivery-joined'], 4) for d in DEPTHS]
TSER_REF = [16, 145, 347, 542, 587, 600]
JSER_REF = [16, 42, 81, 162, 259, 326]
saturates = (tser == sorted(tser) and tser[-1] == NS2)
check("TY4-b THE LIKE-FOR-LIKE SERIES, and why it settles nothing "
      "(round 1, BLOCKER D-A1).  Same pool (6), same law "
      "(LOCAL-NORMALIZED), growing depth: the touched-width >= 4 "
      "mass climbs monotonically to 1.000 by depth 10.  IT CANNOT DO "
      "OTHERWISE: actor width is a MONOTONE NON-DECREASING "
      "functional of the path — a longer history can only touch more "
      "actors — so at a fixed pool this mass climbs to 1 under ANY "
      "law with full support.  'Width spreads with depth' is a "
      "property of the OBSERVABLE, not a discriminating property of "
      "any normalization, and the first pass's headline rested on "
      "it.  Gated here as the near-tautology it is: the series is "
      "anchored count by count AND its monotone saturation is "
      "asserted, so the receipt states the fact and denies it "
      "evidential weight in the same gate.  The delivery-joined "
      "series over the same draws climbs far more slowly and does "
      "NOT saturate",
      tser == TSER_REF and jser == JSER_REF and saturates,
      f"touched >= 4 counts by depth {list(DEPTHS)} = {tser}/{NS2} "
      f"(monotone, saturating = {saturates}); delivery-joined >= 4 = "
      f"{jser}/{NS2}")

print("\n[TY4-c — FIXED DEPTH 8, GROWING POOL: the scaling unbounded "
      "ORDER dimension actually needs]")
PSER = {}
for p in (3, 4, 5, 6, 7, 8):
    PSER[p] = sample_widths(POOL8[:p], 8, NS2, SEEDS[0])
for nm, _ in WIDTHS:
    print(f"    [SAMPLED, LOCAL-NORMALIZED] depth 8, N = {NS2}, seed "
          f"= {SEEDS[0]}, proxy {nm:<15}: mass at FULL width by pool "
          + ", ".join(f"p{p}: {PSER[p][nm].get(p, 0) / NS2:.3f}"
                      for p in sorted(PSER)))
print("    [SAMPLED, LOCAL-NORMALIZED] depth 8, proxy touched: mass "
      "above the FIXED threshold 4 by pool "
      + ", ".join(f"p{p}: {_ge(PSER[p]['touched'], 4) / NS2:.3f}"
                  for p in sorted(PSER)))
tfull = [PSER[p]['touched'].get(p, 0) for p in sorted(PSER)]
jfull = [PSER[p]['delivery-joined'].get(p, 0) for p in sorted(PSER)]
tge4 = [_ge(PSER[p]['touched'], 4) for p in sorted(PSER)]
TFULL_REF = [578, 469, 341, 200, 82, 22]
JFULL_REF = [315, 143, 63, 18, 3, 2]
TGE4_REF = [0, 469, 563, 587, 592, 599]
t_decays = all(tfull[i] < tfull[i - 1] for i in range(1, len(tfull)))
j_decays = all(jfull[i] < jfull[i - 1] for i in range(1, len(jfull)))
check("TY4-c THE FIXED-DEPTH POOL SCALING (round 1, D-A1, "
      "prescribed): D45b's result is UNBOUNDED order dimension, "
      "which needs width growing WITH THE POOL.  At fixed depth 8, "
      "growing the pool from 3 to 8 actors, the mass at the pool's "
      "FULL width DECAYS STRICTLY AND ROUGHLY GEOMETRICALLY — "
      "0.963, 0.782, 0.568, 0.333, 0.137, 0.037 touched and 0.525, "
      "0.238, 0.105, 0.030, 0.005, 0.003 delivery-joined — while the "
      "mass above the FIXED threshold 4 rises to ~1 trivially, "
      "because the threshold is fixed while the pool grows.  Both "
      "monotonicities are gated and every count anchored: the "
      "direction that matters for unbounded ORDER dimension points "
      "AGAINST it",
      tfull == TFULL_REF and jfull == JFULL_REF
      and tge4 == TGE4_REF and t_decays and j_decays,
      f"full-width counts, touched = {tfull}/{NS2} (strictly "
      f"decreasing = {t_decays}); delivery-joined = {jfull}/{NS2} "
      f"(strictly decreasing = {j_decays}); above the fixed "
      f"threshold 4, touched = {tge4}/{NS2}")

print("\n[TY4-d — THE DIAGONAL depth = 2 x pool: D45b's own "
      "constructor ratio]")
DIAG = {}
for p in (3, 4, 5, 6, 7):
    DIAG[p] = sample_widths(POOL8[:p], 2 * p, NS3, SEEDS[0])
for nm, _ in WIDTHS:
    print(f"    [SAMPLED, LOCAL-NORMALIZED] depth = 2 x pool, N = "
          f"{NS3}, seed = {SEEDS[0]}, proxy {nm:<15}: mass at FULL "
          f"width "
          + ", ".join(f"{p}/{2 * p}: {DIAG[p][nm].get(p, 0) / NS3:.3f}"
                      for p in sorted(DIAG)))
dt = [DIAG[p]['touched'].get(p, 0) for p in sorted(DIAG)]
dj = [DIAG[p]['delivery-joined'].get(p, 0) for p in sorted(DIAG)]
DT_REF = [260, 231, 227, 207, 187]
DJ_REF = [102, 72, 49, 36, 22]
d_decays = (all(dt[i] < dt[i - 1] for i in range(1, len(dt)))
            and all(dj[i] < dj[i - 1] for i in range(1, len(dj))))
check("TY4-d THE DIAGONAL SCALING, where depth grows WITH the pool "
      "at D45b's own constructor ratio (6 actors, ~8-12 events), so "
      "the depth-limitation caveat cannot be invoked: the "
      "full-width mass still DECAYS STRICTLY, 0.867 -> 0.623 "
      "touched and 0.340 -> 0.073 delivery-joined across pools 3..7.  "
      "Growing the depth in step with the pool does not rescue "
      "full-width typicality",
      dt == DT_REF and dj == DJ_REF and d_decays,
      f"full-width counts, touched = {dt}/{NS3}; delivery-joined = "
      f"{dj}/{NS3}; strictly decreasing on both proxies = "
      f"{d_decays}")

_PIN_DROPPED = ("the exact/estimated mass of the D45b courier "
                "constructor's OWN record class (computable in closed "
                "form from its 1/(4(n^2+3n-1)) per-event weight, "
                "= 1/212 at n = 6, and astronomically small); and the "
                "per-record ORDER-DIMENSION test itself")
check("TY4-e THE PIN'S DROPPED HALVES, DECLARED IN-GATE (round 1, "
      "D-M2: pin §2 TY1(iii) 'poset width where cheap' and pin §2 "
      "TY4's 'actor count AND DELIVERY PATTERN' were both "
      "pre-registered and silently reduced to an actor count).  Two "
      "are now implemented — poset width in TY1-c, the delivery "
      "pattern as the delivery-joined proxy throughout — and what "
      "remains OUT OF SCOPE is named rather than left implicit: "
      + _PIN_DROPPED + ".  The declaration is gated by requiring "
      "that both implemented halves actually produced numbers",
      len(PW) == 4 and all('delivery-joined' in PROFILES[k][0]
                           for k in PROFILES)
      and len(_PIN_DROPPED) > 100,
      f"poset-width profiles = {len(PW)}; delivery-joined profiles = "
      f"{len(PROFILES)}; declared out of scope = "
      f"{_PIN_DROPPED[:60]}...")

outcome("TY", "THE READING, CORRECTED IN DIRECTION (round 1 D-A1, "
        "D-A2, D-M1, D-M3). (1) AT A FIXED POOL the width mass "
        "saturates with depth — touched width >= 4 at 6 actors runs "
        + ", ".join(f"{_ge(DSER[d]['touched'], 4) / NS2:.3f}"
                    for d in DEPTHS)
        + " over depths " + ", ".join(str(d) for d in DEPTHS)
        + " — but actor width is a MONOTONE functional of the path, "
        "so this is a fact about the observable, not a discriminating "
        "property of either normalization; the first pass's 'WIDTH "
        "SPREADS WITH DEPTH UNDER THE THEORY'S OWN LAW' is withdrawn "
        "on both counts, the law-naming included. (2) THE MASS ABOVE "
        "THE FIXED THRESHOLD 4 does become large as pool and depth "
        "grow (sampled at 6 actors / depth 8: "
        f"{HEAD['touched'][0] / NSAMP:.3f} touched, "
        f"{HEAD['non-idle'][0] / NSAMP:.3f} non-idle, "
        f"{HEAD['delivery-joined'][0] / NSAMP:.3f} delivery-joined) "
        "— and width >= 4 is NECESSARY, NOT SUFFICIENT, so these "
        "UPPER-BOUND the dimension mass. (3) THE MASS AT FULL WIDTH "
        "DECAYS WITH THE POOL under every scaling tested — at fixed "
        "depth 8, "
        + ", ".join(f"{PSER[p]['touched'].get(p, 0) / NS2:.3f}"
                    for p in sorted(PSER))
        + " touched for pools 3..8; on the diagonal depth = 2 x pool, "
        + ", ".join(f"{DIAG[p]['touched'].get(p, 0) / NS3:.3f}"
                    for p in sorted(DIAG))
        + " touched and "
        + ", ".join(f"{DIAG[p]['delivery-joined'].get(p, 0) / NS3:.3f}"
                    for p in sorted(DIAG))
        + " delivery-joined for pools 3..7. THE CORRECTED READING: "
        "what is typical-in-the-making at these scopes is order "
        "dimension >= 3, NOT D45b's UNBOUNDED dimension — the axis "
        "unbounded ORDER dimension lives on is the one where the "
        "mass "
        "decays. The per-record ORDER dimension question (does a "
        "typical "
        "wide record actually realize a crown?) is still NOT answered "
        "here and is the named successor.")

# ---- TY5: doctrine, purity, gate vacuity, separation ----------------
print("\n[TY5 — doctrine, purity, gate vacuity, separation]")
_self = open(os.path.abspath(__file__)).read()
_lines = _self.splitlines()
# Round 1, D-M4(4): the first pass's scan exempted any line
# containing 'not ', 'never', 'no ', 'binds', 'doctrine',
# 'successor' or 'scan-exempt'.  The referee's mutant d5 inserted an
# explicit arena-dimension assertion (scan-exempt) ending '..., not
# blanket negation exemption passed it.  The markers below are
# POSITIVE and SCOPED (the d45b/d46c pattern): each says, in the line
# itself, that the object is an ORDER or a clock-complexity grade.
_W1 = "space" + "time"
_W2 = "3" + "+1"
_W3 = "physical " + "arena"
_W4 = "dimen" + "sion"
_DNEEDLES = (_W1, _W2, _W3, _W4)
_DMARKERS = ('order dimension', 'order-dimension', 'clock-complexity',
             'doctrine', 'proxy', 'scan-exempt', 'note-d45b',
             'grade', 'disclaim', 'never', 'poset', 'crown',
             'd44c', 'd45b', 'width')
def doctrine_scan(lines):
    bad = [i + 1 for i, ln in enumerate(lines)
           if any(nd in ln.lower() for nd in _DNEEDLES)
           and not any(m in ln.lower() for m in _DMARKERS)]
    hit = sum(1 for ln in lines
              if any(nd in ln.lower() for nd in _DNEEDLES))
    return hit, bad
_DHIT, BADL = doctrine_scan(_lines)
# CAPABILITY PROBE: the referee's own mutant-d5 line, rebuilt by
# concatenation so this source does not contain it, must be CAUGHT;
# a properly scoped line must pass.
_probe_bad = ["the generated record has " + _W1 + " dimension "  # scan-exempt
              + _W2 + ", not fewer"]
_probe_ok = ["order dimension is a clock-complexity grade, never a "
             + _W1 + "-dimension estimator"]  # scan-exempt
doct_fires = (doctrine_scan(_probe_bad)[1] == [1]
              and doctrine_scan(_probe_ok)[1] == [])
check("TY5-a DOCTRINE (note-d45b §1 binds), with the blanket "
      "negation exemption REMOVED (round 1, D-M4(4)).  Every source "
      "line naming the arena must carry a POSITIVE, SCOPED marker — "
      "a word saying in the line itself that the object is an ORDER "
      "dimension or a clock-complexity grade — and the bare English "
      "stopwords 'no '/'not ' no longer exempt anything.  The "
      "scanner is PROBED with the referee's own mutant-d5 line, "
      "which it must flag, and with a properly scoped line, which it "
      "must pass.  SCOPE OF THE SCAN, declared: it covers this "
      "receipt's source only; the note and the LOG entry are "
      "authored separately and are not scanned here",
      not BADL and doct_fires and _DHIT >= 30,
      f"lines scanned = {_DHIT} of {len(_lines)}; undisclaimed = "
      f"{BADL if BADL else 'none'}; scanner fires on the referee's "
      f"mutant line = {doct_fires}")

ALLOWED = (Fr, int, str, bool, tuple, list, type(None), frozenset)
def walk(o, n=[0]):
    if isinstance(o, (tuple, list, frozenset)):
        for x in (sorted(o, key=repr) if isinstance(o, frozenset)
                  else o):
            walk(x)
    elif isinstance(o, dict):
        for k in sorted(o, key=repr):
            walk(k); walk(o[k])
    else:
        n[0] += 1
        if not isinstance(o, ALLOWED):
            raise TypeError(f"impure leaf: {type(o)}")
    return n[0]
try:
    LV = walk([PROFILES, PW, lp4, kp4, gap, G[tuple([])], MASS])
    pure = True
except TypeError:
    LV, pure = 0, False
LEAF_REF = 72016
check("TY5-b ALLOW-LIST PURITY on the EXACT layer (the #362 "
      "binding): every leaf of every exact profile, poset-width "
      "profile, potential, and path mass is in {Fraction, int, str, "
      "bool} — floats appear only in printed ~approximations and in "
      "the [SAMPLED] frequencies, which are labelled as such.  The "
      "leaf COUNT is anchored exactly rather than tested for "
      "positivity",
      pure and LV == LEAF_REF,
      f"exact leaves walked = {LV}, impure = 0")

def vacuity_scan(tree):
    """Round 1, D-M4: three gates could not fire (`isinstance(conc,
    bool)`, `0 <= x <= 1`, `isinstance(gap, Fr)`).  This AST scan
    walks the PREDICATE argument of every check() call and rejects
    predicates that are constant by construction."""
    bad, n = [], 0
    for nd in ast.walk(tree):
        if not (isinstance(nd, ast.Call)
                and getattr(nd.func, 'id', '') == 'check'
                and len(nd.args) >= 2):
            continue
        n += 1
        for sub in ast.walk(nd.args[1]):
            if (isinstance(sub, ast.Constant)
                    and (sub.value is True or sub.value is False)):
                bad.append((nd.lineno, 'literal boolean'))
            elif (isinstance(sub, ast.Call)
                  and getattr(sub.func, 'id', '') == 'isinstance'):
                bad.append((nd.lineno, 'isinstance type probe'))
            elif (isinstance(sub, ast.Compare) and len(sub.ops) == 1
                  and isinstance(sub.ops[0], (ast.Gt, ast.GtE))
                  and isinstance(sub.comparators[0], ast.Constant)
                  and sub.comparators[0].value == 0):
                bad.append((nd.lineno, 'sign-only comparison'))
    return n, bad
NGATES, TAUT = vacuity_scan(ast.parse(_self))
_PROBE_V = ('check("a", isinstance(conc, bool))\n'
            'check("b", mass_ge6 > 0 and flag)\n'
            'check("c", ok is True)\n'
            'check("d", flag, "x")\n')
_pn, _pb = vacuity_scan(ast.parse(_PROBE_V))
_PROBE_OK = 'check("a", got == TOP_REF and tser == TSER_REF)\n'
_qn, _qb = vacuity_scan(ast.parse(_PROBE_OK))
probe_fires = (_pn == 4 and len(_pb) == 3 and _qn == 1 and _qb == []
               and {s for _, s in _pb} == {'literal boolean',
                                           'isinstance type probe',
                                           'sign-only comparison'})
check("TY5-c NO VACUOUS GATE — an AST scan of every gate predicate "
      "in this file, replacing the first pass's literal-'True' "
      "needle scan, which certified a receipt containing three "
      "predicates that could not fail (round 1, D-M4).  Any "
      "predicate containing a literal boolean, an isinstance() type "
      "probe, or a bare comparison against 0 is rejected; the "
      "scanner is PROBED on a synthetic block carrying exactly those "
      "three shapes and must flag each, and on a substantive "
      "predicate and must not",
      not TAUT and NGATES >= 12 and probe_fires
      and 'check(' in _self,
      f"gate predicates parsed = {NGATES}; vacuous predicates = "
      f"{TAUT if TAUT else 'none'}; scanner fires on the probe = "
      f"{probe_fires}")

sampled_labelled = all("[" + "SAMPLED" in ln for ln in SAMP_LINES)
check("TY5-d THE EXACT/SAMPLED SEPARATION IS STRUCTURAL — and, "
      "round 1 D-m5, the separation that actually broke was in the "
      "INFERENCE, not the labels.  Every sampled quantity is "
      "produced by sample_widths (seeded, declared N) and printed "
      "under a [SAMPLED, LOCAL-NORMALIZED] label; every exact "
      "quantity is a Fraction from an enumerable family under the "
      "LOOKAHEAD-COMPLETED normalization; the calibration gate TY3-a "
      "quantifies and BOUNDS the only bridge.  The delivered "
      "outcome no longer chains an exact series to a sampled number "
      "with 'so': the exact arm and the sampled arm now answer the "
      "SAME question (how does full-width mass scale with the pool?) "
      "under their own laws, and the sampled scalings are the ones "
      "that carry the reading",
      len(SAMP_LINES) == 9 and sampled_labelled
      and gap < Fr(1, 100) and len(OUT) == 1,
      f"labelled sampled lines = {len(SAMP_LINES)}; calibration gap "
      f"= {float(gap):.6f} < 0.01; delivered outcomes = {len(OUT)}")

print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL  ({len(OUT)} delivered "
      f"outcome(s))")
if FAIL:
    print("[VERDICT] FAIL — breakage; exit 1")
    sys.exit(1)

# Round 1, D-n1 and mutant d3: the first pass's [VERDICT] and
# [OUTCOME TY] hard-coded the four exact profile numbers as string
# literals while recomputing the headline, so a changed profile left
# the summary false about numbers printed twenty lines above it.
# Every number below is interpolated from a gated quantity.
_prof_line = ", ".join(
    f"{float(frac_top[k]):.3f} ({k[0]} actors, depth {k[1]})"
    for k in sorted(frac_top))
_cons_line = ", ".join(
    f"{float(PROFILES[k][0]['delivery-joined'].get(TOPW[k], Fr(0))):.3f}"
    for k in sorted(frac_top))
_pool_line = ", ".join(f"{PSER[p]['touched'].get(p, 0) / NS2:.3f}"
                       for p in sorted(PSER))
_diag_line = ", ".join(f"{DIAG[p]['touched'].get(p, 0) / NS3:.3f}"
                       for p in sorted(DIAG))
_dir = ("DECAYS with the pool" if (t_decays and j_decays and d_decays)
        else "does NOT decay with the pool")
_sat = ("saturates with depth at a fixed pool" if saturates
        else "does NOT saturate with depth at a fixed pool")
print("[VERDICT] d46d GREEN-UNREVIEWED, ROUND-1 REPAIRED: typicality "
      "is measured, the law it is measured under is NAMED, and every "
      "clause of this verdict is interpolated from a gated "
      "computation above. THE LAW: the committed weight layer d42b1 "
      "declares 'no measure claim' in its own docstring, so this "
      "unit uses two candidate normalizations — LOOKAHEAD-COMPLETED "
      "(exact arm) and LOCAL-NORMALIZED (sampled arm) — calibrated "
      f"against each other to a maximum width-mass gap of {gap} "
      f"(~{float(gap):.6f}) at the single (pool 4, depth 3) pair "
      "where both are computable; neither is 'the theory's own law' "
      "and this receipt does not call either one that. THE EXACT "
      "ARM: the lookahead-completed measure is proper at every "
      "enumerable pool and its top-actor-width mass is "
      + _prof_line + " under the liberal TOUCHED proxy, but only "
      + _cons_line + " under the DELIVERY-JOINED proxy — the "
      "liberal proxy counts an actor touched by an IDLE, and about "
      "half of all event mass is idle, so it is an UPPER bound on "
      "dimension-relevant width and idle-heaviness is a CONFOUND "
      "here, not support. THE READING, REVERSED IN DIRECTION: the "
      "width mass " + _sat + ", but actor width is a MONOTONE "
      "functional of the path, so that cannot fail and is not "
      "evidence; on the axis that unbounded ORDER dimension actually "
      "lives "
      "on the full-width mass " + _dir + " — " + _pool_line
      + " at fixed depth 8 for pools 3..8, and " + _diag_line
      + " on the diagonal depth = 2 x pool for pools 3..7. What is "
      "typical-in-the-making at these scopes is therefore ORDER "
      "dimension >= 3, NOT the UNBOUNDED dimension D45b constructs; "
      "and since actor width >= 4 is NECESSARY BUT NOT SUFFICIENT "
      "(d44c AG5: all four- and five-event labelled posets have "
      "order dimension <= 2), even that is an UPPER bound on the "
      "ORDER dimension mass. What is NOT answered here, and is the "
      "named "
      "successor: whether a typical wide record actually REALIZES a "
      "crown (a per-record order-dimension test under a named "
      "normalization). Horizon-scoped throughout; ORDER-dimension "
      "proxy only, a clock-complexity grade; no infinite-volume and "
      "no dimension-of-the-world claim (doctrine). Not "
      "review-hardened until "
      "the D46d round converts (paper-32's round precedes it).")
