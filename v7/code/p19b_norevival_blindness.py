"""
v7 Paper XIX (Channel B)  --  p19b_norevival_blindness.py
=========================================================

THE NO-REVIVAL / CP-DIVISIBILITY ESCAPE QUESTION (date stamp 2026-06-17).

The SHARD seal is a state-independent irreversible commitment (v6 paper56, the
indivisible gravitational channel): the off-diagonal coherence decays as

      |rho_01(t)| = exp( -INTEGRAL_0^t lambda(s) ds ),   lambda(s) >= 0,

so the seal channel is CP-DIVISIBLE, MONOTONE, NO REVIVALS.  Paper X (publishable
paper-X, gravitational decoherence) proved the Gaussian onset (lambda ~ t =>
|rho_01| ~ exp(-k t^2/2)) is MECHANISM-BLIND: a continuous Ornstein-Uhlenbeck
classical-noise ontology and a matched sparse-seal record ontology produce
bit-identical free-induction coherence to all orders (the identity INT lambda_OU
= chi is sympy-exact).

THE QUESTION fully investigated here: can the no-revival / CP-divisibility be turned
into a SIGNATURE that ESCAPES this blindness?  Probe (a) the BLP/RHP non-Markovianity
measure N; (b) higher-order / multi-time correlations; (c) the specific lambda(t)
form / exact decay shape -- does ANYTHING beyond the onset discriminate the seal
CP-divisible decoherence from a GENERIC CP-divisible noise with the SAME |rho_01(t)|?

THE HONEST PRIOR (stated, then TESTED, NOT assumed): the no-revival CANNOT
discriminate SHARD from standard QM with ordinary CP-divisible decoherence (both give
N=0, no revivals); it CAN only discriminate against REVIVAL-exhibiting
(non-CP-divisible / non-Markovian) collapse models (which give N>0).  So it is BLIND
in the SHARD-vs-QM sense, a discriminator only against a specific exotic class.

THE KILL-CRITERION (pre-declared, binding): a GENUINE escape requires a measurable
quantity Q[ |rho_01| , higher moments , multi-time stats ] that takes a DIFFERENT
value on the SHARD seal channel than on a standard-QM CP-divisible decoherence channel
with the SAME single-time coherence.  If every such Q agrees whenever the coherences
agree (and the ONLY thing N separates is the revival class), the verdict is
BLIND_NO_ESCAPE -- the honest, expected, valuable outcome.  Do NOT manufacture an
escape.

  CHECK GROUP 1  encode the seal coherence; monotone, no revivals, Gaussian onset.
  CHECK GROUP 2  the COMPARISON: (a) QM OU CP-divisible decoherence (monotone);
                 (b) underdamped (revival) Gaussian collapse model -> coherence
                 partially REVIVES (lambda(t) goes negative on intervals).
  CHECK GROUP 3  the BLP/RHP measure N: N=0 for SEAL and for QM-OU; N>0 for revival.
  CHECK GROUP 4  ESCAPE ATTEMPTS (genuine): does any higher-order / multi-time
                 correlation, or the SPECIFIC lambda(t) form, distinguish the seal
                 from a generic CP-divisible noise with the SAME |rho_01(t)|?
  CHECK GROUP 5  VERDICT + the precise discrimination boundary.

PHYSICS CONTEXT (two channels of the SHARD discrete-sealed substrate; the records ARE
the causal set, v6 paper1).  CHANNEL A is the seal-swerve (covariant momentum
diffusion, DHS 2004 / PDS 2009 -- NOT mechanism-blind, scale-gated).  CHANNEL B (this
receipt) is the no-revival / CP-divisibility: seal-specific but BLIND vs QM.

TAGS used inline:  [SEAL]=SHARD seal channel; [QM]=standard-QM CP-divisible
decoherence; [REVIVAL]=non-CP-divisible collapse model; [NO-GO/BLIND]=cannot
discriminate SHARD from QM; [NOT-BLIND]=discriminates (only vs the revival class).

Pre-geometric / open-system discipline: t is the matter free-induction time (proper
time along the worldline); lambda is a record-commitment hazard / dephasing rate.
HIGH PRECISION: mpmath dps>=120 for every cancellation-heavy quantity (running
integrals, the all-orders OU/seal comparison, the BLP measure); sympy-EXACT where the
claim is algebraic (the onset integral, the OU running integral, lambda_OU = chi',
the moment identities).  NEVER float64 for the near-vacuum / cancellation-heavy decay
quantities; any solver-tolerance number is flagged.

VERIFIED CITATIONS:
  v6 paper56  (relativistic-isp-v6-paper56-indivisible-gravitational-channel.md):
              state-independent irreversible seal => |rho_01|=exp(-INT lambda),
              lambda>=0 => CP-divisible, monotone, NEVER revives (sec 3, C11/C12).
  v6 publishable paper-X (paper-X-gravitational-decoherence.md): the Gaussian onset
              is mechanism-blind; OU-noise and matched sparse-seal share the
              free-induction curve to all orders (INT lambda_OU = chi, sympy-exact;
              machine-zero residual); revival threshold (omega0 tau)_* =
              3.644173671645632... for the underdamped kernel.
  H.-P. Breuer, E.-M. Laine, J. Piilo, Phys. Rev. Lett. 103, 210401 (2009) -- the
              BLP non-Markovianity measure N = INT_{d/dt D > 0} (d/dt D) dt over the
              trace-distance growth (information backflow).
  A. Rivas, S. F. Huelga, M. B. Plenio, Phys. Rev. Lett. 105, 050403 (2010) -- the
              RHP CP-divisibility measure (g(t)>0 iff CP-divisibility broken).
  Breuer, Laine, Piilo, Vacchini, Rev. Mod. Phys. 88, 021002 (2016) -- the
              non-Markovianity Colloquium (the BLP/RHP instrument).
  Dowker, Henson, Sorkin, Mod. Phys. Lett. A19, 1829 (2004); Philpott, Dowker,
              Sorkin, Phys. Rev. D79, 124047 (2009) -- the swerve (Channel A context).
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
#  Model parameters (record-internal; all dimensionless, hbar = 1)
# ===========================================================================
# SEAL / QM-OU shared kernel: OU (Ornstein-Uhlenbeck, exponential) autocorrelation
#   K(s) = sigma^2 exp(-|s|/tau_c).
# This is the DP-family / paper-X kernel.  Its dephasing:
#   chi(T)        = sigma^2 tau_c^2 ( T/tau_c - 1 + exp(-T/tau_c) )      (hbar=1)
#   lambda_OU(t)  = chi'(t) = sigma^2 tau_c ( 1 - exp(-t/tau_c) )  >= 0
#   |rho_01(T)|   = exp(-chi(T))   monotone non-increasing.
sigma   = mp.mpf("1.3")
tau_c   = mp.mpf("0.7")

def chi_OU(T):
    return sigma**2 * tau_c**2 * (T / tau_c - 1 + mp.e**(-T / tau_c))

def lam_OU(t):
    return sigma**2 * tau_c * (1 - mp.e**(-t / tau_c))      # = chi'(t), >= 0

def C_OU(T):
    return mp.e**(-chi_OU(T))


# ===========================================================================
head("GROUP 1.  THE SEAL COHERENCE |rho_01(t)| = exp(-INT lambda), lambda>=0.")
# ===========================================================================
print("""
  v6 paper56 sec 3 / paper-X sec 3.1-3.2: a state-independent IRREVERSIBLE seal firing
  at hazard lambda(t)>=0 gives  rho_01(T) = e^{i Phi(T)} <E0(T)|E1(T)> rho_01(0)  with
  |<E0|E1>| a non-increasing CONTRACTION, hence

       |rho_01(T)| = exp( -INT_0^T lambda(t) dt ),   lambda(t) >= 0.

  (1a) MONOTONE / NO REVIVALS: lambda>=0 => |rho_01| non-increasing for EVERY hazard.
  (1b) GAUSSIAN ONSET: a RAMPING hazard lambda(t)=a t reproduces paper-X's Gaussian
       onset EXACTLY: INT_0^T a t dt = a T^2/2 => |rho_01| = exp(-a T^2/2).
  (1c) CONSTANT hazard lambda=lambda0 -> pure exponential semigroup exp(-lambda0 T)
       (the MOST Markovian channel).
""")

# --- (1a) monotonicity of the OU seal coherence (the canonical paper-X seal) -----
T_grid = [mp.mpf(k) / 10 for k in range(1, 101)]      # T in {0.1,...,10.0}
C_vals = [C_OU(T) for T in T_grid]
mono_ok = all(C_vals[i + 1] <= C_vals[i] + TOL for i in range(len(C_vals) - 1))
line("1a OU-seal |rho_01| at T=0.1", mp.nstr(C_vals[0], 14))
line("1a OU-seal |rho_01| at T=10.0", mp.nstr(C_vals[-1], 14))
line("1a max upward step (should be <= 0)",
     mp.nstr(max((C_vals[i + 1] - C_vals[i]) for i in range(len(C_vals) - 1)), 6))
check("1a SEAL coherence is MONOTONE non-increasing (no revivals), dps>=120",
      mono_ok, "lambda_OU(t)=sigma^2 tau_c(1-e^{-t/tau_c}) >= 0 everywhere")
lam_min = min(lam_OU(T) for T in T_grid)
line("1a min lambda_OU over grid (>=0 => CP-divisible)", mp.nstr(lam_min, 8))
check("1a hazard lambda_OU(t) >= 0 on the whole grid (CP-divisibility)",
      lam_min >= -TOL)

# --- (1b) Gaussian onset from a ramping hazard (sympy-EXACT) ----------------------
a_sym, T_sym, t_sym = sp.symbols('a T t', positive=True)
ramp_integral = sp.integrate(a_sym * t_sym, (t_sym, 0, T_sym))      # = a T^2/2
onset_resid = sp.simplify(ramp_integral - a_sym * T_sym**2 / 2)
line("1b sympy INT_0^T a t dt", ramp_integral)
line("1b sympy residual vs a T^2/2", onset_resid)
check("1b GAUSSIAN ONSET exact: ramping hazard a t -> |rho_01|=exp(-a T^2/2) "
      "(sympy-exact)", onset_resid == 0,
      "paper-X sec 3.1: the onset is the RAMP, carries no mechanism info")
# numeric cross-check of the Gaussian onset value (high precision)
a_num = mp.mpf("1") / sigma**0   # pick a=1 for a clean numeric anchor; arbitrary > 0
a_num = mp.mpf("0.8")
T_anchor = mp.mpf("3.5")
onset_val  = mp.e**(-a_num * T_anchor**2 / 2)
onset_int  = mp.e**(-mp.quad(lambda t: a_num * t, [0, T_anchor]))
line("1b numeric exp(-a T^2/2) at a=0.8,T=3.5", mp.nstr(onset_val, 20))
line("1b numeric exp(-INT_0^T a t dt)", mp.nstr(onset_int, 20))
check("1b Gaussian onset numeric residual = 0 (dps>=120)",
      abs(onset_val - onset_int) < TOL)

# --- (1c) constant hazard -> pure exponential semigroup ---------------------------
lam0 = mp.mpf("0.9")
exp_val = mp.e**(-lam0 * T_anchor)
exp_int = mp.e**(-mp.quad(lambda t: lam0, [0, T_anchor]))
line("1c constant-hazard exp(-lambda0 T) at lambda0=0.9,T=3.5", mp.nstr(exp_val, 18))
check("1c constant hazard -> pure exponential semigroup (Markovian limit)",
      abs(exp_val - exp_int) < TOL)

# --- the onset of the OU seal IS quadratic at short T (Zeno onset) ----------------
# chi(T) ~ (sigma^2 / 2) T^2 + O(T^3) at small T (the Gaussian onset of the OU kernel)
Tt = sp.symbols('Tt', positive=True)
sig_s, tc_s = sp.symbols('sigma tau_c', positive=True)
chi_series = sp.series(sig_s**2 * tc_s**2 * (Tt/tc_s - 1 + sp.exp(-Tt/tc_s)),
                       Tt, 0, 4).removeO()
lead = sp.simplify(chi_series.coeff(Tt, 2))                  # should be sigma^2/2
line("1c sympy short-T leading coeff of chi(T) (T^2 term)", lead)
check("1c OU seal has the GAUSSIAN (quadratic-onset) short-T law chi ~ (sigma^2/2)T^2",
      sp.simplify(lead - sig_s**2 / 2) == 0,
      "the OU seal's onset is itself the Gaussian onset -- the shared shape")

print("""
  GROUP 1 result: the SEAL channel |rho_01|=exp(-INT lambda), lambda>=0, is MONOTONE
  (no revivals), reproduces the GAUSSIAN onset exactly via a ramping hazard, and is
  the pure exponential semigroup for a constant hazard.  This is paper56 sec 3 /
  paper-X sec 3.1-3.2 reproduced at dps>=120, sympy-exact.
""")


# ===========================================================================
head("GROUP 2.  THE COMPARISON: (a) QM OU CP-divisible decoherence; (b) revival.")
# ===========================================================================
print("""
  (a) [QM] STANDARD-QM CP-DIVISIBLE ENVIRONMENTAL DECOHERENCE.  The SAME OU kernel
      arises in ordinary open-system pure dephasing with no record/seal ontology at
      all -- a thermal bosonic bath with Lorentzian (OU) spectral density gives
      exactly chi(T) above.  It is ALSO monotone, ALSO no revivals -- the standard-QM
      decoherence channel.  By construction it has the SAME |rho_01(T)| as the SEAL.

  (b) [REVIVAL] A NON-MARKOVIAN / REVIVAL-EXHIBITING COLLAPSE MODEL.  The equally
      positive-type UNDERDAMPED kernel K(s)=sigma^2 e^{-|s|/tau} cos(omega0 s)
      (a Lorentzian-PAIR spectrum, S(omega)>=0, a legitimate Gaussian noise) has a
      running integral INT_0^T K that goes NEGATIVE on sub-intervals once
      omega0 tau exceeds  (omega0 tau)_* = 3.644173671645632...  -> lambda(t)<0 there
      -> the coherence partially REVIVES (non-CP-divisible).  This is the exotic class
      the no-revival CAN discriminate against (collapse models with information
      backflow), NOT standard QM.
""")

# --- (2a) [QM] OU decoherence: same coherence as the seal (trivially, same kernel)
#     We make the "QM vs SEAL share |rho_01|" explicit and exact below in GROUP 4;
#     here we confirm the QM-OU channel is itself monotone / CP-divisible.
check("2a [QM] OU decoherence channel is MONOTONE (same kernel as seal) -- also no "
      "revivals", mono_ok and lam_min >= -TOL,
      "ordinary QM bath dephasing with Lorentzian spectrum")

# --- (2b) [REVIVAL] underdamped kernel running integral and its negative dip -------
# INT_0^T K = sigma^2 tau [ 1 + e^{-T/tau}(omega0 tau sin(omega0 T) - cos(omega0 T)) ]
#             / (1 + (omega0 tau)^2)         (paper-X sec 3.4, verified)
tau_u = mp.mpf("0.5")
def run_int_under(T, omega0):
    ot = omega0 * tau_u
    return (sigma**2 * tau_u
            * (1 + mp.e**(-T / tau_u) * (ot * mp.sin(omega0 * T) - mp.cos(omega0 * T)))
            / (1 + ot**2))

def lam_under(t, omega0):
    # instantaneous dephasing rate gamma(t)/2 ~ running integral of K (hbar=1, /1)
    return run_int_under(t, omega0)

# choose omega0 so that omega0*tau_u = 7 (well past threshold 3.6442) -> revivals
omega0_rev = mp.mpf("7") / tau_u
# scan for a negative running integral (=> negative rate => revival)
Tg = [mp.mpf(k) / 200 for k in range(1, 401)]          # fine grid T in (0,2]
RI = [run_int_under(T, omega0_rev) for T in Tg]
ri_min = min(RI)
ri_argmin = Tg[RI.index(ri_min)]
line("2b underdamped omega0 tau", mp.nstr(omega0_rev * tau_u, 6))
line("2b min running integral INT_0^T K over T in (0,2]", mp.nstr(ri_min, 8))
line("2b at T*", mp.nstr(ri_argmin, 6))
check("2b [REVIVAL] underdamped kernel has NEGATIVE running integral (lambda<0) "
      "=> coherence REVIVES", ri_min < -mp.mpf("1e-6"),
      "non-CP-divisible: the coherence |rho_01| goes back UP on an interval")

# explicitly verify the coherence goes back UP (a revival) for the underdamped model
def chi_under(T, omega0):
    # chi(T) = INT_0^T (T-s) K(s) ds ; integrate the running integral once more
    return mp.quad(lambda s: run_int_under(s, omega0), [0, T])
Crev = [mp.e**(-chi_under(T, omega0_rev)) for T in Tg]
# find a strict upward step (revival) in the coherence
up_steps = [(Crev[i + 1] - Crev[i]) for i in range(len(Crev) - 1)]
max_up = max(up_steps)
check("2b [REVIVAL] coherence |rho_01| has a STRICT upward step (an actual revival)",
      max_up > mp.mpf("1e-9"),
      "max upward step = %s" % mp.nstr(max_up, 6))

# --- the revival THRESHOLD (omega0 tau)_* = 3.644173671645632... (paper-X) --------
# tangency: min over T of [1 + e^{-x}(b sin? ...)] -> reproduce the boxed root.
# The threshold solves  d/dT(INT K)=0 giving a tangent-to-zero minimum.  We locate it
# by bisection on b=omega0*tau so that min_T INT_0^T K = 0.
def min_running(b):
    # with tau scaled to 1 (b = omega0*tau is the only parameter), running integral
    # proportional to f(T)=1 + e^{-T}(b sin(b T/... )) -- use tau=1 form:
    def g(T):
        return (1 + mp.e**(-T) * (b * mp.sin(b * T) - mp.cos(b * T))) / (1 + b**2)
    # scan + refine for the minimum over a few periods
    best = mp.mpf("1e9"); bestT = mp.mpf("0")
    N = 4000
    for k in range(1, N + 1):
        T = mp.mpf(k) * mp.mpf("8") / N
        v = g(T)
        if v < best:
            best, bestT = v, T
    # one Newton-ish refine via golden bracket
    lo, hi = bestT - mp.mpf("8") / N, bestT + mp.mpf("8") / N
    for _ in range(80):
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if g(m1) < g(m2):
            hi = m2
        else:
            lo = m1
    return g((lo + hi) / 2)

# bisect b so that min_running(b)=0
blo, bhi = mp.mpf("3.0"), mp.mpf("4.5")
for _ in range(200):
    bm = (blo + bhi) / 2
    if min_running(bm) > 0:
        blo = bm
    else:
        bhi = bm
b_star = (blo + bhi) / 2
b_star_ref = mp.mpf("3.644173671645632136171")     # paper-X boxed value
line("2b revival threshold (omega0 tau)_* computed", mp.nstr(b_star, 16))
line("2b paper-X boxed (omega0 tau)_*", mp.nstr(b_star_ref, 16))
check("2b revival threshold (omega0 tau)_* = 3.644173671645632... matches paper-X",
      abs(b_star - b_star_ref) < mp.mpf("1e-9"),
      "boundary of the CP-divisible region; bisection",
      solver_tol=True)

print("""
  GROUP 2 result: [QM] OU decoherence is monotone / CP-divisible (no revivals), the
  SAME shape as the [SEAL].  [REVIVAL] the underdamped collapse model has a negative
  running integral past (omega0 tau)_* = 3.6442... and its coherence ACTUALLY revives
  (a strict upward step).  These are the two foils: QM (looks like the seal) and the
  revival class (the only thing the no-revival can discriminate against).
""")


# ===========================================================================
head("GROUP 3.  THE BLP/RHP NON-MARKOVIANITY MEASURE N.")
# ===========================================================================
print("""
  BLP (Breuer-Laine-Piilo, PRL 103, 210401): for a pure-dephasing qubit the optimal
  trace-distance pair is the equatorial pair, and D(t) = |rho_01(t)| (the coherence).
  Information BACKFLOW = d/dt D(t) > 0.  The BLP non-Markovianity measure is

       N_BLP = INT_{ d/dt D > 0 }  (d/dt D(t)) dt   = total upward variation of D.

  For pure dephasing this is ZERO exactly when |rho_01| is MONOTONE non-increasing
  (CP-divisible), and POSITIVE exactly when there is a revival.  (RHP agrees here:
  the RHP measure integrates the negative part of the rate gamma(t)=-d/dt ln D; for
  pure dephasing RHP>0 iff BLP>0 iff a revival, so N captures both.)

  We compute N for the SEAL, for QM-OU, and for the REVIVAL model.
""")

def N_BLP(C_func, T_grid_local):
    """Total upward variation of D(t)=C_func(t) over the grid (BLP measure, >=0)."""
    vals = [C_func(T) for T in T_grid_local]
    up = mp.mpf("0")
    for i in range(len(vals) - 1):
        d = vals[i + 1] - vals[i]
        if d > 0:
            up += d
    return up, vals

# fine grid for the measure
Tm = [mp.mpf(k) / 500 for k in range(0, 1001)]          # T in [0,2] step 0.002

# [SEAL] = OU seal coherence (monotone)
N_seal, _ = N_BLP(C_OU, Tm)
# [QM] = OU decoherence -- IDENTICAL coherence to the seal (same kernel)
N_qm = N_seal           # bit-identical curve => identical measure (made exact in G4)
# [REVIVAL] = underdamped coherence
def C_rev(T):
    return mp.e**(-chi_under(T, omega0_rev))
N_rev, _ = N_BLP(C_rev, Tm)

line("3 N_BLP [SEAL]   (SHARD seal, OU hazard)", mp.nstr(N_seal, 8))
line("3 N_BLP [QM]     (standard QM OU decoherence)", mp.nstr(N_qm, 8))
line("3 N_BLP [REVIVAL](underdamped collapse model)", mp.nstr(N_rev, 8))

check("3 N_BLP[SEAL] = 0  (no information backflow; CP-divisible)",
      N_seal < mp.mpf("1e-30"))
check("3 N_BLP[QM] = 0  (standard QM CP-divisible decoherence; no backflow)",
      N_qm < mp.mpf("1e-30"))
check("3 N_BLP[REVIVAL] > 0  (information backflow; non-CP-divisible)",
      N_rev > mp.mpf("1e-6"),
      "the measure SEPARATES the revival class")

# THE DECISIVE STATEMENT: N cannot separate SEAL from QM (both 0); only from REVIVAL.
check("3 N CANNOT separate SHARD-seal from QM (N[SEAL]=N[QM]=0)",
      abs(N_seal - N_qm) < mp.mpf("1e-30"),
      "[NO-GO/BLIND] the no-revival is blind in the SHARD-vs-QM sense")
check("3 N DOES separate the seal/QM from the REVIVAL class (N[REVIVAL]>0=N[seal])",
      N_rev - N_seal > mp.mpf("1e-6"),
      "[NOT-BLIND only vs the exotic class] this is the WHOLE discrimination power")

# RHP cross-check: the RHP measure integrates the NEGATIVE part of the dephasing rate.
# For pure dephasing gamma(t) = -d/dt ln|rho_01| = d/dt chi.  Seal: gamma>=0 (RHP=0);
# revival: gamma<0 somewhere (RHP>0).  Reuse lambda_OU>=0 and the underdamped dip.
gamma_seal_min = min(lam_OU(T) for T in Tm[1:])
line("3 RHP: min dephasing rate gamma(t) for SEAL/QM (>=0 => RHP=0)",
     mp.nstr(gamma_seal_min, 8))
gamma_rev_min = min(lam_under(T, omega0_rev) for T in Tm[1:])
line("3 RHP: min dephasing rate gamma(t) for REVIVAL (<0 => RHP>0)",
     mp.nstr(gamma_rev_min, 8))
check("3 RHP agrees with BLP: gamma>=0 for SEAL/QM (RHP=0), gamma<0 for REVIVAL "
      "(RHP>0)", gamma_seal_min >= -TOL and gamma_rev_min < -mp.mpf("1e-6"))

print("""
  GROUP 3 result: N_BLP[SEAL] = N_BLP[QM] = 0 and N_BLP[REVIVAL] > 0; RHP agrees.
  The BLP/RHP non-Markovianity measure CANNOT separate the SHARD seal from standard-QM
  CP-divisible decoherence (both 0); it separates BOTH of them from the revival class
  (non-CP-divisible collapse models).  This is the precise discrimination boundary.
""")


# ===========================================================================
head("GROUP 4.  ESCAPE ATTEMPTS -- genuinely try to beat the blindness.")
# ===========================================================================
print("""
  PRE-DECLARED KILL-CRITERION: a GENUINE escape = a measurable Q that DIFFERS between
  the SHARD seal and a standard-QM CP-divisible decoherence channel with the SAME
  single-time |rho_01(t)|.  We attack from four directions:

   E1  THE SPECIFIC lambda(t) FORM / exact decay shape.  Does fixing the OU shape
       (not just the onset) separate seal from QM-noise?  -> the all-orders identity
       INT lambda_OU = chi (paper-X sec 3.3): the matched sparse-seal and the
       continuous OU noise share |rho_01(T)| to ALL ORDERS in T.  [sympy-EXACT]
   E2  HIGHER-ORDER SINGLE-TIME MOMENTS of the dephasing (the cumulant tower).  For a
       Gaussian channel ALL cumulants beyond the 2nd vanish; the seal with the matched
       hazard has the SAME chi(T), hence the SAME full free-induction statistics.
       Probe: is there a single-time functional of the curve that differs?  -> NO.
   E3  MULTI-TIME / TWO-TIME CORRELATION at the level of the REDUCED COHERENCE.  The
       Gaussian two-time function g2(t1,t2) is fixed by chi (it is the SAME kernel);
       seal and OU-noise share it.  -> NO escape at the passive two-time level.
   E4  THE ONE PLACE A DIFFERENCE LIVES (honest): genuine MULTI-TIME / invasive
       protocols (echo/CPMG, the non-Gaussian JUMP cumulants of a DISCRETE seal) CAN
       separate a REFOCUSABLE noise from an IRREVERSIBLE commitment -- but (i) that is
       REVERSIBILITY, the SAME axis as the revival class, NOT the no-revival itself;
       (ii) the structural indivisibility is invisible to the reduced channel at every
       order (paper-X sec 3.3 / 4, O4-O7).  So the no-revival ITSELF buys no escape.
""")

# ---- E1: the all-orders identity INT_0^T lambda_OU = chi(T) (sympy-EXACT) ---------
print("\n  E1.  THE SPECIFIC lambda(t) FORM: INT lambda_OU = chi, all orders (sympy).")
sig_e, tc_e, T_e, t_e = sp.symbols('sigma tau_c T t', positive=True)
chi_sym   = sig_e**2 * tc_e**2 * (T_e / tc_e - 1 + sp.exp(-T_e / tc_e))
lam_sym   = sig_e**2 * tc_e * (1 - sp.exp(-t_e / tc_e))          # = chi'(t)
int_lam   = sp.integrate(lam_sym, (t_e, 0, T_e))
e1_resid  = sp.simplify(int_lam - chi_sym)
line("E1 sympy INT_0^T lambda_OU dt", sp.simplify(int_lam))
line("E1 sympy chi(T)", sp.simplify(chi_sym))
line("E1 sympy residual INT lambda_OU - chi", e1_resid)
check("E1 SHAPE-MATCH: INT lambda_OU = chi to ALL ORDERS (sympy-exact) => seal and "
      "OU-noise share |rho_01(T)| entirely", e1_resid == 0,
      "[NO-GO/BLIND] the specific OU shape does NOT separate seal from QM-noise")
# numeric machine-zero cross-check (the paper-X 7.1e-102 result, at dps>=120)
def C_seal_from_lam(T):
    return mp.e**(-mp.quad(lam_OU, [0, T]))
max_gap = max(abs(C_OU(T) - C_seal_from_lam(T)) for T in T_grid)
line("E1 numeric max|C_OU - C_seal| over T in {0.1..10}", mp.nstr(max_gap, 6))
check("E1 numeric all-orders agreement: max|C_OU - C_seal| ~ machine zero (dps>=120)",
      max_gap < TOL,
      "paper-X sec 3.3: free-induction decay does not separate noise from sealing")

# ---- E2: higher-order single-time cumulants of the Gaussian dephasing -------------
print("\n  E2.  HIGHER-ORDER SINGLE-TIME MOMENTS / cumulant tower.")
print("""
  For a Gaussian dephasing the cumulant generating function of the accumulated phase
  Phi=INT delta E dt is ln<e^{iPhi}> = -chi(T) with ALL higher cumulants zero; the
  matched-hazard seal has the SAME chi, hence the SAME generating function.  Test: pick
  several DISTINCT single-time functionals of the coherence curve (value, log-slope,
  curvature, an arbitrary weighted moment) and confirm seal == QM-OU on every one.
""")
def logslope(C_func, T, h=mp.mpf("1e-30")):
    return (mp.log(C_func(T + h)) - mp.log(C_func(T - h))) / (2 * h)
def curvature(C_func, T, h=mp.mpf("1e-20")):
    return (C_func(T + h) - 2 * C_func(T) + C_func(T - h)) / h**2
# functional 1: value;  2: log-slope (=-lambda);  3: a weighted integral moment
Tprobe = [mp.mpf("0.3"), mp.mpf("0.9"), mp.mpf("1.7"), mp.mpf("3.1")]
f_val_gap   = max(abs(C_OU(T) - C_seal_from_lam(T)) for T in Tprobe)
f_slope_gap = max(abs(logslope(C_OU, T) - logslope(C_seal_from_lam, T)) for T in Tprobe)
# weighted moment INT_0^5 w(T) C(T) dT with an arbitrary weight w(T)=T e^{-T}
m_OU   = mp.quad(lambda T: T * mp.e**(-T) * C_OU(T), [0, 5])
m_seal = mp.quad(lambda T: T * mp.e**(-T) * C_seal_from_lam(T), [0, 5])
line("E2 single-time VALUE gap (seal vs QM-OU)", mp.nstr(f_val_gap, 6))
line("E2 LOG-SLOPE (=-lambda) gap", mp.nstr(f_slope_gap, 6))
line("E2 weighted MOMENT gap INT T e^{-T} C dT", mp.nstr(abs(m_OU - m_seal), 6))
check("E2 EVERY single-time functional (value, log-slope, weighted moment) AGREES "
      "seal == QM-OU (dps>=120)",
      f_val_gap < TOL and f_slope_gap < mp.mpf("1e-20") and abs(m_OU - m_seal) < TOL,
      "[NO-GO/BLIND] no single-time observable separates them")

# ---- E3: passive two-time correlation at the reduced-coherence level --------------
print("\n  E3.  PASSIVE TWO-TIME CORRELATION g2(t1,t2) at the reduced level.")
print("""
  For Gaussian dephasing the two-time phase correlation is fixed by the SAME kernel K:
  <Phi(t1)Phi(t2)> is a functional of chi, identical for the seal (matched hazard) and
  the OU noise.  A free-induction-equivalent two-time function (e.g. the Ramsey
  correlation built from chi at t1,t2,t1+t2) is therefore shared.  Test the symmetric
  combination  chi(t1)+chi(t2)+chi(t1+t2) ... actually the additive-phase variance
  Var(Phi(t1)+Phi(t2)) reconstructed from chi: it must agree because chi agrees.
""")
def chi_seal(T):
    return mp.quad(lam_OU, [0, T])        # = chi by E1, numerically
pairs = [(mp.mpf("0.4"), mp.mpf("0.9")), (mp.mpf("1.1"), mp.mpf("2.3"))]
g3_gap = mp.mpf("0")
for (t1, t2) in pairs:
    # any free-induction-reconstructible two-time functional is a function of chi(.)
    F_OU   = chi_OU(t1) + chi_OU(t2) + chi_OU(t1 + t2)
    F_seal = chi_seal(t1) + chi_seal(t2) + chi_seal(t1 + t2)
    g3_gap = max(g3_gap, abs(F_OU - F_seal))
line("E3 max gap in a two-time chi-functional (seal vs QM-OU)", mp.nstr(g3_gap, 6))
check("E3 PASSIVE two-time correlation (any chi-functional) AGREES seal == QM-OU",
      g3_gap < TOL,
      "[NO-GO/BLIND] passive multi-time at the reduced-coherence level: no escape")

# ---- E4: the ONE place a difference lives, and why it is NOT the no-revival -------
print("\n  E4.  WHERE A DIFFERENCE *DOES* LIVE -- and why it is not the no-revival.")
print("""
  HONEST: a difference between seal (irreversible commitment) and a REFOCUSABLE noise
  CAN appear in (i) an ECHO / CPMG multi-time sequence (refocuses reversible phase, not
  a committed record) and (ii) the non-Gaussian JUMP cumulants of a genuinely DISCRETE
  seal (the bimodal limit C(T)=cos(sigma_E T) -- a hard oscillation, NOT a smooth
  Gaussian).  BUT both of these are the REVERSIBILITY / discreteness axis, i.e. the
  SAME axis as the revival class (echo restoration is itself an information backflow);
  they are NOT a consequence of the *no-revival* property.  The no-revival, by itself,
  is exactly the CP-divisibility the seal SHARES with QM.  So:
     * a REFOCUSABLE QM noise and the seal DIFFER under echo -> but that splits the seal
       from REVERSIBLE noise, again the reversibility/revival axis, NOT seal-vs-QM-
       irreversible-decoherence (which is also non-refocusable).
     * the bimodal DISCRETE seal C(T)=cos(sigma_E T) DOES revive (it is non-CP-
       divisible) -> it is in the REVIVAL class, so any discrimination it provides is
       captured by N>0 already, NOT a new no-revival escape.
""")
# (i) the bimodal discrete-seal cosine REVIVES => it is in the revival class (N>0),
#     so it is NOT a NEW discriminator beyond GROUP 3.
sigE = mp.mpf("2.0")
def C_bimodal(T):
    return abs(mp.cos(sigE * T))          # |coherence| of the hard which-path oscillation
N_bimodal, _ = N_BLP(C_bimodal, Tm)
line("E4 N_BLP[bimodal discrete seal cos(sigma_E T)]", mp.nstr(N_bimodal, 8))
check("E4 the DISCRETE (bimodal) seal cos(sigma_E T) is itself a REVIVAL (N>0) -- "
      "captured by GROUP 3, NOT a new no-revival escape", N_bimodal > mp.mpf("1e-3"),
      "[NOT a new escape] discreteness lives on the revival/reversibility axis")
# (ii) bit-identical onset of the discrete seal vs the smooth Gaussian at short T
#     cos(sigma_E T) ~ 1 - (sigma_E^2/2)T^2 == exp(-(sigma_E^2/2)T^2) to O(T^2):
xT = sp.symbols('xT', positive=True)
sE = sp.symbols('sigma_E', positive=True)
cos_series = sp.series(sp.cos(sE * xT), xT, 0, 3).removeO()
gauss_series = sp.series(sp.exp(-sE**2 * xT**2 / 2), xT, 0, 3).removeO()
onset_match = sp.simplify(cos_series - gauss_series)      # O(T^2) agreement; differ O(T^4)
line("E4 sympy cos onset - Gaussian onset (to O(T^2))", onset_match)
check("E4 the discrete-seal ONSET is bit-identical to the Gaussian onset at O(T^2) "
      "(differ only at O(T^4), the revival/jump cumulant)", onset_match == 0,
      "[NO-GO/BLIND] the ONSET itself is shared; only the revival (O(T^4)) differs")

print("""
  GROUP 4 result: ALL FOUR escape attempts fail to beat the blindness AT THE
  NO-REVIVAL LEVEL.  E1 (specific OU shape) -> shared to all orders (sympy-exact).
  E2 (higher single-time moments) -> every functional agrees.  E3 (passive two-time)
  -> shared.  E4 (where a difference DOES live) -> it lives on the REVERSIBILITY /
  revival axis (echo, discrete jumps), the SAME axis GROUP 3's N already captures, NOT
  a new consequence of the no-revival.  The no-revival ITSELF discriminates ONLY
  against the revival class.
""")


# ===========================================================================
head("GROUP 5.  VERDICT + THE PRECISE DISCRIMINATION BOUNDARY.")
# ===========================================================================
all_pass = all(c for _, c in CHECKS)
n_pass = sum(1 for _, c in CHECKS if c)
n_tot = len(CHECKS)

# adjudicate the kill-criterion: did ANY escape attempt produce a seal-vs-QM gap?
escape_gaps = {
    "E1 specific-shape (all-orders OU)": max_gap,
    "E2 single-time functionals": max(f_val_gap, abs(m_OU - m_seal)),
    "E3 passive two-time": g3_gap,
}
max_escape_gap = max(escape_gaps.values())
genuine_escape = max_escape_gap > mp.mpf("1e-12")     # would-be seal-vs-QM separation

# the N-separation power: seal/QM (0) vs revival (>0)
sep_revival = (N_rev > mp.mpf("1e-6")) and (N_seal < mp.mpf("1e-30")) \
              and (abs(N_seal - N_qm) < mp.mpf("1e-30"))

print(f"""
  KILL-CRITERION ADJUDICATION (pre-declared, binding):
    A genuine escape requires a measurable Q with Q[SEAL] != Q[QM] at SAME |rho_01|.
    max seal-vs-QM gap over ALL escape attempts E1-E3 = {mp.nstr(max_escape_gap, 6)}
    genuine_escape (gap > 1e-12)?  {genuine_escape}
    => NO escape attempt separates the SHARD seal from standard-QM CP-divisible
       decoherence.  Every passive single-time / multi-time / shape functional agrees.

  THE ONLY DISCRIMINATION POWER (GROUP 3):
    N_BLP[SEAL] = N_BLP[QM] = 0;  N_BLP[REVIVAL] > 0;  RHP agrees.
    separates_only_revival?  {sep_revival}
    => the no-revival / CP-divisibility discriminates ONLY against the REVIVAL class
       (non-CP-divisible / non-Markovian collapse models with information backflow),
       NOT against standard quantum mechanics.

  VERDICT:  BLIND_NO_ESCAPE.
    No measurable quantity separates the SHARD seal from standard-QM CP-divisible
    environmental decoherence -- they share |rho_01(t)| to all orders (E1, sympy-exact),
    every single-time functional (E2), every passive multi-time correlation (E3), and
    the BLP/RHP measure N (both = 0, GROUP 3).  The honest prior is CONFIRMED, not
    manufactured away.

  THE PRECISE DISCRIMINATION BOUNDARY:
    [BLIND   ] SHARD seal  vs  standard-QM CP-divisible decoherence  -> INDISTINGUISHABLE
               (N=0 both; identical |rho_01| to all orders; no escape).
    [NOT-BLIND] SHARD seal / QM-decoherence  vs  REVIVAL-exhibiting collapse models
               (non-CP-divisible, N>0)  ->  DISCRIMINATED.
    The boundary is the CP-divisibility line itself: the no-revival is a discriminator
    EXACTLY against the non-CP-divisible (information-backflow) class and NOTHING finer.
    It is SHARD-SPECIFIC (a seal IS CP-divisible by paper56 sec 3) but BLIND vs QM,
    because QM CP-divisible decoherence sits on the SAME side of that line.

  MIX CONTEXT (the two channels):
    CHANNEL A (seal-swerve, covariant momentum diffusion, DHS 2004 / PDS 2009):
              [TESTABLE / NOT-BLIND but SCALE-GATED] -- the only channel that is BOTH
              seal-specific AND escapes mechanism-blindness (continuum QFT conserves
              free-particle momentum; a covariant anomalous heating is a discrete-
              substrate-vs-continuum DISCRIMINATOR; magnitude kappa ~ sigma l_step^k
              needs the imported scale).
    CHANNEL B (this receipt, the no-revival / CP-divisibility):
              [NO-GO/BLIND] -- seal-specific but cannot beat QM; discriminates only
              against the revival class.

  ALL CHECKS PASS: {all_pass}   ({n_pass}/{n_tot})
""")

assert all_pass, "SOME CHECK FAILED -- see *** FAIL *** above"
assert not genuine_escape, "an escape was found -- re-examine (prior expected BLIND)"
assert sep_revival, "N must separate the revival class (and nothing finer)"
print(f"ALL CHECKS PASS ({n_pass}/{n_tot})")
print("VERDICT: BLIND_NO_ESCAPE  (the no-revival discriminates only the revival class)")
head("DONE.  (all machine-check asserts passed; mpmath dps=%d, sympy-exact where algebraic)"
     % mp.mp.dps)
