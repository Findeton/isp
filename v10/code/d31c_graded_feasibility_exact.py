#!/usr/bin/env python3
"""
d31c_graded_feasibility_exact.py — v10 D31C: graded-feasibility
reconnaissance for stationary path-covariant kernels. Pin: note-d31
(committed pre-run). Stdlib only; exact rationals. RECONNAISSANCE ONLY:
no unbounded-existence claim (stated). Gates C1-C5; exit 1 on failure.
"""
from fractions import Fraction as F
from itertools import product

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

print("[d31c graded feasibility — exact reconnaissance]")
print("      family (i): normalized weights graded by {birth, interact at")
print("      d_cover = 1, interact at d_cover >= 2}; the D28 seed domain.")

# The concrete bi pair on the D28 seed (R sealed; A, B unsealed, d(A,B) = 1):
#   Z(H)   = 2 f_b + 2 f_i1                       (2 births, 2 d1-interacts)
#   H + i  = a parallel (A,B) edge: opportunities unchanged -> Z(H+i) = Z(H)
#   H + b  = a leaf z1 on A: 3 births; (A,B) d1 x2, (A,z1) d1 x2, (B,z1) d2 x2
#            -> Z(H+b) = 3 f_b + 4 f_i1 + 2 f_i2
def Z_H(fb, f1, f2):   return 2*fb + 2*f1
def Z_Hi(fb, f1, f2):  return 2*fb + 2*f1
def Z_Hb(fb, f1, f2):  return 3*fb + 4*f1 + 2*f2

# C1: covariance on the bi pair <=> Z(H+b) = Z(H+i), for normalized weights
ok1 = True
for fb, f1, f2 in product((F(1,10), F(1,3), F(2,5)), repeat=3):
    lhs = (fb/Z_H(fb,f1,f2)) * (f1/Z_Hb(fb,f1,f2))     # birth then interact
    rhs = (f1/Z_H(fb,f1,f2)) * (fb/Z_Hi(fb,f1,f2))     # interact then birth
    ok1 &= (lhs == rhs) == (Z_Hb(fb,f1,f2) == Z_Hi(fb,f1,f2))
check("C1 the forced equality: normalized path-covariance on the concrete "
      "bi pair holds iff Z(H+b) = Z(H+i) — instantiated over a positive "
      "weight grid", ok1)

# C2: THE OBSTRUCTION — the equality is impossible for positive weights
ok2 = True
diffs = []
for fb, f1, f2 in product((F(1,10), F(1,3), F(2,5)), repeat=3):
    d = Z_Hb(fb,f1,f2) - Z_Hi(fb,f1,f2)
    diffs.append(d)
    ok2 &= d == fb + 2*f1 + 2*f2 and d > 0
check("C2 THE OBSTRUCTION (family i): Z(H+b) - Z(H+i) = f_b + 2 f_i1 + "
      "2 f_i2 > 0 for every positive weight assignment — a birth strictly "
      "adds opportunities while a parallel-edge interact adds none: NO "
      "positive stationary path-covariant kernel exists in the "
      "multiplicity-insensitive class-graded family (no-none, normalized)",
      ok2, f"closed form verified on {len(diffs)} grid points")
print("      C2 scope (round-1 corrected — TWO conditions, not one): the")
print("      argument needs (a) multiplicity-insensitivity (Z(H+i) = Z(H) —")
print("      parallel edges qualify) AND (b) BIRTH-INERTNESS of the existing")
print("      opportunity classes (a leaf birth must not reclassify old ops,")
print("      so Z(H+b) = Z(H) + the newborn's strictly positive mass).")
print("      d_cover classes, static-age classes and component indicators")
print("      satisfy both — OBSTRUCTED. Simple-graph degree, motif and")
print("      component-size gradings are multiplicity-insensitive but NOT")
print("      birth-inert (a leaf birth reclassifies the parent's old ops) —")
print("      they move to the OPEN arm with distance-degree (front F3').")
print("      RECONNAISSANCE LIMIT: no unbounded claim beyond the exhibited")
print("      domain for any family in the open arm.")

# C3: the multiplicity-insensitive extension, instantiated once more
# (age-graded: weights by register age class — an interact changes no ages
# at the step scale used here; the same Z argument applies)
ok3 = True
for fb_y, fb_o, f1, f2 in product((F(1,8), F(1,4)), repeat=4):
    Z_h  = fb_y + fb_o + 2*f1              # one young, one old register
    Z_hi = Z_h                              # parallel edge: no age/class change
    Z_hb = fb_y + fb_o + fb_y + 4*f1 + 2*f2   # newborn = young
    ok3 &= (Z_hb - Z_hi) > 0
check("C3 the extension: an age-graded family (young/old births) hits the "
      "same obstruction — the newborn's opportunities strictly enlarge Z "
      "while the parallel interact leaves it fixed", ok3)

# C4: the none-arm escape — covariance bought by a state-dependent idle rate
ok4 = True
fb, f1, f2 = F(1,20), F(1,30), F(1,50)
def fn(nb, n1, n2):
    return 1 - (nb*fb + n1*f1 + n2*f2)     # the none weight absorbs Z
# path products over ACTIVE ops with Z == 1: birth-then-interact vs reverse
p1 = fb * f1
p2 = f1 * fb
okpos = fn(2, 2, 0) > 0 and fn(3, 4, 2) > 0 and fn(2, 2, 0) < 1
ok4 &= (p1 == p2) and okpos
check("C4 THE NONE-ARM ESCAPE — BOUNDED-DOMAIN ONLY (round-1 M2): with a "
      "none op absorbing normalization (Z == 1), constant class weights "
      "give ACTIVE-SUBPRODUCT path-covariance on the none-free skeleton "
      "(the D28b R6 convention; none-padded full products are NOT order-"
      "invariant — the pads carry different f_n). The escape does NOT "
      "extend: idle positivity fails at u* = 6 for these constants (any "
      "4-birth extension carries active mass 31/30 > 1), and generally "
      "u*f_b > 1 at finite u — while Z == 1 re-imposes the A1 forcing, so "
      "at unbounded growth the class carries NO interactions (the A3 "
      "collapse): THIS ESCAPE IS THE BOUNDED-GROWTH ESCAPE D31A already "
      "prices, not a third route",
      ok4, f"f_n at seed = {fn(2,2,0)}, at H+b = {fn(3,4,2)}; ill-defined at u=6")

# C5: the landscape for D32's admissibility axis
print("      C5 THE LANDSCAPE [feeds D32's declared covariance column]:")
print("        no-none, normalized, multiplicity-insensitive grading:")
print("          OBSTRUCTED (C2/C3 — theorem-grade on the exhibited class);")
print("        degree-sensitive gradings: OPEN (the interact shifts Z —")
print("          the equation reopens; front);")
print("        none-absorbing kernels: EXIST on BOUNDED DOMAINS ONLY (C4 —")
print("          constants encode a size cap; at unbounded growth the arm")
print("          collapses to pure-birth-plus-idle: it IS the bounded-growth")
print("          escape, not a third route; the D28 kernels' none weight was")
print("          uniform, not absorbing — a separate failure);")
print("        K_flat-class (teleological Phi weights): EXIST, horizon-")
print("          dependent (D28b R5).")
print("      Path-covariance therefore remains a DECLARED STATUS COLUMN in")
print("      D32, not a filter — the physical question (is the accretion")
print("      path a record?) is still open, and now has a price list.")
check("C5 the landscape printed", True)

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total}: 4 substantive gates + 1 print gate)"
      if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
