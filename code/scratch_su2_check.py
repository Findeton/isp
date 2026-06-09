#!/usr/bin/env python3
"""Prototype: validate the SIMPLE-loop SU(2) lattice loop equation against exact 2D SU(2).

Exact 2D SU(2) (Wilson action, weight prod_p exp[(beta/2) tr U_p], tr U = 2cos(theta)):
  per-plaquette single-site average of winding-n holonomy
    c_n(beta) = <(1/2) tr V^n> = [I_n - (1/2)(I_{n+2}+I_{|n-2|})] / ((2/beta) I_1)
  simple loop:  <W(C)> = prod_p c_{|w_p|}(beta),  w_p = winding of C around plaquette p.

Claim to test (simple loop, ell0 in C):
  6 W(C) + beta * sum_{p contains ell0} s_p [ W(C+dp) - W(C-dp) ] = 0
"""
from scipy.special import iv
from loops import (plaq_boundary, plaquettes_with_link, chain_add,
                   fill_winding_2d, e, sub)

d = 2


def c_n(n, beta):
    n = abs(n)
    num = iv(n, beta) - 0.5 * (iv(n + 2, beta) + iv(abs(n - 2), beta))
    return float(num / ((2.0 / beta) * iv(1, beta)))


def exact_su2(chain, beta):
    if not chain:
        return 1.0
    w = fill_winding_2d(chain)
    val = 1.0
    for p, wp in w.items():
        val *= c_n(wp, beta)
    return val


def residual(C, link, beta):
    (x, mu) = link
    if C.get((x, mu), 0) != 1:        # emit only at FORWARD-traversed links (n=+1)
        return None
    r = 6.0 * exact_su2(C, beta)
    for (P, s) in plaquettes_with_link(x, mu, d):
        base, a, b = P
        dp = plaq_boundary(base, a, b, d)
        r += beta * s * (exact_su2(chain_add(C, dp, +1), beta)
                         - exact_su2(chain_add(C, dp, -1), beta))
    return r


def rect(w, h):
    """Simple w x h rectangular loop (winding +1), lower-left at origin."""
    C = {}
    for i in range(w):
        C = chain_add(C, plaq_boundary((i, 0), 0, 1, d), +1) if i == 0 and h == 1 else C
    # build by summing the w*h unit plaquettes (boundary = rectangle)
    C = {}
    for i in range(w):
        for j in range(h):
            C = chain_add(C, plaq_boundary((i, j), 0, 1, d), +1)
    return C


def Lshape():
    C = {}
    for (i, j) in [(0, 0), (1, 0), (0, 1)]:
        C = chain_add(C, plaq_boundary((i, j), 0, 1, d), +1)
    return C


if __name__ == "__main__":
    print("Validate SIMPLE-loop SU(2) equation: 6W(C)+beta*sum s[W(C+dp)-W(C-dp)] =? 0\n")
    tests = {"1x1": rect(1, 1), "1x2": rect(2, 1), "2x2": rect(2, 2),
             "1x3": rect(3, 1), "L-tromino": Lshape()}
    for beta in (0.5, 1.0, 2.0, 4.0):
        worst = 0.0; n = 0
        for name, C in tests.items():
            for link in list(C.keys()):
                r = residual(C, link, beta)
                if r is not None:
                    worst = max(worst, abs(r)); n += 1
        print(f"  beta={beta:>4}:  max |residual| over {n} (loop,fwd-link) pairs = {worst:.3e}")
    print("\n(If ~1e-12, the contact coeff 6=2(N^2-1) and deformation beta-coeff are CORRECT.)")
