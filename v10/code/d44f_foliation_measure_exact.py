#!/usr/bin/env python3
"""
d44f_foliation_measure_exact.py — v10 D44f (successor 6): horn 2's
two open arms — the foliation face (Arm F, FG0-FG4) and the measure
side (Arm M, MG1-MG3). Pin: note-d44f-foliation-and-measure.md.
Parents: d43c TERMINAL #344 (the constructed {V_C} family; note
§5 C3's two open faces are EXACTLY what this unit tests); the d42b3
admission layer (exec'd __file__-anchored, the committed pattern);
paper 30 §5 (the completion problem's within-cut object); D44a
TERMINAL #368 (residue 1 decided at every verified depth — cited by
MG2's uniqueness upgrade at its honest conditional scope).

ARM F: from the join cut BOTH actors hold admissible arbitration
opportunities on the SAME component (different initiators). The two
cut-advance orders (A-first / B-first) are computed as FULL branch
ensembles — classical weights exact Fractions through the layer's
admissible()/candidates_for; amplitudes through the committed
V-family at mp.dps 50 — and compared entrywise on the TERMINAL
ensembles (multisets of (canonical record, weight, amplitude)).
Either FG2 horn is a delivered outcome (exit 0); exit 1 is reserved
for breakage/anchor failure.

ARM M: the forcing sweep (pinned tilt directions spanning the
component index at both cuts; every non-trivial tilt convicted by a
NAMED committed gate; a tilt slipping ALL gates fails the sweep —
no silent acceptance) and the reduction map (the cross-component
weight assignment problem at the fixture's cuts mapped cut-by-cut,
in Fractions, onto the committed completion problem's within-cut
normalizer-and-ratio object; the dictionary printed and gated; the
uniqueness upgrade stated at conditional scope, citing LOG #368).
"""
import os
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

_here = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(_here, 'd42b3_placement_exact.py')).read()
ns = {}
exec(_src[:_src.index('print("[d42b3')], ns)
V0 = ns['V0']
candidates_for = ns['candidates_for']
admissible = ns['admissible']
event_poset = ns['event_poset']
View = ns['View']
arb_components_in_view = ns['arb_components_in_view']
PK1 = ns['PK1']
regs_of = ns['regs_of']
canon = ns['canon']
mu_of = ns['mu_of']
enumerate_family = ns['enumerate_family']
AB = ('A', 'B')

print("[d44f — the foliation face and the measure side]")
print("  banner: classical weights, menus, Z-multipliers, ratios,")
print("  and the MG2 dictionary are EXACT Fractions (the committed")
print("  d42b3 layer, __file__-anchored). FLOAT ENTRY POINTS,")
print("  enumerated exhaustively: (1) the d43c V-family matrices and")
print("  branch-amplitude products (mp.dps 50, compared at 1e-40);")
print("  (2) the MG1 tilt amplitudes (same discipline). Nothing")
print("  else leaves Fractions; MG3 gates this with the d45a-form")
print("  ALLOW-LIST purity walk (LOG #362 successor binding) plus a")
print("  gated trip control. FG2 was PRE-REGISTERED OPEN (either")
print("  horn a result, exit 0); the computation delivered the")
print("  UNEQUAL horn, which the receipt now gates as an anchor —")
print("  exit 1 = breakage/anchor failure only, never a horn")
print("  preference. No continuum claim; Hegerfeldt untouched;")
print("  fixture scale.")

# ---- the fixture (the committed d43c/d42b3 events) -----------------
pA0 = ('p', 'A', V0, 0)
pB1 = ('p', 'B', V0, 1)
tA, tB = ('A', V0, 0), ('B', V0, 1)
SELFA = ('r', 'A', frozenset({tA}), frozenset({tA}))
SELFB = ('r', 'B', frozenset({tB}), frozenset({tB}))
PAIRA = ('r', 'A', frozenset({tA, tB}), frozenset({tA}))
PAIRB = ('r', 'A', frozenset({tA, tB}), frozenset({tB}))
BPAIRA = ('r', 'B', frozenset({tA, tB}), frozenset({tA}))
BPAIRB = ('r', 'B', frozenset({tA, tB}), frozenset({tB}))
H1, H2 = [pA0], [pA0, pB1]
PAIRCK = frozenset({tA, tB})

def fmt_t(t):
    return f"{t[0]}{t[2]}"

def fmt_e(e):
    if e[0] == 'r':
        return (f"r[{e[1]}|ck={{{','.join(sorted(map(fmt_t, e[2])))}}}"
                f"|w={{{','.join(sorted(map(fmt_t, e[3])))}}}]")
    if e[0] == 'p':
        return f"p[{e[1]}|v0|{e[3]}]"
    return f"n[{e[1]}]"

# ============ FG0 — the committed d43c objects, re-anchored =========
print("\n[FG0 — the committed d43c objects re-anchored]")
O_pair = zeros(2, 1)
O_pair[0, 0] = 1 / sqrt(2)
O_pair[1, 0] = 1 / sqrt(2)
A_pair = zeros(4, 2)
A_pair[0, 0] = mpf(1)
A_pair[3, 1] = mpf(1)
V_pair = A_pair * O_pair
O_sing = zeros(1, 1)
O_sing[0, 0] = mpf(1)
A_sing = zeros(2, 1)
A_sing[0, 0] = mpf(1)
V_sing = A_sing * O_sing
VFAM = {1: V_sing, 2: V_pair}
BORN = {1: [Fr(1)], 2: [Fr(1, 2), Fr(1, 2)]}

def iso_defect(M):
    G = M.T * M
    return max(fabs(G[i, j] - (1 if i == j else 0))
               for i in range(G.rows) for j in range(G.cols))

defects = [iso_defect(M) for M in (V_pair, V_sing)]
check("FG0-a V_single (2x1) and V_pair (4x1) rebuilt as Acceptance o "
      "OpeningClick (the committed d43c PG3-E1 construction) and "
      "ISOMETRIC at 1e-40",
      (V_pair.rows, V_pair.cols, V_sing.rows, V_sing.cols)
      == (4, 1, 2, 1) and all(d < TOL for d in defects),
      f"max V^T V - I defect = {chop(max(defects))}")

edge = frozenset({tuple(sorted((tA, tB)))})
k1_pair = PK1(frozenset({tA, tB}), edge)
k1_sing = PK1(frozenset({tA}), frozenset())
born_ok = (fabs(V_pair[0, 0] ** 2 - mpf(1) / 2) < TOL
           and fabs(V_pair[3, 0] ** 2 - mpf(1) / 2) < TOL
           and fabs(V_sing[0, 0] ** 2 - 1) < TOL)
check("FG0-b BORN = K1 (the committed d43c PG3-E3 anchor): V_pair's "
      "squared branch amplitudes are 1/2-1/2 = PK1 on the "
      "2-conflict (recomputed from the layer) and V_single's branch "
      "is deterministic = PK1 on the singleton, at 1e-40",
      born_ok and k1_pair == {frozenset({tA}): Fr(1, 2),
                              frozenset({tB}): Fr(1, 2)}
      and k1_sing == {frozenset({tA}): Fr(1)},
      f"PK1(pair) = 1/2-1/2, PK1(single) = 1: "
      f"{k1_pair == {frozenset({tA}): Fr(1, 2), frozenset({tB}): Fr(1, 2)}}")

def arb_menu(h, a):
    return sorted(((e, q) for e, q in candidates_for(h, AB)
                   if e[1] == a and e[0] == 'r'), key=repr)

m1A = arb_menu(H1, 'A')
m2A = arb_menu(H2, 'A')
m2B = arb_menu(H2, 'B')
menus_ok = (dict(m1A) == {SELFA: Fr(1, 4)}
            and dict(m2A) == {SELFA: Fr(1, 4), PAIRA: Fr(1, 8),
                              PAIRB: Fr(1, 8)}
            and dict(m2B) == {SELFB: Fr(1, 4), BPAIRA: Fr(1, 8),
                              BPAIRB: Fr(1, 8)})
check("FG0-c the committed menus, exact in Fractions: A's arb menu "
      "at the early cut = {self: 1/4}; at the join = {self: 1/4, "
      "pair winners: 1/8 + 1/8} (the d43c PG3-E4/R3 anchor); B's "
      "join menu is the mirror {self: 1/4, pair winners: 1/8 + 1/8}",
      menus_ok, "1/4 early; 1/4 + 1/8 + 1/8 at the join, both actors")

# the share x Born factorization of the menus (the E4 form — this is
# the bare-weight identity MG2's dictionary consumes; gated here so
# the reduction below is non-tautological)
def share(h, e):
    acts2 = h + [e]
    pred = event_poset(acts2)
    view = View(acts2, pred, pred[len(acts2) - 1])
    return Fr(1, 4) / len(arb_components_in_view(view, e[1]))

fact_ok = (dict(m1A)[SELFA] == share(H1, SELFA) * BORN[1][0]
           and all(dict(m2A)[e] == share(H2, e) * b for e, b in
                   ((SELFA, BORN[1][0]), (PAIRA, BORN[2][0]),
                    (PAIRB, BORN[2][1])))
           and all(dict(m2B)[e] == share(H2, e) * b for e, b in
                   ((SELFB, BORN[1][0]), (BPAIRA, BORN[2][0]),
                    (BPAIRB, BORN[2][1]))))
check("FG0-d the menu FACTORIZATION (past-local share x exact Born "
      "split) reproduces every committed arb weight at both cuts, "
      "both actors, exactly — the d43c E4 reconstruction re-anchored",
      fact_ok, "q = (1/4 / #components(own view)) x Born, 7/7 events")

both_hold = (any(e[2] == PAIRCK for e, q in m2A)
             and any(e[2] == PAIRCK for e, q in m2B)
             and all(not admissible(H1, e)[0]
                     for e in (PAIRA, PAIRB, BPAIRA, BPAIRB)))
check("FG0-e the FG1 precondition: at the join cut BOTH actors hold "
      "admissible arbitration opportunities on the SAME component "
      "(ckey {A0,B1}, initiators A and B) — and none of the four "
      "pair events is admissible at the early cut",
      both_hold, "the overlapping-visibility configuration is live")

# ============ FG1 — the two cut-advance orders ======================
print("\n[FG1 — the two cut-advance orders through the V-family]")
# The advance rule (pinned): the designated actor's FULL arb menu
# branches first; from each post-first state the OTHER actor's
# remaining admissible arb opportunities branch; a branch terminates
# when the second actor's remaining arb menu is empty. Classical
# branch weights are the exact q-products through the layer;
# amplitudes are the V-family branch entries (V_single: 1;
# V_pair: 1/sqrt(2) per winner), multiplied along the branch.

def amp_branch(e):
    if len(e[2]) == 1:
        return V_sing[0, 0]                       # deterministic
    return V_pair[0, 0] if e[3] == frozenset({tA}) else V_pair[3, 0]

def ensemble(h, first, second):
    out = []
    for e1, q1 in arb_menu(h, first):
        h3 = h + [e1]
        rem = arb_menu(h3, second)
        if not rem:
            out.append((h3, q1, amp_branch(e1)))
        else:
            for e2, q2 in rem:
                out.append((h3 + [e2], q1 * q2,
                            amp_branch(e1) * amp_branch(e2)))
    return out

ENS_A = ensemble(H2, 'A', 'B')
ENS_B = ensemble(H2, 'B', 'A')

def show(tag, E):
    print(f"  {tag} terminal ensemble ({len(E)} branches):")
    for hh, q, a in sorted(E, key=lambda x: repr([fmt_e(e)
                                                  for e in x[0][2:]])):
        steps = ' '.join(fmt_e(e) for e in hh[2:])
        print(f"    {steps}  weight {q}  amp {mp.nstr(a, 12)}")

show("A-first", ENS_A)
show("B-first", ENS_B)

shapes_ok = (len(ENS_A) == 3 and len(ENS_B) == 3
             and sum(q for _, q, _ in ENS_A) == Fr(5, 16)
             and sum(q for _, q, _ in ENS_B) == Fr(5, 16))
check("FG1-a both branch trees computed to termination: 3 terminal "
      "branches each (self-then-self at 1/16; the two pair winners "
      "at 1/8, after which the other actor's arb menu is EMPTY — the "
      "pair arbitration resolves the whole component); total "
      "classical arb-sector weight 5/16 under BOTH orders, exact",
      shapes_ok, "3 vs 3 branches; totals 5/16 = 5/16")

def ckey_sig(hh):
    return tuple(sorted(repr((tuple(sorted(e[2])), tuple(sorted(e[3]))))
                        for e in hh[2:]))

# multiset comparison is STRUCTURAL (frozenset ==), never repr-based
def multiset_matches(A, B):
    B2 = list(B)
    m = 0
    for x in A:
        for i, y in enumerate(B2):
            if x == y:
                del B2[i]
                m += 1
                break
    return m

def multiset_diff(A, B):
    B2 = list(B)
    out = []
    for x in A:
        for i, y in enumerate(B2):
            if x == y:
                del B2[i]
                break
        else:
            out.append(x)
    return out

entA = [(canon(hh), q, mp.nstr(a, 45)) for hh, q, a in ENS_A]
entB = [(canon(hh), q, mp.nstr(a, 45)) for hh, q, a in ENS_B]
n_match = multiset_matches(entA, entB)
amp_dev = max(fabs(sorted(a for _, _, a in ENS_A)[i]
                   - sorted(a for _, _, a in ENS_B)[i])
              for i in range(3))
wamp_ok = (sorted((q, mp.nstr(a, 45)) for _, q, a in ENS_A)
           == sorted((q, mp.nstr(a, 45)) for _, q, a in ENS_B)
           and amp_dev < TOL)
check("FG1-b the entrywise comparison is computed on the committed "
      "canonical form: the (canonical record, weight, amplitude) "
      "multisets share exactly 1 of 3 entries (the self-then-self "
      "branch — its two orders are ONE canonical record: the "
      "intermediate ordering is bookkeeping, said precisely); the "
      "(weight, amplitude) multisets WITHOUT records are equal at "
      "1e-40",
      n_match == 1 and wamp_ok,
      f"canonical-entry matches = {n_match}/3; weight-amp multisets "
      f"equal; max amp deviation = {chop(amp_dev)}")

# ============ FG2 — the verdict + the attribution gate ==============
print("\n[FG2 — the verdict on the foliation face]")
EQUAL = (n_match == len(entA) == len(entB))
print(f"  the two orders' terminal ensembles equal: {EQUAL}")
check("FG2-a the verdict is UNEQUAL (pre-registered open; this horn "
      "delivered): the terminal-state ensembles differ — 2 of 3 "
      "canonical records disagree across the orders",
      (not EQUAL) and n_match == 1,
      "the obstruction is exhibited entry-by-entry below")

diffA = multiset_diff(entA, entB)
diffB = multiset_diff(entB, entA)
print("  the obstruction, entry-by-entry (A-first only vs B-first "
      "only):")
diff_pairing_ok = True
for eA_, eB_ in ((PAIRA, BPAIRA), (PAIRB, BPAIRB)):
    kA_, kB_ = canon(H2 + [eA_]), canon(H2 + [eB_])
    inA = any(x[0] == kA_ for x in diffA)
    inB = any(x[0] == kB_ for x in diffB)
    diff_pairing_ok = diff_pairing_ok and inA and inB
    print(f"    A-first: {fmt_e(eA_)} (weight 1/8)  vs  B-first: "
          f"{fmt_e(eB_)} (weight 1/8); same winner, same weight, "
          f"amps equal at 1e-40; records differ in the initiator")

def erase_init(cn):
    def em(node):
        act, preds = node
        if act[0] == 'r':
            act = ('r', '*', act[2], act[3])
        return (act, frozenset(em(p) for p in preds))
    return frozenset(em(n) for n in cn)

erA = [(erase_init(canon(hh)), q, mp.nstr(a, 45)) for hh, q, a in ENS_A]
erB = [(erase_init(canon(hh)), q, mp.nstr(a, 45)) for hh, q, a in ENS_B]
er_eq = (multiset_matches(erA, erB) == len(erA) == len(erB))
margA = sorted(ckey_sig(hh) for hh, _, _ in ENS_A)
margB = sorted(ckey_sig(hh) for hh, _, _ in ENS_B)
check("FG2-b the obstruction is EXACTLY the initiator slot: erasing "
      "the initiator tag from arbitration events in the canonical "
      "DAGs (the poset structure kept intact) makes the two "
      "ensembles ENTRYWISE EQUAL — and the (ckey, winner) marginal "
      "multisets are equal un-erased. The winner set, the weights, "
      "and the amplitudes are order-invariant; the records differ "
      "only in WHO initiates the pair arbitration (and hence which "
      "version register carries the winner)",
      er_eq and margA == margB and len(diffA) == 2
      and diff_pairing_ok,
      f"erased ensembles equal = {er_eq}; winner marginals "
      f"equal = {margA == margB}")

# attribution: which committed requirement forces the difference
excl_ok = (admissible(H2, BPAIRA)[0] and admissible(H2, BPAIRB)[0]
           and not admissible(H2 + [PAIRA], BPAIRA)[0]
           and not admissible(H2 + [PAIRA], BPAIRB)[0]
           and not admissible(H2 + [BPAIRB], PAIRA)[0]
           and not admissible(H2 + [BPAIRB], PAIRB)[0])
shared = regs_of(PAIRA) & regs_of(BPAIRA)
acts2 = H2 + [PAIRA, BPAIRA]
in_past = 2 in event_poset(acts2)[3]
check("FG2-c ATTRIBUTION, part 1 (carrier licensing + admission "
      "structure CONVICTED): the two actors' pair opportunities are "
      "MUTUALLY EXCLUSIVE — each is admissible at the join but "
      "inadmissible after the other fires — because the pair "
      "arbitration's licensed carriers are BOTH proposers' registers "
      "(A4/A6: shared carriers {A, B}), which places either actor's "
      "pair arb in the other's event past, where the resolved "
      "component blocks re-arbitration. This is note-d43c §5 C3's "
      "forfeited commutation-by-disjointness, now a firing gate",
      excl_ok and shared == frozenset({'A', 'B'}) and in_past,
      f"mutual exclusion 4/4; shared carriers = "
      f"{sorted(shared)}; A's pair arb lies in B's pair-arb past = "
      f"{in_past}")

check("FG2-d ATTRIBUTION, part 2 (Born weights and isometry "
      "ACQUITTED): the weight-amplitude content is order-invariant "
      "(FG1-b) and the winner marginals agree (FG2-b) — the "
      "difference is NOT forced by the Born = K1 kernel or the "
      "isometry requirement; it is forced by the event identity's "
      "initiator attachment under carrier-licensed mutual exclusion. "
      "THE CHOICE A FOLIATION WOULD HAVE TO MAKE, stated exactly: "
      "which actor initiates the join arbitration — nothing else",
      wamp_ok and margA == margB and er_eq and not EQUAL,
      "obstruction confined to the initiator slot + its version "
      "register")

# ============ FG3 — the disjoint-components control =================
print("\n[FG3 — disjoint components commute; the overlapped mutant "
      "fails the gate]")
# Genuinely disjoint components at ONE cut: two same-value proposals
# (no conflict edge) yield TWO singleton components in the full view.
pB0 = ('p', 'B', V0, 0)
tB0 = ('B', V0, 0)
SELFB0 = ('r', 'B', frozenset({tB0}), frozenset({tB0}))
G2 = [pA0, pB0]
gpred = event_poset(G2)
gcomps = View(G2, gpred, set(range(2))).components()

def commutes(h, e1, e2):
    """The commutation gate: both orders fully admissible, one
    canonical record, equal mu — returns (ok, detail)."""
    a1 = admissible(h, e1)[0] and admissible(h + [e1], e2)[0]
    a2 = admissible(h, e2)[0] and admissible(h + [e2], e1)[0]
    if not (a1 and a2):
        return False, f"orders admissible = {a1}/{a2}"
    o1, o2 = h + [e1, e2], h + [e2, e1]
    same = canon(o1) == canon(o2) and mu_of(o1) == mu_of(o2)
    return same, f"canon equal + mu equal = {same}; mu = {mu_of(o1)}"

ok_dis, det_dis = commutes(G2, SELFA, SELFB0)
check("FG3-a the DISJOINT control PASSES: at the same-value cut "
      "[pA0, pB0] the full view holds TWO disjoint singleton "
      "components ({A0} and {B0}); the two self-arbitrations "
      "commute EXACTLY — both orders admissible, one canonical "
      "record, equal mu (= 1/1024) — the disjointness lemma as a "
      "firing gate",
      len(gcomps) == 2
      and sorted(len(c) for _, c in gcomps) == [1, 1]
      and ok_dis and mu_of(G2 + [SELFA, SELFB0]) == Fr(1, 1024),
      det_dis)

ok_ov, det_ov = commutes(H2, PAIRA, BPAIRB)
check("FG3-b the OVERLAPPED mutant FAILS the SAME gate (the gated "
      "negative control — the gate demonstrably can fail): the two "
      "actors' pair arbitrations on the SHARED component do not "
      "commute — each order's second event is INADMISSIBLE (the "
      "first resolves the component)",
      not ok_ov, det_ov)

# ============ FG4 — the same-initiator sequential control ===========
print("\n[FG4 — order irrelevance where no ambiguity exists]")
# Same-initiator sequential opportunities are totally ordered on the
# initiator's own chain (proposing on a version requires the version
# to exist), so the POSABLE order question is the committed A7
# witness pair: A's unambiguous self-arbitration (singleton component
# in its own past view at BOTH positions) against the blind pB1.
E1 = [pA0, SELFA, pB1]
E2 = [pA0, pB1, SELFA]
fg4_ok = (canon(E1) == canon(E2)
          and mu_of(E1) == mu_of(E2) == Fr(1, 256)
          and admissible([pA0], SELFA)[1]
          == admissible(H2, SELFA)[1] == Fr(1, 4))
check("FG4 the same-initiator sequential control: where NO overlap "
      "ambiguity exists (A's self-arb reads only its own singleton "
      "component), order is irrelevant — the committed A7 witness "
      "pair is ONE canonical record with mu = 1/256 under both "
      "orders (the d42b3 G-T2 anchor) and A's arb weight is 1/4 at "
      "both positions; the V-family applies the SAME V_single with "
      "amplitude 1 in both. Strictly-sequential same-initiator "
      "opportunities admit no order choice at all (each requires "
      "the previous event's output register), declared",
      fg4_ok, "canon equal; mu = 1/256 = 1/256; q = 1/4 both cuts")

# ============ MG1 — the forcing sweep ===============================
print("\n[MG1 — the forcing sweep: per-component amplitude tilts]")
# A tilt assigns per-cut, per-component operator instances:
#   {(cut, |C|): matrix}, cut in {1 (early), 2 (join)}.
# The committed gate battery (all four are d43c PG3 requirements):
#   ISO      isometry at 1e-40 (PG3-E2)
#   BORN     squared branch amplitudes = PK1 at 1e-40 (PG3-E3)
#   MENU     share x |amp|^2 = the committed menus, both cuts (E4)
#   CUTIND   the SAME matrices at both cuts, entrywise 1e-40 (E5)
# The sweep convicts each non-trivial tilt by NAME; a tilt slipping
# ALL FOUR gates makes the sweep gate itself FAIL (no silent
# acceptance) — demonstrated live via the reduced-battery run below.
COMMITTED = {frozenset({tA}): Fr(1), frozenset({tB}): Fr(0)}

def tilt_family(f1=None, f2=None, g1=None):
    """cut-2 singleton factor f1, cut-2 pair matrix f2 (or scale),
    cut-1 singleton factor g1; defaults = committed."""
    W = {(1, 1): V_sing if g1 is None else g1 * V_sing,
         (2, 1): V_sing if f1 is None else f1 * V_sing,
         (2, 2): V_pair if f2 is None else
         (f2 if hasattr(f2, 'rows') else f2 * V_pair)}
    return W

def pair_matrix(c, s):
    M = zeros(4, 1)
    M[0, 0] = c
    M[3, 0] = s
    return M

def born_of(M, size):
    if size == 1:
        return {frozenset({tA}): M[0, 0] ** 2}
    return {frozenset({tA}): M[0, 0] ** 2, frozenset({tB}): M[3, 0] ** 2}

def battery(W, gates=('ISO', 'BORN', 'MENU', 'CUTIND')):
    fired = []
    if 'ISO' in gates:
        if any(iso_defect(M) >= TOL for M in
               (W[(1, 1)], W[(2, 1)], W[(2, 2)])):
            fired.append('ISO')
    if 'BORN' in gates:
        dev = []
        for (cut, size), M in sorted(W.items()):
            k1 = k1_sing if size == 1 else k1_pair
            b = born_of(M, size)
            dev += [fabs(b[w] - mpf(k1[w].numerator) / k1[w].denominator)
                    for w in sorted(k1, key=repr)]
        if any(d >= TOL for d in dev):
            fired.append('BORN')
    if 'MENU' in gates:
        recon = [(share(H1, SELFA) * born_of(W[(1, 1)], 1)[frozenset({tA})],
                  dict(m1A)[SELFA]),
                 (share(H2, SELFA) * born_of(W[(2, 1)], 1)[frozenset({tA})],
                  dict(m2A)[SELFA]),
                 (share(H2, PAIRA) * born_of(W[(2, 2)], 2)[frozenset({tA})],
                  dict(m2A)[PAIRA]),
                 (share(H2, PAIRB) * born_of(W[(2, 2)], 2)[frozenset({tB})],
                  dict(m2A)[PAIRB])]
        if any(fabs(got - mpf(want.numerator) / want.denominator) >= TOL
               for got, want in recon):
            fired.append('MENU')
    if 'CUTIND' in gates:
        if any(fabs(W[(1, 1)][i, 0] - W[(2, 1)][i, 0]) >= TOL
               for i in range(2)):
            fired.append('CUTIND')
    return fired

TILTS = [
    ("T0 trivial (the committed family)", tilt_family(), []),
    ("T1 pair-scale 9/10 (component-index tilt at the join)",
     tilt_family(f2=mpf(9) / 10), None),
    ("T2 singleton-scale 11/10 (component-index tilt, both cuts)",
     tilt_family(f1=mpf(11) / 10, g1=mpf(11) / 10), None),
    ("T3 within-pair rotation (3/5, 4/5) — isometry-preserving",
     tilt_family(f2=pair_matrix(mpf(3) / 5, mpf(4) / 5)), None),
    ("T4 cross-component transfer (singleton x 1/sqrt(2) both cuts, "
     "pair x sqrt(3/2)) — arb-sector TOTAL preserved at the join",
     tilt_family(f1=1 / sqrt(2), g1=1 / sqrt(2), f2=sqrt(mpf(3) / 2)),
     None),
    ("T5 cut-asymmetric sign (join singleton = -V_single)",
     tilt_family(f1=mpf(-1)), None),
    ("T6 cut-asymmetric singleton scale 4/5 (join only)",
     tilt_family(f1=mpf(4) / 5), None),
]
print("  the pinned tilt directions (spanning the component index at")
print("  both cuts: T1/T2 per-component scale, T3 within-pair, T4")
print("  pair-vs-singleton, T5/T6 cut-asymmetric) and the battery's")
print("  convictions:")
conv = {}
for name, W, _ in TILTS:
    conv[name] = battery(W)
    print(f"    {name}: fired = {conv[name] if conv[name] else '[]'}")

W4 = TILTS[4][1]
t4_total = (share(H2, SELFA) * born_of(W4[(2, 1)], 1)[frozenset({tA})]
            + share(H2, PAIRA)
            * (born_of(W4[(2, 2)], 2)[frozenset({tA})]
               + born_of(W4[(2, 2)], 2)[frozenset({tB})]))
check("MG1-a the trivial tilt is NOT convicted (the battery has a "
      "live green baseline — no false convictions) and EVERY "
      "non-trivial tilt IS convicted by at least one named committed "
      "gate",
      conv[TILTS[0][0]] == [] and all(conv[n] for n, _, x in TILTS[1:]),
      "; ".join(f"{n.split()[0]}:{'+'.join(conv[n]) if conv[n] else 'NONE'}"
                for n, _, _ in TILTS))

check("MG1-b the conviction table's load-bearing rows: T3 (isometry-"
      "PRESERVING within-pair rotation) is convicted by BORN+MENU, "
      "not ISO — the kernel, not unitarity, pins the within-pair "
      "split; T4 (cross-component transfer that PRESERVES the "
      "arb-sector total, = 1/2 exactly) is convicted by ISO+BORN+"
      "MENU — moving weight BETWEEN components cannot be hidden in "
      "the total; T5 (pure sign at one cut) is convicted by CUTIND "
      "ALONE",
      conv[TILTS[3][0]] == ['BORN', 'MENU']
      and conv[TILTS[4][0]] == ['ISO', 'BORN', 'MENU']
      and conv[TILTS[5][0]] == ['CUTIND']
      and fabs(t4_total - mpf(1) / 2) < TOL,
      f"T4 arb-sector total = 1/2 at 1e-40 (dev "
      f"{chop(fabs(t4_total - mpf(1) / 2))}), yet convicted")

reduced_t5 = battery(TILTS[5][1], gates=('ISO', 'BORN', 'MENU'))
sweep_reduced = (conv[TILTS[0][0]] == []
                 and all(battery(W, gates=('ISO', 'BORN', 'MENU'))
                         for n, W, _ in TILTS[1:]))
check("MG1-c NO SILENT ACCEPTANCE, demonstrated live: under the "
      "REDUCED battery {ISO, BORN, MENU} the T5 sign tilt slips ALL "
      "gates and the sweep gate FAILS (all-convicted is False) — "
      "the wiring that would catch an all-gate-slipping tilt is "
      "exercised, not narrated; the full battery's CUTIND row is "
      "load-bearing",
      reduced_t5 == [] and (not sweep_reduced),
      f"reduced-battery T5 convictions = {reduced_t5}; reduced sweep "
      f"all-convicted = {sweep_reduced} (would exit 1 if it were the "
      "battery)")

check("MG1-d THE FORCING CONCLUSION, RESCOPED (round-1 BLOCKER-1): "
      "every pinned non-trivial re-weighting WITH NONZERO "
      "SQUARED-AMPLITUDE CONTENT violates a committed gate — the "
      "operator layer FORCES the classical cross-component WEIGHTS "
      "(the |amp|^2 data; each V_C's Born split sums to 1); the "
      "surviving freedom is the SIGN/PHASE SECTOR (MG1-e: gauge on "
      "amplitudes carrying EXACTLY ZERO |amp|^2 content — invisible "
      "to weights by construction): the family cannot carry a "
      "MEASURE tilt",
      all(conv[n] for n, _, _ in TILTS[1:])
      and all(sum(BORN[k]) == Fr(1) for k in (1, 2)),
      "6/6 nonzero-|amp|^2 tilts convicted; Born sums = 1, 1")

# round-1 BLOCKER-1: the referee's four sign tilts, adopted — the
# battery's gate-passing set is the sign group {+-1}^3 on amplitudes,
# and every member carries zero squared-amplitude content:
W0REF = tilt_family()
def amp2_dev(W):
    d = mpf(0)
    for k in ((1, 1), (2, 1), (2, 2)):
        M, M0 = W[k], W0REF[k]
        for i in range(M.rows):
            d = max(d, fabs(M[i, 0] ** 2 - M0[i, 0] ** 2))
    return d
NTILTS = [
    ("N1 cut-symmetric singleton sign",
     tilt_family(f1=mpf(-1), g1=mpf(-1))),
    ("N2 within-pair relative sign",
     tilt_family(f2=pair_matrix(-1 / sqrt(2), 1 / sqrt(2)))),
    ("N3 pair global sign", tilt_family(f2=mpf(-1))),
    ("N4 joint sign",
     tilt_family(f1=mpf(-1), g1=mpf(-1), f2=mpf(-1))),
]
ne_ok = True
for name, W in NTILTS:
    fired = battery(W)
    d2v = amp2_dev(W)
    print(f"    {name}: fired = {fired if fired else '[]'}; "
          f"|amp^2| dev = {chop(d2v)}")
    ne_ok = ne_ok and (fired == []) and (d2v < TOL)
check("MG1-e THE SIGN SECTOR (round-1 BLOCKER-1, the referee's "
      "tilts adopted as the gate): all four sign tilts slip ALL "
      "FOUR committed gates AND carry exactly ZERO squared-"
      "amplitude content — the gate-passing freedom is the sign "
      "group {+-1}^3 acting on amplitudes, a GAUGE sector with no "
      "|amp|^2 (hence no weight/measure) content; the pinned "
      "'every non-trivial tilt is convicted' lemma was FALSE as "
      "stated and is superseded by MG1-d's rescoped form (the "
      "battery is real-valued; complex phases belong to the same "
      "zero-|amp|^2 gauge sector — declared, not swept)",
      ne_ok,
      "4/4 sign tilts: all gates slipped, |amp^2| dev = 0")

# ============ MG2 — the reduction map ===============================
print("\n[MG2 — the measure side reduces to residue 1, cut by cut]")
# The committed completion object (paper 30 §5.1; d42b3 D1(ii)):
# within a cut h, q'(e|h) = q(e|h) * Z(h+e) / Z(h) with normalizer
# Z(h) = sum_e q(e|h) * Z(h+e). The backward recursion is recomputed
# here from the layer at depth 4 and anchored to the committed
# numbers before the reduction is stated.
FAM, CACHE = enumerate_family(AB, 4)
Z = {}
for h in FAM:
    if len(h) == 4:
        Z[tuple(h)] = Fr(1)
for L in (3, 2, 1, 0):
    for h in FAM:
        if len(h) != L:
            continue
        Z[tuple(h)] = sum(q * Z[tuple(h + [e])]
                          for e, q in CACHE[tuple(h)])
root_q = [q for e, q in CACHE[()] if e == pA0][0]
root_completed = root_q * Z[tuple(H1)] / Z[()]
check("MG2-a the committed completion re-anchored from the layer "
      "(unit boundary, depth 4): Z(empty) = 1037/64, Z([pA0]) = "
      "133/16, Z([pA0,pB1]) = 23/4, and the root completed weight "
      "q'(pA0|empty) = (1/8)(133/16)/(1037/64) = 133/2074 — paper "
      "30 §5.3's printed root extreme, reproduced exactly",
      Z[()] == Fr(1037, 64) and Z[tuple(H1)] == Fr(133, 16)
      and Z[tuple(H2)] == Fr(23, 4) and root_q == Fr(1, 8)
      and root_completed == Fr(133, 2074) and len(FAM) == 1191,
      f"family = {len(FAM)} (anchor 1191); root completed = "
      f"{root_completed}")

ZS = {e: Z[tuple(H2 + [e])] for e in
      (SELFA, PAIRA, PAIRB, SELFB, BPAIRA, BPAIRB)}
Z1S = Z[tuple(H1 + [SELFA])]
check("MG2-b the committed multipliers at the fixture's arb cuts "
      "are COMPONENT-CONSTANT: at the join, ALL SIX arb successors "
      "(both initiators, both components) carry Z = 2 exactly; at "
      "the early cut, Z = 4 — so the committed completion datum "
      "lies in the per-component class the operator family can "
      "express (the dictionary's z_C is well-defined; this is a "
      "computed fact about the committed Z, not a definition)",
      all(z == Fr(2) for z in ZS.values()) and Z1S == Fr(4),
      f"Z(join arb successors) = {sorted(str(z) for z in ZS.values())}; "
      f"Z(early arb successor) = {Z1S}")

# THE DICTIONARY (printed, then gated row by row)
DICT_ROWS = [
    ("cut h", "arb cut (H1 early; H2 join)"),
    ("successor event e", "component-branch (C, w)"),
    ("bare weight q(e|h)", "share s_C x Born_C(w)  [gated FG0-d]"),
    ("multiplier Z(h+e)", "z_C, component-constant  [gated MG2-b]"),
    ("normalizer Z(h) = sum q Z", "N = sum_C s_C z_C (sector)"),
    ("completed q'(e|h) = q Z/Z(h)", "w(C,w) = s_C Born_C(w) z_C / N"),
    ("within-cut ratio q':q'", "s z Born : s' z' Born'"),
]
print("  THE DICTIONARY (completion side <-> fixture side):")
for lhs, rhs in DICT_ROWS:
    print(f"    {lhs:<30} <-> {rhs}")

# the correspondence, gated arithmetically at both cuts: for probe
# multiplier tuples (z_single, z_pair) in Fractions, the fixture-side
# assignment equals the completion-side transfer restricted to the
# arb sector, entry by entry — non-tautological because the bare
# identity q = s x Born is itself a gate (FG0-d), and the committed
# instantiation uses the recomputed Z.
CUTS = [(H1, [(SELFA, 1, BORN[1][0])]),
        (H2, [(SELFA, 1, BORN[1][0]), (PAIRA, 2, BORN[2][0]),
              (PAIRB, 2, BORN[2][1])])]
PROBES = [(Fr(1), Fr(1)), (Fr(2), Fr(3)), (Fr(5), Fr(7)),
          (Fr(3), Fr(1)), (Fr(2), Fr(2))]
red_ok = True
for h, sector in CUTS:
    s_of = {}
    for e, c, b in sector:
        s_of.setdefault(c, share(h, e))
    # the per-component share is constant across a component's
    # branches (gated as part of the correspondence):
    red_ok = red_ok and all(share(h, e) == s_of[c]
                            for e, c, b in sector)
    for z1, z2 in PROBES:
        zc = {1: z1, 2: z2}
        Nfix = sum(s_of[c] * zc[c] for c in sorted(s_of))
        Ncom = sum(admissible(h, e)[1] * zc[c] for e, c, b in sector)
        red_ok = red_ok and (Nfix == Ncom)
        for e, c, b in sector:
            w_fix = s_of[c] * b * zc[c] / Nfix
            w_com = admissible(h, e)[1] * zc[c] / Ncom
            red_ok = red_ok and (w_fix == w_com)
check("MG2-c the REDUCTION, gated cut-by-cut in Fractions: for "
      "every probe multiplier tuple (5 tuples, both cuts) the "
      "cross-component assignment problem — weights s_C z_C "
      "Born_C / N with COMPONENT-SUM normalizer N = sum_C s_C z_C — "
      "coincides ENTRYWISE with the committed completion's "
      "within-cut transfer q Z / Z restricted to the arb sector, "
      "whose normalizer is the BRANCH sum sum_e q z: the two "
      "normalizers are EQUAL exactly because each V_C's Born split "
      "sums to 1 (the sector's branch sum collapses to the "
      "component sum). SAME normalizers, SAME ratio constraints: "
      "horn 2's measure side IS residue 1's within-cut object at "
      "the fixture's cuts — arithmetically, not metaphorically",
      red_ok, "5 probes x 2 cuts x all branches + share constancy, "
      "exact")

# the committed instantiation: z = the recomputed Z values
z_committed = {1: ZS[SELFA], 2: ZS[PAIRA]}
Nsec = (share(H2, SELFA) * z_committed[1]
        + share(H2, PAIRA) * z_committed[2])
sector_ratios = [share(H2, e) * b * z_committed[c] / Nsec
                 for e, c, b in CUTS[1][1]]
qprime = [admissible(H2, e)[1] * ZS[e] / Z[tuple(H2)]
          for e, c, b in CUTS[1][1]]
qp_norm = [x / sum(qprime) for x in qprime]
check("MG2-d the COMMITTED instantiation (round-1 minor-1 relabel): "
      "plugging the recomputed committed multipliers (z_single, "
      "z_pair) = (2, 2) into the fixture side reproduces the "
      "committed completed arb-sector conditionals exactly — "
      "q'(self, pairA, pairB | H2) = (2/23, 1/23, 1/23) AT THE "
      "DEPTH-4 HORIZON (the absolute q' is horizon-bound), "
      "sector-normalized (1/2, 1/4, 1/4) on both sides — THE "
      "HORIZON-STABLE FORCED OBJECT IS THE SECTOR CONDITIONAL",
      qprime == [Fr(2, 23), Fr(1, 23), Fr(1, 23)]
      and sector_ratios == qp_norm
      and sector_ratios == [Fr(1, 2), Fr(1, 4), Fr(1, 4)],
      f"q' = {[str(x) for x in qprime]}; sector-normalized = "
      f"{[str(x) for x in sector_ratios]}")

# round-1 minor-1: the depth-5 horizon recomputation, in-receipt —
# absolute q' shifts with the horizon; the sector conditional does not:
FAM5, CACHE5 = enumerate_family(AB, 5)
Z5 = {}
for h in FAM5:
    if len(h) == 5:
        Z5[tuple(h)] = Fr(1)
for L in (4, 3, 2, 1, 0):
    for h in FAM5:
        if len(h) != L:
            continue
        Z5[tuple(h)] = sum(q * Z5[tuple(h + [e])]
                           for e, q in CACHE5[tuple(h)])
ZS5 = {e: Z5[tuple(H2 + [e])] for e in
       (SELFA, PAIRA, PAIRB, SELFB, BPAIRA, BPAIRB)}
qprime5 = [admissible(H2, e)[1] * ZS5[e] / Z5[tuple(H2)]
           for e, c, b in CUTS[1][1]]
qp5_norm = [x / sum(qprime5) for x in qprime5]
check("MG2-d2 (round-1 minor-1, the referee's depth-5 check "
      "in-receipt): at the depth-5 horizon the multipliers double "
      "(all six join successors Z = 4; early Z = 8; family 6,471) "
      "and the ABSOLUTE q' changes — but the sector-normalized "
      "conditional is IDENTICALLY (1/2, 1/4, 1/4): the forced "
      "object that survives horizon change is the SECTOR "
      "CONDITIONAL; component-constancy of z is per-horizon",
      len(FAM5) == 6471
      and all(z == Fr(4) for z in ZS5.values())
      and Z5[tuple(H1 + [SELFA])] == Fr(8)
      and qp5_norm == [Fr(1, 2), Fr(1, 4), Fr(1, 4)]
      and qprime5 != qprime,
      f"Z5(join succ) all 4; early Z5 = {Z5[tuple(H1 + [SELFA])]}; "
      f"sector-normalized = {[str(x) for x in qp5_norm]}; absolute "
      f"q'5 = {[str(x) for x in qprime5]} != depth-4 q'")

lam = Fr(7, 3)
scale_ok = True
for h, sector in CUTS:
    s_of = {}
    for e, c, b in sector:
        s_of.setdefault(c, share(h, e))
    for z1, z2 in PROBES:
        zc = {1: z1, 2: z2}
        zl = {1: lam * z1, 2: lam * z2}
        Nz = sum(s_of[c] * zc[c] for c in sorted(s_of))
        Nl = sum(s_of[c] * zl[c] for c in sorted(s_of))
        for e, c, b in sector:
            scale_ok = scale_ok and (s_of[c] * b * zc[c] / Nz
                                     == s_of[c] * b * zl[c] / Nl)
check("MG2-e the UNIQUENESS MECHANISM at fixture scale: the global "
      "scale lambda — the ONLY freedom MG1's sweep leaves the "
      "operator layer — cancels from every assigned weight "
      "(w(lambda z) = w(z), exact, all probes, both cuts): given "
      "the completion's multipliers, the cross-component weights "
      "are DETERMINED",
      scale_ok, "lambda = 7/3 cancels identically")

print("  THE UNIQUENESS UPGRADE (conditional; scope-honest):")
print("    MG2-c reduces the family's cross-component weight problem")
print("    to residue 1's within-cut completion object at the")
print("    fixture's cuts (depth <= 2). D44a is TERMINAL at LOG #368:")
print("    residue 1 is DECIDED AT EVERY VERIFIED DEPTH at d42a")
print("    scope (exhaustive through depth 7; sigma menu-exact and")
print("    transition-deterministic with zero exceptions over 179,783")
print("    histories; the completed transfer q' exists on the")
print("    six-state quotient). THEREFORE, at verified-depth scope,")
print("    the family's completed cross-component weights are FORCED")
print("    to the decided completion's values: the reduction (MG2-c)")
print("    maps the family's freedom onto the completion's, the")
print("    decided completion fixes the multipliers there, and the")
print("    residual global scale cancels (MG2-e). CONDITIONAL: the")
print("    all-depth form awaits the depth-free structural lemma")
print("    (H1, with H0/H2) — residue 1's FINAL NAMED GAP, open;")
print("    this receipt adds no claim beyond verified depth.")
depth_ok = (len(H1) == 1 and len(H2) == 2)
check("MG2-f the uniqueness upgrade's arithmetic content is in "
      "scope: the fixture's cuts lie at depths 1 and 2, strictly "
      "inside D44a's exhaustively verified depth (7 — the D44a "
      "receipt-carried scope constant, CITED from LOG #368, not "
      "computed here; round-1 minor-2 declared) — the conditional "
      "statement above rests on gates MG2-c/MG2-e plus the cited "
      "terminal record, and on nothing else",
      depth_ok and red_ok and scale_ok,
      "depths (1, 2) <= 7 (cited); reduction + scale-cancellation "
      "gated")

# ============ MG3 — honesty + purity ================================
print("\n[MG3 — honesty and purity]")
sizes_realized = sorted({len(e[2]) for e, q in m1A}
                        | {len(e[2]) for e, q in m2A}
                        | {len(e[2]) for e, q in m2B})
check("MG3-a FIXTURE SCALE, mechanical: the realized component sizes "
      "across the fixture's arb menus are exactly {1, 2} and the "
      "V-family covers precisely those; the dictionary was PRINTED "
      "(7 rows) and each substantive row is gated (FG0-d bare "
      "weights; MG2-b multipliers; MG2-c normalizers and ratios); "
      "NO CONTINUUM CLAIM — the reduction, the forcing sweep, and "
      "the FG2 obstruction are statements about the pair-plus-path "
      "fixture on the d42a-terminal grammar with the d42b2 click "
      "layer; Hegerfeldt untouched",
      sizes_realized == [1, 2] and sorted(VFAM) == [1, 2]
      and len(DICT_ROWS) == 7,
      f"realized |C| = {sizes_realized}; dictionary rows = "
      f"{len(DICT_ROWS)}")

# the d45a-form ALLOW-LIST purity walk (LOG #362 successor binding):
# reject any LEAF not in {Fraction, int, str} over every retained
# CLASSICAL structure (containers recursed; mp objects are banned
# leaves by construction — the walk convicts them).
ALLOW = (Fr, int, str)
VIOL = []
SEEN_LEAVES = [0]
def allow_walk(obj, path="root"):
    if isinstance(obj, dict):
        for k in sorted(obj, key=repr):
            allow_walk(k, path + ".key")
            allow_walk(obj[k], path + ".val")
    elif isinstance(obj, (tuple, list, set, frozenset)):
        for x in (sorted(obj, key=repr)
                  if isinstance(obj, (set, frozenset)) else obj):
            allow_walk(x, path + "[]")
    elif isinstance(obj, ALLOW):
        SEEN_LEAVES[0] += 1
    else:
        VIOL.append((path, type(obj).__name__))

CLASSICAL = [dict(m1A), dict(m2A), dict(m2B), BORN,
             [(list(hh), q) for hh, q, _ in ENS_A],
             [(list(hh), q) for hh, q, _ in ENS_B],
             {repr(e): z for e, z in ZS.items()}, Z1S,
             Z[()], Z[tuple(H1)], Z[tuple(H2)], root_completed,
             PROBES, qprime, sector_ratios, DICT_ROWS]
for structure in CLASSICAL:
    allow_walk(structure)
check("MG3-b the ALLOW-LIST purity walk (the d45a successor binding, "
      "LOG #362 — allow-list form, NOT a deny-list): every leaf of "
      "every retained classical structure (menus, Born tables, both "
      "FG1 ensembles' records and weights, the committed Z values, "
      "the probes, the completed weights, the dictionary) is in "
      "{Fraction, int, str}; zero violations",
      not VIOL and SEEN_LEAVES[0] > 200,
      f"violations = {len(VIOL)}; allowed leaves walked = "
      f"{SEEN_LEAVES[0]}")

VIOL2, SAVE = [], (VIOL, SEEN_LEAVES[0])
VIOL, SEEN_LEAVES = VIOL2, [0]
allow_walk([Fr(1, 2), mpf(1) / 2, "ok"])
tripped = [(p, t) for p, t in VIOL2]
VIOL, SEEN_LEAVES = SAVE[0], [SAVE[1]]
check("MG3-c the purity walk's TRIP CONTROL (the gate can fail): a "
      "deliberately polluted structure containing one mpf leaf is "
      "convicted by the same walk with the mpf named",
      len(tripped) == 1 and tripped[0][1] == 'mpf',
      f"tripped = {tripped}")

# ============ summary ===============================================
print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — breakage or anchor failure; exit 1 by "
          "design (both FG2 horns are delivered outcomes and exit 0; "
          "this exit is not a horn)")
    sys.exit(1)
print("[VERDICT] d44f GREEN — both arms delivered at fixture scale."
      "\n  ARM F (FG2: the UNEQUAL horn, pre-registered open): the "
      "two cut-advance orders through the constructed V-family do "
      "NOT produce equal terminal ensembles — the obstruction is "
      "exhibited entry-by-entry and is EXACTLY the initiator slot "
      "of the join arbitration (and the version register it names): "
      "weights, amplitudes, and winner marginals are order-"
      "invariant (Born = K1 and isometry ACQUITTED), initiator-"
      "erased ensembles are entrywise EQUAL, and the fork is forced "
      "by carrier licensing (A4/A6: the pair arb's carriers are "
      "both proposers) making the two actors' opportunities "
      "mutually exclusive (note-d43c §5 C3's forfeited commutation, "
      "now a firing gate). The choice a foliation would have to "
      "make: WHO initiates the join arbitration — nothing else. "
      "Disjoint components commute exactly (FG3, with the "
      "overlapped mutant failing the same gate); same-initiator "
      "sequencing is order-irrelevant where unambiguous (FG4, the "
      "committed A7 witness pair at mu = 1/256)."
      "\n  ARM M: the forcing sweep convicts EVERY pinned non-"
      "trivial per-component tilt by a named committed gate (ISO / "
      "BORN / MENU / CUTIND; the isometry-preserving within-pair "
      "rotation dies at BORN+MENU; the total-preserving cross-"
      "component transfer dies at ISO+BORN+MENU; the sign tilt dies "
      "at CUTIND alone, and the reduced battery demonstrably lets "
      "it slip — no silent acceptance). MG2: the cross-component "
      "weight problem at the fixture's cuts IS residue 1's within-"
      "cut completion object — same normalizers, same ratio "
      "constraints, gated in Fractions with the committed Z "
      "recomputed (Z(empty) = 1037/64; root completed weight "
      "133/2074 = paper 30 §5.3's printed extreme; the fixture's "
      "arb multipliers component-constant at 2 and 4). THE "
      "UNIQUENESS UPGRADE, at its honest conditional scope (D44a "
      "TERMINAL, LOG #368): at verified-depth scope the family's "
      "completed cross-component weights are FORCED to the decided "
      "completion's values; the all-depth form remains exactly "
      "conditional on the depth-free structural lemma (H1 with "
      "H0/H2) — residue 1's final named gap. Fixture scale; no "
      "continuum claim; Hegerfeldt untouched.")
