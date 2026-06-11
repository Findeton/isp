#!/usr/bin/env python3
"""
v6_p26c: the pre-click metric - what fidelity misses (Paper 26,
Part III).

Two simulated processors at IDENTICAL average gate fidelity per cycle:
  A: coherent over-rotation by theta about Z each cycle (unitary - the
     environment forms NO record: Sigma_leak = 0);
  B: dephasing with lambda = sin^2(theta/2) (the environment records
     which-path evidence: Sigma_leak > 0).
Matched: F_avg = 1 - (2/3) sin^2(theta/2) = 1 - (2/3) lambda.

 (i)  after n cycles WITH a spin-echo recovery sequence (the standard
      recalibration resource), processor A returns the logical state
      at fidelity 1.0000 while processor B does not - the echo cannot
      recall evidence the environment already sealed;
 (ii) the pre-click metric (protected minus leaked logical nats)
      predicts B's loss through the Part-I law, while per-cycle
      fidelity is blind to the difference;
 (iii) the boundary term: the raw capacity side of the law imports the
      record area law (P13: capacity quanta) - stated, not re-derived.
"""
import numpy as np

theta = 0.2
lam = np.sin(theta / 2) ** 2
F_A = 1 - (2 / 3) * np.sin(theta / 2) ** 2
F_B = 1 - (2 / 3) * lam
print(f"== matched processors: F_avg(A) = {F_A:.6f}, F_avg(B) ="
      f" {F_B:.6f} ==")

Z = np.array([[1, 0], [0, -1]], complex)
X = np.array([[0, 1], [1, 0]], complex)
def U_rot(th):
    return np.array([[np.exp(-1j * th / 2), 0],
                     [0, np.exp(1j * th / 2)]])
rho0 = 0.5 * np.array([[1, 1], [1, 1]], complex)   # |+><+|

n = 100
# processor A: coherent Z-rotations, echo: X at half-time
rho = rho0.copy()
U = U_rot(theta)
for k in range(n // 2):
    rho = U @ rho @ U.conj().T
rho = X @ rho @ X
for k in range(n // 2):
    rho = U @ rho @ U.conj().T
rho = X @ rho @ X
F_A_final = float(np.real(np.trace(rho @ rho0)))

# processor B: dephasing channel, same echo schedule
rho = rho0.copy()
def dephase(r, l):
    return (1 - l) * r + l * (Z @ r @ Z)
for k in range(n // 2):
    rho = dephase(rho, lam)
rho = X @ rho @ X
for k in range(n // 2):
    rho = dephase(rho, lam)
rho = X @ rho @ X
F_B_final = float(np.real(np.trace(rho @ rho0)))

gam_pred = (1 - 2 * lam) ** n
F_B_pred = (1 + gam_pred) / 2
print(f"\n== (i) after n = {n} cycles, with spin echo ==")
print(f"  processor A (coherent, Sigma_leak = 0): recovered fidelity ="
      f" {F_A_final:.6f}")
print(f"  processor B (dephasing):                recovered fidelity ="
      f" {F_B_final:.6f}")
print(f"  Part-I prediction for B: (1 + (1-2 lam)^n)/2 = {F_B_pred:.6f}")
print("  -> SAME per-cycle fidelity; the echo recalls A's unitary error")
print("     EXACTLY and recalls NOTHING of B's: evidence already sealed")
print("     in the environment is not recallable by control pulses.")

print("\n== (ii) the metric ==")
# Sigma_leak per cycle for B: which-path evidence of the dephasing
# Kraus pair = binary monitor with BC = 1 - 2 lam
bcB = 1 - 2 * lam
sigB = -4 * np.log(bcB)            # quarter law inverted (small-leak)
print(f"  Sigma_leak/cycle: A = 0.000000;  B = {sigB:.6f} nats"
      f" (quarter-law equivalent)")
print(f"  pre-click capacity after {n} cycles (protected - leaked,")
print(f"  qubit = ln 2 = {np.log(2):.4f} nats):")
print(f"   A: {np.log(2):.4f} - 0 = {np.log(2):.4f}  (full)")
KB = max(np.log(2) - n * sigB / 4, 0.0)
print(f"   B: ln2 - n Sigma/4 = {KB:.4f}  (capacity exhausted)")
print("  -> the metric ORDERS the processors correctly where fidelity")
print("     cannot; 'Sigma_leak per logical cycle' is the record-native")
print("     hardware number.")

print("\n== (iii) the boundary term (stated) ==")
print("  K_pre <= min(boundary capacity, rate, channel capacity)")
print("           - Sigma_leak:")
print("  the boundary term is the RECORD AREA LAW (P13: capacity")
print("  extensive in the seam area, quanta with log-closing spacing);")
print("  rate (Margolus-Levitin) and channel capacity (Devetak) enter")
print("  as NAMED IMPORTS - per-term statuses, not a collage.")
print("== p26c done ==")
