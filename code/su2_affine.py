#!/usr/bin/env python3
"""
TARGET II, STEP 3 (continued): the non-abelian MAGNETIC DUAL -- affine SU(2)_k modular data and the
't Hooft Z_2 flux theta (paper 42, Part II, §19.3). The frontier from §19.2: U(1) confinement rides
on Poisson SELF-duality (electric<->monopole) with the scale as a theta cusp; SU(2) has no literal
Poisson dual, so we need the non-abelian electric-magnetic modular structure. Two pieces:

(1) The modular DATA is concrete and exact: affine SU(2)_k characters carry an SL(2,Z) representation
    via the Kac-Peterson matrices
        S_{a b} = sqrt(2/(k+2)) sin(pi a b/(k+2)),  a=2j+1 in {1,...,k+1}
        T_{a a} = exp(2 pi i (h_j - c/24)),  h_j = j(j+1)/(k+2),  c = 3k/(k+2).
    Verified here: S symmetric + unitary, S^2 = C = I (SU(2) self-conjugate), (ST)^3 = S^2 up to the
    central phase. This is the rep-theoretic non-abelian S-transform (it MIXES irreps -- Verlinde).

(2) The genuine 4D magnetic dual is 't Hooft's: on T^4, SU(2)/Z_2 partition functions split into
    fluxes (e,m) in Z_2 x Z_2 (electric, magnetic), and the modular S of a 2-torus swaps e<->m. The
    flux sum is a finite Z_2 theta; confinement <-> the electric-flux free energy. This structure is
    EXACT/kinematic; the flux FREE ENERGIES are 4D-dynamical (unsolvable) -- that is the open core.

This module verifies (1) and states (2). It does NOT claim the dynamical confinement result.
"""
import numpy as np


def kac_peterson(k):
    a = np.arange(1, k + 2)                          # a = 2j+1, j = 0,1/2,...,k/2
    A, B = np.meshgrid(a, a, indexing="ij")
    S = np.sqrt(2.0 / (k + 2)) * np.sin(np.pi * A * B / (k + 2))
    j = (a - 1) / 2.0
    h = j * (j + 1) / (k + 2)
    c = 3.0 * k / (k + 2)
    T = np.diag(np.exp(2 * np.pi * 1j * (h - c / 24.0)))
    return S, T, h, c


def check_sl2z(k):
    S, T, h, c = kac_peterson(k)
    n = k + 1
    I = np.eye(n)
    sym = np.max(np.abs(S - S.T))
    unit = np.max(np.abs(S @ S.conj().T - I))
    s2 = np.max(np.abs(S @ S - I))                   # S^2 = C = I for SU(2)
    ST3 = np.linalg.matrix_power(S @ T, 3)
    # (ST)^3 = S^2 up to a global phase (the c/24 framing anomaly); divide it out
    phase = ST3[0, 0] / (S @ S)[0, 0] if abs((S @ S)[0, 0]) > 1e-12 else ST3[0, 0]
    st3 = np.max(np.abs(ST3 - phase * (S @ S)))
    return sym, unit, s2, st3, abs(phase), c


if __name__ == "__main__":
    print("=" * 78)
    print("TARGET II / STEP 3 cont.: non-abelian magnetic dual -- affine SU(2)_k modular data")
    print("=" * 78 + "\n")
    print("(1) Kac-Peterson SL(2,Z) representation (the rep-theoretic non-abelian S-transform):")
    print("   k    dim   |S-S^T|   |SS*-I|   |S^2-I|   |(ST)^3 - phase*S^2|   c=3k/(k+2)")
    for k in (1, 2, 3, 4, 8, 16):
        sym, unit, s2, st3, ph, c = check_sl2z(k)
        print(f"   {k:>2}   {k+1:>3}   {sym:.1e}   {unit:.1e}   {s2:.1e}        {st3:.1e}          {c:.4f}")
    print("   => S,T satisfy the modular relations exactly (S^2=I, (ST)^3=S^2 up to the c/24 phase).")
    print("      The S-transform mixes irreps (Verlinde fusion) -- NOT a simple e<->m swap.\n")

    print("(2) cusp data (q->0 leading exponents h_j - c/24 of the characters), e.g. k=4:")
    S, T, h, c = kac_peterson(4)
    for jj, hh in enumerate(h):
        print(f"     j={jj/2:.1f}:  h_j - c/24 = {hh - c/24:+.4f}")
    print("   These are 2D-CFT conformal weights (dimensionless), NOT the 4D scale Lambda.\n")

    print("HONEST STATUS (paper 42 §19.3):")
    print(" - The non-abelian modular DATA exists and is exact (affine S-matrix; verified above).")
    print(" - The right MAGNETIC DUAL for 4D confinement is 't Hooft's Z_2 flux theta on T^4")
    print("   (fluxes (e,m) in Z_2xZ_2, modular S swaps e<->m) -- kinematic/exact.")
    print(" - OPEN CORE (not done, not faked): showing the electric-flux free energy / string tension")
    print("   is the CUSP DATUM of that flux theta, with Lambda ~ e^{-1/(2 b0 g^2)} as the cusp scale.")
    print("   That is 4D dynamics (unsolvable in closed form). The conjecture is now PRECISE; it is")
    print("   NOT proved. This is the genuine open problem Target II reduces to.")
