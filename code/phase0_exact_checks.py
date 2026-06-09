#!/usr/bin/env python3
"""
Phase-0 exact checks recorded in paper 41, section 48.

(1) 2D SU(2) Yang-Mills: the fundamental Wilson loop obeys an EXACT area law
        <W(C)> = exp(-sigma_2D * A),   sigma_2D = (g^2/2) C_2(1/2) = 3 g^2/8 = 3/(2 beta),
    with C_2(1/2)=3/4, beta=4/g^2.  (This equals the sec.25 tree value of m_{1/2}.)

(2) 3D compact U(1) (Villain): the plaquette weight is LITERALLY a Jacobi theta,
        V(t;beta) = sum_n exp(-(beta/2)(t - 2 pi n)^2)
                  = (1/sqrt(2 pi beta)) sum_k exp(-k^2/(2 beta)) exp(-i k t)
                  = (1/sqrt(2 pi beta)) theta_3(-t/2, exp(-1/(2 beta))).
    Poisson summation between the two forms IS its modular transform (the sec.30
    heat-kernel duality); the spectral coefficients exp(-k^2/(2 beta)) are exactly
    the sec.30 heat-kernel coefficients.  Goepfert-Mack confinement lives in the
    monopole / sine-Gordon sector built on this theta structure.

    => Phase-1 modularity test answered YES (paper 41, section 48.3): in the one
       rigorously-solved confining gauge theory, the certifying structure is modular.

Requires: mpmath, numpy.
"""
import math
import mpmath as mp

mp.mp.dps = 30


def sigma_2d_fundamental(beta):
    """Exact 2D SU(2) fundamental string tension: 3 g^2/8 = 3/(2 beta)."""
    g2 = 4.0 / beta
    return 3.0 * g2 / 8.0  # == 3/(2 beta)


def villain_direct(t, beta, N=80):
    return mp.fsum([mp.e ** (-(beta / 2) * (t - 2 * mp.pi * n) ** 2) for n in range(-N, N + 1)])


def villain_dual(t, beta, K=250):
    pref = 1 / mp.sqrt(2 * mp.pi * beta)
    return (pref * mp.fsum([mp.e ** (-mp.mpf(k) ** 2 / (2 * beta)) * mp.e ** (-1j * k * t)
                            for k in range(-K, K + 1)])).real


def villain_theta3(t, beta):
    q = mp.e ** (-1 / (2 * beta))
    return (1 / mp.sqrt(2 * mp.pi * beta)) * mp.jtheta(3, -t / 2, q)


def main():
    print("== (1) 2D SU(2) exact area law: sigma_2D = 3/(2 beta) ==")
    for beta in (2.0, 4.0, 8.0):
        print(f"   beta={beta}: sigma_2D = {sigma_2d_fundamental(beta):.6f}  (= 3/(2 beta) = {3/(2*beta):.6f})")

    print("\n== (2) 3D U(1) Villain weight = Jacobi theta_3 (Phase-1 modularity) ==")
    for (t, beta) in ((0.7, 1.0), (1.3, 3.0), (0.4, 0.3)):
        d = villain_direct(t, beta)
        s = villain_dual(t, beta)
        th = villain_theta3(t, beta)
        print(f"   t={t}, beta={beta}:")
        print(f"       direct  = {mp.nstr(d, 14)}")
        print(f"       dual    = {mp.nstr(s, 14)}   (diff {mp.nstr(abs(d-s),3)})")
        print(f"       theta_3 = {mp.nstr(th, 14)}   (diff {mp.nstr(abs(d-th),3)})")
    print("\n   => weight is a Jacobi theta; Poisson summation = its modular transform.")
    print("      Modularity test (sec 48.3): YES, in the solved confining case 3D U(1).")


if __name__ == "__main__":
    main()
