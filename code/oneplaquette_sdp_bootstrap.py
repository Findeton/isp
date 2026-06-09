#!/usr/bin/env python3
"""
One-plaquette SU(2) bootstrap via a genuine semidefinite program (SDP).

This is the validated Phase-0 computation recorded in paper 41, sections 47 and 49.
It reproduces the EXACT one-plaquette result WITHOUT evaluating the group integral,
using only:
  (A) the exact loop equation (Schwinger-Dyson / Bessel recursion), and
  (B) positivity of the character moment (Gram) matrix + a localizing matrix.

Model: weight ~ exp(beta * (1/2) tr U) on a single SU(2) plaquette.
Moments: m[n] = < chi_{n/2}(U) >, with m[0]=1.  (chi_{1/2}=2cos a, etc.)

Exact answer (for cross-check):  m_{1/2} = 2 I_2(beta)/I_1(beta).

Loop equation (exact):  m[n+1] = (n+2) ( m[n-1]/n - (2/beta) m[n] ),  n>=1.
Positivity:
  moment matrix   M[a,c] = sum_{nc=|a-c|..a+c step 2} m[nc]            (>= 0)
  localizing mat  L[a,c] = 3 M[a,c] - sum_{a' in {a-2,a,a+2}} M[a',c]  (>= 0)
                  (enforces support chi_{1/2} in [-2,2], i.e. 4 - chi_{1/2}^2 = 3 - chi_1 >= 0)

Results (paper 41, section 49):
  - full loop equations:  SDP pins the exact value to ~1e-10 at cutoff J=2.
  - truncated loop equations (order K, higher moments free): the bracket tightens
    with K (the number of exact relations), not just with matrix size J -- the
    Phase-2 truncation-vs-continuum structure in miniature.
  - the dual certificate of the moment-PSD constraint is extracted (rank one).

Requires: cvxpy, numpy, scipy.  Solver: CLARABEL or SCS (open source).
Tight bounds (e.g. beta>=5) need an arbitrary-precision SDP solver (SDPB).
"""
import sys
import numpy as np
import cvxpy as cp
from scipy.special import iv


def exact_m_half(beta):
    return float(2 * iv(2, beta) / iv(1, beta))


def _moment_matrix_expr(m, size):
    """M[a,c] = sum_{nc=|a-c|..a+c step 2} m[nc]   (affine in the cvxpy variable m)."""
    rows = []
    for a in range(size):
        row = []
        for c in range(size):
            terms = [m[nc] for nc in range(abs(a - c), a + c + 1, 2)]
            row.append(cp.sum(terms) if terms else cp.Constant(0))
        rows.append(row)
    return cp.bmat(rows)


def bootstrap(beta, J, Kloop=None, solver="SCS"):
    """
    Bracket m_{1/2} subject to loop equations (up to order Kloop; None = all) and
    moment + localizing positivity, with character cutoff spin J (matrix size 2J+1).
    Returns (lo, hi, moment_PSD_dual_certificate).
    """
    Nmax = 4 * J + 4
    if Kloop is None:
        Kloop = Nmax
    m = cp.Variable(Nmax + 1)
    cons = [m[0] == 1]
    for n in range(1, min(Kloop, Nmax)):
        cons += [m[n + 1] == (n + 2) * (m[n - 1] / n - (2.0 / beta) * m[n])]
    Mbig = _moment_matrix_expr(m, 2 * J + 3)
    M = Mbig[: 2 * J + 1, : 2 * J + 1]
    Lrows = []
    for a in range(2 * J + 1):
        nbrs = [v for v in (a - 2, a, a + 2) if 0 <= v <= 2 * J + 2]
        Lrows.append([3 * Mbig[a, c] - cp.sum([Mbig[v, c] for v in nbrs])
                      for c in range(2 * J + 1)])
    L = cp.bmat(Lrows)
    Mcon = (M >> 0)
    cons += [Mcon, L >> 0]

    cp.Problem(cp.Maximize(m[1]), cons).solve(solver=solver)
    hi, cert = m[1].value, Mcon.dual_value
    cp.Problem(cp.Minimize(m[1]), cons).solve(solver=solver)
    lo = m[1].value
    lo = None if lo is None else float(lo)
    hi = None if hi is None else float(hi)
    return lo, hi, cert


def main():
    print("== Validation: full loop equations, SDP brackets the exact m_1/2 ==")
    for beta in (1.0, 2.0):
        ex = exact_m_half(beta)
        print(f"beta={beta}: exact m_1/2 = {ex:.6f}")
        for J in (1, 2, 3):
            lo, hi, _ = bootstrap(beta, J)
            if lo is not None:
                print(f"   J={J}: [{lo:.6f}, {hi:.6f}]  width={hi-lo:.2e}")

    print("\n== Convergence: truncated loop equations (order K, higher moments free) ==")
    beta = 2.0
    print(f"beta={beta}: exact m_1/2 = {exact_m_half(beta):.6f}")
    for (J, K) in ((2, 2), (3, 2), (4, 2), (3, 3), (4, 4)):
        lo, hi, _ = bootstrap(beta, J, Kloop=K)
        if lo is not None:
            print(f"   J={J}, K={K}: [{lo:.5f}, {hi:.5f}]  width={hi-lo:.3e}")

    print("\n== Dual certificate (moment-PSD), J=3 ==")
    _, _, cert = bootstrap(2.0, 3, Kloop=3)
    print("   eigenvalues:", np.round(np.linalg.eigvalsh(np.array(cert)), 4))
    print("   (rank-one: a single dominant mode certifies the bound)")


if __name__ == "__main__":
    sys.exit(main())
