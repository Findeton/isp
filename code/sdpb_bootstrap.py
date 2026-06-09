#!/usr/bin/env python3
"""
Bootstrap -> SDPB bridge (paper 42, Target I).

Encodes the SAME 2D U(1) loop-equation bootstrap SDP that tighten_test.py solves
with cvxpy/SCS, but solves it at ARBITRARY PRECISION via SDPB
(bootstrapcollaboration/sdpb Docker image).

Purpose: settle EMPIRICALLY whether the ~1.4 bracket-width saturation on W(1x1)
(seen across 279->1500 cvxpy variables) is PRECISION-limited (then SDPB tightens it)
or STRUCTURAL/operator-basis (then SDPB confirms ~1.4 at 256-bit too).

Formulation (the SDPB-native way -- also the reusable reduction the large system needs):
  the loop equations  A c = 0  and the normalization  c_empty = 1  are EXACT LINEAR
  constraints. SDPB wants a non-degenerate SDP (no free/redundant dual directions:
  SCS regularizes through rank-deficiency, SDPB's exact Cholesky(Q) refuses it). So we
  ELIMINATE the linear constraints: the objective and the Gram blocks depend only on the
  loop variables in S = {target} u {Gram entries}. The achievable values of c_S over the
  feasible affine set {A c = 0, c_empty = 1} form an affine hull  c_S = p_S + U w  (U an
  orthonormal basis of the projected null space, w the reduced free variables). We feed
  SDPB the small, non-degenerate SDP in w:
      maximize  c_target = o0 + sum_k o_k w_k
      s.t.      Gram(c_S) = G0 + sum_k w_k G_k  >= 0     (one block per operator block)
  with the SDPB constant slot y0 (fixed to 1 by normalization) carrying o0 / G0.

SDPB PMP-JSON conventions (reverse-engineered + validated on a trivial 2x2 SDP):
  optimize objective.y s.t. normalization.y = 1 and  sum_n y_n M_n(x) >= 0;  ALL numbers
  are STRINGS; polynomials[row][col][n] = coeff-list of entry (row,col) of M_n (degree 0).
"""
import json
import os
import re
import subprocess
import sys

import numpy as np
from scipy.special import iv

from loops import plaq_boundary, chain_add, canonical_full as canon, plaquettes_with_link
from mm_equations import abelian_loop_equation
from tighten_test import operator_blocks, build_variables, d

IMAGE = "bootstrapcollaboration/sdpb:master"


def build_problem(beta, K, spw, Lcap):
    """Full (unpruned) bootstrap: variables V, loop equations, Gram blocks (as var-index
    matrices), and the empty/target variable indices."""
    blocks = operator_blocks(Kcharge=K, spw=spw)
    allops = [o for blk in blocks for o in blk]
    V = build_variables(allops, Lcap)
    idx = {k: i for i, k in enumerate(V)}
    empty = canon({}, d)

    eqs = []
    for C in V.values():
        for link in list(C.keys()):
            eq = abelian_loop_equation(C, link, d)
            if all(kk in idx for kk in eq):
                eqs.append({idx[kk]: a + b * beta for kk, (a, b) in eq.items()})

    gram_blocks = []
    for blk in blocks:
        valid = [o for o in blk if all(canon(chain_add(o, p, -1), d) in idx for p in blk)]
        if len(valid) >= 2:
            gram_blocks.append([[idx[canon(chain_add(Ci, Cj, -1), d)] for Cj in valid]
                                for Ci in valid])

    target = canon(plaq_boundary((0, 0), 0, 1, d), d)
    return len(V), eqs, gram_blocks, idx[empty], idx[target]


def reduce_sdp(N1, eqs, gram_blocks, norm_idx, target_idx, tol=1e-7):
    """Eliminate the linear constraints. Returns the reduced SDP in free vars w:
       o0, o_lin (objective c_target = o0 + o_lin.w) and per-block (G0, [G_k]) so that
       Gram(c_S) = G0 + sum_k w_k G_k. Non-degenerate: w = orthonormal coords on the
       achievable affine hull of the relevant variables S."""
    # Affine feasible set:  B c = rhs,  B = [loop eqs; e_norm],  rhs = [0..0, 1].
    B = np.zeros((len(eqs) + 1, N1))
    for r, row in enumerate(eqs):
        for j, v in row.items():
            B[r, j] = v
    B[-1, norm_idx] = 1.0
    rhs = np.zeros(len(eqs) + 1)
    rhs[-1] = 1.0
    p, *_ = np.linalg.lstsq(B, rhs, rcond=None)          # particular solution
    _, sv, Vt = np.linalg.svd(B)                          # null space of B
    null_mask = np.concatenate([sv, np.zeros(N1 - len(sv))]) <= tol * (sv[0] if len(sv) else 1)
    Nbasis = Vt[null_mask].T                              # N1 x Knull,  B @ Nbasis = 0

    S = sorted({norm_idx, target_idx} | {v for M in gram_blocks for r in M for v in r})
    pos = {v: i for i, v in enumerate(S)}
    pS = p[S]
    NS = Nbasis[S, :]                                     # |S| x Knull
    U, svr, _ = np.linalg.svd(NS, full_matrices=False)
    r = int(np.sum(svr > tol * (svr[0] if len(svr) else 1)))
    U = U[:, :r]                                          # |S| x r orthonormal hull basis
    # c_S = pS + U w  ->  c_S[pos[v]] for any relevant variable v
    o0 = float(pS[pos[target_idx]])
    o_lin = [float(U[pos[target_idx], k]) for k in range(r)]
    red_blocks = []
    for M in gram_blocks:
        G0 = [[float(pS[pos[M[i][j]]]) for j in range(len(M))] for i in range(len(M))]
        Gk = [[[float(U[pos[M[i][j]], k]) for j in range(len(M))] for i in range(len(M))]
              for k in range(r)]
        red_blocks.append((G0, Gk))
    return r, o0, o_lin, red_blocks


def _s(x):
    return repr(float(x))


def emit_pmp(r, o0, o_lin, red_blocks, sense):
    sgn = 1.0 if sense == "max" else -1.0
    objective = [_s(sgn * o0)] + [_s(sgn * o) for o in o_lin]   # y0 (=1) carries o0
    normalization = ["1"] + ["0"] * r
    arr = []
    for (G0, Gk) in red_blocks:
        m = len(G0)
        # polynomials[i][j] = [ [G0_ij], [G1_ij], ..., [Gr_ij] ]
        polys = [[[[_s(G0[i][j])]] + [[_s(Gk[k][i][j])] for k in range(r)]
                  for j in range(m)] for i in range(m)]
        arr.append({"DampedRational": {"constant": "1", "base": "1", "poles": []},
                    "polynomials": polys})
    return {"objective": objective, "normalization": normalization,
            "PositiveMatrixWithPrefactorArray": arr}


def run_sdpb(pmp, workdir, precision=256):
    import shutil
    shutil.rmtree(workdir, ignore_errors=True)          # clear stale sdp/out/checkpoint
    os.makedirs(workdir, exist_ok=True)
    with open(os.path.join(workdir, "pmp.json"), "w") as f:
        json.dump(pmp, f)
    mount = f"{os.path.abspath(workdir)}:/work"
    conv = subprocess.run(["docker", "run", "--rm", "-v", mount, IMAGE, "pmp2sdp",
                           "-i", "/work/pmp.json", "-o", "/work/sdp", "-p", str(precision)],
                          capture_output=True, text=True)
    if conv.returncode != 0:
        return None, "pmp2sdp: " + conv.stderr[-400:]
    sol = subprocess.run(["docker", "run", "--rm", "-v", mount, IMAGE, "sdpb",
                          "-s", "/work/sdp", "--precision", str(precision),
                          "--procsPerNode", "1", "-o", "/work/out", "--maxIterations", "1000"],
                         capture_output=True, text=True)
    out = os.path.join(workdir, "out", "out.txt")
    if not os.path.exists(out) or not open(out).read().strip():
        err = re.search(r"caught error message:\s*(.*?)Stacktrace", sol.stdout + sol.stderr, re.S)
        return None, "sdpb: " + (err.group(1).strip()[:300] if err else (sol.stdout + sol.stderr)[-300:])
    txt = open(out).read()
    m = re.search(r"primalObjective\s*=\s*([-\d.eE+]+)", txt)
    reason = re.search(r'terminateReason\s*=\s*"([^"]*)"', txt)
    return (float(m.group(1)) if m else None), (reason.group(1) if reason else "?")


if __name__ == "__main__":
    beta = 1.0
    K, spw, Lcap = (int(sys.argv[1]) if len(sys.argv) > 1 else 3,
                    int(sys.argv[2]) if len(sys.argv) > 2 else 1,
                    int(sys.argv[3]) if len(sys.argv) > 3 else 14)
    N1, eqs, gram_blocks, norm_idx, target_idx = build_problem(beta, K, spw, Lcap)
    r, o0, o_lin, red_blocks = reduce_sdp(N1, eqs, gram_blocks, norm_idx, target_idx)
    ex = float(iv(1, beta) / iv(0, beta))
    print(f"SDPB bootstrap test: 2D U(1), beta={beta}, K={K}, spw={spw}, Lcap={Lcap}")
    print(f"  full vars={N1}, loop-eqs={len(eqs)}, gram blocks={[len(M) for M in gram_blocks]}")
    print(f"  reduced free vars (w) = {r}, exact W(1x1) = {ex:.6f}")
    res = {}
    for sense in ("max", "min"):
        pmp = emit_pmp(r, o0, o_lin, red_blocks, sense)
        val, info = run_sdpb(pmp, f"/tmp/sdpb_boot_{sense}", precision=256)
        if val is None:
            print(f"  {sense}: FAILED ({info})")
            res[sense] = None
        else:
            res[sense] = val if sense == "max" else -val
            print(f"  {sense} W(1x1) = {res[sense]:.8f}   [{info}]")
    if res.get("max") is not None and res.get("min") is not None:
        width = res["max"] - res["min"]
        print(f"\n  SDPB(256-bit) bracket: W(1x1) in [{res['min']:.6f}, {res['max']:.6f}]  width={width:.4f}")
        print(f"  cvxpy/SCS gave width 1.3988 on the same convex program.")
        verdict = ("STRUCTURAL: arbitrary precision does NOT shrink it -> operator-basis limit"
                   if width > 1.0 else "precision DID help -> bracket shrinks at high precision")
        print(f"  -> {verdict}.")
