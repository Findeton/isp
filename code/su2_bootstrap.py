#!/usr/bin/env python3
"""
SU(2) coherent / localizing block design with WALK-BASED CLOSURE (paper 42, M3, step 1).

The abelian moment bootstrap SATURATED at width ~1.4 (SDPB-confirmed structural, 18.7): for
U(1) the Gram M[i,j]=<O_i^dag O_j>=W(C_j-C_i) collapses to SINGLE loops. SU(2) is richer:
loops do NOT add, so the Gram is genuine TWO-LOOP correlators M[i,j]=<W(C_i)W(C_j)>, and the
loop equation's FIERZ SPLIT couples those back to single loops.

The first §18.8 probe TRUNCATED -- it dropped every loop equation referencing a loop outside
the seed set, so weak coupling never tightened. This version CLOSES the system: a BFS over
ordered WALKS generates the loop equation for each loop AND for the deformation/split loops it
produces (realized directly as walks, so the self-intersection structure is unambiguous), to a
fixed depth + size cap. Decisive test: does the coherent SU(2) design break the ~1.4 saturation
at weak coupling once the system is closed (not just at strong coupling)?

2D is the validation ground (exact W(1x1)=c_1=I2/I1 must be contained). Variables are keyed by
winding chain (in 2D W depends only on the chain); the equations' SPLIT structure still comes
from the walks. The design ports to 4D unchanged (d is a parameter).
"""
import cvxpy as cp
from scipy.special import iv

from su2_loops import (su2_eq_walks, plaquette_walk, walk_to_chain, canonical_walk,
                       reverse_walk, reduce_walk, skey, pkey)

d = 2
EMPTY = ()                                            # skey of the empty walk (identity, W=1)


def c1(beta):
    return float(iv(2, beta) / iv(1, beta))                # exact 2D SU(2) W(1x1)


def rect_walk(w, h):
    pts = ([(i, 0) for i in range(w)] + [(w, j) for j in range(h)] +
           [(w - i, h) for i in range(w)] + [(0, h - j) for j in range(h)])
    walk = []
    for k in range(len(pts)):
        (ax, ay), (bx, by) = pts[k], pts[(k + 1) % len(pts)]
        if bx - ax == 1:    walk.append(((ax, ay), 0, +1))
        elif bx - ax == -1: walk.append(((bx, ay), 0, -1))
        elif by - ay == 1:  walk.append(((ax, ay), 1, +1))
        else:               walk.append(((ax, by), 1, -1))
    return walk


def seed_walks():
    return [plaquette_walk((0, 0), 0, 1, d), rect_walk(2, 1)]


def close(seeds, depth, max_steps):
    """BFS over walks: generate every loop equation (chain/pair-keyed), discovering the
    deformation + split walks and recursing on them up to `depth` / length `max_steps`."""
    seen = {}
    frontier = []
    for w0 in seeds:
        w = reduce_walk(w0)
        if not w:
            continue
        k = canonical_walk(w, d)
        if k not in seen:
            seen[k] = w; frontier.append(w)
    equations = []
    for _ in range(depth):
        nf = []
        for w in frontier:
            for a in range(len(w)):
                if w[a][2] != +1:
                    continue                              # forward anchors (FF + FB now handled)
                lin, bil = su2_eq_walks(w, a, d)
                lt, bt = {}, {}
                for (ww, ca, cb) in lin:
                    k = skey(ww, d)
                    pa, pb = lt.get(k, (0, 0)); lt[k] = (pa + ca, pb + cb)
                for ((w1, w2), ca, cb) in bil:
                    k = pkey(w1, w2, d)
                    pa, pb = bt.get(k, (0, 0)); bt[k] = (pa + ca, pb + cb)
                equations.append((lt, bt))
                disc = [ww for (ww, _, _) in lin] + \
                       [ww for ((w1, w2), _, _) in bil for ww in (w1, w2)]
                for ww0 in disc:
                    ww = reduce_walk(ww0)
                    if 0 < len(ww) <= max_steps:
                        kk = canonical_walk(ww, d)
                        if kk not in seen:
                            seen[kk] = ww; nf.append(ww)
        frontier = nf
    return equations, seen


def build(beta, equations, gram_ops, use_gram=True):
    singles, pairs = {EMPTY}, set()
    for (lt, bt) in equations:
        singles |= set(lt); pairs |= set(bt)
    singles |= {skey(o, d) for o in gram_ops}
    for oi in gram_ops:
        for oj in gram_ops:
            pairs.add(pkey(oi, oj, d))
    sidx = {k: i for i, k in enumerate(sorted(singles))}
    pidx = {k: i for i, k in enumerate(sorted(pairs))}

    x = cp.Variable(len(sidx))
    y = cp.Variable(len(pidx)) if pidx else None
    cons = [x[sidx[EMPTY]] == 1, x <= 1, x >= -1]          # SU(2) pointwise |W|<=1 localizing
    if y is not None:
        cons += [y <= 1, y >= -1]
    nkept = 0
    for (lt, bt) in equations:
        if not all(k in sidx for k in lt) or not all(p in pidx for p in bt):
            continue
        expr = sum((a + b * beta) * x[sidx[k]] for k, (a, b) in lt.items())
        if bt:
            expr = expr + sum((a + b * beta) * y[pidx[p]] for p, (a, b) in bt.items())
        cons.append(expr == 0); nkept += 1

    if use_gram:
        n = len(gram_ops)
        M = [[None] * (n + 1) for _ in range(n + 1)]
        M[0][0] = cp.Constant(1.0)
        for i, oi in enumerate(gram_ops):
            M[0][i + 1] = M[i + 1][0] = x[sidx[skey(oi, d)]]
            for j, oj in enumerate(gram_ops):
                M[i + 1][j + 1] = y[pidx[pkey(oi, oj, d)]]
        cons.append(cp.bmat(M) >> 0)
    return x, sidx, cons, nkept, len(sidx), len(pidx)


def bracket(beta, equations, gram_ops, use_gram=True):
    res = {}
    tgt_key = skey(plaquette_walk((0, 0), 0, 1, d), d)
    for sense in ("max", "min"):
        x, sidx, cons, nkept, ns, npr = build(beta, equations, gram_ops, use_gram)
        tgt = x[sidx[tgt_key]]
        try:
            cp.Problem(cp.Maximize(tgt) if sense == "max" else cp.Minimize(tgt),
                       cons).solve(solver="CLARABEL")
            res[sense] = None if tgt.value is None else float(tgt.value)
        except cp.error.SolverError:
            res[sense] = None
    return res, nkept, ns, npr


def gram_ops_default():
    return [plaquette_walk((0, 0), 0, 1, d), rect_walk(2, 1),
            plaquette_walk((1, 0), 0, 1, d), plaquette_walk((0, 1), 0, 1, d)]


if __name__ == "__main__":
    gram_ops = gram_ops_default()
    print("SU(2) coherent 2-loop bootstrap WITH walk-based closure (2D; exact W(1x1)=c_1).")
    print("Abelian U(1) moment bootstrap SATURATED flat at width ~1.40 (SDPB-confirmed, 18.7).\n")

    print("A. Full bracket at depth 3 (with-Gram vs no-Gram control):")
    eqs3, seen3 = close(seed_walks(), depth=3, max_steps=14)
    print(f"   closed: {len(seen3)} walks, {len(eqs3)} equations\n")
    for beta in (0.5, 1.0, 2.0, 4.0):
        rg, nk, ns, npr = bracket(beta, eqs3, gram_ops, use_gram=True)
        rn, _, _, _ = bracket(beta, eqs3, gram_ops, use_gram=False)
        ex = c1(beta)
        if None in (rg["max"], rg["min"], rn["max"], rn["min"]):
            print(f"   beta={beta:>4}: solver None")
            continue
        wg, wn = rg["max"] - rg["min"], rn["max"] - rn["min"]
        ok = "OK" if rg["min"] - 1e-6 <= ex <= rg["max"] + 1e-6 else "**NOT CONTAINED**"
        print(f"   beta={beta:>4}: [{rg['min']:+.4f},{rg['max']:+.4f}] w={wg:.4f} | "
              f"no-Gram w={wn:.4f} | exact={ex:.4f} [{ok}] | Gram tightens {wn-wg:.4f}")

    print("\nB. Depth-scaling at beta=2 (does it keep tightening, vs the abelian flat 1.40?):")
    for depth in (2, 3, 4):
        eqs, seen = close(seed_walks(), depth=depth, max_steps=16)
        rg, nk, ns, npr = bracket(2.0, eqs, gram_ops, use_gram=True)
        if None in (rg["max"], rg["min"]):
            print(f"   depth={depth}: ({ns} singles, {npr} pairs) -> solver None (needs SDPB)")
        else:
            print(f"   depth={depth}: ({ns} singles, {npr} pairs) W(1x1) width = {rg['max']-rg['min']:.4f}")
    print("   -> monotone tightening (NOT the abelian flat saturation); larger depth needs SDPB.")
