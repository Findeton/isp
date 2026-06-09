#!/usr/bin/env python3
"""
Wire the CLOSED SU(2) coherent bootstrap to SDPB at arbitrary precision (paper 42, M3 step 2).

The §18.10 closure tightens the W(1x1) bracket monotonically with depth (1.26 -> 0.97 -> 0.48
at beta=2), but CLARABEL hits its numerical ceiling around depth 4 / beta 4. This module reuses
the validated eliminate-then-positivity reduction (sdpb_bootstrap.py, 18.7), generalized to the
combined singles+pairs variable vector z=(x;y):

  - equalities (loop equations + W(empty)=1): linear in z -> eliminate by parametrizing the
    feasible affine hull z = p + V w  (w the free variables, V = null space of the equality
    matrix). This makes the SDP NON-DEGENERATE (no free/redundant dual directions), as SDPB
    requires.
  - PSD blocks in z -> in w: the 2-loop Gram block, and the SU(2) pointwise bounds 1 +- z_k >= 0
    (each a 1x1 block). Objective x[target] = o0 + o.w.

Then emit SDPB PMP-JSON via sdpb_bootstrap.emit_pmp / run_sdpb (256-bit), and compare to CLARABEL.
"""
import sys
import numpy as np

from su2_loops import plaquette_walk, skey, pkey
from su2_bootstrap import close, seed_walks, gram_ops_default, c1, d, EMPTY
from sdpb_bootstrap import emit_pmp, run_sdpb


def assemble(beta, equations, gram_ops):
    singles, pairs = {EMPTY}, set()
    for (lt, bt) in equations:
        singles |= set(lt); pairs |= set(bt)
    singles |= {skey(o, d) for o in gram_ops}
    for oi in gram_ops:
        for oj in gram_ops:
            pairs.add(pkey(oi, oj, d))
    S = sorted(singles)
    Pr = sorted(pairs)
    sidx = {k: i for i, k in enumerate(S)}
    pidx = {k: len(S) + i for i, k in enumerate(Pr)}
    nz = len(S) + len(Pr)

    rows, rhs = [], []
    for (lt, bt) in equations:
        if not all(k in sidx for k in lt) or not all(p in pidx for p in bt):
            continue
        row = np.zeros(nz)
        for k, (a, b) in lt.items():
            row[sidx[k]] += a + b * beta
        for p, (a, b) in bt.items():
            row[pidx[p]] += a + b * beta
        rows.append(row); rhs.append(0.0)
    row = np.zeros(nz); row[sidx[EMPTY]] = 1.0
    rows.append(row); rhs.append(1.0)
    return sidx, pidx, nz, np.array(rows), np.array(rhs)


def reduce_blocks(beta, equations, gram_ops, tol=1e-7):
    sidx, pidx, nz, B, rhs = assemble(beta, equations, gram_ops)
    p, *_ = np.linalg.lstsq(B, rhs, rcond=None)
    _, sv, Vt = np.linalg.svd(B)
    mask = np.concatenate([sv, np.zeros(nz - len(sv))]) <= tol * (sv[0] if len(sv) else 1)
    V = Vt[mask].T                                          # nz x r, B@V = 0
    r = V.shape[1]
    t = sidx[skey(plaquette_walk((0, 0), 0, 1, d), d)]
    o0 = float(p[t]); o_lin = [float(V[t, k]) for k in range(r)]

    red = []
    # 2-loop Gram block (unit operator as row/col 0)
    n = len(gram_ops)
    G0 = [[0.0] * (n + 1) for _ in range(n + 1)]
    Gk = [[[0.0] * (n + 1) for _ in range(n + 1)] for _ in range(r)]
    G0[0][0] = 1.0

    def put(i, j, zi):
        G0[i][j] = float(p[zi])
        for k in range(r):
            Gk[k][i][j] = float(V[zi, k])
    for i, oi in enumerate(gram_ops):
        zi = sidx[skey(oi, d)]
        put(0, i + 1, zi); put(i + 1, 0, zi)
        for j, oj in enumerate(gram_ops):
            put(i + 1, j + 1, pidx[pkey(oi, oj, d)])
    red.append((G0, Gk))
    # SU(2) pointwise bounds: 1 - z_zi >= 0 and 1 + z_zi >= 0
    for zi in range(nz):
        red.append(([[1.0 - float(p[zi])]], [[[-float(V[zi, k])]] for k in range(r)]))
        red.append(([[1.0 + float(p[zi])]], [[[float(V[zi, k])]] for k in range(r)]))
    return r, o0, o_lin, red, nz


def sdpb_bracket(beta, equations, gram_ops, precision=256):
    r, o0, o_lin, red, nz = reduce_blocks(beta, equations, gram_ops)
    res = {}
    for sense in ("max", "min"):
        pmp = emit_pmp(r, o0, o_lin, red, sense)
        val, info = run_sdpb(pmp, f"/tmp/su2_sdpb_{sense}", precision=precision)
        # emit_pmp maximizes -x[target] for the "min" sense, so negate to recover min.
        res[sense] = (None, info) if val is None else (val if sense == "max" else -val, info)
    return res, r, nz


if __name__ == "__main__":
    depth = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    beta = float(sys.argv[2]) if len(sys.argv) > 2 else 2.0
    gram_ops = gram_ops_default()
    eqs, seen = close(seed_walks(), depth=depth, max_steps=16)
    print(f"SU(2) closed bootstrap -> SDPB (256-bit): depth={depth}, beta={beta}")
    print(f"  closed: {len(seen)} walks, {len(eqs)} equations")
    res, r, nz = sdpb_bracket(beta, eqs, gram_ops)
    ex = c1(beta)
    print(f"  combined vars z (singles+pairs) = {nz}, reduced free w = {r}, exact W(1x1)={ex:.5f}")
    lo, hi = res["min"][0], res["max"][0]
    if lo is None or hi is None:
        print(f"  max: {res['max']}\n  min: {res['min']}")
    else:
        ok = "OK" if lo - 1e-6 <= ex <= hi + 1e-6 else "** NOT CONTAINED **"
        print(f"  SDPB W(1x1) in [{lo:.6f}, {hi:.6f}] width={hi-lo:.5f} exact={ex:.5f} [{ok}]")
        print(f"    [{res['max'][1]} / {res['min'][1]}]")
