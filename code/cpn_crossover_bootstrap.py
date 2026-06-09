#!/usr/bin/env python3
"""
Checkable testbed: can the POSITIVITY bootstrap track a mass gap through the dimensional-transmutation
crossover?  2D O(N) sigma model at large N, where the gap is EXACTLY known, as the lab.

Large-N 2D O(N) lattice (action beta*sum_<xy> s_x.s_y, |s|^2=1):
  propagator 1/(phat^2+m^2), phat^2=sum_mu 4 sin^2(p_mu/2);
  gap equation  I(m^2):=int_BZ d^2p/(2pi)^2 1/(phat^2+m^2) = beta/N  =>  m ~ e^{-2 pi beta/N} (transmutation);
  axis 2-pt fn  G(r)=<s_0.s_r> ~ e^{-(gap) r}, with EXACT axis gap = 2 arcsinh(m/2)
  (nearest singularity of 1/sqrt(a(a+4)), a=4 sin^2(p/2)+m^2, at Im p = 2 arcsinh(m/2)).

BOOTSTRAP (positivity part): G(r)=int_0^{y0} y^r dnu(y), dnu>=0, y0=e^{-gap}: a Stieltjes moment
sequence. From 2K+2 moments, top of support obeys y0 >= lambda_max(H1,H0) (generalized eigenvalue),
  gap_est(K) = -log lambda_max(H1,H0),  H0=[G(i+j)], H1=[G(i+j+1)], i,j=0..K  (-> true gap as K->inf).
We feed EXACT G(r) (best case) to isolate the truncation/RESOLUTION limit. Question: at fixed K does
it track the gap through the crossover (m:O(1)->0), or does it need K ~ correlation length 1/gap?
"""
import numpy as np
import scipy.linalg as sla
from numpy.polynomial.legendre import leggauss

_pg, _pw = leggauss(3000)
_P = _pg * np.pi
_W = _pw * np.pi


def I_gap(m2):
    a = 4 * np.sin(_P / 2) ** 2 + m2
    b = a + 2.0
    return np.sum(_W / np.sqrt(b * b - 4.0)) / (2 * np.pi)


def G_axis(r, m2):
    a = 4 * np.sin(_P / 2) ** 2 + m2
    return np.sum(_W * np.cos(_P * r) / np.sqrt(a * (a + 4.0))) / (2 * np.pi)


def true_gap(m):
    return 2.0 * np.arcsinh(m / 2.0)                     # exact axis spectral threshold


def bootstrap_gap(m2, K, cond_cap=1e13):
    """gap_est = -log lambda_max(H1,H0); return (gest, cond, ok). Reports ill-conditioning gracefully."""
    G = np.array([G_axis(r, m2) for r in range(2 * K + 2)])
    H0 = np.array([[G[i + j] for j in range(K + 1)] for i in range(K + 1)])
    H1 = np.array([[G[i + j + 1] for j in range(K + 1)] for i in range(K + 1)])
    cond = np.linalg.cond(H0)
    if cond > cond_cap:
        return float("nan"), cond, False                  # double precision exhausted
    try:
        lam = sla.eigh(H1, H0, eigvals_only=True)
        return -np.log(lam[-1]), cond, True
    except Exception:
        return float("nan"), cond, False


def fmt(e, tg):
    return f"{e:7.4f} x{e/tg:5.2f}" if e == e else "  ill-cond  "


if __name__ == "__main__":
    print("=" * 86)
    print("Testbed: positivity bootstrap of the mass gap THROUGH the transmutation crossover")
    print("2D O(N) large-N (EXACT data). gap_est(K)->true gap as K->inf; fixed K = fixed resolution.")
    print("=" * 86 + "\n")

    print("(A) Fixed truncation K=5 across the strong->weak crossover (reach r<=11):")
    print("    beta/N   m_prop  true_gap   xi=1/gap   gap_est  ratio   cond(H0)")
    for m in (0.8, 0.4, 0.2, 0.1, 0.05, 0.02):
        m2 = m * m; tg = true_gap(m)
        e, c, ok = bootstrap_gap(m2, 5)
        r = f"x{e/tg:4.2f}" if ok else "  -- "
        print(f"    {I_gap(m2):6.3f}  {m:6.3f}  {tg:8.4f}  {1/tg:7.1f}   {fmt(e,tg):>12}  {r}  {c:.1e}")
    print("    => as xi grows past the reach (11), gap_est OVER-estimates (ratio rises) then fails:")
    print("       fixed K does NOT track the gap uniformly through the crossover.\n")

    print("(B) Convergence in K at a RESOLVABLE gap (m=0.3, xi=3.3):  reach >~ xi => converges")
    m = 0.3; m2 = m * m; tg = true_gap(m)
    for K in (1, 2, 3, 4, 5):
        e, c, ok = bootstrap_gap(m2, K)
        print(f"    K={K} (reach {2*K+1:2d}): gap_est={fmt(e,tg)}   cond={c:.1e}")
    print(f"    true gap = {tg:.4f}\n")

    print("(C) Same at a SMALL gap (m=0.03, xi=33): reach (<=2K+1) stays below xi => NOT resolved,")
    print("    and cond(H0) explodes (need exponentially growing precision too):")
    m = 0.03; m2 = m * m; tg = true_gap(m)
    for K in (1, 3, 5, 7, 9):
        e, c, ok = bootstrap_gap(m2, K)
        print(f"    K={K} (reach {2*K+1:2d}): gap_est={fmt(e,tg)}   cond={c:.1e}")
    print(f"    true gap = {tg:.4f}\n")

    print("VERDICT: even with EXACT moments, the positivity bootstrap resolves the gap only when its")
    print("reach (2K+1) >~ correlation length xi = 1/gap. Since the transmutation gap -> 0 as beta/N grows")
    print("(xi ~ e^{2 pi beta/N}), uniform-in-coupling control needs K ~ xi (exponentially many moments)")
    print("AND exponentially growing precision (Hankel cond ~ e^{cK}). No fixed-resource uniform control")
    print("through the crossover -- the SAME wall as 4D Step E, now demonstrated in a checkable lab.")
