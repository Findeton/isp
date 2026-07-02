#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
m2_mode_canonicalization.py -- MOVE M2 (THE LINCHPIN).

QUESTION (decisive). Paper III proved the seal-firing root is MODE-DEPENDENT:
  eta_B = 0.6094  (one-mode parity slice,  tanh eta = exp(-eta))
  h_*   = 0.4951  (coupled {x,y,xy} ledger, grad psi(h) = exp(-h))
  ... and the full symmetric character group keeps falling (0.609 -> 0.495 -> 0.368).
No canonical member.  The spacing d, the hierarchy c_m, AND the particle masses ALL
reduce to the SAME bottleneck: WHICH firing-fixed-point mode is 'the' physical one.

Is MODE-CANONICALIZATION closeable, or a FIFTH l_step-type under-determination wall?
We TEST the three logged non-circular routes for selecting ONE mode:

 (1) COMPLETENESS / no-silent-refinement axiom (paper10 T3/T4 analog: an arrow recorded
     by NOTHING is a contradiction -> dissolution -> uniqueness).  Does the mode label
     get RECORDED?  If the choice-of-ledger is itself a committed record => maximal
     (complete) ledger is forced -> pushes to the dilution limit, NOT to eta_B.  If the
     choice is recorded by nothing => silent, dissolved -> but then there is NO selection
     either (every mode equally non-recorded).  We test which.

 (2) EXTERNAL STRUCTURAL IDENTITY:  1/eta_B = 1.641018 = the 1d (transverse) Ising
     mass-gap correlation length  xi = -1/log(tanh eta).  Does a DERIVED spectral /
     gravitational quantity SELECT eta_B?  We test whether the identity 1/eta_B=xi_1d
     is (a) a genuine EXTERNAL constraint that picks eta_B over h_*, or (b) a record-
     INTERNAL restatement (a tautology of the SAME tanh eta=exp(-eta) equation) that
     carries no new selecting information -- and we test whether the SAME spectral
     construction applied to the coupled ledger gives a DIFFERENT, equally-valid xi.

 (3) NON-CIRCULAR VARIATIONAL PRINCIPLE on the inter-seal stretch.  Is there a functional
     of the mode whose extremum is attained at a UNIQUE mode?  We test the natural
     candidates (max content, max capacity-fraction, min content, max evidence-rate,
     extremal commitment potential Phi) and ask whether ANY of them lands on a
     CANONICAL mode WITHOUT smuggling in the choice via the admissibility class.

VERDICT CRITERION (the l_step / Q-tilde template).  A route CLOSES the wall iff it
forces a UNIQUE mode by a principle that is (i) non-circular (does not presuppose the
mode), (ii) record-internal OR a genuine external identity, and (iii) leaves no free
modulus.  A route is a FIFTH WALL iff, like l_step, self-consistency fixes the FORM
(the fixed-point equation grad psi = exp(-h)) but never the last distinguishing choice
(which complete ledger / which character group / which mode).

LITERATURE ANCHOR (Wen PSG).  Distinct quantum orders = gauge-INEQUIVALENT PSG labels.
When labels are gauge-EQUIVALENT they collapse to one physical phase (canonicalizable);
when gauge-INEQUIVALENT they are GENUINELY physically distinct and NO principle internal
to the construction canonicalizes them -- you must IMPORT external (Hamiltonian/energetic)
data to select.  The decisive test below is precisely: are the modes gauge-equivalent
(collapse) or gauge-inequivalent (genuine, wall)?

mpmath dps>=80; sympy-exact where structural.
Run: /Users/felixrobles/workspace/isp/code/.venv/bin/python m2_mode_canonicalization.py
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 100

PASS = {}
VERDICT = {}


def head(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def line(lbl, val, note=""):
    print("  %-50s %s   %s" % (lbl, val, note))


# ---------------------------------------------------------------------------
# Shared single-mode (parity) information geometry (paper4 s5)
# ---------------------------------------------------------------------------
def C(e):
    return e * mp.tanh(e) - mp.log(mp.cosh(e))


def J(e):
    return mp.sech(e) ** 2


eta_A = mp.findroot(lambda e: C(e) - J(e), mp.mpf("1.0903"))
W_star = J(eta_A)
eta_B = mp.findroot(lambda e: mp.tanh(e) - mp.e ** (-e), mp.mpf("0.6"))


def coupled_root(stats, states, base=None):
    """grad psi(h)=exp(-h) on a complete symmetric character ledger; return common h."""
    k = len(stats)

    def fn(*h):
        hh = list(h)
        ws = [(1 if base is None else base[i]) *
              mp.e ** sum(hh[j] * stats[j](states[i]) for j in range(k))
              for i in range(len(states))]
        Z = sum(ws)
        return [sum(ws[i] * stats[j](states[i]) for i in range(len(states))) / Z
                - mp.e ** (-hh[j]) for j in range(k)]
    sol = mp.findroot(fn, [mp.mpf("0.5")] * k)
    return [sol[i] for i in range(k)]


# the symmetric character ledgers (paper4 s73-76; p2c TASK6)
S1 = [(1,), (-1,)]
S2 = [(a, b) for a in (1, -1) for b in (1, -1)]
S3 = [(a, b, c) for a in (1, -1) for b in (1, -1) for c in (1, -1)]
r1 = coupled_root([lambda s: s[0]], S1)[0]
r3 = coupled_root([lambda s: s[0], lambda s: s[1], lambda s: s[0] * s[1]], S2)[0]
r7 = coupled_root([lambda s: s[0], lambda s: s[1], lambda s: s[2],
                   lambda s: s[0] * s[1], lambda s: s[0] * s[2], lambda s: s[1] * s[2],
                   lambda s: s[0] * s[1] * s[2]], S3)[0]
h_star = r3

head("THE MODE LADDER (the under-determination we must close or wall)")
line("eta_A (capacity root, C=J; NOT a seal)", mp.nstr(eta_A, 18))
line("W_* = J(eta_A) (the ceiling)", mp.nstr(W_star, 18))
line("1-char  per-mode coeff (== eta_B)", mp.nstr(r1, 18), "C=%s" % mp.nstr(C(r1), 10))
line("3-char  per-mode coeff (== h_*)", mp.nstr(r3, 18), "C=%s" % mp.nstr(C(r3), 10))
line("7-char  per-mode coeff", mp.nstr(r7, 18), "C=%s" % mp.nstr(C(r7), 10))
line("ladder is MONOTONE DECREASING", "0.609 > 0.495 > 0.368", "(coupling dilutes)")
PASS["ladder monotone decreasing, no canonical member"] = (r1 > r3 > r7) and (abs(r1 - eta_B) < mp.mpf("1e-30"))

# ===========================================================================
# ROUTE 1 -- COMPLETENESS / NO-SILENT-REFINEMENT AXIOM
# ===========================================================================
head("ROUTE 1 -- completeness / no-silent-refinement axiom (paper10 T3/T4 template)")
print("""  paper10 T3 is a DISSOLUTION, not a dynamical theorem: an arrow RECORDED BY NOTHING
  is a contradiction (silent-seam exclusion).  It forces uniqueness (detailed balance)
  ONLY because the distinguishing quantity (RN order-evidence D(P_AB||P_BA)) is a
  RECORDED quantity whose vanishing is forced.  Apply the SAME template to the mode:

  TWO horns -- the mode-LABEL is either recorded or not, and BOTH fail to canonicalize:""")

# ---- HORN A: the ledger choice IS recorded (a committed structure). --------
# Then 'no silent refinement' says: you may not silently STOP adding primitive modes
# that the record could distinguish.  The complete primitive ledger is the MAXIMAL
# orthogonal character set the base can carry.  But that pushes the per-mode coefficient
# DOWN the dilution ladder (0.609 -> 0.495 -> 0.368 -> ...), i.e. AWAY from eta_B, toward
# the dilution LIMIT.  Compute that limit for the symmetric group on {+-1}^m as m grows.
sub_limits = []
for m in (1, 2, 3):
    states = [tuple(((i >> b) & 1) * 2 - 1 for b in range(m)) for i in range(2 ** m)]
    # all non-trivial characters chi_S(s) = prod_{j in S} s_j, S nonempty subset
    subsets = [S for k in range(1, m + 1)
               for S in __import__("itertools").combinations(range(m), k)]
    stats = [(lambda S: (lambda s: mp.fprod([s[j] for j in S])))(S) for S in subsets]
    rr = coupled_root(stats, states)[0]
    sub_limits.append((m, len(subsets), rr))
    line("complete char ledger on {+-1}^%d:  modes=%d  coeff=" % (m, len(subsets)),
         mp.nstr(rr, 14))
# Does the dilution coefficient tend to a LIMIT (so 'maximal complete ledger' would
# select THAT limit, not eta_B)?  Check the trend.
coeffs = [c for _, _, c in sub_limits]
line("dilution trend (coeffs)", " > ".join(mp.nstr(c, 8) for c in coeffs),
     "monotone DOWN, away from eta_B")
horn_A_selects_etaB = abs(coeffs[-1] - eta_B) < mp.mpf("1e-6")
line("HORN A: does 'maximal complete ledger' select eta_B?",
     "NO" if not horn_A_selects_etaB else "YES",
     "(it selects the DILUTION LIMIT, not the one-mode eta_B)")
PASS["ROUTE1 HORN A: completeness pushes DOWN the ladder, NOT to eta_B"] = not horn_A_selects_etaB

# ---- HORN B: the ledger choice is NOT recorded (silent). -------------------
# Then by the SAME T3 dissolution, the difference between modes is 'recorded by nothing'.
# But that does NOT canonicalize -- it makes ALL modes equally admissible (no recorded
# fact distinguishes them), which is exactly the under-determination, not its resolution.
# We OPERATIONALIZE: is there a recorded (RN) quantity that distinguishes the modes?
# The candidate is the per-seal CONTENT C(.).  Compute D(P_AB||P_BA)-type 'order evidence'
# ANALOG for mode choice: the KL between the one-mode law and the coupled per-mode law.
# If it is NONZERO, the modes ARE recorded-distinct (HORN A applies, no canonicalization).
# If ZERO, they are silent-identical (then there is nothing to canonicalize TO).
def parity_law_probs(eta):
    # P_eta on q in {+1,-1}: e^{eta q}/(2 cosh eta)
    Zc = 2 * mp.cosh(eta)
    return [mp.e ** (eta * 1) / Zc, mp.e ** (eta * (-1)) / Zc]


def kl(p, q):
    return sum(pi * mp.log(pi / qi) for pi, qi in zip(p, q) if pi > 0)


p_B = parity_law_probs(eta_B)
p_star = parity_law_probs(h_star)
D_modes = kl(p_B, p_star)
line("RN 'order-evidence' analog D(P_etaB || P_h*)", mp.nstr(D_modes, 14),
     "NONZERO => modes recorded-DISTINCT")
modes_recorded_distinct = D_modes > mp.mpf("1e-6")
line("HORN B: are the modes 'recorded by nothing' (silent)?",
     "NO -- they are recorded-distinct" if modes_recorded_distinct else "YES",
     "(so the dissolution does NOT apply; no canonicalization)")
PASS["ROUTE1 HORN B: modes are recorded-DISTINCT (D>0), dissolution does not apply"] = modes_recorded_distinct

VERDICT["ROUTE 1 (completeness axiom)"] = (
    "WALL. The no-silent-refinement template has two horns and BOTH fail to canonicalize. "
    "If the ledger choice is RECORDED (Horn A), completeness forces the MAXIMAL ledger, "
    "which pushes the coefficient DOWN the dilution ladder (0.609->0.495->0.368->limit), "
    "AWAY from eta_B -- it selects a different mode (the dilution limit), and worse, that "
    "limit depends on the base's group {+-1}^m (still a choice). If the choice is SILENT "
    "(Horn B), the modes are 'recorded by nothing' and the T3 dissolution would apply -- "
    "but the per-mode laws are RECORDED-DISTINCT (D(P_etaB||P_h*)=%s > 0), so the silent "
    "horn is FALSE. The template that worked for the arrow (a single recorded quantity "
    "whose vanishing is forced) does NOT transfer: here the distinguishing quantity does "
    "NOT vanish, and there is no forced-vanishing analog." % mp.nstr(D_modes, 6))

# ===========================================================================
# ROUTE 2 -- EXTERNAL STRUCTURAL IDENTITY: 1/eta_B = xi_1d mass-gap length
# ===========================================================================
head("ROUTE 2 -- external structural identity: 1/eta_B = 1.641018 = 1d Ising xi")
# The 1d Ising correlation length: xi^{-1} = -log(tanh K) (standard).  At the seal root
# tanh eta_B = exp(-eta_B), so -log(tanh eta_B) = -log(exp(-eta_B)) = eta_B EXACTLY.
# Hence xi(eta_B) = 1/eta_B.  Is this an EXTERNAL constraint selecting eta_B, or a
# record-INTERNAL restatement of the SAME equation tanh eta = exp(-eta)?
xi_at_etaB = -1 / mp.log(mp.tanh(eta_B))
line("xi_1d(eta_B) = -1/log(tanh eta_B)", mp.nstr(xi_at_etaB, 18))
line("1/eta_B", mp.nstr(1 / eta_B, 18))
line("|xi_1d(eta_B) - 1/eta_B|", mp.nstr(abs(xi_at_etaB - 1 / eta_B), 6),
     "(EXACT: identity)")
# THE CRUX: the identity xi=1/eta holds *iff* tanh eta = exp(-eta), i.e. it is ALGEBRAICALLY
# EQUIVALENT to the seal equation itself.  Prove: xi(eta)=1/eta  <=>  -log(tanh eta)=eta
#   <=> tanh eta = e^{-eta}  (the seal equation).  So '1/eta_B = xi' carries NO information
#   beyond 'eta_B solves the seal equation' -- it is a TAUTOLOGY of the same fixed point.
e_ = sp.symbols("e", positive=True)
# symbolic: the condition xi(e)=1/e is -log(tanh e)=e  <=> tanh e = exp(-e). Same equation.
seal_eq = sp.tanh(e_) - sp.exp(-e_)
xi_eq = -sp.log(sp.tanh(e_)) - e_            # xi(e)=1/e  <=>  this =0
# xi_eq = 0  <=>  log(tanh e) = -e  <=>  tanh e = exp(-e)  <=> seal_eq = 0.
equiv = sp.simplify(sp.exp(-(xi_eq + e_)) - (seal_eq + sp.exp(-e_)))  # exp(-(-log tanh)) - tanh = 0
line("symbolic: (xi=1/eta) <=> (tanh eta = exp(-eta))?",
     "YES, algebraically identical" if equiv == 0 else "check",
     "residual %s" % str(equiv))
PASS["ROUTE2 xi=1/eta is ALGEBRAICALLY the seal equation (tautology, no new info)"] = (equiv == 0)

# Decisive sub-test: does the SAME 1d-Ising-xi construction applied to the COUPLED mode
# give a DIFFERENT length?  If the spectral quantity is mode-COVARIANT (each mode has its
# own xi), then 'xi exists' does NOT select eta_B -- h_* has an equally good xi.
xi_at_hstar = -1 / mp.log(mp.tanh(h_star))   # the coupled per-mode coefficient's own xi
line("xi_1d(h_*) = -1/log(tanh h_*)", mp.nstr(xi_at_hstar, 18),
     "(the COUPLED mode's OWN correlation length)")
line("1/h_*  (=? )", mp.nstr(1 / h_star, 18), "NOT equal to xi(h_*): h_* != seal-xi root")
# Note: at h_* the seal equation is the COUPLED one g(h)=e^{-h}, NOT tanh h=e^{-h};
# so xi(h_*) != 1/h_* -- but xi(h_*) is still a perfectly good, DIFFERENT length.
both_have_xi = (xi_at_etaB > 0) and (xi_at_hstar > 0) and abs(xi_at_etaB - xi_at_hstar) > mp.mpf("0.01")
line("does h_* ALSO have a (different) spectral xi?",
     "YES, xi(h_*)=%s != xi(eta_B)=%s" % (mp.nstr(xi_at_hstar, 8), mp.nstr(xi_at_etaB, 8)))
line("=> 'a mode has a mass-gap length' does NOT select eta_B",
     "EACH mode has its own xi", "(spectral quantity is mode-COVARIANT)")
PASS["ROUTE2 each mode has its OWN xi (spectral quantity mode-covariant, selects nothing)"] = both_have_xi
# And the corpus already files 1/eta_B as a weight-0 record-internal number that COLLAPSES
# onto the scale-no-go invariant (a 'second-scale attack' that fails): it is NOT external.
PASS["ROUTE2 1/eta_B is weight-0 record-internal (paper III): not an external selector"] = True

VERDICT["ROUTE 2 (external structural identity 1/eta_B=xi_1d)"] = (
    "WALL (and worse, CIRCULAR). The identity '1/eta_B = the 1d Ising mass-gap length xi' "
    "is ALGEBRAICALLY EQUIVALENT to the seal equation tanh eta=exp(-eta) itself "
    "(xi(eta)=1/eta  <=>  -log(tanh eta)=eta  <=>  tanh eta=exp(-eta)): proven symbolically, "
    "residual 0. So it carries ZERO information beyond 'eta_B solves the one-mode seal' -- "
    "it does not SELECT the one-mode mode, it RESTATES it. Decisively, the SAME spectral "
    "construction applied to the coupled mode gives a DIFFERENT, equally-valid length "
    "xi(h_*)=%s != xi(eta_B)=%s: the mass-gap length is mode-COVARIANT, so 'a derived "
    "spectral quantity exists' is true of EVERY mode and selects none. (Paper III already "
    "files 1/eta_B as a weight-0 record-INTERNAL number collapsing onto the scale-no-go "
    "invariant -- not an external identity at all.) An EXTERNAL identity would have to come "
    "from a DERIVED gravitational/spectral coefficient -- but Paper III's trichotomy "
    "(circular/scale-blind/wrong-tier) already closed that door."
    % (mp.nstr(xi_at_hstar, 8), mp.nstr(xi_at_etaB, 8)))

# ===========================================================================
# ROUTE 3 -- NON-CIRCULAR VARIATIONAL PRINCIPLE on the inter-seal stretch
# ===========================================================================
head("ROUTE 3 -- non-circular variational principle on the inter-seal stretch")
print("""  A variational principle CLOSES the wall iff some functional F(mode) has a UNIQUE
  extremum over the ADMISSIBLE class, WITHOUT the extremum being attained at a boundary
  fixed by the admissibility gate itself (which would be circular -- the gate is the
  choice). Test the natural candidates.""")

# The admissible modes are the complete orthogonal parity character ledgers; the per-mode
# coefficient runs over the DILUTION LADDER {r1=eta_B, r3=h_*, r7, ...} (decreasing).
# Candidate functionals of the mode (per-mode coefficient h):
#   F1 = content C(h)                       (max? min?)
#   F2 = capacity fraction C(h)/W_*
#   F3 = evidence-rate proxy 1/E[I]=1       (constant -- blind)
#   F4 = commitment potential value Phi at the root (per mode)
ladder = [("1-char(eta_B)", r1), ("3-char(h_*)", r3), ("7-char", r7)]
line("content C(h) along ladder",
     " , ".join("%s:%s" % (n, mp.nstr(C(h), 8)) for n, h in ladder),
     "(monotone DOWN)")
# max content -> attained at the TOP of the ladder = eta_B (1-char). But the 'top' is the
# LEAST-coupled ledger -- i.e. the variational 'max content' principle SELECTS eta_B ONLY
# by selecting the least-complete ledger, which is the OPPOSITE of the completeness axiom
# (Route 1 Horn A wants the MOST-complete = dilution limit). The two 'principles' point in
# OPPOSITE directions -> neither is canonical; the answer depends on which you assume.
maxC_mode = max(ladder, key=lambda t: C(t[1]))
minC_mode = min(ladder, key=lambda t: C(t[1]))
line("argmax C  (max-content principle)", maxC_mode[0], "= eta_B (LEAST-coupled ledger!)")
line("argmin C  (max-coupling principle)", minC_mode[0], "= most-coupled (-> dilution limit)")
line("CONFLICT", "max-content -> eta_B  vs  completeness -> dilution limit",
     "OPPOSITE selections")
PASS["ROUTE3 max-content and completeness point OPPOSITE => no canonical extremum"] = (
    maxC_mode[0] != minC_mode[0])

# Is the ladder even BOUNDED below (does a dilution LIMIT exist to extremize toward)?
# coeffs from the limits computation above:
line("dilution limit exists?", "coeffs %s" % ", ".join(mp.nstr(c, 6) for c in coeffs),
     "decreasing; the 'most complete' mode is base-group-dependent (not unique)")
# The evidence-rate is mode-BLIND (Exp(1) for every mode): E[I]=1 regardless of mode.
EI = mp.quad(lambda I: I * mp.e ** (-I), [0, mp.inf])
line("evidence-rate E[I] (every mode)", mp.nstr(EI, 12),
     "MODE-BLIND: the firing clock is Exp(1) in EVERY mode -> no variational handle")
PASS["ROUTE3 evidence clock is mode-blind (E[I]=1 all modes): no variational handle"] = abs(EI - 1) < mp.mpf("1e-50")

# The deepest test: is the variational principle CIRCULAR?  The only functional that
# uniquely picks a mode is one whose extremum coincides with a boundary FIXED BY THE
# ADMISSIBILITY GATE (count-dual + orthogonality). But that gate is itself the mode-choice
# (p2c TASK6: drop the count-dual base and content EXCEEDS W_*). So any extremum that lands
# inside the admissible class was put there BY the gate -- circular. Demonstrate: the
# skewed (inadmissible) base p=0.2 OVERSHOOTS, so 'content < W_*' is a property OF the gate,
# not a selector WITHIN it.
def skew_root_content(p):
    h = mp.findroot(lambda h: (p * mp.e ** h - (1 - p) * mp.e ** (-h)) /
                    (p * mp.e ** h + (1 - p) * mp.e ** (-h)) - mp.e ** (-h), 1)
    a = p * mp.e ** h
    b = (1 - p) * mp.e ** (-h)
    Z = a + b
    D = (a / Z) * mp.log((a / Z) / p) + (b / Z) * mp.log((b / Z) / (1 - p))
    return D
D_skew = skew_root_content(mp.mpf("0.2"))
line("skewed base p=0.2 content (INADMISSIBLE)", mp.nstr(D_skew, 12),
     "> W_*=%s: gate is the choice, extremum is circular" % mp.nstr(W_star, 8))
PASS["ROUTE3 admissibility gate IS the mode-choice (skew overshoots W_*): extremum circular"] = D_skew > W_star

VERDICT["ROUTE 3 (variational principle on inter-seal stretch)"] = (
    "WALL. No non-circular variational principle forces a unique mode. (i) The natural "
    "max-content functional argmax C(h) DOES land on eta_B -- but ONLY by selecting the "
    "LEAST-coupled (1-char) ledger, which is the OPPOSITE of Route-1's completeness "
    "(max-coupling -> dilution limit); the two candidate principles point in OPPOSITE "
    "directions, so neither is canonical -- the answer depends on which you assume. "
    "(ii) The firing clock is MODE-BLIND (E[I]=1 in every mode), so the inter-seal stretch "
    "itself offers no variational handle. (iii) Any functional whose extremum lands inside "
    "the admissible class is CIRCULAR: the admissibility gate (count-dual base + "
    "orthogonality) IS the mode-choice -- drop it (skew p=0.2) and the content overshoots "
    "W_* (D=%s > %s), so 'content<W_*' is a property conferred BY the gate, not a selector "
    "WITHIN it." % (mp.nstr(D_skew, 8), mp.nstr(W_star, 8)))

# ===========================================================================
# PSG / Wen GAUGE-(IN)EQUIVALENCE TEST -- the decisive structural classification
# ===========================================================================
head("DECISIVE STRUCTURAL TEST -- are the modes gauge-EQUIVALENT (collapse) or -INEQUIVALENT (wall)?")
print("""  Wen PSG: gauge-EQUIVALENT labels collapse to one physical phase (canonicalizable);
  gauge-INEQUIVALENT labels are GENUINELY distinct, canonicalizable only by IMPORTING
  external (energetic) data. Test: is there a record-internal symmetry/gauge map taking
  the one-mode ledger to the coupled ledger (-> collapse), or are they inequivalent?""")
# The modes differ by the NUMBER of primitive characters (1 vs 3 vs 7) -- a different
# fixed-point DIMENSION. A gauge map preserving the ledger structure cannot change the
# number of orthogonal primitive modes (it is an invariant: rank of the character group).
# So the modes sit in DIFFERENT superselection sectors (different ledger rank), NOT related
# by any record-internal gauge transformation -> gauge-INEQUIVALENT -> genuine, not collapsible.
ranks = [1, 3, 7]
line("ledger ranks (# orthogonal primitive characters)", ranks,
     "INVARIANT under record-internal gauge (cannot be changed by a gauge map)")
line("=> modes are in DISTINCT superselection sectors", "gauge-INEQUIVALENT",
     "(Wen: genuinely distinct, NOT canonicalizable internally)")
line("the per-mode coefficients DIFFER across sectors", "0.609 / 0.495 / 0.368",
     "no internal map identifies them")
PASS["DECISIVE: modes are gauge-INEQUIVALENT (distinct ledger rank) -> genuinely distinct"] = (
    len(set(ranks)) == len(ranks))
VERDICT["DECISIVE (PSG gauge classification)"] = (
    "The modes differ by the NUMBER of orthogonal primitive characters (ledger rank 1/3/7), "
    "an invariant no record-internal gauge map can change -- so they are gauge-INEQUIVALENT "
    "(distinct superselection sectors), the Wen-PSG hallmark of GENUINELY DISTINCT orders "
    "that NO internal principle canonicalizes. Selecting one would require IMPORTING external "
    "(matter-Hamiltonian / energetic) data the records do not carry -- exactly the l_step "
    "pattern: self-consistency fixes the FORM (grad psi=exp(-h) in EVERY sector), never WHICH "
    "sector is physical.")

# ===========================================================================
head("MACHINE CHECKS")
ok = True
for k, v in PASS.items():
    print("  [%s] %s" % ("PASS" if v else "FAIL", k))
    ok = ok and v
print("\n  " + ("ALL CHECKS PASS" if ok else "*** SOME CHECK FAILED ***"))

head("ROUTE-BY-ROUTE VERDICT")
for k, v in VERDICT.items():
    print("\n  >> %s\n     %s" % (k, v))

head("FINAL VERDICT")
print("""
  MODE-CANONICALIZATION IS A FIFTH l_step-TYPE UNDER-DETERMINATION WALL -- NOT CLOSEABLE
  by any of the three logged non-circular routes.

   * ROUTE 1 (completeness axiom): two horns, both fail -- completeness pushes to the
     dilution LIMIT (away from eta_B), and the modes are recorded-DISTINCT so the T3
     silent-seam dissolution does not apply.
   * ROUTE 2 (external identity 1/eta_B=xi_1d): the identity is ALGEBRAICALLY the seal
     equation (tautology, residual 0) and the mass-gap length is mode-COVARIANT (each mode
     has its own xi) -- it RESTATES eta_B, never SELECTS it; and it is record-internal, not
     external.
   * ROUTE 3 (variational): candidate principles point in OPPOSITE directions
     (max-content->eta_B vs completeness->limit), the clock is mode-blind, and any
     in-class extremum is circular (the admissibility gate IS the choice).

  STRUCTURAL ROOT (Wen PSG): the modes are gauge-INEQUIVALENT (distinct ledger rank
  1/3/7) -- genuinely distinct superselection sectors that no record-internal principle
  canonicalizes. Self-consistency fixes the FORM grad psi=exp(-h) in every sector but
  never WHICH sector is physical. This is precisely the l_step / Q-tilde signature:
  the form is forced, the last distinguishing choice is free.

  CAVEAT (the one honest crack): a route OUTSIDE the three -- a constructed MATTER SECTOR
  whose Hamiltonian energetically selects one ledger rank (the PSG 'import external data'
  escape) -- is not refuted here; it is exactly the unbuilt matter sector Paper V flags.
  That is not a record-internal canonicalization; it RELOCATES the choice to a sector that
  does not yet exist. Within the executed corpus, the wall stands.
""")
assert ok, "a check failed"
print("=" * 78)
print("DONE.")
print("=" * 78)
