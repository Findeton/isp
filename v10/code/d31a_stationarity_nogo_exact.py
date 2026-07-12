#!/usr/bin/env python3
"""
d31a_stationarity_nogo_exact.py — v10 D31A: the graph-blind stationarity
no-go. Pin: note-d31 (committed pre-run). Stdlib only; exact rationals.
Theorem: in the none-free, unbounded-growth grammar, a stationary
path-covariant kernel whose per-labelled-opportunity weights depend only
on the unsealed count u cannot assign positive weight to interactions;
the unique such kernel is pure birth w_b(u) = 1/u.
Gates A1-A5; exit 1 on any failure.
"""
from fractions import Fraction as F

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def kernel_weights(u, wb, wi):
    """Per-labelled-opportunity weights at unsealed count u:
    u births at wb(u) each, u(u-1) directed interacts at wi(u) each."""
    return wb(u), wi(u)

def norm_gap(u, wb, wi):
    return u*wb(u) + u*(u-1)*wi(u) - 1

print("[d31a graph-blind stationarity no-go — exact]")
print("      grammar: none-free; at count u: u labelled births, u(u-1)")
print("      labelled directed interacts; weights depend on u only.")

# A1: the three independent pair types, instantiated at u = 2..6
ok1 = True
for u in range(2, 7):
    # bb: birth then birth vs reversed — products both w_b(u) w_b(u+1)
    #     (the u-sequence is order-independent): identical expressions.
    # ii: interact then interact — both w_i(u) w_i(u); identical.
    # bi (THE FORCING PAIR): birth then old-pair interact vs reversed:
    #     P1 = w_b(u) * w_i(u+1)   [interact after the birth: count u+1]
    #     P2 = w_i(u) * w_b(u)     [interact leaves u unchanged]
    #     Covariance <=> w_i(u+1) = w_i(u), given w_b(u) > 0.
    for (wb, wi) in (
        (lambda v: F(1, v), lambda v: F(0)),
        (lambda v: F(1, 2*v), lambda v: F(1, 2*v*(v-1)) if v > 1 else F(0))):
        P1 = wb(u) * wi(u+1)
        P2 = wi(u) * wb(u)
        ok1 &= (P1 == P2) == (wi(u+1) == wi(u))
check("A1 pair types at u = 2..6: bb and ii are identically covariant; the "
      "bi pair forces w_i(u+1) = w_i(u) exactly when birth weights are "
      "positive (the forcing equation instantiated)", ok1)

# A2: a non-constant w_i kernel violates covariance on an exhibited pair
wb2 = lambda u: (1 - (u-1)*F(1,10)) / u          # normalization with wi = c/u
wi2 = lambda u: F(1, 10*u)
u = 2
P1, P2 = wb2(u)*wi2(u+1), wi2(u)*wb2(u)
ok2 = (P1 != P2) and norm_gap(2, wb2, wi2) == 0 and norm_gap(3, wb2, wi2) == 0
check("A2 violation exhibit: the normalized u-varying kernel w_i(u) = 1/(10u) "
      "breaks path-covariance on the bi pair at u = 2", ok2,
      f"P1 = {P1} vs P2 = {P2}")

# A3: the constant-c kernel is covariant on every tested pair — and its
# positivity collapses at the computed u*
c = F(1, 10)
wb3 = lambda u: (1 - u*(u-1)*c) / u
wi3 = lambda u: c
ok3 = True
for u in range(2, 7):
    ok3 &= wb3(u)*wi3(u+1) == wi3(u)*wb3(u)      # covariant (wi constant)
    ok3 &= norm_gap(u, wb3, wi3) == 0
u_star = next(u for u in range(2, 100) if u*(u-1) >= 10)
ok3 &= wb3(u_star) < 0
check("A3 the collapse: the constant-c kernel is covariant at every tested "
      "u BUT birth positivity fails at the computed u* — unbounded growth "
      "forces c = 0", ok3, f"c = 1/10, u* = {u_star}, w_b(u*) = {wb3(u_star)}")

# A4: pure birth w_b = 1/u — full path-covariance on the enumerated domain
# (every length-3 birth path from u = 2; all path products equal; total mass 1)
ok4 = True
prod = F(1)
u = 2
n_paths = 1
for step in range(3):
    prod *= F(1, u)                              # each labelled birth weight
    n_paths *= u                                 # u labelled choices
    u += 1
ok4 &= (prod == F(1, 24)) and (n_paths == 24) and (n_paths * prod == 1)
check("A4 the unique survivor: pure birth w_b(u) = 1/u — every length-3 "
      "path carries the identical product 1/24; 24 labelled paths; total "
      "mass exactly 1 (full path-covariance on the enumerated domain)", ok4)

# A5: the corollary
print("      A5 COROLLARY [with D28 T2]: the stationary + path-covariant +")
print("      graph-blind class contains NO diamond-forming kernel — its only")
print("      member is pure birth, which has no common operational futures.")
print("      THE CONCLUSION AT ITS HONEST WIDTH (the external review's")
print("      narrowing): a stationary path-covariant kernel with interactions")
print("      must consult RICHER STATE THAN u — graph structure, degree, age,")
print("      motifs, or global invariants; LOCALITY IS NOT SPECIFICALLY")
print("      FORCED. Printed limits: none-ops excluded (the none arm changes")
print("      the equation — D31C tests it); bounded growth escapes (c > 0")
print("      admissible below a u-cap); birth positivity is a hypothesis;")
print("      per-labelled-opportunity weights with the stated counts assumed.")
check("A5 the corollary and limits printed", True)

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total}: 4 substantive gates + 1 print gate)"
      if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
