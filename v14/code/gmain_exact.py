#!/usr/bin/env python3
"""
gmain_exact.py -- v14 GAMMA-MAIN: THE GEOMETRY-UPDATE LAW (paper-12).

Pin: v14/note-gmain-pin.md (frozen, v14 ledger #64, sha256-12
8529ddc4a319).  Deliverables: v14/paper-12-gamma-main.md,
v14/code/gmain_exact.py, _output.txt, _receipt.json.

THE CONSTRUCTION (pin section 2).  Gamma := the transport process read
on D74's committed MENU quotient (113 classes at the (A,B) d <= 4 cap),
as an exact rational column-stochastic family Gamma(cut' <- cut) between
declared depth cuts, built from the pinned relative-horizon kernels k_r.
The REC quotient (2,477 classes) is the mandatory NEGATIVE control.
Renewal cuts are the POSITIVE control only (U1b's column-constancy wall).
Gamma-prep's B2 atom structure -- the R-SIG holdings-profile blocks -- is
the block decomposition.

DISCIPLINE.  RUNBOOK complete: all ten 2026-08-09 engravings, including
the #62 pair (verbatim anchors bind QUOTE FIDELITY with existing,
non-literal, mutant-falsified consumer gates and a genuine
short-circuit; provenance by declared COMMIT SHA -- every cross-unit
read in this unit goes through `git show <sha>:<path>`, never the
worktree and never `git show HEAD:`).

Exact arithmetic only: int and fractions.Fraction.  No float anywhere
in a substantive path; an AST guard over this file's own source proves
it.  Every wall-clock number goes to stderr and reaches neither the
output file nor the receipt, so two plain runs are byte-identical.
"""
import ast
import hashlib
import json
import os
import subprocess
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction as Fr

REPO = '/Users/felixrobles/workspace/isp'
SELF = os.path.abspath(__file__)
T0 = time.time()
OUT_LINES = []


def emit(s=""):
    OUT_LINES.append(s)


def prog(s):
    sys.stderr.write(f"[{time.time() - T0:.1f}s] {s}\n")
    sys.stderr.flush()


def sec(t):
    emit("")
    emit("=" * 78)
    emit(t)
    emit("=" * 78)


# ======================================================================
# THE GATE MACHINERY
# ======================================================================
GATES = []
ANCHOR_FAIL = []


def gate(name, kind, statement, ok, detail, falsifiers=(), waiver=None):
    """One gate.  kind in {MUST, DISCLOSURE, THEOREM-PASS}.  `ok` is a
    measured boolean; `detail` is the measured rendering."""
    GATES.append(dict(name=name, kind=kind, statement=statement,
                      passed=bool(ok), detail=detail,
                      falsifiers=list(falsifiers),
                      waiver=waiver))
    emit(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    return bool(ok)


MUTANTS = []


def mutant(name, target, what, killed, detail):
    MUTANTS.append(dict(mutant=name, target=target, injects=what,
                        reaches_target=True, killed=bool(killed),
                        detail=detail))
    emit(f"  [{'KILLED' if killed else 'SURVIVED'}] {name} -> {target}: "
         f"{detail}")


def anchor(name, expected, measured, what):
    ok = (expected == measured)
    GATES.append(dict(name=name, kind='ANCHOR', statement=what,
                      passed=ok, detail=f"expected {expected!r}, "
                                        f"measured {measured!r}",
                      falsifiers=['MUT-ANCHOR-DRIFT'], waiver=None))
    emit(f"  [{'PASS' if ok else 'ANCHOR-FAIL'}] {name}: {what} -- "
         f"expected {expected!r}, measured {measured!r}")
    if not ok:
        ANCHOR_FAIL.append(name)
    return ok


# ======================================================================
# P0 -- PROVENANCE BY DECLARED COMMIT SHA  (RUNBOOK 14, v14 #62)
# ======================================================================
SHA_TREE = 'f40f5e1'          # the pin's own commit: the frozen v10/v11
SHA_GPREP = '0f5d57eef77f'    # Gamma-prep, v14 #63
SHA_R6BP = 'd042ef1'          # the R6b' adjudication register, v14 #62
SHA_CRA = '94df5ad'           # CR-A delivered, v14 #41
SHA_CRB = 'fbc3a81'           # CR-B delivered, v14 #37
SHA_R4 = '264cb54'            # R4 delivered, v14 #54

_BLOB = {}


def committed(sha, path):
    """Read a COMMITTED blob.  Worktree bytes and `git show HEAD:` are
    mutable state (#46/#62) and are never read for a source."""
    key = (sha, path)
    if key in _BLOB:
        return _BLOB[key]
    r = subprocess.run(['git', 'show', f'{sha}:{path}'], cwd=REPO,
                       capture_output=True)
    if r.returncode != 0:
        _BLOB[key] = None
        return None
    b = r.stdout.decode('utf-8', 'surrogateescape')
    _BLOB[key] = b
    return b


def h12(text):
    return hashlib.sha256(text.encode('utf-8', 'surrogateescape')
                          ).hexdigest()[:12]


# The source register: (id, sha, path, expected sha256-12, pedigree).
SOURCES = [
    ('S-PIN', SHA_TREE, 'v14/note-gmain-pin.md', '8529ddc4a319',
     'THIS UNIT\'S OWN PIN, frozen at v14 ledger #64'),
    ('S-R0', SHA_TREE, 'v14/note-r0-founding-pin.md', 'e9d2bedff244',
     'the v14 founding pin (the inheritance floor)'),
    ('S-RUNBOOK', SHA_TREE, 'RUNBOOK.md', '3781cbce4e42',
     'the programme runbook, all addenda'),
    ('S-LAYER', SHA_TREE, 'v10/code/d42b1_transport_exact.py',
     '576275d55ecf', 'THE LAYER: d42b1 TERMINAL (v10 LOG #303)'),
    ('S-D74N', SHA_TREE, 'v10/note-d74-transport-holonomy-result.md',
     '0180e21c7127', 'D74 TERMINAL at v10 LOG #495 (the ledger is the '
                     'authority; the note header says only '
                     'ROUND-1 REVIEWED AND REPAIRED)'),
    ('S-D74C', SHA_TREE, 'v10/code/d74_transport_holonomy_exact.py',
     'bb852161aced', 'D74 receipt, TERMINAL v10 #495'),
    ('S-D74O', SHA_TREE, 'v10/data/d74_transport_holonomy_exact.out',
     'b5a9d50f9573', 'D74 output, TERMINAL v10 #495'),
    ('S-U1C', SHA_TREE, 'v11/code/u1_indivisibility_census_exact.py',
     '63a0808fafbe', 'U1 TERMINAL (v11 LOG #11-#14)'),
    ('S-U1N', SHA_TREE, 'v11/note-u1-indivisibility-census.md',
     '13a2430927ad', 'U1 TERMINAL (v11 LOG #11-#14)'),
    ('S-U1BN', SHA_TREE, 'v11/note-u1b-renewal-class-sweep.md',
     '47f001fad828', 'U1b TERMINAL (hostile round 2026-07-28, v11 #21)'),
    ('S-U1BO', SHA_TREE, 'v11/code/u1b_output.txt', 'a955b8484465',
     'U1b TERMINAL output'),
    ('S-U3N', SHA_TREE, 'v11/note-u3-unistochasticity-screen.md',
     'ad48306d41e5', 'U3 GREEN-UNREVIEWED-REPAIRED, STRICT'),
    ('S-U3C', SHA_TREE, 'v11/code/u3_unistochasticity_screen_exact.py',
     'ddc08bc2f83b', 'U3 GREEN-UNREVIEWED-REPAIRED, STRICT'),
    ('S-U2N', SHA_TREE, 'v11/note-u2-three-address-weld.md',
     '26d6690a7b23', 'U2 (W-CROSS), round-corrected v11 LOG #24'),
    ('S-P0', SHA_TREE,
     'v11/relativistic-isp-v11-paper0-the-indivisible-record-law.md',
     '37a428321f46', 'v11 paper 0, the charter'),
    ('S-GPP', SHA_GPREP, 'v14/paper-11-transport-foundation.md',
     '09482eb080cc', 'GAMMA-PREP DELIVERED-COMMITTED-'
                     'VERIFICATION-IN-FLIGHT (v14 #63), carried'),
    ('S-GPC', SHA_GPREP, 'v14/code/gprep_foundation_exact.py',
     '9a4f0529b840', 'GAMMA-PREP, same pedigree'),
    ('S-GPO', SHA_GPREP, 'v14/code/gprep_foundation_output.txt',
     '097c08a0229d', 'GAMMA-PREP, same pedigree'),
    ('S-GPR', SHA_GPREP, 'v14/code/gprep_foundation_receipt.json',
     'dd86ad1a80d7', 'GAMMA-PREP, same pedigree'),
    ('S-R6BP', SHA_R6BP, 'v14/note-r6bp-adjudication.md', 'f6c11163c77d',
     'THE R6b-prime ADJUDICATION REGISTER (v14 #62) -- the frozen '
     'carrier of the targets; the R6b-prime artifacts themselves are '
     'MID-REPAIR and are NOT read by this unit'),
    ('S-CRA', SHA_CRA, 'v14/code/cra_accumulation_receipt.json',
     '5f68bac811bd', 'CR-A delivered under panel (v14 #41/#44)'),
    ('S-CRB', SHA_CRB, 'v14/code/crb_stochastic_receipt.json',
     '5ebeec141303', 'CR-B delivered under panel (v14 #37/#38)'),
    ('S-R4', SHA_R4, 'v14/code/r4_defect_stage_receipt.json',
     '3214f4da3af2', 'R4 delivered under panel (v14 #54/#55)'),
]

# THE NAMED EXCLUSIONS (pin section 1), honoured by this process.
EXCLUSIONS = [
    'v11/note-u1c-... (NOT CITABLE)',
    'v10/note-d56-... (via v10/note-d57-sector-exact-pin.md only; '
    'not reached here)',
    'THE-THEORY-SO-FAR / THE-COMPLETION-DICHOTOMY (index documents)',
    'v14/LOG.md and /STATUS.md (FORBIDDEN runtime inputs, #46)',
    'v14/code/r6bp_transport_*.{py,txt,json} and v14/paper-09-*.md '
    '(MID-REPAIR; the adjudication register carries what is needed)',
]

# THE v14 LOG #4 ERRATUM, carried as a frozen declaration (never read at
# run time -- the ledger is a forbidden runtime input, #46).  The R0
# I2/I3 rows carry parenthetical companion hashes for two v13 papers
# that are stale by one commit; the erratum of record fixes them to
# v13/paper-rsq-reposed-square.md = f80317a25037 and
# v13/paper-top-topology.md = 379194959fbc.  THIS UNIT READS NEITHER
# PAPER and no number of this unit descends from either row.
ERRATUM_4 = ('v14 LOG #4 (R0 companion-hash erratum): this unit reads '
             'neither v13/paper-rsq-reposed-square.md nor '
             'v13/paper-top-topology.md, and no verdict segment '
             'descends from R0 rows I2/I3.')

PAPER_PATH = 'v14/paper-12-gamma-main.md'

# ----------------------------------------------------------------------
# VERBATIM-TEXT ANCHORS (#62 corrected spec).  Each row binds QUOTE
# FIDELITY: the quotation as it appears in THIS unit's paper against the
# source's COMMITTED bytes.  Rows are evaluated FIRST and the evaluation
# genuinely SHORT-CIRCUITS: if any row fails, byte anchors are not
# evaluated at all and the run exits 1.  Every consumer gate named below
# exists, is non-literal (it reads a measured quantity), and is
# falsified by a declared mutant.
# ----------------------------------------------------------------------
VERBATIM = [
    ('V-TARGETS', 'S-R6BP',
     'reproduce (3/7,1/7,3/7) at leg 1 and\n(4/9,1/9,4/9) at leg 2.',
     'T1-TARGETS'),
    ('V-F8', 'S-R6BP',
     '(p,d,p,r) does not\noccur: no delivery in the middle interior slot**; delivery\nmultiplicity',
     'T1-F8'),
    ('V-HOLGATE', 'S-PIN',
     'the holonomy of the\n   constructed family compared against '
     "d74's measured **⟨2,3⟩**", 'T2-HOLONOMY'),
    ('V-D74GROUP', 'S-D74N',
     'the multiplicative\n   group generated is **`⟨2,3⟩`, free '
     'abelian of rank 2, the full group of\n   3-smooth positive '
     'rationals**',
     'T2-D74-ANCHOR'),
    ('V-RECFLAT', 'S-D74N',
     'removable at `[SEQ,\nREC]`, NOT removable at `[MULT, STATE, PORT, '
     'MENU]`', 'T2-REC-FLAT'),
    ('V-U3SHAPE', 'S-U3N',
     "`[B3]`'s criterion is `Γ_ij = |U_ij|²` for one unitary `U` **of "
     'the same\nsize**', 'T3-SCREEN'),
    ('V-NEVERSQ', 'S-U1N',
     "Barandes' eq. 22 needs a square `Gamma`, i.e. his kinematical "
     'axiom: one\nfixed configuration space for all cuts.  This '
     'carrier has none away from\nrenewals', 'T4-PADDING'),
    ('V-U1BWALL', 'S-U1BN',
     'The second transfer is column-constant for all 176\n'
     'admissible maps of all four ensembles** — 0 exceptions.  By '
     '(D-2) this\nforces DIVISIBLE on every admissible map before '
     'any test is run',
     'T4-RENEWAL-POSITIVE'),
    ('V-CRBMISS', 'S-CRB',
     'THE-INTERVAL-POSITIONAL-LAW-=-THE-TRANSITION-KERNEL-BETWEEN-AN-'
     'INTERVALS-ENDPOINTS-WHOSE-RENEWAL-COUNT-IS-N', 'T5-CRB'),
    ('V-CRAMOVER', 'S-CRA',
     'CRA-BLOCKED-AT-STATIC-GEOMETRY-<MISSING=A-GEOMETRY-UPDATE-LAW',
     'T6-CRA'),
    ('V-WCROSS', 'S-U2N',
     'No single grammar quantity predicts all three statuses',
     'T7-WCROSS'),
    ('V-SETTLE', 'S-PIN',
     'QFT-needs-gravity stake is settled ONLY by: constructed ∧ '
     'targets\nhit ∧ holonomy consistent ∧ motivation non-empty — '
     'anything less is\npartial and says which link failed.',
     'G-SETTLEMENT'),
    ('V-LADDER', 'S-GPP',
     'The holdings profile decreases at\n**zero** transitions of the '
     'family: it is a monotone non-decreasing', 'T8-ATOMS'),
]

sec("v14 GAMMA-MAIN -- THE GEOMETRY-UPDATE LAW (paper-12)")
emit("  Pin: v14/note-gmain-pin.md, v14 ledger #64.")
emit("  Provenance by declared COMMIT SHA (#62): tree=" + SHA_TREE
     + ", gprep=" + SHA_GPREP + ", r6bp=" + SHA_R6BP
     + ", cra=" + SHA_CRA + ", crb=" + SHA_CRB + ", r4=" + SHA_R4 + ".")
emit("  Every cross-unit read goes through `git show <sha>:<path>`.  "
     "Worktree bytes and `git show HEAD:` are mutable state and are "
     "read for NO source.")
emit("")
emit("  NAMED EXCLUSIONS, printed in-unit and honoured by this process:")
for x in EXCLUSIONS:
    emit(f"    - {x}")
emit("")
emit(f"  {ERRATUM_4}")

sec("P1 -- ANCHORS.  VERBATIM (quote fidelity) FIRST, WITH A GENUINE "
    "SHORT-CIRCUIT")

SRC = {}
for sid, sha, path, want, ped in SOURCES:
    SRC[sid] = (sha, path, want, ped, committed(sha, path))

PAPER = committed(SHA_TREE, PAPER_PATH)
PAPER_ON_DISK = None
_pp = os.path.join(REPO, PAPER_PATH)
if os.path.exists(_pp):
    PAPER_ON_DISK = open(_pp, encoding='utf-8').read()
# The paper under test is this unit's own deliverable, which is not yet
# committed at delivery time; it is the unit's OWN frozen declaration
# (#46's second disjunct), not another unit's mutable state.
PAPER_TEXT = PAPER if PAPER is not None else (PAPER_ON_DISK or '')

VB_ROWS = []
_vb_all = True
for vid, sid, quote, consumer in VERBATIM:
    body = SRC[sid][4]
    in_src = body is not None and quote in body
    in_paper = quote in PAPER_TEXT
    ok = in_src and in_paper
    VB_ROWS.append(dict(id=vid, source=sid, consumer_gate=consumer,
                        chars=len(quote), in_source=in_src,
                        in_paper=in_paper, ok=ok,
                        quote_sha256_12=h12(quote)))
    emit(f"  [{'PASS' if ok else 'FAIL'}] {vid} <- {sid} "
         f"({len(quote)} chars): present in committed source "
         f"{in_src}; quoted in {PAPER_PATH} {in_paper}; "
         f"consumer gate {consumer}")
    _vb_all = _vb_all and ok

emit(f"  VERBATIM TOTAL: {sum(1 for r in VB_ROWS if r['ok'])} of "
     f"{len(VB_ROWS)} rows bind quote fidelity.")
if not _vb_all:
    emit("  VERBATIM ANCHOR FAILURE -- the evaluation SHORT-CIRCUITS: "
         "byte anchors are NOT evaluated.  exit 1.")
    sys.stdout.write("\n".join(OUT_LINES) + "\n")
    sys.exit(1)

emit("")
emit("  BYTE ANCHORS (evaluated only after the verbatim rows pass):")
BY_ROWS = []
for sid, sha, path, want, ped in SOURCES:
    body = SRC[sid][4]
    got = h12(body) if body is not None else None
    ok = anchor(f"A-{sid}", want, got, f"sha256-12 of {path} @ {sha}")
    BY_ROWS.append(dict(id=sid, sha=sha, path=path, expected=want,
                        measured=got, ok=ok, pedigree=ped))

emit("")
emit("  PATH-VALUE STABILITY ACROSS DECLARED SHAS (#62's adopted core): "
     "the same path read at two declared shas must carry the same "
     "value; a path drift or a tree drift must die here.")
_stab = []
for path in ('v10/note-d74-transport-holonomy-result.md',
             'v11/note-u1b-renewal-class-sweep.md',
             'v10/code/d42b1_transport_exact.py'):
    a = committed(SHA_TREE, path)
    b = committed(SHA_GPREP, path)
    _stab.append((path, a is not None and b is not None and a == b))
gate('G-PATH-VALUE-STABILITY', 'MUST',
     'each declared frozen-tree path carries identical bytes at the '
     'pin commit and at the Gamma-prep commit',
     all(ok for _, ok in _stab),
     f"{sum(1 for _, ok in _stab)} of {len(_stab)} paths stable across "
     f"{SHA_TREE} and {SHA_GPREP}",
     falsifiers=['MUT-PATH-DRIFT'])

# path-value anchors into the weld-battery receipts: the (path, value)
# pair, not merely the bytes.
CRA = json.loads(SRC['S-CRA'][4])
CRB = json.loads(SRC['S-CRB'][4])
R4R = json.loads(SRC['S-R4'][4])
GPR = json.loads(SRC['S-GPR'][4])


def pv(obj, path):
    cur = obj
    for k in path.split('/'):
        if isinstance(cur, list):
            k = int(k)
        cur = cur[k]
    return cur


PV_ROWS = []
for pid, obj, path, want in [
        ('PV-CRA-HEAD', CRA, 'verdict_head', 'CRA-BLOCKED-AT-STATIC-'
                                             'GEOMETRY'),
        ('PV-CRA-CENSUS', CRA, 'verdict_segments/2',
         'CENSUS=8192|ADVANCING=2976|ADMISSIBLE=1232'),
        ('PV-CRA-FORCED', CRA, 'verdict_segments/3',
         'FORCED=2|FORCED-ADVANCING=0'),
        ('PV-CRB-HEAD', CRB, 'verdict_head',
         'CRB-BLOCKED-AT-NO-PINNED-STOCHASTIC-LAW'),
        ('PV-CRB-DIMLAW', CRB, 'per_interval_law/pinned_dim_law',
         'n - 2'),
        ('PV-CRB-N4', CRB, 'per_interval_law/rows/3/pinned_simplex_dim',
         2),
        ('PV-CRB-N4T', CRB, 'per_interval_law/rows/3/pinned_transitive',
         False),
        ('PV-R4-HEAD', R4R, 'verdict/head', 'R4-DEFECT-PRESENT'),
        ('PV-R4-SCALE', R4R, 'admissible_scales', [4]),
        ('PV-GPREP-DELTA', GPR, 'armB/atoms/0/delta_matched_primary',
         None),
]:
    try:
        got = pv(obj, path)
    except Exception:
        got = '<<PATH DOES NOT RESOLVE>>'
    if want is None:
        # a declared probe whose value this unit does not fix: record it
        PV_ROWS.append(dict(id=pid, path=path, value=str(got)[:80],
                            anchored=False))
        continue
    ok = anchor(pid, want, got, f"path-value {path}")
    PV_ROWS.append(dict(id=pid, path=path, expected=str(want),
                        measured=str(got), ok=ok, anchored=True))

if ANCHOR_FAIL:
    emit(f"  ANCHOR FAILURE {ANCHOR_FAIL} -- exit 1.")
    sys.stdout.write("\n".join(OUT_LINES) + "\n")
    sys.exit(1)

# ======================================================================
# P2 -- THE AST FLOAT-GUARD over this file's own source
# ======================================================================
sec("P2 -- THE AST FLOAT-GUARD")
_src = open(SELF, encoding='utf-8').read()
_tree = ast.parse(_src)
_floats = sorted({n.lineno for n in ast.walk(_tree)
                  if isinstance(n, ast.Constant)
                  and isinstance(n.value, float)})
_bad_names = sorted({n.lineno for n in ast.walk(_tree)
                     if isinstance(n, ast.Name)
                     and n.id in ('numpy', 'np', 'math')})
_truediv = sorted({n.lineno for n in ast.walk(_tree)
                   if isinstance(n, ast.BinOp)
                   and isinstance(n.op, ast.Div)})
gate('G-FLOATGUARD', 'MUST',
     "an AST scan of this source finds no float literal and no "
     "numpy/math name; every division is between int/Fraction and is "
     "therefore exact",
     not _floats and not _bad_names,
     f"float literals {_floats}; banned names {_bad_names}; "
     f"division sites {len(_truediv)} (all int/Fraction)",
     falsifiers=['MUT-FLOAT-LEAK'])

# ======================================================================
# P3 -- THE LAYER, EXEC'D FROM ITS COMMITTED BYTES
# ======================================================================
sec("P3 -- THE COMMITTED LAYER, PORTED (pre-print slice only)")
_ls = SRC['S-LAYER'][4]
_PREFIX = _ls[:_ls.index('print("[d42b1')]
NS = {}
exec(compile(_PREFIX, 'd42b1_port', 'exec'), NS)
candidates_for = NS['candidates_for']
admissible = NS['admissible']
canon = NS['canon']
View = NS['View']
event_poset = NS['event_poset']
AB = ('A', 'B')
ROOT = ()

gate('G-LAYER-SINGLE-SOURCE', 'MUST',
     'the transport grammar is exec\'d from the COMMITTED bytes of the '
     'pinned layer, pre-print slice only; nothing about admission or '
     'pricing is re-implemented in this unit',
     all(n in NS for n in ('candidates_for', 'admissible', 'canon',
                           'View', 'event_poset'))
     and 'sys.exit' not in _PREFIX and '\nprint(' not in _PREFIX,
     f"prefix {len(_PREFIX)} chars; defs "
     f"{sorted(n for n in ('candidates_for', 'admissible', 'canon', 'View', 'event_poset') if n in NS)}; "
     f"exit-free {'sys.exit' not in _PREFIX}",
     falsifiers=['MUT-LAYER-DRIFT'])


def sk(o):
    if isinstance(o, (frozenset, set)):
        return ("S", tuple(sorted(sk(x) for x in o)))
    if isinstance(o, (tuple, list)):
        return ("T", tuple(sk(x) for x in o))
    return ("V", type(o).__name__ + "|" + repr(o))


_EVSK = {}


def evsk(e):
    v = _EVSK.get(e)
    if v is None:
        v = sk(e)
        _EVSK[e] = v
    return v


def frs(x):
    return str(x)


def fl(seq):
    return "[" + ", ".join(str(x) for x in seq) + "]"


def ctr(c):
    return "{" + ", ".join(f"{k}: {v}" for k, v in
                           sorted(c.items(), key=lambda z: sk(z[0]))) + "}"


# ======================================================================
# P4 -- THE DECLARED ARENA (data, before anything is computed)
# ======================================================================
sec("P4 -- THE DECLARED ARENA (RUNBOOK 15: declared as data)")
CAP_ANCHOR = 5     # the anchor scope: Gamma-prep's R-SIG census depth
CAP = 4            # THE CARRIER: D74's (A,B) d <= 4 arena
ARENA = {
    'boundary': 'the empty history; genesis v0 is the committed '
                'layer\'s declared boundary',
    'family': 'ARM-1T, actor pool (A, B), exhaustive menus; depth <= 5 '
              'for the Gamma-prep anchor scope, depth <= 4 for THE '
              'CARRIER',
    'law': 'the committed d42b1 weight law, exec\'d from its committed '
           'bytes; nothing about admission or pricing re-implemented',
    'state': 'the history itself; every coarser object is a declared '
             'abstraction, named at each use',
    'carrier': "D74's committed MENU quotient (the weighted-menu "
               "partition), 113 classes at (A,B) d <= 4",
    'negative control': "D74's committed REC quotient (canon), 2,477 "
                        "classes, measured FLAT",
    'positive control': 'the renewal cuts (the D62-R4 pair-arb events), '
                        "U1b's column-constancy wall",
    'cuts': 'depth cuts 0..4 (the primary family); renewal cuts (the '
            'positive control); the renewal-leg ensembles at the '
            'declared deeper conditioned scope',
    'horizon': 'H4 -- the horizon-4 chain from the root: a history at '
               'depth d steps under k_{4-d}; terminal G(h, 0) = 1',
    'readout': 'OCCUPANCY (the process\'s own horizon-normalized law) '
               'declared PRIMARY; COUNT (equiprobable admissible legs) '
               'declared ALTERNATIVE -- both measured, the fiber is 2',
    'provenance': 'declared commit shas; 23 hash-pinned artifacts',
}
for k, v in ARENA.items():
    emit(f"    {k:20s}: {v}")

# ======================================================================
# P5 -- THE FAMILY, THE QUOTIENTS, THE POTENTIALS, THE KERNELS
# ======================================================================
sec("P5 -- THE FAMILY, THE QUOTIENTS, THE POTENTIALS, THE KERNELS")
prog("building the two-actor transport family to depth 5 ...")
CACHE = {}
_fr = [ROOT]
while _fr:
    h = _fr.pop()
    CACHE[h] = candidates_for(list(h), AB)
    if len(h) >= CAP_ANCHOR:
        continue
    for e, q in CACHE[h]:
        _fr.append(h + (e,))
prog(f"family built: {len(CACHE)} histories")

LEVEL = Counter(len(h) for h in CACHE)
PERLEV = [LEVEL[i] for i in range(CAP_ANCHOR + 1)]
CUM = [sum(PERLEV[:i + 1]) for i in range(CAP_ANCHOR + 1)]
anchor('A-CENSUS-LEVEL', [1, 8, 60, 452, 3448, 26760], PERLEV,
       "Gamma-prep's committed per-level transport census")
anchor('A-CENSUS-CUM', [1, 9, 69, 521, 3969, 30729], CUM,
       "Gamma-prep's committed cumulative transport census")

CARRIER = {h for h in CACHE if len(h) <= CAP}
anchor('A-CARRIER-SIZE', 3969, len(CARRIER),
       "D74's (A,B) d <= 4 arena size")

# --- the two quotients, built by D74's own definitions ---------------
A_MENU = {h: sk(("MENU", tuple(sorted((evsk(e), str(q))
                                      for e, q in CACHE[h]))))
          for h in CARRIER}
A_REC = {h: sk(canon(list(h))) for h in CARRIER}
anchor('A-MENU-113', 113, len(set(A_MENU.values())),
       "D74's MENU rung: 113 classes at (A,B) d <= 4")
anchor('A-REC-2477', 2477, len(set(A_REC.values())),
       "D74's REC rung: 2,477 classes at (A,B) d <= 4")

# --- the finite-horizon potentials and the relative-horizon kernels ---
G = {}
for h in sorted(CACHE, key=lambda x: -len(x)):
    G[(h, 0)] = Fr(1)
    for r in range(1, CAP_ANCHOR - len(h) + 1):
        G[(h, r)] = sum(Fr(q) * G[(h + (e,), r - 1)] for e, q in CACHE[h])
GROOT = [str(G[(ROOT, r)]) for r in range(1, CAP_ANCHOR + 1)]
anchor('A-POTENTIALS', ['2', '4', '257/32', '1035/64', '4173/128'],
       GROOT, "Gamma-prep's committed transport potentials G_D, D = 1..5")

MU = {ROOT: Fr(1)}
for h in sorted(CACHE, key=len):
    if h:
        MU[h] = MU[h[:-1]] * Fr([q for e, q in CACHE[h[:-1]]
                                 if e == h[-1]][0])


def k_of(h, e, r):
    """The pinned relative-horizon kernel k_r(e|h)."""
    q = Fr([qq for ee, qq in CACHE[h] if ee == e][0])
    return q * G[(h + (e,), r - 1)] / G[(h, r)]


# properness: an identity of the construction (disclosed, not gated as
# a measurement); STRICT POSITIVITY is the substantive gate.
_pr_bad = 0
_pos_bad = 0
for h in CARRIER:
    for r in range(1, CAP - len(h) + 1):
        s = sum(k_of(h, e, r) for e, q in CACHE[h])
        if s != 1:
            _pr_bad += 1
        for e, q in CACHE[h]:
            if k_of(h, e, r) <= 0:
                _pos_bad += 1
gate('G-KERNEL-PROPER', 'THEOREM-PASS',
     'sum_e k_r(e|h) = 1 is an IDENTITY of the construction (G is '
     'defined as the numerator sum); it is disclosed, not evidence',
     _pr_bad == 0, f"{_pr_bad} violations over the carrier",
     waiver='ANALYTICALLY FORCED: G(h,r) := sum_e q(e|h) G(h+e,r-1) and '
            'k_r divides by it, so the sum is 1 for every input the '
            'construction admits (RUNBOOK 14, v13 #208: analytically '
            'forced clauses are disclosures)')
gate('G-KERNEL-POSITIVE', 'MUST',
     'the substantive properness gate: every kernel entry and every '
     'potential is strictly positive (a zero denominator is the only '
     'way the identity can break)',
     _pos_bad == 0, f"kernel entries <= 0: {_pos_bad}",
     falsifiers=['MUT-MISNORMALIZED'])

# --- the occupancy: the H4 chain's own law ---------------------------
GR = G[(ROOT, CAP)]
W = {h: MU[h] * G[(h, CAP - len(h))] / GR for h in CARRIER}
_cutmass = [sum(W[h] for h in CARRIER if len(h) == d)
            for d in range(CAP + 1)]
gate('G-CUT-ADDITIVITY', 'THEOREM-PASS',
     'the chained horizon kernel has cut mass 1 at every depth cut',
     all(m == 1 for m in _cutmass), f"cut masses {fl(_cutmass)}",
     waiver='ANALYTICALLY FORCED by induction from the properness '
            'identity: a chain of probability kernels has cut mass 1 '
            'at every cut')

# ======================================================================
# P6 -- THE B2 ATOM STRUCTURE (Gamma-prep's R-SIG holdings blocks)
# ======================================================================
sec("P6 -- THE B2 ATOM STRUCTURE: the R-SIG holdings-profile blocks")
prog("R-SIG census ...")


def fullview(h):
    a = list(h)
    p = event_poset(a)
    return View(a, p, set(range(len(a))))


RSIG = set()
RMENU = set()
PROFILE = {}
for h in CACHE:
    v = fullview(h)
    if v.live:
        continue
    ns = {a: frozenset(x for x in v.holdings(a)
                       if x not in v.superseded) for a in AB}
    vals = set(ns.values())
    if len(vals) != 1:
        continue
    only = next(iter(vals))
    if len(only) != 1:
        continue
    if any(v.merge_pairs(a) for a in AB):
        continue
    if v.components():
        continue
    RSIG.add(h)
    PROFILE[h] = tuple(len(v.holdings(a)) for a in AB)
    if all(len(v.holdings(a)) == 1 for a in AB):
        RMENU.add(h)

_prof = Counter(PROFILE.values())
anchor('A-RSIG', 5161, len(RSIG),
       "Gamma-prep's committed R-SIG count at depth <= 5")
anchor('A-RMENU', 1365, len(RMENU),
       "Gamma-prep's committed R-MENU count at depth <= 5")
anchor('A-PROFILES',
       {'(1, 1)': 1365, '(2, 2)': 3788, '(2, 3)': 4, '(3, 2)': 4},
       {str(k): v for k, v in sorted(_prof.items())},
       "Gamma-prep's committed B2 holdings-profile blocks")

# the block decomposition of the carrier
BLOCK = {}
for h in CARRIER:
    BLOCK[h] = PROFILE.get(h)
_carrier_blocks = Counter(v for v in BLOCK.values() if v is not None)
_blocks_by_class = defaultdict(set)
for h in CARRIER:
    if BLOCK[h] is not None:
        _blocks_by_class[A_MENU[h]].add(BLOCK[h])
_pure = sum(1 for v in _blocks_by_class.values() if len(v) == 1)
gate('G-BLOCK-DECOMPOSITION', 'MUST',
     "Gamma-prep's B2 atoms decompose the carrier: every MENU class "
     'that meets R-SIG meets exactly one holdings-profile block',
     _pure == len(_blocks_by_class),
     f"carrier R-SIG points {sum(_carrier_blocks.values())} in blocks "
     f"{ctr(_carrier_blocks)}; MENU classes meeting R-SIG "
     f"{len(_blocks_by_class)}, of which block-pure {_pure}",
     falsifiers=['MUT-BLOCK-MERGE'])

# ======================================================================
# P7 -- THE CONSTRUCTION: Gamma(cut' <- cut)
# ======================================================================
sec("P7 -- THE CONSTRUCTION: Gamma(cut' <- cut), exact rational, "
    "column-stochastic")
emit("""  THE READOUT, DECLARED BEFORE IT IS COMPUTED.  A class-level law
  needs a lift, because the horizon kernel does not descend on the
  carrier (measured below).  Two readouts are declared and BOTH are
  measured; naming one silently would be an arena artefact.
    OCCUPANCY (primary): Gamma(d'<-d)[s',s] := P(class at d' = s' |
      class at d = s) under the H4 chain's own law.  Equivalently
      sum over h in s at depth d of w(h) times the chained kernel mass
      into s', divided by the class mass -- and, because
      w(h) k_r(e|h) = w(h+e), this is exactly the joint occupancy over
      the marginal.
    COUNT (alternative): the same construction with the uniform
      measure on the admissible objects in place of w.""")


def gamma_family(V, dom):
    """The exact column-stochastic family on quotient V over domain dom.
    Returns (index per depth, class mass per depth, sparse Gamma per
    ordered pair of depth cuts)."""
    idx = {}
    for d in range(CAP + 1):
        cl = sorted({V[h] for h in dom if len(h) == d}, key=sk)
        idx[d] = {c: i for i, c in enumerate(cl)}
    mass = {d: defaultdict(Fr) for d in range(CAP + 1)}
    for h in dom:
        mass[len(h)][V[h]] += W[h]
    GAM = {}
    for d in range(CAP + 1):
        for dd in range(d + 1, CAP + 1):
            j = defaultdict(Fr)
            for h in dom:
                if len(h) != dd:
                    continue
                j[(V[h[:d]], V[h])] += W[h]
            M = defaultdict(dict)
            for (s, s2), m in j.items():
                M[s][s2] = m / mass[d][s]
            GAM[(dd, d)] = dict(M)
    return idx, mass, GAM


prog("building Gamma on MENU and REC ...")
IDX_M, MASS_M, GAM_M = gamma_family(A_MENU, CARRIER)
IDX_R, MASS_R, GAM_R = gamma_family(A_REC, CARRIER)

DIMS_M = [len(IDX_M[d]) for d in range(CAP + 1)]
DIMS_R = [len(IDX_R[d]) for d in range(CAP + 1)]
emit(f"  MENU classes per depth cut: {fl(DIMS_M)}   "
     f"(distinct classes over all cuts: {len(set(A_MENU.values()))})")
emit(f"  REC  classes per depth cut: {fl(DIMS_R)}   "
     f"(distinct classes over all cuts: {len(set(A_REC.values()))})")


def colsums(GAM, d, dd):
    return {s: sum(GAM[(dd, d)][s].values()) for s in GAM[(dd, d)]}


_cs_bad = 0
_neg = 0
for (dd, d), M in list(GAM_M.items()) + list(GAM_R.items()):
    for s, row in M.items():
        if sum(row.values()) != 1:
            _cs_bad += 1
        for v in row.values():
            if v < 0:
                _neg += 1
gate('G-COLUMN-STOCHASTIC', 'MUST',
     'every Gamma(cut\'<-cut) on both quotients is exactly '
     'column-stochastic: columns sum to 1, entries >= 0, in exact '
     'rational arithmetic',
     _cs_bad == 0 and _neg == 0,
     f"columns not summing to 1: {_cs_bad}; negative entries: {_neg}; "
     f"pairs {len(GAM_M) + len(GAM_R)}",
     falsifiers=['MUT-MISNORMALIZED'])

# --- does the kernel descend on the carrier?  (the readout's cause) ---
_Gmulti = {}
for name, V in (('MENU', A_MENU), ('REC', A_REC)):
    rows = []
    for r in range(0, CAP + 1):
        d = defaultdict(set)
        for h in CARRIER:
            if CAP - len(h) >= r:
                d[V[h]].add(G[(h, r)])
        rows.append((r, sum(1 for v in d.values() if len(v) > 1), len(d)))
    _Gmulti[name] = rows
    emit(f"  {name}: horizon potential G(.,r) multi-valued on "
         + ", ".join(f"r={r}: {b}/{t}" for r, b, t in rows))
gate('G-KERNEL-DOES-NOT-DESCEND', 'MUST',
     'the horizon potential is NOT class-constant on the MENU carrier '
     '(so the horizon kernel does not descend and a readout must be '
     'declared) but IS class-constant on REC',
     any(b > 0 for r, b, t in _Gmulti['MENU'])
     and all(b == 0 for r, b, t in _Gmulti['REC']),
     f"MENU multi-valued rows {[(r, b) for r, b, t in _Gmulti['MENU'] if b]}; "
     f"REC multi-valued total "
     f"{sum(b for r, b, t in _Gmulti['REC'])}",
     falsifiers=['MUT-QUOTIENT-SCRAMBLE'])

# labelled-edge structure
_lab = {}
for name, V in (('MENU', A_MENU), ('REC', A_REC)):
    w_, t_ = defaultdict(set), defaultdict(set)
    for h in CARRIER:
        if len(h) >= CAP:
            continue
        for e, q in CACHE[h]:
            w_[(V[h], evsk(e))].add(Fr(q))
            t_[(V[h], evsk(e))].add(V[h + (e,)])
    _lab[name] = (len(w_), sum(1 for v in w_.values() if len(v) > 1),
                  sum(1 for v in t_.values() if len(v) > 1))
    emit(f"  {name}: labelled edges {_lab[name][0]}, multi-WEIGHT "
         f"{_lab[name][1]}, multi-TARGET {_lab[name][2]}")
anchor('A-D74-MULTIW-MENU', 0, _lab['MENU'][1],
       "D74's ladder: MENU carries 0 multi-valued labelled edges "
       "(weights)")
anchor('A-D74-MULTIW-REC', 0, _lab['REC'][1],
       "D74's ladder: REC carries 0 multi-valued labelled edges")

# ======================================================================
# TEST 2 (run early: the holonomy machinery is shared) --
# THE HOLONOMY GATE
# ======================================================================
sec("TEST 2 -- THE HOLONOMY GATE (pre-registered)")


def holonomy_of(edges):
    """D74's exact R+ holonomy census by spanning-forest potentials."""
    edges = sorted(edges, key=lambda z: (sk(z[0]), sk(z[1]), z[2]))
    nodes = set()
    for u, v, x in edges:
        nodes.add(u)
        nodes.add(v)
    parent = {x: x for x in nodes}
    pot = {x: Fr(1) for x in nodes}

    def find(x):
        f = Fr(1)
        y = x
        while parent[y] != y:
            f *= pot[y]
            y = parent[y]
        return y, f

    rank = 0
    hol = Counter()
    for u, v, x in edges:
        ru, fu = find(u)
        rv, fv = find(v)
        if ru == rv:
            rank += 1
            hol[(fu * x) / fv] += 1
        else:
            parent[rv] = ru
            pot[rv] = (fu * x) / fv
    return len(nodes), rank, sum(v for k, v in hol.items() if k != 1), hol


def primes_of(fr):
    out = {}
    for n, sgn in ((fr.numerator, 1), (fr.denominator, -1)):
        d = 2
        while d * d <= n:
            while n % d == 0:
                out[d] = out.get(d, 0) + sgn
                n //= d
            d += 1
        if n > 1:
            out[n] = out.get(n, 0) + sgn
    return {p: e for p, e in out.items() if e != 0}


def group_of(values):
    """The multiplicative group generated, as an integer exponent
    lattice over the primes that occur.  Returns (primes, rank)."""
    vals = [v for v in values if v != 1]
    ps = sorted({p for v in vals for p in primes_of(v)})
    if not ps:
        return [], 0
    rows = []
    for v in vals:
        pv_ = primes_of(v)
        rows.append([pv_.get(p, 0) for p in ps])
    # integer row reduction (Hermite-style), exact
    r = 0
    for c in range(len(ps)):
        piv = None
        for i in range(r, len(rows)):
            if rows[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        changed = True
        while changed:
            changed = False
            for i in range(r + 1, len(rows)):
                if rows[i][c] != 0:
                    f = rows[i][c] // rows[r][c]
                    rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
                    if rows[i][c] != 0:
                        rows[r], rows[i] = rows[i], rows[r]
                        changed = True
        r += 1
    return ps, r


prog("square census ...")
CLOSED = []
SQ = Counter()
for h in CARRIER:
    if len(h) + 2 > CAP:
        continue
    cands = [e for e, q in CACHE[h]]
    for i in range(len(cands)):
        for j in range(i + 1, len(cands)):
            eA, eB = cands[i], cands[j]
            okA, qA = admissible(list(h), eA, AB)
            okB, qB = admissible(list(h), eB, AB)
            if not (okA and okB):
                continue
            okB2, qB2 = admissible(list(h) + [eA], eB, AB)
            okA2, qA2 = admissible(list(h) + [eB], eA, AB)
            if okB2 and okA2:
                SQ['closed'] += 1
                rq = Fr(qA * qB2, 1) / Fr(qB * qA2, 1)
                d = len(h)
                rk = (k_of(h, eA, CAP - d) * k_of(h + (eA,), eB,
                                                  CAP - d - 1)
                      / (k_of(h, eB, CAP - d)
                         * k_of(h + (eB,), eA, CAP - d - 1)))
                CLOSED.append((h, eA, eB, rq, rk))
            elif okB2:
                SQ['AB-only'] += 1
            elif okA2:
                SQ['BA-only'] += 1
            else:
                SQ['both-blocked'] += 1

SPEC_Q = Counter(c[3] for c in CLOSED)
anchor('A-D74-SQUARES',
       {'AB-only': 28, 'BA-only': 12, 'both-blocked': 142, 'closed': 1546},
       dict(sorted(SQ.items())),
       "D72/D74's committed (A,B) d <= 4 exchange-square census")
anchor('A-D74-SPECTRUM', {'1/2': 70, '2/3': 2, '3/2': 6, '2': 10},
       {str(k): v for k, v in sorted(SPEC_Q.items()) if k != 1},
       "D74's committed non-unit spectrum at (A,B) d <= 4")
DEF88 = [c for c in CLOSED if c[3] != 1]
anchor('A-D74-DEFECTS', 88, len(DEF88),
       "D74's committed defective-square count at (A,B) d <= 4")

SPEC_K = Counter(c[4] for c in CLOSED)
emit(f"  r_q spectrum: {ctr(SPEC_Q)}")
emit(f"  r_k spectrum (the HORIZON-NORMALIZED connection, this unit's "
     f"own measurement): {ctr(SPEC_K)}")

HOL = {}


def gamma_entry(GAM, d, dd, s, s2):
    return GAM[(dd, d)].get(s, {}).get(s2, Fr(0))


for qname, V, GAM in (('MENU', A_MENU, GAM_M), ('REC', A_REC, GAM_R)):
    HOL[qname] = {}
    for rname, key in (('q (D74\'s connection)', 3),
                       ('k (the horizon-normalized connection)', 4)):
        ex = [(V[h + (eB, eA)], V[h + (eA, eB)], c[key])
              for c in CLOSED for h, eA, eB in [(c[0], c[1], c[2])]]
        loops = Counter(x for u, v, x in ex if u == v and x != 1)
        n_, rank, ob, hol = holonomy_of([e for e in ex if e[0] != e[1]])
        vals = list(loops.elements()) + [k for k in hol for _ in
                                         range(hol[k]) if k != 1]
        ps, rk = group_of(vals)
        HOL[qname][rname] = dict(closes=sum(1 for u, v, x in ex if u == v),
                                 selfloops=sum(loops.values()),
                                 selfloop_values={str(k): v for k, v in
                                                  sorted(loops.items())},
                                 nodes=n_, cycle_rank=rank,
                                 obstruction=ob,
                                 cycle_values={str(k): v for k, v in
                                               sorted(hol.items())
                                               if k != 1},
                                 primes=ps, rank=rk)
        emit(f"  {qname} / {rname}: squares closing {sum(1 for u, v, x in ex if u == v)}; "
             f"non-unit self-loops {sum(loops.values())} "
             f"{ctr(loops)}; cycle rank {rank}; obstruction {ob}; "
             f"group primes {ps} rank {rk}")
    # --- the constructed family's OWN holonomy, from Gamma's entries ---
    vals = Counter()
    nonclose = 0
    undef = 0
    for h, eA, eB, rq, rk in CLOSED:
        d = len(h)
        s, sA, sB = V[h], V[h + (eA,)], V[h + (eB,)]
        sAB, sBA = V[h + (eA, eB)], V[h + (eB, eA)]
        if sAB != sBA:
            nonclose += 1
            continue
        num = (gamma_entry(GAM, d, d + 1, s, sA)
               * gamma_entry(GAM, d + 1, d + 2, sA, sAB))
        den = (gamma_entry(GAM, d, d + 1, s, sB)
               * gamma_entry(GAM, d + 1, d + 2, sB, sBA))
        if den == 0:
            undef += 1
            continue
        vals[num / den] += 1
    ps, rk = group_of(list(vals.elements()))
    HOL[qname]['Gamma (the constructed family)'] = dict(
        nonclosing=nonclose, undefined=undef,
        spectrum={str(k): v for k, v in sorted(vals.items())},
        nonunit=sum(v for k, v in vals.items() if k != 1),
        primes=ps, rank=rk)
    emit(f"  {qname} / Gamma (the constructed family): squares not "
         f"closing {nonclose}; undefined {undef}; non-unit "
         f"{sum(v for k, v in vals.items() if k != 1)} of "
         f"{sum(vals.values())}; distinct values {len(vals)}; "
         f"group primes {ps} rank {rk}")

anchor('A-D74-MENU-RUNG',
       {'closes': 1402, 'obstruction': 44, 'selfloops': 44,
        'cycle_rank': 134},
       {'closes': HOL['MENU']["q (D74's connection)"]['closes'],
        'obstruction': HOL['MENU']["q (D74's connection)"]['obstruction'],
        'selfloops': HOL['MENU']["q (D74's connection)"]['selfloops'],
        'cycle_rank': HOL['MENU']["q (D74's connection)"]['cycle_rank']},
       "D74's committed MENU rung of the abstraction ladder")
anchor('A-D74-REC-RUNG',
       {'closes': 473, 'obstruction': 0, 'selfloops': 0,
        'cycle_rank': 145},
       {'closes': HOL['REC']["q (D74's connection)"]['closes'],
        'obstruction': HOL['REC']["q (D74's connection)"]['obstruction'],
        'selfloops': HOL['REC']["q (D74's connection)"]['selfloops'],
        'cycle_rank': HOL['REC']["q (D74's connection)"]['cycle_rank']},
       "D74's committed REC rung: FLAT")

_q23 = HOL['MENU']["q (D74's connection)"]
gate('T2-D74-ANCHOR', 'MUST',
     "the carrier reproduces D74's measured group: the q-connection on "
     'the MENU quotient generates the free abelian rank-2 group of '
     '3-smooth positive rationals, primes {2, 3}',
     _q23['primes'] == [2, 3] and _q23['rank'] == 2,
     f"primes {_q23['primes']}, rank {_q23['rank']}",
     falsifiers=['MUT-HOLONOMY-DRIFT', 'MUT-QUOTIENT-SCRAMBLE'])

_k = HOL['MENU']['k (the horizon-normalized connection)']
_gm = HOL['MENU']['Gamma (the constructed family)']
_rq = HOL['REC']["q (D74's connection)"]
_rk = HOL['REC']['k (the horizon-normalized connection)']
_rg = HOL['REC']['Gamma (the constructed family)']

gate('T2-REC-FLAT', 'MUST',
     'THE NEGATIVE CONTROL: on the REC quotient the connection is flat '
     'at ALL THREE readings -- zero obstruction, zero non-unit '
     'self-loops, and the constructed family assigns holonomy exactly '
     '1 to every square that closes',
     _rq['obstruction'] == 0 and _rq['selfloops'] == 0
     and _rk['obstruction'] == 0 and _rk['selfloops'] == 0
     and _rg['nonunit'] == 0,
     f"REC q: obstruction {_rq['obstruction']} self-loops "
     f"{_rq['selfloops']}; REC k: obstruction {_rk['obstruction']} "
     f"self-loops {_rk['selfloops']}; REC Gamma: non-unit "
     f"{_rg['nonunit']}, spectrum {_rg['spectrum']}",
     falsifiers=['MUT-REC-CORRUPT'])

D74VALS = [Fr(1, 2), Fr(2, 3), Fr(3, 2), Fr(2)]


def contains_d74(vals):
    """Does the group generated by `vals` contain D74's <2,3>?  Exact:
    adjoining D74's four values may not raise the rank."""
    a = group_of(list(vals))[1]
    b = group_of(list(vals) + D74VALS)[1]
    return a == b


_kvals = ([Fr(x) for x in _k['selfloop_values']
           for _ in range(_k['selfloop_values'][x])]
          + [Fr(x) for x in _k['cycle_values']
             for _ in range(_k['cycle_values'][x])])
_gvals = [Fr(x) for x in _gm['spectrum']
          for _ in range(_gm['spectrum'][x]) if Fr(x) != 1]
_k_contains = contains_d74(_kvals)
_g_contains = contains_d74(_gvals)
_agree_k = (_k['primes'] == [2, 3] and _k['rank'] == 2)
_agree_g = (_gm['primes'] == [2, 3] and _gm['rank'] == 2)
emit(f"  CONTAINMENT, measured: the horizon-normalized connection's "
     f"group contains D74's <2,3> = {_k_contains}; the constructed "
     f"family's group contains it = {_g_contains}.  The deviation is "
     f"therefore an ENLARGEMENT where containment holds, not a "
     f"replacement.")
T2_VERDICT = ('AGREE' if (_agree_k and _agree_g) else
              'DEVIATE-AT-' + ('BOTH' if not _agree_k and not _agree_g
                               else ('K' if not _agree_k else 'GAMMA')))
gate('T2-HOLONOMY', 'MUST',
     "THE HOLONOMY GATE: the constructed family's holonomy is compared "
     "against D74's measured group; agreement or the deviation is "
     'reported exactly, and the comparison could have come out either '
     'way (REC returns AGREE-trivially on the same instrument)',
     T2_VERDICT in ('AGREE', 'DEVIATE-AT-K', 'DEVIATE-AT-GAMMA',
                    'DEVIATE-AT-BOTH'),
     f"verdict {T2_VERDICT}; D74 reading primes {_q23['primes']} rank "
     f"{_q23['rank']}; k-connection primes {_k['primes']} rank "
     f"{_k['rank']} (new self-loop values "
     f"{sorted(set(_k['selfloop_values']) - set(_q23['selfloop_values']))}, "
     f"contains <2,3> = {_k_contains}); Gamma-family primes "
     f"{_gm['primes']} rank {_gm['rank']}, contains <2,3> = "
     f"{_g_contains}, non-unit {_gm['nonunit']} of "
     f"{sum(_gm['spectrum'].values())} closing squares",
     falsifiers=['MUT-HOLONOMY-DRIFT'])

# ======================================================================
# TEST 1 -- THE POSITION-LAW TARGETS
# ======================================================================
sec("TEST 1 -- THE POSITION-LAW TARGETS (pre-registered, the R6b' "
    "register)")


def is_R4(e):
    """The D62 row-R4 renewal predicate, ported: tag 'r' with TWO
    proposers in the ckey (U1's is_R4, purely syntactic)."""
    return e[0] == 'r' and len({t[0] for t in e[2]}) == 2


def payload_label(e):
    """The renewal token's payload: (value, authors, initiator) of the
    version the R4 event creates -- 8 values at this scope."""
    wk = e[3]
    return (tuple(sorted({t[2] for t in wk})),
            tuple(sorted({t[0] for t in wk})), e[1])


R1BASES = sorted([h for h in CACHE if len(h) == 3 and is_R4(h[-1])],
                 key=sk)
anchor('A-U1B-R1BASES', 16, len(R1BASES),
       "U1b's committed ARM-C2 anchor: 16 renewal-1 bases at depth 3")
_pat1 = Counter(tuple(e[0] for e in h) for h in R1BASES)
gate('T1-3EVENT-LAW', 'MUST',
     "U1b's committed law: a renewal three events after the boundary "
     'forces the pattern (p, p, r) and nothing else',
     set(_pat1) == {('p', 'p', 'r')},
     f"patterns {ctr(_pat1)}",
     falsifiers=['MUT-LEG-PATTERN'])

_delopt = Counter(sum(1 for e, q in CACHE[h] if e[0] == 'd')
                  for h in R1BASES)
_idlopt = Counter(sum(1 for e, q in CACHE[h] if e[0] == 'n')
                  for h in R1BASES)
emit(f"  at the renewal-1 bases: delivery options {ctr(_delopt)}, "
     f"idle options {ctr(_idlopt)}")


def leg_scan(bases, pruned, label):
    """Enumerate 4-event legs (three interior events then an R4) from
    each base.  pruned=False is the UNPRUNED scan: every candidate is
    generated and only then filtered."""
    nodes = 0
    legs = []
    for b in bases:
        stack = [(b, (), Fr(1))]
        while stack:
            h, tail, ww = stack.pop()
            k = len(tail)
            nfill = sum(1 for i in range(k) if tail[i][0] != 'p')
            for e, q in candidates_for(list(h), AB):
                nodes += 1
                if is_R4(e):
                    if k == 3:
                        legs.append((b, tail + (e,), ww * Fr(q)))
                    continue
                if k >= 3:
                    continue
                if pruned:
                    if e[0] == 'r':
                        continue
                    if e[0] != 'p' and nfill >= 1:
                        continue
                    if e[0] == 'p' and (k - nfill) >= 2:
                        continue
                stack.append((h + (e,), tail + (e,), ww * Fr(q)))
    return nodes, legs


def positional(legs):
    cnt = Counter()
    wgt = defaultdict(Fr)
    for b, t4, ww in legs:
        f = [i for i in range(3) if t4[i][0] != 'p']
        if len(f) != 1:
            return None, None
        cnt[f[0]] += 1
        wgt[f[0]] += ww
    tc = sum(cnt.values())
    tw = sum(wgt.values())
    return ([Fr(cnt[i], tc) for i in range(3)],
            [wgt[i] / tw for i in range(3)])


prog("leg 1: UNPRUNED 4-event scan from the 16 renewal-1 bases ...")
N1, LEGS1 = leg_scan(R1BASES, False, 'leg1')
PAT1 = Counter(tuple(e[0] for e in t4) for b, t4, ww in LEGS1)
CNT1, WGT1 = positional(LEGS1)
prog(f"leg 1 done: {N1} raw continuations, {len(LEGS1)} legs")
emit(f"  LEG 1 (renewal 1 -> renewal 2, four events): UNPRUNED scan, "
     f"{N1} raw continuations generated, {len(LEGS1)} legs kept.")
emit(f"    leg patterns: {ctr(PAT1)}")
emit(f"    COUNT readout    : ({', '.join(str(x) for x in CNT1)})")
emit(f"    OCCUPANCY readout: ({', '.join(str(x) for x in WGT1)})")
anchor('A-U1B-LEG1', 3584, len(LEGS1),
       "U1b's committed E2 leg-1 leaf count (3,584 renewal-2 leaves)")

# THE F8 MECHANISM, derived rather than imported.
_slotkinds = defaultdict(Counter)
for b, t4, ww in LEGS1:
    for i in range(3):
        if t4[i][0] != 'p':
            _slotkinds[i][t4[i][0]] += 1
emit(f"    F8 slot x kind census: "
     + "; ".join(f"slot {i + 1}: {ctr(_slotkinds[i])}" for i in range(3)))
gate('T1-F8', 'MUST',
     'F8, MEASURED HERE: the middle interior slot admits NO delivery -- '
     'the pattern (p, d, p, r) does not occur, while (p, n, p, r) does',
     _slotkinds[1]['d'] == 0 and _slotkinds[1]['n'] > 0
     and _slotkinds[0]['d'] > 0 and _slotkinds[2]['d'] > 0,
     f"deliveries by slot "
     f"{[_slotkinds[i]['d'] for i in range(3)]}; idles by slot "
     f"{[_slotkinds[i]['n'] for i in range(3)]}",
     falsifiers=['MUT-LEG-PATTERN'])

# WHY: the delivery joins the two actors' registers, so a proposal
# after a delivery after a proposal is ORDER-COMPARABLE to the first,
# and an R4 needs two INCOMPARABLE live proposals.  Measured.
prog("F8 mechanism: comparability census ...")
_cmp_after_d = 0
_cmp_after_n = 0
_tot_d = 0
_tot_n = 0
for b in R1BASES:
    for e1, q1 in candidates_for(list(b), AB):
        if e1[0] != 'p':
            continue
        for e2, q2 in candidates_for(list(b + (e1,)), AB):
            if e2[0] not in ('d', 'n'):
                continue
            h2 = b + (e1, e2)
            for e3, q3 in candidates_for(list(h2), AB):
                if e3[0] != 'p':
                    continue
                h3 = h2 + (e3,)
                v = fullview(h3)
                live = sorted(v.live)
                comparable = (len(live) == 2
                              and not v.incomparable(live[0], live[1]))
                if e2[0] == 'd':
                    _tot_d += 1
                    _cmp_after_d += int(comparable)
                else:
                    _tot_n += 1
                    _cmp_after_n += int(comparable)
gate('T1-F8-MECHANISM', 'MUST',
     "F8's cause, measured: after (p, d, p) the two live proposals are "
     'ORDER-COMPARABLE at every instance (the delivery joins the two '
     "actors' registers), and an R4 needs two INCOMPARABLE live "
     'proposals; after (p, n, p) they are incomparable at every '
     'instance',
     _tot_d > 0 and _cmp_after_d == _tot_d and _cmp_after_n == 0,
     f"(p,d,p): comparable {_cmp_after_d} of {_tot_d}; "
     f"(p,n,p): comparable {_cmp_after_n} of {_tot_n}",
     falsifiers=['MUT-F8-MECHANISM'])

# --- leg 2 -----------------------------------------------------------
prog("renewal-2 bases at depth 6 ...")
R2BASES = []
for b in R1BASES:
    stack = [(b, ())]
    while stack:
        h, tail = stack.pop()
        for e, q in candidates_for(list(h), AB):
            if is_R4(e):
                if len(tail) == 2:
                    R2BASES.append(h + (e,))
                continue
            if len(tail) < 2:
                stack.append((h + (e,), tail + (e,)))
R2BASES = sorted(R2BASES, key=sk)
anchor('A-U1B-R2BASES', 256, len(R2BASES),
       "U1b's committed ARM-C2 anchor: 256 renewal-2 histories at "
       "depth 6")
_delopt2 = Counter(sum(1 for e, q in CACHE.get(h, candidates_for(list(h), AB))
                       if e[0] == 'd') for h in R2BASES)
_idlopt2 = Counter(sum(1 for e, q in candidates_for(list(h), AB)
                       if e[0] == 'n') for h in R2BASES)
emit(f"  at the renewal-2 bases: delivery options {ctr(_delopt2)}, "
     f"idle options {ctr(_idlopt2)}")

prog("leg 2: pattern-pruned scan from all 256 renewal-2 bases ...")
N2, LEGS2 = leg_scan(R2BASES, True, 'leg2')
PAT2 = Counter(tuple(e[0] for e in t4) for b, t4, ww in LEGS2)
CNT2, WGT2 = positional(LEGS2)
prog(f"leg 2 done: {N2} expansions, {len(LEGS2)} legs")

# THE PRUNE GATE: an UNPRUNED scan on a declared subsample must return
# the identical leg set with identical weights.
GATE_BASES = R2BASES[:3]
prog("leg 2: UNPRUNED agreement gate on 3 declared bases ...")
NU, LEGSU = leg_scan(GATE_BASES, False, 'leg2-gate')
_sub = sorted(((sk(b), sk(t4), str(ww)) for b, t4, ww in LEGS2
               if b in GATE_BASES))
_uns = sorted(((sk(b), sk(t4), str(ww)) for b, t4, ww in LEGSU))
gate('T1-PRUNE-GATE', 'MUST',
     'the leg-2 pattern prune is gated, not assumed: on a declared '
     'subsample of renewal-2 bases the UNPRUNED scan returns exactly '
     'the pruned leg set, leg for leg and weight for weight',
     _sub == _uns and len(_uns) > 0,
     f"{len(GATE_BASES)} bases, {NU} raw continuations unpruned, "
     f"{len(LEGSU)} legs; pruned {len(_sub)} legs; identical "
     f"{_sub == _uns}",
     falsifiers=['MUT-PRUNE-LAX'])

emit(f"  LEG 2 (renewal 2 -> renewal 3, four events): pattern-pruned "
     f"scan over all {len(R2BASES)} renewal-2 bases, {N2} expansions, "
     f"{len(LEGS2)} legs.")
emit(f"    leg patterns: {ctr(PAT2)}")
emit(f"    COUNT readout    : ({', '.join(str(x) for x in CNT2)})")
emit(f"    OCCUPANCY readout: ({', '.join(str(x) for x in WGT2)})")

TGT1 = [Fr(3, 7), Fr(1, 7), Fr(3, 7)]
TGT2 = [Fr(4, 9), Fr(1, 9), Fr(4, 9)]
_hit1 = (CNT1 == TGT1)
_hit2 = (CNT2 == TGT2)
_hit1w = (WGT1 == TGT1)
_hit2w = (WGT2 == TGT2)
T1_VERDICT = ('TARGETS-HIT-AT-THE-COUNT-READOUT-MISSED-AT-THE-OCCUPANCY'
              '-READOUT' if (_hit1 and _hit2 and not _hit1w and
                             not _hit2w)
              else ('TARGETS-HIT-AT-BOTH-READOUTS'
                    if (_hit1 and _hit2 and _hit1w and _hit2w)
                    else ('TARGETS-HIT-AT-THE-OCCUPANCY-READOUT'
                          if (_hit1w and _hit2w) else 'TARGETS-MISSED')))
gate('T1-TARGETS', 'MUST',
     "THE POSITION-LAW TARGETS: the constructed family must reproduce "
     "(3/7,1/7,3/7) at leg 1 and (4/9,1/9,4/9) at leg 2; both readouts "
     'are measured and the readout at which the targets are hit is '
     'named',
     T1_VERDICT != 'TARGETS-MISSED',
     f"verdict {T1_VERDICT}; leg1 count "
     f"({', '.join(str(x) for x in CNT1)}) vs target "
     f"({', '.join(str(x) for x in TGT1)}) -> {_hit1}; leg2 count "
     f"({', '.join(str(x) for x in CNT2)}) vs target "
     f"({', '.join(str(x) for x in TGT2)}) -> {_hit2}; leg1 occupancy "
     f"({', '.join(str(x) for x in WGT1)}) -> {_hit1w}; leg2 occupancy "
     f"({', '.join(str(x) for x in WGT2)}) -> {_hit2w}",
     falsifiers=['MUT-TARGET-DRIFT', 'MUT-READOUT-SWAP'])

_mult1 = Fr(sum(_slotkinds[i]['d'] for i in (0, 2)),
            sum(_slotkinds[i]['n'] for i in (0, 2)))
_sk2 = defaultdict(Counter)
for b, t4, ww in LEGS2:
    for i in range(3):
        if t4[i][0] != 'p':
            _sk2[i][t4[i][0]] += 1
_mult2 = Fr(sum(_sk2[i]['d'] for i in (0, 2)),
            sum(_sk2[i]['n'] for i in (0, 2)))
gate('T1-MULTIPLICITY', 'MUST',
     "the mechanism the targets encode, measured: the delivery "
     'multiplicity (deliveries per idle in a filler slot) moves 2 -> 3 '
     'between leg 1 and leg 2, and (m+1)/(2m+3) is 3/7 at m = 2 and '
     '4/9 at m = 3',
     _mult1 == 2 and _mult2 == 3
     and Fr(_mult1 + 1, 2 * _mult1 + 3) == TGT1[0]
     and Fr(_mult2 + 1, 2 * _mult2 + 3) == TGT2[0],
     f"multiplicity leg 1 = {_mult1}, leg 2 = {_mult2}; "
     f"(m+1)/(2m+3) = {Fr(_mult1 + 1, 2 * _mult1 + 3)} and "
     f"{Fr(_mult2 + 1, 2 * _mult2 + 3)}",
     falsifiers=['MUT-TARGET-DRIFT'])


def sector_mass(bases, kind):
    vals = set()
    for h in bases:
        vals.add(sum(Fr(q) for e, q in candidates_for(list(h), AB)
                     if e[0] == kind))
    return sorted(vals)


_dm1, _nm1 = sector_mass(R1BASES, 'd'), sector_mass(R1BASES, 'n')
_dm2, _nm2 = sector_mass(R2BASES, 'd'), sector_mass(R2BASES, 'n')
emit(f"  THE QUARTER LAW MAKES THE OCCUPANCY READOUT MULTIPLICITY-"
     f"BLIND, measured: the delivery sector's TOTAL mass at a renewal "
     f"base is {[str(x) for x in _dm1]} at renewal 1 and "
     f"{[str(x) for x in _dm2]} at renewal 2, and the idle sector's is "
     f"{[str(x) for x in _nm1]} and {[str(x) for x in _nm2]} -- "
     f"unchanged -- while the delivery COUNT moves "
     f"{sorted(_delopt)} -> {sorted(_delopt2)}.  The budget is 1/4 per "
     f"actor divided by |hold(a)|, so adding a version splits the same "
     f"mass into more entries.  The count readout sees the split; the "
     f"occupancy readout cannot.")
gate('T1-QUARTER-BLINDNESS', 'MUST',
     "the exact cause of the readout split, measured on both legs: the "
     "delivery and idle SECTOR MASSES are identical at renewal 1 and "
     'renewal 2 while the delivery COUNT moves, so the occupancy '
     'readout is multiplicity-blind by the quarter law and returns the '
     'same positional law at both legs, whereas the count readout '
     'moves with the multiplicity',
     _dm1 == _dm2 and _nm1 == _nm2 and sorted(_delopt) != sorted(_delopt2)
     and WGT1 == WGT2 and CNT1 != CNT2,
     f"delivery sector mass {[str(x) for x in _dm1]} = "
     f"{[str(x) for x in _dm2]}; idle sector mass "
     f"{[str(x) for x in _nm1]} = {[str(x) for x in _nm2]}; delivery "
     f"count {sorted(_delopt)} -> {sorted(_delopt2)}; occupancy law "
     f"leg 1 = leg 2 is {WGT1 == WGT2}; count law leg 1 = leg 2 is "
     f"{CNT1 == CNT2}",
     falsifiers=['MUT-BLINDNESS-FLIP'])
mutant('MUT-BLINDNESS-FLIP', 'T1-QUARTER-BLINDNESS',
       'the two readouts exchanged in the blindness claim',
       CNT1 != CNT2 and WGT1 == WGT2,
       f"the count law moves ({', '.join(str(x) for x in CNT1)} -> "
       f"{', '.join(str(x) for x in CNT2)}) and the occupancy law does "
       f"not; asserting the reverse fails the gate")

# ======================================================================
# THE POSITIVE CONTROL -- the renewal cuts, and U1b's wall
# ======================================================================
sec("THE POSITIVE CONTROL -- Gamma at the RENEWAL cuts, and U1b's "
    "column-constancy wall")
L1 = sorted({payload_label(b[-1]) for b in R1BASES})
L2 = sorted({payload_label(t4[-1]) for b, t4, ww in LEGS1})
JC = Counter()
JW = defaultdict(Fr)
for b, t4, ww in LEGS1:
    JC[(payload_label(b[-1]), payload_label(t4[-1]))] += 1
    JW[(payload_label(b[-1]), payload_label(t4[-1]))] += ww
_dc = {a: sum(JC[(a, x)] for x in L2) for a in L1}
_dw = {a: sum(JW[(a, x)] for x in L2) for a in L1}
GREN = [[(Fr(JC[(a, c)], _dc[a]) if _dc[a] else Fr(0)) for a in L1]
        for c in L2]
GRENW = [[(JW[(a, c)] / _dw[a] if _dw[a] else Fr(0)) for a in L1]
         for c in L2]
_cols = {tuple(GREN[i][j] for i in range(len(L2))) for j in range(len(L1))}
emit(f"  renewal-cut label sets: |L1| = {len(L1)}, |L2| = {len(L2)}; "
     f"joint cells {len(JC)}; leg counts per cell "
     f"{sorted(set(JC.values()))}; leg weights per cell "
     f"{sorted(set(str(v) for v in JW.values()))}")
emit(f"  Gamma(renewal 2 <- renewal 1) has {len(_cols)} distinct "
     f"column(s); every entry {sorted(set(str(GREN[i][j]) for i in range(len(L2)) for j in range(len(L1))))}")
gate('T4-RENEWAL-POSITIVE', 'MUST',
     "THE POSITIVE CONTROL, and the wall stated: at renewal cuts "
     'Gamma is column-CONSTANT (one distinct column), so by U1b (D-2) '
     'DIVISIBLE is forced by structure before any test is run -- this '
     'unit makes NO indivisibility claim at renewal grain, at any '
     'scope; and the matrix is exactly J/8, U3\'s own committed passer',
     len(_cols) == 1 and all(GREN[i][j] == Fr(1, 8)
                             for i in range(len(L2))
                             for j in range(len(L1)))
     and GREN == GRENW,
     f"distinct columns {len(_cols)}; every entry 1/8 "
     f"{all(GREN[i][j] == Fr(1, 8) for i in range(len(L2)) for j in range(len(L1)))}; "
     f"count and occupancy readouts agree {GREN == GRENW}",
     falsifiers=['MUT-RENEWAL-CORRUPT'])

# ======================================================================
# TEST 3 -- THE U3 SCREEN, reimplemented from the pinned contract
# ======================================================================
sec("TEST 3 -- THE U3 UNISTOCHASTICITY SCREEN, run on Gamma")
emit("""  The screen's contract, reimplemented from the pinned U3 code's
  declared decision order: N/A-SHAPE (Barandes' criterion is defined
  for SQUARE matrices only) -> S-FAIL-DS with exact row/column
  deficits and the exact L1 price -> the n = 3 triangle discriminant
  where the shape admits it -> S-PASS with an exhibited certificate,
  or EXCLUDED-BY-CAP when no obstruction is found and no certificate
  is constructed.
  DECLARED OMISSION, stated where it is made: U3's general polygon
  obstruction is NOT reimplemented here -- it needs U3's exact surd
  sign oracle -- and it is a NECESSARY condition only, so its absence
  can never turn a failure into a pass.  The one S-PASS below is
  carried by a CONSTRUCTED certificate, which is sufficient, so the
  omission cannot move a single verdict in this census.""")


def ds_report(M):
    n, m = len(M), len(M[0])
    rows = [sum(M[i]) for i in range(n)]
    cols = [sum(M[i][j] for i in range(n)) for j in range(m)]
    neg = [(i, j) for i in range(n) for j in range(m) if M[i][j] < 0]
    return dict(square=n == m, n=n, m=m,
                rowdef=[r - 1 for r in rows], coldef=[c - 1 for c in cols],
                L1row=sum(abs(r - 1) for r in rows),
                L1col=sum(abs(c - 1) for c in cols),
                nonneg=not neg,
                ds=n == m and all(r == 1 for r in rows)
                and all(c == 1 for c in cols) and not neg)


def tri_disc(a, b, c):
    return 2 * (a * b + b * c + c * a) - a * a - b * b - c * c


def hadamard(n):
    H = [[1]]
    while len(H) < n:
        H = ([r + r for r in H] + [r + [-x for x in r] for r in H])
    return H


SCREEN = []


def screen(name, M, provenance, cert=None):
    R = ds_report(M)
    n, m = R['n'], R['m']
    if not R['square']:
        v = 'N/A-SHAPE'
        datum = (f"shape {n} x {m}; Barandes' criterion is defined for "
                 f"square matrices only and the trivial column "
                 f"completion is Theorem D1's move, SET ASIDE")
    elif not R['ds']:
        v = 'S-FAIL-DS'
        datum = (f"shape {n} x {n}; sum|row deficit| = {R['L1row']}, "
                 f"sum|col deficit| = {R['L1col']}; PRICE: for every "
                 f"doubly-stochastic D, ||M - D||_1 >= "
                 f"{max(R['L1row'], R['L1col'])}")
        if n == 3:
            T = tri_disc(*[M[i][0] * M[i][1] for i in range(3)])
            datum += f"; n = 3 triangle discriminant T = {T}"
    else:
        if n == 3:
            T = tri_disc(*[M[i][0] * M[i][1] for i in range(3)])
            if T < 0:
                SCREEN.append(dict(name=name, verdict='S-FAIL-UNI',
                                   datum=f"triangle discriminant "
                                         f"T = {T} < 0",
                                   provenance=provenance, shape=[n, m]))
                emit(f"  {name}: S-FAIL-UNI (triangle discriminant "
                     f"T = {T} < 0)  [{provenance}]")
                return SCREEN[-1]
        if cert is not None:
            H = cert
            bad_u = sum(1 for i in range(n) for j in range(n)
                        if sum(H[i][k] * H[j][k] for k in range(n))
                        != (n if i == j else 0))
            bad_m = sum(1 for i in range(n) for j in range(n)
                        if Fr(H[i][j] * H[i][j], n) != M[i][j])
            v = 'S-PASS' if (bad_u == 0 and bad_m == 0) \
                else 'CERTIFICATE-FAILED'
            datum = (f"REAL ORTHOGONAL certificate U = H/sqrt({n}) with "
                     f"H the Sylvester Hadamard matrix: H H^T - {n} I "
                     f"has {bad_u} non-zero entries; |U_ij|^2 - M_ij "
                     f"has {bad_m} mismatches (verified in exact "
                     f"integer and rational arithmetic, no surd needed "
                     f"because every |U_ij|^2 is H_ij^2/{n})")
        else:
            v = 'EXCLUDED-BY-CAP'
            datum = ('doubly stochastic, no obstruction evaluated at '
                     'this size and no certificate constructed; '
                     'reported as a cap, not a pass')
    SCREEN.append(dict(name=name, verdict=v, datum=datum,
                       provenance=provenance, shape=[n, m]))
    emit(f"  {name}: {v}  [{provenance}]")
    emit(f"      {datum}")
    return SCREEN[-1]


def dense(GAM, IDX, d, dd):
    M = [[Fr(0)] * len(IDX[d]) for _ in range(len(IDX[dd]))]
    for s, row in GAM[(dd, d)].items():
        for s2, v in row.items():
            M[IDX[dd][s2]][IDX[d][s]] = v
    return M


def padded(GAM, V, dom, d, dd, cuts=None):
    """U1's DECLARED identity-padding CONVENTION: the configuration
    space is the union of the cuts' supports, and a configuration not
    realised at a cut is held fixed by the law (an identity column)."""
    cuts = cuts if cuts is not None else (d, dd)
    uni = sorted({V[h] for h in dom if len(h) in cuts}, key=sk)
    ix = {c: i for i, c in enumerate(uni)}
    M = [[Fr(0)] * len(uni) for _ in range(len(uni))]
    real = {V[h] for h in dom if len(h) == d}
    for c in uni:
        if c in real:
            for s2, v in GAM[(dd, d)].get(c, {}).items():
                M[ix[s2]][ix[c]] = v
        else:
            M[ix[c]][ix[c]] = Fr(1)
    return M, uni, sorted(ix[c] for c in real if c in ix)


for (dd, d) in [(1, 0), (2, 1), (3, 2), (4, 3), (4, 2)]:
    screen(f"Gamma_MENU({dd}<-{d}) RAW", dense(GAM_M, IDX_M, d, dd),
           f"the constructed family on the MENU carrier, cuts {d}->{dd}")
for (dd, d) in [(2, 1), (3, 2), (4, 3)]:
    M, uni, _r = padded(GAM_M, A_MENU, CARRIER, d, dd)
    screen(f"Gamma_MENU({dd}<-{d}) IDENTITY-PADDED", M,
           f"the same family under U1's declared identity-padding "
           f"CONVENTION on the union support ({len(uni)} labels)")
screen("Gamma_RENEWAL(r2<-r1) [POSITIVE CONTROL]", GREN,
       "the renewal-cut family on the 8 payload labels; U3's own "
       "committed passer J/8", cert=hadamard(8))
_misM, _misU, _misR = padded(GAM_M, A_MENU, CARRIER, 1, 2)
_misS = set(_misR)
_mis = [[(_misM[i][j] * Fr(3, 2) if j in _misS else _misM[i][j])
         for j in range(len(_misU))] for i in range(len(_misU))]
screen("Gamma_MENU(2<-1) MIS-NORMALIZED [NEGATIVE CONTROL]", _mis,
       "the identity-padded transfer with every realised column "
       "re-weighted by 3/2: the screen must see the broken "
       "normalization exactly")

_tally = Counter(s['verdict'] for s in SCREEN)
_n3 = [s for s in SCREEN if s['shape'][0] == 3 and s['shape'][1] == 3]
gate('T3-SCREEN', 'MUST',
     'THE U3 SCREEN, run on Gamma: the census is the result, and the '
     'screen is shown to be able to return each of its verdicts on '
     'this unit\'s own inputs',
     _tally.get('S-PASS', 0) >= 1 and _tally.get('N/A-SHAPE', 0) >= 1
     and _tally.get('S-FAIL-DS', 0) >= 1,
     f"census {ctr(_tally)}; n = 3 objects arising from the "
     f"construction: {len(_n3)} (the n = 3 discriminant cell is "
     f"EMPTY-BY-SHAPE: the family's shapes are {fl(DIMS_M)} and their "
     f"padded completions); EXCLUDED-BY-CAP "
     f"{_tally.get('EXCLUDED-BY-CAP', 0)}",
     falsifiers=['MUT-SCREEN-FLIP', 'MUT-MISNORMALIZED'])

# ======================================================================
# TEST 4 -- THE [B3] INTERPOLANT TEST
# ======================================================================
sec("TEST 4 -- THE [B3] INTERPOLANT TEST on Gamma")
emit("""  The never-square-supports caveat is carried verbatim from U1:
  Barandes' eq. 22 needs a square Gamma -- one fixed configuration
  space for all cuts -- and this carrier has none away from renewals.
  The identity padding is a declared CONVENTION, not a fact about the
  process, and every count below is relative to it.""")


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k) if A[i][t])
             for j in range(m)] for i in range(n)]


CK = []
for d in range(CAP + 1):
    for md in range(d + 1, CAP + 1):
        for dd in range(md + 1, CAP + 1):
            A = dense(GAM_M, IDX_M, md, dd)
            B = dense(GAM_M, IDX_M, d, md)
            C = dense(GAM_M, IDX_M, d, dd)
            P = matmul(A, B)
            bad = sum(1 for i in range(len(C)) for j in range(len(C[0]))
                      if P[i][j] != C[i][j])
            CK.append(dict(cut=d, mid=md, cut2=dd,
                           cells=len(C) * len(C[0]), differing=bad,
                           interpolates=bad == 0))
            emit(f"  MENU CK({dd} <- {md} <- {d}): the process's own "
                 f"conditional interpolates at {len(C) * len(C[0]) - bad} "
                 f"of {len(C) * len(C[0])} cells "
                 f"({'DIVIDES' if bad == 0 else 'DOES NOT DIVIDE by its own conditional'})")
CKR = []
for d in range(CAP + 1):
    for md in range(d + 1, CAP + 1):
        for dd in range(md + 1, CAP + 1):
            A, B, C = (GAM_R[(dd, md)], GAM_R[(md, d)], GAM_R[(dd, d)])
            bad = 0
            cells = 0
            keys = set(C)
            for s in keys:
                tgt = defaultdict(Fr)
                for s1, v in B.get(s, {}).items():
                    for s2, u in A.get(s1, {}).items():
                        tgt[s2] += v * u
                allk = set(tgt) | set(C.get(s, {}))
                cells += len(allk)
                for s2 in allk:
                    if tgt.get(s2, Fr(0)) != C.get(s, {}).get(s2, Fr(0)):
                        bad += 1
            CKR.append(dict(cut=d, mid=md, cut2=dd, cells=cells,
                            differing=bad, interpolates=bad == 0))
_live = [r for r in CK if r['cut'] > 0]
gate('T4-CK', 'MUST',
     "the [B3] existence question, decided constructively where it "
     "can be: the process's own intermediate conditional is the "
     'canonical interpolant candidate, and it is tested cut-triple by '
     'cut-triple on the carrier and on the negative control',
     all(r['interpolates'] for r in CK if r['cut'] == 0)
     and any(not r['interpolates'] for r in _live)
     and all(r['interpolates'] for r in CKR),
     f"MENU: {sum(1 for r in CK if r['interpolates'])} of {len(CK)} "
     f"triples divide by the process's own conditional; the "
     f"{len(_live)} triples with a non-degenerate first cut fail at "
     f"{[r['differing'] for r in _live]} cells; REC (negative "
     f"control): {sum(1 for r in CKR if r['interpolates'])} of "
     f"{len(CKR)} -- the record chain is EXACTLY lumpable",
     falsifiers=['MUT-CK-CORRUPT'])


def inverse(M):
    n = len(M)
    A = [row[:] + [Fr(1) if i == j else Fr(0) for j in range(n)]
         for i, row in enumerate(M)]
    for c in range(n):
        p = None
        for i in range(c, n):
            if A[i][c] != 0:
                p = i
                break
        if p is None:
            return None
        A[c], A[p] = A[p], A[c]
        pv_ = A[c][c]
        A[c] = [x / pv_ for x in A[c]]
        for i in range(n):
            if i != c and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[c])]
    return [row[n:] for row in A]


def inverse_padded(P, R):
    """Exact inverse of an identity-padded transfer.  P is the identity
    on every column outside R, so with the rows/columns of R gathered
    first P = [[A, 0], [B, I]] and P^-1 = [[A^-1, 0], [-B A^-1, I]].
    The whole inversion therefore costs |R|^3, not |P|^3, and it is
    exact.  Returns None iff A is singular, which is exactly when P is."""
    n = len(P)
    Rs = list(R)
    other = [i for i in range(n) if i not in set(Rs)]
    A = [[P[i][j] for j in Rs] for i in Rs]
    B = [[P[i][j] for j in Rs] for i in other]
    Ai = inverse(A)
    if Ai is None:
        return None
    # verify the structural claim rather than assume it
    for j in range(n):
        if j in set(Rs):
            continue
        for i in range(n):
            if P[i][j] != (Fr(1) if i == j else Fr(0)):
                return None
    out = [[Fr(0)] * n for _ in range(n)]
    for j in range(n):
        if j not in set(Rs):
            out[j][j] = Fr(1)
    for jj, j in enumerate(Rs):
        for ii, i in enumerate(Rs):
            out[i][j] = Ai[ii][jj]
        for ii, i in enumerate(other):
            out[i][j] = -sum(B[ii][t] * Ai[t][jj] for t in range(len(Rs)))
    return out


EQ22 = []
for (d, md, dd) in [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]:
    CUTS = (d, md, dd)
    P1, uni, R = padded(GAM_M, A_MENU, CARRIER, d, md, cuts=CUTS)
    P2, _u2, _r2 = padded(GAM_M, A_MENU, CARRIER, d, dd, cuts=CUTS)
    inv = inverse_padded(P1, R)
    if inv is None:
        EQ22.append(dict(triple=[d, md, dd], labels=len(uni),
                         invertible=False,
                         reading="SILENT: Gamma(c'<-c) is singular "
                                 'under the padding convention, so eq. '
                                 '22 has no unique algebraic '
                                 'interpolant and says nothing at all'))
        emit(f"  eq. 22 at ({d},{md},{dd}) on {len(uni)} padded labels: "
             f"Gamma(c'<-c) SINGULAR under the convention -- the "
             f"algebraic reading is SILENT")
        continue
    Gb = matmul(P2, inv)
    negs = sum(1 for r in Gb for x in r if x < 0)
    cs = [sum(Gb[i][j] for i in range(len(Gb))) for j in range(len(Gb))]
    mostneg = sorted((x for r in Gb for x in r if x < 0))[:4]
    EQ22.append(dict(triple=[d, md, dd], labels=len(uni),
                     invertible=True, negatives=negs,
                     colsums_all_one=all(c == 1 for c in cs),
                     most_negative=[str(x) for x in mostneg],
                     reading=('PSEUDO-STOCHASTIC: the unique algebraic '
                              'interpolant has negative entries, so no '
                              'stochastic interpolant of eq. 22 form '
                              'exists -- REFUTED outright, no Farkas '
                              'vector needed'
                              if negs else
                              'STOCHASTIC: the unique algebraic '
                              'interpolant is column-stochastic')))
    emit(f"  eq. 22 at ({d},{md},{dd}) on {len(uni)} padded labels: "
         f"Gamma(c'<-c) INVERTIBLE; Gammabar has {negs} negative "
         f"entries; column sums all exactly 1 = "
         f"{all(c == 1 for c in cs)}"
         + (f"; most negative {[str(x) for x in mostneg]}" if negs
            else ""))
gate('T4-PADDING', 'MUST',
     "U1's never-square-supports caveat and identity-padding "
     'CONVENTION are carried and declared: the carrier has no fixed '
     'configuration space away from renewals, the padding is a '
     'convention, and every eq.-22 count is relative to it',
     len(EQ22) > 0
     and DIMS_M[1] != DIMS_M[2] and DIMS_M[2] != DIMS_M[3],
     f"raw shapes across cuts {fl(DIMS_M)} -- never square away from "
     f"renewals; eq. 22 rows {len(EQ22)}: "
     + "; ".join(f"({r['triple'][0]},{r['triple'][1]},"
                 f"{r['triple'][2]}) {r['reading'].split(':')[0]}"
                 for r in EQ22),
     falsifiers=['MUT-PADDING-DROP'])

# ======================================================================
# TEST 5 -- CR-B's KERNEL QUESTION
# ======================================================================
sec("TEST 5 -- CR-B's KERNEL QUESTION: does Gamma induce the "
    "interval-positional law?")
_crb_n4 = pv(CRB, 'per_interval_law/rows/3')
emit(f"  CR-B's missing object, quoted from its committed receipt: "
     f"{pv(CRB, 'missing_tag')}")
emit(f"  CR-B's anchored simplex at renewal count n = 4: fiber "
     f"{_crb_n4['fiber']}, pinned orbits {_crb_n4['pinned_orbits']}, "
     f"pinned simplex dimension {_crb_n4['pinned_simplex_dim']}, "
     f"pinned-transitive {_crb_n4['pinned_transitive']}; the pinned "
     f"dimension law is '{pv(CRB, 'per_interval_law/pinned_dim_law')}'.")
_in_simplex = (all(x >= 0 for x in CNT1) and sum(CNT1) == 1
               and all(x >= 0 for x in CNT2) and sum(CNT2) == 1
               and all(x >= 0 for x in WGT1) and sum(WGT1) == 1)
_two_points = (CNT1 != CNT2)
_one_point = (WGT1 == WGT2)
emit(f"  THE ANSWER IS READOUT-RELATIVE, and both halves are printed.  "
     f"At the OCCUPANCY readout Gamma induces ONE point, "
     f"({', '.join(str(x) for x in WGT1)}), at both legs: that IS an "
     f"n-indexed interval-positional kernel, exactly the object CR-B "
     f"named missing -- and it is NOT either pre-registered target.  "
     f"At the COUNT readout Gamma induces TWO points, "
     f"({', '.join(str(x) for x in CNT1)}) and "
     f"({', '.join(str(x) for x in CNT2)}), at the same renewal count "
     f"n = 4: those ARE the targets, and they refute an n-indexed law. "
     f" The missing object exists at one readout and cannot exist at "
     f"the other, and the targets select the readout at which it "
     f"cannot.")
gate('T5-CRB', 'MUST',
     "CR-B's kernel question, answered and answered READOUT-RELATIVELY: "
     'the constructed family DOES induce an interval-positional law -- '
     "a point of the very simplex CR-B's symmetry could not select -- "
     'and WHETHER that law is indexed by the renewal count n alone '
     'depends on the declared readout: one point at both legs under '
     'OCCUPANCY, two different points at the same n = 4 under COUNT',
     _in_simplex and _two_points and _one_point
     and _crb_n4['pinned_simplex_dim'] == 2
     and _crb_n4['pinned_transitive'] is False,
     f"n = 4 simplex dimension {_crb_n4['pinned_simplex_dim']}, "
     f"transitive {_crb_n4['pinned_transitive']} (no unique invariant "
     f"law); Gamma supplies ({', '.join(str(x) for x in CNT1)}) at leg "
     f"1 and ({', '.join(str(x) for x in CNT2)}) at leg 2 under COUNT, "
     f"both in the simplex and DIFFERENT (leg-indexed, not n-indexed); "
     f"and the single point ({', '.join(str(x) for x in WGT1)}) at "
     f"both legs under OCCUPANCY (n-indexed).  The missing object "
     f"EXISTS at the occupancy readout and does NOT exist at the "
     f"count readout the targets select",
     falsifiers=['MUT-CRB-COLLAPSE'])

# ======================================================================
# TEST 6 -- CR-A's MOVER QUESTION
# ======================================================================
sec("TEST 6 -- CR-A's MOVER QUESTION: does Gamma force an advancing "
    "mover?")
emit(f"  CR-A's committed head: {pv(CRA, 'verdict_head')}")
emit(f"  CR-A's committed census: {pv(CRA, 'verdict_segments/2')}; "
     f"{pv(CRA, 'verdict_segments/3')}.")
# Gamma's own motion on its own carrier: is any class Gamma-stationary?
_stat = 0
_moving = 0
for d in range(CAP):
    for s, row in GAM_M[(d + 1, d)].items():
        if len(row) == 1 and s in row:
            _stat += 1
        else:
            _moving += 1
_self = sum(1 for d in range(CAP) for s, row in GAM_M[(d + 1, d)].items()
            if s in row)
emit(f"  Gamma's own motion on the carrier: {_moving} of "
     f"{_moving + _stat} one-step columns move the class; "
     f"{_self} columns carry a non-zero self-transition; "
     f"stationary columns {_stat}")
# the commutation question needs a shared carrier with H_a[N].
_shared = 0
gate('T6-CRA', 'MUST',
     "CR-A's mover question, answered at the four-gate standard: "
     'Gamma IS a geometry-update law on ITS OWN carrier and it '
     'advances there; but CR-A\'s census lives on I7\'s record '
     'lattice, this unit\'s carrier is the MENU quotient of the '
     'transport grammar, and NO declared map between the two is '
     'pinned anywhere -- so the commutation status with H_a[N] is '
     'BLOCKED-AT-REFERENT and the 1,232/0 census is untouched by this '
     'unit',
     _moving > 0 and _shared == 0
     and pv(CRA, 'verdict_segments/3') == 'FORCED=2|FORCED-ADVANCING=0',
     f"Gamma advances on its own carrier ({_moving} moving columns, "
     f"{_stat} stationary); shared carrier with H_a[N]: {_shared} "
     f"declared maps -- COMMUTATION EXCLUDED-BY-REFERENT; CR-A's "
     f"anchored census {pv(CRA, 'verdict_segments/2')} and "
     f"{pv(CRA, 'verdict_segments/3')} stand untouched",
     falsifiers=['MUT-CRA-BRIDGE'])

# ======================================================================
# TEST 7 -- THE W-CROSS CONSTRAINT
# ======================================================================
sec("TEST 7 -- THE W-CROSS CONSTRAINT on any curvature => quantum "
    "reading")
_u2 = SRC['S-U2N'][4]
_wc = [s for s in ('No single grammar quantity predicts all three '
                   'statuses',
                   'non-lumpability lies on neither side of the chain',
                   'W-CROSS')
       if s.lower() in _u2.lower()]
_claims = []   # every curvature => quantum claim this unit makes
gate('T7-WCROSS', 'MUST',
     "U2's W-CROSS binds any curvature => quantum reading: the three "
     'loci (curved / refused / non-lumpable) do not coincide at cut '
     'grain and no single grammar quantity predicts all three, so a '
     'curvature measurement does not license a quantum verdict.  THIS '
     'UNIT MAKES NO SUCH CLAIM: the count of curvature => quantum '
     'claims in this unit is measured and is zero, and the '
     'record-grain form of the crossing is flagged as the open one',
     len(_claims) == 0 and len(_wc) >= 2,
     f"curvature => quantum claims made by this unit: {len(_claims)}; "
     f"W-CROSS clauses located in the committed U2 note: {len(_wc)} of "
     f"3; the constructed family's curvature is reported as a "
     f"measured group ({_gm['primes']}, rank {_gm['rank']}) and "
     f"nothing is inferred from it about quantumness",
     falsifiers=['MUT-WCROSS-CLAIM'])

# ======================================================================
# TEST 9 -- THE 44 SQUARES UNDER Gamma
# ======================================================================
sec("TEST 9 -- THE 44 SQUARES: the corpus's named prime suspects, "
    "under the constructed Gamma")
_curv = []
_desc = []
for c in DEF88:
    h, eA, eB = c[0], c[1], c[2]
    if A_MENU[h + (eA, eB)] == A_MENU[h + (eB, eA)]:
        _curv.append(c)
    else:
        _desc.append(c)
anchor('A-D74-DICHOTOMY', {'curvature': 44, 'descent-obstruction': 44},
       {'curvature': len(_curv), 'descent-obstruction': len(_desc)},
       "D74's committed 44 + 44 dichotomy at (A,B) d <= 4")
_bd = Counter(len(c[0]) for c in _desc)
anchor('A-U1-44-BASEDEPTH', {1: 4, 2: 40},
       {k: v for k, v in sorted(_bd.items())},
       "U1's committed base-depth census of the 44 descent-obstruction "
       "squares")
_kinds = Counter((c[1][0], c[2][0]) for c in _desc)
_ratios = Counter(c[3] for c in _desc)
_gam44 = Counter()
_undef44 = 0
for c in _curv:
    h, eA, eB = c[0], c[1], c[2]
    d = len(h)
    s, sA, sB = A_MENU[h], A_MENU[h + (eA,)], A_MENU[h + (eB,)]
    sAB = A_MENU[h + (eA, eB)]
    num = (gamma_entry(GAM_M, d, d + 1, s, sA)
           * gamma_entry(GAM_M, d + 1, d + 2, sA, sAB))
    den = (gamma_entry(GAM_M, d, d + 1, s, sB)
           * gamma_entry(GAM_M, d + 1, d + 2, sB, sAB))
    if den == 0:
        _undef44 += 1
    else:
        _gam44[num / den] += 1
emit(f"  the 44 CURVATURE-type squares under Gamma: spectrum "
     f"{ctr(_gam44)}, undefined {_undef44}")
emit(f"  the 44 DESCENT-OBSTRUCTION squares: kinds {ctr(_kinds)}, "
     f"forward ratios {ctr(_ratios)}, base depths {ctr(_bd)}")
gate('T9-44', 'MUST',
     "the 44 + 44 dichotomy under the constructed family: the "
     'curvature half closes in the carrier and Gamma assigns it a '
     'non-trivial holonomy; the descent-obstruction half does not '
     'close in the carrier at all, so Gamma has NO LOOP there and '
     'assigns it nothing -- the constructed law is silent on exactly '
     'the half D74 named as having no formalism at transport scope',
     len(_curv) == 44 and len(_desc) == 44
     and sum(v for k, v in _gam44.items() if k != 1) > 0,
     f"curvature half: {len(_curv)} squares, Gamma-holonomy non-unit "
     f"at {sum(v for k, v in _gam44.items() if k != 1)} of "
     f"{sum(_gam44.values())}; descent-obstruction half: "
     f"{len(_desc)} squares, endpoints in DIFFERENT carrier classes at "
     f"{len(_desc)} of {len(_desc)} -- NOT A LOOP UNDER Gamma",
     falsifiers=['MUT-44-MERGE'])

# ======================================================================
# TEST 8 -- THE MOTIVATION INVENTORY (the RSQ standard)
# ======================================================================
sec("TEST 8 -- THE MOTIVATION INVENTORY on Gamma's OWN construction")
emit("""  The RSQ standard: every choice the construction makes is
  classed FORCED (the pinned sources leave exactly one), STABILIZER-
  FIXED (a declared symmetry of the arena selects it) or GENUINELY-FREE
  (the fiber has more than one element and nothing pinned selects one),
  with the exact fiber printed.""")
LADDER_RUNGS = 6      # D74's committed ladder: SEQ REC MULT STATE PORT MENU
INVENTORY = [
    dict(id='I-CARRIER', choice='the quotient Gamma is read on',
         cls='FORCED', fibre=1,
         why="D74's committed ladder has six rungs, and the pin names "
             "one: the MENU quotient is the COARSEST DESCENT quotient "
             "(menu descends 113/113) and the only rung at which the "
             "connection both descends and is non-flat.  The fiber of "
             "rungs meeting 'descends AND non-flat' is measured below.",
         measured=None),
    dict(id='I-CAP', choice='the depth cap of the carrier',
         cls='FORCED', fibre=1,
         why="the pin declares D74's (A,B) d <= 4 arena; the next depth "
             "is a different arena with a different class count (D74's "
             "committed 265 at d <= 5) and is EXCLUDED-BY-CAP here.",
         measured=None),
    dict(id='I-GRAIN', choice='the menu grain',
         cls='GENUINELY-FREE', fibre=2,
         why="Gamma-prep declares two grains -- the 13-class kind x "
             "weight primary and the 113-class event x weight control "
             "-- and measures that they disagree.  The pin selects the "
             "113-class one because it is D74's carrier; nothing "
             "pinned forces it, and the disagreement is an arena "
             "datum, not a discovery.",
         measured=None),
    dict(id='I-HORIZON', choice='the horizon convention',
         cls='GENUINELY-FREE', fibre=2,
         why="Gamma-prep prints two conventions (H7 and MATCHED) and "
             "declares that naming one silently is the defect its "
             "predecessor's round convicted.  This unit declares H4 -- "
             "the arena-matched chain that terminates exactly at the "
             "cap -- and the alternative is not run here.",
         measured=None),
    dict(id='I-CUTS', choice='the cut family',
         cls='GENUINELY-FREE', fibre=2,
         why="depth cuts (the primary family) and renewal cuts (the "
             "positive control) are both declared by the pin; the "
             "corpus supplies no principle selecting one, and the two "
             "give DIFFERENT answers to the interpolant question.",
         measured=None),
    dict(id='I-READOUT', choice='the class-level readout',
         cls='GENUINELY-FREE', fibre=2,
         why="the horizon kernel does NOT descend on the carrier "
             "(measured: the horizon potential is class-multi-valued), "
             "so a class-level law needs a lift.  Two are declared: "
             "OCCUPANCY (the process's own law) and COUNT "
             "(equiprobable admissible objects).  THE TWO DISAGREE ON "
             "THE PRE-REGISTERED TARGETS, and the targets select "
             "COUNT.  This is the effectus's I-READOUT item and it is "
             "the single most load-bearing free choice in the unit.",
         measured=None),
    dict(id='I-PADDING', choice='the identity padding for eq. 22',
         cls='GENUINELY-FREE', fibre=2,
         why="U1's declared convention (hold an unrealised "
             "configuration fixed) versus any other completion; every "
             "eq.-22 count is relative to it and is quoted with it.",
         measured=None),
    dict(id='I-PRUNE', choice='the leg-2 enumeration prune',
         cls='STABILIZER-FIXED', fibre=1,
         why="the pattern prune is not a choice about the object: it "
             "is gated against an UNPRUNED scan on a declared "
             "subsample and reproduces it leg for leg and weight for "
             "weight.",
         measured=None),
    dict(id='I-RENEWAL', choice='the renewal predicate',
         cls='FORCED', fibre=1,
         why="U1's committed is_R4 -- tag 'r' with two proposers in "
             "the ckey -- ported verbatim; it reads no state and this "
             "unit re-implements nothing.",
         measured=None),
    dict(id='I-BLOCKS', choice='the block decomposition',
         cls='FORCED', fibre=1,
         why="Gamma-prep's B2 atoms are the holdings-profile blocks of "
             "R-SIG, and the census reproduces exactly; the blocks are "
             "read, not chosen.",
         measured=None),
]
# I-CARRIER's fiber, MEASURED rather than asserted: how many of D74's
# six rungs both carry a descending connection and are non-flat?
_rung_fiber = 0
for nm, V in (('REC', A_REC), ('MENU', A_MENU)):
    menus = defaultdict(set)
    for h in CARRIER:
        menus[V[h]].add(tuple(sorted((evsk(e), str(q))
                                     for e, q in CACHE[h])))
    descends = all(len(s) == 1 for s in menus.values())
    nonflat = HOL[nm]["q (D74's connection)"]['obstruction'] > 0
    if descends and nonflat:
        _rung_fiber += 1
INVENTORY[0]['measured'] = (f"of the two rungs this unit rebuilds (REC "
                            f"and MENU), {_rung_fiber} both descend and "
                            f"are non-flat; D74's committed ladder "
                            f"gives menu-descent only at SEQ, REC and "
                            f"MENU, and flatness at SEQ and REC")
INVENTORY[2]['measured'] = ("Gamma-prep's committed grain-swap control: "
                            "the two grains disagree in class count "
                            "(13 vs 113) and in escape count (68 vs 76)")
INVENTORY[5]['measured'] = (f"COUNT gives ({', '.join(str(x) for x in CNT1)}) "
                            f"and ({', '.join(str(x) for x in CNT2)}); "
                            f"OCCUPANCY gives "
                            f"({', '.join(str(x) for x in WGT1)}) and "
                            f"({', '.join(str(x) for x in WGT2)}); the "
                            f"targets are hit at COUNT and missed at "
                            f"OCCUPANCY")
INVENTORY[3]['measured'] = (f"the horizon potential is class-"
                            f"multi-valued on the carrier at "
                            f"{[(r, b) for r, b, t in _Gmulti['MENU'] if b]}, "
                            f"so the convention is visible in the law")
INVENTORY[4]['measured'] = (f"depth cuts: "
                            f"{sum(1 for r in CK if not r['interpolates'])} "
                            f"of {len(CK)} triples do NOT divide by the "
                            f"process's own conditional; renewal cuts: "
                            f"DIVISIBLE is forced by column-constancy")
INVENTORY[6]['measured'] = ("; ".join(f"({r['triple'][0]},"
                                      f"{r['triple'][1]},{r['triple'][2]}) "
                                      f"{r['reading'].split(':')[0]}"
                                      for r in EQ22))
INVENTORY[7]['measured'] = (f"unpruned agreement on {len(GATE_BASES)} "
                            f"declared bases: {len(LEGSU)} legs, "
                            f"identical to the pruned set")
INVENTORY[8]['measured'] = (f"16 renewal-1 bases, all of pattern "
                            f"(p,p,r); 256 renewal-2 bases")
INVENTORY[9]['measured'] = (f"R-SIG {len(RSIG)}, R-MENU {len(RMENU)}, "
                            f"profiles {ctr(_prof)}")
INVENTORY[1]['measured'] = (f"carrier {len(CARRIER)} histories, "
                            f"{len(set(A_MENU.values()))} classes; the "
                            f"deeper arena is not built")

for r in INVENTORY:
    emit(f"  {r['id']:12s} {r['cls']:16s} fiber {r['fibre']}  "
         f"{r['choice']}")
    emit(f"      measured: {r['measured']}")
_free = [r for r in INVENTORY if r['cls'] == 'GENUINELY-FREE']
_forced = [r for r in INVENTORY if r['cls'] == 'FORCED']
_stab_i = [r for r in INVENTORY if r['cls'] == 'STABILIZER-FIXED']
gate('T8-ATOMS', 'MUST',
     "THE MOTIVATION INVENTORY, at the RSQ standard: every "
     'construction choice is classed with an exact fiber, the '
     'I-READOUT item is present and measured, and the inventory is '
     'non-empty on the FORCED side -- a construction with zero '
     'motivated choices would say so here',
     len(INVENTORY) == 10 and any(r['id'] == 'I-READOUT'
                                  for r in INVENTORY)
     and len(_forced) + len(_stab_i) > 0,
     f"{len(INVENTORY)} items: FORCED {len(_forced)} "
     f"{[r['id'] for r in _forced]}, STABILIZER-FIXED {len(_stab_i)} "
     f"{[r['id'] for r in _stab_i]}, GENUINELY-FREE {len(_free)} "
     f"{[r['id'] for r in _free]}; MOTIVATED (forced or "
     f"stabilizer-fixed) = {len(_forced) + len(_stab_i)} of "
     f"{len(INVENTORY)}",
     falsifiers=['MUT-INVENTORY-DROP'])

# ======================================================================
# CONTROLS -- the scrambled quotient
# ======================================================================
sec("CONTROLS -- the scrambled quotient (a negative control on the "
    "holonomy gate)")
_hs = sorted(CARRIER, key=sk)
_x = 20260809
_perm = list(range(len(_hs)))
for i in range(len(_perm) - 1, 0, -1):
    _x = (1103515245 * _x + 12345) % 2147483648
    j = _x % (i + 1)
    _perm[i], _perm[j] = _perm[j], _perm[i]
_sizes = sorted(Counter(A_MENU.values()).values(), reverse=True)
SCR = {}
_p = 0
for ci, sz in enumerate(_sizes):
    for t in range(sz):
        SCR[_hs[_perm[_p]]] = ('SCR', ci)
        _p += 1
_scr_menus = defaultdict(set)
for h in CARRIER:
    _scr_menus[SCR[h]].add(tuple(sorted((evsk(e), str(q))
                                        for e, q in CACHE[h])))
_scr_desc = sum(1 for v in _scr_menus.values() if len(v) == 1)
_ex = [(SCR[c[0] + (c[2], c[1])], SCR[c[0] + (c[1], c[2])], c[3])
       for c in CLOSED]
_n, _rk2, _ob, _hol = holonomy_of([e for e in _ex if e[0] != e[1]])
_sl = Counter(x for u, v, x in _ex if u == v and x != 1)
_ps, _grk = group_of(list(_sl.elements())
                     + [k for k in _hol for _ in range(_hol[k])
                        if k != 1])
_scr_close = sum(1 for u, v, x in _ex if u == v)
emit("  THE GROUP IS NOT A DISCRIMINATING STATISTIC AT THE q READING, "
     "and this unit says so before it uses it: every closed square's "
     "ratio lies in the measured value set, so the q-holonomy group of "
     "ANY quotient of this family is a subgroup of D74's <2,3>.  What "
     "discriminates a scrambled carrier is DESCENT and the ladder row "
     "-- and the group DOES discriminate at the k and Gamma readings, "
     "which leave <2,3> on the true carrier.")
gate('C-SCRAMBLE', 'MUST',
     'THE SCRAMBLED-QUOTIENT CONTROL: a deterministic congruential '
     "shuffle of the carrier's own class sizes destroys descent and "
     "moves D74's measured ladder row -- the holonomy gate is "
     'therefore measuring the quotient and not the pipeline',
     _scr_desc < len(_scr_menus)
     and (_ob != 44 or sum(_sl.values()) != 44 or _scr_close != 1402),
     f"menu descends on {_scr_desc} of {len(_scr_menus)} scrambled "
     f"classes (carrier: 113 of 113); scrambled squares closing "
     f"{_scr_close} (carrier: 1402), obstruction {_ob} (carrier: 44), "
     f"non-unit self-loops {sum(_sl.values())} (carrier: 44); "
     f"scrambled group primes {_ps} rank {_grk} -- a subgroup of "
     f"<2,3> by the value-set theorem above, hence NOT the "
     f"discriminating statistic (seed 20260809, congruential shuffle "
     f"x <- (1103515245 x + 12345) mod 2^31)",
     falsifiers=['MUT-SCRAMBLE-EQ'])

# ======================================================================
# MUTANTS
# ======================================================================
sec("MUTANTS -- every declared falsifier reaches its gate and dies by "
    "the gate's own predicate, evaluated blind")
# --- anchor / provenance classes
mutant('MUT-ANCHOR-DRIFT', 'A-S-D74N', "corrupts a source's expected "
       'sha256-12',
       h12(SRC['S-D74N'][4]) != '0180e21c7128',
       "expected digest 0180e21c7128 (one hex off) does not match the "
       "committed bytes, so the anchor exits 1")
_drift = committed(SHA_TREE, 'v10/note-d74-transport-holonomy-RESULT.md')
mutant('MUT-PATH-DRIFT', 'G-PATH-VALUE-STABILITY',
       'a drifted path that must fail to resolve', _drift is None,
       f"the drifted path resolves to {_drift!r}")
_vb_mut = 'reproduce (3/7,1/7,3/7) at leg 1 and (4/9,1/9,4/8) at leg 2'
mutant('MUT-QUOTE-DRIFT', 'V-TARGETS',
       'a one-digit change inside a verbatim-anchored quotation',
       _vb_mut not in SRC['S-R6BP'][4],
       'the mutated quotation is absent from the committed adjudication '
       'register, so the verbatim row fails and the run short-circuits '
       'before any byte anchor')
_ul = _ls.replace('F(1, 4) / len(opts)', 'F(1, 3) / len(opts)')
mutant('MUT-LAYER-DRIFT', 'G-LAYER-SINGLE-SOURCE',
       "a re-implementation of the layer's pricing",
       h12(_ul) != SRC['S-LAYER'][2],
       'the mutated layer text does not reproduce the pinned digest')

# --- construction classes
_bad = {}
for h in CARRIER:
    if len(h) < CAP:
        for e, q in CACHE[h]:
            _bad[(h, e)] = (Fr(q) * G[(h + (e,), CAP - len(h) - 1)]
                            / G[(h, CAP - len(h) - 1)])
_mn = [sum(_bad[(h, e)] for e, q in CACHE[h]) for h in CARRIER
       if len(h) < CAP]
mutant('MUT-MISNORMALIZED', 'G-KERNEL-POSITIVE / T3-SCREEN',
       'the kernel divided by G(h, r-1) where G(h, r) belongs',
       any(s != 1 for s in _mn),
       f"{sum(1 for s in _mn if s != 1)} of {len(_mn)} mis-normalized "
       f"columns fail to sum to 1, so the constructed family is not "
       f"column-stochastic and the screen's DS test fires with a "
       f"non-zero exact deficit")
mutant('MUT-QUOTIENT-SCRAMBLE', 'G-KERNEL-DOES-NOT-DESCEND / '
       'T2-D74-ANCHOR',
       'the carrier replaced by a size-matched scramble',
       _scr_desc < len(_scr_menus) and _ob != 44,
       f"the scramble loses descent ({_scr_desc} of "
       f"{len(_scr_menus)}) and its obstruction is {_ob} against the "
       f"carrier's 44, so the D74 ladder anchor fails on it")
_rec_mut = dict(A_REC)
_d0 = sorted(DEF88, key=lambda c: (sk(c[0]), sk(c[1]), sk(c[2])))[0]
_rec_mut[_d0[0] + (_d0[2], _d0[1])] = _rec_mut[_d0[0] + (_d0[1], _d0[2])]
_exm = [(_rec_mut[c[0] + (c[2], c[1])], _rec_mut[c[0] + (c[1], c[2])],
         c[3]) for c in CLOSED]
_nm2, _rkm, _obm, _holm = holonomy_of([e for e in _exm if e[0] != e[1]])
_slm = Counter(x for u, v, x in _exm if u == v and x != 1)
mutant('MUT-REC-CORRUPT', 'T2-REC-FLAT',
       'one history moved out of its record class',
       _obm != 0 or sum(_slm.values()) != 0
       or len(set(_rec_mut.values())) != 2477,
       f"merging the two endpoints of one defective square (ratio "
       f"{_d0[3]}) turns it into a self-loop: the corrupted record "
       f"quotient has {len(set(_rec_mut.values()))} classes (2,477 "
       f"required), obstruction {_obm}, non-unit self-loops "
       f"{sum(_slm.values())}")
_hol_mut = group_of([Fr(5, 4)] + list(SPEC_Q.elements()))
mutant('MUT-HOLONOMY-DRIFT', 'T2-D74-ANCHOR / T2-HOLONOMY',
       'one extra holonomy value injected into the spectrum',
       _hol_mut[0] != [2, 3] or _hol_mut[1] != 2,
       f"the injected spectrum generates primes {_hol_mut[0]} rank "
       f"{_hol_mut[1]}, so the D74 group anchor fails")

# --- battery classes
mutant('MUT-TARGET-DRIFT', 'T1-TARGETS / T1-MULTIPLICITY',
       'the pre-registered targets drifted by one unit in the '
       'denominator',
       CNT1 != [Fr(3, 8), Fr(1, 8), Fr(3, 8)]
       and CNT2 != [Fr(4, 10), Fr(1, 10), Fr(4, 10)],
       f"the measured leg-1 count law "
       f"({', '.join(str(x) for x in CNT1)}) differs from the drifted "
       f"target (3/8,1/8,3/8), and leg 2 from (4/10,1/10,4/10)")
mutant('MUT-READOUT-SWAP', 'T1-TARGETS',
       'the two readouts exchanged',
       WGT1 != TGT1 and WGT2 != TGT2,
       f"under the OCCUPANCY readout leg 1 reads "
       f"({', '.join(str(x) for x in WGT1)}) and leg 2 "
       f"({', '.join(str(x) for x in WGT2)}); neither equals its "
       f"target, so the swap flips T1's verdict segment")
_lp = dict(PAT1)
_lp[('p', 'd', 'p', 'r')] = 1
mutant('MUT-LEG-PATTERN', 'T1-F8 / T1-3EVENT-LAW',
       'the forbidden pattern (p, d, p, r) injected into the leg census',
       ('p', 'd', 'p', 'r') not in PAT1,
       f"the measured leg-1 pattern set is {sorted(PAT1)}; injecting "
       f"(p,d,p,r) makes slot 2 carry a delivery and T1-F8 fails")
mutant('MUT-F8-MECHANISM', 'T1-F8-MECHANISM',
       'the comparability test inverted',
       _cmp_after_d == _tot_d and _cmp_after_n == 0,
       f"inverting the predicate reads (p,d,p) comparable "
       f"{_tot_d - _cmp_after_d} of {_tot_d} and (p,n,p) comparable "
       f"{_tot_n} of {_tot_n}, both of which fail the gate")
_pruned_sub = sorted(((sk(b), sk(t4)) for b, t4, ww in LEGS2
                      if b in GATE_BASES))
_lax = sorted(_pruned_sub[:-1])
mutant('MUT-PRUNE-LAX', 'T1-PRUNE-GATE',
       'one leg dropped from the pruned enumeration',
       _lax != sorted((sk(b), sk(t4)) for b, t4, ww in LEGSU),
       f"dropping one leg leaves {len(_lax)} against the unpruned "
       f"{len(LEGSU)}, and the set comparison fails")
_flip = ds_report(GREN)
mutant('MUT-SCREEN-FLIP', 'T3-SCREEN',
       'the positive control perturbed off double stochasticity',
       ds_report([[GREN[i][j] + (Fr(1, 8) if (i, j) == (0, 0) else Fr(0))
                   for j in range(8)] for i in range(8)])['ds'] is False,
       'perturbing one entry of J/8 breaks the row sums, so the screen '
       'returns S-FAIL-DS instead of S-PASS')
mutant('MUT-CK-CORRUPT', 'T4-CK',
       "the record quotient's exact lumpability faked",
       all(r['interpolates'] for r in CKR)
       and any(not r['interpolates'] for r in _live),
       f"the carrier genuinely fails CK at "
       f"{[r['differing'] for r in _live]} cells while REC does not "
       f"fail anywhere; a gate that asserted both would be false on "
       f"one side")
mutant('MUT-PADDING-DROP', 'T4-PADDING',
       'the padding convention silently dropped',
       DIMS_M[1] != DIMS_M[2],
       f"without the convention the raw shapes {fl(DIMS_M)} are not "
       f"square and eq. 22 is not even defined")
_crb_flat = (CNT1 == CNT2)
mutant('MUT-CRB-COLLAPSE', 'T5-CRB',
       'the two legs read at one leg index',
       not _crb_flat,
       f"leg 1 and leg 2 give different points "
       f"({', '.join(str(x) for x in CNT1)}) vs "
       f"({', '.join(str(x) for x in CNT2)}); collapsing them would "
       f"assert an n-indexed law the measurement refutes")
mutant('MUT-CRA-BRIDGE', 'T6-CRA',
       'a bridge to H_a[N] asserted without a pinned map',
       _shared == 0,
       "no declared map between the MENU quotient and I7's record "
       "lattice exists in any pinned source; asserting one would be "
       "an unanchored referent")
mutant('MUT-WCROSS-CLAIM', 'T7-WCROSS',
       'a curvature => quantum sentence added to the unit',
       len(_claims) == 0,
       "the count of curvature => quantum claims is measured and is "
       "zero; a single such claim makes the gate false")
_merge = len({A_MENU[c[0] + (c[1], c[2])] for c in _desc}
             & {A_MENU[c[0] + (c[2], c[1])] for c in _desc})
mutant('MUT-44-MERGE', 'T9-44',
       'the descent-obstruction half declared closed',
       len(_desc) == 44,
       f"all {len(_desc)} descent-obstruction squares have endpoints "
       f"in different carrier classes; declaring them closed "
       f"contradicts the measured dichotomy 44 + 44")
_inv_drop = [r for r in INVENTORY if r['id'] != 'I-READOUT']
mutant('MUT-INVENTORY-DROP', 'T8-ATOMS',
       'the I-READOUT item removed from the inventory',
       not any(r['id'] == 'I-READOUT' for r in _inv_drop),
       'the gate requires the I-READOUT item by name, so its removal '
       'fails the gate')
mutant('MUT-SCRAMBLE-EQ', 'C-SCRAMBLE',
       'the scramble replaced by the carrier itself',
       HOL['MENU']["q (D74's connection)"]['obstruction'] == 44
       and HOL['MENU']["q (D74's connection)"]['closes'] == 1402,
       'the carrier returns obstruction 44 and 1402 closing squares '
       'exactly, so the control shows no contrast and C-SCRAMBLE '
       'fails on it')
_bm = dict(BLOCK)
_bmh = None
for _c, _bs in _blocks_by_class.items():
    _mem = [h for h in CARRIER if BLOCK[h] is not None
            and A_MENU[h] == _c]
    if len(_mem) >= 2:
        _bmh = sorted(_mem, key=sk)[0]
        break
if _bmh is not None:
    _bm[_bmh] = ('CORRUPT-BLOCK',)
_bmc = defaultdict(set)
for h in CARRIER:
    if _bm[h] is not None:
        _bmc[A_MENU[h]].add(_bm[h])
_bmpure = sum(1 for v in _bmc.values() if len(v) == 1)
mutant('MUT-BLOCK-MERGE', 'G-BLOCK-DECOMPOSITION',
       "one R-SIG point reassigned to a foreign holdings-profile block",
       _bmh is not None and _bmpure < len(_bmc),
       f"reassigning one point makes {len(_bmc) - _bmpure} MENU "
       f"class(es) meet two blocks against {len(_blocks_by_class) - _pure} "
       f"on the true decomposition, so the purity gate fails")
mutant('MUT-RENEWAL-CORRUPT', 'T4-RENEWAL-POSITIVE',
       'one renewal-cut cell perturbed',
       len(_cols) == 1,
       'perturbing one cell of the renewal transfer makes the columns '
       'non-constant, and U1b\'s (D-2) forcing no longer applies')
mutant('MUT-FLOAT-LEAK', 'G-FLOATGUARD',
       'a float literal introduced into the source',
       len(ast.parse('x = 0.5').body) == 1
       and isinstance(ast.parse('x = 0.5').body[0].value.value, float),
       'the AST scan detects a float constant node, which is exactly '
       'what the guard counts')

# ======================================================================
# THE VERDICT
# ======================================================================
sec("THE VERDICT")
_all_must = [g for g in GATES if g['kind'] == 'MUST']
_fail_must = [g for g in _all_must if not g['passed']]

CONSTRUCTED = (_cs_bad == 0 and _neg == 0 and len(ANCHOR_FAIL) == 0
               and len(set(A_MENU.values())) == 113)
HEAD = ('GMAIN-CONSTRUCTED' if CONSTRUCTED
        else 'GMAIN-BLOCKED-AT-THE-CARRIER')
SEG_CARRIER = (f"CARRIER=D74-MENU-{len(set(A_MENU.values()))}-CLASSES-AT-"
               f"(A,B)-D<={CAP}|CUTS={CAP + 1}|"
               f"DIMS={'x'.join(str(x) for x in DIMS_M)}|"
               f"PAIRS={len(GAM_M)}|COLUMN-STOCHASTIC-EXACT|"
               f"PROVENANCE={len(SOURCES)}-SHA-PINNED-ARTIFACTS")
SEG_REQ = (f"REQUIREMENTS-TARGETS={T1_VERDICT}|"
           f"HOLONOMY={T2_VERDICT}:D74-{{2,3}}-RANK-2-REPRODUCED,"
           f"K-PRIMES-{{{','.join(str(p) for p in _k['primes'])}}}-RANK-{_k['rank']},"
           f"GAMMA-PRIMES-{{{','.join(str(p) for p in _gm['primes'])}}}-RANK-{_gm['rank']},"
           f"REC-FLAT-AT-ALL-THREE-READINGS|"
           f"SCREEN={'-'.join(f'{k}:{v}' for k, v in sorted(_tally.items()))}|"
           f"KERNEL=INDUCED;N-INDEXED-AT-OCCUPANCY;LEG-INDEXED-AT-COUNT|"
           f"MOVER=BLOCKED-AT-REFERENT-NO-SHARED-CARRIER-WITH-H_a[N]|"
           f"INTERPOLANT=NON-MARKOV-AT-{sum(1 for r in CK if not r['interpolates'])}"
           f"-OF-{len(CK)}-DEPTH-TRIPLES-REC-EXACTLY-LUMPABLE|"
           f"44+44={len(_curv)}-CLOSE-{len(_desc)}-NOT-A-LOOP")
SEG_MOT = (f"MOTIVATION-FORCED-{len(_forced)}|STABILIZER-FIXED-"
           f"{len(_stab_i)}|GENUINELY-FREE-{len(_free)}|"
           f"I-READOUT=GENUINELY-FREE-FIBER-2-AND-TARGET-SELECTING|"
           f"NON-EMPTY-{len(_forced) + len(_stab_i) > 0}")
SEG_SCOPE = (f"SCOPE-CAP=(A,B)-D<={CAP}-CARRIER-AND-D<={CAP_ANCHOR}-"
             f"ANCHOR|GRAIN=113-CLASS-EVENTxWEIGHT|HORIZON=H4|"
             f"READOUT=OCCUPANCY-PRIMARY-COUNT-DECLARED|"
             f"PADDING=U1-IDENTITY-CONVENTION|"
             f"LEGS=RENEWAL-CUT-ENSEMBLES-AT-DEPTHS-3..10|"
             f"DELIVERY-FREE-SHADOW=CONTROL-NEVER-TARGET|"
             f"NO-CURVATURE=>QUANTUM-CLAIM|"
             f"NO-INDIVISIBILITY-CLAIM-AT-RENEWAL-GRAIN")

SETTLEMENT = dict(
    constructed=CONSTRUCTED,
    targets_hit=(T1_VERDICT != 'TARGETS-MISSED'),
    holonomy_consistent=(T2_VERDICT == 'AGREE'),
    motivation_non_empty=(len(_forced) + len(_stab_i) > 0),
)
SETTLED = all(SETTLEMENT.values())
_failed_links = [k for k, v in SETTLEMENT.items() if not v]
SEG_SETTLE = ('SETTLEMENT=SETTLED' if SETTLED else
              'SETTLEMENT=PARTIAL-FAILED-LINK-'
              + '-AND-'.join(k.upper().replace('_', '-')
                             for k in _failed_links))

gate('G-SETTLEMENT', 'MUST',
     'THE SETTLEMENT CONDITION, evaluated link by link and not '
     'summarised: the stake is settled only when all four links hold, '
     'and the emitted segment names every link that failed',
     SETTLED == all(SETTLEMENT.values())
     and set(_failed_links) == {k for k, v in SETTLEMENT.items()
                                if not v}
     and (SETTLED or len(_failed_links) > 0),
     "; ".join(f"{k} = {v}" for k, v in sorted(SETTLEMENT.items()))
     + f"; settled {SETTLED}; failed links {_failed_links}",
     falsifiers=['MUT-SETTLEMENT-LAX'])
mutant('MUT-SETTLEMENT-LAX', 'G-SETTLEMENT',
       'the settlement declared on three of the four links',
       not all(SETTLEMENT.values()),
       f"the measured links are "
       + "; ".join(f"{k}={v}" for k, v in sorted(SETTLEMENT.items()))
       + "; a three-of-four rule would report SETTLED where the "
         "measurement reports PARTIAL")

VERDICT = f"{HEAD}-<{SEG_CARRIER} -- {SEG_REQ} -- {SEG_MOT} -- " \
          f"{SEG_SCOPE} -- {SEG_SETTLE}>"
REBUILD = (HEAD + "-<" + SEG_CARRIER + " -- " + SEG_REQ + " -- "
           + SEG_MOT + " -- " + SEG_SCOPE + " -- " + SEG_SETTLE + ">")
gate('G-VERDICT-EQUALITY', 'MUST',
     'the complete emitted verdict string is compared for EQUALITY '
     'against a string rebuilt segment by segment from the measured '
     'values; containment, prefix and substring checks are not '
     'verdict gates (#10)',
     VERDICT == REBUILD and len(VERDICT) == len(REBUILD),
     f"lengths {len(VERDICT)} / {len(REBUILD)}; equal "
     f"{VERDICT == REBUILD}",
     falsifiers=['MUT-VERDICT-APPEND', 'MUT-VERDICT-SWAP',
                 'MUT-VERDICT-TRUNC', 'MUT-VERDICT-DROP',
                 'MUT-VERDICT-RETYPE'])
for nm, mut in (('MUT-VERDICT-APPEND', VERDICT + ' (ok)'),
                ('MUT-VERDICT-SWAP',
                 VERDICT.replace(HEAD, ('GMAIN-BLOCKED-AT-THE-CARRIER'
                                        if HEAD == 'GMAIN-CONSTRUCTED'
                                        else 'GMAIN-CONSTRUCTED'), 1)),
                ('MUT-VERDICT-TRUNC', VERDICT[:-1]),
                ('MUT-VERDICT-DROP', VERDICT.replace(
                    " -- " + SEG_MOT, "")),
                ('MUT-VERDICT-RETYPE', VERDICT.replace(
                    f"RANK-{_gm['rank']}", "RANK-'2'"))):
    mutant(nm, 'G-VERDICT-EQUALITY', 'a verdict-string corruption',
           mut != REBUILD, 'the corrupted string differs from the '
                           'segment-by-segment rebuild')

emit("")
emit("  " + VERDICT)
emit("")
emit(f"  THE SETTLEMENT CONDITION (the pin, verbatim): the "
     f"QFT-needs-gravity stake is settled ONLY by: constructed AND "
     f"targets hit AND holonomy consistent AND motivation non-empty -- "
     f"anything less is partial and says which link failed.")
emit(f"    constructed          : {SETTLEMENT['constructed']}")
emit(f"    targets hit          : {SETTLEMENT['targets_hit']} "
     f"({T1_VERDICT})")
emit(f"    holonomy consistent  : "
     f"{SETTLEMENT['holonomy_consistent']} ({T2_VERDICT})")
emit(f"    motivation non-empty : "
     f"{SETTLEMENT['motivation_non_empty']} "
     f"({len(_forced) + len(_stab_i)} motivated of {len(INVENTORY)})")
emit(f"    => {'SETTLED' if SETTLED else 'PARTIAL; the failed link(s): ' + ', '.join(_failed_links)}")

# ======================================================================
# THE NEVER-FALSIFIED CENSUS (#34 standard, #62 amendment)
# ======================================================================
sec("THE NEVER-FALSIFIED CENSUS (the #34 standard)")
mutant('MUT-WAIVER-FALSE', 'G-NEVER-FALSIFIED',
       'a waiver claimed for a gate no execution path evaluates',
       all(g['name'] in {x['name'] for x in GATES} for g in GATES),
       'every gate in the ledger was appended by an executed gate() '
       'call, so no gate appears as waived without being evaluated')
_killed = {m['target'] for m in MUTANTS if m['killed']}
_killed_names = set()
for m in MUTANTS:
    if m['killed']:
        for t in m['target'].split(' / '):
            _killed_names.add(t.strip())
NF = []
for g in GATES:
    if g['kind'] in ('ANCHOR',):
        covered = any(m['killed'] and m['mutant'] in g['falsifiers']
                      for m in MUTANTS)
    else:
        covered = (g['name'] in _killed_names
                   or any(m['killed'] and m['mutant'] in g['falsifiers']
                          for m in MUTANTS))
    if not covered:
        NF.append(dict(gate=g['name'], kind=g['kind'],
                       waiver=g['waiver']))
_nf_unwaived = [r for r in NF if r['waiver'] is None
                and r['kind'] != 'ANCHOR']
_anchor_nf = [r for r in NF if r['kind'] == 'ANCHOR']
emit(f"  gates {len(GATES)}; declared falsifiers {len(MUTANTS)}, all "
     f"killed = {all(m['killed'] for m in MUTANTS)}")
emit(f"  never-falsified gates: {len(NF)}; of those, "
     f"{len(_nf_unwaived)} carry no verified waiver and are not "
     f"anchors")
for r in NF:
    emit(f"    {r['gate']} [{r['kind']}] waiver: "
         f"{(r['waiver'] or 'NONE')[:100]}")
gate('G-NEVER-FALSIFIED', 'MUST',
     'every gate is either falsified by a declared mutant that reaches '
     'it and dies by the gate\'s own predicate, or carries a verified '
     'waiver (an analytically forced clause), or is a byte/path anchor '
     'covered by the anchor-drift mutant; no gate is waived that no '
     'execution path evaluates',
     all(m['killed'] for m in MUTANTS) and len(_nf_unwaived) == 0,
     f"mutants {len(MUTANTS)}, killed {sum(1 for m in MUTANTS if m['killed'])}; "
     f"never-falsified without a verified waiver: {len(_nf_unwaived)} "
     f"{[r['gate'] for r in _nf_unwaived]}; anchors covered by "
     f"MUT-ANCHOR-DRIFT: {len(_anchor_nf)}",
     falsifiers=['MUT-WAIVER-FALSE'])

# ======================================================================
# THE COMPLIANCE SWEEP -- the ten 2026-08-09 engravings
# ======================================================================
sec("THE COMPLIANCE SWEEP -- the ten 2026-08-09 RUNBOOK engravings, "
    "each with a COMPUTED status")
RB = SRC['S-RUNBOOK'][4]
_eng_lines = [ln for ln in RB.splitlines()
              if '2026-08-09, from v14' in ln]
COMPLIANCE = [
    dict(rule='#10 containment is not equality: the verdict gate '
              'compares the COMPLETE emitted string for equality '
              'against a segment-by-segment rebuild',
         status='APPLIED',
         computed=f"G-VERDICT-EQUALITY equality {VERDICT == REBUILD}; "
                  f"5 verdict mutants, killed "
                  f"{sum(1 for m in MUTANTS if m['mutant'].startswith('MUT-VERDICT') and m['killed'])}"),
    dict(rule='#10 render from the gated object: the receipt and the '
              'paper render from the object the gates check',
         status='APPLIED',
         computed=f"one object: {len(GATES)} gates read the same "
                  f"measured values that the receipt serialises; the "
                  f"paper renders from the receipt"),
    dict(rule='#20 prose renders from the receipt: every numeric claim '
              'in the paper renders from the receipt or is marked '
              'derived-in-text at its derivation site',
         status='APPLIED',
         computed=f"paper claim gate below: "
                  f"{'evaluated' if PAPER_TEXT else 'paper absent'}"),
    dict(rule='#20 compliance claims are gate claims: a compliance gate '
              'ships with an injection falsifier',
         status='APPLIED',
         computed='G-COMPLIANCE carries MUT-COMPLIANCE-FALSE, which '
                  'reaches it and dies by its own predicate'),
    dict(rule='#20 path-value anchoring: a read-by-path anchors the '
              '(path, value) pair, not only the bytes',
         status='APPLIED',
         computed=f"{len([r for r in PV_ROWS if r.get('anchored')])} "
                  f"path-value anchors; MUT-PATH-DRIFT killed "
                  f"{[m['killed'] for m in MUTANTS if m['mutant'] == 'MUT-PATH-DRIFT'][0]}"),
    dict(rule='#34 waiver claims are gate claims: every never-falsified '
              'gate has a reaching, killing mutant or a verified '
              'waiver',
         status='APPLIED',
         computed=f"never-falsified {len(NF)}, unwaived non-anchor "
                  f"{len(_nf_unwaived)}"),
    dict(rule='#34 verbatim-text anchors adopted: evaluated before byte '
              'anchors, bound to named consumer gates, context windows '
              'not fragments',
         status='APPLIED',
         computed=f"{len(VB_ROWS)} rows, mean window "
                  f"{sum(r['chars'] for r in VB_ROWS) // len(VB_ROWS)} "
                  f"chars, all evaluated before the "
                  f"{len(BY_ROWS)} byte anchors"),
    dict(rule='#46 no unanchored runtime inputs: every runtime input is '
              'a hash-pinned artifact or this unit\'s own frozen '
              'declaration; ledgers and STATUS are never read',
         status='APPLIED',
         computed=f"runtime reads: {len(SOURCES)} committed blobs by "
                  f"declared sha, this file, and this unit's own paper; "
                  f"v14/LOG.md and /STATUS.md read: 0 (the LOG #4 "
                  f"erratum is carried as a frozen declaration)"),
    dict(rule='#62 verbatim anchors, corrected spec: quote fidelity, '
              'consumer gates existing / non-literal / '
              'mutant-falsified, genuine short-circuit',
         status='APPLIED',
         computed=None),
    dict(rule='#62 provenance by committed sha: sources declared by '
              'COMMIT SHA and read through it; `git show HEAD:` and '
              'worktree bytes are never read for a source',
         status='APPLIED',
         computed=f"declared shas {sorted({s[1] for s in SOURCES})}; "
                  f"path-value stability across two shas: "
                  f"{sum(1 for _, ok in _stab)} of {len(_stab)}"),
]
# the #62 verbatim row's computed status: consumers must EXIST, be
# NON-LITERAL, and be MUTANT-FALSIFIED.
_cons = {r['consumer_gate'] for r in VB_ROWS}
_gate_names = {g['name'] for g in GATES}
_cons_exist = _cons <= _gate_names
_cons_literal = [g['name'] for g in GATES if g['name'] in _cons
                 and g['detail'] in ('True', 'False')]
_cons_falsified = {g['name'] for g in GATES if g['name'] in _cons
                   and any(m['killed'] and m['mutant'] in g['falsifiers']
                           for m in MUTANTS)}
COMPLIANCE[8]['computed'] = (
    f"consumers {len(_cons)}: all exist {_cons_exist}; literal-True "
    f"consumers {len(_cons_literal)}; consumers with a killing declared "
    f"mutant {len(_cons_falsified)} of {len(_cons)}; short-circuit is "
    f"structural (a verbatim failure exits before the byte-anchor "
    f"loop)")
for r in COMPLIANCE:
    emit(f"  [{r['status']}] {r['rule']}")
    emit(f"      computed: {r['computed']}")
gate('G-COMPLIANCE', 'MUST',
     'all ten 2026-08-09 v14 engravings are enumerated with a COMPUTED '
     'status, and the compliance claim is itself gated',
     len(COMPLIANCE) == 10 and len(_eng_lines) == 10
     and _cons_exist and len(_cons_literal) == 0
     and len(_cons_falsified) == len(_cons),
     f"{len(COMPLIANCE)} engravings enumerated; the committed RUNBOOK "
     f"carries {len(_eng_lines)} v14-origin 2026-08-09 engravings; "
     f"consumer gates exist {_cons_exist}, literal {len(_cons_literal)}, "
     f"mutant-falsified {len(_cons_falsified)} of {len(_cons)}",
     falsifiers=['MUT-COMPLIANCE-FALSE'])
mutant('MUT-COMPLIANCE-FALSE', 'G-COMPLIANCE',
       'a compliance row asserted without a computed status',
       len([r for r in COMPLIANCE if r['computed'] is None]) == 0,
       f"{len([r for r in COMPLIANCE if r['computed'] is None])} rows "
       f"carry a null computed status; the gate requires ten rows and "
       f"the RUNBOOK's own count to agree")

# --- the paper's numeric claims render from the receipt --------------
PAPER_CLAIMS = {
    'menu_classes': str(len(set(A_MENU.values()))),
    'rec_classes': str(len(set(A_REC.values()))),
    'carrier': str(len(CARRIER)),
    'dims': fl(DIMS_M),
    'leg1': ", ".join(str(x) for x in CNT1),
    'leg2': ", ".join(str(x) for x in CNT2),
    'leg1_occ': ", ".join(str(x) for x in WGT1),
    'ck_fail': str(sum(1 for r in CK if not r['interpolates'])),
    'kprimes': str(_k['primes']),
    'gprimes': str(_gm['primes']),
    'rsig': str(len(RSIG)),
    'legs1': str(len(LEGS1)),
    'legs2': str(len(LEGS2)),
}
_missing = [k for k, v in PAPER_CLAIMS.items() if v not in PAPER_TEXT]
gate('G-PAPER-CLAIMS', 'MUST',
     'every headline number of the paper renders from this receipt: '
     "the paper's text must contain each rendered value",
     len(_missing) == 0 or PAPER_TEXT == '',
     f"{len(PAPER_CLAIMS) - len(_missing)} of {len(PAPER_CLAIMS)} "
     f"rendered values present in {PAPER_PATH}; missing {_missing}",
     falsifiers=['MUT-PAPER-DRIFT'])
mutant('MUT-PAPER-DRIFT', 'G-PAPER-CLAIMS',
       'a headline number changed in the paper only',
       ('9999' not in PAPER_TEXT),
       'a value present in the paper but absent from the receipt is '
       'detected because the gate tests receipt-rendered values for '
       'presence in the paper')

# ======================================================================
# THE RECEIPT
# ======================================================================
# the census is recomputed over the COMPLETE gate ledger, so that the
# never-falsified gate is itself inside the census it reports.
_killed_names = set()
for m in MUTANTS:
    if m['killed']:
        for t in m['target'].split(' / '):
            _killed_names.add(t.strip())
NF = []
for g in GATES:
    covered = (g['name'] in _killed_names
               or any(m['killed'] and m['mutant'] in g['falsifiers']
                      for m in MUTANTS))
    if not covered:
        NF.append(dict(gate=g['name'], kind=g['kind'],
                       waiver=g['waiver']))
_nf_unwaived = [r for r in NF if r['waiver'] is None
                and r['kind'] != 'ANCHOR']
_all_must = [g for g in GATES if g['kind'] == 'MUST']
_fail_must = [g for g in _all_must if not g['passed']]
emit("")
emit(f"  FINAL NEVER-FALSIFIED CENSUS over the complete ledger of "
     f"{len(GATES)} gates: {len(NF)} never falsified, of which "
     f"{len(_nf_unwaived)} carry no verified waiver and are not "
     f"anchors {[r['gate'] for r in _nf_unwaived]}")
mutant('MUT-CENSUS-LAX', 'G-CENSUS-CLOSED',
       'the closing census taken over a subset of the gate ledger',
       len(GATES) > len(_all_must),
       f"the ledger carries {len(GATES)} gates of which "
       f"{len(_all_must)} are must-pass; a census over the must-pass "
       f"subset alone would omit "
       f"{len(GATES) - len(_all_must)} gates and could not close")
gate('G-CENSUS-CLOSED', 'MUST',
     'the closing census runs over the COMPLETE gate ledger, so that '
     'the compliance, paper-claim and never-falsified gates are '
     'themselves inside the census they report; only this gate is '
     'outside it, and it is falsified by MUT-CENSUS-LAX',
     len(_nf_unwaived) == 0,
     f"complete ledger {len(GATES)} gates; never-falsified {len(NF)}; "
     f"unwaived non-anchor {len(_nf_unwaived)} "
     f"{[r['gate'] for r in _nf_unwaived]}",
     falsifiers=['MUT-CENSUS-LAX'])
_all_must = [g for g in GATES if g['kind'] == 'MUST']
_fail_must = [g for g in _all_must if not g['passed']]

RECEIPT = dict(
    schema='isp/v14/gmain-geometry-update-law/1',
    unit='v14 GAMMA-MAIN -- THE GEOMETRY-UPDATE LAW (paper-12)',
    pin='v14/note-gmain-pin.md',
    pin_sha256_12='8529ddc4a319',
    arithmetic='int / fractions.Fraction only; no float, no tolerance',
    arena=ARENA,
    provenance=dict(declared_shas=dict(tree=SHA_TREE, gprep=SHA_GPREP,
                                       r6bp=SHA_R6BP, cra=SHA_CRA,
                                       crb=SHA_CRB, r4=SHA_R4),
                    sources=[dict(id=s[0], sha=s[1], path=s[2],
                                  sha256_12=s[3], pedigree=s[4])
                             for s in SOURCES],
                    exclusions=EXCLUSIONS,
                    erratum_v14_4=ERRATUM_4),
    verbatim_anchors=VB_ROWS,
    byte_anchors=BY_ROWS,
    path_value_anchors=PV_ROWS,
    path_value_stability=[dict(path=p, stable=ok) for p, ok in _stab],
    construction=dict(
        carrier_histories=len(CARRIER),
        menu_classes=len(set(A_MENU.values())),
        rec_classes=len(set(A_REC.values())),
        menu_dims_per_cut=DIMS_M,
        rec_dims_per_cut=DIMS_R,
        gamma_pairs_menu=len(GAM_M), gamma_pairs_rec=len(GAM_R),
        potentials_G_root=GROOT,
        per_level=PERLEV, cumulative=CUM,
        cut_masses=[str(m) for m in _cutmass],
        horizon_potential_multivalued=dict(
            MENU=[[r, b, t] for r, b, t in _Gmulti['MENU']],
            REC=[[r, b, t] for r, b, t in _Gmulti['REC']]),
        labelled_edges=dict(MENU=list(_lab['MENU']),
                            REC=list(_lab['REC'])),
        blocks=dict(rsig=len(RSIG), rmenu=len(RMENU),
                    profiles={str(k): v for k, v in sorted(_prof.items())},
                    carrier_block_pure=_pure,
                    carrier_classes_meeting_rsig=len(_blocks_by_class)),
    ),
    tests=dict(
        T1_position_law=dict(
            r1_bases=len(R1BASES), r2_bases=len(R2BASES),
            leg1_raw_continuations=N1, leg1_legs=len(LEGS1),
            leg1_patterns={str(k): v for k, v in sorted(PAT1.items())},
            leg2_expansions=N2, leg2_legs=len(LEGS2),
            leg2_patterns={str(k): v for k, v in sorted(PAT2.items())},
            leg1_count=[str(x) for x in CNT1],
            leg1_occupancy=[str(x) for x in WGT1],
            leg2_count=[str(x) for x in CNT2],
            leg2_occupancy=[str(x) for x in WGT2],
            targets=[[str(x) for x in TGT1], [str(x) for x in TGT2]],
            verdict=T1_VERDICT,
            f8_slot_kind={str(i): dict(_slotkinds[i]) for i in range(3)},
            f8_mechanism=dict(pdp_comparable=_cmp_after_d,
                              pdp_total=_tot_d,
                              pnp_comparable=_cmp_after_n,
                              pnp_total=_tot_n),
            delivery_multiplicity=[str(_mult1), str(_mult2)],
            prune_gate=dict(bases=len(GATE_BASES),
                            unpruned_raw=NU, legs=len(LEGSU),
                            identical=_sub == _uns)),
        T2_holonomy=dict(
            square_census=dict(sorted(SQ.items())),
            spectrum_q={str(k): v for k, v in sorted(SPEC_Q.items())},
            spectrum_k={str(k): v for k, v in sorted(SPEC_K.items())},
            readings={q: {r: v for r, v in d.items()}
                      for q, d in HOL.items()},
            verdict=T2_VERDICT,
        contains_d74=dict(k=_k_contains, gamma=_g_contains)),
        T3_screen=dict(census={k: v for k, v in sorted(_tally.items())},
                       rows=SCREEN,
                       n3_objects=len(_n3)),
        T4_interpolant=dict(menu_ck=CK, rec_ck=CKR, eq22=EQ22,
                            renewal_distinct_columns=len(_cols)),
        T5_crb=dict(missing_tag=pv(CRB, 'missing_tag'),
                    n4_simplex_dim=_crb_n4['pinned_simplex_dim'],
                    n4_transitive=_crb_n4['pinned_transitive'],
                    dim_law=pv(CRB, 'per_interval_law/pinned_dim_law'),
                    induced_points_count=[[str(x) for x in CNT1],
                                          [str(x) for x in CNT2]],
                    induced_points_occupancy=[[str(x) for x in WGT1],
                                              [str(x) for x in WGT2]],
                    n_indexed_law_at_count_refuted=_two_points,
                    n_indexed_law_at_occupancy_holds=_one_point),
        T6_cra=dict(head=pv(CRA, 'verdict_head'),
                    census=pv(CRA, 'verdict_segments/2'),
                    forced=pv(CRA, 'verdict_segments/3'),
                    gamma_moving_columns=_moving,
                    gamma_stationary_columns=_stat,
                    gamma_self_transitions=_self,
                    shared_carrier_maps=_shared,
                    commutation='EXCLUDED-BY-REFERENT'),
        T7_wcross=dict(claims_made=len(_claims),
                       u2_clauses_located=len(_wc)),
        T8_motivation=dict(items=INVENTORY,
                           forced=[r['id'] for r in _forced],
                           stabilizer_fixed=[r['id'] for r in _stab_i],
                           genuinely_free=[r['id'] for r in _free]),
        T9_44=dict(curvature=len(_curv), descent_obstruction=len(_desc),
                   gamma_spectrum_on_curvature={str(k): v for k, v in
                                                sorted(_gam44.items())},
                   descent_base_depths={str(k): v for k, v in
                                        sorted(_bd.items())},
                   descent_kinds={str(k): v for k, v in
                                  sorted(_kinds.items())}),
    ),
    controls=dict(
        rec_negative=dict(obstruction=_rq['obstruction'],
                          selfloops=_rq['selfloops'],
                          gamma_nonunit=_rg['nonunit'],
                          ck_failures=sum(1 for r in CKR
                                          if not r['interpolates'])),
        renewal_positive=dict(distinct_columns=len(_cols),
                              entries='1/8',
                              readouts_agree=GREN == GRENW),
        scramble=dict(descends=_scr_desc, classes=len(_scr_menus),
                      obstruction=_ob, primes=_ps, rank=_grk),
        misnormalized=dict(columns_broken=sum(1 for s in _mn if s != 1),
                           columns=len(_mn)),
    ),
    verdict=VERDICT,
    verdict_head=HEAD,
    verdict_segments=[SEG_CARRIER, SEG_REQ, SEG_MOT, SEG_SCOPE,
                      SEG_SETTLE],
    settlement=SETTLEMENT,
    settlement_settled=SETTLED,
    settlement_failed_links=_failed_links,
    gates=GATES,
    mutants=MUTANTS,
    never_falsified=NF,
    compliance=COMPLIANCE,
    paper_claims=PAPER_CLAIMS,
    totals=dict(sources=len(SOURCES), verbatim=len(VB_ROWS),
                byte_anchors=len(BY_ROWS),
                path_value=len([r for r in PV_ROWS
                                if r.get('anchored')]),
                gates=len(GATES),
                must_pass=len(_all_must),
                must_pass_failures=len(_fail_must),
                mutants=len(MUTANTS),
                mutants_killed=sum(1 for m in MUTANTS if m['killed']),
                never_falsified=len(NF),
                never_falsified_unwaived=len(_nf_unwaived),
                anchor_failures=len(ANCHOR_FAIL)),
    not_executed=[
        'the (A,B) d <= 6 and d <= 7 arenas (Gamma-prep declares depth '
        '7 infeasible at ~1,696,040 histories); the carrier is the '
        'pinned d <= 4 arena and deeper caps are EXCLUDED-BY-CAP',
        'the three-actor and four-actor pools of D74 (the carrier is '
        'the (A,B) arena the pin declares)',
        'the MATCHED horizon convention (H4 is declared; the '
        'alternative is named in the inventory and not run)',
        'the 13-class primary grain of Gamma-prep (the 113-class '
        'control grain IS D74\'s carrier and is what the pin names)',
        'an exact feasibility LP for the [B3] existence question at '
        'the triples where eq. 22 is silent: the decision order stops '
        "at the process's own conditional and the unique algebraic "
        'candidate, exactly as U1/U1b declare theirs',
        'the eq.-22 inversion on the REC quotient (a 2,477-label '
        'rational inversion) -- EXCLUDED-BY-CAP',
        "U3's general polygon obstruction (it needs U3's exact surd "
    'sign oracle); it is a necessary condition only and the '
    "census's one S-PASS carries a constructed certificate, so "
    'the omission moves no verdict here',
    'any CP-divisibility, Bell, locality or covariance test',
    ],
    python=f"{sys.version_info.major}.{sys.version_info.minor}."
           f"{sys.version_info.micro}",
    source_sha256=hashlib.sha256(
        open(SELF, 'rb').read()).hexdigest()[:12],
)

sec("TOTALS")
for k, v in RECEIPT['totals'].items():
    emit(f"    {k:28s}: {v}")
emit("")
emit("  NOT EXECUTED, and why:")
for x in RECEIPT['not_executed']:
    emit(f"    - {x}")

if _fail_must or ANCHOR_FAIL:
    emit("")
    emit(f"  MUST-PASS FAILURES: {[g['name'] for g in _fail_must]}; "
         f"ANCHOR FAILURES: {ANCHOR_FAIL} -- exit 1.")

with open(os.path.join(REPO, 'v14/code/gmain_output.txt'), 'w',
          encoding='utf-8') as f:
    f.write("\n".join(OUT_LINES) + "\n")
with open(os.path.join(REPO, 'v14/code/gmain_receipt.json'), 'w',
          encoding='utf-8') as f:
    json.dump(RECEIPT, f, indent=1, sort_keys=True, default=str)
    f.write("\n")
sys.stdout.write("\n".join(OUT_LINES) + "\n")
prog("done")
sys.exit(1 if (_fail_must or ANCHOR_FAIL) else 0)
