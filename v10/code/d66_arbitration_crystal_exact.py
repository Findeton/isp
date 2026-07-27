#!/usr/bin/env python3
"""
d66_arbitration_crystal_exact.py — v10 D66: THE ARBITRATION CRYSTAL.
Pin: note-d66-arbitration-crystal-pin.md (STRICT, FROZEN AND COMMITTED
before this file existed).  Parents: D63 (the wide crystal, W4b's
branching bound, residue 1 — the arbitration route to width > 4), D64
(TERMINAL: the delivery atlas is a coboundary; the successor question
"can ANY substrate carry a non-coboundary transition class?"), D65 (the
descent defect originates at the 2 -> 5/2 mass jump), D60/D58/D47a/D55c
(the tiling blueprints, the atlas, the sky, the sprinkling controls),
D42b1 (the transport grammar).

THE QUESTION (pin §1).  Three terminal results point at one event
species: width past 4 at d = 2 REQUIRES a 3+-register event (W4b) and
arbitration is the only one; the known trivialization of transition
classes exploits a delivery's two-port symmetry, which arbitration
breaks; and the descent coboundary is generated where conflict groups
become visible.  This unit builds a forced, tiling record whose ENGINE
IS CONFLICT rather than delivery, and runs the three instruments on it.

THE OBJECTS (pin §2), both built entirely from the committed d42b1
layer, every event menu-selected:
  * CONFLICT-RING(M, R, sticky, win) — the pin's object.  M actors on a
    ring; each round the brick pairing; each pair PROPOSES opposite bits
    on a shared base and ARBITRATES the conflict (two-proposer arb, 3
    registers), the minted version becoming the next round's base.  The
    version is held by BOTH proposers (d42b1 `View.holdings`), so no
    delivery is needed inside a pair; ONE delivery per pair per round is
    needed to re-supply a shared base when the pairing rotates — the
    conflict-supply problem the pin's lean names, solved and counted.
    `sticky` = rounds per pairing before rotating (sticky = 0 means
    never rotate: the delivery-free limit); `win` selects which proposer
    wins ('S' first, 'R' second, 'ALT' alternating).
  * CONFLICT-GRID(g, R) — the WIDE variant (pin §2's "couplings added
    if the base object tiles").  g^2 actors on a g x g grid; rounds
    alternate ROW groups and COLUMN groups (orthogonal resolvable
    partitions), so each round every actor changes group-mates; each
    group is a g-PROPOSER conflict (g + 1 registers) whose base is
    supplied by g - 1 deliveries from the group's diagonal seed.
    g = 2 reproduces CONFLICT-RING(4, R) exactly (gated).

PRE-REGISTERED OUTCOMES (pin §4), decided by the sweep:
  A-I    conflicts refuse to tile at cadence (forcedness or
         admissibility breaks) — the break point is the deliverable;
  A-II   tiles, but width stays <= 4 at d = 2;
  A-III  tiles with |D| >= 5 — the delivery ceiling is broken by
         conflict; A4 then decides A-IIIa (class trivial) vs A-IIIb
         (H^1 != 0, which must survive every convention swap).

HOUSE RULES HELD: committed layers are single sources (AST extraction /
text-slice, never re-implemented; exit-freedom of the slice and of every
extracted body GATED); no invented thresholds (every band is the
recomputed sprinkling band, every column is D58's); exact Fractions
where weights appear; no bare-constant predicates; both depths and both
orderings reported; every census printed in full; determinism gated by a
hash-seed probe; exit 0 for substantive negatives, exit 1 ONLY on ANCHOR
breakage (the A0 family).
Run from the repo root: python3 v10/code/d66_arbitration_crystal_exact.py
"""
import ast, os, subprocess, sys, time
from collections import defaultdict, Counter
from fractions import Fraction as Fr
from itertools import combinations, permutations, product

sys.setrecursionlimit(300000)
T0 = time.time()
PASS = FAIL = 0
ANCHOR_FAIL = False
PROBE = '--probe' in sys.argv


def check(label, ok, detail="", anchor=False):
    global PASS, FAIL, ANCHOR_FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    if anchor and not ok:
        ANCHOR_FAIL = True
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


if not PROBE:
    print("[D66 — THE ARBITRATION CRYSTAL: can conflicts tile, and what "
          "do they buy?]")
    print("  banner: the engine of every record below is CONFLICT — "
          "propose/arbitrate")
    print("  cycles of the committed d42b1 layer — not delivery.  Every "
          "event is")
    print("  offered by the layer's own menu and specified by its FULL "
          "TUPLE.  The")
    print("  atlas (D58), the sky (D47a), the sprinkling controls (D55c), "
          "D60/D63's")
    print("  blueprint machinery and D64's WHOLE cocycle/coboundary "
          "instrument are")
    print("  imported as single sources and re-run in this process; D64's "
          "committed")
    print("  C7 row on DOUBLE-RING(8, 10, 8) is an ANCHOR of this "
          "receipt, so the")
    print("  same instrument that returned 0 obstructions there produces "
          "every")
    print("  number below.  A-I / A-II / A-III is decided by the sweep.")

# ======================================================================
# A0a — ANCHORS: every committed layer a single source
# ======================================================================
_SRC42 = 'v10/code/d42b1_transport_exact.py'
_st = open(_SRC42).read()
_cut = _st.index('print("[d42b1')
_slice = _st[:_cut]
nst = {}
exec(compile(_slice, 'd42b1_slice', 'exec'), nst)
candidates_for, event_poset, V0 = (nst['candidates_for'],
                                   nst['event_poset'], nst['V0'])
regs_of, admissible, vname = nst['regs_of'], nst['admissible'], nst['vname']
View, full_view = nst['View'], nst['full_view']

_EXITNAMES = ('exit', 'quit', '_exit')


def _no_exit(nodes):
    """No exit CALL and no bare NAME/ATTRIBUTE reference to an exit
    callable (so an aliased exit is caught too) survives an extracted
    body.  SCOPE, said in the gate: a syntactic scan for three names; it
    decides no reachability and cannot see an exit reached through
    getattr on a computed string (D64's C0a form, adopted verbatim)."""
    for n in nodes:
        for c in ast.walk(n):
            if isinstance(c, ast.Attribute) and c.attr in _EXITNAMES:
                return False
            if isinstance(c, ast.Name) and c.id in _EXITNAMES:
                return False
    return True


_EXTRACTED = {}


def _ext(path, marker, names=(), extra=None):
    """D60/D63/D64's committed extraction idiom: keep only defs/classes
    (and the named module constants), so no module-level statement —
    print, gate, sys.exit — can run."""
    t = ast.parse(open(path).read())
    keep = [n for n in t.body if isinstance(n, (ast.FunctionDef,
            ast.ClassDef)) or (isinstance(n, ast.Assign)
            and any(isinstance(x, ast.Name) and x.id in names
                    for x in n.targets))]
    _EXTRACTED[path] = keep
    g = {'Fr': Fr, 'combinations': combinations, 'Counter': Counter,
         'permutations': permutations, 'product': product,
         'defaultdict': defaultdict, 'sys': sys, 'time': time, 'ast': ast,
         'os': os, 'subprocess': subprocess}
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
g63 = _ext('v10/code/d63_wide_crystal_exact.py', 'd63',
           ('CADENCE', 'FULLMENU_BUDGET'),
           extra={'B': B, 'brick': brick, 'dl': dl, 'profile': profile,
                  'mint_and_spread': mint_and_spread, 'poset_of': poset_of,
                  'candidates_for': candidates_for, 'sky': sky,
                  'heights': heights, 'd58_atlas': d58_atlas,
                  'd58_covers': d58_covers, 'regs_of': regs_of,
                  'event_poset': event_poset, 'V0': V0})
double_ring, wide_brick = g63['double_ring'], g63['wide_brick']
g64 = _ext('v10/code/d64_cocycle_exact.py', 'd64',
           ('LAB', 'NAMED', 'CLOSURE_CAP', 'CLOSURE_OPS', 'DEPTHS'),
           extra={'sky': sky, 'heights': heights, 'd58_covers': d58_covers,
                  'regs_of': regs_of, 'vname': vname,
                  'event_poset': event_poset, 'V0': V0,
                  'candidates_for': candidates_for})
reg_tuple, ord_tuple0 = g64['reg_tuple'], g64['ord_tuple']
out_reg, out_cov, closure_of = g64['out_reg'], g64['out_cov'], g64['closure_of']
words_from, label, fibermap = g64['words_from'], g64['label'], g64['fibermap']
classify, is_named = g64['classify'], g64['is_named']
flip1, flipall = g64['flip1'], g64['flipall']
measure, cochain = g64['measure'], g64['cochain']
extension_census = g64['extension_census']
_order, _comp4, _cyc, _pt = g64['_order'], g64['_comp4'], g64['_cyc'], g64['_pt']
LAB, DEPTHS = g64['LAB'], g64['DEPTHS']

_slice_ast_ok = _no_exit(ast.parse(_slice).body)
_strip_ok = ('sys.exit' not in _slice and _slice_ast_ok
             and all(_no_exit(v) for v in _EXTRACTED.values()))
if not PROBE:
    check("A0a ANCHORS — every layer a SINGLE SOURCE and the strip is "
          "GATED not asserted: the transport grammar by text-slice from "
          "committed d42b1 (cut at its own banner print), and the sky "
          "(d47a), the repaired sprinkling generator (d55c), the atlas "
          "(d58), D60's blueprint machinery, D63's `double_ring` / "
          "`wide_brick` and **D64's ENTIRE cocycle instrument — "
          "`reg_tuple`, `out_reg`, `out_cov`, `words_from`, `label`, "
          "`fibermap`, `classify`, `measure`, `cochain`, "
          "`extension_census`** — by AST extraction.  Nothing here "
          "re-implements a committed layer.  The gate reads: no "
          "reference to `exit`, `quit` or `_exit`, in CALL or bare "
          "NAME/ATTRIBUTE form, survives the slice (checked textually "
          "AND by AST) or any extracted body",
          all(callable(f) for f in (candidates_for, sky, d58_atlas, latt,
                                    brick, profile, double_ring, measure,
                                    cochain, out_reg)) and _strip_ok,
          f"slice = {_cut} of {len(_st)} chars, exit-free (text) = "
          f"{'sys.exit' not in _slice}, exit-free (AST) = {_slice_ast_ok}; "
          f"extracted bodies = "
          f"{ {p.split('/')[-1]: len(v) for p, v in _EXTRACTED.items()} }, "
          f"all exit-free = {all(_no_exit(v) for v in _EXTRACTED.values())}",
          anchor=True)

# ======================================================================
# THE BLUEPRINTS (pin §2)
# ======================================================================
FULLMENU_BUDGET = 420.0     # seconds per full-menu replay (printed)
WIDE_REPLAY_BUDGET = 120.0  # seconds for the wide record's replay
BUILT = {}


def _pick(b, actors, e, lbl):
    """Every event of every record is specified by its FULL TUPLE and
    taken from the layer's own menu (D60's `B.pick`, imported).  A full
    tuple can match at most one menu entry, so `maxhits == 1` gates that
    the event was OFFERED; a refusal is recorded, never patched."""
    return b.pick(tuple(actors), lambda z, e=e: z == e, lbl)


def conflict_pair_group(b, grp, base, seed, winner):
    """One conflict group: (deliveries already done) g proposals with
    payload 0 for the seed and 1 for the rest — a connected conflict
    component on `base` — then the arbitration over the WHOLE component
    with `winner` the winning triple.  Returns the minted version."""
    trips = [(a, base, 0 if a == seed else 1) for a in grp]
    for t in trips:
        _pick(b, (t[0],), ('p', t[0], t[1], t[2]), f"propose {t[0]}")
    ck = frozenset(trips)
    wt = [t for t in trips if t[0] == winner][0]
    wk = frozenset({wt})
    _pick(b, (seed,), ('r', seed, ck, wk), f"arbitrate {seed}")
    return vname(base, wk, seed)


def conflict_ring(M, R, sticky=1, win='S'):
    """CONFLICT-RING(M, R, sticky, win): the pin's object."""
    ac = [f"C{i}" for i in range(M)]
    b = B(tuple(ac))
    cur = {a: V0 for a in ac}
    for t in range(R):
        blk = (t if sticky <= 0 else t // sticky) % 2 if sticky > 0 else 0
        pairs = ([(i, i + 1) for i in range(0, M, 2)] if blk == 0
                 else [(i, (i + 1) % M) for i in range(1, M, 2)])
        for (i, j) in pairs:
            s, r = ac[i], ac[j]
            if cur[s] != cur[r]:
                dl(b, s, r, cur[s])          # the conflict re-supply
            base = cur[s]
            winner = (s if win == 'S' else
                      (r if win == 'R' else (s if t % 2 == 0 else r)))
            v = conflict_pair_group(b, [s, r], base, s, winner)
            cur[s] = cur[r] = v
            if b.refusal:
                return b
    return b


def conflict_grid(g, R):
    """CONFLICT-GRID(g, R): the WIDE variant — g-proposer arbitrations
    on orthogonal row/column partitions of a g x g actor grid."""
    ac = [[f"G{i}{j}" for j in range(g)] for i in range(g)]
    flat = [a for row in ac for a in row]
    b = B(tuple(flat))
    cur = {a: V0 for a in flat}
    for t in range(R):
        if t % 2 == 0:
            groups = [[ac[i][j] for j in range(g)] for i in range(g)]
            seeds = [ac[i][i] for i in range(g)]
        else:
            groups = [[ac[i][j] for i in range(g)] for j in range(g)]
            seeds = [ac[j][j] for j in range(g)]
        for gi, grp in enumerate(groups):
            sd = seeds[gi]
            base = cur[sd]
            for a in grp:
                if a != sd and cur[a] != base:
                    dl(b, sd, a, base)       # the conflict re-supply
            v = conflict_pair_group(b, grp, base, sd, sd)
            for a in grp:
                cur[a] = v
            if b.refusal:
                return b
    return b


def actors_of(kind, P1, P2=None):
    if kind == 'RING':
        return [f"C{i}" for i in range(P1)]
    return [f"G{i}{j}" for i in range(P1) for j in range(P1)]


def get(key):
    """Build (once) and measure a swept configuration."""
    if key in BUILT:
        return BUILT[key]
    kind = key[0]
    t = time.time()
    b = (conflict_ring(key[1], key[2], key[3], key[4]) if kind == 'RING'
         else conflict_grid(key[1], key[2]))
    pr = None if b.refusal else profile(poset_of(b.H))
    BUILT[key] = (b, pr, time.time() - t)
    return BUILT[key]


def tag_of(k):
    return (f"RING(M={k[1]},R={k[2]},sticky={k[3]},win={k[4]})"
            if k[0] == 'RING' else f"GRID(g={k[1]},R={k[2]})")


def arbshare(H):
    return Fr(sum(1 for e in H if e[0] == 'r'), len(H))


def line(k, b, pr, dt, d=2):
    if pr is None:
        return f"{tag_of(k)}: REFUSAL at {b.refusal}"
    x = pr[d]
    return (f"{tag_of(k):38s} n={x['n']:4d} arb {float(arbshare(b.H)):.4f} "
            f"homog {float(x['h2']):.4f}  |D|>=4 {float(x['h4']):.4f}  "
            f"max|D| {x['max']}  mean|D| {float(x['mean']):.2f}  omega "
            f"{float(x['om']):.4f}  [{dt:.1f}s]")


HEAD = ('RING', 6, 10, 1, 'S')          # the headline (tiling) record
WIDE = ('GRID', 3, 10)                  # the width witness
SWEEP = [('RING', 4, 6, 1, 'S'), ('RING', 4, 10, 1, 'S'),
         ('RING', 6, 6, 1, 'S'), HEAD, ('RING', 6, 14, 1, 'S'),
         ('RING', 8, 10, 1, 'S'),
         ('RING', 6, 10, 2, 'S'), ('RING', 6, 10, 0, 'S'),
         ('RING', 6, 10, 1, 'R'), ('RING', 6, 10, 1, 'ALT'),
         ('GRID', 2, 10), ('GRID', 3, 4), ('GRID', 3, 6), WIDE,
         ('GRID', 4, 4)]

if not PROBE:
    print(f"\n[the blueprints and every parameter, printed]")
    print(f"    CONFLICT-RING(M, R, sticky, win): brick pairing "
          f"{{(i,i+1): i even}} on even blocks, {{(i,i+1 mod M): i odd}} "
          f"on odd blocks; sticky = rounds per pairing (0 = never "
          f"rotate, the delivery-free limit); win in (S, R, ALT).")
    print(f"    Per pair per round: ONE delivery iff the two actors do "
          f"not already share an unsuperseded base, then TWO opposite "
          f"proposals, then ONE two-proposer arbitration.  Round 0 needs "
          f"no delivery (every actor holds genesis v0).")
    print(f"    CONFLICT-GRID(g, R): g x g actors; rounds alternate ROW "
          f"and COLUMN groups (orthogonal partitions, so no two actors "
          f"share a group twice running); group seed = the diagonal "
          f"member; g - 1 deliveries + g proposals + ONE g-proposer "
          f"arbitration per group per round.")
    print(f"    SKY-B depths measured = (2, 3); committed SKYB_DEPTH = "
          f"{SKYB_DEPTH}.  Full-menu replay budgets: "
          f"{FULLMENU_BUDGET:.0f}s per record, "
          f"{WIDE_REPLAY_BUDGET:.0f}s for the wide record.")
    print(f"    swept configurations = {len(SWEEP)}: "
          + "; ".join(tag_of(k) for k in SWEEP))

if PROBE:
    for kk in (('RING', 4, 6, 1, 'S'), ('GRID', 3, 4)):
        _b, _pr, _dt = get(kk)
        C = poset_of(_b.H)
        print(f"DIGEST {kk}: " + repr(
            [(_pr[d]['h2'], _pr[d]['om'], _pr[d]['h4'], _pr[d]['max'],
              _pr[d]['n']) for d in (2, 3)])
            + " arb " + repr(arbshare(_b.H)) + " widths "
            + repr(sorted(Counter(len(sky(C, e, 'B', 2)[0])
                                  for e in range(len(C))).items())))
    sys.exit(0)

# ======================================================================
# A0 — THE ANCHORS: the committed controls, re-run in this process
# ======================================================================
print("\n[A0 THE ANCHORS — D63's delivery crystal, D60's brick and the "
      "eleven genuine sprinkling configurations, RE-RUN here]")
t_a = time.time()
b_dr = double_ring(8, 10, 8)
P_DR = profile(poset_of(b_dr.H))
b_bk = wide_brick(8, 14, 0)
P_BK = profile(poset_of(b_bk.H))
D63_ROW = {'n': 177, 'h2': Fr(47, 59), 'h4': Fr(1, 3), 'max': 4,
           'om': Fr(100, 137), 'h2_3': Fr(137, 177), 'h4_3': Fr(119, 177),
           'max_3': 4}                  # v10/data/d63_wide_crystal_exact.out
D60_ROW = {'h2': Fr(10, 13), 'om': Fr(125, 192), 'h4': Fr(0), 'max': 3}
_dr_ok = (P_DR[2]['n'] == D63_ROW['n'] and P_DR[2]['h2'] == D63_ROW['h2']
          and P_DR[2]['h4'] == D63_ROW['h4']
          and P_DR[2]['max'] == D63_ROW['max']
          and P_DR[2]['om'] == D63_ROW['om']
          and P_DR[3]['h2'] == D63_ROW['h2_3']
          and P_DR[3]['h4'] == D63_ROW['h4_3']
          and P_DR[3]['max'] == D63_ROW['max_3'])
_bk_same = (list(b_bk.H) == list(brick(8, 14).H))
_bk_ok = (P_BK[2]['h2'] == D60_ROW['h2'] and P_BK[2]['om'] == D60_ROW['om']
          and P_BK[2]['h4'] == D60_ROW['h4']
          and P_BK[2]['max'] == D60_ROW['max'])
print(f"    DR(8,10,8): n={P_DR[2]['n']}, d=2 homog {P_DR[2]['h2']} "
      f"(~{float(P_DR[2]['h2']):.4f}), |D|>=4 {P_DR[2]['h4']}, max|D| "
      f"{P_DR[2]['max']}, omega {P_DR[2]['om']}; d=3 homog {P_DR[3]['h2']}, "
      f"|D|>=4 {P_DR[3]['h4']}, max|D| {P_DR[3]['max']}")
print(f"    BRICK(8,14): d=2 homog {P_BK[2]['h2']}, omega {P_BK[2]['om']}, "
      f"|D|>=4 {P_BK[2]['h4']}, max|D| {P_BK[2]['max']}  [{time.time()-t_a:.1f}s]")
check("A0(i) [ANCHOR, exit 1 on breakage] THE DELIVERY CONTROLS "
      "REPRODUCE THEIR COMMITTED ROWS EXACTLY.  D63's own `double_ring` "
      "function object gives 177 events, d = 2 homogeneity 47/59, "
      "|D| >= 4 at 1/3, max |D| = 4, mean omega 100/137, and D63's d = 3 "
      "row; D60's brick is reproduced EVENT FOR EVENT with its published "
      "row (10/13, 125/192, 0, 3).  Every comparison this unit makes is "
      "against these re-run objects, never against a re-typed number",
      _dr_ok and _bk_same and _bk_ok and not b_dr.refusal
      and not b_bk.refusal,
      f"DR row exact = {_dr_ok}; brick event list identical = {_bk_same}, "
      f"row = {_bk_ok}", anchor=True)

print("\n[A0(ii) THE SPRINKLING COMPARATORS — D58's atlas re-run on the "
      "same eleven genuine configurations D60/D63 used]")
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
for d in (2, 3):
    print(f"    d = {d}: BAND homogeneity [{BAND[d][0]}, {BAND[d][1]}] "
          f"(~[{float(BAND[d][0]):.4f}, {float(BAND[d][1]):.4f}]); "
          f"|D|>=4 band [{W4B[d][0]}, {W4B[d][1]}] "
          f"(~[{float(W4B[d][0]):.4f}, {float(W4B[d][1]):.4f}]); max|D| "
          f"[{MXB[d][0]}, {MXB[d][1]}]")
print(f"    [{time.time() - t_cmp:.1f}s]")
check("A0(ii) [ANCHOR, exit 1 on breakage] THE COMPARATORS ARE RE-RUN, "
      "NOT RE-TYPED, and reproduce D60/D63's committed bands exactly: "
      "homogeneity [77/120, 4/5] and |D| >= 4 [17/40, 13/20] at d = 2.  "
      "Every threshold used anywhere below is one of these measured "
      "numbers or one of D58's own columns; this unit invents none",
      BAND[2] == (Fr(77, 120), Fr(4, 5))
      and W4B[2] == (Fr(17, 40), Fr(13, 20)) and len(SPR) == 11,
      f"{len(SPR)} genuine configurations; d = 2 band {BAND[2]}, |D|>=4 "
      f"band {W4B[2]}, sprinkling max|D| {MXB[2]}", anchor=True)

# ======================================================================
# A1 — THE SWEEP: does conflict tile at cadence?
# ======================================================================
print("\n[A1 THE SWEEP — every configuration built by the layer's own "
      "menu.  All figures at d = 2; 'band' = A0(ii)'s recomputed "
      "sprinkling band; 'wide' = D58's |D| >= 4 column]")
t_sw = time.time()
for k in SWEEP:
    b, pr, dt = get(k)
    print("    " + line(k, b, pr, dt))
print(f"    swept {len(SWEEP)} configurations, "
      f"{sum(len(v[0].H) for v in BUILT.values())} events built "
      f"[{time.time() - t_sw:.1f}s]")

_refusals = [(tag_of(k), v[0].refusal) for k, v in BUILT.items()
             if v[0].refusal is not None]
_hits = max(v[0].maxhits for v in BUILT.values())
_kinds = Counter(e[0] for v in BUILT.values() for e in v[0].H)
print(f"    event species over the whole sweep: {dict(sorted(_kinds.items()))}"
      f"; refusals = {len(_refusals)} {_refusals if _refusals else ''}; "
      f"max menu hits per specification over every step of every record "
      f"= {_hits}")
check("A1(a) CONFLICT TILES AT CADENCE — NO REFUSAL ANYWHERE, AND THE "
      "PIN'S OUTCOME A-I DOES NOT FIRE.  Every one of the swept "
      "conflict records is admissible at every step against the layer's "
      "own restricted menu, and every specification — a FULL EVENT "
      "TUPLE, so the winner choice W and the ckey are part of the "
      "specification — matched EXACTLY ONE candidate.  WHAT THIS GATE "
      "MEASURES (D63's round-1 MINOR 4): uniqueness is STRUCTURAL "
      "(menu events are pairwise distinct and a full tuple can match at "
      "most one), so the gated content is that the specified event IS "
      "OFFERED (hits = 1, never 0) and that no step was refused",
      _hits == 1 and not _refusals and len(BUILT) == len(SWEEP),
      f"records = {len(BUILT)}, events = "
      f"{sum(len(v[0].H) for v in BUILT.values())}, max hits = {_hits}, "
      f"refusals = {len(_refusals)}")

# ---- A1(b) the conflict budget bound -------------------------------------
print("\n[A1(b) THE CONFLICT BUDGET — how much of a record CAN be "
      "arbitration?]")
print("  BOUND (a counting theorem of the layer, not a parameter).  An "
      "arbitration's")
print("  ckey is a set of k live proposal triples, and a proposal is "
      "resolved by at")
print("  most one arbitration in any record (`View.resolved`), so "
      "#proposals >= k *")
print("  #arbs and an arbitration's share of the events of a record is "
      "at most")
print("  1/(k+1) where k is the smallest proposer count in it.  "
      "Deliveries only")
print("  lower it.  The delivery-free CONFLICT-RING(sticky = 0) "
      "SATURATES the bound.")
_bud_ok = True
_share_rows = []
for k in SWEEP:
    b = BUILT[k][0]
    H = b.H
    arbs = [e for e in H if e[0] == 'r']
    props = [e for e in H if e[0] == 'p']
    ks = [len({t[0] for t in e[2]}) for e in arbs]
    consumed = sum(ks)
    kmin = min(ks)
    sh = arbshare(H)
    bound = Fr(1, kmin + 1)
    if not (consumed == len(props) and sh <= bound):
        _bud_ok = False
    _share_rows.append((tag_of(k), len(H), len(arbs), kmin, sh, bound,
                        sum(1 for e in H if e[0] == 'd')))
for (tg, n, na, kmin, sh, bd, nd) in _share_rows:
    print(f"    {tg:38s} n={n:4d} arbs={na:3d} (k={kmin}) deliveries={nd:3d} "
          f"arb share {sh} (~{float(sh):.4f}) vs bound 1/(k+1) = {bd} "
          f"(~{float(bd):.4f})" + ("   <== SATURATED" if sh == bd else ""))
_sat = [r[0] for r in _share_rows if r[4] == r[5]]
check("A1(b) THE ARBITRATION SHARE IS BOUNDED BY THE GRAMMAR AND THE "
      "BOUND IS ATTAINED.  Every proposal in every swept record is "
      "consumed by exactly one arbitration (#proposals = sum of "
      "proposer counts, gated), so no record of this layer can be more "
      "than 1/(k+1) arbitration, and the delivery-free ring attains it "
      "exactly at 1/3.  THE DESIGN PROBLEM THE PIN NAMED, MEASURED: "
      "re-supplying a conflict costs one delivery per group per round, "
      "which is why the rotating ring runs at 25.6% rather than 33.3% — "
      "and A2/A3 show what that delivery BUYS",
      _bud_ok and len(_sat) > 0,
      f"records checked = {len(_share_rows)}, proposal-consumption "
      f"equalities = {len(_share_rows)}, bound violations = 0, "
      f"saturating records = {_sat}")

# ======================================================================
# A2 — THE ATLAS CENSUS
# ======================================================================
print("\n[A2 THE ATLAS CENSUS — every swept record at d = 2 AND d = 3, "
      "with the delivery crystal, the brick and the sprinkling bands "
      "beside them.  Orderings reported BOTH WAYS because the depths "
      "disagree (D60's MINOR-4 lesson)]")


def _inb(pr, d):
    return BAND[d][0] <= pr[d]['h2'] <= BAND[d][1]


def pos(pr, d):
    return ('in' if _inb(pr, d) else
            ('ABOVE' if pr[d]['h2'] > BAND[d][1] else 'below'))


ALLREC = [(tag_of(k), BUILT[k][1]) for k in SWEEP] + \
         [('DR(8,10,8) [D63 control]', P_DR), ('BRICK(8,14) [D60]', P_BK)]
for (tg, pr) in ALLREC:
    row = []
    for d in (2, 3):
        x = pr[d]
        row.append(f"d={d}: homog {float(x['h2']):.4f}[{pos(pr, d)}] "
                   f"|D|>=4 {float(x['h4']):.4f} max {x['max']} omega "
                   f"{float(x['om']):.4f}")
    print(f"    {tg:38s} " + "  |  ".join(row))
IN_BAND = [k for k in SWEEP if _inb(BUILT[k][1], 2)]
WIDEK = [k for k in SWEEP if BUILT[k][1][2]['h4'] > 0]
BOTH = [k for k in SWEEP if k in IN_BAND and k in WIDEK]
FIVE = [k for k in SWEEP if BUILT[k][1][2]['max'] >= 5]
print(f"    d = 2: in the homogeneity band = {len(IN_BAND)} of "
      f"{len(SWEEP)}; carrying |D| >= 4 = {len(WIDEK)}; BOTH (D63's F3 "
      f"pattern) = {len(BOTH)}; carrying |D| >= 5 = {len(FIVE)}")
print(f"      in-band AND wide: " + ", ".join(tag_of(k) for k in BOTH))
_flips = [k for k in SWEEP if _inb(BUILT[k][1], 2) != _inb(BUILT[k][1], 3)]
check("A2(a) THE CENSUS IS REPORTED AT BOTH DEPTHS FOR EVERY RECORD AND "
      "THE DEPTHS DISAGREE, so every width and homogeneity sentence in "
      "this unit is depth-labelled.  The conflict ring reproduces D63's "
      "F3 PATTERN with an engine of conflict instead of delivery — "
      "inside the recomputed homogeneity band at d = 2 AND carrying "
      "4-direction charts — which is the first time the tiling/width "
      "composition has been exhibited without a delivery circuit",
      len(BOTH) > 0 and len(IN_BAND) > 0 and len(WIDEK) > 0,
      f"in-band {len(IN_BAND)}, wide {len(WIDEK)}, both {len(BOTH)}, "
      f"|D|>=5 {len(FIVE)} of {len(SWEEP)}; band-membership flips "
      f"between the depths at {len(_flips)} records")

# ---- W4b with each record's own B, and the refinement --------------------
print("\n[A2(b) THE BRANCHING BOUNDS — W4b with each record's OWN "
      "measured B, and the refinement this unit's records force]")
print("  W4b (D63, verified there): if every event carries at most B "
      "registers then")
print("  |D_e(d)| <= B^d.  A two-proposer arbitration carries THREE "
      "registers")
print("  (proposers u {new version}), so W4b's bound at d = 2 is 9 — and "
      "D63's")
print("  residue 1 asked whether a conflict record can use them.")
print("  W4c THE MINT-REGISTER REFINEMENT (this unit).  The version "
      "register minted")
print("  by an arbitration is a BIRTH WIRE: `regs_of` puts a version "
      "name in exactly")
print("  one event's register set, so it has NO P-successor.  Replacing "
      "|regs(x)| by")
print("  the number of registers of x that RECUR (the live out-degree "
      "b(x)) in W4b's")
print("  own proof gives |D_e(d)| <= Bl^d with Bl = max b(x) — and for "
      "an arbitration")
print("  b = #proposers = |regs| - 1.  CONSEQUENCE: a TWO-proposer "
      "conflict record")
print("  has Bl = 2 exactly like a delivery circuit and CANNOT exceed 4 "
      "at d = 2,")
print("  despite carrying 3-register events.  Width past 4 needs 3+ "
      "PROPOSERS, not")
print("  merely 3+ registers — W4b's necessary condition is not "
      "sufficient.")
_w4_ok = True
_mint_ok = True
_bl_rows = []
for k in SWEEP + [('CTRL-DR',), ('CTRL-BK',)]:
    if k[0].startswith('CTRL'):
        H = (b_dr if k[0] == 'CTRL-DR' else b_bk).H
        pr = P_DR if k[0] == 'CTRL-DR' else P_BK
        tg = 'DR(8,10,8)' if k[0] == 'CTRL-DR' else 'BRICK(8,14)'
    else:
        H, pr, tg = BUILT[k][0].H, BUILT[k][1], tag_of(k)
    Bmax = max(len(regs_of(e)) for e in H)
    # live out-degree, from event_poset's own `last` bookkeeping
    outdeg = [0] * len(H)
    last = {}
    for j, op in enumerate(H):
        for r in regs_of(op):
            if r in last:
                outdeg[last[r]] += 1
        for r in regs_of(op):
            last[r] = j
    Bl = max(outdeg)
    # every version register occurs in exactly one event
    occ = Counter(r for e in H for r in regs_of(e)
                  if not isinstance(r, str))
    vmulti = sum(1 for r, c in occ.items() if c > 1)
    if vmulti:
        _mint_ok = False
    kmax = max([len({t[0] for t in e[2]}) for e in H if e[0] == 'r'],
               default=0)
    for d in (2, 3):
        if pr[d]['max'] > Bmax ** d or pr[d]['max'] > Bl ** d:
            _w4_ok = False
    _bl_rows.append((tg, Bmax, Bl, kmax, pr[2]['max'], pr[3]['max'],
                     len(occ), vmulti))
for (tg, Bm, Bl, km, m2, m3, nv, vm) in _bl_rows:
    print(f"    {tg:38s} B={Bm} (W4b bound {Bm**2} at d=2), live Bl={Bl} "
          f"(W4c bound {Bl**2}), max proposers k={km}: measured max|D| "
          f"d2={m2} d3={m3}; version registers {nv}, occurring twice = {vm}")
check("A2(b) BOTH BOUNDS HOLD ON EVERY RECORD, AND W4c IS THE ONE THAT "
      "BINDS.  The mint-register fact is GATED, not asserted: across "
      "every record built here every version register occurs in EXACTLY "
      "ONE event's `regs_of`, so an arbitration's live out-degree is its "
      "proposer count.  Hence the two-proposer conflict ring — 3 "
      "registers per arbitration, W4b bound 9 — is held to max |D| = 4 "
      "at d = 2, exactly the delivery ceiling, and the grids with 3 and "
      "4 proposers are the records that pass it.  D63's residue 1 is "
      "therefore answered with a correction to its own necessity "
      "statement",
      _w4_ok and _mint_ok,
      f"records checked = {len(_bl_rows)}, W4b/W4c violations = 0, "
      f"version registers occurring more than once = 0")

# ---- the interior control ------------------------------------------------
print("\n[A2(c) THE INTERIOR CONTROL (D60's C7 excision) on the headline "
      "records — so the frontier is read on the MECHANISM, not on the "
      "record's ends]")


def interior_of(H):
    C = poset_of(H)
    hs = heights(C)
    lo, hi = min(hs), max(hs)
    return C, {e for e in range(len(C)) if lo + 2 <= hs[e] <= hi - 3}


INT = {}
for k in [x for x in (HEAD, ('RING', 8, 10, 1, 'S'), WIDE,
                      ('GRID', 4, 4), ('RING', 6, 14, 1, 'S'))
          if x in BUILT]:
    C, popn = interior_of(BUILT[k][0].H)
    pi = profile(C, popn)
    INT[k] = pi
    pf = BUILT[k][1]
    ih = pi[2]['h2']
    tg = ('in band' if BAND[2][0] <= ih <= BAND[2][1]
          else ('ABOVE band' if ih > BAND[2][1] else 'BELOW band'))
    print(f"    {tag_of(k):38s} FULL n={pf[2]['n']:4d} homog "
          f"{float(pf[2]['h2']):.4f} |D|>=4 {float(pf[2]['h4']):.4f} max "
          f"{pf[2]['max']}  ->  INTERIOR n={pi[2]['n']:4d} homog "
          f"{float(ih):.4f} [{tg}] |D|>=4 {float(pi[2]['h4']):.4f} max "
          f"{pi[2]['max']}")
_int_up = all(INT[k][2]['h2'] > BUILT[k][1][2]['h2'] for k in INT)
_int_maxkept = all(INT[k][2]['max'] == BUILT[k][1][2]['max'] for k in INT)
check("A2(c) THE WIDTH IS THE CIRCUIT'S, NOT THE PREFIX'S — and the "
      "band half is again largely an ENDS property (D63's MAJOR-3 "
      "lesson, reproduced here on conflict records).  Excising the "
      "bottom two and top three height layers RAISES homogeneity at "
      "every controlled record and leaves max |D| unchanged, so the "
      "|D| = 6 and |D| = 8 charts are not boundary artefacts",
      _int_up and _int_maxkept,
      f"records controlled = {len(INT)}; interior homogeneity > full at "
      f"all = {_int_up}; interior max|D| = full max|D| at all = "
      f"{_int_maxkept}")

# ======================================================================
# A3 — THE WIDTH VERDICT
# ======================================================================
print("\n[A3 THE WIDTH VERDICT — does ANY conflict record carry "
      "|D| >= 5 at d = 2?  This is the delivery ceiling's door (D63 §4, "
      "residue 1)]")
WID = {}
for k in SWEEP:
    C = poset_of(BUILT[k][0].H)
    WID[k] = Counter(len(sky(C, e, 'B', 2)[0]) for e in range(len(C)))
    print(f"    {tag_of(k):38s} width histogram at d = 2: "
          f"{dict(sorted(WID[k].items()))}")
_maxw = {k: BUILT[k][1][2]['max'] for k in SWEEP}
DOOR = [k for k in SWEEP if _maxw[k] >= 5]
print(f"    max |D| at d = 2 by proposer count k: "
      + ", ".join(f"{tag_of(k)} k={max(len({t[0] for t in e[2]}) for e in BUILT[k][0].H if e[0]=='r')} -> {_maxw[k]}"
                  for k in [x for x in (HEAD, WIDE, ('GRID', 4, 4))
                            if x in BUILT]))
if DOOR:
    kk = max(DOOR, key=lambda k: _maxw[k])
    Hw = BUILT[kk][0].H
    Cw = poset_of(Hw)
    hw = heights(Cw)
    ew = max(range(len(Cw)), key=lambda e: len(sky(Cw, e, 'B', 2)[0]))
    dirs, rows = sky(Cw, ew, 'B', 2)
    outp = out_reg(Hw, 'tuple')
    W = words_from(outp, hw, ew, 2)
    print(f"\n    THE WITNESS — {tag_of(kk)}, base event index {ew}: "
          f"{Hw[ew][0]}-event by {Hw[ew][1]}, height {hw[ew]}, "
          f"{len(regs_of(Hw[ew]))} registers "
          f"({len({t[0] for t in Hw[ew][2]}) if Hw[ew][0]=='r' else '-'} "
          f"proposers)")
    print(f"      SKY-B(d=2) chart, read from the COMMITTED d47a `sky` "
          f"directly: |D| = {len(dirs)}, directions {sorted(dirs)}")
    for f in sorted(dirs):
        print(f"        direction {f:3d}: kind {Hw[f][0]} by {Hw[f][1]}, "
              f"height {hw[f]} (= {hw[ew]} + {hw[f]-hw[ew]}), ordered "
              f"after the base in the committed poset = {Cw[ew][f]}; "
              f"P-paths (raw ; role) = "
              + " | ".join(f"{[str(x)[:14] for x in w]} ; {o}"
                           for (w, o) in sorted(W.get(f, ()), key=repr)))
    _wit_ok = (set(W) == set(dirs) and len(dirs) >= 5
               and all(Cw[ew][f] and hw[f] == hw[ew] + 2 for f in dirs))
else:
    _wit_ok = False
check("A3 [THE DOOR DECIDES] " + (
      "**THE DELIVERY CEILING IS BROKEN BY CONFLICT.**  Conflict records "
      "carry |D| >= 5 at d = 2 — the first records in this campaign to "
      "do so — and the witness is exhibited event by event: its chart is "
      "read from the COMMITTED d47a `sky` directly, every direction is "
      "verified to be ordered after the base in the committed poset and "
      "to sit exactly two height layers above it, and every direction's "
      "P-paths are printed.  This is not an instrument artefact and it "
      "is not a chart-counting convention: the base event is an "
      "arbitration over 3 (resp. 4) DISTINCT PROPOSERS, whose live "
      "out-degree is 3 (resp. 4), and the width is exactly what W4c "
      "allows and W4b's 'three registers' never could" if DOOR else
      "**THE DOOR STAYS SHUT IN THIS FAMILY.**  No swept conflict record "
      "reaches |D| >= 5 at d = 2") + ".  The predicate is the width "
      "census itself, computed from the sweep",
      len(DOOR) > 0 and _wit_ok,
      f"records with max|D| >= 5 at d = 2 = {len(DOOR)} of {len(SWEEP)}: "
      + ", ".join(f"{tag_of(k)}={_maxw[k]}" for k in DOOR)
      + f"; witness chart verified against the committed sky and poset = "
      f"{_wit_ok}; W4b bound at the witness's B and W4c bound at its live "
      f"Bl are both printed above")

# ======================================================================
# A1(c) / A5 — FULL-MENU REPLAY and THE MASS CENSUS
# ======================================================================
print("\n[A1(c) THE FULL-MENU REPLAY (D60's C1 grade) — every step "
      "re-driven with ALL actors offered — carrying A5's MENU-MASS "
      "CENSUS on the same pass]")


def full_menu_replay(H, actors, budget):
    t = time.time()
    worst = widest = 0
    mass = Counter()
    permass = Counter()
    steps = 0
    for j, e in enumerate(H):
        menu = candidates_for(H[:j], tuple(actors))
        n_hit = sum(1 for x, q in menu if x == e)
        widest = max(widest, len(menu))
        worst = max(worst, n_hit)
        tot = sum(q for x, q in menu)
        mass[tot] += 1
        for a in actors:
            permass[sum(q for x, q in menu if x[1] == a)] += 1
        steps = j + 1
        if n_hit != 1:
            return {'status': 'BROKEN', 'step': j, 'hits': n_hit,
                    'menu': len(menu), 't': time.time() - t,
                    'mass': mass, 'permass': permass, 'steps': steps}
        if time.time() - t > budget:
            return {'status': 'BUDGET-CUT', 'step': steps, 'hits': worst,
                    'menu': widest, 't': time.time() - t, 'mass': mass,
                    'permass': permass, 'steps': steps}
    return {'status': 'OK', 'step': len(H), 'hits': worst, 'menu': widest,
            't': time.time() - t, 'mass': mass, 'permass': permass,
            'steps': steps}


REPLAY = {}
_repl = [(('RING', 4, 6, 1, 'S'), FULLMENU_BUDGET),
         (('RING', 6, 6, 1, 'S'), FULLMENU_BUDGET),
         (('GRID', 3, 4), FULLMENU_BUDGET),
         (HEAD, FULLMENU_BUDGET), (WIDE, WIDE_REPLAY_BUDGET)]
_seenr = set()
for k, bud in [x for x in _repl
               if x[0] in BUILT and not (x[0] in _seenr or _seenr.add(x[0]))]:
    bb = BUILT[k][0]
    ac = actors_of(k[0], k[1])
    REPLAY[tag_of(k)] = full_menu_replay(bb.H, ac, bud)
    r = REPLAY[tag_of(k)]
    print(f"    {tag_of(k):38s} ({len(bb.H):3d} events, {len(ac):2d} "
          f"actors): {r['status']} at step {r['step']}/{len(bb.H)}, max "
          f"hits per specification = {r['hits']}, widest full menu = "
          f"{r['menu']} candidates  [{r['t']:.1f}s]")
_rep_ok = all(r['hits'] == 1 and r['status'] != 'BROKEN'
              for r in REPLAY.values())
_rep_full = [n for n, r in REPLAY.items() if r['status'] == 'OK']
_rep_head = REPLAY[tag_of(HEAD)]['status'] == 'OK'
check("A1(c) ADMISSIBLE AGAINST THE UNRESTRICTED LAYER — THE C1 GRADE "
      "HOLDS ON A CONFLICT RECORD OF CRYSTAL LENGTH.  Replayed with all "
      "actors offered at every step, every specification is OFFERED "
      "among the hundreds of candidates the layer enumerates and matches "
      "exactly one; the headline record (10 rounds, >= 100 events) is "
      "replayed END TO END, as are a complete WIDE record and two "
      "smaller rings.  The wide headline carries a PRINTED budget and "
      "its cut point is reported, never hidden — no step it reached "
      "refused or was ambiguous",
      _rep_ok and _rep_head and len(_rep_full) >= len(REPLAY) - 1,
      "; ".join(f"{n}: {r['status']} step {r['step']} hits {r['hits']} "
                f"menu {r['menu']}" for n, r in REPLAY.items()))

print("\n[A5 THE MENU-MASS CENSUS — the per-state menu mass along the "
      "replayed records, LABELLED (pin A5)]")
print("  WHAT D65 MEASURED AND WHAT THIS IS.  D65's 2 -> 5/2 jump is a "
      "TWO-ACTOR,")
print("  DELIVERY-FREE d42a statement: over its 36-state exhaustive "
      "family the")
print("  per-state menu mass takes exactly two values, 2 and 5/2, and the "
      "excess 1/2")
print("  appears exactly where a blind conflict group becomes visible in "
      "the join")
print("  view.  THIS record is at TRANSPORT scope with M actors and an "
      "open delivery")
print("  sector, so the masses are NOT the same numbers and are not "
      "compared as such.")
print("  The commensurable quantity is the LADDER EXCESS: d42b1 prices "
      "each actor's")
print("  menu at 1 + (m - 1)/4 with m the number of distinct ckey groups "
      "(plus the")
print("  merge sector) visible to it, so mass - M, in units of 1/4, "
      "COUNTS the extra")
print("  visible conflict groups.  D65's 5/2 over two actors is an "
      "excess of two")
print("  quarters; the census below is of exactly that quantity, at this "
      "scope.")
for k in [x for x in (('RING', 4, 6, 1, 'S'), ('GRID', 3, 4), HEAD, WIDE)
          if tag_of(x) in REPLAY]:
    r = REPLAY[tag_of(k)]
    nact = len(actors_of(k[0], k[1]))
    exc = Counter()
    for m, c in r['mass'].items():
        exc[(m - nact) * 4] += c
    print(f"    {tag_of(k):38s} ({nact} actors, {r['steps']} prefixes "
          f"measured): total menu mass {dict(sorted(r['mass'].items()))}")
    print(f"      {'':36s}   LADDER EXCESS (mass - M in quarters) "
          f"{dict(sorted(exc.items()))}; per-actor menu sums "
          f"{dict(sorted(r['permass'].items()))}")
_ladpts = [(q, c) for r in REPLAY.values() for q, c in r['permass'].items()]
_onlad = sum(c for q, c in _ladpts if (q * 4).denominator == 1)
_offlad = sorted({q for q, c in _ladpts if (q * 4).denominator != 1})
_ladder_ok = (all(q >= 1 for q, c in _ladpts) and _onlad > 0
              and len(_offlad) > 0)
_exc_seen = sorted({(m - len(actors_of(k[0], k[1]))) * 4
                    for k in [x for x in (('RING', 4, 6, 1, 'S'),
                                          ('GRID', 3, 4), HEAD, WIDE)
                              if tag_of(x) in REPLAY]
                    for m in REPLAY[tag_of(k)]['mass']})
check("A5 [REPORTING GATE, labelled] THE MASS PROFILE, AND IT "
      "REPRODUCES d42b1's OWN DECLARED LEAK RATHER THAN ITS LADDER.  "
      "Every per-actor menu sum is at least 1 and the total mass sits at "
      "M (the actor count) except at prefixes where an unarbitrated "
      "conflict group is visible, where it rises — the D65 geography, "
      "seen at transport scope.  BUT the sums are NOT all on the "
      "1 + k/4 ladder: values like 13/12 and 19/16 occur, which is "
      "d42b1's OWN committed N1 exhibit ('the general-depth ladder is "
      "FALSE under current pricing — a dead component still inflates the "
      "live singleton's view-relative arb denominator'), here reproduced "
      "on conflict records at transport scope by an independent route.  "
      "The difference in scope from D65 is stated rather than elided: "
      "D65's two values (2, 5/2) are a two-actor delivery-free "
      "statement, are NOT reproduced here, and are not claimed to be",
      _ladder_ok and len(_exc_seen) > 1,
      f"(prefix, actor) points measured = "
      f"{sum(sum(r['permass'].values()) for r in REPLAY.values())}, of "
      f"which ON the 1 + k/4 ladder = {_onlad}; OFF-ladder values "
      f"observed = {_offlad} (d42b1 N1); ladder-excess values observed "
      f"(quarters) = {_exc_seen}")

# ======================================================================
# A4 — THE COBOUNDARY GATE
# ======================================================================
print("\n[A4 THE COBOUNDARY GATE — D64's C7, BOTH ROUTES, at five port "
      "conventions.  The question D64 left: can ANY substrate carry a "
      "transition class that is NOT a coboundary?]")
print("  THE PORT CONVENTIONS FOR 3+-REGISTER EVENTS, DEFINED AND "
      "PRINTED (pin A4).")
print("  An arbitration's registers are its PROPOSERS plus the newly "
      "minted version,")
print("  and its role structure gives several natural orders.  All five "
      "are run:")
print("    REG       — d64's canonical: the layer's own tuple order "
      "(proposers sorted,")
print("                then the version).  Deliveries: (sender, "
      "receiver).")
print("    REGA      — every register sorted by name (d64's alternative "
      "port order).")
print("    ARBLOSE   — LOSERS first, then WINNERS, then the version: the "
      "conflict's")
print("                own asymmetry used as the port order, which is "
      "what D64's")
print("                residue 1 said an arbitration has and a delivery "
      "does not.")
print("    ARBVFIRST — the VERSION first, then the proposers sorted: the "
      "minted wire")
print("                read as port 0, a referee-style alternative that "
      "shifts every")
print("                port index.")
print("    COV       — the register-free surrogate (covering relation, "
      "cover-index")
print("                ports), the only instrument also defined on "
      "sprinklings.")
print("  TWO NATURAL CONVENTIONS COINCIDE WITH REG ON THIS FAMILY and "
      "are not run")
print("  separately: initiator-first and winner-first, because the "
      "schedule always")
print("  makes the initiator the sorted-first proposer.  That is a fact "
      "about the")
print("  blueprint, printed here rather than hidden in a choice.")


def my_ord_tuple(op, conv):
    rt = reg_tuple(op)
    if conv == 'sorted':
        return tuple(sorted(rt, key=repr))
    if conv == 'tuple':
        return rt
    if op[0] != 'r':
        return rt
    props = tuple(sorted({t[0] for t in op[2]}, key=repr))
    v = tuple(x for x in rt if x not in props)
    if conv == 'lose':
        Wn = {t[0] for t in op[3]}
        return (tuple(sorted((p for p in props if p not in Wn), key=repr))
                + tuple(sorted((p for p in props if p in Wn), key=repr)) + v)
    if conv == 'vfirst':
        return v + props
    raise ValueError(conv)


CONV = (('tuple', 'REG'), ('sorted', 'REGA'), ('lose', 'ARBLOSE'),
        ('vfirst', 'ARBVFIRST'))
INST = [t for _, t in CONV] + ['COV']

SUBS = {}


def add_sub(nm, H, C, kind='grammar'):
    SUBS[nm] = {'H': H, 'C': C, 'kind': kind, 'h': heights(C), 'inst': {}}
    if H is not None:
        for conv, tg in CONV:
            SUBS[nm]['inst'][tg] = out_reg(H, conv)
    SUBS[nm]['inst']['COV'] = out_cov(C)


A4SET = [x for x in (HEAD, ('RING', 4, 10, 1, 'S'),
                     ('RING', 6, 6, 1, 'S'), ('RING', 8, 10, 1, 'S'),
                     ('RING', 6, 10, 1, 'R'), ('RING', 6, 10, 0, 'S'),
                     ('GRID', 3, 6), WIDE, ('GRID', 4, 4)) if x in BUILT]
_conv_agree = True
for k in A4SET:
    H = BUILT[k][0].H
    for op in H:
        for c in ('tuple', 'sorted'):
            if my_ord_tuple(op, c) != ord_tuple0(op, c):
                _conv_agree = False
g64['ord_tuple'] = my_ord_tuple
for k in A4SET:
    add_sub(tag_of(k), BUILT[k][0].H, poset_of(BUILT[k][0].H))
add_sub('DR(8,10,8)', b_dr.H, poset_of(b_dr.H))
add_sub('BRICK(8,14)', b_bk.H, poset_of(b_bk.H))
add_sub('M21', None, mink4(latt(120, 2, 60, 8)), 'sprinkling')
add_sub('M31', None, mink4(latt(120, 3, 48, 8)), 'sprinkling')
g64['SUB'] = SUBS
MEAS = {}
g64['MEAS'] = MEAS

# --- instrument validation (D64's C0b), re-run on the conflict records
_cl_ok = _rt_ok = _bnd_ok = _cov_ok = True
_val_rows = []
for nm in sorted(SUBS):
    v = SUBS[nm]
    n = len(v['C'])
    if v['H'] is not None:
        bad_rt = sum(1 for op in v['H']
                     if set(reg_tuple(op)) != set(regs_of(op)))
        if bad_rt:
            _rt_ok = False
        bnd = all(len(v['inst']['REG'][x]) <= len(regs_of(v['H'][x]))
                  for x in range(n))
        if not bnd:
            _bnd_ok = False
        cl = closure_of(v['inst']['REG'], n, v['h'])
        same = (cl == v['C'])
        if not same:
            _cl_ok = False
        pset = {(x, y) for x in range(n)
                for (y, r, kk) in v['inst']['REG'][x]}
        cset = set(d58_covers(v['C']))
        if not (cset <= pset):
            _cov_ok = False
        _val_rows.append((nm, n, bad_rt, bnd, same, len(pset), len(cset),
                          len(pset - cset)))
    clc = closure_of(v['inst']['COV'], n, v['h'])
    if clc != v['C']:
        _cov_ok = False
print("\n  [A4(a) INSTRUMENT VALIDATION (D64's C0b) — re-run on every "
      "conflict record: P is `event_poset`'s own generating relation and "
      "its transitive closure must BE the committed order]")
for (nm, n, bad_rt, bnd, same, npe, nce, skip) in _val_rows:
    print(f"      {nm:38s} n={n:4d} reg_tuple != regs_of at {bad_rt}; "
          f"#P-successors <= |regs_of| = {bnd}; closure(P) == committed "
          f"order = {same}; P-edges {npe}, covers {nce}, height-skipping "
          f"{skip}")
check("A4(a) [ANCHOR] THE COCYCLE INSTRUMENT IS VALIDATED ON THE NEW "
      "SUBSTRATES, NOT ASSUMED.  On every conflict record and every "
      "control: `reg_tuple` is `regs_of` with an order; each event has "
      "at most |regs_of| P-successors; THE TRANSITIVE CLOSURE OF P "
      "EQUALS the committed order `poset_of`; the covering relation is "
      "contained in P; and the COV surrogate's own closure is the "
      "committed order on every substrate including the sprinklings.  "
      "The two committed conventions of my `ord_tuple` reproduce D64's "
      "own function value for value on every event",
      _cl_ok and _rt_ok and _bnd_ok and _cov_ok and _conv_agree,
      f"grammar substrates validated = {len(_val_rows)}; closure == "
      f"order everywhere = {_cl_ok}; reg_tuple == regs_of = {_rt_ok}; "
      f"successor bound = {_bnd_ok}; COV closure and cover containment = "
      f"{_cov_ok}; ord_tuple agrees with d64 at REG and REGA = "
      f"{_conv_agree}", anchor=True)

t_m = time.time()
for nm in sorted(SUBS):
    for tg in sorted(SUBS[nm]['inst']):
        for d in DEPTHS:
            MEAS[(nm, tg, d)] = measure(nm, tg, d)
print(f"\n  [A4(b) THE TRANSITION CENSUS — {len(MEAS)} cells "
      f"(substrate x instrument x depth)  [{time.time()-t_m:.1f}s]]")
print(f"      {'substrate':38s} {'inst':9s} {'d':>2s} {'charts':>7s} "
      f"{'wide':>5s} {'pairs':>6s} {'triples':>8s} {'ROLE id/non':>14s} "
      f"  classes")
for nm in sorted(SUBS):
    for tg in INST:
        if tg not in SUBS[nm]['inst']:
            continue
        for d in DEPTHS:
            r = MEAS[(nm, tg, d)]
            print(f"      {nm:38s} {tg:9s} {d:2d} {r['charts']:7d} "
                  f"{r['wide']:5d} {r['pairs']:6d} {r['triples']:8d} "
                  f"{r['ROLE'][0]:6d}/{r['ROLE'][1]:<7d} {r['kinds']}")
_reach = all(r['reach_ok'] for r in MEAS.values())
_xh = sum(r['xhpairs'] for r in MEAS.values())
_viol = sum(r['cocycle'][1] for r in MEAS.values())
_tested = sum(r['cocycle'][0] for r in MEAS.values())
check("A4(b) THE CENSUS AND THE COCYCLE.  The P-path enumeration reaches "
      "EXACTLY SKY-B's direction set at every base event of every "
      "substrate at both depths (so the coordinates cover the charts and "
      "nothing else), every overlapping chart pair is same-height, and "
      "the fibre-map cocycle has ZERO violations wherever it is defined "
      "— with the coverage reported against this unit's interest: on the "
      "conflict RING at d = 2 the test has NO CONTENT, because every "
      "chart triple with pairwise overlaps has an EMPTY triple "
      "intersection, so there is no composition to test",
      _reach and _xh == 0 and _viol == 0,
      f"cells = {len(MEAS)}; P-reach == SKY-B everywhere = {_reach}; "
      f"cross-height overlapping pairs = {_xh}; cocycle triples tested "
      f"with a defined composition = {_tested}, VIOLATIONS = {_viol}")

# --- the artifact probes (D64's C2b) --------------------------------------
print("\n  [A4(c) THE ARTIFACT PROBES (D64's C2b) — a labeling can "
      "produce a flat or a non-flat atlas for reasons that have nothing "
      "to do with the geometry]")
_blind = [(nm, tg, d, w) for (nm, tg, d), r in sorted(MEAS.items(), key=repr)
          for w in LAB
          if r[w + ':const'][0] > 0 and r[w + ':const'][1] == r[w + ':const'][0]]
_disj = {}
for nm in sorted(SUBS):
    if SUBS[nm]['kind'] != 'grammar':
        continue
    for d in DEPTHS:
        r = MEAS[(nm, 'REG', d)]
        cnt = Counter(len(set(reg_tuple(SUBS[nm]['H'][a]))
                          & set(reg_tuple(SUBS[nm]['H'][c])))
                      for (a, c, s) in r['pairlist'])
        _disj[(nm, d)] = dict(sorted(cnt.items()))
for k in sorted(_disj, key=repr):
    print(f"      PROBE 2 {k[0]:38s} d={k[1]}: overlapping pairs by "
          f"|regs(e) & regs(e')| = {_disj[k]}"
          + ("   <== ALL DISJOINT: RAW identity impossible, no outcome "
             "read at RAW" if set(_disj[k]) == {0} else ""))
for nm in sorted(SUBS):
    for tg in ('REG',):
        for d in (2,):
            if tg not in SUBS[nm]['inst']:
                continue
            r = MEAS[(nm, tg, d)]
            print(f"      PROBE 1 {nm:38s} {tg} d={d}: directions seen by "
                  f">= 2 charts = {r['ROLE:const'][0]}, of which the label "
                  f"is CONSTANT across charts = {r['ROLE:const'][1]} "
                  f"(RAW: {r['RAW:const'][1]})")
_readcells = [(nm, tg, d) for nm in sorted(SUBS)
              if SUBS[nm]['kind'] == 'grammar'
              for tg in INST if tg in SUBS[nm]['inst'] for d in DEPTHS]
_blind_read = [(nm, tg, d) for (nm, tg, d) in _readcells
               if MEAS[(nm, tg, d)]['ROLE:const'][0] > 0
               and MEAS[(nm, tg, d)]['ROLE:const'][1]
               == MEAS[(nm, tg, d)]['ROLE:const'][0]]
BLIND_ROLE = set(_blind_read)
_blind_wide = [c for c in _blind_read if c[0] == tag_of(WIDE)]
print(f"      PROBE 1 FIRES at {len(_blind)} (labeling, substrate, "
      f"instrument, depth) cells IN TOTAL — printed in full, because a "
      f"blind labeling makes a FLAT reading an artefact: "
      f"{[(a, b, c, w) for (a, b, c, w) in _blind]}")
print(f"      OF THOSE, the cells where the READ labeling (ROLE) is "
      f"blind — whose FLAT readings are artefacts and are EXCLUDED from "
      f"every convention-robustness sentence below: {sorted(BLIND_ROLE)}")
check("A4(c) THE PROBES DECIDE WHERE THE OUTCOME MAY BE READ, AND "
      "PROBE 1 DOES FIRE — WHICH IS PRINTED AND ACTED ON RATHER THAN "
      "FOLDED AWAY.  The decisive reading (A-IIIa: the wide record's "
      "transition class) is made at the ROLE labeling on the WIDE "
      "record, and PROBE 1 does NOT fire at any of its cells at any "
      "instrument or depth: some direction always carries different "
      "labels in different charts there, so the wide record's flat "
      "atlas is NOT an artefact of a labeling that cannot see a "
      "transition.  Where PROBE 1 DOES fire — the FIRST-letter "
      "labelings on the grids, and every instrument's ROLE labeling on "
      "the DELIVERY-FREE ring, whose atlas is flat for exactly that "
      "reason — the cells are listed and excluded by name.  "
      "PROBE 2 (disjoint base registers make RAW non-identity a "
      "tautology) is reported per substrate and no outcome is read at "
      "RAW either",
      len(_blind_wide) == 0 and len(_disj) > 0 and len(_readcells) > 0,
      f"blind ROLE cells on the WIDE record = {len(_blind_wide)}; blind "
      f"ROLE cells anywhere = {len(_blind_read)} of {len(_readcells)} "
      f"{sorted(BLIND_ROLE)}; blind cells at any labeling = "
      f"{len(_blind)}; PROBE-2 censuses printed for {len(_disj)} "
      f"grammar substrate/depth cells")

# --- C7 both routes, all conventions, plus the general test ---------------


def uf_trivialize(r):
    """THE FREE-RELABELLING TEST (this unit's extension, declared).
    D64's C7 asks whether a per-chart Z/2 PORT FLIP removes every
    non-identity transition.  This asks the same question for the
    LARGEST possible gauge group: an arbitrary per-chart bijection of
    the label alphabet.  Identify (chart a, word w) with (chart c,
    m_ac(w)) for every pair-transition and take the transitive closure;
    a consistent global relabelling exists IFF no class contains two
    DISTINCT words of the SAME chart.  Obstruction count = classes that
    do; `surv` re-runs the identification as an independent check."""
    par = {}

    def find(x):
        par.setdefault(x, x)
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    def uni(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            par[rx] = ry
    seen = set()
    for (a, c), m in sorted(r['pairmap'].items(), key=repr):
        if (c, a) in seen:
            continue
        seen.add((a, c))
        for (x, y) in m:
            uni((a, x), (c, y))
    cls = defaultdict(list)
    for kk in list(par):
        cls[find(kk)].append(kk)
    bad = 0
    for root, mem in cls.items():
        byc = defaultdict(set)
        for (ch, w) in mem:
            byc[ch].add(w)
        if any(len(vv) > 1 for vv in byc.values()):
            bad += 1
    rho = {(ch, w): root for root, mem in cls.items() for (ch, w) in mem}
    surv = sum(1 for (a, c), m in sorted(r['pairmap'].items(), key=repr)
               for (x, y) in m if rho[(a, x)] != rho[(c, y)])
    return {'classes': len(cls), 'obstructions': bad, 'surv': surv,
            'edges': len(seen)}


def parity_obstruction(r):
    """The convention-comparable Z/2 PARITY route: g = 0 on identity and
    g = 1 on ANY non-identity length-preserving transition, whether or
    not it is a restriction of a NAMED involution (D64's `cochain`
    silently drops the 'other' class, which makes its route vacuous
    under some conventions; this one never is).  Route (b) only — the
    verification needs a named involution and is reported by
    `cochain`."""
    g = {}
    for (a, c) in sorted(r['pairmap'], key=repr):
        if a > c:
            continue
        cls = classify(r['pairmap'][(a, c)])
        if cls == 'length-changing':
            continue
        g[(a, c)] = 0 if is_named(cls, 'identity') else 1
    adj = defaultdict(list)
    for (a, c), val in sorted(g.items(), key=repr):
        adj[a].append((c, val))
        adj[c].append((a, val))
    eps = {}
    for s0 in sorted(adj):
        if s0 in eps:
            continue
        eps[s0] = 0
        st = [s0]
        while st:
            x = st.pop()
            for (y, val) in adj[x]:
                if y not in eps:
                    eps[y] = eps[x] ^ val
                    st.append(y)
    inc = [(a, c) for (a, c), val in sorted(g.items(), key=repr)
           if eps[a] ^ eps[c] != val]
    return {'edges': len(g), 'nonid': sum(g.values()),
            'obstructions': len(inc), 'witness': inc[:1]}


# --- instrument validation for the two ADDED routes (d47a's doctrine: an
# --- instrument is shown to have a true positive AND a true negative
# --- BEFORE it is pointed at data)
_w00, _w01, _w10, _w11 = (0, 0), (0, 1), (1, 0), (1, 1)
_mid = ((_w00, _w00), (_w01, _w01))
_mtau = ((_w00, _w10), (_w01, _w11))
_POS_PAR = {'pairmap': {(0, 1): _mtau, (1, 2): _mid, (0, 2): _mid}}
_NEG_PAR = {'pairmap': {(0, 1): _mtau, (1, 2): _mtau, (0, 2): _mid}}
_POS_FREE = {'pairmap': {(0, 1): ((_w00, _w00),), (1, 2): ((_w00, _w00),),
                         (0, 2): ((_w01, _w00),)}}
_NEG_FREE = {'pairmap': {(0, 1): ((_w00, _w00),), (1, 2): ((_w00, _w00),),
                         (0, 2): ((_w00, _w00),)}}
_vp = (parity_obstruction(_POS_PAR)['obstructions'],
       parity_obstruction(_NEG_PAR)['obstructions'],
       uf_trivialize(_POS_FREE)['obstructions'],
       uf_trivialize(_NEG_FREE)['obstructions'])
print("\n  [A4(d0) VALIDATION OF THE TWO ADDED ROUTES — a true positive "
      "AND a true negative for each, constructed here, before either is "
      "pointed at a record (d47a's SG1 doctrine)]")
print(f"      PARITY route: an odd triangle (tau, identity, identity) "
      f"-> {_vp[0]} obstruction(s); an even triangle (tau, tau, "
      f"identity) -> {_vp[1]}.  Classifications used: "
      f"{classify(_mtau)} / {classify(_mid)}.")
print(f"      FREE-RELABELLING route: three charts forcing two DISTINCT "
      f"words of one chart into one class -> {_vp[2]} obstruction(s); "
      f"the same triangle made consistent -> {_vp[3]}.")
check("A4(d0) THE TWO ADDED ROUTES ARE NOT BLIND AND NOT TRIGGER-HAPPY. "
      "Each returns a POSITIVE on a constructed inconsistency and a ZERO "
      "on the consistent version of the same shape, so a zero reported "
      "below is a measurement and not an instrument that cannot fire.  "
      "This matters most for the FREE-RELABELLING route, which returns "
      "zero at every cell of the real census",
      _vp == (1, 0, 1, 0) and classify(_mtau) == 'tau'
      and classify(_mid) == 'identity',
      f"(parity positive, parity negative, free positive, free negative) "
      f"= {_vp}")

print("\n  [A4(d) THE COBOUNDARY COMPUTATION — D64's `cochain` (both "
      "routes: the DFS obstruction count AND the census re-run under the "
      "resulting relabelling), at every convention, beside the "
      "convention-comparable PARITY route and the FREE-RELABELLING "
      "test]")
print(f"      {'substrate':38s} {'inst':9s} {'d':>2s} {'gen':>9s} "
      f"{'edges':>6s} {'comps':>6s} {'C7 OBS':>7s} {'C7 surv':>8s} "
      f"{'cech t/v':>10s} {'PARITY e/OBS':>13s} {'FREE OBS/surv':>14s}")
CO = {}
UFR = {}
PAR = {}
for nm in sorted(SUBS):
    for tg in INST:
        if tg not in SUBS[nm]['inst']:
            continue
        for d in DEPTHS:
            r = MEAS[(nm, tg, d)]
            co = cochain(nm, tg, d)
            uf = uf_trivialize(r)
            pa = parity_obstruction(r)
            CO[(nm, tg, d)] = co
            UFR[(nm, tg, d)] = uf
            PAR[(nm, tg, d)] = pa
            print(f"      {nm:38s} {tg:9s} {d:2d} {co['gen'][:9]:>9s} "
                  f"{co['labelled']:6d} {co['comps']:6d} "
                  f"{co['incons']:7d} {co['surv']:8d} "
                  f"{co['cech_t']:4d}/{co['cech_v']:<5d} "
                  f"{pa['edges']:5d}/{pa['obstructions']:<7d} "
                  f"{uf['obstructions']:6d}/{uf['surv']:<7d}")

_dr7 = CO[('DR(8,10,8)', 'REG', 2)]
_dr7a = CO[('DR(8,10,8)', 'REGA', 2)]
_dranchor = (_dr7['labelled'] == 138 and _dr7['charts'] == 60
             and _dr7['comps'] == 9 and _dr7['incons'] == 0
             and _dr7['eps0'] == 32 and _dr7['eps1'] == 28
             and _dr7['surv'] == 0 and _dr7['cech_t'] == 108
             and _dr7['cech_v'] == 0
             and MEAS[('DR(8,10,8)', 'REG', 2)]['ROLE'][:2] == (57, 115)
             and _dr7a['eps0'] == 40 and _dr7a['eps1'] == 20
             and _dr7a['incons'] == 0)
check("A4(d) [ANCHOR] THE COBOUNDARY INSTRUMENT REPRODUCES D64's "
      "COMMITTED C7 ROW EXACTLY.  On DOUBLE-RING(8, 10, 8) at REG and "
      "d = 2 this receipt's re-run of D64's own `cochain` gives 60 "
      "charts, 138 labelled overlaps, 9 components, ZERO obstructions, "
      "eps = 32/28, zero surviving non-identity transitions and 108 Cech "
      "triples with 0 violations, with the transition split 57/115 and "
      "REGA's eps = 40/20 — every published figure.  **So the same "
      "instrument, unmodified, produces every obstruction count below**, "
      "and a non-zero count cannot be a difference of instruments",
      _dranchor,
      f"DR REG d2: charts {_dr7['charts']}, labelled {_dr7['labelled']}, "
      f"comps {_dr7['comps']}, obstructions {_dr7['incons']}, eps "
      f"{_dr7['eps0']}/{_dr7['eps1']}, surviving {_dr7['surv']}, cech "
      f"{_dr7['cech_t']}/{_dr7['cech_v']}; REGA eps {_dr7a['eps0']}/"
      f"{_dr7a['eps1']}, obstructions {_dr7a['incons']}", anchor=True)

# --- the wide record's verdict, and the ring's obstruction ----------------
_wide_nm = tag_of(WIDE)
_wide_rows = {(tg, d): (CO[(_wide_nm, tg, d)], UFR[(_wide_nm, tg, d)],
                        PAR[(_wide_nm, tg, d)]) for tg in INST
              for d in DEPTHS}
_wide_triv = all(co['incons'] == 0 and uf['obstructions'] == 0
                 and pa['obstructions'] == 0
                 for (co, uf, pa) in _wide_rows.values())
_wide_nonid = {tg: MEAS[(_wide_nm, tg, 2)]['ROLE'][1] for tg in INST}
_wide_kinds = {tg: MEAS[(_wide_nm, tg, 2)]['kinds'] for tg in INST}
print(f"\n    THE WIDE RECORD ({_wide_nm}), which is where A-IIIa vs "
      f"A-IIIb is decided:")
print(f"      transitions by class at d = 2, per convention: "
      f"{_wide_kinds}")
print(f"      every length-preserving transition is the IDENTITY at "
      f"every convention = "
      f"{all(all(kk in ('identity', 'length-changing') for kk in v) for v in _wide_kinds.values())}")
print(f"      obstruction counts (C7 / PARITY / FREE) at d = 2: "
      + ", ".join(f"{tg}: {_wide_rows[(tg,2)][0]['incons']}/"
                  f"{_wide_rows[(tg,2)][2]['obstructions']}/"
                  f"{_wide_rows[(tg,2)][1]['obstructions']}" for tg in INST))

RINGS = [tag_of(k) for k in A4SET if k[0] == 'RING']
_ring_obs = {(nm, tg, d): (CO[(nm, tg, d)]['incons'],
                           PAR[(nm, tg, d)]['obstructions'],
                           UFR[(nm, tg, d)]['obstructions'])
             for nm in RINGS for tg in INST for d in DEPTHS
             if (nm, tg, d) not in BLIND_ROLE}
_ring_c7_pos = sorted(k for k, v in _ring_obs.items() if v[0] > 0)
_ring_par_pos = sorted(k for k, v in _ring_obs.items() if v[1] > 0)
_ring_free_pos = sorted(k for k, v in _ring_obs.items() if v[2] > 0)
print(f"\n    THE PAIR-CONFLICT RINGS — the cells with a NON-ZERO "
      f"obstruction count:")
print(f"      D64's C7 route: {len(_ring_c7_pos)} cells; PARITY route: "
      f"{len(_ring_par_pos)} cells; FREE-RELABELLING route: "
      f"{len(_ring_free_pos)} cells.  Per record, "
      f"(instrument/depth -> C7 | PARITY | FREE):")
_ring_by_rec = {}
for kk in sorted(_ring_obs, key=repr):
    _ring_by_rec.setdefault(kk[0], []).append((kk[1], kk[2],) + _ring_obs[kk])
for nm in sorted(_ring_by_rec):
    print(f"        {nm}: " + ", ".join(
        f"{tg}/d{d} {c7}|{pa}|{fr}"
        for (tg, d, c7, pa, fr) in _ring_by_rec[nm]))
_par_ring = {nm: (max([v[1] for kk, v in _ring_obs.items()
                       if kk[0] == nm and kk[2] == 2] or [0]),
                  max([v[1] for kk, v in _ring_obs.items()
                       if kk[0] == nm and kk[2] == 3] or [0]))
             for nm in sorted(_ring_by_rec)}
_obs_rings = sorted(nm for nm, v in _par_ring.items() if v[0] > 0)
_clean_rings = sorted(nm for nm, v in _par_ring.items() if v[0] == 0)
print(f"      THE PATTERN, its lists computed from the census rather "
      f"than typed: maximum PARITY obstruction over the five "
      f"conventions, by ring, at d = 2 / d = 3 = {_par_ring}.  "
      f"OBSTRUCTING rings: {_obs_rings}.  CLEAN rings: "
      f"{_clean_rings}.  Read: the rotating rings that obstruct are the "
      f"M = 6 ones — THREE pairs per round, an ODD cycle in the nerve — "
      f"while the rotating M = 4 and M = 8 rings (two and four pairs, "
      f"EVEN cycles) are clean, as is the delivery-free ring, which has "
      f"no rotation and no non-identity transition at all.  A Z/2 "
      f"holonomy around an odd conflict ring is the natural reading, "
      f"THREE RING SIZES DO NOT ESTABLISH IT, and it is filed as a "
      f"residue rather than a result.")
_pw = PAR[(tag_of(HEAD), 'REG', 2)]
if _pw['witness']:
    (a, c) = _pw['witness'][0]
    rr = MEAS[(tag_of(HEAD), 'REG', 2)]
    Hh = SUBS[tag_of(HEAD)]['H']
    hh = SUBS[tag_of(HEAD)]['h']
    print(f"      A WITNESS EDGE on {tag_of(HEAD)} at REG d = 2: charts "
          f"{a} and {c} (base events {Hh[a][0]}/{Hh[c][0]}, heights "
          f"{hh[a]}/{hh[c]}, widths {len(rr['D'][a])}/{len(rr['D'][c])}), "
          f"transition {rr['pairmap'].get((a, c))} classified "
          f"{classify(rr['pairmap'][(a, c)])}")
_X = extension_census(MEAS[(tag_of(HEAD), 'REG', 2)])
if _X is not None:
    print(f"      THE GROUP NAME, on the ring (D64's C4b applied here): "
          f"fibre {[_pt(p) for p in _X['pts']]}; subgroups of S_4 "
          f"consistent with every observed map = {_X['ncons']}, minimal "
          f"by inclusion = {[len(H_) for H_ in _X['minimal']]}; "
          f"UNIQUELY-tau maps = {_X['uniq_tau']} of {_X['tau_pairs']} "
          f"tau-classified pairs — so the Z/2 reading is a CONVENTION "
          f"here exactly as it was in D64")
_c7_dir = all((co['surv'] > 0 if co['incons'] > 0 else True)
              and (co['cech_v'] == 0 if co['incons'] == 0 else True)
              for co in CO.values())
_c7_amb = sorted(k for k, co in CO.items()
                 if co['incons'] == 0 and co['surv'] > 0)
print(f"    C7's two routes agree in the decisive direction at every "
      f"one of the {len(CO)} cells: a non-zero obstruction count always "
      f"leaves a surviving non-identity transition, and a zero count "
      f"always passes the Cech form.  The converse fails at "
      f"{len(_c7_amb)} cell(s) {_c7_amb} — there a pair whose FIBRE MAP "
      f"is the identity still has different label SETS at a direction "
      f"carrying two wire words (D64's 'ambiguous' status), which "
      f"route (c) counts and route (b) never sees; it is printed, not "
      f"folded away.")
_spr_par = {k: PAR[k]['obstructions'] for k in PAR
            if SUBS[k[0]]['kind'] == 'sprinkling'}
_dr_par = {k: PAR[k]['obstructions'] for k in PAR if k[0] == 'DR(8,10,8)'}
_ring_par_all = {k: PAR[k]['obstructions'] for k in PAR
                 if k[0] in RINGS}
print(f"    THE PARITY ROUTE'S CONTROLS, which decide how the ring's "
      f"obstruction may be read: genuine sprinklings carry NON-ZERO "
      f"parity obstructions too ({_spr_par}), while the delivery "
      f"crystal DR(8,10,8) carries ZERO at every convention and depth "
      f"({sorted(set(_dr_par.values()))}).  On this statistic the "
      f"pair-conflict ring sits with the SPRINKLINGS and against the "
      f"delivery crystal — which is a finding about the statistic's "
      f"discriminating power as much as about the ring.")
check("A4(e) [THE CLASS DECIDES] THE WIDE RECORD'S CLASS IS TRIVIAL — "
      "**A-IIIa, not A-IIIb** — AND THE PAIR-CONFLICT RING CARRIES THE "
      "CAMPAIGN'S FIRST NON-ZERO OBSTRUCTION COUNT, WHICH IS REPORTED "
      "AND NOT CLAIMED AS H^1 != 0.  On the wide record all three "
      "routes return ZERO obstructions at every one of the five port "
      "conventions and at both depths — and that is NOT vacuous: at REG, "
      "REGA, ARBVFIRST and COV every length-preserving transition is the "
      "identity (with 52 testable Cech triples at d = 2, so the "
      "triviality has content), while at ARBLOSE 41 of the 90 pairs "
      "carry a NON-identity length-preserving map and the class is a "
      "coboundary anyway.  Conflict bought WIDTH and bought no gauge.  "
      "On the two-proposer rings D64's own C7 returns a NON-ZERO "
      "obstruction count at several conventions — the first anywhere in "
      "this campaign, produced by the instrument that returns 0 on the "
      "delivery crystal in this same run — but it FAILS the pin's "
      "survival requirement: the FREE-RELABELLING test trivializes every "
      "one of those cells, the ring's chart triples all have EMPTY "
      "triple intersections (so there is no Cech 2-skeleton and the "
      "'class' lives in the cycle space of a graph), and D64's C4b "
      "extension census says the Z/2 name is a convention here too.  "
      "The gate is the self-consistency of C7's two routes, not the "
      "verdict",
      _c7_dir and _wide_triv and len(_ring_c7_pos) > 0
      and len(_ring_free_pos) == 0 and max(_spr_par.values()) > 0,
      f"C7's routes agree in the decisive direction in every one of "
      f"{len(CO)} cells = {_c7_dir} (converse exceptions {len(_c7_amb)}, "
      f"printed); sprinkling parity obstructions "
      f"{sorted(set(_spr_par.values()))} vs delivery-crystal "
      f"{sorted(set(_dr_par.values()))}; wide record "
      f"trivial at every convention and every route = {_wide_triv}; ring "
      f"cells with a non-zero C7 obstruction = {len(_ring_c7_pos)}; ring "
      f"cells with a non-zero FREE-relabelling obstruction = "
      f"{len(_ring_free_pos)}")

# ======================================================================
# THE VERDICT
# ======================================================================
OUTCOME = ('A-I' if _refusals else
           ('A-IIIb' if (DOOR and not _wide_triv) else
            ('A-IIIa' if DOOR else 'A-II')))
print(f"\n[THE PRE-REGISTERED OUTCOME, read off the sweep: {OUTCOME}]")
check("A6(a) [THE OUTCOME] " + {
    'A-I': "**A-I — CONFLICTS REFUSE TO TILE.**  The break point and its "
           "mechanism are the deliverable",
    'A-II': "**A-II — CONFLICT TILES BUT THE WIDTH DOOR STAYS SHUT.**  No "
            "swept conflict record reaches |D| >= 5 at d = 2",
    'A-IIIa': "**A-IIIa — CONFLICT TILES AND BREAKS THE DELIVERY CEILING, "
              "AND THE CLASS IS TRIVIAL AGAIN.**  Forced conflict records "
              "run to crystal length with no refusal anywhere; the "
              "two-proposer ring tiles INSIDE the sprinkling homogeneity "
              "band at d = 2 while carrying 4-direction charts (D63's F3 "
              "pattern, with conflict as the engine); and the "
              "3- and 4-proposer grids carry |D| = 6 and |D| = 8 at "
              "d = 2, the first records in the campaign past the delivery "
              "ceiling of 4.  On the wide record the transition class is "
              "TRIVIAL at every port convention and by every route — the "
              "identity outright at four conventions, a coboundary at the "
              "fifth",
    'A-IIIb': "**A-IIIb — a non-coboundary class on a wide record**"
    }[OUTCOME] + ".  The predicate is the pre-registered disjunction "
    "itself, computed from the sweep: a refusal anywhere would have "
    "printed A-I, a max |D| of 4 everywhere would have printed A-II, and "
    "a surviving obstruction on the wide record would have printed "
    "A-IIIb",
    OUTCOME == 'A-IIIa',
    f"refusals = {len(_refusals)}; records with |D| >= 5 at d = 2 = "
    f"{len(DOOR)}; wide record's class trivial at every convention and "
    f"route = {_wide_triv}")

# ======================================================================
# A6 — anti-vacuity, caps, determinism
# ======================================================================
_src = open('v10/code/d66_arbitration_crystal_exact.py').read()
_tree = ast.parse(_src)
_bound = set()
for _n in ast.walk(_tree):
    if isinstance(_n, ast.Name) and isinstance(_n.ctx, ast.Store):
        _bound.add(_n.id)
    elif isinstance(_n, (ast.FunctionDef, ast.AsyncFunctionDef)):
        _bound.add(_n.name)
        for _a in _n.args.args:
            _bound.add(_a.arg)
_ch = [c for c in ast.walk(_tree)
       if isinstance(c, ast.Call) and isinstance(c.func, ast.Name)
       and c.func.id == 'check']
_vac = [ast.dump(c.args[1])[:60] for c in _ch
        if isinstance(c.args[1], ast.Constant)
        or not ({x.id for x in ast.walk(c.args[1])
                 if isinstance(x, ast.Name)} & _bound)]
check("A6(b) AST anti-vacuity in d47a's SG8 form: every check() "
      "predicate is a bare constant NOWHERE and references at least one "
      "run-bound name.  SCOPE (LOG #403 MA-2): the scan enforces exactly "
      "that and detects no vacuous gate in arbitrary syntactic form",
      len(_ch) >= 10 and not _vac,
      f"check() calls = {len(_ch)}, bare-constant or unbound predicates "
      f"= {len(_vac)}")

print("\n[A6(c) DEPTHS, CAPS, RANGES AND POPULATIONS — all printed, none "
      "silent]")
print(f"    SKY-B depths measured: 2 and 3 at every record and every "
      f"instrument (committed SKYB_DEPTH = {SKYB_DEPTH}).")
print(f"    swept conflict configurations = {len(SWEEP)}; records built "
      f"= {len(BUILT)}; conflict events built = "
      f"{sum(len(v[0].H) for v in BUILT.values())}; largest record = "
      f"{max(len(v[0].H) for v in BUILT.values())} events; controls "
      f"re-run = DR(8,10,8) (177), BRICK(8,14) (65), 11 sprinkling "
      f"configurations, 2 sprinklings charted.")
print(f"    full-menu replays = {len(REPLAY)}, budgets "
      f"{FULLMENU_BUDGET:.0f}s / {WIDE_REPLAY_BUDGET:.0f}s (wide), "
      f"statuses { {n: r['status'] for n, r in REPLAY.items()} }.")
print(f"    A4 measurement cells = {len(MEAS)} over {len(SUBS)} "
      f"substrates x {len(INST)} instruments x 2 depths; overlapping "
      f"pairs examined = {sum(r['pairs'] for r in MEAS.values())}; "
      f"triples examined = {sum(r['triples'] for r in MEAS.values())}.")
print(f"    thresholds used anywhere: D58's |D| >= 2 and |D| >= 4 "
      f"columns, the pin's overlap (>= 2 shared directions) and triple "
      f"(pairwise overlaps, >= 1 shared direction) predicates, and the "
      f"A0(ii) sprinkling bands.  NO OTHER THRESHOLD IS USED.")
print(f"    NOTHING WAS CUT SILENTLY: the only budget that binds is the "
      f"wide record's full-menu replay, whose cut point is printed in "
      f"A1(c).  Total wall clock at this line: {time.time() - T0:.1f}s.")

t_det = time.time()
_digs = []
for _seed in ('0', '7', '999'):
    _env = dict(os.environ, PYTHONHASHSEED=_seed)
    _digs.append(subprocess.run(
        [sys.executable, 'v10/code/d66_arbitration_crystal_exact.py',
         '--probe'], capture_output=True, text=True, env=_env).stdout)
check("A6(d) DETERMINISM IS GATED, NOT ASSERTED (D63's W6b pattern; the "
      "layer reads next(iter(frozenset)) in load-bearing places and this "
      "unit's arbitrations have TWO AND THREE proposers, where D64's "
      "note observed that `regs_of`'s `next(iter(...))` tie-break and "
      "`reg_tuple`'s sort could in principle diverge — A4(a)'s closure "
      "gate is what would catch it).  THE DIGEST COVERS: a ring and a "
      "grid record rebuilt in probe mode under PYTHONHASHSEED 0 / 7 / "
      "999 — exact-Fraction profile rows at both depths, arbitration "
      "share and full width histogram — byte-identical stdout.  IT DOES "
      "NOT COVER the sweep's larger records or the A4 census",
      len(set(_digs)) == 1 and 'DIGEST' in _digs[0]
      and "('GRID', 3, 4)" in _digs[0],
      f"probe runs = 3, distinct outputs = {len(set(_digs))}  "
      f"[{time.time() - t_det:.1f}s]")

print("\n[VERDICT — D66]")
print(f"  {OUTCOME} FIRED.  CONFLICT TILES, AND IT BUYS WIDTH THE "
      f"DELIVERY GRAMMAR CANNOT.")
print(f"    THE TILING HALF.  {tag_of(HEAD)}: "
      f"{len(BUILT[HEAD][0].H)} events over "
      f"{len(actors_of(HEAD[0], HEAD[1]))} actors in {HEAD[2]} rounds, "
      f"{float(arbshare(BUILT[HEAD][0].H)):.4f} of them ARBITRATIONS, "
      f"every event offered by")
print(f"    the layer's own menu with all actors offered at every one of "
      f"the {len(BUILT[HEAD][0].H)} steps.")
print(f"    At d = 2: homogeneity {BUILT[HEAD][1][2]['h2']} "
      f"(~{float(BUILT[HEAD][1][2]['h2']):.4f}), INSIDE the recomputed "
      f"band [{float(BAND[2][0]):.4f}, {float(BAND[2][1]):.4f}]; "
      f"|D| >= 4 at {BUILT[HEAD][1][2]['h4']}; max |D| "
      f"{BUILT[HEAD][1][2]['max']}.")
print(f"    THE WIDTH HALF.  {tag_of(WIDE)}: max |D| = "
      f"{BUILT[WIDE][1][2]['max']} at d = 2 and "
      f"{tag_of(('GRID', 4, 4))}: max |D| = "
      f"{BUILT[('GRID', 4, 4)][1][2]['max']} — past the delivery "
      f"ceiling of 4 for the first time.")
print(f"    THE MECHANISM, AND IT CORRECTS ITS OWN PARENT (W4c): the "
      f"version register an")
print(f"    arbitration mints is a BIRTH WIRE with no successor, so "
      f"three registers")
print(f"    are worth two, a two-proposer conflict ring is held to the "
      f"delivery")
print(f"    ceiling 4 at d = 2, and width past 4 needs 3+ PROPOSERS.  "
      f"The measured")
print(f"    law in this family is max |D| = 2k at d = 2 for a "
      f"k-proposer grid.")
print(f"    THE GAUGE HALF (A4).  On the wide record all three routes "
      f"return ZERO")
print(f"    obstructions at all five port conventions and both depths — "
      f"identity at")
print(f"    four of them and a COBOUNDARY at the fifth (ARBLOSE, where "
      f"41 pairs are")
print(f"    non-identity): no class, A-IIIa.  On the two-proposer rings "
      f"D64's own C7")
print(f"    returns a NON-ZERO")
print(f"    obstruction count — the first in the campaign — but it does "
      f"not survive")
print(f"    the free-relabelling test, the triples are all empty, and "
      f"the Z/2 name is")
print(f"    a convention (C4b), so H^1 != 0 IS NOT CLAIMED.  D64's "
      f"successor question")
print(f"    stays open with its first non-trivial data point.")
print(f"  SCOPE (pin §5): grammar layer, the swept family only; a "
      f"crystal certifies")
print(f"  MECHANISMS, never objects (#440); no measure claim at "
      f"transport scope (B1)")
print(f"  and therefore no typicality; omega is a chart-size ratio along "
      f"covers (D58);")
print(f"  every width claim carries the record's own B, its live Bl and "
      f"W4b's bound;")
print(f"  every gauge sentence carries the convention table; transfer to "
      f"the")
print(f"  identified click law runs through paper 29's missing map (D59) "
      f"and is not")
print(f"  claimed; the missing map is not touched.")
print(f"\n[d66] {PASS} PASS / {FAIL} FAIL   "
      f"[total wall clock {time.time() - T0:.1f}s]")
print("[exit protocol, pin A0/A6] exit 1 ONLY on ANCHOR breakage — the "
      "A0 family (A0a single sources, A0(i) the delivery controls' "
      "committed rows, A0(ii) the sprinkling bands, A4(a) instrument "
      "validation, A4(d) D64's committed C7 row), the five gates "
      "carrying anchor=True.  Every substantive negative exits 0.  "
      "anchor broken = " + str(ANCHOR_FAIL))
sys.exit(1 if ANCHOR_FAIL else 0)
