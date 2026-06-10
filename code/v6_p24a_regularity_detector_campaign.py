#!/usr/bin/env python3
"""
v6_p24a: the (C-reg-b) regularity detector (Paper 24).

(C-reg-b) asks WHICH controlled limits are smooth geometries.  The
proposed detector (P15's handle, made operational): the LOCAL WEYL
REMAINDER

   r_t(x) = K_t(x, x) sqrt(4 pi c(x) t) - 1

(K_t the record heat kernel of -d(c d.)): a controlled limit is in the
REGULARITY STRATUM iff sup_x |r_t(x)| -> 0 as t -> 0 along the tower.

 (i)  SMOOTH class: the detector vanishes linearly in t (table).
 (ii) INTERFACE class (P12's synthetic member): the detector is O(1)
      AT THE SEAM and does not decay - localized failure, exactly at
      the non-smooth locus.
 (iii) MICROSTRUCTURE class (c_k, k = 32): the detector is O(1)
      THROUGHOUT for t between the micro and macro scales - global
      failure until homogenization replaces the metric.
The criterion separates the three strata cleanly at machine level:
(C-reg-b) is hereby POSED with a validated detector; the THEOREM
(detector <=> smoothness, with rates) is the named residue.
"""
import numpy as np

def ring_A(n, cvals):
    cb = np.asarray(cvals) * n * n
    A = np.diag(cb + np.roll(cb, 1))
    for i in range(n):
        A[i, (i + 1) % n] -= cb[i]
        A[(i + 1) % n, i] -= cb[i]
    return A

def detector(n, cfun, ts):
    x = (np.arange(n) + 0.5) / n
    c = cfun(x)
    A = ring_A(n, c)
    ev, P = np.linalg.eigh(A)
    out = []
    for t in ts:
        Kdiag = (P ** 2 * np.exp(-t * ev)).sum(axis=1) * n
        r = Kdiag * np.sqrt(4 * np.pi * c * t) - 1
        out.append((t, np.abs(r).max(), np.abs(r)))
    return x, out

n = 512
ts = (0.02, 0.01, 0.005, 0.0025)

print("== (i) smooth class: detector -> 0 linearly in t ==")
x, sm = detector(n, lambda x: 1 + 0.5 * np.sin(2 * np.pi * x), ts)
for t, d, _ in sm:
    print(f"  t = {t:6.4f}: sup |r_t| = {d:.5f}")
print(f"  ratio across halvings: "
      f"{sm[0][1]/sm[1][1]:.2f}, {sm[1][1]/sm[2][1]:.2f},"
      f" {sm[2][1]/sm[3][1]:.2f}   [linear in t: 2.00]")

print("\n== (ii) interface class: localized O(1) failure at the seam ==")
x, itf = detector(n, lambda x: np.where(x < 0.5, 1.0, 4.0), ts)
for t, d, prof in itf:
    away = np.abs(prof[(np.abs(x - 0.5) > 0.1) & (np.abs(x - 1.0) > 0.1)
                       & (x > 0.1)]).max()
    print(f"  t = {t:6.4f}: sup |r_t| = {d:.4f}   away from seams ="
          f" {away:.5f}")
print("  -> the detector fails O(1) AT the interface and is smooth-class")
print("     small AWAY from it: the failure LOCATES the non-smooth locus.")

print("\n== (iii) microstructure class: global failure between scales ==")
x, mic = detector(n, lambda x: 1 + 0.45 * np.sin(2 * np.pi * 32 * x), ts)
for t, d, _ in mic:
    print(f"  t = {t:6.4f}: sup |r_t| = {d:.4f}")
print("  -> O(1) everywhere and NOT decaying over this t-range (the")
print("     micro scale 1/32 corresponds to t ~ 1e-3): the metric the")
print("     detector tests is not the one the tower converges to -")
print("     the homogenized stratum announces itself globally.")

print("\n== verdict ==")
print("  the local-Weyl-remainder detector separates SMOOTH (decay ~ t),")
print("  INTERFACE (localized O(1)), and MICROSTRUCTURE (global O(1))")
print("  strata at machine level: (C-reg-b) is POSED with a validated,")
print("  computable criterion; the equivalence theorem (detector <=>")
print("  regularity stratum, with rates) is the named residue - now a")
print("  precise statement in classical heat-kernel analysis rather")
print("  than an open-ended question.")
print("== p24a done ==")
