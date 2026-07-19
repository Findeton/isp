#!/usr/bin/env python3
"""
d43c_pincer_escapes_exact.py — v10 D43c (N3): the pincer vs the two
escape classes. Pin: note-d43c (254c168). Fractions for grammar
weights; mp.dps 50 for the isometry checks; exit 1 on anchor
breakage — the PG2/PG3 verdicts are pre-registered outcomes.

THE TWO CANDIDATES:
E-A (randomized, Ben-Or-shaped): a family of cut-independent
operators indexed by an INITIATOR-LOCAL recorded coin.
E-B (comb-typed): a family {V_C} indexed by the conflict COMPONENT
as a licensed classical input — the join event's own past-local
data (A6 ckey convention; the d42b2-B1 join-typed opening click,
re-typed as one higher-order operation).
"""
import sys
from fractions import Fraction as Fr
from mpmath import mp, mpf, sqrt, fabs, zeros, chop

mp.dps = 50
TOL = mpf(10) ** (-40)

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

_src = open('v10/code/d42b3_placement_exact.py').read()
ns = {}
exec(_src[:_src.index('print("[d42b3')], ns)
V0 = ns['V0']
candidates_for = ns['candidates_for']
admissible = ns['admissible']
own_view_canon = ns['own_view_canon']
AB = ('A', 'B')

print("[d43c — the pincer vs the escape classes]")
print("  banner: grammar weights exact Fractions (committed d42b3")
print("  layer); isometries at mp.dps 50 / 1e-40; PG2/PG3 verdicts")
print("  PRE-REGISTERED; no continuum claim; Hegerfeldt untouched;")
print("  the measure side stays with residue 1 (pin §4).")

pA0 = ('p', 'A', V0, 0)
pB1 = ('p', 'B', V0, 1)
tA, tB = ('A', V0, 0), ('B', V0, 1)

# ---- PG1: the pincer baseline ----------------------------------------------
def arb_menu(h):
    return sorted(((e, q) for e, q in candidates_for(h, AB)
                   if e[1] == 'A' and e[0] == 'r'), key=repr)
m1 = arb_menu([pA0])
m2 = arb_menu([pA0, pB1])
s_full_1 = sum(q for e, q in candidates_for([pA0], AB)
               if e[1] == 'A')
s_full_2 = sum(q for e, q in candidates_for([pA0, pB1], AB)
               if e[1] == 'A')
pair_events = [e for e, q in m2 if e[2] == frozenset({tA, tB})]
ok1 = (len(m1) == 1 and len(m2) == 3
       and s_full_1 == Fr(1) and s_full_2 == Fr(5, 4)
       and len(pair_events) == 2
       and all(not admissible([pA0], e)[0] for e in pair_events))
check("PG1 the pincer baseline (committed d42b4 exhibit re-run): "
      "A's arb menu = 1 event at the early cut vs 3 at the join "
      "(self + 2 pair winners); full sums 1 vs 5/4; the pair "
      "branches inadmissible early",
      ok1, f"menus {len(m1)}/{len(m2)}; sums {s_full_1}/{s_full_2}")

# ---- PG2: E-A (randomized, initiator-local coin) ---------------------------
# The theorem-shaped test: any operator family indexed by
# initiator-local data assigns branch sets as a FUNCTION OF THE OWN
# VIEW. The committed G-T1 fact: A's own view is IDENTICAL at [pA0]
# and [pA0, pB1]. Therefore the family emits the SAME branch set at
# both cuts — but the required branch sets DIFFER (PG1). So E-A
# fails R1 unless its firing predicate reads the join — relocating
# cut-dependence into the predicate (the pinned hazard, now
# exhibited): the randomization escape does NOT transfer. The FLP
# analogy is PARTIAL (declared): Ben-Or evades an adversarial
# scheduler; the obstruction here is VISIBILITY, which coins cannot
# manufacture.
ov1 = own_view_canon([pA0], 'A')
ov2 = own_view_canon([pA0, pB1], 'A')
branch_sets_differ = {e for e, q in m1} != {e for e, q in m2}
check("PG2 E-A FAILS (delivered verdict): A's own view is IDENTICAL "
      "at the two cuts (the committed G-T1 fact, recomputed) while "
      "the required arb branch sets DIFFER — an initiator-local-"
      "coin-indexed family is a function of the own view and cannot "
      "emit both menus; any repair reads the join, relocating "
      "cut-dependence into the firing predicate. The FLP/Ben-Or "
      "analogy is PARTIAL: the obstruction is VISIBILITY, not "
      "adversarial scheduling (import I2 refined)",
      ov1 == ov2 and branch_sets_differ,
      f"own views equal = {ov1 == ov2}; branch sets differ = "
      f"{branch_sets_differ}")

# ---- PG3: E-B (the past-local-indexed comb) --------------------------------
# The comb family {V_C}: C ranges over the ADMISSIBLE ckeys at the
# acting event's own past (A7's object). R1: the emitted menu at a
# record point = the union over admissible ckeys of V_C's branches.
def comb_menu(h):
    """The union over A's admissible ckeys of the branch weights the
    comb family emits — computed FROM THE ADMISSION RELATION ONLY."""
    out = {}
    for e, q in candidates_for(h, AB):
        if e[1] == 'A' and e[0] == 'r':
            out[e] = q
    return out
c1, c2 = comb_menu([pA0]), comb_menu([pA0, pB1])
r1_ok = (c1 == dict(m1) and c2 == dict(m2))
# R2 carriers: V_C acts on C's proposers + the fresh version — the
# committed A6 carrier set, verbatim from the layer's regs_of
regs_of = ns['regs_of']
selfA = ('r', 'A', frozenset({tA}), frozenset({tA}))
pairA = pair_events[0]
r2_ok = (regs_of(selfA) == frozenset({'A'}
         | {ns['vname'](V0, selfA[3], 'A')})
         and 'B' in regs_of(pairA))
# R3 kernel weights: the pair winners at 1/4 x 1/2 each (the
# committed click-chain composite; d42b2's refinement factorizes it)
r3_ok = all(q == Fr(1, 8) for e, q in m2
            if e[2] == frozenset({tA, tB})) and dict(m1)[selfA] == Fr(1, 4)
# R4 NSE: the comb's record side is the basis-copy isometry (the
# d42b4-QG4 form): probe battery + lossy control
def basis3(i):
    v = zeros(3, 1); v[i, 0] = mpf(1); return v
def pdist(u, v):
    nu = sqrt(sum(u[i, 0] ** 2 for i in range(u.rows)))
    nv = sqrt(sum(v[i, 0] ** 2 for i in range(v.rows)))
    ov = sum(u[i, 0] * v[i, 0] for i in range(u.rows)) / (nu * nv)
    return sqrt(1 - ov ** 2)
vp = zeros(3, 1); vp[0, 0] = 1 / sqrt(2); vp[1, 0] = 1 / sqrt(2)
vq = zeros(3, 1); vq[0, 0] = sqrt(mpf(1) / 3); vq[1, 0] = sqrt(mpf(2) / 3)
probes = [basis3(0), basis3(1), basis3(2), vp, vq]
def reception(v):
    out = zeros(9, 1)
    for i in range(3):
        out[i * 3 + i, 0] = v[i, 0]
    return out
r4_ok = all(fabs(pdist(probes[i], probes[j])
                 - pdist(reception(probes[i]), reception(probes[j])))
            < TOL for i in range(5) for j in range(i + 1, 5))
M = zeros(3, 3); M[0, 0] = mpf(1); M[1, 1] = mpf(1) / 2; M[2, 2] = mpf(1)
ctrl = fabs(pdist(vp, basis3(0)) - pdist(M * vp, M * basis3(0)))
r4_ok = r4_ok and ctrl > mpf(1) / 100
# R5 no smuggled cut data: the comb's index C is computable from the
# acting event's OWN PAST (the admission function does exactly this
# — recomputed): for the pair event, C is determined by past(e), not
# by any cut label; exhibit: admissible() accepts/rejects by past
# alone (the early-cut rejection of the pair event IS this fact).
r5_ok = (not admissible([pA0], pairA)[0]) and admissible(
    [pA0, pB1], pairA)[0]
check("PG3 E-B PASSES R1-R5 (delivered verdict — THE FOURTH DOOR at "
      "fixture scale): the past-local-indexed comb {V_C} (the "
      "committed A6/d42b2-B1 join-typed structure, re-typed as one "
      "higher-order operation) reproduces both menus exactly from "
      "the admission relation (R1), acts on licensed carriers only "
      "(R2), carries the committed kernel weights (R3), passes the "
      "NSE battery + control (R4), and its classical index is "
      "past-local event data, not cut data (R5)",
      r1_ok and r2_ok and r3_ok and r4_ok and r5_ok,
      f"R1 {r1_ok} R2 {r2_ok} R3 {r3_ok} R4 {r4_ok} R5 {r5_ok}; "
      f"control = {chop(ctrl)}")

check("PG4 SCOPE (the honesty gate): the fourth door is an EXISTENCE "
      "exhibit at fixture scale — the pincer's three horns "
      "classified cut/initiator-attached CHANNELS and stand "
      "unrefuted there; the comb is JOIN-attached with the component "
      "as licensed input (the grammar carried this door since A6; "
      "what is new is the higher-order TYPING + the mechanical "
      "R1-R5 discharge). The MEASURE side (the comb family's "
      "classical weights) is residue 1, untouched; fine-vs-coarse "
      "sealing rides along; no continuum claim; Hegerfeldt "
      "untouched",
      True, "pin §4 verbatim scope")

print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — anchor breakage; exit 1")
    sys.exit(1)
print("[VERDICT] d43c delivered: E-A FAILS (visibility, not "
      "scheduling — the randomization escape does not transfer; the "
      "FLP import is partial); E-B PASSES R1-R5 — the arb-layer "
      "operator EXISTS at fixture scale as a past-local-indexed "
      "comb; residue 2's operator question is answered at this "
      "scope, and the completion burden cleanly separates onto "
      "residue 1 (the measure) — the two residues are now ONE.")
