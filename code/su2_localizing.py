#!/usr/bin/env python3
"""
SU(2) bootstrap with LOCALIZING BLOCKS + the string-tension objective (paper 42, §18.12).

The bare 2-loop Gram tightens only modestly (§18.11). Localizing matrices are the documented core
ingredient for SHARP bootstrap bounds:

    M^{+-}_p[i,j] = <W(C_i) (1 +- W_p) W(C_j)>  >= 0     (1 +- W_p >= 0 pointwise for SU(2)),

whose entries are two- and THREE-loop correlators. The 3-loop correlators are constrained by the
PRODUCT Schwinger-Dyson equations (su2_products.product_eq_walks). This module assembles:
  variables   : singles x, pairs y, triples z (walk/holonomy keys)
  constraints : single-loop eqs (x,y); product eqs (y,z); 2-loop Gram; localizing M^{+-}_p;
                pointwise bounds |.|<=1; W(empty)=1
and brackets W(1x1) (2D go/no-go: does it approach the exact c_1?), then any loop for sigma.
"""
import cvxpy as cp
from scipy.special import iv

from su2_loops import su2_eq_walks, plaquette_walk, skey, pkey
from su2_products import product_eq_walks, tkey
from su2_bootstrap import close, seed_walks, rect_walk, c1, d, EMPTY


def build_equations(depth, max_steps, spectators):
    """Single-loop closure + product equations (each loop x each spectator not sharing the anchor)."""
    single, seen = close(seed_walks(), depth=depth, max_steps=max_steps)   # [(lt,bt)], {key:walk}
    prod = []                                                              # [(bt_pairs, tt_triples)]
    for w in seen.values():
        for a in range(len(w)):
            if w[a][2] != +1:
                continue
            for Cp in spectators:
                pe = product_eq_walks(w, a, Cp, d)
                if pe is None:
                    continue
                bil, tri = pe
                bt = {}
                for ((X, Y), ca, cb) in bil:
                    k = pkey(X, Y, d); pa, pb = bt.get(k, (0, 0)); bt[k] = (pa + ca, pb + cb)
                tt = {}
                for ((X, Y, Z), ca, cb) in tri:
                    k = tkey(X, Y, Z, d); pa, pb = tt.get(k, (0, 0)); tt[k] = (pa + ca, pb + cb)
                if bt or tt:
                    prod.append((bt, tt))
    return single, prod


def solve(beta, single, prod, gram_ops, loc_plaqs, use_loc, sense):
    sK = {EMPTY}
    pK, tK = set(), set()
    for (lt, bt) in single:
        sK |= set(lt); pK |= set(bt)
    for (bt, tt) in prod:
        pK |= set(bt); tK |= set(tt)
    sK |= {skey(o, d) for o in gram_ops}
    ops = gram_ops
    for oi in ops:
        for oj in ops:
            pK.add(pkey(oi, oj, d))
    if use_loc:
        for p in loc_plaqs:
            sK.add(skey(p, d))
            for oi in ops:
                pK.add(pkey(p, oi, d))
                for oj in ops:
                    tK.add(tkey(oi, p, oj, d))
    si = {k: i for i, k in enumerate(sorted(sK))}
    pi = {k: i for i, k in enumerate(sorted(pK))}
    ti = {k: i for i, k in enumerate(sorted(tK))}
    x = cp.Variable(len(si)); y = cp.Variable(len(pi)); z = cp.Variable(len(ti)) if ti else None

    cons = [x[si[EMPTY]] == 1, x <= 1, x >= -1, y <= 1, y >= -1]
    if z is not None:
        cons += [z <= 1, z >= -1]
    for (lt, bt) in single:
        if not all(k in si for k in lt) or not all(k in pi for k in bt):
            continue
        e = sum((a + b * beta) * x[si[k]] for k, (a, b) in lt.items())
        if bt:
            e = e + sum((a + b * beta) * y[pi[k]] for k, (a, b) in bt.items())
        cons.append(e == 0)
    for (bt, tt) in prod:
        if not all(k in pi for k in bt) or not all(k in ti for k in tt):
            continue
        e = sum((a + b * beta) * y[pi[k]] for k, (a, b) in bt.items())
        if tt:
            e = e + sum((a + b * beta) * z[ti[k]] for k, (a, b) in tt.items())
        cons.append(e == 0)

    # 2-loop Gram
    n = len(ops)
    M = [[None] * (n + 1) for _ in range(n + 1)]; M[0][0] = cp.Constant(1.0)
    for i, oi in enumerate(ops):
        M[0][i + 1] = M[i + 1][0] = x[si[skey(oi, d)]]
        for j, oj in enumerate(ops):
            M[i + 1][j + 1] = y[pi[pkey(oi, oj, d)]]
    cons.append(cp.bmat(M) >> 0)

    # localizing blocks M^{+-}_p
    if use_loc:
        for p in loc_plaqs:
            xp = x[si[skey(p, d)]]
            for s in (+1, -1):
                L = [[None] * (n + 1) for _ in range(n + 1)]
                L[0][0] = 1.0 + s * xp
                for i, oi in enumerate(ops):
                    off = x[si[skey(oi, d)]] + s * y[pi[pkey(p, oi, d)]]
                    L[0][i + 1] = L[i + 1][0] = off
                    for j, oj in enumerate(ops):
                        L[i + 1][j + 1] = y[pi[pkey(oi, oj, d)]] + s * z[ti[tkey(oi, p, oj, d)]]
                cons.append(cp.bmat(L) >> 0)

    tgt = x[si[skey(plaquette_walk((0, 0), 0, 1, d), d)]]
    prob = cp.Problem(cp.Maximize(tgt) if sense == "max" else cp.Minimize(tgt), cons)
    for solver in ("CLARABEL", "SCS"):
        try:
            prob.solve(solver=solver)
            if tgt.value is not None:
                return float(tgt.value), len(si), len(pi), len(ti)
        except cp.error.SolverError:
            continue
    return None, len(si), len(pi), len(ti)


def bracket(beta, single, prod, gram_ops, loc_plaqs, use_loc):
    lo, ns, npr, nt = solve(beta, single, prod, gram_ops, loc_plaqs, use_loc, "min")
    hi, _, _, _ = solve(beta, single, prod, gram_ops, loc_plaqs, use_loc, "max")
    return lo, hi, ns, npr, nt


if __name__ == "__main__":
    gram_ops = [plaquette_walk((0, 0), 0, 1, d), rect_walk(2, 1),
                plaquette_walk((1, 0), 0, 1, d), plaquette_walk((0, 1), 0, 1, d)]
    loc_plaqs = [plaquette_walk((0, 0), 0, 1, d)]
    spectators = gram_ops
    DEPTH, MAXLEN = 3, 14
    single, prod = build_equations(DEPTH, MAXLEN, spectators)
    print(f"SU(2) localizing-block bootstrap (2D go/no-go), depth={DEPTH}")
    print(f"  single-loop eqs={len(single)}, product eqs={len(prod)}\n")
    print("  Does adding the localizing block (3-loop) tighten W(1x1) vs the bare 2-loop Gram?\n")
    for beta in (1.0, 2.0):
        ex = c1(beta)
        lo0, hi0, ns, npr, nt0 = bracket(beta, single, prod, gram_ops, loc_plaqs, use_loc=False)
        lo1, hi1, ns1, npr1, nt = bracket(beta, single, prod, gram_ops, loc_plaqs, use_loc=True)
        if None in (lo0, hi0, lo1, hi1):
            print(f"  beta={beta}: solver None  (bare {lo0,hi0}, loc {lo1,hi1})")
            continue
        ok0 = "OK" if lo0 - 1e-6 <= ex <= hi0 + 1e-6 else "NOT-CONT"
        ok1 = "OK" if lo1 - 1e-6 <= ex <= hi1 + 1e-6 else "NOT-CONT"
        print(f"  beta={beta}: bare-Gram  w={hi0-lo0:.4f} [{lo0:.4f},{hi0:.4f}] [{ok0}]  "
              f"(x={ns},y={npr})")
        print(f"           +localizing w={hi1-lo1:.4f} [{lo1:.4f},{hi1:.4f}] [{ok1}]  "
              f"(z triples={nt})   exact={ex:.4f}")