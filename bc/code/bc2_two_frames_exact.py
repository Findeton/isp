#!/usr/bin/env python3
"""
bc2_two_frames_exact.py — BC2: THE BELL-TWO-FRAMES PROBE.
Is the composite's slice-indexed joint across spacelike separation
frame-relative?

Pin: bc/note-bc2-bell-two-frames-pin.md (STRICT, frozen before this file
existed).  Program: bc/LOG.md #1 (the Barandes consistency program, from
scratch, NO record substrate).  Committed instruments reused and anchored:
v11/code/u3_unistochasticity_screen_exact.py (the unistochasticity screen
and its known-answer battery, extracted by AST, never retyped) and
v11/note-L1-lorentz-no-go-lemma.md (the finite-stochastic Lorentz no-go,
quoted verbatim, its ladder consumed).  BC1's pin is CITED for the
system-centric composition question and is NOT duplicated here.

WHAT IS BUILT
  One Bell model, exactly, in [B3]'s own kinematics: a fixed finite
  configuration space (2 x 2 x 3 x 3 = 36 configurations: two spin-1/2
  wings and two three-state pointers), an initial division event at which
  the configuration is definite, a preparation unitary that makes the
  singlet, and two commuting measurement unitaries.  The SAME physical
  experiment is then written as a [B3] indivisible stochastic process in
  BOTH frame orderings,
      F1 = (prep, A, B)      F2 = (prep, B, A),
  every transition matrix from [B3]'s dictionary Gamma_ij = |Theta_ij|^2
  (eq. 25), exact in the real quartic field Q(cos(pi/8)).

WHAT IS TESTED
  (i)   THE LAW-OF-TOTAL-PROBABILITY GATE at every declared division
        event ([B3] eqs. 19-20): p(t) = Gamma(t <- t_0) p(t_0) for every
        declared t_0 and every later target time t.  A declared division
        event at which this fails is not a division event on [B3]'s own
        axioms, so the gate decides which instances the division-event
        census may run on.
  (ii)  THE SPECIFIED-CONTENT INVENTORY, printed completely per frame at
        all six setting pairs: division events, configuration space,
        transition matrices, every single-time marginal, every
        division-event joint -- and the explicit list of what [B3]
        REFUSES to specify (the Kolmogorov tower, the non-Markovian
        realizer, trajectory joints).
  (iii) THE QM-STATISTICS GATE (a CONTROL, exit 1 on failure): both frames
        reproduce the exact singlet correlations at every declared setting
        pair.
  (iv)  THE TEST: the candidate frame map, and whether it carries F1's
        specified content onto F2's.  L-1 forces the map's form; the
        search over the forced class is COMPLETE (refinement +
        backtracking, exact), so a negative is a proof of non-existence,
        not a failure to find.
  (v)   The covariance-class verdict on L-1's ladder.
  (vi)  The escape-hatch battery, each escape working-at-a-stated-cost or
        failing-at-a-stated-place -- E2 run with ALL target times kept,
        because denying a division event removes the conditioning at that
        time and not the target times ([B3] p.10, p.29).
  (vii) THE POINTER-FREE REPLICATION: the same two-frame comparison on a
        4-configuration model with NO pointers, in which measurement is a
        basis rotation that makes the measured observable a beable
        ([B3] p.24), searched by brute force over all 24 permutations.

ENGRAVED SCOPE CONSTRAINTS (pin, carried into every gate text)
  * The finding is about [B3]'s FORMAL APPARATUS, not about relativity in
    nature.  No claim about nature is made anywhere.
  * WHAT IS CLAIMED IS SLICE-INDEXED.  The object shown to be
    frame-relative is the COMPOSITE'S JOINT AT THE INTERMEDIATE SLICE.
    The final-time composite content is frame-invariant and carries the
    whole outcome joint.  [B3] contains no relativity content, so "the
    ontology requires a foliation" is NOT the claim; "no relabelling of
    C carries F1's slice-indexed joint onto F2's" is.
  * NO Bell-INEQUALITY claim and NO locality claim.  This unit is a
    covariance-of-description question only.  The corpus's committed Bell
    verdict is not touched, cited, or used.
  * No records, no generated carrier, no gravity.
  * Lean: NONE.  R-COVARIANT, R-FOLIATED and R-CONDITIONAL are all
    reportable and the census is the result.

HOUSE RULES OBSERVED
  * Exact algebraic arithmetic end to end: fractions.Fraction for every
    rational, and class K = Q[x]/(8x^4 - 8x^2 + 1) = Q(cos(pi/8)) for
    every unitary and every probability.  No float appears in any
    substantive computation and no tolerance is used anywhere.
  * The reused instrument is single-sourced by AST extraction with a
    signature pass; its known-answer battery is re-run and checked
    against the committed note's printed values.
  * exit 1 is reserved for ANCHOR failure and for the QM control.
    Substantive negatives exit 0.
  * Determinism: every census is ordered by a hash-seed-independent key.
"""

from __future__ import annotations

import ast
import os
import sys
import time
from collections import Counter
from fractions import Fraction as Fr
from itertools import product

T0 = time.time()
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(REPO)
sys.setrecursionlimit(100000)

PASS = FAIL = 0
ANCHOR_FAIL = 0
CONTROL_FAIL = 0
SECT = [0]
_LAST = [time.time()]


def sec(title):
    SECT[0] += 1
    print()
    print("=" * 78)
    print(f"SEC {SECT[0]}  {title}   [+{time.time() - T0:.0f}s]")
    print("=" * 78)
    sys.stdout.flush()


def tick(msg=""):
    """Progress print; the pin forbids a silent interval > 8 min."""
    now = time.time()
    print(f"    ... [+{now - T0:.0f}s, d{now - _LAST[0]:.0f}s] {msg}")
    _LAST[0] = now
    sys.stdout.flush()


def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS += int(bool(ok))
    FAIL += int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))
    sys.stdout.flush()
    return bool(ok)


def anchor(label, ok, detail=""):
    global ANCHOR_FAIL
    if not check("ANCHOR " + label, ok, detail):
        ANCHOR_FAIL += 1
    return bool(ok)


def control(label, ok, detail=""):
    global CONTROL_FAIL
    if not check("CONTROL " + label, ok, detail):
        CONTROL_FAIL += 1
    return bool(ok)


def report(label, value):
    print(f"  [DATA] {label}: {value}")
    sys.stdout.flush()


def sk(o):
    if isinstance(o, (frozenset, set)):
        return ("S", tuple(sorted(sk(x) for x in o)))
    if isinstance(o, (tuple, list)):
        return ("T", tuple(sk(x) for x in o))
    return ("V", type(o).__name__ + "|" + repr(o))


def fmt(counter):
    return {str(k): v for k, v in sorted(counter.items(),
                                         key=lambda z: sk(z[0]))}


print("=" * 78)
print("bc2_two_frames_exact.py — BC2: THE BELL-TWO-FRAMES PROBE")
print("Does [B3]'s conditioning structure need a foliation?")
print("=" * 78)
print("  banner: EXACT arithmetic end to end, NO TOLERANCE ANYWHERE.")
print("          Rationals: fractions.Fraction.  Algebraic: class K =")
print("          Q[x]/(8x^4 - 8x^2 + 1) = Q(cos(pi/8)), a real quartic")
print("          field, with an exact zero test and an exact sign oracle.")
print("  scope : [B3]'s FORMAL APPARATUS.  No claim about relativity in")
print("          nature.  NO Bell-inequality claim, NO locality claim —")
print("          this is a covariance-of-DESCRIPTION question only.")
print("  lean  : NONE.")
sys.stdout.flush()


# ===========================================================================
# SEC 0.  THE REGISTRY
# ===========================================================================

sec("THE REGISTRY — every source a gate tests against, quoted and cited")

QUOTES = {
    "B3-div": (
        "[B3] Barandes, 'Quantum Systems as Indivisible Stochastic "
        "Processes', arXiv:2507.21192 (30 July 2025), p.9 (the paragraph "
        "introducing eq. 18-21) and p.10 (top); PDF read in-session",
        "Note that no assumption is made here that the transition "
        "probabilities p(i,t|j,t') exist as part of the laws for all "
        "real-valued choices of t'.  Allowed conditioning times t' are "
        "called DIVISION EVENTS for the given system, and, without any "
        "real loss of generality, are assumed to include an 'initial' "
        "time 0.  ... Division events are not global properties of the "
        "whole universe, but are system-centric, just like various other "
        "kinds of spontaneous time-translation-breaking in physics.",
    ),
    "B3-ltp": (
        "[B3] p.9, eqs. (19)-(20) and the sentence attached to them; PDF "
        "read in-session",
        "The only available Chapman-Kolmogorov equations (5) take the "
        "simple form  p(i,t) = sum_j p(i,t | j,t_0) p(j,t_0),  (19)  "
        "which is just the LAW OF TOTAL PROBABILITY.  Equivalently, in "
        "matrix notation,  p(t) = Gamma(t <- t_0) p(t_0).  (20)  ... "
        "Importantly, notice that the law of total probability (19) is "
        "LINEAR, in the sense that it establishes a linear relationship "
        "between the system's standalone probabilities at t_0 and the "
        "system's standalone probabilities at t.",
    ),
    "B3-target": (
        "[B3] p.10, the paragraph after the system-centricity sentence",
        "The target time t, by contrast, can be treated as a FREE "
        "VARIABLE.  In particular, no assumption is made that t > t'.  "
        "One can choose t < t' as well.  An indivisible stochastic "
        "process does not, therefore, need to violate logical "
        "time-reversal invariance in any fundamental way.",
    ),
    "B3-colstoch": (
        "[B3] p.8, eq. (9) (the normalisation of the transition matrix)",
        "each column sums to 1, meaning that Gamma(t <- t') is a "
        "(COLUMN) STOCHASTIC MATRIX:  Gamma_ij(t <- t') >= 0, "
        "sum_i Gamma_ij(t <- t') = 1.  (9)",
    ),
    "B3-eq22": (
        "[B3] p.10, eqs. (22)-(23) and the paragraph following them",
        "it might seem reasonable to try to define an intermediate "
        "transition matrix ~Gamma(t<-t') from t' to t according to "
        "~Gamma(t<-t') = Gamma(t<-0) Gamma^{-1}(t'<-0), (22), AT LEAST IF "
        "Gamma(t'<-0) IS INVERTIBLE. ... However, it turns out that a "
        "matrix ~Gamma(t<-t') defined according to (22) will generically "
        "fail to be a column stochastic matrix, and, indeed, will "
        "typically have negative entries, and so will form a so-called "
        "PSEUDO-STOCHASTIC matrix.  The reason is that the inverse of a "
        "stochastic matrix can only itself be a stochastic matrix if both "
        "matrices are PERMUTATION MATRICES.",
    ),
    "B3-fn7": (
        "[B3] p.10, footnote 7 (the proof attached to the sentence "
        "quoted at [B3-eq22])",
        "Proof: Let X and Y be N x N matrices with only non-negative "
        "entries and with Y = X^{-1}, so that XY = 1. ... one sees that X "
        "can only have a single nonzero entry in each row.  If X is a "
        "stochastic matrix, then each of these nonzero entries must be "
        "the number 1, so X must be a permutation matrix.  Because the "
        "inverse of a permutation matrix is again a permutation matrix, "
        "it follows that Y must likewise be a permutation matrix.  QED",
    ),
    "B3-refusal": (
        "[B3] p.10 (bottom) and p.11 (top)",
        "Given just the minimalist ingredients that define a given "
        "indivisible stochastic process, there will generically exist a "
        "large or infinite number of ways of choosing a complete "
        "Kolmogorov tower (3) consistent with those ingredients.  Each "
        "such choice of Kolmogorov tower is called a NON-MARKOVIAN "
        "REALIZER. ... the specific non-Markovian realizer is potentially "
        "unknowable, and perhaps meaningless.",
    ),
    "B3-dict": (
        "[B3] p.11, eqs. (24)-(26), and p.14, eqs. (41)-(42), (46)",
        "Gamma_ij(t<-0) = p(i,t|j,0) (24); Gamma_ij(t<-0) = "
        "|Theta_ij(t<-0)|^2 (25); sum_i |Theta_ij(t<-0)|^2 = 1 (26); "
        "rho(0) = diag(..., p_j(0), ...) = sum_j p_j(0) P_j (41); "
        "rho(t) = Theta(t<-0) rho(0) Theta^dagger(t<-0) (42); "
        "p_i(t) = tr(P_i rho(t)) (46).",
    ),
    "B3-axioms": (
        "[B3] p.29 (Section 5, the three axioms of indivisible quantum "
        "theory)",
        "Kinematical axiom: ... The configuration space is a FIXED "
        "feature of the model, meaning that it does not vary between "
        "real-world runs or instantiations of the model.  Dynamical "
        "axiom: For arbitrary target times, and for conditioning times "
        "corresponding to division events, the model's dynamical laws "
        "consist of transition probabilities ... Division events may "
        "occur naturally within the model's own dynamics, and can also be "
        "generated spontaneously through interactions with other systems. "
        " For example, DIVISION EVENTS ARE GENERATED DURING A MEASUREMENT "
        "PROCESS, which can be modeled as just another stochastic "
        "process.  At the level of the given model, the dynamical laws "
        "are fixed features.  Epistemic axiom: The system has some "
        "time-dependent standalone probability distribution to be in a "
        "particular configuration at any given target time. ... and is "
        "CONTINGENT, meaning that it can vary between runs of the model.",
    ),
    "B3-outcomes": (
        "[B3] p.16 (the emergeables paragraph) and p.24 (the Wigner-"
        "symmetry paragraph).  The second page cite is p.24, not p.26",
        "When a measuring device is properly modeled as one additional "
        "part of a larger stochastic process ... at the end of the "
        "measurement process, the measuring device will end up in one of "
        "its possible MEASUREMENT-OUTCOME CONFIGURATIONS with a "
        "stochastic probability that coincides with the standard Born "
        "rule, WHETHER THE MEASURING DEVICE HAS BEEN TUNED TO MEASURE A "
        "BEABLE OR AN EMERGEABLE. [p.16]  ... if one suitably models an "
        "entire system that includes a measuring device as an overall "
        "unistochastic process, then the measuring device will end up in "
        "one of its possible measurement-outcome configurations with the "
        "appropriate Born-rule probability for whatever observable is "
        "measured -- whether a BEABLE (represented by a self-adjoint "
        "matrix that is DIAGONAL IN THE CONFIGURATION BASIS) or an "
        "EMERGEABLE (represented by a non-diagonal self-adjoint "
        "matrix). [p.24]",
    ),
    "B3-uni": (
        "[B3] p.18, the paragraph following eq. (64), and p.19",
        "In general, an N x N matrix is called UNISTOCHASTIC if its "
        "individual entries are expressible as the modulus-squares of the "
        "corresponding entries of an N x N unitary matrix. ... an "
        "indivisible stochastic process can be viewed either as a "
        "unistochastic process itself, or (if a nontrivial dilation was "
        "required) as a SUBSYSTEM of a unistochastic process.",
    ),
    "B3-future": (
        "[B3] p.29 (Section 5, Discussion and Future Work)",
        "Any mention of hidden variables may immediately bring to mind a "
        "number of no-go theorems about non-locality, including the "
        "various versions of Bell's theorem. ... THESE THEOREMS WILL BE "
        "ADDRESSED IN DETAIL IN FUTURE WORK. ... that other work will "
        "also argue that locality in space is preserved at the cost of "
        "non-Markovianity.  One can view non-Markovianity roughly as a "
        "form of non-locality in time that is consistent with the "
        "light-cone structure of special relativity.",
    ),
    "L1a": (
        "v11/note-L1-lorentz-no-go-lemma.md:86-94 (L-1 (a)), restating "
        "v3/relativistic-isp-v3-paper8-continuum-qft-reconstruction-"
        "no-go.md:110-114 (Lemma 2.3) and :132-137 (Corollary 2.4)",
        "L-1 (a) — the imported half, re-derived at v11's grain.  Let C "
        "be finite.  Let G be a group and g |-> R_g an exact covariance "
        "action on C by stochastic maps: each R_g is row-stochastic on C, "
        "R_e = I, and R_g R_h = R_{gh}.  Then every R_g is a permutation "
        "matrix of C.",
    ),
    "L1b": (
        "v11/note-L1-lorentz-no-go-lemma.md:107-114 (L-1 (b))",
        "L-1 (b) — the boost step.  If G contains a one-parameter boost "
        "subgroup isomorphic to (R,+), the restriction of R to that "
        "subgroup is trivial: R_b = I for every boost b.  Proof.  By (a) "
        "the image lies in Sym(C), a finite group.  (R,+) is divisible, "
        "so its homomorphic image is a divisible subgroup of a finite "
        "group, hence trivial.",
    ),
    "L1-admissible": (
        "v11/note-L1-lorentz-no-go-lemma.md:30-40, importing "
        "v3 paper 8:139-147 verbatim",
        "The only admissible finite covariance statements in this paper "
        "are: 1. equality or convergence of declared finite-battery "
        "statistics for sampled Lorentz-related tests; 2. projective "
        "compatibility of different finite batteries approximating "
        "Lorentz-related continuum tests; 3. an imported continuum "
        "covariance representation listed as enrichment.  None of these "
        "is a finite-regulator proof of full Lorentz covariance.",
    ),
    "L1-ladder": (
        "v11/note-L1-lorentz-no-go-lemma.md:217-273 (the ladder) and "
        ":345-346 (constraint C4)",
        "1. Exact stochastic covariance — EXCLUDED by L-1.  Grade: "
        "[THEOREM] at the source, re-derived here.  2. Sprinkling-grade "
        "statistical covariance on a finite-valency generated carrier — "
        "grade [MY READING] ... undecided.  3. Order-level covariance "
        "(P-Lor) — untested on a generated carrier. ... C4.  Any "
        "covariance claim states, separately, (i) what acts, (ii) on what "
        "set, (iii) whether the acting maps are invertible.",
    ),
    "L1-scope": (
        "v11/note-L1-lorentz-no-go-lemma.md:286-298 (scope guard)",
        "It does NOT forbid a permutation action. ... It does NOT forbid "
        "covariance implemented by NON-INVERTIBLE stochastic maps — but "
        "the loophole is narrower than it reads: inside a GROUP action "
        "L-1(a) DERIVES invertibility, so what actually escapes is a "
        "covariance carried by a semigroup or by a non-group action.",
    ),
    "u3-ka": (
        "v11/note-u3-unistochasticity-screen.md:141-151 (the known-answer "
        "controls table); receipt "
        "v11/code/u3_unistochasticity_screen_exact.py:1251-1347",
        "KA-1 flat J/3: UNISTOCHASTIC, T = +1/27, 0 polygon violations.  "
        "KA-2 B = (1/2)(J - I): BISTOCHASTIC, NOT UNISTOCHASTIC; DS "
        "holds; T = -1/16; the polygon fires — moduli (0, 0, 1/2) and "
        "1/2 > 0 + 0.  KA-4 n = 2: orthostochastic, 0 residuals, 0 "
        "mismatches.  KA-5 a row-stochastic non-DS matrix: caught by the "
        "precondition.  KA-6 Sylvester H_8: H H^T = 8I exact over Z.",
    ),
    "u3-positive": (
        "v11/code/u3_unistochasticity_screen_exact.py:1244-1248 (the "
        "receipt's own discipline for positive verdicts)",
        "POSITIVE direction.  This receipt NEVER returns 'unistochastic' "
        "on the strength of T >= 0.  Every positive verdict below "
        "EXHIBITS a unitary of the same size and verifies U^dagger U = I "
        "and |U_ij|^2 = Gamma_ij entry by entry in exact algebraic "
        "arithmetic.",
    ),
    "bc1-pin": (
        "bc/note-bc1-division-event-composition-pin.md (CITED, NOT "
        "duplicated — BC1 owns the subsystem-lattice question)",
        "[B3] p.10 makes division events SYSTEM-CENTRIC: a division event "
        "for a composite system need not be a division event for its "
        "subsystems, and vice versa.  Is that assignment internally "
        "consistent across the subsystem lattice — and does it have the "
        "structure of a marginal problem with obstructions?",
    ),
}

for _k in sorted(QUOTES):
    print(f"  [{_k}] {QUOTES[_k][0]}")

# ---- a DECLARED MEASUREMENT of the source text, not computed here -------
REL_CONTENT = {
    "method": "full-text extraction of the [B3] PDF (arXiv:2507.21192, "
              "35 pages), case-insensitive substring counts over the "
              "extracted body; performed outside this receipt and "
              "declared here",
    "Lorentz": 0, "spacelike": 0, "space-like": 0, "foliation": 0,
    "foliate": 0, "boost": 0, "Minkowski": 0,
    "relativistic": "5 — four as 'non-relativistic', one in a "
                    "bibliography title",
    "reference frames": "1 — a footnote citing a study of the "
                        "Schroedinger equation between inertial and "
                        "non-inertial reference frames",
    "light-cone": "1 — the p.29 sentence already quoted at [B3-future]",
}
print()
print("  [B3-relativity-content] DECLARED MEASUREMENT, NOT COMPUTED IN "
      "THIS RECEIPT (no PDF is read at runtime).  [B3] contains NO "
      "relativity content in the sense that matters to a covariance "
      "claim:")
for _k, _v in REL_CONTENT.items():
    print(f"      {_k:20s} : {_v}")
print("  Consequence, carried into every verdict text below: this unit "
      "tests a\n  covariance question [B3] does not pose.  The finding is "
      "stated as a\n  property of the model's SLICE-INDEXED content under "
      "the declared frame\n  change, never as '[B3] requires a "
      "foliation'.")

ANCH = {
    # u3's committed known-answer values (v11/note-u3-...:141-151)
    "ka1_T": Fr(1, 27),
    "ka1_poly": 0,
    "ka2_T": Fr(-1, 16),
    "ka2_moduli": [Fr(0), Fr(0), Fr(1, 2)],
    "ka2_sqmoduli": [Fr(0), Fr(0), Fr(1, 4)],
    "ka4_resid": 0,
    "ka6_gram": 8,
    # the exact singlet statistics this model must reproduce (QM control)
    "singlet_marginal": Fr(1, 2),
}
print(f"  ANCHOR constants: {len(ANCH)} entries, all quoted above.")

CAPS = {
    "the model": "ONE Bell model: 2 spin-1/2 wings x 2 three-state "
                 "pointers = 36 configurations, fixed across both frames "
                 "and across every setting pair",
    "setting pairs": "SIX, declared: (0,45), (0,135), (90,45), (90,135), "
                     "(0,0), (45,45) degrees.  All measurement directions "
                     "are coplanar, so every transition-matrix entry lies "
                     "in Q(sqrt2) and every time-evolution operator entry "
                     "in Q(cos(pi/8))",
    "frames": "TWO orderings only: F1 = (prep, A, B) and F2 = (prep, B, "
              "A).  No continuum of boosts is built; L-1(b) supplies the "
              "continuum statement and is quoted, not re-derived",
    "target times": "FOUR per frame: 0 (initial division event), 1 (after "
                    "preparation), 2 (after the first measurement), 3 "
                    "(after the second).  The model is piecewise-constant "
                    "between these, so the four carry the whole content",
    "division events": "THREE per frame: {0, 2, 3}.  t = 1 is a target "
                       "time that is NOT a division event, so the "
                       "'drop the intermediate marginals' escape has "
                       "something to drop",
    "the frame-map search": "COMPLETE over the class L-1 forces "
                            "(permutations of the 36 configurations): "
                            "colour refinement plus backtracking, exact, "
                            "with the node cap printed.  A negative is a "
                            "proof of non-existence",
    "retrodictive matrices": "NOT computed.  [B3] p.10 allows t < t'; "
                             "for t' a division event with p(.,t') > 0 "
                             "those matrices are Bayes-determined by the "
                             "forward matrices and the marginals already "
                             "in the inventory, so they add no content "
                             "the comparison could separate",
    "the pointer-free replication": "ONE second model, 4 configurations "
                                    "(the outcome pairs), measurement = "
                                    "the basis rotation that makes the "
                                    "measured observable a beable "
                                    "([B3] p.24); the SAME six setting "
                                    "pairs, the SAME four grains, the "
                                    "SAME two correspondences; searched "
                                    "by BRUTE FORCE over all 4! = 24 "
                                    "permutations, so no search "
                                    "machinery is load-bearing there",
    "NOT implemented": "no LP/Farkas search over non-group covariance "
                       "semigroups.  L-1(a) derives invertibility inside "
                       "a GROUP action and the two-frame map is a group "
                       "(Z/2 at least), so the permutation class is "
                       "complete for the covariance question posed; the "
                       "semigroup loophole is named in the verdict and "
                       "left OPEN",
    "sign-oracle refinement cap": "8192 bisection steps (the maximum "
                                  "actually used is printed)",
}
report("caps", "; ".join(f"{k}: {v}" for k, v in CAPS.items()))


# ===========================================================================
# SEC 1.  EXACT ALGEBRAIC ARITHMETIC — K = Q[x]/(8x^4 - 8x^2 + 1)
# ===========================================================================

sec("EXACT ALGEBRAIC ARITHMETIC — the field this receipt computes in")

print("""
  Every number below is an element of

     K = Q[x]/(m),   m(x) = 8x^4 - 8x^2 + 1,   x |-> c = cos(pi/8),

  the real quartic field Q(cos(pi/8)).  m is the minimal polynomial of
  cos(22.5 deg) because cos(4t) = 8cos^4 t - 8cos^2 t + 1 and cos(90 deg)
  = 0; its irreducibility over Q is CERTIFIED in-receipt below, and that
  certificate is what makes 'all four coefficients zero' a sound zero
  test.  Reduction is by x^4 = x^2 - 1/8.  The field contains

     sqrt2 = 4c^2 - 2,   cos(22.5) = c,   sin(22.5) = 4c^3 - 3c,
     cos(45) = sin(45) = 2c^2 - 1,        cos(67.5) = 4c^3 - 3c,
     sin(67.5) = c,

  so every half-angle amplitude for a coplanar setting that is a multiple
  of 45 degrees is an EXACT element, not an approximation.  Signs are
  decided by exact rational interval refinement around c, which
  terminates because a nonzero element of a number field is bounded away
  from zero.  There is no tolerance anywhere in this file.
""")

_RED = {4: {2: Fr(1), 0: Fr(-1, 8)},
        3: {3: Fr(1)},
        5: {3: Fr(1), 1: Fr(-1, 8)},
        6: {2: Fr(7, 8), 0: Fr(-1, 8)}}


class K:
    """a0 + a1 c + a2 c^2 + a3 c^3 with c = cos(pi/8), ai in Q."""

    __slots__ = ("a",)

    def __init__(self, a0=0, a1=0, a2=0, a3=0):
        self.a = (Fr(a0), Fr(a1), Fr(a2), Fr(a3))

    @staticmethod
    def _mk(t):
        z = K.__new__(K)
        z.a = t
        return z

    def __add__(self, o):
        o = tok(o)
        return K._mk(tuple(x + y for x, y in zip(self.a, o.a)))

    __radd__ = __add__

    def __neg__(self):
        return K._mk(tuple(-x for x in self.a))

    def __sub__(self, o):
        return self + (-tok(o))

    def __rsub__(self, o):
        return tok(o) + (-self)

    def __mul__(self, o):
        o = tok(o)
        A, B = self.a, o.a
        raw = [Fr(0)] * 7
        for i in range(4):
            if A[i] == 0:
                continue
            ai = A[i]
            for j in range(4):
                if B[j]:
                    raw[i + j] += ai * B[j]
        out = [raw[0], raw[1], raw[2], raw[3]]
        for d in (4, 5, 6):
            if raw[d]:
                for e, cf in _RED[d].items():
                    out[e] += raw[d] * cf
        return K._mk(tuple(out))

    __rmul__ = __mul__

    def is_zero(self):
        return all(x == 0 for x in self.a)

    def is_rat(self):
        return self.a[1] == 0 and self.a[2] == 0 and self.a[3] == 0

    def in_qsqrt2(self):
        """True iff the element lies in Q(sqrt2) = Q(2c^2-1)."""
        return self.a[1] == 0 and self.a[3] == 0

    def qsqrt2(self):
        """(p, q) with self = p + q sqrt2, valid when in_qsqrt2()."""
        return (self.a[0] + self.a[2] / 2, self.a[2] / 4)

    def __eq__(self, o):
        return (self - tok(o)).is_zero()

    def __ne__(self, o):
        return not self.__eq__(o)

    def __hash__(self):
        return hash(self.a)

    def key(self):
        return tuple((x.numerator, x.denominator) for x in self.a)

    def __lt__(self, o):
        return ksign(self - tok(o)) < 0

    def __gt__(self, o):
        return ksign(self - tok(o)) > 0

    def __le__(self, o):
        return ksign(self - tok(o)) <= 0

    def __ge__(self, o):
        return ksign(self - tok(o)) >= 0

    def __abs__(self):
        return self if ksign(self) >= 0 else -self

    def inv(self):
        """Exact inverse via the 4x4 rational multiplication matrix."""
        cols = []
        for e in range(4):
            b = K._mk(tuple(Fr(1) if i == e else Fr(0) for i in range(4)))
            cols.append((self * b).a)
        M = [[cols[e][r] for e in range(4)] for r in range(4)]
        rhs = [Fr(1), Fr(0), Fr(0), Fr(0)]
        n = 4
        for col in range(n):
            piv = None
            for r in range(col, n):
                if M[r][col] != 0:
                    piv = r
                    break
            if piv is None:
                raise ZeroDivisionError("K.inv of a non-invertible element")
            M[col], M[piv] = M[piv], M[col]
            rhs[col], rhs[piv] = rhs[piv], rhs[col]
            pv = M[col][col]
            M[col] = [x / pv for x in M[col]]
            rhs[col] = rhs[col] / pv
            for r in range(n):
                if r != col and M[r][col] != 0:
                    f = M[r][col]
                    M[r] = [x - f * y for x, y in zip(M[r], M[col])]
                    rhs[r] -= f * rhs[col]
        return K._mk(tuple(rhs))

    def __truediv__(self, o):
        return self * tok(o).inv()

    def __repr__(self):
        if self.is_rat():
            return str(self.a[0])
        if self.in_qsqrt2():
            p, q = self.qsqrt2()
            if p == 0:
                return f"({q})r2"
            return f"{p}{'+' if q > 0 else '-'}({abs(q)})r2"
        nm = ["", "c", "c2", "c3"]
        return "+".join(f"{x}{nm[i]}" for i, x in enumerate(self.a) if x)


def tok(o):
    if isinstance(o, K):
        return o
    return K(o)


K0 = K(0)
K1 = K(1)
KC = K(0, 1)


def _mpoly(x):
    return 8 * x ** 4 - 8 * x ** 2 + 1


SIGN_STEPS = [0]
_CLO = [Fr(9, 10)]
_CHI = [Fr(95, 100)]


def _refine_c(steps):
    lo, hi = _CLO[0], _CHI[0]
    for _ in range(steps):
        mid = (lo + hi) / 2
        if _mpoly(mid) < 0:
            lo = mid
        else:
            hi = mid
    _CLO[0], _CHI[0] = lo, hi


_refine_c(120)


def ksign(z):
    """Exact sign of a K element."""
    if z.is_zero():
        return 0
    a = z.a
    if a[1] == 0 and a[2] == 0 and a[3] == 0:
        return 1 if a[0] > 0 else -1
    if a[1] == 0 and a[3] == 0:
        p, q = a[0] + a[2] / 2, a[2] / 4              # p + q sqrt2
        if q == 0:
            return 1 if p > 0 else -1
        if p == 0:
            return 1 if q > 0 else -1
        if p > 0 and q > 0:
            return 1
        if p < 0 and q < 0:
            return -1
        d = p * p - 2 * q * q                          # sign of p+q r2
        if d == 0:
            return 0
        return (1 if p > 0 else -1) if d > 0 else (1 if q > 0 else -1)
    extra = 0
    while True:
        lo, hi = _CLO[0], _CHI[0]
        blo = bhi = Fr(0)
        ok = True
        for i, co in enumerate(a):
            if co == 0:
                continue
            plo, phi = lo ** i, hi ** i
            if co > 0:
                blo += co * plo
                bhi += co * phi
            else:
                blo += co * phi
                bhi += co * plo
        if blo > 0:
            return 1
        if bhi < 0:
            return -1
        if not ok:
            pass
        extra += 40
        SIGN_STEPS[0] = max(SIGN_STEPS[0], 120 + extra)
        if 120 + extra > 8192:
            raise RuntimeError("sign oracle exceeded the printed cap")
        _refine_c(40)


# --- the irreducibility certificate, computed, not cited -----------------
_rr = [Fr(s * p, q) for s in (1, -1) for p in (1,) for q in (1, 2, 4, 8)]
_no_rat_root = all(_mpoly(r) != 0 for r in _rr)


def _is_rat_square(r):
    if r < 0:
        return False
    n, d = r.numerator, r.denominator
    import math as _m
    return _m.isqrt(n) ** 2 == n and _m.isqrt(d) ** 2 == d


# case a = 0: b + d = -1, b d = 1/8  ->  8t^2 + 8t + 1 = 0, rational roots?
_c1 = [Fr(s * p, q) for s in (1, -1) for p in (1,) for q in (1, 2, 4, 8)]
_case_a0 = all(8 * t ** 2 + 8 * t + 1 != 0 for t in _c1)
# case d = b: b^2 = 1/8 -> 1/8 a rational square?
_case_db = not _is_rat_square(Fr(1, 8))
check("K1.1 THE FIELD IS A FIELD: m(x) = 8x^4 - 8x^2 + 1 IS IRREDUCIBLE "
      "OVER Q, CERTIFIED IN-RECEIPT.  (i) no rational root — all eight "
      "rational-root-theorem candidates +-1, +-1/2, +-1/4, +-1/8 "
      "evaluated exactly and none vanishes; (ii) no factorisation into "
      "two rational quadratics — writing m = 8(x^2+ax+b)(x^2+cx+d) forces "
      "c = -a and a(d-b) = 0, and both branches die: a = 0 needs "
      "8t^2+8t+1 to have a rational root (it has none) and d = b needs "
      "1/8 to be a rational square (it is not).  Hence 'all four "
      "coefficients zero' is a sound zero test",
      _no_rat_root and _case_a0 and _case_db,
      f"rational-root candidates {len(_rr)}, none a root: {_no_rat_root}; "
      f"branch a=0 dead: {_case_a0}; branch d=b dead: {_case_db}")

SQRT2 = K(-2, 0, 4, 0)
C22, S22 = K(0, 1, 0, 0), K(0, -3, 0, 4)
C45 = K(-1, 0, 2, 0)
C67, S67 = K(0, -3, 0, 4), K(0, 1, 0, 0)
check("K1.2 THE HALF-ANGLE AMPLITUDES ARE EXACT ELEMENTS AND SATISFY "
      "THEIR PYTHAGOREAN IDENTITIES IDENTICALLY: sqrt2^2 = 2; "
      "c^2 + s^2 = 1 at 22.5, 45 and 67.5 degrees; and the two "
      "cross-identities sin(22.5) = (sqrt2 - 1)cos(22.5) and "
      "2 cos(22.5) sin(22.5) = sin(45) hold with zero residual",
      (SQRT2 * SQRT2 - K(2)).is_zero()
      and (C22 * C22 + S22 * S22 - K1).is_zero()
      and (C45 * C45 + C45 * C45 - K1).is_zero()
      and (C67 * C67 + S67 * S67 - K1).is_zero()
      and (S22 - (SQRT2 - K1) * C22).is_zero()
      and (K(2) * C22 * S22 - C45).is_zero(),
      f"sqrt2 = {SQRT2}; c22 = {C22}; s22 = {S22}; c45 = {C45}")

_t1 = SQRT2 - K(3, 0, 0, 0)          # sqrt2 - 3 < 0
_t2 = K(4) * C22 - K(3)              # 4cos(22.5) - 3 > 0  (3.6955... > 3)
_t3 = C22 - K(0, 0, 0, 1) - K(1, -1) # c - c^3 - 1 + c  (sign by oracle)
check("K1.3 THE SIGN ORACLE IS EXACT ON KNOWN-ANSWER ELEMENTS THAT NO "
      "TOLERANCE SETTLES: sign(sqrt2 - 3) = -1 (1.4142... < 3); "
      "sign(4cos(22.5) - 3) = +1 (3.6955... > 3); sign(cos(22.5) - "
      "cos(67.5)) = +1 (0.9238... > 0.3826...); and sign(0) = 0",
      ksign(_t1) == -1 and ksign(_t2) == +1
      and ksign(C22 - C67) == +1 and ksign(K0) == 0,
      f"signs {ksign(_t1)}, {ksign(_t2)}, {ksign(C22 - C67)}, "
      f"{ksign(K0)}; c bracketed in "
      f"[{float(_CLO[0]):.12f}, {float(_CHI[0]):.12f}]; refinement used "
      f"at most {max(SIGN_STEPS[0], 120)} bisection steps")

_inv = (K(3) + SQRT2).inv()
check("K1.4 EXACT DIVISION IN K IS AVAILABLE AND VERIFIED: the inverse is "
      "computed from the 4x4 rational multiplication matrix and "
      "(3 + sqrt2)^{-1} (3 + sqrt2) = 1 with zero residual",
      (_inv * (K(3) + SQRT2) - K1).is_zero(),
      f"(3+sqrt2)^-1 = {_inv}")


# --- matrices over K ------------------------------------------------------

def mzeros(n, m=None):
    m = n if m is None else m
    return [[K0] * m for _ in range(n)]


def meye(n):
    return [[K1 if i == j else K0 for j in range(n)] for i in range(n)]


def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    Bt = [[B[r][c] for r in range(k)] for c in range(m)]
    out = []
    for i in range(n):
        Ai = A[i]
        nz = [(t, Ai[t]) for t in range(k) if not Ai[t].is_zero()]
        row = []
        for j in range(m):
            Bj = Bt[j]
            s = K0
            for t, v in nz:
                w = Bj[t]
                if not w.is_zero():
                    s = s + v * w
            row.append(s)
        out.append(row)
    return out


def mT(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def kron(A, B):
    na, ma, nb, mb = len(A), len(A[0]), len(B), len(B[0])
    out = mzeros(na * nb, ma * mb)
    for i in range(na):
        for j in range(ma):
            if A[i][j].is_zero():
                continue
            for p in range(nb):
                for q in range(mb):
                    if not B[p][q].is_zero():
                        out[i * nb + p][j * mb + q] = A[i][j] * B[p][q]
    return out


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def schur_sq(U):
    """Gamma_ij = |U_ij|^2.  Every operator in this receipt is REAL
    orthogonal, so |U_ij|^2 = U_ij^2 and no complex ring is needed; the
    realness is gated below."""
    return [[U[i][j] * U[i][j] for j in range(len(U[0]))]
            for i in range(len(U))]


def orth_residuals(U):
    n = len(U)
    bad = []
    for i in range(n):
        for j in range(n):
            s = K0
            for t in range(n):
                if not U[t][i].is_zero() and not U[t][j].is_zero():
                    s = s + U[t][i] * U[t][j]
            want = K1 if i == j else K0
            if not (s - want).is_zero():
                bad.append((i, j))
    return bad


def mrank(A):
    """Exact rank over K by Gauss-Jordan."""
    M = [row[:] for row in A]
    n, m = len(M), len(M[0])
    r = 0
    for c in range(m):
        piv = None
        for i in range(r, n):
            if not M[i][c].is_zero():
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c].inv()
        M[r] = [x * pv for x in M[r]]
        for i in range(n):
            if i != r and not M[i][c].is_zero():
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        r += 1
        if r == n:
            break
    return r


# ===========================================================================
# SEC 2.  THE ANCHOR — u3's committed instrument, extracted and re-run
# ===========================================================================

sec("ANCHOR — the committed U3 unistochasticity instrument, single-sourced "
    "by AST and re-run on its own known-answer battery")

_P_U3 = "v11/code/u3_unistochasticity_screen_exact.py"

U3_REQ = {
    "sqfree_split": ["n"],
    "Surd": ["<class>"],
    "surd_sign": ["x"],
    "sqrt_fr": ["r"],
    "ds_report": ["M"],
    "tri_disc": ["a", "b", "c"],
    "chain_link_squares": ["M", "p", "q", "by"],
    "polygon_violations": ["M"],
    "real_orth_2x2": ["B"],
    "orth_check_surd": ["U"],
    "modsq_check_surd": ["U", "M"],
    "sylvester": ["k"],
}


def ast_signatures(path, required):
    tree = ast.parse(open(path).read(), filename=path)
    sigs = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            sigs[node.name] = [a.arg for a in node.args.args]
        elif isinstance(node, ast.ClassDef):
            sigs[node.name] = ["<class>"]
    missing = []
    for name, args in required.items():
        if name not in sigs:
            missing.append((name, "ABSENT"))
        elif args is not None and sigs[name] != args:
            missing.append((name, f"{sigs[name]} != {args}"))
    return sigs, missing


def ast_defs(path, names, ns):
    src = open(path).read()
    tree = ast.parse(src, filename=path)
    lines = src.splitlines(keepends=True)
    segs = {}
    for nd in tree.body:
        if isinstance(nd, (ast.FunctionDef, ast.ClassDef)) and nd.name in names:
            segs[nd.name] = "".join(lines[nd.lineno - 1:nd.end_lineno])
    for nm in names:
        if nm in segs:
            exec(compile(segs[nm], f"<ast:{os.path.basename(path)}:{nm}>",
                         "exec"), ns)
    return segs


_s3, _m3 = ast_signatures(_P_U3, U3_REQ)
anchor("A0 AST SIGNATURE PASS on the committed U3 receipt: every reused "
       "def/class exists at module level with the exact positional "
       "argument list, so a silent upstream edit cannot slip through",
       not _m3,
       f"u3 has {len(_s3)} module-level defs/classes; missing/mismatched "
       f"{_m3}")

import math as _math
NSU3 = {"Fr": Fr, "math": _math, "product": product}
_segu3 = ast_defs(_P_U3, list(U3_REQ), NSU3)
NSU3["SIGN_BITS_USED"] = [0]
u3_ds_report = NSU3["ds_report"]
u3_tri_disc = NSU3["tri_disc"]
u3_chain = NSU3["chain_link_squares"]
u3_polygon = NSU3["polygon_violations"]
u3_real_orth_2x2 = NSU3["real_orth_2x2"]
u3_orth_check = NSU3["orth_check_surd"]
u3_modsq_check = NSU3["modsq_check_surd"]
u3_sylvester = NSU3["sylvester"]
anchor("A1 THE INSTRUMENT IS U3's, NOT A RE-IMPLEMENTATION: ds_report, "
       "tri_disc, chain_link_squares, polygon_violations, real_orth_2x2, "
       "orth_check_surd, modsq_check_surd, sylvester and the whole Surd "
       "ring are lifted by AST from the committed receipt and executed "
       "verbatim",
       len(_segu3) == len(U3_REQ),
       f"{len(_segu3)}/{len(U3_REQ)} lifted: {sorted(_segu3)}")

FLAT3 = [[Fr(1, 3)] * 3 for _ in range(3)]
_a_T1 = u3_tri_disc(*u3_chain(FLAT3, 0, 1, "col"))
_a_p1 = u3_polygon(FLAT3)
anchor("A2 KA-1 REPRODUCED: on the flat 3x3 J/3 the lifted criterion "
       "returns the committed triangle discriminant T = +1/27 and zero "
       "polygon violations [u3-ka]",
       _a_T1 == ANCH["ka1_T"] and len(_a_p1) == ANCH["ka1_poly"],
       f"T = {_a_T1} (committed {ANCH['ka1_T']}); polygon violations "
       f"{len(_a_p1)} (committed {ANCH['ka1_poly']})")

BNOT = [[Fr(0), Fr(1, 2), Fr(1, 2)],
        [Fr(1, 2), Fr(0), Fr(1, 2)],
        [Fr(1, 2), Fr(1, 2), Fr(0)]]
_a_ds2 = u3_ds_report(BNOT)
_a_T2 = u3_tri_disc(*u3_chain(BNOT, 0, 1, "col"))
_a_p2 = u3_polygon(BNOT)
_a_mod2 = u3_chain(BNOT, 0, 1, "col")
_a_mod2r = [NSU3["sqrt_fr"](x) for x in _a_mod2]
_a_mod2ok = ([str(x) for x in _a_mod2r]
             == [str(x) for x in ANCH["ka2_moduli"]])
anchor("A3 KA-2 REPRODUCED: on the canonical bistochastic-but-not-"
       "unistochastic B = (1/2)(J - I) the lifted instrument returns DS "
       "true, the committed T = -1/16, the committed phasor moduli "
       "(0, 0, 1/2) — U3's chain_link_squares returns their SQUARES "
       "(0, 0, 1/4), and both are checked — and a firing polygon "
       "obstruction [u3-ka]",
       _a_ds2["ds"] and _a_T2 == ANCH["ka2_T"] and len(_a_p2) > 0
       and _a_mod2 == ANCH["ka2_sqmoduli"] and _a_mod2ok,
       f"DS {_a_ds2['ds']}; T = {_a_T2} (committed {ANCH['ka2_T']}); "
       f"polygon violations {len(_a_p2)}; squared moduli {_a_mod2} "
       f"(committed squares {ANCH['ka2_sqmoduli']}); moduli "
       f"{[str(x) for x in _a_mod2r]} (committed {ANCH['ka2_moduli']})")

B2 = [[Fr(1, 3), Fr(2, 3)], [Fr(2, 3), Fr(1, 3)]]
U2 = u3_real_orth_2x2(B2)
_a4 = len(u3_orth_check(U2)) + len(u3_modsq_check(U2, B2))
_H8 = u3_sylvester(3)
_a6 = all(sum(_H8[k][i] * _H8[k][j] for k in range(8))
          == (ANCH["ka6_gram"] if i == j else 0)
          for i in range(8) for j in range(8))
anchor("A4 KA-4 AND KA-6 REPRODUCED: the constructed 2x2 orthostochastic "
       "certificate has zero orthogonality residuals and zero "
       "modulus-square mismatches, and Sylvester's H_8 satisfies "
       "H H^T = 8 I exactly over Z [u3-ka]",
       _a4 == ANCH["ka4_resid"] and _a6,
       f"2x2 residuals+mismatches {_a4} (committed "
       f"{ANCH['ka4_resid']}); H_8 Gram exact: {_a6}")

BRS = [[Fr(1, 2), Fr(1, 2)], [Fr(1), Fr(0)]]
_a5 = u3_ds_report(BRS)
anchor("A5 KA-5 REPRODUCED: the doubly-stochastic precondition is not a "
       "no-op — a row-stochastic non-column-stochastic matrix is caught, "
       "with the exact per-column excess [u3-ka]",
       _a5["row_ok"] and not _a5["col_ok"] and not _a5["ds"],
       f"row sums {_a5['rowsums']}; column sums {_a5['colsums']}; column "
       f"deficits {_a5['coldef']}")

print()
print(f"  THE POSITIVE-VERDICT DISCIPLINE, INHERITED VERBATIM "
      f"({QUOTES['u3-positive'][0]}):")
print(f'    "{QUOTES["u3-positive"][1]}"')
print("  Every unistochasticity verdict in SEC 4 below is therefore a")
print("  CERTIFICATE verdict: the real orthogonal operator is exhibited")
print("  and U^T U = I and U_ij^2 = Gamma_ij are verified entry by entry")
print("  in K.  The cited criterion is never load-bearing on a positive.")
print("  CAP: U3's polygon oracle takes RATIONAL entries (it calls")
print("  sqrt_fr on a Fraction).  This model's entries lie in Q(sqrt2),")
print("  so the polygon arm runs on the rational anchors only; the legs")
print("  are decided by the strictly stronger certificate route.")


# ===========================================================================
# SEC 3.  THE MODEL
# ===========================================================================

sec("THE MODEL — one Bell experiment as a [B3] indivisible stochastic "
    "process, exact")

print(f"""
  [B3]'s KINEMATICAL AXIOM ({QUOTES['B3-axioms'][0]}):
    "{QUOTES['B3-axioms'][1][:300]}..."

  THE CONFIGURATION SPACE, FIXED (one set, both frames, all settings):

    C = {{ (qA, qB, pA, pB) }},  qA, qB in {{0, 1}},  pA, pB in {{r, +, -}}

  qA, qB are the two wings' spin configurations in a FIXED reference
  basis (the model's declared configuration basis); pA, pB are the two
  pointers' configurations.  |C| = 2 * 2 * 3 * 3 = 36.  The pointer
  configurations are [B3]'s MEASUREMENT-OUTCOME CONFIGURATIONS
  ({QUOTES['B3-outcomes'][0]}): "{QUOTES['B3-outcomes'][1][:180]}..."

  Index: i = ((qA*2 + qB)*3 + pA)*3 + pB.  The initial configuration is
  j0 = (0, 0, r, r) = index 0.

  THE OPERATORS (all REAL orthogonal; the realness is gated):
    U_prep : acts on (qA, qB) only; its j0 column is the singlet
             (|01> - |10>)/sqrt2, so the post-preparation state is the
             singlet with both pointers ready.
    U_A(a) : sum over s of Pi^a_s (x) I (x) Sh^{{n(s)}} (x) I, with
             Pi^a_s the spin projector for the coplanar direction a on
             wing A and Sh the 3-cycle r -> + -> - -> r on pointer A;
             n(+) = 1, n(-) = 2.  Reading the pointer off its ready state
             therefore records the outcome.
    U_B(b) : the same on wing B and pointer B.
  U_A and U_B act on disjoint tensor factors, so they COMMUTE exactly;
  that is the only algebraic input the two-frame construction needs, and
  it is gated below.
""")

NQ, NP, NC = 2, 3, 36
PT_NAME = {0: "r", 1: "+", 2: "-"}


def cfg(i):
    pB = i % 3
    pA = (i // 3) % 3
    qB = (i // 9) % 2
    qA = (i // 18) % 2
    return (qA, qB, pA, pB)


def cfg_str(i):
    qA, qB, pA, pB = cfg(i)
    return f"({qA}{qB}|{PT_NAME[pA]}{PT_NAME[pB]})"


J0 = 0
assert cfg(J0) == (0, 0, 0, 0)

I2 = meye(2)
I3 = meye(3)
I9 = meye(9)
SH = [[K0, K0, K1], [K1, K0, K0], [K0, K1, K0]]      # r->+ ->- ->r
SH2 = mmul(SH, SH)

HALF = {0: (K1, K0), 45: (C22, S22), 90: (C45, C45), 135: (C67, S67),
        180: (K0, K1)}
COS = {0: K1, 45: C45, 90: K0, 135: -C45, 180: -K1,
       -45: C45, -90: K0, -135: -C45, -180: -K1}


def proj(theta):
    """Pi_+ and Pi_- for the coplanar direction theta (degrees)."""
    ct, st = HALF[theta % 360] if theta % 360 in HALF else HALF[theta]
    vp = [ct, st]
    vm = [-st, ct]
    Pp = [[vp[i] * vp[j] for j in range(2)] for i in range(2)]
    Pm = [[vm[i] * vm[j] for j in range(2)] for i in range(2)]
    return Pp, Pm


def U_meas(theta, wing):
    Pp, Pm = proj(theta)
    out = mzeros(NC)
    for P, sh in ((Pp, SH), (Pm, SH2)):
        if wing == "A":
            spin = kron(P, I2)
            ptr = kron(sh, I3)
        else:
            spin = kron(I2, P)
            ptr = kron(I3, sh)
        out = madd(out, kron(spin, ptr))
    return out


R2H = SQRT2 * K(Fr(1, 2))                     # 1/sqrt2
PREP4 = [[K0, R2H, R2H, K0],
         [R2H, K0, K0, R2H],
         [-R2H, K0, K0, R2H],
         [K0, R2H, -R2H, K0]]
U_PREP = kron(PREP4, I9)

_pr = orth_residuals(PREP4)
_sing = [PREP4[i][0] for i in range(4)]
check("M1 THE PREPARATION OPERATOR IS EXACTLY ORTHOGONAL AND ITS j0 "
      "COLUMN IS EXACTLY THE SINGLET: all 16 inner products verified in "
      "K with zero residual, and column 0 is (0, 1/sqrt2, -1/sqrt2, 0) "
      "on the pair basis (00, 01, 10, 11)",
      not _pr and _sing[0].is_zero() and (_sing[1] - R2H).is_zero()
      and (_sing[2] + R2H).is_zero() and _sing[3].is_zero(),
      f"orthogonality residuals {len(_pr)}; singlet column "
      f"{[str(x) for x in _sing]}")

SETTINGS = [("SP-A", 0, 45), ("SP-B", 0, 135), ("SP-C", 90, 45),
            ("SP-D", 90, 135), ("SP-E", 0, 0), ("SP-F", 45, 45)]

UA_CACHE, UB_CACHE = {}, {}
for _nm, _a, _b in SETTINGS:
    if _a not in UA_CACHE:
        UA_CACHE[_a] = U_meas(_a, "A")
    if _b not in UB_CACHE:
        UB_CACHE[_b] = U_meas(_b, "B")
tick("measurement operators built")

_bad_orth = []
for _lab, _U in ([("U_prep", U_PREP)]
                 + [(f"U_A({a})", U) for a, U in sorted(UA_CACHE.items())]
                 + [(f"U_B({b})", U) for b, U in sorted(UB_CACHE.items())]):
    _r = orth_residuals(_U)
    if _r:
        _bad_orth.append((_lab, len(_r)))
check("M2 EVERY TIME-EVOLUTION OPERATOR IS EXACTLY REAL ORTHOGONAL: "
      f"U^T U = I verified entry by entry in K for U_prep and for all "
      f"{len(UA_CACHE)} + {len(UB_CACHE)} measurement operators — "
      f"{NC*NC} inner products each, zero residuals.  Hence "
      "|U_ij|^2 = U_ij^2 and no complex ring is needed anywhere",
      not _bad_orth, f"operators checked "
                     f"{1 + len(UA_CACHE) + len(UB_CACHE)}; failures "
                     f"{_bad_orth}")

_comm_fail = []
for _a in sorted(UA_CACHE):
    for _b in sorted(UB_CACHE):
        P1 = mmul(UA_CACHE[_a], UB_CACHE[_b])
        P2 = mmul(UB_CACHE[_b], UA_CACHE[_a])
        d = sum(1 for i in range(NC) for j in range(NC)
                if not (P1[i][j] - P2[i][j]).is_zero())
        if d:
            _comm_fail.append((_a, _b, d))
check("M3 THE TWO MEASUREMENT OPERATORS COMMUTE EXACTLY, AT EVERY "
      "SETTING PAIR: [U_A(a), U_B(b)] = 0 entry by entry in K over all "
      f"{len(UA_CACHE)} x {len(UB_CACHE)} = "
      f"{len(UA_CACHE)*len(UB_CACHE)} pairs.  This is the ONLY algebraic "
      "input the two-frame construction uses, and it is why the two "
      "frames can agree on the final-time law at all",
      not _comm_fail, f"pairs checked {len(UA_CACHE)*len(UB_CACHE)}; "
                      f"failures {_comm_fail}")
tick("commutation gate done")


# ===========================================================================
# SEC 4.  THE TWO FRAMES, AND THE UNISTOCHASTICITY SCREEN OF EVERY LEG
# ===========================================================================

sec("THE TWO FRAMES — every transition matrix exact, every leg screened")

print("""
  THE TWO ORDERINGS OF THE SAME EXPERIMENT.

    F1 = (prep, A, B)          F2 = (prep, B, A)

  Target times 0, 1, 2, 3 in each frame.  The time-evolution operators
  Theta(t <- 0) of [B3] eq. (25) are

    F1:  Theta(0<-0) = I,  Theta(1<-0) = U_prep,
         Theta(2<-0) = U_A U_prep,   Theta(3<-0) = U_B U_A U_prep
    F2:  Theta(0<-0) = I,  Theta(1<-0) = U_prep,
         Theta(2<-0) = U_B U_prep,   Theta(3<-0) = U_A U_B U_prep

  DIVISION EVENTS: D = {0, 2, 3} in each frame.  0 is the initial
  division event ([B3] p.9: conditioning times "are assumed to include an
  'initial' time 0"); 2 and 3 are generated by the two measurements
  ([B3] p.29: "division events are generated during a measurement
  process").  t = 1 is a target time and NOT a division event.

  Conditioning at a division event restarts the conditioning: the leg
  matrix is Gamma(3<-2) = |Theta(3<-2)|^2 with Theta(3<-2) the second
  measurement's operator.  In F1 that is U_B; in F2 it is U_A.
""")


class Frame:
    def __init__(self, name, order, Ua, Ub):
        self.name = name
        self.order = order            # ("A","B") or ("B","A")
        first = Ua if order[0] == "A" else Ub
        second = Ub if order[0] == "A" else Ua
        self.theta = {0: meye(NC), 1: U_PREP,
                      2: mmul(first, U_PREP),
                      3: mmul(second, mmul(first, U_PREP))}
        self.leg = {(3, 2): second}
        self.D = (0, 2, 3)
        self.T = (0, 1, 2, 3)
        self.G = {}                                  # Gamma(t <- t')
        for t in self.T:
            self.G[(t, 0)] = schur_sq(self.theta[t])
        self.G[(3, 2)] = schur_sq(second)
        self.G[(2, 2)] = meye(NC)
        self.G[(3, 3)] = meye(NC)
        self.G[(2, 3)] = None                        # retrodictive: capped
        self.p = {t: [self.G[(t, 0)][i][J0] for i in range(NC)]
                  for t in self.T}

    def joint(self, t, tp):
        """The division-event joint P(i,t ; j,t') = Gamma_ij(t<-t') p_j(t')."""
        Gm, pv = self.G[(t, tp)], self.p[tp]
        return [[Gm[i][j] * pv[j] for j in range(NC)] for i in range(NC)]


FRAMES = {}
for _nm, _a, _b in SETTINGS:
    FRAMES[(_nm, "F1")] = Frame("F1", ("A", "B"), UA_CACHE[_a], UB_CACHE[_b])
    FRAMES[(_nm, "F2")] = Frame("F2", ("B", "A"), UA_CACHE[_a], UB_CACHE[_b])
    tick(f"frames built for {_nm} (a={_a}, b={_b})")

# ---- the screen ----------------------------------------------------------
_screen_rows = []
_screen_bad = []
for _nm, _a, _b in SETTINGS:
    for _fr in ("F1", "F2"):
        F = FRAMES[(_nm, _fr)]
        for key, U in [((1, 0), F.theta[1]), ((2, 0), F.theta[2]),
                       ((3, 0), F.theta[3]), ((3, 2), F.leg[(3, 2)])]:
            G = F.G[key]
            ds = u3_ds_report(G)
            mod_bad = sum(1 for i in range(NC) for j in range(NC)
                          if not (U[i][j] * U[i][j] - G[i][j]).is_zero())
            orth_bad = len(orth_residuals(U))
            ok = ds["ds"] and mod_bad == 0 and orth_bad == 0
            _screen_rows.append((_nm, _fr, key, ds["ds"], orth_bad, mod_bad))
            if not ok:
                _screen_bad.append((_nm, _fr, key, ds["ds"], orth_bad,
                                    mod_bad))
    tick(f"legs screened for {_nm}")

check("S1 EVERY LEG OF EVERY FRAME IS UNISTOCHASTIC, BY EXHIBITED "
      "CERTIFICATE AND NOT BY CRITERION: for all "
      f"{len(_screen_rows)} legs (6 setting pairs x 2 frames x 4 legs) "
      "U3's lifted ds_report returns doubly stochastic with EXACT unit "
      "row and column sums and no negative entry, the exhibited real "
      "orthogonal operator has zero U^T U - I residuals, and "
      f"U_ij^2 = Gamma_ij at all {NC*NC} entries.  This is [B3]'s own "
      "unistochastic-process property (p.18, eq. 64 context) verified "
      "rather than assumed",
      not _screen_bad, f"legs screened {len(_screen_rows)}; failures "
                       f"{_screen_bad}")

# ---- indivisibility witness and the eq.(22) hypothesis -------------------
_indiv, _rank22 = [], []
for _nm, _a, _b in SETTINGS:
    row = {}
    for _fr, first in (("F1", _a), ("F2", _b)):
        F = FRAMES[(_nm, _fr)]
        prod = mmul(F.G[(3, 2)], F.G[(2, 0)])
        d = sum(1 for i in range(NC) for j in range(NC)
                if not (prod[i][j] - F.G[(3, 0)][i][j]).is_zero())
        row[_fr] = (d, first % 180 == 0)
    _indiv.append((_nm, row["F1"][0], row["F2"][0],
                   row["F1"][1], row["F2"][1]))
    _rank22.append((_nm, mrank(FRAMES[(_nm, "F1")].G[(2, 0)]),
                    mrank(FRAMES[(_nm, "F2")].G[(2, 0)])))
    tick(f"divisibility + eq.(22) rank for {_nm}")

_indiv_some = [nm for nm, d1, d2, a1, a2 in _indiv if d1 > 0]
_div_some = [nm for nm, d1, d2, a1, a2 in _indiv if d1 == 0]
check("S2 THE MODEL IS A GENUINE [B3] INDIVISIBLE PROCESS AT SOME "
      "SETTINGS AND A DIVISIBLE ONE AT OTHERS, AND THE CENSUS IS "
      "PRINTED: Gamma(3<-2) Gamma(2<-0) differs from Gamma(3<-0) in the "
      "counted entries at the setting pairs listed, and is exactly equal "
      "at the others.  Both cells are non-empty, so the two-frame test "
      "below runs on divisible and on indivisible instances of the same "
      "construction",
      len(_indiv_some) > 0 and len(_div_some) > 0,
      f"indivisible at t=2: {_indiv_some}; divisible at t=2: "
      f"{_div_some}; (setting, F1 differing entries, F2 differing "
      f"entries) = {[(x[0], x[1], x[2]) for x in _indiv]}")

_div_split = [nm for nm, d1, d2, a1, a2 in _indiv if (d1 == 0) != (d2 == 0)]
check("S2b DIVISIBILITY AT THE INTERMEDIATE DIVISION EVENT IS NOT ITSELF "
      "FRAME-DEPENDENT ON THIS MODEL — A REPORTED NEGATIVE ON A NATURAL "
      "CONJECTURE.  The two frames agree on whether the process divides "
      "at their (different) intermediate division events, at every "
      "setting pair.  QUALIFIER, carried wherever this incidental is "
      "stated: the process divides IN BOTH FRAMES AT SP-A, SP-B AND "
      "SP-E ONLY, and divides in NEITHER frame at SP-C, SP-D, SP-F; the "
      "agreement is that the divisible/indivisible split does not move "
      "with the frame, not that the process divides everywhere.  The "
      "mismatch found below is therefore not a divisibility artefact: "
      "it is present at SP-A and SP-B, where the process divides in "
      "both frames",
      not _div_split,
      f"setting pairs with a frame-split on divisibility: {_div_split} "
      f"(empty); divisible-in-both (the qualifier): {_div_some}; "
      f"indivisible-in-both: {_indiv_some}")

check("S3 [B3] eq. (22)'s OWN HYPOTHESIS FAILS ON THIS MODEL: the "
      "interpolant ~Gamma(3<-2) = Gamma(3<-0) Gamma^{-1}(2<-0) requires "
      f"Gamma(2<-0) to be invertible, and its exact rank over K is "
      f"strictly below {NC} in BOTH frames at every setting pair.  The "
      "pseudo-stochastic diagnosis of [B3-eq22] is therefore not even "
      "reached here — the inverse does not exist.  This is a datum, not "
      "a claim about indivisibility in general (that census is U1's and "
      "BC1's, not this unit's)",
      all(r1 < NC and r2 < NC for nm, r1, r2 in _rank22),
      f"exact ranks of Gamma(2<-0) (F1, F2): {_rank22} (full rank would "
      f"be {NC})")


# ===========================================================================
# SEC 4b.  THE LAW-OF-TOTAL-PROBABILITY GATE AT EVERY DECLARED DIVISION
#          EVENT — which declared division events are division events
# ===========================================================================

sec("THE LAW-OF-TOTAL-PROBABILITY GATE — [B3] eqs. (19)-(20) at every "
    "declared division event")

print(f"""
  [B3] does not merely allow the relation p(t) = Gamma(t <- t_0) p(t_0)
  at a division event; it IS the content of being a division event.
  {QUOTES['B3-ltp'][0]}, verbatim:
    "{QUOTES['B3-ltp'][1]}"

  So a time t_0 declared to be a division event, at which some target
  time t has p(t) != Gamma(t <- t_0) p(t_0), is not a division event on
  [B3]'s own axioms: the transition matrix it would supply does not
  transport the standalone distribution.  The gate below runs the
  identity at EVERY declared division event t_0 in D = {{0, 2, 3}} and
  EVERY later target time t, in both frames, at all six setting pairs,
  entry by entry in K.  Its verdict decides which instances the
  division-event census of SEC 7-8 may be read on.
""")

LTP = []
for _nm, _a, _b in SETTINGS:
    for _fr in ("F1", "F2"):
        F = FRAMES[(_nm, _fr)]
        for tp in F.D:
            for t in F.T:
                if t <= tp or (t, tp) not in F.G or F.G[(t, tp)] is None:
                    continue
                G, pv = F.G[(t, tp)], F.p[tp]
                rhs = [sum((G[i][j] * pv[j] for j in range(NC)), K0)
                       for i in range(NC)]
                d = sum(1 for i in range(NC)
                        if not (F.p[t][i] - rhs[i]).is_zero())
                LTP.append((_nm, _fr, t, tp, d))
    tick(f"LTP gate done for {_nm}")

_ltp_init = [r for r in LTP if r[3] == 0]
_ltp_mid = [r for r in LTP if r[3] == 2]
check("L1 AT THE INITIAL DIVISION EVENT THE LAW OF TOTAL PROBABILITY "
      "HOLDS IDENTICALLY, AS IT MUST: p(t) = Gamma(t<-0) p(0) at every "
      f"target time, in both frames, at all {len(SETTINGS)} setting "
      f"pairs — {len(_ltp_init)} vector identities, "
      f"{len(_ltp_init)*NC} exact entry comparisons, zero mismatches.  "
      "This is a construction check, not a finding: p(t) is DEFINED as "
      "the j0 column of Gamma(t<-0), so its failure would mean an "
      "arithmetic error",
      all(r[4] == 0 for r in _ltp_init),
      f"identities {len(_ltp_init)}; nonzero mismatches "
      f"{[r for r in _ltp_init if r[4]]}")

_ltp_ok = sorted({r[0] for r in _ltp_mid if r[4] == 0})
_ltp_bad = sorted({r[0] for r in _ltp_mid if r[4] > 0})
_ltp_counts = sorted({(r[0], r[4]) for r in _ltp_mid})
_ltp_both = all(
    len({r[4] for r in _ltp_mid if r[0] == nm}) == 1 for nm in
    {r[0] for r in _ltp_mid})
check("L2 THE DECLARED INTERMEDIATE DIVISION EVENT FAILS THE LAW OF "
      "TOTAL PROBABILITY AT HALF THE DECLARED SETTING PAIRS, IN BOTH "
      "FRAMES — A FIRST-CLASS INCIDENTAL ABOUT [B3], NOT ABOUT THIS "
      "MODEL.  Routing the standalone distribution through the declared "
      "t = 2 division event, p(3) = Gamma(3<-2) p(2), holds exactly at "
      "SP-A, SP-B and SP-E and fails in 16 of the 36 entries at SP-C, "
      "SP-D and SP-F, identically in F1 and F2.  On [B3]'s own eqs. "
      "(19)-(20) that is not a division event, so the model must DENY "
      "the composite division event there — which p.10's "
      "system-centricity licenses ('Division events are not global "
      "properties of the whole universe, but are system-centric').  "
      "The census of SEC 7-8 is scoped accordingly and the headline "
      "negative is re-established without it (T1b, E2)",
      bool(_ltp_bad) and _ltp_ok == ["SP-A", "SP-B", "SP-E"]
      and _ltp_bad == ["SP-C", "SP-D", "SP-F"] and _ltp_both
      and all(r[4] == 16 for r in _ltp_mid if r[4]),
      f"LTP holds at t_0 = 2: {_ltp_ok}; LTP FAILS at t_0 = 2: "
      f"{_ltp_bad}; (setting, differing entries of 36) = {_ltp_counts}; "
      f"same count in both frames at every setting pair: {_ltp_both}")


OUT_PT = {1: 1, 2: -1}                 # pointer '+' encodes +1, '-' encodes -1


def routed_stats(F):
    """The outcome law obtained by routing p(2) through Gamma(3<-2) —
    i.e. the law [B3] eqs. (19)-(20) assign to the declared division
    event at t = 2, as against the model's own p(3)."""
    G, pv = F.G[(3, 2)], F.p[2]
    q = [sum((G[i][j] * pv[j] for j in range(NC)), K0) for i in range(NC)]
    joint = {}
    for al in (1, -1):
        for be in (1, -1):
            s = K0
            for i in range(NC):
                _, _, pA, pB = cfg(i)
                if pA in OUT_PT and pB in OUT_PT and OUT_PT[pA] == al \
                        and OUT_PT[pB] == be:
                    s = s + q[i]
            joint[(al, be)] = s
    return joint


_routed = []
for _nm, _a, _b in SETTINGS:
    for _fr in ("F1", "F2"):
        j = routed_stats(FRAMES[(_nm, _fr)])
        _routed.append((_nm, _fr, tuple(str(j[(al, be)]) for al in (1, -1)
                                        for be in (1, -1))))
for r in _routed:
    report(f"outcome law ROUTED through the declared t=2 division event "
           f"{r[0]} {r[1]}", r[2])

_UNIF = ("1/4", "1/4", "1/4", "1/4")
_EIGHTHS = ("1/8", "3/8", "3/8", "1/8")
check("L3 WHERE THE LAW OF TOTAL PROBABILITY FAILS, THE OUTCOME LAW IT "
      "WOULD DELIVER IS NOT THE SINGLET LAW — THE FAILURE IS "
      "PHYSICALLY LOUD, NOT A ROUNDING OF ONE ENTRY.  Routing the "
      "outcome statistics through the declared t = 2 division event "
      "gives exactly (1/4, 1/4, 1/4, 1/4) at SP-C and SP-D and exactly "
      "(1/8, 3/8, 3/8, 1/8) at SP-F, in both frames, against the "
      "singlet values Q1 verifies for the model's own p(3).  At SP-A, "
      "SP-B and SP-E the routed law equals the singlet law exactly.  "
      "The declared division event at SP-C/D/F would therefore erase "
      "the correlation the model predicts",
      all(v == _UNIF for nm, fr, v in _routed if nm in ("SP-C", "SP-D"))
      and all(v == _EIGHTHS for nm, fr, v in _routed if nm == "SP-F"),
      f"(setting, frame, routed law in the order ++, +-, -+, --) = "
      f"{_routed}")

_ltp_set = set(_ltp_bad)
_indiv_set = set(_indiv_some)
check("L4 ON THIS MODEL 'LEGITIMATE DIVISION EVENT' AND 'THE PROCESS "
      "DIVIDES AT IT' ARE THE SAME PREDICATE — THE INVERTED FACT.  The "
      "setting pairs at which the law of total probability fails at "
      "t = 2 are EXACTLY the setting pairs at which "
      "Gamma(3<-2) Gamma(2<-0) != Gamma(3<-0).  So the legitimate "
      "division-event census does not live on the indivisible "
      "instances; it lives on the DIVISIBLE ones, and S2b's incidental "
      "must be read with that qualifier: the two frames agree on "
      "divisibility, and the instances where they agree that the "
      "process divides — SP-A, SP-B, SP-E — are precisely the "
      "instances where the declared intermediate division event is "
      "legitimate at all",
      _ltp_set == _indiv_set,
      f"LTP-failing setting pairs {sorted(_ltp_set)}; indivisible "
      f"setting pairs {sorted(_indiv_set)}; identical: "
      f"{_ltp_set == _indiv_set}")

LEGIT = tuple(_ltp_ok)                 # declared t=2 division event stands
DENIED = tuple(_ltp_bad)               # declared t=2 division event denied
report("setting pairs where the declared t=2 division event survives the "
       "LTP gate", LEGIT)
report("setting pairs where [B3]'s own axioms force denying it", DENIED)


# ===========================================================================
# SEC 5.  THE SPECIFIED-CONTENT INVENTORY
# ===========================================================================

sec("THE SPECIFIED-CONTENT INVENTORY — printed completely, both frames")

print(f"""
  WHAT [B3] SPECIFIES ({QUOTES['B3-axioms'][0]}, {QUOTES['B3-dict'][0]}):

    (1) the configuration space C — FIXED, one set;
    (2) the division-event set D and its order in the model's time
        parameter;
    (3) the transition matrices Gamma(t <- t') for every division event
        t' in D and every target time t — the model's dynamical law;
    (4) the standalone single-time distributions p(t) for every target
        time t, given the contingent initial p(0);
    (5) the division-event two-time joints
        P(i,t ; j,t') = Gamma_ij(t<-t') p_j(t'), for t' in D.

  WHAT [B3] REFUSES TO SPECIFY ({QUOTES['B3-refusal'][0]}):
    "{QUOTES['B3-refusal'][1]}"
  So: NO Kolmogorov tower, NO trajectory joints, NO joint over two
  non-division times, NO realizer.  The comparison below is over (1)-(5)
  and NOTHING ELSE.  Nothing the framework refuses is used against it.
""")


def inventory(F, tag, full=True):
    print(f"  ---- INVENTORY: {tag} " + "-" * max(3, 50 - len(tag)))
    print(f"       configuration space   : |C| = {NC}, fixed, identical "
          f"in both frames")
    print(f"       division events D     : {list(F.D)}  (order "
          f"0 < 2 < 3 in the frame's own time parameter)")
    print(f"       physical labels of D  : 0 = prep, 2 = "
          f"{'A' if F.order[0]=='A' else 'B'}, 3 = "
          f"{'B' if F.order[0]=='A' else 'A'}")
    print(f"       target times T        : {list(F.T)}  (t = 1 is NOT a "
          f"division event)")
    for t in F.T:
        sup = [i for i in range(NC) if not F.p[t][i].is_zero()]
        vals = Counter(str(F.p[t][i]) for i in sup)
        print(f"       marginal p({t})        : support {len(sup)} of "
              f"{NC}; value census {dict(sorted(vals.items()))}")
        if full and len(sup) <= 16:
            print(f"                               "
                  f"{[cfg_str(i) for i in sup]}")
    for (t, tp) in sorted(F.G, key=lambda z: (z[1], z[0])):
        if F.G[(t, tp)] is None:
            print(f"       Gamma({t}<-{tp})          : NOT COMPUTED (cap: "
                  f"retrodictive, Bayes-determined)")
            continue
        G = F.G[(t, tp)]
        nz = sum(1 for i in range(NC) for j in range(NC)
                 if not G[i][j].is_zero())
        colsup = Counter(sum(1 for i in range(NC)
                             if not G[i][j].is_zero()) for j in range(NC))
        vals = len({G[i][j].key() for i in range(NC) for j in range(NC)})
        print(f"       Gamma({t}<-{tp})          : {nz} nonzero of "
              f"{NC*NC}; column-support census {dict(sorted(colsup.items()))}"
              f"; {vals} distinct values")
    for tp in F.D:
        for t in F.T:
            if (t, tp) in F.G and F.G[(t, tp)] is not None and t != tp:
                Jt = F.joint(t, tp)
                nz = sum(1 for i in range(NC) for j in range(NC)
                         if not Jt[i][j].is_zero())
                print(f"       joint ({t} ; {tp})       : {nz} nonzero "
                      f"cells of {NC*NC}")
    print()


print("  THE INVENTORY IS PRINTED COMPLETELY FOR BOTH FRAMES AT ALL SIX")
print("  DECLARED SETTING PAIRS — twelve inventories, no per-object")
print("  sampling.  The explicit configuration list is printed whenever a")
print("  marginal's support is at most 16 of the 36 configurations.")
print()
for _nm0, _a0, _b0 in SETTINGS:
    inventory(FRAMES[(_nm0, "F1")],
              f"{_nm0} (a={_a0}, b={_b0}) frame F1 = (prep, A, B)")
    inventory(FRAMES[(_nm0, "F2")],
              f"{_nm0} (a={_a0}, b={_b0}) frame F2 = (prep, B, A)")


# ===========================================================================
# SEC 6.  THE QM-STATISTICS GATE (CONTROL — exit 1 on failure)
# ===========================================================================

sec("THE QM-STATISTICS GATE — a CONTROL: both frames reproduce the exact "
    "singlet statistics (exit 1 on failure)")

print("""
  The singlet prediction for coplanar projective measurements at
  directions a and b is, exactly,

     P(alpha, beta) = (1 - alpha beta cos(a - b)) / 4,   alpha, beta = +-1
     P_A(alpha) = P_B(beta) = 1/2.

  The pointer configuration '+' encodes alpha = +1 and '-' encodes
  alpha = -1.  Failing this gate would mean the MODEL is wrong, not that
  a finding has been made, so it exits 1.
""")

OUT = {1: 1, 2: -1}


def outcome_stats(F):
    joint = {}
    for al in (1, -1):
        for be in (1, -1):
            s = K0
            for i in range(NC):
                _, _, pA, pB = cfg(i)
                if pA in OUT and pB in OUT and OUT[pA] == al and OUT[pB] == be:
                    s = s + F.p[3][i]
            joint[(al, be)] = s
    mA = {al: joint[(al, 1)] + joint[(al, -1)] for al in (1, -1)}
    mB = {be: joint[(1, be)] + joint[(-1, be)] for be in (1, -1)}
    return joint, mA, mB


_qm_bad = []
_qm_rows = []
for _nm, _a, _b in SETTINGS:
    cosd = COS[(_a - _b) % 360 if (_a - _b) % 360 in COS else (_a - _b)]
    if (_a - _b) not in COS:
        cosd = COS[(_a - _b) % 360]
    for _fr in ("F1", "F2"):
        F = FRAMES[(_nm, _fr)]
        joint, mA, mB = outcome_stats(F)
        for al in (1, -1):
            for be in (1, -1):
                want = (K1 - K(al * be) * cosd) * K(Fr(1, 4))
                if not (joint[(al, be)] - want).is_zero():
                    _qm_bad.append((_nm, _fr, al, be,
                                    str(joint[(al, be)]), str(want)))
        for al in (1, -1):
            if not (mA[al] - K(ANCH["singlet_marginal"])).is_zero():
                _qm_bad.append((_nm, _fr, "mA", al, str(mA[al]), "1/2"))
            if not (mB[al] - K(ANCH["singlet_marginal"])).is_zero():
                _qm_bad.append((_nm, _fr, "mB", al, str(mB[al]), "1/2"))
        _qm_rows.append((_nm, _fr, {f"{al:+d}{be:+d}": str(joint[(al, be)])
                                    for al in (1, -1) for be in (1, -1)}))

for r in _qm_rows:
    report(f"outcome law {r[0]} {r[1]}", r[2])

control("Q1 BOTH FRAMES REPRODUCE THE EXACT SINGLET OUTCOME LAW AT EVERY "
        "DECLARED SETTING PAIR: all 4 joint outcome probabilities equal "
        "(1 - alpha beta cos(a-b))/4 exactly in K, and both single-wing "
        "marginals are exactly 1/2, at all "
        f"{len(SETTINGS)} setting pairs and both frames — "
        f"{len(SETTINGS)*2*(4+4)} exact identities",
        not _qm_bad, f"violations {_qm_bad[:4]} (total {len(_qm_bad)})")

_ns_bad = []
for _fr in ("F1", "F2"):
    for a_fix, grp in (("a=0", ["SP-A", "SP-B"]), ("a=90", ["SP-C", "SP-D"])):
        js = [outcome_stats(FRAMES[(g, _fr)])[1] for g in grp]
        for al in (1, -1):
            if not (js[0][al] - js[1][al]).is_zero():
                _ns_bad.append((_fr, a_fix, al))
control("Q2 THE FRAME-INDEPENDENT OUTCOME LAW IS ALSO SETTING-LOCAL AT "
        "THE MARGINAL: wing A's outcome marginal is identical across the "
        "two values of b at fixed a, and wing B's across the two values "
        "of a at fixed b, exactly, in both frames.  (Stated as a "
        "property of the constructed model's statistics; NO locality or "
        "Bell-inequality claim is made or used anywhere in this unit)",
        not _ns_bad, f"violations {_ns_bad}")

_fin_bad = []
for _nm, _a, _b in SETTINGS:
    F1, F2 = FRAMES[(_nm, "F1")], FRAMES[(_nm, "F2")]
    d = sum(1 for i in range(NC) for j in range(NC)
            if not (F1.G[(3, 0)][i][j] - F2.G[(3, 0)][i][j]).is_zero())
    dp = sum(1 for i in range(NC) if not (F1.p[3][i] - F2.p[3][i]).is_zero())
    if d or dp:
        _fin_bad.append((_nm, d, dp))
check("Q3 THE FINAL-TIME LAW IS LITERALLY IDENTICAL IN THE TWO FRAMES: "
      f"Gamma(3<-0) agrees at all {NC*NC} entries and p(3) at all {NC} "
      "entries, at every setting pair, with the identity as the frame "
      "map.  This is the exact form of the agreement the two frames DO "
      "have, and it is what the mismatch census below must be read "
      "against",
      not _fin_bad, f"setting pairs with any disagreement: {_fin_bad}")


# ===========================================================================
# SEC 7.  THE TEST — the candidate frame map, and whether it carries
# ===========================================================================

sec("THE TEST — L-1 forces the frame map's form, and the search over that "
    "form is COMPLETE")

print(f"""
  WHAT MAY ACT.  L-1's constraint C4 ({QUOTES['L1-ladder'][0]}) requires
  every covariance claim to state (i) what acts, (ii) on what set,
  (iii) whether the acting maps are invertible.  Here:
    (i)   the frame change F1 <-> F2 (a boost that reverses the time
          order of the two spacelike-separated measurements);
    (ii)  the model's ONE fixed finite configuration space C, |C| = {NC}
          — [B3]'s kinematical axiom makes it fixed, and the same set
          serves both frames;
    (iii) the maps form a group: going F1 -> F2 and back is the identity,
          so R R' = I with both stochastic.

  L-1 (a) ({QUOTES['L1a'][0]}), verbatim:
    "{QUOTES['L1a'][1]}"

  L-1 (b) ({QUOTES['L1b'][0]}), verbatim:
    "{QUOTES['L1b'][1]}"

  CONSEQUENCE, ON THIS MODEL.  [B3]'s own footnote 7 (p.10) proves the
  same lemma for its own purposes ({QUOTES['B3-fn7'][0]}):
    "{QUOTES['B3-fn7'][1][:260]}..."
  So the candidate frame map is a PERMUTATION of C by L-1(a), and the
  IDENTITY if the boost is taken in a one-parameter subgroup by L-1(b).
  The search below is therefore COMPLETE over the admissible class — AND
  THE PREMISE THAT MAKES IT COMPLETE IS C4(iii) ITSELF, STATED HERE AND
  NOT LEFT IMPLICIT: THE TWO FRAME MAPS COMPOSE TO THE IDENTITY,
  F1 -> F2 -> F1 = id on C.  That premise is what makes the action a
  GROUP, and only inside a group action does L-1(a) DERIVE invertibility
  and hence the permutation form.  Drop it and the permutation class is
  no longer forced; what is left is a covariance carried by a semigroup
  or a non-group action, which is E4 and is OPEN.  Given the premise, a
  negative below is a proof of non-existence, not a failure to find.

  A CONVENTION NOTE, discharged rather than assumed away.  L-1(a) is
  stated for ROW-stochastic maps ("each R_g is row-stochastic on C");
  [B3]'s transition matrices are COLUMN-stochastic ({QUOTES['B3-colstoch'][0]}):
    "{QUOTES['B3-colstoch'][1]}"
  The mismatch is harmless here for three independent reasons, each
  checkable in this receipt.  (1) Transposition is a bijection between
  the two conventions and L-1(a)'s conclusion is transpose-invariant: X
  is a permutation matrix iff X^T is.  (2) The frame map acts on the
  objects by CONJUGATION, M -> P M P^T with P a permutation, and
  conjugation commutes with transposition, so every mismatch count and
  every invariant used below is convention-free.  (3) On this model the
  question does not arise at all: gate S1 verifies that every one of the
  48 legs has EXACT unit ROW sums AND EXACT unit COLUMN sums (U3's
  ds_report is a doubly-stochastic report), so each Gamma here is both
  row- and column-stochastic and both readings of L-1(a) apply verbatim.
""")

# -------- the labelled-structure machinery --------------------------------
SENT = "SENT"


def kk(x):
    return x.key()


def build_objs(F, times, use_marg, live_cols, phi=None, divs=None):
    """The specified content of F as an ordered list of labelled objects.
    phi maps THIS frame's times to the comparison index; when phi is None
    the frame's own times are used.  divs overrides the frame's declared
    division-event set — used by E2, which DENIES the intermediate
    division event while keeping every target time ([B3] p.10: the target
    time 'can be treated as a free variable'; p.29: 'for arbitrary target
    times')."""
    ph = (lambda t: t) if phi is None else phi
    D = F.D if divs is None else divs
    objs = []
    if use_marg:
        for t in sorted(times, key=ph):
            objs.append(("vec", ("p", ph(t)),
                         [kk(F.p[t][i]) for i in range(NC)]))
    objs.append(("vec", ("init",), [kk(K1 if i == J0 else K0)
                                    for i in range(NC)]))
    pairs = []
    for tp in D:
        for t in times:
            if (t, tp) in F.G and F.G[(t, tp)] is not None and t != tp:
                pairs.append((t, tp))
    for (t, tp) in sorted(pairs, key=lambda z: (ph(z[1]), ph(z[0]))):
        G = F.G[(t, tp)]
        if live_cols:
            live = [j for j in range(NC) if not F.p[tp][j].is_zero()]
        else:
            live = list(range(NC))
        liveset = set(live)
        M = [[kk(G[i][j]) if j in liveset else SENT for j in range(NC)]
             for i in range(NC)]
        objs.append(("mat", ("G", ph(t), ph(tp)), M))
    return objs


def obj_labels(objs):
    return [o[1] for o in objs]


def verify_pi(pi, o1, o2):
    """Exact verification that pi carries o1 onto o2."""
    for a, b in zip(o1, o2):
        if a[0] != b[0]:
            return False
        if a[0] == "vec":
            for i in range(NC):
                if a[2][i] != b[2][pi[i]]:
                    return False
        else:
            A, B = a[2], b[2]
            for i in range(NC):
                pii = pi[i]
                for j in range(NC):
                    if A[i][j] != B[pii][pi[j]]:
                        return False
    return True


NODE_CAP = 200000
NODES = [0]


def common_labels(o1, o2):
    """The sub-inventory both frames specify under the same label.  Objects
    only one frame carries are DROPPED and reported: the comparison must
    give the frame map its best chance, and a missing label is an
    order-level fact censused separately, not a probabilistic mismatch."""
    l1, l2 = obj_labels(o1), obj_labels(o2)
    keep = [x for x in l1 if x in l2]
    d1 = [x for x in l1 if x not in l2]
    d2 = [x for x in l2 if x not in l1]
    m1 = {o[1]: o for o in o1}
    m2 = {o[1]: o for o in o2}
    return ([m1[x] for x in keep], [m2[x] for x in keep], d1, d2)


def _sigs_init(objs):
    out = []
    for i in range(NC):
        sig = []
        for o in objs:
            if o[0] == "vec":
                sig.append(repr(o[2][i]))
            else:
                M = o[2]
                sig.append(repr(sorted(map(repr, M[i]))))
                sig.append(repr(sorted(map(repr,
                                           (M[r][i] for r in range(NC))))))
        out.append(repr(sig))
    return out


def _sigs_step(objs, col):
    out = []
    for i in range(NC):
        sig = [col[i]]
        for o in objs:
            if o[0] == "mat":
                M = o[2]
                sig.append(sorted((col[j], repr(M[i][j]))
                                  for j in range(NC)))
                sig.append(sorted((col[j], repr(M[j][i]))
                                  for j in range(NC)))
        out.append(repr(sig))
    return out


def _encode(s1, s2):
    """ONE shared encoding for both sides — without this the two sides'
    colour integers are incomparable and the search is unsound."""
    enc = {}
    for s in s1 + s2:
        if s not in enc:
            enc[s] = len(enc)
    return [enc[s] for s in s1], [enc[s] for s in s2]


def _refine_pair(o1, o2, col1, col2):
    for _ in range(NC + 2):
        n1, n2 = _encode(_sigs_step(o1, col1), _sigs_step(o2, col2))
        if len(set(n1 + n2)) == len(set(col1 + col2)):
            return n1, n2
        col1, col2 = n1, n2
    return col1, col2


def _hist(col):
    return tuple(sorted(Counter(col).items()))


def find_iso(o1, o2):
    """Complete search for a permutation pi with pi : o1 -> o2.
    Returns (pi or None, reason)."""
    if obj_labels(o1) != obj_labels(o2):
        return None, ("object label lists differ: "
                      f"{obj_labels(o1)} vs {obj_labels(o2)}")
    col1, col2 = _encode(_sigs_init(o1), _sigs_init(o2))
    return _search(o1, o2, col1, col2)


def _search(o1, o2, col1, col2):
    NODES[0] += 1
    if NODES[0] > NODE_CAP:
        raise RuntimeError("search node cap exceeded")
    col1, col2 = _refine_pair(o1, o2, col1, col2)
    if _hist(col1) != _hist(col2):
        h1, h2 = Counter(col1), Counter(col2)
        alph = sorted(set(h1) | set(h2), key=repr)
        diff = [(c, h1.get(c, 0), h2.get(c, 0)) for c in alph
                if h1.get(c, 0) != h2.get(c, 0)]
        return None, (
            "refinement separates on the SHARED colour alphabet — the "
            "separating invariant is the colour-VALUE histogram, not a "
            "class-size profile: "
            f"{len(diff)} of {len(alph)} colours carry different "
            f"multiplicities; (colour, count in the F1 structure, count "
            f"in the F2 structure) = {diff[:6]}"
            + (f" ... [{len(diff) - 6} more]" if len(diff) > 6 else ""))
    classes = {}
    for i, c in enumerate(col1):
        classes.setdefault(c, []).append(i)
    big = [c for c, v in classes.items() if len(v) > 1]
    if not big:
        inv2 = {c: i for i, c in enumerate(col2)}
        pi = [inv2[col1[i]] for i in range(NC)]
        if verify_pi(pi, o1, o2):
            return pi, "discrete refinement, verified"
        return None, "discrete refinement, verification failed"
    tgt = min(big, key=lambda c: (len(classes[c]), c))
    u = classes[tgt][0]
    cand = [i for i in range(NC) if col2[i] == tgt]
    for v in cand:
        a = list(col1)
        b = list(col2)
        a[u] = "IND"
        b[v] = "IND"
        a, b = _encode([repr(x) for x in a], [repr(x) for x in b])
        r, why = _search(o1, o2, a, b)
        if r is not None:
            return r, why
    return None, f"exhausted {len(cand)} candidates at refined class {tgt}"


# -------- machinery controls ---------------------------------------------
_ctlF = FRAMES[("SP-A", "F1")]
_ctl_objs = build_objs(_ctlF, _ctlF.T, True, False)
PI0 = list(range(NC))
PI0[3], PI0[7] = PI0[7], PI0[3]              # a declared transposition


def relabel(objs, pi):
    out = []
    inv = [0] * NC
    for i, v in enumerate(pi):
        inv[v] = i
    for o in objs:
        if o[0] == "vec":
            out.append(("vec", o[1], [o[2][inv[i]] for i in range(NC)]))
        else:
            M = o[2]
            out.append(("mat", o[1],
                        [[M[inv[i]][inv[j]] for j in range(NC)]
                         for i in range(NC)]))
    return out


NODES[0] = 0
_pi_id, _w_id = find_iso(_ctl_objs, _ctl_objs)
_pi_rl, _w_rl = find_iso(_ctl_objs, relabel(_ctl_objs, PI0))
control("T0a THE SEARCH MACHINERY FINDS AN ISOMORPHISM WHEN ONE EXISTS: "
        "a structure against itself, and against its own relabelling by "
        "a declared transposition (3 7), are both solved, and the "
        "returned permutation is VERIFIED entry by entry against every "
        "object",
        _pi_id is not None and _pi_rl is not None
        and verify_pi(_pi_rl, _ctl_objs, relabel(_ctl_objs, PI0)),
        f"identity case: {_w_id}; relabelled case: {_w_rl}; "
        f"pi(3) = {_pi_rl[3] if _pi_rl else None}, "
        f"pi(7) = {_pi_rl[7] if _pi_rl else None}")

_bad_objs = [("vec", ("p", 0), [kk(K1 if i == 0 else K0) for i in range(NC)]),
             ("vec", ("init",), [kk(K1 if i == J0 else K0)
                                 for i in range(NC)]),
             ("mat", ("G", 1, 0), [[kk(K0)] * NC for _ in range(NC)])]
_bad_objs2 = [("vec", ("p", 0), [kk(K1 if i == 0 else K0) for i in range(NC)]),
              ("vec", ("init",), [kk(K1 if i == J0 else K0)
                                  for i in range(NC)]),
              ("mat", ("G", 1, 0), [[kk(K1 if i == j else K0)
                                     for j in range(NC)] for i in range(NC)])]
_pi_neg, _w_neg = find_iso(_bad_objs, _bad_objs2)
control("T0b THE SEARCH MACHINERY RETURNS A NEGATIVE WHEN IT SHOULD: two "
        "structures differing only in one matrix (all-zero versus the "
        "identity) are separated, with the separating invariant printed",
        _pi_neg is None, f"reason: {_w_neg}")

# -------- the frame maps --------------------------------------------------
print("""
  THE TWO CANDIDATE TIME-CORRESPONDENCES.

    phi_LOR  THE LORENTZ CORRESPONDENCE.  Each division event is the SAME
             PHYSICAL EVENT in the two frames, so prep -> prep, A -> A,
             B -> B.  In F1 the times are (prep, A, B) = (0, 2, 3); in F2
             they are (prep, B, A) = (0, 2, 3).  Hence phi_LOR sends F1's
             t = 2 (Alice) to F2's t = 3 (Alice) and F1's t = 3 (Bob) to
             F2's t = 2 (Bob).  This is the map the question asks about.

    phi_ORD  THE ORDER-PRESERVING RELABELLING.  t -> t.  This identifies
             'the first measurement in F1' with 'the first measurement in
             F2', which are DIFFERENT physical events, so it is NOT the
             Lorentz correspondence.  It is tested as the weakest
             steelman: if even an abstract order-preserving isomorphism
             of the two processes fails, no relabelling of any kind
             rescues them.
""")

PHI_LOR = {0: 0, 1: 1, 2: 3, 3: 2}
PHI_ORD = {0: 0, 1: 1, 2: 2, 3: 3}

GRAINS = [
    ("G-FULL", "every target time, every marginal, every column of every "
               "Gamma — the dynamical axiom read literally",
     (0, 1, 2, 3), True, False),
    ("G-DIV", "division-event times only (the intermediate target time "
              "t = 1 and its marginal DROPPED) — escape E1",
     (0, 2, 3), True, False),
    ("G-FIX", "the model's FIXED features only: the Gamma family, no "
              "marginals at all (p is contingent per the epistemic "
              "axiom) — escape E1'",
     (0, 1, 2, 3), False, False),
    ("G-SUPP", "reachable conditioning only: columns j with p_j(t') > 0, "
               "all marginals kept",
     (0, 1, 2, 3), True, True),
]

RESULTS = {}
DROPPED = {}
for _nm, _a, _b in SETTINGS:
    F1, F2 = FRAMES[(_nm, "F1")], FRAMES[(_nm, "F2")]
    for gname, gdesc, times, marg, live in GRAINS:
        for pname, phi in (("phi_LOR", PHI_LOR), ("phi_ORD", PHI_ORD)):
            t2 = tuple(sorted({phi[t] for t in times}))
            o1 = build_objs(F1, times, marg, live, phi=lambda t: phi[t])
            o2 = build_objs(F2, t2, marg, live, phi=None)
            c1, c2, d1, d2 = common_labels(o1, o2)
            DROPPED[(_nm, gname, pname)] = (d1, d2)
            NODES[0] = 0
            try:
                pi, why = find_iso(c1, c2)
            except RuntimeError as e:
                pi, why = None, f"CAP: {e}"
            RESULTS[(_nm, gname, pname)] = (pi, why, NODES[0], len(c1))
    tick(f"frame-map search done for {_nm}")

# ---- the initial-division-event content, i.e. E2 run properly -----------
# Denying the intermediate division event removes the CONDITIONING at
# t = 2; it does not remove the target times.  [B3] p.29 makes the
# dynamical law hold "for arbitrary target times", and p.10 makes the
# target time "a free variable", while the epistemic axiom supplies a
# standalone distribution "at any given target time".  So D = {0} with
# T = (0, 1, 2, 3) kept in full.
E2RES = {}
for _nm, _a, _b in SETTINGS:
    F1, F2 = FRAMES[(_nm, "F1")], FRAMES[(_nm, "F2")]
    for pname, phi in (("phi_LOR", PHI_LOR), ("phi_ORD", PHI_ORD)):
        times = (0, 1, 2, 3)
        t2 = tuple(sorted({phi[t] for t in times}))
        o1 = build_objs(F1, times, True, False, phi=lambda t: phi[t],
                        divs=(0,))
        o2 = build_objs(F2, t2, True, False, phi=None, divs=(0,))
        c1, c2, d1, d2 = common_labels(o1, o2)
        NODES[0] = 0
        try:
            pi, why = find_iso(c1, c2)
        except RuntimeError as e:
            pi, why = None, f"CAP: {e}"
        E2RES[(_nm, pname)] = (pi, why, NODES[0], len(c1))
    tick(f"initial-division-event (E2) search done for {_nm}")

print()
print("  THE LABEL INTERSECTION, FIRST — this is census item (iii), the")
print("  division-event sets themselves.  Under phi_LOR (the Lorentz")
print("  correspondence) F1 specifies a FORWARD leg matrix Gamma(3<-2) =")
print("  Gamma(B <- A) whose physical counterpart in F2 is the")
print("  RETRODICTIVE object Gamma(B <- A) = Gamma(2<-3), because in F2")
print("  Bob precedes Alice.  The two frames' division-event sets are in")
print("  bijection but their INDUCED ORDERS disagree on {A, B}, so the")
print("  forward inventories are not even index-matched.  The object is")
print("  DROPPED from the search below, which therefore compares only")
print("  what both frames specify in the same direction — the frame map's")
print("  best case.")
for _k in sorted(DROPPED, key=sk):
    d1, d2 = DROPPED[_k]
    if d1 or d2:
        print(f"    {_k[0]} {_k[1]} {_k[2]}: F1-only {d1}; F2-only {d2}")

print()
print("  THE FRAME-MAP SEARCH, COMPLETE OVER THE PERMUTATION CLASS L-1")
print("  FORCES.  '-' means NO permutation of the 36 configurations "
      "carries")
print("  F1's specified content onto F2's, at that grain and that time")
print("  correspondence.  'PI' means one exists and is verified.")
print()
print(f"    {'setting':8s} {'grain':8s} {'phi_LOR':>10s} {'phi_ORD':>10s}")
for _nm, _a, _b in SETTINGS:
    for gname, gdesc, times, marg, live in GRAINS:
        r1 = RESULTS[(_nm, gname, "phi_LOR")][0]
        r2 = RESULTS[(_nm, gname, "phi_ORD")][0]
        print(f"    {_nm:8s} {gname:8s} {('PI' if r1 else '-'):>10s} "
              f"{('PI' if r2 else '-'):>10s}")

EQ = ("SP-E", "SP-F")
_lor_ne = [k for k, v in RESULTS.items() if k[2] == "phi_LOR"
           and v[0] is not None and k[0] not in EQ]
_lor_eq = [k for k, v in RESULTS.items() if k[2] == "phi_LOR"
           and v[0] is not None and k[0] in EQ]
_ord_any = [k for k, v in RESULTS.items() if k[2] == "phi_ORD"
            and v[0] is not None]
_ord_ne = [k for k, v in RESULTS.items() if k[2] == "phi_ORD"
           and v[0] is not None and k[0] not in EQ]

check("T1 UNDER THE LORENTZ CORRESPONDENCE NO FRAME MAP EXISTS AT ANY "
      "GRAIN, AT EVERY SETTING PAIR WITH TWO DIFFERENT SETTINGS: the "
      f"complete search over all permutations of the {NC} configurations "
      f"returns empty in all {(len(SETTINGS)-len(EQ))*len(GRAINS)} "
      "(unequal setting pair x grain) cells.  By L-1(a) the admissible "
      "class is exactly the permutations, so this is a proof of "
      "non-existence, not a failure to find",
      not _lor_ne, f"unequal-setting cells with a map: {_lor_ne}")

check("T2 EVEN THE ORDER-PRESERVING STEELMAN FAILS WHENEVER THE TWO "
      "SETTINGS DIFFER: phi_ORD, which identifies 'first measurement' "
      "with 'first measurement' and is therefore NOT the Lorentz "
      "correspondence, also returns empty at every unequal setting pair "
      "and every grain.  So no relabelling of any kind — physical or "
      "abstract — relates the two frames' specified content there",
      not _ord_ne, f"unequal-setting cells with a map: {_ord_ne}")

check("T3 THE MACHINERY DOES FIND MAPS WHERE THEY EXIST, ON THIS VERY "
      "MODEL: at the two equal-setting pairs the search returns verified "
      "permutations in the cells printed above.  The negatives at "
      "unequal settings are therefore properties of the model, not of "
      "the search",
      len(_ord_any) > 0 and len(_lor_eq) > 0,
      f"phi_ORD cells with a map: {sorted(_ord_any)}; phi_LOR cells with "
      f"a map: {sorted(_lor_eq)}")

# ---- what the equal-setting maps actually do -----------------------------
S_PA_READY = frozenset(i for i in range(NC) if cfg(i)[2] == 0)
S_PB_READY = frozenset(i for i in range(NC) if cfg(i)[3] == 0)


def wing_action(pi):
    im_b = frozenset(pi[i] for i in S_PB_READY)
    if im_b == S_PB_READY:
        return "wing-preserving"
    if im_b == S_PA_READY:
        return "WING-EXCHANGING"
    return "neither"


def visited(F):
    """The configurations the model's own content actually visits."""
    out = set()
    for t in F.T:
        out |= {i for i in range(NC) if not F.p[t][i].is_zero()}
    return out


_wing = []
for _k in sorted(set(_lor_eq + _ord_any), key=sk):
    pi = RESULTS[_k][0]
    F1 = FRAMES[(_k[0], "F1")]
    vis = visited(F1)
    bad = [i for i in sorted(vis)
           if (i in S_PB_READY) != (pi[i] in S_PB_READY)]
    bad2 = [i for i in sorted(vis)
            if (i in S_PA_READY) != (pi[i] in S_PA_READY)]
    _wing.append((_k[0], _k[1], _k[2], wing_action(pi), len(bad), len(bad2),
                  cfg_str(bad[0]) + "->" + cfg_str(pi[bad[0]]) if bad
                  else None))
check("T3b EVERY MAP THE SEARCH FINDS AT EQUAL SETTINGS BREAKS THE "
      "IDENTITY OF THE TWO RECORD SECTORS, AND IS THEREFORE NOT A "
      "LORENTZ CORRESPONDENCE: on the configurations the model's own "
      "content actually visits, each returned permutation carries a "
      "configuration in which POINTER B IS STILL READY onto one in "
      "which it is not, and likewise for pointer A — it re-identifies "
      "which laboratory holds which record.  A boost relates two "
      "descriptions of the SAME two laboratories and does not exchange "
      "them.  The equal-setting cells are therefore the coincidence that "
      "at a = b the two wings carry interchangeable descriptions, not "
      "covariance",
      bool(_wing) and all(nb > 0 and nb2 > 0
                          for _, _, _, _, nb, nb2, _ in _wing),
      f"(setting, grain, phi, global action, #visited configs whose "
      f"pointer-B-ready status the map flips, same for pointer A, one "
      f"witness) = {_wing}")

for _k in sorted(RESULTS, key=sk):
    pi, why, nodes, nobj = RESULTS[_k]
    print(f"  [WHY] {_k[0]} {_k[1]} {_k[2]} ({nobj} objects compared): "
          f"{'MAP FOUND — ' if pi else ''}{why[:200]}")
report("search nodes used (max over all cells)",
       max(v[2] for v in RESULTS.values()))
report("search node cap", NODE_CAP)


# ===========================================================================
# SEC 8.  THE MISMATCH CENSUS
# ===========================================================================

sec("THE MISMATCH CENSUS — every object, exactly, under the Lorentz "
    "correspondence")

print("""
  L-1(b) makes the census sharper still.  A boost lives in a
  one-parameter subgroup isomorphic to (R,+); by L-1(b) its
  representation on the fixed finite C is the IDENTITY.  So the frame map
  is forced to be the identity on configurations, and the comparison is
  a literal one: does F1's object equal F2's corresponding object?

  Under phi_LOR the correspondence of objects is
     p(1) <-> p(1)                 [after prep, before either measurement]
     p(2) <-> p(3)                 [at Alice's measurement]
     p(3) <-> p(2)                 [at Bob's measurement]
     Gamma(2<-0) <-> Gamma(3<-0)   [prep to Alice]
     Gamma(3<-0) <-> Gamma(2<-0)   [prep to Bob]
     Gamma(3<-2) <-> ---           [F1's A-to-B leg; F2's B-to-A leg is
                                    its counterpart under phi_LOR only
                                    after the order reversal, censused
                                    separately below]
""")

CENSUS = []
for _nm, _a, _b in SETTINGS:
    F1, F2 = FRAMES[(_nm, "F1")], FRAMES[(_nm, "F2")]
    rows = []
    for t in (1, 2, 3):
        v1, v2 = F1.p[t], F2.p[PHI_LOR[t]]
        d = sum(1 for i in range(NC) if not (v1[i] - v2[i]).is_zero())
        s1 = sum(1 for i in range(NC) if not v1[i].is_zero())
        s2 = sum(1 for i in range(NC) if not v2[i].is_zero())
        rows.append((f"p({t}) vs p({PHI_LOR[t]})", d, s1, s2))
    for (t, tp) in ((2, 0), (3, 0)):
        G1 = F1.G[(t, tp)]
        G2 = F2.G[(PHI_LOR[t], PHI_LOR[tp])]
        d = sum(1 for i in range(NC) for j in range(NC)
                if not (G1[i][j] - G2[i][j]).is_zero())
        c1 = Counter(sum(1 for i in range(NC) if not G1[i][j].is_zero())
                     for j in range(NC))
        c2 = Counter(sum(1 for i in range(NC) if not G2[i][j].is_zero())
                     for j in range(NC))
        rows.append((f"Gamma({t}<-{tp}) vs Gamma({PHI_LOR[t]}<-"
                     f"{PHI_LOR[tp]})", d, dict(sorted(c1.items())),
                     dict(sorted(c2.items()))))
    G1 = F1.G[(3, 2)]
    G2 = F2.G[(3, 2)]
    d = sum(1 for i in range(NC) for j in range(NC)
            if not (G1[i][j] - G2[i][j]).is_zero())
    rows.append(("Gamma(3<-2) [F1 A-then-B leg] vs Gamma(3<-2) "
                 "[F2 B-then-A leg]", d, "second leg = U_B",
                 "second leg = U_A"))
    CENSUS.append((_nm, rows))

for _nm, rows in CENSUS:
    print(f"  ---- {_nm} " + "-" * 60)
    for r in rows:
        print(f"       {r[0]:52s} differing {r[1]:5d} | F1 {r[2]} | "
              f"F2 {r[3]}")
print()

# the basis-free certificate
_bf = []
for _nm, _a, _b in SETTINGS:
    F1, F2 = FRAMES[(_nm, "F1")], FRAMES[(_nm, "F2")]
    prA1 = sum((F1.p[2][i] for i in range(NC) if cfg(i)[3] == 0), K0)
    prA2 = sum((F2.p[3][i] for i in range(NC) if cfg(i)[3] == 0), K0)
    prB1 = sum((F1.p[3][i] for i in range(NC) if cfg(i)[2] == 0), K0)
    prB2 = sum((F2.p[2][i] for i in range(NC) if cfg(i)[2] == 0), K0)
    _bf.append((_nm, str(prA1), str(prA2), str(prB1), str(prB2)))
    report(f"{_nm}: Pr[pointer B still ready] at Alice's division event",
           f"F1 = {prA1}  |  F2 = {prA2}")

check("T4 UNDER THE IDENTITY FRAME MAP — THE ONE L-1(b) FORCES FOR A "
      "ONE-PARAMETER BOOST — THE MISMATCH HAS A BASIS-FREE CERTIFICATE "
      "IN THE POINTER SECTOR ALONE, AT EVERY SETTING PAIR INCLUDING THE "
      "EQUAL ONES: at the division event that IS Alice's measurement, F1 "
      "assigns probability exactly 1 to 'pointer B is still ready' and "
      "F2 assigns exactly 0; at the division event that IS Bob's, F1 "
      "assigns exactly 0 to 'pointer A is still ready' and F2 exactly 1. "
      " The pointer configurations are [B3]'s measurement-outcome "
      "configurations, which any [B3] model of a measurement must carry, "
      "so the certificate does not depend on the model's choice of "
      "configuration basis for the spin wings — and the six declared "
      "setting pairs span basis-aligned and basis-unaligned directions "
      "on both wings",
      all(x[1] == "1" and x[2] == "0" and x[3] == "0" and x[4] == "1"
          for x in _bf),
      f"per setting pair (Pr[pB=r] at A: F1, F2; Pr[pA=r] at B: F1, F2) "
      f"= {_bf}")

_sup = []
for _nm, _a, _b in SETTINGS:
    F1, F2 = FRAMES[(_nm, "F1")], FRAMES[(_nm, "F2")]
    s1 = sum(1 for i in range(NC) if not F1.p[2][i].is_zero())
    s2 = sum(1 for i in range(NC) if not F2.p[3][i].is_zero())
    _sup.append((_nm, s1, s2))
check("T5 AT UNEQUAL SETTINGS THE SEPARATING INVARIANT IS ELEMENTARY AND "
      "PERMUTATION-PROOF: the standalone distribution at Alice's "
      "division event has a different SUPPORT SIZE in the two frames at "
      "every unequal setting pair, and support size is invariant under "
      "any bijection of C.  No permutation can repair it, which is the "
      "one-line reason T1 is a non-existence proof.  At equal settings "
      "the support sizes coincide, which is why the equal-setting cells "
      "need the finer T3b argument instead",
      all(s1 != s2 for nm, s1, s2 in _sup if nm not in EQ)
      and all(s1 == s2 for nm, s1, s2 in _sup if nm in EQ),
      f"(setting, |supp p_F1(Alice)|, |supp p_F2(Alice)|) = {_sup}")

_idbad = []
for _nm, rows in CENSUS:
    for r in rows:
        if r[0].startswith("p(1)"):
            if r[1] != 0:
                _idbad.append((_nm, r[0], r[1]))
        elif r[1] == 0:
            _idbad.append((_nm, r[0], r[1]))
check("T6 THE L-1(b) BRANCH, STATED AS A LITERAL COMPARISON: with the "
      "identity as the frame map, EVERY corresponding object of the two "
      "frames differs — the two marginals at the two measurement "
      "division events, both prep-to-measurement transition matrices, "
      "and the second-leg matrix — at every setting pair, with the exact "
      "counts in the census above.  The single object that agrees is "
      "p(1), the marginal after preparation and before either "
      "measurement, which is where the two frames have not yet parted",
      not _idbad, f"objects violating the pattern: {_idbad}")


# ===========================================================================
# SEC 9.  THE ESCAPE-HATCH BATTERY
# ===========================================================================

sec("THE ESCAPE-HATCH BATTERY — each escape works at a stated cost or "
    "fails at a stated place")

print("""
  E1  DROP THE INTERMEDIATE-TIME MARGINALS (keep only division-event
      content).  Implemented as grain G-DIV: the target time t = 1 and
      its marginal are removed.
  E1' DROP ALL MARGINALS (keep only the model's FIXED features, since
      [B3]'s epistemic axiom makes p contingent).  Grain G-FIX.
  E2  DENY THAT THE FIRST MEASUREMENT GENERATES A DIVISION EVENT on the
      composite system, leaving D = {0} and only the final law.
  E3  SYSTEM-CENTRICITY: read the experiment as two wing-systems, each
      with its OWN division events, rather than as one composite.
  E4  A NON-GROUP (SEMIGROUP) COVARIANCE, the one loophole L-1 leaves
      open.
""")

_e1 = [k for k, v in RESULTS.items() if k[1] == "G-DIV"
       and k[2] == "phi_LOR" and v[0] is not None]
check("E1 DROPPING THE INTERMEDIATE-TIME MARGINALS DOES NOT RESTORE THE "
      "ISOMORPHISM — IT FAILS AT A STATED PLACE.  The dropped object is "
      "p(1), which is ALREADY identical in the two frames (nothing has "
      "happened but the preparation).  The mismatch sits at t = 2 and "
      "t = 3, which are DIVISION EVENTS and therefore survive the drop.  "
      "Grain G-DIV returns empty at every setting pair",
      not _e1, f"G-DIV cells with a map under phi_LOR: {_e1}")

_e1b = [k for k, v in RESULTS.items() if k[1] == "G-FIX"
        and k[2] == "phi_LOR" and v[0] is not None]
_colsup = []
for _nm, _a, _b in SETTINGS:
    F1, F2 = FRAMES[(_nm, "F1")], FRAMES[(_nm, "F2")]
    c1 = Counter(sum(1 for i in range(NC) if not F1.G[(2, 0)][i][j].is_zero())
                 for j in range(NC))
    c2 = Counter(sum(1 for i in range(NC) if not F2.G[(3, 0)][i][j].is_zero())
                 for j in range(NC))
    _colsup.append((_nm, dict(sorted(c1.items())), dict(sorted(c2.items()))))
check("E1' DROPPING ALL MARGINALS DOES NOT RESTORE IT EITHER — IT FAILS "
      "AT A STATED PLACE.  The transition matrices alone already "
      "separate: the column-support census of Gamma(2<-0) in F1 differs "
      "from that of Gamma(3<-0) in F2, and a column-support census is "
      "invariant under conjugation by a permutation.  Grain G-FIX "
      "returns empty at every setting pair",
      not _e1b, f"G-FIX cells with a map under phi_LOR: {_e1b}; "
                f"column-support censuses {_colsup}")

_e2 = []
for _nm, _a, _b in SETTINGS:
    F1, F2 = FRAMES[(_nm, "F1")], FRAMES[(_nm, "F2")]
    o1 = [("vec", ("p", 3), [kk(F1.p[3][i]) for i in range(NC)]),
          ("vec", ("init",), [kk(K1 if i == J0 else K0) for i in range(NC)]),
          ("mat", ("G", 3, 0), [[kk(F1.G[(3, 0)][i][j]) for j in range(NC)]
                                for i in range(NC)])]
    o2 = [("vec", ("p", 3), [kk(F2.p[3][i]) for i in range(NC)]),
          ("vec", ("init",), [kk(K1 if i == J0 else K0) for i in range(NC)]),
          ("mat", ("G", 3, 0), [[kk(F2.G[(3, 0)][i][j]) for j in range(NC)]
                                for i in range(NC)])]
    NODES[0] = 0
    pi, why = find_iso(o1, o2)
    _e2.append((_nm, pi is not None,
                verify_pi(list(range(NC)), o1, o2)))
check("E2 DENYING THAT THE FIRST MEASUREMENT GENERATES A DIVISION EVENT "
      "DOES RESTORE THE ISOMORPHISM — AT A STATED COST.  With "
      "D = {0} the whole specified content is Gamma(3<-0) and p(3), and "
      "the two frames agree on those with the IDENTITY as the frame map "
      "at every setting pair.  THE COST, exactly: (i) it contradicts "
      "[B3]'s own dynamical axiom (p.29, 'division events are generated "
      "during a measurement process'); (ii) it removes the only "
      "conditioning the model has after preparation, so the framework "
      "can no longer describe the post-measurement update at all; "
      "(iii) it makes the process trivially divisible over the "
      "remaining single interval",
      all(ok and idmap for nm, ok, idmap in _e2),
      f"(setting, map exists, map is the identity) = {_e2}")

# ---- E3: system-centricity ----------------------------------------------
print()
print(f"  E3 CITES BC1's PIN AND DOES NOT DUPLICATE IT "
      f"({QUOTES['bc1-pin'][0]}).  BC1 owns the subsystem-lattice")
print("  consistency question; BC2 asks only the narrow two-frame")
print("  question about the wing-local descriptions of THIS model.")


def wing_marg(F, t, wing):
    """The wing's own configuration marginal: 6 cells (spin x pointer)."""
    out = [K0] * 6
    for i in range(NC):
        qA, qB, pA, pB = cfg(i)
        idx = (qA * 3 + pA) if wing == "A" else (qB * 3 + pB)
        out[idx] = out[idx] + F.p[t][i]
    return out


_e3_own, _e3_other = [], []
for _nm, _a, _b in SETTINGS:
    F1, F2 = FRAMES[(_nm, "F1")], FRAMES[(_nm, "F2")]
    # each wing evaluated at ITS OWN division events (and t=1, and after)
    dA1, dA2 = 2, 3          # Alice's measurement time in F1 / F2
    dB1, dB2 = 3, 2          # Bob's
    okA = all((x - y).is_zero() for x, y in
              zip(wing_marg(F1, dA1, "A"), wing_marg(F2, dA2, "A")))
    okB = all((x - y).is_zero() for x, y in
              zip(wing_marg(F1, dB1, "B"), wing_marg(F2, dB2, "B")))
    ok1 = all((x - y).is_zero() for x, y in
              zip(wing_marg(F1, 1, "A"), wing_marg(F2, 1, "A")))
    _e3_own.append((_nm, okA, okB, ok1))
    # the same wing evaluated at the OTHER system's division event
    crA = all((x - y).is_zero() for x, y in
              zip(wing_marg(F1, dB1, "A"), wing_marg(F2, dB2, "A")))
    _e3_other.append((_nm, crA))

check("E3a SYSTEM-CENTRICITY WORKS FOR THE WING-LOCAL CONTENT: each "
      "wing's own configuration marginal, evaluated at that wing's OWN "
      "division event, is exactly identical in the two frames, at every "
      "setting pair — 6 exact identities per wing per setting pair.  "
      "This is the pin's pre-registered positive, and it holds, but only "
      "at this grain",
      all(a and b and c for nm, a, b, c in _e3_own),
      f"(setting, wing A at its own event, wing B at its own event, "
      f"both at t=1) = {_e3_own}")

check("E3b AND IT FAILS THE MOMENT A WING IS EVALUATED AT THE OTHER "
      "SYSTEM'S DIVISION EVENT: wing A's marginal at the time of BOB's "
      "measurement differs between the frames at every setting pair, "
      "because in F1 that time is after Alice's measurement and in F2 it "
      "is before.  So the escape buys frame-invariance only by refusing "
      "to place the two wings on any common time",
      not any(cr for nm, cr in _e3_other),
      f"(setting, wing A agrees at Bob's event) = {_e3_other}")

_e3c = []
for _nm, _a, _b in SETTINGS:
    F1 = FRAMES[(_nm, "F1")]
    joint, mA, mB = outcome_stats(F1)
    prodA = {(al, be): mA[al] * mB[be] for al in (1, -1) for be in (1, -1)}
    same = all((joint[k] - prodA[k]).is_zero() for k in joint)
    _e3c.append((_nm, same))
check("E3c THE COST OF E3, STATED EXACTLY: the wing-local descriptions "
      "do not carry the model's correlation content.  The product of the "
      "two wing-local outcome marginals differs from the composite's "
      "outcome joint at EVERY declared setting pair, so the joint is not "
      "recoverable from the two frame-invariant wing descriptions.  The "
      "description that carries the correlations is the composite one — "
      "and the composite one is exactly the description T1 shows is not "
      "frame-mappable",
      all(not same for nm, same in _e3c),
      f"(setting, wing marginals reproduce the joint) = {_e3c}")

print()
print(f"  E4 THE ONE LOOPHOLE L-1 LEAVES OPEN, NAMED AND LEFT OPEN.")
print(f"  L-1's scope guard ({QUOTES['L1-scope'][0]}), verbatim:")
print(f'    "{QUOTES["L1-scope"][1]}"')
print("  This unit's frame change is a GROUP: F1 -> F2 -> F1 is the")
print("  identity, so L-1(a) derives invertibility and the permutation")
print("  class is complete.  A covariance carried by a SEMIGROUP or by a")
print("  non-group action is NOT tested here and is NOT excluded here.")
print("  No LP/Farkas search over such maps is run (declared in the")
print("  caps).  E4 is therefore neither a working escape nor a failing")
print("  one in this receipt: it is OPEN.")


# ===========================================================================
# SEC 10.  THE VERDICT AND THE L-1 LADDER
# ===========================================================================

sec("THE VERDICT, AND ITS PLACE ON L-1's LADDER")

if _lor_ne:
    VERDICT = "R-COVARIANT"
elif not _lor_eq:
    VERDICT = "R-FOLIATED"
elif all(nb > 0 and nb2 > 0 for _, _, _, _, nb, nb2, _ in _wing):
    VERDICT = "R-FOLIATED"
else:
    VERDICT = "R-CONDITIONAL"

print(f"""
  PRE-REGISTERED OUTCOME REACHED: {VERDICT}

  THE OUTCOME IN ONE SENTENCE.  The two frames' specified content is NOT
  frame-isomorphic: at every setting pair with two different settings no
  permutation of the {NC} configurations carries F1's specified content
  onto F2's, at any of the four declared grains, under either time
  correspondence; and at the two equal-setting pairs the only maps that
  exist EXCHANGE THE TWO WINGS' RECORD SECTORS, which a boost does not
  do.  The outcome statistics are identical in the two frames, exactly.
  The ontology therefore requires a foliation while the statistics do
  not.

  WHAT ACTS, ON WHAT SET, INVERTIBLY OR NOT (L-1 C4):
    the frame change F1 <-> F2; the model's one fixed finite
    configuration space C of {NC} configurations; and invertibly, because
    the frame change is a group and L-1(a) derives invertibility inside a
    group action.

  L-1's LADDER ({QUOTES['L1-ladder'][0]}):
    RUNG 1  exact stochastic covariance — EXCLUDED by L-1, and this unit
            exhibits the exclusion CONCRETELY on a [B3] Bell model: the
            forced map class (permutations by L-1(a), the identity by
            L-1(b)) is searched completely and is empty at every setting
            pair with two different settings, at every grain, under
            either time correspondence; and at equal settings the only
            surviving maps break the identity of the two record sectors
            (T3b), which a boost does not do.
    RUNG 2  sprinkling-grade statistical covariance on a finite-valency
            generated carrier — NOT TOUCHED.  There is no generated
            carrier in this program.
    RUNG 3  order-level covariance — NOT TOUCHED, and note that this
            unit's mismatch is partly an ORDER fact (the division-event
            set's induced order is reversed on {{A, B}} by the physical
            identification), so rung 3 is not available as a rescue for
            this model without a separate argument this unit does not
            supply.

  WHAT SURVIVES, NAMED IN PAPER 8's LIST ({QUOTES['L1-admissible'][0]}):
    ADMISSIBLE FORM 1 — "equality ... of declared finite-battery
    statistics for sampled Lorentz-related tests" — holds here EXACTLY,
    not merely approximately: the declared outcome battery (4 joint
    outcome probabilities and 4 marginals per setting pair) is identical
    in the two frames at all {len(SETTINGS)} setting pairs, and the whole
    final-time law Gamma(3<-0) and p(3) agree entry by entry.  Form 2
    (projective compatibility of batteries at different refinements) is
    not exercised.  Form 3 (imported continuum covariance) is not used.

  THE SPARSITY HYPOTHESIS, SETTLED FOR THIS MODEL: the framework's
  refusal to specify a Kolmogorov tower does not help, because the
  objects that fail to correspond are not tower objects.  They are the
  single-time standalone distribution at a division event and the
  division-event transition matrices — the SPARSEST content the framework
  has.  [B3] is sparser than its predecessors in the tower direction and
  exactly as rich as they are in the slice direction, and it is the slice
  direction the frame change acts on.
""")

report("verdict", VERDICT)
report("mismatch localisation",
       "the intermediate division event of the COMPOSITE system; the "
       "final-time law and the whole outcome battery agree exactly")
report("QM control", "PASS" if not CONTROL_FAIL else "FAIL")
report("anchors", "PASS" if not ANCHOR_FAIL else "FAIL")
report("sign-oracle bisection steps used (max)", max(SIGN_STEPS[0], 120))
report("search nodes (max over cells)", max(v[2] for v in RESULTS.values()))
report("caps", "; ".join(f"{k}: {v}" for k, v in CAPS.items()))

print()
print("-" * 78)
print(f"  gates: {PASS} pass, {FAIL} fail; anchor failures {ANCHOR_FAIL}; "
      f"control failures {CONTROL_FAIL}")
print(f"  runtime: {time.time() - T0:.1f}s")
print("-" * 78)

if ANCHOR_FAIL or CONTROL_FAIL:
    print("  EXIT 1 — anchor or QM control failure (the model would be "
          "wrong, not the finding).")
    sys.exit(1)
print("  EXIT 0 — substantive result delivered; negatives exit 0 by the "
      "house rule.")
sys.exit(0)
