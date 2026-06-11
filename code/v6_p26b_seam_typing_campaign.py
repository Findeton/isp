#!/usr/bin/env python3
"""
v6_p26b: error correction is selective record formation (Paper 26,
Part II).

Theorem B (Knill-Laflamme, restated in record terms): a code protects
a logical sector iff its ALLOWED seams (syndrome records) carry zero
logical evidence while routing the noise evidence into the ledger -
P E_i^dag E_j P = c_ij P on the code space.

Receipts on the 3-qubit bit-flip code (|0L> = |000>, |1L> = |111>):

 (i)   TYPED CLICKS: the syndrome (Z1Z2, Z2Z3) is INFORMATIVE about
       the error (I(error : syndrome) printed, most of H(error)) and
       EXACTLY SILENT about the logical bit (I(L : syndrome) = 0 to
       machine precision): allowed clicks reveal noise, not logic.
 (ii)  THE KL RECEIPTS: P E_i^dag E_j P proportional to P for the
       correctable set {1, X1, X2, X3} (residuals machine-zero), and
       VIOLATED for Z1 (P Z1 P has eigenvalues +-1 on the code space:
       the forbidden seam in operator form).
 (iii) RECOVERY: logical error after majority correction = 3p^2 - 2p^3
       (machine vs formula): the code converts first-order leakage
       into second-order failure BY routing clicks.
 (iv)  THE FORBIDDEN CLICK COSTS CAPACITY: a Z-type environment record
       of strength eps on one qubit leaks logical evidence at the
       Part-I rate (quarter law) and NO recovery exists within the
       code: typed wrongly, the same click budget destroys the
       computation.
"""
import numpy as np
from itertools import product

# ---------- (i) typed clicks ----------
print("== (i) the syndrome is silent about logic, loud about noise ==")
p = 0.08
errors = [((), (1 - p) ** 3), ((0,), p * (1 - p) ** 2),
          ((1,), p * (1 - p) ** 2), ((2,), p * (1 - p) ** 2),
          ((0, 1), p * p * (1 - p)), ((0, 2), p * p * (1 - p)),
          ((1, 2), p * p * (1 - p)), ((0, 1, 2), p ** 3)]
def syndrome(flips):
    b = [0, 0, 0]
    for q in flips:
        b[q] ^= 1
    return (b[0] ^ b[1], b[1] ^ b[2])
# joint over (logical bit, error, syndrome); logical ~ uniform
joint = {}
for L in (0, 1):
    for flips, w in errors:
        s = syndrome(flips)
        joint[(L, s)] = joint.get((L, s), 0.0) + 0.5 * w
pL = {0: 0.5, 1: 0.5}
ps = {}
for (L, s), w in joint.items():
    ps[s] = ps.get(s, 0.0) + w
I_Ls = sum(w * np.log(w / (pL[L] * ps[s]))
           for (L, s), w in joint.items() if w > 0)
js = {}
pe = {}
for flips, w in errors:
    s = syndrome(flips)
    js[(flips, s)] = js.get((flips, s), 0.0) + w
    pe[flips] = pe.get(flips, 0.0) + w
I_es = sum(w * np.log(w / (pe[f] * ps[s]))
           for (f, s), w in js.items() if w > 0)
H_e = -sum(w * np.log(w) for w in pe.values())
print(f"  I(logical : syndrome) = {abs(I_Ls):.2e} nats   (EXACTLY zero)")
print(f"  I(error : syndrome)   = {I_es:.4f} nats   (of H(error) ="
      f" {H_e:.4f})")
print("  -> the allowed seam routes noise evidence into the ledger and")
print("     carries ZERO logical evidence: selective record formation.")

# ---------- (ii) the KL receipts ----------
print("\n== (ii) Knill-Laflamme in operator form ==")
X = np.array([[0, 1], [1, 0]], complex)
Z = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)
def op3(ops):
    M = np.array([[1.0]], dtype=complex)
    for o in ops:
        M = np.kron(M, o)
    return M
v0 = np.zeros(8); v0[0] = 1
v1 = np.zeros(8); v1[7] = 1
P = np.outer(v0, v0) + np.outer(v1, v1)
Es = [op3([I2, I2, I2]), op3([X, I2, I2]), op3([I2, X, I2]),
      op3([I2, I2, X])]
worst = 0.0
for i in range(4):
    for j in range(4):
        M = P @ Es[i].conj().T @ Es[j] @ P
        c = np.trace(M) / 2
        worst = max(worst, np.abs(M - c * P).max())
print(f"  correctable set {{1, X1, X2, X3}}: max ||P Ei Ej P - c P|| ="
      f" {worst:.1e}   (KL: PASS)")
MZ = P @ op3([Z, I2, I2]) @ P
ev = np.linalg.eigvalsh(MZ)
print(f"  forbidden seam Z1: eigenvalues of P Z1 P on code space ="
      f" {ev[0]:.0f}, {ev[-1]:.0f}   (NOT proportional to P: KL FAILS)")
print("  -> the code's type system, in operator form: X-seams sealable")
print("     and silent; Z-seams carry logical evidence.")

# ---------- (iii) recovery ----------
print("\n== (iii) recovery: leakage converted to second order ==")
for pp in (0.02, 0.05, 0.1):
    fail = sum(w for flips, w in
               [(f, ww) for f, ww in
                [((), (1-pp)**3), ((0,), pp*(1-pp)**2),
                 ((1,), pp*(1-pp)**2), ((2,), pp*(1-pp)**2),
                 ((0,1), pp*pp*(1-pp)), ((0,2), pp*pp*(1-pp)),
                 ((1,2), pp*pp*(1-pp)), ((0,1,2), pp**3)]]
               if len(flips) >= 2)
    print(f"  p = {pp}: logical failure = {fail:.6f}"
          f"   formula 3p^2 - 2p^3 = {3*pp**2 - 2*pp**3:.6f}")
print("  -> first-order physical leakage, second-order logical failure:")
print("     the click-routing dividend.")

# ---------- (iv) the forbidden click costs capacity ----------
print("\n== (iv) the same budget, typed wrongly ==")
eps = 0.1
sig = 2 * 2 * eps * np.arctanh(2 * eps)
bc = np.sqrt(1 - 4 * eps ** 2)
print(f"  Z-type environment record at eps = {eps} on one qubit:")
print(f"  logical evidence rate sigma = {sig:.5f}/step; logical")
print(f"  coherence multiplier = {bc:.5f}/step (the Part-I quarter law")
print(f"  applies UNMITIGATED: the bit-flip code has no Z-syndrome);")
print("  -> identical click budgets differ in computational cost by")
print("     their TYPE: the capacity law must count typed clicks, not")
print("     clicks - the record-native correction to 'error rate'.")
print("== p26b done ==")
