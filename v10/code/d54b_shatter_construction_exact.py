#!/usr/bin/env python3
"""
d54b_shatter_construction_exact.py — v10 D54 Stage 2: the targeted
shatter construction.  Pin: note-d54-dilworth-gate-pin.md §4 + the §8
first-run amendment (LOG #427; the pin was committed before this file,
and §8 records that its §4 blueprint was REFUTED by its own first run).

TWO BUILDS, both selected event-by-event from the committed d42b1 menu:

PART 1 — the §4 nine-actor blueprint, kept as a GATED NEGATIVE EXHIBIT:
admissible end to end, but it realizes only 8 of 16 traces.  Mechanism
(§8 A1): a delivery is a join in BOTH directions — the sender's wire
absorbs the receiver's accumulated past, so accumulator chains
cross-contaminate through shared senders.  The per-sender send-traces
form a chain: the theorem, biting its own construction.

PART 2 — the §8 COURIER architecture: sending into an EMPTY receiver
folds nothing back, so direction-actors mint one fresh courier per
contaminating step (11 couriers; 20 actors), and each courier performs
exactly one send into a non-empty accumulator.

Admissibility is decided ONLY by the layer: every event is SELECTED
from candidates_for's own menu.  A refusal prints prefix, spec and
menu, and is an exit-0 deliverable.  Exit 1 only on anchor breakage.
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
print("  banner: two builds, both menu-selected.  PART 1 = the pinned §4")
print("  blueprint as a NEGATIVE EXHIBIT (admissible, 8/16, the backflow")
print("  mechanism).  PART 2 = the §8 courier architecture.  Capacity =")
print("  D53 SC5; SKY-B only; depth reported; claims reading-relative.")

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
      "from committed D47a (AST extraction) — nothing re-implemented",
      callable(candidates_for) and callable(sky), "single sources")


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


class Builder:
    def __init__(self, actors):
        self.actors = actors
        self.H = []
        self.refusal = None

    def pick(self, spec, label):
        if self.refusal:
            return None
        menu = candidates_for(list(self.H), self.actors)
        hits = sorted((e for e, q in menu if spec(e)), key=repr)
        if not hits:
            self.refusal = (label, len(self.H))
            print(f"  [REFUSAL] '{label}' at prefix {len(self.H)}; menu "
                  f"size {len(menu)}, types "
                  f"{sorted({e[0] for e, q in menu})}")
            return None
        self.H.append(hits[0])
        return hits[0]

    def last_of(self, a):
        return max(i for i in range(len(self.H))
                   if a in ((self.H[i][1], self.H[i][2])
                            if self.H[i][0] == 'd' else (self.H[i][1],)))


def build_core(b):
    """Shared opening: X mints v1 (base event E), delivers to A-D, pads,
    directions at a common height.  Returns (E_IDX, V1, DIR_IDX)."""
    b.pick(lambda e: e[0] == 'p' and e[1] == 'X' and e[2] == V0
           and e[3] == 0, "X proposes on v0")
    E_IDX = len(b.H)
    b.pick(lambda e: e[0] == 'r' and e[1] == 'X', "X arbitrates -> E")
    V1 = None
    if not b.refusal:
        menu = candidates_for(list(b.H), b.actors)
        dv = sorted({e[3] for e, q in menu
                     if e[0] == 'd' and e[3] != V0}, key=repr)
        V1 = dv[0] if dv else None
    for r in ('A', 'B', 'C', 'D'):
        b.pick(lambda e, r=r: e[0] == 'd' and e[1] == 'X' and e[2] == r
               and e[3] == V1, f"X delivers v1 to {r}")
    DIR_IDX = {}
    if not b.refusal:
        C = poset_of(b.H)
        hh = heights(C)
        TARGET = hh[E_IDX] + 5
        for r in ('A', 'B', 'C', 'D'):
            while not b.refusal:
                hh = heights(poset_of(b.H))
                if hh[b.last_of(r)] + 1 == TARGET:
                    break
                b.pick(lambda e, r=r: e[0] == 'n' and e[1] == r,
                       f"{r} pads")
            e = b.pick(lambda e, r=r: e[0] == 'p' and e[1] == r
                       and e[2] == V1 and e[3] == 0,
                       f"{r} proposes on v1 (direction)")
            if e is not None:
                DIR_IDX[r] = len(b.H) - 1
    return E_IDX, V1, DIR_IDX


def dl(b, s, r, V1, label):
    b.pick(lambda e, s=s, r=r: e[0] == 'd' and e[1] == s and e[2] == r
           and e[3] == V1, label)


def sky_report(b, E_IDX, DIR_IDX):
    C = poset_of(b.H)
    hh = heights(C)
    dirs_idx = sorted(DIR_IDX.values())
    DEPTH = hh[dirs_idx[0]] - hh[E_IDX]
    dirs, rows = sky(C, E_IDX, 'B', DEPTH)
    idx_of = {v: k for k, v in DIR_IDX.items()}
    have = {tuple(sorted(idx_of[i] for i in t)) for t in set(rows)}
    return C, hh, dirs, rows, have, DEPTH, dirs_idx, idx_of


NEED = {tuple(sorted(s)) for k in range(5) for s in combinations('ABCD', k)}

# =========================================================== PART 1
print("\n[PART 1 — the pinned §4 blueprint, as a negative exhibit]")
b1 = Builder(('X', 'A', 'B', 'C', 'D', 'F', 'G', 'H', 'I'))
E1, V1a, D1 = build_core(b1)
for who, srcs in [('F', ['A', 'B', 'C', 'D']), ('G', ['B', 'C', 'D']),
                  ('H', ['A', 'C', 'D']), ('I', ['B', 'D', 'A'])]:
    for s in srcs:
        dl(b1, s, who, V1a, f"{who} <- {s}")
dl(b1, 'D', 'A', V1a, "A <- D")
dl(b1, 'D', 'C', V1a, "C <- D")
if b1.refusal is None:
    _, _, _, rows1, have1, DEP1, _, _ = sky_report(b1, E1, D1)
    check("N1 [NEGATIVE EXHIBIT, gated] THE PINNED §4 BLUEPRINT IS "
          "ADMISSIBLE AND FAILS: all events menu-offered, yet only "
          f"{len(have1 & NEED)}/16 subsets realized.  The mechanism is "
          "SENDER-WIRE BACKFLOW — a delivery joins both ways, the "
          "sender absorbs the receiver's accumulated past, and the "
          "accumulator chains collapse onto one.  The per-sender "
          "send-traces form a chain: the theorem biting its own "
          "construction.  Pin §8 A1, on the record",
          b1.refusal is None and len(have1 & NEED) == 8,
          f"events = {len(b1.H)}, subsets = {sorted(have1 & NEED)}")
else:
    check("N1 the §4 blueprint build reached its sky",
          b1.refusal is None, f"refusal = {b1.refusal}")

# =========================================================== PART 2
print("\n[PART 2 — the §8 courier architecture]")
COURIERS = {'J': 'B', 'K': 'C', 'L': 'C', 'M': 'C',
            'N': 'D', 'O': 'D', 'P': 'D', 'Q': 'D', 'R': 'D', 'S': 'D',
            'T': 'A'}
ACT2 = ('X', 'A', 'B', 'C', 'D', 'F', 'G', 'H', 'I') + tuple(COURIERS)
b2 = Builder(ACT2)
E2, V1b, D2 = build_core(b2)
# clean first receipts (empty accumulators; senders stay clean)
for s, r in [('A', 'F'), ('B', 'G'), ('A', 'H'), ('B', 'I')]:
    dl(b2, s, r, V1b, f"{r} <- {s} (clean first receipt)")
# courier mints (empty couriers; senders stay clean)
for c, src in COURIERS.items():
    dl(b2, src, c, V1b, f"mint courier {c} <- {src}")
# contaminating courier sends, chain order per accumulator
for c, r in [('J', 'F'), ('K', 'F'), ('N', 'F'),
             ('L', 'G'), ('O', 'G'),
             ('M', 'H'), ('P', 'H'),
             ('Q', 'I'), ('T', 'I'),
             ('R', 'A'), ('S', 'C')]:
    dl(b2, c, r, V1b, f"{r} <- courier {c} (carries {COURIERS[c]})")

check("K3 THE COURIER BLUEPRINT IS ADMISSIBLE END TO END: all "
      f"{len(b2.H)} events over {len(ACT2)} actors were offered by the "
      "committed layer's own menu at their prefixes — the layer, not "
      "the author, decided",
      b2.refusal is None,
      f"events = {len(b2.H)}, refusal = {b2.refusal}")

if b2.refusal is None:
    C, hh, dirs, rows, have, DEPTH, dirs_idx, idx_of = \
        sky_report(b2, E2, D2)
    r = set(rows)
    n = len(b2.H)

    inc_ok = all(not (C[i][j] or C[j][i])
                 for i, j in combinations(dirs_idx, 2))
    check("K4 the directions are a genuine sky: pairwise INCOMPARABLE "
          "(proposal locality), one common height, all strictly above "
          "E; the height offset is REPORTED — the claim is "
          "reading-relative to SKY-B at that depth",
          inc_ok and len({hh[i] for i in dirs_idx}) == 1
          and all(C[E2][i] for i in dirs_idx),
          f"incomparable = {inc_ok}, h = {hh[dirs_idx[0]]}, "
          f"DEPTH = {DEPTH}")

    check("K5 SKY-B at E reproduces the intended directions from the "
          "committed instrument itself",
          sorted(dirs) == dirs_idx,
          f"instrument dirs = {sorted(dirs)}, blueprint = {dirs_idx}")

    check("K6 CAPACITY BY THE CORRECTED CONDITION (D53 SC5, never D47 "
          "SG2): >= 4 directions, >= 16 DISTINCT traces, empty trace "
          "present",
          len(dirs) >= 4 and len(r) >= 16 and frozenset() in r,
          f"|dirs| = {len(dirs)}, distinct traces = {len(r)}, empty = "
          f"{frozenset() in r}")

    wit = shattered_set(rows, dirs, 4)
    check("K7 **ALL 16 SUBSETS ARE REALIZED AND THE INSTRUMENT RETURNS "
          "A SHATTERED 4-SET.**  Under the committed SKY-B reading at "
          "the reported depth, this record's sky is NOT realizable as a "
          "2+1 celestial sky — arcs on a circle cannot shatter 4 (D47a "
          "SG0, constructed, not cited)",
          NEED <= have and wit is not None,
          f"subsets = {len(have & NEED)}/16; shattered 4-set = "
          f"{sorted(idx_of[i] for i in wit) if wit else None}")

    if wit is not None:
        print(f"  [WITNESS TRANSPORT-SHATTER-4] taken by a REAL record: "
              f"set = {sorted(idx_of[i] for i in wit)}, actors = "
              f"{len(ACT2)}, events = {n}, depth = {DEPTH}")

    byact = defaultdict(set)
    for f in range(n):
        if C[E2][f]:
            byact[b2.H[f][1]].add(
                frozenset(c for c in dirs if c == f or C[c][f]))
    nested = all(a <= b or b <= a
                 for trs in byact.values()
                 for a, b in combinations(trs, 2))
    contributing = sum(1 for trs in byact.values() if trs)
    check("K8 CONSISTENCY WITH THE DILWORTH GATE: traces decompose into "
          "per-initiator CHAINS (zero crossings) and >= 6 actors "
          "contribute — the construction SATURATES the theorem, it does "
          "not beat it",
          nested and contributing >= 6,
          f"nested = {nested}, contributing actors = {contributing} "
          f"(bound: 6), total = {len(ACT2)}")

    for kind in ('A', 'C'):
        dA, rA = sky(C, E2, kind)
        check(f"K9-{kind} D53 CONTROL: SKY-{kind} on this record has NO "
              "empty trace — the definition-level disqualification "
              "reproduced on the constructed object",
              frozenset() not in set(rA),
              f"|dirs| = {len(dA)}, empty = {frozenset() in set(rA)}")

# hygiene
_self = ast.parse(open('v10/code/d54b_shatter_construction_exact.py').read())
_bound = set()
for _n in ast.walk(_self):
    if isinstance(_n, ast.Name) and isinstance(_n.ctx, ast.Store):
        _bound.add(_n.id)
    elif isinstance(_n, (ast.FunctionDef, ast.ClassDef)):
        _bound.add(_n.name)
_ch = [c for c in ast.walk(_self) if isinstance(c, ast.Call)
       and isinstance(c.func, ast.Name) and c.func.id == 'check']
_vac = [c for c in _ch if isinstance(c.args[1], ast.Constant)]
check("K10 AST anti-vacuity (scope per LOG #403 MA-2: no bare-constant "
      "predicates, nothing more)",
      len(_ch) >= 9 and not _vac,
      f"check() calls = {len(_ch)}, bare = {len(_vac)}")

print("\n[VERDICT — D54b]")
if b2.refusal is None:
    print("  THE COURIER BLUEPRINT IS ADMISSIBLE AND IT SHATTERS: a")
    print(f"  20-actor, {len(b2.H)}-event transport record, every event")
    print("  selected from the committed layer's own menu, whose SKY-B")
    print("  sky at the minting event realizes ALL 16 subsets of its 4")
    print("  directions and returns a shattered 4-set.  Under that")
    print("  committed reading the sky is NOT realizable as a 2+1")
    print("  celestial sky.")
    print("  AND THE PINNED BLUEPRINT'S FAILURE IS PART OF THE RESULT:")
    print("  sender-wire backflow is why 9 actors and 31 events were not")
    print("  enough — knowledge transport is monotone along wires, and")
    print("  only clean couriers can carry a single direction into a")
    print("  charged accumulator.")
    print("  SCOPE: reading-relative to SKY-B at the reported depth; an")
    print("  obstruction certificate against 2+1, NOT a positive 3+1")
    print("  claim — the S^2 side is a separate unit.  20 actors vs the")
    print("  theorem's bound of 6: minimality is an open residue.")
else:
    print(f"  REFUSED at '{b2.refusal[0]}' (prefix {b2.refusal[1]}) — "
          "the blocking clause is the deliverable, per pin §4.")

print(f"\n[d54b] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("EXIT 1")
    sys.exit(1)
print("EXIT 0")
