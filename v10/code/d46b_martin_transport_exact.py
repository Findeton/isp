#!/usr/bin/env python3
"""
d46b_martin_transport_exact.py — v10 D46b (ladder step b): [I1]
Martin/R-theory at transport scope.  Pin:
note-d46b-martin-at-transport.md (strict).  Parents: D44b TERMINAL
#374 (the transport chain ESCAPES its windows — [I1] named as THE
successor); D44a TERMINAL #368 (the delivery-free decision this
probes the edge of); the d44f horizon lesson (LOG #370: the
horizon-stable object is the SECTOR CONDITIONAL, not the absolute
completed weight).

ROUND-1 REPAIRED REVISION (v10/reviews/d46bd-round1-hostile-review.md).
Two of the four first-pass headlines REVERSE under the referee's
recomputation and are delivered here in their corrected form:

  * B-A1 / MB5 REVERSES.  The first pass compared a remaining-horizon-4
    root kernel with a remaining-horizon-1 witness kernel through an
    ABSOLUTE-depth potential.  At MATCHED remaining horizon the
    witness's per-kind sector masses are EXACTLY the root's at
    r = 1, 2, 3.  The transport analogue of root = renewal is
    SUPPORTED in sector mass at this scope, not refuted.
  * B-A2 / MB4 REVERSES.  lambda = 2 is the delivery-free chain's
    Perron EIGENVALUE and is not comparable with a finite-horizon
    ratio; the delivery-free family's OWN finite-horizon ratios,
    rebuilt here from the committed d42b3 layer, are UNIFORMLY LARGER
    than transport's (G_4 = 1037/64 vs 1035/64), so "deliveries add
    branching" had the wrong sign; and the transport ratio PEAKS at
    D = 5 and turns down at D = 6, so "RISES" is false.
  * B-M2.  The pin's MB3 object is the SECTOR-NORMALIZED CONDITIONAL;
    the first pass substituted sector MASSES.  The pinned object is
    computed here: it is EXACTLY horizon-stable at the root (r = 1..6,
    drift 0 — partly a symmetry artifact, stated) and contracts
    uniformly off it.
  * B-M3.  "~0.738 per level" was one datum; the ratio SEQUENCE is
    reported, and the contraction claim is STRENGTHENED (credit: the
    referee) to three norms out to D = 6 and to a family-uniform
    sequence at fixed relative horizon.
  * B-A3 / B-M1 / B-m5 / B-n1.  The three tautological gates are gone;
    the witness is identified, not merely priced; the vacuity scan is
    an AST scan of every gate predicate; the [VERDICT] is assembled
    from the delivered outcomes and cannot contradict them.

GREEN-UNREVIEWED — round 1 is in hand and applied; the unit is not
review-hardened until its round converts (paper-32's round precedes
it).
"""
import ast
import os
import sys
from fractions import Fraction as Fr

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

OUT = []
def outcome(tag, text):
    OUT.append((tag, text))
    print(f"  [OUTCOME {tag}] {text}")

print("[d46b — Martin/R-theory at transport scope]")
print("  banner: GREEN-UNREVIEWED, ROUND-1 REPAIRED.  Round 1")
print("  (d46bd-round1-hostile-review.md) reversed MB5 and MB4 and")
print("  found the pin's MB3 object uncomputed; all three are")
print("  delivered here in corrected form, with the referee's")
print("  strengthened contraction result gated.  Not citable as")
print("  review-hardened until the round converts (paper-32 first).")
print("  EXACT Fractions everywhere; the committed d42b1 transport")
print("  layer and the committed d42b3 delivery-free layer are both")
print("  exec'd path-anchored, so the two families are compared")
print("  like-for-like.  NO infinite-volume and NO boundary-existence")
print("  claim: this unit computes finite-horizon potentials, their")
print("  kernel candidates at MATCHED REMAINING HORIZON, and the")
print("  exact horizon-stability verdict at the reachable caps —")
print("  nothing more.  The d44f lesson binds the reading and names")
print("  the object: the SECTOR-NORMALIZED CONDITIONAL, not the")
print("  absolute completed weight, is the candidate physical object.")

_SRC = 'v10/code/d42b1_transport_exact.py'
_src = open(_SRC).read()
ns = {}
exec(_src[:_src.index('print("[d42b1')], ns)
V0 = ns['V0']
candidates_for = ns['candidates_for']
AB = ('A', 'B')

# ---- MB0: the family and its census ---------------------------------
# Round-1 B-A1 needs kernels at MATCHED REMAINING horizon r for a
# depth-3 witness, i.e. menus to depth 5; B-A2 needs G_6.  The family
# is therefore built one level deeper than the first pass (CAP = 5),
# and the committed depth-4 census is re-anchored inside it.
CAP = 5
COMMITTED_CAP = 4
CACHE = {}
frontier = [()]
while frontier:
    h = frontier.pop()
    CACHE[h] = candidates_for(list(h), AB)
    if len(h) >= CAP:
        continue
    for e, q in CACHE[h]:
        frontier.append(h + (e,))
lev = {}
for h in CACHE:
    lev[len(h)] = lev.get(len(h), 0) + 1
cum = [sum(lev[j] for j in range(k + 1)) for k in range(CAP + 1)]
check("MB0 the committed ARM-1T family re-anchored from the layer and "
      "extended one level: cumulative sizes "
      "[1, 9, 69, 521, 3969, 30729] — the first five are the "
      "D44b/d42b1 census, the sixth is the extension round 1 (B-A1, "
      "B-A2) requires, since a matched-remaining-horizon comparison "
      "at a depth-3 witness and the D = 6 potential both need menus "
      "at depth 5",
      cum == [1, 9, 69, 521, 3969, 30729],
      f"cumulative = {cum}; per level = {[lev[k] for k in sorted(lev)]}")

# order-independence (the pin's MB6 'determinism', B-m2: the first
# pass claimed 'seeds byte-identical' in a receipt with no seeds).
# This receipt is seedless; what determinism MEANS here is that the
# family and its menus do not depend on the traversal order.  Rebuilt
# by BFS (the referee's independent order) to the committed cap and
# compared menu-for-menu.
bfs = {}
layer = [()]
while layer:
    nxt = []
    for h in layer:
        bfs[h] = candidates_for(list(h), AB)
        if len(h) < COMMITTED_CAP:
            for e, q in bfs[h]:
                nxt.append(h + (e,))
    layer = nxt
same_keys = set(bfs) == {h for h in CACHE if len(h) <= COMMITTED_CAP}
same_menus = same_keys and all(bfs[h] == CACHE[h] for h in bfs)
check("MB0-b DETERMINISM (order-independence), the pin's MB6 promise "
      "delivered instead of asserted: the receipt carries NO seed and "
      "NO sampling, so the operative determinism claim is that the "
      "family and every per-history menu are independent of the "
      "traversal order; the depth-4 family is rebuilt BFS (the "
      "referee's order) and compared menu-for-menu, weights included, "
      "against the stack-built cache",
      same_keys and same_menus and len(bfs) == 3969,
      f"BFS histories = {len(bfs)}; key sets agree = {same_keys}; "
      f"menus identical = {same_menus}")

# ---- MB1: the transport ladder (menu weight sums) -------------------
def census_of(cache, upto):
    s = {}
    for h in cache:
        if len(h) > upto:
            continue
        k = str(sum(q for e, q in cache[h]))
        s[k] = s.get(k, 0) + 1
    return s

cen4 = census_of(CACHE, COMMITTED_CAP)
cen5 = census_of(CACHE, CAP)
check("MB1 THE TRANSPORT LADDER: the exact per-history menu weight "
      "sum takes finitely many values, censused with multiplicities "
      "AT THE COMMITTED CAP (round 1 B-m3: the multiplicities are "
      "cap-bound and are labelled so) and again one level deeper — "
      "the value set is unchanged by the extension, which is the "
      "content of the claim",
      cen4 == {'2': 3757, '5/2': 212}
      and cen5 == {'2': 29605, '5/2': 1124}
      and set(cen4) == set(cen5),
      f"depth <= 4: {cen4}; depth <= 5: {cen5}")

# B-m6: the 'exactly the delivery-free values' comparison was made in
# prose against a hard-coded self-anchor.  The delivery-free family is
# rebuilt here from the committed d42b3 layer (the layer d43b/D44a
# run on) and censused, so the comparison is computed.
_SRC3 = 'v10/code/d42b3_placement_exact.py'
_src3 = open(_SRC3).read()
ns3 = {}
exec(_src3[:_src3.index('print("[d42b3')], ns3)
cf3 = ns3['candidates_for']
DF = {}
fr3 = [()]
while fr3:
    h = fr3.pop()
    DF[h] = cf3(list(h), AB)
    if len(h) >= CAP:
        continue
    for e, q in DF[h]:
        fr3.append(h + (e,))
dlev = {}
for h in DF:
    dlev[len(h)] = dlev.get(len(h), 0) + 1
dcum = [sum(dlev[j] for j in range(k + 1)) for k in range(CAP + 1)]
dcen = census_of(DF, CAP)
check("MB1-b THE DELIVERY-FREE LADDER RECOMPUTED, not cited (round 1 "
      "B-m6): the delivery-free family is rebuilt from the committed "
      "d42b3 placement layer to the same depth — cumulative "
      "[1, 7, 39, 215, 1191, 6471] (the d43b MG0 census) — and its "
      "own menu-weight-sum census is taken; the transport claim is "
      "then the computed statement that the two VALUE SETS coincide, "
      "{2, 5/2}, with different multiplicities",
      dcum == [1, 7, 39, 215, 1191, 6471]
      and dcen == {'2': 5963, '5/2': 508}
      and set(dcen) == set(cen5) == {'2', '5/2'},
      f"delivery-free cumulative = {dcum}; census = {dcen}; value "
      f"sets equal = {set(dcen) == set(cen5)}")

# ---- MB2: the finite-horizon potentials, BOTH families --------------
# Round-1 B-A2: the potential must be a RELATIVE-horizon object if it
# is to be compared across states (and across families) at all.
# G(h, r) = total admissible weight of h's subtree to REMAINING depth
# r (G(h, 0) = 1; else sum_e q(e|h) G(h + e, r - 1)).  At the root,
# G(root, D) is the first pass's G_D.
def rel_potential(cache):
    memo = {}
    def G(h, r):
        if r == 0:
            return Fr(1)
        key = (h, r)
        if key not in memo:
            memo[key] = sum(q * G(h + (e,), r - 1) for e, q in cache[h])
        return memo[key]
    return G

GT = rel_potential(CACHE)
GD = rel_potential(DF)
ROOT = ()
tG = [GT(ROOT, r) for r in range(1, CAP + 2)]
dG = [GD(ROOT, r) for r in range(1, CAP + 2)]
TG_REF = [Fr(2), Fr(4), Fr(257, 32), Fr(1035, 64), Fr(4173, 128),
          Fr(134587, 2048)]
DG_REF = [Fr(2), Fr(4), Fr(257, 32), Fr(1037, 64), Fr(2101, 64),
          Fr(68313, 1024)]
check("MB2 THE TRANSPORT FINITE-HORIZON POTENTIALS at the root, "
      "exact, D = 1..6 by backward recursion — the first pass "
      "stopped at D = 4 and read a two-point trend (round 1, B-A2 "
      "defect 3); the sequence is anchored value by value",
      tG == TG_REF,
      "; ".join(f"G_{i + 1} = {v}" for i, v in enumerate(tG)))
check("MB2-b THE DELIVERY-FREE FINITE-HORIZON POTENTIALS at the same "
      "root and the same horizons, computed from the committed d42b3 "
      "layer — the like-for-like partner the first pass never built.  "
      "Round-1 B-m1: the two families are NUMERICALLY IDENTICAL "
      "through D = 3 and first separate at D = 4 (1035/64 transport "
      "vs 1037/64 delivery-free), i.e. deliveries are invisible to "
      "the potential below depth 4 — a finding in its own right",
      dG == DG_REF and dG[:3] == tG[:3] and dG[3] != tG[3],
      "; ".join(f"G_{i + 1} = {v}" for i, v in enumerate(dG))
      + f"; first separation at D = 4")

# ---- MB4: the growth ratios, BOTH families side by side -------------
print("\n[MB4 — finite-horizon growth, transport vs delivery-free]")
tR = [tG[i] / tG[i - 1] for i in range(1, len(tG))]
dR = [dG[i] / dG[i - 1] for i in range(1, len(dG))]
print("      D | delivery-free G_D | transport G_D | df ratio | "
      "transport ratio")
for i in range(len(tG)):
    rr = (f"{dR[i - 1]} (~{float(dR[i - 1]):.6f}) | "
          f"{tR[i - 1]} (~{float(tR[i - 1]):.6f})") if i else "— | —"
    print(f"      {i + 1} | {dG[i]} | {tG[i]} | {rr}")
TR_REF = [Fr(2), Fr(257, 128), Fr(1035, 514), Fr(1391, 690),
          Fr(134587, 66768)]
DR_REF = [Fr(2), Fr(257, 128), Fr(1037, 514), Fr(2101, 1037),
          Fr(68313, 33616)]
check("MB4 THE GROWTH RATIOS OF BOTH FAMILIES, exact and side by "
      "side (round 1, B-A2, prescribed fix): the successive "
      "finite-horizon ratios G_D(root)/G_(D-1)(root) at D = 2..6 for "
      "the transport family AND for the delivery-free family, each "
      "value anchored.  NOTE THE CATEGORY DISTINCTION the first pass "
      "violated: D44a's lambda = 2 is the delivery-free transfer's "
      "PERRON EIGENVALUE, i.e. the D -> infinity limit of the "
      "delivery-free column; it is not a finite-horizon quantity and "
      "no finite-horizon ratio may be compared with it",
      tR == TR_REF and dR == DR_REF,
      "transport = " + ", ".join(str(x) for x in tR)
      + "; delivery-free = " + ", ".join(str(x) for x in dR))
df_ge = all(dR[i] >= tR[i] for i in range(len(tR)))
df_strict = [i + 2 for i in range(len(tR)) if dR[i] > tR[i]]
peak = max(range(len(tR)), key=lambda i: tR[i])
turns = tR[-1] < tR[-2] and tR[-2] > tR[-3]
check("MB4-b THE SIGN AND THE TURNOVER, the two facts that reverse "
      "the first pass's headline: (i) at every horizon the "
      "DELIVERY-FREE ratio is >= the transport ratio, strictly so "
      "from D = 4 on, so at the reachable caps deliveries REDUCE "
      "finite-horizon branching rather than adding it; (ii) the "
      "transport ratio is not monotone — it PEAKS at D = 5 and turns "
      "down at D = 6, so the first pass's 'RISES' was a two-point "
      "read that reverses at the next horizon",
      df_ge and df_strict == [4, 5, 6] and peak == 3 and turns,
      f"delivery-free >= transport at every D = {df_ge}; strictly "
      f"larger at D = {df_strict}; transport peak at D = {peak + 2} "
      f"(~{float(tR[peak]):.6f}); D = 6 ratio ~{float(tR[-1]):.6f} "
      f"< D = 5")
outcome("MB4", "THE GROWTH READING, CORRECTED (round 1 B-A2). The "
        "transport finite-horizon growth ratios are 257/128, "
        "1035/514, 1391/690, 134587/66768 — all slightly above 2, "
        "PEAKING at D = 5 and turning over by D = 6. The "
        "delivery-free family's own finite-horizon ratios at the same "
        "horizons (257/128, 1037/514, 2101/1037, 68313/33616) are "
        "UNIFORMLY LARGER, so at the reachable caps DELIVERIES REDUCE "
        "finite-horizon branching; the first pass's 'deliveries add "
        "branching' had the wrong sign, and its comparison of a "
        "finite-horizon ratio with the asymptotic eigenvalue "
        "lambda = 2 was a category error. No statement is made about "
        "either family's D -> infinity growth: that is exactly what "
        "the caps withhold.")

# ---- MB3: THE MARTIN-KERNEL CANDIDATES, at MATCHED horizon ----------
print("\n[MB3 — the kernel candidates at matched remaining horizon]")
# Round-1 B-A1: the first pass's kernel(G_D, h) used an ABSOLUTE depth
# cap, so k(.|h) at a depth-L history carried remaining horizon D - L.
# Every comparison across states was therefore a comparison across
# horizons.  The horizon-invariant object — the one the d44f lesson
# names — is the RELATIVE-horizon kernel.
def krel(cache, G, h, r):
    """k_r(e | h) = q(e|h) G(h + e, r - 1) / G(h, r): the completed
    transfer of h's subtree at REMAINING horizon r.  Sums to 1 by
    construction of G."""
    tot = G(h, r)
    return {e: q * G(h + (e,), r - 1) / tot for e, q in cache[h]}

def sector(k):
    s = {}
    for e, v in k.items():
        s[e[0]] = s.get(e[0], Fr(0)) + v
    return s

def conditional(k):
    """THE PINNED OBJECT (note §2 MB3; the d44f lesson, LOG #370):
    the SECTOR-NORMALIZED CONDITIONAL k(e) / sector-mass(kind(e)) —
    NOT the sector mass, which is what the first pass substituted."""
    s = sector(k)
    return {e: v / s[e[0]] for e, v in k.items()}

RK = [krel(CACHE, GT, ROOT, r) for r in range(1, CAP + 2)]
root_proper = all(sum(k.values()) == 1 for k in RK)
fam_proper_r1 = all(sum(krel(CACHE, GT, h, 1).values()) == 1
                    for h in CACHE)
fam_proper_r2 = all(sum(krel(CACHE, GT, h, 2).values()) == 1
                    for h in CACHE if len(h) <= 4)
check("MB3-a THE KERNEL CANDIDATES ARE PROPER — and not only at the "
      "root (round 1, B-M4: the first pass measured properness at "
      "h = [] alone and wrote 'the kernel candidates' in the plural): "
      "k_r(.|root) sums to EXACTLY 1 at every remaining horizon "
      "r = 1..6, and k_r(.|h) sums to exactly 1 at EVERY history in "
      "the family at r = 1 (30,729 histories) and at every history "
      "with a computable r = 2 (3,969)",
      root_proper and fam_proper_r1 and fam_proper_r2,
      f"root r = 1..6 proper = {root_proper}; family-wide r = 1 "
      f"proper = {fam_proper_r1} (30729 histories); family-wide "
      f"r = 2 proper = {fam_proper_r2} (3969 histories)")

SM = [sector(k) for k in RK]
for i, s in enumerate(SM):
    print(f"    root sector masses at remaining horizon r = {i + 1}: "
          f"{ {kk: str(vv) for kk, vv in sorted(s.items())} }")
abs_drift = [max(abs(RK[i][e] - RK[i - 1][e]) for e in RK[0])
             for i in range(1, len(RK))]
l1_drift = [sum(abs(RK[i][e] - RK[i - 1][e]) for e in RK[0])
            for i in range(1, len(RK))]
sec_drift = [max(abs(SM[i][kk] - SM[i - 1][kk]) for kk in SM[0])
             for i in range(1, len(SM))]
AD_REF = [Fr(0), Fr(1, 1028), Fr(191, 265995), Fr(412, 1439685),
          Fr(4629, 187210517)]
L1_REF = [Fr(0), Fr(3, 514), Fr(382, 88665), Fr(824, 479895),
          Fr(27774, 187210517)]
SD_REF = [Fr(0), Fr(3, 1028), Fr(191, 88665), Fr(412, 479895),
          Fr(13887, 187210517)]
check("MB3-b THE ABSOLUTE KERNEL AND THE SECTOR MASSES DO DRIFT with "
      "the remaining horizon, exactly and at every one of the five "
      "reachable steps r -> r + 1, in all three norms (L-infinity, "
      "L1, sector-L-infinity); each drift is anchored to its exact "
      "rational.  The r = 1 -> 2 step is exactly ZERO in all three, "
      "so of the five steps only four carry any absolute drift at "
      "all (round 1, B-M3)",
      abs_drift == AD_REF and l1_drift == L1_REF
      and sec_drift == SD_REF,
      "L-inf = " + ", ".join(str(x) for x in abs_drift)
      + "; L1 = " + ", ".join(str(x) for x in l1_drift)
      + "; sector-L-inf = " + ", ".join(str(x) for x in sec_drift))

# ---- MB3-c: THE PINNED OBJECT, computed at last ---------------------
CD = [conditional(k) for k in RK]
cond_drift = [max(abs(CD[i][e] - CD[i - 1][e]) for e in CD[0])
              for i in range(1, len(CD))]
cond_stable = all(d == 0 for d in cond_drift)
print(f"    root SECTOR-NORMALIZED CONDITIONAL, drift across "
      f"r = 1..6: {[str(d) for d in cond_drift]}")
check("MB3-c THE PIN'S OBJECT, COMPUTED (round 1, B-M2: the first "
      "pass named the SECTOR-NORMALIZED CONDITIONAL in its pin and "
      "then measured sector MASSES instead, reporting a negative "
      "where its own pinned object gives an exact positive).  At the "
      "root the conditional k_r(e)/sector-mass(kind(e)) is EXACTLY "
      "IDENTICAL at every remaining horizon r = 1..6 — drift exactly "
      "0 at all five steps, not small but zero.  HONESTY CAVEAT, "
      "gated by MB3-d below: at the root all options within a sector "
      "are exchangeable, which FORCES a uniform conditional at every "
      "horizon, so the root's exactness is partly a symmetry "
      "artifact and the off-root behaviour is the real test",
      cond_stable and len(cond_drift) == 5
      and cond_drift == [Fr(0)] * 5,
      f"conditional drift at r -> r+1 for r = 1..5 = "
      f"{[str(d) for d in cond_drift]}; horizon-stable = "
      f"{cond_stable}")

# off-root: does the conditional survive away from the symmetry point?
off_sup, off_n, off_drifters = [], [], []
for r in (1, 2, 3, 4):
    best, n, nd = Fr(0), 0, 0
    for h in CACHE:
        if len(h) + r > CAP:
            continue
        n += 1
        a, b = conditional(krel(CACHE, GT, h, r)), \
            conditional(krel(CACHE, GT, h, r + 1))
        d = max(abs(b[e] - a[e]) for e in a)
        if d:
            nd += 1
        if d > best:
            best = d
    off_sup.append(best)
    off_n.append(n)
    off_drifters.append(nd)
OFF_REF = [Fr(1, 18), Fr(4, 171), Fr(8, 741), Fr(176, 32877)]
off_contracts = all(off_sup[i] < off_sup[i - 1]
                    for i in range(1, len(off_sup)))
check("MB3-d THE CONDITIONAL OFF THE ROOT, the honest half of MB3-c: "
      "the SUPREMUM over the whole family of the conditional's drift "
      "at fixed RELATIVE horizon is exact and CONTRACTS — 1/18, "
      "4/171, 8/741, 176/32877 at r = 1->2 .. 4->5 — and only a "
      "minority of histories carry any conditional drift at all.  So "
      "the correct statement is: the d44f conditional is exactly "
      "horizon-stable at the root by symmetry, and contracts "
      "uniformly off it",
      off_sup == OFF_REF and off_contracts
      and off_drifters == [700, 140, 36, 4]
      and off_n == [3969, 521, 69, 9],
      "; ".join(f"r={i + 1}->{i + 2}: sup {off_sup[i]} "
                f"(~{float(off_sup[i]):.3e}) over {off_n[i]} "
                f"histories, {off_drifters[i]} with any drift"
                for i in range(4)))
outcome("MB3", "THE HORIZON-STABILITY READING, CORRECTED (round 1 "
        "B-M2). The object the pin and the d44f lesson name — the "
        "SECTOR-NORMALIZED CONDITIONAL — is EXACTLY horizon-stable "
        "at the root: identical at r = 1..6, drift exactly 0, which "
        "at the root is partly forced by within-sector "
        "exchangeability. Off the root it does drift, and its "
        "family-wide supremum CONTRACTS (1/18, 4/171, 8/741, "
        "176/32877), with only 700 of 3,969 histories carrying any "
        "conditional drift at the first step. What DOES drift at "
        "every horizon is the absolute kernel and the per-kind "
        "sector MASS — exactly the horizon-bound quantities d44f "
        "predicts. The first pass reported 'the finite-horizon "
        "kernel has not stabilized' by measuring the horizon-bound "
        "object; on the pinned object the verdict is positive.")

# ---- MB3-e: the contraction, in three norms and family-wide --------
ratios = [(abs_drift[i] / abs_drift[i - 1]) if abs_drift[i - 1] else None
          for i in range(1, len(abs_drift))]
l1_ratios = [(l1_drift[i] / l1_drift[i - 1]) if l1_drift[i - 1] else None
             for i in range(1, len(l1_drift))]
sec_ratios = [(sec_drift[i] / sec_drift[i - 1]) if sec_drift[i - 1]
              else None for i in range(1, len(sec_drift))]
norm_free = (ratios == l1_ratios == sec_ratios)
seq = [r for r in ratios if r is not None]
monotone = all(abs_drift[i] < abs_drift[i - 1]
               for i in range(2, len(abs_drift)))
print(f"    root drift ratios (L-inf): "
      f"{[f'{float(r):.4f}' for r in seq]}  — a SEQUENCE, not a rate")
uni_sup = []
for r in (1, 2, 3, 4):
    best = Fr(0)
    for h in CACHE:
        if len(h) + r + 1 > CAP + 1:
            continue
        a, b = krel(CACHE, GT, h, r), krel(CACHE, GT, h, r + 1)
        d = max(abs(b[e] - a[e]) for e in a)
        if d > best:
            best = d
    uni_sup.append(best)
UNI_REF = [Fr(3, 110), Fr(3, 253), Fr(373, 69230), Fr(2333, 1838829)]
uni_contracts = all(uni_sup[i] < uni_sup[i - 1]
                    for i in range(1, len(uni_sup)))
check("MB3-e THE CONTRACTION, STRENGTHENED (credit: round 1's "
      "referee, B-M3 'Standing').  The first pass read a single "
      "ratio ~0.738 as a per-level RATE; there are three horizons "
      "there, hence two drifts, hence exactly ONE ratio.  Extended "
      "and gated here in the strong form: (i) the drift contracts "
      "monotonically at the root from r = 2 on, out to r = 6; (ii) "
      "the contraction is NOT norm-dependent — the L-infinity, L1 "
      "and sector-L-infinity ratio sequences are EXACTLY equal, "
      "rational for rational; (iii) it holds UNIFORMLY over the "
      "family at fixed relative horizon, sup drift 3/110, 3/253, "
      "373/69230, 2333/1838829, contracting at every step.  The rate "
      "is reported as the SEQUENCE it is",
      monotone and norm_free and uni_sup == UNI_REF and uni_contracts,
      "root ratio sequence = " + ", ".join(
          f"{r} (~{float(r):.4f})" for r in seq)
      + f"; identical in all three norms = {norm_free}; family-wide "
      "sup drift = " + ", ".join(f"{x} (~{float(x):.3e})"
                                 for x in uni_sup))
outcome("MB3-c", "THE CONTRACTION READING, CORRECTED AND "
        "STRENGTHENED (round 1 B-M3). The root kernel's horizon "
        "drift contracts monotonically out to r = 6, but NOT at a "
        "constant rate: the successive L-infinity ratios are "
        + ", ".join(f"~{float(r):.3f}" for r in seq)
        + " — a sequence, not the '~0.738 per level' the first pass "
        "read off one datum. The contraction is norm-independent "
        "(identical exact ratios in L-infinity, L1 and "
        "sector-L-infinity) and uniform over the family at fixed "
        "relative horizon (sup 3/110, 3/253, 373/69230, "
        "2333/1838829). This is Cauchy-CONSISTENT evidence that a "
        "limit kernel may exist — evidence at the reachable "
        "horizons, NOT a convergence proof and NOT a claim that a "
        "boundary exists (horizon-scoped throughout).")

# ---- MB5: root vs the D44b reconvergence point ----------------------
print("\n[MB5 — root vs the D44b reconvergence point, MATCHED horizon]")
vname = ns['vname']
admissible = ns['admissible']
View = ns['View']
event_poset = ns['event_poset']
pA0 = ('p', 'A', V0, 0)
tA = ('A', V0, 0)
SELFA = ('r', 'A', frozenset({tA}), frozenset({tA}))
V1 = vname(V0, frozenset({tA}), 'A')
DELIV = ('d', 'A', 'B', V1)
WIT = (pA0, SELFA, DELIV)
adm = [admissible(list(WIT[:i]), WIT[i], AB) for i in range(3)]
wq = Fr(1)
for a, q in adm:
    wq *= q if a else Fr(0)
# B-M1: the first pass gated a WEIGHT, not an OBJECT.  After
# [pA0, blind self-seal] every delivery from A prices at 1/8, so
# delivering the genesis version v0 — which reconciles nothing,
# since B already holds v0 — carries the same 1/256 and passed.  The
# created-version identity and the reconvergence predicate are gated.
_pred = event_poset(list(WIT))
_full = View(list(WIT), _pred, set(range(len(WIT))))
holdA, holdB = _full.holdings('A'), _full.holdings('B')
root_hold = View([], event_poset([]), set()).holdings('A')
payload_is_created = (DELIV[3] == V1 and V1 != V0 and V1 in holdA)
reconverged = (holdA == holdB and V1 in holdB)
not_root_state = (holdA != root_hold)
check("MB5-a THE RECONVERGENCE WITNESS IS IDENTIFIED, not merely "
      "priced (round 1, B-M1): [pA0, blind self-seal, deliver v1 to "
      "B] is re-admitted through the committed layer with every "
      "event admissible and chain weight exactly 1/256 (the gated "
      "D44b/#374 value) AND the delivery's payload is gated to be "
      "the ARB-CREATED version v1 (v1 != v0, v1 held by A) AND the "
      "reconvergence predicate itself is gated: after the chain A "
      "and B hold the SAME version set, which is what makes this a "
      "reconvergence point.  Delivering the genesis v0 instead "
      "carries the identical 1/256 and reconciles nothing; the "
      "first pass could not tell the two apart",
      all(a for a, q in adm) and wq == Fr(1, 256)
      and payload_is_created and reconverged,
      f"chain weight = {wq}; payload = created version v1 "
      f"({payload_is_created}); A and B holdings coincide = "
      f"{reconverged} ({len(holdA)} versions each)")

# THE CORRECTED COMPARISON: matched REMAINING horizon.
MATCH = []
for r in (1, 2, 3):
    sr = sector(krel(CACHE, GT, ROOT, r))
    sw = sector(krel(CACHE, GT, WIT, r))
    MATCH.append((r, sr, sw, sr == sw))
    print(f"    matched remaining horizon r = {r}:  root "
          f"{ {kk: str(vv) for kk, vv in sorted(sr.items())} }  vs  "
          f"witness "
          f"{ {kk: str(vv) for kk, vv in sorted(sw.items())} }  "
          f"equal = {sr == sw}")
mis_root4 = sector(krel(CACHE, GT, ROOT, 4))
mis_wit1 = sector(krel(CACHE, GT, WIT, 1))
print(f"    the FIRST PASS's pairing (root r = 4 vs witness r = 1, "
      f"the absolute-cap artifact): root "
      f"{ {kk: str(vv) for kk, vv in sorted(mis_root4.items())} }  vs  "
      f"witness "
      f"{ {kk: str(vv) for kk, vv in sorted(mis_wit1.items())} }  "
      f"equal = {mis_root4 == mis_wit1}")
matched_equal = all(m[3] for m in MATCH)
M_REF = ({'d': Fr(1, 4), 'n': Fr(1, 2), 'p': Fr(1, 4)},
         {'d': Fr(1, 4), 'n': Fr(1, 2), 'p': Fr(1, 4)},
         {'d': Fr(64, 257), 'n': Fr(128, 257), 'p': Fr(65, 257)})
check("MB5-b ROOT vs RENEWAL AT MATCHED REMAINING HORIZON — the "
      "corrected comparison (round 1, BLOCKER B-A1).  The first pass "
      "compared a remaining-horizon-4 root kernel with a "
      "remaining-horizon-1 witness kernel, because its potential was "
      "capped at ABSOLUTE depth; at remaining horizon 1 a kernel "
      "degenerates to the normalized one-step menu with no lookahead "
      "at all, so the two objects were not the same functional of "
      "the state and the difference measured the horizon mismatch.  "
      "At MATCHED remaining horizon r = 1, 2, 3 the witness's "
      "per-kind sector masses are EXACTLY the root's, value for "
      "value, and each of the six masses is anchored here",
      matched_equal
      and tuple(m[1] for m in MATCH) == M_REF
      and tuple(m[2] for m in MATCH) == M_REF
      and mis_root4 != mis_wit1,
      f"equal at r = 1, 2, 3 = {[m[3] for m in MATCH]}; the first "
      f"pass's mismatched pairing differs = "
      f"{mis_root4 != mis_wit1}")

# the same question asked of the whole family rather than one point
share = []
for r in (1, 2, 3):
    sr = sector(krel(CACHE, GT, ROOT, r))
    n = tot = 0
    for h in CACHE:
        if h == ROOT or len(h) + r > CAP + 1:
            continue
        tot += 1
        if sector(krel(CACHE, GT, h, r)) == sr:
            n += 1
    share.append((r, n, tot))
check("MB5-c THE RENEWAL QUESTION ASKED OF THE WHOLE FAMILY, not of "
      "one hand-picked point: how many histories share the root's "
      "per-kind sector masses at matched remaining horizon.  The "
      "1/256 witness is one of thousands, so its agreement with the "
      "root is not a coincidence of a special state — and, "
      "conversely, sector-mass agreement is NOT by itself the "
      "renewal identity",
      [s[1:] for s in share] == [(8196, 30728), (1060, 3968),
                                 (104, 520)],
      "; ".join(f"r={r}: {n}/{t} histories match the root"
                for r, n, t in share))
outcome("MB5", "ROOT = RENEWAL AT TRANSPORT SCOPE, REVERSED (round 1 "
        "B-A1). At MATCHED remaining horizon the reconvergence "
        "witness's per-kind sector masses are EXACTLY the root's at "
        "r = 1, 2, 3 — every value identical. The transport analogue "
        "of the delivery-free root = renewal identity is therefore "
        "SUPPORTED in sector mass at every horizon this scope can "
        "compute, not refuted; the first pass's negative was "
        "produced entirely by pairing a remaining-horizon-4 root "
        "kernel with a remaining-horizon-1 witness kernel. TWO "
        "LIMITS, stated: (i) the FULL kernel comparison is UNTESTED, "
        "because the witness and the root carry different option "
        "sets — after the chain A and B hold v1, which is not the "
        "root's holdings state, so D44a's 'root = renewal AS ONE "
        "SIGMA-STATE' does not even predict full-kernel agreement "
        "here; (ii) sector-mass agreement is shared by 8196 of "
        "30728 histories at r = 1, so it is a necessary, not a "
        "sufficient, signature of renewal. Nothing here says "
        "reconvergence restores holdings without restoring the "
        "future — that sentence of the first pass is withdrawn as "
        "unsupported by any computation in this receipt.")

# ---- MB6: purity, gate vacuity, scope -------------------------------
print("\n[MB6 — purity, gate vacuity, scope]")
ALLOWED = (Fr, int, str, bool, tuple, list, type(None), frozenset)
def walk(o, n=[0]):
    if isinstance(o, (tuple, list, frozenset)):
        for x in (sorted(o, key=repr) if isinstance(o, frozenset)
                  else o):
            walk(x)
    elif isinstance(o, dict):
        for k in sorted(o, key=repr):
            walk(k); walk(o[k])
    else:
        n[0] += 1
        if not isinstance(o, ALLOWED):
            raise TypeError(f"impure leaf: {type(o)}")
    return n[0]
try:
    L = walk([tG, dG, tR, dR, RK, SM, CD, abs_drift, l1_drift,
              sec_drift, off_sup, uni_sup, cen4, cen5, dcen,
              [m[1] for m in MATCH], [m[2] for m in MATCH]])
    pure = True
except TypeError:
    L = 0
    pure = False
LEAF_REF = 633
check("MB6-a ALLOW-LIST PURITY (the #362 successor binding): every "
      "leaf of every potential, ratio, kernel, sector mass, "
      "conditional, drift and census is in {Fraction, int, str, "
      "bool} — floats appear ONLY in human-readable ~approximations "
      "inside detail strings, never in a gated quantity.  The leaf "
      "COUNT is anchored exactly (round 1, B-A3: 'L > 0' on a "
      "freshly-built list is a tautology)",
      pure and L == LEAF_REF, f"leaves walked = {L}, impure = 0")

# Round-1 B-A3(c): the first pass's vacuity scan looked for the
# literal `True` argument only, so `isinstance(x, Fraction)` on a
# freshly-constructed Fraction — three of its twelve gates — was
# invisible.  The scan is now an AST scan of the PREDICATE ARGUMENT
# of every check() call in this file, rejecting predicates that are
# constant by construction: a literal boolean, an isinstance() type
# probe, or a bare sign comparison against 0.
_self_src = open(os.path.abspath(__file__)).read()
_tree = ast.parse(_self_src)
TAUT = []
NGATES = 0
def vacuity_scan(tree):
    """Return (n_gates, [(lineno, shape)]) for every check() call whose
    PREDICATE argument is constant by construction."""
    bad, n = [], 0
    for nd in ast.walk(tree):
        if not (isinstance(nd, ast.Call)
                and getattr(nd.func, 'id', '') == 'check'
                and len(nd.args) >= 2):
            continue
        n += 1
        for sub in ast.walk(nd.args[1]):
            if (isinstance(sub, ast.Constant)
                    and (sub.value is True or sub.value is False)):
                bad.append((nd.lineno, 'literal boolean'))
            elif (isinstance(sub, ast.Call)
                  and getattr(sub.func, 'id', '') == 'isinstance'):
                bad.append((nd.lineno, 'isinstance type probe'))
            elif (isinstance(sub, ast.Compare) and len(sub.ops) == 1
                  and isinstance(sub.ops[0], (ast.Gt, ast.GtE))
                  and isinstance(sub.comparators[0], ast.Constant)
                  and sub.comparators[0].value == 0):
                bad.append((nd.lineno, 'sign-only comparison'))
    return n, bad

NGATES, TAUT = vacuity_scan(_tree)
# CAPABILITY PROBE: the scanner is shown to FIRE on the three shapes
# round 1 found surviving in this very receipt, and to stay silent on
# a substantive predicate.  A control that cannot fire is not a
# control (the sibling round's pattern (iii)).
_PROBE_V = ('check("a", isinstance(drift, Fr))\n'
            'check("b", r23 > 0 and r34 > 0)\n'
            'check("c", flag, "d")\n')
_pn, _pb = vacuity_scan(ast.parse(_PROBE_V))
_PROBE_OK = ('check("a", cen4 == {"2": 3757} and tG == TG_REF)\n')
_qn, _qb = vacuity_scan(ast.parse(_PROBE_OK))
probe_fires = (_pn == 3 and len(_pb) == 3
               and {s for _, s in _pb} == {'isinstance type probe',
                                           'sign-only comparison'}
               and len({ln for ln, _ in _pb}) == 2
               and _qn == 1 and _qb == [])
check("MB6-b NO VACUOUS GATE — an AST scan of every gate predicate "
      "in this file (round 1, BLOCKER B-A3).  The first pass scanned "
      "for the literal token 'True' and therefore certified a "
      "receipt containing three predicates that could not fail: "
      "'r23 > 0 and r34 > 0' on freshly-built positive rationals, "
      "and 'isinstance(drift, Fr)' / 'isinstance(d23, Fr)' on "
      "quantities constructed as Fractions one line earlier.  This "
      "gate parses its own source, walks the SECOND ARGUMENT of "
      "every check() call, and rejects any predicate containing a "
      "literal boolean, an isinstance() type probe, or a bare "
      "comparison against 0 — the three shapes that mutation "
      "survived.  The scanner is itself PROBED on a synthetic gate "
      "block carrying exactly those shapes and must flag them, and "
      "on a substantive predicate and must not",
      not TAUT and NGATES >= 15 and probe_fires
      and 'check(' in _self_src,
      f"gate predicates parsed = {NGATES}; vacuous predicates = "
      f"{TAUT if TAUT else 'none'}; scanner fires on the probe = "
      f"{probe_fires} (flagged {len(_pb)} of 3 synthetic gates)")

# Round-1 B-m5: 'CAP == 4 and len(OUT) >= 3' checked a constant and a
# list length, so it could not have caught the very assertion it
# certified the absence of.  (scan-exempt: this comment and the four
# needle literals below describe the scanner, not the physics.)  The
# scope gate now scans (scan-exempt) for infinite-volume language
# and requires a POSITIVE scope marker on the line (the d46c KG3
# pattern — markers that say in the line itself that the statement is
# finite-horizon or evidential, never a bare negation).
_N1 = "bound" + "ary"
_N2 = "infinite-" + "volume"
_N3 = "limit " + "kernel"
_N4 = "conver" + "ges"
_SCOPE_NEEDLES = (_N1, _N2, _N3, _N4)
_SCOPE_MARKERS = ('finite-horizon', 'horizon-scoped', 'candidate',
                  'evidence', 'evidential', 'cauchy-consistent',
                  'may exist', 'would formalize', 'no ' + _N1,
                  'not a ' + _N4, 'reachable', 'scan-exempt',
                  'open', 'asserts no', 'withheld', 'withholds',
                  'needle', 'marker')
def scope_scan(lines):
    bad = [i + 1 for i, ln in enumerate(lines)
           if any(nd in ln.lower() for nd in _SCOPE_NEEDLES)
           and not any(m in ln.lower() for m in _SCOPE_MARKERS)]
    hit = sum(1 for ln in lines
              if any(nd in ln.lower() for nd in _SCOPE_NEEDLES))
    return hit, bad

_lines = _self_src.splitlines()
_SCANNED, SCOPE_BAD = scope_scan(_lines)
# CAPABILITY PROBE (built by concatenation so the scanner cannot see
# the needles in this source): an undisclaimed existence assertion
# must be caught, a properly scoped line must not.
_probe_bad = ["the transport chain HAS a Martin " + _N1
              + " and its " + _N3 + " exists"]
_probe_ok = ["no " + _N1 + " existence is claimed: finite-horizon "
             + _N3 + " evidence only"]
scope_fires = (scope_scan(_probe_bad)[1] == [1]
               and scope_scan(_probe_ok)[1] == [])
check("MB6-c SCOPE, scanned rather than asserted (round 1, B-m5).  "
      "Each of the four needle words — boundary, infinite-volume, "
      "limit kernel, converges (scan-exempt: needle literals) — "
      "must occur only on lines carrying a POSITIVE scope marker: a "
      "word saying in the line itself that the statement is "
      "finite-horizon, evidential, or explicitly withheld.  Every "
      "result above is a finite-horizon measurement at the extended "
      "caps; the receipt asserts no boundary existence (scan-exempt "
      "clause) and no transport-scope closure, and D44b's open "
      "verdict stands untouched.  The scanner is PROBED both ways: "
      "it must flag a synthetic undisclaimed existence assertion and "
      "must pass a properly scoped one",
      not SCOPE_BAD and _SCANNED >= 7 and scope_fires and CAP == 5
      and len(OUT) == 4,
      f"lines scanned = {_SCANNED} of {len(_lines)}; undisclaimed = "
      f"{SCOPE_BAD if SCOPE_BAD else 'none'}; scanner fires on the "
      f"probe = {scope_fires}; cap = {CAP}; delivered outcomes = "
      f"{len(OUT)}")

print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL  ({len(OUT)} delivered "
      f"outcomes)")
if FAIL:
    print("[VERDICT] FAIL — breakage; exit 1")
    sys.exit(1)

# Round-1 B-A3(b) / B-n1: the first pass's [VERDICT] was a LITERAL,
# and the referee's mutants b5/b6/b7 flipped the delivered outcomes
# while the verdict string went on asserting the old headline at
# 12 PASS / exit 0.  Every clause below is now BUILT from a computed
# quantity, so a flipped outcome cannot leave an asserting verdict
# behind.
_ladder = ("takes exactly the delivery-free value set {"
           + ", ".join(sorted(cen5, key=len))
           + f"}} ({cen4['2']} / {cen4['5/2']} at the committed cap)"
           if set(cen5) == set(dcen) else
           "does NOT take the delivery-free value set")
_growth = (("the delivery-free family's finite-horizon ratios are "
            "UNIFORMLY LARGER than transport's, so at the reachable "
            "caps DELIVERIES REDUCE finite-horizon branching")
           if df_ge else
           ("the transport ratios are >= the delivery-free ones, so "
            "deliveries ADD finite-horizon branching"))
_trend = (f"the transport ratio PEAKS at D = {peak + 2} and turns "
          "down at D = 6" if turns else
          "the transport ratio is still rising at D = 6")
_stab = (("the SECTOR-NORMALIZED CONDITIONAL — the object the pin "
          "and the d44f lesson name — is EXACTLY horizon-stable at "
          "the root (drift 0 at r = 1..6, partly forced by "
          "within-sector exchangeability) and contracts uniformly "
          "off it")
         if cond_stable else
         ("the sector-normalized conditional DRIFTS with the horizon "
          "even at the root"))
_contract = (("their drift CONTRACTS monotonically, identically in "
              "L-infinity, L1 and sector-L-infinity, and uniformly "
              "over the family at fixed relative horizon — "
              "Cauchy-consistent evidence, no existence claim")
             if (monotone and norm_free and uni_contracts) else
             "their drift does NOT contract at the reachable "
             "horizons")
_renewal = (("the transport analogue of the delivery-free "
             "root = renewal identity is SUPPORTED in sector mass: "
             "at MATCHED remaining horizon r = 1, 2, 3 the 1/256 "
             "reconvergence witness's per-kind sector masses are "
             "EXACTLY the root's.  The first pass's contrary "
             "headline was an artifact of comparing a "
             "remaining-horizon-4 root kernel with a "
             "remaining-horizon-1 witness kernel; it is WITHDRAWN.  "
             "The FULL-kernel comparison remains untested, the two "
             "states carrying different option sets")
            if matched_equal else
            ("the transport analogue of root = renewal FAILS in "
             "sector mass at matched remaining horizon"))
print("[VERDICT] d46b GREEN-UNREVIEWED, ROUND-1 REPAIRED: [I1]'s "
      "machinery is INSTANTIATED at transport scope in its honest "
      "finite-horizon form, and every clause of this verdict is "
      "assembled from a gated computation above rather than "
      "asserted. THE LADDER SURVIVES TRANSPORT: the per-history menu "
      "weight sum " + _ladder + ", against the delivery-free census "
      "recomputed here from the committed d42b3 layer — the "
      "quarter-quantized structure is not a deliverylessness "
      "artifact. THE GROWTH READING IS REVERSED: " + _growth + ", and "
      + _trend + "; D44a's lambda = 2 is an asymptotic EIGENVALUE "
      "and is not comparable with any finite-horizon ratio. THE "
      "HORIZON-STABILITY READING IS CORRECTED ONTO ITS PINNED "
      "OBJECT: " + _stab + ", while the absolute kernel and the "
      "per-kind sector MASSES drift at every horizon, and "
      + _contract + ". AND THE root = renewal READING IS REVERSED: "
      + _renewal + ". Not review-hardened until the D46b round "
      "converts (paper-32's round precedes it).")
