#!/usr/bin/env python3
"""
d23_click_identifiability_exact.py — v10 D23: exact click identifiability
of interaction graph and coupling (pin: note-d23, committed pre-run).
Stdlib only; all arithmetic exact rationals (Pythagorean rotations,
Z-basis clicks).
Post-review upgrade (hostile round 1, mathematics/rebuild stream,
2026-07-12): closed forms gated at EVERY grid point (degree-<=2 identity),
print notation harmonized to the coupling g = sin^2 (the note's s), dead
code removed, gate/print count relabeled. Survived clean-room rebuild
(all 12 distributions identical).
"""
from fractions import Fraction as F

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def matvec(M, v):
    return [sum(M[i][j]*v[j] for j in range(len(v))) for i in range(len(M))]

def ry(c, s):   # rotation with rational cos=c, sin=s (c^2+s^2=1)
    return [[c, -s],[s, c]]

def cry(ctrl, targ, c, s, n=3):
    """controlled-Ry on n qubits: |1><1|_ctrl (x) Ry + |0><0|_ctrl (x) I."""
    dim = 2**n
    M = [[F(0)]*dim for _ in range(dim)]
    R = ry(c, s)
    for col in range(dim):
        bits = [(col >> (n-1-q)) & 1 for q in range(n)]
        if bits[ctrl] == 0:
            M[col][col] = F(1)
        else:
            t = bits[targ]
            for tnew in (0, 1):
                bits2 = list(bits); bits2[targ] = tnew
                row = sum(b << (n-1-q) for q, b in enumerate(bits2))
                M[row][col] += R[tnew][t]
    return M

# source preparation on A: Ry with (cos,sin)=(3/5,4/5) => P(A=1)=16/25
PREP_C, PREP_S = F(3,5), F(4,5)

# exact Pythagorean coupling grid: s_coupling = sin^2
GRID = [(F(1),F(0)), (F(24,25),F(7,25)), (F(4,5),F(3,5)),
        (F(3,5),F(4,5)), (F(7,25),F(24,25)), (F(0),F(1))]

def clicks(graph, c, s):
    """Z-basis click distribution over (a,b,c) for the given edge list,
    edges applied in the listed causal order."""
    psi = [F(0)]*8; psi[0] = F(1)
    # prepare A (qubit 0)
    P = [[F(0)]*8 for _ in range(8)]
    R = ry(PREP_C, PREP_S)
    for col in range(8):
        bits = [(col >> (2-q)) & 1 for q in range(3)]
        for anew in (0,1):
            b2 = list(bits); b2[0] = anew
            row = sum(bb << (2-q) for q, bb in enumerate(b2))
            P[row][col] += R[anew][bits[0]]
    psi = matvec(P, psi)
    for (u, v) in graph:
        psi = matvec(cry(u, v, c, s), psi)
    return [x*x for x in psi]   # exact probabilities

G_STAR = [(0,1),(0,2)]
G_CHAIN = [(0,1),(1,2)]

print("[d23 click identifiability — exact]")
# (i) normalization/positivity
okn = True
for g in (G_STAR, G_CHAIN):
    for (c, s) in GRID:
        p = clicks(g, c, s)
        okn &= sum(p) == 1 and all(x >= 0 for x in p)
check("(i) exact normalization + positivity, all graphs x couplings", okn)

# (ii) graph identifiability at every interior coupling; closed forms
# gated at EVERY grid point — both sides are polynomials of degree <= 2
# in the coupling g = sin^2, so the six grid points overdetermine them:
# the closed forms are identities on all of [0,1].
oki = True
for (c, s) in GRID[1:-1]:
    p1, p2 = clicks(G_STAR, c, s), clicks(G_CHAIN, c, s)
    oki &= (p1 != p2)
okf = True
for (c, s) in GRID:
    g = s*s   # the coupling (the note's s = sin^2)
    pC_star = sum(clicks(G_STAR, c, s)[k] for k in range(8) if k & 1)
    pC_chain = sum(clicks(G_CHAIN, c, s)[k] for k in range(8) if k & 1)
    okf &= pC_star == g*F(16,25) and pC_chain == g*g*F(16,25)
check("(ii) GRAPH IDENTIFIED: star != chain at every interior coupling "
      "(necessarily equal at the boundary couplings 0 and 1); closed forms "
      "P(C=1) = g*16/25 (star) vs g^2*16/25 (chain), g = sin^2 the coupling, "
      "gated at ALL six grid points (degree <= 2 => identities on [0,1])",
      oki and okf)

# (iii) coupling identifiability within each graph
okc = True
for gr in (G_STAR, G_CHAIN):
    laws = [tuple(clicks(gr, c, s)) for (c, s) in GRID]
    okc &= len(set(laws)) == len(laws)
    for (c, s) in GRID:
        pB = sum(clicks(gr, c, s)[k] for k in range(8) if (k >> 1) & 1)
        okc &= pB == (s*s)*F(16,25)
check("(iii) COUPLING IDENTIFIED: coupling -> click law injective on the "
      "grid; identifying statistic P(B=1) = g*16/25 exactly, g = sin^2 "
      "(the note's coupling s) — linear in the coupling => injective "
      "within each graph on [0,1]", okc)

# (iv) D19 reconciliation note (a print, not a re-proof)
print("      (iv) D19 contrast: these are instrumented one/two-record CLICK")
print("      statistics; D19's null lives at abstract-history shadows, and")
print("      the COHERENCE clause needs complete support (D21, receipt-carried).")
check("(iv) reconciliation printed", True)

# (v) the reality dictionary [LITERATURE]
print("      (v) THE IDENTIFIED GRAPH AND COUPLINGS OF THIS REALITY")
print("      [LITERATURE; PDG-class values; identified by the laboratory/")
print("      collider/solar-system click record over its tested energy domain]:")
for line in (
  "vertex e-e-gamma (QED):        alpha^-1 = 137.035999...",
  "vertex q-q-g (QCD):            alpha_s(M_Z) = 0.1180 +/- 0.0009",
  "weak vertices (W/Z):           G_F = 1.1663787e-5 GeV^-2 (CODATA), sin^2 th-hat(M_Z) = 0.23122 (MS-bar)",
  "Yukawa vertices (H-f-f):       y_t ~ 0.94 (MS-bar) ... (fermion mass ladder)",
  "Higgs self-coupling:           m_H = 125.20 +/- 0.11 GeV, lambda_H ~ 0.13",
  "EH coupling (graviton EFT):    kappa = 8 pi G / c^4, G = 6.67430e-11 m^3 kg^-1 s^-2",
  "beyond the printed list:       neutrino-mass (dim-5) operator + dark sector demanded (open per D20)",
):
    print("        " + line)
check("(v) the dictionary printed", True)

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total}: 3 substantive gates + 2 informational prints)"
      if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
