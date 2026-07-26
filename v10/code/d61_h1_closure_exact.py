#!/usr/bin/env python3
"""
d61_h1_closure_exact.py — v10 D61: closing (H1).
Pin: note-d61-h1-closure-pin.md §1-§3 + the §4 first-run amendment
(run 1's hand-rolled state was coarser than sigma; and any cache-gated
machine leaves the depth gap — the theorem is carried by the probe's
prose-over-code proof, this receipt gates its case claims, code-facts,
and conclusion).  Exit 1 only on anchor breakage.
"""
import sys
from collections import defaultdict
from fractions import Fraction as Fr
from itertools import permutations
sys.setrecursionlimit(200000)
PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
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
      "no abstraction of this receipt's own)",
      callable(canon_sigma) and callable(canon_menu), "single sources")

# code-facts the proof reads (Lemma 1): asserted against the source
src = _s
cfact = ("def regs_of(op):" in src
         and "if op[0] in ('p', 'n'): return frozenset([op[1]])" in src
         and "props = {t[0] for t in op[2]}" in src)
check("N1 CODE-FACTS (Lemma 1's register geometry, asserted against "
      "the committed source): regs_of gives {actor} for p/n and "
      "{proposers} u {fresh vname} for r — the registers are ACTOR "
      "NAMES plus arbitrator-owned version names, which is the entire "
      "basis of the dichotomy",
      cfact, "source assertions hold")

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


# ---------------- N2: the invariants (5a/5b/5e), all instances ------
inv_bad = 0
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
check("N2 LEMMA 5's INVARIANTS (5a alive singleton; 5b <= 1 live, on "
      "X_a; 5e <= 1 full-view-superseded X) at EVERY history, "
      "layer-computed: zero violations",
      inv_bad == 0, f"histories = {len(FAM)}, violations = {inv_bad}")

# ---------------- N3: the CASE-CLAIM battery ------------------------
print("\n[N3 — Lemma 5's step cases, checked at every instance]")
c_self = c_pair = c_prop = 0
b_self = b_pair = b_prop = b_cover = 0
for h in FAM:
    if len(h) >= CAP:
        continue
    st, _ = state_of(h)
    for e, q in CACHE[h]:
        if e[0] == 'p':
            c_prop += 1
            a = e[1]
            alive, live = st[a]
            if e[2] != next(iter(alive)) or live:
                b_prop += 1
        elif e[0] == 'r':
            actors_in = {t[0] for t in e[2]}
            base = next(iter(e[2]))[1]
            if len(actors_in) == 1:
                c_self += 1
                a = e[1]
                if len(e[2]) != 1 or base != next(iter(st[a][0])):
                    b_self += 1
            else:
                c_pair += 1
                if not all(base == next(iter(st[x][0])) for x in AB):
                    b_pair += 1
        if e[0] not in ('p', 'r', 'n'):
            b_cover += 1
check("N3(a) THE PROPOSE CASE: every admissible propose is on the "
      "actor's own alive singleton X_a with no prior live proposal — "
      "at every instance",
      c_prop > 0 and b_prop == 0,
      f"instances = {c_prop}, violations = {b_prop}")
check("N3(b) THE SELF-ARB CASE: every admissible single-actor arb "
      "consumes a SINGLETON component on that actor's own X_a — at "
      "every instance",
      c_self > 0 and b_self == 0,
      f"instances = {c_self}, violations = {b_self}")
check("N3(c) THE PAIR-ARB CASE: every admissible two-actor arb sits "
      "on a base that is BOTH actors' alive singleton (X_A = X_B = "
      "base) — at every instance",
      c_pair > 0 and b_pair == 0,
      f"instances = {c_pair}, violations = {b_pair}")
check("N3(d) CASE EXHAUSTIVENESS: every menu event is p, r or n — the "
      "case split covers the alphabet",
      b_cover == 0, f"non-p/r/n menu events = {b_cover}")

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
for h in FAM:
    sg = canon_sigma(h)
    cm = canon_menu(h)
    if sg in by_sig and by_sig[sg] != cm:
        h1_bad += 1
    by_sig[sg] = cm
check("N4 (H1)'s CONCLUSION at this receipt's scope: equal canonical "
      "sigma => IDENTICAL canonical menu (renamed event-multiset with "
      f"exact weights), over all {len(FAM)} histories, "
      f"{len(by_sig)} sigma classes — zero splits.  The probe gated "
      "the same over 930,631 histories at depth 8 [PROBE-CARRIED]",
      h1_bad == 0 and len(by_sig) >= 30,
      f"sigma classes = {len(by_sig)}, splits = {h1_bad}")

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
      "the quarter law as the closed form G derives it (probe §6)",
      qbad == 0, f"off-law = {qbad}")

print("\n[VERDICT]")
ok = (inv_bad == 0 and b_prop == b_self == b_pair == b_cover == 0
      and third == 0 and h1_bad == 0 and qbad == 0)
if ok:
    print("  (H1) STANDS AS A THEOREM at two-actor delivery-free d42a")
    print("  scope, CARRIED BY THE ADOPTED PROOF NOTE (d60p §3-§7,")
    print("  prose-over-code) — with every case claim, the code-facts,")
    print("  the dichotomy, and the conclusion gated at every cached")
    print("  instance here, and the conclusion additionally gated at")
    print("  depth 8 by the probe.  A Lean-grade mechanization remains")
    print("  a RESIDUE, stated as such.  Consequences per the pin:")
    print("  D44a unconditional at this scope; RESIDUE 1 CLOSED here;")
    print("  D49 unconditional-at-depth here, within the stationary")
    print("  form (D50).  Transport untouched; three actors out of")
    print("  scope.")
else:
    print("  a gate failed — the failure is the deliverable.")
print(f"\n[d61] {PASS} PASS / {FAIL} FAIL")
sys.exit(1 if FAIL else 0)
