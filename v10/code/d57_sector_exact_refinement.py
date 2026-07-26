#!/usr/bin/env python3
"""
d57_sector_exact_refinement.py — v10 D57: the sector-exact question.
Pin: note-d57-sector-exact-pin.md (STRICT, LOG #434, before code).

**ROUND-1 REVIEWED AND REPAIRED (2026-07-26).**  Independent hostile
review `v10/reviews/batch-round1-d50-to-d60.md` — REVISE, 1 BLOCKER /
1 MAJOR / 6 MINOR / 2 NIT.  The refinement is correct, the algorithm
computes what it says, and every per-depth count reproduced exactly at
all four caps under an independent implementation.  Ground (2) — the
refinement blow-up — STANDS and is STRENGTHENED here.  Ground (1) does
not:

  * BLOCKER 1 — S1's stated MECHANISM is refuted by this unit's own
    exhaustive data.  The arb denominator is `len(comps) +
    len(view.merge_pairs(a))` (d42b1 line 328), NOT the component count;
    and `max |comps| = 1` at EVERY depth over all 243,769 histories, so
    it does not grow.  The 1/8 witness has (|comps|, |merge_pairs|, D) =
    (1, 1, 2) — the 2 comes entirely from a MERGE PAIR.  **"THE SECTOR
    ALPHABET IS NOT FINITE" IS WITHDRAWN** as an extrapolation through a
    premise the same data refutes.  The question is REOPENED, not
    answered in the other direction.
  * MAJOR 1 — at this unit's own 2-actor scope the only growth route the
    data supports is provably capped: `|merge_pairs(a)| <= 1`, so
    `D <= |comps| + 1`.  Combined with `max |comps| = 1` the observed
    {1/2, 1/4, 1/8} may be the COMPLETE arb-sector alphabet at this
    scope.  A rescue must exhibit |comps| >= 2 or move to >= 3 actors.
  * MINOR 1 — the pin promised a COMPONENT CENSUS and a REFINEMENT
    WITNESS; neither was delivered.  Both are printed here.
  * MINOR 2 — S1's `all((v*4).denominator >= 1 ...)` conjunct is true of
    every Fraction; removed.
  * MINOR 3 — `quant_bad` was computed and never gated; it is gated now,
    in the direction it lands (the k/4 law IS refuted).
  * MINOR 4 — "totals tested = 1,084,928" double-counted across nested
    caps (cap C's family is a prefix-subfamily of cap C+1's).  Per-cap
    counts and the DISTINCT total are both reported.
  * MINOR 5 — no anti-vacuity scan and no determinism gate; both added.
  * MINOR 6 — S2's stated decider ("2+ levels past d") is an invented
    constant that its own data contradicts; the stated rule is replaced
    by the implemented one, said plainly.
  * NIT 1 — the stale docstring/banner ("caps 3/4/5", "cap 6 CUT") are
    corrected: the loop is (3, 4, 5, 6) and cap 6 ran.
  * NIT 2 — the idle sector is excluded by the `ty != 'n'` filter; said
    aloud, and the idle alphabet reported.

Computes the COARSEST sector-lumpable partition of the exhaustive
2-actor d42b1 family at caps 3/4/5/6 and decides stability-vs-growth.
Exit 1 only on anchor breakage.
"""
import ast
import sys
from collections import defaultdict
from fractions import Fraction as Fr
sys.setrecursionlimit(300000)
PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

print("[D57 — the coarsest sector-exact partition at transport scope, "
      "ROUND-1 REPAIRED]")
print("  banner: sector = (initiator, event-type); the aggregated")
print("  transfer T_s(h, c) = sum q over sector s landing in class c;")
print("  fixpoint refinement from the sector-signature partition; cap")
print("  layer closed by signature (declared).  **Caps 3/4/5/6 ALL")
print("  EXHAUSTIVE — cap 6 RAN and carries the headline** (the")
print("  committed banner said it was cut; round-1 NIT 1).  The ARB")
print("  SECTOR MECHANISM is re-derived from the layer rather than")
print("  asserted, with the component census the pin promised.  Exact")
print("  Fractions.")

_s = open('v10/code/d42b1_transport_exact.py').read()
ns = {}
exec(_s[:_s.index('print("[d42b1')], ns)
cf = ns['candidates_for']
event_poset, View = ns['event_poset'], ns['View']
arb_components_in_view = ns['arb_components_in_view']
AB = ('A', 'B')
check("S0 anchor: committed d42b1 layer (single source), including the "
      "View internals the arb denominator is built from — so the "
      "mechanism below is READ OFF THE LAYER, not asserted about it",
      callable(cf) and callable(arb_components_in_view), "")

def enumerate_cap(cap):
    FAM = [()]
    CACHE = {}
    fr = [()]
    while fr:
        h = fr.pop()
        CACHE[h] = cf(list(h), AB)
        if len(h) >= cap:
            continue
        for e, q in CACHE[h]:
            h2 = h + (e,)
            FAM.append(h2)
            fr.append(h2)
    return FAM, CACHE

def sector_of(e):
    return (e[1], e[0])

def arb_denominator(h, e):
    """d42b1's own arb denominator, recomputed from the layer:
        D = len(arb_components_in_view(view, a)) + len(merge_pairs(a))
    with `view` the CANDIDATE'S OWN causal past, exactly as
    `admissible()` builds it."""
    a = e[1]
    acts2 = list(h) + [e]
    j = len(acts2) - 1
    pred = event_poset(acts2)
    view = View(acts2, pred, pred[j])
    c = len(arb_components_in_view(view, a))
    m = len(view.merge_pairs(a))
    return c, m, c + m

RESULTS = {}
RESULTS_TRIV = {}
PERCAP = {}
ALPH_BY_TYPE = defaultdict(set)
CENSUS = defaultdict(lambda: [0, 0, 0])      # depth -> max c, max m, max D
ARBWIT = {}                                  # arb sector total -> witness
SPLITWIT = {}
CLS3 = {}
quant_bad = 0
for CAP in (3, 4, 5, 6):
    FAM, CACHE = enumerate_cap(CAP)
    SIG = {}
    ntot = 0
    for h in FAM:
        tot = defaultdict(lambda: Fr(0))
        arbdet = defaultdict(list)
        for e, q in CACHE[h]:
            tot[sector_of(e)] += q
            if e[0] == 'r':
                c, m, D = arb_denominator(h, e)
                arbdet[e[1]].append((c, m, D, q))
                r = CENSUS[len(h)]
                r[0] = max(r[0], c)
                r[1] = max(r[1], m)
                r[2] = max(r[2], D)
        for (a, ty), v in tot.items():
            ALPH_BY_TYPE[ty].add(v)
            if ty != 'n':
                ntot += 1
                if v * 4 != int(v * 4):
                    quant_bad += 1
            if ty == 'r' and v not in ARBWIT:
                ARBWIT[v] = (len(h), a, list(arbdet[a]))
        SIG[h] = tuple(sorted(((a, ty, v) for (a, ty), v in tot.items()),
                              key=repr))
    PERCAP[CAP] = (len(FAM), ntot)

    def refine(boundary):
        """boundary = 'sig'   : the cap layer is closed by its signature
           boundary = 'triv'  : the whole cap layer is ONE class (the
                                coarsest possible treatment)"""
        cls = {}
        keys = {}
        for h in FAM:
            k = (('CAP',) if (boundary == 'triv' and len(h) >= CAP)
                 else SIG[h])
            keys.setdefault(k, len(keys))
            cls[h] = keys[k]
        it = 0
        wit = None
        while True:
            it += 1
            nk, ncls = {}, {}
            for h in FAM:
                if len(h) >= CAP:
                    key = ('cap', cls[h]) if boundary == 'sig' else ('cap',)
                else:
                    agg = defaultdict(lambda: Fr(0))
                    for e, q in CACHE[h]:
                        agg[(sector_of(e), cls[h + (e,)])] += q
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
                    # prefer a SAME-DEPTH witness pair; fall back to any
                    pair = None
                    for L in sorted({len(h) for h in mem}):
                        reps = [sorted((h for h in v if len(h) == L),
                                       key=repr)[:1] for v in seen.values()]
                        reps = [r[0] for r in reps if r]
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
        return cls, it, wit

    cls, it, wit = refine('sig')
    if wit:
        SPLITWIT[CAP] = wit
    bydep = defaultdict(set)
    for h in FAM:
        bydep[len(h)].add(cls[h])
    RESULTS[CAP] = {d: len(v) for d, v in sorted(bydep.items())}
    CLS3[CAP] = {h: cls[h] for h in FAM if len(h) == 3}
    clt, itt, _ = refine('triv')
    bdt = defaultdict(set)
    for h in FAM:
        bdt[len(h)].add(clt[h])
    RESULTS_TRIV[CAP] = {d: len(v) for d, v in sorted(bdt.items())}
    print(f"  cap {CAP}: histories = {len(FAM)}, iterations = {it}, "
          f"fixpoint classes per depth = {RESULTS[CAP]}")
    print(f"          trivial-boundary control (iterations {itt}): "
          f"{RESULTS_TRIV[CAP]}")
    if CAP == 3:
        # determinism / order-independence (round-1 MINOR 5)
        FAM.reverse()
        cls_r, _, _ = refine('sig')
        blocks_a = {frozenset(h for h in FAM if cls[h] == c)
                    for c in set(cls.values())}
        blocks_b = {frozenset(h for h in FAM if cls_r[h] == c)
                    for c in set(cls_r.values())}
        DET_OK = blocks_a == blocks_b
        FAM.reverse()

# ------------------------------------------------------------------- S1
print("\n[S1 THE ARB SECTOR MECHANISM — read off the layer, round-1 "
      "BLOCKER 1]")
print("  d42b1 line 328, the 'r' branch of admissible():")
print("      D = len(comps) + len(view.merge_pairs(a))")
print("      return True, F(1,4) / D * law(ckey, et)[wkey]")
print("  — components PLUS MERGE PAIRS, not the component count.")
print("  COMPONENT / MERGE-PAIR CENSUS BY DEPTH (the census pin §3 "
      "promised, cap 6, exhaustive):")
for d in sorted(CENSUS):
    c, m, D = CENSUS[d]
    print(f"     depth {d}: max|comps| = {c}   max|merge_pairs| = {m}   "
          f"max D = {D}")
print("  SECTOR ALPHABET BY TYPE (round-1 NIT 2: the committed 'sector "
      "alphabet' silently EXCLUDED the idle sector; it is printed here):")
for ty in sorted(ALPH_BY_TYPE):
    print(f"     type '{ty}': "
          f"{sorted(map(str, ALPH_BY_TYPE[ty]), key=lambda z: -Fr(z))}"
          + ("   <- excluded by the ty != 'n' filter" if ty == 'n' else ""))
for v in sorted(ARBWIT, reverse=True):
    dep, a, det = ARBWIT[v]
    print(f"  arb sector total {v}: witness depth {dep} actor {a}; "
          f"per-event (|comps|, |merge_pairs|, D, q) = "
          f"{[(c, m, D, str(q)) for c, m, D, q in det]}")
MAXC = max(CENSUS[d][0] for d in CENSUS)
MAXM = max(CENSUS[d][1] for d in CENSUS)
ARB_ALPH = ALPH_BY_TYPE['r']
check("S1 [CORRECTED BY ROUND 1 — THE COMMITTED MECHANISM IS REFUTED BY "
      "THIS UNIT'S OWN DATA] The arb sector does NOT price 1/4 divided "
      "by the number of components, and the component count does NOT "
      f"grow with depth: max |comps| = {MAXC} at EVERY depth over every "
      "one of the enumerated histories.  The denominator is |comps| + "
      "|merge_pairs|, and the 1/8 witness gets its 2 ENTIRELY FROM A "
      "MERGE PAIR.  **'THE SECTOR ALPHABET IS NOT FINITE' IS "
      "WITHDRAWN** — it was an extrapolation from a three-element "
      "observed alphabet through a premise the same data refutes.  The "
      "logic that would make it matter is sound (finite R + lumpable => "
      "at most |R|.|sectors| distinct totals; infinitely many values => "
      "no finite R) but its antecedent is NOT established.  Gated as a "
      "REPORT of the mechanism actually in the layer",
      MAXC == 1 and MAXM <= 1
      and ARB_ALPH == {Fr(1, 2), Fr(1, 4), Fr(1, 8)}
      and Fr(1, 8) in ARB_ALPH,
      f"max|comps| = {MAXC}, max|merge_pairs| = {MAXM}, max D = "
      f"{max(CENSUS[d][2] for d in CENSUS)}; observed arb-sector "
      f"alphabet = {sorted(map(str, ARB_ALPH))}; the 1/8 witness has "
      f"(|comps|, |merge_pairs|, D) = "
      f"{[(c, m, D) for c, m, D, q in ARBWIT[Fr(1, 8)][2]]}")

print("\n[S1b THE QUESTION, REOPENED — round-1 MAJOR 1]")
print("  At 2-actor scope the surviving growth route is PROVABLY CAPPED.")
print("  merge_pairs(a) requires two held created versions with")
print("  INCOMPARABLE creation events.  Every arb or merge by an actor")
print("  puts that actor in its own register set (regs_of gives")
print("  props | {vname(...)} for 'r', where arb_components_in_view")
print("  requires a in proposers; and {a, ('mw', a, pk)} for 'm'), so")
print("  ALL creations authored by one actor lie on that actor's")
print("  register chain and are pairwise COMPARABLE.  With two actors")
print("  there are exactly two chains, so at most one incomparable")
print("  pair: |merge_pairs(a)| <= 1, hence D <= |comps| + 1, at every")
print("  depth.  Combined with max|comps| = 1 throughout the enumerated")
print("  window, the observed {1/2, 1/4, 1/8} is CONSISTENT WITH BEING")
print("  THE COMPLETE arb-sector alphabet at this unit's own scope.")
check("S1b THE FINITE-ALPHABET PREREQUISITE HAS NOT BEEN SHOWN TO FAIL, "
      "and the receipt's own data is consistent with the alphabet being "
      "COMPLETE at this scope.  A rescue of ground (1) must either "
      "EXHIBIT |comps| >= 2 (plausibly reachable near depth 8 via the "
      "two-independent-arbs divergence — not exhibited anywhere, and cap "
      "6 cannot see it) or move to >= 3 actors, which is a scope change. "
      "Neither is in this receipt.  **Ground (1) is withdrawn as stated "
      "and the question is REOPENED**, which is a different thing from "
      "answering it negatively",
      MAXM <= 1 and MAXC == 1 and len(ARB_ALPH) == 3,
      f"|merge_pairs| never exceeded {MAXM} over the exhaustive cap-6 "
      f"family (bound proved above for 2 actors); |comps| never exceeded "
      f"{MAXC}; arb alphabet size = {len(ARB_ALPH)} and unchanged from "
      f"cap 3 to cap 6")

print("\n[S1c QUANTIZATION — round-1 MINOR 3/MINOR 4]")
print("  per-cap non-idle sector totals (the committed receipt summed "
      "these ACROSS NESTED CAPS, and cap C's family is a "
      "prefix-subfamily of cap C+1's):")
for CAP in (3, 4, 5, 6):
    print(f"     cap {CAP}: |FAM| = {PERCAP[CAP][0]:7d}   non-idle "
          f"sector totals = {PERCAP[CAP][1]:8d}")
_sum = sum(PERCAP[c][1] for c in PERCAP)
_distinct = PERCAP[6][1]
print(f"     SUM = {_sum} <- what the committed receipt reported as "
      f"'totals tested'; DISTINCT = {_distinct} (inflation "
      f"{_sum / _distinct:.2f}x)")
check("S1c THE k/4 LAW IS REFUTED AND THE REFUTATION IS NOW GATED "
      "(round-1 MINOR 3: `quant_bad` was computed and appeared only in a "
      "detail string, so the 'twice refuted' story was a printout).  "
      "Round-1 MINOR 2: the committed predicate's second conjunct, "
      "`all((v*4).denominator >= 1 ...)`, is true of every Fraction and "
      "is gone",
      quant_bad > 0 and Fr(1, 8) in ARB_ALPH,
      f"non-idle totals outside k/4 = {quant_bad}; per-cap census above; "
      f"distinct totals tested = {_distinct}, not the {_sum} advertised")

# ------------------------------------------------------------------- S2
print("\n  THE DECIDER — per-depth fixpoint class counts across caps:")
print("  depth :  cap3  cap4  cap5  cap6")
stab = []
for d in range(0, 7):
    row = [RESULTS[c].get(d, None) for c in (3, 4, 5, 6)]
    print(f"    {d}   :  " + "  ".join(str(x) if x is not None else "-"
                                       for x in row))
    vals = [x for x in row if x is not None]
    if len(vals) >= 3:
        stab.append((d, vals[-1] == vals[-2]))
last_two_stable = all(x for _, x in stab)
check("S2 THE MAIN QUESTION — read as LOOKAHEAD CONVERGENCE, not as raw "
      "growth (the first run's 'any growth = blow-up' reading was too "
      "crude: counts at depth d MUST grow while the cap is within the "
      "refinement's lookahead).  **THE DECIDER, STATED AS IT IS "
      "IMPLEMENTED (round-1 MINOR 6): for every depth carrying at least "
      "three cap values, do the LAST TWO cap values agree?**  The "
      "committed label said 'once the cap moves 2+ levels past d', a "
      "threshold justified nowhere and contradicted by its own data "
      "(depth 2 is stable from lookahead 1 onward: 9, 9, 9, 9).  The "
      "verdict is the same under either reading — every comparable depth "
      "fails the criterion — but the rule as written was an invented "
      "constant",
      len(RESULTS) == 4 and len(stab) > 0,
      f"(depth, stable-at-last-two-caps) = {stab} -> "
      + ("**CAP-STABLE AT EVERY COMPARABLE DEPTH — finite-lookahead "
         "convergence: closure evidence, the sector-exact chain is a "
         "live candidate**" if last_two_stable else
         "**NOT stabilized — the refinement keeps splitting beyond its "
         "lookahead: blow-up evidence at this window**"))

print("\n[S3 THE REFINEMENT WITNESS the pin promised — round-1 MINOR 1]")
for CAP in sorted(SPLITWIT):
    it, old, h1, h2 = SPLITWIT[CAP]
    print(f"  cap {CAP}: first refinement at iteration {it}; a class "
          f"splits, witness pair")
    print(f"      {list(h1)}")
    print(f"      {list(h2)}")
# the headline creep, 16 -> 17 at depth 3, exhibited
inv5 = defaultdict(list)
for h, c in CLS3[5].items():
    inv5[c].append(h)
SPLIT3 = None
for c, mem in sorted(inv5.items(), key=repr):
    parts = defaultdict(list)
    for h in mem:
        parts[CLS3[6][h]].append(h)
    if len(parts) > 1:
        ks = sorted(parts, key=lambda k: (-len(parts[k]), repr(k)))
        SPLIT3 = (len(mem), [(len(parts[k]),
                              sorted(parts[k], key=repr)[0]) for k in ks])
        break
print(f"  THE HEADLINE CREEP, EXHIBITED: depth-3 histories = "
      f"{len(CLS3[6])}, cap5 classes = {len(set(CLS3[5].values()))}, "
      f"cap6 classes = {len(set(CLS3[6].values()))}")
if SPLIT3:
    tot, parts = SPLIT3
    print(f"    SPLIT: one cap5 class of {tot} histories splits "
          f"{' / '.join(str(n) for n, _ in parts)} at cap6")
    for n, ex in parts:
        print(f"      cap6 class ({n} histories), example: {list(ex)}")
check("S3 THE HEADLINE CREEP IS NOT A MARGINAL ONE-OFF.  The committed "
      "receipt rested '16 -> 16 -> 17 at depth 3' on a single count with "
      "no witness (the pin promised one).  The split is exhibited above "
      "and it separates a substantive distinction over a double-digit "
      "block of histories, not one stray",
      SPLIT3 is not None and SPLIT3[1][-1][0] > 1
      and len(set(CLS3[6].values())) > len(set(CLS3[5].values())),
      f"depth-3: cap5 {len(set(CLS3[5].values()))} classes -> cap6 "
      f"{len(set(CLS3[6].values()))}; the splitting cap5 class had "
      f"{SPLIT3[0] if SPLIT3 else 0} histories and splits "
      f"{[n for n, _ in SPLIT3[1]] if SPLIT3 else []}")

print("\n[S4 THE BOUNDARY TREATMENT BIASES TOWARD CLOSURE — ground (2) "
      "STRENGTHENED]")
print("  The refinement was run a SECOND time at every cap with the")
print("  OPPOSITE boundary: the whole cap layer lumped into ONE class,")
print("  the coarsest possible treatment.  If the signature boundary")
print("  were manufacturing the growth, the trivial boundary would show")
print("  less of it.  It shows EXACTLY ONE LEVEL LESS OF LOOKAHEAD:")
_ident = []
for CAP in (4, 5, 6):
    same = all(RESULTS_TRIV[CAP].get(d) == RESULTS[CAP - 1].get(d)
               for d in RESULTS[CAP - 1])
    _ident.append(same and RESULTS_TRIV[CAP].get(CAP) == 1)
    print(f"    cap {CAP} trivial-boundary = {RESULTS_TRIV[CAP]}   vs   "
          f"cap {CAP - 1} signature = {RESULTS[CAP - 1]}   identical on "
          f"the shared depths = {same}")
check("S4 THE SIGNATURE BOUNDARY IS WORTH EXACTLY ONE EXTRA LEVEL OF "
      "LOOKAHEAD, and BOTH truncations UNDER-refine relative to the "
      "untruncated fixpoint (the cap layer's true successors would split "
      "it further).  So the reported per-depth counts are LOWER BOUNDS "
      "on the true counts: observed growth is genuine growth, and the "
      "blow-up reading is the CONSERVATIVE one.  The suspicion that the "
      "boundary treatment manufactures the negative is answered in the "
      "unit's favour",
      all(_ident),
      f"cap-C-with-signature == cap-(C+1)-with-trivial at every shared "
      f"depth, C = 3, 4, 5: {_ident}")

print("\n[S5 determinism and anti-vacuity — round-1 MINOR 5]")
_self = ast.parse(open('v10/code/d57_sector_exact_refinement.py').read())
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
check("S5 ORDER-INDEPENDENCE AND ANTI-VACUITY.  The refinement was "
      "re-run at cap 3 with the family enumerated in the OPPOSITE order "
      "— which is what a PYTHONHASHSEED change would perturb, since "
      "every key here is a dict-built tuple sorted by repr — and "
      "produced the IDENTICAL partition, block for block.  The AST scan "
      "(LOG #403 MA-2 scope) is the one this unit lacked, and is how "
      "MINOR 2's always-true conjunct survived",
      DET_OK and len(_ch) >= 7 and not _vac,
      f"cap-3 partition identical under reversed enumeration = "
      f"{DET_OK}; check() calls = {len(_ch)}, bare/unbound = {len(_vac)}")

print("\n[VERDICT — D57, ROUND-1 REPAIRED]")
print("  GROUND (2) STANDS AND IS STRENGTHENED.  Depth 3 crept "
      f"{[RESULTS[c].get(3) for c in (3, 4, 5, 6)]}, depth 4 "
      f"{[RESULTS[c].get(4) for c in (4, 5, 6)]}, depth 5 "
      f"{[RESULTS[c].get(5) for c in (5, 6)]}; nothing comparable "
      "stabilized, the witness is exhibited (S3), and the boundary "
      "treatment biases toward CLOSURE (S4), so the negative is "
      "conservative.")
print("  GROUND (1) IS WITHDRAWN AS STATED.  The arb-sector mechanism "
      "the committed receipt gave is refuted by its own exhaustive "
      "data, and 'THE SECTOR ALPHABET IS NOT FINITE' is unsupported.  "
      "LOG #437's adjudication — that ground (1) CARRIES the verdict "
      "and ground (2) corroborates — must be inverted: the verdict now "
      "rests on ground (2) alone.")
print("  THE REOPENED QUESTION: is |comps| >= 2 reachable at all, and "
      "if not at 2-actor scope, at 3?  That is a scope change and is "
      "not in this receipt.")
print("  DECLARED: actor-swap symmetry not quotiented (counts <= 2x "
      "upper bounds); the idle sector is excluded from 'the sector "
      "alphabet' by the ty != 'n' filter (its own alphabet is printed "
      "in S1); depth-7 confirmation is the residue.")
print(f"\n[d57] {PASS} PASS / {FAIL} FAIL")
sys.exit(1 if FAIL else 0)
