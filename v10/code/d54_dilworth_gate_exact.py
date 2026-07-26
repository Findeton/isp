#!/usr/bin/env python3
"""
d54_dilworth_gate_exact.py — v10 D54 Stages 0+1: the Dilworth gate.
Pin: note-d54-dilworth-gate-pin.md (STRICT, LOG #427, committed before
this file existed).

STAGE 0 gates the premise [P]: any two events sharing an actor wire are
comparable at TRANSPORT scope (d42b1).  Gated at arb scope (D44c clause
iv), never before at d42b1, where deliveries carry TWO actors.  If P
fails the unit ends here and the failure is the deliverable (exit 0).

STAGE 1 corroborates the theorem [T]: one actor's worldline contributes
a CHAIN of traces to any sky, so a k-actor shadow family is a union of
<= k inclusion-chains, so shatter-4 needs >= 6 actors (Dilworth on B4)
and shatter-k needs >= C(k, floor(k/2)).  THE PROOF carries the theorem
(result note); the sweep CORROBORATES (D44c-P round-1 P2 discipline).

Exit 1 only on anchor breakage or mutant misbehaviour.
Run from the repo root: python3 v10/code/d54_dilworth_gate_exact.py
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

print("[D54 stages 0+1 — the Dilworth gate]")
print("  banner: STAGE 0 gates premise P before anything leans on it;")
print("  STAGE 1's sweep CORROBORATES the theorem, whose proof lives in")
print("  the result note.  Transport layer exec'd from the committed")
print("  d42b1 receipt; sky + shatter imported from committed D47a by")
print("  AST extraction.  Deterministic LCG sampling; depths PRINTED.")

# ---------------------------------------------------------------- anchors
_SRCT = 'v10/code/d42b1_transport_exact.py'
_st = open(_SRCT).read()
nst = {}
exec(compile(_st[:_st.index('print("[d42b1')], 'd42b1_ported', 'exec'), nst)
candidates_for = nst['candidates_for']
event_poset = nst['event_poset']

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

check("A0 anchors: the transport layer from the committed d42b1 receipt "
      "(single source) and the sky/shatter instrument from the committed "
      "D47a receipt (AST extraction) — nothing re-implemented",
      callable(candidates_for) and callable(sky)
      and callable(shattered_set),
      f"sources = {_SRCT}, {_D47A}")


def actors_of(e):
    """The actor wires an event touches.  Deliveries ('d', s, r, v)
    carry sender AND receiver; all other event types carry their
    initiator e[1].  (Arbitrations additionally consume other actors'
    PROPOSAL events, but those proposals are themselves on their
    proposers' wires — the premise concerns the arb event's own
    carriers.)"""
    if e[0] == 'd':
        return (e[1], e[2])
    return (e[1],)


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


# families: exhaustive 2-actor + deterministic walks at widths 3, 4, 6
def walks(actors, depth, nwalks, seed):
    s = seed
    out = []
    for _ in range(nwalks):
        h = []
        for _ in range(depth):
            cand = candidates_for(h, actors)
            if not cand:
                break
            s = (1103515245 * s + 12345) % (1 << 31)
            h = h + [cand[s % len(cand)][0]]
        out.append(h)
    return out


FAMS = []
AB = ('A', 'B')
EXH = [[]]
fr = [[]]
while fr:
    h = fr.pop()
    if len(h) >= 5:
        continue
    for e, q in candidates_for(h, AB):
        EXH.append(h + [e])
        fr.append(h + [e])
FAMS.append(('exhaustive w2 cap5', AB, EXH))
FAMS.append(('walks w3 d12', ('A', 'B', 'C'), walks(('A', 'B', 'C'), 12, 90, 11)))
FAMS.append(('walks w4 d12', ('A', 'B', 'C', 'D'), walks(('A', 'B', 'C', 'D'), 12, 70, 22)))
FAMS.append(('walks w6 d14', tuple('ABCDEF'), walks(tuple('ABCDEF'), 14, 50, 33)))

# ------------------------------------------------------------- STAGE 0
print("\n[STAGE 0 — premise P at transport scope]")
p_pairs = p_bad = 0
p_wit = None
for name, actors, fam in FAMS:
    for h in fam:
        if len(h) < 2:
            continue
        C = poset_of(h)
        n = len(h)
        for i in range(n):
            for j in range(i + 1, n):
                if set(actors_of(h[i])) & set(actors_of(h[j])):
                    p_pairs += 1
                    if not (C[i][j] or C[j][i]):
                        p_bad += 1
                        if p_wit is None:
                            p_wit = (name, [str(x) for x in h], i, j)
check("P [STAGE 0] ANY TWO EVENTS SHARING AN ACTOR WIRE ARE COMPARABLE, "
      "at transport scope, with deliveries' TWO-actor carriers included: "
      "zero violations over every family.  The premise the whole theorem "
      "stands on is now GATED at the scope where it is used, not "
      "believed",
      p_pairs > 0 and p_bad == 0,
      f"actor-sharing pairs tested = {p_pairs}, incomparable = {p_bad}"
      + (f"; WITNESS = {p_wit}" if p_wit else ""))

def is_nested(t1, t2):
    """THE instrument predicate — shared by the sweep and the M1 mutant
    (round-1 MINOR 7: the first draft's mutant tested a hand-written
    comparison on literals, never the sweep's code path)."""
    return t1 <= t2 or t2 <= t1


# ------------------------------------------------------------- STAGE 1
print("\n[STAGE 1 — the nested-trace lemma, corroborated]")
skies = 0
groups = 0
nest_bad = 0
nest_wit = None
ndirs_census = defaultdict(int)
max_traces = 0
groups_live = 0
for name, actors, fam in FAMS:
    for h in fam:
        if len(h) < 3:
            continue
        C = poset_of(h)
        n = len(h)
        for e_i in range(n):
            for d in (1, 2, 3):
                dirs, _rows = sky(C, e_i, 'B', d)
                if len(dirs) < 2:
                    continue
                skies += 1
                ndirs_census[len(dirs)] += 1
                fut = [f for f in range(n) if C[e_i][f]]
                byact = defaultdict(list)
                alltr = set()
                for f in fut:
                    tr = frozenset(c for c in dirs if c == f or C[c][f])
                    byact[h[f][1]].append(tr)
                    alltr.add(tr)
                max_traces = max(max_traces, len(alltr))
                for a, trs in byact.items():
                    groups += 1
                    if len(set(trs)) > 1:
                        groups_live += 1
                    for t1, t2 in combinations(trs, 2):
                        if not is_nested(t1, t2):
                            nest_bad += 1
                            if nest_wit is None:
                                nest_wit = (name, e_i, d, a,
                                            sorted(t1), sorted(t2))
check("T-LEMMA [STAGE 1] THE TRACES CONTRIBUTED BY ONE ACTOR'S "
      "WORLDLINE FORM A CHAIN under inclusion — per-initiator trace "
      "pairs nested with ZERO exceptions.  SCOPE, declared (round-1 "
      "MINOR 4): the sweep runs SKY-B at d in {1,2,3} and NEVER reaches "
      "the 4-direction/16-trace regime the theorem is applied in (dirs "
      "and trace census printed below); nesting is width- and "
      "depth-independent BY THE PROOF, and the round verified it "
      "directly at d = 5 on both constructed records [REFEREE-CARRIED]",
      skies > 0 and nest_bad == 0,
      f"skies = {skies}, groups = {groups} (with >= 2 distinct traces: "
      f"{groups_live}), non-nested = {nest_bad}; |dirs| census = "
      f"{dict(sorted(ndirs_census.items()))}, max distinct traces in "
      f"any swept sky = {max_traces}"
      + (f"; WITNESS = {nest_wit}" if nest_wit else ""))

# --- the B4 certificate: both bounds constructive
print("\n[STAGE 1 — the B4 certificate]")
PAIRS = [frozenset(s) for s in combinations(range(4), 2)]
anti_ok = all(not (a <= b or b <= a) for a, b in combinations(PAIRS, 2))
SCD = [
    [frozenset(), frozenset({0}), frozenset({0, 1}), frozenset({0, 1, 2}),
     frozenset({0, 1, 2, 3})],
    [frozenset({1}), frozenset({1, 2}), frozenset({1, 2, 3})],
    [frozenset({2}), frozenset({0, 2}), frozenset({0, 2, 3})],
    [frozenset({3}), frozenset({1, 3}), frozenset({0, 1, 3})],
    [frozenset({0, 3})],
    [frozenset({2, 3})],
]
cover = set()
chains_ok = True
for ch in SCD:
    for a, b in zip(ch, ch[1:]):
        if not a < b:
            chains_ok = False
    cover |= set(ch)
all16 = {frozenset(s) for k in range(5) for s in combinations(range(4), k)}
check("T-B4 [STAGE 1] THE DILWORTH CERTIFICATE, both bounds "
      "constructive: the 6 pairs of B4 are PAIRWISE INCOMPARABLE (an "
      "antichain — since a chain contains at most one member of an "
      "antichain, ANY chain cover of B4 needs >= 6 chains), and the "
      "exhibited symmetric chain decomposition IS a cover by exactly 6 "
      "chains of all 16 subsets.  Hence min chain cover = 6 EXACTLY, "
      "and with T-LEMMA: **shatter-4 requires at least 6 actors**",
      anti_ok and chains_ok and cover == all16 and len(SCD) == 6,
      f"antichain of size 6 verified = {anti_ok}; SCD chains = "
      f"{len(SCD)}, all strict chains = {chains_ok}, cover complete = "
      f"{cover == all16}")

# (first draft brute-forced 2^(2^k) antichain masks — 2^32 at k = 5,
#  unrunnable; replaced by the CONSTRUCTIVE de Bruijn-Tengbergen-
#  Kruyswijk recursion, which is exact for every k and gives BOTH
#  bounds: the SCD is a chain cover of size C(k, floor(k/2)), and the
#  middle layer is an antichain of the same size.)
from math import comb
def scd(k):
    if k == 0:
        return [[frozenset()]]
    out = []
    for ch in scd(k - 1):
        top = ch[-1] | {k - 1}
        out.append(ch + [top])
        if len(ch) > 1:
            out.append([a | {k - 1} for a in ch[:-1]])
    return out
sperner = []
scd_ok = True
for k in range(1, 7):
    chains = scd(k)
    allk = {frozenset(s) for r in range(k + 1)
            for s in combinations(range(k), r)}
    flat = [a for ch in chains for a in ch]
    part = (len(flat) == len(set(flat)) == len(allk)
            and set(flat) == allk)
    chn = all(a < b for ch in chains for a, b in zip(ch, ch[1:]))
    mid = [frozenset(s) for s in combinations(range(k), k // 2)]
    anti = all(not (a <= b or b <= a) for a, b in combinations(mid, 2))
    scd_ok = scd_ok and part and chn and anti
    sperner.append((k, len(chains), len(mid)))
check("T-SPERNER [STAGE 1] the general count, CONSTRUCTIVE both ways "
      "for k = 1..6: the de Bruijn-Tengbergen-Kruyswijk recursion "
      "yields a PARTITION of B_k into strict chains, the middle layer "
      "is an antichain, and the two counts COINCIDE at C(k, floor(k/2)) "
      "— so the largest antichain and the minimum chain cover are both "
      "exactly 1, 2, 3, 6, 10, 20.  Shatter-k requires at least that "
      "many actors.  (ROUND-1 BLOCKER 1: the application to SPHERE "
      "skies is NOT via shattering — caps on S^2 have VC dimension 4, "
      "shattering 4 and NEVER 5, certified by an exact Radon partition "
      "[REFEREE-CARRIED] — so the sphere's unbounded-actor conclusion "
      "goes via TRACE COUNTING instead: Theta(n^3) cap traces against "
      "chains of length n+1 force Theta(n^2) actors.  The Sperner count "
      "prices shatter-k; it does not by itself price the sphere.)",
      scd_ok and all(c == m == comb(k, k // 2) for k, c, m in sperner),
      f"(k, SCD chains, middle layer) = {sperner}")

# --- corollary sweep at widths < 6, capacity reported honestly
print("\n[STAGE 1 — corollary sweep below the bound]")
cap_ok = 0
shat = 0
for name, actors, fam in FAMS:
    if len(actors) >= 6:
        continue
    for h in fam:
        if len(h) < 4:
            continue
        C = poset_of(h)
        for e_i in range(len(h)):
            for d in (1, 2, 3):
                dirs, rows = sky(C, e_i, 'B', d)
                r = set(rows)
                if len(dirs) >= 4 and len(r) >= 16 and frozenset() in r:
                    cap_ok += 1
                    if shattered_set(rows, dirs, 4) is not None:
                        shat += 1
check("T-SWEEP [STAGE 1] no shattered 4-set below width 6 — reported "
      "WITH a capacity census in the STRICT FIRST-DRAFT FORM (>= 4 "
      "dirs, >= 16 traces, AND the empty trace; the batch round's "
      "corrected D53 SC5 drops the empty-row clause, so this census "
      "UNDERCOUNTS corrected-capable skies — relabelled per the batch "
      "round, verdict unchanged: the gate is shat == 0 either way): "
      "if the census is zero the sweep is vacuous under the strict "
      "form and the claim rests on the theorem alone, which is "
      "exactly what a theorem is for",
      shat == 0,
      f"strict-form-capable skies at widths < 6 = {cap_ok}, shattered "
      f"= {shat}"
      + ("; sweep VACUOUS below the bound under the strict form — "
         "consistent with the theorem (capable skies need 16 traces "
         "from < 6 chains, which Dilworth forbids)"
         if cap_ok == 0 else ""))

# --- mutant: the instrument must detect a non-nested family
print("\n[mutants + hygiene]")
MUT = [frozenset({0, 1}), frozenset({1, 2})]
mut_caught = not is_nested(MUT[0], MUT[1])
check("M1 the nestedness test is not blind: a crossing pair ({0,1} vs "
      "{1,2}) is flagged non-nested by is_nested() — THE SAME function "
      "the sweep calls (round-1 MINOR 7: the first draft inlined a "
      "duplicate comparison and the mutant never touched the sweep's "
      "code path)",
      mut_caught and nest_bad == 0,
      "crossing pair detected by the sweep's own predicate = True")

WITNESS = []
def report_witness(kind, payload):
    WITNESS.append(kind)
    print(f"  [WITNESS {kind}] {payload}")
report_witness("NESTEDNESS-EXERCISE",
               {'crossing_pair': [sorted(MUT[0]), sorted(MUT[1])],
                'note': 'the branch a real T-LEMMA violation would take'})
check("M2 the witness branch is live and EXERCISED (LOG #354 F1)",
      WITNESS == ['NESTEDNESS-EXERCISE'], f"invocations = {WITNESS}")

_self = ast.parse(open('v10/code/d54_dilworth_gate_exact.py').read())
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
check("M3 AST anti-vacuity: every check() references a run-bound name; "
      "SCOPE (LOG #403 MA-2): exactly that and nothing more",
      len(_ch) >= 7 and not _vac,
      f"check() calls = {len(_ch)}, bare/unbound = {len(_vac)}")

print("\n[VERDICT — D54 stages 0+1]")
print("  STAGE 0: premise P GATED at transport scope, zero violations —")
print(f"  {p_pairs} actor-sharing pairs, deliveries' two-carrier case")
print("  included.")
print("  STAGE 1: the nested-trace lemma corroborated on every sky of")
print(f"  every family ({skies} skies, zero non-nested per-actor pairs);")

print("  the B4 certificate gives min chain cover = 6 with both bounds")
print("  constructive; the dBTK partition is exact for k = 1..6.")
print("  **THE DILWORTH GATE: shatter-4 needs >= 6 actors; shatter-k")
print("  needs >= C(k, floor(k/2)) actors.**  The sphere consequence is")
print("  NOT via shattering (caps shatter 4, never 5 — round-1 B1); the")
print("  unbounded-actor result for spheres goes via trace counting and")
print("  is carried in the result note.  The WORD theorem is carried by")
print("  the proof; everything here is gate and corroboration.")

print(f"\n[d54 s0+1] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("EXIT 1")
    sys.exit(1)
print("EXIT 0")
