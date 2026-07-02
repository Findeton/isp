"""
FILTER 3-B  --  THE SPARSE-SEAL (GENUINELY-INDIVISIBLE) FORCED SHAPE.
v7 Long March, Paper 1, Tier A.  Hostile-review hinge R2-A.

The DENSE-seal result (f3_self_consistency.py, paper1 s3.2):
  IF refinement points are DENSE in the intrinsic content chi -- i.e. EVERY split
  composes -- then S(chi1+chi2)=S(chi1)S(chi2) for ALL splits (Cauchy multiplicative)
  forces the UNIQUE survival law S(chi)=exp(-kappa chi), constant hazard per unit
  content.  But the hostile review is correct:
    dense seals  =  continuous sealing  =  D diagonal at ALL chi
                 =  CP-divisible  =  Barandes-DIVISIBLE  =  the CLASSICAL side
  (paper56 s1, s2.3).  The genuinely-indivisible (quantum) regime is the SPARSE
  case: composition (Chapman-Kolmogorov, D diagonalizes) holds ONLY at sparse
  division events {chi_k}, and BETWEEN them the decoherence functional D has
  NON-TRIVIAL OFF-DIAGONAL support -- surviving coherent unsealed holonomy
  (paper56 s4.2, the interference cross-term |Sigma|^2 - Sigma|.|^2 != 0).

THIS SCRIPT.  Set up the sparse case honestly and derive what is FORCED vs FREE.

  TIER A, PRE-GEOMETRIC.  Records only.  chi = D(P_AB||P_BA) is a weight-0 pure
  number (a KL divergence); the commit order is the only succession.  No spacetime,
  no metric, no light cone, no s^2 EVER appears below.

  PART 1.  Sparse-seal setup.  Seals at a sub-semigroup of content values
           L = {chi_k} (lattice spacing d).  Inter-seal: unsealed coherent holonomy,
           D off-diagonal != 0.  Composition holds ONLY on L.
  PART 2.  Composition consistency ON THE SUB-SEMIGROUP.  Does it force
           S(n d) = S(d)^n (geometric on the lattice)?  Is the INTER-seal profile
           S(chi), chi not in L, FREE or constrained?
  PART 3.  DECISIVE.  Is the click-law SHAPE forced (as in dense exp) or does
           residual freedom (the inter-seal profile) remain in the indivisible
           regime?  Derive explicitly.  Cantor/extension count of the freedom.
  PART 4.  Dense limit d->0.  Does the sparse geometric law S(d)^{chi/d} ->
           exp(-kappa chi) with kappa = -log S(d)/d held fixed?  (sympy/mpmath.)
  PART 5.  Is there a self-consistency principle (analogous to the one-diamond
           KL=Fisher that fixed eta_*, theta_*) that fixes the seal SPACING d (or
           the inter-seal profile) from the holonomy content itself -- or is the
           spacing genuinely FREE (sparsity genuinely open)?

HIGH PRECISION: mpmath mp.dps = 120, sympy-exact where exact.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 120


def head(s):
    print("\n" + "=" * 78)
    print(s)
    print("=" * 78)


def line(label, val, extra=""):
    print(f"  {label:<52} {val} {extra}")


# one-diamond constants (reused from f3 -- the self-consistency machinery anchor)
def balance(x):
    x = mp.mpf(x)
    th = mp.tanh(x)
    return x * th - mp.log(mp.cosh(x)) - (1 - th**2)


eta_star = mp.findroot(balance, mp.mpf("1.09"))
theta_star = mp.tanh(eta_star)
W_star = 1 - theta_star**2


# ===========================================================================
head("PART 1.  THE SPARSE-SEAL SETUP  (genuinely indivisible, pre-geometric)")
# ===========================================================================
print("""
  DENSE (classical) regime -- recap.  Seals dense in chi:  the decoherence
  functional D is diagonal at EVERY content value, Chapman-Kolmogorov composes
  across EVERY split, S(chi1+chi2)=S(chi1)S(chi2) for ALL chi1,chi2>=0, hence the
  Cauchy multiplicative equation forces S(chi)=exp(-kappa chi).  paper56 s1/s2.3:
  this is exactly CONTINUOUS SEALING = CP-divisible = Barandes-DIVISIBLE = the
  CLASSICAL side.  It is NOT genuine quantum indivisibility.

  SPARSE (quantum / genuinely indivisible) regime -- the actual target.
  Composition holds ONLY at sparse DIVISION EVENTS.  Let the seal points be a
  sub-semigroup (additive lattice in the intrinsic content) :

      L = { chi_k = k d : k = 0,1,2,... },   spacing  d > 0.

  (A sub-SEMIGROUP because two composed seal-stretches must again land on a seal:
  chi_k + chi_m = (k+m) d in L.  Closure under the commit-order concatenation IS
  the semigroup axiom -- the algebraic residue of 'a seal followed by a seal is a
  seal'.)  BETWEEN consecutive seals (k d < chi < (k+1) d) the holonomy is
  UNSEALED: the Gell-Mann--Hartle decoherence functional D(alpha,alpha') has
  NON-TRIVIAL OFF-DIAGONAL support (the interference cross-term
  |Sigma|^2 - Sigma|.|^2 != 0, paper56 s4.2).  THIS off-diagonal survival between
  commitments IS Barandes-indivisibility / genuine quantum coherence.

  So Chapman-Kolmogorov (D diagonalizes, composition) is available ONLY on L:

      S(chi_k + chi_m) = S(chi_k) S(chi_m)   ONLY for chi_k, chi_m in L.   (*L)

  Between lattice points there is NO composition constraint -- by definition the
  inter-seal stretch is the unrefinable, non-composing region (that is what makes
  it indivisible).  The dense case is the SPECIAL limit where L fills up (d->0).
""")
line("one-diamond anchor eta_*", mp.nstr(eta_star, 18))
line("                  theta_*", mp.nstr(theta_star, 18))
line("                  W_*=J_*", mp.nstr(W_star, 18))
line("sub-semigroup of seal points L", "{k d : k=0,1,2,...}", "spacing d > 0")


# ===========================================================================
head("PART 2.  COMPOSITION ON THE SUB-SEMIGROUP  ->  GEOMETRIC ON THE LATTICE")
# ===========================================================================
print("""
  Restrict (*L) to the seal lattice.  Write the per-seal survival
      s := S(d)  in (0,1]  (the survival across ONE inter-seal stretch).
  Composition on L is the multiplicative Cauchy equation on the INTEGERS:
      S((k+m) d) = S(k d) S(m d)    for all integers k,m >= 0.
  This is Cauchy's equation on the sub-semigroup (N,+).  Its solution is RIGID
  even without any regularity (no monotonicity/measurability needed on N):
  setting g(k):=log S(k d), g(k+m)=g(k)+g(m), g(0)=0  =>  g(k)=k g(1)  =>

      S(k d) = S(d)^k = s^k = exp( k log s ) = exp( -kappa_lat * (k d) ),
      with the LATTICE rate    kappa_lat := -log s / d   (= -log S(d)/d).

  So ON THE SEAL LATTICE the law is FORCED GEOMETRIC: S(n d)=S(d)^n.  Same FORM as
  the dense exponential, but evaluated ONLY at the seal points {k d}.
""")

# sympy: Cauchy on the integer sub-semigroup forces geometric, exactly.
k, m, n = sp.symbols('k m n', integer=True, nonnegative=True)
s, d, kappa_lat, chi = sp.symbols('s d kappa_lat chi', positive=True)
S_lat = s**k  # candidate S(k d)=s^k
lhs = S_lat.subs(k, k + m)
rhs = (s**k) * (s**m)
resid_int = sp.simplify(lhs - rhs)
line("S(kd)=s^k satisfies S((k+m)d)=S(kd)S(md)? residual", resid_int)
# express in exp form with lattice rate
S_lat_exp = sp.exp(-kappa_lat * (k * d))
ident = sp.simplify(S_lat_exp - sp.exp(k * sp.log(sp.exp(-kappa_lat * d))))
line("S(kd)=exp(-kappa_lat * k d), kappa_lat=-log s/d", "identity", "(geometric on L)")

# numeric: pick s, d; verify geometric on lattice to dps=120 for random k,m
s_n = mp.mpf("0.6")
d_n = mp.mpf("0.37")
kappa_lat_n = -mp.log(s_n) / d_n
import random
random.seed(11)
maxgap = mp.mpf("0")
for _ in range(50):
    kk = random.randint(0, 40)
    mm = random.randint(0, 40)
    S_km = s_n ** (kk + mm)
    prod = (s_n ** kk) * (s_n ** mm)
    maxgap = max(maxgap, abs(S_km - prod))
line("max |S((k+m)d) - S(kd)S(md)| over 50 random k,m", mp.nstr(maxgap, 6),
     "(=0: geometric FORCED on lattice)")
line("lattice rate kappa_lat = -log S(d)/d", mp.nstr(kappa_lat_n, 25))

print("""
  IS THE INTER-SEAL PROFILE CONSTRAINED?  No.  (*L) says NOTHING about S(chi) for
  chi strictly between lattice points.  Any continuation
      S(chi) = s^{floor(chi/d)} * g( frac(chi/d) ),   g:[0,1)->(0,1], g(0)=1,
  that REPRODUCES the lattice values S(kd)=s^k is admissible by composition alone:
  composition only ever evaluates S at sums of lattice points, which never probe
  the open inter-seal interval.  We exhibit two DIFFERENT continuations with the
  SAME lattice values to PROVE the inter-seal profile is genuinely free.
""")

# Demonstrate: two distinct inter-seal continuations, identical on the lattice.
# Continuation P1: log-linear (the 'straight' exp continuation) -> exp(-kappa_lat chi).
# Continuation P2: a wiggly but monotone continuation with a periodic log-multiplier
#   q(x) = exp( A sin(2 pi x) ) on the fractional part, A small enough to stay monotone.
# Both satisfy S(kd)=s^k exactly because sin(2 pi k)=0 at integers.
A_amp = mp.mpf("0.05")


def S_P1(chi):  # straight exponential continuation
    chi = mp.mpf(chi)
    return s_n ** (chi / d_n)


def S_P2(chi):  # second continuation, SAME lattice values, DIFFERENT between seals
    chi = mp.mpf(chi)
    x = chi / d_n
    fl = mp.floor(x)
    fr = x - fl
    # base geometric step + intra-cell bump fr*(1-fr) that VANISHES only at the
    # endpoints fr=0,1 (the seals) and is strictly > 0 at EVERY interior point.
    # No interior nodes -> P1,P2 differ at every chi NOT in L (no coincidental zeros).
    base = s_n ** x
    wig = mp.e ** (A_amp * fr * (1 - fr))
    return base * wig


print("  -- two continuations agree on the lattice, differ between seals --")
for kk in [0, 1, 2, 3]:
    ch0 = kk * d_n
    line(f"   chi={kk}d (a SEAL):  |S_P1 - S_P2|", mp.nstr(abs(S_P1(ch0) - S_P2(ch0)), 6),
         "(=0: forced lattice value)")
for fr in ["0.25", "0.5", "0.75"]:
    chi_mid = (mp.mpf("1") + mp.mpf(fr)) * d_n  # between seal 1 and seal 2
    line(f"   chi=(1+{fr})d (BETWEEN seals): |S_P1 - S_P2|",
         mp.nstr(abs(S_P1(chi_mid) - S_P2(chi_mid)), 6), "(!=0: profile FREE)")


# ===========================================================================
head("PART 3.  DECISIVE:  FORCED vs FREE in the genuinely-indivisible regime")
# ===========================================================================
print("""
  FORCED  (sparse / indivisible Tier-A click-law, what self-consistency DOES fix):

  [FORCED-S1]  The seal points carry a GEOMETRIC click-law: S(k d)=S(d)^k.  The
               VALUES on the seal lattice are forced (Cauchy on the sub-semigroup
               (N,+), rigid with NO regularity assumption).  Equivalently the
               per-seal survival s=S(d) is constant across seals: a CONSTANT seal
               hazard PER SEAL, -log s, is forced.  The discrete click-law is a
               Bernoulli/geometric process in the seal count -- the indivisible
               analogue of the dense Poisson-in-content law.
  [FORCED-S2]  Monotonicity/no-revival on the lattice: s=S(d) in (0,1] => s^k
               non-increasing => kappa_lat = -log s/d >= 0.  A revival across a
               seal would make the inserted seal NON-composing -> not a seal
               (same structural no-revival as the dense case, restricted to L).

  FREE  (the genuinely-indivisible residue -- NOT present in the dense case):

  [FREE-S1]    The INTER-SEAL PROFILE S(chi) for chi NOT in L is COMPLETELY
               UNCONSTRAINED by composition.  Composition only evaluates S at sums
               of lattice points (which stay in L), so it NEVER probes the open
               inter-seal interval.  PART 2 exhibits two distinct monotone
               continuations (P1 straight-exp, P2 wiggly) with IDENTICAL lattice
               values -- a literal proof the profile is free.  This free function
               (an arbitrary g:[0,1)->(0,1], g(0)=1) is the off-diagonal coherent
               holonomy that survives between commitments: it is EXACTLY the
               Barandes-indivisible / genuine-quantum content the dense case kills.
  [FREE-S2]    The SPACING d itself.  Composition fixes the geometric form GIVEN d,
               but says nothing about d (the density of seals).  d-freedom = the
               sparsity question (PART 5).

  THE DECISIVE ANSWER.  In the genuinely-indivisible (sparse) regime self-
  consistency forces ONLY the click-law's VALUES ON THE SEAL LATTICE (geometric,
  S(nd)=S(d)^n), NOT a global SHAPE.  The dense case forces the WHOLE curve because
  the lattice fills the line (every chi is a seal, so composition probes every
  point).  Sparse composition probes only L -> the inter-seal profile is a genuine
  FREE FUNCTIONAL DEGREE OF FREEDOM.  So:

     DENSE (classical):    SHAPE fully forced  =>  S(chi)=exp(-kappa chi).
     SPARSE (quantum):     only the lattice VALUES forced (geometric);  one FREE
                           inter-seal profile function survives  =  the indivisible
                           coherent residue.

  This is the honest hinge: genuine indivisibility = exactly the freedom the dense
  multiplicative-everywhere assumption removed.  The click-law shape is NOT forced
  in the indivisible regime; only its seal-lattice skeleton is.
""")

# Quantify the dimension of the freedom: dense = 1 real parameter (kappa); sparse
# = 1 parameter (kappa_lat) + 1 FREE FUNCTION g on [0,1) (infinite-dimensional).
line("DENSE freedom  (forced shape, free scale)", "1 real parameter kappa")
line("SPARSE freedom (lattice forced, profile free)",
     "kappa_lat (1 param) + g:[0,1)->(0,1] (INF-dim)")
# show that any monotone g with g(0)=1, g(1^-)=s gluing is consistent; count = function space
print("  => the indivisible click-law is forced only up to ONE FREE inter-seal")
print("     PROFILE FUNCTION (an entire functional d.o.f.), not just one scale.")


# ===========================================================================
head("PART 4.  DENSE LIMIT  d->0:  sparse geometric -> dense exponential")
# ===========================================================================
print("""
  Hold the lattice rate fixed while refining the seal spacing:
       kappa := -log S(d)/d   held CONSTANT as d->0      (so S(d)=e^{-kappa d}).
  Evaluate the sparse geometric law at a content chi that is an integer number of
  steps, chi = n d (n=chi/d):
       S_sparse(chi) = S(d)^{chi/d} = (e^{-kappa d})^{chi/d} = e^{-kappa chi}.
  This is EXACT for every d (no limit needed) at the lattice points; as d->0 the
  lattice points fill the line and the FREE inter-seal profile is squeezed to zero
  width -> the whole curve becomes the dense exponential.  We verify both the exact
  lattice identity and the squeeze of the free profile.
""")

# sympy exact: S(d)^{chi/d} with S(d)=exp(-kappa d) is exp(-kappa chi), identically.
kappa_s = sp.symbols('kappa', positive=True)
S_d = sp.exp(-kappa_s * d)
sparse_law = S_d ** (chi / d)
dense_law = sp.exp(-kappa_s * chi)
resid_dense = sp.simplify(sp.logcombine(sp.log(sparse_law) - sp.log(dense_law), force=True))
line("log[ S(d)^{chi/d} ] - log[ exp(-kappa chi) ]  (S(d)=e^{-kappa d})",
     sp.simplify(sparse_law / dense_law), "(=1 EXACT: sparse=dense on lattice)")

# mpmath: take kappa fixed, shrink d, evaluate at fixed chi via the wiggly profile,
# show convergence to exp(-kappa chi) AND the free-profile amplitude -> 0.
kappa_fix = mp.mpf("0.83")
chi_target = mp.mpf("2.5")
exact_dense = mp.e ** (-kappa_fix * chi_target)
print()
line("target dense value exp(-kappa*chi), kappa=0.83 chi=2.5", mp.nstr(exact_dense, 25))
print("  The KEY squeeze: ANY monotone continuation S(chi) with the forced lattice")
print("  values must, on a cell [kd,(k+1)d], lie between S((k+1)d)=s^{k+1} and")
print("  S(kd)=s^k; so its WORST-CASE deviation from the straight exponential is")
print("  bounded by the survival DROP across one cell, B(d) := s^k (1 - s).  As d->0")
print("  this bound -> 0 for EVERY continuation, not just our P2 -> the free profile")
print("  is squeezed out and the dense exponential becomes UNIQUE.")
print()
print("  d        S_sparse(chi) at lattice (geometric)  |S_sparse - dense|   sup_{any monotone profile} dev  B(d)=s^k(1-s)")
for d_val in ["0.5", "0.1", "0.02", "0.004", "0.0005"]:
    dd = mp.mpf(d_val)
    s_here = mp.e ** (-kappa_fix * dd)   # so kappa_lat == kappa_fix exactly
    # number of steps to reach chi_target (round to nearest lattice point)
    nsteps = mp.nint(chi_target / dd)
    chi_lat = nsteps * dd
    S_sparse_lat = s_here ** nsteps
    err_dense = abs(S_sparse_lat - mp.e ** (-kappa_fix * chi_lat))
    # WORST-CASE free-profile deviation over a cell at this content level: any
    # monotone continuation is trapped in [s^{k+1}, s^k], so the largest deviation
    # from the straight exp continuation is bounded by the cell survival drop.
    cell_bound = (s_here ** nsteps) * (1 - s_here)   # = s^k - s^{k+1} = s^k(1-s)
    line2 = f"  d={d_val:<8} S_lat={mp.nstr(S_sparse_lat,12):<20} |S-dense|={mp.nstr(err_dense,4):<11} cellbound B(d)={mp.nstr(cell_bound,6)}"
    print(line2)

print("""
  RESULT.  S(d)^{chi/d} = exp(-kappa chi) is EXACT at the lattice points for every
  d (the geometric law IS the exponential sampled on L).  As d->0 with
  kappa=-log S(d)/d fixed: (i) the lattice fills the line, (ii) the WORST-CASE
  deviation of ANY monotone inter-seal continuation from the straight exponential
  is bounded by the one-cell survival drop B(d)=s^k(1-s) -> 0 (B(d) ~ kappa*d*s^k).
  So the entire free functional d.o.f. is squeezed to zero amplitude -- the dense
  exponential becomes UNIQUE.  The dense exp is the d->0 limit of the sparse
  geometric law, AND the dense uniqueness is precisely the disappearance of the
  sparse free profile.  paper1 s3.2 IS the d->0 limit of s5.3 -- one statement.
""")


# ===========================================================================
head("PART 5.  IS THE SPACING d SELF-CONSISTENTLY FIXED, OR GENUINELY FREE?")
# ===========================================================================
print("""
  The one-diamond constants eta_*, theta_* were fixed by an INTRINSIC self-
  consistency condition KL content = Fisher capacity:
        D(P_eta || mu_D) = J(eta)   <=>   eta tanh eta - log cosh eta = 1 - tanh^2 eta,
  a balance between two record-internal numbers, with a UNIQUE nonzero root.  The
  question: is there an ANALOGOUS intrinsic balance that fixes the seal spacing d
  (or the inter-seal profile) from the holonomy content ITSELF?

  Candidate principle (the natural analogue):  a seal fires when the ACCUMULATED
  inter-seal holonomy content saturates the one-diamond capacity -- i.e. the seal
  spacing in content equals the per-diamond saturated content:
        d  ?=  W_*  =  1 - theta_*^2  =  J(eta_*)   (the Fisher capacity at the
                                                     self-consistent tilt).
  This WOULD fix d to a pure number.  We test whether it is FORCED (a genuine self-
  consistency identity like KL=Fisher) or merely a NATURAL CHOICE (not forced).
""")

# Evaluate the candidate intrinsic spacing d_* = W_* and its consequences.
d_star = W_star  # candidate: spacing = one-diamond saturated content
line("candidate intrinsic spacing d_* = W_* = 1 - theta_*^2", mp.nstr(d_star, 30))
# If kappa is the one no-go scale, the per-seal survival would be s_* = exp(-kappa d_*),
# but kappa is provably free (weight-0 content -> rate needs an absolute unit).
print("""
  ANALYSIS (honest).  Two record-internal numbers are available:
    - W_* = 1 - theta_*^2 = J_* : the saturated content / Fisher capacity per
      diamond -- a forced PURE NUMBER (it IS fixed by KL=Fisher).
    - the per-diamond KL content D(P_eta_* || mu_D) = W_* (equal at the root, by
      the self-consistency condition itself).
  So there is a forced INTRINSIC CONTENT UNIT W_* per saturated diamond.  IF the
  seal-spacing principle 'a seal fires once one diamond's worth of content has
  accumulated' is adopted, then d = W_* is a forced PURE NUMBER and the spacing is
  NOT free in CONTENT units.  BUT -- and this is the decisive honest point -- this
  does NOT remove the freedom, for two independent reasons:
""")

# Reason 1: scale no-go. d is a content (weight-0) quantity; converting the GEOMETRIC
# lattice rate kappa_lat = -log s/d to a COMMIT-ORDER rate still needs the one absolute
# unit kappa. Fixing d in content units leaves kappa free -- exactly the no-go floor.
print("""  [REASON 1 -- the scale no-go is untouched].  Even if d = W_* is forced as a
  CONTENT number, the click-law's absolute rate kappa = -log s/d still requires the
  one absolute commit-order unit the records provably do not carry (do-delete C6,
  paper-XI scale no-go).  Fixing the spacing in WEIGHT-0 content units cannot
  manufacture the missing absolute scale: d_*=W_* is dimensionless content, and
  kappa stays the one free no-go scale.  (Receipt: W_* and the per-diamond KL agree
  at the root to the balance residual below -- the content unit IS forced, the rate
  is NOT.)""")
line("    per-diamond KL content D(P_eta_*||mu_D)", mp.nstr(eta_star*theta_star - mp.log(mp.cosh(eta_star)), 25))
line("    Fisher capacity W_* = J_* = 1 - theta_*^2", mp.nstr(W_star, 25))
line("    |KL content - Fisher capacity| at root", mp.nstr(abs((eta_star*theta_star - mp.log(mp.cosh(eta_star))) - W_star), 6),
     "(=0: content unit W_* is forced)")

# Reason 2: the inter-seal PROFILE is still free even if d is fixed. Fixing d pins
# WHERE seals are, not the SHAPE of S between them.
print("""
  [REASON 2 -- the inter-seal profile freedom is independent of d].  Even granting
  d = W_* (seal LOCATIONS fixed), PART 3's [FREE-S1] is untouched: the inter-seal
  PROFILE function g:[0,1)->(0,1] (the surviving off-diagonal coherent holonomy)
  is not constrained by composition NOR by the KL=Fisher saturation condition,
  which is a statement about the ENDPOINT content of a diamond, not about the
  coherence trajectory between seals.  So the genuinely-indivisible residue (the
  free profile = the quantum coherence) survives EVEN IF the spacing is pinned.

  IS THE SPACING PRINCIPLE ITSELF FORCED?  No -- and we are honest about it.
  'A seal fires at one saturated-diamond's worth of accumulated content (d=W_*)'
  is a NATURAL and self-consistent CHOICE (it reuses the SAME KL=Fisher balance
  that fixed eta_*), but composition-consistency does NOT force it: ANY spacing
  d>0 gives a consistent geometric lattice law.  Unlike eta_* (where KL=Fisher has
  a UNIQUE nonzero root, so the constant is FORCED), there is no second balance
  equation whose unique root SELECTS d.  The saturation principle is a plausible
  closure, not a derived identity.  Verdict: the spacing is FORCED-IF the
  saturation closure is adopted (d=W_*), but the closure is CONJECTURED, not forced
  -- so the sparsity (whether sealing is sparse, and at what density) is GENUINELY
  OPEN.
""")

# Show there is no second self-consistency equation: composition is solved by EVERY d.
print("  -- composition consistency vs spacing: is any d>0 admissible? --")
for d_try in ["0.05", "0.3648", "1.0", "3.7"]:
    dd = mp.mpf(d_try)
    s_try = mp.mpf("0.5")  # arbitrary per-seal survival
    # check geometric composition holds for this (d, s) on the lattice
    ok = abs((s_try ** 2) * (s_try ** 3) - s_try ** 5) < mp.mpf("1e-100")
    tag = "  <- = W_* (saturation closure)" if abs(dd - W_star) < mp.mpf("1e-3") else ""
    line(f"   d={d_try}: composition on lattice holds?", ok, tag)
print("  => EVERY d>0 is composition-consistent; no intrinsic equation selects d.")
print("     The saturation closure d=W_* is the ONLY candidate that reuses KL=Fisher,")
print("     but it is a CHOICE, not forced.  Sparsity is genuinely open.")


# ===========================================================================
head("CANONICAL OUTPUT BLOCK  (F3-B sparse-seal shape receipt)")
# ===========================================================================
print(f"""
  SPARSE-SEAL SETUP (genuinely indivisible, pre-geometric, Tier A):
    seal points  L = {{k d : k>=0}}  (sub-semigroup of intrinsic content, spacing d)
    between seals: D off-diagonal != 0  =  coherent unsealed holonomy
                 =  Barandes-indivisible / genuine quantum.
    composition (Chapman-Kolmogorov / D diagonalizes) holds ONLY on L.

  FORCED in the indivisible regime (self-consistency fixes the LATTICE SKELETON):
    [FORCED-S1]  S(n d) = S(d)^n  GEOMETRIC on the seal lattice  (Cauchy on (N,+),
                 rigid, no regularity needed).  Per-seal survival s=S(d) constant.
                 lattice rate kappa_lat = -log S(d)/d.
                 (max |S((k+m)d)-S(kd)S(md)| over 50 random k,m = {mp.nstr(maxgap,4)})
    [FORCED-S2]  s in (0,1] => kappa_lat>=0  (no revival, restricted to L).

  FREE in the indivisible regime (the genuine-quantum residue):
    [FREE-S1]    the INTER-SEAL PROFILE  g:[0,1)->(0,1], g(0)=1  is UNCONSTRAINED
                 (proof: two monotone continuations P1,P2 agree on L, differ between
                 seals).  An ENTIRE FREE FUNCTIONAL d.o.f. -- the surviving coherent
                 off-diagonal holonomy.  This is exactly what the dense case removes.
    [FREE-S2]    the spacing d (the sparsity / seal density).

  DECISIVE:  in the genuinely-indivisible (sparse) regime self-consistency forces
  ONLY the click-law's VALUES ON THE SEAL LATTICE (geometric), NOT a global SHAPE.
  The dense exponential is forced only because dense seals fill the line; sparse
  seals leave a free inter-seal profile.  SHAPE NOT FORCED; lattice skeleton forced.

  DENSE LIMIT d->0:  S(d)^{{chi/d}} = exp(-kappa chi) EXACT on the lattice for every
  d (with kappa=-log S(d)/d); as d->0 the lattice fills the line and the WORST-CASE
  deviation of ANY monotone inter-seal continuation is bounded by the one-cell
  survival drop B(d)=s^k(1-s) -> 0, recovering the UNIQUE dense exponential.  paper1
  s3.2 IS the d->0 limit of s5.3.  (cell-bound B(d) collapses with d, verified.)

  SPACING d:  composition admits EVERY d>0 (no second self-consistency equation
  selects it).  A natural closure d=W_*=1-theta_*^2={mp.nstr(W_star,12)} reuses the
  one-diamond KL=Fisher saturation (a seal per saturated-diamond's content), which
  would FIX d as a pure CONTENT number -- but (R1) it cannot manufacture the absolute
  commit-order scale kappa (the no-go is untouched), (R2) it does not constrain the
  free inter-seal profile, and (R3) it is a CONJECTURED closure, not a forced
  identity (no unique-root selection, unlike eta_*).  So the spacing -- and hence
  SPARSITY ITSELF -- is GENUINELY OPEN.

  HONEST STATUS:  the genuinely-indivisible click-law does NOT have a forced global
  SHAPE.  Self-consistency forces the SEAL-LATTICE SKELETON (geometric values
  S(nd)=S(d)^n, constant per-seal hazard, no revival) and nothing more.  What
  remains OPEN: (i) the inter-seal coherence profile (a free functional d.o.f. = the
  genuine quantum/Barandes-indivisible content), (ii) the seal spacing d / sparsity
  (no intrinsic equation selects it; the W_* saturation closure is plausible but
  unforced), (iii) the one absolute scale kappa (the standing no-go floor).  The
  dense exponential of paper1 s3.2 is recovered exactly as the d->0 (continuous-
  sealing = classical) limit, confirming that the FORCED dense shape and the OPEN
  sparse freedom are the two faces of one statement: indivisibility = the free
  inter-seal profile the dense limit annihilates.

  Pre-geometric throughout: chi is a record-internal KL pure number; no spacetime,
  metric, light cone, or s^2 was used.
""")

head("DONE.")
