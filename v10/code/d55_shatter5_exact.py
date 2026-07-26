#!/usr/bin/env python3
"""
d55_shatter5_exact.py — v10 D55 A1: the GENERALIZED courier builder and
the shatter-5 question.  Pin: note-d55-dimension-meter-pin.md (STRICT,
LOG #430, committed before this file existed).

THE MACHINE (pin §2): given the dBTK symmetric chain decomposition
scd(m), build one minting actor X, m direction-actors, one accumulator
per chain, one clean courier per contaminating step (cost per chain
(|S1|-1) + (len-1)).  m = 4 re-derives D54's trace family AS AN ANCHOR;
m = 5 is the question: 10 chains, 26 couriers, 42 actors, 84 events.

TRACTABILITY, declared and gated: menus are enumerated restricted to
the step's initiator.  admissible(acts, e) reads only (acts, e) — no
actor list — so membership cannot change; sampled full-menu equivalence
is GATED (TG-EQ).

Exit 1 only on anchor breakage (the m = 4 anchor failing, the sampled
menu-equivalence failing).  A refusal in the m = 5 build is an exit-0
deliverable naming the step.
Run from the repo root: python3 v10/code/d55_shatter5_exact.py
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

print("[D55 A1 — shatter-5 via the generalized courier builder]")
print("  banner: the builder is MECHANICAL from scd(m); m = 4 must")
print("  reproduce D54's family (anchor, exit 1 on failure); m = 5 is")
print("  the pre-registered question.  Menus initiator-restricted, with")
print("  sampled full-menu equivalence GATED.  Every event selected")
print("  from the committed layer's own menu.")

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

check("G0 anchors: transport layer from committed d42b1; sky/shatter "
      "from committed D47a (AST extraction)",
      callable(candidates_for) and callable(sky), "single sources")


def scd(k):
    """The committed D54 dBTK recursion (chain PARTITION of B_k)."""
    if k == 0:
        return [[frozenset()]]
    out = []
    for ch in scd(k - 1):
        top = ch[-1] | {k - 1}
        out.append(ch + [top])
        if len(ch) > 1:
            out.append([a | {k - 1} for a in ch[:-1]])
    return out


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
        self.eq_samples = []

    def pick(self, initiators, spec, label, sample_eq=False):
        """Select from the menu RESTRICTED to `initiators`; optionally
        record a full-menu equivalence sample (gated later)."""
        if self.refusal:
            return None
        menu = candidates_for(list(self.H), tuple(initiators))
        hits = sorted((e for e, q in menu if spec(e)), key=repr)
        if not hits:
            self.refusal = (label, len(self.H))
            print(f"  [REFUSAL] '{label}' at prefix {len(self.H)}; "
                  f"restricted menu size {len(menu)}, types "
                  f"{sorted({e[0] for e, q in menu})}")
            for e, q in sorted(menu, key=lambda x: repr(x[0]))[:15]:
                print(f"      offered: {e}")
            return None
        e = hits[0]
        if sample_eq:
            full = candidates_for(list(self.H), self.actors)
            restr_from_full = sorted(
                (ev for ev, q in full
                 if ev[1] in initiators
                 and (ev[0] != 'd' or ev[2] in initiators)), key=repr)
            menu_sorted = sorted((ev for ev, q in menu), key=repr)
            self.eq_samples.append(
                (label, e in [ev for ev, q in full],
                 menu_sorted == restr_from_full))
        self.H.append(e)
        return e

    def last_of(self, a):
        return max(i for i in range(len(self.H))
                   if a in ((self.H[i][1], self.H[i][2])
                            if self.H[i][0] == 'd' else (self.H[i][1],)))


def build(m, sample_steps=()):
    """The generalized courier builder for shatter-m."""
    dirs_a = [f"D{i}" for i in range(m)]
    chains = []
    for ch in scd(m):
        ch2 = [s for s in ch if s]              # X's delivery supplies {}
        if len(ch2) == 1 and len(next(iter(ch2))) == 1:
            continue                            # singletons: directions
        chains.append(ch2)
    accs = [f"A{i}" for i in range(len(chains))]
    n_cour = sum((len(ch[0]) - 1) + (len(ch) - 1) for ch in chains)
    cours = [f"C{i}" for i in range(n_cour)]
    ACT = tuple(['X'] + dirs_a + accs + cours)
    b = Builder(ACT)
    step = [0]

    def pick(inits, spec, label):
        step[0] += 1
        return b.pick(inits, spec, label,
                      sample_eq=step[0] in sample_steps)

    pick(('X',), lambda e: e[0] == 'p' and e[1] == 'X' and e[2] == V0
         and e[3] == 0, "X proposes")
    E_IDX = len(b.H)
    pick(('X',), lambda e: e[0] == 'r' and e[1] == 'X', "X arbitrates")
    V1 = None
    if not b.refusal:
        menu = candidates_for(list(b.H), ('X', dirs_a[0]))
        dv = sorted({e[3] for e, q in menu
                     if e[0] == 'd' and e[3] != V0}, key=repr)
        V1 = dv[0] if dv else None
    for r in dirs_a:
        pick(('X', r), lambda e, r=r: e[0] == 'd' and e[1] == 'X'
             and e[2] == r and e[3] == V1, f"X delivers v1 to {r}")
    DIR_IDX = {}
    if not b.refusal:
        hh = heights(poset_of(b.H))
        TARGET = hh[E_IDX] + m + 1
        for r in dirs_a:
            while not b.refusal:
                hh = heights(poset_of(b.H))
                if hh[b.last_of(r)] + 1 == TARGET:
                    break
                pick((r,), lambda e, r=r: e[0] == 'n' and e[1] == r,
                     f"{r} pads")
            e = pick((r,), lambda e, r=r: e[0] == 'p' and e[1] == r
                     and e[2] == V1 and e[3] == 0, f"{r} direction")
            if e is not None:
                DIR_IDX[r] = len(b.H) - 1

    def dl(s, r, label):
        # deliveries need BOTH endpoints in the restricted actor list:
        # candidates_for ENUMERATES receivers from `actors` (run-1
        # refusal taught this — the restriction soundness claim holds
        # for admissible(), not for enumeration)
        pick((s, r), lambda e, s=s, r=r: e[0] == 'd' and e[1] == s
             and e[2] == r and e[3] == V1, label)

    ci = [0]

    def courier_step(direction, acc):
        c = cours[ci[0]]
        ci[0] += 1
        dl(direction, c, f"mint {c} <- {direction}")
        dl(c, acc, f"{acc} <- {c} (carries {direction})")

    for ch, acc in zip(chains, accs):
        S1 = sorted(ch[0])
        dl(dirs_a[S1[0]], acc, f"{acc} <- {dirs_a[S1[0]]} (clean first)")
        for j in S1[1:]:
            courier_step(dirs_a[j], acc)
        cur = ch[0]
        for nxt in ch[1:]:
            (j,) = sorted(nxt - cur)
            courier_step(dirs_a[j], acc)
            cur = nxt
    return b, E_IDX, DIR_IDX, len(chains), n_cour, len(ACT)


def family_of(b, E_IDX, DIR_IDX):
    C = poset_of(b.H)
    hh = heights(C)
    didx = sorted(DIR_IDX.values())
    DEPTH = hh[didx[0]] - hh[E_IDX]
    dirs, rows = sky(C, E_IDX, 'B', DEPTH)
    name = {v: k for k, v in DIR_IDX.items()}
    have = {frozenset(name[i] for i in t) for t in set(rows)}
    return C, dirs, rows, have, DEPTH, didx, name


# ============================== m = 4 anchor ============================
print("\n[the m = 4 anchor — the general machine vs D54's hand build]")
b4, E4, D4, nch4, nc4, na4 = build(4, sample_steps=(3, 9, 20))
if b4.refusal is None:
    C4, dirs4, rows4, have4, DEP4, didx4, _ = family_of(b4, E4, D4)
    need4 = {frozenset(s) for k in range(5)
             for s in combinations(sorted(D4), k)}
    w4 = shattered_set(rows4, dirs4, 4)
    check("G1 THE ANCHOR: the GENERAL builder at m = 4 re-derives D54's "
          "result — all 16 subsets realized, shattered 4-set returned — "
          "from scd(4) alone, with no hand-tuning.  (The record differs "
          "from D54's in actor accounting — 6 accumulators vs 4+2 late "
          "deliveries — but the trace FAMILY is the same: all of B4)",
          need4 <= have4 and w4 is not None,
          f"actors = {na4} (chains {nch4}, couriers {nc4}), events = "
          f"{len(b4.H)}, depth = {DEP4}, subsets = "
          f"{len(have4 & need4)}/16, shatter = {w4 is not None}")
else:
    check("G1 the m = 4 anchor reached its sky",
          b4.refusal is None, f"refusal = {b4.refusal}")

eq_ok = all(inmenu and eq for _, inmenu, eq in b4.eq_samples)
check("G2 TG-EQ [ANCHOR] the initiator-restricted menu is EXACTLY the "
      "full menu filtered to those initiators, on sampled steps — "
      "admissible(acts, e) reads no actor list, and this gates it",
      len(b4.eq_samples) >= 3 and eq_ok,
      f"samples = {[(l, i, q) for l, i, q in b4.eq_samples]}")

# ============================== m = 5 ==================================
print("\n[the m = 5 build — THE QUESTION]")
b5, E5, D5, nch5, nc5, na5 = build(5, sample_steps=(3,))
check("G3 THE m = 5 BUILD IS ADMISSIBLE END TO END: "
      f"{len(b5.H)} events over {na5} actors ({nch5} accumulator "
      "chains, "
      f"{nc5} couriers), every event offered by the committed layer's "
      "own menu — the layer, not the author, decided",
      b5.refusal is None,
      f"events = {len(b5.H)}, refusal = {b5.refusal}")

if b5.refusal is None:
    C5, dirs5, rows5, have5, DEP5, didx5, name5 = family_of(b5, E5, D5)
    r5 = set(rows5)
    need5 = {frozenset(s) for k in range(6)
             for s in combinations(sorted(D5), k)}
    inc5 = all(not (C5[i][j] or C5[j][i])
               for i, j in combinations(didx5, 2))
    check("G4 the five directions are a genuine sky: pairwise "
          "incomparable, one height, above E; depth reported",
          inc5 and sorted(dirs5) == didx5 and len(dirs5) == 5,
          f"|dirs| = {len(dirs5)}, depth = {DEP5}")
    check("G5 CAPACITY (the SC5 analog at m = 5): >= 5 directions, "
          ">= 32 DISTINCT traces, empty trace present",
          len(dirs5) >= 5 and len(r5) >= 32 and frozenset() in r5,
          f"distinct traces = {len(r5)}, empty = {frozenset() in r5}")
    w5 = shattered_set(rows5, dirs5, 5)
    check("G6 **ALL 32 SUBSETS REALIZED AND A SHATTERED 5-SET "
          "RETURNED.**  The transport layer admits a sky that exceeds "
          "the sphere's VC dimension — caps on S^2 shatter 4 and never "
          "5 (D54 round 1, Radon-certified) — so this sky is not "
          "realizable by caps on S^2.  THE METER READS BEYOND 3+1: the "
          "admissibility layer does not select the sphere",
          need5 <= have5 and w5 is not None,
          f"subsets = {len(have5 & need5)}/32; shattered 5-set = "
          f"{sorted(name5[i] for i in w5) if w5 else None}")
    if w5 is not None:
        print(f"  [WITNESS TRANSPORT-SHATTER-5] actors = {na5}, events "
              f"= {len(b5.H)}, depth = {DEP5}, set = "
              f"{sorted(name5[i] for i in w5)}")

    byact = defaultdict(set)
    for f in range(len(b5.H)):
        if C5[E5][f]:
            byact[b5.H[f][1]].add(
                frozenset(c for c in dirs5 if c == f or C5[c][f]))
    nested = all(a <= b or b <= a for trs in byact.values()
                 for a, b in combinations(trs, 2))
    contributing = sum(1 for trs in byact.values() if trs)
    mid5 = {frozenset(s) for s in combinations(sorted(D5), 2)}
    tight = mid5 <= have5 and have5 >= need5
    check("G7 DILWORTH CONSISTENCY at m = 5: per-initiator traces are "
          "chains (zero crossings); contributing actors >= C(5,2) = 10 "
          "(the gate's price, paid); and the realized family contains "
          "the 10-element middle layer, so its min chain cover is "
          "EXACTLY 10 — Dilworth-tight",
          nested and contributing >= 10 and tight,
          f"nested = {nested}, contributing = {contributing} (bound "
          f"10), middle layer present = {mid5 <= have5}")

    print("\n  per-depth table (D54 K11 discipline):")
    sh_ds = []
    for dd in range(1, 10):
        dD, rD = sky(C5, E5, 'B', dd)
        rset = set(rD)
        wD = (shattered_set(rD, dD, 5)
              if len(dD) >= 5 else None)
        if wD is not None:
            sh_ds.append(dd)
        print(f"    d={dd}: |dirs|={len(dD)}, traces={len(rset)}, "
              f"shatter5={'YES' if wD else None}")
    check("G8 PER-DEPTH REPORTING: the depths at which the record "
          "shatters a 5-set are enumerated, not sampled",
          len(sh_ds) >= 1 and DEP5 in sh_ds,
          f"shatter-5 depths = {sh_ds}")

# hygiene
_self = ast.parse(open('v10/code/d55_shatter5_exact.py').read())
_ch = [c for c in ast.walk(_self) if isinstance(c, ast.Call)
       and isinstance(c.func, ast.Name) and c.func.id == 'check']
_vac = [c for c in _ch if isinstance(c.args[1], ast.Constant)]
check("G9 AST anti-vacuity (no bare-constant predicates; scope per LOG "
      "#403 MA-2: exactly that, nothing more)",
      len(_ch) >= 8 and not _vac,
      f"check() calls = {len(_ch)}, bare = {len(_vac)}")

print("\n[VERDICT — D55 A1]")
if b5.refusal is None and 'w5' in dir() and w5 is not None:
    print("  SHATTER-5 IS CONSTRUCTIBLE.  The generalized courier")
    print(f"  builder, mechanical from scd(5), yields a {na5}-actor,")
    print(f"  {len(b5.H)}-event record whose SKY-B sky realizes all 32")
    print("  subsets of its 5 directions.  Caps on S^2 stop at 4, so")
    print("  this sky exceeds the sphere: THE ADMISSIBILITY LAYER DOES")
    print("  NOT SELECT 3+1.  The ladder measures capacity; selection,")
    print("  if it exists anywhere, lives in the MEASURE — the")
    print("  convergence question, exactly as pre-stated in the pin.")
    print("  Scope: reading-relative to SKY-B, depths enumerated; ONE")
    print("  engineered record — NO genericity claim (not posable at")
    print("  transport scope, D52).")
else:
    print("  THE m = 5 BUILD WAS REFUSED — the refusing step and menu")
    print("  are printed above; the blocking clause is the deliverable")
    print("  and would be the framework's first dimensional selection.")

print(f"\n[d55] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("EXIT 1")
    sys.exit(1)
print("EXIT 0")
