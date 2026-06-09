#!/usr/bin/env python3
"""
Makeenko-Migdal / Schwinger-Dyson loop-equation generator (paper 42, Target I, module 2).

ABELIAN U(1) case (built first: no Fierz splitting, validatable against exact 2D).
Wilson action S = -beta sum_p cos(theta_p). For a charge-1 loop observable O = exp(i sum_l n_l theta_l),
the identity <dO/dtheta_l0> = <O dS/dtheta_l0> gives the exact lattice loop equation

    2 n_{l0} W(C)  +  beta sum_{p contains l0} s_{p,l0} [ W(C + dp) - W(C - dp) ]  =  0 ,

linear in Wilson loops, relating C to its plaquette-deformations C +/- dp.
(s_{p,l0} = orientation of link l0 in the plaquette boundary dp.)

The non-abelian SU(N) case adds, at self-intersections of C, Fierz splitting terms
W(C1)W(C2) - (1/N) W(C); that extension is documented in paper 42 sec.3 and is the
next step once the abelian engine is validated here.

Equation format: a dict { canonical_cycle_key : (a, b) }, coefficient = a + b*beta;
the equation is  sum_key (a + b*beta) * W(key) = 0.   The empty cycle key = identity, W=1.
"""
from loops import plaq_boundary, plaquettes_with_link, chain_add, canonical_full as canonical


def abelian_loop_equation(C, link, d):
    """U(1) Schwinger-Dyson equation at (cycle C, link=(x,mu)). Returns {cycle_key:(a,b)}."""
    (x, mu) = link
    eq = {}

    def acc(chain, a, b):
        k = canonical(chain, d)
        ca, cb = eq.get(k, (0, 0))
        eq[k] = (ca + a, cb + b)

    n0 = C.get((x, mu), 0)
    if n0 != 0:
        acc(C, 2 * n0, 0)                       # 2 n_{l0} W(C)
    for (P, s) in plaquettes_with_link(x, mu, d):
        base, a, b = P
        dp = plaq_boundary(base, a, b, d)
        acc(chain_add(C, dp, +1), 0, +s)        # +beta s W(C + dp)
        acc(chain_add(C, dp, -1), 0, -s)        # -beta s W(C - dp)

    return {k: (a, b) for k, (a, b) in eq.items() if not (a == 0 and b == 0)}


def loops_up_to(Lmax, d):
    """Enumerate canonical cycles built from up to Lmax unit plaquettes (BFS over plaquette adds)."""
    from loops import plaq_boundary
    seed = plaq_boundary((0,) * d, 0, 1, d)
    seen = {canonical(seed, d): seed}
    frontier = [seed]
    # generate by adding/removing adjacent plaquettes around occupied links
    plaqs = []
    R = range(-Lmax - 1, Lmax + 2)
    from itertools import product, combinations
    for x in product(R, repeat=d):
        for a, b in combinations(range(d), 2):
            plaqs.append((x, a, b))
    for _ in range(Lmax):
        new = []
        for C in frontier:
            for (x, a, b) in plaqs:
                dp = plaq_boundary(x, a, b, d)
                if not any(k in C for k in dp):
                    continue                      # only adjacent plaquettes
                for sgn in (+1, -1):
                    Cn = chain_add(C, dp, sgn)
                    if not Cn:
                        continue
                    k = canonical(Cn, d)
                    if k not in seen:
                        seen[k] = Cn; new.append(Cn)
        frontier = new
    return seen  # {canonical_key: representative_chain}
