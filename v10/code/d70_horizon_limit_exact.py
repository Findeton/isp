#!/usr/bin/env python3
"""
d70_horizon_limit_exact.py — v10 D70: THE HORIZON LIMIT.  Is there a
measure at transport scope that needs no bounded abstraction?

PIN: v10/note-d70-horizon-limit-pin.md (STRICT, frozen and committed
BEFORE this file was written; it names this receipt path and the note
path before either existed).  Campaign: THE MEASURE CAMPAIGN, opened
at LOG #481, scoped by v10/note-d69-measure-campaign-scoping.md (route
R4, with R5 as its proof engine and R1+R2 as the HZ5 arm).

ROUND-1 REPAIRED, 2026-07-27.  This file is the ROUND-1 REPAIR of the
first delivery, against reviews/d70-round1-hostile-review.md (5 MAJOR /
4 MODERATE / 5 MINOR; the review broke no arithmetic and every number
of the first delivery reproduced exactly — what it broke were the
READINGS).  What changed, all of it visible in the gates below:
  * MAJOR 1  THE FOUR-ACTOR POOL IS NOW BUILT TO DEPTH 4 and the
    r = 3 -> 4 term the first delivery declined to compute is part of
    this receipt.  The two-term rise it delivered its headline on is a
    ONE-STEP BLIP that reverses at the very next horizon.
  * MAJOR 2  THE PINNED-OBJECT DOCTRINE IS APPLIED IN ONE DIRECTION.
    The first delivery took the horn verdict on the pinned conditional
    and the pool verdict on the absolute kernel; here the pinned
    sector-normalized conditional is the headline object EVERYWHERE,
    including in the outcome decision, and the absolute kernel is
    context everywhere.  The pinned object is now tabulated ACROSS
    ACTOR POOLS, which the first delivery never did.
  * MAJOR 3  THE HORN'S ROOT LEG IS A THEOREM, NOT A MEASUREMENT.
    The layer's A <-> B and 0 <-> 1 relabellings are gated to be exact
    automorphisms, the root menu is gated to be one orbit per event
    kind, and the root conditional is therefore forced uniform for ANY
    equivariant terminal.  A non-equivariant terminal is exhibited
    breaking it.
  * MAJOR 4  "ROUTE R5 IS CLOSED" IS NARROWED to the MENU-EXACT ATOM
    route.  The sigma-level class R-SIG is gated to be RE-ENTERED and
    its N-step hitting probability is gated to be NON-ZERO where it is
    computable — the sigma-level renewal route is OPEN.
  * MAJOR 5  HZ5's TWO MAPS ARE GATED TO COINCIDE on the decider's
    whole input, so ONE test ran and R2's closure is inherited.
  * MODERATE 6-9 and MINOR 1-5: theorem-passes counted and disclosed,
    HZ5-1's unfailable clause repaired, window-artifact zeros
    qualified, anchor count reconciled, HZ8-b's scan made total, NC2
    relabelled a GRAMMAR perturbation, the determinism digest widened
    past cap 3, residue 4 replaced.
The review's own recomputations are credited where they are used and
every one of them is re-derived here by this receipt's own code.

PARENTS AND WHAT THIS RECEIPT REUSES RATHER THAN REBUILDS.
  * v10/code/d42b1_transport_exact.py — THE COMMITTED LAYER.  exec'd
    path-anchored, pre-print slice only.  Admission and pricing are
    NEVER re-implemented here.
  * v10/code/d42b3_placement_exact.py — the committed delivery-free
    layer (the d42a family), same idiom; used by the HZ6 positive
    control and by the HZ0 delivery-free anchors.
  * v10/code/d44a_closure_theorem_exact.py — the sigma slice, by TEXT
    SLICE (the d61/d62/d65 idiom), for the HZ6-ii Zhat control.
  * v10/code/d46b_martin_transport_exact.py — the objects: G(h, r),
    k_r(e|h), sector(), conditional().  Their DEFINITIONS are lifted
    by AST extraction from that receipt (gate HZ0-b), so the kernel
    this unit measures is the kernel D46b gated, character for
    character.
  * v10/code/d57_sector_exact_refinement.py — the coarsest-lumpable
    fixpoint refinement and its trivial-boundary control; its refine()
    shape is reproduced for HZ5 at two strictly coarser sector maps.

EXACT Fractions end to end.  Every cap, pool, horizon, window, seed
and wall-clock printed by the receipt itself.  Exit 1 ONLY on HZ0
anchor breakage (pin §7); every substantive negative exits 0.

WHAT THIS RECEIPT DOES NOT DO (pin §6, binding at every citation).
No infinite-volume claim under any outcome (scan-exempt: needle).
Every statement is horizon-scoped and pool-scoped.  The pinned object is the
SECTOR-NORMALIZED CONDITIONAL; the absolute completed weights are
horizon-bound (D44f) and are carried as context only.  No dimension
claim, no typicality claim, no quantum-layer claim.  No claim about
the identified click law: the missing map (D59/D65) is untouched.
"""
import ast
import os
import subprocess
import sys
import time
from collections import defaultdict
from fractions import Fraction as Fr
from itertools import permutations

sys.setrecursionlimit(300000)

T00 = time.time()


def sec():
    return f"[t+{time.time() - T00:7.1f}s]"


PASS = FAIL = ANCHOR_FAIL = 0
GATE_LABELS = []
THEOREM_GATES = []


def check(label, ok, detail="", anchor=False, theorem=""):
    """theorem = a NON-EMPTY string naming why this gate CANNOT FAIL.
    Round-1 MODERATE 7: '41 PASS' was read as 41 tests when at least
    seven of the passes were theorems of the construction.  Every such
    gate now declares the reason in its own line and is counted
    separately in the summary, so the PASS count is never read as a
    count of tests."""
    global PASS, FAIL, ANCHOR_FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    ANCHOR_FAIL += int(anchor and not ok)
    GATE_LABELS.append(label)
    if theorem:
        THEOREM_GATES.append((label.split(None, 1)[0], theorem))
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else "")
          + ("   [ANCHOR]" if anchor else "")
          + (f"   [THEOREM-PASS — CANNOT FAIL: {theorem}]"
             if theorem else ""))


OUT = []


def outcome(tag, text):
    OUT.append((tag, text))
    print(f"\n  [OUTCOME {tag}] {text}")


def fr(x):
    return str(x)


def frl(xs):
    return ", ".join(str(x) for x in xs)


print("[D70 — THE HORIZON LIMIT: is there a measure at transport scope "
      "that needs no bounded abstraction?]")
print("  banner: ROUND-1 REVIEWED AND REPAIRED (reviews/"
      "d70-round1-hostile-review.md,")
print("  5 MAJOR / 4 MODERATE / 5 MINOR; the review broke no arithmetic")
print("  and broke four readings).  Pin note-d70-horizon-limit-pin.md,")
print("  frozen and committed before this file was written.  EXACT")
print("  Fractions everywhere; the committed d42b1 transport layer and")
print("  the committed d42b3 delivery-free layer are exec'd")
print("  path-anchored and NOTHING about admission or pricing is")
print("  re-implemented.  The kernel objects are lifted by AST from the")
print("  terminal D46b receipt, so the object measured here IS the")
print("  object D46b gated.  NO infinite-volume claim under any")
print("  outcome (D46b MB6, binding): every number below is a")
print("  finite-horizon, finite-pool, finite-depth measurement at the")
print("  caps this receipt prints, and the pin's own prohibition is")
print("  enforced lexically by gate HZ8-b.")

# ======================================================================
# N0 / HZ0-a — THE SINGLE SOURCES, BY TEXT SLICE AND BY AST
# ======================================================================
print(f"\n{sec()} [HZ0-a — single sources]")

_LAYER = 'v10/code/d42b1_transport_exact.py'
_ls = open(_LAYER).read()
_PREFIX = _ls[:_ls.index('print("[d42b1')]
ns = {}
exec(compile(_PREFIX, 'd42b1_port', 'exec'), ns)
candidates_for = ns['candidates_for']
admissible = ns['admissible']
event_poset = ns['event_poset']
View = ns['View']
vname = ns['vname']
V0 = ns['V0']
deliver_options_in_view = ns['deliver_options_in_view']
prop_options_in_view = ns['prop_options_in_view']

_DFL = 'v10/code/d42b3_placement_exact.py'
_dfs = open(_DFL).read()
_DFPREFIX = _dfs[:_dfs.index('print("[d42b3')]
nsdf = {}
exec(compile(_DFPREFIX, 'd42b3_port', 'exec'), nsdf)
cf_df = nsdf['candidates_for']

check("HZ0-a(i) SINGLE SOURCE, TRANSPORT: the committed d42b1 layer is "
      "exec'd from its own path, pre-print slice only, and the slice is "
      "gated to carry the DEFINITIONS this receipt rides on — "
      "candidates_for, admissible, event_poset, View, vname, V0, and "
      "BOTH enumerators whose asymmetry is the B1 wall "
      "(deliver_options_in_view reads the whole holdings set; "
      "prop_options_in_view skips superseded).  Nothing about admission "
      "or pricing is re-implemented anywhere in this file",
      callable(candidates_for) and callable(admissible)
      and callable(deliver_options_in_view)
      and "def candidates_for" in _PREFIX
      and "def admissible" in _PREFIX
      and "def deliver_options_in_view" in _PREFIX
      and "def prop_options_in_view" in _PREFIX
      and "sys.exit" not in _PREFIX and "\ncheck(" not in _PREFIX,
      f"{_LAYER}: prefix {len(_PREFIX)} chars, 0 sys.exit, 0 top-level "
      f"check()", anchor=True)

check("HZ0-a(ii) SINGLE SOURCE, DELIVERY-FREE: the committed d42b3 "
      "placement layer is exec'd the same way — the like-for-like "
      "partner D46b built for its MB1-b / MB2-b anchors and the family "
      "the HZ6-ii positive control runs on",
      callable(cf_df) and "def candidates_for" in _DFPREFIX
      and "sys.exit" not in _DFPREFIX,
      f"{_DFL}: prefix {len(_DFPREFIX)} chars", anchor=True)

# ---- the kernel objects, lifted from the terminal D46b receipt -------
_D46B = 'v10/code/d46b_martin_transport_exact.py'
_bs = open(_D46B).read()
_btree = ast.parse(_bs)
_blines = _bs.splitlines(keepends=True)
_WANT = ('rel_potential', 'krel', 'sector', 'conditional')
_SEGS = {}
for _nd in _btree.body:
    if isinstance(_nd, ast.FunctionDef) and _nd.name in _WANT:
        _SEGS[_nd.name] = "".join(_blines[_nd.lineno - 1:_nd.end_lineno])
nsk = {'Fr': Fr}
for _nm in _WANT:
    exec(compile(_SEGS[_nm], 'd46b_' + _nm + '_ast', 'exec'), nsk)
rel_potential = nsk['rel_potential']
krel = nsk['krel']
sector = nsk['sector']
conditional = nsk['conditional']

check("HZ0-a(iii) THE KERNEL OBJECTS ARE THE D46B OBJECTS, extracted by "
      "AST from the TERMINAL D46b receipt rather than retyped: "
      "rel_potential (the exact backward recursion G(h, r) with "
      "G(h, 0) = 1), krel (k_r(e|h) = q(e|h).G(h+e, r-1)/G(h, r)), "
      "sector (per-EVENT-KIND mass) and conditional (THE PINNED OBJECT: "
      "k_r(e)/sector-mass(kind(e)), the d44f/LOG #370 horizon-stable "
      "candidate).  The four function definitions are located by "
      "ast.FunctionDef and compiled from the source lines they occupy, "
      "so a change to D46b's definitions would change this receipt's "
      "object",
      set(_SEGS) == set(_WANT)
      and all(callable(nsk[n]) for n in _WANT)
      and "G(h + (e,), r - 1)" in _SEGS['rel_potential']
      and "q * G(h + (e,), r - 1) / tot" in _SEGS['krel']
      and "v / s[e[0]]" in _SEGS['conditional'],
      f"lifted {len(_SEGS)} definitions from {_D46B}: "
      + ", ".join(f"{n} ({len(_SEGS[n].splitlines())} lines)"
                  for n in _WANT), anchor=True)

# ---- d44a's sigma, by text slice (the d61/d62/d65 idiom) ------------
_D44A = 'v10/code/d44a_closure_theorem_exact.py'
_ds = open(_D44A).read()
_blk1 = _ds[_ds.index("SG_VIOL = {'alive'"):_ds.index("\nSIG = {tuple(h)")]
nsdf['AB'] = ('A', 'B')
nsdf['permutations'] = permutations
nsdf['defaultdict'] = defaultdict


def cands_of(hk):
    return cf_df(list(hk), ('A', 'B'))


nsdf['cands_of'] = cands_of
exec(compile(_blk1, 'd44a_sigma_port', 'exec'), nsdf)
canon_sigma = nsdf['canon_sigma']

check("HZ0-a(iv) SIGMA BY TEXT SLICE for the HZ6-ii positive control: "
      "d44a's sigma_raw / ser / canon_sigma / own_alive block extracted "
      "verbatim between two anchored source landmarks (the d61/d62/d65 "
      "idiom), gated to be a PURE DEFINITION block — no sys.exit, no "
      "top-level check(), no top-level print survives extraction, so "
      "none of d44a's own gate protocol can execute inside this receipt",
      callable(canon_sigma) and "def sigma_raw" in _blk1
      and "def canon_sigma" in _blk1 and "def ser(" in _blk1
      and _blk1.count("sys.exit") == 0
      and _blk1.count("\ncheck(") == 0
      and _blk1.count("\nprint(") == 0,
      f"{_D44A}: slice {len(_blk1)} chars, "
      f"(exit, check, print) = (0, 0, 0)", anchor=True)

# ======================================================================
# HZ0 — THE ANCHORS.  Exit 1 lives here and nowhere else.
# ======================================================================
print(f"\n{sec()} [HZ0 — ANCHORS: every committed number this unit "
      f"stands on, reproduced in this receipt's own process]")

AB = ('A', 'B')
ABC = ('A', 'B', 'C')
ABCD = ('A', 'B', 'C', 'D')

# DECLARED CAPS — printed here, before anything uses them.
CAP_T = 6          # two-actor transport family, exhaustive menus
CAP_3 = 4          # three-actor pool, exhaustive menus
CAP_4 = 4          # four-actor pool — ROUND-1 MAJOR 1: was 3
CAP_DF = 6         # delivery-free d42a family, exhaustive menus
CAP_D46B = 5       # D46b's OWN cap — the window its anchors were taken in
CAP_NEG = 5        # the HZ6-i negative control's declared window
HZ5_CAPS = (3, 4, 5, 6)
HASHSEEDS = (0, 7, 999)
print(f"  DECLARED CAPS (pin §2 'every cap printed by the receipt'): "
      f"two-actor transport depth {CAP_T}; three-actor pool depth "
      f"{CAP_3}; four-actor pool depth {CAP_4}; delivery-free d42a "
      f"depth {CAP_DF}; D46b's own anchor window depth {CAP_D46B}; "
      f"HZ5 refinement caps {HZ5_CAPS}; HZ6-i negative-control window "
      f"depth {CAP_NEG}; HZ6-iv PYTHONHASHSEED values {HASHSEEDS}.  "
      f"NO sampled arm is run anywhere in this receipt: every row below "
      f"is EXACT and exhaustive at its printed cap, so the D46d "
      f"exact/sampled separation has nothing to separate.")
print(f"  ROUND-1 MAJOR 1, THE COST DECISION, PRINTED BEFORE THE RUN: "
      f"the four-actor pool's cap moved from 3 to {CAP_4}.  That is "
      f"318,704 further histories, which the first delivery priced and "
      f"declined.  THE CHOICE MADE HERE IS SINGLE-CORE AND SERIAL — no "
      f"multiprocessing, no worker pool, no shared state — because the "
      f"measured rate on this machine is ~1.1 ms per four-actor depth-4 "
      f"menu, i.e. ~6-8 minutes serial, and a serial build keeps the "
      f"receipt byte-deterministic and free of any scheduling order.  "
      f"The wall clock of that build is printed by the receipt itself "
      f"below, and it makes this the campaign's longest receipt.")


def build(actors, cap):
    cache = {}
    frontier = [()]
    while frontier:
        h = frontier.pop()
        cache[h] = candidates_for(list(h), actors)
        if len(h) >= cap:
            continue
        for e, q in cache[h]:
            frontier.append(h + (e,))
    return cache


# ---------------------------------------------------------------------
# THE DEEPEST-LAYER LEAF COLLAPSE, declared here and CONTROLLED below.
# ---------------------------------------------------------------------
# The AST-lifted D46b recursion is G(h, 0) = 1 and
# G(h, r) = sum_e q(e|h) G(h + e, r - 1).  A history at the family's
# deepest layer D is therefore only ever asked for G(h, 1), and
# G(h, 1) = sum_e q(e|h) * 1 = the menu's total weight.  NOTHING ELSE
# about a depth-D menu can enter any number in this receipt, because
# drift_cells never takes a kernel at depth > D - 1.  So the deepest
# layer is stored as its exact menu-weight TOTAL under one synthetic
# option, which reproduces G(h, 1) EXACTLY and holds 318,704 four-actor
# menus in ~0.2 GB instead of tens of GB.  This is a storage decision,
# not a modelling one, and it is CONTROLLED at HZ2-f by running the
# three-actor pool BOTH ways and requiring byte-identical drift cells.
LEAF = ('LEAF-COLLAPSED-DEEPEST-LAYER',)


def build_leaf(actors, cap):
    """Exhaustive menus to depth cap - 1; the depth-cap layer stored as
    its exact menu-weight total only (see LEAF above)."""
    cache = {}
    frontier = [()]
    while frontier:
        h = frontier.pop()
        cache[h] = candidates_for(list(h), actors)
        if len(h) >= cap - 1:
            continue
        for e, q in cache[h]:
            frontier.append(h + (e,))
    deep = 0
    for h in [x for x in cache if len(x) == cap - 1]:
        for e, q in cache[h]:
            tot = sum(qq for ee, qq in
                      candidates_for(list(h) + [e], actors))
            cache[h + (e,)] = [(LEAF, tot)]
            deep += 1
    return cache, deep


def collapse_deepest(cache, cap):
    """The same collapse applied to an already-built full cache, for the
    HZ2-f like-for-like control."""
    out = {}
    for h, men in cache.items():
        if len(h) == cap:
            out[h] = [(LEAF, sum(q for e, q in men))]
        elif len(h) < cap:
            out[h] = men
    return out


_t = time.time()
CACHE = build(AB, CAP_T)
_TBUILD = time.time() - _t
LEV = defaultdict(int)
for h in CACHE:
    LEV[len(h)] += 1
CUM = [sum(LEV[j] for j in range(k + 1)) for k in range(CAP_T + 1)]
print(f"{sec()}   two-actor transport family built to depth {CAP_T} in "
      f"{_TBUILD:.1f}s: per level {[LEV[k] for k in sorted(LEV)]}")

check("HZ0-1 THE ARM-1T CENSUS, both committed anchors in one object: "
      "the cumulative sizes [1, 9, 69, 521, 3969, 30729] (the "
      "D44b/d42b1/D46b census) AND 243,769 to depth 6 (the D56 probe's "
      "M1 anchor).  D46b held menus to depth 5 and D56 obtained its "
      "depth-6 count by summing menu sizes at depth 5; this receipt "
      "holds the menus THEMSELVES to depth 6, so the depth-6 number is "
      "an enumerated family here and not a count",
      CUM == [1, 9, 69, 521, 3969, 30729, 243769],
      f"cumulative = {CUM}; per level = "
      f"{[LEV[k] for k in sorted(LEV)]}", anchor=True)

# --- the ladder (D46b MB1) -------------------------------------------
def census_of(cache, upto):
    s = {}
    for h in cache:
        if len(h) > upto:
            continue
        k = str(sum(q for e, q in cache[h]))
        s[k] = s.get(k, 0) + 1
    return s


cen4 = census_of(CACHE, 4)
cen5 = census_of(CACHE, 5)
cen6 = census_of(CACHE, 6)
check("HZ0-2 THE QUARTER-QUANTIZED LADDER (D46b MB1): the exact "
      "per-history menu weight sum takes the value set {2, 5/2} with "
      "multiplicities {2: 3757, 5/2: 212} at depth <= 4 and "
      "{2: 29605, 5/2: 1124} at depth <= 5 — both committed — and the "
      "value set is UNCHANGED at depth <= 6, which is this receipt's "
      "own one-level extension of the claim, not a committed number",
      cen4 == {'2': 3757, '5/2': 212}
      and cen5 == {'2': 29605, '5/2': 1124}
      and set(cen6) == set(cen5) == {'2', '5/2'},
      f"depth <= 4: {cen4}; depth <= 5: {cen5}; depth <= 6 (NEW): "
      f"{cen6}", anchor=True)

# --- the delivery-free partner ---------------------------------------
_t = time.time()
DF = {}
_fr = [()]
while _fr:
    h = _fr.pop()
    DF[h] = cf_df(list(h), AB)
    if len(h) >= CAP_DF:
        continue
    for e, q in DF[h]:
        _fr.append(h + (e,))
_DFBUILD = time.time() - _t
dlev = defaultdict(int)
for h in DF:
    dlev[len(h)] += 1
dcum = [sum(dlev[j] for j in range(k + 1)) for k in range(CAP_DF + 1)]
dcen = census_of(DF, 5)
print(f"{sec()}   delivery-free d42a family built to depth {CAP_DF} in "
      f"{_DFBUILD:.1f}s")
check("HZ0-3 THE DELIVERY-FREE PARTNER, RECOMPUTED not cited (D46b "
      "MB1-b): the d42a family from the committed d42b3 layer — "
      "cumulative [1, 7, 39, 215, 1191, 6471] to depth 5 (the d43b MG0 "
      "census) and 34,375 to depth 6 (D65's N1 anchor) — and its own "
      "menu-weight-sum census {2: 5963, 5/2: 508} at depth <= 5, so "
      "the transport/delivery-free VALUE-SET coincidence is computed "
      "here and not quoted",
      dcum[:6] == [1, 7, 39, 215, 1191, 6471] and dcum[6] == 34375
      and dcen == {'2': 5963, '5/2': 508}
      and set(dcen) == set(cen5),
      f"delivery-free cumulative = {dcum}; census depth <= 5 = {dcen}; "
      f"value sets equal = {set(dcen) == set(cen5)}", anchor=True)

# --- the potentials and both ratio columns ---------------------------
GT = rel_potential(CACHE)
GD = rel_potential(DF)
ROOT = ()
tG = [GT(ROOT, r) for r in range(1, CAP_T + 2)]
dG = [GD(ROOT, r) for r in range(1, CAP_DF + 2)]
TG_REF = [Fr(2), Fr(4), Fr(257, 32), Fr(1035, 64), Fr(4173, 128),
          Fr(134587, 2048)]
DG_REF = [Fr(2), Fr(4), Fr(257, 32), Fr(1037, 64), Fr(2101, 64),
          Fr(68313, 1024)]
check("HZ0-4 THE TRANSPORT FINITE-HORIZON POTENTIALS at the root, "
      "exact, by the AST-lifted backward recursion: G_1..G_6 = 2, 4, "
      "257/32, 1035/64, 4173/128, 134587/2048 (D46b MB2, every value "
      "anchored) — and G_7, which this receipt's one-level-deeper "
      "family makes computable for the first time and which is NEW, "
      "horizon-scoped, and anchored to nothing",
      tG[:6] == TG_REF,
      "; ".join(f"G_{i + 1} = {v}" for i, v in enumerate(tG))
      + f"  [G_7 = {tG[6]} is NEW]", anchor=True)
check("HZ0-5 THE DELIVERY-FREE POTENTIALS at the same root and "
      "horizons (D46b MB2-b): 2, 4, 257/32, 1037/64, 2101/64, "
      "68313/1024 — numerically IDENTICAL to transport through D = 3 "
      "and first separating at D = 4 (1035/64 transport vs 1037/64 "
      "delivery-free), i.e. deliveries are invisible to the potential "
      "below depth 4",
      dG[:6] == DG_REF and dG[:3] == tG[:3] and dG[3] != tG[3],
      "; ".join(f"G_{i + 1} = {v}" for i, v in enumerate(dG[:6]))
      + f"; first separation at D = 4  [G_7 = {dG[6]} is NEW]",
      anchor=True)

tR = [tG[i] / tG[i - 1] for i in range(1, len(tG))]
dR = [dG[i] / dG[i - 1] for i in range(1, len(dG))]
TR_REF = [Fr(2), Fr(257, 128), Fr(1035, 514), Fr(1391, 690),
          Fr(134587, 66768)]
DR_REF = [Fr(2), Fr(257, 128), Fr(1037, 514), Fr(2101, 1037),
          Fr(68313, 33616)]
print("      D | delivery-free G_D | transport G_D | df ratio | "
      "transport ratio")
for i in range(len(tG)):
    rr = (f"{dR[i - 1]} (~{float(dR[i - 1]):.6f}) | "
          f"{tR[i - 1]} (~{float(tR[i - 1]):.6f})") if i else "— | —"
    print(f"      {i + 1} | {dG[i]} | {tG[i]} | {rr}")
df_ge = all(dR[i] >= tR[i] for i in range(5))
peak = max(range(5), key=lambda i: tR[i])
turns = tR[4] < tR[3] and tR[3] > tR[2]
check("HZ0-6 BOTH RATIO COLUMNS EXACTLY (D46b MB4/MB4-b): the "
      "transport ratios G_D/G_(D-1) at D = 2..6 are 2, 257/128, "
      "1035/514, 1391/690, 134587/66768 and the delivery-free ones are "
      "2, 257/128, 1037/514, 2101/1037, 68313/33616; the delivery-free "
      "column is >= the transport column at every horizon (deliveries "
      "REDUCE finite-horizon branching at the reachable caps) and the "
      "transport column PEAKS at D = 5 and turns down at D = 6.  "
      "D44a's lambda = 2 is the delivery-free chain's ASYMPTOTIC "
      "Perron eigenvalue and is not comparable with any of these "
      "finite-horizon quantities — the category distinction D46b's "
      "round 1 imposed",
      tR[:5] == TR_REF and dR[:5] == DR_REF and df_ge
      and peak == 3 and turns,
      f"transport = {frl(tR[:5])}; delivery-free = {frl(dR[:5])}; "
      f"df >= transport everywhere = {df_ge}; transport peak at "
      f"D = {peak + 2}; D = 7 transport ratio = {tR[5]} "
      f"(~{float(tR[5]):.6f}) [NEW]", anchor=True)

# --- the root conditional, and the two D46b drift sequences ----------
RK = [krel(CACHE, GT, ROOT, r) for r in range(1, CAP_T + 2)]
SM = [sector(k) for k in RK]
CD = [conditional(k) for k in RK]
cond_drift = [max(abs(CD[i][e] - CD[i - 1][e]) for e in CD[0])
              for i in range(1, len(CD))]
check("HZ0-7 THE PINNED OBJECT AT THE ROOT (D46b MB3-c) IS A THEOREM "
      "OF THE CONSTRUCTION, NOT A MEASUREMENT — ROUND-1 MAJOR 3, "
      "re-graded here.  The sector-normalized conditional is EXACTLY "
      "identical at every remaining horizon r = 1..6 — drift exactly 0 "
      "at all five committed steps, not small but zero.  D46b carried "
      "this as an honesty caveat ('partly a symmetry artifact'); round "
      "1 established it is not PARTLY an artifact but ENTIRELY one, and "
      "HZ3-s1/HZ3-s2 below GATE the mechanism: the layer's A <-> B and "
      "0 <-> 1 relabellings are exact automorphisms, the root menu is "
      "ONE ORBIT PER EVENT KIND under them, and therefore ANY "
      "equivariant terminal forces the uniform-within-kind conditional "
      "at every horizon.  The value 0 here carries NO information about "
      "horizon stability; the off-root behaviour (HZ0-8, HZ2) is the "
      "whole of the real test.  The sixth step r = 6 -> 7 is this "
      "receipt's extension and is 0 for the same reason",
      cond_drift[:5] == [Fr(0)] * 5,
      f"root conditional drift r -> r+1 for r = 1..6 = "
      f"{[str(d) for d in cond_drift]}", anchor=True,
      theorem="root-menu symmetry x equivariant terminal, gated at "
              "HZ3-s1/HZ3-s2")

abs_drift = [max(abs(RK[i][e] - RK[i - 1][e]) for e in RK[0])
             for i in range(1, len(RK))]
l1_drift = [sum(abs(RK[i][e] - RK[i - 1][e]) for e in RK[0])
            for i in range(1, len(RK))]
sec_drift = [max(abs(SM[i][k] - SM[i - 1][k]) for k in SM[0])
             for i in range(1, len(SM))]
AD_REF = [Fr(0), Fr(1, 1028), Fr(191, 265995), Fr(412, 1439685),
          Fr(4629, 187210517)]
L1_REF = [Fr(0), Fr(3, 514), Fr(382, 88665), Fr(824, 479895),
          Fr(27774, 187210517)]
SD_REF = [Fr(0), Fr(3, 1028), Fr(191, 88665), Fr(412, 479895),
          Fr(13887, 187210517)]
check("HZ0-7b THE ROOT ABSOLUTE DRIFT (D46b MB3-b), all three norms, "
      "value for value: the ABSOLUTE kernel and the per-kind sector "
      "MASSES do drift with the remaining horizon at every one of "
      "D46b's five reachable steps — these are the horizon-BOUND "
      "quantities D44f predicts, as against the sector-normalized "
      "conditional of HZ0-7 — and the r = 1 -> 2 step is exactly zero "
      "in all three",
      abs_drift[:5] == AD_REF and l1_drift[:5] == L1_REF
      and sec_drift[:5] == SD_REF,
      "L-inf = " + frl(abs_drift[:5]) + "; L1 = " + frl(l1_drift[:5])
      + "; sector-L-inf = " + frl(sec_drift[:5])
      + f"  [the sixth step r = 6 -> 7 is NEW: L-inf {abs_drift[5]}]",
      anchor=True)

# D46b's off-root sup, IN D46B'S OWN WINDOW (len(h) + r <= CAP_D46B)
off_sup_a, off_n_a, off_dr_a = [], [], []
for r in (1, 2, 3, 4):
    best, n, nd = Fr(0), 0, 0
    for h in CACHE:
        if len(h) + r > CAP_D46B:
            continue
        n += 1
        a = conditional(krel(CACHE, GT, h, r))
        b = conditional(krel(CACHE, GT, h, r + 1))
        d = max(abs(b[e] - a[e]) for e in a)
        nd += int(bool(d))
        if d > best:
            best = d
    off_sup_a.append(best)
    off_n_a.append(n)
    off_dr_a.append(nd)
check("HZ0-8 THE OFF-ROOT CONDITIONAL SUP (D46b MB3-d) — reproduced IN "
      "D46B'S OWN WINDOW, len(h) + r <= 5, because a sup taken over a "
      "wider family is a different number and comparing it to a "
      "committed one would be the horizon-mismatch error D46b's round 1 "
      "convicted: 1/18, 4/171, 8/741, 176/32877 over 3969, 521, 69, 9 "
      "histories with 700, 140, 36, 4 of them carrying any conditional "
      "drift at all",
      off_sup_a == [Fr(1, 18), Fr(4, 171), Fr(8, 741), Fr(176, 32877)]
      and off_n_a == [3969, 521, 69, 9]
      and off_dr_a == [700, 140, 36, 4],
      "; ".join(f"r={i + 1}->{i + 2}: sup {off_sup_a[i]} over "
                f"{off_n_a[i]} histories, {off_dr_a[i]} drifting"
                for i in range(4)), anchor=True)

# D46b's family-uniform sup on the ABSOLUTE kernel, same window
uni_sup_a = []
for r in (1, 2, 3, 4):
    best = Fr(0)
    for h in CACHE:
        if len(h) + r + 1 > CAP_D46B + 1:
            continue
        a = krel(CACHE, GT, h, r)
        b = krel(CACHE, GT, h, r + 1)
        d = max(abs(b[e] - a[e]) for e in a)
        if d > best:
            best = d
    uni_sup_a.append(best)
check("HZ0-9 THE FAMILY-UNIFORM SUP (D46b MB3-e), also in D46b's own "
      "window: 3/110, 3/253, 373/69230, 2333/1838829 — the four-term "
      "sequence the pin's HZ2 lean rests on, and which the pin itself "
      "records is four terms at small caps at two actors, is 'not a "
      "rate' in its own source, and is not a limit",
      uni_sup_a == [Fr(3, 110), Fr(3, 253), Fr(373, 69230),
                    Fr(2333, 1838829)],
      frl(uni_sup_a), anchor=True)

# D46b MB5 witness + the non-sufficiency census (HZ4 rides on these)
tA = ('A', V0, 0)
pA0 = ('p', 'A', V0, 0)
SELFA = ('r', 'A', frozenset({tA}), frozenset({tA}))
V1 = vname(V0, frozenset({tA}), 'A')
WIT = (pA0, SELFA, ('d', 'A', 'B', V1))
_adm = [admissible(list(WIT[:i]), WIT[i], AB) for i in range(3)]
_wq = Fr(1)
for _a, _q in _adm:
    _wq *= _q if _a else Fr(0)
MATCH = []
for r in (1, 2, 3):
    MATCH.append(sector(krel(CACHE, GT, ROOT, r))
                 == sector(krel(CACHE, GT, WIT, r)))
share = []
for r in (1, 2, 3):
    sr = sector(krel(CACHE, GT, ROOT, r))
    n = tot = 0
    for h in CACHE:
        if h == ROOT or len(h) + r > CAP_D46B + 1:
            continue
        tot += 1
        if sector(krel(CACHE, GT, h, r)) == sr:
            n += 1
    share.append((n, tot))
check("HZ0-10 MB5 — ROOT = RENEWAL AT MATCHED REMAINING HORIZON, and "
      "its NON-SUFFICIENCY CENSUS, both reproduced: the 1/256 "
      "reconvergence witness [p(A,v0,0), blind self-seal, deliver v1 "
      "to B] is re-admitted through the committed layer, its per-kind "
      "sector masses equal the root's at r = 1, 2, 3, and 8196/30728, "
      "1060/3968, 104/520 histories share the root's masses — so "
      "sector-mass agreement is NECESSARY and NOT SUFFICIENT for "
      "renewal.  HZ4 rides on exactly this and may not upgrade it",
      all(a for a, q in _adm) and _wq == Fr(1, 256) and all(MATCH)
      and share == [(8196, 30728), (1060, 3968), (104, 520)],
      f"witness chain weight = {_wq}; matched-horizon equality at "
      f"r = 1, 2, 3 = {MATCH}; census = "
      + "; ".join(f"r={i + 1}: {n}/{t}" for i, (n, t) in
                  enumerate(share)), anchor=True)

if ANCHOR_FAIL:
    print(f"\n[VERDICT] HZ0 ANCHOR BREAKAGE — {ANCHOR_FAIL} committed "
          f"number(s) failed to reproduce in this receipt's own "
          f"process.  Per the pin's falsifier 6 and exit protocol §7 "
          f"the unit is INVALID and nothing below may be read.  "
          f"NOTHING HAS BEEN ADJUSTED TO MAKE IT PASS.  exit 1")
    sys.exit(1)
print(f"{sec()}   HZ0: all {PASS} ANCHOR GATES reproduce.  ROUND-1 "
      f"MINOR 1, the count reconciled and THIS RECEIPT MADE THE SOURCE: "
      f"the {PASS} are 4 PROVENANCE gates (HZ0-a i-iv: the two exec'd "
      f"layers, the AST kernel lift, the sigma text slice) plus 11 "
      f"COMMITTED-NUMBER anchors (HZ0-1..HZ0-10 and HZ0-7b).  The first "
      f"delivery's note said '14 anchors' over a list of ten bullets; "
      f"the right statement is 4 + 11 = {PASS} anchor gates.  Exit 1 is "
      f"now unreachable — every gate below exits 0 whichever way it "
      f"lands (pin §7).")

# ======================================================================
# HZ1 — PROPERNESS, EXTENDED
# ======================================================================
print(f"\n{sec()} [HZ1 — PROPERNESS, EXTENDED: gated FIRST, as the "
      f"prerequisite (pin §4 lean); its failure is outcome HZ-IV]")

print("  WHAT IS AND IS NOT SUBSTANTIVE HERE, said before the numbers.")
print("  sum_e k_r(e|h) = 1 is an IDENTITY of the construction: G(h, r)")
print("  is defined as sum_e q(e|h) G(h+e, r-1) and k_r divides by it.")
print("  Verifying it is a REGRESSION TRIPWIRE on the extraction and on")
print("  the menu bookkeeping — it catches a menu used in the kernel")
print("  that differs from the menu used in the potential — and it is")
print("  labelled as one.  The three SUBSTANTIVE properness questions")
print("  are gated separately below: (a) strict positivity of every")
print("  potential (a zero denominator is the only way the identity can")
print("  break), (b) non-negativity of every kernel entry, and (c)")
print("  CUT-ADDITIVITY of the chained measure — the transport analogue")
print("  of the d42a defect the pin's HZ-IV names.")

prop_rows = []
prop_bad = pos_bad = neg_bad = 0
ntested = 0
for r in range(1, CAP_T + 2):
    n = 0
    for h in CACHE:
        if len(h) + r > CAP_T + 1:
            continue
        n += 1
        g = GT(h, r)
        if g <= 0:
            pos_bad += 1
            continue
        k = krel(CACHE, GT, h, r)
        ntested += 1
        if sum(k.values()) != 1:
            prop_bad += 1
        if any(v < 0 for v in k.values()):
            neg_bad += 1
    prop_rows.append((r, n))
print("  relative horizon r | histories with a computable k_r | "
      "sum_e k_r == 1 exactly")
for r, n in prop_rows:
    print(f"      r = {r:d}  |  {n:7d}  |  yes")
R_MAX = prop_rows[-1][0]
check("HZ1-a PROPERNESS FAMILY-WIDE, EXTENDED FROM r = 1, 2 TO "
      f"r = 1..{R_MAX} [REGRESSION TRIPWIRE, and the extension is the "
      "content].  D46b gated sum_e k_r(e|h) = 1 family-wide at r = 1 "
      "(30,729 histories) and r = 2 (3,969).  Here it holds at EVERY "
      "history of the depth-6 family with a computable k_r: 243,769 at "
      "r = 1, 30,729 at r = 2, 3,969 at r = 3, 521 at r = 4, 69 at "
      "r = 5, 9 at r = 6, 1 at r = 7.  The pin's weak POSITIVE lean on "
      "HZ1 at r >= 3 family-wide is CONFIRMED at these caps; outcome "
      "HZ-IV is not entered by this route",
      prop_bad == 0 and ntested == sum(n for r, n in prop_rows),
      f"kernels tested = {ntested}; sums != 1 = {prop_bad}; "
      f"per-r counts = {[n for r, n in prop_rows]}",
      theorem="sum_e k_r = 1 is the definition of G divided by itself; "
              "only a menu/potential mismatch could break it")
check("HZ1-b STRICT POSITIVITY AND NON-NEGATIVITY — the substantive "
      "half.  Every one of the potentials above is strictly positive "
      "(so no kernel is defined by a zero denominator) and every kernel "
      "entry is >= 0, so each k_r really is a probability on the menu "
      "and not merely a normalized signed weight.  The mechanism is in "
      "the committed layer: the idle option is emitted at every history "
      "and its weight 1 - (1/4)(has_p) - (1/4)(has_am) - (1/4)(has_d) "
      "is at worst 1/4",
      pos_bad == 0 and neg_bad == 0
      and ntested == sum(n for r, n in prop_rows),
      f"non-positive potentials = {pos_bad}; negative kernel entries = "
      f"{neg_bad}, over {ntested} kernels")

CUTS = [GT(ROOT, n) for n in range(1, CAP_T + 2)]
cut_flat = all(c == 1 for c in CUTS)
chain_bad = 0
for R in range(1, CAP_T + 2):
    mass = {(): Fr(1)}
    for n in range(R):
        nxt = {}
        for h, w in mass.items():
            k = krel(CACHE, GT, h, R - n)
            for e, v in k.items():
                nxt[h + (e,)] = nxt.get(h + (e,), Fr(0)) + w * v
        mass = nxt
        if sum(mass.values()) != 1:
            chain_bad += 1
check("HZ1-c CUT-ADDITIVITY IS AN IDENTITY, NOT A MEASUREMENT — "
      "ROUND-1 MODERATE 6, re-graded here.  The first delivery called "
      "this 'the substantive half'; it is not.  Given HZ1-a "
      "(sum_e k_r = 1 at every history) the chained mass at every cut "
      "is 1 BY INDUCTION — it is a product of probability kernels — so "
      "HZ-IV's cut-additivity clause was disposed of by construction "
      "before this receipt ran, and the contrast against the raw "
      "weight's cut masses is the observation that the raw weight is "
      "UNNORMALIZED.  THE SUBSTANTIVE PROPERNESS GATE IS HZ1-b (strict "
      "positivity: the only way the identity can break), and the "
      "substantive version of 'is it consistent across R' is not "
      "cut-additivity at all — it is exactly what HZ2's drift table "
      "measures.  Kept as REPORTING because the raw cut masses are "
      "worth printing: "
      "The RAW path weight is NOT a measure at transport either: its "
      "cut masses sum_{|h| = n} q(h) are exactly the root potentials "
      f"{frl(CUTS[:CAP_T + 1])}, so the same defect §B2.10 names at "
      "d42a (1, 2, 4, 257/32, 1037/64, 2101/64, 68313/1024) is present "
      "here with the transport potentials in place of the "
      "delivery-free ones.  What the horizon normalization BUYS is "
      "exactly this: chaining k_R, k_(R-1), ..., k_1 from the root "
      "gives total mass exactly 1 at EVERY intermediate cut, for every "
      f"R = 1..{CAP_T + 1}.  So the finite-horizon objects are honest "
      "measures and the HZ-IV cut-additivity failure does NOT fire — "
      "at the price of the horizon dependence HZ2 and HZ3 measure",
      chain_bad == 0 and not cut_flat and CUTS[:2] == [Fr(2), Fr(4)],
      f"raw cut masses = {frl(CUTS)} (flat = {cut_flat}); chained "
      f"cut-mass violations over R = 1..{CAP_T + 1} = {chain_bad}",
      theorem="a chain of probability kernels has cut mass 1 by "
              "induction from HZ1-a")

# ======================================================================
# HZ2 — THE CAUCHY TABLE
# ======================================================================
print(f"\n{sec()} [HZ2 — THE CAUCHY TABLE (the unit's core).  No fitted "
      f"rate, no extrapolation, no invented threshold.  The word the "
      f"pin permits, and the only word used below, is 'contracts over "
      f"the computed horizons'.]")


def linf(a, b):
    return max(abs(b[e] - a[e]) for e in a)


def l1n(a, b):
    return sum(abs(b[e] - a[e]) for e in a)


def drift_cells(cache, G, cap, rmax_off=1):
    """sup ||k_(r+1) - k_r|| by (relative horizon r, history DEPTH L),
    in the three D46b norms plus the two conditional norms.  Reported
    per depth as well as family-uniform, because 'contracts at the root
    while failing family-wide' is the pin's own falsifier 2."""
    cells = {}
    for r in range(1, cap + 1):
        for L in range(0, cap + 2 - r - rmax_off):
            hs = [h for h in cache if len(h) == L]
            if not hs:
                continue
            best = [Fr(0)] * 5
            for h in hs:
                a, b = krel(cache, G, h, r), krel(cache, G, h, r + 1)
                sa, sb = sector(a), sector(b)
                ca, cb = conditional(a), conditional(b)
                vals = [linf(a, b), l1n(a, b),
                        max(abs(sb[k] - sa[k]) for k in sa),
                        linf(ca, cb), l1n(ca, cb)]
                best = [max(x, y) for x, y in zip(best, vals)]
            cells[(r, L)] = best
    return cells


def contracts_from_first_nonzero(seq):
    """The D46b framing, made a function: a leading EXACT ZERO is
    stronger than contraction (the r = 1 -> 2 root step is exactly 0 in
    all three norms), so contraction is read from the first nonzero
    term onward and must be STRICT from there."""
    i0 = next((i for i, v in enumerate(seq) if v != 0), None)
    if i0 is None:
        return True
    s = seq[i0:]
    return all(s[i] < s[i - 1] for i in range(1, len(s)))


CELLS2 = drift_cells(CACHE, GT, CAP_T)
NORMS = ("L-inf (abs kernel)", "L1 (abs kernel)", "sector-L-inf",
         "L-inf (CONDITIONAL)", "L1 (CONDITIONAL)")
RS2 = sorted({r for r, L in CELLS2})
LS2 = sorted({L for r, L in CELLS2})
print(f"  TWO-ACTOR ARM (ARM-1T), exhaustive to depth {CAP_T}.")
print("  THE WINDOW-CONTROLLED OBJECT FIRST.  A sup over the whole "
      "family at relative horizon r is taken over histories of depth "
      f"<= {CAP_T} - r, so the window SHRINKS as r grows and a "
      "family-uniform sequence in r is NOT a single-window sequence.  "
      "The rows below fix the history depth L and vary r, which is the "
      "comparison the pin's falsifier 2 asks for ('the root is not the "
      "family'):")
ROWS2 = {}
for j, nm in enumerate(NORMS):
    print(f"    sup over depth-L histories, norm = {nm}:")
    for L in LS2:
        seq = [CELLS2[(r, L)][j] for r in RS2 if (r, L) in CELLS2]
        ROWS2[(nm, L)] = seq
        print(f"      L = {L}: " + ", ".join(
            f"r={RS2[i]}->{RS2[i] + 1}: {seq[i]}"
            for i in range(len(seq))))
row_contracts = {(nm, L): contracts_from_first_nonzero(ROWS2[(nm, L)])
                 for nm in NORMS for L in LS2}
ROW_BAD = sorted([(nm, L) for (nm, L) in row_contracts
                  if not row_contracts[(nm, L)]], key=repr)
ROW_BAD_OFFROOT = [(nm, L) for (nm, L) in ROW_BAD if L > 0]
ROW_BAD_ROOT = [(nm, L) for (nm, L) in ROW_BAD if L == 0]

print("  AND THE FAMILY-UNIFORM SUP (the D46b object), with the "
      "shrinking-window caveat above attached to it in place.  "
      "ROUND-1 MODERATE 9: the window at horizon r contains only the "
      "depths printed beside each column, and where that list is [0] "
      "THE WINDOW CONTAINS THE ROOT AND NOTHING ELSE — so a terminal 0 "
      "in a CONDITIONAL row there is the symmetry identity of HZ0-7 / "
      "HZ3-s2 and is NOT contraction and NOT shrinkage.  Every such "
      "entry is marked [ROOT ONLY — window artifact, not a limit]:")
DEPTHS_AT_R = {r: sorted({L for (rr, L) in CELLS2 if rr == r})
               for r in RS2}
ROOTONLY_R = [r for r in RS2 if DEPTHS_AT_R[r] == [0]]
print(f"    depths inside the family-uniform window, by r: "
      + "; ".join(f"r={r}: {DEPTHS_AT_R[r]}" for r in RS2)
      + f"   -> ROOT-ONLY at r = {ROOTONLY_R}")
UNI2 = {}
for j, nm in enumerate(NORMS):
    row = [max(CELLS2[(r, L)][j] for (rr, L) in CELLS2 if rr == r)
           for r in RS2]
    UNI2[nm] = row
    print(f"    {nm:22s}: " + ", ".join(
        f"r={RS2[i]}->{RS2[i] + 1}: {row[i]}"
        + ("  [ROOT ONLY — window artifact, not a limit]"
           if RS2[i] in ROOTONLY_R else "")
        for i in range(len(row))))
uni_contracts = {nm: contracts_from_first_nonzero(UNI2[nm])
                 for nm in NORMS}
UNI2_OFFROOT = {nm: [UNI2[nm][i] for i in range(len(RS2))
                     if RS2[i] not in ROOTONLY_R] for nm in NORMS}
cond_tail_is_artifact = all(
    UNI2[nm][-1] == 0 and RS2[-1] in ROOTONLY_R
    for nm in ("L-inf (CONDITIONAL)", "L1 (CONDITIONAL)"))
check("HZ2-e THE TERMINAL ZEROS OF THE CONDITIONAL FAMILY-UNIFORM ROWS "
      "ARE WINDOW ARTIFACTS AND ARE STRUCK FROM EVERY 'CONTRACTS' / "
      "'SHRINKS' READING (ROUND-1 MODERATE 9).  At the deepest "
      "reachable horizon the family-uniform window has emptied of "
      "off-root histories: it contains the root alone, where the "
      "conditional is 0 by the symmetry identity of HZ0-7.  So the "
      "final 0 in the two conditional rows is neither contraction nor "
      "shrinkage, it is the window emptying, and the first delivery "
      "quoted it in a summary sentence and in LOG #484.  The gate "
      "requires (i) that the deepest horizon's window IS root-only, "
      "(ii) that the conditional rows do end in 0 there, and (iii) that "
      "the off-root-window prefix of every row is what any contraction "
      "statement is taken on",
      cond_tail_is_artifact and ROOTONLY_R == [RS2[-1]]
      and all(len(UNI2_OFFROOT[nm]) == len(RS2) - 1 for nm in NORMS),
      f"root-only horizons = {ROOTONLY_R} of {RS2}; conditional rows "
      f"end in 0 there = {cond_tail_is_artifact}; the off-root-window "
      f"conditional rows, which are what is read: "
      + "; ".join(f"{nm} = {frl(UNI2_OFFROOT[nm])}"
                  for nm in ("L-inf (CONDITIONAL)", "L1 (CONDITIONAL)")))

# D46b MB3-e's actual norm-freeness claim: the ROOT drift ratios
def ratios(seq):
    return [seq[i] / seq[i - 1] for i in range(1, len(seq))
            if seq[i - 1] != 0]


rat_abs, rat_l1, rat_sec = ratios(abs_drift), ratios(l1_drift), \
    ratios(sec_drift)
norm_free2 = (rat_abs == rat_l1 == rat_sec)
print(f"  the ROOT drift, exact, r = 1..{CAP_T + 1}: L-inf "
      f"{frl(abs_drift)}; L1 {frl(l1_drift)}; sector-L-inf "
      f"{frl(sec_drift)}")
print(f"  its ratio SEQUENCE (a SEQUENCE, not a rate — D46b's own "
      f"word): {[f'{float(x):.4f}' for x in rat_abs]}; the three norms "
      f"give exactly equal ratio sequences: {norm_free2}")
root_abs_contracts = contracts_from_first_nonzero(abs_drift)
root_abs_contracts_d46b = contracts_from_first_nonzero(abs_drift[:5])
root_cond_zero = all(d == 0 for d in cond_drift)
check("HZ2-d THE ROOT ROW, WHERE THE EXTRA HORIZON CHANGES A COMMITTED "
      "READING.  D46b MB3-e gated that the ROOT's absolute drift "
      "'contracts monotonically at the root from r = 2 on, out to "
      "r = 6', which was true of every step it could compute.  This "
      "receipt computes ONE MORE step and reports what it finds, in the "
      "direction it lands.  The gate's substantive content is (i) the "
      "monotonicity verdict on D46b's own five steps, (ii) the "
      "monotonicity verdict once the sixth is added, and (iii) that the "
      "three norms still give EXACTLY equal ratio sequences over all "
      "six ratios — so whatever the sixth step does, it is not a "
      "norm artifact.  The PINNED object (the sector-normalized "
      "conditional) is separately reported at the root and is exactly "
      "zero at every one of the six steps",
      norm_free2 and root_abs_contracts_d46b and root_cond_zero
      and len(rat_abs) == len(abs_drift) - 2,
      f"D46b's five steps contract monotonically = "
      f"{root_abs_contracts_d46b}; WITH the sixth step added, the root "
      f"absolute drift contracts monotonically = {root_abs_contracts}; "
      f"ratio sequence = {[f'{float(x):.4f}' for x in rat_abs]}; "
      f"norm-free over all {len(rat_abs)} ratios = {norm_free2}; the "
      f"root CONDITIONAL drift is exactly zero at all "
      f"{len(cond_drift)} steps = {root_cond_zero}")
if not root_abs_contracts:
    outcome("HZ2-ROOT-REVERSAL",
            "D46b MB3-e's 'the root drift contracts monotonically out "
            "to r = 6' DOES NOT SURVIVE r = 7.  The root's absolute "
            f"L-infinity drift runs {frl(abs_drift)} — falling through "
            f"the five steps D46b could compute and then RISING by a "
            f"factor {rat_abs[-1]} (~{float(rat_abs[-1]):.3f}) at the "
            "one step it could not.  The reversal is exact, is "
            "identical in all three norms, and is the same shape as "
            "the reversal D46b's own round 1 found in the growth "
            "column (peak at D = 5, turn down at D = 6): a "
            "finite-horizon quantity read as a trend over five points "
            "turns at the sixth.  WHAT IT DOES NOT TOUCH: the PINNED "
            "object.  The sector-normalized conditional at the root is "
            "exactly zero at every step including r = 6 -> 7, and "
            "every OFF-ROOT depth stratum contracts in all five norms "
            "(HZ2-a).  So the object that reverses is the "
            "horizon-BOUND absolute kernel — precisely the quantity "
            "D44f says is horizon-bound.  ROUND-1 MAJOR 3, SAID "
            "AGAINST THIS RECEIPT: that the pinned object stays 0 here "
            "is NOT a consolation and carries no evidence of "
            "stability — HZ3-s1/HZ3-s2 gate the root conditional as "
            "FORCED to 0 by the root menu's orbit structure under the "
            "layer's own automorphisms, so it would have stayed 0 "
            "whatever the absolute kernel did.  What the reversal "
            "shows is that a monotonicity read off five finite-horizon "
            "points turned at the sixth.  Reported here rather than "
            "smoothed: the campaign's rule is that a surprise IS the "
            "result.")

# the window question: D46b's window vs this receipt's wider one
wider = []
for i, r in enumerate([1, 2, 3, 4]):
    a = uni_sup_a[i]
    b = max(CELLS2[(r, L)][0] for (rr, L) in CELLS2 if rr == r)
    wider.append((r, a, b, b > a))
print("  WINDOW DEPENDENCE, gated because a sup over a bigger family is "
      "a different number: D46b's window (len(h) + r <= 5) vs this "
      "receipt's (len(h) + r <= 6):")
for r, a, b, grew in wider:
    print(f"      r = {r}: D46b window sup {a} (~{float(a):.3e})  vs  "
          f"extended window sup {b} (~{float(b):.3e})   larger on the "
          f"wider window = {grew}")
window_grows = [g for r, a, b, g in wider]

check("HZ2-a THE DRIFT CONTRACTS OVER THE COMPUTED HORIZONS AT EVERY "
      "OFF-ROOT HISTORY DEPTH, two-actor arm, in all five norms — the "
      "window-controlled statement, which is the one the pin's "
      "falsifier 2 ('the root is not the family') actually tests, and "
      "which the family-uniform sequence alone cannot supply because "
      "its window shrinks with r.  **THE ROOT ROW IS EXCLUDED FROM "
      "THIS PREDICATE ON PURPOSE AND THE EXCLUSION IS STATED HERE, NOT "
      "BURIED: the root is HZ2-d's subject, where its behaviour is "
      "delivered in the direction it lands, and every failing row in "
      "this table is printed below whether or not the predicate counts "
      "it.**  A leading EXACT zero counts as stronger than contraction "
      "and contraction is read strictly from the first nonzero term, "
      "which is D46b's own framing of the root row.  This is a TABLE, "
      "not a rate and not a limit: no fit, no extrapolation and no "
      "threshold is applied to it anywhere in this receipt, and "
      "whether it is more than a table is HZ4's question",
      not ROW_BAD_OFFROOT and RS2 == list(range(1, CAP_T + 1))
      and len(ROWS2) == len(NORMS) * len(LS2),
      f"depth-stratified rows checked = {len(ROWS2)} "
      f"({len(NORMS)} norms x {len(LS2)} depths); OFF-ROOT rows that do "
      f"NOT contract = {ROW_BAD_OFFROOT if ROW_BAD_OFFROOT else 'none'};"
      f" ROOT rows that do not contract (HZ2-d's subject, counted here "
      f"only as a printed fact) = "
      f"{ROW_BAD_ROOT if ROW_BAD_ROOT else 'none'}; family-uniform rows "
      f"contract = "
      + ", ".join(f"{nm}: {uni_contracts[nm]}" for nm in NORMS))

check("HZ2-b THE SUP IS WINDOW-DEPENDENT, AND BOTH WINDOWS ARE PRINTED "
      "SIDE BY SIDE RATHER THAN ONE OF THEM QUOTED.  A family-uniform "
      "sup over a deeper family can only be >= the shallower one, so "
      "D46b's committed four-term sequence is a LOWER BOUND on the sup "
      "over this receipt's deeper family; treating it as window-free "
      "would be the horizon-mismatch error D46b's own round 1 convicted "
      "in the other direction.  The gate requires the committed values "
      "to be exactly the shallow-window column AND records, in the "
      "direction it lands, at which r the extra depth moves the sup",
      [a for r, a, b, g in wider] == uni_sup_a
      and all(b >= a for r, a, b, g in wider) and len(wider) == 4,
      f"sup grew on the wider window at r = "
      f"{[r for r, a, b, g in wider if g] or 'no r'}; unchanged at "
      f"r = {[r for r, a, b, g in wider if not g] or 'no r'}; extended "
      f"column = {frl([b for r, a, b, g in wider])}")

# ---- wider actor pools ----------------------------------------------
print(f"\n{sec()}   HZ2 IN ACTOR POOL — the pin's falsifier 4 ('if the "
      f"drift's contraction rate degrades systematically with actor "
      f"pool, the two-actor arm was measuring ARM-1T and not "
      f"transport').  Pools are EXACT and exhaustive at the printed "
      f"depths; no sampled arm is used.")
print(f"  ROUND-1 MAJOR 1: THE FOUR-ACTOR POOL IS BUILT TO DEPTH "
      f"{CAP_4}.  The first delivery stopped at depth 3, where the "
      f"L = 1 row has only TWO terms, and delivered its headline on "
      f"that two-term row while naming the depth-4 computation as 'the "
      f"cheapest thing in the campaign and the one that would re-grade "
      f"the headline'.  It is computed here.")
POOLS = [("2 actors (A,B)", AB, CAP_T, CACHE, GT)]
_t = time.time()
C3 = build(ABC, CAP_3)
_lv = defaultdict(int)
for h in C3:
    _lv[len(h)] += 1
CM3 = [sum(_lv[j] for j in range(k + 1)) for k in range(CAP_3 + 1)]
_T3BUILD = time.time() - _t
print(f"{sec()}     3 actors (A,B,C): exhaustive to depth {CAP_3} in "
      f"{_T3BUILD:.1f}s, cumulative {CM3}  [FULL MENUS at every depth]")
POOLS.append(("3 actors (A,B,C)", ABC, CAP_3, C3, rel_potential(C3)))

_t = time.time()
C4, DEEP4 = build_leaf(ABCD, CAP_4)
_lv = defaultdict(int)
for h in C4:
    _lv[len(h)] += 1
CM4 = [sum(_lv[j] for j in range(k + 1)) for k in range(CAP_4 + 1)]
_T4BUILD = time.time() - _t
print(f"{sec()}     4 actors (A,B,C,D): exhaustive to depth {CAP_4} in "
      f"{_T4BUILD:.1f}s SERIAL, SINGLE-CORE, cumulative {CM4}; the "
      f"deepest layer is {DEEP4} histories held as their exact "
      f"menu-weight totals (the declared LEAF collapse, controlled at "
      f"HZ2-f).  Per level {[_lv[k] for k in sorted(_lv)]}")
POOLS.append(("4 actors (A,B,C,D)", ABCD, CAP_4, C4, rel_potential(C4)))
check("HZ2-POOL4 THE FOUR-ACTOR DEPTH-4 LEVEL IS THE PRICED ONE.  The "
      "first delivery's §10 residue 1 estimated '318,704 more "
      "histories'; the level is enumerated here and its size is "
      "reported in the direction it lands, together with the serial "
      "wall clock so the cost claim can be audited rather than trusted",
      CM4[:4] == [1, 25, 593, 13993] and DEEP4 == 318704
      and CM4[4] == 13993 + 318704,
      f"four-actor cumulative census = {CM4}; depth-4 level = {DEEP4}; "
      f"serial build wall clock = {_T4BUILD:.1f}s "
      f"(~{_T4BUILD / max(DEEP4, 1) * 1000:.2f} ms per depth-4 menu)")

POOLCELLS = {}
for nm, actors, cap, c, G in POOLS:
    POOLCELLS[nm] = drift_cells(c, G, cap)

# ---- HZ2-f: the leaf collapse, controlled like for like -------------
C3COL = collapse_deepest(C3, CAP_3)
CELLS3_COL = drift_cells(C3COL, rel_potential(C3COL), CAP_3)
collapse_exact = (set(CELLS3_COL) == set(POOLCELLS["3 actors (A,B,C)"])
                  and all(CELLS3_COL[k]
                          == POOLCELLS["3 actors (A,B,C)"][k]
                          for k in CELLS3_COL))
check("HZ2-f THE DEEPEST-LAYER LEAF COLLAPSE CHANGES NO NUMBER, "
      "CONTROLLED LIKE FOR LIKE ON A POOL WHERE BOTH ARE AFFORDABLE.  "
      "The four-actor depth-4 layer is stored as its exact menu-weight "
      "total, because the AST-lifted recursion has G(h, 0) = 1 and can "
      "therefore only ever ask a deepest-layer history for "
      "G(h, 1) = sum_e q(e|h).  Asserting that would be a modelling "
      "claim, so it is GATED instead: the THREE-actor pool is built "
      "with full menus at depth 4 AND with the same collapse, both are "
      "pushed through the identical drift_cells, and every one of the "
      "five norms in every (r, L) cell must agree as an exact rational. "
      "If the collapse lost anything, this gate is where it would show",
      collapse_exact and len(CELLS3_COL) == len(POOLCELLS[POOLS[1][0]]),
      f"cells compared = {len(CELLS3_COL)} x {len(NORMS)} norms; "
      f"disagreements = "
      f"{sum(1 for k in CELLS3_COL if CELLS3_COL[k] != POOLCELLS[POOLS[1][0]][k])}")

MATCHED = sorted(set(POOLCELLS[POOLS[0][0]])
                 & set(POOLCELLS[POOLS[1][0]])
                 & set(POOLCELLS[POOLS[2][0]]))
print(f"  MATCHED-CELL COMPARISON (same relative horizon r, same "
      f"history depth L, three pools), IN ALL FIVE NORMS — ROUND-1 "
      f"MAJOR 2: the first delivery tabulated the cross-pool comparison "
      f"for norm index 0 only, so THE PINNED OBJECT WAS NEVER "
      f"TABULATED ACROSS ACTOR POOLS ANYWHERE IN THE UNIT, which is "
      f"precisely what the pin's falsifier 4 asks about.  It is "
      f"tabulated here.  The deeper four-actor cap also widens the "
      f"matched set from 5 cells to {len(MATCHED)}:")
for j, nm in enumerate(NORMS):
    tagj = "  <-- THE PINNED OBJECT" if j >= 3 else "  (context: "\
        "horizon-bound absolute kernel, D44f)"
    print(f"    norm = {nm}{tagj}")
    print("      (r, L) | " + " | ".join(n2 for n2, *_ in POOLS))
    for (r, L) in MATCHED:
        print(f"      ({r}, {L}) | " + " | ".join(
            str(POOLCELLS[n2][(r, L)][j]) for n2, *_ in POOLS))
print("  family-uniform sup per pool, at the horizons each pool's cap "
      "can reach (the windows DIFFER and the rows are not comparable "
      "across pools except in the matched cells above):")
POOLUNI = {}
for nm, actors, cap, c, G in POOLS:
    rs = sorted({r for r, L in POOLCELLS[nm]})
    row = [max(POOLCELLS[nm][(r, L)][0] for (rr, L) in POOLCELLS[nm]
               if rr == r) for r in rs]
    POOLUNI[nm] = (rs, row)
    print(f"      {nm:20s} depth {cap}: "
          + ", ".join(f"r={rs[i]}->{rs[i] + 1}: {row[i]}"
                      for i in range(len(row))))
POOLROWBAD = {}
POOLROWBAD_OFF = {}
POOLROWBAD_OFF_PIN = {}
POOLROWBAD_OFF_ABS = {}
POOLSEQ = {}
for nm, actors, cap, c, G in POOLS:
    bad = []
    for j in range(len(NORMS)):
        for L in sorted({L for r, L in POOLCELLS[nm]}):
            rs = sorted({r for r, LL in POOLCELLS[nm] if LL == L})
            seq = [POOLCELLS[nm][(r, L)][j] for r in rs]
            POOLSEQ[(nm, NORMS[j], L)] = (rs, seq)
            if not contracts_from_first_nonzero(seq):
                bad.append((NORMS[j], L))
    POOLROWBAD[nm] = bad
    POOLROWBAD_OFF[nm] = [(n2, L) for n2, L in bad if L > 0]
    POOLROWBAD_OFF_PIN[nm] = [(n2, L) for n2, L in POOLROWBAD_OFF[nm]
                              if 'CONDITIONAL' in n2]
    POOLROWBAD_OFF_ABS[nm] = [(n2, L) for n2, L in POOLROWBAD_OFF[nm]
                              if 'CONDITIONAL' not in n2]
print("  depth-stratified rows that do NOT contract, per pool "
      "(norm, depth L) — printed in full, root rows included, and "
      "SPLIT BY OBJECT (ROUND-1 MAJOR 2: the pinned sector-normalized "
      "conditional is the headline object, the absolute kernel is "
      "horizon-bound D44f context — one doctrine, one direction, "
      "everywhere in this receipt):")
for nm, actors, cap, c, G in POOLS:
    print(f"      {nm:20s}: ALL = "
          f"{POOLROWBAD[nm] if POOLROWBAD[nm] else 'none'}")
    print(f"      {'':20s}  PINNED OBJECT, off-root = "
          f"{POOLROWBAD_OFF_PIN[nm] if POOLROWBAD_OFF_PIN[nm] else 'NONE'}"
          f"   |   ABSOLUTE (context), off-root = "
          f"{POOLROWBAD_OFF_ABS[nm] if POOLROWBAD_OFF_ABS[nm] else 'none'}")
print("  THE FOUR-ACTOR L = 1 ROW IN ALL FIVE NORMS, THE ROW THE FIRST "
      "DELIVERY'S HEADLINE RESTED ON, NOW WITH ITS THIRD TERM.  The "
      "pinned rows are printed BESIDE the absolute ones, which the "
      "first delivery never did:")
P4 = POOLS[2][0]
BLIP = {}
for j, nm2 in enumerate(NORMS):
    rs, seq = POOLSEQ[(P4, nm2, 1)]
    steps = [(seq[i] / seq[i - 1] - 1) for i in range(1, len(seq))]
    BLIP[nm2] = (rs, seq, steps)
    print(f"      {nm2:22s}: "
          + ", ".join(f"r={rs[i]}->{rs[i] + 1}: {seq[i]} "
                      f"(~{float(seq[i]):.6e})" for i in range(len(seq)))
          + "   step changes "
          + ", ".join(f"{float(x) * 100:+.2f}%" for x in steps)
          + (f"   t3 vs t1 = "
             f"{float(seq[-1] / seq[0] - 1) * 100:+.2f}%"
             if len(seq) >= 3 else ""))
_r3, _s3 = POOLSEQ[(POOLS[1][0], NORMS[0], 0)]
print("  AND THE PRECEDENT THE UNIT ALREADY HELD, at three actors, in "
      "the ROOT row of the same norm — a rise at step 2 followed by a "
      "fall at step 3, i.e. a two-term rise was ALREADY known inside "
      "this family to be non-diagnostic:")
print(f"      3 actors, L-inf absolute, L = 0: {frl(_s3)}"
      + "   step changes "
      + ", ".join(f"{float(_s3[i] / _s3[i - 1] - 1) * 100:+.2f}%"
                  for i in range(1, len(_s3)) if _s3[i - 1] != 0))
blip_rows = [nm2 for nm2 in NORMS if 'CONDITIONAL' not in nm2]
blip_shape = all(len(BLIP[nm2][1]) >= 3 and BLIP[nm2][2][0] > 0
                 and BLIP[nm2][2][1] < 0 for nm2 in blip_rows)
blip_below_first = [nm2 for nm2 in blip_rows
                    if BLIP[nm2][1][-1] < BLIP[nm2][1][0]]
pin_rows_contract_4 = all(
    contracts_from_first_nonzero(BLIP[nm2][1])
    for nm2 in NORMS if 'CONDITIONAL' in nm2)
check("HZ2-BLIP THE FOUR-ACTOR RISE IS A ONE-STEP BLIP THAT REVERSES AT "
      "THE VERY NEXT HORIZON — ROUND-1 MAJOR 1, THE FIRST DELIVERY'S "
      "HEADLINE RE-GRADED BY ITS OWN NAMED COMPUTATION.  At depth 3 the "
      "four-actor L = 1 row had exactly two terms and rose between "
      "them; at depth 4 it has three, and it FALLS in every absolute "
      "norm at r = 3 -> 4, ending BELOW its first term in L-infinity "
      "and in L1.  The gate requires the shape to be exactly that — up "
      "at the first step, down at the second — and reports which norms "
      "end below their first term.  Meanwhile THE PINNED OBJECT never "
      "rose at all: both conditional norms contract strictly at every "
      "one of the three steps.  The honest description of the "
      "four-actor pool is therefore CONTRACTION, with a two-term blip "
      "in a horizon-bound context statistic",
      blip_shape and pin_rows_contract_4 and len(blip_below_first) >= 2,
      "; ".join(f"{nm2}: {frl(BLIP[nm2][1])} "
                f"[{', '.join(f'{float(x) * 100:+.2f}%' for x in BLIP[nm2][2])}]"
                for nm2 in NORMS)
      + f"; absolute norms ending BELOW their first term = "
      f"{blip_below_first}; pinned rows contract strictly = "
      f"{pin_rows_contract_4}")
print("  and the EXACT SEQUENCES of every OFF-ROOT row that does not "
      "contract, printed in place because this is the pin's HZ-I "
      "clause (c) and it must not be quoted as a boolean:")
OFFROW_DETAIL = []
for nm, actors, cap, c, G in POOLS:
    for n2, L in POOLROWBAD_OFF[nm]:
        j = NORMS.index(n2)
        rs, seq = POOLSEQ[(nm, n2, L)]
        rise = max((seq[i] / seq[i - 1] - 1
                    for i in range(1, len(seq)) if seq[i] > seq[i - 1]),
                   default=Fr(0))
        OFFROW_DETAIL.append((nm, n2, L, cap, rs, seq, rise))
        print(f"      {nm}, norm {n2}, depth L = {L}: "
              + ", ".join(f"r={rs[i]}->{rs[i] + 1}: {seq[i]} "
                          f"(~{float(seq[i]):.6e})"
                          for i in range(len(seq)))
              + f"   largest rise = {rise} (~{float(rise) * 100:.2f}%)"
              + ("   [PINNED OBJECT]" if 'CONDITIONAL' in n2 else
                 "   [absolute kernel — D44f context, NOT the verdict "
                 "object]"))
if not OFFROW_DETAIL:
    print("      none — every off-root row contracts at every pool")
pool_contracts = {nm: contracts_from_first_nonzero(POOLUNI[nm][1])
                  for nm in POOLUNI}
pool_mono_in_width = all(
    POOLCELLS[POOLS[0][0]][(r, L)][0] <= POOLCELLS[POOLS[1][0]][(r, L)][0]
    for (r, L) in MATCHED)
pool_pin_falls = all(
    POOLCELLS[POOLS[0][0]][(r, L)][3] >= POOLCELLS[POOLS[2][0]][(r, L)][3]
    for (r, L) in MATCHED if POOLCELLS[POOLS[0][0]][(r, L)][3] != 0)
check("HZ2-c POOL DEPENDENCE, TAKEN ON THE PINNED OBJECT AND ON NOTHING "
      "ELSE — ROUND-1 MAJOR 2, THE DOCTRINE APPLIED IN ONE DIRECTION.  "
      "The pin's §6 and §2 say in terms that the pinned object is the "
      "SECTOR-NORMALIZED CONDITIONAL and that absolute completed "
      "weights are horizon-bound (D44f) CONTEXT.  The first delivery "
      "enforced that at HZ3-b, in capitals, and then folded the "
      "absolute rows into THIS gate's boolean, which is the direction "
      "that maximised the delivered negative.  Here one doctrine runs "
      "in one direction: the verdict is taken on the pinned conditional "
      "at every pool, and the absolute rows are printed in full beside "
      "it and are NOT folded in.  The pin's falsifier 4 asks whether "
      "contraction degrades with actor pool; the drift is compared "
      "across pools ONLY at identical (r, L), in all five norms, and "
      "the answer is recorded in the direction it lands.  As at HZ2-a "
      "the ROOT row is excluded from the predicate — at every pool it "
      "is the symmetry identity of HZ0-7 in the pinned object and the "
      "horizon-bound quantity of HZ2-d in the absolute one",
      all(not POOLROWBAD_OFF_PIN[nm] for nm in POOLROWBAD_OFF_PIN)
      and len(POOLUNI) == 3
      and all((r, L) in POOLCELLS[nm] for (r, L) in MATCHED
              for nm, *_ in POOLS),
      "PINNED-OBJECT off-root rows contract at every pool: "
      + ", ".join(f"{nm} = {not POOLROWBAD_OFF_PIN[nm]}"
                  for nm in POOLROWBAD_OFF_PIN)
      + "; ABSOLUTE (context) off-root rows that do not contract: "
      + ", ".join(f"{nm} = {POOLROWBAD_OFF_ABS[nm] or 'none'}"
                  for nm in POOLROWBAD_OFF_ABS)
      + "; family-uniform rows contract: "
      + ", ".join(f"{nm} = {pool_contracts[nm]}" for nm in POOLUNI)
      + f"; matched cells = {len(MATCHED)} at {MATCHED}; drift at 3 "
      f"actors >= drift at 2 actors in every matched cell = "
      f"{pool_mono_in_width}; the PINNED drift at 4 actors <= at 2 "
      f"actors in every matched cell where it is nonzero = "
      f"{pool_pin_falls}")

# ======================================================================
# HZ3 — TRUNCATION-CONVENTION INDEPENDENCE (the horn gate)
# ======================================================================
print(f"\n{sec()} [HZ3 — TRUNCATION-CONVENTION INDEPENDENCE (the horn "
      f"gate)]")
print("  THE CONVENTIONS, DECLARED, and one correction to the pin's own")
print("  suggested pattern, made in place.  The pin proposes 'the")
print("  committed one, plus a second — e.g. the D57 S4 pattern of a")
print("  maximally coarse terminal'.  But the COMMITTED terminal IS")
print("  already the maximally coarse one: G(h, 0) = 1 is")
print("  state-independent, it gives every terminal history the same")
print("  value, and there is nothing coarser.  The S4 pattern therefore")
print("  INVERTS here: a second convention has to REFINE the terminal,")
print("  not coarsen it.  Two are declared and both are carried")
print("  independently through the whole computation:")
print("    C1 (COMMITTED, D46b): G(h, 0) = 1.  Maximally coarse.")
print("    C2 (BRANCH-COUNT TERMINAL): G(h, 0) = |menu(h)|, the number")
print("       of admissible continuations.  Counting measure at the")
print("       cap layer instead of uniform measure — a genuinely")
print("       different completion of the truncation, and NOT a")
print("       reparametrization of C1.")
print("    C3 (MENU-MASS TERMINAL): G(h, 0) = sum_e q(e|h).  DECLARED")
print("       AND GATED TO BE A HORIZON SHIFT of C1 — it can never")
print("       separate, and it is carried precisely so that C2's")
print("       separation cannot be mistaken for one.")


def make_G(cache, term):
    memo = {}

    def G(h, r):
        if r == 0:
            return term(h)
        key = (h, r)
        v = memo.get(key)
        if v is None:
            v = sum(q * G(h + (e,), r - 1) for e, q in cache[h])
            memo[key] = v
        return v
    return G


G_C1 = make_G(CACHE, lambda h: Fr(1))
G_C2 = make_G(CACHE, lambda h: Fr(len(CACHE[h])))
G_C3 = make_G(CACHE, lambda h: sum(q for e, q in CACHE[h]))

c1_eq_ast = all(G_C1(ROOT, r) == GT(ROOT, r) for r in range(1, CAP_T + 2))
c3_shift = all(G_C3(ROOT, r) == GT(ROOT, r + 1)
               for r in range(0, CAP_T + 1))
c3_kernel_shift = True
for h in CACHE:
    if len(h) + 2 > CAP_T:
        continue
    for r in (1, 2):
        if len(h) + r > CAP_T:
            continue
        if krel(CACHE, G_C3, h, r) != krel(CACHE, G_C1, h, r + 1):
            c3_kernel_shift = False
check("HZ3-a THE CONVENTIONS ARE WHAT THEY ARE DECLARED TO BE.  C1 "
      "reproduces the AST-lifted D46b potential value for value at the "
      "root; C3's potential equals C1's at one higher horizon at every "
      "horizon, and C3's KERNEL at horizon r equals C1's at horizon "
      "r + 1 entrywise over the family — so C3 is exactly a relabelling "
      "of the horizon index and is excluded from the horn comparison "
      "by construction, not by preference",
      c1_eq_ast and c3_shift and c3_kernel_shift,
      f"C1 == D46b's G at r = 1..{CAP_T + 1}: {c1_eq_ast}; "
      f"C3(r) == C1(r+1): {c3_shift}; C3's kernel == C1's shifted "
      f"kernel entrywise: {c3_kernel_shift}")

# ---------------------------------------------------------------------
# HZ3-s — ROUND-1 MAJOR 3: THE ROOT LEG IS A THEOREM, GATED.
# ---------------------------------------------------------------------
print("  ROUND-1 MAJOR 3, THE ROOT LEG RE-GRADED FROM [MEASURED] TO "
      "[THEOREM].  The first delivery presented 'the pinned object "
      "separates NOWHERE at the root, exactly 0 at every horizon' as "
      "the measured half of an object-dependence finding — something "
      "that could have come out otherwise.  It could not.  The layer "
      "carries exact relabelling symmetries, the root menu is a single "
      "orbit per event kind under them, and therefore ANY equivariant "
      "terminal forces the uniform-within-kind conditional at the root "
      "at every horizon.  Gated in three steps rather than asserted:")
_SWA = {'A': 'B', 'B': 'A'}


def make_sigma(swap_actor, swap_bit):
    """The relabelling action on the committed layer's own event and
    version algebra.  Versions are rebuilt exactly as vname/mname build
    them (sorted value tuple, sorted author tuple, sorted merge pair),
    so the image of a legal name is a legal name."""
    def sa(a):
        return _SWA[a] if swap_actor else a

    def sb(x):
        return (1 - x) if swap_bit else x

    def sv(v):
        if v == V0:
            return v
        if v[1] == 'm':
            pk = tuple(sorted((sv(v[2][0]), sv(v[2][1])), key=repr))
            val = v[3]
            return ('v', 'm', pk,
                    None if val is None
                    else tuple(sorted(sb(x) for x in val)), sa(v[4]))
        return ('v', sv(v[1]), tuple(sorted(sb(x) for x in v[2])),
                tuple(sorted(sa(a) for a in v[3])), sa(v[4]))

    def st(t):
        return (sa(t[0]), sv(t[1]), sb(t[2]))

    def se(e):
        k = e[0]
        if k == 'p':
            return ('p', sa(e[1]), sv(e[2]), sb(e[3]))
        if k == 'n':
            return ('n', sa(e[1]))
        if k == 'd':
            return ('d', sa(e[1]), sa(e[2]), sv(e[3]))
        if k == 'r':
            return ('r', sa(e[1]), frozenset(st(x) for x in e[2]),
                    frozenset(st(x) for x in e[3]))
        if k == 'm':
            pk = tuple(sorted((sv(e[2][0]), sv(e[2][1])), key=repr))
            return ('m', sa(e[1]), pk,
                    'both' if e[3] == 'both' else sv(e[3]))
        raise ValueError(k)

    def sh(h):
        return tuple(se(x) for x in h)
    return se, sh


SYM_DEPTH = 3
SYMS = (("A <-> B (actor relabelling)", 1, 0),
        ("0 <-> 1 (proposal-value relabelling)", 0, 1),
        ("both together", 1, 1))
SYMRES = []
for _snm, _swa, _swb in SYMS:
    _se, _sh = make_sigma(_swa, _swb)
    nviol = miss = ntot = 0
    for h in CACHE:
        if len(h) > SYM_DEPTH:
            continue
        ntot += 1
        g = _sh(h)
        if g not in CACHE:
            miss += 1
            continue
        # SET comparison, never sorted-by-repr: two EQUAL frozensets can
        # have different reprs in the same process, so a repr sort is
        # not a safe multiset test.
        if (set((_se(e), q) for e, q in CACHE[h]) != set(CACHE[g])
                or len(CACHE[h]) != len(CACHE[g])):
            nviol += 1
    SYMRES.append((_snm, ntot, miss, nviol))
    print(f"      {_snm:38s}: {ntot} histories of depth <= {SYM_DEPTH}, "
          f"images outside the family = {miss}, menus not carried "
          f"across = {nviol}")
_seF, _shF = make_sigma(1, 1)
gviol = gtot = 0
GTOT_EXPECT = sum(CAP_T + 1 - len(h) for h in CACHE
                  if len(h) <= SYM_DEPTH)
for h in CACHE:
    if len(h) > SYM_DEPTH:
        continue
    for r in range(1, CAP_T + 2 - len(h)):
        gtot += 1
        if GT(h, r) != GT(_shF(h), r):
            gviol += 1
sym_clean = all(m == 0 and v == 0 for nm2, n2, m, v in SYMRES)
check("HZ3-s1 THE RELABELLINGS ARE EXACT AUTOMORPHISMS OF THE COMMITTED "
      "LAYER.  Relabelling a history and relabelling its menu give the "
      "same (event, weight) multiset, for the actor swap alone, for the "
      "proposal-value swap alone and for the two together, over every "
      "history of depth <= 3; the family is closed under all three; and "
      "the AST-lifted potential G(h, r) is invariant, at every history "
      "of depth <= 3 and every horizon that history can reach.  This is "
      "a fact about the layer, obtained without touching it",
      sym_clean and gviol == 0 and gtot == GTOT_EXPECT,
      "; ".join(f"{nm2}: {n2} histories, {m} images missing, {v} menu "
                f"violations" for nm2, n2, m, v in SYMRES)
      + f"; G(h, r) == G(sigma h, r) over {gtot} (history, horizon) "
      f"pairs with {gviol} violations")

_seA, _ = make_sigma(1, 0)
_seB, _ = make_sigma(0, 1)


def orbit_of(e):
    S = {e}
    while True:
        T = S | {_seA(x) for x in S} | {_seB(x) for x in S}
        if T == S:
            return S
        S = T


ROOTKINDS = defaultdict(set)
for e, q in CACHE[ROOT]:
    ROOTKINDS[e[0]].add(e)
ORBIT_OK = all(orbit_of(sorted(v, key=repr)[0]) == v
               for v in ROOTKINDS.values())
print("      the root menu, by kind, and its orbit under the group the "
      "two relabellings generate:")
for k in sorted(ROOTKINDS):
    reps = sorted(ROOTKINDS[k], key=repr)
    print(f"        kind '{k}': {len(ROOTKINDS[k])} options, orbit of "
          f"one of them has size {len(orbit_of(reps[0]))} -> single "
          f"orbit = {orbit_of(reps[0]) == ROOTKINDS[k]}")

# C5 (the first delivery's own residue 4) and C4 (non-equivariant)
G_C5 = make_G(CACHE, lambda h: Fr(1 + len({e[0] for e, q in CACHE[h]})))
G_C4 = make_G(CACHE,
              lambda h: Fr(2) if (h and h[-1][1] == 'A') else Fr(1))
TERMS = (("C1 committed", G_C1), ("C2 branch-count", G_C2),
         ("C3 menu-mass", G_C3), ("C5 sector-weighted (residue 4)",
                                  G_C5),
         ("C4 ACTOR-ASYMMETRIC (NON-equivariant)", G_C4))
ROOTUNIF = {}
ROOTSEP = {}
for tnm, GG in TERMS:
    unif = []
    csep = []
    asep = []
    for r in range(1, CAP_T + 1):
        kk = krel(CACHE, GG, ROOT, r)
        cc = conditional(kk)
        byk = defaultdict(list)
        for e, v in cc.items():
            byk[e[0]].append(v)
        unif.append(all(len(set(v)) == 1 for v in byk.values()))
        k1 = krel(CACHE, G_C1, ROOT, r)
        csep.append(max(abs(cc[e] - conditional(k1)[e]) for e in k1))
        asep.append(max(abs(kk[e] - k1[e]) for e in k1))
    ROOTUNIF[tnm] = unif
    ROOTSEP[tnm] = (csep, asep)
    print(f"      {tnm:40s}: root conditional uniform WITHIN EVERY "
          f"KIND at r = 1..{CAP_T} = {all(unif)};  separation from C1 "
          f"in the PINNED object = {frl(csep)};  in the absolute "
          f"kernel = {frl(asep)}")
equiv_unif = all(all(ROOTUNIF[t]) for t in ROOTUNIF
                 if not t.startswith('C4'))
c4_breaks = ROOTSEP['C4 ACTOR-ASYMMETRIC (NON-equivariant)'][0][0] != 0
check("HZ3-s2 THE ROOT'S EXACT ZERO IS FORCED, FOR EVERY EQUIVARIANT "
      "TERMINAL — THEOREM OF THE CONSTRUCTION.  Each event kind in the "
      "root menu is a SINGLE ORBIT of the group HZ3-s1 gates "
      "({p(A,v0,0), p(A,v0,1), p(B,v0,0), p(B,v0,1)}, {d(A,B,v0), "
      "d(B,A,v0)}, {n(A), n(B)}), so an invariant potential gives every "
      "option in a kind the same completed weight and the "
      "sector-normalized conditional is uniform within kind at EVERY "
      "horizon and under EVERY equivariant terminal.  Four such "
      "terminals are pushed through and all four give uniform-in-kind "
      "root conditionals and separation exactly 0 from C1 at the root, "
      "INCLUDING C5 — which is precisely the first delivery's own §10 "
      "residue 4 ('a third that refines differently, e.g. a "
      "sector-weighted terminal').  So residue 4 as written could not "
      "have sharpened anything: it reproduces the same tautology.  The "
      "absolute separations are nonzero and are printed beside it",
      ORBIT_OK and equiv_unif
      and all(x == 0 for x in ROOTSEP['C5 sector-weighted (residue 4)'][0])
      and all(x != 0 for x in ROOTSEP['C5 sector-weighted (residue 4)'][1]),
      f"root menu kinds and sizes = "
      f"{ {k: len(v) for k, v in sorted(ROOTKINDS.items())} }; every "
      f"kind is one orbit = {ORBIT_OK}; equivariant terminals give a "
      f"uniform-in-kind root conditional = {equiv_unif}; C5 root "
      f"conditional separation from C1 = "
      f"{frl(ROOTSEP['C5 sector-weighted (residue 4)'][0])}; C5 root "
      f"ABSOLUTE separation = "
      f"{frl(ROOTSEP['C5 sector-weighted (residue 4)'][1])}",
      theorem="root-menu orbit structure x terminal equivariance; no "
              "equivariant terminal can give a nonzero root conditional "
              "separation")
check("HZ3-s3 AND THE INVARIANCE BREAKS THE MOMENT EQUIVARIANCE IS "
      "DROPPED — the falsification test the pin's HZ3 asks for, run.  "
      "C4 is a legitimate function of the terminal history's own state "
      "(G(h, 0) = 2 if the last event's actor is A, else 1), strictly "
      "positive, and NOT equivariant.  Its root conditional separates "
      "from C1 immediately.  So HZ3-s2's zero is a statement about the "
      "SYMMETRY CLASS of the terminal and not about horizons, and the "
      "honest successor residue is a NON-EQUIVARIANT terminal, not "
      "another equivariant one",
      c4_breaks
      and not ROOTUNIF['C4 ACTOR-ASYMMETRIC (NON-equivariant)'][0],
      f"C4 root conditional separation from C1, r = 1..{CAP_T} = "
      f"{frl(ROOTSEP['C4 ACTOR-ASYMMETRIC (NON-equivariant)'][0])}; C4 "
      f"root absolute separation = "
      f"{frl(ROOTSEP['C4 ACTOR-ASYMMETRIC (NON-equivariant)'][1])}")

print("  THE HORN COMPARISON: k^C1_r(e|h) vs k^C2_r(e|h), ENTRYWISE in "
      "exact Fractions, at MATCHED relative horizon.  C2's potential "
      f"needs the menu one level deeper than C1's, so the comparison "
      f"runs at len(h) + r <= {CAP_T}.  AS AT HZ2, THE WINDOW-CONTROLLED "
      "TABLE COMES FIRST: a family-wide sup at horizon r is taken over "
      "a window that SHRINKS with r, so a family-wide sequence falling "
      "in r proves nothing on its own.  The rows below fix the history "
      "depth L and vary r.")
HORNC = {}
for r in range(1, CAP_T + 1):
    for L in range(0, CAP_T + 1 - r):
        hs = [h for h in CACHE if len(h) == L]
        if not hs:
            continue
        ba = bc = Fr(0)
        neq = 0
        for h in hs:
            a = krel(CACHE, G_C1, h, r)
            b = krel(CACHE, G_C2, h, r)
            neq += int(a == b)
            ba = max(ba, linf(a, b))
            bc = max(bc, linf(conditional(a), conditional(b)))
        HORNC[(r, L)] = (len(hs), neq, ba, bc)
HLS = sorted({L for r, L in HORNC})
HRS = sorted({r for r, L in HORNC})
for nm, idx in (("L-inf (abs kernel)", 2), ("L-inf (CONDITIONAL)", 3)):
    print(f"    sup |k^C1_r - k^C2_r| over depth-L histories, "
          f"norm = {nm}:")
    for L in HLS:
        seq = [HORNC[(r, L)][idx] for r in HRS if (r, L) in HORNC]
        print(f"      L = {L}: " + ", ".join(
            f"r={HRS[i]}: {seq[i]}" for i in range(len(seq))))
HROWS = {(nm, L): [HORNC[(r, L)][idx] for r in HRS if (r, L) in HORNC]
         for nm, idx in (("abs", 2), ("cond", 3)) for L in HLS}
HROW_BAD = sorted([k for k in HROWS
                   if not contracts_from_first_nonzero(HROWS[k])],
                  key=repr)
HROW_BAD_OFF = [(nm, L) for nm, L in HROW_BAD if L > 0]
HROW_BAD_ROOT = [(nm, L) for nm, L in HROW_BAD if L == 0]
print("  rows that do NOT shrink in r (norm, depth L): "
      f"{HROW_BAD if HROW_BAD else 'none'}")

print("  AND the family-wide row, with the shrinking-window caveat "
      "attached:")
HORN = {}
for r in HRS:
    n = sum(HORNC[(r, L)][0] for L in HLS if (r, L) in HORNC)
    neq = sum(HORNC[(r, L)][1] for L in HLS if (r, L) in HORNC)
    ba = max(HORNC[(r, L)][2] for L in HLS if (r, L) in HORNC)
    bc = max(HORNC[(r, L)][3] for L in HLS if (r, L) in HORNC)
    HORN[r] = (n, neq, ba, bc, (HORNC[(r, 0)][2], HORNC[(r, 0)][3]))
print("      r | histories | C1 == C2 exactly | sup L-inf (abs) | "
      "sup L-inf (CONDITIONAL) | at the root (abs, cond)")
for r in HRS:
    n, neq, ba, bc, rd = HORN[r]
    print(f"      {r} | {n:7d} | {neq:7d} | {ba} (~{float(ba):.3e}) | "
          f"{bc} (~{float(bc):.3e}) | ({rd[0]}, {rd[1]})")
horn_abs = [HORN[r][2] for r in HRS]
horn_cond = [HORN[r][3] for r in HRS]
horn_root_abs = [HORN[r][4][0] for r in HRS]
horn_root_cond = [HORN[r][4][1] for r in HRS]
horn_neq_total = sum(HORN[r][1] for r in HRS)
horn_separates = any(x != 0 for x in horn_abs)
HROW_BAD_COND = [k for k in HROW_BAD if k[0] == 'cond']
HROW_BAD_ABS = [k for k in HROW_BAD if k[0] == 'abs']
# THE HORN VERDICT IS TAKEN ON THE PINNED OBJECT (pin §6: "the pinned
# object is the SECTOR-NORMALIZED CONDITIONAL; absolute completed
# weights are horizon-bound (D44f) and are context").  The absolute
# rows are reported in full beside it and are NOT folded into it.
horn_cond_shrinks = not [k for k in HROW_BAD_COND if k[1] > 0]
horn_shrinks = horn_cond_shrinks
horn_root_cond_zero = all(x == 0 for x in horn_root_cond)
horn_root_abs_nonzero = all(x != 0 for x in horn_root_abs)
check("HZ3-b0 THE ROOT LEG OF THE HORN IS THE SAME THEOREM AS HZ0-7 — "
      "ROUND-1 MAJOR 3, split out of HZ3-b so that a forced identity is "
      "never counted as a measurement.  'The pinned object separates "
      "nowhere at the root' and 'the root conditional drift is exactly "
      "0' are ONE statement: by HZ3-s1/HZ3-s2 the root menu is a single "
      "orbit per kind and both C1 and C2 are equivariant terminals, so "
      "both give the uniform-within-kind root conditional and their "
      "difference is 0 at every horizon whatever the absolute kernels "
      "do.  It carries no information about convention independence.  "
      "The absolute root row is nonzero, which is the only content on "
      "this line and is D44f context",
      horn_root_cond_zero and horn_root_abs_nonzero,
      f"ROOT conditional separation = {frl(horn_root_cond)}; ROOT "
      f"absolute separation = {frl(horn_root_abs)}",
      theorem="root-menu symmetry x equivariance of C1 and C2 "
              "(HZ3-s2); no equivariant pair can separate at the root")
check("HZ3-b THE HORN'S CONTENT IS THE OFF-ROOT TABLE, AND OFF THE ROOT "
      "THE PINNED SEPARATION SHRINKS AT EVERY FIXED DEPTH.  Two facts, "
      "kept apart from the root identity of HZ3-b0: (i) NO history in "
      "the whole comparison has k^C1_r = k^C2_r, so the conventions are "
      "genuinely different completions and not a reparametrization — C3 "
      "is the reparametrization and HZ3-a gates it as one; (ii) at "
      "every fixed OFF-ROOT depth the separation in THE PINNED OBJECT "
      "shrinks in r, over a fixed eight-history window at the deepest "
      "rows.  **THE HORN VERDICT IS TAKEN ON THE PINNED OBJECT AND ON "
      "NOTHING ELSE, because the pin's §6 says so in terms — AND, "
      "AFTER ROUND 1, SO IS THE POOL VERDICT AT HZ2-c: ONE DOCTRINE, "
      "ONE DIRECTION.  The absolute rows are printed in full beside it "
      "and are NOT folded into the verdict — and they do NOT all "
      "shrink, which is exactly what D44f predicts of a horizon-bound "
      "quantity.**  The root row is excluded from (ii) exactly as at "
      "HZ2-a, and is HZ3-b0's forced identity",
      horn_separates and horn_neq_total == 0 and horn_cond_shrinks,
      f"histories with k^C1_r == k^C2_r = {horn_neq_total}; family-wide "
      f"absolute sup by r = {frl(horn_abs)}; family-wide conditional "
      f"sup by r = {frl(horn_cond)}; ROOT absolute = "
      f"{frl(horn_root_abs)}; ROOT conditional = {frl(horn_root_cond)}; "
      f"PINNED-object rows that do not shrink = "
      f"{HROW_BAD_COND if HROW_BAD_COND else 'none'}; ABSOLUTE "
      f"(horizon-bound, D44f context) rows that do not shrink = "
      f"{HROW_BAD_ABS if HROW_BAD_ABS else 'none'}; of those, off-root "
      f"= {[k for k in HROW_BAD_ABS if k[1] > 0]}")
outcome("HZ3-HORN",
        "THE CONVENTION GATE, DELIVERED ON THE PINNED OBJECT, WITH THE "
        "ROOT LEG DEMOTED TO A THEOREM (ROUND-1 MAJOR 3).  The two "
        "declared terminal conventions are different completions at "
        "every single history in the comparison — "
        f"{horn_neq_total} of the histories tested have k^C1_r = "
        "k^C2_r — so the truncation is a CHOICE and not a formality.  "
        "THE HORN LIVES OFF THE ROOT, AND OFF THE ROOT IT SHRINKS: the "
        "pinned separation at fixed depth runs 1/8, 1/12, 487/7790, "
        "40337/800358, 109092211/2569013838 — five terms, roughly "
        "1/(4r + 4), over a fixed eight-history window — down to "
        f"{horn_cond[-2]} at r = {HRS[-2]}.  AT THE ROOT IT IS EXACTLY "
        "0 AND THAT IS AN IDENTITY, NOT A MEASUREMENT: HZ3-s1/HZ3-s2 "
        "gate the root menu as one orbit per kind under the layer's own "
        "A <-> B and 0 <-> 1 automorphisms, so every equivariant "
        "terminal — C1, C2, C3 and the sector-weighted C5 the first "
        "delivery proposed as its residue 4 — gives the same "
        "uniform-in-kind root conditional and separation 0, while the "
        "non-equivariant C4 separates by 1/6 at r = 1.  So the first "
        "delivery's 'the pinned object stays exactly 0, so nothing "
        "physical moves' was not a consolation: the 0 was forced and "
        "would have stayed 0 whatever the absolute kernel did.  WHAT "
        "SURVIVES, and it is weaker than 'the horn is "
        "object-dependent': the ABSOLUTE kernel — D44f's horizon-bound "
        "context object, carried here as context and not folded into "
        f"any verdict — does NOT shrink monotonically at "
        f"{len(HROW_BAD_ABS)} of the {len(HLS)} depth rows "
        f"({HROW_BAD_ABS}), while the pinned object shrinks at every "
        "off-root depth.  The correct one-line statement is: THE "
        "ABSOLUTE KERNEL INHERITS THE TRUNCATION CONVENTION; THE PINNED "
        "CONDITIONAL IS PROTECTED BY SYMMETRY AT THE ROOT AND MEASURED "
        "TO SHRINK OFF IT.  Nothing here is extrapolated past the "
        "computed horizons, and 1/8 at r = 1 is not a small number: the "
        "conventions are far apart where the family is large and close "
        "only where the window is small.")

# ======================================================================
# HZ4 — THE LEMMA SLOT
# ======================================================================
print(f"\n{sec()} [HZ4 — THE LEMMA SLOT (proof-shaped; may return "
      f"empty, and saying so is a result).  No outcome here may upgrade "
      f"HZ2's labels unless a bound is printed.]")

print("  (i) THE TRANSPORT RENEWAL PREDICATE, DEFINED FROM D62's ROW R4")
print("      AND VERIFIED AGAINST THE LAYER AT EVERY OCCURRENCE.")
print("      R4's serialisation (note-d62 §8): hold = {A: v, B: v},")
print("      live = (), comps = (), refs = {v}, flag(v) = False —")
print("      serialisation-identical to sigma([]).  Ported to transport")
print("      as TWO predicates, because the port is not unique and")
print("      reporting only one would decide the question by fiat:")
print("        R-SIG  : every actor's NON-SUPERSEDED holdings is the")
print("                 same singleton {v}; no live proposals; no")
print("                 components; no merge pairs; v not superseded.")
print("                 (The literal R4 port: d42a's sigma sees the")
print("                 non-superseded token only, because")
print("                 prop_options_in_view SKIPS superseded.)")
print("        R-MENU : R-SIG and, in addition, holdings(a) = {v}")
print("                 EXACTLY for every a — no superseded remainder.")
print("                 (The MENU-EXACT port: at transport")
print("                 deliver_options_in_view enumerates over the")
print("                 WHOLE holdings set, so anything left in it is")
print("                 visible in the menu.)")
print("      The verification is the corpus's own standard: at a")
print("      renewal the menu must be the ROOT's menu with v0 renamed")
print("      to v, weight for weight, through the committed layer.")


def rename_v(e, v):
    """The root's menu with the genesis version renamed to v."""
    if e[0] == 'p':
        return ('p', e[1], v if e[2] == V0 else e[2], e[3])
    if e[0] == 'd':
        return ('d', e[1], e[2], v if e[3] == V0 else e[3])
    return e


def state_data(h, actors):
    pred = event_poset(list(h))
    vw = View(list(h), pred, set(range(len(h))))
    hold = {a: frozenset(vw.holdings(a)) for a in actors}
    nsup = {a: frozenset(x for x in hold[a] if x not in vw.superseded)
            for a in actors}
    return vw, hold, nsup


ROOTMENU = sorted(((e, q) for e, q in CACHE[ROOT]), key=repr)
RSIG, RMENU = [], []
SD_DEPTH = 5
_t = time.time()
STATE = {}
for h in CACHE:
    if len(h) > SD_DEPTH:
        continue
    vw, hold, nsup = state_data(h, AB)
    STATE[h] = (hold, nsup)
    if any(len(nsup[a]) != 1 for a in AB):
        continue
    v = next(iter(nsup['A']))
    if nsup['B'] != nsup['A']:
        continue
    if vw.live or vw.components():
        continue
    if any(vw.merge_pairs(a) for a in AB):
        continue
    RSIG.append((h, v))
    if all(hold[a] == frozenset({v}) for a in AB):
        RMENU.append((h, v))
print(f"{sec()}      state data built for {len(STATE)} histories "
      f"(depth <= {SD_DEPTH}; the predicate needs full views, which is "
      f"the declared window for this gate) in {time.time() - _t:.1f}s")

# SET comparison throughout, never sorted-by-repr: two EQUAL frozensets
# can carry different reprs in the same process, so a repr sort is not a
# safe multiset test.  (Round-1 MINOR 4 observed that the determinism
# digest never covered HZ4; it does now, and this is the arm that had to
# be made hash-robust for that to mean anything.)
sig_menu_ok = sig_menu_bad = 0
menu_menu_ok = menu_menu_bad = 0
SIG_GAP = None
for h, v in RSIG:
    want = {(rename_v(e, v), q) for e, q in ROOTMENU}
    got = set(CACHE[h])
    if got == want and len(CACHE[h]) == len(ROOTMENU):
        sig_menu_ok += 1
    else:
        sig_menu_bad += 1
        if SIG_GAP is None:
            SIG_GAP = (h, v, sorted(got - want, key=repr),
                       sorted(want - got, key=repr))
for h, v in RMENU:
    want = {(rename_v(e, v), q) for e, q in ROOTMENU}
    if set(CACHE[h]) == want and len(CACHE[h]) == len(ROOTMENU):
        menu_menu_ok += 1
    else:
        menu_menu_bad += 1
RSIGSET = {h for h, v in RSIG}
RMENUSET = {h for h, v in RMENU}


def reentry_count(S):
    """Points of S reached from OUTSIDE S: a history in S with at least
    one proper prefix that is not in S.  Zero means the class is
    absorbing-complement — left exactly once and never re-entered."""
    return sum(1 for h in S
               if any(h[:i] not in S for i in range(len(h))))


SIG_REENTRY = reentry_count(RSIGSET)
MENU_REENTRY = reentry_count(RMENUSET)
SIGSHAPES = defaultdict(int)
for h, v in RSIG:
    shape = tuple(sorted((e[0], str(q)) for e, q in CACHE[h]))
    SIGSHAPES[shape] += 1
depths_sig = sorted({len(h) for h, v in RSIG})
depths_menu = sorted({len(h) for h, v in RMENU})
print(f"      R-SIG  points at depth <= {SD_DEPTH}: {len(RSIG)} "
      f"(depths {depths_sig}); of these, "
      f"{sig_menu_ok} have the root's menu under renaming and "
      f"{sig_menu_bad} do NOT")
print(f"      R-MENU points at depth <= {SD_DEPTH}: {len(RMENU)} "
      f"(depths {depths_menu}); of these, "
      f"{menu_menu_ok} have the root's menu under renaming and "
      f"{menu_menu_bad} do NOT")
if SIG_GAP:
    h, v, extra, missing = SIG_GAP
    print(f"      THE GAP, EXHIBITED at the first R-SIG point that is "
          f"not a menu renewal:")
    print(f"        history  = {list(h)}")
    print(f"        in its menu and not in the renamed root menu: "
          f"{[(e, str(q)) for e, q in extra][:6]}")
    print(f"        in the renamed root menu and not in its menu: "
          f"{[(e, str(q)) for e, q in missing][:6]}")

print(f"      ROUND-1 MAJOR 4, THE TEST THE FIRST DELIVERY NEVER RAN ON "
      f"R-SIG.  Is each class ABSORBING-COMPLEMENT, i.e. left exactly "
      f"once and never re-entered?  Counting the points of each class "
      f"that have at least one proper prefix OUTSIDE the class:")
print(f"        R-MENU re-entries: {MENU_REENTRY} of {len(RMENUSET)} "
      f"-> absorbing-complement = {MENU_REENTRY == 0}")
print(f"        R-SIG  re-entries: {SIG_REENTRY} of {len(RSIGSET)} "
      f"-> absorbing-complement = {SIG_REENTRY == 0}")
print(f"      and the menu shapes R-SIG actually carries, as "
      f"(kind, weight) multisets — the class is NOT a shapeless "
      f"remainder:")
for shape, cnt in sorted(SIGSHAPES.items(), key=lambda x: (-x[1],
                                                           repr(x[0]))):
    _agg = defaultdict(int)
    for k, q in shape:
        _agg[(k, q)] += 1
    print(f"        {cnt:5d} points: "
          + ", ".join(f"{n}x{k}@{q}" for (k, q), n in
                      sorted(_agg.items())))
check("HZ4-i THE RENEWAL PREDICATE, VERIFIED AGAINST THE LAYER — and "
      "the two ports COME APART at transport, which is itself the "
      "finding.  R-SIG, the literal D62 R4 port, is NOT sufficient for "
      "a menu renewal at transport scope: the histories it selects "
      "carry the root's sigma-data and a DIFFERENT menu, because "
      "deliver_options_in_view enumerates over the whole holdings set "
      "while d42a's prop_options_in_view skips superseded.  R-MENU, "
      "the menu-exact port, is exact wherever it holds.  This is the "
      "B1 wall showing up inside the renewal question, and it is the "
      "same one line of the committed layer that HZ7 probes",
      len(RSIG) > 0 and len(RMENU) > 0 and menu_menu_bad == 0
      and menu_menu_ok == len(RMENU) and MENU_REENTRY == 0
      and SIG_REENTRY == sig_menu_bad,
      f"R-SIG = {len(RSIG)} points, menu-exact at {sig_menu_ok}, NOT "
      f"menu-exact at {sig_menu_bad}; R-MENU = {len(RMENU)} points, "
      f"menu-exact at {menu_menu_ok}, NOT menu-exact at "
      f"{menu_menu_bad}; RE-ENTRIES: R-MENU {MENU_REENTRY}, R-SIG "
      f"{SIG_REENTRY}; distinct R-SIG menu shapes = {len(SIGSHAPES)}")

# ---- the structural obstruction: holdings never shrink ---------------
print("  (ii) THE RETURN-WEIGHT CENSUS, and the structural fact that "
      "decides it.")
print("      holdings(a) in the committed layer is a UNION over the "
      "arbs, deliveries and merges in the view (d42b1's View.holdings), "
      "so extending a history can only ADD to it.  If that is exact, a "
      "renewal is unreachable the moment any actor holds two versions, "
      "and the return-weight census is decided rather than estimated.  "
      "Gated exhaustively over the family rather than asserted:")
mono_bad = mono_pairs = 0
MONO_EXPECT = sum(len(CACHE[h]) for h in CACHE if len(h) < SD_DEPTH)
grow_first = defaultdict(int)
for h in CACHE:
    if len(h) >= SD_DEPTH:
        continue
    hold_h = STATE[h][0]
    for e, q in CACHE[h]:
        h2 = h + (e,)
        if h2 not in STATE:
            continue
        mono_pairs += 1
        hold_2 = STATE[h2][0]
        if any(not hold_h[a] <= hold_2[a] for a in AB):
            mono_bad += 1
        if any(len(hold_h[a]) == 1 for a in AB) and \
           any(len(hold_2[a]) > 1 for a in AB):
            grow_first[e[0]] += 1
check("HZ4-ii(a) HOLDINGS ARE MONOTONE ALONG EVERY TRANSITION, "
      "exhaustively over the declared window: no event of any kind ever "
      "removes a version from any actor's holdings.  Together with "
      "R-MENU (which requires holdings(a) = {v} exactly) this makes the "
      "menu-exact renewal set ABSORBING-COMPLEMENT: once any actor "
      "holds a second version, no continuation of that history is ever "
      "a menu renewal again.  The event kinds that first break "
      "singleton holdings are censused",
      mono_bad == 0 and mono_pairs == MONO_EXPECT,
      f"transitions checked = {mono_pairs} (every transition out of "
      f"every history of depth < {SD_DEPTH}); holdings-shrinking "
      f"transitions = {mono_bad}; first-growth events by kind = "
      f"{dict(sorted(grow_first.items()))}",
      theorem="View.holdings is a union over the view's arbs, "
              "deliveries and merges, and extending a history only ADDS "
              "events — a one-line consequence of the layer, censused "
              "here rather than proved.  ROUND-1 MAJOR 4(a): note that "
              "the layer DOES have a shrinking set — 'superseded' "
              "grows, so NON-superseded holdings shrink — which is "
              "exactly why this argument covers R-MENU and NOT R-SIG")

# return-weight census by cycle length, under BOTH normalizations named
print("      RETURN-WEIGHT CENSUS from renewal to renewal by cycle "
      "length.  NORMALIZATION NAMED AT EVERY USE (D46d B2): column q "
      "is the RAW committed weight product; column k^C1_r is the "
      f"horizon-{CAP_T + 1} completed conditional chained from the root "
      "under convention C1.")
RMSET = {h for h, v in RMENU}
ret_q = defaultdict(lambda: Fr(0))
ret_k = defaultdict(lambda: Fr(0))
QW = {(): Fr(1)}
KW = {(): Fr(1)}
for n in range(0, SD_DEPTH):
    nq, nk = {}, {}
    for h in [x for x in QW if len(x) == n]:
        kk = krel(CACHE, GT, h, CAP_T + 1 - n)
        for e, q in CACHE[h]:
            nq[h + (e,)] = nq.get(h + (e,), Fr(0)) + QW[h] * q
            nk[h + (e,)] = nk.get(h + (e,), Fr(0)) + KW[h] * kk[e]
    QW.update(nq)
    KW.update(nk)
for h in QW:
    if h in RMSET and h != ROOT:
        ret_q[len(h)] += QW[h]
        ret_k[len(h)] += KW[h]
print("      cycle length n | # renewal histories at depth n | raw-q "
      "mass | horizon-completed k^C1 mass | k^C1 mass NOT at a renewal")
for n in range(1, SD_DEPTH + 1):
    nn = sum(1 for h, v in RMENU if len(h) == n)
    kk = ret_k.get(n, Fr(0))
    print(f"      n = {n} | {nn:6d} | {ret_q.get(n, Fr(0))} "
          f"(~{float(ret_q.get(n, Fr(0))):.6f}) | {kk} "
          f"(~{float(kk):.6f}) | {1 - kk} (~{float(1 - kk):.6f})")
esc = [1 - ret_k.get(n, Fr(0)) for n in range(1, SD_DEPTH + 1)]
esc_grows = all(esc[i] >= esc[i - 1] for i in range(1, len(esc)))
check("HZ4-ii(b) THE RETURN-WEIGHT CENSUS IS A DEPARTURE CENSUS.  The "
      "renewal class is exactly the histories in which nothing has been "
      "created yet, and by HZ4-ii(a) it is never re-entered once left, "
      "so 'return weight by cycle length' degenerates: there are no "
      "cycles, only a survival curve.  The mass still at a renewal at "
      "depth n falls monotonically and the mass permanently outside it "
      "rises, under BOTH normalizations, at every depth of the declared "
      "window",
      esc_grows and esc[-1] > esc[0] and len(esc) == SD_DEPTH,
      f"horizon-completed mass NOT at a renewal, n = 1..{SD_DEPTH}: "
      + ", ".join(f"{x} (~{float(x):.6f})" for x in esc))

# ---- (iii) the B1 ladder's cylinders ---------------------------------
print("  (iii) THE B1 LADDER'S CYLINDERS: do the never-regenerating "
      "cylinders carry vanishing total weight?  (Pin falsifier 5.)")
LAD = []
_h = []
_v = V0
for k in range(1, 9):
    _t3 = ('A', _v, 0)
    _e1 = ('p', 'A', _v, 0)
    ok1, q1 = admissible(_h, _e1, AB)
    _h = _h + [_e1]
    _e2 = ('r', 'A', frozenset({_t3}), frozenset({_t3}))
    ok2, q2 = admissible(_h, _e2, AB)
    _h = _h + [_e2]
    _v = vname(_v, frozenset({_t3}), 'A')
    _pred = event_poset(_h)
    _vw = View(_h, _pred, set(range(len(_h))))
    LAD.append((k, ok1 and ok2, q1, q2, len(_vw.holdings('A'))))
lad_q = Fr(1)
LADW = []
for k, ok, q1, q2, nh in LAD:
    lad_q *= q1 * q2
    LADW.append((k, lad_q, nh))
print("      rung k | admissible | q(propose) | q(self-arb) | "
      "|holdings(A)| | cylinder weight prod q")
for (k, ok, q1, q2, nh), (_, w, _n) in zip(LAD, LADW):
    print(f"      {k:6d} | {str(ok):>10} | {q1} | {q2} | {nh:6d} | {w} "
          f"(~{float(w):.3e})")
lad_ok = all(ok for k, ok, q1, q2, nh in LAD)
lad_hold = [nh for k, ok, q1, q2, nh in LAD] == list(range(2, 10))
lad_vanish = all(LADW[i][1] < LADW[i - 1][1] for i in range(1, len(LADW)))
# the mass NOT in the renewal class, i.e. the never-regenerating mass
nonren_k = esc[-1]
check("HZ4-iii THE LADDER'S OWN CYLINDER WEIGHT VANISHES, AND THAT DOES "
      "NOT HELP.  The single B1 ladder cylinder does carry weight "
      "tending to 0 rung by rung, so falsifier 5 read narrowly — 'the "
      "ladder's cylinders carry non-vanishing weight' — does NOT fire.  "
      "But by HZ4-ii(a) the ladder is not the object that matters: the "
      "NEVER-REGENERATING SET is everything past the first creation "
      "event, and its horizon-completed mass at the deepest computed "
      "cut is the number printed here, not a vanishing one.  So the "
      "regenerative route is blocked by the size of the "
      "non-regenerating set, not by the ladder",
      lad_ok and lad_hold and lad_vanish
      and nonren_k > LADW[-1][1] and nonren_k == esc[-1],
      f"every rung admissible = {lad_ok}; |holdings(A)| = k+1 = "
      f"{lad_hold}; cylinder weight falls monotonically = "
      f"{lad_vanish}, last = {LADW[-1][1]} "
      f"(~{float(LADW[-1][1]):.3e}); never-regenerating "
      f"horizon-completed mass at depth {SD_DEPTH} = {nonren_k} "
      f"(~{float(nonren_k):.6f})")

# ---- (iv) the minorization attempt -----------------------------------
print("  (iv) THE MINORIZATION ATTEMPT, RUN ON BOTH PORTS — ROUND-1 "
      "MAJOR 4(c).  A Doeblin/regenerative bound needs delta > 0 with: "
      "from EVERY history, the probability of hitting a renewal within "
      "N steps is >= delta.  The first delivery computed this for "
      "R-MENU only, at N = 1..3, and concluded that 'D69 route R5 is "
      "CLOSED'.  R-SIG — the literal D62 row-R4 port, which is what "
      "D69's R5 actually names — was never tested.  Both are tested "
      "here, out to N = 5, i.e. to the deepest N the window admits.  "
      "TWO HORIZON NORMALIZATIONS ARE PRINTED because the answer "
      "depends on which completed conditional the hitting probability "
      "is taken under, and naming one silently would repeat the defect "
      "D46d's BLOCKER B2 convicted: (H7) the horizon-7 conditional "
      "chained from the root, the receipt's own object, and (H6) the "
      "horizon-6 conditional matched to this gate's depth-5 window.  "
      "Also stated against this receipt: at N = 4 and N = 5 the window "
      "holds 9 and 1 histories, so those rows are NOT a bound and none "
      "is claimed — they are a demonstration that the route was never "
      "tested.")


def minorization(RSET, hoff, label):
    rows = []
    for N in (1, 2, 3, 4, 5):
        worst = None
        nz = 0
        tot = 0
        for h in CACHE:
            if len(h) + N > SD_DEPTH:
                continue
            tot += 1
            frontier = {h: Fr(1)}
            hit = Fr(0)
            for step in range(N):
                nxt = {}
                for g, w in frontier.items():
                    kk = krel(CACHE, GT, g, hoff - len(g))
                    for e, q in CACHE[g]:
                        g2 = g + (e,)
                        if g2 in RSET:
                            hit += w * kk[e]
                        else:
                            nxt[g2] = nxt.get(g2, Fr(0)) + w * kk[e]
                frontier = nxt
            if hit == 0:
                nz += 1
            if worst is None or hit < worst:
                worst = hit
        rows.append((N, tot, nz, worst))
        print(f"      {label} N = {N}: histories tested {tot}; hitting "
              f"probability EXACTLY 0 at {nz} of them; infimum = "
              f"{worst} (~{float(worst):.6f})")
    return rows


MIN_ROWS = minorization(RMSET, CAP_T + 1, "R-MENU (H7)")
MIN_ROWS_SIG = minorization(RSIGSET, CAP_T + 1, "R-SIG  (H7)")
MIN_ROWS_SIG6 = minorization(RSIGSET, SD_DEPTH + 1, "R-SIG  (H6)")
HZ4_BOUND = None
inf_zero = all(w == 0 for N, tot, nz, w in MIN_ROWS[:3])
sig_zero_collapses = [nz for N, tot, nz, w in MIN_ROWS_SIG]
sig_pos_at_4 = MIN_ROWS_SIG[3][3] > 0 and MIN_ROWS_SIG[3][2] == 0
sig_pos_at_4_h6 = MIN_ROWS_SIG6[3][3] > 0 and MIN_ROWS_SIG6[3][2] == 0
check("HZ4-iv NO BOUND EXHIBITED FOR THE MENU-EXACT ATOM — and, "
      "ROUND-1 MAJOR 4, THE SIGMA-LEVEL ROUTE IS NOT CLOSED BUT "
      "UNTESTED.  (a) For R-MENU the infimum of the N-step "
      "renewal-hitting probability is EXACTLY ZERO at every N the first "
      "delivery computed, and it is zero for a structural reason and "
      "not for want of depth: by HZ4-ii(a) holdings never shrink, so "
      "every history in which some actor already holds two versions has "
      "hitting probability exactly 0 for EVERY N.  There is no "
      "minorization constant to print for the menu-exact atom.  (b) For "
      "R-SIG the picture is the opposite shape: the class is RE-ENTERED "
      f"{SIG_REENTRY} times (HZ4-i), the zero-set COLLAPSES with N "
      f"({sig_zero_collapses[0]} -> {sig_zero_collapses[1]} -> "
      f"{sig_zero_collapses[2]} -> {sig_zero_collapses[3]} points), and "
      "at N = 4 there is NO history with hitting probability 0 and the "
      "infimum over the window is STRICTLY POSITIVE, under both horizon "
      "normalizations.  That is the shape of a Doeblin condition, not "
      "of a closed route.  (c) Stated exactly: classical Doeblin "
      "minorization needs no atom at all (P^N(x, .) >= delta nu(.)); "
      "the first delivery stated the ATOM version as if it were the "
      "general one.  NO OPERATOR-LEVEL MINORIZATION — Birkhoff / "
      "Hilbert-metric contraction of the positive backward recursion "
      "G, the natural instrument for this kernel — IS ATTEMPTED "
      "ANYWHERE IN THIS RECEIPT, and that is the named successor.  "
      "Consequently, per the pin, NOTHING in HZ4 upgrades any HZ2 "
      "label, HZ2's rows stay a table over the computed horizons, and "
      "outcome HZ-III's bound clause is NOT satisfied",
      inf_zero and HZ4_BOUND is None
      and all(0 < nz < tot for N, tot, nz, w in MIN_ROWS[:3])
      and sig_pos_at_4 and sig_pos_at_4_h6,
      "R-MENU infimum by N = "
      + ", ".join(f"N={N}: {w} over {tot} histories, {nz} exactly 0"
                  for N, tot, nz, w in MIN_ROWS)
      + "; R-SIG (H7) = "
      + ", ".join(f"N={N}: {w} over {tot}, {nz} exactly 0"
                  for N, tot, nz, w in MIN_ROWS_SIG)
      + "; R-SIG (H6) = "
      + ", ".join(f"N={N}: {w} over {tot}, {nz} exactly 0"
                  for N, tot, nz, w in MIN_ROWS_SIG6)
      + "; printed minorization constant = NONE (no bound is claimed "
      "from a 9-history and a 1-history window)")

# ---- the HZ4 positive control: the same predicate at d42a ------------
print("  HZ4 POSITIVE CONTROL — the same predicate machinery on the "
      "DELIVERY-FREE d42a family, where D62's row R4 says every "
      "pair-arb IS a renewal to the root state.  If the predicate "
      "cannot find the renewal the corpus derived, the transport "
      "negative above is an instrument artifact.")
DF_RSIG = DF_RMENU = DF_MENU_OK = 0
DF_PAIRARB = DF_PAIRARB_REN = 0
DFROOTMENU = sorted(DF[ROOT], key=repr)
for h in DF:
    if len(h) > 4:
        continue
    pred = event_poset(list(h))
    vw = View(list(h), pred, set(range(len(h))))
    hold = {a: frozenset(vw.holdings(a)) for a in AB}
    nsup = {a: frozenset(x for x in hold[a] if x not in vw.superseded)
            for a in AB}
    if any(len(nsup[a]) != 1 for a in AB) or nsup['A'] != nsup['B']:
        continue
    if vw.live or vw.components():
        continue
    v = next(iter(nsup['A']))
    DF_RSIG += 1
    if all(hold[a] == frozenset({v}) for a in AB):
        DF_RMENU += 1
    want = sorted(((rename_v(e, v), q) for e, q in DFROOTMENU), key=repr)
    if sorted(DF[h], key=repr) == want:
        DF_MENU_OK += 1
    if h and h[-1][0] == 'r' and len({t[0] for t in h[-1][2]}) == 2:
        DF_PAIRARB += 1
        if sorted(DF[h], key=repr) == want:
            DF_PAIRARB_REN += 1
check("HZ4-v THE INSTRUMENT FINDS THE RENEWAL WHERE THE CORPUS DERIVED "
      "ONE.  At delivery-free d42a scope the R-SIG predicate selects "
      "renewal points, and at EVERY one of them the menu is the root's "
      "menu under renaming, weight for weight — including at every "
      "history ending in a pair-arb, which is exactly D62 row R4's "
      "derived statement, re-derived here from the committed d42b3 "
      "layer through this receipt's own predicate.  So the transport "
      "negative in HZ4-i/ii/iv is a fact about transport and not about "
      "the predicate",
      DF_MENU_OK == DF_RSIG and DF_PAIRARB_REN == DF_PAIRARB
      and DF_RSIG > DF_PAIRARB and DF_RMENU < DF_RSIG,
      f"d42a: R-SIG points = {DF_RSIG}, menu-exact at {DF_MENU_OK}; "
      f"R-MENU points = {DF_RMENU}; histories ending in a pair-arb = "
      f"{DF_PAIRARB}, of which menu-renewals = {DF_PAIRARB_REN}")

# ======================================================================
# HZ5 — THE AGGREGATION ARM
# ======================================================================
print(f"\n{sec()} [HZ5 — THE AGGREGATION ARM (secondary, cheap, "
      f"independent): D57's coarsest-lumpable fixpoint at two STRICTLY "
      f"COARSER sector maps.  NOT DROPPED — the runtime budget did not "
      f"bind; had it bound, the drop would have been printed here.]")


def sec_type(e):
    return e[0]


BUDGET = {'p': 'propose', 'r': 'arb-merge', 'm': 'arb-merge',
          'd': 'deliver', 'n': 'idle'}


def sec_budget(e):
    return BUDGET[e[0]]


def sec_actor_type(e):
    return (e[1], e[0])


print("  THE SECTOR MAPS, and the strictness of the coarsening, gated "
      "rather than asserted:")
_bydepth = {}
for h in CACHE:
    for e, q in CACHE[h]:
        _bydepth.setdefault(len(h), set()).add(
            (sec_actor_type(e), sec_type(e), sec_budget(e)))
_cum = set()
_SIZES = {}
for d in sorted(_bydepth):
    _cum |= _bydepth[d]
    _SIZES[d] = (len({a for a, t, b in _cum}), len({t for a, t, b in _cum}),
                 len({b for a, t, b in _cum}))
print("      sector-map sizes by cumulative depth (|(actor,type)|, "
      "|type|, |budget|):")
for d in sorted(_SIZES):
    print(f"        depth <= {d}: {_SIZES[d]}")
_NAT, _NT, _NB = _SIZES[max(_SIZES)]
_first_strict = next((d for d in sorted(_SIZES)
                      if _SIZES[d][1] > _SIZES[d][2]), None)
check("HZ5-0 THE TWO NEW SECTOR MAPS ARE STRICTLY COARSER THAN D57's, "
      "and strictly ordered between themselves ON THE FULL FAMILY — "
      "with the depth at which the second ordering becomes strict "
      "printed, because it is NOT strict at shallow depth and saying "
      "so is the point.  D57's (initiator, event-type) refines "
      "TYPE-ONLY (s = event-type), which refines BUDGET-ONLY (s = the "
      "weight budget: propose | arb-and-merge | deliver | idle, the "
      "d42b1 docstring's own four budgets).  BUDGET-ONLY merges the "
      "'r' and 'm' types, so it is strictly coarser than TYPE-ONLY "
      "only once MERGE events appear in the family; the first depth at "
      "which that happens is printed and is a fact about the grammar "
      "(d42b1's own declared MERGE-SECTOR VACUITY at its caps), not "
      "about the maps",
      _NAT > _NT > _NB and _first_strict is not None,
      f"on the full depth-{CAP_T} family |(actor, type)| = {_NAT} > "
      f"|type| = {_NT} > |budget| = {_NB}; the type/budget ordering "
      f"first becomes strict at cumulative depth {_first_strict} "
      f"(before that the two maps coincide, 4 sectors each)")

# --- ROUND-1 MAJOR 5: the two maps are ONE map on the decider's input
print("  ROUND-1 MAJOR 5, THE MERGE CENSUS THAT DECIDES WHETHER THESE "
      "ARE TWO TESTS OR ONE.  BUDGET-ONLY differs from TYPE-ONLY only "
      "by merging the 'r' and 'm' types, so wherever no 'm' entry "
      "occurs in a menu the two maps are a BIJECTIVE RELABELLING of "
      "each other and induce the SAME initial signature and the SAME "
      "fixpoint partition.  Where the 'm' entries actually are:")
MBY = defaultdict(int)
for h in CACHE:
    for e, q in CACHE[h]:
        if e[0] == 'm':
            MBY[len(h)] += 1
M_HIST = sum(1 for h in CACHE if any(e[0] == 'm' for e in h))
M_FIRST_PARENT = min(MBY) if MBY else None
print(f"      menu entries of kind 'm', by PARENT depth: "
      f"{dict(sorted(MBY.items()))}")
print(f"      histories CONTAINING an m event: {M_HIST} of {len(CACHE)}")
print(f"      first parent depth carrying an 'm' menu entry: "
      f"{M_FIRST_PARENT}")

# --- the finite-alphabet prerequisite, gated FIRST and SEPARATELY ----
print("  THE FINITE-ALPHABET PREREQUISITE, GATED FIRST AND SEPARATELY "
      "(pin §3 HZ5, and D69 §6: whether the sector-total alphabet at "
      "transport scope is finite is [OPEN] — D57's ground (1) is "
      "withdrawn, and this gate treats it as open in BOTH directions):")
ALPH = {'type': defaultdict(lambda: defaultdict(set)),
        'budget': defaultdict(lambda: defaultdict(set))}
for cap in HZ5_CAPS:
    for h in CACHE:
        if len(h) > cap:
            continue
        tt = defaultdict(lambda: Fr(0))
        bb = defaultdict(lambda: Fr(0))
        for e, q in CACHE[h]:
            tt[sec_type(e)] += q
            bb[sec_budget(e)] += q
        for s, v in tt.items():
            ALPH['type'][cap][s].add(v)
        for s, v in bb.items():
            ALPH['budget'][cap][s].add(v)
for mp in ('type', 'budget'):
    print(f"    {mp.upper()}-ONLY sector-total alphabet by cap:")
    for cap in HZ5_CAPS:
        tot = sorted({v for s in ALPH[mp][cap] for v in ALPH[mp][cap][s]})
        print(f"      cap {cap}: {len(tot):3d} distinct totals over "
              f"{len(ALPH[mp][cap])} sectors; per sector "
              + ", ".join(f"{s}: {len(ALPH[mp][cap][s])}"
                          for s in sorted(ALPH[mp][cap])))
alph_growth = {}
alph_nested = {}
for mp in ('type', 'budget'):
    tots = [{v for s in ALPH[mp][c] for v in ALPH[mp][c][s]}
            for c in HZ5_CAPS]
    alph_growth[mp] = [len(t) for t in tots]
    alph_nested[mp] = all(tots[i - 1] <= tots[i]
                          for i in range(1, len(tots)))
check("HZ5-1 THE FINITE-ALPHABET PREREQUISITE IS NOT SETTLED BY THIS "
      "WINDOW, IN EITHER DIRECTION, AND THE GATE SAYS SO.  The number "
      "of distinct sector totals is reported per cap for both maps; it "
      "is not extrapolated to a claim of finiteness and not "
      "extrapolated to a claim of blow-up.  D57's precedent is the "
      "reason for the caution: it pre-registered this prerequisite, "
      "published a refutation of it, and the refutation was itself "
      "withdrawn in round.  ROUND-1 MODERATE 8, THE PREDICATE "
      "REPAIRED: the first delivery's predicate was 'the per-cap "
      "alphabet SIZES are non-decreasing', which cannot return False "
      "for any input, because the cap-c family is a SUBSET of the "
      "cap-(c+1) family and the collected alphabets are therefore "
      "nested by construction.  The predicate here tests the "
      "SET-INCLUSION nesting itself, which is a genuine regression "
      "tripwire on the family construction (a cap-c total absent at "
      "cap c+1 would mean the families are not nested and every HZ5 "
      "number below would be void), and the size clause is retained "
      "but DISCLOSED as the unfailable half.  What the gate delivers "
      "either way is the verdict [OPEN], which is a REPORT, not a test",
      all(alph_nested.values())
      and all(len(v) == len(HZ5_CAPS) for v in alph_growth.values())
      and all(v[i] >= v[i - 1] for v in alph_growth.values()
              for i in range(1, len(v))),
      "; ".join(f"{mp}-only distinct totals by cap {HZ5_CAPS} = "
                f"{alph_growth[mp]}, alphabets nested by inclusion = "
                f"{alph_nested[mp]}" for mp in alph_growth),
      theorem="the size-monotonicity half is forced by family nesting; "
              "only the set-inclusion half is a tripwire, and the "
              "delivered verdict [OPEN] is a report")

# --- the refinement, both maps, both boundary treatments -------------
def run_refine(smap, cap, boundary):
    FAM = [h for h in CACHE if len(h) <= cap]
    SIG = {}
    for h in FAM:
        tot = defaultdict(lambda: Fr(0))
        for e, q in CACHE[h]:
            tot[smap(e)] += q
        SIG[h] = tuple(sorted(((s, v) for s, v in tot.items()), key=repr))
    cls, keys = {}, {}
    for h in FAM:
        k = (('CAP',) if (boundary == 'triv' and len(h) >= cap)
             else SIG[h])
        keys.setdefault(k, len(keys))
        cls[h] = keys[k]
    it, wit = 0, None
    while True:
        it += 1
        nk, ncls = {}, {}
        for h in FAM:
            if len(h) >= cap:
                key = ('cap', cls[h]) if boundary == 'sig' else ('cap',)
            else:
                agg = defaultdict(lambda: Fr(0))
                for e, q in CACHE[h]:
                    agg[(smap(e), cls[h + (e,)])] += q
                key = (cls[h], tuple(sorted(agg.items(), key=repr)))
            nk.setdefault(key, len(nk))
            ncls[h] = nk[key]
        stable = len(nk) == len(set(cls.values()))
        if not stable and wit is None:
            byold = defaultdict(list)
            for h in FAM:
                byold[cls[h]].append(h)
            for old, mem in sorted(byold.items(), key=repr):
                seen = defaultdict(list)
                for h in mem:
                    seen[ncls[h]].append(h)
                if len(seen) < 2:
                    continue
                pair = None
                for L in sorted({len(h) for h in mem}):
                    reps = [sorted((x for x in v if len(x) == L),
                                   key=repr)[:1] for v in seen.values()]
                    reps = [x[0] for x in reps if x]
                    if len(reps) >= 2:
                        pair = tuple(sorted(reps, key=repr)[:2])
                        break
                if pair is None:
                    two = sorted((sorted(v, key=repr)[0]
                                  for v in seen.values()), key=repr)
                    pair = (two[0], two[1])
                wit = (it, old, pair[0], pair[1])
                break
        cls = ncls
        if stable:
            break
    bydep = defaultdict(set)
    for h in FAM:
        bydep[len(h)].add(cls[h])
    return {d: len(v) for d, v in sorted(bydep.items())}, it, wit, cls


HZ5RES = {}
HZ5TRIV = {}
HZ5WIT = {}
HZ5CLS = {}
HZ5FULL = {}
for mp, smap in (('type', sec_type), ('budget', sec_budget)):
    print(f"\n  {mp.upper()}-ONLY AGGREGATION (route "
          f"{'R1' if mp == 'type' else 'R2'} of D69 §3):")
    for cap in HZ5_CAPS:
        _t = time.time()
        r1, it1, w1, cls1 = run_refine(smap, cap, 'sig')
        r2, it2, w2, cls2 = run_refine(smap, cap, 'triv')
        HZ5RES[(mp, cap)] = r1
        HZ5TRIV[(mp, cap)] = r2
        HZ5WIT[(mp, cap)] = w1
        HZ5CLS[(mp, cap)] = {h: cls1[h] for h in cls1 if len(h) == 3}
        HZ5FULL[(mp, cap)] = cls1
        print(f"    cap {cap}: histories = "
              f"{sum(1 for h in CACHE if len(h) <= cap)}, iterations "
              f"{it1}, fixpoint classes per depth = {r1}")
        print(f"            trivial-boundary control (iterations "
              f"{it2}): {r2}   [{time.time() - _t:.1f}s]")

print("\n  THE DECIDER, STATED AS IT IS IMPLEMENTED (D57's round-1 "
      "MINOR 6, carried verbatim): for every depth carrying at least "
      "three cap values, do the LAST TWO cap values agree?  No other "
      "threshold is used anywhere and none is invented.")
HZ5_STAB = {}
for mp in ('type', 'budget'):
    print(f"    {mp.upper()}-ONLY   depth : " + "  ".join(
        f"cap{c}" for c in HZ5_CAPS))
    stab = []
    for d in range(0, 7):
        row = [HZ5RES[(mp, c)].get(d) for c in HZ5_CAPS]
        print(f"                    {d}   :  " + "   ".join(
            f"{x}" if x is not None else "-" for x in row))
        vals = [x for x in row if x is not None]
        if len(vals) >= 3:
            stab.append((d, vals[-1] == vals[-2]))
    HZ5_STAB[mp] = stab
    print(f"                    (depth, stable-at-last-two-caps) = "
          f"{stab}")
type_closes = all(s for d, s in HZ5_STAB['type'])
budget_closes = all(s for d, s in HZ5_STAB['budget'])

# ---- ROUND-1 MAJOR 5: is R2 a distinct test at these caps? ----------
DECIDER_DEPTHS = sorted({d for d, s in HZ5_STAB['type']})


def same_partition(ca, cb, keys):
    fwd, rev = {}, {}
    for h in keys:
        a, b = ca[h], cb[h]
        if fwd.setdefault(a, b) != b or rev.setdefault(b, a) != a:
            return False
    return True


PART_SAME = {}
for cap in HZ5_CAPS:
    ks = [h for h in HZ5FULL[('type', cap)] if len(h) <= max(DECIDER_DEPTHS)]
    ks_all = list(HZ5FULL[('type', cap)])
    PART_SAME[cap] = (same_partition(HZ5FULL[('type', cap)],
                                     HZ5FULL[('budget', cap)], ks),
                      same_partition(HZ5FULL[('type', cap)],
                                     HZ5FULL[('budget', cap)], ks_all))
print(f"    THE TWO MAPS, COMPARED AS PARTITIONS (ROUND-1 MAJOR 5).  "
      f"The decider carried from D57 is 'for every depth carrying at "
      f"least three cap values, do the LAST TWO cap values agree?', so "
      f"its input is exactly depths {DECIDER_DEPTHS}.  Below parent "
      f"depth {M_FIRST_PARENT} no menu carries an 'm' entry, so on "
      f"every menu entry there BUDGET-ONLY is a bijective relabelling "
      f"of TYPE-ONLY:")
for cap in HZ5_CAPS:
    print(f"      cap {cap}: identical partition on the decider's "
          f"depths {DECIDER_DEPTHS} = {PART_SAME[cap][0]}; identical on "
          f"the WHOLE cap-{cap} family = {PART_SAME[cap][1]}")
decider_identical = all(PART_SAME[c][0] for c in HZ5_CAPS)
m_absent_below = all(d >= M_FIRST_PARENT for d in MBY)
m_only_deep = all(len(h) > M_FIRST_PARENT for h in CACHE
                  if any(e[0] == 'm' for e in h))
check("HZ5-4 THE TWO 'ROUTES' ARE ONE COMPUTATION AT EVERY DEPTH THE "
      "DECIDER USES — ROUND-1 MAJOR 5.  No menu entry of kind 'm' "
      f"occurs at parent depth below {M_FIRST_PARENT}, so on every menu "
      "entry the decider ever sees, BUDGET-ONLY is TYPE-ONLY with two "
      "labels merged that never both occur — a bijective relabelling.  "
      "The induced initial signature is therefore the same function up "
      "to names, the fixpoint refinement is the same refinement, and "
      "the resulting partitions are gated here to be IDENTICAL AS "
      "PARTITIONS at every cap on the decider's whole input.  The one "
      "number that differs (depth 6: 10 vs 9) lies in the cap layer and "
      "never enters the decider.  So the honest statement is that ONE "
      "test was run: route R1 CLOSES on measurement, and route R2's "
      "closure is INHERITED, not measured.  Extending R2 to a cap where "
      "merges have support is the residue this creates",
      decider_identical and m_absent_below and m_only_deep
      and M_FIRST_PARENT is not None,
      f"'m' menu entries by parent depth = {dict(sorted(MBY.items()))}; "
      f"histories containing an m event = {M_HIST} of {len(CACHE)}; "
      f"partitions identical on the decider's depths {DECIDER_DEPTHS} "
      f"at every cap = {decider_identical}; identical on the whole "
      f"family by cap = "
      f"{ {c: PART_SAME[c][1] for c in HZ5_CAPS} }")

# S4-pattern control
s4_ok = {}
for mp in ('type', 'budget'):
    ident = []
    for cap in HZ5_CAPS[1:]:
        same = all(HZ5TRIV[(mp, cap)].get(d) == HZ5RES[(mp, cap - 1)].get(d)
                   for d in HZ5RES[(mp, cap - 1)])
        ident.append(same and HZ5TRIV[(mp, cap)].get(cap) == 1)
    s4_ok[mp] = ident
    print(f"    S4 CONTROL, {mp.upper()}-ONLY: cap-C-with-signature == "
          f"cap-(C+1)-with-trivial on every shared depth, C = 3, 4, 5: "
          f"{ident}")
check("HZ5-2 D57's S4 TRIVIAL-BOUNDARY CONTROL TRANSFERS TO BOTH "
      "COARSER MAPS, so the counts printed above are LOWER BOUNDS on "
      "the untruncated fixpoint and any growth reading is the "
      "CONSERVATIVE one — exactly as at D57's own granularity.  The "
      "signature boundary is worth precisely one extra level of "
      "lookahead and both truncations UNDER-refine",
      all(s4_ok['type']) and all(s4_ok['budget']),
      f"type-only: {s4_ok['type']}; budget-only: {s4_ok['budget']}")

print("\n  S3 SPLIT WITNESS at each cap (D57's S3, the clause the "
      "committed first receipt lacked):")
for mp in ('type', 'budget'):
    for cap in HZ5_CAPS:
        w = HZ5WIT[(mp, cap)]
        if w is None:
            print(f"    {mp}-only cap {cap}: NO SPLIT — the signature "
                  f"partition is already the fixpoint")
            continue
        it, old, h1, h2 = w
        print(f"    {mp}-only cap {cap}: first split at iteration {it}; "
              f"witness pair")
        print(f"        {list(h1)}")
        print(f"        {list(h2)}")
SPLIT3 = {}
for mp in ('type', 'budget'):
    inv5 = defaultdict(list)
    for h, c in HZ5CLS[(mp, 5)].items():
        inv5[c].append(h)
    found = None
    for c, mem in sorted(inv5.items(), key=repr):
        parts = defaultdict(list)
        for h in mem:
            parts[HZ5CLS[(mp, 6)][h]].append(h)
        if len(parts) > 1:
            found = (len(mem), sorted((len(v) for v in parts.values()),
                                      reverse=True))
            break
    SPLIT3[mp] = found
    n5 = len(set(HZ5CLS[(mp, 5)].values()))
    n6 = len(set(HZ5CLS[(mp, 6)].values()))
    print(f"    {mp}-only DEPTH-3 CREEP: cap5 {n5} classes -> cap6 "
          f"{n6} classes; splitting cap5 class had "
          f"{found[0] if found else 0} histories, splits "
          f"{found[1] if found else []}")
check("HZ5-3 THE COARSER AGGREGATIONS DO NOT CLOSE EITHER, AND THE "
      "SPLIT IS EXHIBITED RATHER THAN COUNTED.  At both TYPE-ONLY and "
      "BUDGET-ONLY the per-depth fixpoint counts fail the last-two-caps "
      "decider at every comparable depth, the S4 control says the "
      "counts are lower bounds, and a named double-digit depth-3 class "
      "splits between cap 5 and cap 6 at each map.  This is outcome "
      "HZ5-b at caps 3-6, on two actors, with the counts as lower "
      "bounds — the same grade as D57's own verdict and no stronger.  "
      "ROUND-1 MAJOR 5, THE CLAIM NARROWED: this is ONE closed route, "
      "not two.  HZ5-4 gates that the two sector maps induce the "
      "IDENTICAL partition on the decider's whole input, so route R1 "
      "closes on measurement and route R2's closure is INHERITED from "
      "it rather than independently measured",
      (not type_closes) and (not budget_closes)
      and SPLIT3['type'] is not None and SPLIT3['budget'] is not None,
      f"type-only stable at last two caps = {type_closes}; budget-only "
      f"= {budget_closes}; depth-3 split witnesses present = "
      f"{SPLIT3['type'] is not None}, {SPLIT3['budget'] is not None}")

# ======================================================================
# HZ6 — CONTROLS AND ANTI-VACUITY
# ======================================================================
print(f"\n{sec()} [HZ6 — CONTROLS AND ANTI-VACUITY]")

# ---- (i) the negative control ---------------------------------------
print("  (i) NEGATIVE CONTROL — an instrument that cannot fail is not "
      "evidence (D68 F5).  THREE deliberately perturbed weight laws "
      "are pushed through the identical pipeline, on the SAME declared "
      f"window (depth <= {CAP_NEG}) as the true law, so every "
      "comparison is like-for-like.  All three are synthetic, are "
      "declared here, are used NOWHERE else in this receipt, and "
      "change no committed number.  ALL THREE ARE REPORTED, including "
      "the one that does NOT break contraction — a perturbation the "
      "statistic survives is information about the statistic's "
      "robustness, not a result to be dropped:")
print("      NC1  [WEIGHT LAW] propose weights x3 at even depth, "
      "x(1/3) at odd")
print("      NC2  [GRAMMAR, NOT A WEIGHT LAW — ROUND-1 MINOR 3] "
      "deliveries FORBIDDEN at even depth, proposals FORBIDDEN at odd "
      "depth.  Setting a weight to 0 REMOVES the menu entry, so NC2's "
      "drift is taken over a DIFFERENT FAMILY; the pin asks for 'a "
      "deliberately perturbed WEIGHT LAW' and NC1 and NC3 are that, "
      "NC2 is not.  It is kept, because a grammar perturbation is a "
      "legitimate second kind of control, but it is counted separately")
print("      NC3  [WEIGHT LAW] idle weight x100 at even depth only")
print("      (a purely depth-dependent rescaling of ALL weights is "
      "invisible to k_r by construction — it cancels in the ratio — so "
      "every control below is type-selective as well as "
      "depth-selective, which is why it can bite at all.)")


def tilted(fn):
    return {h: [(e, fn(len(h), e, q)) for e, q in men]
            for h, men in CACHE.items() if len(h) <= CAP_NEG}


TCACHE = tilted(lambda L, e, q: q)
NCS = [
    ("NC1 propose x3/x(1/3) by depth parity",
     tilted(lambda L, e, q: q * (Fr(3) if L % 2 == 0 else Fr(1, 3))
            if e[0] == 'p' else q)),
    ("NC2 no deliveries at even depth, no proposals at odd depth",
     tilted(lambda L, e, q: Fr(0) if ((L % 2 == 0 and e[0] == 'd')
                                      or (L % 2 == 1 and e[0] == 'p'))
            else q)),
    ("NC3 idle x100 at even depth only",
     tilted(lambda L, e, q: q * Fr(100)
            if (e[0] == 'n' and L % 2 == 0) else q)),
]
GTt = rel_potential(TCACHE)


def uni_seq(cache, G, cap):
    out = []
    for r in range(1, cap + 1):
        best = Fr(0)
        for h in cache:
            if len(h) + r + 1 > cap + 1:
                continue
            a, b = krel(cache, G, h, r), krel(cache, G, h, r + 1)
            best = max(best, linf(a, b))
        out.append((r, best))
    return out


TRUE_SEQ = uni_seq(TCACHE, GTt, CAP_NEG)
print(f"      TRUE law, window depth {CAP_NEG}: "
      + ", ".join(f"r={r}->{r + 1}: {v} (~{float(v):.4e})"
                  for r, v in TRUE_SEQ))
NCRES = []
pert_proper = True
for nm, C in NCS:
    G = rel_potential(C)
    s = uni_seq(C, G, CAP_NEG)
    ok = contracts_from_first_nonzero([v for r, v in s])
    NCRES.append((nm, s, ok))
    print(f"      {nm}: "
          + ", ".join(f"r={r}->{r + 1}: {v} (~{float(v):.4e})"
                      for r, v in s)
          + f"   contracts = {ok}")
    for h in C:
        for r in (1, 2):
            if len(h) + r > CAP_NEG + 1:
                continue
            if sum(krel(C, G, h, r).values()) != 1:
                pert_proper = False
true_contracts = contracts_from_first_nonzero(
    [v for r, v in TRUE_SEQ])
BREAKERS = [nm for nm, s, ok in NCRES if not ok]
SURVIVORS = [nm for nm, s, ok in NCRES if ok]
pert_contracts = not BREAKERS
WEIGHTLAW = [nm for nm, s, ok in NCRES if not nm.startswith('NC2')]
GRAMMAR = [nm for nm, s, ok in NCRES if nm.startswith('NC2')]
WL_BREAK = [nm for nm in BREAKERS if nm in WEIGHTLAW]
GR_BREAK = [nm for nm in BREAKERS if nm in GRAMMAR]
print(f"      ROUND-1 MINOR 3, THE COUNT RESTATED BY KIND: of the "
      f"{len(WEIGHTLAW)} declared WEIGHT-LAW perturbations "
      f"{len(WL_BREAK)} break contraction (NC3), and of the "
      f"{len(GRAMMAR)} declared GRAMMAR perturbation {len(GR_BREAK)} "
      f"breaks it (NC2).  The first delivery reported '2 of 3' without "
      f"the distinction.  The pin's falsifier-1 clause is satisfied by "
      f"the weight-law breaker alone.")
check("HZ6-i THE INSTRUMENT CAN FAIL.  On the identical pipeline, the "
      "same norm, the same window and the same relative horizons, the "
      "true law's family-uniform drift contracts and at least one "
      "declared perturbation makes it STOP contracting — so the "
      "statistic is not one that returns 'contracting' whatever it is "
      "fed, and pin falsifier 1 does NOT fire.  Every perturbed kernel "
      "is still proper, so what the control isolates is the "
      "contraction and nothing else.  REPORTED IN FULL AND NOT "
      "CHERRY-PICKED: which perturbations broke it and which did not "
      "are both named, and the survivor is a measured robustness fact "
      "about the statistic, not a discarded trial",
      true_contracts and len(WL_BREAK) > 0 and pert_proper
      and len(NCRES) == len(NCS),
      f"true law contracts = {true_contracts}; WEIGHT-LAW perturbations "
      f"that BREAK contraction = {WL_BREAK} (of {len(WEIGHTLAW)}); "
      f"GRAMMAR perturbations that break it = {GR_BREAK} (of "
      f"{len(GRAMMAR)}); perturbations the statistic SURVIVES = "
      f"{SURVIVORS}; all perturbed kernels proper = {pert_proper}")

# ---- (ii) the positive control --------------------------------------
print("  (ii) POSITIVE CONTROL — the delivery-free d42a family through "
      "THE SAME PIPELINE must reproduce Zhat's known objects.")
_t = time.time()
SIGDF = {h: canon_sigma(h) for h in DF}
STATES = sorted(set(SIGDF.values()))
SIDX = {s: i for i, s in enumerate(STATES)}
SHORTREP = {}
for h in sorted(DF, key=lambda x: (len(x), repr(x))):
    s = SIGDF[h]
    if s not in SHORTREP:
        SHORTREP[s] = h
NS = len(STATES)
TM = [[Fr(0)] * NS for _ in range(NS)]
for s in STATES:
    hr = SHORTREP[s]
    for e, q in DF[hr]:
        TM[SIDX[s]][SIDX[SIGDF.get(hr + (e,), canon_sigma(hr + (e,)))]] += q


def dense_nullspace(M, n):
    A = [row[:] for row in M]
    piv, r = {}, 0
    for c in range(n):
        pr = None
        for i in range(r, n):
            if A[i][c] != 0:
                pr = i
                break
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        f = A[r][c]
        A[r] = [x / f for x in A[r]]
        for i in range(n):
            if i != r and A[i][c] != 0:
                g = A[i][c]
                A[i] = [A[i][k] - g * A[r][k] for k in range(n)]
        piv[c] = r
        r += 1
    out = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [Fr(0)] * n
        v[fc] = Fr(1)
        for c, ri in piv.items():
            v[c] = -A[ri][fc]
        out.append(v)
    return out


EIG = {}
for lam in (Fr(2), Fr(1), Fr(5, 2), Fr(9, 4)):
    B = dense_nullspace([[TM[i][j] - (lam if i == j else Fr(0))
                          for j in range(NS)] for i in range(NS)], NS)
    if B:
        v = B[0]
        v = [x / min((y for y in v if y != 0), key=abs) for x in v]
        cen = defaultdict(int)
        for x in v:
            cen[str(x)] += 1
        EIG[str(lam)] = (len(B), all(x > 0 for x in v), dict(cen), v)
    else:
        EIG[str(lam)] = (0, None, {}, None)
f2 = EIG['2'][3]
f2_positive = (f2 is not None) and min(f2) > Fr(0)
f1_mixed = (EIG['1'][3] is not None
            and min(EIG['1'][3]) < Fr(0) < max(EIG['1'][3]))
# G is a function of sigma alone on the delivery-free family: the
# pipeline's OWN object seeing the closure
gfun_bad = 0
GFUN = {}
for r in (1, 2, 3):
    seen = {}
    for h in DF:
        if len(h) + r > CAP_DF + 1:
            continue
        v = seen.setdefault(SIGDF[h], GD(h, r))
        if v != GD(h, r):
            gfun_bad += 1
    GFUN[r] = len(seen)
# T f = 2 f exactly, and T^r 1 = G(., r)
Tf_ok = all(sum(TM[i][j] * f2[j] for j in range(NS)) == 2 * f2[i]
            for i in range(NS)) if f2 else False
vec = [Fr(1)] * NS
POW = []
for r in range(1, 7):
    vec = [sum(TM[i][j] * vec[j] for j in range(NS)) for i in range(NS)]
    POW.append(vec[:])
pow_ok = all(POW[r - 1][SIDX[SIGDF[ROOT]]] == GD(ROOT, r)
             for r in range(1, 7))
print(f"      the transfer operator on the {NS} sigma states: "
      + "; ".join(f"lambda = {lam}: ker dim {EIG[lam][0]}"
                  + (f", positive generator = {EIG[lam][1]}, values "
                     f"{EIG[lam][2]}" if EIG[lam][0] else "")
                  for lam in ('2', '1', '5/2', '9/4')))
print(f"      G(., r) is a function of sigma alone: distinct "
      f"(sigma, G) pairs at r = 1, 2, 3 = "
      f"{[GFUN[r] for r in (1, 2, 3)]} over {NS} states, violations "
      f"= {gfun_bad}")
print(f"      lambda = 2 is used ONLY as an ASYMPTOTIC eigenvalue: it "
      f"is gated as T f = 2 f exactly, and it is NOT compared with any "
      f"finite-horizon ratio — the delivery-free finite-horizon ratios "
      f"printed at HZ0-6 are {frl(dR[:5])} and none of them equals 2 "
      f"(D46b's own relabelling, carried).")
check("HZ6-ii THE PIPELINE REPRODUCES ZHAT'S KNOWN OBJECTS ON THE "
      "DELIVERY-FREE FAMILY.  ker(T - 2I) is ONE-dimensional with a "
      "strictly positive generator taking the values {1, 4/3, 7/3} at "
      "multiplicities {29, 5, 2} — D49's f = (4,4,3,7,3,3)/3; "
      "ker(T - I) is one-dimensional and MIXED-SIGN; ker(T - 5/2 I) and "
      "ker(T - 9/4 I) are empty; T f = 2 f holds exactly; and this "
      "receipt's own potential G(h, r), the object HZ0-HZ3 measure, is "
      "a function of sigma(h) alone on this family with T^r applied to "
      "the all-ones vector reproducing it at the root at every horizon. "
      "So the horizon pipeline and the corpus's Perron object are the "
      "same object where both exist",
      EIG['2'][0] == 1 and f2_positive
      and EIG['2'][2] == {'1': 29, '4/3': 5, '7/3': 2}
      and EIG['1'][0] == 1 and f1_mixed
      and EIG['5/2'][0] == 0 and EIG['9/4'][0] == 0
      and Tf_ok and gfun_bad == 0 and pow_ok and NS == 36,
      f"states = {NS}; ker(T-2I) dim {EIG['2'][0]} positive "
      f"{EIG['2'][1]} values {EIG['2'][2]}; ker(T-I) dim "
      f"{EIG['1'][0]} one-signed {EIG['1'][1]}; T f = 2 f exactly = "
      f"{Tf_ok}; G factors through sigma with {gfun_bad} violations; "
      f"T^r 1 == G(root, r) at r = 1..6 = {pow_ok}  "
      f"[{time.time() - _t:.1f}s]")

# ---- (iii) AST anti-vacuity scan ------------------------------------
print("  (iii) AST ANTI-VACUITY SCAN over every check() predicate in "
      "this file (D57 S5), WITH ITS KNOWN DEFECT NAMED so the scan is "
      "not sold as more than it is.")
_self_src = open(os.path.abspath(__file__)).read()
_tree = ast.parse(_self_src)
_bound = set()
for _n in ast.walk(_tree):
    if isinstance(_n, ast.Name) and isinstance(_n.ctx, ast.Store):
        _bound.add(_n.id)
    elif isinstance(_n, ast.FunctionDef):
        _bound.add(_n.name)


def vacuity_scan(tree, bound):
    bad, n = [], 0
    for nd in ast.walk(tree):
        if not (isinstance(nd, ast.Call)
                and getattr(nd.func, 'id', '') == 'check'
                and len(nd.args) >= 2):
            continue
        n += 1
        p = nd.args[1]
        names = {x.id for x in ast.walk(p) if isinstance(x, ast.Name)}
        if isinstance(p, ast.Constant):
            bad.append((nd.lineno, 'literal constant'))
            continue
        if bound and not (names & bound):
            bad.append((nd.lineno, 'no bound name'))
        for sub in ast.walk(p):
            if (isinstance(sub, ast.Constant)
                    and (sub.value is True or sub.value is False)):
                bad.append((nd.lineno, 'literal boolean'))
            elif (isinstance(sub, ast.Call)
                  and getattr(sub.func, 'id', '') == 'isinstance'):
                bad.append((nd.lineno, 'isinstance type probe'))
            elif (isinstance(sub, ast.Compare) and len(sub.ops) == 1
                  and isinstance(sub.ops[0], (ast.Gt, ast.GtE))
                  and isinstance(sub.comparators[0], ast.Constant)
                  and sub.comparators[0].value == 0
                  and isinstance(sub.left, ast.Name)):
                bad.append((nd.lineno, 'bare sign comparison'))
    return n, bad


NGATES, TAUT = vacuity_scan(_tree, _bound)
_PB = ('check("a", isinstance(x, Fr))\n'
       'check("b", True)\n'
       'check("c", n > 0)\n')
_pn, _pb = vacuity_scan(ast.parse(_PB), {'x', 'n'})
_PG = ('check("d", cen4 == {"2": 3757} and tG == TG_REF)\n')
_qn, _qb = vacuity_scan(ast.parse(_PG), {'cen4', 'tG', 'TG_REF'})
probe_fires = (_pn == 3 and len(_pb) >= 3 and _qn == 1 and _qb == [])
check("HZ6-iii NO VACUOUS GATE, AND THE SCANNER'S OWN DEFECT IS NAMED. "
      "Every check() predicate in this file is parsed; a predicate is "
      "rejected if it is a literal constant, contains a literal "
      "boolean, contains an isinstance() type probe, contains a bare "
      "name-vs-0 sign comparison, or mentions no name bound anywhere in "
      "this file.  The scanner is probed both ways and must flag three "
      "synthetic vacuous shapes and pass a substantive one.  **THE "
      "CARRIED DEFECT (D46b's own finding, named here so this gate is "
      "not oversold): the scan is defeated by HOISTING — a predicate "
      "that reads a boolean computed on an earlier line looks "
      "substantive to the scanner whatever that line did.**  The scan "
      "bounds the shape of a predicate, not its content",
      not TAUT and NGATES >= 20 and probe_fires,
      f"gate predicates parsed = {NGATES}; flagged = "
      f"{TAUT if TAUT else 'none'}; scanner fires on the vacuous probe "
      f"and passes the substantive one = {probe_fires} ({len(_pb)} of 3 "
      f"synthetic gates flagged)")

# ---- (iv) determinism under PYTHONHASHSEED --------------------------
print("  (iv) DETERMINISM under PYTHONHASHSEED 0/7/999 (D63 W6b).  "
      "SCOPE, STATED: three full runs of this receipt would triple a "
      "runtime that is printed in its own output and could not be "
      "byte-identical for that reason alone, so the gate runs a "
      "DETERMINISTIC DIGEST of the pipeline under the three seeds and "
      "requires byte-identical stdout.  ROUND-1 MINOR 4, THE DIGEST "
      "WIDENED PAST CAP 3: the first delivery's digest covered the "
      "two-actor pipeline at cap 3 only, and therefore excluded the 3- "
      "and 4-actor pools, the whole of HZ4, the whole of HZ5 and the "
      "horn past depth 3 — i.e. every arm round 1 found a defect in.  "
      "The digest now carries: the two-actor family at CAP 4 (census, "
      "potentials under BOTH terminal conventions, the absolute drift "
      "sup and the PINNED conditional's horn separation), the THREE- "
      "and FOUR-ACTOR pools (census, potentials, matched drift cell), "
      "the HZ4 RENEWAL PREDICATE (R-SIG and R-MENU counts and "
      "menu-exactness through the layer's own View), and BOTH HZ5 "
      "sector maps' refinements at cap 4.  It is still a digest and "
      "not this receipt's whole stdout, and the wider claim is not "
      "made.")
_DIGEST = r'''
import sys
from collections import defaultdict
from fractions import Fraction as Fr
_s = open('v10/code/d42b1_transport_exact.py').read()
ns = {}
exec(compile(_s[:_s.index('print("[d42b1')], 'L', 'exec'), ns)
cf = ns['candidates_for']
View = ns['View']
event_poset = ns['event_poset']
V0 = ns['V0']
AB = ('A', 'B')
CAP = 4
def build_(actors, cap):
    C_ = {}
    fr_ = [()]
    while fr_:
        h = fr_.pop()
        C_[h] = cf(list(h), actors)
        if len(h) >= cap:
            continue
        for e, q in C_[h]:
            fr_.append(h + (e,))
    return C_
C = build_(AB, CAP)
def mkG_on(cache, term):
    memo = {}
    def G(h, r):
        if r == 0:
            return term(h)
        k = (h, r)
        if k not in memo:
            memo[k] = sum(q * G(h + (e,), r - 1) for e, q in cache[h])
        return memo[k]
    return G
def mkG(term):
    return mkG_on(C, term)
G1 = mkG(lambda h: Fr(1))
G2 = mkG(lambda h: Fr(len(C[h])))
def kr(G, h, r):
    t = G(h, r)
    return {e: q * G(h + (e,), r - 1) / t for e, q in C[h]}
def cond(k):
    s = defaultdict(lambda: Fr(0))
    for e, v in k.items():
        s[e[0]] += v
    return {e: v / s[e[0]] for e, v in k.items()}
out = [str(len(C))]
for r in range(1, CAP + 2):
    out.append(str(G1((), r)))
for r in range(1, CAP + 1):
    out.append(str(G2((), r)))
for r in (1, 2):
    b = Fr(0)
    for h in C:
        if len(h) + r + 1 > CAP + 1:
            continue
        a1, a2 = kr(G1, h, r), kr(G1, h, r + 1)
        b = max(b, max(abs(a2[e] - a1[e]) for e in a1))
    out.append(str(b))
for r in (1, 2):
    b = Fr(0)
    for h in C:
        if len(h) + r > CAP:
            continue
        c1, c2 = cond(kr(G1, h, r)), cond(kr(G2, h, r))
        b = max(b, max(abs(c2[e] - c1[e]) for e in c1))
    out.append(str(b))
BUD = {'p': 'propose', 'r': 'arb-merge', 'm': 'arb-merge',
       'd': 'deliver', 'n': 'idle'}
for MAP in ('type', 'budget'):
    sm = (lambda e: e[0]) if MAP == 'type' else (lambda e: BUD[e[0]])
    SIG = {}
    for h in C:
        t = defaultdict(lambda: Fr(0))
        for e, q in C[h]:
            t[sm(e)] += q
        SIG[h] = tuple(sorted(((s, v) for s, v in t.items()), key=repr))
    cls, keys = {}, {}
    for h in sorted(C, key=repr):
        keys.setdefault(SIG[h], len(keys))
        cls[h] = keys[SIG[h]]
    while True:
        nk, nc = {}, {}
        for h in sorted(C, key=repr):
            if len(h) >= CAP:
                key = ('cap', cls[h])
            else:
                agg = defaultdict(lambda: Fr(0))
                for e, q in C[h]:
                    agg[(sm(e), cls[h + (e,)])] += q
                key = (cls[h], tuple(sorted(agg.items(), key=repr)))
            nk.setdefault(key, len(nk))
            nc[h] = nk[key]
        st = len(nk) == len(set(cls.values()))
        cls = nc
        if st:
            break
    byd = defaultdict(set)
    for h in C:
        byd[len(h)].add(cls[h])
    out.append(str({d: len(v) for d, v in sorted(byd.items())}))
# ---- the wider pools (round-1 MINOR 4) -----------------------------
for actors in (('A', 'B', 'C'), ('A', 'B', 'C', 'D')):
    CP = build_(actors, 2)
    GP = mkG_on(CP, lambda h: Fr(1))
    out.append(str(len(CP)))
    for r in (1, 2, 3):
        out.append(str(GP((), r)))
# ---- the HZ4 renewal predicate (round-1 MINOR 4) -------------------
def rn(e, v):
    if e[0] == 'p':
        return ('p', e[1], v if e[2] == V0 else e[2], e[3])
    if e[0] == 'd':
        return ('d', e[1], e[2], v if e[3] == V0 else e[3])
    return e
nsig = nmenu = nexact = 0
for h in sorted((x for x in C if len(x) <= 3), key=repr):
    vw = View(list(h), event_poset(list(h)), set(range(len(h))))
    hold = {a: frozenset(vw.holdings(a)) for a in AB}
    nsu = {a: frozenset(x for x in hold[a] if x not in vw.superseded)
           for a in AB}
    if any(len(nsu[a]) != 1 for a in AB) or nsu['A'] != nsu['B']:
        continue
    if vw.live or vw.components():
        continue
    if any(vw.merge_pairs(a) for a in AB):
        continue
    v = next(iter(nsu['A']))
    nsig += 1
    if all(hold[a] == frozenset({v}) for a in AB):
        nmenu += 1
    if set(C[h]) == {(rn(e, v), w) for e, w in C[()]}:
        nexact += 1
out.append(f"{nsig},{nmenu},{nexact}")
sys.stdout.write("|".join(out))
'''
DIG = []
for seed in HASHSEEDS:
    env = dict(os.environ)
    env['PYTHONHASHSEED'] = str(seed)
    r = subprocess.run([sys.executable, '-c', _DIGEST], env=env,
                       capture_output=True, text=True, cwd=os.getcwd())
    DIG.append((seed, r.returncode, r.stdout))
det_ok = (len({d for s, rc, d in DIG}) == 1
          and all(rc == 0 for s, rc, d in DIG) and DIG[0][2] != "")
print(f"      digest = {DIG[0][2]}")
check("HZ6-iv DETERMINISM under PYTHONHASHSEED 0/7/999: the pipeline "
      "digest is byte-identical across the three seeds.  Everything in "
      "this receipt is exact-rational, seedless and sorted by repr; the "
      "gate exists because dict-built keys sorted by repr are exactly "
      "what a hash-seed change perturbs — and round 1's own probe of "
      "this receipt found that TWO EQUAL FROZENSETS CAN CARRY "
      "DIFFERENT REPRS in one process, so every menu comparison in "
      "HZ3-s1 and HZ4 was converted from a repr sort to a SET "
      "comparison as part of this repair.  SCOPE: the digest, widened "
      "past cap 3 to both wider pools, the renewal predicate and both "
      "HZ5 sector maps, but still not the whole stdout — said in the "
      "label so the gate is not read wider than it is",
      det_ok and len(DIG) == 3,
      f"seeds {[s for s, rc, d in DIG]}; return codes "
      f"{[rc for s, rc, d in DIG]}; distinct digests = "
      f"{len({d for s, rc, d in DIG})}")

# ======================================================================
# HZ7 — THE WALL CONTROL (diagnostic; changes nothing)
# ======================================================================
print(f"\n{sec()} [HZ7 — THE WALL CONTROL (diagnostic; changes "
      f"nothing)]")
print("  MANDATED LABEL, printed by the gate itself: THE COMMITTED "
      "LAYER IS UNCHANGED; NO OTHER NUMBER IN THIS RECEIPT USES THE "
      "RESTRICTED ENUMERATOR; ADOPTING IT WOULD BE A DIFFERENT THEORY "
      "AND IS NOT PROPOSED.")
ns7 = {}
exec(compile(_PREFIX, 'd42b1_port_restricted', 'exec'), ns7)


def restricted_deliver(view, a, actors):
    """deliver_options_in_view with the holdings set restricted to
    NON-SUPERSEDED members — the one-line change the B1 ladder rides
    on.  Confined to namespace ns7."""
    return sorted(((r, v) for r in actors if r != a
                   for v in view.holdings(a) if v not in view.superseded),
                  key=repr)


ns7['deliver_options_in_view'] = restricted_deliver
cf7 = ns7['candidates_for']
adm7 = ns7['admissible']
vname7 = ns7['vname']
ep7 = ns7['event_poset']
View7 = ns7['View']
V07 = ns7['V0']

LAD7 = []
_h = []
_v = V07
for k in range(1, 11):
    _t3 = ('A', _v, 0)
    _e1 = ('p', 'A', _v, 0)
    ok1, q1 = adm7(_h, _e1, AB)
    _h = _h + [_e1]
    _e2 = ('r', 'A', frozenset({_t3}), frozenset({_t3}))
    ok2, q2 = adm7(_h, _e2, AB)
    _h = _h + [_e2]
    _v = vname7(_v, frozenset({_t3}), 'A')
    _vw = View7(_h, ep7(_h), set(range(len(_h))))
    men = cf7(_h, AB)
    dels = [(e, q) for e, q in men if e[0] == 'd' and e[1] == 'A']
    LAD7.append((k, ok1 and ok2, len(_vw.holdings('A')), len(dels),
                 sorted({str(q) for e, q in dels}),
                 sum(q for e, q in dels), len(men)))
print("      rung | admissible | |holdings(A)| | #delivery-options | "
      "weight each | delivery sector total | |menu|")
for k, ok, nh, nd, ws, tot, nm in LAD7:
    _w = ws[0] if len(ws) == 1 else str(ws)
    print(f"      {k:4d} | {str(ok):>10} | {nh:13d} | {nd:17d} | "
          f"{_w:>11} | {tot} | {nm}")
r7_admissible = all(ok for k, ok, nh, nd, ws, tot, nm in LAD7)
r7_hold_grows = [nh for k, ok, nh, nd, ws, tot, nm in LAD7] \
    == list(range(2, 12))
r7_dels = {nd for k, ok, nh, nd, ws, tot, nm in LAD7}
r7_menus = {nm for k, ok, nh, nd, ws, tot, nm in LAD7[1:]}
r7_bounded = len(r7_dels) == 1 and len(r7_menus) == 1
committed_unchanged = (ns['deliver_options_in_view']
                       is deliver_options_in_view
                       and ns['deliver_options_in_view']
                       is not restricted_deliver)
_c_del = deliver_options_in_view(
    View(list(WIT), event_poset(list(WIT)), set(range(3))), 'A', AB)
_r_del = restricted_deliver(
    View(list(WIT), event_poset(list(WIT)), set(range(3))), 'A', AB)
check("HZ7 THE B1 LADDER DOES NOT SURVIVE THE RESTRICTED ENUMERATOR — "
      "DIAGNOSTIC ONLY.  With deliver_options_in_view restricted to "
      "non-superseded holdings inside a SEPARATE namespace, the ladder "
      "is still admissible at every rung and |holdings(A)| still grows "
      "without bound, but the delivery menu collapses to a constant "
      "cardinality and the whole menu is constant from rung 2 on.  So "
      "the B1 obstruction, as constructed, rests on that one line of "
      "the committed layer, and it does NOT harden from 'a fact about "
      "one line' to 'a fact about transport' on this evidence.  WHAT "
      "THIS DOES NOT SHOW, said in the gate: that any bounded "
      "abstraction exists under the restricted enumerator — only that "
      "THIS ladder stops being a witness.  The committed layer object "
      "is gated to be untouched",
      r7_admissible and r7_hold_grows and r7_bounded
      and committed_unchanged and len(_c_del) > len(_r_del),
      f"every rung admissible = {r7_admissible}; |holdings(A)| = k+1 = "
      f"{r7_hold_grows}; distinct delivery-option counts over 10 rungs "
      f"= {sorted(r7_dels)}; distinct menu sizes from rung 2 = "
      f"{sorted(r7_menus)}; committed enumerator object unchanged = "
      f"{committed_unchanged} (committed gives {len(_c_del)} options at "
      f"the MB5 witness, restricted gives {len(_r_del)})")

# ======================================================================
# HZ8 — DOCTRINE
# ======================================================================
print(f"\n{sec()} [HZ8 — DOCTRINE]")
_N1 = "conver" + "g"
_N2 = "infinite-" + "volume"
_N3 = "bound" + "ary theorem"
_N4 = "limit " + "measure"
_N5 = "limit " + "kernel"
_NEEDLES = (_N1, _N2, _N3, _N4, _N5)
_MARK = ('scan-exempt', 'horizon-scoped', 'finite-horizon',
         'over the computed horizons', 'no ' + _N2,
         'explicitly not a ' + _N3, 'not a ' + _N3, 'needle',
         'no claim')


def has_needle(text, needles=None):
    """A needle counts only at a WORD START.  Without this the scanner
    fires on 'reconvergence' — the name of D46b's own MB5 witness —
    which is a different word and not an existence claim.  The boundary
    rule is stated here rather than patched into the marker list,
    because adding the witness's name to the exemptions would be a
    loophole and not a rule."""
    low = text.lower()
    for nd in (_NEEDLES if needles is None else needles):
        p = low.find(nd)
        while p != -1:
            if p == 0 or not low[p - 1].isalpha():
                return True
            p = low.find(nd, p + 1)
    return False


def needle_scan(lines):
    return [i + 1 for i, ln in enumerate(lines)
            if has_needle(ln) and not any(m in ln.lower() for m in _MARK)]


_lines = _self_src.splitlines()
NEEDLE_HITS = [i + 1 for i, ln in enumerate(_lines) if has_needle(ln)]
UNDISCLAIMED = needle_scan(_lines)
_pb2 = ["the transport kernel " + _N1 + "es to a " + _N4]
_pg2 = ["the drift contracts over the computed horizons; no " + _N2
        + " claim (scan-exempt: needle literal)"]


scan_fires = (needle_scan(_pb2) == [1] and needle_scan(_pg2) == [])
check("HZ8-a NO INFINITE-VOLUME CLAIM, SCANNED RATHER THAN ASSERTED "
      "(D46b MB6, binding; the d46c KG3 pattern).  Every line of this "
      "file carrying one of the three needle roots must also carry a "
      "POSITIVE scope marker saying in the line itself that the "
      "statement is finite-horizon, horizon-scoped, or explicitly "
      "withheld.  The scanner is probed both ways: it must flag a "
      "synthetic undisclaimed existence assertion and must pass a "
      "properly scoped line",
      not UNDISCLAIMED and len(NEEDLE_HITS) >= 5 and scan_fires,
      f"needle lines = {len(NEEDLE_HITS)} of {len(_lines)}; "
      f"undisclaimed = {UNDISCLAIMED if UNDISCLAIMED else 'none'}; "
      f"scanner fires both ways = {scan_fires}")

check("HZ8-c NORMALIZATION NAMED AT EVERY USE (D46d BLOCKER B2), CAPS "
      "AND POOLS PRINTED, NO SAMPLED ARM.  Three normalizations appear "
      "in this receipt and each is named where it is used: the RAW "
      "committed weight q (HZ1-c cut masses, HZ4-ii, HZ4-iii), the "
      "horizon-completed kernel k^C1_r (HZ1, HZ2, HZ4-ii, HZ4-iv), and "
      "the SECTOR-NORMALIZED CONDITIONAL, which is the PINNED object "
      "(HZ0-7, HZ2, HZ3).  Absolute completed weights are horizon-bound "
      "(D44f) and are carried as context only.  No arm of this receipt "
      "is sampled, so the D46d exact/sampled separation is vacuous here "
      "by construction and is reported as such rather than claimed as a "
      "discipline exercised",
      len(NORMS) == 5 and CAP_T == 6 and len(POOLS) == 3
      and len(HZ5_CAPS) == 4,
      f"caps: transport {CAP_T}, pools {[c for nm, a, c, ca, g in POOLS]}"
      f", delivery-free {CAP_DF}, HZ5 {HZ5_CAPS}, negative control "
      f"{CAP_NEG}, renewal window {SD_DEPTH}; sampled arms = 0")

# HZ8-b RUNS LAST so that its scan is TOTAL (round-1 MINOR 2: the first
# delivery's scan saw 40 of 42 labels because two gates were delivered
# after it).  Its own label is folded in before the predicate is taken,
# so the coverage is N of N including this line.
_HZ8B = ("HZ8-b THE PIN'S OWN LEXICAL PROHIBITION, ENFORCED ON THIS "
         "RECEIPT'S GATE LABELS, AND THE SCAN MADE TOTAL (ROUND-1 "
         "MINOR 2).  The pin (HZ2) forbids the word rooted at the "
         "needle above from appearing in any label unless HZ4 supplies "
         "a bound; HZ4 supplied none (HZ4-iv), so the required wording "
         "is 'contracts over the computed horizons'.  This gate is now "
         "the LAST gate of the receipt and its own label is included "
         "in the scanned text, so every check() label delivered by "
         "this run — all of them, including this one — is concatenated "
         "and searched.  The gate is conditional on HZ4's actual "
         "outcome and not on an assumption about it")
_LBL = " ".join(GATE_LABELS + [_HZ8B])
_forbidden_word_present = has_needle(_LBL, (_N1,))
check(_HZ8B,
      (not _forbidden_word_present) or (HZ4_BOUND is not None),
      f"HZ4 bound printed = {HZ4_BOUND is not None}; labels scanned = "
      f"{len(GATE_LABELS) + 1} of {len(GATE_LABELS) + 1} (this gate "
      f"included); forbidden root present = {_forbidden_word_present}")

# ======================================================================
# THE PRE-REGISTERED OUTCOME
# ======================================================================
print(f"\n{sec()} [THE PRE-REGISTERED OUTCOME — assembled from the "
      f"computed predicates above, never asserted]")

print("  THE PIN'S HZ-I HAS THREE CLAUSES AND EACH IS EVALUATED "
      "SEPARATELY, because the receipt found a fourth thing the pin "
      "did not pre-register and must not be silently folded into one "
      "of them.  HZ-I fires iff: (a) 'the family-uniform drift stops "
      "contracting at reachable r', OR (b) 'contracts at the root "
      "while failing family-wide', OR (c) 'fails at wider pools'.")
print("  ROUND-1 MAJOR 2, THE DECISION OBJECT NAMED ONCE AND USED "
      "EVERYWHERE.  Each clause is evaluated on THE PINNED "
      "SECTOR-NORMALIZED CONDITIONAL, because the pin §6 and §2 say "
      "the pinned object is the sector-normalized conditional and that "
      "absolute completed weights are horizon-bound (D44f) CONTEXT.  "
      "The first delivery applied that doctrine at HZ3-b and at §4.3 "
      "and then evaluated clause (c) on the ABSOLUTE rows, which is "
      "the direction that maximised the delivered negative.  Both "
      "readings are computed and printed here; the DELIVERED one is "
      "the pinned one, and the absolute one is printed beside it as "
      "context and labelled as such.  ROUND-1 MODERATE 9: the "
      "family-uniform clause is read on the OFF-ROOT-WINDOW prefix, "
      "since the deepest horizon's window holds the root alone.")
PIN_NORMS = [n for n in NORMS if 'CONDITIONAL' in n]
ABS_NORMS = [n for n in NORMS if 'CONDITIONAL' not in n]
ROW_BAD_OFF_PIN = [(n, L) for (n, L) in ROW_BAD_OFFROOT
                   if 'CONDITIONAL' in n]
ROW_BAD_ROOT_PIN = [(n, L) for (n, L) in ROW_BAD_ROOT
                    if 'CONDITIONAL' in n]
HZI_a = not all(contracts_from_first_nonzero(UNI2_OFFROOT[nm])
                for nm in PIN_NORMS)
HZI_a_abs = not all(contracts_from_first_nonzero(UNI2_OFFROOT[nm])
                    for nm in ABS_NORMS)
HZI_b = (not ROW_BAD_ROOT_PIN) and bool(ROW_BAD_OFF_PIN)
HZI_c = any(POOLROWBAD_OFF_PIN[nm] for nm in POOLROWBAD_OFF_PIN)
HZI_c_abs = any(POOLROWBAD_OFF_ABS[nm] for nm in POOLROWBAD_OFF_ABS)
HZI = HZI_a or HZI_b or HZI_c
HZI_LETTER_ABS = HZI_a_abs or HZI_c_abs
UNREGISTERED = bool(ROW_BAD_ROOT) and not ROW_BAD_OFFROOT
print(f"      ON THE PINNED OBJECT — THE DELIVERED READING:")
print(f"      (a) family-uniform sequences stop contracting = {HZI_a}")
print(f"      (b) root contracts while the family fails = {HZI_b}")
print(f"      (c) a wider pool's off-root rows fail          = {HZI_c}")
print(f"      => HZ-I fires ON THE PIN'S OWN OBJECT = {HZI}")
print(f"      ON THE ABSOLUTE KERNEL (D44f context, NOT the decision "
      f"object): (a) = {HZI_a_abs}, (c) = {HZI_c_abs}, so the "
      f"LETTER-READING the first delivery took would fire = "
      f"{HZI_LETTER_ABS} — on the four-actor L = 1 row, whose rise "
      f"HZ2-BLIP shows reverses at the very next horizon and ends "
      f"below its first term in two of three absolute norms.")
print(f"      NOT A PIN CLAUSE, and delivered separately at HZ2-d: the "
      f"root's ABSOLUTE row fails while every off-root row contracts = "
      f"{UNREGISTERED}.  This is the MIRROR IMAGE of clause (b) and "
      f"the pin did not pre-register it in either direction; it is "
      f"reported as its own outcome and is NOT counted as HZ-I.")

CAUCHY_OK = not HZI
POOL_OK = not HZI_c
PROPER_OK = (prop_bad == 0 and pos_bad == 0 and neg_bad == 0
             and chain_bad == 0)
INSTRUMENT_OK = true_contracts and bool(BREAKERS)
CONV_SEPARATES = horn_separates
CONV_SHRINKS = horn_shrinks and horn_cond_shrinks

if not PROPER_OK:
    FIRED = 'HZ-IV'
elif HZI or not INSTRUMENT_OK:
    FIRED = 'HZ-I'
elif CONV_SEPARATES and not CONV_SHRINKS:
    FIRED = 'HZ-II'
else:
    FIRED = 'HZ-III (bound clause NOT satisfied)' if HZ4_BOUND is None \
        else 'HZ-III'
HZ5_FIRED = 'HZ5-b' if not (type_closes or budget_closes) else 'HZ5-a'

# Every clause of both outcomes and of the verdict is BUILT from a
# computed quantity (the D46b B-A3(b) lesson: a flipped gate must not
# leave an asserting headline behind).
_v_proper = (f"properness holds family-wide out to relative horizon "
             f"{R_MAX} (D46b had r = 1, 2) and the chained kernel is "
             f"cut-additive at every cut while the raw weight is not "
             f"(raw cut masses {frl(CUTS[:4])}, ...), so HZ-IV does "
             f"NOT fire"
             if PROPER_OK else
             "PROPERNESS FAILS on the declared family, which is "
             "outcome HZ-IV: the finite-horizon objects are not "
             "measures and the defect is printed at HZ1")
_v_cauchy = (f"the drift CONTRACTS OVER THE COMPUTED HORIZONS at every "
             f"fixed OFF-ROOT history depth, in all five norms, over a "
             f"family of {CUM[-1]} histories, and every family-uniform "
             f"row contracts too"
             + (f"; but the ROOT's ABSOLUTE row does NOT — it falls "
                f"through D46b's five steps and RISES at the sixth, "
                f"which is the mirror image of the pin's falsifier 2 "
                f"and is delivered as its own outcome"
                if UNREGISTERED else "")
             if not (HZI_a or HZI_b) else
             "the two-actor arm's drift fails one of the pin's first "
             "two HZ-I clauses")
_v_pool = ("and IT CONTRACTS AT EVERY OFF-ROOT DEPTH AT ALL THREE ACTOR "
           "POOLS, at every depth each pool's cap can reach, ON THE "
           "PINNED OBJECT — the four-actor pool included, now that it "
           "is built to depth 4.  The horizon-bound ABSOLUTE kernel, "
           "carried as D44f context and not folded into this verdict, "
           "has exactly one non-monotone off-root family of rows: the "
           "four-actor L = 1 row in the three absolute norms, which "
           "RISES by 0.19% / 3.06% / 14.95% at r = 2 -> 3 and then "
           "FALLS by 11.28% / 4.87% / 4.87% at r = 3 -> 4, ending "
           "BELOW its first term in L-infinity and in L1.  On a "
           "two-term window that row is what the first delivery fired "
           "the pin's HZ-I clause (c) on; with its third term it is a "
           "one-step blip, and the unit's own three-actor ROOT row had "
           "the same shape (a x1.50 rise at step 2, a fall at step 3).  "
           "The drift MAGNITUDE also falls with actor pool in every "
           "matched cell, in all five norms"
           if POOL_OK else
           "BUT THE PINNED OBJECT DOES NOT CONTRACT AT THE WIDEST "
           "POOL: "
           + "; ".join(
               f"{nm} at depth L = {L} in {n2}, cap {cap}, "
               f"{len(seq)} terms, rises by {rise} "
               f"(~{float(rise) * 100:.2f}%)"
               for nm, n2, L, cap, rs, seq, rise in OFFROW_DETAIL
               if 'CONDITIONAL' in n2)
           + " — that is the pin's HZ-I clause (c) and its falsifier 4, "
           "taken on the pin's own object")
_v_window = (f"the sup is WINDOW-DEPENDENT and grows on the deeper "
             f"family at r = {[r for r, a, b, g in wider if g]}, so "
             f"D46b's committed four-term sequence is a lower bound on "
             f"the deeper family's sup"
             if any(g for r, a, b, g in wider) else
             "the sup is unchanged on the deeper family at every "
             "committed r")
_v_horn = (("the two declared terminal conventions separate at EVERY "
            "history in the absolute kernel; at the ROOT the pinned "
            "conditional cannot separate at all — that is the "
            "symmetry THEOREM of HZ3-s2, not a measurement — and OFF "
            "the root the pinned separation SHRINKS in r at every "
            "fixed depth, from 1/8 down over five terms (family-wide "
            "absolute sup " + frl(horn_abs) + "; family-wide "
            "conditional sup " + frl(horn_cond) + ", whose last entry "
            "is the root-only window artifact of HZ2-e), so horn (I) "
            "does NOT fire as a non-shrinking separation and HZ-II is "
            "not the outcome.  The absolute kernel INHERITS the "
            "convention; the pinned conditional is protected by "
            "symmetry at the root and measured to shrink off it")
           if CONV_SEPARATES and CONV_SHRINKS else
           ("the two declared terminal conventions separate in the "
            "PINNED object by an amount that does NOT shrink in r — "
            "THE IMPORTED COMPLETION HORN (I) AT TRANSPORT SCOPE, and "
            "the difference is the deliverable: absolute sup "
            + frl(horn_abs) + ", conditional sup " + frl(horn_cond))
           if CONV_SEPARATES else
           "the two declared terminal conventions agree ENTRYWISE at "
           "every computed horizon")
_v_bound = ("HZ4 exhibited NO BOUND.  THE MENU-EXACT ATOM ROUTE IS "
            "CLOSED and nothing wider is: holdings never shrink, so "
            "the MENU-EXACT renewal class R-MENU is absorbing-"
            f"complement — {MENU_REENTRY} re-entries over "
            f"{len(RMENUSET)} points — the never-regenerating set "
            f"carries {float(nonren_k):.4f} of the horizon-completed "
            f"mass at depth {SD_DEPTH}, and the N-step hitting "
            "probability into R-MENU is EXACTLY zero for every history "
            "past the first creation event.  BUT THE SIGMA-LEVEL "
            "CLASS R-SIG — the literal D62 row-R4 port, which is what "
            "D69's R5 actually names — IS A DIFFERENT OBJECT AND IS "
            f"OPEN: it is re-entered {SIG_REENTRY} times, its "
            "zero-set collapses with N ("
            + " -> ".join(str(nz) for N, tot, nz, w in MIN_ROWS_SIG)
            + f"), and at N = 4 NO history in the window has hitting "
            f"probability 0 and the infimum is {MIN_ROWS_SIG[3][3]} "
            f"(~{float(MIN_ROWS_SIG[3][3]):.4f}) — the shape of a "
            "Doeblin condition, on a 9-history window that is NOT a "
            "bound and from which none is claimed.  The layer's own "
            "reason is printed at HZ4-ii(a): holdings grow, but "
            "'superseded' grows too, so NON-superseded holdings shrink "
            "— which is exactly why the absorbing-complement argument "
            "covers R-MENU and cannot cover R-SIG.  Classical Doeblin "
            "minorization needs no atom at all, and NO OPERATOR-LEVEL "
            "MINORIZATION (Birkhoff / Hilbert-metric contraction of "
            "the positive backward recursion G) was attempted anywhere "
            "in this receipt.  So D69's route R5 is NARROWED, not "
            "closed: the MENU-EXACT ATOM route is closed, THE "
            "SIGMA-LEVEL RENEWAL ROUTE IS OPEN, and operator-level "
            "minorization is the campaign's named successor proof "
            "engine"
            if HZ4_BOUND is None else
            f"HZ4 exhibited a minorization constant: {HZ4_BOUND}")
_v_licence = ("so what is delivered is HZ-III's SHAPE WITHOUT HZ-III's "
              "LICENCE: the standing label is the pin's own "
              "'root-free over the computed horizons', explicitly not "
              "a boundary theorem (scan-exempt: needle), and no HZ2 "
              "label is upgraded"
              if HZ4_BOUND is None and FIRED.startswith('HZ-III') else
              "the licence question is moot at this outcome")
_v_instr = ("the instrument can fail: on the same window the perturbed "
            "law does NOT contract while the true law does"
            if INSTRUMENT_OK else
            "THE INSTRUMENT COULD NOT FAIL — the pin's falsifier 1 "
            "fires and every HZ2 number above is VOID")
_v_hz5 = (("BOTH coarser aggregations FAIL D57's last-two-caps decider "
           "at every comparable depth, with the S4 trivial-boundary "
           "control transferring to both maps so the counts are LOWER "
           "BOUNDS and the negative is the conservative reading, and "
           "with a depth-3 class exhibited splitting between cap 5 and "
           "cap 6 at each map.  So the aggregation wall extends from "
           "D57's (actor, type) granularity to the two coarsest maps "
           "the corpus had named.  BUT THAT IS ONE CLOSED ROUTE, NOT "
           "TWO: HZ5-4 gates that no menu entry of kind 'm' occurs "
           f"below parent depth {M_FIRST_PARENT}, so on the decider's "
           f"whole input (depths {DECIDER_DEPTHS}) BUDGET-ONLY is a "
           "bijective relabelling of TYPE-ONLY and the two maps induce "
           "the IDENTICAL partition at every cap.  D69's route R1 "
           "closes ON MEASUREMENT and route R2's closure is INHERITED, "
           "not measured; extending R2 to a cap where merges have "
           "support is the residue")
          if not (type_closes or budget_closes) else
          ("at least one coarser aggregation CLOSES the fixpoint at "
           "these caps — Perron reopens in aggregated form and the "
           "D57 wall is granularity-specific: type-only closes = "
           f"{type_closes}, budget-only closes = {budget_closes}"))
_v_wall = ("the B1 ladder does NOT survive the restricted enumerator, "
           "so the obstruction as constructed rests on that one line "
           "of the committed layer"
           if r7_bounded else
           "the B1 ladder SURVIVES the restricted enumerator, so the "
           "obstruction hardens from a fact about one line to a fact "
           "about transport")

outcome(FIRED,
        f"THE HORIZON-LIMIT ROUTE, AT THE DECLARED CAPS.  {_v_proper}. "
        f"{_v_cauchy}, {_v_pool} — but {_v_window}.  {_v_horn}.  "
        f"{_v_bound}, {_v_licence}.")
outcome(HZ5_FIRED,
        f"THE AGGREGATION ARM, independent of everything above.  "
        f"{_v_hz5}.  The finite-alphabet prerequisite was gated FIRST "
        f"and SEPARATELY and is left [OPEN] in both directions, as "
        f"D69 §6 requires of any citation of it.")

WALL = time.time() - T00
print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL, OF WHICH "
      f"{len(THEOREM_GATES)} ARE THEOREM-PASSES THAT CANNOT FAIL   "
      f"({len(OUT)} delivered outcomes)   wall clock {WALL:.1f}s")
print(f"[THEOREM-PASSES] ROUND-1 MODERATE 7: '{PASS} PASS' is NOT "
      f"{PASS} tests.  The gates that cannot fail, each with its "
      f"reason, so the count is never read as evidence it is not:")
for _gid, _why in THEOREM_GATES:
    print(f"    {_gid:12s} {_why}")
print(f"    => {PASS - len(THEOREM_GATES)} of the {PASS} passes are "
      f"gates that could have returned False on this family.")
print(f"[RUNTIME] family builds dominate: two-actor depth {CAP_T} "
      f"{_TBUILD:.1f}s, THREE-actor depth {CAP_3} {_T3BUILD:.1f}s, "
      f"FOUR-actor depth {CAP_4} {_T4BUILD:.1f}s (serial, single-core, "
      f"the round-1 MAJOR 1 arm and the reason this is the campaign's "
      f"longest receipt), delivery-free depth {CAP_DF} "
      f"{_DFBUILD:.1f}s; total {WALL:.1f}s.  Nothing was cut: every arm "
      f"the pin declares ran, including HZ5, which the pin allowed to "
      f"be dropped.")

print(f"\n[VERDICT] D70 ROUND-1 REVIEWED AND REPAIRED, outcome {FIRED} "
      f"+ {HZ5_FIRED}.  Every clause below is built from a gated "
      f"quantity above and cannot contradict it.  "
      f"PROPERNESS: {_v_proper}.  "
      f"THE CAUCHY TABLE: {_v_cauchy}, {_v_pool}; and {_v_window}.  "
      f"THE HORN: {_v_horn}.  "
      f"THE LEMMA SLOT: {_v_bound} — {_v_licence}.  "
      f"THE AGGREGATION ARM: {_v_hz5}.  "
      f"CONTROLS: {_v_instr}; the delivery-free positive control "
      f"reproduces ker(T - 2I) as one positive ray with values "
      f"{EIG['2'][2]} and T f = 2 f exactly, lambda = 2 used only as "
      f"an asymptotic eigenvalue; the anti-vacuity scan flagged "
      f"{len(TAUT)} of {NGATES} gate predicates, with its hoisting "
      f"defect named; the pipeline digest is byte-identical under "
      f"PYTHONHASHSEED {HASHSEEDS} across "
      f"{len({d for s, rc, d in DIG})} distinct value(s).  "
      f"THE WALL CONTROL (diagnostic, changes nothing): {_v_wall} — the "
      f"committed layer is unchanged, no other number here uses the "
      f"restricted enumerator, and adopting it would be a different "
      f"theory and is not proposed.  "
      f"SCOPE: transport scope, the declared families and caps only; no "
      f"infinite-volume claim (scan-exempt: needle literal) under any "
      f"outcome; no dimension, typicality or quantum-layer claim; the "
      f"missing map is untouched.")
sys.exit(0)
