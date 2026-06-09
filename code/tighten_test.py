#!/usr/bin/env python3
"""
Frontend tightening diagnostic (paper 42): does a coherent, point-group-reduced
variable set + a RICHER Gram (charge-powers + spatial loops) tighten the U(1)
bootstrap bracket on W(1x1) below the trivial |W|<=1 -- in 2D at strong coupling,
toward the exact I_1/I_0 ?

Uses point-group canonicalization (loops.canonical_full) so a coherent (uncapped)
loop set is affordable, and a Gram whose operators include charge powers k*P
(=> the single-plaquette moment structure that pins per-plaquette physics) AND
small spatial loops (=> the area-law structure).
"""
import numpy as np
import cvxpy as cp
from itertools import product
from scipy.special import iv
from loops import (plaq_boundary, chain_add, canonical_full as canon,
                   plaquettes_with_link, e, sub)
from mm_equations import abelian_loop_equation

d = 2


def size(ch): return sum(abs(w) for w in ch.values())


def scale_chain(ch, k):                       # charge-k version (winding * k)
    return {kk: k * w for kk, w in ch.items()}


def operator_blocks(Kcharge=4, spw=2):
    """Two Gram blocks, each with small pairwise differences:
       (1) charge-power block {0,P,...,KP};
       (2) spatial block: empty + single plaquettes at positions in a spw x spw box + a 1x2."""
    from itertools import product as iprod
    P = plaq_boundary((0, 0), 0, 1, d)
    charge = [{}] + [scale_chain(P, k) for k in range(1, Kcharge + 1)]
    spatial = [{}]
    for off in iprod(range(spw + 1), repeat=2):
        spatial.append(plaq_boundary(off, 0, 1, d))
    spatial.append(chain_add(P, plaq_boundary((1, 0), 0, 1, d)))   # 1x2
    return [charge, spatial]


def build_variables(ops, Lcap, Vmax=1500):
    V = {canon({}, d): {}}
    def add(ch):
        if size(ch) <= Lcap and len(V) < Vmax:
            V.setdefault(canon(ch, d), ch)
    for Ci in ops:
        add(Ci)
        for Cj in ops:
            add(chain_add(Ci, Cj, -1))                       # Gram difference cycles
    for _ in range(3):                                       # close under deformations
        for ch in list(V.values()):
            if len(V) >= Vmax: break
            for (x, mu) in list(ch.keys()):
                for (P, s) in plaquettes_with_link(x, mu, d):
                    bb, a, b = P
                    dp = plaq_boundary(bb, a, b, d)
                    add(chain_add(ch, dp, +1)); add(chain_add(ch, dp, -1))
    return V


def solve(beta, blocks, Lcap, sense):
    allops = [o for blk in blocks for o in blk]
    V = build_variables(allops, Lcap)
    idx = {k: i for i, k in enumerate(V)}
    x = cp.Variable(len(V))
    cons = [x[idx[canon({}, d)]] == 1]
    neq = 0
    for k, C in V.items():
        for link in list(C.keys()):
            eq = abelian_loop_equation(C, link, d)
            if all(kk in idx for kk in eq):
                cons.append(sum((a + b * beta) * x[idx[kk]] for kk, (a, b) in eq.items()) == 0); neq += 1
    gram_sizes = []
    for blk in blocks:
        valid = [o for o in blk if all(canon(chain_add(o, p, -1), d) in idx for p in blk)]
        if len(valid) >= 2:
            M = cp.bmat([[x[idx[canon(chain_add(Ci, Cj, -1), d)]] for Cj in valid] for Ci in valid])
            cons.append(M >> 0); gram_sizes.append(len(valid))
    tgt = canon(plaq_boundary((0, 0), 0, 1, d), d)            # W(1x1)
    obj = cp.Maximize(x[idx[tgt]]) if sense == "max" else cp.Minimize(x[idx[tgt]])
    cp.Problem(obj, cons).solve(solver="SCS")
    v = x[idx[tgt]].value
    return (None if v is None else float(v)), len(V), neq, gram_sizes


if __name__ == "__main__":
    import time
    print("Gram-scaling: 2D U(1), W(1x1) bracket vs Gram size (does cvxpy keep tightening, or choke?)\n")
    for (K, spw, Lc) in [(3, 1, 14), (4, 2, 18), (5, 2, 22)]:
        blocks = operator_blocks(Kcharge=K, spw=spw)
        beta = 1.0; ex = float(iv(1, beta) / iv(0, beta))
        t0 = time.time()
        lo, nv, ne, gs = solve(beta, blocks, Lc, "min")
        hi, _, _, _ = solve(beta, blocks, Lc, "max")
        dt = time.time() - t0
        if lo is not None:
            print(f"  K={K},spw={spw},Lcap={Lc}: W(1x1) in [{lo:.5f}, {hi:.5f}] width={hi-lo:.4f} "
                  f"exact={ex:.5f}  (vars={nv}, eqs={ne}, gram={gs}, {dt:.0f}s)")
        else:
            print(f"  K={K},spw={spw},Lcap={Lc}: solver None (vars={nv}, eqs={ne}, gram={gs}, {dt:.0f}s)")
    print("\nWidth decreasing with Gram size => keep scaling (cvxpy) until precision/scale wall => SDPB.")
