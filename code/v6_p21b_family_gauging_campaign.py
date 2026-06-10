#!/usr/bin/env python3
"""
v6_p21b: gauging the family fiber forces the sixteenth Weyl fermion
(Paper 21).

By P18's reconstruction, a record family fiber IS gauge: its U(g)
must satisfy the seam/anomaly predicates.  For g = 3 (the minimal
protected replication, p21a) with the SM content per family in
fundamentals/antifundamentals of SU(3)_H:

 (i)  WITHOUT nu_R: the SU(3)_H cubic needs a partition of the SM
      multiplet dimensions {6, 3, 3, 2, 1} (sum 15, ODD) into equal
      3_H and 3bar_H halves: IMPOSSIBLE.  A gauged three-family fiber
      over the bare SM content is ANOMALOUS, always.
 (ii) WITH nu_R (dims {6, 3, 3, 2, 1, 1}, sum 16): exhaustive scan of
      all 2^6 chirality assignments against BOTH conditions
        SU(3)_H^3:        sum (+-) dim   = 0
        SU(3)_H^2-U(1)_Y: sum (+-) dim Y6 = 0
      The solutions are printed - the assignment (Q, L | u^c, d^c,
      e^c, nu^c) and its global conjugate.
 (iii) g = 2 contrast: no cubic exists, but WITTEN counts doublets:
      15 (odd) FAILS without nu_R, passes with it - yet g = 2 is
      unprotected (p21a): the only protected, gaugeable, minimal
      family structure is g = 3 WITH nu_R.

THE FORCED PREDICTION: any record family fiber implies the existence
of the right-handed neutrino - the sixteenth Weyl fermion - and (for
g = 3) the unique embedding above.
"""
from itertools import product

fields = [("Q", 6, 1), ("u^c", 3, -4), ("d^c", 3, 2),
          ("L", 2, -3), ("e^c", 1, 6), ("nu^c", 1, 0)]

# ---------- (i) without nu_R ----------
print("== (i) g = 3 without nu_R: impossible ==")
dims5 = [6, 3, 3, 2, 1]
print(f"  SM multiplet dims {dims5}, total {sum(dims5)} (ODD):")
print("  an equal 3_H | 3bar_H partition cannot exist - the cubic")
print("  SU(3)_H anomaly CANNOT cancel: a gauged three-family fiber")
print("  over the 15-Weyl SM content is anomalous, with no assignment.")

# ---------- (ii) with nu_R: the exhaustive scan ----------
print("\n== (ii) with nu_R: the exhaustive assignment scan ==")
sols = []
for signs in product((1, -1), repeat=6):
    cubic = sum(s * d for s, (n, d, y) in zip(signs, fields))
    mixed = sum(s * d * y for s, (n, d, y) in zip(signs, fields))
    if cubic == 0 and mixed == 0:
        sols.append(signs)
print(f"  assignments passing BOTH conditions: {len(sols)} of 64")
for signs in sols:
    plus = [n for s, (n, d, y) in zip(signs, fields) if s > 0]
    minus = [n for s, (n, d, y) in zip(signs, fields) if s < 0]
    print(f"   3_H: {plus}   3bar_H: {minus}")
print("  -> the UNIQUE solution up to global conjugation:")
print("     (Q, L) in 3_H, (u^c, d^c, e^c, nu^c) in 3bar_H - the")
print("     left-handed doublets and the right-handed singlets fall on")
print("     opposite sides of the family code, and nu^c MUST EXIST for")
print("     the partition to balance (8 = 8).")

# ---------- (iii) the g = 2 contrast and the verdict ----------
print("\n== (iii) g = 2 contrast, and the forced prediction ==")
print("  g = 2: no cubic; WITTEN counts SU(2)_H doublets = total Weyl")
print(f"  fields = 15 per generation-stack: ODD: FAILS without nu_R;")
print("  16 with it: passes - but g = 2 is UNPROTECTED (p21a): the")
print("  epsilon seam erases the replication.")
print("  THE VERDICT: the only protected, gaugeable, minimal family")
print("  structure is g = 3 WITH the sixteenth Weyl fermion:")
print("    ANY RECORD FAMILY FIBER FORCES THE RIGHT-HANDED NEUTRINO,")
print("  and at g = 3 the embedding (Q, L | u^c, d^c, e^c, nu^c) is")
print("  unique.  (The premise - that replication IS a fiber - is the")
print("  named hypothesis (F-fiber); under it, nu_R is a falsifiable")
print("  structural prediction, and 16 = the SO(10)-spinor count is")
print("  noted as a direction, not a claim.)")
print("== p21b done ==")
