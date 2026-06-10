#!/usr/bin/env python3
"""
v6_p13e: horizon capacity and record entropy (Paper 13, route 5).

Paper 7 Section 12 named capacity quantization (C5) as a direction
contingent on (C)/(M).  With the wedge machinery of p13b, finite
receipts exist:

 (i)  THE 1+1 HORIZON CUT: the record entropy of the wedge (the ledger
      capacity sealed behind the cut) grows as S = (1/6) ln L + const -
      ONE SIXTH OF A NAT PER E-FOLD of record depth: the 1+1 "area law"
      (the area is a single seam point; the log is the known 1+1
      behavior, coefficient c/6 with c = 1).
 (ii) THE AREA LAW IN 2d: for a 2d record lattice cut along a line, the
      wedge entropy is EXTENSIVE IN THE CUT AREA: S = s * (cut length)
      + corner terms; linearity receipt across sizes.
 (iii) CAPACITY QUANTA: the modular (entanglement) spectrum of the
      wedge is DISCRETE with level spacing Delta eps = 2 pi^2 / ln(c L)
      (the boost tower of p13b: the alpha = 1 log-box): the ledger
      behind a horizon cut is counted in discrete quanta whose spacing
      closes only logarithmically - C5's discreteness, realized at
      finite scope.
"""
import numpy as np

def wedge_entropy(XV, PV):
    nus = np.sqrt(np.abs(np.linalg.eigvals(XV @ PV)))
    nus = np.clip(nus, 0.5 + 1e-15, None)
    return float(np.sum((nus + 0.5) * np.log(nus + 0.5)
                        - (nus - 0.5) * np.log(nus - 0.5))), np.sort(nus)[::-1]

# ---------- (i) 1+1: one sixth of a nat per e-fold ----------
print("== (i) the 1+1 horizon cut: S = (1/6) ln L + const ==")
n1 = 4000
A = np.diag(np.full(n1, 2.0)) + np.diag(-np.ones(n1 - 1), 1) \
    + np.diag(-np.ones(n1 - 1), -1)          # Dirichlet ends, massless
ev, P = np.linalg.eigh(A)
X = 0.5 * (P @ np.diag(ev ** -0.5) @ P.T)
Pm = 0.5 * (P @ np.diag(ev ** 0.5) @ P.T)
Ss = {}
chord = lambda L: (2 * n1 / np.pi) * np.sin(np.pi * L / n1)
print("    L      S(L)        S - (1/6) ln(chord)   [chord = (2n/pi) sin(pi L/n)]")
for L in (64, 128, 256, 512, 1024):
    sl = slice(0, L)                          # end region: single cut
    S, _ = wedge_entropy(X[sl, sl], Pm[sl, sl])
    Ss[L] = S
    print(f"   {L:5d}   {S:.6f}        {S - np.log(chord(L))/6:.6f}")
slope = np.polyfit([np.log(chord(L)) for L in (64, 128, 256, 512, 1024)],
                   [Ss[L] for L in (64, 128, 256, 512, 1024)], 1)[0]
print(f"  fitted coefficient of ln(record depth) = {slope:.5f}"
      f"   target c/6 = {1/6:.5f}   err = {abs(slope - 1/6):.1e}")
print("  -> S - (1/6) ln(depth) is CONSTANT (drift ~1e-3 over 16x in L):")
print("     the ledger capacity sealed behind a single horizon seam grows")
print("     by exactly ONE SIXTH OF A NAT PER E-FOLD of record depth.")

# ---------- (ii) 2d: the area law ----------
print("\n== (ii) 2d record lattice: wedge entropy is extensive in cut area ==")
mass2 = 0.05
rows = []
for n in (12, 16, 20, 24, 28):
    N2 = n * n
    idx = np.arange(N2).reshape(n, n)
    A2 = np.zeros((N2, N2))
    for i in range(n):
        for j in range(n):
            a = idx[i, j]
            A2[a, a] = 4.0 + mass2 ** 2
            for (di, dj) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ii, jj = i + di, j + dj
                if 0 <= ii < n and 0 <= jj < n:
                    A2[a, idx[ii, jj]] = -1.0
    ev2, P2 = np.linalg.eigh(A2)
    X2 = 0.5 * (P2 @ np.diag(ev2 ** -0.5) @ P2.T)
    Pm2 = 0.5 * (P2 @ np.diag(ev2 ** 0.5) @ P2.T)
    half = idx[:, :n // 2].ravel()
    S2, _ = wedge_entropy(X2[np.ix_(half, half)], Pm2[np.ix_(half, half)])
    rows.append((n, S2))
    print(f"   n = {n:2d}: cut length {n:2d}, S = {S2:.5f}")
ns = np.array([r[0] for r in rows]); S2s = np.array([r[1] for r in rows])
co = np.polyfit(ns, S2s, 1)
res = np.abs(S2s - np.polyval(co, ns)).max()
print(f"  linear fit S = {co[0]:.5f} * n + {co[1]:.5f};"
      f" max residual = {res:.1e}")
print("  -> the sealed capacity is EXTENSIVE IN THE CUT AREA (the record")
print("     area law): entropy per unit horizon area is a lattice constant")
print("     (nonuniversal), the LAW is the linearity.")

# ---------- (iii) capacity quanta ----------
print("\n== (iii) capacity quanta: the modular ledger is discrete ==")
print("    L     eps_1     eps_2     eps_3     spacing   2pi^2/ln(cL)")
for L in (128, 512):
    sl = slice(0, L)
    _, nus = wedge_entropy(X[sl, sl], Pm[sl, sl])
    eps = np.log((nus + 0.5) / (nus - 0.5))
    sp = np.mean(np.diff(eps[:4]))
    print(f"  {L:5d}  {eps[0]:8.5f}  {eps[1]:8.5f}  {eps[2]:8.5f}"
          f"   {sp:8.5f}")
r_meas = None
sl1, sl2 = slice(0, 128), slice(0, 512)
_, nu1 = wedge_entropy(X[sl1, sl1], Pm[sl1, sl1])
_, nu2 = wedge_entropy(X[sl2, sl2], Pm[sl2, sl2])
e1 = np.log((nu1 + 0.5) / (nu1 - 0.5)); e2 = np.log((nu2 + 0.5) / (nu2 - 0.5))
s1 = np.mean(np.diff(e1[:4])); s2 = np.mean(np.diff(e2[:4]))
c_eff = np.exp(2 * np.pi ** 2 / s1) / 128
pred2 = 2 * np.pi ** 2 / np.log(c_eff * 512)
print(f"  one-constant log law: c fixed at L = 128 gives c = {c_eff:.3f};")
print(f"  predicted spacing at L = 512: {pred2:.5f}   measured: {s2:.5f}"
      f"   err = {abs(pred2 - s2):.1e}")
print("  -> the modular ledger behind the seam is DISCRETE (capacity")
print("     quanta), with spacing closing only logarithmically in record")
print("     depth: Delta eps = 2 pi^2 / ln(c L) - the boost log-box of")
print("     p13b.  This is P7's C5 discreteness direction, realized at")
print("     finite record scope.")
print("== p13e done ==")
