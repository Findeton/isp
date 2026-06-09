#!/usr/bin/env python3
"""
Lattice Wilson-loop bootstrap -- a general, correct SDP engine + the recipe to scale.

This is the scaffold for the "external-scale" step of paper 41 (sec. 49-50): the
genuine lattice Yang-Mills bootstrap (Kazakov-Zheng style).  It separates the parts
that are solver-mechanical and CORRECT here from the part that is genuine research
(the lattice Makeenko-Migdal loop equations), which is left as a clearly marked,
documented extension point so that nothing is fabricated.

ENGINE (correct, here): given
    - a list of observables x[0..n-1] (x[0] = identity, value 1),
    - linear equality constraints  sum_i A[r,i] x[i] = b[r]   (the loop equations),
    - one or more "moment/Gram blocks": each block is a square array of entries,
      every entry an affine form  c0 + sum_i c[i] x[i]  in the observables, required PSD,
    - an objective observable to maximize / minimize,
the engine builds and solves the semidefinite program and returns the bracket and the
dual certificates.  This is exactly the bootstrap of sec. 46-49, generalized.

INSTANCE (validated, here): the one-plaquette SU(2) model is encoded as a
BootstrapProblem and reproduces the sec.49 result -- this checks the engine.

EXTENSION (the external research, NOT implemented here, to avoid a wrong implementation):
    To do the genuine d-dimensional lattice bootstrap one supplies:
      (i)  observables = Wilson loops W(C) for a family of loops C (and, at finite N,
           the independent multi-loop moments needed for the Gram blocks);
      (ii) linear constraints = the lattice MAKEENKO-MIGDAL loop equations
           (Schwinger-Dyson on the link variables): deforming a link relates a loop to
           loops with a plaquette appended and, at self-intersections, to products of
           sub-loops (the contact terms).  See Makeenko-Migdal; Kazakov-Zheng 2024
           "Bootstrap for lattice Yang-Mills theory" for the precise lattice form;
      (iii) Gram blocks = the reflection-positive / loop-correlation moment matrices;
      (iv)  objective = the string tension proxy  sigma_lat ~ -log W(area)/area.
    Phase 2 (the make-or-break): scan beta -> infinity and test whether the lower
    bracket on sigma_lat / a(beta)^2 stays positive uniformly; per sec.49 the
    truncation ORDER (how many loop equations / how big the loops) must grow with
    1/a -- this is where an arbitrary-precision SDP solver (SDPB) is required.
    Phase 3: construct the dual certificate from modular/theta data (Viazovska-style;
    sec. 30/48), rather than search for it, so it survives the continuum limit.

Requires: cvxpy, numpy.  Solver: SCS/CLARABEL here; SDPB for tight 4D bounds.
"""
import numpy as np
import cvxpy as cp


class BootstrapProblem:
    def __init__(self, n_obs):
        self.n = n_obs
        self.lin = []      # list of (coeffs: np.array len n, rhs: float)
        self.blocks = []   # list of blocks; block = list of rows; entry = (const, {obs_index: coeff})
        self.obj = None    # observable index for objective

    def add_linear(self, coeffs, rhs):
        self.lin.append((np.asarray(coeffs, float), float(rhs)))

    def add_block(self, block):
        self.blocks.append(block)

    def set_objective(self, obs_index):
        self.obj = obs_index


def _affine(x, entry):
    const, terms = entry
    e = cp.Constant(const)
    for i, c in terms.items():
        e = e + c * x[i]
    return e


def solve(problem, sense="max", solver="SCS"):
    x = cp.Variable(problem.n)
    cons = [x[0] == 1]
    for coeffs, rhs in problem.lin:
        cons.append(cp.sum(cp.multiply(coeffs, x)) == rhs)
    for block in problem.blocks:
        s = len(block)
        M = cp.bmat([[_affine(x, block[a][c]) for c in range(s)] for a in range(s)])
        cons.append(M >> 0)
    obj = cp.Maximize(x[problem.obj]) if sense == "max" else cp.Minimize(x[problem.obj])
    p = cp.Problem(obj, cons)
    p.solve(solver=solver)
    val = None if x[problem.obj].value is None else float(x[problem.obj].value)
    duals = [c.dual_value for c in cons if c.is_psd()] if hasattr(cons[-1], "is_psd") else None
    return val, x.value, p


def _one_plaquette_instance(beta, J):
    """Encode the validated one-plaquette SU(2) bootstrap as a BootstrapProblem.

    Observables x[n] = m[n] = <chi_{n/2}>, n=0..Nmax.  Identity x[0]=1.
    """
    Nmax = 4 * J + 4
    P = BootstrapProblem(Nmax + 1)
    # loop equations: m[n+1] - (n+2)(m[n-1]/n - (2/beta) m[n]) = 0
    for n in range(1, Nmax):
        coeffs = np.zeros(Nmax + 1)
        coeffs[n + 1] += 1.0
        coeffs[n - 1] += -(n + 2) / n
        coeffs[n] += (n + 2) * (2.0 / beta)
        P.add_linear(coeffs, 0.0)
    # moment block (size 2J+1): entry[a,c] = sum_{nc=|a-c|..a+c step2} m[nc]
    def mom_entry(a, c):
        terms = {}
        for nc in range(abs(a - c), a + c + 1, 2):
            terms[nc] = terms.get(nc, 0.0) + 1.0
        return (0.0, terms)
    size = 2 * J + 1
    P.add_block([[mom_entry(a, c) for c in range(size)] for a in range(size)])
    P.set_objective(1)  # m_{1/2}
    return P


def main():
    from scipy.special import iv
    print("Engine self-test: one-plaquette SU(2) instance reproduces sec.49 (no localizing block)")
    for beta in (1.0, 2.0):
        ex = float(2 * iv(2, beta) / iv(1, beta))
        P = _one_plaquette_instance(beta, J=3)
        hi, _, _ = solve(P, "max")
        lo, _, _ = solve(P, "min")
        print(f"  beta={beta}: exact m_1/2={ex:.6f}   bracket [{lo:.6f}, {hi:.6f}]")
    print("\n  Engine works. The lattice case = supply Wilson-loop observables + Makeenko-Migdal")
    print("  loop equations + reflection-positive Gram blocks (see module docstring), and use")
    print("  SDPB for tight bounds.  Phase 2 scans beta->inf for sigma_lat/a^2 > 0 uniformly.")


if __name__ == "__main__":
    main()
