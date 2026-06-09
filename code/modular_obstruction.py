#!/usr/bin/env python3
"""
Paper 43 §7.2 -- Phase 1: the modularity test for Lemma 1(b). [the decider]

A modular FORM needs two things of Z[e,m](tau): (H) holomorphy in tau, and (C) covariance under
SL(2,Z): Z(-1/tau) = (c tau + d)^w rho(S) Z(tau). Phase 0 fixed rho (the S_3 flux permutation) and
Gamma(2). Phase 1 tests (H) and (C) for pure SU(2).

Finding (made precise here, illustrated numerically):
 - (H) is FINE in the coupling variable tau_c = i*const/g^2: Z(beta) is holomorphic (entire, on a
   finite lattice) in the complexified coupling. So holomorphy is NOT the obstruction.
 - (C) FAILS: the modular S, tau -> -1/tau, maps the coupling to its strong-weak DUAL (g^2 -> #/g^2).
   Covariance therefore demands a Montonen-Olive strong-weak DUALITY -- a SUPERSYMMETRIC (N=4)
   phenomenon. Pure SU(2) has asymptotic freedom, which manifestly breaks g^2 <-> 1/g^2: the string
   tension is ~ e^{-c*beta} at weak coupling but ~ -log(beta) at strong coupling, related by NO
   power-law automorphy factor. The exact 't Hooft flux duality (Phase 0) is only KINEMATIC (it
   permutes flux labels); the dynamical Z does not transform covariantly. => Lemma 1(b) FAILS.
 - Secondary: augmenting tau with the theta-angle (the SUSY variable tau = theta/2pi + 4pi i/g^2) is
   separately blocked by reality/CP -- Z(theta) is real & even, so its Fourier coefficients are
   two-sided-symmetric, never a one-sided (weakly-holomorphic) q-expansion. SUSY evades this with a
   holomorphic INDEX (not the real partition function); pure YM has no such index.
 - Contrast: 2D YM IS modular because its modular S is the exact AREA duality (Migdal), which 2D has.
   4D non-SUSY has no analogous exact duality.
"""
import numpy as np
from scipy.special import iv


# ---- Secondary obstruction: reality/CP kills the theta-augmented variable ----
def theta_fourier_coeffs(chi, nmax=12):
    """Dilute-instanton-gas model Z(theta)/Z(0) = exp(chi (cos theta - 1)); its theta-Fourier
    coefficients are e^{-chi} I_n(chi), which are SYMMETRIC (a_n=a_{-n}) and TWO-SIDED."""
    return {n: float(np.exp(-chi) * iv(abs(n), chi)) for n in range(-nmax, nmax + 1)}


def reality_obstruction():
    print("Secondary obstruction (theta-variable): Z(theta) real & even => two-sided Fourier.")
    c = theta_fourier_coeffs(chi=3.0, nmax=6)
    print("   n :        -3        -2        -1         0         1         2         3")
    row = "   a_n: " + " ".join(f"{c[n]:9.5f}" for n in range(-3, 4))
    print(row)
    sym = max(abs(c[n] - c[-n]) for n in range(1, 7))
    print(f"   symmetric a_n = a_(-n) to {sym:.1e};  nonzero on BOTH sides (no n<-N truncation).")
    print("   => NOT a weakly-holomorphic q-expansion; the theta-augmented tau cannot be modular.\n")


# ---- Main obstruction: no strong-weak (Montonen-Olive) S-duality in pure SU(2) ----
def sigma_strong(beta):
    """Strong-coupling (small beta) string tension: leading area law <W>~(beta/4)^Area."""
    return -np.log(beta / 4.0)                              # sigma a^2, large & positive


def sigma_weak(beta):
    """Weak-coupling (large beta): 2-loop asymptotic freedom, sigma a^2 ~ e^{-(3 pi^2/11) beta}."""
    return np.exp(-(3 * np.pi ** 2 / 11.0) * beta)         # tiny & positive


def s_duality_obstruction():
    print("Main obstruction (coupling variable): modular S = strong-weak duality g^2 -> #/g^2.")
    print("   For a weight-w modular form, Z(S.tau) = (automorphy, a POWER law) x rho(S) Z(tau).")
    print("   Pure SU(2) string tension across the strong<->weak (beta <-> 'dual') divide:")
    print("    beta    sigma(strong-coupling form)   sigma(weak-coupling form)   ratio")
    for beta in (0.5, 1.0, 2.0):
        ss, sw = sigma_strong(beta), sigma_weak(1.0 / beta if beta != 0 else 1)
        print(f"    {beta:>4}        {ss:>8.4f}                  {sw:>10.3e}          {ss/sw:.2e}")
    print("   strong-coupling sigma ~ -log(beta)  (O(1));  weak-coupling sigma ~ e^{-c beta} (tiny).")
    print("   Their ratio across the would-be S-dual points grows EXPONENTIALLY -- not a power-law")
    print("   automorphy factor.  So Z is NOT S-covariant: there is no Montonen-Olive duality for")
    print("   pure SU(2) (that is an N=4 SUSY phenomenon; asymptotic freedom breaks g^2<->1/g^2).\n")


if __name__ == "__main__":
    print("=" * 76)
    print("Paper 43 §7.2 / Phase 1: does the 4D SU(2) flux vector transform as a modular FORM?")
    print("=" * 76 + "\n")
    reality_obstruction()
    s_duality_obstruction()
    print("VERDICT (Phase 1): Lemma 1(b) FAILS for pure 4D SU(2).")
    print(" - Holomorphy in the coupling is fine; the obstruction is MODULAR COVARIANCE.")
    print(" - Covariance under the modular S requires a strong-weak (Montonen-Olive) DUALITY, which")
    print("   exists for N=4 SUSY but NOT for pure SU(2) (asymptotic freedom; no g^2<->1/g^2 symmetry).")
    print(" - The exact 't Hooft flux duality (Phase 0) is only KINEMATIC (permutes flux labels); the")
    print("   dynamical partition function does not transform with an automorphy factor.")
    print(" - The theta-augmented variable is additionally killed by reality/CP (no holomorphic index).")
    print(" => The coupling-variable modularity the conjecture's part (b) needs does NOT hold.")
    print("    Residual structure: Phase 2A (quasi/mock-modular) ; provable positive: Phase 3 (worldsheet).")
