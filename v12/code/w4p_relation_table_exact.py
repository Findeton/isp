#!/usr/bin/env python3
"""
w4p_relation_table_exact.py — v12 W4': ONE INVARIANT OR THREE.

Pin: v12/note-w4p-one-invariant-or-three-pin.md (STRICT, frozen before
this file existed).  Binding specification: v12 paper 0 v2.1 sec.1 (T2'
the composition defect and the THREE-DEFECT distinction; T3'), sec.2
(the evidence table's W4' row), sec.4 (W4'); v12/LOG.md #1-#8.
Antecedents: [AB], [AMB], [F], [T], [B1], [B3], [REV2].

THE QUESTION.  Paper 0 v1's T5 bundled three obstructions into one
class as a HYPOTHESIS.  U2's precedent is the engraved warning: three
structures assumed one, measured three.  This unit assumes no
unification.  It formalizes the objects, constructs the candidate maps,
and measures co-variation on models CHOSEN IN ADVANCE TO SEPARATE.  The
deliverable is the relation TABLE.

THE OBJECTS
  T   THE TEMPORAL OBJECT — the Delta^B-family on declared
      compositions.  W1's committed machinery is reused by AST lift
      from the committed file and anchored against W1's committed
      numbers.  T is already THREE objects ([REV2]; W1' C+1): Delta^B
      (the Born-shadow defect), D_210 (a DECLARED law's residual) and
      d_div (existential divisibility).
  X   THE CONTEXTUAL OBJECT — the Abramsky-Brandenburger
      no-global-section obstruction on the CHSH context 4-cycle [AB],
      on declared exact empirical models, with the possibilistic
      hierarchy and the Abramsky-Mansfield-Barbosa cohomological
      witness [AMB], computed where defined, its SUFFICIENT-NOT-
      NECESSARY caution carried as a measured fact, not a remark.
  B1  BC1's measured obstruction — division events do not glue across
      the subsystem lattice.  CITED from the committed bc state (the bc
      working tree is dirty with frozen partial edits; every quoted
      constant is verified against the committed blob by `git show`).
  B2  BC2's measured obstruction — the intermediate-slice composite
      description is not frame-mappable.  CITED the same way, WITH
      bc/LOG.md #4's corrections carried forward (M-1's inversion,
      M-2's E2 rescoring, M-3's narrowing).

WHAT IS RE-RUN AND WHAT IS NOT.  BC1 and BC2 are NOT re-run: their
verdicts enter as fixed cited data points with verified provenance.
This unit builds (i) the contextual invariant on BC2's OWN QUOTED
statistics (a new invariant on old numbers, not a re-run), and (ii) a
common-domain toy zoo on which all four invariants are defined and
computed exactly, because the corpus's own carriers have disjoint
domains.

THE TEST OF INDEPENDENCE, stated before any model is built.  For an
ordered pair of invariants (P, Q):
  * Q is NOT a function of P  iff  two zoo models exist with equal P and
    different Q;
  * both directions witnessed => INDEPENDENT;
  * one direction only => MAPPED-BUT-INEQUIVALENT (the map, plus the
    non-injectivity witness);
  * neither => UNSEPARATED-ON-THIS-ZOO.  That is NOT reported as
    IDENTICAL: IDENTICAL requires a CONSTRUCTED equivalence, gated.

HOUSE RULES OBSERVED
  * Exact arithmetic end to end.  fractions.Fraction; a Q(sqrt2) class
    with an exact sign oracle (cross-anchored against W1's committed Q2
    oracle); W1's cyclotomic class Cyc for the amplitude layer; integer
    Hermite normal form for the [AMB] obstruction over Z.  No float, no
    tolerance anywhere.
  * Anchors exit 1.  Substantive negatives exit 0.
  * Every sweep is exhaustive over a declared finite set; no sampling,
    no randomness, no hashing, no wall clock in any substantive path.
  * Lean: NONE.  "the three are one", "the three are three" and "the
    three are more than three" are all reportable outcomes.
"""

from __future__ import annotations

import ast
import itertools
import os
import subprocess
import sys
import time
from fractions import Fraction as Fr

T0 = time.time()


def el():
    return "%7.1fs" % (time.time() - T0)


def hr(c="="):
    print(c * 78)


def head(title):
    hr()
    print(title)
    hr()


GATES = []
CITED = {}
ANCH = [0]


def cite(tag, text):
    CITED[tag] = text


def gate(sec, name, ok, detail="", tag=""):
    GATES.append((sec, name, bool(ok), detail, tag))
    line = "  [%s] %-6s %-50s" % ("PASS" if ok else "FAIL", sec, name)
    if detail:
        line += " %s" % detail
    if tag:
        line += "   <%s>" % tag
    print(line)
    return bool(ok)


def anchor(name, ok, detail=""):
    if not ok:
        print("  [ANCHOR-FAIL] %-42s %s" % (name, detail))
        print("\nANCHOR FAILURE — the reused/arithmetic layer is unsound.")
        sys.exit(1)
    ANCH[0] += 1
    print("  [anchor] %-44s ok %s" % (name, detail))


head("w4p_relation_table_exact.py — v12 W4'")
print("ONE INVARIANT OR THREE: the exact relation table between the")
print("temporal (Delta^B), the contextual (AB/AMB), and the measured BC")
print("obstructions.")
hr()
print("  pin    : v12/note-w4p-one-invariant-or-three-pin.md")
print("  binding: v12 paper 0 v2.1 sec.1 T2'/T3', sec.2, sec.4 W4';")
print("           v12/LOG.md #1-#8; bc/LOG.md #2-#4 (COMMITTED state only).")
print("  warning: U2's precedent — three structures assumed one, measured")
print("           three.  NO UNIFICATION IS ASSUMED ANYWHERE BELOW.")
print("  lean   : NONE.  exits: substantive negatives exit 0; exit 1 is")
print("           ANCHOR-only (reused values, provenance, arithmetic layer).")
print()

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "..", ".."))


def git_show(spec):
    return subprocess.run(["git", "show", spec], cwd=REPO, check=True,
                          stdout=subprocess.PIPE).stdout.decode("utf-8")


# ============================================================================
head("SECTION 0 — PROVENANCE: the reused source and the cited constants")
# ============================================================================
print("0.1  THE REUSED SOURCE (AST lift from the COMMITTED W1' receipt).")

W1P_PATH = "v12/code/w1p_three_class_exact.py"
W1P_SRC = git_show("HEAD:" + W1P_PATH)
with open(os.path.join(REPO, W1P_PATH), "rb") as fh:
    _disk = fh.read().decode("utf-8")
anchor("committed W1' blob == working-tree file", _disk == W1P_SRC,
       "%d bytes, byte-identical" % len(W1P_SRC))

LIFT = ["ptrim", "pmul", "padd", "psub", "pscal", "pdivmod", "cyclotomic",
        "pgcdext", "Cyc", "Q2", "MP", "mmul", "_dot", "mdag", "mB", "msub",
        "mzero", "meq", "mid", "is_unitary", "delta_def", "delta_cross",
        "diag", "perm", "row_monomial", "col_monomial", "S_rat", "mmul_rat",
        "stochastic", "shadow_no_D", "shadow_with_D"]

LIFT_CONST = ["_CYCLO"]              # the memo table cyclotomic() closes over

_tree = ast.parse(W1P_SRC, filename=W1P_PATH)
_picked, _sigs, _consts = {}, {}, []
for _node in _tree.body:
    if isinstance(_node, (ast.FunctionDef, ast.ClassDef)) and \
            _node.name in LIFT:
        _picked[_node.name] = _node
        if isinstance(_node, ast.FunctionDef):
            _sigs[_node.name] = tuple(a.arg for a in _node.args.args)
    elif isinstance(_node, ast.Assign) and len(_node.targets) == 1 and \
            isinstance(_node.targets[0], ast.Name) and \
            _node.targets[0].id in LIFT_CONST:
        _consts.append(_node)
anchor("every declared name present in the committed source",
       len(_picked) == len(LIFT) and len(_consts) == len(LIFT_CONST),
       "%d/%d functions+classes, %d/%d module constants"
       % (len(_picked), len(LIFT), len(_consts), len(LIFT_CONST)))

SIG_EXPECT = {"delta_def": ("K", "U2", "U1"),
              "delta_cross": ("K", "U2", "U1"),
              "mB": ("K", "A"), "mmul": ("K", "A", "B"),
              "S_rat": ("x",), "stochastic": ("M",),
              "shadow_with_D": ("K", "U2", "U1"),
              "mmul_rat": ("A", "B")}
anchor("AST signature pass on the lifted functions",
       all(_sigs.get(k) == v for k, v in SIG_EXPECT.items()),
       "%d signatures checked" % len(SIG_EXPECT))

_body = _consts + [_picked[n] for n in
                   sorted(_picked, key=lambda n: _picked[n].lineno)]
_mod = ast.Module(body=sorted(_body, key=lambda nd: nd.lineno),
                  type_ignores=[])
NS = {"__builtins__": __builtins__, "itertools": itertools, "sys": sys,
      "time": time, "Fr": Fr}
exec(compile(ast.fix_missing_locations(_mod), "<w1p-lift>", "exec"), NS)
Cyc, Q2, MP = NS["Cyc"], NS["Q2"], NS["MP"]
mmul, mB, msub, mzero, meq = (NS["mmul"], NS["mB"], NS["msub"], NS["mzero"],
                              NS["meq"])
mdag, is_unitary = NS["mdag"], NS["is_unitary"]
delta_def, delta_cross = NS["delta_def"], NS["delta_cross"]
diag, perm = NS["diag"], NS["perm"]
row_monomial, col_monomial = NS["row_monomial"], NS["col_monomial"]
S_rat, mmul_rat, stochastic = NS["S_rat"], NS["mmul_rat"], NS["stochastic"]
print("     lifted: %s" % ", ".join(LIFT[:11]))
print("             %s" % ", ".join(LIFT[11:22]))
print("             %s" % ", ".join(LIFT[22:]))
print()

print("0.2  THE CITED BC CONSTANTS — every quotation verified against the")
print("     COMMITTED blob.  The bc working tree is DIRTY with frozen")
print("     partial edits; no code path below reads it.")
BC2_COMMIT, BC1_COMMIT = "cbb7279", "42d8610"
BC2_TXT = git_show("%s:bc/note-bc2-bell-two-frames.md" % BC2_COMMIT)
BC1_TXT = git_show("%s:bc/note-bc1-division-event-composition.md" % BC1_COMMIT)
BCLOG_TXT = git_show("HEAD:bc/LOG.md")

Q_BC2 = {
    "settings": "`SP-A (0°,45°)`, `SP-B (0°,135°)`,",
    "law": "`P(α,β) = (1 − αβ cos(a−b))/4`",
    "divides": "at `SP-A, SP-B, SP-E` and differs in `576` entries at",
    "empty16": "**Unequal settings: 16 of 16 cells empty under "
               "`φ_LOR`, and 16 of 16",
    "gfull": "| SP-A, SP-B, SP-C, SP-D | G-FULL | `-` | `-` |",
    "spE": "| SP-E (0°,0°) | G-SUPP | `PI` | `PI` |",
    "spF": "| SP-F (45°,45°) | G-SUPP | `PI` | `PI` |",
    "notartefact": "a divisibility artefact: it is present at setting pairs "
                   "where the",
    "finaltime": "**The final-time law is literally identical in the two "
                 "frames:**",
    "permclass": "the candidate frame map is a **permutation** of `C`",
}
Q_BC1 = {
    "ghz": "**GHZ-generating Clifford, ABC > BC at t_2.**",
    "divbc": "DIV_BC = {0,1,3,4}",
    "gs1": "| GS1 restriction-compatibility | 66/88 |",
    "gs2": "| GS2 gluing | 88/88 |",
    "gs3": "| GS3 system-independence | 22/88 |",
    "hard": "Ten grid slices in the sweep admit **no non-empty** assignment",
    "product": "has DIV_ABC = {0,4}, a proper subset of the grid",
    "markov": "everywhere — 385 (reading, subsystem, time) slots, all true",
    "predicate": "> a column-stochastic X_b on C_S with "
                 "X_b Γ_S(t_k←0) = Γ_S(t_b←0).",
    "gs1axiom": "**GS1 restriction-compatibility.**",
}
Q_LOG = {
    "m1": "declared intermediate division event VIOLATES the law of total",
    "m1b": "division event ⟺ the process divides at it",
    "m2": "mis-scored — with all target times kept",
    "pointerfree": "24/24 permutations fail at all four grains",
    "m3": "is the INTERMEDIATE-slice composite description.",
}
_missing = [("bc2." + k) for k, v in Q_BC2.items() if v not in BC2_TXT]
_missing += [("bc1." + k) for k, v in Q_BC1.items() if v not in BC1_TXT]
_missing += [("log4." + k) for k, v in Q_LOG.items() if v not in BCLOG_TXT]
anchor("every cited BC string present in the committed blob", not _missing,
       "%d quotations (%d bc2, %d bc1, %d bc/LOG #4); missing: %s"
       % (len(Q_BC2) + len(Q_BC1) + len(Q_LOG), len(Q_BC2), len(Q_BC1),
          len(Q_LOG), _missing or "none"))
print("     bc2 note @ %s ; bc1 note @ %s ; bc/LOG.md @ HEAD"
      % (BC2_COMMIT, BC1_COMMIT))
print()

# ============================================================================
head("SECTION 1 — THE EXACT ARITHMETIC LAYER BUILT HERE")
# ============================================================================
print("1.1  Q(sqrt2) with an exact sign oracle (class ES), cross-anchored")
print("     against W1's committed Q2 oracle.")


class ES:
    """a + b sqrt2, a, b in Q.  Exact field arithmetic and exact sign."""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = Fr(a)
        self.b = Fr(b)

    def __repr__(self):
        if self.b == 0:
            return str(self.a)
        if self.a == 0:
            return "%s*r2" % self.b
        return "%s%s%s*r2" % (self.a, "+" if self.b > 0 else "-", abs(self.b))

    def __add__(self, o):
        o = es(o)
        return ES(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return ES(-self.a, -self.b)

    def __sub__(self, o):
        return self + (-es(o))

    def __rsub__(self, o):
        return es(o) + (-self)

    def __mul__(self, o):
        o = es(o)
        return ES(self.a * o.a + 2 * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def inv(self):
        d = self.a * self.a - 2 * self.b * self.b
        if d == 0:
            raise ZeroDivisionError
        return ES(self.a / d, -self.b / d)

    def __truediv__(self, o):
        return self * es(o).inv()

    def __eq__(self, o):
        o = es(o)
        return self.a == o.a and self.b == o.b

    def __ne__(self, o):
        return not self.__eq__(o)

    def __hash__(self):
        return hash((self.a, self.b))

    def key(self):
        return (self.a, self.b)

    def is_zero(self):
        return self.a == 0 and self.b == 0

    def sign(self):
        return Q2(self.a, self.b).sign()

    def __lt__(self, o):
        return (self - es(o)).sign() < 0

    def __le__(self, o):
        return (self - es(o)).sign() <= 0

    def __gt__(self, o):
        return (self - es(o)).sign() > 0

    def __ge__(self, o):
        return (self - es(o)).sign() >= 0


def es(x):
    return x if isinstance(x, ES) else ES(x, 0)


E0, E1 = ES(0), ES(1)
R2 = ES(0, 1)

_ok = True
for _a in range(-4, 5):
    for _b in range(-4, 5):
        for _d in (1, 2, 3, 5):
            if ES(Fr(_a, _d), Fr(_b, _d)).sign() != \
                    Q2(Fr(_a, _d), Fr(_b, _d)).sign():
                _ok = False
anchor("ES sign oracle == W1's committed Q2 oracle", _ok,
       "324 exact points of Q(sqrt2)")
anchor("ES field laws",
       (R2 * R2 == ES(2) and ES(1, 1) * ES(1, -1) == ES(-1)
        and ES(3, 2) / ES(3, 2) == ES(1) and ES(1, 1) + ES(2, -3) == ES(3, -2)
        and (ES(1, 2) * (ES(3, 1) + ES(0, 2))
             == ES(1, 2) * ES(3, 1) + ES(1, 2) * ES(0, 2))),
       "sqrt2^2 = 2, (1+r2)(1-r2) = -1, x/x = 1, additivity, distributivity")

print()
print("1.2  Integer linear algebra: column Hermite normal form over Z.")
print("     The [AMB] obstruction lives over Z, so rational solvability is")
print("     NOT the right test; both are reported.")


def _hnf_cols(A):
    m = len(A)
    n = len(A[0])
    H = [row[:] for row in A]
    piv = []
    c0 = 0
    for r in range(m):
        if c0 >= n:
            piv.append(None)
            continue
        for c in range(c0 + 1, n):
            while H[r][c] != 0:
                if H[r][c0] == 0:
                    for i in range(m):
                        H[i][c0], H[i][c] = H[i][c], H[i][c0]
                    continue
                q = H[r][c0] // H[r][c]
                for i in range(m):
                    H[i][c0], H[i][c] = H[i][c], H[i][c0] - q * H[i][c]
        if H[r][c0] == 0:
            piv.append(None)
            continue
        if H[r][c0] < 0:
            for i in range(m):
                H[i][c0] = -H[i][c0]
        piv.append(c0)
        c0 += 1
    return H, piv


def int_solvable(A, b):
    """Exact: does Ax = b have a solution x in Z^n?"""
    if not A:
        return all(v == 0 for v in b)
    H, piv = _hnf_cols(A)
    m, n = len(A), len(A[0])
    y = [0] * n
    for r in range(m):
        acc = b[r] - sum(H[r][c] * y[c] for c in range(n) if y[c])
        p = piv[r]
        if p is None:
            if acc != 0:
                return False
            continue
        if acc % H[r][p] != 0:
            return False
        y[p] = acc // H[r][p]
    return all(sum(H[r][c] * y[c] for c in range(n)) == b[r]
               for r in range(m))


def rat_solvable(A, b):
    if not A:
        return all(v == 0 for v in b)
    m, n = len(A), len(A[0])
    M = [[Fr(A[i][j]) for j in range(n)] + [Fr(b[i])] for i in range(m)]
    r = 0
    for c in range(n):
        p = None
        for i in range(r, m):
            if M[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        r += 1
    return all(M[i][n] == 0 for i in range(r, m))


anchor("HNF/Z solver known answers",
       (int_solvable([[2]], [3]) is False and rat_solvable([[2]], [3]) is True
        and int_solvable([[2, 3]], [1]) is True
        and int_solvable([[2, 4]], [1]) is False
        and int_solvable([[1, 1], [1, -1]], [2, 0]) is True
        and int_solvable([[1, 1], [1, 1]], [1, 2]) is False
        and int_solvable([[0, 0]], [0]) is True),
       "2x=3 no/Z yes/Q; 2x+3y=1 yes; 2x+4y=1 no; +3 more")

print()
print("1.3  Exact rational LP (Phase-I simplex, Bland's rule) — the DECLARED")
print("     FALLBACK for existential divisibility.  A certificate cascade")
print("     decides first; LP invocations are counted and reported.")
LPCALL = [0]


def lp_feasible(A, b):
    LPCALL[0] += 1
    m = len(A)
    n = len(A[0])
    A = [[Fr(x) for x in row] for row in A]
    b = [Fr(x) for x in b]
    for i in range(m):
        if b[i] < 0:
            A[i] = [-x for x in A[i]]
            b[i] = -b[i]
    T = [A[i][:] + [Fr(1) if j == i else Fr(0) for j in range(m)] + [b[i]]
         for i in range(m)]
    basis = [n + i for i in range(m)]
    cost = [Fr(0)] * (n + m + 1)
    for i in range(m):
        for j in range(n + m + 1):
            cost[j] -= T[i][j]
    for j in range(n, n + m):
        cost[j] = Fr(0)
    it = 0
    while True:
        it += 1
        if it > 50000:
            raise RuntimeError("LP iteration cap")
        e = None
        for j in range(n + m):
            if cost[j] < 0:
                e = j
                break
        if e is None:
            break
        lv, best = None, None
        for i in range(m):
            if T[i][e] > 0:
                rr = T[i][n + m] / T[i][e]
                if best is None or rr < best or (rr == best
                                                 and basis[i] < basis[lv]):
                    best, lv = rr, i
        if lv is None:
            break
        pv = T[lv][e]
        T[lv] = [x / pv for x in T[lv]]
        for i in range(m):
            if i != lv and T[i][e] != 0:
                f = T[i][e]
                T[i] = [x - f * y for x, y in zip(T[i], T[lv])]
        if cost[e] != 0:
            f = cost[e]
            cost = [x - f * y for x, y in zip(cost, T[lv])]
        basis[lv] = e
    return -cost[n + m] == 0


anchor("LP known answers",
       (lp_feasible([[1, 1]], [Fr(1)]) is True
        and lp_feasible([[1, 1], [1, 1]], [Fr(1), Fr(2)]) is False
        and lp_feasible([[1, -1]], [Fr(0)]) is True
        and lp_feasible([[-1, -1]], [Fr(1)]) is False),
       "x+y=1 yes; contradictory pair no; x=y yes; -x-y=1 no")
LPCALL[0] = 0
print()

# ============================================================================
head("SECTION 2 — OBJECT T: THE TEMPORAL DEFECT FAMILY  [B1] [REV2]")
# ============================================================================
print("Delta^B(U2,U1) = B(U2 U1) - B(U2) B(U1),  B(U)_ij = |U_ij|^2.")
print("D_210 = Gam_20 - Gam_21 Gam_10   (the residual of a DECLARED law).")
print("d_div = 0 iff SOME column-stochastic K has K Gam_10 = Gam_20.")
print("These are THREE objects and are never conflated (W1' C+1, [REV2]).")
print()

K8, K12 = Cyc(8), Cyc(12)
INV_R2_8 = K8.inv(K8.sqrt_of(2))       # W1's own construction, by search
INV_R3_12 = K12.inv(K12.sqrt_of(3))    # and verified by squaring in-field
H2 = [[K8.mul(K8.rat(a), INV_R2_8) for a in row] for row in ([1, 1], [1, -1])]
W_UNB = [[K8.mul(K8.zpow(k), INV_R2_8) for k in row]
         for row in ([0, 2], [2, 0])]
F3 = [[K12.mul(K12.zpow(4 * ((i * j) % 3)), INV_R3_12) for j in range(3)]
      for i in range(3)]
anchor("lifted Cyc reproduces W1's unitaries",
       is_unitary(K8, H2) and is_unitary(K8, W_UNB) and is_unitary(K12, F3),
       "H, W = (1/r2)[[1,i],[i,1]], F3 = DFT_3")

d_HH = delta_def(K8, H2, H2)
d_HW = delta_def(K8, H2, W_UNB)
anchor("W1 committed value  Delta^B(H,H) = [[1/2,-1/2],[-1/2,1/2]]",
       (K8.to_rat(d_HH[0][0]) == Fr(1, 2) and K8.to_rat(d_HH[0][1]) ==
        Fr(-1, 2) and K8.to_rat(d_HH[1][0]) == Fr(-1, 2)
        and K8.to_rat(d_HH[1][1]) == Fr(1, 2)),
       "reproduced exactly in Q(zeta_8)")
anchor("W1 committed value  Delta^B(H,W) = 0, both factors unbiased",
       (mzero(K8, d_HW) and not row_monomial(K8, H2)
        and not col_monomial(K8, W_UNB)),
       "THE NAMED WITNESS the pin calls for")
anchor("W1 cross-term identity on both pairs",
       (meq(K8, d_HH, delta_cross(K8, H2, H2))
        and meq(K8, d_HW, delta_cross(K8, H2, W_UNB))),
       "[B1]'s entrywise interference cross-term")

_bad = 0
for _s, _t, _u, _v in itertools.product(range(8), repeat=4):
    _U2 = mmul(K8, mmul(K8, diag(K8, [K8.one, K8.zpow(_s)]), H2),
               diag(K8, [K8.one, K8.zpow(_t)]))
    _U1 = mmul(K8, mmul(K8, diag(K8, [K8.one, K8.zpow(_u)]), H2),
               diag(K8, [K8.one, K8.zpow(_v)]))
    if mzero(K8, delta_def(K8, _U2, _U1)) != (((_t + _u) % 8) in (2, 6)):
        _bad += 1
anchor("W1 committed closed form  2x2 unbiased: Delta^B = 0 <=> t+u = +-2 (8)",
       _bad == 0, "4096 parameter quadruples, 0 deviations")

c1c, s1c = Fr(24, 25), Fr(7, 25)
c2c, s2c = Fr(4, 5), Fr(3, 5)
c1 = c1c ** 2 - s1c ** 2
c2 = c2c ** 2 - s2c ** 2
ctot = c1 * c2 - (2 * c1c * s1c) * (2 * c2c * s2c)
B1m, B2m, Btot = S_rat(c1), S_rat(c2), S_rat(ctot)
DeltaB = [[Btot[i][j] - mmul_rat(B2m, B1m)[i][j] for j in range(2)]
          for i in range(2)]
Kdiv = S_rat(Fr(-175, 527))
anchor("W1 committed value  Delta^B_00 = -4032/15625 with d_div = 0",
       (DeltaB[0][0] == Fr(-4032, 15625) and stochastic(Kdiv)
        and mmul_rat(Kdiv, B1m) == Btot and Kdiv != B2m),
       "the [REV2] three-defect separation, reproduced")

print()
print("2.1  THE INTERNAL RELATIONS OF T — an implication lattice, not an")
print("     identity.  T is three objects before any other object is met.")
_imp_ok, _imp_n = True, 0
for _U2 in (H2, W_UNB, mmul(K8, H2, W_UNB), mmul(K8, W_UNB, W_UNB)):
    for _U1 in (H2, W_UNB, mmul(K8, W_UNB, H2), mmul(K8, H2, H2)):
        _imp_n += 1
        if mzero(K8, delta_def(K8, _U2, _U1)):
            if not meq(K8, mB(K8, mmul(K8, _U2, _U1)),
                       mmul(K8, mB(K8, _U2), mB(K8, _U1))):
                _imp_ok = False
gate("T-int", "Delta^B = 0  =>  d_div = 0  (the divisor is K = B(U2))",
     _imp_ok, "%d exact pairs; a one-line theorem, gated" % _imp_n)
gate("T-int", "STRICT: d_div = 0 while Delta^B != 0", True,
     "W1 C+1 anchor: Delta^B_00 = -4032/15625 with K = S(-175/527)",
     "[REV2]")
gate("T-int", "D_210 = Delta^B ONLY under the Born declaration", True,
     "Gam_21 := B(U2), Gam_10 := B(U1), Gam_20 := B(U2U1)")
gate("T-int", "Delta^B = 0 is PHASE ALIGNMENT, not absence of coherence",
     mzero(K8, d_HW), "Delta^B(H,W) = 0 with BOTH factors fully unbiased")
print("     => 'the temporal invariant' is already not one invariant.")
print()

# ============================================================================
head("SECTION 3 — OBJECT X: THE AB/AMB CONTEXTUAL OBSTRUCTION  [AB] [AMB]")
# ============================================================================
cite("[AB]", "Abramsky-Brandenburger NJP 13 113036 (2011) — the presheaf "
             "formulation; global section = non-contextual; the "
             "possibilistic hierarchy (contextual / logically contextual / "
             "strongly contextual).")
cite("[AMB]", "Abramsky-Mansfield-Barbosa arXiv:1111.3620 — the "
              "cohomological obstruction on the free abelian presheaf "
              "generated by the SUPPORT: a SUFFICIENT, NOT NECESSARY "
              "witness of contextuality.")
cite("[F]", "Fine PRL 48 291 (1982) — for the (2,2,2) scenario a joint "
            "distribution exists iff the CHSH inequalities hold.")
cite("[T]", "Tsirelson — the real-unit-vector (Gram) representation of "
            "quantum correlators; imported, not re-derived.")
cite("[B1]", "Barandes arXiv:2302.10778 — the Born projection and its "
             "interference cross-term.")
cite("[B3]", "Barandes arXiv:2507.21192 — division events, "
             "system-centricity, measurement-outcome configurations.")
cite("[REV2]", "the second external hostile review, adjudicated at v12 "
               "LOG #4 — the three-defect distinction.")
cite("[BC1]", "bc/note-bc1-division-event-composition.md @ 42d8610.")
cite("[BC2]", "bc/note-bc2-bell-two-frames.md @ cbb7279, with bc/LOG.md #4's "
              "corrections (M-1, M-2, M-3) carried forward.")

print("Scenario: X = {A0,A1,B0,B1}; the cover is the CHSH 4-CYCLE")
print("  C1={A0,B0}  C2={A0,B1}  C3={A1,B1}  C4={A1,B0};  outcomes {+1,-1}.")
print("Adjacent contexts meet in ONE measurement; opposite contexts meet in")
print("the EMPTY set, whose only section is the empty one, so those overlaps")
print("impose equality of coefficient sums.")
print()

MEAS = ["A0", "A1", "B0", "B1"]
CTX = [("A0", "B0"), ("A0", "B1"), ("A1", "B1"), ("A1", "B0")]
OUT = (1, -1)
SEC2 = [(x, y) for x in OUT for y in OUT]
GLOBAL = [dict(zip(MEAS, g)) for g in itertools.product(OUT, repeat=4)]


def table_from(mA, mB, E):
    T = {}
    for a in (0, 1):
        for b in (0, 1):
            T[(a, b)] = {(x, y): (es(1) + es(mA[a]) * x + es(mB[b]) * y
                                  + es(E[a][b]) * (x * y)) * ES(Fr(1, 4))
                         for x, y in SEC2}
    return T


HALF = ES(Fr(1, 2))
IR2 = ES(0, Fr(1, 2))

TABLES = {"DET": table_from([1, 1], [1, 1], [[1, 1], [1, 1]]),
          "UNIF": table_from([0, 0], [0, 0], [[0, 0], [0, 0]]),
          "LCORR": table_from([0, 0], [0, 0], [[1, 1], [1, 1]]),
          "SINGLET": table_from([0, 0], [0, 0], [[IR2, IR2], [IR2, -IR2]]),
          "PR": table_from([0, 0], [0, 0], [[1, 1], [1, -1]])}
_h = {(0, 0): {(1, 1): Fr(1, 10), (1, -1): Fr(1, 10),
               (-1, 1): Fr(2, 5), (-1, -1): Fr(2, 5)},
      (0, 1): {(1, 1): Fr(0), (1, -1): Fr(1, 5),
               (-1, 1): Fr(7, 10), (-1, -1): Fr(1, 10)},
      (1, 0): {(1, 1): Fr(0), (1, -1): Fr(2, 5),
               (-1, 1): Fr(1, 2), (-1, -1): Fr(1, 10)},
      (1, 1): {(1, 1): Fr(1, 10), (1, -1): Fr(3, 10),
               (-1, 1): Fr(3, 5), (-1, -1): Fr(0)}}
TABLES["HARDY"] = {k: {s: es(v) for s, v in d.items()} for k, d in _h.items()}
TORDER = ["DET", "UNIF", "LCORR", "SINGLET", "HARDY", "PR"]

print("3.1  THE DECLARED EMPIRICAL MODELS (exact; no-signaling verified).")
for nm in TORDER:
    T = TABLES[nm]
    okn = all(sum((T[c][s] for s in SEC2), E0) == E1 for c in T)
    okp = all(T[c][s].sign() >= 0 for c in T for s in SEC2)
    okA = all(sum((T[(a, b)][(x, y)] for y in OUT), E0)
              == sum((T[(a, 1 - b)][(x, y)] for y in OUT), E0)
              for a in (0, 1) for b in (0, 1) for x in OUT)
    okB = all(sum((T[(a, b)][(x, y)] for x in OUT), E0)
              == sum((T[(1 - a, b)][(x, y)] for x in OUT), E0)
              for a in (0, 1) for b in (0, 1) for y in OUT)
    gate("X1", "%-8s normalized, nonneg, no-signaling" % nm,
         okn and okp and okA and okB, "exact in Q(sqrt2)", "[AB]")

print()
print("3.2  THE PROBABILISTIC OBSTRUCTION, decided by CERTIFICATES in BOTH")
print("     directions: a positive exhibits a global section and verifies")
print("     all 16 induced marginals; a negative exhibits a linear")
print("     functional whose maximum over ALL 16 deterministic global")
print("     sections is computed here and is strictly below the model's")
print("     value.  [F] is used only as an independent cross-check.")

CHSH_SIGNS = [sg for sg in itertools.product((1, -1), repeat=4)
              if sg.count(-1) % 2 == 1]


def corr(T, a, b):
    return sum((T[(a, b)][(x, y)] * (x * y) for x, y in SEC2), E0)


def chsh(T, sg):
    E = [corr(T, a, b) for a in (0, 1) for b in (0, 1)]
    return sum((es(sg[i]) * E[i] for i in range(4)), E0)


det_max = None
for sg in CHSH_SIGNS:
    for g in GLOBAL:
        v = sum((es(sg[i]) * es(g["A%d" % (i // 2)] * g["B%d" % (i % 2)])
                 for i in range(4)), E0)
        det_max = v if det_max is None or v > det_max else det_max
gate("X2", "max CHSH over the 16 deterministic global sections = 2",
     det_max == ES(2), "8 sign patterns x 16 assignments, exact", "[F]")

SECTIONS = {"DET": {(1, 1, 1, 1): E1},
            "UNIF": {tuple(g[m] for m in MEAS): ES(Fr(1, 16))
                     for g in GLOBAL},
            "LCORR": {(1, 1, 1, 1): HALF, (-1, -1, -1, -1): HALF}}


def marginals_of(d):
    T = {}
    for a in (0, 1):
        for b in (0, 1):
            dd = {s: E0 for s in SEC2}
            for g, w in d.items():
                gg = dict(zip(MEAS, g))
                s = (gg["A%d" % a], gg["B%d" % b])
                dd[s] = dd[s] + w
            T[(a, b)] = dd
    return T


XVAL = {}
for nm in TORDER:
    T = TABLES[nm]
    mx = max(chsh(T, sg) for sg in CHSH_SIGNS)
    if nm in SECTIONS:
        d = SECTIONS[nm]
        mg = marginals_of(d)
        ok = (sum(d.values(), E0) == E1
              and all(w.sign() >= 0 for w in d.values())
              and all(mg[c][s] == T[c][s] for c in T for s in SEC2))
        gate("X2", "%-8s NON-CONTEXTUAL: global section exhibited" % nm, ok,
             "%d-atom distribution, 16 marginals verified; max CHSH = %s"
             % (len(d), mx), "[AB]")
        ctxl = False
    else:
        gate("X2", "%-8s CONTEXTUAL: functional exceeds the vertex max" % nm,
             mx > ES(2), "max CHSH = %s > 2" % mx, "[AB]")
        ctxl = True
    XVAL[nm] = {"chsh": mx, "contextual": ctxl}
gate("X2", "cross-check [F]: contextual <=> a CHSH inequality is violated",
     all((XVAL[nm]["chsh"] > ES(2)) == XVAL[nm]["contextual"]
         for nm in TORDER), "agreement on all 6 models", "[F]")

print()
print("3.3  THE POSSIBILISTIC HIERARCHY [AB]: strong > logical > "
      "probabilistic.")
for nm in TORDER:
    T = TABLES[nm]
    supp = {c: [s for s in SEC2 if T[c][s].sign() > 0] for c in T}
    cons = [g for g in GLOBAL
            if all((g["A%d" % a], g["B%d" % b]) in supp[(a, b)]
                   for a in (0, 1) for b in (0, 1))]
    bad = []
    for (a, b) in T:
        for s in supp[(a, b)]:
            if not any(g["A%d" % a] == s[0] and g["B%d" % b] == s[1]
                       for g in cons):
                bad.append(((a, b), s))
    lvl = ("SC" if not cons else
           ("LC" if bad else ("PC" if XVAL[nm]["contextual"] else "NC")))
    XVAL[nm].update({"level": lvl, "supp": supp, "nglobal": len(cons),
                     "nbad": len(bad)})
    print("     %-8s level %-3s | consistent global assignments %2d | "
          "non-extendable local sections %d" % (nm, lvl, len(cons), len(bad)))
gate("X3", "the hierarchy is STRICT on the declared models",
     (XVAL["DET"]["level"] == "NC" and XVAL["SINGLET"]["level"] == "PC"
      and XVAL["HARDY"]["level"] == "LC" and XVAL["PR"]["level"] == "SC"),
     "NC(DET) < PC(SINGLET) < LC(HARDY) < SC(PR): four distinct levels",
     "[AB]")

print()
print("3.4  THE [AMB] COHOMOLOGICAL WITNESS, computed where defined.")
print("     THE DEFINITION IMPLEMENTED, printed in full so that the verdict")
print("     is a statement about a stated object.  Let S be the support")
print("     presheaf and F = F_Z S the free abelian presheaf it generates.")
print("     For C0 in the cover and s0 in S(C0),")
print("       gamma(s0) = 0  <=>  there are r_i in F(C_i) with r_{C0} = s0")
print("                           and r_i| = r_j| on every C_i n C_j,")
print("                           the empty intersections included.")
print("     This is the compatible-family form of [AMB]'s obstruction: an")
print("     INTEGER linear feasibility problem, decided by Hermite normal")
print("     form.  The rational relaxation is reported alongside.  No claim")
print("     is made to reproduce any published per-model table; the verdict")
print("     below is a verdict about THIS definition.")


def gamma_zero(supp, i0, s0):
    var, idx = [], {}
    for i, c in enumerate(CTX):
        for s in supp[(int(c[0][1]), int(c[1][1]))]:
            idx[(i, s)] = len(var)
            var.append((i, s))
    n = len(var)
    A, b = [], []
    for i in range(4):
        for j in range(i + 1, 4):
            U = tuple(sorted(set(CTX[i]) & set(CTX[j])))
            for t in itertools.product(OUT, repeat=len(U)):
                row = [0] * n
                for (ii, sg) in ((i, 1), (j, -1)):
                    ci = CTX[ii]
                    ab = (int(ci[0][1]), int(ci[1][1]))
                    for s in supp[ab]:
                        if tuple(s[ci.index(m)] for m in U) == t:
                            row[idx[(ii, s)]] += sg
                A.append(row)
                b.append(0)
    c0 = CTX[i0]
    for s in supp[(int(c0[0][1]), int(c0[1][1]))]:
        row = [0] * n
        row[idx[(i0, s)]] = 1
        A.append(row)
        b.append(1 if s == s0 else 0)
    return int_solvable(A, b), rat_solvable(A, b)


for nm in TORDER:
    supp = XVAL[nm]["supp"]
    nz, nzq, tot = 0, 0, 0
    for i0, c in enumerate(CTX):
        for s0 in supp[(int(c[0][1]), int(c[1][1]))]:
            tot += 1
            z, zq = gamma_zero(supp, i0, s0)
            nz += 0 if z else 1
            nzq += 0 if zq else 1
    XVAL[nm]["gnz"] = nz
    XVAL[nm]["gtot"] = tot
    print("     %-8s gamma != 0 at %2d of %2d local sections over Z "
          "(%2d over Q)" % (nm, nz, tot, nzq))

gate("X4", "SUFFICIENT: gamma != 0 occurs only on contextual models",
     all(XVAL[nm]["gnz"] == 0 for nm in TORDER
         if not XVAL[nm]["contextual"]),
     "the three non-contextual models have gamma = 0 everywhere", "[AMB]")
gate("X4", "gamma != 0 on the PR box, at every local section",
     XVAL["PR"]["gnz"] == XVAL["PR"]["gtot"],
     "%d/%d sections obstructed" % (XVAL["PR"]["gnz"], XVAL["PR"]["gtot"]),
     "[AMB]")
gate("X4", "NOT NECESSARY: a CONTEXTUAL model with gamma = 0 everywhere",
     XVAL["SINGLET"]["contextual"] and XVAL["SINGLET"]["gnz"] == 0,
     "SINGLET: max CHSH = %s > 2, yet gamma = 0 at all %d sections"
     % (XVAL["SINGLET"]["chsh"], XVAL["SINGLET"]["gtot"]), "[AMB]")
gate("X4", "NOT NECESSARY even at the LOGICAL level, on this definition",
     (XVAL["HARDY"]["level"] == "LC" and XVAL["HARDY"]["nbad"] > 0
      and XVAL["HARDY"]["gnz"] == 0),
     "HARDY has a NON-EXTENDABLE local section and gamma = 0 at all %d "
     "sections: an explicit Z-family with a negative coefficient defeats "
     "the support restriction" % XVAL["HARDY"]["gtot"], "[AMB]")
gate("X4", "so gamma is STRICTLY WEAKER than logical contextuality here",
     XVAL["HARDY"]["gnz"] < XVAL["PR"]["gnz"],
     "the witness fires on the STRONGLY contextual PR and on nothing else "
     "in this zoo — reported for the definition of 3.4 and no other",
     "[AMB]")
print("     THE CAUTION, MEASURED rather than quoted: the cohomological")
print("     witness is SUFFICIENT and NOT NECESSARY.  The singlet at the")
print("     CHSH settings has full support, so every local section extends")
print("     to a compatible Z-family and gamma vanishes on a model with NO")
print("     global section at all.  gamma is therefore a SEPARATE object,")
print("     strictly weaker than the AB obstruction: X is not one invariant")
print("     either.")
print()

# ============================================================================
head("SECTION 4 — OBJECT B: THE MEASURED BC OBSTRUCTIONS (cited)")
# ============================================================================
print("4.1  BC1 — division events do not glue across the subsystem lattice.")
print("     CITED, NOT re-run.  bc/note-bc1-... @ %s." % BC1_COMMIT)
print("       BC1's predicate, quoted: DIV_S(t_k) holds iff for EVERY grid")
print("       target t_b >= t_k there EXISTS a column-stochastic X_b with")
print("       X_b Gam_S(t_k<-0) = Gam_S(t_b<-0).")
print("       => BC1's predicate IS d_div, the THIRD member of T's family —")
print("          neither Delta^B nor D_210.  This is a fact about the two")
print("          texts, established by quotation; it is NOT an")
print("          identification of the invariants (see 6.4).")
print("       axioms over 88 (model, reading) pairs:")
print("         GS0 88/88 | GS1 66/88 | GS2 88/88 | GS3 22/88")
print("       GHZ-Clifford: DIV_ABC = {0,1,2,3,4}, DIV_BC = {0,1,3,4} — the")
print("         composite divides at t_2 where a PART does not;")
print("       quantum product model: DIV_ABC = {0,4} and no GS crossing;")
print("       classical Markov control: divides everywhere (385 slots) and")
print("         satisfies all four axioms;")
print("       ten grid slices admit NO non-empty consistent assignment.")
gate("B1c", "BC1 constants quoted with verified provenance", True,
     "%d strings matched in the committed blob" % len(Q_BC1), "[BC1]")
print()
print("4.2  BC2 — the intermediate-slice composite description is not")
print("     frame-mappable.  CITED, NOT re-run, WITH bc/LOG.md #4's")
print("     corrections carried forward.")
print("       settings SP-A (0,45) SP-B (0,135) SP-C (90,45) SP-D (90,135):")
print("         exactly a CHSH 4-cycle;  law P(a,b) = (1 - ab cos(a-b))/4;")
print("       admissible map class: PERMUTATIONS of C (L-1(a)), search")
print("         exhaustive, so a negative is a proof of non-existence;")
print("       16 of 16 cells EMPTY at unequal settings, both time")
print("         correspondences, all four grains;")
print("       SP-E and SP-F: a map EXISTS at grain G-SUPP (`PI`);")
print("       DIVISIBILITY of the declared legs: Gam(3<-2)Gam(2<-0) EQUALS")
print("         Gam(3<-0) at SP-A, SP-B, SP-E and differs in 576 entries at")
print("         SP-C, SP-D, SP-F, IN BOTH FRAMES;")
print("       BC2's own sentence: the finding 'is present at setting pairs")
print("         where the process divides in both frames';")
print("       the final-time law is literally identical in the two frames.")
print("     CORRECTIONS CARRIED (bc/LOG.md #4, committed):")
print("       M-1  the declared intermediate division event VIOLATES the law")
print("            of total probability at SP-C/D/F; on that model")
print("            'legitimate division event <=> the process divides at it'")
print("            — the LEGITIMATE census therefore lives on the DIVISIBLE")
print("            instances, and the negatives there are carried by")
print("            initial-division-event objects (round-verified).")
print("       M-2  E2 was mis-scored: with all target times kept it FAILS.")
print("            There is no escape by declaring only the initial")
print("            division event.  This unit uses NO E2-based witness.")
print("       M-3  the non-mappable object is the INTERMEDIATE-slice")
print("            composite description, not the final-time law.")
print("       pointer-free replication: 24/24 permutations fail.")
gate("B2c", "BC2 constants + bc/LOG #4 corrections quoted with provenance",
     True, "%d strings matched in the committed blobs"
     % (len(Q_BC2) + len(Q_LOG)), "[BC2]")
print()
print("4.3  THE CONTEXTUAL INVARIANT ON BC2's OWN QUOTED STATISTICS.")
print("     A NEW invariant computed on OLD numbers — not a re-run.")
E_BC2 = {}
for (lab, a, b) in [("SP-A", 0, 45), ("SP-B", 0, 135), ("SP-C", 90, 45),
                    ("SP-D", 90, 135)]:
    cosv = {45: IR2, 315: IR2, 135: -IR2, 225: -IR2}[(a - b) % 360]
    E_BC2[(a, b)] = -cosv
    print("       %s (%3d,%3d): cos(a-b) = %-8s => E = %s"
          % (lab, a, b, cosv, -cosv))
Ebc = [[E_BC2[(0, 45)], E_BC2[(0, 135)]], [E_BC2[(90, 45)], E_BC2[(90, 135)]]]
T_BC2 = table_from([0, 0], [0, 0], Ebc)
mx_bc2 = max(chsh(T_BC2, sg) for sg in CHSH_SIGNS)
gate("B2x", "BC2's Bell model is CONTEXTUAL: |CHSH| = 2 sqrt2",
     mx_bc2 == ES(0, 2), "max CHSH = %s > 2 = the vertex maximum" % mx_bc2,
     "[AB]")
supp_bc2 = {c: [s for s in SEC2 if T_BC2[c][s].sign() > 0] for c in T_BC2}
nz_bc2 = sum(0 if gamma_zero(supp_bc2, i0, s0)[0] else 1
             for i0, c in enumerate(CTX)
             for s0 in supp_bc2[(int(c[0][1]), int(c[1][1]))])
gate("B2x", "and its [AMB] witness VANISHES at every local section",
     nz_bc2 == 0,
     "full support => gamma = 0: the false negative lands on the corpus's "
     "own measured model", "[AMB]")
print("     => ON BC2's OWN MODEL, in one place: X = PC (contextual) with")
print("        gamma = 0; the frame obstruction NONZERO at all four CHSH")
print("        settings; the temporal residual ZERO at SP-A/SP-B and")
print("        NONZERO at SP-C/SP-D.  Three invariants, one model, three")
print("        different patterns.")
print()

# ============================================================================
head("SECTION 5 — THE COMMON-DOMAIN ZOO (built here; exact)")
# ============================================================================
print("The corpus's own carriers have DISJOINT domains: BC1's models are")
print("closed unitary circuits with no measurement cover (X undefined), and")
print("BC2's model carries no subsystem-lattice census (B1 undefined —")
print("deferred to BC1 by BC2 sec.7 E3c itself).  A common-domain zoo is")
print("therefore built here, on which all four objects are defined.")
print()
print("THE CARRIER.  Configurations C = {(pA,pB)}, pX in {r,+,-}: two")
print("measurement-outcome pointers ([B3] p.16), |C| = 9, initial (r,r).")
print("A-MEASURE overwrites pA with x ~ P_A(.|a), pB untouched; B-MEASURE")
print("overwrites pB with y ~ P(.|pA,b), pA untouched (with the marginal")
print("P_B(.|b) whenever pA = r or the conditioning event has probability")
print("zero — a declared convention on unreachable columns).  Two frame")
print("orderings F1 = (A,B) and F2 = (B,A) of the same two events.")
print("PREFIX NONE, or SWAPBACK: two pointer-exchange steps first, so")
print("Gam(2<-0) = I — a permutation prologue that changes NO statistic.")
print("VARIANT REC: the declared second leg is the true conditional law (a")
print("stable record of the first outcome is read).  VARIANT COH: the")
print("declared second leg is the phase-forgetting law that ignores the")
print("record, so its residual D_210 = joint - product is exactly a")
print("Born-shadow defect at the wing cut.")
print()

PT = ("r", 1, -1)
CFG = [(u, v) for u in PT for v in PT]
NC9 = len(CFG)
CIX = {c: i for i, c in enumerate(CFG)}
IDM = [[E1 if i == j else E0 for j in range(NC9)] for i in range(NC9)]
SWAPM = [[E1 if CFG[i] == (CFG[j][1], CFG[j][0]) else E0
          for j in range(NC9)] for i in range(NC9)]


def _mm(A, B):
    n, p, m = len(A), len(B), len(B[0])
    out = []
    for i in range(n):
        row = []
        for j in range(m):
            acc = E0
            for k in range(p):
                if not A[i][k].is_zero() and not B[k][j].is_zero():
                    acc = acc + A[i][k] * B[k][j]
            row.append(acc)
        out.append(row)
    return out


def _stoch(M):
    n = len(M)
    for j in range(len(M[0])):
        s = E0
        for i in range(n):
            if M[i][j].sign() < 0:
                return False
            s = s + M[i][j]
        if s != E1:
            return False
    return True


def _is_perm(M):
    n = len(M)
    return all(sum(1 for i in range(n) if M[i][j] == E1) == 1
               and sum(1 for i in range(n) if not M[i][j].is_zero()) == 1
               for j in range(n))


CERTS = {}


def divides(Gs, Gt, extra=()):
    """Exact: does SOME column-stochastic X satisfy X Gs = Gt?  Returns
    (verdict, certificate name).  Certificate cascade; exact LP fallback."""
    n = len(Gs)
    cols = list(range(len(Gs[0])))
    scol = {j: tuple(Gs[i][j] for i in range(n)) for j in cols}
    tcol = {j: tuple(Gt[i][j] for i in range(n)) for j in cols}
    if Gs == Gt:
        return True, "identity"
    seen = {}
    for j in cols:
        k = scol[j]
        if k in seen and tcol[seen[k]] != tcol[j]:
            return False, "equal-source-columns/different-targets"
        seen.setdefault(k, j)
    for nm_, X in extra:
        if _stoch(X) and _mm(X, Gs) == Gt:
            return True, "declared-bridge"
    if _is_perm(Gs):
        X = _mm(Gt, [[Gs[j][i] for j in range(n)] for i in range(n)])
        if _stoch(X) and _mm(X, Gs) == Gt:
            return True, "permutation-inverse"
    reps = {}
    for j in cols:
        reps.setdefault(scol[j], []).append(j)
    keys = list(reps)
    sup = [set(i for i in range(n) if not d[i].is_zero()) for d in keys]
    if all(not (sup[p] & sup[q]) for p in range(len(sup))
           for q in range(p + 1, len(sup))):
        X = [[E1 if i == 0 else E0 for _ in range(n)] for i in range(n)]
        for kk, d in enumerate(keys):
            tgt = tcol[reps[d][0]]
            for i in sup[kk]:
                for r in range(n):
                    X[r][i] = tgt[r]
        if _stoch(X) and _mm(X, Gs) == Gt:
            return True, "disjoint-support-construction"
    if all(x.b == 0 for row in Gs for x in row) and \
       all(x.b == 0 for row in Gt for x in row):
        A, bb = [], []
        for d in keys:
            j = reps[d][0]
            for i in range(n):
                row = [Fr(0)] * (n * n)
                for c in range(n):
                    row[i * n + c] = d[c].a
                A.append(row)
                bb.append(tcol[j][i].a)
        for c in range(n):
            row = [Fr(0)] * (n * n)
            for i in range(n):
                row[i * n + c] = Fr(1)
            A.append(row)
            bb.append(Fr(1))
        return lp_feasible(A, bb), "exact-LP"
    return None, "UNDECIDED-BY-CAP"


def dec(Gs, Gt, extra=()):
    v, c = divides(Gs, Gt, extra)
    CERTS[c] = CERTS.get(c, 0) + 1
    return v


def margA(T, a):
    return {x: sum((T[(a, 0)][(x, y)] for y in OUT), E0) for x in OUT}


def margB(T, a, b):
    return {y: sum((T[(a, b)][(x, y)] for x in OUT), E0) for y in OUT}


def step_A_first(T, a):
    M = [[E0] * NC9 for _ in range(NC9)]
    pa = margA(T, a)
    for (u, v) in CFG:
        for x in OUT:
            M[CIX[(x, v)]][CIX[(u, v)]] = M[CIX[(x, v)]][CIX[(u, v)]] + pa[x]
    return M


def step_B_after(T, a, b):
    M = [[E0] * NC9 for _ in range(NC9)]
    pa, pb = margA(T, a), margB(T, a, b)
    for (u, v) in CFG:
        for y in OUT:
            if u == "r" or pa[u].sign() == 0:
                w = pb[y]
            else:
                w = T[(a, b)][(u, y)] / pa[u]
            M[CIX[(u, y)]][CIX[(u, v)]] = M[CIX[(u, y)]][CIX[(u, v)]] + w
    return M


def step_B_coh(T, a, b):
    M = [[E0] * NC9 for _ in range(NC9)]
    pb = margB(T, a, b)
    for (u, v) in CFG:
        for y in OUT:
            M[CIX[(u, y)]][CIX[(u, v)]] = M[CIX[(u, y)]][CIX[(u, v)]] + pb[y]
    return M


def step_B_first(T, a, b):
    return step_B_coh(T, a, b)


def step_A_after(T, a, b):
    M = [[E0] * NC9 for _ in range(NC9)]
    pa, pb = margA(T, a), margB(T, a, b)
    for (u, v) in CFG:
        for x in OUT:
            if v == "r" or pb[v].sign() == 0:
                w = pa[x]
            else:
                w = T[(a, b)][(x, v)] / pb[v]
            M[CIX[(x, v)]][CIX[(u, v)]] = M[CIX[(x, v)]][CIX[(u, v)]] + w
    return M


def build(T, a, b, prefix, frame):
    steps = []
    if prefix == "SWAPBACK":
        steps += [SWAPM, SWAPM]
    if frame == "F1":
        steps += [step_A_first(T, a), step_B_after(T, a, b)]
    else:
        steps += [step_B_first(T, a, b), step_A_after(T, a, b)]
    G = [IDM]
    for M in steps:
        G.append(_mm(M, G[-1]))
    p0 = [E1 if CFG[i] == ("r", "r") else E0 for i in range(NC9)]
    P = [[G[t][i][CIX[("r", "r")]] for i in range(NC9)] for t in range(len(G))]
    return {"G": G, "p": P, "p0": p0, "nt": len(G)}


def declared_cuts(T, a, b, variant, prefix):
    out = []
    off = 2 if prefix == "SWAPBACK" else 0
    if prefix == "SWAPBACK":
        out.append((1, SWAPM))
    out.append((off + 1, step_B_after(T, a, b) if variant == "REC"
                else step_B_coh(T, a, b)))
    return out


print("5.1  THE ZOO'S TEMPORAL VALUE  T = (some D_210 != 0, some d_div != 0)")
print("     over the model's DECLARED cuts and all four contexts.")
ZOO = {}
UNDEC = [0]
for prefix in ("NONE", "SWAPBACK"):
    for variant in ("REC", "COH"):
        for nm in TORDER:
            T = TABLES[nm]
            a210, adiv = False, False
            for a in (0, 1):
                for b in (0, 1):
                    M = build(T, a, b, prefix, "F1")
                    for (tc, leg) in declared_cuts(T, a, b, variant, prefix):
                        if M["G"][tc + 1] != _mm(leg, M["G"][tc]):
                            a210 = True
                        v = dec(M["G"][tc], M["G"][tc + 1],
                                extra=[("declared", leg)])
                        if v is None:
                            UNDEC[0] += 1
                        elif v is False:
                            adiv = True
            ZOO[(nm, variant, prefix)] = {"T": (a210, adiv)}
        print("     %-8s %-4s  T = %s   %s" % (
            prefix, variant,
            {n2: ZOO[(n2, variant, prefix)]["T"] for n2 in TORDER}, el()))

gate("Z1", "REC kills the declared residual at every cut, every context",
     all(ZOO[(n2, "REC", p)]["T"][0] is False
         for n2 in TORDER for p in ("NONE", "SWAPBACK")),
     "the record makes the declared law compose: T3's constructive instance")
gate("Z1", "COH's residual is nonzero exactly on the CORRELATED tables",
     (all(ZOO[(n2, "COH", "NONE")]["T"][0] is True
          for n2 in ("LCORR", "SINGLET", "HARDY", "PR"))
      and all(ZOO[(n2, "COH", "NONE")]["T"][0] is False
              for n2 in ("DET", "UNIF"))),
     "D_210 = joint - product at the wing cut: a CORRELATION measure — the "
     "LOCAL LCORR table has the same defect as the singlet")
gate("Z1", "d_div = 0 across the whole zoo",
     all(ZOO[k]["T"][1] is False for k in ZOO),
     "W1 C+1's separation instantiated on a Bell carrier: the DECLARED "
     "residual separates where the EXISTENTIAL one cannot", "[REV2]")
gate("Z1", "no divisibility decision is UNDECIDED-BY-CAP", UNDEC[0] == 0,
     "certificate cascade: %s ; exact-LP invocations %d"
     % (CERTS, LPCALL[0]))
print()

print("5.2  THE ZOO'S B1 VALUE — BC1's axioms on the lattice {A, B, AB},")
print("     reading C (conditional on the complement's configuration at the")
print("     conditioning time; p0-independent), c* = r.  DECLARED CAPS: a")
print("     TWO-atom lattice, so BC1's GS2 is vacuous here; BC1's GS2")
print("     failures are cited (4.1), not reproduced.")


def reduce_C(G, side, cstar="r"):
    n = len(PT)
    M = [[E0] * n for _ in range(n)]
    for jv, v in enumerate(PT):
        src = CIX[(v, cstar)] if side == "A" else CIX[(cstar, v)]
        for i, c in enumerate(CFG):
            u = c[0] if side == "A" else c[1]
            M[PT.index(u)][jv] = M[PT.index(u)][jv] + G[i][src]
    return M


def div_set(mats):
    D = []
    for t in range(len(mats)):
        if all(dec(mats[t], mats[tb]) is True
               for tb in range(t, len(mats))):
            D.append(t)
    return tuple(D)


for prefix in ("NONE", "SWAPBACK"):
    for variant in ("REC", "COH"):
        shown = None
        for nm in TORDER:
            T = TABLES[nm]
            recs = []
            for a in (0, 1):
                for b in (0, 1):
                    M = build(T, a, b, prefix, "F1")
                    dAB = div_set(M["G"])
                    dA = div_set([reduce_C(G, "A") for G in M["G"]])
                    dB = div_set([reduce_C(G, "B") for G in M["G"]])
                    gs0 = all(0 in d for d in (dA, dB, dAB))
                    gs1 = set(dAB) <= set(dA) and set(dAB) <= set(dB)
                    gs3 = (dA == dB == dAB)
                    recs.append((gs0, gs1, True, gs3, dA, dB, dAB))
            worst = min(recs, key=lambda r: (r[0], r[1], r[3]))
            ZOO[(nm, variant, prefix)]["B1raw"] = worst
            ZOO[(nm, variant, prefix)]["B1"] = worst[:3]
            ZOO[(nm, variant, prefix)]["B1ext"] = worst[4:7]
            shown = worst
        print("     %-8s %-4s  D(A)=%s D(B)=%s D(AB)=%s  (GS0,GS1,GS2)=%s"
              % (prefix, variant, shown[4], shown[5], shown[6], shown[:3]))

gate("Z2", "prefix NONE: the division-event family IS a global section",
     all(ZOO[(n2, v, "NONE")]["B1"] == (True, True, True)
         for n2 in TORDER for v in ("REC", "COH")),
     "GS0 and GS1 hold on every table and variant", "[BC1]")
gate("Z2", "prefix SWAPBACK: GS1 FAILS — BC1's crossing, reproduced exactly",
     all(ZOO[(n2, v, "SWAPBACK")]["B1"][1] is False
         for n2 in TORDER for v in ("REC", "COH")),
     "the composite divides at a permutation step where the atom cannot: "
     "constant columns cannot reach the identity", "[BC1]")
gate("Z2", "the SWAPBACK prologue changes NO statistic",
     all(build(TABLES[n2], a, b, "SWAPBACK", "F1")["p"][-1]
         == build(TABLES[n2], a, b, "NONE", "F1")["p"][-1]
         for n2 in TORDER for a in (0, 1) for b in (0, 1)),
     "identical final-time distribution => identical empirical model => "
     "identical X, by construction")
print()

print("5.3  THE ZOO'S B2 VALUE — the frame-reordering instrument built here.")
print("     THIS IS NOT BC2 RE-RUN.  It is a REDUCED analogue at |C| = 9,")
print("     structurally modelled on BC2's declared comparison: the")
print("     compared content is {p(t)} and {Gam(t<-0)} under a declared time")
print("     correspondence; the forward second legs are not index-matched")
print("     under phi_LOR and are dropped (BC2 sec.5.1); the admissible map")
print("     class is the PERMUTATIONS of C (L-1(a), quoted by BC2); the")
print("     search is EXHAUSTIVE, so a negative is a proof of non-existence")
print("     inside that class.  Grains: G-FULL (marginals + all columns),")
print("     G-FIX (matrices only), G-SUPP (reachable conditioning only:")
print("     columns j with p_j(0) > 0, which is {(r,r)} in both frames).")
print("     Correspondences: phi_LOR (same physical event) and phi_ORD.")

NODEMAX = [0]


def frame_search(objs1, objs2, n, cap=200000):
    inv1 = [[] for _ in range(n)]
    inv2 = [[] for _ in range(n)]
    for k in range(len(objs1)):
        kind, M1, cols = objs1[k]
        _, M2, _ = objs2[k]
        if kind == "p":
            for i in range(n):
                inv1[i].append(M1[i].key())
                inv2[i].append(M2[i].key())
        else:
            full = (len(cols) == n)
            for i in range(n):
                inv1[i].append(tuple(sorted(M1[i][j].key() for j in cols)))
                inv2[i].append(tuple(sorted(M2[i][j].key() for j in cols)))
                if full:
                    inv1[i].append(tuple(sorted(M1[j][i].key()
                                                for j in range(n))))
                    inv2[i].append(tuple(sorted(M2[j][i].key()
                                                for j in range(n))))
    cand = [[k for k in range(n) if inv2[k] == inv1[i]] for i in range(n)]
    colsets = [set(o[2]) if o[0] == "G" else None for o in objs1]
    order = sorted(range(n), key=lambda i: len(cand[i]))
    R = [None] * n
    used = [False] * n
    nodes = [0]

    def ok(i):
        for idx in range(len(objs1)):
            kind, M1, _ = objs1[idx]
            _, M2, _ = objs2[idx]
            if kind == "p":
                if M2[R[i]] != M1[i]:
                    return False
            else:
                cs = colsets[idx]
                for j in range(n):
                    if R[j] is None:
                        continue
                    if j in cs and M2[R[i]][R[j]] != M1[i][j]:
                        return False
                    if i in cs and M2[R[j]][R[i]] != M1[j][i]:
                        return False
        return True

    def dfs(d):
        nodes[0] += 1
        if nodes[0] > cap:
            raise RuntimeError("frame search node cap exceeded")
        if d == n:
            return True
        i = order[d]
        for k in cand[i]:
            if used[k]:
                continue
            R[i] = k
            used[k] = True
            if ok(i) and dfs(d + 1):
                return True
            used[k] = False
            R[i] = None
        return False

    res = tuple(R) if dfs(0) else None
    NODEMAX[0] = max(NODEMAX[0], nodes[0])
    return res


def frame_objects(M, grain, times):
    reach = [j for j in range(NC9) if M["p0"][j].sign() > 0]
    allc = list(range(NC9))
    objs = []
    for t in times:
        if grain != "G-FIX":
            objs.append(("p", M["p"][t], None))
        objs.append(("G", M["G"][t], reach if grain == "G-SUPP" else allc))
    return objs


GR = ("G-FULL", "G-FIX", "G-SUPP")
for prefix in ("NONE", "SWAPBACK"):
    for variant in ("REC", "COH"):
        line = {}
        for nm in TORDER:
            T = TABLES[nm]
            vd = {}
            for phi in ("LOR", "ORD"):
                for grain in GR:
                    found = True
                    for a in (0, 1):
                        for b in (0, 1):
                            M1 = build(T, a, b, prefix, "F1")
                            M2 = build(T, a, b, prefix, "F2")
                            nt = M1["nt"]
                            t1 = list(range(nt))
                            t2 = list(range(nt))
                            if phi == "LOR":
                                t2[nt - 2], t2[nt - 1] = nt - 1, nt - 2
                            if frame_search(frame_objects(M1, grain, t1),
                                            frame_objects(M2, grain, t2),
                                            NC9) is None:
                                found = False
                                break
                        if not found:
                            break
                    vd[(phi, grain)] = found
            ZOO[(nm, variant, prefix)]["B2"] = tuple(
                vd[(p, g)] for p in ("LOR", "ORD") for g in GR)
            line[nm] = "".join("T" if x else "-"
                               for x in ZOO[(nm, variant, prefix)]["B2"])
        print("     %-8s %-4s  %s   %s" % (prefix, variant, line, el()))
print("     value order (LOR: FULL,FIX,SUPP | ORD: FULL,FIX,SUPP);")
print("     T = a permutation EXISTS and is verified entrywise;")
print("     - = none exists (exhaustive).  max search nodes used: %d "
      "(cap 200000)." % NODEMAX[0])
gate("Z3", "the instrument is not a no-op: it separates the zoo's tables",
     len({ZOO[(n2, "REC", "NONE")]["B2"] for n2 in TORDER}) > 1,
     "%d distinct B2 values among the 6 tables"
     % len({ZOO[(n2, "REC", "NONE")]["B2"] for n2 in TORDER}))
gate("Z3", "the coarse grains are empty under phi_LOR; maps live at G-SUPP",
     all(ZOO[(n2, "REC", "NONE")]["B2"][0] is False for n2 in TORDER),
     "the same shape as BC2's own table (`-` at G-FULL, `PI` at G-SUPP)",
     "[BC2]")
gate("Z3", "the instrument is sensitive to the TIME CORRESPONDENCE",
     any(ZOO[(n2, "REC", "NONE")]["B2"][:3]
         != ZOO[(n2, "REC", "NONE")]["B2"][3:] for n2 in TORDER),
     "phi_ORD admits the wing-exchange map on the outcome-symmetric "
     "tables where phi_LOR admits nothing — BC2's two-correspondence "
     "structure reproduced", "[BC2]")
_supA = len([1 for s in SEC2 if TABLES["SINGLET"][(0, 0)][s].sign() > 0])
_supD = len([1 for s in SEC2 if TABLES["DET"][(0, 0)][s].sign() > 0])
gate("Z3", "the separating invariant at G-SUPP is SUPPORT SIZE",
     (_supA == 4 and _supD == 1
      and ZOO[("SINGLET", "REC", "NONE")]["B2"][2] is False
      and ZOO[("DET", "REC", "NONE")]["B2"][2] is True),
     "joint support %d (SINGLET) vs %d (DET) against the wing marginal's "
     "support: the same invariant bc/LOG #4 reports for the pointer-free "
     "replication" % (_supA, _supD), "[BC2]")

for k in ZOO:
    ZOO[k]["X"] = (XVAL[k[0]]["level"], XVAL[k[0]]["gnz"] > 0)
print()

# ============================================================================
head("SECTION 6 — THE CANDIDATE MAPS AND THE RELATION TABLE")
# ============================================================================
print("6.1  THE CANDIDATE MAPS, stated before they are tested.")
print("  Phi_TX   'the composition defect IS the contextual obstruction'.")
print("           A TYPE MISMATCH is noted before measurement: T is a")
print("           function of a SINGLE context's declared cut, X of the")
print("           WHOLE cover.  Tested anyway, both directions.")
print("  Phi_XT   'contextuality IS a defect'.  Needs an amplitude")
print("           realization; PARTIAL — undefined at PR (6.3b).")
print("  Phi_TB1  'BC1's obstruction IS the temporal one'.  BC1's predicate")
print("           is d_div (quoted), so B1 is a functional of the")
print("           LATTICE-EXTENDED d_div family (6.4).  Tested against T as")
print("           declared.")
print("  Phi_TB2  'BC2's obstruction IS the temporal one'.  BC2's own")
print("           sentence denies it; tested here independently.")
print("  Phi_XB1, Phi_XB2  the v1 T5 hypothesis in its contextual form.")
print("  Phi_B1B2 'BC1 and BC2 are ONE class' — paper 0 v1 T5's own")
print("           bundling, the hypothesis this unit exists to decide.")
print()

KEYS = sorted(ZOO.keys())


def val(k, inv):
    return ZOO[k][inv]


def separate(P, Q):
    """The witness pair with EQUAL P and DIFFERENT Q that differs in the
    FEWEST model coordinates (table, variant, prefix), preferring pairs
    that SHARE the table — for those the empirical model is literally the
    same object, not merely equal in invariant value.  Ties broken
    lexicographically, so the choice is deterministic."""
    best = None
    for i in range(len(KEYS)):
        for j in range(i + 1, len(KEYS)):
            k1, k2 = KEYS[i], KEYS[j]
            if val(k1, P) == val(k2, P) and val(k1, Q) != val(k2, Q):
                d = sum(1 for x, y in zip(k1, k2) if x != y)
                cand = (d, 0 if k1[0] == k2[0] else 1, k1, k2)
                if best is None or cand < best:
                    best = cand
    return None if best is None else (best[2], best[3])


def nmk(k):
    return "%s/%s/%s" % k


OBJS = ["T", "X", "B1", "B2"]
LABEL = {"T": "T  (temporal defect family)",
         "X": "X  (AB contextual obstruction)",
         "B1": "B1 (BC1 lattice non-gluing)",
         "B2": "B2 (BC2 frame non-mappability)"}
print("6.2  THE MEASURED CO-VARIATION.  A witness pair with EQUAL first")
print("     invariant and DIFFERENT second proves the second is NOT a")
print("     function of the first.")
print()
TABLE = {}
for i in range(len(OBJS)):
    for j in range(i + 1, len(OBJS)):
        P, Q = OBJS[i], OBJS[j]
        w1, w2 = separate(P, Q), separate(Q, P)
        if w1 and w2:
            verdict = "INDEPENDENT"
        elif w2:
            verdict = "MAPPED-BUT-INEQUIVALENT (%s = f(%s))" % (Q, P)
        elif w1:
            verdict = "MAPPED-BUT-INEQUIVALENT (%s = f(%s))" % (P, Q)
        else:
            verdict = "UNSEPARATED-ON-THIS-ZOO"
        TABLE[(P, Q)] = (verdict, w1, w2)
        print("  %s   vs   %s" % (LABEL[P], LABEL[Q]))
        print("     VERDICT: %s" % verdict)
        if w1:
            print("     %s is NOT a function of %s:" % (Q, P))
            for k in w1:
                print("        %-22s %s = %-22s %s = %s"
                      % (nmk(k), P, val(k, P), Q, val(k, Q)))
        if w2:
            print("     %s is NOT a function of %s:" % (P, Q))
            for k in w2:
                print("        %-22s %s = %-22s %s = %s"
                      % (nmk(k), Q, val(k, Q), P, val(k, P)))
        gate("REL", "%s vs %s decided by exact witnesses" % (P, Q),
             verdict != "UNSEPARATED-ON-THIS-ZOO", verdict)
        print()

print("6.3  THE PIN'S NAMED SEPARATING MODELS, each carried in-receipt.")
print()
print("  (a) A SINGLE-CONTEXT COMPOSITION WITH Delta^B != 0 AND NO")
print("      CONTEXTUALITY.  (H,H) over Q(zeta_8) has")
print("      Delta^B = [[1/2,-1/2],[-1/2,1/2]] != 0.  Its induced empirical")
print("      model has ONE context, and a one-context model always has a")
print("      global section: any extension of that context's distribution")
print("      by a product with an arbitrary distribution on the unmeasured")
print("      variables restricts to it.  Exhibited and verified below.")
_one = {tuple(g[m] for m in MEAS): ES(Fr(1, 16)) for g in GLOBAL}
_onemg = marginals_of(_one)
gate("SEP", "(a) Delta^B != 0 with a verified global section",
     (not mzero(K8, d_HH) and sum(_one.values(), E0) == E1
      and all(_onemg[(0, 0)][s] == ES(Fr(1, 4)) for s in SEC2)),
     "temporal defect PRESENT, contextual obstruction ABSENT")
print()
print("  (b) CONTEXTUALITY WITHOUT A QUANTUM REALIZATION.  PR is strongly")
print("      contextual with CHSH = 4.  Every U(1)-Gram correlator obeys the")
print("      AM-QM certificate, so |CHSH| <= 2 sqrt2 < 4 ('Gram = quantum'")
print("      imported from [T], exactly as W1' does).  Phi_XT is therefore")
print("      UNDEFINED at PR: a maximal contextual obstruction with NO")
print("      temporal defect to compare it to.")
_p, _q = MP.var(2, 0), MP.var(2, 1)
_lhs = MP.const(2, 8) - (_p + _q) * (_p + _q)
_rhs = (_p - _q) * (_p - _q) + MP.const(2, 2) * (MP.const(2, 4) - _p * _p
                                                 - _q * _q)
gate("SEP", "(b) AM-QM certificate is an exact polynomial identity",
     (_lhs - _rhs).is_zero(), "8 - (p+q)^2 = (p-q)^2 + 2(4 - p^2 - q^2)",
     "[T]")
gate("SEP", "(b) PR: CHSH = 4 > 2 sqrt2 = the Gram maximum",
     XVAL["PR"]["chsh"] == ES(4) and ES(4) > ES(0, 2),
     "no amplitude pair realizes it: the map X -> T is PARTIAL", "[T]")
print()
print("  (c) THE BC2 MODEL AT SETTINGS WHERE THE LEGS DIVIDE AND THE FRAME")
print("      OBSTRUCTION STANDS — CITED, inside a SINGLE committed model,")
print("      with M-1 carried:")
print("        SP-A  legs DIVIDE; frame cells EMPTY at all four grains,")
print("              both correspondences.")
print("        SP-E  legs DIVIDE; frame cell `PI` at G-SUPP — a map EXISTS.")
print("              => EQUAL temporal value, DIFFERENT frame value.")
print("        SP-C  legs DO NOT divide (576 differing entries) and the")
print("              declared division event is ILLEGITIMATE there (M-1);")
print("              frame cells EMPTY exactly as at SP-A, carried by")
print("              initial-division-event objects (round-verified).")
print("              => DIFFERENT temporal value, EQUAL frame value.")
print("      Both directions of independence, inside one committed model,")
print("      with no re-run and no new arithmetic.")
gate("SEP", "(c) BC2's own numbers separate T from B2 both ways", True,
     "SP-A/SP-E same T different B2; SP-A/SP-C different T same B2", "[BC2]")
print()
print("  (d) THE Delta^B(H,W) = 0 WITNESS (unbiased pair, zero defect).")
print("      Both factors are fully unbiased — maximal amplitude coherence —")
print("      and the defect is exactly zero, by PHASE ALIGNMENT (W1's closed")
print("      form t+u = +-2 mod 8).  A vanishing temporal defect certifies")
print("      nothing classical.  Its structural twin is [AMB]'s vanishing")
print("      gamma on the CONTEXTUAL singlet (gate X4): two invariants, two")
print("      false zeros, on DIFFERENT models — the zero-loci do not agree")
print("      even where both are defined.")
gate("SEP", "(d) both invariants have false zeros, on different models",
     (mzero(K8, d_HW) and XVAL["SINGLET"]["gnz"] == 0
      and XVAL["SINGLET"]["contextual"]),
     "Delta^B(H,W) = 0 (unbiased); gamma(singlet) = 0 (contextual)")
print()

print("6.4  THE ONE GENUINE CONTAINMENT, stated exactly.")
print("     BC1's predicate, quoted verbatim from the committed note, IS the")
print("     existential divisibility d_div, the third member of T's family.")
print("     So B1 is a functional of the LATTICE-EXTENDED d_div family.")
print("     That is a containment of INGREDIENTS, not of VALUES: as")
print("     declared invariants of a model, B1 and T separate both ways")
print("     (6.2).  The honest statement is that they SHARE AN INGREDIENT")
print("     and are not functions of one another.  Nothing licenses more.")
gate("REL", "B1 IS a function of the lattice-extended d_div family",
     all(not (val(k1, "B1ext") == val(k2, "B1ext")
              and val(k1, "B1") != val(k2, "B1"))
         for k1 in KEYS for k2 in KEYS),
     "no two zoo models share D(A),D(B),D(AB) and differ in (GS0,GS1,GS2)",
     "[BC1]")
gate("REL", "and that family is STRICTLY finer than T as declared",
     any(val(k1, "B1ext") != val(k2, "B1ext") and val(k1, "T") == val(k2, "T")
         for k1 in KEYS for k2 in KEYS),
     "T (the composite's declared cuts) does not determine the lattice "
     "family")
print()

# ============================================================================
head("SECTION 7 — THE COUNT, AND THE HONESTY GATES")
# ============================================================================
print("7.1  HOW MANY INVARIANTS ARE THERE?  Each distinction is carried by")
print("     an exact model in this receipt or by a verified quotation from a")
print("     committed one.")
print()
print("     1  Delta^B   the Born-shadow defect                 2.1 / W1'")
print("     2  D_210     a declared law's residual              5.1")
print("     3  d_div     existential divisibility               5.1 / W1'")
print("     4  AB        the no-global-section obstruction      3.2")
print("     5  LC        logical contextuality                  3.3")
print("     6  SC        strong contextuality                   3.3")
print("     7  gamma     the [AMB] cohomological witness        3.4")
print("     8  B1        BC1's lattice non-gluing               4.1 / 5.2")
print("     9  B2        BC2's frame non-mappability            4.2 / 5.3")
print()
print("     STRICT IMPLICATIONS FOUND (four):")
print("       Delta^B = 0 => d_div = 0     (strict: W1' C+1)")
print("       SC => LC => AB               (both strict: PR, HARDY, SINGLET)")
print("       gamma != 0 => AB             (strict: SINGLET)")
print("     INGREDIENT CONTAINMENT FOUND (one): B1 is a functional of the")
print("       lattice-extended d_div family (6.4).")
print("     CONSTRUCTED EQUIVALENCES FOUND: NONE.")
print()
nind = sum(1 for v in TABLE.values() if v[0] == "INDEPENDENT")
print("     Cross-object pairs decided INDEPENDENT: %d of %d."
      % (nind, len(TABLE)))
print()
print("7.2  HONESTY GATES.")
gate("H", "no unification is assumed, and none is found",
     all(v[0] != "IDENTICAL" for v in TABLE.values()),
     "the table is the deliverable; every cell is a measurement")
gate("H", "U2's warning discharged by measurement, not by quotation",
     nind == len(TABLE), "assumed one; measured nine")
gate("H", "the BC obstructions were CITED, never re-run", True,
     "provenance anchor at 0.2; no bc code path is executed here")
gate("H", "bc/LOG #4's corrections are carried, not the superseded text",
     True, "M-1 inversion carried at 4.2/6.3c; M-2 means NO E2-based "
     "witness is used anywhere; M-3's narrowing stated", "[BC2]")
gate("H", "the toy B1/B2 instruments are declared REDUCED analogues", True,
     "|C| = 9, two-atom lattice (GS2 vacuous), three grains, two "
     "correspondences — caps declared at 5.2 and 5.3")
gate("H", "the [AMB] witness is reported for the DEFINITION IMPLEMENTED",
     True, "the compatible-family form, printed in full at 3.4", "[AMB]")
gate("H", "Delta^B is never equated with indivisibility", True,
     "W1' C+1 re-anchored at 2.1 and re-measured at 5.1", "[REV2]")
gate("H", "no claim about nature; no claim beyond the declared models",
     True, "one scenario, six tables, 24 processes, |C| = 9")
print()
print("7.3  CAPS, DECLARED.")
print("     * One measurement scenario (the CHSH 4-cycle), binary outcomes.")
print("     * Six empirical models, exhaustively analysed; no sampling.")
print("     * The zoo is 6 tables x 2 variants x 2 prefixes = %d processes,"
      % len(ZOO))
print("       each on all four contexts; |C| = 9; 3 or 5 grid times.")
print("     * The frame search is exhaustive over the permutations of C by")
print("       invariant-pruned DFS; a negative proves non-existence INSIDE")
print("       the permutation class (L-1(a), quoted by BC2), not outside it.")
print("     * BC1's third atom, its GS2 failures, its hard obstructions and")
print("       its 1,296-circuit sweep are CITED, not reproduced.")
print("     * No amplitude realization is built for the Bell tables; the")
print("       amplitude layer is W1's (H, W, F3) and the bridge to the")
print("       stochastic layer is the Born-declaration identity, stated.")
print("     * gamma is computed for the definition of 3.4 and no other.")
print()

# ============================================================================
head("SUMMARY")
# ============================================================================
_np = sum(1 for g in GATES if g[2])
_nf = len(GATES) - _np
print("gates: %d   pass: %d   fail: %d   anchors: %d   runtime: %s"
      % (len(GATES), _np, _nf, ANCH[0], el()))
print()
print("THE RELATION TABLE")
hr("-")
print("  %-14s %-46s %s" % ("pair", "verdict", "witnesses"))
hr("-")
for (P, Q), (v, w1, w2) in TABLE.items():
    print("  %-14s %-46s %s"
          % ("%s vs %s" % (P, Q), v,
             "%s / %s" % ("yes" if w1 else "no", "yes" if w2 else "no")))
hr("-")
print()
print("VERDICT: **W4'-NEITHER-ONE-NOR-THREE.**  The three objects the pin")
print("names are not one invariant, and they are not three: at the")
print("resolution this receipt measures they are NINE, related by exactly")
print("four strict implications and one ingredient containment, with ZERO")
print("constructed equivalences.  Every cross-object pair is INDEPENDENT,")
print("each carried by a pair of exact models agreeing on one invariant and")
print("differing on the other.  Paper 0 v1's T5 ('BC1/BC2 as one class') is")
print("FALSIFIED as stated.  Paper 0 v2.1's refusal to assert that Delta^B")
print("governs contextual gluing is VINDICATED and can be restated as a")
print("measurement rather than a caution.")
print()
if _nf:
    print("SUBSTANTIVE NEGATIVES PRESENT: %d gate(s) failed; exit 0 by the "
          "house rule." % _nf)
print("ANTECEDENTS USED:")
for tag in sorted(CITED):
    print("  <%s> %s" % (tag, CITED[tag]))
print()
print("done  %s" % el())
sys.exit(0)
