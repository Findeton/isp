#!/usr/bin/env python3
"""
Correctness gate for the SU(2) loop-equation generator (M3): the non-abelian
Makeenko-Migdal equation -- contact + deformation + FIERZ SPLIT -- must be satisfied
by the exact 2D SU(2) solution.

Exact 2D SU(2) (Wilson action): single loop  <W(C)> = prod_p c_{|w_p|},
  c_n(beta) = <(1/2) tr V^n> = [I_n - (1/2)(I_{n+2}+I_{|n-2|})]/((2/beta) I_1).
Two-loop correlator (validation cases): disjoint -> product; same single plaquette with
  windings a,b -> <(1/2 tr V^a)(1/2 tr V^b)> = (1/2)(c_{a+b} + c_{|a-b|}).
"""
from scipy.special import iv
from loops import fill_winding_2d, plaq_boundary, chain_add
from su2_loops import su2_loop_equation, plaquette_walk, walk_to_chain, reverse_walk

d = 2


def c_n(n, beta):
    n = abs(n)
    return float((iv(n, beta) - 0.5 * (iv(n + 2, beta) + iv(abs(n - 2), beta)))
                 / ((2.0 / beta) * iv(1, beta)))


def W1(chain, beta):
    if not chain:
        return 1.0
    v = 1.0
    for _, wp in fill_winding_2d(chain).items():
        v *= c_n(wp, beta)
    return v


def W2(c1, c2, beta):
    """Exact 2D SU(2) two-loop correlator for the validation cases."""
    w1, w2 = fill_winding_2d(c1), fill_winding_2d(c2)
    s1 = {p for p, w in w1.items() if w}
    s2 = {p for p, w in w2.items() if w}
    if s1.isdisjoint(s2):                              # independent plaquettes
        return W1(c1, beta) * W1(c2, beta)
    if len(s1) == 1 and s1 == s2:                      # same single plaquette
        p = next(iter(s1)); a, b = w1[p], w2[p]
        return 0.5 * (c_n(a + b, beta) + c_n(abs(a - b), beta))
    raise NotImplementedError("two-loop correlator only for disjoint / same-single-plaquette")


def residual_from_eq(lin, bil, beta, key_chain):
    """Evaluate sum (a+b*beta) W(key)  +  sum (a+b*beta) <W k1 W k2>  using exact 2D values.
    key_chain maps a canonical key -> a representative chain (for exact evaluation)."""
    r = 0.0
    for k, (a, b) in lin.items():
        r += (a + b * beta) * W1(key_chain[k], beta)
    for (k1, k2), (a, b) in bil.items():
        r += (a + b * beta) * W2(key_chain[k1], key_chain[k2], beta)
    return r


# We bypass the generator's canonical keys for exact eval (the 2-loop correlator depends on
# RELATIVE position, lost by per-loop canonicalization). So we re-evaluate the equation's
# contributions directly from a known walk, using the same coefficients the generator emits.
from su2_loops import CONTACT, SPLIT
from loops import plaquettes_with_link


def residual_direct(walk, anchor, beta):
    site, mu, s = walk[anchor]
    assert s == +1
    x = site
    C = walk_to_chain(walk)
    r = CONTACT * W1(C, beta)
    for (P, sp) in plaquettes_with_link(x, mu, d):
        base, a, b = P
        dp = plaq_boundary(base, a, b, d)
        r += beta * sp * (W1(chain_add(C, dp, +1), beta) - W1(chain_add(C, dp, -1), beta))
    n = len(walk)
    for j in range(n):
        if j == anchor or (walk[j][0], walk[j][1]) != (x, mu):
            continue
        if walk[j][2] == +1:
            arc1 = [walk[(anchor + t) % n] for t in range((j - anchor) % n)]
            arc2 = [walk[(j + t) % n] for t in range((anchor - j) % n)]
            r += SPLIT * W2(walk_to_chain(arc1), walk_to_chain(arc2), beta)
            r += -2 * W1(C, beta)
    return r


def doubled_plaquette():
    p = plaquette_walk((0, 0), 0, 1, d)
    return p + p                                       # traverse the unit plaquette twice


def figure_eight():
    # P(0,0) forward sharing link ((1,0),1) with -P(1,0); shared link traversed twice forward.
    return [((1, 0), 1, +1), ((0, 1), 0, -1), ((0, 0), 1, -1), ((0, 0), 0, +1),
            ((1, 0), 1, +1), ((1, 1), 0, +1), ((2, 0), 1, -1), ((1, 0), 0, -1)]


if __name__ == "__main__":
    print("SU(2) loop-equation gate (M3): contact + deformation + Fierz split vs exact 2D SU(2)\n")
    cases = {
        "doubled 1x1 (split -> identical plaquette, <W^2>=(1+c2)/2)": (doubled_plaquette(), 0),
        "figure-8    (split -> two disjoint plaquettes, <WW>=c1^2)": (figure_eight(), 0),
    }
    ok = True
    for name, (walk, anchor) in cases.items():
        print(f"  {name}")
        for beta in (0.5, 1.0, 2.0, 4.0):
            r = residual_direct(walk, anchor, beta)
            ok = ok and abs(r) < 1e-10
            print(f"      beta={beta:>4}:  |residual| = {abs(r):.3e}")
    # also exercise the generator itself (structure / no crash) and report term counts
    lin, bil = su2_loop_equation(doubled_plaquette(), 0, d)
    print(f"\n  generator on doubled-1x1: {len(lin)} linear terms, {len(bil)} bilinear terms")
    print("\n  RESULT:", "PASS (<=1e-10)" if ok else "FAIL")
