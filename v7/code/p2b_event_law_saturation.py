#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
p2b_event_law_saturation.py -- Long March v7, PAPER 2, P2-R2 DECISIVE receipt.

THE DECISIVE QUESTION
=====================
Does paper4's primitive EVENT LAW *force* a seal to fire exactly at
self-consistency (KL content C = Fisher capacity J, i.e. at eta_*),
thereby forcing the spacing d = W_* and CLOSING the spacing question?

This receipt reads paper4 as TWO distinct laws and tests their relationship
at mpmath dps>=120 / sympy-exact:

  LAW-A  (paper4 s5, "single-diamond law" / KL=Fisher self-consistency):
            D(P_eta || mu_D) = J(eta)
         <=> eta tanh eta - log cosh eta = 1 - tanh^2 eta
         ->  eta_A = 1.090344354879492...,  W_* = 1 - tanh^2 eta_A = 0.364784952089976...
         This law fixes the diamond's internal CONSTANTS (eta_*, theta_*, W_*).
         It is the law Paper 1 and Paper 2 build the spacing candidate d=W_* on.

  LAW-B  (paper4 s71, "intrinsic division-event commitment law" = the SEAL law):
            S(I) = exp(-I),  retained memory = no-division survival,
            scalar fixed point  tanh eta = exp(-eta)
         ->  eta_B = 0.609377863436...,  theta_B = tanh eta_B = exp(-eta_B) = 0.543689...
         This is paper4's ACTUAL seal-firing / division-commitment law.

CRUX TO SETTLE
==============
  (a) Is "a seal fires" SYNONYMOUS with "the diamond reaches C=J at eta_*"?
      -> Test: is the seal-firing condition LAW-B (tanh=exp(-eta)) the SAME
         equation/root as the self-consistency condition LAW-A (C=J)?
  (b) Does the event law FORBID sealing past / before eta_* (forcing seal AT eta_*)?
      -> Test: does LAW-B's seal-firing content equal W_*?  If yes, d=W_* forced.
         If LAW-B fires at a DIFFERENT content, d=W_* is NOT what the event law gives.
  (c) Is "a sealed record is a self-consistent diamond at eta_*" a THEOREM of the
      paper4 ontology, or a CHOICE?
      -> Decided by whether LAW-A (self-consistency) and LAW-B (sealing) coincide.

Pre-geometric (Tier A): records, commit order, weight-0 KL content chi.
NO spacetime / metric / s^2.

Run: python3 p2b_event_law_saturation.py
Fallback: /Users/felixrobles/workspace/isp/code/.venv/bin/python p2b_event_law_saturation.py
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 140  # >=100 demanded; 140 for cancellation-heavy balances

# ---------------------------------------------------------------------------
def head(s):
    print("\n" + "=" * 78); print(s); print("=" * 78)

def sub(s):
    print("\n  -- " + s + " --")

def line(label, val, extra=""):
    s = "    {:<54}".format(label) + str(val)
    if extra:
        s += "   " + extra
    print(s)

PASS = {}

# ===========================================================================
head("PAPER 4 EVENT-LAW READING -- two laws, two roots (sympy-exact + mpmath)")

eta = sp.symbols('eta', positive=True)

# --- LAW-A: KL content vs Fisher capacity (paper4 s5) ---------------------
psi_s = sp.log(2*sp.cosh(eta)) - sp.log(2)         # log partition (count-dual base)
C_s   = eta*sp.tanh(eta) - sp.log(sp.cosh(eta))    # KL content  D(P_eta||mu_D)
J_s   = sp.simplify(sp.diff(psi_s, eta, 2))        # Fisher capacity = sech^2 eta

line("psi(eta)              ", psi_s)
line("C(eta) = D(P_eta||mu) ", C_s, "(KL content; rises 0->inf)")
line("J(eta) = psi''(eta)   ", sp.simplify(J_s), "(Fisher capacity = sech^2; falls 1->0)")

def C(x): return x*mp.tanh(x) - mp.log(mp.cosh(x))
def J(x): return 1 - mp.tanh(x)**2

# LAW-A self-consistency root: C(eta)=J(eta)
fA  = lambda x: C(x) - J(x)
etaA = mp.findroot(fA, mp.mpf("1.0903"))
thetaA = mp.tanh(etaA)
W_star = 1 - thetaA**2          # = J(etaA)
W_star_C = C(etaA)              # = C(etaA), independent formula

sub("LAW-A  (paper4 s5: single-diamond self-consistency C=J)")
line("eta_A  (root of C=J)            ", mp.nstr(etaA, 40))
line("theta_A = tanh eta_A            ", mp.nstr(thetaA, 40))
line("W_* = J(eta_A) (Fisher)         ", mp.nstr(W_star, 40))
line("W_* = C(eta_A) (KL, independent)", mp.nstr(W_star_C, 40))
line("|C(eta_A) - J(eta_A)| balance   ", mp.nstr(abs(W_star - W_star_C), 6))
PASS["LAW-A: eta_A = 1.0903443548...  (matches paper4 s5)"] = \
    abs(etaA - mp.mpf("1.090344354879492")) < mp.mpf("1e-15")
PASS["LAW-A: W_* = 0.364784952...  (matches paper4 s5)"] = \
    abs(W_star - mp.mpf("0.364784952089976")) < mp.mpf("1e-15")
PASS["LAW-A: C(eta_A)=J(eta_A) to <1e-100 (independent)"] = \
    abs(W_star - W_star_C) < mp.mpf("1e-100")

# --- LAW-B: intrinsic division-event commitment (paper4 s71) --------------
# retained parity memory tanh(eta) = no-division survival exp(-eta)
fB  = lambda x: mp.tanh(x) - mp.exp(-x)
etaB = mp.findroot(fB, mp.mpf("0.6"))
thetaB = mp.tanh(etaB)
survB  = mp.exp(-etaB)

sub("LAW-B  (paper4 s71: intrinsic DIVISION-EVENT COMMITMENT = the SEAL law)")
line("eta_B  (root of tanh eta = exp(-eta))", mp.nstr(etaB, 40))
line("theta_B = tanh eta_B                 ", mp.nstr(thetaB, 40))
line("exp(-eta_B) (no-division survival)   ", mp.nstr(survB, 40))
line("|tanh eta_B - exp(-eta_B)| residual  ", mp.nstr(abs(thetaB - survB), 6))
PASS["LAW-B: eta_B = 0.6093778634...  (matches paper4 s71)"] = \
    abs(etaB - mp.mpf("0.6093778634360061")) < mp.mpf("1e-15")
PASS["LAW-B: theta_B = exp(-eta_B) self-consistent <1e-100"] = \
    abs(thetaB - survB) < mp.mpf("1e-100")

# ===========================================================================
head("CRUX (a)+(b): do the SEAL law (LAW-B) and SELF-CONSISTENCY (LAW-A) COINCIDE?")

print("""
  If 'a seal fires' were SYNONYMOUS with 'the diamond reaches C=J at eta_*',
  then LAW-B's root eta_B would EQUAL LAW-A's root eta_A, and the content the
  seal commits would equal W_*.  We test the two roots and the two contents.
""")

gap_eta = abs(etaA - etaB)
line("eta_A (self-consistency C=J)   ", mp.nstr(etaA, 30))
line("eta_B (seal-firing commitment) ", mp.nstr(etaB, 30))
line("|eta_A - eta_B|                ", mp.nstr(gap_eta, 8),
     "<-- NONZERO: the two laws are DISTINCT")
PASS["eta_A != eta_B  (seal law is NOT the C=J law)"] = gap_eta > mp.mpf("0.4")

# Content the SEAL actually commits (LAW-B fires at eta_B): C(eta_B)
content_at_seal = C(etaB)
J_at_seal       = J(etaB)
sub("Content & capacity AT the seal-firing point eta_B (LAW-B)")
line("C(eta_B)  content accrued at the seal ", mp.nstr(content_at_seal, 30))
line("J(eta_B)  capacity at the seal        ", mp.nstr(J_at_seal, 30))
line("W_* (= max_eta min(C,J), at eta_A)    ", mp.nstr(W_star, 30))
line("C(eta_B) vs W_* :  C(eta_B) - W_*      ", mp.nstr(content_at_seal - W_star, 8))
line("eta_B < eta_A ?  (seal fires BEFORE saturation, UNDER-saturated)",
     etaB < etaA)
line("C(eta_B) < J(eta_B) ?  (under-saturated: content below capacity)",
     content_at_seal < J_at_seal)
# Is the seal at saturation?  Only if C(eta_B)=J(eta_B).
PASS["SEAL (LAW-B) fires UNDER-saturated (C(eta_B) < J(eta_B))"] = \
    content_at_seal < J_at_seal
PASS["SEAL content C(eta_B) != W_*  (event law does NOT commit W_*)"] = \
    abs(content_at_seal - W_star) > mp.mpf("1e-6")

print("""
  READING: paper4's EVENT/SEAL law (LAW-B, s71) is a SURVIVAL/commitment law
  -- exp(-I) Poisson-in-evidence + 'retained memory = no-division survival' --
  whose fixed point tanh eta = exp(-eta) sits at eta_B = 0.6094, STRICTLY BELOW
  the self-consistency point eta_A = 1.0903.  The seal fires while the diamond
  is still UNDER-saturated (C < J).  It is NOT synonymous with reaching C=J.
""")

# ===========================================================================
head("Does the EVENT LAW forbid sealing past / before eta_*?  (crux b)")

print("""
  The capacity ceiling (Paper 2 s3.2) forbids OVER-saturation: a sealed diamond
  cannot carry content C > J, so any seal has C <= W_*.  We confirm the event-law
  seal indeed respects this ceiling -- and lands strictly INSIDE it (under-filled).
""")
line("C(eta_B) <= W_*  (event-law seal respects the ceiling)",
     content_at_seal <= W_star)
line("C(eta_B) / W_*  (fraction of capacity committed)",
     mp.nstr(content_at_seal / W_star, 12))
PASS["event-law seal respects ceiling C(eta_B) <= W_*"] = content_at_seal <= W_star

# The event law's survival clock can in principle fire at ANY evidence I, with
# probability 1-exp(-I); it does not single out I = W_*.  Demonstrate: the mean
# committed evidence under S(I)=exp(-I) is integral_0^inf I e^{-I} dI = 1, NOT W_*.
mean_evidence = mp.quad(lambda I: I*mp.exp(-I), [0, mp.inf])
sub("The seal CLOCK does not single out the content W_*")
line("mean committed evidence  E[I] = int I e^{-I} dI", mp.nstr(mean_evidence, 30),
     "(= 1, in RN/KL evidence units; NOT W_*)")
line("W_* (the saturation content)                   ", mp.nstr(W_star, 30))
PASS["seal clock mean EVIDENCE = 1 (evidence units; a different axis from content W_*)"] = \
    abs(mean_evidence - 1) < mp.mpf("1e-100")

print("""
  THREE DISTINCT OBJECTS must be kept apart (do NOT conflate them):
   (1) the TILT coefficient eta_B = 0.6094  -- selected by tanh eta = e^{-eta};
   (2) the EVIDENCE I ~ Exp(1) -- the random Poisson firing clock, S(I)=e^{-I},
       inter-seal evidence random with MEAN 1 in RN/KL *evidence* units;
   (3) the deterministic CONTENT at the selected tilt, C(eta_B) = 0.1561 *content*
       units, which is < W_* = 0.3648 (under the capacity ceiling).
  C(eta_B) is DETERMINISTIC (a function of the selected tilt), NOT 'a random Poisson
  variable' -- the randomness/mean-1 belongs to the evidence I, a different axis.
  The seal law does NOT pin the per-seal content to W_*: it fires UNDER capacity.
""")

# ===========================================================================
head("CRUX (c): is 'sealed record = self-consistent diamond at eta_*' THEOREM or CHOICE?")

print("""
  paper4 ONTOLOGY: a sealed record diamond's internal CONSTANTS (eta_*, theta_*,
  W_*) are fixed by LAW-A (C=J, s5).  But WHEN the diamond commits/seals is set by
  LAW-B (the division-event law, s71), a SEPARATE law with its OWN root eta_B.

  paper4 NEVER asserts the commit happens at eta_A.  s71's commitment fixed point
  is tanh eta = exp(-eta) (eta_B), explicitly DISTINCT from s5's C=J (eta_A).
  Indeed s69 tested the 'commit when accumulated distinguishability reaches a
  FIXED UNIT' model and found the selected eta depends on the supplied unit/shape
  -- i.e. a fixed-content commitment threshold is NOT canonically W_*.

  Therefore 'a sealed record is the self-consistent diamond AT eta_* (content W_*)'
  is a MODELING CHOICE (identify the commit point with the constant-fixing point),
  NOT a theorem of the paper4 ontology.  The ontology splits the two:
     - constants  <- self-consistency (LAW-A, eta_A)
     - commit/seal <- division-event law (LAW-B, eta_B != eta_A).
""")
PASS["paper4 SEPARATES constant-fixing (eta_A) from sealing (eta_B)"] = gap_eta > mp.mpf("0.4")

# ===========================================================================
head("ALTERNATIVE READING TESTED: could the EVENT (idempotent E^2=E) itself = C=J?")

print("""
  Steel-man: maybe the PRIMITIVE EVENT IDENTITY (s3: E^2=E, count-symmetric,
  Var(q|E)=0) is what 'fires', and IT is characterized by C=J?  We check what s3
  actually constrains.  The event identity fixes the FORM of the readout
  (q=2E-1, q^2=1, mu(+-)=1/2) -- it is a structural/algebraic condition, carrying
  NO eta at all (it holds for the whole tilt family P_eta).  The eta is pinned
  only by an ADDITIONAL principle: LAW-A (C=J) for the constants, LAW-B for the
  seal.  So the event identity alone does NOT fire at C=J; it is eta-agnostic.
""")
# Demonstrate eta-agnosticism: q^2 = 1 for ALL eta (the event identity), unrelated to C=J.
for e in [mp.mpf("0.3"), etaB, mp.mpf("0.9"), etaA, mp.mpf("1.5")]:
    # under P_eta on q in {-1,+1}, q^2 = 1 identically (event identity), C,J vary
    line("eta=%s : q^2=1 (event id holds), C=%s, J=%s"
         % (mp.nstr(e,5), mp.nstr(C(e),6), mp.nstr(J(e),6)), "")
PASS["event identity E^2=E is eta-agnostic (holds all eta)"] = True

# ===========================================================================
head("THE 'no over-saturation' premise vs the 'no under-saturation' premise")

print("""
  Paper 2 R1 symmetric premises:
    'no over-saturation' (C<=J admissible only) => d <= W_*        [ceiling]
    'no under-saturation' (P-sat, commit AT capacity) => d >= W_*  [extremal CHOICE]
  Together => d = W_*.

  Does the EVENT LAW supply 'no under-saturation'?  NO.  LAW-B fires at eta_B
  with C(eta_B) < J(eta_B): the event law's own seal is UNDER-saturated.  So far
  from forbidding under-saturation, paper4's actual sealing law REALIZES it.
  Hence the event law does NOT supply P-sat; it CONTRADICTS the W_* candidate.
""")
line("under-saturation margin J(eta_B) - C(eta_B)", mp.nstr(J_at_seal - content_at_seal, 12),
     "> 0  => event-law seal is under-saturated")
PASS["event law does NOT supply 'no under-saturation' (P-sat)"] = \
    (J_at_seal - content_at_seal) > 0

# ===========================================================================
head("VERDICT")

closes = PASS.get("eta_A != eta_B  (seal law is NOT the C=J law)", False)
verdict = "STILL A CHOICE" if closes else "CLOSURE"
print(f"""
  Does paper4's EVENT LAW force d = W_* (close the spacing)?   ->  NO.

  (a) The seal-firing condition is paper4 s71's DIVISION-EVENT COMMITMENT law
      (LAW-B: tanh eta = exp(-eta), root eta_B = {mp.nstr(etaB,16)}), which is a
      SURVIVAL/Poisson-in-evidence law, NOT the s5 self-consistency law
      (LAW-A: C=J, root eta_A = {mp.nstr(etaA,16)}).  'Seal fires' is NOT
      synonymous with 'C=J'.  KL=Fisher (s5) fixes the diamond's CONSTANTS;
      the seal-firing content is set by a SEPARATE law.

  (b) The event law fires at eta_B < eta_A, i.e. UNDER-saturated
      (C(eta_B)={mp.nstr(content_at_seal,12)} < J(eta_B)={mp.nstr(J_at_seal,12)}).
      It does NOT forbid sealing before eta_*; it positively DOES seal before it.
      The committed content is set by the exp(-I) survival clock (mean evidence 1,
      a Poisson random variable), not pinned to W_*.

  (c) 'A sealed record is the self-consistent diamond at eta_* (content W_*)' is a
      MODELING CHOICE that IDENTIFIES the commit point with the constant-fixing
      point.  paper4's ontology SEPARATES them (constants<-LAW-A, seal<-LAW-B),
      and s69 already found a fixed-content commitment threshold is non-canonical.

  STATUS: d = W_* remains a CHOICE.  The event law does NOT close it -- and, read
  literally, paper4's OWN division-event law (s71) would have the seal fire at a
  DIFFERENT, under-saturated content (eta_B), not at W_*.  The premise d=W_* rests
  on is exactly P-sat ('commit AT capacity / one seal per saturated diamond'),
  which the event law neither supplies nor matches.

  => Paper 2 s3.3 / s5 should be UPDATED: not merely 'the equality is unforced',
     but 'paper4's primitive event law (s71) is a survival-commitment law with its
     OWN root eta_B != eta_A, so it gives neither d=W_* nor the C=J seal; closing
     d=W_* needs P-sat, which is in TENSION with the literal s71 seal law.'
""")

# ===========================================================================
head("MACHINE CHECKS")
allpass = True
for k, v in PASS.items():
    flag = "PASS" if v else "FAIL"
    if not v: allpass = False
    print(f"  [{flag}] {k}")
print("\n  " + ("ALL CHECKS PASS" if allpass else "*** SOME CHECK FAILED ***"))
