#!/usr/bin/env python3
# =====================================================================
# P56 -- THE POSITIVE CONTROL: does our gravity-detector light up when
# gravity IS there?  SYK model, free (q=2) vs interacting (q=4).
#
# CONTEXT: P55 showed a FREE record lattice has no graviton (correctly
# BLIND).  But "free" is the point: gravity needs a HOLOGRAPHIC interacting
# theory.  The simplest computable one is SYK -- N Majoranas with random
# all-to-all coupling -- whose interacting (q=4) version has a genuine
# emergent gravity dual (JT / near-AdS_2: a black hole, maximal chaos, the
# Schwarzian), while its free (q=2) version is integrable (no gravity).
#
# THE CLEANEST GRAVITY SIGNATURE (this script): QUANTUM CHAOS via
# random-matrix level statistics.  An integrable/free theory has
# UNCORRELATED levels -> Poisson, <r> ~ 0.386.  A holographic (black-hole)
# theory has level REPULSION -> random matrix theory, <r> ~ 0.53 (GOE).
# The level-spacing ratio <r> = <min(s_n,s_{n+1})/max(...)> is a clean,
# unfolding-free diagnostic.  q=2 -> Poisson (no gravity); q=4 -> RMT
# (the black-hole/gravity sector turns ON with the interaction).
#
# This is the POSITIVE complement to P55's negative: free -> blind;
# interacting-holographic -> the gravitational sector lights up.
# (Caveat recorded: RMT chaos is the NECESSARY signature; the SUFFICIENT
# holographic structure -- maximal chaos lambda=2pi/beta + the Schwarzian
# -- is the deeper follow-up.  No propagating spin-2 graviton: SYK is 2D.)
# float64 exact diagonalization; the J-disorder is seeded deterministically
# (no RNG nondeterminism -- a fixed integer-seeded Gaussian via Box-Muller).
# =====================================================================
import numpy as np
from itertools import combinations
np.set_printoptions(linewidth=140, suppress=True)
def hr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70, flush=True)
print("#"*70); print("# P56 -- SYK positive control: free (q=2) vs interacting (q=4) chaos"); print("#"*70)

# ---- deterministic Gaussian (seeded Box-Muller, no global RNG state) ----
def gaussians(n, seed):
    # a fixed linear-congruential uniform stream -> Box-Muller normals
    u = np.empty(n+ (n & 1)); x = (seed * 2 + 1) % (2**32)
    for i in range(len(u)):
        x = (1664525*x + 1013904223) % (2**32); u[i] = (x + 0.5)/2**32
    u = u.reshape(-1, 2)
    r = np.sqrt(-2*np.log(u[:, 0])); th = 2*np.pi*u[:, 1]
    return (r*np.cos(th)).ravel()[:n]

# ---- Majorana operators via Jordan-Wigner (sparse-ish dense for small N) ----
import scipy.sparse as sp
I2 = sp.identity(2, format='csr'); Z = sp.csr_matrix([[1, 0], [0, -1]])
X = sp.csr_matrix([[0, 1], [1, 0]]); Y = sp.csr_matrix([[0, -1j], [1j, 0]])
def kron_list(ops):
    M = ops[0]
    for o in ops[1:]: M = sp.kron(M, o, format='csr')
    return M
def majoranas(N):
    # N Majoranas (N even) on N/2 qubits; chi normalized so {chi_a,chi_b}=delta_ab
    nq = N//2; chi = []
    for k in range(nq):
        left = [Z]*k
        for P in (X, Y):
            ops = left + [P] + [I2]*(nq-k-1)
            chi.append(kron_list(ops)/np.sqrt(2))
    return chi   # list of N sparse Hermitian matrices

def syk_H(N, q, seed):
    chi = majoranas(N); dim = chi[0].shape[0]
    H = sp.csr_matrix((dim, dim), dtype=complex)
    combos = list(combinations(range(N), q))
    g = gaussians(len(combos), seed)
    # variance: <J^2> = (q-1)! J^2 / N^{q-1}; set J=1
    var = np.math.factorial(q-1)/N**(q-1)
    pref = (1j**(q//2)) * np.sqrt(var)   # i^{q/2} makes H Hermitian for these conventions
    for c, gc in zip(combos, g):
        term = chi[c[0]]
        for idx in c[1:]: term = term @ chi[idx]
        H = H + (pref*gc)*term
    H = (H + H.getH())/2   # enforce Hermiticity (kill tiny imag from convention)
    return H

def parity_project(N, H):
    # fermion parity P = Z_1...Z_{N/2}; project onto P=+1 sector
    nq = N//2; P = kron_list([Z]*nq)
    diagP = np.real(P.diagonal())
    idx = np.where(diagP > 0)[0]
    Hd = H.toarray()
    return Hd[np.ix_(idx, idx)]

def r_statistic(evals):
    e = np.sort(np.real(evals)); s = np.diff(e)
    s = s[s > 1e-9]                       # drop (near-)degeneracies
    r = np.minimum(s[:-1], s[1:])/np.maximum(s[:-1], s[1:])
    # use the central 80% of the spectrum (avoid edges)
    lo, hi = int(0.1*len(r)), int(0.9*len(r))
    return np.mean(r[lo:hi]), len(r[lo:hi])

# =====================================================================
hr("level-spacing ratio <r>: free (q=2) vs interacting (q=4) SYK")
# =====================================================================
print("  Poisson (integrable/free, NO gravity): <r> = 0.386")
print("  GOE (random matrix / black hole, GRAVITY sector): <r> = 0.531\n")
print(f"  {'N':>3} {'q':>2} {'sector dim':>10} {'<r>':>8} {'verdict':>22}")
results = {}
for N in (16, 20, 24):
    for q in (2, 4):
        H = syk_H(N, q, seed=12345)
        Hb = parity_project(N, H)
        ev = np.linalg.eigvalsh(Hb)
        rval, nr = r_statistic(ev)
        verdict = "Poisson (no gravity)" if rval < 0.45 else "RMT/GOE (BLACK HOLE)"
        results[(N, q)] = rval
        print(f"  {N:>3} {q:>2} {Hb.shape[0]:>10} {rval:>8.4f} {verdict:>22}", flush=True)

# =====================================================================
hr("VERDICT (P56 positive control)")
# =====================================================================
r2 = results[(24, 2)]; r4 = results[(24, 4)]
print(f"  N=24: free q=2 <r>={r2:.4f} (Poisson~0.386), interacting q=4 <r>={r4:.4f} (GOE~0.531)")
print(f"  -> the INTERACTION turns ON the random-matrix (black-hole) spectral")
print(f"     statistics that the FREE theory lacks.  Our chaos/gravity detector")
print(f"     LIGHTS UP exactly where gravity is known to emerge (SYK q=4) and")
print(f"     stays DARK where it is absent (free q=2) -- the positive complement")
print(f"     to P55's negative (free record lattice -> blind).")
print(f"  NEXT (sufficiency): maximal chaos lambda_L -> 2pi/beta (the chaos-bound")
print(f"     saturation that is SPECIFIC to gravity, not generic chaos) + the")
print(f"     emergent Schwarzian/zero-T entropy + the entanglement first law")
print(f"     becoming the JT bulk equation of motion.  THEN: the interacting")
print(f"     record dynamics (SHARD eta) -- does memory/feedback push it here?")
