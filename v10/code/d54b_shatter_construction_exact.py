#!/usr/bin/env python3
"""
d54b_shatter_construction_exact.py — v10 D54 Stage 2: the targeted
shatter construction.  Pin: note-d54-dilworth-gate-pin.md §4 (STRICT,
LOG #427, committed before this file existed).

THE BLUEPRINT (pin §4): 9 actors — X mints v1 at base event E; X
delivers v1 to A,B,C,D; each direction-actor pads and proposes on v1 so
all four proposals land at the SAME height (pairwise incomparable by
proposal locality) — the four directions of SKY-B(5) at E; then
accumulators F,G,H,I plus two late cross-deliveries realize the B4
symmetric chain decomposition WORN AS WORLDLINES.

**ADMISSIBILITY IS DECIDED ONLY BY THE COMMITTED LAYER**: every event
is SELECTED from d42b1's own candidates_for menu by specification —
nothing is constructed freehand.  A refusal prints the prefix, the
specification and the menu, and the blocking clause is the deliverable
(exit 0).  Exit 1 only on anchor breakage.

Run from the repo root: python3 v10/code/d54b_shatter_construction_exact.py
"""
import ast
import sys
from collections import defaultdict
from fractions import Fraction as Fr
from itertools import combinations, permutations, product

sys.setrecursionlimit(300000)

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

print("[D54b — the targeted shatter construction]")
print("  banner: the builder SELECTS every event from the committed")
print("  d42b1 menu; a refusal is an exit-0 deliverable naming the")
print("  blocking step.  Capacity gate = D53 SC5, never D47 SG2.")
print("  Sky = SKY-B only (D53); the depth used is REPORTED and the")
print("  claim is reading-relative to it.")

# ---------------------------------------------------------------- anchors
_SRCT = 'v10/code/d42b1_transport_exact.py'
_st = open(_SRCT).read()
nst = {}
exec(compile(_st[:_st.index('print("[d42b1')], 'd42b1_ported', 'exec'), nst)
candidates_for = nst['candidates_for']
event_poset = nst['event_poset']
V0 = nst['V0']

_D47A = 'v10/code/d47a_sky_instrument_exact.py'
_ta = ast.parse(open(_D47A).read())
_keep = [n for n in _ta.body
         if isinstance(n, ast.FunctionDef)
         or (isinstance(n, ast.Assign)
             and any(isinstance(x, ast.Name)
                     and x.id in ('CYCLIC_CAP', 'SKYB_DEPTH')
                     for x in n.targets))]
g47 = {'Fr': Fr, 'combinations': combinations,
       'permutations': permutations, 'product': product}
exec(compile(ast.fix_missing_locations(ast.Module(body=_keep,
                                                  type_ignores=[])),
             'd47a_extract', 'exec'), g47)
sky = g47['sky']
shattered_set = g47['shattered_set']

check("K0 anchors: transport layer from committed d42b1, sky/shatter "
      "from committed D47a (AST extraction)",
      callable(candidates_for) and callable(sky), "single sources")

ACTORS = ('X', 'A', 'B', 'C', 'D', 'F', 'G', 'H', 'I')
H = []                     # the history under construction
REFUSAL = None


def poset_of(h):
    pred = event_poset(list(h))
    n = len(h)
    return [[i in pred[j] for j in range(n)] for i in range(n)]


def heights(C):
    n = len(C)
    hh = [0] * n
    for x in sorted(range(n), key=lambda x: sum(C[i][x] for i in range(n))):
        p = [i for i in range(n) if C[i][x]]
        hh[x] = 1 + max((hh[i] for i in p), default=-1)
    return hh


def pick(spec, label):
    """Select the unique menu event matching `spec`; append it.  On
    refusal, record and print the deliverable."""
    global REFUSAL
    if REFUSAL:
        return None
    menu = candidates_for(list(H), ACTORS)
    hits = sorted((e for e, q in menu if spec(e)), key=repr)
    if not hits:
        REFUSAL = (label, len(H))
        print(f"  [REFUSAL] step '{label}' at prefix length {len(H)}: no "
              f"menu event matches.  Menu size = {len(menu)}; menu event "
              f"types = {sorted({e[0] for e, q in menu})}")
        for e, q in sorted(menu, key=lambda x: repr(x[0]))[:20]:
            print(f"      offered: {e}  q={q}")
        return None
    e = hits[0]
    H.append(e)
    return e


# ---------------------------------------------------------------- build
print("\n[the build — every event selected from the layer's own menu]")
pick(lambda e: e[0] == 'p' and e[1] == 'X' and e[2] == V0 and e[3] == 0,
     "X proposes on v0")
E_IDX = len(H)
pick(lambda e: e[0] == 'r' and e[1] == 'X', "X arbitrates -> base event E")

# the minted version: read it from the delivery menu, not reconstructed
V1 = None
if not REFUSAL:
    menu = candidates_for(list(H), ACTORS)
    dv = sorted({e[3] for e, q in menu if e[0] == 'd' and e[3] != V0},
                key=repr)
    V1 = dv[0] if dv else None
check("K1 the opening is admissible and mints a fresh version: X's "
      "proposal and arbitration selected from the menu, and the layer "
      "now OFFERS deliveries of a non-genesis version — v1 read from the "
      "menu, never reconstructed",
      REFUSAL is None and V1 is not None,
      f"E at index {E_IDX}; v1 = {V1}")

for r in ('A', 'B', 'C', 'D'):
    pick(lambda e, r=r: e[0] == 'd' and e[1] == 'X' and e[2] == r
         and e[3] == V1, f"X delivers v1 to {r}")

# pads: each direction-actor idles until its proposal would land at the
# common height TARGET = h(E) + 5, computed from the actual poset
DIR_IDX = {}
if not REFUSAL:
    C = poset_of(H)
    hh = heights(C)
    TARGET = hh[E_IDX] + 5
    for r in ('A', 'B', 'C', 'D'):
        while not REFUSAL:
            C = poset_of(H)
            hh = heights(C)
            last = max(i for i in range(len(H))
                       if r in (H[i][1], H[i][2] if H[i][0] == 'd' else H[i][1]))
            if hh[last] + 1 == TARGET:
                break
            pick(lambda e, r=r: e[0] == 'n' and e[1] == r, f"{r} pads")
        e = pick(lambda e, r=r: e[0] == 'p' and e[1] == r and e[2] == V1
                 and e[3] == 0, f"{r} proposes on v1 (direction)")
        if e is not None:
            DIR_IDX[r] = len(H) - 1

check("K2 the four directions are built: each direction-actor padded to "
      "the common height and proposed on v1 — four events, pairwise "
      "incomparability and equal height verified below on the finished "
      "poset",
      REFUSAL is None and len(DIR_IDX) == 4,
      f"direction indices = {DIR_IDX}")

# accumulators: the SCD chains as worldlines (order is load-bearing)
CHAINS = [('F', ['A', 'B', 'C', 'D']),
          ('G', ['B', 'C', 'D']),
          ('H', ['A', 'C', 'D']),
          ('I', ['B', 'D', 'A'])]
for who, srcs in CHAINS:
    for s in srcs:
        pick(lambda e, s=s, who=who: e[0] == 'd' and e[1] == s
             and e[2] == who and e[3] == V1, f"{who} receives from {s}")
# the two late cross-deliveries (after ALL accumulator receipts)
pick(lambda e: e[0] == 'd' and e[1] == 'D' and e[2] == 'A' and e[3] == V1,
     "A receives from D  (trace {A,D})")
pick(lambda e: e[0] == 'd' and e[1] == 'D' and e[2] == 'C' and e[3] == V1,
     "C receives from D  (trace {C,D})")

check("K3 THE BLUEPRINT IS ADMISSIBLE END TO END: all "
      f"{len(H)} events were offered by the committed layer's own menu "
      "at their prefixes — the layer, not the author, decided",
      REFUSAL is None,
      f"events = {len(H)}, refusal = {REFUSAL}")

if REFUSAL is None:
    # ---------------------------------------------------------- verdicts
    C = poset_of(H)
    hh = heights(C)
    n = len(H)
    dirs_idx = sorted(DIR_IDX.values())
    inc_ok = all(not (C[i][j] or C[j][i])
                 for i, j in combinations(dirs_idx, 2))
    same_h = len({hh[i] for i in dirs_idx}) == 1
    above_e = all(C[E_IDX][i] for i in dirs_idx)
    DEPTH = hh[dirs_idx[0]] - hh[E_IDX]
    check("K4 the directions are a genuine sky: pairwise INCOMPARABLE "
          "(proposal locality did its job), all at ONE height, all "
          "strictly above E — and the height offset is REPORTED, since "
          "the claim is reading-relative to SKY-B at that depth",
          inc_ok and same_h and above_e,
          f"pairwise incomparable = {inc_ok}, common height = {same_h} "
          f"(h = {hh[dirs_idx[0]]}), above E = {above_e}, DEPTH = {DEPTH}")

    dirs, rows = sky(C, E_IDX, 'B', DEPTH)
    r = set(rows)
    check("K5 SKY-B AT E REPRODUCES THE INTENDED DIRECTIONS from the "
          "committed instrument itself — the four proposals and nothing "
          "else at that offset",
          sorted(dirs) == dirs_idx,
          f"instrument dirs = {sorted(dirs)}, blueprint dirs = {dirs_idx}")

    cap5 = len(dirs) >= 4 and len(r) >= 16 and frozenset() in r
    check("K6 CAPACITY BY THE CORRECTED CONDITION (D53 SC5, never D47 "
          "SG2): >= 4 directions, >= 16 DISTINCT traces, empty trace "
          "present",
          cap5,
          f"|dirs| = {len(dirs)}, distinct traces = {len(r)}, empty "
          f"present = {frozenset() in r}")

    idx_of = {v: k for k, v in DIR_IDX.items()}
    traces_named = sorted({tuple(sorted(idx_of[i] for i in t)) for t in r})
    need = {tuple(sorted(s)) for k in range(5)
            for s in combinations('ABCD', k)}
    have = {tuple(sorted(idx_of[i] for i in t)) for t in r}
    wit = shattered_set(rows, dirs, 4)
    check("K7 **ALL 16 SUBSETS OF THE 4 DIRECTIONS ARE REALIZED AS "
          "TRACES, AND THE INSTRUMENT RETURNS A SHATTERED 4-SET.**  "
          "Under the committed SKY-B reading at the reported depth, this "
          "record's sky is NOT realizable as a 2+1 celestial sky — arcs "
          "on a circle cannot shatter 4 (D47a SG0, constructed)",
          need <= have and wit is not None,
          f"subsets realized = {len(have & need)}/16; shattered 4-set = "
          f"{wit}; traces = {traces_named}")

    if wit is not None:
        print(f"  [WITNESS TRANSPORT-SHATTER-4] the pre-registered "
              f"witness branch, taken by a REAL record this time: "
              f"shattered set = {sorted(idx_of[i] for i in wit)}, "
              f"actors = {len(ACTORS)}, events = {n}, depth = {DEPTH}")

    # consistency with the theorem
    byact = defaultdict(set)
    for f in range(n):
        if C[E_IDX][f]:
            byact[H[f][1]].add(
                frozenset(c for c in dirs if c == f or C[c][f]))
    nested = all(a <= b or b <= a
                 for trs in byact.values()
                 for a, b in combinations(trs, 2))
    contributing = sum(1 for trs in byact.values() if trs)
    check("K8 CONSISTENCY WITH THE DILWORTH GATE: the record's traces "
          "decompose into per-initiator CHAINS (zero crossings), and at "
          "least 6 actors contribute — the construction does not beat "
          "the theorem, it SATURATES it",
          nested and contributing >= 6,
          f"per-actor chains nested = {nested}, contributing actors = "
          f"{contributing} (bound: 6), total actors = {len(ACTORS)}")

    for kind in ('A', 'C'):
        dA, rA = sky(C, E_IDX, kind)
        check(f"K9-{kind} D53 CONTROL: SKY-{kind} on this same record "
              "has NO empty trace, so it could never have shattered — "
              "the definition-level disqualification reproduced on the "
              "constructed object",
              frozenset() not in set(rA),
              f"|dirs| = {len(dA)}, empty trace present = "
              f"{frozenset() in set(rA)}")

# hygiene
_self = ast.parse(open('v10/code/d54b_shatter_construction_exact.py').read())
_bound = set()
for _n in ast.walk(_self):
    if isinstance(_n, ast.Name) and isinstance(_n.ctx, ast.Store):
        _bound.add(_n.id)
    elif isinstance(_n, ast.FunctionDef):
        _bound.add(_n.name)
        for _a in _n.args.args:
            _bound.add(_a.arg)
_ch = [c for c in ast.walk(_self) if isinstance(c, ast.Call)
       and isinstance(c.func, ast.Name) and c.func.id == 'check']
_vac = [c for c in _ch if isinstance(c.args[1], ast.Constant)
        or not ({x.id for x in ast.walk(c.args[1])
                 if isinstance(x, ast.Name)} & _bound)]
check("K10 AST anti-vacuity (scope per LOG #403 MA-2: references >= 1 "
      "run-bound name, nothing more)",
      len(_ch) >= 8 and not _vac,
      f"check() calls = {len(_ch)}, bare/unbound = {len(_vac)}")

print("\n[VERDICT — D54b]")
if REFUSAL is None:
    print("  THE BLUEPRINT IS ADMISSIBLE AND IT SHATTERS.  A 9-actor,")
    print(f"  {len(H)}-event transport record, every event selected from")
    print("  the committed layer's own menu, whose SKY-B sky at the")
    print("  minting event realizes ALL 16 subsets of its 4 directions —")
    print("  including the empty trace and all six pairs — and is")
    print("  therefore NOT realizable as a 2+1 celestial sky.")
    print("  SCOPE, carried: the claim is reading-relative to SKY-B at")
    print("  the reported depth; it is an OBSTRUCTION certificate against")
    print("  2+1 under that committed definition, and says NOTHING")
    print("  positive about 3+1 — the S^2 cap-realization side is a")
    print("  separate unit.  The construction SATURATES the Dilworth")
    print("  gate rather than beating it.")
else:
    print(f"  THE BLUEPRINT WAS REFUSED at step '{REFUSAL[0]}' (prefix "
          f"{REFUSAL[1]}).  The refusal and its menu are printed above; "
          "the blocking clause is the deliverable, per pin §4.")

print(f"\n[d54b] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("EXIT 1")
    sys.exit(1)
print("EXIT 0")
