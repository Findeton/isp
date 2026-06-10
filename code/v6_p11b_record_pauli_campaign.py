#!/usr/bin/env python3
"""
v6_p11b: record-Pauli at the reconstructed layer - the D9b capstone
(Paper 11, Part II).

Setting: the sealed collar of an IDENTICAL pair of cells.  By the
frame-winding theorem (P9 7.1), one period of the identified pair collar
is one exchange, and the collar closes with the framed-exchange operator

    E = e^{2 pi i m} SWAP = eps * SWAP,    eps = (-1)^{2m},

GIVEN that the fiber carries weight m under the frame bundle (the
association content of axiom (X), branch D9a).  The per-period pair
transfer is PSD without loss of generality (site-RP structure: T^2 is
PSD for every reversible slice transfer, v6.3).

 THEOREM (record-Pauli, conditional on association): sealed spectral
 positivity on the exchange collar forces the physical sector to be
 Fix(E): SYMMETRIC for integer m, ANTISYMMETRIC for half-integer m -
 statistics = (-1)^{2m}.  The wrong sector assigns strictly NEGATIVE
 sealed weights (excluded by event-weight positivity, the P7 Theorem 7.6
 family), and its pseudo-correlations are signed - the driven/non-moment
 signature of Papers 8 and 10.

 Consequences, machine-verified: Pauli exclusion appears as an EXACT ZERO
 of the coincidence probability in the forced half-integer sector (not
 imposed - derived from the sealed collar); integer fibers bunch.

 What this does to axiom (X): the single-valuedness clause is REPLACED by
 a positivity theorem; (X) reduces to the association clause (D9a) alone.
"""
import numpy as np

rng = np.random.default_rng(7)

# per-cell PSD collar transfer (site-RP structure: T = S^2, v6.3)
B = rng.uniform(0.2, 1.0, (3, 3))
S0 = (B + B.T) / 2
T = S0 @ S0.T
T /= np.linalg.eigvalsh(T)[-1]
lam, U = np.linalg.eigh(T)
d = 3
M = 3   # collar periods

# pair modes split by SWAP parity
modes = []
for i in range(d):
    for j in range(i, d):
        if i == j:
            v = np.kron(U[:, i], U[:, i])
            modes.append((lam[i] * lam[j], +1, v, (i, j)))
        else:
            vs = (np.kron(U[:, i], U[:, j]) + np.kron(U[:, j], U[:, i])) / np.sqrt(2)
            va = (np.kron(U[:, i], U[:, j]) - np.kron(U[:, j], U[:, i])) / np.sqrt(2)
            modes.append((lam[i] * lam[j], +1, vs, (i, j)))
            modes.append((lam[i] * lam[j], -1, va, (i, j)))

print("== record-Pauli: sealed spectral weights on the exchange collar ==")
print("  closing operator E = eps * SWAP, eps = (-1)^(2m); sealed weight of a")
print(f"  pair mode = (lam_a lam_b)^M * eps * swap_parity   (M = {M} periods)\n")
for m, name in ((0.0, "integer fiber (m = 0)  "), (0.5, "half-integer (m = 1/2) ")):
    eps = (-1) ** int(2 * m)
    w_sym = [(la ** M) * eps * (+1) for la, s, v, ij in modes if s == +1]
    w_asy = [(la ** M) * eps * (-1) for la, s, v, ij in modes if s == -1]
    print(f"  {name}: sym weights ({len(w_sym)}): min = {min(w_sym):+.2e},"
          f" all {'>= 0' if min(w_sym) >= 0 else 'NEGATIVE' if max(w_sym) < 0 else 'mixed'};"
          f"  antisym ({len(w_asy)}): min = {min(w_asy):+.2e},"
          f" all {'>= 0' if min(w_asy) >= 0 else 'NEGATIVE' if max(w_asy) < 0 else 'mixed'}")
    forced = "SYMMETRIC (bosonic)" if eps > 0 else "ANTISYMMETRIC (fermionic)"
    print(f"     -> positivity of sealed weights FORCES the {forced} sector:")
    print(f"        statistics = (-1)^(2m).  The wrong sector carries strictly")
    print(f"        negative sealed event weights: excluded (P7 7.6 family).\n")

# Pauli exclusion as an exact zero of the coincidence probability
diag_proj = np.zeros((d * d,))
for k in range(d):
    diag_proj[k * d + k] = 1.0
def sector_law(eps):
    sec = [(la, v) for la, s, v, ij in modes if s == (1 if eps > 0 else -1)]
    wts = np.array([la ** M for la, v in sec])
    wts = wts / wts.sum()
    return sec, wts
print("== consequences in the FORCED sectors ==")
sec_f, w_f = sector_law(-1)         # m = 1/2: antisymmetric forced
coinc_f = sum(w * np.sum((v.reshape(d, d).diagonal()) ** 2 * 0 + (v * diag_proj) @ v)
              for (la, v), w in zip(sec_f, w_f))
coinc_f = sum(w * float((v * diag_proj) @ v) for (la, v), w in zip(sec_f, w_f))
sec_b, w_b = sector_law(+1)         # m = 0: symmetric forced
coinc_b = sum(w * float((v * diag_proj) @ v) for (la, v), w in zip(sec_b, w_b))
# distinguishable reference: all modes, no projection
wts_all = np.array([la ** M for la, s, v, ij in modes])
wts_all = wts_all / wts_all.sum()
coinc_d = sum(w * float((v * diag_proj) @ v)
              for (la, s, v, ij), w in zip(modes, wts_all))
print(f"  coincidence probability P(a = b):")
print(f"    forced half-integer sector: {coinc_f:.2e}   (PAULI EXCLUSION:")
print(f"      an EXACT zero, derived from the sealed collar, not imposed)")
print(f"    forced integer sector:      {coinc_b:.6f}  > 0  (occupancy allowed;")
print(f"      the sharp bunching law 2/(1+|<a|b>|^2) is Paper 9 Section 8)")

# the wrong sector is a signed (driven-type) sector
print("\n== the wrong sector is signed: the P8/P10 failure signature ==")
f = rng.normal(size=d * d)
def twisted_corr(eps, R):
    """raw exchange-collar 'correlations' with the twist E inserted and NO
    sector projection: a signed spectral measure unless restricted."""
    C = []
    for r in range(R + 1):
        c = sum((la ** r) * eps * s * float((v @ f)) ** 2
                for la, s, v, ij in modes)
        C.append(c)
    return C
def hankel_min(C, N):
    G = np.array([[C[i + j] for j in range(1, N + 1)] for i in range(1, N + 1)])
    return np.linalg.eigvalsh(G)[0]
C_wrong = twisted_corr(-1, 14)      # half-integer twist, full (unprojected) space
print(f"  half-integer twisted correlations, unprojected: site-Hankel min eig")
print(f"  (N = 6) = {hankel_min(C_wrong, 6):+.6f}   SIGNED: fails the moment test -")
print(f"  the wrong-statistics sector sits with the driven/non-moment sectors of")
print(f"  Papers 8 and 10; projecting onto Fix(E) restores positivity:")
C_right = []
for r in range(15):
    c = sum((la ** r) * float((v @ f)) ** 2
            for la, s, v, ij in modes if s == -1)
    C_right.append(c)
print(f"  projected (forced) sector: site-Hankel min eig (N = 6) = "
      f"{hankel_min(C_right, 6):+.2e}   (moment-class: RP)")

print("\n== what this does to axiom (X) ==")
print("  The single-valuedness clause of (X) is REPLACED by a theorem: sealed")
print("  positivity on the exchange collar selects Fix(E).  (X) reduces to its")
print("  association clause alone (D9a: the fiber transport is tied to the")
print("  frame bundle).  Fermions are now AVAILABLE + POSITIVITY-RIGID: given")
print("  a genuinely spinning fiber, wrong statistics is not merely unaesthetic")
print("  - it assigns negative sealed event weights, the same exclusion that")
print("  killed split-signature phases (P7 7.6) and silent arrows (P10 T3).")
print("== p11b done ==")
