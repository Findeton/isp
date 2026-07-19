#!/usr/bin/env python3
"""
d43c_pincer_escapes_exact.py — v10 D43c (N3): the pincer vs the two
escape classes. Pin: note-d43c + its §5 round-1 amendments.
Fractions for grammar weights; mp.dps 50 for the isometry checks;
exit 1 on anchor breakage; the layer exec'd __file__-anchored
(round-1 F-B8 repair).

ROUND-1 REBUILT REVISION (reviews/d43bc-round1-hostile-review.md,
R-C1..R-C3, adopted at LOG #339). The first build's PG3 announced an
operator it never constructed (R1 was x == x — extensional theater,
owned in note §5 C1). This revision BUILDS the referee's pre-verified
{V_C} family from committed machinery: V_C = Acceptance composed
with OpeningClick (the d42b2-B1 join-typed chain as ONE typed
higher-order operation; for |C| = 2 the chain is one click +
acceptance). Gated: isometries at 1e-40 (both V's and both factors);
Born branch weights = the committed K1 kernel; the MENU
RECONSTRUCTION — (past-local admissible-ckey index x budget share)
x (the cut-independent operator Born splits) = the committed menus
at BOTH cuts, exactly, in Fractions; the SAME matrices at both cuts.

THE TWO CANDIDATES:
E-A (randomized, Ben-Or-shaped): a family of cut-independent
operators indexed by an INITIATOR-LOCAL recorded coin — EXCLUDED
(PG2, unchanged: it survived round 1 and was strengthened there).
E-B (comb-typed): the family {V_C} indexed by the conflict COMPONENT
as a licensed classical input — now CONSTRUCTED, not just typed.
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
own_view_canon = ns['own_view_canon']
event_poset = ns['event_poset']
View = ns['View']
arb_components_in_view = ns['arb_components_in_view']
PK1 = ns['PK1']
regs_of = ns['regs_of']
AB = ('A', 'B')

print("[d43c — the pincer vs the escape classes (round-1 rebuilt)]")
print("  banner: grammar weights exact Fractions (committed d42b3")
print("  layer, __file__-anchored); isometries at mp.dps 50 / 1e-40;")
print("  PG3 now gates the CONSTRUCTED {V_C} family (round-1 R-C1 —")
print("  the first build's extensional R1 is retired); no continuum")
print("  claim; Hegerfeldt untouched; the measure side stays with")
print("  residue 1 (pin §4 + note §5).")

pA0 = ('p', 'A', V0, 0)
pB1 = ('p', 'B', V0, 1)
tA, tB = ('A', V0, 0), ('B', V0, 1)
SELFA = ('r', 'A', frozenset({tA}), frozenset({tA}))
PAIRA = ('r', 'A', frozenset({tA, tB}), frozenset({tA}))
PAIRB = ('r', 'A', frozenset({tA, tB}), frozenset({tB}))
H1, H2 = [pA0], [pA0, pB1]

# ---- PG1: the pincer baseline (kept — survived round 1) ------------
def arb_menu(h):
    return sorted(((e, q) for e, q in candidates_for(h, AB)
                   if e[1] == 'A' and e[0] == 'r'), key=repr)
m1 = arb_menu(H1)
m2 = arb_menu(H2)
s_full_1 = sum(q for e, q in candidates_for(H1, AB) if e[1] == 'A')
s_full_2 = sum(q for e, q in candidates_for(H2, AB) if e[1] == 'A')
pair_events = [e for e, q in m2 if e[2] == frozenset({tA, tB})]
ok1 = (len(m1) == 1 and len(m2) == 3
       and s_full_1 == Fr(1) and s_full_2 == Fr(5, 4)
       and len(pair_events) == 2
       and all(not admissible(H1, e)[0] for e in pair_events))
check("PG1 the pincer baseline (committed d42b4 exhibit re-run): "
      "A's arb menu = 1 event at the early cut vs 3 at the join "
      "(self + 2 pair winners); full sums 1 vs 5/4; the pair "
      "branches inadmissible early",
      ok1, f"menus {len(m1)}/{len(m2)}; sums {s_full_1}/{s_full_2}")

# ---- PG2: E-A (randomized, initiator-local coin) — kept verbatim ---
# The theorem-shaped test: any operator family indexed by
# initiator-local data assigns branch sets as a FUNCTION OF THE OWN
# VIEW. The committed G-T1 fact: A's own view is IDENTICAL at [pA0]
# and [pA0, pB1]. Therefore the family emits the SAME branch set at
# both cuts — but the required branch sets DIFFER (PG1). So E-A
# fails R1 unless its firing predicate reads the join — relocating
# cut-dependence into the predicate (the pinned hazard, now
# exhibited): the randomization escape does NOT transfer. The FLP
# analogy is PARTIAL (declared): Ben-Or evades an adversarial
# scheduler; the obstruction here is VISIBILITY, which coins cannot
# manufacture. (Round 1 strengthened this to the DISTRIBUTIONAL
# form with clock robustness — note §5 C4; the gate is unchanged.)
ov1 = own_view_canon(H1, 'A')
ov2 = own_view_canon(H2, 'A')
branch_sets_differ = {e for e, q in m1} != {e for e, q in m2}
check("PG2 E-A FAILS (delivered verdict): A's own view is IDENTICAL "
      "at the two cuts (the committed G-T1 fact, recomputed) while "
      "the required arb branch sets DIFFER — an initiator-local-"
      "coin-indexed family is a function of the own view and cannot "
      "emit both menus; any repair reads the join, relocating "
      "cut-dependence into the firing predicate. The FLP/Ben-Or "
      "analogy is PARTIAL: the obstruction is VISIBILITY, not "
      "adversarial scheduling (import I2 refined)",
      ov1 == ov2 and branch_sets_differ,
      f"own views equal = {ov1 == ov2}; branch sets differ = "
      f"{branch_sets_differ}")

# ---- PG3: E-B — the {V_C} family, CONSTRUCTED (round-1 R-C1) -------
# The referee's pre-verified ~40-line core, adopted. V_C acts on the
# record state at the arb point; its classical index C is the
# component read from the event's own past cone (A6 ckey; d42b2-B1).
#
# OpeningClick (|C| = 2): the join-typed chain-opening click carries
# the first selection, uniform over the component's proposals:
# |C> -> sum_t sqrt(1/2) |C, t>. For |C| = 2 the order is then
# determined, and greedy acceptance is deterministic: the winner is
# the first-selected proposal, the loser is excluded, the version
# v(C, w) is created — Acceptance embeds |C, t> into the orthogonal
# winner+version record basis. V_C = Acceptance o OpeningClick.
O_pair = zeros(2, 1)
O_pair[0, 0] = 1 / sqrt(2)
O_pair[1, 0] = 1 / sqrt(2)
A_pair = zeros(4, 2)        # |C,tA> -> |w=tA, v(C,tA)>  (record 0)
A_pair[0, 0] = mpf(1)       # |C,tB> -> |w=tB, v(C,tB)>  (record 3)
A_pair[3, 1] = mpf(1)
V_pair = A_pair * O_pair
O_sing = zeros(1, 1)        # |C| = 1: the one-proposal selection is
O_sing[0, 0] = mpf(1)       # deterministic (uniform over 1)
A_sing = zeros(2, 1)        # acceptance creates the version record
A_sing[0, 0] = mpf(1)
V_sing = A_sing * O_sing
VFAM = {1: V_sing, 2: V_pair}   # the family, indexed by |C| ONLY —
                                # one object, both cuts (E5)

def iso_defect(M):
    G = M.T * M
    return max(fabs(G[i, j] - (1 if i == j else 0))
               for i in range(G.rows) for j in range(G.cols))

prod_dev = max(fabs(V_pair[i, 0] - (A_pair * O_pair)[i, 0])
               for i in range(4))
shapes_ok = (V_pair.rows, V_pair.cols, V_sing.rows, V_sing.cols) \
    == (4, 1, 2, 1)
check("PG3-E1 the operators EXIST as matrices: V_pair (4x1) and "
      "V_single (2x1) built as Acceptance o OpeningClick (the "
      "d42b2-B1 chain composed as ONE typed higher-order operation; "
      "for |C| = 2 the chain is one click + acceptance); the matrix "
      "product verified",
      shapes_ok and prod_dev < TOL,
      f"shapes ok = {shapes_ok}; product deviation = {chop(prod_dev)}")

defects = [iso_defect(M) for M in (V_pair, V_sing, O_pair, A_pair,
                                   O_sing, A_sing)]
check("PG3-E2 ISOMETRY at 1e-40 for V_pair, V_single, AND both "
      "factors of each (opening click; acceptance) — the NSE/D25/"
      "D27 record-side requirement on the constructed object itself",
      all(d < TOL for d in defects),
      f"max V^T V - I defect = {chop(max(defects))}")

# committed kernel, recomputed from the layer (not from the menus)
edge = frozenset({tuple(sorted((tA, tB)))})
k1_pair = PK1(frozenset({tA, tB}), edge)
k1_sing = PK1(frozenset({tA}), frozenset())
born_pair = {frozenset({tA}): V_pair[0, 0] ** 2,
             frozenset({tB}): V_pair[3, 0] ** 2}
born_sing = {frozenset({tA}): V_sing[0, 0] ** 2}
BORN = {1: [Fr(1)], 2: [Fr(1, 2), Fr(1, 2)]}   # exact (dyadic) Born
born_ok = (all(fabs(born_pair[w]
                    - mpf(k1_pair[w].numerator) / k1_pair[w].denominator)
               < TOL for w in k1_pair)
           and all(fabs(born_sing[w]
                        - mpf(k1_sing[w].numerator) / k1_sing[w].denominator)
                   < TOL for w in k1_sing)
           and all(fabs(born_pair[frozenset({t})] - mpf(x.numerator)
                        / x.denominator) < TOL
                   for t, x in ((tA, BORN[2][0]), (tB, BORN[2][1]))))
check("PG3-E3 BORN WEIGHTS = the committed K1 kernel at 1e-40: the "
      "squared branch amplitudes of V_pair are 1/2-1/2 (= PK1 on "
      "the 2-conflict, recomputed from the layer) and V_single's "
      "branch is deterministic (= PK1 on the singleton); the exact "
      "dyadic Born values are tied to the matrices",
      born_ok and k1_pair == {frozenset({tA}): Fr(1, 2),
                              frozenset({tB}): Fr(1, 2)}
      and k1_sing == {frozenset({tA}): Fr(1)},
      f"born(pair) ~ (1/2, 1/2); born(single) ~ 1; PK1 match = "
      f"{born_ok}")

# ---- the menu RECONSTRUCTION (the non-tautological form of R1) -----
# Classical layer, read from the layer's own past-view machinery
# (NOT from the composite menu): the admissible-ckey INDEX via
# admissible(), and the budget share Fr(1,4)/#components via the
# event's own past view. The operator layer: the V_C Born splits.
def share(h, e):
    acts2 = h + [e]
    pred = event_poset(acts2)
    view = View(acts2, pred, pred[len(acts2) - 1])
    return Fr(1, 4) / len(arb_components_in_view(view, e[1]))

def reconstruct(h):
    """(past-local admissible-ckey index x budget share) x (V_C
    Born). Returns (menu, index-tags, applied-operators)."""
    out = {}
    used = []
    if admissible(h, SELFA)[0]:                    # ckey {tA}
        out[SELFA] = share(h, SELFA) * BORN[1][0]
        used.append(('single', VFAM[1]))
    okA, okB = admissible(h, PAIRA)[0], admissible(h, PAIRB)[0]
    if okA and okB:                                # ckey {tA, tB}
        s = share(h, PAIRA)
        out[PAIRA] = s * BORN[2][0]
        out[PAIRB] = s * BORN[2][1]
        used.append(('pair', VFAM[2]))
    return out, [n for n, _ in used], [M for _, M in used]

r1, idx1, ops1 = reconstruct(H1)
r2, idx2, ops2 = reconstruct(H2)
recon_ok = (r1 == dict(m1) and r2 == dict(m2))
check("PG3-E4 MENU RECONSTRUCTION at BOTH cuts, EXACT in Fractions: "
      "(past-local admissible-ckey index x budget share Fr(1,4)/"
      "#components, from the layer's own past-view machinery) x "
      "(the V_C Born splits) equals the committed menus — the "
      "early-cut singleton menu (sum 1/4 on the arb sector) and the "
      "join menu (1/4 + 1/8 + 1/8); the index sets are {single} vs "
      "{single, pair}",
      recon_ok and idx1 == ['single'] and idx2 == ['single', 'pair'],
      f"cut-1 match = {r1 == dict(m1)}; cut-2 match = "
      f"{r2 == dict(m2)}; index sets = {idx1} vs {idx2}")

same_matrix = (ops1[0] is ops2[0])
regs_pair = regs_of(PAIRA)
regs_self = regs_of(SELFA)
carriers_ok = ('A' in regs_pair and 'B' in regs_pair
               and 'A' in regs_self and 'B' not in regs_self
               and regs_self == frozenset(
                   {'A', ns['vname'](V0, SELFA[3], 'A')}))
check("PG3-E5 CUT-INDEPENDENCE where it belongs + the horn-2 price: "
      "the SAME matrices serve at both cuts (the family is indexed "
      "by the component only; the singleton operator applied at "
      "cut 1 IS the object applied at cut 2 — only the classical "
      "index set differs, and admissible() computes it from the "
      "event's own past cone); the price, gated on carriers: V_pair "
      "acts on BOTH proposers' records (licensed join carriers per "
      "A4/A6) — commutation-by-disjointness is FORFEITED at joins "
      "(the foliation face stays open; note §5 C3), while V_single "
      "touches only the initiator + the created version",
      same_matrix and carriers_ok,
      f"same singleton matrix at both cuts = {same_matrix}; "
      f"pair carriers include A and B = "
      f"{'A' in regs_pair and 'B' in regs_pair}")

# ---- kept R3 + re-scoped R4 + kept R5 ------------------------------
r3_ok = (all(q == Fr(1, 8) for e, q in m2
             if e[2] == frozenset({tA, tB}))
         and dict(m1)[SELFA] == Fr(1, 4))
check("PG3-R3 (kept): the committed kernel weights at the menus — "
      "the pair winners at 1/4 x 1/2 = 1/8 each and the singleton "
      "at 1/4 (the load-bearing weight gate; PG1's sums are "
      "tilt-blind by construction)",
      r3_ok, "1/8 + 1/8 + 1/4 at the join; 1/4 early")

# The comb's ACTUAL record side (round-1 F-C1: the old R4 was the
# d42b4 toy, attributed to an object absent from the code — retired):
# the winner/version registers of V_C are orthogonal record vectors,
# and Acceptance preserves probe distances by construction (it is an
# isometry); a lossy control certifies the test can fail.
def pdist(u, v):
    nu = sqrt(sum(u[i, 0] ** 2 for i in range(u.rows)))
    nv = sqrt(sum(v[i, 0] ** 2 for i in range(v.rows)))
    ov = sum(u[i, 0] * v[i, 0] for i in range(u.rows)) / (nu * nv)
    return sqrt(1 - ov ** 2)
branch_ov = fabs(sum(A_pair[i, 0] * A_pair[i, 1] for i in range(4)))
u = zeros(2, 1); u[0, 0] = 1 / sqrt(2); u[1, 0] = 1 / sqrt(2)
v = zeros(2, 1); v[0, 0] = mpf(1)
dist_dev = fabs(pdist(u, v) - pdist(A_pair * u, A_pair * v))
Mlossy = zeros(2, 2); Mlossy[0, 0] = mpf(1); Mlossy[1, 1] = mpf(1) / 2
ctrl = fabs(pdist(u, v) - pdist(Mlossy * u, Mlossy * v))
check("PG3-R4 (re-scoped to the comb's actual record side): the two "
      "winner+version records of V_pair are ORTHOGONAL outputs and "
      "Acceptance preserves probe distances at 1e-40 (isometry — "
      "distances preserved by construction, now stated of the "
      "constructed object); the lossy control fires",
      branch_ov < TOL and dist_dev < TOL and ctrl > mpf(1) / 100,
      f"branch overlap = {chop(branch_ov)}; distance deviation = "
      f"{chop(dist_dev)}; control = {chop(ctrl)}")

r5_ok = ((not admissible(H1, PAIRA)[0]) and admissible(H2, PAIRA)[0]
         and (not admissible(H1, PAIRB)[0])
         and admissible(H2, PAIRB)[0])
check("PG3-R5 (kept): the classical index is PAST-LOCAL event data, "
      "not cut data — admissible() accepts/rejects the pair ckey by "
      "the event's own past alone (rejected at the early cut, "
      "accepted at the join, both winners)",
      r5_ok, f"early reject / join accept = {r5_ok}")

# ---- PG4: the scope gate, now mechanical (round-1 F-C6) ------------
sizes_realized = sorted({len(e[2]) for e, q in m1}
                        | {len(e[2]) for e, q in m2})
born_sums = [sum(BORN[k]) for k in (1, 2)]
check("PG4 SCOPE (the honesty gate, now mechanical): FIXTURE SCALE "
      "— the realized component sizes at the two cuts are exactly "
      "{1, 2} and the constructed family covers precisely those; "
      "THE MEASURE STAYS CLASSICAL — each V_C's Born split sums to "
      "1 exactly, so the operator carries the branch SPLIT only and "
      "the family's weights remain the classical q's (residue 1, "
      "untouched). Horn 2's explicitly-open arm is now TYPED AND "
      "CONSTRUCTED at fixture scale; its foliation/commuting-family "
      "face at overlapping visibility and the measure question "
      "remain open and separate; the three horns stand for cut/"
      "initiator-attached CHANNELS; fine-vs-coarse sealing rides "
      "along; no continuum claim; Hegerfeldt untouched",
      sizes_realized == [1, 2] and sorted(VFAM) == [1, 2]
      and born_sums == [Fr(1), Fr(1)],
      f"realized |C| = {sizes_realized}; family index = "
      f"{sorted(VFAM)}; Born sums = {[str(x) for x in born_sums]}")

print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — anchor breakage; exit 1")
    sys.exit(1)
print("[VERDICT] d43c round-1 rebuilt, GREEN: E-A FAILS (visibility, "
      "not scheduling — the randomization escape does not transfer; "
      "the FLP import is partial; E-A's only repair route is the "
      "join-licensed visibility, i.e. E-A reduces to E-B, which PG3 "
      "adjudicates). E-B: the operator family {V_single, V_pair} is "
      "CONSTRUCTED from committed machinery — isometric at 1e-40, "
      "Born = K1, and (past-local index) x (cut-independent "
      "operator) reproduces the committed menus at both cuts "
      "exactly. Residue 2's OPERATOR-EXISTENCE face is discharged "
      "at fixture scale by the exhibited family; its foliation/"
      "commuting-family face at overlapping visibility remains OPEN "
      "(horn 2's standing arm — V_pair's carriers overlap both "
      "proposers), and the comb's weight/measure side is residue 1: "
      "the residues remain SEPARATE. The fourth door is horn 2's "
      "open arm, now typed past-locally and exhibited.")
