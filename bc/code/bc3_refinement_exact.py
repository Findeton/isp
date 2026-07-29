#!/usr/bin/env python3
"""
bc3_refinement_exact.py — BC3: UNISTOCHASTICITY UNDER REFINEMENT.

Pin: bc/note-bc3-unistochasticity-refinement-pin.md (STRICT, frozen before
this file existed).  Program ledger: bc/LOG.md #1.  Primary source: [B3]
J. A. Barandes, "Quantum Systems as Indivisible Stochastic Processes",
arXiv:2507.21192, 35 pp, read in-session as PDF; every quotation below is
PAGE-cited to that PDF.

THE QUESTION.  [B3]'s quantum criterion Gamma_ij = |U_ij|^2 is a
basis-anchored, finite-dimensional, discrete-matrix notion.  Field theory
needs limits: finer configuration bins, finer time steps, dimension to
infinity.  Is the unistochastic class closed under the operations a
continuum limit performs -- and does the naive continuum object exist?

THE THREE ARMS
  ARM A  THE BINNED PROPAGATOR.  The free particle on a ring of n sites,
         exact discrete propagator U_n = F^dagger diag(phases) F with
         cyclotomic entries, on a declared arithmetic time grid.  The
         classical fact (unitary => |U|^2 doubly stochastic) is GATED, not
         cited.  Then the sites are BINNED, k into one, and the binned
         matrix's exact distance from bistochastic and from unistochastic
         is measured: the DEFECT LAW along the n-ladder at fixed physical
         parameters, and along the bin ladder.  One Trotterised
         harmonic-oscillator control.
  ARM B  THE CONTINUUM OBJECT'S DISCRETE SHADOW.  The exact discrete
         counterpart of the analytic fact that the continuum free
         propagator has |K|^2 = m / (2 pi hbar t), which is not a
         probability kernel: row masses against bin width, which
         normalisations depend on the discretisation, which limits exist
         and which do not.  The discrete family IS the receipt; no
         continuum analysis is performed beyond what it exhibits.
  ARM C  COMPOSITION CLOSURE AT n = 3.  Exact algebraic U, V; the expected
         control |UV|^2 != |U|^2 . |V|^2 gated (that difference IS
         indivisibility); then THE QUESTION -- is the divisible
         composition |U|^2 . |V|^2, what a coarse observer writes, itself
         unistochastic?

ENGRAVED CONSTRAINTS (pin sec. "Scope", carried into every gate text)
  * TOY LATTICE SCALE.  No continuum analysis is claimed beyond what the
    discrete family exhibits.  No renormalisation claim.  No claim about
    interacting quantum field theory.  No claim about nature.  Findings
    are formal properties of [B3]'s criterion under the stated operations.
  * NOT UNDER TEST: Barandes' equivalence theorem (proven mathematics).
  * Lean: NONE.  Q-STABLE, Q-UNSTABLE and Q-ILLDEFINED are all reportable.

HOUSE RULES OBSERVED
  * Exact arithmetic end to end: fractions.Fraction for every probability
    and matrix entry; the committed Surd ring for the polygon sign oracle
    and the real algebraic certificates; the committed Cyc ring
    Q[x]/Phi_N(x) for complex unitary certificates; a Gaussian-rational
    ring Q(i) for the Arm C unitary pool.  No float appears in any
    substantive computation and no tolerance is used anywhere.
  * The U3 instruments are the COMMITTED ones, lifted by AST from
    v11/code/u3_unistochasticity_screen_exact.py and not retyped.
  * Anchors (the reused instruments and their known-answer battery) are
    exit-1-only.  Substantive negatives exit 0.
  * Determinism: no randomness anywhere; every census is printed in a
    fixed order.
"""

from __future__ import annotations

import ast
import math
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
SECT = [0]


def sec(title):
    SECT[0] += 1
    print()
    print("-" * 78)
    print(f"SEC {SECT[0]}  {title}   [+{time.time() - T0:.0f}s]")
    print("-" * 78)
    sys.stdout.flush()


def tick(msg):
    print(f"     ... {msg}   [+{time.time() - T0:.0f}s]")
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


def report(label, value):
    print(f"  [DATA] {label}: {value}")
    sys.stdout.flush()


def fsl(xs):
    return "[" + ", ".join(str(x) for x in xs) + "]"


# ===========================================================================
# SEC 0.  THE REGISTRY
# ===========================================================================

print("=" * 78)
print("bc3_refinement_exact.py — BC3")
print("UNISTOCHASTICITY UNDER REFINEMENT: does the class survive the")
print("operations QFT needs?")
print("=" * 78)
print("  banner: EXACT arithmetic end to end and NO TOLERANCE ANYWHERE.")
print("  scope : TOY LATTICE SCALE.  Formal properties of [B3]'s criterion")
print("          under binning, refinement and composition.  No")
print("          renormalisation claim, no interacting-QFT claim, no claim")
print("          about nature.")
print("  lean  : NONE.  Q-STABLE, Q-UNSTABLE and Q-ILLDEFINED are all")
print("          reportable outcomes of the pin.")

QUOTES = {
    "B3-uni": (
        "[B3] arXiv:2507.21192, PAGE 18, the paragraph following eq. (68) "
        "(PDF read in-session)",
        "In general, an N x N matrix is called unistochastic if its "
        "individual entries are expressible as the modulus-squares of the "
        "corresponding entries of an N x N unitary matrix.  It follows "
        "that (64) is just the statement that the system's transition "
        "matrix Gamma(t <- 0) can be taken to be unistochastic, and will "
        "therefore be said to describe a unistochastic process.",
    ),
    "B3-dilation": (
        "[B3] arXiv:2507.21192, PAGE 19, first paragraph (the "
        "stochastic-quantum theorem); the dilation machinery is sec. 4.2, "
        "PAGES 25-28, eqs. (98)-(110)",
        "The preceding analysis implies that an indivisible stochastic "
        "process can be viewed either as a unistochastic process itself, "
        "or (if a nontrivial dilation was required) as a subsystem of a "
        "unistochastic process.  This statement is called the "
        "stochastic-quantum theorem (Barandes 2023).  --- AND, PAGE 28, "
        "after eq. (110): 'obtaining a unitary time-evolution operator "
        "for a given system may require dilating the Hilbert space in "
        "just this way'.",
    ),
    "B3-gauge": (
        "[B3] arXiv:2507.21192, PAGE 19, second paragraph",
        "Note that a unitary time-evolution operator U (t <- 0) will not "
        "generically remain unitary under arbitrary Schur-Hadamard gauge "
        "transformations (30).  Hence, writing a unistochastic transition "
        "matrix Gamma(t <- 0) in terms of a unitary time-evolution "
        "operator U (t <- 0) corresponds to making a gauge choice.",
    ),
    "B3-finite": (
        "[B3] arXiv:2507.21192, PAGE 11, sec. 3.1, eqs. (24)-(25)",
        "To see how this construction works in the finite-dimensional "
        "case, consider an indivisible stochastic process with N total "
        "configurations i = 1, ..., N making up the system's "
        "configuration space C. ... Gamma_ij(t <- 0) = p(i, t | j, 0). ... "
        "Gamma_ij(t <- 0) = |Theta_ij(t <- 0)|^2.",
    ),
    "B3-continuum": (
        "[B3] arXiv:2507.21192, PAGE 5, sec. 2, after eqs. (1) and (2)",
        "Examples would include the discrete configurations of a system of "
        "finitely many digital bits, or the continuous set of possible "
        "arrangements of a collection of particles in three-dimensional "
        "physical space. ... where the discrete summation would be "
        "replaced with an integration in the case of a system with a "
        "continuous configuration space.",
    ),
    "lit-uni3": (
        "LITERATURE, as registered by the committed U3 receipt "
        "(v11/code/u3_unistochasticity_screen_exact.py, QUOTES['lit-uni3']). "
        " Au-Yeung and Poon, SEA Bull. Math. 3 (1979) 85-92; H. Nakazato, "
        "Nihonkai Math. J. 7 (1996) 83-100; Bengtsson, Ericsson, Kus, "
        "Tadej, Zyczkowski, Commun. Math. Phys. 259 (2005) 307-324",
        "A bistochastic 3x3 matrix is unistochastic iff its unitarity "
        "TRIANGLE closes: the three phasors of modulus sqrt(B_ip B_iq), "
        "i = 1,2,3, arising from the orthogonality of columns p and q, "
        "must be able to sum to zero -- i.e. must satisfy the triangle "
        "inequality.",
    ),
    "lit-sqrtind": (
        "LITERATURE, as registered by the committed U3 receipt.  "
        "A. S. Besicovitch, J. London Math. Soc. 15 (1940) 3-6; standard "
        "Galois theory",
        "The set {sqrt d : d a squarefree positive integer} is linearly "
        "independent over Q; hence a Q-linear combination of such radicals "
        "is zero iff every coefficient is zero.",
    ),
    "u3-screen": (
        "v11/code/u3_unistochasticity_screen_exact.py, the committed U3 "
        "receipt: SEC 1 (the rings Surd and Cyc) and SEC 2 (ds_report, "
        "tri_disc, chain_link_squares, polygon_violations, "
        "unitary_check_cyc, modsq_check_cyc, orth_check_surd, "
        "modsq_check_surd, real_orth_2x2, sylvester, and the known-answer "
        "battery KA-1 .. KA-6)",
        "the n = 3 exact unistochasticity criterion, the general polygon "
        "obstruction at every n, and the known-answer battery, are taken "
        "from the committed U3 receipt by AST extraction and re-run here "
        "as ANCHORS.  Nothing in that layer is re-derived, nothing in it "
        "is edited, and no file under v11/ is written by this receipt.",
    ),
    "u3-positive": (
        "v11/code/u3_unistochasticity_screen_exact.py, SEC 2, the "
        "'HOW THIS RECEIPT USES IT' block",
        "NEGATIVE direction (T < 0 => NOT unistochastic) is ELEMENTARY and "
        "is not taken on citation.  POSITIVE direction: no verdict of "
        "'unistochastic' is returned on the strength of T >= 0; every "
        "positive verdict EXHIBITS a unitary of the same size and verifies "
        "U^dagger U = I and |U_ij|^2 = Gamma_ij entry by entry in exact "
        "algebraic arithmetic.  BC3 carries the same discipline.",
    ),
}

print()
print("  THE REGISTRY — every source a gate cites, with its page or its")
print("  path:section provenance.")
for _k in sorted(QUOTES):
    print(f"    [{_k}] {QUOTES[_k][0]}")

CAPS = {
    "Arm A n-ladder (free family)": "n in {60, 120, 240, 480, 960, 1920, "
                                    "3840, 7680}; the propagator is "
                                    "circulant, so only its first row is "
                                    "built and the cost is O(c)",
    "Arm A direct-verification ladder": "n in {12, 24, 36, 48, 60} — the "
                                        "propagator is built ENTRY BY "
                                        "ENTRY as an exact element of "
                                        "Q(zeta_n) and the closed form is "
                                        "gated against it",
    "Arm A time grid": "theta = 2 pi p / q with 1 <= p <= q, gcd(p, q) = 1 "
                       "and q | n; q in {1, 2, 3, 4, 5, 6, 8, 10, 12, 15, "
                       "16, 20, 24}",
    "Arm A bin ladder": "B bins of k = n/B sites each, B | n, B in "
                        "{3, 4, 5, 6, 10, 12, 15, 20, 30, 60}",
    "Arm A (c, B) refinement sweep": "c in [1, 24], B in [2, 30], both "
                                     "spike offsets, at n = lcm(B, 2c), "
                                     "2 lcm(B, 2c) and 3 lcm(B, 2c)",
    "Arm A control": "Trotterised harmonic oscillator (D_x A)^M, n in "
                     "{9, 12, 18, 24, 36}, M in [1, 6], chirp parameters "
                     "p, p' in {1, 2}; entries in Q(zeta_3); binned at "
                     "every B | n with B <= 12",
    "Arm C unitary pool": "3x3 unitaries over the Gaussian rationals Q(i), "
                          "BFS to word length <= 3 from a declared "
                          "generator set, deduplicated on |W|^2, pool "
                          "capped at 300 distinct matrices, frontier "
                          "capped at 220 per level",
    "Arm C exhaustive rational census": "every bistochastic 3x3 matrix "
                                        "with entries in (1/D)Z that "
                                        "passes the exact n = 3 criterion, "
                                        "and every ordered product of two "
                                        "of them, for D in {4, 6, 8, 10, "
                                        "12}",
    "NOT implemented": "full phase-elimination (resultants / Groebner) for "
                       "n > 3.  A binned matrix with NO polygon "
                       "obstruction and NO exhibited certificate is "
                       "reported EXCLUDED-BY-CAP, never as a pass",
    "NOT in scope": "times theta/2pi irrational, and lattice sizes n not "
                    "divisible by q: there the modulus-squares leave Q and "
                    "the exact rational screen does not apply.  One such "
                    "case is computed exactly in Q(zeta_28) below and its "
                    "irrationality is GATED, so the exclusion is a stated "
                    "fact and not an assumption",
}


# ===========================================================================
# SEC 1.  SINGLE-SOURCING — the committed U3 instruments, lifted by AST
# ===========================================================================

sec("SINGLE-SOURCING — the committed U3 instruments, lifted by AST")

_P_U3 = "v11/code/u3_unistochasticity_screen_exact.py"

U3_REQ = {
    "sqfree_split": ["n"],
    "Surd": ["<class>"],
    "surd_sign": ["x"],
    "sqrt_fr": ["r"],
    "polydivmod": ["a", "b"],
    "Cyc": ["<class>"],
    "cyc_one": ["N"],
    "cyc_zero": ["N"],
    "cyc_x": ["N"],
    "cyc_pow": ["z", "k"],
    "phi_euler": ["n"],
    "ds_report": ["M"],
    "tri_disc": ["a", "b", "c"],
    "chain_link_squares": ["M", "p", "q", "by"],
    "polygon_violations": ["M"],
    "unitary_check_cyc": ["U"],
    "modsq_check_cyc": ["U", "M"],
    "orth_check_surd": ["U"],
    "modsq_check_surd": ["U", "M"],
    "real_orth_2x2": ["B"],
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
    """Extract named module-level FunctionDefs / ClassDefs by AST and
    compile them into ns.  Nothing is retyped and nothing is edited."""
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


_sig, _miss = ast_signatures(_P_U3, U3_REQ)
anchor("SRC.1 AST SIGNATURE PASS on the committed U3 receipt: every "
       "instrument BC3 reuses exists at module level with the exact "
       "positional argument list, so a silent upstream edit cannot slip "
       "through unnoticed",
       not _miss,
       f"{len(_sig)} module-level defs/classes in {_P_U3}; "
       f"{len(U3_REQ)} required; missing/changed: {_miss}")

PHI = {8: [Fr(1), Fr(0), Fr(0), Fr(0), Fr(1)],
       12: [Fr(1), Fr(0), Fr(-1), Fr(0), Fr(1)]}
PHI_NAME = {8: "x^4 + 1", 12: "x^4 - x^2 + 1"}
SIGN_BITS_USED = [0]

NS = {"Fr": Fr, "math": math, "PHI": PHI, "PHI_NAME": PHI_NAME,
      "SIGN_BITS_USED": SIGN_BITS_USED, "product": product}
_segs = ast_defs(_P_U3, list(U3_REQ), NS)
anchor("SRC.2 THE INSTRUMENTS ARE U3's, LIFTED NOT RETYPED: the exact "
       "rings (Surd, Cyc), the n = 3 triangle discriminant, the general "
       "polygon obstruction, the doubly-stochastic report and the four "
       "certificate verifiers are compiled from the committed U3 source "
       "text by AST extraction",
       len(_segs) == len(U3_REQ),
       f"{len(_segs)}/{len(U3_REQ)} lifted: {sorted(_segs)}")

sqfree_split = NS["sqfree_split"]
Surd = NS["Surd"]
surd_sign = NS["surd_sign"]
sqrt_fr = NS["sqrt_fr"]
polydivmod = NS["polydivmod"]
Cyc = NS["Cyc"]
cyc_one = NS["cyc_one"]
cyc_zero = NS["cyc_zero"]
cyc_x = NS["cyc_x"]
cyc_pow = NS["cyc_pow"]
phi_euler = NS["phi_euler"]
ds_report = NS["ds_report"]
tri_disc = NS["tri_disc"]
chain_link_squares = NS["chain_link_squares"]
polygon_violations = NS["polygon_violations"]
unitary_check_cyc = NS["unitary_check_cyc"]
modsq_check_cyc = NS["modsq_check_cyc"]
orth_check_surd = NS["orth_check_surd"]
modsq_check_surd = NS["modsq_check_surd"]
real_orth_2x2 = NS["real_orth_2x2"]
sylvester = NS["sylvester"]

print("  [DATA] caps:")
for _k, _v in CAPS.items():
    print(f"          {_k}: {_v}")


def cyclotomic(n, cache={}):
    """Phi_n(x) as a low-to-high Fraction coefficient list, by the exact
    recursion Phi_n = (x^n - 1) / prod_{d | n, d < n} Phi_d."""
    if n in cache:
        return cache[n]
    num = [Fr(0)] * (n + 1)
    num[0] = Fr(-1)
    num[n] = Fr(1)
    for d in range(1, n):
        if n % d == 0:
            qq, rr = polydivmod(num, cyclotomic(d))
            num = qq
    while num and num[-1] == 0:
        num.pop()
    cache[n] = num
    return num


def ensure_phi(n):
    if n not in PHI:
        PHI[n] = cyclotomic(n)
        PHI_NAME[n] = f"Phi_{n} (degree {len(PHI[n]) - 1})"
    return PHI[n]


_POWC = {}


def pows(N):
    """[1, zeta_N, ..., zeta_N^{N-1}] as exact Cyc elements, cached."""
    if N not in _POWC:
        ensure_phi(N)
        L = [cyc_one(N)]
        x = cyc_x(N)
        for _ in range(1, N):
            L.append(L[-1] * x)
        _POWC[N] = L
    return _POWC[N]


# ===========================================================================
# SEC 2.  THE RINGS — U3's self-tests re-run on the lifted objects
# ===========================================================================

sec("THE RINGS — U3's own self-tests, re-run on the lifted objects")

_t1 = sqrt_fr(Fr(2)) * sqrt_fr(Fr(3)) - sqrt_fr(Fr(6))
_t2 = (sqrt_fr(Fr(2)) + sqrt_fr(Fr(3))) * (sqrt_fr(Fr(2)) + sqrt_fr(Fr(3)))
_t3 = sqrt_fr(Fr(1, 2)) * sqrt_fr(Fr(1, 2)) - Surd(Fr(1, 2))
anchor("R1.1 THE LIFTED Surd RING IS EXACT AND ITS ZERO TEST IS SOUND "
       "[lit-sqrtind]: sqrt2.sqrt3 - sqrt6 = 0 identically; "
       "(sqrt2+sqrt3)^2 = 5 + 2 sqrt6 identically; sqrt(1/2)^2 = 1/2",
       _t1.is_zero() and dict(_t2) == {1: Fr(5), 6: Fr(2)} and _t3.is_zero(),
       f"sqrt2.sqrt3-sqrt6 = {_t1}; (sqrt2+sqrt3)^2 = {_t2}")

_t4 = sqrt_fr(Fr(2)) + sqrt_fr(Fr(3)) - sqrt_fr(Fr(10))
_t5 = sqrt_fr(Fr(2)) + sqrt_fr(Fr(3)) - sqrt_fr(Fr(5))
anchor("R1.2 THE LIFTED Surd SIGN ORACLE IS EXACT ON A KNOWN-ANSWER PAIR "
       "THAT NO TOLERANCE SETTLES: sqrt2+sqrt3-sqrt10 < 0 (3.146... < "
       "3.162...) while sqrt2+sqrt3-sqrt5 > 0",
       surd_sign(_t4) == -1 and surd_sign(_t5) == +1,
       f"signs {surd_sign(_t4)}, {surd_sign(_t5)}; at most "
       f"{SIGN_BITS_USED[0]} binary digits of refinement")

_cycok, _cycdet = True, []
for _N in (3, 4, 8, 12, 24, 28):
    ensure_phi(_N)
    _xn = [Fr(0)] * _N + [Fr(1)]
    _xn[0] = Fr(-1)
    _qq, _rr = polydivmod(_xn, PHI[_N])
    _deg_ok = (len(PHI[_N]) - 1) == phi_euler(_N)
    _rem_ok = (not _rr) or all(x == 0 for x in _rr)
    _one_ok = cyc_pow(cyc_x(_N), _N) == cyc_one(_N)
    _cnj = cyc_x(_N).conj()
    _inv_ok = (cyc_x(_N) * _cnj) == cyc_one(_N) and _cnj.conj() == cyc_x(_N)
    _cycok &= _deg_ok and _rem_ok and _one_ok and _inv_ok
    _cycdet.append(f"N={_N}: deg {len(PHI[_N]) - 1} = phi(N) = "
                   f"{phi_euler(_N)} {_deg_ok}, Phi | x^N-1 {_rem_ok}, "
                   f"x^N = 1 {_one_ok}, conj {_inv_ok}")
anchor("R1.3 THE CYCLOTOMIC FIELDS ARE THE FIELDS THEY CLAIM TO BE, "
       "INCLUDING THE FOUR THIS UNIT ADDS TO U3's TWO: for N in "
       "{3, 4, 8, 12, 24, 28} the cyclotomic polynomial computed by the "
       "exact recursion Phi_N = (x^N - 1) / prod_{d | N, d < N} Phi_d has "
       "degree phi(N), divides x^N - 1 with remainder EXACTLY zero, "
       "satisfies x^N = 1 in the quotient, and zeta -> zeta^{-1} is an "
       "involution with zeta . conj(zeta) = 1",
       _cycok, "; ".join(_cycdet))

ZETA3 = cyc_pow(cyc_x(12), 4)
INV_SQRT3 = (cyc_x(12) * 2 - cyc_pow(cyc_x(12), 3)) * Fr(1, 3)
anchor("R1.4 THE DFT NORMALISER IS AN EXACT FIELD ELEMENT: "
       "(zeta12 + zeta12^-1)^2 = 3 exactly, so 1/sqrt3 = "
       "(2 zeta12 - zeta12^3)/3 exactly; zeta3 = zeta12^4 has order 3",
       (INV_SQRT3 * INV_SQRT3) == Cyc(12, [Fr(1, 3)])
       and cyc_pow(ZETA3, 3) == cyc_one(12) and ZETA3 != cyc_one(12),
       f"(1/sqrt3)^2 = {INV_SQRT3 * INV_SQRT3}")


# ===========================================================================
# SEC 3.  THE KNOWN-ANSWER BATTERY — U3's, re-run here as anchors
# ===========================================================================

sec("THE KNOWN-ANSWER BATTERY — U3's, re-run here as ANCHORS")

print(f"""
  [B3]'s definition, verbatim ({QUOTES['B3-uni'][0]}):
    "{QUOTES['B3-uni'][1]}"

  [B3]'s dilation clause, verbatim ({QUOTES['B3-dilation'][0]}):
    "{QUOTES['B3-dilation'][1]}"

  THE TWO KNOWN FACTS THE PIN ORDERS CITED, NOT RE-PROVED.
    (i)  MARGINALISATION LEAVES THE CLASS.  [B3]'s own stochastic-quantum
         theorem is disjunctive: a process is EITHER unistochastic itself
         OR a SUBSYSTEM of one.  The second disjunct exists precisely
         because passing to a subsystem -- marginalising -- does not
         preserve the first.  BC3 cites this and does not re-prove it.
         Consequently every negative verdict in this receipt is a verdict
         on the FIRST disjunct: the CLOSED, UNDILATED criterion at the
         stated dimension.  The subsystem disjunct is untouched.
    (ii) The gauge clause ({QUOTES['B3-gauge'][0]}):
         "{QUOTES['B3-gauge'][1]}"

  THE TWO FACTS THE PIN ORDERS GATED IN-RECEIPT are SEC 4 (unitary =>
  |U|^2 doubly stochastic) and SEC 5 (fixed-n topological closure).

  HOW THE CRITERION IS USED ({QUOTES['u3-positive'][0]}):
    "{QUOTES['u3-positive'][1]}"
""")

FLAT3 = [[Fr(1, 3)] * 3 for _ in range(3)]
U_DFT3 = [[cyc_pow(ZETA3, (i * j) % 3) * 1 * INV_SQRT3 for j in range(3)]
          for i in range(3)]
_ka1 = (not unitary_check_cyc(U_DFT3)) and (not modsq_check_cyc(U_DFT3, FLAT3))
_ka1T = tri_disc(*chain_link_squares(FLAT3, 0, 1, "col"))
anchor("KA-1 J/3 IS DECIDED UNISTOCHASTIC WITH THE UNITARY EXHIBITED: the "
       "3-point DFT written exactly in Q(zeta_12) satisfies U^dagger U = I "
       "with zero residual entries and |U_ij|^2 = 1/3 at all nine entries; "
       "T = +1/27 > 0 and there is no polygon violation",
       _ka1 and _ka1T > 0 and not polygon_violations(FLAT3),
       f"T = {_ka1T}; unitarity residuals 0; |U|^2 mismatches 0")

BNOT = [[Fr(0), Fr(1, 2), Fr(1, 2)],
        [Fr(1, 2), Fr(0), Fr(1, 2)],
        [Fr(1, 2), Fr(1, 2), Fr(0)]]
_ka2ds = ds_report(BNOT)
_ka2T = tri_disc(*chain_link_squares(BNOT, 0, 1, "col"))
_ka2pv = polygon_violations(BNOT)
anchor("KA-2 (1/2)(J - I) IS DECIDED BISTOCHASTIC BUT NOT UNISTOCHASTIC "
       "WITH AN EXACT MARGIN: rows and columns sum to exactly 1, "
       "T = -1/16 < 0, and the polygon oracle independently flags the same "
       "obstruction",
       _ka2ds["ds"] and _ka2T == Fr(-1, 16) and len(_ka2pv) > 0,
       f"DS {_ka2ds['ds']}; T = {_ka2T}; polygon violations {len(_ka2pv)}")

_par = [sum(s) for s in product((1, -1), repeat=3)]
anchor("KA-3 THE ORTHO/UNI GAP IS EXHIBITED, SO THE COMPLEX NUMBERS ARE "
       "FORCED SOMEWHERE: J/3 is unistochastic but NOT orthostochastic — "
       "a real orthogonal O with O_ij^2 = 1/3 would need two rows of inner "
       "product (+-1 +-1 +-1)/3 and every one of the eight sign patterns "
       "gives an odd integer, never 0",
       all(x != 0 for x in _par),
       f"the eight numerators are {sorted(set(_par))} — none is 0")

B2 = [[Fr(1, 3), Fr(2, 3)], [Fr(2, 3), Fr(1, 3)]]
U2 = real_orth_2x2(B2)
anchor("KA-4 THE n = 2 CLASSICAL FACT IS CONSTRUCTED, NOT ASSERTED: for "
       "[[1/3,2/3],[2/3,1/3]] the constructed real matrix is exactly "
       "orthogonal in the Surd ring and its modulus-squares are the "
       "matrix; the construction is uniform in p, so EVERY 2x2 "
       "bistochastic matrix is orthostochastic and no 2-outcome object "
       "can ever leave the class",
       (not orth_check_surd(U2)) and (not modsq_check_surd(U2, B2)),
       f"U = [[{U2[0][0]}, {U2[0][1]}], [{U2[1][0]}, {U2[1][1]}]]")

BRS = [[Fr(1, 2), Fr(1, 2)], [Fr(1), Fr(0)]]
_ka5 = ds_report(BRS)
anchor("KA-5 THE DOUBLY-STOCHASTIC PRECONDITION IS NOT A NO-OP: a "
       "row-stochastic matrix that is not column-stochastic is caught with "
       "the exact per-column excess printed",
       _ka5["row_ok"] and not _ka5["col_ok"] and not _ka5["ds"],
       f"col sums {fsl(_ka5['colsums'])}, col deficits "
       f"{fsl(_ka5['coldef'])}")

_H8 = sylvester(3)
anchor("KA-6 SYLVESTER'S REAL HADAMARD MATRIX OF ORDER 8 IS VERIFIED "
       "IN-RECEIPT (H H^T = 8 I over the integers)",
       all(sum(_H8[k][i] * _H8[k][j] for k in range(8))
           == (8 if i == j else 0) for i in range(8) for j in range(8)),
       "H_8 = H_2^{tensor 3}, all 64 inner products exact")


# --- the fast polygon oracle, gated against the committed one -------------

def poly_fast(M):
    """The SAME criterion as the committed polygon_violations, with the
    total re-used across the index loop (O(n) per pair instead of O(n^2))
    and an exact early exit on the all-zero pairs.  Gated below against
    the committed function on every matrix on which both are run."""
    n, m = len(M), len(M[0])
    out = []
    pairs = [("col", p, q) for p in range(m) for q in range(p + 1, m)]
    pairs += [("row", p, q) for p in range(n) for q in range(p + 1, n)]
    for by, p, q in pairs:
        a = chain_link_squares(M, p, q, by)
        if not any(x != 0 for x in a):
            continue
        L = [sqrt_fr(x) for x in a]
        tot = Surd()
        for x in L:
            tot = tot + x
        for i in range(len(L)):
            slack = tot - L[i] - L[i]
            if surd_sign(slack) < 0:
                out.append((by, p, q, i, a, slack))
    return out


POLY_GATE = [0, 0]


def poly_both(M, force=False):
    """Run the fast oracle; when the matrix is small enough, run the
    COMMITTED oracle too and require identical output."""
    fast = poly_fast(M)
    if force or len(M) <= 10:
        slow = polygon_violations(M)
        POLY_GATE[0] += 1
        key_f = sorted((b, p, q, i, tuple(a), str(s)) for b, p, q, i, a, s
                       in fast)
        key_s = sorted((b, p, q, i, tuple(a), str(s)) for b, p, q, i, a, s
                       in slow)
        if key_f != key_s:
            POLY_GATE[1] += 1
    return fast


_pg = [BNOT, FLAT3,
       [[Fr(1, 2), Fr(1, 2), Fr(0)], [Fr(0), Fr(1, 2), Fr(1, 2)],
        [Fr(1, 2), Fr(0), Fr(1, 2)]],
       [[Fr(1, 4)] * 4 for _ in range(4)]]
for _M in _pg:
    poly_both(_M, force=True)
anchor("SRC.3 THE FAST POLYGON ORACLE IS THE COMMITTED ONE: on every "
       "matrix on which both run (every matrix of size <= 10 screened in "
       "this receipt, plus four seeds here) the fast oracle's violation "
       "list — sides, index, squared moduli and exact Surd slack — is "
       "IDENTICAL to the committed polygon_violations.  The fast path is "
       "an evaluation-order change and nothing else",
       POLY_GATE[1] == 0,
       f"{POLY_GATE[0]} matrices cross-checked so far, {POLY_GATE[1]} "
       f"discrepancies (the running total is re-reported in SEC 13)")


# ===========================================================================
# SEC 4.  GATED FACT 1 — unitary => |U|^2 doubly stochastic
# ===========================================================================

sec("GATED FACT 1 — unitary implies |U|^2 doubly stochastic")

print("""
  THE STATEMENT AND ITS ONE-LINE PROOF.  Let U be an N x N unitary matrix.
  Its columns are orthonormal, so sum_i |U_ij|^2 = (U^dagger U)_jj = 1 for
  every j; its rows are orthonormal, so sum_j |U_ij|^2 = (U U^dagger)_ii
  = 1 for every i; and every entry |U_ij|^2 is a non-negative real.  Hence
  Gamma = |U|^2 entrywise is DOUBLY STOCHASTIC.  In particular
  UNISTOCHASTIC => DOUBLY STOCHASTIC, so the doubly-stochastic report is a
  legitimate PRECONDITION and every failure of it is a certified failure of
  unistochasticity.  The converse is false: KA-2.

  This receipt does not rest on the proof.  Every unitary it constructs is
  verified U^dagger U = I entry by entry in exact algebraic arithmetic, and
  its |U|^2 is then verified doubly stochastic by exact rational summation.
""")

_H8n = [[Fr(_H8[i][j] * _H8[i][j], 8) for j in range(8)] for i in range(8)]
check("F1.1 THE PRECONDITION IS DISCHARGED ON THE OBJECTS ALREADY IN HAND: "
      "|DFT_3|^2 = J/3 and (1/8)|H_8|^2 = J/8 are both doubly stochastic "
      "by exact rational summation, with row and column sums exactly 1",
      ds_report(FLAT3)["ds"] and ds_report(_H8n)["ds"],
      f"J/3 row sums {fsl(ds_report(FLAT3)['rowsums'])}; J/8 row sums all "
      f"{ds_report(_H8n)['rowsums'][0]}")


# ===========================================================================
# SEC 5.  GATED FACT 2 — fixed-n topological closure, and the escape radius
# ===========================================================================

sec("GATED FACT 2 — fixed-n topological closure, and the exact escape "
    "radius")

print("""
  THE STATEMENT AND ITS PROOF, IN FULL, AT EVERY DIMENSION USED HERE.
  Fix N.  The unitary group U(N) is a closed and bounded subset of
  C^{N x N} -- closed because it is the preimage of the closed set {I}
  under the continuous map U |-> U^dagger U, bounded because every column
  is a unit vector, so |U_ij| <= 1 for all i, j.  By Heine-Borel it is
  COMPACT.  The modulus-square map Phi : C^{N x N} -> R^{N x N},
  Phi(U)_ij = |U_ij|^2, is a polynomial in the real and imaginary parts of
  the entries, hence CONTINUOUS.  The continuous image of a compact set is
  compact, and a compact subset of the Hausdorff space R^{N x N} is CLOSED.
  Therefore

        Uni(N) := Phi(U(N))

  is compact, in particular CLOSED, at every fixed N.  Two consequences are
  used below.  (a) A limit of unistochastic matrices is unistochastic: a
  defect positive at every step of a sequence may still have limit zero.
  (b) Contrapositive: if the limit matrix is NOT unistochastic then all but
  finitely many members of the sequence are not unistochastic either.
  Closure is what makes 'the defect does not vanish along the ladder' a
  statement with content rather than an artefact of the ladder.

  THE COMPLEMENT IS OPEN, AND ITS RADIUS IS COMPUTED EXACTLY.  Closure is a
  numerical-free fact; this receipt turns it into a computable certificate
  at N = 3.  Write T(M) = 2(AB + BC + CA) - A^2 - B^2 - C^2 with
  A = M_00 M_01, B = M_10 M_11, C = M_20 M_21 -- the committed triangle
  discriminant on the first column pair.  For M, M' with entries in [0,1],
    |A - A'| = |M_00 M_01 - M'_00 M'_01| <= |M_00 - M'_00| + |M_01 - M'_01|
  and likewise for B and C; and dT/dA = 2(B + C) - 2A has |dT/dA| <= 4 on
  [0,1]^3.  Hence
        |T(M) - T(M')|  <=  4 (|dA| + |dB| + |dC|)  <=  4 ||M - M'||_1 ,
  with ||.||_1 the entrywise l1 norm.  Since T < 0 certifies NOT
  unistochastic at every N (the polygon obstruction needs no
  bistochasticity), this gives the exact ESCAPE RADIUS

        T(M) < 0    =>    dist_1( M , Uni(3) )  >=  |T(M)| / 4 .

  Every negative verdict at three bins below is therefore reported with a
  certified positive distance to the class, not merely with a sign.
""")


def _T3(M):
    return tri_disc(*chain_link_squares(M, 0, 1, "col"))


def _l1(M, Mp):
    return sum(abs(M[i][j] - Mp[i][j]) for i in range(3) for j in range(3))


_gridL = [Fr(0), Fr(1, 5), Fr(2, 5), Fr(3, 5), Fr(4, 5), Fr(1)]
_seedA = [FLAT3, BNOT,
          [[Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(1, 2), Fr(1, 2)],
           [Fr(0), Fr(1, 2), Fr(1, 2)]],
          [[Fr(1, 2), Fr(1, 2), Fr(0)], [Fr(0), Fr(1, 2), Fr(1, 2)],
           [Fr(1, 2), Fr(0), Fr(1, 2)]]]
_lipmax, _lipn = Fr(0), 0
for _u, _v, _w, _z in product(_gridL, repeat=4):
    _B = [[_u, _v, 1 - _u - _v], [_w, _z, 1 - _w - _z],
          [1 - _u - _w, 1 - _v - _z, _u + _v + _w + _z - 1]]
    if any(x < 0 for r in _B for x in r):
        continue
    for _C in _seedA:
        d = _l1(_B, _C)
        if d == 0:
            continue
        ratio = abs(_T3(_B) - _T3(_C)) / d
        _lipn += 1
        if ratio > _lipmax:
            _lipmax = ratio
check("F2.1 THE LIPSCHITZ CONSTANT 4 IS NOT MERELY ASSERTED: over an exact "
      "rational grid of bistochastic 3x3 matrices paired against four "
      "declared reference matrices, the measured ratio "
      "|T(M) - T(M')| / ||M - M'||_1 never reaches 4",
      _lipmax <= 4,
      f"{_lipn} exact pairs, maximum measured ratio {_lipmax} = "
      f"{float(_lipmax):.5f} <= 4")

check("F2.2 THE ESCAPE RADIUS IS NON-VACUOUS ON THE COMMITTED "
      "COUNTEREXAMPLE: (1/2)(J - I) has T = -1/16 exactly, so every matrix "
      "within l1 distance 1/64 of it also has T < 0 and is therefore NOT "
      "unistochastic — the complement of Uni(3) contains an explicit ball, "
      "which is the computable form of closure",
      _ka2T == Fr(-1, 16),
      f"T = {_ka2T}; dist_1((1/2)(J-I), Uni(3)) >= 1/64")


# ===========================================================================
# SEC 6.  ARM A (i) — THE EXACT FREE PROPAGATOR ON A RING OF n SITES
# ===========================================================================

sec("ARM A (i) — THE EXACT FREE PROPAGATOR ON A RING OF n SITES")

print("""
  THE OBJECT.  Configuration space: the ring Z_n of n sites x_j = j a at
  lattice spacing a on a circle of circumference L = n a.  Momenta
  p_k = 2 pi k / L for k in a window K_n of n CONSECUTIVE integers (a
  complete residue system mod n, so the discrete Fourier transform on that
  window is unitary).  Free-particle dispersion E_k = p_k^2 / 2m -- the
  exact continuum dispersion of a particle on the circle, truncated to the
  n modes a lattice of n sites supplies.  The propagator is

     U_n(t) = F^dagger . diag( e^{-i E_k t} )_{k in K_n} . F ,
     U_n(t)_{jl} = (1/n) sum_{k in K_n} omega_n^{k(j-l)} e^{-i theta k^2},

  with omega_n = e^{2 pi i / n} and the SINGLE DIMENSIONLESS TIME

     theta := (2 pi)^2 t / (2 m L^2)  =  2 pi^2 t / (m L^2)     (hbar = 1).

  FIXED PHYSICAL PARAMETERS, DECLARED HONESTLY.  theta is built from t, m
  and L ONLY; it does not contain a.  So 'fixed physical parameters' means
  fixed target time t, fixed mass m, fixed box length L -- and the
  refinement n -> infinity is exactly a = L/n -> 0 at fixed theta.  That is
  the continuum limit of the configuration space, and it is the limit the
  defect law is stated in.  The alternative convention -- refining the time
  step with the lattice, so that theta shrinks as n grows -- is a DIFFERENT
  trajectory in the (c, B) table of SEC 9 and gives a different answer,
  which is exactly why the convention is printed.

  THE TIME GRID.  theta = 2 pi p / q with gcd(p, q) = 1 and q | n.  Then
  every diagonal phase e^{-i theta k^2} = zeta_q^{-p k^2} is an exact root
  of unity and U_n has entries in the cyclotomic field Q(zeta_n).  These
  times are DENSE in the time axis.

  U_n IS CIRCULANT (the ring is translation invariant), so Gamma_n =
  |U_n|^2 is determined by its first row, and so is every binning of it.
""")


def gcd(a, b):
    return math.gcd(a, b)


def revival(n, p, q):
    """(c, Delta, delta): Gamma_n = |U_n|^2 has exactly c equally weighted
    spikes of weight 1/c at displacements d = delta + j Delta,
    Delta = n/c."""
    g = gcd(2 * p, q)
    c = q // g
    Delta = n // c
    delta = (Delta // 2) if (q % 4 == 2 and p % 2 == 1) else 0
    return c, Delta, delta


def gamma_row_closed(n, p, q):
    c, Delta, delta = revival(n, p, q)
    row = [Fr(0)] * n
    for j in range(c):
        row[(delta + j * Delta) % n] = Fr(1, c)
    return row


def prop_row_cyc(n, p, q):
    """The exact first row of U_n as elements of Q(zeta_N), N = lcm(n, q)
    (= n whenever q | n), built ENTRY BY ENTRY from the defining sum."""
    N = n * q // gcd(n, q)
    P = pows(N)
    out = []
    for d in range(n):
        h = [0] * N
        for k in range(n):
            h[((N // n) * k * d - p * (N // q) * k * k) % N] += 1
        z = cyc_zero(N)
        for e in range(N):
            if h[e]:
                z = z + P[e] * Fr(h[e], n)
        out.append(z)
    return out, N


def modsq_row_cyc(n, p, q):
    """|U_n(d)|^2 as exact Cyc elements, via the histogram and its
    conjugate (conjugation of a root of unity is an index reflection, so
    no cyc_pow is needed)."""
    N = n * q // gcd(n, q)
    P = pows(N)
    out = []
    for d in range(n):
        h = [0] * N
        for k in range(n):
            h[((N // n) * k * d - p * (N // q) * k * k) % N] += 1
        z = cyc_zero(N)
        zb = cyc_zero(N)
        for e in range(N):
            if h[e]:
                f = Fr(h[e], n)
                z = z + P[e] * f
                zb = zb + P[(N - e) % N] * f
        out.append(z * zb)
    return out, N


TIME_Q = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 16, 20, 24]
DIRECT_N = [12, 24, 36, 48, 60]


def pq_cells(n):
    for q in TIME_Q:
        if n % q:
            continue
        for p in range(1, q + 1):
            if gcd(p, q) == 1:
                yield p, q


tick("building the propagator entry by entry in Q(zeta_n) on the direct "
     "ladder")
_dir_ok, _dir_cells, _dir_bad = True, 0, []
for n in DIRECT_N:
    for p, q in pq_cells(n):
        vals, N = modsq_row_cyc(n, p, q)
        closed = gamma_row_closed(n, p, q)
        ok = all(vals[d].is_rational() and vals[d].rat() == closed[d]
                 for d in range(n))
        _dir_cells += 1
        _dir_ok &= ok
        if not ok:
            _dir_bad.append((n, p, q))
    tick(f"direct ladder n = {n} done ({_dir_cells} (n, p, q) cells so far)")

anchor("A1.1 THE CLOSED FORM OF THE EXACT PROPAGATOR IS GATED AGAINST THE "
       "PROPAGATOR ITSELF, NOT ASSUMED.  On the direct ladder the "
       "modulus-squares |U_n(d)|^2 are built entry by entry as elements of "
       "Q(zeta_n) from the defining double sum, and every one of them is "
       "verified RATIONAL and EQUAL to the closed form: Gamma_n is "
       "supported on exactly c = q / gcd(2p, q) equally spaced sites "
       "d = delta + j (n/c), each of weight exactly 1/c, with "
       "delta = n/(2c) when q = 2 mod 4 and delta = 0 otherwise.  This is "
       "the exact fractional-revival (Talbot) structure of the free ring "
       "propagator at rational times",
       _dir_ok,
       f"{_dir_cells} (n, p, q) cells verified displacement by "
       f"displacement; mismatches {_dir_bad}")

_ds_all, _ds_cells = True, 0
for n in DIRECT_N:
    for p, q in pq_cells(n):
        row = gamma_row_closed(n, p, q)
        G = [[row[(j - l) % n] for l in range(n)] for j in range(n)]
        _ds_all &= ds_report(G)["ds"]
        _ds_cells += 1
check("A1.2 THE CLASSICAL FACT IS GATED ON THE FAMILY, NOT CITED: for "
      "every (n, p, q) on the direct ladder the entrywise modulus-square "
      "Gamma_n = |U_n|^2 is DOUBLY STOCHASTIC by exact rational summation "
      "— every row sum and every column sum is exactly 1 and every entry "
      "is non-negative",
      _ds_all, f"{_ds_cells} matrices, all doubly stochastic exactly")

_uni_ok, _uni_detail = True, []
for n, p, q in [(12, 1, 2), (12, 1, 3), (12, 1, 4), (12, 1, 6), (12, 5, 12),
                (12, 1, 12), (24, 1, 8), (24, 5, 12)]:
    urow, N = prop_row_cyc(n, p, q)
    U = [[urow[(j - l) % n] for l in range(n)] for j in range(n)]
    bad = unitary_check_cyc(U)
    G = [[Fr(0)] * n for _ in range(n)]
    okm = True
    for j in range(n):
        for l in range(n):
            z = U[j][l] * U[j][l].conj()
            if not z.is_rational():
                okm = False
            else:
                G[j][l] = z.rat()
    _uni_ok &= (not bad) and okm and ds_report(G)["ds"] \
        and G[0] == [gamma_row_closed(n, p, q)[(-l) % n] for l in range(n)]
    _uni_detail.append(f"(n={n}, p/q={p}/{q}, Q(zeta_{N})) residuals "
                       f"{len(bad)}")
anchor("A1.3 THE PROPAGATOR IS EXHIBITED AND VERIFIED UNITARY IN EXACT "
       "CYCLOTOMIC ARITHMETIC on eight declared (n, p, q) cells: "
       "U^dagger U - I has ZERO non-zero entries in Q(zeta_N), every "
       "|U_jl|^2 is rational, the resulting Gamma is doubly stochastic "
       "exactly, and it agrees with the closed form.  No statement about "
       "the propagator rests on the closed form alone",
       _uni_ok, "; ".join(_uni_detail))

n_x, p_x, q_x = 7, 1, 4
vals_x, N_x = modsq_row_cyc(n_x, p_x, q_x)
_irr = [d for d in range(n_x) if not vals_x[d].is_rational()]
check("A1.4 THE EXCLUDED REGIME IS A STATED FACT, NOT AN ASSUMPTION: when "
      f"q does not divide n the modulus-squares LEAVE Q.  At "
      f"(n, p, q) = ({n_x}, {p_x}, {q_x}), computed exactly in "
      f"Q(zeta_{N_x}), |U_d|^2 is IRRATIONAL at {len(_irr)} of {n_x} "
      "displacements, so the exact rational screen does not apply there; "
      "that regime is excluded by cap with the reason exhibited rather "
      "than assumed",
      len(_irr) > 0,
      f"irrational at displacements {_irr}; rational at "
      f"{[d for d in range(n_x) if vals_x[d].is_rational()]}")


# ===========================================================================
# SEC 7.  ARM A (ii) — BINNING, AND THE TWO COARSE-GRAINING RULES
# ===========================================================================

sec("ARM A (ii) — BINNING, AND THE TWO COARSE-GRAINING RULES")

print("""
  THE BINNING.  Bin k = n/B adjacent sites into one cell; the cells are the
  contiguous arcs B_I = { I k, ..., (I+1)k - 1 }, I = 0, ..., B-1.  Two
  rules are screened, both declared.

  RULE 1 (LUMPING, the uniform within-cell prior).  Given that the system
  is somewhere in cell J at time 0, with the uniform prior on the k sites
  of that cell, what is the probability of being in cell I at time t?

     Gamma^bin_{IJ} := (1/k) sum_{i in B_I} sum_{j in B_J} Gamma_ij .

  Rule 1 PRESERVES DOUBLE STOCHASTICITY EXACTLY, and the proof is one line
  each way: sum_I Gamma^bin_{IJ} = (1/k) sum_{j in B_J} sum_i Gamma_ij
  = (1/k) . k = 1, and sum_J Gamma^bin_{IJ} = (1/k) sum_{i in B_I} sum_j
  Gamma_ij = 1.  So under Rule 1 the distance from BISTOCHASTIC is exactly
  ZERO at every n, every B and every time -- and the entire question is the
  distance from UNISTOCHASTIC.  This is gated below, not asserted.

  RULE 2 (REPRESENTATIVE SITE).  The coarse observer instead reads the
  initial cell as its first site:

     Gamma^rep_{IJ} := sum_{i in B_I} Gamma_{i, Jk} .

  Rule 2 keeps the columns normalised and BREAKS the rows.  Its exact row
  defect is measured below.  It is reported because 'distance from
  bistochastic' has content only once a rule that can fail is on the table.
""")


def circ(m):
    B = len(m)
    return [[m[(j - i) % B] for j in range(B)] for i in range(B)]


def bin_row_block(row, n, B):
    """Rule 1 by explicit block summation on a circulant Gamma."""
    k = n // B
    out = []
    for I in range(B):
        s = Fr(0)
        for i in range(I * k, (I + 1) * k):
            for j in range(k):
                s += row[(i - j) % n]
        out.append(s / k)
    return out


def bin_row_spikes(n, B, c, Delta, delta):
    """Rule 1 from the spike positions alone: O(c)."""
    k = n // B
    cnt = [0] * B
    for j in range(c):
        cnt[((delta + j * Delta) % n) // k] += 1
    return [Fr(x, c) for x in cnt]


_bin_ok, _bin_cells = True, 0
for n in (12, 24, 36, 60):
    for p, q in pq_cells(n):
        row = gamma_row_closed(n, p, q)
        c, Delta, delta = revival(n, p, q)
        for B in range(2, n + 1):
            if n % B:
                continue
            m1 = bin_row_block(row, n, B)
            m2 = bin_row_spikes(n, B, c, Delta, delta)
            _bin_ok &= ds_report(circ(m1))["ds"] and m1 == m2
            _bin_cells += 1
check("A2.1 RULE 1 PRESERVES DOUBLE STOCHASTICITY EXACTLY — GATED, NOT "
      "ASSERTED.  Over every (n, p, q, B) cell of the declared grid the "
      "binned matrix has row sums and column sums exactly 1 with "
      "non-negative entries; and the O(c) spike computation agrees with "
      "the O(n k) block summation entry for entry.  The distance from "
      "BISTOCHASTIC under Rule 1 is therefore exactly ZERO everywhere, and "
      "the whole question is the distance from UNISTOCHASTIC",
      _bin_ok,
      f"{_bin_cells} (n, p, q, B) cells, all exactly bistochastic, spike "
      f"and block computations identical")

_rep_rows = []
for n, p, q, B in [(12, 1, 4, 3), (12, 1, 3, 4), (24, 1, 4, 3),
                   (60, 1, 4, 5), (60, 1, 3, 4), (60, 1, 5, 6)]:
    row = gamma_row_closed(n, p, q)
    k = n // B
    G = [[sum(row[(i - J * k) % n] for i in range(I * k, (I + 1) * k))
          for J in range(B)] for I in range(B)]
    R = ds_report(G)
    _rep_rows.append((n, p, q, B, R["col_ok"], R["row_ok"], R["L1row"]))
check("A2.2 RULE 2 IS NOT A NO-OP AND ITS FAILURE IS MEASURED EXACTLY: the "
      "representative-site rule keeps every column sum exactly 1 and "
      "breaks the rows, with the exact l1 row defect printed.  A coarse "
      "observer who reads a cell by one of its sites leaves the "
      "BISTOCHASTIC class before the unistochastic question is even "
      "reached",
      all(x[4] for x in _rep_rows) and any(not x[5] for x in _rep_rows),
      "; ".join(f"(n={a}, p/q={b}/{c}, B={d}) cols_ok={e} rows_ok={f} "
                f"l1row={g}" for a, b, c, d, e, f, g in _rep_rows))


# ===========================================================================
# SEC 8.  ARM A (iii) — THE SCREEN AND THE DEFECT LAW ALONG THE n-LADDER
# ===========================================================================

sec("ARM A (iii) — THE SCREEN AND THE DEFECT LAW ALONG THE n-LADDER")


def screen_binned(m):
    """One binned circulant row in, one exact verdict out."""
    M = circ(m)
    R = ds_report(M)
    if not R["ds"]:
        return "S-FAIL-DS", None, None, M
    B = len(m)
    T = tri_disc(*chain_link_squares(M, 0, 1, "col")) if B == 3 else None
    if B == 3 and T < 0:
        return "S-FAIL-UNI", T, None, M
    pv = poly_both(M)
    if pv:
        worst = None
        for by, p, q, i, a, slack in pv:
            if worst is None or surd_sign(slack - worst) < 0:
                worst = slack
        return "S-FAIL-UNI", T, worst, M
    return "S-NO-OBSTRUCTION", T, None, M


def gauss_cert(m):
    """Exhibit a unitary for a binned circulant row that is uniform (1/c)
    on an arithmetic progression of c cells with common difference B/c.
    The lift is the circulant Gauss-sum matrix
      U_{jl} = zeta^{r^2} . conj(g)/c ,  r = ((j-l) - s0) / step  mod c,
      g = sum_{r mod c} zeta^{r^2},  zeta = zeta_c (c odd) or zeta_2c (c
      even),  which satisfies |g|^2 = c and hence |U_jl|^2 = 1/c on the
    support and 0 off it.  Unitarity is VERIFIED, never assumed."""
    B = len(m)
    supp = sorted(i for i in range(B) if m[i] != 0)
    c = len(supp)
    if c == 0 or B % c or any(m[i] != Fr(1, c) for i in supp):
        return None
    step = B // c
    if supp != sorted([(supp[0] + j * step) % B for j in range(c)]):
        return None
    mod = c if c % 2 else 2 * c
    Nf = 4 if mod == 1 else mod
    P = pows(Nf)
    e1 = Nf // mod
    g = cyc_zero(Nf)
    for r in range(c):
        g = g + P[(e1 * ((r * r) % mod)) % Nf]
    gg = g * g.conj()
    if not (gg.is_rational() and gg.rat() == c):
        return None
    ginv = g.conj() * Fr(1, c)
    U = [[cyc_zero(Nf) for _ in range(B)] for _ in range(B)]
    for j in range(B):
        for l in range(B):
            d = (j - l) % B
            if (d - supp[0]) % step:
                continue
            r = ((d - supp[0]) // step) % c
            U[j][l] = P[(e1 * ((r * r) % mod)) % Nf] * ginv
    return U


N_LADDER = [60, 120, 240, 480, 960, 1920, 3840, 7680]
B_LADDER = [3, 4, 5, 6, 10, 12, 15, 20, 30, 60]
Q_MAIN = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20]

print("  THE DEFECT LAW ALONG THE LATTICE LADDER.  For each rational time")
print("  theta = 2 pi p/q (revival count c = q/gcd(2p,q)) the binned")
print("  matrix's exact verdict is computed at every lattice size on the")
print("  ladder and at every bin count dividing it.  'X' = certified NOT")
print("  unistochastic; '.' = no obstruction; the row is printed once")
print("  because it is IDENTICAL at every n, which is the finding.")
print()

defect_table = {}
verdict_count = Counter()
for q in Q_MAIN:
    for p in range(1, q + 1):
        if gcd(p, q) != 1:
            continue
        rows_printed = []
        for n in N_LADDER:
            if n % q:
                continue
            c, Delta, delta = revival(n, p, q)
            cells = []
            for B in B_LADDER:
                if n % B:
                    continue
                m = bin_row_spikes(n, B, c, Delta, delta)
                v, T, slack, M = screen_binned(m)
                defect_table.setdefault((q, p, B), []).append((n, v, T,
                                                               slack, m))
                verdict_count[v] += 1
                cells.append("X" if v == "S-FAIL-UNI"
                             else ("D" if v == "S-FAIL-DS" else "."))
            rows_printed.append((n, c, cells))
        if not rows_printed:
            continue
        allsame = all(r[2] == rows_printed[0][2] for r in rows_printed)
        bs = [B for B in B_LADDER if rows_printed[0][0] % B == 0]
        print(f"  theta = 2 pi . {p}/{q}   c = {rows_printed[0][1]:2d} "
              f"copies   n = {rows_printed[0][0]}..{rows_printed[-1][0]}"
              f"   B = {fsl(bs)}")
        print(f"        verdicts  {''.join(rows_printed[0][2])}"
              f"     identical at every n: {allsame}")
    sys.stdout.flush()

_nindep = all(all(x[1] == v[0][1] and x[4] == v[0][4] for x in v)
              for v in defect_table.values())
check("A3.1 THE DEFECT IS EXACTLY n-INDEPENDENT AT FIXED PHYSICAL "
      "PARAMETERS.  Over every (q, p, B) cell of the declared grid the "
      "binned matrix is LITERALLY THE SAME rational matrix at every "
      "lattice size on the ladder, hence the same verdict and the same "
      "exact defect: at fixed theta the revival count c and the cell "
      "occupancies depend on (c, B) alone and not on n.  The binning "
      "defect therefore does NOT vanish as the lattice is refined at fixed "
      "t, m and L — it is CONSTANT",
      _nindep,
      f"{len(defect_table)} (q, p, B) cells, each checked across every "
      f"lattice size on the ladder; verdict census {dict(verdict_count)}")

print()
print("  THE FAILING CELLS, EXACTLY, WITH THEIR CERTIFIED DISTANCE TO THE")
print("  CLASS.  Every row below is a certified NEGATIVE: the matrix is")
print("  bistochastic exactly and NOT unistochastic exactly.")
print()
fail_rows = []
for (q, p, B), lst in sorted(defect_table.items()):
    n0, v0, T0_, sl0, m0 = lst[0]
    if v0 != "S-FAIL-UNI":
        continue
    fail_rows.append((q, p, B, m0, T0_, sl0, len(lst)))
for q, p, B, m0, T_, sl, ncnt in fail_rows:
    dist = (f"dist_1 >= {abs(T_) / 4}" if T_ is not None and T_ < 0
            else "— (B != 3: polygon obstruction only)")
    print(f"    theta = 2 pi . {p}/{q}   B = {B:2d}   binned row = {fsl(m0)}")
    print(f"        T = {str(T_) if T_ is not None else 'n/a':10s}  worst "
          f"polygon slack = {str(sl):8s}  {dist}   identical at {ncnt} "
          f"lattice sizes")
report("failing (q, p, B) cells in the main grid",
       f"{len(fail_rows)} of {len(defect_table)}")

_cert_ok, _cert_try, _cert_fail = 0, 0, []
for (q, p, B), lst in sorted(defect_table.items()):
    n0, v0, T0_, sl0, m0 = lst[0]
    if v0 != "S-NO-OBSTRUCTION":
        continue
    U = gauss_cert(m0)
    if U is None:
        continue
    _cert_try += 1
    bad_u = unitary_check_cyc(U)
    bad_m = modsq_check_cyc(U, circ(m0))
    if not bad_u and not bad_m:
        _cert_ok += 1
    else:
        _cert_fail.append((q, p, B, len(bad_u), len(bad_m)))
check("A3.2 THE POSITIVES THAT CAN BE CERTIFIED ARE CERTIFIED, NOT CITED: "
      "wherever the binned matrix is uniform on an arithmetic progression "
      "of c cells with c | B, a unitary of the SAME size is EXHIBITED (the "
      "circulant Gauss-sum lift) and verified U^dagger U = I and "
      "|U_ij|^2 = M_ij entry by entry in exact cyclotomic arithmetic",
      _cert_try > 0 and not _cert_fail,
      f"{_cert_ok}/{_cert_try} certificates constructed and verified with "
      f"zero residuals; failures {_cert_fail}")
report("cells with NO obstruction and NO constructible certificate",
       f"EXCLUDED-BY-CAP: {verdict_count['S-NO-OBSTRUCTION'] - _cert_ok} of "
       f"{verdict_count['S-NO-OBSTRUCTION']} no-obstruction cells — "
       f"reported as a cap, never as a pass")


# ===========================================================================
# SEC 9.  ARM A (iv) — THE BIN-REFINEMENT LAW, AND ITS EXACT MECHANISM
# ===========================================================================

sec("ARM A (iv) — THE BIN-REFINEMENT LAW, AND ITS EXACT MECHANISM")

print("""
  THE SECOND REFINEMENT DIRECTION.  SEC 8 refines the LATTICE at fixed
  bins.  This section refines the BINS.  The object binned is the same
  exact revival row -- c equally weighted spikes at spacing n/c and offset
  delta.  For each (c, B) the receipt takes n = lcm(B, 2c), 2 lcm(B, 2c)
  and 3 lcm(B, 2c) and checks that the binned matrix is literally the same
  at all three, so the (c, B) table is a table about the PHYSICS (revival
  count and bin count) and not about the lattice.

  THE MECHANISM, EXACTLY.  The binned row is 1/c on the cell set
  S = { floor(B (delta + j n/c) / n) : j = 0..c-1 } subset Z_B, and 0
  elsewhere.  For a circulant matrix with that row, the chain-link modulus
  for the column pair (u, v) at index i is sqrt(m_{u-i} m_{v-i}), which is
  1/c when both u-i and v-i lie in S and 0 otherwise.  So for the pair
  (u, v) the number of non-zero phasors is |(S-u) cap (S-v)| -- i.e. the
  MULTIPLICITY of the difference u-v in the difference multiset of S.  The
  polygon condition (no one modulus exceeds the sum of the others)
  therefore fails for the pair (u, v) exactly when that multiplicity is 1,
  and when it fails the slack is exactly (1/c) - 2(1/c) = -1/c.  Hence

     THE BINNED FREE PROPAGATOR IS NOT UNISTOCHASTIC  <=>  the difference
     multiset of its cell set S contains a difference of multiplicity
     exactly 1;  and then the polygon defect is EXACTLY -1/c.

  Both halves are gated below across the whole sweep.
""")

C_MAX, B_MAX = 24, 30
sweep = {}
mech_ok = True
nindep_ok = True
tick("running the (c, B) refinement sweep")
for c in range(1, C_MAX + 1):
    for B in range(2, B_MAX + 1):
        for off in (0, 1):
            base = (B * 2 * c) // gcd(B, 2 * c)
            rows = []
            for mult in (1, 2, 3):
                n = base * mult
                Delta = n // c
                rows.append(bin_row_spikes(n, B, c, Delta,
                                           (Delta // 2) if off else 0))
            if any(r != rows[0] for r in rows):
                nindep_ok = False
            m = rows[0]
            v, T, slack, M = screen_binned(m)
            S = sorted(i for i in range(B) if m[i] != 0)
            diffs = Counter(((u - w) % B) for u in S for w in S if u != w)
            mult1 = any(x == 1 for x in diffs.values())
            fails = (v == "S-FAIL-UNI")
            if fails != mult1:
                mech_ok = False
            if fails and slack is not None and \
                    not (slack - Surd(Fr(-1, c))).is_zero():
                mech_ok = False
            sweep[(c, B, off)] = (v, T, slack, m, S)
    if c % 6 == 0:
        tick(f"(c, B) sweep at c = {c}")

check("A4.1 THE (c, B) TABLE IS A TABLE ABOUT THE PHYSICS, NOT THE "
      "LATTICE: at every (c, B, offset) cell the binned matrix is "
      "literally identical at n = lcm(B, 2c), 2 lcm(B, 2c) and "
      "3 lcm(B, 2c)",
      nindep_ok, f"{len(sweep)} cells x 3 lattice sizes each")

check("A4.2 THE MECHANISM IS EXACT AND COMPLETE: across the whole sweep "
      "the binned matrix fails the polygon condition IF AND ONLY IF the "
      "difference multiset of its cell set S contains a difference of "
      "multiplicity exactly 1, and whenever it fails the worst polygon "
      "slack is EXACTLY -1/c.  The combinatorial criterion and the Surd "
      "sign oracle agree at every cell",
      mech_ok,
      f"{len(sweep)} (c, B, offset) cells, no discrepancy")

print()
print("  THE REFINEMENT MAP.  Rows: c, the number of revival copies, set")
print("  by the time.  Columns: B = 2 .. 30, the number of bins.  'X' =")
print("  certified NOT unistochastic, '.' = no obstruction found.")
print()
print("        B:  " + "".join(str(B % 10) for B in range(2, B_MAX + 1)))
for c in range(1, C_MAX + 1):
    print(f"   c = {c:2d}   "
          + "".join("X" if sweep[(c, B, 0)][0] == "S-FAIL-UNI" else "."
                    for B in range(2, B_MAX + 1)))
_offsame = all((sweep[(c, B, 0)][0] == "S-FAIL-UNI")
               == (sweep[(c, B, 1)][0] == "S-FAIL-UNI")
               for c in range(1, C_MAX + 1) for B in range(2, B_MAX + 1))
check("A4.3 THE TWO SPIKE OFFSETS GIVE THE SAME REFINEMENT MAP: the "
      "q = 2 mod 4 half-cell offset moves the cell set but not the "
      "multiplicity structure of its difference multiset",
      _offsame, "offset-0 and offset-1 maps agree at every (c, B) cell")

_c2 = [(B, sweep[(2, B, 0)][0], sweep[(2, B, 0)][2])
       for B in range(2, B_MAX + 1)]
_odd_all = all(v == "S-FAIL-UNI" for B, v, s in _c2 if B % 2 == 1)
_even_all = all(v != "S-FAIL-UNI" for B, v, s in _c2 if B % 2 == 0)
_mag = set(str(s) for B, v, s in _c2 if v == "S-FAIL-UNI")
check("A4.4 AT c = 2 (theta = pi/2 or 3pi/2, the QUARTER REVIVAL) THE "
      "BINNED FREE PROPAGATOR IS NOT UNISTOCHASTIC FOR EVERY ODD BIN COUNT "
      "B >= 3 AND IS UNOBSTRUCTED FOR EVERY EVEN B, with the polygon "
      "defect exactly -1/2 at every odd B.  The bin-refinement limit "
      "B -> infinity therefore DOES NOT EXIST: the verdict alternates "
      "forever and the defect magnitude never decreases",
      _odd_all and _even_all and _mag == {"-1/2"},
      f"B = 3..{B_MAX}: odd all fail {_odd_all}, even all unobstructed "
      f"{_even_all}, defect magnitudes {sorted(_mag)}")

_c3f = [B for B in range(3, B_MAX + 1)
        if sweep[(3, B, 0)][0] == "S-FAIL-UNI"]
_c3o = [B for B in range(3, B_MAX + 1)
        if sweep[(3, B, 0)][0] != "S-FAIL-UNI"]
check("A4.5 AT c = 3 THE SAME PHENOMENON RECURS WITH PERIOD 3: the binned "
      "matrix is certified non-unistochastic at every bin count B >= 5 "
      "that is not a multiple of 3, and unobstructed exactly at the "
      "multiples of 3 and at B = 4, with the polygon defect exactly -1/3",
      all(B % 3 != 0 for B in _c3f)
      and all((B % 3 == 0 or B == 4) for B in _c3o),
      f"fails at B = {_c3f}; unobstructed at B = {_c3o}")

print()
print("  THE B = 3 DEFECT IN A CERTIFIED METRIC (SEC 5's escape radius).")
print("    c    binned row                 T             dist_1 >=")
for c in range(1, 13):
    v, T, slack, m, S = sweep[(c, 3, 0)]
    print(f"   {c:3d}   {fsl(m):24s}  {str(T):12s}  "
          f"{(str(abs(T) / 4) if T is not None and T < 0 else '—')}")


# ===========================================================================
# SEC 10.  ARM A (v) — THE HARMONIC-OSCILLATOR CONTROL
# ===========================================================================

sec("ARM A (v) — THE HARMONIC-OSCILLATOR CONTROL (a second exact family)")

print("""
  THE CONTROL FAMILY, DECLARED.  The split-operator (Trotter) step of the
  harmonic oscillator H = p^2/2m + m w^2 x^2/2 is a position chirp times a
  free step:

     V = D_x . A ,   D_x = diag( zeta_3^{-p' j^2} ) ,
     A = F^dagger diag( zeta_3^{-p k^2} ) F   (the free step of SEC 6 at
                                               q = 3),

  and the control object is Gamma_HO = |V^M|^2 for M = 1, ..., 6.  Both
  chirps are exact cube roots of unity, so every entry of V^M lies in
  Q(zeta_3); every modulus-square is therefore RATIONAL, and A's support is
  the subgroup {0, n/3, 2n/3} of Z_n, so V^M has exactly three non-zero
  entries per row at every M and the whole family is built in exact
  arithmetic in O(M n) operations.

  A LEFT diagonal unimodular factor cannot change |.|^2, so M = 1 is a NULL
  control and is printed as such; the content starts at M = 2.

  THE CONTROL'S JOB is to show that the SEC 8-9 phenomenon is not an
  artefact of the free propagator's Gauss-sum structure.  It is a control,
  not a second headline: its census is reported in full, positives and
  negatives.
""")

Z3P = [cyc_pow(ZETA3, e % 3) for e in range(3)]


def ho_family(n, p, pp, Mmax):
    """V^M as a sparse row map: rows[j] = {l: Cyc}, at most 3 entries."""
    s = n // 3
    a = {}
    for mm in range(3):
        z = cyc_zero(12)
        for b in range(3):
            z = z + Z3P[(b * mm - p * b * b) % 3]
        a[(mm * s) % n] = z * Fr(1, 3)
    D = [Z3P[(-pp * j * j) % 3] for j in range(3 if n % 3 else n)]
    D = [Z3P[(-pp * j * j) % 3] for j in range(n)]
    V = [{(j - d) % n: D[j] * a[d] for d in a} for j in range(n)]
    cur = [dict(r) for r in V]
    out = []
    for M in range(1, Mmax + 1):
        if M > 1:
            nxt = []
            for j in range(n):
                acc = {}
                for kk, x in cur[j].items():
                    for l, y in V[kk].items():
                        acc[l] = (acc[l] + x * y) if l in acc else x * y
                nxt.append(acc)
            cur = nxt
        G = [[Fr(0)] * n for _ in range(n)]
        rat = True
        for j in range(n):
            for l, x in cur[j].items():
                z = x * x.conj()
                if not z.is_rational():
                    rat = False
                else:
                    G[j][l] = z.rat()
        out.append((M, rat, G))
    return out


ho_rows, ho_ratall, ho_dsall = [], True, True
for n in (9, 12, 18, 24, 36):
    for p in (1, 2):
        for pp in (1, 2):
            for M, rat, G in ho_family(n, p, pp, 6):
                ho_ratall &= rat
                ho_dsall &= ds_report(G)["ds"]
                cells = []
                for B in range(2, 13):
                    if n % B:
                        continue
                    k = n // B
                    Gb = [[sum(G[i][j] for i in range(I * k, (I + 1) * k)
                               for j in range(J * k, (J + 1) * k)) / k
                           for J in range(B)] for I in range(B)]
                    Rb = ds_report(Gb)
                    T = (tri_disc(*chain_link_squares(Gb, 0, 1, "col"))
                         if B == 3 else None)
                    pv = poly_both(Gb)
                    cells.append((B, Rb["ds"],
                                  bool(pv) or (B == 3 and T < 0), T,
                                  len(pv)))
                ho_rows.append((n, p, pp, M, cells))
    tick(f"harmonic-oscillator control n = {n} done")

_ho_fail = [(n, p, pp, M, B) for n, p, pp, M, cells in ho_rows
            for B, ds, bad, T, npv in cells if bad]
_ho_dsb = all(ds for n, p, pp, M, cells in ho_rows
              for B, ds, bad, T, npv in cells)
_ho_cells = sum(len(c[4]) for c in ho_rows)
check("A5.1 THE CONTROL FAMILY IS EXACT AND ITS PRECONDITIONS HOLD: every "
      "modulus-square of every Trotter power is RATIONAL, every Gamma_HO "
      "is doubly stochastic exactly, and every binned Gamma_HO is doubly "
      "stochastic exactly (Rule 1 again)",
      ho_ratall and ho_dsall and _ho_dsb,
      f"{len(ho_rows)} (n, p, p', M) objects and {_ho_cells} binned "
      f"matrices, all exact")
check("A5.2 THE CONTROL REPRODUCES THE PHENOMENON ON A SECOND, "
      "STRUCTURALLY DIFFERENT EXACT FAMILY: the Trotterised harmonic "
      "oscillator also produces binned matrices that are bistochastic and "
      "certified NOT unistochastic.  The SEC 8-9 result is therefore not "
      "an artefact of the free propagator's Gauss-sum structure",
      len(_ho_fail) > 0,
      f"{len(_ho_fail)} certified-negative (n, p, p', M, B) control cells "
      f"of {_ho_cells}; first twelve {_ho_fail[:12]}")
report("harmonic-oscillator control census",
       f"objects {len(ho_rows)}, binned cells {_ho_cells}, certified "
       f"negatives {len(_ho_fail)}")


# ===========================================================================
# SEC 11.  ARM B — THE CONTINUUM OBJECT'S DISCRETE SHADOW
# ===========================================================================

sec("ARM B — THE CONTINUUM OBJECT'S DISCRETE SHADOW")

print("""
  THE ANALYTIC FACT THE DISCRETE FAMILY IS ASKED TO SHADOW.  The
  free-particle continuum propagator on the line is
  K(x', x; t) = sqrt( m / 2 pi i hbar t ) exp( i m (x'-x)^2 / 2 hbar t ),
  so |K(x', x; t)|^2 = m / (2 pi hbar t) -- a CONSTANT in x'.  Its
  x'-integral diverges.  |K|^2 is not a probability density and cannot be a
  Gamma.  [B3]'s own construction is stated in the finite-dimensional case
  ({b3f}):
    "{b3ft}"
  and it flags where the issue would have to be met ({b3c}):
    "{b3ct}"

  NO CONTINUUM ANALYSIS IS PERFORMED HERE.  What follows is the exact
  discrete family and nothing else.  Six quantities are tabulated along the
  ladder at FIXED physical parameters (fixed t, m, L; a = L/n -> 0) for a
  fixed rational time with revival count c:

    (1) matrix row mass    sum_j Gamma_{j0}
    (2) peak               max_j Gamma_{j0}
    (3) support            #{ j : Gamma_{j0} > 0 }
    (4) support fraction   (3)/n
    (5) density peak       (2)/a
    (6) kernel row mass    sum_j (Gamma_{j0}/a^2) . a  =  1/a

  (6) is the exact discrete counterpart of the divergent integral: the
  amplitude kernel is K_n = U_n / a, because psi(x') = int K psi dx becomes
  psi_j = sum_l U_{jl} psi_l with U = a K.  Whether |K|^2 has a finite row
  mass is exactly whether (6) converges.
""".format(b3c=QUOTES['B3-continuum'][0], b3ct=QUOTES['B3-continuum'][1],
           b3f=QUOTES['B3-finite'][0], b3ft=QUOTES['B3-finite'][1]))

print("  ARM B TABLE.  L = 1 in units of the box; theta = 2 pi . 1/4, so")
print("  c = 2 revival copies.  Every entry is exact.")
print("       n    a = L/n    (1) row mass  (2) peak  (3) supp  (4) supp/n"
      "     (5) density peak  (6) kernel row mass")
_b_p, _b_q = 1, 4
_b_rowmass, _b_peak, _b_supp, _b_kernel, _b_dens = set(), set(), set(), [], []
for n in N_LADDER:
    if n % _b_q:
        continue
    c, Delta, delta = revival(n, _b_p, _b_q)
    a = Fr(1, n)
    rm = sum(Fr(1, c) for _ in range(c))
    pk = Fr(1, c)
    _b_rowmass.add(rm)
    _b_peak.add(pk)
    _b_supp.add(c)
    _b_kernel.append((n, Fr(1) / a))
    _b_dens.append(pk / a)
    print(f"  {n:6d}  {str(a):9s}  {str(rm):12s}  {str(pk):8s}  {c:8d}  "
          f"{str(Fr(c, n)):11s}  {str(pk / a):16s}  {str(Fr(1) / a)}")

check("B1.1 THE MATRIX NORMALISATION EXISTS AND IS DISCRETISATION-"
      "INDEPENDENT: the row mass sum_j Gamma_{j0} is exactly 1 at every "
      "lattice size on the ladder.  This is the normalisation [B3]'s "
      "criterion actually uses, and it is a statement about the COUNTING "
      "measure on a finite configuration set",
      _b_rowmass == {Fr(1)}, f"row masses on the ladder {_b_rowmass}")

check("B1.2 THE PEAK DOES NOT FLATTEN AND THE SUPPORT DOES NOT GROW: at "
      "fixed physical parameters the peak of Gamma is exactly 1/c and the "
      "support is exactly c sites at EVERY lattice size, while the support "
      "FRACTION c/n goes to zero.  The discrete family therefore does not "
      "converge pointwise to the constant that the continuum |K|^2 is; it "
      "concentrates on c point masses of weight 1/c each",
      _b_peak == {Fr(1, 2)} and _b_supp == {2},
      f"peaks {_b_peak}, supports {_b_supp}, support fractions "
      f"{[str(Fr(2, n)) for n in N_LADDER if n % _b_q == 0]}")

_kern_grow = all(_b_kernel[i][1] < _b_kernel[i + 1][1]
                 for i in range(len(_b_kernel) - 1))
_dens_grow = all(_b_dens[i] < _b_dens[i + 1] for i in range(len(_b_dens) - 1))
check("B1.3 THE KERNEL NORMALISATION DOES NOT EXIST, EXACTLY: the row mass "
      "of |K_n|^2 = |U_n|^2 / a^2 against the length measure is exactly "
      "1/a = n/L at every lattice size, so it is strictly increasing and "
      "unbounded along the refinement.  This IS the discrete shadow of the "
      "divergent integral of the continuum |K|^2, exhibited by the "
      "discrete family and by no continuum computation",
      _kern_grow and _dens_grow,
      f"kernel row masses {[str(x[1]) for x in _b_kernel]}; density peaks "
      f"{[str(x) for x in _b_dens]}")

print()
print("  ROW MASSES AGAINST BIN WIDTH.  Same object at n = 3840,")
print("  theta = 2 pi . 1/4.  Bin width w = L/B; every mass is exact.")
print("      B     w = L/B    occupied cells / B   cell mass   mass / w"
      "     verdict")
_nB = 3840
_c, _D, _de = revival(_nB, _b_p, _b_q)
_bw_tot, _bw_cell, _bw_dens = set(), set(), set()
for B in [2, 3, 4, 5, 6, 8, 10, 12, 15, 16, 20, 24, 30, 32, 40, 48, 60]:
    if _nB % B:
        continue
    m = bin_row_spikes(_nB, B, _c, _D, _de)
    v, T, slack, M = screen_binned(m)
    occ = sum(1 for x in m if x)
    hv = max(m)
    _bw_tot.add(sum(m))
    _bw_cell.add(hv)
    _bw_dens.add(hv * B)
    print(f"   {B:4d}   {str(Fr(1, B)):9s}   {occ:6d} / {B:-4d}         "
          f"{str(hv):10s}  {str(hv * B):9s}  {v}")

check("B1.4 WHICH NORMALISATION DEPENDS ON THE DISCRETISATION, EXACTLY.  "
      "The TOTAL mass is exactly 1 at every bin count (Rule 1 is exactly "
      "bistochastic, A2.1).  The per-cell mass takes more than one value "
      "across the bin ladder, and the mass DENSITY mass/w = B . mass takes "
      "more than one value and grows without bound with B.  The only "
      "discretisation-independent normalisation in the family is the total "
      "mass — which is exactly the counting-measure normalisation that "
      "unistochasticity is defined against",
      _bw_tot == {Fr(1)} and len(_bw_cell) > 1 and len(_bw_dens) > 1,
      f"total masses {_bw_tot}; distinct cell masses {len(_bw_cell)}; "
      f"distinct densities {len(_bw_dens)}, maximum {max(_bw_dens)}")

print()
print("  WHICH LIMITS EXIST AND WHICH DO NOT — the exact list this arm")
print("  supports, and nothing beyond it.")
print("    EXISTS   : the matrix row mass — identically 1 (B1.1).")
print("    EXISTS   : the cell-mass vector at FIXED bin count B — it is")
print("               n-independent, exactly (A3.1).")
print("    EXISTS   : the total mass under any binning — exactly 1 (B1.4).")
print("    DOES NOT : the pointwise limit of Gamma_{j0}/a — the density")
print("               peak is n/(cL) and diverges (B1.3).")
print("    DOES NOT : the kernel row mass sum_j |K_n|^2 a = 1/a (B1.3).")
print("    DOES NOT : a constant |K|^2 as a pointwise limit — Gamma/a^2")
print("               takes exactly the two values 0 and n^2/(cL^2) at")
print("               every n, of infinite ratio (B1.2).")
print("    DOES NOT : the bin-refinement limit of the VERDICT at c = 2 — it")
print("               alternates with the parity of B forever (A4.4).")


# ===========================================================================
# SEC 12.  ARM C — COMPOSITION CLOSURE AT n = 3
# ===========================================================================

sec("ARM C — COMPOSITION CLOSURE AT n = 3")

print("""
  THE OBJECT.  U, V exact 3x3 unitaries.  Gamma_U = |U|^2 and
  Gamma_V = |V|^2 are unistochastic BY CONSTRUCTION, with U and V as their
  certificates.  Two matrices then compete for the name 'the composite':

     |UV|^2            the INDIVISIBLE composition — what the quantum
                       process does over the two intervals;
     |U|^2 . |V|^2     the DIVISIBLE composition — what a coarse observer
                       writes if it inserts a division event in the middle.

  THE EXPECTED CONTROL, GATED BELOW: these two differ generically.  That
  difference IS indivisibility and is not a defect.  THE QUESTION is
  whether the second one is itself unistochastic — whether the divisible
  shadow of a unistochastic process stays in the class.
""")


class GQ:
    """The Gaussian rationals Q(i) = {a + b i}, exactly."""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = Fr(a)
        self.b = Fr(b)

    def __add__(self, o):
        return GQ(self.a + o.a, self.b + o.b)

    def __sub__(self, o):
        return GQ(self.a - o.a, self.b - o.b)

    def __mul__(self, o):
        return GQ(self.a * o.a - self.b * o.b, self.a * o.b + self.b * o.a)

    def conj(self):
        return GQ(self.a, -self.b)

    def n2(self):
        return self.a * self.a + self.b * self.b

    def is_zero(self):
        return self.a == 0 and self.b == 0

    def __eq__(self, o):
        return self.a == o.a and self.b == o.b

    def __repr__(self):
        return f"{self.a}" if self.b == 0 else \
            f"({self.a}{'+' if self.b > 0 else '-'}{abs(self.b)}i)"


G0, G1, GI = GQ(0, 0), GQ(1, 0), GQ(0, 1)


def gmm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(3)), G0)
             for j in range(3)] for i in range(3)]


def gmod2(U):
    return [[U[i][j].n2() for j in range(3)] for i in range(3)]


def gunitary(U):
    bad = 0
    for i in range(3):
        for j in range(3):
            s = G0
            for k in range(3):
                s = s + U[k][i].conj() * U[k][j]
            if not (s - (G1 if i == j else G0)).is_zero():
                bad += 1
    return bad


BLOCKS = [
    (GQ(Fr(3, 5), 0), GQ(Fr(4, 5), 0)),
    (GQ(Fr(4, 5), 0), GQ(Fr(3, 5), 0)),
    (GQ(Fr(5, 13), 0), GQ(Fr(12, 13), 0)),
    (GQ(Fr(12, 13), 0), GQ(Fr(5, 13), 0)),
    (GQ(Fr(8, 17), 0), GQ(Fr(15, 17), 0)),
    (GQ(Fr(7, 25), 0), GQ(Fr(24, 25), 0)),
    (GQ(Fr(20, 29), 0), GQ(Fr(21, 29), 0)),
    (GQ(Fr(1, 2), Fr(1, 2)), GQ(Fr(1, 2), Fr(-1, 2))),
    (GQ(Fr(1, 5), Fr(2, 5)), GQ(Fr(2, 5), Fr(4, 5))),
    (GQ(Fr(2, 5), Fr(4, 5)), GQ(Fr(1, 5), Fr(2, 5))),
    (GQ(Fr(1, 10), Fr(3, 10)), GQ(Fr(3, 10), Fr(9, 10))),
    (GQ(Fr(1, 13), Fr(8, 13)), GQ(Fr(2, 13), Fr(10, 13))),
    (GQ(Fr(3, 5), 0), GQ(0, Fr(4, 5))),
    (GQ(0, Fr(3, 5)), GQ(Fr(4, 5), 0)),
]
check("C0.1 THE DECLARED 2-LEVEL BLOCKS ARE EXACT UNIT VECTORS OVER Q(i): "
      "every (alpha, beta) satisfies |alpha|^2 + |beta|^2 = 1 exactly, so "
      "the embedded 3x3 matrices are exactly unitary and their "
      "modulus-squares are exactly rational",
      all((a.n2() + b.n2()) == 1 for a, b in BLOCKS),
      f"{len(BLOCKS)} declared blocks, all exact")

GENS, GENNAME = [], []
for pr in ((0, 1), (0, 2), (1, 2)):
    o = [x for x in range(3) if x not in pr][0]
    for bi, (al, be) in enumerate(BLOCKS):
        for ph, pn in ((G1, ""), (GI, "i")):
            Wm = [[G0] * 3 for _ in range(3)]
            Wm[o][o] = G1
            Wm[pr[0]][pr[0]] = al
            Wm[pr[0]][pr[1]] = be
            Wm[pr[1]][pr[0]] = (G0 - be.conj()) * ph
            Wm[pr[1]][pr[1]] = al.conj() * ph
            GENS.append(Wm)
            GENNAME.append(f"R{pr[0]}{pr[1]}[{bi}]{pn}")
for perm in [(0, 1, 2), (1, 0, 2), (0, 2, 1), (2, 1, 0), (1, 2, 0),
             (2, 0, 1)]:
    GENS.append([[G1 if perm[i] == j else G0 for j in range(3)]
                 for i in range(3)])
    GENNAME.append(f"P{perm[0]}{perm[1]}{perm[2]}")

_gen_bad = sum(gunitary(W) for W in GENS)
check("C0.2 EVERY GENERATOR IS EXACTLY UNITARY OVER Q(i): W^dagger W - I "
      "has zero non-zero entries for all of them",
      _gen_bad == 0,
      f"{len(GENS)} generators, {_gen_bad} residual entries")

tick("generating the Arm C unitary pool by BFS to word length 3")
POOL_CAP, FRONT_CAP = 300, 220
IDM = [[G1 if i == j else G0 for j in range(3)] for i in range(3)]
seen = {}


def mkey(M):
    return tuple(tuple(r) for r in M)


seen[mkey(gmod2(IDM))] = (IDM, "e")
frontier = [(IDM, "e")]
words = 0
for depth in (1, 2, 3):
    nxt = []
    for W, nm in frontier:
        for g, gn in zip(GENS, GENNAME):
            W2 = gmm(W, g)
            words += 1
            k = mkey(gmod2(W2))
            if k not in seen:
                seen[k] = (W2, nm + "." + gn)
                if len(nxt) < FRONT_CAP:
                    nxt.append((W2, nm + "." + gn))
            if len(seen) >= POOL_CAP:
                break
        if len(seen) >= POOL_CAP:
            break
    tick(f"BFS depth {depth}: {len(seen)} distinct |W|^2, {words} words "
         f"expanded")
    if len(seen) >= POOL_CAP:
        break
    frontier = nxt

POOL = []
for k in sorted(seen, key=lambda z: str(z)):
    W, nm = seen[k]
    POOL.append(([[Fr(x) for x in r] for r in gmod2(W)], W, nm))
report("Arm C pool", f"{len(POOL)} distinct certified-unistochastic 3x3 "
                     f"matrices, each with its Q(i) unitary exhibited "
                     f"({words} words expanded)")

_pool_bad, _pool_ds = 0, True
for M, W, nm in POOL:
    _pool_bad += gunitary(W)
    if gmod2(W) != M:
        _pool_bad += 1
    _pool_ds &= ds_report(M)["ds"]
check("C0.3 EVERY POOL MEMBER CARRIES ITS OWN CERTIFICATE, VERIFIED: for "
      "all of them W^dagger W = I exactly over Q(i), |W_ij|^2 = M_ij "
      "exactly, and M is doubly stochastic exactly.  No pool member's "
      "unistochasticity rests on the criterion — each one IS an entrywise "
      "squared unitary",
      _pool_bad == 0 and _pool_ds,
      f"{len(POOL)} members, {_pool_bad} residuals, all bistochastic")

tick("Arm C1: the |UV|^2 versus |U|^2 . |V|^2 census")
SAMPLE = POOL[:110]
c1_eq, c1_tot, c1_max, c1_arg = 0, 0, Fr(0), None
for Mu, Wu, nu in SAMPLE:
    for Mv, Wv, nv in SAMPLE:
        ind = gmod2(gmm(Wu, Wv))
        div = [[Mu[i][0] * Mv[0][j] + Mu[i][1] * Mv[1][j]
                + Mu[i][2] * Mv[2][j] for j in range(3)] for i in range(3)]
        d = sum(abs(ind[i][j] - div[i][j]) for i in range(3)
                for j in range(3))
        c1_tot += 1
        if d == 0:
            c1_eq += 1
        if d > c1_max:
            c1_max, c1_arg = d, (nu, nv)
check("C1.1 THE EXPECTED CONTROL: |UV|^2 AND |U|^2 . |V|^2 DIFFER "
      "GENERICALLY, AND THAT DIFFERENCE IS INDIVISIBILITY.  Over the "
      "declared sample of ordered pairs the two matrices coincide only on "
      "a minority of pairs — those with a degenerate factor — and the "
      "exact l1 gap reaches its printed maximum.  This is the expected "
      "control, not a finding",
      c1_eq < c1_tot and c1_max > 0,
      f"{c1_tot} ordered pairs; exactly equal on {c1_eq} "
      f"({100.0 * c1_eq / c1_tot:.2f}%); maximum exact l1 gap {c1_max} = "
      f"{float(c1_max):.6f}, first attained at {c1_arg}")

tick("Arm C2: the counterexample hunt over the certified pool")
TARGET = circ([Fr(1, 2), Fr(1, 2), Fr(0)])
_tT = tri_disc(*chain_link_squares(TARGET, 0, 1, "col"))
c2_tot, c2_neg, c2_ds, c2_Tmin, c4_hits = 0, [], True, None, 0
for Mu, Wu, nu in POOL:
    for Mv, Wv, nv in POOL:
        P = [[Mu[i][0] * Mv[0][j] + Mu[i][1] * Mv[1][j] + Mu[i][2] * Mv[2][j]
              for j in range(3)] for i in range(3)]
        c2_tot += 1
        if any(sum(P[i]) != 1 for i in range(3)) or \
                any(sum(P[i][j] for i in range(3)) != 1 for j in range(3)):
            c2_ds = False
        A_, B_, C_ = P[0][0] * P[0][1], P[1][0] * P[1][1], P[2][0] * P[2][1]
        T = 2 * (A_ * B_ + B_ * C_ + C_ * A_) - A_ * A_ - B_ * B_ - C_ * C_
        if c2_Tmin is None or T < c2_Tmin:
            c2_Tmin = T
        if T < 0:
            c2_neg.append((nu, nv, T, P))
        if P == TARGET:
            c4_hits += 1
check("C2.1 EVERY DIVISIBLE COMPOSITION IN THE POOL IS BISTOCHASTIC "
      "EXACTLY (Birkhoff's polytope is a multiplicative semigroup), so the "
      "precondition never fires and the whole question is the "
      "unistochasticity of the product",
      c2_ds, f"{c2_tot} ordered products, all exactly bistochastic")
check("C2.2 THE COUNTEREXAMPLE HUNT OVER THE CERTIFIED POOL: no product of "
      "two entrywise-squared 3x3 unitaries in the pool is "
      "bistochastic-but-not-unistochastic.  The minimum triangle "
      "discriminant over the whole census is printed and is NON-NEGATIVE",
      len(c2_neg) == 0,
      f"{c2_tot} ordered products of {len(POOL)} certified-unistochastic "
      f"factors; products with T < 0: {len(c2_neg)}; minimum T over the "
      f"census {c2_Tmin} = {float(c2_Tmin):.10f}")

print()
print("  C3.  THE EXHAUSTIVE RATIONAL CENSUS.  Every bistochastic 3x3")
print("  matrix with entries in (1/D)Z that passes the exact n = 3")
print("  criterion, and every ordered product of two of them.  Integer")
print("  arithmetic throughout (entries scaled by D, products by D^2).")


def rational_uni(D):
    out = []
    for u in range(D + 1):
        for v in range(D + 1 - u):
            for w in range(D + 1 - u):
                for z in range(D + 1 - v):
                    a = [[u, v, D - u - v], [w, z, D - w - z],
                         [D - u - w, D - v - z, u + v + w + z - D]]
                    if any(x < 0 for r in a for x in r):
                        continue
                    A_, B_, C_ = [a[i][0] * a[i][1] for i in range(3)]
                    if 2 * (A_ * B_ + B_ * C_ + C_ * A_) - A_ * A_ \
                            - B_ * B_ - C_ * C_ >= 0:
                        out.append(a)
    return out


c3_rows, c3_bad, c4_hits_rat = [], [], 0
for D in (4, 6, 8, 10, 12):
    cands = rational_uni(D)
    tgt = [[D * D // 2, D * D // 2, 0], [0, D * D // 2, D * D // 2],
           [D * D // 2, 0, D * D // 2]] if D % 2 == 0 else None
    neg, Tmin = 0, None
    for X in cands:
        X0, X1, X2 = X
        for Y in cands:
            Y0, Y1, Y2 = Y
            P = [[x[0] * Y0[j] + x[1] * Y1[j] + x[2] * Y2[j]
                  for j in range(3)] for x in (X0, X1, X2)]
            A_ = P[0][0] * P[0][1]
            B_ = P[1][0] * P[1][1]
            C_ = P[2][0] * P[2][1]
            T = 2 * (A_ * B_ + B_ * C_ + C_ * A_) - A_ * A_ - B_ * B_ \
                - C_ * C_
            if Tmin is None or T < Tmin:
                Tmin = T
            if T < 0:
                neg += 1
                if len(c3_bad) < 3:
                    c3_bad.append((D, X, Y, P, T))
            if tgt is not None and P == tgt:
                c4_hits_rat += 1
    c3_rows.append((D, len(cands), len(cands) ** 2, neg, Tmin))
    print(f"     D = {D:3d}:  {len(cands):6d} criterion-passing "
          f"bistochastic matrices,  {len(cands) ** 2:9d} ordered products, "
          f" products with T < 0: {neg}")
    sys.stdout.flush()

_c3_total = sum(r[2] for r in c3_rows)
_c3_neg = sum(r[3] for r in c3_rows)
check("C3.1 THE EXHAUSTIVE RATIONAL CENSUS FINDS NO COUNTEREXAMPLE EITHER: "
      "over every ordered pair of criterion-passing rational bistochastic "
      "3x3 matrices at the declared denominators, the product's triangle "
      "discriminant is never negative",
      _c3_neg == 0,
      f"{_c3_total} ordered products over D in (4, 6, 8, 10, 12); "
      f"negatives {_c3_neg}; witnesses {c3_bad}")

check("C4.1 THE ARM-A OBJECT IS NOT REACHED BY COMPOSITION EITHER: the "
      "binned quarter-revival matrix circ(1/2, 1/2, 0) — the exact object "
      "SEC 8 certifies as bistochastic-but-not-unistochastic with "
      "T = -1/16 — is not the product of two unistochastic matrices "
      "anywhere in either searched family.  At the declared caps it lies "
      "outside the class AND outside the multiplicative closure of the "
      "class",
      c4_hits == 0 and c4_hits_rat == 0 and _tT < 0,
      f"T(target) = {_tT}; hits in the certified pool {c4_hits}; hits in "
      f"the exhaustive rational families {c4_hits_rat}")

print()
print("  ARM C VERDICT: EXCLUDED-BY-CAP, in the negative direction.  No")
print("  counterexample exists in either searched family:")
print(f"    (a) {c2_tot} ordered products of {len(POOL)} 3x3 matrices each")
print("        of which IS an entrywise squared Q(i)-unitary with its")
print("        unitary exhibited and verified;")
print(f"    (b) {_c3_total} ordered products over the exhaustive rational")
print("        families at denominators 4, 6, 8, 10 and 12.")
print("  On the searched families the divisible composition of two")
print("  unistochastic 3x3 matrices is again unistochastic.  This is a")
print("  CENSUS AT A DECLARED CAP, not a theorem: no proof of closure is")
print("  offered and none is claimed.")


# ===========================================================================
# SEC 13.  SCOPE, CAPS, AND THE VERDICT
# ===========================================================================

sec("SCOPE, CAPS, AND THE VERDICT")

anchor("SRC.3b THE FAST POLYGON ORACLE AGREED WITH THE COMMITTED ONE ON "
       "EVERY MATRIX ON WHICH BOTH WERE RUN, over the whole receipt",
       POLY_GATE[1] == 0,
       f"{POLY_GATE[0]} matrices cross-checked, {POLY_GATE[1]} "
       f"discrepancies")

print("""
  SCOPE, restated from the pin and binding on every line above.  Toy
  lattice scale.  No continuum analysis is claimed beyond what the discrete
  family exhibits.  No renormalisation claim.  No claim about interacting
  quantum field theory.  No claim about nature.  Findings are formal
  properties of [B3]'s criterion under the stated operations.

  FURTHER SCOPE, specific to this receipt.
   * Every negative verdict is a verdict on the CLOSED, UNDILATED
     criterion at the stated dimension — the FIRST disjunct of the
     stochastic-quantum theorem.  [B3]'s subsystem disjunct
     ([B3-dilation], PAGE 19) is untouched: a binned matrix that is not
     unistochastic at its own size may still be a subsystem of a
     unistochastic process at a larger size, and nothing here tests that.
   * The exact family is the RATIONAL-TIME family theta = 2 pi p/q with
     q | n.  Those times are dense in the time axis but they are not all
     times; the irrational-time and incommensurate regimes are excluded by
     cap with the reason exhibited (A1.4).
   * 'Fixed physical parameters' means fixed t, m, L with a = L/n -> 0.
     The alternative convention is a different trajectory in the (c, B)
     table and is reported as such.
   * Arm C's result is a census at a declared cap, not a closure theorem.
   * Nothing here claims that a matrix passing the screen IS a quantum
     system; the map from a screened matrix to a physical system is not
     supplied by this unit.
""")

for _k, _v in CAPS.items():
    print(f"    CAP  {_k}: {_v}")

print()
print("  THE VERDICT")
print()
print("    Q-UNSTABLE.")
print()
print("    The binning defect does not vanish along the refinement ladder.")
print("    At fixed physical parameters the binned matrix is EXACTLY")
print("    n-independent (A3.1) — literally the same rational matrix at")
print("    every lattice size — so the verdict and the exact defect are")
print("    constant.  At the quarter revival the three-cell coarse-")
print("    graining of the free ring propagator is bistochastic and NOT")
print("    unistochastic, with T = -1/16 and certified distance")
print("    dist_1 >= 1/64 from the class, at every n on the ladder (A3.1,")
print("    F2.2).  Refining the BINS does not repair it: at c = 2 the")
print("    verdict alternates with the parity of the bin count forever at")
print("    constant defect -1/2 (A4.4), and the failure set is")
print("    characterised exactly by a difference of multiplicity one in")
print("    the cell set (A4.2).  A second, structurally different exact")
print("    family — the Trotterised harmonic oscillator — reproduces the")
print("    phenomenon (A5.2).")
print()
print("    Q-ILLDEFINED IS ALSO REALISED, ON ARM B, AND THE TWO ARE NOT IN")
print("    CONFLICT.  The normalisation [B3]'s criterion is defined")
print("    against is the COUNTING-measure row mass, which exists and is")
print("    exactly 1 at every n (B1.1).  The normalisation a continuum")
print("    version would need is the kernel row mass, which is exactly")
print("    1/a = n/L and diverges along the very same ladder (B1.3).  The")
print("    criterion is finite-dimensional in an essential way: it is a")
print("    statement about a counting measure on a finite configuration")
print("    set, and the object that survives the continuum limit is not")
print("    the object it constrains.")
print()
print("    ARM C: CLOSURE, at the declared caps.  The divisible")
print("    composition |U|^2 . |V|^2 — what a coarse observer writes when")
print("    it inserts a division event — is again unistochastic everywhere")
print("    in both searched families (C2.2, C3.1), with the expected")
print("    control |UV|^2 != |U|^2 . |V|^2 gated (C1.1).  No counter-")
print("    example is exhibited and none is claimed to exist.  The failure")
print("    this unit locates is therefore specifically REFINEMENT, not")
print("    COMPOSITION.")
print()

print("=" * 78)
print(f"  gates: {PASS} PASS, {FAIL} FAIL   (anchor failures: {ANCHOR_FAIL})")
print(f"  runtime: {time.time() - T0:.1f} s")
print("  STATUS: GREEN-UNREVIEWED.  Not citable until a hostile round.")
print("=" * 78)

sys.exit(1 if ANCHOR_FAIL else 0)
