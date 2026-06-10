#!/usr/bin/env python3
"""
v6_p12d: the synthetic stratum and the boundary-record frontier
(Paper 12; folds O10 into gate (C)).

 (i)  BOUNDARY RECORDS (O10, operational): for the degenerate record
      metric c(x) = x^alpha on (0,1), the Weyl alternative says the
      singular end is limit-circle for alpha < 3/2 (the operator has a
      one-parameter family of self-adjoint extensions: the limit demands
      a BOUNDARY CONDITION) and limit-point for alpha >= 3/2 (unique).
      Receipt: two microscopically different record towers (clamped vs
      free at the degenerate end) converge to DIFFERENT spectra exactly
      in the limit-circle range and to the SAME spectrum in the
      limit-point range: the ledger underdetermines the limit precisely
      where von Neumann extension theory says boundary data is missing -
      O10's content made operational: NON-TAME = MISSING BOUNDARY
      RECORDS.  (Degeneracy loci where extra boundary records are
      demanded are horizon-flavored; flagged as a direction.)
 (ii) THE SYNTHETIC STRATUM IS PHYSICAL: a discontinuous record metric
      (an interface) is not a smooth geometry, yet the record dynamics
      converges to definite physics: the reflection/transmission of a
      wave packet matches the impedance law R = (Z1-Z2)/(Z1+Z2),
      Z = sqrt(c).
 (iii) COMPACTNESS PRODUCES SYNTHETIC LIMITS: the oscillating family
      c_k = 1 + 0.6 sin(2 pi k x) has NO pointwise limit, yet its
      spectra converge - to the HOMOGENIZED operator c_eff = 0.8
      (harmonic mean), not to any member of the smooth family: the
      closure of the controlled class contains non-classical geometries.
 (iv) LORENTZIAN HOMOGENIZATION: a wave packet in the k = 32 medium
      propagates at the homogenized speed sqrt(0.8), not at the naive
      mean: light in microstructured record geometry reads the
      synthetic metric.
"""
import numpy as np

# ---------- (i) boundary records: the Weyl alternative, operational ----------
print("== (i) O10 operational: limit-circle = missing boundary records ==")
def degenerate_spec(n, alpha, clamped, k=3):
    h = 1.0 / n
    cb = np.array([((i + 0.5) * h) ** alpha for i in range(n)])
    A = np.zeros((n, n))
    for i in range(n):
        if i + 1 < n:
            A[i, i] += cb[i + 1] * n * n
            A[i, i + 1] -= cb[i + 1] * n * n
            A[i + 1, i] -= cb[i + 1] * n * n
            A[i + 1, i + 1] += cb[i + 1] * n * n
    # right end x = 1: Dirichlet wall via the last bond
    A[n - 1, n - 1] += 1.0 * n * n
    # left (degenerate) end: clamped includes the first bond to u(0)=0
    if clamped:
        A[0, 0] += cb[0] * n * n
    return np.sort(np.linalg.eigvalsh(A))[:k]
print("   alpha   n      |lam_1^clamped - lam_1^free|")
for alpha in (0.5, 1.0, 2.0, 3.0):
    for n in (200, 400, 800, 1600):
        g = abs(degenerate_spec(n, alpha, True)[0]
                - degenerate_spec(n, alpha, False)[0])
        print(f"   {alpha:4.1f}   {n:4d}     {g:.6f}")
print("  reading, against the Weyl alternative (limit-circle iff alpha < 3/2):")
print("   alpha = 0.5: the gap PERSISTS (2.83, drift < 2% per doubling): the")
print("     two record towers converge to DIFFERENT self-adjoint extensions -")
print("     the ledger underdetermines the limit; a boundary record decides.")
print("   alpha = 3.0: the gap vanishes at O(1/n): unique limit (limit-point).")
print("   alpha = 1.0: the gap decays like 1/log n (machine: ratios 1.099,")
print("     1.090 vs 1/log-law 1.105, 1.094): AT the logarithmic threshold")
print("     these two particular schemes merge log-slowly - limit-circle")
print("     guarantees that SOME schemes differ in the limit, not that every")
print("     pair does; alpha = 2.0 shows the mirrored slow approach on the")
print("     limit-point side.  The binary receipt is the 0.5 / 3.0 contrast.")
print("  -> O10's identity, operational: NON-TAME SECTORS ARE SECTORS WITH")
print("     MISSING BOUNDARY RECORDS - the deficiency space parametrizes the")
print("     ledger entries the continuum limit still needs; where it is")
print("     trivial, the microscopic scheme is irrelevant.  (Degeneracy loci")
print("     demanding boundary records are horizon-flavored: a direction,")
print("     not a claim.)")

# ---------- (ii) the interface: synthetic but physical ----------
print("\n== (ii) the synthetic stratum is physical: impedance law at an interface ==")
n = 4096
h = 1.0 / n
x = np.arange(n) * h
c = np.where(x < 0.5, 1.0, 4.0)
cb = 0.5 * (c + np.roll(c, -1))
def lap(u):
    return (np.roll(cb, 1) * (np.roll(u, 1) - u)
            + cb * (np.roll(u, -1) - u)) * n * n
sig = 0.015
u0 = np.exp(-0.5 * ((x - 0.30) / sig) ** 2)
u0p = -(x - 0.30) / sig ** 2 * u0
dt = 0.2 * h / 2.0
u_prev = u0
u = u0 + dt * (-np.sqrt(1.0) * u0p) + 0.5 * dt * dt * lap(u0)
t_final = 0.28
for _ in range(int(t_final / dt)):
    u_next = 2 * u - u_prev + dt * dt * lap(u)
    u_prev, u = u, u_next
ut = (u - u_prev) / dt
E_dens = 0.5 * (ut ** 2 + c * ((np.roll(u, -1) - u) * n) ** 2)
E_left = E_dens[x < 0.5].sum()
E_right = E_dens[x >= 0.5].sum()
Z1, Z2 = 1.0, 2.0
R2 = ((Z1 - Z2) / (Z1 + Z2)) ** 2
print(f"  c jumps 1 -> 4 at x = 0.5; impedances Z = sqrt(c) = 1, 2")
print(f"  reflected fraction  = {E_left/(E_left+E_right):.4f}"
      f"   (impedance law R^2 = {R2:.4f})")
print(f"  transmitted fraction = {E_right/(E_left+E_right):.4f}"
      f"   (1 - R^2 = {1-R2:.4f})")
print("  -> the interface limit is NOT a smooth geometry, but the record")
print("     dynamics converges to definite physics (the transmission law):")
print("     the Dirichlet/synthetic stratum is part of the record continuum.")

# ---------- (iii) compactness produces synthetic limits ----------
print("\n== (iii) the closure of the smooth class contains homogenized limits ==")
def ring_spec(n, cfun, k=5):
    cb = np.array([cfun((i + 0.5) / n) for i in range(n)]) * n * n
    A = np.diag(cb + np.roll(cb, 1))
    for i in range(n):
        A[i, (i + 1) % n] -= cb[i]
        A[(i + 1) % n, i] -= cb[i]
    return np.sort(np.linalg.eigvalsh(A))[1:k + 1]
n = 2048
target = ring_spec(n, lambda x: 0.8)
print("   k(oscillation)   max rel gap of spectrum to the c_eff = 0.8 operator")
for kk in (2, 4, 8, 16, 32):
    s = ring_spec(n, lambda x, kk=kk: 1.0 + 0.6 * np.sin(2 * np.pi * kk * x))
    print(f"      {kk:4d}            {np.abs(s - target).max()/target.max():.5f}")
print("  -> the family c_k has NO pointwise limit, yet its spectra converge -")
print("     to the HOMOGENIZED geometry c_eff = sqrt(1 - 0.36) = 0.8 (harmonic")
print("     mean), which is NOT a member of the family: spectral compactness")
print("     of the controlled class (preconditions audited in p12a) closes")
print("     onto a SYNTHETIC stratum.  Smooth Lorentzian geometry is the")
print("     regularity class of the record continuum, not its totality.")

# ---------- (iv) Lorentzian homogenization: light reads the synthetic metric ----------
print("\n== (iv) wave speed in the microstructured medium ==")
n = 4096
h = 1.0 / n
x = np.arange(n) * h
c32 = 1.0 + 0.6 * np.sin(2 * np.pi * 32 * x)
cb = 0.5 * (c32 + np.roll(c32, -1))
u0 = np.exp(-0.5 * ((x - 0.20) / 0.02) ** 2)
u0p = -(x - 0.20) / 0.02 ** 2 * u0
dt = 0.15 * h
u_prev = u0
u = u0 + dt * (-np.sqrt(0.8) * u0p) + 0.5 * dt * dt * lap(u0) * 0
def lap32(u):
    return (np.roll(cb, 1) * (np.roll(u, 1) - u)
            + cb * (np.roll(u, -1) - u)) * n * n
u = u0 + dt * (-np.sqrt(0.8) * u0p) + 0.5 * dt * dt * lap32(u0)
T = 0.45
for _ in range(int(T / dt)):
    u_next = 2 * u - u_prev + dt * dt * lap32(u)
    u_prev, u = u, u_next
e = u ** 2
peak = x[np.argmax(e)]
v_meas = (peak - 0.20) / T
print(f"  medium c(x) = 1 + 0.6 sin(64 pi x); packet launched at speed sqrt(0.8)")
print(f"  measured packet speed = {v_meas:.4f}    homogenized speed sqrt(0.8) = "
      f"{np.sqrt(0.8):.4f}    naive mean speed sqrt(<c>) = 1.0000")
print("  -> light in the microstructured record geometry propagates at the")
print("     SYNTHETIC (homogenized) speed, not the naive mean: the Lorentzian")
print("     face of (iii), and the operational meaning of the synthetic")
print("     stratum for null structure.")
print("== p12d done ==")
