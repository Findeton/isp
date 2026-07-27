#!/usr/bin/env python3
"""
d67_k4_double_grid_exact.py — v10 D67: THE k = 4 DOUBLE GRID.
Pin: note-d67-k4-double-grid-pin.md (STRICT, FROZEN AND COMMITTED before
this file existed).  Parents: D66 (TERMINAL — the width ceiling is
k*b <= k^2, SATURATED at 9 by DOUBLE-GRID(3, R); crossed conflict is the
mechanism; the flagship is in-band at d = 3 with max |D| = 9), W4c (the
dead-wire theorem: width is bought by PROPOSER count, not register
count), and the committed instruments (d58 atlas, d47a sky, d64/d66 C7
coboundary, d55c sprinklings, d60/d63 blueprint machinery, d42b1 the
transport grammar).

THE QUESTION (pin §1).  The genuine sprinkling range is max |D| 10-17 at
d = 2.  A k = 4 double grid bounds at k^2 = 16 — INSIDE that range for
the first time.  Does the crossed-conflict mechanism reach
SPRINKLING-GRADE WIDTH, and can it stay band-uniform while doing it?

THE DESIGN PROBLEM (pin §2), and the four schedules this unit tried.
A 4-proposer arbitration needs FOUR live proposals on one shared base.
On a 4 x 4 actor grid, row r's four actors must all hold the row base
and column c's four actors must all hold the column base; the minted
version goes to ALL FOUR proposers (d42b1 `View.holdings`), so a group
that arbitrates together needs no re-supply.  What costs deliveries is
ROTATION.  The four schedules, all built, all reported:

  V1  DOUBLE-GRID(g, R) [MINTS-FIRST, PHASE-SEPARATED] — D66's own
      committed blueprint, generalized to g = 4 by this unit's
      `dgrid(g, R, order, boot)` and GATED to reproduce d66's
      `double_grid(3, R)` EVENT FOR EVENT.  2g independent base lineages
      are minted once (each seed alone, from genesis) and spread by
      2g(g-1) bootstrap deliveries; thereafter every round is 2g^2
      proposals, then the g ROW arbitrations, then the g COLUMN
      arbitrations, and ZERO deliveries.  Every actor holds TWO live
      proposals on TWO distinct unsuperseded bases —
      `prop_options_in_view` blocks only a second live proposal on the
      SAME base — which is the two-base holding pattern the k = 4
      rotation would otherwise have to buy with deliveries.
  V2  SHARED-BASE(g) — the one-lineage design: mint ONE version, spread
      it to all g^2 actors, then let rows and columns conflict on THAT
      base.  It REFUSES at the second proposal of the first actor, and
      the refusal is the mechanism that FORCES V1's mints-first
      bootstrap: an actor may not hold two live proposals on one base.
  V3  CONFLICT-GRID(g, R) [ROTATION, DELIVERY-SUPPLIED] — D66's own
      committed rotating blueprint: rounds alternate ROW and COLUMN
      groups on ONE lineage per actor, and each group is re-supplied by
      g - 1 deliveries per round.  It forces, and it is the delivery
      corner Bl = 2 of the width law: max |D| = 2k.
  V4  DOUBLE-GRID(g, R, order = 'inter') — the same objects as V1 with
      the arbitration order INTERLEAVED (row 0, column 0, row 1, column
      1, ...) instead of phase-separated.  It forces and it COLLAPSES
      the width, which is what identifies the phase separation (not the
      concurrency alone) as the load-bearing part of the schedule.

  ARBCHAIN*(m, k) — this unit's corrected smallest witness.  One
      k-proposer arbitration whose k proposer registers are consumed by
      m further K-PROPOSER arbitrations and by k - m deliveries.  D66's
      own `arbchain(m, k)` hardcodes THREE proposers in its secondary
      arbitrations (its gate only ever ran k = 3), so it realizes
      3m + 2(k - m), not the k*m + 2(k - m) its docstring claims for
      general k.  Both are built and both are measured here; the
      correction is reported in K3, and at k = 3 the two agree exactly.

ROUND-1 REPAIRS (v10/reviews/d67-round1-hostile-review.md; 1 BLOCKER /
5 MAJOR / 7 MINOR / 4 NIT).  THREE OBJECTS IN THIS RECEIPT WERE BUILT BY
THE ROUND-1 REFEREE AND ARE CARRIED HERE WITH CREDIT (house style: a
round-supplied construction is named as such and then gated like any
other):

  DOUBLE-GRID(4, 4) [BLOCKER 1] — one more round than the first
      version's sweep could afford.  It REFUTES the first version's
      flagship negative: a WHOLE k = 4 record is inside the d = 3
      sprinkling homogeneity band, on BOTH published band columns,
      while carrying max |D| = 16 = k^2.  The width-uniformity frontier
      at k = 4 does not exist.
  ARBCHAIN**(k) [MAJOR 1] — ARBCHAIN*(k, k) with every actor register
      HEIGHT-LEVELLED by the grammar's own ('n', a) idle event before
      the proposals, so that all k depth-1 consumers sit at exactly
      height + 1.  It realizes |D_e(2)| = k^2 at k = 3, 4, 5 AND 6.  The
      first version's "the ceiling is not reached at k = 5" measured
      ARBCHAIN*'s bootstrap ORDERING, not a wall: height alignment is a
      DESIGN REQUIREMENT the grammar's own idles satisfy.
  LEVELLED-DGRID(4, 2) [NIT 2] — the same levelling pass applied to the
      DOUBLE-GRID bootstrap.  It closes the first version's residue 2:
      the fourth width-16 chart per round is recovered and homogeneity
      rises at both depths (interior d = 3 to 4/5).

THE R-PREFIX LEMMA (a runtime economy, gated not assumed).  `dgrid(g, R)`
appends round R to the record of round R - 1, so the R-round record is a
PREFIX of the R'-round record for every R < R'.  DOUBLE-GRID(4, 4) is
therefore built ONCE and (4, 1), (4, 2), (4, 3) are read off its
prefixes; the lemma is gated at g = 3, where BOTH records are built
independently and both are D66 anchors, and the derived g = 4 rows are
gated against the round-1 committed rows, every one of which the round-1
referee reproduced in an independent driver of his own.

PRE-REGISTERED OUTCOMES (pin §4), decided by the sweep:
  K-I    the 4-proposer schedule refuses to force — the break mechanism
         is the deliverable;
  K-II   forces, but max |D| stays below 10 — the gap between the k^2
         bound and realized width is the finding;
  K-III  max |D| >= 10 — SPRINKLING-GRADE WIDTH FROM PURE INTERACTION;
         K4 then decides whether uniformity survives and K5 whether the
         transition class is (again) trivial.

HOUSE RULES HELD: committed layers are SINGLE SOURCES (text-slice /AST
extraction, never re-implemented; exit-freedom of the slice and of every
extracted body GATED); exact Fractions where weights appear; no invented
thresholds (every band is the recomputed sprinkling band, every column
is D58's); no bare-constant predicates; both depths and both orderings
reported; every census printed in full; every width witness verified
EVENT BY EVENT against the committed `sky` and the committed order with
its P-paths printed (the D66-round standard); determinism gated by a
hash-seed probe; exit 0 for substantive negatives, exit 1 ONLY on ANCHOR
breakage (the K0 family plus the two instrument anchors).
Run from the repo root: python3 v10/code/d67_k4_double_grid_exact.py
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
    print("[D67 — THE k = 4 DOUBLE GRID: sprinkling-grade width, or the "
          "reason why not]")
    print("  banner: the objects below are FOUR-PROPOSER conflict "
          "crystals of the committed")
    print("  d42b1 layer.  Every event is offered by the layer's own "
          "menu and specified by")
    print("  its FULL EVENT TUPLE.  The sky (D47a), the atlas (D58), the "
          "sprinkling controls")
    print("  (D55c), D60/D63's blueprint machinery, D66's DOUBLE-GRID / "
          "CONFLICT-GRID /")
    print("  ARBCHAIN blueprints and D64's WHOLE cocycle instrument are "
          "imported as single")
    print("  sources and re-run in this process.  D66's committed "
          "DOUBLE-GRID(3, 2/4) rows")
    print("  and D64's committed C7 row are ANCHORS of this receipt.  "
          "K-I / K-II / K-III is")
    print("  decided by the sweep.")

# ======================================================================
# K0a — ANCHORS: every committed layer a single source
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
prop_options_in_view, own_view = nst['prop_options_in_view'], nst['own_view']

_EXITNAMES = ('exit', 'quit', '_exit')
_REFLECT = ('getattr', 'setattr', 'eval', 'exec', '__import__', 'compile',
            'vars', 'globals', 'locals')


def _no_exit(nodes):
    """No exit CALL and no bare NAME/ATTRIBUTE reference to an exit
    callable survives an extracted body.  SCOPE, said in the gate (D64
    C0a / D66 NIT 4): a syntactic scan for three names; it decides no
    reachability and cannot see an exit reached through getattr on a
    computed string.  ROUND-1 NIT 4 asked for that residual hole to be
    narrowed; `_reflect_defs` below is the widening."""
    for n in nodes:
        for c in ast.walk(n):
            if isinstance(c, ast.Attribute) and c.attr in _EXITNAMES:
                return False
            if isinstance(c, ast.Name) and c.id in _EXITNAMES:
                return False
    return True


def _reflect_defs(nodes):
    """ROUND-1 NIT 4, THE WIDENING.  The name scan cannot see an exit
    reached through `getattr(m, 'ex' + 'it')`.  So: find every top-level
    def/class in an extracted body that CONTAINS a reflective construct
    (getattr / setattr / eval / exec / __import__ / compile / vars /
    globals / locals) at all, and report it by name.  The gate is then
    checkable rather than declared: NONE of the names this unit BINDS
    AND CALLS may be one of them.  SCOPE, still said aloud: the scan is
    syntactic and per top-level body; a reflective construct reached
    through a helper a bound function calls at run time would not be
    seen — but every hit found here lives in the committed EXTRACTION
    helpers, which this unit never binds."""
    out = {}
    for n in nodes:
        if not isinstance(n, (ast.FunctionDef, ast.ClassDef)):
            continue
        c = sum(1 for x in ast.walk(n)
                if isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
                and x.func.id in _REFLECT)
        if c:
            out[n.name] = c
    return out


_EXTRACTED = {}


def _ext(path, marker, names=(), extra=None):
    """D60/D63/D64/D66's committed extraction idiom: keep only
    defs/classes (and the named module constants), so no module-level
    statement — print, gate, sys.exit — can run."""
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
measure, cochain = g64['measure'], g64['cochain']
extension_census = g64['extension_census']
_pt = g64['_pt']
LAB, DEPTHS = g64['LAB'], g64['DEPTHS']
g66 = _ext('v10/code/d66_arbitration_crystal_exact.py', 'd66', (),
           extra={'B': B, 'dl': dl, 'profile': profile, 'poset_of': poset_of,
                  'candidates_for': candidates_for, 'sky': sky,
                  'heights': heights, 'V0': V0, 'vname': vname,
                  'regs_of': regs_of, 'event_poset': event_poset,
                  'd58_covers': d58_covers, 'reg_tuple': reg_tuple,
                  'classify': classify, 'is_named': is_named})
d66_double_grid, d66_conflict_grid = g66['double_grid'], g66['conflict_grid']
d66_arbchain, _pick = g66['arbchain'], g66['_pick']
conflict_pair_group = g66['conflict_pair_group']
_skyB = g66['_skyB']
my_ord_tuple = g66['my_ord_tuple']
uf_trivialize, parity_obstruction = g66['uf_trivialize'], g66['parity_obstruction']
_c7_edges = g66['_c7_edges']
interior_of, full_menu_replay = g66['interior_of'], g66['full_menu_replay']
arbshare = g66['arbshare']

_slice_ast_ok = _no_exit(ast.parse(_slice).body)
_strip_ok = ('sys.exit' not in _slice and _slice_ast_ok
             and all(_no_exit(v) for v in _EXTRACTED.values()))
# ROUND-1 NIT 4 — the widening: every name this unit BINDS out of a
# committed module, against every top-level body in that module that
# contains a reflective construct at all.
_BOUND = {
    'v10/code/d47a_sky_instrument_exact.py':
        ('sky', 'heights', 'mink_order', 'lattice_points'),
    'v10/code/d55c_m31_control_exact.py': ('mink4', 'latt'),
    'v10/code/d58_atlas_instrument_exact.py': ('atlas', 'covers'),
    'v10/code/d60_crystal_exact.py':
        ('B', 'brick', 'mint_and_spread', 'dl', 'profile', 'poset_of',
         'show'),
    'v10/code/d63_wide_crystal_exact.py': ('double_ring', 'wide_brick'),
    'v10/code/d64_cocycle_exact.py':
        ('reg_tuple', 'ord_tuple', 'out_reg', 'out_cov', 'closure_of',
         'words_from', 'label', 'fibermap', 'classify', 'is_named',
         'measure', 'cochain', 'extension_census', '_pt'),
    'v10/code/d66_arbitration_crystal_exact.py':
        ('double_grid', 'conflict_grid', 'arbchain', '_pick', '_skyB',
         'my_ord_tuple', 'uf_trivialize', 'parity_obstruction',
         '_c7_edges', 'interior_of', 'full_menu_replay', 'arbshare',
         'conflict_pair_group')}
_REFL = {p: _reflect_defs(v) for p, v in _EXTRACTED.items()}
_refl_bound = {p: sorted(set(_REFL[p]) & set(_BOUND.get(p, ())))
               for p in _REFL if set(_REFL[p]) & set(_BOUND.get(p, ()))}
_slice_refl = _reflect_defs(ast.parse(_slice).body)
_refl_ok = not _refl_bound and not _slice_refl
if not PROBE:
    print("\n[K0a(ii) THE EXIT-SCAN WIDENING (round-1 NIT 4) — where the "
          "reflective constructs are, printed by name]")
    for p in sorted(_REFL):
        print(f"    {p.split('/')[-1]:38s} top-level bodies containing a "
              f"reflective construct: {dict(sorted(_REFL[p].items()))}; "
              f"of those, BOUND BY THIS UNIT: {_refl_bound.get(p, [])}")
    print(f"    the d42b1 text-slice: {_slice_refl}.  So every reflective "
          f"construct in this receipt's imported surface lives in a "
          f"committed EXTRACTION HELPER (the `_ext`/`_no_exit` idiom each "
          f"module carries), and this unit binds NONE of them: the "
          f"declared hole in the name scan is not merely disclosed, it is "
          f"EMPTY on the bodies actually called.")
if not PROBE:
    check("K0a [ANCHOR] EVERY LAYER A SINGLE SOURCE, AND THE STRIP IS "
          "GATED NOT ASSERTED.  The transport grammar by text-slice from "
          "committed d42b1 (cut at its own banner print); the sky "
          "(d47a), the repaired sprinkling generator (d55c), the atlas "
          "(d58), D60's blueprint machinery, D63's `double_ring` / "
          "`wide_brick`, D64's ENTIRE cocycle instrument and **D66's own "
          "`double_grid`, `conflict_grid`, `arbchain`, `_pick`, "
          "`_skyB`, `my_ord_tuple`, `uf_trivialize`, "
          "`parity_obstruction`, `_c7_edges`, `interior_of` and "
          "`full_menu_replay`** by AST extraction — this unit "
          "re-implements NO committed layer and NO committed "
          "instrument.  The gate reads: no reference to `exit`, `quit` "
          "or `_exit`, in CALL or bare NAME/ATTRIBUTE form, survives the "
          "slice (checked textually AND by AST) or any extracted body — "
          "AND (ROUND-1 NIT 4, THE WIDENING) no body this unit BINDS "
          "contains a reflective construct (getattr / setattr / eval / "
          "exec / __import__ / compile / vars / globals / locals) through "
          "which the name scan could be evaded.  SCOPE, still said "
          "aloud: both scans are syntactic and decide no reachability; "
          "what the widening buys is that the residual hole is EMPTY on "
          "the bodies actually called rather than merely declared",
          all(callable(f) for f in (candidates_for, sky, d58_atlas, latt,
                                    brick, profile, double_ring, measure,
                                    cochain, out_reg, d66_double_grid,
                                    d66_arbchain, _skyB, full_menu_replay))
          and _strip_ok and _refl_ok,
          f"slice = {_cut} of {len(_st)} chars, exit-free (text) = "
          f"{'sys.exit' not in _slice}, exit-free (AST) = {_slice_ast_ok}; "
          f"extracted bodies = "
          f"{ {p.split('/')[-1]: len(v) for p, v in _EXTRACTED.items()} }, "
          f"all exit-free = {all(_no_exit(v) for v in _EXTRACTED.values())}; "
          f"BOUND bodies containing a reflective construct = "
          f"{_refl_bound} (slice: {_slice_refl})",
          anchor=True)

# ======================================================================
# THE BLUEPRINTS (pin §2) — the four schedule variants
# ======================================================================
FULLMENU_BUDGET = 240.0      # seconds per full-menu replay (printed)
HEAD_REPLAY_BUDGET = 150.0   # seconds for DOUBLE-GRID(4, 2) (printed)
AC2_REPLAY_BUDGET = 1500.0   # seconds for ARBCHAIN**(5) (printed)
BUILT = {}


def _levelup(b, actors):
    """THE LEVELLING PASS (round-1 MAJOR 1 / NIT 2, the referee's
    construction, carried here with credit and gated like any other).
    Pad every actor register with the grammar's OWN idle event
    ('n', a) — the same event kind the committed blueprints already use
    for their tails — until every actor's last event sits at a COMMON
    height.  Nothing else changes: no new lineage, no delivery, no
    arbitration.  Its point is that height alignment is a DESIGN
    REQUIREMENT the grammar can satisfy from inside, not an obstruction:
    a chart counts only directions at EXACTLY height + 2, so a schedule
    whose k depth-1 consumers sit at height + 1 realizes SUM_y b(y)."""
    C = poset_of(b.H)
    hs = heights(C)
    last = {}
    for j, op in enumerate(b.H):
        for r in regs_of(op):
            if isinstance(r, str):
                last[r] = j
    cur = {a: hs[last[a]] for a in actors if a in last}
    L = max(cur.values())
    pads = 0
    for a in actors:
        while cur.get(a, L) < L:
            _pick(b, (a,), ('n', a), f"level {a}")
            if b.refusal:
                return pads, L
            cur[a] += 1
            pads += 1
    return pads, L


def dgrid(g, R, order='phase', boot='mints', level=False):
    """V1/V4 — THE DOUBLE GRID, generalized in g from D66's committed
    `double_grid` and gated (K0d) to reproduce it EVENT FOR EVENT at
    g = 3, order = 'phase', boot = 'mints'.

    2g groups (g rows and g columns) on g^2 actors; each actor is in
    exactly ONE row and ONE column, so it carries TWO live proposals on
    TWO distinct unsuperseded bases.  Bootstrap: 2g single-proposer
    mints (each seed alone, from genesis, before any delivery reaches
    it) and 2g(g-1) deliveries.  Then each round is 2g^2 proposals and
    2g arbitrations and ZERO deliveries.

    `order` = 'phase'  — all g ROW arbitrations, then all g COLUMN
                         arbitrations (D66's schedule);
              'inter'  — row 0, column 0, row 1, column 1, ... .
    The ONLY difference is the arbitration order inside a round.
    `level` = True — LEVELLED-DGRID: `_levelup` between the bootstrap
    and the rounds (round-1 NIT 2's construction, which closes this
    unit's first version's residue 2).

    THE R-PREFIX PROPERTY, used by `get` and gated in K0f: the rounds
    are appended, so dgrid(g, R).H is literally the first
    2g(g+1) + 2g(g+1)*R events of dgrid(g, R') for every R < R'."""
    ac = [[f"D{i}{j}" for j in range(g)] for i in range(g)]
    flat = [a for row in ac for a in row]
    b = B(tuple(flat))
    groups = ([[ac[i][j] for j in range(g)] for i in range(g)]
              + [[ac[i][j] for i in range(g)] for j in range(g)])
    # row seeds on the diagonal, column seeds two steps off it, so the 2g
    # seeds are pairwise distinct and each is UNTOUCHED when it mints
    seeds = ([ac[i][i] for i in range(g)]
             + [ac[(j + 2) % g][j] for j in range(g)])
    cur = [None] * len(groups)
    for gi, sd in enumerate(seeds):          # bootstrap: 2g mints ...
        _pick(b, (sd,), ('p', sd, V0, 0), f"mint-propose {sd}")
        ck = frozenset({(sd, V0, 0)})
        _pick(b, (sd,), ('r', sd, ck, ck), f"mint-arbitrate {sd}")
        cur[gi] = vname(V0, ck, sd)
        if b.refusal:
            return b
    for gi, grp in enumerate(groups):        # ... and 2g(g-1) deliveries
        for a in grp:
            if a != seeds[gi]:
                dl(b, seeds[gi], a, cur[gi])
                if b.refusal:
                    return b
    b.npad, b.plevel = 0, None
    if level:
        b.npad, b.plevel = _levelup(b, flat)
        if b.refusal:
            return b
    seq = (list(range(2 * g)) if order == 'phase'
           else [x for i in range(g) for x in (i, g + i)])
    for t in range(R):
        trips = []
        for gi, grp in enumerate(groups):    # ALL proposals of the round
            tp = [(a, cur[gi], 0 if a == seeds[gi] else 1) for a in grp]
            trips.append(tp)
            for x in tp:
                _pick(b, (x[0],), ('p',) + x, f"propose {x[0]}")
                if b.refusal:
                    return b
        for gi in seq:
            wk = frozenset({(seeds[gi], cur[gi], 0)})
            _pick(b, (seeds[gi],),
                  ('r', seeds[gi], frozenset(trips[gi]), wk),
                  f"arbitrate {seeds[gi]}")
            if b.refusal:
                return b
            cur[gi] = vname(cur[gi], wk, seeds[gi])
    return b


def shared_base(g):
    """V2 — THE ONE-LINEAGE DESIGN, built until it breaks.  Mint one
    version, spread it to every actor, then have an actor make its ROW
    proposal and its COLUMN proposal on THAT ONE BASE.  The second
    proposal is not offered: d42b1's `prop_options_in_view` skips a base
    on which the actor already has a live proposal.  Returns (builder,
    the actor, the base) so the refusal can be gated against the layer's
    own option list rather than against the absence of a menu hit."""
    ac = [[f"S{i}{j}" for j in range(g)] for i in range(g)]
    flat = [a for row in ac for a in row]
    b = B(tuple(flat))
    sd = ac[0][0]
    _pick(b, (sd,), ('p', sd, V0, 0), f"mint-propose {sd}")
    ck = frozenset({(sd, V0, 0)})
    _pick(b, (sd,), ('r', sd, ck, ck), f"mint-arbitrate {sd}")
    cur = vname(V0, ck, sd)
    for a in flat:
        if a != sd:
            dl(b, sd, a, cur)
    a0 = ac[0][1]
    _pick(b, (a0,), ('p', a0, cur, 1), f"ROW proposal by {a0}")
    _pick(b, (a0,), ('p', a0, cur, 0),
          f"COLUMN proposal by {a0} ON THE SAME BASE")
    return b, a0, cur


def arbchain_k(m, k, level=False):
    """ARBCHAIN*(m, k) — D67's corrected smallest witness.  One
    k-proposer arbitration whose k proposer registers are consumed by m
    further K-PROPOSER arbitrations and by k - m deliveries.  D66's own
    `arbchain` hardcodes THREE proposers in its secondary arbitrations
    (its gate only ever ran k = 3), so it realizes 3m + 2(k - m); both
    are measured in K3 and they agree exactly at k = 3.

    `level` = True gives ARBCHAIN**(k) := arbchain_k(k, k, level=True),
    the ROUND-1 REFEREE'S construction (MAJOR 1): the same shape, with
    `_levelup` inserted between the bootstrap and the proposals.  The
    bootstrap of ARBCHAIN* supplies A_i AND all k - 2 helpers T_ij by a
    SERIAL delivery chain on register S_i, so p(S_i, Y_i, 0) sits k - 1
    layers above its mint and at k = 5 two of the five secondary
    arbitrations land at height offset 2 from THE ARBITRATION.  That is
    a property of the ORDERING OF A BOOTSTRAP, and one levelling pass
    removes it — at every k tried."""
    A = [f"A{i}" for i in range(k)]
    S = [f"S{i}" for i in range(m)]
    T = [[f"T{i}x{j}" for j in range(k - 2)] for i in range(m)]
    F = [f"F{i}" for i in range(m, k)]
    acts = tuple(A + S + [x for r in T for x in r] + F)
    b = B(acts)

    def mint(sd):
        _pick(b, (sd,), ('p', sd, V0, 0), f"mint-propose {sd}")
        ck = frozenset({(sd, V0, 0)})
        _pick(b, (sd,), ('r', sd, ck, ck), f"mint-arbitrate {sd}")
        return vname(V0, ck, sd)

    X = mint(A[0])
    for a in A[1:]:
        dl(b, A[0], a, X)
    Y = []
    for i in range(m):
        Y.append(mint(S[i]))
        dl(b, S[i], A[i], Y[i])
        for x in T[i]:
            dl(b, S[i], x, Y[i])
    b.npad, b.plevel = 0, None
    if level:
        b.npad, b.plevel = _levelup(b, list(acts))
    g0 = [(a, X, 0 if a == A[0] else 1) for a in A]
    gi = [[(S[i], Y[i], 0), (A[i], Y[i], 1)]
          + [(x, Y[i], 1) for x in T[i]] for i in range(m)]
    for x in g0 + [x for tp in gi for x in tp]:
        _pick(b, (x[0],), ('p',) + x, f"propose {x[0]}")
    ebase = len(b.H)
    _pick(b, (A[0],), ('r', A[0], frozenset(g0), frozenset({g0[0]})),
          "THE ARBITRATION")
    V = vname(X, frozenset({g0[0]}), A[0])
    for i in range(m):                       # arbitration consumers
        _pick(b, (S[i],), ('r', S[i], frozenset(gi[i]),
                           frozenset({gi[i][0]})), f"second arb {S[i]}")
    for i in range(m, k):                    # delivery consumers
        dl(b, A[i], F[i - m], V)
    tail = [x for i in range(m) for x in ([A[i], S[i]] + T[i])]
    tail += [x for i in range(m, k) for x in (A[i], F[i - m])]
    for a in tail:
        _pick(b, (a,), ('n', a), f"idle {a}")
    return b, ebase


def succ_of(H):
    """The immediate-successor relation P, read from `event_poset`'s own
    `last` bookkeeping over the committed `regs_of`."""
    su = defaultdict(set)
    last = {}
    for j, op in enumerate(H):
        for r in regs_of(op):
            if r in last:
                su[last[r]].add(j)
        for r in regs_of(op):
            last[r] = j
    return su


def actors_of(key):
    if key[0] in ('DG', 'INTER', 'LDG'):
        return [f"D{i}{j}" for i in range(key[1]) for j in range(key[1])]
    if key[0] == 'CG':
        return [f"G{i}{j}" for i in range(key[1]) for j in range(key[1])]
    return None


def tag_of(k):
    if k[0] == 'DG':
        return f"DOUBLE-GRID(g={k[1]},R={k[2]})"
    if k[0] == 'LDG':
        return f"LEVELLED-DGRID(g={k[1]},R={k[2]})"
    if k[0] == 'INTER':
        return f"DGRID-INTERLEAVED(g={k[1]},R={k[2]})"
    return f"CONFLICT-GRID(g={k[1]},R={k[2]})"


class Prefix:
    """A record read off the first n events of a longer build (the
    R-prefix lemma; K0f gates it).  `maxhits` is the parent's, which is
    an UPPER bound for any prefix because the prefix's steps are
    literally the parent's first n picks — and `_pick` refuses on 0 hits,
    so 1 is exact."""

    def __init__(self, parent, n):
        self.H = list(parent.H[:n])
        self.refusal = None
        self.maxhits = parent.maxhits
        self.actors = parent.actors
        self.npad, self.plevel = 0, None


def get(key):
    """Build (once) and measure a swept configuration.  DOUBLE-GRID
    (4, R) for R < 4 is READ OFF the (4, 4) build by the R-prefix lemma
    (K0f) instead of being rebuilt: the four separate builds cost 1,900 s
    and the one build costs what its own last round costs."""
    if key in BUILT:
        return BUILT[key]
    t = time.time()
    if key[0] == 'DG' and key != PREFIX_PARENT and key[1] == PREFIX_PARENT[1]:
        par = get(PREFIX_PARENT)[0]
        b = Prefix(par, PREFIX_N(key))
    else:
        b = (dgrid(key[1], key[2]) if key[0] == 'DG'
             else (dgrid(key[1], key[2], level=True) if key[0] == 'LDG'
                   else (dgrid(key[1], key[2], order='inter')
                         if key[0] == 'INTER'
                         else d66_conflict_grid(key[1], key[2]))))
    pr = None if b.refusal else profile(poset_of(b.H))
    BUILT[key] = (b, pr, time.time() - t)
    return BUILT[key]


def line(k, b, pr, dt, d=2):
    if pr is None:
        return f"{tag_of(k)}: REFUSAL at {b.refusal}"
    x = pr[d]
    return (f"{tag_of(k):32s} n={x['n']:4d} arb {float(arbshare(b.H)):.4f} "
            f"homog {float(x['h2']):.4f}  |D|>=4 {float(x['h4']):.4f}  "
            f"max|D| {x['max']:2d}  mean|D| {float(x['mean']):.2f}  omega "
            f"{float(x['om']):.4f}  [{dt:.1f}s]")


# The k = 4 R-sweep, the committed (3, R) anchor family, the interleaved
# variant, the rotating (delivery-supplied) comparator, and the two
# round-1 additions: DOUBLE-GRID(4, 4) (BLOCKER 1) and LEVELLED-DGRID
# (4, 2) (NIT 2).
HEAD = ('DG', 4, 2)          # the R = 2 record the first version headlined
FLAG = ('DG', 4, 4)          # THE ROUND-1 FLAGSHIP: in band, WHOLE, 16 wide
PREFIX_PARENT = FLAG         # built once; R < 4 read off its prefixes


def PREFIX_N(k):
    """The R-prefix lemma's own event count: bootstrap 2g(g+1) then
    2g(g+1) per round."""
    return 2 * k[1] * (k[1] + 1) * (1 + k[2])


ANCH = [('DG', 3, 2), ('DG', 3, 4)]
SWEEP = [('DG', 4, 1), HEAD, ('DG', 4, 3), FLAG, ('LDG', 4, 2)] + ANCH + \
        [('INTER', 3, 2), ('INTER', 4, 2), ('CG', 4, 4), ('CG', 4, 6)]

if not PROBE:
    print(f"\n[the blueprints and every parameter, printed]")
    print(f"    V1 DOUBLE-GRID(g, R) [MINTS-FIRST, PHASE-SEPARATED]: 2g "
          f"groups (g rows + g columns) on g^2 actors, 2g independent "
          f"base lineages minted once (2 events each) and spread by "
          f"2g(g-1) bootstrap deliveries; then each round is 2g^2 "
          f"proposals + g ROW arbitrations + g COLUMN arbitrations and "
          f"ZERO deliveries.  At g = 4: 16 actors, 8 groups, k = 4 "
          f"proposers per arbitration, 40 bootstrap events (8 mints, 24 "
          f"deliveries) and 40 events per round.")
    print(f"    V2 SHARED-BASE(g): one lineage, spread to every actor, "
          f"rows and columns conflicting on THAT base.  Built until it "
          f"breaks; the break is gated against "
          f"`prop_options_in_view` itself.")
    print(f"    V3 CONFLICT-GRID(g, R) [ROTATION]: D66's committed "
          f"rotating blueprint — rounds alternate ROW and COLUMN groups "
          f"on one lineage per actor, g - 1 deliveries per group per "
          f"round.")
    print(f"    V4 DOUBLE-GRID(g, R, order='inter'): V1 with the "
          f"arbitration order interleaved (row 0, col 0, row 1, col 1, "
          f"...).  Same events, same groups, same bootstrap; ONLY the "
          f"arbitration order differs.")
    print(f"    ARBCHAIN*(m, k): one k-proposer arbitration, m "
          f"k-proposer arbitration consumers and k - m delivery "
          f"consumers, so the refined bound predicts "
          f"|D_e(2)| = k*m + 2*(k - m) over [2k, k^2].")
    print(f"    [ROUND 1, THE REFEREE'S THREE CONSTRUCTIONS, carried with "
          f"credit and gated like any other object]")
    print(f"      DOUBLE-GRID(4, 4) — BLOCKER 1: one more round than the "
          f"first version's sweep could afford.  It is the object that "
          f"REFUTES the first version's flagship negative.")
    print(f"      ARBCHAIN**(k) = arbchain_k(k, k, level=True) — MAJOR 1: "
          f"ARBCHAIN*(k, k) with every actor register HEIGHT-LEVELLED by "
          f"the grammar's own ('n', a) idle before the proposals, so that "
          f"all k depth-1 consumers sit at exactly height + 1.")
    print(f"      LEVELLED-DGRID(g, R) = dgrid(g, R, level=True) — NIT 2: "
          f"the same levelling pass between the DOUBLE-GRID bootstrap and "
          f"its rounds.")
    print(f"    SKY-B depths measured = (2, 3); committed SKYB_DEPTH = "
          f"{SKYB_DEPTH}.  Full-menu replay budgets: "
          f"{FULLMENU_BUDGET:.0f}s per record, "
          f"{HEAD_REPLAY_BUDGET:.0f}s for DOUBLE-GRID(4, 2), "
          f"{AC2_REPLAY_BUDGET:.0f}s for ARBCHAIN**(5).")
    print(f"    swept configurations = {len(SWEEP)}: "
          + "; ".join(tag_of(k) for k in SWEEP))
    print(f"    THE R-PREFIX LEMMA (runtime economy, gated in K0f): "
          f"{tag_of(FLAG)} is built ONCE and "
          f"{', '.join(tag_of(k) for k in SWEEP if k[0] == 'DG' and k[1] == FLAG[1] and k != FLAG)}"
          f" are read off its prefixes at "
          f"{ {tag_of(k): PREFIX_N(k) for k in SWEEP if k[0] == 'DG' and k[1] == FLAG[1] and k != FLAG} }"
          f" events.")

if PROBE:
    for kk in (('DG', 3, 2), ('INTER', 3, 2)):
        _b, _pr, _dt = get(kk)
        C = poset_of(_b.H)
        print(f"DIGEST {kk}: " + repr(
            [(_pr[d]['h2'], _pr[d]['om'], _pr[d]['h4'], _pr[d]['max'],
              _pr[d]['n']) for d in (2, 3)])
            + " arb " + repr(arbshare(_b.H)) + " widths "
            + repr(sorted(Counter(len(sky(C, e, 'B', 2)[0])
                                  for e in range(len(C))).items())))
    for _m in (0, 2, 4):
        _b, _e = arbchain_k(_m, 4)
        _C = poset_of(_b.H)
        print(f"DIGEST ARBCHAIN*({_m},4): n={len(_b.H)} "
              f"|D|={len(sky(_C, _e, 'B', 2)[0])} hits={_b.maxhits} "
              f"refusal={_b.refusal}")
    for _k in (3, 4):
        _b, _e = arbchain_k(_k, _k, level=True)
        _C = poset_of(_b.H)
        _hs = heights(_C)
        print(f"DIGEST ARBCHAIN**({_k}): n={len(_b.H)} pads={_b.npad} "
              f"level={_b.plevel} h(e)={_hs[_e]} "
              f"|D|={len(sky(_C, _e, 'B', 2)[0])} hits={_b.maxhits} "
              f"refusal={_b.refusal}")
    _bs, _a0, _cu = shared_base(4)
    print(f"DIGEST SHARED-BASE(4): refusal={_bs.refusal} n={len(_bs.H)}")
    sys.exit(0)

# ======================================================================
# K0 — THE ANCHORS: the committed controls, re-run in this process
# ======================================================================
print("\n[K0b THE DELIVERY ANCHORS — D63's delivery crystal and D60's "
      "brick, RE-RUN here]")
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
      f"|D|>=4 {P_BK[2]['h4']}, max|D| {P_BK[2]['max']}  "
      f"[{time.time()-t_a:.1f}s]")
check("K0b [ANCHOR, exit 1 on breakage] THE DELIVERY CONTROLS REPRODUCE "
      "THEIR COMMITTED ROWS EXACTLY.  D63's own `double_ring` function "
      "object gives 177 events, d = 2 homogeneity 47/59, |D| >= 4 at "
      "1/3, max |D| = 4, mean omega 100/137 and D63's d = 3 row; D60's "
      "brick is reproduced EVENT FOR EVENT with its published row.  "
      "Every comparison this unit makes is against these re-run objects, "
      "never against a re-typed number",
      _dr_ok and _bk_same and _bk_ok and not b_dr.refusal
      and not b_bk.refusal,
      f"DR row exact = {_dr_ok}; brick event list identical = {_bk_same}, "
      f"row = {_bk_ok}", anchor=True)

print("\n[K0c THE SPRINKLING COMPARATORS — D58's atlas re-run on the same "
      "eleven genuine configurations D60/D63/D66 used.  THE WIDTH RANGE "
      "THIS UNIT IS SHOOTING AT IS READ OFF THESE, NOT TYPED]")
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
          f"(~[{float(W4B[d][0]):.4f}, {float(W4B[d][1]):.4f}]); "
          f"**max|D| RANGE [{MXB[d][0]}, {MXB[d][1]}]**")
# ROUND-1 MAJOR 2(a): the comparison population is BIMODAL BY SPACETIME
# DIMENSION and the hull [10, 17] is the hull of two disjoint clusters.
# Every "sprinkling-grade" sentence in this receipt carries this table.
DIMR = {(dim, d): (min(SPR[k][d]['max'] for k in SPR if k[0] == dim),
                   max(SPR[k][d]['max'] for k in SPR if k[0] == dim))
        for dim in ('M21', 'M31') for d in (2, 3)}
DIMN = {dim: sum(1 for k in SPR if k[0] == dim) for dim in ('M21', 'M31')}
for d in (2, 3):
    print(f"    d = {d}: THE max|D| RANGE IS A HULL OF TWO DIMENSIONALLY "
          f"DISTINCT CLUSTERS (round-1 MAJOR 2a) — M21 (2+1, "
          f"{DIMN['M21']} configurations) "
          f"{sorted(SPR[k][d]['max'] for k in SPR if k[0] == 'M21')} = "
          f"range [{DIMR[('M21', d)][0]}, {DIMR[('M21', d)][1]}]; "
          f"M31 (3+1, {DIMN['M31']}) "
          f"{sorted(SPR[k][d]['max'] for k in SPR if k[0] == 'M31')} = "
          f"range [{DIMR[('M31', d)][0]}, {DIMR[('M31', d)][1]}].")
print(f"    SIZE-MATCHING (round-1 NIT 3, said so the repair does not add "
      f"the WRONG caveat): all {len(SPR)} genuine configurations are at "
      f"N = 120 events and the headline record is 120 events, so the "
      f"comparison IS size-matched and no extreme-order-statistic caveat "
      f"applies.  What needed the label is the DIMENSIONAL population, "
      f"printed above, not the size.")
print(f"    [{time.time() - t_cmp:.1f}s]")
check("K0c [ANCHOR, exit 1 on breakage] THE COMPARATORS ARE RE-RUN, NOT "
      "RE-TYPED, and reproduce D60/D63/D66's committed bands exactly: "
      "homogeneity [77/120, 4/5] and |D| >= 4 [17/40, 13/20] at d = 2, "
      "and the sprinkling max |D| RANGE [10, 17] at d = 2 — the range "
      "the pin's K3 question is asked against, and the k = 4 bound "
      "k^2 = 16 sits INSIDE it.  AND (ROUND-1 MAJOR 2a) THE RANGE IS "
      "GATED AS A HULL OF TWO CLUSTERS, NOT AS A POPULATION: the five "
      "M21 (2+1) configurations give [10, 11] and the six M31 (3+1) ones "
      "give [14, 17], so 16 lies in the 3+1 cluster and NOT in the 2+1 "
      "one, and no sentence in this receipt says 'inside the sprinkling "
      "range' without saying WHICH sprinklings.  Every threshold used "
      "anywhere below is one of these measured numbers or one of D58's "
      "own columns; this unit invents none",
      BAND[2] == (Fr(77, 120), Fr(4, 5))
      and W4B[2] == (Fr(17, 40), Fr(13, 20)) and len(SPR) == 11
      and MXB[2] == (10, 17) and DIMR[('M21', 2)] == (10, 11)
      and DIMR[('M31', 2)] == (14, 17)
      and DIMR[('M21', 2)][1] < 16 <= DIMR[('M31', 2)][1],
      f"{len(SPR)} genuine configurations; d = 2 band {BAND[2]}, |D|>=4 "
      f"band {W4B[2]}, sprinkling max|D| range {MXB[2]} = hull of M21 "
      f"{DIMR[('M21', 2)]} and M31 {DIMR[('M31', 2)]}; d = 3 max|D| "
      f"range {MXB[3]} = hull of M21 {DIMR[('M21', 3)]} and M31 "
      f"{DIMR[('M31', 3)]}", anchor=True)

# ======================================================================
# K0d/K1 — THE SWEEP: does the 4-proposer schedule force?
# ======================================================================
print("\n[K1a THE SWEEP — every configuration built by the layer's own "
      "menu, every event specified by its FULL EVENT TUPLE.  All figures "
      "at d = 2; 'band' = K0c's recomputed sprinkling band]")
t_sw = time.time()
get(FLAG)                    # the prefix parent, built before the loop so
                             # the printed cost curve is honest per record
for k in SWEEP:
    b, pr, dt = get(k)
    print("    " + line(k, b, pr, dt)
          + ("   <== READ OFF THE PREFIX OF " + tag_of(FLAG)
             if isinstance(b, Prefix) else ""))
    sys.stdout.flush()
print(f"    swept {len(SWEEP)} configurations, "
      f"{sum(len(v[0].H) for v in BUILT.values())} events built "
      f"[{time.time() - t_sw:.1f}s]")

# ---- K0f the R-prefix lemma ---------------------------------------------
print(f"\n[K0f THE R-PREFIX LEMMA — gated at g = 3, where BOTH records are "
      f"built INDEPENDENTLY and both are D66 anchors, and then used at "
      f"g = 4 to buy the round-1 flagship's extra round]")
_pref3_ok = (list(BUILT[('DG', 3, 2)][0].H)
             == list(BUILT[('DG', 3, 4)][0].H[:PREFIX_N(('DG', 3, 2))]))
print(f"    at g = 3: dgrid(3, 2).H == dgrid(3, 4).H[:{PREFIX_N(('DG', 3, 2))}] "
      f"event for event = {_pref3_ok} — two SEPARATE builds, both gated "
      f"against d66's own `double_grid` function object in K0d.")
# the round-1 committed rows, every one of which the round-1 referee
# reproduced in an independent driver of his own (review §C)
R1_ROWS = {('DG', 4, 1): {'n': 80, 'h2': Fr(13, 40), 'h4': Fr(9, 80),
                          'max': 4, 'max3': 7, 'h2_3': Fr(37, 80)},
           ('DG', 4, 2): {'n': 120, 'h2': Fr(49, 120), 'h4': Fr(4, 15),
                          'max': 16, 'max3': 16, 'h2_3': Fr(13, 24)},
           ('DG', 4, 3): {'n': 160, 'h2': Fr(73, 160), 'h4': Fr(7, 20),
                          'max': 16, 'max3': 16, 'h2_3': Fr(21, 32)}}
_pref4_ok = True
for k, row in R1_ROWS.items():
    pr = BUILT[k][1]
    ok = (pr[2]['n'] == row['n'] and pr[2]['h2'] == row['h2']
          and pr[2]['h4'] == row['h4'] and pr[2]['max'] == row['max']
          and pr[3]['h2'] == row['h2_3'] and pr[3]['max'] == row['max3'])
    _pref4_ok = _pref4_ok and ok
    print(f"    {tag_of(k):32s} from the prefix: n={pr[2]['n']} d2 homog "
          f"{pr[2]['h2']} |D|>=4 {pr[2]['h4']} max {pr[2]['max']} | d3 "
          f"homog {pr[3]['h2']} max {pr[3]['max']}  ==  the ROUND-1 "
          f"COMMITTED ROW: {ok}")
check("K0f [ANCHOR, exit 1 on breakage] THE R-PREFIX LEMMA IS GATED, NOT "
      "ASSUMED, AND THE ROWS IT SAVES ARE ANCHORED AGAINST INDEPENDENTLY "
      "BUILT ONES.  `dgrid` appends rounds, so the R-round record is a "
      "PREFIX of the R'-round record for R < R'; the identity is checked "
      "EVENT FOR EVENT at g = 3 between two separate builds, both of "
      "which K0d gates against d66's own function object.  At g = 4 the "
      "lemma buys the round-1 flagship: DOUBLE-GRID(4, 4) is built once "
      "and (4, 1), (4, 2), (4, 3) are read off its prefixes — and every "
      "one of those three rows reproduces THE ROUND-1 COMMITTED ROW, "
      "which was produced by an independent build and which the round-1 "
      "referee reproduced again in a driver of his own.  So the economy "
      "changes the runtime and nothing else",
      _pref3_ok and _pref4_ok,
      f"g = 3 prefix identity event for event = {_pref3_ok}; g = 4 rows "
      f"reproduced from prefixes = {_pref4_ok} (at {len(R1_ROWS)} "
      f"configurations, both depths)", anchor=True)

_refusals = [(tag_of(k), v[0].refusal) for k, v in BUILT.items()
             if v[0].refusal is not None]
_hits = max(v[0].maxhits for v in BUILT.values())
_kinds = Counter(e[0] for v in BUILT.values() for e in v[0].H)
print(f"    event species over the whole sweep: {dict(sorted(_kinds.items()))}"
      f"; refusals = {len(_refusals)} {_refusals if _refusals else ''}; "
      f"max menu hits per specification over every step of every record "
      f"= {_hits}")
check("K1a [THE PIN'S K-I DOES NOT FIRE] THE 4-PROPOSER SCHEDULE FORCES. "
      "Every one of the swept records — including the k = 4 DOUBLE GRID "
      "at every R — is admissible at every step against the layer's own "
      "restricted menu, and every specification (a FULL EVENT TUPLE, so "
      "the winner key and the ckey are part of the specification) "
      "matched EXACTLY ONE candidate.  WHAT THIS GATE MEASURES (D63 "
      "MINOR 4 / D66 A1(a)): uniqueness is STRUCTURAL — menu events are "
      "pairwise distinct and a full tuple can match at most one — so the "
      "gated content is that the specified event IS OFFERED (hits = 1, "
      "never 0) and that no step was refused.  SCOPE OF THE PREFIX ROWS "
      "(K0f): the three prefix-derived records were driven as the first "
      "n steps of DOUBLE-GRID(4, 4)'s own drive, so their forcedness is "
      "that drive's, step for step, not a separate claim",
      _hits == 1 and not _refusals and len(BUILT) == len(SWEEP),
      f"records = {len(BUILT)} ({sum(1 for v in BUILT.values() if isinstance(v[0], Prefix))} "
      f"of them prefixes of another), events = "
      f"{sum(len(v[0].H) for v in BUILT.values())} "
      f"({sum(len(v[0].H) for k, v in BUILT.items() if not isinstance(v[0], Prefix))} "
      f"independently driven), max hits = {_hits}, "
      f"refusals = {len(_refusals)}")

print("\n[K0d THE COMMITTED DOUBLE-GRID ANCHOR — D66's own (3, 2) and "
      "(3, 4) rows, reproduced by THIS unit's generalized blueprint]")
_d66_rows = {                      # v10/data/d66_arbitration_crystal_exact.out
    ('DG', 3, 2): {'n': 72, 'arb': Fr(1, 4), 'h2': Fr(4, 9),
                   'h4': Fr(5, 72), 'max': 9, 'om': Fr(1394, 2500),
                   'dels': 12},
    ('DG', 3, 4): {'n': 120, 'arb': Fr(1, 4), 'h2': Fr(31, 60),
                   'h4': Fr(11, 120), 'max': 9, 'dels': 12,
                   'h2_3': Fr(47, 60), 'max_3': 9,
                   'hist': {0: 10, 1: 48, 2: 5, 3: 46, 4: 2, 9: 9}}}
_anch_ok = True
_evt_ok = True
for k in ANCH:
    b, pr, dt = BUILT[k]
    row = _d66_rows[k]
    nd = sum(1 for e in b.H if e[0] == 'd')
    same = list(b.H) == list(d66_double_grid(k[1], k[2]).H)
    _evt_ok = _evt_ok and same
    ok = (len(b.H) == row['n'] and arbshare(b.H) == row['arb']
          and pr[2]['h2'] == row['h2'] and pr[2]['h4'] == row['h4']
          and pr[2]['max'] == row['max'] and nd == row['dels'])
    if 'h2_3' in row:
        ok = ok and pr[3]['h2'] == row['h2_3'] and pr[3]['max'] == row['max_3']
        hist = dict(sorted(Counter(
            len(sky(poset_of(b.H), e, 'B', 2)[0])
            for e in range(len(b.H))).items()))
        ok = ok and hist == row['hist']
        print(f"    {tag_of(k):32s} width histogram at d = 2 = {hist} "
              f"(committed {row['hist']})")
    _anch_ok = _anch_ok and ok
    print(f"    {tag_of(k):32s} n={len(b.H)} arb {arbshare(b.H)} "
          f"deliveries {nd} d2 homog {pr[2]['h2']} |D|>=4 {pr[2]['h4']} "
          f"max|D| {pr[2]['max']} | d3 homog {pr[3]['h2']} max|D| "
          f"{pr[3]['max']}  ==  D66's committed row: {ok}; event list "
          f"IDENTICAL to d66's own `double_grid` = {same}")
check("K0d [ANCHOR, exit 1 on breakage] THIS UNIT'S GENERALIZED "
      "BLUEPRINT IS D66's BLUEPRINT.  `dgrid(3, R, 'phase', 'mints')` "
      "produces the SAME EVENT LIST, event for event, as the committed "
      "`d66.double_grid(3, R)` function object — the strong form, not "
      "the profile-coincidence form D66's own A1(d) had to settle for — "
      "and both reproduce D66's committed rows for (3, 2) and (3, 4) "
      "exactly: 72 and 120 events, arbitration share 1/4, 12 bootstrap "
      "deliveries, d = 2 homogeneity 4/9 and 31/60, max |D| = 9, d = 3 "
      "homogeneity 47/60, and (3, 4)'s full width histogram "
      "{0:10, 1:48, 2:5, 3:46, 4:2, 9:9}.  So the g = 4 rows below are "
      "produced by the object that reproduces the committed g = 3 ones",
      _anch_ok and _evt_ok,
      f"committed rows reproduced = {_anch_ok}; event lists identical to "
      f"d66's function object = {_evt_ok} (at {len(ANCH)} "
      f"configurations)", anchor=True)

_skyB_ok = True
for _kk in (('DG', 3, 2), HEAD):
    _Ck = poset_of(BUILT[_kk][0].H)
    _hk = heights(_Ck)
    for _d in (2, 3):
        for _e in range(len(_Ck)):
            if set(_skyB(_Ck, _hk, _e, _d)) != set(sky(_Ck, _e, 'B', _d)[0]):
                _skyB_ok = False
check("K0e THE HOISTED SKY-B (D66's `_skyB`, imported) AGREES WITH THE "
      "COMMITTED d47a `sky` EVENT FOR EVENT.  The bulk bound-checking "
      "reads SKY-B with the height vector computed once per record "
      "instead of once per event; that is an optimisation, not a "
      "definition, and it is gated against the committed instrument at "
      "every event of two whole records at both depths — one of them the "
      "HEADLINE k = 4 record.  Every chart this unit EXHIBITS is read "
      "from the committed `sky` directly",
      _skyB_ok, f"records compared event for event at both depths = 2 "
      f"({tag_of(('DG', 3, 2))}, {tag_of(HEAD)}); disagreements = 0")

# ---- K1b the schedule variants -------------------------------------------
print("\n[K1b THE SCHEDULE VARIANTS — the pin's §3 K1 asks for TWO "
      "variants before any conclusion about forcedness.  FOUR were "
      "built; the one that REFUSES is reported with its mechanism, not "
      "papered over]")
_bs, _sb_actor, _sb_base = shared_base(4)
_sbH = _bs.H[:_bs.refusal[1]] if _bs.refusal else _bs.H
_sb_view = own_view(list(_sbH), _sb_actor)      # d42b1's OWN view builder
_sb_opts = prop_options_in_view(_sb_view, _sb_actor)
_sb_live = [(op[1], op[2], op[3]) for op in _sb_view.live.values()]
_sb_menu = candidates_for(list(_sbH), (_sb_actor,))
_sb_kinds = sorted({e[0] for e, q in _sb_menu})
print(f"    V2 SHARED-BASE(4): REFUSAL = {_bs.refusal}.  At that prefix "
      f"({len(_sbH)} events: 1 mint + 15 deliveries + 1 proposal) the "
      f"actor {_sb_actor} holds the single lineage and already has a "
      f"LIVE proposal on it.")
print(f"      the layer's own option list "
      f"`prop_options_in_view(view, {_sb_actor})` = {_sb_opts} — EMPTY, "
      f"because d42b1 skips a base on which the actor already has a live "
      f"proposal; live triples in view = {_sb_live}; the whole menu "
      f"offered to {_sb_actor} has kinds {_sb_kinds} and contains NO "
      f"proposal at all.")
print(f"      MECHANISM, stated WITH THE STEP THAT MAKES IT TRUE "
      f"(round-1 MINOR 5; the first version wrote 'two live bases per "
      f"actor, i.e. 2g independent lineages' and the 'i.e.' skipped a "
      f"step).  (1) A k-proposer conflict needs k live proposals ON ONE "
      f"BASE, and one actor may hold AT MOST ONE live proposal per base "
      f"— that is what the empty option list above shows, and it gives "
      f"TWO BASES PER ACTOR, not yet 2g lineages.  (2) THE MISSING STEP: "
      f"two concurrent groups CANNOT SHARE A BASE.  `admissible` "
      f"requires triples(view, comp) == ckey for a WHOLE component, "
      f"`View.components()` groups live proposals by base, and on one "
      f"base the payload-0/payload-1 conflict graph of two groups is "
      f"CONNECTED — so one base admits exactly one arbitration per "
      f"generation.  (3) Hence g row bases + g column bases, pairwise "
      f"distinct because every (r, c) cell sits in one of each: 2g "
      f"lineages.  That is what V1's mints-first bootstrap builds and "
      f"why it cannot be replaced by a single mint-and-spread.")
_sb_stub = len(_bs.H)
print(f"      WHAT V2 IS AND IS NOT (round-1 MINOR 4).  `shared_base(4)` "
      f"mints one version, spreads it to fifteen actors, makes ONE actor "
      f"propose twice on that base back to back, and stops: it is a "
      f"{_sb_stub}-event DEMONSTRATION OF `prop_options_in_view`, not an "
      f"alternative schedule that was driven and failed, and it never "
      f"attempts an arbitration.  IT DOES NOT SHOW THAT ONE LINEAGE PER "
      f"ACTOR REFUSES: V3 CONFLICT-GRID(4, R) IS a one-lineage-per-actor "
      f"design and it does NOT refuse — it forces, tiles and reaches "
      f"width 8.  The scoped claim, and the only one made here, is that "
      f"a grid whose rows and columns conflict CONCURRENTLY cannot run "
      f"on one shared base.")
check("K1b(i) [A FIRST-CLASS NEGATIVE, GATED AGAINST THE LAYER ITSELF, "
      "AND SCOPED IN THE LABEL — round-1 MINOR 4] THE ONE-*SHARED-BASE* "
      "k = 4 SCHEDULE REFUSES, AND THE REFUSAL IS NOT A MISSING MENU HIT "
      "BUT THE LAYER'S OWN OPTION LIST BEING EMPTY.  "
      "`prop_options_in_view` returns NO option for the actor's second "
      "proposal on the shared base, so the menu offered to it contains "
      "no proposal of any kind; the mints-first bootstrap of V1 is "
      "FORCED by the grammar rather than chosen for convenience.  THE "
      "DISQUALIFIERS, IN THE LABEL: this is a 19-event DEMONSTRATION "
      "stopped by construction, not a driven schedule that failed, and "
      "it says NOTHING against one lineage PER ACTOR — V3 is exactly "
      "that and forces.  This is the pin's second variant and it is "
      "reported as a finding at that scope",
      _bs.refusal is not None and _sb_opts == []
      and 'p' not in _sb_kinds and len(_sb_live) == 1,
      f"refusal at prefix {_bs.refusal[1] if _bs.refusal else None} of a "
      f"{_sb_stub}-event stub; prop_options_in_view = {_sb_opts}; menu "
      f"kinds = {_sb_kinds}; live triples = {len(_sb_live)}; the "
      f"one-lineage-per-actor V3 CONFLICT-GRID(4, 4) refusal = "
      f"{BUILT[('CG', 4, 4)][0].refusal}")

_dels_of = {k: [j for j, e in enumerate(BUILT[k][0].H) if e[0] == 'd']
            for k in SWEEP}
_boot_of = {k: (2 * (2 * k[1]) + 2 * k[1] * (k[1] - 1)
                + BUILT[k][0].npad
                if k[0] in ('DG', 'INTER', 'LDG') else 0) for k in SWEEP}
print(f"\n    THE DELIVERY COUNT, per variant (the pin's 'count "
      f"deliveries'):")
for k in SWEEP:
    dd = _dels_of[k]
    inr = [j for j in dd if j >= _boot_of[k]]
    print(f"      {tag_of(k):32s} deliveries {len(dd):3d} total, "
          f"{len(dd) - len(inr):3d} in the bootstrap (first "
          f"{_boot_of[k]} events), {len(inr):3d} IN ROUNDS "
          f"({float(Fr(len(dd), len(BUILT[k][0].H))):.4f} of the record)")
_dg_free = all(len([j for j in _dels_of[k] if j >= _boot_of[k]]) == 0
               for k in SWEEP if k[0] in ('DG', 'INTER', 'LDG'))
_cg_pays = all(len([j for j in _dels_of[k] if j >= _boot_of[k]]) > 0
               for k in SWEEP if k[0] == 'CG')
check("K1b(ii) THE DELIVERY ECONOMICS OF THE k = 4 ROTATION, MEASURED.  "
      "The concurrent (DOUBLE-GRID) schedule pays 2g(g-1) = 24 "
      "deliveries ONCE, in the bootstrap, and ZERO in every round "
      "thereafter — because `View.holdings` gives the minted version to "
      "ALL FOUR proposers and each actor's two axes live on two distinct "
      "unsuperseded bases.  The rotating (CONFLICT-GRID) schedule pays "
      "g(g-1) = 12 deliveries EVERY round, forever.  So at k = 4 the "
      "rotation is not merely more expensive, it is asymptotically more "
      "expensive, and the two-base holding pattern is what buys the "
      "difference",
      _dg_free and _cg_pays,
      f"in-round deliveries: DOUBLE-GRID/INTERLEAVED = 0 at every R "
      f"({_dg_free}); CONFLICT-GRID > 0 at every R ({_cg_pays}); "
      f"bootstrap deliveries at g = 4 = "
      f"{len(_dels_of[HEAD])} of {len(BUILT[HEAD][0].H)} events")

# ---- K1c the conflict budget --------------------------------------------
print("\n[K1c THE CONFLICT BUDGET AT k = 4 — how much of a record CAN be "
      "arbitration?  (pin: 'the budget bound gives <= 1/5 for conflict "
      "groups at k = 4')]")
print("  BOUND (D66's counting theorem of the layer, re-run here, not "
      "re-derived).  An")
print("  arbitration's ckey is a set of k live proposal triples and a "
      "proposal is")
print("  resolved by at most one arbitration in any record, so "
      "#proposals >= k * #arbs")
print("  and the arbitration share of a record is at most 1/(k+1) with k "
      "the smallest")
print("  proposer count in it.  Deliveries only lower it.  The step "
      "D66's round-1")
print("  MINOR 3 supplied: two arbitrations consuming the same proposal "
      "triple share")
print("  that proposer's register, `event_poset` makes them causally "
      "COMPARABLE, and")
print("  the later one's View has the triple in `resolved` — so "
      "`admissible` refuses it.")
print("  ROUND-1 MINOR 1, THE LABEL CORRECTED BEFORE THE NUMBER IS READ.  "
      "The first")
print("  version called 1/5 'the budget bound SATURATED'.  It is not this "
      "record's")
print("  applicable bound: the DOUBLE-GRIDs mint their 2g lineages with "
      "ONE-PROPOSER")
print("  arbitrations, so k_min = 1 and the bound that applies to THIS "
      "record is 1/2.")
print("  Nor is 1/5 'the conflict share': the CONFLICT arbitrations are "
      "16 of the 24")
print("  and their share is 2/15.  What 1/5 equals is the bound that "
      "would apply to a")
print("  record ALL of whose arbitrations had four proposers — which this "
      "one is not.")
print("  The three readings are printed as three columns and never "
      "merged again.")
_bud_ok = True
_norepeat = True
_share_rows = []
for k in SWEEP:
    H = BUILT[k][0].H
    arbs = [e for e in H if e[0] == 'r']
    props = [e for e in H if e[0] == 'p']
    ks = [len({t[0] for t in e[2]}) for e in arbs]
    consumed = sum(ks)
    _cons = Counter(t for e in arbs for t in e[2])
    if any(c > 1 for c in _cons.values()) or len(_cons) != consumed:
        _norepeat = False
    kmin = min(ks)
    kcon = min([x for x in ks if x >= 2], default=kmin)
    sh = arbshare(H)
    bound = Fr(1, kmin + 1)
    if not (consumed == len(props) and sh <= bound):
        _bud_ok = False
    _share_rows.append((tag_of(k), len(H), len(arbs), kmin, sh, bound,
                        kcon, Fr(1, kcon + 1), Counter(ks),
                        Fr(sum(1 for x in ks if x >= 2), len(H))))
for (tg, n, na, kmin, sh, bd, kc, bc, ct, csh) in _share_rows:
    print(f"    {tg:32s} n={n:4d} arbs={na:3d} BY PROPOSER COUNT "
          f"{dict(sorted(ct.items()))} (k_min={kmin}, k_conflict={kc}); "
          f"TOTAL arb share {sh} (~{float(sh):.4f}); CONFLICT-arb share "
          f"{csh} (~{float(csh):.4f}); THIS RECORD'S APPLICABLE bound "
          f"1/(k_min+1) = {bd}"
          + ("   <== attained" if sh == bd else "")
          + (f"; the all-k-proposer bound 1/(k_conflict+1) = {bc}   <== "
             f"the TOTAL share equals it" if sh == bc and bc != bd else ""))
_sat2 = [r[0] for r in _share_rows if r[4] == r[7]]
_k4_share = arbshare(BUILT[HEAD][0].H)
_k4_ks = Counter(len({t[0] for t in e[2]})
                 for e in BUILT[HEAD][0].H if e[0] == 'r')
_k4_conf = Fr(sum(v for kk, v in _k4_ks.items() if kk >= 2),
              len(BUILT[HEAD][0].H))
print(f"    THE k = 4 READING, IN ITS THREE PARTS.  (a) The headline "
      f"record's 24 arbitrations are {_k4_ks[4]} FOUR-proposer conflict "
      f"arbitrations and {_k4_ks[1]} ONE-proposer bootstrap MINTS — not "
      f"'24 arbitrations of four proposers each'.  (b) Its CONFLICT-"
      f"arbitration share is {_k4_conf} (~{float(_k4_conf):.4f}), not "
      f"1/5.  (c) Its k_min is 1, so its OWN applicable budget bound is "
      f"1/2 and the total share {_k4_share} does not saturate it; what "
      f"{_k4_share} equals is 1/(k_conflict+1), the bound for a record "
      f"all of whose arbitrations carry four proposers.  Records whose "
      f"TOTAL share equals 1/(k_conflict+1): {_sat2}.")
_g = HEAD[1]
_boot_ev, _boot_arb = 2 * _g * (_g + 1), 2 * _g
_rnd_ev, _rnd_arb = 2 * _g * _g + 2 * _g, 2 * _g
print(f"    AND THE MECHANISM BEHIND THE 1/(g+1) COINCIDENCE, which the "
      f"first version left unstated (round-1 MINOR 1's 'the real finding "
      f"in this row').  The bootstrap is 2g mint-proposals + 2g "
      f"mint-arbitrations + 2g(g-1) deliveries = 2g(g+1) = {_boot_ev} "
      f"events carrying 2g = {_boot_arb} arbitrations; every round is "
      f"2g^2 proposals + 2g arbitrations = 2g(g+1) = {_rnd_ev} events "
      f"carrying 2g = {_rnd_arb} arbitrations.  BOTH PHASES SIT AT "
      f"1/(g+1) FOR UNRELATED REASONS — the bootstrap because deliveries "
      f"pad it to the same length, the rounds because g^2 proposals feed "
      f"g arbitrations on each axis — so the total is 1/(g+1) at EVERY R, "
      f"which is why the share is R-independent in the table above.  "
      f"Levelling breaks the coincidence exactly as it should: "
      f"LEVELLED-DGRID(4, 2) pads the bootstrap by "
      f"{BUILT[('LDG', 4, 2)][0].npad} idles and its share falls to "
      f"{arbshare(BUILT[('LDG', 4, 2)][0].H)}.")
check("K1c [WHAT THIS GATE MEASURES: not the prose inequality but the "
      "STRICTLY STRONGER per-arbitration equality #proposals = SUM of "
      "proposer counts, together with 'no consumed triple occurs twice'] "
      "THE PROPOSAL-CONSUMPTION EQUALITY HOLDS EXACTLY ON EVERY RECORD, "
      "AND THE ARBITRATION SHARE IS REPORTED IN ITS THREE SEPARATE "
      "READINGS (round-1 MINOR 1).  The k = 4 DOUBLE GRID's TOTAL "
      "arbitration share is exactly 1/5 = 1/(k_conflict + 1) at every R "
      "swept — an exact and R-independent equality with the bound for an "
      "all-four-proposer record, whose mechanism is printed above — "
      "while its CONFLICT-arbitration share is 2/15 and its own "
      "applicable bound, with k_min = 1, is 1/2 and is NOT saturated.  "
      "The first version's 'the budget bound SATURATED' merged the three "
      "and is withdrawn",
      _bud_ok and _norepeat and _k4_share == Fr(1, 5)
      and _k4_conf == Fr(2, 15) and _k4_ks[1] == 8 and _k4_ks[4] == 16
      and len(_sat2) > 0,
      f"records checked = {len(_share_rows)}, proposal-consumption "
      f"equalities = {len(_share_rows)}, repeated consumed triples = 0 "
      f"({_norepeat}), general-bound violations = 0; headline "
      f"arbitrations by proposer count = {dict(sorted(_k4_ks.items()))}; "
      f"TOTAL share = {_k4_share} = 1/(k_conflict+1), CONFLICT share = "
      f"{_k4_conf}, applicable bound 1/(k_min+1) = 1/2")

# ======================================================================
# K2 — THE ATLAS CENSUS
# ======================================================================
print("\n[K2a THE ATLAS CENSUS — every swept record at d = 2 AND d = 3, "
      "with the delivery crystal, the brick and the sprinkling bands "
      "beside them.  Orderings reported BOTH WAYS because the depths "
      "disagree (D60's MINOR-4 lesson)]")


def _inb(pr, d):
    return BAND[d][0] <= pr[d]['h2'] <= BAND[d][1]


def _inb4(pr, d):
    """ROUND-1 MAJOR 4.  K0c computes and prints TWO sprinkling bands at
    each depth — homogeneity (|D| >= 2) and |D| >= 4 — and the first
    version read every in-band verdict on the first alone.  This is the
    second column, and from here on EVERY 'in band' sentence names its
    column and reports both."""
    return W4B[d][0] <= pr[d]['h4'] <= W4B[d][1]


def pos(pr, d):
    return ('in' if _inb(pr, d) else
            ('ABOVE' if pr[d]['h2'] > BAND[d][1] else 'below'))


def pos4(pr, d):
    return ('in' if _inb4(pr, d) else
            ('ABOVE' if pr[d]['h4'] > W4B[d][1] else 'below'))


ALLREC = [(tag_of(k), BUILT[k][1]) for k in SWEEP] + \
         [('DR(8,10,8) [D63 control]', P_DR), ('BRICK(8,14) [D60]', P_BK)]
for (tg, pr) in ALLREC:
    row = []
    for d in (2, 3):
        x = pr[d]
        row.append(f"d={d}: homog {float(x['h2']):.4f}[{pos(pr, d)}] "
                   f"|D|>=4 {float(x['h4']):.4f}[{pos4(pr, d)}] max "
                   f"{x['max']:2d} omega {float(x['om']):.4f}")
    print(f"    {tg:32s} " + "  |  ".join(row))
IN_BAND = {d: [k for k in SWEEP if _inb(BUILT[k][1], d)] for d in (2, 3)}
IN_BAND4 = {d: [k for k in SWEEP if _inb4(BUILT[k][1], d)] for d in (2, 3)}
BOTH_COL = {d: [k for k in SWEEP if _inb(BUILT[k][1], d)
                and _inb4(BUILT[k][1], d)] for d in (2, 3)}
WIDEK = [k for k in SWEEP if BUILT[k][1][2]['h4'] > 0]
_kof = {k: max((len({t[0] for t in e[2]}) for e in BUILT[k][0].H
                if e[0] == 'r'), default=0) for k in SWEEP}
for d in (2, 3):
    print(f"    d = {d}: in the HOMOGENEITY band = {len(IN_BAND[d])} of "
          f"{len(SWEEP)} {[tag_of(k) for k in IN_BAND[d]]}; in the "
          f"|D| >= 4 band = {len(IN_BAND4[d])} "
          f"{[tag_of(k) for k in IN_BAND4[d]]}; in BOTH = "
          f"{len(BOTH_COL[d])} {[tag_of(k) for k in BOTH_COL[d]]}")
print(f"    ROUND-1 MAJOR 4, ACTED ON: K0c computes TWO bands at each "
      f"depth and the first version read every verdict on the first.  "
      f"Both are now printed per record and per depth, and the "
      f"BOTH-COLUMNS column above is the one the flagship verdict is "
      f"read on.")
_flips = [k for k in SWEEP if _inb(BUILT[k][1], 2) != _inb(BUILT[k][1], 3)]
check("K2a THE CENSUS IS REPORTED AT BOTH DEPTHS AND ON BOTH BAND "
      "COLUMNS FOR EVERY RECORD, so every width and homogeneity sentence "
      "in this unit is depth-labelled AND column-labelled (round-1 "
      "MAJOR 4).  The population, the controls and the bands are printed "
      "in full beside the swept records; no record is summarised away",
      len(ALLREC) == len(SWEEP) + 2 and all(
          BUILT[k][1][d]['n'] == len(BUILT[k][0].H)
          for k in SWEEP for d in (2, 3)),
      f"records censused = {len(ALLREC)} (sweep {len(SWEEP)} + 2 "
      f"controls) at both depths and both columns; in the homogeneity "
      f"band at d = 2 = {len(IN_BAND[2])}, at d = 3 = {len(IN_BAND[3])}; "
      f"in the |D|>=4 band at d = 2 = {len(IN_BAND4[2])}, at d = 3 = "
      f"{len(IN_BAND4[3])}; in BOTH columns at d = 3 = "
      f"{[tag_of(k) for k in BOTH_COL[3]]}; band-membership flips "
      f"between the depths at {len(_flips)} records")

# ---- K2b the branching bounds -------------------------------------------
print("\n[K2b THE BRANCHING BOUNDS AT k = 4 — W4b with each record's OWN "
      "measured B, W4c with its OWN measured live Bl, and the refined "
      "depth-2 bound with THE RECORD'S OWN MEASURED k*b (pin K2)]")
print("  W4b (D63): if every event carries at most B registers then "
      "|D_e(d)| <= B^d.")
print("  W4c (D66, PROVED there from the committed layer): the version "
      "register an")
print("  arbitration mints is a BIRTH WIRE with no P-successor, so "
      "|D_e(d)| <= Bl^d with")
print("  Bl the maximum LIVE out-degree, and for an arbitration "
      "b <= #proposers = |regs| - 1.")
print("  THE DEPTH-2 REFINEMENT (D66 BLOCKER 1): the EXACT containment "
      "D_e(2) SUBSET")
print("  succ(e) u U{succ(y) : y in succ(e)} holds always; where no "
      "P-edge out of e skips")
print("  a height layer it sharpens to |D_e(2)| <= SUM_y b(y) <= "
      "b(e)*Bl <= k*Bl <= k^2.")
print("  At k = 4 that ceiling is 16 — INSIDE the sprinkling range "
      f"[{MXB[2][0]}, {MXB[2][1]}].")
_w4_ok = True
_mint_ok = True
_ref_ok = True
_sharp_exc = 0
_sharp_explained = True
_bl_rows = []
for k in SWEEP + [('CTRL-DR',), ('CTRL-BK',)]:
    if k[0].startswith('CTRL'):
        H = (b_dr if k[0] == 'CTRL-DR' else b_bk).H
        pr = P_DR if k[0] == 'CTRL-DR' else P_BK
        tg = 'DR(8,10,8)' if k[0] == 'CTRL-DR' else 'BRICK(8,14)'
    else:
        H, pr, tg = BUILT[k][0].H, BUILT[k][1], tag_of(k)
    C = poset_of(H)
    Bmax = max(len(regs_of(e)) for e in H)
    su = succ_of(H)
    bdeg = {j: len(su[j]) for j in range(len(H))}
    Bl = max(bdeg.values())
    _hs = heights(C)
    _maxkb = 0
    for e in range(len(H)):
        d2 = len(_skyB(C, _hs, e, 2))
        reach = set(su[e])
        for y in su[e]:
            reach |= su[y]
        if d2 > len(reach):
            _ref_ok = False
        _sum = sum(bdeg[y] for y in su[e])
        _maxkb = max(_maxkb, _sum)
        if d2 > _sum:
            _sharp_exc += 1
            if any(_hs[y] == _hs[e] + 1 for y in su[e]):
                _sharp_explained = False
    occ = Counter(r for e in H for r in regs_of(e) if not isinstance(r, str))
    vmulti = sum(1 for r, c in occ.items() if c > 1)
    if vmulti:
        _mint_ok = False
    kmax = max([len({t[0] for t in e[2]}) for e in H if e[0] == 'r'],
               default=0)
    _lt = sum(1 for j, op in enumerate(H) if op[0] == 'r'
              and bdeg[j] < len({t[0] for t in op[2]}))
    for d in (2, 3):
        if pr[d]['max'] > Bmax ** d or pr[d]['max'] > Bl ** d:
            _w4_ok = False
    _bl_rows.append((tg, Bmax, Bl, kmax, pr[2]['max'], pr[3]['max'],
                     vmulti, _lt, _maxkb))
for (tg, Bm, Bl, km, m2, m3, vm, lt, mkb) in _bl_rows:
    print(f"    {tg:32s} B={Bm} (W4b {Bm**2}) live Bl={Bl} (W4c "
          f"{Bl**2}) k={km} (k^2={km**2}); MEASURED max SUM_y b(y) = "
          f"{mkb:2d}; measured max|D| d2={m2:2d} d3={m3:2d}; version "
          f"registers occurring twice = {vm}; arbitrations with b < k = "
          f"{lt}")
check("K2b BOTH BOUNDS HOLD ON EVERY RECORD AT BOTH DEPTHS, THE EXACT "
      "CONTAINMENT HOLDS EVENT BY EVENT, AND THE SHARP SUM FORM IS GATED "
      "WITH THE RECORD'S OWN MEASURED k*b.  Across every record built "
      "here every version register occurs in EXACTLY ONE event's "
      "`regs_of` — W4c's dead-wire step — so an arbitration's live "
      "out-degree is at most its proposer count.  The exceptions to the "
      "SHARP form are counted AND characterised (D66's repair): they are "
      "exactly the events all of whose P-successors sit two or more "
      "layers above them",
      _w4_ok and _mint_ok and _ref_ok and _sharp_explained,
      f"records checked = {len(_bl_rows)}, W4b/W4c violations = 0, "
      f"exact-containment violations = 0 ({_ref_ok}), events where the "
      f"SHARP sum form does not apply = {_sharp_exc} (every one has NO "
      f"P-successor at height + 1: {_sharp_explained}), version "
      f"registers occurring more than once = 0")

# ---- K2c the interior control -------------------------------------------
print("\n[K2c THE INTERIOR CONTROL (D60's C7 excision, D66's "
      "`interior_of`) ON EVERY SWEPT RECORD, AT BOTH DEPTHS AND ON BOTH "
      "BAND COLUMNS — is any width or any band membership an ENDS "
      "artefact?]")
print("  WHAT THE INTERIOR IS, AND IS NOT (round-1 MINOR 6).  "
      "`interior_of` returns the")
print("  FULL closure and a SUBSET of events; `profile` then averages "
      "over that subset")
print("  while every chart is still computed on the WHOLE record — a "
      "base at height")
print("  hi - 3 still reads directions at hi - 1, inside the excised "
      "layers.  So the")
print("  interior is a CONDITIONAL AVERAGE OVER A POPULATION OF EVENTS: "
      "not a record,")
print("  not a sub-poset, and NOT AN OBJECT.  The word 'object' is "
      "withdrawn from")
print("  every interior sentence in this unit.  For the same reason 'no "
      "wide chart is")
print("  a boundary artefact' tests that the BASE is off the boundary; "
      "the chart's")
print("  CONTENTS are not excised, and the gate says only what it "
      "measures.")


def _pos(h, d):
    return ('IN ' if BAND[d][0] <= h <= BAND[d][1]
            else ('ABOVE' if h > BAND[d][1] else 'below'))


def _pos4(h, d):
    return ('IN ' if W4B[d][0] <= h <= W4B[d][1]
            else ('ABOVE' if h > W4B[d][1] else 'below'))


INT = {}
_moved_in = []
for k in SWEEP:
    C, popn = interior_of(BUILT[k][0].H)
    pi = profile(C, popn)
    INT[k] = pi
    pf = BUILT[k][1]
    cells = []
    for d in (2, 3):
        cells.append(f"d={d} homog {float(pf[d]['h2']):.4f}"
                     f"[{_pos(pf[d]['h2'], d)}]"
                     f" -> {float(pi[d]['h2']):.4f}[{_pos(pi[d]['h2'], d)}]"
                     f" ; |D|>=4 {float(pf[d]['h4']):.4f}"
                     f"[{_pos4(pf[d]['h4'], d)}] -> "
                     f"{float(pi[d]['h4']):.4f}[{_pos4(pi[d]['h4'], d)}]")
        if (not (BAND[d][0] <= pf[d]['h2'] <= BAND[d][1])
                and BAND[d][0] <= pi[d]['h2'] <= BAND[d][1]):
            _moved_in.append((tag_of(k), d))
    print(f"    {tag_of(k):32s} n {pf[2]['n']:4d}->{pi[2]['n']:4d}  "
          + "  |  ".join(cells)
          + f"  max|D| d2 {pf[2]['max']:2d}->{pi[2]['max']:2d} d3 "
          f"{pf[3]['max']:2d}->{pi[3]['max']:2d}")
_int_ge = all(INT[k][d]['h2'] >= BUILT[k][1][d]['h2']
              for k in INT for d in (2, 3))
_int_up = sum(1 for k in INT for d in (2, 3)
              if INT[k][d]['h2'] > BUILT[k][1][d]['h2'])
_int_maxkept = all(INT[k][d]['max'] == BUILT[k][1][d]['max']
                   for k in INT for d in (2, 3))
_int_both3 = [tag_of(k) for k in SWEEP
              if _inb(INT[k], 3) and _inb4(INT[k], 3)]
print(f"    EXCISION MOVES A RECORD INTO THE HOMOGENEITY BAND AT: "
      f"{_moved_in}")
print(f"    INTERIOR POPULATIONS IN BOTH d = 3 COLUMNS AT ONCE: "
      f"{_int_both3}")
check("K2c THE WIDTH IS THE CIRCUIT'S, NOT THE PREFIX'S — AND THE "
      "INTERIOR IS A POPULATION, NOT AN OBJECT (round-1 MINOR 6, in the "
      "label and not only in the prose).  Excising the bottom two and "
      "top three height layers leaves max |D| unchanged at both depths "
      "on every swept record — so no wide chart anywhere in this unit, "
      "including the k = 4 charts, has a base on the boundary — and it "
      "never LOWERS homogeneity, so the band verdicts below are reported "
      "with their interior values beside them.  WHAT THE EXCISION DOES "
      "NOT DO: it restricts the averaging POPULATION and leaves the "
      "poset and every chart's CONTENTS whole, so an interior figure is "
      "a conditional average over a subset of events and is never called "
      "a record or an object here",
      _int_maxkept and _int_ge and len(INT) == len(SWEEP),
      f"records controlled = {len(INT)} of {len(SWEEP)} at BOTH depths "
      f"and BOTH columns; (record, depth) cells where interior "
      f"homogeneity strictly rises = {_int_up} of {2 * len(INT)}; never "
      f"falls = {_int_ge}; interior max|D| = full max|D| everywhere = "
      f"{_int_maxkept}; cells the excision moves INTO the homogeneity "
      f"band = {len(_moved_in)}; interior populations inside BOTH d = 3 "
      f"columns = {_int_both3}")

# ======================================================================
# K3 — THE WIDTH VERDICT
# ======================================================================
print("\n[K3 THE WIDTH VERDICT — max |D| at d = 2 against the sprinkling "
      f"range [{MXB[2][0]}, {MXB[2][1]}] and the k = 4 bound k^2 = 16]")
WID = {}
for k in SWEEP:
    C = poset_of(BUILT[k][0].H)
    hs = heights(C)
    WID[k] = Counter(len(_skyB(C, hs, e, 2)) for e in range(len(C)))
    print(f"    {tag_of(k):32s} k={_kof[k]}  width histogram at d = 2: "
          f"{dict(sorted(WID[k].items()))}")
_maxw = {k: BUILT[k][1][2]['max'] for k in SWEEP}
_maxw3 = {k: BUILT[k][1][3]['max'] for k in SWEEP}
GRADE = [k for k in SWEEP if _maxw[k] >= MXB[2][0]]
print(f"    max |D| at d = 2 by proposer count k: "
      + ", ".join(f"{tag_of(k)} k={_kof[k]} -> {_maxw[k]}" for k in SWEEP))
print(f"    RECORDS AT OR ABOVE THE SPRINKLING FLOOR ({MXB[2][0]}): "
      f"{[tag_of(k) for k in GRADE]}")


def witness(kk, tagline, want, paths='per-chart'):
    """The D66-round standard: a width claim is EXHIBITED event by
    event, its chart read from the COMMITTED d47a `sky`, every direction
    verified ordered after the base in the COMMITTED `poset_of` order
    and sitting exactly two height layers above it, and every
    direction's P-paths printed."""
    Hw = BUILT[kk][0].H
    Cw = poset_of(Hw)
    hw = heights(Cw)
    su = succ_of(Hw)
    bases = sorted(e for e in range(len(Cw))
                   if len(sky(Cw, e, 'B', 2)[0]) == want)
    outp = out_reg(Hw, 'tuple')
    _dsets = {frozenset(sky(Cw, e, 'B', 2)[0]) for e in bases}
    _d1sets = {tuple(sorted(su[e])) for e in bases}
    print(f"\n    {tagline} — {tag_of(kk)}: {len(bases)} BASES whose "
          f"chart has width {want}, at events {bases}")
    print(f"      ROUND-1 MINOR 2, SAID BEFORE THE WITNESSES: those "
          f"{len(bases)} bases carry {len(_dsets)} DISTINCT DIRECTION "
          f"SET(S) and {len(_d1sets)} distinct D(1) set(s).  "
          + ("They are the SAME chart seen from several bases — the "
             "record contains ONE width-%d direction set, not %d of them, "
             "and the first version's 'three charts of width 16' is "
             "literally true and materially misleading."
             % (want, len(bases)) if len(_dsets) == 1 else
             "The direction sets are distinct."))
    ok = len(bases) > 0
    _seen = set()
    for ew in bases:
        dirs, rows = sky(Cw, ew, 'B', 2)
        W = words_from(outp, hw, ew, 2)
        _new = frozenset(dirs) not in _seen
        _seen.add(frozenset(dirs))
        kw = len({t[0] for t in Hw[ew][2]}) if Hw[ew][0] == 'r' else 0
        okc = (len(set(dirs)) == want and len(dirs) == want
               and set(W) == set(dirs)
               and all(Cw[ew][f] and hw[f] == hw[ew] + 2 for f in dirs))
        ok = ok and okc
        print(f"      base {ew:3d}: {Hw[ew][0]}-event by {Hw[ew][1]}, "
              f"height {hw[ew]}, {len(regs_of(Hw[ew]))} registers "
              f"({kw} proposers), live out-degree b(e) = {len(su[ew])}; "
              f"D(1) = {sorted(su[ew])} kinds "
              f"{[Hw[f][0] for f in sorted(su[ew])]} out-degrees "
              f"{[len(su[f]) for f in sorted(su[ew])]}; SUM_y b(y) = "
              f"{sum(len(su[y]) for y in su[ew])}, k^2 = {kw * kw}")
        print(f"        |D| = {len(dirs)} directions {sorted(dirs)}; all "
              f"distinct / ordered after the base in the committed "
              f"poset / at height + 2 = {okc}"
              + ("" if _new else "   [SAME DIRECTION SET as a base above "
                                 "— P-paths not repeated]"))
        if not _new and paths == 'per-chart':
            continue
        for f in sorted(dirs):
            print(f"          direction {f:3d}: kind {Hw[f][0]} by "
                  f"{Hw[f][1]}, height {hw[f]} (= {hw[ew]} + "
                  f"{hw[f]-hw[ew]}), ordered after base = {Cw[ew][f]}; "
                  f"P-paths (raw ; role) = "
                  + " | ".join(f"{[str(x)[:12] for x in w]} ; {o}"
                               for (w, o) in sorted(W.get(f, ()), key=repr)))
    return ok, bases


_wit_ok, _wit_bases = witness(
    HEAD, "THE WIDTH WITNESSES, EXHIBITED EVENT BY EVENT (the D66-round "
    "standard: a width claim is not an instrument artefact until it is "
    "read off the committed sky and the committed order)", _maxw[HEAD])
_fwit_ok, _fwit_bases = witness(
    FLAG, "THE SAME, ON THE ROUND-1 FLAGSHIP — the record that is IN "
    "BAND AS A WHOLE RECORD (K4) while carrying k^2.  One direction set "
    "per round is exhibited with its P-paths; the repeats are named as "
    "repeats", _maxw[FLAG])
print(f"\n    THE UNFILLED SUCCESSOR CENSUS (the pin's K-II ask, "
      f"reported whichever outcome fires): for every ARBITRATION of the "
      f"headline record, how much of its own SUM_y b(y) budget the chart "
      f"actually realizes at d = 2:")
_Hh = BUILT[HEAD][0].H
_Ch = poset_of(_Hh)
_hh = heights(_Ch)
_suh = succ_of(_Hh)
_gap_rows = []
for e in range(len(_Hh)):
    if _Hh[e][0] != 'r':
        continue
    kk_ = len({t[0] for t in _Hh[e][2]})
    if kk_ < 2:
        continue
    sm = sum(len(_suh[y]) for y in _suh[e])
    d2 = len(_skyB(_Ch, _hh, e, 2))
    _gap_rows.append((e, kk_, len(_suh[e]), sm, d2, kk_ * kk_,
                      sorted({_hh[y] - _hh[e] for y in _suh[e]})))
_full = [r for r in _gap_rows if r[4] == r[3]]
_short = [r for r in _gap_rows if r[4] < r[3]]
_ceil = [r for r in _gap_rows if r[4] == r[5] and r[4] > 0]
print(f"      {len(_gap_rows)} conflict arbitrations: {len(_full)} "
      f"REALIZE THEIR WHOLE SUM_y b(y) BUDGET (|D(2)| = SUM_y b(y), "
      f"including the ones whose budget is itself small), {len(_short)} "
      f"FALL SHORT of it, and {len(_ceil)} ATTAIN THE CEILING k^2 = 16.  "
      f"The three counts are different questions and are reported "
      f"separately.")
print(f"      {'base':>5s} {'k':>2s} {'b(e)':>4s} {'SUM b(y)':>8s} "
      f"{'|D(2)|':>6s} {'k^2':>4s}  successor height offsets")
for r in _gap_rows:
    print(f"      {r[0]:5d} {r[1]:2d} {r[2]:4d} {r[3]:8d} {r[4]:6d} "
          f"{r[5]:4d}  {r[6]}" + ("   <== SATURATES k^2"
                                  if r[4] == r[5] and r[4] > 0 else ""))
_reason = sorted({tuple(r[6]) for r in _short})
print(f"      THE SHORTFALLS, CHARACTERISED: the arbitrations that do "
      f"not realize SUM_y b(y) have successor height offsets in "
      f"{_reason} — a chart counts only directions at EXACTLY height "
      f"+ 2, so a successor that skips a layer (offset >= 2) contributes "
      f"its own successors at height + 3 or beyond and nothing at "
      f"depth 2.  Where every successor sits at offset 1 the whole "
      f"budget is realized.")
_meanw = {k: BUILT[k][1][2]['mean'] for k in SWEEP}
_sprmean = (min(SPR[k][2]['mean'] for k in SPR),
            max(SPR[k][2]['mean'] for k in SPR))
print(f"\n    ROUND-1 MAJOR 2(b), THE OTHER WIDTH COLUMNS, PRINTED BESIDE "
      f"THE max.  `max |D|` is the ONLY column on which the k = 4 record "
      f"touches the sprinkling population at d = 2.  Its mean chart is "
      f"{float(_meanw[HEAD]):.2f} directions against the sprinklings' "
      f"{float(_sprmean[0]):.2f}-{float(_sprmean[1]):.2f}; its "
      f"homogeneity {float(BUILT[HEAD][1][2]['h2']):.4f} and its "
      f"|D| >= 4 {float(BUILT[HEAD][1][2]['h4']):.4f} are BELOW both "
      f"d = 2 bands, whole and interior; and "
      f"{WID[HEAD].get(_maxw[HEAD], 0)} events of {len(BUILT[HEAD][0].H)} "
      f"carry the {_maxw[HEAD]}-wide chart.  The claim the measurement "
      f"supports is about the MAXIMUM, at ONE depth, at ONE k.")
check("K3a [THE WIDTH VERDICT, SCOPED TO THE STATISTIC IT MEASURES "
      "(round-1 MAJOR 2)] " + (
      f"**THE MAXIMUM CHART WIDTH REACHES A VALUE INSIDE THE HULL OF THE "
      f"SPRINKLING MAXIMA.**  The k = 4 DOUBLE GRID carries max |D| = "
      f"{_maxw[HEAD]} at d = 2 — at or above the genuine sprinkling "
      f"floor of {MXB[2][0]} and inside the measured hull "
      f"[{MXB[2][0]}, {MXB[2][1]}], which is the hull of the M21 cluster "
      f"[{DIMR[('M21', 2)][0]}, {DIMR[('M21', 2)][1]}] and the M31 "
      f"cluster [{DIMR[('M31', 2)][0]}, {DIMR[('M31', 2)][1]}]: 16 sits "
      f"in the 3+1 cluster and OUTSIDE the 2+1 one, and the gate says so "
      f"rather than saying 'inside the sprinkling range'.  Every "
      f"witnessing chart is read from the COMMITTED d47a `sky`, every "
      f"direction verified ordered after the base in the COMMITTED "
      f"`poset_of` order and sitting exactly two height layers above it, "
      f"and every distinct chart's P-paths printed.  The base is an "
      f"arbitration over FOUR DISTINCT PROPOSERS whose four depth-1 "
      f"successors are themselves four-proposer ARBITRATIONS.  WHAT IS "
      f"NOT CLAIMED (round-1 MAJOR 2c): not that the mechanism is "
      f"sprinkling-grade — by K3d it delivers k^2 at every k anyone has "
      f"built, 25 at k = 5 and 36 at k = 6, ABOVE the whole hull — so 16 "
      f"is a PARAMETER PICKED, not a coincidence discovered, and 'the "
      f"first sprinkling-grade width in the campaign' is withdrawn as a "
      f"milestone claim about the mechanism"
      if _maxw[HEAD] >= MXB[2][0] else
      f"**THE WIDTH STAYS BELOW THE SPRINKLING FLOOR.**  The k = 4 "
      f"DOUBLE GRID carries max |D| = {_maxw[HEAD]} at d = 2 against the "
      f"floor {MXB[2][0]}") + ".  The predicate is the width census "
      "itself, computed from the sweep and compared with the RE-RUN "
      "sprinkling hull and its two clusters, not with a typed number",
      _wit_ok and len(_wit_bases) > 0 and _fwit_ok and len(_fwit_bases) > 0,
      f"headline max |D| = {_maxw[HEAD]} at d = 2 ({_maxw3[HEAD]} at "
      f"d = 3) vs sprinkling hull {MXB[2]} = M21 {DIMR[('M21', 2)]} u "
      f"M31 {DIMR[('M31', 2)]}; witnessing bases = {len(_wit_bases)} "
      f"carrying 1 direction set, all verified against the committed sky "
      f"and order = {_wit_ok}; the same on the flagship "
      f"{tag_of(FLAG)}: {len(_fwit_bases)} bases, verified = "
      f"{_fwit_ok}; mean |D| headline {float(_meanw[HEAD]):.2f} vs "
      f"sprinklings {float(_sprmean[0]):.2f}-{float(_sprmean[1]):.2f}; "
      f"records at or above the sprinkling floor = "
      f"{len(GRADE)} of {len(SWEEP)}")

# ---- K3b the smallest witnesses, and D66's blueprint corrected ----------
print("\n[K3b THE SMALLEST WITNESSES — ARBCHAIN*(m, k), and a CORRECTION "
      "TO D66's OWN BLUEPRINT.  D66's `arbchain(m, k)` docstring claims "
      "|D_e(2)| = k*m + 2*(k - m) 'sweeps the WHOLE interval [2k, k^2] "
      "as m runs 0..k', but its secondary arbitrations are hardcoded to "
      "THREE proposers and its gate only ever ran k = 3.  Both families "
      "are built here and both are measured]")
AC = {}
for k in (3, 4, 5):
    for m in range(k + 1):
        bb, ee = arbchain_k(m, k)
        Cc = poset_of(bb.H)
        sc = succ_of(bb.H)
        D2 = sky(Cc, ee, 'B', 2)[0]
        AC[('star', m, k)] = (bb, ee, len(D2), k * m + 2 * (k - m),
                              [bb.H[f][0] for f in sorted(sc[ee])],
                              [len(sc[f]) for f in sorted(sc[ee])],
                              max(len(v) for v in sc.values()))
        if k in (4, 5):
            b2, e2 = d66_arbchain(m, k)
            C2 = poset_of(b2.H)
            s2 = succ_of(b2.H)
            AC[('d66', m, k)] = (b2, e2, len(sky(C2, e2, 'B', 2)[0]),
                                 k * m + 2 * (k - m),
                                 [b2.H[f][0] for f in sorted(s2[e2])],
                                 [len(s2[f]) for f in sorted(s2[e2])],
                                 max(len(v) for v in s2.values()))
for fam in ('star', 'd66'):
    for k in (3, 4, 5):
        rows = [(m, AC[(fam, m, k)]) for m in range(k + 1)
                if (fam, m, k) in AC]
        if not rows:
            continue
        nm = "ARBCHAIN*" if fam == 'star' else "d66 ARBCHAIN"
        for (m, r) in rows:
            print(f"    {nm}(m={m}, k={k}): n={len(r[0].H):3d} actors="
                  f"{len(r[0].actors):2d} hits={r[0].maxhits} "
                  f"successors {r[4]} out-degrees {r[5]}; |D_e(2)| = "
                  f"{r[2]:2d}  (refined prediction k*m + 2*(k-m) = "
                  f"{r[3]:2d}"
                  + (", MET" if r[2] == r[3] else ", NOT MET") + f"); "
                  f"Bl = {r[6]}, W4c bound {r[6] ** 2}")
_star34 = all(AC[('star', m, k)][2] == AC[('star', m, k)][3]
              for k in (3, 4) for m in range(k + 1))
_star3_vals = [AC[('star', m, 3)][2] for m in range(4)]
_d66_k4 = [AC[('d66', m, 4)][2] for m in range(5)]
_d66_pred = [3 * m + 2 * (4 - m) for m in range(5)]
_star5 = [AC[('star', m, 5)][2] for m in range(6)]
_star5_pred = [AC[('star', m, 5)][3] for m in range(6)]
print(f"    ARBCHAIN* at k = 3 gives {_star3_vals} — D66's committed "
      f"6, 7, 8, 9 exactly, so the corrected blueprint is a strict "
      f"generalization that AGREES with its parent where the parent was "
      f"gated.")
print(f"    ARBCHAIN* at k = 4 gives {[AC[('star', m, 4)][2] for m in range(5)]}"
      f" = k*m + 2*(k-m) = 8, 10, 12, 14, 16: the WHOLE interval "
      f"[2k, k^2] = [8, 16] is occupied and W4c's k^2 = 16 is SATURATED "
      f"in a {len(AC[('star', 4, 4)][0].H)}-event record over "
      f"{len(AC[('star', 4, 4)][0].actors)} actors.")
print(f"    D66's OWN `arbchain` at k = 4 gives {_d66_k4}, which is "
      f"{_d66_pred} = 3m + 2(k - m) and NOT k*m + 2*(k - m): its "
      f"secondary arbitrations have THREE proposers whatever k is (its "
      f"out-degree columns above read 3, never 4).  D66's NOTE and D66's "
      f"GATE are both k = 3 statements and neither is touched; what is "
      f"corrected here is the BLUEPRINT's claim to general k.")
print(f"    AT k = 5 NEITHER ARBCHAIN FAMILY REACHES THE CEILING: "
      f"ARBCHAIN* gives {_star5} against the refined prediction "
      f"{_star5_pred} and the ceiling k^2 = 25.  THE CAUSE, WHICH IS "
      f"INSIDE ARBCHAIN*'s OWN BOOTSTRAP AND NOT IN THE BOUND: S_i "
      f"supplies A_i AND all k - 2 helpers T_ij by a SERIAL delivery "
      f"chain on register S_i, so p(S_i, Y_i, 0) sits k - 1 layers above "
      f"its mint and at k = 5 two of the five secondary arbitrations "
      f"land at height offset 2 from THE ARBITRATION — and a chart "
      f"counts only what sits at EXACTLY height + 2.  That is a property "
      f"of THE ORDERING OF A BOOTSTRAP.  The first version filed it as "
      f"an open residue and reopened D66's residue 6; ROUND 1 REMOVED IT "
      f"INSTEAD, in one levelling pass, and K3d below is the result: the "
      f"ceiling is reached at k = 5 AND k = 6.")
check("K3b THE REFINED BOUND IS EXACTLY RIGHT AT k = 4 AND THE WHOLE "
      "INTERVAL [2k, k^2] = [8, 16] IS OCCUPIED BY FORCED, "
      "MENU-OFFERED RECORDS — 8, 10, 12, 14, 16 at m = 0..4 — while "
      "D66's own ARBCHAIN blueprint, whose docstring claims the same "
      "formula for general k, realizes 3m + 2(k - m) instead.  Both "
      "families are printed; the correction is to the blueprint's "
      "generality, not to any gated D66 number (at k = 3 the two "
      "agree exactly: 6, 7, 8, 9)",
      _star34 and _star3_vals == [6, 7, 8, 9]
      and _d66_k4 == _d66_pred and _d66_k4 != [8, 10, 12, 14, 16]
      and all(r[0].maxhits == 1 and not r[0].refusal for r in AC.values()),
      f"ARBCHAIN* meets k*m + 2*(k-m) at every m for k = 3 and k = 4 = "
      f"{_star34}; k = 3 values {_star3_vals}; k = 4 values "
      f"{[AC[('star', m, 4)][2] for m in range(5)]}; d66's k = 4 values "
      f"{_d66_k4} = 3m + 2(k-m) {_d66_pred}; k = 5 values {_star5} vs "
      f"prediction {_star5_pred}; refusals over all "
      f"{len(AC)} chains = 0")

# ---- K3d the k-CEILING LADDER (round-1 MAJOR 1) --------------------------
print("\n[K3d THE CEILING LADDER — ARBCHAIN**(k), THE ROUND-1 REFEREE'S "
      "CONSTRUCTION, carried here with credit and gated like any other "
      "object.  It is ARBCHAIN*(k, k) with every actor register "
      "HEIGHT-LEVELLED by the grammar's OWN ('n', a) idle event — the "
      "same event kind the committed blueprints already use for their "
      "tails — before the proposals, so that all k depth-1 consumers sit "
      "at exactly height + 1.  Nothing else changes: no new lineage, no "
      "delivery, no arbitration]")
AC2 = {}
t_ac2 = time.time()
for k in (3, 4, 5, 6):
    t_k = time.time()
    bb, ee = arbchain_k(k, k, level=True)
    Cc = poset_of(bb.H)
    hsc = heights(Cc)
    sc = succ_of(bb.H)
    D2 = sky(Cc, ee, 'B', 2)[0]
    offs = sorted(hsc[y] - hsc[ee] for y in sc[ee])
    AC2[k] = {'b': bb, 'e': ee, 'C': Cc, 'h': hsc, 'su': sc, 'D2': D2,
              'offs': offs, 'outdeg': [len(sc[f]) for f in sorted(sc[ee])],
              'kinds': [bb.H[f][0] for f in sorted(sc[ee])],
              'Bl': max(len(v) for v in sc.values()), 't': time.time() - t_k}
    print(f"    ARBCHAIN**(k={k}): n={len(bb.H):3d} actors="
          f"{len(bb.actors):2d} ({bb.npad} levelling idles to common "
          f"height {bb.plevel}) hits={bb.maxhits} refusal={bb.refusal}; "
          f"h(e)={hsc[ee]}; D(1) = {len(sc[ee])} x '"
          f"{AC2[k]['kinds'][0]}' at height offsets {offs}, out-degrees "
          f"{AC2[k]['outdeg']}; SUM_y b(y) = "
          f"{sum(len(sc[y]) for y in sc[ee])}; |D_e(2)| = "
          f"{len(D2):2d}  vs  k^2 = {k * k:2d}"
          + ("   <== THE CEILING, REALIZED" if len(D2) == k * k else
             "   <== SHORT") + f"; Bl = {AC2[k]['Bl']}, W4c bound "
          f"{AC2[k]['Bl'] ** 2}  [{AC2[k]['t']:.1f}s]")
    sys.stdout.flush()
def _closure_of_P(su, n):
    """The transitive closure of THIS UNIT's own immediate-successor
    relation P (`succ_of`), built independently of `event_poset`'s own
    ancestor bookkeeping — the round-1 referee's check, and D64's C0b
    form: closure(P) must BE the committed order."""
    reach = [set() for _ in range(n)]
    for i in range(n - 1, -1, -1):
        r = set()
        for j in su[i]:
            r.add(j)
            r |= reach[j]
        reach[i] = r
    return [[j in reach[i] for j in range(n)] for i in range(n)]


# the k = 5 record verified to the D66-round standard, against the
# COMMITTED sky, the COMMITTED order and the COMMITTED heights
_V = AC2[5]
_vb, _ve, _vC, _vh = _V['b'], _V['e'], _V['C'], _V['h']
_vP = _closure_of_P(_V['su'], len(_vb.H))
_v_close = (_vP == _vC)
_v_heights = (heights(_vP) == _vh)
_v_dirs = sorted(sky(_vC, _ve, 'B', 2)[0])
_v_ok = (len(set(_v_dirs)) == 25 and len(_v_dirs) == 25
         and all(_vC[_ve][f] for f in _v_dirs)
         and all(_vh[f] == _vh[_ve] + 2 for f in _v_dirs))
_v_w4c = 0
for e in range(len(_vC)):
    for d in (1, 2, 3):
        if len(_skyB(_vC, _vh, e, d)) > _V['Bl'] ** d:
            _v_w4c += 1
_v_occ = Counter(r for e in _vb.H for r in regs_of(e) if not isinstance(r, str))
_v_multi = sum(1 for r, c in _v_occ.items() if c > 1)
_vout = out_reg(_vb.H, 'tuple')
_vW = words_from(_vout, _vh, _ve, 2)
print(f"\n    ARBCHAIN**(5), VERIFIED TO THE D66-ROUND STANDARD (the "
      f"k = 5 record that reaches 25):")
print(f"      the transitive closure of THIS UNIT's own P == the "
      f"committed `poset_of` order on all {len(_vb.H)} events = "
      f"{_v_close}; the heights of that closure == the committed heights "
      f"= {_v_heights}")
print(f"      |D_e(2)| read from the COMMITTED d47a `sky(C, e, 'B', 2)` "
      f"= {len(_v_dirs)}; the 25 directions {_v_dirs}")
print(f"      all pairwise distinct / ALL ordered after the base in the "
      f"COMMITTED order / ALL at height exactly {_vh[_ve]} + 2 = "
      f"{_vh[_ve] + 2} = {_v_ok}")
for f in _v_dirs:
    print(f"        direction {f:3d}: kind {_vb.H[f][0]} by {_vb.H[f][1]}, "
          f"height {_vh[f]}, ordered after base = {_vC[_ve][f]}; P-paths "
          f"(raw ; role) = "
          + " | ".join(f"{[str(x)[:12] for x in w]} ; {o}"
                       for (w, o) in sorted(_vW.get(f, ()), key=repr)))
print(f"      Bl = {_V['Bl']}; W4c violations at d = 1, 2, 3 = {_v_w4c}; "
      f"version registers occurring more than once = {_v_multi}")
_ladder_ok = all(len(AC2[k]['D2']) == k * k for k in AC2)
_ladder_off = all(AC2[k]['offs'] == [1] * k for k in AC2)
print(f"\n    THE LADDER, READ.  |D_e(2)| = "
      f"{ {k: len(AC2[k]['D2']) for k in sorted(AC2)} } against k^2 = "
      f"{ {k: k * k for k in sorted(AC2)} }.  The k^2 ceiling is "
      f"REALIZED AT EVERY k TRIED, k = 3, 4, 5, 6, and the mechanism is "
      f"the one the first version's own refined sentence names — THE k "
      f"DEPTH-1 CONSUMERS MUST SIT AT HEIGHT + 1 — reached here by "
      f"LEVELLING, with no phase separation of any kind in these records "
      f"(round-1 MAJOR 1's correction to claim (iv)).  So height "
      f"alignment is a DESIGN REQUIREMENT THE GRAMMAR'S OWN IDLES "
      f"SATISFY, not an obstruction; D66's residue 6 stays CLOSED and is "
      f"NOT reopened; and the k-ceiling question is closed at every k "
      f"anyone has built.  WHAT REMAINS OPEN, stated exactly: whether a "
      f"TILING k = 5 schedule — a DOUBLE-GRID(5, R) — exists and reaches "
      f"25.  ARBCHAIN** is a SMALLEST-WITNESS record of exactly the "
      f"class ARBCHAIN* is, not a tiling crystal, and neither this unit "
      f"nor round 1 has built one.")
check("K3d [ROUND-1 MAJOR 1 — THE CEILING IS REACHED AT EVERY k TRIED] "
      "**k^2 IS REALIZED AT k = 3, 4, 5 AND 6 BY FORCED, MENU-OFFERED "
      "RECORDS.**  ARBCHAIN**(k) — the round-1 referee's construction, "
      "ARBCHAIN*(k, k) height-levelled by the grammar's own idle event — "
      "carries |D_e(2)| = 9, 16, 25, 36 with all k depth-1 consumers at "
      "height offset exactly 1 and out-degree exactly k.  The k = 5 "
      "member is verified to the D66-round standard: its chart is read "
      "from the COMMITTED sky, its 25 directions are pairwise distinct, "
      "all ordered after the base in the COMMITTED order and all at "
      "height exactly + 2, with P-paths printed; the transitive closure "
      "of THIS UNIT's own P IS the committed order on all 157 events, "
      "and its heights are the committed heights; W4c holds at d = 1, 2, "
      "3 with zero violations and every version register occurs in "
      "exactly one `regs_of`.  THE FIRST VERSION'S '`k^2` IS UNREALIZED "
      "AT k = 5', 'the ceiling is not reached at k = 5' AND ITS "
      "REOPENING OF D66's RESIDUE 6 ARE ALL WITHDRAWN: what it measured "
      "was ARBCHAIN*'s bootstrap ORDERING",
      _ladder_ok and _ladder_off and _v_ok and _v_close and _v_heights
      and _v_w4c == 0 and _v_multi == 0
      and all(AC2[k]['b'].maxhits == 1 and not AC2[k]['b'].refusal
              for k in AC2)
      and all(AC2[k]['outdeg'] == [k] * k for k in AC2),
      f"|D_e(2)| by k = { {k: len(AC2[k]['D2']) for k in sorted(AC2)} } "
      f"= k^2 everywhere ({_ladder_ok}); depth-1 height offsets all "
      f"[1,...,1] ({_ladder_off}); out-degrees "
      f"{ {k: AC2[k]['outdeg'] for k in sorted(AC2)} }; event counts "
      f"{ {k: len(AC2[k]['b'].H) for k in sorted(AC2)} }; k = 5 closure "
      f"== committed order = {_v_close}, heights == committed = "
      f"{_v_heights}, 25 directions verified = {_v_ok}, W4c violations = "
      f"{_v_w4c}, version registers occurring twice = {_v_multi}  "
      f"[{time.time() - t_ac2:.1f}s]")

# ---- K3c the variant that collapses the width ---------------------------
print("\n[K3c WHAT THE SCHEDULE'S PHASE SEPARATION IS WORTH — V1 against "
      "V4, the SAME objects with the arbitration order interleaved]")
for (a, c) in ((('DG', 3, 2), ('INTER', 3, 2)), (HEAD, ('INTER', 4, 2))):
    print(f"    {tag_of(a):32s} n={len(BUILT[a][0].H):3d} max|D| d2="
          f"{_maxw[a]:2d} d3={_maxw3[a]:2d} homog d2="
          f"{float(BUILT[a][1][2]['h2']):.4f}   vs   {tag_of(c):32s} "
          f"n={len(BUILT[c][0].H):3d} max|D| d2={_maxw[c]:2d} d3="
          f"{_maxw3[c]:2d} homog d2={float(BUILT[c][1][2]['h2']):.4f}")
_inter_collapse = all(_maxw[c] < _maxw[a] for (a, c) in
                      ((('DG', 3, 2), ('INTER', 3, 2)), (HEAD, ('INTER', 4, 2))))
print(f"    READ IT.  V4 has the same actors, the same 2g lineages, the "
      f"same bootstrap, the same 2g^2 proposals and the same 2g "
      f"arbitrations per round, and ZERO in-round deliveries — it "
      f"differs from V1 in NOTHING but the ORDER of the arbitrations "
      f"inside a round.  Interleaving them destroys the width.  What "
      f"THIS control shows, and it is the empirical half: THE ORDER OF "
      f"THE ARBITRATIONS INSIDE A ROUND DECIDES WHICH SUCCESSORS SIT AT "
      f"OFFSET 1.")
print(f"    AND WHAT IS *NOT* EMPIRICAL, MARKED AS SUCH (round-1 NIT 1). "
      f"The refinement sentence 'the second concurrent consumer must sit "
      f"at height + 1' CANNOT FAIL: SKY-B(2) counts events at EXACTLY "
      f"height + 2, so a successor at offset 1 contributes its own "
      f"b(y) successors while a successor at offset 2 contributes only "
      f"ITSELF (its successors land at offset >= 3 and are not counted), "
      f"and b(e) <= Bl = k caps that route at k.  The sentence is the "
      f"INSTRUMENT'S DEFINITION plus one inequality — DEFINITIONAL, not "
      f"a mechanism that could have come out otherwise — and it is "
      f"labelled definitional wherever it appears in this unit.  The "
      f"empirical content of this box is the V4 collapse, and the "
      f"empirical content of K3d is that a schedule CAN satisfy the "
      f"definitional condition at every k.")
check("K3c THE ARBITRATION ORDER INSIDE A ROUND DECIDES THE WIDTH, AND "
      "THE CONTROL IS A ONE-LINE CHANGE.  Interleaving the row and "
      "column arbitrations of a round — same actors, same lineages, same "
      "bootstrap, same events, same zero in-round deliveries — collapses "
      "max |D| at both g = 3 and g = 4.  D66's design finding ('what a "
      "second direction needs is a second CONCURRENT consumer') is "
      "therefore refined to: THE CONSUMER MUST ALSO SIT AT HEIGHT + 1 — "
      "which, ROUND-1 NIT 1, IS DEFINITIONAL (SKY-B counts offset-2 "
      "successors only as themselves, and b <= Bl caps that at k) AND IS "
      "SAID HERE TO BE DEFINITIONAL.  What is gated in this cell is the "
      "empirical half: that the ORDER changes which successors are at "
      "offset 1.  AND (round-1 MAJOR 1) PHASE SEPARATION IS NOT THE "
      "GENERAL LEVER: ARBCHAIN** has none and reaches k^2 at every k "
      "(K3d) — phase separation is how the TILING schedule meets the "
      "height condition, levelling is another way, and the condition is "
      "what is load-bearing",
      _inter_collapse,
      "; ".join(f"{tag_of(a)} {_maxw[a]} -> {tag_of(c)} {_maxw[c]}"
                for (a, c) in ((('DG', 3, 2), ('INTER', 3, 2)),
                               (HEAD, ('INTER', 4, 2)))))

# ======================================================================
# K1d — FULL-MENU REPLAY (C1 grade)
# ======================================================================
print("\n[K1d THE FULL-MENU REPLAY (D60's C1 grade) — every step "
      "re-driven with ALL actors offered, against a PRINTED budget]")
print("  ROUND-1 MAJOR 3, THE TWO GRADES SEPARATED BEFORE EITHER IS "
      "CLAIMED.  The whole")
print("  sweep carries the RESTRICTED-MENU grade of K1a (each event "
      "offered to its own")
print("  initiator).  D60's C1 grade — ALL actors offered at every "
      "step — is a")
print("  DIFFERENT and STRICTLY STRONGER property, it is expensive, and "
      "it is run on")
print("  the records listed below and on NO OTHERS.  The first version's "
      "claim (i)")
print("  welded the two together ('1,040 events ... C1-graded'); that "
      "sentence is")
print("  withdrawn and the C1-graded event count is printed here as a "
      "number.")
REPLAY = {}
_repl = [(('ARBCHAIN*', 0, 4), FULLMENU_BUDGET),
         (('ARBCHAIN*', 4, 4), FULLMENU_BUDGET),
         (('ARBCHAIN**', 5), AC2_REPLAY_BUDGET),
         (('DG', 3, 2), FULLMENU_BUDGET),
         (HEAD, HEAD_REPLAY_BUDGET)]
for k, bud in _repl:
    if k[0] == 'ARBCHAIN*':
        bb = AC[('star', k[1], k[2])][0]
        ac = list(bb.actors)
        nm = f"ARBCHAIN*(m={k[1]},k={k[2]})"
    elif k[0] == 'ARBCHAIN**':
        bb = AC2[k[1]]['b']
        ac = list(bb.actors)
        nm = f"ARBCHAIN**(k={k[1]})"
    else:
        bb = BUILT[k][0]
        ac = actors_of(k)
        nm = tag_of(k)
    REPLAY[nm] = full_menu_replay(bb.H, ac, bud)
    r = REPLAY[nm]
    print(f"    {nm:32s} ({len(bb.H):3d} events, {len(ac):2d} actors): "
          f"{r['status']} at step {r['step']}/{len(bb.H)}, max hits per "
          f"specification = {r['hits']}, widest full menu = {r['menu']} "
          f"candidates  [{r['t']:.1f}s]")
    sys.stdout.flush()
_rep_ok = all(r['hits'] == 1 and r['status'] != 'BROKEN'
              for r in REPLAY.values())
_rep_full = [n for n, r in REPLAY.items() if r['status'] == 'OK']
_c1_steps = sum(r['steps'] for r in REPLAY.values())
_sweep_ev = sum(len(v[0].H) for v in BUILT.values())
_c1_recs = len(REPLAY)
_never = [tag_of(k) for k in SWEEP if tag_of(k) not in REPLAY]
print(f"\n    THE C1 ACCOUNTING, AS A NUMBER (round-1 MAJOR 3).  Records "
      f"full-menu replayed = {_c1_recs}; C1-graded STEPS delivered = "
      f"{_c1_steps}; COMPLETE C1 records = {len(_rep_full)} "
      f"{sorted(_rep_full)}.  The restricted-menu sweep of K1a covers "
      f"{_sweep_ev} events over {len(SWEEP)} records; of the swept "
      f"records, the ones NEVER full-menu replayed at all are {_never}. "
      f"So '1,040 events, C1-graded' was never true and is not said "
      f"here.")
print(f"    THE PIN'S K1 NAMED THE HEADLINE RECORD, AND THE GAP IS "
      f"STATED AS A LIMITATION RATHER THAN PAPERED OVER.  "
      f"{tag_of(HEAD)} is BUDGET-CUT at step "
      f"{REPLAY[tag_of(HEAD)]['step']}/{len(BUILT[HEAD][0].H)} against a "
      f"printed {HEAD_REPLAY_BUDGET:.0f} s — and the budget is a "
      f"RECEIPT-RUNTIME CHOICE, not a property of the object (round-1 "
      f"MAJOR 3): the referee's own 157-event ARBCHAIN**(5) replays "
      f"COMPLETE within this receipt at a larger printed budget, so the "
      f"wall is the number chosen, not the layer.  WHAT IS DELIVERED "
      f"INSTEAD, and what it is worth: TWO complete C1 records that "
      f"carry the k^2 ceiling — ARBCHAIN*(m=4,k=4) at 16 directions and "
      f"ARBCHAIN**(k=5) at 25 — so the C1 grade for a ceiling-carrying "
      f"record does not rest on the cut record at all.  WHAT IS STILL "
      f"MISSING: a C1-complete DOUBLE-GRID(4, R), i.e. a C1-complete "
      f"TILING record at k = 4.  That is a limitation of this receipt "
      f"and it is carried as one.")
check("K1d [C1 GRADE, WITH THE ACCOUNTING STATED AS A NUMBER AND THE "
      "PIN-K1 GAP CARRIED AS A LIMITATION — round-1 MAJOR 3] "
      "ADMISSIBLE AGAINST THE UNRESTRICTED LAYER, ON "
      f"{_c1_steps} STEPS OF {_c1_recs} RECORDS AND NO OTHERS.  "
      "Replayed with ALL actors offered at every step, every "
      "specification is OFFERED among the hundreds or thousands of "
      "candidates the layer enumerates and matches EXACTLY ONE — no step "
      "refused, none ambiguous.  TWO COMPLETE CEILING-CARRYING RECORDS "
      "ARE REPLAYED END TO END: ARBCHAIN*(m=4, k=4), the 16-direction "
      "witness, and ARBCHAIN**(k=5), the 25-direction one — the latter a "
      "HIGHER forcedness grade than any DOUBLE-GRID record in this unit. "
      "THE DISQUALIFIER IS IN THE LABEL AND NOT ONLY IN THE PARENTHESIS "
      "(round-1 MINOR 7): DOUBLE-GRID(4, 2) IS BUDGET-CUT AND NO TILING "
      "k = 4 RECORD IS C1-COMPLETE HERE; the restricted-menu drive of "
      "K1a already establishes admissibility of every event of it "
      "against its whole prefix, so what the cut tail lacks is exactly "
      "the 'offered among ALL actors' property, and the budget is a "
      "printed receipt-runtime choice rather than a property of the "
      "object.  AND THE REPLAY INSTRUMENT IS ANCHORED IN PASSING: "
      "DOUBLE-GRID(3, 2) is replayed 72/72 at widest menu 536 "
      "candidates, D66's committed figures to the digit",
      _rep_ok and 'ARBCHAIN*(m=4,k=4)' in _rep_full
      and 'ARBCHAIN**(k=5)' in _rep_full
      and REPLAY[tag_of(('DG', 3, 2))]['status'] == 'OK'
      and REPLAY[tag_of(('DG', 3, 2))]['menu'] == 536
      and REPLAY[tag_of(('DG', 3, 2))]['step'] == 72,
      "; ".join(f"{n}: {r['status']} step {r['step']} hits {r['hits']} "
                f"menu {r['menu']}" for n, r in REPLAY.items())
      + f"; C1-graded steps = {_c1_steps} of {_sweep_ev} swept events; "
      f"records never full-menu replayed = {_never}")

# ======================================================================
# K4 — THE BAND QUESTION
# ======================================================================
print("\n[K4 THE BAND QUESTION AT BOTH DEPTHS AND ON BOTH BAND COLUMNS — "
      "is any k = 4 record IN-BAND while WIDE?  (D66's flagship managed "
      "it at d = 3 with max |D| = 9; the pin's honest lean is that the "
      "budget bound thins conflicts as k grows, so band membership "
      "should get HARDER)]")
print("  ROUND-1 BLOCKER 1, SAID FIRST.  The first version of this "
      "receipt stopped the")
print("  sweep at R = 3, reported the d = 3 homogeneity trend 0.4625 -> "
      "0.5417 -> 0.6562")
print("  against a floor of 0.6833 — a monotone sequence one step below "
      "the floor with")
print("  GROWING increments — and then stated the negative as a property "
      "of k = 4.  It")
print("  is a property of R <= 3.  The cost of the missing row was ONE "
      "BUILD, and the")
print("  row is here.  ROUND-1 MAJOR 4: every verdict below names its "
      "COLUMN and both")
print("  columns are reported.  ROUND-1 MAJOR 5: the family is MONOTONE "
      "in R and the")
print("  band is an interval it CROSSES, so 'in band' is reported as a "
      "crossing of a")
print("  one-parameter sweep and never as a property of an object.")
print(f"    {'record':32s} {'k':>2s} {'max d2':>6s} {'d3':>3s}  "
      f"{'homog d2':>8s} {'pos':>5s} {'|D|>=4 d2':>9s} {'pos':>5s}  "
      f"{'homog d3':>8s} {'pos':>5s} {'|D|>=4 d3':>9s} {'pos':>5s}  "
      f"{'int d3 h2':>9s} {'pos':>5s} {'int d3 h4':>9s} {'pos':>5s}")
_bandwide = {d: [] for d in (2, 3)}
_bandwide_both = {d: [] for d in (2, 3)}
for k in SWEEP:
    pf, pi = BUILT[k][1], INT[k]
    for d in (2, 3):
        if _inb(pf, d) and pf[2]['max'] >= MXB[2][0]:
            _bandwide[d].append(k)
        if _inb(pf, d) and _inb4(pf, d) and pf[2]['max'] >= MXB[2][0]:
            _bandwide_both[d].append(k)
    print(f"    {tag_of(k):32s} {_kof[k]:2d} {_maxw[k]:6d} {_maxw3[k]:3d}  "
          f"{float(pf[2]['h2']):8.4f} {_pos(pf[2]['h2'], 2):>5s} "
          f"{float(pf[2]['h4']):9.4f} {_pos4(pf[2]['h4'], 2):>5s}  "
          f"{float(pf[3]['h2']):8.4f} {_pos(pf[3]['h2'], 3):>5s} "
          f"{float(pf[3]['h4']):9.4f} {_pos4(pf[3]['h4'], 3):>5s}  "
          f"{float(pi[3]['h2']):9.4f} {_pos(pi[3]['h2'], 3):>5s} "
          f"{float(pi[3]['h4']):9.4f} {_pos4(pi[3]['h4'], 3):>5s}")
_k4recs = [k for k in SWEEP if _kof[k] == 4]
_k4_inband = {d: [k for k in _k4recs if _inb(BUILT[k][1], d)] for d in (2, 3)}
_k4_inband4 = {d: [k for k in _k4recs if _inb4(BUILT[k][1], d)]
               for d in (2, 3)}
_k4_both = {d: [k for k in _k4recs
                if _inb(BUILT[k][1], d) and _inb4(BUILT[k][1], d)]
            for d in (2, 3)}
_k4_int_inband = {d: [k for k in _k4recs if _inb(INT[k], d)] for d in (2, 3)}
_k4_int_both = {d: [k for k in _k4recs
                    if _inb(INT[k], d) and _inb4(INT[k], d)] for d in (2, 3)}


def _trendrow(kk):
    return (kk[2], float(BUILT[kk][1][2]['h2']), float(BUILT[kk][1][3]['h2']))


_trend4 = [_trendrow(k) for k in SWEEP if k[0] == 'DG' and k[1] == 4]
_trend3 = [_trendrow(k) for k in ANCH]
print("    THE R-TREND, WHOLE RECORD AND INTERIOR, WITH THE BAND AS AN "
      "INTERVAL THE SWEEP CROSSES (round-1 MAJOR 5):")
for (gg, rows) in ((4, _trend4), (3, _trend3)):
    print(f"      g = {gg} WHOLE     d = 3: " + ", ".join(
        "R=%d %.4f [%s]"
        % (r, b, _pos(BUILT[('DG', gg, r)][1][3]['h2'], 3))
        for (r, a, b) in rows))
    print(f"      g = {gg} INTERIOR  d = 3: " + ", ".join(
        "R=%d %.4f [%s]"
        % (r, float(INT[('DG', gg, r)][3]['h2']),
           _pos(INT[('DG', gg, r)][3]['h2'], 3)) for (r, a, b) in rows))
    print(f"      g = {gg} WHOLE     d = 2: " + ", ".join(
        "R=%d %.4f [%s] max|D| %d"
        % (r, a, _pos(BUILT[('DG', gg, r)][1][2]['h2'], 2),
           BUILT[('DG', gg, r)][1][2]['max']) for (r, a, b) in rows))
_mono4 = all(_trend4[i][2] < _trend4[i + 1][2] for i in range(len(_trend4) - 1))
_mono4i = all(float(INT[('DG', 4, _trend4[i][0])][3]['h2'])
              < float(INT[('DG', 4, _trend4[i + 1][0])][3]['h2'])
              for i in range(len(_trend4) - 1))
print(f"      BOTH SEQUENCES ARE MONOTONE IN R (whole {_mono4}, interior "
      f"{_mono4i}) and each crosses the d = 3 homogeneity band "
      f"[{float(BAND[3][0]):.4f}, {float(BAND[3][1]):.4f}] at a "
      f"DIFFERENT R: the interior enters at R = 2 and leaves at R = 3; "
      f"the whole record enters at R = 4.  'IN BAND' THEREFORE NAMES A "
      f"ROUND NUMBER, NOT AN OBJECT — a one-parameter family monotone in "
      f"a statistic crosses any interval somewhere, and the first "
      f"version read one cell of this table and called it a frontier.  "
      f"What survives the objection is the CROSSING ITSELF, reported as "
      f"a crossing, and the fact that at R = 4 the whole record is "
      f"inside BOTH d = 3 columns while carrying k^2.")
print(f"    IN-BAND k = 4 RECORDS, PER COLUMN.  d = 2: homogeneity "
      f"{[tag_of(k) for k in _k4_inband[2]]}, |D|>=4 "
      f"{[tag_of(k) for k in _k4_inband4[2]]}, BOTH "
      f"{[tag_of(k) for k in _k4_both[2]]}.  d = 3: homogeneity "
      f"{[tag_of(k) for k in _k4_inband[3]]}, |D|>=4 "
      f"{[tag_of(k) for k in _k4_inband4[3]]}, BOTH "
      f"{[tag_of(k) for k in _k4_both[3]]}.")
print(f"    UNDER THE INTERIOR POPULATION RESTRICTION (K2c; a population, "
      f"not an object).  d = 3: homogeneity "
      f"{[tag_of(k) for k in _k4_int_inband[3]]}, BOTH COLUMNS "
      f"{[tag_of(k) for k in _k4_int_both[3]]}.  ROUND-1 MAJOR 4, "
      f"EXPLICITLY: the interior of {tag_of(HEAD)} — the cell the first "
      f"version shipped — is IN the d = 3 homogeneity band at "
      f"{INT[HEAD][3]['h2']} and BELOW the d = 3 |D| >= 4 band at "
      f"{INT[HEAD][3]['h4']} ({float(INT[HEAD][3]['h4']):.4f} vs "
      f"[{float(W4B[3][0]):.4f}, {float(W4B[3][1]):.4f}]), and below "
      f"BOTH d = 2 bands.  It is in band on ONE COLUMN OF TWO.  The same "
      f"is true of D66's committed k = 3 flagship "
      f"({tag_of(('DG', 3, 4))} is at |D| >= 4 "
      f"{BUILT[('DG', 3, 4)][1][3]['h4']} at d = 3, far below), so this "
      f"is a CORPUS-LEVEL HABIT this unit inherited rather than invented "
      f"— said once, here, and carried.")
print(f"    THE MECHANISM, MEASURED RATHER THAN GUESSED: the pin's lean "
      f"was that the budget bound 1/(k+1) thins conflicts as k grows.  "
      f"The k = 4 total arbitration share IS 1/5 against k = 3's 1/4 "
      f"(K1c), and the width histograms of K3 show WHERE the homogeneity "
      f"goes: the k = 4 records carry a large population of width-0 and "
      f"width-1 charts (the bootstrap deliveries and the round's "
      f"proposals) against a handful of very wide ones.  A wider record "
      f"at FIXED round count is a more heterogeneous record — and the "
      f"remedy is more rounds, which is exactly what the R = 4 row is.")
_bandwide_int = {d: [k for k in _k4recs
                     if _inb(INT[k], d)
                     and BUILT[k][1][2]['max'] >= MXB[2][0]] for d in (2, 3)}
print(f"    THE ANSWER.  On the WHOLE record, in-band-AND-16-wide = "
      f"d2 {[tag_of(k) for k in _bandwide[2]]}, d3 "
      f"{[tag_of(k) for k in _bandwide[3]]}; on BOTH COLUMNS at once = "
      f"d2 {[tag_of(k) for k in _bandwide_both[2]]}, d3 "
      f"{[tag_of(k) for k in _bandwide_both[3]]}.  Under the interior "
      f"population restriction: d2 "
      f"{[tag_of(k) for k in _bandwide_int[2]]}, d3 "
      f"{[tag_of(k) for k in _bandwide_int[3]]}.")
check("K4 [THE BAND VERDICT — ROUND-1 BLOCKER 1, THE FIRST VERSION'S "
      "FLAGSHIP NEGATIVE INVERTED TO A POSITIVE] " + (
      f"**THE WIDTH-UNIFORMITY FRONTIER AT k = 4 DOES NOT EXIST: A "
      f"WHOLE k = 4 RECORD IS BAND-UNIFORM ON BOTH PUBLISHED COLUMNS "
      f"WHILE CARRYING k^2 = 16.**  {tag_of(FLAG)} — 200 events, forced, "
      f"menu hits [1, 1], ZERO in-round deliveries, total arbitration "
      f"share 1/5, max |D| = 16 at both depths — sits at d = 3 "
      f"homogeneity {BUILT[FLAG][1][3]['h2']} = "
      f"{float(BUILT[FLAG][1][3]['h2']):.4f} INSIDE "
      f"[{float(BAND[3][0]):.4f}, {float(BAND[3][1]):.4f}] AND at d = 3 "
      f"|D| >= 4 {float(BUILT[FLAG][1][3]['h4']):.4f} INSIDE "
      f"[{float(W4B[3][0]):.4f}, {float(W4B[3][1]):.4f}] — AS A WHOLE "
      f"RECORD, on BOTH band columns, which is MORE than D66's k = 3 "
      f"flagship achieves (it is in band on one of the two).  The pin's "
      f"honest lean — band membership should get HARDER as k grows — is "
      f"therefore REFUTED, in the direction of the unit's own interest, "
      f"and the first version's '(i) no k = 4 record is in band at "
      f"either depth', its FRONTIER box and its licensed claim (v) are "
      f"WITHDRAWN: they were properties of R <= 3, not of k = 4.  THE "
      f"R = 2 INTERIOR RESULT IS THE SAME PHENOMENON SEEN TWO ROUNDS "
      f"EARLY.  AND THE VERDICT IS STATED AS A CROSSING, NOT AS A MATCH "
      f"(round-1 MAJOR 5): both the whole-record and the interior d = 3 "
      f"homogeneity sequences are MONOTONE in R and each crosses the "
      f"band at a different R — the interior enters at R = 2 and leaves "
      f"at R = 3, the whole record enters at R = 4 — so 'in band' names "
      f"a round number and the object claim is only ever that the "
      f"crossing HAPPENS while the record carries k^2"
      if _bandwide_both[3] else
      (f"**IN BAND ON THE HOMOGENEITY COLUMN ONLY.**  A whole k = 4 "
       f"record is inside the d = 3 homogeneity band while 16 wide, but "
       f"not inside the |D| >= 4 band" if _bandwide[3] else
       f"**NO WHOLE k = 4 RECORD IS IN BAND AT EITHER DEPTH.**  Checked "
       f"at R = {sorted(k[2] for k in _k4recs if k[0] == 'DG')}"))
      + ".  The predicate is band membership on BOTH recomputed "
      "sprinkling columns, with the interior population restriction "
      "beside it.  THE VERDICT IS NOT AN ARTEFACT OF A MIS-SET BAND, "
      "and the gate says so: the SAME pipeline, the SAME re-run bands "
      "and the SAME depth put D66's committed k = 3 flagship "
      "DOUBLE-GRID(3, 4) INSIDE the d = 3 homogeneity band at max "
      "|D| = 9 and BELOW the d = 3 |D| >= 4 band — the instrument "
      "demonstrably separates the two columns and demonstrably CAN "
      "detect 'in band and wide' where it exists",
      len(_k4recs) >= 3 and _inb(BUILT[('DG', 3, 4)][1], 3)
      and _maxw3[('DG', 3, 4)] == 9
      and _inb(BUILT[FLAG][1], 3) and _inb4(BUILT[FLAG][1], 3)
      and BUILT[FLAG][1][2]['max'] == 16 and _mono4 and _mono4i
      and not _inb4(INT[HEAD], 3),
      f"k = 4 records = {len(_k4recs)}; WHOLE-record in band at d = 3: "
      f"homogeneity {[tag_of(k) for k in _k4_inband[3]]}, |D|>=4 "
      f"{[tag_of(k) for k in _k4_inband4[3]]}, BOTH COLUMNS "
      f"{[tag_of(k) for k in _k4_both[3]]}; in BOTH columns AND 16 wide "
      f"= {[tag_of(k) for k in _bandwide_both[3]]}; flagship "
      f"{tag_of(FLAG)} d3 homog {BUILT[FLAG][1][3]['h2']} in "
      f"{BAND[3]}, d3 |D|>=4 {BUILT[FLAG][1][3]['h4']} in {W4B[3]}, "
      f"max|D| {BUILT[FLAG][1][2]['max']}/{BUILT[FLAG][1][3]['max']}; "
      f"the headline's INTERIOR is in the d3 homogeneity band "
      f"({INT[HEAD][3]['h2']}) and BELOW the d3 |D|>=4 band "
      f"({INT[HEAD][3]['h4']} vs {W4B[3]}); monotone in R (whole "
      f"{_mono4}, interior {_mono4i}); the g = 3 anchor "
      f"DOUBLE-GRID(3,4) d = 3 homogeneity "
      f"{BUILT[('DG', 3, 4)][1][3]['h2']} "
      f"[{_pos(BUILT[('DG', 3, 4)][1][3]['h2'], 3)}] and |D|>=4 "
      f"{BUILT[('DG', 3, 4)][1][3]['h4']} "
      f"[{_pos4(BUILT[('DG', 3, 4)][1][3]['h4'], 3)}] with max |D| = "
      f"{_maxw3[('DG', 3, 4)]}")

# ---- K4b the levelling lever (round-1 NIT 2 / the first version's residue 2)
print("\n[K4b THE LEVELLING LEVER — the first version's residue 2 asked "
      "whether a bootstrap exists that LEVELS the first round's four row "
      "arbitrations, which would recover the lost chart AND raise "
      "homogeneity.  Round 1 built it in one pass of the grammar's own "
      "idle event; it is gated here, and the residue is CLOSED]")
_L, _D = ('LDG', 4, 2), HEAD
_lb, _lp = BUILT[_L][0], BUILT[_L][1]
_db, _dp = BUILT[_D][0], BUILT[_D][1]
_lw = Counter(len(sky(poset_of(_lb.H), e, 'B', 2)[0])
              for e in range(len(_lb.H)))
_dw = WID[_D]
print(f"    {tag_of(_D):32s} n={len(_db.H):3d} (no pads)            "
      f"d2 homog {_dp[2]['h2']} = {float(_dp[2]['h2']):.4f}, d3 "
      f"{_dp[3]['h2']} = {float(_dp[3]['h2']):.4f}; max|D| "
      f"{_dp[2]['max']}; charts of width 16 at d = 2 = "
      f"{_dw.get(16, 0)}; arb share {arbshare(_db.H)}")
print(f"    {tag_of(_L):32s} n={len(_lb.H):3d} ({_lb.npad} levelling "
      f"idles to common height {_lb.plevel})  d2 homog {_lp[2]['h2']} = "
      f"{float(_lp[2]['h2']):.4f}, d3 {_lp[3]['h2']} = "
      f"{float(_lp[3]['h2']):.4f}; max|D| {_lp[2]['max']}; charts of "
      f"width 16 at d = 2 = {_lw.get(16, 0)}; arb share "
      f"{arbshare(_lb.H)}")
print(f"    interior populations: {tag_of(_D)} d2 "
      f"{float(INT[_D][2]['h2']):.4f} d3 {float(INT[_D][3]['h2']):.4f} "
      f"[{_pos(INT[_D][3]['h2'], 3)}] ; {tag_of(_L)} d2 "
      f"{float(INT[_L][2]['h2']):.4f} d3 {float(INT[_L][3]['h2']):.4f} "
      f"[{_pos(INT[_L][3]['h2'], 3)}]")
_lev_chart = _lw.get(16, 0) > _dw.get(16, 0)
_lev_homog = (_lp[2]['h2'] > _dp[2]['h2'] and _lp[3]['h2'] > _dp[3]['h2'])
print(f"    READ IT.  The row-0 arbitration of the first round — the ONE "
      f"arbitration in the headline record that sits a height layer "
      f"below its three siblings because the bootstrap depresses it, and "
      f"which therefore realizes 4 of its 16 — now realizes its whole "
      f"budget: {_dw.get(16, 0)} charts of width 16 become "
      f"{_lw.get(16, 0)}, i.e. FOUR per round instead of three, and "
      f"homogeneity rises at BOTH depths.  THE TRADE, RECORDED: the "
      f"levelling pads the record with {_lb.npad} idle events, so the "
      f"1/(g+1) arbitration-share coincidence of K1c is diluted from "
      f"{arbshare(_db.H)} to {arbshare(_lb.H)}.  Residue 2's conjecture "
      f"is right on BOTH halves and it cost one pass of the grammar's "
      f"own idle event; the first version's 'unbuilt' is corrected.")
check("K4b [ROUND-1 NIT 2 — RESIDUE 2 IS CLOSED, NOT OPEN] **THE "
      "LEVELLED BOOTSTRAP RECOVERS THE FOURTH WIDTH-16 CHART AND RAISES "
      "HOMOGENEITY AT BOTH DEPTHS.**  LEVELLED-DGRID(4, 2) — the same "
      "schedule with one pass of the grammar's own ('n', a) idle "
      "inserted between the bootstrap and the rounds, so that every "
      "actor register starts the rounds at a common height — forces, "
      "carries max |D| = 16, and turns three width-16 charts into FOUR "
      "while moving d = 2 homogeneity up and d = 3 homogeneity up, its "
      "interior population reaching the d = 3 homogeneity band.  The "
      "trade is printed: the pad dilutes the arbitration share from 1/5 "
      "to 6/35.  It does NOT by itself put the whole record in band — "
      "that is K4's R = 4 row — and the gate says so",
      _lev_chart and _lev_homog and not _lb.refusal and _lb.maxhits == 1
      and _lp[2]['max'] == 16 and _lb.npad > 0,
      f"pads = {_lb.npad} to common height {_lb.plevel}; width-16 charts "
      f"{_dw.get(16, 0)} -> {_lw.get(16, 0)}; d2 homogeneity "
      f"{_dp[2]['h2']} -> {_lp[2]['h2']}; d3 {_dp[3]['h2']} -> "
      f"{_lp[3]['h2']}; interior d3 {INT[_D][3]['h2']} -> "
      f"{INT[_L][3]['h2']} [{_pos(INT[_L][3]['h2'], 3)}]; arb share "
      f"{arbshare(_db.H)} -> {arbshare(_lb.H)}; max|D| "
      f"{_lp[2]['max']}/{_lp[3]['max']}")

# ======================================================================
# K5 — THE COBOUNDARY BATTERY
# ======================================================================
print("\n[K5 THE COBOUNDARY GATE — D64's C7, BOTH ROUTES, at five port "
      "conventions, plus the convention-comparable PARITY route and the "
      "FREE-RELABELLING route.  The gauge question rides along at zero "
      "marginal cost and the pin declares NO LEAN either way]")
print("  THE PORT CONVENTIONS FOR 5-REGISTER EVENTS (a k = 4 "
      "arbitration carries four")
print("  proposers plus the minted version), all five run, all defined "
      "in D66 and")
print("  imported here unmodified: REG (the layer's own tuple order), "
      "REGA (all")
print("  registers sorted by name), ARBLOSE (losers, winners, version), "
      "ARBVFIRST")
print("  (version first), COV (the register-free surrogate, the only one "
      "also defined")
print("  on sprinklings).")
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


# ROUND-1 MINOR 3: DOUBLE-GRID(4, 3) — the OTHER record carrying
# max |D| = 16, with seven wide charts — was outside the first version's
# census while claim (vi) said "every k = 4 wide record".  It is in the
# census now.
K5SET = [HEAD, ('DG', 4, 1), ('DG', 4, 3), ('DG', 3, 4), ('CG', 4, 4),
         ('INTER', 4, 2)]
_conv_agree = True
for k in K5SET:
    for op in BUILT[k][0].H:
        for c in ('tuple', 'sorted'):
            if my_ord_tuple(op, c) != ord_tuple0(op, c):
                _conv_agree = False
g64['ord_tuple'] = my_ord_tuple
for k in K5SET:
    add_sub(tag_of(k), BUILT[k][0].H, poset_of(BUILT[k][0].H))
_acb = AC[('star', 4, 4)][0]
add_sub('ARBCHAIN*(m=4,k=4)', _acb.H, poset_of(_acb.H))
add_sub('DR(8,10,8)', b_dr.H, poset_of(b_dr.H))
add_sub('M21', None, mink4(latt(120, 2, 60, 8)), 'sprinkling')
add_sub('M31', None, mink4(latt(120, 3, 48, 8)), 'sprinkling')
g64['SUB'] = SUBS
MEAS = {}
g64['MEAS'] = MEAS

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
print("\n  [K5a INSTRUMENT VALIDATION (D64's C0b) — re-run on every k = 4 "
      "record: P is `event_poset`'s own generating relation and its "
      "transitive closure must BE the committed order]")
for (nm, n, bad_rt, bnd, same, npe, nce, skip) in _val_rows:
    print(f"      {nm:32s} n={n:4d} reg_tuple != regs_of at {bad_rt}; "
          f"#P-successors <= |regs_of| = {bnd}; closure(P) == committed "
          f"order = {same}; P-edges {npe}, covers {nce}, height-skipping "
          f"{skip}")
check("K5a [ANCHOR] THE COCYCLE INSTRUMENT IS VALIDATED ON THE k = 4 "
      "SUBSTRATES, NOT ASSUMED.  On every k = 4 record and every "
      "control: `reg_tuple` is `regs_of` with an order; each event has "
      "at most |regs_of| P-successors; THE TRANSITIVE CLOSURE OF P "
      "EQUALS the committed order `poset_of`; the covering relation is "
      "contained in P; the COV surrogate's own closure is the committed "
      "order on every substrate including the sprinklings; and D66's "
      "`my_ord_tuple` reproduces D64's own `ord_tuple` value for value "
      "on every event at both committed conventions",
      _cl_ok and _rt_ok and _bnd_ok and _cov_ok and _conv_agree,
      f"grammar substrates validated = {len(_val_rows)}; closure == "
      f"order everywhere = {_cl_ok}; reg_tuple == regs_of = {_rt_ok}; "
      f"successor bound = {_bnd_ok}; COV closure and cover containment = "
      f"{_cov_ok}; ord_tuple agrees with d64 = {_conv_agree}", anchor=True)

t_m = time.time()
for nm in sorted(SUBS):
    for tg in sorted(SUBS[nm]['inst']):
        for d in DEPTHS:
            MEAS[(nm, tg, d)] = measure(nm, tg, d)
print(f"\n  [K5b THE TRANSITION CENSUS — {len(MEAS)} cells "
      f"(substrate x instrument x depth)  [{time.time()-t_m:.1f}s]]")
print(f"      {'substrate':32s} {'inst':9s} {'d':>2s} {'charts':>7s} "
      f"{'wide':>5s} {'pairs':>6s} {'triples':>8s} {'ROLE id/non':>14s} "
      f"  classes")
for nm in sorted(SUBS):
    for tg in INST:
        if tg not in SUBS[nm]['inst']:
            continue
        for d in DEPTHS:
            r = MEAS[(nm, tg, d)]
            print(f"      {nm:32s} {tg:9s} {d:2d} {r['charts']:7d} "
                  f"{r['wide']:5d} {r['pairs']:6d} {r['triples']:8d} "
                  f"{r['ROLE'][0]:6d}/{r['ROLE'][1]:<7d} {r['kinds']}")
_reach = all(r['reach_ok'] for r in MEAS.values())
_xh = sum(r['xhpairs'] for r in MEAS.values())
_viol = sum(r['cocycle'][1] for r in MEAS.values())
_tested = sum(r['cocycle'][0] for r in MEAS.values())
check("K5b THE CENSUS AND THE COCYCLE.  The P-path enumeration reaches "
      "EXACTLY SKY-B's direction set at every base event of every "
      "substrate at both depths (so the coordinates cover the charts and "
      "nothing else), every overlapping chart pair is same-height, and "
      "the fibre-map cocycle has ZERO violations wherever it is defined "
      "— with the coverage reported rather than assumed: the testable "
      "triple count is printed per cell and a zero there is a DEAD test, "
      "not a passed one",
      _reach and _xh == 0 and _viol == 0,
      f"cells = {len(MEAS)}; P-reach == SKY-B everywhere = {_reach}; "
      f"cross-height overlapping pairs = {_xh}; cocycle triples tested "
      f"with a defined composition = {_tested}, VIOLATIONS = {_viol}")

print("\n  [K5c THE ARTIFACT PROBES (D64's C2b) — a labeling can produce "
      "a flat atlas for reasons that have nothing to do with geometry]")
_blind = [(nm, tg, d, w) for (nm, tg, d), r in sorted(MEAS.items(), key=repr)
          for w in LAB
          if r[w + ':const'][0] > 0 and r[w + ':const'][1] == r[w + ':const'][0]]
for nm in sorted(SUBS):
    for d in DEPTHS:
        r = MEAS[(nm, 'REG', d)] if 'REG' in SUBS[nm]['inst'] else None
        if r is None:
            continue
        print(f"      PROBE 1 {nm:32s} REG d={d}: directions seen by >= 2 "
              f"charts = {r['ROLE:const'][0]}, of which the label is "
              f"CONSTANT across charts = {r['ROLE:const'][1]} (RAW: "
              f"{r['RAW:const'][1]})")
_readcells = [(nm, tg, d) for nm in sorted(SUBS)
              if SUBS[nm]['kind'] == 'grammar'
              for tg in INST if tg in SUBS[nm]['inst'] for d in DEPTHS]
BLIND_ROLE = {(nm, tg, d) for (nm, tg, d) in _readcells
              if MEAS[(nm, tg, d)]['ROLE:const'][0] > 0
              and MEAS[(nm, tg, d)]['ROLE:const'][1]
              == MEAS[(nm, tg, d)]['ROLE:const'][0]}
_wide_nm = tag_of(HEAD)
_blind_wide = [c for c in BLIND_ROLE if c[0] == _wide_nm]
print(f"      PROBE 1 FIRES at {len(_blind)} (labeling, substrate, "
      f"instrument, depth) cells: {[(a, b, c, w) for (a, b, c, w) in _blind]}")
print(f"      OF THOSE, the cells where the READ labeling (ROLE) is "
      f"blind — EXCLUDED BY NAME from every convention-robustness "
      f"sentence below: {sorted(BLIND_ROLE)}")
check("K5c THE PROBES DECIDE WHERE THE OUTCOME MAY BE READ, AND THEY ARE "
      "PRINTED AND ACTED ON RATHER THAN FOLDED AWAY.  The decisive "
      "reading — the k = 4 wide record's transition class — is made at "
      "the ROLE labeling, and the cells where PROBE 1 fires there are "
      "listed and excluded by name.  No outcome anywhere is read at RAW",
      len(_readcells) > 0,
      f"blind ROLE cells on the headline k = 4 record = "
      f"{len(_blind_wide)} {sorted(_blind_wide)}; blind ROLE cells "
      f"anywhere = {len(BLIND_ROLE)} of {len(_readcells)}; blind cells "
      f"at any labeling = {len(_blind)}")

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
print("\n  [K5d VALIDATION OF THE TWO ADDED ROUTES (d47a's SG1 doctrine: "
      "a true positive AND a true negative, constructed, before either "
      "is pointed at a record)]")
print(f"      PARITY route: an odd triangle (tau, identity, identity) -> "
      f"{_vp[0]} obstruction(s); an even triangle (tau, tau, identity) "
      f"-> {_vp[1]}.  FREE-RELABELLING route: an inconsistent triangle "
      f"-> {_vp[2]}; the consistent one -> {_vp[3]}.")
check("K5d THE TWO ADDED ROUTES ARE NOT BLIND AND NOT TRIGGER-HAPPY, so "
      "a zero reported below is a measurement and not an instrument that "
      "cannot fire",
      _vp == (1, 0, 1, 0) and classify(_mtau) == 'tau'
      and classify(_mid) == 'identity',
      f"(parity positive, parity negative, free positive, free negative) "
      f"= {_vp}")

print("\n  [K5e THE COBOUNDARY COMPUTATION — D64's `cochain` (both "
      "routes), at every convention, beside PARITY and FREE]")
print(f"      {'substrate':32s} {'inst':9s} {'d':>2s} {'gen':>9s} "
      f"{'edges':>6s} {'comps':>6s} {'C7 OBS':>7s} {'C7 surv':>8s} "
      f"{'cech t/v':>10s} {'PARITY e/OBS':>13s} {'FREE OBS/surv':>14s}")
CO, UFR, PAR = {}, {}, {}
for nm in sorted(SUBS):
    for tg in INST:
        if tg not in SUBS[nm]['inst']:
            continue
        for d in DEPTHS:
            r = MEAS[(nm, tg, d)]
            co, uf, pa = cochain(nm, tg, d), uf_trivialize(r), parity_obstruction(r)
            CO[(nm, tg, d)], UFR[(nm, tg, d)], PAR[(nm, tg, d)] = co, uf, pa
            print(f"      {nm:32s} {tg:9s} {d:2d} {co['gen'][:9]:>9s} "
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
check("K5e(i) [ANCHOR] THE COBOUNDARY INSTRUMENT REPRODUCES D64's "
      "COMMITTED C7 ROW EXACTLY.  On DOUBLE-RING(8, 10, 8) at REG and "
      "d = 2: 60 charts, 138 labelled overlaps, 9 components, ZERO "
      "obstructions, eps = 32/28, zero survivors, 108 Cech triples with "
      "0 violations, transition split 57/115, REGA eps = 40/20.  So the "
      "same instrument, unmodified, produces every obstruction count "
      "below and a non-zero count cannot be a difference of instruments",
      _dranchor,
      f"DR REG d2: charts {_dr7['charts']}, labelled {_dr7['labelled']}, "
      f"comps {_dr7['comps']}, obstructions {_dr7['incons']}, eps "
      f"{_dr7['eps0']}/{_dr7['eps1']}, surviving {_dr7['surv']}, cech "
      f"{_dr7['cech_t']}/{_dr7['cech_v']}; REGA eps {_dr7a['eps0']}/"
      f"{_dr7a['eps1']}, obstructions {_dr7a['incons']}", anchor=True)

_wide_rows = {(tg, d): (CO[(_wide_nm, tg, d)], UFR[(_wide_nm, tg, d)],
                        PAR[(_wide_nm, tg, d)]) for tg in INST
              for d in DEPTHS}
_wide_triv = all(co['incons'] == 0 and uf['obstructions'] == 0
                 and pa['obstructions'] == 0
                 for (co, uf, pa) in _wide_rows.values())
_ac_nm = 'ARBCHAIN*(m=4,k=4)'
_ac_rows = {(tg, d): (CO[(_ac_nm, tg, d)], UFR[(_ac_nm, tg, d)],
                      PAR[(_ac_nm, tg, d)]) for tg in INST for d in DEPTHS}
_ac_triv = all(co['incons'] == 0 and uf['obstructions'] == 0
               and pa['obstructions'] == 0
               for (co, uf, pa) in _ac_rows.values())
print(f"\n    THE k = 4 WIDE RECORDS, where the gauge question is read:")
for nm in (_wide_nm, _ac_nm):
    print(f"      {nm}: transitions by class at d = 2, per convention = "
          f"{ {tg: MEAS[(nm, tg, 2)]['kinds'] for tg in INST} }")
    for tg in INST:
        rr = MEAS[(nm, tg, 2)]
        ce, cn = _c7_edges(rr)
        pa = PAR[(nm, tg, 2)]
        print(f"        {tg:9s}: C7 cochain on {ce:4d} edges of which "
              f"NON-IDENTITY {cn:4d} -> obstruction "
              f"{CO[(nm, tg, 2)]['incons']}; PARITY cochain on "
              f"{pa['edges']:4d} edges of which NON-IDENTITY "
              f"{pa['nonid']:4d} -> obstruction {pa['obstructions']}; "
              f"FREE -> {UFR[(nm, tg, 2)]['obstructions']}; Cech triples "
              f"{CO[(nm, tg, 2)]['cech_t']}")
_live_conv = {nm: sorted(tg for tg in INST if PAR[(nm, tg, 2)]['nonid'] > 0)
              for nm in (_wide_nm, _ac_nm)}
print(f"    WHERE THE TEST HAS CONTENT (D66 MAJOR 4's lesson: credit the "
      f"column that carries it).  Conventions at which the PARITY "
      f"cochain is NOT identically zero — i.e. where a non-trivial "
      f"cochain is actually being trivialized rather than a zero one "
      f"being confirmed: {_live_conv}.  At the other conventions the "
      f"content is PROBE 1's silence (the labeling COULD have shown a "
      f"transition and did not), NOT the Cech triple count.")
_allobs = {k: (CO[k]['incons'], PAR[k]['obstructions'],
               UFR[k]['obstructions']) for k in CO}
_nonzero = sorted(k for k, v in _allobs.items() if max(v) > 0)
_spr_par = {k: PAR[k]['obstructions'] for k in PAR
            if SUBS[k[0]]['kind'] == 'sprinkling'}
print(f"    CELLS WITH ANY NON-ZERO OBSTRUCTION over the whole "
      f"{len(CO)}-cell census (C7 | PARITY | FREE): "
      f"{ {k: _allobs[k] for k in _nonzero} }")
print(f"    THE CONTROLS: genuine sprinklings at COV carry "
      f"{ {k[0] + '/d' + str(k[2]): v for k, v in sorted(_spr_par.items(), key=repr) if k[1] == 'COV'} }"
      f" parity obstructions; the delivery crystal DR(8,10,8) at COV "
      f"carries "
      f"{ {'d' + str(d): PAR[('DR(8,10,8)', 'COV', d)]['obstructions'] for d in DEPTHS} }.")
_c7_dir = all((co['surv'] > 0 if co['incons'] > 0 else True)
              and (co['cech_v'] == 0 if co['incons'] == 0 else True)
              for co in CO.values())
_c7_pos = sorted(k for k in CO if CO[k]['incons'] > 0)
_free_pos = sorted(k for k in UFR if UFR[k]['obstructions'] > 0)
_par_pos = sorted(k for k in PAR if PAR[k]['obstructions'] > 0)
_par_conv = sorted({k[1] for k in _par_pos
                    if SUBS[k[0]]['kind'] == 'grammar'})
_par_recs = sorted({k[0] for k in _par_pos
                    if SUBS[k[0]]['kind'] == 'grammar'})
print(f"    THE ROUTES, SEPARATED (D66 residue 5 asked exactly this).  "
      f"D64's own C7 obstructs at {len(_c7_pos)} cells {_c7_pos}; the "
      f"FREE-RELABELLING route at {len(_free_pos)} cells {_free_pos}; "
      f"the PARITY route at {len(_par_pos)} cells, whose GRAMMAR members "
      f"live at conventions {_par_conv} on records {_par_recs}.  Note "
      f"which records those are: the obstructing convention is ARBLOSE "
      f"— the winner/loser port order — and it obstructs on the k = 3 "
      f"DOUBLE GRID as well as the k = 4 one, so this is a property of "
      f"the DOUBLE-GRID SCHEDULE and of that port convention, NOT a "
      f"k = 4 phenomenon.  C7 does not see it because it drops the "
      f"'other' class by construction (its ARBLOSE domain shrinks from "
      f"{PAR[(_wide_nm, 'ARBLOSE', 2)]['edges']} edges to "
      f"{_c7_edges(MEAS[(_wide_nm, 'ARBLOSE', 2)])[0]}).")
check("K5e(ii) [THE GAUGE VERDICT, NO LEAN EITHER WAY; ROUND-1 MINOR 7 — "
      "THE DISQUALIFIER IS IN THE LABEL: THE HEADLINE RECORD IS *NOT* "
      "TRIVIAL AT EVERY CONVENTION AND ROUTE, AND WHAT THIS CELL GATES "
      "IS THE ROUTE-AGREEMENT, NOT THE TRIVIALITY] " + (
      "**THE k = 4 CLASS IS TRIVIAL TOO.**  On both wide k = 4 records "
      "— the DOUBLE GRID and the 16-direction ARBCHAIN* — all three "
      "routes return ZERO obstructions at all five port conventions and "
      "both depths.  Width past every previous record buys no gauge: "
      "D64's successor question is answered negatively again, on the "
      "widest substrate the campaign has built"
      if (_wide_triv and _ac_triv) else
      "**TRIVIAL BY C7 AND BY FREE RELABELLING AT EVERY CELL OF THE "
      "CENSUS; NON-ZERO BY THE PARITY ROUTE AT ONE CONVENTION.**  D64's "
      "own C7 returns ZERO obstructions at every one of the census "
      "cells and so does the FREE-RELABELLING route — the largest "
      "possible gauge group — so no non-trivial structure group is "
      "exhibited by k = 4 conflict either, and D64's successor question "
      "is answered NEGATIVELY again on the widest substrate the "
      "campaign has built.  What is NOT zero is the PARITY route at "
      "ARBLOSE, the winner/loser port order — D66's residue 5 named "
      "exactly that convention as the one that behaves differently and "
      "asked for a sweep; the sweep is here, and the answer is that it "
      "obstructs on the DOUBLE-GRID schedule at k = 3 AND at k = 4, so "
      "it is a property of the schedule and the convention and not of "
      "the proposer count.  It is REPORTED AND NOT CLAIMED as "
      "H^1 != 0: the free-relabelling route trivializes every one of "
      "those cells, the genuine sprinklings carry non-zero parity "
      "obstructions too at COV, and the Z/2 name is a convention "
      "(D64 C4b)") + ".  C7's two routes agree in the decisive "
      "direction at every cell of the census, which is the gate; the "
      "verdict is the measurement.  AND THE CENSUS NOW CONTAINS BOTH "
      "16-WIDE RECORDS (round-1 MINOR 3): DOUBLE-GRID(4, 3), which "
      "carries max |D| = 16 at both depths with seven wide charts, was "
      "outside the first version's census while its claim (vi) said "
      "'every k = 4 wide record'; it is a substrate here",
      _c7_dir and len(CO) == len(MEAS) and len(_free_pos) == 0,
      f"cells = {len(CO)}; C7's routes agree in the decisive direction "
      f"everywhere = {_c7_dir}; headline k = 4 record trivial at every "
      f"convention and route = {_wide_triv}; ARBCHAIN*(4,4) trivial = "
      f"{_ac_triv}; cells with any non-zero obstruction = "
      f"{len(_nonzero)} {_nonzero}")

# ======================================================================
# THE VERDICT
# ======================================================================
OUTCOME = ('K-I' if _refusals else
           ('K-III' if _maxw[HEAD] >= MXB[2][0] else 'K-II'))
print(f"\n[THE PRE-REGISTERED OUTCOME, read off the sweep: {OUTCOME}]")
check("K6a [THE OUTCOME] " + {
    'K-I': "**K-I — THE 4-PROPOSER SCHEDULE REFUSES TO FORCE.**  The "
           "break mechanism is the deliverable",
    'K-II': "**K-II — IT FORCES, BUT max |D| STAYS BELOW THE SPRINKLING "
            "FLOOR.**  The gap between the k^2 bound and the realized "
            "width is the finding, and the unfilled-successor census "
            "characterises it",
    'K-III': "**K-III — max |D| REACHES THE SPRINKLING HULL, AND THE "
             "UNIFORMITY SURVIVES IT.**  The k = 4 DOUBLE GRID forces, "
             "tiles at cadence with ZERO in-round deliveries and a TOTAL "
             "arbitration share of exactly 1/5 = 1/(k_conflict + 1) at "
             "every R (its CONFLICT share is 2/15 and its own applicable "
             "bound, k_min = 1, is 1/2 and is not saturated — K1c), and "
             "carries max |D| = 16 = k^2 at d = 2 — W4c's ceiling "
             "realized at k = 4, inside the HULL [10, 17] of the "
             "sprinkling maxima, which is the hull of the M21 cluster "
             "[10, 11] and the M31 cluster [14, 17], so 16 lies in the "
             "3+1 cluster and outside the 2+1 one.  AND (round-1 "
             "BLOCKER 1) K4's uniformity half comes back POSITIVE on the "
             "WHOLE record at R = 4, on BOTH band columns, so the "
             "width-uniformity frontier at k = 4 does not exist; and "
             "(round-1 MAJOR 1) K3d realizes k^2 at k = 3, 4, 5 AND 6, "
             "so 16 is a parameter picked and not a coincidence "
             "discovered"
    }[OUTCOME] + ".  The predicate is the pre-registered disjunction "
    "itself, computed from the sweep: a refusal anywhere would have "
    "printed K-I and a max |D| below the RE-RUN sprinkling floor would "
    "have printed K-II",
    OUTCOME == 'K-III',
    f"refusals = {len(_refusals)}; headline max |D| at d = 2 = "
    f"{_maxw[HEAD]} vs the re-run sprinkling floor {MXB[2][0]} (M21 "
    f"cluster {DIMR[('M21', 2)]}, M31 cluster {DIMR[('M31', 2)]}) and "
    f"the k = 4 bound 16; records at or above the floor = {len(GRADE)}; "
    f"the k^2 ladder = { {k: len(AC2[k]['D2']) for k in sorted(AC2)} }")

# ======================================================================
# K6 — anti-vacuity, caps, determinism
# ======================================================================
_src = open('v10/code/d67_k4_double_grid_exact.py').read()
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
check("K6b AST anti-vacuity in d47a's SG8 form: every check() predicate "
      "is a bare constant NOWHERE and references at least one run-bound "
      "name.  SCOPE (LOG #403 MA-2): the scan enforces exactly that and "
      "detects no vacuous gate in arbitrary syntactic form",
      len(_ch) >= 10 and not _vac,
      f"check() calls = {len(_ch)}, bare-constant or unbound predicates "
      f"= {len(_vac)}")

print("\n[K6c DEPTHS, CAPS, RANGES AND POPULATIONS — all printed, none "
      "silent]")
print(f"    SKY-B depths measured: 2 and 3 at every record and every "
      f"instrument (committed SKYB_DEPTH = {SKYB_DEPTH}).")
print(f"    swept configurations = {len(SWEEP)}; records built = "
      f"{len(BUILT)}; events built in the sweep = "
      f"{sum(len(v[0].H) for v in BUILT.values())}; largest record = "
      f"{max(len(v[0].H) for v in BUILT.values())} events; ARBCHAIN "
      f"families built = {len(AC)} ({sum(len(r[0].H) for r in AC.values())} "
      f"events); controls re-run = DR(8,10,8) (177), BRICK(8,14) (65), "
      f"11 sprinkling configurations, 2 sprinklings charted.")
print(f"    R VALUES SWEPT IN THE DOUBLE-GRID FAMILY = "
      f"{sorted({k[2] for k in SWEEP if k[0] == 'DG'})} (at g = 4: "
      f"{sorted({k[2] for k in SWEEP if k[0] == 'DG' and k[1] == 4})}; at "
      f"g = 3, the committed anchors: "
      f"{sorted({k[2] for k in SWEEP if k[0] == 'DG' and k[1] == 3})}).  "
      f"THE COST CURVE, printed because it is what bounds the sweep: "
      f"{ {tag_of(k): f'{BUILT[k][2]:.1f}s' for k in SWEEP if k[0] in ('DG', 'LDG')} }"
      f" — the layer's own menu enumeration grows with the base count "
      f"and every arbitration mints a version (D66 residue 7).  The "
      f"R = 4 row is the round-1 flagship and it is what the R-prefix "
      f"lemma (K0f) buys: the three shorter g = 4 records are read off "
      f"its prefixes instead of being rebuilt, which is why their "
      f"printed cost is a fraction of a second.  DOUBLE-GRID(5, R) is "
      f"still out of this receipt's reach, so the k = 5 CEILING question "
      f"is carried by ARBCHAIN**(5) (K3d) and the k = 5 TILING question "
      f"is left open by name.")
print(f"    full-menu replays = {len(REPLAY)}, budgets "
      f"{FULLMENU_BUDGET:.0f}s / {HEAD_REPLAY_BUDGET:.0f}s "
      f"(DOUBLE-GRID(4, 2)) / {AC2_REPLAY_BUDGET:.0f}s (ARBCHAIN**(5)), "
      f"statuses { {n: r['status'] for n, r in REPLAY.items()} }; "
      f"C1-graded steps delivered = {_c1_steps}.")
_ac2_cost = {k: "%.1fs" % AC2[k]['t'] for k in sorted(AC2)}
print(f"    ARBCHAIN** ladder built at k = {sorted(AC2)} "
      f"({sum(len(AC2[k]['b'].H) for k in AC2)} events, "
      f"{sum(AC2[k]['b'].npad for k in AC2)} of them levelling idles), "
      f"per-k build cost {_ac2_cost}.")
print(f"    K5 measurement cells = {len(MEAS)} over {len(SUBS)} "
      f"substrates x {len(INST)} instruments x 2 depths; overlapping "
      f"pairs examined = {sum(r['pairs'] for r in MEAS.values())}; "
      f"triples examined = {sum(r['triples'] for r in MEAS.values())}.")
print(f"    thresholds used anywhere: D58's |D| >= 2 and |D| >= 4 "
      f"columns, the pin's overlap and triple predicates, and the K0c "
      f"sprinkling bands and max|D| range.  NO OTHER THRESHOLD IS USED; "
      f"in particular the K3 verdict is read against the RE-RUN "
      f"sprinkling floor {MXB[2][0]}, not against the pin's prose.")
print(f"    NOTHING WAS CUT SILENTLY: the only budgets that bind are the "
      f"full-menu replays, whose cut points are printed in K1d.  Total "
      f"wall clock at this line: {time.time() - T0:.1f}s.")

t_det = time.time()
_digs = []
for _seed in ('0', '7', '999'):
    _env = dict(os.environ, PYTHONHASHSEED=_seed)
    _digs.append(subprocess.run(
        [sys.executable, 'v10/code/d67_k4_double_grid_exact.py', '--probe'],
        capture_output=True, text=True, env=_env).stdout)
check("K6d DETERMINISM IS GATED ON THE PROBE FAMILY ONLY — AND THE SCOPE "
      "IS IN THE LABEL, NOT ONLY IN THE PARENTHESIS (round-1 MINOR 7): "
      "**IT DOES NOT COVER THE g = 4 DOUBLE-GRID BUILDS, THE ROUND-1 "
      "FLAGSHIP, OR THE K5 CENSUS** (D63's W6b pattern; the "
      "layer reads next(iter(frozenset)) in load-bearing places and this "
      "unit's arbitrations have FOUR proposers, where the `regs_of` "
      "tie-break and `reg_tuple`'s sort could in principle diverge — "
      "K5a's closure gate is what would catch it).  THE DIGEST COVERS: "
      "the g = 3 double grid, its interleaved variant, ARBCHAIN*(m, 4) "
      "at m = 0, 2, 4 (the 16-direction witness included) and the "
      "SHARED-BASE refusal, PLUS (this round) ARBCHAIN**(3) and "
      "ARBCHAIN**(4) with their levelling-pad counts, common levelling "
      "height, h(e) and |D_e(2)| — all rebuilt in probe mode under "
      "PYTHONHASHSEED 0 / 7 / 999 — exact-Fraction profile rows at both "
      "depths, arbitration share, full width histogram and the refusal "
      "index — byte-identical stdout.  IT DOES NOT COVER the g = 4 "
      "DOUBLE-GRID builds (including the flagship), LEVELLED-DGRID, "
      "ARBCHAIN**(5)/(6), or the K5 census",
      len(set(_digs)) == 1 and 'DIGEST' in _digs[0]
      and "ARBCHAIN*(4,4)" in _digs[0] and 'SHARED-BASE' in _digs[0]
      and 'ARBCHAIN**(4)' in _digs[0],
      f"probe runs = 3, distinct outputs = {len(set(_digs))}  "
      f"[{time.time() - t_det:.1f}s]")

print("\n[VERDICT — D67, ROUND-1 REPAIRED]")
print(f"  {OUTCOME} FIRED.")
_hks = Counter(len({t[0] for t in e[2]})
               for e in BUILT[HEAD][0].H if e[0] == 'r')
_fks = Counter(len({t[0] for t in e[2]})
               for e in BUILT[FLAG][0].H if e[0] == 'r')
print(f"    THE FLAGSHIP.  {tag_of(FLAG)}: {len(BUILT[FLAG][0].H)} events "
      f"over {len(actors_of(FLAG))} actors, {FLAG[2]} rounds, "
      f"{sum(1 for e in BUILT[FLAG][0].H if e[0] == 'r')} arbitrations = "
      f"{_fks[4]} FOUR-proposer conflict arbitrations + {_fks[1]} "
      f"ONE-proposer bootstrap mints,")
print(f"    {len(_dels_of[FLAG])} deliveries — ALL of them in the "
      f"bootstrap, ZERO in any round — TOTAL arbitration share "
      f"{arbshare(BUILT[FLAG][0].H)} = 1/(k_conflict + 1) and CONFLICT "
      f"share {Fr(_fks[4], len(BUILT[FLAG][0].H))}; the record's own "
      f"applicable bound (k_min = 1) is 1/2 and is NOT saturated.")
print(f"    Every event offered by the layer's own menu, every "
      f"specification matching exactly one candidate.")
print(f"    THE SCHEDULE.  {tag_of(HEAD)}, the R = 2 member: "
      f"{len(BUILT[HEAD][0].H)} events, {_hks[4]} four-proposer conflict "
      f"arbitrations + {_hks[1]} one-proposer mints.")
print(f"    THE DESIGN.  Rows and columns conflict CONCURRENTLY on "
      f"{2 * HEAD[1]} independent lineages, so every actor holds TWO "
      f"live proposals on TWO distinct unsuperseded bases.  The "
      f"one-SHARED-BASE alternative REFUSES (K1b) — a second live "
      f"proposal on the same base is not offered — so the mints-first "
      f"bootstrap is FORCED; one lineage PER ACTOR does NOT refuse (V3 "
      f"forces and reaches width 8) and the rotation alternative pays "
      f"{HEAD[1] * (HEAD[1] - 1)} deliveries every round forever.")
print(f"    THE WIDTH.  max |D| = {_maxw[FLAG]} at d = 2 "
      f"({_maxw3[FLAG]} at d = 3) on the flagship and {_maxw[HEAD]} / "
      f"{_maxw3[HEAD]} on the R = 2 record; {len(_wit_bases)} bases of "
      f"the R = 2 record carry ONE width-16 direction set, "
      f"{len(_fwit_bases)} bases of the flagship, each verified event by "
      f"event against the committed sky and the committed order — "
      f"against the sprinkling-maxima HULL [{MXB[2][0]}, {MXB[2][1]}] = "
      f"M21 {DIMR[('M21', 2)]} u M31 {DIMR[('M31', 2)]} and W4c's "
      f"k^2 = 16.")
print(f"    THE CEILING LADDER.  ARBCHAIN*(m, 4) occupies the whole "
      f"interval 8, 10, 12, 14, 16 and its m = 4 member is C1-complete; "
      f"ARBCHAIN**(k) realizes k^2 = "
      f"{ {k: len(AC2[k]['D2']) for k in sorted(AC2)} } at k = "
      f"{sorted(AC2)}, and its k = 5 member — 25 directions — is "
      f"C1-COMPLETE at 157/157, widest full menu "
      f"{REPLAY['ARBCHAIN**(k=5)']['menu']}.  Height alignment is a "
      f"DESIGN REQUIREMENT the grammar's own idles satisfy, not an "
      f"obstruction; D66's residue 6 stays CLOSED.")
print(f"    THE UNIFORMITY.  WHOLE-record k = 4 records inside BOTH "
      f"d = 3 band columns: {[tag_of(k) for k in _k4_both[3]]} — the "
      f"flagship, at homogeneity {BUILT[FLAG][1][3]['h2']} and |D| >= 4 "
      f"{BUILT[FLAG][1][3]['h4']}, while 16 directions wide.  Inside the "
      f"homogeneity column alone: d = 2 "
      f"{[tag_of(k) for k in _k4_inband[2]]}, d = 3 "
      f"{[tag_of(k) for k in _k4_inband[3]]}.  Under the interior "
      f"POPULATION restriction (not an object): d = 3 "
      f"{[tag_of(k) for k in _k4_int_inband[3]]}.  Both sequences are "
      f"MONOTONE in R and the band is an interval they cross at "
      f"different R — the interior at R = 2, the whole record at R = 4 — "
      f"so the claim is the crossing, and that it happens while the "
      f"record carries k^2.  THE FIRST VERSION'S 'no whole k = 4 record "
      f"is in band at either depth' IS WITHDRAWN.")
print(f"    THE GAUGE.  {len(CO)} coboundary cells, C7 + PARITY + FREE, "
      f"five conventions, both depths; C7 obstructs at {len(_c7_pos)} "
      f"cells, FREE at {len(_free_pos)}, PARITY at {len(_par_pos)} (the "
      f"grammar ones all at ARBLOSE, on the DOUBLE GRID at k = 3 AND "
      f"k = 4 — D66's residue 5, swept).")
print(f"  SCOPE (pin §5): grammar layer; the swept family only; a "
      f"crystal certifies MECHANISMS, never objects (#440); no measure "
      f"claim at transport scope and therefore no typicality; omega is a "
      f"chart-size ratio along covers (D58); every width claim carries "
      f"the record's own B, its live Bl, its measured k*b and both "
      f"bounds; every gauge sentence carries the convention table; "
      f"transfer to the identified interactive click law runs through "
      f"paper 29's missing map (D59) and is not claimed; the missing map "
      f"is not touched.")
print(f"\n[d67] {PASS} PASS / {FAIL} FAIL   "
      f"[total wall clock {time.time() - T0:.1f}s]")
print("[exit protocol, pin K0/K6] exit 1 ONLY on ANCHOR breakage — the "
      "K0 family (K0a single sources, K0b the delivery controls' "
      "committed rows, K0c the sprinkling bands, the width range AND its "
      "two dimensional clusters, K0d D66's committed DOUBLE-GRID rows, "
      "K0f the R-prefix lemma and the round-1 committed g = 4 rows) and "
      "the two instrument anchors (K5a validation, K5e(i) D64's "
      "committed C7 row).  Every substantive negative exits 0.  "
      "anchor broken = " + str(ANCHOR_FAIL))
sys.exit(1 if ANCHOR_FAIL else 0)
