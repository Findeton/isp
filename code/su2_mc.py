#!/usr/bin/env python3
"""
Minimal SU(2) lattice Monte Carlo (2D), the gold-standard validator for the loop-equation
generator (paper 42, M3) -- no analytic assumptions; validates contact + deformation + FF + FB
splits against the actual theory, and generalizes to 4D.

SU(2) as unit quaternions q=(q0,q1,q2,q3), U = q0 I + i(q.sigma); tr U = 2 q0, W = q0 of the
ordered product. Wilson action S = beta sum_p (1 - (1/2) tr U_p); weight exp(-S). Metropolis.
Quaternions are plain float tuples (scalar arithmetic) -- avoids numpy per-call overhead.
"""
import math
import random

random.seed(12345)


def qmul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
            a0 * b1 + b0 * a1 - (a2 * b3 - a3 * b2),
            a0 * b2 + b0 * a2 - (a3 * b1 - a1 * b3),
            a0 * b3 + b0 * a3 - (a1 * b2 - a2 * b1))


def qconj(a):
    return (a[0], -a[1], -a[2], -a[3])


def rand_su2(eps):
    x, y, z = random.gauss(0, 1), random.gauss(0, 1), random.gauss(0, 1)
    nrm = math.sqrt(x * x + y * y + z * z) or 1.0
    ang = eps * random.gauss(0, 1)
    s = math.sin(ang) / nrm
    return (math.cos(ang), s * x, s * y, s * z)


ID = (1.0, 0.0, 0.0, 0.0)


class Lattice2D:
    def __init__(self, L, beta):
        self.L, self.beta = L, beta
        self.U = {(x, y, mu): ID for x in range(L) for y in range(L) for mu in (0, 1)}

    def link(self, x, y, mu, dag=False):
        q = self.U[(x % self.L, y % self.L, mu)]
        return qconj(q) if dag else q

    def _plaq_tr(self, bx, by):
        p = qmul(self.link(bx, by, 0), self.link(bx + 1, by, 1))
        p = qmul(p, self.link(bx, by + 1, 0, True))
        p = qmul(p, self.link(bx, by, 1, True))
        return 2.0 * p[0]

    def sweep(self, eps):
        L, b = self.L, self.beta
        acc = 0
        for x in range(L):
            for y in range(L):
                for mu in (0, 1):
                    bases = [(x, y), ((x, y - 1) if mu == 0 else (x - 1, y))]
                    old = self.U[(x, y, mu)]
                    s_old = self._plaq_tr(*bases[0]) + self._plaq_tr(*bases[1])
                    self.U[(x, y, mu)] = qmul(rand_su2(eps), old)
                    s_new = self._plaq_tr(*bases[0]) + self._plaq_tr(*bases[1])
                    dS = -(b / 2.0) * (s_new - s_old)
                    if dS > 0 and random.random() >= math.exp(-dS):
                        self.U[(x, y, mu)] = old
                    else:
                        acc += 1
        return acc / (L * L * 2)

    def W(self, walk):
        q = ID
        for (site, mu, s) in walk:
            q = qmul(q, self.link(site[0], site[1], mu, dag=(s == -1)))
        return q[0]


def measure(L, beta, products, therm=1500, nmeas=12000, gap=3, eps=0.45):
    """products: list of tuples of walks; returns [<prod_k W(w)> for each], n_measurements.
    (Arity 1 = <W>, 2 = <W W>, 3 = <W W W>, ...)"""
    lat = Lattice2D(L, beta)
    for _ in range(therm):
        lat.sweep(eps)
    s = [0.0] * len(products)
    n = 0
    for it in range(nmeas):
        lat.sweep(eps)
        if it % gap:
            continue
        n += 1
        for i, prod in enumerate(products):
            v = 1.0
            for w in prod:
                v *= lat.W(w)
            s[i] += v
    return [si / n for si in s], n
