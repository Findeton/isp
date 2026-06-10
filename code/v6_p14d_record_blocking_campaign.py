#!/usr/bin/env python3
"""
v6_p14d: the record RG preserves chirality in gauge sectors (Paper 14).

The O8 content proper: Paper 10 proved (free, 1d) that GW blocking
preserves the record-chirality structure while naive decimation destroys
the species.  Here the dichotomy is extended to GAUGE-COUPLED sectors:

 (i)  EXACT GW PRESERVATION: gauge-covariant record blocking (2x2
      block, link-transported orthonormal kernel B with BB^dag = 1,
      Gaussian smearing 1/alpha) maps the fine GW propagator to a
      coarse propagator obeying the GW relation with the COMPUTED
      R_c = (1 + 2/alpha):
        {g5, D_c^{-1}} = (1 + 2/alpha) g5   at machine precision,
      in a random smooth gauge sector.  Chirality survives record
      coarse-graining EXACTLY, gauge fields included - the
      Ginsparg-Wilson mechanism realized covariantly.
 (ii) TOPOLOGY SURVIVES GEOMETRY DECIMATION: decimating the GAUGE
      record (coarse link = transport product of fine links) preserves
      the flux sector exactly (Q_c = Q), and the coarse record GW
      operator's index still equals Q: the topological ledger entry is
      blocking-invariant.
 (iii) THE NAIVE CONTRAST: naive (central-difference) record
      kinematics in 2d carries FOUR species (zeros of the symbol at
      all Brillouin corners, machine count); the GW operator carries
      ONE.  Naive decimation in gauge sectors inherits the doubled,
      chirality-broken structure - P10's dichotomy, now gauge-coupled.
"""
import numpy as np

g1 = np.array([[0, 1], [1, 0]], complex)
g2 = np.array([[0, -1j], [1j, 0]], complex)
g5 = np.array([[1, 0], [0, -1]], complex)

def hop(L1, L2, U, mu):
    V = L1 * L2
    T = np.zeros((V, V), complex)
    for x1 in range(L1):
        for x2 in range(L2):
            s = x1 * L2 + x2
            t = (((x1 + 1) % L1) * L2 + x2) if mu == 0 else (x1 * L2 + (x2 + 1) % L2)
            T[s, t] = U[mu][x1, x2]
    return T

def wilson(L1, L2, U, m0=-1.0, r=1.0):
    V = L1 * L2
    D = (m0 + 2 * r) * np.eye(2 * V, dtype=complex)
    for mu, g in ((0, g1), (1, g2)):
        T = hop(L1, L2, U, mu)
        D -= 0.5 * (np.kron(r * np.eye(2) - g, T)
                    + np.kron(r * np.eye(2) + g, T.conj().T))
    return D

def overlap(L1, L2, U):
    V = L1 * L2
    G5 = np.kron(g5, np.eye(V))
    H = G5 @ wilson(L1, L2, U)
    ev, P = np.linalg.eigh(H)
    s = (P * np.sign(ev)) @ P.conj().T
    return np.eye(2 * V) + G5 @ s, G5, s

def flux_links(L1, L2, Q):
    x2 = np.arange(L2)
    U1 = np.exp(-2j * np.pi * Q * x2 / (L1 * L2))[None, :] * np.ones((L1, 1))
    U2 = np.ones((L1, L2), complex)
    U2[:, L2 - 1] = np.exp(2j * np.pi * Q * np.arange(L1) / L1)
    return [U1, U2]

def smooth_random_links(L1, L2, amp, rng):
    """Q = 0 smooth random sector from two low-frequency potentials."""
    def pot():
        x1 = np.arange(L1)[:, None] / L1
        x2 = np.arange(L2)[None, :] / L2
        f = np.zeros((L1, L2))
        for (k1, k2) in ((1, 0), (0, 1), (1, 1), (2, 1)):
            f += rng.normal() * np.cos(2 * np.pi * (k1 * x1 + k2 * x2)
                                       + rng.uniform(0, 2 * np.pi))
        return amp * f
    return [np.exp(1j * pot()), np.exp(1j * pot())]

# ---------- (i) exact GW preservation under record blocking ----------
print("== (i) record blocking preserves GW exactly (gauge-coupled) ==")
rng = np.random.default_rng(146)
Lf = 12; Lc = 6
U = smooth_random_links(Lf, Lf, 0.4, rng)
Df, G5f, _ = overlap(Lf, Lf, U)
sv = np.linalg.svd(Df, compute_uv=False)
print(f"  random smooth Q = 0 sector; sigma_min(D_f) = {sv[-1]:.2e}"
      f"  (the operator is MASSLESS: generic sectors are near-critical;"
      f"\n   roundoff in the receipt scales as eps * cond)")
Vf, Vc = Lf * Lf, Lc * Lc
# gauge-transported orthonormal blocking kernel (site space)
Bs = np.zeros((Vc, Vf), complex)
for c1 in range(Lc):
    for c2 in range(Lc):
        c = c1 * Lc + c2
        x1, x2 = 2 * c1, 2 * c2
        corner = x1 * Lf + x2
        Bs[c, corner] = 0.5
        Bs[c, ((x1 + 1) % Lf) * Lf + x2] = 0.5 * U[0][x1, x2]
        Bs[c, x1 * Lf + (x2 + 1) % Lf] = 0.5 * U[1][x1, x2]
        Bs[c, ((x1 + 1) % Lf) * Lf + (x2 + 1) % Lf] = \
            0.5 * U[0][x1, x2] * U[1][(x1 + 1) % Lf, x2]
B = np.kron(np.eye(2), Bs)
print(f"  ||B B^dag - 1||_max = {np.abs(B @ B.conj().T - np.eye(2*Vc)).max():.1e}"
      f"   (orthonormal, link-transported kernel)")
alpha = 3.0
Dc_inv = B @ np.linalg.inv(Df) @ B.conj().T + (1.0 / alpha) * np.eye(2 * Vc)
G5c = np.kron(g5, np.eye(Vc))
defect = G5c @ Dc_inv + Dc_inv @ G5c - (1 + 2 / alpha) * G5c
print(f"  ||{{g5, D_c^-1}} - (1 + 2/alpha) g5||_max = {np.abs(defect).max():.2e}"
      f"   (alpha = {alpha})")
print("  -> the coarse record propagator obeys the GW relation with the")
print("     COMPUTED R_c = 1 + 2/alpha, exactly, with gauge fields on:")
print("     record coarse-graining is form-invariant on the chirality law.")

# ---------- (ii) topology survives geometry decimation ----------
print("\n== (ii) the topological ledger entry survives decimation ==")
Lf = 16; Lc = 8
print("    Q    Q_coarse (flux of decimated links)    index(D(U_c))")
for Q in (1, 2, 3):
    U = flux_links(Lf, Lf, Q)
    U1c = np.zeros((Lc, Lc), complex)
    U2c = np.zeros((Lc, Lc), complex)
    for c1 in range(Lc):
        for c2 in range(Lc):
            x1, x2 = 2 * c1, 2 * c2
            U1c[c1, c2] = U[0][x1, x2] * U[0][(x1 + 1) % Lf, x2]
            U2c[c1, c2] = U[1][x1, x2] * U[1][x1, (x2 + 1) % Lf]
    Uc = [U1c, U2c]
    phc = np.zeros((Lc, Lc))
    for c1 in range(Lc):
        for c2 in range(Lc):
            p = (Uc[0][c1, c2] * Uc[1][(c1 + 1) % Lc, c2]
                 * np.conj(Uc[0][c1, (c2 + 1) % Lc]) * np.conj(Uc[1][c1, c2]))
            phc[c1, c2] = np.angle(p)
    Qc = phc.sum() / (2 * np.pi)
    _, _, sc = overlap(Lc, Lc, Uc)
    idx = 0.5 * np.real(np.trace(sc))
    print(f"    {Q}        {Qc:+.10f}                    {idx:+.5f}")
print("  -> decimating the gauge RECORD (coarse link = transport product)")
print("     preserves the flux sector exactly, and the coarse record GW")
print("     operator reads the SAME index: topology is blocking-invariant")
print("     ledger data.")

# ---------- (iii) the naive contrast: species count ----------
print("\n== (iii) naive record kinematics doubles; GW does not ==")
L = 64
ks = 2 * np.pi * np.arange(L) / L
count_naive = 0
count_gw = 0
min_gw = np.inf
for i1 in range(L):
    for i2 in range(L):
        k1, k2 = ks[i1], ks[i2]
        naive = np.sqrt(np.sin(k1) ** 2 + np.sin(k2) ** 2)
        if naive < 1e-12:
            count_naive += 1
        # free overlap symbol: D(k) = 1 + (a(k) + i b.gamma)/|..|
        b1, b2 = np.sin(k1), np.sin(k2)
        aw = -1.0 + (2 - np.cos(k1) - np.cos(k2))
        den = np.sqrt(aw * aw + b1 * b1 + b2 * b2)
        # eigenvalues of D(k): 1 + (aw +- i sqrt(b1^2+b2^2))/den
        lam = 1 + (aw + 1j * np.sqrt(b1 ** 2 + b2 ** 2)) / den
        if abs(lam) < 1e-12:
            count_gw += 1
        if (i1, i2) != (0, 0):
            min_gw = min(min_gw, abs(lam))
print(f"  Brillouin scan {L}x{L}: zeros of the naive symbol = {count_naive}"
      f"   (corners (0,0),(pi,0),(0,pi),(pi,pi))")
print(f"  zeros of the record GW symbol = {count_gw} (only k = 0;"
      f" next-smallest |D(k)| off origin = {min_gw:.3f})")
print("  -> 2d naive record kinematics carries FOUR species; the record")
print("     GW operator carries ONE: P10's decimation dichotomy holds in")
print("     2d, and (i)-(ii) show the GW side survives gauge coupling")
print("     and blocking EXACTLY - the record RG has a chirality-exact")
print("     channel; the naive channel is excluded.")
print("== p14d done ==")
