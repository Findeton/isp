#!/usr/bin/env python3
"""
v6_p18e: the nonabelian seam/anomaly predicates, computed from
generators (Paper 18 Part II).

Paper 14's abelian filter is lifted to the reconstructed nonabelian
fibers.  Nothing is quoted: every anomaly coefficient below is COMPUTED
from explicit representation generators by the trace identities

   tr_R(T^a T^b)        = T(R) delta^ab          (Dynkin index)
   tr_R(T^a {T^b,T^c})  = (1/2) A(R) d^abc       (cubic coefficient),

with the fundamental's d-symbol as the reference tensor.

 (i)   SU(3) representation data from built generators (fund = Gell-
       Mann/2; antifund = -transpose; adjoint from the structure
       constants; 6 = Sym^2(fund); 10 = Sym^3(fund)): Dynkin indices
       T(R) and cubic coefficients A(R), with the PROPORTIONALITY
       RECEIPT ||D_R - A(R) D_fund|| ~ 1e-14 (the cubic trace tensor of
       every rep is exactly proportional to the d-symbol: the predicate
       is one number per rep).
 (ii)  SU(2) HAS NO CUBIC ANOMALY: the d-tensor vanishes identically
       (machine zero) - its place is taken by the WITTEN global
       constraint (named import, pi_4(SU(2)) = Z_2): the number of
       Weyl doublets must be EVEN.
 (iii) THE PREDICATE STACK for a content {(c_i, w_i, Y_i)}:
         SU(3)^3:        sum A(c_i) dim(w_i)            = 0
         SU(3)^2-U(1):   sum T(c_i) dim(w_i) Y_i        = 0
         SU(2)^2-U(1):   sum T(w_i) dim(c_i) Y_i        = 0
         U(1)^3:         sum dim_i Y_i^3                = 0
         U(1)-grav:      sum dim_i Y_i                  = 0
         WITTEN:         sum over doublets of dim(c_i)  even
         Z_6 LATTICE:    2 t(c_i) + 3 d(w_i) + Y_i      = 0 mod 6
       (the last is Paper 17's quotient receipt PROMOTED to a
       structural constraint: charges live on the quotient lattice).
"""
import numpy as np
from itertools import product as iproduct

# ---------- generators ----------
l = np.zeros((8, 3, 3), complex)
l[0][0, 1] = l[0][1, 0] = 1
l[1][0, 1] = -1j; l[1][1, 0] = 1j
l[2][0, 0] = 1; l[2][1, 1] = -1
l[3][0, 2] = l[3][2, 0] = 1
l[4][0, 2] = -1j; l[4][2, 0] = 1j
l[5][1, 2] = l[5][2, 1] = 1
l[6][1, 2] = -1j; l[6][2, 1] = 1j
l[7] = np.diag([1, 1, -2]) / np.sqrt(3)
Tf = l / 2                                     # fundamental
Tbar = np.array([-t.T for t in Tf])            # antifundamental

f = np.zeros((8, 8, 8))
for a in range(8):
    for b in range(8):
        comm = Tf[a] @ Tf[b] - Tf[b] @ Tf[a]
        for c in range(8):
            f[a, b, c] = np.real(-2j * np.trace(comm @ Tf[c]))
Tadj = np.array([-1j * f[a] for a in range(8)])

def sym_power_basis(n):
    idx = [t for t in iproduct(range(3), repeat=n) if list(t) == sorted(t)]
    vecs = []
    for t in idx:
        v = np.zeros(3 ** n)
        from itertools import permutations as perms
        ps = set(perms(t))
        for p in ps:
            j = 0
            for x in p:
                j = j * 3 + x
            v[j] = 1.0
        vecs.append(v / np.linalg.norm(v))
    return np.array(vecs)

def sym_rep(n):
    S = sym_power_basis(n)
    reps = []
    for a in range(8):
        big = np.zeros((3 ** n, 3 ** n), complex)
        for k in range(n):
            term = np.array([[1.0]])
            for m in range(n):
                term = np.kron(term, Tf[a] if m == k else np.eye(3))
            big += term
        reps.append(S @ big @ S.T)
    return np.array(reps)

T6 = sym_rep(2)
T10 = sym_rep(3)

def dynkin(T):
    return float(np.real(np.mean([np.trace(T[a] @ T[a]) for a in range(8)])))

def dtensor(T):
    D = np.zeros((8, 8, 8))
    for a in range(8):
        for b in range(8):
            anti = T[b] @ T[a] + T[a] @ T[b]
            for c in range(8):
                D[a, b, c] = np.real(np.trace(T[c] @ anti))
    return D

# ---------- (i) the SU(3) data ----------
print("== (i) SU(3) representation data, computed from generators ==")
Df = dtensor(Tf)
nf2 = float((Df * Df).sum())
print("   rep    dim   T(R)      A(R)     ||D_R - A D_fund|| (propor-")
print("                                    tionality receipt)")
for name, T, dim in (("3", Tf, 3), ("3bar", Tbar, 3), ("8", Tadj, 8),
                     ("6", T6, 6), ("10", T10, 10)):
    TR = dynkin(T)
    DR = dtensor(T)
    A = float((DR * Df).sum() / nf2)
    res = np.abs(DR - A * Df).max()
    print(f"   {name:4s}   {dim:3d}   {TR:6.3f}   {A:+7.3f}    {res:.1e}")
print("  -> A(3) = 1, A(3bar) = -1, A(8) = 0, A(6) = +7, A(10) = +27;")
print("     T = 1/2, 1/2, 3, 5/2, 15/2 - COMPUTED, with every rep's cubic")
print("     tensor exactly proportional to the d-symbol: one number per")
print("     rep feeds the predicate.")

# ---------- (ii) SU(2): no cubic anomaly; Witten instead ----------
print("\n== (ii) SU(2): the cubic vanishes; Witten takes its place ==")
s = np.zeros((3, 2, 2), complex)
s[0] = [[0, 1], [1, 0]]; s[1] = [[0, -1j], [1j, 0]]; s[2] = [[1, 0], [0, -1]]
Tw = s / 2
D2 = np.zeros((3, 3, 3))
for a in range(3):
    for b in range(3):
        anti = Tw[a] @ Tw[b] + Tw[b] @ Tw[a]
        for c in range(3):
            D2[a, b, c] = np.real(np.trace(Tw[c] @ anti))
print(f"  ||d-tensor of SU(2)||_max = {np.abs(D2).max():.1e}  (IDENTICALLY"
      f" ZERO: no cubic predicate exists)")
print("  -> the SU(2) seam constraint is GLOBAL, not perturbative: the")
print("     Witten condition (pi_4(SU(2)) = Z_2, named import): the")
print("     number of Weyl doublets must be EVEN.")

# ---------- (iii) the stack, assembled ----------
print("\n== (iii) the Phase II predicate stack ==")
print("  SU(3)^3 / SU(3)^2-U(1) / SU(2)^2-U(1) / U(1)^3 / U(1)-grav /")
print("  WITTEN-even / Z_6-LATTICE (P17's quotient receipt, promoted to")
print("  a structural constraint).  Executed on the candidate space in")
print("  p18f.")
print("== p18e done ==")
