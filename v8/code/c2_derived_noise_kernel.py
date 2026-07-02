r"""
MOVE C2  --  DOES SHARD DERIVE THE LITERATURE'S COLORED LORENTZ-INVARIANT NOISE
KERNEL?   (v7 Long March, Paper 1, hostile-review attack on a potential WIN.)

THE CLAIM UNDER TEST
--------------------
Covariant collapse models need a COLORED, Lorentz-invariant noise correlation
G((Delta x)^2) plus a NORMAL-ORDERING prescription to get a finite energy-
production rate.  The 2025 literature HAND-PICKS the kernel:

  Gundhi, Diosi, Carlesso, "Towards relativistic generalization of collapse
  models", arXiv:2507.06954 (2025):
     Eq.(30)  spectral ansatz   \hat G(q) = exp( - q^4 / beta^4 )         [4D FT]
     Eq.(31)  1+1 closed form   G(x) = (beta^2/2) MeijerG^{2,0}_{0,3}(...)
     normal ordering  O(z) -> :O(z):   to kill the 1/2 vacuum divergence.
     The authors STATE: "this \hat G is just one of the many possible choices"
     and the q^4 (not q^2) is a PRAGMATIC fix (exp(-q^2) diverges in the
     spacelike region where q^2 < 0).  => HAND-PICKED ANSATZ, not derived.

The MOVE-C2 question SHARD wants to win:
  Does SHARD's PRINCIPLED record discreteness / the FORCED odometer +
  inter-seal coherence profile DERIVE this kernel, turning the literature's
  ad-hoc choice into a forced object?

WHAT THIS RECEIPT DOES
----------------------
PART 1.  Pin the literature's REQUIRED kernel properties (LI, positive-type /
         Bochner, finite-energy via the q^2*Ghat heating integral) and exhibit
         that exp(-q^4) satisfies them while exp(-q^2) and white do not.  This
         reproduces the literature's *constraint set* independently.
PART 2.  Locate the SHARD candidate objects and CLASSIFY each against the
         kernel role:  (a) the f1_kernel_positive_type template; (b) the FORCED
         odometer chi; (c) the FREE inter-seal coherence profile (f3b);
         (d) the seal spacing d / principled discreteness.
PART 3.  THE DECISIVE TEST.  For SHARD to DERIVE the kernel it must produce a
         UNIQUE LI positive-type finite-energy G.  Test the three SHARD routes:
         (R1) is the inter-seal profile that object? (R2) does principled
         discreteness fix the characteristic length / spectral shape? (R3) is
         the f1 template a derivation or a re-use of the SAME ansatz?
PART 4.  Build the honest comparison TABLE: literature kernel vs SHARD object,
         property by property.  Verdict: derive / inherit / blocked.

HIGH PRECISION: mpmath mp.dps = 100.  Pre-geometric caveat tracked throughout:
the kernel lives at Tier B (it needs s^2); SHARD's FORCED content is Tier A.
"""

import mpmath as mp

mp.mp.dps = 100


def head(s):
    print("\n" + "=" * 78)
    print(s)
    print("=" * 78)


def line(label, val, extra=""):
    print(f"  {label:<54} {val} {extra}")


# ===========================================================================
head("PART 1.  THE LITERATURE'S REQUIRED KERNEL PROPERTIES (2507.06954)")
# ===========================================================================
print("""
  Covariant-collapse kernel G((x-y)^2) must satisfy, per the 2025 work:
    [P-LI]   Lorentz invariance: G = G((x-y)_mu (x-y)^mu)  (interval only).
    [P-PT]   positive-type (Bochner): \\hat G(q) >= 0 everywhere, so the noise
             two-point function is a genuine covariance (PSD Gram).
    [P-FE]   finite energy: the heating integral \\int d q (q-weight) \\hat G(q)
             converges (white noise \\hat G=1 DIVERGES -> infinite heating).
    [P-NO]   a NORMAL-ORDERING prescription :O: removes the residual 1/2
             vacuum term (a SEPARATE device, on top of the kernel).
  The literature CHOICE  \\hat G(q) = exp(-q^4/beta^4)  (Eq.30), with q^4 (not
  q^2) precisely because q^2 < 0 in spacelike regions makes exp(-q^2) blow up.
  This is the SAME template SHARD's f1_kernel_positive_type.py already uses.
""")

def ghat_white(q):   return mp.mpf(1)
def ghat_gauss(q):   return mp.e ** (-(q) ** 2)
def ghat_quartic(q): return mp.e ** (-(q) ** 4)   # the literature Eq.(30) shape

# [P-PT] positive-type: spectrum nonnegative (Bochner). Check at sample q.
print("  [P-PT] Bochner nonnegativity \\hat G(q) >= 0:")
for nm, gh in [("white  ", ghat_white), ("gauss  ", ghat_gauss),
               ("quartic", ghat_quartic)]:
    vals = [gh(mp.mpf(q)) for q in ["0", "1", "2", "3"]]
    line(f"    {nm} ghat(0,1,2,3)",
         ", ".join(mp.nstr(v, 8) for v in vals),
         f"nonneg={all(v >= 0 for v in vals)}")

# [P-FE] finite-energy heating proxy: \int_0^inf q^2 \hat G(q) dq.
print("\n  [P-FE] heating integral I = \\int_0^inf q^2 \\hat G(q) dq (UV energy weight):")
I_gauss   = mp.quad(lambda q: q ** 2 * ghat_gauss(q),   [0, mp.mpf("60")])
I_quartic = mp.quad(lambda q: q ** 2 * ghat_quartic(q), [0, mp.mpf("60")])
line("    white  I", "DIVERGES", "(not L1 -> infinite heating: the C3 catastrophe)")
line("    gauss  I", mp.nstr(I_gauss, 20), "finite (but exp(-q^2) ill-defined off-shell)")
line("    quartic I", mp.nstr(I_quartic, 20), "finite AND off-shell-safe -> literature CHOICE")

# quartic strictly lighter UV than gaussian (controls short-interval heating)
print("\n  quartic/gauss UV tail ratio -> 0 (quartic strictly lighter):")
for q in ["2", "3", "4"]:
    qq = mp.mpf(q)
    line(f"    q={q}", mp.nstr(ghat_quartic(qq) / ghat_gauss(qq), 10), "(->0)")

# Off-shell safety: the DECISIVE reason q^4 is hand-picked over q^2. On a
# spacelike interval the LI argument s^2 = q.q can be NEGATIVE; exp(-q^2)-type
# kernels with quadratic exponent in the interval blow up, quartic stays bounded.
print("\n  [why q^4 not q^2] off-shell (spacelike s^2<0) boundedness of exp(-s^2 form):")
for s2 in ["-4", "-1", "0", "1", "4"]:
    s2m = mp.mpf(s2)
    quad_exp  = mp.e ** (-(s2m) ** 2)       # quartic-in-s: exp(-(s^2)^2) bounded
    line(f"    s^2={s2:>3}: exp(-(s^2)^2)", mp.nstr(quad_exp, 8),
         "bounded for all sign(s^2)  <- quartic safe")
print("    (a quadratic exp(-s^2) would -> +inf as s^2 -> -inf: the literature's")
print("     stated reason for picking q^4.  It is a PRAGMATIC ad-hoc fix.)")


# ===========================================================================
head("PART 2.  THE SHARD CANDIDATE OBJECTS, CLASSIFIED AGAINST THE KERNEL ROLE")
# ===========================================================================
print("""
  Four SHARD objects could a priori play the role of G((Delta x)^2).  Classify
  each by (tier, forced/free, geometry-dependence):

  (a) f1_kernel_positive_type template  \\hat g(q)=exp(-q^4/beta^4).
        TIER B (needs s^2).  paper1 itself labels it "the Tier-B FORM of the
        seal memory", positive-type + quartic UV, white forbidden.  It is the
        SAME exp(-q^4) ansatz as literature Eq.(30) -- a TEMPLATE, NOT a
        derivation (paper1 s5 item: kernel is an emergent Tier-B notion,
        "where (a locality kernel) is only an emergent Tier-B notion, not a
        Tier-A output").
  (b) the FORCED odometer chi = D(P_AB||P_BA).
        TIER A, FORCED (dchi>=0 unconditional; additive by arrow-positivity).
        But chi is a WEIGHT-0 SCALAR content (a KL number), NOT a two-point
        spatial correlation.  It has no (Delta x)^2 argument at all -> cannot
        BE G(.) as a function of an interval.  Wrong type.
  (c) the FREE inter-seal coherence profile g:[0,1)->(0,1] (f3b).
        TIER A, *FREE* (infinite-dim functional d.o.f.; the genuine-quantum
        / Barandes-indivisible content).  This is the closest in SPIRIT to the
        literature's "free functional choice of kernel" -- but it is free in
        CONTENT (chi), not in an interval s^2, and crucially it is UNCONSTRAINED
        (two continuations P1,P2 differ between seals).  A FREE object cannot
        DERIVE a unique kernel: same status as the literature's "one of many".
  (d) the seal spacing d / principled BHS-sprinkling discreteness.
        Would set a characteristic LENGTH (the literature kernel's peak scale).
        But f3b PART 5: d is GENUINELY FREE; no intrinsic equation selects it
        (the d=W_* saturation closure is plausible but UNFORCED).
""")
line("(a) f1 template  exp(-q^4)", "Tier B", "SAME ansatz as lit Eq.(30); NOT derived")
line("(b) odometer chi (KL number)", "Tier A FORCED", "weight-0 scalar; WRONG TYPE for G(s^2)")
line("(c) inter-seal profile g", "Tier A FREE", "closest in spirit; but UNCONSTRAINED (free fn)")
line("(d) seal spacing d", "FREE", "would set length; no intrinsic eq selects it (f3b P5)")


# ===========================================================================
head("PART 3.  DECISIVE TEST: does SHARD DERIVE a UNIQUE LI positive-type G?")
# ===========================================================================
print("""
  To DERIVE the kernel (beat the literature) SHARD must FORCE a UNIQUE
  LI + positive-type + finite-energy G.  Test the three routes.

  ROUTE R1: 'the inter-seal coherence profile IS G((Delta x)^2)'.
    FAILS on TWO independent counts:
      (i)  TYPE MISMATCH.  The profile is a function of fractional CONTENT
           frac(chi/d) in [0,1) -- a Tier-A, weight-0, pre-geometric scalar.
           G is a function of an INTERVAL s^2 -- a Tier-B geometric object.
           There is no map chi -> s^2 at Tier A (that map is the OPEN
           covariance/emergence frontier; paper1 s4 'Lorentz invariance and
           microcausality are NOT claimed').  So the profile cannot even be
           EVALUATED on the kernel's domain without importing the missing
           geometry.
      (ii) FREEDOM, not derivation.  Even granting a map, the profile is
           UNCONSTRAINED by composition (f3b [FREE-S1]; two distinct
           continuations).  A free functional CANNOT single out exp(-q^4):
           it has exactly the literature's "one of many possible choices"
           status.  Matching freedom to freedom is NOT a derivation.
""")
# Demonstrate the freedom collision quantitatively: build TWO admissible profiles,
# both Tier-A-consistent (agree on the seal lattice), and show they map to
# DIFFERENT putative spectra -- so the profile fixes NO unique kernel.
def profile_straight(u):           # P1: log-linear in content (the 'exp' profile)
    return mp.e ** (-mp.mpf("1.4") * u)
def profile_wiggly(u):             # P2: same endpoints, different interior
    return mp.e ** (-mp.mpf("1.4") * u) * mp.e ** (mp.mpf("0.05") * u * (1 - u))
# endpoints (the FORCED lattice values) agree; interiors differ -> not unique
line("profile P1 vs P2 at u=0 (seal)", mp.nstr(abs(profile_straight(0) - profile_wiggly(0)), 6), "(=0 forced)")
line("profile P1 vs P2 at u=1 (seal)", mp.nstr(abs(profile_straight(1) - profile_wiggly(1)), 6), "(=0 forced)")
for u in ["0.25", "0.5", "0.75"]:
    uu = mp.mpf(u)
    line(f"profile P1 vs P2 at u={u} (BETWEEN)",
         mp.nstr(abs(profile_straight(uu) - profile_wiggly(uu)), 6), "(!=0: NOT unique -> no derived G)")

print("""
  ROUTE R2: 'principled record discreteness (BHS sprinkling / seal spacing d)
             DERIVES the characteristic length and hence the kernel shape'.
    PARTIAL then BLOCKED.
      (i)  A discreteness scale a (record length) IS principled in SHARD and
           DOES set a UV cutoff -> a colored (non-white) noise is NATURAL, not
           ad hoc.  This is a genuine PARTIAL win: SHARD MOTIVATES coloring
           from first principles (records are discrete -> no white-noise
           catastrophe by construction), where the literature must IMPOSE it.
      (ii) BUT the SHAPE of the falloff (q^4 vs q^2 vs Gaussian vs hard cutoff)
           is NOT fixed by 'there is a length a'.  A cutoff length gives a
           SCALE beta ~ 1/a, not a FUNCTIONAL FORM.  And d itself is FREE
           (f3b P5: no intrinsic equation selects the spacing; the W_*
           saturation closure is unforced).  So discreteness derives THAT the
           noise is colored, NOT WHICH colored kernel.  The q^4 ansatz stays
           hand-picked even given SHARD discreteness.
      (iii) the scale no-go bites: a is weight-0 record content -> turning the
           cutoff into an absolute heating rate still needs the one free scale
           kappa (paper57 G no-go / paper1 s3.4).  Same wall as everywhere.
""")
# Quantify (i)+(ii): a discreteness scale fixes the SCALE beta but the FAMILY of
# admissible positive-type finite-energy kernels at that scale is INFINITE.
# Exhibit >=3 distinct positive-type, finite-energy spectra sharing one cutoff
# scale beta=1: quartic, sextic, and a compact-support (Epanechnikov-type) bump.
def ghat_sextic(q):  return mp.e ** (-(q) ** 6)
def ghat_bump(q):    # smooth compact-support positive-type bump (its own square)
    q = mp.mpf(q)
    return (mp.e ** (-1 / (1 - (q / 4) ** 2))) if abs(q) < 4 else mp.mpf(0)
print("  admissible-kernel FAMILY at a single cutoff scale beta~1 (all P-PT & P-FE):")
for nm, gh in [("quartic exp(-q^4)", ghat_quartic), ("sextic exp(-q^6)", ghat_sextic),
               ("compact bump    ", ghat_bump)]:
    I = mp.quad(lambda q: q ** 2 * gh(q), [0, mp.mpf("8")])
    nn = all(gh(mp.mpf(q)) >= 0 for q in ["0", "1", "2", "3"])
    line(f"    {nm}", f"I={mp.nstr(I, 12)}", f"nonneg={nn} -> ADMISSIBLE")
print("    => >= 3 distinct LI positive-type finite-energy kernels at one scale.")
print("       Discreteness fixes the SCALE, NOT the SHAPE.  The shape stays free.")

print("""
  ROUTE R3: 'the f1_kernel_positive_type receipt IS the derivation'.
    NO -- it is a RE-USE of the literature ansatz.  f1's docstring fixes
    \\hat g(q)=exp(-q^4/beta^4) as 'the worked template' and CHECKS its
    properties (Bochner PSD, UV decay, sign-indefinite position kernel).  It
    VERIFIES a hand-picked form satisfies the constraints; it does not DERIVE
    the form from a SHARD principle.  paper1 lists the kernel as a Tier-B
    EMERGENT notion explicitly NOT a Tier-A output.  So f1 and lit Eq.(30) are
    the SAME ansatz, independently property-checked -- a CONVERGENCE, not a
    SHARD derivation.
""")


# ===========================================================================
head("PART 4.  HONEST COMPARISON TABLE  (literature kernel vs SHARD object)")
# ===========================================================================
print("""
  PROPERTY                 LITERATURE (2507.06954)        SHARD
  -----------------------  -----------------------------  ----------------------------
  object                   G((Delta x)^2), \\hat G=e^{-q^4} (a) f1 template = SAME e^{-q^4}
                                                          (c) inter-seal profile (free fn)
  Lorentz invariance       IMPOSED (G of interval only)   NOT claimed (open frontier; Tier B)
  positive-type (Bochner)  required; e^{-q^4}>=0 OK        f1 verifies PSD for SAME e^{-q^4}
  finite energy            via q^4 falloff + normal-order  colored-by-discreteness (motivated)
  normal ordering :O:      EXPLICIT extra device           NOT present (no QFT vacuum at Tier A)
  derived or hand-picked?  HAND-PICKED ('one of many')     ALSO not derived:
                                                            - f1 template = same ansatz
                                                            - profile is FREE (not unique)
                                                            - discreteness fixes SCALE not SHAPE
  what SHARD DOES add      --                              PRINCIPLED reason the noise is
                                                            COLORED (records discrete -> no
                                                            white-noise catastrophe by
                                                            construction), not imposed.
""")

print("""
  VERDICT (Move C2).  SHARD does NOT derive the literature's colored LI noise
  kernel.  The three routes all fail to produce a UNIQUE G:

    - the FORCED Tier-A objects (odometer chi, the geometric seal skeleton) are
      the WRONG TYPE -- weight-0 content scalars, not functions of an interval
      s^2; the chi -> s^2 map is the OPEN covariance frontier.
    - the genuinely-quantum SHARD object (the inter-seal coherence profile) is
      itself FREE / UNCONSTRAINED -- it has EXACTLY the literature's
      'one of many possible choices' status.  Matching a free profile to a free
      kernel is not a derivation.
    - principled discreteness gives a real but PARTIAL win: it MOTIVATES that
      the noise must be COLORED (records are discrete -> a UV cutoff is built in,
      so the white-noise / infinite-heating catastrophe is avoided BY
      CONSTRUCTION rather than by hand).  But it fixes only the SCALE, not the
      FUNCTIONAL SHAPE; >=3 distinct positive-type finite-energy kernels share
      any one cutoff scale.  The q^4 vs q^2 vs bump choice stays hand-picked.
    - the f1 receipt re-uses the literature exp(-q^4) ansatz and property-checks
      it; it is a CONVERGENCE on the same template, not a derivation.

  SO: the potential WIN does NOT land as a DERIVED kernel.  The honest, defensible
  partial: SHARD's principled record discreteness explains WHY the noise is
  colored (the literature's hardest ad-hoc move -- avoiding white noise -- becomes
  structural), but the SPECIFIC kernel exp(-q^4) and the normal-ordering device
  remain hand-picked in BOTH frameworks.  The free inter-seal profile is the
  genuine-quantum residue, NOT a kernel-derivation engine.  Pre-geometric wall:
  the kernel is Tier B (needs s^2); SHARD's forced content is Tier A.
""")

head("DONE.")
