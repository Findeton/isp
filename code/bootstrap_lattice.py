#!/usr/bin/env python3
"""
Lattice U(1) Wilson-loop bootstrap (paper 42, Target I): mm_equations wired into an SDP.

Variables: W(D) for cycles D (canonical, mod translation+reversal); W(empty)=1.
Constraints:
  - loop equations from mm_equations.abelian_loop_equation (linear in the W's);
  - positivity: for test cycles {C_i}, the Gram matrix M[i,j] = W(C_j - C_i) >= 0
    (abelian: <O_{C_i}^dag O_{C_j}> = W(C_j - C_i), real & symmetric since W(D)=W(-D)).
Truncation: keep cycles with L1 winding-size <= Lcap; include only loop equations / Gram
entries whose cycles all lie in the kept variable set. Objective: max/min a target loop.

Wiring is validated in 2D U(1) against the exact solution W = prod_p I_{w_p}/I_0.
"""
import numpy as np
import cvxpy as cp
from loops import (plaq_boundary, chain_add, canonical, sub, e,
                   plaquettes_with_link, exact_W_2d)
from mm_equations import abelian_loop_equation


def size(ch):
    return sum(abs(w) for w in ch.values())


def small_test_cycles(d, win=1):
    """Test cycles for the Gram block: empty + single plaquettes at all positions in a
    win-sized box in each coordinate plane (their pairwise differences are the Gram entries;
    a bigger window => bigger Gram => tighter bound)."""
    from itertools import combinations, product
    cs = [{}]
    for a, b in combinations(range(d), 2):
        for off2 in product(range(win + 1), repeat=2):
            x = [0] * d; x[a], x[b] = off2
            cs.append(plaq_boundary(tuple(x), a, b, d))
    # dedupe identical-position plaquettes
    uniq, seen = [], set()
    for c in cs:
        key = frozenset(c.items())
        if key not in seen:
            seen.add(key); uniq.append(c)
    return uniq


def build(d, Lcap, test_cycles, Vmax=900):
    """Build variable set V (canon->chain): test cycles + their differences, closed under
    plaquette deformations, capped by L1 size Lcap and total count Vmax."""
    V = {canonical({}, d): {}}
    def add(ch):
        if size(ch) <= Lcap and len(V) < Vmax:
            V.setdefault(canonical(ch, d), ch)
    for Ci in test_cycles:
        add(Ci)
        for Cj in test_cycles:
            add(chain_add(Ci, Cj, -1))           # Gram difference cycles
    for _ in range(3):                            # close under plaquette deformations (BFS)
        for ch in list(V.values()):
            if len(V) >= Vmax: break
            for (x, mu) in list(ch.keys()):
                for (P, s) in plaquettes_with_link(x, mu, d):
                    bb, a, b = P
                    dp = plaq_boundary(bb, a, b, d)
                    for sg in (+1, -1):
                        add(chain_add(ch, dp, sg))
    return V


def solve(d, beta, Lcap, test_cycles, target_chain, sense, solver="SCS"):
    V = build(d, Lcap, test_cycles)
    keys = list(V.keys())
    idx = {k: i for i, k in enumerate(keys)}
    x = cp.Variable(len(keys))
    cons = [x[idx[canonical({}, d)]] == 1]

    # loop equations (only those fully inside V)
    neq = 0
    for k, C in V.items():
        for link in list(C.keys()):
            eq = abelian_loop_equation(C, link, d)
            if all(kk in idx for kk in eq):
                expr = sum((a + b * beta) * x[idx[kk]] for kk, (a, b) in eq.items())
                cons.append(expr == 0); neq += 1

    # positivity Gram block (only if all difference-cycles are in V)
    tc = [c for c in test_cycles]
    diffs_ok = all(canonical(chain_add(Ci, Cj, -1), d) in idx for Ci in tc for Cj in tc)
    if diffs_ok:
        m = len(tc)
        M = cp.bmat([[x[idx[canonical(chain_add(Ci, Cj, -1), d)]] for Cj in tc] for Ci in tc])
        cons.append(M >> 0)

    tkey = canonical(target_chain, d)
    if tkey not in idx:
        raise ValueError("target not in variable set; raise Lcap")
    obj = cp.Maximize(x[idx[tkey]]) if sense == "max" else cp.Minimize(x[idx[tkey]])
    cp.Problem(obj, cons).solve(solver=solver)
    val = x[idx[tkey]].value
    return (None if val is None else float(val)), len(keys), neq


def bracket(d, beta, Lcap, target_chain, win=1):
    tc = small_test_cycles(d, win)
    lo, nv, ne = solve(d, beta, Lcap, tc, target_chain, "min")
    hi, _, _ = solve(d, beta, Lcap, tc, target_chain, "max")
    return lo, hi, nv, ne


if __name__ == "__main__":
    d = 2
    P = plaq_boundary((0, 0), 0, 1, d)            # 1x1 plaquette (target)
    print("Wiring validation: 2D U(1), bracket the plaquette W(1x1) vs exact I_1/I_0\n")
    from scipy.special import iv
    for win in (1, 2, 3):
        print(f"\n-- Gram window {win} (bigger window = bigger Gram = tighter) --")
        for beta in (0.7, 1.5, 3.0):
            lo, hi, nv, ne = bracket(d, beta, Lcap=16, target_chain=P, win=win)
            ex = float(iv(1, beta) / iv(0, beta))
            if lo is not None:
                ok = lo - 1e-4 <= ex <= hi + 1e-4
                print(f"  beta={beta}: W(1x1) in [{lo:.5f}, {hi:.5f}]  exact {ex:.5f}  "
                      f"width={hi-lo:.3f} contains={ok}  (vars={nv}, eqs={ne})")
            else:
                print(f"  beta={beta}: solver None (vars={nv}, eqs={ne})")
