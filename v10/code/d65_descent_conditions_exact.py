#!/usr/bin/env python3
"""
d65_descent_conditions_exact.py — v10 D65: THE DESCENT CONDITIONS.
Pin: note-d65-descent-conditions-pin.md (STRICT, frozen).  Parents:
paper 29 ("Where the action cocycle lives" — Theorem 1's refined
cylinder cocycle and its F1 falsifier, Theorem 2's finite boundary
sufficiency and its F2 falsifier, §4.3's five durable-record
hypotheses), D59 (the two click-law objects meet at ONE MISSING MAP;
six supplied-not-derived items), and the CLOSED generated law: (H1)
[THEOREM] menu = G(sigma) (D61) + (H2) [THEOREM] sigma(h+e) =
TABLE(sigma(h), renamed e) (D62) => d44a's closure theorem is
UNCONDITIONAL at two-actor delivery-free d42a scope (36 sigma states,
176 transition keys).

WHAT THIS RECEIPT IS.  It gates the GENERATED law, one by one,
against the conditions paper 29 states that ANY record process must
satisfy for the action line's conditional-measure reading to descend
to it.  It measures the generated side of the missing map against the
action side's stated requirements.  It does NOT identify the two
measures, does NOT construct the functional level, does NOT touch
transport.  Every verdict is scoped to the exhaustive depth-6 family
and to two-actor delivery-free d42a.

DC1 is the only gate that can genuinely surprise, and it is
PRE-REGISTERED BOTH WAYS (pin §2).  Exit protocol (pin §3): exit 0
for substantive negatives — a DC1 failure IS the deliverable and its
full structure is printed — exit 1 ONLY on anchor breakage.

ROUND-1 REPAIRS (reviews/d65-round1-hostile-review.md, 1 BLOCKER /
5 MAJOR / 8 MINOR / 3 NIT — every number in that review reproduces
here).  What changed:
  * BLOCKER 1: the REPAIR SPACE is now computed and gated (block
    DC1-R).  The corollary proves an IMPLICATION; the first delivery
    read it as an equivalence.  Exact rational linear algebra at the
    depth-4 and depth-5 truncations gives the real hierarchy —
    repair cone 573 ⊃ repairs that descend 205 ⊃ (depth, sigma)
    family 28 ⊃ D49's Zhat (one ray) — plus two witnesses showing
    that "annihilates the defect" and "descends to the record" imply
    each other in NEITHER direction.  What collapses 573 to 1 is
    D50's FORM choice, not descent.
  * MAJOR 1: the LOAD-BEARING test is the REFINED sub-census DC1(f);
    the wider sigma-commuting census DC1(a) tests a hypothesis paper
    29 §3.1 explicitly exempts, and 56,376 of its 88,632 failures lie
    outside Theorem 1's hypothesis entirely.
  * MAJOR 2: D59's boundary-state ledger item STANDS (it is the
    action line's slot); what the generated line has is its own
    derived boundary statistic.  moved == 0.
  * MAJOR 3: the three FAILs are TWO statements, not one.
  * MAJOR 4: every entailed / tautological / constant gate is
    relabelled as a corollary or a reporting line (the d62-delta
    idiom).
  * MAJOR 5: the class-level census (720 = 616 + 104) is printed
    beside the pair census; it is the census's real information
    content and it nearly discharges residue 4.
  * MINORs/NITs: N3/N4 are anchors; CG3a is re-gated; the raw weight
    is order-independent but is NOT a measure (cut masses printed);
    Zhat's descent is gated; DC1-C's domain and orientation stated,
    with a second d42b3 anchor; the VERDICT prose is predicate-
    guarded.

Run:  python3 v10/code/d65_descent_conditions_exact.py [FAMDEPTH]
      (default 6.  The depth is PRINTED; there is no silent cap.)
"""
import sys
import ast
import time
from collections import defaultdict
from fractions import Fraction as Fr
from itertools import permutations
sys.setrecursionlimit(200000)

PASS = FAIL = ANCHOR_FAIL = 0


def check(label, ok, detail="", anchor=False):
    global PASS, FAIL, ANCHOR_FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    ANCHOR_FAIL += int(anchor and not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


def spec(d):
    """A census dict printed deterministically, sorted by key."""
    return {k: d[k] for k in sorted(d, key=repr)}


T0 = time.time()
print("[D65 — THE DESCENT CONDITIONS: the generated law measured")
print(" against paper 29's requirements for a record measure]")
print("  banner: EXACT Fractions end-to-end; the admission layer and")
print("  the sigma machinery are TEXT-SLICED from the committed")
print("  receipts (the d61/d62 idiom), never re-implemented; TWO-ACTOR")
print("  DELIVERY-FREE d42a ONLY; nothing here transfers to the")
print("  identified (action-line) click law — the map is still the map.")
print("  round: ROUND-1 REVIEWED AND REPAIRED (1 BLOCKER / 5 MAJOR /")
print("  8 MINOR / 3 NIT).  The BLOCKER's computation — the REPAIR")
print("  SPACE — is now a gate (block DC1-R); the load-bearing DC1")
print("  test is the REFINED sub-census DC1(f); entailed gates are")
print("  labelled as corollaries; D59's ledger loses its one move.")

# ==================================================================
# N0 — the committed layers, by TEXT SLICE.  Idiom copied verbatim
# from v10/code/d62_h2_update_table_exact.py (which copied d61).
# ==================================================================
_s = open('v10/code/d42b3_placement_exact.py').read()
_PREFIX = _s[:_s.index('print("[d42b3')]
ns = {}
exec(_PREFIX, ns)
cf, ep, V0, vname = (ns['candidates_for'], ns['event_poset'],
                     ns['V0'], ns['vname'])
adm = ns['admissible']
View, triples, canonH = ns['View'], ns['triples'], ns['canon']
AB = ('A', 'B')
_D44A = 'v10/code/d44a_closure_theorem_exact.py'
_ds = open(_D44A).read()
_blk1 = _ds[_ds.index("SG_VIOL = {'alive'"):_ds.index("\nSIG = {tuple(h)")]
_blk2 = _ds[_ds.index("def _rename_event(e, m2):"):
            _ds.index("\ngroups = defaultdict(list)")]
_blk3 = _ds[_ds.index("def canon_pair(hk, e):"):_ds.index("\nTRANS = {}")]
ns['AB'] = AB
ns['permutations'] = permutations
ns['defaultdict'] = defaultdict


def cands_of(hk):
    return cf(list(hk), AB)


ns['cands_of'] = cands_of
for _b, _nm in ((_blk1, 'sigma'), (_blk2, 'menu'), (_blk3, 'pair')):
    exec(compile(_b, 'd44a_' + _nm + '_port', 'exec'), ns)
sigma_raw, canon_sigma, ser = ns['sigma_raw'], ns['canon_sigma'], ns['ser']
canon_pair, SG_VIOL = ns['canon_pair'], ns['SG_VIOL']
canon_menu, own_alive = ns['canon_menu'], ns['own_alive']
_rename_event, _menu_extras = ns['_rename_event'], ns['_menu_extras']
SIGMEMO, RAWMEMO = ns['SIGMEMO'], ns['RAWMEMO']

check("N0(a) SINGLE SOURCES: d42b3's admission layer (candidates_for / "
      "admissible / event_poset / View / triples / canon / vname / V0) "
      "and d44a's sigma_raw / ser / canon_sigma / own_alive / "
      "_rename_event / _menu_extras / canon_menu / canon_pair "
      "extracted VERBATIM by text slice (the d61/d62 idiom); the "
      "slices carry the expected DEFINITIONS, not merely callables",
      callable(canon_sigma) and callable(canon_pair)
      and callable(canon_menu) and callable(ser)
      and "def sigma_raw" in _blk1 and "def ser(" in _blk1
      and "def canon_sigma" in _blk1 and "def own_alive" in _blk1
      and "def _rename_event" in _blk2 and "def _menu_extras" in _blk2
      and "def canon_menu" in _blk2 and "def canon_pair" in _blk3
      and "def candidates_for" in _PREFIX and "def admissible" in _PREFIX
      and "def canon(acts)" in _PREFIX,
      "d42b3 prefix + 3 d44a slices", anchor=True)

_stray = [(nm, b.count("sys.exit"), b.count("\ncheck("), b.count("\nprint("))
          for nm, b in (('blk1', _blk1), ('blk2', _blk2), ('blk3', _blk3))]
check("N0(b) SLICE HYGIENE (the d50 lesson, as gated in d62): the "
      "three d44a slices are PURE DEFINITIONS — zero sys.exit, zero "
      "top-level check(), zero top-level print() survive extraction, "
      "so nothing of d44a's own gate protocol can execute here; the "
      "d42b3 prefix is cut before its first print",
      all(x == 0 for nm, a, c, p in _stray for x in (a, c, p))
      and 'sys.exit' not in _PREFIX,
      f"stray (exit, check, print) per slice = "
      f"{[(nm, a, c, p) for nm, a, c, p in _stray]}", anchor=True)

# ------------------------------------------------------------------
# N0(c) — THE CODE-FACTS THIS UNIT READS.  DC1 and DC3(4) are about
# the WEIGHTS; DC2 is about the MENU; so the source lines that define
# the weight of every event class, the menu's construction, and d44a's
# committed per-class mass anchors are quoted verbatim.
# ------------------------------------------------------------------
_F = {
    "the IDLE weight — the quarter budget, both refusals":
        "        return True, 1 - (F(1, 4) if has_p else 0) - "
        "(F(1, 4) if has_r else 0)",
    "the PROPOSE weight — a quarter split over the actor's own-view "
    "propose options":
        "        return True, F(1, 4) / len(opts)",
    "the ARB weight — a quarter split over the actor's own-view "
    "components, times the K1 kernel on the winner":
        "    return True, F(1, 4) / len(comps) * PK1(ckey, et)[wkey]",
    "an inadmissible propose returns NO weight (the support is the "
    "admissible set, exactly)":
        "        if (b, x) not in opts: return False, None",
    "an arb whose ckey matches no own-view component is refused":
        "    if not match: return False, None",
    "an arb whose winner is not a maximal independent set is refused":
        "    if wkey not in mis_of(ckey, et): return False, None",
    "candidates_for's base set: V0 plus every minted version":
        "    bases = sorted({V0} | {vname(next(iter(op[2]))[1], op[3], "
        "op[1])",
    "candidates_for enumerates arb ckeys by BASE GROUP of the "
    "full-view live proposals (so a ckey is single-based)":
        "        live_by_base.setdefault(op[2], []).append(i)",
    "candidates_for's arb ckeys run over EVERY nonempty subset of a "
    "base group, with every nonempty winner subset":
        "            for smask in range(1, 1 << n):",
    "admissible's ckey match is by COMPONENT triples (so a ckey that "
    "spans two bases can never match)":
        "    match = [c for c in comps if triples(view, c[1]) == ckey]",
    "candidates_for appends the idle unconditionally (the menu is "
    "never empty)":
        "        e = ('n', a)",
}
_missing = [k for k, v in _F.items() if v not in _s]
check("N0(c) CODE-FACTS (d42b3): every source line this unit's "
      f"conditions read is present VERBATIM ({len(_F)} lines: the "
      "three weight formulas that MAKE the kernel, the three "
      "refusals that make the support exact, candidates_for's base "
      "set and single-based ckey enumeration, and the unconditional "
      "idle)",
      not _missing, f"quoted lines = {len(_F)}, missing = {_missing}",
      anchor=True)

_F2 = {
    "d44a's COMMITTED per-class menu masses (SB2's row sums) — the "
    "provenance of the two mass values this unit's defect analysis "
    "uses; no mass constant is invented here":
        "      == [Fr(2), Fr(2), Fr(2), Fr(5, 2), Fr(2), Fr(2)],",
    "canon_sigma is the MINIMUM serialisation over base bijections":
        "        if best is None or s < best: best = s",
    "canon_menu renames the menu under the SAME sigma-minimising "
    "bijection (the object (H1) is a statement about)":
        "        if ser(hold, live, comps, refs, sup, m) != sbest: continue",
}
_missing2 = [k for k, v in _F2.items() if v not in _ds]
check("N0(d) CODE-FACTS (d44a): the committed mass anchors and the "
      "two canonicalisation lines this unit's keys are built from",
      not _missing2, f"quoted lines = {len(_F2)}, missing = {_missing2}",
      anchor=True)

# the two mass values are READ OFF d44a's committed row-sum line, not
# typed in as bare constants (pin §3: no invented thresholds).
_rowsum_line = "      == [Fr(2), Fr(2), Fr(2), Fr(5, 2), Fr(2), Fr(2)],"
MASSES_COMMITTED = sorted({Fr(2), Fr(5, 2)}) if _rowsum_line in _ds else []
check("N0(e) THE MASS CONSTANTS HAVE PROVENANCE: the only two menu "
      "masses this receipt ever compares against are exactly the "
      "distinct values of d44a's committed SB2 row-sum anchor "
      "(2, 2, 2, 5/2, 2, 2) — read off the source line, never typed "
      "in as a free threshold",
      MASSES_COMMITTED == [Fr(2), Fr(5, 2)],
      f"committed mass set = {[str(m) for m in MASSES_COMMITTED]}",
      anchor=True)

# ==================================================================
# THE FAMILY — the committed enumerator, exhaustive to depth CAP
# ==================================================================
CAP = int(sys.argv[1]) if len(sys.argv) > 1 else 6
FAM = [()]
fr = [()]
CACHE = {}
while fr:
    h = fr.pop()
    CACHE[h] = cf(list(h), AB)
    if len(h) >= CAP:
        continue
    for e, q in CACHE[h]:
        FAM.append(h + (e,))
        fr.append(h + (e,))
by_depth = defaultdict(int)
BYD = defaultdict(list)
for h in FAM:
    by_depth[len(h)] += 1
    BYD[len(h)].append(h)
census = [by_depth[d] for d in range(CAP + 1)]
CENSUS_REF = [1, 6, 32, 176, 976, 5280, 27904]
print(f"\n  family depth CAP = {CAP}: {len(FAM)} histories, census by "
      f"depth = {census}")
check("N1 CENSUS ANCHOR: the committed layer's own history census "
      "[1, 6, 32, 176, 976, 5280, 27904] (d44a SG0 / D61 round-1's "
      "independent reproduction), total 34,375 at depth 6",
      census == CENSUS_REF[:CAP + 1] and (CAP != 6 or len(FAM) == 34375),
      f"census = {census}, histories = {len(FAM)}", anchor=True)

# sigma on the whole family; the state and key anchors
SIG = {h: canon_sigma(h) for h in FAM}
STATES = sorted(set(SIG.values()))
SIDX = {s: i for i, s in enumerate(STATES)}
_SHORTREP = {}      # sigma state -> its shortest witness history
for h in FAM:
    _s2 = SIG[h]
    if _s2 not in _SHORTREP or len(h) < len(_SHORTREP[_s2]):
        _SHORTREP[_s2] = h
# the RAW (unnormalised) path weight q(h) = prod of the menu weights
# along h — the object DC1(b) is about.  Used by DC1-C's anchors and
# by the DC1-R block.
QPATH = {(): Fr(1)}
for _d in range(CAP):
    for h in BYD[_d]:
        for e, q in CACHE[h]:
            QPATH[h + (e,)] = QPATH[h] * q
NKEY = defaultdict(set)
NTR = 0
CPAIR = {}          # (h, e) -> the committed canon_pair value, once
for h in FAM:
    for e, q in CACHE[h]:
        NTR += 1
        CPAIR[(h, e)] = canon_pair(h, e)
        s_next = SIG.get(h + (e,))
        if s_next is not None:
            NKEY[CPAIR[(h, e)]].add(s_next)
        else:
            NKEY[CPAIR[(h, e)]]          # key seen, successor beyond the cap
_kmulti = sum(1 for v in NKEY.values() if len(v) > 1)
print(f"  transitions out of the family = {NTR} (into depth {CAP + 1}); "
      f"distinct (sigma, renamed event) keys = {len(NKEY)}; keys "
      f"carrying two different successor states = {_kmulti}")
check("N2 THE CLOSED LAW's ANCHORS: exactly 36 sigma states and "
      "exactly 176 (sigma, renamed event) transition keys — d44a "
      "CG1/CG3a, re-derived here from the committed canon_sigma / "
      "canon_pair on the whole family (the state space this unit's "
      "conditions are evaluated on)",
      (len(STATES) == 36 and len(NKEY) == 176) if CAP == 6
      else (len(STATES) > 0 and len(NKEY) > 0),
      f"sigma states = {len(STATES)}, keys = {len(NKEY)}"
      + ("" if CAP == 6 else "  [NON-DEFAULT DEPTH: anchors apply at "
                             "CAP = 6 only]"), anchor=(CAP == 6))
check("N2(b) EACH TRANSITION KEY HAS A SINGLE SUCCESSOR STATE — d44a "
      "CG3a = (H2) [D62 THEOREM], re-gated here rather than assumed "
      "(round-1 MINOR 5: the key table is a dict and a silent "
      "overwrite would hide exactly this).  It is the property that "
      "makes DC1(d)'s key resolution meaningful: sigma(Ha) is a "
      "FUNCTION of (sigma(H), renamed a)",
      _kmulti == 0, f"keys = {len(NKEY)}, keys with two successors = "
      f"{_kmulti}", anchor=True)
check("N3 THE LAYER'S OWN SANITY COUNTERS (d44a's sigma port, carried "
      "through this receipt's sweep): alive-singleton, "
      "non-superseded-holdings, live-on-X and conflicting-pair-"
      "comparability violations all zero.  ANCHOR (round-1 MINOR 5): "
      "a break here would void the meaning of every sigma-indexed "
      "statement below, so it must exit 1, not 0",
      all(v == 0 for v in SG_VIOL.values()), f"SG_VIOL = {dict(SG_VIOL)}",
      anchor=True)


def MASS(hk):
    """the menu mass N(h) = sum of the exact menu weights."""
    return sum(q for e, q in CACHE[hk])


# per-state mass: constant on sigma classes (a corollary of (H1))
SMASS = {}
mass_split = 0
for h in FAM:
    s = SIG[h]
    m = MASS(h)
    if s in SMASS:
        if SMASS[s] != m:
            mass_split += 1
    else:
        SMASS[s] = m
mass_census = defaultdict(int)
for s, m in SMASS.items():
    mass_census[str(m)] += 1
check("N4 THE STATE MASS IS A FUNCTION OF sigma (corollary of (H1); "
      "re-gated directly, not assumed): every history in a sigma "
      "class has the same menu mass, and the value set is exactly "
      "d44a's committed {2, 5/2} — 34 states of mass 2, 2 states of "
      "mass 5/2 (the two states where an actor's blind conflict group "
      "is visible in the join view: the quarter law's excess).  "
      "ANCHOR (round-1 MINOR 5): DC1(c)'s entire meaning rests on M "
      "being a function of sigma, so a break here must exit 1",
      mass_split == 0
      and sorted(set(SMASS.values())) == MASSES_COMMITTED,
      f"mass-splitting classes = {mass_split}; per-state mass census "
      f"= {spec(mass_census)}", anchor=True)

print(f"  [t = {time.time() - T0:.1f}s]")

# ==================================================================
#  DC1 — THE COMMUTING-SQUARE IDENTITY  (paper 29 Theorem 1 / F1)
#  THE ONLY GATE THAT CAN SURPRISE.  Pre-registered both ways.
# ==================================================================
print("\n[DC1 — THE COMMUTING-SQUARE IDENTITY (paper 29 Theorem 1 / "
      "F1). SUBSTANTIVE; pre-registered both ways in the pin.]")
print("  *** WHICH CENSUS IS LOAD-BEARING (round-1 MAJOR 1).  The pin's")
print("  primary predicate DC1(a) calls a pair COMMUTING when both")
print("  orders are admissible and sigma(Hab) = sigma(Hba).  That is")
print("  equality of a COARSE terminal state, and paper 29 §3 defines")
print("  commutation at the REFINED record level ('[Hab] = [Hba]  ...")
print("  This is a statement about record identity, not merely equality")
print("  of a coarse terminal state'), while §3.1 says what the theorem")
print("  does NOT require: 'The theorem does not require equal weights")
print("  for two distinct serial histories that later push to one")
print("  quotient atom.'  So the sigma-commuting class is WIDER than")
print("  Theorem 1's hypothesis and its failures include pairs the")
print("  theorem exempts.  DC1(f) — the refined-record sub-census — is")
print("  therefore THE LOAD-BEARING TEST, and DC1(a) is reported as the")
print("  pin's (coarser) predicate with its excess named.  The pin is")
print("  frozen and its predicate is gated as written; the WEIGHT of")
print("  the result sits on DC1(f). ***")
print("  P(e|H) = menu weight / menu mass, exact Fractions.  For every")
print("  history H of the exhaustive family and every UNORDERED pair")
print("  {a, b} of distinct menu events at H (each unordered pair IS")
print("  the two ordered pairs (a,b) and (b,a): the tested identity is")
print("  symmetric under the swap), we census:")
print("    - both-orders admissibility (b at Ha AND a at Hb);")
print("    - one-order-refused pairs (the admissibility ASYMMETRY);")
print("    - NEITHER-order-admissible pairs (MUTUAL EXCLUSION);")
print("    - both-orders-admissible but sigma(Hab) != sigma(Hba)")
print("      (non-commuting by the pin's definition; excluded by name);")
print("    - for COMMUTING pairs (the pin's definition: both orders")
print("      admissible AND sigma(Hab) = sigma(Hba), which by (H1)+(H2)")
print("      means the two continuations carry THE SAME ENTIRE FUTURE")
print("      LAW — the generated analogue of [Hab] = [Hba]):")
print("          P(a|H) P(b|Ha)  =?  P(b|H) P(a|Hb)")
print("      recorded FOR BOTH ORDERED DIRECTIONS of the pair.  The")
print("      identity is symmetric under the swap, but the RATIO")
print("      DEFECT d is not (it inverts), so every defect census")
print("      below is over ORDERED pairs: a pair contributing d also")
print("      contributes 1/d.  Nothing then depends on which element")
print("      of the pair the enumeration happens to call 'a'.")
print("    - and, as a STRICTLY STRONGER hypothesis, the sub-census on")
print("      pairs with REFINED RECORD IDENTITY canon(Hab) = canon(Hba)")
print("      (d42b3's committed canonical-DAG functor) — this is paper")
print("      29's literal '[Hab] = [Hba]'.")
print("  EXHAUSTIVE over ALL parents of the family (no sampling: the")
print("  deepest level is included in full, see the per-level counts).")

n_unord = 0
n_pairs = n_both = n_onesided = n_neither = n_sigdiff = n_comm = 0
n_defect = 0
n_refined = n_refined_defect = 0
n_notrefined = n_notrefined_defect = 0
excl_spec = defaultdict(int)
excl_examples = []
defect_spec = defaultdict(int)
raw_spec = defaultdict(int)
massratio_spec = defaultdict(int)
refined_spec = defaultdict(int)
cls_spec = defaultdict(int)
sig_spec = defaultdict(int)
samemass_spec = defaultdict(int)
diffmass_spec = defaultdict(int)
per_level = defaultdict(lambda: [0, 0, 0])   # depth -> [pairs, comm, defect]
coboundary_bad = 0
onesided_examples = []
sigdiff_examples = []
defect_examples = []
KEYA = defaultdict(set)     # (sigma, {per-event renamed a, b}) -> defects
KEYB = defaultdict(set)     # (sigma, joint renamed pair)       -> defects


def canon_pair2(hk, e1, e2):
    """The JOINT canonical key of (sigma(h), {e1, e2}) — canon_pair's
    own idiom (d44a, text-sliced above) applied to TWO events at once,
    so that the two renamed events are read under ONE sigma-minimising
    bijection.  Gated against canon_pair below (N5)."""
    hold, live, comps, refs, sup = sigma_raw(hk)
    sbest = canon_sigma(hk)
    best = None
    for perm in permutations(range(len(refs))):
        m = {refs[i]: perm[i] for i in range(len(refs))}
        if ser(hold, live, comps, refs, sup, m) != sbest:
            continue
        extras = _menu_extras([(e1, None), (e2, None)], m)
        for eperm in permutations(range(len(extras))):
            m2 = dict(m)
            for i in range(len(extras)):
                m2[extras[i]] = 100 + eperm[i]
            c = (repr(_rename_event(e1, m2)), repr(_rename_event(e2, m2)))
            if best is None or c < best:
                best = c
    return (sbest, best)


_n5bad = 0
for h in FAM:
    if len(h) > 2:
        continue
    for e, q in CACHE[h]:
        sb, eb = canon_pair(h, e)
        s2, pr = canon_pair2(h, e, e)
        if not (s2 == sb and pr == (eb, eb)):
            _n5bad += 1
check("N5 THE JOINT KEY IS canon_pair's OWN IDIOM: canon_pair2(h, e, "
      "e) reproduces (canon_sigma(h), (ebest, ebest)) with ebest the "
      "committed canon_pair's renamed event, at every transition out "
      "of every history of DEPTH <= 2 (214 transitions) — so the pair "
      "key is the committed key's two-event extension, not a new "
      "normal form.  SCOPE, STATED (round-1 MINOR 8): this is a "
      "DIAGONAL check at depth <= 2 while DC1(d)'s key-B census runs "
      "family-wide, and on the diagonal there is only one event, so "
      "it cannot by itself certify that two DISTINCT events are "
      "renamed under one common bijection.  What carries DC1(d) is "
      "the AGREEMENT of the two independent key resolutions A and B "
      "(616 classes each, zero splits under either)",
      _n5bad == 0, f"transitions checked = "
      f"{sum(len(CACHE[h]) for h in FAM if len(h) <= 2)}, "
      f"disagreements = {_n5bad}")


def menu_at(hk, local):
    """the menu of hk as a dict, from the family cache when hk is in
    it, else computed by the committed enumerator (the deepest level's
    children lie one step beyond the family)."""
    if hk in CACHE:
        return CACHE[hk]
    if hk not in local:
        local[hk] = cf(list(hk), AB)
    return local[hk]


for h in FAM:
    mn = CACHE[h]
    N = MASS(h)
    qh = {e: q for e, q in mn}
    local = {}
    d = len(h)
    for i in range(len(mn)):
        for j in range(i + 1, len(mn)):
            a, b = mn[i][0], mn[j][0]
            n_unord += 1
            n_pairs += 2
            per_level[d][0] += 2
            Ha, Hb = h + (a,), h + (b,)
            ma = {e: q for e, q in menu_at(Ha, local)}
            mb = {e: q for e, q in menu_at(Hb, local)}
            ok_ab, ok_ba = b in ma, a in mb
            if not (ok_ab and ok_ba):
                if ok_ab or ok_ba:
                    n_onesided += 2
                    if len(onesided_examples) < 3:
                        onesided_examples.append((h, a, b, ok_ab, ok_ba))
                else:
                    n_neither += 2
                    excl_spec[tuple(sorted((a[0], b[0])))] += 1
                    if len(excl_examples) < 2 and len(h) <= 1:
                        excl_examples.append((h, a, b))
                continue
            n_both += 2
            Hab, Hba = Ha + (b,), Hb + (a,)
            s1, s2 = canon_sigma(Hab), canon_sigma(Hba)
            same_record = canonH(list(Hab)) == canonH(list(Hba))
            for k in (Hab, Hba):
                SIGMEMO.pop(k, None)
                RAWMEMO.pop(k, None)
            if s1 != s2:
                n_sigdiff += 2
                if len(sigdiff_examples) < 3:
                    sigdiff_examples.append((h, a, b))
                continue
            n_comm += 2
            per_level[d][1] += 2
            Na = sum(q for e, q in menu_at(Ha, local))
            Nb = sum(q for e, q in menu_at(Hb, local))
            rawL, rawR = qh[a] * ma[b], qh[b] * mb[a]
            L = (qh[a] / N) * (ma[b] / Na)
            R = (qh[b] / N) * (mb[a] / Nb)
            dv = L / R
            # BOTH ordered directions of the pair; d inverts under the
            # swap, so every census below is order-canonical.
            for (u, v, dd) in ((a, b, dv), (b, a, 1 / dv)):
                defect_spec[str(dd)] += 1
                cls_spec[((u[0], v[0]), str(dd))] += 1
                sig_spec[(SIDX[SIG[h]], str(dd))] += 1
                (samemass_spec if Na == Nb else diffmass_spec)[str(dd)] += 1
                KEYA[(SIG[h], (CPAIR[(h, u)][1], CPAIR[(h, v)][1]))].add(
                    str(dd))
                KEYB[canon_pair2(h, u, v)].add(str(dd))
            raw_spec[str(rawL / rawR)] += 2
            massratio_spec[str(Nb / Na)] += 1
            massratio_spec[str(Na / Nb)] += 1
            # the sharper structural claim: defect == M(sigma(Hb)) /
            # M(sigma(Ha)), M the per-state mass function of N4
            if dv != Nb / Na:
                coboundary_bad += 1
            if same_record:
                n_refined += 2
                refined_spec[str(dv)] += 1
                refined_spec[str(1 / dv)] += 1
                if dv != 1:
                    n_refined_defect += 2
            else:
                n_notrefined += 2
                if dv != 1:
                    n_notrefined_defect += 2
            if dv != 1:
                n_defect += 2
                per_level[d][2] += 2
                if len(defect_examples) < 2 and len(h) <= 1:
                    defect_examples.append(
                        (h, a, b, qh[a], ma[b], qh[b], mb[a], N, Na, Nb, dv))
    if d >= CAP:
        local.clear()

print(f"\n  PAIR CENSUS (exhaustive, every parent of the family).")
print(f"  ALL COUNTS ARE ORDERED PAIRS (a, b); the enumeration unit is")
print(f"  the unordered pair and each contributes its two directions.")
print(f"    unordered pairs {{a, b}} of distinct menu events = {n_unord}")
print(f"    ORDERED pairs (a, b) of distinct menu events   = {n_pairs}")
print(f"      NEITHER order admissible (MUTUAL EXCLUSION)   = {n_neither}")
print(f"      exactly ONE order admissible (ASYMMETRY)      = {n_onesided}")
print(f"      both orders admissible                        = {n_both}")
print(f"        of which sigma(Hab) != sigma(Hba) (NON-COMMUTING, "
      f"excluded by name) = {n_sigdiff}")
print(f"        of which SIGMA-COMMUTING (the pin's coarse")
print(f"          definition — the WIDER class, NOT Theorem 1's")
print(f"          hypothesis; see MAJOR 1 above)               = {n_comm}")
print(f"          of which the identity HOLDS                = "
      f"{n_comm - n_defect}")
print(f"          of which the identity FAILS                = "
      f"{n_defect}")
print(f"          of which REFINED-RECORD IDENTICAL (Theorem 1's")
print(f"            own hypothesis — THE LOAD-BEARING ROW)   = "
      f"{n_refined}")
print(f"              identity FAILS on                       = "
      f"{n_refined_defect}")
print(f"          of which sigma-commuting but NOT refined-")
print(f"            record identical (paper 29 §3.1 EXEMPTS")
print(f"            these: no descent content)                = "
      f"{n_notrefined}")
print(f"              identity FAILS on                       = "
      f"{n_notrefined_defect}"
      f"  ({n_notrefined_defect} of the {n_defect} DC1(a) failures lie")
print(f"              OUTSIDE Theorem 1's hypothesis entirely)")
print(f"    MUTUAL-EXCLUSION census by event tags: {spec(excl_spec)}")
for m in excl_examples:
    print(f"      [MUTUALLY EXCLUSIVE WITNESS] H = {m[0]}")
    print(f"          a = {m[1]}")
    print(f"          b = {m[2]}")
print(f"    per-level [ordered pairs, commuting, defects] by parent "
      f"depth:")
for dd in range(CAP + 1):
    print(f"      depth {dd}: {per_level[dd]}")
print(f"    REFINED-RECORD sub-census (canon(Hab) = canon(Hba), paper "
      f"29's literal [Hab] = [Hba]):")
print(f"      refined-identical ORDERED pairs = {n_refined}, of which "
      f"the identity FAILS = {n_refined_defect}")
print(f"      refined-identical defect spectrum = {spec(refined_spec)}")
if onesided_examples:
    print(f"    ASYMMETRY EXAMPLES: {onesided_examples}")
if sigdiff_examples:
    print(f"    NON-COMMUTING EXAMPLES: {sigdiff_examples}")

print(f"\n  THE EXACT RATIO DEFECT SPECTRUM  d = "
      f"P(a|H)P(b|Ha) / P(b|H)P(a|Hb):")
print(f"    {spec(defect_spec)}")
print(f"  the RAW (unnormalised) product ratio  q(a|H)q(b|Ha) / "
      f"q(b|H)q(a|Hb):")
print(f"    {spec(raw_spec)}")
print(f"  the INTERMEDIATE-MASS ratio  N(Hb) / N(Ha):")
print(f"    {spec(massratio_spec)}")
print(f"  defect by ORDERED pair class (event tag of a, then of b):")
for k in sorted(cls_spec, key=repr):
    print(f"    {k[0]}  d = {k[1]:>3}: {cls_spec[k]}")
print(f"  defect by sigma(H) (state index : {{d : count}}) — the set of "
      f"DEFECTING states is [ENTAILED by DC1(c) + the two-valued mass: "
      f"a parent state defects IFF its menu contains two events leading "
      f"to states of DIFFERENT mass, so this is a corollary, not an "
      f"independent localisation of the pathology (round-1 MINOR 6)]:")
_bysig = defaultdict(dict)
for (si, dv), c in sig_spec.items():
    _bysig[si][dv] = c
for si in sorted(_bysig):
    print(f"    sigma[{si:2d}] (mass {SMASS[STATES[si]]}): "
          f"{spec(_bysig[si])}")
print(f"  defect on SAME-MASS intermediate states  N(Ha) = N(Hb): "
      f"{spec(samemass_spec)}")
print(f"  defect on MASS-MIXED intermediate states N(Ha) != N(Hb): "
      f"{spec(diffmass_spec)}")
for m in defect_examples:
    print("  [DC1 DEFECT WITNESS]")
    for lab, z in zip(("H", "a", "b", "q(a|H)", "q(b|Ha)", "q(b|H)",
                       "q(a|Hb)", "N(H)", "N(Ha)", "N(Hb)",
                       "defect d"), m):
        print(f"      {lab:9s}: {z}")

DC1_HOLDS = (n_defect == 0)
DC1F_HOLDS = (n_refined_defect == 0)
check("DC1(a) THE SIGMA-COMMUTING SQUARE IDENTITY [THE PIN'S PRIMARY "
      "PREDICATE, gated as written — but the COARSE one: round-1 "
      "MAJOR 1].  Exhaustive over every sigma-commuting pair at every "
      "history of the family.  PRE-REGISTERED BOTH WAYS (pin §2): a "
      "FAIL here is the deliverable, not a bug.  WHAT IT IS AND IS "
      "NOT: sigma-equality is equality of a coarse terminal state, "
      "which paper 29 §3.1 explicitly exempts from Theorem 1; the "
      "failures outside the refined-record class carry NO descent "
      "content, and a genuine positive record-cylinder measure can "
      "fail this very test (gated below, DC1-R(f)).  The consequence "
      "sentence in the verdict is carried by DC1(f), not by this gate",
      DC1_HOLDS, f"sigma-commuting pairs = {n_comm}, identity failures "
      f"= {n_defect} ({'HOLDS' if DC1_HOLDS else 'FAILS'}); of those "
      f"failures {n_refined_defect} are refined-record identical and "
      f"{n_notrefined_defect} are NOT (outside Theorem 1's hypothesis)")
check("DC1(b) THE RAW (UNNORMALISED) COCYCLE: on every commuting pair "
      "the raw weight products agree exactly, q(a|H) q(b|Ha) = q(b|H) "
      "q(a|Hb) — so the generated law's UNNORMALISED history weight "
      "mu(h) = prod q IS order-independent on commuting pairs; the "
      "whole defect, if any, lives in the normalisation",
      set(raw_spec) == {'1'} and n_comm > 0,
      f"raw product ratio spectrum = {spec(raw_spec)}")
check("DC1(c) THE DEFECT IS EXACTLY THE INTERMEDIATE-MASS RATIO (the "
      "pin's pre-registered structural fallback, sharpest form): for "
      "EVERY commuting pair, d = M(sigma(Hb)) / M(sigma(Ha)) with M "
      "the per-state mass function gated in N4 — i.e. the defect is "
      "the COBOUNDARY of a function of sigma alone, a mass-ratio "
      "cocycle and nothing else",
      coboundary_bad == 0 and n_comm > 0,
      f"commuting pairs = {n_comm}, pairs where d != N(Hb)/N(Ha) = "
      f"{coboundary_bad}")
_ksplitA = sum(1 for v in KEYA.values() if len(v) > 1)
_ksplitB = sum(1 for v in KEYB.values() if len(v) > 1)
check("DC1(d) THE DEFECT IS A FUNCTION OF (sigma(H), class(a), "
      "class(b)) ALONE [COROLLARY OF DC1(c) + N2(b) — round-1 "
      "MAJOR 4(b): given d = M(sigma(Hb))/M(sigma(Ha)) and given that "
      "sigma(Ha) is a function of (sigma(H), renamed a) (N2(b) = "
      "CG3a), d is a function of the pair key BY CONSTRUCTION and "
      "cannot come out otherwise.  Printed because the CLASS COUNTS "
      "are the census's real information content (see DC1(i)), not "
      "because the gate is at risk].  Tested on TWO key resolutions, "
      "both ORDERED (the defect inverts under the swap, so an "
      "unordered key would be wrong): (A) the two events renamed "
      "SEPARATELY by the committed canon_pair, (B) the two events "
      "renamed JOINTLY by canon_pair2 (N5).  No key carries two "
      "different defect values under either resolution — and since a "
      "key fixed by an automorphism swapping a and b receives BOTH d "
      "and 1/d, this also forces d = 1 on every self-swapped class",
      _ksplitA == 0 and _ksplitB == 0,
      f"key-A classes = {len(KEYA)}, splitting = {_ksplitA}; key-B "
      f"classes = {len(KEYB)}, splitting = {_ksplitB}")
check("DC1(e) THE FAILURE VANISHES EXACTLY ON THE SAME-MASS SUBCLASS "
      "[COROLLARY OF DC1(c) — round-1 MAJOR 4(b): d = M/M is 1 iff "
      "the two masses are equal, so this restates DC1(c) on a "
      "partition of the same population; printed for the counts] "
      "(the natural subclass named in the pin's lean): every "
      "commuting pair whose two intermediate states carry EQUAL menu "
      "mass satisfies the identity, and every failure has "
      "MASS-MIXED intermediates — the risk sits precisely where the "
      "pin said it would, and nowhere else",
      set(samemass_spec) <= {'1'} and '1' not in diffmass_spec
      and sum(samemass_spec.values()) > 0,
      f"same-mass pairs = {sum(samemass_spec.values())} "
      f"(spectrum {spec(samemass_spec)}); mass-mixed pairs = "
      f"{sum(diffmass_spec.values())} (spectrum {spec(diffmass_spec)})")
check("DC1(f) THE REFINED-RECORD SUB-CENSUS — *** THE LOAD-BEARING "
      "TEST (round-1 MAJOR 1) ***.  Paper 29's literal hypothesis is "
      "[Hab] = [Hba] at the REFINED record level, which on the "
      "generated side is equality of d42b3's committed canonical DAG "
      "(the identification is an interpretive step and is declared as "
      "such — residue 3).  This is the strictly stronger hypothesis, "
      "the only one of the two from which Theorem 1's contrapositive "
      "follows, and it is a DIFFERENT predicate over a DIFFERENT "
      "population from DC1(a) — not a duplicate of it (round-1 "
      "MAJOR 3)",
      DC1F_HOLDS and n_refined > 0,
      f"refined-identical pairs = {n_refined} of {n_comm} "
      f"sigma-commuting, identity failures = {n_refined_defect} "
      f"({'HOLDS' if DC1F_HOLDS else 'FAILS'}); failure rate "
      f"{n_refined_defect}/{n_refined} vs DC1(a)'s {n_defect}/{n_comm}"
      f"; spectrum = {spec(refined_spec)}")
check("DC1(g) THE CENSUS BOOKKEEPING CLOSES [BOOKKEEPING LINE, NOT A "
      "GATE — round-1 MAJOR 4(b): all four conjuncts are "
      "counter-construction tautologies (n_pairs and n_unord are "
      "incremented in one place by 2 and 1; the exclusion categories "
      "are mutually exclusive branches of one if/else; n_defect only "
      "ever increments inside the commuting branch).  Printed so that "
      "the exclusion counts are visibly exhaustive rather than "
      "residual], so that the exclusion "
      "counts are exhaustive rather than residual: every ordered pair "
      "is accounted for exactly once as mutually-exclusive, "
      "asymmetric, non-commuting, identity-holding or "
      "identity-failing, and the ordered total is twice the unordered "
      "enumeration.  All four exclusion categories are named and "
      "counted; none is a leftover",
      n_pairs == 2 * n_unord
      and n_pairs == n_neither + n_onesided + n_both
      and n_both == n_sigdiff + n_comm
      and n_defect <= n_comm,
      f"ordered pairs = {n_pairs} = 2 x {n_unord} = neither "
      f"{n_neither} + asymmetric {n_onesided} + both-orders "
      f"{n_both}; both-orders = sigma-differs {n_sigdiff} + commuting "
      f"{n_comm}")
check("DC1(h) THE ADMISSIBILITY ASYMMETRY, THE MUTUAL-EXCLUSION AND "
      "THE NON-COMMUTING CENSUSES [REPORTING-ONLY, CANNOT FAIL — the "
      "predicate is the constant True; the pin asks for these numbers "
      "whichever way they land].  What the numbers say: "
      "admissibility on a menu pair is SYMMETRIC (zero asymmetric "
      "pairs — no admissible menu event ever survives its partner in "
      "one order and not the other), the menu is NOT all-concurrent "
      "(a nonzero block of pairs is mutually exclusive: the two "
      "events cannot follow each other in EITHER order), and "
      "wherever both orders do run they already agree on the "
      "successor state (zero non-commuting pairs)",
      True, f"asymmetric = {n_onesided}; mutually exclusive = "
      f"{n_neither}; both-orders-admissible-but-sigma-differs = "
      f"{n_sigdiff}")

# ------------------------------------------------------------------
# DC1(i) — THE CLASS-LEVEL CENSUS (round-1 MAJOR 5).  What the
# 794,570-pair sweep is EVIDENCE for: by (H1) and (H2) every quantity
# in the DC1 census is a function of (sigma(H), renamed a, renamed b),
# so the pair census collapses onto the PAIR CLASSES of the 36-state
# chain.  The class count is the census's information content; the
# ~1,080-fold multiplicity is replication, not independent
# confirmation.  Computed here from one representative history per
# state, independently of the family sweep, and compared to it.
# ------------------------------------------------------------------
cl_tot = cl_comm = cl_excl = cl_one = cl_sigdiff = 0
for s in STATES:
    hrep = _SHORTREP[s]
    mnr = CACHE[hrep]
    cl_tot += len(mnr) * (len(mnr) - 1)
    for i in range(len(mnr)):
        for j in range(i + 1, len(mnr)):
            a, b = mnr[i][0], mnr[j][0]
            Ha, Hb = hrep + (a,), hrep + (b,)
            ma_ = {e for e, q in menu_at(Ha, {})}
            mb_ = {e for e, q in menu_at(Hb, {})}
            ok1, ok2 = b in ma_, a in mb_
            if ok1 and ok2:
                if canon_sigma(Ha + (b,)) != canon_sigma(Hb + (a,)):
                    cl_sigdiff += 2
                else:
                    cl_comm += 2
            elif ok1 or ok2:
                cl_one += 2
            else:
                cl_excl += 2
print(f"\n  THE CLASS-LEVEL CENSUS (round-1 MAJOR 5 — the census's "
      f"actual information content):")
print(f"    sum over the {len(STATES)} sigma states of m(m-1)      = "
      f"{cl_tot}")
print(f"      ... both orders admissible (sigma-commuting) = {cl_comm}")
print(f"      ... neither order admissible (exclusive)     = {cl_excl}")
print(f"      ... exactly one order admissible             = {cl_one}")
print(f"      ... both admissible but sigma differs        = {cl_sigdiff}")
print(f"    ordered pair CLASSES seen in the family sweep  = {len(KEYA)}"
      f"  (key A) / {len(KEYB)} (key B)")
print(f"    so every class is realised inside the depth-{CAP} family, and")
print(f"    the {n_pairs} ordered pairs are ~{n_pairs // max(cl_tot, 1)} "
      f"instances each of {cl_tot} class-level facts.")
check("DC1(i) THE CENSUS IS 720 CLASS-LEVEL FACTS, NOT 794,570 "
      "INDEPENDENT ONES [SUBSTANTIVE — it can fail two ways: a class "
      "the family never realises, or a family pair class with no "
      "representative-level counterpart].  Built from ONE "
      "representative history per sigma state, independently of the "
      "family sweep: the class-level pair census (sum of m(m-1) over "
      "the 36 states) partitions into commuting and mutually "
      "exclusive with nothing left over, and its commuting count is "
      "exactly the number of ordered pair classes the exhaustive "
      "sweep found (with zero splitting classes, DC1(d)).  "
      "CONSEQUENCE, and it is the honest reading of the headline: the "
      "exhaustive census REPLICATES each class-level fact about a "
      "thousand times over; the evidential content is the class count, "
      "and the multiplicity is replication, not independent "
      "confirmation",
      cl_tot == cl_comm + cl_excl + cl_one + cl_sigdiff
      and cl_one == 0 and cl_sigdiff == 0
      and cl_comm == len(KEYA) == len(KEYB) and _ksplitA == 0,
      f"class-level ordered pairs = {cl_tot} = commuting {cl_comm} + "
      f"exclusive {cl_excl} + one-sided {cl_one} + sigma-differing "
      f"{cl_sigdiff}; family-wide pair classes = {len(KEYA)} (key A), "
      f"{len(KEYB)} (key B), splitting = {_ksplitA}/{_ksplitB}")
print(f"  [t = {time.time() - T0:.1f}s]")

# ------------------------------------------------------------------
# DC1-C — the completion corollary.  d42b3's D1(ii) gradient
# completion Z re-derived on the depth-4 slice (anchored to d42b3's
# OWN committed numbers), and the SAME identity re-tested under the
# completed kernel P_Z(e|h) = q(e|h) Z(h+e)/Z(h).  This is NOT a
# property of the generated law: Z is SUPPLIED data (D50 — the form
# remains a choice).  Labelled accordingly.
# ------------------------------------------------------------------
print("\n[DC1-C — the completion corollary, INSTANTIATED (REPORTING; Z "
      "is SUPPLIED data, D50: the form remains a choice).  Round-1 "
      "MAJOR 4(a): d42b3's gradient Z is NOT 'an independent "
      "completion of a different shape' — it is a SECOND MEMBER OF "
      "THE SAME (depth, sigma) FAMILY (verified below: 0 cells "
      "carrying two values), so its zero-failure result is an "
      "INSTANCE of the two-line corollary and cannot fail once "
      "DC1(b) holds.  It is kept because its two d42b3 anchors are "
      "worth re-deriving and because the corollary deserves a "
      "worked instance — not as independent evidence.]")
ZD = 4
Z = {}
if CAP < ZD:
    print(f"  [SKIPPED: d42b3's Z is defined on its depth-{ZD} slice "
          f"and CAP = {CAP} < {ZD}.  Re-run at the default depth.]")
for h in FAM:
    if CAP >= ZD and len(h) == ZD:
        Z[h] = Fr(1)
for L in range(ZD - 1, -1, -1):
    if CAP < ZD:
        break
    for h in FAM:
        if len(h) != L:
            continue
        Z[h] = sum(q * Z[h + (e,)] for e, q in CACHE[h])
zcls = defaultdict(set)
for h in FAM:
    if len(h) <= ZD and h in Z:
        zcls[canonH(list(h))].add(Z[h])
z_split = sum(1 for v in zcls.values() if len(v) > 1)
zn_comm = zn_def = zn_par = zn_refid = 0
for h in FAM:
    if len(h) > ZD - 2 or CAP < ZD:
        continue
    zn_par += 1
    mn = CACHE[h]
    qh = {e: q for e, q in mn}
    for i in range(len(mn)):
        for j in range(i + 1, len(mn)):
            a, b = mn[i][0], mn[j][0]
            Ha, Hb = h + (a,), h + (b,)
            ma = {e: q for e, q in CACHE[Ha]}
            mb = {e: q for e, q in CACHE[Hb]}
            if b not in ma or a not in mb:
                continue
            if canon_sigma(Ha + (b,)) != canon_sigma(Hb + (a,)):
                continue
            zn_comm += 1
            if canonH(list(Ha + (b,))) == canonH(list(Hb + (a,))):
                zn_refid += 1
            LZ = (qh[a] * Z[Ha] / Z[h]) * (ma[b] * Z[Ha + (b,)] / Z[Ha])
            RZ = (qh[b] * Z[Hb] / Z[h]) * (mb[a] * Z[Hb + (a,)] / Z[Hb])
            if LZ != RZ:
                zn_def += 1
# ---- the gradient Z's SHAPE (round-1 MAJOR 4(a)) and d42b3's second
# ---- committed anchor (round-1 NIT 2)
zsig_cells = defaultdict(set)
for h in Z:
    zsig_cells[(len(h), SIG[h])].add(Z[h])
zsig_split = sum(1 for v in zsig_cells.values() if len(v) > 1)
_cut4 = sum(QPATH[h] for h in BYD[ZD]) if CAP >= ZD else None
_interior = [h for h in FAM if len(h) <= ZD - 1]
_int_classes = defaultdict(list)
for h in _interior:
    _int_classes[canonH(list(h))].append(h)
_deformed = set()
for cn, mem in _int_classes.items():
    hh = mem[0]
    if len({Z[hh + (e,)] for e, q in CACHE[hh]}) > 1:
        _deformed.add(cn)
if CAP >= ZD:
    print(f"    Z's SHAPE: (depth, sigma) cells occupied = "
          f"{len(zsig_cells)}, cells carrying more than one Z value = "
          f"{zsig_split}  -> Z FACTORS THROUGH (depth, sigma), i.e. it "
          f"satisfies the corollary's own hypothesis")
    print(f"    Z's DOMAIN: parents of depth <= {ZD - 2} = {zn_par} of "
          f"{len(FAM)} histories; commuting pairs there = {zn_comm} "
          f"UNORDERED (= {2 * zn_comm} in this note's ordered unit), of "
          f"which {zn_refid} are refined-record identical and "
          f"{zn_comm - zn_refid} are not (round-1 MINOR 3)")
    print(f"    Z's ANCHORS: Z(empty) = {Z.get(())} — which is EXACTLY "
          f"the depth-{ZD} raw cut mass sum_{{|h|={ZD}}} q(h) = {_cut4}, "
          f"so it certifies that the recursion RAN (round-1 NIT 2); the "
          f"second, independent anchor is d42b3's own deformation "
          f"census: interior histories = {len(_interior)} (d42b3 anchor "
          f"215), interior cut classes = {len(_int_classes)} (anchor "
          f"114), classes with within-cut ratio deformation = "
          f"{len(_deformed)} (anchor 21), root deformed = "
          f"{canonH([]) in _deformed} (anchor True)")
check("DC1-C d42b3's GRADIENT COMPLETION, re-derived and anchored to "
      "its OWN committed numbers (D1(ii)): Z(empty) = 1037/64, Z > 0 "
      "throughout, Z constant on d42b3's canonical classes, and the "
      "deformation census 21 of 114 interior cut classes with the "
      "root included.  Under the completed kernel P_Z(e|h) = "
      "q Z(h+e)/Z(h) — which IS normalised per cut by the recursion — "
      "the commuting-square identity holds on every commuting pair "
      "with both continuations inside Z's domain.  [ENTAILED, NOT "
      "INDEPENDENT EVIDENCE — round-1 MAJOR 4(a): Z factors through "
      "(depth, sigma) (gated in the same line: 0 cells with two "
      "values), so once DC1(b) holds the zero-failure result is a "
      "THEOREM of the corollary and cannot fail.  What IS at risk "
      "here, and is the reason to keep the gate, is the pair of "
      "d42b3 anchors and the factoring claim.]  Its cost is d42b3's "
      "own; its domain is the 39 parents of depth <= 2",
      (Z.get(()) == Fr(1037, 64) and all(z > 0 for z in Z.values())
       and z_split == 0 and zn_def == 0 and zn_comm > 0
       and zsig_split == 0 and Z.get(()) == _cut4
       and len(_interior) == 215 and len(_int_classes) == 114
       and len(_deformed) == 21 and canonH([]) in _deformed)
      if CAP >= ZD else True,
      f"Z(empty) = {Z.get(())} (d42b3 anchor 1037/64 = the depth-4 raw "
      f"cut mass); Z-class splits = {z_split}; (depth,sigma) cells "
      f"with two values = {zsig_split}; deformation = "
      f"{len(_deformed)}/{len(_int_classes)} (anchors 21/114); "
      f"commuting pairs in Z's domain = {zn_comm} unordered = "
      f"{2 * zn_comm} ordered; identity failures under P_Z = {zn_def}")
print("\n  THE GENERAL COROLLARY [PROOF — two lines, from two gated")
print("  ingredients; printed, not gated, because it is algebra.")
print("  ROUND-1 BLOCKER 1: it proves an IMPLICATION, and the first")
print("  delivery of this unit read it as an equivalence.  Its actual")
print("  hypothesis is stated first, its sufficiency second]:")
print("    THE HYPOTHESIS THE PROOF USES is exactly one equation:")
print("        Z(Hab) = Z(Hba)   for every commuting pair.")
print("    (depth, sigma)-factoring — Z(h) = Zhat(|h|, sigma(h)) — is")
print("    ONE SUFFICIENT CONDITION for it, and a very special one.")
print("    Given that hypothesis, for every COMMUTING pair,")
print("        P_Z(a|H) P_Z(b|Ha) = q(a|H) q(b|Ha) Z(Hab) / Z(H)")
print("        P_Z(b|H) P_Z(a|Hb) = q(b|H) q(a|Hb) Z(Hba) / Z(H)")
print("    (both telescope), and the two right-hand sides are EQUAL:")
print("    the raw products agree by DC1(b) [gated above, 0")
print("    exceptions], and Z(Hab) = Z(Hba) by hypothesis — which for")
print("    a (depth, sigma)-factoring Z holds because |Hab| = |Hba|")
print("    and sigma(Hab) = sigma(Hba) is the definition of the")
print("    commuting class.  So the DC1 defect is annihilated by ANY")
print("    completion satisfying the displayed equation.")
print("    WHAT THE PROOF DOES NOT GIVE, and the first delivery")
print("    wrongly took from it: (a) it does not say the corpus's")
print("    completions are the ONLY repairs — the solution space of")
print("    the displayed equation is measured in DC1-R below and is")
print("    573-dimensional at the depth-4 truncation, against 28 for")
print("    the (depth, sigma) family; and (b) it says NOTHING about")
print("    DESCENT — 'mu_Z is a function of the record' is a")
print("    different and inequivalent system of equations, and")
print("    DC1-R(e)/(f) exhibit positive completions separating the")
print("    two conditions in BOTH directions.")
print("    THE CORPUS HAS A COMPLETION THAT DOES BOTH.  D49's")
print("    root-free Zhat(h) = 2^(-|h|) . f(class(sigma(h)))")
print("    (lambda = 2, f = (4,4,3,7,3,3)/3) has the factoring shape,")
print("    is normalised per cut at every depth at this scope, and —")
print("    gated below in DC1-R(h), where the first delivery only")
print("    asserted it — its measure mu_Zhat = q.Zhat IS constant on")
print("    every record class of the family.  So Zhat genuinely")
print("    descends.  The price is named and unchanged: D50 — the")
print("    stationary FORM of Z is a CHOICE, i.e. supplied, not")
print("    derived; DC1-R now puts a number on that choice.  That is")
print("    why DC4 item 2 stands as supplied and is priced rather")
print("    than moved.")

# ==================================================================
#  DC1-R — THE REPAIR SPACE.  *** ROUND-1 BLOCKER 1: the computation
#  the first delivery did not run. ***  How big is the space of
#  positive completions that repair the DC1 defect, where does the
#  corpus's family sit inside it, and is "repairs the square" the
#  same condition as "descends to the record"?  Everything below is
#  EXACT rational linear algebra (sparse elimination over Q, no
#  floating point, no modular shortcut).
# ==================================================================
print("\n[DC1-R — THE REPAIR SPACE (round-1 BLOCKER 1).  Setup, and it")
print(" is d42b3's own gradient construction: truncate at depth D; let")
print(" Z be FREE and positive on the depth-D histories and extend it")
print(" downward by the completion recursion Z(h) = sum_e q(e|h)")
print(" Z(h+e), which is exactly what makes P_Z(e|h) = q Z(h+e)/Z(h)")
print(" a normalised kernel.  Then:")
print("   * Z REPAIRS the defect  <=>  Z(Hab) = Z(Hba) for every")
print("     commuting pair whose square closes inside the truncation")
print("     (given DC1(b), this is necessary AND sufficient — see the")
print("     corollary above).  A LINEAR system.")
print("   * Z DESCENDS  <=>  mu_Z = q.Z is a function of the record,")
print("     i.e. Z is constant on record classes (q is, gated in")
print("     DC1-R(i)).  A DIFFERENT linear system.")
print(" Z == 1 solves both, so each solution space meets the positive")
print(" orthant in an OPEN cone and every dimension below is a")
print(" dimension of strictly positive completions.]")

REC = {h: canonH(list(h)) for h in FAM}
_recd = defaultdict(set)
for h in FAM:
    _recd[len(h)].add(REC[h])
REC_BY_DEPTH = [len(_recd[d]) for d in range(CAP + 1)]
REC_ALL = defaultdict(list)
for h in FAM:
    REC_ALL[REC[h]].append(h)
print(f"\n  record classes by depth = {REC_BY_DEPTH}, total "
      f"{len(REC_ALL)}  (d42b3's committed canon; the same layer census "
      f"D49 reports)")


def repair_system(D):
    """(TOP, IDX, W, ROWS) for the depth-D truncation.  W[h] is the row
    of the linear functional Z(h) in the free depth-D coordinates —
    the path-weight vector of h's depth-D descendants.  ROWS holds one
    linear equation Z(Hab) - Z(Hba) = 0 per commuting pair whose
    square closes inside the truncation."""
    TOP = BYD[D]
    IDX = {h: i for i, h in enumerate(TOP)}
    W = {h: {IDX[h]: Fr(1)} for h in TOP}
    for L in range(D - 1, -1, -1):
        for h in BYD[L]:
            r = defaultdict(Fr)
            for e, q in CACHE[h]:
                for k, v in W[h + (e,)].items():
                    r[k] += q * v
            W[h] = dict(r)
    ROWS = []
    for L in range(D - 1):
        for h in BYD[L]:
            mn = CACHE[h]
            for i in range(len(mn)):
                for j in range(i + 1, len(mn)):
                    a, b = mn[i][0], mn[j][0]
                    Ha, Hb = h + (a,), h + (b,)
                    if b not in {e for e, q in CACHE[Ha]}:
                        continue
                    if a not in {e for e, q in CACHE[Hb]}:
                        continue
                    Hab, Hba = Ha + (b,), Hb + (a,)
                    if SIG[Hab] != SIG[Hba]:
                        continue
                    r = defaultdict(Fr)
                    for k, v in W[Hab].items():
                        r[k] += v
                    for k, v in W[Hba].items():
                        r[k] -= v
                    ROWS.append((h, a, b, Hab, Hba,
                                 {k: v for k, v in r.items() if v != 0}))
    return TOP, IDX, W, ROWS


def echelon(rows):
    """EXACT sparse row echelon over Q: column -> the pivot row scaled
    to a leading 1.  Deterministic (rows in family order, columns by
    index).  The rank is len(result)."""
    piv = {}
    for r0 in rows:
        r = dict(r0)
        while r:
            c = min(r)
            if c in piv:
                f = r[c]
                for k, v in piv[c].items():
                    nv = r.get(k, 0) - f * v
                    if nv == 0:
                        r.pop(k, None)
                    else:
                        r[k] = nv
            else:
                f = r[c]
                piv[c] = {k: v / f for k, v in r.items()}
                break
    return piv


RD = 4
R_OK = (CAP >= RD)
if not R_OK:
    print(f"  [SKIPPED: the truncation needs CAP >= {RD}; CAP = {CAP}.]")
    rk4 = dim4 = dsig4 = drec4 = dboth4 = notimp4 = 0
else:
    RTOP, RIDX, RW, RROWS = repair_system(RD)
    RSUB = [h for h in FAM if len(h) <= RD]
    _pv = echelon([r[5] for r in RROWS])
    rk4 = len(_pv)
    dim4 = len(RTOP) - rk4
    print(f"\n  D = {RD}:  free variables (depth-{RD} histories) = "
          f"{len(RTOP)};  repair constraints = {len(RROWS)};")
    print(f"            EXACT rational rank = {rk4}  ->  dim of the "
          f"POSITIVE REPAIR CONE = {dim4}")
    check(f"DC1-R(a) THE REPAIR CONE IS {dim4}-DIMENSIONAL AT THE "
          f"DEPTH-{RD} TRUNCATION [SUBSTANTIVE — this is the number "
          "the first delivery never computed, and the whole of "
          "round-1's BLOCKER].  The necessary-and-sufficient repair "
          "condition Z(Hab) = Z(Hba) is a linear system on the free "
          "boundary values; its exact rational rank is computed by "
          "sparse elimination over Q (no modular shortcut, no float). "
          " Every solution is a completion under which the generated "
          "law's completed kernel satisfies EVERY commuting-square "
          "identity the census tests",
          rk4 == len(RROWS) and dim4 == len(RTOP) - len(RROWS),
          f"variables = {len(RTOP)}, constraints = {len(RROWS)}, exact "
          f"rank = {rk4} (the constraints are independent), dim = "
          f"{dim4}")

    # ---- the (depth, sigma) family inside the cone -------------------
    _sig_top = defaultdict(list)
    for h in RTOP:
        _sig_top[SIG[h]].append(h)
    dsig4 = len(_sig_top)
    # record identity implies sigma identity — the containment that
    # puts the (depth, sigma) family INSIDE the descending family (and
    # the property residue 3 says is a fact about THIS functor).
    _rec_sig_split = sum(1 for c, hs in REC_ALL.items()
                         if len({SIG[h] for h in hs}) > 1)
    _sig_bad = 0
    for s in sorted(_sig_top, key=repr):
        base = {RIDX[h]: Fr(1) for h in _sig_top[s]}
        Zs = {h: sum(base.get(k, 0) * v for k, v in RW[h].items())
              for h in RSUB}
        for (_, _, _, Hab, Hba, _r) in RROWS:
            if Zs[Hab] != Zs[Hba]:
                _sig_bad += 1
    check(f"DC1-R(b) THE (depth, sigma) FAMILY IS A {dsig4}-DIMENSIONAL "
          f"SLICE OF THE {dim4}-DIMENSIONAL CONE [SUBSTANTIVE]: the "
          "completions the dichotomy line forced are the ones "
          "constant on the sigma classes of the boundary cut; each of "
          "its basis vectors is verified to satisfy ALL of the repair "
          "equations (the corollary, instantiated), and it leaves "
          f"{dim4 - dsig4} independent directions of strictly positive "
          "repairs TRANSVERSE to the corpus's family.  The same line "
          "gates the containment that places this family INSIDE the "
          "descending one: record identity implies sigma identity on "
          "every record class of the family — a property of THIS "
          "record functor (residue 3), not a general fact",
          _sig_bad == 0 and 0 < dsig4 < dim4 and _rec_sig_split == 0,
          f"dim (depth,sigma) family = {dsig4} (= the sigma states "
          f"realised at depth {RD}); repair-equation violations across "
          f"its {dsig4} basis vectors = {_sig_bad}; transverse "
          f"directions = {dim4 - dsig4}; record classes carrying two "
          f"sigma values = {_rec_sig_split} of {len(REC_ALL)}")

    # ---- the record-constant (descending) family ---------------------
    # Record classes are ordered by FIRST OCCURRENCE in the enumerator's
    # own history order — NOT by repr, which for a frozenset depends on
    # the interpreter's hash seed.  Every loop below that touches record
    # classes uses this order, so the output is byte-identical across
    # PYTHONHASHSEED values.
    _rec_top = defaultdict(list)
    _rec_order = []
    for h in RTOP:
        if REC[h] not in _rec_top:
            _rec_order.append(REC[h])
        _rec_top[REC[h]].append(h)
    drec4 = len(_rec_top)
    RCB = [{RIDX[h]: Fr(1) for h in _rec_top[c]} for c in _rec_order]
    _prop_bad = 0
    _ZB = []
    for v in RCB:
        Zv = {h: sum(v.get(k, 0) * x for k, x in RW[h].items())
              for h in RSUB}
        _ZB.append(Zv)
        for c, hs in REC_ALL.items():
            if len(hs[0]) > RD:
                continue
            if len({Zv[h] for h in hs if len(h) <= RD}) > 1:
                _prop_bad += 1
    _rec_sub = len({c for c, hs in REC_ALL.items() if len(hs[0]) <= RD})
    QROWS = []
    notimp4 = 0
    for (_, _, _, Hab, Hba, _r) in RROWS:
        qr = {}
        for ci, Zv in enumerate(_ZB):
            s = Zv[Hab] - Zv[Hba]
            if s != 0:
                qr[ci] = s
        if qr:
            notimp4 += 1
            QROWS.append(qr)
    rk_both = len(echelon(QROWS))
    dboth4 = drec4 - rk_both
    check(f"DC1-R(c) THE DESCENDING SUB-CONE IS {dboth4}-DIMENSIONAL "
          "[SUBSTANTIVE]: a completion DESCENDS when mu_Z = q.Z is a "
          "function of the record, i.e. (q being record-constant, "
          "DC1-R(i)) when Z is constant on record classes.  That "
          f"family is {drec4}-dimensional at the boundary cut and — "
          "gated, not assumed — its constancy PROPAGATES downward "
          "through the recursion to every record class of every "
          "shallower depth.  Intersecting it with the repair system "
          "gives the completions that do BOTH",
          _prop_bad == 0 and 0 < dboth4 < dim4,
          f"dim record-constant family = {drec4} (= record classes at "
          f"depth {RD}); downward-propagation violations = {_prop_bad} "
          f"over {_rec_sub} record classes at depths 0..{RD}; rank of "
          f"the repair system ON that family = {rk_both}; dim of "
          f"repairs THAT ALSO DESCEND = {dboth4}")
    check("DC1-R(d) SQUARE-REPAIR AND DESCENT ARE DIFFERENT CONDITIONS, "
          "AND THE HIERARCHY IS STRICT [SUBSTANTIVE — the direct "
          "refutation of the first delivery's 'the completions the "
          "dichotomy line forced are PRECISELY the objects that repair "
          "descent'].  Neither family contains the other: the repair "
          f"cone ({dim4}) is not inside the record-constant family "
          f"({drec4}) and the record-constant family is not inside the "
          "repair cone, since their intersection is a proper subspace "
          "of each; and a repair equation is implied by "
          "record-constancy exactly when its two corners share a "
          "record",
          dboth4 < dim4 and dboth4 < drec4
          and zn_comm == len(RROWS)
          and notimp4 == len(RROWS) - zn_refid,
          f"repair cone {dim4} vs intersection {dboth4} (so repairs "
          f"are NOT all descents); record-constant {drec4} vs "
          f"intersection {dboth4} (so descents are NOT all repairs); "
          f"repair rows NOT implied by record-constancy = {notimp4} of "
          f"{len(RROWS)} (= exactly the {len(RROWS) - zn_refid} rows "
          f"whose two corners carry DIFFERENT records)")

    # ---- WITNESS (i): repairs, does not descend ----------------------
    _pcols = sorted(_pv)
    _free = [c for c in range(len(RTOP)) if c not in _pv]

    def _kernel_vec(fc):
        x = defaultdict(Fr)
        x[fc] = Fr(1)
        for c in reversed(_pcols):
            s = Fr(0)
            for k, v in _pv[c].items():
                if k != c and x.get(k):
                    s += v * x[k]
            if s:
                x[c] = -s
        return {k: v for k, v in x.items() if v != 0}

    w1 = None
    for fc in _free:
        vv = _kernel_vec(fc)
        mx = max(abs(x) for x in vv.values())
        vv = {k: x / mx for k, x in vv.items()}
        base = {i: Fr(1) + vv.get(i, Fr(0)) / 100 for i in range(len(RTOP))}
        Zw = {h: sum(base[k] * x for k, x in RW[h].items()) for h in RSUB}
        bad = sum(1 for (_, _, _, Hab, Hba, _r) in RROWS
                  if Zw[Hab] != Zw[Hba])
        split = [c for c, hs in REC_ALL.items()
                 if len(hs[0]) <= RD
                 and len({QPATH[h] * Zw[h] for h in hs if len(h) <= RD}) > 1]
        if split:
            w1 = (fc, len(vv), all(z > 0 for z in Zw.values()), bad,
                  len(split), sorted(len(REC_ALL[c]) for c in split))
            break
    print(f"\n  WITNESS (i) — A POSITIVE COMPLETION THAT REPAIRS EVERY")
    print(f"  SQUARE AND DOES NOT DESCEND.  Construction, deterministic:")
    print(f"  the kernel vectors of the repair system are read off the")
    print(f"  exact echelon in free-column order, each scaled to")
    print(f"  max|v| = 1; the FIRST one that is not record-constant is")
    print(f"  taken and Z = 1 + v/100 (so 99/100 <= Z <= 101/100 at the")
    print(f"  boundary and Z > 0 everywhere).  Result: free column "
          f"{w1[0] if w1 else None},")
    print(f"  kernel support {w1[1] if w1 else None} — Z > 0: "
          f"{w1[2] if w1 else None}; repair-equation violations: "
          f"{w1[3] if w1 else None} of {len(RROWS)};")
    print(f"  record classes carrying TWO different mu_Z values: "
          f"{w1[4] if w1 else None} (sizes {w1[5] if w1 else None}).")
    print(f"  [The round-1 referee's own witness of this shape reported "
          f"4 violated")
    print(f"  record-constancy equations with a size-4 class; the exact "
          f"counts are")
    print(f"  a property of WHICH kernel direction is taken — the "
          f"verdict is not.]")
    check("DC1-R(e) WITNESS (i): 'ANNIHILATES THE DEFECT' DOES NOT "
          "IMPLY 'DESCENDS' [SUBSTANTIVE — it fails if every repair is "
          "record-constant, which is what the first delivery's "
          "'precisely' would require].  A strictly positive completion "
          "that satisfies EVERY commuting-square identity the census "
          "tests, and whose induced measure mu_Z = q.Z is NOT a "
          "function of the record: a single record class carries two "
          "different masses, so P_Z is not the conditional system of "
          "any measure on record cylinders",
          w1 is not None and w1[2] and w1[3] == 0 and w1[4] > 0,
          f"positive = {w1[2] if w1 else None}, repair violations = "
          f"{w1[3] if w1 else None}/{len(RROWS)}, record classes with "
          f"two mu values = {w1[4] if w1 else None}")

    # ---- WITNESS (ii): descends, does not repair ---------------------
    _TL, _TR = Fr(39003, 1659203), Fr(3000, 127631)
    n_break = 0
    n_two = 0
    n_refnum = 0
    refhit = []
    for c in _rec_order:
        base = {i: Fr(1) for i in range(len(RTOP))}
        for h in _rec_top[c]:
            base[RIDX[h]] = Fr(101, 100)
        Zw = {h: sum(base[k] * x for k, x in RW[h].items()) for h in RSUB}
        bad = [(H, a, b, Hab, Hba) for (H, a, b, Hab, Hba, _r) in RROWS
               if Zw[Hab] != Zw[Hba]]
        if not bad:
            continue
        n_break += 1
        if len(bad) == 2:
            n_two += 1
        H, a, b, Hab, Hba = bad[0]
        _qh = {e: q for e, q in CACHE[H]}
        _ma = {e: q for e, q in CACHE[H + (a,)]}
        _mb = {e: q for e, q in CACHE[H + (b,)]}
        LZ = _qh[a] * _ma[b] * Zw[Hab] / Zw[()]
        RZ = _qh[b] * _mb[a] * Zw[Hba] / Zw[()]
        if {LZ, RZ} == {_TL, _TR}:
            n_refnum += 1
        if not refhit and len(bad) == 2 and (LZ, RZ) == (_TL, _TR):
            refhit = [c, len(bad), H, a, b, LZ, RZ, len(_rec_top[c])]
    print(f"\n  WITNESS (ii) — A POSITIVE MEASURE ON REFINED RECORD")
    print(f"  CYLINDERS WHOSE CONDITIONALS VIOLATE THE SIGMA-COMMUTING")
    print(f"  SQUARE IDENTITY.  Construction, deterministic: Z = 1 on")
    print(f"  the boundary cut except on ONE record class, set to")
    print(f"  101/100, extended by the same recursion — so Z is")
    print(f"  record-constant by construction, mu_Z = q.Z is a positive")
    print(f"  measure on refined record cylinders (constant on all")
    print(f"  {_rec_sub} record classes of depth <= {RD}, and additive")
    print(f"  along cuts by the recursion), and yet:")
    print(f"    depth-{RD} record classes whose perturbation breaks at")
    print(f"    least one sigma-commuting square = {n_break} of "
          f"{drec4}; of those,")
    print(f"    {n_two} break exactly two.")
    if refhit:
        print(f"    THE ROUND-1 REFEREE'S OWN WITNESS, RECONSTRUCTED "
              f"EXACTLY:")
        print(f"      H = {refhit[2]}")
        print(f"      a = {refhit[3]}")
        print(f"      b = {refhit[4]}")
        print(f"      P_Z(a|H) P_Z(b|Ha) = {refhit[5]}")
        print(f"      P_Z(b|H) P_Z(a|Hb) = {refhit[6]}   (sigma equal, "
              f"RECORDS DIFFER)")
        print(f"      ratio = {refhit[5] / refhit[6]}; squares broken = "
              f"{refhit[1]}; perturbed class size = {refhit[7]}")
        print(f"    ({n_refnum} of the {drec4} single-class "
              f"perturbations reproduce that exact")
        print(f"    pair of products; the one printed is the first in "
              f"the deterministic")
        print(f"    scan — record classes ordered by first occurrence "
              f"in the enumerator's")
        print(f"    own history order, never by repr, whose value for a "
              f"frozenset is")
        print(f"    hash-seed dependent.  The round-1 referee printed "
              f"this same witness at")
        print(f"    another pair of the same shape — a propose at the "
              f"root and that same")
        print(f"    actor's idle — and reported the SAME two products, "
              f"the same ratio and")
        print(f"    the same verdict.)")
    check("DC1-R(f) WITNESS (ii): 'DESCENDS' DOES NOT IMPLY "
          "'ANNIHILATES THE DEFECT' [SUBSTANTIVE — and it is the "
          "second half of round-1's BLOCKER, plus the direct evidence "
          "for MAJOR 1].  A strictly positive measure on refined "
          "record cylinders exists whose conditionals violate the "
          "sigma-commuting square identity — at a pair whose two "
          "records DIFFER, which is exactly the class paper 29 §3.1 "
          "exempts.  CONSEQUENCE: DC1(a) is not by itself a descent "
          "test, and Theorem 1 is untouched by its failures outside "
          "the refined class.  The referee's own witness (the exact "
          "fractions 39003/1659203 and 3000/127631) is reconstructed "
          "here from a deterministic scan, not imported",
          n_break > 0 and bool(refhit),
          f"perturbations breaking >= 1 square = {n_break} of {drec4}; "
          f"exactly two = {n_two}; reproducing the referee's exact "
          f"products = {n_refnum}; referee's witness reconstructed = "
          f"{bool(refhit)}")

# ---- the depth-5 truncation -----------------------------------------
if CAP >= 5:
    RTOP5, RIDX5, RW5, RROWS5 = repair_system(5)
    rk5 = len(echelon([r[5] for r in RROWS5]))
    dim5 = len(RTOP5) - rk5
    dsig5 = len({SIG[h] for h in RTOP5})
    drec5 = len({REC[h] for h in RTOP5})
    print(f"\n  D = 5:  variables {len(RTOP5)}; repair constraints "
          f"{len(RROWS5)}; EXACT rank {rk5};")
    print(f"          dim repair cone = {dim5}   vs  (depth,sigma) "
          f"family = {dsig5},  record-constant = {drec5}")
    check("DC1-R(g) THE SAME PICTURE ONE LEVEL DEEPER [SUBSTANTIVE]: "
          "at the depth-5 truncation the repair cone grows to "
          f"{dim5} dimensions while the (depth, sigma) family grows "
          f"only to {dsig5} — the gap is not an artefact of the depth-4 "
          "cut, it widens with depth, because the family is bounded by "
          "the 36 states while the cone grows with the boundary",
          rk5 == len(RROWS5) and dim5 > dim4 and dsig5 < 36,
          f"variables = {len(RTOP5)}, constraints = {len(RROWS5)}, "
          f"exact rank = {rk5}, dim = {dim5}, (depth,sigma) = {dsig5}, "
          f"record-constant = {drec5}")
else:
    dim5 = dsig5 = 0

# ---- the bottom of the hierarchy: D49's Zhat ------------------------
_TM = [[Fr(0)] * len(STATES) for _ in STATES]
for s in STATES:
    hrep = _SHORTREP[s]
    for e, q in CACHE[hrep]:
        _nx = SIG[hrep + (e,)] if (hrep + (e,)) in SIG \
            else canon_sigma(hrep + (e,))
        _TM[SIDX[s]][SIDX[_nx]] += q


def dense_nullspace(M, n):
    """EXACT null space basis of an n x n rational matrix."""
    A = [row[:] for row in M]
    piv = {}
    r = 0
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


_NS = len(STATES)
_eig = {}
for lam in (Fr(2), Fr(1), Fr(5, 2), Fr(9, 4)):
    B = dense_nullspace(
        [[_TM[i][j] - (lam if i == j else Fr(0)) for j in range(_NS)]
         for i in range(_NS)], _NS)
    if B:
        v = B[0]
        v = [x / min((y for y in v if y != 0), key=abs) for x in v]
        cen = defaultdict(int)
        for x in v:
            cen[str(x)] += 1
        _eig[str(lam)] = (len(B), all(x > 0 for x in v), dict(spec(cen)), v)
    else:
        _eig[str(lam)] = (0, None, {}, None)
print("\n  THE TRANSFER OPERATOR (T f)(s) = sum_e q(e|s) f(s.e) on the "
      f"{_NS} states:")
for lam in ('2', '1', '5/2', '9/4'):
    k, onesign, cen, _ = _eig[lam]
    print(f"    lambda = {lam:>4}:  ker dim {k}" +
          (f", one-signed generator = {onesign}, value census {cen}"
           if k else "  (empty)"))
_f2 = _eig['2'][3]
ZHAT = {}
_zh_bad = 0
_zh_mu = defaultdict(set)
if _f2 is not None:
    for h in FAM:
        ZHAT[h] = Fr(1, 2 ** len(h)) * _f2[SIDX[SIG[h]]]
    for d in range(CAP):
        for h in BYD[d]:
            if sum(q * ZHAT[h + (e,)] for e, q in CACHE[h]) != ZHAT[h]:
                _zh_bad += 1
    for h in FAM:
        _zh_mu[REC[h]].add(QPATH[h] * ZHAT[h])
_zh_split = sum(1 for v in _zh_mu.values() if len(v) > 1)
check("DC1-R(h) THE BOTTOM OF THE HIERARCHY: D49's Zhat IS ONE RAY, "
      "AND ITS MEASURE GENUINELY DESCENDS [SUBSTANTIVE — and it "
      "supplies the gate the first delivery asserted without one "
      "(round-1 MINOR 2): the corollary gives only the SQUARE "
      "identity, and by DC1-R(e) that does not imply descent].  "
      "Inside the (depth, sigma) family the depth-stationary form "
      "Z = 2^(-|h|) f(sigma) is the lambda = 2 eigenvector of the "
      "transfer operator: its kernel is ONE-dimensional with a "
      "strictly positive generator taking the values {1, 4/3, 7/3} "
      "with multiplicities {29, 5, 2} (= D49's f = (4,4,3,7,3,3)/3), "
      "lambda = 1 has a MIXED-SIGN generator (so there is no "
      "depth-ungraded completion of this form) and lambda = 5/2, 9/4 "
      "have none.  Zhat is harmonic for the completion recursion at "
      "every depth of the family, and mu_Zhat = q.Zhat is CONSTANT ON "
      "EVERY RECORD CLASS — so Zhat's measure IS a function of the "
      "record: the corpus's selected completion really does descend",
      (_eig['2'][0] == 1 and _eig['2'][1] is True
       and _eig['1'][0] == 1 and _eig['1'][1] is False
       and _eig['5/2'][0] == 0 and _eig['9/4'][0] == 0
       and _zh_bad == 0 and _zh_split == 0 and len(_zh_mu) > 0
       and (_eig['2'][2] == {'1': 29, '4/3': 5, '7/3': 2}
            if CAP == 6 else True)),
      f"ker(T - 2I) dim = {_eig['2'][0]}, positive = {_eig['2'][1]}, "
      f"values = {_eig['2'][2]}; ker(T - I) dim = {_eig['1'][0]}, "
      f"one-signed = {_eig['1'][1]}; ker(T - 5/2 I) = {_eig['5/2'][0]}, "
      f"ker(T - 9/4 I) = {_eig['9/4'][0]}; harmonicity violations = "
      f"{_zh_bad}; record classes = {len(_zh_mu)}, classes carrying "
      f"two mu_Zhat values = {_zh_split}")

# ---- the raw weight: order-independent, and NOT a measure -----------
_qcls = defaultdict(set)
for h in FAM:
    _qcls[REC[h]].add(QPATH[h])
_q_split = sum(1 for v in _qcls.values() if len(v) > 1)
CUTS = [sum(QPATH[h] for h in BYD[d]) for d in range(CAP + 1)]
print(f"\n  THE RAW PATH WEIGHT q(h) = prod q:  constant on "
      f"{len(_qcls) - _q_split} of {len(_qcls)} record classes;")
print(f"  cut masses sum_{{|h| = n}} q(h), n = 0..{CAP}: "
      f"{[str(c) for c in CUTS]}")
check("DC1-R(i) THE RAW WEIGHT IS ORDER-INDEPENDENT GLOBALLY — AND IT "
      "IS NOT A MEASURE [SUBSTANTIVE, two-sided].  (+) DC1(b) says "
      "the raw products agree on adjacent commuting squares; the "
      "stronger global statement is gated here: q(h) is constant on "
      "EVERY record class of the family, so the unnormalised weight "
      "is a function of the record.  (-) But q is NOT a measure on "
      "cylinders (round-1 MINOR 1): it is not additive along cuts — "
      "the cut masses printed above are 1, 2, 4, 257/32, ... and not "
      "constant — which is precisely why a completion is needed at "
      "all.  The correct wording is 'the unnormalised weight is "
      "ORDER-INDEPENDENT', never 'the unnormalised weight descends "
      "to a record measure'",
      _q_split == 0 and len(set(CUTS)) > 1 and CUTS[0] == Fr(1),
      f"record classes = {len(_qcls)}, classes carrying two q values = "
      f"{_q_split}; cut masses = {[str(c) for c in CUTS]} (not "
      f"constant, so q is not additive along cuts)")

print("\n  *** DC1-R VERDICT — THE HIERARCHY (round-1 BLOCKER 1) ***")
print(f"    repair cone ({dim4})  STRICTLY CONTAINS")
print(f"    repairs that also descend ({dboth4})  STRICTLY CONTAINS")
print(f"    the (depth, sigma) family ({dsig4})  STRICTLY CONTAINS")
print(f"    the depth-stationary ray (1) = D49's Zhat")
print(f"    [at D = 5: {dim5} / {dsig5} — the gap widens with depth]")
print("    Reading it in words.  The descent defect names the JOB a")
print("    completion has to do; it does NOT single out the corpus's")
print("    completions among the objects that do it.  What collapses")
print("    the cone to one ray is D50's FORM choice — depth-stationary")
print("    factoring through sigma — which is supplied, not derived,")
print("    and is now a number rather than an adjective.  The two")
print("    lines therefore MEET more weakly than the first delivery")
print("    said: the corpus's completions are AMONG the repairs (and")
print("    Zhat's measure genuinely descends, DC1-R(h)), but 'the")
print("    completions the dichotomy line forced are PRECISELY the")
print("    objects that repair descent' is FALSE IN BOTH DIRECTIONS")
print("    (DC1-R(e), DC1-R(f)).  The successor question sharpens to:")
print("    is there any RECORD-LEVEL demand that cuts the cone down to")
print("    the family, or is the family selected only by the form?")
print(f"  [t = {time.time() - T0:.1f}s]")

# ==================================================================
#  DC2 — BOUNDARY SUFFICIENCY  (paper 29 Theorem 2 / F2)
#  *** A RESTATEMENT GATE.  NOT A NEW RESULT. ***
# ==================================================================
print("\n[DC2 — BOUNDARY SUFFICIENCY (paper 29 Theorem 2 / F2).")
print(" *** RESTATEMENT GATE — REPORTING ONLY.  NOTHING NEW IS PROVED")
print(" HERE.  Paper 29 Theorem 2 says a boundary-only kernel exists")
print(" EXACTLY WHEN the next-record law is constant on the fibres of")
print(" the declared boundary statistic.  With pi = sigma that")
print(" condition IS (H1), a THEOREM of D61; the state update is (H2),")
print(" a THEOREM of D62.  The CONTENT of this gate is the")
print(" IDENTIFICATION — the generated line's declared boundary")
print(" statistic EXISTS and is sigma — and the printing of the kernel.")
print(" F-DC2 (pin §4) is: mislabelling this as new.  It is not new. ***")
FIB = defaultdict(set)
CMENU = {}
for h in FAM:
    CMENU[h] = canon_menu(h)
    FIB[SIG[h]].add(CMENU[h])
fib_split = sum(1 for v in FIB.values() if len(v) > 1)
check("DC2(a) FIBRE CONSTANCY, re-affirmed directly on the family "
      "[RESTATEMENT of (H1) = d44a CG1; the THEOREM is carried by "
      "note-d61-h1-closure-result.md, this is its re-run]: every two "
      "histories with the same sigma have the SAME renamed menu "
      "multiset with exact weights — so pi(x) = pi(x') implies "
      "L_x = L_x', which is exactly Theorem 2's necessary and "
      "sufficient condition",
      fib_split == 0 and len(FIB) == len(STATES),
      f"fibres = {len(FIB)}, fibres with two different menus = "
      f"{fib_split}, histories swept = {len(FAM)}")
print("\n  THE 36-ROW NORMALISED KERNEL K(. | sigma), EXACT.")
print("  Rows are sigma classes (index, mass, serialised state);")
print("  entries are renamed event classes with their probabilities.")
KROWS = {}
_SHORT = _SHORTREP
for i, s in enumerate(STATES):
    rep = _SHORT[s]
    rows = ast.literal_eval(CMENU[rep])
    m = SMASS[s]
    KROWS[s] = tuple((ev, Fr(w) / m) for ev, w in rows)
    print(f"\n  sigma[{i:2d}]  mass = {m}   shortest witness depth "
          f"{len(rep)}")
    print(f"     state: {s}")
    for ev, p in KROWS[s]:
        print(f"       K = {str(p):>8}   {ev}")
rowsum_bad = sum(1 for s in STATES
                 if sum(p for ev, p in KROWS[s]) != Fr(1))
_kmenu_bad = 0
for h in FAM:
    rows = ast.literal_eval(CMENU[h])
    if tuple((ev, Fr(w) / SMASS[SIG[h]]) for ev, w in rows) != KROWS[SIG[h]]:
        _kmenu_bad += 1
check("DC2(b) THE KERNEL IS THE LAW [COROLLARY OF DC2(a) — it can "
      "only fail if DC2(a) fails; a reporting line for the printed "
      "object]: at EVERY history of the family "
      "the normalised renamed menu equals the row K(.|sigma(h)) "
      "printed above, entrywise with exact Fractions — so the printed "
      "36-row object IS the generated next-record law, not a summary "
      "of it [RESTATEMENT of (H1); it can only fail if DC2(a) fails]",
      _kmenu_bad == 0, f"histories = {len(FAM)}, rows disagreeing with "
      f"the printed kernel = {_kmenu_bad}")
check("DC2(c) EVERY KERNEL ROW NORMALISES EXACTLY [REPORTING-ONLY, "
      "CANNOT FAIL — this "
      "is division by the row's own mass; printed "
      "because the pin asks for the kernel, in the D58-A3 "
      "reporting-line style]",
      rowsum_bad == 0, f"rows = {len(STATES)}, rows not summing to 1 = "
      f"{rowsum_bad}")
print(f"  [t = {time.time() - T0:.1f}s]")

# ==================================================================
#  DC3 — THE FIVE DURABLE-RECORD HYPOTHESES  (paper 29 §4.3)
# ==================================================================
print("\n[DC3 — paper 29 §4.3's five durable-record hypotheses, gated "
      "one by one, each labelled by what it can and cannot do]")

# ---- (1) exclusive and exhaustive durable alternatives -------------
# SUBSTANTIVE.  It can fail two ways: a repeated event in the menu
# (not exclusive), or an admissible event the menu omits (not
# exhaustive).  The pool is built INDEPENDENTLY of candidates_for.
def pool_of(hk, single_base):
    """every well-formed event over the tokens h has uttered: idles,
    proposes on every base present, arbs over every nonempty set of
    uttered proposal triples with every nonempty winner subset.
    single_base=True restricts ckeys to one base (justified by the
    quoted code-fact 'admissible's ckey match is by COMPONENT
    triples'); single_base=False is the unrestricted surface."""
    full = View(list(hk), ep(list(hk)), set(range(len(hk))))
    bases = sorted({V0} | {vname(next(iter(op[2]))[1], op[3], op[1])
                           for op in full.arbs.values()}, key=repr)
    trips = sorted({(op[1], op[2], op[3])
                    for op in full.props.values()}, key=repr)
    out = []
    for a in AB:
        out.append(('n', a))
        for b in bases:
            for x in (0, 1):
                out.append(('p', a, b, x))
        n = len(trips)
        for smask in range(1, 1 << n):
            S = [trips[i] for i in range(n) if smask >> i & 1]
            if single_base and len({t[1] for t in S}) != 1:
                continue
            ck = frozenset(S)
            for wmask in range(1, 1 << len(S)):
                W = frozenset(S[i] for i in range(len(S))
                              if wmask >> i & 1)
                out.append(('r', a, ck, W))
    return out


ex_bad_missing = ex_bad_extra = ex_bad_weight = ex_dup = 0
ex_pool = 0
for h in FAM:
    mn = CACHE[h]
    if len({e for e, q in mn}) != len(mn):
        ex_dup += 1
    md = {e: q for e, q in mn}
    seen = set()
    for e in pool_of(h, True):
        if e in seen:
            continue
        seen.add(e)
        ex_pool += 1
        ok, q = adm(list(h), e)
        if ok and e not in md:
            ex_bad_missing += 1
        if ok and e in md and md[e] != q:
            ex_bad_weight += 1
        if (not ok) and e in md:
            ex_bad_extra += 1
ux_bad = ux_pool = 0
for h in FAM:
    if len(h) > 4:
        continue
    md = {e: q for e, q in CACHE[h]}
    seen = set()
    for e in pool_of(h, False):
        if e in seen:
            continue
        seen.add(e)
        ux_pool += 1
        ok, q = adm(list(h), e)
        if ok and (e not in md or md[e] != q):
            ux_bad += 1
        if (not ok) and e in md:
            ux_bad += 1
check("DC3(1) ENUMERATION COMPLETENESS OF candidates_for AGAINST "
      "admissible [SUBSTANTIVE — it can fail two ways and neither is "
      "excluded a priori.  SCOPE OF THE CLAIM, corrected in round 1 "
      "(MINOR 7): the adversarial POOL is built independently of "
      "candidates_for, but the VERDICT on each pool event is d42b3's "
      "own `admissible`, which is also what candidates_for calls — so "
      "what is tested is that the menu enumeration is complete and "
      "non-redundant WITH RESPECT TO admissible, not the grammar's "
      "exclusivity or exhaustiveness in any sense independent of the "
      "layer]: at every "
      "history of the family the menu is a set of PAIRWISE DISTINCT "
      "events (exclusivity: no alternative is listed twice), and it "
      "is EXACTLY the admissible set — the pool of well-formed events "
      "over the tokens the "
      "history has uttered finds NO admissible event the menu omits, "
      "NO menu event the layer refuses, and NO weight disagreement",
      ex_dup == 0 and ex_bad_missing == 0 and ex_bad_extra == 0
      and ex_bad_weight == 0,
      f"histories = {len(FAM)}, pool events tested = {ex_pool} "
      f"(single-based ckeys); duplicate-menu histories = {ex_dup}; "
      f"omitted admissible = {ex_bad_missing}; refused-but-listed = "
      f"{ex_bad_extra}; weight disagreements = {ex_bad_weight}")
check("DC3(1') THE SAME GATE ON THE UNRESTRICTED SURFACE (the "
      "single-base restriction of the pool above is itself lifted): "
      "over every history of depth <= 4, ckeys spanning ANY set of "
      "uttered triples, with every winner subset — still exactly the "
      "menu, entrywise with weights",
      ux_bad == 0, f"histories = {sum(1 for h in FAM if len(h) <= 4)}, "
      f"pool events tested = {ux_pool}, violations = {ux_bad}")

# ---- (2) decoherence of the queried record algebra -----------------
print("\n  DC3(2) DECOHERENCE OF THE QUERIED RECORD ALGEBRA "
      "[REPORTING ONLY — TRIVIALLY SATISFIED AND THEREFORE")
print("  UNINFORMATIVE; there is NO gate here that could fail, and")
print("  the pin (§2, DC3 clause 2) requires this to be said plainly].")
print("    The generated law is a CLASSICAL stochastic process on")
print("    records: sigma is a serialised finite state, the menu is a")
print("    finite set of exact Fraction weights, and the queried")
print("    algebra is the algebra of history cylinders itself.  A")
print("    classical process has a diagonal decoherence functional by")
print("    construction, so hypothesis (2) holds for the empty reason.")
print("    WHERE THE REMAINING MAP SEGMENT LIVES: paper 29's")
print("    hypothesis (2) is a condition on class OPERATORS and their")
print("    Gram functional D(alpha,beta) = <v_alpha, v_beta> (§4.1,")
print("    §4.2).  The generated line has NO functional level at all —")
print("    no amplitudes, no class operators, no Gram functional, and")
print("    hence no non-trivial decoherence condition to satisfy or")
print("    violate.  This unit does NOT create one.  So the segment of")
print("    the missing map that runs from a decoherence functional to")
print("    the generated record measure is UNTOUCHED here, and it is")
print("    exactly the segment where D59's items 'record instrument'")
print("    and 'preferred durable algebra' still sit.")
check("DC3(2) [REPORTING-ONLY, CANNOT FAIL — labelled as the pin's "
      "F-DC3 requires]: the generated law is classical, so "
      "decoherence of the queried record algebra is satisfied "
      "trivially and carries NO information about the map",
      True, "no falsifiable content; the map's functional segment is "
      "named above and is untouched by this unit")

# ---- (3) one common refined cylinder -------------------------------
check("DC3(3) ONE COMMON REFINED CYLINDER [= DC1(a), THE SAME "
      "PREDICATE, counted here because §4.3 lists it — round-1 "
      "MAJOR 3: the three FAILs of this receipt are TWO statements, "
      "DC1(a) (= this gate) and DC1(f), and DC1(f) is the "
      "load-bearing one.  Note that the hypothesis §4.3 actually "
      "states is the REFINED one, so DC1(f) is the closer reading of "
      "this clause]: the identity that a common refined cylinder "
      "forces, tested on every sigma-commuting pair",
      DC1_HOLDS, f"sigma-commuting pairs = {n_comm}, failures = "
      f"{n_defect}; on the refined sub-class {n_refined_defect} of "
      f"{n_refined} (DC1(f)); see the DC1 census above")

# ---- (4) positive mass for every displayed conditioning cylinder ---
pos_bad = 0
pos_n = 0
minw = None
for h in FAM:
    for e, q in CACHE[h]:
        pos_n += 1
        if not (q > 0):
            pos_bad += 1
        if minw is None or q < minw:
            minw = q
cyl_bad = 0
cyl_n = 0
for h in FAM:
    mn = CACHE[h]
    N = MASS(h)
    if not (N > 0):
        cyl_bad += 1
    for e, q in mn:
        cyl_n += 1
        if not (q / N > 0):
            cyl_bad += 1
check("DC3(4) POSITIVITY OF EVERY DISPLAYED CONDITIONING CYLINDER "
      "[SUBSTANTIVE — a zero weight anywhere would make a displayed "
      "conditional undefined and would void DC1's test on that pair]: "
      "every menu weight is a STRICTLY POSITIVE exact Fraction, every "
      "menu mass is strictly positive, and hence every conditional "
      "P(e|H) = q/N used anywhere in this receipt is strictly "
      "positive.  The support of the law is exactly the admissible "
      "set (DC3(1)) — the law never displays a zero-mass alternative",
      pos_bad == 0 and cyl_bad == 0 and pos_n > 0,
      f"menu entries = {pos_n}, non-positive weights = {pos_bad}; "
      f"conditionals = {cyl_n}, non-positive = {cyl_bad}; smallest "
      f"weight in the family = {minw}")

# ---- (5) sufficient declared boundary ------------------------------
check("DC3(5) SUFFICIENT DECLARED BOUNDARY [RESTATEMENT, = DC2(a)'s "
      "OWN PREDICATE — the same computation reported twice because "
      "§4.3 lists it; it is (H1) + (H2) and NOT a new result]: "
      "pi = sigma is a "
      "sufficient boundary statistic, the kernel K(.|sigma) exists on "
      "36 values and is printed above",
      fib_split == 0, f"fibres = {len(FIB)}, non-constant fibres = "
      f"{fib_split}")
print(f"  [t = {time.time() - T0:.1f}s]")

# ==================================================================
#  DC4 — THE SUPPLIED-VS-DERIVED LEDGER, RE-SCORED
# ==================================================================
print("\n[DC4 — D59's six supplied-not-derived items, re-scored at "
      "the closed scope.  NO ITEM MOVES WITHOUT A GATE ABOVE IT.]")
print("  D59 §2 quotes paper 29's abstract: the corpus 'supplies")
print("  rather than derives' (1) boundary state, (2) measure and")
print("  contour, (3) renormalization, (4) record instrument,")
print("  (5) generated record grammar, (6) clock dictionary.")
print("  Re-scored against THIS unit's gates only:\n")
LEDGER = [
    ("1. boundary state",
     "STANDS as supplied — CORRECTED IN ROUND 1 (MAJOR 2).  The "
     "generated line has its own DERIVED boundary statistic; D59's "
     "item is a different object and does not move.",
     "Ground: D59's six items are quoted from paper 29's abstract, "
     "where the possessive is the IDENTIFIED law's: the corpus "
     "supplies rather than derives ITS boundary state, and §9.2's "
     "slot table names the object as the 'boundary/cosmological state "
     "— selects amplitudes and long-range correlations'.  The "
     "generated line's sigma was never on that list, so it cannot "
     "move ON that list; item 5 below has exactly this shape and is "
     "scored the same way.  WHAT IS TRUE, and it is a theorem, "
     "belongs beside the ledger rather than inside it: on the "
     "generated side the declared boundary statistic is not "
     "supplicated — sigma is CONSTRUCTED from the committed layer, "
     "its sufficiency is (H1) [D61] + (H2) [D62], and the 36-row "
     "kernel is printed (DC2(a)/(b)/(c)).  That is a derived boundary "
     "statistic FOR THE GENERATED LINE; the action line's "
     "boundary/cosmological state remains supplied, untouched by "
     "every gate in this receipt."),
    ("2. measure and contour",
     "STANDS as supplied — and DC1 SHARPENS why.",
     "Ground: DC1(a) FAILS / DC1(b)+DC1(c) locate the failure.  The "
     "generated law has an order-independent UNNORMALISED weight "
     "(DC1(b)) and a normalised kernel that is NOT order-independent "
     "(DC1(a)); the gap between them is exactly the coboundary of the "
     "state-mass function (DC1(c)).  A measure on record cylinders "
     "therefore requires a completion — supplied data, whose form D50 "
     "already showed is a choice (DC1-C exhibits one that works, at "
     "its own stated cost).  Not derived, and now PRICED WITH A "
     "NUMBER rather than an adjective (DC1-R): at the depth-4 "
     "truncation the completions that repair the defect form a "
     "573-dimensional positive cone, of which 205 dimensions also "
     "descend and 28 are the (depth, sigma) family the dichotomy line "
     "forced; the selection down to D49's one ray is D50's FORM "
     "choice, not a consequence of descent."),
    ("3. renormalization",
     "STANDS as supplied.  Untouched by every gate above.",
     "Ground: no gate in this unit concerns a continuum limit, a "
     "regulator or a scale.  The generated law is finite and "
     "combinatorial; renormalization is an action-line slot and this "
     "unit produced no fact about it."),
    ("4. record instrument",
     "STANDS as supplied.  DC3(2) says exactly why it cannot move.",
     "Ground: DC3(2) is reporting-only.  The generated line is "
     "classical and has NO functional level — no class operators, no "
     "Gram decoherence functional — so it cannot derive which "
     "alternatives decohere or which algebra is queried.  What DC3(1) "
     "does establish is narrower and worth stating: the generated "
     "line's OWN alternative set is exclusive and exhaustive and its "
     "support is exactly the admissible set.  That is a record "
     "GRAMMAR fact, not a record INSTRUMENT fact."),
    ("5. generated record grammar",
     "STANDS as supplied FOR THE ACTION LINE; on the generated line "
     "it was never supplied.  No movement is claimed.",
     "Ground: D59's item is 'the identified (D15) law has not been "
     "given a generated record grammar'.  The d42a grammar exists and "
     "this unit gated its exclusivity/exhaustiveness (DC3(1)) and its "
     "boundary sufficiency (DC2) — but NOTHING here connects it to "
     "the D15 action content.  Paper 29 Theorem 5 is untouched."),
    ("6. clock dictionary",
     "STANDS as supplied.  Untouched by every gate above.",
     "Ground: no gate in this unit produces a rate, a unit or a time "
     "coordinate.  Paper 29's Theorem 1 needs no time coordinate and "
     "neither does this receipt; the dictionary slot is exactly where "
     "D59 left it."),
]
for name, verdict, ground in LEDGER:
    print(f"  {name}")
    print(f"    VERDICT: {verdict}")
    print(f"    {ground}\n")
moved = sum(1 for n, v, g in LEDGER if v.startswith("MOVES"))
check("DC4 THE LEDGER IS GATE-BOUND, AND NOTHING MOVES ON IT "
      "[REPORTING — the predicate reads a hand-written literal list "
      "in this same file, so it is a bookkeeping line, not a "
      "measurement; it is printed because the pin asks for the "
      "re-scoring].  ROUND-1 MAJOR 2: the first delivery moved item 1 "
      "(boundary state) from supplied to derived.  That was a "
      "conflation of the ACTION line's slot — paper 29 §9.2's "
      "boundary/cosmological state — with the GENERATED line's own "
      "derived statistic, and it contradicted this receipt's own "
      "treatment of item 5, which has the identical shape and stands. "
      " Corrected: all six items STAND; the generated line's derived "
      "boundary statistic is stated beside the ledger, not inside it",
      moved == 0 and len(LEDGER) == 6,
      f"items = {len(LEDGER)}, moved = {moved}, standing = "
      f"{len(LEDGER) - moved}")

# ==================================================================
#  DET — determinism of the load-bearing iteration
# ==================================================================
print("\n[DET — determinism probe]")
det_spec = defaultdict(int)
det_comm = 0
for h in sorted((h for h in FAM if len(h) <= 3), key=repr, reverse=True):
    mn = list(reversed(CACHE[h]))
    N = MASS(h)
    qh = {e: q for e, q in mn}
    for i in range(len(mn)):
        for j in range(i + 1, len(mn)):
            a, b = mn[i][0], mn[j][0]
            Ha, Hb = h + (a,), h + (b,)
            ma = {e: q for e, q in CACHE[Ha]}
            mb = {e: q for e, q in CACHE[Hb]}
            if b not in ma or a not in mb:
                continue
            if canon_sigma(Ha + (b,)) != canon_sigma(Hb + (a,)):
                continue
            det_comm += 2
            Na, Nb = MASS(Ha), MASS(Hb)
            _d = ((qh[a] / N) * (ma[b] / Na)
                  / ((qh[b] / N) * (mb[a] / Nb)))
            det_spec[str(_d)] += 1
            det_spec[str(1 / _d)] += 1
ref_spec = defaultdict(int)
ref_comm = 0
for h in FAM:
    if len(h) > 3:
        continue
    mn = CACHE[h]
    N = MASS(h)
    qh = {e: q for e, q in mn}
    for i in range(len(mn)):
        for j in range(i + 1, len(mn)):
            a, b = mn[i][0], mn[j][0]
            Ha, Hb = h + (a,), h + (b,)
            ma = {e: q for e, q in CACHE[Ha]}
            mb = {e: q for e, q in CACHE[Hb]}
            if b not in ma or a not in mb:
                continue
            if canon_sigma(Ha + (b,)) != canon_sigma(Hb + (a,)):
                continue
            ref_comm += 2
            Na, Nb = MASS(Ha), MASS(Hb)
            _d = ((qh[a] / N) * (ma[b] / Na)
                  / ((qh[b] / N) * (mb[a] / Nb)))
            ref_spec[str(_d)] += 1
            ref_spec[str(1 / _d)] += 1
check("DET(a) ORDER-INDEPENDENCE OF THE CENSUS ITSELF [BOOKKEEPING "
      "LINE — round-1 MAJOR 4(b): the enumeration is a full double "
      "loop over an unordered pair set and every pair records BOTH d "
      "and 1/d, so the count and the spectrum are order-invariant by "
      "construction; kept because the discipline it encodes is the "
      "reason every census here is ordered].  The defect d "
      "INVERTS under the swap of a and b, so a census taken on one "
      "direction per unordered pair would depend on which element the "
      "enumeration calls 'a'; every census here is therefore over "
      "ORDERED pairs, and this gate is what holds that discipline: "
      "re-running the DC1 sub-census over parents of depth <= 3 with "
      "the parent list and every menu REVERSED reproduces the same "
      "commuting count and the same exact defect spectrum",
      det_comm == ref_comm and spec(det_spec) == spec(ref_spec)
      and ref_comm > 0,
      f"commuting (forward) = {ref_comm}, (reversed) = {det_comm}; "
      f"spectra equal = {spec(det_spec) == spec(ref_spec)}; spectrum "
      f"= {spec(ref_spec)}")
check("DET(b) NO LOAD-BEARING SET ITERATION [BOOKKEEPING LINE — "
      "round-1 MAJOR 4(b): the predicate is an isinstance check on "
      "the enumerator's own return value and cannot fail; the "
      "substance is the byte-identity under PYTHONHASHSEED "
      "variation, which is run externally and recorded in the result "
      "note]: every ordered structure "
      "this receipt builds is a list from the committed enumerator or "
      "a sorted sequence (sorted(...) on refs, tokens, states and "
      "pools); every census is aggregated into a dict and PRINTED "
      "sorted by key.  The receipt is additionally expected to be "
      "byte-identical under PYTHONHASHSEED variation (run externally, "
      "recorded in the result note)",
      all(isinstance(CACHE[h], list) for h in FAM),
      "checked: every cached menu is the enumerator's own list")

# ==================================================================
print("\n[VERDICT]")
anchored = (CAP == 6 and census == CENSUS_REF and len(STATES) == 36
            and len(NKEY) == 176)
substantive_ok = (ex_dup == 0 and ex_bad_missing == 0
                  and ex_bad_extra == 0 and ex_bad_weight == 0
                  and ux_bad == 0 and pos_bad == 0 and cyl_bad == 0
                  and fib_split == 0 and mass_split == 0
                  and coboundary_bad == 0 and _ksplitA == 0
                  and _ksplitB == 0 and set(raw_spec) == {'1'}
                  and _q_split == 0 and _zh_bad == 0 and _zh_split == 0
                  and cl_one == 0 and cl_sigdiff == 0
                  and (not R_OK or _rec_sig_split == 0))
print("  SCOPE (non-negotiable): two-actor DELIVERY-FREE d42a, the")
print(f"  exhaustive depth-{CAP} family.  Nothing below is licensed")
print("  beyond it, and nothing below transfers to the identified")
print("  (action-line) click law: paper 29's map remains open.\n")
if not DC1F_HOLDS:
    print("  DC1(f) — THE LOAD-BEARING TEST — FAILS.  THE FAILURE IS")
    print("  THE DELIVERABLE (pin §2/§4).")
    print(f"  {n_refined_defect} of {n_refined} REFINED-RECORD-IDENTICAL")
    print("  ordered pairs violate P(a|H)P(b|Ha) = P(b|H)P(a|Hb).")
    print(f"  On the wider sigma-commuting class (DC1(a), the pin's")
    print(f"  coarser predicate) the count is {n_defect} of {n_comm} —")
    print(f"  but {n_notrefined_defect} of those failures lie OUTSIDE")
    print("  Theorem 1's hypothesis, which paper 29 §3.1 explicitly")
    print("  exempts, and carry no descent content (DC1-R(f) exhibits a")
    print("  genuine record measure that fails the same wider test).")
elif not DC1_HOLDS:
    print("  DC1(a) fails on the wider sigma-commuting class while the")
    print("  refined sub-census holds — see the census above.")
else:
    print("  DC1 — HOLDS on every commuting pair of the family.")
if not DC1_HOLDS:
    print("  The structure of the failure is COMPLETE:")
    if set(raw_spec) == {'1'}:
        print("    - the RAW products always agree (DC1(b), gated), so")
        print("      the generated law's unnormalised history weight IS")
        print("      order-independent on commuting pairs — and, more")
        print("      strongly, q is constant on every record class")
        print("      (DC1-R(i)).  It is NOT a measure: the cut masses")
        print(f"      are {[str(c) for c in CUTS]}, so q is not additive")
        print("      along cuts, which is why a completion is needed;")
    if coboundary_bad == 0:
        print("    - the entire defect is the NORMALISATION: exactly")
        print("      d = M(sigma(Hb))/M(sigma(Ha)), the coboundary of the")
        print("      per-state menu mass (DC1(c), gated) — a MASS-RATIO")
        print("      COCYCLE, the pin's pre-registered structural")
        print("      fallback, in its sharpest form;")
    print(f"    - the defect spectrum is exactly {spec(defect_spec)};")
    if _ksplitA == 0 and _ksplitB == 0:
        print("      and it is a function of (sigma(H), class(a),")
        print("      class(b)) alone under both key resolutions (DC1(d),")
        print(f"      gated) — {len(KEYA)} classes, which with DC1(i)'s")
        print(f"      {cl_tot} class-level facts is the census's real")
        print("      information content;")
    if set(samemass_spec) <= {'1'} and '1' not in diffmass_spec:
        print("    - it VANISHES exactly on same-mass intermediates and")
        print("      occurs at every mass-mixed pair (DC1(e), gated) —")
        print("      the pin's lean was right, and nothing else fails.")
if not DC1F_HOLDS and pos_bad == 0 and cyl_bad == 0:
    print("  CONSEQUENCE, stated exactly and no wider: there is NO")
    print("  positive measure on refined record cylinders at this")
    print("  scope whose conditionals are the generated NORMALISED")
    print("  kernel — paper 29 Theorem 1's contrapositive, applied to")
    print("  a system that satisfies its three positivity hypotheses")
    print("  (DC3(4), gated) and its cylinder-identity hypothesis")
    print("  (DC1(f), the refined sub-census, gated).")
    print("  This does NOT contradict Theorem 1 (a theorem), and it is")
    print("  NOT an F1 hit: F1 asks for a MEASURE with unequal")
    print("  products; what is exhibited is a conditional system that")
    print("  is not induced by any such measure.  The generated law is")
    print("  ORDER-WEIGHTED at the normalised level, and any map from")
    print("  the action line's conditional-measure reading to it must")
    print("  carry order data or supply a completion.")
    print("  AND THE DEFECT IS REPAIRABLE, BUT NOT ONLY BY THE CORPUS'S")
    print("  COMPLETIONS (DC1-R): the repair cone has dimension")
    print(f"  {dim4} at the depth-4 truncation, of which {dboth4}")
    print(f"  dimensions also descend and {dsig4} are the (depth, sigma)")
    print("  family; the corpus's Zhat is one ray inside it whose")
    print("  measure genuinely descends (DC1-R(h)).  Square-repair and")
    print("  descent imply each other in NEITHER direction (DC1-R(e),")
    print("  DC1-R(f)).  The descent defect names the JOB the corpus's")
    print("  completions do; it does not single them out.")
print("\n  DC2 — RESTATEMENT, satisfied.  pi = sigma; fibre constancy")
print("  is (H1); the 36-row kernel is printed.  NOT A NEW RESULT.")
print("  DC3 — (1) SUBSTANTIVE, PASS; (2) reporting-only, trivially")
print("  satisfied and uninformative; (3) = DC1(a), "
      + ("FAIL" if not DC1_HOLDS else "PASS") + "; (4) SUBSTANTIVE,")
print("  PASS; (5) = DC2, restatement.")
print("  DC4 — NO item moves; all six stand (round-1 MAJOR 2).  The")
print("  generated line's own derived boundary statistic is stated")
print("  beside the ledger, not on it.")
print("\n  THE FAIL COUNT, READ HONESTLY (round-1 MAJOR 3): the FAILs")
print("  below are TWO statements, not one and not three — DC1(a)")
print("  (= DC3(3), literally the same predicate) and DC1(f), which is")
print("  a different predicate over a different population under a")
print("  strictly stronger hypothesis, and is the only one of them")
print("  paper 29's theorem speaks to.")
if not anchored:
    print("\n  [NON-ANCHORED RUN: CAP != 6 or an anchor moved — no")
    print("  verdict sentence above may be quoted.]")
print(f"\n[d65] {PASS} PASS / {FAIL} FAIL"
      + (f"  ({ANCHOR_FAIL} anchor failures)" if ANCHOR_FAIL else "")
      + f"  [family depth {CAP}; {n_unord} unordered menu pairs "
      f"= {n_pairs} ordered; substantive-gate block "
      f"{'clean' if substantive_ok else 'DIRTY'}; runtime "
      f"{time.time() - T0:.1f}s]")
sys.exit(1 if ANCHOR_FAIL else 0)
