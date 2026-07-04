"""
v8 Paper 7 (manifoldlikeness flanks), receipt g3 -- THE MEASURE CENSUS AND THE
EXTENSIVE-ACTION NO-GO.

Paper 4 Section 5 left the frontier question: does the click-law give any lever on
Kleitman-Rothschild suppression?  ("nothing in the corpus suggesting a lever").  This
receipt sharpens that to a THEOREM plus an exact census:

  THE THEOREM (proved in paper 7 Section 4; the receipt exhibits the arithmetic).
  No RECORD-NATIVE COUNTING MEASURE and no EXTENSIVE ACTION suppresses the layered
  bulk.  Precisely: let W(P) = m(P) * exp(-beta*S(P)) with m one of
     m_U = 1 (unlabeled),  m_L = n!/|Aut P| (labeled),  m_H = m_L * e(P) (commit
     histories; e(P) = number of linear extensions -- each odometer history is one
     microstate), and |S(P)| <= c*n (EXTENSIVE: bounded per-seal cost).  Then
        W(2-layer bulk) / W(dim<=2 class)  >=  2^{n^2/4} / [ (n!)^3 e^{2 beta c n} ]
        --> infinity.
  Counting inputs are SELF-CONTAINED (no KR asymptotics import): the free-bipartite
  family on a fixed n/2 + n/2 split gives >= 2^{n^2/4} labeled 2-layer posets
  (transitivity is vacuous across two layers), while every dim<=2 poset is the
  intersection of an ordered realizer pair, so there are at most (n!)^2 labeled ones;
  the history factor costs at most one more n! (e(P) <= n!).  Consequence: any
  positive-weight suppression mechanism needs a SUPER-EXTENSIVE action -- gaps growing
  like n^2 -- sharpening pE's scoping (pE: positive weights cannot CANCEL; here:
  extensive positive weights cannot even SUPPRESS).

  THE CENSUS (exact, riding receipt pE's enumeration: all unlabeled posets to n = 7,
  A000112-checked; |Aut| A001035-checked).  For each iso class we add e(P) by the
  order-ideal DP, cross-checked by the identity
        sum over LABELED posets of e(P)  =  n! * A006455(n)
  (pair each linear order with the naturally-labeled posets it extends).  We then
  report the mass shares of the GEOMETRIC (dim<=2) class, the KR-type class, and the
  bulk under the three measures m_U / m_L / m_H, and the direction of the shift:
  DOES THE HISTORY MEASURE HELP OR HURT?  (e(P) is maximal on antichain-like orders,
  so the honest expectation is HURT -- recorded either way.)

  THE SUPER-EXTENSIVE CANDIDATE (scout-grade): the per-class 2D Benincasa-Dowker
  action gap between bulk and geometric classes vs n at n <= 7 -- enumerable n cannot
  exhibit asymptotics (pE's scoping); the receipt records the trend and the n^2 bar
  the theorem sets, nothing more.

Depends on: pE_phase_causalset.py (enumeration, |Aut|, dim<=2 oracle, BD action).
"""

import os
import sys
import math
import time
import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pE_phase_causalset import process_n, OEIS_A000112  # noqa: E402

mp.mp.dps = int(os.environ.get("G3_DPS", "60"))
N_MAX = int(os.environ.get("G3_NMAX", "7"))

CHECKS = []
def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))

def head(s):
    print("\n" + "=" * 80); print(s); print("=" * 80)

# ------------------------------------------------------------ linear extensions
def linear_extensions(n, rel):
    """e(P) by DP over order ideals (bitmask): e(D) = sum over maximal x of e(D-x)."""
    preds = [0] * n
    for (a, b) in rel:
        preds[b] |= (1 << a)
    memo = {0: 1}
    def ideal_count(D):
        if D in memo:
            return memo[D]
        total = 0
        for x in range(n):
            bx = 1 << x
            if D & bx:
                rest = D ^ bx
                # x maximal in D iff no y in D has x among preds? x is REMOVABLE from the
                # ideal top iff x's successors are all outside D; equivalently D-x is an
                # ideal: no y in D-x with x in preds[y].
                ok = True
                for y in range(n):
                    if (rest >> y) & 1 and (preds[y] >> x) & 1:
                        ok = False; break
                if ok:
                    total += ideal_count(rest)
        memo[D] = total
        return total
    return ideal_count((1 << n) - 1)

A006455 = {1: 1, 2: 2, 3: 7, 4: 40, 5: 357, 6: 4824, 7: 96428, 8: 2800472}

# ------------------------------------------------------------------------ main
def main():
    t0 = time.time()
    head(f"g3 -- MEASURE CENSUS (n <= {N_MAX}) + THE EXTENSIVE-ACTION NO-GO ARITHMETIC")

    per_n = {}
    EXT = {}   # id(class) -> e(P)  (IsoClass uses __slots__; keep e(P) alongside)
    for n in range(2, N_MAX + 1):
        tt = time.time()
        classes = process_n(n, want_aut=True)
        for c in classes:
            EXT[id(c)] = linear_extensions(n, c.rel)
        per_n[n] = classes
        print(f"   n={n}: {len(classes)} classes  [{time.time()-tt:.1f}s]")

    # CHECK 1: enumeration counts (pE's own guarantee, re-verified here)
    head("CHECK 1 -- enumeration matches OEIS A000112")
    ok = all(len(per_n[n]) == OEIS_A000112[n] for n in per_n)
    check("A000112 reproduced for all n", ok,
          ", ".join(f"n{n}:{len(per_n[n])}" for n in per_n))

    # CHECK 1b: labeled totals match A001035 (re-run of pE's own cross-check)
    head("CHECK 1b -- labeled totals: sum n!/|Aut| == A001035")
    A001035 = {2: 3, 3: 19, 4: 219, 5: 4231, 6: 130023, 7: 6129859, 8: 431723379}
    ok1b = all(sum(c.lab_mult for c in per_n[n]) == A001035[n] for n in per_n)
    check("A001035 reproduced for all n (|Aut| validated directly)", ok1b,
          ", ".join(f"n{n}:{sum(c.lab_mult for c in per_n[n])}" for n in per_n))

    # CHECK 2: the microstate identity  sum_labeled e(P) = n! * A006455(n)
    head("CHECK 2 -- commit-history microstates: sum over labeled posets of e(P) = n!*A006455")
    ok_all = True
    for n in per_n:
        got = sum(c.lab_mult * EXT[id(c)] for c in per_n[n])
        expect = math.factorial(n) * A006455[n]
        ok = (got == expect)
        ok_all &= ok
        print(f"   n={n}: sum lab*e = {got}   n!*A006455 = {expect}  -> {'OK' if ok else 'MISMATCH'}")
    check("microstate identity exact for all n (validates e(P) and |Aut| jointly)", ok_all)

    # CHECK 3: e(P) sanity -- chain=1, antichain=n! (max), N-poset known small value
    head("CHECK 3 -- e(P) anchors")
    n = 4
    chain_rel = frozenset((i, j) for i in range(4) for j in range(i + 1, 4))
    anti_rel = frozenset()
    npos_rel = frozenset([(0, 2), (1, 2), (1, 3)])
    e_chain = linear_extensions(4, chain_rel)
    e_anti = linear_extensions(4, anti_rel)
    e_npos = linear_extensions(4, npos_rel)
    check("e(chain)=1, e(antichain)=n!, e(N-poset on 4)=5",
          e_chain == 1 and e_anti == 24 and e_npos == 5,
          f"got {e_chain}, {e_anti}, {e_npos} (N-poset extensions: 0123, 0132, 1023, 1032, 1302)")

    # THE CENSUS: shares under the three measures
    head("THE CENSUS -- geometric/KR/bulk mass shares under m_U, m_L, m_H")
    print(f"   {'n':>2} | {'share_geo_U':>11} {'share_geo_L':>11} {'share_geo_H':>11} | "
          f"{'share_KR_U':>10} {'share_KR_L':>10} {'share_KR_H':>10}")
    rows = {}
    for n in sorted(per_n):
        cl = per_n[n]
        wU = [(1, c) for c in cl]
        wL = [(c.lab_mult, c) for c in cl]
        wH = [(c.lab_mult * EXT[id(c)], c) for c in cl]
        def share(wlist, pred):
            tot = sum(w for w, c in wlist)
            sel = sum(w for w, c in wlist if pred(c))
            return sel / tot
        gU = share(wU, lambda c: c.geom); gL = share(wL, lambda c: c.geom); gH = share(wH, lambda c: c.geom)
        kU = share(wU, lambda c: c.kr); kL = share(wL, lambda c: c.kr); kH = share(wH, lambda c: c.kr)
        rows[n] = (gU, gL, gH, kU, kL, kH)
        print(f"   {n:>2} | {gU:11.4f} {gL:11.4f} {gH:11.4f} | {kU:10.4f} {kL:10.4f} {kH:10.4f}")

    # CHECK 4: the geometric share is DECREASING in n under every measure (the wall
    # is real and no counting measure reverses it at enumerable n)
    head("CHECK 4 -- geometric share decreasing in n under all three measures")
    ns = sorted(rows)
    dec = all(rows[ns[i + 1]][j] <= rows[ns[i]][j] + 1e-12
              for i in range(len(ns) - 1) for j in (0, 1, 2))
    check("share_geo monotonically non-increasing in n for m_U, m_L, m_H", dec)

    # CHECK 5: the history measure does NOT help the geometric class (record the
    # direction honestly: e(P) favors antichain-like orders)
    head("CHECK 5 -- history measure direction at the largest n")
    nl = ns[-1]
    gU, gL, gH = rows[nl][0], rows[nl][1], rows[nl][2]
    helps = gH > gL
    print(f"   n={nl}: share_geo: U={gU:.4f}  L={gL:.4f}  H={gH:.4f}  -> history helps? {helps}")
    check("history-measure direction recorded (verdict either way; expectation: hurts)",
          True, f"gH={gH:.4f} vs gL={gL:.4f}: history {'helps' if helps else 'hurts or neutral'}")

    # THE NO-GO ARITHMETIC: 2^{n^2/4} vs (n!)^3 e^{2 beta c n}
    head("THE NO-GO ARITHMETIC -- ln[2^{n^2/4}] vs ln[(n!)^3] + 2 beta c n")
    print(f"   (beta*c = 1; the bound is monotone in beta*c and the verdict is asymptotic)")
    print(f"   {'n':>5} | {'(n^2/4)ln2':>12} {'3 ln n!':>12} {'2n':>8} | {'margin':>12}")
    cross = None
    for n in (8, 16, 24, 32, 48, 64, 96, 128):
        lhs = (n * n / 4) * math.log(2)
        rhs = 3 * math.lgamma(n + 1) + 2 * n
        margin = lhs - rhs
        if cross is None and margin > 0:
            cross = n
        print(f"   {n:>5} | {lhs:12.1f} {rhs:12.1f} {2*n:8.0f} | {margin:12.1f}")
    # the EXACT crossover of the (n!)^3 form (floored exponent), by direct scan:
    exact_cross = next(n for n in range(2, 200)
                       if (n * n // 4) * math.log(2) > 3 * math.lgamma(n + 1) + 2 * n)
    print(f"   exact crossover (smallest n with floor(n^2/4) ln2 > 3 ln n! + 2n): "
          f"n = {exact_cross}")
    check("bulk/geometric log-mass margin positive from some finite n on (crossover shown)",
          cross is not None,
          f"first tabulated n with positive margin: {cross}; exact crossover n = {exact_cross}")
    # exact small-n counterpart: free-bipartite labeled count 2^{floor(n^2/4)} at the
    # fixed even split is a LOWER bound on labeled height<=2 posets -- verify at n<=6
    # against the census (sum of lab_mult over height<=2, dim>=3 excluded NOT needed:
    # bound is on ALL 2-layer posets; verify the inequality direction only).
    okb = True
    for n in (4, 6):
        two_layer_mass = sum(c.lab_mult for c in per_n[n] if c.height <= 2)
        # the free-bipartite count on the fixed balanced split with all 2^{(n/2)^2}
        # relation patterns, INCLUDING relabelings, is <= labeled height<=2 posets;
        # the raw pattern count (fixed split, no relabeling) is the clean lower bound:
        lower = 2 ** ((n // 2) * (n - n // 2))
        okb &= (two_layer_mass >= lower)
        print(f"   n={n}: labeled height<=2 mass = {two_layer_mass}  >=  2^(n^2/4) = {lower}  "
              f"{'OK' if two_layer_mass >= lower else 'FAIL'}")
    check("free-bipartite lower bound consistent with the exact census (n=4,6)", okb)

    # SCOUT: BD-action gap between bulk and geometric vs n (super-extensive candidate)
    head("SCOUT -- BD-action separation bulk vs geometric (enumerable n; trend only)")
    print(f"   {'n':>2} | {'mean S geo':>11} {'mean S bulk':>11} {'gap':>8} {'std bulk':>9}")
    gaps = {}
    for n in sorted(per_n):
        geo = [c.S for c in per_n[n] if c.geom]
        bulk = [c.S for c in per_n[n] if not c.geom]
        if not bulk:
            continue
        mg = sum(geo) / len(geo); mb = sum(bulk) / len(bulk)
        vb = (sum((x - mb) ** 2 for x in bulk) / len(bulk)) ** 0.5
        gaps[n] = mb - mg
        print(f"   {n:>2} | {mg:11.3f} {mb:11.3f} {mb-mg:8.3f} {vb:9.3f}")
    check("BD-gap trend recorded (scout; no asymptotic claim at enumerable n)", True,
          ", ".join(f"n{n}:{gaps[n]:+.2f}" for n in sorted(gaps)))

    head("VERDICT")
    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print(f"\n{'ALL CHECKS PASS' if npass == len(CHECKS) else 'CHECKS'} ({npass}/{len(CHECKS)})")
    for name, ok, _ in CHECKS:
        if not ok:
            print(f"   FAILED: {name}")
    print(f"[runtime {time.time()-t0:.1f}s; N_MAX={N_MAX}; dps={mp.mp.dps}]")

if __name__ == "__main__":
    main()
