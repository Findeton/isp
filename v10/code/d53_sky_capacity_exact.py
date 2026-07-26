#!/usr/bin/env python3
"""
d53_sky_capacity_exact.py — v10 D53: D47's capacity condition was NOT
sufficient — and the FIRST CORRECTION OF IT WAS ALSO WRONG.

**ROUND-1 REVIEWED AND REPAIRED (2026-07-26).**  Independent hostile
review `v10/reviews/batch-round1-d50-to-d60.md` — REVISE, 1 BLOCKER /
2 MAJOR / 3 MINOR / 2 NIT.  Every number in the audit reproduced exactly
and the strata really are D47's; what did not survive is the sentence the
unit was named for.  Corrections carried below, each named where it lands:

  * BLOCKER 1 — the "empty trace" necessity theorem is FALSE.  Shattering
    a k-set S requires a row DISJOINT FROM S, i.e. the empty trace ON S;
    that coincides with an empty ROW only when S is the whole direction
    set.  SKY-A and SKY-C DO shatter, including on genuine Minkowski
    records.  SC1 restated to the true condition, SC3 REVERSED, witnesses
    printed (SC3 was the gate carrying the false claim).
  * MAJOR 1 — SC5 was not a necessary condition and false-negatived.  The
    empty-trace clause is REMOVED from the corrected condition; the
    corrected census is 196 skies, not 52, and the reduction is 2.8x, not
    10.7x.
  * MAJOR 2 — "a TAUTOLOGY, not a measurement" was overstated: 144 of the
    415 were genuinely capable.  The vacuous count is 271, not 415.
  * MINOR 1 — the surviving lemma needs TWO hypotheses the first draft
    never stated (the reflexive `c == f` clause in d47a's own trace
    definition, and TRANSITIVITY of the order).  Both are now exhibited
    by counterexample.
  * MINOR 2 / NIT 1 — SC1 and SC5 were theorem-passes and the structural
    claim was gated by nothing; the structural claim is now the content of
    SC1b and SC3 and both are falsifiable.  SC4's predicate now tests its
    own label.
  * MINOR 3 — d47b TG3/TG4 belong on the damage list and are added.
  * NIT 2 — `capable(...)` generic in k made the false clause look like a
    general law; the k = |dirs| special case, where the clause IS correct,
    is now its own named function.

WHAT THE UNIT STILL DELIVERS.  D47's capacity gate (|directions| >= 4 and
|rows| >= 2) is necessary and NOT sufficient: shatter-4 needs 16 DISTINCT
traces on the 4-set.  That correction stands, it is what makes 358 of
D47's 554 decidable pairs vacuous, and it binds on every future sky unit.

Exit 1 only on anchor breakage.  Run from the repo root.
"""
import ast
import sys
from collections import defaultdict
from fractions import Fraction as Fr
from itertools import combinations, permutations, product

sys.setrecursionlimit(200000)

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

print("[D53 — the sky instrument's capacity condition, ROUND-1 REPAIRED]")
print("  banner: shatter-k on a set S requires all 2^k traces ON S, and")
print("  the empty one among them is a row DISJOINT FROM S — NOT an")
print("  empty row.  Round 1 refuted the first draft's identification of")
print("  the two: SKY-A and SKY-C shatter, and witnesses are printed")
print("  below on a finite poset, on genuine M^{3+1}, and on D47's own")
print("  M^{2+1} records.  D47's capacity gate is still not sufficient;")
print("  the corrected necessary condition drops the empty-trace clause.")

# ------------------------------------------------------------------ SC0
print("\n[SC0 anchor — the instrument, imported from committed D47a]")
_D47A = 'v10/code/d47a_sky_instrument_exact.py'
_src = open(_D47A).read()
_t = ast.parse(_src)
_keep = [n for n in _t.body
         if isinstance(n, ast.FunctionDef)
         or (isinstance(n, ast.Assign)
             and any(isinstance(x, ast.Name)
                     and x.id in ('CYCLIC_CAP', 'SKYB_DEPTH')
                     for x in n.targets))]
g = {'Fr': Fr, 'combinations': combinations,
     'permutations': permutations, 'product': product}
exec(compile(ast.fix_missing_locations(ast.Module(body=_keep,
                                                  type_ignores=[])),
             'd47a_extract', 'exec'), g)
sky = g['sky']
mink_order = g['mink_order']
lattice_points = g['lattice_points']
shattered_set = g['shattered_set']
arc_system = g['arc_system']

# The 3+1 sprinkling.  ROUND-1 REPAIR: its generator is the one D58's
# BLOCKER 1 corrected (high-bit LCG draw; the committed low-bit draw
# collapsed to 32 distinct points at box = 32).  Single source: the
# repaired d55c, extracted the same way.
_D55C = 'v10/code/d55c_m31_control_exact.py'
_t5 = ast.parse(open(_D55C).read())
_k5 = [n for n in _t5.body if isinstance(n, ast.FunctionDef)]
g5 = {'Fr': Fr, 'combinations': combinations,
      'permutations': permutations, 'product': product}
exec(compile(ast.fix_missing_locations(ast.Module(body=_k5,
                                                  type_ignores=[])),
             'd55c_extract', 'exec'), g5)
mink4, latt4 = g5['mink4'], g5['latt4']

check("SC0 the sky constructor and the shatter test are imported from "
      "the committed D47a receipt by AST extraction — the object under "
      "audit is D47's own, not a re-implementation — and the M^{3+1} "
      "generator from the ROUND-1 REPAIRED d55c (single source for the "
      "generator fix)",
      all(callable(f) for f in (sky, mink_order, shattered_set,
                                mink4, latt4)),
      f"sources = {_D47A}, {_D55C}")

# ------------------------------------------------------------------ SC1
print("\n[SC1 THE NECESSARY CONDITION — RESTATED BY ROUND 1]")
print("  The first draft asserted: 'a system with no empty trace cannot")
print("  shatter ANY set, for any k >= 1.'  **THAT IS FALSE.**  Shattering")
print("  S needs a row r with r & S = {} — a row DISJOINT FROM S, not an")
print("  empty row.  The two coincide only when S is the entire direction")
print("  set.  d47a's own shattered_set decides the counterexample:")
_cx_rows = [frozenset({0}), frozenset({1})]
_cx_shat = shattered_set(_cx_rows, [0, 1], 1)
print(f"    rows = [{{0}}, {{1}}]  cols = [0, 1]   empty ROW present = "
      f"{frozenset() in set(_cx_rows)}")
print(f"    d47a shattered_set(rows, [0,1], 1) = {_cx_shat}   <- a "
      f"shattered 1-set, with no empty row anywhere")
_rows6, _cols6 = arc_system(6)
_has_empty_arc = frozenset() in set(_rows6)
_caps = [frozenset(s) for k in range(5) for s in combinations(range(4), k)]
_has_empty_cap = frozenset() in set(_caps)
check("SC1 THE TRUE NECESSARY CONDITION.  Shattering a k-set S requires "
      "all 2^k traces ON S; the empty one is a row DISJOINT FROM S.  The "
      "first draft read that as 'the system contains the empty row' and "
      "concluded that a system without one can never shatter — REFUTED "
      "HERE by d47a's own decider on a two-row system with no empty row. "
      "The empty-ROW reading is correct only at k = |dirs| (SC1b).  Both "
      "of D47's synthetic validation systems do contain the empty row, "
      "which is why the instrument's own validation could not see this",
      _cx_shat is not None
      and frozenset() not in set(_cx_rows)
      and _has_empty_arc and _has_empty_cap
      and shattered_set(_caps, range(4), 4) is not None,
      f"counterexample shatters {_cx_shat} with empty row = "
      f"{frozenset() in set(_cx_rows)}; arc system contains empty row = "
      f"{_has_empty_arc}; cap system contains empty row = {_has_empty_cap}"
      f"; cap system shatters 4 = "
      f"{shattered_set(_caps, range(4), 4) is not None}")

# ------------------------------------------------------------------ SC1b
print("\n[SC1b WHAT SURVIVES — the true lemma, with the two hypotheses "
      "the first draft never stated]")
print("  LEMMA.  Let C be a FINITE TRANSITIVE strict order.  Then every")
print("  SKY-A and SKY-C row is NON-EMPTY, because d47a writes the trace")
print("  of f as {c in dirs : c == f or C[c][f]} — the REFLEXIVE clause")
print("  `c == f` is load-bearing (a cover lies above no cover, so the")
print("  first draft's stated reason is false for the covers themselves),")
print("  and transitivity is what carries a non-cover f down to a cover.")
print("  CONSEQUENCE, and it is ALL the empty-row argument buys: a SKY-A")
print("  or SKY-C sky can never shatter its FULL direction set (k =")
print("  |dirs|).  It says NOTHING about proper subsets.")


def poset_21():
    """base e = 0; five covers c1..c5 = 1..5; one event above each
    non-empty T subset of {c1..c4}.  21 events, transitive."""
    covers = [1, 2, 3, 4, 5]
    tops = []
    for k in range(1, 5):
        for T in combinations([1, 2, 3, 4], k):
            tops.append(set(T))
    n = 1 + len(covers) + len(tops)
    C = [[False] * n for _ in range(n)]
    for c in covers:
        C[0][c] = True
    for idx, T in enumerate(tops):
        f = 6 + idx
        C[0][f] = True
        for c in T:
            C[c][f] = True
    return C


C21 = poset_21()
_tri_ok = all(not (C21[i][j] and C21[j][k2] and not C21[i][k2])
              for i in range(21) for j in range(21) for k2 in range(21))
d21, r21 = sky(C21, 0, 'A')
r21s = set(r21)
w21 = shattered_set(r21, d21, 4)


def sky_A_no_reflexive(C, e):
    """d47a's SKY-A with the reflexive `c == f` clause REMOVED — the
    first draft's stated reason, coded literally."""
    n = len(C)
    fut = [f for f in range(n) if C[e][f]]
    dirs = [c for c in fut if not any(C[e][k] and C[k][c] for k in range(n))]
    rows = {frozenset(c for c in dirs if C[c][f]) for f in fut}
    return dirs, sorted(rows, key=lambda s: (len(s), sorted(s)))


_dnr, _rnr = sky_A_no_reflexive(C21, 0)
_empty_without_reflexive = frozenset() in set(_rnr)

# a non-transitive acyclic order: 0<1, 0<2, 0<3, 1<2, 2<3, NOT 1<3
CNT = [[False] * 4 for _ in range(4)]
for (i, j) in ((0, 1), (0, 2), (0, 3), (1, 2), (2, 3)):
    CNT[i][j] = True
_dnt, _rnt = sky(CNT, 0, 'A')
_empty_nontransitive = frozenset() in set(_rnt)

print(f"  the 21-event poset: transitive = {_tri_ok}, SKY-A |dirs| = "
      f"{len(d21)}, |rows| = {len(r21s)}, EMPTY ROW PRESENT = "
      f"{frozenset() in r21s}")
print(f"  hypothesis 1 (reflexivity): the SAME poset with the `c == f` "
      f"clause removed has an empty row = {_empty_without_reflexive}")
print(f"  hypothesis 2 (transitivity): on 0<1,0<2,0<3,1<2,2<3 (NOT 1<3), "
      f"d47a SKY-A dirs = {_dnt}, rows = {[sorted(x) for x in _rnt]}, "
      f"EMPTY ROW = {_empty_nontransitive}")
FULLSET_SAFE = True
FULLSET_TESTED = 0
for N in (40, 80, 160):
    _C = mink_order(lattice_points(N))
    for e in range(N):
        for kind in ('A', 'C'):
            dirs, rows = sky(_C, e, kind)
            if len(dirs) < 1:
                continue
            FULLSET_TESTED += 1
            if shattered_set(rows, dirs, len(dirs)) is not None:
                FULLSET_SAFE = False
check("SC1b THE SURVIVING LEMMA, with both hypotheses exhibited.  On a "
      "finite TRANSITIVE order every SKY-A/SKY-C row is non-empty — the "
      "reflexive `c == f` clause and transitivity are each load-bearing, "
      "and dropping either one produces an empty row (both counter-"
      "examples printed above).  Hence a SKY-A/SKY-C sky can never "
      "shatter its FULL direction set.  That is the WHOLE content of the "
      "empty-row argument; SC3 shows it does not extend to proper subsets",
      _tri_ok and frozenset() not in r21s
      and _empty_without_reflexive and _empty_nontransitive
      and FULLSET_SAFE and FULLSET_TESTED > 0,
      f"21-event poset transitive = {_tri_ok}, empty row = "
      f"{frozenset() in r21s}; empty row without reflexivity = "
      f"{_empty_without_reflexive}; empty row without transitivity = "
      f"{_empty_nontransitive}; full-direction-set shatterings over "
      f"{FULLSET_TESTED} SKY-A/SKY-C skies on D47's own records = 0")

# ------------------------------------------------------------------ SC2
print("\n[SC2 the audit of D47's OWN strata, with the CORRECTED "
      "condition]")


def capable(dirs, rows, k=4):
    """CORRECTED BY ROUND 1 (MAJOR 1).  A sky can possibly shatter SOME
    k-set only if it has >= k directions AND >= 2^k distinct traces.  The
    first draft's third clause — 'and the empty trace is among them' —
    is NOT necessary and false-negatived 144 genuinely capable skies."""
    return len(dirs) >= k and len(set(rows)) >= (1 << k)


def can_shatter_full_set(dirs, rows):
    """The k = |dirs| special case, where the empty-ROW clause IS the
    right one (SC1b).  Kept separate so the correct special case cannot
    be mistaken for a general law again (round-1 NIT 2)."""
    return frozenset() in set(rows)


def best_trace_count(dirs, rows, k=4):
    """max over k-subsets S of |{r & S : r in rows}| — the capacity
    diagnostic: how far the sky got toward the 2^k it needs."""
    R = [frozenset(r) for r in rows]
    best = 0
    for sub in combinations(sorted(dirs), k):
        S = set(sub)
        best = max(best, len({frozenset(r & S) for r in R}))
    return best


ST = defaultdict(lambda: [0, 0, 0, 0])   # skies, w/empty ROW, d47-dec, capable
D47_DEC = []                             # (kind, dirs, rows) per decidable sky
for N in (40, 80, 160):
    C = mink_order(lattice_points(N))
    for e in range(N):
        for kind in ('A', 'B', 'C'):
            dirs, rows = sky(C, e, kind)
            if not dirs:
                continue
            r = set(rows)
            emp = frozenset() in r
            ST[kind][0] += 1
            if emp:
                ST[kind][1] += 1
            if len(dirs) >= 4 and len(r) >= 2:
                ST[kind][2] += 1
                D47_DEC.append((kind, tuple(dirs), tuple(rows), emp))
                if capable(dirs, rows, 4):
                    ST[kind][3] += 1
for k in ('A', 'B', 'C'):
    s, we, d, cp = ST[k]
    print(f"  SKY-{k}: skies {s:4d}, with empty ROW {we:4d}, "
          f"D47-'decidable' {d:4d}, CORRECTED-CAPABLE {cp:4d}")
tot_dec = sum(ST[k][2] for k in 'ABC')
tot_cap = sum(ST[k][3] for k in 'ABC')
check("SC2 A LARGE PART OF D47's DECIDABLE STRATUM WAS STRUCTURALLY "
      "INCAPABLE OF FIRING — and this, the unit's durable content, is "
      "unaffected by round 1.  Of the pairs D47 counted as shatter-4 "
      f"decidable, only {tot_cap} of {tot_dec} carry the 16 DISTINCT "
      "traces a shattered 4-set needs; over the rest D47's 'zero "
      "shatterings' is a tautology.  (The count is now the CORRECTED "
      "one: the first draft's 52 came from a third clause round 1 "
      "refuted)",
      tot_cap < tot_dec and tot_dec > 0 and tot_cap > 0,
      f"D47-decidable = {tot_dec}, corrected-capable = {tot_cap}, "
      f"vacuous = {tot_dec - tot_cap}")

# ------------------------------------------------------------------ SC2b
print("\n[SC2b MAJOR 2 — how much of the 'incapable' stratum was really "
      "incapable?]")
no_empty = [x for x in D47_DEC if not x[3]]
ne_wide = [x for x in no_empty if len(x[1]) >= 5]
ne_cap = [x for x in no_empty if capable(x[1], x[2], 4)]
best_over_ne = max((best_trace_count(d, r, 4) for _, d, r, _ in ne_cap),
                   default=0)
best_over_all = max((best_trace_count(d, r, 4) for _, d, r, _ in D47_DEC),
                    default=0)
print(f"  D47-decidable                                        = "
      f"{len(D47_DEC)}")
print(f"  without the empty ROW ('structurally incapable')      = "
      f"{len(no_empty)}")
print(f"    ... of which |dirs| >= 5 (the empty-row argument gives NO")
print(f"        obstruction on any 4-subset at all)             = "
      f"{len(ne_wide)}")
print(f"    ... of which >= 16 distinct traces (the CORRECTED")
print(f"        necessary condition is satisfied)               = "
      f"{len(ne_cap)}")
print(f"  best |{{r & S}}| over any 4-set, all three kinds        = "
      f"{best_over_all} of 16")
check("SC2b 'A TAUTOLOGY, NOT A MEASUREMENT' WAS OVERSTATED — corrected "
      f"by round 1 (MAJOR 2).  {len(ne_cap)} of the {len(no_empty)} skies "
      "the first draft called structurally incapable pass the CORRECTED "
      f"necessary condition and reach {best_over_ne} of the 16 required "
      "traces on their best 4-set: D47's zero over them is a real "
      f"measurement.  Inside the stratum the first draft wrote off, the "
      f"genuinely vacuous count is {len(no_empty) - len(ne_cap)}, not "
      f"{len(no_empty)} — and {tot_dec - tot_cap} of the {tot_dec} "
      f"decidable pairs overall",
      len(ne_cap) > 0 and len(ne_wide) > len(ne_cap)
      and best_over_ne > 1,
      f"empty-row-free = {len(no_empty)}, of which |dirs|>=5 = "
      f"{len(ne_wide)}, corrected-capable = {len(ne_cap)}, genuinely "
      f"vacuous inside that stratum = {len(no_empty) - len(ne_cap)}, "
      f"best trace count over the capable ones = {best_over_ne}/16")

# ------------------------------------------------------------------ SC3
print("\n[SC3 RESIDUE 2 — the first draft's answer is REVERSED by round 1]")
print("  The first draft printed, as an unconditional structural reason,")
print("  that SKY-A and SKY-C 'can NEVER shatter, at any width or depth'.")
print("  Three independent witness families refute it:")
print(f"  (1) FINITE POSET.  The 21-event transitive poset above: "
      f"SKY-A |dirs| = {len(d21)}, |rows| = {len(r21s)}, empty row = "
      f"{frozenset() in r21s}, SHATTERED 4-SET = {w21}")
if w21:
    _S = set(w21)
    print(f"      the 16 traces on it: "
          f"{sorted([sorted(x) for x in {frozenset(r & _S) for r in r21}], key=lambda z: (len(z), z))}")
    print(f"      MECHANISM: c5's own row {{c5}} is non-empty as a ROW and "
          f"DISJOINT from the 4-set — it supplies the empty trace ON S. "
          f"Available at every width >= 5.")
# (2) the dual: SKY-C on the reversed order is SKY-A on the original
C21R = [[C21[j][i] for j in range(21)] for i in range(21)]
d21c, r21c = sky(C21R, 0, 'C')
w21c = shattered_set(r21c, d21c, 4)
print(f"  (2) THE DUAL.  SKY-C on the reversed 21-event poset: |dirs| = "
      f"{len(d21c)}, empty row = {frozenset() in set(r21c)}, SHATTERED "
      f"4-SET = {w21c}")

# (3) genuine Minkowski M^{3+1}
M31_N, M31_BOX, M31_T, M31_SEED = 300, 30, 120, 11
P31 = latt4(M31_N, M31_BOX, M31_SEED, M31_T)
C31 = mink4(P31)
_distinct31 = len(set(P31))
_tri31 = all(not (C31[i][j] and C31[j][k2] and not C31[i][k2])
             for i in range(0, M31_N, 7) for j in range(M31_N)
             for k2 in range(M31_N))
MINK_HITS = {'A': [], 'C': []}
for e in range(M31_N):
    for kind in ('A', 'C'):
        dirs, rows = sky(C31, e, kind)
        if not capable(dirs, rows, 4):
            continue
        w = shattered_set(rows, dirs, 4)
        if w is not None:
            MINK_HITS[kind].append((e, len(dirs), len(set(rows)), w))
print(f"  (3) GENUINE M^{{3+1}} (N = {M31_N}, T = {M31_T}, box = "
      f"{M31_BOX}, seed {M31_SEED}; {_distinct31}/{M31_N} distinct "
      f"points, order transitive on the sampled rows = {_tri31}):")
for kind in ('A', 'C'):
    hits = MINK_HITS[kind]
    print(f"      SKY-{kind}: shattered 4-sets at {len(hits)} base events"
          + (f"; witness e = {hits[0][0]} |dirs| = {hits[0][1]} |rows| = "
             f"{hits[0][2]} EMPTY ROW = "
             f"{frozenset() in set(sky(C31, hits[0][0], kind)[1])} "
             f"shattered 4-set = {hits[0][3]}" if hits else ""))
# (4) D53's own 2+1 records: SKY-C shatters 3-sets
c3_cap = c3_hit = 0
c3_wit = None
C160 = mink_order(lattice_points(160))
for e in range(160):
    dirs, rows = sky(C160, e, 'C')
    if not capable(dirs, rows, 3):
        continue
    c3_cap += 1
    w = shattered_set(rows, dirs, 3)
    if w is not None:
        c3_hit += 1
        if c3_wit is None:
            c3_wit = (e, len(dirs), len(set(rows)),
                      frozenset() in set(rows), w)
print(f"  (4) D53's OWN RECORDS.  SKY-C on d47a's lattice_points(160): "
      f"shattered 3-sets at {c3_hit} of {c3_cap} capable base events, "
      f"with ZERO empty rows anywhere; witness = {c3_wit}")
A_shatters = len(MINK_HITS['A']) > 0
C_shatters = len(MINK_HITS['C']) > 0 or c3_hit > 0
check("SC3 [CORRECTED BY ROUND 1 — THE FIRST DRAFT'S ANSWER IS REVERSED] "
      "**SKY-A AND SKY-C DO SHATTER.**  The claim 'they can NEVER "
      "shatter, at any width or depth' is refuted by four independent "
      "witness families printed above: a 21-event transitive poset, its "
      "dual, genuine M^{3+1} sprinklings, and D47's OWN M^{2+1} records "
      "one rung down (SKY-C shatters 3-sets there).  So D47 residue 2 is "
      "NOT answered by this unit: all three sky definitions remain in the "
      "field of view, and the programme's restriction to SKY-B was a "
      "blinder — which is exactly what made D55c miss its own "
      "discriminator",
      A_shatters and C_shatters and w21 is not None and w21c is not None,
      f"SKY-A shatter-4 on M^{{3+1}} at {len(MINK_HITS['A'])} events; "
      f"SKY-C at {len(MINK_HITS['C'])} events; SKY-C shatter-3 on the "
      f"2+1 records at {c3_hit}/{c3_cap}; finite-poset witnesses "
      f"{w21} (SKY-A) and {w21c} (SKY-C, dual)")

# ------------------------------------------------------------------ SC4
print("\n[SC4 what is NOT affected — damage list, CORRECTED]")
_arc_no4 = shattered_set(_rows6, _cols6, 4) is None
_arc_yes3 = shattered_set(_rows6, _cols6, 3) is not None
_cap_yes4 = shattered_set(_caps, range(4), 4) is not None
_synth_empty = _has_empty_arc and _has_empty_cap
check("SC4 THE DAMAGE IS BOUNDED AND STATED, and the list is CORRECTED "
      "by round 1 (MINOR 3).  UNTOUCHED: D47a's constructed separator "
      "(arcs shatter 3 and not 4, exact-rational caps shatter 4 — both "
      "re-decided in this process by the predicate below); its instrument "
      "validation on SYNTHETIC systems, which do contain the empty row; "
      "the DEMOTION of circular-ones, which never used shatter-4; and "
      "D47b's ACTOR-WIDTH result (TG2), a measurement of sky SIZE.  "
      "**ADDED BY ROUND 1: d47b TG3/TG4 ARE damaged** — they run the "
      "identical `|dirs| < 4 or |rows| < 2` gate over all three sky "
      "kinds on transport skies and report shattered 4-sets over exactly "
      "the stratum this unit calls vacuous; they must be re-run under "
      "SC5's corrected condition",
      _arc_no4 and _arc_yes3 and _cap_yes4 and _synth_empty,
      f"arcs shatter 4 = {not _arc_no4}, arcs shatter 3 = {_arc_yes3}, "
      f"caps shatter 4 = {_cap_yes4}, both synthetic systems carry the "
      f"empty row = {_synth_empty}")

# ------------------------------------------------------------------ SC5
print("\n[SC5 the corrected capacity condition — MAJOR 1 REPAIRED]")
strict = defaultdict(int)
for N in (40, 80, 160):
    C = mink_order(lattice_points(N))
    for e in range(N):
        for kind in ('A', 'B', 'C'):
            dirs, rows = sky(C, e, kind)
            if dirs and capable(dirs, rows, 4):
                strict[kind] += 1
tot_strict = sum(strict.values())
_old_clause = sum(1 for kind, d, r, emp in D47_DEC
                  if capable(d, r, 4) and emp)
for kind in ('A', 'B', 'C'):
    print(f"  SKY-{kind}: >= 4 dirs and >= 16 distinct traces: "
          f"{strict[kind]:3d}")
print(f"  corrected total = {tot_strict}; the first draft's "
      f"empty-row-gated total = {_old_clause}")
check("SC5 THE CORRECTED CONDITION — the third clause is GONE.  A sky "
      "can possibly shatter a 4-set only with >= 4 directions and >= 16 "
      "DISTINCT traces.  The first draft also demanded the empty ROW; "
      "round 1 showed that clause is NOT necessary (SC1) and it "
      f"false-negatived {tot_strict - _old_clause} genuinely capable "
      f"skies.  Applied to the same Minkowski records the corrected "
      f"condition admits {tot_strict} skies against D47's {tot_dec} — "
      "a reduction of "
      f"{tot_dec / max(tot_strict, 1):.1f}x, not the 10.7x first "
      "published.  Any future sky unit must gate THIS",
      tot_strict > _old_clause and tot_strict < tot_dec
      and strict['A'] > 0 and strict['C'] > 0,
      f"corrected-capable = {tot_strict} (A {strict['A']}, B "
      f"{strict['B']}, C {strict['C']}), D47 SG2-'decidable' = "
      f"{tot_dec}, reduction factor = {tot_dec / max(tot_strict, 1):.1f}x"
      f"; the withdrawn clause would have admitted {_old_clause}")

print("\n[VERDICT — D53, ROUND-1 REPAIRED]")
print("  WHAT STANDS.  D47's capacity gate was NECESSARY BUT NOT "
      f"SUFFICIENT: {tot_dec - tot_cap} of its {tot_dec} 'decidable' "
      "pairs lack the 16 distinct traces a shattered 4-set needs, so "
      "D47's zero over them is a tautology.  The corrected condition is "
      "SC5's and it binds on every future sky unit.")
print("  WHAT IS WITHDRAWN.  The empty-trace NECESSITY theorem; "
      "'SKY-A and SKY-C can never shatter'; 'residue 2 is answered, and "
      "negatively'; 'only SKY-B is usable'; and the book's [EXACT] label "
      "on the structural claim.  Shattering S needs a row DISJOINT FROM "
      "S; that is an empty ROW only at k = |dirs|.")
print("  WHAT SURVIVES OF THE EMPTY-ROW ARGUMENT.  Exactly SC1b: on a "
      "finite TRANSITIVE order (reflexive trace clause load-bearing) a "
      "SKY-A/SKY-C sky cannot shatter its FULL direction set.  D54's "
      "K9-A/K9-C [THEOREM-PASS] labels remain correct for the "
      "no-empty-row FACT they gate; D54's pin inherits the false reason "
      "and must be restated.")
print("  CONSEQUENCE FOR THE 3+1 PROGRAMME, REVERSED: the targeted "
      "attack must NOT be built on SKY-B alone.  SKY-A and SKY-C are "
      "live readings, and under SKY-A the M^{3+1} discriminator is "
      "SHARPER than under SKY-B (D55c, repaired in the same round).")
print("  CONSUMERS THAT MUST RE-RUN UNDER SC5's CORRECTED CONDITION: "
      "d54, d54b K6, d47b TG3/TG4, D55, d55c (repaired here).")

print(f"\n[d53] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("EXIT 1")
    sys.exit(1)
print("EXIT 0")
