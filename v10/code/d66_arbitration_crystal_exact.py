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
    g = 2 is CONFLICT-RING(4, R) up to actor renaming: every profile
    column coincides at both depths (GATED in A1(d)), but the two
    event LISTS are NOT equal — the actor names differ (G00... vs
    C0...).  Round-1 MINOR 4/NIT 3: the earlier "(gated)" claim of an
    exact reproduction had no predicate behind it and its strong form
    is false; what is gated is the profile coincidence.
  * DOUBLE-GRID(g, R) — THE ROUND-1 REFEREE'S CONSTRUCTION, rebuilt
    here and gated (BLOCKER 1 / MAJOR 1 / MAJOR 2).  The same g x g
    actors, but ROWS AND COLUMNS CONFLICT CONCURRENTLY: every actor
    carries TWO live proposals on two distinct unsuperseded bases
    (`prop_options_in_view` blocks only a second live proposal on the
    SAME base), so no re-supply delivery is ever needed after the
    bootstrap.  Six independent base lineages are minted once (each
    seed alone, from genesis, before any delivery reaches it) and
    spread by 12 bootstrap deliveries; thereafter each round is 18
    proposals then 3 ROW arbitrations then 3 COLUMN arbitrations, and
    ZERO deliveries.  Consequence, which is the whole point: the
    depth-1 successor of a row arbitration on each of its three
    proposer registers is a COLUMN ARBITRATION, not a delivery — so
    the arbitration's directions multiply by 3 instead of 2 and the
    chart reaches |D| = 9 = k^2, W4c's own ceiling, SATURATED.
  * ARBCHAIN(m, k) — the same mechanism in the smallest possible
    record: one k-proposer arbitration whose k proposer registers are
    consumed by m further k-proposer arbitrations and by k - m
    deliveries, so |D_e(2)| = k*m + 2*(k - m) sweeps the WHOLE
    interval [2k, k^2] as m runs 0..k.  m = 0 is the RING/GRID case
    (2k) and m = k is the ceiling (k^2).

THE ROUND-1 CORRECTION THIS FILE CARRIES (BLOCKER 1).  The first
version of this receipt printed "the measured law in this family is
max |D| = 2k at d = 2 for a k-proposer grid".  That is FALSE as a law.
`2k` is the value of the true bound at Bl = 2, i.e. exactly when every
depth-1 successor of an arbitration is a two-register event (a
delivery) — which is what the RING and GRID blueprints impose and
nothing in the grammar forces.  The correct statement, refining W4c,
is |D_e(2)| <= sum over y in succ(e) of b(y) <= b(e)*Bl <= k^2 for a
k-proposer arbitration, and A3b REALIZES AND SATURATES it.

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


def double_grid(g, R):
    """DOUBLE-GRID(g, R) — THE ROUND-1 REFEREE'S CONSTRUCTION (BLOCKER 1),
    rebuilt from the review's blueprint prose with this unit's own driver
    and the committed layer's own menu.  Rows AND columns conflict
    CONCURRENTLY on SIX independent base lineages, so every actor holds
    two live proposals on two distinct unsuperseded bases and NO delivery
    is needed in any round.  Round order: all 18 proposals, then the 3 ROW
    arbitrations, then the 3 COLUMN arbitrations — which is what makes the
    depth-1 successor of a row arbitration on each proposer register a
    COLUMN ARBITRATION (live out-degree 3) rather than a delivery (2)."""
    ac = [[f"D{i}{j}" for j in range(g)] for i in range(g)]
    flat = [a for row in ac for a in row]
    b = B(tuple(flat))
    groups = ([[ac[i][j] for j in range(g)] for i in range(g)]
              + [[ac[i][j] for i in range(g)] for j in range(g)])
    # row seeds on the diagonal, column seeds two steps off it, so the six
    # seeds are pairwise distinct and each is UNTOUCHED when it mints
    seeds = ([ac[i][i] for i in range(g)]
             + [ac[(j + 2) % g][j] for j in range(g)])
    cur = [None] * len(groups)
    for gi, sd in enumerate(seeds):          # bootstrap: six mints ...
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
    for t in range(R):
        trips = []
        for gi, grp in enumerate(groups):    # ALL proposals of the round
            tp = [(a, cur[gi], 0 if a == seeds[gi] else 1) for a in grp]
            trips.append(tp)
            for x in tp:
                _pick(b, (x[0],), ('p',) + x, f"propose {x[0]}")
                if b.refusal:
                    return b
        for gi in range(len(groups)):        # rows first, then columns
            wk = frozenset({(seeds[gi], cur[gi], 0)})
            _pick(b, (seeds[gi],),
                  ('r', seeds[gi], frozenset(trips[gi]), wk),
                  f"arbitrate {seeds[gi]}")
            if b.refusal:
                return b
            cur[gi] = vname(cur[gi], wk, seeds[gi])
    return b


def arbchain(m, k=3):
    """ARBCHAIN(m, k): the smallest record in which a k-proposer
    arbitration's k proposer registers are consumed by m further
    k-proposer arbitrations and by k - m deliveries.  Returns (builder,
    index of THE arbitration).  |D_e(2)| = k*m + 2*(k - m): m = 0 is the
    RING/GRID case 2k, m = k is W4c's ceiling k^2."""
    A = [f"A{i}" for i in range(k)]
    S, T = [f"S{i}" for i in range(m)], [f"T{i}" for i in range(m)]
    F = [f"F{i}" for i in range(m, k)]
    b = B(tuple(A + S + T + F))

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
        dl(b, S[i], T[i], Y[i])
    g0 = [(a, X, 0 if a == A[0] else 1) for a in A]
    gi = [[(S[i], Y[i], 0), (A[i], Y[i], 1), (T[i], Y[i], 1)]
          for i in range(m)]
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
    tail = [x for i in range(m) for x in (A[i], S[i], T[i])]
    tail += [x for i in range(m, k) for x in (A[i], F[i - m])]
    for a in tail:
        _pick(b, (a,), ('n', a), f"idle {a}")
    return b, ebase


def actors_of(kind, P1, P2=None):
    if kind == 'RING':
        return [f"C{i}" for i in range(P1)]
    if kind == 'DGRID':
        return [f"D{i}{j}" for i in range(P1) for j in range(P1)]
    return [f"G{i}{j}" for i in range(P1) for j in range(P1)]


def get(key):
    """Build (once) and measure a swept configuration."""
    if key in BUILT:
        return BUILT[key]
    kind = key[0]
    t = time.time()
    b = (conflict_ring(key[1], key[2], key[3], key[4]) if kind == 'RING'
         else (double_grid(key[1], key[2]) if kind == 'DGRID'
               else conflict_grid(key[1], key[2])))
    pr = None if b.refusal else profile(poset_of(b.H))
    BUILT[key] = (b, pr, time.time() - t)
    return BUILT[key]


def tag_of(k):
    if k[0] == 'RING':
        return f"RING(M={k[1]},R={k[2]},sticky={k[3]},win={k[4]})"
    if k[0] == 'DGRID':
        return f"DOUBLE-GRID(g={k[1]},R={k[2]})"
    return f"GRID(g={k[1]},R={k[2]})"


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
WIDE = ('GRID', 3, 10)                  # the |D| = 6 width witness
DGW = ('DGRID', 3, 4)                   # THE WIDEST RECORD: |D| = 9 = k^2
DGS = ('DGRID', 3, 2)                   # its full-menu-replayed sibling
# ROUND-1 MAJOR 5 added RING(8, 6), RING(10, 6), RING(12, 6) and
# RING(10, 10): the parity reading of the odd-ring obstruction is then
# read at FIVE ring sizes (M = 4, 6, 8, 10, 12), and M = 12 is the row
# that could have killed it.  ROUND-1 BLOCKER 1 added the DOUBLE-GRIDs.
SWEEP = [('RING', 4, 6, 1, 'S'), ('RING', 4, 10, 1, 'S'),
         ('RING', 6, 6, 1, 'S'), HEAD, ('RING', 6, 14, 1, 'S'),
         ('RING', 8, 6, 1, 'S'), ('RING', 8, 10, 1, 'S'),
         ('RING', 10, 6, 1, 'S'), ('RING', 10, 10, 1, 'S'),
         ('RING', 12, 6, 1, 'S'),
         ('RING', 6, 10, 2, 'S'), ('RING', 6, 10, 0, 'S'),
         ('RING', 6, 10, 1, 'R'), ('RING', 6, 10, 1, 'ALT'),
         ('GRID', 2, 10), ('GRID', 3, 4), ('GRID', 3, 6), WIDE,
         ('GRID', 4, 4), DGS, DGW]

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
    print(f"    DOUBLE-GRID(g, R) [round-1 BLOCKER 1, the REFEREE's "
          f"construction]: the same g x g actors, but ROWS AND COLUMNS "
          f"CONFLICT CONCURRENTLY on six independent base lineages "
          f"minted once in a bootstrap of 6 mints + 2g(g-1) deliveries; "
          f"each round is then g^2*2 proposals + g ROW arbitrations + g "
          f"COLUMN arbitrations and ZERO deliveries.")
    print(f"    ARBCHAIN(m, k) [round-1 BLOCKER 1]: one k-proposer "
          f"arbitration whose k proposer registers are consumed by m "
          f"further k-proposer arbitrations and k - m deliveries, so "
          f"|D_e(2)| = k*m + 2*(k - m) sweeps [2k, k^2].")
    print(f"    SKY-B depths measured = (2, 3); committed SKYB_DEPTH = "
          f"{SKYB_DEPTH}.  Full-menu replay budgets: "
          f"{FULLMENU_BUDGET:.0f}s per record, "
          f"{WIDE_REPLAY_BUDGET:.0f}s for the wide record.")
    print(f"    swept configurations = {len(SWEEP)}: "
          + "; ".join(tag_of(k) for k in SWEEP))

if PROBE:
    for kk in (('RING', 4, 6, 1, 'S'), ('GRID', 3, 4), DGS):
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
print("  most one arbitration in any record, so #proposals >= k * #arbs "
      "and an")
print("  arbitration's share of the events of a record is at most 1/(k+1) "
      "where k is")
print("  the smallest proposer count in it.  Deliveries only lower it.")
print("  THE STEP THE PRINTED PROOF USED TO SKIP (round-1 MINOR 3).  "
      "`View.resolved` is")
print("  VIEW-RELATIVE — it is rebuilt from the arbitrations in ONE "
      "event's causal")
print("  past — so by itself it does not exclude two causally "
      "INCOMPARABLE arbitrations")
print("  each seeing the same triple live.  The register argument closes "
      "it: two")
print("  arbitrations consuming the same proposal triple both carry that "
      "proposer's")
print("  register in `regs_of`, and `event_poset` makes every later event "
      "touching a")
print("  register inherit the whole past of the previous one — so they "
      "are CAUSALLY")
print("  COMPARABLE, the later one's View has the triple in `resolved`, "
      "its component")
print("  is gone from `arb_components_in_view`, and `admissible` returns "
      "False.  The")
print("  conclusion is then gated numerically per record: #proposals = "
      "sum of proposer")
print("  counts AND no consumed triple occurs twice.")
_bud_ok = True
_norepeat = True
_share_rows = []
for k in SWEEP:
    b = BUILT[k][0]
    H = b.H
    arbs = [e for e in H if e[0] == 'r']
    props = [e for e in H if e[0] == 'p']
    ks = [len({t[0] for t in e[2]}) for e in arbs]
    consumed = sum(ks)
    _cons = Counter(t for e in arbs for t in e[2])
    if any(c > 1 for c in _cons.values()) or len(_cons) != consumed:
        _norepeat = False
    kmin = min(ks)
    kcon = min([x for x in ks if x >= 2], default=kmin)   # conflict groups
    sh = arbshare(H)
    bound = Fr(1, kmin + 1)
    if not (consumed == len(props) and sh <= bound):
        _bud_ok = False
    _share_rows.append((tag_of(k), len(H), len(arbs), kmin, sh, bound,
                        sum(1 for e in H if e[0] == 'd'), kcon,
                        Fr(1, kcon + 1)))
for (tg, n, na, kmin, sh, bd, nd, kc, bc) in _share_rows:
    print(f"    {tg:38s} n={n:4d} arbs={na:3d} (k_min={kmin}, "
          f"k_conflict={kc}) deliveries={nd:3d} arb share {sh} "
          f"(~{float(sh):.4f}) vs bound 1/(k_min+1) = {bd} "
          f"(~{float(bd):.4f})" + ("   <== SATURATED" if sh == bd else "")
          + (f"; = 1/(k_conflict+1) = {bc}   <== THE CONFLICT GROUPS "
             f"SATURATE" if sh == bc and bc != bd else ""))
_sat = [r[0] for r in _share_rows if r[4] == r[5]]
_sat2 = [r[0] for r in _share_rows if r[4] == r[8]]
print(f"    TWO BOUNDS, AND WHICH ONE A RECORD SATURATES.  `k_min` is "
      f"the smallest proposer count anywhere in the record, and "
      f"1/(k_min+1) is the only GENERAL bound.  The DOUBLE-GRIDs mint "
      f"their six base lineages with SINGLE-proposer arbitrations in the "
      f"bootstrap, so their k_min is 1 and their general bound is 1/2 — "
      f"but their CONFLICT GROUPS all have k = 3 and their share is "
      f"EXACTLY 1/(3+1) = 1/4, i.e. the rounds saturate and the "
      f"bootstrap spends none of the slack.  Records saturating the "
      f"general bound: {_sat}.  Records whose share equals "
      f"1/(k_conflict+1): {_sat2}.")
check("A1(b) [WHAT THIS GATE MEASURES, round-1 NIT 2: not the prose "
      "inequality #proposals >= k*#arbs but the STRICTLY STRONGER "
      "per-arbitration equality #proposals = SUM of proposer counts, "
      "together with 'no consumed triple occurs twice'] THE ARBITRATION "
      "SHARE IS BOUNDED BY THE GRAMMAR AND THE BOUND IS ATTAINED AT TWO "
      "DIFFERENT k.  No record of this layer can be more than 1/(k+1) "
      "arbitration; the delivery-free ring attains 1/3 at k = 2 and the "
      "DELIVERY-FREE DOUBLE-GRID attains 1/4 at k = 3.  ROUND-1 MAJOR 1, "
      "CARRIED: the earlier reading — that re-supplying a conflict COSTS "
      "a delivery, so the tiling records must run at 25.6% rather than "
      "33.3% — is a property of the ROTATING PAIR schedule only.  A "
      "schedule in which every actor carries TWO concurrent conflicts "
      "needs no in-round delivery at all and saturates its own bound",
      _bud_ok and _norepeat and len(_sat) > 0 and len(_sat2) > len(_sat),
      f"records checked = {len(_share_rows)}, proposal-consumption "
      f"equalities = {len(_share_rows)}, repeated consumed triples = 0 "
      f"({_norepeat}), general-bound violations = 0, records saturating "
      f"1/(k_min+1) = {_sat}, records at 1/(k_conflict+1) = {_sat2}")

# ---- A1(d) the duplicate object, said out loud ---------------------------
print("\n[A1(d) THE DUPLICATE IN THE SWEEP, SAID OUT LOUD (round-1 "
      "MINOR 4 / NIT 3) — the module docstring used to claim `g = 2 "
      "reproduces CONFLICT-RING(4, R) exactly (gated)`; no predicate "
      "tested it and the strong form is FALSE]")
_g2, _r4 = ('GRID', 2, 10), ('RING', 4, 10, 1, 'S')
_pg, _pr4 = BUILT[_g2][1], BUILT[_r4][1]
_lists_equal = (list(BUILT[_g2][0].H) == list(BUILT[_r4][0].H))
_cols = ('n', 'h2', 'h3', 'h4', 'max', 'mean', 'om')
_rows_equal = all(_pg[d][c] == _pr4[d][c] for d in (2, 3) for c in _cols)
_shapes_equal = ([e[0] for e in BUILT[_g2][0].H]
                 == [e[0] for e in BUILT[_r4][0].H])
print(f"    event LISTS identical = {_lists_equal} (they are not: the "
      f"actor names differ, G00... vs C0...); event-KIND sequences "
      f"identical = {_shapes_equal}; every profile column identical at "
      f"both depths = {_rows_equal}")
check("A1(d) GRID(g=2, R) AND RING(M=4, R) ARE THE SAME OBJECT UP TO "
      "ACTOR RENAMING, AND THAT IS GATED RATHER THAN ASSERTED.  Their "
      "event-kind sequences coincide and every profile column coincides "
      "at both depths, while their event lists are NOT literally equal "
      "(the actor names differ).  So the sweep contains one duplicate "
      "object under two names, which D63's round-1 MINOR 8 asked to be "
      "said out loud, and the docstring's earlier unqualified '(gated)' "
      "is replaced by this predicate",
      _rows_equal and _shapes_equal and not _lists_equal,
      f"profile columns equal at both depths = {_rows_equal}; kind "
      f"sequences equal = {_shapes_equal}; event lists equal = "
      f"{_lists_equal}")

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
_kof = {k: max((len({t[0] for t in e[2]}) for e in BUILT[k][0].H
                if e[0] == 'r'), default=0) for k in SWEEP}
print(f"      (round-1 MINOR 5) the in-band AND wide set BY PROPOSER "
      f"COUNT k: { {tag_of(k): _kof[k] for k in BOTH} } — every member "
      f"has k = 2, but they are not all RINGS: "
      f"{sorted(tag_of(k) for k in BOTH if k[0] != 'RING')} is a GRID "
      f"blueprint (and, by A1(d), the M = 4 ring under another name).")
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
print("  by an arbitration is a BIRTH WIRE with NO P-successor.  "
      "Replacing |regs(x)| by")
print("  the number of registers of x that RECUR (the live out-degree "
      "b(x)) in W4b's")
print("  own proof gives |D_e(d)| <= Bl^d with Bl = max b(x) — and for "
      "an arbitration")
print("  b <= #proposers = |regs| - 1.  CONSEQUENCE: a TWO-proposer "
      "conflict record")
print("  has Bl = 2 exactly like a delivery circuit and CANNOT exceed 4 "
      "at d = 2,")
print("  despite carrying 3-register events.  Width past 4 needs 3+ "
      "PROPOSERS, not")
print("  merely 3+ registers — W4b's necessary condition is not "
      "sufficient.")
print("\n  W4c's PROOF, WRITTEN IN (round-1 MAJOR 3: the [THEOREM] tag "
      "was carried by a")
print("  per-record census, i.e. by a measurement, and its printed "
      "reason — '`regs_of`")
print("  places a version name in exactly one event's register set' — "
      "was at the wrong")
print("  level, since `regs_of` is a function of ONE event while "
      "'occurs once' is a")
print("  property of the RECORD.  Four steps, each checked against the "
      "committed")
print("  d42b1 source, whose lines are quoted below:")
print("    (1) A version occupies a register ONLY where it is born.  "
      "`regs_of` returns")
print("        {a} for p/n, {sender, receiver} for d, {a, ('mw',a,pk)} "
      "for m, and")
print("        props u {vname(base, op[3], op[1])} for r.  A DELIVERY OF "
      "VERSION v")
print("        THEREFORE CARRIES v IN ITS PAYLOAD op[3] AND DOES NOT "
      "OCCUPY v's")
print("        REGISTER — which is exactly why the minted wire is dead.  "
      "Merge-created")
print("        names (`mname`) never appear in any `regs_of` at all.")
print("    (2) So a version register can recur only if TWO DISTINCT "
      "ARBITRATIONS MINT")
print("        THE SAME `vname` — i.e. share the base, the winner key's "
      "value tuple,")
print("        the winner key's author tuple, and the initiator.")
print("    (3) Two such arbitrations share at least one PROPOSER "
      "REGISTER (the winner")
print("        authors, and the initiator, are proposers of both).  In "
      "`event_poset`,")
print("        once an event touches register r it becomes last[r] and "
      "every later")
print("        event touching r inherits its whole past — so the two are "
      "CAUSALLY")
print("        COMPARABLE.")
print("    (4) The later one's `View` therefore contains the earlier "
      "arbitration, so")
print("        base is in view.superseded; `arb_components_in_view` "
      "SKIPS components")
print("        whose base is superseded, `admissible` finds no matching "
      "component and")
print("        returns False.  THE SECOND ARBITRATION IS INADMISSIBLE.  "
      "QED.")
_Q = {
    'regs_of(d) is {sender, receiver}, not the payload':
        "if k == 'd': return frozenset([op[1], op[2]])",
    'regs_of(r) is proposers u {the minted vname}':
        "return frozenset(props | {vname(base, op[3], op[1])})",
    'event_poset inherits the whole past through a register':
        "pred[j] |= pred[last[r]] | {last[r]}",
    'an arbitration supersedes its base in the View':
        "self.superseded.add(base)",
    'arb_components_in_view SKIPS a superseded base':
        "if base in view.superseded: continue",
    'admissible(r) refuses when no component matches':
        "if not match: return False, None"}
_quote_ok = all(s in _st for s in _Q.values())
for lab, s in _Q.items():
    print(f"      [committed d42b1, line "
          f"{_st[:_st.index(s)].count(chr(10)) + 1 if s in _st else '??'}] "
          f"{s}    <== {lab}")
check("A2(b0) [MAJOR 3, THE THEOREM TAG NOW CARRIES AN ARGUMENT] W4c's "
      "LOAD-BEARING STEP IS PROVED FROM THE COMMITTED LAYER, NOT "
      "MEASURED.  Every line the four-step proof leans on is quoted "
      "above and gated to occur VERBATIM in the committed "
      "d42b1_transport_exact.py: that a delivery's registers are "
      "{sender, receiver} and not the payload version; that an "
      "arbitration's registers are its proposers plus the minted name; "
      "that `event_poset` makes any two events sharing a register "
      "causally comparable; that an arbitration supersedes its base; "
      "that `arb_components_in_view` skips a superseded base; and that "
      "`admissible` refuses an arbitration with no matching component.  "
      "The per-record census below is kept as EVIDENCE beside the proof, "
      "not as its warrant",
      _quote_ok, f"source lines gated verbatim = "
      f"{sum(1 for s in _Q.values() if s in _st)} of {len(_Q)}")
print("\n  THE WIDTH LAW, CORRECTED (round-1 BLOCKER 1).  W4c's bound is "
      "NOT attained at")
print("  2k as a law: `2k` is the value of the refined bound when every "
      "depth-1")
print("  successor of an arbitration is a TWO-register event, i.e. a "
      "delivery, which")
print("  is what the RING and GRID blueprints impose and nothing in the "
      "grammar")
print("  forces.  THE REFINEMENT.  Every P-edge raises the height by at "
      "least 1, so a")
print("  depth-2 direction is reached from e by a P-path of length 1 or "
      "2, i.e.")
print("       D_e(2)  SUBSET OF  succ(e)  UNION  { succ(y) : y in "
      "succ(e) },")
print("  an EXACT containment, gated below at every event of every "
      "record.  When e")
print("  has at least one successor at height h(e) + 1 — i.e. when no "
      "P-edge out of")
print("  e skips a layer — the first term contributes nothing at depth 2 "
      "and the")
print("  bound is the sharp |D_e(2)| <= SUM_{y in succ(e)} b(y) <= b(e) * "
      "Bl <= k * Bl,")
print("  which is <= k^2 = W4c's own ceiling for a k-proposer "
      "arbitration.  A3b")
print("  builds a record in which an arbitration's successors are "
      "ARBITRATIONS and")
print("  SATURATES k^2 = 9.  The exceptions to the SHARP form are "
      "counted and")
print("  CHARACTERISED below rather than hidden: they are exactly the "
      "events all of")
print("  whose P-successors sit two or more layers above them (a "
      "height-skipping")
print("  edge into a terminal arbitration at a record's end).")
def _skyB(C, hs, e, d):
    """SKY-B's own definition (d47a, kind 'B') with the height vector
    hoisted out of the loop — the committed `sky` recomputes `heights`
    on every call, which is O(n^3) over a whole record.  GATED below to
    agree with the committed `sky` event for event."""
    return [f for f in range(len(C)) if C[e][f] and hs[f] - hs[e] == d]


_skyB_ok = True
for _kk in (HEAD, ('GRID', 3, 4)):
    _Ck = poset_of(BUILT[_kk][0].H)
    _hk = heights(_Ck)
    for _d in (2, 3):
        for _e in range(len(_Ck)):
            if set(_skyB(_Ck, _hk, _e, _d)) != set(sky(_Ck, _e, 'B', _d)[0]):
                _skyB_ok = False
check("A2(b*) THE HOISTED SKY-B AGREES WITH THE COMMITTED d47a `sky` "
      "EVENT FOR EVENT.  The bulk bound-checking below reads SKY-B with "
      "the height vector computed once per record instead of once per "
      "event; that is an optimisation, not a definition, and it is gated "
      "against the committed instrument at every event of two whole "
      "records at both depths.  Every chart this unit EXHIBITS is still "
      "read from the committed `sky` directly",
      _skyB_ok, f"records compared event for event at both depths = 2 "
      f"({tag_of(HEAD)}, {tag_of(('GRID', 3, 4))}); disagreements = 0")

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
        C = poset_of(H)
    else:
        H, pr, tg = BUILT[k][0].H, BUILT[k][1], tag_of(k)
        C = poset_of(H)
    Bmax = max(len(regs_of(e)) for e in H)
    # the immediate-successor relation P, from event_poset's own `last`
    succ = defaultdict(set)
    last = {}
    for j, op in enumerate(H):
        for r in regs_of(op):
            if r in last:
                succ[last[r]].add(j)
        for r in regs_of(op):
            last[r] = j
    bdeg = {j: len(succ[j]) for j in range(len(H))}
    Bl = max(bdeg.values())
    # THE REFINED BOUND, gated event by event: the EXACT containment
    # first, then the SHARP sum form with its exceptions characterised
    _hs = heights(C)
    for e in range(len(H)):
        d2 = len(_skyB(C, _hs, e, 2))
        reach = set(succ[e])
        for y in succ[e]:
            reach |= succ[y]
        if d2 > len(reach):
            _ref_ok = False
        if d2 > sum(bdeg[y] for y in succ[e]):
            _sharp_exc += 1
            if any(_hs[y] == _hs[e] + 1 for y in succ[e]):
                _sharp_explained = False
    # every version register occurs in exactly one event
    occ = Counter(r for e in H for r in regs_of(e)
                  if not isinstance(r, str))
    vmulti = sum(1 for r, c in occ.items() if c > 1)
    if vmulti:
        _mint_ok = False
    kmax = max([len({t[0] for t in e[2]}) for e in H if e[0] == 'r'],
               default=0)
    # NIT 1: live out-degree is <=, not =, the proposer count
    _lt = sum(1 for j, op in enumerate(H) if op[0] == 'r'
              and bdeg[j] < len({t[0] for t in op[2]}))
    for d in (2, 3):
        if pr[d]['max'] > Bmax ** d or pr[d]['max'] > Bl ** d:
            _w4_ok = False
    _bl_rows.append((tg, Bmax, Bl, kmax, pr[2]['max'], pr[3]['max'],
                     len(occ), vmulti, _lt))
for (tg, Bm, Bl, km, m2, m3, nv, vm, lt) in _bl_rows:
    print(f"    {tg:38s} B={Bm} (W4b bound {Bm**2} at d=2), live Bl={Bl} "
          f"(W4c bound {Bl**2}), max proposers k={km}: measured max|D| "
          f"d2={m2} d3={m3}; version registers {nv}, occurring twice = "
          f"{vm}; arbitrations with b < k = {lt}")
print(f"    (round-1 NIT 1) 'an arbitration's live out-degree IS its "
      f"proposer count' is an INEQUALITY b <= k, not an equality: the "
      f"last arbitration of each group at a record's end has live "
      f"out-degree 0.  Arbitrations with b < k, per record: "
      f"{[r[8] for r in _bl_rows]}.  Nothing turns on it — the bound "
      f"uses the maximum — but the gate is labelled for what it "
      f"measures.")
check("A2(b) BOTH BOUNDS HOLD ON EVERY RECORD, THE REFINED BOUND HOLDS "
      "EVENT BY EVENT, AND W4c IS THE ONE THAT BINDS.  Across every "
      "record built here every version register occurs in EXACTLY ONE "
      "event's `regs_of` — as A2(b0) proves it must — so an "
      "arbitration's live out-degree is AT MOST its proposer count.  "
      "Hence the two-proposer conflict ring — 3 registers per "
      "arbitration, W4b bound 9 — is held to max |D| = 4 at d = 2, "
      "exactly the delivery ceiling, and the records with 3 and 4 "
      "proposers are the ones that pass it.  D63's residue 1 is answered "
      "with a correction to its own necessity statement.  AND (round-1 "
      "BLOCKER 1) the EXACT containment D_e(2) SUBSET succ(e) u "
      "succ(succ(e)) is verified at EVERY EVENT OF EVERY RECORD, and the "
      "SHARP sum form |D_e(2)| <= SUM_{y in succ(e)} b(y) holds "
      "everywhere except at events whose every P-successor skips a "
      "height layer — the exceptions are counted AND characterised, "
      "never waved through.  The sharp form is the bound A3b saturates "
      "at k^2 = 9",
      _w4_ok and _mint_ok and _ref_ok and _sharp_explained,
      f"records checked = {len(_bl_rows)}, W4b/W4c violations = 0, "
      f"exact-containment violations = 0 ({_ref_ok}), events where the "
      f"SHARP sum form does not apply = {_sharp_exc} (every one of them "
      f"has NO P-successor at height + 1, i.e. its only successors skip "
      f"a layer: {_sharp_explained}), version registers occurring more "
      f"than once = 0")

# ---- the interior control ------------------------------------------------
print("\n[A2(c) THE INTERIOR CONTROL (D60's C7 excision) ON EVERY SWEPT "
      "RECORD AND AT BOTH DEPTHS — round-1 MINOR 2 and MAJOR 2: the "
      "first version ran it on 5 of 15 records and at d = 2 only, while "
      "drawing a MECHANISM conclusion from it ('the grids' shortfall is "
      "not an ends effect'), and the missing rows are the ones that "
      "REFUTE that conclusion]")


def interior_of(H):
    C = poset_of(H)
    hs = heights(C)
    lo, hi = min(hs), max(hs)
    return C, {e for e in range(len(C)) if lo + 2 <= hs[e] <= hi - 3}


def _pos(h, d):
    return ('IN ' if BAND[d][0] <= h <= BAND[d][1]
            else ('ABOVE' if h > BAND[d][1] else 'below'))


INT = {}
_moved_in = []
for k in SWEEP:
    C, popn = interior_of(BUILT[k][0].H)
    pi = profile(C, popn)
    INT[k] = pi
    pf = BUILT[k][1]
    cells = []
    for d in (2, 3):
        cells.append(f"d={d} {float(pf[d]['h2']):.4f}[{_pos(pf[d]['h2'], d)}]"
                     f" -> {float(pi[d]['h2']):.4f}[{_pos(pi[d]['h2'], d)}]")
        if (not (BAND[d][0] <= pf[d]['h2'] <= BAND[d][1])
                and BAND[d][0] <= pi[d]['h2'] <= BAND[d][1]):
            _moved_in.append((tag_of(k), d))
    print(f"    {tag_of(k):38s} n {pf[2]['n']:4d}->{pi[2]['n']:4d}  "
          + "  |  ".join(cells)
          + f"  max|D| d2 {pf[2]['max']}->{pi[2]['max']} d3 "
          f"{pf[3]['max']}->{pi[3]['max']}")
_int_up = sum(1 for k in INT for d in (2, 3)
              if INT[k][d]['h2'] > BUILT[k][1][d]['h2'])
_int_ge = all(INT[k][d]['h2'] >= BUILT[k][1][d]['h2']
              for k in INT for d in (2, 3))
_int_maxkept = all(INT[k][d]['max'] == BUILT[k][1][d]['max']
                   for k in INT for d in (2, 3))
print(f"    EXCISION MOVES A RECORD INTO THE BAND AT: {_moved_in} — so "
      f"the earlier sentence 'the grids' shortfall is NOT an ends effect "
      f"the way D63's band membership was' is REFUTED at d = 3 for the "
      f"k = 3 grids, which is exactly D63's ends effect.")
check("A2(c) THE WIDTH IS THE CIRCUIT'S, NOT THE PREFIX'S — AND THE BAND "
      "HALF IS AN ENDS PROPERTY AT BOTH DEPTHS, WHICH THE FULL TABLE "
      "SHOWS AND THE OLD FIVE-RECORD TABLE HID.  Excising the bottom two "
      "and top three height layers never LOWERS homogeneity and leaves "
      "max |D| unchanged at both depths on every swept record, so no "
      "wide chart anywhere is a boundary artefact; and at d = 3 the same "
      "excision carries k = 3 grids INTO the band while they still carry "
      "max |D| = 6, which is the round-1 correction to this unit's own "
      "mechanism sentence",
      _int_ge and _int_maxkept and len(INT) == len(SWEEP),
      f"records controlled = {len(INT)} of {len(SWEEP)} at BOTH depths; "
      f"(record, depth) cells where interior homogeneity strictly rises "
      f"= {_int_up} of {2 * len(INT)}; never falls = {_int_ge}; interior "
      f"max|D| = full max|D| everywhere = {_int_maxkept}; cells the "
      f"excision moves INTO the band = {len(_moved_in)}")

# ======================================================================
# A3 — THE WIDTH VERDICT
# ======================================================================
print("\n[A3 THE WIDTH VERDICT — does ANY conflict record carry "
      "|D| >= 5 at d = 2?  This is the delivery ceiling's door (D63 §4, "
      "residue 1)]")
WID = {}
for k in SWEEP:
    C = poset_of(BUILT[k][0].H)
    hs = heights(C)
    WID[k] = Counter(len(_skyB(C, hs, e, 2)) for e in range(len(C)))
    print(f"    {tag_of(k):38s} width histogram at d = 2: "
          f"{dict(sorted(WID[k].items()))}")
_maxw = {k: BUILT[k][1][2]['max'] for k in SWEEP}
DOOR = [k for k in SWEEP if _maxw[k] >= 5]
print(f"    max |D| at d = 2 by proposer count k: "
      + ", ".join(f"{tag_of(k)} k={_kof[k]} -> {_maxw[k]}"
                  for k in [x for x in (HEAD, WIDE, ('GRID', 4, 4), DGW)
                            if x in BUILT]))
print(f"    THE DELIVERY COMPARATOR IS DEPTH-LABELLED (round-1 MINOR 7). "
      f"'max |D| = 4 for any delivery circuit' is a d = 2 statement: "
      f"D63's committed note reports that AT d = 3 its max |D| reaches "
      f"5 at 14 records and 6 at 4 more, i.e. 18 of its 38 delivery "
      f"configurations EXCEED 4 at d = 3.  Re-run here: DR(8,10,8) "
      f"max|D| d2={P_DR[2]['max']} d3={P_DR[3]['max']}, BRICK(8,14) "
      f"d2={P_BK[2]['max']} d3={P_BK[3]['max']}.")


def _witness(kk, tagline):
    Hw = BUILT[kk][0].H
    Cw = poset_of(Hw)
    hw = heights(Cw)
    ew = max(range(len(Cw)), key=lambda e: len(sky(Cw, e, 'B', 2)[0]))
    dirs, rows = sky(Cw, ew, 'B', 2)
    outp = out_reg(Hw, 'tuple')
    W = words_from(outp, hw, ew, 2)
    succ = defaultdict(set)
    last = {}
    for j, op in enumerate(Hw):
        for r in regs_of(op):
            if r in last:
                succ[last[r]].add(j)
        for r in regs_of(op):
            last[r] = j
    kw = len({t[0] for t in Hw[ew][2]}) if Hw[ew][0] == 'r' else 0
    print(f"\n    {tagline} — {tag_of(kk)}, base event index {ew}: "
          f"{Hw[ew][0]}-event by {Hw[ew][1]}, height {hw[ew]}, "
          f"{len(regs_of(Hw[ew]))} registers ({kw} proposers), live "
          f"out-degree b = {len(succ[ew])}")
    print(f"      D(1) = {sorted(succ[ew])} with kinds "
          f"{[Hw[f][0] for f in sorted(succ[ew])]} and live out-degrees "
          f"{[len(succ[f]) for f in sorted(succ[ew])]}; the refined bound "
          f"SUM_y b(y) = {sum(len(succ[y]) for y in succ[ew])}, k*Bl "
          f"ceiling = {kw * max(len(v) for v in succ.values())}, k^2 = "
          f"{kw * kw}")
    print(f"      SKY-B(d=2) chart, read from the COMMITTED d47a `sky` "
          f"directly: |D| = {len(dirs)}, directions {sorted(dirs)}")
    for f in sorted(dirs):
        print(f"        direction {f:3d}: kind {Hw[f][0]} by {Hw[f][1]}, "
              f"height {hw[f]} (= {hw[ew]} + {hw[f]-hw[ew]}), ordered "
              f"after the base in the committed poset = {Cw[ew][f]}; "
              f"P-paths (raw ; role) = "
              + " | ".join(f"{[str(x)[:14] for x in w]} ; {o}"
                           for (w, o) in sorted(W.get(f, ()), key=repr)))
    ok = (set(W) == set(dirs) and len(dirs) >= 5
          and len(set(dirs)) == len(dirs)
          and all(Cw[ew][f] and hw[f] == hw[ew] + 2 for f in dirs))
    return ok, len(dirs), kw


if DOOR:
    kk = max(DOOR, key=lambda k: _maxw[k])
    _wit_ok, _wn, _wk = _witness(kk, "THE WIDEST WITNESS IN THE UNIT")
    _wit8, _w8n, _w8k = _witness(
        ('GRID', 4, 4), "THE 4-PROPOSER GRID WITNESS (the round-1 review "
        "verified this one event by event)")
    _wit_ok = _wit_ok and _wit8
else:
    _wit_ok = False
    _wn = _wk = 0
check("A3 [THE DOOR DECIDES] " + (
      "**THE DELIVERY CEILING IS BROKEN BY CONFLICT.**  Conflict records "
      "carry |D| >= 5 at d = 2 — the first records in this campaign to "
      "do so — and the witness is exhibited event by event: its chart is "
      "read from the COMMITTED d47a `sky` directly, every direction is "
      "verified to be ordered after the base in the committed poset and "
      "to sit exactly two height layers above it, and every direction's "
      "P-paths are printed.  This is not an instrument artefact and it "
      "is not a chart-counting convention: the base event is an "
      "arbitration over DISTINCT PROPOSERS whose live out-degree is its "
      "proposer count, and the width is exactly what W4c allows and "
      "W4b's 'three registers' never could.  ROUND-1 BLOCKER 1: the "
      "widest chart in this unit is NOT 2k — see A3b, where a "
      "delivery-free schedule reaches k^2" if DOOR else
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
         (DGS, FULLMENU_BUDGET),
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
      "refused or was ambiguous.  WHERE THE PREFIX BITES (round-1 "
      "MINOR 1): the A-IIIa verdict is read on GRID(3,10), whose "
      "full-menu replay is BUDGET-CUT, and on GRID(3,6) and GRID(4,4), "
      "which are not full-menu replayed at all; the complete wide "
      "records that ARE replayed end to end are GRID(3,4) and "
      "DOUBLE-GRID(3,2), and GRID(3,4) is now in the A4 census "
      "(A4SET) so the decisive computation has a C1-complete member.  "
      "The restricted-menu drive already establishes admissibility of "
      "every event against the whole prefix, so what the untested tail "
      "lacks is exactly the 'offered among ALL actors' property, which "
      "is what D60's C1 grade is",
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
# A3b — THE ROUND-1 REFEREE'S CONSTRUCTIONS, REBUILT AND GATED
# ======================================================================
print("\n[A3b THE ROUND-1 REVIEW'S OWN CONSTRUCTIONS, REBUILT HERE WITH "
      "THIS UNIT'S DRIVER AND GATED (BLOCKER 1, MAJOR 1, MAJOR 2).  The "
      "review supplied a DOUBLE-GRID whose 3-proposer arbitrations carry "
      "|D| = 9 at d = 2 in a record with ZERO in-round deliveries.  "
      "House style: a round-supplied object is credited to the round and "
      "then GATED like any other, never taken on the reviewer's word]")
_dg = BUILT[DGW][0]
_dgC = poset_of(_dg.H)
_dgh = heights(_dgC)
_dgpr = BUILT[DGW][1]
_dgW = {e: sky(_dgC, e, 'B', 2)[0] for e in range(len(_dgC))}
_dghist = dict(sorted(Counter(len(v) for v in _dgW.values()).items()))
_dgsucc = defaultdict(set)
_last = {}
for j, op in enumerate(_dg.H):
    for r in regs_of(op):
        if r in _last:
            _dgsucc[_last[r]].add(j)
    for r in regs_of(op):
        _last[r] = j
_dgb = {j: len(_dgsucc[j]) for j in range(len(_dg.H))}
_dgBl = max(_dgb.values())
_dgk = max(len({t[0] for t in e[2]}) for e in _dg.H if e[0] == 'r')
_ngrp = 2 * DGW[1]                   # g row groups + g column groups
_boot = 2 * _ngrp + _ngrp * (DGW[1] - 1)   # 2 events per mint + spreads
_dels = [j for j, e in enumerate(_dg.H) if e[0] == 'd']
_inround = [j for j in _dels if j >= _boot]
NINE = sorted(e for e in _dgW if len(_dgW[e]) == 9)
for kk in (DGS, DGW):
    bb, pp = BUILT[kk][0], BUILT[kk][1]
    print(f"    {tag_of(kk):26s} n={len(bb.H):4d} refusal={bb.refusal} "
          f"max menu hits={bb.maxhits} kinds="
          f"{dict(sorted(Counter(e[0] for e in bb.H).items()))} arb share "
          f"{arbshare(bb.H)} vs bound 1/(k+1) = "
          f"{Fr(1, _dgk + 1)}"
          + ("   <== SATURATED" if arbshare(bb.H) == Fr(1, _dgk + 1) else ""))
    for d in (2, 3):
        x = pp[d]
        print(f"      d={d}: homogeneity {x['h2']} (~{float(x['h2']):.4f}) "
              f"[{_pos(x['h2'], d)} the sprinkling band "
              f"[{float(BAND[d][0]):.4f}, {float(BAND[d][1]):.4f}]], "
              f"|D|>=4 {x['h4']} (~{float(x['h4']):.4f}), max|D| "
              f"{x['max']}, mean|D| {float(x['mean']):.3f}, omega "
              f"{float(x['om']):.4f}")
print(f"    {tag_of(DGW)} width histogram at d = 2: {_dghist}")
print(f"    deliveries: {len(_dels)} in total, at event indices "
      f"{_dels}; the bootstrap is the first {_boot} events, and the "
      f"number of deliveries occurring in ANY round is {len(_inround)}.")
print(f"    THE NINE |D| = 9 CHARTS, verified against the COMMITTED "
      f"d47a `sky` and the COMMITTED `poset_of` order, one line each:")
_nine_ok = True
for e in NINE:
    dirs = _dgW[e]
    okc = (len(set(dirs)) == 9 and _dg.H[e][0] == 'r'
           and len({t[0] for t in _dg.H[e][2]}) == 3
           and all(_dgC[e][f] and _dgh[f] == _dgh[e] + 2 for f in dirs))
    _nine_ok = _nine_ok and okc
    print(f"      base {e:3d}: r-event by {_dg.H[e][1]}, height "
          f"{_dgh[e]:2d}, {len(regs_of(_dg.H[e]))} registers, "
          f"{len({t[0] for t in _dg.H[e][2]})} proposers, b(e)="
          f"{_dgb[e]}; D(1)={sorted(_dgsucc[e])} kinds "
          f"{[_dg.H[f][0] for f in sorted(_dgsucc[e])]} out-degrees "
          f"{[_dgb[f] for f in sorted(_dgsucc[e])]}; |D(2)|={len(dirs)} "
          f"directions {sorted(dirs)}; all distinct / ordered after the "
          f"base / at height+2 = {okc}")
_dgref_ok = all(len(_dgW[e]) <= sum(_dgb[y] for y in _dgsucc[e])
                for e in _dgW)
_dg_w4c = all(len(_dgW[e]) <= _dgBl ** 2 for e in _dgW)
print(f"    W4c on this record: Bl = {_dgBl}, bound Bl^2 = "
      f"{_dgBl ** 2}, measured max |D| = {_dgpr[2]['max']} — the "
      f"k^2 CEILING IS SATURATED, and the refined bound "
      f"|D_e(2)| <= SUM_y b(y) holds at every event = {_dgref_ok}.")
_dgocc = Counter(r for e in _dg.H for r in regs_of(e)
                 if not isinstance(r, str))
_dgrep = REPLAY.get(tag_of(DGS))
print(f"    FORCEDNESS: {tag_of(DGS)} full-menu replay (D60's C1 grade, "
      f"all 9 actors offered at every step) = {_dgrep['status']} at step "
      f"{_dgrep['step']}/{len(BUILT[DGS][0].H)}, max hits per "
      f"specification = {_dgrep['hits']}, widest full menu = "
      f"{_dgrep['menu']} candidates — so the counterexample carries the "
      f"SAME forcedness grade as this unit's own records, and a HIGHER "
      f"one than {tag_of(WIDE)}, whose replay is budget-cut at "
      f"{REPLAY[tag_of(WIDE)]['step']}/{len(BUILT[WIDE][0].H)}.")
check("A3b(a) [BLOCKER 1 — THE WIDTH LAW WAS WRONG AND THIS IS THE "
      "OBJECT THAT BREAKS IT] `max |D| = 2k` IS NOT A LAW ABOUT "
      "k-PROPOSER CRYSTALS; W4c's OWN CEILING k^2 IS REALIZED AND "
      "SATURATED.  DOUBLE-GRID(3, R) is a forced, menu-offered, "
      "C1-graded conflict crystal in which rows and columns conflict "
      "CONCURRENTLY: every actor holds two live proposals on two "
      "distinct unsuperseded bases, so the record has ZERO in-round "
      "deliveries, the arbitration share SATURATES 1/(k+1) = 1/4, and "
      "the depth-1 successor of a row arbitration on each proposer "
      "register is a COLUMN ARBITRATION rather than a delivery.  Nine "
      "charts of width 9 = k^2 result, three per round, each verified "
      "against the committed sky and the committed order.  `2k` is the "
      "special case Bl = 2, i.e. the case the RING and GRID blueprints "
      "impose by making every successor of an arbitration a delivery",
      (not _dg.refusal and _dg.maxhits == 1 and _dgpr[2]['max'] == 9
       and _dgBl == 3 and _dgk == 3 and _nine_ok and len(NINE) == 9
       and _dgref_ok and _dg_w4c and len(_inround) == 0
       and arbshare(_dg.H) == Fr(1, 4)
       and _dgrep['status'] == 'OK' and _dgrep['hits'] == 1
       and sum(1 for c in _dgocc.values() if c > 1) == 0),
      f"n = {len(_dg.H)}, refusals = 0, max hits = {_dg.maxhits}; arb "
      f"share {arbshare(_dg.H)} = bound {Fr(1, _dgk + 1)}; in-round "
      f"deliveries = {len(_inround)} of {len(_dels)}; max |D| = "
      f"{_dgpr[2]['max']} = Bl^2 = k^2 = {_dgBl ** 2}; charts of width 9 "
      f"= {len(NINE)}, all verified = {_nine_ok}; refined bound "
      f"violations = 0; version registers occurring twice = "
      f"{sum(1 for c in _dgocc.values() if c > 1)}; C1 full-menu replay "
      f"of {tag_of(DGS)} = {_dgrep['status']} {_dgrep['step']}/"
      f"{len(BUILT[DGS][0].H)}, widest menu {_dgrep['menu']}")
check("A3b(b) [MAJOR 1 — THE DESIGN FINDING IS INVERTED] THE DELIVERY IS "
      "NOT WHAT GIVES THE CRYSTAL ITS SECOND DIRECTION, AND THE "
      "MAXIMUM-CONFLICT SCHEDULE IS NOT THE ONE THAT CANNOT TILE WIDELY. "
      "The earlier finding rested on ONE schedule — the delivery-free "
      "pair ring at sticky = 0, in which each actor has exactly ONE "
      "conflict lineage, so its propose/arbitrate cycle is a chain of "
      "DIAMONDS and the depth-2 layer is a single event.  That is a "
      "property of one live conflict per actor, not of "
      "delivery-freedom.  The DELIVERY-FREE DOUBLE-GRID gives each actor "
      "TWO standing conflicts, has zero in-round deliveries, SATURATES "
      "the arbitration share, and is the WIDEST record in the unit.  The "
      "corrected statement: what a second direction needs is a SECOND "
      "CONCURRENT CONSUMER of the proposer's register — rotation buys "
      "one with a delivery, concurrency buys one for free, and a "
      "concurrent arbitration is the better of the two",
      (len(_inround) == 0 and arbshare(_dg.H) == Fr(1, 4)
       and _dgpr[2]['max'] > BUILT[('RING', 6, 10, 0, 'S')][1][2]['max']
       and _dgpr[2]['max'] == max(_maxw.values())),
      f"delivery-free ring (sticky=0): arb share "
      f"{arbshare(BUILT[('RING', 6, 10, 0, 'S')][0].H)}, max |D| = "
      f"{BUILT[('RING', 6, 10, 0, 'S')][1][2]['max']}, one conflict "
      f"lineage per actor; delivery-free DOUBLE-GRID: arb share "
      f"{arbshare(_dg.H)} (SATURATED), in-round deliveries "
      f"{len(_inround)}, max |D| = {_dgpr[2]['max']} = the widest in the "
      f"sweep ({max(_maxw.values())})")
check("A3b(c) [MAJOR 2 — RESIDUE 2 IS ANSWERED, NOT OPEN] A k >= 3 "
      "CONFLICT SCHEDULE EXISTS THAT IS INSIDE THE HOMOGENEITY BAND AND "
      "PAST THE CEILING AT ONCE.  The anti-correlation sentence ('no "
      "swept configuration is both inside the band and past the "
      "ceiling') was a d = 2 statement shipped without its depth label. "
      "At d = 3 the DOUBLE-GRID's homogeneity is INSIDE the recomputed "
      "d = 3 sprinkling band while it carries max |D| = 9 — in-band and "
      "nine directions wide, simultaneously — and A2(c) shows the "
      "unit's own k = 3 grids move into the d = 3 band under its own "
      "interior control.  The anti-correlation is therefore restated as "
      "a d = 2 property of this family, and D66's residue 2 is CLOSED by "
      "the round's own construction",
      (BAND[3][0] <= _dgpr[3]['h2'] <= BAND[3][1]
       and _dgpr[3]['max'] >= 5 and _dgpr[2]['max'] >= 5),
      f"DOUBLE-GRID d = 3 homogeneity {_dgpr[3]['h2']} "
      f"(~{float(_dgpr[3]['h2']):.4f}) in band "
      f"[{BAND[3][0]}, {BAND[3][1]}] = "
      f"{BAND[3][0] <= _dgpr[3]['h2'] <= BAND[3][1]}, |D|>=4 at "
      f"{_dgpr[3]['h4']} (~{float(_dgpr[3]['h4']):.4f}), max |D| = "
      f"{_dgpr[3]['max']}; d = 2 homogeneity "
      f"{float(_dgpr[2]['h2']):.4f} [{_pos(_dgpr[2]['h2'], 2)}]")

print("\n  [A3b(d) THE SMALLEST WITNESSES — ARBCHAIN(m, k = 3): the "
      "whole interval [2k, k^2] is realized as m, the number of the "
      "arbitration's proposer registers consumed by a FURTHER "
      "arbitration rather than by a delivery, runs 0..k]")
_ac_rows = []
_ac_ok = True
for m in (0, 1, 2, 3):
    bb, ee = arbchain(m, 3)
    if bb.refusal or bb.maxhits != 1:
        _ac_ok = False
        _ac_rows.append((m, None))
        continue
    Cc = poset_of(bb.H)
    hh = heights(Cc)
    sc = defaultdict(set)
    lst = {}
    for j, op in enumerate(bb.H):
        for r in regs_of(op):
            if r in lst:
                sc[lst[r]].add(j)
        for r in regs_of(op):
            lst[r] = j
    D2 = sky(Cc, ee, 'B', 2)[0]
    pred_val = 3 * m + 2 * (3 - m)
    if len(D2) != pred_val:
        _ac_ok = False
    _ac_rows.append((m, (len(bb.H), len(bb.actors), ee, hh[ee],
                         sorted(sc[ee]), [bb.H[f][0] for f in sorted(sc[ee])],
                         [len(sc[f]) for f in sorted(sc[ee])], len(D2),
                         pred_val, max(len(v) for v in sc.values()))))
for (m, r) in _ac_rows:
    if r is None:
        print(f"      m={m}: REFUSAL")
        continue
    print(f"      ARBCHAIN(m={m}, k=3): n={r[0]:3d} actors={r[1]:2d}, THE "
          f"arbitration at index {r[2]} (height {r[3]}, 4 registers, 3 "
          f"proposers, live out-degree {len(r[4])}); D(1)={r[4]} kinds "
          f"{r[5]} out-degrees {r[6]}; |D_e(2)| = {r[7]} "
          f"(= k*m + 2*(k-m) = {r[8]}), Bl = {r[9]}, W4c bound "
          f"{r[9] ** 2}")
print(f"      m = 0 IS the RING/GRID case and gives 2k = 6; m = 1 gives "
      f"7 > 2k with successor kinds ['r','d','d'] and out-degrees "
      f"[3,2,2]; m = 3 gives 9 = k^2, W4c's bound, SATURATED.  These "
      f"reproduce the STRUCTURE and the VALUES of the review's two small "
      f"witnesses (its |D| = 7 record: successors r/d/d at out-degrees "
      f"3/2/2; its |D| = 9 record: three arbitration successors) with "
      f"this unit's own blueprint; they are not the review's exact "
      f"scripts and their event counts differ (the review's were 26 "
      f"events / 17 actors and 44 / 24).")
check("A3b(d) THE REFINED BOUND IS EXACTLY RIGHT AND THE WHOLE INTERVAL "
      "[2k, k^2] IS OCCUPIED.  |D_e(2)| = k*m + 2*(k - m) at every m, "
      "with every event menu-offered and matching exactly one candidate: "
      "6, 7, 8, 9 at m = 0, 1, 2, 3 for k = 3.  So `2k` is not a law, "
      "not a ceiling and not even a typical value — it is the m = 0 "
      "corner of a one-parameter family, and W4c's k^2 is the corner at "
      "the other end",
      _ac_ok and all(r is not None for _, r in _ac_rows),
      "; ".join(f"m={m}: |D|={r[7]} = predicted {r[8]}"
                for m, r in _ac_rows if r) )

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


# ROUND-1 MAJOR 5 added the five-ring-size ladder (M = 4, 6, 8, 10, 12 at
# R = 6, plus M = 10 at R = 10 beside M = 6 at R = 10) so the parity
# reading and the "count = R - 1" reading are both DECIDED, not filed;
# round-1 MINOR 1 added GRID(3,4), the one complete WIDE record that is
# full-menu replayed end to end.
A4SET = [x for x in (HEAD, ('RING', 4, 6, 1, 'S'), ('RING', 4, 10, 1, 'S'),
                     ('RING', 6, 6, 1, 'S'), ('RING', 8, 6, 1, 'S'),
                     ('RING', 8, 10, 1, 'S'), ('RING', 10, 6, 1, 'S'),
                     ('RING', 10, 10, 1, 'S'), ('RING', 12, 6, 1, 'S'),
                     ('RING', 6, 10, 1, 'R'), ('RING', 6, 10, 0, 'S'),
                     ('GRID', 3, 4), ('GRID', 3, 6), WIDE,
                     ('GRID', 4, 4)) if x in BUILT]
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


def _c7_edges(r):
    """C7's OWN cochain domain: length-preserving pairs that are NOT the
    'other' class (D64's `cochain` drops 'other' by construction).
    Returns (edges, non-identity edges)."""
    g = {}
    for (a, c) in sorted(r['pairmap'], key=repr):
        if a > c:
            continue
        cls = classify(r['pairmap'][(a, c)])
        if cls in ('length-changing', 'other'):
            continue
        g[(a, c)] = 0 if is_named(cls, 'identity') else 1
    return len(g), sum(g.values())


print(f"\n      WHERE THE NON-VACUITY ACTUALLY LIVES (round-1 MAJOR 4 — "
      f"the earlier claim credited the WRONG COLUMN).  Per convention at "
      f"d = 2, C7's own cochain domain (it DROPS the 'other' class by "
      f"construction) beside PARITY's (which never drops anything):")
_wide_acct = {}
for tg in INST:
    rr = MEAS[(_wide_nm, tg, 2)]
    ce, cn = _c7_edges(rr)
    pa = PAR[(_wide_nm, tg, 2)]
    _wide_acct[tg] = (ce, cn, pa['edges'], pa['nonid'],
                      CO[(_wide_nm, tg, 2)]['cech_t'])
    print(f"        {tg:9s} kinds {rr['kinds']}: C7 cochain on {ce:3d} "
          f"edges of which NON-IDENTITY {cn:3d} -> obstruction "
          f"{CO[(_wide_nm, tg, 2)]['incons']}; PARITY cochain on "
          f"{pa['edges']:3d} edges of which NON-IDENTITY {pa['nonid']:3d} "
          f"-> obstruction {pa['obstructions']}; Cech triples "
          f"{CO[(_wide_nm, tg, 2)]['cech_t']}")
_c7_live = sorted(tg for tg in INST if _wide_acct[tg][1] > 0)
_par_live = sorted(tg for tg in INST if _wide_acct[tg][3] > 0)
_full_dom = sorted(tg for tg in INST
                   if _wide_acct[tg][0] == _wide_acct[tg][2])
_cut_dom = sorted(tg for tg in INST
                  if _wide_acct[tg][0] < _wide_acct[tg][2])
print(f"        READ IT HONESTLY.  C7's cochain is the ZERO COCHAIN at "
      f"ALL FIVE conventions, but for TWO DIFFERENT REASONS.  At "
      f"{_full_dom} it is zero on the FULL length-preserving domain "
      f"(every such transition is outright the identity): there is "
      f"nothing to trivialize and the Cech triples test 0 = 0 + 0, so "
      f"the triple COUNT is not evidence of non-vacuity there (D64's "
      f"round-1 MINOR 1 struck out exactly that move) — what IS "
      f"non-vacuous at those cells is that PROBE 1 does not fire, i.e. "
      f"the labeling COULD have shown a transition and did not.  At "
      f"{_cut_dom} the cochain is zero only because C7 DROPS the 'other' "
      f"class by construction: its domain shrinks from "
      f"{_wide_acct['ARBLOSE'][2]} edges to {_wide_acct['ARBLOSE'][0]}, "
      f"discarding the "
      f"{MEAS[(_wide_nm, 'ARBLOSE', 2)]['kinds'].get('other', 0)} "
      f"non-identity maps the sentence invokes.  The only routes on this "
      f"record that trivialize a cochain that is NOT identically zero "
      f"are PARITY (at {_par_live}) and FREE.  The strongest line about "
      f"this record is therefore PARITY's and FREE's, not C7's.")
check("A4(e0) [MAJOR 4 — THE NON-VACUITY CLAIM IS RE-ATTRIBUTED TO THE "
      "COLUMN THAT CARRIES IT] The wide record's transition class is "
      "trivial by all three routes at all five conventions, and the "
      "ACCOUNTING for why that is not vacuous is now printed cell by "
      "cell.  C7's Z/2 cochain is IDENTICALLY ZERO at every convention: "
      "at four of them on the full length-preserving domain (so the Cech "
      "triples are a dead test and PROBE 1's silence is the content), "
      "and at ARBLOSE only because C7 drops the 'other' class, shrinking "
      "its domain and discarding exactly the non-identity maps the old "
      "sentence invoked.  The route that genuinely trivializes a "
      "NON-trivial cochain on this record is PARITY — and, "
      "independently, the free-relabelling route.  The A-IIIa verdict is "
      "unaffected; the credit is corrected",
      (len(_c7_live) == 0 and len(_full_dom) == 4 and len(_cut_dom) == 1
       and _par_live == _cut_dom and _wide_triv),
      f"conventions at which C7's cochain has a non-identity edge = "
      f"{_c7_live}; C7 domain = PARITY domain at {_full_dom}; C7 domain "
      f"SHRUNK at {_cut_dom} "
      f"({_wide_acct['ARBLOSE'][0]} of {_wide_acct['ARBLOSE'][2]} edges "
      f"kept); conventions at which PARITY's cochain has non-identity "
      f"edges = { {tg: _wide_acct[tg][3] for tg in _par_live} }; wide "
      f"record trivial by every route at every convention = {_wide_triv}")

print(f"\n      HOW MANY DISTINCT READINGS THE FIVE CONVENTIONS ACTUALLY "
      f"GIVE (round-1 MINOR 6).  The conventions ARE genuinely distinct "
      f"labelings — the (chart, direction) cells at which each disagrees "
      f"with REG on the ROLE label are counted below — but on the wide "
      f"record every census COLUMN is identical at four of them, so the "
      f"robustness sentence is that the wide record admits TWO distinct "
      f"readings, not five:")
_ref_lab = MEAS[(_wide_nm, 'REG', 2)]['Wd']
_cells = [(e, f) for e in _ref_lab for f in _ref_lab[e]]
_conv_diff = {}
for tg in INST:
    Wd = MEAS[(_wide_nm, tg, 2)]['Wd']
    _conv_diff[tg] = sum(
        1 for (e, f) in _cells
        if label(Wd.get(e, {}).get(f, frozenset()), 'ROLE')
        != label(_ref_lab[e][f], 'ROLE'))
print(f"        (chart, direction) cells = {len(_cells)}; cells whose "
      f"ROLE label differs from REG's: {_conv_diff}")
_col = {tg: (MEAS[(_wide_nm, tg, 2)]['kinds'],
             CO[(_wide_nm, tg, 2)]['incons'],
             PAR[(_wide_nm, tg, 2)]['obstructions'],
             UFR[(_wide_nm, tg, 2)]['obstructions'],
             CO[(_wide_nm, tg, 2)]['cech_t']) for tg in INST}
_distinct_readings = len({repr(v) for v in _col.values()})
print(f"        distinct census ROWS over the five conventions at d = 2 "
      f"= {_distinct_readings} (four identical + ARBLOSE).")

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
      f"holonomy around an odd conflict ring is the natural reading.")

# ---- MAJOR 5: the residue's own experiment, run rather than filed -------
print(f"\n      [MAJOR 5 — THE RESIDUE'S OWN EXPERIMENT, RUN.  The first "
      f"version filed 'it needs M = 10, 12, 14 and a proof, not three "
      f"sizes' as an open residue; the experiment costs seconds and the "
      f"receipt now runs it.  REG, d = 2, one row per ring:]")
_ladder = [('RING', M, R, 1, 'S') for (M, R) in
           ((4, 6), (6, 6), (8, 6), (10, 6), (12, 6), (6, 10), (10, 10))]
_lad_rows = []
for kk in _ladder:
    nm = tag_of(kk)
    if (nm, 'REG', 2) not in CO:
        continue
    rr = MEAS[(nm, 'REG', 2)]
    ce, cn = _c7_edges(rr)
    pa = PAR[(nm, 'REG', 2)]
    _lad_rows.append((kk[1], kk[2], kk[1] // 2, pa['edges'], pa['nonid'],
                      CO[(nm, 'REG', 2)]['incons'], pa['obstructions']))
for (M, R, ppr, ed, ni, c7, po) in _lad_rows:
    print(f"        RING(M={M:2d}, R={R:2d})  {ppr} pairs/round  M/2 "
          f"{'ODD ' if ppr % 2 else 'EVEN'}  parity edges {ed:3d}  "
          f"non-identity {ni:3d}  C7 obstructions {c7:2d}  PARITY "
          f"obstructions {po:2d}   (R - 1 = {R - 1})")
_odd = [r for r in _lad_rows if r[2] % 2 == 1]
_even = [r for r in _lad_rows if r[2] % 2 == 0]
_parity_reading = (all(r[6] > 0 for r in _odd) and all(r[6] == 0
                                                       for r in _even))
_isRm1 = all(r[6] == r[1] - 1 for r in _odd)
print(f"        THE PARITY READING SURVIVES AT FIVE RING SIZES, NOT "
      f"THREE: odd M/2 (M = "
      f"{sorted({r[0] for r in _odd})}) obstructs, even M/2 (M = "
      f"{sorted({r[0] for r in _even})}) is clean, and the M = 12 clean "
      f"row is the one that could have killed it.")
print(f"        AND THE MAGNITUDES ARE NOT A RING QUANTITY (round-1 "
      f"MAJOR 5, second half).  The obstruction count is the SAME for "
      f"M = 6 and M = 10 at each R and equals R - 1 at every obstructing "
      f"ring: {[(f'M={r[0]},R={r[1]}', r[6], r[1] - 1) for r in _odd]}.  "
      f"It counts ROUNDS, not the ring; presenting '5 (R = 6) and 9 "
      f"(R = 10)' as the RING's obstruction invites reading a magnitude "
      f"that is neither a ring quantity nor a cohomological one.  The "
      f"only invariant statement available is != 0.")
print(f"        THE ONE ROW THAT DOES NOT MATCH THE REVIEW'S OWN TABLE: "
      f"the review reports RING(4, 6) at 'edges 23, non-id 3'; this "
      f"unit's instrument measures "
      f"{[(r[3], r[4]) for r in _lad_rows if r[0] == 4 and r[1] == 6]} "
      f"there.  The OBSTRUCTION count agrees (0 both ways) and every "
      f"other row of the review's table reproduces to the digit; the "
      f"M = 4 edge/non-identity discrepancy is disclosed rather than "
      f"smoothed, and it does not touch the parity reading.")
check("A4(e1) [MAJOR 5 — THE ODD-RING RESIDUE IS DECIDED AT FIVE SIZES, "
      "AND THE MAGNITUDE IS RE-READ] THE OBSTRUCTION IS EXACTLY THE "
      "PARITY OF M/2 ACROSS THE MEASURED LADDER, AND ITS COUNT IS R - 1, "
      "NOT A RING QUANTITY.  Rings with an ODD number of pairs per round "
      "(M = 6, 10) obstruct at every R measured; rings with an EVEN "
      "number (M = 4, 8, 12) are clean, and M = 12 is the row that could "
      "have falsified the reading.  The obstruction COUNT is identical "
      "for M = 6 and M = 10 at each R and equals R - 1 at each of them, "
      "so it counts rounds and not the ring.  The residue's remaining "
      "content is the PROOF, not more sizes",
      _parity_reading and _isRm1 and len(_lad_rows) == len(_ladder),
      f"ring sizes measured = {sorted({r[0] for r in _lad_rows})} at R in "
      f"{sorted({r[1] for r in _lad_rows})}; odd-M/2 rows all obstruct "
      f"and even-M/2 rows are all clean = {_parity_reading}; every "
      f"obstructing count equals R - 1 = {_isRm1}")
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
print(f"    THE SCOPE OF THAT COMPARISON (round-1 MINOR 8): a sprinkling "
      f"has no H, so only the register-free COV instrument is defined on "
      f"it — the ring's other four conventions have NO sprinkling "
      f"counterpart.  The comparison is therefore made AT COV and "
      f"nowhere else: sprinklings "
      f"{ {k[0] + '/d' + str(k[2]): v for k, v in sorted(_spr_par.items(), key=repr) if k[1] == 'COV'} }"
      f" vs the delivery crystal at COV "
      f"{ {k[0] + '/d' + str(k[2]): v for k, v in sorted(_dr_par.items(), key=repr) if k[1] == 'COV'} }"
      f" vs {tag_of(HEAD)} at COV "
      f"{ {'d' + str(d): PAR[(tag_of(HEAD), 'COV', d)]['obstructions'] for d in DEPTHS} }.")
check("A4(e) [THE CLASS DECIDES] THE WIDE RECORD'S CLASS IS TRIVIAL — "
      "**A-IIIa, not A-IIIb** — AND THE PAIR-CONFLICT RING CARRIES THE "
      "CAMPAIGN'S FIRST NON-ZERO OBSTRUCTION COUNT, WHICH IS REPORTED "
      "AND NOT CLAIMED AS H^1 != 0.  On the wide record all three "
      "routes return ZERO obstructions at every one of the five port "
      "conventions and at both depths — with the non-vacuity accounted "
      "for in A4(e0) rather than asserted: at REG, REGA, ARBVFIRST and "
      "COV the Z/2 cochain is IDENTICALLY ZERO, so the content there is "
      "that PROBE 1 does not fire (the labeling could have shown a "
      "transition and did not) and NOT the Cech triple count, and at "
      "ARBLOSE the 'other' maps that C7 drops are trivialized by the "
      "PARITY and FREE routes instead.  Conflict bought WIDTH and bought "
      "no gauge.  "
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
              "d = 2 while the DELIVERY-FREE DOUBLE-GRID carries |D| = 9 "
              "= k^2, W4c's own ceiling, SATURATED — the first records "
              "in the campaign past the delivery ceiling of 4.  On the "
              "wide record the transition class is "
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
      f"configurations, 2 sprinklings charted; ROUND-1 ADDITIONS = "
      f"DOUBLE-GRID(3,2) and (3,4), ARBCHAIN(m = 0..3, k = 3), and the "
      f"ring ladder M = 8, 10, 12 at R = 6 plus M = 10 at R = 10.")
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
      "share and full width histogram — byte-identical stdout.  THE "
      "DOUBLE-GRID IS IN THE DIGEST, so the round-1 counterexample's "
      "|D| = 9 histogram is covered.  IT DOES NOT COVER the sweep's "
      "larger records or the A4 census",
      len(set(_digs)) == 1 and 'DIGEST' in _digs[0]
      and "('GRID', 3, 4)" in _digs[0] and "('DGRID', 3, 2)" in _digs[0],
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
      f"{BUILT[WIDE][1][2]['max']} at d = 2, "
      f"{tag_of(('GRID', 4, 4))}: max |D| = "
      f"{BUILT[('GRID', 4, 4)][1][2]['max']}, and "
      f"{tag_of(DGW)}: max |D| = {BUILT[DGW][1][2]['max']} — past the "
      f"delivery grammar's d = 2 ceiling of 4 for the first time.")
print(f"    THE MECHANISM, AND IT CORRECTS ITS OWN PARENT (W4c): the "
      f"version register an")
print(f"    arbitration mints is a BIRTH WIRE with no successor — proved "
      f"in A2(b0) from")
print(f"    the committed layer, not measured — so three registers are "
      f"worth two, a")
print(f"    two-proposer conflict ring is held to the delivery ceiling 4 "
      f"at d = 2, and")
print(f"    width past 4 needs 3+ PROPOSERS.")
print(f"    THE WIDTH LAW (round-1 BLOCKER 1, CORRECTED).  max |D| = 2k "
      f"is NOT a law")
print(f"    about k-proposer crystals: it is what the RING and GRID "
      f"schedules realize,")
print(f"    because in them every depth-1 successor of an arbitration is "
      f"a delivery")
print(f"    (Bl = 2).  The true ceiling is the refinement |D_e(2)| <= "
      f"SUM_y b(y) <=")
print(f"    k * Bl <= k^2, gated at every event of every record here, "
      f"and it is")
print(f"    REALIZED AND SATURATED at k^2 = 9 by the delivery-free "
      f"DOUBLE-GRID(3, R)")
print(f"    (nine charts of width 9, three per round), with "
      f"ARBCHAIN(m, 3) occupying")
print(f"    the whole interval 6, 7, 8, 9.  The genuine headline is "
      f"therefore: W4c's")
print(f"    bound is TIGHT, and the widest chart in the campaign is 9.")
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
