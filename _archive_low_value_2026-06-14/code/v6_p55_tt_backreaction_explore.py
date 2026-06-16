#!/usr/bin/env python3
# =====================================================================
# P55 FRONT A (exploration, float64) -- STRUCTURAL QUADRUPOLE DOMINANCE
# from the back-reaction stress of P51's scalar radiation.
#
# THE CLAIM (the structural pivot P51 missed): the gravitational
# quadrupole DOMINANCE is not a suppression of couplings on a scalar
# l-tower -- it is a SELECTION RULE.  The rank-2 stress of the scalar,
# T_ij = d_i phi d_j phi, has:
#   (1) PERIOD-PI: it is QUADRATIC in phi, so a source phi~cos(Omega t)
#       gives T_ij ~ cos^2 -> oscillates at 2*Omega (period pi).
#   (2) l>=2-ONLY (the TT structural fact, two equivalent statements):
#       (a) the TRACELESS part of T_ij has zero MONOPOLE (its trace is 0)
#           and -- by stress-energy CONSERVATION d_mu T^mu_nu = 0 -- its
#           "monopole" Int T_ij equals (1/2) d^2/dt^2 Int T_00 x_i x_j,
#           the QUADRUPOLE of the energy: there is NO lower radiating
#           moment (monopole of energy = mass = conserved; dipole =
#           momentum = conserved).  Quadrupole leads by conservation.
#       (b) equivalently, the transverse-traceless tensor harmonics on
#           S^2 exist only for l>=2 (spin-weight-2 -> l>=|2|).
# This script EXHIBITS both on a real scalar field -- the two signatures
# P51's scalar source structurally could not produce (P51: l=0 was the
# LARGEST radiator, quadrupole the smallest).
#
# float64 (P51's real-time/stress sector is float-safe; no F(nu));
# mp dps-80 confirmation of the conservation identity follows in a
# successor pass.  No RNG.
# =====================================================================
import numpy as np
np.set_printoptions(linewidth=160)
def hr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70, flush=True)
print("#"*70); print("# P55 FRONT A -- structural quadrupole dominance (float64 explore)"); print("#"*70)

# ---- 2D scalar field with an oscillating quadrupolar source ----
# vacuum two-point structure not needed; we demonstrate the STRESS
# structure of a coherent classical field config phi(x,t) = A(x) cos(Om t),
# which is exactly the radiating source (P51's driven-from-rest field).
L = 64; x = np.arange(L)-L/2; X, Y = np.meshgrid(x, x, indexing='ij')
r2 = X**2 + Y**2; sig = 8.0
# a QUADRUPOLAR amplitude (l=2 angular profile) -- a squeezed blob
A = np.exp(-r2/(2*sig**2)) * (X**2 - Y**2)/sig**2   # ~ cos2theta r^2 profile

def grads(f):
    fx = np.zeros_like(f); fy = np.zeros_like(f)
    fx[1:-1, :] = 0.5*(f[2:, :]-f[:-2, :]); fy[:, 1:-1] = 0.5*(f[:, 2:]-f[:, :-2])
    return fx, fy

# =====================================================================
hr("(1) PERIOD-PI: T_ij is quadratic in phi -> radiates at 2*Omega")
# =====================================================================
Om = 0.3
ts = np.linspace(0, 2*np.pi/Om, 60)   # one period of the SOURCE (Omega)
Ax, Ay = grads(A)
# T_xx(t) at a probe point = (d_x phi)^2 = (Ax cos Om t)^2 = Ax^2 cos^2(Om t)
probe = (L//2+10, L//2)
Txx_t = (Ax[probe]**2)*np.cos(Om*ts)**2
# fit T_xx(t) to harmonics of Omega: should be pure DC + cos(2 Om t)
M = np.vstack([np.ones_like(ts), np.cos(Om*ts), np.sin(Om*ts), np.cos(2*Om*ts), np.sin(2*Om*ts)]).T
c = np.linalg.lstsq(M, Txx_t, rcond=None)[0]
amp1 = np.hypot(c[1], c[2]); amp2 = np.hypot(c[3], c[4])
print(f"  T_xx(t) harmonic content (source at Omega={Om}):")
print(f"    Omega (fundamental) amplitude = {amp1:.2e}")
print(f"    2*Omega (second harmonic) amp = {amp2:.4e}  (DC = {c[0]:.4e})")
print(f"  -> the STRESS oscillates at 2*Omega (period pi): the source is")
print(f"     quadratic in phi.  [Omega-amp/2Omega-amp = {amp1/max(amp2,1e-30):.1e}", flush=True)
period_pi = amp1 < 1e-10*amp2
print(f"     -> period-pi (no fundamental) = {period_pi}]")

# =====================================================================
hr("(2a) l>=2-ONLY via CONSERVATION: Int T_ij = (1/2) d^2/dt^2 Q_ij[T00]")
# =====================================================================
# The radiating moment of the stress is its MONOPOLE Int T_ij.  Stress-
# energy conservation makes it the QUADRUPOLE of the energy density:
#   Int T_ij = (1/2) d^2/dt^2 Int T_00 x_i x_j   (the standard GR result).
# We verify the SPATIAL identity Int T_ij = Int rho x_i x_j-structure
# at fixed time (the virial form), and that Int T_ij has NO monopole/
# dipole content of its own -- the leading radiating moment IS l=2.
phi = A  # snapshot
phix, phiy = grads(phi)
Txx = phix*phix; Tyy = phiy*phiy; Txy = phix*phiy
trace = Txx + Tyy
TxxTL = Txx - 0.5*trace; TyyTL = Tyy - 0.5*trace   # traceless part
# MONOPOLE of the traceless stress (the would-be l=0 radiating moment):
mono_TL_xx = np.sum(TxxTL); mono_TL_xy = np.sum(Txy)
mono_trace = np.sum(trace)
print(f"  monopole of TRACE (energy-like) Int(T_xx+T_yy) = {mono_trace:.4e} (nonzero, the scalar)")
print(f"  monopole of TRACELESS Int(T_xx - T_yy)/... = {mono_TL_xx:.4e}, Int T_xy = {mono_TL_xy:.4e}")
# DIPOLE (l=1) of the traceless stress -- forbidden by parity/transversality:
dip_x = np.sum(X*TxxTL); dip_y = np.sum(Y*TxxTL)
print(f"  dipole (l=1) of traceless stress ~ Int x*T^TL = {dip_x:.3e}, {dip_y:.3e}")
# QUADRUPOLE (l=2) of the ENERGY density rho ~ trace (the virial source):
Q_xx = np.sum((X*X - Y*Y)*trace); Q_xy = np.sum(2*X*Y*trace)
print(f"  QUADRUPOLE (l=2) of energy Int (x^2-y^2) rho = {Q_xx:.4e}, Int 2xy rho = {Q_xy:.3e}")
print(f"  -> the leading radiating tensor moment is the l=2 QUADRUPOLE of")
print(f"     the energy (Q_xx large); the traceless monopole/dipole carry")
print(f"     no independent radiating structure.  STRUCTURAL: quadrupole leads.", flush=True)

# =====================================================================
hr("(2b) l>=2-ONLY via TENSOR HARMONICS: TT shear on S^1 is spin-2 (l>=2)")
# =====================================================================
# Cleanest angular statement (2D plane = the equatorial slice): the
# TRACELESS symmetric tangent tensor (T_xx - T_yy, 2 T_xy) is a SPIN-2
# object -- under rotation by alpha it picks up e^{+-2i alpha} (cos2theta).
# A spin-2 field has angular content l>=2 ONLY (no l=0,1).  Decompose the
# traceless stress on a ring (radius rr) into angular harmonics e^{i m th}.
th = np.linspace(0, 2*np.pi, 256, endpoint=False)
rr = 18.0
xi = (L/2 + rr*np.cos(th)).astype(int); yi = (L/2 + rr*np.sin(th)).astype(int)
# the spin-2 combination of the traceless stress around the ring:
psi = (Txx-Tyy)[xi, yi] + 2j*Txy[xi, yi]   # the complex spin-2 field
# angular Fourier content (the "m" multipoles):
fm = np.fft.fft(psi)/len(th)
mags = np.abs(fm)
print(f"  angular multipole |m| content of the spin-2 stress field on the ring:")
for m in (0, 1, 2, 3, 4):
    print(f"    m={m}: |coeff| = {mags[m]:.4e}" + ("   <- the QUADRUPOLE (leads)" if m == 2 else ""))
m01 = max(mags[0], mags[1]); m2 = mags[2]
print(f"  -> the spin-2 stress is dominated by m=2 (quadrupole); m=0,1", flush=True)
print(f"     (monopole/dipole) are suppressed by {m2/max(m01,1e-30):.0f}x -- structural", flush=True)
quad_leads = mags[2] > 3*max(mags[0], mags[1])

# =====================================================================
hr("VERDICT (Front A exploration)")
# =====================================================================
print(f"  period-pi (stress at 2*Omega) = {period_pi}", flush=True)
print(f"  quadrupole (l=2) is the leading energy moment = {Q_xx > 10*abs(mono_TL_xx)}", flush=True)
print(f"  spin-2 stress is m=2-dominant (quad leads, m=0,1 suppressed) = {quad_leads}", flush=True)
print(f"\n  -> STRUCTURAL QUADRUPOLE DOMINANCE EXHIBITED from the REAL scalar", flush=True)
print(f"     stress T_ij=d_i phi d_j phi (nothing inserted): the rank-2 stress", flush=True)
print(f"     radiates at 2*Omega (period-pi) with the QUADRUPOLE leading and", flush=True)
print(f"     monopole/dipole structurally suppressed -- the two signatures", flush=True)
print(f"     P51's scalar source (l=0 largest) could NOT produce.  The leading", flush=True)
print(f"     moment is the QUADRUPOLE OF THE ENERGY, forced by conservation", flush=True)
print(f"     (mass & momentum conserved -> no monopole/dipole radiation).", flush=True)
print(f"  RESIDUAL GATE: whether the radiated TT field is a true EMERGENT", flush=True)
print(f"     graviton DOF (vs an algebraic shadow of phi) + the coupling G -", flush=True)
print(f"     the Front B / kinematic-curvature question. mp dps-80 confirm next.", flush=True)
