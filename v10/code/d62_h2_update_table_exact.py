#!/usr/bin/env python3
"""
d62_h2_update_table_exact.py — v10 D62: closing (H2), the update table.
Pin: note-d62-h2-update-table-pin.md (STRICT).  Proof note:
note-d62-h2-update-table.md (the rows, written out as prose-over-code);
parents: note-d61-h1-closure-result.md ((H1) [THEOREM], (H0) discharged
incl. Lemma 7b) and the adopted proof note note-d60p-h1-probe.md
§3-§9 (Lemmas 1-7b, invariants 5a-5e, ser()/serialisation, the (H2)
corollary with its three obligations O1/O2/O3).

WHAT THIS RECEIPT IS AND IS NOT.  The THEOREM force comes from the
NOTE's rows being proofs — each row a reading of the committed layer
plus Lemma 5's invariants.  These gates are EVIDENCE for the rows,
NEVER premises: a cache-gated table check alone cannot close the depth
gap (the D61 §4/§5 lesson, restated in the pin in advance so it cannot
be over-promised a third time).  What the gates buy is that the TABLE
AS WRITTEN IN THE NOTE — implemented here as ONE function reading only
(serialised sigma, renamed event), never a history — reproduces the
committed layer's sigma(h+e) at every cached transition, on every
abstract transition key of the reachable quotient, and that the three
obligations' PREMISES hold everywhere they are consumed.

Exit protocol (pin §4): exit 0 for substantive negatives — a genuine
(H2) counterexample IS the deliverable — exit 1 ONLY on anchor
breakage (N0-class: the committed-layer and d44a slices, the census).
TWO-ACTOR DELIVERY-FREE d42a ONLY.

Run:  python3 v10/code/d62_h2_update_table_exact.py [FAMDEPTH]
      (default 6: transitions into depth 7.  The depth is PRINTED;
      there is no silent cap.)
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


T0 = time.time()
print("[D62 — (H2): the update table, gated against the committed layer]")
print("  banner: the THEOREM is carried by note-d62-h2-update-table.md")
print("  (the four rows + O1/O2/O3, prose-over-code).  This receipt")
print("  implements THE TABLE as one function of (serialised sigma,")
print("  renamed event) — it never sees a history — and compares it")
print("  with the layer's own sigma(h+e).  TWO-ACTOR d42a ONLY.")

# ------------------------------------------------------------------
# N0 — the committed layers, by TEXT SLICE (never re-implemented).
# Idiom copied from v10/code/d61_h1_closure_exact.py.
# ------------------------------------------------------------------
_s = open('v10/code/d42b3_placement_exact.py').read()
_PREFIX = _s[:_s.index('print("[d42b3')]
ns = {}
exec(_PREFIX, ns)
cf, ep, V0, vname = (ns['candidates_for'], ns['event_poset'],
                     ns['V0'], ns['vname'])
adm = ns['admissible']
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
own_alive = ns['own_alive']

check("N0(a) SINGLE SOURCES: d42b3's admission layer (candidates_for / "
      "admissible / event_poset / regs_of / vname / V0) and d44a's "
      "sigma_raw / ser / canon_sigma / _rename_event / _menu_extras / "
      "canon_pair extracted VERBATIM by text slice (the d61 idiom); "
      "the slices carry the expected definitions, not merely callables",
      callable(canon_sigma) and callable(canon_pair) and callable(ser)
      and "def sigma_raw" in _blk1 and "def ser(" in _blk1
      and "def canon_sigma" in _blk1 and "def own_alive" in _blk1
      and "def _rename_event" in _blk2 and "def _menu_extras" in _blk2
      and "def canon_pair" in _blk3
      and "def candidates_for" in _PREFIX and "def admissible" in _PREFIX,
      "d42b3 prefix + 3 d44a slices", anchor=True)

# the d50 lesson: nothing executable may survive a text slice.
_stray = [(nm, b.count("sys.exit"), b.count("\ncheck("), b.count("\nprint("))
          for nm, b in (('blk1', _blk1), ('blk2', _blk2), ('blk3', _blk3))]
check("N0(b) SLICE HYGIENE (the d50 lesson): the three d44a slices are "
      "PURE DEFINITIONS — zero sys.exit, zero top-level check(), zero "
      "top-level print() survive the extraction, so nothing of d44a's "
      "own gate protocol can execute inside this receipt; the d42b3 "
      "prefix is cut before its first print, as in d61",
      all(x == 0 for nm, a, c, p in _stray for x in (a, c, p))
      and 'sys.exit' not in _PREFIX,
      f"stray (exit, check, print) per slice = "
      f"{[(nm, a, c, p) for nm, a, c, p in _stray]}", anchor=True)

# ------------------------------------------------------------------
# N0(c) — the CODE-FACTS the note's rows read, asserted against source
# ------------------------------------------------------------------
_F = {
    "vname is a structural 5-tuple ('v', base, values(W), authors(W), init)":
        "    return ('v', base, value, authors, init)",
    "regs_of: p/n occupy the actor register":
        "    if op[0] in ('p', 'n'): return frozenset([op[1]])",
    "regs_of: an r occupies its ckey's PROPOSERS + the fresh version":
        "    return frozenset(props | {vname(base, op[3], op[1])})",
    "View: every arb in the view supersedes its base":
        "            self.superseded.add(next(iter(op[2]))[1])",
    "View: every arb in the view resolves exactly its ckey triples":
        "            self.resolved |= set(op[2])",
    "View.live: a proposal is live iff its triple is unresolved":
        "                     if (op[1], op[2], op[3]) not in self.resolved}",
    "View.live: the comprehension head (round-1 MINOR 2 — the missing "
    "half)":
        "        self.live = {i: op for i, op in self.props.items()",
    "holdings(a): a gains the minted version iff a proposed in the ckey":
        "                h.add(vname(base, op[3], op[1]))",
    "holdings(a): the proposer test itself — the note's (L5) (round-1 "
    "MINOR 2)":
        "            if a in {t[0] for t in op[2]}:",
    "edges(): a conflict edge needs same base, opposite bits, INCOMPARABLE":
        "                        and self.incomparable(i, k)):",
    "edges(): the bit predicate — the entire content of Row 0 (round-1 "
    "MINOR 2)":
        "                if (pi[2] == pk[2] and pi[3] != pk[3]",
    "prop_options_in_view refuses a superseded base":
        "        if b in view.superseded: continue",
    "prop_options_in_view refuses a base already carrying a live own "
    "proposal":
        "        if any(op[1] == a and op[2] == b for op in view.live.values()):",
    "arb_components_in_view refuses a superseded base":
        "        if base in view.superseded: continue",
    "arb_components_in_view returns only components containing an "
    "a-proposal (the proposer test — Lemma 2's last step, and O2's "
    "hinge)":
        "        if a in {view.props[i][1] for i in comp}:",
    "admissible reaches the ckey ONLY through arb_components_in_view":
        "    comps = arb_components_in_view(view, a)",
    "admissible's ckey match is by component triples":
        "    match = [c for c in comps if triples(view, c[1]) == ckey]",
}
_missing = [k for k, v in _F.items() if v not in _s]
check("N0(c) CODE-FACTS: every source line the note's rows and the "
      f"three obligations read is present VERBATIM in the committed "
      f"d42b3 source ({len(_F)} lines: vname's structure, regs_of, "
      "View's superseded/resolved/live, holdings, edges' "
      "incomparability clause, both admissibility refusals, and "
      "arb_components_in_view's proposer test)",
      not _missing, f"quoted lines = {len(_F)}, missing = {_missing}",
      anchor=True)
_F2 = {
    "sigma_raw drops a full-superseded holding to None":
        "        hold[a] = X[a] if X[a] not in sup else None",
    "refs = non-None holds u live-carrying bases":
        "    refs = sorted({b for b in (hold['A'], hold['B']) if b is not None}",
    "ser writes sup ONLY restricted to refs (round-1 MINOR 10)":
        "                 tuple(sorted((m[b], b in sup) for b in refs))))",
    "_menu_extras sends a base outside the sigma renaming to 100 + i":
        "                m2[extras[i]] = 100 + eperm[i]",
}
_missing2 = [k for k, v in _F2.items() if v not in _ds]
check("N0(d) CODE-FACTS: the four d44a source lines that define WHAT "
      "THE TABLE TRANSFORMS (hold's None convention, refs, ser's "
      "restriction of sup to refs, and canon_pair's 100+i extension "
      "for a base outside the sigma renaming — the O1 token)",
      not _missing2, f"quoted lines = {len(_F2)}, missing = {_missing2}",
      anchor=True)

# ==================================================================
#  THE TABLE — note-d62-h2-update-table.md §3, rows R1/R2/R2'/R3/R4.
#  Reads ONLY (serialised sigma, renamed event).  No history, no
#  poset, no view, no layer call except the committed ser().
# ==================================================================
NEW = ('NEW',)          # the fresh version token minted by an arb (O2)
ROWS = ('R1-idle', 'R2-propose-held', "R2'-propose-dropped-base",
        'R3-self-arb', 'R4-pair-arb')


def comps_of_live(live):
    """comps as a FUNCTION OF live (note §3 Row 0): by (5b) each actor
    has at most one live proposal, so a base carries at most two; by
    LEMMA 7b two conflicting live proposals are always incomparable,
    so edges() = {same base, opposite bits} with no poset test left.
    This is obligation O3."""
    by = {}
    for t in live:
        by.setdefault(t[1], []).append(t)
    out = []
    for b in sorted(by, key=repr):
        ts = by[b]
        if len(ts) == 2 and ts[0][2] != ts[1][2]:
            mem = tuple(sorted((t[0], t[2]) for t in ts))
            E = (tuple(sorted(((ts[0][0], ts[0][2]),
                               (ts[1][0], ts[1][2])))),)
            out.append((b, mem, E))
        else:
            for t in ts:
                out.append((b, ((t[0], t[2]),), ()))
    return tuple(out)


def canon_parts(hold, live, comps, refs, sup):
    """canon_sigma's minimisation, applied to PARTS instead of a
    history — the committed ser() is called verbatim."""
    best = None
    for perm in permutations(range(len(refs))):
        m = {refs[i]: perm[i] for i in range(len(refs))}
        s = ser(hold, live, comps, refs, sup, m)
        if best is None or s < best:
            best = s
    return best


def parse_sigma(sig):
    """sigma is ser()'s repr: (hold, live, comps, (token, in sup)*)."""
    hold_t, live_t, comps_t, refsup_t = ast.literal_eval(sig)
    return dict(hold_t), tuple(live_t), tuple(comps_t), dict(refsup_t)


def TABLE(sig, ev):
    """THE UPDATE TABLE.  In: sigma(h) as ser() writes it, and the
    event renamed into the same token language (canon_pair's ebest).
    Out: (sigma(h+e), row).  Nothing else is read."""
    hold, live, comps, supf = parse_sigma(sig)
    e = ast.literal_eval(ev)
    x = e[1]
    y = 'B' if x == 'A' else 'A'
    supf = dict(supf)
    if e[0] == 'n':                                   # ---- Row R1
        return sig, 'R1-idle'
    if e[0] == 'p':                                   # ---- Row R2/R2'
        b, i = e[2], e[3]
        if b in supf:
            row = 'R2-propose-held'
        else:
            row = "R2'-propose-dropped-base"
            supf[b] = True          # O1: the dropped base IS superseded
        hold2 = dict(hold)
        live2 = tuple(sorted(live + ((x, b, i),), key=repr))
    else:
        ck = tuple(e[2])
        base = ck[0][1]
        if len({t[0] for t in ck}) == 1:              # ---- Row R3
            row = 'R3-self-arb'
            hold2 = {x: NEW, y: (None if hold[y] == base else hold[y])}
            live2 = tuple(t for t in live if t not in set(ck))
        else:                                         # ---- Row R4
            row = 'R4-pair-arb'
            hold2 = {x: NEW, y: NEW}
            live2 = ()
        supf[base] = True
        supf[NEW] = False           # O2: the minted token is FRESH
    comps2 = comps_of_live(live2)                     # ---- Row 0 (O3)
    refs2 = sorted({hold2[a] for a in AB if hold2[a] is not None}
                   | {t[1] for t in live2}, key=repr)
    sup2 = {b for b, f in supf.items() if f}
    return canon_parts(hold2, live2, comps2, refs2, sup2), row


_BLIND_FORBIDDEN = ('event_poset', 'View', 'candidates_for',
                    'admissible', 'sigma_raw', 'canon_sigma',
                    'own_alive', 'cands_of', 'FAM', 'CACHE')
_blind_names = set(TABLE.__code__.co_names) \
    | set(comps_of_live.__code__.co_names) \
    | set(canon_parts.__code__.co_names) \
    | set(parse_sigma.__code__.co_names)
check("N0(e) THE TABLE IS BLIND TO HISTORY, checked through its WHOLE "
      "call graph (round-1 MINOR 4: the first draft inspected TABLE "
      "and comps_of_live only, so a history read one call down would "
      "have passed): TABLE, comps_of_live, canon_parts and "
      "parse_sigma together mention no history, poset, view or layer "
      "enumerator — the table reads its two arguments and calls only "
      "the committed ser()",
      not (_blind_names & set(_BLIND_FORBIDDEN))
      and 'ser' in canon_parts.__code__.co_names,
      f"call-graph global reads = {sorted(_blind_names)}",
      anchor=True)

# ------------------------------------------------------------------
# the family and the cache (the committed enumerator)
# ------------------------------------------------------------------
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
print(f"\n  family depth CAP = {CAP}: {len(FAM)} histories, census by "
      f"depth = {census}")
print(f"  TRANSITIONS GATED: every cached transition out of EVERY one "
      f"of these histories — i.e. into depth {CAP + 1}.  No silent cap.")
check("N0(f) CENSUS ANCHOR: the committed layer's own history census "
      "[1, 6, 32, 176, 976, 5280, 27904] (d44a / the D61 round-1 "
      "review's independent reproduction), total 34,375 at depth 6",
      census[:7] == [1, 6, 32, 176, 976, 5280, 27904][:CAP + 1]
      and (CAP != 6 or len(FAM) == 34375),
      f"census = {census}, histories = {len(FAM)}", anchor=True)

# ------------------------------------------------------------------
# The ABSTRACT transition system (d44a CG3a's BFS), computed FIRST so
# that T1's closure gate has a depth-independent target.  Its own gate
# prints below as T5.
# ------------------------------------------------------------------
SROOT = canon_sigma(())
REP = {SROOT: ()}
bfs = [SROOT]
n_exp = n_edge = 0
bfs_keys = set()
bfs_bad = 0
while bfs:
    s = bfs.pop(0)
    hk = REP[s]
    n_exp += 1
    for e, q in cands_of(hk):
        n_edge += 1
        sb, eb = canon_pair(hk, e)
        bfs_keys.add((sb, eb))
        pred, row = TABLE(sb, eb)
        s2 = canon_sigma(hk + (e,))
        if pred != s2:
            bfs_bad += 1
        if s2 not in REP:
            REP[s2] = hk + (e,)
            bfs.append(s2)
REACH = set(REP)

# ==================================================================
#  T1 — the table against the layer, at every cached transition
# ==================================================================
print(f"\n[T1 — TABLE(sigma(h), renamed e) vs the layer's sigma(h+e), "
      f"every cached transition into depth {CAP + 1}]")
mism = []
n_mism = 0
rowcount = defaultdict(int)
rowmiss = defaultdict(int)
KEYS = {}
KEYROW = {}
ntr = 0
states = set()
succ_states = set()
compsbad = 0
holdnone_bad = 0
for h in FAM:
    hold, live, comps, refs, sup = sigma_raw(h)
    states.add(canon_sigma(h))
    # Row 0 (O3): comps is a function of live, at EVERY state
    if (tuple(sorted(comps, key=repr))
            != tuple(sorted(comps_of_live(live), key=repr))):
        compsbad += 1
    # (5e), the premise of O1: at most one actor's token is dropped
    if sum(1 for a in AB if hold[a] is None) > 1:
        holdnone_bad += 1
    for e, q in CACHE[h]:
        ntr += 1
        sb, eb = canon_pair(h, e)
        pred, row = TABLE(sb, eb)
        act = canon_sigma(h + (e,))
        succ_states.add(act)
        rowcount[row] += 1
        KEYS[(sb, eb)] = act
        KEYROW[(sb, eb)] = row
        if pred != act:
            n_mism += 1
            rowmiss[row] += 1
            if len(mism) < 3:
                mism.append((h, e, sb, eb, pred, act))
for m in mism:
    print("  [T1 COUNTEREXAMPLE — (H2) FALSIFIED AT THIS ROW]")
    for lab, z in zip(("history", "event", "sigma(h)", "renamed e",
                       "TABLE says", "layer says"), m):
        print(f"      {lab}: {z}")
check(f"T1(a) THE TABLE REPRODUCES THE LAYER: at every one of the "
      f"{ntr} cached transitions into depth {CAP + 1}, the row's "
      "prediction from (sigma(h), renamed e) ALONE equals the "
      "committed canon_sigma(h + [e]) — string-identical "
      "serialisation.  The mismatch COUNT is total (round-1 MINOR 1: "
      "only the printed examples are capped at three)",
      n_mism == 0, f"transitions = {ntr}, mismatches = {n_mism}, "
      f"per-row mismatches = {dict(rowmiss) or 0}")
check("T1(b) THE ABSTRACT TRANSITION SYSTEM, anchored to d44a's "
      "committed numbers: the distinct (sigma, renamed event) keys "
      "number exactly 176 (d44a CG3a's traversed-edge count; CG2's "
      "160 cached keys + CG7c's 16 depth-6->7 keys) and the sigma "
      "states exactly 36 (d44a CG1/CG3a)",
      (len(KEYS) == 176 and len(states) == 36) if CAP == 6 else
      (len(KEYS) > 0 and len(states) > 0),
      f"keys = {len(KEYS)}, states = {len(states)}"
      + ("" if CAP == 6 else "  [NON-DEFAULT DEPTH: anchors apply at "
                             "CAP = 6 only]"), anchor=(CAP == 6))
check("T1(c) CLOSURE: no cached transition leaves the BFS-reachable "
      "sigma set — every parent state AND every successor state of "
      "every cached transition is one of the abstract system's "
      "reachable states (d44a CG3a's 'reachable == cache-realized', "
      "re-gated depth-independently against the BFS below)",
      succ_states <= REACH and states <= REACH and len(succ_states) > 0,
      f"reachable = {len(REACH)}, parent states = {len(states)}, "
      f"successor states = {len(succ_states)}, escapes = "
      f"{len((succ_states | states) - REACH)}")
check("T1(d) ROW 0 (obligation O3): comps is a FUNCTION OF live at "
      "EVERY state — the layer's components()/edges()/incomparable() "
      "output equals the Lemma-7b-driven reconstruction (same base + "
      "opposite bits, no poset test), so the table never has to "
      "transport a poset",
      compsbad == 0, f"states checked = {len(FAM)}, "
      f"reconstruction failures = {compsbad}")
# W-blindness: a corollary of the rows (the minted name is abstracted)
wgroups = defaultdict(set)
for (sb, eb), tgt in KEYS.items():
    e = ast.literal_eval(eb)
    key2 = (sb, e[:3]) if e[0] == 'r' else (sb, eb)
    wgroups[key2].add(tgt)
wbad = sum(1 for v in wgroups.values() if len(v) > 1)
narb_w = sum(1 for k in wgroups
             if isinstance(k[1], tuple) and k[1] and k[1][0] == 'r')
check("T1(e) [COROLLARY OF T1(a) — round-1 MAJOR 1(a): TABLE never "
      "reads e[3], so once T1(a) passes this CANNOT fail; printed as "
      "a reporting line in D58-A3 style, worth seeing and not worth "
      "counting as independent evidence]: the successor sigma does "
      "not depend on the WINNER key W — keys differing only in wkey "
      "have the same layer target (the minted name vname(b, W, x) is "
      "abstracted to one fresh token, so arbitration's winner is "
      "invisible to sigma)",
      wbad == 0 and narb_w > 0,
      f"arb (sigma, ckey)-groups = {narb_w}, groups with split "
      f"targets = {wbad}")
print(f"  [t = {time.time() - T0:.1f}s]")

# ==================================================================
#  T4 — row coverage (done here: it reads T1's tallies)
# ==================================================================
print("\n[T4 — row coverage: every transition matched to exactly one "
      "row of the note's table]")
def row_of_class(sig, ev):
    """The INDEPENDENT row classifier (round-1 MAJOR 1(c) repair):
    derives the row from the event class alone — tag, base-in-refs,
    |proposers(ckey)| — through its own parse and its own tests, so
    it CAN disagree with the row label TABLE returns (the old
    `unassigned` counter was ntr - ntr, a tautology, because TABLE
    returns a row on every path)."""
    _sf = dict(parse_sigma(sig)[3])
    e = ast.literal_eval(ev)
    if e[0] == 'n':
        return 'R1-idle'
    if e[0] == 'p':
        return ('R2-propose-held' if e[2] in _sf
                else "R2'-propose-dropped-base")
    return ('R3-self-arb' if len({t[0] for t in e[2]}) == 1
            else 'R4-pair-arb')


rowdisagree = sum(1 for k, r in KEYROW.items()
                  if row_of_class(*k) != r)
check("T4(a) ROW COVERAGE, INDEPENDENTLY CLASSIFIED (round-1 MAJOR "
      "1(c): the first draft's `unassigned` counter could not fire): "
      "an independent classifier re-derives each cached transition's "
      "row from (event tag, base-in-refs, |proposers(ckey)|) through "
      "its own parse, and agrees with TABLE's row label at every "
      "key; the five rows partition the classes and none is empty",
      rowdisagree == 0 and all(rowcount[r] > 0 for r in ROWS)
      and set(rowcount) == set(ROWS),
      f"keys re-classified = {len(KEYROW)}, disagreements = "
      f"{rowdisagree}; per-row counts = "
      f"{ {r: rowcount[r] for r in ROWS} }")
_n_r2p = rowcount["R2'-propose-dropped-base"]
if CAP == 6:
    check("T4(b) ROW CENSUS ANCHORS (independent numbers this receipt "
          "did not choose): R1 = 68,750 = 2 x 34,375 (an idle by each "
          "actor at every history — the D61 round-1 review's 68,750 "
          "(h, actor) pairs); R2' = 9,656 = exactly the review's "
          "count of cone-extra propose options caused by MISSED "
          "SUPERSESSION (the dropped-base proposes ARE that excess); "
          "R3 + R4 = 44,356 = the review's admissible-arb census",
          rowcount['R1-idle'] == 68750 and _n_r2p == 9656
          and rowcount['R3-self-arb'] + rowcount['R4-pair-arb'] == 44356,
          f"R1 = {rowcount['R1-idle']}, R2' = {_n_r2p}, "
          f"R3+R4 = {rowcount['R3-self-arb'] + rowcount['R4-pair-arb']}")
else:
    print("  [T4(b) row-census anchors apply at CAP = 6 only — SKIPPED "
          f"at CAP = {CAP}; counts printed above]")

# ------------------------------------------------------------------
# T4(c) — the ROW PRECONDITIONS, at every instance.  These are the
# claims the note's rows make about what an admissible event can BE;
# each is read off admissible()/prop_options_in_view()/
# arb_components_in_view() plus Lemma 5.  Gated per row.
# ------------------------------------------------------------------
pre_bad = defaultdict(int)
pre_n = defaultdict(int)
sub = defaultdict(int)
tok_bad = 0
twolive_samebit = 0
for h in FAM:
    _ho, _li, _co, _rf, _su = sigma_raw(h)
    _by = defaultdict(list)
    for _t in _li:
        _by[_t[1]].append(_t)
    if any(len(v) == 2 and v[0][2] == v[1][2] for v in _by.values()):
        twolive_samebit += 1
    for e, q in CACHE[h]:
        sb, eb = canon_pair(h, e)
        hold, live, comps, supf = parse_sigma(sb)
        ee = ast.literal_eval(eb)
        x = ee[1]
        y = 'B' if x == 'A' else 'A'
        refs = set(supf)
        livex = [t for t in live if t[0] == x]
        if ee[0] == 'p':
            b = ee[2]
            if b in refs:
                pre_n['R2'] += 1
                # 5a + prop_options_in_view: the base IS the actor's
                # own alive token, and it had no live proposal (5b)
                if not (b == hold[x] and not livex):
                    pre_bad['R2'] += 1
            else:
                pre_n["R2'"] += 1
                # O1: dropped base => hold is None, no live own
                # proposal, and the token is canon_pair's 100
                if not (hold[x] is None and not livex and b == 100):
                    pre_bad["R2'"] += 1
        elif ee[0] == 'r':
            ck, wk = tuple(ee[2]), tuple(ee[3])
            base = ck[0][1]
            props = {t[0] for t in ck}
            common = (all(t[1] == base for t in ck)
                      and set(wk) <= set(ck)
                      and all(t in live for t in ck)
                      and base in refs)
            if len(props) == 1:
                pre_n['R3'] += 1
                # the note's R3 sub-cases, tallied for non-vacuity
                sub['R3 x self-arbs its HELD token' if hold[x] == base
                    else 'R3 x self-arbs its DROPPED token (after R2\')'] += 1
                if hold[y] == base:
                    sub['R3 opponent token DROPPED by the arb '
                        '(shared base) — invisible supersession'] += 1
                    if any(t[0] == y and t[1] == base for t in live):
                        sub['R3 ... AND the opponent is left with a live '
                            'proposal STRANDED on the superseded base'] += 1
                elif hold[y] is None:
                    sub['R3 opponent token already dropped'] += 1
                else:
                    sub['R3 opponent wholly untouched'] += 1
                # Lemma 5's self case: a SINGLETON component, the
                # initiator's own live proposal, on X_x
                if not (common and len(ck) == 1 and props == {x}
                        and (hold[x] == base
                             or (hold[x] is None and supf[base]))):
                    pre_bad['R3'] += 1
            else:
                pre_n['R4'] += 1
                # Lemma 5's pair case: both actors' live proposals on
                # one base, which is BOTH actors' non-superseded token
                if not (common and len(ck) == 2 and props == set(AB)
                        and hold['A'] == hold['B'] == base
                        and supf[base] is False):
                    pre_bad['R4'] += 1
        else:
            pre_n['R1'] += 1
        # no renamed event may mention a token outside refs u {100},
        # and only a propose may mention 100 (arbs carry no extras)
        toks = ([ee[2]] if ee[0] == 'p' else
                [t[1] for t in tuple(ee[2]) + tuple(ee[3])]
                if ee[0] == 'r' else [])
        if any(t not in refs and t != 100 for t in toks) or (
                ee[0] == 'r' and any(t == 100 for t in toks)):
            tok_bad += 1
check("T4(c) ROW PRECONDITIONS at every instance: R2's base is the "
      "actor's own held token with no prior live proposal (5a + 5b); "
      "R2''s base is OUTSIDE refs with hold = None and no live own "
      "proposal, and canon_pair renames it to the single extra token "
      "100 (O1); R3's ckey is a SINGLETON of the initiator's own live "
      "proposal on its token; R4's ckey is both actors' live "
      "proposals on one base that is both actors' NON-superseded "
      "token (Lemma 5's four cases, as preconditions)",
      not pre_bad, f"instances per row = {dict(pre_n)}, precondition "
      f"violations = {dict(pre_bad) or 0}")
_SUBS = ['R3 x self-arbs its HELD token',
         "R3 x self-arbs its DROPPED token (after R2')",
         'R3 opponent token DROPPED by the arb (shared base) — '
         'invisible supersession',
         'R3 ... AND the opponent is left with a live proposal STRANDED '
         'on the superseded base',
         'R3 opponent token already dropped',
         'R3 opponent wholly untouched']
check("T4(e) NON-VACUITY OF THE ROWS' SUB-CASES: every branch the "
      "note's row R3 distinguishes actually OCCURS in the family — "
      "including the two that carry the whole delicacy (the "
      "opponent's token dropped by an arb it cannot see, and the "
      "opponent left with a live proposal stranded on a base that is "
      "now superseded) — and states carrying two live proposals on "
      "ONE base with the SAME bit (two singleton components, no "
      "edge) exist too, so Row 0's same-bit branch is not vacuous",
      all(sub[k] > 0 for k in _SUBS) and twolive_samebit > 0,
      f"sub-case counts = { {k: sub[k] for k in _SUBS} }; states with "
      f"two same-bit live proposals on one base = {twolive_samebit}")
check("T4(d) TOKEN DISCIPLINE: no renamed event mentions a token "
      "outside refs u {100}, and NO ARB ever carries the extra token "
      "— an arb's base is live-carrying, hence in refs, so the "
      "dropped-base subtlety is confined to row R2'",
      tok_bad == 0, f"violations = {tok_bad}")

# ==================================================================
#  T3 — obligation O1 isolated: the propose-on-a-dropped-base row
# ==================================================================
print("\n[T3 — O1: the dropped-base row, isolated]")
o1_n = 0
o1_bad = 0
o1_cls = defaultdict(set)
for h in FAM:
    hold, live, comps, refs, sup = sigma_raw(h)
    for e, q in CACHE[h]:
        if e[0] != 'p':
            continue
        if e[2] in refs:
            continue
        o1_n += 1
        x = e[1]
        y = 'B' if x == 'A' else 'A'
        Xx = own_alive(h, x)
        # the four facts the S3(b)/O1 argument asserts about the token
        if not (e[2] == Xx                      # 5a: the propose is on X_x
                and hold[x] is None             # X_x is full-superseded
                and Xx in sup                   # ... explicitly
                and Xx not in refs              # 5e + 5b: not referenced
                and hold[y] != Xx
                and all(t[1] != Xx for t in live)):
            o1_bad += 1
        sb, eb = canon_pair(h, e)
        o1_cls[(sb, eb)].add(canon_sigma(h + (e,)))
o1_split = sum(1 for v in o1_cls.values() if len(v) > 1)
check("T3(a) O1's FORCEDNESS, at every instance: on a "
      "propose-on-a-dropped-base the discarded token is exactly X_x = "
      "own_alive(h, x) (5a), it IS in the full-view superseded set "
      "(hence hold[x] = None), and it is NOT in refs — the opponent "
      "does not hold it (5e) and no live proposal sits on it (5b + "
      "5d).  So sigma(h) determines everything about it except its "
      "name, which the renamed event supplies",
      o1_bad == 0 and o1_n > 0,
      f"dropped-base proposes = {o1_n}, violations = {o1_bad}")
check("T3(b) [COROLLARY OF T1(a) — round-1 MAJOR 1(b): each class's "
      "successors all equal TABLE(sb, eb), a single value, so once "
      "T1(a) passes this cannot fail; printed as a reporting line, "
      "not counted as independent evidence]: within each (sigma, "
      "renamed e) class of dropped-base proposes, the successor "
      "sigmas are pairwise IDENTICAL",
      o1_split == 0 and len(o1_cls) > 0,
      f"classes = {len(o1_cls)}, splitting classes = {o1_split}")
check("T3(c) O1's PREMISE — invariant (5e) — at every state: at most "
      "one actor's token is full-view superseded, i.e. at most one "
      "hold[a] is None.  If two were, two distinct dropped bases "
      "could be mentioned and the canonical renaming would have a "
      "genuine choice (the adopted note's §8 GAP 2)",
      holdnone_bad == 0, f"states = {len(FAM)}, violations = "
      f"{holdnone_bad}")
print(f"  [t = {time.time() - T0:.1f}s]")

# ==================================================================
#  T2 — obligation O2: fresh-version-name non-collision
# ==================================================================
print("\n[T2 — O2: the minted version name is always fresh]")


def minted(e):
    return vname(next(iter(e[2]))[1], e[3], e[1])


def bases_present(h):
    """every base token existing in h: V0 plus every minted version
    (candidates_for's own base set: {V0} u {vname(...) : arbs})."""
    return {V0} | {minted(e) for e in h if e[0] == 'r'}


coll = 0
narb = 0
for h in FAM:
    pres = bases_present(h)
    for e, q in CACHE[h]:
        if e[0] != 'r':
            continue
        narb += 1
        if minted(e) in pres:
            coll += 1
check("T2(a) THE COLLISION CENSUS, re-run: over every admissible arb "
      "at every cached transition, the minted vname(b, W, x) is NOT a "
      "base already present in h (present = V0 u the versions minted "
      "by h's arbs — candidates_for's own base set).  Anchored to the "
      "D61 round-1 review's census: 44,356 admissible arbs, 0 "
      "collisions",
      coll == 0 and (narb == 44356 if CAP == 6 else narb > 0),
      f"admissible arbs = {narb}, collisions = {coll}")

# T2(b) — the INADMISSIBILITY PREMISE, adversarially.  For every
# history and every arb event drawn from the layer's own outputs
# (the arbs of h, and the arb candidates at every prefix of h — i.e.
# events the layer itself once admitted), if that event's minted name
# is ALREADY present in h, the layer must refuse it NOW.
adv_pool = adv_fired = adv_admitted = 0
adv_kinds = defaultdict(int)
for h in FAM:
    pres = bases_present(h)
    pool = {e for e in h if e[0] == 'r'}
    for k in range(len(h) + 1):
        pool |= {e for e, q in CACHE[h[:k]] if e[0] == 'r'}
    for e in pool:
        adv_pool += 1
        if minted(e) not in pres:
            continue
        adv_fired += 1
        ok, q = adm(list(h), e)
        adv_kinds[('in h' if e in h else 'NOT in h — a DIFFERENT event '
                   'with the SAME minted name',
                   'self' if len({t[0] for t in e[2]}) == 1 else 'pair')] += 1
        if ok:
            adv_admitted += 1
check("T2(b) O2's ARGUMENT ON A REACHABILITY-RESTRICTED SURFACE "
      "(round-1 MINOR 7: this pool is arbs of h plus arb CANDIDATES "
      "at every prefix — all layer-minted; the round built the truly "
      "adversarial surface, every well-formed arb over all uttered "
      "triples, 69,652 colliding candidates, and confirmed 0 admitted "
      "at 2.3x this surface): every arb event whose minted name is "
      "ALREADY present in h is REFUSED by the committed admissible() "
      "at h — including the events that are not in h at all.  This is "
      "the premise of the note's proof (a collision forces an earlier "
      "arb by x on the same base b; that arb lies in the candidate's "
      "view — the full view for a pair-arb, cone_x for a self-arb by "
      "Lemma 1(c) and the proposer test — so b is superseded there "
      "and arb_components_in_view skips it)",
      adv_admitted == 0 and adv_fired > 0,
      f"pool = {adv_pool}, colliding-name candidates = {adv_fired}, "
      f"ADMITTED (violations) = {adv_admitted}; by kind = "
      f"{dict(adv_kinds)}")

# T2(c) — the named witness: two DISTINCT admissible arbs at one
# history mint the SAME version name; once either fires the other is
# refused.  (The pin's "constructed adversarially if reachable".)
tA, tB = ('A', V0, 0), ('B', V0, 1)
pA0, pB1 = ('p', 'A', V0, 0), ('p', 'B', V0, 1)
SELFA = ('r', 'A', frozenset({tA}), frozenset({tA}))
PAIR = ('r', 'A', frozenset({tA, tB}), frozenset({tA}))
W = [pA0, pB1]
same_name = vname(V0, SELFA[3], 'A') == vname(V0, PAIR[3], 'A')
both_ok = adm(W, SELFA)[0] and adm(W, PAIR)[0]
after_pair = adm(W + [PAIR], SELFA)[0]
after_self = adm([pA0, SELFA], SELFA)[0]
after_self2 = adm([pA0, SELFA], PAIR)[0]
check("T2(c) THE NAMED WITNESS (O2 is not vacuous): at h = [pA(v0,0), "
      "pB(v0,1)] the self-arb and the pair-arb are BOTH admissible "
      "and mint the SAME name ('v', v0, (0,), ('A',), 'A') — vname "
      "keys on the WINNER, not the ckey, so distinct events can "
      "collide.  Once either fires, the other is REFUSED: the base is "
      "superseded in the survivor's view.  So the collision is "
      "excluded by admissibility, not by luck",
      same_name and both_ok and not after_pair and not after_self
      and not after_self2,
      f"same minted name = {same_name}; both admissible at h = "
      f"{both_ok}; selfA after PAIR = {after_pair}; selfA after selfA "
      f"= {after_self}; PAIR after selfA = {after_self2}")
print(f"  [t = {time.time() - T0:.1f}s]")

# ==================================================================
#  T5 — coverage of the ABSTRACT transition system (d44a CG3a's BFS)
# ==================================================================
print("\n[T5 — coverage: the table on EVERY abstract transition key]")
check("T5 THE FRONTIER-EXHAUSTED BFS on sigma-space (d44a CG3a, "
      "re-run): all 36 reachable states EXPANDED, 176 traversed "
      "edges, and the TABLE predicts the layer's successor on every "
      "one of them; every key the cached sweep saw is one of them "
      "(with equality at the anchored depth).  STATED HONESTLY: the "
      "BFS uses one representative per class, which is LICENSED BY "
      "the rows — this is coverage evidence, NOT an independent "
      "proof of (H2)",
      n_exp == 36 and n_edge == 176 and bfs_bad == 0
      and set(KEYS) <= bfs_keys
      and (bfs_keys == set(KEYS) if CAP == 6 else True),
      f"expanded = {n_exp}, edges = {n_edge}, abstract keys = "
      f"{len(bfs_keys)}, table mismatches = {bfs_bad}, cached keys "
      f"contained = {set(KEYS) <= bfs_keys}, key sets coincide = "
      f"{bfs_keys == set(KEYS)}")
check("T5(b) THE LAYER'S OWN SANITY COUNTERS (d44a's sigma port, "
      "carried through this receipt's whole sweep): alive-singleton, "
      "non-superseded-holdings, live-on-X and conflicting-pair-"
      "comparability violations all zero — the invariants the rows "
      "consume, as the committed port itself counts them",
      all(v == 0 for v in SG_VIOL.values()), f"SG_VIOL = {dict(SG_VIOL)}")

# ==================================================================
print("\n[VERDICT]")
ok = (n_mism == 0 and not rowmiss and compsbad == 0
      and holdnone_bad == 0
      and rowdisagree == 0 and not pre_bad and tok_bad == 0
      and all(sub[k] > 0 for k in _SUBS) and twolive_samebit > 0
      and o1_bad == 0 and o1_split == 0 and coll == 0
      and adv_admitted == 0 and adv_fired > 0 and bfs_bad == 0
      and wbad == 0 and same_name and both_ok and not after_pair)
anchored = (CAP == 6 and len(KEYS) == 176 and len(states) == 36
            and n_edge == 176 and n_exp == 36 and narb == 44356)
if ok and anchored:
    print("  (H2) IS A THEOREM at two-actor delivery-free d42a scope:")
    print("  sigma(h + [e]) is a function of (sigma(h), renamed e) at")
    print("  EVERY depth.  Carried by note-d62-h2-update-table.md's")
    print("  five rows — each a reading of the committed layer plus")
    print("  D61's Lemma 5 invariants — with all THREE obligations")
    print("  discharged as proofs: O1 (the dropped-base token is")
    print("  forced by 5e + 5b, its superseded mark computed not")
    print("  read), O2 (a minted vname can never collide: the")
    print("  collision forces an earlier arb by the same actor on the")
    print("  same base, which lies in the candidate's own view and")
    print("  supersedes it there, so the arb is inadmissible), O3")
    print("  (comps is a function of live by Lemma 7b + 5b, so no")
    print("  poset is transported).  The gates above are EVIDENCE for")
    print("  the rows and were never premises of them.")
    print("  CONSEQUENCES (pin §3, and no more than these):")
    print("  - (H0) discharged (D61), (H1) THEOREM (D61), (H2) THEOREM")
    print("    (here) => D44a's closure theorem is UNCONDITIONAL at")
    print("    two-actor delivery-free d42a scope.")
    print("  - The 36-state closure, the six-state chain and the")
    print("    Perron package hold AT EVERY DEPTH there.")
    print("  - RESIDUE 1 IS CLOSED AT THAT SCOPE; D49's root-free")
    print("    completion is unconditional at every depth there —")
    print("    still within the stationary form (D50: the form")
    print("    remains a choice), still DELIVERY-FREE (transport")
    print("    untouched).  The D61 quotation embargo lifts.")
    print("  - Paper 30/32 and book updates land AFTER this unit's")
    print("    hostile round, per discipline.")
    print("  RESIDUES: Lean-grade mechanization of the induction")
    print("  (unchanged from D61); three actors OUT OF SCOPE (the")
    print("  wall is Lemma 2's proposer test); transport untouched.")
elif ok and not anchored:
    print("  every substantive gate passed, but the run was NOT at the")
    print("  anchored depth (CAP != 6) or an anchor moved: no theorem")
    print("  claim is made from this run.  Re-run with no argument.")
else:
    print("  A GATE FAILED — the failure IS the deliverable (pin §4).")
    print("  If T1 printed a counterexample, (H2) is FALSE as stated")
    print("  at that row and D44a's closure theorem does not close;")
    print("  if an obligation's gate failed, the unit ships '(H2)")
    print("  conditional on' that named sub-obligation.  Nothing")
    print("  above may be quoted as closure.")
print(f"\n[d62] {PASS} PASS / {FAIL} FAIL"
      + (f"  ({ANCHOR_FAIL} anchor failures)" if ANCHOR_FAIL else "")
      + f"  [family depth {CAP}, transitions into depth {CAP + 1}, "
      f"runtime {time.time() - T0:.1f}s]")
sys.exit(1 if ANCHOR_FAIL else 0)
