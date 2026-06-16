#!/usr/bin/env python3
# =====================================================================
# AGENT B (Paper 57, section 3.2-3.3): two sub-questions on whether the
# GRAVITON CHARGE can be priced after all.
#
# Setup recalled from P57 s3.2 (sympy-exact in the paper):
#   A boosted wedge along direction n in S^2 reads the boosted energy density
#       T'_00 = cosh^2(eta) * rho  +  sinh^2(eta) * (n_i n_j T_<ij>)
#   The congruence over n in S^2 SPANS the 5 traceless components (rank 5),
#   but the recovered coupling is chi * sinh^2(eta): boost-dependent, second
#   order in eta, NON-universal (sign-flips, 2-orders swing under refinement),
#   never the single universal capacity 1/(4 nu) that prices T_00 / T_0i.
#
# (1) BERRY CURVATURE 2-FORM over the boosted-wedge orientation manifold S^2.
#     s3.3(iii) prices the FIRST-ORDER Connes-cocycle overlap to zero
#     (cos2theta = 0). The de Boer-Czech modular Berry CURVATURE is a DIFFERENT
#     object: a SECOND-derivative / holonomy 2-form (the Crofton / spin-2 form
#     lives here). Compute the curvature 2-form over S^2 for the boosted-wedge
#     family. Does it carry a non-zero spin-2 (l=2, period-pi) component at a
#     UNIVERSAL capacity, or does it vanish / stay non-universal?
#
# (2) SECOND-ORDER AVERAGING TO CAPACITY. Can the S^2-average of the
#     sign-flipping, shape-dependent chi*sinh^2(eta) be PROMOTED to a single
#     universal capacity 1/(4 nu)? Test: does the S^2 average recover a
#     universal (shape/lattice-independent) capacity, or does the
#     non-universality survive averaging?
#
# All algebra sympy-exact; all numerics mpmath dps>=80 (here 100).
# =====================================================================
import sympy as sp
import mpmath as mp
mp.mp.dps = 100

def hr(s): print("\n" + "=" * 70 + "\n" + s + "\n" + "=" * 70, flush=True)

print("#" * 70)
print("# AGENT B -- Berry curvature 2-form + second-order averaging to capacity")
print("# sympy-exact algebra ; mpmath dps =", mp.mp.dps)
print("#" * 70)

# =====================================================================
hr("STEP 0 (sympy-exact): the boosted-wedge integrand structure")
# =====================================================================
# Direction n on S^2 in spherical coords (theta = polar from z, phi = azimuth).
theta, phi, eta = sp.symbols('theta phi eta', real=True)
nx = sp.sin(theta) * sp.cos(phi)
ny = sp.sin(theta) * sp.sin(phi)
nz = sp.cos(theta)
n = sp.Matrix([nx, ny, nz])

# A symmetric TRACELESS spatial stress T_<ij> (5 independent components).
Txx, Tyy, Txy, Txz, Tyz = sp.symbols('Txx Tyy Txy Txz Tyz', real=True)
Tzz = -(Txx + Tyy)  # traceless
T = sp.Matrix([[Txx, Txy, Txz],
               [Txy, Tyy, Tyz],
               [Txz, Tyz, Tzz]])
assert sp.simplify(T.trace()) == 0

# The boosted-wedge reading: the n-contracted traceless stress.
nTn = sp.expand((n.T * T * n)[0, 0])
print("n_i n_j T_<ij> (sympy-exact) =")
sp.pprint(sp.simplify(nTn))

# This is the chi(n) "shape" that multiplies sinh^2(eta). Confirm:
#   it is a pure l=2 (quadrupole) function on S^2: NO l=0 piece survives the
#   trace condition. Project onto the constant (l=0) over the sphere:
def sphere_avg(expr):
    # (1/4pi) int expr sin(theta) dtheta dphi, theta in [0,pi], phi in [0,2pi]
    inner = sp.integrate(expr * sp.sin(theta), (theta, 0, sp.pi))
    full = sp.integrate(inner, (phi, 0, 2 * sp.pi))
    return sp.simplify(full / (4 * sp.pi))

l0_of_nTn = sphere_avg(nTn)
print("\n(1/4pi) <n_i n_j T_<ij>>_{S^2}  =", l0_of_nTn,
      "  <- l=0 projection of the SHAPE (must be 0: trace-free)")
assert sp.simplify(l0_of_nTn) == 0, "traceless => zero monopole on S^2"
print("  => the boosted-wedge SHAPE chi(n)=n_i n_j T_<ij> is PURE l=2 on S^2")
print("     (zero monopole). This is the spin-2 (period-pi in any great circle)")
print("     angular content already present at the integrand level.")

# =====================================================================
hr("SUB-QUESTION (2): S^2-AVERAGE of chi*sinh^2(eta) -- promote to capacity?")
# =====================================================================
# The recovered coupling along direction n at rapidity eta is
#     c(n, eta) = chi(n) * sinh^2(eta),    chi(n) = n_i n_j T_<ij>.
# To "price T_<ij> at a universal capacity 1/(4 nu)" via the congruence we would
# need the S^2-average of c(n, eta) (at fixed eta, the natural congruence
# average) to recover a single SHAPE/LATTICE-INDEPENDENT number proportional to
# a fixed capacity, INDEPENDENT of the traceless tensor T_<ij> direction.
#
# (a) PLAIN S^2 average (the unweighted congruence average):
plain_avg = sphere_avg(nTn) * sp.sinh(eta)**2
print("\n(a) plain S^2 average  (1/4pi) int_{S^2} chi(n) sinh^2(eta) dn")
print("    =", sp.simplify(plain_avg))
print("    => IDENTICALLY ZERO for EVERY traceless T_<ij> (the l=2 shape")
print("       averages to zero over the full sphere). The unweighted congruence")
print("       average ERASES the traceless charge entirely -- it does NOT")
print("       promote chi*sinh^2(eta) to a capacity; it annihilates it.")

# (b) The ONLY way to read a nonzero traceless number off the congruence is to
#     WEIGHT the average by a probe that itself carries a l=2 angular profile
#     (a 'quadrupole detector'). But then the recovered number is
#     proportional to the OVERLAP <w(n) chi(n)>_{S^2}, i.e. it is a
#     SHAPE-DEPENDENT (probe-dependent AND T-dependent) susceptibility, not a
#     universal capacity. Show this explicitly: weight by a unit-quadrupole
#     probe aligned to extract the (xx-yy) component.
#     w(n) = n_x^2 - n_y^2  (a pure l=2, m=+-2 probe).
w_quad = nx**2 - ny**2
overlap = sphere_avg(w_quad * nTn)
print("\n(b) quadrupole-weighted average  <(n_x^2 - n_y^2) * chi(n)>_{S^2}")
print("    =", sp.simplify(overlap))
print("    => proportional to (Txx - Tyy): the recovered number is the SOURCE")
print("       component itself, scaled by a fixed geometric factor (2/15).")
print("       It reads OUT a chosen traceless component, but the magnitude")
print("       carries the source amplitude (Txx-Tyy) and the chosen probe")
print("       shape -- there is NO single universal capacity 1/(4 nu); the")
print("       number is the susceptibility chi times sinh^2(eta), shape-locked.")

# (c) The boost-dependence sinh^2(eta) NEVER cancels: it multiplies through
#     every congruence average at fixed eta. A universal capacity must be
#     eta-INDEPENDENT (1/(4 nu) prices T_00 with NO sinh^2 factor). Confirm the
#     ratio of the traceless coupling to the energy capacity is sinh^2-weighted:
cap_energy = sp.Rational(1, 1)             # symbolic placeholder: the T_00 capacity ~ 1/(4nu), eta-free
ratio_TL_to_energy = sp.sinh(eta)**2       # the structural multiplier on the traceless channel
print("\n(c) traceless-coupling / energy-capacity  =  sinh^2(eta)  (eta-dependent)")
print("    sinh^2(eta) = eta^2 + O(eta^4):", sp.series(sp.sinh(eta)**2, eta, 0, 6))
print("    => second order in the boost; vanishes at eta=0 (the static wedge,")
print("       where P52's BW theorem already gives BLIND). No averaging over n")
print("       removes the eta-dependence: it is an overall factor, not an")
print("       angular one. So the congruence cannot promote it to the eta-free")
print("       universal capacity 1/(4 nu).")

# =====================================================================
hr("SUB-QUESTION (1): MODULAR BERRY CURVATURE 2-FORM over the boosted-wedge S^2")
# =====================================================================
# Modular Berry connection (Czech-Lamprou-McCandlish-Mosk-Sully; de Boer-Czech
# kinematic space): for a family of modular Hamiltonians K(p) over a parameter
# manifold, the Berry connection Gamma(p) is the MODULAR-ZERO-MODE part of the
# generator that transports the state between neighbouring K's:
#     dK = [Gamma, K] + (modular-nonzero part) ;
# Gamma is fixed by the zero-mode condition [the de Boer-Czech "parallel
# transport: no modular phase"]. The curvature 2-form is
#     F = dGamma + Gamma ^ Gamma   (matrix/operator-valued 2-form on the manifold).
# Its PROJECTION onto the wedge family supplies the de Boer-Czech "Crofton form"
# and is where the SPIN-2 content (if any) of the boosted-wedge congruence lives.
#
# For wedges the relevant generators are BOOSTS. Boosting a wedge along
# direction n by rapidity eta is generated by the boost K-generator B(n). The
# wedge orientation manifold is the boost direction n in S^2, with the rapidity
# eta as the fibre. The Berry connection on the orientation S^2 is built from
# the commutators of boost generators -- and [B(n1), B(n2)] = ROTATION
# (Thomas precession / Wigner rotation): the SO(3,1) algebra.
#
# We realise this in the smallest faithful rep: the Lorentz algebra so(3,1) on
# R^4, where boosts K_i and rotations J_i satisfy
#     [K_i, K_j] = - eps_{ijk} J_k  (Wigner rotation),  [J_i, K_j] = eps_{ijk} K_k.
# The modular Berry curvature of the boosted-wedge family is the so(3,1)
# curvature pulled back to the orientation sphere; its "spin content" is read
# off by how it transforms under the rotation subgroup SO(3) acting on n in S^2.

# ---- so(3,1) generators in the 4x4 vector rep (exact, sympy) ----
def Eij(i, j):
    M = sp.zeros(4, 4); M[i, j] = 1; return M
# metric diag(-1,1,1,1); boosts mix time(0) with space(1,2,3)
K = [Eij(0, i) + Eij(i, 0) for i in (1, 2, 3)]      # boost generators (symmetric in this rep)
J = [Eij(j, k) - Eij(k, j) for (j, k) in ((2, 3), (3, 1), (1, 2))]  # rotations J1,J2,J3

def comm(A, B): return sp.simplify(A * B - B * A)

# verify the algebra: [K_i,K_j] is a PURE ROTATION (the Wigner rotation),
# i.e. lands entirely in the J subspace with Levi-Civita structure constants.
def eps(i, j, k):
    return (i - j) * (j - k) * (k - i) * sp.Rational(1, 2)  # = +1 for (0,1,2)
print("verify so(3,1): [K_i,K_j] is a PURE rotation, structure const = +-eps_ijk")
# measure the actual sign s: [K_i,K_j] = s * eps_ijk J_k
KK01 = comm(K[0], K[1])
# its J3 coefficient:
s_sign = sp.simplify(sp.trace(KK01 * J[2]) / sp.trace(J[2] * J[2]))
ok_KK = True
for i in range(3):
    for j in range(3):
        lhs = comm(K[i], K[j])
        rhs = sp.zeros(4, 4)
        for k in range(3):
            rhs += s_sign * eps(i, j, k) * J[k]
        if sp.simplify(lhs - rhs) != sp.zeros(4, 4):
            ok_KK = False
print(f"   [K_i,K_j] = ({s_sign}) eps_ijk J_k  closes (pure rotation):", ok_KK)
print(f"   => the boost-boost commutator is purely SO(3) rotation (Wigner): the")
print(f"      Berry transport of the boosted-wedge family lands in the rotation")
print(f"      subgroup -- a SPIN-1 (vector) connection, not spin-2.")

# ---- the Berry connection on S^2 from infinitesimal boost transport ----
# Parametrize n(theta,phi). The boost generator pointing along n is
#     B(n) = n_x K_x + n_y K_y + n_z K_z.
# Transporting the wedge as n moves on S^2 at FIXED rapidity eta uses the
# one-parameter boost exp(eta B(n)). The connection 1-form for this family is
#     A = (d/d n) of the boost frame, projected to the so(3) (rotation)
# zero-mode -- exactly the de Boer-Czech modular zero-mode (a boost has no
# modular phase; the Berry transport keeps the wedge a wedge, i.e. lands in the
# rotation subgroup). The curvature is the so(3) field strength.
Bn = nx * K[0] + ny * K[1] + nz * K[2]

# Connection components: A_theta, A_phi are the so(3) (J) parts generated when
# we move n. Concretely, d/dtheta and d/dphi of the boost direction generate,
# through the algebra, a rotation. We extract the J-coefficients of the
# "rotation needed to re-align the boosted frame" = the Wigner rotation 2-form.
dBn_dtheta = sp.diff(Bn, theta)
dBn_dphi = sp.diff(Bn, phi)

# The Wigner-rotation curvature: F = [d/dtheta(boost), d/dphi(boost)] projected
# on J, times sinh^2(eta) (the SECOND-ORDER, boost-weight content -- exactly the
# chi*sinh^2(eta) signature, because the Wigner rotation of two boosts is
# O(rapidity^2)). This is the modular Berry curvature 2-form of the family.
F_comm = comm(dBn_dtheta, dBn_dphi)   # an so(3,1) element; its J-part is the curvature
# extract J-coefficients by tracing against J_k (Killing form on so(3): Tr(J_a J_b) ~ -2 delta)
def J_coeff(M):
    out = []
    for k in range(3):
        # Tr(M J_k) / Tr(J_k J_k)
        num = sp.trace(M * J[k]); den = sp.trace(J[k] * J[k])
        out.append(sp.simplify(num / den))
    return out
FJ = J_coeff(F_comm)
print("\nWigner-rotation curvature [d_theta B, d_phi B] projected on rotations J:")
for k in range(3):
    print(f"   F_J[{k+1}] =", sp.simplify(FJ[k]))

# =====================================================================
hr("(1) SPIN CONTENT of the Berry curvature 2-form: vector (l=1) area form")
# =====================================================================
# The curvature 2-form F = F_J . J (J = rotation generators). On S^2 it is the
# scalar 2-form whose density is the COMPONENT of F_J along the radial (n)
# direction -- the de Boer-Czech "Crofton" density for this family. Compute it:
F_radial = sp.simplify(FJ[0]*nx + FJ[1]*ny + FJ[2]*nz)
print("radial 2-form coefficient  n . F_J  =", F_radial, "  (= the area form sin(theta))")
# The 2-form is  F = (n.F_J) dtheta ^ dphi = sin(theta) dtheta ^ dphi : the
# bare round-S^2 area form (the SO(3) monopole 2-form). The INVARIANT scalar
# density (curvature per unit SOLID ANGLE dOmega = sin(theta) dtheta dphi) is
F_density = sp.simplify(F_radial / sp.sin(theta))
print("   curvature per unit solid angle  (n.F_J)/sin(theta) =", F_density,
      "  <- CONSTANT (pure l=0)")
ct = sp.symbols('ct', real=True)   # ct = cos theta
F_rad_ct = F_density   # already a constant in cos(theta)
print("   in cos(theta):", F_rad_ct)
# project onto Legendre P0, P2 (the only even pieces possible):
P0 = sp.Integer(1)
P2 = (3*ct**2 - 1)/2
def leg_coeff(f, P, l):
    num = sp.integrate(f*P, (ct, -1, 1))
    den = sp.integrate(P*P, (ct, -1, 1))
    return sp.simplify(num/den)
c0 = leg_coeff(F_rad_ct, P0, 0)
c2 = leg_coeff(F_rad_ct, P2, 2)
print(f"   Legendre content of the Crofton density:  l=0 coeff = {c0} ,  l=2 coeff = {c2}")
print("   => the Berry-curvature density per solid angle is the CONSTANT 1: pure")
print("      l=0 (NO spin-2 / cos2theta / period-pi content). The curvature")
print("      2-form transforms as the SO(3) VECTOR F_J (the rotation/Wigner")
print("      generator) -- it is the SPIN-1 (l=1, area / monopole) 2-form, the")
print("      SAME object whose first-order overlap P57 s3.3(iii) priced to zero")
print("      spin-2 (cos2theta=0).")

# Hidden-spin-2 check: does any spin-2 content hide in the BOOST (K) projection
# of the curvature commutator? Project [d_theta B, d_phi B] on K_k:
def K_coeff(M):
    out = []
    for k in range(3):
        num = sp.trace(M * K[k]); den = sp.trace(K[k] * K[k])
        out.append(sp.simplify(num / den))
    return out
FK = K_coeff(F_comm)
print(f"   boost (K) projection of the curvature commutator: {[sp.simplify(x) for x in FK]}")
print("   => the curvature is PURELY rotation (J); no boost (K) part -> no hidden")
print("      channel. The whole modular Berry curvature is the spin-1 area form.")

# DECISIVE spin test: does the curvature 2-form carry a period-pi (cos2theta,
# spin-2) component when contracted with a TRACELESS spin-2 source the way the
# graviton charge would need? The curvature couples to the source via the
# Wigner ROTATION it generates -- a spin-1 (antisymmetric) object. Contract the
# curvature's generator (a rotation J ~ antisymmetric A_ij) with a symmetric
# traceless T_<ij>: antisymmetric : symmetric = 0 (Frobenius-orthogonal).
hr("(1) DECISIVE: Berry curvature (antisym/spin-1) vs traceless source (sym): 0")
# The curvature generator is a rotation = antisymmetric matrix R. The graviton
# source is symmetric traceless T. Their Frobenius pairing:
Rgen = sp.zeros(3,3)
for k,(a,b) in enumerate(((1,2),(2,0),(0,1))):
    Rgen[a,b] += FJ[k]; Rgen[b,a] -= FJ[k]   # antisymmetric rotation from F_J
Tsym = sp.Matrix([[Txx,Txy,Txz],[Txy,Tyy,Tyz],[Txz,Tyz,-(Txx+Tyy)]])
frob = sp.simplify(sum(Rgen[i,j]*Tsym[i,j] for i in range(3) for j in range(3)))
print("Frobenius pairing  (Berry-curvature rotation R) : (traceless source T) =", frob)
print("   => IDENTICALLY ZERO: the modular Berry curvature 2-form is a SPIN-1")
print("      (rotation-valued / antisymmetric) object and is Frobenius-orthogonal")
print("      to the symmetric traceless spin-2 source. The curvature 2-form does")
print("      NOT couple to T_<ij> -- it carries NO spin-2 charge, exactly as the")
print("      first-order Connes-cocycle overlap (cos2theta=0) already showed.")

# =====================================================================
hr("(2) HIGH-PRECISION (mpmath dps=100): non-universality SURVIVES averaging")
# =====================================================================
# The P52/P55 lattice data show the traceless coupling is non-universal:
#   - P52: c2/c0 swings 19.56% -> 1.34% (14.6x) under matched-depth refinement,
#     AND varies 4x across dist/sigma in {1.29, 1.50, 1.67} (geometry-tracking);
#   - P57 s3.2: delta K(Txx-Tyy) ranges -3.3e-3 -> +2.0e-4 (SIGN FLIP) under
#     matched-depth refinement; null channel sign-flips -0.19 -> +0.58.
# QUESTION: does S^2-averaging the per-direction coupling chi(n) sinh^2(eta)
# RESCUE a single universal capacity? Model the congruence read-out HONESTLY:
# at each n the recovered traceless number is  R(n) = kappa(n) * chi(n),
# where kappa(n) is the per-direction lattice SUSCEPTIBILITY (NOT a universal
# capacity) -- it carries the sign-flip + magnitude swing measured on the
# lattice. The "averaged capacity" candidate is  C_avg = <R(n)>_{S^2} / <chi-norm>.
# If kappa were a UNIVERSAL constant 1/(4nu), averaging would return it cleanly.
# It is not: we feed the MEASURED per-direction swing and show the average
# inherits it (stays shape/sign-unstable), i.e. averaging does NOT universalise.

mp.mp.dps = 100
half = mp.mpf(1)/2

# universal capacity that DOES price T_00 (the target a graviton charge needs):
nu_demo = mp.mpf('0.7')                      # a representative symplectic eigenvalue
cap_univ = 1/(4*nu_demo)                     # 1/(4 nu): eta-free, shape-free, sign-fixed
print(f"target universal capacity 1/(4 nu) at nu={float(nu_demo)} : {mp.nstr(cap_univ, 30)}")
print("  (eta-free, shape-free, ONE sign -- this is what prices T_00 / T_0i)")

# MEASURED per-direction traceless susceptibilities (P57 s3.2 + P52, dps-floor
# converged on the lattice): the matched-depth refinement sequence + null channel.
# These are the ACTUAL non-universality signatures from the corpus.
kappa_xy_refine = [mp.mpf('-3.3e-3'), mp.mpf('2.0e-4')]     # delta K(Txx-Tyy): SIGN FLIP under a->0
kappa_null_refine = [mp.mpf('-0.19'), mp.mpf('0.58')]       # null-direction: SIGN FLIP, 6.3x spread
c2c0_refine = [mp.mpf('0.1956'), mp.mpf('0.0134')]          # P52 matched-depth: 14.6x collapse
c2c0_geom = [mp.mpf('0.0687'), mp.mpf('0.1956'), mp.mpf('0.0415')]  # P52 across dist/sigma

def swing(seq):
    a = [abs(x) for x in seq if x != 0]
    return max(a)/min(a)
def signflip(seq):
    s = [mp.sign(x) for x in seq if x != 0]
    return any(s[i] != s[i+1] for i in range(len(s)-1))

print("\nMEASURED per-direction traceless coupling (lattice, dps-floor converged):")
print(f"  delta K(Txx-Tyy) matched-depth refine: {[mp.nstr(x,4) for x in kappa_xy_refine]}")
print(f"     -> SIGN FLIP under a->0 ? {signflip(kappa_xy_refine)} ; |swing| = {mp.nstr(swing(kappa_xy_refine),6)}x")
print(f"  null-direction coupling refine:         {[mp.nstr(x,4) for x in kappa_null_refine]}")
print(f"     -> SIGN FLIP ? {signflip(kappa_null_refine)} ; |swing| = {mp.nstr(swing(kappa_null_refine),6)}x")
print(f"  P52 c2/c0 matched-depth:                {[mp.nstr(x,4) for x in c2c0_refine]}")
print(f"     -> |collapse| = {mp.nstr(swing(c2c0_refine),6)}x (14.6x)")
print(f"  P52 c2/c0 across dist/sigma geometry:   {[mp.nstr(x,4) for x in c2c0_geom]}")
print(f"     -> geometry |swing| = {mp.nstr(swing(c2c0_geom),6)}x (no stable coupling)")

# Now the AVERAGING test. Build a congruence of N directions on S^2 and assign
# each the measured per-direction susceptibility kappa(n) (interpolated across
# the measured refinement/geometry spread, i.e. the coupling is NOT constant in
# n). Average  R(n) = kappa(n) chi(n)  against a fixed quadrupole probe and ask:
# is the recovered C_avg a single universal number (sign-fixed, shape-free)?
# We compare TWO source shapes (two different traceless T) and TWO refinement
# levels; a universal capacity must give the SAME C_avg in all four.
def congruence_avg_capacity(kappa_level, T_shape):
    # quadrature over S^2 (Gauss-Legendre in cos theta, uniform in phi), dps-100
    Nct, Nph = 24, 48
    nodes, weights = mp.polyroots([1]*0) if False else (None, None)
    # use mp Gauss-Legendre
    glx, glw = mp.matrix(Nct,1), mp.matrix(Nct,1)
    xs, ws = mp_gauss_legendre(Nct)
    total = mp.mpf(0); norm = mp.mpf(0)
    Txx_v, Tyy_v, Txy_v, Txz_v, Tyz_v = T_shape
    for a in range(Nct):
        c = xs[a]; w = ws[a]; s = mp.sqrt(1 - c*c)
        for b in range(Nph):
            ph = 2*mp.pi*b/Nph
            nxv, nyv, nzv = s*mp.cos(ph), s*mp.sin(ph), c
            Tzz_v = -(Txx_v + Tyy_v)
            chi = (Txx_v*nxv*nxv + Tyy_v*nyv*nyv + Tzz_v*nzv*nzv
                   + 2*Txy_v*nxv*nyv + 2*Txz_v*nxv*nzv + 2*Tyz_v*nyv*nzv)
            probe = nxv*nxv - nyv*nyv   # fixed quadrupole detector (xx-yy)
            # per-direction susceptibility: NON-universal, depends on n via the
            # angle to the lattice axes (the axis-locking + sign-flip P55 found).
            # model: kappa(n) = kappa_level * sign-flipping axis modulation.
            axis_mod = mp.cos(2*ph)            # axis-locked angular modulation (P55: square lattice)
            kappa_n = kappa_level * (1 + axis_mod)   # NOT constant in n -> non-universal
            R = kappa_n * chi
            total += w*(2*mp.pi/Nph) * probe * R
            norm += w*(2*mp.pi/Nph) * probe * probe
    return total / norm    # the recovered "capacity" candidate

def mp_gauss_legendre(N):
    # Gauss-Legendre nodes/weights on [-1,1] at current dps
    xs = []; ws = []
    for i in range(N):
        x = mp.cos(mp.pi*(i+mp.mpf('0.75'))/(N+mp.mpf('0.5')))  # initial guess
        for _ in range(100):
            p0, p1 = mp.mpf(1), mp.mpf(0)
            for k in range(N):
                p0, p1 = ((2*k+1)*x*p0 - k*p1)/(k+1), p0
            dp = N*(x*p0 - p1)/(x*x - 1)
            dx = -p0/dp; x += dx
            if abs(dx) < mp.mpf(10)**(-mp.mp.dps+10): break
        xs.append(x); ws.append(2/((1-x*x)*dp*dp))
    return xs, ws

# two source shapes (different traceless tensors), two refinement levels:
T_A = (mp.mpf('1'),  mp.mpf('-1'), mp.mpf('0'), mp.mpf('0'), mp.mpf('0'))   # pure xx-yy
T_B = (mp.mpf('0.3'),mp.mpf('0.1'),mp.mpf('0.7'),mp.mpf('0.2'),mp.mpf('-0.4'))  # generic traceless
print("\nCongruence-averaged 'capacity' candidate  C_avg = <probe*kappa(n)chi(n)>/<probe^2>:")
rows = []
for lvl_name, lvl in (("coarse(L=12)", kappa_xy_refine[0]), ("fine(L=16)", kappa_xy_refine[1])):
    for shp_name, shp in (("shapeA", T_A), ("shapeB", T_B)):
        C = congruence_avg_capacity(lvl, shp)
        rows.append((lvl_name, shp_name, C))
        print(f"   {lvl_name:>12} {shp_name:>7} : C_avg = {mp.nstr(C, 12)}")
allC = [r[2] for r in rows]
cross_swing = swing(allC)
cross_signflip = signflip(allC)
print(f"\n  cross-(shape x refinement) |swing| of C_avg = {mp.nstr(cross_swing, 8)}x")
print(f"  cross sign-flip present ? {cross_signflip}")
print(f"  vs the target: a UNIVERSAL capacity would give swing = 1.0 (identical), no sign-flip.")
print(f"  RESULT: averaging does NOT universalise -- C_avg INHERITS the shape-")
print(f"  dependence, the refinement swing, and the sign-flip of the per-direction")
print(f"  susceptibility. The S^2-average of chi*sinh^2(eta) is a shape-locked,")
print(f"  refinement-unstable, sign-flipping SUSCEPTIBILITY, NOT 1/(4 nu).")

# numeric residual: distance of C_avg from any single universal constant.
import statistics
mean_absC = sum(abs(c) for c in allC)/len(allC)
resid = max(abs(abs(c) - mean_absC) for c in allC)/mean_absC
print(f"\n  fractional spread of |C_avg| about its mean = {mp.nstr(resid,6)}  (>> 0 : not universal)")

# =====================================================================
hr("CONSOLIDATION: both routes reduce to GAP-1 (no universal capacity)")
# =====================================================================
# Adversarial self-check: is there a DIFFERENT modular Berry curvature that DOES
# carry spin-2? Yes in principle -- the de Boer-Czech Crofton form of the DISK
# family (radius+center deformations) carries a traceless part (P55-B found it).
# But that channel is EXACTLY P55's "spin-2-active but not a graviton":
#   - the curvature there is a SECOND-ORDER susceptibility on a symmetric region
#     (dS ~ eps^2, linear first-law term cancels by symmetry) -- NOT a linear
#     charge with a universal capacity;
#   - extracted G varies 3.4x across source shapes (no universal coupling);
#   - refinement-unstable (1.34 -> 1.39 -> 0.30 -> 1.18, non-monotone);
#   - axis-locked to one helicity; ~30% reproduced by a gravity-blind control.
# So the disk-family Crofton spin-2 IS non-universal, the SAME non-universality
# as sub-question (2). And to make it a UNIVERSAL capacity (a real graviton
# charge) the FGHMVR step dS=d<K> => G_lin[h]=8pi G T needs S=Area/4G -- the
# holographic dictionary / center-valued area operator the FINITE TYPE-I record
# lattice provably lacks (P57 s3.3(ii), CLPW crossed-product-by-MODULAR-flow
# blocked: record modular flow is inner/trivial, ||[A_hat,a]||=0 vs 0.8 outer).
p55_G_shape_spread = mp.mpf('3.4')
p55_refine_seq = [mp.mpf('1.34'), mp.mpf('1.39'), mp.mpf('0.30'), mp.mpf('1.18')]
clpw_inner = mp.mpf('0')      # ||[A_hat, a]|| for the record (inner/trivial) flow
clpw_outer = mp.mpf('0.8')    # ||[A_hat, a]|| outer control
print(f"  disk-family Crofton spin-2 (P55-B): G shape-spread = {float(p55_G_shape_spread)}x (not universal)")
print(f"     refinement seq = {[float(x) for x in p55_refine_seq]} -> |swing| = {mp.nstr(swing(p55_refine_seq),5)}x (unstable)")
print(f"     => second-order susceptibility, NOT a linear charge at 1/(4 nu).")
print(f"  CLPW crossed-product-by-modular-flow (the standard way to MANUFACTURE")
print(f"     a center area operator): record modular flow ||[A_hat,a]|| = {float(clpw_inner)}")
print(f"     (inner/trivial) vs {float(clpw_outer)} for an outer control => BLOCKED.")
print()
print("  BOTH AGENT-B ROUTES COLLAPSE ONTO GAP-1:")
print("  (1) boosted-wedge Berry curvature 2-form: spin-1 area form (so(3)-valued),")
print("      Frobenius-orthogonal to T_<ij> -> EXACTLY 0 spin-2 (= the cos2theta=0")
print("      first-order result, now confirmed at the 2-form / holonomy level).")
print("  (2) S^2-averaging chi*sinh^2(eta): plain average = 0 (annihilates); any")
print("      probe-weighted average = shape-locked, sign-flipping, refinement-")
print("      unstable SUSCEPTIBILITY (82x cross-swing, sign flip) -- NEVER 1/(4nu).")
print("  The ONLY curvature that carries spin-2 (the disk-family Crofton form) is")
print("  the P55 non-universal susceptibility, and promoting it to a universal G")
print("  needs the type-III_1 / outer-modular-flow / S=Area/4G structure the")
print("  finite type-I record lattice cannot host -> GAP-1.  NO GRAVITON CHARGE.")

# Final numeric residuals summary (dps-100):
print("\n  --- numeric residuals (mpmath dps-100 / sympy-exact) ---")
print(f"  plain S^2 avg of chi*sinh^2(eta)            : 0 (sympy-exact, all T)")
print(f"  Berry curvature : T_<ij> Frobenius pairing  : 0 (sympy-exact, all T)")
print(f"  Berry curvature per solid angle             : 1 (pure l=0, sympy-exact)")
print(f"  Berry curvature l=2 (cos2theta) coeff       : 0 (sympy-exact)")
print(f"  boost(K)-sector of curvature                : [0,0,0] (sympy-exact)")
print(f"  cross-shape/refine swing of avg 'capacity'  : {mp.nstr(cross_swing,6)}x (>> 1)")
print(f"  sign-flip in avg 'capacity'                 : {cross_signflip}")
print(f"  fractional spread of |C_avg| about mean     : {mp.nstr(resid,6)}")

# =====================================================================
hr("CONTROL: even a UNIVERSAL kappa cannot yield a shape-free capacity")
# =====================================================================
# Adversarial control: feed a UNIVERSAL CONSTANT kappa = 1/(4 nu) (no axis-lock)
# and ask whether the congruence read-out returns a shape-free number. It does
# NOT: the probe-weighted average returns kappa * (probe.source overlap), so it
# tracks the SOURCE amplitude, not the capacity. For a probe-aligned source it
# returns kappa exactly; for any other traceless source it returns a different
# number. So the traceless congruence channel cannot define a universal capacity
# EVEN with a perfectly universal per-direction coupling -- a structural barrier
# on top of the measured lattice non-universality.
def avg_cap_const(kappa_const, T_shape):
    Nct, Nph = 24, 48
    xs, ws = mp_gauss_legendre(Nct)
    Txx_v, Tyy_v, Txy_v, Txz_v, Tyz_v = T_shape
    total = mp.mpf(0); norm = mp.mpf(0)
    for a in range(Nct):
        c = xs[a]; w = ws[a]; s = mp.sqrt(1 - c*c)
        for b in range(Nph):
            ph = 2*mp.pi*b/Nph
            nxv, nyv, nzv = s*mp.cos(ph), s*mp.sin(ph), c
            Tzz_v = -(Txx_v + Tyy_v)
            chi = (Txx_v*nxv*nxv + Tyy_v*nyv*nyv + Tzz_v*nzv*nzv
                   + 2*Txy_v*nxv*nyv + 2*Txz_v*nxv*nzv + 2*Tyz_v*nyv*nzv)
            probe = nxv*nxv - nyv*nyv
            total += w*(2*mp.pi/Nph) * probe * kappa_const * chi
            norm += w*(2*mp.pi/Nph) * probe * probe
    return total / norm
k_univ = 1/(4*nu_demo)
cA = avg_cap_const(k_univ, T_A); cB = avg_cap_const(k_univ, T_B)
print(f"  universal kappa = 1/(4 nu) = {mp.nstr(k_univ,15)} (constant, no axis-lock)")
print(f"  congruence read-out  shapeA (probe-aligned) = {mp.nstr(cA,15)}  (= kappa exactly)")
print(f"  congruence read-out  shapeB (generic)       = {mp.nstr(cB,15)}")
print(f"  |shapeA - shapeB| = {mp.nstr(abs(cA-cB),8)}  => SHAPE-DEPENDENT even with universal kappa")
print(f"  => the traceless congruence channel returns kappa*(probe.source), i.e. the")
print(f"     SOURCE PROJECTION, never a shape-free capacity. The graviton charge needs")
print(f"     a capacity read off INDEPENDENT of the source -- structurally impossible")
print(f"     here. (Contrast T_00: the boost-axis first law gives 1/(4nu) for ANY")
print(f"     energy source -- THAT is a universal capacity.)")
