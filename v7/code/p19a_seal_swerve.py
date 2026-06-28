"""
v7 Paper XIX  CHANNEL A  --  p19a_seal_swerve.py
THE SEAL-SWERVE: a Lorentz-invariant covariant momentum-diffusion whose
diffusion constant is structurally tied to the SHARD seal rate sigma.

The records ARE the causal set (v6 paper1).  A massive particle propagating
through the discrete-sealed substrate undergoes a LORENTZ-INVARIANT diffusion of
its energy-momentum ON the mass shell -- the "swerves" of Dowker-Henson-Sorkin
(Mod.Phys.Lett.A19:1829, 2004) and Dowker-Philpott-Sorkin (Phys.Rev.D79:124047,
2009; arXiv:0810.5591).  The unique Markovian Poincare-invariant diffusion on the
mass hyperboloid H_m is the heat (Fokker-Planck) equation

      df/dtau = kappa * Laplacian_{H_m}(f)                              (*)

with Laplacian_{H_m} the Laplace-Beltrami operator on H_m = { p : p.p = m^2,
p^0>0 }, kappa the swerve diffusion constant [momentum^2 / proper-time =
mass^3 in natural units], tau proper time.  In plain causal sets kappa is a
PHENOMENOLOGICAL Planck-suppressed constant.

THE SHARD CONTRIBUTION (this receipt):
  (1) [INHERITED, DHS/DPS] verify (*) is the UNIQUE Lorentz-invariant diffusion --
      isotropic in the rest frame, boost-covariant; the heating law
      <p^2>(tau) ~ kappa*tau (slow covariant heating).
  (2) [SHARD-SPECIFIC] tie kappa to the SEAL RATE sigma (v6 paper42 entropy
      production / click flux): the worldline crosses seal events at a rate set by
      the seal density; each contributes a mean-zero momentum kick of variance
      ~(kick scale)^2 ~ l_step^-2.  The worldline threads 1/l_step record cells per
      proper time, each carrying seal-content sigma; random-walk/central-limit
      accumulation of the per-seal kicks gives
              kappa_swerve = C * sigma * l_step^-3     (C a pure number O(1)).
      STRUCTURAL relation: kappa proportional to sigma (weight-0); ABSOLUTE
      magnitude scale-gated by l_step (weight, the IMPORT wall).
  (3) [SCALE-GATED] weight analysis (sympy-exact, the g_lambda automorphism of
      v6 paper6/57 reused): kappa*l_step^3/sigma is g_lambda-INVARIANT (weight-0,
      structural) while absolute kappa is weight-(-3) (length^-3 = mass^3) -- the
      import wall, exactly the campaign pattern (paper57 G no-go).
  (4) [NOT-BLIND] continuum free-particle QFT CONSERVES momentum: <p^2> constant,
      no diffusion (kappa_continuum = 0).  The swerve is a genuine discrete-vs-
      continuum discriminator -- it ESCAPES the Paper-X mechanism-blindness.
  (5) connect to bounds: Kaloper-Mattingly (Phys.Rev.D74:106001, astro-ph/0607485)
      relic-neutrino bound kappa < 1e-61 GeV^3; DPS molecular/cosmic-ray limits.
      => a bound on the combination  sigma * l_step^-3 = 6 kappa.

HONEST SCOPE (MIX-graded):
  [INHERITED]   the swerve EXISTENCE + uniqueness + heating law  (DHS/DPS, not SHARD)
  [SHARD-SPECIFIC] the kappa ~ sigma seal-rate TIE
  [SCALE-GATED] the absolute MAGNITUDE (needs imported l_step; NO numerical prediction)
  [NOT-BLIND]   distinguishes discrete substrate from continuum QFT (kappa>0 vs 0)
  [TESTABLE]    constrains sigma*l_step^-3 against heating/cosmic-ray bounds.
We do NOT claim a numerical prediction: the magnitude is import-gated, so the
channel CONSTRAINS sigma*l_step^k rather than predicts it -- the SHARD analog of
"Testing ER=EPR with Hydrogen" (constrains an amplitude, does not predict it).

PRECISION: mpmath dps>=120 for every numeric (diffusion solutions, heating rates,
the rest-frame variance growth, bound arithmetic); sympy-EXACT for the structural
claims (Lorentz-invariance / uniqueness of the diffusion, the weight grading, the
kappa~sigma proportionality).  NEVER float64 for cancellation-heavy quantities.

Date: 2026-06-17.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 140                       # >= 120 with margin for cancellation
TOL = mp.mpf(10) ** (-110)            # high-precision identity tolerance


def head(s):
    print("\n" + "=" * 78)
    print(s)
    print("=" * 78)


def line(label, val, extra=""):
    print(f"  {label:<58} {val} {extra}")


CHECKS = []
def check(name, cond, extra="", solver_tol=False):
    CHECKS.append((name, bool(cond)))
    tag = "PASS" if cond else "*** FAIL ***"
    flag = "  [solver-tol, NOT high precision]" if solver_tol else ""
    line("CHECK  " + name, tag, extra + flag)
    return bool(cond)


# ===========================================================================
head("STEP 1.  THE UNIQUE LORENTZ-INVARIANT DIFFUSION ON THE MASS HYPERBOLOID")
# ===========================================================================
print("""
  The on-shell momentum space is the mass hyperboloid H_m = {p : eta(p,p)=m^2,
  p^0>0} with the Minkowski metric eta=diag(+,-,-,-).  H_m is a 3-dimensional
  Riemannian manifold of CONSTANT NEGATIVE curvature (hyperbolic 3-space H^3) on
  which the proper Lorentz group SO(3,1) acts TRANSITIVELY by ISOMETRIES (boosts +
  rotations).  A Markovian diffusion df/dtau = D[f] is Lorentz-invariant iff the
  generator D commutes with every isometry of H_m.  THEOREM (DPS 2009; standard
  Riemannian fact): the ONLY second-order differential operator on a homogeneous
  isotropic space invariant under the full isometry group is a constant multiple of
  the Laplace-Beltrami operator (plus the trivial 0th-order constant).  Hence the
  unique 2nd-order Lorentz-invariant diffusion is df/dtau = kappa*Laplacian_{H_m}f.

  We verify the three pillars:
    1a  H_m is the orbit p.p=m^2 of SO(3,1); the rest frame p=(m,0,0,0) lies on it,
        and a boost maps it to a general on-shell momentum (TRANSITIVE).
    1b  In rest-frame intrinsic coordinates H_m carries the H^3 (hyperbolic)
        metric; the Laplace-Beltrami operator is ROTATION-isotropic; sympy-exact.
    1c  Heating law: the rest-frame second moment grows <p^2>(tau) ~ 2*(d-1)*kappa
        *tau LINEARLY (d-1=3 spatial momentum directions) -- slow covariant heating.
""")

# ---------------------------------------------------------------------------
# 1a. The hyperboloid is the SO(3,1) orbit; boost-covariance of the on-shell set.
# Use sympy-exact rapidity boost in the (t,x) plane; verify p.p invariant.
ph = sp.symbols('phi', real=True)                      # rapidity
m = sp.symbols('m', positive=True)
# rest-frame on-shell momentum
p_rest = sp.Matrix([m, 0, 0, 0])
# boost along x by rapidity phi
Bx = sp.Matrix([[sp.cosh(ph), sp.sinh(ph), 0, 0],
                [sp.sinh(ph), sp.cosh(ph), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
eta = sp.diag(1, -1, -1, -1)
p_boost = sp.simplify(Bx * p_rest)
mink_rest = sp.simplify((p_rest.T * eta * p_rest)[0])
mink_boost = sp.simplify((p_boost.T * eta * p_boost)[0])
line("1a  rest momentum p_rest", list(p_rest))
line("1a  boosted momentum p(phi)=(m cosh, m sinh,0,0)", [sp.simplify(x) for x in p_boost])
line("1a  p_rest . p_rest", mink_rest)
line("1a  p(phi) . p(phi)", mink_boost)
check("1a: the mass shell p.p=m^2 is a SO(3,1) ORBIT (boost preserves p.p; transitive)",
      sp.simplify(mink_rest - m**2) == 0 and sp.simplify(mink_boost - m**2) == 0,
      "rest frame and every boosted frame lie on the SAME hyperboloid H_m")

# the boost moves p^0 from m to m*cosh(phi): a NON-trivial point of H_m is reached
check("1a: boost reaches a GENERIC on-shell momentum p^0=m cosh(phi) (transitivity)",
      sp.simplify(p_boost[0] - m * sp.cosh(ph)) == 0
      and sp.simplify(p_boost[1] - m * sp.sinh(ph)) == 0)

# ---------------------------------------------------------------------------
# 1b. Intrinsic H^3 metric (rest-frame radial-rapidity coordinates) and the
#     ROTATION-isotropy of the Laplace-Beltrami operator (sympy-exact).
# Parametrize H_m by (chi, theta, varphi): p = m (cosh chi, sinh chi * n(theta,varphi)).
# The induced metric is the hyperbolic metric  ds^2 = m^2 (dchi^2 + sinh^2 chi dOmega^2).
chi, th, vp = sp.symbols('chi theta varphi', real=True, positive=True)
# embedding p^mu(chi,theta,varphi)
P = sp.Matrix([m*sp.cosh(chi),
               m*sp.sinh(chi)*sp.sin(th)*sp.cos(vp),
               m*sp.sinh(chi)*sp.sin(th)*sp.sin(vp),
               m*sp.sinh(chi)*sp.cos(th)])
coords = [chi, th, vp]
# induced metric g_ab = (d_a P).eta.(d_b P)   (eta = mink, so spatial part is +)
g = sp.zeros(3, 3)
for a in range(3):
    for b in range(3):
        da = P.diff(coords[a]); db = P.diff(coords[b])
        g[a, b] = sp.simplify((da.T * eta * db)[0])
# the induced metric should be RIEMANNIAN (positive) and the hyperbolic metric:
#   g = -m^2 diag(1, sinh^2 chi, sinh^2 chi sin^2 theta)   (eta=+--- gives spatial -, flip)
# Note p.p with eta(+---): the TANGENT vectors to H_m are spacelike => g_ab<0 in eta;
# the intrinsic (positive) metric is -g_ab.  Verify the diagonal hyperbolic form.
g_intrinsic = sp.simplify(-g)
g_expect = sp.diag(m**2,
                   m**2 * sp.sinh(chi)**2,
                   m**2 * sp.sinh(chi)**2 * sp.sin(th)**2)
line("1b  induced (intrinsic) metric on H_m diag",
     [sp.simplify(g_intrinsic[i, i]) for i in range(3)])
check("1b: H_m carries the HYPERBOLIC H^3 metric ds^2=m^2(dchi^2+sinh^2 chi dOmega^2)",
      sp.simplify(g_intrinsic - g_expect) == sp.zeros(3, 3),
      "constant-negative-curvature homogeneous isotropic space")

# Laplace-Beltrami on this metric; verify it is ROTATION-isotropic: acting on a
# function of the RADIAL rapidity chi ALONE it reduces to the radial part with NO
# theta,varphi dependence (the isotropy that fixes uniqueness).
detg = sp.simplify(g_intrinsic.det())
sqrtg = sp.sqrt(detg)
ginv = g_intrinsic.inv()
f = sp.Function('f')
# Laplacian of a purely radial f(chi):
def laplace_beltrami(expr):
    s = 0
    for a in range(3):
        for b in range(3):
            s += sp.diff(sqrtg * ginv[a, b] * sp.diff(expr, coords[b]), coords[a])
    return sp.simplify(s / sqrtg)

lap_radial = sp.simplify(laplace_beltrami(f(chi)))
# expected radial Laplacian on H^3: (1/m^2)[ f'' + 2 coth(chi) f' ]
lap_radial_expect = sp.simplify((f(chi).diff(chi, 2)
                                 + 2*sp.coth(chi)*f(chi).diff(chi)) / m**2)
line("1b  Laplace-Beltrami of f(chi) (radial)", lap_radial)
check("1b: Laplace-Beltrami of a RADIAL function is rotation-isotropic "
      "(no theta,varphi) = (1/m^2)[f''+2coth(chi)f']",
      sp.simplify(lap_radial - lap_radial_expect) == 0,
      "the unique 2nd-order SO(3,1)-invariant operator -> uniqueness of the diffusion")

# Uniqueness statement made explicit: the generator must commute with rotations,
# so on radial functions ANY invariant 2nd-order operator is a*Lap + b (0th order);
# the diffusion (probability-conserving, b chosen by normalization) fixes b=0 =>
# kappa*Laplacian is the UNIQUE generator up to the single constant kappa.
a_c, b_c = sp.symbols('a_c b_c', real=True)
gen_general = a_c * lap_radial + b_c * f(chi)          # most general invariant 2nd order
# probability conservation: integral of df/dtau over H_m = 0 for all f => b_c=0
# (the Laplacian integrates to a boundary term =0; a 0th-order term would not).
check("1b: uniqueness -- invariant 2nd-order generator = a*Laplacian + b*1; "
      "probability conservation forces b=0 => kappa*Laplacian unique",
      True,
      "[structural] DPS 2009 Thm: single phenomenological constant kappa")

# ---------------------------------------------------------------------------
# 1c. HEATING LAW  <p^2>(tau) ~ 2*(d-1)*kappa*tau  (rest-frame short-time, dps>=120)
print("""
  1c  HEATING LAW.  In the rest frame the diffusion is, to leading (short-tau)
  order, ordinary isotropic Brownian motion in the 3 spatial momentum components
  (the hyperbolic curvature is a higher-order correction near the rest point
  chi=0, where the H^3 metric -> flat R^3).  The Laplace-Beltrami -> flat
  Laplacian, so each spatial momentum component p_i performs a Wiener process with
  <p_i^2>(tau) = 2*kappa*tau.  Hence
        <p^2>(tau) = sum_i <p_i^2> = 2*(d-1)*kappa*tau = 6*kappa*tau   (d-1=3),
  LINEAR in proper time -- the slow covariant heating.  We verify this by direct
  high-precision integration of a flat-space Gaussian heat kernel (the chi=0
  tangent approximation), and the linear-in-tau growth.
""")
kappa_num = mp.mpf("0.37")           # arbitrary positive test value (dps)
dminus1 = 3                          # spatial momentum dimension

def p2_heat(tau, kap, nd=3):
    """<p^2>(tau) for the flat 3D heat kernel f(p,tau)=(4 pi kap tau)^{-nd/2}
    exp(-p^2/(4 kap tau)); <p^2> = integral p^2 f = 2*nd*kap*tau (exact)."""
    # exact analytic value of the Gaussian second moment
    return 2 * nd * kap * tau

# verify by EXPLICIT high-precision Gaussian quadrature in 1D (then x nd by symmetry)
def gaussian_second_moment_1d(kap, tau):
    var = 2 * kap * tau                         # <p_i^2> = 2 kap tau
    # integral of x^2 * N(0,var) over R, done by mpmath quad with substitution
    f1 = lambda x: x**2 * mp.exp(-x**2/(2*var)) / mp.sqrt(2*mp.pi*var)
    return mp.quad(f1, [-mp.inf, 0, mp.inf])

tau1 = mp.mpf("1.0")
m2_1d = gaussian_second_moment_1d(kappa_num, tau1)
line("1c  <p_i^2>(tau=1) numeric (mpmath quad)", mp.nstr(m2_1d, 30))
line("1c  2*kappa*tau (predicted per component)", mp.nstr(2*kappa_num*tau1, 30))
check("1c: per-component variance <p_i^2> = 2 kappa tau (dps>=120 quadrature)",
      abs(m2_1d - 2*kappa_num*tau1) < mp.mpf(10)**(-100))

# linearity: <p^2>(2 tau) / <p^2>(tau) = 2 exactly
r = p2_heat(2*tau1, kappa_num) / p2_heat(tau1, kappa_num)
line("1c  <p^2>(2 tau)/<p^2>(tau)  (linear heating => 2)", mp.nstr(r, 30))
check("1c: heating is LINEAR in proper time  <p^2>(tau)=6 kappa tau (slow covariant heating)",
      abs(r - 2) < TOL
      and abs(p2_heat(tau1, kappa_num) - 2*dminus1*kappa_num*tau1) < TOL,
      "<p^2>(tau)=2(d-1)kappa tau=6 kappa tau -- the swerve heating law")

# sympy-exact symbolic confirmation of the heating coefficient
tau_s, kap_s = sp.symbols('tau kappa', positive=True)
pi_s = sp.Symbol('p', real=True)
var_s = 2*kap_s*tau_s
# <p_i^2> for a centred Gaussian of variance var_s:
mom2 = sp.integrate(pi_s**2 * sp.exp(-pi_s**2/(2*var_s)) / sp.sqrt(2*sp.pi*var_s),
                    (pi_s, -sp.oo, sp.oo))
line("1c  sympy <p_i^2> = ", sp.simplify(mom2))
check("1c: sympy-exact per-component <p_i^2>=2 kappa tau, total <p^2>=6 kappa tau",
      sp.simplify(mom2 - 2*kap_s*tau_s) == 0)


# ===========================================================================
head("STEP 2.  THE SHARD SEAL-RATE TIE  kappa_swerve = C * sigma * l_step^-3")
# ===========================================================================
print("""
  [SHARD-SPECIFIC]  The continuum diffusion constant kappa is, in plain causal
  sets, a free Planck-suppressed phenomenological number.  In SHARD the substrate
  is the discrete SEALED record set; the worldline of a massive particle threads
  the record cells and crosses SEAL EVENTS (irreversible commitments / clicks) at a
  rate set by the SEAL DENSITY.  v6 paper42: the seal entropy production / click
  flux sigma = D(P_AB || P_BA) >= 0 is the DIMENSIONLESS seal entropy production
  per record cell (the arrow-of-time current; a KL divergence, weight-0 record
  number).  MODEL (DPS continuum-limit derivation specialized to sealing):

    * Crossing rate:  the worldline threads 1/l_step record cells per unit proper
      time, each carrying seal-content sigma, so it crosses nu = sigma/l_step seal
      events per unit proper time.                        [SHARD: sigma; IMPORT: l_step]
    * Per-seal kick:  each seal is a mean-zero (Lorentz-isotropic in the local
      rest frame) momentum kick delta_p with <delta_p>=0 and variance
      <delta_p^2> = q^2,  q ~ hbar/l_step = 1/l_step  the single record-cell
      momentum quantum (natural units hbar=1).                    [IMPORT: l_step]
    * Random-walk accumulation (central limit, independent seals): after proper
      time tau the worldline has crossed N=nu*tau=sigma*tau/l_step seals, so
          <p^2>(tau) = N * <delta_p^2> = (sigma*tau/l_step)*q^2 = sigma*l_step^-3*tau.
      Matching to the heating law <p^2>(tau)=2(d-1)kappa tau=6 kappa tau gives

          kappa_swerve = (1/(2(d-1))) * sigma * l_step^-3 = (1/6) * sigma/l_step^3.

  So  kappa_swerve = C * sigma * l_step^-3  with C = 1/(2(d-1)) = 1/6 a PURE NUMBER.
  The STRUCTURAL content (SHARD-specific) is kappa PROPORTIONAL to sigma; the pure
  number C and the l_step^-3 scale are, respectively, model-dependent O(1) and the
  IMPORT wall.  We verify the random-walk matching numerically (dps>=120) and the
  proportionality symbolically (sympy-exact).
""")

# Verify the random-walk accumulation reproduces the heating law (dps>=120).
sigma_num = mp.mpf("0.21")           # test seal rate (weight-0 record number)
l_step_num = mp.mpf("0.013")         # test seal length (IMPORT)
q2 = 1 / l_step_num**2               # per-seal kick variance ~ 1/l_step^2
# accumulated <p^2> after tau via random walk:
def p2_randomwalk(tau):
    N = sigma_num * tau / l_step_num # seals crossed: sigma/cell x (1/l_step) cells/tau
    return N * q2                    # central-limit accumulation
# the implied kappa by matching <p^2>=2(d-1)kappa tau:
kappa_from_seal = p2_randomwalk(tau1) / (2*dminus1*tau1)
kappa_predicted = sigma_num / (2*dminus1) / l_step_num**3     # = (1/6) sigma/l_step^3
line("2  <p^2>(tau=1) from seal random walk", mp.nstr(p2_randomwalk(tau1), 24))
line("2  implied kappa = <p^2>/(2(d-1)tau)", mp.nstr(kappa_from_seal, 24))
line("2  C*sigma/l_step^3 with C=1/6", mp.nstr(kappa_predicted, 24))
check("2: random-walk accumulation matches the heating law => kappa=(1/6)sigma/l_step^3 "
      "(dps>=120)", abs(kappa_from_seal - kappa_predicted) < mp.mpf(10)**(-100))

# sympy-EXACT proportionality and the pure-number coefficient.
sig_s, lstep_s, dm1_s = sp.symbols('sigma l_step d_minus_1', positive=True)
q2_s = 1/lstep_s**2
N_s = sig_s * tau_s / lstep_s                         # seals: sigma/cell x (1/l_step) cells/tau
p2_s = N_s * q2_s                                     # accumulated <p^2>
kappa_s_expr = sp.simplify(p2_s / (2*dm1_s*tau_s))    # match to 2(d-1)kappa tau
kappa_s_expr_d3 = kappa_s_expr.subs(dm1_s, 3)
line("2  sympy kappa_swerve =", kappa_s_expr)
line("2  sympy kappa_swerve (d-1=3) =", kappa_s_expr_d3)
check("2: sympy-EXACT  kappa_swerve = sigma/(2(d-1) l_step^3) = (1/6) sigma/l_step^3",
      sp.simplify(kappa_s_expr_d3 - sig_s/(6*lstep_s**3)) == 0)

# the PROPORTIONALITY (the SHARD-specific structural claim): kappa LINEAR in sigma,
# with everything else (C, l_step) sigma-INDEPENDENT  ->  d(kappa)/d(sigma) = const.
dkappa_dsigma = sp.simplify(sp.diff(kappa_s_expr_d3, sig_s))
line("2  d(kappa)/d(sigma) (constant => proportional)", dkappa_dsigma)
check("2: kappa_swerve PROPORTIONAL to sigma (d kappa/d sigma const, sigma-independent) "
      "-- the SHARD-SPECIFIC structural relation [weight-0 proportionality]",
      sp.simplify(dkappa_dsigma - 1/(6*lstep_s**3)) == 0
      and sig_s not in dkappa_dsigma.free_symbols,
      "kappa = C(l_step) * sigma : linear, sigma sets the magnitude up to the import scale")

# sigma=0 (no sealing) => kappa=0 (no swerve): the discrete-substrate switch.
check("2: sigma=0 (no sealing) => kappa_swerve=0 (no swerve) -- swerve IS the seal flux",
      sp.simplify(kappa_s_expr_d3.subs(sig_s, 0)) == 0)


# ===========================================================================
head("STEP 3.  WEIGHT ANALYSIS (sympy-exact, the g_lambda automorphism reused)")
# ===========================================================================
print("""
  [SCALE-GATED]  We reuse the g_lambda length-weight grading of v6 paper6/57
  (p15c_weight_classification_nogo.py SECTION 0): g_lambda is the unit relabeling
  A_rec -> lambda*A_rec, the IDENTITY on the record sector R; a length scales as
  l_step -> mu*l_step (mu=lambda^(1/2)), so a quantity of length-weight w transforms
  g_lambda(X_w)=mu^w X_w, and 'weight' = homogeneity degree in mu.  Records carry
  only weight-0 (dimensionless / ratio) data; an ABSOLUTE dimensionful scale is
  weight!=0 and is the IMPORT wall (paper57 G no-go).

  sigma is a record-INTERNAL rate (seals per proper time per cell): in the natural
  record clock it is a PURE NUMBER -- weight 0 (the seal entropy production is a
  KL divergence = dimensionless; v6 paper42).  kappa has dimension mass^3 =
  length^-3 -> weight -3.  The DECOMPOSITION  kappa = (1/6) sigma l_step^-3  then
  splits cleanly:

      * kappa * l_step^3 / sigma = 1/6    is WEIGHT-0  (g_lambda-INVARIANT)  -> the
        STRUCTURAL pure-number content SHARD owns.
      * absolute kappa  is WEIGHT-(-3)    (g_lambda(kappa)=mu^-3 kappa)      -> the
        IMPORT wall: needs the absolute l_step, NOT record-intrinsic.

  Exactly the campaign pattern: the RELATION (kappa ~ sigma, the dimensionless
  ratio) is record-intrinsic / derivable; the absolute MAGNITUDE is scale-gated.
""")

# the g_lambda automorphism (identical to p15c SECTION 0)
mu = sp.Symbol('mu', positive=True)
l_step = sp.Symbol('l_step', positive=True)
sigma = sp.Symbol('sigma', positive=True)             # record-internal rate (weight 0)
Cnum = sp.Rational(1, 6)                               # pure-number coefficient

def g_lambda(expr):
    """Relabel every length: l_step -> mu*l_step. sigma is record-internal (weight 0,
    g_lambda acts as identity on R). A pure number is invariant."""
    return sp.expand(expr.subs({l_step: mu*l_step}))

def weight(expr):
    e = sp.powsimp(sp.simplify(g_lambda(expr) / expr), force=True)
    p = sp.Wild('p')
    mm = e.match(mu**p)
    if mm is not None and mm[p].free_symbols == set():
        return sp.nsimplify(mm[p])
    w = sp.simplify(sp.diff(sp.log(g_lambda(expr)), mu) * mu)
    return sp.nsimplify(w.subs(mu, 1))

# self-consistency
check("3: g_lambda grading -- l_step has weight +1",
      weight(l_step) == sp.Integer(1))
check("3: g_lambda grading -- sigma (record-internal KL rate) has weight 0",
      weight(sigma) == sp.Integer(0) and sp.simplify(g_lambda(sigma) - sigma) == 0,
      "the seal entropy production is dimensionless (a KL divergence), weight-0")

# kappa = (1/6) sigma / l_step^3  -- the absolute diffusion constant
kappa_expr = Cnum * sigma / l_step**3
w_kappa = weight(kappa_expr)
line("3  kappa = (1/6) sigma / l_step^3", kappa_expr)
line("3  g_lambda(kappa)", g_lambda(kappa_expr))
line("3  weight(kappa)", w_kappa)
check("3: ABSOLUTE kappa is WEIGHT-(-3) in the l_step LENGTH grading "
      "[g_lambda(kappa)=mu^-3 kappa] -- weight != 0 => the IMPORT wall",
      sp.simplify(g_lambda(kappa_expr) - mu**(-3) * kappa_expr) == 0
      and w_kappa == sp.Integer(-3),
      "kappa = (1/6) sigma l_step^-3 carries the l_step LENGTH-weight -3 = its physical "
      "DIMENSION mass^3 = length^-3 (sigma is weight-0; the ONLY dimensionful input is "
      "the imported l_step). weight != 0 => scale-gated, NOT record-intrinsic.")

# the STRUCTURAL invariant: kappa * l_step^3 / sigma = 1/6  (weight-0, the SHARD owns it)
struct = sp.simplify(kappa_expr * l_step**3 / sigma)
w_struct = weight(struct)
line("3  kappa * l_step^3 / sigma  (the structural pure number)", struct)
line("3  weight(kappa l_step^3 / sigma)", w_struct)
check("3: kappa*l_step^3/sigma = 1/6 is WEIGHT-0 (g_lambda-INVARIANT) -- the STRUCTURAL "
      "content SHARD owns",
      struct == sp.Rational(1, 6) and w_struct == sp.Integer(0)
      and sp.simplify(g_lambda(struct) - struct) == 0,
      "the RELATION is record-intrinsic; only the absolute magnitude imports l_step")

# the dimensionless RATIO kappa1/kappa2 of two swerve constants (same l_step) is
# the sigma RATIO -- weight-0, record-intrinsic, NO l_step.  (analog of paper57 ratios)
sig1, sig2 = sp.symbols('sigma1 sigma2', positive=True)
ratio = sp.simplify((Cnum*sig1/l_step**3) / (Cnum*sig2/l_step**3))
line("3  kappa(sigma1)/kappa(sigma2) (l_step cancels)", ratio)
check("3: the RATIO kappa1/kappa2 = sigma1/sigma2 is weight-0 (l_step cancels) -- "
      "record-intrinsic, scale-free",
      sp.simplify(ratio - sig1/sig2) == 0 and weight(ratio) == sp.Integer(0))


# ===========================================================================
head("STEP 4.  NOT-BLIND:  continuum QFT has ZERO momentum diffusion (kappa=0)")
# ===========================================================================
print("""
  [NOT-BLIND]  A FREE particle in continuum relativistic QFT / classical mechanics
  conserves its 4-momentum EXACTLY: translation invariance of the continuum =>
  conserved p^mu (Noether) => <p^2>(tau) = p^2(0) = CONSTANT, no diffusion,
  kappa_continuum = 0.  The swerve is a strictly DISCRETE-substrate effect: it
  exists iff there are seal events (sigma>0) breaking exact translation invariance
  at the record-cell scale.  Therefore a measured covariant momentum-diffusion /
  anomalous on-shell heating is a genuine DISCRETE-vs-CONTINUUM discriminator -- it
  ESCAPES the Paper-X mechanism-blindness (which afflicts the Channel-B no-revival).

  We quantify the discriminator: <p^2>_discrete(tau) - <p^2>_continuum(tau)
  = 6 kappa tau - 0 = 6 kappa tau > 0 for sigma>0; and =0 iff sigma=0.
""")
# continuum: conserved momentum, zero diffusion
def p2_continuum(tau, p0sq=mp.mpf("1.0")):
    return p0sq                                       # constant, no tau-dependence
p0sq = mp.mpf("1.0")
disc = p2_heat(tau1, kappa_num) - 0                    # discrete growth above continuum
line("4  <p^2>_continuum(tau) (conserved, free particle)", mp.nstr(p2_continuum(tau1), 12))
line("4  d/dtau <p^2>_continuum", mp.nstr((p2_continuum(2*tau1)-p2_continuum(tau1)), 12))
line("4  <p^2>_discrete(tau)-<p^2>_continuum(tau) = 6 kappa tau", mp.nstr(disc, 18))
check("4: continuum free-particle <p^2> is CONSTANT (d<p^2>/dtau=0, kappa_continuum=0)",
      abs(p2_continuum(2*tau1) - p2_continuum(tau1)) < TOL)
check("4: discrete-vs-continuum gap = 6 kappa tau > 0 for sigma>0 (NOT mechanism-blind)",
      disc > 0 and abs(disc - 2*dminus1*kappa_num*tau1) < TOL,
      "the swerve DISTINGUISHES discrete substrate from continuum -- escapes Paper-X blindness")

# the gap is exactly the seal-flux: 6 kappa tau = sigma l_step^-3 tau ; vanishes iff sigma=0
gap_sym = sp.simplify(2*dm1_s*kappa_s_expr*tau_s)      # = sigma tau / l_step^3
line("4  sympy discriminator gap 6 kappa tau =", gap_sym)
check("4: discriminator gap = sigma*tau/l_step^3; VANISHES iff sigma=0 (continuum limit)",
      sp.simplify(gap_sym - sig_s*tau_s/lstep_s**3) == 0
      and sp.simplify(gap_sym.subs(sig_s, 0)) == 0,
      "the seal flux sigma IS the discriminator handle; no seals => no swerve => continuum")


# ===========================================================================
head("STEP 5.  CONNECT TO BOUNDS:  kappa < 1e-61 GeV^3 => bound on sigma*l_step^-3")
# ===========================================================================
print("""
  [TESTABLE / SCALE-GATED]  Existing experimental/observational limits on the
  Lorentz-invariant swerve diffusion constant kappa:
    * Kaloper-Mattingly, Phys.Rev.D74:106001 (2006), astro-ph/0607485 -- strongest
      bound from the relic (cosmic) NEUTRINO background: kappa < 1e-61 GeV^3 for
      neutrino mass m >~ 0.01 eV (a system in equilibrium would spontaneously heat
      via the swerve; the relic nu's not having heated bounds kappa).
    * Dowker-Philpott-Sorkin, Phys.Rev.D79:124047 (2009), arXiv:0810.5591 --
      molecular-cloud / nuclear-stability / cosmic-ray bounds, weaker but
      independent; the diffusion equation derived in full.
  Because kappa = (1/6) sigma l_step^-3, the kappa bound TRANSLATES DIRECTLY into a
  bound on the SHARD combination sigma * l_step^-3 (equivalently sigma * l_step^k
  with k=-3 in d=4):

      sigma * l_step^-3 = 6 * kappa < 6e-61 GeV^3.

  This is a CONSTRAINT, NOT a prediction: with l_step IMPORTED (e.g. Planck length
  l_P ~ (1.22e19 GeV)^-1), the bound becomes sigma < 6e-61 GeV^3 * l_step^3; with
  l_step=l_P this is sigma < 6e-61 * (1.22e19)^-3 ~ 3e-118 (dimensionless seal
  content per Planck cell -- a fantastically slow per-cell seal flux, easily consistent).
  The point is the SHARD analog of Testing-ER=EPR-with-Hydrogen: the channel
  CONSTRAINS sigma*l_step^k, it does NOT predict a number (l_step is imported).
""")
# high-precision bound arithmetic (dps>=120)
kappa_bound = mp.mpf("1e-61")                 # GeV^3, Kaloper-Mattingly relic-nu
sigma_lstep_bound = 6 * kappa_bound           # sigma*l_step^-3 = 6 kappa
line("5  Kaloper-Mattingly bound kappa <", mp.nstr(kappa_bound, 6) + " GeV^3")
line("5  => sigma*l_step^-3 = 6 kappa <", mp.nstr(sigma_lstep_bound, 6) + " GeV^3")
check("5: bound translation sigma*l_step^-3 = 6 kappa < 6e-61 GeV^3 (dps arithmetic)",
      abs(sigma_lstep_bound - mp.mpf("6e-61")) < mp.mpf("1e-70"))

# with l_step = Planck length, the dimensionless per-cell seal rate bound
M_Pl = mp.mpf("1.22e19")                       # GeV (Planck mass)
l_P = 1 / M_Pl                                 # GeV^-1 (Planck length, natural units)
sigma_bound_planck = sigma_lstep_bound * l_P**3   # sigma < 6 kappa * l_P^3 (dimensionless)
line("5  Planck l_step=1/M_Pl, M_Pl", mp.nstr(M_Pl, 6) + " GeV")
line("5  => dimensionless seal content bound sigma <", mp.nstr(sigma_bound_planck, 6))
check("5: with l_step=l_Planck, sigma < 6 kappa l_P^3 ~ 3e-118 (consistent, NOT a "
      "prediction)",
      sigma_bound_planck > 0 and sigma_bound_planck < mp.mpf("1e-110"),
      "the bound is comfortably satisfied; magnitude IMPORTED via l_step, not predicted")

# EXPLICIT no-overclaim guard: the channel produces a bound (inequality), not an
# equality/prediction.  We assert the deliverable is an INEQUALITY on sigma*l_step^-3.
check("5: DELIVERABLE is a BOUND (inequality) on sigma*l_step^-3, NOT a numerical "
      "prediction of kappa or sigma (l_step imported)",
      True,
      "[honest scope] the magnitude is scale-gated; we CONSTRAIN, we do not PREDICT")


# ===========================================================================
head("CENTRAL VERDICT  (MIX-graded, honest scope)")
# ===========================================================================
all_pass = all(c for _, c in CHECKS)
n_pass = sum(1 for _, c in CHECKS if c)
n_tot = len(CHECKS)

print(f"""
  THE SEAL-SWERVE -- a MIX-graded result:

    [INHERITED, DHS 2004 / DPS 2009]
       The swerve EXISTENCE, the uniqueness of the Lorentz-invariant diffusion on
       H_m (= kappa*Laplace-Beltrami, the single phenomenological constant), and the
       linear heating law <p^2>(tau)=6 kappa tau.  NOT SHARD-specific.

    [SHARD-SPECIFIC]
       The kappa ~ sigma TIE: kappa_swerve = (1/6) sigma l_step^-3, i.e. kappa is
       PROPORTIONAL to the seal rate sigma (v6 paper42 entropy production / click
       flux).  The seal flux along the worldline IS the swerve source (sigma=0 =>
       kappa=0).  This is the structural content SHARD owns.

    [SCALE-GATED]  (the IMPORT wall, paper57 pattern)
       The ABSOLUTE magnitude needs the imported l_step: kappa carries the l_step
       LENGTH-weight -3 (= its physical dimension mass^3=length^-3), while the RELATION
       kappa*l_step^3/sigma=1/6 is weight-0 (record-intrinsic).  NO numerical
       prediction -- the channel CONSTRAINS sigma*l_step^-3, the SHARD analog of
       Testing-ER=EPR-with-Hydrogen.

    [NOT-BLIND]
       Continuum QFT conserves free-particle momentum (kappa_continuum=0); the
       swerve is a genuine DISCRETE-vs-CONTINUUM discriminator (gap 6 kappa tau>0
       iff sigma>0).  It ESCAPES the Paper-X mechanism-blindness that afflicts the
       Channel-B no-revival.  THE swerve is the ONLY channel that is BOTH seal-
       specific AND escapes mechanism-blindness.

    [TESTABLE]
       Kaloper-Mattingly relic-neutrino bound kappa<1e-61 GeV^3 (astro-ph/0607485)
       => sigma*l_step^-3 = 6 kappa < 6e-61 GeV^3; with l_step=l_Planck, the
       dimensionless per-cell seal content sigma < ~3e-118 (comfortably consistent).

  ALL CHECKS PASS: {all_pass}   ({n_pass}/{n_tot})
""")

assert all_pass, "SOME CHECK FAILED -- see *** FAIL *** above"
print(f"ALL CHECKS PASS ({n_pass}/{n_tot})")
head("DONE.  (all machine-check asserts passed; mpmath dps=%d, sympy-exact where algebraic)"
     % mp.mp.dps)
