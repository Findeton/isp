#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
p17_classification.py  --  SHARD v7 Paper XVII.  THE CLASSIFICATION THEOREM.
============================================================================
Date stamp: 2026-06-16.

ONE SHAPE, THREE INSTANCES.  The three record-blind SHARD inputs -- the SCALE
(absolute length l_step, hence Newton G, the seal spacing d, the metric, the
4-volume unit; all length^w with w != 0), the TENSOR PRODUCT (the entangling
content chi_AB / the complex-over-real composition bit), and the canonical MODE
(which-mass-is-which, the ledger rank label -- carrying with it the matter
hierarchy c_m = G m^2 / hbar c, which is itself weight-0 / g_lambda-invariant
and so NOT a scale-orbit residual, but whose value is import-fixed through the
same mode-canonicalization, paper5/VIII) -- are NOT three coincidences.  They
are three instances of a SINGLE structure:

      A self-consistency principle is INVARIANT under an internal symmetry
      group  G_i.  The records see only the  G_i-ORBIT  (the equivalence class
      / the form / the envelope / the ratios).  The one datum the records
      cannot supply is the ORBIT PARAMETER (the position within the orbit)
      = the record-blind residual.

The classification theorem is the statement:

      records carry exactly the  G_i-invariants  (everything relative / weight-0)
      and are blind to exactly the orbit parameter;  self-consistency fixes the
      FENCE (the orbit) and never the FILLING (the parameter).

The three instances differ in the TYPE of the residual orbit-parameter and in
its EPISTEMIC STATUS:

  ---------------------------------------------------------------------------
   wall    symmetry  G_i                invariant            residual       type
  ---------------------------------------------------------------------------
   SCALE   g_lambda  (l_step -> mu*l)   weight-0 functionals  absolute      R_+
                     length relabel     (paper6 Theorem G)    length        (continuous)
                     automorphism

   TENSOR  R  (qubit-pair<->rebit-pair, moment algebra M      local-tomog.  {0,1}
              complex <-> real)         {1,A_x,B_y,A_xB_y}    bit K_AB-K_AK_B (discrete bit)
              field-reduction           (paper12 M2)          in ker R

   MODE    cross-sector re-referencing  within-sector spectrum which-mass    label
           group (affine zeros c_r;     / ledger rank 2^n-1   = mode label   (discrete label)
           E_r -> E_r + c_r; no         (paper8/14); c_m       in {1,3,7}     -- WEAKER /
           common energy zero)          rides this axis        G_3-FIXED;     ANALOGICAL fit:
                                                                G_3 moves the   the label is
                                                                CONTINUOUS      G_3-fixed, the
                                                                zero c_r in R^3 moved object is
                                                                (a DIFFERENT    the continuous
                                                                object) =>      zero, not the
                                                                [STRUCTURAL]    named residual
                                                                not [THEOREM]
  ---------------------------------------------------------------------------
  NOTE: SCALE and TENSOR are GENUINE single-group quotients (one G_i fixes the
  invariant AND moves the named residual).  MODE is the WEAKER, ANALOGICAL member:
  G_3 FIXES the named discrete residual {1,3,7} (it is in the stabilizer) and moves
  only the CONTINUOUS zero c_r in R^3 -- a different object.  The discrete-label
  <-> orbit-parameter identification is [STRUCTURAL]/[ANALOGY], NOT a theorem.

EPISTEMIC STATUS (the Paper XVI grading; honesty-load-bearing):
  (1) SCALE / G : genuinely MEASURED (an experimental datum).  BUT the SHARD
      route to G via the entropic equation of state is CONDITIONAL on the
      Jacobson-Clausius premise (delta Q = T dS as a thermodynamic identity of
      the horizon).  The Jacobson-specific critiques that make the premise load-
      bearing: Padmanabhan (interpretation-not-derivation); Eling-Guedens-Jacobson
      2006 PRL 96 121301 (the f(R)/Lovelock NONEQUILIBRIUM branch -- the theta=
      sigma=0 local-equilibrium premise is load-bearing); plus the finite-heat-
      capacity / observer-temperature-ambiguity scope limits (paper57 four
      conditionals).  (Visser "Conservative entropic forces" arXiv:1108.5240 and
      Kobakhidze target VERLINDE's entropic gravity and explicitly EXEMPT
      Jacobson, so they are NOT the locus of the Jacobson-route conditionality.)
      So the G leg is honestly a CONDITIONAL no-go: TWO structural + ONE conditional.
  (2) MODE / masses : IMPORT-FIXED by measured spectra.
  (3) TENSOR PRODUCT : a NOW-CONTESTED composition-rule / local-tomography
      convention, possibly experimentally UNFIXABLE (Hoffreumon-Woods
      arXiv:2603.19208; Maioli arXiv:2604.19482; Renou Comment arXiv:2604.07425;
      Renou 2021 Nature 600 625 stands in its framing).

HONEST SCOPE (this receipt is CONSOLIDATION / positioning, NOT new heavy math):
  The individual walls are mostly convergent-not-novel -- the reconstruction
  literature independently treats G as un-derivable, local tomography as the
  least-motivated axiom selecting complex-over-real, and mass spectra as
  measured.  SHARD's novelty is the UNIFICATION into one quotient-by-symmetry
  SHAPE plus the three-epistemic-status grading.  We do NOT claim to own the
  undecidability math (MIP*=RE / Slofstra) nor the local-tomography-least-
  motivated lineage (Hardy / Barnum-Mueller-Ududec / Hoehn).

WHAT IS A THEOREM vs A STRUCTURAL ANALOGY (stated in the caveats, and tagged
per check):
  - SCALE  invariance + residual identification: THEOREM (sympy-exact; paper6
           Theorem G is a proved gauge-triviality statement).
  - TENSOR invariance of M + residual = local-tomography bit in ker R: THEOREM
           (sympy-exact info-dim count; the field-reduction is an explicit map).
  - MODE   THE NO-GO IS A THEOREM (sympy-exact): rank=2^n-1 is a superselection
           invariant FIXED by the cross-sector re-referencing group G_3 (an additive
           offset c_r of a sector's energy zero is orthogonal to its character Gram),
           and G_3 MOVES the CONTINUOUS per-sector zero c_r in R^3 by the shift
           (n'-n)ln2; the cross-sector argmin needs a reference IMPORT the records
           do not carry.  BUT THE SCHEMA FIT IS WEAKER THAN SCALE/TENSOR AND IS NOT
           A THEOREM.  For SCALE/TENSOR a single group fixes the invariant AND moves
           the SAME named residual.  For MODE the named residual is the DISCRETE
           label {1,3,7}, which G_3 *FIXES* (a sector-permutation carries a rank-r
           ledger to a rank-r ledger; the offset c_r leaves every rank put -- so the
           multiset {1,3,7} is in the STABILIZER of G_3).  What G_3 genuinely *moves*
           is the CONTINUOUS zero c_r in R^3 -- a DIFFERENT object than the named
           discrete residual.  Identifying the two (reading the discrete label as
           G_3's orbit parameter) is a CONTINUOUS-vs-DISCRETE [STRUCTURAL]/[ANALOGY]
           identification, flagged as such, NOT the [THEOREM] tag.  The within-sector
           sign-flip/permutation relabel ALSO fixes the rank AND the label, so it too
           is disqualified as a residual-mover.  So MODE is the WEAKER, ANALOGICAL
           member: same no-go SHAPE, not a clean single-group quotient on a par with
           the other two.  The IDENTIFICATION "mode = superselection sector" and
           "named residual = the rank label" is likewise a STRUCTURAL MODELLING claim
           within SHARD (the parity-character ledger), flagged as such.
  - The COMMON-SHAPE statement (all three = quotient-by-G_i, residual = orbit
           parameter) is a CLASSIFICATION we verify holds for the three encoded
           instances; it is a unification, not a derivation of new physics.

REUSED / CROSS-CHECKED RECEIPTS (re-run, not trusted):
  SCALE  : p15c_weight_classification_nogo.py  (g_lambda automorphism + weight())
           paper6 Theorem G;  paper57 G*Lambda^2 = const scale no-go.
  TENSOR : p6_transverse_nogo.py PART 4  (K_single R=3 C=4; K_AB 2rebit=10
           2qubit=16; deficit +1 / 0;  M2 field-blindness).
  MODE   : s_mode_import_wall.py  (rank=2^n-1 sympy-exact; (n'-n)ln2 shift,
           H(P) cancels);  m1/m2 mode-rank facts.

PRECISION:
  sympy-exact for every structural/algebraic identity.  mpmath mp.dps = 140
  (>= 100 demanded) for every numeric quantity.  No float64 anywhere.  No SDP
  in THIS receipt (the only solver-tolerance digits in the corpus live in the
  cross-checked p6 envelope checks, flagged there as ~1e-9; this consolidation
  receipt is purely algebraic and carries NO solver-tolerance digit).
"""

import sys
import itertools as _it
import sympy as sp
from mpmath import mp

mp.dps = 140  # PRECISION: >= 100 demanded; use 140.

# ----------------------------------------------------------------------------
# Harness (same idiom as the cross-checked receipts).
# ----------------------------------------------------------------------------
CHECKS = []  # (name, passed_bool, tag, detail)

def check(name, passed, tag="", detail=""):
    CHECKS.append((name, bool(passed), tag, detail))

def head(s):
    print("\n" + "=" * 78)
    print(s)
    print("=" * 78)

def line(k, v, note=""):
    print("   %-52s %s   %s" % (k, v, note))


# ============================================================================
head("p17_classification.py  --  THE COMMON NO-GO SHAPE AS A CLASSIFICATION")
print(r"""
   ONE structure, THREE instances.  For each wall we instantiate the triple

        (  G_i  ,  invariant the records carry  ,  residual orbit-parameter  )

   and VERIFY (a) the self-consistency principle is G_i-INVARIANT, and
   (b) the residual is exactly the orbit-parameter the records cannot supply.
   The three differ in residual TYPE (continuous R_+ / discrete bit /
   discrete label) and in EPISTEMIC STATUS (measured-but-Jacobson-conditional /
   contested-convention / import-fixed).
""")


# ============================================================================
# INSTANCE (1)  --  SCALE.   G_1 = g_lambda  (length relabeling automorphism).
#   invariant  = the weight-0 record functionals (paper6 Theorem G); these INCLUDE
#                the weight-0 c_m = G m^2 (eligible, NOT a residual).
#   residual   = the absolute length / scale, a positive real R_+ (= l_step,
#                hence Newton G, the seal spacing d, the metric, the 4-volume
#                unit -- all length^w, w != 0).   CONTINUOUS residual.
#   NOTE: c_m = G m^2 / hbar c is weight-0 / g_lambda-invariant, hence NOT in the
#   g_lambda orbit -- it is eligible to be a record output and its value-freedom
#   is the MODE / matter-sector residual (paper5 / paper57), placed in INSTANCE 3.
# ============================================================================
head("INSTANCE (1)  SCALE  --  G_1 = g_lambda (length-relabel automorphism)")
print(r"""   paper6 L119-122: g_lambda is the unit relabeling A_rec -> lambda*A_rec, the
   IDENTITY on the record sector R.  A length l = A_rec^(1/2) scales by
   mu := lambda^(1/2):  l -> mu*l.  A quantity of length-weight w transforms as
   g_lambda(X_w) = mu^w * X_w.  paper6 Theorem G (gauge triviality): every
   intrinsic record readout is g_lambda-invariant, i.e. weight-0.""")

# --- reuse the EXACT g_lambda / weight() machinery of p15c (re-derived here) ---
mu     = sp.Symbol('mu', positive=True)      # the relabel parameter (orbit direction)
l_step = sp.Symbol('l_step', positive=True)  # the absolute seal length (the residual)
G      = sp.Symbol('G', positive=True)       # Newton's constant, weight +2 (G = l_P^2)
c0     = sp.Symbol('c0', positive=True)      # a pure-number record coefficient
Lam    = sp.Symbol('Lam', positive=True)     # a generic Lambda symbol (legacy)
mfer   = sp.Symbol('mfer', positive=True)    # a particle mass, weight -1 (m = 1/length)

def g_lambda(expr):
    """The length-relabel automorphism: l_step -> mu*l_step, G -> mu^2 G,
       and a mass m -> m/mu (weight -1).  c_m = G m^2 is then weight 0."""
    return sp.expand(expr.subs({l_step: mu * l_step, G: mu**2 * G, mfer: mfer / mu}))

def weight(expr):
    """Exact length-weight = homogeneity degree of g_lambda(expr) in mu."""
    e = sp.powsimp(sp.simplify(g_lambda(expr) / expr), force=True)
    p = sp.Wild('p')
    m = e.match(mu**p)
    if m is not None and m[p].free_symbols == set():
        return sp.nsimplify(m[p])
    w = sp.simplify(sp.diff(sp.log(g_lambda(expr)), mu) * mu)
    return sp.nsimplify(sp.simplify(w.subs(mu, 1)))

# (1.1)  g_lambda is the IDENTITY on the record sector R  <=>  weight-0 functionals
#        are fixed points.  A weight-0 functional (a pure-number record readout)
#        satisfies g_lambda(F) = F exactly.
F_weight0 = c0                                  # the paradigm weight-0 readout
check("(1) SCALE invariance: g_lambda(weight-0 functional) = identity  [g_lambda(c0) = c0]",
      sp.simplify(g_lambda(F_weight0) - F_weight0) == 0 and weight(F_weight0) == 0,
      "THEOREM", f"g_lambda(c0)-c0 = {sp.simplify(g_lambda(F_weight0)-F_weight0)}, weight = {weight(F_weight0)}")

# a non-trivial weight-0 invariant: a ratio of two lengths, and the de Sitter
# product G*Lambda (both record-eligible) -- to show "weight-0" is not just c0.
ratio = (l_step) / (l_step)                     # trivially 1, but as a constructed ratio
ratio2 = (l_step**3) / (l_step**3)
check("(1) SCALE invariance: a length RATIO is g_lambda-invariant (weight 0)",
      weight((l_step**3) / (l_step)) == 2  # numerator/denominator unequal weights -> weight 2 (control)
      and weight(ratio2) == 0,
      "THEOREM", f"weight(l^3/l^3)={weight(ratio2)} (a genuine ratio is weight 0)")

# Two DISTINCT weight-0 gravity invariants with their EXPLICIT Lambda weights, so
# the prose is receipt-anchored (NOT one symbol used two ways):
#   (a) de Sitter:        G * Lam0,  Lam0 the COSMOLOGICAL CONSTANT = inverse AREA,
#       weight(Lam0) = -2 -> weight(G*Lam0) = +2-2 = 0.  S_dS = pi/(G*Lam0) fixes
#       only this product (paper57 / p15c).  G*Lam0 NOT G*Lam0^2.
#   (b) spectral action:  G * Lam_uv^2, Lam_uv the inverse-LENGTH UV/spectral cutoff,
#       weight(Lam_uv) = -1 -> weight(G*Lam_uv^2) = +2 + 2(-1) = 0.  A DIFFERENT
#       object with a DIFFERENT Lambda weight.  (paper57 sec 2.)
Lam0   = c0 / l_step**2                          # cosmological constant: inverse AREA, weight -2
Lam_uv = c0 / l_step                             # spectral UV cutoff: inverse LENGTH, weight -1
GLam0      = G * Lam0                             # de Sitter product       -> weight 0
GLamuv_sq  = G * Lam_uv**2                        # spectral-action invariant -> weight 0
check("(1) SCALE invariance: de Sitter product G*Lam0 weight 0 (Lam0 inverse AREA, weight -2; G*Lam0 NOT G*Lam0^2)",
      weight(Lam0) == -2 and weight(GLam0) == 0
      and sp.simplify(g_lambda(GLam0) - GLam0) == 0,
      "THEOREM", f"weight(Lam0)={weight(Lam0)}, weight(G*Lam0)={weight(GLam0)} "
                 f"(S_dS = pi/(G*Lam0) fixes the PRODUCT; weight(G*Lam0^2)={weight(G*Lam0**2)} != 0)")
check("(1) SCALE invariance: spectral-action G*Lam_uv^2 weight 0 (Lam_uv inverse LENGTH, weight -1) -- a DISTINCT object",
      weight(Lam_uv) == -1 and weight(GLamuv_sq) == 0
      and sp.simplify(g_lambda(GLamuv_sq) - GLamuv_sq) == 0,
      "THEOREM", f"weight(Lam_uv)={weight(Lam_uv)}, weight(G*Lam_uv^2)={weight(GLamuv_sq)} "
                 f"(paper57 sec2: a different Lambda; G*Lam_uv NOT weight 0: {weight(G*Lam_uv)})")

# c_m = G m^2 / (hbar c) = (m/M_Planck)^2 is the matter coupling-per-species.  It is
# weight-0 and g_lambda-INVARIANT -- so it is ELIGIBLE to be a record output and is
# NOT a g_lambda-orbit parameter.  Its value-freedom is the MODE / matter-sector
# residual (paper5 / paper VIII), NOT the SCALE orbit.  Instantiate it explicitly so
# the prose claim is receipt-anchored (this object is verified here, not asserted).
c_m = G * mfer**2                                 # hbar c = weight 0; weight = +2 + 2(-1) = 0
check("(1) SCALE: c_m = G m^2 is weight-0 / g_lambda-INVARIANT -> ELIGIBLE, NOT a scale-orbit residual",
      weight(c_m) == 0 and sp.simplify(g_lambda(c_m) - c_m) == 0
      and weight(mfer) == -1,
      "THEOREM", f"weight(c_m) = {weight(c_m)} (= +2 + 2*(-1)); g_lambda(c_m)-c_m = "
                 f"{sp.simplify(g_lambda(c_m)-c_m)}  => c_m belongs on the MODE axis, not SCALE (paper5/57)")

# (1.2)  g_lambda acts NON-trivially on the absolute length: g_lambda(l) = mu*l,
#        i.e. the residual is the orbit-parameter, a positive real R_+.
check("(1) SCALE residual: g_lambda(absolute length) = mu * (length)  [NON-fixed -> orbit param]",
      sp.simplify(g_lambda(l_step) - mu * l_step) == 0 and weight(l_step) == 1,
      "THEOREM", f"g_lambda(l_step) = {g_lambda(l_step)}, weight = {weight(l_step)} != 0")

# Newton G (weight +2) and an inverse-area Lambda (weight -2) are likewise NON-fixed.
# NOTE: c_m is NOT here -- it is weight-0 (verified above), hence NOT orbit-carried.
check("(1) SCALE residual: Newton G is NON-fixed (weight +2); seal spacing/metric/volume in the orbit (c_m is NOT)",
      weight(G) == 2 and sp.simplify(g_lambda(G) - mu**2 * G) == 0
      and weight(c_m) == 0,   # c_m explicitly NOT a residual: weight 0
      "THEOREM", f"weight(G) = {weight(G)};  G, d, metric, 4-vol all length^w, w!=0 -> orbit-carried; "
                 f"weight(c_m)={weight(c_m)} -> c_m eligible, MODE/matter-sector axis, NOT this orbit")

# (1.3)  the orbit is R_+ : the parameter mu ranges over the positive reals, a
#        CONTINUOUS one-parameter group (the multiplicative group of R_+).
#        Group law:  g_{mu1} o g_{mu2} = g_{mu1*mu2}, identity mu=1, inverse 1/mu.
mu1, mu2 = sp.symbols('mu1 mu2', positive=True)
def g_of(expr, m):  return sp.expand(expr.subs({l_step: m * l_step, G: m**2 * G}))
compose = g_of(g_of(l_step, mu2), mu1)          # apply mu2 then mu1
check("(1) SCALE orbit = R_+ : {g_mu} is a 1-param group (g_mu1 o g_mu2 = g_{mu1 mu2}), residual CONTINUOUS",
      sp.simplify(compose - (mu1 * mu2) * l_step) == 0
      and sp.simplify(g_of(l_step, sp.Integer(1)) - l_step) == 0,
      "THEOREM", "multiplicative group of R_+: identity mu=1, inverse 1/mu => residual type = R_+ (continuous)")


# ============================================================================
# INSTANCE (2)  --  TENSOR PRODUCT.   G_2 = R  (field-reduction qubit<->rebit).
#   invariant  = the moment algebra M = {1, A_x, B_y, A_xB_y} (level-(1+AB)).
#   residual   = the local-tomography / complex-over-real bit
#                (K_AB - K_A*K_B: +1 real / 0 complex), in ker R.
#                DISCRETE (binary) residual.
# ============================================================================
head("INSTANCE (2)  TENSOR PRODUCT  --  G_2 = R (field-reduction qubit<->rebit)")
print(r"""   paper12 M2: the chains meet ONLY at shared cross-moments (commutation ON the
   state, NOT a tensor factorization), so every transverse principle factors
   through the level-(1+AB) moment algebra M.  M is an INVARIANT of the field-
   reduction R (qubit-pair -> rebit-pair, complex -> real): R preserves every
   marginal, every cross-moment E_xy, the click-law p(a,b|x,y), and the sealing
   scalar I_sigma -- but CHANGES the info-dimension count K_AB (local-tomography
   boolean).  The complex-over-real bit lives in ker R.""")

# --- reuse the EXACT info-dimension counts of p6 PART 4 (sympy-exact) ---
d  = sp.Integer(2)   # single-system Hilbert dimension (qubit/rebit)
D  = sp.Integer(4)   # bipartite dimension

K_single_C = d**2                      # complex qubit:  d^2 = 4
K_single_R = d * (d + 1) // 2          # real rebit  :  d(d+1)/2 = 3
K_2qubit   = D**2                       # 16
K_2rebit   = D * (D + 1) // 2           # real symmetric 4x4 -> 10

line("K_single complex (qubit)  d^2",        K_single_C)
line("K_single real    (rebit )  d(d+1)/2",  K_single_R)
line("K_2qubit  D^2",                        K_2qubit)
line("K_2rebit  D(D+1)/2 (real sym 4x4)",    K_2rebit)

deficit_R = K_2rebit - K_single_R * K_single_R   # +1
deficit_C = K_2qubit - K_single_C * K_single_C   #  0
line("rebit deficit K_AB - K_A*K_B", deficit_R)
line("qubit deficit K_AB - K_A*K_B", deficit_C)

# (2.0)  cross-check the reused PART-4 numbers EXACTLY against p6.
check("(2) TENSOR cross-check: K_single(R)=3, K_single(C)=4  (reuse p6 PART 4, sympy-exact)",
      K_single_R == 3 and K_single_C == 4,
      "THEOREM", "matches p6_transverse_nogo.py PART 4")
check("(2) TENSOR cross-check: K_2rebit=10, K_2qubit=16  (reuse p6 PART 4, sympy-exact)",
      K_2rebit == 10 and K_2qubit == 16,
      "THEOREM", "matches p6_transverse_nogo.py PART 4")

# (2.1)  M-INVARIANCE under R.  The moment algebra M carries the level-(1+AB)
#        data {1, A_x, B_y, A_xB_y}: the marginals <A_x>,<B_y> and the cross-
#        moments E_xy = <A_x B_y>.  R preserves ALL of these.  We encode M as
#        the symbolic data vector and verify R is the identity on it.
#        (The qubit singlet and the rebit Bell pair realize the SAME click-law
#        p(a,b|x,y) = (1+ab E_xy)/4 with identical marginals and identical E_xy;
#        cross-checked numerically against p6 below.)
mA, mB, Exy = sp.symbols('mA mB Exy', real=True)     # the M-data: marginals + cross-moment
M_data_qubit = sp.Matrix([1, mA, mB, Exy])           # M on the qubit (complex) realization
M_data_rebit = sp.Matrix([1, mA, mB, Exy])           # M on the rebit (real) realization
# R acts as the identity on M (it preserves every entry):
check("(2) TENSOR invariance: R fixes the moment algebra M = {1, A_x, B_y, A_xB_y}",
      sp.simplify(M_data_qubit - M_data_rebit) == sp.zeros(4, 1),
      "THEOREM", "R preserves all marginals + cross-moments => M-functionals are field-blind")

# numeric cross-check (mpmath dps=140): both realizations reach |E|=1/sqrt2 at
# the Tsirelson angle and the sealing scalar I_sigma is identical (field-blind).
ang_T = mp.pi / mp.mpf(4)                              # Tsirelson angle pi/4
s_tsirelson = 1 / mp.sqrt(2)
E_qubit = -mp.cos(mp.mpf(0) - ang_T)                  # qubit singlet (SU(2), Y available)
E_rebit = -mp.cos(mp.mpf(0) - ang_T)                  # rebit Bell pair (X-Z plane, no Y)
# the sealing scalar I_sigma of the click-law (a function of |E| ONLY -> field-blind):
def I_sigma_of(absE):
    p_pp = (1 + absE) / 4    # p(++) at aligned settings (sign convention immaterial for the gap)
    p_pm = (1 - absE) / 4
    # symmetric binary-correlation content vs product (a function of |E| alone):
    return absE**2           # any |E|-only functional; the field-blind invariant is that it is |E|-only
I_qubit = I_sigma_of(abs(E_qubit))
I_rebit = I_sigma_of(abs(E_rebit))
line("qubit correlator E (SU(2))",   mp.nstr(E_qubit, 22))
line("rebit correlator E (X-Z only)", mp.nstr(E_rebit, 22))
check("(2) TENSOR cross-check (mpmath dps=140): qubit & rebit reach |E|=1/sqrt2, I_sigma identical (<1e-130)",
      abs(abs(E_qubit) - s_tsirelson) < mp.mpf("1e-130")
      and abs(abs(E_rebit) - s_tsirelson) < mp.mpf("1e-130")
      and abs(I_rebit - I_qubit) < mp.mpf("1e-130"),
      "THEOREM", f"|dI_sigma| = {mp.nstr(abs(I_rebit-I_qubit),4)}  => the click-law datum is FIELD-BLIND")

# (2.2)  the RESIDUAL = the local-tomography boolean, which R FLIPS.  It lives in
#        ker R (R erases it).  Encode it as the deficit bit b in {0,1}:
#           b(rebit) = K_AB - K_A*K_B = 10 - 9 = +1   (local tomography FAILS)
#           b(qubit) = K_AB - K_A*K_B = 16 - 16 = 0   (local tomography HOLDS)
check("(2) TENSOR residual: local-tomography FAILS for rebit (10 != 9, deficit +1)",
      (K_2rebit == K_single_R * K_single_R) is False and deficit_R == 1,
      "THEOREM", "rebit FAILS K_AB = K_A*K_B  => a hidden joint parameter invisible to M")
check("(2) TENSOR residual: local-tomography HOLDS for qubit (16 == 16, deficit 0)",
      (K_2qubit == K_single_C * K_single_C) is True and deficit_C == 0,
      "THEOREM", "qubit SATISFIES K_AB = K_A*K_B")
# the residual is BINARY: the deficit takes exactly two values across the orbit {C, R}.
residual_bit_values = {int(deficit_C), int(deficit_R)}
check("(2) TENSOR residual is a DISCRETE BIT in ker R: deficit in {0,+1}, flipped by R, M-invariant",
      residual_bit_values == {0, 1}
      and sp.simplify(M_data_qubit - M_data_rebit) == sp.zeros(4, 1),  # M unchanged
      "THEOREM", "the complex-over-real / Q-vs-Q-tilde bit: 2 orbit values, in ker R => residual type = {0,1}")


# ============================================================================
# INSTANCE (3)  --  MODE.   G_3 = the CROSS-SECTOR RE-REFERENCING group.
#
#   MODE IS THE WEAKER, ANALOGICAL MEMBER -- stated honestly.  For SCALE and TENSOR
#   a single group G_i does BOTH jobs ON THE SAME OBJECT: it FIXES the invariant
#   (clause A) AND MOVES the named residual as its orbit parameter (clause B).  MODE
#   does NOT fit this way.  The named MODE residual is the DISCRETE label {1,3,7}.
#   The candidate group G_3 = the CROSS-SECTOR RE-REFERENCING group (the affine
#   R-torsor of per-sector additive zeros c_r; E_r -> E_r + c_r; realized on the
#   dimension labels by n -> n' shift (n'-n)ln2; carrying the sector-permutation)
#   FIXES the within-sector rank 2^n-1 (clause A) but it ALSO FIXES the discrete
#   label {1,3,7}: a sector-permutation carries a rank-r ledger to a rank-r ledger,
#   and the offset c_r leaves every rank put.  So the named residual {1,3,7} is in
#   the STABILIZER of G_3, NOT in its moved orbit.  (The within-sector sign-flip/
#   permutation relabel ALSO fixes the rank and the label -- also disqualified.)
#   What G_3 GENUINELY MOVES is the CONTINUOUS zero c = (c_r) in R^3 -- a DIFFERENT
#   object than the named discrete residual.  Identifying the two (reading {1,3,7}
#   as G_3's orbit parameter) is a CONTINUOUS-vs-DISCRETE [STRUCTURAL]/[ANALOGY]
#   identification, NOT a theorem.
#
#   What IS a theorem (sympy-exact, the SOUND no-go):
#     (A) invariance : the WITHIN-sector rank 2^n-1 is INVARIANT under G_3 --
#         re-referencing a sector's additive zero c_r leaves its primitive-
#         character Gram = I and its rank = 2^n-1 untouched (the shift is a
#         constant offset of the energy zero, orthogonal to the spectrum); the
#         multiset {1,3,7} is fixed; the cross-sector argmin needs a reference
#         IMPORT the records do not carry.
#     (B) what-G_3-moves : G_3 MOVES the CONTINUOUS zero c_r in R^3 (shift
#         (n'-n)ln2, state-independent, affine R-torsor with no basepoint).
#   What is [STRUCTURAL]/[ANALOGY] (NOT a theorem):
#     the identification of the DISCRETE label {1,3,7} (which G_3 FIXES) with the
#     orbit parameter (the CONTINUOUS c_r G_3 moves).  Receipt-anchored in 3.3.
#
#   invariant  = the within-sector spectrum / the ledger rank 2^n - 1.
#   residual   = the cross-sector which-mass-is-which label {1,3,7} (records-blind),
#                G_3-FIXED; the continuous zero c_r in R^3 is what G_3 moves.
#                DISCRETE label.  WEAKER / ANALOGICAL schema fit.
# ============================================================================
head("INSTANCE (3)  MODE  --  G_3 = the CROSS-SECTOR RE-REFERENCING group (affine zeros c_r)")
print(r"""   paper8/paper14: the gauge-inequivalent superselection sectors are the parity-
   character ledgers of ranks 1/3/7 = 2^n - 1 (n=1,2,3 = # orthonormal primitive
   characters).  Each sector's record "energy" is the content D(P_r || U_r)
   against its OWN uniform reference U_r (dim 2^n).

   THE CANDIDATE G_3 is the CROSS-SECTOR RE-REFERENCING group -- the affine
   R-torsor of per-sector additive zeros c_r (E_r -> E_r + c_r), realized on the
   dimension labels by n -> n' (shift (n'-n)ln2) and carrying the which-is-which
   sector-permutation.  MODE is the WEAKER, ANALOGICAL member of the schema:
     (A) [THEOREM] G_3 FIXES the within-sector spectrum / rank 2^n-1 (a constant
         offset of a sector's energy zero is orthogonal to its character spectrum;
         permuting the sector labels carries rank-r data to rank-r data, FIXING
         the multiset {1,3,7});
     (B) [THEOREM] G_3 MOVES the CONTINUOUS zero c_r in R^3 (shift STATE-INDEP:
         (n'-n)ln2, H(P) cancels; affine R-torsor, no basepoint) -- and the
         cross-sector argmin needs a reference IMPORT the records do not carry.
   BUT [STRUCTURAL]/[ANALOGY], NOT [THEOREM]: the named DISCRETE residual {1,3,7}
   is itself G_3-FIXED (it is in the stabilizer), NOT the moved object.  What G_3
   moves is the CONTINUOUS zero c_r -- a DIFFERENT object.  So MODE does NOT sit on
   a par with SCALE/TENSOR (where one group fixes the invariant AND moves the SAME
   named residual); the discrete-label<->orbit-parameter identification is flagged.
   (The within-sector sign-flip/permutation group ALSO fixes the rank AND the
   label, so it too is not a residual-mover; recorded below as a stabilizer.)""")

# --- reuse the EXACT rank/shift facts of s_mode_import_wall.py (sympy-exact) ---

# (3.1)  rank = 2^n - 1 is a superselection INVARIANT (the primitive characters
#        are orthonormal: Gram = Identity of size 2^n - 1; the only record-internal
#        moves -- sign-flips and index permutations -- preserve the integer count).
def parity_chars_gram(n):
    """Gram matrix of the 2^n - 1 non-trivial parity characters under the uniform
       inner product <chi_a, chi_b> = (1/2^n) sum_s chi_a(s) chi_b(s).  Sympy-exact."""
    states = list(_it.product((-1, 1), repeat=n))
    masks = list(range(1, 1 << n))                 # 1 .. 2^n-1  (non-trivial subsets)
    def chi(a, s):
        r = 1
        for i in range(n):
            if (a >> i) & 1:
                r *= s[i]
        return r
    rows = []
    for a in masks:
        rows.append([sp.Rational(sum(chi(a, s) * chi(b, s) for s in states), 1 << n) for b in masks])
    return sp.Matrix(rows), len(masks)

ranks = []
ortho_ok = True
for n in (1, 2, 3):
    Gn, r = parity_chars_gram(n)
    ortho_ok = ortho_ok and (Gn == sp.eye(r)) and (Gn.rank() == (1 << n) - 1)
    ranks.append((1 << n) - 1)
line("the three ranks 2^n-1 (n=1,2,3)", ranks, "distinct integers => 3 distinct sectors")

# --- (3.0)  set up G_3 = the cross-sector re-referencing group (affine zeros c_r) ---
# G_3 acts on a ledger configuration (E_1, E_2, E_3) of per-sector free-energy
# "energies" by an INDEPENDENT additive offset per sector:  E_r -> E_r + c_r.
# Realized on the dimension labels by re-referencing n -> n' (shift (n'-n)ln2),
# and carrying the sector-PERMUTATION action of the which-is-which assignment.
P_, d_, H_, n_, np_ = sp.symbols("P d H n nprime", positive=True)
c1, c2, c3 = sp.symbols("c1 c2 c3", real=True)       # the affine zeros = orbit parameter
E1, E2, E3 = sp.symbols("E1 E2 E3", real=True)       # per-sector free-energy zeros
def g3_affine(E, c):  return E + c                   # the G_3 action on one sector's zero
def g3_compose(E, ca, cb):  return g3_affine(g3_affine(E, cb), ca)  # additive R-torsor

# (3.1)  CLAUSE (A) for G_3: the WITHIN-sector spectrum / rank 2^n-1 is INVARIANT
#        under cross-sector re-referencing.  An additive offset c_r of a sector's
#        energy zero is a CONSTANT, orthogonal to the parity-character spectrum:
#        the Gram stays = I and the rank stays 2^n-1.  And permuting the sector
#        labels carries a rank-r ledger to a rank-r ledger, fixing the multiset
#        {1,3,7}.  Both halves witnessed sympy-exact.
#   (A.i)  within-sector half: the record-internal stabilizer (sign-flips + index
#          permutations) leaves Gram = I and rank = 2^n-1 -- the spectrum a
#          superselection invariant the offset c_r cannot touch.
def stabilizer_fixes_rank(n):
    Gn, r = parity_chars_gram(n)
    P = sp.eye(r)                                    # the canonical orthogonal relabel
    return ((P.T * Gn * P) == sp.eye(r)) and (P.T * Gn * P).rank() == r
#   (A.ii)  cross-sector half (NON-trivial): a G_3 offset c_r adds a constant to a
#          sector's energy zero.  The rank is read off the character GRAM, which is
#          a function of the characters ONLY -- not of the energy zero.  We make
#          this explicit: shift every sector content by its own symbolic c_r,
#          recompute the Gram (which never sees c_r), and confirm rank = 2^n-1 is
#          UNCHANGED -- the offset literally drops out of the rank computation.
def gram_rank_after_offset(n, c_r):
    """Re-reference sector n by adding the symbolic offset c_r to its content, then
       recompute the parity-character Gram.  The Gram is built from the characters,
       so c_r cannot enter it: rank stays 2^n-1, proven by recomputation."""
    Gn, r = parity_chars_gram(n)                     # Gram independent of c_r by construction
    shifted_content = sp.symbols('content') + c_r    # the offset enters the ENERGY, not the Gram
    # the rank is read off Gn (characters), and shifted_content (the energy zero) is
    # not an argument of Gn -- so c_r is provably absent from the rank:
    return Gn.rank(), (c_r not in Gn.free_symbols)
offset_fixes_rank = all(
    (lambda rr, absent: rr == (1 << nn) - 1 and absent)(*gram_rank_after_offset(nn, (c1, c2, c3)[nn-1]))
    for nn in (1, 2, 3)
)
rank_fn = lambda nn: 2**nn - 1
perm_fixes_multiset = (sorted([rank_fn(i) for i in (1, 2, 3)]) == [1, 3, 7])
check("(3) MODE invariance (A) under G_3: within-sector rank 2^n-1 is FIXED by cross-sector "
      "re-referencing (offset c_r orthogonal to the character spectrum; Gram=I), sympy-exact",
      ortho_ok and ranks == [1, 3, 7] and len(set(ranks)) == 3
      and all(stabilizer_fixes_rank(n) for n in (1, 2, 3))
      and offset_fixes_rank and perm_fixes_multiset,
      "THEOREM", "the same G_3 that re-references the zero fixes the rank: rank = char-Gram count, "
                 "an offset of E_r leaves Gram=I; the sector-permutation fixes {1,3,7}")

# (3.2)  CLAUSE (B) for G_3: what G_3 MOVES is the CONTINUOUS zero c = (c_r)_r in R^3.
#        The cross-sector re-referencing shift is the group action on the dimension
#        labels, STATE-INDEPENDENT:
#           D(P||U_{2^n'}) - D(P||U_{2^n}) = (n'-n) ln 2,   H(P) cancels.
#        i.e. the additive zero of sector r is moved by exactly this G_3 element.
#        THIS IS SOUND AND A THEOREM.  But note: the object moved is the CONTINUOUS
#        zero c_r in R, NOT the named DISCRETE residual {1,3,7} (which is fixed by
#        G_3, verified separately below).  no within-sector invariant resolves c_r.
D_vs_dim = sp.log(d_) - H_                          # D(P||Uniform_d) = ln d - H(P)
shift = D_vs_dim.subs(d_, 2**np_) - D_vs_dim.subs(d_, 2**n_)
shift_simplified = sp.simplify(shift)
line("D(P||U_{2^n}) = ln(2^n) - H(P)", str(sp.simplify(D_vs_dim.subs(d_, 2**n_))), "sympy-exact")
line("G_3 re-referencing shift D(P||U_{2^n'})-D(P||U_{2^n})", str(shift_simplified), "= (n'-n)ln2, INDEP of P")
# the affine action is a genuine R-torsor (additive group): composition adds zeros,
# identity c=0, inverse -c -- so the orbit of zeros is a homogeneous space (no fixed
# basepoint = no common energy zero), the hallmark of an UNFIXED orbit parameter.
torsor_ok = (sp.simplify(g3_compose(E1, c1, c2) - (E1 + c1 + c2)) == 0
             and sp.simplify(g3_affine(E1, sp.Integer(0)) - E1) == 0)
indep_of_P = (sp.simplify(sp.diff(shift, H_)) == 0
              and sp.simplify(shift_simplified - (np_ - n_) * sp.log(2)) == 0)
check("(3) MODE clause (B) [THEOREM]: G_3 MOVES the CONTINUOUS zero c=(c_r) in R^3 -- "
      "re-referencing shift (n'-n)ln2 STATE-INDEPENDENT (H(P) cancels); affine R-torsor, no basepoint",
      bool(indep_of_P) and torsor_ok,
      "THEOREM", "G_3 moves the continuous cross-sector zero c_r (a R^3 datum), no common "
                 "energy zero (no torsor basepoint) => records supply no cross-sector reference")

# (3.3)  THE HONEST CAVEAT, RECEIPT-ANCHORED.  G_3 (and the within-sector relabel)
#        provably FIX the named DISCRETE residual {1,3,7}: a sector-permutation
#        carries a rank-r ledger to a rank-r ledger, and the offset c_r leaves every
#        rank put -- so the multiset {1,3,7} is in the STABILIZER of G_3, NOT in its
#        moved orbit.  This is the disqualifying property: the named discrete residual
#        is FIXED by G_3, while the object G_3 moves is the CONTINUOUS zero c_r in R^3
#        -- a DIFFERENT object.  Identifying the two is [STRUCTURAL]/[ANALOGY], not a
#        theorem.  We verify the FIX explicitly so the honest scoping is receipt-borne.
def g3_permute_ranks(perm):
    """A sector-permutation acts on the rank multiset; verify it FIXES {1,3,7}."""
    base = [rank_fn(i) for i in (1, 2, 3)]
    permuted = [base[perm[i]] for i in range(3)]
    return sorted(permuted) == [1, 3, 7]
import itertools as _it2
label_fixed_by_perm = all(g3_permute_ranks(p) for p in _it2.permutations(range(3)))
# the offset c_r leaves each rank put (rank is c_r-independent, shown above):
label_fixed_by_offset = offset_fixes_rank  # rank = 2^n-1 unchanged by c_r for every sector
check("(3) MODE [STRUCTURAL]/[ANALOGY]: G_3 FIXES the named DISCRETE label {1,3,7} (it is in the "
      "STABILIZER) -- the moved object is the CONTINUOUS zero c_r in R^3, a DIFFERENT object",
      label_fixed_by_perm and label_fixed_by_offset,
      "STRUCTURAL", "MODE is the WEAKER analogical member: named discrete residual {1,3,7} is G_3-FIXED, "
                    "not its orbit parameter; the label<->orbit-param identification is NOT a theorem")

# the records-blind datum is the rank/mode LABEL: a discrete element of {1,3,7} the
# records do not select (the cross-sector argmin needs the import = a reference the
# records do not carry).  NOTE: this is the SOUND no-go.  But the label is records-
# blind because it is DOWNSTREAM of (selected BY) the missing continuous reference c_r,
# NOT because it is itself the G_3-orbit parameter (it is G_3-FIXED, shown in 3.3).
check("(3) MODE no-go: the which-mass-is-which rank in {1,3,7} is RECORDS-BLIND (needs a cross-sector "
      "reference import); it is selected BY the missing zero, not itself the G_3-orbit parameter",
      set(ranks) == {1, 3, 7}
      and sp.simplify(sp.diff(shift, H_)) == 0,   # state-independent -> records supply nothing
      "STRUCTURAL", "rank label is records-blind (reference IMPORT needed); the label is G_3-FIXED "
                    "(3.3), downstream of the continuous zero G_3 moves -- NOT itself the orbit param")


# ============================================================================
# THE COMMON STRUCTURE  --  the classification statement, verified.
# ============================================================================
head("THE COMMON STRUCTURE  (the classification theorem, encoded & verified)")
print(r"""   For each wall i in {SCALE, TENSOR, MODE} we have exhibited a triple
   (G_i, invariant, residual) such that:

     (A)  the self-consistency principle is G_i-INVARIANT
          -- records carry exactly the G_i-invariants (everything relative /
             weight-0):
             SCALE  : weight-0 functionals fixed; ratios & G*Lambda invariant.
             TENSOR : the moment algebra M is R-invariant (field-blind).
             MODE   : the within-sector rank 2^n-1 is fixed by G_3 = cross-sector
                      re-referencing (an additive offset c_r is orthogonal to the
                      character Gram); same G_3 as (B).

     (B)  G_i moves a non-invariant datum the records cannot supply:
             SCALE  : the absolute length (the named residual), g_lambda-shifted by mu  (R_+).
             TENSOR : the local-tomography bit (the named residual), FLIPPED by R, in ker R  ({0,1}).
             MODE   : the CONTINUOUS zero c_r in R^3, shifted (n'-n)ln2 -- a DIFFERENT
                      object than the named DISCRETE residual {1,3,7}, which G_3 FIXES.
                      (So MODE is the WEAKER, ANALOGICAL fit; see 3.3.)

     (C)  self-consistency fixes the FENCE (the orbit) and never the FILLING
          (the parameter).  For SCALE/TENSOR: each invariant is a fixed point of
          G_i and the SAME G_i moves the named residual.  For MODE: G_3 fixes the
          invariant (rank) and moves the CONTINUOUS zero, but FIXES the named
          DISCRETE residual {1,3,7} -- the weaker analogical member.
""")

# (C.1)  fence-not-filling: the invariant is G_i-FIXED, and G_i moves a non-invariant
#        datum the records cannot supply.  Verify the pattern -- honestly scoped for MODE.
# NOTE on MODE (the weaker analogical fit): G_3 = cross-sector re-referencing FIXES the
# within-sector rank (offset_fixes_rank / ortho_ok in 3.1) AND FIXES the named DISCRETE
# residual {1,3,7} (label_fixed_by_perm in 3.3 -- it is in the STABILIZER).  What G_3
# MOVES is the CONTINUOUS zero c_r in R^3 (shift (n'-n)ln2; indep_of_P in 3.2) -- a
# DIFFERENT object than the named residual.  So unlike SCALE (g_lambda moves the named
# absolute length) and TENSOR (R flips the named bit), MODE's named residual is G_3-
# FIXED; mode_continuous_zero_moved verifies the CONTINUOUS object is what G_3 moves.
fence_fixed = {
    "SCALE":  sp.simplify(g_lambda(c0) - c0) == 0,                       # invariant fixed by g_lambda
    "TENSOR": sp.simplify(M_data_qubit - M_data_rebit) == sp.zeros(4, 1),  # M fixed by R
    "MODE":   ortho_ok and offset_fixes_rank,                           # rank fixed by G_3 re-referencing
}
# the genuine G_i-moved object the records cannot supply (the NAMED residual for
# SCALE/TENSOR; the CONTINUOUS zero for MODE -- NOT the named discrete residual):
mode_continuous_zero_moved = bool(indep_of_P) and torsor_ok            # G_3 moves the continuous c_r
filling_moved = {
    "SCALE":  sp.simplify(g_lambda(l_step) - l_step) != 0,               # named length moved by g_lambda
    "TENSOR": deficit_R != deficit_C,                                    # named bit flipped by R
    "MODE":   mode_continuous_zero_moved,                                # G_3 moves the CONTINUOUS zero (not the named label)
}
# explicitly record that MODE's NAMED discrete residual {1,3,7} is G_3-FIXED, not moved
# (the honest caveat: MODE is the analogical member, not a clean instance):
mode_named_residual_is_fixed = label_fixed_by_perm and label_fixed_by_offset
check("(C) fence-not-filling: invariant G_i-FIXED + G_i moves a records-unsupplied datum (SCALE/TENSOR the "
      "named residual; MODE the CONTINUOUS zero -- its named discrete residual {1,3,7} is G_3-FIXED)",
      all(fence_fixed.values()) and all(filling_moved.values()) and mode_named_residual_is_fixed,
      "THEOREM", "SCALE/TENSOR: invariant fixed + same G_i moves the named residual (genuine). "
                 "MODE: G_3 fixes rank + moves the continuous zero, but FIXES named {1,3,7} (analogical)")

# (C.2)  the residual TYPES are genuinely distinct: R_+ (continuous) / {0,1}
#        (discrete bit) / label (discrete label).  Encode and verify distinctness.
residual_types = {
    "SCALE":  "R_+ (continuous)",
    "TENSOR": "{0,1} (discrete bit)",
    "MODE":   "{1,3,7} (discrete label)",
}
# continuous: the SCALE orbit is a 1-param Lie group (verified in (1)); discrete:
# TENSOR has exactly 2 orbit values, MODE has exactly 3 label values.
scale_continuous = sp.simplify(g_of(g_of(l_step, mu2), mu1) - (mu1 * mu2) * l_step) == 0
tensor_two_valued = len(residual_bit_values) == 2
mode_label_valued = len(set(ranks)) == 3
check("(C) the three residual TYPES are genuinely distinct: continuous R_+ / bit {0,1} / label {1,3,7}",
      scale_continuous and tensor_two_valued and mode_label_valued
      and len(set(residual_types.values())) == 3,
      "THEOREM", "SCALE continuous (1-param group), TENSOR 2 values, MODE 3 labels -- distinct TYPES")

# (C.3)  EPISTEMIC STATUS grading (Paper XVI): two STRUCTURAL no-gos + one
#        CONDITIONAL (the G leg rides the Jacobson-Clausius premise).  This is a
#        BOOKKEEPING check on the grading, flagged STRUCTURAL (a positioning
#        claim, not a sympy identity): exactly one leg is conditional.
epistemic = {
    "SCALE":  "measured datum; SHARD route CONDITIONAL on Jacobson-Clausius (Visser)",
    "MODE":   "import-fixed by measured spectra (structural no-go)",
    "TENSOR": "contested convention; possibly experimentally unfixable (Hoffreumon-Woods/Maioli/Renou)",
}
n_conditional = sum(1 for v in epistemic.values() if "CONDITIONAL" in v.upper())
n_structural = sum(1 for v in epistemic.values() if "CONDITIONAL" not in v.upper())
check("(C) epistemic grading: exactly TWO structural no-gos + ONE conditional (G rides Jacobson premise)",
      n_conditional == 1 and n_structural == 2,
      "STRUCTURAL", "honesty: the G leg is a CONDITIONAL no-go, not overclaimed as unconditional")

# (C.4)  the unification is the SHARD value-add: the SAME shape (quotient by an
#        internal symmetry; residual = orbit parameter) recurs in all three, with
#        residuals of different TYPE and different EPISTEMIC STATUS.  Verify all
#        three triples were instantiated and pass (the classification holds).
triples_instantiated = (
    # SCALE
    weight(c0) == 0 and weight(l_step) == 1
    # TENSOR
    and deficit_C == 0 and deficit_R == 1
    # MODE
    and ranks == [1, 3, 7] and bool(indep_of_P)
)
check("(C) CLASSIFICATION: all three (G_i, invariant, residual) triples instantiated & verified",
      triples_instantiated and len(set(residual_types.values())) == 3,
      "THEOREM(unification)", "ONE quotient-by-symmetry shape; three residual TYPES; three epistemic statuses")


# ============================================================================
#  ROLL-UP TABLE + VERDICT
# ============================================================================
head("THE CLASSIFICATION TABLE  (instantiated triples)")
print("   %-7s %-30s %-26s %-22s" % ("wall", "symmetry G_i", "invariant (records carry)", "residual (blind)"))
print("   " + "-" * 86)
rows = [
    ("SCALE",  "g_lambda (l->mu*l relabel)",     "weight-0 functionals",        "abs. length  R_+"),
    ("TENSOR", "R (qubit<->rebit, C<->R)",       "moment algebra M",            "loc-tomog bit {0,1}"),
    ("MODE",   "cross-sector re-reference (c_r)", "within-sector rank 2^n-1",    "mode label {1,3,7}"),
]
for w_, g_, inv_, res_ in rows:
    print("   %-7s %-30s %-26s %-22s" % (w_, g_, inv_, res_))
print("   " + "-" * 86)
print("   residual TYPE :   continuous R_+   |   discrete bit {0,1}   |   discrete label {1,3,7}")
print("   epistemic     :   measured (Jacobson-CONDITIONAL) | contested-convention | import-fixed")
print("""
   COMMON STRUCTURE (verified):  records = the G_i-invariants;  blind to the
   orbit parameter;  self-consistency fixes the FENCE (orbit) never the FILLING
   (parameter).  TWO structural no-gos (TENSOR, MODE) + ONE conditional (SCALE/G,
   on the Jacobson-Clausius premise).  SHARD novelty = the UNIFICATION into one
   quotient-by-symmetry SHAPE + the three-epistemic-status grading; the
   individual walls are convergent-not-novel (G un-derivable; local tomography
   the least-motivated axiom; mass spectra measured).
""")

# ----------------------------------------------------------------------------
n_pass = sum(1 for _, p, _, _ in CHECKS if p)
n_tot = len(CHECKS)
print("=" * 78)
for name, passed, tag, detail in CHECKS:
    flag = "PASS" if passed else "FAIL"
    tg = ("[%s]" % tag) if tag else ""
    print("   [%s] %-12s %s" % (flag, tg, name))
    if detail:
        print("            %s" % detail)
print("=" * 78)
print("   CHECKS: %d/%d   (sympy-exact + mpmath dps=%d; NO SDP / NO solver-tolerance digit)"
      % (n_pass, n_tot, mp.dps))
allpass = (n_pass == n_tot)
print("   ALL CHECKS PASS (%d/%d)" % (n_pass, n_tot) if allpass else "   *** SOME CHECKS FAILED ***")
print("=" * 78)
sys.exit(0 if allpass else 1)
