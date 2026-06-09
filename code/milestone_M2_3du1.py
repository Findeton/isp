#!/usr/bin/env python3
"""
Milestone M2 (paper 42, Part I): 3D compact U(1) -- Goepfert-Mack confinement.

M2 is the first GENUINELY confining case (unlike 2D, where the area law is a trivial
factorization). 3D compact U(1) confines for ALL beta:
  - STRONG coupling (small beta): trivial area law, like every compact gauge theory,
        sigma_lat = -log( I_1(beta)/I_0(beta) )   (leading strong-coupling, exact).
  - WEAK coupling (large beta): the DISTINCTIVE part -- confinement PERSISTS via a
        plasma of MONOPOLES (Polyakov 1977; Goepfert-Mack 1982, rigorous), with an
        EXPONENTIALLY SMALL string tension  sigma ~ exp(-c beta).
    Contrast: 4D compact U(1) DEconfines at weak coupling (Coulomb phase, beta>beta_c).
    So weak-coupling sigma>0 is the real M2 test, and it is hard (sigma exp. small).

The exact dual is a monopole Coulomb gas / sine-Gordon, built on the Jacobi-theta
structure of the Villain weight (paper 41 sec.48) -- i.e. the modular object that a
bootstrap certificate for this confinement would use (Part II, Milestone A).

This script establishes the exact confinement REFERENCE (sigma>0 for all beta) and
characterizes the bootstrap M2 gate honestly. The genuine loop-equation SDP that
*reproduces* the weak-coupling (monopole) sigma needs the abelian Makeenko-Migdal
module (Target I module 2, not yet built) and SDPB precision (sigma exp. small).
"""
import numpy as np
from scipy.special import iv


def sigma_strong(beta):
    """Leading strong-coupling area-law string tension (exact leading order, any d>=2)."""
    return -np.log(iv(1, beta) / iv(0, beta))


def monopole_scaling(beta, g3=0.2527):
    """Qualitative 3D U(1) monopole/Debye scaling (Polyakov/GM): orders of magnitude only.
    S_mon ~ 2 pi^2 beta g3 (lattice Coulomb self-energy g3~0.2527); fugacity z~e^{-S_mon};
    Debye mass m_D ~ sqrt(z); sigma ~ m_D (up to O(1) constants we do NOT fix here)."""
    S_mon = 2 * np.pi**2 * beta * g3
    z = np.exp(-S_mon)
    m_D = np.sqrt(z)
    return S_mon, z, m_D


def main():
    print("Milestone M2: 3D compact U(1) -- Goepfert-Mack confinement (sigma>0 for ALL beta)\n")

    print("(A) STRONG coupling -- exact leading area law sigma_lat = -log(I_1/I_0) > 0:")
    for beta in (0.5, 1.0, 2.0, 5.0):
        print(f"     beta={beta:4.1f}:  sigma_lat = {sigma_strong(beta):.5f}   (confining)")

    print("\n(B) WEAK coupling -- the DISTINCTIVE part: monopole plasma, sigma ~ exp(-c beta) > 0")
    print("     (Polyakov/Goepfert-Mack; orders of magnitude only, O(1) constants NOT fixed):")
    for beta in (2.0, 4.0, 8.0, 16.0):
        S, z, mD = monopole_scaling(beta)
        print(f"     beta={beta:5.1f}:  monopole action ~{S:6.2f}  fugacity z~{z:.2e}  m_D~{mD:.2e}  => sigma>0 (tiny)")

    print("\n(C) The 3D-vs-4D contrast (why M2 is a genuine test, not a triviality):")
    print("     3D compact U(1): confines for ALL beta (monopoles always proliferate). [GM]")
    print("     4D compact U(1): DEconfines for beta>beta_c~1 (Coulomb phase). [Guth; Froehlich-Spencer]")

    print("\n(D) Modular structure (paper 41 sec.48): the Villain weight is a Jacobi theta_3;")
    print("     the confining monopole/sine-Gordon dual is its modular transform -- i.e. the")
    print("     certificate that would prove this sigma>0 is a modular object (Part II, Milestone A).")

    print("\nM2 STATUS (honest):")
    print("  - Confinement REFERENCE established: 3D U(1) confines for all beta (sigma>0),")
    print("    strong-coupling exact + weak-coupling monopole (GM), distinct from 4D U(1).")
    print("  - The EASY part (strong coupling, sigma~O(1)) a bootstrap captures like 2D (M1).")
    print("  - The GENUINE part (weak-coupling monopole sigma, exp. small) is the M2 GATE:")
    print("    it requires the abelian Makeenko-Migdal loop-equation module + SDPB precision.")
    print("    => M2 = reference + structure + modular connection done; the bootstrap run that")
    print("       reproduces weak-coupling GM is the gated next implementation step.")


if __name__ == "__main__":
    main()
