"""
v7  --  pK1_seal_information_rate.py
THE kappa = 1 CRUX:  does the seal commit at exactly the information rate?

The forced click-law is  |rho_01| = exp(-kappa * chi), chi = accumulated seal
content.  The paper56 [TARGET] "decoherence rate = seal rate = sigma" amounts, in
DIMENSIONLESS per-content terms, to the saturation claim  kappa = -d log|rho_01|/dchi
= 1: one nat of recorded distinguishability costs exactly e^-1 of coherence.

This receipt settles whether kappa is (a) =1 (saturation), (b) a FIXED number != 1
(forced but sub-unit), or (c) free -- and shows the answer hinges ENTIRELY on WHICH
information measure the "seal rate sigma" is.

PHYSICS.  Model the dense seal as a weak which-path RECORDING: path j in {0,1}
(uniform prior) leaves a classical record drawn from P_j(x); P_1 = P_0 + s*delta a
weak perturbation (Sum delta = 0).  Two INDEPENDENTLY-defined quantities:
  * COHERENCE LOSS per seal:  |rho_01| -> |rho_01| * BC,  BC = Sum_x sqrt(P_0 P_1)
    the record overlap (Bhattacharyya coefficient).  d(-log|rho_01|) = -log BC = D_B
    the Bhattacharyya distance (a Renyi-1/2 quantity).
  * SEAL CONTENT / ENTROPY PRODUCTION sigma: several candidate measures --
      sigma_KL   = D(P_0 || P_1)                 (a pairwise KL = Renyi-1; SHARD's
                                                  sigma = D(P_AB||P_BA) is of THIS type)
      sigma_symKL= (1/2)[D(P0||P1)+D(P1||P0)]    (symmetrized)
      sigma_JSD  = I(path : record) = JSD(P0,P1) (the RECORDED MUTUAL INFORMATION /
                                                  which-path info actually committed)

  kappa_X = D_B / sigma_X.

THE RESULT (derived + verified):  in the dense (weak-seal) limit s->0 EVERY divergence
reduces to the Fisher form J = Sum delta^2/P_0 with a Renyi-ORDER-dependent prefactor:
      D_B   -> (1/8) J s^2     (order 1/2)
      D_KL  -> (1/2) J s^2     (order 1)
      JSD   -> (1/8) J s^2     (the mutual information)
Hence, DISTRIBUTION-INDEPENDENTLY (forced):
      kappa_JSD  = D_B / JSD   -> 1     <-- SATURATION holds, but ONLY for sigma = the
                                            recorded mutual information (JSD).
      kappa_KL   = D_B / D_KL  -> 1/4   <-- for SHARD's actual pairwise-KL sigma,
                                            kappa = 1/4, NOT 1.

VERDICT (honest):  kappa is FORCED (not free) in the dense limit -- but its value is
set by the Renyi-ORDER of the chosen sigma.  The paper56 [TARGET] kappa=1 is TRUE iff
"the seal rate" is identified with the recorded WHICH-PATH MUTUAL INFORMATION (JSD) --
which is exactly the decoherence-equals-information-gain complementarity (Landauer-
saturation), a known-in-substance result.  With SHARD's stated sigma = D(P_AB||P_BA)
(a pairwise KL, Renyi-1, asymmetric) kappa = 1/4 != 1: decoherence and entropy
production stay PROPORTIONAL with a forced universal constant, but are NOT equal.
=> the literal [TARGET] (sigma = the KL) is FALSE; the saturation lives in a different
information measure.  Either way kappa is pinned, separable from the scale no-go.

PRIOR ART (this receipt CONSOLIDATES + classifies, it does NOT discover):
  * kappa=1/4 for the KL is ALREADY a corpus theorem -- v6 paper26 Theorem A, the
    "quarter law" -ln BC = sigma/4 + O(sigma^2).  This receipt's contribution is only
    the RENYI-ORDER EXPLANATION of why 1/4 (coherence = order-1/2, KL = order-1) and
    the observation that switching KL->JSD recovers the factor 4 (kappa=1).
  * kappa=1 (coherence loss = mutual information recorded) is the KNOWN decoherence-
    information complementarity: Englert duality (PRL 77, 2154, 1996), Zurek
    (Rev.Mod.Phys.75, 715, 2003), "Decoherence Implies Information Gain"
    (Phys.Rev.Research 7, L012040, 2024 / arXiv:2402.16740).
  * SHARD's sigma = D(P_AB||P_BA) is a genuine ASYMMETRIC pairwise KL (the forward-
    reverse structure does NOT symmetrize it to a JSD), so its Renyi order is 1 and
    kappa=1/4 IS the right number -- PROVIDED sigma governs the logical-coherence decay
    at all, which is the unbuilt seal-history functor (paper56 sec 2.2).  This receipt
    therefore DISSOLVES the [TARGET]'s equality framing but PUNTS that bridge.
  NET: not a new theorem -- a consolidation/dissolution; the [TARGET] kappa=1 is FALSE
  for SHARD's KL (=1/4, paper26) and KNOWN where true (JSD = complementarity).

PRECISION: mpmath dps=120 (numeric convergence) + sympy-exact leading-order Fisher
coefficients.  NEVER float64.

Date: 2026-06-17.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 120
TOL = mp.mpf(10) ** (-90)

def head(s):
    print("\n" + "=" * 78); print(s); print("=" * 78)

def line(label, val, extra=""):
    print(f"  {label:<58} {val} {extra}")

CHECKS = []
def check(name, cond, extra=""):
    CHECKS.append((name, bool(cond)))
    line("CHECK  " + name, "PASS" if cond else "*** FAIL ***", extra)
    return bool(cond)


# ===========================================================================
head("STEP 1.  SYMPY-EXACT WEAK-LIMIT COEFFICIENTS (the forced ratios)")
# ===========================================================================
print("""
  2-outcome record P0=(a,1-a), P1=(a+s,1-a-s) (delta=(1,-1), Sum delta=0).
  Expand each divergence to O(s^2); the Fisher form is J = 1/a + 1/(1-a).
  D_B (Bhattacharyya distance), D_KL, D_symKL, JSD -- read off the s^2 coefficient
  and divide by J to expose the Renyi-order prefactor.  kappa_X = D_B / sigma_X.
""")
a, s = sp.symbols('a s', positive=True)
P0 = [a, 1 - a]
P1 = [a + s, 1 - a - s]
J = sp.simplify(1/a + 1/(1 - a))                          # Fisher form for delta=(1,-1)

def series_s2(expr):
    """leading s^2 coefficient of expr (expr = O(s^2)); robust to nested sqrt/log
    via the limit expr/s^2 -> coeff (avoids sympy series().coeff() sqrt-branch bug)."""
    return sp.simplify(sp.limit(expr / s**2, s, 0))

# Bhattacharyya distance D_B = -log(BC),  BC = Sum sqrt(P0 P1).
# sympy's limit/series chokes on log(sum-of-sqrts) AND on the sqrt-sum directly, so
# expand each sqrt term separately (sympy handles series of sqrt(a^2+a s) fine), sum,
# read the s^2 coeff of BC, and use D_B = -log(1+(BC-1)) = -(BC-1)+O(s^4) (BC-1=O(s^2)).
BC_terms = [sp.sqrt(P0[i]*P1[i]) for i in range(2)]
BC_ser = sum(sp.series(t, s, 0, 3).removeO() for t in BC_terms)
# the sqrt((1-a)(1-a-s)) series introduces |a-1|; on the simplex 0<a<1 it is (1-a):
c_BC = sp.expand(BC_ser).coeff(s, 2).subs(sp.Abs(a - 1), 1 - a)
c_DB = sp.simplify(-c_BC)                    # leading s^2 coeff of D_B
# KL D(P0||P1)
D_KL = P0[0]*sp.log(P0[0]/P1[0]) + P0[1]*sp.log(P0[1]/P1[1])
c_KL = series_s2(D_KL)
# symmetrized KL
D_KL_rev = P1[0]*sp.log(P1[0]/P0[0]) + P1[1]*sp.log(P1[1]/P0[1])
D_symKL = (D_KL + D_KL_rev)/2
c_sym = series_s2(D_symKL)
# Jensen-Shannon / mutual information of (uniform path : record)
M = [(P0[0]+P1[0])/2, (P0[1]+P1[1])/2]
JSD = (P0[0]*sp.log(P0[0]/M[0]) + P0[1]*sp.log(P0[1]/M[1])
       + P1[0]*sp.log(P1[0]/M[0]) + P1[1]*sp.log(P1[1]/M[1]))/2
c_JSD = series_s2(JSD)

for nm, c, want in [("D_B  (Bhattacharyya, order 1/2)", c_DB, sp.Rational(1,8)),
                    ("D_KL (order 1)", c_KL, sp.Rational(1,2)),
                    ("D_symKL", c_sym, sp.Rational(1,2)),
                    ("JSD  (mutual information)", c_JSD, sp.Rational(1,8))]:
    ratio = sp.simplify(c / J)
    line(f"1  s^2 coeff of {nm} / J", ratio)
    check(f"1: {nm} -> ({want}) * J * s^2  (sympy-exact Fisher reduction)",
          sp.simplify(ratio - want) == 0)

kappa_KL_exact  = sp.simplify(c_DB / c_KL)
kappa_JSD_exact = sp.simplify(c_DB / c_JSD)
kappa_sym_exact = sp.simplify(c_DB / c_sym)
line("1  kappa_KL  = coeff(D_B)/coeff(D_KL)", kappa_KL_exact)
line("1  kappa_symKL", kappa_sym_exact)
line("1  kappa_JSD = coeff(D_B)/coeff(JSD)", kappa_JSD_exact)
check("1: kappa_JSD = 1 EXACTLY (saturation) -- coherence loss = recorded mutual info",
      kappa_JSD_exact == 1)
check("1: kappa_KL = 1/4 EXACTLY (SHARD's pairwise-KL sigma) -- NOT 1, but FORCED",
      kappa_KL_exact == sp.Rational(1, 4))
check("1: kappa_symKL = 1/4 EXACTLY", kappa_sym_exact == sp.Rational(1, 4))
check("1: the ratios are DISTRIBUTION-INDEPENDENT (a cancels) => FORCED, not free",
      a not in kappa_KL_exact.free_symbols and a not in kappa_JSD_exact.free_symbols)


# ===========================================================================
head("STEP 2.  NUMERIC CONFIRMATION (dps=120), MANY DISTRIBUTIONS, DENSE LIMIT")
# ===========================================================================
print("""
  n-outcome records, several base P0 and shift directions delta (Sum delta=0),
  strength s -> 0.  Confirm kappa_JSD -> 1 and kappa_KL -> 1/4 universally.
""")
def normalize(v):
    tot = sum(v); return [x/tot for x in v]

def bhatt_dist(P0, P1):
    return -mp.log(sum(mp.sqrt(p0*p1) for p0, p1 in zip(P0, P1)))

def kl(P0, P1):
    return sum(p0*mp.log(p0/p1) for p0, p1 in zip(P0, P1))

def jsd(P0, P1):
    M = [(p0+p1)/2 for p0, p1 in zip(P0, P1)]
    return (kl(P0, M) + kl(P1, M))/2

bases = [
    normalize([mp.mpf("0.25")]*4),                                  # uniform 4
    normalize([mp.mpf("0.4"), mp.mpf("0.3"), mp.mpf("0.2"), mp.mpf("0.1")]),
    normalize([mp.mpf("0.05"), mp.mpf("0.6"), mp.mpf("0.15"), mp.mpf("0.2")]),
    normalize([mp.mpf("0.5"), mp.mpf("0.5")]),                      # binary
]
shifts = [
    [mp.mpf("1"), mp.mpf("-1"), mp.mpf("0.5"), mp.mpf("-0.5")],
    [mp.mpf("0.7"), mp.mpf("-0.2"), mp.mpf("-0.3"), mp.mpf("-0.2")],
    [mp.mpf("-0.6"), mp.mpf("0.1"), mp.mpf("0.2"), mp.mpf("0.3")],
    [mp.mpf("1"), mp.mpf("-1")],
]
s_small = mp.mpf("1e-15")            # deep dense limit; KL converges as O(s) so need s<<1e-12
                                     # (JSD converges O(s^2)); divergences ~1e-30, fine at dps=120
worst_JSD = mp.mpf(0); worst_KL = mp.mpf(0)
for bi, (P0, dlt) in enumerate(zip(bases, shifts)):
    if len(dlt) != len(P0):
        continue
    # project delta to Sum=0 (already), build P1
    dsum = sum(dlt); dlt = [d - dsum/len(dlt) for d in dlt]
    P1 = [p + s_small*d for p, d in zip(P0, dlt)]
    DB = bhatt_dist(P0, P1); KLv = kl(P0, P1); JS = jsd(P0, P1)
    kJSD = DB/JS; kKL = DB/KLv
    line(f"2  base#{bi}: kappa_JSD", mp.nstr(kJSD, 18), f" kappa_KL {mp.nstr(kKL, 16)}")
    worst_JSD = max(worst_JSD, abs(kJSD - 1))
    worst_KL = max(worst_KL, abs(kKL - mp.mpf(1)/4))
line("2  worst |kappa_JSD - 1| over all bases", mp.nstr(worst_JSD, 6))
line("2  worst |kappa_KL - 1/4| over all bases", mp.nstr(worst_KL, 6))
check("2: kappa_JSD -> 1 for ALL distributions (dense limit, dps=120)",
      worst_JSD < mp.mpf("1e-12"), "saturation is universal (forced)")
check("2: kappa_KL -> 1/4 for ALL distributions (dense limit, dps=120)",
      worst_KL < mp.mpf("1e-12"), "the pairwise-KL coefficient is universal (forced)")


# ===========================================================================
head("STEP 3.  FINITE-s: the universal value is the DENSE limit only")
# ===========================================================================
print("""
  At FINITE seal strength s the ratio kappa runs and is distribution-dependent; only
  the dense (s->0) limit is universal.  This matches the corpus: the exponential law
  |rho_01|=exp(-kappa chi) is the DENSE/divisible regime.  We show kappa_KL(s) drifts
  from 1/4 as s grows (so the forced value is a limit statement, honestly scoped).
""")
P0 = normalize([mp.mpf("0.4"), mp.mpf("0.3"), mp.mpf("0.2"), mp.mpf("0.1")])
dlt = [mp.mpf("0.7"), mp.mpf("-0.2"), mp.mpf("-0.3"), mp.mpf("-0.2")]
dsum = sum(dlt); dlt = [d - dsum/len(dlt) for d in dlt]
prev = None
for sv in [mp.mpf("1e-1"), mp.mpf("1e-2"), mp.mpf("1e-3"), mp.mpf("1e-4")]:
    P1 = [max(p + sv*d, mp.mpf("1e-90")) for p, d in zip(P0, dlt)]
    P1 = normalize(P1)
    kKL = bhatt_dist(P0, P1)/kl(P0, P1)
    line(f"3  s={mp.nstr(sv,2)}: kappa_KL", mp.nstr(kKL, 16), f" |-1/4| {mp.nstr(abs(kKL-mp.mpf(1)/4),6)}")
    prev = kKL
check("3: kappa_KL(s) -> 1/4 as s->0 (the universal value is the dense limit)",
      abs(prev - mp.mpf(1)/4) < mp.mpf("1e-3"),
      "finite-s kappa is distribution-dependent; only the limit is forced (honest scope)")


# ===========================================================================
head("VERDICT")
# ===========================================================================
all_pass = all(c for _, c in CHECKS)
n_pass = sum(1 for _, c in CHECKS if c); n_tot = len(CHECKS)
print(f"""
  THE kappa CRUX -- resolved:
    * kappa is NOT free and NOT a convention: in the dense limit it is FORCED to a
      distribution-INDEPENDENT value, set purely by the RENYI-ORDER of the chosen
      seal-rate measure (sympy-exact Fisher reduction, Step 1; numeric Step 2).
    * kappa = 1 (the paper56 [TARGET] saturation) holds IFF sigma = the recorded
      WHICH-PATH MUTUAL INFORMATION (JSD): coherence-loss EXACTLY equals information
      recorded -- the decoherence=information-gain complementarity (Landauer-
      saturation), a clean but KNOWN-IN-SUBSTANCE identity.
    * WITH SHARD's actual sigma = D(P_AB||P_BA) (a pairwise KL, Renyi-1), kappa = 1/4:
      decoherence and entropy production are PROPORTIONAL with a forced universal
      constant, but NOT equal.  The literal [TARGET] kappa=1 is FALSE for the KL.
    * Either way kappa is dimensionless and separable from the scale no-go (it is a
      weight-0 forced number) -- so the [TARGET] does NOT need the un-fixable rate.

  CONSEQUENCE for publishability: the genuinely-true, clean theorem is the
  JSD-saturation (decoherence per seal = mutual information recorded), which is the
  known complementarity in record language -- modest novelty.  The SHARD-specific
  claim (kappa=1 for the KL sigma) is refuted: kappa=1/4.  The [TARGET] is best
  DISSOLVED: "decoherence = entropy production" is a proportionality with a forced
  Renyi-order constant (1/4 for KL), and an EQUALITY only for the mutual-information
  measure.

  ALL CHECKS PASS: {all_pass}   ({n_pass}/{n_tot})
""")
assert all_pass, "SOME CHECK FAILED"
print(f"ALL CHECKS PASS ({n_pass}/{n_tot})")
head("DONE.  (mpmath dps=%d; sympy-exact weak-limit coefficients)" % mp.mp.dps)
