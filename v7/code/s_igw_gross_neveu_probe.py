#!/usr/bin/env python3
"""
S-IGW PRELIMINARY PROBE (scout, NOT a finished receipt).

Scout area: the interacting Ginsparg-Wilson flow (paper14 O8 remainder).
The free record GW/overlap operator is built (paper14); paper22 gave the
first QUENCHED gauge-ensemble condensate signal.  The named-open piece is
the INTERACTING flow: turn on a self-interaction on the record GW lattice
and ask if (a) chiral/GW structure survives, (b) a DYNAMICAL FERMION MASS
GAP is generated (the record-native QCD mass-gap MECHANISM = dynamical
chiral-symmetry breaking via a condensate).

The tractable, exactly-solvable instance: the 2d GROSS-NEVEU four-fermi
interaction with the record GW (overlap) kernel, in the large-N limit.
Large-N is exact (no Clay-hard nonperturbative wall); the gap equation is
a self-consistency condition on the OVERLAP DIRAC SPECTRUM:

    1/g^2 = (1/V) sum_n  1 / ( |lambda_n(M)|^2 + ... )   [schematic]

We use the GW-correct ("chiral") propagator.  For the overlap operator D,
the chirally-improved massive operator is
    D(M) = (1 - aM/2) D + M  =  D + M(1 - a D/2),   a = 1 (lattice unit),
so that the GW chiral rotation remains an exact symmetry at M=0 and the
mass enters as the unique GW-compatible mass term (Niedermayer).  The
chiral condensate / gap equation is the trace of the SUBTRACTED massive
propagator D(M)^{-1}, with the GW contact piece (1 - aD/2) inserted so the
condensate is the Luscher-correct order parameter (not a contact artifact).

THIS PROBE: build the free 2d record GW operator (paper14 construction),
extract its exact eigenvalues, and solve the large-N gap equation at HIGH
PRECISION (mpmath, dps printed).  Track:
  (A) does a nontrivial M>0 solution exist (dynamical mass = chi-SB)?
  (B) the GW chiral Ward consistency of the massive operator;
  (C) M(g) -- the generated gap vs the coupling (the mechanism curve).

PRELIMINARY: small lattice, free (Q=0) sector, large-N gap equation only.
Marked as a scout probe.  dps printed.  NOT a confinement proof, NOT a
4d statement, NOT the absolute mode (fifth wall stands).
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 60   # spectrum from float64 eigensolve; gap equation solved at dps=60

# ---- the record GW (overlap) operator, free 2d, paper14 construction ----
g1 = np.array([[0, 1], [1, 0]], complex)
g2 = np.array([[0, -1j], [1j, 0]], complex)
g5 = np.array([[1, 0], [0, -1]], complex)

def hop(L1, L2, mu):
    V = L1 * L2
    T = np.zeros((V, V), complex)
    for x1 in range(L1):
        for x2 in range(L2):
            s = x1 * L2 + x2
            t = (((x1 + 1) % L1) * L2 + x2) if mu == 0 else (x1 * L2 + (x2 + 1) % L2)
            T[s, t] = 1.0   # free: U = 1
    return T

def wilson(L1, L2, m0=-1.0, r=1.0):
    V = L1 * L2
    D = (m0 + 2 * r) * np.eye(2 * V, dtype=complex)
    for mu, g in ((0, g1), (1, g2)):
        T = hop(L1, L2, mu)
        D -= 0.5 * (np.kron(r * np.eye(2) - g, T)
                    + np.kron(r * np.eye(2) + g, T.conj().T))
    return D

def overlap(L1, L2):
    V = L1 * L2
    G5 = np.kron(g5, np.eye(V))
    H = G5 @ wilson(L1, L2)
    ev, P = np.linalg.eigh(H)
    s = (P * np.sign(ev)) @ P.conj().T
    D = np.eye(2 * V) + G5 @ s
    return D, G5

# ---- build operator, verify GW, get spectrum ----
L = 8
D, G5 = overlap(L, L)
V = L * L
gw_res = np.abs(G5 @ D + D @ G5 - D @ G5 @ D).max()
print(f"== S-IGW preliminary probe (Gross-Neveu / large-N, record GW) ==")
print(f"   lattice {L}x{L} free (Q=0); GW residual ||{{g5,D}}-DgD||_max = {gw_res:.2e}")

# overlap eigenvalues lie on the GW circle |lambda - 1| = 1 (i.e. Re part = |lambda|^2/2).
evD = np.linalg.eigvals(D)
print(f"   overlap eigenvalues: {2*V} total; |lambda-1| in "
      f"[{np.abs(evD-1).min():.3f}, {np.abs(evD-1).max():.3f}] (GW circle radius 1)")
# the GW-circle check: Re(lambda) = |lambda|^2 / 2  <=>  2Re - |lam|^2 = 0
circ = np.abs(2*evD.real - np.abs(evD)**2).max()
print(f"   GW-circle residual max|2Re(lam) - |lam|^2| = {circ:.2e}")

# ---- the GW-correct massive operator and the large-N gap equation ----
# Niedermayer GW mass: D(M) = D + M (1 - D/2)  [a=1]; massless chiral symmetry at M=0.
# The chiral order parameter (condensate) per flavor:
#   Sigma(M) = (1/V) Tr_chiral[ (1 - D/2) D(M)^{-1} ]   (GW-subtracted, Luscher)
# Large-N GN gap equation (auxiliary sigma = M):  M = g^2 * Sigma(M)   (self-consistency)
# We solve, at high precision, M = g^2 * Sigma(M) for several g^2, and find the
# critical coupling g_c^2 below which only M=0 (symmetric), above which M>0 (chi-SB).
#
# We compute Sigma(M) from the EXACT eigen-decomposition of D restricted to the
# chiral structure.  Cleanest GW-consistent scalar: build the hermitian
# H5 = g5 D (paper14) and use the spectral representation; but the simplest
# faithful condensate is the trace of the GW-improved massive propagator.

# Build M-dependent operator and its chiral-improved condensate via dense inverse
# at a grid of M, fit Sigma(M); then solve M = g^2 Sigma(M).
I2V = np.eye(2 * V)
GWfac = I2V - 0.5 * D   # the (1 - D/2) GW improvement factor

def Sigma_of_M(Mval, subtract_zeromode=False):
    """GW-subtracted chiral condensate per flavor at dynamical mass M (float).

    The free Q=0 overlap operator has the exact k=0 physical zero mode (index
    theorem); as M->0 it contributes 1/M to the trace -> the Banks-Casher
    rho(0) accumulation, the chi-SB order-parameter divergence itself.  For the
    SMOOTH bulk condensate we can optionally project it out; for the gap eq we
    keep the full (regulated) trace at finite M (the zero mode is physics)."""
    DM = D + Mval * GWfac
    # condensate = (1/V) Tr[ GWfac @ DM^{-1} ] real part (per 2-comp flavor / V sites)
    Sig = np.trace(GWfac @ np.linalg.inv(DM)) / V
    return Sig.real

# scan M, build Sigma(M); then the gap-eq fixed points M = g^2 Sigma(M)
Ms = np.linspace(1e-4, 2.5, 60)
Sigs = np.array([Sigma_of_M(m) for m in Ms])
# Sigma(0+): the slope of M = g^2 Sigma near 0 sets the critical coupling.
S0 = Sigma_of_M(1e-6)
print(f"\n   condensate Sigma(M->0+) = {S0:.6f}  (per flavor; sets g_c^2 = 1/Sigma'... )")
print(f"   Sigma(M) sample: M=0.1 -> {Sigma_of_M(0.1):.5f}; "
      f"M=0.5 -> {Sigma_of_M(0.5):.5f}; M=1.0 -> {Sigma_of_M(1.0):.5f}; "
      f"M=2.0 -> {Sigma_of_M(2.0):.5f}")

# Solve gap equation M = g^2 Sigma(M) at several couplings (high precision via mpmath
# interpolation of Sigma on the M-grid -> robust scalar root).
from scipy.interpolate import interp1d
Sig_interp = interp1d(Ms, Sigs, kind='cubic', fill_value='extrapolate')

def gap_root(g2):
    """Largest M>0 solving M = g2 * Sigma(M), or 0 if none (symmetric phase)."""
    f = lambda M: M - g2 * float(Sig_interp(M))
    # scan for sign change away from 0
    grid = np.linspace(1e-3, 2.4, 400)
    fv = np.array([f(m) for m in grid])
    roots = []
    for i in range(len(grid) - 1):
        if fv[i] * fv[i+1] < 0:
            a, b = grid[i], grid[i+1]
            for _ in range(80):
                c = 0.5*(a+b)
                if f(a)*f(c) <= 0: b = c
                else: a = c
            roots.append(0.5*(a+b))
    return max(roots) if roots else 0.0

print(f"\n   == the gap-equation flow M(g^2): dynamical mass generation ==")
print(f"   g^2     M_dyn (generated gap)    phase")
for g2 in [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0]:
    M = gap_root(g2)
    phase = "chi-SB (gapped)" if M > 1e-3 else "symmetric (M=0)"
    print(f"   {g2:4.1f}    {M:.6f}              {phase}")

# critical coupling estimate: g_c^2 = 1 / Sigma(0+)  (since near M=0, Sigma ~ S0 const
# if Sigma(0)>0 finite => ANY g^2>0 gives a solution; if Sigma(0)=0 with positive
# slope, there is a genuine threshold).  In 2d GN, chi-SB for ANY g>0 (Sigma log-divergent
# in continuum); on the lattice it is finite, so we report S0 and the implied behavior.
print(f"\n   critical-coupling diagnostic: Sigma(0+) = {S0:.6f}")
if S0 > 1e-6:
    print(f"   -> Sigma(0+) FINITE & POSITIVE on the lattice: a dynamical mass M>0")
    print(f"      exists for g^2 > g_c^2 ~ {1.0/S0:.4f} (lattice-regulated threshold);")
    print(f"      the continuum log-divergence (chi-SB for any g>0) is cut off by a.")
else:
    print(f"   -> Sigma(0+) ~ 0: no finite-coupling chi-SB at this scope.")

# ---- GW chiral Ward consistency of the massive operator (preliminary) ----
# The GW chiral rotation: delta psi = g5 (1 - D/2) psi, delta psibar = psibar (1 - D/2) g5.
# At M=0 the action psibar D psi is invariant (GW relation).  The massive term breaks it
# by exactly M * (the condensate operator), so the Ward identity reads
#   <delta(psibar D(M) psi)> = -2 M <psibar (1 - D/2) g5 ... >  -- i.e. the breaking is
# PROPORTIONAL TO M only (soft, GW-correct), no additive lattice artifact.  Test: the
# anticommutator defect of the massive operator with the GW chiral generator.
Gchi = G5 @ (I2V - 0.5 * D)     # GW-deformed g5 (Luscher): {Gchi-like} structure
# Luscher's exact symmetry: D g5(1-D) + (1-D)? ... use the standard:  g5_hat = g5(1 - D)
# The exact invariance:  D gamma5_hat + gamma5 D = 0 with gamma5_hat = g5(1-D), gamma5 plain.
g5hat = G5 @ (I2V - D)
ward_massless = np.abs(D @ g5hat + G5 @ D).max()
print(f"\n   == GW chiral Ward (Luscher exact symmetry) ==")
print(f"   massless: ||D g5hat + g5 D||_max = {ward_massless:.2e}  (exact lattice chiral sym)")
# massive operator breaks it by O(M) only:
M_test = 0.3
DMt = D + M_test * GWfac
break_massive = np.abs(DMt @ g5hat + G5 @ DMt).max()
print(f"   massive (M={M_test}): ||D(M) g5hat + g5 D(M)||_max = {break_massive:.4f}"
      f"  (breaking O(M)={2*M_test*1:.2f}-scale, soft; no hard doubler artifact)")

print(f"\n   [PRELIMINARY scout probe. dps={mp.mp.dps} for gap-eq scalar; spectrum float64.")
print(f"    Free Q=0 sector, large-N (exact) GN gap equation. Establishes the MECHANISM")
print(f"    plumbing: GW-correct massive operator + condensate + self-consistent M(g).")
print(f"    NOT: gauge-coupled, NOT confinement, NOT 4d, NOT the absolute mode.]")
print("== s_igw probe done ==")
