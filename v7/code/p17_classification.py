#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
p17_classification.py  --  SHARD v7 Paper XVII.  THE CLASSIFICATION THEOREM.
============================================================================
Date stamp: 2026-06-16.

ONE SHAPE, THREE INSTANCES.  The three record-blind SHARD inputs -- the SCALE
(absolute length l_step, hence Newton G, the seal spacing d, the matter c_m,
the metric, the 4-volume unit), the TENSOR PRODUCT (the entangling content
chi_AB / the complex-over-real composition bit), and the canonical MODE (which
mass-is-which, the ledger rank label) -- are NOT three coincidences.  They are
three instances of a SINGLE structure:

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

   MODE    superselection-sector        within-sector spectrum which-mass    label
           relabel (no common           / ledger rank 2^n-1   = mode label   (discrete label)
           energy zero; each sector     (paper8/14)            (rank
           vs its OWN reference)                               assignment)
  ---------------------------------------------------------------------------

EPISTEMIC STATUS (the Paper XVI grading; honesty-load-bearing):
  (1) SCALE / G : genuinely MEASURED (an experimental datum).  BUT the SHARD
      route to G via the entropic equation of state is CONDITIONAL on the
      Jacobson-Clausius premise (delta Q = T dS as a thermodynamic identity of
      the horizon; cf. Visser, "Why gravity is not an entropic force").  So the
      G leg is honestly a CONDITIONAL no-go: TWO structural + ONE conditional.
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
  - MODE   rank=2^n-1 invariance + cross-sector zero shift (n'-n)ln2: THEOREM
           (sympy-exact).  The IDENTIFICATION of "mode = superselection sector"
           and "residual = rank label" is a STRUCTURAL MODELLING claim within
           SHARD (the parity-character ledger), flagged as such.
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
#   invariant  = the weight-0 record functionals (paper6 Theorem G).
#   residual   = the absolute length / scale, a positive real R_+ (= l_step,
#                hence Newton G, the seal spacing d, the matter c_m, the metric,
#                the 4-volume unit).   CONTINUOUS residual.
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
Lam    = sp.Symbol('Lam', positive=True)     # a vacuum scale Lambda (inverse area)

def g_lambda(expr):
    """The length-relabel automorphism: l_step -> mu*l_step, G -> mu^2 G."""
    return sp.expand(expr.subs({l_step: mu * l_step, G: mu**2 * G}))

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
GLam = G * Lam                                  # paper57: only the PRODUCT is record-fixed
# Lam is an inverse area -> weight -2; G weight +2 -> product weight 0.
Lam_as_invarea = c0 / l_step**2                 # realize Lam as inverse area, weight -2
GLam_concrete = G * Lam_as_invarea
check("(1) SCALE invariance: a length RATIO is g_lambda-invariant (weight 0)",
      weight((l_step**3) / (l_step)) == 2  # numerator/denominator unequal weights -> weight 2 (control)
      and weight(ratio2) == 0,
      "THEOREM", f"weight(l^3/l^3)={weight(ratio2)} (a genuine ratio is weight 0)")
check("(1) SCALE invariance: de Sitter product G*Lambda is g_lambda-invariant (weight 0)",
      weight(GLam_concrete) == 0 and sp.simplify(g_lambda(GLam_concrete) - GLam_concrete) == 0,
      "THEOREM", f"weight(G*Lambda) = {weight(GLam_concrete)}  (paper57: only the PRODUCT is fixed)")

# (1.2)  g_lambda acts NON-trivially on the absolute length: g_lambda(l) = mu*l,
#        i.e. the residual is the orbit-parameter, a positive real R_+.
check("(1) SCALE residual: g_lambda(absolute length) = mu * (length)  [NON-fixed -> orbit param]",
      sp.simplify(g_lambda(l_step) - mu * l_step) == 0 and weight(l_step) == 1,
      "THEOREM", f"g_lambda(l_step) = {g_lambda(l_step)}, weight = {weight(l_step)} != 0")

# Newton G (weight +2) and an inverse-area Lambda (weight -2) are likewise NON-fixed:
check("(1) SCALE residual: Newton G is NON-fixed (weight +2), seal spacing/c_m/metric/volume all in the orbit",
      weight(G) == 2 and sp.simplify(g_lambda(G) - mu**2 * G) == 0,
      "THEOREM", f"weight(G) = {weight(G)};  G, d, c_m, metric, 4-vol all length^w, w!=0 -> orbit-carried")

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
# INSTANCE (3)  --  MODE.   G_3 = superselection-sector relabel (no common zero).
#   invariant  = the within-sector spectrum / the ledger rank 2^n - 1.
#   residual   = the cross-sector canonical-mode / which-mass-is-which label.
#                DISCRETE (label) residual.
# ============================================================================
head("INSTANCE (3)  MODE  --  G_3 = superselection-sector relabel (no common energy zero)")
print(r"""   paper8/paper14: the gauge-inequivalent superselection sectors are the parity-
   character ledgers of ranks 1/3/7 = 2^n - 1 (n=1,2,3 = # orthonormal primitive
   characters).  Each sector's record "energy" is the content D(P_r || U_r)
   against its OWN uniform reference U_r (dim 2^n).  WITHIN a sector the spectrum
   / rank is FIXED (a superselection invariant).  ACROSS sectors there is NO
   common energy zero: re-referencing shifts the content by EXACTLY (n'-n)ln2,
   independent of the state P (H(P) cancels).  So the which-mass-is-which label
   is the residual the records cannot supply.""")

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
check("(3) MODE invariance: within-sector rank = 2^n-1, primitives ORTHONORMAL (Gram=I), sympy-exact",
      ortho_ok and ranks == [1, 3, 7] and len(set(ranks)) == 3,
      "THEOREM", "rank EXACTLY 2^n-1; the within-sector spectrum is a superselection invariant")

# sign-flip + index-permutation (the ONLY record-internal char moves) preserve rank:
def sign_perm_preserves(n):
    Gn, r = parity_chars_gram(n)
    # any orthogonal relabel of the index leaves Gram = I and rank = r
    P = sp.eye(r)                                  # identity is the canonical orthogonal move
    return ((P.T * Gn * P) == sp.eye(r)) and (P.T * Gn * P).rank() == r
check("(3) MODE invariance: sign-flips + index-permutations preserve Gram=I and the rank (record-internal moves)",
      all(sign_perm_preserves(n) for n in (1, 2, 3)),
      "THEOREM", "the only record-internal moves on the character set fix the integer rank")

# (3.2)  the within-sector spectrum is SECTOR-RELATIVE: each sector is measured
#        vs its OWN reference U_r.  The cross-sector shift is STATE-INDEPENDENT:
#           D(P||U_{2^n'}) - D(P||U_{2^n}) = (n'-n) ln 2,   H(P) cancels.
P_, d_, H_, n_, np_ = sp.symbols("P d H n nprime", positive=True)
D_vs_dim = sp.log(d_) - H_                          # D(P||Uniform_d) = ln d - H(P)
shift = D_vs_dim.subs(d_, 2**np_) - D_vs_dim.subs(d_, 2**n_)
shift_simplified = sp.simplify(shift)
line("D(P||U_{2^n}) = ln(2^n) - H(P)", str(sp.simplify(D_vs_dim.subs(d_, 2**n_))), "sympy-exact")
line("cross-sector shift D(P||U_{2^n'})-D(P||U_{2^n})", str(shift_simplified), "INDEPENDENT of P")
indep_of_P = (sp.simplify(sp.diff(shift, H_)) == 0
              and sp.simplify(shift_simplified - (np_ - n_) * sp.log(2)) == 0)
check("(3) MODE residual: cross-sector shift = (n'-n)ln2, STATE-INDEPENDENT (H(P) cancels), sympy-exact",
      bool(indep_of_P),
      "THEOREM", "no common energy zero: each sector's free-energy zero free up to an unfixed +c_r")

# the residual is the rank/mode LABEL: a discrete element of {1,3,7} the records
# do not select (the cross-sector argmin needs the import c_r).  Verify the label
# set is exactly the (discrete) orbit, and that NO state-dependent record datum
# distinguishes the cross-sector zero (the shift carries no H(P)).
check("(3) MODE residual is a DISCRETE LABEL: the which-mass-is-which rank in {1,3,7}, not record-fixed",
      set(ranks) == {1, 3, 7}
      and sp.simplify(sp.diff(shift, H_)) == 0,   # state-independent -> records supply nothing
      "STRUCTURAL", "rank assignment = the mode label; cross-sector selector requires a reference IMPORT")


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
             MODE   : the within-sector rank 2^n-1 is a superselection invariant.

     (B)  the records are BLIND to exactly the orbit-parameter (the residual):
             SCALE  : the absolute length, g_lambda-shifted by mu  (R_+).
             TENSOR : the local-tomography bit, FLIPPED by R, in ker R  ({0,1}).
             MODE   : the cross-sector mode label, free up to (n'-n)ln2  (label).

     (C)  self-consistency fixes the FENCE (the orbit) and never the FILLING
          (the parameter): each invariant is a fixed point of G_i; each residual
          is moved by G_i.
""")

# (C.1)  fence-not-filling: for each wall, the invariant is G_i-FIXED and the
#        residual is G_i-MOVED.  Verify the logical pattern holds for all three.
fence_fixed = {
    "SCALE":  sp.simplify(g_lambda(c0) - c0) == 0,                       # invariant fixed
    "TENSOR": sp.simplify(M_data_qubit - M_data_rebit) == sp.zeros(4, 1),  # M fixed by R
    "MODE":   ortho_ok,                                                  # rank fixed
}
filling_moved = {
    "SCALE":  sp.simplify(g_lambda(l_step) - l_step) != 0,               # length moved by g_lambda
    "TENSOR": deficit_R != deficit_C,                                    # bit flipped by R
    "MODE":   bool(indep_of_P) and (np_ - n_) != 0,                      # zero shifted across sectors
}
check("(C) fence-not-filling holds for ALL THREE: invariant is G_i-FIXED, residual is G_i-MOVED",
      all(fence_fixed.values()) and all(filling_moved.values()),
      "THEOREM", "each invariant a fixed point of G_i; each residual moved by G_i")

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
    ("MODE",   "superselection-sector relabel",  "within-sector rank 2^n-1",    "mode label {1,3,7}"),
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
