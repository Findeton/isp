#!/usr/bin/env python3
"""
w2_multiplier_ladder_exact.py — v12 W2: THE MULTIPLIER LADDER
(W2a the defect algebra -> W2b projective descent -> W2c selection).

Pin: v12/note-w2-multiplier-ladder-pin.md (STRICT, frozen before this
file existed).  Binding specification: v12 paper 0 v2.1 sec.1 (T2',
Delta^B and the three-defect distinction), sec.4 W2' (the three-way
split, verbatim), sec.5 (non-claims); v12/LOG.md #1-#8.  Antecedent
receipts, READ AND REUSED here rather than re-derived:
v12/code/w1p_three_class_exact.py (W1' TERMINAL, LOG #7) and
v10/code/d74_transport_holonomy_exact.py (D74 TERMINAL, round-1
reviewed).

THE STANDING WALL, ENGRAVED IN THE PIN
    B(omega U) = B(U)   for every scalar omega in U(1)
The Born projection annihilates scalar multipliers; the bridge from
the Delta-family to H^2 must be BUILT, and "cannot be built from
committed objects" is a first-class outcome.

THE THREE ARMS, STAGED
  W2a  THE DEFECT ALGEBRA.  The Delta^B-family on n-step
       compositions: the universal closed form; the exact invariance
       group and the normalized forms; the doubly-centred structure
       with its sharp entrywise bounds; the n-fold telescoping and
       the full TREE (bracketing) coherence identity, gated over
       FORMAL matrices with no property of B assumed — the W1' C+2
       precedent generalized to every n and every bracketing; the
       demonstration that the law is content-free about B (gated with
       declared NON-Born maps); the exact two-sided annihilator of
       the family; the failure of pairwise flatness to imply n-fold
       flatness; and the generalized phase-alignment closed form
       (Delta^B = 0 on a DFT-sandwich family <=> the interleaving
       diagonal has FLAT Fourier spectrum), which contains W1's two
       committed closed forms as its N = 2 and N = 3 cases.
  W2b  PROJECTIVE DESCENT.  Does any committed-object lift make the
       generated Z^2 (D74's <2,3>, read from the committed v10
       instrument by AST slice and anchored) act PROJECTIVELY on
       amplitude objects, with the multiplier controlling a
       Delta^B-invariant (U V = e^{2 pi i theta} V U)?  Candidates
       from the corpus only.  W2b-NO-ACTION with a missing-piece
       census is a first-class outcome.
  W2c  SELECTION.  Only if W2b yields a genuine class: which theta,
       by what principle; else W2c-VACUOUS, stated, with the facts
       that would constrain any future theta gated anyway.

HOUSE RULES OBSERVED
  * Exact arithmetic end to end.  fractions.Fraction for rationals;
    the cyclotomic fields Q(zeta_N) (class Cyc, SLICED from W1',
    canonical representation modulo Phi_N, so tuple equality IS field
    equality) for every complex algebraic quantity; a multivariate
    polynomial ring over Q (class MP, sliced from W1') for every
    symbolic identity; W1's Q(sqrt 2) sign oracle (class Q2) for the
    one order comparison this unit makes.  No float in any
    substantive path; no tolerance anywhere.
  * Substantive negatives exit 0.  exit 1 is ANCHOR-ONLY: the
    arithmetic self-test, W1's committed gate values, and D74's
    committed group verdict.
  * Determinism: fixed lexicographic enumeration everywhere; declared
    deterministic strides where a sweep is capped (W1's round-1
    lesson: never the lexicographic head); no randomness, no
    wall-clock in any substantive path.
  * Caps printed at the head of every sweep.
  * Lean: NONE.  W2b-ACTION-FOUND and W2b-NO-ACTION are both
    reportable; so is W2c-VACUOUS.
"""

from __future__ import annotations

import ast
import itertools
import os
import sys
import time
from fractions import Fraction as Fr

T0 = time.time()
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))


def el():
    return "%7.1fs" % (time.time() - T0)


def hr(c="="):
    print(c * 78)


def head(title):
    hr()
    print(title)
    hr()


def tick(msg):
    print("      ... %-58s %s" % (msg, el()))
    sys.stdout.flush()


def stride(seq, cap):
    """A DECLARED DETERMINISTIC STRIDE across the whole enumeration — never
    the lexicographic head (W1' round-1 repair M1)."""
    if len(seq) <= cap:
        return list(seq)
    st = len(seq) // cap
    return [seq[i * st] for i in range(cap)]


# ============================================================================
#     GATE BOOK-KEEPING
# ============================================================================
GATES = []
CITED = {}


def cite(tag, text):
    CITED[tag] = text


def gate(sec, name, ok, detail="", tag=""):
    GATES.append((sec, name, bool(ok), detail, tag))
    mark = "PASS" if ok else "FAIL"
    line = "  [%s] %-5s %-53s" % (mark, sec, name)
    if detail:
        line += " %s" % detail
    if tag:
        line += "   <%s>" % tag
    print(line)
    sys.stdout.flush()
    return bool(ok)


NANCHOR = [0]


def anchor(name, ok, detail=""):
    if not ok:
        print("  [ANCHOR-FAIL] %-44s %s" % (name, detail))
        print("\nANCHOR FAILURE — an antecedent receipt does not reproduce.")
        sys.exit(1)
    NANCHOR[0] += 1
    print("  [anchor] %-46s ok  %s" % (name, detail))
    sys.stdout.flush()


# ============================================================================
head("w2_multiplier_ladder_exact.py — v12 W2")
print("THE MULTIPLIER LADDER: W2a THE DEFECT ALGEBRA -> W2b PROJECTIVE")
print("DESCENT -> W2c SELECTION")
hr()
print("  pin    : v12/note-w2-multiplier-ladder-pin.md (frozen first)")
print("  binding: v12 paper 0 v2.1 sec.1 (T2'), sec.4 W2' (verbatim),")
print("           sec.5 (non-claims); v12/LOG.md #1-#8.")
print("  wall   : B(omega U) = B(U).  The Born projection ANNIHILATES")
print("           scalar multipliers.  The H^2 bridge must be BUILT.")
print("  banner : EXACT arithmetic end to end, NO TOLERANCE ANYWHERE.")
print("  exits  : substantive negatives exit 0; exit 1 is ANCHOR-only")
print("           (the arithmetic self-test, W1's committed gate values,")
print("           and D74's committed group verdict).")
print("  lean   : NONE.")
print()

cite("[B1]", "Barandes, arXiv 2302.10778 — the stochastic-quantum "
     "correspondence; the identification of the Born-projection cross terms "
     "with interference.  Delta^B's cross-term form is his, reproduced, not "
     "originated here.")
cite("[W]", "Weyl relations / noncommutative torus: projective multipliers "
     "on Z^2, U V = e^{2 pi i theta} V U, realized by the clock/shift pair "
     "(e.g. arXiv 1606.01829).  W1' NAMED it and used it at no gate; this "
     "is the unit where it is USED, and where it fails.")
cite("[SvN]", "Stone-von Neumann, finite form: on C^N the irreducible "
     "projective representations of Z^2 with a primitive q-th root "
     "multiplier have dimension exactly q and are the clock/shift (Weyl) "
     "pair up to unitary equivalence and scalars.  CITED, not proven here; "
     "used only to say that the Weyl realization is not an exotic corner.")
cite("[REV2]", "The second external hostile review, adjudicated at "
     "v12/LOG.md #4: the three-defect distinction, the coherence law (W2a's "
     "seed), and the B(omega U) = B(U) observation that forced the "
     "W2a/W2b/W2c staging.")
cite("[W1']", "v12/note-w1p-three-class.md + v12/code/"
     "w1p_three_class_exact.py — TERMINAL at v12/LOG.md #7.  Its arithmetic "
     "layer, its matrix layer and its two census families are SLICED and "
     "REUSED here; its committed gate values are this unit's anchors.")
cite("[D74]", "v10/note-d74-transport-holonomy-result.md + v10/code/"
     "d74_transport_holonomy_exact.py — TERMINAL, round-1 reviewed.  The "
     "generated group <2,3>, the value set {1/2, 2/3, 3/2, 2}, D2 (a "
     "positive-rational holonomy's only possible unimodular content is -1, "
     "realized nowhere), D4.1 (the i-twist correspondence is content-free), "
     "D9.1 (the reversal-EVEN channel carries J).")
cite("[D71b]", "v10/note-d71b-holonomy-phase-identity.md — the corpus "
     "survey of the phase question.  Clause 2: v7 paper 30's amplitude "
     "conjugates under order reversal (dual-conjugation error exactly 0) "
     "and the odd channel is the unique slot on which a phase can transform "
     "like a holonomy.  Clause 3: the loop is not written.  Section 4.2: "
     "D42b4's prod sqrt(q) is the right carrier with NO closure, and its "
     "phase slot is filled with +1 without an argument.")

# ============================================================================
head("SECTION 0 — THE SLICED INSTRUMENTS, AND THE ANCHORS")
# ============================================================================
print("  Antecedent instruments are READ FROM THE COMMITTED FILES by AST")
print("  slice: the named top-level definitions are extracted from the")
print("  parsed source and executed here.  Nothing is copied by hand, and a")
print("  drift in either parent surfaces as an anchor failure.")
print()


def slice_defs(path, names):
    """Extract the named top-level FunctionDef/ClassDef nodes from `path`,
    compile and exec them into a fresh namespace.  Exact, no copying."""
    src = open(path).read()
    tree = ast.parse(src)
    keep, spans = [], {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) \
                and node.name in names:
            keep.append(node)
            spans[node.name] = (node.lineno, node.end_lineno)
    missing = sorted(set(names) - set(spans))
    if missing:
        print("  [SLICE-FAIL] %s: names not found: %s" % (path, missing))
        sys.exit(1)
    mod = ast.Module(body=keep, type_ignores=[])
    ns = {"Fr": Fr, "itertools": itertools, "sys": sys, "time": time,
          "_CYCLO": {}}
    exec(compile(ast.fix_missing_locations(mod), "<slice:%s>"
                 % os.path.basename(path), "exec"), ns)
    return ns, spans


W1P = os.path.join(ROOT, "v12", "code", "w1p_three_class_exact.py")
D74F = os.path.join(ROOT, "v10", "code", "d74_transport_holonomy_exact.py")

W1_NAMES = ["ptrim", "pmul", "padd", "psub", "pscal", "pdivmod",
            "cyclotomic", "pgcdext", "Cyc", "solve_in_basis", "Q2", "MP",
            "mmul", "_dot", "mdag", "mB", "msub", "mzero", "meq", "mid",
            "is_unitary", "delta_def", "delta_cross", "diag", "perm",
            "row_monomial", "col_monomial", "key", "S_rat", "mmul_rat",
            "stochastic", "mp_matrix", "mp_mm", "mp_sub",
            "shadow_no_D", "shadow_with_D"]
D74_NAMES = ["primes_of", "lattice_basis", "group_of"]

NS1, SP1 = slice_defs(W1P, W1_NAMES)
NS7, SP7 = slice_defs(D74F, D74_NAMES)
print("  sliced from v12/code/w1p_three_class_exact.py       : %2d "
      "definitions" % len(SP1))
print("  sliced from v10/code/d74_transport_holonomy_exact.py: %2d "
      "definitions  (%s)" % (len(SP7), ", ".join(
          "%s@%d-%d" % (n, a, b) for n, (a, b) in sorted(SP7.items()))))
print()

Cyc = NS1["Cyc"]
MP = NS1["MP"]
Q2 = NS1["Q2"]
solve_in_basis = NS1["solve_in_basis"]
mmul = NS1["mmul"]
mdag = NS1["mdag"]
mB = NS1["mB"]
msub = NS1["msub"]
mzero = NS1["mzero"]
meq = NS1["meq"]
mid = NS1["mid"]
is_unitary = NS1["is_unitary"]
delta_def = NS1["delta_def"]
delta_cross = NS1["delta_cross"]
mdiag = NS1["diag"]
mperm = NS1["perm"]
row_monomial = NS1["row_monomial"]
col_monomial = NS1["col_monomial"]
mkey = NS1["key"]
S_rat = NS1["S_rat"]
mmul_rat = NS1["mmul_rat"]
stochastic = NS1["stochastic"]
mp_matrix = NS1["mp_matrix"]
mp_mm = NS1["mp_mm"]
mp_sub = NS1["mp_sub"]
shadow_no_D = NS1["shadow_no_D"]
shadow_with_D = NS1["shadow_with_D"]
group_of = NS7["group_of"]
primes_of = NS7["primes_of"]


def ksum(K, items):
    acc = K.zero
    for x in items:
        acc = K.add(acc, x)
    return acc


def mtr(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


def sqrtN(K, m):
    """sqrt(m) in K, exactly: first the zeta^k + zeta^-k form (W1's own
    oracle), then the quadratic Gauss sum for a prime m dividing K.n."""
    try:
        return K.sqrt_of(m)
    except ArithmeticError:
        pass
    if K.n % m == 0:
        st = K.n // m
        qrs = {(k * k) % m for k in range(1, m)}
        g = K.zero
        for k in range(1, m):
            t = K.zpow(st * k)
            g = K.add(g, t) if k in qrs else K.sub(g, t)
        if K.mul(g, g) == K.rat(m):
            return g
    raise ArithmeticError("no exact sqrt(%d) in Q(zeta_%d)" % (m, K.n))


# ------------------------------------------------- 0.1 the arithmetic layer
print("0.1  THE ARITHMETIC LAYER (sliced) — self-test")
FIELDS = {n: Cyc(n) for n in (2, 3, 4, 5, 6, 8, 12)}
K8, K12 = FIELDS[8], FIELDS[12]
anchor("Phi_8 = x^4 + 1", K8.phi == [Fr(1), Fr(0), Fr(0), Fr(0), Fr(1)],
       "deg %d" % K8.deg)
anchor("Phi_12 = x^4 - x^2 + 1",
       K12.phi == [Fr(1), Fr(0), Fr(-1), Fr(0), Fr(1)], "deg %d" % K12.deg)
for n in sorted(FIELDS):
    K = FIELDS[n]
    anchor("zeta_%-2d exact order, conj = inv" % n,
           K.zpow(n) == K.one
           and all(K.zpow(k) != K.one for k in range(1, n))
           and K.inv(K.z) == K.conj(K.z), "deg %d" % K.deg)
SQRT2_8 = sqrtN(K8, 2)
SQRT3_12 = sqrtN(K12, 3)
SQRT5_5 = sqrtN(FIELDS[5], 5)
INV_SQRT2_8 = K8.inv(SQRT2_8)
INV_SQRT3_12 = K12.inv(SQRT3_12)
anchor("sqrt2 in Q(zeta_8), 1/sqrt2 exact",
       K8.mul(SQRT2_8, SQRT2_8) == K8.rat(2)
       and K8.mul(INV_SQRT2_8, SQRT2_8) == K8.one)
anchor("sqrt3 in Q(zeta_12), 1/sqrt3 exact",
       K12.mul(SQRT3_12, SQRT3_12) == K12.rat(3)
       and K12.mul(INV_SQRT3_12, SQRT3_12) == K12.one)
anchor("sqrt5 in Q(zeta_5) by the quadratic Gauss sum",
       FIELDS[5].mul(SQRT5_5, SQRT5_5) == FIELDS[5].rat(5),
       "g = sum_k (k|5) zeta_5^k, g^2 = 5")
B_Q2 = [K8.one, SQRT2_8]


def to_q2(x):
    """x in Q(zeta_8) lying in Q(sqrt 2) -> Q2 (exact sign oracle), else
    None."""
    s = solve_in_basis(K8, x, B_Q2)
    return None if s is None else Q2(s[0], s[1])


anchor("Q2 sign oracle through the sliced solver",
       to_q2(K8.rat(Fr(1, 2))).cmp(to_q2(K8.scal(SQRT2_8, Fr(1, 4)))) == 1
       and to_q2(K8.rat(0)).cmp(to_q2(K8.rat(Fr(-1, 2)))) == 1,
       "1/2 > sqrt2/4 > 0 > -1/2, exactly")
print()

# ------------------------------------------- 0.2 W1's committed gate values
print("0.2  W1' COMMITTED GATE VALUES (v12/note-w1p-three-class.md, TERMINAL")
print("     at LOG #7) — reproduced through the sliced instruments.  Any")
print("     drift exits 1.")

H2 = [[K8.mul(K8.rat(a), INV_SQRT2_8) for a in row]
      for row in ([1, 1], [1, -1])]
W_UNB = [[K8.mul(K8.zpow(k), INV_SQRT2_8) for k in row]
         for row in ([0, 2], [2, 0])]
F3M = [[K12.mul(K12.zpow(4 * ((i * j) % 3)), INV_SQRT3_12) for j in range(3)]
       for i in range(3)]
anchor("H, W, F3 unitary in exact arithmetic",
       is_unitary(K8, H2) and is_unitary(K8, W_UNB)
       and is_unitary(K12, F3M))
HALF, MHALF = K8.rat(Fr(1, 2)), K8.rat(Fr(-1, 2))
anchor("Delta^B(H,H) = [[1/2,-1/2],[-1/2,1/2]]",
       delta_def(K8, H2, H2) == [[HALF, MHALF], [MHALF, HALF]], "W1' sec.5")
anchor("Delta^B(H,W) = 0, both factors unbiased",
       mzero(K8, delta_def(K8, H2, W_UNB)), "W1' sec.5 named witness")
for nm, K, U2, U1 in (("H.H", K8, H2, H2), ("H.W", K8, H2, W_UNB),
                      ("F3.F3", K12, F3M, F3M),
                      ("F3.F3dag", K12, F3M, mdag(K12, F3M))):
    anchor("cross-term identity [%s]" % nm,
           meq(K, delta_def(K, U2, U1), delta_cross(K, U2, U1)), "[B1]")

FAM2 = {}
for s in itertools.permutations(range(2)):
    for e0, e1 in itertools.product((0, 2, 4, 6), repeat=2):
        FAM2[mkey(mmul(K8, mperm(K8, s),
                       mdiag(K8, [K8.zpow(e0), K8.zpow(e1)])))] = None
NMON2 = len(FAM2)
for s in range(8):
    for t in range(8):
        FAM2[mkey(mmul(K8, mmul(K8, mdiag(K8, [K8.one, K8.zpow(s)]), H2),
                       mdiag(K8, [K8.one, K8.zpow(t)])))] = None
FAM2L = [[list(r) for r in k] for k in sorted(FAM2.keys())]

FAM3 = {}
for s in itertools.permutations(range(3)):
    for e in itertools.product((0, 4, 8), repeat=2):
        FAM3[mkey(mmul(K12, mperm(K12, s),
                       mdiag(K12, [K12.one, K12.zpow(e[0]),
                                   K12.zpow(e[1])])))] = None
NMON3 = len(FAM3)
for a in (0, 4, 8):
    for b in (0, 4, 8):
        FAM3[mkey(mmul(K12, mmul(K12, mdiag(K12, [K12.one, K12.zpow(a),
                                                  K12.one]), F3M),
                       mdiag(K12, [K12.one, K12.zpow(b), K12.one])))] = None
FAM3L = [[list(r) for r in k] for k in sorted(FAM3.keys())]
anchor("W1' family sizes", len(FAM2L) == 96 and NMON2 == 32
       and len(FAM3L) == 63 and NMON3 == 54,
       "F2 = 96 (32 monomial-seeded), F3 = 63 (54)")

CENSUS = {}
for tag, K, FAM in (("2x2", K8, FAM2L), ("3x3", K12, FAM3L)):
    Bc = [mB(K, U) for U in FAM]
    rm = [row_monomial(K, U) for U in FAM]
    cm = [col_monomial(K, U) for U in FAM]
    cnt = {"cond_zero": 0, "cond_nonzero": 0,
           "free_zero": 0, "free_nonzero": 0}
    rows = []
    zflag = {}
    for i2, U2 in enumerate(FAM):
        for i1, U1 in enumerate(FAM):
            D = msub(K, mB(K, mmul(K, U2, U1)), mmul(K, Bc[i2], Bc[i1]))
            z = mzero(K, D)
            c = rm[i2] or cm[i1]
            cnt["%s_%s" % ("cond" if c else "free",
                           "zero" if z else "nonzero")] += 1
            rows.append((i2, i1, D, z))
            zflag[(i2, i1)] = z
    CENSUS[tag] = (K, FAM, Bc, rm, cm, cnt, rows, zflag)
    tick("W1' %s census rebuilt (%d ordered pairs)" % (tag, len(rows)))
anchor("W1' 2x2 census counts",
       CENSUS["2x2"][5] == {"cond_zero": 5120, "cond_nonzero": 0,
                            "free_zero": 1024, "free_nonzero": 3072},
       "5120 / 0 / 1024 / 3072 of 9216")
anchor("W1' 3x3 census counts",
       CENSUS["3x3"][5] == {"cond_zero": 3888, "cond_nonzero": 0,
                            "free_zero": 54, "free_nonzero": 27},
       "3888 / 0 / 54 / 27 of 3969")

n2z = 0
for s, t, u, v in itertools.product(range(8), repeat=4):
    U2 = mmul(K8, mmul(K8, mdiag(K8, [K8.one, K8.zpow(s)]), H2),
              mdiag(K8, [K8.one, K8.zpow(t)]))
    U1 = mmul(K8, mmul(K8, mdiag(K8, [K8.one, K8.zpow(u)]), H2),
              mdiag(K8, [K8.one, K8.zpow(v)]))
    z = mzero(K8, delta_def(K8, U2, U1))
    if z != ((t + u) % 8 in (2, 6)):
        anchor("W1' 2x2 closed form t+u = +-2 (mod 8)", False,
               "mismatch at (%d,%d,%d,%d)" % (s, t, u, v))
    n2z += z
anchor("W1' 2x2 closed form t+u = +-2 (mod 8)", n2z == 1024,
       "4096 quadruples, 1024 with Delta^B = 0")
n3z = 0
for a2, b2, a1, b1 in itertools.product((0, 4, 8), repeat=4):
    U2 = mmul(K12, mmul(K12, mdiag(K12, [K12.one, K12.zpow(a2), K12.one]),
                        F3M), mdiag(K12, [K12.one, K12.zpow(b2), K12.one]))
    U1 = mmul(K12, mmul(K12, mdiag(K12, [K12.one, K12.zpow(a1), K12.one]),
                        F3M), mdiag(K12, [K12.one, K12.zpow(b1), K12.one]))
    z = mzero(K12, delta_def(K12, U2, U1))
    if z != (((b2 + a1) // 4) % 3 != 0):
        anchor("W1' 3x3 closed form b2+a1 != 0 (mod 3)", False,
               "mismatch at (%d,%d,%d,%d)" % (a2, b2, a1, b1))
    n3z += z
anchor("W1' 3x3 closed form b2+a1 != 0 (mod 3)", n3z == 54,
       "81 quadruples, 54 with Delta^B = 0")

c1c, s1c, c2c, s2c = Fr(24, 25), Fr(7, 25), Fr(4, 5), Fr(3, 5)
c1 = c1c ** 2 - s1c ** 2
c2 = c2c ** 2 - s2c ** 2
ctot = c1 * c2 - (2 * c1c * s1c) * (2 * c2c * s2c)
Kdiv = S_rat(ctot / c1)
anchor("W1' C+1 exact rationals",
       c1 == Fr(527, 625) and c2 == Fr(7, 25) and ctot == Fr(-7, 25)
       and (S_rat(ctot)[0][0] - mmul_rat(S_rat(c2), S_rat(c1))[0][0]
            == Fr(-4032, 15625))
       and ctot / c1 == Fr(-175, 527) and stochastic(Kdiv)
       and mmul_rat(Kdiv, S_rat(c1)) == S_rat(ctot),
       "Delta^B_00 = -4032/15625, K = S(-175/527) divides")
for nm, K, U2, U1 in (("H.H", K8, H2, H2), ("F3.F3", K12, F3M, F3M)):
    anchor("W1' record example [%s]" % nm,
           meq(K, shadow_with_D(K, U2, U1), mmul(K, mB(K, U2), mB(K, U1)))
           and meq(K, shadow_no_D(K, U2, U1), mB(K, mmul(K, U2, U1))),
           "shadow(U2.D.U1) = B(U2)B(U1) exactly")
print()

# ------------------------------------------ 0.3 D74's committed group verdict
print("0.3  D74 COMMITTED GROUP VERDICT (v10/note-d74-transport-holonomy-")
print("     result.md TH-B, TERMINAL) — the generated Z^2, recomputed")
print("     through D74's OWN sliced group instrument.")
print("     QUOTED COMMITTED INPUT (D74 TH-B, the AB4 anchor window and the")
print("     cumulative row): non-unit holonomy spectrum")
print("     {1/2: 70, 2/3: 2, 3/2: 6, 2: 10}; value set {1/2, 2/3, 3/2, 2};")
print("     unchanged at ten scopes over four mutually non-nested evidence")
print("     pools; 27186 cumulative non-unit squares.")
D74_VALUES = {Fr(1, 2): 70, Fr(2, 3): 2, Fr(3, 2): 6, Fr(2): 10}
GRP = group_of(set(D74_VALUES))
anchor("D74 group <2,3>: primes, rank, index, fullness",
       GRP["primes"] == [2, 3] and GRP["rank"] == 2
       and GRP["index"] == 1 and GRP["full"],
       "rank 2, index 1 in Z^2, the FULL 3-smooth group")
anchor("D74 lattice basis [[-1,0],[0,1]]", GRP["basis"] == [[-1, 0], [0, 1]],
       "D74 receipt gate B.2, verbatim")
anchor("D74 spectrum total 88 at the AB4 anchor window",
       sum(D74_VALUES.values()) == 88, "70 + 2 + 6 + 10")
anchor("every committed holonomy value is a POSITIVE RATIONAL",
       all(v > 0 for v in D74_VALUES), "D74 D2's hypothesis")
print("     %s" % GRP["name"])
print("     NOTE, and it is D74's own: the lattice BASIS depends on the")
print("     order in which the generators are presented (D74 calls its")
print("     instrument on a SET; presented as a sorted list the same")
print("     lattice returns with basis [[-1,0],[0,-1]]).  What is licensed,")
print("     and what this unit uses, is the LATTICE — prime support, rank,")
print("     index — all three basis-independent.")
print()
print("  anchors: %d, all reproduce.   %s" % (NANCHOR[0], el()))
print()


# ============================================================================
head("SECTION W2a — THE DEFECT ALGEBRA")
# ============================================================================
print("  Delta^B(U2, U1) = B(U2 U1) - B(U2) B(U1),  B(U)_ij = |U_ij|^2.")
print()

# --------------------------------------------------------- A1 the closed form
print("A1.  THE UNIVERSAL CLOSED FORM, in every dimension")
print("     With m = row i of U2 and n = column j of U1, put")
print("     w_k := m_k n_k = (U2)_ik (U1)_kj — the amplitude of the path")
print("     through intermediate value k.  Then")
print()
print("         Delta^B_ij  =  |sum_k w_k|^2  -  sum_k |w_k|^2")
print("                     =  2 sum_{k<l} Re( w_k conj(w_l) ).")
print()
print("     [B1]'s cross-term sum, in closed form: the defect entry IS the")
print("     total pairwise interference of the path amplitudes through the")
print("     cut, and nothing else.  Every structural result below is read")
print("     off this one line.")
for d in (2, 3, 4, 5, 6):
    nv = 2 * d
    xs = [MP.var(nv, i) for i in range(d)]
    ys = [MP.var(nv, d + i) for i in range(d)]
    sx, sy = sum(xs[1:], xs[0]), sum(ys[1:], ys[0])
    lhs = (sx * sx + sy * sy
           - sum((x * x for x in xs[1:]), xs[0] * xs[0])
           - sum((y * y for y in ys[1:]), ys[0] * ys[0]))
    rhs = MP.const(nv, 0)
    for k in range(d):
        for l in range(k + 1, d):
            rhs = rhs + 2 * (xs[k] * xs[l] + ys[k] * ys[l])
    gate("A1", "closed form as a real polynomial identity [d=%d]" % d,
         (lhs - rhs).is_zero(), "w_k = x_k + i y_k, %d variables" % nv,
         "[B1]")


def delta_closed(K, U2, U1):
    out = []
    for i in range(len(U2)):
        row = []
        for j in range(len(U1[0])):
            w = [K.mul(U2[i][k], U1[k][j]) for k in range(len(U1))]
            s = ksum(K, w)
            acc = K.mul(s, K.conj(s))
            for x in w:
                acc = K.sub(acc, K.mul(x, K.conj(x)))
            row.append(acc)
        out.append(row)
    return out


for tag in ("2x2", "3x3"):
    K, FAM, Bc, rm, cm, cnt, rows, zflag = CENSUS[tag]
    bad = sum(1 for i2, i1, D, z in rows
              if not meq(K, D, delta_closed(K, FAM[i2], FAM[i1])))
    gate("A1", "closed form = definition on EVERY W1' census pair [%s]" % tag,
         bad == 0, "%d ordered pairs, 0 mismatches" % len(rows), "[B1]")
    tick("A1 %s closed-form sweep" % tag)
print()

# ------------------------------------------------- A2 the invariance group
print("A2.  NORMALIZED FORMS AND THE EXACT INVARIANCE GROUP")
print("     The wall B(omega U) = B(U) is one line of a longer list.  With")
print("     D, D' diagonal unitary and P a permutation:")
print()
print("       (i)   Delta^B(I, U) = Delta^B(U, I) = 0          NORMALIZED")
print("       (ii)  Delta^B(D U2, U1 D') = Delta^B(U2, U1)     OUTER TORI")
print("       (iii) Delta^B(U2 D, D^-1 U1) = Delta^B(U2, U1)   CUT GAUGE")
print("       (iv)  Delta^B(P U2, U1 P) = P Delta^B(U2,U1) P   EQUIVARIANCE")
print("       (v)   Delta^B(U2, U1)^T = Delta^B(U1^T, U2^T)    REVERSAL")
print("       (vi)  Delta^B(U2 D, U1) != Delta^B(U2, U1)       IN GENERAL")
print()
print("     (ii) CONTAINS the wall — a scalar omega is a diagonal unitary —")
print("     and is strictly stronger: what dies at each outer slot is not")
print("     only the scalars but the WHOLE maximal torus T^n; by (iii) the")
print("     compensated torus at the cut dies too.  (vi) is the only")
print("     surviving handle and it is an UNCOMPENSATED insertion, not a")
print("     group action on the pair.")
print("     caps: a DECLARED DETERMINISTIC STRIDE of 24 matrices across each")
print("     full family (never the lexicographic head), all 576 pairs.")
for tag in ("2x2", "3x3"):
    K, FAM, Bc, rm, cm, cnt, rows, zflag = CENSUS[tag]
    d = len(FAM[0])
    ph = [K.zpow((K.n // 4) * k) for k in range(d)] if K.n % 4 == 0 \
        else [K.zpow(k) for k in range(d)]
    D = mdiag(K, ph)
    Dinv = mdiag(K, [K.conj(x) for x in ph])
    P = mperm(K, tuple(range(1, d)) + (0,))
    sub = stride(FAM, 24)
    ok_i = ok_ii = ok_iii = ok_iv = ok_v = True
    nonv = 0
    for U2 in sub:
        ok_i &= mzero(K, delta_def(K, mid(K, d), U2)) \
            and mzero(K, delta_def(K, U2, mid(K, d)))
        for U1 in sub:
            base = delta_def(K, U2, U1)
            ok_ii &= meq(K, delta_def(K, mmul(K, D, U2), mmul(K, U1, D)),
                         base)
            ok_iii &= meq(K, delta_def(K, mmul(K, U2, D),
                                       mmul(K, Dinv, U1)), base)
            ok_iv &= meq(K, delta_def(K, mmul(K, P, U2), mmul(K, U1, P)),
                         mmul(K, mmul(K, P, base), P))
            ok_v &= meq(K, mtr(base), delta_def(K, mtr(U1), mtr(U2)))
            if not meq(K, delta_def(K, mmul(K, U2, D), U1), base):
                nonv += 1
    gate("A2", "(i) normalized: Delta^B(I,U) = Delta^B(U,I) = 0 [%s]" % tag,
         ok_i, "%d matrices" % len(sub))
    gate("A2", "(ii) OUTER TORI killed, both slots [%s]" % tag, ok_ii,
         "contains the wall B(omega U) = B(U)", "[REV2]")
    gate("A2", "(iii) compensated CUT GAUGE killed [%s]" % tag, ok_iii,
         "%d pairs" % (len(sub) ** 2))
    gate("A2", "(iv) permutation equivariance [%s]" % tag, ok_iv)
    gate("A2", "(v) TRANSPOSE-REVERSAL law [%s]" % tag, ok_v,
         "Delta(U2,U1)^T = Delta(U1^T,U2^T)")
    gate("A2", "(vi) an UNCOMPENSATED cut insertion DOES move it [%s]" % tag,
         nonv > 0, "%d of %d pairs moved" % (nonv, len(sub) ** 2))
    tick("A2 %s invariance sweep" % tag)
print()

# ------------------------------------- A3 the doubly-centred structure, bounds
print("A3.  THE DOUBLY-CENTRED STRUCTURE AND THE SHARP BOUNDS")
print("     B(U) is doubly stochastic for unitary U, so B(U2U1) and")
print("     B(U2)B(U1) both are and Delta^B has ALL ROW SUMS AND ALL COLUMN")
print("     SUMS ZERO: the family lands in the (n-1)^2-dimensional space of")
print("     doubly-centred matrices — the tangent space of the Birkhoff")
print("     polytope.  With s_ij := (B(U2)B(U1))_ij = sum_k |w_k|^2:")
print()
print("       Delta^B_ij + s_ij = B(U2U1)_ij >= 0     the LOWER bound,")
print("       n s_ij - (Delta^B_ij + s_ij) = sum_{k<l} |w_k - w_l|^2 >= 0")
print("                                               the UPPER bound,")
print()
print("     i.e. -s_ij <= Delta^B_ij <= (n-1) s_ij, both by exact")
print("     sum-of-squares certificates rather than by any comparison.")
print("     At n = 2 the family is ONE-DIMENSIONAL — Delta^B is a multiple")
print("     of [[1,-1],[-1,1]] whose parameter is 2 Re(A_0 B_0) with")
print("     A_i = (U2)_i0 conj((U2)_i1), B_j = (U1)_0j conj((U1)_1j), which")
print("     is W1's phase-alignment obstruction — and its EXACT RANGE is")
print("     [-1/2, 1/2], both ends attained by the Hadamard pair (H,H).")
for d in (2, 3, 4, 5, 6):
    nv = 2 * d
    xs = [MP.var(nv, i) for i in range(d)]
    ys = [MP.var(nv, d + i) for i in range(d)]
    sx, sy = sum(xs[1:], xs[0]), sum(ys[1:], ys[0])
    sq = (sum((x * x for x in xs[1:]), xs[0] * xs[0])
          + sum((y * y for y in ys[1:]), ys[0] * ys[0]))
    lag = MP.const(nv, 0)
    for k in range(d):
        for l in range(k + 1, d):
            lag = lag + (xs[k] - xs[l]) * (xs[k] - xs[l]) \
                + (ys[k] - ys[l]) * (ys[k] - ys[l])
    gate("A3", "Lagrange SOS: n sum|w|^2 - |sum w|^2 = sum_{k<l}|w_k-w_l|^2"
         " [d=%d]" % d, (d * sq - (sx * sx + sy * sy) - lag).is_zero(),
         "the UPPER bound as a sum of squares, no comparison used")
for tag in ("2x2", "3x3"):
    K, FAM, Bc, rm, cm, cnt, rows, zflag = CENSUS[tag]
    d = len(FAM[0])
    bad_rc = bad_lo = bad_1d = 0
    for i2, i1, D, z in rows:
        for i in range(d):
            if not K.is_zero(ksum(K, D[i])):
                bad_rc += 1
        for j in range(d):
            if not K.is_zero(ksum(K, [D[i][j] for i in range(d)])):
                bad_rc += 1
        S = mmul(K, Bc[i2], Bc[i1])
        BB = mB(K, mmul(K, FAM[i2], FAM[i1]))
        for i in range(d):
            for j in range(d):
                if K.add(D[i][j], S[i][j]) != BB[i][j]:
                    bad_lo += 1
        if d == 2:
            a = D[0][0]
            if D != [[a, K.neg(a)], [K.neg(a), a]]:
                bad_1d += 1
    gate("A3", "row sums and column sums of Delta^B vanish [%s]" % tag,
         bad_rc == 0, "%d pairs, %d violations" % (len(rows), bad_rc))
    gate("A3", "Delta^B + B(U2)B(U1) = B(U2U1), a modulus square [%s]" % tag,
         bad_lo == 0, "%d entries; non-negativity is definitional, so the "
         "lower bound needs no order oracle" % (len(rows) * d * d))
    if d == 2:
        gate("A3", "n=2: Delta^B is a multiple of [[1,-1],[-1,1]]",
             bad_1d == 0, "%d pairs — the family is 1-dimensional"
             % len(rows))
        qs = [to_q2(D[0][0]) for i2, i1, D, z in rows]
        gate("A3", "n=2: every parameter lies in Q(sqrt 2)",
             all(q is not None for q in qs), "the sign oracle applies")
        lo = hi = qs[0]
        for q in qs:
            if q.cmp(lo) < 0:
                lo = q
            if q.cmp(hi) > 0:
                hi = q
        gate("A3", "n=2: the EXACT RANGE is [-1/2, 1/2]",
             lo == Q2(Fr(-1, 2), 0) and hi == Q2(Fr(1, 2), 0),
             "min %s, max %s, by the exact Q(sqrt 2) sign oracle"
             % (lo, hi))
    tick("A3 %s structure sweep" % tag)
xv, yv = MP.var(2, 0), MP.var(2, 1)
gate("A3", "AM-GM certificate (x+y)^2 - 4xy = (x-y)^2",
     ((xv + yv) * (xv + yv) - 4 * (xv * yv)
      - (xv - yv) * (xv - yv)).is_zero(),
     "on unit rows x + y = 1 gives |A_0|^2 = xy <= 1/4, so |Delta| <= 1/2")
gate("A3", "(H,H) attains both ends of the n=2 range",
     delta_def(K8, H2, H2)[0][0] == HALF
     and delta_def(K8, H2, H2)[0][1] == MHALF)
print()

# ------------------------------------------------- A4 the n-fold coherence law
print("A4.  THE n-FOLD TELESCOPING AND THE TREE COHERENCE LAW")
print("     Write Delta_n(L_1..L_n) := B(L_1...L_n) - B(L_1)...B(L_n).  For")
print("     a binary bracketing T of L_1...L_n define recursively")
print("       Phi(leaf) = 0,")
print("       Phi(T) = Delta^B(U(T_L), U(T_R)) + Phi(T_L) B(U(T_R))")
print("                                        + (prod_L B) Phi(T_R).")
print("     THEOREM: Phi(T) = Delta_n for EVERY bracketing T.  The distinct")
print("     telescopings at n steps number the Catalan number C_{n-1}; the")
print("     two at n = 3 are exactly W1's C+2 coherence law.  The gate uses")
print("     INDEPENDENT polynomial variables for B of every contiguous")
print("     sub-product, so NO PROPERTY OF B IS ASSUMED — not unitarity,")
print("     not positivity, not even that B acts entrywise.")


def all_trees(lo, hi):
    if lo == hi:
        return [lo]
    out = []
    for m in range(lo, hi):
        for L in all_trees(lo, m):
            for R in all_trees(m + 1, hi):
                out.append((L, R))
    return out


def tree_span(T):
    if isinstance(T, int):
        return (T, T)
    return (tree_span(T[0])[0], tree_span(T[1])[1])


def phi_formal(T, Bv, nv, d):
    if isinstance(T, int):
        return ([[MP.const(nv, 0) for _ in range(d)] for _ in range(d)],
                Bv[(T, T)])
    L, R = T
    (la, lb), (ra, rb) = tree_span(L), tree_span(R)
    phiL, prodL = phi_formal(L, Bv, nv, d)
    phiR, prodR = phi_formal(R, Bv, nv, d)
    dlr = mp_sub(Bv[(la, rb)], mp_mm(Bv[(la, lb)], Bv[(ra, rb)], nv))
    t1 = mp_mm(phiL, Bv[(ra, rb)], nv)
    t2 = mp_mm(prodL, phiR, nv)
    tot = [[dlr[i][j] + t1[i][j] + t2[i][j] for j in range(d)]
           for i in range(d)]
    return tot, mp_mm(prodL, prodR, nv)


CATALAN = {2: 1, 3: 2, 4: 5, 5: 14, 6: 42}
print("     caps: FORMAL gate at d = 2 for n = 2..6 (up to 42 bracketings)")
print("     and d = 3 for n = 2..5 (up to 14).")
for d, nmax in ((2, 6), (3, 5)):
    for n in range(2, nmax + 1):
        ivs = [(i, j) for i in range(1, n + 1) for j in range(i, n + 1)]
        nv = len(ivs) * d * d
        Bv = {ij: mp_matrix(nv, t * d * d, d) for t, ij in enumerate(ivs)}
        trees = all_trees(1, n)
        ph0, prod0 = phi_formal(trees[0], Bv, nv, d)
        target = mp_sub(Bv[(1, n)], prod0)
        allok = all(x.is_zero() for r in mp_sub(ph0, target) for x in r)
        for T in trees[1:]:
            ph, prod = phi_formal(T, Bv, nv, d)
            allok &= all(x.is_zero() for r in mp_sub(ph, target) for x in r)
            allok &= all(x.is_zero() for r in mp_sub(prod, prod0)
                         for x in r)
        gate("A4", "TREE coherence: Phi(T) = Delta_%d, all %2d bracketings"
             " [d=%d]" % (n, len(trees), d), allok
             and len(trees) == CATALAN[n],
             "%d formal variables, no property of B assumed" % nv, "[REV2]")
    tick("A4 formal trees d=%d" % d)
n, d = 3, 2
ivs = [(i, j) for i in range(1, n + 1) for j in range(i, n + 1)]
nv = len(ivs) * d * d
Bv = {ij: mp_matrix(nv, t * d * d, d) for t, ij in enumerate(ivs)}
Ls = mp_sub(Bv[(1, 3)], mp_mm(Bv[(1, 2)], Bv[(3, 3)], nv))
Ls2 = mp_mm(mp_sub(Bv[(1, 2)], mp_mm(Bv[(1, 1)], Bv[(2, 2)], nv)),
            Bv[(3, 3)], nv)
Rs = mp_sub(Bv[(1, 3)], mp_mm(Bv[(1, 1)], Bv[(2, 3)], nv))
Rs2 = mp_mm(Bv[(1, 1)], mp_sub(Bv[(2, 3)],
                               mp_mm(Bv[(2, 2)], Bv[(3, 3)], nv)), nv)
gate("A4", "n=3 reduces to W1's C+2 coherence law verbatim",
     all((Ls[i][j] + Ls2[i][j] - Rs[i][j] - Rs2[i][j]).is_zero()
         for i in range(2) for j in range(2)),
     "the two bracketings of three steps", "[W1']")


def phi_exact(K, T, U):
    if isinstance(T, int):
        dd = len(U[T])
        return ([[K.zero] * dd for _ in range(dd)], mB(K, U[T]))
    L, R = T
    (la, lb), (ra, rb) = tree_span(L), tree_span(R)
    UL = U[la]
    for t in range(la + 1, lb + 1):
        UL = mmul(K, UL, U[t])
    UR = U[ra]
    for t in range(ra + 1, rb + 1):
        UR = mmul(K, UR, U[t])
    phiL, prodL = phi_exact(K, L, U)
    phiR, prodR = phi_exact(K, R, U)
    dlr = delta_def(K, UL, UR)
    t1 = mmul(K, phiL, mB(K, UR))
    t2 = mmul(K, prodL, phiR)
    tot = [[K.add(K.add(dlr[i][j], t1[i][j]), t2[i][j])
            for j in range(len(dlr))] for i in range(len(dlr))]
    return tot, mmul(K, prodL, prodR)


print("     caps: EXACT corroboration on a deterministic stride of 4")
print("     matrices from each family; n = 2..5 (2x2), n = 2..4 (3x3);")
print("     every bracketing of every ordered tuple.")
for tag, nmax in (("2x2", 5), ("3x3", 4)):
    K, FAM, Bc, rm, cm, cnt, rows, zflag = CENSUS[tag]
    sub = stride(FAM, 4)
    bad = ntup = 0
    for n in range(2, nmax + 1):
        for combo in itertools.product(range(len(sub)), repeat=n):
            U = {i + 1: sub[c] for i, c in enumerate(combo)}
            tot = U[1]
            prodB = mB(K, U[1])
            for t in range(2, n + 1):
                tot = mmul(K, tot, U[t])
                prodB = mmul(K, prodB, mB(K, U[t]))
            target = msub(K, mB(K, tot), prodB)
            for T in all_trees(1, n):
                if not meq(K, phi_exact(K, T, U)[0], target):
                    bad += 1
            ntup += 1
        tick("A4 exact n=%d [%s]" % (n, tag))
    gate("A4", "TREE coherence on EXACT committed matrices [%s]" % tag,
         bad == 0, "%d ordered tuples, every bracketing, 0 failures" % ntup,
         "[W1']")
print()

# --------------------------------------- A5 the law is content-free about B
print("A5.  THE COHERENCE LAW IS CONTENT-FREE ABOUT THE BORN PROJECTION")
print("     A4's gate assumed nothing about B, so the law holds for ANY map")
print("     whatsoever.  Made concrete and falsifiable-looking: the same")
print("     identity is gated with B replaced by five DECLARED NON-BORN")
print("     maps.  A law that survives replacing its subject constrains the")
print("     subject not at all — the law is an identity of associativity.")


def f_id(K, M):
    return [list(r) for r in M]


def f_re(K, M):
    return [[K.re(x) for x in r] for r in M]


def f_sq(K, M):
    return [[K.mul(x, x) for x in r] for r in M]


def f_tr(K, M):
    return mtr(M)


def f_aff(K, M):
    dd = len(M)
    return [[K.add(K.add(M[i][j], K.scal(M[j][i], 2)),
                   K.rat(3) if i == j else K.zero) for j in range(dd)]
            for i in range(dd)]


print("     caps: a deterministic stride of 6 matrices from each family,")
print("     all 216 ordered triples, both families, five maps.")
for nm, f in (("f = identity", f_id), ("f = entrywise Re", f_re),
              ("f = entrywise square (no modulus)", f_sq),
              ("f = transpose", f_tr), ("f = M + 2 M^T + 3 I", f_aff)):
    allok = True
    ntest = 0
    for tag in ("2x2", "3x3"):
        K, FAM, Bc, rm, cm, cnt, rows, zflag = CENSUS[tag]
        sub = stride(FAM, 6)
        dd = len(sub[0])
        for U3, U2, U1 in itertools.product(sub, repeat=3):
            fU1, fU2, fU3 = f(K, U1), f(K, U2), f(K, U3)
            U21, U32 = mmul(K, U2, U1), mmul(K, U3, U2)
            U321 = mmul(K, U3, U21)
            L1 = msub(K, f(K, U321), mmul(K, f(K, U32), fU1))
            L2 = mmul(K, msub(K, f(K, U32), mmul(K, fU3, fU2)), fU1)
            R1 = msub(K, f(K, U321), mmul(K, fU3, f(K, U21)))
            R2 = mmul(K, fU3, msub(K, f(K, U21), mmul(K, fU2, fU1)))
            allok &= all(K.add(L1[i][j], L2[i][j])
                         == K.add(R1[i][j], R2[i][j])
                         for i in range(dd) for j in range(dd))
            ntest += 1
    gate("A5", "the coherence law holds for %-33s" % nm, allok,
         "%d triples over both families" % ntest)
tick("A5 non-Born maps")
print()

# ---------------------------------------------- A6 the two-sided annihilator
print("A6.  THE TWO-SIDED ANNIHILATOR OF THE FAMILY IS THE MONOMIAL GROUP")
print("     W1' gated SUFFICIENCY (row-monomial U2 or column-monomial U1")
print("     forces Delta^B = 0) and showed it is NOT NECESSARY pairwise.")
print("     Under a UNIVERSAL quantifier it becomes an equivalence:")
print()
print("       K_L := {U2 : Delta^B(U2, V) = 0 for every unitary V}")
print("            =  the ROW-MONOMIAL unitaries, exactly;")
print("       K_R := {U1 : Delta^B(V, U1) = 0 for every unitary V}")
print("            =  the COLUMN-MONOMIAL unitaries, exactly.")
print()
print("     Sufficiency is A1's closed form: at most one w_k is nonzero, so")
print("     the pairwise sum is empty.  Necessity: if row i of U2 has")
print("     nonzero entries a, b at columns k != l, the PROBE")
print("     V = D_m^(k) . R_kl, with R_kl the exact rational rotation")
print("     [[3/5,-4/5],[4/5,3/5]] in the (k,l) plane and D_m^(k) carrying")
print("     i^m at position k, gives")
print("       Delta^B(U2, V)_ik = (24/25) Re( i^m a conj(b) ),")
print("     and Re(z) = Re(iz) = 0 forces z = 0, so m in {0,1} separates")
print("     every non-monomial row.  K_R follows from K_L by A2(v).")
print("     THIS IS A HAND PROOF WITH GATED INGREDIENTS: the closed form")
print("     (A1), the probes' unitarity, the two-phase separation and the")
print("     exhaustive family corroboration are gated; the quantifier over")
print("     ALL unitaries is carried by the argument, not by the sweep.")
gate("A6", "the two-phase separation Re(z) = Re(iz) = 0 => z = 0",
     True, "z = x + iy: Re z = x, Re(iz) = -y; both zero forces z = 0",
     "DECLARATIVE (one line of real algebra)")


def probe(K, d, k, l, m):
    M = [list(r) for r in mid(K, d)]
    c, s = K.rat(Fr(3, 5)), K.rat(Fr(4, 5))
    M[k][k], M[k][l] = c, K.neg(s)
    M[l][k], M[l][l] = s, c
    ph = K.zpow(K.n // 4) if m else K.one
    return [[K.mul(ph, x) if i == k else x for x in r]
            for i, r in enumerate(M)]


for tag in ("2x2", "3x3"):
    K, FAM, Bc, rm, cm, cnt, rows, zflag = CENSUS[tag]
    d = len(FAM[0])
    probes = [probe(K, d, k, l, m) for k in range(d)
              for l in range(k + 1, d) for m in (0, 1)]
    gate("A6", "every probe is unitary in exact arithmetic [%s]" % tag,
         all(is_unitary(K, V) for V in probes),
         "%d probes = 2 phases x %d planes, entries in Q(i) only"
         % (len(probes), d * (d - 1) // 2))
    probesT = [mtr(V) for V in probes]
    unsep_L = unsep_R = nnm_L = nnm_R = suff_bad = 0
    for i, U in enumerate(FAM):
        if rm[i]:
            suff_bad += sum(1 for j in range(len(FAM)) if not zflag[(i, j)])
        else:
            nnm_L += 1
            unsep_L += all(mzero(K, delta_def(K, U, V)) for V in probes)
        if cm[i]:
            suff_bad += sum(1 for j in range(len(FAM)) if not zflag[(j, i)])
        else:
            nnm_R += 1
            unsep_R += all(mzero(K, delta_def(K, V, U)) for V in probesT)
    gate("A6", "SUFFICIENCY re-gated through the closed form [%s]" % tag,
         suff_bad == 0, "a monomial slot kills Delta^B against the whole "
         "family")
    gate("A6", "NECESSITY: every non-row-monomial U2 is separated [%s]" % tag,
         unsep_L == 0, "%d non-row-monomial members, %d unseparated"
         % (nnm_L, unsep_L))
    gate("A6", "NECESSITY: every non-col-monomial U1 is separated [%s]" % tag,
         unsep_R == 0, "%d non-col-monomial members, %d unseparated"
         % (nnm_R, unsep_R))
    mono = [U for i, U in enumerate(FAM) if rm[i]]
    gate("A6", "B|Mon IS a homomorphism onto the permutations [%s]" % tag,
         all(mzero(K, delta_def(K, U, V)) for U in mono for V in mono)
         and all(x in (K.zero, K.one) for U in mono for r in mB(K, U)
                 for x in r),
         "%d monomial members; the WHOLE torus T^n is in the kernel — the "
         "wall's structural form" % len(mono))
    tick("A6 %s annihilator sweep" % tag)
print()

# ------------------------------- A7 pairwise flatness does not imply n-fold
print("A7.  PAIRWISE FLATNESS DOES NOT IMPLY n-FOLD FLATNESS")
print("     The coherence law gives Delta_3 = Delta^B(U3, U2U1) +")
print("     B(U3) Delta^B(U2,U1); with both consecutive defects zero the")
print("     first term survives.  The defect is NOT locally determined —")
print("     flatness at every cut of a chain does not make the chain flat.")
for tag in ("2x2", "3x3"):
    K, FAM, Bc, rm, cm, cnt, rows, zflag = CENSUS[tag]
    found = None
    nseen = 0
    for i3 in range(len(FAM)):
        for i2 in range(len(FAM)):
            if not zflag[(i3, i2)]:
                continue
            for i1 in range(len(FAM)):
                if not zflag[(i2, i1)]:
                    continue
                nseen += 1
                U321 = mmul(K, FAM[i3], mmul(K, FAM[i2], FAM[i1]))
                pB = mmul(K, Bc[i3], mmul(K, Bc[i2], Bc[i1]))
                if not mzero(K, msub(K, mB(K, U321), pB)):
                    found = (i3, i2, i1)
                    break
            if found:
                break
        if found:
            break
    gate("A7", "an exhibited triple: both cuts flat, Delta_3 != 0 [%s]" % tag,
         found is not None, "family indices %s, found after %d pairwise-flat "
         "triples" % (found, nseen))
    tick("A7 %s consecutive-flat scan" % tag)
print()

# ------------------------- A8 the generalized phase-alignment closed form
print("A8.  THE GENERALIZED PHASE-ALIGNMENT CLOSED FORM, ALL N")
print("     On the DFT-sandwich family U2 = D_a F_N D_b, U1 = D_c F_N D_e")
print("     (F_N the unitary DFT, D's diagonal unitary) one has")
print("     B(U2) = B(U1) = J/N, so Delta^B = 0 iff B(F_N E F_N) = J/N with")
print("     E = D_b D_c the INTERLEAVING diagonal.  Since")
print("     (F_N E F_N)_jk = (1/N) sum_m eps_m omega^{m(j+k)}, the entries")
print("     are the DFT of the unimodular sequence eps read at j+k, so")
print()
print("       Delta^B = 0  <=>  |DFT(eps)(s)| = sqrt(N) for every s")
print("                    <=>  eps has ZERO periodic autocorrelation at")
print("                         every nonzero lag (a CAZAC sequence).")
print()
print("     Delta^B = 0 is PHASE ALIGNMENT, and the alignment condition is")
print("     FLATNESS OF A FOURIER SPECTRUM.  W1's two committed closed")
print("     forms are the N = 2 and N = 3 cases.")
print("     caps: eps_0 = 1 fixed (an outer scalar is annihilated by A2);")
print("     N=2 eps in mu_8 over Q(zeta_8); N=3 in mu_6 over Q(zeta_12);")
print("     N=4 in mu_8 over Q(zeta_8); N=5 in mu_5 over Q(zeta_5).")
A8_TAB = []
for N, K, rootstep, phorder, invs in (
        (2, FIELDS[8], 4, 8, K8.inv(SQRT2_8)),
        (3, FIELDS[12], 4, 6, K12.inv(SQRT3_12)),
        (4, FIELDS[8], 2, 8, K8.rat(Fr(1, 2))),
        (5, FIELDS[5], 1, 5, FIELDS[5].inv(SQRT5_5))):
    FN = [[K.mul(K.zpow((rootstep * i * j) % K.n), invs) for j in range(N)]
          for i in range(N)]
    gate("A8", "F_%d is unitary in exact arithmetic [Q(zeta_%d)]"
         % (N, K.n), is_unitary(K, FN))
    st = K.n // phorder
    oneN = K.rat(Fr(1, N))
    nflat = ntot = mism_spec = mism_auto = 0
    for tail in itertools.product(range(phorder), repeat=N - 1):
        eps = [K.one] + [K.zpow(st * t) for t in tail]
        M = mmul(K, mmul(K, FN, mdiag(K, eps)), FN)
        flat = all(x == oneN for r in mB(K, M) for x in r)
        spec = all(K.mul(a, K.conj(a)) == K.rat(N) for a in
                   [ksum(K, [K.mul(eps[m], K.zpow((rootstep * m * s) % K.n))
                             for m in range(N)]) for s in range(N)])
        auto = all(K.is_zero(ksum(K, [K.mul(eps[m], K.conj(eps[(m + lag) % N]))
                                      for m in range(N)]))
                   for lag in range(1, N))
        mism_spec += (flat != spec)
        mism_auto += (flat != auto)
        nflat += flat
        ntot += 1
    A8_TAB.append((N, ntot, nflat))
    gate("A8", "Delta^B = 0  <=>  FLAT SPECTRUM  [N=%d]" % N,
         mism_spec == 0, "%d interleaving diagonals, %d flat, 0 mismatches"
         % (ntot, nflat))
    gate("A8", "flat spectrum <=> zero periodic autocorrelation [N=%d]" % N,
         mism_auto == 0, "the Wiener-Khinchin equivalence, exactly")
    tick("A8 N=%d" % N)
tu_ok = all(all(x == K8.rat(Fr(1, 2)) for row in
                mB(K8, mmul(K8, mmul(K8, H2,
                                     mdiag(K8, [K8.one, K8.zpow(r)])), H2))
                for x in row) == (r in (2, 6)) for r in range(8))
gate("A8", "N=2 flatness reproduces W1's t+u = +-2 (mod 8)", tu_ok,
     "8 interleaving phases", "[W1']")
m3_ok = all(all(x == K12.rat(Fr(1, 3)) for row in
                mB(K12, mmul(K12, mmul(K12, F3M,
                                       mdiag(K12, [K12.one, K12.zpow(m),
                                                   K12.one])), F3M))
                for x in row) == (m != 0) for m in (0, 4, 8))
gate("A8", "N=3 flatness reproduces W1's b2+a1 != 0 (mod 3)", m3_ok,
     "the D(m) = diag(1, omega^m, 1) sub-family", "[W1']")
print()

# ------------------------------------- A9 the conditionings that kill it
print("A9.  THE CONDITIONINGS THAT KILL THE FAMILY  (reporting-only: the")
print("     general record theorem is W3's, not this unit's)")
print("     Exactly three shapes appear, and A1 says why:")
print("       (a) SUPPORT — at most one w_k nonzero (A1; sufficient only);")
print("       (b) ALGEBRAIC — a monomial slot (A6; exact under a universal")
print("           quantifier);")
print("       (c) CONDITIONING AT THE CUT — the dephasing channel D, which")
print("           replaces sum_k w_k by an incoherent sum.  Interleaving D")
print("           at EVERY cut kills Delta_n identically, for every n.")
for tag, K, U2, U1 in (("H.H", K8, H2, H2), ("F3.F3", K12, F3M, F3M)):
    d = len(U1)
    ok = True
    for n in (2, 3, 4):
        Us = ([U2, U1] * 3)[:n]
        acc = mB(K, Us[0])
        for U in Us[1:]:
            acc = mmul(K, acc, mB(K, U))
        out = [[K.zero] * d for _ in range(d)]
        for j in range(d):
            rho = [[K.zero] * d for _ in range(d)]
            rho[j][j] = K.one
            for U in reversed(Us):
                rho = mmul(K, mmul(K, U, rho), mdag(K, U))
                rho = [[rho[i][i] if i == k else K.zero for k in range(d)]
                       for i in range(d)]
            for i in range(d):
                out[i][j] = rho[i][i]
        ok &= meq(K, out, acc)
    gate("A9", "D at every cut kills Delta_n, n = 2,3,4 [%s]" % tag, ok,
         "the D-interleaved shadow IS the product of the Born shadows",
         "[W1']")
print()


# ============================================================================
head("SECTION W2b — PROJECTIVE DESCENT")
# ============================================================================
print("  THE TARGET, made precise before anything is run.  W2b asks for")
print("  three things at once:")
print("    (1) a committed object supplying a homomorphism")
print("        rho : Z^2 -> PU(H) — the generated group ACTING;")
print("    (2) a lift rho~ : Z^2 -> U(H) whose multiplier")
print("        omega(g,h) = rho~(g) rho~(h) rho~(g+h)^-1 has [omega] != 0")
print("        in H^2_grp(Z^2, U(1)) — the Weyl relation")
print("        U V = e^{2 pi i theta} V U;")
print("    (3) a functional F of the Delta^B-family that the multiplier")
print("        CONTROLS: constant on fixed-theta data, and separating")
print("        different theta.")
print("  All three are required.  (3) is what 'the multiplier controls a")
print("  Delta-invariant' means, and it is decided first, because it")
print("  decides itself.")
print()

# ------------------------------------------------ B1 the generated group
print("B1.  THE GENERATED Z^2, from the committed instrument")
print("     D74's <2,3> is the group of the TRANSPORT HOLONOMY VALUES: the")
print("     image of the loops of the menu quotient under the holonomy map,")
print("     computed as an integer exponent lattice.  Section 0.3 anchored")
print("     it: prime support [2,3], rank 2, index 1 in Z^2.")
gate("B1", "the generated group is free abelian of rank 2",
     GRP["rank"] == 2 and GRP["index"] == 1, GRP["name"], "[D74]")
gate("B1", "its values are POSITIVE RATIONALS: it sits in (R+, x)",
     all(v > 0 for v in D74_VALUES)
     and all(set(primes_of(v)) <= {2, 3} for v in D74_VALUES),
     "value set {1/2, 2/3, 3/2, 2}", "[D74]")
gate("B1", "R+ meets U(1) in {1}: NO unimodular part is available",
     all(abs(v) != 1 for v in D74_VALUES),
     "D74's D2 in one line — the only positive rational of modulus 1 is 1, "
     "so the only possible U(1) content is the sign -1, realized nowhere",
     "[D74]")
print("     WHAT THIS IS AND IS NOT: a group of VALUES, not a group of")
print("     TRANSFORMATIONS.  D74 exhibits no action of <2,3> on anything;")
print("     the holonomy map runs FROM loops TO this group.  Requirement")
print("     (1) is not in the committed record.")
print()

# ---------------------------------------- B2 what [omega] actually is
print("B2.  WHAT [omega] IS: THE ALTERNATING BICHARACTER — AND IT IS A")
print("     SCALAR.  For Z^2 with trivial action, [omega] in")
print("     H^2_grp(Z^2, U(1)) is determined by the ANTISYMMETRIZATION")
print("       beta(g,h) := omega(g,h) / omega(h,g),")
print("     an alternating bicharacter invariant under coboundaries; and")
print("     for ANY lift, rho~(g) rho~(h) rho~(g)^-1 rho~(h)^-1 =")
print("     beta(g,h) . I is a SCALAR MATRIX.  So the complete invariant of")
print("     the class is exactly a scalar — and B annihilates scalars.")
print("     Gated on the finite models Z_m x Z_m, m = 2..6.")
for m in (2, 3, 4, 5, 6):
    K = FIELDS[m]
    G = [(a, b) for a in range(m) for b in range(m)]

    def wcoc(k, g, h, K=K, m=m):
        return K.zpow((k * g[1] * h[0]) % K.n)

    coc_ok = True
    for k in range(m):
        for g in G:
            for h in G:
                for j in G:
                    gh = ((g[0] + h[0]) % m, (g[1] + h[1]) % m)
                    hj = ((h[0] + j[0]) % m, (h[1] + j[1]) % m)
                    coc_ok &= (K.mul(wcoc(k, g, h), wcoc(k, gh, j))
                               == K.mul(wcoc(k, h, j), wcoc(k, g, hj)))
    gate("B2", "the Weyl cocycles are normalized 2-cocycles [Z_%d^2]" % m,
         coc_ok and all(wcoc(k, (0, 0), g) == K.one
                        and wcoc(k, g, (0, 0)) == K.one
                        for k in range(m) for g in G),
         "%d classes, %d associativity checks each" % (m, len(G) ** 3))
    betas = {k: K.mul(wcoc(k, (1, 0), (0, 1)),
                      K.inv(wcoc(k, (0, 1), (1, 0)))) for k in range(m)}
    gate("B2", "beta(e1,e2) separates all %d Weyl classes [Z_%d^2]" % (m, m),
         len(set(betas.values())) == m,
         "beta takes %d distinct values in mu_%d" % (len(set(betas.values())),
                                                     m))
    nalt = 0
    for M in itertools.product(range(m), repeat=4):
        if all((M[0] * g[0] * g[0] + (M[1] + M[2]) * g[0] * g[1]
                + M[3] * g[1] * g[1]) % m == 0 for g in G):
            nalt += 1
    gate("B2", "exactly %d alternating bicharacters on Z_%d^2" % (m, m),
         nalt == m, "H^2(Z_%d^2, U(1)) = Z_%d, realized by the Weyl cocycles"
         % (m, m))
    if m <= 3:
        nlam = 0
        inv_ok = True
        nz = [g for g in G if g != (0, 0)]
        for lam in itertools.product(range(m), repeat=len(nz)):
            L = {(0, 0): 0}
            for idx, g in enumerate(nz):
                L[g] = lam[idx]
            for k in range(m):
                def w2(g, h, k=k, L=L, K=K, m=m):
                    gh = ((g[0] + h[0]) % m, (g[1] + h[1]) % m)
                    return K.mul(wcoc(k, g, h),
                                 K.zpow(((L[g] + L[h] - L[gh])
                                         * (K.n // m)) % K.n))
                inv_ok &= (K.mul(w2((1, 0), (0, 1)),
                                 K.inv(w2((0, 1), (1, 0)))) == betas[k])
            nlam += 1
        gate("B2", "beta is coboundary-invariant [Z_%d^2]" % m, inv_ok,
             "ALL %d normalized 1-cochains x %d classes" % (nlam, m))
tick("B2 finite models")
print()

# -------------------------------------- B3 THE MULTIPLIER CANCELS
print("B3.  THE MULTIPLIER CANCELS FROM THE ENTIRE Delta^B-FAMILY")
print("     THEOREM.  Let rho~ : G -> U(N) be any projective representation")
print("     with multiplier omega, and put beta_B := B o rho~.  Then")
print("     beta_B is INDEPENDENT OF THE LIFT (B kills the scalars) and")
print("       Delta^B(rho~(g), rho~(h))")
print("           = B(omega(g,h) rho~(gh)) - B(rho~(g)) B(rho~(h))")
print("           = beta_B(gh) - beta_B(g) beta_B(h).")
print("     The multiplier does not appear.  The whole Delta^B-family of a")
print("     projective representation is the DEVIATION OF beta_B FROM BEING")
print("     A HOMOMORPHISM, and beta_B is a function of the PU(N)-valued")
print("     map alone.  This promotes the wall B(omega U) = B(U) from a")
print("     pointwise remark to a statement about the entire family.")
WEYL = {}
for N in (2, 3, 4, 5, 6):
    K = FIELDS[N]
    X = [[K.one if (i - j) % N == 1 else K.zero for j in range(N)]
         for i in range(N)]
    Z = mdiag(K, [K.zpow(j) for j in range(N)])
    WEYL[N] = (K, X, Z)
    gate("B3", "clock/shift unitary, X Z = zeta^-1 Z X [N=%d]" % N,
         is_unitary(K, X) and is_unitary(K, Z)
         and meq(K, mmul(K, X, Z),
                 [[K.mul(K.conj(K.z), x) for x in r]
                  for r in mmul(K, Z, X)]),
         "the Weyl pair over Q(zeta_%d)" % K.n, "[W]")
    words = {}
    for a in range(N):
        for b in range(N):
            Uw = mid(K, N)
            for _ in range(a):
                Uw = mmul(K, Uw, X)
            for _ in range(b):
                Uw = mmul(K, Uw, Z)
            words[(a, b)] = Uw
    li = all(meq(K, mB(K, [[K.mul(K.zpow(s), x) for x in r] for r in Uw]),
                 mB(K, Uw))
             for Uw in words.values() for s in range(K.n))
    gate("B3", "beta_B is lift-independent on every word [N=%d]" % N, li,
         "%d words x %d scalars" % (len(words), K.n), "[REV2]")
    WEYL[N] = (K, X, Z, words)
tick("B3 lift-independence")
print()

# ------------------------------------------- B4 the collision exhibit
print("B4.  THE COLLISION EXHIBIT: SAME beta_B, DIFFERENT [omega]")
print("     Take U = X_N (shift) and V = Z_N^k (clock power), k = 0..N-1.")
print("     The commutator is zeta_N^{-k} I, so the multiplier class has")
print("     order N/gcd(N,k) — every class realizable on C^N, the trivial")
print("     one included.  But B(Z_N^k) = I for EVERY k, so")
print("       beta_B(a,b) = B(X^a Z^{kb}) = P^a,  P = the shift permutation,")
print("     INDEPENDENT OF k.  All N classes share one and the same")
print("     beta_B, hence one and the same Delta^B-family — which is")
print("     identically zero.")
print("     caps: all N^2 words per class; the Delta^B sweep is all N^4")
print("     ordered word pairs for N <= 4 and the 9x9 sub-block a,b < 3 for")
print("     N = 5, 6 (printed per row).")
B4_TAB = []
for N in (2, 3, 4, 5, 6):
    K, X, Z, _ = WEYL[N]
    lim = N if N <= 4 else 3
    betas, orders, dzero = {}, {}, {}
    for k in range(N):
        Zk = mid(K, N)
        for _ in range(k):
            Zk = mmul(K, Zk, Z)
        C = mmul(K, mmul(K, X, Zk), mmul(K, mdag(K, X), mdag(K, Zk)))
        sc = C[0][0]
        is_sc = meq(K, C, [[sc if i == j else K.zero for j in range(N)]
                           for i in range(N)])
        o, acc = 1, sc
        while acc != K.one and o <= N:
            acc = K.mul(acc, sc)
            o += 1
        orders[k] = o if is_sc else None
        wl = []
        for a in range(N):
            for b in range(N):
                Uw = mid(K, N)
                for _ in range(a):
                    Uw = mmul(K, Uw, X)
                for _ in range(b):
                    Uw = mmul(K, Uw, Zk)
                wl.append(((a, b), Uw))
        betas[k] = tuple(tuple(tuple(x) for x in mB(K, Uw))
                         for ab, Uw in wl)
        small = [Uw for ab, Uw in wl if ab[0] < lim and ab[1] < lim]
        dzero[k] = all(mzero(K, delta_def(K, P, Q))
                       for P in small for Q in small)
    ords = sorted({o for o in orders.values() if o})
    same = len(set(betas.values())) == 1
    B4_TAB.append((N, ords, same, all(dzero.values())))
    gate("B4", "all %d multiplier classes share ONE beta_B [N=%d]" % (N, N),
         same and all(o is not None for o in orders.values()),
         "multiplier orders present: %s" % ", ".join(str(o) for o in ords),
         "[W]")
    gate("B4", "and the Delta^B-family is IDENTICALLY ZERO on all of them"
         " [N=%d]" % N, all(dzero.values()),
         "%d ordered word pairs per class (cap a,b < %d)"
         % ((lim * lim) ** 2, lim))
    tick("B4 N=%d" % N)
print("     At N = 6 the classes have orders 1, 2, 3 and 6 — four distinct")
print("     elements of H^2(Z^2, U(1)), the trivial one among them —")
print("     carried by realizations with literally identical Born data.  NO")
print("     FUNCTIONAL OF THE Delta^B-FAMILY CAN SEPARATE THEM.")
print()

# -------------------------------- B5 Delta on monomial realizations
print("B5.  EVERY MONOMIAL REALIZATION IS Delta^B-FLAT, AT EVERY theta —")
print("     AND BREAKING MONOMIALITY HANDS CONTROL TO THE BASIS")
print("     The Weyl pair is monomial, and A6 makes the monomial group the")
print("     exact annihilator of the family.  So the canonical realization")
print("     of [W]'s own object — the only irreducible one at a primitive")
print("     multiplier, by [SvN] — carries no defect at all.  Conjugating")
print("     it by an exact rational rotation preserves theta and creates a")
print("     defect; two different conjugators at the SAME theta create")
print("     DIFFERENT defects.  The basis controls the family; theta does")
print("     not.")
KB = K8
XP = [[KB.zero, KB.one], [KB.one, KB.zero]]
ZP = mdiag(KB, [KB.rat(1), KB.rat(-1)])
CONJ = [("R(3/5,4/5)", [[KB.rat(Fr(3, 5)), KB.rat(Fr(-4, 5))],
                        [KB.rat(Fr(4, 5)), KB.rat(Fr(3, 5))]]),
        ("R(5/13,12/13)", [[KB.rat(Fr(5, 13)), KB.rat(Fr(-12, 13))],
                           [KB.rat(Fr(12, 13)), KB.rat(Fr(5, 13))]])]
gate("B5", "the base Weyl pair is monomial and Delta^B-flat",
     mzero(KB, delta_def(KB, XP, ZP))
     and mzero(KB, delta_def(KB, ZP, XP)),
     "commutator -I, theta = 1/2", "[W]")
B5_DELTAS = []
for nm, Wc in CONJ:
    Wd = mdag(KB, Wc)
    gate("B5", "%-14s is unitary in exact arithmetic" % nm,
         is_unitary(KB, Wc))
    Xc = mmul(KB, mmul(KB, Wc, XP), Wd)
    Zc = mmul(KB, mmul(KB, Wc, ZP), Wd)
    comm = mmul(KB, mmul(KB, Xc, Zc), mmul(KB, mdag(KB, Xc), mdag(KB, Zc)))
    dv = delta_def(KB, Xc, Zc)
    B5_DELTAS.append(dv)
    gate("B5", "conjugation by %-14s preserves theta = 1/2" % nm,
         meq(KB, comm, [[KB.rat(-1), KB.zero], [KB.zero, KB.rat(-1)]]),
         "the commutator is still -I", "[W]")
    gate("B5", "... and creates a defect: Delta^B(X',Z') != 0 [%s]" % nm,
         not mzero(KB, dv), "Delta^B_00 = %s"
         % to_q2(dv[0][0]))
gate("B5", "SAME theta, DIFFERENT Delta^B-family",
     not meq(KB, B5_DELTAS[0], B5_DELTAS[1]),
     "two conjugators, one class: the basis controls the defect")
print()

# --------------------- B6 the exhaustive projective-pair census, committed
print("B6.  THE EXHAUSTIVE PROJECTIVE-PAIR CENSUS OVER W1's COMMITTED")
print("     FAMILIES — AND THE DOUBLE DISSOCIATION IT EXHIBITS.")
print("     For every ordered pair (U,V) of each family: is the group")
print("     commutator U V U^-1 V^-1 a SCALAR — so that the pair generates")
print("     a projective Z^2-action whose beta(e1,e2) is that scalar (B2) —")
print("     and what is the Delta^B-family of the generated words?  No")
print("     sampling: all 9216 + 3969 ordered pairs are classified, and for")
print("     every projective pair the FULL FINGERPRINT of the family is")
print("     recorded (all 81 ordered pairs of the 9 words U^a V^b,")
print("     a, b < 3) so that families can be compared across theta.")
print("     THE SWEEP REFUTES THE FLATNESS EXPECTATION: non-monomial")
print("     committed projective pairs exist and their families are NOT")
print("     zero.  What the sweep then measures is the thing that matters —")
print("     whether theta and the family determine each other.  They do")
print("     not, in EITHER direction.")
B6_TAB = {}
for tag in ("2x2", "3x3"):
    K, FAM, Bc, rm, cm, cnt, rows, zflag = CENSUS[tag]
    d = len(FAM[0])
    invs = [mdag(K, U) for U in FAM]
    byscalar = {}
    for i, U in enumerate(FAM):
        for j, V in enumerate(FAM):
            C = mmul(K, mmul(K, U, V), mmul(K, invs[i], invs[j]))
            sc = C[0][0]
            if not meq(K, C, [[sc if a == b else K.zero for b in range(d)]
                              for a in range(d)]):
                continue
            words = []
            for a in range(3):
                for b in range(3):
                    Wd = mid(K, d)
                    for _ in range(a):
                        Wd = mmul(K, Wd, U)
                    for _ in range(b):
                        Wd = mmul(K, Wd, V)
                    words.append(Wd)
            fp = tuple(tuple(tuple(x) for x in delta_def(K, P, Q))
                       for P in words for Q in words)
            rec = byscalar.setdefault(sc, {"n": 0, "fams": {}, "mm": 0,
                                           "mm_flat": 0})
            rec["n"] += 1
            rec["fams"].setdefault(fp, 0)
            rec["fams"][fp] += 1
            if rm[i] and rm[j]:
                rec["mm"] += 1
                rec["mm_flat"] += all(all(all(y == 0 for y in e)
                                          for e in row) for m in fp
                                      for row in m)

    def order_of(sc, K=K):
        o, acc = 1, sc
        while acc != K.one and o <= K.n:
            acc = K.mul(acc, sc)
            o += 1
        return o

    def is_zero_fp(fp):
        return all(all(all(y == 0 for y in e) for e in row)
                   for m in fp for row in m)

    def theta_of(sc, K=K):
        for m in range(K.n):
            if K.zpow(m) == sc:
                return Fr(m, K.n)
        return None

    rowsum = []
    for sc, rec in sorted(byscalar.items()):
        zf = [f for f in rec["fams"] if is_zero_fp(f)]
        rowsum.append((theta_of(sc), order_of(sc), rec["n"],
                       len(rec["fams"]), bool(zf), rec["mm"],
                       rec["mm_flat"]))
    rowsum.sort()
    print("     [%s] commutator-scalar classes, exact:" % tag)
    print("       %-9s %-7s %8s %10s %9s %12s"
          % ("theta", "order", "pairs", "families", "zero fam",
             "mono x mono"))
    for th, o, n, nf, zf, mm, mmf in rowsum:
        print("       %-9s %-7d %8d %10d %9s %12d"
              % (th, o, n, nf, zf, mm))
    tot = sum(r[2] for r in rowsum)
    nontriv = [r for r in rowsum if r[1] > 1]
    hist = {}
    for th, o, n, nf, zf, mm, mmf in rowsum:
        hist[o] = hist.get(o, 0) + n
    B6_TAB[tag] = rowsum
    gate("B6", "projective pairs found and classified [%s]" % tag, True,
         "of %d ordered pairs, %d have a SCALAR commutator; beta-order "
         "histogram %s; theta values realized %s"
         % (len(FAM) ** 2, tot, dict(sorted(hist.items())),
            [str(r[0]) for r in rowsum]), "DATA")
    gate("B6", "MONOMIAL x MONOMIAL projective pairs are Delta^B-flat [%s]"
         % tag, all(r[5] == r[6] for r in rowsum),
         "%d such pairs, all flat — A6's prediction, at every theta"
         % sum(r[5] for r in rowsum))
    nzfam = sum(r[3] - (1 if r[4] else 0) for r in nontriv)
    gate("B6", "FINDING: committed projective pairs with theta != 0 carry "
         "NONZERO families [%s]" % tag, nzfam > 0,
         "%d distinct nonzero Delta^B-families across the theta != 0 "
         "classes — the flatness expectation is REFUTED by the sweep"
         % nzfam)
    gate("B6", "SPLIT: theta does NOT determine the Delta^B-family [%s]"
         % tag, all(r[3] > 1 for r in nontriv),
         "at each fixed theta != 0 the committed carriers realize %s "
         "distinct families" % ", ".join(str(r[3]) for r in nontriv))
    shared = [str(r[0]) for r in rowsum if r[4]]
    gate("B6", "COLLISION: the Delta^B-family does NOT determine theta [%s]"
         % tag, len(shared) > 1,
         "one and the same family (the identically zero one) is realized at "
         "theta = %s" % ", ".join(shared))
    tick("B6 %s projective census" % tag)
print()

# ------------------------------------------------- B7 the parity obstruction
print("B7.  THE PARITY OBSTRUCTION")
print("     A2(v) is the family's reversal law: under")
print("     R : (U2,U1) -> (U1^T, U2^T) — reverse the order, transpose each")
print("     step — Delta^B goes to its TRANSPOSE.  Hence every scalar")
print("     functional of Delta^B that is transpose-invariant (the trace,")
print("     the entry sums, the Frobenius norm, every symmetric function of")
print("     the spectrum) is REVERSAL-EVEN.")
print("     A U(1) holonomy is reversal-ODD by definition:")
print("     Hol(gamma^-1) = conj(Hol(gamma)).  That is [D71b] Clause 2's")
print("     finding — the corpus's only phase-shaped amplitude is placed on")
print("     the reversal-ODD channel, at dual-conjugation error exactly 0,")
print("     and no other placement transforms like a holonomy.")
print("     A quantity that is BOTH reversal-even AND unimodular satisfies")
print("     z = conj(z) and |z| = 1, hence z = +-1; and -1 is realized")
print("     nowhere in the committed values ([D74] D2).  The multiplier and")
print("     the defect sit on OPPOSITE PARITY CHANNELS.")
zx = MP.var(1, 0)
gate("B7", "even and unimodular forces z = +-1",
     (zx * zx - MP.const(1, 1)
      - (zx - MP.const(1, 1)) * (zx + MP.const(1, 1))).is_zero(),
     "z = conj(z) gives y = 0; x^2 = 1 factors as (x-1)(x+1) = 0")
for tag in ("2x2", "3x3"):
    K, FAM, Bc, rm, cm, cnt, rows, zflag = CENSUS[tag]
    d = len(FAM[0])
    bad = 0
    treven = 0
    for i2, i1, D, z in rows:
        Drev = delta_def(K, mtr(FAM[i1]), mtr(FAM[i2]))
        if not meq(K, mtr(D), Drev):
            bad += 1
        if ksum(K, [D[a][a] for a in range(d)]) \
                != ksum(K, [Drev[a][a] for a in range(d)]):
            treven += 1
    gate("B7", "the reversal law on EVERY census pair [%s]" % tag, bad == 0,
         "%d ordered pairs, 0 violations" % len(rows))
    gate("B7", "tr Delta^B is reversal-EVEN on every census pair [%s]" % tag,
         treven == 0, "%d pairs; the same holds for every transpose-"
         "invariant functional" % len(rows))
    tick("B7 %s parity sweep" % tag)
print()

# --------------------------------------------- B8 the missing-piece census
print("B8.  THE MISSING-PIECE CENSUS — EVERY COMMITTED CANDIDATE, AND")
print("     EXACTLY WHAT EACH ONE LACKS")
CENSUS_ROWS = [
    ("CAND-1  D74's transport holonomy r, group <2,3>",
     "a group of VALUES in (R+, x); no committed action on any space; "
     "R+ meets U(1) in {1} ([D74] D2, re-gated at B1)",
     "MISSING: the action rho : Z^2 -> PU(H), and a U(1)-valued cocycle"),
    ("CAND-2  the i-twist L' = e^{i log r}  ([D74] D4.1)",
     "committed and committed-DEAD — the law it restores is D1's own "
     "identity; cohomologically log r is a HOLONOMY, an H^1 object, and "
     "e^{i log r} is a character-valued H^1 object",
     "MISSING: the antisymmetric BILINEAR pairing that an H^2 class IS "
     "(B2)"),
    ("CAND-3  v7 paper 30's amplitude e^{-kE} e^{i Phi(O)}  ([D71b] 3.2)",
     "a phase built from a LINEAR functional Phi of the reversal-odd "
     "channel O = F - F*: a character, not a multiplier; and B7 puts it on "
     "the opposite parity channel from Delta^B",
     "MISSING: the pairing; the closure; and the parity is wrong"),
    ("CAND-4  D42b4's prod sqrt(q) amplitude  ([D71b] 4.2)",
     "the right carrier — it IS the square root of the process's own "
     "weights — but assigned PER COMPLETE HISTORY, with zero occurrences "
     "of loop/cycle/closure/holonomy in its note and its phase slot filled "
     "with +1 without an argument",
     "MISSING: the closure device, hence any commutator at all"),
    ("CAND-5  W1's U(1)-Gram edge phases g_ab = z_a conj(w_b)",
     "committed and gated: the 4-cycle holonomy is IDENTICALLY 1 on 8192 "
     "quadruples — every factorized edge phase is a coboundary",
     "MISSING: non-factorizability; the class is zero by construction"),
    ("CAND-6  the canonical Weyl / NC-torus pair  ([W])",
     "the action EXISTS and [omega] != 0 for every theta in (1/N)Z — but "
     "it is monomial, so by A6/B5 its Delta^B-family is identically zero, "
     "and by B4 all N classes share one Born shadow",
     "NOT MISSING, REFUTING: the action exists and controls nothing"),
    ("CAND-7  W1's committed families as carriers (B6)",
     "exhaustive over 13185 ordered pairs: 1999 generate a projective "
     "Z^2-action, and the non-monomial ones DO carry a nonzero "
     "Delta^B-family — but the same theta carries several families and the "
     "same family occurs at several theta",
     "NOT MISSING, REFUTING: the committed carriers realize the action and "
     "the correspondence fails in both directions at once"),
]
for a, b, c in CENSUS_ROWS:
    print("     %s" % a)
    print("         status : %s" % b)
    print("         verdict: %s" % c)
gate("B8", "the census covers the corpus's phase candidates", True,
     "7 candidates: D74's r, the i-twist, v7 p30's amplitude, D42b4's "
     "prod sqrt(q), W1's Gram edge phases, the Weyl pair, W1's families",
     "DATA")
print()

B3_OK = all(ok for s, n, ok, d, t in GATES if s == "B3")
B4_OK = all(ok for s, n, ok, d, t in GATES if s == "B4")
B5_OK = all(ok for s, n, ok, d, t in GATES if s == "B5")
B6_OK = all(ok for s, n, ok, d, t in GATES if s == "B6")
B7_OK = all(ok for s, n, ok, d, t in GATES if s == "B7")
NO_ACTION = B3_OK and B4_OK and B5_OK and B6_OK and B7_OK
print("     THE VERDICT, SPLIT BY REQUIREMENT, so that it says exactly what")
print("     it means:")
print("       (1) the ACTION.  D74's <2,3> never acts — it is a group of")
print("           values (B1).  But OTHER committed objects do carry")
print("           projective Z^2-actions: 1999 of W1's 13185 ordered pairs")
print("           (B6).  Requirement (1) is met, by carriers unrelated to")
print("           the generated group.")
print("       (2) the CLASS.  Those carriers realize theta = 1/2 (2x2) and")
print("           theta = 1/3, 2/3 (3x3) — genuinely nontrivial classes.")
print("           Requirement (2) is met.")
print("       (3) the CONTROL.  This is what fails, and it fails as a")
print("           theorem (B3) and twice over as a measurement (B4, B6).")
print("     So W2b-NO-ACTION names the failure precisely: not that no")
print("     projective action can be built from committed objects, but that")
print("     the multiplier of any such action is invisible to the")
print("     Delta^B-family — and that the generated Z^2 in particular is")
print("     not the group that acts.")
gate("B9", "W2b VERDICT: NO-ACTION" if NO_ACTION
     else "W2b VERDICT: a functional survives — ACTION-FOUND", True,
     "requirements (1) and (2) are MET by W1's committed families and NOT "
     "by the generated <2,3>; requirement (3) FAILS: B3 the multiplier "
     "cancels from the family identically; B4 four classes with one Born "
     "shadow; B5 one theta, two bases, two families; B6 the double "
     "dissociation on the committed carriers themselves; B7 the parities "
     "are opposite", "DATA")
print()


# ============================================================================
head("SECTION W2c — SELECTION")
# ============================================================================
print("  W2c runs only if W2b yields a genuine class controlling a")
print("  Delta-invariant.  It does not.  W2c is VACUOUS.")
print("  Two facts are gated anyway, because they are what any future")
print("  bridge would face, and because a vacuous verdict that names its")
print("  own conditions is worth more than one that does not.")
print()
print("C1.  theta IS QUANTIZED BY DIMENSION.  From U V = omega V U on C^N,")
print("     det(UV) = det(U) det(V) while det(omega V U) = omega^N det(V)")
print("     det(U), so omega^N = 1: on C^N only theta in (1/N)Z is")
print("     realizable, and the continuum H^2(Z^2, U(1)) = U(1) is reached")
print("     only in a limit.  No committed object supplies N.")
for d in (2, 3):
    nv = 2 * d * d
    A = mp_matrix(nv, 0, d)
    Bm = mp_matrix(nv, d * d, d)

    def det_mp(M, nv=nv):
        acc = MP.const(nv, 0)
        for p in itertools.permutations(range(len(M))):
            sgn = 1
            for i in range(len(p)):
                for j in range(i + 1, len(p)):
                    if p[i] > p[j]:
                        sgn = -sgn
            t = MP.const(nv, sgn)
            for i in range(len(M)):
                t = t * M[i][p[i]]
            acc = acc + t
        return acc
    gate("C1", "det(AB) = det(A) det(B) as a polynomial identity [d=%d]" % d,
         (det_mp(mp_mm(A, Bm, nv)) - det_mp(A) * det_mp(Bm)).is_zero(),
         "%d independent variables" % nv)
for N in (2, 3, 4, 5, 6):
    K, X, Z, _ = WEYL[N]
    om = K.conj(K.z)
    powN = K.one
    for _ in range(N):
        powN = K.mul(powN, om)
    gate("C1", "the realized multiplier obeys omega^N = 1 [N=%d]" % N,
         powN == K.one, "theta = -1/%d; theta in (1/%d)Z is the whole "
         "realizable set on C^%d" % (N, N, N), "[W]")
print()
print("C2.  NO COMMITTED PRINCIPLE SELECTS theta.  The corpus supplies a")
print("     value group in (R+, x) with no unimodular part ([D74] D2), a")
print("     phase form on a reversal-ODD channel with no bilinear pairing")
print("     ([D71b] Clauses 2 and 3), and an amplitude carrier with no")
print("     closure ([D71b] 4.2).  None of the three fixes a dimension N, a")
print("     residue k, or a pairing.  Paper 0 v2.1's own reading of theta")
print("     as h-bar-like is explicitly conditional on the generators")
print("     carrying physical dimensions and the exponent being a")
print("     symplectic pairing; no committed object supplies either.")
gate("C2", "W2c VERDICT: VACUOUS", True,
     "no class survives W2b, so there is no theta to select; the "
     "constraints any future theta would face are gated at C1", "DATA")
print()


# ============================================================================
head("SECTION D — ANTECEDENTS, AS USED")
# ============================================================================
for t in sorted(CITED):
    print("  %-8s %s" % (t, CITED[t]))
print()
print("  This unit claims: A1's closed form and the structure read off it")
print("  (A2, A3), the tree coherence law at every n (A4), the content-free")
print("  demonstration (A5), the exact two-sided annihilator (A6), the")
print("  failure of local determination (A7), the flat-spectrum form of the")
print("  alignment condition (A8), and the W2b no-go (B3-B7) with its")
print("  census (B8).  It claims no novelty for the cross-term identity")
print("  [B1], the coherence law at n = 3 [REV2], the Weyl relations [W],")
print("  Stone-von Neumann [SvN], or any committed number of [W1'] or")
print("  [D74].")
print()


# ============================================================================
head("SECTION E — THE VERDICT")
# ============================================================================
fails = [(s, n, d) for s, n, ok, d, _ in GATES if not ok]
npass = sum(1 for _, _, ok, _, _ in GATES if ok)
print("  anchors  : %d, all reproduce (exit 1 is anchor-only)" % NANCHOR[0])
print("  gate book: %d gates, %d pass, %d fail" % (len(GATES), npass,
                                                   len(fails)))
if fails:
    print()
    print("  FAILURES:")
    for s, n, d in fails:
        print("    %-5s %-53s %s" % (s, n, d))
print()
DECL = [(s, n) for s, n, ok, d, t in GATES
        if t.startswith("DECLARATIVE") or t == "DATA"
        or n.startswith("W2b VERDICT") or n.startswith("W2c VERDICT")]
DEGEN = [("A5", "the coherence law holds for f = identity"),
         ("A3", "(H,H) attains both ends of the n=2 range")]
print("  DISCLOSURE, in the W1' round-1 idiom.  Of the %d gates, %d carry"
      % (len(GATES), len(DECL) + len(DEGEN)))
print("  no independent information and are named here: %d are DECLARATIVE"
      % len(DECL))
print("  or DATA (a printed classification, a one-line piece of real")
print("  algebra, or a verdict summary), and 2 are degenerate or")
print("  re-assertions of an anchor —")
for s, n in DECL + DEGEN:
    print("      %-5s %s" % (s, n))
print("  The independent-evidence count is therefore %d."
      % (len(GATES) - len(DECL) - len(DEGEN)))
print()
print("  WHERE THIS RECEIPT'S OWN EXPECTATION WAS REFUTED BY ITS OWN SWEEP:")
print("  B6 was written to check that every committed projective pair is")
print("  Delta^B-flat.  It is not — the non-monomial ones carry nonzero")
print("  families.  The gate now reports what the sweep measures, and what")
print("  it measures is stronger than what was expected: the double")
print("  dissociation between theta and the family, on the committed")
print("  carriers themselves.")
print()
A_OK = all(ok for s, n, ok, d, t in GATES
           if s in ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9"))
print("  W2a — THE DEFECT ALGEBRA: %s"
      % ("STRUCTURE DELIVERED" if A_OK else "BROKEN"))
print("    * the universal closed form Delta^B_ij = |sum_k w_k|^2 -")
print("      sum_k |w_k|^2 with w_k = (U2)_ik (U1)_kj: the defect entry IS")
print("      the total pairwise interference through the cut.")
print("    * the invariance group: BOTH outer tori and the compensated cut")
print("      gauge are annihilated; only an UNCOMPENSATED insertion moves")
print("      the family.  The pin's wall is the scalar corner of this.")
print("    * the family is doubly centred, with sharp entrywise bounds")
print("      -s_ij <= Delta^B_ij <= (n-1) s_ij by sum-of-squares")
print("      certificates; at n = 2 it is exactly one-dimensional with")
print("      EXACT RANGE [-1/2, 1/2], both ends attained by (H,H).")
print("    * the n-fold coherence law is a TREE identity: all C_{n-1}")
print("      bracketings give the same Delta_n — gated over formal matrices")
print("      to n = 6 (d=2) and n = 5 (d=3) with no property of B assumed,")
print("      and on exact committed matrices at every n it reaches.")
print("    * the law is CONTENT-FREE about B: it survives replacing B by")
print("      five declared non-Born maps.  It constrains the family; it")
print("      selects nothing.")
print("    * the two-sided annihilator is EXACTLY the monomial group in")
print("      each slot: W1's sufficiency becomes an equivalence under a")
print("      universal quantifier, by an exact rational probe.")
print("    * pairwise flatness does NOT imply n-fold flatness: exhibited.")
print("    * the alignment condition in closed form for all N: on a")
print("      DFT-sandwich family Delta^B = 0 iff the interleaving diagonal")
print("      has FLAT FOURIER SPECTRUM, equivalently zero periodic")
print("      autocorrelation.  W1's t+u = +-2 (mod 8) and b2+a1 != 0")
print("      (mod 3) are the N = 2 and N = 3 cases.")
print()
print("  W2b — PROJECTIVE DESCENT: %s"
      % ("NO-ACTION" if NO_ACTION else "ACTION-FOUND"))
print("    * THE VERDICT SPLIT BY REQUIREMENT: the ACTION and the CLASS are")
print("      both available from committed objects — W1's families supply")
print("      1999 projective pairs at theta = 1/2, 1/3, 2/3 — but NOT from")
print("      the generated <2,3>, which never acts; and the CONTROL fails")
print("      outright.")
print("    * THE MULTIPLIER CANCELS.  For any projective representation")
print("      Delta^B(rho~(g), rho~(h)) = beta_B(gh) - beta_B(g) beta_B(h)")
print("      with beta_B = B o rho~ lift-independent: omega is gone from")
print("      the whole family identically, not merely pointwise.")
print("    * FOUR CLASSES, ONE BORN SHADOW.  At N = 6 the pairs (X, Z^k)")
print("      realize multiplier classes of order 1, 2, 3 and 6 with")
print("      literally identical Born data and an identically zero")
print("      Delta^B-family.  No functional can separate them.")
print("    * THE CANONICAL REALIZATION IS FLAT.  The Weyl pair is monomial")
print("      and A6 makes the monomial group the exact annihilator; break")
print("      monomiality and a defect appears, controlled by the")
print("      conjugating basis — two conjugators at one theta, two")
print("      different families.")
print("    * THE DOUBLE DISSOCIATION ON THE COMMITTED CARRIERS.  Of W1's")
print("      13185 ordered pairs, 1999 have a scalar commutator and so")
print("      generate a projective Z^2-action.  Non-monomial ones DO carry")
print("      a nonzero Delta^B-family — the flatness expectation is refuted")
print("      by the sweep — but at ONE fixed theta the carriers realize")
print("      SEVERAL distinct families (theta does not determine the")
print("      family), and ONE family occurs at SEVERAL theta (the family")
print("      does not determine theta).  Both directions fail at once.")
print("    * THE PARITIES ARE OPPOSITE.  Delta^B is reversal-EVEN; a U(1)")
print("      holonomy is reversal-ODD; even and unimodular forces +-1, and")
print("      -1 is realized nowhere in the committed values.")
print("    * THE MISSING-PIECE CENSUS (B8): the corpus has a value group")
print("      with no unimodular part, a character where a bicharacter is")
print("      needed, an amplitude with no closure, and edge phases that are")
print("      coboundaries by construction.")
print()
print("  W2c — SELECTION: VACUOUS.  Gated anyway: theta is quantized to")
print("  (1/N)Z on C^N by the determinant, and no committed object supplies")
print("  N, k, or a symplectic pairing.")
print()
hr()
print("  VERDICT: W2a-STRUCTURE-DELIVERED / W2b-NO-ACTION / W2c-VACUOUS"
      if (A_OK and NO_ACTION and not fails)
      else "  VERDICT: see the gate book")
hr()
print()
print("  WHAT WOULD REOPEN W2b, stated so it can be aimed at: a committed")
print("  object that (a) represents the generated group by OPERATORS on a")
print("  common space rather than by values, (b) supplies an ANTISYMMETRIC")
print("  BILINEAR pairing on it, and (c) breaks monomiality in the")
print("  configuration basis so that the defect is nonzero where the")
print("  multiplier lives.  B3 says even all three together do not suffice:")
print("  the multiplier still cancels from the family, so a fourth thing is")
print("  needed — an invariant of the LIFT rather than of the projective")
print("  representation, which the Born projection cannot see by")
print("  construction.")
print()
print("  determinism: fixed lexicographic enumeration everywhere; declared")
print("  deterministic strides where capped; no randomness, no float in any")
print("  substantive path; every cap printed.")
print("  runtime: %s" % el())
hr()
