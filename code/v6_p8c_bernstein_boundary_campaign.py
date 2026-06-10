#!/usr/bin/env python3
"""
v6_p8c: mapping the boundary of the Bernstein class (Paper 8, item 3).

Gaussian record sector with collar correlation sequence C(r).  SITE
reflection through the origin makes the OS cross-block the Hankel matrix
G_{ij} = C(i+j); BOND reflection (through the bond between sites 0 and 1)
makes it G_{ij} = C(i+j-1), i,j = 1..N.

  T1 (typed sufficiency): C(r) = int lambda^r dnu(lambda), nu >= 0:
      support in [-1,1]  ==>  SITE-RP at every N (Gram, v_i = lambda^i);
      support in [0,1]   ==>  SITE- and BOND-RP at every N
      (the bond Gram needs lambda dnu >= 0).
  T2 (converses, imported classical machinery):
      site-RP at all N = Hankel PSD of the shifted sequence m_k = C(k+2);
      by HAMBURGER's theorem m has a representing positive measure, and
      |C(r)| <= C(0) (Cauchy-Schwarz for covariances) forces support into
      [-1,1].  Site reflection pins C(r) for r >= 2 ONLY (index-shift
      caveat, machine demo below).
      site+bond RP at all N is exactly the STIELTJES pair for
      m_k = C(k+1): representing measure on [0,1].  The Bernstein/
      completely-monotone class of v6.4 is EXACTLY the two-reflection
      class; the site-only class is strictly larger (alternating /
      antiferromagnetic sectors: site-RP, bond-FAILS - the lattice
      antiferromagnet phenomenon of Frohlich-Israel-Lieb-Simon).

Physical sectors tested: lattice massive free field (1d exact, 3d line
restriction), Yukawa, power law, alternating, damped-oscillating (RKKY-
type) - with the failure boundary N*(k) and eps*(N) mapped.
"""
import numpy as np

def hankel_min_eig(C, N):
    G = np.array([[C[i + j] for j in range(1, N + 1)] for i in range(1, N + 1)])
    return np.linalg.eigvalsh(G)[0]

def bond_min_eig(C, N):
    G = np.array([[C[i + j - 1] for j in range(1, N + 1)] for i in range(1, N + 1)])
    return np.linalg.eigvalsh(G)[0]

def first_failure(C, Nmax, tol=-1e-10):
    for N in range(1, Nmax + 1):
        if hankel_min_eig(C, N) < tol:
            return N
    return None

R = 200  # sequence length

print("== A. typed sufficiency (T1): mixtures of lambda^r, by support ==")
rng = np.random.default_rng(3)
worst_site = 0.0
worst_bond_signed = 1.0
worst_bond_pos = 0.0
for trial in range(200):
    k = rng.integers(1, 6)
    lams = rng.uniform(-0.95, 0.95, size=k)
    wts = rng.uniform(0.1, 1.0, size=k)
    C = [float(np.sum(wts * lams**r)) for r in range(2 * R + 2)]
    worst_site = min(worst_site, hankel_min_eig(C, 40) / abs(C[2]))
    worst_bond_signed = min(worst_bond_signed, bond_min_eig(C, 40) / abs(C[2]))
    lp = np.abs(lams)
    Cp = [float(np.sum(wts * lp**r)) for r in range(2 * R + 2)]
    worst_bond_pos = min(worst_bond_pos, bond_min_eig(Cp, 40) / abs(Cp[2]))
print(f"  200 random positive mixtures, nu on [-0.95,0.95], N=40:")
print(f"    SITE cross-block worst normalized min eig = {worst_site:.2e}  (theorem: >= 0)")
print(f"    BOND cross-block worst = {worst_bond_signed:.2e}"
      f"  (signed support: bond-RP NOT guaranteed)")
print(f"  same mixtures folded to nu on [0,0.95]: BOND worst = {worst_bond_pos:.2e}"
      f"  (theorem: >= 0)")

print("\n== A2. converses (T2) and the reflection typing ==")
# alternating: site-RP, bond-FAILS with the predicted rank-1 form
C_alt0 = [(-0.6) ** r for r in range(2 * R + 2)]
u2 = sum(0.36 ** i for i in range(24))
print(f"  alternating (-0.6)^r:  site min eig(N=24) = {hankel_min_eig(C_alt0, 24):.2e}"
      f"   bond min eig(N=24) = {bond_min_eig(C_alt0, 24):.4f}")
print(f"    bond block = -0.6 u u^T (rank one): predicted min eig = "
      f"{-0.6 * u2:.4f}   (SITE-ONLY: Hamburger class, not Stieltjes)")
C_geo = [0.5 ** r for r in range(2 * R + 2)]
print(f"  geometric 0.5^r:       site min eig(N=24) = {hankel_min_eig(C_geo, 24):.2e}"
      f"   bond min eig(N=24) = {bond_min_eig(C_geo, 24):.2e}   (BOTH: Stieltjes)")
# index-shift demo: site reflection is blind to C(0), C(1)
C_shift = [1.0, -5.0] + [0.6 ** r for r in range(2, 2 * R + 2)]
print(f"  index-shift demo C(1) = -5, C(r>=2) = 0.6^r:")
print(f"    site min eig(N=24) = {hankel_min_eig(C_shift, 24):.2e}  (PASSES at all N:")
print(f"    the site cross-block never sees r < 2); bond min eig(N=1) = "
      f"{bond_min_eig(C_shift, 1):.1f}  (FAILS instantly)")
print("  -> the moment structure is pinned only from the reflection plane")
print("     outward: site-RP at all N <=> (C(r))_{r>=2} is a bounded Hamburger")
print("     moment sequence (support [-1,1]); site+bond at all N <=> Stieltjes")
print("     (support [0,1]) for r >= 1: v6.4's Bernstein class is EXACTLY the")
print("     two-reflection class, and the site-only class is strictly larger.")

print("\n== B. physical sectors ==")
# 1d lattice massive free field: C(r) = lam^r exactly
for m2 in (0.1, 1.0):
    lam = ((2 + m2) - np.sqrt((2 + m2)**2 - 4)) / 2
    C = [lam**r for r in range(2 * R + 2)]
    print(f"  1d massive free field m^2={m2}: C(r) = {lam:.6f}^r,"
          f" min eig(N=40) = {hankel_min_eig(C, 40):.2e}   RP-ALL-N (exact geometric)")
# 3d massive lattice free field restricted to a line (FFT)
L = 64
k = 2 * np.pi * np.fft.fftfreq(L)
KX, KY, KZ = np.meshgrid(k, k, k, indexing="ij")
for m2 in (0.5,):
    denom = m2 + 2 * (3 - np.cos(KX) - np.cos(KY) - np.cos(KZ))
    Cfull = np.fft.ifftn(1.0 / denom).real
    Cline = Cfull[:, 0, 0]
    C = [Cline[r % L] for r in range(0, 2 * 21 + 2)]
    me = hankel_min_eig(C, 20) / C[2]
    print(f"  3d massive lattice field (L={L}, m^2={m2}), line restriction:"
          f" normalized min eig(N=20) = {me:.2e}   {'RP' if me > -1e-9 else 'FAILS'}")
# Yukawa and power law
C_yuk = [np.exp(-0.4 * r) / (1 + r) for r in range(2 * R + 2)]
C_pow = [(1 + r) ** -1.5 for r in range(2 * R + 2)]
print(f"  Yukawa e^(-0.4 r)/(1+r):      min eig(N=40) = {hankel_min_eig(C_yuk, 40):.2e}   RP (CM)")
print(f"  power law (1+r)^-1.5:         min eig(N=40) = {hankel_min_eig(C_pow, 40):.2e}   RP (CM)")
# alternating (antiferromagnetic-compatible)
C_alt = [(-0.6) ** r for r in range(2 * R + 2)]
print(f"  alternating (-0.6)^r:         min eig(N=40) = {hankel_min_eig(C_alt, 40):.2e}"
      f"   SITE-RP (bond fails: Hamburger-only, see A2)")
# damped oscillation - fails
C_osc = [np.exp(-0.2 * r) * np.cos(1.1 * r) for r in range(2 * R + 2)]
print(f"  e^(-0.2 r) cos(1.1 r):        min eig(N=6)  = {hankel_min_eig(C_osc, 6):.4f}   FAILS"
      f" (first failure at N = {first_failure(C_osc, 40)})")
# RKKY-type
C_rkky = [np.cos(1.2 * r) / (1 + r) ** 3 for r in range(2 * R + 2)]
print(f"  RKKY cos(1.2 r)/(1+r)^3:      first failure at N = {first_failure(C_rkky, 60)}")

print("\n== C. boundary map 1: the pure-oscillation ray exits the cone at N = 2 ==")
# exact identity: for C(r) = e^{-ar} cos(kr),
#   C2 C4 - C3^2 = e^{-6a} * (cos 2k - 1)/2  < 0  for every k in (0, pi):
print("   k     N*(first failure)   2x2 det identity (cos2k-1)/2")
for kk in (0.05, 0.1, 0.4, 0.8, 1.6, 2.4, 3.0, 3.09):
    C = [np.exp(-0.2 * r) * np.cos(kk * r) for r in range(20)]
    nf = first_failure(C, 10)
    det2 = C[2] * C[4] - C[3] ** 2
    ident = np.exp(-0.2 * 6) * (np.cos(2 * kk) - 1) / 2
    print(f"  {kk:5.2f}      {nf}                {det2:+.6f} = {ident:+.6f}")
print("  -> EVERY pure damped oscillation (k not in {0,pi}) fails reflection positivity")
print("     already at N=2, by the exact identity C2 C4 - C3^2 = e^-6a (cos2k-1)/2 < 0:")
print("     the moment-class boundary is razor sharp and certified at size 2.")

print("\n== D. boundary map 2: critical mixing eps*(N) from an INTERIOR moment point ==")
# base: continuous mixture C0(r) = int_0^0.9 lam^r dlam / 0.9 (strictly PD Hankel);
# perturbation: e^{-0.1 r} cos(0.7 r) (non-moment).  eps*(N) = largest RP mixing.
def Cmix(eps):
    return [(1 - eps) * (0.9 ** (r + 1) / (0.9 * (r + 1))) +
            eps * np.exp(-0.1 * r) * np.cos(0.7 * r) for r in range(2 * 81 + 2)]
print("   N     eps*(N)")
eps_vals = []
for N in (2, 4, 6, 8, 12, 16, 24, 32, 48, 64):
    lo, hi = 0.0, 1.0
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if hankel_min_eig(Cmix(mid), N) < -1e-13:
            hi = mid
        else:
            lo = mid
    eps_vals.append((N, 0.5 * (lo + hi)))
    print(f"  {N:4d}   {0.5*(lo+hi):.6f}")
print("  -> eps*(N) decreases monotonically toward the all-N boundary: the")
print("     finite-size margin of a non-moment admixture is computable per model,")
print("     and the all-N-stable SITE class is exactly the shifted Hamburger")
print("     moment class (converse: A2).")

print("\n== E. per-model certificate demo ==")
def certificate(C, N):
    me = hankel_min_eig(C, N)
    return me, ("RP-AT-SIZE" if me >= -1e-12 else "RP-FAILS")
for name, C in [("massive 1d (m^2=1)", [(((3) - np.sqrt(5)) / 2) ** r for r in range(200)]),
                ("RKKY k=1.2", C_rkky),
                ("alternating", C_alt)]:
    me, verdict = certificate(C, 24)
    print(f"  {name:22s} N=24: min eig = {me:+.3e}  {verdict}")
print("== p8c done ==")
