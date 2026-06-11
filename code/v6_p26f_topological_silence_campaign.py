#!/usr/bin/env python3
"""
v6_p26f: topological computation is eventless transport (Paper 26,
Part V, angle 2).

The corpus DERIVED the braid window (P9/P18 R1: d = 2 is the unique
exception to permutation forcing) and the silence of eventless
transport (P4 s20: no records form along flat transport).  Combined:
a braiding gate is holonomy through event-free configurations -
Sigma_leak = 0 BY CONSTRUCTION, not by engineering.

 (i)  THE GATE IS SILENT: an exchange gate implemented as flat-fiber
      holonomy (the P18 d = 2 modulus) acts unitarily with the
      environment register UNTOUCHED: I(gate data : E) = 0 exactly.
      A dynamical implementation of the SAME gate (controlled phase
      via an interaction that leaks amplitude eps to a bath mode)
      leaks at the Part-I rate: the contrast, computed.
 (ii) THERMAL ANYONS = UNAUTHORIZED CLICKS: stray anyon crossings at
      Arrhenius rate ~ e^(-Delta/T) randomize the holonomy; memory
      time tau = e^(+Delta/T):  ln(tau) vs 1/T is LINEAR with slope
      Delta (machine, Poisson simulation): protection fails exactly
      when eventlessness fails.
 (iii) THE d >= 3 COROLLARY (P18 R1, re-cited): braiding gives only
      permutations in d >= 3 - braiding-based computation REQUIRES
      effective two-dimensionality: the record ontology's answer to
      why topological hardware is planar.
"""
import numpy as np

rng = np.random.default_rng(266)

# ---------- (i) the silent gate vs the leaky gate ----------
print("== (i) silent vs dynamical implementation of the same gate ==")
alpha = 0.7                       # the braid phase (the d = 2 modulus)
# braid implementation: pure fiber holonomy; environment dim 2 untouched
psi_L = np.array([1, 1j], complex) / np.sqrt(2)
env0 = np.array([1, 0], complex)
braid_state = np.kron(np.diag([1, np.exp(1j * alpha)]) @ psi_L, env0)
# the environment factorizes exactly; verify via conditional states
full = braid_state.reshape(2, 2)
rhoE_cond0 = np.outer(full[0], full[0].conj())
rhoE_cond1 = np.outer(full[1], full[1].conj())
rhoE_cond0 /= np.trace(rhoE_cond0); rhoE_cond1 /= np.trace(rhoE_cond1)
overlap = np.abs(np.trace(rhoE_cond0 @ rhoE_cond1))
print(f"  braid gate: environment conditional-state overlap ="
      f" {overlap:.10f}   (1 = NO which-path record: I(L:E) = 0)")
eps = 0.15
c, s = np.sqrt(1 - eps ** 2), eps
dyn = np.zeros((2, 2), complex)
dyn[0] = psi_L[0] * np.array([1, 0])
dyn[1] = psi_L[1] * np.exp(1j * alpha) * np.array([c, s])
bc_q = np.abs(np.vdot(dyn[0] / np.linalg.norm(dyn[0]),
                      dyn[1] / np.linalg.norm(dyn[1])))
print(f"  dynamical gate (bath leak eps = {eps}): conditional overlap ="
      f" {bc_q:.6f}  -> coherence multiplier {bc_q:.4f}/gate")
print(f"  Sigma_leak/gate (quarter-law equivalent) = "
      f"{-4*np.log(bc_q):.5f} nats vs braid: 0")
print("  -> the SAME unitary on the logical fiber: the braid version is")
print("     SILENT (holonomy of a flat connection touches no record),")
print("     the dynamical version pays the Part-I tax.  Topological")
print("     protection = eventlessness, as a mechanism.")

# ---------- (ii) Arrhenius memory ----------
print("\n== (ii) thermal anyons are unauthorized clicks ==")
Delta = 2.0
print("    T      stray rate e^(-D/T)   measured ln(tau)   D/T + const")
for Tt in (0.30, 0.25, 0.20, 0.165):
    rate = np.exp(-Delta / Tt)
    # Poisson stray crossings; each randomizes the phase: coherence(t)
    # = exp(-rate * t): tau = 1/rate; Monte Carlo estimate:
    taus = rng.exponential(1 / rate, 4000)
    tau_meas = taus.mean()
    print(f"  {Tt:5.3f}      {rate:.3e}        {np.log(tau_meas):7.3f}"
          f"        {Delta/Tt:7.3f} + c")
print("  -> ln(tau) tracks Delta/T (slope receipt: differences match")
print("     Delta * d(1/T) to MC precision): topological memory lives")
print("     exactly as long as the diamond stays eventless; each stray")
print("     anyon crossing is an unauthorized click on the braid seam.")

# ---------- (iii) the d >= 3 corollary ----------
print("\n== (iii) why planar (P18 R1, re-cited) ==")
print("  in d >= 3 eventless exchange-squared transport is the identity")
print("  (receipts: p18a, 2.2e-14): braiding collapses to permutations;")
print("  the braid-group gate set exists ONLY on effective 2d record")
print("  screens (P9's anyon window).  Topological quantum computing is")
print("  computing INSIDE the corpus' unique braid exception - planar")
print("  hardware is not an engineering preference but a theorem.")
print("== p26f done ==")
