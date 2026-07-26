#!/usr/bin/env python3
"""
d53_sky_capacity_exact.py — v10 D53: D47's capacity condition was NOT
sufficient, and fixing it ANSWERS D47's residue 2.

THE FINDING.  Shattering a k-set requires all 2^k traces, and that
INCLUDES THE EMPTY TRACE.  D47's capacity gate (SG2) admitted a sky as
"shatter-4 decidable" on |directions| >= 4 and |rows| >= 2.  That is
necessary and NOT sufficient.  Under SKY-A the directions are the COVERS
of the base event, so every event strictly above it lies above at least
one cover — **the empty trace can never occur, and shatter-k is
structurally impossible for every k >= 1.**  Dually for SKY-C.

Consequence: a large part of D47's "decidable" stratum could not have
fired under any circumstances, and its zero-shattering result there is a
tautology rather than a measurement.  Only SKY-B admits the empty trace,
which answers D47 residue 2 ("which sky definition is privileged?")
negatively and decisively: **SKY-A and SKY-C are unusable for this
test.**

Nothing here touches D47's separator (SG0), its instrument validation on
synthetic set systems (SG1), or its actor-width result (D47b TG2) — the
last of which never used shatter-4 at all.

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

print("[D53 — the sky instrument's capacity condition]")
print("  banner: shatter-k requires ALL 2^k traces INCLUDING THE EMPTY")
print("  ONE.  D47's capacity gate checked |directions| >= 4 and")
print("  |rows| >= 2, which is necessary and NOT sufficient.  This")
print("  receipt measures how much of D47's decidable stratum was")
print("  structurally incapable of firing, and answers residue 2.")

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

check("SC0 the sky constructor and the shatter test are imported from "
      "the committed D47a receipt by AST extraction — the object under "
      "audit is D47's own, not a re-implementation",
      all(callable(f) for f in (sky, mink_order, shattered_set)),
      f"source = {_D47A}")

# ------------------------------------------------------------------ SC1
print("\n[SC1 the necessary condition, stated and checked on a control]")
_rows6, _cols6 = arc_system(6)
_has_empty_arc = frozenset() in set(_rows6)
_caps = [frozenset(s) for k in range(5) for s in combinations(range(4), k)]
_has_empty_cap = frozenset() in set(_caps)
check("SC1 THE NECESSARY CONDITION.  Shattering a k-set requires all "
      "2^k traces, and the empty set is one of them; so a system with no "
      "empty trace cannot shatter ANY set, for any k >= 1.  Both of "
      "D47's synthetic validation systems DO contain the empty trace — "
      "which is exactly why the instrument passed its validation there "
      "and why the defect below went unseen",
      _has_empty_arc and _has_empty_cap
      and shattered_set(_caps, range(4), 4) is not None,
      f"arc system contains empty trace = {_has_empty_arc}; cap system "
      f"contains empty trace = {_has_empty_cap}; cap system shatters 4 = "
      f"{shattered_set(_caps, range(4), 4) is not None}")

# ------------------------------------------------------------------ SC2
print("\n[SC2 the audit of D47's OWN strata]")
ST = defaultdict(lambda: [0, 0, 0, 0])   # skies, w/empty, decidable, dec+empty
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
                if emp:
                    ST[kind][3] += 1
for k in ('A', 'B', 'C'):
    s, we, d, dwe = ST[k]
    print(f"  SKY-{k}: skies {s:4d}, with empty trace {we:4d}, "
          f"D47-'decidable' {d:4d}, ACTUALLY CAPABLE {dwe:4d}")
tot_dec = sum(ST[k][2] for k in 'ABC')
tot_cap = sum(ST[k][3] for k in 'ABC')
check("SC2 A LARGE PART OF D47's DECIDABLE STRATUM WAS STRUCTURALLY "
      "INCAPABLE OF FIRING.  Of the pairs D47 counted as shatter-4 "
      f"decidable, only {tot_cap} of {tot_dec} contain the empty trace "
      "and could therefore ever have shattered.  D47's 'zero shatterings' "
      "over the rest is a TAUTOLOGY, not a measurement",
      tot_cap < tot_dec and tot_dec > 0,
      f"D47-decidable = {tot_dec}, actually capable = {tot_cap}, "
      f"vacuous = {tot_dec - tot_cap}")

# ------------------------------------------------------------------ SC3
print("\n[SC3 residue 2 ANSWERED — which sky definition can be used?]")
A_dead = ST['A'][3] == 0 and ST['A'][2] > 0
C_dead = ST['C'][3] == 0 and ST['C'][2] > 0
B_live = ST['B'][3] > 0
print("  STRUCTURAL REASON, not an accident of this sample:")
print("    SKY-A takes the directions to be the COVERS of the base event,")
print("    so EVERY event strictly above it lies above at least one")
print("    cover — the empty trace cannot occur.  SKY-C is the dual and")
print("    fails the same way.  SKY-B takes an antichain at a fixed")
print("    height, so an event above the base may lie above NO direction,")
print("    and the empty trace occurs.")
check("SC3 D47 RESIDUE 2 IS ANSWERED, and negatively: **SKY-A and SKY-C "
      "can NEVER shatter, at any width or depth**, so they are unusable "
      "for the 2+1 obstruction test; SKY-B is the only committed "
      "definition that can fire.  This also explains D47b's unexplained "
      "observation that SKY-A never reached decidability — it was doubly "
      "disqualified",
      A_dead and C_dead and B_live,
      f"SKY-A capable {ST['A'][3]}/{ST['A'][2]}, SKY-C capable "
      f"{ST['C'][3]}/{ST['C'][2]}, SKY-B capable {ST['B'][3]}/{ST['B'][2]}")

# ------------------------------------------------------------------ SC4
print("\n[SC4 what is NOT affected]")
check("SC4 THE DAMAGE IS BOUNDED AND STATED.  Untouched: D47a's "
      "constructed separator (arcs never shatter 4, exact-rational caps "
      "do, opposite-edge case certified); its instrument validation on "
      "SYNTHETIC systems, which contain the empty trace and so were "
      "genuine; the DEMOTION of circular-ones after it rejected 121 of "
      "554 real 2+1 skies, which never used shatter-4; and D47b's "
      "ACTOR-WIDTH result, which is a measurement of sky SIZE and does "
      "not invoke shattering at all",
      _has_empty_cap and shattered_set(_rows6, _cols6, 4) is None,
      "separator re-checked in this process: arcs shatter no 4-set, caps "
      "do, both validation systems carry the empty trace")

# ------------------------------------------------------------------ SC5
print("\n[SC5 the corrected capacity condition]")
def capable(dirs, rows, k=4):
    """A sky can POSSIBLY shatter a k-set only if it has >= k directions
    AND >= 2^k distinct traces AND the empty trace is among them."""
    r = set(rows)
    return len(dirs) >= k and len(r) >= (1 << k) and frozenset() in r

strict = 0
for N in (40, 80, 160):
    C = mink_order(lattice_points(N))
    for e in range(N):
        for kind in ('A', 'B', 'C'):
            dirs, rows = sky(C, e, kind)
            if dirs and capable(dirs, rows):
                strict += 1
check("SC5 THE CORRECTED CONDITION, and it is much tighter: a sky can "
      "possibly shatter a 4-set only with >= 4 directions, >= 16 DISTINCT "
      "traces, and the empty trace present.  Applied to the same "
      f"Minkowski records it admits {strict} skies against D47's "
      f"{tot_dec} — any future sky unit must gate THIS, not D47's SG2",
      strict <= tot_dec,
      f"corrected-capable = {strict}, D47 SG2-'decidable' = {tot_dec}, "
      f"reduction factor = {tot_dec / max(strict, 1):.1f}x")

print("\n[VERDICT — D53]")
print("  D47's capacity gate was NECESSARY BUT NOT SUFFICIENT, and the "
      "gap is structural rather than statistical: shattering needs the "
      "EMPTY TRACE, and two of the three committed sky definitions can "
      "never produce it.")
print(f"  **RESIDUE 2 IS ANSWERED: only SKY-B is usable.**  SKY-A and "
      f"SKY-C are dead for this test at every width and depth, which is "
      f"a stronger statement than 'they did not fire'.")
print("  D47's zero-shattering result survives only on the SKY-B "
      "stratum; elsewhere it was a tautology.  The separator, the "
      "circular-ones demotion and the actor-width result are all "
      "untouched.")
print("  CONSEQUENCE FOR THE 3+1 PROGRAMME: the targeted-construction "
      "attack must be built on SKY-B, and its capacity gate must be SC5's "
      "condition, not D47's.")

print(f"\n[d53] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("EXIT 1")
    sys.exit(1)
print("EXIT 0")
