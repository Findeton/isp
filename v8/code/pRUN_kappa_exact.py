"""
v7  THREAD RAMANUJAN  --  pRUN_kappa_exact.py
THE EXACT RUNNING OF THE SEAL/DECOHERENCE PROPORTIONALITY CONSTANT kappa(s).

CONTEXT.  The keystone [TARGET] "decoherence rate = seal rate = sigma" DISSOLVED into
a FLUCTUATION-DISSIPATION proportionality (paper56 functor; thesis): the coherence
loss per seal is the BHATTACHARYYA distance D_B = -log Sum sqrt(P0 P1) (a Renyi-1/2,
"which-path / noise" quantity), while SHARD's seal rate sigma = D(P_AB||P_BA) is a
pairwise KL D_KL (a Renyi-1, "forward-vs-reverse arrow / dissipation" quantity).  They
are NOT equal (kappa=1 false) but PROPORTIONAL,  D_B = kappa(s) * D_KL,  with kappa -> 1/4
in the dense/weak-seal limit (the corpus "quarter law", v6 paper26 Theorem A, which is
LEADING-ORDER and float64).

pK1 (sympy-exact, dps=120) settled the DENSE LIMIT: kappa is forced to a distribution-
INDEPENDENT value set by the RENYI ORDER of the chosen sigma -- 1/4 for the KL (alpha=1),
1 for the JSD mutual information.  pK1 also FLAGGED that at FINITE seal strength s the ratio
RUNS and is distribution-dependent, but gave NO closed form.  THIS receipt supplies the
EXACT finite-strength running and the master divergence structure underneath.

================================  WHAT IS PROVED  ================================
 [A] THE ALL-ORDER GAUSSIAN IDENTITY (the clean exact result).  For the Gaussian-
     displacement record family  P0 = N(0,1),  P1 = N(mu,1)  (a coherent which-path
     displacement of any strength mu), the Bhattacharyya distance and the KL are
     ELEMENTARY and EXACTLY proportional at ALL mu:
         D_B(mu)  = mu^2 / 8           (NOT just leading order -- exact, all mu)
         D_KL(mu) = mu^2 / 2
         kappa(mu) = D_B/D_KL = 1/4    EXACTLY, for EVERY displacement mu.
     The quarter law is EXACT (not asymptotic) on the Gaussian-displacement family.
     This is the sharp statement: kappa=1/4 is a THEOREM, not a small-s expansion, for
     the canonical continuous which-path recorder.  (sympy-exact closed-form integrals.)

 [B] THE EXACT CLOSED-FORM RUNNING (symmetric binary record -- paper26's own family).
     For  P0 = (1/2+e, 1/2-e),  P1 = (1/2-e, 1/2+e)  (record bias e in [0,1/2)):
         D_B(e)  = -(1/2) log(1 - 4 e^2)
         D_KL(e) =  4 e * artanh(2 e)                       (= 2e log((1+2e)/(1-2e)))
         kappa(e) = -log(1 - 4 e^2) / ( 8 e * artanh(2 e) )
                  = 1/4 + e^2/6 + 14 e^4/45 + 724 e^6/945 + ...     (monotone increasing)
     So kappa RUNS UP from 1/4 (strong records lose coherence FASTER per nat of arrow
     than the quarter law) -- an exact elementary closed form, the running paper26 only
     observed numerically and never wrote down.  The dense limit e->0 recovers 1/4.
     For the ASYMMETRIC family P0=(a,1-a), P1=(a+s,1-a-s) the running acquires an O(s)
     term whose coefficient DEPENDS on the base a (distribution-dependent running),
     confirmed below; only the symmetric a=1/2 case runs as a pure even series in e.

 [C] THE MASTER (TWO-PARAMETER) DIVERGENCE.  Both quantities are specializations of ONE
     Renyi family.  Define the Renyi-alpha divergence  D_alpha(P0||P1) =
     (1/(alpha-1)) log Sum_x P0^alpha P1^(1-alpha).  Then:
         * the SEAL / arrow sigma = D_KL          = D_{alpha=1}              (Renyi-1)
         * the COHERENCE loss     D_B = -log BC   = (1/2) D_{alpha=1/2}      (Renyi-1/2)
     and in the weak limit EVERY order collapses to the SAME Fisher form with a linear-
     in-alpha prefactor:
         D_alpha  ->  (alpha/2) * J * s^2 / 2 ,   J = Fisher info = Sum delta^2/P0
     (verified: coeff/J = alpha/2 for alpha in {1/2,1,2,3,4}).  Hence the weak-limit
     proportionality constant for ANY Renyi-order seal measure is
         kappa_alpha = D_B / D_alpha  ->  (1/8 J) / (alpha/2 J)  =  1/(4 alpha).
     kappa = 1/4 is exactly "alpha=1 (the KL)"; kappa=1 would be alpha=1/4.  The quarter
     is the RATIO OF THE TWO RENYI ORDERS (1/2 for noise, 1 for dissipation): kappa =
     (1/2)/2 = 1/4 -- a clean FDT reading (noise order / 2 / dissipation order).

 FDT READING (the paper thesis, supported not proven here): D_B = the NOISE (Renyi-1/2,
 symmetric overlap / which-path; the real part of the influence functional), sigma = the
 DISSIPATION (Renyi-1, asymmetric forward-reverse; the entropy production); the forced
 pure number 1/4 = the ratio of their divergence orders in the athermal/dense limit; the
 ABSOLUTE rate stays imported (measured, like G -- Paper 57 no-go), only the constant is
 forced.

================================  NOVELTY (narrow)  ================================
 GENUINELY NEW (vs paper26's leading-order float64 quarter law and vs the standard
 Renyi/Fisher geometry):
   (1) [A] the ALL-ORDER (exact-at-every-mu) Gaussian-displacement identity kappa=1/4 --
       the quarter law upgraded from O(sigma) asymptotic to an EXACT theorem on the
       canonical continuous recorder.  (The mu^2/8 and mu^2/2 forms are individually
       textbook; their EXACT-ratio-is-1/4-at-all-orders statement AS the running of the
       seal/decoherence constant is the new packaging.)
   (2) [B] the EXACT closed-form RUNNING kappa(e) = -log(1-4e^2)/(8e artanh(2e)) for the
       symmetric binary record, with the explicit ascending series -- the finite-strength
       law paper26 left as an unquantified "large-eps deviation".
 NOT NEW (imported/known, stated honestly): the individual divergence formulae (D_B,
 D_KL, Renyi) are textbook; the weak-limit Fisher reduction and the alpha/2 Renyi-order
 prefactor are standard information geometry; the quarter-law leading order is paper26;
 kappa=1 (JSD) is the known decoherence=information complementarity (Englert/Zurek).
 The FDT INTERPRETATION (noise/dissipation = Renyi-1/2 / Renyi-1) is a reading, not a
 theorem; the absolute scale remains imported.

PRECISION: mpmath dps=140 numeric + sympy-EXACT closed forms.  NEVER float64.
Date: 2026-06-17.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 140
TOL = mp.mpf(10) ** (-110)

def head(s):
    print("\n" + "=" * 80); print(s); print("=" * 80)

def line(label, val, extra=""):
    print(f"  {label:<60} {val} {extra}")

CHECKS = []
def check(name, cond, extra=""):
    CHECKS.append((name, bool(cond)))
    line("CHECK  " + name, "PASS" if cond else "*** FAIL ***", extra)
    return bool(cond)


# ===========================================================================
head("STEP A.  THE ALL-ORDER GAUSSIAN-DISPLACEMENT IDENTITY  (kappa = 1/4 EXACTLY, all mu)")
# ===========================================================================
print("""
  Record family: a coherent which-path DISPLACEMENT.  Path 0 leaves N(0,1), path 1
  leaves N(mu,1) (unit variance; mu = record displacement = seal strength).  We compute
  the Bhattacharyya distance D_B = -log BC and the KL D_KL in CLOSED FORM (sympy-exact
  Gaussian integrals) and show kappa = D_B/D_KL = 1/4 EXACTLY at every mu -- the quarter
  law is a THEOREM here, not a weak-seal expansion.
""")
mu = sp.symbols('mu', positive=True)
x = sp.symbols('x', real=True)
p0 = sp.exp(-x**2/2) / sp.sqrt(2*sp.pi)
p1 = sp.exp(-(x-mu)**2/2) / sp.sqrt(2*sp.pi)

BC_sym = sp.simplify(sp.integrate(sp.sqrt(p0*p1), (x, -sp.oo, sp.oo)))   # Bhattacharyya coeff
DB_sym = sp.simplify(-sp.log(BC_sym))
DKL_sym = sp.simplify(sp.integrate(p0*sp.log(p0/p1), (x, -sp.oo, sp.oo)))
kappa_G = sp.simplify(DB_sym / DKL_sym)
line("A  BC(mu) = Sum sqrt(p0 p1)", BC_sym)
line("A  D_B(mu)  = -log BC", DB_sym)
line("A  D_KL(mu) = D(P0||P1)", DKL_sym)
line("A  kappa(mu) = D_B / D_KL", kappa_G)
check("A: D_B(mu) = mu^2/8 EXACTLY (all mu, sympy-exact Gaussian integral)",
      sp.simplify(DB_sym - mu**2/8) == 0)
check("A: D_KL(mu) = mu^2/2 EXACTLY (all mu)",
      sp.simplify(DKL_sym - mu**2/2) == 0)
check("A: kappa(mu) = 1/4 EXACTLY for EVERY mu (all-order quarter law, NOT asymptotic)",
      kappa_G == sp.Rational(1, 4))
check("A: kappa is mu-INDEPENDENT (no running on the Gaussian family) -- forced const",
      mu not in kappa_G.free_symbols)

# numeric cross-check at several finite (NOT small) mu, dps=140, direct quadrature
print("\n  numeric cross-check (direct mpmath quadrature, dps=140, finite mu):")
def gauss_DB_DKL(muv):
    f0 = lambda t: mp.e**(-t**2/2)/mp.sqrt(2*mp.pi)
    f1 = lambda t: mp.e**(-(t-muv)**2/2)/mp.sqrt(2*mp.pi)
    BC = mp.quad(lambda t: mp.sqrt(f0(t)*f1(t)), [-mp.inf, muv/2, mp.inf])
    DB = -mp.log(BC)
    DKL = mp.quad(lambda t: f0(t)*mp.log(f0(t)/f1(t)), [-mp.inf, muv/2, mp.inf])
    return DB, DKL
worst_G = mp.mpf(0)
for muv in [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("3"), mp.mpf("7")]:
    DB, DKL = gauss_DB_DKL(muv)
    kap = DB/DKL
    line(f"A  mu={mp.nstr(muv,4)}: D_B={mp.nstr(DB,16)}", f"D_KL={mp.nstr(DKL,16)} kappa={mp.nstr(kap,20)}")
    worst_G = max(worst_G, abs(kap - mp.mpf(1)/4), abs(DB - muv**2/8), abs(DKL - muv**2/2))
line("A  worst |error| over finite mu (D_B vs mu^2/8, D_KL vs mu^2/2, kappa vs 1/4)", mp.nstr(worst_G, 6))
check("A: numeric quadrature confirms D_B=mu^2/8, D_KL=mu^2/2, kappa=1/4 at finite mu (dps=140)",
      worst_G < mp.mpf("1e-60"))


# ===========================================================================
head("STEP B.  THE EXACT CLOSED-FORM RUNNING  kappa(e)  (symmetric binary record)")
# ===========================================================================
print("""
  paper26's own family: a biased record bit, P0=(1/2+e, 1/2-e), P1 mirrored.  Here the
  quarter law RUNS.  We derive the EXACT elementary closed form (sympy) and verify it
  against direct dps=140 computation, plus the ascending series 1/4 + e^2/6 + ...
""")
e = sp.symbols('e', positive=True)
P0b = [sp.Rational(1,2)+e, sp.Rational(1,2)-e]
P1b = [sp.Rational(1,2)-e, sp.Rational(1,2)+e]
BCb = sp.simplify(sp.sqrt(P0b[0]*P1b[0]) + sp.sqrt(P0b[1]*P1b[1]))
DBb = sp.simplify(-sp.log(BCb))
DKLb = sp.simplify(P0b[0]*sp.log(P0b[0]/P1b[0]) + P0b[1]*sp.log(P0b[1]/P1b[1]))
line("B  BC(e) = Sum sqrt(P0 P1)", BCb)
line("B  D_B(e)  = -log BC", DBb)
line("B  D_KL(e) (claim: 4 e artanh(2e))", DKLb)
check("B: BC(e) = sqrt(1 - 4 e^2) (symmetric-binary overlap, sympy-exact)",
      sp.simplify(BCb - sp.sqrt(1 - 4*e**2)) == 0)
check("B: D_B(e) = -(1/2) log(1 - 4 e^2) EXACTLY",
      sp.simplify(DBb - (-sp.Rational(1,2)*sp.log(1 - 4*e**2))) == 0)
# D_KL = 4 e artanh(2e): verify numerically (sympy branch-simplify of the log-ratio is
# unreliable, so check the closed form at many points to high precision instead)
DKL_closed = 4*e*sp.atanh(2*e)
worst_DKL = mp.mpf(0)
for ev in ["0.05", "0.1", "0.2", "0.3", "0.4", "0.49"]:
    lhs = mp.mpf(sp.N(DKLb.subs(e, sp.Rational(ev)), 130))
    rhs = mp.mpf(sp.N(DKL_closed.subs(e, sp.Rational(ev)), 130))
    worst_DKL = max(worst_DKL, abs(lhs - rhs))
line("B  worst |D_KL(e) - 4 e artanh(2e)| over e in [0.05,0.49]", mp.nstr(worst_DKL, 6))
check("B: D_KL(e) = 4 e * artanh(2e) EXACTLY (= 2e log((1+2e)/(1-2e)), dps=130 over grid)",
      worst_DKL < mp.mpf("1e-100"))

# the exact running closed form and its ascending series
kappa_e = DBb / DKL_closed
kappa_e_series = sp.series(DBb/DKLb, e, 0, 8).removeO()
line("B  kappa(e) = -log(1-4e^2) / (8 e artanh(2e))", sp.simplify(kappa_e))
line("B  kappa(e) ascending series", sp.simplify(kappa_e_series))
check("B: kappa(e) = 1/4 + e^2/6 + 14 e^4/45 + 724 e^6/945 + O(e^8) (sympy-exact series)",
      sp.simplify(kappa_e_series
                  - (sp.Rational(1,4) + e**2/6 + 14*e**4/45 + 724*e**6/945)) == 0)
check("B: kappa(0) = 1/4 (dense limit recovers the quarter law)",
      sp.limit(DBb/DKLb, e, 0) == sp.Rational(1,4))

# numeric: kappa(e) closed form vs direct, and monotone running UP
print("\n  numeric (dps=140): closed-form kappa(e) vs direct D_B/D_KL, and the running:")
def kappa_bin_sym(ev):
    P0 = [mp.mpf("0.5")+ev, mp.mpf("0.5")-ev]
    P1 = [mp.mpf("0.5")-ev, mp.mpf("0.5")+ev]
    BC = mp.sqrt(P0[0]*P1[0]) + mp.sqrt(P0[1]*P1[1])
    DB = -mp.log(BC); DKL = P0[0]*mp.log(P0[0]/P1[0]) + P0[1]*mp.log(P0[1]/P1[1])
    closed = -mp.log(1 - 4*ev**2) / (8*ev*mp.atanh(2*ev))
    return DB/DKL, closed
worst_run = mp.mpf(0); prev = mp.mpf(0)
mono = True
for ev in [mp.mpf("0.01"), mp.mpf("0.1"), mp.mpf("0.25"), mp.mpf("0.4"), mp.mpf("0.49")]:
    direct, closed = kappa_bin_sym(ev)
    line(f"B  e={mp.nstr(ev,4)}: kappa direct={mp.nstr(direct,22)}", f"closed={mp.nstr(closed,22)}")
    worst_run = max(worst_run, abs(direct - closed))
    if direct <= prev: mono = (ev == mp.mpf("0.01")) and mono  # first point: no prev
    prev = direct
check("B: closed-form kappa(e) matches direct D_B/D_KL to dps=140",
      worst_run < mp.mpf("1e-100"))
check("B: kappa(e) RUNS UP from 1/4 (monotone increasing in e) -- strong records "
      "decohere faster per nat of arrow than the quarter law", mono,
      "the running is real, exact, and one-signed")


# ===========================================================================
head("STEP C.  THE MASTER RENYI DIVERGENCE  (sigma and D_B are two orders of ONE family)")
# ===========================================================================
print("""
  Renyi-alpha divergence  D_alpha = 1/(alpha-1) log Sum P0^alpha P1^(1-alpha).
   * seal / arrow      sigma = D_KL       = D_{alpha=1}            (Renyi order 1)
   * coherence loss    D_B = -log BC      = (1/2) D_{alpha=1/2}    (Renyi order 1/2)
  Weak limit: D_alpha -> (alpha/2) * (J/2) * s^2, i.e. coeff/J = alpha/2 (verified for
  alpha in {1/2,1,2,3,4}).  Hence kappa_alpha = D_B/D_alpha -> 1/(4 alpha): the quarter
  is alpha=1, saturation kappa=1 is alpha=1/4.  kappa = (Renyi order of noise)/2/(Renyi
  order of dissipation) = (1/2)/2 / 1 = 1/4.
""")
# (i) D_B = (1/2) Renyi_{1/2} -- exact identity (binary, sympy)
a, s = sp.symbols('a s', positive=True)
P0g = [a, 1-a]; P1g = [a+s, 1-a-s]
Renyi_half = sp.simplify(sp.log(sum(sp.sqrt(P0g[i]*P1g[i]) for i in range(2))) / (sp.Rational(1,2)-1))
DB_g = sp.simplify(-sp.log(sum(sp.sqrt(P0g[i]*P1g[i]) for i in range(2))))
check("C: D_B = (1/2) D^Renyi_{1/2} EXACTLY (coherence loss IS half the Renyi-1/2 div)",
      sp.simplify(DB_g - Renyi_half/2) == 0)

# (ii) weak-limit Renyi-order prefactor: coeff/J = alpha/2 for several alpha (mpmath, exact ratio)
print("\n  weak-limit Renyi coefficient coeff(D_alpha)/J -> alpha/2 (dps=140):")
av = mp.mpf("0.37"); sv = mp.mpf("1e-22")
P0n = [av, 1-av]; P1n = [av+sv, 1-av-sv]
J = 1/av + 1/(1-av)
worst_renyi = mp.mpf(0)
for al in [mp.mpf("0.5"), mp.mpf("1.0001"), mp.mpf("2"), mp.mpf("3"), mp.mpf("4")]:
    if abs(al-1) < mp.mpf("1e-3"):
        # KL is the alpha->1 limit
        Dal = sum(P0n[i]*mp.log(P0n[i]/P1n[i]) for i in range(2))
        alab = mp.mpf("1")
    else:
        Sal = sum(P0n[i]**al * P1n[i]**(1-al) for i in range(2))
        Dal = mp.log(Sal)/(al-1)
        alab = al
    coef_over_J = (Dal/sv**2)/J
    line(f"C  alpha={mp.nstr(alab,6)}: coeff/J = {mp.nstr(coef_over_J,14)}", f"(predict alpha/2 = {mp.nstr(alab/2,14)})")
    worst_renyi = max(worst_renyi, abs(coef_over_J - alab/2))
line("C  worst |coeff/J - alpha/2| over alpha grid", mp.nstr(worst_renyi, 6))
check("C: D_alpha -> (alpha/2) J s^2/... i.e. coeff/J = alpha/2 for ALL alpha (dps=140)",
      worst_renyi < mp.mpf("1e-6"),
      "the seal/coherence prefactor is LINEAR in the Renyi order")

# (iii) master weak-limit constant kappa_alpha = 1/(4 alpha)
print("\n  master weak-limit constant  kappa_alpha = D_B/D_alpha -> 1/(4 alpha):")
DB_n = -mp.log(sum(mp.sqrt(P0n[i]*P1n[i]) for i in range(2)))
worst_master = mp.mpf(0)
for al in [mp.mpf("0.5"), mp.mpf("1.0001"), mp.mpf("2"), mp.mpf("4")]:
    if abs(al-1) < mp.mpf("1e-3"):
        Dal = sum(P0n[i]*mp.log(P0n[i]/P1n[i]) for i in range(2)); alab = mp.mpf("1")
    else:
        Dal = mp.log(sum(P0n[i]**al * P1n[i]**(1-al) for i in range(2)))/(al-1); alab = al
    kap_al = DB_n/Dal
    line(f"C  alpha={mp.nstr(alab,6)}: kappa_alpha = {mp.nstr(kap_al,16)}", f"(predict 1/(4 alpha) = {mp.nstr(1/(4*alab),16)})")
    worst_master = max(worst_master, abs(kap_al - 1/(4*alab)))
line("C  worst |kappa_alpha - 1/(4 alpha)|", mp.nstr(worst_master, 6))
check("C: kappa_alpha -> 1/(4 alpha): quarter=KL(alpha=1), saturation kappa=1=alpha 1/4",
      worst_master < mp.mpf("1e-5"),
      "the quarter law = ratio of Renyi orders: kappa = (1/2)/2 / 1 = 1/4")


# ===========================================================================
head("STEP D.  ASYMMETRIC RUNNING IS DISTRIBUTION-DEPENDENT (honest scope)")
# ===========================================================================
print("""
  The symmetric binary kappa(e) runs as a pure EVEN series (no O(e) term).  For the
  ASYMMETRIC family P0=(a,1-a), P1=(a+s,1-a-s) the running has an O(s) term whose slope
  DEPENDS on the base a -- so 'kappa runs' is distribution-dependent off the symmetric
  point; only the DENSE LIMIT value 1/4 and the GAUSSIAN all-order value 1/4 are
  distribution-FREE.  (Confirms pK1's flag with the exact slope.)
""")
def kappa_asym(av, sv):
    P0 = [av, 1-av]; P1 = [av+sv, 1-av-sv]
    BC = mp.sqrt(P0[0]*P1[0]) + mp.sqrt(P0[1]*P1[1])
    DB = -mp.log(BC); DKL = P0[0]*mp.log(P0[0]/P1[0]) + P0[1]*mp.log(P0[1]/P1[1])
    return DB/DKL
sv = mp.mpf("1e-10")
slopes = {}
for av in [mp.mpf("0.3"), mp.mpf("0.45"), mp.mpf("0.5")]:
    kap = kappa_asym(av, sv)
    slope = (kap - mp.mpf(1)/4)/sv          # O(s) slope of kappa above 1/4
    slopes[str(av)] = slope
    line(f"D  a={mp.nstr(av,4)}: kappa(s=1e-10)={mp.nstr(kap,20)}", f"O(s) slope (kappa-1/4)/s = {mp.nstr(slope,12)}")
check("D: symmetric a=1/2 has ~zero O(s) slope (even running in e) [structural]",
      abs(slopes["0.5"]) < mp.mpf("1e-6"))
check("D: asymmetric a!=1/2 has NONZERO, a-DEPENDENT O(s) slope -> running is "
      "distribution-dependent off the dense limit (honest scope)",
      abs(slopes["0.3"]) > mp.mpf("1e-3") and abs(slopes["0.3"] - slopes["0.45"]) > mp.mpf("1e-3"))


# ===========================================================================
head("VERDICT")
# ===========================================================================
all_pass = all(c for _, c in CHECKS)
n_pass = sum(1 for _, c in CHECKS if c); n_tot = len(CHECKS)
print(f"""
  THE EXACT RUNNING OF THE SEAL/DECOHERENCE CONSTANT kappa(s) -- resolved:

   [A] ALL-ORDER GAUSSIAN IDENTITY (the clean exact result, genuinely new packaging):
       on the canonical continuous which-path recorder N(0,1) vs N(mu,1),
       D_B = mu^2/8,  D_KL = mu^2/2,  kappa = 1/4  EXACTLY at EVERY displacement mu.
       The quarter law is a THEOREM, not a weak-seal expansion -- no running at all on
       the Gaussian family.  (paper26's quarter law was leading-order/float64.)

   [B] EXACT CLOSED-FORM RUNNING (symmetric binary, genuinely new):
       kappa(e) = -log(1-4e^2) / (8 e artanh(2e)) = 1/4 + e^2/6 + 14e^4/45 + 724e^6/945+...
       D_B = -(1/2)log(1-4e^2),  D_KL = 4e artanh(2e).  kappa runs monotonically UP from
       1/4: strong records decohere faster per nat of arrow than the quarter.  This is
       the finite-strength law paper26 left as an unquantified 'large-eps deviation'.

   [C] MASTER RENYI STRUCTURE: sigma = D_(alpha=1) (Renyi-1, dissipation), D_B =
       (1/2)D_(alpha=1/2) (Renyi-1/2, noise).  Weak limit D_alpha -> (alpha/2) J s^2/...,
       so kappa_alpha -> 1/(4 alpha): the quarter = ratio of Renyi orders (noise 1/2 over
       dissipation 1, with the 1/2 from D_B=half-Renyi).  Saturation kappa=1 would need
       alpha=1/4 -- which the mutual-information (JSD) measure supplies (pK1).

   [D] HONEST SCOPE: off the dense limit and off the Gaussian family the running is
       DISTRIBUTION-DEPENDENT (asymmetric base a gives an a-dependent O(s) slope).  Only
       (i) the dense limit and (ii) the all-order Gaussian value are distribution-FREE.
       The ABSOLUTE seal rate stays imported (Paper 57 no-go); only the dimensionless
       constant kappa is forced -- the FDT thesis (D_B=noise, sigma=dissipation, 1/4 =
       order ratio in the athermal limit) is the reading these exact forms support.

  NOVELTY carved narrowly: NEW = [A] the all-order Gaussian kappa=1/4 + [B] the exact
  closed-form running.  KNOWN/IMPORTED = individual divergence formulae (textbook),
  Renyi/Fisher weak-limit geometry (standard), the quarter leading order (paper26),
  kappa=1 complementarity (Englert/Zurek), the absolute scale (imported).  FDT
  interpretation = a reading, not a theorem.

  ALL CHECKS PASS: {all_pass}   ({n_pass}/{n_tot})
""")
assert all_pass, "SOME CHECK FAILED -- see *** FAIL *** above"
print(f"ALL CHECKS PASS ({n_pass}/{n_tot})")
head("DONE.  (mpmath dps=%d; sympy-exact closed forms for D_B, D_KL, kappa)" % mp.mp.dps)
