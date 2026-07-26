#!/usr/bin/env python3
"""
d63_wide_crystal_exact.py — v10 D63: THE WIDE CRYSTAL.
Pin: note-d63-wide-crystal-pin.md (STRICT, committed before this file).

THE QUESTION (pin §1).  D60 left the sharp residue: can ANY grammar
record carry sprinkling-grade chart WIDTH (|D| >= 4 at d = 2) while
keeping sprinkling-band tiling homogeneity?  D54 shows transport buys
width (shatter records reach |D| >= 4 at homogeneity 0.357-0.386, far
below the band); D60 shows tiling buys homogeneity (0.7692 in-band,
boundary-limited) with max |D| = 3 at every (M, R) tried.  Do the two
MECHANISMS compose or exclude?

THE OBJECTS (pin §2), both delivery circuits of the committed d42b1
layer, every event menu-selected:
  * WIDE-BRICK(M, R, C, cad): D60's brick circuit spliced with C
    courier actors running D54-style cross-ring deliveries (a delivery
    is a JOIN in both directions — the backflow architecture) at a
    fixed printed cadence.  C = 0 must reproduce D60's brick EXACTLY.
  * DOUBLE-RING(M, R, cpl): two coupled M-rings, both running the
    brick circuit, with `cpl` inter-ring deliveries per round.

PRE-REGISTERED FALSIFIERS (pin §4), decided by the sweep, not asserted:
  F1 the grammar wall  — no swept configuration reaches |D| >= 4 at d = 2;
  F2 the trade-off wall — width only below the homogeneity band;
  F3 THE WIDE CRYSTAL   — some configuration sits IN the band AND
                          carries |D| >= 4 charts.
No verdict sentence may exceed the swept (M, R, C, cpl) family.

HOUSE RULES HELD: committed layers are single sources (AST / text-slice,
never re-implemented; the slice's exit-freedom is GATED, W0a); no
invented thresholds ("band" = the W3 recomputed sprinkling band, "wide"
= D58's |D| >= 4 column, nothing else); anchors are committed numbers
(D60's published row, W0); every gate can fail (AST anti-vacuity, W6);
every swept range and cap printed; exit 0 for substantive negatives,
exit 1 ONLY on W0 anchor breakage.
Run from the repo root: python3 v10/code/d63_wide_crystal_exact.py
"""
import ast, os, subprocess, sys, time
from collections import defaultdict, Counter
from fractions import Fraction as Fr
from itertools import combinations, permutations, product

sys.setrecursionlimit(300000)
T0 = time.time()
PASS = FAIL = 0
ANCHOR_FAIL = False


def check(label, ok, detail="", anchor=False):
    global PASS, FAIL, ANCHOR_FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    if anchor and not ok:
        ANCHOR_FAIL = True
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


print("[D63 — the wide crystal: does tiling homogeneity compose with "
      "chart width?]")
print("  banner: two delivery circuits of the committed layer — D60's")
print("  brick spliced with D54-style couriers, and two coupled rings —")
print("  swept in the courier count C and the inter-ring coupling.  The")
print("  atlas and the eleven genuine sprinkling comparators are RE-RUN")
print("  in this process from D58's own repaired instrument, never")
print("  re-typed.  C = 0 must reproduce D60's published row exactly.")
print("  F1/F2/F3 is DECIDED BY THE SWEEP; orderings reported whichever")
print("  way they land; no claim exceeds the swept family.")

# ======================================================================
# W0a — anchors: every committed layer a single source
# ======================================================================
_SRC42 = 'v10/code/d42b1_transport_exact.py'
_st = open(_SRC42).read()
_cut = _st.index('print("[d42b1')
_slice = _st[:_cut]
nst = {}
exec(compile(_slice, 'd42b1_slice', 'exec'), nst)
candidates_for, event_poset, V0 = (nst['candidates_for'],
                                   nst['event_poset'], nst['V0'])
regs_of, admissible = nst['regs_of'], nst['admissible']


def _no_exit(nodes):
    """No exit call survives in an extracted body (house rule: the
    strip must be GATED, not asserted).  Round-1 NIT 2: the gate now
    also catches bare `exit()`/`quit()` (Name calls) and `os._exit`,
    not only `*.exit` attribute calls."""
    for n in nodes:
        for c in ast.walk(n):
            if isinstance(c, ast.Call):
                if (isinstance(c.func, ast.Attribute)
                        and c.func.attr in ('exit', '_exit')):
                    return False
                if (isinstance(c.func, ast.Name)
                        and c.func.id in ('exit', 'quit')):
                    return False
    return True


_EXTRACTED = {}


def _ext(path, marker, names=(), extra=None):
    """D60's committed extraction idiom: keep only defs/classes (and the
    named module constants), so no module-level statement — print, gate,
    sys.exit — can run."""
    t = ast.parse(open(path).read())
    keep = [n for n in t.body if isinstance(n, (ast.FunctionDef,
            ast.ClassDef)) or (isinstance(n, ast.Assign)
            and any(isinstance(x, ast.Name) and x.id in names
                    for x in n.targets))]
    _EXTRACTED[path] = keep
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
SKYB_DEPTH = g47['SKYB_DEPTH']
g55c = _ext('v10/code/d55c_m31_control_exact.py', 'd55c')
mink4, latt = g55c['mink4'], g55c['latt']
g58 = _ext('v10/code/d58_atlas_instrument_exact.py', 'd58', (),
           extra={'sky': sky, 'heights': heights})
d58_atlas, d58_covers = g58['atlas'], g58['covers']
g60 = _ext('v10/code/d60_crystal_exact.py', 'd60', (),
           extra={'sky': sky, 'heights': heights, 'd58_covers': d58_covers,
                  'candidates_for': candidates_for,
                  'event_poset': event_poset, 'V0': V0})
B, brick = g60['B'], g60['brick']
mint_and_spread, dl = g60['mint_and_spread'], g60['dl']
profile, poset_of, show = g60['profile'], g60['poset_of'], g60['show']

_strip_ok = ('sys.exit' not in _slice
             and all(_no_exit(v) for v in _EXTRACTED.values()))
check("W0a ANCHORS — every layer a SINGLE SOURCE, and the strip is "
      "GATED not asserted: the transport grammar by text-slice from "
      "committed d42b1 (cut at its own banner print), and the sky "
      "instrument (d47a), the repaired sprinkling generator (d55c), THE "
      "ATLAS ITSELF (d58) and **D60's blueprint machinery — its `B` "
      "driver, `mint_and_spread`, `dl`, `brick`, `profile`** — by AST "
      "extraction.  Nothing here re-implements a committed layer; the "
      "brick this unit widens is D60's own function object.  The gate "
      "reads: no `sys.exit` survives the slice or any extracted body",
      all(callable(f) for f in (candidates_for, sky, d58_atlas, latt,
                                brick, profile)) and _strip_ok,
      f"slice = {_cut} of {len(_st)} chars, exit-free = "
      f"{'sys.exit' not in _slice}; extracted bodies = "
      f"{ {p.split('/')[-1]: len(v) for p, v in _EXTRACTED.items()} }, "
      f"all exit-free = {all(_no_exit(v) for v in _EXTRACTED.values())}",
      anchor=True)

# ======================================================================
# THE BLUEPRINTS (pin §2)
# ======================================================================
CADENCE = 1          # courier phase after EVERY brick round (printed)
FULLMENU_BUDGET = 300.0   # seconds per full-menu replay (printed, W1b)
BUILT = {}           # every record this receipt builds, cached


def chords(M, C):
    """Courier k spans the ring chord (k mod M) -> ((k + M/2) mod M).
    At C = M every ring actor is a chord endpoint exactly twice, at
    C = M/2 exactly once; below that the coupling is PARTIAL and the
    lattice is deliberately irregular — that irregularity is part of
    what the sweep measures."""
    return [(k % M, (k + M // 2) % M) for k in range(C)]


def wide_brick(M, R, C, cad=CADENCE):
    """WIDE-BRICK(M, R, C): D60's brick circuit + C couriers.  At C = 0
    this is D60's `brick(M, R)` EVENT FOR EVENT (W0)."""
    ring = [f"R{i}" for i in range(M)]
    cour = [f"K{k}" for k in range(C)]
    ch = chords(M, C)
    b = B(tuple(ring + cour))
    V1 = mint_and_spread(b, ring)
    for t in range(R):
        pairs = ([(i, i + 1) for i in range(0, M, 2)] if t % 2 == 0
                 else [(i, (i + 1) % M) for i in range(1, M, 2)])
        for (i, j) in pairs:
            s, r = ring[i], ring[j]
            if t % 4 >= 2:
                s, r = r, s
            dl(b, s, r, V1)
        if C and (t + 1) % cad == 0:
            for k, (i, j) in enumerate(ch):
                # D54's courier: ring -> EMPTY-ish courier, then courier
                # -> the far ring actor.  Both are joins (backflow).
                dl(b, ring[i], cour[k], V1)
                dl(b, cour[k], ring[j], V1)
    return b


def double_ring(M, R, cpl):
    """DOUBLE-RING(M, R, cpl): two M-rings each running D60's brick
    circuit, with `cpl` inter-ring deliveries per round (direction
    alternating with the round parity)."""
    A = [f"A{i}" for i in range(M)]
    Z = [f"B{i}" for i in range(M)]
    b = B(tuple(A + Z))
    V1 = mint_and_spread(b, A + Z)
    for t in range(R):
        pairs = ([(i, i + 1) for i in range(0, M, 2)] if t % 2 == 0
                 else [(i, (i + 1) % M) for i in range(1, M, 2)])
        for ring in (A, Z):
            for (i, j) in pairs:
                s, r = ring[i], ring[j]
                if t % 4 >= 2:
                    s, r = r, s
                dl(b, s, r, V1)
        for i in range(cpl):
            s, r = A[i], Z[i]
            if t % 2 == 1:
                s, r = r, s
            dl(b, s, r, V1)
    return b


def actors_of(kind, M, C):
    if kind == 'WB':
        return ([f"R{i}" for i in range(M)] + [f"K{k}" for k in range(C)])
    return [f"A{i}" for i in range(M)] + [f"B{i}" for i in range(M)]


def get(kind, M, R, P, cad=CADENCE):
    """Build (once) and measure a swept configuration."""
    key = (kind, M, R, P, cad)
    if key in BUILT:
        return BUILT[key]
    t = time.time()
    b = wide_brick(M, R, P, cad) if kind == 'WB' else double_ring(M, R, P)
    pr = None if b.refusal else profile(poset_of(b.H))
    BUILT[key] = (b, pr, time.time() - t)
    return BUILT[key]


def line(tag, b, pr, dt, d=2):
    if pr is None:
        return f"{tag}: REFUSAL at {b.refusal}"
    x = pr[d]
    return (f"{tag}: n={x['n']:4d} homog {float(x['h2']):.4f}  "
            f"|D|>=4 {float(x['h4']):.4f}  max|D| {x['max']}  "
            f"mean|D| {float(x['mean']):.2f}  omega {float(x['om']):.4f}  "
            f"[{dt:.1f}s]")


print(f"\n[blueprints, printed caps]  SKY-B depths measured = (2, 3) "
      f"(committed SKYB_DEPTH = {SKYB_DEPTH}); courier cadence = "
      f"{CADENCE} (a courier phase after EVERY brick round); courier "
      f"chord rule k -> (k mod M, (k + M/2) mod M), e.g. M = 8, C = 4: "
      f"{chords(8, 4)}; double-ring coupling = the first `cpl` positions, "
      f"direction alternating with round parity; full-menu replay budget "
      f"= {FULLMENU_BUDGET:.0f}s per record.")

if '--probe' in sys.argv:
    # DETERMINISM PROBE (round-1 MINOR 5: the note's determinism claim
    # was gated nowhere, and `regs_of` reads next(iter(frozenset)), so
    # the claim is not idle).  Build the anchor and the winner and
    # print their exact-Fraction digest; the main run re-invokes this
    # file under three PYTHONHASHSEEDs and compares stdout.
    for kk in (('WB', 8, 14, 0), ('DR', 8, 10, 8)):
        _b, _pr, _dt = get(*kk)
        print(f"DIGEST {kk}: " + repr([( _pr[d]['h2'], _pr[d]['om'],
              _pr[d]['h4'], _pr[d]['max'], _pr[d]['n']) for d in (2, 3)]))
    sys.exit(0)

# ======================================================================
# W0 — THE ANCHOR: C = 0 reproduces D60's published row EXACTLY
# ======================================================================
print("\n[W0 THE ANCHOR — WIDE-BRICK(8, 14, C = 0) against D60's "
      "committed row]")
b_anchor, P_ANCHOR, dt_a = get('WB', 8, 14, 0)
b_d60 = brick(8, 14)
_same_record = (b_anchor.H == b_d60.H)
D60_ROW = {'homog': Fr(10, 13), 'omega': Fr(125, 192),
           'w4': Fr(0), 'max': 3}          # v10/data/d60_crystal_exact.out
_num_ok = (P_ANCHOR[2]['h2'] == D60_ROW['homog']
           and P_ANCHOR[2]['om'] == D60_ROW['omega']
           and P_ANCHOR[2]['h4'] == D60_ROW['w4']
           and P_ANCHOR[2]['max'] == D60_ROW['max'])
_dec_ok = (f"{float(P_ANCHOR[2]['h2']):.4f}" == "0.7692"
           and f"{float(P_ANCHOR[2]['om']):.4f}" == "0.6510"
           and f"{float(P_ANCHOR[2]['h4']):.4f}" == "0.0000"
           and P_ANCHOR[2]['max'] == 3)
_agree = d58_atlas(poset_of(b_anchor.H), 'anchor', quiet=True)
# round-1 NIT 1: h4 — the column this unit is about — is in the check
_atlas_ok = all(_agree[d]['h2'] == P_ANCHOR[d]['h2']
                and _agree[d]['om'] == P_ANCHOR[d]['om']
                and _agree[d]['h4'] == P_ANCHOR[d]['h4']
                and _agree[d]['max'] == P_ANCHOR[d]['max'] for d in (2, 3))
print("  " + line('WIDE-BRICK M=8 R=14 C=0', b_anchor, P_ANCHOR, dt_a))
check("W0 [ANCHOR, exit 1 on breakage] THE C = 0 WIDE-BRICK IS D60'S "
      "BRICK.  Three independent ways: (i) the event list is IDENTICAL "
      "to D60's own `brick(8, 14)` called in this process; (ii) the "
      "exact Fractions reproduce D60's published row "
      "(10/13 / 125/192 / 0 / 3); (iii) the four decimals of that row "
      "(0.7692 / 0.6510 / 0.0000 / 3) come out unchanged.  The "
      "population-restricted `profile` also still agrees with D58's own "
      "`atlas` on the full population, so every widened measurement "
      "below is a restriction of the committed instrument",
      _same_record and _num_ok and _dec_ok and _atlas_ok,
      f"identical event list = {_same_record} ({len(b_anchor.H)} events); "
      f"homog {P_ANCHOR[2]['h2']}, omega {P_ANCHOR[2]['om']}, |D|>=4 "
      f"{P_ANCHOR[2]['h4']}, max|D| {P_ANCHOR[2]['max']}; decimals "
      f"{_dec_ok}; atlas agreement {_atlas_ok}", anchor=True)

# ======================================================================
# W3 — the comparators, RE-RUN (never re-typed)
# ======================================================================
print("\n[W3 THE COMPARATORS — D58's atlas re-run IN THIS PROCESS on the "
      "same eleven genuine sprinkling configurations D60 used]")
t_cmp = time.time()
SPR = {}
for box in (30, 40, 60, 90):
    SPR[('M21', box)] = d58_atlas(mink4(latt(120, 2, box, 8)),
                                  f'M21 box={box}', quiet=True)
for box in (20, 24, 40, 48, 60, 90):
    SPR[('M31', box)] = d58_atlas(mink4(latt(120, 3, box, 8)),
                                  f'M31 box={box}', quiet=True)
SPR[('M21', 'd47a')] = d58_atlas(mink3(latt3(120, box=60)),
                                 'M21 d47a', quiet=True)
for k in sorted(SPR, key=repr):
    r = SPR[k][2]
    print(f"    {k[0]} box={k[1]:>5}: homog {float(r['h2']):.4f}, "
          f"|D|>=4 {float(r['h4']):.4f}, mean|D| {float(r['mean']):.2f}, "
          f"max|D| {r['max']:2d}, mean omega {float(r['om']):.4f}")
BAND = {d: (min(SPR[k][d]['h2'] for k in SPR),
            max(SPR[k][d]['h2'] for k in SPR)) for d in (2, 3)}
W4B = {d: (min(SPR[k][d]['h4'] for k in SPR),
           max(SPR[k][d]['h4'] for k in SPR)) for d in (2, 3)}
MXB = {d: (min(SPR[k][d]['max'] for k in SPR),
           max(SPR[k][d]['max'] for k in SPR)) for d in (2, 3)}
OMB = {d: (min(SPR[k][d]['om'] for k in SPR),
           max(SPR[k][d]['om'] for k in SPR)) for d in (2, 3)}
for d in (2, 3):
    print(f"    d = {d}:  BAND homogeneity [{BAND[d][0]}, {BAND[d][1]}] "
          f"(~[{float(BAND[d][0]):.4f}, {float(BAND[d][1]):.4f}]); "
          f"|D|>=4 [{W4B[d][0]}, {W4B[d][1]}] "
          f"(~[{float(W4B[d][0]):.4f}, {float(W4B[d][1]):.4f}]); max|D| "
          f"[{MXB[d][0]}, {MXB[d][1]}]; mean omega "
          f"[{float(OMB[d][0]):.4f}, {float(OMB[d][1]):.4f}]")
print(f"    [{time.time() - t_cmp:.1f}s]")
check("W3 THE COMPARATORS ARE RE-RUN, NOT RE-TYPED (the batch round's "
      "D60 MINOR 1 / D58 NIT 1-2), and they reproduce D60's committed "
      "band exactly: homogeneity [77/120, 4/5] and |D| >= 4 "
      "[17/40, 13/20] at d = 2.  Every threshold used anywhere below is "
      "one of these measured numbers — this unit invents none",
      BAND[2] == (Fr(77, 120), Fr(4, 5))
      and W4B[2] == (Fr(17, 40), Fr(13, 20)) and len(SPR) == 11,
      f"{len(SPR)} genuine configurations; d = 2 band {BAND[2]}, "
      f"|D|>=4 band {W4B[2]}, sprinkling max|D| {MXB[2]}", anchor=True)

# ======================================================================
# W4 — THE FRONTIER
# ======================================================================
FRONTIER = {}    # key -> profile, every swept point


def sweep(title, kind, M, R, params, cad=CADENCE):
    t = time.time()
    print(f"  === {title} ===")
    for P in params:
        b, pr, dt = get(kind, M, R, P, cad)
        tag = (f"{kind} M={M:2d} R={R:2d} "
               + (f"C={P}" if kind == 'WB' else f"cpl={P}")
               + (f" cad={cad}" if cad != CADENCE else ""))
        print("    " + line(tag, b, pr, dt))
        if pr is not None:
            FRONTIER[(kind, M, R, P, cad)] = pr
    print(f"    swept {kind} {'C' if kind == 'WB' else 'cpl'} in "
          f"{list(params)} at (M, R) = ({M}, {R})  "
          f"[{time.time() - t:.1f}s]")


print("\n[W4 THE FRONTIER — the courier sweep.  All figures at d = 2; "
      "'band' = W3's [%.4f, %.4f]; 'wide' = D58's |D| >= 4 column]"
      % (float(BAND[2][0]), float(BAND[2][1])))
sweep("WIDE-BRICK courier sweep at D60's committed (M, R) = (8, 14)",
      'WB', 8, 14, (0, 1, 2, 3, 4))
sweep("WIDE-BRICK courier sweep at (M, R) = (6, 10)",
      'WB', 6, 10, (0, 1, 2, 3))
sweep("WIDE-BRICK courier sweep at (M, R) = (10, 14)",
      'WB', 10, 14, (0, 1, 2, 3))
print("  === cadence probe: the same courier count at HALF cadence ===")
for cad in (2,):
    b, pr, dt = get('WB', 8, 14, 2, cad)
    print("    " + line(f"WB M= 8 R=14 C=2 cad={cad}", b, pr, dt))
    if pr is not None:
        FRONTIER[('WB', 8, 14, 2, cad)] = pr

print("\n[W4 THE FRONTIER — the double-ring coupling sweep]")
sweep("DOUBLE-RING coupling sweep at (M, R) = (8, 10)",
      'DR', 8, 10, tuple(range(0, 9)))
sweep("DOUBLE-RING coupling sweep at (M, R) = (6, 14)",
      'DR', 6, 14, tuple(range(0, 7)))
sweep("DOUBLE-RING coupling sweep at (M, R) = (4, 14)",
      'DR', 4, 14, tuple(range(0, 5)))
print("  === DOUBLE-RING at FULL coupling, rounds sweep (the D60 lesson: "
      "a headline is a parameter — so the trend is printed, not a point) "
      "===")
t = time.time()
for R in (10, 14, 20, 26):
    b, pr, dt = get('DR', 4, R, 4)
    print("    " + line(f"DR M= 4 R={R:2d} cpl=4", b, pr, dt))
    FRONTIER[('DR', 4, R, 4, CADENCE)] = pr
print(f"    swept R in [10, 14, 20, 26] at (M, cpl) = (4, 4)  "
      f"[{time.time() - t:.1f}s]")

# the height-layer census for the cpl = 1 dip (round-1 MAJOR 2(c): the
# mechanism was asserted in one place and disclaimed in another; the
# census decides it and is one loop)
print("\n  === the height-layer census at (M, R) = (8, 10): does partial "
      "coupling break the layer structure? ===")
_layers = {}
for cpl in (0, 1, 2, 8):
    bb = BUILT[('DR', 8, 10, cpl, CADENCE)][0]
    hs = heights(poset_of(bb.H))
    cnt = Counter(hs.values() if isinstance(hs, dict) else hs)
    prof = [cnt[i] for i in range(max(cnt) + 1)]
    _layers[cpl] = prof
    print(f"    cpl={cpl}: {len(prof)} layers, sizes {prof}, distinct "
          f"sizes = {len(set(prof))}")

# ------------------------------------------------- the decision
IN_BAND = {k: v for k, v in FRONTIER.items()
           if BAND[2][0] <= v[2]['h2'] <= BAND[2][1]}
WIDE = {k: v for k, v in FRONTIER.items() if v[2]['h4'] > 0}
BOTH = {k: v for k, v in FRONTIER.items() if k in IN_BAND and k in WIDE}
VERDICT = ('F3' if BOTH else ('F2' if WIDE else 'F1'))
WINNER = (max(BOTH, key=lambda k: (BOTH[k][2]['h4'], -BOTH[k][2]['n']))
          if BOTH else None)
# round-1 MINOR 8: the cadence probe is a VARIANT of an (M, R, C)
# setting, not a distinct one — both counts printed
_distinct = {k[:4] for k in FRONTIER}
print(f"\n  swept configurations = {len(FRONTIER)} "
      f"({len(_distinct)} distinct (kind, M, R, param) settings + "
      f"{len(FRONTIER) - len(_distinct)} cadence variant); refusals = "
      f"{sum(1 for v in BUILT.values() if v[1] is None)}; in the "
      f"homogeneity band = {len(IN_BAND)}; wide (|D| >= 4 present) = "
      f"{len(WIDE)}; BOTH = {len(BOTH)} "
      f"({len({k[:4] for k in BOTH})} distinct settings)")
if BOTH:
    print("  configurations that are IN BAND AND WIDE (the F3 set), by "
          "width:")
    for k in sorted(BOTH, key=lambda k: -BOTH[k][2]['h4']):
        x = BOTH[k][2]
        print(f"    {k[0]} M={k[1]} R={k[2]} "
              f"{'C' if k[0] == 'WB' else 'cpl'}={k[3]} cad={k[4]}: "
              f"n={x['n']}, homog {x['h2']} (~{float(x['h2']):.4f}), "
              f"|D|>=4 {x['h4']} (~{float(x['h4']):.4f}), max|D| "
              f"{x['max']}")
check("W4 [THE FRONTIER DECIDES] " + (
      "**F3 — THE WIDE CRYSTAL EXISTS, AT d = 2.**  Some swept "
      "configuration sits INSIDE the recomputed sprinkling homogeneity "
      "band AND carries 4-direction charts at d = 2, so the tiling "
      "mechanism and the width mechanism COMPOSE at grammar layer.  "
      "D60's residue 2 (the max |D| = 3 ceiling AT d = 2) was a "
      "property of the 1+1 brick's cone, not of tiling records as such "
      "(round-1 MAJOR 1: at d = 3 the F3 pattern is met by uncoupled "
      "records already — W2 prints the census — so the novelty is this "
      "d = 2 statement)" if VERDICT == 'F3' else
      ("**F2 — THE TRADE-OFF WALL.**  Width is reached only OUTSIDE "
       "the homogeneity band (round-1 MINOR 7: each wide "
       "configuration's side of the band is in the frontier print "
       "above; the pre-registered F2 is width-never-in-band, which is "
       "this predicate)" if VERDICT == 'F2' else
       "**F1 — THE GRAMMAR WALL.**  No swept configuration reaches "
       "|D| >= 4 at d = 2")) + ".  The predicate is the pre-registered "
      "disjunction itself, computed from the sweep",
      VERDICT == 'F3',
      f"verdict = {VERDICT}; in-band {len(IN_BAND)}, wide {len(WIDE)}, "
      f"both {len(BOTH)} of {len(FRONTIER)} swept; winner = {WINNER}")

if WINNER is None:
    print("\n[no F3 witness — the remaining gates run on the widest "
          "swept configuration instead]")
    WINNER = max(FRONTIER, key=lambda k: (FRONTIER[k][2]['h4'],
                                          FRONTIER[k][2]['h2']))
W_kind, W_M, W_R, W_P, W_cad = WINNER
b_win, P_WIN, dt_w = BUILT[WINNER]
print(f"\n  THE WINNING CONFIGURATION (rule: among the in-band-and-wide "
      f"set, the largest |D| >= 4 fraction; ties broken by fewest "
      f"events) = {W_kind} M={W_M} R={W_R} "
      f"{'C' if W_kind == 'WB' else 'cpl'}={W_P} cad={W_cad}, "
      f"{len(b_win.H)} events over {len(actors_of(W_kind, W_M, W_P))} "
      f"actors")

# ======================================================================
# W2 — the atlas census per record, at d = 2 AND d = 3, both orderings
# ======================================================================
print("\n[W2 THE ATLAS CENSUS — EVERY swept record, at d = 2 AND d = 3 "
      "(round-1 MINOR 1: the pin says per record and means it), "
      "orderings reported BOTH ways (D60's MINOR 4 lesson: the depths "
      "disagree)]")


def _inb(pr, d):
    return BAND[d][0] <= pr[d]['h2'] <= BAND[d][1]


for k in sorted(FRONTIER, key=repr):
    pr = FRONTIER[k]
    row = []
    for d in (2, 3):
        x = pr[d]
        pos = ('in' if _inb(pr, d) else
               ('ABOVE' if x['h2'] > BAND[d][1] else 'below'))
        row.append(f"d={d}: h {float(x['h2']):.4f}[{pos}] w "
                   f"{float(x['h4']):.4f} max {x['max']}")
    print(f"    {k[0]}({k[1]},{k[2]},{k[3]}"
          + (f",cad{k[4]}" if k[4] != CADENCE else "") + "): "
          + "  |  ".join(row))
_w2 = P_WIN
_flips = [k for k in FRONTIER if _inb(FRONTIER[k], 2) != _inb(FRONTIER[k], 3)]
_flip = _inb(_w2, 2) != _inb(_w2, 3)
# round-1 MINOR 1/2: the d = 3 max census — W4b's bound there is 8,
# and records DO move past 4
_mv5 = sorted(k for k in FRONTIER if FRONTIER[k][3]['max'] == 5)
_mv6 = sorted(k for k in FRONTIER if FRONTIER[k][3]['max'] >= 6)
print(f"    max|D| at d = 3 EXCEEDS 4 at {len(_mv5) + len(_mv6)} of "
      f"{len(FRONTIER)} records: {len(_mv5)} reach 5, {len(_mv6)} reach "
      f"6 (W4b's d = 3 bound is 2^3 = 8; none exceeds it)")
# round-1 MAJOR 1: the F3 PATTERN AT d = 3 — including who meets it
# with ZERO coupling.  The novelty of this unit is a d = 2 statement.
_f3d3 = sorted(k for k in FRONTIER
               if _inb(FRONTIER[k], 3) and FRONTIER[k][3]['h4'] > 0)
_f3d3_zero = [k for k in _f3d3 if k[3] == 0]
print(f"    the F3 pattern (in-band AND |D| >= 4 present) evaluated at "
      f"d = 3: holds at {len(_f3d3)} configurations, {len(_f3d3_zero)} "
      f"of them with ZERO coupling {_f3d3_zero} — D60's own brick among "
      f"them.  THE NOVELTY OF THIS UNIT IS A d = 2 STATEMENT: at d = 2 "
      f"no zero-coupling configuration is wide at all")
_f3d2_zero = [k for k in BOTH if k[3] == 0]
check("W2 THE CENSUS IS REPORTED AT BOTH DEPTHS FOR EVERY RECORD, AND "
      "THE DEPTHS DO NOT AGREE — the D60 MINOR-4 lesson holds for the "
      "wide records too, so every width and homogeneity statement in "
      "this unit is depth-labelled.  The winner is in the band at "
      "d = 2 and " + ("OUT of it at d = 3" if _flip
                      else "in it at d = 3 as well")
      + "; its |D| >= 4 fraction rises with depth (as the brick's did) "
      "and its max |D| happens to stay at 4 at d = 3 — a MEASUREMENT, "
      "not W4b (the theorem's d = 3 bound is 8, and other records do "
      "reach 5 and 6 there — round-1 MINOR 2).  And the d = 2 novelty "
      "is gated as a d = 2 statement: at d = 3 the F3 pattern is "
      "already met by zero-coupling configurations (round-1 MAJOR 1), "
      "at d = 2 by none",
      _w2[3]['h4'] > _w2[2]['h4'] and len(_f3d3_zero) > 0
      and len(_f3d2_zero) == 0
      and all(FRONTIER[k][3]['max'] <= 8 for k in FRONTIER),
      f"winner d=2: homog {float(_w2[2]['h2']):.4f}, |D|>=4 "
      f"{float(_w2[2]['h4']):.4f}, max {_w2[2]['max']}; d=3: homog "
      f"{float(_w2[3]['h2']):.4f}, |D|>=4 {float(_w2[3]['h4']):.4f}, max "
      f"{_w2[3]['max']}; band-membership flips across the sweep = "
      f"{len(_flips)}; d3 max>4 at {len(_mv5) + len(_mv6)}; F3-pattern-"
      f"at-d3 zero-coupling = {len(_f3d3_zero)}, at-d2 = {len(_f3d2_zero)}")

# ======================================================================
# W4b — THE STRUCTURAL WIDTH WALL (a theorem of the layer, verified)
# ======================================================================
print("\n[W4b WHY THE WIDTH STOPS WHERE IT DOES — a theorem of the "
      "committed layer, stated and then verified on every record built "
      "here]")
print("  THEOREM (the branching bound).  Let a record's events carry at")
print("  most B registers each (`regs_of`).  Then for every event e and")
print("  every depth d >= 1, the SKY-B chart satisfies |D_e(d)| <= B^d.")
print("  Proof.  Write R_e(k) = {f : e <= f, h[f] = h[e] + k} for the")
print("  REFLEXIVE k-layer (so R_e(0) = {e}, R_e(k) = D_e(k) for k >= 1,")
print("  and R_e(k) = {} for k < 0).  `event_poset` sets pred[j] =")
print("  U_{r in regs(j)} (pred[last[r]] u {last[r]}), so the order is")
print("  the transitive closure of the relation P: x P y iff x is the")
print("  immediately preceding event on some register of y.  Each P-step")
print("  raises height by at least 1, and each x has at most")
print("  |regs(x)| <= B P-successors (one per register, the next event")
print("  on that wire).  Hence for k >= 1, R_e(k) = U_{y : e P y}")
print("  R_y(k - (h[y] - h[e])): every f > e is reached from e by a")
print("  P-path, whose first step is some such y.  Induct on k: the")
print("  union has at most B terms, each of size at most B^{k-1}")
print("  because h[y] - h[e] >= 1.  So |R_e(k)| <= B^k, and D_e(d) =")
print("  R_e(d).  []")
print("  CONSEQUENCE, and it is the wall: a record made of DELIVERIES")
print("  has B = 2 (carriers {s, r}), so max |D| <= 4 at d = 2 and <= 8")
print("  at d = 3 — NO delivery circuit whatever can reach the")
print(f"  sprinklings' max |D| {MXB[2][0]}-{MXB[2][1]}.  Width beyond 4 at")
print("  d = 2 needs events with 3+ registers, and the layer has exactly")
print("  one such species: an ARBITRATION over a component with 2+")
print("  distinct proposers (regs = proposers u {new version}).  So at")
print("  grammar layer chart width past 4 is bought with CONFLICT, not")
print("  with transport.")
wall_ok = True
sat = []
_bvals = set()
for k, (b, pr, dt) in sorted(BUILT.items(), key=repr):
    if pr is None:
        continue
    Bmax = max(len(regs_of(e)) for e in b.H)
    _bvals.add(Bmax)
    for d in (2, 3):
        if pr[d]['max'] > Bmax ** d:
            wall_ok = False
    if pr[2]['max'] == Bmax ** 2:
        sat.append(k)
# the 3-register arbitration exhibit (the wall is about DELIVERY
# circuits, not about the grammar)
_h2p = [('p', 'A', V0, 0), ('p', 'C', V0, 1)]
_ck = frozenset({('A', V0, 0), ('C', V0, 1)})
_arb = ('r', 'A', _ck, frozenset({('A', V0, 0)}))
_arb_ok, _arb_q = admissible(_h2p, _arb, ('A', 'B', 'C'))
_arb_regs = len(regs_of(_arb))
print(f"  registers per event species (committed `regs_of`): proposal 1, "
      f"idle 1, delivery 2, merge 2, arbitration = #proposers + 1 — the "
      f"exhibited two-proposer arb is admissible (q = {_arb_q}) and "
      f"carries {_arb_regs} registers")
check("W4b THE WIDTH WALL IS STRUCTURAL AND THE DOUBLE RING SATURATES "
      "IT.  Every record built in this unit obeys |D| <= B^d with B the "
      "record's own maximum register count, and B = 2 IS NOW GATED, not "
      "asserted (round-1 MINOR 6: max |regs_of(e)| measured on every "
      "event of every record, mint prefix included) — and the bound is "
      "TIGHT: the coupled rings hit max |D| = 4 = 2^2 at d = 2 exactly, "
      "which is why D60's 3 was beatable and why nothing here reaches "
      "the sprinklings' 10-17 at d = 2.  What W4b licenses is a "
      "NECESSITY: |D| >= 5 at d = 2 REQUIRES a 3+-register event, i.e. "
      "an arbitration over 2+ distinct proposers (round-1 MINOR 3 — "
      "whether a record CARRYING such width exists is open, residue 1); "
      "the exhibited admissible 3-register arbitration shows only that "
      "the wall is a fact about DELIVERY CIRCUITS, not about the grammar",
      wall_ok and len(sat) > 0 and _arb_ok and _arb_regs == 3
      and _bvals == {2},
      f"records checked = {sum(1 for v in BUILT.values() if v[1])}, "
      f"bound violations = 0, B values measured = {sorted(_bvals)}, "
      f"saturating configurations = {len(sat)} "
      f"(e.g. {sorted(sat, key=repr)[0]}); brick max|D| = "
      f"{P_ANCHOR[2]['max']}, winner max|D| = {P_WIN[2]['max']}, bound "
      f"2^2 = 4, sprinklings {MXB[2][0]}-{MXB[2][1]}")

# ======================================================================
# W1 — FORCEDNESS at D60's C1 grade
# ======================================================================
print("\n[W1 FORCEDNESS at D60's C1 grade — every event offered by the "
      "layer's own menu, every specification matched by EXACTLY ONE "
      "candidate, no tie broken, no refusal]")
_refusals = [(k, v[0].refusal) for k, v in BUILT.items()
             if v[0].refusal is not None]
_hits = max(v[0].maxhits for v in BUILT.values())
print(f"    records built = {len(BUILT)}, events built = "
      f"{sum(len(v[0].H) for v in BUILT.values())}, refusals = "
      f"{len(_refusals)} {_refusals if _refusals else ''}, max menu hits "
      f"per specification over every step of every record = {_hits}")
check("W1 EVERY RECORD IN THE SWEEP IS ADMISSIBLE AT EVERY STEP "
      "(restricted-menu drive).  WHAT THIS GATE MEASURES (round-1 "
      "MINOR 4): a delivery specification is its full tuple and menu "
      "events are pairwise distinct, so 'matches exactly one candidate' "
      "cannot exceed one — the gated quantity is that the specified "
      "event IS OFFERED (hits = 1, never 0) and no step was refused.  "
      "Tie-freedom is structural, not discovered",
      _hits == 1 and not _refusals,
      f"max hits = {_hits} (1 => offered and unique), refusals = "
      f"{len(_refusals)}")

print("\n[W1b THE FULL-MENU REPLAY — the strong form: ALL actors offered "
      "at EVERY step (the batch round's own test on D60's brick)]")


def full_menu_replay(H, actors, budget=FULLMENU_BUDGET):
    t = time.time()
    worst = 0
    widest = 0
    for j, e in enumerate(H):
        menu = candidates_for(H[:j], tuple(actors))
        n_hit = sum(1 for x, q in menu if x == e)
        widest = max(widest, len(menu))
        worst = max(worst, n_hit)
        if n_hit != 1:
            return {'status': 'BROKEN', 'step': j, 'hits': n_hit,
                    'menu': len(menu), 't': time.time() - t}
        if time.time() - t > budget:
            return {'status': 'BUDGET-CUT', 'step': j + 1, 'hits': worst,
                    'menu': widest, 't': time.time() - t}
    return {'status': 'OK', 'step': len(H), 'hits': worst,
            'menu': widest, 't': time.time() - t}


REPLAY = {}
for nm, k in (('C=0 anchor', ('WB', 8, 14, 0, CADENCE)),
              ('WIDE-BRICK C=2', ('WB', 8, 14, 2, CADENCE)),
              ('THE WINNER', WINNER)):
    if k not in BUILT:
        continue
    bb = BUILT[k][0]
    ac = actors_of(k[0], k[1], k[3])
    REPLAY[nm] = full_menu_replay(bb.H, ac)
    r = REPLAY[nm]
    print(f"    {nm:16s} ({len(bb.H):3d} events, {len(ac):2d} actors): "
          f"{r['status']} at step {r['step']}/{len(bb.H)}, max hits per "
          f"specification = {r['hits']}, widest full menu = {r['menu']} "
          f"candidates  [{r['t']:.1f}s]")
check("W1b ADMISSIBLE AGAINST THE UNRESTRICTED LAYER: replayed with "
      "all actors offered at every step, each record's every "
      "specification is OFFERED among the (up to several hundred) "
      "candidates the layer enumerates — uniqueness being structural "
      "(round-1 MINOR 4), the content is presence at every one of the "
      "hundreds of steps.  This is the grade D60's C1 was verified at "
      "in the batch round, and the wide records hold it",
      all(r['status'] == 'OK' and r['hits'] == 1
          for r in REPLAY.values()) and len(REPLAY) >= 3,
      "; ".join(f"{n}: {r['status']} hits {r['hits']} menu {r['menu']}"
                for n, r in REPLAY.items()))

# ======================================================================
# W5 — the interior control (D60's C7) on the frontier's key points
# ======================================================================
print("\n[W5 THE INTERIOR CONTROL (D60's C7) — boundary excision, so the "
      "frontier is read on the MECHANISM and not on the prefix]")


def interior_of(H):
    C = poset_of(H)
    hs = heights(C)
    lo, hi = min(hs), max(hs)
    return C, {e for e in range(len(C)) if lo + 2 <= hs[e] <= hi - 3}


# round-1 MAJOR 3: band membership is the F3 criterion, so the control
# runs on the WHOLE F3 set, not on hand-named key points
INT = {}
_stay = []
_leave_top = []
for k in sorted(BOTH, key=repr):
    C, pop = interior_of(BUILT[k][0].H)
    pi = profile(C, pop)
    INT[k] = pi
    pf = FRONTIER[k]
    ih = pi[2]['h2']
    tag = ('in band' if BAND[2][0] <= ih <= BAND[2][1]
           else ('ABOVE band' if ih > BAND[2][1] else 'BELOW band'))
    (_leave_top if ih > BAND[2][1] else _stay).append(k)
    print(f"    {k[0]}({k[1]},{k[2]},{k[3]}"
          + (f",cad{k[4]}" if k[4] != CADENCE else "") + "): "
          f"FULL n={pf[2]['n']:4d} homog {float(pf[2]['h2']):.4f} "
          f"|D|>=4 {float(pf[2]['h4']):.4f}  ->  INTERIOR "
          f"n={pi[2]['n']:4d} homog {float(ih):.4f} [{tag}] |D|>=4 "
          f"{float(pi[2]['h4']):.4f}")
_int_wide = all(INT[k][2]['h4'] >= FRONTIER[k][2]['h4'] for k in INT)
_int_homog = all(INT[k][2]['h2'] > FRONTIER[k][2]['h2'] for k in INT)
_win_int = INT.get(WINNER)
check("W5 THE WIDTH IS NOT A BOUNDARY ARTEFACT — AND 'IN THE BAND' "
      "LARGELY IS.  The interior control (D60's C7 excision) runs on "
      "EVERY F3 member (round-1 MAJOR 3, not on hand-named points): "
      "excision RAISES the |D| >= 4 fraction at every one — the wide "
      "charts are the circuit's, not the prefix's, and that is the "
      "durable half of F3.  Reported against the unit's own interest: "
      f"{len(_leave_top)} of {len(INT)} F3 members' INTERIORS leave "
      "the homogeneity band THROUGH THE TOP (the mechanism reading is "
      "D60's: homogeneity tends to 1, i.e. ABOVE the band, so band "
      "membership is partly an ENDS property of finite records; "
      f"{len(_stay)} stay in-band).  The composition claim survives as: "
      "the width mechanism does not destroy the tiling mechanism — "
      "both halves of F3 are carried, the width half unconditionally, "
      "the band half as a finite-record statement",
      _int_wide and _int_homog and len(INT) == len(BOTH),
      f"F3 members controlled = {len(INT)}/{len(BOTH)}; interior "
      f"|D|>=4 >= full at all = {_int_wide}; interior homogeneity > "
      f"full at all = {_int_homog}; interiors leaving the band through "
      f"the top = {len(_leave_top)}, staying in = {len(_stay)}; winner "
      f"{float(FRONTIER[WINNER][2]['h2']):.4f} -> "
      f"{float(_win_int[2]['h2']):.4f}")

# ======================================================================
# the licensed comparison, stated no wider than the sweep
# ======================================================================
print("\n[the licensed reading — stated no wider than the swept family]")
_beats_brick = P_WIN[2]['h4'] > P_ANCHOR[2]['h4']
_w4_reach = [k for k in FRONTIER if FRONTIER[k][2]['h4'] >= W4B[2][0]]
print(f"    configurations whose d = 2 |D| >= 4 fraction reaches the "
      f"SPRINKLING |D| >= 4 band [{float(W4B[2][0]):.4f}, "
      f"{float(W4B[2][1]):.4f}]: {len(_w4_reach)} "
      + ", ".join(f"{k[0]}({k[1]},{k[2]},{k[3]})="
                  f"{float(FRONTIER[k][2]['h4']):.4f} at homogeneity "
                  f"{float(FRONTIER[k][2]['h2']):.4f}"
                  for k in sorted(_w4_reach, key=repr)))
_both_bands = [k for k in _w4_reach
               if BAND[2][0] <= FRONTIER[k][2]['h2'] <= BAND[2][1]]
print(f"    configurations INSIDE BOTH bands at once at d = 2: "
      f"{len(_both_bands)} {sorted(_both_bands, key=repr)}")
_both3 = [k for k in FRONTIER
          if BAND[3][0] <= FRONTIER[k][3]['h2'] <= BAND[3][1]
          and W4B[3][0] <= FRONTIER[k][3]['h4'] <= W4B[3][1]]
print(f"    configurations INSIDE BOTH bands at once at d = 3: "
      f"{len(_both3)} "
      + ", ".join(f"{k[0]}({k[1]},{k[2]},{k[3]}) homog "
                  f"{float(FRONTIER[k][3]['h2']):.4f} / |D|>=4 "
                  f"{float(FRONTIER[k][3]['h4']):.4f}"
                  for k in sorted(_both3, key=repr)))
check("THE LICENSED CLAIM — A d = 2 STATEMENT (round-1 MAJOR 1), and "
      "its limit, REPORTED AT BOTH DEPTHS BECAUSE THEY DISAGREE.  "
      "Inside the swept (M, R, C, cpl) family the two mechanisms "
      "COMPOSE AT d = 2: coupled delivery circuits tile at in-band "
      "homogeneity while carrying 4-direction charts at a third of "
      "their events — which the brick never did AT d = 2, at any "
      "parameter (at d = 3 the uncoupled brick already meets the F3 "
      "pattern; W2's census).  At d = 2 the sweep does NOT deliver a "
      "configuration inside BOTH sprinkling bands at once — the "
      "|D| >= 4 fraction reaches the sprinkling band only where "
      "homogeneity has climbed ABOVE the band's top (the rounds "
      "sweep).  At d = 3 it DOES: configurations sit inside the d = 3 "
      "homogeneity band and the d = 3 |D| >= 4 band simultaneously.  "
      "And on the max |D| column no configuration reaches sprinkling "
      "values at d = 2, because none can (W4b; at d = 3 the bound is "
      "8 and the measured max is 6).  All three halves are reported",
      _beats_brick and len(_w4_reach) > 0 and len(_both_bands) == 0
      and len(_both3) > 0,
      f"winner |D|>=4 {P_WIN[2]['h4']} (~{float(P_WIN[2]['h4']):.4f}) vs "
      f"brick {P_ANCHOR[2]['h4']}; reaching the sprinkling |D|>=4 band "
      f"at d = 2 = {len(_w4_reach)}; inside both bands at d = 2 = "
      f"{len(_both_bands)}, at d = 3 = {len(_both3)}")

# ======================================================================
# W6 — anti-vacuity, caps, determinism, exits
# ======================================================================
_src = open('v10/code/d63_wide_crystal_exact.py').read()
_ch = [c for c in ast.walk(ast.parse(_src))
       if isinstance(c, ast.Call) and isinstance(c.func, ast.Name)
       and c.func.id == 'check']
_vac = [c for c in _ch if isinstance(c.args[1], ast.Constant)]
check("W6 AST anti-vacuity (no bare-constant predicates; #403 MA-2 "
      "scope): every gate above reads a measured quantity, and the two "
      "reporting-only lines are the printed tables, which carry no "
      "check().  The frontier gate reads the pre-registered disjunction "
      "itself, so F1 and F2 would each have been reported by the same "
      "line that reported F3",
      len(_ch) >= 8 and not _vac,
      f"check() calls = {len(_ch)}, bare-constant predicates = "
      f"{len(_vac)}")

print(f"\n[W6 DEPTHS, CAPS AND RANGES — all printed, none silent]")
print(f"    SKY-B depths measured: 2 and 3 (committed SKYB_DEPTH = "
      f"{SKYB_DEPTH}); atlas = D58's, unmodified.")
print(f"    WIDE-BRICK courier counts swept: C = 0..4 at (M, R) = "
      f"(8, 14); C = 0..3 at (6, 10); C = 0..3 at (10, 14); cadence 1 "
      f"throughout plus one cadence-2 probe at (8, 14, C = 2).")
print(f"    DOUBLE-RING couplings swept: cpl = 0..8 at (M, R) = (8, 10); "
      f"cpl = 0..6 at (6, 14); cpl = 0..4 at (4, 14); rounds R = "
      f"10, 14, 20, 26 at (M, cpl) = (4, 4).")
print(f"    configurations built = {len(BUILT)}; events built = "
      f"{sum(len(v[0].H) for v in BUILT.values())}; largest record = "
      f"{max(len(v[0].H) for v in BUILT.values())} events.")
_rep_times = ", ".join("%s %.1fs" % (n, r['t'])
                       for n, r in REPLAY.items())
print(f"    full-menu replays: {len(REPLAY)}, budget "
      f"{FULLMENU_BUDGET:.0f}s each, statuses "
      f"{ {n: r['status'] for n, r in REPLAY.items()} } ({_rep_times}).")
print(f"    NOTHING WAS CUT: no sweep was truncated for runtime, so no "
      f"trend-based cut has to be defended (the D50 lesson).  Total wall "
      f"clock at this line: {time.time() - T0:.1f}s.")

# W6b — determinism, GATED (round-1 MINOR 5): the probe re-run under
# three hash seeds must produce byte-identical stdout
t_det = time.time()
_digs = []
for _seed in ('0', '7', '999'):
    _env = dict(os.environ, PYTHONHASHSEED=_seed)
    _digs.append(subprocess.run(
        [sys.executable, 'v10/code/d63_wide_crystal_exact.py', '--probe'],
        capture_output=True, text=True, env=_env).stdout)
check("W6b DETERMINISM IS GATED, NOT ASSERTED (round-1 MINOR 5; the "
      "layer reads next(iter(frozenset)) in load-bearing places): the "
      "anchor and the winner rebuilt in probe mode under "
      "PYTHONHASHSEED 0 / 7 / 999 — byte-identical stdout, exact "
      "Fractions included",
      len(set(_digs)) == 1 and 'DIGEST' in _digs[0]
      and "('DR', 8, 10, 8)" in _digs[0],
      f"probe runs = 3, distinct outputs = {len(set(_digs))}  "
      f"[{time.time() - t_det:.1f}s]")

print("\n[VERDICT — D63]")
print(f"  {VERDICT} FIRED.  " + (
    "THE WIDE CRYSTAL EXISTS: the tiling mechanism and the width"
    if VERDICT == 'F3' else "the pre-registered wall"))
if VERDICT == 'F3':
    print("  mechanism COMPOSE inside the swept family.  The witness:")
    print(f"    {W_kind} M={W_M} R={W_R} "
          f"{'C' if W_kind == 'WB' else 'cpl'}={W_P} — "
          f"{len(b_win.H)} events, {len(actors_of(W_kind, W_M, W_P))} "
          f"actors, FORCED against the unrestricted menu, d = 2 "
          f"homogeneity {P_WIN[2]['h2']} (~{float(P_WIN[2]['h2']):.4f}, "
          f"inside the band [{float(BAND[2][0]):.4f}, "
          f"{float(BAND[2][1]):.4f}]), |D| >= 4 at {P_WIN[2]['h4']} "
          f"(~{float(P_WIN[2]['h4']):.4f}) of its events, max |D| "
          f"{P_WIN[2]['max']}.")
    print("  D60's residue 2 is CLOSED IN THE SWEPT FAMILY, AT d = 2: "
          "max |D| = 3")
    print("  was the 1+1 brick's light cone, not a property of tiling "
          "records; a")
    print("  second spatial direction (couriers or a coupled ring) takes "
          "it to 4.")
    print("  (At d = 3 uncoupled records meet the F3 pattern already — "
          "W2's census —")
    print("  so the composition novelty is a d = 2 statement throughout.)")
print("  AND THE NEW CEILING IS A THEOREM, NOT A PARAMETER (W4b): a "
      "record")
print("  of deliveries has 2 registers per event, so |D| <= 2^d — no "
      "delivery")
print(f"  circuit can approach the sprinklings' max |D| "
      f"{MXB[2][0]}-{MXB[2][1]} at d = 2.  Width")
print("  past 4 must be bought with ARBITRATION over conflicts.")
print("  SCOPE (pin §5): grammar layer; the claim is about the swept")
print("  (M, R, C, cpl) family and no wider.  No measure claim (transport")
print("  scope has none — B1); no typicality; no physical-object claim —")
print("  a crystal is a MECHANISM certificate (#440).  Transfer to the")
print("  identified interactive click law runs through paper 29's missing")
print("  map (D59) and is not claimed.  omega is a chart-size ratio along")
print("  covers (D58 round-1 MAJOR 2), never a symmetric overlap.")
print(f"\n[d63] {PASS} PASS / {FAIL} FAIL   "
      f"[total wall clock {time.time() - T0:.1f}s]")
print("[exit protocol, pin W6] exit 1 ONLY on W0/W3 anchor breakage; "
      "substantive negatives exit 0.  anchor broken = " + str(ANCHOR_FAIL))
sys.exit(1 if ANCHOR_FAIL else 0)
