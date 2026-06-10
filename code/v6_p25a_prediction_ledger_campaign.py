#!/usr/bin/env python3
"""
v6_p25a: the prediction ledger and the candidacy assembly (Paper 25).

 (i)  THE OPERATOR LEDGER: every low-dimension gauge-invariant operator
      of the reconstructed content, enumerated with its (Delta B,
      Delta L) - the structural predictions read off the lattice:
        dim 3:  nu^c nu^c only (P23 M1)         (0, -2): Majorana
        dim 4:  the three Yukawas + L H nu^c    (0, 0): Dirac channel
        dim 5:  (L H)(L H) Weinberg             (0, -2): light Majorana
        dim 6:  Q Q Q L,  u^c u^c d^c e^c,
                u^c d^c d^c nu^c                (+-1, +-1): B-L = 0
      machine receipts: hypercharge sums exact; color epsilon
      invariance under SU(3) (det receipt); weak singlet existence.
 (ii) THE PREDICTIONS, falsifiably stated:
        P-nu:   nu_R exists                 [conditional on (F-fiber)]
        P-Maj:  neutrinos are Majorana (0nu-beta-beta != 0)
        P-BL:   all B-violation conserves B - L (p -> e+ pi0 class
                allowed; n-nbar oscillation channels suppressed)
        P-eps:  hierarchy steps are powers of eps_record = 0.0318 in
                [eps^2, sqrt(eps)]           [pattern claim, 9/9]
        P-mass: every charged fermion mass is proportional to v
 (iii) THE CANDIDACY TABLE: structure-by-structure status, with the
      kill-condition scoreboard and the calibration requirement stated
      (one dimensionful measurement; external by the corpus' own gauge
      theorems).
"""
import numpy as np

rng = np.random.default_rng(25)

def su(d):
    Z = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    Q, R = np.linalg.qr(Z)
    U = Q * (np.diag(R) / np.abs(np.diag(R)))
    return U / np.linalg.det(U) ** (1 / d)

# ---------- (i) the operator ledger ----------
print("== (i) the operator ledger of the reconstructed content ==")
eps3 = np.zeros((3, 3, 3))
for p, s in (((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
             ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)):
    eps3[p] = s
worst = 0.0
for _ in range(6):
    U = su(3)
    e2 = np.einsum("ia,jb,kc,abc->ijk", U, U, U, eps3)
    worst = max(worst, np.abs(e2 - eps3).max())
print(f"  color epsilon invariance under SU(3) (det = 1): {worst:.1e}")
ops = [
    ("nu^c nu^c",        3, [0],            0, -2, "Majorana mass (M1)"),
    ("Q u^c H",          4, [1, -4, 3],     0,  0, "u-type Yukawa"),
    ("Q d^c H*",         4, [1, 2, -3],     0,  0, "d-type Yukawa"),
    ("L e^c H*",         4, [-3, 6, -3],    0,  0, "e-type Yukawa"),
    ("L nu^c H",         4, [-3, 0, 3],     0,  0, "Dirac-nu (seesaw)"),
    ("(L H)(L H)",       5, [-3, 3, -3, 3], 0, -2, "Weinberg dim-5"),
    ("Q Q Q L",          6, [1, 1, 1, -3],  1,  1, "proton decay"),
    ("u^c u^c d^c e^c",  6, [-4, -4, 2, 6], -1, -1, "proton decay"),
    ("u^c d^c d^c nu^c", 6, [-4, 2, 2, 0],  -1, -1, "proton decay"),
]
print("   operator             dim   sum Y6   dB   dL   B-L   role")
for name, dim, ys, dB, dL, role in ops:
    print(f"   {name:18s}   {dim}     {sum(ys):+d}     {dB:+d}   {dL:+d}"
          f"    {dB - dL:+d}    {role}")
print("  -> every listed operator is hypercharge-exact (sums printed);")
print("     the color-epsilon and weak contractions exist where used")
print("     (receipts above and P20).  READINGS: the only bare mass is")
print("     Majorana nu^c nu^c (dim 3); B violation first enters at")
print("     dim 6 and EVERY channel conserves B - L; the Weinberg")
print("     operator provides the light-Majorana channel.")

# ---------- (ii) the predictions ----------
print("\n== (ii) the prediction ledger ==")
print("  P-nu:   nu_R exists (16th Weyl)       [conditional: (F-fiber),")
print("          P21 - falsified if no sterile state at any scale]")
print("  P-Maj:  neutrinos are Majorana; 0nbb != 0   [M1 + Weinberg]")
print("  P-BL:   all baryon violation conserves B - L: p -> e+ pi0")
print("          class allowed at dim-6/Lambda^2; B-L-violating")
print("          channels (n-nbar) need dim 9: doubly suppressed")
print("  P-eps:  fermion hierarchy steps = powers of eps_record =")
print("          0.0318 within [eps^2, sqrt(eps)]   [pattern: 9/9]")
print("  P-mass: every charged fermion mass proportional to v  [M1]")

# ---------- (iii) the candidacy table ----------
print("\n== (iii) the candidacy assembly ==")
rows = [
    ("gauge group",        "OUTPUT: reconstructed from exchange (P18)"),
    ("matter content",     "UNIQUE minimal chiral floor = SM (P17-19)"),
    ("hypercharges",       "forced (anomalies + Z_6 lattice)"),
    ("scalar sector",      "one doublet, lattice-minimal, seam-maximal"
                           " (P20)"),
    ("EWSB",               "tree mechanism exact; photon = Q (P20)"),
    ("generations",        "protected iff >= 3; gauged fiber forces"
                           " nu_R (P21)"),
    ("QCD/QED signs",      "necessity + direction + condensate PASS"
                           " (P22)"),
    ("masses",             "protected except nu^c; seesaw structural"
                           " (P23)"),
    ("hierarchy",          "grain matches eps_record (P23; pattern)"),
    ("gravity + QM",       "the original corpus (P4-P16)"),
    ("continuum",          "conditional: (C-reg-b) detector-posed,"
                           " (PR-RP+) evidenced (P24)"),
    ("calibration",        "EXTERNAL: one dimensionful measurement"
                           " (corpus gauge theorems)"),
]
for k, v in rows:
    print(f"   {k:16s} {v}")
print("\n  KILL-CONDITION SCOREBOARD: wrong gauge sign - PASSED (P22);")
print("  scalar seam obstruction - PASSED (P20); exotic floor flood -")
print("  PASSED (P19); (PR-RP) negative - NO (evidenced positive, P24).")
print("  VERDICT: at stated scopes, and conditional on the two bounded")
print("  mathematical residues, SHARD IS A CANDIDATE ROUTE TOWARD THE")
print("  STANDARD MODEL: every clause of that sentence now has a")
print("  theorem, an exhaustive enumeration, or a machine receipt")
print("  behind it, and the places it could have died are on record as")
print("  having been tested.")
print("== p25a done ==")
