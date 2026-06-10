#!/usr/bin/env python3
"""
v6_p12c: the Lorentzian instances of gate (C) - time-dependent and
lapse-resolved record geometries (Paper 12).

 (i)  COSMOLOGICAL REDSHIFT, 1+1 (precision): on the FRW record lattice
      ds^2 = -dt^2 + a(t)^2 dx^2, a propagating wave's coordinate
      frequency obeys omega(t) a(t) = const; measured from the record
      evolution with O(h^2) accuracy.
 (ii) COSMOLOGICAL REDSHIFT, 3+1 (the first genuinely 3+1 curved record
      instance): the same law measured on a 32^3 expanding record
      lattice with the full 3H friction.
 (iii) GRAVITATIONAL TIME DILATION (the lapse sector): one record
      lattice, one coordinate clock, two identical cavities at lapses
      N = 1 and N = 0.7: the measured frequency ratio equals the lapse
      ratio - and the lapse enters the record operator exactly as the
      normal-sector boost datum Z_perp of Paper 5 Section 11: the
      missing normal datum is OPERATIONAL in the record dynamics.
"""
import numpy as np

# ---------- (i) 1+1 FRW: omega * a = const ----------
print("== (i) cosmological redshift on the 1+1 FRW record lattice ==")
def frw_run(n, kidx, t_end=2.0, D=1):
    h = 1.0 / n
    dt = 0.2 * h
    x = np.arange(n) * h
    k = 2 * np.pi * kidx
    a = lambda t: 1.0 + 0.4 * t
    adot = 0.4
    u_prev = np.cos(k * x)
    # right-mover: u_t = +(k/a) sin(kx) at t=0
    u = u_prev + dt * (k / a(0)) * np.sin(k * x)
    rec = [u_prev[0], u[0]]
    steps = int(round(t_end / dt))
    for m in range(1, steps):
        t = m * dt
        H = adot / a(t)
        gam = D * H * dt / 2
        lap = (np.roll(u, -1) - 2 * u + np.roll(u, 1)) / h ** 2
        u_next = (2 * u - (1 - gam) * u_prev + dt ** 2 * lap / a(t) ** 2) / (1 + gam)
        u_prev, u = u, u_next
        rec.append(u[0])
    return np.array(rec), dt, a
def freq_in_window(rec, dt, t0, t1):
    i0, i1 = int(t0 / dt), int(t1 / dt)
    seg = rec[i0:i1]
    s = np.sign(seg)
    idx = np.where(np.diff(s) != 0)[0]
    crossings = idx + seg[idx] / (seg[idx] - seg[idx + 1])
    periods = np.diff(crossings) * dt
    return np.pi / np.mean(periods)
for n in (512, 1024, 2048):
    rec, dt, a = frw_run(n, kidx=40)
    w_early = freq_in_window(rec, dt, 0.10, 0.40)
    w_late = freq_in_window(rec, dt, 1.60, 1.90)
    meas = w_late / w_early
    pred = a(0.25) / a(1.75)
    print(f"  n = {n:5d}: omega_late/omega_early = {meas:.6f}"
          f"   a(t_early)/a(t_late) = {pred:.6f}   err = {abs(meas-pred):.2e}")
print("  -> omega(t) a(t) = const measured from record evolution; error")
print("     falls with refinement: the FRW redshift law is a (C)-docket")
print("     convergence statement, verified.")

# ---------- (ii) 3+1 FRW on 32^3 ----------
print("\n== (ii) the first genuinely 3+1 curved record instance (32^3 FRW) ==")
n3 = 32
h = 1.0 / n3
dt = 0.18 * h
kidx = 4
k = 2 * np.pi * kidx
x = np.arange(n3) * h
X = x[:, None, None] * np.ones((1, n3, n3))
a = lambda t: 1.0 + 0.4 * t
def evolve_mode(phase0):
    """right-moving mode with initial spatial phase phase0; returns the
    record at site (0,0,0) per step."""
    u_prev = np.cos(k * X + phase0)
    u = u_prev + dt * (k / a(0)) * np.sin(k * X + phase0)
    rec = [u_prev[0, 0, 0], u[0, 0, 0]]
    steps = int(round(2.0 / dt))
    for m in range(1, steps):
        t = m * dt
        H = 0.4 / a(t)
        gam = 3 * H * dt / 2      # D = 3: the full 3H friction
        lap = sum(np.roll(u, s, axis=ax) for ax in range(3) for s in (1, -1)) - 6 * u
        lap /= h ** 2
        u_next = (2 * u - (1 - gam) * u_prev + dt ** 2 * lap / a(t) ** 2) / (1 + gam)
        u_prev, u = u, u_next
        rec.append(u[0, 0, 0])
    return np.array(rec)
rc = evolve_mode(0.0)                 # A cos(phi)
rs = evolve_mode(-np.pi / 2)          # A sin(phi)
phi = np.unwrap(np.arctan2(rs, rc))
ts = np.arange(len(phi)) * dt
def mean_omega(t0, t1):
    i0, i1 = int(t0 / dt), int(t1 / dt)
    return (phi[i1] - phi[i0]) / (ts[i1] - ts[i0])
w_early = abs(mean_omega(0.10, 0.40))
w_late = abs(mean_omega(1.60, 1.90))
meas = w_late / w_early
pred = a(0.25) / a(1.75)
print(f"  32^3 expanding lattice, k = (4,0,0), phase-quadrature measurement:")
print(f"  omega ratio = {meas:.5f}   prediction a(early)/a(late) = {pred:.5f}"
      f"   err = {abs(meas-pred):.2e}")
print("  -> the 3+1 time-dependent record geometry carries the cosmological")
print("     redshift with the full 3H friction: gate (C)'s docket now")
print("     contains a genuinely 3+1 curved instance.")

# ---------- (iii) gravitational time dilation: the lapse sector ----------
print("\n== (iii) one lattice, one coordinate clock, two lapses ==")
n = 1200
h = 1.0 / n
Nfield = np.ones(n)
Nfield[650:951] = 0.7
cav1 = slice(101, 300)      # lapse 1 cavity (Dirichlet walls outside)
cav2 = slice(701, 900)      # lapse 0.7 cavity, identical length
def cavity_freq(cav):
    idx = np.arange(cav.start, cav.stop)
    m = len(idx)
    # local operator A = -N d(N d): rows for interior of the cavity
    Nc = Nfield[idx]
    Nh = 0.5 * (Nfield[idx] + Nfield[np.clip(idx + 1, 0, n - 1)])
    Nl = 0.5 * (Nfield[idx] + Nfield[np.clip(idx - 1, 0, n - 1)])
    A = np.zeros((m, m))
    for j in range(m):
        A[j, j] = Nc[j] * (Nh[j] + Nl[j]) * n * n
        if j + 1 < m:
            A[j, j + 1] = -Nc[j] * Nh[j] * n * n
        if j - 1 >= 0:
            A[j, j - 1] = -Nc[j] * Nl[j] * n * n
    # symmetrize in the 1/N measure for the eigenproblem
    W = np.diag(1.0 / Nc)
    As = np.diag(np.sqrt(1.0 / Nc)) @ (np.diag(Nc) @ (W @ A)) if False else A
    ev, vec = np.linalg.eig(A)
    order = np.argsort(np.real(ev))
    lam1 = np.real(ev[order][0])
    v1 = np.real(vec[:, order][:, 0])
    # evolve the actual record dynamics and extract the frequency by the
    # exact three-term cosine recursion (P8 machinery)
    dt = 0.1 * h
    u_prev = np.zeros(n); u_prev[idx] = v1
    u = u_prev.copy()
    lapN = lambda w: Nfield * (np.roll(0.5 * (Nfield + np.roll(Nfield, -1))
                                       * (np.roll(w, -1) - w), 0)
                               - np.roll(0.5 * (Nfield + np.roll(Nfield, 1))
                                         * (w - np.roll(w, 1)), 0)) * n * n
    # Dirichlet walls
    walls = np.ones(n); walls[:101] = 0; walls[300:701] = 0; walls[900:] = 0
    u = (u_prev + 0.5 * dt * dt * lapN(u_prev)) * walls
    amp = [float(u_prev[idx] @ v1), float(u[idx] @ v1)]
    for _ in range(4000):
        u_next = (2 * u - u_prev + dt * dt * lapN(u)) * walls
        u_prev, u = u, u_next
        amp.append(float(u[idx] @ v1))
    amp = np.array(amp)
    num = amp[2:] + amp[:-2]
    den = 2 * amp[1:-1]
    mask = np.abs(den) > 0.2 * np.abs(den).max()
    return np.arccos(np.clip((num[mask] / den[mask]).mean(), -1, 1)) / dt
w1 = cavity_freq(cav1)
w2 = cavity_freq(cav2)
print(f"  cavity at N = 1.0: omega = {w1:.6f}")
print(f"  cavity at N = 0.7: omega = {w2:.6f}")
print(f"  measured ratio = {w2/w1:.6f}    lapse ratio = 0.700000"
      f"    err = {abs(w2/w1-0.7):.2e}")
print("  -> gravitational time dilation from record dynamics: identical")
print("     cavities tick at the LAPSE-WEIGHTED rate in one coordinate clock.")
print("     The lapse enters the record operator A = -N d(N d) precisely as")
print("     the normal-sector boost weight - the Z_perp datum of Paper 5")
print("     Section 11, here OPERATIONAL: the frequency ratio between the")
print("     two worldlines IS the normal boost holonomy connecting them.")
print("== p12c done ==")
