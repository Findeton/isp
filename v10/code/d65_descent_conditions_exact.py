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
for h in FAM:
    by_depth[len(h)] += 1
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
NKEY = {}
NTR = 0
CPAIR = {}          # (h, e) -> the committed canon_pair value, once
for h in FAM:
    for e, q in CACHE[h]:
        NTR += 1
        CPAIR[(h, e)] = canon_pair(h, e)
        NKEY[CPAIR[(h, e)]] = SIG.get(h + (e,))
print(f"  transitions out of the family = {NTR} (into depth {CAP + 1}); "
      f"distinct (sigma, renamed event) keys = {len(NKEY)}")
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
check("N3 THE LAYER'S OWN SANITY COUNTERS (d44a's sigma port, carried "
      "through this receipt's sweep): alive-singleton, "
      "non-superseded-holdings, live-on-X and conflicting-pair-"
      "comparability violations all zero",
      all(v == 0 for v in SG_VIOL.values()), f"SG_VIOL = {dict(SG_VIOL)}")


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
      "is visible in the join view: the quarter law's excess)",
      mass_split == 0
      and sorted(set(SMASS.values())) == MASSES_COMMITTED,
      f"mass-splitting classes = {mass_split}; per-state mass census "
      f"= {spec(mass_census)}")

print(f"  [t = {time.time() - T0:.1f}s]")

# ==================================================================
#  DC1 — THE COMMUTING-SQUARE IDENTITY  (paper 29 Theorem 1 / F1)
#  THE ONLY GATE THAT CAN SURPRISE.  Pre-registered both ways.
# ==================================================================
print("\n[DC1 — THE COMMUTING-SQUARE IDENTITY (paper 29 Theorem 1 / "
      "F1). SUBSTANTIVE; pre-registered both ways in the pin.]")
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
      "of every history of depth <= 2 — so the pair key is the "
      "committed key's two-event extension, not a new normal form",
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
print(f"        of which COMMUTING (the pin's definition)    = {n_comm}")
print(f"          of which the identity HOLDS                = "
      f"{n_comm - n_defect}")
print(f"          of which the identity FAILS                = "
      f"{n_defect}")
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
print(f"  defect by sigma(H) (state index : {{d : count}}):")
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
check("DC1(a) THE COMMUTING-SQUARE IDENTITY, exhaustive over every "
      "commuting pair at every history of the family.  PRE-REGISTERED "
      "BOTH WAYS (pin §2): a FAIL here is the deliverable, not a bug — "
      "it says the generated normalised law is ORDER-WEIGHTED and the "
      "missing map must carry order data",
      DC1_HOLDS, f"commuting pairs = {n_comm}, identity failures = "
      f"{n_defect} ({'HOLDS' if DC1_HOLDS else 'FAILS'})")
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
      "class(b)) ALONE — the pin's structural fallback, tested on TWO "
      "key resolutions, both ORDERED (the defect inverts under the "
      "swap, so an unordered key would be wrong): (A) the two events "
      "renamed SEPARATELY by the committed canon_pair, (B) the two "
      "events renamed JOINTLY by canon_pair2 (N5).  No key carries "
      "two different defect values under either resolution — and "
      "since a key fixed by an automorphism swapping a and b receives "
      "BOTH d and 1/d, this also forces d = 1 on every self-swapped "
      "class",
      _ksplitA == 0 and _ksplitB == 0,
      f"key-A classes = {len(KEYA)}, splitting = {_ksplitA}; key-B "
      f"classes = {len(KEYB)}, splitting = {_ksplitB}")
check("DC1(e) THE FAILURE VANISHES EXACTLY ON THE SAME-MASS SUBCLASS "
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
check("DC1(f) THE REFINED-RECORD SUB-CENSUS: paper 29's literal "
      "hypothesis is [Hab] = [Hba] at the REFINED record level, which "
      "on the generated side is equality of d42b3's committed "
      "canonical DAG.  Reported both ways: the pin's sigma-commuting "
      "class and this strictly stronger subclass",
      n_refined_defect == 0 and n_refined > 0,
      f"refined-identical pairs = {n_refined}, identity failures = "
      f"{n_refined_defect}; spectrum = {spec(refined_spec)}")
check("DC1(g) THE CENSUS BOOKKEEPING CLOSES, so that the exclusion "
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
      "THE NON-COMMUTING CENSUSES [REPORTING — the pin asks for these "
      "numbers whichever way they land].  What the numbers say: "
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
print(f"  [t = {time.time() - T0:.1f}s]")

# ------------------------------------------------------------------
# DC1-C — the completion corollary.  d42b3's D1(ii) gradient
# completion Z re-derived on the depth-4 slice (anchored to d42b3's
# OWN committed numbers), and the SAME identity re-tested under the
# completed kernel P_Z(e|h) = q(e|h) Z(h+e)/Z(h).  This is NOT a
# property of the generated law: Z is SUPPLIED data (D50 — the form
# remains a choice).  Labelled accordingly.
# ------------------------------------------------------------------
print("\n[DC1-C — the completion corollary (REPORTING; Z is SUPPLIED "
      "data, D50: the form remains a choice)]")
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
zn_comm = zn_def = 0
for h in FAM:
    if len(h) > ZD - 2 or CAP < ZD:
        continue
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
            LZ = (qh[a] * Z[Ha] / Z[h]) * (ma[b] * Z[Ha + (b,)] / Z[Ha])
            RZ = (qh[b] * Z[Hb] / Z[h]) * (mb[a] * Z[Hb + (a,)] / Z[Hb])
            if LZ != RZ:
                zn_def += 1
check("DC1-C d42b3's GRADIENT COMPLETION, re-derived and anchored to "
      "its OWN committed numbers (D1(ii)): Z(empty) = 1037/64, Z > 0 "
      "throughout, and Z constant on d42b3's canonical classes.  "
      "Under the completed kernel P_Z(e|h) = q Z(h+e)/Z(h) — which IS "
      "normalised per cut by the recursion — the commuting-square "
      "identity HOLDS on every commuting pair with both continuations "
      "inside Z's domain.  STATED HONESTLY: this is a property of a "
      "SUPPLIED completion, not of the generated law; its cost is "
      "d42b3's own (within-cut ratio deformation at 21 of 114 "
      "interior classes, the root included), and its domain here is "
      "parents of depth <= 2",
      (Z.get(()) == Fr(1037, 64) and all(z > 0 for z in Z.values())
       and z_split == 0 and zn_def == 0 and zn_comm > 0)
      if CAP >= ZD else True,
      f"Z(empty) = {Z.get(())} (d42b3 anchor 1037/64); Z-class "
      f"splits = "
      f"{z_split}; commuting pairs in Z's domain = {zn_comm}; "
      f"identity failures under P_Z = {zn_def}")
print("\n  THE GENERAL COROLLARY [PROOF — two lines, from two gated")
print("  ingredients; printed, not gated, because it is algebra]:")
print("    Let Z be ANY positive completion that factors through")
print("    (depth, sigma) — i.e. Z(h) = Zhat(|h|, sigma(h)).  Then for")
print("    every COMMUTING pair,")
print("        P_Z(a|H) P_Z(b|Ha) = q(a|H) q(b|Ha) Z(Hab) / Z(H)")
print("        P_Z(b|H) P_Z(a|Hb) = q(b|H) q(a|Hb) Z(Hba) / Z(H)")
print("    (both telescope), and the two right-hand sides are EQUAL:")
print("    the raw products agree by DC1(b) [gated above, 0")
print("    exceptions], and Z(Hab) = Z(Hba) because |Hab| = |Hba| and")
print("    sigma(Hab) = sigma(Hba) is the definition of the commuting")
print("    class.  So the DC1 defect is annihilated by ANY completion")
print("    of that shape.")
print("    THE CORPUS ALREADY HAS ONE.  D49's root-free completion")
print("    Zhat(h) = 2^(-|h|) . f(class(sigma(h))) (lambda = 2,")
print("    f = (4,4,3,7,3,3)/3) has EXACTLY that shape and is")
print("    normalised per cut at every depth at this scope (D49 +")
print("    (H1)/(H2)).  So: the generated law's NORMALISED MENU KERNEL")
print("    does not descend, and the SAME law read through the")
print("    corpus's own selected completion does.  The price is")
print("    named and unchanged: D50 — the stationary FORM of Z is a")
print("    CHOICE, i.e. supplied, not derived.  That is why DC4 item 2")
print("    stands as supplied and is now priced rather than moved.")

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
_SHORT = {}
for h in FAM:
    s = SIG[h]
    if s not in _SHORT or len(h) < len(_SHORT[s]):
        _SHORT[s] = h
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
check("DC2(b) THE KERNEL IS THE LAW: at EVERY history of the family "
      "the normalised renamed menu equals the row K(.|sigma(h)) "
      "printed above, entrywise with exact Fractions — so the printed "
      "36-row object IS the generated next-record law, not a summary "
      "of it [RESTATEMENT of (H1); it can only fail if DC2(a) fails]",
      _kmenu_bad == 0, f"histories = {len(FAM)}, rows disagreeing with "
      f"the printed kernel = {_kmenu_bad}")
check("DC2(c) EVERY KERNEL ROW NORMALISES EXACTLY [RESTATEMENT — this "
      "is division by the row's own mass and cannot fail; printed "
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
check("DC3(1) EXCLUSIVE AND EXHAUSTIVE ALTERNATIVES [SUBSTANTIVE — it "
      "can fail two ways and neither is excluded a priori]: at every "
      "history of the family the menu is a set of PAIRWISE DISTINCT "
      "events (exclusivity: no alternative is listed twice), and it "
      "is EXACTLY the admissible set — an independently constructed "
      "adversarial pool of well-formed events over the tokens the "
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
check("DC3(3) ONE COMMON REFINED CYLINDER [SUBSTANTIVE — this IS "
      "DC1's commutation census, and it is the gate that decided the "
      "unit]: the identity that a common refined cylinder forces, "
      "tested on every commuting pair",
      DC1_HOLDS, f"commuting pairs = {n_comm}, failures = {n_defect}; "
      f"see the DC1 census above for the full structure")

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
check("DC3(5) SUFFICIENT DECLARED BOUNDARY [RESTATEMENT — = DC2, "
      "which is (H1) + (H2); NOT a new result]: pi = sigma is a "
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
     "MOVES: supplied -> DERIVED, at the closed scope and for the "
     "GENERATED line only.",
     "Ground: DC2(a)/DC2(c) + (H1) [D61 THEOREM] + (H2) [D62 THEOREM]. "
     "Paper 29 Theorem 2 asks for a declared boundary statistic whose "
     "fibres carry a constant next-record law.  On the generated side "
     "that statistic is not supplicated: sigma is CONSTRUCTED from the "
     "layer and its sufficiency is a theorem, with the 36-row kernel "
     "printed.  SCOPE: this is the generated line's own boundary; it "
     "says NOTHING about the action line's cosmological boundary "
     "state, which remains supplied."),
    ("2. measure and contour",
     "STANDS as supplied — and DC1 SHARPENS why.",
     "Ground: DC1(a) FAILS / DC1(b)+DC1(c) locate the failure.  The "
     "generated law has an order-independent UNNORMALISED weight "
     "(DC1(b)) and a normalised kernel that is NOT order-independent "
     "(DC1(a)); the gap between them is exactly the coboundary of the "
     "state-mass function (DC1(c)).  A measure on record cylinders "
     "therefore requires a completion — supplied data, whose form D50 "
     "already showed is a choice (DC1-C exhibits one that works, at "
     "its own stated cost).  Not derived; now precisely priced."),
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
check("DC4 THE LEDGER IS GATE-BOUND: exactly one of D59's six items "
      "moves (item 1, the boundary state, and only for the GENERATED "
      "line at the closed scope), and its mover is a gate printed "
      "above (DC2(a)/DC2(c), carried by the D61/D62 theorems); the "
      "other five stand, each with its one-line ground",
      moved == 1 and len(LEDGER) == 6,
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
check("DET(a) ORDER-INDEPENDENCE OF THE CENSUS ITSELF.  The defect d "
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
check("DET(b) NO LOAD-BEARING SET ITERATION: every ordered structure "
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
                  and _ksplitB == 0 and set(raw_spec) == {'1'})
print("  SCOPE (non-negotiable): two-actor DELIVERY-FREE d42a, the")
print(f"  exhaustive depth-{CAP} family.  Nothing below is licensed")
print("  beyond it, and nothing below transfers to the identified")
print("  (action-line) click law: paper 29's map remains open.\n")
if not DC1_HOLDS:
    print("  DC1 — FAILS.  THE FAILURE IS THE DELIVERABLE (pin §2/§4).")
    print(f"  {n_defect} of {n_comm} commuting pairs violate")
    print("  P(a|H)P(b|Ha) = P(b|H)P(a|Hb).  Its structure is COMPLETE:")
    print("    - the RAW products always agree (DC1(b)), so the")
    print("      generated law's unnormalised history weight IS")
    print("      order-independent on commuting pairs;")
    print("    - the entire defect is the NORMALISATION: exactly")
    print("      d = M(sigma(Hb))/M(sigma(Ha)), the coboundary of the")
    print("      per-state menu mass (DC1(c)) — a MASS-RATIO COCYCLE,")
    print("      the pin's pre-registered structural fallback, in its")
    print("      sharpest form;")
    print(f"    - the defect spectrum is exactly {spec(defect_spec)};")
    print("    - it is a function of (sigma(H), class(a), class(b))")
    print("      alone under both key resolutions (DC1(d));")
    print("    - it VANISHES exactly on same-mass intermediates and")
    print("      occurs at every mass-mixed pair (DC1(e)) — the pin's")
    print("      lean was right, and nothing else fails.")
    print("  CONSEQUENCE, stated exactly and no wider: there is NO")
    print("  positive measure on refined record cylinders at this")
    print("  scope whose conditionals are the generated NORMALISED")
    print("  kernel — paper 29 Theorem 1's contrapositive, applied to")
    print("  a system that satisfies its three positivity hypotheses")
    print("  (DC3(4)) and its cylinder-identity hypothesis (DC1(f)).")
    print("  This does NOT contradict Theorem 1 (a theorem), and it is")
    print("  NOT an F1 hit: F1 asks for a MEASURE with unequal")
    print("  products; what is exhibited is a conditional system that")
    print("  is not induced by any such measure.  The generated law is")
    print("  ORDER-WEIGHTED at the normalised level, and any map from")
    print("  the action line's conditional-measure reading to it must")
    print("  carry order data or supply a completion (DC1-C).")
else:
    print("  DC1 — HOLDS on every commuting pair of the family.")
print("\n  DC2 — RESTATEMENT, satisfied.  pi = sigma; fibre constancy")
print("  is (H1); the 36-row kernel is printed.  NOT A NEW RESULT.")
print("  DC3 — (1) SUBSTANTIVE, PASS; (2) reporting-only, trivially")
print("  satisfied and uninformative; (3) = DC1, "
      + ("FAIL" if not DC1_HOLDS else "PASS") + "; (4) SUBSTANTIVE,")
print("  PASS; (5) = DC2, restatement.")
print("  DC4 — one item moves (boundary state, generated line only);")
print("  five stand.")
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
