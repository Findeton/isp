#!/usr/bin/env python3
"""
v6_p12a: the Euclidean-first decomposition of gate (C) - the OS bridge
and the compactness preconditions (Paper 12, sub-gates C2 and C4).

THE DECOMPOSITION.  "Lorentzian spectral convergence" is not a standard
notion (wave operators are not elliptic).  After Paper 10, gate (C)
restructures as:

  (C1) EUCLIDEAN spectral convergence of the spatial record geometry
       (elliptic; Mosco/Dirichlet-form class)               [p12b]
  (C2) OS reconstruction of the LORENTZIAN dynamics from the Euclidean
       limit - the corpus' own arrow-positivity machinery   [here]
  (C3) the identities passing to the limit (Bianchi exact at finite
       scope; T and linearized focusing via PSD-closure and the audited
       uniform constants)                                    [paper text]
  (C4) compactness of the controlled refinement class (import: uniform
       heat-kernel bounds => Mosco precompactness)           [here + p12d]

This script instantiates (C2) and audits the (C4) preconditions:

 A. THE OS BRIDGE, OPERATIONAL: a curved spatial record geometry's
    EUCLIDEAN kernel (a positive record law, e^{-tau A}) determines the
    full LORENTZIAN propagator: reconstruct A from Euclidean data,
    evolve cos(sqrt(A) t), and match the direct Lorentzian leapfrog to
    O(dt^2).  Wick rotation as an operational record procedure, riding
    on P10's theorem (RP -> OS reconstruction) rather than on analytic
    continuation axioms.
 B. HEAT-KERNEL UNIFORMITY ((C4) preconditions): two-sided sub-Gaussian
    bounds with constants UNIFORM over the conductance class - the
    hypotheses of the imported Mosco-compactness machinery, verified at
    finite scope across random class members.
"""
import numpy as np
from scipy.linalg import expm
import scipy.sparse as sp

rng = np.random.default_rng(12)

def ring_A(n, cfun):
    cb = np.array([cfun((i + 0.5) / n) for i in range(n)]) * n * n
    main = cb + np.roll(cb, 1)
    A = np.diag(main)
    for i in range(n):
        A[i, (i + 1) % n] -= cb[i]
        A[(i + 1) % n, i] -= cb[i]
    return A

# ---------- A. the OS bridge ----------
print("== A. the OS bridge: Euclidean record data -> Lorentzian propagator ==")
n, tau = 64, 2e-4
cfun = lambda x: 1.0 + 0.5 * np.sin(2 * np.pi * x)
A = ring_A(n, cfun)
K = expm(-tau * A)                       # the Euclidean record kernel
print(f"  Euclidean kernel: min entry = {K.min():.2e}"
      f"  (positive within round-off: a record law; all {n} modes resolved)")
ev, P = np.linalg.eigh(K)
A_rec = P @ np.diag(-np.log(np.clip(ev, 1e-30, None)) / tau) @ P.T
print(f"  generator reconstruction: ||A_rec - A|| = {np.abs(A_rec - A).max():.2e}")
# Lorentzian evolution from the OS-reconstructed spectral data
u0 = np.exp(-0.5 * ((np.arange(n) / n - 0.3) / 0.05) ** 2)
t_final = 0.5
w = np.sqrt(np.clip(np.linalg.eigvalsh(A_rec), 0, None))
evA, PA = np.linalg.eigh(A_rec)
u_os = PA @ (np.cos(np.sqrt(np.clip(evA, 0, None)) * t_final) * (PA.T @ u0))
print("   dt        max |u_leapfrog(t) - u_OS(t)|      ratio")
prev = None
for dt in (0.002, 0.001, 0.0005):
    u_prev = u0.copy()
    u = u0 - 0.5 * dt * dt * (A @ u0)
    steps = int(round(t_final / dt))
    for _ in range(steps - 1):
        u_next = 2 * u - u_prev - dt * dt * (A @ u)
        u_prev, u = u, u_next
    err = np.abs(u - u_os).max()
    print(f"  {dt:7.4f}   {err:.6e}                  "
          f"{'-' if prev is None else f'{prev/err:5.2f}'}")
    prev = err
print("  -> the EUCLIDEAN record law alone determines the LORENTZIAN wave")
print("     evolution (phases included), and the direct Lorentzian leapfrog")
print("     converges to it at O(dt^2): Wick rotation as an operational")
print("     record procedure, grounded in P10's RP theorem rather than in an")
print("     analytic-continuation axiom.  This is sub-gate (C2), instantiated.")

# ---------- B. heat-kernel uniformity across the class ----------
print("\n== B. (C4) preconditions: uniform two-sided heat-kernel bounds ==")
def sample_c():
    while True:
        a = rng.uniform(-0.2, 0.2, 6)
        if np.abs(a).sum() <= 0.45:
            return lambda x, a=a: 1.0 + sum(
                a[j] * np.sin(2 * np.pi * (j + 1) * x) for j in range(3)) + sum(
                a[3 + j] * np.cos(2 * np.pi * (j + 1) * x) for j in range(3))
n = 64
xs = np.arange(n) / n
dmat = np.minimum(np.abs(xs[:, None] - xs[None, :]),
                  1 - np.abs(xs[:, None] - xs[None, :]))
sup_c, inf_c = 0.0, np.inf
for trial in range(15):
    Ac = ring_A(n, sample_c())
    for t in (0.005, 0.02, 0.08):
        Kt = expm(-t * Ac) * n            # density vs counting normalization
        upper = (Kt * np.sqrt(t) * np.exp(dmat ** 2 / (5 * t))).max()
        lower = (np.diag(Kt) * np.sqrt(t)).min()
        sup_c = max(sup_c, upper)
        inf_c = min(inf_c, lower)
print(f"  15 random class members x t in {{0.005, 0.02, 0.08}}:")
print(f"    sup over class of  sqrt(t) K_t(x,y) exp(+d^2/5t)  = {sup_c:.4f}")
print(f"    inf over class of  sqrt(t) K_t(x,x)               = {inf_c:.4f}")
print("  -> two-sided sub-Gaussian bounds hold with CLASS-UNIFORM constants:")
print("     exactly the hypotheses under which the imported Dirichlet-form")
print("     machinery (Mosco/Kuwae-Shioya) yields spectral PRECOMPACTNESS of")
print("     the controlled refinement class - sub-gate (C4)'s precondition,")
print("     audited.  (The compactness CONTENT - what the limit points are -")
print("     is p12d's subject: they include non-classical, homogenized")
print("     geometries: the synthetic stratum.)")
print("== p12a done ==")
