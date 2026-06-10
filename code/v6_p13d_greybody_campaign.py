#!/usr/bin/env python3
"""
v6_p13d: greybody factors as record-impedance physics (Paper 13, route 4).

A massive (or transverse) record mode in the static lapse geometry obeys,
in the record (tortoise) coordinate, u_tt = u_yy - V(y) u with
V(y) = N(y)^2 m_perp^2: the lapse-squared mass term IS the greybody
barrier.  For the Rindler-to-flat profile N^2 = 1/(1 + e^{-2 kappa y})
(exactly N = e^{kappa y} = kappa x near the horizon, N = 1 at infinity)
the barrier is the exactly solvable smooth step
V = m^2/(1 + e^{-2 kappa y}), with closed-form reflection

    R(omega) = [ sinh(pi(k - q)/2kappa) / sinh(pi(k + q)/2kappa) ]^2,
    k = omega,  q = sqrt(omega^2 - m^2).

 (i)  STATIONARY SCATTERING: high-precision ODE integration of the
      record mode vs the closed form.
 (ii) THE TWO LIMITS: kappa -> infinity reproduces EXACTLY Paper 12's
      sharp-interface impedance law R = ((k-q)/(k+q))^2; kappa -> 0 is
      the adiabatic (transparent) limit.  The greybody filter is the
      THERMAL-WIDTH-SMOOTHED impedance mismatch: the step width in
      record coordinates is 1/(2 kappa) = 1/(4 pi T_H).
 (iii) RECORD-NATIVE CHECK: a narrowband record wave packet evolved by
      the lattice lapse dynamics splits with energy fractions matching
      R(omega_0).
 (iv) SUB-BARRIER TOTAL REFLECTION: omega < m_perp modes cannot escape
      (R = 1): the massive sector is confined behind its own barrier.
Composition statement (text): the Hawking flux of the lapse horizon is
the route-2 thermal spectrum at T = kappa/2pi filtered by Gamma(omega) =
1 - R(omega): greybody = record impedance of the near-horizon collar.
"""
import numpy as np

def R_exact(om, m, kappa):
    if om <= m:
        return 1.0
    k = om; q = np.sqrt(om * om - m * m)
    return (np.sinh(np.pi * (k - q) / (2 * kappa))
            / np.sinh(np.pi * (k + q) / (2 * kappa))) ** 2

def R_numeric(om, m, kappa, y_span=30.0, h=5e-4):
    """Integrate u'' = (V - om^2) u from the transmitted side and read
    off R by decomposing into e^{+-iky} on the horizon side."""
    q = np.sqrt(complex(om * om - m * m))
    V = lambda y: m * m / (1 + np.exp(-2 * kappa * y))
    yR = y_span / (2 * kappa)
    yL = -y_span / (2 * kappa)
    u = np.exp(1j * q * yR)
    up = 1j * q * u
    y = yR
    n = int(round((yR - yL) / h))
    h = (yR - yL) / n
    for _ in range(n):                     # RK4 backward
        def f(y, s):
            return np.array([s[1], (V(y) - om * om) * s[0]])
        s = np.array([u, up])
        k1 = f(y, s)
        k2 = f(y - h / 2, s - h / 2 * k1)
        k3 = f(y - h / 2, s - h / 2 * k2)
        k4 = f(y - h, s - h * k3)
        s = s - h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        u, up = s
        y -= h
    k = om
    Aamp = 0.5 * (u + up / (1j * k)) * np.exp(-1j * k * y)
    Bamp = 0.5 * (u - up / (1j * k)) * np.exp(1j * k * y)
    return abs(Bamp / Aamp) ** 2

# ---------- (i) closed form vs record ODE ----------
print("== (i) greybody factor: record scattering vs the closed form ==")
m, kappa = 1.0, 0.5
print(f"  profile N^2 = 1/(1+e^(-2 kappa y)), m_perp = {m}, kappa = {kappa}"
      f"  (T_H = kappa/2pi = {kappa/(2*np.pi):.5f})")
print("   omega     R_record        R_exact         |diff|")
for om in (1.05, 1.2, 1.5, 2.0):
    Rn = R_numeric(om, m, kappa)
    Re = R_exact(om, m, kappa)
    print(f"   {om:5.2f}   {Rn:.8f}    {Re:.8f}    {abs(Rn-Re):.1e}")
print("  -> the record mode reflects off the lapse-squared barrier at")
print("     exactly the closed-form greybody factor.")

# ---------- (ii) the two limits ----------
print("\n== (ii) sharp-step limit = P12's impedance law; adiabatic limit ==")
om = 1.5
q = np.sqrt(om * om - m * m)
imped = ((om - q) / (om + q)) ** 2
for kap in (2.0, 8.0, 32.0):
    print(f"   kappa = {kap:5.1f}:  R_exact = {R_exact(om, m, kap):.6f}")
print(f"   sharp-interface impedance law ((k-q)/(k+q))^2 = {imped:.6f}")
print(f"   kappa = 0.125: R_exact = {R_exact(om, m, 0.125):.2e}  (adiabatic:"
      f" transparent)")
print("  -> the greybody filter interpolates the P12 interface physics:")
print("     it is the impedance mismatch smoothed over the thermal record")
print("     width 1/(4 pi T_H); hot horizons scatter like sharp seams,")
print("     cold ones are transparent.")

# ---------- (iii) record-native packet check ----------
print("\n== (iii) record lattice packet vs R(omega_0) ==")
om0, kap = 1.2, 2.0
n = 32768
yL, yR = -120.0, 120.0
y = np.linspace(yL, yR, n)
h = y[1] - y[0]
V = m * m / (1 + np.exp(-2 * kap * y))
sig = 12.0
y0 = -55.0
k0 = om0                                   # massless dispersion on the left
env = np.exp(-0.5 * ((y - y0) / sig) ** 2)
u0 = env * np.cos(k0 * y)
# u_t = -u_y for a right-mover f(y - t):
v0 = env * k0 * np.sin(k0 * y) + (y - y0) / sig ** 2 * env * np.cos(k0 * y)
dt = 0.2 * h
def lap(u):
    r = np.zeros_like(u)
    r[1:-1] = (u[2:] - 2 * u[1:-1] + u[:-2]) / (h * h)
    return r
u_prev = u0
u = u0 + dt * v0 + 0.5 * dt * dt * (lap(u0) - V * u0)
T = 95.0
for _ in range(int(T / dt)):
    u_next = 2 * u - u_prev + dt * dt * (lap(u) - V * u)
    u_prev, u = u, u_next
ut = (u - u_prev) / dt
uy = np.gradient(u, h)
e_dens = 0.5 * (ut ** 2 + uy ** 2 + V * u ** 2)
E_left = e_dens[y < 0].sum()
E_right = e_dens[y >= 0].sum()
R_pack = E_left / (E_left + E_right)
# narrowband target: average R over the packet's spectral weight
ks = np.linspace(k0 - 4 / sig, k0 + 4 / sig, 401)
wgt = ks ** 2 * np.exp(-sig * sig * (ks - k0) ** 2)   # energy-flux weight
R_band = np.sum(wgt * np.array([R_exact(kk, m, kap) for kk in ks])) / wgt.sum()
print(f"  packet omega_0 = {om0}, bandwidth 1/sigma = {1/sig:.3f}:")
print(f"  reflected energy fraction = {R_pack:.5f}")
print(f"  bandwidth-averaged R      = {R_band:.5f}"
      f"   (monochromatic R = {R_exact(om0, m, kap):.5f})")
print(f"  |diff| = {abs(R_pack - R_band):.1e}")
print("  -> the record dynamics itself realizes the greybody filter.")

# ---------- (iv) sub-barrier confinement ----------
print("\n== (iv) below the barrier: total reflection ==")
for om in (0.5, 0.9):
    Rn = R_numeric(om, m, kap)
    print(f"   omega = {om}: |R - 1| = {abs(Rn - 1):.1e}   (evanescent"
          f" transmitted channel: unitarity forces R = 1)")
print("  -> massive record modes below the barrier top cannot escape to")
print("     the flat region: the horizon's emission in each massive")
print("     channel opens only above m_perp - the greybody gap.")
print("== p13d done ==")
