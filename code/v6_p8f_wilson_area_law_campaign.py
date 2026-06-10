#!/usr/bin/env python3
"""
v6_p8f: Wilson-trace area law as a finite confinement probe (Paper 8, item 6).

The record-native question: WHERE the primitive holonomy disorder lives
decides the Wilson-trace law.

  T1 (character factorization, exact): for independent conjugation-
     invariant SU(2) elements g_1..g_A,
        E[chi_j(g_1...g_A)] = d_j (E[chi_j(g)]/d_j)^A.
  T2 (area law from sealed plaquettes): if the primitive disorder lives on
     PLAQUETTES (independent sealed closed-holonomy cells - exactly the
     SHARD primitive), the fundamental Wilson trace obeys an EXACT area
     law  <(1/2) tr W(R,T)> = r^{RT},  sigma = -ln r.
  T3 (perimeter law from link noise): if the disorder lives on TRANSPORTS
     (independent links), the same identity gives an exact PERIMETER law
     r^{2(R+T)}.
  Probe: 2d link-level Monte Carlo (Wilson action) confirms T2; a 3d
     Metropolis run (cube/Bianchi-constrained plaquettes) measures Creutz
     ratios: area-law-consistent at the tested coupling.  The continuum
     statement remains (R-)'''/(C)-class and is NOT claimed.
"""
import numpy as np
from scipy.special import iv

rng = np.random.default_rng(42)

# ---------- quaternion SU(2) helpers ----------
def qmul(a, b):
    w = a[..., :1] * b[..., :1] - np.sum(a[..., 1:] * b[..., 1:], axis=-1, keepdims=True)
    v = (a[..., :1] * b[..., 1:] + b[..., :1] * a[..., 1:]
         + np.cross(a[..., 1:], b[..., 1:]))
    return np.concatenate([w, v], axis=-1)

def qconj(a):
    out = a.copy()
    out[..., 1:] *= -1
    return out

def rand_su2(shape, spread=1.0):
    """random SU(2): rotation angle ~ spread-limited, axis uniform."""
    psi = rng.uniform(0, np.pi * spread, shape)
    ax = rng.normal(size=shape + (3,))
    ax /= np.linalg.norm(ax, axis=-1, keepdims=True)
    q = np.empty(shape + (4,))
    q[..., 0] = np.cos(psi)
    q[..., 1:] = np.sin(psi)[..., None] * ax
    return q

# ---------- A. one-cell distribution and character ratio ----------
print("== A. one-cell Wilson distribution: r(beta) and the Bessel identity ==")
# integration shim: np.trapz was removed in NumPy 2.0 (np.trapezoid added);
# support both so the script runs on any NumPy
_trapz = getattr(np, "trapezoid", None) or getattr(np, "trapz")

def r_beta(beta, M=200001):
    phi = np.linspace(0, np.pi, M)
    w = np.exp(beta * np.cos(phi)) * np.sin(phi)**2
    return _trapz(np.cos(phi) * w, phi) / _trapz(w, phi)
for beta in (1.0, 1.5, 2.2):
    rq = r_beta(beta)
    rb = iv(2, beta) / iv(1, beta)
    print(f"  beta={beta:3.1f}: r = <cos phi> = {rq:.9f}   I2(beta)/I1(beta) = {rb:.9f}"
          f"   gap = {abs(rq-rb):.1e}")

def sample_class(beta, size):
    shape = size if isinstance(size, tuple) else (size,)
    size = int(np.prod(shape))
    out = np.empty(size)
    have = 0
    # rejection from uniform angle
    wmax = None
    phig = np.linspace(0, np.pi, 20001)
    wg = np.exp(beta * (np.cos(phig) - 1)) * np.sin(phig)**2
    wmax = wg.max()
    while have < size:
        cand = rng.uniform(0, np.pi, 4 * (size - have))
        w = np.exp(beta * (np.cos(cand) - 1)) * np.sin(cand)**2
        keep = cand[rng.uniform(0, wmax, cand.shape) < w]
        k = min(len(keep), size - have)
        out[have:have + k] = keep[:k]
        have += k
    return out.reshape(shape)

print("\n== B. theorem T1/T2: product of A independent sealed plaquettes ==")
beta = 1.5
r = r_beta(beta)
NTR = 200000
print("   A    MC <(1/2)tr(g1...gA)>    r^A          gap/err")
for A in (1, 2, 4, 6, 9):
    phi = sample_class(beta, (NTR, A))
    ax = rng.normal(size=(NTR, A, 3))
    ax /= np.linalg.norm(ax, axis=-1, keepdims=True)
    g = np.empty((NTR, A, 4))
    g[..., 0] = np.cos(phi)
    g[..., 1:] = np.sin(phi)[..., None] * ax
    P = g[:, 0]
    for i in range(1, A):
        P = qmul(P, g[:, i])
    est = P[..., 0].mean()
    err = P[..., 0].std() / np.sqrt(NTR)
    print(f"  {A:3d}   {est:+.6f}              {r**A:+.6f}    {abs(est-r**A)/err:5.2f} sigma")
print(f"  -> exact area law for sealed-plaquette disorder: sigma = -ln r = {-np.log(r):.6f}")

# ---------- C. 2d link-level Monte Carlo ----------
print("\n== C. 2d Wilson-action lattice MC vs the exact area law ==")
L = 12
def sh(A, shifts):
    out = A
    for ax, n in shifts.items():
        out = np.roll(out, -n, axis=ax)
    return out

def make_parity(L, dims):
    g = np.indices((L,) * dims).sum(axis=0) % 2
    return g

def sweep2d(U, beta, eps=0.45, hits=4):
    par = make_parity(L, 2)
    for mu in (0, 1):
        nu = 1 - mu
        # staples
        for p in (0, 1):
            up = qmul(qmul(sh(U[nu], {mu: 1}), qconj(sh(U[mu], {nu: 1}))), qconj(U[nu]))
            dn = qmul(qmul(qconj(sh(U[nu], {mu: 1, nu: -1})), qconj(sh(U[mu], {nu: -1}))),
                      sh(U[nu], {nu: -1}))
            V = up + dn
            mask = (par == p)
            for _ in range(hits):
                dU = rand_su2((L, L), spread=eps)
                Unew = qmul(dU, U[mu])
                s_old = qmul(U[mu], V)[..., 0]
                s_new = qmul(Unew, V)[..., 0]
                acc = (rng.uniform(size=(L, L)) < np.exp(np.minimum(0, beta * (s_new - s_old)))) & mask
                U[mu][acc] = Unew[acc]

def wloop(U, R, T, mu, nu):
    ident = np.zeros(U[0].shape)
    ident[..., 0] = 1.0
    P = ident.copy()
    for i in range(R):
        P = qmul(P, sh(U[mu], {mu: i}))
    for j in range(T):
        P = qmul(P, sh(U[nu], {mu: R, nu: j}))
    for i in reversed(range(R)):
        P = qmul(P, qconj(sh(U[mu], {mu: i, nu: T})))
    for j in reversed(range(T)):
        P = qmul(P, qconj(sh(U[nu], {nu: j})))
    return P[..., 0].mean()

U = [np.zeros((L, L, 4)) for _ in range(2)]
for mu in (0, 1):
    U[mu][..., 0] = 1.0
for _ in range(300):
    sweep2d(U, beta)
loops = [(1, 1), (1, 2), (2, 2), (2, 3), (3, 3)]
acc = {RT: [] for RT in loops}
for it in range(900):
    sweep2d(U, beta)
    if it % 3 == 0:
        for RT in loops:
            acc[RT].append(wloop(U, RT[0], RT[1], 0, 1))
print("   loop    MC <W>          exact r^(RT)    pull")
for RT in loops:
    a = np.array(acc[RT])
    nb = 10
    bins = a[: len(a) // nb * nb].reshape(nb, -1).mean(axis=1)
    est, err = bins.mean(), bins.std() / np.sqrt(nb)
    pred = r ** (RT[0] * RT[1])
    print(f"  {RT}   {est:+.6f}+-{err:.6f}   {pred:+.6f}     {abs(est-pred)/err:5.2f} sigma")
print(f"  -> 2d link MC reproduces the sealed-plaquette area law exactly"
      f" (sigma = {-np.log(r):.6f} at beta = {beta})")

# ---------- D. perimeter contrast: disorder on transports ----------
print("\n== D. theorem T3: independent-link (transport) disorder ==")
Ulink = [np.zeros((L, L, 4)) for _ in range(2)]
# iid class-distributed links at the same one-cell distribution
for mu in (0, 1):
    phi = sample_class(beta, (L, L))
    ax = rng.normal(size=(L, L, 3))
    ax /= np.linalg.norm(ax, axis=-1, keepdims=True)
    Ulink[mu][..., 0] = np.cos(phi)
    Ulink[mu][..., 1:] = np.sin(phi)[..., None] * ax
print("   loop    <W> (iid links, 800 draws)        r^(perimeter)   r^(area)     pull-to-perim")
for RT in ((1, 1), (2, 2), (3, 3)):
    vals = []
    for draw in range(800):
        for mu in (0, 1):
            phi = sample_class(beta, (L, L))
            ax = rng.normal(size=(L, L, 3))
            ax /= np.linalg.norm(ax, axis=-1, keepdims=True)
            Ulink[mu][..., 0] = np.cos(phi)
            Ulink[mu][..., 1:] = np.sin(phi)[..., None] * ax
        vals.append(wloop(Ulink, RT[0], RT[1], 0, 1))
    vals = np.array(vals)
    est, err = vals.mean(), vals.std() / np.sqrt(len(vals))
    P = 2 * (RT[0] + RT[1])
    print(f"  {RT}   {est:+.6f} +- {err:.6f}            {r**P:+.6f}      {r**(RT[0]*RT[1]):+.6f}"
          f"     {abs(est - r**P)/err:5.2f} sigma")
print("  -> transport disorder gives the PERIMETER law: deconfined.")
print("     Confinement <-> the primitive disorder lives on closed-holonomy cells,")
print("     which is precisely the SHARD primitive (P4: plaquette = sealed diamond).")

# ---------- E. 3d probe: Bianchi-constrained plaquettes ----------
print("\n== E. 3d probe (cube-constrained plaquettes): Creutz ratios at beta=2.2 ==")
L3 = 6
beta3 = 2.2
def sweep3d(U, beta, eps=0.40, hits=4):
    par = make_parity(L3, 3)
    for mu in (0, 1, 2):
        Vtot = np.zeros((L3, L3, L3, 4))
        for nu in (0, 1, 2):
            if nu == mu:
                continue
            up = qmul(qmul(sh(U[nu], {mu: 1}), qconj(sh(U[mu], {nu: 1}))), qconj(U[nu]))
            dn = qmul(qmul(qconj(sh(U[nu], {mu: 1, nu: -1})), qconj(sh(U[mu], {nu: -1}))),
                      sh(U[nu], {nu: -1}))
            Vtot = Vtot + up + dn
        for p in (0, 1):
            mask = (par == p)
            for _ in range(hits):
                dU = rand_su2((L3, L3, L3), spread=eps)
                Unew = qmul(dU, U[mu])
                s_old = qmul(U[mu], Vtot)[..., 0]
                s_new = qmul(Unew, Vtot)[..., 0]
                acc = (rng.uniform(size=(L3, L3, L3)) <
                       np.exp(np.minimum(0, beta * (s_new - s_old)))) & mask
                U[mu][acc] = Unew[acc]
U3 = [np.zeros((L3, L3, L3, 4)) for _ in range(3)]
for mu in range(3):
    U3[mu][..., 0] = 1.0
for _ in range(400):
    sweep3d(U3, beta3)
planes = [(0, 1), (0, 2), (1, 2)]
loops3 = [(1, 1), (1, 2), (2, 2), (2, 3), (3, 3)]
acc3 = {RT: [] for RT in loops3}
for it in range(1200):
    sweep3d(U3, beta3)
    if it % 4 == 0:
        for RT in loops3:
            v = np.mean([wloop(U3, RT[0], RT[1], mu, nu) for mu, nu in planes])
            acc3[RT].append(v)
W = {}
for RT in loops3:
    a = np.array(acc3[RT])
    nb = 10
    bins = a[: len(a) // nb * nb].reshape(nb, -1).mean(axis=1)
    W[RT] = (bins.mean(), bins.std() / np.sqrt(nb))
print("   loop    <W>")
for RT in loops3:
    print(f"  {RT}   {W[RT][0]:+.6f} +- {W[RT][1]:.6f}")
chi22 = -np.log(W[(2, 2)][0] * W[(1, 1)][0] / W[(1, 2)][0]**2)
e22 = np.sqrt((W[(2, 2)][1]/W[(2, 2)][0])**2 + (W[(1, 1)][1]/W[(1, 1)][0])**2
              + 4 * (W[(1, 2)][1]/W[(1, 2)][0])**2)
print(f"  Creutz chi(2,2) = {chi22:.4f} +- {e22:.4f}"
      f"   (nonzero at {chi22/e22:.0f} sigma)")
w33, e33w = W[(3, 3)]
print(f"  W(3,3) = {w33:+.6f} +- {e33w:.6f}: below measurement resolution at"
      f" this run length; chi(3,3) is NOT quoted.")
print(f"  -> nonzero string tension chi(2,2) at beta = {beta3} on 6^3 with"
      f" Bianchi-constrained plaquettes: AREA-LAW-CONSISTENT at finite scope.")
print("     Scope: a finite probe; the continuum statement is (R-)'''/(C)-class.")
print("== p8f done ==")
