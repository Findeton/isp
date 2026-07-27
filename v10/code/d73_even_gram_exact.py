#!/usr/bin/env python3.13
"""
d73_even_gram_exact.py — v10 D73: THE EVEN GRAM.  Does the real
(dual-even) channel of the rooted boundary law host a rank-2 metric
response, or is `E_total` lossless and the even channel provably
scalar?

ROUND-1 REPAIRED, 2026-07-27 (`reviews/d73-round1-hostile-review.md`:
1 BLOCKER / 4 MAJOR / 5 MODERATE / 5 MINOR).  What the round changed,
named here because the numbers below moved with it:
  * **THE FIXTURE (BLOCKER).**  The first delivery anchored on p30
    `§25.3/§25.4`'s three dual pairs `((24576,540672), (25488,525208),
    (24606,549648))` and never read p30 `§26.2`, which audits the
    `N = 9` frontier, ranks that triple **11th**, prints its
    `TV9 = 1.676e-5` as the loser's score and says in the paper's own
    words that *"the previous theorem target is falsified if read as a
    final predictive law"*.  `§27` then SELECTS
    `((912,25104), (17288,525076), (24576,540672))`, at `TV9 = 0`
    exactly.  So the first delivery's central negative — no `K` moves
    `TV_9` off `1.676e-5` — was **fixture-guaranteed**: that residual
    is a sector-selection artefact no function of the even 3-vector can
    reach.  This receipt now runs BOTH fixtures, gates all four
    `TV9 = 0` frontier triples against the paper's own table, and asks
    the promoted-`K` question where it can have an answer.
  * **THE MECHANISM (MAJOR 4).**  "`TV_9` is monotone under refinement
    of the colouring" was asserted, not proved, and is not a general
    fact.  The receipt's own G3-d data carry the correct and exact
    mechanism: candidates whose atom-average weight function `h` is
    IDENTICAL to `full`'s give an identical `forward_tv` in one line.
    G3-g now gates that biconditional on both fixtures, with
    h-identity-breaking controls that do move the number.
  * **THE TRANSFER HINT (MAJOR 1/2, MODERATE 1/2).**  G5's census is
    swept over seven blueprints, its distinct matrices are counted, and
    its narrow control is MEASURED.  The hint inverts: see G5.
  * F3 is now explicitly and visibly deferred (MODERATE 3) instead of
    silently dropped.

RUN: `python3.13 v10/code/d73_even_gram_exact.py` from the repository
root.  The committed v7 campaign calls `int.bit_count()`, so it needs
Python >= 3.10; this environment's bare `python3` is 3.8 and crashes
inside a lifted namespace with no diagnostic.  A version guard below
turns that crash into an instruction.

PIN: v10/note-d73-even-gram-pin.md (STRICT, FROZEN, COMMITTED before
this file was written; it names claim P2, tests 1-3 and falsifiers
F1-F4).  Parents: D71c (v10/note-d71c-spin2-archaeology.md — the
"something 2" was `h^{ij}`; the even Gram located at
`v7/code/p30_reflection_positive_campaign.py:394-406` and discarded),
v2 paper 10 Prop 10.6 (the all-order signed-`h^{12}` no-go), v6 paper
4 `:1064` (`missing_components=8193`, verdict `FAILS-FULL-GR`), v6
paper 54 (anticommutator -> traceless symmetric rank-2), D63/D67 (the
wide charts a rank-2 form would need).

WHAT THIS RECEIPT REUSES RATHER THAN REBUILDS.
  * v7/code/p30_reflection_positive_campaign.py — THE COMMITTED
    CAMPAIGN.  Every definition it owns is lifted by AST extraction
    (defs/classes and four named module constants only, so no
    module-level print, gate or `sys.exit` can run): the record
    universe, the deletion graph, the feature cache, `DUAL_PAIRS`,
    `pair_values`, `colors_for_mode`, `atom_weights`, `atom_metrics`,
    `weights_by_mode`, `forward_tv`, `recurrence_errors`,
    `coarsening_identity`, `dual_key`, `even_func`, `odd_func`,
    **`matrix_entries` (THE GRAM, lines 394-406)** and
    `principal_minors_3`.  THE GRAM IS NEVER RE-IMPLEMENTED HERE.
  * v7/code/p29_projected_likelihood_basis_audit.py — imported from
    its own path (it is `__main__`-guarded), supplying `perms`,
    `canon_bits`, `permutation_order_bits`, `restrict_bits`,
    `fmt_frac`, ... exactly as p30 imports them.
  * v7/relativistic-isp-v7-paper30-rooted-boundary-law.md — the
    COMMITTED TEXT.  The seven even principal minors (:2991-2997),
    the three odd reflected diagonal entries (:3003-3005), the three
    i-twisted minors and the aggregate-geometry `TV_9` table
    (:2974-2976) are TEXT-SLICED out of the paper and compared
    string-for-string with this process's own output.  That is the
    anchor, and exit 1 lives there and nowhere else.
  * v10/code/d42b1_transport_exact.py, d47a, d55c, d58, d60, d63 —
    the D63 layer chain, replicated exactly as D63 builds it, for the
    G5 transfer probe only.  [SAMPLED]/context grade, labelled at
    every use.

EXACT.  Every Gram entry, minor, eigen-coefficient, `TV_9`, weight
and covariance below is an exact `Fraction`.  `Decimal` at prec 200 is
used ONLY for display and for the cubic root-finding in G2.  ACCURATE
LABELLING (MINOR 4): `[float port]` marks the EIGENVALUES, whose
digits are the float port of brackets certified by exact rational sign
changes.  The anisotropy ratios, Frobenius shares, condition number,
discriminant and window table are printed through `dfl(...)`, which is
an exact decimal TRUNCATION of an exact Fraction — exact input,
truncated display, and not tagged.  No number below is a float
computation.

SCOPE, binding at every citation.  Everything in G1-G4 is a statement
about the `N = 5..9` record window of v7 paper 30's rooted boundary
law under ONE of TWO named dual-pair triples, both of them the
paper's: the FALSIFIED rank-11 target of `§25` and the SELECTED
`TV9 = 0` triple of `§26.2/§27`.  Every gate says which.  No claim
about gravity, no claim about any continuum limit, no claim that any
object here is a metric.  G5 is a seven-blueprint sweep at one depth
and is labelled [SAMPLED] in its own gate text.

EXIT CODES (MINOR 3).  Exit 1 fires ONLY on G1 anchor breakage — the
committed objects failing to reproduce.  Every substantive negative,
F1 included, exits 0.  **So `exit 0` is a statement about G0/G1 and
about nothing else: it is NOT a summary of the FAIL count, and must
never be quoted as one.**  The `PASS / FAIL` line is the summary.
"""
import ast
import os
import re
import subprocess
import sys
import time
from collections import defaultdict
from decimal import Decimal as Dec, getcontext
from fractions import Fraction as Fr
from itertools import combinations, permutations, product

# MINOR 2 — the version guard.  v7's committed campaign calls
# `int.bit_count()` (p30:165), new in Python 3.10.  Without this line a
# reader following a bare `python3` gets an AttributeError from inside a
# lifted third-party namespace and no diagnostic at all.
if sys.version_info < (3, 10):
    sys.stderr.write(
        f"[D73] REFUSING TO RUN under Python "
        f"{sys.version_info.major}.{sys.version_info.minor}.  The committed "
        f"v7 campaign p30_reflection_positive_campaign.py calls "
        f"int.bit_count() (:165), which needs Python >= 3.10.  Run:\n"
        f"    python3.13 v10/code/d73_even_gram_exact.py\n")
    sys.exit(2)

getcontext().prec = 200
sys.setrecursionlimit(300000)
T00 = time.time()


def sec():
    return f"[t+{time.time() - T00:7.1f}s]"


PASS = FAIL = ANCHOR_FAIL = 0
GATES = []


def check(label, ok, detail="", anchor=False):
    global PASS, FAIL, ANCHOR_FAIL
    ok = bool(ok)
    PASS, FAIL = PASS + int(ok), FAIL + int(not ok)
    ANCHOR_FAIL += int(anchor and not ok)
    GATES.append((label.split(':')[0][:78], ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}"
          + (f"  ({detail})" if detail else "")
          + ("   [ANCHOR — exit 1 on breakage]" if anchor else ""))


OUTCOMES = []


def outcome(tag, text):
    OUTCOMES.append((tag, text))
    print(f"\n  [OUTCOME {tag}] {text}")


print("[D73 — THE EVEN GRAM: does the real channel host a rank-2 metric")
print("       response?  (pin v10/note-d73-even-gram-pin.md, claim P2)")
print("       ROUND-1 REPAIRED — reviews/d73-round1-hostile-review.md]")
print("  banner: v7 paper 30 computed a 3x3 reflected Gram on its three")
print("  dual-EVEN channels, printed seven principal minors, used them as")
print("  a positivity check, and then priced the law with the trace")
print("  E_total = sum_j E_j.  This receipt prints the MATRIX the corpus")
print("  never printed, decides F1 (Gram proportional to the identity),")
print("  promotes K(E) = k.E_total to K(E) = E^T N E and re-runs paper")
print("  30's own four gates on the promotion, and answers v6 paper 4's")
print("  FAILS-FULL-GR row.  F1 is a first-class no-go: NO NULL OUTCOME.")
print("  ROUND 1's BLOCKER, carried in the open: paper 30 §26.2 FALSIFIES")
print("  the §25 triple this unit first anchored on (it ranks 11th; its")
print("  TV9 = 1.676e-5 is the LOSER's score) and §27 SELECTS a triple at")
print("  TV9 = 0 exactly.  Both fixtures are run below and every gate")
print("  names which one it is speaking about.")

# ======================================================================
# G0 — LAYER ANCHORS.  Single source for every committed object.
# ======================================================================
print(f"\n{sec()} [G0 — LAYER ANCHORS: every committed object a single "
      f"source, lifted not retyped]")

ISP = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   '..', '..'))
P30 = os.path.join(ISP, 'v7', 'code', 'p30_reflection_positive_campaign.py')
P29 = os.path.join(ISP, 'v7', 'code', 'p29_projected_likelihood_basis_audit.py')
PAPER30 = os.path.join(ISP, 'v7',
                       'relativistic-isp-v7-paper30-rooted-boundary-law.md')

sys.path.insert(0, os.path.dirname(P29))
import p29_projected_likelihood_basis_audit as p29   # noqa: E402


def _no_exit(nodes):
    """No exit call survives an extracted body (the D63 gate shape)."""
    for n in nodes:
        for c in ast.walk(n):
            if isinstance(c, ast.Call):
                if (isinstance(c.func, ast.Attribute)
                        and c.func.attr in ('exit', '_exit')):
                    return False
                if (isinstance(c.func, ast.Name)
                        and c.func.id in ('exit', 'quit')):
                    return False
    return True


def _ext(path, marker, names=(), extra=None):
    """D60/D63's committed extraction idiom: keep only defs/classes (and
    the named module constants), so no module-level statement — print,
    gate, sys.exit — can run."""
    tree = ast.parse(open(path).read())
    keep = [n for n in tree.body
            if isinstance(n, (ast.FunctionDef, ast.ClassDef))
            or (isinstance(n, ast.Assign)
                and any(isinstance(x, ast.Name) and x.id in names
                        for x in n.targets))]
    g = {'Fr': Fr, 'Fraction': Fr, 'combinations': combinations,
         'permutations': permutations, 'product': product,
         'defaultdict': defaultdict, 'sys': sys, 'os': os, 'ast': ast,
         'time': time, 'Decimal': Dec, 'D': Dec, 'math': __import__('math')}
    if extra:
        g.update(extra)
    exec(compile(ast.fix_missing_locations(
        ast.Module(body=keep, type_ignores=[])), marker, 'exec'), g)
    return g, keep


_P30SRC = open(P30).read()
_P30TREE = ast.parse(_P30SRC)
_P30LINES = _P30SRC.splitlines(keepends=True)
P30NAMES = ('DUAL_PAIRS', 'POSTHOC_PAIRS', 'RAW_TO_CANON_CACHE',
            'SUBSET_PAIR_CACHE', 'checks', 'counts_by_n', 'reps_by_n',
            'exact_by_n')
_p29_names = {k: getattr(p29, k) for k in dir(p29) if not k.startswith('__')}
g30, _keep30 = _ext(P30, 'p30_ast', P30NAMES, extra=_p29_names)

# THE GRAM, character for character, located by ast.FunctionDef.
_SEG = {}
for _nd in _P30TREE.body:
    if isinstance(_nd, ast.FunctionDef):
        _SEG[_nd.name] = "".join(_P30LINES[_nd.lineno - 1:_nd.end_lineno])
_GRAM_SRC = _SEG['matrix_entries']
_MINOR_SRC = _SEG['principal_minors_3']

WANT30 = ('build_record_universe', 'build_decks_and_reverse',
          'build_feature_cache', 'pair_values', 'colors_for_mode',
          'atom_weights', 'atom_metrics', 'weights_by_mode',
          'total_variation', 'forward_tv', 'recurrence_errors',
          'coarsening_identity', 'dual_key', 'opposite_bits',
          'matrix_entries', 'principal_minors_3', 'even_func', 'odd_func',
          'dec_frac', 'fmt_dec_frac', 'max_weight_diff')
for _n in WANT30:
    globals()[_n] = g30[_n]
DUAL_PAIRS = g30['DUAL_PAIRS']
fmt_frac = p29.fmt_frac

check("G0-a SINGLE SOURCE, THE CAMPAIGN: v7's committed reflection-"
      "positive campaign is lifted by AST extraction from its own path — "
      "defs/classes plus four named module constants only, so not one of "
      "its module-level prints, gates or `sys.exit`s can execute inside "
      "this receipt.  The 21 objects this unit rides on are gated present "
      "and callable, `DUAL_PAIRS` is gated to be the committed triple, and "
      "**the Gram itself is gated character-for-character**: the body of "
      "`matrix_entries` must still carry the line "
      "`value += Fraction(count, total) * f(key) * g(target)` and the "
      "reflection switch `dual_key(key, n) if reflected else key`.  A "
      "change to p30's definition of the Gram changes this receipt's "
      "object and breaks this gate",
      all(callable(g30[n]) for n in WANT30)
      and DUAL_PAIRS == ((24576, 540672), (25488, 525208), (24606, 549648))
      and "value += Fraction(count, total) * f(key) * g(target)" in _GRAM_SRC
      and "dual_key(key, n) if reflected else key" in _GRAM_SRC
      and "matrix[i][i] * matrix[j][j] - matrix[i][j] * matrix[j][i]"
      in _MINOR_SRC
      and _no_exit(_keep30),
      f"{os.path.relpath(P30, ISP)}: {len(_keep30)} top-level nodes kept, "
      f"{len(WANT30)} objects lifted, exit-free = {_no_exit(_keep30)}; "
      f"matrix_entries = lines "
      f"{_GRAM_SRC.count(chr(10))} long; DUAL_PAIRS = {DUAL_PAIRS}",
      anchor=True)

check("G0-b SINGLE SOURCE, THE PRIMITIVES: p29's record primitives are "
      "IMPORTED from p29's own path (it is `__main__`-guarded, so the "
      "import runs no audit) and handed to the extracted p30 namespace as "
      "its globals, exactly as p30's own `from p29... import` line does.  "
      "`perms`, `canon_bits`, `permutation_order_bits`, `restrict_bits`, "
      "`height`, `relation_count`, `interval_counts`, `degree_moments`, "
      "`has_rel`, `bit_index` and `fmt_frac` are gated present",
      all(callable(getattr(p29, n)) for n in
          ('perms', 'canon_bits', 'permutation_order_bits', 'restrict_bits',
           'height', 'relation_count', 'interval_counts', 'degree_moments',
           'has_rel', 'bit_index', 'fmt_frac'))
      and p29.__file__ == P29,
      f"{os.path.relpath(P29, ISP)}; PRECISION_LINE = "
      f"{p29.PRECISION_LINE!r}", anchor=True)

# ---- the committed TEXT, sliced ---------------------------------------
_PT = open(PAPER30).read()


def _textblock(after, which=0):
    """Slice the `which`-th ```text fence that follows the marker."""
    i = _PT.index(after)
    for _ in range(which + 1):
        i = _PT.index("```text", i) + len("```text")
    j = _PT.index("```", i)
    return [ln.strip() for ln in _PT[i:j].strip().splitlines() if ln.strip()]


_MARK = "The reflected even Gram matrix has nonnegative principal minors."
PAPER_EVEN_MINORS = _textblock(_MARK, 0)
PAPER_ODD_DIAG = _textblock("The real odd reflected diagonal is negative:", 0)
PAPER_TWIST = _textblock(
    "After the `i`-twist, the odd-sector reflected Gram has nonnegative "
    "principal minors:", 0)
_TVROW = [r for r in _PT.splitlines() if r.startswith("| aggregate `L")]
PAPER_TV = {r.split('|')[1].strip().replace('aggregate ', '').strip('` '):
            (int(r.split('|')[2].strip()), r.split('|')[4].strip())
            for r in _TVROW}

# ---- THE BLOCKER's OWN SOURCE: §26.2's frontier table, §26.2's
# ---- falsification sentence and §27's selected triple, all TEXT-SLICED.
_PAIRRX = re.compile(r"\((\d+)\s*,\s*(\d+)\)")


def _table_after(marker):
    """The markdown table that follows `marker`: rows as split cell lists."""
    i = _PT.index(marker)
    rows, seen = [], False
    for ln in _PT[i:].splitlines()[1:]:
        s = ln.strip()
        if s.startswith('|'):
            seen = True
            cells = [c.strip() for c in s.strip('|').split('|')]
            if set("".join(cells)) <= set("-: "):
                continue
            rows.append(cells)
        elif seen and not s:
            break
    return rows


_FRONT_ROWS = _table_after(
    "The first four full-forward finalists have exact zero error:")
PAPER_FRONTIER = {}
for _r in _FRONT_ROWS[1:]:                       # [0] is the header row
    PAPER_FRONTIER[int(_r[0])] = {
        'triple': tuple((int(a), int(b)) for a, b in _PAIRRX.findall(_r[1])),
        'atoms': int(_r[2].strip('` ')), 'tv9': _r[3].strip('` '),
        'rec9': _r[4].strip('` ')}
PAPER_OLD_TARGET = tuple(
    (int(a), int(b)) for a, b in
    _PAIRRX.findall(_textblock("The old reflection-positive target:", 0)[0]))
_OLDSCORE = _textblock("ranks only `11` in this audited `N=9` frontier:", 0)
PAPER_OLD_TV9 = _OLDSCORE[0].split('=')[1].strip()
PAPER_OLD_REC9 = _OLDSCORE[1].split('=')[1].strip()
PAPER_FALSIFIED = ("So the previous theorem target is falsified if read as "
                   "a final predictive law.")
_SELBLK = _PT[_PT.index("The coarsest nonlookup recurrence-exact candidate "
                        "is therefore:"):][:400]
PAPER_SELECTED = tuple((int(a), int(b)) for a, b in _PAIRRX.findall(_SELBLK))

check("G0-c SINGLE SOURCE, THE COMMITTED NUMBERS: the anchor targets are "
      "TEXT-SLICED out of the committed paper, not retyped into this file. "
      "Seven even principal minors from the fence that follows paper 30's "
      "own sentence 'The reflected even Gram matrix has nonnegative "
      "principal minors', three odd reflected diagonal entries, three "
      "i-twisted minors, and the three aggregate-geometry rows (atoms and "
      "`TV_9`) of the section-25.3 table.  **ROUND 1's BLOCKER ADDS FOUR "
      "MORE SLICES, FROM 130 LINES FURTHER DOWN THE SAME FILE:** §26.2's "
      "`N = 9` frontier table (four triples, atoms, `TV9`, `rec9`), the "
      "fence naming the old reflection-positive target, the fence printing "
      "its rank-11 score, and §27's selected triple.  The unit's first "
      "delivery text-sliced §25 and stopped; that is exactly how it came "
      "to anchor on a falsified target",
      len(PAPER_EVEN_MINORS) == 7 and len(PAPER_ODD_DIAG) == 3
      and len(PAPER_TWIST) == 7 and set(PAPER_TV) == {'L1', 'L2', 'Linf'}
      and PAPER_EVEN_MINORS[0].startswith("98.6697")
      and PAPER_ODD_DIAG[0].startswith("-26.05")
      and set(PAPER_FRONTIER) == {1, 2, 3, 4}
      and all(len(PAPER_FRONTIER[r]['triple']) == 3 for r in PAPER_FRONTIER)
      and len(PAPER_SELECTED) == 3 and len(PAPER_OLD_TARGET) == 3
      and PAPER_FALSIFIED in _PT,
      f"{os.path.relpath(PAPER30, ISP)}: even minors {len(PAPER_EVEN_MINORS)}"
      f", odd diagonal {len(PAPER_ODD_DIAG)}, twisted {len(PAPER_TWIST)}, "
      f"TV rows {PAPER_TV}; §26.2 frontier ranks {sorted(PAPER_FRONTIER)} "
      f"with atoms "
      f"{[PAPER_FRONTIER[r]['atoms'] for r in sorted(PAPER_FRONTIER)]} and "
      f"TV9 {sorted({PAPER_FRONTIER[r]['tv9'] for r in PAPER_FRONTIER})}; "
      f"§27 selected {PAPER_SELECTED}; old target {PAPER_OLD_TARGET} scores "
      f"TV9={PAPER_OLD_TV9} rec9={PAPER_OLD_REC9}; the paper's own "
      f"falsification sentence is present = {PAPER_FALSIFIED in _PT}",
      anchor=True)

# ======================================================================
# G1 — THE ANCHOR.  Exit 1 lives here and nowhere else.
# ======================================================================
print(f"\n{sec()} [G1 — THE ANCHOR: reproduce the committed Gram, its "
      f"seven printed principal minors and the campaign's TV_9 table, in "
      f"this process, from the committed campaign's own code]")

WINDOW = (5, 6, 7, 8, 9)
NMAX = 9
print(f"  DECLARED WINDOW (pin P2 test 2): N = {WINDOW}, target N = {NMAX}. "
      f"Nothing in this receipt is computed outside it.")

_t = time.time()
for n in range(1, NMAX + 1):
    counts, reps, dist = build_record_universe(n)
    g30['counts_by_n'][n] = counts
    g30['reps_by_n'][n] = reps
    g30['exact_by_n'][n] = dist
_TU = time.time() - _t
_t = time.time()
decks, reverse = build_decks_and_reverse(g30['reps_by_n'], 1, NMAX)
g30['decks'], g30['reverse'] = decks, reverse
_TD = time.time() - _t
_t = time.time()
FC = build_feature_cache(g30['reps_by_n'], 1, NMAX)
g30['feature_cache'] = FC
_TF = time.time() - _t
CB, RB = g30['counts_by_n'], g30['reps_by_n']
print(f"  build times: universes {_TU:.1f}s, deletion graph {_TD:.1f}s, "
      f"feature cache {_TF:.1f}s")

REC_CENSUS = [len(RB[n]) for n in range(1, NMAX + 1)]
check("G1-a THE RECORD UNIVERSE reproduces, N = 1..9: the canonical "
      "record census and the total permutation count both come out of the "
      "committed builder in this process.  This is the substrate every "
      "later number stands on",
      REC_CENSUS == [1, 2, 5, 16, 63, 315, 1956, 14794, 131526]
      and sum(CB[9].values()) == 362880 and sum(CB[5].values()) == 120,
      f"records by N = {REC_CENSUS}; permutations at N = 9 = "
      f"{sum(CB[9].values())}", anchor=True)

even_functions = [even_func(i) for i in range(3)]
odd_functions = [odd_func(i) for i in range(3)]
G_EVEN = matrix_entries(even_functions, n=9, reflected=True)
G_ODD = matrix_entries(odd_functions, n=9, reflected=True)
G_TWIST = tuple(tuple(-v for v in row) for row in G_ODD)
EVEN_MIN = principal_minors_3(G_EVEN)
ODD_DIAG = tuple(G_ODD[i][i] for i in range(3))
TWIST_MIN = principal_minors_3(G_TWIST)

MY_EVEN = [fmt_dec_frac(v, 20) for v in EVEN_MIN]
MY_ODD = [fmt_dec_frac(v, 20) for v in ODD_DIAG]
MY_TWIST = [fmt_dec_frac(v, 20) for v in TWIST_MIN]

check("G1-b [THE PIN'S ANCHOR] THE COMMITTED EVEN GRAM REPRODUCES "
      "EXACTLY.  `matrix_entries(even_functions, reflected=True)` — the "
      "lifted p30:394-406 — is evaluated in this process on the "
      "reconstructed N = 9 universe, its seven principal minors are "
      "formatted with p30's OWN `fmt_dec_frac(v, 20)`, and the seven "
      "strings are compared character-for-character with the seven lines "
      "text-sliced out of paper 30 at :2991-2997.  All seven must match",
      MY_EVEN == PAPER_EVEN_MINORS,
      "; ".join(f"{a}=={b}" for a, b in zip(MY_EVEN, PAPER_EVEN_MINORS))
      if MY_EVEN == PAPER_EVEN_MINORS else
      f"MISMATCH mine={MY_EVEN} paper={PAPER_EVEN_MINORS}", anchor=True)

check("G1-c THE ODD SECTOR'S COMMITTED NUMBERS REPRODUCE TOO — the three "
      "negative real reflected diagonal entries (:3003-3005) and the seven "
      "i-twisted principal minors — so the even/odd pair this unit "
      "compares is the pair paper 30 published, not half of it",
      MY_ODD == PAPER_ODD_DIAG and MY_TWIST == PAPER_TWIST,
      f"odd diagonal {MY_ODD}; twisted minors match = "
      f"{MY_TWIST == PAPER_TWIST}", anchor=True)

_t = time.time()
MODE = {}
for m in ('known', 'full', 'even_abs', 'even_only', 'odd_abs',
          'agg_l1', 'agg_l2', 'agg_linf'):
    colors, weights, metrics = weights_by_mode(m)
    MODE[m] = {'colors': colors, 'weights': weights, 'metrics': metrics,
               'tv': forward_tv(weights),
               'rec': recurrence_errors(9, weights[9], weights[8])}
    print(f"    {m:<9} atoms9={MODE[m]['metrics'][9]['atoms']:<7} "
          f"TV9={fmt_frac(MODE[m]['tv'], 24)}  [{time.time() - _t:.1f}s]")
_TMODES = time.time() - _t
TV_COMMITTED = MODE['agg_l2']['tv']

_tvok = all(
    fmt_frac(MODE[k]['tv'], 24) == PAPER_TV[lbl][1]
    and MODE[k]['metrics'][9]['atoms'] == PAPER_TV[lbl][0]
    for k, lbl in (('agg_l1', 'L1'), ('agg_l2', 'L2'), ('agg_linf', 'Linf')))
check("G1-d THE AGGREGATE-GEOMETRY TABLE REPRODUCES: paper 30's §25.3 "
      "rows (atoms and `TV_9`) for the L1, L2 and Linf aggregates come out "
      "of the lifted `weights_by_mode` + `forward_tv` in this process, "
      "atom count and 24-digit `TV_9` string both.  The `agg_l2` row IS "
      "the committed instantiation of `K(E) = k.E_total` this unit is "
      "asked to promote, so G3's baseline is anchored before it is used",
      _tvok and MODE['agg_l2']['metrics'][9]['atoms'] == 66057,
      f"L1/L2/Linf atoms = "
      f"{[MODE[k]['metrics'][9]['atoms'] for k in ('agg_l1', 'agg_l2', 'agg_linf')]}"
      f" vs paper {[PAPER_TV[l][0] for l in ('L1', 'L2', 'Linf')]}; "
      f"agg_l2 TV9 = {fmt_frac(TV_COMMITTED, 24)}", anchor=True)

check("G1-e THE TWO COMMITTED CEILING IDENTITIES REPRODUCE, WITH THE "
      "CORRECTLY TARGETED NON-VACUITY CONTROL (MODERATE 5).  Paper 30 "
      "gates `TV_9(even_abs) == TV_9(full)` (the componentwise even/odd "
      "colouring loses nothing against the full signed one) and "
      "`TV_9(agg_l2) == TV_9(even_abs)` (the TRACE loses nothing against "
      "componentwise).  Both are exact Fraction equalities here.  The "
      "first delivery offered `known` as the non-vacuity control — but "
      "`known` ablates the even AND the odd data, so it shows only that "
      "the gate resolves the PAIR of channels.  The identity under test "
      "is about the EVEN coordinate, and p30's own `colors_for_mode` "
      "carries the single-channel ablations: `odd_abs` (even coordinate "
      "REMOVED) and `even_only` (odd coordinate removed).  Both are run "
      "here.  **The honest statement the gate now supports: the even "
      "axis's resolution is demonstrably NONZERO at the level of present-"
      "or-absent (removing it costs 43.1x) and demonstrably ZERO at every "
      "level finer than the trace (G3).**",
      MODE['even_abs']['tv'] == MODE['full']['tv']
      and MODE['agg_l2']['tv'] == MODE['even_abs']['tv']
      and MODE['odd_abs']['tv'] > MODE['agg_l2']['tv']
      and MODE['even_only']['tv'] > MODE['agg_l2']['tv']
      and MODE['known']['tv'] > MODE['odd_abs']['tv'],
      f"full = even_abs = agg_l2 = {fmt_frac(TV_COMMITTED, 24)}; "
      f"odd_abs (EVEN CHANNEL ABLATED) = "
      f"{fmt_frac(MODE['odd_abs']['tv'], 24)} "
      f"({float(MODE['odd_abs']['tv'] / TV_COMMITTED):.1f}x worse — THE "
      f"control the gate wanted); even_only (odd channel ablated) = "
      f"{fmt_frac(MODE['even_only']['tv'], 24)} "
      f"({float(MODE['even_only']['tv'] / TV_COMMITTED):.1f}x); known "
      f"(BOTH ablated) = {fmt_frac(MODE['known']['tv'], 24)} "
      f"(ratio {float(MODE['known']['tv'] / TV_COMMITTED):.1f}x worse)",
      anchor=True)

# ======================================================================
# G1-f / G1-g — THE ROUND-1 BLOCKER.  The fixture the first delivery
# anchored on is the one paper 30 declares falsified; the fixture paper
# 30 SELECTS scores TV9 = 0 exactly.  Both are gated against the paper.
# ======================================================================
FRONTIER = {r: PAPER_FRONTIER[r]['triple'] for r in sorted(PAPER_FRONTIER)}
SELECTED = PAPER_SELECTED
FALSIFIED_TRIPLE = DUAL_PAIRS

_t = time.time()
FRONT = {}
for _rk in sorted(FRONTIER):
    _c, _w, _m = weights_by_mode('agg_l2', pairs=FRONTIER[_rk])
    FRONT[_rk] = {'atoms': _m[9]['atoms'], 'tv': forward_tv(_w),
                  'rec': recurrence_errors(9, _w[9], _w[8])}
    print(f"    §26.2 rank {_rk}  {FRONTIER[_rk]}  agg_l2 atoms9="
          f"{FRONT[_rk]['atoms']:<7} TV9={fmt_frac(FRONT[_rk]['tv'], 24)}"
          f"  [{time.time() - _t:.1f}s]")
_TFRONT = time.time() - _t

check("G1-f **THE ROUND-1 BLOCKER, GATED AT ITS SOURCE: THIS UNIT'S FIRST "
      "ANCHOR TRIPLE IS THE ONE PAPER 30 ITSELF DECLARES FALSIFIED, AND "
      "THE NUMBER IT CALLED 'THE COMMITTED TV_9' IS THE RANK-11 LOSER'S "
      "SCORE.**  Paper 30 §26.2 audits the `N = 7` zero-TV frontier by "
      "exact `N = 9` recurrence and full forward TV, and prints four "
      "dual-pair triples with `TV9 = 0` and `rec9 = 0` EXACTLY.  All four "
      "are re-run here through p30's own `weights_by_mode(..., pairs=T)` "
      "— the parameter `pair_values`, `colors_for_mode` and "
      "`weights_by_mode` all carry precisely so the triple can be varied, "
      "and which the first delivery hard-coded away at every call site.  "
      "Gated: each triple's `agg_l2` atom count reproduces the paper's "
      "table to the unit and its `TV_9` is EXACTLY ZERO as a Fraction; "
      "and the string paper 30 prints for the old target's score is "
      "character-identical to the `TV_9` this receipt's G1-d reproduces.  "
      "**So `1.676e-5` is not 'the family's floor'.  It is a "
      "SECTOR-SELECTION residual — paper 30 drives it to 0 by changing "
      "the pairs — and no function whatever of the even 3-vector can "
      "reach an error that lives in the choice of which flags to look "
      "at**",
      all(FRONT[r]['tv'] == 0 for r in FRONT)
      and all(FRONT[r]['atoms'] == PAPER_FRONTIER[r]['atoms'] for r in FRONT)
      and all(FRONT[r]['rec'][0] == 0 for r in FRONT)
      and FALSIFIED_TRIPLE == PAPER_OLD_TARGET
      and fmt_frac(TV_COMMITTED, 24) == PAPER_OLD_TV9,
      f"§26.2 atoms mine "
      f"{[FRONT[r]['atoms'] for r in sorted(FRONT)]} vs paper "
      f"{[PAPER_FRONTIER[r]['atoms'] for r in sorted(PAPER_FRONTIER)]}; TV9 "
      f"{[fmt_frac(FRONT[r]['tv'], 4) for r in sorted(FRONT)]} vs paper "
      f"{[PAPER_FRONTIER[r]['tv9'] for r in sorted(PAPER_FRONTIER)]}; rec9 "
      f"all zero = {all(FRONT[r]['rec'][0] == 0 for r in FRONT)}; this "
      f"unit's first anchor {FALSIFIED_TRIPLE} == paper 30's 'old "
      f"reflection-positive target' = {FALSIFIED_TRIPLE == PAPER_OLD_TARGET}"
      f", which the paper ranks 11 at TV9={PAPER_OLD_TV9} and of which it "
      f"writes: {PAPER_FALSIFIED!r}", anchor=True)

_t = time.time()
SEL = {}
for m in ('full', 'even_abs', 'agg_l2'):
    _c, _w, _m = weights_by_mode(m, pairs=SELECTED)
    SEL[m] = {'colors': _c, 'weights': _w, 'atoms': _m[9]['atoms'],
              'tv': forward_tv(_w)}
    print(f"    SELECTED (§27) {m:<9} atoms9={SEL[m]['atoms']:<7} "
          f"TV9={fmt_frac(SEL[m]['tv'], 24)}  [{time.time() - _t:.1f}s]")
_TSEL = time.time() - _t
TV_SELECTED = SEL['agg_l2']['tv']

check("G1-g **THE SELECTED FIXTURE, GATED: PAPER 30 §27's OWN "
      "ADMISSIBILITY RULE CHOOSES A TRIPLE WITH `TV9 = 0` EXACTLY, AND "
      "THAT IS THE FIXTURE THE PROMOTED-K QUESTION IS RE-ASKED ON.**  "
      "§27's rule is record-intrinsic and does NOT optimise the held-out "
      "objective: low-order gate, then exact `N = 9` recurrence, then "
      "coarsest non-lookup quotient.  It selects "
      "`{(912,25104), (17288,525076), (24576,540672)}` — sliced from the "
      "paper here, not retyped — and the held-out audit gives "
      "`atoms9 = 65523`, `TV9 = 0`, `rec9 = 0`.  Gated: that triple's "
      "`full`, `even_abs` and `agg_l2` colourings ALL score exactly zero "
      "here, so the ceiling identity `TV(full) = TV(even_abs) = "
      "TV(agg_l2)` holds on the selected fixture too — at the value 0.  "
      "**The floor is therefore 0, not 1.676e-5, and 'the trace already "
      "sits at the family's floor' was a description of one superseded "
      "row**",
      SEL['agg_l2']['tv'] == 0 and SEL['full']['tv'] == 0
      and SEL['even_abs']['tv'] == 0
      and SEL['agg_l2']['atoms'] == PAPER_FRONTIER[4]['atoms']
      and SELECTED == FRONTIER[4] and SELECTED != FALSIFIED_TRIPLE,
      f"SELECTED = {SELECTED} (== §26.2 rank 4 = {SELECTED == FRONTIER[4]}); "
      f"agg_l2 atoms9 = {SEL['agg_l2']['atoms']} vs paper "
      f"{PAPER_FRONTIER[4]['atoms']}; TV9 full/even_abs/agg_l2 = "
      f"{[fmt_frac(SEL[m]['tv'], 4) for m in ('full', 'even_abs', 'agg_l2')]}"
      f"; full atoms9 = {SEL['full']['atoms']}, even_abs atoms9 = "
      f"{SEL['even_abs']['atoms']}", anchor=True)

if ANCHOR_FAIL:
    print(f"\n[STOP] {ANCHOR_FAIL} ANCHOR GATE(S) FAILED.  The committed "
          f"objects did not reproduce.  Nothing below is reported.")
    sys.exit(1)

# ======================================================================
# G2 — THE RANK-2 TEST.  The matrix the corpus never printed.
# ======================================================================
print(f"\n{sec()} [G2 — THE MATRIX THE CORPUS NEVER PRINTED, and F1]")


def dfl(x, d=24):
    """[float port] exact Fraction -> Decimal string, display only."""
    return format(+(Dec(x.numerator) / Dec(x.denominator)), f".{d}g")


print("  G^even_{jk} = sum_R P(R) E_j(R) E_k(R*), N = 9, exact Fractions:")
for i in range(3):
    print("    [ " + "  ".join(f"{dfl(G_EVEN[i][j], 18):>22}"
                               for j in range(3)) + " ]")
print("  as exact rationals:")
for i in range(3):
    print("    [ " + "  ".join(f"{str(G_EVEN[i][j]):>26}" for j in range(3))
          + " ]")

SYM = all(G_EVEN[i][j] == G_EVEN[j][i] for i in range(3) for j in range(3))
OFFD = [G_EVEN[i][j] for i, j in combinations(range(3), 2)]
DIAG = [G_EVEN[i][i] for i in range(3)]
MAXOFF = max(abs(v) for v in OFFD)
DIAGSPREAD = max(DIAG) - min(DIAG)

check("G2-a THE GRAM IS SYMMETRIC, and it is symmetric for a REASON this "
      "receipt gates rather than assumes: `P` is the pushforward of the "
      "uniform measure on the 362880 permutations, order reversal is a "
      "bijection of that set, so `P(R*) = P(R)` for every canonical "
      "record class — gated exhaustively — and the reflected two-point "
      "function is therefore automatically symmetric",
      SYM and all(CB[9][k] == CB[9][dual_key(k, 9)] for k in RB[9]),
      f"symmetric = {SYM}; classes with count(R) != count(R*) = "
      f"{sum(1 for k in RB[9] if CB[9][k] != CB[9][dual_key(k, 9)])} of "
      f"{len(RB[9])}")

check("G2-b **F1 IS DECIDED, AND IT DOES NOT FIRE.**  The pin's falsifier "
      "F1 reads: `G^even` is diagonal, or is a multiple of the identity — "
      "then `E_total` is lossless and the even channel provably cannot "
      "host a metric.  Measured: the three off-diagonal entries are all "
      "NONZERO and the three diagonal entries are all DIFFERENT.  The even "
      "channel's reflected two-point function is a genuinely anisotropic "
      "symmetric form, not a rescaled identity.  (What F1's *consequent* "
      "does at this window is a separate question and G3 decides it "
      "separately — the pin's biconditional is not assumed here)",
      MAXOFF > 0 and DIAGSPREAD > 0
      and all(v != 0 for v in OFFD) and len(set(DIAG)) == 3,
      f"off-diagonals G01, G02, G12 = {[dfl(v, 18) for v in OFFD]} "
      f"(all nonzero = {all(v != 0 for v in OFFD)}); diagonal = "
      f"{[dfl(v, 18) for v in DIAG]} (3 distinct = {len(set(DIAG)) == 3}); "
      f"max|off| = {dfl(MAXOFF, 18)}, diagonal spread = "
      f"{dfl(DIAGSPREAD, 18)}")

# ---- the reflection does nothing on the even channel -------------------
EV_VIOL = OD_VIOL = 0
for k in RB[9]:
    kd = dual_key(k, 9)
    for j in range(3):
        if even_functions[j](k) != even_functions[j](kd):
            EV_VIOL += 1
        if odd_functions[j](k) != -odd_functions[j](kd):
            OD_VIOL += 1
DUALPAIR_OK = all(dual_key(l, 5) == r for l, r in DUAL_PAIRS)
G_EVEN_RAWREF = matrix_entries(even_functions, n=9, reflected=False)
G_ODD_RAWREF = matrix_entries(odd_functions, n=9, reflected=False)

check("G2-c **THE REFLECTION IS AN IDENTITY ON THE EVEN CHANNEL, AND A "
      "SIGN ON THE ODD ONE — SO §25.4's POSITIVITY IS ALGEBRA, NOT A "
      "MEASUREMENT.**  Each of the three `DUAL_PAIRS` is gated to be a "
      "genuine order-dual pair of 5-element record types "
      "(`dual_key(left, 5) == right`).  Hence `E_j(R*) = E_j(R)` and "
      "`O_j(R*) = -O_j(R)` identically — verified on all 131526 records x "
      "3 channels, zero violations — and therefore the REFLECTED even "
      "Gram EQUALS the ordinary second-moment matrix `E[E_j E_k]`, while "
      "the reflected odd Gram equals MINUS `E[O_j O_k]`, exactly.  Both "
      "equalities are gated as exact Fraction identities.  Consequence, "
      "stated where it can be checked: paper 30's even reflection "
      "positivity is a Gram-matrix tautology (a second-moment matrix of "
      "real observables is always PSD) and its odd negativity plus "
      "`i`-twist repair is the same tautology with a sign",
      DUALPAIR_OK and EV_VIOL == 0 and OD_VIOL == 0
      and G_EVEN_RAWREF == G_EVEN
      and G_ODD_RAWREF == tuple(tuple(-v for v in r) for r in G_ODD),
      f"dual pairs verified = {DUALPAIR_OK}; even-parity violations = "
      f"{EV_VIOL}, odd-parity violations = {OD_VIOL} of "
      f"{3 * len(RB[9])} tests; reflected even == unreflected even = "
      f"{G_EVEN_RAWREF == G_EVEN}; reflected odd == -unreflected odd = "
      f"{G_ODD_RAWREF == tuple(tuple(-v for v in r) for r in G_ODD)}")


# ---- eigenstructure, exact coefficients + certified brackets -----------
def charpoly(M):
    """(c2, c1, c0) of lambda^3 - c2 lambda^2 + c1 lambda - c0, exact."""
    c2 = M[0][0] + M[1][1] + M[2][2]
    c1 = sum(M[i][i] * M[j][j] - M[i][j] * M[j][i]
             for i, j in combinations(range(3), 2))
    c0 = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
          - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
          + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    return c2, c1, c0


def cubic_disc(c2, c1, c0):
    """Discriminant of x^3 + b x^2 + c x + d with b=-c2, c=c1, d=-c0."""
    b, c, d = -c2, c1, -c0
    return (18 * b * c * d - 4 * b ** 3 * d + b * b * c * c
            - 4 * c ** 3 - 27 * d * d)


def peval(c2, c1, c0, x):
    return x ** 3 - c2 * x ** 2 + c1 * x - c0


def roots3(c2, c1, c0, lo, hi, iters=400):
    """Three real roots, isolated by EXACT rational sign changes on a
    refining grid, then bisected in exact rationals; the decimal digits
    printed later are a [float port] of certified rational brackets."""
    br, m = [], 4096
    prev_x = lo
    prev_s = peval(c2, c1, c0, lo)
    for i in range(1, m + 1):
        x = lo + (hi - lo) * Fr(i, m)
        s = peval(c2, c1, c0, x)
        if s == 0:
            br.append((x, x))
        elif prev_s != 0 and (prev_s > 0) != (s > 0):
            br.append((prev_x, x))
        prev_x, prev_s = x, s
    out = []
    for a, b in br:
        for _ in range(iters):
            if a == b:
                break
            mid = (a + b) / 2
            if (peval(c2, c1, c0, a) > 0) != (peval(c2, c1, c0, mid) > 0):
                b = mid
            else:
                a = mid
        out.append((a + b) / 2)
    return sorted(out), br


C2, C1, C0 = charpoly(G_EVEN)
DISC = cubic_disc(C2, C1, C0)
EIG, BRACK = roots3(C2, C1, C0, Fr(0), C2 + 1)
print(f"  characteristic polynomial (exact): lam^3 - ({dfl(C2, 20)}) lam^2 "
      f"+ ({dfl(C1, 20)}) lam - ({dfl(C0, 20)})")
print(f"  eigenvalues [float port of certified rational brackets]: "
      + ", ".join(dfl(e, 22) for e in reversed(EIG)))

TR = C2
TRACELESS = tuple(tuple(G_EVEN[i][j] - (TR / 3 if i == j else 0)
                        for j in range(3)) for i in range(3))
FROB_T = sum(TRACELESS[i][j] ** 2 for i in range(3) for j in range(3))
FROB_G = sum(G_EVEN[i][j] ** 2 for i in range(3) for j in range(3))
ANISO = FROB_T / (TR * TR / 3)

check("G2-d THE EIGENSTRUCTURE IS THREE DISTINCT POSITIVE EIGENVALUES, "
      "certified exactly.  The characteristic polynomial's coefficients "
      "are the committed principal minors themselves (`c2` = the trace = "
      "the three 1x1 minors, `c1` = the sum of the three 2x2 minors, `c0` "
      "= the 3x3 minor), so the eigen-problem is a rearrangement of the "
      "numbers paper 30 printed and nothing new is imported.  The cubic "
      "discriminant is EXACTLY POSITIVE (three distinct real roots), all "
      "three roots are bracketed by exact rational sign changes strictly "
      "inside (0, tr], and the spectrum is therefore strictly "
      "positive-definite with NO repeated eigenvalue — which is the "
      "sharpest possible negation of `G = lambda I`",
      DISC > 0 and len(EIG) == 3 and all(e > 0 for e in EIG)
      and C1 == sum(EVEN_MIN[3:6]) and C2 == sum(EVEN_MIN[:3])
      and C0 == EVEN_MIN[6],
      f"discriminant = {dfl(DISC, 12)} > 0; coefficients rebuilt from the "
      f"committed minors = {C2 == sum(EVEN_MIN[:3]) and C1 == sum(EVEN_MIN[3:6]) and C0 == EVEN_MIN[6]}; "
      f"eigenvalues [float port] = {[dfl(e, 18) for e in reversed(EIG)]}; "
      f"condition number lam_max/lam_min = {dfl(EIG[2] / EIG[0], 12)}")

check("G2-e THE ANISOTROPY MEASURED, AND REPORTED WHICHEVER WAY IT LANDS "
      "(no majority is claimed and none is found).  The traceless part of "
      "`G^even` is exactly nonzero — which is all F1 turns on — and it "
      "carries a MINORITY of the squared Frobenius weight: the isotropic "
      "part is the larger piece, as it must be for a second-moment matrix "
      "of three positively-correlated nonnegative counts.  Reported as "
      "the exact dimensionless ratio ||G - (tr/3)I||_F^2 / ((tr)^2/3), "
      "which is exactly 0 for any multiple of the identity, together with "
      "the traceless share of ||G||_F^2 for calibration",
      ANISO > 0 and FROB_T > 0 and FROB_T < FROB_G,
      f"||traceless||_F^2 = {dfl(FROB_T, 18)}, ||G||_F^2 = "
      f"{dfl(FROB_G, 18)}, traceless share of ||G||_F^2 = "
      f"{dfl(FROB_T / FROB_G, 12)} (a MINORITY — stated as measured), "
      f"anisotropy ratio = {dfl(ANISO, 12)}, exactly 0 for lambda.I")

# ---- the mean/covariance split: is the anisotropy a VECTOR in disguise? -
P9 = {k: Fr(CB[9][k], 362880) for k in RB[9]}
MU = tuple(sum(P9[k] * even_functions[j](k) for k in RB[9]) for j in range(3))
COV = tuple(tuple(G_EVEN[i][j] - MU[i] * MU[j] for j in range(3))
            for i in range(3))
COV_OFF = [COV[i][j] for i, j in combinations(range(3), 2)]
C2c, C1c, C0c = charpoly(COV)
EIGC, _ = roots3(C2c, C1c, C0c, Fr(0), C2c + 1)
COV_ANISO = (sum((COV[i][j] - (C2c / 3 if i == j else 0)) ** 2
                 for i in range(3) for j in range(3)) / (C2c * C2c / 3))

check("G2-f **THE ANISOTROPY IS NOT MERELY THE CHANNEL MEANS.**  A "
      "second-moment matrix always contains the rank-1 piece `mu mu^T`, "
      "and a form that is `mu mu^T + lambda I` carries a VECTOR's worth of "
      "structure wearing a matrix's clothes.  Subtracting it: the centred "
      "covariance `Cov = G - mu mu^T` is computed exactly, and it too has "
      "all three off-diagonals nonzero, three distinct eigenvalues and a "
      "nonzero traceless part.  So the even channel's rank-2 structure "
      "survives the removal of its rank-1 mean",
      all(v != 0 for v in COV_OFF) and len(set(EIGC)) == 3
      and all(e > 0 for e in EIGC) and COV_ANISO > 0,
      f"mu = {[dfl(m, 14) for m in MU]}; Cov off-diagonals = "
      f"{[dfl(v, 14) for v in COV_OFF]}; Cov eigenvalues [float port] = "
      f"{[dfl(e, 14) for e in reversed(EIGC)]}; Cov anisotropy ratio = "
      f"{dfl(COV_ANISO, 10)}")

# ---- raw vs P(R)-weighted (the pin asks for both) ----------------------
def gram_variant(n, weightfn, reflected=True):
    """THIS UNIT'S variant of the committed Gram: same bilinear shape,
    a declared weight in place of `Fraction(count, total)`.  Gated at
    n = 9, weight = P(R), against the committed `matrix_entries`."""
    keys = list(RB[n])
    W = {k: weightfn(k) for k in keys}
    rows = []
    for j in range(3):
        row = []
        for k in range(3):
            v = Fr(0)
            for key in keys:
                tgt = dual_key(key, n) if reflected else key
                row_j = E_at(n, j, key)
                col_k = E_at(n, k, tgt)
                v += W[key] * row_j * col_k
            row.append(v)
        rows.append(tuple(row))
    return tuple(rows)


def E_at(n, j, key):
    f = FC[n]['flags5'][key]
    l, r = DUAL_PAIRS[j]
    return f.get(l, 0) + f.get(r, 0)


def O_at(n, j, key):
    f = FC[n]['flags5'][key]
    l, r = DUAL_PAIRS[j]
    return f.get(l, 0) - f.get(r, 0)


G_P = gram_variant(9, lambda k: Fr(CB[9][k], 362880))
G_RAW = gram_variant(9, lambda k: Fr(1, len(RB[9])))
C2r, C1r, C0r = charpoly(G_RAW)
EIGR, _ = roots3(C2r, C1r, C0r, Fr(0), C2r + 1)
RAW_OFF = [G_RAW[i][j] for i, j in combinations(range(3), 2)]
RAW_ANISO = (sum((G_RAW[i][j] - (C2r / 3 if i == j else 0)) ** 2
                 for i in range(3) for j in range(3)) / (C2r * C2r / 3))

check("G2-g BOTH WEIGHTINGS THE SOURCE DISTINGUISHES CARRY THE "
      "ANISOTROPY.  This unit's `gram_variant` is FIRST gated to "
      "reproduce the committed `matrix_entries` output entry-for-entry at "
      "`n = 9` with weight `P(R) = count/9!` — so the variant is the "
      "committed object with one declared slot — and is THEN re-run with "
      "the RAW class-uniform weight `1/131526`, which the committed code "
      "never uses.  Under both weights all three off-diagonals are "
      "nonzero, all three eigenvalues are distinct and positive, and the "
      "traceless fraction is nonzero.  F1 is not an artefact of the "
      "measure",
      G_P == G_EVEN and all(v != 0 for v in RAW_OFF)
      and len(set(EIGR)) == 3 and all(e > 0 for e in EIGR)
      and RAW_ANISO > 0,
      f"variant == committed at P(R) = {G_P == G_EVEN}; RAW "
      f"off-diagonals = {[dfl(v, 12) for v in RAW_OFF]}; RAW eigenvalues "
      f"[float port] = {[dfl(e, 12) for e in reversed(EIGR)]}; RAW "
      f"anisotropy ratio = {dfl(RAW_ANISO, 10)} vs P-weighted "
      f"{dfl(ANISO, 10)}")

# ---- the window: does the anisotropy persist across N = 5..9? ----------
WIN = {}
for n in WINDOW:
    tot = sum(CB[n].values())
    Gn = gram_variant(n, lambda k, n=n, t=tot: Fr(CB[n][k], t))
    c2, c1, c0 = charpoly(Gn)
    en, _ = roots3(c2, c1, c0, Fr(0), c2 + 1)
    an = (sum((Gn[i][j] - (c2 / 3 if i == j else 0)) ** 2
              for i in range(3) for j in range(3)) / (c2 * c2 / 3)) if c2 else Fr(0)
    off = [Gn[i][j] for i, j in combinations(range(3), 2)]
    WIN[n] = {'G': Gn, 'eig': en, 'aniso': an, 'off': off,
              'nz': sum(1 for v in off if v != 0), 'tr': c2,
              'disc': cubic_disc(c2, c1, c0)}
    print(f"    N={n}: trace {dfl(c2, 12):>16}  anisotropy "
          f"{dfl(an, 10):>14}  nonzero off-diagonals {WIN[n]['nz']}/3  "
          f"discriminant {dfl(WIN[n]['disc'], 8):>14}  distinct "
          f"eigenvalues found {len(set(en))} {[dfl(e, 8) for e in reversed(en)]}")
print("  the two low-N Grams in full (exact rationals):")
for n in (5, 6):
    for i in range(3):
        print(f"    N={n}  [ " + "  ".join(f"{str(WIN[n]['G'][i][j]):>18}"
                                           for j in range(3)) + " ]")

DISJOINT5 = sum(1 for k in RB[5] for a, b in combinations(range(3), 2)
                if E_at(5, a, k) * E_at(5, b, k) != 0)
FIRST_FULL = min([n for n in WINDOW if WIN[n]['nz'] == 3] or [0])
check("G2-h **F1's LITERAL CONDITION HOLDS AT THE BOTTOM OF THE PIN'S OWN "
      "WINDOW AND IS BROKEN BY DEPTH — the off-diagonal is GENERATED, not "
      "intrinsic.**  The Gram is recomputed at every N in the declared "
      "window 5..9.  At N = 5 it is EXACTLY DIAGONAL, and for a reason "
      "this receipt gates rather than observes: the three even channels "
      "are counts of 5-element induced subposets, so at N = 5 each record "
      "has exactly one 5-subset and the three channel indicators have "
      "DISJOINT SUPPORT (zero records carry two channels at once) — the "
      "product `E_a E_b` vanishes identically for a != b.  Anisotropy is "
      "still present at N = 5, but only as unequal diagonal entries.  The "
      "second off-diagonal switches on at N = 6 and all three from N = 7 "
      "up, and the anisotropy ratio rises monotonically across the "
      "window.  **So the honest reading of F1 is N-dependent: 'G^even is "
      "diagonal' is TRUE at N = 5 and FALSE from N = 7 on, and the "
      "off-diagonal structure is a product of records being deeper than "
      "the flag size, not a fact about the channels**",
      all(WIN[n]['aniso'] > 0 for n in WINDOW)
      and DISJOINT5 == 0 and WIN[5]['nz'] == 0 and WIN[9]['nz'] == 3
      and FIRST_FULL == 7
      and all(WIN[a]['aniso'] < WIN[b]['aniso']
              for a, b in zip(WINDOW, WINDOW[1:])),
      f"records at N = 5 carrying two channels at once = {DISJOINT5} of "
      f"{len(RB[5])}; nonzero off-diagonals by N = "
      f"{ {n: WIN[n]['nz'] for n in WINDOW} }; first N with all three = "
      f"{FIRST_FULL}; anisotropy ratio by N = "
      f"{ {n: dfl(WIN[n]['aniso'], 8) for n in WINDOW} } (monotone rising)")

# ---- G2-i: THE SAME QUESTION ON THE FIXTURE PAPER 30 SELECTED ---------
def gram_on(T, n=9):
    """p30's OWN `matrix_entries(even_func(...), reflected=True)` on a
    different dual-pair triple.  `even_func`'s closure reads `DUAL_PAIRS`
    out of the lifted p30 namespace at call time, so the triple is
    rebound there for the duration and restored (and the restoration is
    gated below).  Nothing is re-implemented."""
    _old = g30['DUAL_PAIRS']
    g30['DUAL_PAIRS'] = T
    try:
        ef = [g30['even_func'](i) for i in range(3)]
        return matrix_entries(ef, n=n, reflected=True)
    finally:
        g30['DUAL_PAIRS'] = _old


_t = time.time()
G_SEL = gram_on(SELECTED)
_TGSEL = time.time() - _t
SEL_OFF = [G_SEL[i][j] for i, j in combinations(range(3), 2)]
SEL_DIAG = [G_SEL[i][i] for i in range(3)]
C2s, C1s, C0s = charpoly(G_SEL)
SEL_ANISO = (sum((G_SEL[i][j] - (C2s / 3 if i == j else 0)) ** 2
                 for i in range(3) for j in range(3)) / (C2s * C2s / 3))
SEL_STAB = [p for p in permutations(range(3))
            if all(G_SEL[p[i]][p[j]] == G_SEL[i][j]
                   for i in range(3) for j in range(3))]
SEL_DISC = cubic_disc(C2s, C1s, C0s)
SEL_PAIRS_OK = all(dual_key(l, 5) == r for l, r in SELECTED)
print("  G^even on the SELECTED (§27) triple, N = 9, exact rationals:")
for i in range(3):
    print("    [ " + "  ".join(f"{str(G_SEL[i][j]):>26}" for j in range(3))
          + " ]")

check("G2-i **THE GENUINE G2 SURVIVOR: ON THE FIXTURE PAPER 30 ITSELF "
      "SELECTED, THE EVEN GRAM IS ANISOTROPIC WITH A TRIVIAL "
      "STABILISER — AND MORE ANISOTROPIC THAN ON THE FALSIFIED ONE.**  "
      "The whole of G2 was computed on the rank-11 target (G1-f).  It is "
      "recomputed here on §27's selected triple, through p30's own "
      "`even_func` + `matrix_entries` with `DUAL_PAIRS` rebound in the "
      "lifted namespace and gated restored.  Each of the selected pairs "
      "is first gated to be a genuine order-dual pair of 5-element record "
      "types (`dual_key(left, 5) == right`), exactly as G2-c gates the "
      "old ones.  Measured: three nonzero off-diagonals, three distinct "
      "diagonal entries, `S_3` stabiliser of order 1, exactly positive "
      "discriminant, and an anisotropy ratio of 0.5114 against the "
      "falsified fixture's 0.3958.  **So F1's non-firing and P2's "
      "rank-2 factual half are NOT fixture artefacts: they transfer to "
      "the selected fixture and are stronger there.  It is the G3 half — "
      "'no `K` moves the number' — that was fixture-guaranteed**",
      SEL_PAIRS_OK and all(v != 0 for v in SEL_OFF)
      and len(set(SEL_DIAG)) == 3 and len(SEL_STAB) == 1
      and SEL_DISC > 0 and SEL_ANISO > ANISO
      and g30['DUAL_PAIRS'] == FALSIFIED_TRIPLE,
      f"SELECTED = {SELECTED}, dual-pair gates all satisfied = "
      f"{SEL_PAIRS_OK}; off-diagonals = {[dfl(v, 12) for v in SEL_OFF]} "
      f"(nonzero {sum(1 for v in SEL_OFF if v != 0)}/3); diagonal = "
      f"{[dfl(v, 12) for v in SEL_DIAG]}; anisotropy ratio = "
      f"{dfl(SEL_ANISO, 12)} vs the falsified fixture's {dfl(ANISO, 12)}; "
      f"S_3 stabiliser order = {len(SEL_STAB)}; discriminant = "
      f"{dfl(SEL_DISC, 10)} > 0; DUAL_PAIRS restored in the lifted "
      f"namespace = {g30['DUAL_PAIRS'] == FALSIFIED_TRIPLE}  [{_TGSEL:.1f}s]")

F1_FIRES = not (MAXOFF > 0 and DIAGSPREAD > 0)
outcome("G2 / F1",
        ("F1 FIRES — G^even is (a multiple of) the identity."
         if F1_FIRES else
         "**F1 DOES NOT FIRE.**  G^even is a genuinely anisotropic "
         "positive-definite symmetric form: three distinct nonzero "
         "off-diagonals, three distinct eigenvalues "
         f"{[dfl(e, 10) for e in reversed(EIG)]}, condition number "
         f"{dfl(EIG[2] / EIG[0], 8)}, traceless Frobenius fraction "
         f"{dfl(FROB_T / FROB_G, 8)}; and the anisotropy survives "
         "centring (G2-f) and reweighting (G2-g).  TWO QUALIFICATIONS "
         "THE UNIT PUTS IN ITS OWN HEADLINE.  (1) It does not fire AT "
         "N = 9; at N = 5, the bottom of the pin's own declared window, "
         "the Gram IS exactly diagonal and F1's literal condition holds "
         "— the off-diagonal is generated by record depth exceeding the "
         "flag size and switches on at N = 6/7 (G2-h).  (2) The same "
         "gates show WHY the object is anisotropic: on the even "
         "channel the reflection is the identity map (G2-c), so this "
         "'reflected Gram' is the ordinary second-moment matrix of three "
         "nonnegative counting observables, and its positive-definiteness "
         "was never evidence of anything.  (3) AND IT DOES NOT FIRE ON "
         "THE RIGHT FIXTURE EITHER: on §27's SELECTED triple the Gram is "
         f"anisotropic at ratio {dfl(SEL_ANISO, 8)} — MORE than the "
         f"falsified fixture's {dfl(ANISO, 8)} — with `S_3` stabiliser "
         "order 1 (G2-i).  This half of the unit survives the round-1 "
         "refixturing intact."))

# ======================================================================
# G3 — THE QUADRATIC PROMOTION.  K(E) = E^T N E on paper 30's own gates.
# ======================================================================
print(f"\n{sec()} [G3 — THE QUADRATIC PROMOTION: K(E) = E^T N E in place "
      f"of K(E) = k.E_total, re-run through paper 30's own four gates]")


def colors_for_K(n, tag, evenfn, pairs=None):
    """p30's `colors_for_mode` with ONE slot changed: the even coordinate.
    Everything else — the `known` base tuple, the odd coordinate
    `Q_odd = sum_j O_j^2`, the colour tuple's shape — is p30's `agg_l2`
    branch verbatim.  Gated below to reproduce `colors_for_mode(n,
    'agg_l2')` EXACTLY when `evenfn = sum`.  `pairs` defaults to the
    falsified §25 triple and is passed explicitly for the SELECTED
    fixture (round 1's BLOCKER: it must be varied, not hard-coded)."""
    pairs = DUAL_PAIRS if pairs is None else pairs
    colors = {}
    for key in RB[n]:
        base = FC[n]['known'][key]
        flags = FC[n]['flags5'][key]
        values = pair_values(flags, pairs)
        E = tuple(ev for _l, _r, ev, _o in values)
        O = tuple(od for _l, _r, _ev, od in values)
        colors[key] = ("mode", tag, base, (evenfn(E), sum(o * o for o in O)))
    return colors


def run_K(tag, evenfn, label, pairs=None, ref=None):
    """`ref` is the `full` colouring/weights of the SAME fixture — the
    reference the coarsening identity and the h-weight difference are
    taken against."""
    ref = MODE['full'] if ref is None else ref
    colors, weights, metrics = {}, {}, {}
    for n in range(1, NMAX + 1):
        colors[n] = colors_for_K(n, tag, evenfn, pairs)
        weights[n] = atom_weights(colors[n], CB[n])
        metrics[n] = atom_metrics(colors[n])
    tv = forward_tv(weights)
    rec = recurrence_errors(9, weights[9], weights[8])
    dmax = max(abs(weights[9][k] - weights[9][dual_key(k, 9)]) for k in RB[9])
    coarse = [coarsening_identity(ref['colors'], colors,
                                  ref['weights'], weights, n)
              for n in WINDOW]
    hdiff = max(abs(weights[9][k] - ref['weights'][9][k]) for k in RB[9])
    return {'label': label, 'tv': tv, 'rec': rec, 'dual': dmax,
            'atoms': metrics[9]['atoms'], 'max_atom': metrics[9]['max_atom'],
            'lookup': metrics[9]['lookup'], 'colors': colors,
            'weights': weights, 'coarse': coarse, 'hdiff': hdiff}


_probe = colors_for_K(7, 'agg_l2', sum)
FIDELITY = all(colors_for_K(n, 'agg_l2', sum) == MODE['agg_l2']['colors'][n]
               for n in WINDOW)
FIDELITY_SEL = all(colors_for_K(n, 'agg_l2', sum, SELECTED)
                   == SEL['agg_l2']['colors'][n] for n in WINDOW)
check("G3-a **OPERATIONALIZATION FIDELITY, GATED BEFORE ANYTHING IS "
      "PROMOTED** (the D68 round-1 BLOCKER's lesson).  The promoted "
      "colouring is not a new invention: `colors_for_K` is p30's own "
      "`colors_for_mode(..., 'agg_l2')` branch with exactly one slot "
      "replaced — the even coordinate.  With that slot set to `sum` it "
      "must reproduce p30's `agg_l2` colour DICTIONARY key-for-key at "
      "every N in the window, and the downstream machinery "
      "(`atom_weights`, `atom_metrics`, `forward_tv`, "
      "`recurrence_errors`, `coarsening_identity`) is p30's, unmodified. "
      "If this gate fails, every number in G3 is about a different law.  "
      "The same fidelity is now gated on the SELECTED fixture too, with "
      "`pairs` passed through instead of hard-coded",
      FIDELITY and FIDELITY_SEL and len(_probe) == len(RB[7]),
      f"colour dictionaries identical at N = {WINDOW}: falsified fixture "
      f"{FIDELITY}, SELECTED fixture {FIDELITY_SEL}; N=7 probe size "
      f"{len(_probe)} == {len(RB[7])}")

GG = G_EVEN
DET = C0
ADJ = tuple(tuple(
    ((GG[(j + 1) % 3][(i + 1) % 3] * GG[(j + 2) % 3][(i + 2) % 3])
     - (GG[(j + 1) % 3][(i + 2) % 3] * GG[(j + 2) % 3][(i + 1) % 3]))
    for j in range(3)) for i in range(3))


def qform(M):
    return lambda E: sum(M[i][j] * E[i] * E[j] for i in range(3)
                         for j in range(3))


I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
NCAND = [
    ('lin     ', 'K = k.E_total  [THE COMMITTED FORM]', sum),
    ('quad-I  ', "N = diag(k,k,k) = I  [the pin's F2 reference]",
     qform(I3)),
    ('quad-G  ', 'N = G^even itself (the Gram, exact rationals)',
     qform(GG)),
    ('quad-adj', 'N = adj(G^even) ~ G^{-1} (exact, PD)', qform(ADJ)),
    ('quad-cov', 'N = Cov = G - mu mu^T', qform(COV)),
    ('quad-D1 ', 'N = diag(5,5,3)  [p30 §26 odd-sector winner, ported]',
     qform(((5, 0, 0), (0, 5, 0), (0, 0, 3)))),
    ('quad-D2 ', 'N = diag(1,2,3)  (anisotropic diagonal)',
     qform(((1, 0, 0), (0, 2, 0), (0, 0, 3)))),
    ('quad-OD1', 'N = I + offdiag(1)  (isotropic diagonal, off-diagonal on)',
     qform(((1, 1, 1), (1, 1, 1), (1, 1, 1)))),
    ('quad-OD2', 'N = 3I - offdiag(1)  (PD, negative off-diagonal)',
     qform(((3, -1, -1), (-1, 3, -1), (-1, -1, 3)))),
    ('bilin-G ', 'the LINEAR contraction of the Gram, k_j = sum_k G_jk',
     lambda E: sum(sum(GG[j][k] for k in range(3)) * E[j] for j in range(3))),
    ('comp    ', 'THE CEILING: componentwise (E_1, E_2, E_3), no '
     'contraction at all', lambda E: E),
]
KRES = {}
_t = time.time()
print("  ON THE FALSIFIED §25 FIXTURE (G1-f) — the eleven the pin's F2 "
      "names:")
for tag, lab, fn in NCAND:
    KRES[tag] = run_K('agg_l2' if tag.strip() == 'lin' else 'd73_' + tag.strip(),
                      fn, lab)
    r = KRES[tag]
    print(f"    {tag} atoms9={r['atoms']:<7} max_atom={r['max_atom']:<3} "
          f"TV9={fmt_frac(r['tv'], 24)} rec9={fmt_frac(r['rec'][0], 18)} "
          f"dual={r['dual']} max|h-h_full|={str(r['hdiff']):<4} "
          f"[{time.time() - _t:.1f}s]  {lab}")
_TK = time.time() - _t

TVs = {t: KRES[t]['tv'] for t in KRES}
MATCH = [t for t in TVs if TVs[t] == TV_COMMITTED]
BETTER = [t for t in TVs if TVs[t] < TV_COMMITTED]
WORSE = [t for t in TVs if TVs[t] > TV_COMMITTED]

check("G3-b **F2 DOES NOT FIRE: the quadratic promotion is CONSISTENT "
      "with the receipted law.**  The pin's F2 reads: a quadratic "
      "`K(E) = E^T N E` cannot match the committed `TV_9` for any `N`, "
      "including `N = diag(k,k,k)`.  Measured: `N = I` reproduces the "
      "committed `TV_9` exactly, as an equality of Fractions, and so do "
      "the Gram-derived forms.  Note for the record what `N = diag(k,k,k)` "
      "actually is — `E^T I E = sum_j E_j^2`, NOT `k.sum_j E_j` — so the "
      "pin's own identification of the two is loose; this receipt tests "
      "the literal quadratic and reports that it lands on the same number "
      "anyway",
      TVs['quad-I  '] == TV_COMMITTED and TVs['lin     '] == TV_COMMITTED
      and len(MATCH) >= 3,
      f"matching the committed TV_9 = {sorted(t.strip() for t in MATCH)}; "
      f"strictly worse = {sorted(t.strip() for t in WORSE)}; strictly "
      f"better = {sorted(t.strip() for t in BETTER)}")

CEIL = KRES['comp    ']['tv']
check("G3-c [MEASURED, NOT A THEOREM — MAJOR 4's REPAIR] NO CANDIDATE "
      "MOVES THE NUMBER ON THE FALSIFIED FIXTURE, AND THE FIRST "
      "DELIVERY'S REASON FOR IT WAS WRONG.  What was claimed: 'any `K` is "
      "a function of `E`, so its colouring coarsens the componentwise "
      "one, so `TV_9(any N) >= TV_9(comp) >= TV_9(full)` — the trace sits "
      "at the family's floor'.  **The second step assumes `TV_9` is "
      "MONOTONE under refinement of the colouring.  That was asserted in "
      "prose, never proved, and is not a general fact**: `forward_tv` is "
      "a nonlinear forward propagation through eight `forward_step`s "
      "built from RATIOS of atom-average weights, and this receipt's own "
      "committed table already shows the atom count does not order it "
      "(`agg_linf` has FEWER atoms than `agg_l1`, 66036 vs 66039, and a "
      "BETTER `TV_9`).  What is true and gated here is the empirical "
      "statement about a finite named list: the componentwise colouring "
      "and all eleven candidates land on the same value, and none came in "
      "below.  The EXACT mechanism is G3-g's h-weight identity, not a "
      "ceiling.  And by G1-f that value is not a floor at all — it is the "
      "rank-11 target's sector-selection residual",
      CEIL == TV_COMMITTED and not BETTER
      and all(TVs[t] >= CEIL for t in TVs)
      and MODE['agg_linf']['metrics'][9]['atoms']
      < MODE['agg_l1']['metrics'][9]['atoms']
      and MODE['agg_linf']['tv'] < MODE['agg_l1']['tv'],
      f"componentwise TV_9 = {fmt_frac(CEIL, 24)} == the falsified "
      f"fixture's committed value {fmt_frac(TV_COMMITTED, 24)}; candidates "
      f"strictly below = {len(BETTER)} of {len(TVs)}; MONOTONICITY "
      f"COUNTEREXAMPLE inside the committed table itself: agg_linf atoms "
      f"{MODE['agg_linf']['metrics'][9]['atoms']} < agg_l1 atoms "
      f"{MODE['agg_l1']['metrics'][9]['atoms']} yet agg_linf TV_9 "
      f"{fmt_frac(MODE['agg_linf']['tv'], 6)} < agg_l1 TV_9 "
      f"{fmt_frac(MODE['agg_l1']['tv'], 6)} — fewer atoms, better score")

DUALOK = [t for t in KRES if KRES[t]['dual'] == 0]
COARSE_OK = [t for t in KRES
             if all(v == 0 for v, _d in KRES[t]['coarse'])]
COARSE_H = [t for t in KRES
            if all(d == 0 for _v, d in KRES[t]['coarse'])]
check("G3-d THE PROMOTED `K` PRESERVES THE OTHER THREE COMMITTED GATES "
      "TOO — dual conjugation, the atom-average collapse, and the "
      "even-absolute compression.  For every candidate `N`: (i) the "
      "h-weight is EXACTLY invariant under order reversal, "
      "`max_R |h(R) - h(R*)| = 0` (paper 30's 'dual positive shadow is "
      "exactly invariant' gate); (ii) the colouring is a strict "
      "coarsening of `full` with ZERO fibre violations and ZERO h-weight "
      "difference at every N in the window (paper 30's Ramanujan exact "
      "atom identity); (iii) the promotion is non-lookup at N = 9.  All "
      "three hold for every candidate, so the promotion is admissible — "
      "it simply buys nothing",
      len(DUALOK) == len(KRES) and len(COARSE_OK) == len(KRES)
      and len(COARSE_H) == len(KRES)
      and not any(KRES[t]['lookup'] for t in KRES),
      f"dual-conjugation error 0 at {len(DUALOK)}/{len(KRES)} candidates; "
      f"coarsening-identity violations 0 at {len(COARSE_OK)}/{len(KRES)}; "
      f"max h-difference 0 at {len(COARSE_H)}/{len(KRES)}; lookup "
      f"colourings = {sum(1 for t in KRES if KRES[t]['lookup'])}")

# ---- what the trace DOES throw away, measured without TV ---------------
LIN_C = KRES['lin     ']['colors'][9]
LIN_ATOMS = len(set(LIN_C.values()))
SEP = {}
for tag in ('quad-I  ', 'quad-G  ', 'quad-D2 ', 'quad-OD1', 'comp    '):
    c = KRES[tag]['colors'][9]
    fwd, bwd = defaultdict(set), defaultdict(set)
    for k in RB[9]:
        fwd[c[k]].add(LIN_C[k])
        bwd[LIN_C[k]].add(c[k])
    refines = all(len(v) == 1 for v in fwd.values())
    coarsens = all(len(v) == 1 for v in bwd.values())
    SEP[tag] = (LIN_ATOMS, len(fwd), len(fwd) - LIN_ATOMS, refines, coarsens,
                sum(1 for v in bwd.values() if len(v) > 1))
REFINES = SEP['comp    '][3]
check("G3-e AT N = 9 THE TRACE IS LOSSY AS A COLOURING AND LOSSLESS AS A "
      "PREDICTOR — two SENSES OF 'LOSSLESS' DISAGREE THERE, which is a "
      "narrower statement than the first delivery's 'the pin's F1 is a "
      "biconditional and the two halves come apart' (retracted; see "
      "G3-e2).  The componentwise even "
      "colouring STRICTLY REFINES the trace's atom partition at N = 9 "
      "(gated: every componentwise atom sits inside one trace atom, and "
      "the atom count strictly rises — the trace really does merge "
      "records the vector separates), and every quadratic promotion but "
      "the singular `N = I + offdiag(1)` likewise raises it — yet not "
      "one of them moves `TV_9` by a single unit in the 24th digit.  So "
      "`E_total` is NOT an injective summary of the even channel — the "
      "corpus's `E_total` genuinely discards information — but everything "
      "it discards is predictively inert for the deletion-graph law at "
      "this window.  Both directions of the partition relation are "
      "reported: `refines` = every promoted atom sits inside one trace "
      "atom, `splits` = how many trace atoms the promotion breaks apart.  "
      "G3-e2 immediately below puts the size of this effect in "
      "proportion, and it is small",
      REFINES and SEP['comp    '][2] > 0 and SEP['quad-I  '][2] > 0
      and all(TVs[t] == TV_COMMITTED for t in ('quad-I  ', 'comp    ')),
      "; ".join(f"{t.strip()}: atoms {SEP[t][0]} -> {SEP[t][1]} "
                f"(+{SEP[t][2]}), refines={SEP[t][3]}, splits="
                f"{SEP[t][5]}" for t in SEP))

# MAJOR 3 — the refinement comparison across the DECLARED WINDOW, not at
# N = 9 alone.  F1's antecedent is TRUE at N = 5; the first delivery
# never tested the consequent there, which is the one place it could
# have been violated.
REFWIN = {n: (len(set(KRES['lin     ']['colors'][n].values())),
              len(set(KRES['comp    ']['colors'][n].values())))
          for n in WINDOW}
print("  THE REFINEMENT COMPARISON ACROSS THE WHOLE DECLARED WINDOW "
      "(MAJOR 3) — trace atoms vs componentwise atoms vs 'is the Gram "
      "diagonal?':")
for n in WINDOW:
    _t9, _c9 = REFWIN[n]
    print(f"    N={n}: trace atoms {_t9:<6} componentwise atoms {_c9:<6} "
          f"trace lossy as a colouring = {_c9 > _t9}  (+{_c9 - _t9}); "
          f"Gram nonzero off-diagonals {WIN[n]['nz']}/3, F1's antecedent "
          f"holds = {WIN[n]['nz'] == 0}")
LOSSY_FROM = min([n for n in WINDOW if REFWIN[n][1] > REFWIN[n][0]] or [0])
_EVALS = {tuple(even_functions[j](k) for j in range(3)) for k in RB[9]}
_TVALS = {sum(v) for v in _EVALS}
print(f"    and the disproportion, stated in full: at N = 9 the even "
      f"3-vector takes {len(_EVALS)} distinct values over the "
      f"{len(RB[9])} records and the trace collapses them onto "
      f"{len(_TVALS)} — destroying "
      f"{100 * (1 - len(_TVALS) / len(_EVALS)):.1f}% of the even "
      f"channel's distinctions — and the ATOM COUNT MOVES BY "
      f"{REFWIN[9][1] - REFWIN[9][0]}.  Essentially all the separating "
      f"is done by p30's `known` base coordinate, not by the even "
      f"channel.  'The trace genuinely discards information' is true of "
      f"the OBSERVABLE and very nearly false of the COLOURING.")
check("G3-e2 **F1'S IMPLICATION IS NOT VIOLATED ANYWHERE IN THE DECLARED "
      "WINDOW, AND THE UNIT'S 'BICONDITIONAL' CONVICTION IS RETRACTED** "
      "(MAJOR 3).  F1 as PINNED reads: *`G^even` is diagonal, or a "
      "multiple of the identity.  THEN `E_total` is lossless...* — an "
      "IMPLICATION, antecedent -> consequent, saying nothing whatever "
      "about what follows from a NON-diagonal Gram.  The first delivery "
      "attributed the CONVERSE to it, found the converse false, and "
      "reported F1 refuted; a pin frozen before the code is the one "
      "document a unit may not rewrite.  Measured here across the whole "
      "window instead of at N = 9 alone: F1's antecedent is TRUE at "
      "N = 5 (the Gram is exactly diag(1/20,1/30,1/30)) and THE "
      "CONSEQUENT HOLDS THERE TOO — the trace colouring is exactly as "
      "fine as the componentwise one at N = 5, 6 and 7; the colouring "
      "only becomes lossy at N = 8, one step AFTER the Gram's "
      "off-diagonal switches fully on at N = 7.  **A one-step lag "
      "between antecedent and consequent failing is the OPPOSITE of "
      "'the two halves come apart'.**  What the unit actually "
      "established is that F1's ANTECEDENT is N-dependent — a real "
      "finding — and that at N = 9 two senses of 'lossless' (as a "
      "colouring, as a predictor) disagree",
      REFWIN[5][0] == REFWIN[5][1] and REFWIN[6][0] == REFWIN[6][1]
      and REFWIN[7][0] == REFWIN[7][1] and LOSSY_FROM == 8
      and WIN[5]['nz'] == 0 and FIRST_FULL == 7,
      f"trace vs componentwise atoms by N = {REFWIN}; first N at which "
      f"the trace is lossy as a colouring = {LOSSY_FROM}; first N at "
      f"which all three off-diagonals are on = {FIRST_FULL}; F1's "
      f"antecedent holds at N = 5 and its consequent holds there too = "
      f"{REFWIN[5][0] == REFWIN[5][1]}; at N = 9 the even 3-vector's "
      f"distinctions are the thing lost, and the atom count moves by "
      f"{REFWIN[9][1] - REFWIN[9][0]} of {REFWIN[9][0]}")

# ---- MAJOR 4: eleven rows are TWO colourings ---------------------------
_KEYS9 = sorted(RB[9])


def partition_signature(colors9):
    """Canonical relabelling of a colouring's PARTITION: two colourings
    with different colour NAMES but the same blocks get the same
    signature.  (The colour tuples all carry the candidate's own tag, so
    naive equality can never see the collapse — which is why the first
    delivery reported eleven rows as eleven tests.)"""
    lab, out = {}, []
    for k in _KEYS9:
        c = colors9[k]
        if c not in lab:
            lab[c] = len(lab)
        out.append(lab[c])
    return tuple(out)


PART = {}
for tag in KRES:
    PART.setdefault(partition_signature(KRES[tag]['colors'][9]), []).append(tag)
PART_TV_OK = all(len({KRES[t]['tv'] for t in grp}) == 1
                 and len({KRES[t]['atoms'] for t in grp}) == 1
                 for grp in PART.values())
check("G3-h **THE ELEVEN CANDIDATES ARE NOT ELEVEN TESTS.  THEY ARE TWO "
      "COLOURINGS** (MAJOR 4).  Every `colors_for_K` colour is "
      "`(base, (fn(E), sum_j O_j^2))`, so every candidate's partition is "
      "a coarsening of `comp`'s partition `(base, (E, sum_j O_j^2))`; a "
      "coarsening has strictly fewer atoms unless it merges nothing, i.e. "
      "unless it EQUALS `comp`.  Computed directly here by canonical "
      "relabelling of the blocks rather than inferred: the eleven rows of "
      "identical twenty-digit strings collapse to TWO distinct partitions "
      "of the 131526 records — the componentwise one (`quad-I`, `quad-G`, "
      "`quad-adj`, `quad-cov`, `quad-D1`, `quad-D2`, `quad-OD2`, "
      "`bilin-G`, `comp`) and the trace's (`lin`, `quad-OD1`, the latter "
      "because `E^T J E = (sum E_j)^2` is a bijection of `sum E_j` on "
      "nonnegative integers).  **The table's visual weight overstates the "
      "evidence by a factor of five and a half, and this receipt says so "
      "in its own gate**",
      len(PART) == 2 and sorted(len(v) for v in PART.values()) == [2, 9]
      and PART_TV_OK and len(KRES) == 11,
      "; ".join(f"partition {i + 1} ({len(g)} rows, atoms "
                f"{KRES[g[0]]['atoms']}): {sorted(t.strip() for t in g)}"
                for i, g in enumerate(PART.values()))
      + f"  -> {len(PART)} distinct colourings among {len(KRES)} rows; "
      f"TV_9 and atom count constant within each = {PART_TV_OK}")

# ---- MAJOR 4: the h-weight identity is the mechanism -------------------
print("  h-IDENTITY CONTROLS on the falsified fixture — functions of the "
      "even 3-vector that BREAK `h == h_full`:")
ADV = [('adv-E3  ', 'K(E) = E_3 only  (drops two channels)',
        lambda E: E[2]),
       ('adv-mod2', 'K(E) = (sum_j E_j) mod 2  (a non-monotone quotient)',
        lambda E: sum(E) % 2)]
_t = time.time()
for tag, lab, fn in ADV:
    KRES[tag] = run_K('d73_' + tag.strip(), fn, lab)
    r = KRES[tag]
    print(f"    {tag} atoms9={r['atoms']:<7} TV9={fmt_frac(r['tv'], 24)} "
          f"ratio={float(r['tv'] / TV_COMMITTED):.3f}x "
          f"max|h-h_full|={str(r['hdiff']):<4} [{time.time() - _t:.1f}s]  "
          f"{lab}")
_TADV = time.time() - _t

# ---- THE BLOCKER's REPAIR: G3 re-posed on the SELECTED fixture ---------
print("  ON THE SELECTED §27 FIXTURE (G1-g) — where the floor is 0 and "
      "the question can have an answer:")
G_SELq = tuple(tuple(G_SEL[i][j] for j in range(3)) for i in range(3))
SELCAND = [
    ('sel-lin  ', 'K = k.E_total  [the trace, on the selected triple]', sum),
    ('sel-comp ', 'THE CEILING: componentwise (E_1, E_2, E_3)',
     lambda E: E),
    ('sel-quadG', 'N = G^even(SELECTED) itself (G2-i, exact rationals)',
     qform(G_SELq)),
    ('sel-E3   ', 'K(E) = E_3 only  [h-identity control]', lambda E: E[2]),
    ('sel-mod2 ', 'K(E) = (sum_j E_j) mod 2  [h-identity control]',
     lambda E: sum(E) % 2),
]
SRES = {}
_t = time.time()
for tag, lab, fn in SELCAND:
    SRES[tag] = run_K('d73_' + tag.strip(), fn, lab, pairs=SELECTED,
                      ref=SEL['full'])
    r = SRES[tag]
    print(f"    {tag} atoms9={r['atoms']:<7} TV9={fmt_frac(r['tv'], 24)} "
          f"max|h-h_full|={str(r['hdiff']):<4} dual={r['dual']}  "
          f"[{time.time() - _t:.1f}s]  {lab}")
_TSK = time.time() - _t

SEL_FLOOR_OK = (SRES['sel-lin  ']['tv'] == 0 and SRES['sel-comp ']['tv'] == 0
                and SRES['sel-quadG']['tv'] == 0)
SEL_MOVERS = [t for t in SRES if SRES[t]['tv'] > 0]
check("G3-f **THE PROMOTED-K QUESTION WAS FIXTURE-DEAD AT THE OLD ANCHOR, "
      "AND IS RE-POSED HERE ON THE ONE PAPER 30 SELECTED (the BLOCKER's "
      "repair).**  At the falsified anchor the residual `1.676e-5` is a "
      "SECTOR-SELECTION artefact (G1-f): it is the error the full "
      "componentwise colouring of THOSE three pairs cannot remove, and no "
      "function whatever of the even 3-vector can touch an error that "
      "lives in the choice of which flags to look at.  So G3's 'nothing "
      "moved' was GUARANTEED BY THE FIXTURE, not discovered about the "
      "even channel.  Re-posed on §27's selected triple, where "
      "`TV_9(full) = 0` exactly: the trace, the componentwise ceiling and "
      "the selected fixture's OWN Gram as `N` all score EXACTLY ZERO — so "
      "the promotion still buys nothing, but now for a completely "
      "different and honest reason (there is nothing left to buy) — while "
      "the two h-identity controls DO move the number off zero.  **On "
      "this fixture the instrument is live: a wrong `K` is visibly "
      "punished, and the trace's optimality is a measurement rather than "
      "a fixture artefact**",
      SEL_FLOOR_OK and len(SEL_MOVERS) == 2
      and all(SRES[t]['tv'] > 0 for t in SEL_MOVERS)
      and SRES['sel-lin  ']['dual'] == 0,
      f"selected-fixture TV_9: trace = {fmt_frac(SRES['sel-lin  ']['tv'], 6)}, "
      f"comp = {fmt_frac(SRES['sel-comp ']['tv'], 6)}, quad-G = "
      f"{fmt_frac(SRES['sel-quadG']['tv'], 6)} (all exactly zero = "
      f"{SEL_FLOOR_OK}); the controls that move it = "
      f"{sorted(t.strip() for t in SEL_MOVERS)} at "
      f"{[fmt_frac(SRES[t]['tv'], 12) for t in sorted(SEL_MOVERS)]}; atoms9 "
      f"{ {t.strip(): SRES[t]['atoms'] for t in SRES} }")

_ALL = [(t, KRES[t]['hdiff'], KRES[t]['tv'] == TV_COMMITTED) for t in KRES]
_ALL += [(t, SRES[t]['hdiff'], SRES[t]['tv'] == TV_SELECTED) for t in SRES]
HID_MATCH = [t for t, h, m in _ALL if h == 0 and m]
HID_MOVE = [t for t, h, m in _ALL if h != 0 and not m]
HID_BROKEN = [t for t, h, m in _ALL if (h == 0) != m]
check("G3-g **THE MECHANISM, EXACT AND GATED: THE h-WEIGHT IDENTITY — "
      "NOT A MONOTONICITY LEMMA** (MAJOR 4).  `forward_tv` depends on a "
      "colouring ONLY through its atom-average weight function `h`.  So "
      "if a candidate's `h` is identical to `full`'s at every record, its "
      "`forward_tv` is identical BY CONSTRUCTION, in one line, with no "
      "assumption about partition order — and that, not any ceiling, is "
      "why candidates agree to the twentieth decimal.  It is paper 30's "
      "own §25.5 exact atom identity restated, and the receipt's own "
      "G3-d already measured it (`max h-difference 0 at 11/11`) without "
      "noticing what it was.  Gated across BOTH fixtures and all "
      "candidates run here: `max_R |h(R) - h_full(R)| = 0` if and only if "
      "the candidate lands exactly on that fixture's baseline `TV_9`.  "
      "The two h-identity-breaking controls on each fixture are the "
      "non-vacuity half — they show the equivalence is not an artefact of "
      "everything scoring the same",
      len(HID_BROKEN) == 0 and len(HID_MATCH) >= 12
      and len(HID_MOVE) == 4
      and KRES['adv-E3  ']['hdiff'] != 0 and KRES['adv-mod2']['hdiff'] != 0,
      f"candidates over the two fixtures = {len(_ALL)}; h-identity AND on "
      f"the baseline = {len(HID_MATCH)}; h-identity BROKEN AND off the "
      f"baseline = {len(HID_MOVE)} "
      f"({sorted(t.strip() for t in HID_MOVE)}); mismatches = "
      f"{len(HID_BROKEN)}; falsified-fixture controls: adv-E3 h-diff "
      f"{KRES['adv-E3  ']['hdiff']} costs "
      f"{float(KRES['adv-E3  ']['tv'] / TV_COMMITTED):.3f}x, adv-mod2 "
      f"h-diff {KRES['adv-mod2']['hdiff']} costs "
      f"{float(KRES['adv-mod2']['tv'] / TV_COMMITTED):.3f}x")

outcome("G3 / F2",
        "**F2 DOES NOT FIRE — AND THE POSITIVE BRANCH WAS ASKED AT A "
        "FIXTURE WHERE IT COULD NOT FIRE.**  The quadratic promotion is "
        f"admissible on all four committed gates ({len(DUALOK)}/11 of the "
        f"pin's candidates clean on dual conjugation, the atom identity "
        f"and non-lookup) and reproduces the falsified fixture's TV_9 = "
        f"{fmt_frac(TV_COMMITTED, 12)} exactly.  THREE CORRECTIONS THE "
        f"ROUND FORCED.  (1) That number is the RANK-11 LOSER's score "
        f"(G1-f), and the residual it names is a sector-selection "
        f"artefact unreachable by any function of the even 3-vector — so "
        f"'nothing moved' was fixture-guaranteed.  On §27's SELECTED "
        f"triple the floor is 0 exactly, the trace/comp/Gram candidates "
        f"all attain it, and h-identity-breaking controls are visibly "
        f"punished (G3-f).  (2) The mechanism is the h-WEIGHT IDENTITY, "
        f"gated across both fixtures at {len(_ALL)} candidates with zero "
        f"mismatches (G3-g) — NOT the unproved monotonicity lemma the "
        f"first delivery argued from, and this receipt exhibits a "
        f"counterexample to that lemma's premise inside the committed "
        f"table (G3-c).  (3) The eleven rows are TWO colourings (G3-h).  "
        f"**What survives, on both fixtures: the even channel is "
        f"PREDICTIVELY trace-only while being STRUCTURALLY anisotropic — "
        f"and on the selected fixture that is now a measurement.**")

# ======================================================================
# G4 — THE FAILS-FULL-GR ANSWER.  Response or rebadged scalar?
# ======================================================================
print(f"\n{sec()} [G4 — THE FAILS-FULL-GR ANSWER: is a Gram-derived N a "
      f"metric RESPONSE, or a rebadged scalar family?]")

# (i) locality: the per-record object.  MINOR 1 — the first delivery
# populated this census by writing the answer into the key and then
# maxed over the keys, a predicate that could not fail.  Here the 2x2
# minors of the actual per-record matrix are computed.
LOCAL_RANK = defaultdict(int)
ZEROV = 0
MINOR_VIOL = 0
for k in RB[9]:
    v = tuple(even_functions[j](k) for j in range(3))
    M2 = [[v[a] * v[b] for b in range(3)] for a in range(3)]
    if any(M2[a][a] * M2[b][b] - M2[a][b] * M2[b][a] != 0
           for a, b in combinations(range(3), 2)):
        MINOR_VIOL += 1
    if all(x == 0 for x in v):
        ZEROV += 1
        LOCAL_RANK[0] += 1
    else:
        LOCAL_RANK[1] += 1
check("G4-a **THE LOCAL OBJECT IS RANK 1, NOT RANK 2 — AND THIS IS A "
      "TRIVIALITY, LABELLED AS ONE** (MINOR 1).  Because the reflection "
      "acts trivially on the even channel (G2-c), the per-record summand "
      "of the Gram is `E_j(R) E_k(R*) = E_j(R) E_k(R)` — the OUTER "
      "PRODUCT of one vector with itself.  **`v v^T` has rank <= 1 for "
      "every vector `v` whatever, so this is true of every second-moment "
      "matrix ever written down and it is NOT an independent failure "
      "mode; §6's presentation of it as a third one gave a triviality "
      "the weight of a finding.**  What is measured rather than "
      "definitional: all three `2x2` minors of the per-record matrix "
      "vanish at every one of the 131526 records (computed, not assumed "
      "from the census key), and 3862 records carry `E(R) = 0` outright.  "
      "The content of the row is only this: rank 3 appears ONLY after "
      "averaging.  A metric is a form AT A POINT; this form exists only "
      "in the ensemble",
      LOCAL_RANK[1] > 0 and MINOR_VIOL == 0
      and LOCAL_RANK[1] + LOCAL_RANK[0] == len(RB[9])
      and ZEROV == LOCAL_RANK[0],
      f"records whose per-record matrix has a nonvanishing 2x2 minor = "
      f"{MINOR_VIOL} of {len(RB[9])} (MEASURED — the only substantive "
      f"number in this gate, together with the {ZEROV} records at "
      f"E(R) = 0); census by |E(R)| = {dict(LOCAL_RANK)}; ensemble rank = "
      f"3 (G2-d)")

# (ii) equivariance: what acts on the channel index?
STAB = []
for p in permutations(range(3)):
    if all(G_EVEN[p[i]][p[j]] == G_EVEN[i][j]
           for i in range(3) for j in range(3)):
        STAB.append(p)
MEANS = [MU[j] for j in range(3)]
VARS = [COV[j][j] for j in range(3)]
DUAL_ACTS_TRIVIALLY = (EV_VIOL == 0)
MINE = [min(even_functions[j](k) for k in RB[9]) for j in range(3)]
MAXE = [max(even_functions[j](k) for k in RB[9]) for j in range(3)]

check("G4-b **THE CHANNEL INDEX CARRIES NO SYMMETRY, SO `N` IS NOT "
      "EQUIVARIANT — IT IS A GAUGE-FIXED TABLE.**  A metric response must "
      "transform: `N -> A N A^T` under whatever acts on the index it "
      "carries.  Three gates, and all three come back empty.  (i) The "
      "substrate's one available involution — paper 30's order-dual `*`, "
      "the same Z/2 as Prop 10.6's and `chi^NN`'s — acts TRIVIALLY on the "
      "even index (G2-c: zero parity violations in 394578 tests); it acts "
      "as a SIGN on the odd index.  (ii) The only other candidate is "
      "relabelling the three dual pairs, and the stabiliser of `G^even` "
      "in S_3 is the IDENTITY ALONE — the three channels have distinct "
      "means and distinct variances, so no nontrivial permutation is even "
      "a numerical symmetry, let alone a substrate one.  (iii) There is "
      "no sign freedom at all: every `E_j` is a nonnegative count, so the "
      "basis is canonically oriented and no analogue of Prop 10.6's "
      "frame flip `E_A^2 -> -E_A^2` exists on this index.  REPORTED "
      "AGAINST THE UNIT'S OWN INTEREST: channels 2 and 3 have EQUAL "
      "means (21/5 each) — a near-symmetry — and the second moment "
      "breaks it anyway, `G_22 != G_33`, so the stabiliser is still "
      "trivial.  A form whose only would-be symmetry is broken by its "
      "own entries is a table of numbers, not a tensor",
      len(STAB) == 1 and STAB[0] == (0, 1, 2)
      and len(set(VARS)) == 3 and G_EVEN[1][1] != G_EVEN[2][2]
      and DUAL_ACTS_TRIVIALLY and all(m >= 0 for m in MINE)
      and all(m > 0 for m in MAXE),
      f"S_3 stabiliser of G = {STAB} (order {len(STAB)}); channel means "
      f"{[dfl(m, 10) for m in MEANS]} (distinct = {len(set(MEANS)) == 3} "
      f"— channels 2 and 3 coincide); channel variances "
      f"{[dfl(v, 10) for v in VARS]} (distinct = {len(set(VARS)) == 3}); "
      f"order-dual acts trivially on E = {DUAL_ACTS_TRIVIALLY}; min/max "
      f"E_j over records = {list(zip(MINE, MAXE))}")

# (iii) the component count, in v6 p4's own units
R9 = len(RB[9])
GLOBAL_COMPONENTS = 6            # symmetric 3x3
PER_RECORD_NEEDED = 6 * R9       # one symmetric 3x3 response per record
DEFICIT = PER_RECORD_NEEDED - GLOBAL_COMPONENTS
SCALAR_COMPONENTS = 1
check("G4-c **THE FAILS-FULL-GR ROW IS ANSWERED, AND THE ANSWER IS: "
      "HALF-CLEARED, STILL FAILING, AND FOR A SHARPER REASON.**  v6 paper "
      "4 `:1064` rejected the scalar-to-tensor shortcut on a COMPONENT "
      "COUNT: 'a scalar potential equation has ONE response component per "
      "screen atom; a two-dimensional symmetric tensor equation has THREE "
      "per atom' (`missing_components = 8193`, verdict FAILS-FULL-GR).  "
      "The even Gram clears the first half of that objection — it "
      "supplies 6 independent components where `K(E) = k.E_total` "
      "supplied 1 — and fails the second half completely: those 6 "
      "components are ONE GLOBAL FORM for the entire N = 9 window, "
      "whereas p4's row counts components PER ATOM.  And G4-a says the "
      "per-atom object, when you do write it down, is rank 1.  So a "
      "Gram-derived `N` is NOT a metric response: it is an ensemble "
      "summary statistic with a metric's index shape.  **THE UNITS, "
      "CORRECTED (MODERATE 4).  `789150` IS NOT 'IN p4's OWN UNITS' AND "
      "MUST NOT BE QUOTED AS ONE.**  v6 p4's `missing_components = 8193` "
      "counts components on a 2-DIMENSIONAL SCREEN (3 per screen atom "
      "against a scalar's 1) at that paper's own grid resolution; D73's "
      "`6` is `dim Sym^2(R^3)` on an index of THREE NAMED 5-ELEMENT "
      "RECORD TYPES, and `131526` counts record classes.  The index has "
      "no dimension in the geometric sense, the atoms are not screen "
      "atoms, and the two numbers are NOT COMMENSURABLE.  `6 x 131526 - "
      "6` is arithmetic on D73's record count under p4's COUNTING RULE — "
      "that, and only that, is what the number below is.  p4's own "
      "receipt is absent from the tree and `8193` was not recomputed: "
      "[STATED, not verified], and the qualification travels with the "
      "number",
      GLOBAL_COMPONENTS > SCALAR_COMPONENTS and DEFICIT > 0
      and R9 == 131526 and MINOR_VIOL == 0,
      f"components supplied by K(E) = k.E_total: {SCALAR_COMPONENTS}; by "
      f"G^even: {GLOBAL_COMPONENTS}; needed for a per-record symmetric "
      f"response: {PER_RECORD_NEEDED} over {R9} records; deficit = "
      f"{DEFICIT} [p4's COUNTING RULE applied to D73's record count — NOT "
      f"p4's units, NOT commensurable with p4's 8193, which was not "
      f"recomputed]; per-record rank of the Gram's own summand = 1 "
      f"(measured: {MINOR_VIOL} of {R9} records carry a nonvanishing 2x2 "
      f"minor)")

# (iv) the Prop 10.6 relation, stated where it can be tested
ODD_MU = tuple(sum(P9[k] * odd_functions[j](k) for k in RB[9])
               for j in range(3))
ODD_OFF = [G_ODD[i][j] for i, j in combinations(range(3), 2)]
ORIENT_EVEN = all(even_functions[j](k) == even_functions[j](dual_key(k, 9))
                  for j in range(3) for k in list(RB[9])[:2000])
ORIENT_ODD_NONTRIVIAL = any(odd_functions[j](k) != 0
                            for j in range(3) for k in RB[9])
check("G4-d **THE PROP-10.6 RELATION, STATED CAREFULLY — THESE ARE "
      "DIFFERENT OBJECTS AND THE UNIT REFUSES TO CONFLATE THEM.**  v2 "
      "paper 10 Prop 10.6 is an ALL-ORDER no-go: the SIGNED off-diagonal "
      "`h^{12}` of a frame metric cannot be recovered from Gamma-level "
      "(endpoint-probability) data, because the staggered conjugation "
      "`S_2` flips `h^{12}` while leaving every Born-squared kernel "
      "invariant.  `G^even_{12} != 0` is NOT a counterexample and must "
      "never be cited as one.  Reason, gated here: `G^even` is itself "
      "built FROM the endpoint measure `P(R)`, so by Prop 10.6's own "
      "argument it is invariant under any representational sign flip; "
      "its off-diagonal is nonzero not because the shadow recovered an "
      "orientation but because the channel basis is CANONICALLY ORIENTED "
      "by counting (G4-b(iii)), which is precisely the freedom Prop 10.6's "
      "frames have and these observables do not.  What the two statements "
      "DO share is located exactly: the orientation datum lives in the "
      "ODD sector here too — the even Gram is blind to the order-dual and "
      "the odd Gram changes sign under it — so paper 30's channel split "
      "reproduces Prop 10.6's diagonal/off-diagonal split ONE LEVEL DOWN, "
      "as an even/odd split, with the sign carried by the odd channel and "
      "the anisotropy by the even one",
      ORIENT_EVEN and ORIENT_ODD_NONTRIVIAL and OD_VIOL == 0
      and all(v != 0 for v in ODD_OFF) and EV_VIOL == 0,
      f"even channel dual-invariant (2000-record spot check + the "
      f"exhaustive G2-c count {EV_VIOL} violations); odd channel "
      f"dual-antiinvariant, {OD_VIOL} violations; odd Gram "
      f"off-diagonals {[dfl(v, 12) for v in ODD_OFF]}; odd channel means "
      f"{[dfl(m, 12) for m in ODD_MU]}")

outcome("G4", "A Gram-derived `N` is a METRIC-SHAPED ENSEMBLE STATISTIC, "
              "not a metric response.  It clears v6 p4's component-count "
              "objection at the global level (6 components, not 1) and "
              "fails it at the level p4 actually stated it (per atom), "
              "and it fails two further tests p4 never needed: the "
              "per-record object is rank 1, and NOTHING acts on the "
              "channel index — the S_3 stabiliser is trivial, the "
              "substrate's own Z/2 acts as the identity on the even "
              "index, and the counting basis admits no sign freedom.  "
              "**A scalar did not become a metric by interpretation.  It "
              "became a covariance matrix, which is a different thing.**")

# ======================================================================
# G5 — TRANSFER PROBE.  [SAMPLED] / context grade, single blueprint.
# ======================================================================
print(f"\n{sec()} [G5 — TRANSFER PROBE [SAMPLED]: the Gram machinery on "
      f"ONE v10 object — a wide-crystal chart's direction set with its "
      f"weights.  Context grade; nothing above depends on it]")

G5_OK = False
G5_NOTE = ""
try:
    V10 = os.path.join(ISP, 'v10', 'code')
    _s42 = open(os.path.join(V10, 'd42b1_transport_exact.py')).read()
    _sl = _s42[:_s42.index('print("[d42b1')]
    n42 = {}
    exec(compile(_sl, 'd42b1_slice', 'exec'), n42)
    cf, ep, V0 = n42['candidates_for'], n42['event_poset'], n42['V0']
    g47, _k47 = _ext(os.path.join(V10, 'd47a_sky_instrument_exact.py'),
                     'd47a', ('CYCLIC_CAP', 'SKYB_DEPTH'))
    sky, heights = g47['sky'], g47['heights']
    g58, _k58 = _ext(os.path.join(V10, 'd58_atlas_instrument_exact.py'),
                     'd58', (), extra={'sky': sky, 'heights': heights})
    d58_covers = g58['covers']
    g60, _k60 = _ext(os.path.join(V10, 'd60_crystal_exact.py'), 'd60', (),
                     extra={'sky': sky, 'heights': heights,
                            'd58_covers': d58_covers, 'candidates_for': cf,
                            'event_poset': ep, 'V0': V0})
    g63, _k63 = _ext(os.path.join(V10, 'd63_wide_crystal_exact.py'), 'd63',
                     ('CADENCE', 'FULLMENU_BUDGET', 'BUILT', '_EXTRACTED'),
                     extra={'sky': sky, 'heights': heights,
                            'd58_covers': d58_covers, 'candidates_for': cf,
                            'event_poset': ep, 'V0': V0,
                            'B': g60['B'], 'brick': g60['brick'],
                            'mint_and_spread': g60['mint_and_spread'],
                            'dl': g60['dl'], 'profile': g60['profile'],
                            'poset_of': g60['poset_of'],
                            'CADENCE': 1, 'BUILT': {}})
    def chart_grams(C, depth=2, wide=4):
        """For every event whose SKY-B chart has >= `wide` directions:
        the direction-Gram `Gamma_{dd'} = sum_rows w(row) 1[d in row]
        1[d' in row]`, uniform `w`.  The chart's own shadow rows are the
        weights the atlas already carries.  **NOT THE SAME TREATMENT THE
        EVEN CHANNEL GOT (MODERATE 1), and the difference is stated
        rather than glossed:** v7's object is `sum_R P(R) E_j(R) E_k(R*)`
        — a second moment of integer COUNTS, under the ORDER-DUAL
        REFLECTION, against the pushforward of the uniform permutation
        measure.  This object is a co-occurrence of 0/1 INDICATORS, with
        NO REFLECTION AT ALL, against a uniform measure on shadow rows.
        Three of the four ingredients differ and the missing one is the
        reflection — the entire subject of p30 §25.4 and of this unit's
        own G2-c.  It is a second-moment matrix, so its PSD-ness is the
        same tautology G2-c deflates on the v7 side; that deflation
        applies here verbatim."""
        out = []
        for e in range(len(C)):
            dirs, rows = sky(C, e, 'B', depth)
            dirs = sorted(set(dirs))
            if len(dirs) < wide or not rows:
                continue
            m = len(dirs)
            w = Fr(1, len(rows))
            M = [[sum(w for r in rows if dirs[i] in r and dirs[j] in r)
                  for j in range(m)] for i in range(m)]
            off = [M[i][j] for i in range(m) for j in range(i + 1, m)]
            dg = [M[i][i] for i in range(m)]
            out.append((e, m, M, off, dg))
        return out

    def census(CG):
        """distinct matrices, stabiliser histogram, identity-proportional
        count, constant-diagonal count."""
        dist, hist, idp, flat = set(), defaultdict(int), 0, 0
        for _e, m, M, off, dg in CG:
            dist.add(tuple(tuple(r) for r in M))
            s = sum(1 for p in permutations(range(m))
                    if all(M[p[i]][p[j]] == M[i][j]
                           for i in range(m) for j in range(m)))
            hist[(m, s)] += 1
            flat += int(len(set(dg)) == 1)
            idp += int(all(v == 0 for v in off) and len(set(dg)) == 1)
        return dist, dict(hist), idp, flat

    # ---- MAJOR 2: the sweep that costs seconds, and that the false
    # ---- uniqueness claim suppressed.
    BLUEPRINTS = [
        ('DOUBLE-RING(8,10,8) [D63 winner]',
         lambda: g63['double_ring'](8, 10, 8), 4),
        ('DOUBLE-RING(6,14,6)', lambda: g63['double_ring'](6, 14, 6), 4),
        ('DOUBLE-RING(4,26,4)', lambda: g63['double_ring'](4, 26, 4), 4),
        ('DOUBLE-RING(4,10,4)', lambda: g63['double_ring'](4, 10, 4), 4),
        ('DOUBLE-RING(8,10,2)', lambda: g63['double_ring'](8, 10, 2), 4),
        ('wide_brick(8,14,2)', lambda: g63['wide_brick'](8, 14, 2), 4),
        ('brick(8,14) [NARROW CONTROL, |D| >= 3]',
         lambda: g60['brick'](8, 14), 3),
    ]
    _t = time.time()
    SWEEP = {}
    print("    THE BLUEPRINT SWEEP (MAJOR 2 — each build costs about a "
          "second, and the first delivery ran one):")
    for _name, _fn, _wide in BLUEPRINTS:
        _b = _fn()
        _C = g60['poset_of'](_b.H)
        _CG = chart_grams(_C, 2, _wide)
        _d, _h, _idp, _fl = census(_CG)
        SWEEP[_name] = {'events': len(_C), 'charts': len(_CG), 'CG': _CG,
                        'C': _C, 'distinct': len(_d), 'hist': _h,
                        'idprop': _idp, 'flat': _fl}
        print(f"      {_name:<40} events={len(_C):<4} charts="
              f"{len(_CG):<4} DISTINCT MATRICES={len(_d):<3} stabiliser "
              f"census={_h} identity-proportional={_idp}")
    _TSWEEP = time.time() - _t

    WINNER = SWEEP['DOUBLE-RING(8,10,8) [D63 winner]']
    NAR = SWEEP['brick(8,14) [NARROW CONTROL, |D| >= 3]']
    Cw, Cn, CGw, CGn = WINNER['C'], NAR['C'], WINNER['CG'], NAR['CG']
    aniso_w = [c for c in CGw
               if any(v != 0 for v in c[3]) or len(set(c[4])) > 1]
    stab_hist, flatdiag = WINNER['hist'], WINNER['flat']
    NONTRIV = sum(v for (m, s), v in stab_hist.items() if s > 1)
    RINGS = [k for k in SWEEP if k.startswith('DOUBLE-RING')]
    RING_ALL8 = all(set(SWEEP[k]['hist']) == {(4, 8)} for k in RINGS)
    BRICK_BREAKS = SWEEP['wide_brick(8,14,2)']['hist']

    # ---- (a) the winner's 59 charts are TWO matrices, with their spectra.
    _cnt = defaultdict(int)
    for _e, _m, M, _o, _d in CGw:
        _cnt[tuple(tuple(r) for r in M)] += 1
    TWO = sorted(_cnt.items(), key=lambda kv: -kv[1])
    print(f"    THE 59 'ANISOTROPIC DIRECTION GRAMS' ARE "
          f"{len(TWO)} MATRICES:")
    SPEC, BLOCKY = [], []
    for M, k in TWO:
        four = (len(M) == 4)
        a, b, c, d = (M[0] if four else (0, 0, 0, 0))
        circ = four and b == d and all(
            M[i][j] == M[0][(j - i) % 4] for i in range(4) for j in range(4))
        # exact spectrum of a SYMMETRIC circulant (a, b, c, b):
        ev = ([a + 2 * b + c, a - c, a - c, a - 2 * b + c] if circ else [])
        # certified, not asserted: the characteristic polynomial vanishes
        # at each claimed eigenvalue, as an exact Fraction identity.
        ev_ok = circ and all(
            all(sum((M[i][j] - (lam if i == j else 0)) * x[j]
                    for j in range(4)) == 0 for i in range(4))
            for lam, x in ((ev[0], (1, 1, 1, 1)), (ev[3], (1, -1, 1, -1)),
                           (ev[1], (1, 0, -1, 0)), (ev[2], (0, 1, 0, -1))))
        zero_blocks = four and (M[0][1] == 0 and M[0][3] == 0
                                and M[2][1] == 0 and M[2][3] == 0)
        SPEC.append((k, M[0], circ, ev, zero_blocks, ev_ok))
        BLOCKY.append(zero_blocks)
        print(f"      on {k} charts, first row {[str(v) for v in M[0]]}, "
              f"symmetric-circulant in sorted order = {circ}, eigenvalues "
              f"{[str(v) for v in ev]} ({len(set(ev))} distinct, certified "
              f"by exact eigenvectors = {ev_ok}), block-decomposable = "
              f"{zero_blocks}")
        for i in range(4):
            print("        [ " + "  ".join(f"{str(M[i][j]):>6}"
                                           for j in range(4)) + " ]")
    SPEC_OK = all(s[5] for s in SPEC)
    DEGEN = [len(set(ev)) for _k, _r, _c, ev, _z, _o in SPEC]

    # ---- (b) the narrow control, MEASURED (MODERATE 2).
    _q = Fr(1, 4)
    NAR_EYE = [c for c in CGn
               if all(v == 0 for v in c[3]) and set(c[4]) == {_q}]
    NAR_MAXSYM = [c for c in CGn
                  if len(set(c[4])) == 1 and len(set(c[3])) == 1
                  and c[3] and c[3][0] != 0]
    NAR_MAXSTAB = sum(v for (m, s), v in NAR['hist'].items() if s == 6)
    print(f"    THE NARROW CONTROL, MEASURED (the first delivery reported "
          f"only its chart count): {len(CGn)} charts at |D| = 3 — the "
          f"same index size as v7's three channels — of which "
          f"{len(NAR_EYE)} have a direction Gram EXACTLY (1/4).I "
          f"(**F1's literal condition, a multiple of the identity, "
          f"FIRING ON THE v10 SIDE**), {len(NAR_MAXSYM)} are the "
          f"maximally symmetric (1/4)I + (1/4)J, and {NAR_MAXSTAB} of "
          f"{len(CGn)} carry the FULL S_3 stabiliser of order 6.")

    G5_OK = True
    G5_NOTE = (f"{len(CGw)} wide charts on the winner but only "
               f"{WINNER['distinct']} DISTINCT matrices ({'+'.join(str(k) for _M, k in TWO)}), "
               f"eigenvalue multiplicities {DEGEN} (v7's three are "
               f"distinct), stabiliser census {stab_hist}, "
               f"identity-proportional {WINNER['idprop']}; every DOUBLE-RING "
               f"blueprint is 100% stabiliser-8 and 2 matrices; "
               f"wide_brick(8,14,2) breaks uniformity at {BRICK_BREAKS}; "
               f"narrow control {len(CGn)} charts with {len(NAR_EYE)} "
               f"EXACTLY (1/4)I — F1 firing on the v10 side")
    check("G5 [SAMPLED / CONTEXT GRADE — SEVEN BLUEPRINTS, ONE DEPTH] "
          "**THE TRANSFER PROBE'S HINT INVERTS ON ITS OWN EVIDENCE.  THE "
          "DIRECTION INDEX IS NOT A BETTER STAGE THAN v7's CHANNEL "
          "INDEX; AS MEASURED IT IS A WORSE ONE.**  Round 1 broke the "
          "first delivery's reading three ways and this gate carries all "
          "three.  (a) IT IS NOT A FIELD, IT IS A CONSTANT: the winner's "
          "59 wide charts carry exactly TWO distinct matrices (51 + 8) — "
          "a metric response is an object that VARIES over its base, and "
          "this one takes two values on a 177-event crystal.  (b) A "
          "LARGE STABILISER IS LESS METRIC DATA, NOT MORE, AND THIS "
          "RECEIPT'S OWN NEGATIVE CONTROL SAYS SO: G6-c offers `7I`, "
          "whose S_3 stabiliser is the FULL group of order 6, as the "
          "demonstration that the F1 instrument fires when F1 is TRUE.  "
          "A bigger stabiliser means a MORE constrained form: with a "
          "trivial stabiliser v7's Gram is a generic point of the "
          "6-dimensional Sym^2(R^3), whereas a D_4-invariant 4x4 "
          "symmetric form is confined to the 3-dimensional span "
          "{I, adjacent, opposite} inside the 10-dimensional "
          "Sym^2(R^4) — which is exactly the observed (3/8, 1/8, 1/4) "
          "shape.  **The direction Gram has FEWER free components than "
          "the channel Gram.**  (c) THE SPECTRA ARE DEGENERATE: matrix A "
          "(51 charts) has eigenvalues 7/8, 3/8, 1/8, 1/8 — a repeated "
          "root — and matrix B (8 charts) has only TWO distinct "
          "eigenvalues 3/7, 3/7, 1/7, 1/7 and is BLOCK-DECOMPOSABLE, its "
          "four directions splitting into two mutually invisible pairs: "
          "a direct sum of two 2x2 blocks wearing a 4x4 index.  Against "
          "v7's three DISTINCT eigenvalues the v10 forms are the more "
          "degenerate objects.  And the uniformity is HAND-BUILT, not "
          "substrate: every DOUBLE-RING blueprint gives 100% "
          "stabiliser-8 and exactly two matrices because a double ring "
          "is constructed with cyclic symmetry and the direction index "
          "inherits it, while the first non-ring wide record, "
          "wide_brick(8,14,2), breaks it at 5 of 12 charts.  The narrow "
          "control — never measured in the first delivery — has FOUR "
          "charts whose direction Gram is exactly (1/4)I, F1's literal "
          "condition firing on the v10 side, and 38 of 42 at the MAXIMAL "
          "stabiliser.  MINOR 5: 'circulant' holds in the CANONICAL "
          "SORTED direction order only and is not an invariant; the "
          "stabiliser order (and the isomorphism type D_4) is",
          G5_OK and len(CGw) > 0 and len(aniso_w) > 0
          and len(Cw) == 177 and len(Cn) == 65
          and WINNER['distinct'] == 2 and len(TWO) == 2
          and RING_ALL8 and set(BRICK_BREAKS) != {(4, 8)}
          and len(NAR_EYE) > 0 and max(DEGEN) < 4 and SPEC_OK,
          f"DOUBLE-RING(8,10,8) = {len(Cw)} events (D63 published 177); "
          f"brick(8,14) = {len(Cn)} events (D60/D63 published 65); "
          f"{G5_NOTE}; every ring blueprint 100% stabiliser-8 = "
          f"{RING_ALL8}; matrix B block-decomposable = {BLOCKY[-1]}; "
          f"sweep {_TSWEEP:.1f}s")

    check("G5-b **'THE ONLY CONFIGURATION D63 FOUND CARRYING 4-DIRECTION "
          "CHARTS AT d = 2' WAS FALSE, AND THE FALSE UNIQUENESS IS WHAT "
          "SUPPRESSED THE SWEEP** (MAJOR 2).  D63's own interior-control "
          "table lists WIDE-BRICK(8,14,C=2), DOUBLE-RING(6,14,6) and "
          "DOUBLE-RING(4,26,4) at nonzero width — width IS D58's "
          "`|D| >= 4` column — and D63 §3 names DR(4,10,4) alongside the "
          "winner.  SEVERAL D63 configurations carry 4-direction charts "
          "at d = 2; the winner is the winner on a COMPOSED "
          "tiling-plus-width criterion, not the only carrier.  The claim "
          "was stated as fact inside gate text and used to justify "
          "running one blueprint.  Measured here: six of the seven "
          "blueprints swept carry 4-direction charts at d = 2",
          sum(1 for k in SWEEP if SWEEP[k]['charts'] > 0
              and not k.startswith('brick')) >= 5
          and SWEEP['wide_brick(8,14,2)']['charts'] > 0
          and SWEEP['DOUBLE-RING(4,10,4)']['charts'] > 0,
          "; ".join(f"{k}: {SWEEP[k]['charts']} wide charts, "
                    f"{SWEEP[k]['distinct']} distinct matrices"
                    for k in SWEEP))

    check("G5-c **THE NARROW CONTROL IS A CONTROL NOW, AND IT FIRES F1 ON "
          "THE v10 SIDE** (MODERATE 2).  The first delivery built the "
          "narrow control, computed its chart Grams and then reported "
          "only `len(CGn)` — so it controlled nothing.  Measured: of the "
          "42 narrow charts (|D| = 3, the same index size as v7's three "
          "channels), FOUR have a direction Gram equal to exactly "
          "(1/4).I — **a multiple of the identity, which is F1's literal "
          "antecedent, on the v10 side** — 34 are the maximally "
          "symmetric (1/4)I + (1/4)J, and 38 of 42 carry the full S_3 "
          "stabiliser of order 6, the same order this receipt's own G6-c "
          "negative control uses to demonstrate F1 firing.  **Had this "
          "been read, the first delivery's forward-pointing hint could "
          "not have been written: on the comparator blueprint the "
          "direction Gram is MORE isotropic than v7's channel Gram, "
          "sometimes exactly lambda.I**",
          len(NAR_EYE) == 4 and NAR_MAXSTAB == 38 and len(CGn) == 42
          and len(NAR_MAXSYM) == 34,
          f"narrow charts = {len(CGn)}; exactly (1/4)I = {len(NAR_EYE)}; "
          f"(1/4)I + (1/4)J = {len(NAR_MAXSYM)}; maximal S_3 stabiliser "
          f"(order 6) = {NAR_MAXSTAB} of {len(CGn)}; stabiliser census = "
          f"{NAR['hist']}; distinct matrices = {NAR['distinct']}")

    outcome("G5 / THE REDIRECTION'S REDIRECTION [MY READING, not a "
            "claim]",
            "The v10 direction Grams AS MEASURED are MORE degenerate "
            "than v7's channel Gram, not less: two constant matrices "
            "across a whole blueprint family, repeated eigenvalues, one "
            "of them block-decomposable, and a stabiliser that is large "
            "precisely because the blueprints were hand-built with "
            "cyclic symmetry.  The one defensible part of the original "
            "hint is CONCEPTUAL and the census neither tests nor "
            "supports it: a chart's direction index is something a group "
            "could act on, where a list of three named record types is "
            "not.  **So the honest successor guidance, graded [MY "
            "READING] and licensed by nothing here: a real tensor stage "
            "needs charts WITHOUT hand-built symmetry — sprinkling-like "
            "substrates or DEFECTED crystals, whose direction geometry "
            "is generic (stabiliser 1) — because a form with a big "
            "stabiliser is a cage, not a metric.**")
except Exception as exc:                                  # noqa: BLE001
    G5_NOTE = f"{type(exc).__name__}: {exc}"
    check("G5 [SAMPLED / CONTEXT GRADE] THE TRANSFER PROBE DID NOT RUN — "
          "reported as a FAIL rather than silently dropped.  Nothing in "
          "G1-G4 depends on it and no G5 claim is made anywhere in this "
          "receipt or its note",
          G5_OK, f"layer chain raised {G5_NOTE}")

# ======================================================================
# F3 — EXPLICITLY DEFERRED, NOT SILENTLY DROPPED (MODERATE 3).
# ======================================================================
outcome("F3 / NOT DECIDED — EXPLICITLY DEFERRED",
        "The pin pre-registers FOUR falsifiers under a NO NULL OUTCOME "
        "header.  F1 is decided (G2, on both fixtures), F2 is decided "
        "(G3, on both fixtures), and F4 is deferred to D72 in the note's "
        "residues.  **F3 — 'the even/odd algebraic split of §3 does not "
        "survive transfer: the anticommutator of the generated line's "
        "own transports is not symmetric, or is not rank-2' — was never "
        "named, never tested and never deferred by the first delivery, "
        "and round 1 was right to call that a first-class omission.**  "
        "It is NOT decided here either, and the reason is stated so the "
        "gap is visible: G5 forms a CO-OCCURRENCE matrix over chart "
        "DIRECTIONS, which is not an anticommutator of the generated "
        "line's transports under any reading, so G5 is not an F3 test "
        "and this receipt will not relabel it as one.  F3 needs the "
        "d42b1 transport pair itself, symmetrised — a unit of work, not "
        "a gate — and it is hereby carried forward as an OPEN "
        "pre-registered falsifier.  No claim anywhere in this receipt or "
        "its note rests on F3 being decided.")

# ======================================================================
# G6 — CONTROLS: anti-vacuity, determinism, negative control
# ======================================================================
print(f"\n{sec()} [G6 — CONTROLS]")

_self = open(os.path.abspath(__file__)).read()
_tree = ast.parse(_self)
_bound = set()
for _n in ast.walk(_tree):
    if isinstance(_n, ast.Name) and isinstance(_n.ctx, ast.Store):
        _bound.add(_n.id)
    elif isinstance(_n, ast.FunctionDef):
        _bound.add(_n.name)


def vacuity_scan(tree, bound):
    bad, n = [], 0
    for nd in ast.walk(tree):
        if not (isinstance(nd, ast.Call)
                and getattr(nd.func, 'id', '') == 'check'
                and len(nd.args) >= 2):
            continue
        n += 1
        p = nd.args[1]
        names = {x.id for x in ast.walk(p) if isinstance(x, ast.Name)}
        if isinstance(p, ast.Constant):
            bad.append((nd.lineno, 'literal constant'))
            continue
        if bound and not (names & bound):
            bad.append((nd.lineno, 'no bound name'))
        for sub in ast.walk(p):
            if (isinstance(sub, ast.Constant)
                    and (sub.value is True or sub.value is False)):
                bad.append((nd.lineno, 'literal boolean'))
            elif (isinstance(sub, ast.Call)
                  and getattr(sub.func, 'id', '') == 'isinstance'):
                bad.append((nd.lineno, 'isinstance type probe'))
    return n, bad


NGATES, TAUT = vacuity_scan(_tree, _bound)
_PB = 'check("a", True)\ncheck("b", isinstance(z, int))\ncheck("c", 1)\n'
_pn, _pb = vacuity_scan(ast.parse(_PB), {'z'})
_PG = 'check("d", G_EVEN == G_P and DISC > 0)\n'
_qn, _qb = vacuity_scan(ast.parse(_PG), {'G_EVEN', 'G_P', 'DISC'})
probe_fires = (_pn == 3 and len(_pb) >= 3 and _qn == 1 and _qb == [])
check("G6-a NO VACUOUS GATE, AND THE SCANNER'S KNOWN DEFECT IS NAMED.  "
      "Every `check()` predicate in this file is parsed and rejected if "
      "it is a literal constant, contains a literal boolean, contains an "
      "`isinstance` type probe, or mentions no name bound anywhere in "
      "this file.  The scanner is probed both ways.  **CARRIED DEFECT "
      "(D46b's finding, repeated here so the gate is not oversold): the "
      "scan is defeated by HOISTING — a predicate reading a boolean "
      "computed on an earlier line looks substantive whatever that line "
      "did.**  It bounds a predicate's shape, not its content",
      not TAUT and NGATES >= 15 and probe_fires,
      f"gate predicates parsed = {NGATES}; flagged = "
      f"{TAUT if TAUT else 'none'}; scanner fires on the vacuous probe "
      f"and passes the substantive one = {probe_fires}")

_DIGEST = r'''
import os, sys, ast
from fractions import Fraction as Fr
from itertools import combinations
ISP = %r
sys.path.insert(0, os.path.join(ISP, 'v7', 'code'))
import p29_projected_likelihood_basis_audit as p29
src = open(os.path.join(ISP, 'v7', 'code',
      'p30_reflection_positive_campaign.py')).read()
t = ast.parse(src)
keep = [n for n in t.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))
        or (isinstance(n, ast.Assign) and any(
            getattr(x, 'id', '') in ('DUAL_PAIRS','RAW_TO_CANON_CACHE',
            'SUBSET_PAIR_CACHE','checks','counts_by_n','reps_by_n',
            'exact_by_n') for x in n.targets))]
g = {k: getattr(p29, k) for k in dir(p29) if not k.startswith('__')}
g.update({'Fraction': Fr, 'combinations': combinations})
import math, sys as _s
from collections import defaultdict
from decimal import Decimal
g.update({'math': math, 'sys': _s, 'defaultdict': defaultdict,
          'D': Decimal, 'Decimal': Decimal})
exec(compile(ast.fix_missing_locations(ast.Module(body=keep,
     type_ignores=[])), 'p30', 'exec'), g)
N = 6
for n in range(1, N + 1):
    c, r, d = g['build_record_universe'](n)
    g['counts_by_n'][n], g['reps_by_n'][n], g['exact_by_n'][n] = c, r, d
fc = g['build_feature_cache'](g['reps_by_n'], 1, N)
g['feature_cache'] = fc
DP = g['DUAL_PAIRS']
tot = sum(g['counts_by_n'][N].values())
def E(j, k):
    f = fc[N]['flags5'][k]
    return f.get(DP[j][0], 0) + f.get(DP[j][1], 0)
M = []
for a in range(3):
    for b in range(3):
        v = Fr(0)
        for k in g['reps_by_n'][N]:
            v += Fr(g['counts_by_n'][N][k], tot) * E(a, k) * E(b, g['dual_key'](k, N))
        M.append(str(v))
sys.stdout.write("|".join(M) + "#" + str(len(g['reps_by_n'][N])))
''' % (ISP,)
HASHSEEDS = (0, 7, 999)
DIG = []
for s in HASHSEEDS:
    env = dict(os.environ)
    env['PYTHONHASHSEED'] = str(s)
    r = subprocess.run([sys.executable, '-c', _DIGEST], env=env,
                       capture_output=True, text=True, cwd=ISP)
    DIG.append((s, r.returncode, r.stdout.strip(), r.stderr[-300:]))
det_ok = (len({d for _s, _rc, d, _e in DIG}) == 1
          and all(rc == 0 for _s, rc, _d, _e in DIG) and DIG[0][2] != "")
print(f"      N = 6 Gram digest = {DIG[0][2][:120]}...")
check("G6-b DETERMINISM under PYTHONHASHSEED 0/7/999: the whole extract-"
      "build-Gram pipeline is re-run in three fresh subprocesses at N = 6 "
      "and its exact-Fraction digest is byte-identical.  The gate is not "
      "idle — `canon_bits` and the flag caches are dict-built and sorted "
      "by iteration order in places, which is exactly what a hash-seed "
      "change perturbs.  SCOPE: the digest, not the whole stdout",
      det_ok and len(DIG) == 3,
      f"seeds {[s for s, _r, _d, _e in DIG]}; return codes "
      f"{[rc for _s, rc, _d, _e in DIG]}; distinct digests = "
      f"{len({d for _s, _rc, d, _e in DIG})}"
      + ("" if det_ok else f"; stderr {DIG[0][3]!r}"))

ID_M = ((Fr(7), Fr(0), Fr(0)), (Fr(0), Fr(7), Fr(0)), (Fr(0), Fr(0), Fr(7)))
c2i, c1i, c0i = charpoly(ID_M)
DISC_I = cubic_disc(c2i, c1i, c0i)
ANISO_I = sum((ID_M[i][j] - (c2i / 3 if i == j else 0)) ** 2
              for i in range(3) for j in range(3))
STAB_I = [p for p in permutations(range(3))
          if all(ID_M[p[i]][p[j]] == ID_M[i][j]
                 for i in range(3) for j in range(3))]
check("G6-c NEGATIVE CONTROL — the F1 instrument fires when F1 is TRUE.  "
      "The same anisotropy, discriminant and stabiliser code is run on a "
      "synthetic `7I`: the traceless part is exactly 0, the cubic "
      "discriminant is exactly 0 (a triple root), and the S_3 stabiliser "
      "is the whole group of order 6.  So G2-b, G2-e and G4-b are "
      "measuring something and would have reported F1 had F1 held",
      ANISO_I == 0 and DISC_I == 0 and len(STAB_I) == 6
      and ANISO_I != FROB_T and len(STAB_I) != len(STAB),
      f"7I: traceless Frobenius^2 = {ANISO_I}, discriminant = {DISC_I}, "
      f"S_3 stabiliser order = {len(STAB_I)}  vs  G^even: "
      f"{dfl(FROB_T, 10)}, {dfl(DISC, 10)}, {len(STAB)}")

# ======================================================================
# VERDICT
# ======================================================================
WALL = time.time() - T00
print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL   ({len(OUTCOMES)} delivered "
      f"outcomes)   wall clock {WALL:.1f}s")
print(f"[EXIT SEMANTICS] exit 1 fires ONLY on G0/G1 anchor breakage; every "
      f"substantive negative exits 0.  So the exit code is NOT a summary "
      f"of the FAIL count and must not be quoted as one — the PASS/FAIL "
      f"line above is (MINOR 3).")
print(f"[RUNTIME] record universes {_TU:.1f}s, deletion graph {_TD:.1f}s, "
      f"feature cache {_TF:.1f}s, the eight committed modes {_TMODES:.1f}s, "
      f"§26.2's four frontier triples {_TFRONT:.1f}s, the selected "
      f"fixture's three modes {_TSEL:.1f}s, its Gram {_TGSEL:.1f}s, the "
      f"{len(NCAND)} promoted-K candidates {_TK:.1f}s, the "
      f"{len(ADV)} h-identity controls {_TADV:.1f}s, the "
      f"{len(SELCAND)} selected-fixture candidates {_TSK:.1f}s; total "
      f"{WALL:.1f}s.  Every arm the pin declares ran, on BOTH fixtures.")

_v_f1 = ("F1 FIRES" if F1_FIRES else
         "F1 DOES NOT FIRE AT N = 9 — the even Gram is genuinely "
         "anisotropic — but it DOES hold at N = 5, where the Gram is "
         "exactly diagonal because the three channel indicators have "
         "disjoint support (G2-h); the off-diagonal is generated by "
         "record depth, first fully present at N = "
         f"{FIRST_FULL}")
_v_f2 = ("F2 FIRES" if BETTER or TVs['quad-I  '] != TV_COMMITTED
         else "F2 DOES NOT FIRE ON EITHER FIXTURE — the quadratic "
              "promotion is admissible on all four committed gates, "
              "reproduces the falsified fixture's TV_9 exactly and "
              "attains the selected fixture's TV_9 = 0 exactly")
print(f"\n[VERDICT] D73 ROUND-1 REVIEWED AND REPAIRED.  **THE FIXTURE, "
      f"FIRST: the triple the first delivery anchored on is the one paper "
      f"30 §26.2 declares FALSIFIED — it ranks 11th, and the "
      f"{fmt_frac(TV_COMMITTED, 12)} this unit called 'the committed "
      f"TV_9' is the loser's score (G1-f).  §27 SELECTS "
      f"{SELECTED} at TV_9 = 0 exactly (G1-g), and both fixtures are run "
      f"here.**  {_v_f1}: eigenvalues "
      f"{[dfl(e, 12) for e in reversed(EIG)]}, three distinct "
      f"off-diagonals {[dfl(v, 10) for v in OFFD]}, traceless Frobenius "
      f"fraction {dfl(FROB_T / FROB_G, 8)}, S_3 stabiliser order "
      f"{len(STAB)} — **AND IT DOES NOT FIRE ON THE SELECTED FIXTURE "
      f"EITHER, where the even Gram is anisotropic at ratio "
      f"{dfl(SEL_ANISO, 8)} (against {dfl(ANISO, 8)}) with stabiliser "
      f"order {len(SEL_STAB)} (G2-i): THE GENUINE G2 SURVIVOR.**  "
      f"{_v_f2}.  THE PROMOTED-K QUESTION WAS FIXTURE-DEAD AT THE OLD "
      f"ANCHOR — {fmt_frac(TV_COMMITTED, 8)} is a SECTOR-SELECTION "
      f"residual no function of the even 3-vector can reach — and "
      f"re-posed on the selected fixture the trace, the componentwise "
      f"ceiling and the fixture's own Gram all attain TV_9 = 0 exactly "
      f"while h-identity-breaking controls are punished (G3-f).  THE "
      f"MECHANISM is the h-WEIGHT IDENTITY, gated at {len(_ALL)} "
      f"candidates over two fixtures with zero mismatches (G3-g) — NOT a "
      f"monotonicity lemma, which the committed table itself falsifies "
      f"(G3-c); and the eleven rows are TWO colourings (G3-h).  THE "
      f"PIN'S F1 IS AN IMPLICATION, NOT A BICONDITIONAL: its antecedent "
      f"is N-dependent (true at N = 5, false from N = 7), its consequent "
      f"holds wherever the antecedent does, and nothing here falsifies "
      f"it — what the unit found is that two senses of 'lossless' "
      f"disagree at N = 9.  THE FAILS-FULL-GR ANSWER: a Gram-derived N "
      f"is a metric-shaped ENSEMBLE STATISTIC — 6 global components "
      f"against v6 p4's per-atom demand (deficit {DEFICIT} in p4's "
      f"COUNTING RULE applied to D73's record count, NOT in p4's units "
      f"and NOT commensurable with p4's 8193, which was not recomputed), "
      f"per-record rank 1, and no group acting on the channel index.  "
      f"THE PROP-10.6 RELATION: different objects, stated in G4-d.  "
      f"TRANSFER, INVERTED: {G5_NOTE or 'not run'} — the v10 direction "
      f"Grams as measured are MORE degenerate and MORE symmetric than "
      f"v7's channel Gram, and a large stabiliser is this receipt's own "
      f"G6-c death condition, so the 'direction index is the stage' hint "
      f"is WITHDRAWN [SAMPLED].  F3 REMAINS OPEN AND IS EXPLICITLY "
      f"DEFERRED, not dropped.  SCOPE: two named fixtures, N = 5..9, "
      f"three dual pairs each, one measure; no gravity claim, no "
      f"continuum claim, no claim that any object here is a metric.")
sys.exit(0)
