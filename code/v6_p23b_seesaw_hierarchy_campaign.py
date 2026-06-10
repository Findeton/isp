#!/usr/bin/env python3
"""
v6_p23b: seesaw and the marginality-hierarchy mechanism (Paper 23).

 (i)  THE SEESAW IS STRUCTURAL: with p23a's theorem (the only bare
      mass is M nu^c nu^c) and P20's seams (Dirac masses = y v), the
      light neutrino masses are m_nu = (y v)^2 / M - machine spectrum
      with the suppression v/M printed: lightness is a CONSEQUENCE of
      the protection theorem, not a tuning.
 (ii) THE MARGINALITY-HIERARCHY MECHANISM: the corpus owns one small
      structural number - the single-relation marginality 3 kappa - 1
      = 0.0318 (P8/P10).  A Froggatt-Nielsen-type record charge ladder
      with THIS epsilon (generation charges 2, 1, 0 from the P21
      family structure) produces mass ratios 1 : eps : eps^2 per
      sector and mixing ~ sqrt(eps) - compared honestly against the
      observed fermion ladder at order-of-magnitude scope: a
      MECHANISM DEMO with the corpus' own small parameter, NOT a fit
      and NOT a derivation of the Yukawa textures.
"""
import numpy as np

rng = np.random.default_rng(23)

# ---------- (i) seesaw ----------
print("== (i) the structural seesaw ==")
v = 1.0
M = 1.0e6                                  # the one record-native scale
y = rng.uniform(0.3, 1.0, (3, 3)) * np.exp(2j * np.pi * rng.uniform(
    size=(3, 3)))
mD = y * v
MR = M * (np.eye(3) + 0.2 * rng.uniform(size=(3, 3)))
MR = (MR + MR.T) / 2
mnu = mD @ np.linalg.inv(MR) @ mD.T
sv_nu = np.linalg.svd(mnu, compute_uv=False)
sv_D = np.linalg.svd(mD, compute_uv=False)
print(f"  Dirac scale y v ~ {sv_D[0]:.3f};   Majorana scale M = {M:.0e}")
print(f"  light spectrum |m_nu| = "
      f"{', '.join(f'{x:.2e}' for x in sv_nu)}")
print(f"  suppression ~ (y v)^2 / M = {sv_D[0]**2/M:.2e}  - structural:")
print("  the protection theorem (p23a) gives nu^c the ONLY v-free mass,")
print("  so neutrino lightness is m ~ v^2/M with no tuning - the")
print("  observed pattern, from the record lattice's own selection.")

# ---------- (ii) the marginality ladder ----------
print("\n== (ii) the marginality-hierarchy mechanism ==")
eps = 0.0318                               # 3 kappa - 1 (P8/P10)
print(f"  the corpus' small number: eps = 3 kappa - 1 = {eps}")
print(f"  sqrt(eps) = {np.sqrt(eps):.4f}")
q = np.array([2, 1, 0])                    # FN record charges per gen
Mmat = np.array([[eps ** (q[i] + q[j]) for j in range(3)]
                 for i in range(3)])
base = rng.uniform(0.5, 1.5, (3, 3))
sv = np.linalg.svd(Mmat * base, compute_uv=False)
print(f"  ladder spectrum, charges (2,1,0) (O(1) x eps^(qi+qj)):")
print(f"   {sv[0]:.3f} : {sv[1]:.2e} : {sv[2]:.2e}"
      f"   (per-generation steps of eps^2 = {eps**2:.1e})")
print("  observed charged-fermion ladders (PDG, order of magnitude):")
print("   up sector:    m_u : m_c : m_t  ~  1.3e-5 : 7.4e-3 : 1")
print("   down sector:  m_d : m_s : m_b  ~  1.1e-3 : 2.2e-2 : 1")
print("   leptons:      m_e : m_mu: m_tau~  2.9e-4 : 5.9e-2 : 1")
print(f"  observed one-step suppressions: 7.4e-3 (u), 2.2e-2 (d),"
      f" 5.9e-2 (e)")
print(f"  the mechanism's rungs: eps^2 = {eps**2:.1e}, eps = {eps:.1e},")
print(f"  sqrt(eps) = {np.sqrt(eps):.3f} (Cabibbo-sized: lam_C = 0.225)")
print("  -> every observed inter-generation step sits BETWEEN eps^2 and")
print("     sqrt(eps): integer/half-integer record charges with O(1)")
print("     coefficients cover the entire observed ladder using the")
print("     corpus' ONE structural small number.  STATUS: a mechanism")
print("     demo at order-of-magnitude scope - the GRAIN of the")
print("     hierarchy matches eps_record = 0.0318; the textures (which")
print("     charges, which O(1)'s) are NOT derived, no fit is claimed.")
print("     Falsifiable form (P-eps, for Paper 25): all fermion")
print("     hierarchy steps are powers of eps_record in [eps^2,")
print("     sqrt(eps)] within O(1) - currently true of all nine.")
print("== p23b done ==")
