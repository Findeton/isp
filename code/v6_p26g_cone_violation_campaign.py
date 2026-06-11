#!/usr/bin/env python3
"""
v6_p26g: quantum advantage as cone violation (Paper 26, Part V,
angle 3).

Paper 16's separation: classical sealability = a finite POSITIVE
(cone) realization; some finite-rank processes have none.  Quantum
information has a rhyming structure: classical simulability of circuit
sampling is governed by quasi-probability NEGATIVITY (discrete-Wigner
negativity as the magic resource; simulation cost ~ (sum |W|)^2,
Pashayan-Wallman-Bartlett, named import).  The dictionary, receipted
on the qutrit:

 (i)  THE PHASE-SPACE CONE: the qutrit discrete-Wigner construction,
      SELF-VALIDATED (phase-point operators: hermitian, trace 1/d...,
      orthogonality, completeness - property receipts before use);
 (ii) STABILIZER = SEALABLE: every qutrit stabilizer state has
      NONNEGATIVE Wigner function (machine: nine states across three
      bases, min W >= -1e-15) - inside the cone: positively
      realizable: classically simulable (Gross' theorem, recovered
      as receipts);
 (iii) MAGIC = CONE VIOLATION: the maximal-magic ("strange") state has
      min W = -1/3 exactly; its negativity compounds multiplicatively
      over copies: total weight (sum |W|)^n: the PWB simulation cost
      grows exponentially in the number of cone-violating records;
 (iv) THE DICTIONARY: sealable sector (P16 cone) <-> nonnegative
      quasi-realization <-> efficient classical record model;
      advantage = computation whose intermediate record description
      VIOLATES every finite cone - the same boundary the clock test
      (Part IV) detects on streams.  Stated at conjecture level for
      the general law; receipted exactly on the qutrit hierarchy.
"""
import numpy as np

d = 3
om = np.exp(2j * np.pi / 3)
Xs = np.zeros((d, d), complex)
for j in range(d):
    Xs[(j + 1) % d, j] = 1
Zs = np.diag([om ** j for j in range(d)])
tau = om ** 2                       # tau = omega^(2^-1), 2^-1 = 2 mod 3

def D(a, b):
    return tau ** (a * b) * np.linalg.matrix_power(Xs, a) \
        @ np.linalg.matrix_power(Zs, b)

A = {}
for q in range(d):
    for p in range(d):
        M = np.zeros((d, d), complex)
        for a in range(d):
            for b in range(d):
                M += om ** (p * a - q * b) * D(a, b)
        A[(q, p)] = M / d

# ---------- (i) self-validation ----------
print("== (i) the phase-space construction, self-validated ==")
herm = max(np.abs(A[u] - A[u].conj().T).max() for u in A)
tr1 = max(abs(np.trace(A[u]) - 1) for u in A)
comp = np.abs(sum(A.values()) - d * np.eye(d)).max()
orth = 0.0
for u in A:
    for v in A:
        val = np.trace(A[u] @ A[v]) / d
        target = 1.0 if u == v else 0.0
        orth = max(orth, abs(val - target))
print(f"  hermiticity {herm:.1e}; trace-1 {tr1:.1e}; completeness"
      f" {comp:.1e}; orthogonality {orth:.1e}")
print("  -> the A_u are a valid qutrit phase-point frame (receipts")
print("     before use; conventions verified, not trusted).")

def W(psi):
    psi = psi / np.linalg.norm(psi)
    return np.array([[np.real(psi.conj() @ (A[(q, p)] @ psi)) / d
                      for p in range(d)] for q in range(d)])

# ---------- (ii) stabilizer states are in the cone ----------
print("\n== (ii) stabilizer states: nonnegative (sealable) ==")
F = np.array([[om ** (j * k) for k in range(d)] for j in range(d)]) \
    / np.sqrt(d)
stab = [np.eye(d)[:, j] for j in range(d)]
stab += [F[:, j] for j in range(d)]
stab += [np.diag([om ** (2 * j * j) for j in range(d)]) @ F[:, k]
         for j in (1,) for k in range(d)]
worst = min(W(s).min() for s in stab)
print(f"  {len(stab)} stabilizer states: min W = {worst:.2e}  (>= 0:")
print("  inside the cone - positive realization exists: classically")
print("  simulable; Gross' theorem as a receipt)")

# ---------- (iii) magic = cone violation ----------
print("\n== (iii) the magic state violates the cone ==")
strange = np.array([0, 1, -1], complex) / np.sqrt(2)
Wm = W(strange)
neg = np.abs(Wm).sum()
print(f"  strange state: min W = {Wm.min():.6f}  (= -1/3 exactly)")
print(f"  total quasi-weight sum|W| = {neg:.6f}  (> 1: cone violation)")
print("   copies n:  1        2        4        8")
print("   (sum|W|)^2n cost factor: "
      + "  ".join(f"{neg**(2*n):.3f}" for n in (1, 2, 4, 8)))
print("  -> negativity compounds multiplicatively: the PWB simulation")
print("     cost (named import) is exponential in the number of")
print("     cone-violating records injected - magic counts UNSEALABLE")
print("     ledger entries.")

# ---------- (iv) the dictionary ----------
print("\n== (iv) the dictionary ==")
print("   P16 (processes)            quantum computing")
print("   sealable = finite cone     stabilizer sector: W >= 0,")
print("                              efficient classical record model")
print("   non-sealable (clock)       magic sector: W < 0, cost ~")
print("                              exp(cone violation)")
print("   Hankel/moment test         negativity witness / Part-IV")
print("                              clock test on streams")
print("  CONJECTURE (advantage = non-sealability): a computation")
print("  resists classical simulation exactly to the extent that its")
print("  intermediate record description admits no finite positive")
print("  realization - receipted here on the qutrit hierarchy, stated")
print("  at conjecture level in general.")
print("== p26g done ==")
