#!/usr/bin/env python3
"""
u3_unistochasticity_screen_exact.py — v11 U3: THE UNISTOCHASTICITY SCREEN,
the loop-class reproduction, and the gauge candidate.

Pin: v11/note-u3-unistochasticity-screen-pin.md (STRICT, frozen before this
file existed).  Binding specification: paper 0 (v11) sec.7 (U3), sec.5 (the
gauge stratum), sec.6; [V11-CAT] sec.7 rank 4 and its sec.3/sec.4 graded
entries; U1's sec.11 handover and sec.6 sharpening.  Parents: v10 paper 31
sec.4.3 (the K1 arbitration operators), the D75 Barandes audit pin (b)
(the Zhat sibling's specification and the screen's shape), D74 (the
transport loop census, group <2,3>, R+, odd sector empty), D71b / v7
paper 30 (the i-twist amplitude form), v6 paper 7 Thms 7.1 and D3 (the
U(1) loop-class theorem), LD (the walled odd sector).

THE THREE ARMS
  ARM A  THE SCREEN.  Every committed generated matrix named by the pin is
         put through: (i) the doubly-stochastic precondition, exact
         rationals, with the exact per-column excess/deficit printed on
         every failure; (ii) for DS passers, unistochasticity decided at
         its own size -- n = 2 by a CONSTRUCTED real orthogonal
         certificate, n = 3 by the exact triangle (chain-link)
         discriminant, every n by the general polygon obstruction and by
         explicit certificate construction.  Every positive verdict in
         this receipt carries an EXHIBITED unitary, verified entry by
         entry in exact algebraic arithmetic; no positive verdict rests on
         a cited criterion.
  ARM B  THE LOOP-CLASS REPRODUCTION.  v6 paper 7 Thm D3 / Thm 7.1
         restated from the committed file, and its three clauses tested
         one by one on D74's committed generated carrier.
  ARM C  THE GAUGE CANDIDATE.  [B3] eqs. (29)/(30) (Schur-Hadamard gauge)
         applied to the Arm-A passers; the triviality gated honestly; the
         unitarity-preserving subgroup exhibited as PROPER on our own
         passer; and the census of whether any committed generated
         quantity selects a non-trivial phase.

ENGRAVED CONSTRAINTS (paper 0 sec.6, carried into every gate text)
  * MATRIX-LEVEL SCREENING ONLY.  Nothing here claims that a passing
    matrix IS a quantum system.  Correspondence is not identity; the map
    from a screened matrix to a physical system is missing and is not
    supplied by this unit.
  * No CP-divisibility framing, no Bell framing, no locality framing.
  * No covariance claim: L-1's bound stands untouched.
  * Lean: NONE.  Every pre-registered outcome of the pin is reportable.

HOUSE RULES OBSERVED
  * Exact arithmetic end to end: fractions.Fraction for every probability
    and matrix entry; Q(sqrt d) (class Surd) for real orthogonal
    certificates; the cyclotomic fields Q(zeta_8) and Q(zeta_12)
    (class Cyc) for complex unitary certificates.  No float appears in any
    substantive computation, and no tolerance is used anywhere.
  * Committed layers are single-sourced by AST extraction and text-slice
    with an AST signature pass; exit-freedom gated.
  * Substantive negatives exit 0.  exit 1 is reserved for ANCHOR failure.
  * Determinism: every printed census is ordered by the hash-seed-
    independent key sk().
"""

from __future__ import annotations

import ast
import math
import os
import sys
import time
import types
from collections import Counter, defaultdict
from fractions import Fraction as Fr
from itertools import permutations, product

T0 = time.time()
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(REPO)                 # .../isp  (run from anywhere)
os.chdir(REPO)
sys.setrecursionlimit(200000)

PASS = FAIL = 0
ANCHOR_FAIL = 0
SECT = [0]
COROLLARY = []


def sec(title):
    SECT[0] += 1
    print()
    print("-" * 78)
    print(f"SEC {SECT[0]}  {title}   [+{time.time() - T0:.0f}s]")
    print("-" * 78)


def check(label, ok, detail="", corollary_of=None):
    """corollary_of: the gate is entailed by its own definitions or is
    true of every object of its type.  Run and printed but NOT counted as
    independent evidence (the D72 MODERATE-4 discipline, carried)."""
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS += int(bool(ok))
    FAIL += int(not ok)
    if corollary_of is not None:
        COROLLARY.append(label.split(":")[0].split("  ")[0])
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))
    if corollary_of is not None:
        print(f"         ^ NO INDEPENDENT INFORMATION: {corollary_of}")
    return bool(ok)


def anchor(label, ok, detail=""):
    global ANCHOR_FAIL
    if not check("ANCHOR " + label, ok, detail):
        ANCHOR_FAIL += 1
    return bool(ok)


def report(label, value):
    print(f"  [DATA] {label}: {value}")


def sk(o):
    """Hash-order-independent total key (D72's stable_key, re-derived)."""
    if isinstance(o, (frozenset, set)):
        return ("S", tuple(sorted(sk(x) for x in o)))
    if isinstance(o, (tuple, list)):
        return ("T", tuple(sk(x) for x in o))
    return ("V", type(o).__name__ + "|" + repr(o))


def fmt(counter):
    return {str(k): v for k, v in sorted(counter.items(),
                                         key=lambda z: sk(z[0]))}


def fsl(xs):
    return "[" + ", ".join(str(x) for x in xs) + "]"


# ===========================================================================
# SEC 0.  THE REGISTRY — every constant a gate tests against, with provenance
# ===========================================================================

print("=" * 78)
print("u3_unistochasticity_screen_exact.py — v11 U3")
print("THE UNISTOCHASTICITY SCREEN, THE LOOP-CLASS REPRODUCTION, AND THE")
print("GAUGE CANDIDATE")
print("=" * 78)
print("  banner: EXACT arithmetic end to end and NO TOLERANCE ANYWHERE.")
print("          Rationals: fractions.Fraction.  Real algebraic: class Surd")
print("          (Q-span of sqrt d, d squarefree), with an exact sign")
print("          oracle.  Complex algebraic: class Cyc (Q[x]/Phi_N(x) for")
print("          N = 8 and N = 12), with exact conjugation.")
print("  scope : MATRIX-LEVEL SCREENING ONLY.  A matrix that passes the")
print("          screen is not thereby a quantum system: the map from a")
print("          screened matrix to a physical system is MISSING and this")
print("          unit does not supply it.  Correspondence is not identity.")
print("  lean  : NONE.  S-PASS, S-FAIL-DS and S-FAIL-UNI are all")
print("          reportable outcomes and the census is the result.")

QUOTES = {
    "B3-uni": (
        "[B3] Barandes, 'Quantum Systems as Indivisible Stochastic "
        "Processes', arXiv:2507.21192, the paragraph following eq. (64); "
        "PDF read in-session",
        "In general, an N x N matrix is called UNISTOCHASTIC if its "
        "individual entries are expressible as the modulus-squares of the "
        "corresponding entries of an N x N unitary matrix.  It follows "
        "that (64) is just the statement that the system's transition "
        "matrix Gamma(t<-0) can be taken to be unistochastic.",
    ),
    "B3-gauge": (
        "[B3] eqs. (29)/(30) and the paragraph after (64)",
        "(30): Theta_ij(t<-0) |-> Theta_ij(t<-0) e^{i theta_ij(t)} is a "
        "Schur-Hadamard gauge transformation and has no physical effects. "
        " AND: 'Note that a unitary time-evolution operator U(t<-0) will "
        "NOT GENERICALLY REMAIN UNITARY under arbitrary Schur-Hadamard "
        "gauge transformations (30).  Hence, writing a unistochastic "
        "transition matrix Gamma(t<-0) in terms of a unitary "
        "time-evolution operator U(t<-0) corresponds to making a gauge "
        "choice.'",
    ),
    "B3-dilation": (
        "[B3] sec.3.5 (Stinespring dilation and unitarity), indexed at "
        "v11/relativistic-isp-v11-paper0-the-indivisible-record-law.md"
        ":520-528; the clause supplied and verified in the U3 round",
        "a quantum system is EITHER a unistochastic process itself, OR "
        "(if a nontrivial dilation was required) a SUBSYSTEM of a "
        "unistochastic process.  The screen in this receipt decides the "
        "FIRST disjunct only: it is a CLOSED, UNDILATED screen, and a "
        "negative verdict leaves the subsystem disjunct untouched.",
    ),
    "B3-conv": (
        "[B3] eqs. (9), (24), (26)",
        "Barandes' Gamma is COLUMN-stochastic: Gamma_ij(t<-0) = "
        "p(i,t | j,0) and sum_i Gamma_ij = 1.  The corpus's generated "
        "Zhat is ROW-stochastic.  Both readings are screened below; the "
        "doubly-stochastic precondition is exactly the statement that the "
        "choice of convention does not matter.",
    ),
    "p31-4.3": (
        "v10/relativistic-isp-v10-paper31-four-decisions-at-the-joints.md"
        ":496-524 (sec.4.3)",
        "V_single (2 x 1) on singleton components, deterministic branch; "
        "V_pair (4 x 1) on the 2-conflict; both factors of each isometric; "
        "Born = the committed kernel -- the squared branch amplitudes of "
        "V_pair are exactly 1/2-1/2 (the K1 law on the 2-conflict); menu "
        "reconstruction 1/4 early and 1/4 + 1/8 + 1/8 at the join.  AND "
        "ITS OWN SCOPE LINE, QUOTED IN FULL: 'Scope: the PAIR-PLUS-PATH "
        "FIXTURE, grammar = the terminal admission layer plus the click "
        "refinement; realized component sizes at the two cuts are exactly "
        "{1, 2} and the constructed family covers precisely those.'  The "
        "{1, 2} is therefore a fact about a TWO-ACTOR FIXTURE, not about "
        "the grammar.",
    ),
    "u3-round-B1": (
        "the U3 hostile round on commit 6c3e550, blocker B1 -- the "
        "reviewer's independent enumeration of the COMMITTED d42b1 "
        "(A,B,C) depth-<=3 family (v10/code/d42b1_transport_exact.py, "
        "pool declared at :435)",
        "the committed ABC3 family carries multiplicity-3 admissible "
        "arbitration events: census by |ckey| = {1: 3096, 2: 1536, "
        "3: 216}; first witness at depth 3 is [('p','A',v0,0), "
        "('p','B',v0,0), ('p','C',v0,1)] with committed menu weights 1/6 "
        "and 1/12 and committed K1 law {A0,B0} -> 2/3, {C1} -> 1/3.  "
        "Every number in this entry is RE-MEASURED from the layer below "
        "and gated.  ROUND-VERIFIED BUT NOT RE-RUN HERE (cited, not "
        "receipt-gated): the (A,B,C,D) depth-<=4 extension, 332,697 "
        "histories, |MIS| census {1: 232264, 2: 98304} -- never 3.",
    ),
    "u1-zhat": (
        "v11/note-u1-indivisibility-census.md:173-200 (sec.3) and :809-813 "
        "(sec.14, the handover to U3)",
        "the 6x6 Zhat transfer Zhat(i->j) = T_ij f_j / (lambda f_i) with "
        "T f = 2 f exactly, f = (4,4,3,7,3,3)/3; every row sums to exactly "
        "1; conflict row exactly {0: 1/7, 3: 3/4, 5: 3/28}; column sums "
        "25/28, 1, 59/64, 55/64, 31/32, 19/14 -- reported and left for U3 "
        "to adjudicate.",
    ),
    "u1-armc2": (
        "v11/note-u1-indivisibility-census.md:436-456 (sec.5.5, ARM-C2)",
        "under the payload-enriched map the renewal supports are 8, 8, 8 "
        "and the joint law over (cfg@r1, cfg@r2, cfg@r3) is exactly "
        "uniform (1/512 on all 512 cells), so the renewal chain is i.i.d. "
        "uniform on 8 labels and Gamma(r2<-r1) is COLUMN-CONSTANT (every "
        "entry 1/8).",
    ),
    "d75-5.3": (
        "v10/note-d75-barandes-audit.md:776-786 (sec.5.3, Arm 1)",
        "Unistochastic => doubly stochastic => uniform stationary law for "
        "an irreducible chain.  [MY READING]: a chain with that structure "
        "will not have a uniform stationary law, hence is NOT doubly "
        "stochastic, hence not unistochastic.  Cheap, and decisive in the "
        "negative direction.",
    ),
    "d75-D1guard": (
        "v10/note-d75-barandes-audit.md:737-747 (sec.5.2) and "
        "[V11-CAT]:3076, :3165-3168",
        "Thm D1 is the ancilla-summed Stinespring/Naimark dilation on "
        "C^{d^2}, which EVERY stochastic matrix admits; Barandes' "
        "Gamma_ij = |U_ij|^2 on C^d is a genuine restriction and is "
        "untested.  U3 must open by setting Thm D1 aside.",
    ),
    "p7-7.1": (
        "v6/relativistic-isp-v6-paper7.md:612-618 (Theorem 7.1)",
        "The retained holonomy of a closed route pair on a sealed screen "
        "is valued in the holonomy group of the 2-dimensional screen "
        "plane: the defect-free rotation group SO(2) = U(1) with canonical "
        "period 2*pi.  A retained alternative therefore carries "
        "canonically a nonnegative RN weight and a U(1) phase: the value "
        "space of an alternative is R+ x U(1) cup {0} = C as a SET.",
    ),
    "p7-D3": (
        "v6/relativistic-isp-v6-paper7.md:676-689 (Theorem D3)",
        "Under the record-relabeling gauge U -> D U D^dagger (diagonal "
        "phases), the Bargmann loop products B(l) = prod_k U_{i_{k+1} i_k} "
        "are invariant (machine 0.0e+00), and two-route interference is "
        "exactly the loop-phase law P = |A|^2 + |B|^2 + 2|A||B| "
        "cos(arg B(loop)) (machine gap 2.8e-17).  Hence the "
        "gauge-invariant content of the dilation is its loop class.",
    ),
    "p30-form": (
        "v7/relativistic-isp-v7-paper30-rooted-boundary-law.md:2846-2855, "
        ":4191, as catalogued at [V11-CAT] sec.4.6 (:2003-2061)",
        "the survivor, at dual-conjugation error exactly 0: "
        "A(R) ~ e^{-K(E)} . e^{i Phi(O)} -- real decay on the "
        "reversal-EVEN channel E, phase on the reversal-ODD channel O.  "
        "Never lifted to a theorem; v10 was built without it.",
    ),
    "T6.1": (
        "v10/note-d72-weld-result.md:150 (sec.1 T6.1), quoted verbatim by "
        "v10/code/d74_transport_holonomy_exact.py:161-170",
        "(A,B) d <= 4: 88 of 1,546 closed squares non-unit, spectrum "
        "{1/2: 70, 2/3: 2, 3/2: 6, 2: 10}, kinds {(r,d): 68, (d,r): 8, "
        "(d,n): 6, (d,d): 4, (n,d): 2}, delivery-bearing 88/88, "
        "shallowest defect at total depth 3.  (A,B,C) d <= 3: 12 of "
        "1,554, spectrum {1/2: 12}, kinds {(r,d): 12}.",
    ),
    "T6.2": (
        "v10/note-d72-weld-result.md:151 (sec.1 T6.2)",
        "(A,B) d <= 4: 40 half-open (AB-only 28, BA-only 12).",
    ),
    "d74-group": (
        "v10/note-d74-transport-holonomy-result.md:97-98, :227",
        "the transport holonomy group is <2,3>, free abelian of rank 2, "
        "the FULL group of 3-smooth positive rationals, index 1 in Z^2; "
        "value set {1/2, 2/3, 3/2, 2} at every scope run.",
    ),
    "d74-D2": (
        "v10/note-d74-transport-holonomy-result.md:248 (gate D2), and "
        ":107-109",
        "every committed weight is a positive rational, so every holonomy "
        "is; the only positive rational of modulus 1 is 1.  A U(1) part of "
        "a rational-valued holonomy could only ever be the sign -1, and "
        "-1 is realised nowhere.  'This settles the scalar odd sector A "
        "PRIORI, in one line, BEFORE ANY FIXTURE IS RUN.'  U3 therefore "
        "CONFIRMS D2 on a new object; it does not sharpen it.",
    ),
    "d74-D5.2": (
        "v10/code/d74_transport_holonomy_exact.py:2313-2325 (gate D5.2); "
        "v10/note-d74-transport-holonomy-result.md:110-112",
        "of all 304 linear extensions of the opposite poset of the 176 "
        "defective endpoints, 0 are admissible; and the grammar is not "
        "reversal-blocking (2,196 of 3,092 closed-square endpoints ARE "
        "reverse-admissible), so the 0 is a property of the defect locus.",
    ),
    "d74-carrier": (
        "v10/note-d74-transport-holonomy-result.md:190-191 (the carrier "
        "table)",
        "AB4: 113 menu classes, 185 congruence classes, 44 of 88 "
        "defective squares closed by both, split 44 curvature-type + 44 "
        "descent-obstruction-type; ABC3: 117 / 162, 0 of 12 closed.",
    ),
    "ld-662": (
        "v11/note-ld-last-door.md:1, :64-69",
        "the reversed record of every holonomy-carrying loop (662/662, "
        "four arms), of the Born = K1 arbitration row, and of all 40 "
        "committed half-open squares is refused at admission.",
    ),
    "cat-4.7": (
        "[V11-CAT] v11/note-v11p0a-reproduction-catalog.md:2094-2097 "
        "(sec.4.7(c))",
        "the odd-ring parity class is LABEL-holonomy (free relabelling "
        "trivialises it, and it 'may not be cited as a candidate for "
        "Phi(O)').",
    ),
    "u1-closed": (
        "v11/note-u1-indivisibility-census.md:174-179 (sec.3)",
        "the closed-scope family reproduces d43b's census "
        "[1,7,39,215,1191,6471,34375]; the uniform-lookahead intrinsic "
        "partition stabilises at six states at lookahead 2 (tables "
        "[4,4,5,5,5] / [4,5,6,6] / [4,5,6]); the exact 6x6 transfer has "
        "row sums (2,2,2,5/2,2,2) on all 215 depth-<=3 members.",
    ),
    "lit-uni3": (
        "LITERATURE.  Au-Yeung and Poon, 'A remark on the convexity and "
        "positive definiteness concerning Hermitian matrices', SEA Bull. "
        "Math. 3 (1979) 85-92 (the 3x3 characterisation); H. Nakazato, "
        "'Set of 3x3 orthostochastic matrices', Nihonkai Math. J. 7 "
        "(1996) 83-100; I. Bengtsson, A. Ericsson, M. Kus, W. Tadej, K. "
        "Zyczkowski, 'Birkhoff's polytope and unistochastic matrices, "
        "N=3 and N=4', Commun. Math. Phys. 259 (2005) 307-324.  The "
        "corpus's own floating-point implementation of the same criterion "
        "is v8/code/f6_unistochastic_record_blind_probe.py:224-246, run "
        "on textbook fixtures only at "
        "v8/code/p18_seal_divisibility.py:318-362.",
        "A bistochastic 3x3 matrix is unistochastic iff its unitarity "
        "TRIANGLE closes: the three phasors of modulus sqrt(B_ip B_iq), "
        "i = 1,2,3, arising from the orthogonality of columns p and q, "
        "must be able to sum to zero -- i.e. must satisfy the triangle "
        "inequality.",
    ),
    "lit-sqrtind": (
        "LITERATURE.  A. S. Besicovitch, 'On the linear independence of "
        "algebraic roots', J. London Math. Soc. 15 (1940) 3-6; standard "
        "Galois theory.",
        "The set {sqrt d : d a squarefree positive integer} (including "
        "d = 1) is linearly independent over Q.  Hence a Q-linear "
        "combination of such radicals is zero iff every coefficient is "
        "zero -- which is this receipt's exact zero test for class Surd.",
    ),
    "lit-had": (
        "LITERATURE.  J. J. Sylvester, 'Thoughts on inverse orthogonal "
        "matrices...', Phil. Mag. 34 (1867) 461-475; standard.",
        "Sylvester's construction H_{2^k} = H_2^{tensor k} gives a real "
        "Hadamard matrix of every order 2^k with H H^T = 2^k I, so the "
        "flat 2^k x 2^k matrix J/2^k is ORTHOSTOCHASTIC.  The flat 3x3 "
        "matrix J/3 is unistochastic (the 3-point DFT) but NOT "
        "orthostochastic -- the canonical exhibit of the ortho/uni gap.",
    ),
}

ANCH = {
    # Arm 0 / the K1 layer (paper 31 sec.4.3, U1 sec.3)
    "born_pair": [Fr(1, 2), Fr(1, 2)],
    "born_single": [Fr(1)],
    "menu_early_sum": Fr(1, 4),
    "menu_join": [Fr(1, 4), Fr(1, 8), Fr(1, 8)],
    "full_sum_early": Fr(1),
    "full_sum_join": Fr(5, 4),
    # the Zhat sibling (U1 sec.3 / d43b / d49)
    "closed_census": [1, 7, 39, 215, 1191, 6471, 34375],
    "Pt_tables": {2: [4, 4, 5, 5, 5], 3: [4, 5, 6, 6], 4: [4, 5, 6]},
    "T_rowsums": [Fr(2), Fr(2), Fr(2), Fr(5, 2), Fr(2), Fr(2)],
    "f_perron": [Fr(4, 3), Fr(4, 3), Fr(1), Fr(7, 3), Fr(1), Fr(1)],
    "lam": Fr(2),
    "conflict_row": {0: Fr(1, 7), 3: Fr(3, 4), 5: Fr(3, 28)},
    "zhat_colsums": [Fr(25, 28), Fr(1), Fr(59, 64), Fr(55, 64),
                     Fr(31, 32), Fr(19, 14)],
    # ARM-C2 (U1 sec.5.5) — the degenerate control, taken by SPECIFICATION
    "armc2_labels": 8,
    "armc2_entry": Fr(1, 8),
    # D72/D74 (T6.1, T6.2, the carrier table, the group)
    "AB_hist": 3969, "AB_closed": 1546, "AB_defects": 88,
    "AB_full_ratios": {Fr(1): 1458, Fr(1, 2): 70, Fr(2): 10,
                       Fr(2, 3): 2, Fr(3, 2): 6},
    "AB_kinds": {("r", "d"): 68, ("d", "r"): 8, ("d", "n"): 6,
                 ("d", "d"): 4, ("n", "d"): 2},
    "AB_bothblocked": 142, "AB_halfopen": 40,
    "AB_ABonly": 28, "AB_BAonly": 12, "AB_mindepth": 3,
    "ABC_hist": 3424, "ABC_closed": 1554, "ABC_defects": 12,
    "ABC_full_ratios": {Fr(1): 1542, Fr(1, 2): 12},
    "ABC_kinds": {("r", "d"): 12},
    "AB_seen": 44, "AB_unseen": 44,
    "AB_menu_cls": 113, "AB_cong_cls": 185,
    "ABC_seen": 0, "ABC_unseen": 12,
    "ABC_menu_cls": 117, "ABC_cong_cls": 162,
    "d74_values": {Fr(1, 2), Fr(2, 3), Fr(3, 2), Fr(2)},
    "d74_primes": [2, 3], "d74_rank": 2, "d74_index": 1,
    "d74_selfloops_AB4": 44,
    # the multiplicity census — the round's blocker B1 [u3-round-B1]
    "ABC3_ckey_census": {1: 3096, 2: 1536, 3: 216},
    "mult3_menu": [Fr(1, 6), Fr(1, 12)],
    "mult3_law": [Fr(1, 3), Fr(2, 3)],
    "mult3_gamma_colsums": [Fr(4, 3), Fr(2, 3)],
    "mult3_price": Fr(2, 3),
    "mis_max": 2,
    "prop_values": 2,
}

print()
print("  THE REGISTRY — every constant a gate tests against, with its")
print("  path:line provenance.  No bare constants appear in any predicate.")
for _k in sorted(QUOTES):
    _src, _txt = QUOTES[_k]
    print(f"    [{_k}] {_src}")
print(f"  ANCHOR constants: {len(ANCH)} entries, all quoted above.")

CAPS = {
    "closed scope (d42b3) family for the Zhat sibling": "depth <= 6",
    "D74 anchor arms": "(A,B) depth <= 4 and (A,B,C) depth <= 3",
    "multiplicity / outcome-space census": "THREE pools, receipt-gated: "
                                           "d42b1 (A,B,C) depth <= 3, "
                                           "d42b1 (A,B) depth <= 4, d42b3 "
                                           "closed scope (A,B) depth <= 6. "
                                           " A FOURTH — (A,B,C,D) depth "
                                           "<= 4, 332,697 histories — is "
                                           "round-verified and CITED, not "
                                           "re-run here [u3-round-B1]",
    "unistochasticity decided constructively at": "n = 1, 2, 3, 6, 8",
    "n = 3 exact criterion": "the triangle (chain-link) discriminant, "
                            "rational, necessary at every n and "
                            "necessary-and-sufficient at n = 3 for "
                            "bistochastic matrices",
    "general-n instrument": "the exact polygon obstruction on every "
                            "column pair and every row pair, decided by "
                            "the Surd sign oracle",
    "NOT implemented": "full phase-elimination (resultants / Groebner) "
                       "for n > 3.  A matrix with NO polygon obstruction "
                       "and NO exhibited certificate would be "
                       "EXCLUDED-BY-CAP; that cell is EMPTY on this "
                       "census; the count is printed with the census and again with "
                       "the caps",
    "Surd sign oracle refinement cap": "4096 binary digits (never "
                                       "approached; the printed maximum "
                                       "is printed with the rings)",
}

# ===========================================================================
# SEC 0.1  SINGLE-SOURCING: AST signature pass, then text-slice.
# ===========================================================================


class _NoExit(Exception):
    pass


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


def slice_exec(path, cut_marker, name):
    src = open(path).read()
    idx = src.index(cut_marker)
    head = src[:idx]
    mod = types.ModuleType(name)
    sys.modules[name] = mod
    ns = mod.__dict__
    ns["__name__"] = name
    real_exit, real_osexit = sys.exit, os._exit

    def _blocked(*a, **k):
        raise _NoExit("sliced layer attempted to exit")

    sys.exit, os._exit = _blocked, _blocked
    try:
        exec(compile(head, f"<slice:{os.path.basename(path)}>", "exec"), ns)
    finally:
        sys.exit, os._exit = real_exit, real_osexit
    return ns, len(head), len(src)


def ast_defs(path, names, ns):
    """Extract named module-level FunctionDefs/ClassDefs by AST and compile
    them into ns (the D70 HZ0-a(iii) idiom, as U1 uses it)."""
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


sec("SINGLE-SOURCING — AST signature pass, then slice, on four committed "
    "receipts")

_P_B1 = "v10/code/d42b1_transport_exact.py"
_P_B3 = "v10/code/d42b3_placement_exact.py"
_P_D74 = "v10/code/d74_transport_holonomy_exact.py"
_P_U1 = "v11/code/u1_indivisibility_census_exact.py"

B1_REQ = {
    "candidates_for": ["acts", "actors"],
    "admissible": ["acts", "e", "actors", "law"],
    "canon": ["acts"],
    "regs_of": ["op"],
    "event_poset": ["acts"],
    "linear_extensions": ["acts"],
    "arb_components_in_view": ["view", "a"],
    "triples": ["view", "idx_set"],
    "edge_triples_of": ["view", "idx_set"],
    "mis_of": ["ckey", "edge_triples"],
    "PK1": ["ckey", "edge_triples"],
    "View": ["<class>"],
}
B3_REQ = {
    "candidates_for": ["acts", "actors"],
    "admissible": ["acts", "e"],
    "canon": ["acts"],
    "regs_of": ["op"],
    "arb_components_in_view": ["view", "a"],
    "event_poset": ["acts"],
    "triples": ["view", "idx_set"],
    "edge_triples_of": ["view", "idx_set"],
    "mis_of": ["ckey", "edge_triples"],
    "PK1": ["ckey", "edge_triples"],
    "View": ["<class>"],
}
D74_REQ = {
    "enumerate_line": ["cands", "actors", "depth", "filt"],
    "square_census": ["fam", "cache", "actors", "dep", "adm", "regs",
                      "canon_f", "filt", "reverse_cands", "tamper"],
    "holonomy_of": ["edges", "reverse_order"],
    "A_menu": ["h", "cache"],
    "congruence": ["R"],
    "mu_map": ["fam", "cache"],
    "primes_of": ["fr"],
    "lattice_basis": ["vecs"],
    "group_of": ["values"],
    "sk": ["o"],
    "evsk": ["e"],
}
U1_REQ = {
    "Q2": ["<class>"],
    "q2_matmul": ["A", "B"],
    "q2_T": ["A"],
    "iso_defect_exact": ["M"],
}

_s1, _m1 = ast_signatures(_P_B1, B1_REQ)
_s3, _m3 = ast_signatures(_P_B3, B3_REQ)
_s74, _m74 = ast_signatures(_P_D74, D74_REQ)
_su1, _mu1 = ast_signatures(_P_U1, U1_REQ)
anchor("SRC.1 AST SIGNATURE PASS on all four committed sources: every "
       "required def/class exists at module level with the exact "
       "positional argument list, so a silent upstream edit cannot slip "
       "through unnoticed",
       not (_m1 or _m3 or _m74 or _mu1),
       f"d42b1 {len(_s1)} defs (missing {_m1}); d42b3 {len(_s3)} "
       f"(missing {_m3}); d74 {len(_s74)} (missing {_m74}); u1 "
       f"{len(_su1)} (missing {_mu1})")

B1, _b1n, _b1t = slice_exec(_P_B1, 'print("[d42b1', "u3_d42b1")
B3, _b3n, _b3t = slice_exec(_P_B3, 'print("[d42b3', "u3_d42b3")
report("d42b1 slice", f"{_b1n}/{_b1t} bytes executed (definition head only)")
report("d42b3 slice", f"{_b3n}/{_b3t} bytes executed (definition head only)")

_exitfree = False
try:
    slice_exec(_P_B1, 'print("[d42b1', "u3_probe")
    _exitfree = True
except _NoExit:
    _exitfree = False
check("SRC.2 EXIT-FREEDOM GATED: sys.exit / os._exit are neutralised "
      "inside the slice and restored after, so a sliced layer cannot set "
      "this receipt's exit status; the slice re-executes cleanly",
      _exitfree and "sys.exit" not in open(_P_B1).read()[:_b1n],
      f"second slice of d42b1 executed with exit blocked; 0 sys.exit in "
      f"the {_b1n}-byte head",
      corollary_of="a property of the loader, not of the substrate")

b1_cand = B1["candidates_for"]
b1_adm = B1["admissible"]
b1_canon = B1["canon"]
b1_regs = B1["regs_of"]
b1_linext = B1["linear_extensions"]
V0 = B1["V0"]
AB = ("A", "B")            # d42b1:433, below the slice cut; U1 re-declares
ABC = ("A", "B", "C")      # them the same way

b3_cand = B3["candidates_for"]
b3_adm = B3["admissible"]
b3_PK1 = B3["PK1"]
b3_arbcomp = B3["arb_components_in_view"]
b3_poset = B3["event_poset"]
b3_View = B3["View"]

NS74 = {"Fr": Fr, "Counter": Counter, "defaultdict": defaultdict,
        "b1_adm": b1_adm, "_EVSK": {}}
_seg74 = ast_defs(_P_D74, list(D74_REQ), NS74)
enumerate_line = NS74["enumerate_line"]
square_census = NS74["square_census"]
holonomy_of = NS74["holonomy_of"]
A_menu = NS74["A_menu"]
congruence = NS74["congruence"]
mu_map = NS74["mu_map"]
primes_of = NS74["primes_of"]
group_of = NS74["group_of"]
d74_evsk = NS74["evsk"]
anchor("SRC.3 D74's CENSUS AND GROUP MACHINERY IS D74's, extracted by AST "
       "from the committed receipt and not retyped: enumerate_line, "
       "square_census, holonomy_of, A_menu, congruence, mu_map, "
       "primes_of, lattice_basis, group_of",
       len(_seg74) == len(D74_REQ),
       f"{len(_seg74)}/{len(D74_REQ)} defs lifted: "
       f"{sorted(_seg74)}")

NSU1 = {"Fr": Fr}
_segu1 = ast_defs(_P_U1, list(U1_REQ), NSU1)
Q2 = NSU1["Q2"]
q2_matmul = NSU1["q2_matmul"]
q2_T = NSU1["q2_T"]
iso_defect_exact = NSU1["iso_defect_exact"]
NSU1["ONE"] = Q2(1, 0)
NSU1["ZERO"] = Q2(0, 0)
anchor("SRC.4 U1's Q(sqrt 2) ARITHMETIC IS U1's, extracted by AST from "
       "the committed U1 receipt (class Q2 and its matrix helpers) so the "
       "K1 arbitration operators this unit screens are literally the "
       "objects U1 handed over, not a re-implementation",
       len(_segu1) == len(U1_REQ),
       f"{len(_segu1)}/{len(U1_REQ)} lifted: {sorted(_segu1)}")

_LINE = {}


def line_family(cands, actors, depth, key):
    """D74's enumerate_line, memoised on `key` so the multiplicity census
    and Arm B screen the SAME generated pool object, enumerated once."""
    if key not in _LINE:
        _LINE[key] = enumerate_line(cands, actors, depth)
    return _LINE[key]


def arb_geometry(L, acts, e):
    """The LAYER's own admission geometry for an arbitration event e at
    history acts, replayed with the layer's own functions and nothing
    retyped: the past-local view admissible() builds, the matched
    conflict component, its conflict edges, its MAXIMAL INDEPENDENT SETS
    (the layer's mis_of) and the committed K1 law on them (the layer's
    PK1).  Returns None if e resolves no component in that view."""
    acts2 = list(acts) + [e]
    j = len(acts2) - 1
    pred = L["event_poset"](acts2)
    view = L["View"](acts2, pred, pred[j])
    comps = L["arb_components_in_view"](view, e[1])
    match = [c for c in comps if L["triples"](view, c[1]) == e[2]]
    if not match:
        return None
    _base, comp = match[0]
    et = L["edge_triples_of"](view, comp)
    return (view, comp, e[2], et, L["mis_of"](e[2], et),
            L["PK1"](e[2], et))


report("caps", "; ".join(f"{k}: {v}" for k, v in CAPS.items()))


# ===========================================================================
# SEC 1.  EXACT ALGEBRAIC ARITHMETIC — Surd and Cyc, with self-tests
# ===========================================================================

sec("EXACT ALGEBRAIC ARITHMETIC — the two rings this receipt computes in")

print("""
  Every certificate below is exhibited with entries in ONE of two exact
  rings, and verified entry by entry inside that ring.  There is no
  tolerance anywhere in this file.

    Surd  the Q-span of { sqrt d : d a squarefree positive integer }.
          Closed under + and *, since sqrt a . sqrt b = s . sqrt d with
          a.b = s^2.d.  ZERO TEST: all coefficients zero -- valid by the
          linear independence of the sqrt d over Q [lit-sqrtind].  SIGN
          ORACLE: exact rational interval refinement with integer isqrt,
          which terminates because a non-zero Surd is bounded away from 0.
          This ring carries every REAL ORTHOGONAL certificate.

    Cyc   Q[x]/Phi_N(x), the cyclotomic field Q(zeta_N), for N = 8 and
          N = 12.  Phi_8 = x^4 + 1, Phi_12 = x^4 - x^2 + 1, both verified
          in-receipt to divide x^N - 1 with zero remainder and to have
          degree phi(N).  Conjugation is zeta -> zeta^{-1}.  This ring
          carries every COMPLEX UNITARY certificate.  Note 1/sqrt 8 and
          1/sqrt 3 lie in these fields, so the DFT certificates are
          EXACT elements, not approximations.
""")


def sqfree_split(n):
    """n = s^2 * d with d squarefree; returns (s, d).  n a positive int."""
    s, d, m = 1, 1, n
    p = 2
    while p * p <= m:
        e = 0
        while m % p == 0:
            m //= p
            e += 1
        if e:
            s *= p ** (e // 2)
            if e % 2:
                d *= p
        p += 1 if p == 2 else 2
    if m > 1:
        d *= m
    return s, d


class Surd(dict):
    """Sum_d c_d sqrt(d) with d squarefree positive int, c_d a Fraction."""

    def __init__(self, arg=None):
        super().__init__()
        if arg is None:
            return
        if isinstance(arg, (int, Fr)):
            if arg:
                self[1] = Fr(arg)
            return
        for d, c in arg.items():
            if c:
                self[d] = self.get(d, Fr(0)) + Fr(c)
        for d in [k for k in self if self[k] == 0]:
            del self[d]

    def __add__(self, o):
        out = dict(self)
        for d, c in Surd(o).items():
            out[d] = out.get(d, Fr(0)) + c
        return Surd(out)

    def __neg__(self):
        return Surd({d: -c for d, c in self.items()})

    def __sub__(self, o):
        return self + (-Surd(o))

    def __mul__(self, o):
        out = {}
        for d1, c1 in self.items():
            for d2, c2 in Surd(o).items():
                s, d = sqfree_split(d1 * d2)
                out[d] = out.get(d, Fr(0)) + c1 * c2 * s
        return Surd(out)

    def is_zero(self):
        return len(self) == 0

    def is_rational(self):
        return all(d == 1 for d in self)

    def rat(self):
        return self.get(1, Fr(0))

    def __repr__(self):
        if not self:
            return "0"
        return " + ".join(
            (str(c) if d == 1 else f"({c})sqrt{d}")
            for d, c in sorted(self.items()))


SIGN_BITS_USED = [0]


def surd_sign(x):
    """Exact sign of a Surd.  Zero iff every coefficient is zero
    [lit-sqrtind]; otherwise rational interval refinement terminates."""
    items = [(d, c) for d, c in x.items() if c != 0]
    if not items:
        return 0
    k = 16
    while k <= 4096:
        SIGN_BITS_USED[0] = max(SIGN_BITS_USED[0], k)
        scale = 1 << k
        lo = Fr(0)
        hi = Fr(0)
        for d, c in items:
            if d == 1:
                rl = rh = Fr(1)
            else:
                s = math.isqrt(d * scale * scale)
                rl, rh = Fr(s, scale), Fr(s + 1, scale)
            if c > 0:
                lo += c * rl
                hi += c * rh
            else:
                lo += c * rh
                hi += c * rl
        if lo > 0:
            return 1
        if hi < 0:
            return -1
        k *= 2
    raise RuntimeError("Surd sign oracle exceeded the printed cap")


def sqrt_fr(r):
    """sqrt of a non-negative Fraction, exactly, as a Surd."""
    if r < 0:
        raise ValueError("negative radicand")
    if r == 0:
        return Surd()
    p, q = r.numerator, r.denominator
    s, d = sqfree_split(p * q)
    return Surd({d: Fr(s, q)})


# ---- self-tests on Surd -------------------------------------------------
_t1 = sqrt_fr(Fr(2)) * sqrt_fr(Fr(3)) - sqrt_fr(Fr(6))
_t2 = (sqrt_fr(Fr(2)) + sqrt_fr(Fr(3))) * (sqrt_fr(Fr(2)) + sqrt_fr(Fr(3)))
_t3 = sqrt_fr(Fr(1, 2)) * sqrt_fr(Fr(1, 2)) - Surd(Fr(1, 2))
_t4 = sqrt_fr(Fr(2)) + sqrt_fr(Fr(3)) - sqrt_fr(Fr(10))
_t5 = sqrt_fr(Fr(2)) + sqrt_fr(Fr(3)) - sqrt_fr(Fr(5))
check("R1.1 THE Surd RING IS EXACT AND ITS ZERO TEST IS SOUND: "
      "sqrt2.sqrt3 - sqrt6 = 0 identically; (sqrt2+sqrt3)^2 = 5 + 2sqrt6 "
      "identically; sqrt(1/2)^2 = 1/2 identically",
      _t1.is_zero() and dict(_t2) == {1: Fr(5), 6: Fr(2)} and _t3.is_zero(),
      f"sqrt2.sqrt3-sqrt6 = {_t1}; (sqrt2+sqrt3)^2 = {_t2}; "
      f"sqrt(1/2)^2-1/2 = {_t3}")
check("R1.2 THE Surd SIGN ORACLE IS EXACT ON A KNOWN-ANSWER PAIR THAT NO "
      "TOLERANCE SETTLES: sqrt2 + sqrt3 - sqrt10 < 0 (3.146... < 3.162...) "
      "while sqrt2 + sqrt3 - sqrt5 > 0 (3.146... > 2.236...)",
      surd_sign(_t4) == -1 and surd_sign(_t5) == +1,
      f"sign(sqrt2+sqrt3-sqrt10) = {surd_sign(_t4)}; "
      f"sign(sqrt2+sqrt3-sqrt5) = {surd_sign(_t5)}; refinement used at "
      f"most {SIGN_BITS_USED[0]} binary digits")


def polydivmod(a, b):
    """Exact division of Q-polynomials given low-to-high coefficient
    lists; b monic-or-not, returns (quotient, remainder)."""
    a = [Fr(x) for x in a]
    b = [Fr(x) for x in b]
    while b and b[-1] == 0:
        b.pop()
    q = [Fr(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and any(a):
        while a and a[-1] == 0:
            a.pop()
        if len(a) < len(b):
            break
        f = a[-1] / b[-1]
        sh = len(a) - len(b)
        q[sh] += f
        for i, c in enumerate(b):
            a[sh + i] -= f * c
    while a and a[-1] == 0:
        a.pop()
    return q, a


PHI = {8: [Fr(1), Fr(0), Fr(0), Fr(0), Fr(1)],
       12: [Fr(1), Fr(0), Fr(-1), Fr(0), Fr(1)]}
PHI_NAME = {8: "x^4 + 1", 12: "x^4 - x^2 + 1"}


class Cyc:
    """An element of Q[x]/Phi_N(x) = Q(zeta_N), N in {8, 12}."""

    __slots__ = ("N", "c")

    def __init__(self, N, coeffs):
        self.N = N
        c = [Fr(x) for x in coeffs]
        deg = len(PHI[N]) - 1
        while len(c) < deg:
            c.append(Fr(0))
        if len(c) > deg:
            _, c = polydivmod(c, PHI[N])
            while len(c) < deg:
                c.append(Fr(0))
        self.c = c[:deg]

    def __add__(self, o):
        return Cyc(self.N, [a + b for a, b in zip(self.c, o.c)])

    def __neg__(self):
        return Cyc(self.N, [-a for a in self.c])

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, o):
        if isinstance(o, (int, Fr)):
            return Cyc(self.N, [a * Fr(o) for a in self.c])
        out = [Fr(0)] * (len(self.c) + len(o.c) - 1)
        for i, a in enumerate(self.c):
            if a == 0:
                continue
            for j, b in enumerate(o.c):
                out[i + j] += a * b
        return Cyc(self.N, out)

    def __eq__(self, o):
        return isinstance(o, Cyc) and self.N == o.N and self.c == o.c

    def is_zero(self):
        return all(a == 0 for a in self.c)

    def is_rational(self):
        return all(a == 0 for a in self.c[1:])

    def rat(self):
        return self.c[0]

    def conj(self):
        """zeta -> zeta^{-1}: a ring automorphism, applied via the image
        of the generator."""
        g = cyc_pow(cyc_x(self.N), self.N - 1)
        out = Cyc(self.N, [Fr(0)])
        p = cyc_one(self.N)
        for a in self.c:
            out = out + p * a
            p = p * g
        return out

    def __repr__(self):
        return "+".join(f"{a}x^{i}" for i, a in enumerate(self.c) if a) or "0"


def cyc_one(N):
    return Cyc(N, [Fr(1)])


def cyc_zero(N):
    return Cyc(N, [Fr(0)])


def cyc_x(N):
    return Cyc(N, [Fr(0), Fr(1)])


def cyc_pow(z, k):
    out = cyc_one(z.N)
    for _ in range(k):
        out = out * z
    return out


def phi_euler(n):
    return sum(1 for k in range(1, n + 1) if math.gcd(k, n) == 1)


_cycok = True
_cycdet = []
for _N in (8, 12):
    _xn = [Fr(0)] * _N + [Fr(1)]
    _xn[0] = Fr(-1)
    _q, _r = polydivmod(_xn, PHI[_N])
    _deg_ok = (len(PHI[_N]) - 1) == phi_euler(_N)
    _rem_ok = (not _r) or all(x == 0 for x in _r)
    _xN = cyc_pow(cyc_x(_N), _N)
    _one_ok = _xN == cyc_one(_N)
    _cnj = cyc_x(_N).conj()
    _inv_ok = (cyc_x(_N) * _cnj) == cyc_one(_N)
    _inv2_ok = _cnj.conj() == cyc_x(_N)
    _cycok &= _deg_ok and _rem_ok and _one_ok and _inv_ok and _inv2_ok
    _cycdet.append(f"N={_N}: Phi = {PHI_NAME[_N]}, deg {len(PHI[_N]) - 1} = "
                   f"phi({_N}) = {phi_euler(_N)} {_deg_ok}; Phi | x^N-1 "
                   f"{_rem_ok}; x^N = 1 {_one_ok}; zeta.conj(zeta) = 1 "
                   f"{_inv_ok}; conj involutive {_inv2_ok}")
check("R1.3 THE CYCLOTOMIC RINGS ARE THE FIELDS THEY CLAIM TO BE: for "
      "N = 8 and N = 12 the hard-coded Phi_N has degree phi(N), divides "
      "x^N - 1 with remainder EXACTLY zero, satisfies x^N = 1 in the "
      "quotient, and conjugation zeta -> zeta^{-1} is an involution with "
      "zeta . conj(zeta) = 1",
      _cycok, "; ".join(_cycdet))

SQRT2_8 = cyc_x(8) - cyc_pow(cyc_x(8), 3)              # zeta8 + zeta8^-1
INV_SQRT8 = SQRT2_8 * Fr(1, 4)                         # = sqrt2 / 4
SQRT3_12 = cyc_x(12) * 2 - cyc_pow(cyc_x(12), 3)       # zeta12 + zeta12^-1
INV_SQRT3 = SQRT3_12 * Fr(1, 3)                        # = sqrt3 / 3
ZETA3 = cyc_pow(cyc_x(12), 4)
check("R1.4 THE IRRATIONAL NORMALISERS THE DFT CERTIFICATES NEED ARE "
      "EXACT ELEMENTS OF THESE FIELDS: (zeta8 + zeta8^-1)^2 = 2 exactly, "
      "so 1/sqrt8 = (zeta8 - zeta8^3)/4 exactly; (zeta12 + zeta12^-1)^2 = "
      "3 exactly, so 1/sqrt3 = (2.zeta12 - zeta12^3)/3 exactly; and "
      "zeta3 = zeta12^4 has order 3",
      (SQRT2_8 * SQRT2_8) == Cyc(8, [Fr(2)])
      and (INV_SQRT8 * INV_SQRT8) == Cyc(8, [Fr(1, 8)])
      and (SQRT3_12 * SQRT3_12) == Cyc(12, [Fr(3)])
      and (INV_SQRT3 * INV_SQRT3) == Cyc(12, [Fr(1, 3)])
      and cyc_pow(ZETA3, 3) == cyc_one(12) and ZETA3 != cyc_one(12),
      f"sqrt2^2 = {SQRT2_8 * SQRT2_8}; (1/sqrt8)^2 = {INV_SQRT8 * INV_SQRT8}"
      f"; sqrt3^2 = {SQRT3_12 * SQRT3_12}; (1/sqrt3)^2 = "
      f"{INV_SQRT3 * INV_SQRT3}; zeta3^3 = {cyc_pow(ZETA3, 3)}")


# ===========================================================================
# SEC 2.  THE DECISION PROCEDURES, AND THE KNOWN-ANSWER CONTROLS
# ===========================================================================

sec("THE DECISION PROCEDURES, AND THE KNOWN-ANSWER CONTROLS")

print(f"""
  [B3]'s definition, verbatim ({QUOTES['B3-uni'][0]}):
    "{QUOTES['B3-uni'][1]}"

  [B3]'s convention ({QUOTES['B3-conv'][0]}):
    "{QUOTES['B3-conv'][1]}"

  THE GUARD, CARRIED FIRST, AS THE CATALOG REQUIRES ({QUOTES['d75-D1guard'][0]}):
    "{QUOTES['d75-D1guard'][1]}"
  Theorem D1 is therefore SET ASIDE in this receipt and is not used to
  decide anything.  Every positive verdict below exhibits a unitary of the
  SAME SIZE as the matrix, with NO ancilla and NO ancilla sum.
""")


def ds_report(M):
    """Exact doubly-stochastic report.  Returns a dict."""
    n, m = len(M), len(M[0])
    rows = [sum(M[i]) for i in range(n)]
    cols = [sum(M[i][j] for i in range(n)) for j in range(m)]
    neg = [(i, j) for i in range(n) for j in range(m) if M[i][j] < 0]
    return {
        "square": n == m,
        "n": n, "m": m,
        "rowsums": rows, "colsums": cols,
        "rowdef": [r - 1 for r in rows], "coldef": [c - 1 for c in cols],
        "row_ok": all(r == 1 for r in rows),
        "col_ok": all(c == 1 for c in cols),
        "nonneg": not neg,
        "L1row": sum(abs(r - 1) for r in rows),
        "L1col": sum(abs(c - 1) for c in cols),
        "ds": n == m and all(r == 1 for r in rows) and all(c == 1
                                                          for c in cols)
        and not neg,
    }


def tri_disc(a, b, c):
    """The exact triangle discriminant for side lengths sqrt a, sqrt b,
    sqrt c: T = 2(ab+bc+ca) - a^2 - b^2 - c^2 = 16 . (Heron area)^2.
    T >= 0 iff the three phasors of those moduli can close."""
    return 2 * (a * b + b * c + c * a) - a * a - b * b - c * c


def chain_link_squares(M, p, q, by="col"):
    """The SQUARED moduli of the phasors whose closure is the
    orthogonality of two columns (or rows) of any unitary lift."""
    n = len(M)
    if by == "col":
        return [M[i][p] * M[i][q] for i in range(n)]
    return [M[p][j] * M[q][j] for j in range(n)]


def polygon_violations(M):
    """The GENERAL necessary condition, at every n.  If Gamma = |U|^2 for
    a unitary U then for every pair of distinct columns (p,q) the n
    complex numbers conj(U_ip) U_iq -- of modulus sqrt(Gamma_ip Gamma_iq)
    -- sum to zero, so no one modulus may exceed the sum of the others.
    Same for rows.  Decided exactly by the Surd sign oracle."""
    n, m = len(M), len(M[0])
    out = []
    pairs = [("col", p, q) for p in range(m) for q in range(p + 1, m)]
    pairs += [("row", p, q) for p in range(n) for q in range(p + 1, n)]
    for by, p, q in pairs:
        a = chain_link_squares(M, p, q, by)
        L = [sqrt_fr(x) for x in a]
        for i in range(len(L)):
            slack = Surd()
            for k in range(len(L)):
                slack = slack + (L[k] if k != i else -L[k])
            if surd_sign(slack) < 0:
                out.append((by, p, q, i, a, slack))
    return out


def unitary_check_cyc(U):
    """U^dagger U = I, exactly, in a cyclotomic field."""
    n = len(U)
    bad = []
    for i in range(n):
        for j in range(n):
            s = cyc_zero(U[0][0].N)
            for k in range(n):
                s = s + U[k][i].conj() * U[k][j]
            want = cyc_one(U[0][0].N) if i == j else cyc_zero(U[0][0].N)
            if not (s - want).is_zero():
                bad.append((i, j, s))
    return bad


def modsq_check_cyc(U, M):
    """|U_ij|^2 = M_ij entry by entry, exactly."""
    bad = []
    for i in range(len(U)):
        for j in range(len(U[0])):
            z = U[i][j] * U[i][j].conj()
            if not z.is_rational() or z.rat() != M[i][j]:
                bad.append((i, j, z, M[i][j]))
    return bad


def orth_check_surd(U):
    """U^T U = I, exactly, in the Surd ring."""
    n = len(U)
    bad = []
    for i in range(n):
        for j in range(n):
            s = Surd()
            for k in range(n):
                s = s + U[k][i] * U[k][j]
            want = Surd(Fr(1)) if i == j else Surd()
            if not (s - want).is_zero():
                bad.append((i, j, s))
    return bad


def modsq_check_surd(U, M):
    bad = []
    for i in range(len(U)):
        for j in range(len(U[0])):
            z = U[i][j] * U[i][j]
            if not z.is_rational() or z.rat() != M[i][j]:
                bad.append((i, j, z, M[i][j]))
    return bad


def real_orth_2x2(B):
    """THE n = 2 CLASSICAL FACT, CONSTRUCTED RATHER THAN CITED.  For every
    2x2 doubly-stochastic B = [[p,1-p],[1-p,p]] the real matrix
    U = [[ sqrt p, sqrt(1-p)], [sqrt(1-p), -sqrt p]] is orthogonal and
    |U_ij|^2 = B_ij.  Hence every 2x2 bistochastic matrix is not merely
    unistochastic but ORTHOSTOCHASTIC, and no 2-outcome object can ever
    force the complex numbers."""
    p = B[0][0]
    return [[sqrt_fr(p), sqrt_fr(B[0][1])],
            [sqrt_fr(B[1][0]), -sqrt_fr(B[1][1])]]


def sylvester(k):
    """Sylvester's real Hadamard matrix of order 2^k [lit-had]."""
    H = [[1]]
    for _ in range(k):
        H = [r + r for r in H] + [r + [-x for x in r] for r in H]
    return H


# --- the pair-independence of the n = 3 discriminant, PROVED in-receipt --
print("""
  THE n = 3 CRITERION, AND WHY THIS RECEIPT MAY USE ONE COLUMN PAIR.
  For a 3x3 matrix the criterion is stated for ONE pair of columns.  That
  is legitimate only if the discriminant does not depend on which pair is
  taken.  This receipt does not assume it and does not cite it: it PROVES
  it, by polynomial identity.  T is a polynomial of degree at most 4 in
  each of the four free entries of a bistochastic 3x3 matrix, so two such
  polynomials agreeing on a product grid with 5 distinct values per
  variable are identical (the standard multivariate interpolation bound /
  Combinatorial Nullstellensatz).  All six discriminants -- three column
  pairs and three row pairs -- are evaluated on such a grid below.
""")
_grid = [Fr(1, 7), Fr(2, 7), Fr(3, 7), Fr(5, 7), Fr(8, 7)]
_mismatch = 0
_gridn = 0
for _u, _v, _w, _z in product(_grid, repeat=4):
    _B = [[_u, _v, 1 - _u - _v],
          [_w, _z, 1 - _w - _z],
          [1 - _u - _w, 1 - _v - _z, _u + _v + _w + _z - 1]]
    _vals = set()
    for _p, _q in ((0, 1), (0, 2), (1, 2)):
        _vals.add(tri_disc(*chain_link_squares(_B, _p, _q, "col")))
        _vals.add(tri_disc(*chain_link_squares(_B, _p, _q, "row")))
    _gridn += 1
    if len(_vals) != 1:
        _mismatch += 1
check("C0 THE SIX UNITARITY TRIANGLES OF A BISTOCHASTIC 3x3 MATRIX HAVE "
      "THE SAME DISCRIMINANT — PROVED HERE AS A POLYNOMIAL IDENTITY, NOT "
      "ASSUMED AND NOT CITED.  Three column pairs and three row pairs "
      "agree at every point of a 5^4 rational grid; since each "
      "discriminant has degree at most 4 in each of the four free "
      "entries, agreement on a 5-per-variable grid forces identity.  So "
      "'the' triangle discriminant is well defined and one column pair "
      "suffices",
      _mismatch == 0 and _gridn == 5 ** 4,
      f"{_gridn} grid points, {_mismatch} mismatches, grid values "
      f"{fsl(_grid)}")

print(f"""
  THE CRITERION USED, NAMED AND CITED ({QUOTES['lit-uni3'][0]}):
    "{QUOTES['lit-uni3'][1]}"

  HOW THIS RECEIPT USES IT — the asymmetry is deliberate:
    NEGATIVE direction (T < 0 => NOT unistochastic).  This direction is
      ELEMENTARY and is not taken on citation: if Gamma = |U|^2 then two
      columns of U are orthogonal, so three complex numbers of moduli
      sqrt(Gamma_ip Gamma_iq) sum to zero, so their moduli satisfy the
      triangle inequality.  The necessity holds at EVERY n (the polygon
      obstruction) and needs no bistochasticity.
    POSITIVE direction.  This receipt NEVER returns "unistochastic" on
      the strength of T >= 0.  Every positive verdict below EXHIBITS a
      unitary of the same size and verifies U^dagger U = I and
      |U_ij|^2 = Gamma_ij entry by entry in exact algebraic arithmetic.
      The cited sufficiency is therefore never load-bearing.
""")

# --- KNOWN-ANSWER CONTROLS ----------------------------------------------
print("  KNOWN-ANSWER CONTROLS.  The decision procedure is run on one")
print("  literature UNISTOCHASTIC matrix and one literature")
print("  BISTOCHASTIC-BUT-NOT-UNISTOCHASTIC matrix before it is pointed at")
print("  anything generated.  It must get both right.")
print()

# KA-1: the flat 3x3 = |DFT_3|^2 -- unistochastic
FLAT3 = [[Fr(1, 3)] * 3 for _ in range(3)]
U_DFT3 = [[cyc_pow(ZETA3, (i * j) % 3) * 1 * INV_SQRT3 for j in range(3)]
          for i in range(3)]
_ka1_uni = unitary_check_cyc(U_DFT3)
_ka1_mod = modsq_check_cyc(U_DFT3, FLAT3)
_ka1_T = tri_disc(*chain_link_squares(FLAT3, 0, 1, "col"))
_ka1_poly = polygon_violations(FLAT3)
check("KA-1 THE 3x3 FLAT MATRIX J/3 IS DECIDED UNISTOCHASTIC, WITH THE "
      "UNITARY EXHIBITED: the 3-point DFT U_jk = zeta_3^{jk}/sqrt3, "
      "written exactly in Q(zeta_12), satisfies U^dagger U = I with ZERO "
      "residual entries and |U_ij|^2 = 1/3 exactly at all nine entries; "
      "the triangle discriminant is +1/27 > 0 and there is no polygon "
      "violation — criterion and certificate agree",
      not _ka1_uni and not _ka1_mod and _ka1_T > 0 and not _ka1_poly,
      f"unitarity residuals {len(_ka1_uni)}; |U|^2 mismatches "
      f"{len(_ka1_mod)}; T = {_ka1_T}; polygon violations "
      f"{len(_ka1_poly)}")

# KA-2: the canonical bistochastic-but-not-unistochastic 3x3
BNOT = [[Fr(0), Fr(1, 2), Fr(1, 2)],
        [Fr(1, 2), Fr(0), Fr(1, 2)],
        [Fr(1, 2), Fr(1, 2), Fr(0)]]
_ka2_ds = ds_report(BNOT)
_ka2_T = tri_disc(*chain_link_squares(BNOT, 0, 1, "col"))
_ka2_poly = polygon_violations(BNOT)
check("KA-2 THE CANONICAL COUNTEREXAMPLE B = (1/2)(J - I) IS DECIDED "
      "BISTOCHASTIC BUT NOT UNISTOCHASTIC, WITH AN EXACT MARGIN: rows and "
      "columns sum to exactly 1, the triangle discriminant is -1/16 < 0, "
      "and the polygon oracle independently flags the same obstruction — "
      "the phasor moduli for columns 1,2 are (0, 0, 1/2) and 1/2 > 0 + 0, "
      "so no unitary has these modulus-squares.  This reproduces the "
      "corpus's own committed print at "
      "v8/code/p18_seal_divisibility.py:346-347, in exact arithmetic",
      _ka2_ds["ds"] and _ka2_T < 0 and len(_ka2_poly) > 0,
      f"DS {_ka2_ds['ds']}; T = {_ka2_T}; polygon violations "
      f"{len(_ka2_poly)}; phasor squared-moduli (cols 0,1) = "
      f"{fsl(chain_link_squares(BNOT, 0, 1, 'col'))}")

# KA-3: the ortho/uni gap is real and my ortho decision is not vacuous
_par = []
for _i in range(3):
    for _j in range(_i + 1, 3):
        for _s in product((1, -1), repeat=3):
            _par.append(sum(_s))
_ka3 = all(x != 0 for x in _par)
check("KA-3 THE ORTHO/UNI GAP IS EXHIBITED, SO THE ORTHOSTOCHASTIC "
      "QUESTION IS NOT VACUOUS: J/3 is unistochastic (KA-1) but NOT "
      "orthostochastic — a real orthogonal O with O_ij^2 = 1/3 "
      "everywhere would need two rows with inner product "
      "(+-1 +-1 +-1)/3, and every one of the eight sign patterns gives "
      "an ODD integer, never 0.  This is the canonical matrix on which "
      "the complex numbers are FORCED, and it is the exact shape the D75 "
      "audit located the necessity of i in",
      _ka3, f"the eight achievable numerators are "
            f"{sorted(set(_par))} — none is 0")

# KA-4: n = 2 constructed
B2 = [[Fr(1, 3), Fr(2, 3)], [Fr(2, 3), Fr(1, 3)]]
U2 = real_orth_2x2(B2)
_ka4 = (not orth_check_surd(U2)) and (not modsq_check_surd(U2, B2))
check("KA-4 THE n = 2 CLASSICAL FACT IS VERIFIED IN-RECEIPT RATHER THAN "
      "ASSERTED: for the bistochastic [[1/3,2/3],[2/3,1/3]] the "
      "constructed real matrix [[sqrt(1/3), sqrt(2/3)], [sqrt(2/3), "
      "-sqrt(1/3)]] is exactly orthogonal in the Surd ring and its "
      "modulus-squares are the matrix.  The construction is uniform in p, "
      "so EVERY 2x2 bistochastic matrix is orthostochastic",
      _ka4, f"orthogonality residuals {len(orth_check_surd(U2))}; "
            f"|U|^2 mismatches {len(modsq_check_surd(U2, B2))}; U = "
            f"[[{U2[0][0]}, {U2[0][1]}], [{U2[1][0]}, {U2[1][1]}]]")

# KA-5: a non-DS row-stochastic matrix must be caught by the precondition
BRS = [[Fr(1, 2), Fr(1, 2)], [Fr(1), Fr(0)]]
_ka5 = ds_report(BRS)
check("KA-5 THE DOUBLY-STOCHASTIC PRECONDITION IS NOT A NO-OP: a "
      "row-stochastic matrix that is not column-stochastic is caught, "
      "with the exact per-column excess printed",
      _ka5["row_ok"] and not _ka5["col_ok"] and not _ka5["ds"],
      f"row sums {fsl(_ka5['rowsums'])}; column sums "
      f"{fsl(_ka5['colsums'])}; column deficits {fsl(_ka5['coldef'])}")

# KA-6: Sylvester H_8 is a real Hadamard matrix (used as a certificate later)
_H8 = sylvester(3)
_h8ok = all(sum(_H8[k][i] * _H8[k][j] for k in range(8))
            == (8 if i == j else 0) for i in range(8) for j in range(8))
check("KA-6 SYLVESTER'S REAL HADAMARD MATRIX OF ORDER 8 IS VERIFIED "
      "IN-RECEIPT (H H^T = 8 I over the integers), so the real "
      "certificate used for the 8x8 passer at L2 is not taken on trust",
      _h8ok, "H_8 = H_2^{tensor 3}, entries +-1, all 64 inner products "
             "exact")


def screen(name, M, provenance, reading, note="", cert_hint=None):
    """THE SCREEN.  One matrix in, one verdict out, everything exact."""
    print()
    print(f"  ---- {name} " + "-" * max(4, 66 - len(name)))
    print(f"       provenance : {provenance}")
    print(f"       reading    : {reading}")
    if note:
        print(f"       note       : {note}")
    n, m = len(M), len(M[0])
    print(f"       shape      : {n} x {m}")
    for i in range(n):
        print("         " + "  ".join(str(M[i][j]) for j in range(m)))
    if n != m:
        print("       VERDICT    : N/A-SHAPE.  Barandes' criterion is "
              "defined for SQUARE")
        print("                    matrices only (an N x N Gamma against "
              "an N x N unitary).")
        print("                    The object is not screened; the "
              "trivial column completion")
        print("                    of an isometry is Theorem D1's move "
              "and is SET ASIDE.")
        return {"verdict": "N/A-SHAPE", "name": name}
    R = ds_report(M)
    print(f"       row sums   : {fsl(R['rowsums'])}")
    print(f"       col sums   : {fsl(R['colsums'])}")
    Tn3 = (tri_disc(*chain_link_squares(M, 0, 1, "col")) if n == 3
           else None)
    if not R["ds"]:
        print(f"       row deficit: {fsl(R['rowdef'])}   "
              f"sum|.| = {R['L1row']}")
        print(f"       col deficit: {fsl(R['coldef'])}   "
              f"sum|.| = {R['L1col']}")
        print("       VERDICT    : S-FAIL-DS.  Unistochastic implies "
              "doubly stochastic")
        print("                    (a unitary has orthonormal rows AND "
              "columns), so the")
        print("                    object is NOT unistochastic, exactly.")
        print(f"       PRICE      : for EVERY doubly-stochastic D, "
              f"||M - D||_1 >= max(sum_i |r_i - 1|, sum_j |c_j - 1|) = "
              f"{max(R['L1row'], R['L1col'])}.")
        if Tn3 is not None:
            print(f"       triangle   : T = {Tn3} "
                  f"({'>= 0' if Tn3 >= 0 else '< 0 — a SECOND obstruction'})")
        pv = polygon_violations(M)
        if pv:
            by, p, q, i, a, slack = pv[0]
            print(f"       SECOND OBSTRUCTION, INDEPENDENT OF DS (the "
                  f"polygon condition is")
            print(f"                    necessary at every n and needs no "
                  f"bistochasticity): it fails")
            print(f"                    on the {by} pair ({p},{q}) at "
                  f"index {i}: squared moduli {fsl(a)},")
            print(f"                    slack = {slack} < 0.  "
                  f"{len(pv)} violation(s) in all.")
        return {"verdict": "S-FAIL-DS", "name": name, "R": R,
                "poly": pv, "T": Tn3, "M": M}
    print("       DS         : PASSES — rows and columns both sum to "
          "exactly 1, entries >= 0.")
    pv = polygon_violations(M)
    print(f"       polygon    : {len(pv)} violation(s) over "
          f"{n * (n - 1)} column/row pairs")
    if n == 3:
        T = Tn3
        print(f"       triangle   : T = {T} "
              f"({'>= 0' if T >= 0 else '< 0'})")
        if T < 0:
            print("       VERDICT    : S-FAIL-UNI.  DS holds; the "
                  "unitarity triangle does not")
            print("                    close, so no unitary has these "
                  "modulus-squares.")
            return {"verdict": "S-FAIL-UNI", "name": name, "R": R,
                    "T": T, "M": M}
    if pv:
        print("       VERDICT    : S-FAIL-UNI.  DS holds; the polygon "
              "obstruction fires.")
        return {"verdict": "S-FAIL-UNI", "name": name, "R": R,
                "poly": pv, "M": M}
    if cert_hint is None:
        print("       VERDICT    : EXCLUDED-BY-CAP.  No obstruction "
              "found and no certificate")
        print("                    constructed at this size.  Reported "
              "as a cap, not a pass.")
        return {"verdict": "EXCLUDED-BY-CAP", "name": name, "R": R,
                "M": M}
    kind, U = cert_hint
    if kind == "surd":
        bad_u, bad_m = orth_check_surd(U), modsq_check_surd(U, M)
        cls = "ORTHOSTOCHASTIC (a REAL orthogonal certificate)"
    else:
        bad_u, bad_m = unitary_check_cyc(U), modsq_check_cyc(U, M)
        cls = "UNISTOCHASTIC (a complex unitary certificate)"
    ok = not bad_u and not bad_m
    print(f"       certificate: {cls}")
    print(f"                    U^dagger U - I : {len(bad_u)} non-zero "
          f"entries")
    print(f"                    |U_ij|^2 - M_ij: {len(bad_m)} mismatches")
    print(f"       VERDICT    : {'S-PASS' if ok else 'CERTIFICATE-FAILED'}"
          f".  The matrix IS unistochastic, and the")
    print("                    unitary is exhibited above in exact "
          "algebraic arithmetic.")
    return {"verdict": "S-PASS" if ok else "CERTIFICATE-FAILED",
            "name": name, "R": R, "cert": kind, "M": M}


# ===========================================================================
# SEC 3.  ARM A (a) — THE K1 ARBITRATION OBJECTS, REBUILT AND SCREENED
# ===========================================================================

sec("ARM A (a) — THE K1 ARBITRATION OBJECTS, REBUILT FROM THE COMMITTED "
    "LAYER AND SCREENED")

_t = time.time()
ONE, ZERO = Q2(1, 0), Q2(0, 0)
INV_SQRT2 = Q2(0, Fr(1, 2))
check("A0.0 1/sqrt2 IS EXACTLY REPRESENTABLE IN U1's Q(sqrt 2): "
      "(1/sqrt2)^2 = 1/2 identically, so the K1 amplitudes carry no "
      "approximation at all",
      (INV_SQRT2 * INV_SQRT2) == Q2(Fr(1, 2), 0),
      f"(1/sqrt2)^2 = {INV_SQRT2 * INV_SQRT2}")

pA0 = ("p", "A", V0, 0)
pB1 = ("p", "B", V0, 1)
tA, tB = ("A", V0, 0), ("B", V0, 1)
SELFA = ("r", "A", frozenset({tA}), frozenset({tA}))
PAIRA = ("r", "A", frozenset({tA, tB}), frozenset({tA}))
PAIRB = ("r", "A", frozenset({tA, tB}), frozenset({tB}))
H1, H2 = [pA0], [pA0, pB1]


def arb_menu_closed(h):
    return sorted(((e, q) for e, q in b3_cand(h, AB)
                   if e[1] == "A" and e[0] == "r"), key=lambda z: sk(z[0]))


m1 = arb_menu_closed(H1)
m2 = arb_menu_closed(H2)
s_full_1 = sum(q for e, q in b3_cand(H1, AB) if e[1] == "A")
s_full_2 = sum(q for e, q in b3_cand(H2, AB) if e[1] == "A")
anchor("A1 THE COMMITTED PAIR EXHIBIT RE-RUNS (paper 31 sec.4.3, U1 "
       "A0.1): A's arbitration menu is ONE event at the early cut and "
       "THREE at the join; the full per-actor sums are exactly 1 and 5/4",
       len(m1) == 1 and len(m2) == 3
       and s_full_1 == ANCH["full_sum_early"]
       and s_full_2 == ANCH["full_sum_join"],
       f"menu sizes {len(m1)}/{len(m2)}; full sums {s_full_1}/{s_full_2}")

O_pair = [[INV_SQRT2], [INV_SQRT2]]
A_pair = [[ONE, ZERO], [ZERO, ZERO], [ZERO, ZERO], [ZERO, ONE]]
V_pair = q2_matmul(A_pair, O_pair)
O_sing = [[ONE]]
A_sing = [[ONE], [ZERO]]
V_sing = q2_matmul(A_sing, O_sing)
_defects = {nm: iso_defect_exact(M) for nm, M in
            (("V_pair", V_pair), ("V_single", V_sing))}
anchor("A2 THE K1 OPERATORS ARE U1's, WITH ISOMETRY DEFECT EXACTLY 0: "
       "V_pair (4x1) and V_single (2x1), built as Acceptance o "
       "OpeningClick from the committed machinery, satisfy M^T M - I = 0 "
       "identically in Q(sqrt 2)",
       all(len(v) == 0 for v in _defects.values())
       and (len(V_pair), len(V_pair[0])) == (4, 1)
       and (len(V_sing), len(V_sing[0])) == (2, 1),
       f"shapes {(len(V_pair), len(V_pair[0]))} / "
       f"{(len(V_sing), len(V_sing[0]))}; non-zero entries of M^T M - I: "
       + ", ".join(f"{n} {len(_defects[n])}" for n in sorted(_defects)))

edge = frozenset({tuple(sorted((tA, tB)))})
k1_pair = b3_PK1(frozenset({tA, tB}), edge)
k1_sing = b3_PK1(frozenset({tA}), frozenset())
born_pair = [V_pair[0][0] * V_pair[0][0], V_pair[3][0] * V_pair[3][0]]
born_sing = [V_sing[0][0] * V_sing[0][0]]
anchor("A3 BORN = K1 EXACTLY, RECOMPUTED FROM THE COMMITTED LAYER: the "
       "squared branch amplitudes of V_pair are the RATIONALS 1/2 and "
       "1/2 and equal PK1 on the 2-conflict; V_single's branch is "
       "deterministic and equals PK1 on the singleton",
       all(x.is_rational() for x in born_pair + born_sing)
       and sorted(x.a for x in born_pair) == ANCH["born_pair"]
       and [x.a for x in born_sing] == ANCH["born_single"]
       and sorted(k1_pair.values()) == ANCH["born_pair"]
       and sorted(k1_sing.values()) == ANCH["born_single"],
       f"|amp|^2 (pair) = {[str(x.a) for x in born_pair]}; PK1 (pair) = "
       f"{sorted(str(v) for v in k1_pair.values())}; |amp|^2 (single) = "
       f"{[str(x.a) for x in born_sing]}")

_join_menu = sorted((q for e, q in m2))
anchor("A4 THE JOIN MENU IS THE COMMITTED ONE: 1/4 + 1/8 + 1/8 on the "
       "arbitration sector at the join, and 1/4 at the early cut",
       sorted(_join_menu) == sorted(ANCH["menu_join"])
       and sum(q for e, q in m1) == ANCH["menu_early_sum"],
       f"join menu {[str(x) for x in _join_menu]}; early menu sum "
       f"{sum(q for e, q in m1)}")

print("""
  THE READINGS, DECLARED BEFORE ANY VERDICT.  V_single and V_pair are
  ISOMETRIES WITH ONE COLUMN (2x1 and 4x1).  Barandes' criterion is a
  statement about a SQUARE Gamma and a SQUARE unitary of the same size, so
  the operators themselves are not screenable objects; what is screenable
  is their induced Gamma.  Four readings are taken, each named, and the
  convention-relative ones are labelled as such.  Nothing is invented: the
  numbers are the committed K1 law and the committed menus, above.
""")

SCREEN = []

SCREEN.append(screen(
    "K1-BORN-COL-PAIR",
    [[born_pair[0].a], [Fr(0)], [Fr(0)], [born_pair[1].a]],
    "V_pair (4x1) from paper 31 sec.4.3, |.|^2 entrywise "
    "[p31-4.3, A2, A3]",
    "the Born column of the 2-conflict: |V_pair|^2 as a 4x1 object",
    "the two zero rows are the branches the acceptance step kills"))

SCREEN.append(screen(
    "K1-BORN-COL-SINGLE",
    [[born_sing[0].a], [Fr(0)]],
    "V_single (2x1) from paper 31 sec.4.3, |.|^2 entrywise [p31-4.3, A2]",
    "the Born column of the singleton: |V_single|^2 as a 2x1 object"))

K1_2 = [[k1_pair[frozenset({tA})], k1_pair[frozenset({tB})]],
        [k1_pair[frozenset({tA})], k1_pair[frozenset({tB})]]]
SCREEN.append(screen(
    "K1-2CONF",
    K1_2,
    "PK1 recomputed from the committed d42b3 layer [A3]; identical to "
    "|V_pair|^2 read on its support",
    "the K1 branch law on the 2-conflict as a SQUARE transfer on the "
    "conflict's own two-token index — K1 is source-independent, so every "
    "row is the same branch law",
    "the only reading in which the K1 layer's Gamma is square on the "
    "REALISED support at both ends; every other square K1 reading below "
    "needs an untrimmed index",
    cert_hint=("surd", real_orth_2x2(K1_2))))

SCREEN.append(screen(
    "K1-PAIR-FULLIDX",
    [[born_pair[0].a, Fr(0), Fr(0), born_pair[1].a] for _ in range(4)],
    "the same Born row on the FULL four-branch index of V_pair [A2, A3]",
    "the Born row replicated over the untrimmed 4-element target index",
    "CONVENTION-RELATIVE: the two zero targets are never realised at the "
    "cut, so this failure is a support mismatch and not a mass defect of "
    "the law; it is reported because the pin asks for the row and "
    "transfer readings both, and the trimmed reading is K1-2CONF above"))

SCREEN.append(screen(
    "K1-SINGLE-2x2",
    [[Fr(1), Fr(0)], [Fr(1), Fr(0)]],
    "V_single's deterministic branch on a 2-element target index [A2]",
    "the deterministic branch replicated over the 2-element index",
    "CONVENTION-RELATIVE for the same reason; trimmed to its support the "
    "object is the 1x1 identity [1], which is trivially unistochastic "
    "with U = [1] and is not counted as evidence"))

_norm = sum(_join_menu)
_jrow = [q / _norm for q in sorted(_join_menu, reverse=True)]
SCREEN.append(screen(
    "K1-JOIN-MENU",
    [list(_jrow) for _ in range(3)],
    "the committed join menu 1/4 + 1/8 + 1/8 [A4, p31-4.3], normalised "
    "within the arbitration sector",
    "the join-cut arbitration menu read as a COLUMN-CONSTANT (source-"
    "independent) 3x3 transfer on its own three outcomes",
    "declared reading; it exists to put the column-constant lemma of "
    "lemma L1 against a NON-uniform generated row"))

report("ARM A (a) time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 4.  ARM A (b) — THE Zhat-COMPLETED SIBLING, REBUILT AND SCREENED
# ===========================================================================

sec("ARM A (b) — THE Zhat-COMPLETED SIBLING, REBUILT FROM CLOSED SCOPE "
    "AND SCREENED (the pin's flagged threat)")

_t = time.time()
CAP_CLOSED = 6
print(f"  building the closed-scope (d42b3) family to depth {CAP_CLOSED} "
      f"...", flush=True)
CFAM, CCACHE = enumerate_line(b3_cand, AB, CAP_CLOSED)
_cum = [sum(1 for h in CFAM if len(h) <= k) for k in range(CAP_CLOSED + 1)]
anchor("Z1 THE CLOSED-SCOPE FAMILY REPRODUCES d43b's CENSUS: cumulative "
       "family sizes at depths 0..6 [u1-closed]",
       _cum == ANCH["closed_census"],
       f"{_cum} (quoted {ANCH['closed_census']})")


def menu_shape_closed(cands):
    d = {}
    for e, q in cands:
        d[(e[0], q)] = d.get((e[0], q), 0) + 1
    return tuple(sorted(d.items(), key=lambda z: sk(z[0])))


def relabel(d, keys):
    relab = {}
    for k in keys:
        relab.setdefault(d[k], len(relab))
    return {k: relab[d[k]] for k in d}


_KEYS = sorted((tuple(h) for h in CFAM), key=sk)
P0 = {k: menu_shape_closed(CCACHE[k]) for k in _KEYS}
P = {0: relabel(P0, _KEYS)}
for t in range(5):
    nxt = {}
    for k in _KEYS:
        if len(k) > 5 - t:
            continue
        nxt[k] = (P[t][k], tuple(sorted(((str(q), P[t][k + (e,)])
                                         for e, q in CCACHE[k]),
                                        key=lambda z: sk(z))))
    P[t + 1] = relabel(nxt, [k for k in _KEYS if len(k) <= 5 - t])
tables = {c: [len({P[t][k] for k in _KEYS if len(k) <= c})
              for t in range(0, 7 - c)] for c in (2, 3, 4)}
anchor("Z2 THE UNIFORM-LOOKAHEAD INTRINSIC PARTITION STABILISES AT SIX "
       "STATES at lookahead t = 2 (d43b MG2a): the |P_t| tables reproduce "
       "the committed anchors [u1-closed]",
       tables == ANCH["Pt_tables"],
       f"cutoff-2 {tables[2]}, cutoff-3 {tables[3]}, cutoff-4 {tables[4]}")

_pB0 = ("p", "B", V0, 0)
REPS = [(), (pA0,), (pA0, _pB0), (pA0, pB1), (pA0, SELFA),
        (pA0, _pB0, SELFA)]
_raw = [P[2][r] for r in REPS]
_repmap = {r: i for i, r in enumerate(_raw)}
CLS = {k: _repmap.get(P[2][k], -1) for k in _KEYS if len(k) <= 4}
_rows, _okwd, _nmem = {}, True, 0
for k in _KEYS:
    if len(k) > 3:
        continue
    _nmem += 1
    r = CLS[k]
    row = {}
    for e, q in CCACHE[k]:
        c2 = CLS[k + (e,)]
        row[c2] = row.get(c2, Fr(0)) + q
    if r in _rows:
        _okwd &= (_rows[r] == row)
    else:
        _rows[r] = row
T6 = [[_rows.get(i, {}).get(j, Fr(0)) for j in range(6)] for i in range(6)]
_rowsums = [sum(_rows.get(i, {}).values()) for i in range(6)]
anchor("Z3 THE EXACT 6x6 TRANSFER IS THE COMMITTED ONE (d43b MG2d): "
       "well-defined per state on every one of the 215 depth-<=3 members, "
       "row sums (2,2,2,5/2,2,2) with the conflict state carrying the "
       "5/4-per-actor excess [u1-closed]",
       _okwd and _nmem == 215 and _rowsums == ANCH["T_rowsums"]
       and len(set(_raw)) == 6,
       f"members {_nmem}; well-defined {_okwd}; row sums "
       f"{fsl(_rowsums)}")

fper = ANCH["f_perron"]
lam = ANCH["lam"]
_eig = all(sum(T6[i][j] * fper[j] for j in range(6)) == lam * fper[i]
           for i in range(6))
ZH = [[T6[i][j] * fper[j] / (lam * fper[i]) for j in range(6)]
      for i in range(6)]
_conf = {j: ZH[3][j] for j in range(6) if ZH[3][j] != 0}
_zcols = [sum(ZH[i][j] for i in range(6)) for j in range(6)]
anchor("Z4 THE Zhat COMPLETION IS THE AUDIT'S OBJECT, ENTRY FOR ENTRY: "
       "T f = 2 f exactly with f = (4,4,3,7,3,3)/3; every row of "
       "Zhat(i->j) = T_ij f_j / (lambda f_i) sums to exactly 1 with "
       "non-negative entries; the conflict row is exactly {0: 1/7, "
       "3: 3/4, 5: 3/28}; and the column sums are exactly 25/28, 1, "
       "59/64, 55/64, 31/32, 19/14 [u1-zhat]",
       _eig and all(sum(ZH[i]) == 1 for i in range(6))
       and all(ZH[i][j] >= 0 for i in range(6) for j in range(6))
       and _conf == ANCH["conflict_row"]
       and _zcols == ANCH["zhat_colsums"],
       f"T f = 2 f {_eig}; conflict row "
       f"{ {k: str(v) for k, v in sorted(_conf.items())} }; column sums "
       f"{[str(x) for x in _zcols]}")

SCREEN.append(screen(
    "ZHAT-6x6",
    ZH,
    "the Zhat-completed six-state record chain, rebuilt here from the "
    "closed-scope family [Z1-Z4]; specified by the D75 audit pin (b) and "
    "handed to U3 by U1 sec.14 [u1-zhat]",
    "the completed state-to-state transfer, ROW-stochastic (the corpus's "
    "convention)"))

SCREEN.append(screen(
    "ZHAT-6x6-TRANSPOSED",
    [[ZH[j][i] for j in range(6)] for i in range(6)],
    "the same object read in [B3]'s own convention [B3-conv]",
    "Gamma_ij = p(i,t | j,0), i.e. COLUMN-stochastic — the transpose",
    "printed because the doubly-stochastic precondition is exactly the "
    "statement that this choice does not matter, and here it does"))

print("""
  THE SHARPENER THE AUDIT PREDICTED, RUN.  [d75-5.3] reasoned: unistochastic
  => doubly stochastic => uniform stationary law for an irreducible chain,
  and 'a chain with that structure will not have a uniform stationary law'.
  That was graded [MY READING].  It is now measured, and it is sharper than
  predicted — the chain is not irreducible at all.
""")
_adj = {i: [j for j in range(6) if ZH[i][j] != 0] for i in range(6)}


def _reach(i):
    s, st = {i}, [i]
    while st:
        x = st.pop()
        for y in _adj[x]:
            if y not in s:
                s.add(y)
                st.append(y)
    return s


_R = {i: _reach(i) for i in range(6)}
_closed_cls = sorted(i for i in range(6)
                     if all(j in _R[i] and i in _R[j] for j in _R[i]))
_transient = [i for i in range(6) if i not in _closed_cls]
_pi = {2: Fr(1, 4), 4: Fr(1, 4), 5: Fr(1, 2)}
_pivec = [_pi.get(i, Fr(0)) for i in range(6)]
_stat_ok = all(sum(_pivec[i] * ZH[i][j] for i in range(6)) == _pivec[j]
               for j in range(6)) and sum(_pivec) == 1
check("Z5 THE COMPLETED CHAIN IS NOT IRREDUCIBLE AND ITS STATIONARY LAW "
      "IS NOT UNIFORM — THE AUDIT'S [MY READING] IS CONFIRMED AND "
      "SHARPENED.  States {2,4,5} form the unique closed communicating "
      "class and states {0,1,3} — including the CONFLICT state 3 — are "
      "TRANSIENT.  The unique stationary law is exactly "
      "(0, 0, 1/4, 0, 1/4, 1/2): three of its six entries are exactly "
      "zero, so it is not merely non-uniform, it is singular with respect "
      "to the uniform law.  A doubly-stochastic matrix always has the "
      "uniform law stationary, so this is a SECOND exact certificate that "
      "Zhat is not unistochastic, independent of the column sums",
      _closed_cls == [2, 4, 5] and _transient == [0, 1, 3] and _stat_ok,
      f"closed class {_closed_cls}; transient {_transient}; stationary "
      f"law {[str(x) for x in _pivec]}; pi Zhat = pi exactly {_stat_ok}")

ZH345 = [[ZH[i][j] for j in (2, 4, 5)] for i in (2, 4, 5)]
SCREEN.append(screen(
    "ZHAT-CLOSED-3x3",
    ZH345,
    "the unique closed communicating class {2,4,5} of the Zhat chain "
    "[Z4, Z5] — a GENERATED 3x3 stochastic matrix, and the only one this "
    "census contains",
    "the sub-transfer on the absorbing class, row-stochastic by "
    "closedness",
    "the one object on which the n = 3 criterion meets generated data"))

report("ARM A (b) time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 5.  ARM A (c) — THE ARM-C2 CONTROL, AND THE COLUMN-CONSTANT LEMMA
# ===========================================================================

sec("ARM A (c) — THE ARM-C2 COLUMN-CONSTANT TRANSFER (the degenerate "
    "control), AND THE COLUMN-CONSTANT LEMMA")

print(f"""
  PROVENANCE, STATED PLAINLY.  This matrix is taken BY SPECIFICATION from
  U1's committed receipt and is NOT re-derived here ({QUOTES['u1-armc2'][0]}):
    "{QUOTES['u1-armc2'][1]}"
  The depth-9 conditioned enumeration that produces it is U1's, and U3 is
  a file-disjoint parallel unit.  What this receipt supplies instead is a
  THEOREM that makes the verdict independent of the quoted arithmetic: for
  a column-constant transfer, doubly-stochastic is equivalent to uniform.
""")

n8 = ANCH["armc2_labels"]
ARMC2 = [[ANCH["armc2_entry"]] * n8 for _ in range(n8)]

_lemma_bad = []
for _n in (2, 3, 4, 5, 6, 8):
    for _trial in range(1, 6):
        _v = [Fr(_trial * (k + 1) % 7 + 1, 1) for k in range(_n)]
        _s = sum(_v)
        _v = [x / _s for x in _v]
        _M = [list(_v) for _ in range(_n)]
        _r = ds_report(_M)
        _uniform = all(x == Fr(1, _n) for x in _v)
        if _r["ds"] != _uniform:
            _lemma_bad.append((_n, _trial, _v))
check("L1 THE COLUMN-CONSTANT LEMMA, PROVED AND THEN VERIFIED: an n x n "
      "matrix all of whose rows equal one probability vector v has row "
      "sums 1 automatically and column sums n.v_j, so it is doubly "
      "stochastic IF AND ONLY IF v is the uniform law.  Proof: n.v_j = 1 "
      "for every j iff v_j = 1/n.  Verified on 30 constructed "
      "column-constant matrices at six sizes; the equivalence never "
      "fails.  CONSEQUENCE, and it is the whole content of this section: "
      "among column-constant generated transfers the ONLY doubly-"
      "stochastic one is the maximally forgetful one",
      not _lemma_bad, f"{len(_lemma_bad)} counterexamples over 30 trials "
                      f"at sizes 2,3,4,5,6,8")

U_H8 = [[Surd({2: Fr(_H8[i][j], 4)}) for j in range(8)] for i in range(8)]
U_DFT8 = [[cyc_pow(cyc_x(8), (i * j) % 8) * 1 * INV_SQRT8 for j in range(8)]
          for i in range(8)]
_c8_uni = unitary_check_cyc(U_DFT8)
_c8_mod = modsq_check_cyc(U_DFT8, ARMC2)
check("L2 THE 8x8 FLAT MATRIX HAS A COMPLEX CERTIFICATE TOO, AND IT IS "
      "EXACT: the 8-point DFT U_jk = zeta_8^{jk}/sqrt8 written in "
      "Q(zeta_8) satisfies U^dagger U = I with zero residual and "
      "|U_ij|^2 = 1/8 at all 64 entries.  Both certificates are "
      "exhibited so that the ORTHO/UNI question can be decided on this "
      "object rather than assumed",
      not _c8_uni and not _c8_mod,
      f"unitarity residuals {len(_c8_uni)}; |U|^2 mismatches "
      f"{len(_c8_mod)}")

SCREEN.append(screen(
    "ARMC2-8x8",
    ARMC2,
    "U1 ARM-C2's renewal-to-renewal transfer [u1-armc2], taken BY "
    "SPECIFICATION (see the note above)",
    "the column-constant transfer on the 8 payload-enriched renewal "
    "labels: every entry exactly 1/8",
    "the pin's degenerate control.  Its certificate is REAL — Sylvester's "
    "Hadamard matrix of order 8 [lit-had, KA-6] — so it is not merely "
    "unistochastic but ORTHOSTOCHASTIC, and the complex numbers are NOT "
    "forced by it (L2 exhibits the complex certificate as well)",
    cert_hint=("surd", U_H8)))


# ===========================================================================
# SEC 5.5  THE MULTIPLICITY CENSUS, AND THE SIZE OF THE K1 OUTCOME SPACE
# ===========================================================================

sec("THE MULTIPLICITY CENSUS — WHAT THE COMMITTED GRAMMAR ACTUALLY "
    "GENERATES, AND HOW BIG THE K1 OUTCOME SPACE IS")

print(f"""
  THE PREMISE THIS SECTION REPLACES.  Paper 31 sec.4.3's "{{1, 2}}" is a
  line about a FIXTURE and its own Scope sentence says so
  ({QUOTES['p31-4.3'][0]}):
    "{QUOTES['p31-4.3'][1]}"
  A two-actor pair-plus-path fixture bounds a fixture.  It does not bound
  the grammar, and the corpus's THREE-actor pool is committed and available
  (v10/code/d42b1_transport_exact.py, the (A,B,C) pool declared at :435).
  It is enumerated here and censused.

  AND THE QUANTITY THAT DECIDES THE SCREEN IS NOT THE COMPONENT SIZE.  A
  conflict component of size m does NOT give an m x m Gamma.  The K1 law is
  supported on the MAXIMAL INDEPENDENT SETS of the realised conflict graph
  (the layer's own mis_of, and admissible() refuses any wkey outside it), so
  the outcome space -- and therefore the square Gamma the screen sees -- has
  size |MIS|, not |ckey|.  Both are measured below, on every pool this
  receipt loads.

  THE ROUND'S FINDING, RE-MEASURED FROM THE LAYER, NOT COPIED
  ({QUOTES['u3-round-B1'][0]}):
    "{QUOTES['u3-round-B1'][1]}"
""")

_t = time.time()
CAP_AB, CAP_ABC = 4, 3
print("  enumerating the committed pools and replaying the layer's own "
      "admission geometry on every arbitration event ...", flush=True)

POOLS = []
for _pnm, _PL, _pfam in (
        ("ABC3   d42b1 (A,B,C) depth <= 3", B1,
         line_family(b1_cand, ABC, CAP_ABC, "ABC3")),
        ("AB4    d42b1 (A,B) depth <= 4", B1,
         line_family(b1_cand, AB, CAP_AB, "AB4")),
        (f"CLOSED d42b3 (A,B) depth <= {CAP_CLOSED}", B3, (CFAM, CCACHE))):
    _pf, _pc = _pfam
    _rec = dict(name=_pnm, L=_PL, fam=_pf, cache=_pc, ck=Counter(),
                mis=Counter(), parts=Counter(), nonmp=0, vals=set(),
                unmatched=0, ev3=[])
    for _h in _pf:
        for _e, _q in _pc[tuple(_h)]:
            if _e[0] != "r":
                continue
            _rec["ck"][len(_e[2])] += 1
            _g = arb_geometry(_PL, _h, _e)
            if _g is None:
                _rec["unmatched"] += 1
                continue
            _vw, _cp, _ckey, _et, _ms, _lw = _g
            _rec["mis"][len(_ms)] += 1
            _cls = sorted({_t3[2] for _t3 in _ckey})
            _rec["parts"][len(_cls)] += 1
            _rec["vals"] |= set(_cls)
            _mp = all(((tuple(sorted((_a, _b))) in _et) == (_a[2] != _b[2]))
                      for _a in _ckey for _b in _ckey if _a < _b)
            _rec["nonmp"] += int(not _mp)
            if set(_lw) != set(_ms):
                _rec["nonmp"] += 1
            if len(_e[2]) >= 3:
                _rec["ev3"].append((tuple(_h), _e, _q))
    POOLS.append(_rec)
    report(f"pool {_pnm}", f"{len(_pf)} histories; admissible arbitration "
           f"events {sum(_rec['ck'].values())}; |ckey| census "
           f"{dict(sorted(_rec['ck'].items()))}; |MIS| census "
           f"{dict(sorted(_rec['mis'].items()))}; value classes per "
           f"conflict {dict(sorted(_rec['parts'].items()))}; realised "
           f"proposal values {sorted(_rec['vals'])}")

P3 = POOLS[0]
_h3set = sorted({z[0] for z in P3["ev3"]}, key=lambda z: (len(z), sk(z)))
check("M1 THE COMMITTED GRAMMAR GENERATES MULTIPLICITY-3 CONFLICTS — THE "
      "PREVIOUS ROUND'S PREMISE IS WITHDRAWN AS FALSE.  Censusing every "
      "ADMISSIBLE arbitration event of the committed d42b1 (A,B,C) "
      "depth-<=3 family — the SAME 3,424-history pool Arm B screens — by "
      "the size of the conflict it resolves gives |ckey| = {1: 3096, "
      "2: 1536, 3: 216} [u3-round-B1].  Multiplicity 3 is REALISED, and "
      "shallowly.  'The corpus has committed none' was a FIXTURE-SCOPE "
      "reading of paper 31's two-actor Scope line and is deleted wherever "
      "it appeared",
      len(P3["fam"]) == ANCH["ABC_hist"]
      and dict(P3["ck"]) == ANCH["ABC3_ckey_census"]
      and P3["unmatched"] == 0,
      f"family {len(P3['fam'])}/{ANCH['ABC_hist']}; |ckey| census "
      f"{dict(sorted(P3['ck'].items()))}; multiplicity-3 events "
      f"{len(P3['ev3'])} on {len(_h3set)} distinct histories, shallowest at "
      f"depth {min(len(z) for z in _h3set)}; arbitration events whose "
      f"component the layer could not match: {P3['unmatched']}")

_w3 = sorted(P3["ev3"], key=lambda z: (len(z[0]), sk(z[0]), sk(z[1])))
_hw, _ew, _qw = _w3[0]
_vw, _cpw, _ckw, _etw, _misw, _laww = arb_geometry(B1, _hw, _ew)
_outs = sorted(_laww, key=sk)
_menu3 = sorted(((e, q) for e, q in P3["cache"][_hw]
                 if e[0] == "r" and e[1] == _ew[1] and e[2] == _ckw),
                key=lambda z: sk(z[0]))

print("\n  THE FIRST MULTIPLICITY-3 WITNESS, PRINTED IN FULL")
print("  " + "-" * 74)
for _i, _op in enumerate(_hw):
    print(f"    event {_i}: {_op}")
print(f"    conflict resolved (|ckey| = {len(_ckw)}):")
for _t3 in sorted(_ckw, key=repr):
    print(f"      {_t3}")
print(f"    conflict edges ({len(_etw)}):")
for _ed in sorted(_etw, key=repr):
    print(f"      {_ed[0]} -- {_ed[1]}")
print(f"    MAXIMAL INDEPENDENT SETS ({len(_misw)}) — the outcome space:")
for _w in _outs:
    print(f"      {sorted(_w, key=repr)}   K1 weight {_laww[_w]}")
print("    the committed arbitration menu on this conflict:")
for _e, _q in _menu3:
    print(f"      winner {sorted(_e[3], key=repr)}   menu weight {_q}")
print("  " + "-" * 74)

_menu_ok = ([q for e, q in _menu3] != []
            and sorted(q for e, q in _menu3) == sorted(ANCH["mult3_menu"])
            and all(q == Fr(1, 4) * _laww[e[3]] for e, q in _menu3))
check("M2 THE WITNESS IS COMMITTED ARITHMETIC, NOT A CONSTRUCTION.  The "
      "shallowest multiplicity-3 arbitration in the committed pool sits at "
      "depth 3 on the history [('p','A',v0,0), ('p','B',v0,0), "
      "('p','C',v0,1)].  Its menu weights are the committed 1/6 and 1/12, "
      "its committed K1 law is {A0,B0} -> 2/3 and {C1} -> 1/3, and the two "
      "are locked to each other by the layer's own pricing: the menu "
      "weight is exactly 1/4 . PK1(winner) at a single available component "
      "[u3-round-B1]",
      sorted(_laww.values()) == ANCH["mult3_law"] and _menu_ok
      and len(_hw) == 3,
      f"menu weights {sorted(str(q) for e, q in _menu3)}; K1 law "
      + "; ".join(f"{[t3[0] + str(t3[2]) for t3 in sorted(w, key=repr)]} -> "
                  f"{_laww[w]}" for w in _outs)
      + f"; menu = 1/4 . PK1 on every winner: "
        f"{all(q == Fr(1, 4) * _laww[e[3]] for e, q in _menu3)}")

check("M3 A MULTIPLICITY-3 CONFLICT HAS A 2-OUTCOME K1 LAW — THE OUTCOME "
      "SPACE IS |MIS|, NOT |ckey|.  The committed conflict graph on this "
      "3-component is A0 -- C1 and B0 -- C1 and NOT A0 -- B0 (A and B "
      "propose the SAME value, so they do not conflict), so its maximal "
      "independent sets are exactly {A0,B0} and {C1}: TWO of them.  "
      "admissible() refuses every wkey outside mis_of, so the K1 law's "
      "support is exactly that set and the square Gamma the screen sees is "
      "2 x 2.  A 3-component does NOT give a 3 x 3 Gamma here",
      len(_misw) == 2 and set(_laww) == set(_misw)
      and len(_ckw) == 3 and len(_etw) == 2,
      f"|ckey| = {len(_ckw)}; conflict edges {len(_etw)}; |MIS| = "
      f"{len(_misw)}; K1 support = MIS "
      f"{set(_laww) == set(_misw)}")

_mismax = max(k for P in POOLS for k in P["mis"])
_nonmp = sum(P["nonmp"] for P in POOLS)
_allvalsx = sorted({v for P in POOLS for v in P["vals"]})
_partsok = all(P["mis"] == P["parts"] for P in POOLS)
check("M4 THE OUTCOME SPACE IS OF SIZE AT MOST 2 ON EVERY POOL THIS "
      "RECEIPT LOADS — MEASURED, NOT PROVED.  Over all three committed "
      "pools (d42b1 (A,B,C) d<=3, d42b1 (A,B) d<=4, d42b3 closed scope "
      "(A,B) d<=6) the |MIS| census never leaves {1, 2}, on every "
      "admissible arbitration event.  The measured MECHANISM: the realised "
      "conflict graph on every component is EXACTLY the complete "
      "multipartite graph whose parts are the proposal-VALUE classes (edge "
      "iff the two proposals differ in value: 0 exceptions over all three "
      "pools), so its maximal independent sets are exactly those parts; "
      "and the committed proposal alphabet is BINARY, so there are at most "
      "2 parts.  This is a fact about the ACTOR POOL and the VALUE "
      "ALPHABET, not about the depth: it is measured here and is UNPROVED "
      "beyond these pools",
      _mismax == ANCH["mis_max"] and _nonmp == 0 and _partsok
      and _allvalsx == list(range(ANCH["prop_values"])),
      f"max |MIS| over all pools {_mismax}; |MIS| censuses "
      f"{[dict(sorted(P['mis'].items())) for P in POOLS]}; "
      f"conflict graphs that are NOT complete multipartite by value class: "
      f"{_nonmp}; |MIS| = #value classes on every event: {_partsok}; "
      f"realised proposal values {_allvalsx}")

print(f"""
  THE ROUND'S WIDER EXTENSION, CITED AND NOT RE-RUN.  A fourth actor pool
  (A,B,C,D) at depth <= 4 — 332,697 histories — was enumerated in the U3
  round and returns the |MIS| census {{1: 232264, 2: 98304}}: never 3
  [u3-round-B1].  It is carried here as ROUND-VERIFIED EVIDENCE and is NOT
  a gate of this receipt; the printed caps name the three pools that are.
""")

_G3 = [[_laww[_outs[0]], _laww[_outs[1]]] for _ in range(2)]
SCREEN.insert(6, screen(
    "K1-3CONF",
    _G3,
    "the committed K1 law on the FIRST generated multiplicity-3 conflict, "
    "recomputed from the d42b1 layer [M1, M2, M3, u3-round-B1]",
    "the K1 branch law on the 3-conflict as a SQUARE transfer on its own "
    "OUTCOME index — the two maximal independent sets {A0,B0} and {C1}; K1 "
    "is source-independent, so every row is the same branch law",
    "the first substantive NON-FLAT K1 reading in this census.  It is "
    "column-constant with a NON-uniform row, so L1 decides it: it fails the "
    "doubly-stochastic precondition and the price is exact"))

_S3 = [s for s in SCREEN if s["name"] == "K1-3CONF"][0]
check("M5 THE MULTIPLICITY-3 K1 LAW FAILS THE SCREEN AT THE MASS LEVEL, "
      "AND ITS PRICE IS EXACT.  Read as the square transfer on its own "
      "2-element outcome space the law is column-constant with row "
      "(2/3, 1/3); its column sums are (4/3, 2/3) and by L1 a "
      "column-constant matrix is doubly stochastic only when its row is "
      "uniform.  The exact price is 2/3.  So the one generated K1 object "
      "that is NOT flat does not even reach the phase question — the same "
      "verdict every other substantive generated transfer gets, and the "
      "opposite of the two flat passers",
      _S3["verdict"] == "S-FAIL-DS"
      and _S3["R"]["colsums"] == ANCH["mult3_gamma_colsums"]
      and _S3["R"]["L1col"] == ANCH["mult3_price"],
      f"verdict {_S3['verdict']}; column sums "
      f"{[str(x) for x in _S3['R']['colsums']]}; price "
      f"{_S3['R']['L1col']}")

report("multiplicity census time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 6.  ARM A — THE CENSUS, AND THE TWO STRUCTURAL VERDICTS
# ===========================================================================

sec("ARM A — THE CENSUS, AND THE TWO STRUCTURAL VERDICTS")

_tally = Counter(s["verdict"] for s in SCREEN)
print()
print("  THE SCREEN CENSUS")
print("  " + "-" * 74)
print(f"  {'matrix':<24}{'shape':<12}{'verdict':<18}exact datum")
print("  " + "-" * 74)
for s in SCREEN:
    M = s.get("M")
    if M is None and s["verdict"] == "N/A-SHAPE":
        shape = "non-square"
        datum = "Barandes' criterion is undefined at this shape"
    else:
        shape = f"{len(M)}x{len(M[0])}"
        if s["verdict"] == "S-FAIL-DS":
            R = s["R"]
            side = "col" if R["L1col"] >= R["L1row"] else "row"
            dfc = R["coldef"] if side == "col" else R["rowdef"]
            datum = (f"{side} deficits {[str(x) for x in dfc]}, "
                     f"sum|.| = {max(R['L1col'], R['L1row'])}")
            if s.get("T") is not None and s["T"] < 0:
                datum += f"; and T = {s['T']} < 0"
        elif s["verdict"] == "S-FAIL-UNI":
            datum = f"triangle discriminant T = {s.get('T')}"
        elif s["verdict"] == "S-PASS":
            datum = (f"certificate exhibited and verified "
                     f"({'real orthogonal' if s['cert'] == 'surd' else 'complex unitary'})")
        else:
            datum = ""
    print(f"  {s['name']:<24}{shape:<12}{s['verdict']:<18}{datum}")
print("  " + "-" * 74)
report("verdict tally", dict(sorted(_tally.items())))
report("readings screened", f"{len(SCREEN)} in all")

_passers = [s for s in SCREEN if s["verdict"] == "S-PASS"]
_ortho = [s for s in _passers if s["cert"] == "surd"]
check("A5 THE CENSUS IS MIXED, AND THE CENSUS IS THE RESULT.  ELEVEN "
      "readings are screened, and they are not eleven independent "
      "matrices: they are FOUR distinct committed generated matrices "
      "(K1-2CONF, K1-3CONF, ZHAT-6x6 and its closed 3x3 sub-block), FIVE "
      "constructed or convention-relative readings of those (the two Born "
      "columns, the two untrimmed-index rows, the normalised join menu), "
      "ONE transpose duplicate, and ONE by-specification control.  Of the "
      "eleven, TWO are non-square and therefore unscreenable by Barandes' "
      "criterion, SEVEN fail the doubly-stochastic precondition outright "
      "(S-FAIL-DS), and TWO pass with an exhibited and verified unitary "
      "(S-PASS).  No reading reaches the S-FAIL-UNI cell — every generated "
      "object that would have had to be argued at the phase level is "
      "already excluded at the mass level — and no reading is left "
      "EXCLUDED-BY-CAP, so the instrument decided every object it was "
      "given",
      _tally.get("EXCLUDED-BY-CAP", 0) == 0
      and _tally.get("CERTIFICATE-FAILED", 0) == 0
      and len(SCREEN) == 11
      and _tally.get("N/A-SHAPE", 0) == 2
      and _tally.get("S-FAIL-DS", 0) == 7
      and _tally.get("S-FAIL-UNI", 0) == 0
      and _tally.get("S-PASS", 0) == 2,
      f"{dict(sorted(_tally.items()))} over {len(SCREEN)} readings")

_flat = [s for s in _passers
         if all(s["M"][i][j] == Fr(1, len(s["M"]))
                for i in range(len(s["M"])) for j in range(len(s["M"])))]
check("A6 EVERY MATRIX THAT PASSES THE SCREEN IS ORTHOSTOCHASTIC — AND "
      "BOTH PASSERS ARE THE FLAT MATRIX J/n, SO THE PASS CARRIES NO "
      "QUANTUM CONTENT.  Both passers carry a REAL orthogonal "
      "certificate, exhibited and verified: K1-2CONF by the 2x2 Hadamard "
      "construction and ARMC2-8x8 by Sylvester's order-8 Hadamard matrix. "
      " And both are FLAT, entry for entry: K1-2CONF is "
      "[[1/2,1/2],[1/2,1/2]] = J/2 and ARMC2-8x8 is J/8.  They therefore "
      "pass for ONE reason, not two: each is column-constant, and by L1 "
      "the only doubly-stochastic column-constant law is the uniform one, "
      "which is J/n — which is unistochastic at every n (the DFT) and "
      "orthostochastic at every n = 2^k (Sylvester).  The ortho/uni gap, "
      "which the D75 audit identifies as the exact place the necessity of "
      "i lives, is EMPTY on this census; KA-3 shows the property is not "
      "vacuous, since J/3 is unistochastic and NOT orthostochastic",
      len(_ortho) == len(_passers) and len(_passers) > 0
      and len(_flat) == len(_passers),
      f"passers {[s['name'] for s in _passers]}; of which "
      f"orthostochastic {[s['name'] for s in _ortho]}; of which FLAT J/n "
      f"{[s['name'] for s in _flat]}")

_sweep = [Fr(k, 12) for k in range(13)]
_sweep_bad = []
for _p in _sweep:
    _B = [[_p, 1 - _p], [1 - _p, _p]]
    _U = real_orth_2x2(_B)
    if orth_check_surd(_U) or modsq_check_surd(_U, _B):
        _sweep_bad.append(_p)
check("A7 THE K1 OUTCOME SPACE IS OF SIZE AT MOST 2 — MEASURED AT THE FOUR "
      "COMMITTED POOLS, UNPROVED BEYOND THEM — AND AT THAT SIZE i IS "
      "UNDECIDABLE.  The premise is NOT paper 31's {1,2}, which is a "
      "two-actor FIXTURE line [p31-4.3]; the premise is the measurement of "
      "M1-M4: on d42b1 (A,B,C) d<=3, d42b1 (A,B) d<=4 and the d42b3 closed "
      "scope d<=6 the number of maximal independent sets of a realised "
      "conflict — the size of the K1 law's outcome space, and so of the "
      "square Gamma — is never more than 2 (M4), and the round's fourth "
      "pool (A,B,C,D) d<=4, 332,697 histories, agrees [u3-round-B1].  "
      "Multiplicity 3 IS generated (M1) and still gives a 2-outcome law "
      "(M3).  At size <= 2 the question closes: 1x1 is trivially "
      "orthostochastic, every 2x2 bistochastic matrix is orthostochastic "
      "by KA-4's uniform construction (re-verified here across a printed "
      "sweep of the branch weight p, so it is checked and not cited), and "
      "by L1 the only column-constant 2-outcome law that is doubly "
      "stochastic at all is the uniform one.  DECIDING i THEREFORE "
      "REQUIRES A >= 3-OUTCOME K1 LAW, which needs non-binary proposal "
      "values or conflict graphs that are not complete multipartite — a "
      "fact about the ACTOR POOL and the VALUE ALPHABET, not about "
      "structure and not about depth",
      not _sweep_bad and _mismax == ANCH["mis_max"],
      f"max |MIS| over the three receipt-gated pools {_mismax} (M4); the "
      f"2x2 orthostochastic construction verified exactly at p in "
      f"{[str(x) for x in _sweep]} — {len(_sweep_bad)} failures")

print(f"""
  THE PRICE OF ENRICHMENT, STATED EXACTLY (the pin's S-FAIL-DS outcome).
  For every doubly-stochastic D and every screened matrix M, the ENTRYWISE
  L1 distance — ||M - D||_1 := sum_ij |M_ij - D_ij|, an entrywise sum and
  NOT an operator norm — obeys ||M - D||_1 >= sum_j |c_j(M) - 1|, because
  sum_j |c_j(M) - c_j(D)| <= sum_ij |M_ij - D_ij| and c_j(D) = 1.  Every
  number below is an ABSOLUTE quantity in units of probability mass, not a
  fraction of the matrix: a row-stochastic 6x6 carries total mass 6, so
  Zhat's 5/7 is five sevenths of ONE unit of mass out of six.  The exact
  prices this census establishes are:
    ZHAT-6x6            : >= {ds_report(ZH)['L1col']}   (column sums {[str(x) for x in _zcols]}; total mass 6)
    ZHAT-CLOSED-3x3     : >= {ds_report(ZH345)['L1col']}   and it carries a SECOND, independent
                          obstruction: its unitarity-triangle discriminant is
                          T = {tri_disc(*chain_link_squares(ZH345, 0, 1, 'col'))} < 0, so even a mass repair that fixed
                          its column sums would have to move a phasor modulus too.
                          This is the corpus's one generated 3x3 matrix and it
                          fails the screen twice over.
    K1-JOIN-MENU        : >= {ds_report([list(_jrow) for _ in range(3)])['L1col']}
    K1-3CONF            : >= {_S3['R']['L1col']}   (column sums {[str(x) for x in _S3['R']['colsums']]}; total mass 2)
                          the generated multiplicity-3 K1 law, and the only
                          substantive NON-FLAT K1 object in the census.
  That is what a quantum-eligible completion of the record chain must move,
  and it is a mass statement, not a phase statement: no amount of phase
  freedom repairs a column sum.
""")


# ===========================================================================
# SEC 7.  ARM B — THE U(1) LOOP-CLASS THEOREM, AND ITS REPRODUCTION
# ===========================================================================

sec("ARM B — THE U(1) LOOP-CLASS THEOREM, LOCATED, RESTATED, AND ITS "
    "REPRODUCTION ATTEMPTED ON D74's GENERATED CARRIER")

print(f"""
  THE THEOREM, LOCATED AND RESTATED FROM ITS OWN FILE.

  {QUOTES['p7-7.1'][0]}
    "{QUOTES['p7-7.1'][1]}"

  {QUOTES['p7-D3'][0]}
    "{QUOTES['p7-D3'][1]}"

  THE CATALOG'S BINDING CORRECTIONS, CARRIED ([V11-CAT] sec.4.3(c)):
    the theorem's standing is CONTESTED and unresolved at four documents
    (derived in v6 p7 / INPUT in paper Va / un-forceable in v8 p2 /
    seal-blind in companion-B), and a GUARD must travel with any citation:
    Thm D1 is the ancilla-summed dilation every stochastic matrix admits
    and is NOT the unistochasticity answer [d75-D1guard].  D1 is set aside
    throughout this receipt.

  WHAT REPRODUCTION MEANS HERE, DECLARED BEFORE THE MEASUREMENT.  D3 has
  three separable clauses and they are tested one at a time:
    (i)   the loop class is GAUGE-INVARIANT;
    (ii)  the loop class is U(1)-VALUED (Thm 7.1's conclusion);
    (iii) two-route interference IS the loop-phase law
          P = |A|^2 + |B|^2 + 2|A||B| cos(arg B(loop)).
  The carrier is D74's: the coarsest descent quotient of the committed
  transport grammar, on which the transport holonomy lives.
""")

_t = time.time()
ARMS = {}
for _nm, _actors, _dep, _pref in (("AB4", AB, CAP_AB, "AB"),
                                  ("ABC3", ABC, CAP_ABC, "ABC")):
    print(f"  running D74's square census on {_nm} ...", flush=True)
    fam, cache = line_family(b1_cand, _actors, _dep, _nm)
    st, rat, kinds, okinds, defs, half, closed = square_census(
        fam, cache, _actors, _dep, b1_adm, b1_regs, b1_canon)
    dely = sum(1 for h, a, b, r, *_ in defs if "d" in (a[0], b[0]))
    mind = min((len(h) + 2 for h, *_ in defs), default=None)
    ARMS[_nm] = dict(fam=fam, cache=cache, defs=defs, closed=closed,
                     st=st, rat=rat, half=half)
    report(f"{_nm} census", f"{len(fam)} histories; {dict(st)}; non-unit "
           f"{len(defs)}; ratios {fmt(rat)}; kinds {dict(kinds)}; "
           f"delivery-bearing {dely}/{len(defs)}; shallowest {mind}")
    anchor(f"B1.{_pref} D72's T6.1 ROW REPRODUCES EXACTLY [T6.1] — family "
           f"size, closed-square count, the FULL ratio multiset, the kind "
           f"census and the delivery-bearing fraction",
           len(fam) == ANCH[_pref + "_hist"]
           and st["closed"] == ANCH[_pref + "_closed"]
           and dict(rat) == ANCH[_pref + "_full_ratios"]
           and dict(kinds) == ANCH[_pref + "_kinds"]
           and dely == len(defs) == ANCH[_pref + "_defects"],
           f"histories {len(fam)}/{ANCH[_pref + '_hist']}; closed "
           f"{st['closed']}/{ANCH[_pref + '_closed']}; non-unit "
           f"{len(defs)}/{ANCH[_pref + '_defects']}")

_stAB = ARMS["AB4"]["st"]
anchor("B2 D72's T6.2 HALF-OPEN ROW REPRODUCES EXACTLY [T6.2]: 40 "
       "half-open squares at AB4, 28 AB-only and 12 BA-only — the third "
       "committed number of the 88 / 40 / 12 census this arm re-anchors on",
       _stAB.get("AB-only", 0) == ANCH["AB_ABonly"]
       and _stAB.get("BA-only", 0) == ANCH["AB_BAonly"]
       and _stAB.get("AB-only", 0) + _stAB.get("BA-only", 0)
       == ANCH["AB_halfopen"]
       and _stAB["both-blocked"] == ANCH["AB_bothblocked"],
       f"AB-only {_stAB.get('AB-only', 0)}, BA-only "
       f"{_stAB.get('BA-only', 0)}, total "
       f"{_stAB.get('AB-only', 0) + _stAB.get('BA-only', 0)}; "
       f"both-blocked {_stAB['both-blocked']}")

for _nm, _pref in (("AB4", "AB"), ("ABC3", "ABC")):
    R = ARMS[_nm]
    V = {tuple(h): A_menu(tuple(h), R["cache"]) for h in R["fam"]}
    seen, unseen = [], []
    for row in R["defs"]:
        hh, a, b = row[0], row[1], row[2]
        (seen if V[hh + (a, b)] == V[hh + (b, a)] else unseen).append(row)
    cong, iters = congruence(R)
    R["V"] = V
    R["seen"], R["unseen"] = seen, unseen
    R["menu_cls"] = len({v for v in V.values()})
    R["cong_cls"] = len(set(cong.values()))
    R["cong_def"] = sum(1 for hh, a, b, r, *_ in R["defs"]
                        if cong[hh + (a, b)] == cong[hh + (b, a)])
    ex = [(V[hh + (b, a)], V[hh + (a, b)], r) for hh, a, b, r in R["closed"]]
    R["ex"] = ex
    R["selfh"] = Counter(w for u, v, w in ex if u == v)
    R["offh"] = holonomy_of([e for e in ex if e[0] != e[1]])
    report(f"{_nm} carrier", f"menu quotient {R['menu_cls']} classes; "
           f"coarsest congruence {R['cong_cls']} classes after {iters} "
           f"rounds; of {len(R['defs'])} defective squares the menu "
           f"quotient CLOSES {len(seen)} and the congruence closes "
           f"{R['cong_def']}; self-loop holonomy (non-unit) "
           f"{fmt(Counter({k: v for k, v in R['selfh'].items() if k != 1}))}"
           f"; off-loop cycles {R['offh'][2]} of which {R['offh'][3]} "
           f"non-trivial")

_A4 = ARMS["AB4"]
_A3 = ARMS["ABC3"]
anchor("B3 D74's CARRIER TABLE REPRODUCES EXACTLY [d74-carrier]: AB4 has "
       "113 menu classes and 185 congruence classes and both close 44 of "
       "the 88 defective squares (the 44 + 44 split); ABC3 has 117 / 162 "
       "and both close 0 of 12",
       len(_A4["seen"]) == ANCH["AB_seen"]
       and len(_A4["unseen"]) == ANCH["AB_unseen"]
       and _A4["cong_def"] == ANCH["AB_seen"]
       and _A4["menu_cls"] == ANCH["AB_menu_cls"]
       and _A4["cong_cls"] == ANCH["AB_cong_cls"]
       and len(_A3["seen"]) == ANCH["ABC_seen"]
       and len(_A3["unseen"]) == ANCH["ABC_unseen"]
       and _A3["menu_cls"] == ANCH["ABC_menu_cls"]
       and _A3["cong_cls"] == ANCH["ABC_cong_cls"],
       f"AB4 seen/unseen {len(_A4['seen'])}/{len(_A4['unseen'])}, classes "
       f"{_A4['menu_cls']}/{_A4['cong_cls']}; ABC3 "
       f"{len(_A3['seen'])}/{len(_A3['unseen'])}, classes "
       f"{_A3['menu_cls']}/{_A3['cong_cls']}")

_nonunit_self = sum(v for k, v in _A4["selfh"].items() if k != 1)
anchor("B4 THE GENERATED LOOP CLASS IS NON-TRIVIAL, WHICH IS WHAT MAKES "
       "THE REPRODUCTION QUESTION WORTH ASKING: on AB4's carrier 44 "
       "self-loops carry holonomy != 1, and a self-loop's holonomy is "
       "gauge-invariant outright [d74-carrier]",
       _nonunit_self == ANCH["d74_selfloops_AB4"],
       f"non-unit self-loops {_nonunit_self}; spectrum "
       f"{fmt(Counter({k: v for k, v in _A4['selfh'].items() if k != 1}))}")

# --- clause (i): gauge invariance ---------------------------------------
_pot_vals = {}
_nodes = sorted({u for u, v, w in _A4["ex"]} | {v for u, v, w in _A4["ex"]},
                key=sk)
for _i, _nd in enumerate(_nodes):
    _pot_vals[_nd] = Fr(_i + 1, _i + 3)          # printed, non-constant
_gauged = Counter()
for u, v, w in _A4["ex"]:
    if u == v:
        _gauged[w * _pot_vals[v] / _pot_vals[u]] += 1
_gi = (_gauged == _A4["selfh"])
_pot_nonconst = len({str(x) for x in _pot_vals.values()}) > 1
check("B5 CLAUSE (i) OF THEOREM D3 REPRODUCES ON THE GENERATED CARRIER: "
      "the loop class is gauge-invariant.  Applying the printed "
      "non-constant vertex potential phi(node_i) = (i+1)/(i+3) and "
      "regauging every edge by q' = q . phi(target)/phi(source) leaves "
      "the entire self-loop holonomy spectrum unchanged, value for value "
      "and count for count",
      _gi and _pot_nonconst,
      f"{len(_pot_vals)} distinct nodes, potential takes "
      f"{len({str(x) for x in _pot_vals.values()})} distinct values; "
      f"regauged spectrum "
      f"{fmt(Counter({k: v for k, v in _gauged.items() if k != 1}))}",
      corollary_of="a self-loop's source and target are the same node, so "
      "the potential cancels identically; the gate is run because the "
      "CONCLUSION is load-bearing, not because the count could fail")

# --- clause (ii): is the loop class U(1)-valued? -------------------------
_allvals = set()
for _nm in ARMS:
    _allvals |= {k for k in ARMS[_nm]["selfh"] if k != 1}
    _allvals |= {k for k in ARMS[_nm]["offh"][4] if k != 1}
    _allvals |= {r for _h, _a, _b, r in ARMS[_nm]["closed"] if r != 1}
_G = group_of(sorted(_allvals))
anchor("B6 THE MEASURED VALUE SET AND GROUP ARE D74's [d74-group]: every "
       "non-unit holonomy measured on either arm — raw squares, carrier "
       "self-loops and independent carrier cycles alike — lies in "
       "{1/2, 2/3, 3/2, 2}, and the multiplicative group they generate is "
       "<2,3>, free abelian of rank 2, index 1 in Z^2",
       _allvals == ANCH["d74_values"]
       and _G["primes"] == ANCH["d74_primes"]
       and _G["rank"] == ANCH["d74_rank"]
       and _G["index"] == ANCH["d74_index"],
       f"values {sorted(str(x) for x in _allvals)}; group {_G['name']}; "
       f"primes {_G['primes']}, rank {_G['rank']}, index {_G['index']}")

_allpos = all(x > 0 for x in _allvals)
_unimodular = {x / abs(x) for x in _allvals}
_roots_of_unity = [x for x in _allvals if x ** 1 == 1 or x == -1]
_torsion_free = _G["rank"] == len(_G["primes"]) and _G["index"] == 1
check("B7 THEOREM 7.1's CONCLUSION — CLAUSE (ii) — DOES NOT REPRODUCE, AND "
      "THE OBSTRUCTION IS EXACT AND STRUCTURAL, NOT A FAILURE TO FIND.  "
      "Thm 7.1 concludes the loop class is valued in SO(2) = U(1).  The "
      "generated loop class is valued in <2,3>, a subgroup of the "
      "MULTIPLICATIVE POSITIVE RATIONALS.  THE REASON THE INTERSECTION IS "
      "TRIVIAL IS POSITIVITY, NOT TORSION-FREENESS: every element of "
      "<2,3> is a positive REAL, and R+ intersect U(1) = {1}, so <2,3> "
      "intersect U(1) = {1}.  Torsion-freeness would not do it — "
      "<e^{2 pi i sqrt 2}> is torsion-free and sits INSIDE U(1) — and the "
      "earlier round's appeal to it is withdrawn.  Freeness of rank 2 (B6) "
      "is retained for what it does establish, which is the size of the "
      "character group at B9.  Every measured holonomy is a positive "
      "rational and every one has unimodular part exactly 1: there is no "
      "U(1) content to find, at any depth, for a reason that is a property "
      "of the value SET and not of the window",
      _allpos and _unimodular == {Fr(1)} and _torsion_free
      and _roots_of_unity == [],
      f"all values positive (the load-bearing fact) {_allpos}; unimodular "
      f"parts {sorted(str(x) for x in _unimodular)}; free of rank = "
      f"#primes with index 1 (the B9 fact) {_torsion_free}; roots of unity "
      f"other than 1 among the measured values: {len(_roots_of_unity)}")

print("""
  AND WHAT CLAUSE (ii) WAS TESTED ON, STATED AGAINST THIS UNIT'S INTEREST.
  Thm D3's B(l) is a product of ENTRIES OF THEOREM D1's DILATING UNITARY —
  the construction this receipt sets aside at its first line [d75-D1guard].
  The object measured here is a ratio of committed MENU WEIGHTS, which are
  positive rationals by construction and could never have landed in U(1).
  Clause (ii)'s non-reproduction is therefore PARTLY AN ARTIFACT OF
  REFUSING D1's HYPOTHESIS, and the substantive content of this arm is the
  two things that survive that concession: the POSITIVITY OBSTRUCTION on
  the generated value set, and the UNSELECTED 2-TORUS of characters at B9.
""")

# --- clause (iii): the interference law ---------------------------------
_cosvals = {Fr(1)}          # cos(arg r) for r a positive real is exactly 1
_A_amp, _B_amp = Fr(1), Fr(1)
_P_loopphase = _A_amp ** 2 + _B_amp ** 2 + 2 * _A_amp * _B_amp * Fr(1)
_P_nointerf = (_A_amp + _B_amp) ** 2
check("B8 CLAUSE (iii) OF THEOREM D3 DEGENERATES ON THE GENERATED "
      "CARRIER, EXACTLY.  D3's law is P = |A|^2 + |B|^2 + 2|A||B| "
      "cos(arg B(loop)).  On this carrier arg B(loop) = 0 for EVERY "
      "measured loop, because every holonomy is a positive rational "
      "(B7), so cos(arg B(loop)) = 1 identically and the law collapses to "
      "P = (|A| + |B|)^2 — the classical no-interference sum, with the "
      "cross term at its MAXIMUM and no cancellation available at any "
      "loop.  The interference table Thm D3 recovers (1.000, 0.750, "
      "0.500, 0.000) requires the cosine to range over [-1, 1]; here its "
      "exact range is the single point {1}",
      _cosvals == {Fr(1)} and _P_loopphase == _P_nointerf,
      f"exact range of cos(arg B(loop)) over every measured loop = "
      f"{sorted(str(x) for x in _cosvals)}; at |A| = |B| = 1 the "
      f"loop-phase law gives P = {_P_loopphase} and the no-interference "
      f"sum gives {_P_nointerf}",
      corollary_of="the cosine set is ASSIGNED here, not measured: it is "
      "read off B7's positivity (cos(arg x) = 1 for every positive real "
      "x), and the identity 1 + 1 + 2 = (1 + 1)^2 cannot fail.  The "
      "measurement that carries this clause is B7's; this gate records "
      "the consequence")

check("B9 THE GAUGE STRATUM CAN CARRY A U(1) LOOP CLASS — AND EXACTLY A "
      "2-TORUS OF THEM, NONE SELECTED.  Since the measured holonomy group "
      "is free abelian of rank 2 (B6), Hom(<2,3>, U(1)) = U(1)^2: a "
      "character is fixed by its values on the two free generators 2 and "
      "3 and those may be chosen independently and arbitrarily.  So D3's "
      "U(1) loop class is ATTACHABLE to the generated carrier in a "
      "2-real-parameter family, and the generated data selects no point "
      "of it — the trivial character is the only one anything committed "
      "picks out (B7).  This is the exact price of the reproduction: two "
      "real numbers, unsourced",
      _G["rank"] == 2 and _G["index"] == 1,
      f"free generators {_G['basis']} on primes {_G['primes']}; "
      f"character group U(1)^{_G['rank']}; free real parameters "
      f"{_G['rank']}")

print(f"""
  ARM B VERDICT — PARTIAL REPRODUCTION, WITH THE OBSTRUCTION NAMED EXACTLY.
    clause (i)   gauge-invariance of the loop class : REPRODUCED (B5),
                 and the loop class is non-trivial on the carrier (B4).
    clause (ii)  Thm 7.1's conclusion, that the loop class is U(1)-valued:
                 NOT REPRODUCED (B7).  Obstruction: every generated
                 holonomy is a POSITIVE REAL and R+ intersect U(1) = {{1}}.
                 Scope, against interest: D3's B(l) is built from entries
                 of D1's dilating unitary, which this receipt sets aside;
                 the measured object is a ratio of menu weights and could
                 never have been unimodular.
    clause (iii) interference IS the loop-phase law : DEGENERATE (B8),
                 as a corollary of B7 and not as a second measurement.
                 cos(arg B(loop)) has exact range {{1}}; the law collapses
                 to the classical sum.
  D74's D2 SETTLED THE SCALAR ODD SECTOR A PRIORI ALREADY, and this arm
  does not sharpen it: [d74-D2] states in one line that the only positive
  rational of modulus 1 is 1, and D74's own note records that this
  "settles the scalar odd sector a priori, in one line, before any fixture
  is run" (v10/note-d74-transport-holonomy-result.md:248, :107-109).  What
  this arm adds is CONFIRMATION ON A DIFFERENT OBJECT — the loop class of
  the carrier (self-loops and independent cycles), not the raw square
  holonomies — and the priced residue at B9.
""")
report("ARM B time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 8.  ARM C — THE GAUGE CANDIDATE
# ===========================================================================

sec("ARM C — THE v7 AMPLITUDE FORM READ AS A [B3] SCHUR-HADAMARD GAUGE")

print(f"""
  THE FORM ({QUOTES['p30-form'][0]}):
    "{QUOTES['p30-form'][1]}"

  THE GAUGE GROUP ({QUOTES['B3-gauge'][0]}):
    "{QUOTES['B3-gauge'][1]}"

  WHAT IS AND IS NOT A TEST, STATED BEFORE THE GATES.  Attaching entrywise
  phases to a lift Theta leaves Gamma = conj(Theta) (Schur-Hadamard)
  Theta invariant BY CONSTRUCTION — that is [B3] eq. (28) read as a
  definition, not a measurement, and a gate on it CANNOT FAIL.  It is run
  below and it is labelled as carrying no independent information.  The
  content of this arm is the OTHER half of Barandes' own sentence: a
  unitary does NOT generically remain unitary under an arbitrary
  Schur-Hadamard gauge transformation.  So the real question is whether
  the v7 form's phase lands in the unitarity-preserving subgroup, and
  whether anything generated selects it at all.
""")

_t = time.time()
_theta = [[cyc_pow(cyc_x(8), (i * j * j + 3 * i) % 8) for j in range(8)]
          for i in range(8)]
_Ug = [[U_DFT8[i][j] * _theta[i][j] for j in range(8)] for i in range(8)]
_gam_same = modsq_check_cyc(_Ug, ARMC2)
check("C1 THE SCHUR-HADAMARD ACTION ON Gamma IS AN IDENTITY, AND IS "
      "GATED AS ONE.  Attaching the printed NON-SEPARABLE entrywise phase "
      "matrix theta_ij = zeta_8^{i.j^2 + 3i} to the 8x8 passer's "
      "certificate leaves |U_ij|^2 = 1/8 at all 64 entries, exactly.  "
      "This is [B3] eq. (30) restated, not tested",
      not _gam_same,
      f"|U'_ij|^2 mismatches against Gamma: {len(_gam_same)}",
      corollary_of="|z . w| = |z||w| and |zeta| = 1; the gate cannot fail "
      "as posed and is excluded from the evidence count")

_sep_a = [cyc_pow(cyc_x(8), (2 * i) % 8) for i in range(8)]
_sep_b = [cyc_pow(cyc_x(8), (3 * j) % 8) for j in range(8)]
_Usep = [[U_DFT8[i][j] * _sep_a[i] * _sep_b[j] for j in range(8)]
         for i in range(8)]
_sep_uni = unitary_check_cyc(_Usep)
_Uflip = [[U_DFT8[i][j] * (Cyc(8, [Fr(-1)]) if (i, j) == (0, 0)
                           else cyc_one(8)) for j in range(8)]
          for i in range(8)]
_flip_uni = unitary_check_cyc(_Uflip)
_flip_gam = modsq_check_cyc(_Uflip, ARMC2)
check("C2 THE UNITARITY-PRESERVING SUBGROUP IS PROPER — BARANDES' CLAUSE, "
      "GATED, ON A BY-SPECIFICATION FLAT MATRIX AND THE TEXTBOOK DFT_8.  "
      "Nothing generated enters this gate and it is not claimed to.  The "
      "SEPARABLE gauge "
      "theta_ij = alpha_i + beta_j (printed: alpha_i = 2i, beta_j = 3j in "
      "units of 2pi/8) preserves unitarity exactly: U^dagger U - I has "
      "ZERO non-zero entries.  A single NON-separable element — flipping "
      "the sign of the (0,0) entry alone, which is a legitimate "
      "Schur-Hadamard transformation with theta_00 = pi — leaves Gamma "
      "EXACTLY invariant and DESTROYS unitarity.  So Gamma-invariance and "
      "unitarity-preservation are genuinely different conditions on this "
      "object, and 'the phase is gauge' does not mean 'any phase will do'",
      not _sep_uni and len(_flip_uni) > 0 and not _flip_gam,
      f"separable gauge: unitarity residuals {len(_sep_uni)}; "
      f"single-entry flip: Gamma mismatches {len(_flip_gam)}, unitarity "
      f"residuals {len(_flip_uni)} (first at index "
      f"{_flip_uni[0][:2] if _flip_uni else None})")

print("""
  DOES ANY COMMITTED GENERATED QUANTITY SELECT A NON-TRIVIAL PHASE?
  The v7 form puts the phase on the reversal-ODD channel O.  The question
  is therefore whether the committed grammar supplies an odd datum at all.
  This receipt measures the sharpest available instance and re-anchors the
  rest.
""")

_endpoints = []
for hh, a, b, r, *_ in _A4["defs"]:
    _endpoints.append(tuple(hh) + (a, b))
    _endpoints.append(tuple(hh) + (b, a))
_endpoints = sorted(set(_endpoints), key=sk)
_lin_total = 0
_adm_rev = 0
for _seq in _endpoints:
    for _perm in b1_linext(list(_seq)):
        _rev = tuple(_seq[i] for i in reversed(_perm))
        _lin_total += 1
        _h = []
        _ok = True
        for _e in _rev:
            _o, _q = b1_adm(_h, _e, AB)
            if not _o:
                _ok = False
                break
            _h.append(_e)
        if _ok:
            _adm_rev += 1
anchor("C3 THE ODD CHANNEL IS EMPTY WHERE THE HOLONOMY LIVES, MEASURED "
       "HERE AND NOT ASSUMED [d74-D5.2]: over every linear extension of "
       "the OPPOSITE poset of every one of AB4's defective-square "
       "endpoints, NOT ONE reversed record is admissible.  D74's "
       "committed count is 304 linear extensions over the 176 endpoints, "
       "0 admissible; this receipt reproduces both numbers",
       _lin_total == 304 and _adm_rev == 0 and len(_endpoints) == 176,
       f"{len(_endpoints)} endpoints, {_lin_total} linear extensions of "
       f"the opposite poset, {_adm_rev} admissible")

_carriers = [
    ("the transport holonomy r", "measured at B6/B7: positive rational, "
     "group <2,3>",
     "R+-valued, so it has no unimodular content at all; and traversal "
     "reversal acts on it by r -> 1/r, which is an EVEN-channel action "
     "on log r, not an odd-channel phase",
     False),
    ("the reversal-EVEN invariant J", "D74 gate D9.1 "
     "[v10/note-d74-transport-holonomy-result.md:120-124]",
     "explicitly reversal-EVEN by construction, so it cannot be Phi(O)",
     False),
    ("the odd-ring port-flip parity class", "D66, as graded by the "
     "catalog [cat-4.7]",
     "killed as a candidate: free relabelling trivialises it, and the "
     "catalog forbids citing it for Phi(O)",
     False),
    ("the reversed record itself", "LD [ld-662] and C3 above",
     "refused at admission on 662/662 holonomy-carrying loops, on the "
     "Born = K1 row, and on all 40 half-open squares",
     False),
]
print("  THE CANDIDATE-CARRIER CENSUS FOR Phi(O)")
print("  " + "-" * 74)
for _nm, _src, _why, _sel in _carriers:
    print(f"    {_nm}")
    print(f"      source : {_src}")
    print(f"      status : {_why}")
    print(f"      selects a non-trivial phase? {'YES' if _sel else 'NO'}")
print("  " + "-" * 74)
check("C4 NO COMMITTED GENERATED QUANTITY SELECTS A NON-TRIVIAL PHASE "
      "ASSIGNMENT — 0 of 4 candidate carriers, each with its committed "
      "source.  The v7 form's phase argument Phi(O) therefore evaluates "
      "on every committed generated object to the empty datum, so the "
      "Schur-Hadamard element the form names is the IDENTITY",
      not any(_sel for _, _, _, _sel in _carriers),
      f"0 of {len(_carriers)} carriers select a phase; three of the four "
      f"are re-anchored citations and the fourth (the reversed record) is "
      f"measured at C3",
      corollary_of="the selection column of this table is HAND-WRITTEN "
      "False, so the gate re-reads its own input and cannot fail as "
      "posed.  What carries the four rows is elsewhere and is cited row "
      "by row: B6/B7 for r, D74 gate D9.1 for J, the catalog's 4.7(c) "
      "for the parity class, and the MEASURED C3 for the reversed record")

check("C5 THE v7 FORM IS CARRIABLE ON THE GAUGE STRATUM, AND IT IS "
      "CARRIED TRIVIALLY.  With Phi(O) empty (C4) the form "
      "A(R) ~ e^{-K(E)} . e^{i Phi(O)} reduces to a real positive "
      "amplitude times e^{i.0} = 1.  The identity is in the "
      "unitarity-preserving subgroup of C2 and preserves Gamma, so the "
      "form is CONSISTENT with [B3]'s gauge structure on both passers.  "
      "It is consistent and empty: consistency at the identity is not "
      "evidence that the stratum is occupied",
      True,
      "the identity element preserves both Gamma and unitarity trivially",
      corollary_of="the identity gauge transformation is in every "
      "subgroup; this records the verdict and claims nothing")

print("""
  ARM C VERDICT — CARRIABLE, TRIVIAL, AND WITH THE NON-TRIVIAL PART PRICED.
    * The Schur-Hadamard action on Gamma is an identity and is NOT a test
      (C1).
    * The unitarity-preserving subgroup is PROPER: a single printed
      entrywise sign flip on the 8x8 passer preserves Gamma exactly and
      destroys unitarity exactly (C2).  SCOPE, PLAINLY: the object is the
      textbook DFT_8 attached to a BY-SPECIFICATION FLAT matrix, so
      NOTHING GENERATED ENTERS C2.  It gates Barandes' clause; it does not
      gate it on generated data.
    * Nothing committed and generated selects a non-trivial phase
      (C3, C4), so the v7 form is carried by the identity element (C5).
    * What a non-trivial occupation would cost is now stated exactly:
      2 real parameters at the loop-class level (B9), and at the lift
      level a choice inside the unitarity-preserving subgroup rather than
      the full entrywise group (C2).  Neither is supplied by anything
      generated.
  CORRESPONDENCE IS NOT IDENTITY.  Nothing here says the generated grammar
  HAS an amplitude, a phase, or an interference law; the arm tests whether
  the gauge stratum COULD carry the v7 form consistently, and the answer
  is yes-and-vacuously.
""")
report("ARM C time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 9.  SCOPE, CAPS, AND THE SUMMARY
# ===========================================================================

sec("SCOPE, CAPS, AND THE SUMMARY")

print(f"""
  SCOPE, NON-NEGOTIABLE.
  * MATRIX-LEVEL SCREENING ONLY.  A matrix that passes the screen is NOT
    thereby a quantum system, a Hilbert space, or a dynamics.  The map
    from a screened Gamma to a physical system is MISSING and this unit
    does not supply it.  Correspondence is not identity.
  * The committed matrices only, at their own scopes: the K1 arbitration
    family at paper 31 sec.4.3's PAIR-PLUS-PATH FIXTURE (component sizes
    {{1,2}} — a fixture line, not a bound on the grammar) TOGETHER WITH the
    committed three-actor pool, whose conflicts reach multiplicity 3
    (M1); the Zhat sibling on the closed-scope (d42b3) family to depth
    6; the D74 anchor arms at (A,B) depth <= 4 and (A,B,C) depth <= 3.
  * The K1 outcome-space bound (|MIS| <= 2) is MEASURED on three pools
    here and on a fourth in the U3 round [u3-round-B1].  It is NOT proved
    for the grammar, and no claim is made that it holds at a wider actor
    pool or a non-binary value alphabet.
  * The screen is CLOSED and UNDILATED.  [B3-dilation]: a quantum system
    is either a unistochastic process itself OR a subsystem of one.  This
    receipt decides the FIRST disjunct only; every S-FAIL verdict leaves
    the subsystem disjunct untouched.
  * ARM-C2's 8x8 matrix is taken BY SPECIFICATION from U1's committed
    receipt [u1-armc2] and is NOT re-derived here; the verdict on it is
    made independent of that quote by the column-constant lemma (L1).
  * U1b's biting renewal transfers are NOT awaited (file-disjoint parallel
    unit).  Screening them is a DECLARED FOLLOW-UP, and by L1 the only way
    such a transfer can pass the DS precondition is by being uniform.
  * Named but NOT screened, and owed forward: the 36-state sigma chain
    (v10/note-d61-...:40) and the transport-scope descent quotient of D74
    as a transition matrix.  Both are in the D75 audit's candidate list
    [d75-5.3] and neither is in this pin's list.
  * No CP statement of any kind.  No Bell or locality statement of any
    kind.  No covariance claim: L-1's bound stands untouched, and nothing
    here is a law at renewal grain.
  * Theorem D1 is SET ASIDE throughout [d75-D1guard]: every positive
    verdict exhibits a unitary of the SAME size, with no ancilla and no
    ancilla sum.
  * The n = 3 sufficiency of the triangle criterion is CITED [lit-uni3]
    and is never load-bearing: this receipt returns "unistochastic" only
    with an exhibited, verified certificate.

  CAPS, PRINTED.""")
for _k, _v in CAPS.items():
    print(f"    {_k}: {_v}")
print(f"""    Surd sign oracle: maximum refinement actually used
      {SIGN_BITS_USED[0]} binary digits against the 4096 cap.
    EXCLUDED-BY-CAP verdicts on this census: {_tally.get('EXCLUDED-BY-CAP', 0)}.
""")

print("  THE UNIT'S ANSWERS, IN ONE PLACE.")
print("    ARM A  the screen census, per matrix:")
for s in SCREEN:
    print(f"             {s['name']:<24} {s['verdict']}")
print("           two structural verdicts: both passers are the FLAT J/n "
      "and are")
print("           orthostochastic, so the ortho/uni gap is empty on this "
      "census")
print("           and the passes carry no quantum content (A6); and the K1 "
      "OUTCOME")
print("           SPACE has size at most 2 — MEASURED at four committed "
      "pools,")
print("           UNPROVED beyond them — so by L1 i is undecidable there, "
      "and")
print("           deciding it needs a >= 3-OUTCOME K1 law, i.e. non-binary")
print("           proposal values or non-complete-multipartite conflict "
      "graphs")
print("           (A7, M1-M5).  Multiplicity 3 IS committed and still "
      "gives a")
print("           2-outcome law.")
print("    ARM B  clause (i) REPRODUCED; clause (ii) — Thm 7.1's "
      "conclusion —")
print("           NOT REPRODUCED, obstruction = POSITIVITY: every "
      "generated")
print("           holonomy is a positive real and R+ cap U(1) = {1} (NOT")
print("           torsion-freeness, which does not imply it); clause "
      "(iii)")
print("           DEGENERATE as a corollary, cos range {1}.  D74's D2 had")
print("           already settled this a priori; this arm confirms it on "
      "the")
print("           loop class.  A U(1) loop class is attachable in a "
      "2-torus of")
print("           ways, none selected.")
print("    ARM C  the gauge action on Gamma is an identity (not a test); "
      "the")
print("           unitarity-preserving subgroup is PROPER, gated on the")
print("           by-specification flat matrix and the textbook DFT_8 — "
      "nothing")
print("           generated enters it; no committed generated quantity "
      "selects")
print("           a phase, so the v7 form is carried by the identity — "
      "carriable")
print("           and vacuous.")

_ind = PASS - len(COROLLARY)
print()
print(f"[SUMMARY] {PASS} PASS / {FAIL} FAIL / {ANCHOR_FAIL} ANCHOR-FAIL, "
      f"of which {len(COROLLARY)} carry NO INDEPENDENT INFORMATION and are "
      f"labelled as such ({_ind} independent-evidence passes)")
print(f"[RUNTIME] {time.time() - T0:.0f}s wall clock, single-threaded, "
      f"exact arithmetic throughout, no tolerance anywhere")
print(f"[CAPS] closed scope depth {CAP_CLOSED}; anchor arms depth "
      f"{CAP_AB}/{CAP_ABC}; sizes decided constructively 1,2,3,6,8; "
      f"EXCLUDED-BY-CAP verdicts: {_tally.get('EXCLUDED-BY-CAP', 0)}; "
      f"Surd sign refinement used {SIGN_BITS_USED[0]} of 4096 bits")
if ANCHOR_FAIL:
    print("[EXIT] 1 — an ANCHOR failed; the committed record did not "
          "reproduce")
    sys.exit(1)
print("[EXIT] 0 — substantive negatives are results, not failures")
sys.exit(0)
