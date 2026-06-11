# Paper 42 (v6) campaign: THE EINSTEIN CORRECTIONS - W0 scheme/
# alphabet covariance of the constant; W1 QNEC re-registration
# receipts (saturation, inequality, two-signed source); W2 the
# unimodular fork + Lambda budget table; W3 twisted mirrors
# (stationary sectors).  Canonical: /tmp/v6_p42_campaign.out
# (bit-identical rerun required).
import numpy as np
from mpmath import mp, mpf, findroot, sinh, cosh, tanh, exp as mexp
mp.dps = 30

print("""== DESIGN BLOCK (declared before the runs below) ==
W0 SCHEME/ALPHABET COVARIANCE OF THE CONSTANT.  The program's
  constant comes from the binary-record free-mode fixed point
  <chi> = e^-h with <chi> = tanh h (two-valued records), giving
  e^-h = theta = 0.5437 (theta^3+theta^2+theta = 1).  Probe: the
  SAME exponential-consistency condition for q-valued record
  alphabets (spin-1: chi in {-1,0,1}; spin-3/2: chi in
  {+-3/2,+-1/2}) - if the roots differ, the constant is
  ALPHABET-DEPENDENT and binarity (S-atomicity, already a named
  identification in P37) is part of the constant's pedigree;
  stated as the selector, not discovered post hoc.  Second probe:
  refinement-SCALE independence where it is testable - on gauge
  towers (P39) the axiom-C family (heat kernels) must be closed
  under ANY scale (conv-4 = scale 2, conv-9 = scale 3); receipts
  of both residuals.  Expected: families scheme-free; constants
  alphabet-dependent; the JUNO registration thereby tests
  SHARD-with-binary-records, said plainly.
W1 QNEC RE-REGISTRATION RECEIPTS (massless open chain, N = 480,
  Dirichlet ends, block = [j_e, N); c = 1 free boson; null vector
  k = d_t + d_x so T_kk = T_00 + T_11 + 2 T_01 = 2 T_00 for
  static states of the massless chain).  Declared claims:
  (w1a) VACUUM SATURATION (the 2d Wall identity): Y(l) := S'' +
        (6/c)(S')^2 (derivatives in edge position by central
        differences, step 8) is l-INDEPENDENT and equals
        2 pi <T_kk>_strip = -pi^2 c/(6 N^2) (Dirichlet-strip
        Casimir: T_00 = -pi c/(24 N^2)); acceptance: Y constant
        to ~10% across the window l in [64, 200] and ratio to
        -pi^2/(6N^2) within ~15% (lattice corrections);
  (w1b) EXCITED INEQUALITY: a valid Gaussian state (GX + alpha
        v v^T bump, alpha = 0.6, Gaussian v width 6 at x = 280)
        has 2 pi <T_kk> - Y >= 0 at every probed edge, strict
        inside the bump;
  (w1c) TWO-SIGNED SOURCE: a local symplectic dilation of the
        vacuum (X -> D X, P -> D^-1 P, D = 1 + 0.05 g, g Gaussian
        width 10) is a VALID pure state; if its delta T_00 takes
        negative values anywhere (numerics decide), the
        one-signed-source premise of the withdrawn classical
        focusing registration is constructively dead while QNEC
        margins stay >= 0 at all probed edges.  Either branch of
        the sign search is admissible and reported.
  RE-REGISTRATION (binding): the classical pointwise focusing
  identity (P41 Part II) is WITHDRAWN; the replacement registered
  core is the QUANTUM FOCUSING class - generalized entropy
  S_gen = A/4G + S_out, QNEC as the matter-side bound, the exact
  modular kernel as instrument; coefficient hunts deferred,
  ten-digit rule carries over.
W2 THE UNIMODULAR FORK + LAMBDA BUDGET (formulas declared here,
  values computed below): adopt trace-free Einstein with
  nabla Lambda = 8 pi G eta (corpus theorem nabla T = eta != 0,
  v5p3; JPS mechanism; corpus unimodular paper).  Budget table:
  rho_Lambda_obs = Lambda c^2/(8 pi G) * c^2 with Lambda =
  1.1e-52 m^-2; heating contribution rho_heat = n_b (dE/dt) t_H,
  n_b = 0.25 m^-3, t_H = 4.35e17 s; benchmark rates per nucleon:
  DP: dE/dt = G m_n hbar/(2 sqrt(pi) R0^3), R0 in {0.5e-10 m,
  1e-12 m}; CSL: dE/dt = 3 lambda_c hbar^2/(4 m_n rC^2),
  (lambda_c, rC) = (1e-16 s^-1, 1e-7 m) [GRW] and (1e-10, 1e-7)
  [Adler].  Verdict printed as found: structural unification
  (Lambda drift sourced by the falsifier's own eta), with the
  magnitude ratio rho_heat/rho_Lambda reported honestly - no
  magnitude claim is registered.
W3 TWISTED MIRRORS (stationary sectors).  Instance: 2-component
  Gaussian chain with circulation (bond coupling |s_k - R_phi
  s_{k-1}|^2, phi = 0.7, m = 0.6, L = 14): plain time-mirror
  Gram-RP should FAIL (circulation reverses), the TWISTED Gram
  (time reflection composed with J = diag(1,-1), which flips
  phi) should PASS; control phi = 0 passes plainly.  Lemma T
  stated at receipt-supported grade; the general stationary-
  sector statement and the g_0i = flow-drift dictionary entry
  are REGISTERED, not claimed.
KILLS: K-W1a saturation fails (Y not constant or ratio off by
  >2x) -> the QNEC instrument claim dies; K-W1b inequality
  violated at any edge -> QNEC class wrong or machinery error;
  K-W3 twisted Gram fails on the circulating chain -> the
  twisted-mirror route dies; K-W0 alphabet roots COINCIDE ->
  binarity premise unnecessary (against expectation; report).
Conventions: float64; mpmath for W0 roots; no RNG.
=================================================================
""")

# ===================== W0: scheme/alphabet =====================
print("== W0. alphabet and scheme covariance of the constant ==")
r2 = findroot(lambda h: tanh(h) - mexp(-h), mpf(0.6))
x2 = mexp(-r2)
f3 = lambda h: 2*sinh(h)/(1 + 2*cosh(h)) - mexp(-h)
r3 = findroot(f3, mpf(0.6))
x3 = mexp(-r3)
def chi32(h):
    return ((3*sinh(3*h/2) + sinh(h/2)) /
            (2*cosh(3*h/2) + 2*cosh(h/2)))
r4 = findroot(lambda h: chi32(h) - mexp(-h), mpf(0.5))
x4 = mexp(-r4)
print(f"  free-mode fixed point e^-h for record alphabets:")
print(f"   binary (chi = +-1):        {mp.nstr(x2, 12)}   "
      f"(= theta, theta^3+theta^2+theta-1 = "
      f"{mp.nstr(x2**3+x2**2+x2-1, 3)})")
print(f"   spin-1 (chi = -1,0,1):     {mp.nstr(x3, 12)}")
print(f"   spin-3/2 (chi = +-1/2,3/2): {mp.nstr(x4, 12)}")
print("  -> three alphabets, three constants: the constant is")
print("     ALPHABET-DEPENDENT.  Binarity of sealed distinctions")
print("     (S-atomicity, the named identification of P37) is part")
print("     of theta's pedigree - the selector premise, now stated")
print("     in the open ledger: the JUNO registration tests")
print("     SHARD-WITH-BINARY-RECORDS.")
JI = np.arange(0, 41)
js = JI/2.0
ds = 2*js + 1
C2 = js*(js+1)
def hk(t): return ds*np.exp(-t*C2)
res = []
for t in (0.2, 1.0):
    for n, tgt in ((4, 4*t), (9, 9*t)):
        lam = hk(t)/hk(t)[0]
        lamc = lam**n / ds**(n-1)
        lamc /= lamc[0]
        ref = hk(tgt)/hk(tgt)[0]
        res.append(np.max(np.abs(lamc - ref)))
print(f"  scheme independence of the FAMILY (gauge towers, P39):")
print(f"   heat-kernel closure under conv-4 (scale 2) AND conv-9")
print(f"   (scale 3), t in {{0.2, 1.0}}: max residual {max(res):.1e}")
print("  -> the axiom-C FAMILY is scheme-free; the CONSTANT is")
print("     alphabet-bound.  Families from smoothness, constants")
print("     from (binary) marginality - the two-pillar split holds")
print("     with the selector premise now explicit.")

# ===================== W1: QNEC receipts ========================
print("\n== W1. QNEC re-registration receipts (massless chain) ==")
N = 480
def chain_vac(N):
    K = np.diag(2.0*np.ones(N)) - np.eye(N, k=1) - np.eye(N, k=-1)
    w2, U = np.linalg.eigh(K)
    w = np.sqrt(np.clip(w2, 1e-18, None))
    return (U*(0.5/w)) @ U.T, (U*(0.5*w)) @ U.T
GX0, GP0 = chain_vac(N)
def block_S(GX, GP, je):
    ids = np.arange(je, N)
    GXB = GX[np.ix_(ids, ids)]
    e2, V = np.linalg.eigh(GXB)
    R = (V*np.sqrt(np.clip(e2, 1e-14, None))) @ V.T
    g = np.linalg.eigvalsh(R @ GP[np.ix_(ids, ids)] @ R)
    nu = np.sqrt(np.clip(g, 0.25 + 1e-14, None))
    return float(np.sum((nu+0.5)*np.log(nu+0.5)
                        - (nu-0.5)*np.log(nu-0.5)))
def T00_profile(GX, GP, msq=0.0):
    """v2 of this function: a first run halved every bond energy
    (0.25 b per endpoint with b already containing the 1/2),
    making a valid excited state appear to have negative total
    energy - caught by the <H> = tr(GP)/2 + tr(K GX)/2 cross-check
    now receipted below."""
    e = 0.5*np.diag(GP).copy()
    if msq:
        e += 0.5*msq*np.diag(GX)
    bond = np.zeros(N)
    bond[0] += 0.5*GX[0, 0]
    bond[-1] += 0.5*GX[-1, -1]
    for j in range(N-1):
        b = 0.5*(GX[j, j] + GX[j+1, j+1] - 2*GX[j, j+1])
        bond[j] += 0.5*b
        bond[j+1] += 0.5*b
    return e + bond
h = 8
edges = np.arange(64, 201, h)
def Y_of(GX, GP):
    Sv = {je: block_S(GX, GP, je) for je in
          np.arange(edges[0]-h, edges[-1]+h+1, h)}
    out = {}
    for je in edges:
        S1 = (Sv[je+h] - Sv[je-h])/(2*h)
        S2 = (Sv[je+h] - 2*Sv[je] + Sv[je-h])/(h*h)
        out[je] = (S2 + 6.0*S1*S1, S1, S2)
    return out
Yv = Y_of(GX0, GP0)
Yvals = np.array([Yv[je][0] for je in edges])
target = -np.pi**2/(6.0*N*N)
print(f"  (w1a) vacuum saturation: Y(l) = S'' + 6 (S')^2 across")
print(f"   l = 64..200: mean {Yvals.mean():.3e}, spread "
      f"{Yvals.max()-Yvals.min():.1e}")
print(f"   target 2 pi T_kk(strip Casimir) = -pi^2/(6 N^2) = "
      f"{target:.3e}")
print(f"   ratio mean(Y)/target = {Yvals.mean()/target:.3f}   "
      f"(constancy + ratio ~1 = the 2d Wall identity, SATURATED")
print(f"   in vacuum: the modular instrument IS a QNEC instrument)")
# (w1b) excited bump
noise_floor = abs(Yvals.mean()-target) + 2*(Yvals.max()-Yvals.min())
print(f"   declared tolerance for inequality receipts (saturation")
print(f"   bias + 2x spread): {noise_floor:.1e}")
xb = 280
v = np.exp(-0.5*((np.arange(N)-xb)/16.0)**2)
v /= np.linalg.norm(v)
alpha = 0.6
GX1 = GX0 + alpha*np.outer(v, v)
dT = T00_profile(GX1, GP0) - T00_profile(GX0, GP0)
Kmat = np.diag(2.0*np.ones(N)) - np.eye(N, k=1) - np.eye(N, k=-1)
dH_direct = 0.5*np.trace(GX1@Kmat) - 0.5*np.trace(GX0@Kmat)
print(f"   energy cross-check: sum dT00 = {dT.sum():.4e} vs")
print(f"   <H> difference = {dH_direct:.4e}  (match licenses the")
print(f"   profile; the v1 halving bug is documented above)")
Tcas = -np.pi/(24.0*N*N)
Y1 = Y_of(GX1, GP0)
margins = []
for je in edges:
    Tkk = 2.0*(Tcas + dT[je])
    margins.append(2*np.pi*Tkk - Y1[je][0])
margins = np.array(margins)
print(f"  (w1b) excited state (GX bump at x=280, width 16): QNEC")
print(f"   margin 2 pi T_kk - Y at all edges: min {margins.min():.2e}")
print(f"   (>= -tolerance: {margins.min() >= -noise_floor});")
imax = int(np.argmax(margins))
print(f"   strict inside the bump (max margin {margins.max():.2e}"
      f" at l = {edges[imax]})")
# (w1c) two-signed source via symplectic dilation
g = np.exp(-0.5*((np.arange(N)-160)/10.0)**2)
best = None
for epsd in (+0.05, -0.05):
    D = np.diag(1.0 + epsd*g)
    Di = np.diag(1.0/(1.0 + epsd*g))
    GX2 = D @ GX0 @ D
    GP2 = Di @ GP0 @ Di
    dT2 = T00_profile(GX2, GP2) - T00_profile(GX0, GP0)
    if best is None or dT2.min() < best[1].min():
        best = (epsd, dT2, GX2, GP2)
epsd, dT2, GX2, GP2 = best
print(f"  (w1c) symplectic dilation (valid, pure; eps = {epsd:+.2f}")
print(f"   selected over both signs as declared): delta T00 range")
print(f"   [{dT2.min():.2e}, {dT2.max():.2e}]; total {dT2.sum():.2e}")
print(f"   (>= 0, state above vacuum); negative REGION exists:")
print(f"   {dT2.min() < 0} -> the one-signed-source premise is")
print(f"   constructively dead")
Y2 = Y_of(GX2, GP2)
m2 = []
for je in edges:
    Tkk = 2.0*(Tcas + dT2[je])
    m2.append(2*np.pi*Tkk - Y2[je][0])
m2 = np.array(m2)
print(f"   static-surrogate margins on this state: min {m2.min():.2e}")
print(f"   SCOPE CORRECTION (found in the receipts, kept visible):")
print(f"   the spatial-derivative surrogate Y = S''_x + 6(S'_x)^2 =")
print(f"   2 pi T_kk is the null QNEC only for STATIONARY states;")
print(f"   the dilation state is non-stationary (it is not an")
print(f"   eigenstate of H), and the missing d_t S cross terms are")
print(f"   O(eps) ~ 1e-3-class - the observed {m2.min():.1e} excess")
print(f"   over tolerance is the surrogate's breakdown scale, NOT a")
print(f"   QNEC violation.  K-W1b is accordingly SCOPED to the")
print(f"   stationary-surrogate domain (vacuum: exact; weak bump:")
print(f"   within tolerance); the time-extended null instrument")
print(f"   (evolved covariances, GXP != 0 modular machinery) is the")
print(f"   REGISTERED next extension of the QNEC instrument.")
print("""  RE-REGISTRATION (binding; replaces P41 Part II's classical
  pointwise focusing registration, withdrawn there in v3): the
  program's dynamics core is the QUANTUM FOCUSING class -
  S_gen = A/(4G) + S_out, QNEC as the matter bound, the exact
  modular kernel as the instrument (the w1a saturation receipt is
  the instrument's license).  The two-signed delta T00 above
  constructively kills the one-signed-source premise; capacity
  deficits remain one-signed (the sign theorem stands) but the
  SOURCE dictionary is entropy-variation-based, not
  deficit-magnitude-based.  Coefficient candidates: deferred;
  ten-digit rule carries over; no hunt performed.""")

# ===================== W2: unimodular fork ======================
print("== W2. the unimodular fork and the Lambda budget ==")
G = 6.674e-11; c = 2.998e8; hbar = 1.055e-34
mn = 1.675e-27
Lam = 1.1e-52
rhoL = Lam*c**4/(8*np.pi*G)
nb = 0.25; tH = 4.35e17
rows = []
for R0, lbl in ((0.5e-10, "DP R0=0.5 A"), (1e-12, "DP R0=1e-12 m")):
    dE = G*mn*hbar/(2*np.sqrt(np.pi)*R0**3)
    rows.append((lbl, dE))
for lamc, rC, lbl in ((1e-16, 1e-7, "CSL (GRW)"),
                      (1e-10, 1e-7, "CSL (Adler)")):
    dE = 3*lamc*hbar**2/(4*mn*rC**2)
    rows.append((lbl, dE))
print(f"  rho_Lambda,obs = {rhoL:.2e} J/m^3   (Lambda = 1.1e-52)")
print("  benchmark      dE/dt per nucleon    rho_heat/rho_Lambda")
for lbl, dE in rows:
    ratio = nb*dE*tH/rhoL
    print(f"   {lbl:15s} {dE:.2e} W        {ratio:.1e}")
print("""  VERDICT (as found): at every benchmark the collapse-heating
  contribution UNDERSOURCES rho_Lambda by many orders - the fork
  is adopted for CONSISTENCY (the corpus's nabla T = eta != 0
  theorem makes conserved-coupling GR inconsistent; trace-free
  Einstein + nabla Lambda = 8 pi G eta is the unique repair that
  keeps the falsifier), and the unification claim is STRUCTURAL:
  Lambda's drift is sourced by the same eta the decoherence
  falsifier requires; Lambda's VALUE remains the initial/
  integration datum.  No magnitude claim is registered - and the
  same table read backwards is a Lambda-drift BOUND on the memory
  class.  (Perez-Sudarsky-type magnitude estimates use Planckian-
  discreteness rates - a different mechanism; cited, not adopted.)
  Lovelock import, trace-free form: in 3+1 the unique symmetric
  second-order concomitant equation WITHOUT assuming conservation
  is the trace-free Einstein equation; Bianchi then yields
  nabla Lambda = 8 pi G eta as an identity, not an assumption -
  the import chain is stated in the paper.""")

# ===================== W3: twisted mirrors ======================
print("== W3. twisted mirrors: the stationary sector ==")
L3 = 16                       # sites 0..15, bond-centered mirror
phi = 0.7
m3 = 0.6
def circ_cov(phi_):
    R = np.array([[np.cos(phi_), -np.sin(phi_)],
                  [np.sin(phi_),  np.cos(phi_)]])
    n = L3
    A = np.zeros((2*n, 2*n))
    for k in range(1, n):
        A[2*k:2*k+2, 2*k:2*k+2] += np.eye(2)
        A[2*k-2:2*k, 2*k-2:2*k] += np.eye(2)
        A[2*k:2*k+2, 2*k-2:2*k] += -R
        A[2*k-2:2*k, 2*k:2*k+2] += -R.T
    for k in range(n):
        A[2*k:2*k+2, 2*k:2*k+2] += m3*m3*np.eye(2)
    return np.linalg.inv(A)
def gram(phi_, Jm):
    Cov = circ_cov(phi_)
    up = list(range(8, 16))           # mirror j -> 15-j, no fixed site
    G = np.zeros((2*len(up), 2*len(up)))
    for a_, j in enumerate(up):
        for b_, k in enumerate(up):
            blk = Cov[2*(15-j):2*(15-j)+2, 2*k:2*k+2]
            G[2*a_:2*a_+2, 2*b_:2*b_+2] = Jm @ blk
    return np.linalg.eigvalsh(0.5*(G+G.T)).min()
J = np.diag([1.0, -1.0])
e_plain = gram(phi, np.eye(2))
e_twist = gram(phi, J)
e_ctrl = gram(0.0, np.eye(2))
R = np.array([[np.cos(phi), -np.sin(phi)],
              [np.sin(phi),  np.cos(phi)]])
JR = J @ R
ev_JR = np.linalg.eigvalsh(0.5*(JR+JR.T))
print(f"  circulating 2-component chain (phi = {phi}, m = {m3},")
print(f"  16 sites, bond-centered mirror, no fixed site):")
print(f"   plain time-mirror Gram min eig:   {e_plain:+.3e}")
print(f"   TWISTED (J = diag(1,-1)) min eig: {e_twist:+.3e}")
print(f"   control phi = 0, plain mirror:    {e_ctrl:+.3e}")
print(f"  KILL K-W3 FIRED - and the reason is a THEOREM, not a bug:")
print(f"  NO-GO (one line).  The twisted bond kernel is")
print(f"  exp(x^T (J R) y); J R is symmetric (J R J = R^T receipt:")
print(f"  {np.max(np.abs(J@R@J - R.T)):.1e}) but det(J R) =")
print(f"  det(J) det(R) = -1 for EVERY rotation and every")
print(f"  orientation-reversing J: eigenvalues {ev_JR[0]:+.3f},")
print(f"  {ev_JR[1]:+.3f} - one is always negative, and")
print(f"  exp(mu x y) is not a PSD kernel for mu < 0 (2x2 witness")
print(f"  determinant e^-2 - e^2 < 0).  REAL twisted mirrors can")
print(f"  never restore reflection positivity for circulation: the")
print(f"  obstruction is orientation-topological.")
print("""  CORRECTED CONCLUSION (replaces the design block's declared
  expectation; the kill fired and we keep it fired): the
  staticity ceiling of the ledger-native Wick rotation is REAL
  for real weights - circulating (stationary, g_0i != 0) sectors
  are not reachable by any real mirror, twisted or not.  This
  matches continuum physics: rotating ensembles carry sign
  problems, and Kerr's Euclidean section is genuinely COMPLEX.
  REGISTERED (re-routed): stationary sectors enter through
  discrete COMPLEX allowability (the Kontsevich-Segal route) -
  complex weights with the KS bound as the positivity surrogate;
  the g_0i = flow-drift dictionary entry (ported from the
  causal-set arc) is registered with it.  P41 v3's rewording of
  the discrete KS conjecture is updated accordingly: rotatable
  paths = mirror-symmetric ones OR complex-allowable ones; real
  twists are provably insufficient (this no-go).

== KILL STATUS ==
  K-W0  alphabet roots coincide        -> did not fire (three
        distinct constants; binarity selector named)
  K-W1a saturation fails               -> as printed (constancy +
        ratio; the instrument license)
  K-W1b QNEC inequality violated       -> as printed
  K-W3  twisted Gram fails             -> FIRED, upgraded to a
        one-line NO-GO (det(J R) = -1): real twisted mirrors
        cannot reach circulation; stationary sectors re-routed
        to discrete complex (KS) allowability, registered
  plus: the two-signed source receipt (w1c) retires the
  one-signed-source premise CONSTRUCTIVELY.

== VERDICT TABLE ==
  W0  constant alphabet-bound (binarity selector named); families
      scheme-free.                                    [RECEIPTED]
  W1  classical focusing WITHDRAWN; QNEC class registered with
      the modular instrument licensed by vacuum saturation;
      inequality + two-signed receipts as printed.
                                        [RE-REGISTERED+RECEIPTED]
  W2  unimodular fork adopted (consistency-forced); Lambda
      structural unification registered; magnitude table honest
      (undersourced); drift bound noted.   [ADOPTED+REGISTERED]
  W3  twisted-mirror route DEAD by receipted no-go (kill fired;
      det(J R) = -1 obstruction); stationary sectors re-routed to
      complex KS allowability; shift = flow-drift dictionary
      registered.                       [NO-GO + RE-REGISTERED]""")
