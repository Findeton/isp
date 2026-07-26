#!/usr/bin/env python3
"""
d60_crystal_exact.py — v10 D60: the crystal question.
Pin: note-d60-crystal-question-pin.md (STRICT, LOG #447, before code).

**ROUND-1 REVIEWED AND REPAIRED (2026-07-26).**  Independent hostile
review `v10/reviews/batch-round1-d50-to-d60.md` — REVISE, 0 BLOCKER /
3 MAJOR / 5 MINOR / 3 NIT.  **The object is real and it is FORCED**: the
brick record was rebuilt independently, re-driven with all eight actors
offered at every one of the 65 steps, and every specification matched
exactly one menu entry.  Nothing about the construction is in doubt.  The
findings are about what the numbers are compared to, what they are a
function of, and which metric was chosen:

  * MAJOR 1 — the comparators were cited from D58's INVALID M^{3+1}
    control (32 distinct points wearing 120 labels).  They are now
    RECOMPUTED with D58's own repaired instrument on genuine sprinklings.
    The OVERLAP claim strengthens (0.65 against 0.048-0.120, not against
    0.54).  The HOMOGENEITY claim does not: against genuine M^{3+1} the
    brick sits INSIDE the sprinkling band, which is what the pin
    pre-registered ("comparable to the sprinkling floor") — the committed
    LOG overstated its own pin.
  * MAJOR 2 — 77% is a function of two unfixed blueprint parameters.
    Both sweeps are now RUN AND REPORTED as parameters, not hidden
    constants, and the mechanism statement they license (the shortfall
    from 1 is entirely BOUNDARY) is gated.
  * MAJOR 3 — "sprinkling-grade on both metrics" fails on a third,
    equally natural metric: CHART WIDTH.  At d = 2 the brick has no
    4-direction chart at any parameter setting tried, while genuine
    sprinklings carry them at 42-65% of events.  The honest statement is
    homogeneity-and-overlap tiling with THIN charts, and it is what C5
    now says; C5 also reports the d = 3 reading, where the brick does
    reach |D| >= 4.
  * MINOR 1 — comparators imported as exact Fractions, not re-typed from
    floor-rounded printouts.
  * MINOR 2 — the dead `WALK` variable is now read by a predicate.
  * MINOR 3 — C5/C6 labelled as the reporting gates they are.
  * MINOR 4 — at d = 3 the homogeneity ordering against M21 REVERSES;
    reported, and the d = 2 scope of the claim is said aloud.
  * MINOR 5 — no result note; `note-d60-crystal-result.md` written with
    this repair.
  * NIT 1 — one Fraction, reported one way.
  * NIT 3 — CRYSTAL-2D's phase generator degenerates at K = 3; reported.

CRYSTAL-1D (brick wall) and CRYSTAL-2D (grid): re-delivery circuits as
lattices worn as records; atlas metrics via the committed (and round-1
repaired) D58 extraction.
Exit 1 only on anchor breakage; refusals are exit-0 deliverables.
"""
import ast, sys
from collections import defaultdict, Counter
from fractions import Fraction as Fr
from itertools import combinations, permutations, product
sys.setrecursionlimit(300000)
PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

print("[D60 — the crystal question, ROUND-1 REPAIRED]")
print("  banner: can the grammar TILE?  Blueprints from the pin; every")
print("  event menu-selected; atlas metrics AND comparators from the")
print("  round-1 repaired D58 instrument, recomputed here rather than")
print("  re-typed; the two blueprint parameters SWEPT and reported; the")
print("  chart-width metric reported beside the other two; orderings")
print("  reported whichever way they land.")

_st = open('v10/code/d42b1_transport_exact.py').read()
nst = {}
exec(_st[:_st.index('print("[d42b1')], nst)
candidates_for, event_poset, V0 = (nst['candidates_for'],
                                   nst['event_poset'], nst['V0'])


def _ext(path, marker, names=(), extra=None):
    t = ast.parse(open(path).read())
    keep = [n for n in t.body if isinstance(n, (ast.FunctionDef,
            ast.ClassDef)) or (isinstance(n, ast.Assign)
            and any(isinstance(x, ast.Name) and x.id in names
                    for x in n.targets))]
    g = {'Fr': Fr, 'combinations': combinations, 'Counter': Counter,
         'permutations': permutations, 'product': product,
         'defaultdict': defaultdict, 'sys': sys}
    if extra:
        g.update(extra)
    exec(compile(ast.fix_missing_locations(ast.Module(body=keep,
         type_ignores=[])), marker, 'exec'), g)
    return g


g47 = _ext('v10/code/d47a_sky_instrument_exact.py', 'd47a',
           ('CYCLIC_CAP', 'SKYB_DEPTH'))
sky, heights = g47['sky'], g47['heights']
mink3, latt3 = g47['mink_order'], g47['lattice_points']
g55c = _ext('v10/code/d55c_m31_control_exact.py', 'd55c')
mink4, latt = g55c['mink4'], g55c['latt']
g58 = _ext('v10/code/d58_atlas_instrument_exact.py', 'd58', (),
           extra={'sky': sky, 'heights': heights})
d58_atlas, d58_covers = g58['atlas'], g58['covers']

check("C0 anchors: transport layer (committed d42b1), sky instrument "
      "(committed d47a), the ROUND-1 REPAIRED sprinkling generator "
      "(d55c) and **the atlas instrument itself (d58)** — all single "
      "sources by AST extraction.  Round-1 MINOR 1: the committed "
      "receipt re-typed D58's comparators as two-digit decimals read off "
      "a floor-rounded printout, one of them in the unit's own favour; "
      "they are now RECOMPUTED with D58's own code on genuine records",
      all(callable(f) for f in (candidates_for, sky, d58_atlas, latt)),
      "loaded")


def poset_of(h):
    pred = event_poset(list(h))
    n = len(h)
    return [[i in pred[j] for j in range(n)] for i in range(n)]


class B:
    def __init__(self, actors):
        self.actors = actors
        self.H = []
        self.refusal = None
        self.maxhits = 0

    def pick(self, inits, spec, label):
        if self.refusal:
            return None
        menu = candidates_for(list(self.H), tuple(inits))
        hits = sorted((e for e, q in menu if spec(e)), key=repr)
        self.maxhits = max(self.maxhits, len(hits))
        if not hits:
            self.refusal = (label, len(self.H))
            print(f"  [REFUSAL] '{label}' at prefix {len(self.H)}; "
                  f"menu types {sorted({e[0] for e, q in menu})}")
            return None
        self.H.append(hits[0])
        return hits[0]


def mint_and_spread(b, chain):
    """A1 mints v1; broadcast along `chain` by deliveries."""
    a0 = chain[0]
    b.pick((a0,), lambda e: e[0] == 'p' and e[1] == a0 and e[2] == V0
           and e[3] == 0, f"{a0} proposes")
    b.pick((a0,), lambda e: e[0] == 'r' and e[1] == a0, f"{a0} arbitrates")
    V1 = None
    if not b.refusal:
        menu = candidates_for(list(b.H), (a0, chain[1]))
        dv = sorted({e[3] for e, q in menu
                     if e[0] == 'd' and e[3] != V0}, key=repr)
        V1 = dv[0] if dv else None
    for s, r in zip(chain, chain[1:]):
        b.pick((s, r), lambda e, s=s, r=r: e[0] == 'd' and e[1] == s
               and e[2] == r and e[3] == V1, f"spread {s}->{r}")
    return V1


def dl(b, s, r, V1):
    b.pick((s, r), lambda e, s=s, r=r: e[0] == 'd' and e[1] == s
           and e[2] == r and e[3] == V1, f"{s}->{r}")


def brick(M, ROUNDS, verbose=False):
    """The generic even-m brick pairing; every event menu-selected."""
    ring = [f"R{i}" for i in range(M)]
    b = B(tuple(ring))
    V1 = mint_and_spread(b, ring)
    for t in range(ROUNDS):
        pairs = ([(i, i + 1) for i in range(0, M, 2)] if t % 2 == 0
                 else [(i, (i + 1) % M) for i in range(1, M, 2)])
        for (i, j) in pairs:
            s, r = ring[i], ring[j]
            if t % 4 >= 2:
                s, r = r, s
            dl(b, s, r, V1)
    return b


def profile(C, pop=None):
    """D58's atlas restricted to a POPULATION of events (the poset is
    left whole; only the metric population changes).  Gated in C7 to
    agree with D58's own atlas when pop is everything."""
    n = len(C)
    P = set(range(n)) if pop is None else set(pop)
    h = heights(C)
    out = {}
    for d in (2, 3):
        DIRS = {e: set(sky(C, e, 'B', d)[0]) for e in range(n)}
        widths = [len(DIRS[e]) for e in sorted(P)]
        om = []
        for (e, e2) in d58_covers(C):
            if e not in P or len(DIRS[e]) < 2:
                continue
            d2 = set(sky(C, e2, 'B', d - 1)[0])
            om.append(Fr(len(DIRS[e] & d2), len(DIRS[e])))
        out[d] = {'n': len(P),
                  'h2': Fr(sum(1 for w in widths if w >= 2), len(P)),
                  'h3': Fr(sum(1 for w in widths if w >= 3), len(P)),
                  'h4': Fr(sum(1 for w in widths if w >= 4), len(P)),
                  'max': max(widths), 'mean': Fr(sum(widths), len(P)),
                  'pairs': len(om),
                  'om': (sum(om) / len(om)) if om else None}
    return out


def show(name, r):
    for d in (2, 3):
        x = r[d]
        print(f"  {name} d={d}: events={x['n']}, |D|>=2: {x['h2']} "
              f"(~{float(x['h2']):.4f}), |D|>=4: {x['h4']} "
              f"(~{float(x['h4']):.4f}), max|D|={x['max']}, "
              f"mean|D|={float(x['mean']):.2f}, pairs={x['pairs']}, "
              f"mean omega={x['om']} (~{float(x['om']):.4f})")


# ------------------------------------------------- CRYSTAL-1D: brick
print("\n[CRYSTAL-1D — the brick wall, m = 8, 14 rounds]")
M, ROUNDS = 8, 14
b1 = brick(M, ROUNDS)
check("C1 CRYSTAL-1D IS ADMISSIBLE END TO END AND THE RECORD IS FORCED: "
      f"the brick circuit ({len(b1.H)} events over {M} actors, {ROUNDS} "
      "rounds of alternating re-deliveries) — every event offered by the "
      "layer's own menu, and every specification matched by EXACTLY ONE "
      "candidate, so nothing was tie-broken.  The pre-registered lean "
      "(re-delivery circuits run indefinitely) holds",
      b1.refusal is None and b1.maxhits == 1,
      f"events = {len(b1.H)}, refusal = {b1.refusal}, max menu hits per "
      f"specification = {b1.maxhits}")
C1P = poset_of(b1.H)
A1 = profile(C1P)
show('brick m=8', A1)

# ------------------------------------------------- CRYSTAL-2D: grid
print("\n[CRYSTAL-2D — the 3x3 grid, 12 phases]")
K = 3
GRID = [f"G{i}{j}" for i in range(K) for j in range(K)]
def gid(i, j):
    return f"G{i % K}{j % K}"
b2 = B(tuple(GRID))
V2 = mint_and_spread(b2, GRID)
PHASES = 12
_phase_sets = []
for t in range(PHASES):
    ph = t % 4
    if ph == 0:
        pairs = [(gid(i, j), gid(i, j + 1)) for i in range(K)
                 for j in range(0, K - 1, 2)]
    elif ph == 1:
        pairs = [(gid(i, j), gid(i, j + 1)) for i in range(K)
                 for j in range(1, K - 1, 2)]
    elif ph == 2:
        pairs = [(gid(i, j), gid(i + 1, j)) for j in range(K)
                 for i in range(0, K - 1, 2)]
    else:
        pairs = [(gid(i, j), gid(i + 1, j)) for j in range(K)
                 for i in range(1, K - 1, 2)]
    _phase_sets.append(tuple(sorted(pairs)))
    for (s, r) in pairs:
        if (t // 4) % 2 == 1:
            s, r = r, s
        dl(b2, s, r, V2)
_distinct_phases = len(set(_phase_sets))
print(f"  [NIT 3, round 1] at K = {K} the phase generator "
      f"`range(0, K-1, 2)` and `range(1, K-1, 2)` each yield a SINGLE "
      f"index, so the {PHASES} phases reduce to {_distinct_phases} "
      f"distinct pair sets of {len(_phase_sets[0])} deliveries each — "
      f"the grid is an even smaller object than '3x3, 46 events' "
      f"suggests, which reinforces the unit's own 'size is the named "
      f"residue'")
check("C2 CRYSTAL-2D IS ADMISSIBLE END TO END: the grid circuit "
      f"({len(b2.H)} events over {K * K} actors, {PHASES} phases; "
      f"{_distinct_phases} distinct phase pair-sets, reported)",
      b2.refusal is None, f"events = {len(b2.H)}, refusal = {b2.refusal}")
A2 = profile(poset_of(b2.H))
show('grid 3x3', A2)

# ------------------------------------- the comparators, RECOMPUTED
print("\n[the comparators — RECOMPUTED with D58's own repaired "
      "instrument on genuine sprinklings (round-1 MAJOR 1 / MINOR 1)]")
SPR = {}
for box in (30, 40, 60, 90):
    SPR[('M21', box)] = d58_atlas(mink4(latt(120, 2, box, 8)),
                                  f'M21 box={box}', quiet=True)
for box in (20, 24, 40, 48, 60, 90):
    SPR[('M31', box)] = d58_atlas(mink4(latt(120, 3, box, 8)),
                                  f'M31 box={box}', quiet=True)
SPR[('M21', 'd47a')] = d58_atlas(mink3(latt3(120, box=60)),
                                 'M21 d47a', quiet=True)
ENG = {'SH4': Fr(17, 44), 'SH5': Fr(30, 84)}   # D58's committed records
WALK = Fr(2, 30)                               # D58's generic 2-actor walk
HOM = sorted(SPR[k][2]['h2'] for k in SPR)
W4 = sorted(SPR[k][2]['h4'] for k in SPR)
OM = sorted(SPR[k][2]['om'] for k in SPR)
SPR_LO, SPR_HI = HOM[0], HOM[-1]
ENGINEERED_CEIL = max(ENG.values())
for k in sorted(SPR, key=repr):
    r = SPR[k][2]
    print(f"    {k[0]} box={k[1]:>5}: homog {float(r['h2']):.4f}, "
          f"|D|>=4 {float(r['h4']):.4f}, mean|D| {float(r['mean']):.2f}, "
          f"max|D| {r['max']:2d}, mean omega {float(r['om']):.4f}")
print(f"    BAND homogeneity [{SPR_LO}, {SPR_HI}] "
      f"(~[{float(SPR_LO):.4f}, {float(SPR_HI):.4f}]); |D|>=4 "
      f"[{W4[0]}, {W4[-1]}] (~[{float(W4[0]):.4f}, "
      f"{float(W4[-1]):.4f}]); mean omega [{float(OM[0]):.4f}, "
      f"{float(OM[-1]):.4f}]")
print(f"    engineered ceiling = {ENGINEERED_CEIL} "
      f"(~{float(ENGINEERED_CEIL):.4f}); generic 2-actor walk = {WALK} "
      f"(~{float(WALK):.4f})")

h1, h2 = A1[2]['h2'], A2[2]['h2']
om1, om2 = A1[2]['om'], A2[2]['om']
_in_band = SPR_LO <= h1 <= SPR_HI
check("C3 [THE CRYSTAL VERDICT, RESTATED BY ROUND 1] Both crystals clear "
      "the engineered ceiling by a wide margin — that is the falsifiable "
      "part and it survives every correction.  **CORRECTED (MAJOR 1): "
      "the brick's homogeneity is NOT 'above' the sprinkling comparator; "
      "against GENUINE M^{3+1} sprinklings it sits INSIDE the band.**  "
      "The committed LOG's 'above M31's 73%' was a claim against a "
      "non-sprinkling (32 points wearing 120 labels).  The licensed "
      "statement is the pin's own pre-registration: COMPARABLE TO THE "
      "SPRINKLING BAND.  **SCOPE (MINOR 4): this is a d = 2 statement** "
      "— at d = 3 the brick reads "
      f"{float(A1[3]['h2']):.4f} against M21's "
      f"{float(SPR[('M21', 'd47a')][3]['h2']):.4f} and the ordering "
      "REVERSES",
      h1 > ENGINEERED_CEIL and h2 > ENGINEERED_CEIL,
      f"brick = {h1} (~{float(h1):.4f}), inside the sprinkling band "
      f"[{float(SPR_LO):.4f}, {float(SPR_HI):.4f}] = {_in_band}; grid = "
      f"{h2} (~{float(h2):.4f}); engineered ceiling = "
      f"{float(ENGINEERED_CEIL):.4f}; generic walk = {float(WALK):.4f}")

check("C4 [THE OVERLAP CLAIM — IT STRENGTHENS UNDER CORRECTION] mean "
      "omega at d = 2 against the RECOMPUTED sprinkling comparators.  "
      "The committed receipt compared 0.65 against 0.12 and 0.54, the "
      "second of which came from the degenerate control; against genuine "
      "sprinklings the whole comparator range is below the brick.  D58's "
      "round-1 MAJOR 2 qualifies what this means: omega is a CHART-SIZE "
      "RATIO along covers and systematically favours THIN-charted "
      "records, which the brick is (C5)",
      om1 > OM[-1] and om2 is not None,
      f"brick = {om1} (~{float(om1):.4f}), grid = "
      f"(~{float(om2):.4f}); genuine sprinkling range "
      f"[{float(OM[0]):.4f}, {float(OM[-1]):.4f}]; the withdrawn "
      f"degenerate comparator read 0.54")

print("\n[C5 CHART WIDTH — the third metric, round-1 MAJOR 3]")
W4d = {d: sorted(SPR[k][d]['h4'] for k in SPR) for d in (2, 3)}
MXd = {d: max(SPR[k][d]['max'] for k in SPR) for d in (2, 3)}
for d in (2, 3):
    print(f"    d = {d}:  brick |D|>=4 {float(A1[d]['h4']):.4f} "
          f"(max|D| {A1[d]['max']})  |  grid {float(A2[d]['h4']):.4f} "
          f"(max|D| {A2[d]['max']})  |  genuine sprinklings "
          f"[{float(W4d[d][0]):.4f}, {float(W4d[d][-1]):.4f}] "
          f"(max|D| up to {MXd[d]})")
check("C5 [CORRECTED BY ROUND 1 — MAJOR 3] 'ABOVE THE SPRINKLING FLOOR "
      "ON BOTH METRICS' IS NOT 'SPRINKLING-GRADE'.  On a third, equally "
      "natural metric — chart WIDTH, the thing |D| >= 2 is a threshold "
      "of — the brick is at the floor AT THE DEPTH THE HEADLINE IS "
      "STATED AT: at d = 2 it carries NO 4-direction chart anywhere, at "
      "any parameter setting tried (C6), while genuine sprinklings carry "
      "them at 42-65% of their events and reach max|D| 10-17 against the "
      "brick's 3.  **The honest statement is: the grammar tiles at "
      "sprinkling-grade HOMOGENEITY and above-sprinkling OVERLAP, with "
      "THIN charts.**  Reported whichever way it lands: at d = 3 the "
      f"brick DOES reach |D| >= 4 ({A1[3]['h4']}), JUST BELOW the "
      "d = 3 sprinkling band (FORWARD-CORRECTED by D63's round 1, "
      "MAJOR 4: the first repaired draft said 'inside', but 38/65 = "
      "0.5846 < 0.6000, the band's floor) — the width shortfall is "
      "a d = 2 statement in ORDER of severity, exactly as the "
      "homogeneity ordering is (C3).  The unit's own 'the brick is "
      "1+1-thin by design' was honest; what was missing is this "
      "comparison, which D58 had computed and never printed",
      A1[2]['h4'] == 0 and W4d[2][0] > 0 and A1[2]['max'] < MXd[2],
      f"brick |D|>=4 = {A1[2]['h4']} at d = 2 and {A1[3]['h4']} at "
      f"d = 3; sprinkling d = 2 band [{W4d[2][0]}, {W4d[2][-1]}], d = 3 "
      f"band [{W4d[3][0]}, {W4d[3][-1]}]; brick max|D| = "
      f"{A1[2]['max']}/{A1[3]['max']} against sprinkling "
      f"{MXd[2]}/{MXd[3]}")

# ---------------------------------------- MAJOR 2: the parameter sweeps
print("\n[C6 THE TWO BLUEPRINT PARAMETERS — round-1 MAJOR 2: 77% is not "
      "a property of the mechanism, it is a property of (M, R)]")
print("  === ROUNDS sweep at M = 8 ===")
RSW = {}
for R in (4, 8, 14, 20, 30, 50):
    bb = brick(8, R)
    pr = profile(poset_of(bb.H))[2]
    RSW[R] = pr
    print(f"    R={R:3d} ({len(bb.H):3d} ev): homog "
          f"{float(pr['h2']):.4f}  |D|>=4 {float(pr['h4']):.4f}  mean|D| "
          f"{float(pr['mean']):.2f}  omega {float(pr['om']):.4f}"
          + ("   <- COMMITTED" if R == 14 else ""))
print("  === RING-WIDTH sweep at 14 rounds ===")
MSW = {}
for m in (4, 6, 8, 10, 12, 16):
    bb = brick(m, 14)
    pr = profile(poset_of(bb.H))[2]
    MSW[m] = pr
    print(f"    M={m:3d} ({len(bb.H):3d} ev): homog "
          f"{float(pr['h2']):.4f}  max|D| {pr['max']}  omega "
          f"{float(pr['om']):.4f}"
          + ("   <- COMMITTED" if m == 8 else ""))
_rise = RSW[50]['h2'] > RSW[14]['h2'] > RSW[4]['h2']
_fall = MSW[16]['h2'] < MSW[8]['h2'] < MSW[4]['h2']
check("C6 THE HEADLINE NUMBER IS A PARAMETER, AND BOTH ITS PARAMETERS "
      "ARE NOW SWEPT AND PRINTED.  Homogeneity RISES with rounds "
      f"({float(RSW[4]['h2']):.2f} -> {float(RSW[50]['h2']):.2f}) and "
      f"FALLS with ring width ({float(MSW[4]['h2']):.2f} -> "
      f"{float(MSW[16]['h2']):.2f}); the committed 0.769 is the value at "
      "(M = 8, R = 14) and nothing more.  **The mechanism statement, "
      "which is what the scale doctrine asks this unit to certify, is "
      "C7's: the shortfall from 1 is entirely BOUNDARY, so a re-delivery "
      "circuit's homogeneity tends to 1 as it runs.**  Chart width does "
      "NOT move: at d = 2, |D| >= 4 is 0 at every setting tried",
      _rise and _fall and all(RSW[R]['h4'] == 0 for R in RSW)
      and all(MSW[m]['h4'] == 0 for m in MSW),
      f"rounds {sorted(RSW)} -> homog "
      + str([f"{float(RSW[R]['h2']):.4f}" for R in sorted(RSW)])
      + f"; widths {sorted(MSW)} -> homog "
      + str([f"{float(MSW[m]['h2']):.4f}" for m in sorted(MSW)])
      + "; |D|>=4 identically 0 at d = 2 across both sweeps")

# ------------------------------- MAJOR 2 / the prefix and interior controls
print("\n[C7 WHERE THE SHORTFALL LIVES — the circuit-only and interior "
      "controls]")
hs = heights(C1P)
PREFIX = set(range(9))            # mint + arbitrate + 7 spread deliveries
CIRCUIT = set(range(9, len(b1.H)))
lo, hi = min(hs), max(hs)
INTERIOR = {e for e in range(len(b1.H)) if lo + 2 <= hs[e] <= hi - 3}
p_full = A1[2]
p_circ = profile(C1P, CIRCUIT)
p_pre = profile(C1P, PREFIX)
p_int = profile(C1P, INTERIOR)
for nm, pr in (('FULL        ', {2: p_full, 3: A1[3]}),
               ('CIRCUIT-ONLY', p_circ), ('PREFIX-ONLY ', p_pre),
               ('INTERIOR    ', p_int)):
    print(f"    brick {nm} ({pr[2]['n']:2d} events): d=2 homog "
          f"{float(pr[2]['h2']):.4f}  |D|>=3 {float(pr[2]['h3']):.4f}  "
          f"omega {float(pr[2]['om']):.4f}   |   d=3 homog "
          f"{float(pr[3]['h2']):.4f}  omega {float(pr[3]['om']):.4f}")
check("C7 THE MINT-AND-SPREAD PREFIX DEFLATES THE HEADLINE, AND THE "
      "RESIDUAL SHORTFALL IS ENTIRELY BOUNDARY.  The non-lattice prefix "
      "is not inflating the number: the circuit alone reads HIGHER than "
      "the published figure, so the 9 prefix events COST the unit "
      "homogeneity.  Dropping the bottom two and top three height layers "
      "takes the interior to ~0.9, which is the mechanism claim C6 "
      "points at — the circuit tiles, and what is missing is the "
      "record's ends",
      p_circ[2]['h2'] > p_full['h2'] and p_int[2]['h2'] > p_circ[2]['h2'],
      f"full = {float(p_full['h2']):.4f}, circuit-only = "
      f"{float(p_circ[2]['h2']):.4f}, prefix-only = "
      f"{float(p_pre[2]['h2']):.4f}, interior = "
      f"{float(p_int[2]['h2']):.4f} ({p_int[2]['n']} of {len(b1.H)} "
      f"events; d = 3 interior {float(p_int[3]['h2']):.4f})")

_agree = d58_atlas(C1P, 'brick', quiet=True)
check("C8 [ANCHOR] the population-restricted profile used above is D58's "
      "atlas: with the population set to EVERY event it reproduces D58's "
      "own instrument exactly, so the circuit/interior controls are "
      "restrictions of the committed measurement and not a second "
      "instrument",
      all(_agree[d]['h2'] == A1[d]['h2'] and _agree[d]['om'] == A1[d]['om']
          and _agree[d]['max'] == A1[d]['max'] for d in (2, 3)),
      f"d=2 homog {A1[2]['h2']} vs {_agree[2]['h2']}, omega {A1[2]['om']} "
      f"vs {_agree[2]['om']}; d=3 homog {A1[3]['h2']} vs "
      f"{_agree[3]['h2']}")

_ch = [c for c in ast.walk(ast.parse(open(
    'v10/code/d60_crystal_exact.py').read()))
    if isinstance(c, ast.Call) and isinstance(c.func, ast.Name)
    and c.func.id == 'check']
_vac = [c for c in _ch if isinstance(c.args[1], ast.Constant)]
check("C9 AST anti-vacuity (no bare-constant predicates; #403 MA-2 "
      "scope).  Round-1 MINOR 3: the committed C5 (`wmax1 >= 2`) and C4 "
      "(`om1 is not None`) were theorem-passes implied by C3 having "
      "found any 2-direction chart at all; both are gone, replaced by "
      "the width comparison (C5) and the recomputed-comparator ordering "
      "(C4).  Round-1 MINOR 2: `WALK` was assigned and never read; it is "
      f"read here ({float(WALK):.4f} < the engineered ceiling "
      f"{float(ENGINEERED_CEIL):.4f} < both crystals)",
      len(_ch) >= 8 and not _vac and WALK < ENGINEERED_CEIL < min(h1, h2),
      f"check() calls = {len(_ch)}, bare = {len(_vac)}; walk "
      f"{WALK} < ceiling {ENGINEERED_CEIL} < crystals "
      f"{min(h1, h2)}")

print("\n[VERDICT — D60, ROUND-1 REPAIRED]")
print("  THE OBJECT IS REAL AND FORCED: 65 events, 8 actors, every one")
print("  menu-offered, every specification matched by exactly one")
print("  candidate.  Nothing in the round touches the construction.")
print("  THE LICENSED READING, CORRECTED: the grammar tiles at")
print("  sprinkling-grade HOMOGENEITY (inside the band, not above it) "
      "and")
print("  at ABOVE-sprinkling OVERLAP, WITH THIN CHARTS — at d = 2 no")
print("  4-direction chart at any parameter setting tried, against the")
print("  sprinklings' 42-65%, and max|D| 3 against their 10-17.")
print("  d = 2 scope: at d = 3 the homogeneity ordering against M21")
print("  reverses; the overlap ordering holds at both depths.")
print("  THE MECHANISM CLAIM the sweeps license: the shortfall from 1 is")
print("  boundary, so a re-delivery circuit's homogeneity tends to 1 as")
print("  it runs; 0.769 is a snapshot at (M = 8, R = 14).")
print("  SCOPE carried: grammar layer; transfer to the identified click")
print("  law runs through paper 29's missing map (D59); no typicality")
print("  claim; no object claim (#440).  Size remains the named residue.")
print(f"\n[d60] {PASS} PASS / {FAIL} FAIL")
sys.exit(1 if FAIL else 0)
