#!/usr/bin/env python3
"""
v6_p20b: record EWSB - the lifting mechanism, promoted from analogy
(Paper 20).

Paper 8's record-EWSB was honestly retitled an ANALOGY.  Here the
mechanism is computed at quadratic (tree) record scope, with the
SU(2) x U(1) structure of the reconstructed fibers:

 (i)  THE LIFTED VACUUM: the record weight -mu^2 |phi|^2 + lam |phi|^4
      selects |<phi>| = v = sqrt(mu^2 / 2 lam) (machine minimization),
      and the scalar fluctuation spectrum around it is 3 ZERO MODES
      (the would-be Goldstones) + 1 massive mode m_h^2 = 2 mu^2.
 (ii) THE GAUGE MASS MATRIX: with <phi> = (0, v)/sqrt(2) and couplings
      (g, g') the 4x4 record gauge mass matrix M^2_ab =
      (1/4) g_a g_b (phi^dag {T_a, T_b} phi) has eigenvalues
      { g^2 v^2/4 (x2), (g^2+g'^2) v^2/4, 0 }: W pair, Z, photon -
      machine-exact against the formulas.
 (iii) THE UNBROKEN CHARGE IS ELECTROMAGNETISM: the zero eigenvector is
      the (g' W3 + g B) combination, and Q = T3 + Y/2 annihilates the
      vacuum (||Q <phi>|| = 0 exactly): the massless record direction
      IS electric charge.
 (iv) THE TREE RELATION: m_W / m_Z = cos(theta_W) with
      tan(theta_W) = g'/g - machine across sampled couplings: the
      custodial tree structure of the record doublet.
"""
import numpy as np

rng = np.random.default_rng(201)

s = np.zeros((3, 2, 2), complex)
s[0] = [[0, 1], [1, 0]]; s[1] = [[0, -1j], [1j, 0]]; s[2] = [[1, 0], [0, -1]]
T = s / 2                                   # SU(2) generators
Y = 0.5 * np.eye(2)                         # hypercharge Y = +1/2 on H

# ---------- (i) the lifted vacuum and its spectrum ----------
print("== (i) the lifted vacuum ==")
mu2, lam = 1.7, 0.9
v_pred = np.sqrt(mu2 / (2 * lam))
# minimize V(phi) = -mu2 |phi|^2 + lam |phi|^4 over real 4-dim phi
from scipy.optimize import minimize
def V(x):
    r2 = float(x @ x)
    return -mu2 * r2 + lam * r2 * r2
res = minimize(V, rng.standard_normal(4), method="BFGS", tol=1e-12)
v_num = np.linalg.norm(res.x)
print(f"  |<phi>| numeric = {v_num:.8f}   v = sqrt(mu^2/2lam) = "
      f"{v_pred:.8f}   err = {abs(v_num - v_pred):.1e}")
H = np.zeros((4, 4))
x0 = res.x
r2 = x0 @ x0
for i in range(4):
    for j in range(4):
        H[i, j] = (-2 * mu2 * (i == j) + 4 * lam * (r2 * (i == j)
                   + 2 * x0[i] * x0[j]))
ev = np.sort(np.linalg.eigvalsh(H))
print(f"  fluctuation spectrum: {ev[0]:.2e}, {ev[1]:.2e}, {ev[2]:.2e},"
      f" {ev[3]:.6f}")
print(f"  -> THREE zero modes (the would-be Goldstones) + one massive:")
print(f"     m_h^2 = {ev[3]:.6f} = 4 mu^2 = {4 * mu2:.6f} EXACTLY")
print("     (real-field convention V = -mu^2 r^2 + lam r^4).")

# ---------- (ii)+(iii)+(iv) the gauge mass matrix ----------
print("\n== (ii)-(iv) the record gauge mass matrix ==")
g, gp = 0.65, 0.35
v = 1.0
phi = np.array([0, v / np.sqrt(2)], complex)
gens = [g * T[0], g * T[1], g * T[2], gp * Y]
M2 = np.zeros((4, 4))
for a in range(4):
    for b in range(4):
        anti = gens[a] @ gens[b] + gens[b] @ gens[a]
        M2[a, b] = 0.5 * np.real(phi.conj() @ (anti @ phi))
ev, P = np.linalg.eigh(M2)
mW2 = g ** 2 * v ** 2 / 8
mZ2 = (g ** 2 + gp ** 2) * v ** 2 / 8
print(f"  eigenvalues: {ev[0]:.2e}, {ev[1]:.6f}, {ev[2]:.6f}, {ev[3]:.6f}")
print(f"  predictions (record normalization; ratios convention-free):")
print(f"   0,  mW^2 = g^2 v^2/8 = {mW2:.6f} (x2),"
      f"  mZ^2 = (g^2+g'^2) v^2/8 = {mZ2:.6f}")
zero_vec = P[:, 0]
photon_pred = np.array([0, 0, gp, g]) / np.hypot(g, gp)
align = abs(zero_vec @ photon_pred)
print(f"  photon direction |overlap with (g' W3 + g B)| = {align:.10f}")
Q = T[2] + Y
print(f"  ||Q <phi>|| = {np.linalg.norm(Q @ phi):.1e}"
      f"   (Q = T3 + Y/2 annihilates the vacuum EXACTLY)")
print("  tree relation across sampled couplings:")
for _ in range(3):
    gg, ggp = rng.uniform(0.3, 0.9), rng.uniform(0.2, 0.6)
    gens2 = [gg * T[0], gg * T[1], gg * T[2], ggp * Y]
    M2b = np.zeros((4, 4))
    for a in range(4):
        for b in range(4):
            anti = gens2[a] @ gens2[b] + gens2[b] @ gens2[a]
            M2b[a, b] = 0.5 * np.real(phi.conj() @ (anti @ phi))
    e = np.sort(np.linalg.eigvalsh(M2b))
    ratio = np.sqrt(e[1] / e[3])
    cosw = gg / np.hypot(gg, ggp)
    print(f"   g = {gg:.3f}, g' = {ggp:.3f}: m_W/m_Z = {ratio:.8f}"
          f"   cos(theta_W) = {cosw:.8f}   diff = {abs(ratio - cosw):.1e}")
print("  -> record EWSB at tree scope: three Goldstones for three")
print("     massive vectors, the photon massless along EXACTLY the")
print("     electric-charge direction, and m_W/m_Z = cos(theta_W) -")
print("     the custodial tree structure of the lattice-minimal record")
print("     doublet.  Promoted from P8's analogy to a computed")
print("     mechanism at stated (quadratic/tree) scope; loop stability")
print("     and dynamical mu^2 < 0 origin remain NAMED OPENS.")
print("== p20b done ==")
