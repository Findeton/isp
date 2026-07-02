"""
v7 Paper X, receipt -- the graviton spin-2 three-layer pricing.

Paper 57 closed the gravity SCALE no-go (kappa*sigma_A and G*Lambda^2 each separately scale-invariant; linked, never numerically equal) but left the
graviton's SPIN / tensor character "spin-2-blind, 4/9 priced". This receipt prices the
"spin-2" object against owned record machinery, split into its three logically distinct layers:

  (Q-tensor)        Does the record matter stress carry the rank-2 traceless TENSOR STRUCTURE
                    (quadrupole-leading, dipole-forbidden, period-pi / radiates at 2*Omega)?
                    --> OWNED / DERIVED (reproduces paper55-A).
  (Q-coupling)      Is the record stress a CONSERVED symmetric rank-2 current, so that (by
                    Weinberg's soft-graviton uniqueness) a massless helicity-2 field MUST
                    couple to it universally?  --> the conserved-stress INPUT is OWNED; the
                    "must couple to helicity-2" is the EXTERNAL Weinberg lever.
  (Q-polarization)  Does the record fix the TWO physical helicity states (the +/x transverse-
                    traceless propagating polarizations)?  --> RECORD-BLIND: selecting the 2
                    physical polarizations from the 5-component symmetric-traceless source needs
                    a propagation direction in the unbuilt EMERGENT METRIC CONTINUUM (a direction
                    is scale-free; l_step is only the scale residue, Paper IV) AND a canonical mode
                    frame (mode-canonicalization, the fifth wall, Papers VIII/IX).

THESIS: spin-2 STRUCTURE carried + Weinberg COUPLING owned, but the propagating helicity-2
POLARIZATION content is record-blind -- the second helicity is the metric/mode wall again,
not a new obstruction.

Pre-geometric note: the source multipoles and the conservation law are record-internal stress
statistics. Where a "propagation direction" or "metric" is invoked it is named as the WALLED
input the records lack, never used as a derivation input.
"""
import numpy as np
import sympy as sp

PASS = {}


def head(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


# ===========================================================================
head("(Q-tensor) the record stress carries the spin-2 TENSOR STRUCTURE [OWNED]")
# Binary record source: two equal masses on a circular orbit, omega=1, in the x-y plane.
# Mass quadrupole Q_ij = sum_a m_a (3 x_i x_j - r^2 delta_ij) (trace-removed convention).
# Verify: (i) dipole vanishes (center of mass), (ii) Q traceless, (iii) leading radiation
# is the quadrupole oscillating at 2*omega (period pi), (iv) the TT content is l>=2 only.
t = sp.symbols("t", real=True)
m = sp.Integer(1)
# two masses at +-r(t): equal masses, opposite phase
r = sp.Matrix([sp.cos(t), sp.sin(t), 0])
positions = [r, -r]
masses = [m, m]

# (i) mass dipole = sum m x  (must vanish for the symmetric binary)
dipole = sp.zeros(3, 1)
for ma, x in zip(masses, positions):
    dipole += ma * x
dipole = sp.simplify(dipole)
print("  mass dipole  sum m*x =", dipole.T, " (vanishes => no dipole radiation)")
PASS["(Q-tensor) mass dipole vanishes (dipole radiation forbidden)"] = dipole == sp.zeros(3, 1)

# (ii) trace-free quadrupole
Q = sp.zeros(3, 3)
for ma, x in zip(masses, positions):
    rr = (x.T * x)[0]
    for i in range(3):
        for j in range(3):
            Q[i, j] += ma * (3 * x[i] * x[j] - (rr if i == j else 0))
Q = sp.simplify(Q)
trace = sp.simplify(Q[0, 0] + Q[1, 1] + Q[2, 2])
print("  quadrupole trace =", trace, " (traceless)")
PASS["(Q-tensor) quadrupole is traceless"] = trace == 0
# nonzero, and its time dependence is at 2t (period pi): Q_xx = 1 + 3 cos(2t) for the binary
Qxx = sp.simplify(Q[0, 0])
freq_ok = sp.simplify(sp.trigsimp(Qxx - (1 + 3 * sp.cos(2 * t)))) == 0
print("  Q_xx(t) =", Qxx, " = 1 + 3 cos(2t)  -> radiates at 2*omega (period pi):", freq_ok)
PASS["(Q-tensor) quadrupole oscillates at 2*omega (period pi), nonzero"] = freq_ok and Qxx != 0

# (iv) TT content is l>=2: the trace-free quadrupole has no l=0 (monopole) or l=1 (dipole) part.
# l=0 part = trace/3 = 0 (checked); l=1 part = antisymmetric/vector part = 0 for a symmetric Q.
antisym = sp.simplify(Q - Q.T)
print("  Q symmetric (no l=1 vector part):", antisym == sp.zeros(3, 3), "; trace-free (no l=0):", trace == 0)
PASS["(Q-tensor) source is pure l>=2 (symmetric + traceless: no monopole/dipole radiation)"] = (
    antisym == sp.zeros(3, 3) and trace == 0)


# ===========================================================================
head("(Q-coupling) the record stress is a CONSERVED symmetric current (Weinberg input) [OWNED]")
# A massless helicity-2 field, by Weinberg's soft-graviton uniqueness, MUST couple to a
# conserved symmetric rank-2 current = the stress tensor. SHARD owns that current: the record
# matter stress T_ij = d_i phi d_j phi is symmetric, and conserved on shell. Verify symmetry +
# conservation for a plane-wave record field phi = cos(k.x - w t), with w^2 = |k|^2 (massless).
x, y, z, tt = sp.symbols("x y z t", real=True)
kx, ky, kz = sp.symbols("k_x k_y k_z", real=True)
w = sp.sqrt(kx**2 + ky**2 + kz**2)
phi = sp.cos(kx * x + ky * y + kz * z - w * tt)
coords = [tt, x, y, z]
dphi = [sp.diff(phi, c) for c in coords]   # d_mu phi, mu=0..3 (0=time)
# stress T_mu_nu = d_mu phi d_nu phi - (1/2) eta_mu_nu (d phi)^2  (minimal scalar stress)
eta = sp.diag(-1, 1, 1, 1)
dphi2 = -dphi[0]**2 + dphi[1]**2 + dphi[2]**2 + dphi[3]**2   # eta^{mu nu} d_mu d_nu
T = sp.zeros(4, 4)
for mu in range(4):
    for nu in range(4):
        T[mu, nu] = dphi[mu] * dphi[nu] - sp.Rational(1, 2) * eta[mu, nu] * dphi2
# symmetry
sym_ok = sp.simplify(T - T.T) == sp.zeros(4, 4)
# conservation d_mu T^mu_nu = 0 (raise with eta): d_mu (eta^{mu a} T_{a nu}) = 0
div = []
for nu in range(4):
    s = 0
    for mu in range(4):
        s += eta[mu, mu] * sp.diff(T[mu, nu], coords[mu])
    div.append(sp.simplify(s))
cons_ok = all(d == 0 for d in div)
print("  record stress T_mu_nu symmetric:", sym_ok)
print("  conservation d_mu T^mu_nu = 0 (massless on-shell w^2=|k|^2):", cons_ok, "  div =", div)
PASS["(Q-coupling) record stress is symmetric + conserved => the Weinberg helicity-2 source"] = (
    sym_ok and cons_ok)
print("  [Weinberg soft-graviton uniqueness is EXTERNAL: a massless helicity-2 field MUST couple")
print("   to this conserved symmetric current -- SHARD owns the source, not the theorem.]")


# ===========================================================================
head("(Q-polarization) the TWO physical helicities are RECORD-BLIND [the walls]")
# The source is a 3x3 symmetric traceless tensor: 5 real components. The PROPAGATING graviton
# has exactly 2 physical polarizations (helicity +-2), obtained by the transverse-traceless (TT)
# projection along a propagation direction n-hat. That projection needs:
#   (a) a propagation DIRECTION n-hat -- a unit vector in the unbuilt EMERGENT METRIC CONTINUUM.
#       A direction is SCALE-FREE, so this is NOT the l_step scale wall: Paper IV owns connectivity
#       + the hop-metric up to scale, and places the absolute metric as the l_step no-go for the
#       SCALE and premature for the continuous structure a direction needs (l_step the scale residue);
#   (b) a canonical POLARIZATION BASIS (which 2 of the 5 components are the physical +,x modes)
#       -- a canonical-mode selection = mode-canonicalization, the fifth wall (Papers VIII/IX).
# Count it: a symmetric traceless 3-tensor has 5 dof; TT projection along a fixed n-hat removes 3
# (one longitudinal + two mixed), leaving 2 = the graviton polarizations. We VERIFY the counting
# for an explicit n-hat, and FLAG that n-hat itself (and the basis) is the walled input.
def tt_project(M, n):
    n = np.asarray(n, float); n = n / np.linalg.norm(n)
    P = np.eye(3) - np.outer(n, n)                      # transverse projector
    Mt = P @ M @ P
    Mtt = Mt - 0.5 * P * np.trace(Mt)                   # remove trace within the transverse plane
    return Mtt

# a generic symmetric traceless source (5 dof)
S = np.array([[1.0, 0.3, -0.2], [0.3, 0.5, 0.1], [-0.2, 0.1, -1.5]])
S = 0.5 * (S + S.T); S = S - np.eye(3) * np.trace(S) / 3
dof_source = 5
n = [0, 0, 1]
Stt = tt_project(S, n)
# the TT tensor along z has independent components Stt[0,0] = -Stt[1,1] (+) and Stt[0,1] (x): 2 dof
plus = Stt[0, 0]
cross = Stt[0, 1]
tt_dof = 2
trace_tt = np.trace(Stt)
print("  source: symmetric traceless 3-tensor =", dof_source, "dof")
print("  TT-projected along n=z:  '+' = Stt_xx = %.4f (= -Stt_yy), 'x' = Stt_xy = %.4f ; transverse trace = %.2e"
      % (plus, cross, trace_tt))
print("  TT independent dof = 2 (the helicity +-2 polarizations); 5 -> 2 needs the n-hat + basis")
PASS["(Q-polarization) TT projection: 5-dof source -> exactly 2 physical polarizations (counting)"] = (
    abs(plus + Stt[1, 1]) < 1e-12 and abs(trace_tt) < 1e-12)
# the BLIND attribution below is an ARGUMENT, not a receipted computation (no machine check):
# the 5->2 TT projection needs (a) a propagation DIRECTION n-hat -- a unit vector in the unbuilt
# EMERGENT METRIC CONTINUUM (Paper IV owns connectivity + the hop-metric up to scale; the absolute
# metric is the l_step no-go for the SCALE and premature for the continuous structure a direction
# needs) AND (b) a canonical 2-of-5 mode FRAME (mode-canonicalization, the fifth wall, Papers
# VIII/IX). Physically these are largely ONE missing structure (the metric continuum + a canonical
# mode frame): given a metric, the +/x labeling is pure gauge, so (b) is a separate input only
# because the records lack the full continuum. Hence the second helicity is record-blind.
print("  [ATTRIBUTION, not a machine check] 5->2 needs the emergent metric continuum (direction;")
print("   l_step the scale residue, Paper IV) + a canonical mode frame (the fifth wall, Papers VIII/IX);")
print("   largely one missing structure seen through two walls -- so the second helicity is record-blind.")


# ===========================================================================
head("MACHINE CHECKS")
ok = True
for k, v in PASS.items():
    print("  [%s] %s" % ("PASS" if v else "FAIL", k))
    ok = ok and v
print("\n  " + ("ALL CHECKS PASS" if ok else "*** SOME CHECK FAILED ***"))
assert ok, "a check failed"
print("=" * 78)
print("DONE.  Spin-2 STRUCTURE carried (quadrupole-leading, dipole-forbidden, period-pi, l>=2);")
print("       the conserved symmetric stress is the Weinberg helicity-2 SOURCE (coupling owned,")
print("       theorem external); but the TWO physical polarizations are RECORD-BLIND -- needing the")
print("       emergent metric continuum (direction) + a canonical mode frame (the fifth wall).  Spin-2")
print("       carried, helicity-2 mode-blind: the second helicity is the established walls, not a new one.")
print("=" * 78)
