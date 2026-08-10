#!/usr/bin/env python3
"""
gmain_exact.py -- v14 GAMMA-MAIN: THE GEOMETRY-UPDATE LAW (paper-12).
REPAIRED under the joint adjudication (v14 ledger #82,
v14/note-gmain-adjudication.md, sha256-12 972e54741330): orders
R-GM-1 .. R-GM-11.

Pin: v14/note-gmain-pin.md (frozen, v14 ledger #64, sha256-12
8529ddc4a319).  Deliverables: v14/paper-12-gamma-main.md,
v14/code/gmain_exact.py, gmain_output.txt, gmain_receipt.json.

THE CONSTRUCTION (pin section 2).  Gamma := the transport process read
on D74's committed MENU quotient (113 classes at the (A,B) d <= 4 cap),
as an exact rational column-stochastic family Gamma(cut' <- cut) between
declared depth cuts, built from the pinned relative-horizon kernels k_r.
The REC quotient (2,477 classes) is the mandatory NEGATIVE control.
Renewal cuts are the POSITIVE control only (U1b's column-constancy wall).
Gamma-prep's B2 atom structure -- the R-SIG holdings-profile blocks -- is
the block decomposition.

THE CORRECTED SETTLEMENT (adjudication section 1, carried verbatim as a
verbatim-text anchor): constructed TRUE; targets FALSE (three convergent
reasons, each a computed clause here); holonomy TRUE under
REPRODUCED-AND-LOCATED; motivation TRUE with the readout fiber >= 3 and
the third, step-normalised law printed.  SETTLEMENT = PARTIAL, FAILED
LINK = TARGETS.

DISCIPLINE.  RUNBOOK complete: the TWELVE v14-origin engravings -- the
ten of 2026-08-09 and the two of 2026-08-10 (#82: the CLI-contract
minimum; comparator independence, strengthened).  This unit ships an
argv-parsed CLI (unknown flags exit 2; --selftest; --mutant NAME;
--list-mutants; --out-dir), a verdict comparator that shares no code, no
inputs and no typed literals with its builder, a mutant harness whose
`reaches_target` is MEASURED (the named gate's own predicate evaluated
on the clean object and again on a mutated one), per-row drift
falsifiers for every anchor and every verbatim row, and a paper that is
byte-anchored at delivery.

Exact arithmetic only: int and fractions.Fraction.  No float anywhere;
an AST guard over this file's own source proves it.  Every wall-clock
number goes to stderr and reaches neither the output file nor the
receipt, so two plain runs are byte-identical.
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

# ======================================================================
# THE CLI  (RUNBOOK 14, v14 #82 -- the CLI-contract minimum)
# ======================================================================
USAGE = """usage: gmain_exact.py [--selftest] [--mutant NAME] [--list-mutants]
                      [--out-dir DIR] [--help]

  (no flags)       the plain delivery run: writes gmain_output.txt and
                   gmain_receipt.json into the DEFAULT OUTPUT DIRECTORY,
                   which is this file's own directory and nowhere else.
  --selftest       corrupt one declared anchor, confirm the run exits 1,
                   and write NOTHING.  Exit 1 on success of the test.
  --mutant NAME    evaluate ONE declared falsifier in isolation and
                   report the named gate's own predicate on the clean
                   object and on the mutated one.  Writes nothing.
                   Exit 0 iff the mutant reaches its gate and kills it.
  --list-mutants   print the declared falsifier registry and exit 0.
  --out-dir DIR    write the two artifacts into DIR instead of the
                   default.  A plain run never writes anywhere else.
  --help           print this text and exit 0.

Any other argument is an ERROR: the CLI rejects unknown flags with
exit 2 rather than ignoring them (RUNBOOK 14, v14 #82)."""

# The declared falsifier registry.  `--list-mutants` prints it without
# running the pipeline, and G-MUTANT-REGISTRY gates that the set of
# falsifiers actually evaluated is exactly this list.
MUTANT_REGISTRY = [
    'MUT-VERBATIM-DRIFT', 'MUT-PATH-DRIFT', 'MUT-PROBE-UNRESOLVED',
    'MUT-ANCHOR-DRIFT', 'MUT-PAPER-BYTES', 'MUT-FLOAT-LEAK',
    'MUT-LAYER-DRIFT', 'MUT-ZERO-PRICE', 'MUT-K1-BREAK',
    'MUT-FLOW-HORIZON', 'MUT-BLOCK-MERGE', 'MUT-MONO-UNSCOPED',
    'MUT-ATOMS-UNSCOPED', 'MUT-MISNORMALIZED', 'MUT-IDENTITY-BREAK',
    'MUT-DEVIATION-UNLOCATED', 'MUT-HOLONOMY-DRIFT', 'MUT-HOLONOMY-VERDICT',
    'MUT-REC-CORRUPT',
    'MUT-COUNT-CONTROL-CLEAN', 'MUT-3EVENT-DRIFT', 'MUT-LEG-PATTERN',
    'MUT-F8-MECHANISM', 'MUT-PRUNE-LAX', 'MUT-CENSUS-SHADOW-DRIFT',
    'MUT-LAWVALUE-DRIFT', 'MUT-READOUT-FIBER-COLLAPSE',
    'MUT-MULTIPLICITY-DRIFT', 'MUT-BLINDNESS-FLIP',
    'MUT-RESIDUE-DRIFT', 'MUT-TOKENSCAN-BLIND', 'MUT-RENEWAL-CORRUPT',
    'MUT-SCREEN-FLIP', 'MUT-CK-CORRUPT', 'MUT-EQ22-SIGN',
    'MUT-PADDING-DROP', 'MUT-CRB-COLLAPSE', 'MUT-CRA-BRIDGE',
    'MUT-WCROSS-CLAIM', 'MUT-44-MERGE', 'MUT-INVENTORY-RECLASS',
    'MUT-SCRAMBLE-EQ', 'MUT-QUOTIENT-SCRAMBLE',
    'MUT-SETTLEMENT-ONEWAY', 'MUT-SETTLEMENT-DESYNC',
    'MUT-SETTLEMENT-LAX', 'MUT-REGISTER-DROP', 'MUT-CLI-BLIND',
    'MUT-PAPER-CLAIM-DROP', 'MUT-PROSE-NUMBER', 'MUT-COVERAGE-LAX',
    'MUT-COMPLIANCE-FALSE', 'MUT-WAIVER-FALSE', 'MUT-CENSUS-LAX',
    'MUT-VERDICT-APPEND', 'MUT-VERDICT-SWAP', 'MUT-VERDICT-TRUNC',
    'MUT-VERDICT-DROP', 'MUT-VERDICT-RETYPE', 'MUT-VERDICT-DESYNC'
]


def _cli(argv):
    """argv parsing.  Unknown flags are REJECTED (exit 2), never
    ignored.  Returns (selftest, mutant_name, out_dir)."""
    selftest = False
    mut = None
    outdir = None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == '--help':
            sys.stdout.write(USAGE + "\n")
            raise SystemExit(0)
        if a == '--list-mutants':
            sys.stdout.write("\n".join(MUTANT_REGISTRY) + "\n")
            sys.stdout.write(f"{len(MUTANT_REGISTRY)} declared "
                             f"falsifiers.\n")
            raise SystemExit(0)
        if a == '--selftest':
            selftest = True
            i += 1
            continue
        if a == '--mutant':
            if i + 1 >= len(argv):
                sys.stderr.write("--mutant needs a NAME\n" + USAGE + "\n")
                raise SystemExit(2)
            mut = argv[i + 1]
            if mut not in MUTANT_REGISTRY:
                sys.stderr.write(f"unknown mutant {mut!r}; see "
                                 f"--list-mutants\n")
                raise SystemExit(2)
            i += 2
            continue
        if a == '--out-dir':
            if i + 1 >= len(argv):
                sys.stderr.write("--out-dir needs a DIR\n" + USAGE + "\n")
                raise SystemExit(2)
            outdir = argv[i + 1]
            i += 2
            continue
        sys.stderr.write(f"unknown argument {a!r}\n" + USAGE + "\n")
        raise SystemExit(2)
    return selftest, mut, outdir


SELFTEST, MUT_ONLY, _OUTDIR_FLAG = _cli(sys.argv[1:])
# THE DEFAULT OUTPUT PATH, explicit: this file's own directory.  A plain
# run writes there and nowhere else; a reviewer's scratch copy therefore
# writes beside itself and can never clobber the delivery.
OUT_DIR = _OUTDIR_FLAG if _OUTDIR_FLAG is not None else os.path.dirname(SELF)
WRITES_ALLOWED = (not SELFTEST) and (MUT_ONLY is None)
WRITTEN = []


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


def finish(code):
    """The single exit path.  Artifacts are written ONLY on a plain run
    that reaches here; --selftest and --mutant write nothing."""
    if WRITES_ALLOWED:
        op = os.path.join(OUT_DIR, 'gmain_output.txt')
        rp = os.path.join(OUT_DIR, 'gmain_receipt.json')
        with open(op, 'w', encoding='utf-8') as f:
            f.write("\n".join(OUT_LINES) + "\n")
        WRITTEN.append(op)
        if RECEIPT_BOX:
            with open(rp, 'w', encoding='utf-8') as f:
                json.dump(RECEIPT_BOX[0], f, indent=1, sort_keys=True,
                          default=str)
                f.write("\n")
            WRITTEN.append(rp)
    sys.stdout.write("\n".join(OUT_LINES) + "\n")
    sys.stdout.write(f"[files written: {len(WRITTEN)}]\n")
    prog("done")
    sys.exit(code)


RECEIPT_BOX = []

# ======================================================================
# THE GATE / MUTANT / ANCHOR MACHINERY
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


def mutant(name, target, injects, clean, mutated, detail):
    """A declared falsifier at the #34 standard, MEASURED.

    `clean`   -- the TARGET GATE'S OWN PREDICATE evaluated on the
                 unmutated object.  Must be True, or the mutant does not
                 reach a live gate.
    `mutated` -- THE SAME PREDICATE evaluated on a MUTATED object.  Must
                 be False, or the gate does not see the injection.

    `reaches_target` is therefore computed from the observed pair, never
    asserted (RUNBOOK 14, v14 #34; the Gamma-main instrument round found
    36 unmeasured reach claims here)."""
    reaches = bool(clean) and not bool(mutated)
    killed = reaches
    MUTANTS.append(dict(mutant=name, target=target, injects=injects,
                        predicate_on_clean_object=bool(clean),
                        predicate_on_mutated_object=bool(mutated),
                        reaches_target=reaches, killed=killed,
                        detail=detail))
    if MUT_ONLY is None or MUT_ONLY == name:
        emit(f"  [{'KILLED' if killed else 'SURVIVED'}] {name} -> "
             f"{target}: predicate on the clean object {bool(clean)}, on "
             f"the mutated object {bool(mutated)}; {detail}")
    return killed


ANCHOR_ROWS = []


def anchor(name, expected, measured, what):
    ok = (expected == measured)
    GATES.append(dict(name=name, kind='ANCHOR', statement=what,
                      passed=ok, detail=f"expected {expected!r}, "
                                        f"measured {measured!r}",
                      falsifiers=[], waiver=None))
    ANCHOR_ROWS.append(dict(name=name, expected=expected,
                            measured=measured, what=what, ok=ok))
    emit(f"  [{'PASS' if ok else 'ANCHOR-FAIL'}] {name}: {what} -- "
         f"expected {expected!r}, measured {measured!r}")
    if not ok:
        ANCHOR_FAIL.append(name)
    return ok


def perturb(v):
    """A deterministic value-perturbation used by the per-row drift
    sweeps.  The only property required is perturb(v) != v."""
    if isinstance(v, bool):
        return not v
    if isinstance(v, int):
        return v + 1
    if isinstance(v, str):
        return v + '~'
    if isinstance(v, list):
        return v + ['~']
    if isinstance(v, tuple):
        return v + ('~',)
    if isinstance(v, dict):
        d = dict(v)
        d['~'] = 0
        return d
    return ('~', repr(v))


# ======================================================================
# P0 -- PROVENANCE BY DECLARED COMMIT SHA  (RUNBOOK 14, v14 #62)
# ======================================================================
SHA_TREE = 'f40f5e1'          # the pin's own commit: the frozen v10/v11
SHA_GPREP = '0f5d57eef77f'    # Gamma-prep, v14 #63
SHA_R6BP = 'd042ef1'          # the R6b' adjudication register, v14 #62
SHA_CRA = '94df5ad'           # CR-A delivered, v14 #41
SHA_CRB = 'fbc3a81'           # CR-B delivered, v14 #37
SHA_R4 = '264cb54'            # R4 delivered, v14 #54
# THE REPAIR COMMIT, declared: the joint adjudication that binds this
# repair, and the RUNBOOK carrying the two 2026-08-10 (#82) engravings.
# The pin froze before either existed; the adjudication is the frozen
# carrier of the corrected settlement and of orders R-GM-1..11, and it
# is read at its own committed sha exactly like every other source.
SHA_ADJ = '685d483'           # v14 #82, the joint adjudication

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
    ('S-ADJ', SHA_ADJ, 'v14/note-gmain-adjudication.md', '972e54741330',
     'THE JOINT ADJUDICATION (v14 #82): the corrected settlement and '
     'the eleven binding repair orders this delivery executes'),
    ('S-R0', SHA_TREE, 'v14/note-r0-founding-pin.md', 'e9d2bedff244',
     'the v14 founding pin (the inheritance floor)'),
    ('S-RUNBOOK', SHA_ADJ, 'RUNBOOK.md', 'f5adab0c479d',
     'the programme runbook at the repair commit: all addenda, '
     'including the two 2026-08-10 #82 engravings this repair must meet'),
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
     'carrier of the census shadow; the R6b-prime artifacts themselves '
     'are MID-REPAIR and are NOT read by this unit'),
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
    'v14/review-gmain-{operator,effectus,instrument}.md -- the three '
    'frozen reviews are NOT read at run time; the adjudication note is '
    'the frozen carrier of every ruling this repair executes',
]

# THE v14 LOG #4 ERRATUM, carried as a frozen declaration (never read at
# run time -- the ledger is a forbidden runtime input, #46).
ERRATUM_4 = ('v14 LOG #4 (R0 companion-hash erratum): this unit reads '
             'neither v13/paper-rsq-reposed-square.md nor '
             'v13/paper-top-topology.md, and no verdict segment '
             'descends from R0 rows I2/I3.')

PAPER_PATH = 'v14/paper-12-gamma-main.md'
# THE PAPER'S OWN BYTE ANCHOR (adjudication R-GM-6; #62 corrected spec).
# The paper is this unit's fourth deliverable and is not committed at
# delivery time, so the previous delivery read it from the worktree
# UNANCHORED -- the residue through which the instrument round drove a
# quotation-meaning inversion and three false prose numbers at exit 0.
# It is now hash-pinned exactly like every cross-unit source: the
# delivered bytes are frozen before the delivery run and the run refuses
# to proceed against any other bytes.
PAPER_SHA_EXPECTED = '05f5dc7c7273'

# ----------------------------------------------------------------------
# VERBATIM-TEXT ANCHORS (#62 corrected spec).  Each row binds QUOTE
# FIDELITY: the quotation as it appears in THIS unit's paper against the
# source's COMMITTED bytes.  Rows are evaluated FIRST and the evaluation
# genuinely SHORT-CIRCUITS: if any row fails, byte anchors are not
# evaluated at all and the run exits 1.  Every consumer gate named below
# exists, is non-literal (it reads a measured quantity), and is falsified
# by a declared mutant whose reach is MEASURED.  Every row additionally
# carries its OWN per-row drift falsifier (the sweep below), so coverage
# is by reach and not by naming.
# ----------------------------------------------------------------------
VERBATIM = [
    ('V-TARGETS', 'S-R6BP',
     'reproduce (3/7,1/7,3/7) at leg 1 and\n(4/9,1/9,4/9) at leg 2.',
     'T1-CENSUS-SHADOW'),
    ('V-CENSUS-BIRTH', 'S-R6BP',
     '(C(n−1,2) equiprobable\nconfigurations; position marginal '
     'uniform on n−1)', 'T1-CENSUS-SHADOW'),
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
    # R-GM-13: the SCOPED form of the monotonicity sentence --
    # Gamma-prep's own section 7, not its abstract's unscoped one,
    # which is what the previous delivery inherited and propagated.
    ('V-LADDER', 'S-GPP',
     'Over all\n$30{,}728$ transitions out of every history of depth '
     '$< 5$,\nholdings-shrinking transitions: $0$.',
     'G-MONOTONICITY-SCOPE'),
    ('V-GPREP-ATOMSCOPE', 'S-GPP',
     'scope = 2 actors, transport depth <= 6, MATCHED horizon, '
     'primary grain', 'G-ATOMS-IMPORT-SCOPE'),
    ('V-ADJ-TARGETS', 'S-ADJ',
     'the targets were census\n  statistics at birth (their frozen '
     'source defines them by leaf\n  counts); the target test is Γ-free '
     'and off-carrier (token-scan\n  proof); the count readout breaks '
     'the mandatory negative control\n  (REC gains holonomy; CK fails; '
     '0/544 columns stochastic — not a\n  law).', 'G-SETTLEMENT'),
    ('V-ADJ-HOLONOMY', 'S-ADJ',
     'an agreement demand that is unsatisfiable by an\n  identity '
     '(r_k = r_q·G/G at 1,546/1,546, deviation forced exactly at\n  '
     'non-descent)', 'T2-HOLONOMY'),
    ('V-ADJ-MOTIVATION', 'S-ADJ',
     "I-READOUT's fiber\n  is ≥3 (the third, step-normalised law "
     'measured: 15/38, 5/19,\n  13/38)', 'T8-ATOMS'),
    ('V-ADJ-CARRIER', 'S-ADJ',
     "**CONG-185 supersedes MENU+G**: d74's own coarsest weighted\n"
     'congruence has descent at every horizon, zero multi-valued edges,\n'
     'all 44 curvature squares intact, q-holonomy ⟨2,3⟩, **k-holonomy\n'
     'collapsing back to ⟨2,3⟩** (the enlargement disappears)',
     'G-NEXT-ITERATION'),
    ('V-RB-CLI', 'S-RUNBOOK',
     'every unit ships an argv-parsed CLI that rejects\nunknown flags '
     '(exit 2), a `--selftest` that corrupts one\nanchor, confirms exit '
     '1, and writes nothing, and a\n`--mutant NAME` harness',
     'G-CLI-CONTRACT'),
    ('V-RB-COMPARATOR', 'S-RUNBOOK',
     'a verdict comparator shares\nNOTHING with its builder — neither '
     'code, nor inputs, nor\ntyped literals', 'G-VERDICT-EQUALITY'),
]

sec("v14 GAMMA-MAIN -- THE GEOMETRY-UPDATE LAW (paper-12), REPAIRED")
emit("  Pin: v14/note-gmain-pin.md, v14 ledger #64.")
emit("  Repair: v14/note-gmain-adjudication.md, v14 ledger #82, orders "
     "R-GM-1 .. R-GM-11.")
emit("  Provenance by declared COMMIT SHA (#62): tree=" + SHA_TREE
     + ", adjudication=" + SHA_ADJ + ", gprep=" + SHA_GPREP
     + ", r6bp=" + SHA_R6BP + ", cra=" + SHA_CRA + ", crb=" + SHA_CRB
     + ", r4=" + SHA_R4 + ".")
emit("  Every cross-unit read goes through `git show <sha>:<path>`.  "
     "Worktree bytes and `git show HEAD:` are mutable state and are "
     "read for NO source.  THIS UNIT'S OWN PAPER is read from the "
     "worktree -- it is the fourth deliverable and is not committed at "
     "delivery time -- and it is BYTE-ANCHORED here against its frozen "
     "sha256-12, which is what closes the unanchored-read residue.")
emit("")
emit("  CLI (RUNBOOK 14, v14 #82): argv-parsed; unknown flags exit 2; "
     "--selftest corrupts one anchor and writes nothing; --mutant NAME "
     "evaluates one declared falsifier in isolation; --list-mutants; "
     "--out-dir.  THE DEFAULT OUTPUT DIRECTORY IS THIS FILE'S OWN "
     "DIRECTORY: a plain run writes there and nowhere else.")
emit(f"  mode: selftest={SELFTEST}, mutant={MUT_ONLY!r}, "
     f"writes_allowed={WRITES_ALLOWED}")
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

_pp = os.path.join(REPO, PAPER_PATH)
if not os.path.exists(_pp):
    emit(f"  THE PAPER {PAPER_PATH} IS ABSENT -- this unit's fourth "
         f"deliverable is a REQUIRED input to the quote-fidelity, "
         f"claim and prose-sweep gates.  exit 1.")
    finish(1)
PAPER_TEXT = open(_pp, encoding='utf-8').read()

VB_ROWS = []
_vb_all = True
for vid, sid, quote, consumer in VERBATIM:
    body = SRC[sid][4]
    in_src = body is not None and quote in body
    in_paper = quote in PAPER_TEXT
    ok = in_src and in_paper
    VB_ROWS.append(dict(id=vid, source=sid, consumer_gate=consumer,
                        chars=len(quote), in_source=in_src,
                        in_paper=in_paper, ok=ok, quote=quote,
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
    finish(1)

# --- the per-row VERBATIM drift sweep (adjudication R-GM-7: coverage by
# --- reach, not by naming).  Every row gets its OWN falsifier: perturb
# --- that row's quotation by one character and re-evaluate THAT ROW's
# --- own predicate.  A row is covered only if its own predicate flips.
VB_DRIFT = []
for r in VB_ROWS:
    q2 = r['quote'][:-1] + '§'
    body = SRC[r['source']][4]
    flips = not ((body is not None and q2 in body) and q2 in PAPER_TEXT)
    VB_DRIFT.append(dict(id=r['id'], own_predicate_flips=flips))
_vbd = sum(1 for r in VB_DRIFT if r['own_predicate_flips'])
gate('G-VERBATIM-ROW-DRIFT', 'MUST',
     'EVERY verbatim row carries its own falsifier: a one-character '
     'perturbation of that row\'s quotation flips THAT ROW\'s own '
     'predicate, so quote-fidelity coverage is by reach and not by a '
     'mutant that names one row and touches no other',
     _vbd == len(VB_ROWS),
     f"{_vbd} of {len(VB_ROWS)} verbatim rows falsified by their own "
     f"one-character drift",
     falsifiers=['MUT-VERBATIM-DRIFT'])
_VB_DRIFT_MUT = [dict(r) for r in VB_DRIFT]
_VB_DRIFT_MUT[0]['own_predicate_flips'] = False
_vbd_mut = sum(1 for r in _VB_DRIFT_MUT if r['own_predicate_flips'])
mutant('MUT-VERBATIM-DRIFT', 'G-VERBATIM-ROW-DRIFT',
       'a sweep in which one verbatim row fails to flip under its own '
       'perturbation (the short-quotation failure mode: a quotation so '
       'small that its perturbation also occurs in the source)',
       _vbd == len(VB_ROWS),
       _vbd_mut == len(VB_ROWS),
       f"the clean sweep flips {_vbd} of {len(VB_ROWS)} rows; the "
       f"mutated sweep flips {_vbd_mut}, short of the row total, and "
       f"the gate's own predicate turns false on it")
# the verbatim rows ENTER THE GATE LEDGER (the previous delivery left
# them outside both never-falsified censuses, so the "88 gates"
# denominator excluded thirteen enforced rows).
for _i, _r in enumerate(VB_ROWS):
    GATES.append(dict(name=_r['id'], kind='VERBATIM',
                      statement=f"quote fidelity: the quotation from "
                                f"{_r['source']} in {PAPER_PATH} "
                                f"against the source's committed bytes; "
                                f"consumer gate {_r['consumer_gate']}",
                      passed=_r['ok'],
                      detail=f"{_r['chars']} chars; in source "
                             f"{_r['in_source']}; in paper "
                             f"{_r['in_paper']}; own drift flips "
                             f"{VB_DRIFT[_i]['own_predicate_flips']}",
                      falsifiers=[], waiver=None))

emit("")
emit("  BYTE ANCHORS (evaluated only after the verbatim rows pass):")
BY_ROWS = []
for sid, sha, path, want, ped in SOURCES:
    body = SRC[sid][4]
    got = h12(body) if body is not None else None
    _want = perturb(want) if (SELFTEST and sid == 'S-D74N') else want
    if _want != want:
        emit(f"  --selftest: the expected digest of {sid} is CORRUPTED "
             f"from {want!r} to {_want!r} before evaluation.")
    ok = anchor(f"A-{sid}", _want, got, f"sha256-12 of {path} @ {sha}")
    BY_ROWS.append(dict(id=sid, sha=sha, path=path, expected=_want,
                        measured=got, ok=ok, pedigree=ped))

# THE PAPER'S OWN BYTE ANCHOR -- the fourth deliverable, hash-pinned.
_paper_sha = h12(PAPER_TEXT)
anchor('A-PAPER-SELF', PAPER_SHA_EXPECTED, _paper_sha,
       f"sha256-12 of THIS UNIT'S OWN {PAPER_PATH}, read from the "
       f"worktree because it is the fourth deliverable and is not "
       f"committed at delivery time; the bytes are frozen before the "
       f"delivery run and anchored here")

emit("")
emit("  PATH-VALUE STABILITY ACROSS DECLARED SHAS (#62's adopted core): "
     "the same path read at declared shas must carry the same value; a "
     "path drift or a tree drift must die here.")
_STAB_PATHS = ('v10/note-d74-transport-holonomy-result.md',
               'v11/note-u1b-renewal-class-sweep.md',
               'v10/code/d42b1_transport_exact.py',
               'v11/note-u1-indivisibility-census.md',
               'v10/data/d74_transport_holonomy_exact.out')


def stability(paths):
    out = []
    for path in paths:
        a = committed(SHA_TREE, path)
        b = committed(SHA_GPREP, path)
        c = committed(SHA_ADJ, path)
        out.append((path, a is not None and b is not None
                    and c is not None and a == b and b == c))
    return out


_stab = stability(_STAB_PATHS)
_stab_mut = stability(_STAB_PATHS
                      + ('v10/note-d74-transport-holonomy-RESULT.md',))
gate('G-PATH-VALUE-STABILITY', 'MUST',
     'each declared frozen-tree path carries identical bytes at the pin '
     'commit, at the Gamma-prep commit and at the repair commit',
     all(ok for _, ok in _stab),
     f"{sum(1 for _, ok in _stab if ok)} of {len(_stab)} paths stable "
     f"across {SHA_TREE}, {SHA_GPREP} and {SHA_ADJ}",
     falsifiers=['MUT-PATH-DRIFT'])
mutant('MUT-PATH-DRIFT', 'G-PATH-VALUE-STABILITY',
       'a drifted path (one letter of the filename recased) added to '
       'the declared stability set',
       all(ok for _, ok in _stab),
       all(ok for _, ok in _stab_mut),
       f"the drifted path resolves at 0 of 3 shas, so the stability "
       f"list gains a False and the gate's own predicate turns "
       f"{all(ok for _, ok in _stab_mut)}")

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


def resolves(obj, path):
    try:
        pv(obj, path)
        return True
    except Exception:
        return False


# EVERY declared probe must RESOLVE (adjudication R-GM-9).  The previous
# delivery declared a probe into Gamma-prep's receipt at a path that does
# not exist in it; `pv` raised, the exception was swallowed, the row was
# filed unanchored and was never printed, so the one read of the
# inherited delta* = 1 datum read nothing, silently.  An unresolvable
# declared probe now ABORTS.
PV_DECL = [
    ('PV-CRA-HEAD', 'CRA', CRA, 'verdict_head',
     'CRA-BLOCKED-AT-STATIC-GEOMETRY'),
    ('PV-CRA-CENSUS', 'CRA', CRA, 'verdict_segments/2',
     'CENSUS=8192|ADVANCING=2976|ADMISSIBLE=1232'),
    ('PV-CRA-FORCED', 'CRA', CRA, 'verdict_segments/3',
     'FORCED=2|FORCED-ADVANCING=0'),
    ('PV-CRB-HEAD', 'CRB', CRB, 'verdict_head',
     'CRB-BLOCKED-AT-NO-PINNED-STOCHASTIC-LAW'),
    ('PV-CRB-DIMLAW', 'CRB', CRB, 'per_interval_law/pinned_dim_law',
     'n - 2'),
    ('PV-CRB-N4', 'CRB', CRB, 'per_interval_law/rows/3/pinned_simplex_dim',
     2),
    ('PV-CRB-N4T', 'CRB', CRB, 'per_interval_law/rows/3/pinned_transitive',
     False),
    ('PV-CRB-N4ORB', 'CRB', CRB, 'per_interval_law/rows/3/pinned_orbits',
     3),
    ('PV-R4-HEAD', 'R4', R4R, 'verdict/head', 'R4-DEFECT-PRESENT'),
    ('PV-R4-SCALE', 'R4', R4R, 'admissible_scales', [4]),
    # R-GM-9: the ACTUAL key in Gamma-prep's FLAT receipt.  The
    # receipt serialises its exact rationals as STRINGS, so the
    # committed value of this key is the string '1', not the int 1 --
    # and an anchor that declared the int would die on a type
    # mismatch rather than on a physics one.  The row-wise
    # cross-check below reads the same datum by a second path.
    ('PV-GPREP-DELTA', 'GPREP', GPR, 'B2_best_delta', '1'),
    ('PV-GPREP-DELTA-ROW', 'GPREP', GPR, 'B2_profile_rows/0/5', '1'),
    ('PV-GPREP-ATOM', 'GPREP', GPR, 'B2_atom_found', True),
    ('PV-GPREP-NUBLOCK', 'GPREP', GPR, 'B2_nu_block_size', 1365),
    # R-GM-13: the monotonicity claim's own denominator, read by path
    ('PV-GPREP-MONO', 'GPREP', GPR, 'mono_pairs', 30728),
    ('PV-GPREP-SHRINK', 'GPREP', GPR, 'mono_shrinking', 0),
    ('PV-GPREP-LEVELS', 'GPREP', GPR, 't_per_level',
     [1, 8, 60, 452, 3448, 26760, 213040]),
]
PV_ROWS = []
_unresolved = []
for pid, owner, obj, path, want in PV_DECL:
    if not resolves(obj, path):
        _unresolved.append((pid, owner, path))
        continue
    got = pv(obj, path)
    ok = anchor(pid, want, got, f"path-value {owner}:{path}")
    PV_ROWS.append(dict(id=pid, owner=owner, path=path,
                        expected=str(want), measured=str(got), ok=ok,
                        anchored=True, resolved=True))
gate('G-PROBE-RESOLUTION', 'MUST',
     'EVERY declared path-value probe RESOLVES in its source object; an '
     'unresolvable declared probe aborts the run and is never swallowed '
     'into an unanchored row (adjudication R-GM-9, #46 in spirit)',
     len(_unresolved) == 0,
     f"{len(PV_ROWS)} declared probes, {len(_unresolved)} unresolvable "
     f"{_unresolved}",
     falsifiers=['MUT-PROBE-UNRESOLVED'])
mutant('MUT-PROBE-UNRESOLVED', 'G-PROBE-RESOLUTION',
       "the previous delivery's declared probe path "
       "armB/atoms/0/delta_matched_primary into Gamma-prep's receipt",
       len(_unresolved) == 0,
       resolves(GPR, 'armB/atoms/0/delta_matched_primary'),
       "Gamma-prep's receipt is a FLAT dict with no armB key -- the "
       "delta* = 1 datum lives at B2_best_delta -- so the old path does "
       "not resolve and the resolution gate turns false on it")

if _unresolved:
    emit(f"  UNRESOLVABLE DECLARED PROBE {_unresolved} -- exit 1.")
    finish(1)
if ANCHOR_FAIL:
    emit(f"  ANCHOR FAILURE {ANCHOR_FAIL} -- exit 1.")
    if SELFTEST:
        emit("")
        emit("  ===== SELFTEST RESULT =====")
        emit(f"  corrupted anchor      : A-S-D74N")
        emit(f"  anchors failed        : {ANCHOR_FAIL} "
             f"(exactly one, as designed: "
             f"{ANCHOR_FAIL == ['A-S-D74N']})")
        emit(f"  files written         : {len(WRITTEN)} "
             f"(writes_allowed={WRITES_ALLOWED})")
        emit(f"  exit code             : 1")
        emit("  SELFTEST PASSES iff the three lines above read "
             "['A-S-D74N'], 0 and 1.")
    finish(1)
if SELFTEST:
    emit("  SELFTEST FAILED: the corrupted anchor did not fail the run.")
    finish(1)

mutant('MUT-PAPER-BYTES', 'A-PAPER-SELF',
       "one byte of this unit's own paper changed after the delivery "
       'freeze -- the residue through which a quotation-meaning '
       'inversion and three false prose numbers reached exit 0',
       PAPER_SHA_EXPECTED == _paper_sha,
       PAPER_SHA_EXPECTED == h12(PAPER_TEXT + '§'),
       f"the frozen paper hashes to {_paper_sha}; a single appended "
       f"character hashes to {h12(PAPER_TEXT + chr(167))}, so the "
       f"self-anchor's own predicate turns false")

# ======================================================================
# P2 -- THE AST FLOAT-GUARD over this file's own source
# ======================================================================
sec("P2 -- THE AST FLOAT-GUARD")
_src = open(SELF, encoding='utf-8').read()


def floatguard(text):
    t = ast.parse(text)
    fl_ = sorted({n.lineno for n in ast.walk(t)
                  if isinstance(n, ast.Constant)
                  and isinstance(n.value, float)})
    bn = sorted({n.lineno for n in ast.walk(t)
                 if isinstance(n, ast.Name)
                 and n.id in ('numpy', 'np', 'math')})
    dv = sorted({n.lineno for n in ast.walk(t)
                 if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Div)})
    return fl_, bn, dv


_floats, _bad_names, _truediv = floatguard(_src)
_leak_src = _src.replace("OUT_LINES = []", "OUT_LINES = []\n_leak = 0.5", 1)
_lf, _lb, _ld = floatguard(_leak_src)
gate('G-FLOATGUARD', 'MUST',
     "an AST scan of this source finds no float literal and no "
     "numpy/math name; every division is between int/Fraction and is "
     "therefore exact",
     not _floats and not _bad_names,
     f"float literals {_floats}; banned names {_bad_names}; "
     f"division sites {len(_truediv)} (all int/Fraction)",
     falsifiers=['MUT-FLOAT-LEAK'])
mutant('MUT-FLOAT-LEAK', 'G-FLOATGUARD',
       'a float literal inserted into a COPY of this file\'s own source, '
       'which is then re-scanned by the same guard',
       not _floats and not _bad_names,
       not _lf and not _lb,
       f"the mutated source carries a float constant at line {_lf}, so "
       f"the guard's own predicate turns false on it")

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
_LAYER_DEFS = ('candidates_for', 'admissible', 'canon', 'View',
               'event_poset')


def layer_ok(prefix, ns):
    return (all(n in ns for n in _LAYER_DEFS)
            and 'sys.exit' not in prefix and '\nprint(' not in prefix)


_PREFIX_MUT = _PREFIX + "\nsys.exit(0)\n"
gate('G-LAYER-SINGLE-SOURCE', 'MUST',
     'the transport grammar is exec\'d from the COMMITTED bytes of the '
     'pinned layer, pre-print slice only; nothing about admission or '
     'pricing is re-implemented in this unit, and the ported slice '
     'contains no exit and no print',
     layer_ok(_PREFIX, NS),
     f"prefix {len(_PREFIX)} chars; defs "
     f"{sorted(n for n in _LAYER_DEFS if n in NS)}; "
     f"exit-free {'sys.exit' not in _PREFIX}",
     falsifiers=['MUT-LAYER-DRIFT'])
mutant('MUT-LAYER-DRIFT', 'G-LAYER-SINGLE-SOURCE',
       'an exit smuggled into the ported layer slice',
       layer_ok(_PREFIX, NS), layer_ok(_PREFIX_MUT, NS),
       "the mutated slice carries sys.exit, so the gate's own "
       "exit-free conjunct turns false")


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


def fl(seq):
    return "[" + ", ".join(str(x) for x in seq) + "]"


def frl(seq):
    return "(" + ", ".join(str(x) for x in seq) + ")"


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
    'readout': 'THE FIBER IS AT LEAST THREE, all three measured.  '
               'PRIMARY: the STEP-NORMALISED law q(e|h)/M(h), which is '
               'exactly the pinned kernel k_1 (proved on the carrier '
               'below).  Also measured: RAW-PRODUCT (the unnormalised '
               'weight product the previous delivery called '
               '"occupancy") and COUNT (equiprobable admissible '
               'objects).  A fourth -- the H4 chain Gamma itself is '
               'built from -- is EXCLUDED-BY-CAP on the leg ensembles.',
    'census shadow': 'the R6b-prime register\'s (3/7,1/7,3/7) and '
                     '(4/9,1/9,4/9) are leaf-count statistics of the '
                     'external transport census: a DECLARED CONTROL, '
                     'never a target of this unit (adjudication R-GM-2)',
    'provenance': 'declared commit shas; 24 hash-pinned sources plus '
                  "this unit's own paper, byte-anchored",
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


def potentials(prices):
    """The finite-horizon potentials G(h, r) of a declared price law."""
    out = {}
    for h in sorted(CACHE, key=lambda x: -len(x)):
        out[(h, 0)] = Fr(1)
        for r in range(1, CAP_ANCHOR - len(h) + 1):
            out[(h, r)] = sum(prices[(h, e)] * out[(h + (e,), r - 1)]
                              for e, q in CACHE[h])
    return out


PRICE = {(h, e): Fr(q) for h in CACHE for e, q in CACHE[h]}
G = potentials(PRICE)
GROOT = [str(G[(ROOT, r)]) for r in range(1, CAP_ANCHOR + 1)]
anchor('A-POTENTIALS', ['2', '4', '257/32', '1035/64', '4173/128'],
       GROOT, "Gamma-prep's committed transport potentials G_D, D = 1..5")

MU = {ROOT: Fr(1)}
for h in sorted(CACHE, key=len):
    if h:
        MU[h] = MU[h[:-1]] * PRICE[(h[:-1], h[-1])]


def kernel(h, e, r, GG=None, PP=None):
    """The pinned relative-horizon kernel k_r(e|h)."""
    GG = G if GG is None else GG
    PP = PRICE if PP is None else PP
    return PP[(h, e)] * GG[(h + (e,), r - 1)] / GG[(h, r)]


def k_of(h, e, r):
    return kernel(h, e, r)


def properness(GG, PP):
    """Sum_e k_r(e|h) over the carrier: violations, and strict-positivity
    violations."""
    pr, po = 0, 0
    for h in CARRIER:
        for r in range(1, CAP - len(h) + 1):
            s = sum(kernel(h, e, r, GG, PP) for e, q in CACHE[h])
            if s != 1:
                pr += 1
            for e, q in CACHE[h]:
                if kernel(h, e, r, GG, PP) <= 0:
                    po += 1
    return pr, po


_pr_bad, _pos_bad = properness(G, PRICE)
# THE MACHINE-CHECKED FORCING (RUNBOOK 14, v14 #34): properness is not a
# fact about THESE prices.  Re-price every event by an arbitrary exact
# rational, rebuild the potentials from the re-priced law, and the
# identity still holds -- which is what "analytically forced" means and
# is what the waiver claims.
_ei = {}
for _h in sorted(CACHE, key=sk):
    for _e, _q in CACHE[_h]:
        _ei[(_h, _e)] = len(_ei)
PRICE2 = {k: v * Fr(_ei[k] + 2, _ei[k] + 1) for k, v in PRICE.items()}
G2 = potentials(PRICE2)
_pr_bad2, _pos_bad2 = properness(G2, PRICE2)
gate('G-KERNEL-PROPER', 'THEOREM-PASS',
     'sum_e k_r(e|h) = 1 is an IDENTITY of the construction (G is '
     'defined as the numerator sum); it is disclosed, not evidence',
     _pr_bad == 0 and _pr_bad2 == 0,
     f"{_pr_bad} violations over the carrier at the pinned price law; "
     f"{_pr_bad2} violations after an arbitrary exact re-pricing of "
     f"every one of the {len(PRICE)} priced events -- the forcing, "
     f"machine-checked",
     waiver='ANALYTICALLY FORCED, AND THE FORCING IS MACHINE-CHECKED: '
            'G(h,r) := sum_e q(e|h) G(h+e,r-1) and k_r divides by it, '
            'so the sum is 1 for every price law the construction '
            'admits; re-pricing every event by an arbitrary exact '
            'rational leaves 0 violations (RUNBOOK 14, v13 #208 + '
            'v14 #34)')
gate('G-KERNEL-POSITIVE', 'MUST',
     'the substantive properness gate: every kernel entry and every '
     'potential is strictly positive (a zero denominator is the only '
     'way the identity can break)',
     _pos_bad == 0, f"kernel entries <= 0: {_pos_bad}",
     falsifiers=['MUT-ZERO-PRICE'])
PRICE3 = dict(PRICE)
_zk = sorted(PRICE3, key=lambda z: (sk(z[0]), sk(z[1])))[0]
PRICE3[_zk] = Fr(0)
G3 = potentials(PRICE3)
_pr3, _pos3 = properness(G3, PRICE3)
mutant('MUT-ZERO-PRICE', 'G-KERNEL-POSITIVE',
       'one priced event zeroed, the potentials rebuilt from the '
       'zeroed law and the same positivity predicate re-evaluated',
       _pos_bad == 0, _pos3 == 0,
       f"the zeroed law leaves {_pos3} non-positive kernel entries over "
       f"the carrier, so the positivity gate's own predicate turns "
       f"false on it (and properness itself survives at {_pr3} "
       f"violations -- which is exactly why positivity is the "
       f"substantive companion)")

# --- THE STEP-NORMALISED READOUT IS THE PINNED KERNEL k_1 -------------
# The local menu mass M(h) = sum_e q(e|h) is NOT constant on the
# carrier, so a raw product of weights along a path is not a
# probability.  Normalising each step gives q/M -- and q/M IS k_1,
# because G(h,1) = M(h) by definition.  The step-normalised readout is
# therefore not a third ad-hoc choice: it is the r = 1 member of the
# very kernel family Gamma is built from.
MMASS = {h: sum(Fr(q) for e, q in CACHE[h]) for h in CARRIER}
_mcensus = Counter(str(v) for v in MMASS.values())


def k1_violations(rr):
    """Compared over every carrier history at which the horizon rr is
    available at all; deeper histories have no rr-horizon and are not
    tested (they are counted in the denominator below)."""
    bad, tested = 0, 0
    for h in CARRIER:
        if (h, rr) not in G or G[(h, rr)] == 0:
            continue
        for e, q in CACHE[h]:
            if (h + (e,), rr - 1) not in G:
                continue
            tested += 1
            if kernel(h, e, rr) != PRICE[(h, e)] / MMASS[h]:
                bad += 1
    return bad, tested


_k1_bad, _k1_tested = k1_violations(1)
_k2_bad, _k2_tested = k1_violations(2)
gate('G-K1-IS-THE-STEP-NORMALISER', 'MUST',
     'the local menu mass M(h) = sum_e q(e|h) is NOT constant on the '
     'carrier, so a raw product of weights along a path is not a '
     'probability; and the step-normalised weight q(e|h)/M(h) is '
     'EXACTLY the pinned kernel k_1, since G(h,1) = M(h).  The primary '
     'readout is therefore the r = 1 member of the kernel family the '
     'construction is built from, not a third ad-hoc choice',
     _k1_bad == 0 and len(_mcensus) > 1,
     f"M(h) census over the carrier {ctr(_mcensus)} -- {len(_mcensus)} "
     f"distinct values, so M is not constant; k_1 = q/M violations "
     f"{_k1_bad} of {_k1_tested} carrier kernel entries",
     falsifiers=['MUT-K1-BREAK'])
mutant('MUT-K1-BREAK', 'G-K1-IS-THE-STEP-NORMALISER',
       'the step-normaliser identified with the horizon-2 kernel k_2 '
       'instead of k_1',
       _k1_bad == 0 and len(_mcensus) > 1,
       _k2_bad == 0 and len(_mcensus) > 1,
       f"k_2 = q/M fails at {_k2_bad} of {_k2_tested} carrier kernel "
       f"entries, so the "
       f"gate's own identity conjunct turns false on the mutated "
       f"identification")

# --- the occupancy: the H4 chain's own law ---------------------------
GR = G[(ROOT, CAP)]
W = {h: MU[h] * G[(h, CAP - len(h))] / GR for h in CARRIER}
_cutmass = [sum(W[h] for h in CARRIER if len(h) == d)
            for d in range(CAP + 1)]
GR2 = G2[(ROOT, CAP)]
MU2 = {ROOT: Fr(1)}
for h in sorted(CACHE, key=len):
    if h:
        MU2[h] = MU2[h[:-1]] * PRICE2[(h[:-1], h[-1])]
_cutmass2 = [sum(MU2[h] * G2[(h, CAP - len(h))] / GR2
                 for h in CARRIER if len(h) == d) for d in range(CAP + 1)]
gate('G-CUT-ADDITIVITY', 'THEOREM-PASS',
     'the chained horizon kernel has cut mass 1 at every depth cut',
     all(m == 1 for m in _cutmass) and all(m == 1 for m in _cutmass2),
     f"cut masses {fl(_cutmass)} at the pinned price law; "
     f"{fl(_cutmass2)} after an arbitrary exact re-pricing -- the "
     f"forcing, machine-checked",
     waiver='ANALYTICALLY FORCED, AND THE FORCING IS MACHINE-CHECKED by '
            'induction from the properness identity: a chain of '
            'probability kernels has cut mass 1 at every cut, for every '
            'price law; the re-priced family gives 1 at all five cuts')

# --- N1: THE FLOW IDENTITY NEEDS ITS HORIZON NAMED --------------------
# w(h) k_r(e|h) = w(h+e) is the statement that makes the class law the
# exact conditional.  It holds at r = 4 - |h| and AT NO OTHER
# ADMISSIBLE HORIZON, and the previous delivery wrote it with r free.


def flow(fixed_r=None):
    ok, bad = 0, 0
    for h in CARRIER:
        if len(h) >= CAP:
            continue
        rs = ([CAP - len(h)] if fixed_r is None
              else [fixed_r] if fixed_r <= CAP - len(h) else [])
        for e, q in CACHE[h]:
            for r in rs:
                if W[h] * kernel(h, e, r) == W[h + (e,)]:
                    ok += 1
                else:
                    bad += 1
    return ok, bad


def flow_off_horizon():
    ok, bad = 0, 0
    for h in CARRIER:
        if len(h) >= CAP:
            continue
        for e, q in CACHE[h]:
            for r in range(1, CAP - len(h)):
                if W[h] * kernel(h, e, r) == W[h + (e,)]:
                    ok += 1
                else:
                    bad += 1
    return ok, bad


_flow_ok, _flow_bad = flow()
_off_ok, _off_bad = flow_off_horizon()
_flow1_ok, _flow1_bad = flow(1)
gate('G-FLOW-IDENTITY', 'MUST',
     'THE IDENTITY THAT MAKES THE CLASS LAW THE EXACT CONDITIONAL, WITH '
     'ITS HORIZON NAMED: w(h) k_{4-|h|}(e|h) = w(h+e) holds with zero '
     'violations, and at every OTHER admissible horizon it fails -- so '
     'the r in the identity is not free (operator N1)',
     _flow_bad == 0 and _off_bad > 0,
     f"at r = 4-|h|: {_flow_ok} transitions, {_flow_bad} violations; at "
     f"every other admissible r: {_off_bad} violations of "
     f"{_off_ok + _off_bad} tests",
     falsifiers=['MUT-FLOW-HORIZON'])
mutant('MUT-FLOW-HORIZON', 'G-FLOW-IDENTITY',
       'the identity evaluated at the fixed horizon r = 1 instead of '
       'the depth-matched r = 4-|h| (the free-r reading the previous '
       'delivery printed)',
       _flow_bad == 0 and _off_bad > 0,
       _flow1_bad == 0 and _off_bad > 0,
       f"at the fixed horizon r = 1 the identity fails at "
       f"{_flow1_bad} of {_flow1_ok + _flow1_bad} transitions, so the "
       f"gate's own zero-violation conjunct turns false")

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

# the block decomposition of the carrier -- WITH ITS SCOPE PRINTED.
# The census above is the depth <= 5 ANCHOR scope.  On THE CARRIER the
# decomposition is a statement about NINE of the 113 classes, and the
# previous delivery printed the anchor census under the heading "the
# block decomposition" of the carrier (operator M4 / instrument D8).
BLOCK = {}
for h in CARRIER:
    BLOCK[h] = PROFILE.get(h)
_carrier_blocks = Counter(v for v in BLOCK.values() if v is not None)


def block_pure(bmap):
    by = defaultdict(set)
    for h in CARRIER:
        if bmap[h] is not None:
            by[A_MENU[h]].add(bmap[h])
    return sum(1 for v in by.values() if len(v) == 1), len(by)


_pure, _nclass = block_pure(BLOCK)
_bm = dict(BLOCK)
_bmh = None
_by_cls = defaultdict(list)
for h in sorted(CARRIER, key=sk):
    if BLOCK[h] is not None:
        _by_cls[A_MENU[h]].append(h)
for _c in sorted(_by_cls, key=sk):
    if len(_by_cls[_c]) >= 2:
        _bmh = _by_cls[_c][0]
        break
if _bmh is not None:
    _bm[_bmh] = ('CORRUPT-BLOCK',)
_pure_mut, _nclass_mut = block_pure(_bm)
gate('G-BLOCK-DECOMPOSITION', 'MUST',
     "Gamma-prep's B2 atoms decompose the carrier: every MENU class "
     'that meets R-SIG meets exactly one holdings-profile block -- a '
     'statement about the NINE carrier classes that meet R-SIG, not '
     'about all 113, and the denominator is printed here',
     _pure == _nclass and _nclass > 0,
     f"CARRIER SCOPE: {sum(_carrier_blocks.values())} carrier R-SIG "
     f"points in blocks {ctr(_carrier_blocks)}, meeting "
     f"{_nclass} of {len(set(A_MENU.values()))} MENU classes, of which "
     f"block-pure {_pure}.  ANCHOR SCOPE (depth <= {CAP_ANCHOR}): "
     f"{len(RSIG)} R-SIG points, {len(RMENU)} menu-exact, profiles "
     f"{ctr(_prof)}",
     falsifiers=['MUT-BLOCK-MERGE'])
mutant('MUT-BLOCK-MERGE', 'G-BLOCK-DECOMPOSITION',
       'one carrier R-SIG point reassigned to a foreign '
       'holdings-profile block',
       _pure == _nclass and _nclass > 0,
       _pure_mut == _nclass_mut and _nclass_mut > 0,
       f"reassigning one point leaves {_nclass_mut - _pure_mut} MENU "
       f"class(es) meeting two blocks against "
       f"{_nclass - _pure} on the true decomposition, so the purity "
       f"gate's own predicate turns false")

# --- R-GM-13: THE MONOTONICITY DENOMINATOR, CARRIED ------------------
# The blocking fact this unit inherits from Gamma-prep is quoted here
# from that unit's ABSTRACT, which drops the scope.  The scope is
# restored and MEASURED: the census window is histories of depth < 5,
# and this unit's own family census reproduces the censused
# transition count independently.
_GP_LEVELS = pv(GPR, 't_per_level')
_MONO_CENSUSED = sum(_GP_LEVELS[1:CAP_ANCHOR + 1])
_MONO_TOTAL = sum(_GP_LEVELS[1:])
_MONO_MINE = CUM[CAP_ANCHOR] - 1
_MONO_FRAC = Fr(_MONO_CENSUSED, _MONO_TOTAL)
_MONO_BP = (_MONO_CENSUSED * 10000) // _MONO_TOTAL


def mono_scope_ok(censused, total, mine, shrinking):
    return (censused == mine and total > censused and shrinking == 0
            and censused == pv(GPR, 'mono_pairs'))


emit(f"  THE INHERITED BLOCKING FACT, WITH ITS DENOMINATOR RESTORED: "
     f"the holdings profile decreases at {pv(GPR, 'mono_shrinking')} "
     f"transitions -- OF {_MONO_CENSUSED} CENSUSED, out of the "
     f"family's {_MONO_TOTAL} transitions, i.e. {_MONO_FRAC} = "
     f"{_MONO_BP // 100}.{_MONO_BP % 100:02d} per cent.  The censused "
     f"window is transitions out of histories of depth < "
     f"{CAP_ANCHOR + 1}, and this unit's own cumulative census "
     f"reproduces the censused count independently at {_MONO_MINE}.")
gate('G-MONOTONICITY-SCOPE', 'MUST',
     "R-GM-13: the monotone-holdings fact inherited from Gamma-prep "
     'carries its MEASURED denominator wherever it is used.  The '
     'census window is transitions out of histories of depth < 5; the '
     'censused count is reproduced independently from this unit\'s own '
     'per-level family census; and the family\'s total transition '
     'count is read by path from Gamma-prep\'s own committed '
     'per-level table.  No unscoped reading of the fact survives here',
     mono_scope_ok(_MONO_CENSUSED, _MONO_TOTAL, _MONO_MINE,
                   pv(GPR, 'mono_shrinking')),
     f"censused {_MONO_CENSUSED} (independently reproduced here at "
     f"{_MONO_MINE}); family total {_MONO_TOTAL}; fraction "
     f"{_MONO_FRAC} = {_MONO_BP // 100}.{_MONO_BP % 100:02d} per cent; "
     f"shrinking transitions {pv(GPR, 'mono_shrinking')}",
     falsifiers=['MUT-MONO-UNSCOPED'])
mutant('MUT-MONO-UNSCOPED', 'G-MONOTONICITY-SCOPE',
       "the unscoped reading the previous delivery inherited from "
       "Gamma-prep's abstract: the censused window taken as the whole "
       'family',
       mono_scope_ok(_MONO_CENSUSED, _MONO_TOTAL, _MONO_MINE,
                     pv(GPR, 'mono_shrinking')),
       mono_scope_ok(_MONO_CENSUSED, _MONO_CENSUSED, _MONO_MINE,
                     pv(GPR, 'mono_shrinking')),
       f"with the total set equal to the censused count the fraction "
       f"reads 1 instead of {_MONO_FRAC}, and the gate's own "
       f"strict-inequality conjunct turns false")

# --- R-GM-12: THE B2-ATOMS IMPORT, SCOPED AT THE IMPORT SITE ---------
IMPORT_SCOPE = dict(
    imported="Gamma-prep's R-SIG CENSUS ONLY: the point counts "
             f"({len(RSIG)} R-SIG, {len(RMENU)} menu-exact) and the "
             f"holdings-profile block partition {ctr(_prof)}, both "
             "reproduced here from the committed layer.",
    not_imported="the unqualified ATOM / minorization claim.  "
                 "Gamma-prep's delta* = 1 result is a statement at ITS "
                 "declared grain and horizon, and this unit runs "
                 "neither of that unit's alternatives.",
    named_exclusions=[
        "the MATCHED horizon convention (Gamma-prep declares it; this "
        "unit declares H4 and does not run MATCHED) -- inventory item "
        "I-HORIZON",
        "the 13-class PRIMARY grain (Gamma-prep declares it; this unit "
        "uses the 113-class control grain because it is D74's carrier) "
        "-- inventory item I-GRAIN",
        "the (A,B) d <= 6 arena, which is Gamma-prep's own delivered "
        "arena and is NOT rebuilt here; depth 7 is what Gamma-prep "
        "declares infeasible",
    ],
    carrier_consequence="delta* is MONOTONE UNDER COARSENING (the "
                        "Gamma-prep panel's two-line lemma: refinement "
                        "can only decrease delta*).  At the "
                        "adjudication's ruled carrier CONG-185, which "
                        "REFINES MENU-113, four of the six delivered "
                        "atom rows therefore have delta* = 0 and the "
                        "atom claim collapses to the (1,1) block.  "
                        "This unit inherits only the (1,1)-block atoms "
                        "as live at the ruled carrier, pending the "
                        "Gamma-prep adjudication.",
)
emit("  THE B2-ATOMS IMPORT, SCOPED AT THE IMPORT SITE (R-GM-12):")
emit(f"    IMPORTED     : {IMPORT_SCOPE['imported']}")
emit(f"    NOT IMPORTED : {IMPORT_SCOPE['not_imported']}")
for _x in IMPORT_SCOPE['named_exclusions']:
    emit(f"    EXCLUDED     : {_x}")
emit(f"    AT THE RULED CARRIER: {IMPORT_SCOPE['carrier_consequence']}")

_SCOPE_TOKENS = ('census', 'scope', 'not run', 'CONG-185', '(1,1)',
                 'block', 'exclu', 'import', 'grain', 'MATCHED',
                 'delta', 'collapse')


def atom_sentences(text):
    out = []
    for chunk in text.replace('\n', ' ').split('. '):
        c = chunk.strip()
        if c and 'atom' in c.lower():
            out.append(c)
    return out


def atoms_scoped(text):
    unscoped = [c for c in atom_sentences(text)
                if not any(t.lower() in c.lower() for t in _SCOPE_TOKENS)]
    return unscoped


_atom_unscoped = atoms_scoped(PAPER_TEXT)
_ATOM_SYNTH = ('The B2 atoms are inherited whole and hold of the '
               'process.')
_atom_unscoped_mut = atoms_scoped(PAPER_TEXT + "\n" + _ATOM_SYNTH)


def import_ok(rec, unscoped):
    return (len(rec['named_exclusions']) == 3
            and bool(rec['imported']) and bool(rec['not_imported'])
            and bool(rec['carrier_consequence'])
            and len(unscoped) == 0)


gate('G-ATOMS-IMPORT-SCOPE', 'MUST',
     "R-GM-12: the Gamma-prep B2-atoms import is SCOPED AT THE IMPORT "
     'SITE.  What is imported is the R-SIG census; what is NOT '
     'imported is the unqualified atom claim; the three exclusions '
     "are named (the MATCHED horizon convention, the 13-class primary "
     'grain, and the d <= 6 arena that is Gamma-prep\'s own and is not '
     'rebuilt here); and the carrier consequence is registered -- '
     'delta* is monotone under coarsening, so at the ruled carrier '
     'CONG-185 four of the six delivered atom rows are delta* = 0 and '
     'the claim collapses to the (1,1) block.  The paper is scanned '
     'and every sentence of it that uses the word "atom" carries a '
     'scope token',
     import_ok(IMPORT_SCOPE, _atom_unscoped),
     f"exclusions named {len(IMPORT_SCOPE['named_exclusions'])}; "
     f"paper sentences mentioning atoms "
     f"{len(atom_sentences(PAPER_TEXT))}, of which unscoped "
     f"{len(_atom_unscoped)} {[c[:60] for c in _atom_unscoped]}",
     falsifiers=['MUT-ATOMS-UNSCOPED'])
mutant('MUT-ATOMS-UNSCOPED', 'G-ATOMS-IMPORT-SCOPE',
       'an unqualified atom sentence appended to the paper text -- the '
       'unscoped import the Gamma-prep panel convicted',
       import_ok(IMPORT_SCOPE, _atom_unscoped),
       import_ok(IMPORT_SCOPE, _atom_unscoped_mut),
       f"the appended sentence raises the unscoped count to "
       f"{len(_atom_unscoped_mut)}, so the gate's own zero-unscoped "
       f"predicate turns false")

# ======================================================================
# P7 -- THE CONSTRUCTION: Gamma(cut' <- cut)
# ======================================================================
sec("P7 -- THE CONSTRUCTION: Gamma(cut' <- cut), exact rational, "
    "column-stochastic")
emit("""  THE READOUT, DECLARED BEFORE IT IS COMPUTED, AND THE FIBER IS
  AT LEAST THREE.  A class-level law needs a lift, because the horizon
  kernel does not descend on the carrier (measured below).
    PRIMARY -- the STEP-NORMALISED law.  At the class level: the
      occupancy w(h) = mu(h) G(h,4-|h|)/G(root,4) of the H4 chain,
      whose one-step conditional is the pinned kernel; Gamma(d'<-d) is
      then the exact conditional, because w(h) k_{4-|h|}(e|h) = w(h+e).
      At the LEG level (a different fiber, and the previous delivery
      folded the two into one item): the step-normalised weight
      q(e|h)/M(h) = k_1(e|h).
    ALSO MEASURED -- RAW-PRODUCT: the unnormalised product of raw
      weights along a leg.  This is what the previous delivery called
      "the process's own law"; M(h) is not constant, so it is not a
      probability.
    ALSO MEASURED -- COUNT: the same construction with the uniform
      measure on the admissible objects in place of w.  IT IS BUILT
      HERE, AT THE CLASS LEVEL, AND IT IS NOT A LAW (see the count
      control below).""")


def gamma_family(V, dom, wt, denom):
    """The exact rational family on quotient V over domain dom under a
    declared weight `wt`.  `denom` selects the normalisation:
      'source-mass' -- divide by the weight of the SOURCE class at the
                       earlier cut (this is the conditional-probability
                       normalisation; with wt = w it is the exact
                       disintegration, with wt = 1 it is the literal
                       'uniform measure in place of w');
      'column-sum'  -- divide by the column's own total (the undeclared
                       second choice the count readout needs before it
                       is a family at all).
    Returns (index per depth, class mass per depth, sparse family)."""
    idx = {}
    for d in range(CAP + 1):
        cl = sorted({V[h] for h in dom if len(h) == d}, key=sk)
        idx[d] = {c: i for i, c in enumerate(cl)}
    mass = {d: defaultdict(Fr) for d in range(CAP + 1)}
    for h in dom:
        mass[len(h)][V[h]] += wt[h]
    GAM = {}
    for d in range(CAP + 1):
        for dd in range(d + 1, CAP + 1):
            j = defaultdict(Fr)
            for h in dom:
                if len(h) != dd:
                    continue
                j[(V[h[:d]], V[h])] += wt[h]
            M = defaultdict(dict)
            tot = defaultdict(Fr)
            for (s, s2), m in j.items():
                tot[s] += m
            for (s, s2), m in j.items():
                den = mass[d][s] if denom == 'source-mass' else tot[s]
                M[s][s2] = m / den
            GAM[(dd, d)] = dict(M)
    return idx, mass, GAM


ONE = {h: Fr(1) for h in CARRIER}
prog("building Gamma on MENU and REC ...")
IDX_M, MASS_M, GAM_M = gamma_family(A_MENU, CARRIER, W, 'source-mass')
IDX_R, MASS_R, GAM_R = gamma_family(A_REC, CARRIER, W, 'source-mass')
prog("building the COUNT-readout control (literal and repaired) ...")
IDX_CM, _, CNTLIT_M = gamma_family(A_MENU, CARRIER, ONE, 'source-mass')
IDX_CR, _, CNTLIT_R = gamma_family(A_REC, CARRIER, ONE, 'source-mass')
_, _, CNTFIX_M = gamma_family(A_MENU, CARRIER, ONE, 'column-sum')
_, _, CNTFIX_R = gamma_family(A_REC, CARRIER, ONE, 'column-sum')

DIMS_M = [len(IDX_M[d]) for d in range(CAP + 1)]
DIMS_R = [len(IDX_R[d]) for d in range(CAP + 1)]
emit(f"  MENU classes per depth cut: {fl(DIMS_M)}   "
     f"(distinct classes over all cuts: {len(set(A_MENU.values()))})")
emit(f"  REC  classes per depth cut: {fl(DIMS_R)}   "
     f"(distinct classes over all cuts: {len(set(A_REC.values()))})")


def colcensus(fams):
    """(columns, columns not summing to 1, negative entries)."""
    n, bad, neg = 0, 0, 0
    for F in fams:
        for (dd, d), M in F.items():
            for s, row in M.items():
                n += 1
                if sum(row.values()) != 1:
                    bad += 1
                for v in row.values():
                    if v < 0:
                        neg += 1
    return n, bad, neg


_cols_tot, _cs_bad, _neg = colcensus([GAM_M, GAM_R])
_mn_cols, _mn_bad, _ = colcensus([CNTLIT_M, CNTLIT_R])
gate('G-COLUMN-STOCHASTIC', 'MUST',
     'every Gamma(cut\'<-cut) on both quotients is exactly '
     'column-stochastic: columns sum to 1, entries >= 0, in exact '
     'rational arithmetic',
     _cs_bad == 0 and _neg == 0,
     f"columns {_cols_tot}; columns not summing to 1: {_cs_bad}; "
     f"negative entries: {_neg}; pairs {len(GAM_M) + len(GAM_R)}",
     falsifiers=['MUT-MISNORMALIZED'])
# THE MIS-NORMALIZED NEGATIVE CONTROL, built as an object: the chain
# weighted by the OFF-BY-ONE horizon (G(h, 3-|h|) where G(h, 4-|h|)
# belongs).  The flow identity fails for it, so the joint no longer
# agrees with the marginal and the columns stop summing to 1.
GRM = G[(ROOT, CAP - 1)]
WBAD = {h: MU[h] * G[(h, max(CAP - len(h) - 1, 0))] / GRM
        for h in CARRIER}
_, _, GAMBAD_M = gamma_family(A_MENU, CARRIER, WBAD, 'source-mass')
_, _, GAMBAD_R = gamma_family(A_REC, CARRIER, WBAD, 'source-mass')
_bad_cols, _bad_bad, _bad_neg = colcensus([GAMBAD_M, GAMBAD_R])
_badk = {}
for h in CARRIER:
    if len(h) < CAP:
        for e, q in CACHE[h]:
            _badk[(h, e)] = (PRICE[(h, e)] * G[(h + (e,), CAP - len(h) - 1)]
                             / G[(h, CAP - len(h) - 1)])
_mn = [sum(_badk[(h, e)] for e, q in CACHE[h]) for h in CARRIER
       if len(h) < CAP]
_mn_broken = sum(1 for s in _mn if s != 1)
mutant('MUT-MISNORMALIZED', 'G-COLUMN-STOCHASTIC',
       'the chain re-weighted by the off-by-one horizon -- the kernel '
       'divided by G(h, r-1) where G(h, r) belongs -- and the family '
       'rebuilt from it',
       _cs_bad == 0 and _neg == 0,
       _bad_bad == 0 and _bad_neg == 0,
       f"the mis-normalized family has {_bad_bad} of {_bad_cols} "
       f"columns failing to sum to 1 (and {_mn_broken} of {len(_mn)} "
       f"mis-normalized kernel columns fail properness), so the "
       f"column-stochastic gate's own predicate turns false on it")

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


def gmulti_rows(V):
    rows = []
    for r in range(0, CAP + 1):
        d = defaultdict(set)
        for h in CARRIER:
            if CAP - len(h) >= r:
                d[V[h]].add(G[(h, r)])
        rows.append((r, sum(1 for v in d.values() if len(v) > 1),
                     len(d)))
    return rows


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
# THE HOLONOMY GATE, RE-POSED AS REPRODUCED-AND-LOCATED
# ======================================================================
sec("TEST 2 -- THE HOLONOMY GATE (pre-registered), RE-POSED AS "
    "REPRODUCED-AND-LOCATED")
emit("""  THE GATE'S FORM, CORRECTED (adjudication R-GM-3).  The pin's
  section 3.2 asked for "agreement OR the measured deviation, exactly";
  its section 4 settlement clause silently hardened that into an
  agreement demand.  That demand is unsatisfiable by ANY
  column-stochastic construction from the pinned law on a carrier where
  the potential fails to descend -- because the deviation is an
  IDENTITY, not a census.  The gate is therefore re-posed with three
  conjuncts, each measured and each killable:
    (i)   the q-connection reproduces D74's committed rung on the
          carrier digit for digit;
    (ii)  the deviation of every derived reading is DERIVED, not
          observed: r_k = r_q * G(h eA eB, r-2)/G(h eB eA, r-2) at every
          closed square, and every non-unit factor is LOCATED in a
          measured descent failure of the carrier;
    (iii) the negative control is flat at all three readings.""")


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

# --- (ii) THE DEVIATION IDENTITY, and the LOCATION of every deviation -
_GMV = {}
for r in range(0, CAP + 1):
    d = defaultdict(set)
    for h in CARRIER:
        if CAP - len(h) >= r:
            d[A_MENU[h]].add(G[(h, r)])
    _GMV[r] = {c for c, v in d.items() if len(v) > 1}

DEVROWS = []
for c in CLOSED:
    h, eA, eB = c[0], c[1], c[2]
    d = len(h)
    r = CAP - d
    hAB, hBA = h + (eA, eB), h + (eB, eA)
    f = G[(hAB, r - 2)] / G[(hBA, r - 2)]
    closes = (A_MENU[hAB] == A_MENU[hBA])
    DEVROWS.append(dict(base_depth=d, factor=f, closes_in_menu=closes,
                        endpoint_class_multivalued=(closes and
                                                    A_MENU[hAB] in
                                                    _GMV[r - 2]),
                        identity=(c[4] == c[3] * f)))
_id_viol = sum(1 for r in DEVROWS if not r['identity'])
_facspec = Counter(r['factor'] for r in DEVROWS)
_dev_depths = Counter(r['base_depth'] for r in DEVROWS if r['factor'] != 1)


def located(rows):
    """Every non-unit deviation factor on a square that CLOSES in the
    carrier lies on a class where the horizon potential is measured
    NOT to descend.  This is the clause that makes the deviation
    derived rather than observed."""
    bad = [r for r in rows if r['closes_in_menu'] and r['factor'] != 1
           and not r['endpoint_class_multivalued']]
    return len(bad) == 0, len(bad)


_loc_ok, _loc_bad = located(DEVROWS)
_menu_closing = [r for r in DEVROWS if r['closes_in_menu']]
_mc_dev = [r for r in _menu_closing if r['factor'] != 1]
_mc_multi_unit = [r for r in _menu_closing if r['factor'] == 1
                  and r['endpoint_class_multivalued']]
emit(f"  THE DEVIATION IDENTITY: r_k = r_q * G(h eA eB, r-2)/"
     f"G(h eB eA, r-2) at {len(DEVROWS) - _id_viol} of {len(DEVROWS)} "
     f"closed squares; correction-factor spectrum {ctr(_facspec)}; "
     f"non-unit factors at base depths {ctr(_dev_depths)}")
emit(f"  THE DEVIATION IS LOCATED: of the {len(_menu_closing)} squares "
     f"that CLOSE in the carrier, {len(_mc_dev)} carry a non-unit "
     f"factor and ALL of them sit on a class where G(.,r-2) is "
     f"measured multi-valued; {len(_mc_multi_unit)} squares sit on a "
     f"multi-valued class with factor 1 (the converse fails, and is "
     f"reported rather than claimed)")

# the two falsifiers of (ii), each a constructed mutated object.
_G_MUT = dict(G)
_pick = None
for _i, c in enumerate(CLOSED):
    if DEVROWS[_i]['factor'] != 1:
        _pick = (_i, c)
        break
if _pick is not None:
    _i, c = _pick
    _h, _eA, _eB = c[0], c[1], c[2]
    _r = CAP - len(_h)
    _G_MUT[(_h + (_eA, _eB), _r - 2)] = (G[(_h + (_eA, _eB), _r - 2)]
                                         * Fr(7, 5))
_id_viol_mut = 0
for _i, c in enumerate(CLOSED):
    _h, _eA, _eB = c[0], c[1], c[2]
    _r = CAP - len(_h)
    _f = (_G_MUT[(_h + (_eA, _eB), _r - 2)]
          / _G_MUT[(_h + (_eB, _eA), _r - 2)])
    if c[4] != c[3] * _f:
        _id_viol_mut += 1
gate('T2-DEVIATION-IDENTITY', 'MUST',
     'the deviation of the horizon-normalized connection from D74\'s is '
     'an IDENTITY and is verified as one at every closed square: '
     'r_k = r_q * G(h eA eB, r-2) / G(h eB eA, r-2)',
     _id_viol == 0 and len(DEVROWS) == SQ['closed'],
     f"{len(DEVROWS) - _id_viol} of {len(DEVROWS)} closed squares "
     f"satisfy the identity; violations {_id_viol}; factor spectrum "
     f"{ctr(_facspec)}",
     falsifiers=['MUT-IDENTITY-BREAK'])
mutant('MUT-IDENTITY-BREAK', 'T2-DEVIATION-IDENTITY',
       'one horizon potential perturbed by 7/5 at a deviating square, '
       'the identity re-evaluated against the UNPERTURBED measured '
       'connection',
       _id_viol == 0, _id_viol_mut == 0,
       f"the perturbed potential breaks the identity at {_id_viol_mut} "
       f"squares, so the gate's own predicate turns false")

_DEV_MUT = [dict(r) for r in DEVROWS]
_synth = None
for _r in _DEV_MUT:
    if _r['closes_in_menu'] and _r['factor'] == 1 \
            and not _r['endpoint_class_multivalued']:
        _r['factor'] = Fr(3, 2)
        _synth = True
        break
_loc_ok_mut, _loc_bad_mut = located(_DEV_MUT)
gate('T2-DEVIATION-LOCATED', 'MUST',
     'EVERY non-unit deviation on a square that closes in the carrier '
     'is located in a MEASURED descent failure: its endpoint class is '
     'one on which the horizon potential takes more than one value.  '
     'A deviation on a descending class would be unexplained and this '
     'gate would fail',
     _loc_ok and len(_mc_dev) > 0,
     f"{len(_mc_dev)} non-unit deviations among {len(_menu_closing)} "
     f"carrier-closing squares, unlocated {_loc_bad}; the "
     f"multi-valued depth-2 classes number "
     f"{len(_GMV[CAP - 2])} of {DIMS_M[2]}",
     falsifiers=['MUT-DEVIATION-UNLOCATED'])
mutant('MUT-DEVIATION-UNLOCATED', 'T2-DEVIATION-LOCATED',
       'A SYNTHETIC DEVIATION the gate must catch: a non-unit factor '
       'planted on a carrier-closing square whose endpoint class the '
       'measurement says DOES descend',
       _loc_ok and len(_mc_dev) > 0,
       _loc_ok_mut and len(_mc_dev) > 0,
       f"the planted deviation is unlocated ({_loc_bad_mut} unlocated "
       f"squares against {_loc_bad} on the true object), so the "
       f"location gate's own predicate turns false -- the gate can "
       f"fail, and this is what makes the holonomy head falsifiable")

HOL = {}


def gamma_entry(GAM, d, dd, s, s2):
    return GAM[(dd, d)].get(s, {}).get(s2, Fr(0))


def gamma_reading(V, GAM):
    """The constructed family's OWN holonomy, from its entries."""
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
    ps, rk_ = group_of(list(vals.elements()))
    return dict(nonclosing=nonclose, undefined=undef,
                spectrum={str(k): v for k, v in sorted(vals.items())},
                nonunit=sum(v for k, v in vals.items() if k != 1),
                primes=ps, rank=rk_)


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
        emit(f"  {qname} / {rname}: squares closing "
             f"{sum(1 for u, v, x in ex if u == v)}; "
             f"non-unit self-loops {sum(loops.values())} "
             f"{ctr(loops)}; cycle rank {rank}; obstruction {ob}; "
             f"group primes {ps} rank {rk}")
    HOL[qname]['Gamma (the constructed family)'] = gamma_reading(V, GAM)
    _g = HOL[qname]['Gamma (the constructed family)']
    emit(f"  {qname} / Gamma (the constructed family, AT THE OCCUPANCY "
         f"CONSTRUCTION): squares not closing {_g['nonclosing']}; "
         f"undefined {_g['undefined']}; non-unit {_g['nonunit']} of "
         f"{sum(_g['spectrum'].values())}; distinct values "
         f"{len(_g['spectrum'])}; group primes {_g['primes']} rank "
         f"{_g['rank']}")

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


def d74_rung(rd):
    return (rd['primes'] == [2, 3] and rd['rank'] == 2
            and rd['closes'] == 1402 and rd['obstruction'] == 44
            and rd['selfloops'] == 44 and rd['cycle_rank'] == 134)


_q23_mut = dict(_q23)
_q23_mut['primes'], _q23_mut['rank'] = group_of([Fr(5, 4)]
                                                + list(SPEC_Q.elements()))
gate('T2-D74-ANCHOR', 'MUST',
     "the carrier reproduces D74's committed rung DIGIT FOR DIGIT: the "
     'q-connection generates the free abelian rank-2 group of 3-smooth '
     'positive rationals, primes {2, 3}, with 1402 squares closing, '
     'obstruction 44, 44 non-unit self-loops and cycle rank 134',
     d74_rung(_q23),
     f"primes {_q23['primes']}, rank {_q23['rank']}, closes "
     f"{_q23['closes']}, obstruction {_q23['obstruction']}, self-loops "
     f"{_q23['selfloops']}, cycle rank {_q23['cycle_rank']}",
     falsifiers=['MUT-HOLONOMY-DRIFT'])
mutant('MUT-HOLONOMY-DRIFT', 'T2-D74-ANCHOR',
       'one extra holonomy value (5/4) injected into the q-spectrum and '
       'the group recomputed from the injected spectrum',
       d74_rung(_q23), d74_rung(_q23_mut),
       f"the injected spectrum generates primes {_q23_mut['primes']} "
       f"rank {_q23_mut['rank']}, so the rung gate's own predicate "
       f"turns false")

_k = HOL['MENU']['k (the horizon-normalized connection)']
_gm = HOL['MENU']['Gamma (the constructed family)']
_rq = HOL['REC']["q (D74's connection)"]
_rk = HOL['REC']['k (the horizon-normalized connection)']
_rg = HOL['REC']['Gamma (the constructed family)']


def rec_flat(rqd, rkd, rgd):
    return (rqd['obstruction'] == 0 and rqd['selfloops'] == 0
            and rkd['obstruction'] == 0 and rkd['selfloops'] == 0
            and rgd['nonunit'] == 0)


# the mutated record quotient: one history moved out of its class.
_rec_mut = dict(A_REC)
_d0 = sorted(DEF88, key=lambda c: (sk(c[0]), sk(c[1]), sk(c[2])))[0]
_rec_mut[_d0[0] + (_d0[2], _d0[1])] = _rec_mut[_d0[0] + (_d0[1], _d0[2])]
_exm = [(_rec_mut[c[0] + (c[2], c[1])], _rec_mut[c[0] + (c[1], c[2])],
         c[3]) for c in CLOSED]
_nm2, _rkm, _obm, _holm = holonomy_of([e for e in _exm if e[0] != e[1]])
_slm = Counter(x for u, v, x in _exm if u == v and x != 1)
_rq_mut = dict(_rq, obstruction=_obm, selfloops=sum(_slm.values()))
gate('T2-REC-FLAT', 'MUST',
     'THE NEGATIVE CONTROL: on the REC quotient the connection is flat '
     'at ALL THREE READINGS -- zero obstruction, zero non-unit '
     'self-loops, and the constructed family assigns holonomy exactly '
     '1 to every square that closes.  AT THE DECLARED READOUT: this is '
     'the occupancy construction, and the count control below shows '
     'the control does NOT survive the other one',
     rec_flat(_rq, _rk, _rg),
     f"REC q: obstruction {_rq['obstruction']} self-loops "
     f"{_rq['selfloops']}; REC k: obstruction {_rk['obstruction']} "
     f"self-loops {_rk['selfloops']}; REC Gamma: non-unit "
     f"{_rg['nonunit']}, spectrum {_rg['spectrum']}",
     falsifiers=['MUT-REC-CORRUPT'])
mutant('MUT-REC-CORRUPT', 'T2-REC-FLAT',
       'one history moved out of its record class, the record reading '
       'rebuilt on the corrupted quotient',
       rec_flat(_rq, _rk, _rg), rec_flat(_rq_mut, _rk, _rg),
       f"merging the two endpoints of one defective square (ratio "
       f"{_d0[3]}) turns it into a self-loop: the corrupted record "
       f"quotient has {len(set(_rec_mut.values()))} classes (2,477 "
       f"required), obstruction {_obm}, non-unit self-loops "
       f"{sum(_slm.values())}, so the flatness gate's own predicate "
       f"turns false")

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
emit(f"  CONTAINMENT, measured: the horizon-normalized connection's "
     f"group contains D74's <2,3> = {_k_contains}; the constructed "
     f"family's group contains it = {_g_contains}.  The deviation is "
     f"therefore an ENLARGEMENT where containment holds, not a "
     f"replacement.")


def t2_ok(rung, idviol, locok, recflat):
    return bool(rung) and idviol == 0 and bool(locok) and bool(recflat)


T2_OK = t2_ok(d74_rung(_q23), _id_viol, _loc_ok,
              rec_flat(_rq, _rk, _rg))
T2_VERDICT = ('REPRODUCED-AND-LOCATED' if T2_OK else
              'NOT-LOCATED-AT-' + ('RUNG' if not d74_rung(_q23)
                                   else ('IDENTITY' if _id_viol else
                                         ('LOCATION' if not _loc_ok
                                          else 'REC-CONTROL'))))
gate('T2-HOLONOMY', 'MUST',
     "THE HOLONOMY GATE, RE-POSED: the q-connection reproduces D74's "
     'rung digit for digit; every derived reading\'s deviation is '
     'DERIVED by the exact identity and LOCATED in a measured descent '
     'failure; and the negative control is flat at all three readings.  '
     'Each conjunct is separately measured and separately killable, and '
     'a synthetic deviation on a descending class fails this gate',
     T2_OK,
     f"verdict {T2_VERDICT}; D74 rung reproduced {d74_rung(_q23)}; "
     f"deviation identity violations {_id_viol} of {len(DEVROWS)}; "
     f"unlocated deviations {_loc_bad}; REC flat at all three readings "
     f"{rec_flat(_rq, _rk, _rg)}; k-connection primes {_k['primes']} "
     f"rank {_k['rank']} ON A NON-DESCENDING CARRIER (new self-loop "
     f"values "
     f"{sorted(set(_k['selfloop_values']) - set(_q23['selfloop_values']))}, "
     f"contains <2,3> = {_k_contains}); Gamma-family primes "
     f"{_gm['primes']} rank {_gm['rank']} AT THE OCCUPANCY "
     f"CONSTRUCTION, contains <2,3> = {_g_contains}, non-unit "
     f"{_gm['nonunit']} of {sum(_gm['spectrum'].values())} closing "
     f"squares",
     falsifiers=['MUT-HOLONOMY-VERDICT'])
mutant('MUT-HOLONOMY-VERDICT', 'T2-HOLONOMY',
       'THE SYNTHETIC DEVIATION, carried into the head: the planted '
       'non-unit factor on a descending class, evaluated by the '
       "holonomy head's own four-conjunct predicate",
       T2_OK,
       t2_ok(d74_rung(_q23), _id_viol, _loc_ok_mut,
             rec_flat(_rq, _rk, _rg)),
       f"with the synthetic deviation planted the location conjunct "
       f"reads {_loc_ok_mut} and the head's own predicate turns false, "
       f"so REPRODUCED-AND-LOCATED is a verdict that can fail")

# ======================================================================
# THE COUNT-READOUT CONTROL -- the third convergent reason that the
# pre-registered targets are not values of any law (adjudication R-GM-1)
# ======================================================================
sec("THE COUNT-READOUT CONTROL: what adopting the target-selecting "
    "readout costs")
emit("""  The pre-registered values are hit at the COUNT readout and at no
  other.  The previous delivery declared COUNT an alternative and never
  BUILT it at the class level.  It is built here, twice, and the
  measurement is the third of the adjudication's three convergent
  reasons.
    LITERAL COUNT -- "the same construction with the uniform measure on
      the admissible objects in place of w", word for word.  It is not
      a law: its columns sum to the branching factors.
    REPAIRED COUNT -- the same object after an UNDECLARED second
      choice: renormalise each column by its own total.  Now it is
      column-stochastic -- and it destroys the pin's own mandatory
      negative control.""")


def ck_sparse(GAM):
    rows = []
    for d in range(CAP + 1):
        for md in range(d + 1, CAP + 1):
            for dd in range(md + 1, CAP + 1):
                A, B, C = GAM[(dd, md)], GAM[(md, d)], GAM[(dd, d)]
                bad = 0
                cells = 0
                for s in sorted(set(C) | set(B), key=sk):
                    tgt = defaultdict(Fr)
                    for s1, v in B.get(s, {}).items():
                        for s2, u in A.get(s1, {}).items():
                            tgt[s2] += v * u
                    allk = set(tgt) | set(C.get(s, {}))
                    cells += len(allk)
                    for s2 in allk:
                        if tgt.get(s2, Fr(0)) != C.get(s, {}).get(s2,
                                                                  Fr(0)):
                            bad += 1
                rows.append(dict(cut=d, mid=md, cut2=dd, cells=cells,
                                 differing=bad, interpolates=bad == 0))
    return rows


_lit_cols, _lit_bad, _ = colcensus([CNTLIT_M, CNTLIT_R])
_fix_cols, _fix_bad, _ = colcensus([CNTFIX_M, CNTFIX_R])
_lit_sums = Counter()
for F in (CNTLIT_M, CNTLIT_R):
    for (dd, d), M in F.items():
        for s, row in M.items():
            _lit_sums[sum(row.values())] += 1
prog("count-readout control: holonomy and CK ...")
CNT_HOL_M = gamma_reading(A_MENU, CNTFIX_M)
CNT_HOL_R = gamma_reading(A_REC, CNTFIX_R)
CNT_CK_M = ck_sparse(CNTFIX_M)
CNT_CK_R = ck_sparse(CNTFIX_R)
OCC_CK_R = ck_sparse(GAM_R)
_cnt_ck_m_fail = sum(1 for r in CNT_CK_M if not r['interpolates'])
_cnt_ck_r_fail = sum(1 for r in CNT_CK_R if not r['interpolates'])
_occ_ck_r_fail = sum(1 for r in OCC_CK_R if not r['interpolates'])
emit(f"  LITERAL COUNT: {_lit_cols} columns over both quotients, "
     f"{_lit_cols - _lit_bad} of them sum to 1.  The column sums that "
     f"occur are the branching factors "
     f"{sorted(str(x) for x in _lit_sums)}.")
emit(f"  REPAIRED COUNT: {_fix_cols - _fix_bad} of {_fix_cols} columns "
     f"sum to 1 -- column-stochastic, after a choice nobody declared.")
emit(f"  THE COST, on the pin's OWN mandatory negative control (REC): "
     f"the repaired count family has holonomy non-unit at "
     f"{CNT_HOL_R['nonunit']} of "
     f"{sum(CNT_HOL_R['spectrum'].values())} closing squares, group "
     f"primes {CNT_HOL_R['primes']} rank {CNT_HOL_R['rank']} -- the "
     f"record quotient D74 proved FLAT acquires curvature; and it "
     f"fails Chapman-Kolmogorov at {_cnt_ck_r_fail} of "
     f"{len(CNT_CK_R)} triples where the occupancy construction fails "
     f"at {_occ_ck_r_fail}.  On MENU the repaired count family carries "
     f"primes {CNT_HOL_M['primes']} rank {CNT_HOL_M['rank']} against "
     f"the occupancy construction's {_gm['primes']} rank {_gm['rank']}.")


def count_control(lit_bad, lit_cols, rec_nonunit, rec_ck_fail):
    """The measured cost of the target-selecting readout: it is not a
    law as described, and after the undeclared repair it destroys the
    negative control on BOTH statistics."""
    return (lit_bad == lit_cols and rec_nonunit > 0 and rec_ck_fail > 0)


_cc_ok = count_control(_lit_bad, _lit_cols, CNT_HOL_R['nonunit'],
                       _cnt_ck_r_fail)
_cc_mut = count_control(_lit_bad, _lit_cols, _rg['nonunit'],
                        _occ_ck_r_fail)
gate('T1-COUNT-CONTROL', 'MUST',
     'THE THIRD CONVERGENT REASON, measured: the readout at which the '
     'pre-registered values are hit is (a) not a law as the '
     'construction describes it -- every one of its columns fails to '
     'sum to 1 -- and (b) after the undeclared renormalisation it '
     "breaks the pin's OWN mandatory negative control, giving the "
     'record quotient a non-trivial holonomy and destroying its exact '
     'lumpability',
     _cc_ok,
     f"literal count: {_lit_bad} of {_lit_cols} columns fail to sum to "
     f"1; repaired count on REC: holonomy non-unit "
     f"{CNT_HOL_R['nonunit']}, primes {CNT_HOL_R['primes']} rank "
     f"{CNT_HOL_R['rank']}, CK failures {_cnt_ck_r_fail} of "
     f"{len(CNT_CK_R)}; the occupancy construction on REC: holonomy "
     f"non-unit {_rg['nonunit']}, CK failures {_occ_ck_r_fail}",
     falsifiers=['MUT-COUNT-CONTROL-CLEAN'])
mutant('MUT-COUNT-CONTROL-CLEAN', 'T1-COUNT-CONTROL',
       'the count control scored with the OCCUPANCY construction\'s own '
       'record-quotient statistics -- i.e. the claim that adopting the '
       'count readout costs nothing',
       _cc_ok, _cc_mut,
       f"the occupancy construction leaves REC flat (non-unit "
       f"{_rg['nonunit']}) and exactly lumpable (CK failures "
       f"{_occ_ck_r_fail}), so scoring the control with those numbers "
       f"turns the gate's own predicate false")

# ======================================================================
# TEST 1 -- THE EXTERNAL-CENSUS CONTROL, AND THE LAW VALUE AT THE
# DECLARED PRIMARY READOUT  (adjudication R-GM-2)
# ======================================================================
sec("TEST 1 -- THE EXTERNAL-CENSUS CONTROL AND THE LAW VALUE (the "
    "pre-registered values, DEMOTED to a declared census shadow)")
emit("""  WHAT THIS TEST IS, CORRECTED.  The pin's test 1 asked the
  constructed family to reproduce two positional laws.  The
  adjudication demotes those two rational triples to a DECLARED CENSUS
  SHADOW: they are leaf-count statistics of the external transport
  census, defined by the counting measure in their own frozen source,
  and they are an EXTERNAL CONTROL of this unit, never a target of it.
  What is measured against them is the LAW VALUE: the positional law at
  the declared PRIMARY readout, which is the step-normalised weight
  q(e|h)/M(h) -- proved above to be exactly the pinned kernel k_1.
  The measurement below is deliberately built from the transport
  grammar alone; that it touches no object of the constructed family is
  not asserted but MEASURED, by a token scan of this file's own source
  over the region between the two markers.""")
# <<<T1-CENSUS-REGION-BEGIN>>>


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
_pat1_mut = Counter(dict(_pat1))
_pat1_mut[('p', 'n', 'r')] = 1


def three_event(pats):
    return set(pats) == {('p', 'p', 'r')}


gate('T1-3EVENT-LAW', 'MUST',
     "U1b's committed law: a renewal three events after the boundary "
     'forces the pattern (p, p, r) and nothing else',
     three_event(_pat1),
     f"patterns {ctr(_pat1)}",
     falsifiers=['MUT-3EVENT-DRIFT'])
mutant('MUT-3EVENT-DRIFT', 'T1-3EVENT-LAW',
       'a second three-event pattern injected into the base census',
       three_event(_pat1), three_event(_pat1_mut),
       f"the injected census reads {ctr(_pat1_mut)}, so the gate's own "
       f"set-equality predicate turns false")

_delopt = Counter(sum(1 for e, q in CACHE[h] if e[0] == 'd')
                  for h in R1BASES)
_idlopt = Counter(sum(1 for e, q in CACHE[h] if e[0] == 'n')
                  for h in R1BASES)
emit(f"  at the renewal-1 bases: delivery options {ctr(_delopt)}, "
     f"idle options {ctr(_idlopt)}")


def leg_scan(bases, pruned):
    """Enumerate 4-event legs (three interior events then an R4) from
    each base, carrying BOTH leg weights: the raw product of prices, and
    the step-normalised product q/M -- the pinned kernel k_1 chain.
    pruned=False is the UNPRUNED scan: every candidate is generated and
    only then filtered."""
    nodes = 0
    legs = []
    for b in bases:
        stack = [(b, (), Fr(1), Fr(1))]
        while stack:
            h, tail, ww, wn = stack.pop()
            k = len(tail)
            nfill = sum(1 for i in range(k) if tail[i][0] != 'p')
            cs = candidates_for(list(h), AB)
            mm = sum(Fr(q) for e, q in cs)
            for e, q in cs:
                nodes += 1
                if is_R4(e):
                    if k == 3:
                        legs.append((b, tail + (e,), ww * Fr(q),
                                     wn * Fr(q) / mm))
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
                stack.append((h + (e,), tail + (e,), ww * Fr(q),
                              wn * Fr(q) / mm))
    return nodes, legs


def positional(legs, sel=None):
    """The three measured readouts of the interior filler's position:
    COUNT (uniform on legs), RAW-PRODUCT (the unnormalised price
    product), and the declared PRIMARY, STEP-NORMALISED law."""
    cnt = Counter()
    raw = defaultdict(Fr)
    nrm = defaultdict(Fr)
    for b, t4, ww, wn in legs:
        f = [i for i in range(3) if t4[i][0] != 'p']
        if len(f) != 1:
            return None, None, None
        if sel is not None and not sel(t4[f[0]][0]):
            continue
        cnt[f[0]] += 1
        raw[f[0]] += ww
        nrm[f[0]] += wn
    tc = sum(cnt.values())
    tw = sum(raw.values())
    tn = sum(nrm.values())
    if tc == 0:
        return None, None, None
    return ([Fr(cnt[i], tc) for i in range(3)],
            [raw[i] / tw for i in range(3)],
            [nrm[i] / tn for i in range(3)])


prog("leg 1: UNPRUNED 4-event scan from the 16 renewal-1 bases ...")
N1, LEGS1 = leg_scan(R1BASES, False)
PAT1 = Counter(tuple(e[0] for e in t4) for b, t4, ww, wn in LEGS1)
CNT1, RAW1, LAW1 = positional(LEGS1)
prog(f"leg 1 done: {N1} raw continuations, {len(LEGS1)} legs")
emit(f"  LEG 1 (renewal 1 -> renewal 2, four events): UNPRUNED scan, "
     f"{N1} raw continuations generated, {len(LEGS1)} legs kept.")
emit(f"    leg patterns: {ctr(PAT1)}")
emit(f"    PRIMARY, step-normalised q/M : {frl(LAW1)}")
emit(f"    RAW-PRODUCT                  : {frl(RAW1)}")
emit(f"    COUNT (the census shadow's own measure): {frl(CNT1)}")
anchor('A-U1B-LEG1', 3584, len(LEGS1),
       "U1b's committed E2 leg-1 leaf count (3,584 renewal-2 leaves)")

# THE F8 MECHANISM, derived rather than imported.
_slotkinds = defaultdict(Counter)
for b, t4, ww, wn in LEGS1:
    for i in range(3):
        if t4[i][0] != 'p':
            _slotkinds[i][t4[i][0]] += 1
emit(f"    F8 slot x kind census: "
     + "; ".join(f"slot {i + 1}: {ctr(_slotkinds[i])}" for i in range(3)))


def f8_ok(sl):
    return (sl[1]['d'] == 0 and sl[1]['n'] > 0
            and sl[0]['d'] > 0 and sl[2]['d'] > 0)


_sl_mut = {i: Counter(dict(_slotkinds[i])) for i in range(3)}
_sl_mut[1]['d'] = 1
gate('T1-F8', 'MUST',
     'F8, MEASURED HERE: the middle interior slot admits NO delivery -- '
     'the pattern (p, d, p, r) does not occur, while (p, n, p, r) does. '
     'This fact is READOUT-INVARIANT: it is a statement about which '
     'legs exist, not about how they are weighted',
     f8_ok(_slotkinds),
     f"deliveries by slot "
     f"{[_slotkinds[i]['d'] for i in range(3)]}; idles by slot "
     f"{[_slotkinds[i]['n'] for i in range(3)]}",
     falsifiers=['MUT-LEG-PATTERN'])
mutant('MUT-LEG-PATTERN', 'T1-F8',
       'the forbidden pattern (p, d, p, r) injected into the leg '
       'slot-kind census',
       f8_ok(_slotkinds), f8_ok(_sl_mut),
       f"the injected census puts {_sl_mut[1]['d']} delivery in slot 2, "
       f"so the gate's own predicate turns false")

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


def mech_ok(cd, td, cn, tn):
    return td > 0 and cd == td and cn == 0


gate('T1-F8-MECHANISM', 'MUST',
     "F8's cause, measured: after (p, d, p) the two live proposals are "
     'ORDER-COMPARABLE at every instance (the delivery joins the two '
     "actors' registers), and an R4 needs two INCOMPARABLE live "
     'proposals; after (p, n, p) they are incomparable at every '
     'instance',
     mech_ok(_cmp_after_d, _tot_d, _cmp_after_n, _tot_n),
     f"(p,d,p): comparable {_cmp_after_d} of {_tot_d}; "
     f"(p,n,p): comparable {_cmp_after_n} of {_tot_n}",
     falsifiers=['MUT-F8-MECHANISM'])
mutant('MUT-F8-MECHANISM', 'T1-F8-MECHANISM',
       'the comparability census inverted -- (p,d,p) read as '
       'incomparable and (p,n,p) as comparable',
       mech_ok(_cmp_after_d, _tot_d, _cmp_after_n, _tot_n),
       mech_ok(_tot_d - _cmp_after_d, _tot_d, _tot_n - _cmp_after_n,
               _tot_n),
       f"the inverted census reads (p,d,p) comparable "
       f"{_tot_d - _cmp_after_d} of {_tot_d} and (p,n,p) comparable "
       f"{_tot_n} of {_tot_n}, so the gate's own predicate turns false")

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
_delopt2 = Counter(sum(1 for e, q in candidates_for(list(h), AB)
                       if e[0] == 'd') for h in R2BASES)
_idlopt2 = Counter(sum(1 for e, q in candidates_for(list(h), AB)
                       if e[0] == 'n') for h in R2BASES)
emit(f"  at the renewal-2 bases: delivery options {ctr(_delopt2)}, "
     f"idle options {ctr(_idlopt2)}")

prog("leg 2: pattern-pruned scan from all 256 renewal-2 bases ...")
N2, LEGS2 = leg_scan(R2BASES, True)
PAT2 = Counter(tuple(e[0] for e in t4) for b, t4, ww, wn in LEGS2)
CNT2, RAW2, LAW2 = positional(LEGS2)
prog(f"leg 2 done: {N2} expansions, {len(LEGS2)} legs")

# THE PRUNE GATE: an UNPRUNED scan on a declared subsample must return
# the identical leg set with identical weights.
GATE_BASES = R2BASES[:3]
prog("leg 2: UNPRUNED agreement gate on 3 declared bases ...")
NU, LEGSU = leg_scan(GATE_BASES, False)
_sub = sorted(((sk(b), sk(t4), str(ww), str(wn))
               for b, t4, ww, wn in LEGS2 if b in GATE_BASES))
_uns = sorted(((sk(b), sk(t4), str(ww), str(wn))
               for b, t4, ww, wn in LEGSU))
_lax = sorted(_sub[:-1])
gate('T1-PRUNE-GATE', 'MUST',
     'the leg-2 pattern prune is gated, not assumed: on a declared '
     'subsample of renewal-2 bases the UNPRUNED scan returns exactly '
     'the pruned leg set, leg for leg and weight for weight, at BOTH '
     'weights.  SCOPE, printed: the subsample is 3 of the 256 bases',
     _sub == _uns and len(_uns) > 0,
     f"{len(GATE_BASES)} of {len(R2BASES)} bases ({NU} raw "
     f"continuations unpruned, {len(LEGSU)} legs of the "
     f"{len(LEGS2)} pruned legs); pruned subsample {len(_sub)} legs; "
     f"identical {_sub == _uns}",
     falsifiers=['MUT-PRUNE-LAX'])
mutant('MUT-PRUNE-LAX', 'T1-PRUNE-GATE',
       'one leg dropped from the pruned enumeration of the subsample',
       _sub == _uns and len(_uns) > 0, _lax == _uns and len(_uns) > 0,
       f"dropping one leg leaves {len(_lax)} against the unpruned "
       f"{len(LEGSU)}, so the gate's own set comparison turns false")

emit(f"  LEG 2 (renewal 2 -> renewal 3, four events): pattern-pruned "
     f"scan over all {len(R2BASES)} renewal-2 bases, {N2} expansions, "
     f"{len(LEGS2)} legs.")
emit(f"    leg patterns: {ctr(PAT2)}")
emit(f"    PRIMARY, step-normalised q/M : {frl(LAW2)}")
emit(f"    RAW-PRODUCT                  : {frl(RAW2)}")
emit(f"    COUNT (the census shadow's own measure): {frl(CNT2)}")

# --- THE DECLARED CENSUS SHADOW (an EXTERNAL CONTROL, never a target)
SHADOW1 = [Fr(3, 7), Fr(1, 7), Fr(3, 7)]
SHADOW2 = [Fr(4, 9), Fr(1, 9), Fr(4, 9)]
# THE LAW-VALUE REFERENCE, pre-registered by the adjudication panel's
# own measurement (adjudication section 1: "the third, step-normalised
# law measured: 15/38, 5/19, 13/38").  This unit reproduces it or the
# gate fails.
LAWREF = [Fr(15, 38), Fr(5, 19), Fr(13, 38)]


def shadow_ok(c1, c2):
    return c1 == SHADOW1 and c2 == SHADOW2


gate('T1-CENSUS-SHADOW', 'MUST',
     'THE DECLARED CENSUS SHADOW, reproduced and LABELLED AS A CONTROL: '
     'the two rational triples the R6b-prime register pre-registered '
     'are leaf-count statistics of the external transport census -- its '
     'own words are "C(n-1,2) equiprobable configurations; position '
     'marginal uniform on n-1" -- and they are reproduced here EXACTLY, '
     'at the counting measure that defined them.  Reproducing a leaf '
     'census by re-running the leaf census is an external control of '
     'the enumeration, and this unit enters it as one',
     shadow_ok(CNT1, CNT2),
     f"COUNT at leg 1 {frl(CNT1)} vs the shadow {frl(SHADOW1)}; COUNT "
     f"at leg 2 {frl(CNT2)} vs the shadow {frl(SHADOW2)}; reproduced "
     f"{shadow_ok(CNT1, CNT2)}",
     falsifiers=['MUT-CENSUS-SHADOW-DRIFT'])
mutant('MUT-CENSUS-SHADOW-DRIFT', 'T1-CENSUS-SHADOW',
       'the census shadow drifted by one unit in each denominator',
       shadow_ok(CNT1, CNT2),
       CNT1 == [Fr(3, 8), Fr(1, 8), Fr(3, 8)]
       and CNT2 == [Fr(4, 10), Fr(1, 10), Fr(4, 10)],
       f"the measured count law {frl(CNT1)} / {frl(CNT2)} does not "
       f"equal the drifted shadow (3/8,1/8,3/8) / (4/10,1/10,4/10), so "
       f"the gate's own equality predicate turns false on it")


def law_value_ok(l1, l2):
    return (l1 == LAWREF and l2 == LAWREF and l1 == l2
            and l1 != SHADOW1 and l2 != SHADOW2)


gate('T1-LAW-VALUE', 'MUST',
     'THE LAW VALUE AT THE DECLARED PRIMARY READOUT: at the '
     'step-normalised readout -- the pinned kernel k_1, proved above to '
     'be exactly q/M -- the positional law is LEG-INDEPENDENT and takes '
     'the same value at both legs.  It reproduces the value the '
     'adjudication panel measured independently, and it is NOT either '
     'value of the census shadow',
     law_value_ok(LAW1, LAW2),
     f"step-normalised law {frl(LAW1)} at leg 1 and {frl(LAW2)} at leg "
     f"2; leg-independent {LAW1 == LAW2}; equals the panel's "
     f"independently measured reference {frl(LAWREF)} "
     f"{LAW1 == LAWREF and LAW2 == LAWREF}; equals the census shadow "
     f"{LAW1 == SHADOW1 or LAW2 == SHADOW2}; the law is LEFT-RIGHT "
     f"ASYMMETRIC ({LAW1[0]} vs {LAW1[2]}), which neither the shadow "
     f"nor the raw-product readout is",
     falsifiers=['MUT-LAWVALUE-DRIFT'])
mutant('MUT-LAWVALUE-DRIFT', 'T1-LAW-VALUE',
       'the law value replaced by the census shadow -- the claim that '
       'the pre-registered triples ARE values of the law',
       law_value_ok(LAW1, LAW2), law_value_ok(SHADOW1, SHADOW2),
       f"the shadow is neither leg-independent ({SHADOW1 == SHADOW2}) "
       f"nor equal to the measured law value, so the gate's own "
       f"predicate turns false on it")

# --- THE READOUT FIBER, measured -------------------------------------
_readouts = [('COUNT (uniform on legs)', CNT1, CNT2),
             ('RAW-PRODUCT (the unnormalised price product)', RAW1, RAW2),
             ('STEP-NORMALISED q/M = k_1 (PRIMARY)', LAW1, LAW2)]
_distinct = len({tuple(str(x) for x in r[1]) for r in _readouts})
# the fourth reading: the H4 chain Gamma itself is built from.  A leg
# ends at depth 7 and depth 10; a horizon-matched chain over it needs
# potentials at depth 11, and the declared family stops at depth 5.
_h4_needed = 3 + 4 + 4
_h4_available = CAP_ANCHOR


def fiber_ok(distinct, needed, available):
    return distinct >= 3 and needed > available


gate('T1-READOUT-FIBER', 'MUST',
     'THE READOUT FIBER IS AT LEAST THREE, measured: three motivated '
     'readings of the same leg ensembles give three DIFFERENT '
     'positional laws, and a fourth -- the H4 chain the constructed '
     'family is built from -- is EXCLUDED-BY-CAP on the legs because a '
     'horizon-matched chain over a leg needs potentials deeper than the '
     'declared family.  The previous delivery declared the fiber to be '
     'two and folded two different fibers (carrier-level and leg-level) '
     'into one inventory item',
     fiber_ok(_distinct, _h4_needed, _h4_available),
     "; ".join(f"{n}: {frl(a)} / {frl(b)}" for n, a, b in _readouts)
     + f"; distinct laws at leg 1: {_distinct}; the H4 reading needs "
     f"depth {_h4_needed} against the declared family's "
     f"{_h4_available} -- EXCLUDED-BY-CAP",
     falsifiers=['MUT-READOUT-FIBER-COLLAPSE'])
mutant('MUT-READOUT-FIBER-COLLAPSE', 'T1-READOUT-FIBER',
       'the fiber declared to be two, as the previous delivery declared '
       'it -- the step-normalised reading dropped',
       fiber_ok(_distinct, _h4_needed, _h4_available),
       fiber_ok(len({tuple(str(x) for x in r[1])
                     for r in _readouts[:2]}), _h4_needed,
                _h4_available),
       f"dropping the step-normalised reading leaves "
       f"{len({tuple(str(x) for x in r[1]) for r in _readouts[:2]})} "
       f"distinct laws, short of three, so the gate's own predicate "
       f"turns false")

# --- the multiplicity mechanism, and the quarter law ------------------
_mult1 = Fr(sum(_slotkinds[i]['d'] for i in (0, 2)),
            sum(_slotkinds[i]['n'] for i in (0, 2)))
_sk2 = defaultdict(Counter)
for b, t4, ww, wn in LEGS2:
    for i in range(3):
        if t4[i][0] != 'p':
            _sk2[i][t4[i][0]] += 1
_mult2 = Fr(sum(_sk2[i]['d'] for i in (0, 2)),
            sum(_sk2[i]['n'] for i in (0, 2)))


def mult_ok(m1, m2, s1, s2):
    return (m1 == 2 and m2 == 3
            and Fr(m1 + 1, 2 * m1 + 3) == s1[0]
            and Fr(m2 + 1, 2 * m2 + 3) == s2[0])


gate('T1-MULTIPLICITY', 'MUST',
     'the mechanism the CENSUS SHADOW encodes, measured: the delivery '
     'multiplicity (deliveries per idle in a filler slot) moves 2 -> 3 '
     'between leg 1 and leg 2, and (m+1)/(2m+3) is 3/7 at m = 2 and '
     '4/9 at m = 3 -- so the shadow is a function of a COUNT, which is '
     'exactly why only a counting readout can see it',
     mult_ok(_mult1, _mult2, SHADOW1, SHADOW2),
     f"multiplicity leg 1 = {_mult1}, leg 2 = {_mult2}; "
     f"(m+1)/(2m+3) = {Fr(_mult1 + 1, 2 * _mult1 + 3)} and "
     f"{Fr(_mult2 + 1, 2 * _mult2 + 3)}",
     falsifiers=['MUT-MULTIPLICITY-DRIFT'])
mutant('MUT-MULTIPLICITY-DRIFT', 'T1-MULTIPLICITY',
       'the multiplicity law evaluated against the drifted shadow '
       '(3/8,1/8,3/8) and (4/10,1/10,4/10)',
       mult_ok(_mult1, _mult2, SHADOW1, SHADOW2),
       mult_ok(_mult1, _mult2, [Fr(3, 8), Fr(1, 8), Fr(3, 8)],
               [Fr(4, 10), Fr(1, 10), Fr(4, 10)]),
       f"(m+1)/(2m+3) at the measured multiplicities is "
       f"{Fr(_mult1 + 1, 2 * _mult1 + 3)} and "
       f"{Fr(_mult2 + 1, 2 * _mult2 + 3)}, which the drifted shadow "
       f"does not match, so the gate's own predicate turns false")


def sector_mass(bases, kind):
    vals = set()
    for h in bases:
        vals.add(sum(Fr(q) for e, q in candidates_for(list(h), AB)
                     if e[0] == kind))
    return sorted(vals)


_dm1, _nm1 = sector_mass(R1BASES, 'd'), sector_mass(R1BASES, 'n')
_dm2, _nm2 = sector_mass(R2BASES, 'd'), sector_mass(R2BASES, 'n')
emit(f"  THE QUARTER LAW MAKES THE MASS READOUTS MULTIPLICITY-BLIND, "
     f"measured: the delivery sector's TOTAL mass at a renewal base is "
     f"{[str(x) for x in _dm1]} at renewal 1 and "
     f"{[str(x) for x in _dm2]} at renewal 2, and the idle sector's is "
     f"{[str(x) for x in _nm1]} and {[str(x) for x in _nm2]} -- "
     f"unchanged -- while the delivery COUNT moves "
     f"{sorted(_delopt)} -> {sorted(_delopt2)}.  The budget is 1/4 per "
     f"actor divided by |hold(a)|, so adding a version splits the same "
     f"mass into more entries.  The counting readout sees the split; "
     f"the two mass readouts cannot.")


def blind_ok(dm1, dm2, nm1, nm2, do1, do2, r1, r2, c1, c2):
    return (dm1 == dm2 and nm1 == nm2 and sorted(do1) != sorted(do2)
            and r1 == r2 and c1 != c2)


gate('T1-QUARTER-BLINDNESS', 'MUST',
     "the exact cause of the readout split, measured on both legs: the "
     "delivery and idle SECTOR MASSES are identical at renewal 1 and "
     'renewal 2 while the delivery COUNT moves, so both mass readouts '
     'are multiplicity-blind by the quarter law and return the same '
     'positional law at both legs, whereas the counting readout moves '
     'with the multiplicity',
     blind_ok(_dm1, _dm2, _nm1, _nm2, _delopt, _delopt2, RAW1, RAW2,
              CNT1, CNT2),
     f"delivery sector mass {[str(x) for x in _dm1]} = "
     f"{[str(x) for x in _dm2]}; idle sector mass "
     f"{[str(x) for x in _nm1]} = {[str(x) for x in _nm2]}; delivery "
     f"count {sorted(_delopt)} -> {sorted(_delopt2)}; raw-product law "
     f"leg 1 = leg 2 is {RAW1 == RAW2}; step-normalised law leg 1 = "
     f"leg 2 is {LAW1 == LAW2}; count law leg 1 = leg 2 is "
     f"{CNT1 == CNT2}",
     falsifiers=['MUT-BLINDNESS-FLIP'])
mutant('MUT-BLINDNESS-FLIP', 'T1-QUARTER-BLINDNESS',
       'the two readouts exchanged in the blindness claim: the counting '
       'law asserted blind and the mass law asserted to move',
       blind_ok(_dm1, _dm2, _nm1, _nm2, _delopt, _delopt2, RAW1, RAW2,
                CNT1, CNT2),
       blind_ok(_dm1, _dm2, _nm1, _nm2, _delopt, _delopt2, CNT1, CNT2,
                RAW1, RAW2),
       f"with the readouts exchanged the gate asks the count law to be "
       f"leg-independent ({CNT1 == CNT2}) and the mass law to move "
       f"({RAW1 != RAW2}), so its own predicate turns false")

# --- THE READOUT-INVARIANT RESIDUE ------------------------------------
_res = {}
for nm, legs in (('leg1', LEGS1), ('leg2', LEGS2)):
    for kind, sel in (('idle-only', lambda k: k == 'n'),
                      ('delivery-only', lambda k: k == 'd')):
        _res[(nm, kind)] = positional(legs, sel)
_del_inv = all(_res[(nm, 'delivery-only')][j]
               == [Fr(1, 2), Fr(0), Fr(1, 2)]
               for nm in ('leg1', 'leg2') for j in range(3))
_idle_inv_masslike = all(_res[(nm, 'idle-only')][j]
                         == [Fr(1, 3), Fr(1, 3), Fr(1, 3)]
                         for nm in ('leg1', 'leg2') for j in (0, 1))
_idle_step = _res[('leg1', 'idle-only')][2]
for nm, kind in sorted(_res):
    a, b, c = _res[(nm, kind)]
    emit(f"  RESIDUE {nm} {kind:14s}: count {frl(a)}  raw {frl(b)}  "
         f"step-normalised {frl(c)}")


def residue_ok(dinv, iinv, istep):
    return dinv and iinv and istep != [Fr(1, 3), Fr(1, 3), Fr(1, 3)]


gate('T1-RESIDUE', 'MUST',
     'THE READOUT-INVARIANT RESIDUE, measured and reported with its '
     'exact scope: the DELIVERY-ONLY conditional is (1/2, 0, 1/2) at '
     'both legs and at ALL THREE readouts -- it is the F8 exclusion '
     'itself, and it is readout-free.  The IDLE-ONLY conditional is '
     '(1/3, 1/3, 1/3) at the two count-like readouts and is NOT '
     'invariant at the step-normalised one.  The residue is therefore '
     'partial, and the partiality is printed rather than rounded away',
     residue_ok(_del_inv, _idle_inv_masslike, _idle_step),
     f"delivery-only invariant across all three readouts and both "
     f"legs: {_del_inv}; idle-only invariant across count and "
     f"raw-product: {_idle_inv_masslike}; idle-only at the "
     f"step-normalised readout: {frl(_idle_step)} -- NOT (1/3,1/3,1/3)",
     falsifiers=['MUT-RESIDUE-DRIFT'])
mutant('MUT-RESIDUE-DRIFT', 'T1-RESIDUE',
       'the residue claimed fully readout-invariant -- the '
       'step-normalised idle conditional asserted to be (1/3,1/3,1/3) '
       'as well',
       residue_ok(_del_inv, _idle_inv_masslike, _idle_step),
       residue_ok(_del_inv, _idle_inv_masslike,
                  [Fr(1, 3), Fr(1, 3), Fr(1, 3)]),
       f"the step-normalised idle conditional is {frl(_idle_step)}; "
       f"asserting full invariance turns the gate's own "
       f"partiality conjunct false")
# <<<T1-CENSUS-REGION-END>>>

# THE TOKEN SCAN: that the census-shadow measurement never touches the
# constructed family is MEASURED, not asserted (operator M1.1).
_MK_A = '# <' + '<<T1-CENSUS-REGION-BEGIN>' + '>>'
_MK_B = '# <' + '<<T1-CENSUS-REGION-END>' + '>>'
_T1REGION = _src[_src.index(_MK_A) + len(_MK_A):_src.index(_MK_B)]
_GAMMA_TOKENS = ['A_MENU', 'A_REC', 'GAM_M', 'GAM_R', 'IDX_M', 'IDX_R',
                 'MASS_M', 'MASS_R', 'CNTFIX', 'CNTLIT', 'HOL[',
                 'W[', 'k_of(', 'kernel(', 'CARRIER']
_hits = {t: _T1REGION.count(t) for t in _GAMMA_TOKENS
         if _T1REGION.count(t)}
_leg_depths = sorted({len(b) + len(t4) for b, t4, ww, wn in LEGS1}
                     | {len(b) for b in R1BASES}
                     | {len(b) + len(t4) for b, t4, ww, wn in LEGS2}
                     | {len(b) for b in R2BASES})
_hits_mut = dict(_hits)
_hits_mut['GAM_M'] = 1


def gamma_free(hits, depths, cap):
    return len(hits) == 0 and min(depths) > 0 and max(depths) > cap


gate('T1-OFF-CARRIER', 'MUST',
     'THE SECOND CONVERGENT REASON, measured by a token scan of this '
     "file's own source: the census-shadow and law-value measurement "
     'region contains ZERO references to the constructed family, to '
     'either quotient, to the class indices, to the occupancy or to the '
     'kernels -- it is a measurement of the transport grammar, with '
     'Gamma absent -- and its leg ensembles live at depths that exceed '
     'the declared carrier cap',
     gamma_free(_hits, _leg_depths, CAP),
     f"region {len(_T1REGION)} chars between the two markers; "
     f"forbidden-token hits {_hits} over the scanned tokens "
     f"{_GAMMA_TOKENS}; leg-ensemble depths {_leg_depths} against the "
     f"carrier cap {CAP}",
     falsifiers=['MUT-TOKENSCAN-BLIND'])
mutant('MUT-TOKENSCAN-BLIND', 'T1-OFF-CARRIER',
       'a single reference to the constructed family planted in the '
       'scanned region',
       gamma_free(_hits, _leg_depths, CAP),
       gamma_free(_hits_mut, _leg_depths, CAP),
       f"one planted token gives hits {_hits_mut}, so the gate's own "
       f"zero-hit predicate turns false")

_targets_are_law_values = (LAW1 == SHADOW1 and LAW2 == SHADOW2)
T1_VERDICT = ('TARGETS-ARE-VALUES-OF-THE-LAW' if _targets_are_law_values
              else 'TARGETS-ARE-NOT-VALUES-OF-THE-LAW-AT-THE-DECLARED-'
                   'PRIMARY-READOUT')
emit("")
emit(f"  THE COMPARISON THE SETTLEMENT'S SECOND LINK RIDES ON: at the "
     f"declared primary readout the positional law is {frl(LAW1)} at "
     f"both legs; the pre-registered values are {frl(SHADOW1)} and "
     f"{frl(SHADOW2)}.  {T1_VERDICT}.")

# ======================================================================
# THE POSITIVE CONTROL -- the renewal cuts, and U1b's wall
# ======================================================================
sec("THE POSITIVE CONTROL -- Gamma at the RENEWAL cuts, and U1b's "
    "column-constancy wall")
L1 = sorted({payload_label(b[-1]) for b in R1BASES})
L2 = sorted({payload_label(t4[-1]) for b, t4, ww, wn in LEGS1})
JC = Counter()
JW = defaultdict(Fr)
for b, t4, ww, wn in LEGS1:
    JC[(payload_label(b[-1]), payload_label(t4[-1]))] += 1
    JW[(payload_label(b[-1]), payload_label(t4[-1]))] += ww
_dc = {a: sum(JC[(a, x)] for x in L2) for a in L1}
_dw = {a: sum(JW[(a, x)] for x in L2) for a in L1}
GREN = [[(Fr(JC[(a, c)], _dc[a]) if _dc[a] else Fr(0)) for a in L1]
        for c in L2]
GRENW = [[(JW[(a, c)] / _dw[a] if _dw[a] else Fr(0)) for a in L1]
         for c in L2]
_cols = {tuple(GREN[i][j] for i in range(len(L2))) for j in range(len(L1))}
_GREN_MUT = [[GREN[i][j] + (Fr(1, 8) if (i, j) == (0, 0) else Fr(0))
              for j in range(len(L1))] for i in range(len(L2))]
_cols_mut = {tuple(_GREN_MUT[i][j] for i in range(len(L2)))
             for j in range(len(L1))}
emit(f"  renewal-cut label sets: |L1| = {len(L1)}, |L2| = {len(L2)}; "
     f"joint cells {len(JC)}; leg counts per cell "
     f"{sorted(set(JC.values()))}; leg weights per cell "
     f"{sorted(set(str(v) for v in JW.values()))}")
emit(f"  Gamma(renewal 2 <- renewal 1) has {len(_cols)} distinct "
     f"column(s); every entry {sorted(set(str(GREN[i][j]) for i in range(len(L2)) for j in range(len(L1))))}")


def renewal_ok(M, cols):
    return (len(cols) == 1
            and all(M[i][j] == Fr(1, 8) for i in range(len(L2))
                    for j in range(len(L1))))


gate('T4-RENEWAL-POSITIVE', 'MUST',
     "THE POSITIVE CONTROL, and the wall stated: at renewal cuts "
     'Gamma is column-CONSTANT (one distinct column), so by U1b (D-2) '
     'DIVISIBLE is forced by structure before any test is run -- this '
     'unit makes NO indivisibility claim at renewal grain, at any '
     'scope; and the matrix is exactly J/8, U3\'s own committed passer',
     renewal_ok(GREN, _cols) and GREN == GRENW,
     f"distinct columns {len(_cols)}; every entry 1/8 "
     f"{all(GREN[i][j] == Fr(1, 8) for i in range(len(L2)) for j in range(len(L1)))}; "
     f"count and mass readouts agree {GREN == GRENW}",
     falsifiers=['MUT-RENEWAL-CORRUPT'])
mutant('MUT-RENEWAL-CORRUPT', 'T4-RENEWAL-POSITIVE',
       'one renewal-cut cell perturbed by 1/8 and the column census '
       'rebuilt on the perturbed matrix',
       renewal_ok(GREN, _cols), renewal_ok(_GREN_MUT, _cols_mut),
       f"the perturbed transfer has {len(_cols_mut)} distinct columns "
       f"and entries off 1/8, so U1b's (D-2) forcing no longer applies "
       f"and the gate's own predicate turns false")

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
  omission cannot move a single verdict in this census.
  AND THE ONE PASS IS THE KNOWN DEGENERATE, measured as such below:
  its columns are all equal, so it is doubly stochastic only because
  its column is uniform and it is unistochastic at every n.  It
  carries no quantum content whatever, and the verdict segment says
  so in the segment rather than in a footnote.""")


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


def screen_verdict(M, cert=None):
    R = ds_report(M)
    n = R['n']
    if not R['square']:
        return 'N/A-SHAPE', R, None
    if not R['ds']:
        return 'S-FAIL-DS', R, None
    if n == 3:
        T = tri_disc(*[M[i][0] * M[i][1] for i in range(3)])
        if T < 0:
            return 'S-FAIL-UNI', R, T
    if cert is not None:
        bad_u = sum(1 for i in range(n) for j in range(n)
                    if sum(cert[i][k] * cert[j][k] for k in range(n))
                    != (n if i == j else 0))
        bad_m = sum(1 for i in range(n) for j in range(n)
                    if Fr(cert[i][j] * cert[i][j], n) != M[i][j])
        return ('S-PASS' if (bad_u == 0 and bad_m == 0)
                else 'CERTIFICATE-FAILED'), R, (bad_u, bad_m)
    return 'EXCLUDED-BY-CAP', R, None


SCREEN = []


def screen(name, M, provenance, cert=None):
    v, R, extra = screen_verdict(M, cert)
    n, m = R['n'], R['m']
    if v == 'N/A-SHAPE':
        datum = (f"shape {n} x {m}; Barandes' criterion is defined for "
                 f"square matrices only and the trivial column "
                 f"completion is Theorem D1's move, SET ASIDE")
    elif v == 'S-FAIL-DS':
        datum = (f"shape {n} x {n}; sum|row deficit| = {R['L1row']}, "
                 f"sum|col deficit| = {R['L1col']}; PRICE: for every "
                 f"doubly-stochastic D, ||M - D||_1 >= "
                 f"{max(R['L1row'], R['L1col'])}; the DS failure is "
                 f"FORCED BY SHAPE for a column-stochastic M under the "
                 f"padding (a class realised at the later cut but not "
                 f"the earlier one has row sum > 1 the moment it "
                 f"receives mass), so the exact price is the datum")
        if n == 3:
            datum += ("; n = 3 triangle discriminant T = "
                      + str(tri_disc(*[M[i][0] * M[i][1]
                                       for i in range(3)])))
    elif v == 'S-FAIL-UNI':
        datum = f"triangle discriminant T = {extra} < 0"
    elif v == 'S-PASS':
        colconst = len({tuple(M[i][j] for i in range(n))
                        for j in range(n)}) == 1
        datum = (f"REAL ORTHOGONAL certificate U = H/sqrt({n}) with "
                 f"H the Sylvester Hadamard matrix: H H^T - {n} I "
                 f"has {extra[0]} non-zero entries; |U_ij|^2 - M_ij "
                 f"has {extra[1]} mismatches (verified in exact "
                 f"integer and rational arithmetic, no surd needed "
                 f"because every |U_ij|^2 is H_ij^2/{n}).  DEGENERACY, "
                 f"measured: columns all equal = {colconst}, so this "
                 f"matrix is unistochastic at EVERY n and the pass "
                 f"carries no quantum content")
    else:
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


def padded(GAM, V, dom, d, dd, cuts=None, style='identity'):
    """U1's DECLARED identity-padding CONVENTION and its three declared
    alternatives.  The configuration space is the union of the cuts'
    supports; a configuration NOT realised at the earlier cut is
    completed by the declared style:
      identity -- held fixed by the law (U1's convention);
      cyclic   -- sent to the next unrealised label by a fixed cycle;
      uniform  -- sent to the uniform distribution on all labels;
      marginal -- sent to the earlier cut's own class marginal."""
    cuts = cuts if cuts is not None else (d, dd)
    uni = sorted({V[h] for h in dom if len(h) in cuts}, key=sk)
    ix = {c: i for i, c in enumerate(uni)}
    M = [[Fr(0)] * len(uni) for _ in range(len(uni))]
    real = [c for c in uni if c in {V[h] for h in dom if len(h) == d}]
    other = [c for c in uni if c not in set(real)]
    marg = None
    if style == 'marginal':
        tot = sum(MASS_M[d][c] for c in real) if real else Fr(0)
        marg = {c: (MASS_M[d][c] / tot if tot else Fr(0)) for c in uni}
    for c in uni:
        if c in set(real):
            for s2, v in GAM[(dd, d)].get(c, {}).items():
                M[ix[s2]][ix[c]] = v
        elif style == 'identity':
            M[ix[c]][ix[c]] = Fr(1)
        elif style == 'cyclic':
            j = other.index(c)
            M[ix[other[(j + 1) % len(other)]]][ix[c]] = Fr(1)
        elif style == 'uniform':
            for s2 in uni:
                M[ix[s2]][ix[c]] = Fr(1, len(uni))
        else:
            for s2 in uni:
                M[ix[s2]][ix[c]] = marg.get(s2, Fr(0))
    return M, uni, sorted(ix[c] for c in real), sorted(ix[c] for c in other)


for (dd, d) in [(1, 0), (2, 1), (3, 2), (4, 3), (4, 2)]:
    screen(f"Gamma_MENU({dd}<-{d}) RAW", dense(GAM_M, IDX_M, d, dd),
           f"the constructed family on the MENU carrier, cuts {d}->{dd}")
for (dd, d) in [(2, 1), (3, 2), (4, 3)]:
    M, uni, _r, _o = padded(GAM_M, A_MENU, CARRIER, d, dd)
    screen(f"Gamma_MENU({dd}<-{d}) IDENTITY-PADDED", M,
           f"the same family under U1's declared identity-padding "
           f"CONVENTION on the union support ({len(uni)} labels)")
screen("Gamma_RENEWAL(r2<-r1) [POSITIVE CONTROL]", GREN,
       "the renewal-cut family on the 8 payload labels; U3's own "
       "committed passer J/8", cert=hadamard(8))
_misM, _misU, _misR, _misO = padded(GAM_M, A_MENU, CARRIER, 1, 2)
_misS = set(_misR)
_mis = [[(_misM[i][j] * Fr(3, 2) if j in _misS else _misM[i][j])
         for j in range(len(_misU))] for i in range(len(_misU))]
screen("Gamma_MENU(2<-1) MIS-NORMALIZED [NEGATIVE CONTROL]", _mis,
       "the identity-padded transfer with every realised column "
       "re-weighted by 3/2: the screen must see the broken "
       "normalization exactly")

_tally = Counter(s['verdict'] for s in SCREEN)
_n3 = [s for s in SCREEN if s['shape'][0] == 3 and s['shape'][1] == 3]
_pass_row = [s for s in SCREEN if s['verdict'] == 'S-PASS']
_pass_degenerate = (len({tuple(GREN[i][j] for i in range(len(L2)))
                         for j in range(len(L1))}) == 1)
_tally_mut = Counter(_tally)
_tally_mut['S-PASS'] -= 1
_tally_mut[screen_verdict(_GREN_MUT, hadamard(8))[0]] += 1


def screen_ok(tally, degenerate):
    return (tally.get('S-PASS', 0) == 1 and tally.get('N/A-SHAPE', 0) == 5
            and tally.get('S-FAIL-DS', 0) == 4 and bool(degenerate))


gate('T3-SCREEN', 'MUST',
     'THE U3 SCREEN, run on Gamma: the census composition is the '
     'result, and it is gated exactly -- five N/A-SHAPE, four '
     'S-FAIL-DS with exact L1 prices, ONE S-PASS, and that pass is '
     'MEASURED degenerate (its columns are all equal, so it is '
     'unistochastic at every n).  The positive half of the Barandes '
     'correspondence is EMPTY at every object this unit builds',
     screen_ok(_tally, _pass_degenerate),
     f"census {ctr(_tally)}; the single S-PASS is column-constant "
     f"{_pass_degenerate} -- the known degenerate J/8; n = 3 objects "
     f"arising from the construction: {len(_n3)} (the n = 3 "
     f"discriminant cell is EMPTY-BY-SHAPE: the family's shapes are "
     f"{fl(DIMS_M)} and their padded completions); EXCLUDED-BY-CAP "
     f"{_tally.get('EXCLUDED-BY-CAP', 0)}",
     falsifiers=['MUT-SCREEN-FLIP'])
mutant('MUT-SCREEN-FLIP', 'T3-SCREEN',
       'the positive control perturbed off double stochasticity and the '
       'screen re-run on the perturbed matrix',
       screen_ok(_tally, _pass_degenerate),
       screen_ok(_tally_mut, _pass_degenerate),
       f"perturbing one entry of J/8 makes the screen return "
       f"{screen_verdict(_GREN_MUT, hadamard(8))[0]} instead of "
       f"S-PASS, so the census becomes {ctr(_tally_mut)} and the "
       f"gate's own composition predicate turns false")

# ======================================================================
# TEST 4 -- THE [B3] INTERPOLANT TEST
# ======================================================================
sec("TEST 4 -- THE [B3] INTERPOLANT TEST on Gamma")
emit("""  The never-square-supports caveat is carried verbatim from U1:
  Barandes' eq. 22 needs a square Gamma -- one fixed configuration
  space for all cuts -- and this carrier has none away from renewals.
  The identity padding is a declared CONVENTION, not a fact about the
  process.  This delivery no longer stops at one convention: FOUR are
  run, and the fiber that matters is measured -- how many completions
  let the algebraic reading SPEAK, and whether the ones that speak
  agree.""")


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
CKR = OCC_CK_R
_live = [r for r in CK if r['cut'] > 0]
_CK_MUT = [dict(r) for r in CK]
for _r in _CK_MUT:
    _r['interpolates'] = True
    _r['differing'] = 0


def ck_ok(ck, ckr):
    live = [r for r in ck if r['cut'] > 0]
    return (all(r['interpolates'] for r in ck if r['cut'] == 0)
            and all(not r['interpolates'] for r in live)
            and all(r['interpolates'] for r in ckr))


gate('T4-CK', 'MUST',
     "the [B3] existence question, decided constructively where it "
     "can be: the process's own intermediate conditional is the "
     'canonical interpolant candidate, and it is tested cut-triple by '
     'cut-triple on the carrier and on the negative control.  AT THE '
     'DECLARED READOUT -- the count control above shows the record '
     'quotient loses exact lumpability under the other one',
     ck_ok(CK, CKR),
     f"MENU: {sum(1 for r in CK if r['interpolates'])} of {len(CK)} "
     f"triples divide by the process's own conditional; the "
     f"{len(_live)} triples with a non-degenerate first cut fail at "
     f"{[r['differing'] for r in _live]} cells; REC (negative "
     f"control): {sum(1 for r in CKR if r['interpolates'])} of "
     f"{len(CKR)} -- the record chain is EXACTLY lumpable",
     falsifiers=['MUT-CK-CORRUPT'])
mutant('MUT-CK-CORRUPT', 'T4-CK',
       'the carrier chain declared Markov -- every triple marked as '
       'interpolating -- and the census re-evaluated',
       ck_ok(CK, CKR), ck_ok(_CK_MUT, CKR),
       f"the carrier genuinely fails CK at "
       f"{[r['differing'] for r in _live]} cells; a census asserting "
       f"that it divides everywhere turns the gate's own "
       f"non-degenerate-cut conjunct false")


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


def perm_inverse(Q):
    """Q is expected to be a permutation matrix; verify it and return
    its transpose, else None."""
    n = len(Q)
    for i in range(n):
        if sum(1 for j in range(n) if Q[i][j] == 1) != 1:
            return None
        if sum(1 for j in range(n) if Q[i][j] != 0) != 1:
            return None
    for j in range(n):
        if sum(1 for i in range(n) if Q[i][j] == 1) != 1:
            return None
    return [[Q[j][i] for j in range(n)] for i in range(n)]


def inverse_blocked(P, R, O):
    """Exact inverse of a padded transfer whose unrealised columns form
    a block: with R gathered first, P = [[A, 0], [B, Q]] and
    P^-1 = [[A^-1, 0], [-Q^-1 B A^-1, Q^-1]].  The whole inversion
    costs |R|^3 plus a permutation transpose, not |P|^3, and it is
    exact.  Returns None if the block structure fails (the
    mass-spreading completions) or if A is singular."""
    for j in O:
        for i in R:
            if P[i][j] != 0:
                return None
    A = [[P[i][j] for j in R] for i in R]
    B = [[P[i][j] for j in R] for i in O]
    Q = [[P[i][j] for j in O] for i in O]
    Ai = inverse(A)
    Qi = perm_inverse(Q)
    if Ai is None or Qi is None:
        return None
    n = len(P)
    out = [[Fr(0)] * n for _ in range(n)]
    for jj, j in enumerate(R):
        for ii, i in enumerate(R):
            out[i][j] = Ai[ii][jj]
        col = [-sum(B[ii][t] * Ai[t][jj] for t in range(len(R)))
               for ii in range(len(O))]
        for ii, i in enumerate(O):
            out[i][j] = sum(Qi[ii][t] * col[t] for t in range(len(O)))
    for jj, j in enumerate(O):
        for ii, i in enumerate(O):
            out[i][j] = Qi[ii][jj]
    return out


def duplicate_columns(M):
    """Two identical columns is an exact certificate of singularity."""
    seen = {}
    for j in range(len(M[0])):
        col = tuple(M[i][j] for i in range(len(M)))
        if col in seen:
            return (seen[col], j)
        seen[col] = j
    return None


TRIPLES = [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
EQ22 = []
PADFIBER = []
prog("eq. 22 under four declared completions ...")
for style in ('identity', 'cyclic', 'uniform', 'marginal'):
    for (d, md, dd) in TRIPLES:
        CUTS = (d, md, dd)
        P1, uni, R, O = padded(GAM_M, A_MENU, CARRIER, d, md, cuts=CUTS,
                               style=style)
        dup = duplicate_columns(P1)
        if style in ('uniform', 'marginal'):
            row = dict(style=style, triple=[d, md, dd], labels=len(uni),
                       unrealised=len(O), invertible=False,
                       singular_certificate=(f"columns {dup[0]} and "
                                             f"{dup[1]} are identical"
                                             if dup else None),
                       reading='SILENT: the first transfer is SINGULAR '
                               'under this completion -- every '
                               'unrealised column carries the same '
                               'vector, so two columns coincide '
                               'exactly -- and eq. 22 has no unique '
                               'algebraic interpolant at all')
            if dup is None:
                row['reading'] = ('UNDECIDED: no duplicate-column '
                                  'certificate was found at this '
                                  'completion and no inversion was '
                                  'attempted')
            PADFIBER.append(row)
            emit(f"  eq. 22 [{style}] at ({d},{md},{dd}) on {len(uni)} "
                 f"padded labels: SINGULAR by exact certificate "
                 f"({row['singular_certificate']}) -- the algebraic "
                 f"reading is SILENT")
            continue
        P2, _u2, _r2, _o2 = padded(GAM_M, A_MENU, CARRIER, d, dd,
                                   cuts=CUTS, style=style)
        inv = inverse_blocked(P1, R, O)
        if inv is None:
            row = dict(style=style, triple=[d, md, dd], labels=len(uni),
                       unrealised=len(O), invertible=False,
                       singular_certificate=None,
                       reading='SILENT: no unique algebraic interpolant')
            PADFIBER.append(row)
            emit(f"  eq. 22 [{style}] at ({d},{md},{dd}): SINGULAR -- "
                 f"the algebraic reading is SILENT")
            continue
        Gb = matmul(P2, inv)
        negs = sum(1 for r in Gb for x in r if x < 0)
        cs = [sum(Gb[i][j] for i in range(len(Gb)))
              for j in range(len(Gb))]
        mostneg = sorted((x for r in Gb for x in r if x < 0))[:4]
        row = dict(style=style, triple=[d, md, dd], labels=len(uni),
                   unrealised=len(O), invertible=True, negatives=negs,
                   colsums_all_one=all(c == 1 for c in cs),
                   most_negative=[str(x) for x in mostneg],
                   reading=('PSEUDO-STOCHASTIC: the unique algebraic '
                            'interpolant has negative entries, so no '
                            'stochastic interpolant of eq. 22 form '
                            'exists -- REFUTED outright, no Farkas '
                            'vector needed'
                            if negs else
                            'STOCHASTIC: the unique algebraic '
                            'interpolant is column-stochastic'))
        PADFIBER.append(row)
        if style == 'identity':
            EQ22.append(row)
        emit(f"  eq. 22 [{style}] at ({d},{md},{dd}) on {len(uni)} "
             f"padded labels: INVERTIBLE; Gammabar has {negs} negative "
             f"entries; column sums all exactly 1 = "
             f"{all(c == 1 for c in cs)}"
             + (f"; most negative {[str(x) for x in mostneg]}" if negs
                else ""))

_speak = sorted({r['style'] for r in PADFIBER if r['invertible']})
_silent = sorted({r['style'] for r in PADFIBER if not r['invertible']})
_negs_by_style = {s: [r['negatives'] for r in PADFIBER
                      if r['style'] == s and r['invertible']]
                  for s in _speak}
_agree = (len({tuple(v) for v in _negs_by_style.values()}) == 1)
emit(f"  THE PADDING FIBER, MEASURED WITH ITS SEMANTICS DECLARED: "
     f"{len(PADFIBER) // len(TRIPLES)} completions tested; "
     f"{len(_speak)} let the algebraic reading SPEAK ({_speak}) and "
     f"{len(_silent)} are SILENT ({_silent}); the negative-entry "
     f"counts of the completions that speak are {_negs_by_style} -- "
     f"identical {_agree}.  So the fiber that carries the RESULT is "
     f"{len(_speak)}, not the number of conventions imaginable, and "
     f"the result does not turn on the choice between them.")

_EQ22_MUT = [dict(r, negatives=0,
                  reading='STOCHASTIC: the unique algebraic '
                          'interpolant is column-stochastic')
             for r in EQ22]
_EQ22_COUNTS = [36, 104, 108, 164]


def eq22_ok(rows):
    return (len(rows) == len(TRIPLES)
            and all(r['invertible'] for r in rows)
            and all(r['negatives'] > 0 for r in rows)
            and all(r['colsums_all_one'] for r in rows)
            and [r['negatives'] for r in rows] == _EQ22_COUNTS)


gate('T4-EQ22', 'MUST',
     "THE VALUE CENSUS OF THE INTERPOLANT SIGN, gated (the previous "
     'delivery gated no sign at all and a zeroed negative count '
     'survived a whole run): at every depth-cut triple with a '
     'non-degenerate first cut the unique algebraic candidate exists, '
     'its columns sum to exactly 1, and it carries a POSITIVE number '
     'of negative entries -- and the four counts themselves are gated '
     'against their exact values',
     eq22_ok(EQ22),
     "; ".join(f"({r['triple'][0]},{r['triple'][1]},{r['triple'][2]}) "
               f"negatives {r['negatives']} min "
               f"{r['most_negative'][0] if r['most_negative'] else '-'}"
               for r in EQ22)
     + f"; counts {[r['negatives'] for r in EQ22]} against the exact "
       f"census {_EQ22_COUNTS}; column sums all one "
       f"{all(r['colsums_all_one'] for r in EQ22)}",
     falsifiers=['MUT-EQ22-SIGN'])
mutant('MUT-EQ22-SIGN', 'T4-EQ22',
       'the negative entries of the eq.-22 candidate counted as zero -- '
       'the injection that flipped all four readings from REFUTED to '
       'STOCHASTIC and survived the previous instrument at exit 0',
       eq22_ok(EQ22), eq22_ok(_EQ22_MUT),
       f"with the sign census zeroed the four readings flip to "
       f"STOCHASTIC and the gate's own positive-count predicate turns "
       f"false")


def padding_ok(dims, rows, speak, agree):
    return (dims[1] != dims[2] and dims[2] != dims[3]
            and len(rows) == len(TRIPLES) * 4
            and len(speak) >= 2 and bool(agree)
            and all(r.get('singular_certificate')
                    for r in rows if not r['invertible']))


gate('T4-PADDING', 'MUST',
     "U1's never-square-supports caveat and identity-padding "
     'CONVENTION are carried and declared: the carrier has no fixed '
     'configuration space away from renewals, the padding is a '
     'convention, and the FIBER IS MEASURED WITH ITS SEMANTICS NAMED '
     '-- four completions run, at least two let the reading speak, and '
     'those that speak return identical negative-entry counts, so the '
     'refutation does not turn on the convention',
     padding_ok(DIMS_M, PADFIBER, _speak, _agree),
     f"raw shapes across cuts {fl(DIMS_M)} -- never square away from "
     f"renewals; {len(PADFIBER)} padded readings over "
     f"{len(TRIPLES)} triples x 4 completions; speak {_speak}, silent "
     f"{_silent}; counts agree across the speaking completions "
     f"{_agree}",
     falsifiers=['MUT-PADDING-DROP'])
mutant('MUT-PADDING-DROP', 'T4-PADDING',
       'the fiber sweep reduced to the single identity convention -- '
       'the previous delivery\'s scope, in which the result\'s '
       'robustness was unmeasured',
       padding_ok(DIMS_M, PADFIBER, _speak, _agree),
       padding_ok(DIMS_M, [r for r in PADFIBER
                           if r['style'] == 'identity'], ['identity'],
                  _agree),
       f"with only the identity completion run the sweep has "
       f"{len(TRIPLES)} rows and one speaking completion, so the "
       f"gate's own fiber conjunct turns false")

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
# THE CENSUSED CELLS, and their confound.  Both cells sit at renewal
# count n = 4; the three coordinates paper-09's adjudication ordered
# carried -- ordinal position, absolute depth, ensemble identity --
# move TOGETHER across them, so nothing separates them.
CELLS = [dict(cell='leg 1', ordinal=1, base_depth=3, end_depth=7,
              ensemble='E2', renewal_count=4,
              law=[str(x) for x in LAW1]),
         dict(cell='leg 2', ordinal=2, base_depth=6, end_depth=10,
              ensemble='E3', renewal_count=4,
              law=[str(x) for x in LAW2])]
_n_values = len({c['renewal_count'] for c in CELLS})
_moving = [k for k in ('ordinal', 'base_depth', 'ensemble')
           if len({c[k] for c in CELLS}) == len(CELLS)]
_in_simplex = (all(x >= 0 for x in LAW1) and sum(LAW1) == 1
               and all(x >= 0 for x in LAW2) and sum(LAW2) == 1)
_one_point = (LAW1 == LAW2)
emit(f"  THE ANSWER, WITH ITS SCOPE STAMPED.  At the declared primary "
     f"readout Gamma's process induces ONE point, {frl(LAW1)}, at both "
     f"censused cells -- a point of the very simplex CR-B's symmetry "
     f"could not select.  BUT BOTH CELLS SIT AT n = 4: constancy "
     f"across two cells at ONE value of n is not n-indexing, and the "
     f"three coordinates {_moving} move together across them, so "
     f"ordinal position, absolute depth and ensemble identity are "
     f"CONFOUNDED.  The honest stamp is CONSTANT-ACROSS-THE-TWO-"
     f"CENSUSED-CELLS-AT-n=4; ORDINAL/DEPTH/ENSEMBLE-CONFOUNDED.")
_CELLS_MUT = [CELLS[0]]


def crb_ok(cells, in_simplex, one_point, n_values, moving):
    return (in_simplex and one_point and len(cells) == 2
            and n_values == 1 and len(moving) == 3)


gate('T5-CRB', 'MUST',
     "CR-B's kernel question, answered WITH ITS SCOPE: the constructed "
     "family's process DOES induce an interval-positional law -- a "
     "point of the simplex CR-B's symmetry could not select -- and it "
     'is the SAME point at both censused cells.  The scope is gated '
     'rather than claimed: exactly two cells were censused, both at '
     'renewal count n = 4, and all three of the confounded coordinates '
     'move together across them, so NO n-indexing is inferred from a '
     'single value of n',
     crb_ok(CELLS, _in_simplex, _one_point, _n_values, _moving),
     f"n = 4 simplex dimension {_crb_n4['pinned_simplex_dim']}, "
     f"orbits {_crb_n4['pinned_orbits']}, transitive "
     f"{_crb_n4['pinned_transitive']} (no unique invariant law); the "
     f"induced law is {frl(LAW1)} at both cells, in the simplex "
     f"{_in_simplex}; cells censused {len(CELLS)}; distinct renewal "
     f"counts {_n_values}; confounded coordinates {_moving}",
     falsifiers=['MUT-CRB-COLLAPSE'])
mutant('MUT-CRB-COLLAPSE', 'T5-CRB',
       'the two censused cells collapsed into one -- the reading in '
       'which a single cell is presented as a census',
       crb_ok(CELLS, _in_simplex, _one_point, _n_values, _moving),
       crb_ok(_CELLS_MUT, _in_simplex, _one_point, _n_values, _moving),
       f"a one-cell census cannot support a constancy statement at all, "
       f"so the gate's own two-cell conjunct turns false")

# ======================================================================
# TEST 6 -- CR-A's MOVER QUESTION
# ======================================================================
sec("TEST 6 -- CR-A's MOVER QUESTION: does Gamma force an advancing "
    "mover?")
emit(f"  CR-A's committed head: {pv(CRA, 'verdict_head')}")
emit(f"  CR-A's committed census: {pv(CRA, 'verdict_segments/2')}; "
     f"{pv(CRA, 'verdict_segments/3')}.")
_stat = 0
_movingcols = 0
for d in range(CAP):
    for s, row in GAM_M[(d + 1, d)].items():
        if len(row) == 1 and s in row:
            _stat += 1
        else:
            _movingcols += 1
_selftrans = sum(1 for d in range(CAP)
                 for s, row in GAM_M[(d + 1, d)].items() if s in row)
emit(f"  Gamma's own motion on the carrier: {_movingcols} of "
     f"{_movingcols + _stat} one-step columns move the class; "
     f"{_selftrans} columns carry a non-zero self-transition; "
     f"stationary columns {_stat}")

# THE SHARED-CARRIER COUNT IS MEASURED, NOT DECLARED.  The previous
# delivery set it to the literal 0 and printed it as though measured
# (instrument D7).  It is now a scan of every pinned source for a
# declared map between the record lattice CR-A censuses and this
# unit's carrier.
_BR_LHS = ('H_a[N]', 'I7', 'record lattice')
_BR_RHS = ('MENU', 'transport grammar')
_BR_REL = ('map ', 'functor', 'bijection', 'identification',
           'isomorphism', 'embedding')


def bridge_scan(bodies):
    hits = []
    for sid, body in bodies:
        for ln in (body or '').splitlines():
            if (any(x in ln for x in _BR_LHS)
                    and any(x in ln for x in _BR_RHS)
                    and any(x in ln for x in _BR_REL)):
                hits.append((sid, ln.strip()[:120]))
    return hits


_BODIES = [(sid, SRC[sid][4]) for sid, _s, _p, _w, _pe in SOURCES]
_shared_hits = bridge_scan(_BODIES)
_shared = len(_shared_hits)
_BODIES_MUT = _BODIES + [('SYNTHETIC',
                          'a declared bijection map between the MENU '
                          'quotient and I7 record lattice of H_a[N]')]
_shared_mut = len(bridge_scan(_BODIES_MUT))
emit(f"  THE SHARED-CARRIER SCAN, measured over all {len(_BODIES)} "
     f"pinned source bodies: lines declaring a map between the record "
     f"lattice / H_a[N] and this unit's MENU carrier: {_shared} "
     f"{_shared_hits}")


def cra_ok(mv, shared, forced):
    return mv > 0 and shared == 0 and forced == 'FORCED=2|FORCED-ADVANCING=0'


gate('T6-CRA', 'MUST',
     "CR-A's mover question, answered at the four-gate standard: "
     'Gamma IS a geometry-update law on ITS OWN carrier and it '
     'advances there; but CR-A\'s census lives on I7\'s record '
     'lattice, this unit\'s carrier is the MENU quotient of the '
     'transport grammar, and the count of declared maps between the '
     'two is MEASURED over every pinned source and is zero -- so the '
     'commutation status with H_a[N] is BLOCKED-AT-REFERENT and the '
     '1,232/0 census is untouched by this unit',
     cra_ok(_movingcols, _shared, pv(CRA, 'verdict_segments/3')),
     f"Gamma advances on its own carrier ({_movingcols} moving "
     f"columns, {_stat} stationary); declared maps between the two "
     f"carriers, MEASURED over {len(_BODIES)} pinned sources: "
     f"{_shared} -- COMMUTATION EXCLUDED-BY-REFERENT; CR-A's anchored "
     f"census {pv(CRA, 'verdict_segments/2')} and "
     f"{pv(CRA, 'verdict_segments/3')} stand untouched",
     falsifiers=['MUT-CRA-BRIDGE'])
mutant('MUT-CRA-BRIDGE', 'T6-CRA',
       'a declared bijection between the MENU quotient and the record '
       'lattice planted in the scanned source corpus',
       cra_ok(_movingcols, _shared, pv(CRA, 'verdict_segments/3')),
       cra_ok(_movingcols, _shared_mut, pv(CRA, 'verdict_segments/3')),
       f"the planted declaration raises the measured map count to "
       f"{_shared_mut}, so the gate's own zero-map predicate turns "
       f"false -- the count is a measurement and can move")

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
# THE CLAIM COUNT IS MEASURED, NOT DECLARED.  The previous delivery set
# it to the literal [] and the paper said "the count is gated rather
# than promised" -- which was false (instrument D7).  It is now a
# sentence scan of this unit's OWN emitted text and of its paper.
_CURV = ('curvature', 'holonomy', 'non-unit', 'obstruction')
_QUANT = ('quantum', 'indivisib', 'born rule', 'unistochastic')
_INFER = ('therefore', 'hence', 'implies', 'licenses', 'entails',
          'shows that', 'means that', 'so it is', 'proves that')
_NEG = ('no ', 'not ', 'never', 'forbid', 'cannot', 'may not', 'zero',
        'without', 'refus', 'makes no', 'nothing is inferred',
        'does not', 'none', 'empty', 'silent')


def sentences(text):
    out = []
    for chunk in text.replace('\n', ' ').split('. '):
        c = chunk.strip()
        if c:
            out.append(c)
    return out


def claim_scan(text):
    cand, claims = [], []
    for s in sentences(text):
        low = s.lower()
        if (any(x in low for x in _CURV) and any(x in low for x in _QUANT)
                and any(x in low for x in _INFER)):
            cand.append(s)
            if not any(x in low for x in _NEG):
                claims.append(s)
    return cand, claims


_SCANTEXT = "\n".join(OUT_LINES) + "\n" + PAPER_TEXT
_cand, _claims = claim_scan(_SCANTEXT)
_SYNTH_CLAIM = ('The measured curvature of the constructed family '
                'therefore establishes that the process is quantum.')
_cand_m, _claims_m = claim_scan(_SCANTEXT + "\n" + _SYNTH_CLAIM)
emit(f"  THE CLAIM SCAN, measured over this unit's own emitted text "
     f"({len(OUT_LINES)} lines) and its paper "
     f"({len(PAPER_TEXT)} chars): sentences carrying a curvature term, "
     f"a quantum term AND an inference term: {len(_cand)}; of those, "
     f"sentences carrying no negation: {len(_claims)}.")
for s in _claims:
    emit(f"    CLAIM: {s[:160]}")


def wcross_ok(claims, wc):
    return len(claims) == 0 and len(wc) >= 2


gate('T7-WCROSS', 'MUST',
     "U2's W-CROSS binds any curvature => quantum reading: the three "
     'loci (curved / refused / non-lumpable) do not coincide at cut '
     'grain and no single grammar quantity predicts all three, so a '
     'curvature measurement does not license a quantum verdict.  THIS '
     'UNIT MAKES NO SUCH CLAIM AND THE COUNT IS NOW MEASURED, by a '
     "sentence scan of the unit's own emitted text and paper, not "
     'declared by a literal',
     wcross_ok(_claims, _wc),
     f"curvature => quantum claims MEASURED in this unit: "
     f"{len(_claims)} (candidate sentences before the negation filter: "
     f"{len(_cand)}); W-CROSS clauses located in the committed U2 "
     f"note: {len(_wc)} of 3; the constructed family's curvature is "
     f"reported as a measured group ({_gm['primes']}, rank "
     f"{_gm['rank']}) and nothing is inferred from it about "
     f"quantumness",
     falsifiers=['MUT-WCROSS-CLAIM'])
mutant('MUT-WCROSS-CLAIM', 'T7-WCROSS',
       'a curvature => quantum sentence appended to the scanned text',
       wcross_ok(_claims, _wc), wcross_ok(_claims_m, _wc),
       f"the appended sentence raises the measured claim count to "
       f"{len(_claims_m)}, so the gate's own zero-claim predicate "
       f"turns false -- the count is a measurement and can move")

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
_desc_shared = len({A_MENU[c[0] + (c[1], c[2])] for c in _desc}
                   & {A_MENU[c[0] + (c[2], c[1])] for c in _desc})


def d44_ok(ncurv, ndesc, spec):
    return (ncurv == 44 and ndesc == 44
            and sum(v for k, v in spec.items() if k != 1) == ncurv)


_gam44_mut = Counter({Fr(1): 44})
gate('T9-44', 'MUST',
     "the 44 + 44 dichotomy under the constructed family: the "
     'curvature half closes in the carrier and Gamma assigns it a '
     'non-trivial holonomy at EVERY one of the 44; the '
     'descent-obstruction half does not close in the carrier at all, '
     'so Gamma has NO LOOP there and assigns it nothing -- the '
     'constructed law is silent on exactly the half D74 named as '
     'having no formalism at transport scope.  THE SPECTRUM IS '
     'READOUT-RELATIVE and the qualitative half is not',
     d44_ok(len(_curv), len(_desc), _gam44),
     f"curvature half: {len(_curv)} squares, Gamma-holonomy non-unit "
     f"at {sum(v for k, v in _gam44.items() if k != 1)} of "
     f"{sum(_gam44.values())}, spectrum {ctr(_gam44)}; "
     f"descent-obstruction half: {len(_desc)} squares, endpoints in "
     f"DIFFERENT carrier classes at {len(_desc)} of {len(_desc)} -- "
     f"NOT A LOOP UNDER Gamma",
     falsifiers=['MUT-44-MERGE'])
mutant('MUT-44-MERGE', 'T9-44',
       'the curvature half assigned trivial holonomy -- the reading in '
       'which the constructed family sees no curvature at all',
       d44_ok(len(_curv), len(_desc), _gam44),
       d44_ok(len(_curv), len(_desc), _gam44_mut),
       f"a trivial spectrum leaves 0 non-unit of 44, so the gate's own "
       f"every-one-of-the-44 predicate turns false")

# ======================================================================
# TEST 8 -- THE MOTIVATION INVENTORY (the RSQ standard), WITH THE
# CLASSIFICATION COLUMN GATED AGAINST A MACHINE-COMPUTED FIBER
# ======================================================================
sec("TEST 8 -- THE MOTIVATION INVENTORY on Gamma's OWN construction")
emit("""  The RSQ standard: every choice the construction makes is
  classed FORCED (the pinned sources leave exactly one), STABILIZER-
  FIXED (a declared symmetry or gate of the arena selects it) or
  GENUINELY-FREE (the fiber has more than one element and nothing
  pinned selects one), with the exact fiber printed.  THE
  CLASSIFICATION COLUMN IS NOW GATED: wherever a fiber is machine-
  computable the declared class must agree with it, and a reclassified
  row fails the gate.  The previous delivery's classification column
  was ungated and a genuinely-free choice relabelled FORCED survived a
  whole run.""")
_rung_fiber = 0
for nm, V in (('REC', A_REC), ('MENU', A_MENU)):
    menus = defaultdict(set)
    for h in CARRIER:
        menus[V[h]].add(tuple(sorted((evsk(e), str(q))
                                     for e, q in CACHE[h])))
    md = all(len(s) == 1 for s in menus.values())
    nonflat = HOL[nm]["q (D74's connection)"]['obstruction'] > 0
    if md and nonflat:
        _rung_fiber += 1
_grain_fiber = len({pv(GPR, 'grain_primary_classes'),
                    pv(GPR, 'grain_control_classes')})
_cuts_fiber = 2      # depth cuts and renewal cuts, BOTH built here
_readout_fiber = _distinct
_padding_fiber = len(_speak)
_prune_fiber = 1 if _sub == _uns else 2
INVENTORY = [
    dict(id='I-CARRIER', choice='the quotient Gamma is read on',
         cls='FORCED', fibre=1, fibre_computed=_rung_fiber,
         scope='FORCED AMONG D74\'s SIX COMMITTED RUNGS; GENUINELY '
               'FREE IN THE QUOTIENT LATTICE -- the adjudication\'s '
               'carrier ruling names CONG-185, d74\'s own coarsest '
               'weighted congruence, as a strictly better carrier by '
               'this unit\'s OWN stated criterion, and this unit does '
               'not build it (see the next-iteration register)',
         why="D74's committed ladder has six rungs, and the pin names "
             "one: the MENU quotient is the COARSEST DESCENT quotient "
             "(menu descends 113/113) and, among the two rungs this "
             "unit rebuilds, the only one at which the connection "
             "both descends and is non-flat.",
         measured=None),
    dict(id='I-CAP', choice='the depth cap of the carrier',
         cls='FORCED', fibre=1, fibre_computed=1, scope=None,
         why="the pin declares D74's (A,B) d <= 4 arena; the next depth "
             "is a different arena with a different class count (D74's "
             "committed 265 at d <= 5) and is EXCLUDED-BY-CAP here.",
         measured=None),
    dict(id='I-GRAIN', choice='the menu grain',
         cls='GENUINELY-FREE', fibre=2, fibre_computed=_grain_fiber,
         scope=None,
         why="Gamma-prep declares two grains -- the kind x weight "
             "primary and the event x weight control -- and measures "
             "that they disagree.  The pin selects the 113-class one "
             "because it is D74's carrier; nothing pinned forces it.",
         measured=None),
    dict(id='I-HORIZON', choice='the horizon convention',
         cls='GENUINELY-FREE', fibre=2, fibre_computed=None,
         scope='NOT MACHINE-COMPUTABLE HERE: the alternative convention '
               'is declared by Gamma-prep and is not run in this unit, '
               'so the fiber is DECLARED and is stamped as such',
         why="Gamma-prep prints two conventions (H7 and MATCHED) and "
             "declares that naming one silently is the defect its "
             "predecessor's round convicted.  This unit declares H4 -- "
             "the arena-matched chain that terminates exactly at the "
             "cap -- and the alternative is not run here.",
         measured=None),
    dict(id='I-CUTS', choice='the cut family',
         cls='GENUINELY-FREE', fibre=2, fibre_computed=_cuts_fiber,
         scope=None,
         why="depth cuts (the primary family) and renewal cuts (the "
             "positive control) are both declared by the pin and both "
             "built here; the corpus supplies no principle selecting "
             "one, and the two give DIFFERENT answers to the "
             "interpolant question.",
         measured=None),
    dict(id='I-READOUT', choice='the readout',
         cls='GENUINELY-FREE', fibre=3, fibre_computed=_readout_fiber,
         scope='THE FIBER IS AT LEAST THREE and this item covers TWO '
               'DIFFERENT FIBERS the previous delivery folded into '
               'one: at the CARRIER level the choice is the occupancy '
               'w against the uniform measure on classes; at the LEG '
               'level it is the step-normalised q/M against the raw '
               'price product against the uniform measure on legs.  A '
               'fourth leg-level reading -- the H4 chain itself -- is '
               'EXCLUDED-BY-CAP',
         why="the horizon kernel does NOT descend on the carrier "
             "(measured: the horizon potential is class-multi-valued), "
             "so a class-level law needs a lift.  Three readings are "
             "measured and they give three different positional laws.  "
             "This is the effectus's I-READOUT item and it is the "
             "single most load-bearing free choice in the unit.",
         measured=None),
    dict(id='I-PADDING', choice='the completion convention for eq. 22',
         cls='GENUINELY-FREE', fibre=2, fibre_computed=_padding_fiber,
         scope='FIBER SEMANTICS DECLARED: the fiber counted is '
               'COMPLETIONS THAT SUPPORT A READING, not completions '
               'imaginable.  Four are run; two speak and agree on '
               'every count; two are exactly singular and say nothing',
         why="U1's declared convention (hold an unrealised "
             "configuration fixed) against three alternatives, all "
             "run here; every eq.-22 count is relative to a completion "
             "and is quoted with it.",
         measured=None),
    dict(id='I-PRUNE', choice='the leg-2 enumeration prune',
         cls='STABILIZER-FIXED', fibre=1, fibre_computed=_prune_fiber,
         scope='THE GATE\'S OWN SCOPE, printed: the unpruned agreement '
               'is checked on 3 of the 256 bases',
         why="the pattern prune is not a choice about the object: it "
             "is gated against an UNPRUNED scan on a declared "
             "subsample and reproduces it leg for leg and weight for "
             "weight, at both weights.",
         measured=None),
    dict(id='I-RENEWAL', choice='the renewal predicate',
         cls='FORCED', fibre=1, fibre_computed=1, scope=None,
         why="U1's committed is_R4 -- tag 'r' with two proposers in "
             "the ckey -- ported verbatim; it reads no state and this "
             "unit re-implements nothing.",
         measured=None),
    dict(id='I-BLOCKS', choice='the block decomposition',
         cls='FORCED', fibre=1, fibre_computed=1, scope=None,
         why="Gamma-prep's B2 atoms are the holdings-profile blocks of "
             "R-SIG, and the census reproduces exactly; the blocks are "
             "read, not chosen.",
         measured=None),
]
INVENTORY[0]['measured'] = (f"of the two rungs this unit rebuilds (REC "
                            f"and MENU), {_rung_fiber} both descend and "
                            f"are non-flat; D74's committed ladder "
                            f"gives menu-descent only at SEQ, REC and "
                            f"MENU, and flatness at SEQ and REC")
INVENTORY[1]['measured'] = (f"carrier {len(CARRIER)} histories, "
                            f"{len(set(A_MENU.values()))} classes; the "
                            f"deeper arena is not built")
INVENTORY[2]['measured'] = (f"Gamma-prep's committed grain counts, read "
                            f"by path: primary "
                            f"{pv(GPR, 'grain_primary_classes')} "
                            f"classes, control "
                            f"{pv(GPR, 'grain_control_classes')} "
                            f"classes -- {_grain_fiber} distinct grains")
INVENTORY[3]['measured'] = (f"the horizon potential is class-"
                            f"multi-valued on the carrier at "
                            f"{[(r, b) for r, b, t in _Gmulti['MENU'] if b]}, "
                            f"so the convention is visible in the law")
INVENTORY[4]['measured'] = (f"depth cuts: "
                            f"{sum(1 for r in CK if not r['interpolates'])} "
                            f"of {len(CK)} triples do NOT divide by the "
                            f"process's own conditional; renewal cuts: "
                            f"DIVISIBLE is forced by column-constancy")
INVENTORY[5]['measured'] = (f"three measured readings of the same leg "
                            f"ensembles: step-normalised {frl(LAW1)}, "
                            f"raw-product {frl(RAW1)}, count "
                            f"{frl(CNT1)} -- {_readout_fiber} distinct "
                            f"laws; and at the carrier level the count "
                            f"construction is not a law at all "
                            f"({_lit_bad} of {_lit_cols} columns)")
INVENTORY[6]['measured'] = ("; ".join(f"{s}: "
                                      + ", ".join(str(r['negatives'])
                                                  for r in PADFIBER
                                                  if r['style'] == s
                                                  and r['invertible'])
                                      + (" (speaks)" if s in _speak
                                         else " SILENT")
                                      for s in ('identity', 'cyclic',
                                                'uniform', 'marginal')))
INVENTORY[7]['measured'] = (f"unpruned agreement on {len(GATE_BASES)} "
                            f"of {len(R2BASES)} declared bases: "
                            f"{len(LEGSU)} legs, identical to the "
                            f"pruned set at both weights")
INVENTORY[8]['measured'] = (f"{len(R1BASES)} renewal-1 bases, all of "
                            f"pattern (p,p,r); {len(R2BASES)} "
                            f"renewal-2 bases")
INVENTORY[9]['measured'] = (f"R-SIG {len(RSIG)}, R-MENU {len(RMENU)}, "
                            f"profiles {ctr(_prof)}; on the carrier the "
                            f"blocks are pure on {_pure} of {_nclass} "
                            f"classes that meet R-SIG")

for r in INVENTORY:
    emit(f"  {r['id']:12s} {r['cls']:16s} fiber {r['fibre']} "
         f"(computed {r['fibre_computed']})  {r['choice']}")
    emit(f"      measured: {r['measured']}")
    if r['scope']:
        emit(f"      SCOPE: {r['scope']}")
_free = [r for r in INVENTORY if r['cls'] == 'GENUINELY-FREE']
_forced = [r for r in INVENTORY if r['cls'] == 'FORCED']
_stab_i = [r for r in INVENTORY if r['cls'] == 'STABILIZER-FIXED']


def inventory_ok(inv):
    if len(inv) != 10:
        return False
    if not any(r['id'] == 'I-READOUT' and r['fibre_computed'] is not None
               and r['fibre_computed'] >= 3 for r in inv):
        return False
    mot = sum(1 for r in inv if r['cls'] in ('FORCED',
                                             'STABILIZER-FIXED'))
    if mot == 0:
        return False
    for r in inv:
        fc = r['fibre_computed']
        if fc is None:
            if r['scope'] is None:
                return False
            continue
        if r['fibre'] != fc:
            return False
        if fc == 1 and r['cls'] not in ('FORCED', 'STABILIZER-FIXED'):
            return False
        if fc >= 2 and r['cls'] != 'GENUINELY-FREE':
            return False
    return True


_INV_MUT = [dict(r) for r in INVENTORY]
for r in _INV_MUT:
    if r['id'] == 'I-GRAIN':
        r['cls'] = 'FORCED'
# THE PER-SEGMENT MOTIVATION MAP (effectus F-7): motivation is not a
# property of the inventory, it is a property of each verdict segment.
SEGDEP = [('CARRIER', ['I-CARRIER', 'I-CAP', 'I-GRAIN', 'I-BLOCKS']),
          ('CENSUS-SHADOW', ['I-RENEWAL', 'I-PRUNE', 'I-CUTS']),
          ('LAW-VALUE', ['I-READOUT', 'I-RENEWAL', 'I-PRUNE']),
          ('HOLONOMY', ['I-CARRIER', 'I-CAP', 'I-HORIZON']),
          ('SCREEN', ['I-PADDING', 'I-CUTS']),
          ('INTERPOLANT', ['I-PADDING', 'I-CUTS', 'I-READOUT']),
          ('44+44', ['I-CARRIER', 'I-CAP'])]
_cls = {r['id']: r['cls'] for r in INVENTORY}
SEGMOT = []
for seg, items in SEGDEP:
    freeones = [i for i in items if _cls[i] == 'GENUINELY-FREE']
    SEGMOT.append(dict(segment=seg, items=items, free=freeones,
                       motivated=len(freeones) == 0))
emit("  PER-SEGMENT MOTIVATION (the quantity the RSQ standard actually "
     "asks for):")
for r in SEGMOT:
    emit(f"    {r['segment']:16s} {'MOTIVATED' if r['motivated'] else 'FREE-CHOICE-CARRIED'}"
         f"  descends from {r['items']}; free among them {r['free']}")
gate('T8-ATOMS', 'MUST',
     "THE MOTIVATION INVENTORY, at the RSQ standard, WITH THE "
     'CLASSIFICATION GATED: ten construction choices, each classed '
     'with an exact fiber; every fiber that is machine-computable '
     'agrees with the declared one and with the declared class; the '
     'one fiber that is not computable here is stamped as declared; '
     'the I-READOUT item is present with a COMPUTED fiber of at least '
     'three; and the inventory is non-empty on the motivated side',
     inventory_ok(INVENTORY),
     f"{len(INVENTORY)} items: FORCED {len(_forced)} "
     f"{[r['id'] for r in _forced]}, STABILIZER-FIXED {len(_stab_i)} "
     f"{[r['id'] for r in _stab_i]}, GENUINELY-FREE {len(_free)} "
     f"{[r['id'] for r in _free]}; MOTIVATED = "
     f"{len(_forced) + len(_stab_i)} of {len(INVENTORY)}; computed "
     f"fibers {[(r['id'], r['fibre_computed']) for r in INVENTORY]}; "
     f"per-segment motivation "
     f"{[(r['segment'], r['motivated']) for r in SEGMOT]}",
     falsifiers=['MUT-INVENTORY-RECLASS'])
mutant('MUT-INVENTORY-RECLASS', 'T8-ATOMS',
       'a GENUINELY-FREE choice (I-GRAIN) relabelled FORCED -- the '
       'injection that moved a delivered claim and survived the '
       'previous instrument at exit 0',
       inventory_ok(INVENTORY), inventory_ok(_INV_MUT),
       f"I-GRAIN's fiber is machine-computed at {_grain_fiber} from "
       f"Gamma-prep's own committed grain counts, so relabelling it "
       f"FORCED contradicts the computed fiber and the gate's own "
       f"predicate turns false")

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


def carrier_stats(V):
    menus = defaultdict(set)
    for h in CARRIER:
        menus[V[h]].add(tuple(sorted((evsk(e), str(q))
                                     for e, q in CACHE[h])))
    desc = sum(1 for v in menus.values() if len(v) == 1)
    ex = [(V[c[0] + (c[2], c[1])], V[c[0] + (c[1], c[2])], c[3])
          for c in CLOSED]
    n_, rk_, ob_, hol_ = holonomy_of([e for e in ex if e[0] != e[1]])
    sl = Counter(x for u, v, x in ex if u == v and x != 1)
    ps_, grk_ = group_of(list(sl.elements())
                         + [k for k in hol_ for _ in range(hol_[k])
                            if k != 1])
    return dict(descends=desc, classes=len(menus),
                closes=sum(1 for u, v, x in ex if u == v),
                obstruction=ob_, selfloops=sum(sl.values()),
                primes=ps_, rank=grk_)


_scr = carrier_stats(SCR)
_car = carrier_stats(A_MENU)
emit("  THE GROUP IS NOT A DISCRIMINATING STATISTIC AT THE q READING, "
     "and this unit says so before it uses it: every closed square's "
     "ratio lies in the measured value set, so the q-holonomy group of "
     "ANY quotient of this family is a subgroup of D74's <2,3>.  What "
     "discriminates a scrambled carrier is DESCENT and the ladder row. "
     " The k-reading discriminates too, but as a DESCENT DETECTOR: the "
     "operator panel measured it taking exactly two values across ten "
     "carriers -- rank 2 wherever the horizon potential descends, "
     "rank 3 wherever it does not -- so it is not a carrier "
     "fingerprint either.")


def scramble_ok(scr, car):
    return (scr['descends'] < scr['classes']
            and (scr['obstruction'] != car['obstruction']
                 or scr['selfloops'] != car['selfloops']
                 or scr['closes'] != car['closes']))


gate('C-SCRAMBLE', 'MUST',
     'THE SCRAMBLED-QUOTIENT CONTROL: a deterministic congruential '
     "shuffle of the carrier's own class sizes destroys descent and "
     "moves D74's measured ladder row -- the holonomy gate is "
     'therefore measuring the quotient and not the pipeline',
     scramble_ok(_scr, _car),
     f"menu descends on {_scr['descends']} of {_scr['classes']} "
     f"scrambled classes (carrier: {_car['descends']} of "
     f"{_car['classes']}); scrambled squares closing {_scr['closes']} "
     f"(carrier: {_car['closes']}), obstruction {_scr['obstruction']} "
     f"(carrier: {_car['obstruction']}), non-unit self-loops "
     f"{_scr['selfloops']} (carrier: {_car['selfloops']}); scrambled "
     f"group primes {_scr['primes']} rank {_scr['rank']} -- a subgroup "
     f"of <2,3> by the value-set theorem above, hence NOT the "
     f"discriminating statistic (seed 20260809, congruential shuffle "
     f"x <- (1103515245 x + 12345) mod 2^31)",
     falsifiers=['MUT-SCRAMBLE-EQ'])
mutant('MUT-SCRAMBLE-EQ', 'C-SCRAMBLE',
       'the scramble replaced by the carrier itself -- the control run '
       'against its own object',
       scramble_ok(_scr, _car), scramble_ok(_car, _car),
       f"the carrier returns obstruction {_car['obstruction']} and "
       f"{_car['closes']} closing squares exactly, so the control "
       f"shows no contrast and the gate's own predicate turns false")
_scr_rows = gmulti_rows(SCR)
mutant('MUT-QUOTIENT-SCRAMBLE', 'G-KERNEL-DOES-NOT-DESCEND',
       'the mandatory negative control replaced by a size-matched '
       'scramble of the carrier, and the descent census recomputed on '
       'it',
       any(b > 0 for r, b, t in _Gmulti['MENU'])
       and all(b == 0 for r, b, t in _Gmulti['REC']),
       any(b > 0 for r, b, t in _Gmulti['MENU'])
       and all(b == 0 for r, b, t in _scr_rows),
       f"the scramble carries a class-multi-valued horizon potential at "
       f"{[(r, b) for r, b, t in _scr_rows if b]}, so the gate's own "
       f"control conjunct turns false on it; and it loses menu descent "
       f"({_scr['descends']} of {_scr['classes']}) and moves the "
       f"ladder row to obstruction {_scr['obstruction']} against the "
       f"carrier's {_car['obstruction']}")

# ======================================================================
# THE VERDICT
# ======================================================================
sec("THE VERDICT")
_all_must = [g for g in GATES if g['kind'] == 'MUST']
_fail_must = [g for g in _all_must if not g['passed']]

CONSTRUCTED = (_cs_bad == 0 and _neg == 0 and len(ANCHOR_FAIL) == 0
               and len(set(A_MENU.values())) == 113 and _flow_bad == 0)
HEAD = ('GMAIN-CONSTRUCTED' if CONSTRUCTED
        else 'GMAIN-BLOCKED-AT-THE-CARRIER')
SEG_CARRIER = (f"CARRIER=D74-MENU-{len(set(A_MENU.values()))}-CLASSES-AT-"
               f"(A,B)-D<={CAP}|CUTS={CAP + 1}|"
               f"DIMS={'x'.join(str(x) for x in DIMS_M)}|"
               f"PAIRS={len(GAM_M)}|COLUMN-STOCHASTIC-EXACT-{_cols_tot}-"
               f"OF-{_cols_tot}-COLUMNS|"
               f"FLOW-IDENTITY-w(h)k_{{{CAP}-|h|}}=w(h+e)-{_flow_ok}-OF-"
               f"{_flow_ok}|"
               f"B2-BLOCKS-PURE-ON-{_pure}-OF-"
               f"{len(set(A_MENU.values()))}-CARRIER-CLASSES|"
               f"PROVENANCE={len(SOURCES)}-SHA-PINNED-SOURCES-PLUS-THE-"
               f"SELF-PAPER-BYTE-ANCHORED")
SEG_REQ = (f"REQUIREMENTS-CENSUS-SHADOW=REPRODUCED-AT-THE-COUNTING-"
           f"MEASURE-THAT-DEFINED-IT-{frl(CNT1)}-AND-{frl(CNT2)}-"
           f"EXTERNAL-CONTROL-NEVER-A-TARGET|"
           f"LAW-VALUE-AT-THE-STEP-NORMALISED-PRIMARY-READOUT="
           f"{frl(LAW1)}-AT-BOTH-LEGS-LEG-INDEPENDENT-AND-LEFT-RIGHT-"
           f"ASYMMETRIC|"
           f"RAW-PRODUCT-READOUT={frl(RAW1)}-AT-BOTH-LEGS|"
           f"READOUT-FIBER>={_readout_fiber}-H4-CHAIN-READING-EXCLUDED-"
           f"BY-CAP|"
           f"HOLONOMY={T2_VERDICT}:"
           f"D74-{{{','.join(str(x) for x in _q23['primes'])}}}-RANK-"
           f"{_q23['rank']}-REPRODUCED-DIGIT-FOR-DIGIT-"
           f"{_q23['closes']}-CLOSES-{_q23['obstruction']}-OBSTRUCTION-"
           f"{_q23['selfloops']}-SELFLOOPS-{_q23['cycle_rank']}-CYCLE-"
           f"RANK,"
           f"DEVIATION-IDENTITY-{len(DEVROWS) - _id_viol}-OF-"
           f"{len(DEVROWS)},"
           f"UNLOCATED-DEVIATIONS-{_loc_bad},"
           f"K-PRIMES-{{{','.join(str(p) for p in _k['primes'])}}}-RANK-"
           f"{_k['rank']}-ON-A-NON-DESCENDING-CARRIER,"
           f"GAMMA-PRIMES-{{{','.join(str(p) for p in _gm['primes'])}}}-"
           f"RANK-{_gm['rank']}-AT-THE-OCCUPANCY-CONSTRUCTION,"
           f"REC-FLAT-AT-{sum(1 for x in (_rq['obstruction'], _rk['obstruction'], _rg['nonunit']) if x == 0)}"
           f"-OF-3-READINGS-AT-THE-DECLARED-READOUT|"
           f"SCREEN={'-'.join(f'{k}:{v}' for k, v in sorted(_tally.items()))}"
           f"-THE-ONE-PASS-DEGENERATE-J/8-COLUMN-CONSTANT|"
           f"KERNEL=INDUCED;CONSTANT-ACROSS-THE-{len(CELLS)}-CENSUSED-"
           f"CELLS-AT-n={CELLS[0]['renewal_count']};"
           f"{'/'.join(x.upper() for x in _moving)}-CONFOUNDED|"
           f"MOVER=BLOCKED-AT-REFERENT-{_shared}-DECLARED-MAPS-MEASURED-"
           f"OVER-{len(_BODIES)}-PINNED-SOURCES|"
           f"INTERPOLANT=NON-MARKOV-AT-{sum(1 for r in CK if not r['interpolates'])}"
           f"-OF-{len(CK)}-DEPTH-TRIPLES-AT-THE-DECLARED-READOUT-REC-"
           f"EXACTLY-LUMPABLE|"
           f"EQ22=NO-FORM-INTERPOLANT-AT-{len(EQ22)}-OF-{len(EQ22)}-"
           f"INVERTIBLE-TRIPLES-NEGATIVES-"
           f"{'/'.join(str(r['negatives']) for r in EQ22)}-AT-"
           f"{len(_speak)}-OF-4-COMPLETIONS-THAT-SPEAK|"
           f"44+44={len(_curv)}-CLOSE-{len(_desc)}-NOT-A-LOOP")
SEG_MOT = (f"MOTIVATION-FORCED-{len(_forced)}|STABILIZER-FIXED-"
           f"{len(_stab_i)}|GENUINELY-FREE-{len(_free)}|"
           f"I-READOUT=GENUINELY-FREE-FIBER-{_readout_fiber}-MEASURED-"
           f"THE-THIRD-LAW-{frl(LAW1)}|"
           f"I-CARRIER=FORCED-AMONG-D74-RUNGS-FREE-IN-THE-LATTICE|"
           f"I-PADDING=FIBER-{_padding_fiber}-COMPLETIONS-THAT-SPEAK-OF-"
           f"4-TESTED|"
           f"PER-SEGMENT-MOTIVATED-"
           f"{sum(1 for r in SEGMOT if r['motivated'])}-OF-{len(SEGMOT)}|"
           f"NON-EMPTY-{len(_forced) + len(_stab_i) > 0}")
SEG_SCOPE = (f"SCOPE-CAP=(A,B)-D<={CAP}-CARRIER-AND-D<={CAP_ANCHOR}-"
             f"ANCHOR|GRAIN={len(set(A_MENU.values()))}-CLASS-"
             f"EVENTxWEIGHT|HORIZON=H{CAP}|"
             f"READOUT=STEP-NORMALISED-PRIMARY-RAW-PRODUCT-AND-COUNT-"
             f"MEASURED|"
             f"PADDING={len(_speak)}-SPEAKING-OF-4-DECLARED|"
             f"LEGS=RENEWAL-CUT-ENSEMBLES-AT-DEPTHS-"
             f"{min(_leg_depths)}..{max(_leg_depths)}|"
             f"CENSUS-SHADOW=EXTERNAL-CONTROL-NEVER-TARGET|"
             f"B2-IMPORT=CENSUS-ONLY-ATOM-CLAIM-NOT-IMPORTED-"
             f"{len(IMPORT_SCOPE['named_exclusions'])}-EXCLUSIONS-NAMED|"
             f"MONOTONICITY={_MONO_CENSUSED}-OF-{_MONO_TOTAL}-"
             f"TRANSITIONS-CENSUSED|"
             f"NO-CURVATURE=>QUANTUM-CLAIM-{len(_claims)}-MEASURED|"
             f"NO-INDIVISIBILITY-CLAIM-AT-RENEWAL-GRAIN")

# ----------------------------------------------------------------------
# THE SETTLEMENT.  Four links, each computed, each two-way flippable by
# targeted input, evaluated at ONE arena (the declared primary readout).
# ----------------------------------------------------------------------
LINKS = ['constructed', 'targets', 'holonomy', 'motivation']
SETTLEMENT = dict(
    constructed=CONSTRUCTED,
    targets=_targets_are_law_values,
    holonomy=T2_OK,
    motivation=(len(_forced) + len(_stab_i) > 0
                and _readout_fiber >= 3 and inventory_ok(INVENTORY)),
)


def settlement_segment(payload):
    """A PURE function of a settlement payload.  It is exercised below
    on the measured payload, on an all-true SYNTHETIC payload, and on
    every one-link flip of both -- so the instrument is shown able to
    emit SETTLED, and every link is shown two-way (adjudication
    R-GM-8, closing the instrument round's INJ12)."""
    failed = [k for k in LINKS if not payload[k]]
    if not failed:
        return 'SETTLEMENT=SETTLED'
    return ('SETTLEMENT=PARTIAL-FAILED-LINK-'
            + '-AND-'.join(k.upper() for k in failed))


def four_of_four(payload):
    return all(payload[k] for k in LINKS)


def three_of_four(payload):
    return sum(1 for k in LINKS if payload[k]) >= 3


SYNTHETIC = {k: True for k in LINKS}
BATTERY = [('MEASURED', dict(SETTLEMENT)),
           ('SYNTHETIC-ALL-TRUE', dict(SYNTHETIC))]
for _lk in LINKS:
    for _bbase, _bnm in ((SETTLEMENT, 'MEASURED'),
                         (SYNTHETIC, 'SYNTHETIC')):
        _bp = dict(_bbase)
        _bp[_lk] = not _bp[_lk]
        BATTERY.append((f"{_bnm}-FLIP-{_lk.upper()}", _bp))
emit("  THE SETTLEMENT BATTERY -- the emitted segment as a function of "
     "the payload, on the measured payload, on an all-true synthetic "
     "payload, and on every one-link flip of each:")
for _nm, _p in BATTERY:
    emit(f"    {_nm:28s} {settlement_segment(_p)}")
_ALLFALSE = {k: False for k in LINKS}


def two_way_census(fn):
    """Every one of the four links must move the emitted segment in
    BOTH directions: true->false out of the all-true payload, and
    false->true out of the all-false one."""
    seen = {fn(p) for _n, p in BATTERY}
    both = all(fn({**SYNTHETIC, k: False}) != fn(SYNTHETIC)
               and fn({**_ALLFALSE, k: True}) != fn(_ALLFALSE)
               for k in LINKS)
    return seen, both, (fn(SYNTHETIC) in seen and fn(SYNTHETIC)
                        == settlement_segment(SYNTHETIC))


def oneway_segment(payload):
    """The decorative-conjunct shape: a settlement whose emitted
    segment depends on the first link alone."""
    return ('SETTLEMENT=SETTLED' if payload[LINKS[0]]
            else 'SETTLEMENT=PARTIAL-FAILED-LINK-' + LINKS[0].upper())


_seen, _two_way, _emits_settled = two_way_census(settlement_segment)
_seen1, _two_way1, _emits1 = two_way_census(oneway_segment)
gate('G-SETTLEMENT-TWO-WAY', 'MUST',
     'R-GM-8: the instrument is shown ABLE TO EMIT A SETTLED VERDICT.  '
     'The settlement segment is a pure function of its payload; it is '
     'evaluated on the measured payload, on an all-true synthetic '
     'payload and on every one-link flip of both; the SETTLED form is '
     'emitted on the synthetic payload; and every one of the four '
     'links moves the emitted segment in BOTH directions.  The '
     'previous instrument could not emit SETTLED without failing three '
     'of its own gates',
     _emits_settled and _two_way and len(_seen) > 2,
     f"battery {len(BATTERY)} payloads, {len(_seen)} distinct emitted "
     f"segments; SETTLED emitted on a synthetic payload "
     f"{_emits_settled}; every link two-way {_two_way}",
     falsifiers=['MUT-SETTLEMENT-ONEWAY'])
mutant('MUT-SETTLEMENT-ONEWAY', 'G-SETTLEMENT-TWO-WAY',
       'a settlement whose emitted segment depends on ONE link only -- '
       'the shape in which three of the four conjuncts are decorative',
       _emits_settled and _two_way and len(_seen) > 2,
       _emits1 and _two_way1 and len(_seen1) > 2,
       f"the one-link settlement emits {len(_seen1)} distinct segments "
       f"over the same battery and its two-way census is {_two_way1}, "
       f"so the gate's own predicate turns false on it")

SETTLED = four_of_four(SETTLEMENT)
_failed_links = [k for k in LINKS if not SETTLEMENT[k]]
_three_reasons = dict(
    census_statistics_at_birth=all(r['ok'] for r in VB_ROWS
                                   if r['id'] in ('V-TARGETS',
                                                  'V-CENSUS-BIRTH')),
    gamma_free_and_off_carrier=gamma_free(_hits, _leg_depths, CAP),
    count_readout_breaks_the_control=_cc_ok)
SEG_SETTLE = (
    settlement_segment(SETTLEMENT)
    + f"|CONSTRUCTED=TRUE-<{_cols_tot}-OF-{_cols_tot}-COLUMNS-EXACT;"
      f"FLOW-IDENTITY-{_flow_ok}-OF-{_flow_ok};REBUILT-ON-BOTH-"
      f"QUOTIENTS>"
    + f"|TARGETS={str(SETTLEMENT['targets']).upper()}-<CENSUS-"
      f"STATISTICS-AT-BIRTH-{str(_three_reasons['census_statistics_at_birth']).upper()};"
      f"THE-TARGET-TEST-IS-GAMMA-FREE-AND-OFF-CARRIER-"
      f"{str(_three_reasons['gamma_free_and_off_carrier']).upper()}-"
      f"TOKEN-SCAN-{len(_hits)}-HITS-AT-DEPTHS-{min(_leg_depths)}.."
      f"{max(_leg_depths)};THE-COUNT-READOUT-BREAKS-THE-MANDATORY-"
      f"NEGATIVE-CONTROL-"
      f"{str(_three_reasons['count_readout_breaks_the_control']).upper()}"
      f"-REC-HOLONOMY-RANK-{CNT_HOL_R['rank']}-CK-{_cnt_ck_r_fail}-OF-"
      f"{len(CNT_CK_R)}-FAILS-{_lit_cols - _lit_bad}-OF-{_lit_cols}-"
      f"COLUMNS-STOCHASTIC>"
    + f"|HOLONOMY={str(SETTLEMENT['holonomy']).upper()}-UNDER-"
      f"{T2_VERDICT}-<D74-RUNG-DIGIT-FOR-DIGIT;DEVIATION-IDENTITY-"
      f"{len(DEVROWS) - _id_viol}-OF-{len(DEVROWS)};UNLOCATED-"
      f"{_loc_bad};REC-FLAT>"
    + f"|MOTIVATION={str(SETTLEMENT['motivation']).upper()}-<READOUT-"
      f"FIBER-{_readout_fiber};THE-THIRD-STEP-NORMALISED-LAW-"
      f"{frl(LAW1)};PER-SEGMENT-MAP-"
      f"{sum(1 for r in SEGMOT if r['motivated'])}-OF-{len(SEGMOT)}-"
      f"MOTIVATED>")

_SETTLE_REBUILT = dict(
    constructed=(HEAD == 'GMAIN-CONSTRUCTED'),
    targets=(T1_VERDICT == 'TARGETS-ARE-VALUES-OF-THE-LAW'),
    holonomy=(T2_VERDICT == 'REPRODUCED-AND-LOCATED'),
    motivation=(inventory_ok(INVENTORY) and _readout_fiber >= 3
                and len(_forced) + len(_stab_i) > 0))
_SETTLE_DESYNC = dict(_SETTLE_REBUILT)
_SETTLE_DESYNC['holonomy'] = not _SETTLE_DESYNC['holonomy']


def settle_gate(payload, rebuilt, battery, rule):
    """The settlement gate compares the payload against a dict rebuilt
    from the INDEPENDENT verdict strings of T1, T2 and the head, and
    requires THE RULE IN USE to agree with the conjunction on EVERY
    declared battery payload -- not merely on the delivered one, which
    is what made the previous falsifier contingent on the verdict
    coming out PARTIAL."""
    return (payload == rebuilt
            and all(rule(p) == all(p[k] for k in LINKS)
                    for _n, p in battery))


gate('G-SETTLEMENT', 'MUST',
     'THE SETTLEMENT CONDITION, evaluated link by link at ONE arena '
     '(the declared primary readout) and not summarised: the payload '
     'is compared against a dict rebuilt from the INDEPENDENT verdict '
     'strings of the construction head, of test 1 and of test 2, and '
     'the emitted segment names every link that failed',
     settle_gate(SETTLEMENT, _SETTLE_REBUILT, BATTERY, four_of_four),
     "; ".join(f"{k} = {SETTLEMENT[k]}" for k in LINKS)
     + f"; settled {SETTLED}; failed links {_failed_links}; rebuilt "
       f"from the independent verdict strings "
       f"{[_SETTLE_REBUILT[k] for k in LINKS]}",
     falsifiers=['MUT-SETTLEMENT-DESYNC', 'MUT-SETTLEMENT-LAX'])
mutant('MUT-SETTLEMENT-DESYNC', 'G-SETTLEMENT',
       'the settlement payload desynchronised from the verdict strings '
       'it is supposed to summarise (one link flipped)',
       settle_gate(SETTLEMENT, _SETTLE_REBUILT, BATTERY,
                   four_of_four),
       settle_gate(SETTLEMENT, _SETTLE_DESYNC, BATTERY, four_of_four),
       "a payload that disagrees with the T1/T2/head verdict strings "
       "fails the comparison, so the gate's own predicate turns false")
mutant('MUT-SETTLEMENT-LAX', 'G-SETTLEMENT',
       'the four-of-four rule replaced by a three-of-four rule, '
       'evaluated over the WHOLE DECLARED BATTERY rather than over the '
       'delivered payload alone -- so this falsifier dies whatever the '
       'delivered verdict turns out to be (the INJ12 repair)',
       settle_gate(SETTLEMENT, _SETTLE_REBUILT, BATTERY,
                   four_of_four),
       settle_gate(SETTLEMENT, _SETTLE_REBUILT, BATTERY,
                   three_of_four),
       f"the battery contains one-link-flip payloads on which the "
       f"three-of-four rule reports settled where the four-of-four "
       f"rule reports partial, so the gate's own rule-agreement "
       f"conjunct turns false -- INDEPENDENTLY of what the delivered "
       f"payload is")

VERDICT = f"{HEAD}-<{SEG_CARRIER} -- {SEG_REQ} -- {SEG_MOT} -- " \
          f"{SEG_SCOPE} -- {SEG_SETTLE}>"

# ----------------------------------------------------------------------
# THE VERDICT COMPARATOR (adjudication R-GM-5; RUNBOOK 14, v14 #82).
# The previous delivery's comparator was the same concatenation of the
# same six variables written twice -- an identity.  The engraved
# standard is that a comparator shares NOTHING with its builder:
# neither code, nor inputs, nor typed literals.  This one therefore
#   * takes as its ONLY inputs the emitted string and a SERIALISED
#     receipt record (raw JSON text), which it re-parses itself;
#   * does not concatenate anything: it is a PARSER, walking the
#     emitted string and matching the receipt's rows against it;
#   * types no delimiter, no segment name and no measured value: the
#     head, the segments, the segment-to-key map and the values all
#     come out of the parsed rows, and the connective tissue is
#     CHARACTERISED (equal between segments, non-empty, carrying no
#     alphanumeric) rather than quoted.
# ----------------------------------------------------------------------
VERDICT_MEASURED = {
    'menu_classes': len(set(A_MENU.values())),
    'rec_classes': len(set(A_REC.values())),
    'columns': _cols_tot,
    'sources': len(SOURCES),
    'block_pure': _pure,
    'flow': _flow_ok,
    'readout_fiber': _readout_fiber,
    'law_first': str(LAW1[0]),
    'law_mid': str(LAW1[1]),
    'shadow_first': str(CNT1[0]),
    'shadow2_first': str(CNT2[0]),
    'identity_ok': len(DEVROWS) - _id_viol,
    'unlocated': _loc_bad,
    'q_closes': _q23['closes'],
    'q_cycle_rank': _q23['cycle_rank'],
    'k_rank': _k['rank'],
    'gamma_rank': _gm['rank'],
    'ck_fail': sum(1 for r in CK if not r['interpolates']),
    'ck_total': len(CK),
    'curvature': len(_curv),
    'descent': len(_desc),
    'speaking': len(_speak),
    'forced': len(_forced),
    'stabilizer': len(_stab_i),
    'free': len(_free),
    'segmot': sum(1 for r in SEGMOT if r['motivated']),
    'mono_censused': _MONO_CENSUSED,
    'mono_total': _MONO_TOTAL,
    'claims': len(_claims),
    'declared_maps': _shared,
    'rec_count_rank': CNT_HOL_R['rank'],
    'count_stochastic': _lit_cols - _lit_bad,
}
VERDICT_KEYMAP = {
    '0': ['menu_classes', 'columns', 'sources', 'block_pure', 'flow'],
    '1': ['readout_fiber', 'law_first', 'law_mid', 'shadow_first',
          'shadow2_first', 'identity_ok', 'unlocated', 'q_closes',
          'q_cycle_rank', 'k_rank',
          'gamma_rank', 'ck_fail', 'ck_total', 'curvature', 'descent',
          'speaking', 'declared_maps'],
    '2': ['forced', 'stabilizer', 'free', 'readout_fiber', 'law_first',
          'segmot'],
    '3': ['mono_censused', 'mono_total', 'claims'],
    '4': ['columns', 'flow', 'identity_ok', 'unlocated', 'law_first',
          'rec_count_rank', 'count_stochastic'],
}
_VSEGS = [SEG_CARRIER, SEG_REQ, SEG_MOT, SEG_SCOPE, SEG_SETTLE]
VERDICT_KEYCOUNTS = {i: {k: _VSEGS[int(i)].count(str(VERDICT_MEASURED[k]))
                         for k in ks}
                     for i, ks in VERDICT_KEYMAP.items()}
VERDICT_RECORD = dict(head=HEAD,
                      segments=_VSEGS,
                      measured=VERDICT_MEASURED,
                      keymap=VERDICT_KEYMAP,
                      keycounts=VERDICT_KEYCOUNTS)
VERDICT_RAW = json.dumps(VERDICT_RECORD, sort_keys=True, default=str)


def verdict_audit(vtext, raw):
    """The comparator.  Returns a dict of measured booleans."""
    try:
        rows = json.loads(raw)
    except Exception:
        return dict(parsed=False)
    head = rows['head']
    segs = rows['segments']
    if not vtext.startswith(head):
        return dict(parsed=True, head=False)
    pos = len(head)
    spans = []
    for sg in segs:
        i = vtext.find(sg, pos)
        if i < 0:
            return dict(parsed=True, head=True, located=False)
        spans.append((i, i + len(sg)))
        pos = i + len(sg)
    lead = vtext[len(head):spans[0][0]]
    inner = [vtext[spans[i - 1][1]:spans[i][0]]
             for i in range(1, len(spans))]
    tail = vtext[spans[-1][1]:]

    def structural(x):
        return len(x) > 0 and not any(ch.isalnum() for ch in x)

    covered = (len(head) + sum(len(s) for s in segs) + len(lead)
               + sum(len(x) for x in inner) + len(tail))
    content = True
    misses = []
    for idx, keys in rows['keymap'].items():
        seg = segs[int(idx)]
        for k in keys:
            val = str(rows['measured'][k])
            if val not in seg:
                content = False
                misses.append((idx, k, 'absent'))
            elif seg.count(val) != rows['keycounts'][idx][k]:
                content = False
                misses.append((idx, k, 'count'))
    return dict(parsed=True, head=True, located=True,
                lead=structural(lead), tail=structural(tail),
                inner_uniform=len(set(inner)) == 1,
                inner_structural=all(structural(x) for x in inner),
                covers=covered == len(vtext),
                content=content, misses=misses)


def audit_ok(a):
    return (a.get('parsed') and a.get('head') and a.get('located')
            and a.get('lead') and a.get('tail')
            and a.get('inner_uniform') and a.get('inner_structural')
            and a.get('covers') and a.get('content'))


_AUD = verdict_audit(VERDICT, VERDICT_RAW)
_desync = json.loads(VERDICT_RAW)
_desync['measured']['identity_ok'] = VERDICT_MEASURED['identity_ok'] + 1
_DESYNC_RAW = json.dumps(_desync, sort_keys=True, default=str)
gate('G-VERDICT-EQUALITY', 'MUST',
     'THE COMPLETE EMITTED VERDICT is audited against a SERIALISED '
     'receipt record by a comparator that shares no code, no inputs '
     'and no typed literals with the builder: it re-parses the raw '
     'rows, locates the head and the five segments by search, '
     'CHARACTERISES the connective tissue instead of quoting it '
     '(equal between segments, non-empty, alphanumeric-free), proves '
     'the spans cover the string exactly, and checks every declared '
     'measured value against the segment it belongs to.  Containment, '
     'prefix and substring checks are not verdict gates (#10); a '
     'comparator that agrees with its builder by construction is not '
     'one either (#82)',
     audit_ok(_AUD),
     f"audit {_AUD}; verdict {len(VERDICT)} chars over "
     f"{len(VERDICT_RECORD['segments'])} segments; "
     f"{sum(len(v) for v in VERDICT_KEYMAP.values())} measured values "
     f"checked against the segments that carry them",
     falsifiers=['MUT-VERDICT-APPEND', 'MUT-VERDICT-SWAP',
                 'MUT-VERDICT-TRUNC', 'MUT-VERDICT-DROP',
                 'MUT-VERDICT-RETYPE', 'MUT-VERDICT-DESYNC'])
for _nm, _mv, _mr, _what in (
        ('MUT-VERDICT-APPEND', VERDICT + ' (ok)', VERDICT_RAW,
         'text appended after the closing delimiter'),
        ('MUT-VERDICT-SWAP',
         VERDICT.replace(HEAD, ('GMAIN-BLOCKED-AT-THE-CARRIER'
                                if HEAD == 'GMAIN-CONSTRUCTED'
                                else 'GMAIN-CONSTRUCTED'), 1),
         VERDICT_RAW, 'the head swapped for the other class'),
        ('MUT-VERDICT-TRUNC', VERDICT[:-1], VERDICT_RAW,
         'the closing delimiter truncated'),
        ('MUT-VERDICT-DROP', VERDICT.replace(" -- " + SEG_MOT, "", 1),
         VERDICT_RAW, 'a whole segment dropped'),
        ('MUT-VERDICT-RETYPE',
         VERDICT.replace(f"RANK-{_gm['rank']}",
                         "RANK-'" + str(_gm['rank']) + "'", 1),
         VERDICT_RAW, 'a measured rank retyped as a quoted string'),
        ('MUT-VERDICT-DESYNC', VERDICT, _DESYNC_RAW,
         'the receipt record desynchronised from the emitted string by '
         'one measured value')):
    mutant(_nm, 'G-VERDICT-EQUALITY', _what, audit_ok(_AUD),
           audit_ok(verdict_audit(_mv, _mr)),
           f"the audit of the corrupted object returns "
           f"{ {k: v for k, v in verdict_audit(_mv, _mr).items() if v is not True} }, "
           f"so the comparator's own predicate turns false")

emit("")
emit("  " + VERDICT)
emit("")
emit(f"  THE SETTLEMENT CONDITION (the pin, verbatim): the "
     f"QFT-needs-gravity stake is settled ONLY by: constructed AND "
     f"targets hit AND holonomy consistent AND motivation non-empty -- "
     f"anything less is partial and says which link failed.")
emit(f"  THE CORRECTED SETTLEMENT (the adjudication, section 1), "
     f"evaluated at ONE arena -- the declared primary readout:")
emit(f"    constructed : {SETTLEMENT['constructed']} -- Gamma exists, "
     f"exact, column-stochastic on {_cols_tot} of {_cols_tot} columns, "
     f"the flow identity exact at {_flow_ok} of {_flow_ok} "
     f"transitions, built on both quotients")
emit(f"    targets     : {SETTLEMENT['targets']} -- the law value at "
     f"the declared primary readout is {frl(LAW1)} at both legs; the "
     f"pre-registered values are {frl(SHADOW1)} and {frl(SHADOW2)}.  "
     f"Three convergent reasons, each measured: the targets were "
     f"census statistics at birth "
     f"({_three_reasons['census_statistics_at_birth']}); the target "
     f"test is Gamma-free and off-carrier "
     f"({_three_reasons['gamma_free_and_off_carrier']}, token scan "
     f"{len(_hits)} hits, depths {min(_leg_depths)}..{max(_leg_depths)}); "
     f"the count readout breaks the mandatory negative control "
     f"({_three_reasons['count_readout_breaks_the_control']}: REC "
     f"holonomy rank {CNT_HOL_R['rank']}, CK {_cnt_ck_r_fail} of "
     f"{len(CNT_CK_R)} failing, {_lit_cols - _lit_bad} of {_lit_cols} "
     f"columns stochastic)")
emit(f"    holonomy    : {SETTLEMENT['holonomy']} -- under the "
     f"well-posed form {T2_VERDICT}: D74's rung reproduced digit for "
     f"digit, the deviation derived by an identity at "
     f"{len(DEVROWS) - _id_viol} of {len(DEVROWS)} squares and located "
     f"in a measured descent failure at all of them, the negative "
     f"control flat at all three readings")
emit(f"    motivation  : {SETTLEMENT['motivation']} -- the readout "
     f"fiber is {_readout_fiber} (the third, step-normalised law "
     f"{frl(LAW1)}); {len(_forced) + len(_stab_i)} of "
     f"{len(INVENTORY)} choices motivated; per segment, "
     f"{sum(1 for r in SEGMOT if r['motivated'])} of {len(SEGMOT)}")
emit(f"    => {'SETTLED' if SETTLED else 'PARTIAL; the failed link(s): ' + ', '.join(_failed_links)}")
emit(f"  THE HONEST STATEMENT: the law is constructed, its geometry is "
     f"reproduced and its deviation located, its motivation is "
     f"non-empty -- and the census numbers it was asked to hit were "
     f"never values of any law.")

# ======================================================================
# THE NEXT-ITERATION REGISTER (adjudication R-GM-11's closing section)
# ======================================================================
sec("THE NEXT-ITERATION REGISTER")
REGISTER = [
    dict(item='CONG-185, THE RULED CARRIER',
         fact="the adjudication's carrier ruling: d74's own coarsest "
              "weighted congruence supersedes both MENU-113 and "
              "MENU+G.  On it the horizon potential descends at every "
              "horizon, there are zero multi-valued labelled edges in "
              "weights AND targets, all 44 curvature squares still "
              "close, the q-holonomy is <2,3> -- and the k-holonomy "
              "COLLAPSES BACK to <2,3>, so the enlargement this unit "
              "measures disappears.  The class chain is exactly "
              "lumpable there, so this unit's non-Markov finding is a "
              "MENU artefact.",
         recipe="partition refinement of the menu partition to a fixed "
                "point (5 rounds), reproducing d74's committed AB4 row "
                "'coarsest congruence 185 classes'; then re-run this "
                "unit's nine-test battery on it.  Dims per cut "
                "[1, 5, 17, 49, 113]: the successor is cheap.",
         status='NOT BUILT HERE -- the pin names MENU-113 and this '
                'unit builds what the pin names'),
    dict(item='THE DISINTEGRATION CRITERION, PROPERLY NORMALISED',
         fact="the readout must be fixed by a criterion declared "
              "before the battery and independent of any target.  The "
              "criterion: the readout under which Gamma is a "
              "disintegration of ONE measure across cuts -- the flow "
              "identity w(h) k_{4-|h|}(e|h) = w(h+e), which this unit "
              "verifies exactly.  At the leg level the same criterion "
              "selects the step-normalised reading, which IS the "
              "pinned kernel k_1.",
         recipe="declare the criterion in the pin; run every other "
                "reading as a control whose job is to show the battery "
                "can move -- and it does: the count reading gives the "
                "record quotient a rank-4 holonomy and destroys its "
                "exact lumpability.",
         status='APPLIED HERE as the declared primary; the pin did not '
                'declare it, so this unit declares it in the arena and '
                'measures all three'),
    dict(item='LAW-VALUE TARGETS, PRE-REGISTERED FROM THE LAW',
         fact="the pre-registered values were census statistics at "
              "birth.  A target must be a value of the law under the "
              "declared readout, not a leaf count.",
         recipe="pre-register the measured law values -- the "
                "step-normalised positional law and its "
                "leg-independence -- and demote the counting values to "
                "the declared census shadow they are.  If the corpus "
                "wants the counting values back as targets it must "
                "first PIN A TYPICALITY POSTULATE; that is a separate, "
                "nameable decision and should be taken in the open.",
         status='THE DEMOTION IS DONE HERE; the pre-registration is '
                "the successor's"),
    dict(item='THE HOLONOMY CONJUNCT: REPRODUCED-AND-LOCATED',
         fact="equality of groups is unsatisfiable by any "
              "column-stochastic construction from the pinned law on a "
              "non-descending carrier, and a category error for the "
              "aggregated family.  The well-posed conjunct is "
              "reproduction of the rung plus derivation and location "
              "of every deviation.",
         recipe="carry this unit's three-conjunct form forward; on "
                "CONG-185 the k-reading is expected to collapse onto "
                "the q-reading, which turns the located deviation into "
                "a vanishing one.",
         status='APPLIED HERE'),
    dict(item='THE [B3] FEASIBILITY LP',
         fact="the algebraic route speaks at exactly two of the four "
              "completions tested here.  The convention-free route is "
              "the exact feasibility LP, and it is row-decomposable: "
              "at the (1,2,3) triple it is 45 independent "
              "13-variable non-negative feasibility problems plus one "
              "column-sum coupling, so the scope-out is not forced by "
              "cost.",
         recipe="run the exact rational LP.  AND CARRY THE ATOM "
                "SCOPE: delta* is monotone under coarsening, so at "
                "CONG-185 -- which REFINES MENU-113 -- four of the six "
                "delivered Gamma-prep atom rows have delta* = 0 and "
                "the atom claim collapses to the (1,1) block.  The "
                "Gamma-iteration inherits only the (1,1)-block atoms "
                "as live at the ruled carrier, pending the Gamma-prep "
                "adjudication; and three of the four blocks are not "
                "even statable on the d <= 4 window, so the carrier "
                "must first be extended (d74 commits the wider arm: "
                "265 menu classes, coarsest congruence 462, at "
                "d <= 5).",
         status='NOT RUN HERE -- named in the not-executed register'),
    dict(item='THE LUMPABILITY / INDIVISIBILITY CARRIER STAMP',
         fact="FIRST-CLASS OPEN, from the adjudication: on CONG-185 "
              "the chain is exactly lumpable -- Markov at that level "
              "-- while the indivisibility signature lives at MENU.  "
              "THE QUANTUM CHARACTER OF Gamma IS CARRIER-RELATIVE.",
         recipe="the next iteration must measure the signature at BOTH "
                "levels and stamp every quantum-shape claim with the "
                "carrier it is read at.  This unit's own non-Markov "
                "and eq.-22 results are hereby stamped MENU-113.",
         status='STAMPED HERE, MEASURED AT ONE LEVEL ONLY'),
    dict(item='THE CROSS-UNIT ROWS THIS UNIT LEANS ON AND DOES NOT PIN',
         fact="Gamma-prep declares depth 7 infeasible; d <= 6 is "
              "Gamma-prep's own delivered arena, and this unit's "
              "previous delivery wrote as though d <= 6 were excluded "
              "by that declaration.  d74's d <= 5 arm (265 menu "
              "classes, coarsest congruence 462) is a pinned row the "
              "supply lists do not carry and the successor needs.",
         recipe="pin both rows explicitly in the successor's source "
                "register.",
         status='CORRECTED HERE in the scope section; the pinning is '
                "the successor's"),
]
for r in REGISTER:
    emit(f"  [{r['status']}] {r['item']}")
    emit(f"      fact  : {r['fact']}")
    emit(f"      recipe: {r['recipe']}")
_REG_MUT = [r for r in REGISTER if 'CONG-185' not in r['item']]


def register_ok(reg, vb_ok):
    return (len(reg) >= 6
            and all(r['fact'] and r['recipe'] and r['status']
                    for r in reg)
            and any('CONG-185' in r['item'] for r in reg)
            and vb_ok)


_vadj = all(r['ok'] for r in VB_ROWS if r['id'] == 'V-ADJ-CARRIER')
gate('G-NEXT-ITERATION', 'MUST',
     "the closing section is a REGISTER, not a wish list: every row "
     'carries a measured or quoted FACT, a RECIPE the successor can '
     'execute, and a STATUS saying whether this unit ran it; and the '
     "adjudication's carrier ruling is carried verbatim from its "
     'committed bytes',
     register_ok(REGISTER, _vadj),
     f"{len(REGISTER)} register rows, all with fact/recipe/status; the "
     f"CONG-185 ruling carried verbatim {_vadj}",
     falsifiers=['MUT-REGISTER-DROP'])
mutant('MUT-REGISTER-DROP', 'G-NEXT-ITERATION',
       "the adjudication's ruled carrier dropped from the register",
       register_ok(REGISTER, _vadj), register_ok(_REG_MUT, _vadj),
       f"a register of {len(_REG_MUT)} rows without the CONG-185 row "
       f"fails the gate's own carrier-ruling conjunct")

# ======================================================================
# THE CLI CONTRACT, GATED  (RUNBOOK 14, v14 #82)
# ======================================================================
sec("THE CLI CONTRACT, GATED")
_CLI_FLAGS = ('--selftest', '--mutant', '--list-mutants', '--out-dir',
              '--help')


_GUARD = 'if ' + 'WRITES_ALLOWED' + ':'
_NOWRITE = 'WRITES_ALLOWED = ' + '(not SELFTEST)'


def cli_contract(text, registry, evaluated):
    return dict(
        argv=text.count('sys.argv') >= 1,
        flags=all(f in text for f in _CLI_FLAGS),
        rejects=('SystemExit' + '(2)' in text),
        write_guard=(text.count(_GUARD) == 1
                     and text.count(", 'w',") >= 2),
        no_undeclared=(set(evaluated) <= set(registry)),
        selftest_writes_nothing=(_NOWRITE in text),
    )


_evaluated = [m['mutant'] for m in MUTANTS]
_CLI = cli_contract(_src, MUTANT_REGISTRY, _evaluated)
_CLI_MUT = cli_contract(_src.replace('sys.argv', 'NO_ARGV'),
                        MUTANT_REGISTRY, _evaluated)
gate('G-CLI-CONTRACT', 'MUST',
     'RUNBOOK 14 (v14 #82), the CLI-contract minimum, gated on this '
     "file's own source: an argv-parsed CLI; the five declared flags; "
     'unknown flags rejected with exit 2 rather than ignored; the two '
     'artifact writes reachable only through the single '
     'WRITES_ALLOWED guard, which --selftest and --mutant both close; '
     'and no falsifier evaluated that the registry does not declare '
     '(the exact equality of the two sets is gated at the closing '
     'census, once every falsifier exists)',
     all(_CLI.values()),
     f"{_CLI}; declared falsifiers {len(MUTANT_REGISTRY)}, evaluated so "
     f"far {len(_evaluated)}"
     + ("" if _CLI['no_undeclared'] else
        f"; evaluated-not-declared "
        f"{sorted(set(_evaluated) - set(MUTANT_REGISTRY))}"),
     falsifiers=['MUT-CLI-BLIND'])
mutant('MUT-CLI-BLIND', 'G-CLI-CONTRACT',
       'the argv channel removed from a copy of this source -- the '
       'zero-input-channel runner the #82 engraving declares '
       'undeliverable',
       all(_CLI.values()), all(_CLI_MUT.values()),
       f"the mutated source reads no argv ({_CLI_MUT['argv']}), so the "
       f"gate's own input-channel conjunct turns false")

# ======================================================================
# THE PAPER: CLAIM BINDING AND THE TOTAL PROSE-NUMBER SWEEP
# ======================================================================
sec("THE PAPER -- claim binding, and the TOTAL prose-number sweep")
PAPER_CLAIMS = {
    'menu_classes': str(len(set(A_MENU.values()))),
    'rec_classes': str(len(set(A_REC.values()))),
    'carrier': str(len(CARRIER)),
    'dims': fl(DIMS_M),
    'law': ", ".join(str(x) for x in LAW1),
    'shadow1': ", ".join(str(x) for x in CNT1),
    'shadow2': ", ".join(str(x) for x in CNT2),
    'rawproduct': ", ".join(str(x) for x in RAW1),
    'columns': str(_cols_tot),
    'flow': str(_flow_ok),
    'ck_fail': f"{sum(1 for r in CK if not r['interpolates'])} of "
               f"{len(CK)}",
    'kprimes': str(_k['primes']),
    'gprimes': str(_gm['primes']),
    'rsig': str(len(RSIG)),
    'legs1': str(len(LEGS1)),
    'legs2': str(len(LEGS2)),
    'raw1': str(N1),
    'raw2': str(N2),
    'closed': str(SQ['closed']),
    'menu_closes': str(_q23['closes']),
    'identity': f"{len(DEVROWS) - _id_viol} of {len(DEVROWS)}",
    'eq22': "/".join(str(r['negatives']) for r in EQ22),
    'blocks': f"{_pure} of {len(set(A_MENU.values()))}",
    'mono': f"{_MONO_CENSUSED} of {_MONO_TOTAL}",
    'crb_orbits': f"{pv(CRB, 'per_interval_law/rows/3/pinned_orbits')} "
                  f"orbits",
    'readout_fiber': f"fiber is {_readout_fiber}",
    'count_columns': f"{_lit_cols - _lit_bad} of {_lit_cols}",
    'rec_count_rank': f"rank {CNT_HOL_R['rank']}",
    'motivation': f"{len(_forced)} forced",
    'speaking': f"{len(_speak)} of 4",
}
_missing = [k for k, v in PAPER_CLAIMS.items() if v not in PAPER_TEXT]
_CLAIM_MUT = dict(PAPER_CLAIMS)
_CLAIM_MUT['menu_classes'] = str(len(set(A_MENU.values())) + 1)


def claims_ok(claims, text):
    return len([k for k, v in claims.items() if v not in text]) == 0


gate('G-PAPER-CLAIMS', 'MUST',
     "every headline number of the paper renders from this receipt: "
     "the paper's text must contain each rendered value.  The "
     'vacuous-pass disjunct is gone (an absent paper now aborts at P1) '
     'and every bound value is either at least three characters long '
     'or is bound WITH ITS LABEL',
     claims_ok(PAPER_CLAIMS, PAPER_TEXT),
     f"{len(PAPER_CLAIMS) - len(_missing)} of {len(PAPER_CLAIMS)} "
     f"rendered values present in {PAPER_PATH}; missing {_missing}; "
     f"shortest bound value {min(len(v) for v in PAPER_CLAIMS.values())} "
     f"chars",
     falsifiers=['MUT-PAPER-CLAIM-DROP'])
mutant('MUT-PAPER-CLAIM-DROP', 'G-PAPER-CLAIMS',
       'one headline value drifted by one unit -- the receipt-rendered '
       'value no longer occurs in the paper',
       claims_ok(PAPER_CLAIMS, PAPER_TEXT),
       claims_ok(_CLAIM_MUT, PAPER_TEXT),
       f"the drifted value {_CLAIM_MUT['menu_classes']!r} does not "
       f"occur in the paper, so the gate's own presence predicate "
       f"turns false")

# --- THE TOTAL PROSE-NUMBER SWEEP (adjudication R-GM-6) --------------
# The previous instrument bound 13 of 69 prose numerals and three
# falsified prose numbers survived a whole run at exit 0.  Every
# multi-digit numeral in the paper's prose must now render from a
# receipt value or appear in a DECLARED, PRINTED exemption register.


def digit_runs(text):
    out = []
    cur = ''
    for ch in text:
        if ch.isdigit():
            cur += ch
        else:
            if cur:
                out.append(cur)
            cur = ''
    if cur:
        out.append(cur)
    return out


def strip_code_spans(text):
    """Numerals inside inline-code spans are hashes, identifiers and
    verdict fragments; they are covered by the byte anchors and by the
    verdict comparator, and are excluded here by declaration."""
    out = []
    keep = True
    for ch in text:
        if ch == '`':
            keep = not keep
            continue
        if keep:
            out.append(ch)
    return "".join(out)


RENDERABLES = dict(PAPER_CLAIMS)
RENDERABLES.update({
    'verdict': VERDICT,
    'perlev': fl(PERLEV), 'cum': fl(CUM),
    'groot': fl(GROOT), 'dims_r': fl(DIMS_R),
    'sq': ctr(SQ), 'specq': ctr(SPEC_Q), 'speck': ctr(SPEC_K),
    'menu_rung': f"{_q23['closes']} {_q23['obstruction']} "
                 f"{_q23['selfloops']} {_q23['cycle_rank']}",
    'krung': f"{_k['selfloops']} {_k['rank']}",
    'grung': f"{_gm['nonunit']} {_gm['rank']}",
    'rec_rung': f"{_rq['closes']} {_rq['obstruction']} "
                f"{_rq['selfloops']} {_rq['cycle_rank']}",
    'facspec': ctr(_facspec), 'gam44': ctr(_gam44),
    'bd': ctr(_bd), 'prof': ctr(_prof),
    'ck_cells': fl([r['differing'] for r in _live]),
    'screen': ctr(_tally), 'mmass': ctr(_mcensus),
    'defects': f"{len(DEF88)} {len(_curv)} {len(_desc)}",
    'legcounts': f"{len(R1BASES)} {len(R2BASES)} {len(LEGS1)} "
                 f"{len(LEGS2)} {NU} {len(LEGSU)} {len(GATE_BASES)}",
    'mult': f"{_mult1} {_mult2}",
    'f8': fl([_slotkinds[i]['d'] for i in range(3)])
          + fl([_slotkinds[i]['n'] for i in range(3)]),
    'mech': f"{_cmp_after_d} {_tot_d} {_cmp_after_n} {_tot_n}",
    'flow_off': f"{_off_bad} {_off_ok + _off_bad}",
    'counts': f"{_lit_cols} {_lit_bad} {_fix_cols} "
              f"{CNT_HOL_R['nonunit']} {_cnt_ck_r_fail} {len(CNT_CK_R)} "
              f"{CNT_HOL_R['rank']} {CNT_HOL_M['rank']}",
    'cntprimes': f"{CNT_HOL_R['primes']} {CNT_HOL_M['primes']}",
    'residue': "".join(frl(_res[k][j]) for k in sorted(_res)
                       for j in range(3)),
    'inv': f"{len(_forced)} {len(_stab_i)} {len(_free)} "
           f"{len(INVENTORY)} {_readout_fiber} {_padding_fiber} "
           f"{_grain_fiber} {_rung_fiber}",
    'gatecounts': f"{len(GATES)} {len(MUTANTS)} {len(SOURCES)} "
                  f"{len(VB_ROWS)} {len(BY_ROWS)} {len(PV_ROWS)}",
    'lawref': frl(LAWREF), 'shadowref': frl(SHADOW1) + frl(SHADOW2),
    'monobp': f"{_MONO_BP // 100}.{_MONO_BP % 100:02d}",
    'gplevels': fl(_GP_LEVELS),
    'cells': f"{len(CELLS)} {CELLS[0]['renewal_count']} "
             f"{CELLS[0]['base_depth']} {CELLS[0]['end_depth']} "
             f"{CELLS[1]['base_depth']} {CELLS[1]['end_depth']}",
    'depths': fl(_leg_depths),
    'segmot': f"{sum(1 for r in SEGMOT if r['motivated'])} "
              f"{len(SEGMOT)}",
    'register': str(len(REGISTER)),
    'lit_sums': str(sorted(int(x) for x in _lit_sums)),
    'padfiber': f"{len(PADFIBER)} {len(TRIPLES)} {len(_speak)} "
                f"{len(_silent)}",
    'eq22min': " ".join(x for r in EQ22 for x in r['most_negative']),
    'screen_rows': " ".join(r['datum'] for r in SCREEN),
    'cra': f"{pv(CRA, 'verdict_segments/2')} "
           f"{pv(CRA, 'verdict_segments/3')}",
    'carrier_blocks': ctr(_carrier_blocks)
                      + str(sum(_carrier_blocks.values())),
    'prune': f"{NU} {len(LEGSU)} {len(GATE_BASES)}",
    'sector': " ".join(str(x) for x in (_dm1 + _dm2 + _nm1 + _nm2)),
    'delopt': f"{sorted(_delopt)} {sorted(_delopt2)}",
})
# THE DECLARED EXEMPTION REGISTER, printed in full so that it is
# auditable: numerals that are structural rather than measured.
EXEMPT = [
    ('12', 'this unit is paper-12'), ('14', 'this is v14'),
    ('11', 'paper-11 is Gamma-prep'), ('09', 'paper-09'),
    ('10', 'the RUNBOOK #10 engraving; also a measured value'),
    ('20', 'the RUNBOOK #20 engravings'),
    ('34', 'the RUNBOOK #34 engravings; also a measured value'),
    ('46', 'the RUNBOOK #46 engraving'),
    ('62', 'the RUNBOOK #62 engravings'),
    ('64', 'v14 ledger #64, the pin; also a measured value'),
    ('82', 'v14 ledger #82, the adjudication'),
    ('88', 'v14 ledger #88, the supplementary orders'),
    ('2026', 'the year in the status line'),
    ('08', 'the month in the status line'),
    ('185', 'CONG-185, the adjudication\'s ruled carrier, quoted'),
    ('462', "d74's committed coarsest congruence at d <= 5, quoted"),
    ('265', "d74's committed menu quotient at d <= 5, quoted"),
    ('22', "Barandes' equation 22"),
    ('74', 'D74, the committed transport-holonomy unit'),
    ('42', 'd42b1, the committed layer'),
    ('56', 'd56, a named exclusion'),
    ('57', 'd57, a named exclusion'),
    ('72', 'D72, the committed exchange-square census'),
    ('15', 'RUNBOOK section 15'),
    ('13', 'RUNBOOK section 13; also a measured value'),
    ('11989', "the panel's independent two-route agreement count"),
    ('243768', 'the family transition total, derived in text from '
               "Gamma-prep's committed per-level table"),
    ('30728', 'the censused transition count, measured here'),
]
_EX = {t for t, _w in EXEMPT}
_ALLOWED = set()
for v in RENDERABLES.values():
    _ALLOWED |= set(digit_runs(str(v)))
_ALLOWED |= _EX
_ALLOWED |= {str(i) for i in range(10)}


def prose_sweep(text, allowed):
    """Three declared exclusions, each anchored elsewhere: the verdict
    block-quote (rendered from the gated object and audited by the
    comparator), inline-code spans (hashes and identifiers, covered by
    the byte anchors), and every VERBATIM-ANCHORED QUOTATION (bound
    byte-for-byte to a committed source by its own quote-fidelity row
    and its own drift falsifier).  Everything else is prose and is
    swept."""
    body = text.replace(VERDICT, '')
    for r in VB_ROWS:
        body = body.replace(r['quote'], ' ')
    body = strip_code_spans(body)
    runs = digit_runs(body)
    return sorted({r for r in runs if r not in allowed}), len(runs)


_unexplained, _numerals = prose_sweep(PAPER_TEXT, _ALLOWED)
_unexplained_mut, _ = prose_sweep(PAPER_TEXT + "\nA sweep of 7771 legs "
                                  "returned 1547 squares.\n", _ALLOWED)
emit(f"  THE DECLARED EXEMPTION REGISTER ({len(EXEMPT)} structural "
     f"numerals; every OTHER multi-digit numeral in the paper's prose "
     f"must render from a receipt value):")
for t, w in EXEMPT:
    emit(f"    {t:8s} {w}")
emit(f"  single digits 0-9 are exempt by declaration (section, list and "
     f"index numerals); every prose claim that turns on a single digit "
     f"is bound WITH ITS LABEL through the claim gate above.")
gate('G-PROSE-SWEEP', 'MUST',
     'THE TOTAL PROSE-NUMBER SWEEP: every numeral in the paper -- with '
     'the verdict block-quote and inline-code spans removed, both of '
     'which render or are anchored elsewhere -- is either a digit run '
     'of a value this receipt renders, or a member of the DECLARED and '
     'PRINTED exemption register.  The previous instrument bound 13 of '
     '69 prose numerals and three falsified prose numbers survived a '
     'whole run at exit 0',
     len(_unexplained) == 0,
     f"{_numerals} prose numerals swept over "
     f"{len(_ALLOWED)} allowed digit runs "
     f"({len(RENDERABLES)} receipt renderings + {len(EXEMPT)} declared "
     f"exemptions + the single digits); unexplained {_unexplained}",
     falsifiers=['MUT-PROSE-NUMBER'])
mutant('MUT-PROSE-NUMBER', 'G-PROSE-SWEEP',
       'two falsified prose numbers planted in the paper -- the '
       'injection class that survived the previous instrument '
       'byte-identically',
       len(_unexplained) == 0, len(_unexplained_mut) == 0,
       f"the planted numerals {_unexplained_mut} render from no "
       f"receipt value and appear in no exemption, so the sweep's own "
       f"predicate turns false")

# ======================================================================
# THE COMPLIANCE TABLE (built here; emitted and gated after the
# coverage census, whose numbers one of its rows reports)
# ======================================================================
RB = SRC['S-RUNBOOK'][4]
_eng9 = [ln for ln in RB.splitlines() if '2026-08-09, from v14' in ln]
_eng10 = [ln for ln in RB.splitlines() if '2026-08-10, from v14' in ln]
COMPLIANCE = [
    dict(rule='#10 containment is not equality: the verdict gate '
              'compares the COMPLETE emitted string against a '
              'segment-by-segment reconstruction',
         status='APPLIED', computed=None),
    dict(rule='#10 render from the gated object: the receipt and the '
              'paper render from the object the gates check',
         status='APPLIED', computed=None),
    dict(rule='#20 prose renders from the receipt: every numeric claim '
              'in the paper renders from the receipt or is marked '
              'derived-in-text at its derivation site',
         status='APPLIED', computed=None),
    dict(rule='#20 compliance claims are gate claims: a compliance gate '
              'ships with an injection falsifier that can fail it',
         status='APPLIED', computed=None),
    dict(rule='#20 path-value anchoring: a read-by-path anchors the '
              '(path, value) pair, not only the bytes',
         status='APPLIED', computed=None),
    dict(rule='#34 waiver claims are gate claims: coverage is by REACH, '
              'not by naming; every never-falsified gate has a '
              'reaching, killing mutant or a machine-checked forcing',
         status='APPLIED', computed=None),
    dict(rule='#34 verbatim-text anchors adopted: evaluated before byte '
              'anchors, bound to named consumer gates, context windows '
              'not fragments',
         status='APPLIED', computed=None),
    dict(rule='#46 no unanchored runtime inputs: every runtime input is '
              'a hash-pinned artifact or this unit\'s own frozen '
              'declaration; ledgers and STATUS are never read',
         status='APPLIED', computed=None),
    dict(rule='#62 verbatim anchors, corrected spec: quote fidelity, '
              'consumer gates existing / non-literal / '
              'mutant-falsified, genuine short-circuit',
         status='APPLIED', computed=None),
    dict(rule='#62 provenance by committed sha: sources declared by '
              'COMMIT SHA and read through it; `git show HEAD:` and '
              'worktree bytes are never read for a source',
         status='APPLIED', computed=None),
    dict(rule='#82 the CLI-contract minimum: an argv-parsed CLI that '
              'rejects unknown flags (exit 2), a --selftest that '
              'corrupts one anchor and writes nothing, and a '
              '--mutant NAME harness',
         status='APPLIED', computed=None),
    dict(rule='#82 comparator independence, strengthened: a verdict '
              'comparator shares NOTHING with its builder -- neither '
              'code, nor inputs, nor typed literals',
         status='APPLIED', computed=None),
]

# ======================================================================
# THE COVERAGE CENSUS -- honest denominators (adjudication R-GM-7)
# ======================================================================
sec("THE COVERAGE CENSUS at the #34 standard, with HONEST DENOMINATORS")
# --- the per-row ANCHOR drift sweep, run over EVERY anchor row that the
# --- run created.  Each row gets its OWN falsifier: perturb that row's
# --- expected value and re-evaluate THAT ROW's own predicate.
AN_DRIFT = []
for r in ANCHOR_ROWS:
    AN_DRIFT.append(dict(name=r['name'],
                         own_predicate_flips=(perturb(r['expected'])
                                              != r['measured'])))
_and = sum(1 for r in AN_DRIFT if r['own_predicate_flips'])
_AN_DRIFT_MUT = [dict(r) for r in AN_DRIFT]
for _i in range(1, len(_AN_DRIFT_MUT)):
    _AN_DRIFT_MUT[_i]['own_predicate_flips'] = False
_and_mut = sum(1 for r in _AN_DRIFT_MUT if r['own_predicate_flips'])
gate('G-ANCHOR-ROW-DRIFT', 'MUST',
     'EVERY anchor row carries its own falsifier: perturbing THAT '
     "row's expected value flips THAT row's own predicate, so anchor "
     'coverage is by reach and not by one mutant that names one row '
     'and credits the rest by declaration',
     _and == len(ANCHOR_ROWS) and len(ANCHOR_ROWS) > 0,
     f"{_and} of {len(ANCHOR_ROWS)} anchor rows falsified by their own "
     f"expected-value drift",
     falsifiers=['MUT-ANCHOR-DRIFT'])
mutant('MUT-ANCHOR-DRIFT', 'G-ANCHOR-ROW-DRIFT',
       'THE COVERAGE-BY-NAMING REGIME: a sweep in which exactly one '
       'anchor row is genuinely reached and every other row is '
       'credited by declaration',
       _and == len(ANCHOR_ROWS),
       _and_mut == len(ANCHOR_ROWS),
       f"the clean sweep reaches {_and} of {len(ANCHOR_ROWS)} rows; the "
       f"naming regime reaches {_and_mut}, and the gate's own predicate "
       f"turns false on it")
_adrift = {r['name']: r['own_predicate_flips'] for r in AN_DRIFT}
_vdrift = {VB_ROWS[i]['id']: VB_DRIFT[i]['own_predicate_flips']
           for i in range(len(VB_ROWS))}
_FORCINGS_CHECKED = {'G-KERNEL-PROPER': _pr_bad2 == 0,
                     'G-CUT-ADDITIVITY': all(m == 1 for m in _cutmass2)}
_gate_names = {g['name'] for g in GATES}
_bad_targets = sorted({t for m in MUTANTS
                       for t in m['target'].split(' / ')
                       if t not in _gate_names})
_no_reach = [m['mutant'] for m in MUTANTS if not m['reaches_target']]


def coverage(ledger, mutants):
    rows = []
    for g in ledger:
        if g['kind'] == 'ANCHOR':
            cov = bool(_adrift.get(g['name']))
            route = 'own expected-value drift'
        elif g['kind'] == 'VERBATIM':
            cov = bool(_vdrift.get(g['name']))
            route = 'own quotation drift'
        elif g['kind'] == 'THEOREM-PASS':
            cov = bool(_FORCINGS_CHECKED.get(g['name']))
            route = 'machine-checked forcing'
        else:
            cov = any(m['killed'] and m['reaches_target']
                      and g['name'] in m['target'].split(' / ')
                      for m in mutants)
            route = 'a declared falsifier that REACHES it'
        rows.append(dict(gate=g['name'], kind=g['kind'], covered=cov,
                         route=route, waiver=g['waiver']))
    return rows


COVROWS = coverage(GATES, MUTANTS)
_bad_lists = sorted({(g['name'], f) for g in GATES
                     for f in g['falsifiers']
                     if not any(m['mutant'] == f
                                and g['name'] in m['target'].split(' / ')
                                for m in MUTANTS)})
_bykind = defaultdict(lambda: [0, 0])
for r in COVROWS:
    _bykind[r['kind']][0] += 1
    _bykind[r['kind']][1] += int(r['covered'])
emit("  COVERAGE BY KIND (numerator = entries meeting the #34 standard "
     "by REACH, not by naming):")
for k in sorted(_bykind):
    t, c = _bykind[k]
    emit(f"    {k:14s} {c} of {t}")
_covered = sum(1 for r in COVROWS if r['covered'])
emit(f"    {'TOTAL':14s} {_covered} of {len(COVROWS)} "
     f"({(_covered * 1000) // len(COVROWS) // 10}."
     f"{(_covered * 1000) // len(COVROWS) % 10} per cent)")
emit(f"  mutant targets naming no ledger gate: {_bad_targets}; "
     f"declared falsifiers that do not reach their gate: {_no_reach}")
_SYNTH_GATE = dict(name='G-SYNTHETIC-UNCOVERED', kind='MUST',
                   statement='an unfalsified, unwaived MUST gate',
                   passed=True, detail='', falsifiers=[], waiver=None)
_SYNTH_MUT = dict(mutant='MUT-SYNTHETIC', target='G-DOES-NOT-EXIST',
                  injects='', predicate_on_clean_object=True,
                  predicate_on_mutated_object=False,
                  reaches_target=True, killed=True, detail='')


def coverage_ok(rows, badtargets, noreach, badlists):
    return (all(r['covered'] for r in rows) and len(badtargets) == 0
            and len(noreach) == 0 and len(badlists) == 0
            and len(rows) > 0)


mutant('MUT-COVERAGE-LAX', 'G-COVERAGE-HONEST',
       'a declared falsifier whose target names a gate that does not '
       'exist -- coverage credited by naming, the exact failure mode '
       'the instrument round measured at 52 of 53 anchors',
       coverage_ok(COVROWS, _bad_targets, _no_reach, _bad_lists),
       coverage_ok(COVROWS,
                   sorted({t for m in MUTANTS + [_SYNTH_MUT]
                           for t in m['target'].split(' / ')
                           if t not in _gate_names}), _no_reach,
                   _bad_lists),
       "a target naming no ledger gate enters the bad-target census "
       "and the gate's own predicate turns false")
gate('G-COVERAGE-HONEST', 'MUST',
     'THE COVERAGE LEDGER AT THE #34 STANDARD, with honest '
     'denominators: EVERY ledger entry is covered by its own route -- '
     'a MUST gate by a declared falsifier that REACHES it (measured: '
     "the gate's own predicate true on the clean object and false on "
     'the mutated one), an anchor by its OWN expected-value drift, a '
     'verbatim row by its OWN quotation drift, a theorem-pass by a '
     'machine-checked forcing.  No target may name a gate that does '
     'not exist, and no declared falsifier may fail to reach.  The '
     'previous delivery scored 88 of 88 by naming and 15 of 88 by '
     'reach',
     coverage_ok(COVROWS, _bad_targets, _no_reach, _bad_lists),
     f"{_covered} of {len(COVROWS)} ledger entries covered by reach; "
     f"by kind {dict((k, tuple(v)) for k, v in sorted(_bykind.items()))}; "
     f"bad targets {_bad_targets}; non-reaching falsifiers "
     f"{_no_reach}; gates whose declared falsifier list names a "
     f"falsifier that does not target them {_bad_lists}",
     falsifiers=['MUT-COVERAGE-LAX'])
# THE COMPLIANCE STATUSES, computed HERE and nowhere earlier: every
# count a row prints is the count at the moment the row is emitted, so
# no row can carry a number that was true only while the table was
# being built.
_cons = {r['consumer_gate'] for r in VB_ROWS}
_cons_exist = _cons <= {g['name'] for g in GATES}
_cons_literal = [g['name'] for g in GATES if g['name'] in _cons
                 and g['detail'] in ('True', 'False')]
_cons_falsified = {g['name'] for g in GATES if g['name'] in _cons
                   and any(m['killed'] and m['reaches_target']
                           and g['name'] in m['target'].split(' / ')
                           for m in MUTANTS)}
_COMP_COMPUTED = [
    f"G-VERDICT-EQUALITY audit {audit_ok(_AUD)} over "
    f"{len(VERDICT_RECORD['segments'])} segments and "
    f"{sum(len(v) for v in VERDICT_KEYMAP.values())} measured values; "
    f"6 verdict falsifiers, killed "
    f"{sum(1 for m in MUTANTS if m['mutant'].startswith('MUT-VERDICT') and m['killed'])}",

    f"one object: {len(GATES)} ledger entries read the same measured "
    f"values the receipt serialises; the paper is bound to "
    f"{len(PAPER_CLAIMS)} of them and swept for all others",

    f"TOTAL SWEEP: {_numerals} prose numerals, unexplained "
    f"{len(_unexplained)}; {len(PAPER_CLAIMS)} labelled claim "
    f"bindings; {len(EXEMPT)} declared structural exemptions, printed",

    f"every compliance row carries a computed status; "
    f"G-COMPLIANCE's own falsifier evaluates its predicate on a "
    f"mutated compliance table in which one status is null",

    f"{len(PV_ROWS)} path-value anchors, all resolved (an "
    f"unresolvable declared probe ABORTS: G-PROBE-RESOLUTION); "
    f"MUT-PATH-DRIFT killed "
    f"{[m['killed'] for m in MUTANTS if m['mutant'] == 'MUT-PATH-DRIFT'][0]}",

    f"coverage by REACH {_covered} of {len(COVROWS)} ledger entries; "
    f"by kind {dict((k, tuple(v)) for k, v in sorted(_bykind.items()))}; "
    f"every anchor and every verbatim row carries its OWN drift "
    f"falsifier; both theorem-pass waivers carry a machine-checked "
    f"forcing (re-priced law: {_FORCINGS_CHECKED})",

    f"{len(VB_ROWS)} rows, mean window "
    f"{sum(r['chars'] for r in VB_ROWS) // len(VB_ROWS)} chars, all "
    f"evaluated before the {len(BY_ROWS)} byte anchors, each with its "
    f"OWN drift falsifier ({_vbd} of {len(VB_ROWS)} flip)",

    f"runtime reads: {len(SOURCES)} committed blobs by declared sha, "
    f"this file, and THIS UNIT'S OWN PAPER -- read from the worktree "
    f"because it is the fourth deliverable and is not committed at "
    f"delivery time, and BYTE-ANCHORED here at {PAPER_SHA_EXPECTED} "
    f"(A-PAPER-SELF), which closes the unanchored-read residue; "
    f"v14/LOG.md and /STATUS.md read: 0",

    f"consumers {len(_cons)}: all exist {_cons_exist}; literal-True "
    f"consumers {len(_cons_literal)}; consumers with a REACHING, "
    f"killing declared mutant {len(_cons_falsified)} of {len(_cons)}; "
    f"short-circuit is structural (a verbatim failure exits before the "
    f"byte-anchor loop); each row carries its own drift falsifier, so "
    f"a meaning-inversion cannot pass by leaving the quoted bytes "
    f"intact -- and the paper itself is byte-anchored",

    f"declared shas {sorted({s[1] for s in SOURCES})}; path-value "
    f"stability across three shas: "
    f"{sum(1 for _, ok in _stab if ok)} of {len(_stab)}",

    f"CLI contract measured on this file's own source: {_CLI}; "
    f"declared falsifier registry {len(MUTANT_REGISTRY)}, evaluated in "
    f"total {len(MUTANTS)}; nothing evaluated that the registry does "
    f"not declare ({_CLI['no_undeclared']}); the exact equality of the "
    f"two sets is gated at the closing census; this run's mode "
    f"selftest={SELFTEST} mutant={MUT_ONLY!r} writes_allowed="
    f"{WRITES_ALLOWED}",

    f"the comparator re-parses a SERIALISED record "
    f"({len(VERDICT_RAW)} chars of JSON) and PARSES the emitted "
    f"string; it concatenates nothing, types no delimiter and no "
    f"measured value, and CHARACTERISES the connective tissue "
    f"(uniform between segments {_AUD.get('inner_uniform')}, "
    f"alphanumeric-free {_AUD.get('inner_structural')}, spans cover "
    f"the string exactly {_AUD.get('covers')}); a desynchronised "
    f"record fails it (MUT-VERDICT-DESYNC)",
]
for _ci, _cv in enumerate(_COMP_COMPUTED):
    COMPLIANCE[_ci]['computed'] = _cv

_ENG_TOTAL = len(_eng9) + len(_eng10)
_COMP_MUT = [dict(r) for r in COMPLIANCE]
_COMP_MUT[0]['computed'] = None


def compliance_ok(rows, eng9, eng10, cons_exist, cons_lit, cons_fals,
                  cons):
    return (len(rows) == 12 and len(eng9) == 10 and len(eng10) == 2
            and all(r['computed'] is not None for r in rows)
            and cons_exist and cons_lit == 0 and cons_fals == cons)


sec("THE COMPLIANCE SWEEP -- the twelve v14-origin RUNBOOK engravings "
    "(ten of 2026-08-09 and two of 2026-08-10), each with a COMPUTED "
    "status")
for r in COMPLIANCE:
    emit(f"  [{r['status']}] {r['rule']}")
    emit(f"      computed: {r['computed']}")
gate('G-COMPLIANCE', 'MUST',
     'all TWELVE v14-origin RUNBOOK engravings are enumerated with a '
     'COMPUTED status, the RUNBOOK\'s own counts agree, every row '
     'carries a non-null computed status, and the compliance claim is '
     'itself gated',
     compliance_ok(COMPLIANCE, _eng9, _eng10, _cons_exist,
                   len(_cons_literal), len(_cons_falsified),
                   len(_cons)),
     f"{len(COMPLIANCE)} engravings enumerated; the committed RUNBOOK "
     f"carries {len(_eng9)} v14-origin 2026-08-09 engravings and "
     f"{len(_eng10)} of 2026-08-10, total {_ENG_TOTAL}; rows with a "
     f"null computed status "
     f"{len([r for r in COMPLIANCE if r['computed'] is None])}; "
     f"consumer gates exist {_cons_exist}, literal {len(_cons_literal)}, "
     f"REACHING mutant-falsified {len(_cons_falsified)} of {len(_cons)}",
     falsifiers=['MUT-COMPLIANCE-FALSE'])
mutant('MUT-COMPLIANCE-FALSE', 'G-COMPLIANCE',
       'a compliance row asserted without a computed status -- the '
       'injection the previous delivery\'s falsifier could not detect '
       'because the gate never inspected the column',
       compliance_ok(COMPLIANCE, _eng9, _eng10, _cons_exist,
                     len(_cons_literal), len(_cons_falsified),
                     len(_cons)),
       compliance_ok(_COMP_MUT, _eng9, _eng10, _cons_exist,
                     len(_cons_literal), len(_cons_falsified),
                     len(_cons)),
       f"the mutated table carries "
       f"{len([r for r in _COMP_MUT if r['computed'] is None])} null "
       f"computed status, so the gate's own predicate turns false")

# ======================================================================
# THE NEVER-FALSIFIED AND CLOSING CENSUSES (#34; evaluated LAST, over
# the complete ledger, so nothing is temporally shadowed)
# ======================================================================
sec("THE NEVER-FALSIFIED CENSUS (the #34 standard), evaluated over the "
    "COMPLETE ledger")


def never_falsified(ledger, mutants):
    rows = coverage(ledger, mutants)
    nf = [dict(gate=r['gate'], kind=r['kind'], waiver=r['waiver'])
          for r in rows if not r['covered']]
    unw = [r for r in nf if r['waiver'] is None
           and r['kind'] not in ('ANCHOR', 'VERBATIM')]
    return nf, unw


NF, _nf_unwaived = never_falsified(GATES, MUTANTS)
_NF_MUT, _nfu_mut = never_falsified(GATES + [_SYNTH_GATE], MUTANTS)
emit(f"  ledger entries {len(GATES)}; declared falsifiers "
     f"{len(MUTANTS)}, all killed = {all(m['killed'] for m in MUTANTS)}, "
     f"all reaching = {all(m['reaches_target'] for m in MUTANTS)}")
emit(f"  never-falsified entries: {len(NF)}; of those, "
     f"{len(_nf_unwaived)} carry no verified waiver and are neither "
     f"anchors nor verbatim rows")
for r in NF:
    emit(f"    {r['gate']} [{r['kind']}] waiver: "
         f"{(r['waiver'] or 'NONE')[:110]}")


def nf_ok(mutants, unw):
    return (all(m['killed'] for m in mutants)
            and all(m['reaches_target'] for m in mutants)
            and len(unw) == 0)


mutant('MUT-WAIVER-FALSE', 'G-NEVER-FALSIFIED',
       'an unfalsified, unwaived MUST gate appended to a copy of the '
       'ledger -- the shadow-gate injection the previous instrument '
       'proved invisible to this census',
       nf_ok(MUTANTS, _nf_unwaived), nf_ok(MUTANTS, _nfu_mut),
       f"the injected gate is never falsified and carries no waiver, "
       f"so the unwaived count moves to {len(_nfu_mut)} and the gate's "
       f"own predicate turns false")
gate('G-NEVER-FALSIFIED', 'MUST',
     'every ledger entry is either falsified by a declared mutant that '
     "REACHES it and dies by the gate's own predicate, or carries a "
     'MACHINE-CHECKED forcing, or is an anchor / verbatim row covered '
     'by its OWN per-row drift; and every declared falsifier both '
     'reaches and kills',
     nf_ok(MUTANTS, _nf_unwaived),
     f"falsifiers {len(MUTANTS)}, killed "
     f"{sum(1 for m in MUTANTS if m['killed'])}, reaching "
     f"{sum(1 for m in MUTANTS if m['reaches_target'])}; "
     f"never-falsified without a verified waiver: {len(_nf_unwaived)} "
     f"{[r['gate'] for r in _nf_unwaived]}",
     falsifiers=['MUT-WAIVER-FALSE'])

_ALL_MUST = [g for g in GATES if g['kind'] == 'MUST']
_FAIL_MUST = [g for g in _ALL_MUST if not g['passed']]
_FAIL_ANY = [g for g in GATES if not g['passed']]


def census_closed(censused, full):
    nf, unw = never_falsified(censused, MUTANTS)
    return len(unw) == 0 and len(censused) == len(full)


mutant('MUT-CENSUS-LAX', 'G-CENSUS-CLOSED',
       'the closing census taken over the MUST subset of the ledger, '
       'leaving every anchor and every verbatim row outside the census '
       'that reports on them',
       census_closed(GATES, GATES), census_closed(_ALL_MUST, GATES),
       f"the must-pass subset is {len(_ALL_MUST)} of {len(GATES)} "
       f"entries, so a census over it omits "
       f"{len(GATES) - len(_ALL_MUST)} rows and the gate's own "
       f"denominator conjunct turns false")
_REG_EQ = (sorted(MUTANT_REGISTRY)
           == sorted(m['mutant'] for m in MUTANTS))
gate('G-CENSUS-CLOSED', 'MUST',
     'the closing census runs over the COMPLETE ledger, so that the '
     'compliance, coverage, paper-claim and never-falsified gates are '
     'themselves inside the census they report; the census denominator '
     'is gated against the full ledger size; only this gate is outside '
     'it, and it is falsified by MUT-CENSUS-LAX',
     census_closed(GATES, GATES) and _REG_EQ,
     f"complete ledger {len(GATES)} entries; never-falsified "
     f"{len(NF)}; unwaived non-anchor non-verbatim "
     f"{len(_nf_unwaived)} {[r['gate'] for r in _nf_unwaived]}; the "
     f"declared falsifier registry ({len(MUTANT_REGISTRY)}) equals the "
     f"set evaluated ({len(MUTANTS)}): {_REG_EQ}",
     falsifiers=['MUT-CENSUS-LAX'])

# ======================================================================
# THE RECEIPT
# ======================================================================
RECEIPT = dict(
    schema='isp/v14/gmain-geometry-update-law/2',
    unit='v14 GAMMA-MAIN -- THE GEOMETRY-UPDATE LAW (paper-12), '
         'REPAIRED under v14 #82 (orders R-GM-1..11) and v14 #88 '
         '(supplementary orders R-GM-12, R-GM-13)',
    pin='v14/note-gmain-pin.md',
    pin_sha256_12='8529ddc4a319',
    adjudication='v14/note-gmain-adjudication.md',
    adjudication_sha256_12='972e54741330',
    repair_orders=['R-GM-1 the verdict recomposed to the corrected '
                   'settlement',
                   'R-GM-2 the target section rebuilt: census shadow + '
                   'law value at the step-normalised primary readout',
                   'R-GM-3 the holonomy gate re-posed '
                   'REPRODUCED-AND-LOCATED with a killable identity',
                   'R-GM-4 a real argv-parsed CLI',
                   'R-GM-5 the verdict comparator rebuilt independent '
                   'of its builder',
                   'R-GM-6 the four surviving injections killed',
                   'R-GM-7 the coverage ledger rebuilt at the #34 '
                   'standard with honest denominators',
                   'R-GM-8 INJ12 closed: the instrument can emit '
                   'SETTLED',
                   'R-GM-9 the Gamma-prep probe resolved at the real '
                   'key',
                   'R-GM-10 the false instrument claims corrected; the '
                   'vacuous mutants replaced; N1 scoped',
                   'R-GM-11 paper rewritten single-threaded with the '
                   'next-iteration register',
                   'R-GM-12 the B2-atoms import scoped at the import '
                   'site',
                   'R-GM-13 the monotonicity denominator carried'],
    arithmetic='int / fractions.Fraction only; no float, no tolerance',
    arena=ARENA,
    cli=dict(flags=list(_CLI_FLAGS), contract=_CLI,
             default_out_dir='the directory of the source file',
             mode=dict(selftest=SELFTEST, mutant=MUT_ONLY,
                       writes_allowed=WRITES_ALLOWED)),
    provenance=dict(declared_shas=dict(tree=SHA_TREE, adjudication=SHA_ADJ,
                                       gprep=SHA_GPREP, r6bp=SHA_R6BP,
                                       cra=SHA_CRA, crb=SHA_CRB,
                                       r4=SHA_R4),
                    sources=[dict(id=s[0], sha=s[1], path=s[2],
                                  sha256_12=s[3], pedigree=s[4])
                             for s in SOURCES],
                    paper_sha256_12=_paper_sha,
                    exclusions=EXCLUSIONS,
                    erratum_v14_4=ERRATUM_4),
    verbatim_anchors=[{k: v for k, v in r.items() if k != 'quote'}
                      for r in VB_ROWS],
    verbatim_row_drift=VB_DRIFT,
    byte_anchors=BY_ROWS,
    anchor_row_drift=AN_DRIFT,
    path_value_anchors=PV_ROWS,
    path_value_stability=[dict(path=p, stable=ok) for p, ok in _stab],
    construction=dict(
        carrier_histories=len(CARRIER),
        menu_classes=len(set(A_MENU.values())),
        rec_classes=len(set(A_REC.values())),
        menu_dims_per_cut=DIMS_M,
        rec_dims_per_cut=DIMS_R,
        gamma_pairs_menu=len(GAM_M), gamma_pairs_rec=len(GAM_R),
        columns_total=_cols_tot, columns_bad=_cs_bad,
        potentials_G_root=GROOT,
        per_level=PERLEV, cumulative=CUM,
        cut_masses=[str(m) for m in _cutmass],
        local_menu_mass_census={k: v for k, v in sorted(_mcensus.items())},
        k1_is_step_normaliser_violations=_k1_bad,
        flow_identity=dict(at_matched_horizon_ok=_flow_ok,
                           at_matched_horizon_bad=_flow_bad,
                           off_horizon_ok=_off_ok,
                           off_horizon_bad=_off_bad),
        horizon_potential_multivalued=dict(
            MENU=[[r, b, t] for r, b, t in _Gmulti['MENU']],
            REC=[[r, b, t] for r, b, t in _Gmulti['REC']]),
        labelled_edges=dict(MENU=list(_lab['MENU']),
                            REC=list(_lab['REC'])),
        blocks=dict(rsig=len(RSIG), rmenu=len(RMENU),
                    profiles={str(k): v for k, v in sorted(_prof.items())},
                    carrier_rsig_points=sum(_carrier_blocks.values()),
                    carrier_block_pure=_pure,
                    carrier_classes_meeting_rsig=_nclass,
                    import_scope=IMPORT_SCOPE),
        monotonicity_scope=dict(censused=_MONO_CENSUSED,
                                family_total=_MONO_TOTAL,
                                reproduced_here=_MONO_MINE,
                                fraction=str(_MONO_FRAC),
                                basis_points=_MONO_BP,
                                shrinking=pv(GPR, 'mono_shrinking')),
    ),
    count_readout_control=dict(
        literal_columns=_lit_cols, literal_stochastic=_lit_cols - _lit_bad,
        literal_column_sums=sorted(str(x) for x in _lit_sums),
        repaired_columns=_fix_cols,
        repaired_stochastic=_fix_cols - _fix_bad,
        rec_holonomy=CNT_HOL_R, menu_holonomy=CNT_HOL_M,
        rec_ck_failures=_cnt_ck_r_fail, rec_ck_total=len(CNT_CK_R),
        occupancy_rec_ck_failures=_occ_ck_r_fail),
    tests=dict(
        T1_position_law=dict(
            r1_bases=len(R1BASES), r2_bases=len(R2BASES),
            leg1_raw_continuations=N1, leg1_legs=len(LEGS1),
            leg1_patterns={str(k): v for k, v in sorted(PAT1.items())},
            leg2_expansions=N2, leg2_legs=len(LEGS2),
            leg2_patterns={str(k): v for k, v in sorted(PAT2.items())},
            census_shadow=[[str(x) for x in SHADOW1],
                           [str(x) for x in SHADOW2]],
            census_shadow_status='EXTERNAL CONTROL, NEVER A TARGET',
            leg1_count=[str(x) for x in CNT1],
            leg1_raw_product=[str(x) for x in RAW1],
            leg1_step_normalised=[str(x) for x in LAW1],
            leg2_count=[str(x) for x in CNT2],
            leg2_raw_product=[str(x) for x in RAW2],
            leg2_step_normalised=[str(x) for x in LAW2],
            law_reference=[str(x) for x in LAWREF],
            readout_fiber=_readout_fiber,
            h4_reading='EXCLUDED-BY-CAP: needs depth '
                       f'{_h4_needed} against the family\'s '
                       f'{_h4_available}',
            verdict=T1_VERDICT,
            targets_are_law_values=_targets_are_law_values,
            off_carrier=dict(token_hits=_hits, leg_depths=_leg_depths,
                             region_chars=len(_T1REGION),
                             scanned_tokens=_GAMMA_TOKENS),
            residue={f"{k[0]}/{k[1]}": [[str(x) for x in v]
                                        for v in _res[k]]
                     for k in sorted(_res)},
            f8_slot_kind={str(i): dict(_slotkinds[i]) for i in range(3)},
            f8_mechanism=dict(pdp_comparable=_cmp_after_d,
                              pdp_total=_tot_d,
                              pnp_comparable=_cmp_after_n,
                              pnp_total=_tot_n),
            delivery_multiplicity=[str(_mult1), str(_mult2)],
            prune_gate=dict(bases=len(GATE_BASES), of=len(R2BASES),
                            unpruned_raw=NU, legs=len(LEGSU),
                            identical=_sub == _uns)),
        T2_holonomy=dict(
            square_census=dict(sorted(SQ.items())),
            spectrum_q={str(k): v for k, v in sorted(SPEC_Q.items())},
            spectrum_k={str(k): v for k, v in sorted(SPEC_K.items())},
            readings={q: {r: v for r, v in d.items()}
                      for q, d in HOL.items()},
            deviation=dict(identity_violations=_id_viol,
                           squares=len(DEVROWS),
                           factor_spectrum={str(k): v for k, v in
                                            sorted(_facspec.items())},
                           carrier_closing=len(_menu_closing),
                           non_unit_on_closing=len(_mc_dev),
                           unlocated=_loc_bad,
                           multivalued_unit_factor=len(_mc_multi_unit),
                           non_unit_base_depths={str(k): v for k, v in
                                                 sorted(_dev_depths.items())}),
            verdict=T2_VERDICT,
            contains_d74=dict(k=_k_contains, gamma=_g_contains)),
        T3_screen=dict(census={k: v for k, v in sorted(_tally.items())},
                       rows=SCREEN, n3_objects=len(_n3),
                       single_pass_column_constant=_pass_degenerate),
        T4_interpolant=dict(menu_ck=CK, rec_ck=CKR, eq22=EQ22,
                            padding_fiber=PADFIBER,
                            completions_that_speak=_speak,
                            completions_silent=_silent,
                            negatives_by_completion=_negs_by_style,
                            completions_agree=_agree,
                            renewal_distinct_columns=len(_cols)),
        T5_crb=dict(missing_tag=pv(CRB, 'missing_tag'),
                    n4_simplex_dim=_crb_n4['pinned_simplex_dim'],
                    n4_orbits=_crb_n4['pinned_orbits'],
                    n4_transitive=_crb_n4['pinned_transitive'],
                    dim_law=pv(CRB, 'per_interval_law/pinned_dim_law'),
                    censused_cells=CELLS,
                    distinct_renewal_counts=_n_values,
                    confounded_coordinates=_moving,
                    stamp='CONSTANT-ACROSS-THE-TWO-CENSUSED-CELLS-AT-'
                          'n=4; ORDINAL/DEPTH/ENSEMBLE-CONFOUNDED'),
        T6_cra=dict(head=pv(CRA, 'verdict_head'),
                    census=pv(CRA, 'verdict_segments/2'),
                    forced=pv(CRA, 'verdict_segments/3'),
                    gamma_moving_columns=_movingcols,
                    gamma_stationary_columns=_stat,
                    gamma_self_transitions=_selftrans,
                    declared_maps_measured=_shared,
                    sources_scanned=len(_BODIES),
                    hits=_shared_hits,
                    commutation='EXCLUDED-BY-REFERENT'),
        T7_wcross=dict(claims_measured=len(_claims),
                       candidate_sentences=len(_cand),
                       u2_clauses_located=len(_wc),
                       scanned_chars=len(_SCANTEXT)),
        T8_motivation=dict(items=INVENTORY,
                           forced=[r['id'] for r in _forced],
                           stabilizer_fixed=[r['id'] for r in _stab_i],
                           genuinely_free=[r['id'] for r in _free],
                           per_segment=SEGMOT),
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
                          ck_failures=_occ_ck_r_fail),
        renewal_positive=dict(distinct_columns=len(_cols),
                              entries='1/8',
                              readouts_agree=GREN == GRENW),
        scramble=_scr, carrier=_car,
        misnormalized=dict(columns_broken=_mn_broken, columns=len(_mn),
                           family_columns=_bad_cols,
                           family_bad=_bad_bad),
    ),
    verdict=VERDICT,
    verdict_head=HEAD,
    verdict_segments=VERDICT_RECORD['segments'],
    verdict_record=VERDICT_RECORD,
    verdict_audit=_AUD,
    settlement=SETTLEMENT,
    settlement_links=LINKS,
    settlement_settled=SETTLED,
    settlement_failed_links=_failed_links,
    settlement_three_reasons=_three_reasons,
    settlement_battery=[dict(payload=n, segment=settlement_segment(p))
                        for n, p in BATTERY],
    next_iteration_register=REGISTER,
    gates=GATES,
    mutants=MUTANTS,
    coverage=COVROWS,
    coverage_by_kind={k: dict(entries=v[0], covered=v[1])
                      for k, v in sorted(_bykind.items())},
    never_falsified=NF,
    compliance=COMPLIANCE,
    paper_claims=PAPER_CLAIMS,
    prose_sweep=dict(numerals=_numerals, unexplained=_unexplained,
                     allowed_runs=len(_ALLOWED),
                     exemptions=[list(x) for x in EXEMPT]),
    totals=dict(sources=len(SOURCES), verbatim=len(VB_ROWS),
                byte_anchors=len(BY_ROWS),
                path_value=len(PV_ROWS),
                ledger_entries=len(GATES),
                must_pass=len(_ALL_MUST),
                must_pass_failures=len(_FAIL_MUST),
                failures_any_kind=len(_FAIL_ANY),
                mutants=len(MUTANTS),
                mutants_killed=sum(1 for m in MUTANTS if m['killed']),
                mutants_reaching=sum(1 for m in MUTANTS
                                     if m['reaches_target']),
                coverage_by_reach=_covered,
                never_falsified=len(NF),
                never_falsified_unwaived=len(_nf_unwaived),
                anchor_failures=len(ANCHOR_FAIL),
                engravings_swept=_ENG_TOTAL),
    not_executed=[
        'CONG-185, the adjudication\'s RULED CARRIER: not built here.  '
        'The pin names MENU-113 and this unit builds what the pin '
        'names; the recipe, the expected collapse of the k-reading and '
        'the carrier-relativity of the quantum character are in the '
        'next-iteration register, attributed to the panel that '
        'measured them.',
        'the (A,B) d <= 6 arena -- which is GAMMA-PREP\'S OWN '
        'DELIVERED ARENA, not an excluded one -- and the d <= 7 arena, '
        'which Gamma-prep declares infeasible at ~1,696,040 histories. '
        ' The carrier here is the pinned d <= 4 arena with a d <= 5 '
        'anchor scope.',
        'the three-actor and four-actor pools of D74 (the carrier is '
        'the (A,B) arena the pin declares)',
        'the MATCHED horizon convention (H4 is declared; the '
        'alternative is named in the inventory, stamped in the '
        'B2-import scope, and not run)',
        'the 13-class primary grain of Gamma-prep (the 113-class '
        'control grain IS D74\'s carrier and is what the pin names; '
        'the exclusion is stamped at the import site)',
        'an exact feasibility LP for the [B3] existence question: the '
        'decision order stops at the process\'s own conditional and at '
        'the unique algebraic candidate under four declared '
        'completions.  The LP is row-decomposable and is the '
        'successor\'s first item.',
        'the eq.-22 inversion on the REC quotient (a 2,477-label '
        'rational inversion) -- EXCLUDED-BY-CAP',
        "U3's general polygon obstruction (it needs U3's exact surd "
        "sign oracle); it is a necessary condition only and the "
        "census's one S-PASS carries a constructed certificate, so "
        'the omission moves no verdict here',
        'any CP-divisibility, Bell, locality or covariance test',
    ],
    python=f"{sys.version_info.major}.{sys.version_info.minor}."
           f"{sys.version_info.micro}",
    source_sha256=hashlib.sha256(
        open(SELF, 'rb').read()).hexdigest()[:12],
)
RECEIPT_BOX.append(RECEIPT)

sec("TOTALS")
for k, v in RECEIPT['totals'].items():
    emit(f"    {k:28s}: {v}")
emit("")
emit("  NOT EXECUTED, and why:")
for x in RECEIPT['not_executed']:
    emit(f"    - {x}")

if _FAIL_ANY or ANCHOR_FAIL:
    emit("")
    emit(f"  FAILURES: must-pass {[g['name'] for g in _FAIL_MUST]}; "
         f"any kind {[g['name'] for g in _FAIL_ANY]}; ANCHOR "
         f"{ANCHOR_FAIL} -- exit 1.")

# ======================================================================
# THE --mutant HARNESS: one declared falsifier, in isolation
# ======================================================================
if MUT_ONLY is not None:
    _sel = [m for m in MUTANTS if m['mutant'] == MUT_ONLY]
    emit("")
    emit("  ===== SINGLE-MUTANT HARNESS =====")
    if not _sel:
        emit(f"  {MUT_ONLY} was declared but never evaluated by this "
             f"run.  exit 1.")
        finish(1)
    m = _sel[0]
    emit(f"  mutant                    : {m['mutant']}")
    emit(f"  target gate               : {m['target']}")
    emit(f"  injects                   : {m['injects']}")
    emit(f"  predicate, clean object   : "
         f"{m['predicate_on_clean_object']}")
    emit(f"  predicate, mutated object : "
         f"{m['predicate_on_mutated_object']}")
    emit(f"  reaches target (MEASURED) : {m['reaches_target']}")
    emit(f"  killed                    : {m['killed']}")
    emit(f"  files written             : {len(WRITTEN)}")
    finish(0 if (m['killed'] and m['reaches_target']) else 1)

finish(1 if (_FAIL_ANY or ANCHOR_FAIL) else 0)
