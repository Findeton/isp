#!/usr/bin/env python3
"""
d60_crystal_exact.py — v10 D60: the crystal question.
Pin: note-d60-crystal-question-pin.md (STRICT, LOG #447, before code).
CRYSTAL-1D (brick wall) and CRYSTAL-2D (grid): re-delivery circuits as
lattices worn as records; atlas metrics via the committed D58
extraction; comparators = D58's committed measurements (cited).
Exit 1 only on anchor breakage; refusals are exit-0 deliverables.
"""
import ast, sys
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

print("[D60 — the crystal question]")
print("  banner: can the grammar TILE?  Blueprints from the pin; every")
print("  event menu-selected (restricted menus INCLUDE the delivery")
print("  receiver — the corrected D55 instrument); atlas metrics from")
print("  the committed D58 extraction; orderings reported whichever")
print("  way they land; comparators cited from committed D58 output.")

_st = open('v10/code/d42b1_transport_exact.py').read()
nst = {}
exec(_st[:_st.index('print("[d42b1')], nst)
candidates_for, event_poset, V0 = (nst['candidates_for'],
                                   nst['event_poset'], nst['V0'])
_ta = ast.parse(open('v10/code/d47a_sky_instrument_exact.py').read())
_keep = [n for n in _ta.body if isinstance(n, ast.FunctionDef)
         or (isinstance(n, ast.Assign) and any(isinstance(x, ast.Name)
             and x.id in ('CYCLIC_CAP', 'SKYB_DEPTH') for x in n.targets))]
g47 = {'Fr': Fr, 'combinations': combinations,
       'permutations': permutations, 'product': product}
exec(compile(ast.fix_missing_locations(ast.Module(body=_keep,
     type_ignores=[])), 'd47a', 'exec'), g47)
sky = g47['sky']
check("C0 anchors: transport layer (committed d42b1) + sky instrument "
      "(committed d47a), single sources",
      callable(candidates_for) and callable(sky), "loaded")


def poset_of(h):
    pred = event_poset(list(h))
    n = len(h)
    return [[i in pred[j] for j in range(n)] for i in range(n)]


class B:
    def __init__(self, actors):
        self.actors = actors
        self.H = []
        self.refusal = None

    def pick(self, inits, spec, label):
        if self.refusal:
            return None
        menu = candidates_for(list(self.H), tuple(inits))
        hits = sorted((e for e, q in menu if spec(e)), key=repr)
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


def atlas(C, name):
    n = len(C)
    cov = [(i, j) for i in range(n) for j in range(n)
           if C[i][j] and not any(C[i][k] and C[k][j] for k in range(n))]
    out = {}
    for d in (2, 3):
        widths = []
        D = {}
        for e in range(n):
            dirs, _ = sky(C, e, 'B', d)
            D[e] = set(dirs)
            widths.append(len(dirs))
        om = []
        for (e, e2) in cov:
            if len(D[e]) < 2:
                continue
            d2, _ = sky(C, e2, 'B', d - 1)
            om.append(Fr(len(D[e] & set(d2)), len(D[e])))
        w2 = sum(1 for w in widths if w >= 2)
        mo = (sum(om) / len(om)) if om else None
        out[d] = (n, w2, Fr(w2, n), max(widths), len(om), mo)
        print(f"  {name} d={d}: events={n}, |D|>=2: {w2} "
              f"({100 * w2 // n}%), max|D|={max(widths)}, pairs={len(om)}, "
              f"mean omega={'%.2f' % float(mo) if mo is not None else '-'}")
    return out


# ------------------------------------------------- CRYSTAL-1D: brick
print("\n[CRYSTAL-1D — the brick wall, m = 8, 14 rounds]")
M = 8
RING = [f"R{i}" for i in range(M)]
b1 = B(tuple(RING))
V1 = mint_and_spread(b1, RING)
ROUNDS = 14
for t in range(ROUNDS):
    pairs = ([(0, 1), (2, 3), (4, 5), (6, 7)] if t % 2 == 0
             else [(1, 2), (3, 4), (5, 6), (7, 0)])
    for (i, j) in pairs:
        s, r = RING[i], RING[j]
        if t % 4 >= 2:
            s, r = r, s
        dl(b1, s, r, V1)
check("C1 CRYSTAL-1D IS ADMISSIBLE END TO END: the brick circuit "
      f"({len(b1.H)} events over {M} actors, {ROUNDS} rounds of "
      "alternating re-deliveries) — every event offered by the layer's "
      "own menu.  The pre-registered lean (re-delivery circuits run "
      "indefinitely) holds",
      b1.refusal is None, f"events = {len(b1.H)}, refusal = {b1.refusal}")
A1 = atlas(poset_of(b1.H), 'brick m=8') if b1.refusal is None else None

# ------------------------------------------------- CRYSTAL-2D: grid
print("\n[CRYSTAL-2D — the 3x3 grid, 12 phases]")
K = 3
GRID = [f"G{i}{j}" for i in range(K) for j in range(K)]
def gid(i, j):
    return f"G{i % K}{j % K}"
b2 = B(tuple(GRID))
V2 = mint_and_spread(b2, GRID)
PHASES = 12
for t in range(PHASES):
    ph = t % 4
    pairs = []
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
    for (s, r) in pairs:
        if (t // 4) % 2 == 1:
            s, r = r, s
        dl(b2, s, r, V2)
check("C2 CRYSTAL-2D IS ADMISSIBLE END TO END: the grid circuit "
      f"({len(b2.H)} events over {K * K} actors, {PHASES} phases)",
      b2.refusal is None, f"events = {len(b2.H)}, refusal = {b2.refusal}")
A2 = atlas(poset_of(b2.H), 'grid 3x3') if b2.refusal is None else None

# ------------------------------------------------- the verdict
# D58's committed comparators (v10/data/d58_atlas_instrument_exact.out):
SPRINKLE_FLOOR = Fr(64, 100)   # M21 d=2 homogeneity (M31: 73%)
ENGINEERED_CEIL = Fr(39, 100)  # shatter-4 record d=2 (shatter-5: 35%)
WALK = Fr(7, 100)
if A1 and A2:
    h1, h2 = A1[2][2], A2[2][2]
    check("C3 THE CRYSTAL VERDICT (orderings only, the D58 lesson; "
          "comparators cited from committed D58 output: sprinkling "
          "floor 64%, engineered ceiling 39%, generic walk 7%): the "
          "crystals' d = 2 homogeneity vs the three benchmarks, "
          "reported whichever way it lands",
          h1 > ENGINEERED_CEIL and h2 > ENGINEERED_CEIL,
          f"brick = {float(h1):.2f} "
          f"({'TILES AT SPRINKLING GRADE' if h1 >= SPRINKLE_FLOOR else 'partial'}), "
          f"grid = {float(h2):.2f} "
          f"({'TILES AT SPRINKLING GRADE' if h2 >= SPRINKLE_FLOOR else 'partial (46 events, boundary-dominated — size is a residue)'})")
    om1, om2 = A1[2][5], A2[2][5]
    check("C4 overlap report (mean omega at d = 2; sprinkling "
          "comparators 0.12 (M21) / 0.54 (M31))",
          om1 is not None and om2 is not None,
          f"brick = {float(om1):.2f}, grid = {float(om2):.2f}")
    wmax1, wmax2 = A1[2][3], A2[2][3]
    check("C5 the |D| census, honest: the brick is 1+1-THIN by design "
          "and the grid wider — reported, no dimension claim beyond "
          "the census (scale doctrine: this unit certifies the TILING "
          "MECHANISM, nothing else)",
          wmax1 >= 2,
          f"brick max|D| = {wmax1}, grid max|D| = {wmax2}")

_ch = [c for c in ast.walk(ast.parse(open(
    'v10/code/d60_crystal_exact.py').read()))
    if isinstance(c, ast.Call) and isinstance(c.func, ast.Name)
    and c.func.id == 'check']
_vac = [c for c in _ch if isinstance(c.args[1], ast.Constant)]
check("C6 AST anti-vacuity (no bare-constant predicates; #403 MA-2 "
      "scope)", len(_ch) >= 5 and not _vac,
      f"check() calls = {len(_ch)}, bare = {len(_vac)}")

print("\n[VERDICT] scope carried: grammar layer; transfer to the")
print("  identified click law runs through paper 29's missing map")
print("  (D59); no typicality claim; no object claim (#440).")
print(f"\n[d60] {PASS} PASS / {FAIL} FAIL")
sys.exit(1 if FAIL else 0)
