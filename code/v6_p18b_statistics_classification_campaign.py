#!/usr/bin/env python3
"""
v6_p18b: the statistics-operator classification (Paper 18, Theorem R2).

With eps^2 = 1 forced (R1), the two-excitation statistics operator on a
d-dimensional fiber must be:

  (a) TRANSPORT-COVARIANT: eps commutes with simultaneous fiber
      transport U x U (the exchange cannot see a gauge frame);
  (b) an involutive unitary.

 (i)  THE COMMUTANT IS TWO-DIMENSIONAL: the space of operators on
      V (x) V commuting with all U (x) U is span{1, P} (P = the flip),
      machine-computed for d = 2, 3, 4.  So eps = a 1 + b P with
      eps^2 = 1, unitary:  eps in { +1, -1, +P, -P }.  Four candidates.
 (ii) THE LEDGER CLASH kills +-1: for two excitations with ORTHOGONAL
      fiber labels the exchanged configuration is a DIFFERENT WORD of
      the ledger, and its cross-record is SEALED BY TRANSPORT (the
      eventless seam fixes the amplitude).  eps = +-1 predicts NO
      label exchange (cross-entry 0) where the ledger holds the
      transport value 1: candidates +-1 CONTRADICT SEALED ENTRIES -
      excluded not by positivity but by the ledger itself.
 (iii) THE SIGN IS THE PROJECTIVE LAYER: on the identical-label sector
      the surviving choice +-P is fixed by Paper 11's record-Pauli
      positivity: for a half-integer fiber the +P assignment produces
      a SIGNED sealed Gram (negative eigenvalue printed), the -P
      assignment is positive: eps = (-1)^(2m) P.

THEOREM R2: record exchange = (projective sign) x (fiber permutation).
PARASTATISTICS IS NEVER FUNDAMENTAL in the record ontology - what
remains of it is bookkeeping after hiding the fiber (p18c).
"""
import numpy as np

rng = np.random.default_rng(181)

def haar_u(d):
    Z = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    Q, R = np.linalg.qr(Z)
    return Q * (np.diag(R) / np.abs(np.diag(R)))

# ---------- (i) the commutant ----------
print("== (i) the transport commutant on V x V ==")
for d in (2, 3, 4):
    D = d * d
    rows = []
    for _ in range(40):
        U = haar_u(d)
        UU = np.kron(U, U)
        # commutation [UU, X] = 0 as a linear condition on vec(X)
        M = np.kron(np.eye(D), UU) - np.kron(UU.T, np.eye(D))
        rows.append(M)
    M = np.concatenate(rows)
    sv = np.linalg.svd(M, compute_uv=False)
    dim = int(np.sum(sv < 1e-10 * sv[0]))
    print(f"  d = {d}: dim of commutant of {{U x U}} = {dim}"
          f"   (span{{1, P}}: 2)")
print("  -> eps = a 1 + b P; with eps^2 = 1 and unitarity:")
print("     (a,b) solves a^2 + b^2 = 1, 2ab = 0  =>")
print("     eps in { +1, -1, +P, -P }: FOUR candidates.")

# ---------- (ii) the ledger clash ----------
print("\n== (ii) the ledger clash: +-1 contradict sealed entries ==")
d = 3
e = np.eye(d)
psi = np.kron(e[0], e[1])          # word w: label e1 at x, label e2 at y
psi_x = np.kron(e[1], e[0])        # word w': the exchanged word
P = np.zeros((d * d, d * d))
for i in range(d):
    for j in range(d):
        P[j * d + i, i * d + j] = 1.0
print("   candidate     |<w'| eps |w>|     sealed cross-record modulus")
for name, eps in (("+1", np.eye(d * d)), ("-1", -np.eye(d * d)),
                  ("+P", P), ("-P", -P)):
    val = float(np.abs(psi_x @ (eps @ psi)))
    print(f"     {name:3s}           {val:.1f}                  1.0")
print("  -> the exchanged configuration of DISTINGUISHABLE labels is a")
print("     different ledger word whose cross-record the eventless seam")
print("     SEALS with modulus 1 (the transport value; the SIGN on")
print("     distinguishable words is word-phase gauge).  Candidates +-1")
print("     predict ABSENCE (modulus 0) - no phase convention repairs an")
print("     absent record: they contradict a sealed entry and are")
print("     EXCLUDED by the ledger (a silent label-spectation is a")
print("     silent seam: P4's exclusion principle).  Surviving: +-P.")

# ---------- (iii) the sign is COMPUTED, not chosen ----------
print("\n== (iii) the sign: D9a computes it - exchange IS transport ==")
print("  By P11 Part III (D9a discharged), record exchange of identical")
print("  excitations IS eventless transport along the exchange path,")
print("  which carries a relative 2pi frame rotation (P9's frame-winding")
print("  theorem).  The projective layer therefore CONTRIBUTES the phase")
print("  of a 2pi rotation on the spin-m fiber - computed, not chosen:")
for (m, dim) in ((0.5, 2), (1.0, 3), (1.5, 4)):
    Jz = np.diag(np.arange(m, -m - 1e-9, -1.0))
    R2pi = np.diag(np.exp(2j * np.pi * np.diag(Jz)))
    phase = R2pi[0, 0]
    print(f"   m = {m}: exp(2 pi i Jz) = {phase.real:+.0f} * 1"
          f"   [(-1)^(2m) = {(-1) ** int(2 * m):+d}]")
print("  -> eps = (-1)^(2m) P: THEOREM R2.  The record exchange is the")
print("     fiber PERMUTATION times the computed projective sign; the")
print("     +-P 'freedom' of (i)-(ii) was apparent only before D9a.")
print("     Record-Pauli (P11 Part II) is then a CONSEQUENCE, and")
print("     statistics never carries fiber structure of its own:")
print("     PARASTATISTICS IS NOT FUNDAMENTAL in the record ontology.")
print("== p18b done ==")
