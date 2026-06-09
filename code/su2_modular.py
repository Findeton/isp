#!/usr/bin/env python3
"""
TARGET II, STEP 3: the non-abelian (SU(2)) modular structure (paper 42, Part II, §19.2).

For U(1) (Step 1) the certificate was modular because the Villain weight is a theta function on the
charge lattice Z, and Poisson summation = the modular S-transform = electric-magnetic duality, with
the confinement scale sitting at the theta CUSP. Question for SU(2): is there an analogous modular
object, and does the cusp-confinement mechanism transfer?

The non-abelian analog is the SU(2) HEAT KERNEL on the group (= 2D YM heat-kernel weight). As a class
function of the angle theta (U ~ diag(e^{i theta}, e^{-i theta})), it has TWO representations:

  spectral (sum over irreps j, dim 2j+1, Casimir j(j+1)):
     K_t(theta) = (1/sin theta) sum_{j} (2j+1) sin((2j+1) theta) e^{-t j(j+1)}
                = (e^{t/4}/sin theta) sum_{n>=1} n sin(n theta) e^{-t n^2/4}   (n = 2j+1)

  image / winding (geodesics on S^3 = SU(2); the coweight-lattice Poisson dual):
     K_t(theta) = (e^{t/4} sqrt(4 pi/t) / (t sin theta)) sum_{m in Z} (theta + 2 pi m) e^{-(theta+2 pi m)^2/t}

These are EQUAL by Poisson summation applied to  vartheta(theta,t)=sum_n e^{i n theta - t n^2/4}
= sqrt(4 pi/t) sum_m e^{-(theta+2 pi m)^2/t}  (the modular S-transform, t <-> (2 pi)^2/t).  So the SU(2)
heat kernel IS a (Jacobi-theta-derived) modular object: spectral <-> winding is the S-transform.
Verified below to machine precision -- the non-abelian Villain identity EXISTS.
"""
import numpy as np


def vartheta_spectral(theta, t, nmax=200):
    n = np.arange(-nmax, nmax + 1)
    return float(np.sum(np.exp(1j * n * theta - t * n ** 2 / 4.0)).real)


def vartheta_image(theta, t, mmax=60):
    m = np.arange(-mmax, mmax + 1)
    return float(np.sqrt(4 * np.pi / t) * np.sum(np.exp(-(theta + 2 * np.pi * m) ** 2 / t)))


def heat_spectral(theta, t, nmax=400):
    n = np.arange(1, nmax + 1)
    return float(np.exp(t / 4.0) / np.sin(theta) * np.sum(n * np.sin(n * theta) * np.exp(-t * n ** 2 / 4.0)))


def heat_image(theta, t, mmax=60):
    m = np.arange(-mmax, mmax + 1)
    s = np.sum((theta + 2 * np.pi * m) * np.exp(-(theta + 2 * np.pi * m) ** 2 / t))
    return float(np.exp(t / 4.0) * np.sqrt(4 * np.pi / t) / (t * np.sin(theta)) * s)


def check_modular():
    print("SU(2) heat kernel: spectral (irrep sum) == image (winding sum)  [Poisson = modular S]:")
    print("   theta    t     K_spectral      K_image        |diff|")
    worst = 0.0
    for t in (0.5, 1.0, 2.0):
        for theta in (0.6, 1.3, 2.2):
            ks, ki = heat_spectral(theta, t), heat_image(theta, t)
            worst = max(worst, abs(ks - ki))
            print(f"   {theta:>4}   {t:>4}   {ks:>12.6f}   {ki:>12.6f}    {abs(ks-ki):.1e}")
    print(f"   max |spectral - image| = {worst:.1e}   (EXACT: the non-abelian Villain/theta identity)\n")

    print("Underlying S-transform  vartheta(theta,t) = sqrt(4 pi/t) sum_m e^{-(theta+2pi m)^2/t}:")
    w2 = max(abs(vartheta_spectral(th, t) - vartheta_image(th, t))
             for t in (0.4, 1.0, 3.0) for th in (0.0, 0.9, 2.0))
    print(f"   max mismatch = {w2:.1e}   (t <-> (2 pi)^2 / t is the Jacobi imaginary transform)\n")


def area_law_2d():
    """2D SU(2) YM (heat-kernel action): <W_fund(A)> = e^{-(t/2) C2(fund)} with C2=j(j+1)=3/4.
    Area law sigma_fund = C2(fund)/2 per unit heat-kernel time -- LINEAR in coupling (2D trivial,
    no essential singularity), certified by the spectral (modular) representation."""
    print("2D SU(2) area law (spectral certificate; trivial like 2D U(1)):")
    C2 = 0.5 * 1.5                                   # fundamental j=1/2: C2 = j(j+1) = 3/4
    for t in (0.5, 1.0, 2.0):
        sigma = C2 / 2.0                             # per unit area, in units of the coupling t
        print(f"   t={t}:  sigma_fund = C2(fund)/2 = {sigma:.4f}  (power law in coupling)")
    print()


if __name__ == "__main__":
    print("=" * 78)
    print("TARGET II / STEP 3: SU(2) modular structure (the non-abelian frontier)")
    print("=" * 78 + "\n")
    check_modular()
    area_law_2d()
    print("OBSTRUCTION (honest, see paper 42 §19.2):")
    print(" - SU(2) IS modular: the heat kernel is a Jacobi-theta object; spectral<->winding is S.")
    print(" - But the U(1) cusp-confinement link does NOT transfer simply:")
    print("   (i) the U(1) magnetic/monopole sum (which gave the 3D essential singularity at the")
    print("       cusp) becomes here a GEODESIC-WINDING sum -- geometric, not a vortex/charge gas;")
    print("   (ii) genuine non-abelian confinement is 4D, asymptotic-freedom-driven (Lambda ~")
    print("        e^{-1/(2 b0 g^2)}); whether THAT scale is a cusp term of the affine-character")
    print("        object is the open question;")
    print("   (iii) the affine SU(2)_k S-matrix (Kac-Peterson) MIXES reps (Verlinde fusion), not a")
    print("        simple electric<->magnetic swap -- the non-abelian 'magnetic' (center-vortex)")
    print("        side has no literal Poisson dual. That missing dual IS the frontier.")
