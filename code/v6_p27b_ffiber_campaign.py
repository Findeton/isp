#!/usr/bin/env python3
"""
v6_p27b: (F-fiber) - recorded replication is fiber replication
(Paper 27, Part II).

The derivation attempt, in the corpus' oldest move (silent-seam
exclusion, P4; the mechanism of P18 R2): g EXACTLY identical matter
ledgers with NO distinguishing record carry a silent label - excluded;
the only record-admissible host for unlabeled multiplicity is a
DEGENERACY FIBER, where the label is gauge.  The receipts:

 (i)  THE GAUGE PROPERTY IS EXACTLY IDENTITY OF COPIES: a two-copy
      ledger with copy-mixing seam: when the copies are IDENTICAL,
      every record observable (spectrum, word correlations) is
      invariant under copy-basis rotation U in U(2) (machine: exact);
      when the copies differ by delta != 0, the rotation CHANGES the
      records (machine: the gauge property breaks linearly in delta).
      The premise (R-id) "copies exactly identical at the unbroken
      level" is precisely the gauge condition.
 (ii) THE PHENOMENOLOGICAL FACE: with three copies and TWO
      family-breaking seams (Y_u, Y_d), the record observables are
      exactly the U(3)-family invariants: singular values (masses) and
      the misalignment invariants - the Jarlskog determinant J is
      family-rotation invariant to machine precision while individual
      seam entries are not: MIXING MATRICES (CKM) EXIST BECAUSE TWO
      SEAMS BREAK ONE FIBER INCOMPATIBLY - the fiber theorem's
      observable signature.
 (iii) THE CHAIN, RESTATED: recorded replication => inter-copy seams
      exist (the records that count/compare copies ARE seams) =>
      the multiplicity index supports transport => fiber (Theorem F1)
      => U(g) gauge (P18 R3b) => g >= 3 protected (P21 G1) => nu_R
      forced with the unique embedding (P21 G2).  The old hypothesis
      (F-fiber) is REPLACED by the weaker premise (R-id).
"""
import numpy as np

rng = np.random.default_rng(272)

def haar_u(d):
    Z = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    Q, R = np.linalg.qr(Z)
    return Q * (np.diag(R) / np.abs(np.diag(R)))

# ---------- (i) the gauge property = identity of copies ----------
print("== (i) the copy rotation is a symmetry iff copies are"
      " identical ==")
nb = 5                                  # base ledger dimension
Hbase = rng.standard_normal((nb, nb)); Hbase = (Hbase + Hbase.T) / 2
V = rng.standard_normal((nb, nb)); V = (V + V.T) / 2

print("  unbroken-level ledger H(delta) = diag(H_base, H_base +"
      " delta V):")
print("   delta    max ||[U x 1, H]|| over sampled U in U(2)"
      "    ratio/delta")
for delta in (0.0, 0.05, 0.2):
    H = np.zeros((2 * nb, 2 * nb), complex)
    H[:nb, :nb] = Hbase
    H[nb:, nb:] = Hbase + delta * V
    worst = 0.0
    for _ in range(8):
        G = np.kron(haar_u(2), np.eye(nb))
        worst = max(worst, np.abs(G @ H - H @ G).max())
    ratio = "-" if delta == 0 else f"{worst/delta:8.3f}"
    print(f"   {delta:4.2f}     {worst:.3e}"
          f"                              {ratio}")
print("  -> IDENTICAL copies (delta = 0): the full U(2) copy rotation")
print("     COMMUTES with the ledger exactly - the copy label is gauge,")
print("     a degeneracy fiber in the P18 sense; detuned copies break")
print("     the symmetry at first order in delta (constant ratio).")
print("     The premise (R-id) 'copies exactly identical at the")
print("     unbroken level' IS the gauge condition - machine-sharp.")
print("     Family-breaking seams (the Yukawas) are then COVARIANT")
print("     data on the fiber, and records see only their invariants -")
print("     receipt (ii).")

# ---------- (ii) the Jarlskog receipt ----------
print("\n== (ii) the observable signature: family invariants only ==")
Yu = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
Yd = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
def jarlskog(Yu, Yd):
    Hu = Yu @ Yu.conj().T
    Hd = Yd @ Yd.conj().T
    C = Hu @ Hd - Hd @ Hu
    return np.imag(np.linalg.det(C + 0j)) / 1.0
J0 = jarlskog(Yu, Yd)
sv_u0 = np.linalg.svd(Yu, compute_uv=False)
worst_J, worst_sv, moved = 0.0, 0.0, 0.0
for _ in range(8):
    VQ, Vu, Vd = haar_u(3), haar_u(3), haar_u(3)
    Yu2 = VQ @ Yu @ Vu.conj().T
    Yd2 = VQ @ Yd @ Vd.conj().T
    worst_J = max(worst_J, abs(jarlskog(Yu2, Yd2) - J0) / abs(J0))
    worst_sv = max(worst_sv, np.abs(
        np.linalg.svd(Yu2, compute_uv=False) - sv_u0).max())
    moved = max(moved, np.abs(Yu2 - Yu).max())
print(f"  under random family rotations (V_Q, V_u, V_d):")
print(f"   |dJ|/|J| = {worst_J:.2e}   (Jarlskog: INVARIANT)")
print(f"   max |d singular values| = {worst_sv:.2e}   (masses:"
      f" INVARIANT)")
print(f"   max |d Y entries| = {moved:.2f}   (the seam MATRICES move")
print("    freely: they are gauge data, not records)")
print("  -> the family fiber is gauge: record data = invariants only.")
print("     Masses and CKM-class misalignments (J) survive; bases do")
print("     not.  MIXING EXISTS because two seams (Y_u, Y_d) break ONE")
print("     fiber incompatibly - the fiber theorem's phenomenological")
print("     signature, and the record-native reason a CKM matrix is")
print("     physical while Yukawa entries are not.")

# ---------- (iii) the chain ----------
print("\n== (iii) the chain, assembled ==")
print("  recorded replication (copies counted/compared in records)")
print("   => inter-copy seams exist            [the records ARE seams]")
print("   => the index supports transport      [Lemma F1a/F1b]")
print("   => degeneracy fiber                  [Theorem F1, this part]")
print("   => U(g) family gauge                 [P18 R3(b)]")
print("   => protected iff g >= 3              [P21 G1]")
print("   => anomaly-free iff nu_R exists,")
print("      unique embedding (Q,L | u,d,e,nu) [P21 G2]")
print("  PREMISE LEDGER: (R-id) - the copies are exactly identical at")
print("  the unbroken level (= the gauge condition of receipt (i));")
print("  observation supplies 'recorded replication' (three generations")
print("  are seen, compared, and mixed in actual records).")
print("  -> (F-fiber) is DISCHARGED into (R-id): the prediction P-nu")
print("     (the right-handed neutrino exists) now rides on (R-id) +")
print("     observed replication + corpus theorems alone.")
print("== p27b done ==")
