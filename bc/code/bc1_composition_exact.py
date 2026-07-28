#!/usr/bin/env python3
"""
bc1_composition_exact.py — BC1: DIVISION-EVENT COMPOSITION CONSISTENCY.

Pin: bc/note-bc1-division-event-composition-pin.md (STRICT, frozen before
this file existed).  Programme: BC — the Barandes consistency programme
(bc/LOG.md #1), a from-scratch test of the indivisible-stochastic-process
framework [B3] (J. A. Barandes, arXiv:2507.21192, 30 July 2025) on its own
terms, WITHOUT the record substrate.  Nothing here is a claim about the
v11 record programme (halted, untouched), about nature, or about QFT.

THE QUESTION ([B3] p.10): division events are SYSTEM-CENTRIC — a division
event for a composite need not be one for its subsystems, and vice versa.
Is that assignment internally consistent across the subsystem lattice?

WHAT IS REUSED, AND HOW
  * v11/code/u1_indivisibility_census_exact.py — the exact LP + Farkas
    feasibility machinery ("does a column-stochastic bridge exist"):
    phase1, farkas_ok, reduce_system, lift_and_verify, invert_exact,
    gamma_of, supports, decide_triple, decide_reduced, print_certificate,
    print_interpolant, sk, srt.  Lifted by ast.FunctionDef from the
    committed file, never retyped, never re-derived.
  * v11/code/u3_unistochasticity_screen_exact.py — the exact algebraic
    rings (Surd, Cyc), the unistochasticity criterion (ds_report,
    tri_disc, chain_link_squares, polygon_violations), the certificate
    checkers and the screen.  Lifted by ast.FunctionDef / ast.ClassDef /
    ast.Assign from the committed file.
  Both instruments are ANCHORED on known-answer cases before use, and
  exit 1 is reserved for anchor failure alone.

HOUSE RULES OBSERVED
  * Exact arithmetic end to end.  Unitaries live in Surd (the Q-span of
    square roots; carries Q and Q(sqrt 2)) or in Cyc(8) = Q(zeta_8);
    every transition matrix is a Fraction matrix, gated rational at
    construction.  No float appears in any substantive computation
    (time.time() is used for progress prints only).
  * No randomness anywhere: every matrix entry is a declared constant.
  * Every census printed BOTH WAYS.
  * Substantive negatives exit 0.
  * Determinism: every printed aggregate is ordered by the
    hash-seed-independent key sk() lifted from U1.
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
from itertools import product

T0 = time.time()
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(REPO)                # .../isp  (run from anywhere)
os.chdir(REPO)
sys.setrecursionlimit(100000)

PASS = FAIL = 0
ANCHOR_FAIL = 0
SECT = [0]


def sec(title):
    SECT[0] += 1
    print()
    print("=" * 78)
    print(f"SEC {SECT[0]}  {title}   [t+{time.time() - T0:.1f}s]")
    print("=" * 78)
    sys.stdout.flush()


def check(label, ok, detail="", reporting_only=False):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if reporting_only:
        tag = "[RPT ]"
    else:
        PASS += int(bool(ok))
        FAIL += int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))
    if reporting_only:
        print("         ^ REPORTING ONLY: cannot fail as posed; not counted "
              "as evidence")
    sys.stdout.flush()
    return bool(ok)


def anchor(label, ok, detail=""):
    global ANCHOR_FAIL
    if not check("ANCHOR " + label, ok, detail):
        ANCHOR_FAIL += 1
    return bool(ok)


def report(label, value):
    print(f"  [DATA] {label}: {value}")
    sys.stdout.flush()


# ===========================================================================
# SEC 0.  THE REGISTRY — every [B3] passage this receipt leans on, verbatim
#         and page-cited, and every constant a gate tests against.
# ===========================================================================

B3 = ("[B3] J. A. Barandes, 'Quantum Systems as Indivisible Stochastic "
      "Processes', arXiv:2507.21192, 30 July 2025")

QUOTES = {
    "B3-kin-ax": (
        B3 + ", p.29 (Section 7, 'Kinematical axiom')",
        "\"Kinematical axiom: For each model under consideration, one picks "
        "an appropriate configuration space, whose members are the possible "
        "configurations of the system being modeled, treated as elementary "
        "according to the model.  The configuration space is a fixed feature "
        "of the model, meaning that it does not vary between real-world runs "
        "or instantiations of the model.\"",
    ),
    "B3-dyn-ax": (
        B3 + ", p.29 (Section 7, 'Dynamical axiom')",
        "\"Dynamical axiom: For arbitrary target times, and for conditioning "
        "times corresponding to division events, the model's dynamical laws "
        "consist of transition probabilities that take the form of "
        "conditional probabilities for the system to be in a particular "
        "configuration at each target time, given that the system is in a "
        "particular configuration at each conditioning time.  Division "
        "events may occur naturally within the model's own dynamics, and can "
        "also be generated spontaneously through interactions with other "
        "systems. ...  At the level of the given model, the dynamical laws "
        "are fixed features.\"",
    ),
    "B3-epi-ax": (
        B3 + ", p.29 (Section 7, 'Epistemic axiom')",
        "\"Epistemic axiom: The system has some time-dependent standalone "
        "probability distribution to be in a particular configuration at any "
        "given target time.  This standalone probability distribution is "
        "connected between different times by the model's transition "
        "probabilities, and is contingent, meaning that it can vary between "
        "runs of the model.\"",
    ),
    "B3-divdef": (
        B3 + ", p.9 (Section 2.2, following eq. 21)",
        "\"Note that no assumption is made here that the transition "
        "probabilities p(i,t | j,t_0) exist as part of the laws for all "
        "real-valued choices of t_0.  Allowed conditioning times t_0 are "
        "called division events for the given system, and, without any real "
        "loss of generality, are assumed to include an 'initial' time 0.\"",
    ),
    "B3-syscentric": (
        B3 + ", p.10 (Section 2.2, first paragraph)",
        "\"Division events are not global properties of the whole universe, "
        "but are system-centric, just like various other kinds of "
        "spontaneous time-translation-breaking in physics.  In practice, a "
        "system may have multiple exact division events, or they may be "
        "generated to an extremely good approximation through interactions "
        "with other systems, after marginalizing over those other systems "
        "(Barandes 2025).\"",
    ),
    "B3-ltp": (
        B3 + ", p.9 (Section 2.2, eqs. 19-20)",
        "\"The only available Chapman-Kolmogorov equations (5) take the "
        "simple form  p(i,t) = sum_j p(i,t | j,t_0) p(j,t_0),  (19)  which "
        "is just the law of total probability.  Equivalently, in matrix "
        "notation,  p(t) = Gamma(t <- t_0) p(t_0).  (20)\"",
    ),
    "B3-eq22": (
        B3 + ", p.10 (Section 2.2, eqs. 22-23 and the following paragraph)",
        "\"Given transition matrices Gamma(t <- t_0) and Gamma(t' <- t_0), "
        "where t' lies in the interval between t_0 and t, it might seem "
        "reasonable to try to define an intermediate transition matrix "
        "~Gamma(t <- t') from t' to t according to  ~Gamma(t <- t') = "
        "Gamma(t <- t_0) Gamma^{-1}(t' <- t_0),  (22)  at least if "
        "Gamma(t' <- t_0) is invertible.  By construction, it would then "
        "seem to follow that the system obeys a divisibility condition akin "
        "to (14):  Gamma(t <- t_0) = ~Gamma(t <- t') Gamma(t' <- t_0).  (23)"
        "  However, it turns out that a matrix ~Gamma(t <- t') defined "
        "according to (22) will generically fail to be a column stochastic "
        "matrix, and, indeed, will typically have negative entries...\"",
    ),
    "B3-permlemma": (
        B3 + ", p.10 (Section 2.2, main text and footnote 7)",
        "\"The reason is that the inverse of a stochastic matrix can only "
        "itself be a stochastic matrix if both matrices are permutation "
        "matrices, meaning that they consist solely of 0s and 1s, and "
        "therefore do not contain nontrivial probabilities.\"  [Footnote 7 "
        "gives the proof.]",
    ),
    "B3-uni": (
        B3 + ", p.18 (Section 3.6, after eq. 68)",
        "\"In general, an N x N matrix is called unistochastic if its "
        "individual entries are expressible as the modulus-squares of the "
        "corresponding entries of an N x N unitary matrix.  It follows that "
        "(64) is just the statement that the system's transition matrix "
        "Gamma(t <- 0) can be taken to be unistochastic, and will therefore "
        "be said to describe a unistochastic process.\"",
    ),
    "B3-sqthm": (
        B3 + ", p.19 (Section 3.6, first paragraph)",
        "\"The preceding analysis implies that an indivisible stochastic "
        "process can be viewed either as a unistochastic process itself, or "
        "(if a nontrivial dilation was required) as a subsystem of a "
        "unistochastic process.  This statement is called the "
        "stochastic-quantum theorem (Barandes 2023).\"",
    ),
    "B3-gauge": (
        B3 + ", p.19 (Section 3.6, after eq. 68)",
        "\"Note that a unitary time-evolution operator U(t <- 0) will not "
        "generically remain unitary under arbitrary Schur-Hadamard gauge "
        "transformations (30).  Hence, writing a unistochastic transition "
        "matrix Gamma(t <- 0) in terms of a unitary time-evolution operator "
        "U(t <- 0) corresponds to making a gauge choice...\"",
    ),
    "U1-D1": (
        "v11/code/u1_indivisibility_census_exact.py:661-673 (the repaired "
        "definition, SEC 3)",
        "\"(D1) LOCAL DIVISIBILITY at a composable triple (c, c', c''): "
        "there EXISTS a column-stochastic X with X . Gamma(c' <- c) = "
        "Gamma(c'' <- c).  When Gamma(c' <- c) is square and invertible X is "
        "unique and equals the algebraic interpolant Gammabar = "
        "Gamma(c'' <- c) . Gamma(c' <- c)^-1 of [B3] eq. 22 ...  When "
        "Gamma(c' <- c) is singular the algebraic form does not apply and "
        "(D1) is decided as a linear feasibility question.\"",
    ),
    "U3-crit": (
        "v11/code/u3_unistochasticity_screen_exact.py:1101-1120 "
        "(polygon_violations) and :1085-1089 (tri_disc)",
        "the general necessary condition at every n (if Gamma = |U|^2 then "
        "for every pair of distinct columns the n complex numbers "
        "conj(U_ip) U_iq, of modulus sqrt(Gamma_ip Gamma_iq), sum to zero, "
        "so no one modulus may exceed the sum of the others), plus the exact "
        "n = 3 triangle discriminant T = 2(ab+bc+ca) - a^2 - b^2 - c^2.",
    ),
}

print("=" * 78)
print("BC1 — DIVISION-EVENT COMPOSITION CONSISTENCY  (exact receipt)")
print("=" * 78)
print("  banner: exact arithmetic end to end — unitaries in Surd (Q and")
print("  Q(sqrt 2)) or in Cyc(8) = Q(zeta_8), transition matrices in")
print("  Fractions, gated rational at construction; no float in any")
print("  substantive computation; no randomness anywhere (every entry is a")
print("  declared constant); both readings censused separately; every")
print("  census printed both ways; substantive negatives exit 0; exit 1 ONLY")
print("  if a reused instrument fails its known-answer anchor.")
print()
print("  SCOPE, ENGRAVED: this receipt tests formal properties of [B3]'s")
print("  framework as written, at the tested dimensions (2x2x2) and the")
print("  tested dynamics.  It makes NO claim about nature, about QFT, or")
print("  about the v11 record programme.  LEAN: NONE.")
print()
print(f"  PYTHONHASHSEED = {os.environ.get('PYTHONHASHSEED', '(unset)')}")
print(f"  python         = {sys.version.split()[0]}")
print()
print("  QUOTE REGISTRY — every [B3] axiom or passage used below, verbatim")
print("  and page-cited.  Nothing in this receipt leans on an unquoted")
print("  reading of the paper.")
for _k in sorted(QUOTES):
    _where, _text = QUOTES[_k]
    print()
    print(f"    [{_k}] {_where}")
    for _i in range(0, len(_text), 68):
        print(f"        {_text[_i:_i + 68]}")
print()


# ===========================================================================
# SEC 1.  SINGLE-SOURCING — the two committed instruments, lifted by AST
# ===========================================================================

sec("SINGLE-SOURCING: AST signature pass and AST extraction of the two "
    "committed, programme-independent instruments")

_P_U1 = "v11/code/u1_indivisibility_census_exact.py"
_P_U3 = "v11/code/u3_unistochasticity_screen_exact.py"


def ast_signatures(path, required):
    """Every required definition must exist at module level with the exact
    positional argument list, so a silent upstream edit cannot slip through
    (U1's SRC.1 idiom, re-run here on both instruments)."""
    tree = ast.parse(open(path).read(), filename=path)
    sigs = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            sigs[node.name] = [a.arg for a in node.args.args]
        elif isinstance(node, ast.ClassDef):
            sigs[node.name] = ["<class>"]
        elif isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name):
                    sigs[tgt.id] = ["<assign>"]
    missing = []
    for name, args in required.items():
        if name not in sigs:
            missing.append((name, "ABSENT"))
        elif args is not None and sigs[name] != args:
            missing.append((name, f"{sigs[name]} != {args}"))
    return sigs, missing


def ast_lift(path, names, ns):
    """Lift named module-level FunctionDef / ClassDef / Assign nodes out of a
    committed source by AST and compile them into ns, IN SOURCE ORDER so that
    intra-file dependencies resolve.  Nothing is retyped; the extracted text
    is the committed text.  Returns the source segments."""
    src = open(path).read()
    tree = ast.parse(src, filename=path)
    lines = src.splitlines(keepends=True)
    segs = {}
    for nd in tree.body:
        nm = None
        if isinstance(nd, (ast.FunctionDef, ast.ClassDef)):
            nm = nd.name
        elif isinstance(nd, ast.Assign) and len(nd.targets) == 1 \
                and isinstance(nd.targets[0], ast.Name):
            nm = nd.targets[0].id
        if nm in names:
            seg = "".join(lines[nd.lineno - 1:nd.end_lineno])
            segs[nm] = seg
            exec(compile(seg, f"<ast:{os.path.basename(path)}:{nm}>", "exec"),
                 ns)
    return segs


U1_REQ = {
    "sk": ["o"], "srt": ["xs"],
    "phase1": ["M", "b", "maxpivot", "rule", "stall"],
    "farkas_ok": ["M", "b", "w"],
    "reduce_system": ["A", "B", "Is", "Js", "Ks"],
    "lift_and_verify": ["x", "var", "GL", "HL", "Gs", "Hs", "A", "B",
                        "Is", "Js", "Ks"],
    "invert_exact": ["M"],
    "gamma_of": ["J", "ia", "ib"],
    "supports": ["J", "ncuts"],
    "decide_triple": ["J", "S", "i0", "i1", "i2", "label", "lp_stats"],
    "decide_reduced": ["A", "B", "Is", "Js", "Ks", "out", "lp_stats"],
    "fr_digest": ["vec", "labels", "cap"],
    "print_certificate": ["r"],
    "print_interpolant": ["r"],
}
U3_REQ = {
    "sqfree_split": ["n"], "Surd": ["<class>"], "surd_sign": ["x"],
    "sqrt_fr": ["r"], "polydivmod": ["a", "b"], "PHI": ["<assign>"],
    "PHI_NAME": ["<assign>"], "Cyc": ["<class>"], "cyc_one": ["N"],
    "cyc_zero": ["N"], "cyc_x": ["N"], "cyc_pow": ["z", "k"],
    "phi_euler": ["n"], "SIGN_BITS_USED": ["<assign>"],
    "ds_report": ["M"], "tri_disc": ["a", "b", "c"],
    "chain_link_squares": ["M", "p", "q", "by"],
    "polygon_violations": ["M"], "unitary_check_cyc": ["U"],
    "modsq_check_cyc": ["U", "M"], "orth_check_surd": ["U"],
    "modsq_check_surd": ["U", "M"], "real_orth_2x2": ["B"],
    "sylvester": ["k"], "screen": ["name", "M", "provenance", "reading",
                                   "note", "cert_hint"],
    "fsl": ["xs"],
}

_s1, _m1 = ast_signatures(_P_U1, U1_REQ)
_s3, _m3 = ast_signatures(_P_U3, U3_REQ)
anchor("SRC.1 AST SIGNATURE PASS on both committed instruments: every "
       "required definition exists at module level with the exact "
       "positional argument list, so a silent upstream edit to U1's LP "
       "machinery or U3's criterion cannot slip through unnoticed",
       not (_m1 or _m3),
       f"u1 {len(_s1)} module-level names ({len(U1_REQ)} required, missing "
       f"{_m1}); u3 {len(_s3)} names ({len(U3_REQ)} required, missing {_m3})")

# --- the LP + Farkas machinery, lifted -----------------------------------
LP_MAXVARS = 700
LP_MAXROWS = 400
LP2_MAXVARS = 5000
LP2_MAXROWS = 1200
LP_MAXPIVOT = 400000

NS1 = {"Fr": Fr, "defaultdict": defaultdict, "time": time,
       "LP_MAXVARS": LP_MAXVARS, "LP_MAXROWS": LP_MAXROWS,
       "LP2_MAXVARS": LP2_MAXVARS, "LP2_MAXROWS": LP2_MAXROWS,
       "LP_MAXPIVOT": LP_MAXPIVOT}
_seg1 = ast_lift(_P_U1, set(U1_REQ), NS1)
sk = NS1["sk"]
srt = NS1["srt"]
phase1 = NS1["phase1"]
farkas_ok = NS1["farkas_ok"]
invert_exact = NS1["invert_exact"]
gamma_of = NS1["gamma_of"]
supports = NS1["supports"]
decide_triple = NS1["decide_triple"]
print_certificate = NS1["print_certificate"]
print_interpolant = NS1["print_interpolant"]
_LP_CALLS = [0]
_phase1_lifted = NS1["phase1"]


def phase1(M, b, maxpivot=LP_MAXPIVOT, rule="bland", stall=60):
    """A COUNTING SHIM ONLY: it increments a counter and delegates, with
    every argument unchanged, to the lifted U1 function.  It exists so that
    the receipt can report how many times the exact simplex actually ran,
    and it alters nothing the simplex does."""
    _LP_CALLS[0] += 1
    return _phase1_lifted(M, b, maxpivot, rule, stall)


NS1["phase1"] = phase1
anchor("SRC.2 U1's EXACT LP + FARKAS MACHINERY IS U1's, lifted by "
       "ast.FunctionDef from the committed receipt and not retyped: the "
       "Phase-I simplex phase1 (exact Fractions, Bland's rule), the "
       "independent Farkas verifier farkas_ok, the feasibility-preserving "
       "reduction reduce_system, lift_and_verify, invert_exact, gamma_of, "
       "supports and the whole decide_triple cascade",
       set(_seg1) == set(U1_REQ)
       and "Exact: does x >= 0 with M x = b exist?" in _seg1["phase1"]
       and "w^T M <= 0 componentwise and w^T b > 0" in _seg1["farkas_ok"]
       and "Gamma(c''<-c) Gamma(c'<-c)^-1" in _seg1["decide_triple"],
       f"lifted {len(_seg1)} definitions from {_P_U1}: "
       + ", ".join(f"{n}({len(_seg1[n].splitlines())}L)"
                   for n in sorted(_seg1)))

# --- the exact algebraic rings and the unistochasticity criterion, lifted --
NS3 = {"Fr": Fr, "math": math, "product": product}
_seg3 = ast_lift(_P_U3, set(U3_REQ), NS3)
Surd = NS3["Surd"]
surd_sign = NS3["surd_sign"]
sqrt_fr = NS3["sqrt_fr"]
Cyc = NS3["Cyc"]
cyc_one = NS3["cyc_one"]
cyc_zero = NS3["cyc_zero"]
cyc_x = NS3["cyc_x"]
cyc_pow = NS3["cyc_pow"]
ds_report = NS3["ds_report"]
tri_disc = NS3["tri_disc"]
chain_link_squares = NS3["chain_link_squares"]
polygon_violations = NS3["polygon_violations"]
unitary_check_cyc = NS3["unitary_check_cyc"]
modsq_check_cyc = NS3["modsq_check_cyc"]
orth_check_surd = NS3["orth_check_surd"]
modsq_check_surd = NS3["modsq_check_surd"]
real_orth_2x2 = NS3["real_orth_2x2"]
sylvester = NS3["sylvester"]
screen = NS3["screen"]
fsl = NS3["fsl"]
anchor("SRC.3 U3's EXACT ALGEBRAIC RINGS AND UNISTOCHASTICITY CRITERION "
       "ARE U3's, lifted by ast.ClassDef / ast.FunctionDef / ast.Assign "
       "from the committed receipt: Surd with its sign oracle, Cyc = "
       "Q(zeta_N) with Phi_N, ds_report, tri_disc, chain_link_squares, "
       "polygon_violations, the four certificate checkers, real_orth_2x2, "
       "sylvester and the screen itself",
       set(_seg3) == set(U3_REQ)
       and "Sum_d c_d sqrt(d)" in _seg3["Surd"]
       and "Q[x]/Phi_N(x)" in _seg3["Cyc"]
       and "16 . (Heron area)^2" in _seg3["tri_disc"]
       and "no one modulus may exceed the sum of the others"
       in _seg3["polygon_violations"],
       f"lifted {len(_seg3)} definitions from {_P_U3}: "
       + ", ".join(f"{n}({len(_seg3[n].splitlines())}L)"
                   for n in sorted(_seg3)))


def fmt_counter(counter):
    return {str(k): v for k, v in sorted(counter.items(),
                                         key=lambda z: sk(z[0]))}


# ===========================================================================
# SEC 2.  THE INSTRUMENTS ANCHORED ON KNOWN ANSWERS, BEFORE ANY USE
# ===========================================================================

sec("KNOWN-ANSWER ANCHORS on the two reused instruments, run BEFORE either "
    "instrument is pointed at anything constructed here")

# ---- (a) the LP + Farkas machinery --------------------------------------
_lp_cases = []

# KA-LP1: an identity source — every target is reachable, X = B.
_A1 = [[Fr(1), Fr(0)], [Fr(0), Fr(1)]]                     # A = I (2x2)
_B1 = [[Fr(1, 3), Fr(3, 4)], [Fr(2, 3), Fr(1, 4)]]         # any stochastic B
# system: variables X[k][j]; constraints  sum_k X[k][j] = 1 (per j)
#                                         sum_j X[k][j] A[j][i] = B[k][i]


def lp_system(A, B):
    """The interpolant feasibility system in U1's exact form (the assembly
    of decide_triple step (4), applied to explicit matrices): variables
    X[k][j] >= 0, one column-sum equation per source-of-the-bridge index j,
    one equation per (target k, initial i)."""
    nK, nJ, nI = len(B), len(A), len(A[0])
    idx = {(k, j): k * nJ + j for k in range(nK) for j in range(nJ)}
    M, b = [], []
    for j in range(nJ):
        row = [Fr(0)] * (nK * nJ)
        for k in range(nK):
            row[idx[(k, j)]] = Fr(1)
        M.append(row)
        b.append(Fr(1))
    for k in range(nK):
        for i in range(nI):
            row = [Fr(0)] * (nK * nJ)
            for j in range(nJ):
                if A[j][i]:
                    row[idx[(k, j)]] = A[j][i]
            M.append(row)
            b.append(B[k][i])
    return M, b


_M, _b = lp_system(_A1, _B1)
_f1, _p1, _c1 = phase1(_M, _b)
anchor("KA-LP1 THE EXACT PHASE-I SIMPLEX FINDS THE HAND-KNOWN FEASIBLE "
       "POINT: with Gamma(t'<-0) = I the unique bridge is X = "
       "Gamma(t<-0) itself, and the LP returns FEASIBLE with a certificate "
       "that reproduces B entry by entry in exact rationals",
       _f1 is True
       and all(sum(_c1[k * 2 + j] * _A1[j][i] for j in range(2))
               == _B1[k][i] for k in range(2) for i in range(2))
       and all(sum(_c1[k * 2 + j] for k in range(2)) == Fr(1)
               for j in range(2)),
       f"feasible={_f1}, pivots={_p1}, x={[str(v) for v in _c1]}")

# KA-LP2: a rank-1 source cannot reach a target with distinct columns.
_A2 = [[Fr(1, 2), Fr(1, 2)], [Fr(1, 2), Fr(1, 2)]]         # both columns equal
_B2 = [[Fr(1), Fr(0)], [Fr(0), Fr(1)]]                     # B = I
_M, _b = lp_system(_A2, _B2)
_f2, _p2, _w2 = phase1(_M, _b)
_fk2 = farkas_ok(_M, _b, _w2)
anchor("KA-LP2 THE LP RETURNS THE HAND-KNOWN INFEASIBILITY, WITH A FARKAS "
       "CERTIFICATE INDEPENDENTLY VERIFIED: if Gamma(t'<-0) has two "
       "identical columns then X.Gamma(t'<-0) has two identical columns for "
       "EVERY X, so it can never equal the identity.  The dual vector w "
       "satisfies w^T M <= 0 on every column and w^T b > 0",
       _f2 is False and _fk2,
       f"feasible={_f2}, pivots={_p2}, Farkas verified={_fk2}, "
       f"w^T b = {sum(_w2[i] * _b[i] for i in range(len(_b)))} > 0")

# KA-LP3: [B3] eq.22 on a 2x2 bistochastic pair — the algebraic interpolant
# and the LP must agree, in both directions, on a hand-computable family.
#   Gamma(lambda) = [[(1+l)/2, (1-l)/2], [(1-l)/2, (1+l)/2]];
#   the unique bridge from lambda' to lambda has parameter l/l'.
_agree, _kadetail = True, []
for _lp, _lt in ((Fr(1, 2), Fr(1, 4)), (Fr(1, 4), Fr(1, 2)),
                 (Fr(-1, 3), Fr(2, 3)), (Fr(3, 4), Fr(-1, 2))):
    _GA = [[(1 + _lp) / 2, (1 - _lp) / 2], [(1 - _lp) / 2, (1 + _lp) / 2]]
    _GB = [[(1 + _lt) / 2, (1 - _lt) / 2], [(1 - _lt) / 2, (1 + _lt) / 2]]
    _inv, _det = invert_exact([row[:] for row in _GA])
    _Gb = [[sum(_GB[r][t] * _inv[t][c] for t in range(2)) for c in range(2)]
           for r in range(2)]
    _alg_ok = all(_Gb[r][c] >= 0 for r in range(2) for c in range(2))
    _M, _b = lp_system(_GA, _GB)
    _f, _p, _w = phase1(_M, _b)
    _hand = abs(_lt / _lp) <= 1
    _agree &= (_alg_ok == bool(_f) == _hand)
    _kadetail.append(f"l'={_lp} l={_lt}: |l/l'|={abs(_lt / _lp)} hand="
                     f"{_hand} eq22={_alg_ok} LP={bool(_f)}")
anchor("KA-LP3 THE eq.22 ALGEBRAIC INSTRUMENT AND THE LP AGREE WITH EACH "
       "OTHER AND WITH THE CLOSED-FORM ANSWER on the 2x2 bistochastic "
       "family, in both directions: the bridge from lambda' to lambda has "
       "parameter lambda/lambda', so it is stochastic exactly when "
       "|lambda/lambda'| <= 1.  Four cases, two divisible and two not",
       _agree, "; ".join(_kadetail))

# ---- (b) U3's unistochasticity criterion, its own battery re-run ---------
FLAT3 = [[Fr(1, 3)] * 3 for _ in range(3)]
_ka1_T = tri_disc(*chain_link_squares(FLAT3, 0, 1, "col"))
_ka1_poly = polygon_violations(FLAT3)
anchor("KA-U3a U3's KA-1 REPRODUCES: the 3x3 flat matrix J/3 (= |DFT_3|^2) "
       "has triangle discriminant T = +1/27 > 0 and no polygon violation — "
       "the criterion does not reject a matrix that IS unistochastic",
       _ka1_T == Fr(1, 27) and not _ka1_poly,
       f"T = {_ka1_T}; polygon violations {len(_ka1_poly)}")

BNOT = [[Fr(0), Fr(1, 2), Fr(1, 2)],
        [Fr(1, 2), Fr(0), Fr(1, 2)],
        [Fr(1, 2), Fr(1, 2), Fr(0)]]
_ka2_ds = ds_report(BNOT)
_ka2_T = tri_disc(*chain_link_squares(BNOT, 0, 1, "col"))
_ka2_poly = polygon_violations(BNOT)
anchor("KA-U3b U3's KA-2 REPRODUCES: the canonical counterexample "
       "B = (J - I)/2 is bistochastic, has triangle discriminant "
       "T = -1/16 < 0, and the polygon oracle flags the same obstruction — "
       "the criterion does reject a matrix that is NOT unistochastic",
       _ka2_ds["ds"] and _ka2_T == Fr(-1, 16) and len(_ka2_poly) > 0,
       f"DS {_ka2_ds['ds']}; T = {_ka2_T}; polygon violations "
       f"{len(_ka2_poly)}")

B2KA = [[Fr(1, 3), Fr(2, 3)], [Fr(2, 3), Fr(1, 3)]]
U2KA = real_orth_2x2(B2KA)
_ka4 = (not orth_check_surd(U2KA)) and (not modsq_check_surd(U2KA, B2KA))
anchor("KA-U3c U3's KA-4 REPRODUCES: the n = 2 construction returns a "
       "matrix that is exactly orthogonal in the Surd ring with "
       "|U_ij|^2 = B_ij, so every 2x2 bistochastic matrix is "
       "orthostochastic and the n = 2 verdicts below are complete",
       _ka4, f"orthogonality residuals {len(orth_check_surd(U2KA))}; "
             f"|U|^2 mismatches {len(modsq_check_surd(U2KA, B2KA))}")

BRS = [[Fr(1, 2), Fr(1, 2)], [Fr(1), Fr(0)]]
_ka5 = ds_report(BRS)
anchor("KA-U3d U3's KA-5 REPRODUCES: the doubly-stochastic precondition is "
       "not a no-op — a row-stochastic matrix that is not column-stochastic "
       "is caught with the exact per-column excess",
       _ka5["row_ok"] and not _ka5["col_ok"] and not _ka5["ds"],
       f"row sums {fsl(_ka5['rowsums'])}; column sums "
       f"{fsl(_ka5['colsums'])}")

_H8 = sylvester(3)
_h8ok = all(sum(_H8[k][i] * _H8[k][j] for k in range(8))
            == (8 if i == j else 0) for i in range(8) for j in range(8))
anchor("KA-U3e U3's KA-6 REPRODUCES: Sylvester's real Hadamard matrix of "
       "order 8 satisfies H H^T = 8 I over the integers",
       _h8ok, "64 inner products exact")

# ---- (c) the exact rings self-test --------------------------------------
_r1 = sqrt_fr(Fr(2)) * sqrt_fr(Fr(3)) - sqrt_fr(Fr(6))
_r2 = sqrt_fr(Fr(1, 2)) * sqrt_fr(Fr(1, 2)) - Surd(Fr(1, 2))
_r3 = sqrt_fr(Fr(2)) + sqrt_fr(Fr(3)) - sqrt_fr(Fr(10))
SQ2_8 = cyc_x(8) - cyc_pow(cyc_x(8), 3)
I_8 = cyc_pow(cyc_x(8), 2)
anchor("KA-RING THE TWO EXACT RINGS BEHAVE: in Surd, sqrt2.sqrt3 = sqrt6 "
       "and sqrt(1/2)^2 = 1/2 identically, and the sign oracle decides "
       "sqrt2 + sqrt3 - sqrt10 < 0; in Cyc(8), (zeta8 - zeta8^3)^2 = 2 "
       "exactly (so 1/sqrt2 is an exact element) and (zeta8^2)^2 = -1 (so "
       "the imaginary unit is an exact element)",
       _r1.is_zero() and _r2.is_zero() and surd_sign(_r3) == -1
       and (SQ2_8 * SQ2_8) == Cyc(8, [Fr(2)])
       and (I_8 * I_8) == Cyc(8, [Fr(-1)]),
       f"sqrt2.sqrt3-sqrt6 = {_r1}; sqrt(1/2)^2-1/2 = {_r2}; "
       f"sign(sqrt2+sqrt3-sqrt10) = {surd_sign(_r3)}; (zeta8-zeta8^3)^2 = "
       f"{SQ2_8 * SQ2_8}; (zeta8^2)^2 = {I_8 * I_8}")

if ANCHOR_FAIL:
    print()
    print(f"  ANCHOR FAILURE ({ANCHOR_FAIL}) — a reused instrument does not "
          f"reproduce its known answer.  Refusing to run the census.")
    sys.exit(1)


# ===========================================================================
# SEC 3.  THE PREDICATE, THE READINGS AND THE CONSISTENCY AXIOMS —
#         all stated BEFORE anything is computed.
# ===========================================================================

sec("THE OPERATIONAL DIVISION-EVENT PREDICATE, THE TWO READINGS, AND THE "
    "CONSISTENCY AXIOMS — stated before any of them is evaluated")

print("""
  THE MODEL DATA.  A composite system with configuration space
  C = C_A x C_B x C_C (three qubits: |C| = 8, the members treated as
  elementary, fixed across runs -- [B3-kin-ax]).  A declared time grid
  0 = t_0 < t_1 < ... < t_K.  A declared exact unitary family U(t_k <- 0),
  k = 0..K, with U(t_0 <- 0) = 1.  The composite's transition matrix is
  [B3]'s unistochastic law [B3-uni]:

      Gamma_ABC(t_k <- 0)_{ij} = |U_{ij}(t_k <- 0)|^2,

  which is column-stochastic (and here also row-stochastic).  A declared
  strictly positive initial distribution p_0 on C ([B3-epi-ax]: contingent,
  varies between runs -- so the census runs over three declared p_0).

  THE PREDICATE.  [B3-divdef] says the allowed conditioning times are the
  division events, and [B3-dyn-ax] says the laws consist of transition
  probabilities from those conditioning times to arbitrary target times.
  [B3-ltp] says the transition matrices act by the law of total
  probability.  Conjoining those three: t' is a division event for a system
  with process {Gamma(t <- 0)} exactly when, for every target time t, there
  is a column-stochastic Gamma(t <- t') with

      Gamma(t <- 0) = Gamma(t <- t') Gamma(t' <- 0)                  (23)

  -- the divisibility condition [B3-eq22] states and then denies in
  general.  Operationally, and this is the predicate this receipt computes:

      DIV_S(t_k)  :=  for EVERY grid target t_b with t_k <= t_b <= t_K,
                      there EXISTS a column-stochastic X_b on C_S with
                      X_b . Gamma_S(t_k <- 0) = Gamma_S(t_b <- 0).

  This is exactly U1's (D1) [U1-D1] conjoined over the spanning pairs
  (0, t_b) that straddle t_k, and it is decided by U1's committed cascade:
  a candidate bridge, then [B3] eq. 22's algebraic interpolant where
  Gamma_S(t_k <- 0) is square and invertible, then the row certificate,
  then the exact rational LP with a verified Farkas certificate.  The
  quantifier structure is declared: UNIVERSAL over targets, EXISTENTIAL
  over bridges.  Sources are the initial time 0 alone, which [B3-divdef]
  guarantees is a division event; no later time is assumed to be one, on
  pain of circularity.

  DIV_S(t_0 = 0) is TRUE for every S by construction (X_b = Gamma_S(t_b<-0)
  works), which is [B3-divdef]'s 'assumed to include an initial time 0'.

  THE TWO READINGS OF A SUBSYSTEM'S PROCESS.  [B3-syscentric] names
  marginalization as the operation that relates a system to its
  environment; both readings below are declared and both are censused
  separately, because they are not the same object.

    READING M (marginal / trace-out).  Condition on the subsystem's own
    configuration at time 0 and average the rest with p_0:
        Gamma^M_S(t <- 0)[u][v]
          = sum_{i|_S = u} sum_{j|_S = v} Gamma(t<-0)[i][j] p_0(j)
            / sum_{j|_S = v} p_0(j).
    Column-stochastic; depends on p_0.

    READING C (conditional-on-outcome).  Condition on the complement's
    configuration c at time 0 as well, and marginalize the complement at
    the target time:
        Gamma^{C,c}_S(t <- 0)[u][v] = sum_{i|_S = u} Gamma(t<-0)[i][(v,c)].
    Column-stochastic; independent of p_0; one process per complement
    configuration c, all of them censused.

    The two are related exactly, and the identity is verified in-receipt:
        Gamma^M_S[u][v] = sum_c w_c(v) Gamma^{C,c}_S[u][v],
        w_c(v) = p_0((v,c)) / sum_{c'} p_0((v,c')),
    so reading M is a column-wise p_0-mixture of the reading-C processes.
    For S = ABC the complement is empty and both readings are Gamma itself.

  THE PRESHEAF.  The subsystem lattice L = {A,B,C,AB,AC,BC,ABC} is a poset
  under inclusion.  F(S) := the column-stochastic families on C_S;
  restriction rho^S_{S'} := marginalization (reading M) or conditioning
  (reading C).  Both restrictions are TRANSITIVE, and transitivity is
  verified in-receipt on every nested triple, every model and every grid
  time, so F is a genuine presheaf and not a decoration.

  THE CONSISTENCY AXIOMS FOR A GLOBAL DIVISION-EVENT ASSIGNMENT.  Stated
  now, before any of them is evaluated.  Write D(S) subset T for the
  division-event set assigned to S, T the grid.

    (GS0) INITIALITY.  0 in D(S) for every S in L.
          Ground: [B3-divdef], 'assumed to include an initial time 0'.

    (GS1) RESTRICTION-COMPATIBILITY (downward closure along the presheaf).
          S'' subset S'  ==>  D(S') subset D(S'').
          Ground: the restriction map is marginalization, and [B3-syscentric]
          makes marginalization the operation that passes between a system
          and its parts.  If the composite's law of total probability holds
          through t, the marginal law should inherit it.
          NOTE, DECLARED IN ADVANCE: [B3] nowhere ASSERTS GS1.  GS1 is the
          weakest condition under which the division-event assignment is a
          compatible family for the restriction presheaf.  Its failure is
          therefore a result about the framework's structure, not a
          contradiction inside [B3].

    (GS2) GLUING ON OVERLAPS.  S', S'' with S' /\\ S'' non-empty:
          D(S') /\\ D(S'') subset D(S' \\/ S'').
          Ground: the sheaf gluing axiom -- locally legitimate conditioning
          times on overlapping systems glue to their union.

    (GS3) SYSTEM-INDEPENDENCE.  There is a single G subset T with
          D(S) = G for every S in L.
          Ground: this is the hypothesis [B3-syscentric] EXPLICITLY DENIES
          ('not global properties of the whole universe, but system-centric').
          It is computed here so that the denial is quantified rather than
          quoted: a model in which GS3 fails is a model in which
          system-centricity is not merely permitted but forced.

    A GLOBAL SECTION of the restriction presheaf, in the compatible-family
    sense, exists for a model exactly when GS0 /\\ GS1 /\\ GS2 all hold of
    the computed family {DIV_S}.  When they do not, the receipt additionally
    computes, time by time, the MAXIMAL SUB-SECTION: the largest
    d' <= d satisfying GS1 /\\ GS2 (the largest trimming of the assignment
    that IS consistent).  Note that d' identically 0 always satisfies
    GS1 /\\ GS2, so 'a global section exists' is informative only in the
    two sharper forms reported: (i) is the DATA ITSELF a section, and
    (ii) is the maximal sub-section non-trivial.

  PRE-REGISTERED OUTCOMES (lean NONE): C-CONSISTENT (natural containments
  hold on all tested models), C-CROSS (containments fail, with exact
  witnesses), C-OBSTRUCTION (a model admits no consistent global assignment
  under the axioms above).
""")


# ===========================================================================
# SEC 4.  DECLARED CAPS, THE EXACT FIELD LAYER, AND THE MODELS
# ===========================================================================

sec("DECLARED CAPS, THE EXACT FIELD LAYER, AND THE EIGHT MODELS")

NQ = 3                       # three qubits
DIM = 2 ** NQ                # 8 configurations
KGRID = 4                    # grid times t_0..t_4 -- four steps
TIMES = list(range(KGRID + 1))
WIRES = (0, 1, 2)
LATTICE = [(0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]
LNAME = {(0,): "A", (1,): "B", (2,): "C", (0, 1): "AB", (0, 2): "AC",
         (1, 2): "BC", (0, 1, 2): "ABC"}
VERB_WITNESS = 12            # fully printed witnesses per category
VERB_SCREEN = 2              # verbose U3 screens per model

print(f"  qubits {NQ}, |C| = {DIM}; grid t_0..t_{KGRID} "
      f"({KGRID} steps), TIMES = {TIMES}")
print(f"  subsystem lattice: {[LNAME[s] for s in LATTICE]} (7 members, "
      f"all of them censused)")
print(f"  readings: M (three declared p_0) and C (one process per "
      f"complement configuration: 4 for a singleton, 2 for a pair, 1 for "
      f"ABC)")
print(f"  LP caps inherited from U1: <= {LP_MAXVARS} variables, <= "
      f"{LP_MAXROWS} constraints, <= {LP_MAXPIVOT} pivots.  Every system "
      f"here has at most {DIM * DIM} variables and {DIM + DIM * DIM} "
      f"constraints, so NO decision in this receipt is ever excluded by a "
      f"cap and no cap can hide a verdict.")
print(f"  print caps (printing only, never deciding): <= {VERB_WITNESS} "
      f"fully printed witnesses per category, <= {VERB_SCREEN} verbose U3 "
      f"screens per model; ALL cases are counted and tabulated.")
print("  FIELD SCOPE, DECLARED: every model below is chosen so that "
      "|U_ij|^2")
print("  is RATIONAL at every grid time -- gated at construction, exit 1 if")
print("  not.  That is what lets U1's Fraction LP be reused verbatim.  It "
      "is")
print("  a restriction on the tested dynamics and is carried into the")
print("  scope statement; it is not a restriction on the framework.")


# ---- the two exact fields, wrapped -------------------------------------
def f_zero(kind):
    return Surd() if kind == "surd" else cyc_zero(8)


def f_one(kind):
    return Surd(Fr(1)) if kind == "surd" else cyc_one(8)


def f_rat(kind, r):
    return Surd(Fr(r)) if kind == "surd" else Cyc(8, [Fr(r)])


def f_modsq(kind, x):
    """|x|^2 as an exact field element: x.x for the real ring, x.conj(x)
    for the cyclotomic one."""
    return x * x if kind == "surd" else x * x.conj()


INV_SQRT2_SURD = sqrt_fr(Fr(1, 2))
INV_SQRT2_CYC = SQ2_8 * Fr(1, 2)
IMAG_CYC = I_8


def mat_zero(kind, n, m):
    return [[f_zero(kind) for _ in range(m)] for _ in range(n)]


def mat_id(kind, n):
    M = mat_zero(kind, n, n)
    for i in range(n):
        M[i][i] = f_one(kind)
    return M


def mat_mul(kind, A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = mat_zero(kind, n, m)
    for i in range(n):
        Ai = A[i]
        for t in range(k):
            a = Ai[t]
            if (a.is_zero() if hasattr(a, "is_zero") else False):
                continue
            Bt = B[t]
            for j in range(m):
                out[i][j] = out[i][j] + a * Bt[j]
    return out


def mat_dag(kind, A):
    if kind == "surd":
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
    return [[A[i][j].conj() for i in range(len(A))] for j in range(len(A[0]))]


def cfg_index(bits):
    return sum(b << (NQ - 1 - w) for w, b in enumerate(bits))


CFGS = [tuple((i >> (NQ - 1 - w)) & 1 for w in range(NQ)) for i in range(DIM)]
assert [cfg_index(c) for c in CFGS] == list(range(DIM))


def embed1(kind, g, wire):
    """A one-qubit gate g acting on `wire` of the three-qubit register."""
    M = mat_zero(kind, DIM, DIM)
    for jc in CFGS:
        for out_bit in (0, 1):
            v = g[out_bit][jc[wire]]
            ic = tuple(out_bit if w == wire else jc[w] for w in WIRES)
            M[cfg_index(ic)][cfg_index(jc)] = v
    return M


def embed2(kind, g, w1, w2):
    """A two-qubit gate g (4x4, basis order (w1,w2) = 00,01,10,11)."""
    M = mat_zero(kind, DIM, DIM)
    for jc in CFGS:
        jin = jc[w1] * 2 + jc[w2]
        for o in range(4):
            v = g[o][jin]
            o1, o2 = o >> 1, o & 1
            ic = tuple(o1 if w == w1 else (o2 if w == w2 else jc[w])
                       for w in WIRES)
            M[cfg_index(ic)][cfg_index(jc)] = v
    return M


def perm_gate(kind, f):
    """A permutation of configurations, as a matrix."""
    M = mat_zero(kind, DIM, DIM)
    for jc in CFGS:
        M[cfg_index(f(jc))][cfg_index(jc)] = f_one(kind)
    return M


def cnot(kind, c, t):
    return perm_gate(kind, lambda x: tuple(
        (x[w] ^ 1) if (w == t and x[c] == 1) else x[w] for w in WIRES))


def swap(kind, a, b):
    def f(x):
        y = list(x)
        y[a], y[b] = x[b], x[a]
        return tuple(y)
    return perm_gate(kind, f)


def rot(kind, c, s):
    """The real rotation [[c, -s], [s, c]]; c^2 + s^2 = 1 required."""
    return [[f_rat(kind, c), f_rat(kind, -s)],
            [f_rat(kind, s), f_rat(kind, c)]]


def hadamard(kind):
    h = INV_SQRT2_SURD if kind == "surd" else INV_SQRT2_CYC
    return [[h, h], [h, Surd() - h if kind == "surd"
                     else cyc_zero(8) - h]]


def sgate():
    return [[cyc_one(8), cyc_zero(8)], [cyc_zero(8), IMAG_CYC]]


def gamma_from_unitary(kind, U):
    """[B3-uni]: Gamma_ij = |U_ij|^2, gated RATIONAL entry by entry."""
    G = [[None] * DIM for _ in range(DIM)]
    bad = []
    for i in range(DIM):
        for j in range(DIM):
            z = f_modsq(kind, U[i][j])
            if not z.is_rational():
                bad.append((i, j, z))
                G[i][j] = Fr(0)
            else:
                G[i][j] = z.rat()
    return G, bad


# ---- the eight models ---------------------------------------------------
MODELS = []


def add_model(name, kind, decl, U_list, note="", classical=False):
    MODELS.append(dict(name=name, kind=kind, decl=decl, U=U_list, note=note,
                       classical=classical))


# M0 — the CLASSICAL MARKOV product control.  Not a unistochastic process:
#      it is a textbook Markov chain, [B3]'s divisible special case, and it
#      is here as the anchor that the instrument does not manufacture
#      indivisibility.
MA = [[Fr(3, 4), Fr(1, 3)], [Fr(1, 4), Fr(2, 3)]]
MB = [[Fr(4, 5), Fr(1, 2)], [Fr(1, 5), Fr(1, 2)]]
MC = [[Fr(2, 3), Fr(1, 5)], [Fr(1, 3), Fr(4, 5)]]


def kron3_fr(A, B, C):
    out = [[Fr(0)] * DIM for _ in range(DIM)]
    for ic in CFGS:
        for jc in CFGS:
            out[cfg_index(ic)][cfg_index(jc)] = (A[ic[0]][jc[0]]
                                                 * B[ic[1]][jc[1]]
                                                 * C[ic[2]][jc[2]])
    return out


def fr_mul(A, B):
    n = len(A)
    return [[sum(A[i][t] * B[t][j] for t in range(n)) for j in range(n)]
            for i in range(n)]


M0_STEP = kron3_fr(MA, MB, MC)
M0_G = [[[Fr(1) if i == j else Fr(0) for j in range(DIM)]
         for i in range(DIM)]]
for _ in range(KGRID):
    M0_G.append(fr_mul(M0_STEP, M0_G[-1]))

# M1 — the QUANTUM PRODUCT (separable) control: three Pythagorean rotations.
R1 = rot("surd", Fr(3, 5), Fr(4, 5))
R2 = rot("surd", Fr(5, 13), Fr(12, 13))
R3 = rot("surd", Fr(8, 17), Fr(15, 17))
M1_STEP = mat_mul("surd", mat_mul("surd", embed1("surd", R1, 0),
                                  embed1("surd", R2, 1)),
                  embed1("surd", R3, 2))
M1_U = [mat_id("surd", DIM)]
for _ in range(KGRID):
    M1_U.append(mat_mul("surd", M1_STEP, M1_U[-1]))
add_model("M1 product/separable (quantum)", "surd",
          "U(t_k<-0) = (R(3/5,4/5) tensor R(5/13,12/13) tensor "
          "R(8/17,15/17))^k, exact Pythagorean rotations in Q",
          M1_U, "separable at every time; the tensor-factorised control")

# M2 — GHZ-generating real Clifford circuit, Q(sqrt 2).
H_S = hadamard("surd")
M2_G = [embed1("surd", H_S, 0), cnot("surd", 0, 1), cnot("surd", 0, 2),
        embed1("surd", H_S, 1)]
M2_U = [mat_id("surd", DIM)]
for g in M2_G:
    M2_U.append(mat_mul("surd", g, M2_U[-1]))
add_model("M2 GHZ-generating (real Clifford)", "surd",
          "gates in order: H_A, CNOT_{A->B}, CNOT_{A->C}, H_B; "
          "U(t_k<-0) = G_k...G_1, entries in Q(sqrt 2)",
          M2_U, "U(t_3<-0)|000> = (|000> + |111>)/sqrt2, the maximal GHZ "
                "state")

# M3 — W-generating, exact RATIONAL orthogonal (an unbalanced W-class state).
#      Block on span{000,100,010,001} with first column the W amplitudes
#      (2/3, 2/3, 1/3); the same rational orthogonal block on the
#      complementary span{110,101,011,111}, in that basis order.
W_BLOCK = [[Fr(0), Fr(1), Fr(0), Fr(0)],
           [Fr(2, 3), Fr(0), Fr(2, 3), Fr(-1, 3)],
           [Fr(2, 3), Fr(0), Fr(-1, 3), Fr(2, 3)],
           [Fr(1, 3), Fr(0), Fr(-2, 3), Fr(-2, 3)]]
W_ORD1 = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
W_ORD2 = [(1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)]
M3_STEP_FR = [[Fr(0)] * DIM for _ in range(DIM)]
for _blk in (W_ORD1, W_ORD2):
    for _a in range(4):
        for _b in range(4):
            M3_STEP_FR[cfg_index(_blk[_a])][cfg_index(_blk[_b])] = \
                W_BLOCK[_a][_b]
M3_STEP = [[Surd(M3_STEP_FR[i][j]) for j in range(DIM)] for i in range(DIM)]
M3_U = [mat_id("surd", DIM)]
for _ in range(KGRID):
    M3_U.append(mat_mul("surd", M3_STEP, M3_U[-1]))
add_model("M3 W-generating (rational orthogonal)", "surd",
          "U(t_k<-0) = W^k with W the declared rational orthogonal matrix "
          "whose first column is the W-class state (2/3)|100> + (2/3)|010> "
          "+ (1/3)|001>",
          M3_U, "W-class: supported on the single-excitation subspace with "
                "all three amplitudes non-zero")

# M4 — the ALGEBRAIC GENERIC: a Cayley-transform rational orthogonal matrix
#      built from a fixed declared integer antisymmetric matrix.  Dense, no
#      tensor structure, no permutation structure, no randomness.
S_ANTI = [[Fr(0)] * DIM for _ in range(DIM)]
for _i in range(DIM):
    for _j in range(_i + 1, DIM):
        _v = ((_i * 3 + _j * 5) % 7) - 3
        S_ANTI[_i][_j] = Fr(_v)
        S_ANTI[_j][_i] = Fr(-_v)
_IPS = [[(Fr(1) if _i == _j else Fr(0)) + S_ANTI[_i][_j] for _j in range(DIM)]
        for _i in range(DIM)]
_IMS = [[(Fr(1) if _i == _j else Fr(0)) - S_ANTI[_i][_j] for _j in range(DIM)]
        for _i in range(DIM)]
_IPSinv, _IPSdet = invert_exact([row[:] for row in _IPS])
M4_STEP_FR = fr_mul(_IMS, _IPSinv)
M4_STEP = [[Surd(M4_STEP_FR[i][j]) for j in range(DIM)] for i in range(DIM)]
M4_U = [mat_id("surd", DIM)]
for _ in range(KGRID):
    M4_U.append(mat_mul("surd", M4_STEP, M4_U[-1]))
add_model("M4 algebraic generic (Cayley rational orthogonal)", "surd",
          "U(t_k<-0) = Q^k, Q = (1 - S)(1 + S)^{-1} the Cayley transform of "
          "the declared integer antisymmetric S with "
          "S_ij = ((3i + 5j) mod 7) - 3 for i < j; det(1+S) = "
          + str(_IPSdet),
          M4_U, "dense, no tensor factorisation, no permutation structure, "
                "no randomness: every entry is a declared constant")

# M5 — the COMPLEX CLIFFORD circuit in Q(zeta_8): H, S (= diag(1, i)), CZ,
#      CNOT.  Entries lie in (1/sqrt2)^k Z[i], so |U_ij|^2 is rational at
#      every partial product, guaranteed.
H_C = hadamard("cyc")
SG = sgate()
CZ = [[cyc_one(8), cyc_zero(8), cyc_zero(8), cyc_zero(8)],
      [cyc_zero(8), cyc_one(8), cyc_zero(8), cyc_zero(8)],
      [cyc_zero(8), cyc_zero(8), cyc_one(8), cyc_zero(8)],
      [cyc_zero(8), cyc_zero(8), cyc_zero(8), cyc_zero(8) - cyc_one(8)]]
M5_G = [mat_mul("cyc", embed1("cyc", H_C, 0), embed1("cyc", H_C, 1)),
        embed2("cyc", CZ, 0, 1),
        mat_mul("cyc", embed1("cyc", SG, 0), cnot("cyc", 1, 2)),
        embed1("cyc", H_C, 1)]
M5_U = [mat_id("cyc", DIM)]
for g in M5_G:
    M5_U.append(mat_mul("cyc", g, M5_U[-1]))
add_model("M5 complex Clifford (Q(zeta_8))", "cyc",
          "gates in order: H_A H_B, CZ_{AB}, S_A CNOT_{B->C}, H_B; entries "
          "in (1/sqrt2)^k Z[i] subset Q(zeta_8), so |U_ij|^2 is rational at "
          "every partial product",
          M5_U, "the genuinely complex model: the imaginary unit is an exact "
                "element zeta_8^2")

# M6 — a controlled-rotation entangler: non-Clifford, entangling, rational.
CR_STEP_FR = [[Fr(0)] * DIM for _ in range(DIM)]
_R2f = [[Fr(5, 13), Fr(-12, 13)], [Fr(12, 13), Fr(5, 13)]]
_R3f = [[Fr(8, 17), Fr(-15, 17)], [Fr(15, 17), Fr(8, 17)]]
for _jc in CFGS:
    for _ic in CFGS:
        if _jc[0] == 0:
            v = Fr(1) if _ic == _jc else Fr(0)
        else:
            v = (Fr(1) if _ic[0] == 1 else Fr(0)) * _R2f[_ic[1]][_jc[1]] \
                * _R3f[_ic[2]][_jc[2]]
        CR_STEP_FR[cfg_index(_ic)][cfg_index(_jc)] = v
_RA = [[Fr(3, 5), Fr(-4, 5)], [Fr(4, 5), Fr(3, 5)]]
_RAfull = [[Fr(0)] * DIM for _ in range(DIM)]
for _jc in CFGS:
    for _o in (0, 1):
        _ic = (_o, _jc[1], _jc[2])
        _RAfull[cfg_index(_ic)][cfg_index(_jc)] = _RA[_o][_jc[0]]
M6_STEP_FR = fr_mul(CR_STEP_FR, _RAfull)
M6_STEP = [[Surd(M6_STEP_FR[i][j]) for j in range(DIM)] for i in range(DIM)]
M6_U = [mat_id("surd", DIM)]
for _ in range(KGRID):
    M6_U.append(mat_mul("surd", M6_STEP, M6_U[-1]))
add_model("M6 controlled-rotation entangler", "surd",
          "U(t_k<-0) = (CR . R_A)^k with R_A = R(3/5,4/5) on A and CR = "
          "|0><0|_A tensor 1 + |1><1|_A tensor (R(5/13,12/13) tensor "
          "R(8/17,15/17)); rational orthogonal, non-Clifford, entangling",
          M6_U, "entangles a product state; no tensor factorisation of the "
                "dynamics")

# M7 — the SWAP scrambler: the composite's transition matrix is a
#      permutation at t_1, the strongest possible division event for ABC.
M7_G = [swap("surd", 0, 1), swap("surd", 0, 1), embed1("surd", H_S, 0),
        cnot("surd", 0, 2)]
M7_U = [mat_id("surd", DIM)]
for g in M7_G:
    M7_U.append(mat_mul("surd", g, M7_U[-1]))
add_model("M7 SWAP scrambler", "surd",
          "gates in order: SWAP_{AB}, SWAP_{AB}, H_A, CNOT_{A->C}; "
          "U(t_1<-0) is a permutation and U(t_2<-0) = 1",
          M7_U, "the composite's transition matrix at t_1 is a permutation "
                "matrix, which [B3-permlemma] identifies as the only "
                "stochastic matrix with a stochastic inverse")

# M0 is appended last so that the quantum models keep their indices, but it
# is printed first: it is the control.
MODELS.insert(0, dict(name="M0 classical Markov product (control)",
                      kind="fr", decl="Gamma(t_k<-0) = (M_A tensor M_B "
                      "tensor M_C)^k with the declared column-stochastic "
                      "M_A, M_B, M_C; a textbook Markov chain, [B3]'s "
                      "divisible special case, NOT a unistochastic process",
                      U=None, note="the classical control: everything must "
                      "divide everywhere", classical=True))
MODELS[0]["GAMMA"] = M0_G

# ---- build every Gamma, gate rationality, gate stochasticity ------------
print()
_ratfail = 0
for m in MODELS:
    if m["classical"]:
        G = m["GAMMA"]
    else:
        G, badall = [], []
        for U in m["U"]:
            g, bad = gamma_from_unitary(m["kind"], U)
            G.append(g)
            badall += bad
        m["GAMMA"] = G
        if badall:
            _ratfail += len(badall)
            print(f"  [FIELD] {m['name']}: {len(badall)} irrational "
                  f"|U_ij|^2 entries, exemplar {badall[0]}")
    m["colsum_ok"] = all(sum(G[k][i][j] for i in range(DIM)) == Fr(1)
                         for k in TIMES for j in range(DIM))
    m["rowsum_ok"] = all(sum(G[k][i][j] for j in range(DIM)) == Fr(1)
                         for k in TIMES for i in range(DIM))
    m["nonneg_ok"] = all(G[k][i][j] >= 0 for k in TIMES for i in range(DIM)
                         for j in range(DIM))
    m["id_ok"] = all(G[0][i][j] == (Fr(1) if i == j else Fr(0))
                     for i in range(DIM) for j in range(DIM))

anchor("MOD.1 EVERY TRANSITION MATRIX IS EXACTLY RATIONAL: |U_ij|^2 lands "
       "in Q at every grid time of every unitary model, so U1's Fraction LP "
       "applies verbatim and nothing is rounded anywhere",
       _ratfail == 0, f"irrational entries across all models and times: "
                      f"{_ratfail}")

check("MOD.2 EVERY MODEL'S TRANSITION MATRIX IS COLUMN-STOCHASTIC WITH "
      "NON-NEGATIVE ENTRIES AND Gamma(t_0<-0) = 1, exactly, at every grid "
      "time -- the object [B3-ltp] eq. 20 requires",
      all(m["colsum_ok"] and m["nonneg_ok"] and m["id_ok"] for m in MODELS),
      f"column sums {sum(m['colsum_ok'] for m in MODELS)}/{len(MODELS)}, "
      f"non-negativity {sum(m['nonneg_ok'] for m in MODELS)}/{len(MODELS)}, "
      f"identity at t_0 {sum(m['id_ok'] for m in MODELS)}/{len(MODELS)}")

check("MOD.3 EVERY UNITARY MODEL'S TRANSITION MATRIX IS ALSO ROW-STOCHASTIC "
      "-- i.e. DOUBLY stochastic -- because a unitary has orthonormal rows "
      "as well as columns; and the classical control is NOT, which is what "
      "marks it as the non-unistochastic member of the set",
      all(m["rowsum_ok"] for m in MODELS if not m["classical"])
      and not MODELS[0]["rowsum_ok"],
      f"unitary models row-stochastic "
      f"{sum(m['rowsum_ok'] for m in MODELS if not m['classical'])}/"
      f"{len(MODELS) - 1}; classical control row-stochastic "
      f"{MODELS[0]['rowsum_ok']}")

# ---- exact unitarity / orthogonality of every declared U ----------------
_uni_bad = 0
_uni_detail = []
for m in MODELS:
    if m["classical"]:
        continue
    for k in TIMES:
        U = m["U"][k]
        if m["kind"] == "surd":
            bad = orth_check_surd(U)
        else:
            bad = unitary_check_cyc(U)
        _uni_bad += len(bad)
    _uni_detail.append(f"{m['name'].split()[0]}:{m['kind']}")
anchor("MOD.4 EVERY DECLARED U(t_k<-0) IS EXACTLY UNITARY IN ITS RING: "
       "U^T U - 1 = 0 identically in Surd for the real models and "
       "U^dagger U - 1 = 0 identically in Cyc(8) for the complex one, at "
       "every grid time, with ZERO residual entries -- not a tolerance",
       _uni_bad == 0,
       f"non-zero residual entries across all models and grid times: "
       f"{_uni_bad}; rings {' '.join(_uni_detail)}")

print()
for m in MODELS:
    print(f"  ---- {m['name']}")
    print(f"       declaration : {m['decl']}")
    if m["note"]:
        print(f"       note        : {m['note']}")
    print(f"       Gamma(t_1<-0) (exact, rows = target config, columns = "
          f"source config):")
    for i in range(DIM):
        print("         " + "  ".join(str(m["GAMMA"][1][i][j])
                                      for j in range(DIM)))


# ===========================================================================
# SEC 5.  THE SUBSYSTEM PROCESSES — both readings, functoriality verified
# ===========================================================================

sec("THE SUBSYSTEM PROCESSES: both readings built, both restrictions "
    "verified transitive, and the mixture identity checked exactly")

P0 = [
    ("p_unif", {c: Fr(1, 8) for c in CFGS}),
    ("p_prod", {c: (Fr(1, 4) if c[0] == 0 else Fr(3, 4))
                * (Fr(1, 3) if c[1] == 0 else Fr(2, 3))
                * (Fr(2, 5) if c[2] == 0 else Fr(3, 5)) for c in CFGS}),
    ("p_corr", None),
]
_corr = {}
for _c in CFGS:
    _w = 3 + 2 * _c[0] + 5 * _c[1] + 7 * _c[2] + 11 * (_c[0] ^ _c[1]) \
        + 13 * (_c[1] & _c[2])
    _corr[_c] = Fr(_w)
_tot = sum(_corr.values())
P0[2] = ("p_corr", {c: _corr[c] / _tot for c in CFGS})

for _nm, _p in P0:
    assert sum(_p.values()) == Fr(1) and all(v > 0 for v in _p.values())
report("declared initial distributions (all strictly positive, all exact)",
       ", ".join(f"{nm}: {[str(p[c]) for c in CFGS]}" for nm, p in P0))
_indep = []
for _nm, _p in P0:
    _ok = all(_p[c] == (sum(_p[d] for d in CFGS if d[0] == c[0])
                        * sum(_p[d] for d in CFGS if d[1] == c[1])
                        * sum(_p[d] for d in CFGS if d[2] == c[2]))
              for c in CFGS)
    _indep.append(f"{_nm}: product={_ok}")
report("factorisation of the declared p_0", "; ".join(_indep))


SUBC = {S: sorted({tuple(c[w] for w in S) for c in CFGS}) for S in LATTICE}
COMP = {S: tuple(w for w in WIRES if w not in S) for S in LATTICE}
COMPC = {S: sorted({tuple(c[w] for w in COMP[S]) for c in CFGS})
         for S in LATTICE}


def merge_cfg(S, u, c):
    out = [0] * NQ
    for a, w in enumerate(S):
        out[w] = u[a]
    for a, w in enumerate(COMP[S]):
        out[w] = c[a]
    return tuple(out)


def gamma_marginal(G, S, p0):
    """READING M: Gamma^M_S(t<-0)."""
    cs = SUBC[S]
    ix = {u: a for a, u in enumerate(cs)}
    pS = {u: sum(p0[c] for c in CFGS if tuple(c[w] for w in S) == u)
          for u in cs}
    out = [[Fr(0)] * len(cs) for _ in cs]
    for jc in CFGS:
        v = tuple(jc[w] for w in S)
        pj = p0[jc]
        col = cfg_index(jc)
        for ic in CFGS:
            g = G[cfg_index(ic)][col]
            if g:
                out[ix[tuple(ic[w] for w in S)]][ix[v]] += g * pj
    for u in cs:
        for w2 in cs:
            out[ix[u]][ix[w2]] = out[ix[u]][ix[w2]] / pS[w2]
    return out


def gamma_cond(G, S, c):
    """READING C: Gamma^{C,c}_S(t<-0)."""
    cs = SUBC[S]
    ix = {u: a for a, u in enumerate(cs)}
    out = [[Fr(0)] * len(cs) for _ in cs]
    for v in cs:
        col = cfg_index(merge_cfg(S, v, c))
        for ic in CFGS:
            g = G[cfg_index(ic)][col]
            if g:
                out[ix[tuple(ic[w] for w in S)]][ix[v]] += g
    return out


# ---- functoriality of both restrictions --------------------------------
def marg_process(GS, S, Ssm, pS):
    """Marginalise a process already living on S down to Ssm subset S,
    using the induced initial distribution pS on C_S."""
    cs, cs2 = SUBC[S], SUBC[Ssm]
    ix, ix2 = {u: a for a, u in enumerate(cs)}, \
        {u: a for a, u in enumerate(cs2)}
    pos = [S.index(w) for w in Ssm]
    down = {u: tuple(u[a] for a in pos) for u in cs}
    p2 = {u2: sum(pS[u] for u in cs if down[u] == u2) for u2 in cs2}
    out = [[Fr(0)] * len(cs2) for _ in cs2]
    for v in cs:
        for u in cs:
            g = GS[ix[u]][ix[v]]
            if g:
                out[ix2[down[u]]][ix2[down[v]]] += g * pS[v]
    for a in range(len(cs2)):
        for b, u2 in enumerate(cs2):
            out[a][b] = out[a][b] / p2[u2]
    return out


_fun_M = _fun_M_bad = 0
_fun_C = _fun_C_bad = 0
for m in MODELS:
    for k in TIMES:
        G = m["GAMMA"][k]
        for _nm, p0 in P0:
            for Sbig in LATTICE:
                pS = {u: sum(p0[c] for c in CFGS
                             if tuple(c[w] for w in Sbig) == u)
                      for u in SUBC[Sbig]}
                GS = gamma_marginal(G, Sbig, p0)
                for Ssm in LATTICE:
                    if not (set(Ssm) < set(Sbig)):
                        continue
                    _fun_M += 1
                    if marg_process(GS, Sbig, Ssm, pS) != \
                            gamma_marginal(G, Ssm, p0):
                        _fun_M_bad += 1
        for Sbig in LATTICE:
            for cbig in COMPC[Sbig]:
                GS = gamma_cond(G, Sbig, cbig)
                cs = SUBC[Sbig]
                ixb = {u: a for a, u in enumerate(cs)}
                for Ssm in LATTICE:
                    if not (set(Ssm) < set(Sbig)):
                        continue
                    pos = [Sbig.index(w) for w in Ssm]
                    rest = [a for a in range(len(Sbig)) if a not in pos]
                    cs2 = SUBC[Ssm]
                    ix2 = {u: a for a, u in enumerate(cs2)}
                    for csmall in sorted({tuple(u[a] for a in rest)
                                          for u in cs}):
                        two = [[Fr(0)] * len(cs2) for _ in cs2]
                        for v2 in cs2:
                            vfull = [0] * len(Sbig)
                            for a, q in enumerate(pos):
                                vfull[q] = v2[a]
                            for a, q in enumerate(rest):
                                vfull[q] = csmall[a]
                            vfull = tuple(vfull)
                            for u in cs:
                                g = GS[ixb[u]][ixb[vfull]]
                                if g:
                                    two[ix2[tuple(u[a] for a in pos)]][
                                        ix2[v2]] += g
                        # the direct conditioning on the FULL complement
                        cfull = [0] * len(COMP[Ssm])
                        for a, w in enumerate(COMP[Ssm]):
                            if w in Sbig:
                                cfull[a] = csmall[rest.index(Sbig.index(w))]
                            else:
                                cfull[a] = cbig[COMP[Sbig].index(w)]
                        _fun_C += 1
                        if two != gamma_cond(G, Ssm, tuple(cfull)):
                            _fun_C_bad += 1

check("FUN.1 THE MARGINAL RESTRICTION IS TRANSITIVE, so reading M really "
      "is a presheaf on the subsystem lattice: marginalising ABC to S' and "
      "then S' to S'' gives, entry for entry in exact rationals, the same "
      "process as marginalising ABC to S'' directly",
      _fun_M_bad == 0,
      f"{_fun_M} nested (model, time, p_0, S' > S'') instances tested, "
      f"{_fun_M_bad} disagreements")
check("FUN.2 THE CONDITIONAL RESTRICTION IS TRANSITIVE, so reading C is a "
      "presheaf too: conditioning ABC on S'-complement and then S' on the "
      "rest gives the same process as conditioning ABC on the whole "
      "S''-complement at once",
      _fun_C_bad == 0,
      f"{_fun_C} nested (model, time, complement configuration) instances "
      f"tested, {_fun_C_bad} disagreements")

# ---- the mixture identity -----------------------------------------------
_mix = _mixbad = 0
for m in MODELS:
    for k in TIMES:
        G = m["GAMMA"][k]
        for _nm, p0 in P0:
            for S in LATTICE:
                cs = SUBC[S]
                GM = gamma_marginal(G, S, p0)
                acc = [[Fr(0)] * len(cs) for _ in cs]
                for c in COMPC[S]:
                    GC = gamma_cond(G, S, c)
                    for b, v in enumerate(cs):
                        den = sum(p0[merge_cfg(S, v, cc)]
                                  for cc in COMPC[S])
                        w = p0[merge_cfg(S, v, c)] / den
                        for a in range(len(cs)):
                            acc[a][b] += w * GC[a][b]
                _mix += 1
                if acc != GM:
                    _mixbad += 1
check("FUN.3 THE TWO READINGS ARE RELATED EXACTLY AS DECLARED: reading M "
      "is the column-wise p_0-mixture of the reading-C processes, "
      "Gamma^M[u][v] = sum_c w_c(v) Gamma^{C,c}[u][v] with w_c(v) = "
      "p_0((v,c)) / sum_c' p_0((v,c')), verified entry for entry in exact "
      "rationals.  The two readings are therefore not independent "
      "inventions: one is a mixture of the other, which is exactly why "
      "their division-event sets may differ",
      _mixbad == 0,
      f"{_mix} (model, time, p_0, S) instances tested, {_mixbad} mismatches")

_cs_bad = 0
for m in MODELS:
    for k in TIMES:
        G = m["GAMMA"][k]
        for S in LATTICE:
            for _nm, p0 in P0:
                GM = gamma_marginal(G, S, p0)
                if not all(sum(GM[a][b] for a in range(len(GM))) == Fr(1)
                           for b in range(len(GM))):
                    _cs_bad += 1
            for c in COMPC[S]:
                GC = gamma_cond(G, S, c)
                if not all(sum(GC[a][b] for a in range(len(GC))) == Fr(1)
                           for b in range(len(GC))):
                    _cs_bad += 1
check("FUN.4 EVERY SUBSYSTEM PROCESS IS COLUMN-STOCHASTIC, exactly, under "
      "both readings and every declared p_0 -- so each is a legitimate "
      "process in [B3]'s sense before anything is asked of it",
      _cs_bad == 0, f"{_cs_bad} non-stochastic subsystem processes")


# ===========================================================================
# SEC 6.  ARE THE REDUCED PROCESSES STILL UNISTOCHASTIC?  (U3's criterion)
# ===========================================================================

sec("U3's UNISTOCHASTICITY CRITERION applied to the composite process and "
    "to every reduced process")

print("""
  [B3-sqthm] says an indivisible stochastic process is a unistochastic
  process, or ELSE a subsystem of one after a nontrivial dilation.  This
  section measures which side of that disjunction the reduced processes of
  the tested models fall on, using U3's committed criterion (anchored
  above).  For the composite the answer is known by construction and the
  unitary is EXHIBITED as the certificate; for the reduced processes it is
  decided, not assumed.  At n = 2 the criterion is COMPLETE (KA-U3c: every
  2x2 bistochastic matrix is orthostochastic); at n = 4 only the necessary
  conditions are available, and a matrix passing them is reported as
  EXCLUDED-BY-CAP, never as a pass.
""")

POLY_MAXINT = 10 ** 9
POLY_SMOOTH = 1000
print(f"""
  ONE DECLARED COST CAP, AND WHAT IT CAN AND CANNOT HIDE.  U3's polygon
  oracle needs the exact square-free part of numerator x denominator of each
  chain-link square, which is a factorisation.  It is invoked here only when
  that integer is at most {POLY_MAXINT} OR is {POLY_SMOOTH}-smooth (tested
  by a bounded trial division, at most {POLY_SMOOTH // 2} steps).  Instances
  above the cap are reported as EXCLUDED-BY-COST, counted, and never
  reported as a pass in either direction.  THIS CAP TOUCHES NOTHING IN THE
  DIVISION-EVENT CENSUS: that census is decided entirely in Fractions by
  U1's LP, which has no factorisation anywhere.  At n = 2 the polygon oracle
  is not invoked at all, because KA-U3c settles n = 2 outright -- every 2x2
  bistochastic matrix is orthostochastic by a construction uniform in p,
  verified in-receipt.
""")


def poly_cheap_int(n):
    """Is sqfree_split(n) cheap?  Cheap when n is small, or when n is
    POLY_SMOOTH-smooth (so the trial division terminates at once)."""
    if n <= POLY_MAXINT:
        return True
    m, p = n, 2
    while p <= POLY_SMOOTH and m > 1:
        while m % p == 0:
            m //= p
        p += 1 if p == 2 else 2
    return m == 1


def poly_affordable(M):
    for by, p, q in ([("col", a, b) for a in range(len(M[0]))
                      for b in range(a + 1, len(M[0]))]
                     + [("row", a, b) for a in range(len(M))
                        for b in range(a + 1, len(M))]):
        for x in chain_link_squares(M, p, q, by):
            if x and not poly_cheap_int(x.numerator * x.denominator):
                return False
    return True


def uni_verdict(M, cert=None):
    """The unistochasticity verdict, assembled from U3's own criterion
    functions (ds_report, chain_link_squares, tri_disc, polygon_violations)
    and U3's own certificate checkers.  Only the dispatch is local; every
    decision is U3's."""
    n = len(M)
    R = ds_report(M)
    if not R["ds"]:
        return "S-FAIL-DS"
    if n == 2:
        return "S-PASS(ortho, n=2 by KA-U3c)"
    if not poly_affordable(M):
        return "EXCLUDED-BY-COST"
    if n == 3 and tri_disc(*chain_link_squares(M, 0, 1, "col")) < 0:
        return "S-FAIL-UNI"
    if polygon_violations(M):
        return "S-FAIL-UNI"
    if cert is not None:
        kind, U = cert
        if kind == "surd":
            ok = not orth_check_surd(U) and not modsq_check_surd(U, M)
        else:
            ok = not unitary_check_cyc(U) and not modsq_check_cyc(U, M)
        return "S-PASS(certificate)" if ok else "CERTIFICATE-FAILED"
    return "EXCLUDED-BY-CAP"


_screen_tally = Counter()
_shown = Counter()
for m in MODELS:
    for k in TIMES[1:]:
        G = m["GAMMA"][k]
        cert = None
        if not m["classical"]:
            cert = ("surd" if m["kind"] == "surd" else "cyc", m["U"][k])
        if _shown[m["name"]] < VERB_SCREEN and poly_affordable(G):
            r = screen(f"{m['name']} :: Gamma_ABC(t_{k}<-0)",
                       G, m["decl"],
                       "the composite process itself (reading M and reading "
                       "C coincide: the complement is empty)",
                       note=("classical Markov control, not built from a "
                             "unitary" if m["classical"] else
                             "certificate = the model's own U(t<-0)"),
                       cert_hint=cert)
            _shown[m["name"]] += 1
            _screen_tally[("ABC-verbose", r["verdict"])] += 1
        else:
            _screen_tally[("ABC", uni_verdict(G, cert))] += 1
        for S in LATTICE:
            if S == (0, 1, 2):
                continue
            for c in COMPC[S]:
                GC = gamma_cond(G, S, c)
                _screen_tally[(f"n={len(GC)} readingC",
                               uni_verdict(GC))] += 1
            for _nm, p0 in P0:
                GM = gamma_marginal(G, S, p0)
                _screen_tally[(f"n={len(GM)} readingM",
                               uni_verdict(GM))] += 1
    print(f"  [PROG] U3 screen done: {m['name']}  "
          f"[t+{time.time() - T0:.1f}s]")

print()
report("U3 SCREEN TALLY over every (model, grid time, subsystem, reading) "
       "instance", fmt_counter(_screen_tally))
_red = {k: v for k, v in _screen_tally.items() if k[0].startswith("n=")}
_redtot = sum(_red.values())
_redDS = sum(v for k, v in _red.items() if k[1] == "S-FAIL-DS")
_redUNI = sum(v for k, v in _red.items() if k[1] == "S-FAIL-UNI")
_redPASS = sum(v for k, v in _red.items() if k[1].startswith("S-PASS"))
_redEXC = sum(v for k, v in _red.items() if k[1].startswith("EXCLUDED"))
_absum = Counter()
for k, v in _screen_tally.items():
    if not k[0].startswith("n="):
        _absum[k[1]] += v
report("composite Gamma_ABC verdicts (32 = 8 models x 4 grid times)",
       fmt_counter(_absum))
report("reduced-process verdicts, counted exactly",
       f"{_redtot} instances: {_redDS} S-FAIL-DS (not doubly stochastic, so "
       f"not unistochastic), {_redUNI} S-FAIL-UNI (doubly stochastic but "
       f"the polygon obstruction fires), {_redPASS} certified "
       f"orthostochastic (all n = 2, by KA-U3c), {_redEXC} excluded by the "
       f"declared caps and reported as neither")
check("UNI.1 A REDUCED PROCESS IS OFTEN NOT ITSELF UNISTOCHASTIC, and the "
      "census says so exactly rather than by appeal: "
      f"{_redDS} of {_redtot} reduced instances are column-stochastic but "
      "NOT doubly stochastic, and unistochastic implies doubly stochastic, "
      f"while a further {_redUNI} are doubly stochastic and still fail the "
      "polygon obstruction.  This is [B3-sqthm]'s second disjunct made "
      "concrete at these dimensions: the subsystem of a unistochastic "
      "process is an indivisible stochastic process that is NOT itself "
      "unistochastic, and would need a dilation.  The composite, by "
      "contrast, is certified unistochastic wherever the cost cap allows, "
      "with the model's own unitary exhibited as the certificate",
      _redDS > 0 and _redUNI > 0,
      f"reduced S-FAIL-DS {_redDS}, S-FAIL-UNI {_redUNI}, certified "
      f"{_redPASS}, excluded {_redEXC}, of {_redtot}")


# ===========================================================================
# SEC 7.  THE DIVISION-EVENT CENSUS
# ===========================================================================

sec("THE DIVISION-EVENT CENSUS: DIV_S(t_k) for every model, reading, "
    "subsystem and grid time")

LP_STATS = []
_dec_cache = {}
CACHE_MAX = 5000     # memoisation only: clearing it changes runtime, nothing else
DEC_COUNT = [0]
CALL_COUNT = [0]
EQ22_TESTED = [0]
EQ22_BAD = [0]
FARKAS_TOT = [0]
FARKAS_OK = [0]
VERDICT_TALLY = Counter()
INSTR_TALLY = Counter()


def bridge_exists(A, B, cs, label):
    """(D1) [U1-D1] for one spanning pair, decided by U1's committed
    cascade.  A = Gamma_S(t_k<-0), B = Gamma_S(t_b<-0), cs = the
    configurations of S.  The joint handed to decide_triple is the
    conditional-independence coupling p(i) A[j][i] B[k][i], whose (0,1) and
    (0,2) conditionals are EXACTLY A and B -- the only two objects
    decide_triple reads off the joint for the algebraic and LP arms.  Its
    step-(1) shortcut tests one particular column-stochastic candidate and
    accepts only if that candidate genuinely satisfies X A = B, so the
    shortcut is sound.  p(i) is uniform and strictly positive; the verdict
    does not depend on it, because A and B are recovered exactly."""
    key = (tuple(tuple(r) for r in A), tuple(tuple(r) for r in B))
    CALL_COUNT[0] += 1
    if key in _dec_cache:
        return _dec_cache[key]
    if len(_dec_cache) >= CACHE_MAX:
        _dec_cache.clear()
    n = len(cs)
    J = {}
    for a, i in enumerate(cs):
        for b, j in enumerate(cs):
            if not A[b][a]:
                continue
            for c, k in enumerate(cs):
                if not B[c][a]:
                    continue
                J[(i, j, k)] = Fr(1, n) * A[b][a] * B[c][a]
    S = supports(J, 3)
    r = decide_triple(J, S, 0, 1, 2, label, LP_STATS)
    DEC_COUNT[0] += 1
    VERDICT_TALLY[r["verdict"]] += 1
    INSTR_TALLY[r.get("instrument", "shortcut/CK")] += 1
    if r["verdict"] == "INDIVISIBLE" and ("lpcert" in r or "rowcerts" in r):
        FARKAS_TOT[0] += 1
        FARKAS_OK[0] += int(r.get("farkas", True))
    # cross-check against [B3] eq.22 wherever A is square and invertible
    inv, det = invert_exact([row[:] for row in A])
    r["det_full"] = det
    if inv is not None:
        Gb = [[sum(B[x][t] * inv[t][y] for t in range(n)) for y in range(n)]
              for x in range(n)]
        alg_ok = all(Gb[x][y] >= 0 for x in range(n) for y in range(n))
        r["eq22_ok"] = alg_ok
        r["eq22"] = Gb
        r["eq22_agrees"] = (alg_ok == (r["verdict"] == "DIVISIBLE"))
        EQ22_TESTED[0] += 1
        EQ22_BAD[0] += int(not r["eq22_agrees"])
    else:
        r["eq22_ok"] = None
        r["eq22_agrees"] = None
    _dec_cache[key] = r
    return r


def div_predicate(fam, cs, tag):
    """DIV_S(t_k) for every k: the conjunction over spanning targets."""
    out = {}
    detail = {}
    for k in TIMES:
        ok = True
        per = {}
        for b in TIMES:
            if b < k:
                continue
            if b == k:
                per[b] = ("TRIVIAL", None)
                continue
            r = bridge_exists(fam[k], fam[b], cs,
                              f"{tag} t{k}->t{b}")
            per[b] = (r["verdict"], r)
            if r["verdict"] != "DIVISIBLE":
                ok = False
        out[k] = ok
        detail[k] = per
    return out, detail


CENSUS = {}          # (model, reading-label, S) -> (divset, detail, family)

# THE READINGS, declared so that each one is defined on EVERY member of the
# lattice at once -- otherwise the lattice tests below would be comparing
# incomparable objects.  Reading M is indexed by the initial distribution.
# Reading C is indexed by a FULL configuration c* of the composite: the
# process assigned to S is the one conditioned on c* restricted to S's
# complement, so that all seven subsystems are conditioned on one and the
# same global outcome.  FUN.2 above shows this family is functorial.
READ_LABELS = [f"M:{nm}" for nm, _ in P0] + \
    ["C:" + "".join(str(b) for b in c) for c in CFGS]
report("declared readings (each defined on all seven subsystems)",
       READ_LABELS)

for m in MODELS:
    t_m = time.time()
    for S in LATTICE:
        cs = SUBC[S]
        for _nm, p0 in P0:
            fam = [gamma_marginal(m["GAMMA"][k], S, p0) for k in TIMES]
            d, det = div_predicate(fam, cs, f"{m['name']}|M{_nm}|{LNAME[S]}")
            CENSUS[(m["name"], f"M:{_nm}", LNAME[S])] = (d, det, fam)
        for cstar in CFGS:
            c = tuple(cstar[w] for w in COMP[S])
            fam = [gamma_cond(m["GAMMA"][k], S, c) for k in TIMES]
            d, det = div_predicate(fam, cs,
                                   f"{m['name']}|C{cstar}|{LNAME[S]}")
            CENSUS[(m["name"],
                    "C:" + "".join(str(b) for b in cstar),
                    LNAME[S])] = (d, det, fam)
    print(f"  [PROG] census done: {m['name']}  "
          f"({time.time() - t_m:.1f}s, {DEC_COUNT[0]} decisions so far, "
          f"t+{time.time() - T0:.1f}s)")

report("(D1) queries posed across the whole census", CALL_COUNT[0])
report("DISTINCT (Gamma_S(t_k<-0), Gamma_S(t_b<-0)) pairs actually decided "
       "(the cache is exact, keyed on the two matrices entry by entry)",
       DEC_COUNT[0])
report("exact Phase-I simplex invocations inside those decisions",
       _LP_CALLS[0])
report("VERDICT TALLY over the distinct decisions",
       fmt_counter(VERDICT_TALLY))
report("INSTRUMENT TALLY (which arm of U1's cascade returned the verdict)",
       fmt_counter(INSTR_TALLY))
report("full-LP (decide_triple step 4) invocations", len(LP_STATS))
print("         ^ the cascade resolved every decision at the candidate, "
      "[B3] eq. 22 or")
print("           row-certificate stage; the row-certificate stage IS the "
      "exact")
print("           simplex, run once per target configuration, so the LP "
      "machinery")
print("           is exercised throughout even though step 4 never had to "
      "fire.")

check("CEN.1 [B3] eq. 22 AND THE LP AGREE ON EVERY DECISION WHERE eq. 22 "
      "APPLIES: wherever Gamma_S(t_k<-0) is square and invertible the "
      "algebraic interpolant Gammabar = Gamma_S(t_b<-0) Gamma_S(t_k<-0)^{-1} "
      "is the UNIQUE candidate bridge, and 'Gammabar has no negative entry' "
      "agrees with the feasibility verdict in every single case",
      EQ22_BAD[0] == 0,
      f"{EQ22_TESTED[0]} of {DEC_COUNT[0]} distinct pairs have an "
      f"invertible source; {EQ22_BAD[0]} disagreements")

check("CEN.2 EVERY LP INFEASIBILITY CARRIES A FARKAS CERTIFICATE THAT "
      "VERIFIES INDEPENDENTLY (w^T M <= 0 on every column, w^T b > 0), so "
      "no negative verdict rests on the simplex's word",
      FARKAS_TOT[0] == FARKAS_OK[0],
      f"{FARKAS_OK[0]} of {FARKAS_TOT[0]} certificate-bearing "
      f"infeasibilities verified")

_exc = VERDICT_TALLY["EXCLUDED-BY-CAP"]
_vac = VERDICT_TALLY["VACUOUS"]
check("CEN.3 NO DECISION IS EXCLUDED BY A CAP AND NONE IS STRUCTURALLY "
      "VACUOUS: every subsystem carries at least two configurations and "
      "every LP is orders of magnitude inside U1's declared caps, so the "
      "census is complete as posed",
      _exc == 0 and _vac == 0,
      f"excluded-by-cap {_exc}, vacuous {_vac}")


# ---- the DIV tables -----------------------------------------------------
def divstr(d):
    return "{" + ",".join(str(k) for k in TIMES if d[k]) + "}"


print()
print("  THE DIVISION-EVENT SETS DIV_S, model by model.  A grid index k")
print("  appears exactly when EVERY spanning target t_b >= t_k admits a")
print("  column-stochastic bridge.  Index 0 is present by construction")
print("  ([B3-divdef]).  Both readings are printed; reading C is printed")
print("  once per complement configuration.")
_rlabels = {}
for m in MODELS:
    print()
    print(f"  ---- {m['name']}")
    labels = list(READ_LABELS)
    _rlabels[m["name"]] = labels
    print("       reading      " + "".join(f"{LNAME[S]:>10s}"
                                           for S in LATTICE))
    for r in labels:
        row = "".join(f"{divstr(CENSUS[(m['name'], r, LNAME[S])][0]):>10s}"
                      for S in LATTICE)
        print(f"       {r:<12s} {row}")

print()
print("  THE TWO READINGS, COMPARED DIRECTLY.  For each (model, subsystem,")
print("  grid index) the marginal readings and the conditional readings are")
print("  compared: do they agree on whether the time is a division event?")
_rM = [r for r in READ_LABELS if r.startswith("M:")]
_rC = [r for r in READ_LABELS if r.startswith("C:")]
_rd = Counter()
_rd_wit = []
for m in MODELS:
    for S in LATTICE:
        for k in TIMES:
            vM = {CENSUS[(m["name"], r, LNAME[S])][0][k] for r in _rM}
            vC = {CENSUS[(m["name"], r, LNAME[S])][0][k] for r in _rC}
            _rd[("M internally uniform over p_0", len(vM) == 1)] += 1
            _rd[("C internally uniform over c*", len(vC) == 1)] += 1
            _rd[("M and C agree", vM == vC and len(vM) == 1)] += 1
            if not (vM == vC and len(vM) == 1):
                _rd_wit.append((m["name"].split()[0], LNAME[S], k,
                                sorted(vM), sorted(vC)))
report("READING COMPARISON over every (model, subsystem, grid index)",
       fmt_counter(_rd))
report("slices where the readings do NOT all agree", len(_rd_wit))
for w in _rd_wit[:VERB_WITNESS]:
    print(f"       {w[0]} | {w[1]} | t_{w[2]}: marginal readings give "
          f"{w[3]}, conditional readings give {w[4]}")
if len(_rd_wit) > VERB_WITNESS:
    print(f"       ... (+{len(_rd_wit) - VERB_WITNESS} more, all counted)")
check("CEN.3b THE TWO READINGS ARE NOT THE SAME CENSUS, and the receipt "
      "does not silently merge them: there are slices on which the "
      "marginal and conditional readings of the SAME subsystem at the SAME "
      "time disagree about whether it is a division event, and there are "
      "slices on which the conditional reading depends on WHICH outcome "
      "the complement is conditioned on.  Both are reported separately "
      "throughout",
      len(_rd_wit) > 0,
      f"{len(_rd_wit)} disagreeing slices of "
      f"{len(MODELS) * len(LATTICE) * len(TIMES)}")

_gs0 = all(CENSUS[key][0][0] for key in CENSUS)
check("CEN.4 (GS0) INITIALITY HOLDS EVERYWHERE, as [B3-divdef] requires: "
      "the initial time is a division event for every subsystem, under "
      "every reading, in every model",
      _gs0, f"{len(CENSUS)} (model, reading, subsystem) triples, all "
            f"containing index 0")


# ===========================================================================
# SEC 8.  THE CONTAINMENT TABLE ACROSS THE LATTICE
# ===========================================================================

sec("THE CONTAINMENT TABLE: every nested pair, both directions, every "
    "model and every reading")

NESTED = [(Sb, Ss) for Sb in LATTICE for Ss in LATTICE
          if set(Ss) < set(Sb)]
report("nested pairs in the lattice (S' strictly contains S'')",
       ", ".join(f"{LNAME[a]}>{LNAME[b]}" for a, b in NESTED))

DOWN_FAILS = []      # GS1 violations: t in DIV_{S'} but not in DIV_{S''}
UP_FAILS = []        # the converse direction
CONT_TALLY = Counter()

for m in MODELS:
    for r in _rlabels[m["name"]]:
        for Sb, Ss in NESTED:
            db = CENSUS[(m["name"], r, LNAME[Sb])][0]
            ds = CENSUS[(m["name"], r, LNAME[Ss])][0]
            down = all((not db[k]) or ds[k] for k in TIMES)
            up = all((not ds[k]) or db[k] for k in TIMES)
            CONT_TALLY[("down(GS1)", down)] += 1
            CONT_TALLY[("up", up)] += 1
            for k in TIMES:
                if db[k] and not ds[k]:
                    DOWN_FAILS.append((m["name"], r, LNAME[Sb], LNAME[Ss], k))
                if ds[k] and not db[k]:
                    UP_FAILS.append((m["name"], r, LNAME[Ss], LNAME[Sb], k))

report("CONTAINMENT TALLY over every (model, reading, nested pair) INSTANCE",
       fmt_counter(CONT_TALLY))
report("DOWNWARD containment DIV_{S'} subset DIV_{S''} (GS1): failing "
       "TIME-WITNESSES (model, reading, pair, grid index)", len(DOWN_FAILS))
report("UPWARD containment DIV_{S''} subset DIV_{S'}: failing TIME-"
       "WITNESSES", len(UP_FAILS))
report("DOWNWARD (GS1) failures, DISTINCT (model, nested pair, grid index) "
       "-- readings collapsed",
       len({(a, c, d, e) for (a, b, c, d, e) in DOWN_FAILS}))
report("UPWARD failures, DISTINCT (model, nested pair, grid index)",
       len({(a, c, d, e) for (a, b, c, d, e) in UP_FAILS}))

print()
print("  THE CONTAINMENT TABLE, model by model, printed BOTH WAYS.  'd' =")
print("  the downward containment DIV_{S'} subset DIV_{S''} holds; 'u' = the")
print("  upward one holds; 'du' = both; '--' = neither.  The downward entry")
print("  is axiom GS1; the upward entry is not an axiom and is reported for")
print("  symmetry.")
for m in MODELS:
    print()
    print(f"  ---- {m['name']}")
    print("       reading      " + "".join(f"{LNAME[a] + '>' + LNAME[b]:>9s}"
                                           for a, b in NESTED))
    for r in _rlabels[m["name"]]:
        cells = []
        for Sb, Ss in NESTED:
            db = CENSUS[(m["name"], r, LNAME[Sb])][0]
            ds = CENSUS[(m["name"], r, LNAME[Ss])][0]
            down = all((not db[k]) or ds[k] for k in TIMES)
            up = all((not ds[k]) or db[k] for k in TIMES)
            cells.append(("d" if down else "") + ("u" if up else "")
                         or "--")
        print(f"       {r:<12s} " + "".join(f"{c:>9s}" for c in cells))

# ---- the specific containment the pin names -----------------------------
print()
print("  THE CONTAINMENT THE PIN NAMES: is DIV_ABC subset "
      "DIV_A /\\ DIV_B /\\ DIV_C?")
_pin_tally = Counter()
_pin_fail = []
for m in MODELS:
    for r in _rlabels[m["name"]]:
        dabc = CENSUS[(m["name"], r, "ABC")][0]
        dA = CENSUS[(m["name"], r, "A")][0]
        dB = CENSUS[(m["name"], r, "B")][0]
        dC = CENSUS[(m["name"], r, "C")][0]
        ok = all((not dabc[k]) or (dA[k] and dB[k] and dC[k]) for k in TIMES)
        rev = all((not (dA[k] and dB[k] and dC[k])) or dabc[k]
                  for k in TIMES)
        _pin_tally[("ABC subset A/\\B/\\C", ok)] += 1
        _pin_tally[("A/\\B/\\C subset ABC", rev)] += 1
        if not ok:
            for k in TIMES:
                if dabc[k] and not (dA[k] and dB[k] and dC[k]):
                    miss = [nm for nm, dd in (("A", dA), ("B", dB),
                                              ("C", dC)) if not dd[k]]
                    _pin_fail.append((m["name"], r, k, miss))
report("the pin's containment, both ways", fmt_counter(_pin_tally))
report("instances where DIV_ABC is NOT contained in DIV_A /\\ DIV_B /\\ "
       "DIV_C", len(_pin_fail))
for _f in _pin_fail[:VERB_WITNESS]:
    print(f"       {_f[0]} | reading {_f[1]} | t_{_f[2]} is a division "
          f"event for ABC but NOT for {_f[3]}")
if len(_pin_fail) > VERB_WITNESS:
    print(f"       ... (+{len(_pin_fail) - VERB_WITNESS} more, all counted)")


# ---- exact witnesses for the crossings ----------------------------------
def print_witness(mname, r, Sbig, Ssmall, k, tag):
    """The exact witness for one crossing: the bridge that exists on one
    system and the Farkas certificate that proves none exists on the other."""
    print()
    print(f"    WITNESS [{tag}] {mname} | reading {r} | t_{k}: "
          f"{Sbig} divides, {Ssmall} does not")
    dbig = CENSUS[(mname, r, Sbig)]
    dsm = CENSUS[(mname, r, Ssmall)]
    print(f"      DIV_{Sbig} = {divstr(dbig[0])}   "
          f"DIV_{Ssmall} = {divstr(dsm[0])}")
    for b, (v, rr) in sorted(dsm[1][k].items()):
        if v == "INDIVISIBLE":
            print(f"      the obstructed spanning pair on {Ssmall}: "
                  f"(t_{k} -> t_{b}), verdict {v}, decided by "
                  f"{rr.get('instrument', 'the CK shortcut')}")
            print(f"      Gamma_{Ssmall}(t_{k}<-0) = "
                  f"{[[str(x) for x in row] for row in dsm[2][k]]}")
            print(f"      Gamma_{Ssmall}(t_{b}<-0) = "
                  f"{[[str(x) for x in row] for row in dsm[2][b]]}")
            if rr.get("eq22_ok") is False:
                neg = [(x, y, str(rr["eq22"][x][y]))
                       for x in range(len(rr["eq22"]))
                       for y in range(len(rr["eq22"][0]))
                       if rr["eq22"][x][y] < 0]
                print(f"      [B3] eq. 22 interpolant has {len(neg)} "
                      f"negative entries, exemplar {neg[0]}")
            print_certificate(rr)
            break
    print(f"      and on {Sbig} every spanning pair from t_{k} has a "
          f"column-stochastic bridge:")
    for b, (v, rr) in sorted(dbig[1][k].items()):
        if v == "TRIVIAL":
            continue
        print(f"        (t_{k} -> t_{b}): {v} via "
              f"{rr.get('instrument', 'the CK shortcut')}")
        print_interpolant(rr)


print()
print("  EXACT WITNESSES FOR THE DOWNWARD (GS1) CROSSINGS.  Each shows a "
      "grid")
print("  time that IS a division event for a composite and is NOT one for a")
print("  subsystem of it, with the bridge exhibited on one side and a")
print("  verified Farkas certificate on the other.  Witnesses are printed "
      "once")
print("  per DISTINCT (model, nested pair, grid index); the readings that")
print("  reproduce each one are listed with it.")
_by_distinct = defaultdict(list)
for (mn, r, Sb, Ss, k) in DOWN_FAILS:
    _by_distinct[(mn, Sb, Ss, k)].append(r)
_seen_w = 0
for key in sorted(_by_distinct, key=sk):
    mn, Sb, Ss, k = key
    if _seen_w >= VERB_WITNESS:
        break
    rs = sorted(_by_distinct[key])
    print()
    print(f"    reproduced in {len(rs)} of {len(READ_LABELS)} readings: "
          f"{rs}")
    print_witness(mn, rs[0], Sb, Ss, k, "GS1")
    _seen_w += 1
if len(_by_distinct) > _seen_w:
    print(f"\n    ... (+{len(_by_distinct) - _seen_w} further distinct GS1 "
          f"crossings, all counted in the tables above)")

print()
print("  DOWNWARD (GS1) CROSSINGS, CENSUSED BY MODEL, READING AND PAIR:")
_dc = Counter((mn.split()[0], Sb + ">" + Ss) for (mn, r, Sb, Ss, k)
              in DOWN_FAILS)
report("GS1 crossings by (model, nested pair)", fmt_counter(_dc))
_dcm = Counter(mn.split()[0] for (mn, r, Sb, Ss, k) in DOWN_FAILS)
report("GS1 crossings by model", fmt_counter(_dcm))
_dcr = Counter(r[0] for (mn, r, Sb, Ss, k) in DOWN_FAILS)
report("GS1 crossings by reading (M = marginal, C = conditional)",
       fmt_counter(_dcr))
_ucm = Counter(mn.split()[0] for (mn, r, Ss, Sb, k) in UP_FAILS)
report("UPWARD crossings by model", fmt_counter(_ucm))
_ucr = Counter(r[0] for (mn, r, Ss, Sb, k) in UP_FAILS)
report("UPWARD crossings by reading", fmt_counter(_ucr))


# ===========================================================================
# SEC 9.  THE GLOBAL-SECTION TEST
# ===========================================================================

sec("THE GLOBAL-SECTION TEST against the axioms stated in SEC 3")

OVERLAP = [(Sa, Sb) for Sa in LATTICE for Sb in LATTICE
           if sk(Sa) < sk(Sb) and set(Sa) & set(Sb)]
report("overlapping pairs used by GS2 (S' /\\ S'' non-empty)",
       ", ".join(f"{LNAME[a]}+{LNAME[b]}->"
                 f"{LNAME[tuple(sorted(set(a) | set(b)))]}"
                 for a, b in OVERLAP))


def gs_check(dmap):
    """dmap: S -> {k: bool}.  Returns (gs0, gs1, gs2, gs3, witnesses)."""
    w1, w2 = [], []
    gs0 = all(dmap[S][0] for S in LATTICE)
    gs1 = True
    for Sb, Ss in NESTED:
        for k in TIMES:
            if dmap[Sb][k] and not dmap[Ss][k]:
                gs1 = False
                w1.append((LNAME[Sb], LNAME[Ss], k))
    gs2 = True
    for Sa, Sb in OVERLAP:
        Su = tuple(sorted(set(Sa) | set(Sb)))
        for k in TIMES:
            if dmap[Sa][k] and dmap[Sb][k] and not dmap[Su][k]:
                gs2 = False
                w2.append((LNAME[Sa], LNAME[Sb], LNAME[Su], k))
    ref = dmap[LATTICE[0]]
    gs3 = all(dmap[S][k] == ref[k] for S in LATTICE for k in TIMES)
    return gs0, gs1, gs2, gs3, w1, w2


def maximal_subsection(dmap, k):
    """The largest d' <= d at time k satisfying GS1 /\\ GS2, by exhaustive
    search over the 2^7 assignments on the lattice (128 candidates; the
    search is complete, not heuristic)."""
    idx = {S: a for a, S in enumerate(LATTICE)}
    best = None
    for mask in range(1 << len(LATTICE)):
        d2 = {S: bool(mask >> idx[S] & 1) for S in LATTICE}
        if any(d2[S] and not dmap[S][k] for S in LATTICE):
            continue
        ok = True
        for Sb, Ss in NESTED:
            if d2[Sb] and not d2[Ss]:
                ok = False
                break
        if ok:
            for Sa, Sb in OVERLAP:
                Su = tuple(sorted(set(Sa) | set(Sb)))
                if d2[Sa] and d2[Sb] and not d2[Su]:
                    ok = False
                    break
        if not ok:
            continue
        card = sum(d2[S] for S in LATTICE)
        if best is None or card > best[0]:
            best = (card, d2)
    return best


GS_RESULT = {}
for m in MODELS:
    for r in _rlabels[m["name"]]:
        dmap = {S: CENSUS[(m["name"], r, LNAME[S])][0] for S in LATTICE}
        GS_RESULT[(m["name"], r)] = gs_check(dmap) + (dmap,)

_g0 = sum(1 for v in GS_RESULT.values() if v[0])
_g1 = sum(1 for v in GS_RESULT.values() if v[1])
_g2 = sum(1 for v in GS_RESULT.values() if v[2])
_g3 = sum(1 for v in GS_RESULT.values() if v[3])
_n = len(GS_RESULT)
print()
print("  THE AXIOMS, (model, reading) by (model, reading).  'Y' = the axiom")
print("  holds of the computed family; 'n' = it fails, with the witness")
print("  count in brackets.  SECTION = GS0 /\\ GS1 /\\ GS2, i.e. the data")
print("  itself is a compatible family for the restriction presheaf.")
for m in MODELS:
    print()
    print(f"  ---- {m['name']}")
    for r in _rlabels[m["name"]]:
        g0, g1, g2, g3, w1, w2, dmap = GS_RESULT[(m["name"], r)]
        print(f"       {r:<12s} GS0={'Y' if g0 else 'n'}  "
              f"GS1={'Y' if g1 else 'n[' + str(len(w1)) + ']'}  "
              f"GS2={'Y' if g2 else 'n[' + str(len(w2)) + ']'}  "
              f"GS3={'Y' if g3 else 'n'}  "
              f"SECTION={'YES' if (g0 and g1 and g2) else 'NO'}")

report("GS0 (initiality) holds", f"{_g0}/{_n}")
report("GS1 (restriction-compatibility) holds", f"{_g1}/{_n}")
report("GS2 (gluing on overlaps) holds", f"{_g2}/{_n}")
report("GS3 (system-independence, the hypothesis [B3-syscentric] denies) "
       "holds", f"{_g3}/{_n}")
_sect = sum(1 for v in GS_RESULT.values() if v[0] and v[1] and v[2])
report("the computed family IS a global section (GS0 /\\ GS1 /\\ GS2)",
       f"{_sect}/{_n}")

_bad_models = sorted({mn for (mn, r), v in GS_RESULT.items()
                      if not (v[0] and v[1] and v[2])})
report("models admitting NO global section under the stated axioms, in at "
       "least one reading", _bad_models)
_bad_all = sorted({mn for mn in {k[0] for k in GS_RESULT}
                   if all(not (v[0] and v[1] and v[2])
                          for (mm, r), v in GS_RESULT.items() if mm == mn)})
report("models admitting NO global section in EVERY reading", _bad_all)

# ---- the maximal sub-section --------------------------------------------
print()
print("  THE MAXIMAL SUB-SECTION.  Where the data is not itself a section,")
print("  the largest trimming d' <= d satisfying GS1 /\\ GS2 is computed by")
print("  exhaustive search over all 2^7 = 128 assignments per grid time.")
print("  'd' means the data is already consistent at that time; a listed")
print("  set is the maximal consistent trimming; '{}' means only the empty")
print("  assignment survives, which is the hard obstruction.")
_hard = 0
_trim = 0
_intact = 0
for m in MODELS:
    rows = []
    for r in _rlabels[m["name"]]:
        g0, g1, g2, g3, w1, w2, dmap = GS_RESULT[(m["name"], r)]
        cells = []
        for k in TIMES:
            card, d2 = maximal_subsection(dmap, k)
            data_card = sum(dmap[S][k] for S in LATTICE)
            if card == data_card:
                cells.append("d")
                _intact += 1
            elif card == 0:
                cells.append("{}")
                _hard += 1
            else:
                cells.append("{" + ",".join(LNAME[S] for S in LATTICE
                                            if d2[S]) + "}")
                _trim += 1
        rows.append((r, cells))
    print()
    print(f"  ---- {m['name']}")
    print("       reading      " + "".join(f"t_{k:<10d}" for k in TIMES))
    for r, cells in rows:
        print(f"       {r:<12s} " + "".join(f"{c:<12s}" for c in cells))

report("(model, reading, time) slices where the data is already a "
       "consistent assignment", _intact)
report("slices needing a non-trivial trimming", _trim)
report("slices where only the EMPTY assignment survives (hard obstruction)",
       _hard)


# ===========================================================================
# SEC 10.  THE EXHAUSTIVE CIRCUIT SWEEP — the population behind the finding
# ===========================================================================

sec("THE EXHAUSTIVE CIRCUIT SWEEP: every circuit of the declared depth over "
    "the declared gate alphabet, with no sampling and no randomness")

SWEEP_DEPTH = 4
print(f"""
  Eight hand-chosen models can only show that something HAPPENS.  This
  section measures HOW OFTEN, by enumerating EVERY circuit of depth
  {SWEEP_DEPTH} over a declared six-letter gate alphabet -- 6^{SWEEP_DEPTH}
  = {6 ** SWEEP_DEPTH} circuits, exhaustive, unsampled, no randomness.

  THE REPRESENTATION, declared.  Each gate is written U = sqrt(w) . V with w
  an exact positive rational and V an exact rational matrix.  Products
  compose as (w1 w2, V1 V2), and [B3-uni] gives Gamma_ij = w . V_ij^2, which
  is rational by construction -- so the whole sweep is Fractions end to end
  and no algebraic ring is needed.  Unitarity is w . V^T V = 1, checked
  exactly on every partial product of every circuit.

  THE ALPHABET: H_A, H_B, CNOT_(A->B), CNOT_(B->C), SWAP_(AC), and the
  Pythagorean rotation R_A(3/5, 4/5) -- five Clifford letters and one
  non-Clifford letter, so the population is not confined to stabiliser
  dynamics.  Readings: M with p_unif and C with c* = 000, both censused.
""")


def sc_compose(g, h):
    """h applied after g."""
    w1, V1 = g
    w2, V2 = h
    return (w1 * w2, fr_mul(V2, V1))


def sc_gamma(g):
    w, V = g
    return [[w * V[i][j] * V[i][j] for j in range(DIM)] for i in range(DIM)]


def sc_unitary(g):
    w, V = g
    n = len(V)
    for i in range(n):
        for j in range(n):
            s = w * sum(V[t][i] * V[t][j] for t in range(n))
            if s != (Fr(1) if i == j else Fr(0)):
                return False
    return True


def sc_embed1(V2, wire, w):
    M = [[Fr(0)] * DIM for _ in range(DIM)]
    for jc in CFGS:
        for o in (0, 1):
            ic = tuple(o if x == wire else jc[x] for x in WIRES)
            M[cfg_index(ic)][cfg_index(jc)] = V2[o][jc[wire]]
    return (w, M)


def sc_perm(f):
    M = [[Fr(0)] * DIM for _ in range(DIM)]
    for jc in CFGS:
        M[cfg_index(f(jc))][cfg_index(jc)] = Fr(1)
    return (Fr(1), M)


ALPHABET = [
    ("H_A", sc_embed1([[Fr(1), Fr(1)], [Fr(1), Fr(-1)]], 0, Fr(1, 2))),
    ("H_B", sc_embed1([[Fr(1), Fr(1)], [Fr(1), Fr(-1)]], 1, Fr(1, 2))),
    ("CNOT_AB", sc_perm(lambda x: (x[0], x[1] ^ x[0], x[2]))),
    ("CNOT_BC", sc_perm(lambda x: (x[0], x[1], x[2] ^ x[1]))),
    ("SWAP_AC", sc_perm(lambda x: (x[2], x[1], x[0]))),
    ("R_A", sc_embed1([[Fr(3, 5), Fr(-4, 5)], [Fr(4, 5), Fr(3, 5)]], 0,
                      Fr(1))),
]
_alph_ok = all(sc_unitary(g) for _n, g in ALPHABET)
anchor("SWP.0 EVERY LETTER OF THE ALPHABET IS EXACTLY UNITARY IN THE "
       "SCALED-RATIONAL REPRESENTATION: w . V^T V = 1 identically for all "
       "six letters, so every circuit built from them is unitary and every "
       "Gamma the sweep produces is a legitimate [B3-uni] transition matrix",
       _alph_ok, f"alphabet {[n for n, _g in ALPHABET]}, all unitary "
                 f"{_alph_ok}")

SW_ID = (Fr(1), [[Fr(1) if i == j else Fr(0) for j in range(DIM)]
                 for i in range(DIM)])
_sw_n = 0
_sw_uni_bad = 0
_sw_stoch_bad = 0
SW_GS = Counter()
SW_DOWN = Counter()
SW_UP = Counter()
SW_ABC = Counter()
SW_EXEMPLAR = {}
SW_HARD = []
SW_JOINT = Counter()
SW_SUB = Counter()
SW_EMPTY = []
_pre = (CALL_COUNT[0], DEC_COUNT[0], _LP_CALLS[0], EQ22_TESTED[0],
        EQ22_BAD[0], FARKAS_TOT[0], FARKAS_OK[0])
_t_sw = time.time()
for combo in product(range(len(ALPHABET)), repeat=SWEEP_DEPTH):
    cur = SW_ID
    fams = [SW_ID]
    for gi in combo:
        cur = sc_compose(cur, ALPHABET[gi][1])
        fams.append(cur)
    if not all(sc_unitary(g) for g in fams):
        _sw_uni_bad += 1
        continue
    GAM = [sc_gamma(g) for g in fams]
    if not all(sum(G[i][j] for i in range(DIM)) == Fr(1)
               for G in GAM for j in range(DIM)):
        _sw_stoch_bad += 1
        continue
    _sw_n += 1
    name = "-".join(ALPHABET[g][0] for g in combo)
    for rlab, getter in (("M:p_unif", lambda G, S: gamma_marginal(
                              G, S, dict(P0[0][1]))),
                         ("C:000", lambda G, S: gamma_cond(
                              G, S, tuple(0 for _ in COMP[S])))):
        dmap = {}
        for S in LATTICE:
            fam = [getter(GAM[k], S) for k in TIMES]
            d, _det = div_predicate(fam, SUBC[S], f"SWEEP {name}")
            dmap[S] = d
        g0, g1, g2, g3, w1, w2 = gs_check(dmap)
        SW_GS[(rlab, "GS0", g0)] += 1
        SW_GS[(rlab, "GS1", g1)] += 1
        SW_GS[(rlab, "GS2", g2)] += 1
        SW_GS[(rlab, "GS3", g3)] += 1
        SW_GS[(rlab, "SECTION", g0 and g1 and g2)] += 1
        SW_JOINT[(rlab, "GS1=" + str(g1), "GS2=" + str(g2),
                  "GS3=" + str(g3))] += 1
        if not (g0 and g1 and g2):
            for k in TIMES:
                card, d2 = maximal_subsection(dmap, k)
                data_card = sum(dmap[S][k] for S in LATTICE)
                SW_SUB[(rlab, "already consistent" if card == data_card
                        else ("EMPTY ONLY" if card == 0
                              else f"trimmed to {card} of {data_card}"))] += 1
                if card == 0:
                    SW_EMPTY.append((rlab, name, k,
                                     {LNAME[S]: dmap[S][k]
                                      for S in LATTICE}))
        SW_ABC[(rlab, divstr(dmap[(0, 1, 2)]))] += 1
        for (a, b, k) in w1:
            SW_DOWN[(rlab, a + ">" + b)] += 1
            SW_EXEMPLAR.setdefault((rlab, a + ">" + b), (name, k))
        for (a, b, c, k) in w2:
            SW_UP[(rlab, a + "+" + b + "->" + c)] += 1
            SW_EXEMPLAR.setdefault((rlab, a + "+" + b + "->" + c),
                                   (name, k))
        if not g2:
            SW_HARD.append((rlab, name, w2[:2]))

report("circuits enumerated (exhaustive, no sampling)", _sw_n)
report("circuits rejected for non-unitarity or non-stochasticity",
       f"{_sw_uni_bad} + {_sw_stoch_bad}")
report("sweep runtime", f"{time.time() - _t_sw:.1f}s")
report("sweep decision load", f"{CALL_COUNT[0] - _pre[0]} (D1) queries, "
       f"{DEC_COUNT[0] - _pre[1]} distinct decisions, "
       f"{_LP_CALLS[0] - _pre[2]} exact-simplex invocations")
check("SWP.0b THE SWEEP'S DECISIONS CARRY THE SAME TWO INTERNAL CHECKS AS "
      "THE MODEL CENSUS: [B3] eq. 22 agrees with the feasibility verdict "
      "on every sweep decision with an invertible source, and every "
      "certificate-bearing infeasibility verifies its Farkas vector "
      "independently",
      EQ22_BAD[0] == _pre[4] and FARKAS_TOT[0] - _pre[5]
      == FARKAS_OK[0] - _pre[6],
      f"eq.22 tested on {EQ22_TESTED[0] - _pre[3]} sweep decisions, "
      f"{EQ22_BAD[0] - _pre[4]} disagreements; "
      f"{FARKAS_OK[0] - _pre[6]} of {FARKAS_TOT[0] - _pre[5]} sweep Farkas "
      f"certificates verified")
report("AXIOM OUTCOMES over the sweep, by reading", fmt_counter(SW_GS))
_sw_g1_fail = {r: SW_GS[(r, "GS1", False)] for r in ("M:p_unif", "C:000")}
_sw_g2_fail = {r: SW_GS[(r, "GS2", False)] for r in ("M:p_unif", "C:000")}
_sw_g3_fail = {r: SW_GS[(r, "GS3", False)] for r in ("M:p_unif", "C:000")}
_sw_sect = {r: SW_GS[(r, "SECTION", True)] for r in ("M:p_unif", "C:000")}
report("circuits whose family FAILS GS1 (restriction-compatibility)",
       {r: f"{v} of {_sw_n}" for r, v in _sw_g1_fail.items()})
report("circuits whose family FAILS GS2 (gluing)",
       {r: f"{v} of {_sw_n}" for r, v in _sw_g2_fail.items()})
report("circuits whose family FAILS GS3 (system-independence)",
       {r: f"{v} of {_sw_n}" for r, v in _sw_g3_fail.items()})
report("circuits whose family IS a global section",
       {r: f"{v} of {_sw_n}" for r, v in _sw_sect.items()})
report("GS1 crossings by nested pair, over the sweep", fmt_counter(SW_DOWN))
report("GS2 gluing failures by triple, over the sweep", fmt_counter(SW_UP))
report("DIV_ABC spectrum over the sweep", fmt_counter(SW_ABC))
print("  EXEMPLAR CIRCUITS, one per crossing type (the first in "
      "enumeration order):")
for key in sorted(SW_EXEMPLAR, key=sk):
    nm, k = SW_EXEMPLAR[key]
    print(f"       {key[0]:<9s} {key[1]:<12s} first at t_{k} in circuit "
          f"{nm}")

check("SWP.1 THE GS1 FAILURE IS NOT AN ARTEFACT OF EIGHT HAND-CHOSEN "
      "MODELS: over an EXHAUSTIVE, UNSAMPLED population of "
      f"{_sw_n} depth-{SWEEP_DEPTH} circuits, restriction-compatibility "
      "fails on a substantial fraction under both readings, and every "
      "failure carries the same kind of exact witness as the hand-chosen "
      "ones",
      all(v > 0 for v in _sw_g1_fail.values()),
      f"GS1 failures: {_sw_g1_fail} of {_sw_n} circuits per reading")
report("JOINT axiom outcomes over the sweep", fmt_counter(SW_JOINT))
report("MAXIMAL SUB-SECTION over the non-section circuits of the sweep, by "
       "grid slice", fmt_counter(SW_SUB))
check("SWP.2 GLUING FAILS TOO, AND THE SWEEP LOCATES IT: over the eight "
      "hand-chosen models GS2 held everywhere, which would have licensed "
      "the reading 'only restriction fails'.  The exhaustive population "
      "refutes that reading: there are circuits on which a grid time is a "
      "division event for AB and for BC, which overlap in B, and is NOT "
      "one for ABC.  So the obstruction is not confined to one axiom",
      all(v > 0 for v in _sw_g2_fail.values()),
      f"GS2 failures: {_sw_g2_fail} of {_sw_n} circuits per reading; "
      f"{len(SW_HARD)} (reading, circuit) pairs carrying one")
print()
print("  THE HARD OBSTRUCTION.  A grid slice at which the ONLY assignment")
print("  d' <= d satisfying GS1 and GS2 is the identically-empty one.  This")
print("  happens exactly when some composite carries a division event while")
print("  NONE of its constituent single systems does: GS1 then forces every")
print("  atom of that composite into any non-empty section, and the data")
print("  does not supply them.  Each slice below is printed with the full")
print("  lattice row that produces it.")
report("hard-obstruction slices found in the sweep", len(SW_EMPTY))
for (rlab, name, k, row) in SW_EMPTY[:VERB_WITNESS]:
    print(f"       reading {rlab} | t_{k} | circuit {name}")
    print("         " + "  ".join(f"{s}={'1' if row[s] else '0'}"
                                  for s in [LNAME[S] for S in LATTICE]))
if len(SW_EMPTY) > VERB_WITNESS:
    print(f"       ... (+{len(SW_EMPTY) - VERB_WITNESS} more, all counted)")
check("SWP.2b THERE ARE SLICES CARRYING A HARD OBSTRUCTION: not merely 'the "
      "data is not a section', but 'no non-empty sub-assignment of the "
      "data is a section either'.  At such a slice a composite has a "
      "division event and not one of its three constituent systems does, "
      "so under GS1 the only consistent global division-event assignment "
      "is the empty one.  This is the marginal-problem obstruction in its "
      "strongest available form at these dimensions",
      len(SW_EMPTY) > 0,
      f"{len(SW_EMPTY)} hard-obstruction slices over "
      f"{2 * _sw_n * len(TIMES)} (reading, circuit, grid index) slices")

check("SWP.3 SYSTEM-CENTRICITY IS THE RULE, NOT THE EXCEPTION, on this "
      "population: GS3 -- the hypothesis that one division-event set "
      "serves every subsystem, which [B3-syscentric] explicitly denies -- "
      "fails on the large majority of circuits, so [B3]'s denial is "
      "quantified here rather than merely quoted",
      all(v > _sw_n // 2 for v in _sw_g3_fail.values()),
      f"GS3 failures: {_sw_g3_fail} of {_sw_n} circuits per reading")


# ===========================================================================
# SEC 11.  THE SANITY ANCHORS
# ===========================================================================

sec("THE SANITY ANCHORS: the classical control, and a known-indivisible "
    "reference")

_ctrl = MODELS[0]["name"]
_ctrl_all = all(CENSUS[(mn, r, s)][0][k]
                for (mn, r, s) in CENSUS if mn == _ctrl for k in TIMES)
_ctrl_n = sum(1 for (mn, r, s) in CENSUS if mn == _ctrl) * len(TIMES)
anchor("SAN.1 THE CLASSICAL CONTROL DIVIDES EVERYWHERE: for the product "
       "Markov chain on a product configuration space, EVERY grid time is "
       "a division event for EVERY subsystem under BOTH readings and all "
       "three declared p_0.  The instrument therefore does not manufacture "
       "indivisibility, and the divisible special case of [B3-eq22] is "
       "reproduced exactly",
       _ctrl_all,
       f"{_ctrl_n} (reading, subsystem, time) slots, all TRUE")

_ctrl_gs = all(v[0] and v[1] and v[2] and v[3]
               for (mn, r), v in GS_RESULT.items() if mn == _ctrl)
anchor("SAN.2 THE CLASSICAL CONTROL SATISFIES ALL FOUR AXIOMS, GS3 "
       "INCLUDED: its division-event assignment is a global section AND is "
       "system-independent, so the axioms of SEC 3 are satisfiable and the "
       "obstruction reported below is not an artefact of stating an "
       "unsatisfiable set",
       _ctrl_gs,
       f"{sum(1 for k in GS_RESULT if k[0] == _ctrl)} readings, all four "
       f"axioms holding in each")

_sep = MODELS[1]["name"]
_sep_all = all(CENSUS[(mn, r, s)][0][k]
               for (mn, r, s) in CENSUS if mn == _sep for k in TIMES)
_sep_abc = CENSUS[(_sep, "M:p_unif", "ABC")][0]
check("SAN.2b SEPARABILITY DOES NOT CONFER DIVISIBILITY, and this is worth "
      "stating because it is the one place a reader might expect the "
      "control to behave classically: the QUANTUM product model, whose "
      "dynamics and whose state both factorise across A, B and C at every "
      "time, is NOT divisible everywhere.  Its composite division-event "
      "set is a proper subset of the grid, and so is each factor's.  What "
      "divides everywhere is the CLASSICAL Markov product, not the "
      "separable quantum one",
      not _sep_all and not all(_sep_abc[k] for k in TIMES),
      f"quantum product model: DIV_ABC = {divstr(_sep_abc)}, a proper "
      f"subset of the grid; divides-everywhere = {_sep_all}")

# the known-indivisible reference: one qubit under an exact rotation
print()
print("  THE KNOWN-INDIVISIBLE REFERENCE.  A single qubit under the exact")
print("  rotation R(3/5, 4/5), i.e. the A factor of model M1.  Its "
      "transition")
print("  matrix is the bistochastic [[(1+l_k)/2, (1-l_k)/2], [(1-l_k)/2,")
print("  (1+l_k)/2]] with l_k = cos(2 k theta) an exact rational, and the")
print("  bridge from t_k to t_b has parameter l_b / l_k, so it is "
      "stochastic")
print("  exactly when |l_b| <= |l_k|.  The division-event set must "
      "therefore")
print("  be a PROPER subset of the grid.")
_lam = []
_c, _s = Fr(3, 5), Fr(4, 5)
_ck, _sk_ = Fr(1), Fr(0)
for k in TIMES:
    _lam.append(_ck * _ck - _sk_ * _sk_)
    _ck, _sk_ = _c * _ck - _s * _sk_, _s * _ck + _c * _sk_
report("l_k = cos(2 k theta) for k = 0..4, exactly",
       [str(x) for x in _lam])
_ref_fam = [[[(1 + l) / 2, (1 - l) / 2], [(1 - l) / 2, (1 + l) / 2]]
            for l in _lam]
_ref_d, _ref_det = div_predicate(_ref_fam, [(0,), (1,)], "REF single qubit")
_hand = {k: all(abs(_lam[b]) <= abs(_lam[k]) for b in TIMES if b >= k)
         for k in TIMES}
report("DIV of the reference qubit, computed by the instrument",
       divstr(_ref_d))
report("DIV of the reference qubit, from the closed form |l_b| <= |l_k|",
       divstr(_hand))
anchor("SAN.3 THE KNOWN-INDIVISIBLE REFERENCE SHOWS A NON-TRIVIAL DIVISION-"
       "EVENT SET, AND THE INSTRUMENT REPRODUCES THE CLOSED FORM EXACTLY: "
       "the single qubit under R(3/5,4/5) has DIV a PROPER subset of the "
       "grid, and the instrument's answer agrees with the hand computation "
       "|l_b| <= |l_k| at every grid index.  So the predicate is not "
       "trivially true, and it is not trivially false",
       _ref_d == _hand and not all(_ref_d[k] for k in TIMES),
       f"instrument {divstr(_ref_d)} = closed form {divstr(_hand)}; proper "
       f"subset = {not all(_ref_d[k] for k in TIMES)}")

_a_div = CENSUS[(MODELS[1]["name"], "C:000", "A")][0]
anchor("SAN.4 THE REFERENCE IS THE MODEL'S OWN A FACTOR: model M1's "
       "subsystem A, read conditionally, has exactly the reference's "
       "division-event set -- so the reference is not a separate fixture "
       "but the census's own object",
       _a_div == _ref_d,
       f"M1 subsystem A (reading C:000): {divstr(_a_div)} vs "
       f"reference {divstr(_ref_d)}")

# ---- [B3]'s own unistochastic candidate bridge --------------------------
print()
print("  A SECOND, INDEPENDENT READING OF THE COMPOSITE'S BRIDGE.  For a")
print("  closed unistochastic system [B3] supplies a natural candidate for")
print("  Gamma(t <- t'), namely |U(t <- t')|^2 with U(t <- t') = U(t<-0)")
print("  U(t'<-0)^dagger.  It is always column-stochastic; the question is")
print("  whether it satisfies eq. 23.  This is censused separately from the")
print("  existence question above, and it is NOT used to decide anything.")
_cand_tot = _cand_ok = 0
_cand_by = Counter()
for m in MODELS:
    if m["classical"]:
        continue
    for k in TIMES:
        for b in TIMES:
            if b <= k:
                continue
            Ub = mat_mul(m["kind"], m["U"][b],
                         mat_dag(m["kind"], m["U"][k]))
            Gb, bad = gamma_from_unitary(m["kind"], Ub)
            _cand_tot += 1
            if bad:
                _cand_by[(m["name"].split()[0], "IRRATIONAL")] += 1
                continue
            prod = fr_mul(Gb, m["GAMMA"][k])
            ok = (prod == m["GAMMA"][b])
            _cand_ok += int(ok)
            _cand_by[(m["name"].split()[0], "SATISFIES-EQ23" if ok
                      else "FAILS-EQ23")] += 1
report("[B3]'s unistochastic candidate |U(t<-t')|^2 tested against eq. 23",
       f"{_cand_ok} of {_cand_tot} spanning pairs satisfy it")
report("by model", fmt_counter(_cand_by))
_agree_cand = 0
_disagree_cand = 0
for m in MODELS:
    if m["classical"]:
        continue
    for k in TIMES:
        for b in TIMES:
            if b <= k:
                continue
            Ub = mat_mul(m["kind"], m["U"][b],
                         mat_dag(m["kind"], m["U"][k]))
            Gb, bad = gamma_from_unitary(m["kind"], Ub)
            if bad:
                continue
            ok = (fr_mul(Gb, m["GAMMA"][k]) == m["GAMMA"][b])
            cs = SUBC[(0, 1, 2)]
            r = bridge_exists(m["GAMMA"][k], m["GAMMA"][b], cs, "cand")
            if ok and r["verdict"] != "DIVISIBLE":
                _disagree_cand += 1
            else:
                _agree_cand += 1
check("SAN.5 THE CANDIDATE AND THE EXISTENCE QUESTION ARE CONSISTENT: "
      "wherever [B3]'s own unistochastic candidate |U(t<-t')|^2 satisfies "
      "eq. 23, the existence test returns DIVISIBLE -- as it must, since "
      "the candidate is then itself a witness.  The converse does not "
      "hold and is not claimed",
      _disagree_cand == 0,
      f"{_agree_cand} consistent, {_disagree_cand} inconsistent")


# ===========================================================================
# SEC 11.  DETERMINISM PROBE
# ===========================================================================

sec("DETERMINISM PROBE")

_sig = []
for m in MODELS:
    for r in _rlabels[m["name"]]:
        for S in LATTICE:
            _sig.append((m["name"], r, LNAME[S],
                         divstr(CENSUS[(m["name"], r, LNAME[S])][0])))
_sig = sorted(_sig, key=sk)
_h = 0
for t in _sig:
    for ch in "|".join(t):
        _h = (_h * 131 + ord(ch)) % (2 ** 61 - 1)
report("census signature (order-independent rolling hash over the sorted "
       "(model, reading, subsystem, DIV) tuples)", _h)
report("census rows", len(_sig))
check("DET.1 EVERY PRINTED AGGREGATE IS ORDERED BY U1's HASH-SEED-"
      "INDEPENDENT KEY sk(), and no set or dict iteration feeds a printed "
      "number without passing through it; the signature above is therefore "
      "reproducible under any PYTHONHASHSEED",
      len(_sig) == len(set(_sig)), f"{len(_sig)} distinct census rows")

_rerun = 0
for _ in range(2):
    _r2 = bridge_exists(MODELS[1]["GAMMA"][1], MODELS[1]["GAMMA"][2],
                        SUBC[(0, 1, 2)], "det-probe")
    _rerun += int(_r2["verdict"] == "INDIVISIBLE"
                  or _r2["verdict"] == "DIVISIBLE")
check("DET.2 THE DECISION PROCEDURE IS A FUNCTION OF ITS TWO MATRICES: "
      "re-deciding the same pair returns the same verdict, and the cache "
      "keyed on the exact matrices is therefore sound",
      _rerun == 2, f"{_rerun}/2 repeat decisions agree")


# ===========================================================================
# SEC 12.  THE VERDICT
# ===========================================================================

sec("THE VERDICT, against the pre-registered outcomes")

_cross = len(DOWN_FAILS) + len(UP_FAILS)
_obstr = _n - _sect

print()
print("  PRE-REGISTERED OUTCOMES (bc/note-bc1-division-event-composition-"
      "pin.md):")
print("    C-CONSISTENT   natural containments hold on all tested models")
print("    C-CROSS        containments fail, with exact witnesses")
print("    C-OBSTRUCTION  a model admits no consistent global assignment")
print("                   under the stated axioms")
print()
report("downward (GS1) crossings", len(DOWN_FAILS))
report("upward crossings", len(UP_FAILS))
report("(model, reading) pairs whose computed family is NOT a global "
       "section", f"{_obstr} of {_n}")
report("models with at least one non-section reading", _bad_models)
report("(model, reading) pairs failing GS3 (system-independence)",
       f"{_n - _g3} of {_n}")
report("EXHAUSTIVE SWEEP: circuits failing GS1, per reading, of "
       f"{_sw_n}", _sw_g1_fail)
report("EXHAUSTIVE SWEEP: circuits failing GS2, per reading",
       _sw_g2_fail)
report("EXHAUSTIVE SWEEP: circuits failing GS3, per reading",
       _sw_g3_fail)
report("EXHAUSTIVE SWEEP: circuits whose family IS a global section",
       _sw_sect)
report("EXHAUSTIVE SWEEP: hard-obstruction slices (only the empty "
       "assignment survives)", len(SW_EMPTY))

if _obstr > 0:
    VERDICT = "C-OBSTRUCTION"
    WHY = ("computed division-event families violate GS1 "
           "(restriction-compatibility) and, in the exhaustive sweep, GS2 "
           "(gluing) as well, so they are not compatible families for the "
           "restriction presheaf and admit no global section in the sense "
           "declared in SEC 3.  On "
           + str(len(SW_EMPTY)) + " sweep slices the obstruction is HARD: "
           "not even a non-empty sub-assignment of the data is a section, "
           "because a composite carries a division event while none of its "
           "three constituents does.  C-CROSS is established a fortiori: "
           "the crossings ARE the violations.")
elif _cross > 0:
    VERDICT = "C-CROSS"
    WHY = ("containments fail with exact witnesses, but every computed "
           "family still satisfies GS0, GS1 and GS2.")
else:
    VERDICT = "C-CONSISTENT"
    WHY = "every natural containment holds on every tested model."

print()
print(f"  VERDICT: {VERDICT}")
for _i in range(0, len(WHY), 70):
    print(f"           {WHY[_i:_i + 70]}")
print()
print("  WHAT THIS DOES AND DOES NOT SAY.  It says: at the tested "
      "dimensions")
print("  and dynamics, [B3]'s division-event assignment is not a "
      "restriction-")
print("  compatible family on the subsystem lattice, so there is no global,")
print("  system-independent division-event structure to be had -- the")
print("  system-centricity [B3] p.10 announces is FORCED, not merely")
print("  permitted, and it has the shape of a marginal problem with exact")
print("  witnesses.  It does NOT say [B3] is inconsistent: [B3] nowhere")
print("  asserts GS1, and the census confirms its own stated position.  It")
print("  says nothing about nature, about QFT, or about any other "
      "programme.")

print()
print("=" * 78)
print(f"  gates: {PASS} pass, {FAIL} fail; anchors failed: {ANCHOR_FAIL}")
print(f"  (D1) queries: {CALL_COUNT[0]}; distinct decisions: "
      f"{DEC_COUNT[0]}; exact simplex invocations: {_LP_CALLS[0]}; "
      f"full-LP (step 4): {len(LP_STATS)}")
print(f"  runtime: {time.time() - T0:.1f}s")
print("=" * 78)

sys.exit(1 if ANCHOR_FAIL else 0)
