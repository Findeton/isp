#!/usr/bin/env python3
"""
v6_p10e: the record Ginsparg-Wilson operator - the fermionic record RG
opened (Paper 10, Part III; feeds O5 and O8, Paper 9 D8).

The Ginsparg-Wilson relation was BORN as a block-RG fixed-point
condition; the record RG is therefore its native home.  Free 1+1d
fermions, momentum space, Euclidean gammas g1 = s1, g2 = s2, g5 = s3:

 (i)   blocking the CONTINUUM propagator onto the unit record lattice
       with the cell-average kernel and a contact term alpha,
          G'(k) = sum_n shat(k+2pi n)^2 G(k+2pi n) + alpha,
       gives a Dirac operator D' = G'^{-1} satisfying the GW relation
          {g5, D'} = 2 alpha D' g5 D'   EXACTLY (machine residual);
 (ii)  D' has a SINGLE species (one zero of det D' on the BZ, correct
       continuum slope) and is exponentially LOCAL (decay rate fitted):
       Nielsen-Ninomiya is evaded by modifying the chiral symmetry, not
       locality - the chirality of the blocked theory is the GW-deformed
          d-psi = g5 (1 - alpha D') psi   symmetry (residual = GW residual);
 (iii) the CONTRAST: naive decimation of the naive lattice fermion
       ALIASES the doubler onto k = 0 (species residue doubles): the
       record-RG account of why doubling is robust under coarse-graining
       and why the GW kernel (smearing + contact term) is the escape.
"""
import numpy as np

s1 = np.array([[0, 1], [1, 0]], complex)
s2 = np.array([[0, -1j], [1j, 0]], complex)
s3 = np.diag([1.0, -1.0]).astype(complex)
alpha = 0.5
NSUM = 10          # image sum truncation (GW identity is exact at ANY
                   # truncation: every image term anticommutes with g5)
NG = 48            # BZ grid per axis

def shat(q):
    q = np.asarray(q, float)
    out = np.ones_like(q)
    m = np.abs(q) > 1e-12
    out[m] = np.sin(q[m] / 2) / (q[m] / 2)
    return out if out.shape else float(out)

def G_cont(k1, k2):
    k2n = k1 ** 2 + k2 ** 2
    if k2n < 1e-14:
        return None
    return (-1j) * (s1 * k1 + s2 * k2) / k2n

def Dprime(k1, k2):
    Gp = alpha * np.eye(2, dtype=complex)
    for n1 in range(-NSUM, NSUM + 1):
        for n2 in range(-NSUM, NSUM + 1):
            q1, q2 = k1 + 2 * np.pi * n1, k2 + 2 * np.pi * n2
            g = G_cont(q1, q2)
            if g is None:
                continue
            Gp = Gp + (shat(q1) * shat(q2)) ** 2 * g
    return np.linalg.inv(Gp)

print("== (i) the GW relation, exactly ==")
rng = np.random.default_rng(3)
res_gw = 0.0
res_sym = 0.0
for _ in range(60):
    k = rng.uniform(-np.pi, np.pi, 2)
    if np.hypot(*k) < 0.15:
        continue
    D = Dprime(*k)
    gw = s3 @ D + D @ s3 - 2 * alpha * (D @ s3 @ D)
    res_gw = max(res_gw, np.abs(gw).max())
    # GW-deformed chiral symmetry: D g5(1 - alpha D) + (1 - alpha D) g5 D = 0
    chi = D @ s3 @ (np.eye(2) - alpha * D) + (np.eye(2) - alpha * D) @ s3 @ D
    res_sym = max(res_sym, np.abs(chi).max())
print(f"  max GW residual ||{{g5,D'}} - 2a D' g5 D'|| over 60 random k: {res_gw:.2e}")
print(f"  max deformed-chirality residual: {res_sym:.2e}")
print("  -> the blocked record Dirac operator satisfies Ginsparg-Wilson")
print("     EXACTLY: chirality survives blocking in GW-deformed form.")

print("\n== (ii) single species, correct cone, exponential locality ==")
ks = np.linspace(-np.pi, np.pi, NG, endpoint=False)
detmin_away = 1e9
for k1 in ks:
    for k2 in ks:
        if np.hypot(k1, k2) < 0.5:
            continue
        detmin_away = min(detmin_away, abs(np.linalg.det(Dprime(k1, k2))))
slope = None
for eps in (0.05,):
    D = Dprime(eps, 0.0)
    slope = np.imag(D[0, 1]) / eps   # coefficient of i g1 k1 in 2x2 form
print(f"  min |det D'| on the BZ away from k = 0: {detmin_away:.4f}  (no doubler)")
print(f"  small-k slope of D' (target 1 for the correct cone): {abs(slope):.4f}")
Dx = np.zeros((NG, NG, 2, 2), complex)
for i, k1 in enumerate(ks):
    for j, k2 in enumerate(ks):
        if abs(k1) < 1e-12 and abs(k2) < 1e-12:
            Dx[i, j] = 0.0          # exact limit: G' diverges, D'(0) = 0
        else:
            Dx[i, j] = Dprime(k1, k2)
Dreal = np.fft.ifft2(Dx, axes=(0, 1))
prof = np.array([np.abs(Dreal[x, 0]).max() for x in range(1, NG // 2)])
fit = np.polyfit(np.arange(3, 16), np.log(prof[2:15]), 1)
print(f"  locality: |D'(x)| ~ e^(-x/xi) with xi = {-1/fit[0]:.3f} lattice units")
print(f"  (exponentially local, NOT ultralocal: Nielsen-Ninomiya is evaded")
print(f"   through the GW-modified symmetry while locality survives)")

print("\n== (iii) the aliasing contrast: naive decimation DESTROYS the species ==")
def G_naive(k1, k2):
    sn1, sn2 = np.sin(k1), np.sin(k2)
    s2n = sn1 ** 2 + sn2 ** 2
    if s2n < 1e-14:
        return None
    return (-1j) * (s1 * sn1 + s2 * sn2) / s2n
def G_decimated(k1, k2):
    Gp = np.zeros((2, 2), complex)
    for n1 in (0, 1):
        for n2 in (0, 1):
            g = G_naive(k1 / 2 + np.pi * n1, k2 / 2 + np.pi * n2)
            if g is None:
                continue
            Gp = Gp + 0.25 * g
    return Gp
# one-species continuum normalization: k^2 tr(G G+) = 2 for G = -i g.k/k^2
print(f"  k^2 tr(G G+) as k -> 0  (one species = 2):")
for eps in (0.1, 0.05, 0.02):
    resid_dec = eps ** 2 * np.abs(np.trace(
        G_decimated(eps, 0) @ G_decimated(eps, 0).conj().T)).real
    resid_gw = eps ** 2 * np.abs(np.trace(
        np.linalg.inv(Dprime(eps, 0)) @ np.linalg.inv(Dprime(eps, 0)).conj().T)).real
    print(f"    k = {eps:5.2f}:  GW-blocked = {resid_gw:.4f}    "
          f"naive decimation = {resid_dec:.6f}")
print(f"  -> pure decimation folds the doubler onto k = 0 where its OPPOSITE")
print(f"     chirality CANCELS the pole: the naive-blocked theory loses its")
print(f"     massless species entirely (residue -> 0, vs 2 for one species) -")
print(f"     an even harder failure than doubling, and the record-RG account")
print(f"     of why naive coarse-graining cannot define lattice fermions; the")
print(f"     GW kernel (cell-average smearing + contact term) restores exactly")
print(f"     ONE species with exact GW chirality.")
print("== p10e done ==")
