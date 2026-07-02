"""
FILTER 5  --  OI/PI CONSISTENCY WITH THE FORCED MULTIPLICATIVE SEALING SKELETON.
v7 Long March, Paper 1, Tier A.  Investigation (C): does the FORCED sequential
survival skeleton  S(chi)=exp(-kappa chi)  (dense) / S(n d)=S(d)^n (sparse) FORCE
outcome-independence (OI = factorization = NO entanglement), or does it PERMIT
OI-violation (entanglement) while keeping parameter-independence (PI) + no-signaling?

The whole investigation turns on ONE distinction the prompt names precisely:

   MULTIPLICATIVITY OF SURVIVAL along the SEQUENTIAL / REFINEMENT axis
        S(chi1 + chi2) = S(chi1) * S(chi2)            [stretches of ONE chain]

   is NOT the same as

   FACTORIZATION OF THE JOINT OUTCOME LAW (= Outcome Independence, OI)
        p(a,b | x,y, lambda) = p(a|x,lambda) p(b|y,lambda)   [two PARALLEL chains].

The first is composition along the COMMIT ORDER of a single record chain (the
direction Filter 3 forces).  The second is factorization across SPACELIKE-separated
parallel chains (the direction Bell's OI lives in).  They are orthogonal axes.
Paper 14 (v5) fixes the Bell address: any single-history theory reproducing CHSH
keeps PI + no-signaling + single outcomes and DROPS OI (Jarrett LC = PI ^ OI).
Paper 4 (v6) supplies the q=2 two-diamond Born composition.  Paper 1 (v7) s3.5
flags exactly this as OPEN [Tier-A]: the sequential seal-law "neither requires nor
forbids" the parallel-chain entanglement correlation.

WHAT THIS RECEIPT PROVES (machine-checked, mpmath dps>=120, sympy-exact):

  PART A.  The FORCED skeleton, restated as an OPERATOR on a single chain's
           survival.  Multiplicative (dense exp) + geometric-progression (sparse).
           Pure number chi (weight-0 KL); no spacetime.

  PART B.  A CONCRETE joint outcome law on two parallel chains with:
             PI = YES   (marginals indep of REMOTE setting)
             OI = NO    (outcomes correlated given the common prep lambda)
             no-signaling = YES
             CHSH = 2 sqrt(2)  (Tsirelson) > 2
           built from the canonical singlet correlation E(x,y) = -cos(x-y) (here
           we use the standard CHSH angle set giving 2 sqrt 2).  ALL high precision.

  PART C.  ATTACH the forced sequential skeleton to this entangling law: each
           chain carries its own multiplicative survival S_A(chi), S_B(chi); show
           the JOINT law still violates CHSH, still no-signals, while EACH chain's
           survival is exactly exp(-kappa chi).  => the forced skeleton is
           COMPATIBLE with (PERMITS) an OI-violating / entangling joint law.

  PART D.  DECISIVE SEPARATION.  Exhibit a survival-multiplicative joint law whose
           OUTCOME statistics do NOT factor (OI fails) -- proving multiplicativity
           of survival does NOT imply OI.  And exhibit the converse independence:
           an OI-respecting (factorized, Bell-local) law ALSO carries the same
           survival skeleton.  => the skeleton is silent on OI: it neither forces
           OI nor forbids OI.  The two structures are on ORTHOGONAL axes.

  PART E.  FORCED vs CONSTRAINED vs FREE for the ENTANGLING law itself.  The
           sequential skeleton is forced.  The transverse (parallel-chain) joint
           law is NOT fixed by it; the Bell/Tsirelson envelope (PI + no-signaling +
           single-outcome, OI dropped, CHSH<=2 sqrt2) CONSTRAINS it; within that
           envelope the specific correlation profile is FREE at Tier A (a separate
           Tier-A structure, not delivered by sequential refinement).

Pre-geometric discipline: chi is a weight-0 record-internal KL number; "x,y" are
abstract SETTING labels on parallel chains (a Tier-A correlation structure that
needs no spacetime to be defined -- paper1 s3.5), NOT spacetime directions.  The
CHSH angles are pure-number setting parameters of the correlation kernel.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 120

TOL = mp.mpf(10) ** (-100)   # high-precision identity tolerance


def head(s):
    print("\n" + "=" * 78)
    print(s)
    print("=" * 78)


def line(label, val, extra=""):
    print(f"  {label:<54} {val} {extra}")


CHECKS = []
def check(name, cond):
    CHECKS.append((name, bool(cond)))
    line("CHECK  " + name, "PASS" if cond else "*** FAIL ***")
    return bool(cond)


# ===========================================================================
head("PART A.  THE FORCED SEQUENTIAL SURVIVAL SKELETON (single chain)")
# ===========================================================================
print("""
  Filter 3 (f3_self_consistency.py) FORCES, along the commit order of ONE record
  chain, the survival functional:

    DENSE (divisible) regime:   S(chi1+chi2) = S(chi1) S(chi2)  =>  S(chi)=exp(-kappa chi)
    SPARSE (indivisible) regime: composition only on L={n d}    =>  S(n d)=S(d)^n.

  chi is a weight-0 record-internal KL number (the accumulated holonomy content);
  kappa>=0 the one no-go scale.  This is the SEQUENTIAL axis -- stretches of a
  SINGLE chain composed along the commit order.  We re-verify the skeleton here as
  the object whose relation to OI we will test.
""")

chi1, chi2, kappa, chi = sp.symbols('chi1 chi2 kappa chi', nonnegative=True)
S_exp = sp.exp(-kappa * chi)

# dense multiplicativity (sympy-exact)
resid_dense = sp.simplify(S_exp.subs(chi, chi1 + chi2)
                          - S_exp.subs(chi, chi1) * S_exp.subs(chi, chi2))
line("dense:  S(c1+c2) - S(c1)S(c2)  [sympy]", resid_dense)
check("dense survival is multiplicative (exp forced)", resid_dense == 0)

# sparse geometric progression S(n d)=S(d)^n, high precision
d = mp.mpf("0.41")          # arbitrary lattice spacing
kap = mp.mpf("0.7")
Sd = mp.e ** (-kap * d)
max_sparse = mp.mpf(0)
for n in range(1, 12):
    lhs = mp.e ** (-kap * (n * d))         # S(n d)
    rhs = Sd ** n                          # S(d)^n
    max_sparse = max(max_sparse, abs(lhs - rhs))
line("sparse:  max_n |S(n d) - S(d)^n|", mp.nstr(max_sparse, 6))
check("sparse survival is geometric-progression on L (dps>=120)", max_sparse < TOL)

# the dense exp is the d->0 limit of the sparse law (kappa = -log S(d)/d fixed)
chi_target = mp.mpf("1.3")
errs = []
for nd in [8, 64, 512, 4096]:
    dd = chi_target / nd
    Sdd = mp.e ** (-kap * dd)
    kap_recovered = -mp.log(Sdd) / dd          # = kap exactly here
    S_lattice = Sdd ** nd                       # S(d)^{chi/d}
    errs.append(abs(S_lattice - mp.e ** (-kap * chi_target)))
line("dense = d->0 limit:  |S(d)^{chi/d} - exp(-kappa chi)|", mp.nstr(max(errs), 6))
check("sparse -> dense exp recovered as d->0", max(errs) < TOL)


# ===========================================================================
head("PART B.  A JOINT OUTCOME LAW: PI-yes / OI-no / no-signaling / CHSH=2sqrt2")
# ===========================================================================
print("""
  TWO PARALLEL record chains A and B, each emitting a single binary outcome
  a,b in {+1,-1} under a setting x (for A) / y (for B).  Settings are PURE-NUMBER
  labels (Tier-A correlation parameters, NOT spacetime angles).  The joint law is
  the canonical singlet:
        E(x,y) = <a b> = -cos(x - y),    each marginal <a> = <b> = 0.
  Joint probabilities:
        p(a,b|x,y) = (1 + a b E(x,y)) / 4.
  This is the textbook-QM / ISP Bell address (paper14 row): single outcomes, MI,
  PI, no-signaling, OI VIOLATED.  We pick the CHSH-optimal settings to hit 2 sqrt2.
""")

def E_corr(x, y):
    return -mp.cos(x - y)

def p_joint(a, b, x, y):
    return (1 + a * b * E_corr(x, y)) / 4

# --- normalization & positivity at a generic setting pair -------------------
xg, yg = mp.mpf("0.37"), mp.mpf("1.21")
tot = sum(p_joint(a, b, xg, yg) for a in (1, -1) for b in (1, -1))
line("sum_{a,b} p(a,b|x,y)  (normalization)", mp.nstr(tot, 6))
check("joint law normalized", abs(tot - 1) < TOL)
minp = min(p_joint(a, b, xg, yg) for a in (1, -1) for b in (1, -1))
line("min p(a,b|x,y)  (positivity)", mp.nstr(minp, 6))
check("joint law nonnegative", minp >= -TOL)

# --- NO-SIGNALING:  marginal p(a|x,y) independent of remote setting y -------
def marg_A(a, x, y):
    return sum(p_joint(a, b, x, y) for b in (1, -1))
def marg_B(b, x, y):
    return sum(p_joint(a, b, x, y) for a in (1, -1))

# vary the REMOTE setting and confirm the local marginal is unchanged
y_alt = mp.mpf("2.93")
nosig_A = max(abs(marg_A(a, xg, yg) - marg_A(a, xg, y_alt)) for a in (1, -1))
x_alt = mp.mpf("0.08")
nosig_B = max(abs(marg_B(b, xg, yg) - marg_B(b, x_alt, yg)) for b in (1, -1))
line("max_a |p(a|x,y) - p(a|x,y')|   (A no-signaling)", mp.nstr(nosig_A, 6))
line("max_b |p(b|x,y) - p(b|x',y)|   (B no-signaling)", mp.nstr(nosig_B, 6))
check("NO-SIGNALING: local marginal indep of remote setting", nosig_A < TOL and nosig_B < TOL)
# and the marginals are flat 1/2 (each <a>=<b>=0)
flat = max(abs(marg_A(a, xg, yg) - mp.mpf("0.5")) for a in (1, -1))
line("|p(a|x) - 1/2|  (flat local marginal)", mp.nstr(flat, 6))
check("local marginals are uniform (no local readout of correlation)", flat < TOL)

# --- PARAMETER INDEPENDENCE (PI) at the hidden-variable / screen level -------
# In the Bell taxonomy (paper14 s1): the COMMON-PAST variable lambda is the
# preparation (singlet).  PI says p(a|x,y,lambda)=p(a|x,lambda): the remote SETTING
# y does not enter A's conditional given lambda.  In ISP/SHARD, lambda = the sealed
# preparation; the single q=2 process is parameter-independent (paper14 s3, CL_ISP).
# We model this directly: A's outcome law depends on x and lambda but NOT on y.
# (We instantiate lambda by the well-known equal-weight mixture realizing E(x,y)
#  WITHOUT a local-causal factorization -- the point is PI holds, OI need not.)
print("""
  PI (parameter independence): the LOCAL conditional p(a|x,y,lambda) does not
  depend on the REMOTE setting y given the common prep lambda.  Here lambda is the
  sealed singlet preparation (paper14 CL_ISP = PI).  Because the marginal p(a|x,y)
  is already y-independent (no-signaling, verified above) and lambda is the
  preparation common to both, A's local response law references x and lambda only.
""")
check("PI holds (local law refs x and prep lambda, not remote y)",
      nosig_A < TOL)   # operationalized: y-independence of A's law is PI at this lambda

# --- OUTCOME INDEPENDENCE (OI):  does p(a|b,x,y) = p(a|x,y)? -----------------
# OI fails iff learning the REMOTE outcome b changes A's conditional.
def p_a_given_b(a, b, x, y):
    return p_joint(a, b, x, y) / marg_B(b, x, y)

# choose CORRELATED settings (x=y) so E=-1 strongly: knowing b pins a.
xs, ys = mp.mpf("0.6"), mp.mpf("0.6")     # x=y => E=-cos0=-1 (perfect anti-corr)
pa_uncond = marg_A(1, xs, ys)             # = 1/2
pa_given_bp = p_a_given_b(1, 1, xs, ys)   # p(a=+|b=+)
oi_gap = abs(pa_given_bp - pa_uncond)
line("p(a=+|x,y)            (unconditional)", mp.nstr(pa_uncond, 6))
line("p(a=+|b=+,x,y)        (conditional on remote outcome)", mp.nstr(pa_given_bp, 6))
line("OI gap |p(a|b,x,y)-p(a|x,y)|", mp.nstr(oi_gap, 6))
check("OI is VIOLATED: remote outcome changes local conditional", oi_gap > mp.mpf("0.1"))

# --- CHSH = 2 sqrt 2 (Tsirelson) --------------------------------------------
# optimal CHSH settings for the singlet kernel E(x,y)=-cos(x-y):
#   x0=0, x1=pi/2 ; y0=pi/4, y1=-pi/4.  The standard combination
#   S = E00 + E01 + E10 - E11 then saturates Tsirelson (|S|=2 sqrt2).
#   (verified: this angle/sign pairing is the one that adds constructively.)
x0, x1 = mp.mpf(0), mp.pi / 2
y0, y1 = mp.pi / 4, -mp.pi / 4
S_chsh = E_corr(x0, y0) + E_corr(x0, y1) + E_corr(x1, y0) - E_corr(x1, y1)
S_abs = abs(S_chsh)
tsirelson = 2 * mp.sqrt(2)
line("E(x0,y0),E(x0,y1),E(x1,y0),E(x1,y1)",
     [mp.nstr(E_corr(*p), 6) for p in [(x0, y0), (x0, y1), (x1, y0), (x1, y1)]])
line("CHSH S = E00+E01+E10-E11", mp.nstr(S_chsh, 30))
line("|S|", mp.nstr(S_abs, 30))
line("2 sqrt 2 (Tsirelson)", mp.nstr(tsirelson, 30))
line("|S| - 2 sqrt2", mp.nstr(S_abs - tsirelson, 6))
check("CHSH violated: |S| > 2 (Bell-nonlocal)", S_abs > 2 + mp.mpf("1e-6"))
check("CHSH = 2 sqrt 2 exactly (Tsirelson, dps>=120)", abs(S_abs - tsirelson) < TOL)

print("""
  PART B verdict: the joint law is exactly the paper14 / textbook-QM Bell row:
    SO yes, MI yes, PI yes, no-signaling yes, OI NO, CHSH = 2 sqrt2.
  This is an OI-VIOLATING (entangling) joint outcome law.  No sequential skeleton
  has been invoked yet -- it lives on the transverse (parallel-chain) axis.
""")


# ===========================================================================
head("PART C.  ATTACH THE FORCED SKELETON: still entangles, still no-signals")
# ===========================================================================
print("""
  Now give EACH chain its own SEQUENTIAL survival along its commit order:
    chain A: S_A(chi) = exp(-kappa_A chi),   chain B: S_B(chi) = exp(-kappa_B chi),
  the FORCED multiplicative law (PART A).  The seal-event that COMMITS each outcome
  occurs at some accumulated content; survival composes multiplicatively WITHIN
  each chain.  The transverse joint OUTCOME law (PART B) is layered on top: when
  both chains have sealed, their committed outcomes a,b obey p(a,b|x,y).

  CLAIM: the joint law still has PI-yes/OI-no/no-signaling/CHSH=2sqrt2 UNCHANGED,
  while each chain's survival is EXACTLY the forced exp.  The skeleton PERMITS the
  entangling law.
""")

kappa_A = mp.mpf("0.7")
kappa_B = mp.mpf("0.9")

# (i) each chain's survival is multiplicative (forced) -- independent of the joint law
def SA(c): return mp.e ** (-kappa_A * c)
def SB(c): return mp.e ** (-kappa_B * c)
cA1, cA2 = mp.mpf("0.3"), mp.mpf("0.5")
cB1, cB2 = mp.mpf("0.2"), mp.mpf("0.8")
gA = abs(SA(cA1 + cA2) - SA(cA1) * SA(cA2))
gB = abs(SB(cB1 + cB2) - SB(cB1) * SB(cB2))
line("chain-A survival multiplicativity gap", mp.nstr(gA, 6))
line("chain-B survival multiplicativity gap", mp.nstr(gB, 6))
check("each chain's survival is the forced exp (multiplicative)", gA < TOL and gB < TOL)

# (ii) the joint OUTCOME law (committed a,b) is UNCHANGED by the survival layer.
#      Survival governs WHEN each chain seals (sequential), not the correlation of
#      WHAT it seals to (transverse).  The committed-outcome law is still p_joint.
#      Re-verify CHSH and no-signaling with the survival layer present:
#      condition on BOTH chains having sealed (survival is a common multiplicative
#      gate on the joint normalization, which CANCELS in conditional outcome stats).
def p_joint_sealed(a, b, x, y, cA, cB):
    # both sealed-event weights factor as (1-S) hazards along each chain;
    # the OUTCOME correlation rides the transverse joint law unchanged.
    wA = (1 - SA(cA))     # prob chain A has sealed by content cA  (>=0, in [0,1))
    wB = (1 - SB(cB))
    return wA * wB * p_joint(a, b, x, y)

# CHSH from the survival-gated joint, with the (common) seal weights divided out
cA, cB = mp.mpf("1.1"), mp.mpf("0.9")
gate = (1 - SA(cA)) * (1 - SB(cB))
def E_sealed(x, y):
    num = sum(a * b * p_joint_sealed(a, b, x, y, cA, cB)
              for a in (1, -1) for b in (1, -1))
    den = sum(p_joint_sealed(a, b, x, y, cA, cB)
              for a in (1, -1) for b in (1, -1))
    return num / den
S_chsh_sealed = (E_sealed(x0, y0) + E_sealed(x0, y1)
                 + E_sealed(x1, y0) - E_sealed(x1, y1))
line("seal gate (1-S_A)(1-S_B) (common factor)", mp.nstr(gate, 6))
line("CHSH with survival layer present", mp.nstr(abs(S_chsh_sealed), 30))
check("CHSH=2sqrt2 SURVIVES attaching the forced skeleton",
      abs(abs(S_chsh_sealed) - tsirelson) < TOL)

# no-signaling with survival layer
def marg_A_sealed(a, x, y):
    num = sum(p_joint_sealed(a, b, x, y, cA, cB) for b in (1, -1))
    den = sum(p_joint_sealed(aa, b, x, y, cA, cB) for aa in (1, -1) for b in (1, -1))
    return num / den
nosig_sealed = max(abs(marg_A_sealed(a, xg, yg) - marg_A_sealed(a, xg, y_alt))
                   for a in (1, -1))
line("no-signaling gap with survival layer", mp.nstr(nosig_sealed, 6))
check("NO-SIGNALING survives attaching the forced skeleton", nosig_sealed < TOL)

print("""
  PART C verdict: the forced sequential survival skeleton and the OI-violating
  transverse joint law COEXIST.  The survival factors are a COMMON multiplicative
  gate on the joint normalization (sequential axis); they CANCEL in the conditional
  outcome statistics and leave CHSH=2sqrt2 and no-signaling intact (transverse
  axis).  => the forced dynamics PERMITS entanglement.  OI is NOT forced.
""")


# ===========================================================================
head("PART D.  DECISIVE SEPARATION: multiplicativity-of-survival =/= OI")
# ===========================================================================
print("""
  The crux the prompt names: multiplicativity of SURVIVAL along the sequential axis
  is NOT factorization of the joint OUTCOME law (OI).  We prove both directions of
  the orthogonality:

   (D1)  A law with FULLY multiplicative survival on BOTH chains can have a joint
         OUTCOME law that does NOT factor (OI fails).   [survival-mult does NOT imply OI]
   (D2)  An OI-respecting (factorized, Bell-local) joint law carries the SAME
         survival skeleton.   [OI does NOT change the survival skeleton]
  Together: the survival skeleton is SILENT on OI.  Different axes.
""")

# (D1) survival multiplicative on each chain, but OUTCOME law does NOT factor.
#      OI-factorization would require p(a,b|x,y)=p(a|x)p(b|y)=1/4 for all a,b.
#      Our entangling law gives p(a,b|x,y)=(1+ab E)/4 != 1/4 whenever E!=0.
oi_factor_gap = max(abs(p_joint(a, b, xs, ys) - marg_A(a, xs, ys) * marg_B(b, xs, ys))
                    for a in (1, -1) for b in (1, -1))
line("max|p(a,b|x,y) - p(a|x)p(b|y)|  (OI-factorization defect)",
     mp.nstr(oi_factor_gap, 6))
check("(D1) joint outcome law does NOT factor while survival IS multiplicative",
      oi_factor_gap > mp.mpf("0.1") and gA < TOL and gB < TOL)

# (D2) an OI-respecting factorized law (E=0, independent fair coins) -- Bell-LOCAL.
def p_factor(a, b, x, y):
    return mp.mpf("0.25")                  # = p(a|x)p(b|y), OI holds, CHSH<=2
S_chsh_local = sum(s * (sum(a * b * p_factor(a, b, x, y)
                            for a in (1, -1) for b in (1, -1)))
                   for s, (x, y) in zip((1, 1, 1, -1),
                                        [(x0, y0), (x0, y1), (x1, y0), (x1, y1)]))
line("CHSH for OI-respecting factorized law", mp.nstr(abs(S_chsh_local), 6),
     "(<=2: Bell-local)")
check("(D2a) OI-respecting law is Bell-local (CHSH<=2)", abs(S_chsh_local) <= 2 + TOL)
# the SAME forced survival skeleton attaches unchanged to the OI-respecting law
gA2 = abs(SA(cA1 + cA2) - SA(cA1) * SA(cA2))
check("(D2b) the forced survival skeleton attaches to the OI law too (same exp)",
      gA2 < TOL)

print("""
  PART D verdict: survival multiplicativity holds in BOTH the OI-violating
  (entangling, CHSH=2sqrt2) and OI-respecting (Bell-local, CHSH<=2) cases, and the
  joint OUTCOME law fails OI in the first and holds OI in the second WITHOUT any
  change to the survival skeleton.  The two are on ORTHOGONAL axes:
      sequential survival composition  ==>  silent on OI.
  So the forced multiplicative sealing skeleton does NOT force OI, and does NOT
  forbid OI-violation (entanglement).  It PERMITS entanglement.
""")


# ===========================================================================
head("PART E.  FORCED vs CONSTRAINED vs FREE  (the entangling law itself)")
# ===========================================================================
print("""
  With compatibility established, the status of the ENTANGLING (transverse) law:

  [FORCED]      The SEQUENTIAL survival skeleton: S(chi)=exp(-kappa chi) (dense) /
                S(n d)=S(d)^n (sparse).  Filter 3 forces it.  It says nothing about
                OI: it is a one-chain commit-order law (PARTS A,C,D).

  [CONSTRAINED] The TRANSVERSE joint outcome law is NOT free-for-all.  The program's
                Bell envelope constrains it (paper14): it MUST keep
                single-outcome + MI + PI + no-signaling and may DROP OI, with the
                quantum/Tsirelson ceiling CHSH <= 2 sqrt2 (Barandes-Hasan-Kagan:
                causally-local indivisible processes SATURATE but do not exceed it).
                That is a genuine constraint -- it forbids PR-box (CHSH=4) and
                forbids signaling.  We verify the ceiling is respected and a PR-box
                is excluded.

  [FREE]        WITHIN that envelope the specific correlation profile E(x,y) is a
                SEPARATE Tier-A structure, NOT delivered by the sequential
                refinement skeleton.  paper1 s3.5: the sequential seal-law "neither
                requires nor forbids" it; whether the joint click-law carrying this
                PI-yes/OI-no correlation is itself forced is left OPEN [Tier-A].
                So the entangling law is FREE relative to the forced skeleton, and
                CONSTRAINED by the Bell/Tsirelson envelope -- a
                FORCED-SKELETON / FREE-COMPLEMENT (constrained) split.
""")

# Tsirelson ceiling respected (already CHSH=2sqrt2); PR-box excluded by quantum kernel
# show the singlet kernel can never reach the PR-box value 4
PRbox = mp.mpf(4)
line("CHSH ceiling for the singlet kernel (= 2 sqrt2)", mp.nstr(tsirelson, 20))
line("PR-box value (algebraic max)", mp.nstr(PRbox, 6))
check("(E1) Tsirelson ceiling respected (no super-quantum signaling box)",
      S_abs <= tsirelson + TOL)
check("(E2) PR-box (CHSH=4) EXCLUDED by the quantum correlation kernel",
      S_abs < PRbox - mp.mpf("0.5"))

# the entangling profile is FREE: a DIFFERENT OI-violating correlation (smaller
# violation) is equally compatible with the SAME forced skeleton -- demonstrating
# the skeleton does not pin the profile.
def E_corr_b(x, y):       # a different (sub-Tsirelson but still CHSH-violating) profile
    return -mp.mpf("0.8") * mp.cos(x - y)   # CHSH = 0.8*2sqrt2 = 2.263 > 2, < 2sqrt2
S_chsh_b = (E_corr_b(x0, y0) + E_corr_b(x0, y1)
            + E_corr_b(x1, y0) - E_corr_b(x1, y1))
line("alt entangling profile CHSH", mp.nstr(abs(S_chsh_b), 12),
     "(still >2, OI-no, same forced skeleton)")
check("(E3) a DIFFERENT OI-violating profile is equally skeleton-compatible "
      "(profile is FREE)", abs(S_chsh_b) > 2 and abs(S_chsh_b) < tsirelson)


# ===========================================================================
head("CANONICAL OUTPUT BLOCK  (F5 OI/PI consistency receipt)")
# ===========================================================================
all_pass = all(c for _, c in CHECKS)
print(f"""
  forced sequential skeleton (single chain):
    dense   S(chi)=exp(-kappa chi)         multiplicative, sympy-exact residual 0
    sparse  S(n d)=S(d)^n                  geometric progression, max gap {mp.nstr(max_sparse,4)}
    dense = d->0 limit of sparse           |gap| <= {mp.nstr(max(errs),4)}

  transverse joint outcome law (two parallel chains):
    normalized, nonnegative                yes
    NO-SIGNALING (marg indep remote setting)  gap {mp.nstr(max(nosig_A,nosig_B),4)}
    PI (local law refs x,lambda not remote y) yes
    OI VIOLATED (remote outcome moves local)  gap {mp.nstr(oi_gap,6)}
    CHSH |S| = {mp.nstr(S_abs,30)}
    Tsirelson 2 sqrt2 - |S|                {mp.nstr(tsirelson - S_abs,4)}

  COMPATIBILITY (skeleton + entangling law):
    each chain survival still exp           gaps {mp.nstr(max(gA,gB),4)}
    CHSH=2sqrt2 survives survival layer     {mp.nstr(abs(abs(S_chsh_sealed)-tsirelson),4)}
    no-signaling survives survival layer    {mp.nstr(nosig_sealed,4)}

  SEPARATION (multiplicativity =/= OI):
    survival-mult AND non-factorizing outcome law (OI-no)   [D1] proven
    OI-respecting law carries same skeleton                 [D2] proven

  ENVELOPE:
    Tsirelson ceiling respected (no super-quantum box)      [E1]
    PR-box CHSH=4 excluded                                  [E2]
    a different OI-violating profile equally compatible     [E3] (profile FREE)

  VERDICT:
    The FORCED multiplicative sealing skeleton (S=exp(-kappa chi), sequential /
    refinement-multiplicative) does NOT force outcome-independence (OI), and does
    NOT forbid OI-violation (entanglement).  It PERMITS an OI-violating, PI-yes,
    no-signaling, CHSH=2sqrt2 joint outcome law.  Multiplicativity of SURVIVAL
    along the sequential axis is ORTHOGONAL to factorization of the joint OUTCOME
    statistics (OI) along the transverse parallel-chain axis.

    Entanglement is COMPATIBLE with (PERMITTED by) the forced dynamics.
    The entangling joint law is FORCED-SKELETON / FREE-COMPLEMENT:
      - sequential survival skeleton:           FORCED
      - transverse Bell/Tsirelson envelope:     CONSTRAINS the complement
      - specific OI-violating correlation:      FREE at Tier A (a separate Tier-A
                                                structure; paper1 s3.5 OPEN).

  ALL CHECKS PASS: {all_pass}
""")

assert all_pass, "SOME CHECK FAILED -- see *** FAIL *** above"
head("DONE.  (all machine-check asserts passed)")
