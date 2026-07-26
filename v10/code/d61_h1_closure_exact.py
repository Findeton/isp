#!/usr/bin/env python3
"""
d61_h1_closure_exact.py — v10 D61: closing (H1).
Pin: note-d61-h1-closure-pin.md §1-§3 + the §4 first-run amendment
(run 1's hand-rolled state was coarser than sigma; and any cache-gated
machine leaves the depth gap — the theorem is carried by the probe's
prose-over-code proof, this receipt gates its case claims, code-facts,
and conclusion) + the §5 round-1 amendment (headline restated: (H1) is
a THEOREM; D44a remains CONDITIONAL on (H2); round-1 repairs: 5c/5d
gates, ==36 + window-spectrum anchor, exit protocol, N-numbering).
Exit 1 only on anchor breakage (N0/N1); substantive gate failures are
the deliverable and exit 0.
NOTE (round-1 MINOR 1): the pin §1's N-programme (N1 invariants, N2
determinism, N3 BFS closure, N4 per-transition step, N5 menu law, N6
quarter law) was DELETED by the §4 amendment; this receipt's N-numbers
are its own (N0 anchors, N1 code-facts, N2 invariants, N3 cases, N4
conclusion, N5 quarter law) and do NOT correspond to the pin §1 list.
"""
import sys
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

print("[D61 — closing (H1): the case-claim battery + the conclusion]")
print("  banner: the THEOREM is carried by the adopted proof note")
print("  (d60p §3-§7, prose-over-code); this receipt gates every case")
print("  claim at every cached instance, the code-facts the proof")
print("  reads, and the conclusion.  TWO-ACTOR d42a ONLY.")

_s = open('v10/code/d42b3_placement_exact.py').read()
ns = {}
exec(_s[:_s.index('print("[d42b3')], ns)
cf, ep, V0, vname = (ns['candidates_for'], ns['event_poset'],
                     ns['V0'], ns['vname'])
AB = ('A', 'B')
_D44A = 'v10/code/d44a_closure_theorem_exact.py'
_ds = open(_D44A).read()
_blk1 = _ds[_ds.index("SG_VIOL = {'alive'"):_ds.index("\nSIG = {tuple(h)")]
_blk2 = _ds[_ds.index("def _rename_event(e, m2):"):
            _ds.index("\ngroups = defaultdict(list)")]
ns['AB'] = AB
ns['permutations'] = permutations
ns['defaultdict'] = defaultdict
def cands_of(hk):
    return cf(list(hk), AB)
ns['cands_of'] = cands_of
exec(compile(_blk1, 'd44a_sigma_port', 'exec'), ns)
exec(compile(_blk2, 'd44a_menu_port', 'exec'), ns)
canon_sigma, canon_menu = ns['canon_sigma'], ns['canon_menu']
check("N0 anchors: committed d42b3 layer + sigma/canon_menu extracted "
      "VERBATIM from committed d44a (the probe's own text-slice port; "
      "no abstraction of this receipt's own) — the slices carry the "
      "expected structures, not merely callables (round-1 MINOR 2)",
      callable(canon_sigma) and callable(canon_menu)
      and "def canon_sigma" in _blk1 and "def sigma_raw" in _blk1
      and "def canon_menu" in _blk2 and "_rename_event" in _blk2,
      "single sources; slice contents asserted", anchor=True)

# code-facts the proof reads (Lemma 1): asserted against the source
src = _s
cfact = ("def regs_of(op):" in src
         and "if op[0] in ('p', 'n'): return frozenset([op[1]])" in src
         and "props = {t[0] for t in op[2]}" in src
         and "base = next(iter(op[2]))[1]" in src
         and "return frozenset(props | {vname(base, op[3], op[1])})"
         in src)
check("N1 CODE-FACTS (Lemma 1's register geometry, asserted against "
      "the committed source, INCLUDING the version-register line — "
      "round-1 MINOR 2): regs_of gives {actor} for p/n and {proposers} "
      "u {fresh vname} for r — the registers are ACTOR NAMES plus "
      "arbitrator-owned version names",
      cfact, "source assertions hold", anchor=True)

CAP = 6
FAM = [()]
fr = [()]
CACHE = {}
while fr:
    h = fr.pop()
    CACHE[h] = cf(list(h), AB)
    if len(h) >= CAP:
        continue
    for e, q in CACHE[h]:
        h2 = h + (e,)
        FAM.append(h2)
        fr.append(h2)
print(f"  exhaustive family to depth {CAP}: {len(FAM)} histories")


def cone(h, a):
    p = ep(list(h) + [('n', a)])
    return frozenset(p[len(h)])


def state_of(h):
    """Layer-computed invariant data (as in run 1's N1, which passed)."""
    sup_full = set()
    for e in h:
        if e[0] == 'r':
            sup_full.add(next(iter(e[2]))[1])
    st = {}
    for a in AB:
        ca = cone(h, a)
        holds = {V0}
        supc = set()
        for i in sorted(ca):
            e = h[i]
            if e[0] == 'r':
                b = next(iter(e[2]))[1]
                supc.add(b)
                if a in {t[0] for t in e[2]}:
                    holds.add(vname(b, e[3], e[1]))
        alive = holds - supc
        live = [h[i] for i in sorted(ca)
                if h[i][0] == 'p' and h[i][1] == a
                and not any(h[j][0] == 'r' and j in ca
                            and (h[i][1], h[i][2], h[i][3]) in h[j][2]
                            for j in ca)]
        st[a] = (alive, live)
    return st, sup_full


# ------- N2: the invariants (5a/5b/5c/5d/5e), all instances ---------
# (round-1 MAJOR 1: 5c and 5d — the two invariants Lemma 5's step
# consumes BY NAME — were gated nowhere; they are gated here, 5d
# including the same-bit case the probe's S2.5 cannot see, and 5c in
# order form, menu form, and its first-self-arb-on-the-shared-base
# step.)
inv_bad = c5c_bad = c5d_bad = first_bad = 0
c5c_hist = first_n = 0
for h in FAM:
    st, sup_full = state_of(h)
    for a in AB:
        alive, live = st[a]
        if len(alive) != 1 or len(live) > 1:
            inv_bad += 1
        elif live and live[0][2] != next(iter(alive)):
            inv_bad += 1
    if sum(1 for a in AB if next(iter(st[a][0])) in sup_full) > 1:
        inv_bad += 1
    selfarbs = [j for j, e in enumerate(h)
                if e[0] == 'r' and len({t[0] for t in e[2]}) == 1]
    pairarbs = [j for j, e in enumerate(h)
                if e[0] == 'r' and len({t[0] for t in e[2]}) == 2]
    # 5c order form: no pair-arb positioned after a self-arb
    if selfarbs and pairarbs and max(pairarbs) > min(selfarbs):
        c5c_bad += 1
    # 5c menu form: a post-self-arb history offers no pair-arb
    if selfarbs:
        c5c_hist += 1
        if any(e[0] == 'r' and len({t[0] for t in e[2]}) == 2
               for e, q in CACHE[h]):
            c5c_bad += 1
    else:
        # 5c's missing step (round-1 MAJOR 1): the FIRST self-arb of
        # any history sits on the shared base X_A = X_B
        XA, XB = (next(iter(st[a][0])) for a in AB)
        for e, q in CACHE[h]:
            if e[0] == 'r' and len({t[0] for t in e[2]}) == 1:
                first_n += 1
                if not (next(iter(e[2]))[1] == XA == XB):
                    first_bad += 1
    # 5d full strength: no opponent proposal live in cone_a on X_a,
    # EITHER bit
    for a in AB:
        ca = cone(h, a)
        Xa = next(iter(st[a][0]))
        resolved = {t for j in ca if h[j][0] == 'r' for t in h[j][2]}
        for j in ca:
            e = h[j]
            if (e[0] == 'p' and e[1] != a and e[2] == Xa
                    and (e[1], e[2], e[3]) not in resolved):
                c5d_bad += 1
check("N2 LEMMA 5's INVARIANTS (5a alive singleton; 5b <= 1 live, on "
      "X_a; 5e <= 1 full-view-superseded X) at EVERY history, "
      "layer-computed: zero violations",
      inv_bad == 0, f"histories = {len(FAM)}, violations = {inv_bad}")
check("N2(c) INVARIANT 5c at every history (round-1 MAJOR 1): no "
      "pair-arb after a self-arb — order form AND menu form; and the "
      "FIRST self-arb of any history sits on the shared base "
      "X_A = X_B (the induction's previously-unwritten step)",
      c5c_bad == 0 and first_bad == 0 and c5c_hist > 0 and first_n > 0,
      f"post-self-arb histories = {c5c_hist}, first-self-arb "
      f"candidates = {first_n}, violations = {c5c_bad + first_bad}")
check("N2(d) INVARIANT 5d at every history, FULL STRENGTH incl. the "
      "same-bit case (round-1 MAJOR 1): no opponent proposal live in "
      "cone_a on X_a, either bit",
      c5d_bad == 0, f"violations = {c5d_bad}")

# ---------------- N3: the CASE-CLAIM battery ------------------------
print("\n[N3 — Lemma 5's step cases: PRECONDITIONS and EFFECTS, at "
      "every cached transition (parents to depth <= 5)]")
c_self = c_pair = c_prop = 0
b_self = b_pair = b_prop = 0
b_self_eff = b_pair_eff = b_prop_eff = 0
for h in FAM:
    if len(h) >= CAP:
        continue
    st, _ = state_of(h)
    for e, q in CACHE[h]:
        st2, _ = state_of(h + (e,))
        if e[0] == 'p':
            c_prop += 1
            a = e[1]
            alive, live = st[a]
            if e[2] != next(iter(alive)) or live:
                b_prop += 1
            # effects: both alive unchanged; a gains exactly one live
            # on X_a; the opponent's live unchanged
            y = 'B' if a == 'A' else 'A'
            if not (st2[a][0] == st[a][0] and st2[y] == st[y]
                    and len(st2[a][1]) == 1
                    and st2[a][1][0][2] == e[2]):
                b_prop_eff += 1
        elif e[0] == 'r':
            actors_in = {t[0] for t in e[2]}
            base = next(iter(e[2]))[1]
            v = vname(base, e[3], e[1])
            if len(actors_in) == 1:
                c_self += 1
                a = e[1]
                if len(e[2]) != 1 or base != next(iter(st[a][0])):
                    b_self += 1
                # effects (round-1 MINOR 6 — the INVISIBLE
                # SUPERSESSION, the step's most delicate claim): x
                # advances to the fresh version with 0 live; the
                # OPPONENT's (alive, live) is UNCHANGED, and the arb
                # is NOT in the opponent's cone
                y = 'B' if a == 'A' else 'A'
                if not (st2[a][0] == {v} and st2[a][1] == []
                        and st2[y] == st[y]
                        and len(h) not in cone(h + (e,), y)):
                    b_self_eff += 1
            else:
                c_pair += 1
                if not all(base == next(iter(st[x][0])) for x in AB):
                    b_pair += 1
                # effects: BOTH actors advance to the same fresh
                # version, BOTH live proposals resolved
                if not all(st2[x][0] == {v} and st2[x][1] == []
                           for x in AB):
                    b_pair_eff += 1
check("N3(a) THE PROPOSE CASE, preconditions AND effects: every "
      "admissible propose is on the actor's own alive singleton X_a "
      "with no prior live proposal; after it, alive tokens unchanged, "
      "the actor holds exactly one live proposal on X_a, the opponent "
      "untouched — at every instance",
      c_prop > 0 and b_prop == 0 and b_prop_eff == 0,
      f"instances = {c_prop}, precondition violations = {b_prop}, "
      f"effect violations = {b_prop_eff}")
check("N3(b) THE SELF-ARB CASE, preconditions AND effects (round-1 "
      "MINOR 6): every admissible single-actor arb consumes a "
      "SINGLETON component on that actor's own X_a; after it, the "
      "actor advances to the fresh version with 0 live, and the "
      "OPPONENT's (alive, live) is UNCHANGED with the arb OUTSIDE its "
      "cone — the invisible supersession, gated as an effect",
      c_self > 0 and b_self == 0 and b_self_eff == 0,
      f"instances = {c_self}, precondition violations = {b_self}, "
      f"effect violations = {b_self_eff}")
check("N3(c) THE PAIR-ARB CASE, preconditions AND effects: every "
      "admissible two-actor arb sits on a base that is BOTH actors' "
      "alive singleton; after it, BOTH actors advance to the same "
      "fresh version and BOTH live proposals are resolved",
      c_pair > 0 and b_pair == 0 and b_pair_eff == 0,
      f"instances = {c_pair}, precondition violations = {b_pair}, "
      f"effect violations = {b_pair_eff}")
# round-1 MINOR 2: the old N3(d) counted non-p/r/n menu events, which
# candidates_for cannot construct — a theorem-pass.  The alphabet is a
# CODE-FACT, asserted against the source instead:
check("N3(d) CASE EXHAUSTIVENESS as a CODE-FACT (round-1 MINOR 2: the "
      "old counter could never fire): candidates_for constructs "
      "events only via ('n', a), ('p', ...) and ('r', ...) literals "
      "in the committed source",
      src.count("('n', a)") >= 1 and "('p'," in src and "('r'," in src
      and "('d'," not in src.split("def candidates_for")[1]
                             .split("\ndef ")[0]
      and "('m'," not in src.split("def candidates_for")[1]
                             .split("\ndef ")[0],
      "alphabet asserted against candidates_for's source")

# the dichotomy (Lemma 2), re-gated here at this receipt's own scope
tot = cone_n = full_n = third = 0
for h in FAM:
    if len(h) >= CAP:
        continue
    n = len(h)
    cones = {a: cone(h, a) for a in AB}
    fullset = frozenset(range(n))
    for e, q in CACHE[h]:
        p = ep(list(h) + [e])
        v = frozenset(p[n])
        tot += 1
        if v == cones[e[1]]:
            cone_n += 1
        elif v == fullset:
            full_n += 1
        else:
            third += 1
check("N3(e) THE DICHOTOMY (Lemma 2): every candidate's own view is "
      "the initiator's cone or the FULL view — no third case, at "
      "every instance",
      third == 0 and full_n > 0,
      f"candidates = {tot}: cone = {cone_n}, full = {full_n}, third = "
      f"{third}")

# ---------------- N4: the conclusion (H1) ---------------------------
print("\n[N4 — the conclusion: canon_menu is a function of canon_sigma]")
by_sig = {}
h1_bad = 0
sig_by_depth = defaultdict(set)
for h in FAM:
    sg = canon_sigma(h)
    cm = canon_menu(h)
    if sg in by_sig and by_sig[sg] != cm:
        h1_bad += 1
    by_sig[sg] = cm
    sig_by_depth[len(h)].add(sg)
# the cumulative window spectrum, gated against d44a's committed SG1
# anchor (round-1 MINOR 3: '>= 30' would let a coarsened sigma port
# pass silently; the anchor is EXACTLY 36 with spectrum [11, 19, 28,
# 32, 36] at depths <= 2..6)
_cum = set()
spectrum = []
for d in range(CAP + 1):
    _cum |= sig_by_depth[d]
    if d >= 2:
        spectrum.append(len(_cum))
check("N4 (H1)'s CONCLUSION at this receipt's scope: equal canonical "
      "sigma => IDENTICAL canonical menu (renamed event-multiset with "
      f"exact weights), over all {len(FAM)} histories — zero splits, "
      "with the sigma count gated EXACTLY 36 and the cumulative "
      "window spectrum gated against d44a's committed SG1 anchor "
      "(round-1 MINOR 3).  The probe gated the same over 930,631 "
      "histories at depth 8 [PROBE-CARRIED, re-verified independently "
      "by the round-1 review]",
      h1_bad == 0 and len(by_sig) == 36
      and spectrum == [11, 19, 28, 32, 36],
      f"sigma classes = {len(by_sig)}, splits = {h1_bad}, "
      f"window spectrum = {spectrum}")

# ---------------- N5: the quarter law per sigma class ---------------
qbad = 0
for h in FAM:
    per = defaultdict(lambda: Fr(0))
    for e, q in CACHE[h]:
        per[e[1]] += q
    for a, t in per.items():
        if t not in (Fr(1), Fr(5, 4)):
            qbad += 1
check("N5 the per-actor menu mass is in {1, 5/4} at every history — "
      "a DIRECT per-actor mass census (round-1 MINOR 2: this gate "
      "does not evaluate G; the derivation from G is the note's §6 + "
      "the probe's S3(d))",
      qbad == 0, f"off-law = {qbad}")

print("\n[VERDICT]")
ok = (inv_bad == 0 and c5c_bad == c5d_bad == first_bad == 0
      and b_prop == b_self == b_pair == 0
      and b_prop_eff == b_self_eff == b_pair_eff == 0
      and third == 0 and h1_bad == 0 and qbad == 0)
if ok:
    print("  (H1) STANDS AS A THEOREM at two-actor delivery-free d42a")
    print("  scope, CARRIED BY THE ADOPTED PROOF NOTE (d60p §3-§7b,")
    print("  prose-over-code) — with every case claim (preconditions")
    print("  AND effects), the code-facts, the invariants 5a-5e, the")
    print("  dichotomy, and the conclusion gated at every cached")
    print("  transition here (parents to depth <= 5), and the")
    print("  conclusion additionally gated at depth 8 by the probe and")
    print("  independently by the round-1 review.  A Lean-grade")
    print("  mechanization remains a RESIDUE, stated as such.")
    print("  CONSEQUENCES, RESTATED BY ROUND 1 (the round's BLOCKER):")
    print("  D44a's closure theorem remains CONDITIONAL on (H2) alone")
    print("  — (H0) is now fully discharged (clauses 1-3 by Lemmas")
    print("  4/5, clause 4 by Lemma 7b) — with (H2) verified")
    print("  exhaustively through depth 8 (round-1 review: 176 keys,")
    print("  0 violations, independent layer).  RESIDUE 1 is DECIDED")
    print("  AT EVERY VERIFIED DEPTH; its last named gap has shrunk")
    print("  from three hypotheses to ONE ((H2) — the update table,")
    print("  D62).  'Residue 1 closed' / 'D44a unconditional' are NOT")
    print("  delivered by this unit and may not be quoted from it.")
    print("  Transport untouched; three actors out of scope (and the")
    print("  wall now EXHIBITED: 5,904 admissible third-case views at")
    print("  three actors, depth <= 4 — round-1 review).")
else:
    print("  a gate failed — the failure is the deliverable.")
print(f"\n[d61] {PASS} PASS / {FAIL} FAIL"
      + (f"  ({ANCHOR_FAIL} anchor failures)" if ANCHOR_FAIL else ""))
# round-1 MINOR 8: the pin's protocol is exit 0 for substantive
# negatives, exit 1 ONLY on anchor breakage (N0/N1)
sys.exit(1 if ANCHOR_FAIL else 0)
