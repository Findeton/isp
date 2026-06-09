#!/usr/bin/env python3
"""
Paper 44 §9 -- the theta-angle / Jacobi-form completion of Steps A-D (autonomous extension).

The affine A_1^(1) (level-1) theta is naturally a function of TWO variables: tau (coupling/holonomy)
AND z (an elliptic variable). Physically z is the theta-angle: turning on theta makes the monopoles into
dyons (Witten effect), and the dual-Coulomb gas becomes a function of (tau, z). The affine theta vector
(Theta_{0,1}, Theta_{1,1}),  Theta_{l,1}(tau,z) = sum_{n in Z + l/2} q^{n^2} y^{n}  (q=e^{2pi i tau}, y=e^{2pi i z}),
is a JACOBI FORM: modular in tau, elliptic in z. We VERIFY its three transformation laws numerically
(all standard Kac-Peterson identities, machine precision), and read off the physics:

  - modular S (tau -> -1/tau):  S-matrix = Kac-Peterson (1/sqrt2)[[1,1],[1,-1]]  = the e<->m duality (Step D).
  - spectral flow (z -> z+tau): PERMUTES l=0 <-> l=1, i.e. shifts the center/flux sector
        => the theta-angle branch jump (multi-branch vacuum energy E(theta)).
  - quasi-periodicity (z -> z+1): Theta_{l,1} -> e^{pi i l} Theta_{l,1}.

So the SU(2)-on-R^3xS^1 confinement data organizes as ONE affine Jacobi form: the coupling direction
carries the electric-magnetic duality, the theta direction carries the multi-branch structure via
spectral flow. [Math: standard affine characters. Physics: established deformed-YM theta-dependence.
The explicit Jacobi-form organization of our affine-theta program is the (modest) lens; novelty limited.]
"""
import cmath


def Theta(l, tau, z, N=80):
    """Theta_{l,1}(tau,z) = sum_{n in Z + l/2} e^{2 pi i tau n^2} e^{2 pi i z n}."""
    s = 0j
    for k in range(-N, N + 1):
        n = k + l / 2.0
        s += cmath.exp(2j * cmath.pi * tau * n * n + 2j * cmath.pi * z * n)
    return s


def check(name, lhs, rhs, worst):
    d = abs(lhs - rhs)
    return max(worst, d), f"  {name}: |lhs-rhs| = {d:.2e}"


if __name__ == "__main__":
    print("=" * 76)
    print("Paper 44 §9: the affine theta is a JACOBI FORM (tau = coupling, z = theta-angle)")
    print("=" * 76 + "\n")
    taus = [0.5j, 0.3 + 0.7j, 1.2j]
    zs = [0.0, 0.2, 0.15 + 0.1j]

    # (1) quasi-periodicity z -> z+1 : Theta_{l,1}(tau,z+1) = e^{pi i l} Theta_{l,1}(tau,z)
    print("(1) elliptic z -> z+1 :  Theta_{l,1}(tau,z+1) = e^{i pi l} Theta_{l,1}(tau,z)")
    w = 0.0
    for tau in taus:
        for z in zs:
            for l in (0, 1):
                w, msg = check(f"l={l},tau={tau},z={z}", Theta(l, tau, z + 1),
                               cmath.exp(1j * cmath.pi * l) * Theta(l, tau, z), w)
    print(f"    max deviation = {w:.1e}   (l=0: periodic; l=1: anti-periodic)\n")

    # (2) spectral flow z -> z+tau : Theta_{l,1}(tau,z+tau) = q^{-1/4} e^{-i pi z} Theta_{1-l,1}(tau,z)
    print("(2) spectral flow z -> z+tau :  Theta_{l,1}(tau,z+tau) = q^{-1/4} e^{-i pi z} Theta_{1-l,1}(tau,z)")
    print("    (PERMUTES l=0 <-> l=1 = the center/flux sector = the theta-angle BRANCH JUMP)")
    w = 0.0
    for tau in taus:
        q = cmath.exp(2j * cmath.pi * tau)
        for z in zs:
            for l in (0, 1):
                lhs = Theta(l, tau, z + tau)
                rhs = q ** (-0.25) * cmath.exp(-1j * cmath.pi * z) * Theta(1 - l, tau, z)
                w, _ = check("", lhs, rhs, w)
    print(f"    max deviation = {w:.1e}   (z=theta carries the multi-branch structure)\n")

    # (3) modular S tau->-1/tau, z->z/tau (Jacobi form). Derived via Poisson:
    #     Theta_{l,1}(-1/tau, z/tau) = sqrt(tau/2i) e^{i pi z^2/(2 tau)} [Theta_{0,1}+Theta_{1,1}](tau, l - z).
    #     At z=0 this reduces to the Kac-Peterson S-matrix (Step D) = the electric<->magnetic duality.
    print("(3) modular S (tau->-1/tau, z->z/tau), full Jacobi form:")
    print("    Theta_{l,1}(-1/tau,z/tau) = sqrt(tau/2i) e^{i pi z^2/(2tau)} [Theta_0+Theta_1](tau, l-z)")
    w = 0.0
    for tau in taus:
        for z in zs:
            pref = cmath.sqrt(tau / (2j)) * cmath.exp(1j * cmath.pi * z * z / (2 * tau))
            for l in (0, 1):
                lhs = Theta(l, -1 / tau, z / tau)
                rhs = pref * (Theta(0, tau, l - z) + Theta(1, tau, l - z))
                w, _ = check("", lhs, rhs, w)
    print(f"    max deviation = {w:.1e}   (full Jacobi modular transformation)")
    # and the z=0 reduction to the Kac-Peterson S-matrix (the e<->m duality, Step D):
    w0 = 0.0
    for tau in taus:
        pref = cmath.sqrt(tau / (2j))
        for l in (0, 1):
            lhs = Theta(l, -1 / tau, 0.0)
            rhs = pref * (1 / cmath.sqrt(2)) * sum((-1) ** (l * lp) * Theta(lp, tau, 0.0) for lp in (0, 1)) * cmath.sqrt(2)
            w0, _ = check("", lhs, rhs, w0)
    print(f"    z=0 reduction to KP S-matrix (1/sqrt2)[[1,1],[1,-1]]: dev = {w0:.1e}  (= e<->m duality)\n")

    print("CONCLUSION: the SU(2)-on-R^3xS^1 confinement data is ONE affine level-1 Jacobi form.")
    print("  tau (coupling) direction  -> modular S = electric-magnetic duality (Steps A-D).")
    print("  z (theta-angle) direction -> spectral flow = the multi-branch vacuum-energy structure.")
    print("  Unifies the e-m duality and the theta-dependence in a single modular object, in the")
    print("  calculable regime. [Standard affine-character math; established deformed-YM physics.]")
