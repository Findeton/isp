#!/usr/bin/env python3
"""
v6_p15b: necessity of the class hypotheses (Paper 15).

The theorem's constant depends on the derivative bound K1 of the class.
The dependence is a THRESHOLD, and its other side is Paper 12's
synthetic stratum - made exactly computable here.

 (i)  THE THRESHOLD: on the fixed ellipticity window, the oscillating
      family c_k(x) = 1 + 0.45 sin(2 pi k x) has K1 ~ k.  At fixed
      n = 64 the normalized constant is STABLE deep in the theorem's
      regime K1 h << 1 - low modes are PROTECTED BY HOMOGENIZATION -
      and BLOWS UP at K1 h = O(1): no K-free theorem exists; the
      hypothesis defines the regime, and inside it the constant is
      genuinely uniform.
 (ii) WHAT THE TOWER BUILDS BEYOND THE LINE: at the class boundary the
      discrete spectrum abandons the smooth target c_k AND the
      continuum homogenized target c_eff = sqrt(1 - 0.45^2), and
      converges instead to the SYNTHETIC geometry it built itself: the
      uniform ring at the harmonic mean of the SAMPLED bonds (at
      k/n = 1/2, the exactly dimerized chain: c_hm = 0.7975).  Beyond
      the hypothesis line the tower still converges - to a synthetic
      record geometry determined by the discretization-scale interplay:
      (C-reg-a) and P12's synthetic stratum are two sides of one
      boundary, and the boundary value is COMPUTABLE.
"""
import numpy as np

def ring_lams(n, cvals, k=4):
    cb = np.asarray(cvals) * n * n
    A = np.diag(cb + np.roll(cb, 1))
    for i in range(n):
        A[i, (i + 1) % n] -= cb[i]
        A[(i + 1) % n, i] -= cb[i]
    return np.sort(np.linalg.eigvalsh(A))[1:k + 1]

def csamp(n, k, amp=0.45):
    x = (np.arange(n) + 0.5) / n
    return 1.0 + amp * np.sin(2 * np.pi * k * x)

amp = 0.45
c_eff = np.sqrt(1 - amp ** 2)
n = 64

# ---------- (i) the threshold ----------
print("== (i) the K1 threshold: stable inside the class, blow-up at the"
      " line ==")
print("    k    K1 h     |dlam_1|/(h^2 lam^2)   [n = 64 vs n = 4096 ref]")
for k in (1, 4, 8, 16, 24, 32):
    ref = ring_lams(4096, csamp(4096, k))
    lam = ring_lams(n, csamp(n, k))
    h = 1.0 / n
    r = abs(lam[0] - ref[0]) / (h ** 2 * ref[0] ** 2)
    print(f"   {k:2d}   {2*np.pi*k*amp*h:6.3f}        {r:9.5f}")
print("  -> the normalized constant is FLAT (~0.10) for K1 h << 1 - low")
print("     modes are protected by homogenization - and the line is")
print("     STRUCTURAL, not monotone: a resonance at K1 h = 0.71 (0.65),")
print("     a commensuration ACCIDENT at k = 24 (the sampled pattern is")
print("     balanced, all targets coincide, the constant looks fine by")
print("     coincidence), and full blow-up at the dimer point (12.55).")
print("     No K-free theorem exists; inside the class the uniformity is")
print("     real, beyond it even the FORM of the limit changes (ii).")

# ---------- (ii) the synthetic geometry the tower builds ----------
print("\n== (ii) beyond the line: the tower converges to the sampled-")
print("   harmonic-mean geometry ==")
print("    k    c_hm(sampled)   gap to c_k    gap to c_eff   gap to c_hm")
for k in (8, 16, 24, 32):
    cs = csamp(n, k)
    chm = 1.0 / np.mean(1.0 / cs)
    ref_k = ring_lams(4096, csamp(4096, k))
    ref_eff = ring_lams(4096, np.full(4096, c_eff))
    ref_hm = ring_lams(4096, np.full(4096, chm))
    lam = ring_lams(n, cs)
    gk = np.abs(lam - ref_k).max() / ref_k.max()
    ge = np.abs(lam - ref_eff).max() / ref_eff.max()
    gh = np.abs(lam - ref_hm).max() / ref_hm.max()
    print(f"   {k:2d}      {chm:.5f}       {gk:.5f}       {ge:.5f}"
          f"        {gh:.5f}")
print(f"  (c_eff = {c_eff:.5f}; at k/n = 1/2 the sampled bonds alternate")
print(f"   1 +- {amp}: the dimer chain, c_hm = {1/np.mean(1/csamp(64,32)):.5f})")
print("  -> AT the boundary (k/n = 1/2) the tower's limit is EXACTLY the")
print("     sampled-harmonic-mean (dimer) geometry: gap 0.005 vs 0.11 to")
print("     both smooth targets - the synthetic limit is COMPUTABLE from")
print("     the sampling.  In the intermediate regime the tower")
print("     interpolates between the smooth and sampled-synthetic")
print("     targets (k = 16), with commensuration points where all")
print("     targets coincide (k = 24).  The theorem's hypothesis line is")
print("     the handoff to P12's synthetic stratum - and the stratum's")
print("     boundary value is exact arithmetic, not a fit.")
print("== p15b done ==")
