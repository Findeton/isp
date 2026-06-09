#!/usr/bin/env python3
"""
TARGET II -- testing the conjecture (paper 42, §19.4): measure the 't Hooft Z_2 flux free energy on
the lattice. The §19.3 conjecture is that the SU(2) string tension / electric-flux free energy is the
cusp datum of the flux theta. The 't Hooft flux free energy is the genuine observable behind it.

Method (robust; no reweighting overlap problem): THERMODYNAMIC INTEGRATION. A 't Hooft twist in the
(0,1) plane flips the action sign on a coclosed sheet of (0,1)-plaquettes (here: those at x_k=0 for
k>=2). Interpolate the sheet coupling beta -> beta(1-2 lambda), lambda: 0 (untwisted) -> 1 (twisted):
    F_twist(beta) = -log(Z_tw/Z_0) = integral_0^1  beta <sum_{sheet} tr U_p>_lambda  d lambda.

HONEST SCOPE: this is a small-lattice, pure-Python PROOF-OF-CONCEPT. It demonstrates the observable
and the method and gives confined-regime data, but it does NOT test the CONTINUUM Lambda-cusp content
of the conjecture (that needs large 4D lattices, weak coupling, and continuum scaling -- a real
lattice campaign). SU(2) links are unit quaternions (see su2_mc); Wilson action S=beta sum_p(1-1/2 tr).
"""
import itertools
import math
import random

from su2_mc import qmul, qconj, rand_su2, ID

random.seed(2024)


class LatticeD:
    def __init__(self, L, d, beta):
        self.L, self.d, self.beta = L, d, beta
        self.U = {}
        for x in itertools.product(range(L), repeat=d):
            for mu in range(d):
                self.U[(x, mu)] = ID
        # twist sheet: (0,1)-plaquettes with all other coords = 0
        self.sheet = set()
        for x in itertools.product(range(L), repeat=d):
            if all(x[k] == 0 for k in range(2, d)):
                self.sheet.add((x, 0, 1))

    def shift(self, x, mu, s=+1):
        y = list(x); y[mu] = (y[mu] + s) % self.L; return tuple(y)

    def link(self, x, mu, dag=False):
        q = self.U[(x, mu)]
        return qconj(q) if dag else q

    def plaq_tr(self, x, mu, nu):
        xmu, xnu = self.shift(x, mu), self.shift(x, nu)
        p = qmul(self.link(x, mu), self.link(xmu, nu))
        p = qmul(p, self.link(xnu, mu, True))
        p = qmul(p, self.link(x, nu, True))
        return 2.0 * p[0]

    def plaqs_of_link(self, x, mu):
        """All plaquettes (base, a, b) containing link (x,mu), with a<b."""
        out = []
        for nu in range(self.d):
            if nu == mu:
                continue
            a, b = (mu, nu) if mu < nu else (nu, mu)
            out.append((x, a, b))                                 # forward
            out.append((self.shift(x, nu, -1), a, b))             # backward (base shifted)
        return out

    def coupling(self, base, a, b, lam):
        """beta, but beta(1-2 lambda) on the twist sheet."""
        if (base, a, b) in self.sheet:
            return self.beta * (1.0 - 2.0 * lam)
        return self.beta

    def sweep(self, lam, eps):
        acc = 0
        for key in list(self.U.keys()):
            x, mu = key
            pls = self.plaqs_of_link(x, mu)
            old = self.U[key]
            s_old = sum(self.coupling(b, a1, a2, lam) * 0.5 * self.plaq_tr(b, a1, a2) for (b, a1, a2) in pls)
            self.U[key] = qmul(rand_su2(eps), old)
            s_new = sum(self.coupling(b, a1, a2, lam) * 0.5 * self.plaq_tr(b, a1, a2) for (b, a1, a2) in pls)
            dS = -(s_new - s_old)                                 # S = -coupling*1/2 tr ; weight e^{-S}
            if dS > 0 and random.random() >= math.exp(-dS):
                self.U[key] = old
            else:
                acc += 1
        return acc / len(self.U)

    def mean_plaq(self):
        s, n = 0.0, 0
        for x in itertools.product(range(self.L), repeat=self.d):
            for a in range(self.d):
                for b in range(a + 1, self.d):
                    s += 0.5 * self.plaq_tr(x, a, b); n += 1
        return s / n

    def sheet_sumtr(self):
        return sum(self.plaq_tr(b, a1, a2) for (b, a1, a2) in self.sheet)


def measure_at_lambda(L, d, beta, lam, therm, nmeas, gap, eps=0.4):
    lat = LatticeD(L, d, beta)
    for _ in range(therm):
        lat.sweep(lam, eps)
    s, n = 0.0, 0
    for it in range(nmeas):
        lat.sweep(lam, eps)
        if it % gap == 0:
            s += lat.sheet_sumtr(); n += 1
    return s / n


def twist_free_energy(L, d, beta, lambdas, therm=600, nmeas=2400, gap=2):
    """F = integral_0^1 beta <sum_sheet tr U_p>_lambda d lambda  (Simpson over lambdas)."""
    vals = [beta * measure_at_lambda(L, d, beta, lam, therm, nmeas, gap) for lam in lambdas]
    # composite Simpson (lambdas uniform, odd count)
    h = lambdas[1] - lambdas[0]
    F = vals[0] + vals[-1] + 4 * sum(vals[1:-1:2]) + 2 * sum(vals[2:-2:2])
    return F * h / 3.0, vals


def validate_plaquette(L, d):
    print(f"  MC validation ({d}D, L={L}): <1/2 tr U_p> vs strong-coupling leading beta/4")
    for beta in (0.4, 0.8, 1.6):
        lat = LatticeD(L, d, beta)
        for _ in range(400):
            lat.sweep(0.0, 0.4)
        m = 0.0; n = 0
        for it in range(1500):
            lat.sweep(0.0, 0.4)
            if it % 2 == 0:
                m += lat.mean_plaq(); n += 1
        print(f"    beta={beta}:  <1/2 tr U_p> = {m/n:.4f}   (strong-coupling beta/4 = {beta/4:.4f})")


if __name__ == "__main__":
    import sys
    d = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    L = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    print("=" * 74)
    print(f"TARGET II / §19.4: 't Hooft Z_2 flux free energy, {d}D SU(2), L={L} (proof-of-concept)")
    print("=" * 74)
    validate_plaquette(L, d)
    print(f"\n  't Hooft magnetic-twist free energy F(beta) via thermodynamic integration")
    print(f"  (sheet = {{(0,1)-plaquettes at x_k=0, k>=2}}); confined regime -> F small/bounded:")
    lambdas = [0.0, 0.25, 0.5, 0.75, 1.0]
    print("    beta   F_m (magnetic twist)   F_e=-log tanh(F_m/2) (electric flux)   signal")
    for beta in (1.0, 1.6, 2.2):
        Fm, vals = twist_free_energy(L, d, beta, lambdas)
        Fm = abs(Fm)                                          # free energy magnitude
        Fe = -math.log(math.tanh(Fm / 2.0)) if Fm > 1e-9 else float("inf")
        sig = "confined (F_m small, F_e large)" if Fe > Fm else "ordered"
        print(f"    {beta:>4}      {Fm:.4f}                 {Fe:.4f}                       {sig}")
    print("\n  't Hooft duality: confined <=> magnetic-flux free energy F_m small, electric-flux F_e")
    print("  large (F_e ~ sigma * area).  HONEST: small-lattice proof-of-concept of the observable +")
    print("  method + confinement signal; NOT a continuum Lambda-cusp test (needs large 4D lattices,")
    print("  weak coupling, continuum scaling). The §19.3 conjecture remains OPEN, not proved.")
