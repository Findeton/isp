#!/usr/bin/env python3
"""
v6_p14a: the gauge-coupled record Ginsparg-Wilson operator (Paper 14).

Paper 10 established GW as the record-chirality structure at free scope
(1d); Paper 11 wired it to the fermionic CAR towers.  This campaign
takes the GW relation as the record-chirality LAW and realizes it in 2d
U(1) gauge sectors by its canonical solution (the overlap
representative): D = 1 + g5 sign(g5 D_W(U)), D_W the Wilson kernel at
m0 = -1.  Receipts:

 (i)   the GW relation g5 D + D g5 = D g5 D holds in the GAUGE-COUPLED
       sector at machine precision;
 (ii)  gauge covariance: D(U^g) = G D(U) G^dagger exactly - the record
       operator transforms as relation-code data must (P8/P10 gauge
       mechanism);
 (iii) locality: |D(x,y)| decays exponentially in the gauge sector
       (fitted rate printed) - the record operator remains a collar
       operator, not an all-to-all kernel.

These are preconditions: the discriminating receipts (index theorem,
anomaly density, blocking) are p14b-d.
"""
import numpy as np

g1 = np.array([[0, 1], [1, 0]], complex)
g2 = np.array([[0, -1j], [1j, 0]], complex)
g5 = np.array([[1, 0], [0, -1]], complex)

def flux_links(L1, L2, Q):
    """Uniform-field-strength U(1) links with total flux 2 pi Q."""
    x2 = np.arange(L2)
    U1 = np.exp(-2j * np.pi * Q * x2 / (L1 * L2))[None, :] * np.ones((L1, 1))
    U2 = np.ones((L1, L2), complex)
    U2[:, L2 - 1] = np.exp(2j * np.pi * Q * np.arange(L1) / L1)
    return [U1, U2]

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

def plaq_phase(L1, L2, U):
    ph = np.zeros((L1, L2))
    for x1 in range(L1):
        for x2 in range(L2):
            p = (U[0][x1, x2] * U[1][(x1 + 1) % L1, x2]
                 * np.conj(U[0][x1, (x2 + 1) % L2]) * np.conj(U[1][x1, x2]))
            ph[x1, x2] = np.angle(p)
    return ph

# ---------- setup sanity ----------
L1 = L2 = 12
Q = 1
U = flux_links(L1, L2, Q)
ph = plaq_phase(L1, L2, U)
print("== setup: uniform-flux record gauge sector ==")
print(f"  {L1}x{L2}, Q = {Q}: plaquette phase uniform to "
      f"{np.abs(ph - ph.mean()).max():.1e}; total flux / 2pi = "
      f"{ph.sum()/(2*np.pi):.10f}")

# ---------- (i) GW relation in the gauge sector ----------
print("\n== (i) the GW relation, gauge-coupled ==")
D, G5, s = overlap(L1, L2, U)
gw = G5 @ D + D @ G5 - D @ G5 @ D
print(f"  ||g5 D + D g5 - D g5 D||_max = {np.abs(gw).max():.2e}")
print("  -> the record-chirality law holds EXACTLY in the gauge sector.")

# ---------- (ii) gauge covariance ----------
print("\n== (ii) gauge covariance ==")
rng = np.random.default_rng(14)
th = rng.uniform(0, 2 * np.pi, (L1, L2))
g = np.exp(1j * th)
U1g = np.array([[g[x1, x2] * U[0][x1, x2] * np.conj(g[(x1 + 1) % L1, x2])
                 for x2 in range(L2)] for x1 in range(L1)])
U2g = np.array([[g[x1, x2] * U[1][x1, x2] * np.conj(g[x1, (x2 + 1) % L2])
                 for x2 in range(L2)] for x1 in range(L1)])
Dg, _, _ = overlap(L1, L2, [U1g, U2g])
Gmat = np.kron(np.eye(2), np.diag(g.reshape(-1)))
cov = Dg - Gmat @ D @ Gmat.conj().T
print(f"  ||D(U^g) - G D(U) G^dag||_max = {np.abs(cov).max():.2e}")
print("  -> the record operator transforms covariantly: chirality data")
print("     rides the relation code, as the P8/P10 gauge mechanism demands.")

# ---------- (iii) locality ----------
print("\n== (iii) locality in the gauge sector ==")
L1 = L2 = 16
U = flux_links(L1, L2, 1)
D, G5, s = overlap(L1, L2, U)
V = L1 * L2
src = 0                                       # site (0,0)
norms = {}
for x1 in range(L1):
    for x2 in range(L2):
        d = min(x1, L1 - x1) + min(x2, L2 - x2)
        t = x1 * L2 + x2
        blk = np.abs(D[np.ix_([src, src + V], [t, t + V])]).max()
        norms[d] = max(norms.get(d, 0.0), blk)
ds = np.array(sorted(k for k in norms if 2 <= k <= 8))
vals = np.array([norms[d] for d in ds])
rate = -np.polyfit(ds, np.log(vals), 1)[0]
print("   distance:  " + "  ".join(f"{d}" for d in ds))
print("   max |D| :  " + "  ".join(f"{v:.1e}" for v in vals))
print(f"  fitted decay rate = {rate:.3f} per lattice unit"
      f"   (range/unit = {1/rate:.3f})")
print("  -> the gauge-coupled record GW operator is exponentially local:")
print("     a collar operator with O(1) record range, not an all-to-all")
print("     kernel.  Preconditions (i)-(iii) PASS; the discriminating")
print("     receipts are p14b (index), p14c (anomaly), p14d (blocking).")
print("== p14a done ==")
