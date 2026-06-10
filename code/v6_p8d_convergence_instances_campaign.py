#!/usr/bin/env python3
"""
v6_p8d: new (C) instances (Paper 8, item 4).

 (i)   3d Euclidean: variable-conductance 3-torus -> -div(c grad), O(1/n^2).
 (ii)  2+1 Lorentzian: leapfrog dispersion -> omega = |k| at O(dx^2),
       with cone-isotropy convergence.
 (iii) curved Lorentzian: 1+1 variable-speed leapfrog; mode frequencies
       from ACTUAL evolution -> Sturm-Liouville frequencies at O(dx^2);
       characteristic (null-cone bending) test.
 (iv)  first uniform-convergence lemma: |lambda_k(n) - lambda_k| <=
       C* h^2 lambda_k^2 with ONE constant uniform over a whole
       conductance class and all refinement levels; constant audited.
"""
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spl

# ---------- (i) 3d Euclidean variable-conductance torus ----------
print("== (i) 3d variable-conductance torus: spectral convergence ==")
def c3(x, y, z):
    return 1.0 + 0.3 * np.sin(2 * np.pi * x) * np.cos(2 * np.pi * y) + 0.2 * np.sin(2 * np.pi * z)

def lap3(n):
    idx = lambda i, j, k: (i % n) * n * n + (j % n) * n + (k % n)
    rows, cols, vals = [], [], []
    h = 1.0 / n
    g = np.arange(n) * h
    for i in range(n):
        for j in range(n):
            for k in range(n):
                a = idx(i, j, k)
                for d, (di, dj, dk) in enumerate(((1, 0, 0), (0, 1, 0), (0, 0, 1))):
                    xm = g[i] + 0.5 * h * di
                    ym = g[j] + 0.5 * h * dj
                    zm = g[k] + 0.5 * h * dk
                    cb = c3(xm, ym, zm) * n * n
                    b = idx(i + di, j + dj, k + dk)
                    rows += [a, b, a, b]
                    cols += [a, b, b, a]
                    vals += [cb, cb, -cb, -cb]
    return sp.csr_matrix((vals, (rows, cols)), shape=(n**3, n**3))

NEV = 7
eigs = {}
for n in (8, 12, 16, 24):
    L = lap3(n)
    vals = spl.eigsh(L, k=NEV + 1, sigma=-1e-9, which="LM",
                     return_eigenvectors=False)
    eigs[n] = np.sort(vals)[1:NEV + 1]   # drop the zero mode
ref = (24**2 * eigs[24] - 16**2 * eigs[16]) / (24**2 - 16**2)  # Richardson
e8 = np.abs(eigs[8] - ref) / ref
e12 = np.abs(eigs[12] - ref) / ref
print(f"  first {NEV} nonzero eigenvalues, Richardson reference from n=16,24")
print(f"  max rel err n=8 : {e8.max():.4e}")
print(f"  max rel err n=12: {e12.max():.4e}   ratio = {e8.max()/e12.max():.2f}"
      f"   [O(1/n^2) predicts (12/8)^2 = 2.25]")

# ---------- (ii) 2+1 Lorentzian leapfrog dispersion ----------
print("\n== (ii) 2+1 leapfrog: omega(k) -> |k| at O(dx^2), cone isotropy ==")
def omega_lf(kx, ky, dx, dt):
    sterm = np.sqrt(np.sin(kx * dx / 2)**2 + np.sin(ky * dx / 2)**2) * (dt / dx)
    return (2.0 / dt) * np.arcsin(sterm)
kvec = np.array([0.7, 0.4])
kn = np.linalg.norm(kvec)
errs = []
for dx in (0.1, 0.05, 0.025, 0.0125):
    dt = dx / 2
    errs.append(abs(omega_lf(kvec[0], kvec[1], dx, dt) - kn))
print("   dx        |omega - |k||      ratio")
for i, dx in enumerate((0.1, 0.05, 0.025, 0.0125)):
    r = errs[i - 1] / errs[i] if i else float('nan')
    print(f"  {dx:7.4f}   {errs[i]:.6e}    {r:5.2f}" if i else f"  {dx:7.4f}   {errs[i]:.6e}      -")
# isotropy of the emergent null cone
print("   cone isotropy: spread of omega over angle at |k|=1")
for dx in (0.1, 0.05, 0.025):
    dt = dx / 2
    angs = np.linspace(0, np.pi / 2, 91)
    oms = np.array([omega_lf(np.cos(a), np.sin(a), dx, dt) for a in angs])
    print(f"  dx={dx:7.4f}: (max-min)/mean = {(oms.max()-oms.min())/oms.mean():.3e}")

# ---------- (iii) curved Lorentzian: variable-speed leapfrog ----------
print("\n== (iii) curved 1+1 Lorentzian: variable-speed leapfrog ==")
def cprof(x):
    return (1.0 + 0.5 * np.sin(2 * np.pi * x))**2   # conductance; local speed sqrt(c)

def sl_matrix(n):
    h = 1.0 / n
    g = np.arange(n) * h
    cb = cprof(g + 0.5 * h)            # bond conductances
    main = (cb + np.roll(cb, 1)) / h**2
    off = -cb / h**2
    A = sp.diags([main, off, off], [0, 1, -1], shape=(n, n), format="lil")
    A[0, n - 1] = off[n - 1]
    A[n - 1, 0] = off[n - 1]
    return sp.csr_matrix(A)

# continuum reference by Richardson from fine grids
lam_f = {}
for n in (512, 1024):
    A = sl_matrix(n)
    v = spl.eigsh(A, k=8, sigma=-1e-9, which="LM", return_eigenvectors=False)
    lam_f[n] = np.sort(v)[1:8]
lam_ref = (1024**2 * lam_f[1024] - 512**2 * lam_f[512]) / (1024**2 - 512**2)
om_ref = np.sqrt(lam_ref)

def measured_frequency(n, mode):
    """evolve the ACTUAL leapfrog from a semi-discrete eigenvector and
    extract the oscillation frequency of its amplitude by phase fitting."""
    A = sl_matrix(n)
    vals, vecs = spl.eigsh(A, k=mode + 2, sigma=-1e-9, which="LM")
    order = np.argsort(vals)
    lam = vals[order][mode]
    v = vecs[:, order][:, mode]
    dt = 0.25 / n
    u_prev = v.copy()
    u = v * np.cos(np.sqrt(lam) * dt)   # seed with semi-discrete phase guess
    M = 2000
    amp = np.empty(M)
    amp[0] = v @ u_prev
    amp[1] = v @ u
    for mstep in range(2, M):
        u_next = 2 * u - u_prev - dt**2 * (A @ u)
        u_prev, u = u, u_next
        amp[mstep] = v @ u
    # frequency from the three-term recursion satisfied by cos sequences:
    # amp[m+1] + amp[m-1] = 2 cos(w dt) amp[m]
    num = amp[2:] + amp[:-2]
    den = 2 * amp[1:-1]
    mask = np.abs(den) > 0.2 * np.abs(den).max()
    w_meas = np.arccos(np.clip((num[mask] / den[mask]).mean(), -1, 1)) / dt
    w_pred = (2 / dt) * np.arcsin(np.sqrt(lam) * dt / 2)
    return w_meas, w_pred, np.sqrt(lam)

MODE = 3   # index in the sorted spectrum INCLUDING the zero mode
print("   n     mode-3 leapfrog freq    predicted     |meas-pred|   |freq - continuum|")
errs_c = []
for n in (32, 64, 128, 256):
    wm, wp, ws = measured_frequency(n, MODE)
    err = abs(wm - om_ref[MODE - 1])   # om_ref drops the zero mode
    errs_c.append(err)
    print(f"  {n:4d}   {wm:.9f}        {wp:.9f}   {abs(wm-wp):.2e}    {err:.6e}")
print("   convergence ratios to continuum omega:",
      " ".join(f"{errs_c[i-1]/errs_c[i]:.2f}" for i in range(1, len(errs_c))),
      "  [O(dx^2) predicts 4.00]")

# characteristic (null-cone bending): wavefront vs dx/dt = sqrt(c(x))
print("\n   null-cone bending: pulse arrival vs integrated characteristic")
from scipy.integrate import solve_ivp
T = 0.35
sol = solve_ivp(lambda t, x: np.sqrt(cprof(x)), (0, T), [0.1],
                dense_output=True, rtol=1e-12, atol=1e-12)
x_char = sol.y[0, -1]
arr = []
for n in (256, 512, 1024):
    h = 1.0 / n
    g = np.arange(n) * h
    A = sl_matrix(n)
    sig = 0.02
    # right-moving wave packet: u(x,0)=g0, u_t(x,0) = -sqrt(c) g0'
    g0 = np.exp(-0.5 * ((g - 0.1) / sig)**2)
    g0p = -(g - 0.1) / sig**2 * g0
    dt = 0.2 * h
    u_prev = g0
    u = g0 + dt * (-np.sqrt(cprof(g)) * g0p) + 0.5 * dt**2 * (-(A @ g0))
    nsteps = int(round(T / dt))
    for _ in range(nsteps - 1):
        u_next = 2 * u - u_prev - dt**2 * (A @ u)
        u_prev, u = u, u_next
    # energy-density peak position (quadratic interpolation)
    e = u**2
    i0 = np.argmax(e)
    im, ip = (i0 - 1) % n, (i0 + 1) % n
    denom = e[im] - 2 * e[i0] + e[ip]
    shift = 0.5 * (e[im] - e[ip]) / denom if denom != 0 else 0.0
    arr.append(g[i0] + shift * h)
for n, xa in zip((256, 512, 1024), arr):
    print(f"   n={n:5d}: peak at x = {xa:.6f}   characteristic x = {x_char:.6f}"
          f"   gap = {abs(xa-x_char):.2e}")

# ---------- (iv) uniform-convergence lemma ----------
print("\n== (iv) uniform lemma: |lam_k(n) - lam_k| <= C* h^2 lam_k^2 over a class ==")
rng = np.random.default_rng(5)
def sample_class():
    while True:
        a = rng.uniform(-0.2, 0.2, 6)
        if np.abs(a).sum() <= 0.45:
            return a
def cfun(a):
    return lambda x: 1.0 + sum(a[j] * np.sin(2 * np.pi * (j + 1) * x) for j in range(3)) \
                         + sum(a[3 + j] * np.cos(2 * np.pi * (j + 1) * x) for j in range(3))
def sl_general(n, cf):
    h = 1.0 / n
    g = np.arange(n) * h
    cb = cf(g + 0.5 * h)
    main = (cb + np.roll(cb, 1)) / h**2
    off = -cb / h**2
    A = sp.diags([main, off, off], [0, 1, -1], shape=(n, n), format="lil")
    A[0, n - 1] = off[n - 1]; A[n - 1, 0] = off[n - 1]
    return sp.csr_matrix(A)
KMODES = 12   # eigenvalue indices 1..12 (six +- pairs)
worst = 0.0
worst_info = None
nsamp = 30
for samp in range(nsamp):
    a = sample_class()
    cf = cfun(a)
    lam_fine = {}
    for n in (512, 1024):
        v = spl.eigsh(sl_general(n, cf), k=KMODES + 1, sigma=-1e-9, which="LM",
                      return_eigenvectors=False)
        lam_fine[n] = np.sort(v)[1:KMODES + 1]
    lamr = (1024**2 * lam_fine[1024] - 512**2 * lam_fine[512]) / (1024**2 - 512**2)
    for n in (32, 64, 128):
        v = spl.eigsh(sl_general(n, cf), k=KMODES + 1, sigma=-1e-9, which="LM",
                      return_eigenvectors=False)
        lam_n = np.sort(v)[1:KMODES + 1]
        h = 1.0 / n
        ratio = np.abs(lam_n - lamr) / (h**2 * lamr**2)
        if ratio.max() > worst:
            worst = ratio.max()
            worst_info = (samp, n, int(np.argmax(ratio)) + 1)
print(f"  class: c = 1 + 3-harmonic Fourier, sum|coeffs| <= 0.45 (0.55 <= c <= 1.45)")
print(f"  {nsamp} random conductances x n in {{32,64,128}} x modes 1..{KMODES}:")
print(f"  sup |lam_k(n)-lam_k| / (h^2 lam_k^2) = {worst:.4f}  at (sample,n,mode) = {worst_info}")
print(f"  LEMMA constant C* = 0.25 holds with margin {0.25/worst:.1f}x"
      if worst < 0.25 else f"  C* = 0.25 FAILS, measured {worst:.4f}")
print("== p8d done ==")
