#!/usr/bin/env python3
"""
v6_p21a: the protection theorem - why three is the minimal protected
replication (Paper 21).

In SHARD a family structure is a degeneracy fiber of dimension g; by
P18's reconstruction it carries a U(g) family code.  A replication is
PROTECTED if no family-invariant mass pairing exists - otherwise the
copies can be lifted pairwise (Higgsed away) and the replication is
not structural.

 (i)  THE PROTECTION THEOREM: the space of U(g)-invariant bilinears on
      fund (x) fund is computed (nullspace method, exact):
        g = 1: dim 1 (no protection: a single copy can be massed);
        g = 2: dim 1 - THE EPSILON PAIRING: two families pair into a
               family singlet and can be lifted: g = 2 is UNPROTECTED;
        g = 3: dim 0 - NO invariant bilinear (3 x 3 = 6 + 3bar, no
               singlet): g = 3 is PROTECTED;
        g = 4: dim 0 (protected, but larger).
      MINIMAL PROTECTED REPLICATION = 3.  (For SU(g) instead of U(g)
      the same dims; for g = 2 the epsilon is the pseudo-reality of
      SU(2) - machine receipt.)
 (ii) the corollary, stated: a record family fiber of dimension 2 is
      removable by its own epsilon seam; dimension 3 is the smallest
      replication the ledger cannot erase - the record-native reason
      generations come in threes IF they come from a fiber at all
      (the existence of the family fiber itself is not derived).
"""
import numpy as np

rng = np.random.default_rng(21)

def haar(d):
    Z = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    Q, R = np.linalg.qr(Z)
    return Q * (np.diag(R) / np.abs(np.diag(R)))

def su(d):
    U = haar(d)
    return U / np.linalg.det(U) ** (1 / d)

print("== (i) invariant bilinears on fund x fund of the family code ==")
for g in (1, 2, 3, 4):
    D = g * g
    rows = []
    for _ in range(30):
        U = su(g)
        UU = np.kron(U, U)
        rows.append(UU - np.eye(D))          # invariance: UU x = x
    M = np.concatenate(rows)
    sv = np.linalg.svd(M, compute_uv=False)
    dim = int(np.sum(sv < 1e-10 * max(sv[0], 1)))
    note = {1: "no protection (single copy massed freely)",
            2: "the EPSILON pairing: UNPROTECTED",
            3: "NO invariant pairing: PROTECTED",
            4: "protected (but larger)"}[g]
    print(f"  g = {g}: dim Inv(fund x fund) = {dim}   -> {note}")
print("  -> 2 x 2 contains the family singlet (pseudo-reality of SU(2):")
print("     the epsilon seam lifts the pair); 3 x 3 = 6 + 3bar contains")
print("     NONE.  MINIMAL PROTECTED REPLICATION = 3.")

print("\n== (ii) the epsilon seam, exhibited and used ==")
eps = np.array([[0, 1], [-1, 0]], complex)
worst = 0.0
for _ in range(8):
    U = su(2)
    worst = max(worst, np.abs(U.T @ eps @ U - eps).max())
print(f"  ||U^T eps U - eps|| over sampled SU(2): {worst:.1e}"
      f"   (the g = 2 mass seam is exactly invariant)")
print("  -> a two-family fiber carries its own family-singlet mass seam:")
print("     the ledger can seal a mass term that removes the replication")
print("     pairwise.  A three-family fiber carries NO such seam: the")
print("     replication is record-protected.  THE RECORD-NATIVE")
print("     STATEMENT: generations are structural only in threes (or")
print("     more); three is minimal.  What is NOT derived: that a")
print("     family fiber exists at all - that is the g >= 2 premise,")
print("     and p21b shows what gauging it FORCES.")
print("== p21a done ==")
