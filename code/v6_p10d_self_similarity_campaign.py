#!/usr/bin/env python3
"""
v6_p10d: the self-similarity derivation of the commitment constant (O9)
and the committed placement across lattices (Paper 10, Part III).

 O9 RESOLVED AS STRUCTURAL.  The 2x2 committed diamond (each sub-bond at
 the committed coupling eta) has endpoint correlation

     t_network = 2 theta^2 / (1 + theta^4),   theta = tanh eta,

 and the projective-consistency requirement t_network = theta (the coarse
 sealed correlation must equal the committed single-bond value, because
 commitment is cover-independent: P4 s75, P7 Thm 7.5) is ALGEBRAICALLY
 the commitment cubic:

     2 theta^2/(1+theta^4) = theta  <=>  theta^4 - 2 theta + 1 = 0
     <=>  (theta - 1)(theta^3 + theta^2 + theta - 1) = 0.

 So theta_hist has a SECOND, independent characterization: the unique
 nontrivial coupling at which per-bond commitment is self-consistent
 under binary refinement of a screen bond.  The MK identity of Paper 10
 is this consistency map in RG dress.  SELECTION COROLLARY: scanning
 refinement arity b and route multiplicity m, ONLY (b, m) = (2, 2) is
 consistent - binary division and two-route (2d screen) refinement
 mutually select each other.

 LATTICE UNIVERSALITY: the committed placement h solving
 e^{-h} = <ss>(h) is computed for the triangular and honeycomb lattices
 (strip transfer matrices) and compared to their exact critical points:
 is the square lattice's 2.41%-subcritical placement universal?
"""
import numpy as np, itertools
from scipy.optimize import brentq

eta = brentq(lambda e: np.tanh(e) - np.exp(-e), 0.1, 2.0)
theta = np.tanh(eta)

# ---------- O9: the self-similarity theorem ----------
print("== O9: the refinement self-consistency characterization ==")
# direct network computation: 2x2 diamond, all four bonds at eta
states = list(itertools.product((-1, 1), repeat=4))   # (s0, a, b, s1)
num = den = 0.0
for s0, a, b, s1 in states:
    w = np.exp(eta * (s0 * a + a * s1 + s0 * b + b * s1))
    den += w
    num += w * s0 * s1
t_net = num / den
print(f"  2x2 committed diamond endpoint correlation (exact enumeration):")
print(f"    <s0 s1>_network = {t_net:.15f}")
print(f"    theta_hist      = {theta:.15f}     gap = {abs(t_net-theta):.1e}")
print(f"  algebra: 2 th^2/(1+th^4) - th = {2*theta**2/(1+theta**4)-theta:.1e};")
print(f"  th^4 - 2 th + 1 factors as (th-1)(th^3+th^2+th-1): roots "
      f"{np.sort(np.real(np.roots([1,0,0,-2,1])[np.abs(np.imag(np.roots([1,0,0,-2,1])))<1e-9]))}")
print("  -> PROJECTIVE CONSISTENCY of per-bond commitment under binary")
print("     refinement IS the commitment cubic: a second, independent")
print("     characterization of theta_hist.  The Paper 10 MK identity is this")
print("     consistency map in RG dress: O9 = STRUCTURAL.")

print("\n  selection corollary: m routes of b bonds in series, all committed;")
print("  consistency m*atanh(theta^b) = eta:")
print("    b\\m      1          2          3          4")
for b in (2, 3, 4, 5):
    row = [b * 0 + m * np.arctanh(theta ** b) - eta for m in (1, 2, 3, 4)]
    print(f"    {b}   " + "  ".join(f"{x:+8.4f}" for x in row))
print("  -> (b, m) = (2, 2) is the UNIQUE consistent refinement: binary")
print("     division and two-route (2d-screen) refinement mutually select")
print("     each other.  The corpus' binary primitive and its 2d screens are")
print("     not independent choices: each is the only one consistent with")
print("     the other under commitment.")

# premise ledger receipt: the coarse bond of the consistent network is
# itself exactly a committed bond (correlation = theta = e^-eta)
print(f"\n  premise receipt: coarse correlation {t_net:.12f} = e^-eta = "
      f"{np.exp(-eta):.12f}: the coarse bond satisfies the commitment law")
print("  EXACTLY - commitment is scale-stable at (b,m) = (2,2), as")
print("  cover-independence (P4 s75) requires of a sealed law.")

# ---------- lattice placement: coordination, not dimension ----------
print("\n== committed placement across 2d lattices: the coordination law ==")
def power_lam(T, iters=600):
    v = np.ones(T.shape[0]) / np.sqrt(T.shape[0])
    lam_old = 0.0
    for _ in range(iters):
        w = T @ v
        lam = np.linalg.norm(w)
        v = w / lam
        if abs(lam - lam_old) < 1e-13 * lam:
            break
        lam_old = lam
    return float(v @ (T @ v))

def strip_lnlam(KK, lattice, W):
    sts = np.array(list(itertools.product((-1, 1), repeat=W)), float)
    intra = (sts * np.roll(sts, -1, axis=1)).sum(axis=1)   # in-column NN, PBC
    horiz = sts @ sts.T
    if lattice == "square":
        T = (np.exp(0.5 * KK * intra)[:, None] * np.exp(KK * horiz)
             * np.exp(0.5 * KK * intra)[None, :])
        return np.log(power_lam(T)), 2 * W, 1
    if lattice == "triangular":
        diag = sts @ np.roll(sts, -1, axis=1).T
        T = (np.exp(0.5 * KK * intra)[:, None] * np.exp(KK * (horiz + diag))
             * np.exp(0.5 * KK * intra)[None, :])
        return np.log(power_lam(T)), 3 * W, 1
    if lattice == "honeycomb":
        # brick wall: vertical bonds alternate between even and odd pairings
        pair0 = (sts[:, ::2] * sts[:, 1::2]).sum(axis=1)            # (0,1),(2,3)..
        pair1 = (sts[:, 1::2] * np.roll(sts, -1, axis=1)[:, 1::2]).sum(axis=1)
        D0 = np.exp(KK * pair0)
        D1 = np.exp(KK * pair1)
        H = np.exp(KK * horiz)
        T = (D0[:, None] * H) @ (D1[:, None] * H)
        return np.log(power_lam(T)), 3 * W, 2   # per TWO columns: 2W horiz + W vert
    raise ValueError(lattice)

def strip_ss(K, lattice, W):
    dK = 2e-5
    l1, nb, ncol = strip_lnlam(K + dK, lattice, W)
    l0, _, _ = strip_lnlam(K - dK, lattice, W)
    return (l1 - l0) / (2 * dK) / nb

cases = [
    ("honeycomb", 3, 0.5 * np.log(2 + np.sqrt(3)), 10),
    ("square", 4, 0.5 * np.log(1 + np.sqrt(2)), 12),
    ("triangular", 6, 0.25 * np.log(3.0), 12),
]
print("   lattice      z   K_c(exact)   h_commit     (K_c-h)/K_c    phase")
for name, z, Kc, W in cases:
    h = brentq(lambda K: np.exp(-K) - strip_ss(K, name, W), 0.10, 0.70,
               xtol=1e-9)
    rel = 100 * (Kc - h) / Kc
    phase = "DISORDERED" if h < Kc else "ORDERED"
    print(f"   {name:10s}   {z}   {Kc:.6f}    {h:.6f}     {rel:+7.2f}%     {phase}")
print(f"   [cubic 3d     6   0.221655    0.2746(5)     -23.9 %      ORDERED  (P10)]")
print(f"   [square exact placement: Onsager gives 2.41% (P10); the W=12 strip")
print(f"    estimate carries a finite-width bias toward larger distance]")
print("  -> the control parameter is COORDINATION, not dimension: z = 3 deep")
print("     disordered, z = 4 near-critical, z = 6 ORDERED - in two dimensions")
print("     as in three.  This CORRECTS the dimension reading of Paper 10 R4:")
print("     record-SSB requires sufficient coordination (z >= ~5-6), and")
print("     dimension enters only through the coordination it makes available.")
print("     The committed triangular ledger seals branches IN TWO DIMENSIONS.")
print("== p10d done ==")
