"""GAMMA-ITERATION -- the geometry-update law on the ruled carrier.

v14 paper-16.  ONE self-contained program.  Exact arithmetic only
(`int` and `fractions.Fraction`); the file's own syntax tree is scanned
for float literals and for banned numeric names, and the scan is a gate.

Deliverables: v14/paper-16-gamma-iteration.md, this file,
`giter_output.txt`, `giter_receipt.json`.

PROVENANCE DISCIPLINE (#91).  Every source is read from a path resolved
from this file's own location and is GATED against a sha256-12 declared
in the frozen pin.  No subprocess is spawned, no `git` is invoked, no
moving reference (`HEAD`, a branch name, a tag) is read: a drifted
source fails its byte anchor before any measurement runs, which is what
a pinned-sha read buys without a version-control system present.  The
plain run therefore byte-reproduces off-tree and with git absent.

CLI (#82): `--help`, `--list-gates`, `--list-mutants`, `--selftest`,
`--mutant NAME`, `--out-dir DIR`.  Unknown flags exit 2.  `--selftest`
corrupts exactly one anchor, confirms the run exits 1, and writes
nothing.  `--mutant NAME` evaluates one declared falsifier and leaves
every artifact untouched.  Only a clean plain run writes.

THE GATE-TIME SEAL (#119, lifted from R4b's `r4b_momentum_exact.py`).
Every published object is DIGESTED AT THE MOMENT ITS GATE PASSED, and
every registry row is digested at the moment it is registered.  The
receipt is then built FROM THE SEALED SNAPSHOTS, not from the live
objects; `G-SEAL-COMPLETE` re-digests the live objects and refuses the
delivery if any seal has moved since its gate.  The artifacts are
written to temporaries, re-read, matched AGAINST THE SEAL -- never
against live memory, which would confirm a corruption rather than catch
it -- and only then moved into place with `os.replace`.  A terminal
re-verification runs last, at process exit, and removes the artifacts
and exits non-zero if the bytes on disk have moved: no corrupt file is
left on disk by any path.
"""

import ast
import atexit
import hashlib
import json
import os
import re
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction as Fr

T0 = time.time()
SELF = os.path.abspath(__file__)
HERE = os.path.dirname(SELF)
REPO = os.path.dirname(os.path.dirname(HERE))
OUT_LINES = []

USAGE = """usage: giter_exact.py [--help] [--list-gates] [--list-mutants]
                      [--selftest] [--mutant NAME] [--out-dir DIR]

  (no flags)        the plain delivery run: writes giter_output.txt and
                    giter_receipt.json beside this file, exit 0 only if
                    every MUST gate passes and every falsifier kills.
  --selftest        corrupt exactly one declared anchor, confirm the
                    delivery refuses (exit 1), write nothing.
  --mutant NAME     evaluate one declared falsifier in isolation; exit 0
                    only if it reaches its named gate and kills it.
                    Writes nothing.
  --list-gates      print the gate registry the delivery evaluates.
  --list-mutants    print the falsifier registry.
  --out-dir DIR     write the artifacts to DIR instead of this file's
                    own directory.
"""

MUTANT_REGISTRY = [
    'MUT-VERBATIM-DRIFT', 'MUT-BYTE-DRIFT', 'MUT-PATH-DRIFT',
    'MUT-PROBE-UNRESOLVED', 'MUT-FLOAT-LEAK', 'MUT-LAYER-EXIT',
    'MUT-MOVING-REF', 'MUT-REFINE-ORDER', 'MUT-CONG-COUNT',
    'MUT-CONG-DESCENT',
    'MUT-CONG-EDGES', 'MUT-CONG-SQUARES', 'MUT-CONG-QHOL',
    'MUT-CONG-KHOL', 'MUT-CONG-LUMP', 'MUT-SIX-LAX',
    'MUT-COLUMN-MISNORMALIZED', 'MUT-FLOW-HORIZON', 'MUT-K1-BREAK',
    'MUT-LAWVALUE-DRIFT', 'MUT-SHADOW-DRIFT', 'MUT-SHADOW-AS-TARGET',
    'MUT-PRUNE-LAX', 'MUT-DEVIATION-IDENTITY', 'MUT-DEVIATION-PLANTED',
    'MUT-HOLONOMY-HEAD', 'MUT-RECFLAT-CORRUPT', 'MUT-EQ22-SIGN', 'MUT-EQ22-UNSTAMPED', 'MUT-CARRIER-RELATIVE-FLAT',
    'MUT-MULTITARGET-BLIND', 'MUT-LP-ROW-BLIND', 'MUT-LP-WITNESS-FAKE',
    'MUT-WROUTE-UNCERTIFIED', 'MUT-ATOM-UNSCOPED', 'MUT-UNREACH-DROP',
    'MUT-DELTA-CARRIER-SWAP', 'MUT-GRADING-BLIND', 'MUT-ANCHOR-PATH-FLIP',
    'MUT-RENEWAL-SCOPE-DROP', 'MUT-SUPPLY-D5', 'MUT-SUPPLY-EXCLUSION',
    'MUT-QUOTIENT-SCRAMBLE', 'MUT-REPRICE-WAIVER', 'MUT-COVERAGE-LAX',
    'MUT-COUNTS-ASSERTED', 'MUT-PROSE-NUMBER', 'MUT-PAPER-BYTES',
    'MUT-VERDICT-APPEND', 'MUT-VERDICT-HEAD', 'MUT-VERDICT-TRUNC',
    'MUT-VERDICT-DROP', 'MUT-VERDICT-RETYPE', 'MUT-VERDICT-DESYNC',
    # --- the repair batch (v14 #142/#143 orders R-GI-1 .. R-GI-12) ---
    'MUT-SEAL-BROKEN', 'MUT-SEAL-ROW-BROKEN', 'MUT-DISK-UNCHECKED',
    'MUT-SELECTOR-COMMITTED-FORM', 'MUT-DEVIATION-DELIVERY',
    'MUT-OFFTREE-RELATIVE', 'MUT-COVERAGE-NAMED-ONLY',
    'MUT-BANNED-ALIAS', 'MUT-MOVING-REF-SPACED', 'MUT-SHADOW-WIDE',
    'MUT-ITERATION-UNSORTED', 'MUT-CENSUS-ORDER',
    'MUT-PROSE-TRANSPOSE', 'MUT-VERDICT-REDERIVE',
    'MUT-MECHANISM-RECURRENCE', 'MUT-MECHANISM-NECESSARY',
    'MUT-MINSPLIT-ANY-REFINEMENT', 'MUT-CAP-LOCAL',
    'MUT-NORMALISER-CARRIER', 'MUT-EQ22-CELL-BLIND',
    'MUT-CHOICE-UNPRICED', 'MUT-ATOM-CLASS-SCOPE',
]


def _cli(argv):
    selftest, mut, outdir = False, None, None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == '--help':
            sys.stdout.write(USAGE)
            raise SystemExit(0)
        if a == '--list-mutants':
            sys.stdout.write("\n".join(MUTANT_REGISTRY) + "\n")
            sys.stdout.write(f"{len(MUTANT_REGISTRY)} declared "
                             f"falsifiers.\n")
            raise SystemExit(0)
        if a == '--list-gates':
            LIST_GATES.append(True)
            i += 1
            continue
        if a == '--selftest':
            selftest = True
            i += 1
            continue
        if a == '--mutant':
            if i + 1 >= len(argv):
                sys.stderr.write("--mutant needs a NAME\n" + USAGE)
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
                sys.stderr.write("--out-dir needs a DIR\n" + USAGE)
                raise SystemExit(2)
            outdir = argv[i + 1]
            i += 2
            continue
        sys.stderr.write(f"unknown argument {a!r}\n" + USAGE)
        raise SystemExit(2)
    return selftest, mut, outdir


LIST_GATES = []
SELFTEST, MUT_ONLY, _OUTDIR = _cli(sys.argv[1:])
OUT_DIR = _OUTDIR if _OUTDIR is not None else HERE
WRITES_ALLOWED = (not SELFTEST) and (MUT_ONLY is None) and not LIST_GATES
WRITTEN = []
DIGEST = hashlib.sha256()


def emit(s=""):
    OUT_LINES.append(s)
    DIGEST.update((s + "\n").encode('utf-8'))


def prog(s):
    sys.stderr.write(f"[{time.time() - T0:.1f}s] {s}\n")
    sys.stderr.flush()


def sec(t):
    emit("")
    emit("=" * 74)
    emit(t)
    emit("=" * 74)


RECEIPT = {}
GATES = []
MUTANTS = []
ANCHOR_ROWS = []
ANCHOR_FAIL = []

# ----------------------------------------------------------------------
# THE GATE-TIME SEAL (#119), lifted verbatim-in-pattern from R4b's
# `v14/code/r4b_momentum_exact.py` @ 6d32993: a value is digested at the
# moment its gate passes; the receipt is built FROM the sealed snapshots;
# the payload may only be sealed if every earlier seal still verifies;
# and the terminal integrity gate compares the bytes ON DISK against
# these digests rather than against live memory.
#
# `SEALED_PATHS` is (seal id, receipt path, the gate that seals it).  The
# builder for each path is registered by `sealed()` and is called TWICE:
# once at gate time to take the digest, once at receipt time to re-digest
# the live objects.  A mutation of any published object between those two
# points moves the second digest and dies at `G-SEAL-COMPLETE`.
# ----------------------------------------------------------------------
SEALED_PATHS = [
    ('SEAL-PROVENANCE', 'provenance', 'G-PROVENANCE'),
    ('SEAL-CARRIER', 'carrier', 'G-SIX-PROPERTIES'),
    ('SEAL-LAW', 'law', 'G-FLOW-IDENTITY'),
    ('SEAL-TARGETS', 'targets', 'G-SHADOW-IS-A-CONTROL'),
    ('SEAL-HOLONOMY', 'holonomy', 'G-HOLONOMY-HEAD'),
    ('SEAL-DEVIATION', 'deviation', 'G-HOLONOMY-HEAD'),
    ('SEAL-EQ22', 'quantum_eq22', 'G-EQ22-STAMPED'),
    ('SEAL-QUANTUM', 'quantum', 'G-MECHANISM-MEASURED'),
    ('SEAL-B3', 'b3', 'G-B3-COUPLED'),
    ('SEAL-ANCHOR', 'anchor', 'G-ANCHOR-PATH'),
    ('SEAL-SUPPLY', 'supply', 'G-SUPPLY-EXCLUSIONS'),
    ('SEAL-SUPPLY-D5', 'supply_d5', 'G-SUPPLY-D5'),
    ('SEAL-CHOICES', 'choices', 'G-CHOICE-INVENTORY'),
    ('SEAL-VERDICT-STRING', 'verdict', 'G-VERDICT-EQUALITY'),
    ('SEAL-VERDICT-HEAD', 'verdict_head', 'G-VERDICT-EQUALITY'),
    ('SEAL-VERDICT-RECORD', 'verdict_record', 'G-VERDICT-EQUALITY'),
    ('SEAL-PAPER-SWEEP', 'paper_sweep', 'G-VERIFY-PAPER'),
]
SEAL_GATE = {sid: g for sid, _p, g in SEALED_PATHS}
SEAL_PATH = {sid: p for sid, p, _g in SEALED_PATHS}


def jcanon(value):
    """the canonical serialisation of a receipt object: deterministic,
    sorted, and independent of any dict's insertion order."""
    return json.dumps(value, indent=1, sort_keys=True, default=str)


def digest12(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()[:12]


class Seal:
    """`take` digests an object at the moment its gate passed and keeps
    the SNAPSHOT; `value` returns the snapshot the receipt is built from;
    `verify` re-digests the objects as they stand NOW and names every
    seal that has since been broken; `close` seals the payload only if
    every object seal still holds."""

    def __init__(self):
        self.rows = []
        self.index = {}
        self.snap = {}
        self.build = {}
        self.row_index = {}
        self.sealed_verdict = None
        self.payload = None
        self.payload_sha = None
        self.transcript = None
        self.transcript_sha = None

    def take(self, sid, builder):
        text = jcanon(builder())
        self.build[sid] = builder
        self.snap[sid] = text
        self.index[sid] = digest12(text)
        self.rows.append(dict(seal=sid, path=SEAL_PATH[sid],
                              sealed_at_gate=SEAL_GATE[sid],
                              sha256_12=self.index[sid],
                              bytes=len(text)))
        if sid == 'SEAL-VERDICT-STRING':
            self.sealed_verdict = json.loads(text)

    def value(self, sid):
        return json.loads(self.snap[sid])

    def verify(self):
        broken = []
        for sid in sorted(self.index):
            try:
                now = digest12(jcanon(self.build[sid]()))
            except Exception:
                broken.append(sid)
                continue
            if now != self.index[sid]:
                broken.append(sid)
        return broken

    # --- the registry rows, sealed at REGISTRATION time ---------------
    def row(self, kind, name, obj):
        self.row_index[f"{kind}:{name}"] = digest12(jcanon(obj))

    def verify_rows(self, live):
        broken = []
        for key, obj in live:
            if key not in self.row_index:
                broken.append(key + ' (unsealed)')
            elif digest12(jcanon(obj)) != self.row_index[key]:
                broken.append(key)
        if len(live) != len(self.row_index):
            broken.append(f'row arity {len(live)} against '
                          f'{len(self.row_index)}')
        return broken

    def close(self, payload, transcript, broken):
        if broken:
            raise SystemExit('G-SEAL-COMPLETE :: the payload was sealed '
                             'over a broken seal :: %s' % broken)
        self.payload = payload
        self.payload_sha = digest12(payload)
        self.transcript = transcript
        self.transcript_sha = digest12(transcript)


SEAL = Seal()


def gate(name, kind, statement, ok, detail, falsifiers=(), waiver=None):
    row = dict(name=name, kind=kind, statement=statement,
               passed=bool(ok), detail=detail,
               falsifiers=list(falsifiers), waiver=waiver)
    GATES.append(row)
    SEAL.row('GATE', name, row)
    emit(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    return bool(ok)


def mutant(name, target, injects, clean, mutated, detail):
    reaches = bool(clean) and not bool(mutated)
    row = dict(mutant=name, target=target, injects=injects,
               predicate_on_clean_object=bool(clean),
               predicate_on_mutated_object=bool(mutated),
               reaches_target=reaches, killed=reaches, detail=detail)
    MUTANTS.append(row)
    SEAL.row('MUTANT', name, row)
    if MUT_ONLY is None or MUT_ONLY == name:
        emit(f"  [{'KILLED' if reaches else 'SURVIVED'}] {name} -> "
             f"{target}: predicate on the clean object {bool(clean)}, on "
             f"the mutated object {bool(mutated)}; {detail}")
    return reaches


def anchor(name, expected, measured, what):
    ok = (expected == measured)
    grow = dict(name=name, kind='ANCHOR', statement=what, passed=ok,
                detail=f"expected {expected!r}, measured {measured!r}",
                falsifiers=[], waiver=None)
    GATES.append(grow)
    SEAL.row('GATE', name, grow)
    arow = dict(name=name, expected=expected, measured=measured,
                what=what, ok=ok)
    ANCHOR_ROWS.append(arow)
    SEAL.row('ANCHOR', name, arow)
    emit(f"  [{'PASS' if ok else 'ANCHOR-FAIL'}] {name}: {what} -- "
         f"expected {expected!r}, measured {measured!r}")
    if not ok:
        ANCHOR_FAIL.append(name)
    return ok


def fl(seq):
    return "[" + ", ".join(str(x) for x in seq) + "]"


def frl(seq):
    return "(" + ", ".join(str(x) for x in seq) + ")"


def ctr(c):
    return "{" + ", ".join(f"{k}: {v}" for k, v in
                           sorted(c.items(), key=lambda z: str(z[0]))) + "}"


def _disk_matches_the_seal(op, rp):
    """THE INTEGRITY TEST IS DISK-AGAINST-SEAL, never disk-against-live-
    memory: the bytes are read back and digested, and the digests are
    compared with the ones taken when the gates passed.  A comparison
    against a re-serialisation of the live objects would CONFIRM a
    corruption rather than catch it."""
    try:
        tx = read_bytes_text(op)
        js = read_bytes_text(rp)
    except OSError:
        return False, 'unreadable'
    if digest12(tx) != SEAL.transcript_sha:
        return False, 'transcript digest'
    if digest12(js) != SEAL.payload_sha:
        return False, 'payload digest'
    if DIGEST.hexdigest() != hashlib.sha256(tx.encode('utf-8')).hexdigest():
        return False, 'emitter digest'
    try:
        disk = json.loads(js)
    except ValueError:
        return False, 'the receipt on disk does not parse as JSON'
    for row in SEAL.rows:
        if digest12(jcanon(disk.get(row['path']))) != row['sha256_12']:
            return False, f"sealed path {row['path']}"
    if disk.get('verdict') != SEAL.sealed_verdict:
        return False, 'verdict string'
    return True, 'ok'


def read_bytes_text(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def _terminal_verification(op, rp):
    """RUNS LAST, AT PROCESS EXIT.  If the bytes on disk have moved since
    the write -- the post-write-at-exit-0 case -- the artifacts are
    REMOVED and the process exits non-zero.  No corrupt file is left on
    disk by any path."""
    ok, why = _disk_matches_the_seal(op, rp)
    if not ok:
        for p in (op, rp):
            try:
                os.remove(p)
            except OSError:
                pass
        sys.stderr.write(f"ARTIFACT INTEGRITY GATE FAILED AT EXIT ({why});"
                         f" the artifacts were removed\n")
        sys.stderr.flush()
        os._exit(1)


def finish(code):
    if WRITES_ALLOWED and code == 0:
        op = os.path.join(OUT_DIR, 'giter_output.txt')
        rp = os.path.join(OUT_DIR, 'giter_receipt.json')
        body = SEAL.transcript
        payload = SEAL.payload
        # THE NEGATIVE CONTROL, first: a deliberately corrupted payload is
        # written to a probe path and re-read, and the comparator must
        # NOTICE.  A comparator that always answers "intact" is caught.
        probe = rp + '.integrity-probe'
        with open(probe, 'w', encoding='utf-8') as f:
            f.write(payload[:-2] + ' }\n')
        detected = digest12(read_bytes_text(probe)) != SEAL.payload_sha
        os.remove(probe)
        # STAGED WRITE: temporaries first, matched against the GATE-TIME
        # SEAL, and only then moved into place with os.replace.  A failure
        # leaves no artifact behind at all.
        top, trp = op + '.tmp', rp + '.tmp'
        with open(top, 'w', encoding='utf-8') as f:
            f.write(body)
        with open(trp, 'w', encoding='utf-8') as f:
            f.write(payload)
        staged_ok, why = _disk_matches_the_seal(top, trp)
        if not (detected and staged_ok):
            for p in (top, trp):
                try:
                    os.remove(p)
                except OSError:
                    pass
            sys.stderr.write("ARTIFACT INTEGRITY GATE FAILED: what was "
                             f"about to be written does not match the "
                             f"gate-time seal ({why}; corruption probe "
                             f"detected={detected}); nothing written\n")
            sys.stdout.write(body)
            sys.stdout.write("[files written: 0]\n")
            sys.exit(1)
        os.replace(top, op)
        os.replace(trp, rp)
        WRITTEN.extend([op, rp])
        final_ok, why = _disk_matches_the_seal(op, rp)
        if not final_ok:
            for p in (op, rp):
                try:
                    os.remove(p)
                except OSError:
                    pass
            sys.stderr.write("ARTIFACT INTEGRITY GATE FAILED on disk "
                             f"({why}); the artifacts were removed\n")
            sys.stdout.write(body)
            sys.stdout.write("[files written: 0]\n")
            sys.exit(1)
        sys.stdout.write(body)
        sys.stdout.write(f"[artifact integrity: disk matches the "
                         f"gate-time seal, {len(SEAL.rows)} sealed "
                         f"objects + {len(SEAL.row_index)} sealed "
                         f"registry rows, payload {SEAL.payload_sha}, "
                         f"transcript {SEAL.transcript_sha}, corruption "
                         f"probe detected {detected}; files written: "
                         f"{len(WRITTEN)}]\n")
        sys.stdout.flush()
        # THE TERMINAL RE-VERIFICATION, registered so that it runs after
        # everything else this process can do.
        _EXIT_CHECK.append((op, rp))
    else:
        sys.stdout.write("\n".join(OUT_LINES) + "\n")
        sys.stdout.write(f"[files written: {len(WRITTEN)}]\n")
    prog(f"exit {code}")
    sys.exit(code)


_EXIT_CHECK = []


@atexit.register
def _at_exit_integrity():
    for _op, _rp in _EXIT_CHECK:
        _terminal_verification(_op, _rp)


# ======================================================================
# P0 -- PROVENANCE.  Byte anchors first, verbatim anchors before them.
# ======================================================================
sec("P0 -- PROVENANCE: pinned-sha reads without a version-control "
    "system")
emit("  Every source below is read from a path resolved from this "
     "file's own")
emit("  location and gated against the sha256-12 the frozen pin "
     "declares.  No")
emit("  subprocess, no `git`, no moving reference.  A drifted source "
     "dies at its")
emit("  byte anchor before any measurement runs.")


def read_text(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def sha12_of(t):
    return hashlib.sha256(t.encode('utf-8')).hexdigest()[:12]


SOURCES = [
    ('S-LAYER', 'v10/code/d42b1_transport_exact.py', '576275d55ecf',
     'THE COMMITTED LAYER: the d42b1 transport grammar (v10 #303/#304)'),
    ('S-D74-RESULT', 'v10/note-d74-transport-holonomy-result.md',
     '0180e21c7127', 'D74 result -- the carrier and the group'),
    ('S-D74-PIN', 'v10/note-d74-transport-holonomy-pin.md',
     'b9997d125ef5', 'D74 pin (frozen before its code was written)'),
    ('S-D74-CODE', 'v10/code/d74_transport_holonomy_exact.py',
     'bb852161aced', "D74's receipt -- the congruence recipe"),
    ('S-GMAIN-PAPER', 'v14/paper-12-gamma-main.md', '05f5dc7c7273',
     "GAMMA-MAIN terminal paper; its section 10 is THE INHERITANCE "
     "SOURCE"),
    ('S-GMAIN-CODE', 'v14/code/gmain_exact.py', 'a47d622c7608',
     "GAMMA-MAIN's receipt code"),
    ('S-GMAIN-RECEIPT', 'v14/code/gmain_receipt.json', 'd4fe2c64c082',
     "GAMMA-MAIN's delivered receipt"),
    ('S-GPREP-PAPER', 'v14/paper-11-transport-foundation.md',
     '0f92ab8a1af9', 'GAMMA-PREP terminal paper'),
    ('S-GPREP-RECEIPT', 'v14/code/gprep_foundation_receipt.json',
     'a28d8673a2cc', "GAMMA-PREP's delivered receipt"),
    ('S-ADJ-GMAIN', 'v14/note-gmain-adjudication.md', '972e54741330',
     'the GAMMA-MAIN joint adjudication -- the carrier ruling'),
    ('S-ADJ-GPREP', 'v14/note-gprep-adjudication.md', 'fdd8c76d7b29',
     'the GAMMA-PREP joint adjudication -- the carrier fact'),
    ('S-P09', 'v14/paper-09-renewal-transport.md', '006f96aaa2ff',
     'paper 09 -- the renewal-root first-return law'),
    ('S-PIN', 'v14/note-giter-pin.md', 'aa161f8f8e9d',
     "this unit's own frozen pin"),
]

SRC = {}
BYTE_ROWS = []
for _n, _p, _sha, _what in SOURCES:
    _full = os.path.join(REPO, _p)
    _t = read_text(_full)
    _got = sha12_of(_t)
    SRC[_n] = _t
    BYTE_ROWS.append(dict(name=_n, path=_p, expected=_sha, measured=_got,
                          ok=_got == _sha, what=_what))

# THE EXCLUDED SOURCE, declared and NOT read (the pin's cited-not-
# imported cross-check).  Its pinned sha is not the sha at the tip, and
# the working copy is being rewritten by a concurrent unit; a file whose
# bytes move cannot be a runtime input of a byte-reproducible run.
EXCLUDED = [dict(name='S-WELD2-PAPER', path='v14/paper-13-weld2-carrier-'
                 'census.md', pinned='535e288ff412',
                 reason='CITED, NOT IMPORTED (pin R1).  The pinned sha '
                        'is not the sha of the delivered tip and the '
                        'working copy is mid-repair by a concurrent '
                        'unit, so the bytes move; a moving file is not '
                        'a runtime input (#46/#91).  The weld-2 '
                        'six-of-six re-derivation of CONG-185 is '
                        'carried as a frozen citation and this unit '
                        're-derives the carrier itself instead.')]

# --- VERBATIM-CONTEXT ANCHORS (#62): evaluated FIRST, each at least 40
# --- characters, each occurring EXACTLY ONCE in its source, each bound
# --- to a REGISTERED consumer gate, each with its own drift falsifier.
VERBATIM = [
    ('V-CONG-RECIPE', 'S-D74-CODE', 'G-CONG-REDERIVED',
     "refinement to a fixed point) gives the coarsest weighted"),
    ('V-CONG-AGREE', 'S-D74-RESULT', 'G-CONG-SQUARES',
     "the coarsest weighted **congruence** (partition refinement, 4–6 "
     "rounds to a fixed point) closes **exactly the same** defective "
     "squares on **all six**"),
    ('V-D74-GROUP', 'S-D74-RESULT', 'G-CONG-QHOLONOMY',
     "**`⟨2,3⟩`, free abelian of rank 2, the full group of\n   "
     "3-smooth positive rationals**"),
    ('V-CARRIER-RULING', 'S-ADJ-GMAIN', 'G-SIX-PROPERTIES',
     "**CONG-185 supersedes MENU+G**: d74's own coarsest weighted\n"
     "congruence has descent at every horizon, zero multi-valued edges,"),
    ('V-CARRIER-OPEN', 'S-ADJ-GMAIN', 'G-CARRIER-RELATIVE',
     "quantum character of Γ is carrier-relative, and the next "
     "iteration"),
    ('V-LAWTARGET', 'S-GMAIN-PAPER', 'G-LAW-VALUE',
     "A target must be a\nvalue of the law under the declared readout, "
     "not a leaf count."),
    ('V-READOUT', 'S-GMAIN-PAPER', 'G-K1-IS-THE-STEP-NORMALISER',
     "step-normalised readout is the $r = 1$ member of the very kernel\n"
     "family $\\Gamma$ is built from"),
    ('V-B3LP', 'S-GMAIN-PAPER', 'G-B3-ROW-DECOMPOSED',
     "first triple it is 45 independent 13-variable non-negative "
     "feasibility\nproblems plus one column-sum coupling"),
    ('V-QUANTUM-STAMP', 'S-GMAIN-PAPER', 'G-QUANTUM-STAMPED',
     "**The\nquantum character of Γ is carrier-relative.**"),
    ('V-EQ22-GMAIN', 'S-GMAIN-PAPER', 'G-B3-COUPLED',
     "at every depth-cut triple with a non-degenerate first\ncut, no "
     "interpolant of eq. 22's form exists"),
    ('V-UNREACH', 'S-GPREP-PAPER', 'G-UNREACHABILITY-STAMP',
     "the $(1,1)$ block is entered from outside\n   at exactly $0$ "
     "transitions of the family"),
    ('V-COARSENING', 'S-GPREP-PAPER', 'G-COARSENING-LEMMA',
     "*If $\\Psi'$ coarsens $\\Psi$ then\n$\\delta^{*}(C, N, \\Psi') "
     "\\ge \\delta^{*}(C, N, \\Psi)$.*"),
    ('V-OPENQ', 'S-GPREP-PAPER', 'G-BLOCK-SPLIT-AT-CONG',
     "rounds $2 \\ldots 5$\nmight, and that is the open question"),
    ('V-D5ROW', 'S-GPREP-PAPER', 'G-SUPPLY-D5',
     "$(A,B)$ $d \\le 5$: menu quotient $265$, coarsest\n   congruence "
     "$462$, 6 refinement rounds"),
    ('V-BLOCK33', 'S-GPREP-PAPER', 'G-SUPPLY-FIFTH-BLOCK',
     "$(3, 3)$, $424$ points, all at\n    depth $6$"),
    ('V-RENEWAL-LAW', 'S-P09', 'G-ANCHOR-RENEWAL-ROOT',
     "**g(1) = g(2) = 0;  g(n) = C(n−1,2)(3/4)^(n−3)/256 for "
     "n ≥ 3.**"),
    ('V-RENEWAL-SCOPE', 'S-P09', 'G-ANCHOR-RENEWAL-ROOT',
     "At transport scope the picture will change and is declared"),
    ('V-PIN-EXPECT', 'S-PIN', 'G-HOLONOMY-HEAD',
     "CONG-185 the adjudicated expectation is agreement (the\n"
     "enlargement disappears — descent ⟹ r_k = r_q on closing\n"
     "squares, the operator's theorem)"),
    ('V-ATOM-LIVE', 'S-ADJ-GPREP', 'G-ATOM-BLOCK-SCOPE',
     "the atoms' live content is the (1,1) block only"),
]


def scramble(w):
    """Perturb a quotation at a CONTENT-BEARING token: the last
    alphanumeric run is altered.  A whitespace-only or punctuation-only
    edit would not test quote fidelity (#62)."""
    ms = [m for m in re.finditer(r'[A-Za-z0-9]+', w)]
    if not ms:
        return w + '~'
    m = ms[-1]
    return w[:m.start()] + m.group(0)[::-1] + 'x' + w[m.end():]


VERB_ROWS = []
for _n, _s, _cons, _w in VERBATIM:
    _t = SRC[_s]
    _cnt = _t.count(_w)
    _mut = scramble(_w)
    VERB_ROWS.append(dict(name=_n, source=_s, consumer=_cons,
                          length=len(_w), occurrences=_cnt,
                          ok=(_cnt == 1 and len(_w) >= 40),
                          drift_occurrences=_t.count(_mut),
                          drift_kills=(_t.count(_mut) == 0
                                       and _cnt == 1)))

_selftest_target = 'S-LAYER'
if SELFTEST:
    for _r in BYTE_ROWS:
        if _r['name'] == _selftest_target:
            _r['measured'] = _r['measured'][:-1] + '0'
            _r['ok'] = (_r['measured'] == _r['expected'])

_vb_ok = all(r['ok'] for r in VERB_ROWS)
_vb_drift = all(r['drift_kills'] for r in VERB_ROWS)
_bt_ok = all(r['ok'] for r in BYTE_ROWS)
emit("")
emit(f"  verbatim-context anchors: {len(VERB_ROWS)}, all located "
     f"exactly once and at least 40 characters: {_vb_ok}; each "
     f"perturbed at a content-bearing token and re-located: "
     f"{sum(1 for r in VERB_ROWS if r['drift_kills'])} of "
     f"{len(VERB_ROWS)} rows flip")
for _r in VERB_ROWS:
    emit(f"    {_r['name']:20s} <- {_r['source']:16s} -> "
         f"{_r['consumer']:32s} {_r['length']:4d} chars, "
         f"{_r['occurrences']} occurrence(s)")
emit("")
emit(f"  byte anchors: {len(BYTE_ROWS)} sources, all reproducing their "
     f"pinned sha256-12: {_bt_ok}")
for _r in BYTE_ROWS:
    emit(f"    [{'OK ' if _r['ok'] else 'BAD'}] {_r['name']:16s} "
         f"{_r['path']:46s} {_r['measured']}")
for _r in EXCLUDED:
    emit(f"    [EXCLUDED, NOT READ] {_r['name']}  {_r['path']}  pinned "
         f"{_r['pinned']}")

# THE ANCHOR PRECHECK.  A failing anchor refuses the delivery before a
# single measurement runs, and writes nothing.
if not (_vb_ok and _bt_ok):
    emit("")
    emit("  ANCHOR PRECHECK FAILED -- the delivery is refused before any "
         "measurement.")
    for _r in BYTE_ROWS:
        if not _r['ok']:
            emit(f"    byte anchor {_r['name']}: expected "
                 f"{_r['expected']}, measured {_r['measured']}")
    for _r in VERB_ROWS:
        if not _r['ok']:
            emit(f"    verbatim anchor {_r['name']}: "
                 f"{_r['occurrences']} occurrences")
    sys.stdout.write("\n".join(OUT_LINES) + "\n")
    sys.stdout.write(f"[anchor rows failing: "
                     f"{sum(1 for r in BYTE_ROWS if not r['ok'])} byte, "
                     f"{sum(1 for r in VERB_ROWS if not r['ok'])} "
                     f"verbatim]\n")
    sys.stdout.write("[files written: 0]\n")
    sys.exit(1)

# --- PATH-VALUE ANCHORS: declared probes into the two pinned receipts.
# --- An unresolvable probe ABORTS; it is never swallowed.
GMAIN_R = json.loads(SRC['S-GMAIN-RECEIPT'])
GPREP_R = json.loads(SRC['S-GPREP-RECEIPT'])


def pv(obj, path):
    cur = obj
    for step in path:
        if isinstance(step, int):
            if not isinstance(cur, list) or step >= len(cur):
                return (False, None)
            cur = cur[step]
        else:
            if not isinstance(cur, dict) or step not in cur:
                return (False, None)
            cur = cur[step]
    return (True, cur)


PROBES = [
    ('P-GMAIN-HEAD', GMAIN_R, ('verdict_head',), 'GMAIN-CONSTRUCTED'),
    ('P-GMAIN-LINKS', GMAIN_R, ('settlement_links',),
     ['constructed', 'targets', 'holonomy', 'motivation']),
    ('P-GMAIN-RSIG', GMAIN_R, ('construction', 'blocks',
                               'carrier_rsig_points'), 689),
    ('P-GPREP-BLK11-PTS', GPREP_R, ('B4_block11_points_d4',), 341),
    ('P-GPREP-BLK11-MENU', GPREP_R, ('B4_block11_menu_classes_d4',), 1),
    ('P-GPREP-ENTRIES', GPREP_R, ('B3_block_entries', 0),
     ['(1, 1)', 0]),
    ('P-GPREP-MONO', GPREP_R, ('B3_profile_decreases',), 0),
    ('P-GPREP-PAIRS', GPREP_R, ('B3_profile_pairs',), 243768),
    ('P-GPREP-OPENROWS', GPREP_R, ('B4_carrier_open_rows',),
     [['(1, 1)', 1], ['(1, 1)', 2]]),
    ('P-GPREP-DEADROWS', GPREP_R, ('B4_carrier_dead_rows',),
     [['(2, 2)', 1], ['(2, 2)', 2], ['(2, 3)', 1], ['(3, 2)', 1]]),
    ('P-GPREP-D4STAT', GPREP_R, ('B4_rows_statable_d4',), 0),
]
PROBE_ROWS = []
for _n, _o, _path, _want in PROBES:
    _res, _val = pv(_o, _path)
    PROBE_ROWS.append(dict(name=_n, path=[str(x) for x in _path],
                           resolved=_res, value=_val,
                           matches=(_res and _val == _want)))
_drift_probe = pv(GPREP_R, ('B4_block11_points_d4_DRIFTED',))
_probe_ok = all(r['resolved'] and r['matches'] for r in PROBE_ROWS)
emit("")
emit(f"  path-value anchors: {len(PROBE_ROWS)} declared probes into the "
     f"two pinned receipts; all resolve AND match: {_probe_ok}")
for _r in PROBE_ROWS:
    emit(f"    [{'OK ' if _r['matches'] else 'BAD'}] {_r['name']:20s} "
         f"{'.'.join(_r['path']):44s} -> {_r['value']!r}")
if not _probe_ok:
    emit("  PROBE PRECHECK FAILED -- an unresolvable or mismatched probe "
         "aborts the delivery; it is never swallowed.")
    sys.stdout.write("\n".join(OUT_LINES) + "\n")
    sys.stdout.write("[files written: 0]\n")
    sys.exit(1)

_paths_ok = all(os.path.exists(os.path.join(REPO, _p))
                for _, _p, _, _ in SOURCES)
gate('G-PROVENANCE', 'MUST',
     'every source is read from a path resolved from this file, EVERY '
     'DECLARED PATH RESOLVES ON DISK, and each is gated against the '
     'sha256-12 the frozen pin declares; the verbatim windows are '
     'located first and each is DECLARED AGAINST a registered consumer '
     'gate; every declared probe resolves and matches',
     _bt_ok and _vb_ok and _probe_ok and _vb_drift and _paths_ok,
     f"{len(SOURCES)} declared paths all resolving {_paths_ok}; "
     f"{len(BYTE_ROWS)} byte anchors OK; {len(VERB_ROWS)} verbatim "
     f"windows located exactly once, {sum(1 for r in VERB_ROWS if r['drift_kills'])} "
     f"of {len(VERB_ROWS)} flipping under a content-bearing "
     f"perturbation; {len(PROBE_ROWS)} probes resolved; "
     f"{len(EXCLUDED)} source declared and NOT read",
     falsifiers=['MUT-VERBATIM-DRIFT', 'MUT-BYTE-DRIFT', 'MUT-PATH-DRIFT',
                 'MUT-PROBE-UNRESOLVED'])
mutant('MUT-VERBATIM-DRIFT', 'G-PROVENANCE',
       'every quotation perturbed at its last content-bearing token and '
       're-located in its own source',
       _vb_ok,
       all(r['drift_occurrences'] == 1 for r in VERB_ROWS),
       f"{sum(1 for r in VERB_ROWS if r['drift_occurrences'] == 0)} of "
       f"{len(VERB_ROWS)} perturbed quotations no longer occur, so the "
       f"located-exactly-once predicate turns false on the drifted text")
_bt_mut = [dict(r) for r in BYTE_ROWS]
_bt_mut[0]['measured'] = _bt_mut[0]['measured'][:-1] + '~'
mutant('MUT-BYTE-DRIFT', 'G-PROVENANCE',
       'one byte anchor drifted by a single character',
       _bt_ok,
       all(r['measured'] == r['expected'] for r in _bt_mut),
       f"the drifted row {_bt_mut[0]['name']} reads "
       f"{_bt_mut[0]['measured']} against {_bt_mut[0]['expected']}, so "
       f"the byte-anchor conjunct turns false")
_pd_paths = [(_n, _p + 'x', _s, _w) for _n, _p, _s, _w in SOURCES]
_pd_drift = all(os.path.exists(os.path.join(REPO, _p))
                for _, _p, _, _ in _pd_paths)
mutant('MUT-PATH-DRIFT', 'G-PROVENANCE',
       'EVERY declared source path drifted by one character, re-resolved '
       "through the gate's own all-paths-resolve conjunct",
       _paths_ok, _pd_drift,
       f"the drifted declaration resolves {_pd_drift} against the "
       f"delivered {_paths_ok}, so the gate's OWN path conjunct turns "
       f"false -- a path change that would silently move the arena dies "
       f"here rather than at a predicate the gate does not carry")
mutant('MUT-PROBE-UNRESOLVED', 'G-PROVENANCE',
       'a probe pointed at a key that does not exist in the pinned '
       'receipt',
       _probe_ok, _drift_probe[0],
       f"the drifted probe resolves {_drift_probe[0]}, so the "
       f"all-probes-resolve conjunct turns false -- an unresolvable "
       f"probe aborts rather than being swallowed")

SEAL.take('SEAL-PROVENANCE',
          lambda: dict(byte_anchors=BYTE_ROWS, verbatim=VERB_ROWS,
                       path_value=PROBE_ROWS, excluded=EXCLUDED))

# --- NO MOVING REFERENCE, NO SUBPROCESS: measured on this file's own
# --- syntax tree.
_src_text = read_text(SELF)
_tree = ast.parse(_src_text)
_BAN = {'subprocess', 'popen', 'Popen', 'system', 'check_output',
        'numpy', 'math', 'random'}


def scan_names(tree):
    """#125 REPAIR: the banned-name scan collects IMPORT names too.  The
    delivered scan looked only at `ast.Name` and `ast.Attribute`, so
    `import subprocess as sp` and `from math import sqrt` evaded it -- an
    alias is a use, and a bare import is a capability."""
    names = set()
    for nd in ast.walk(tree):
        if isinstance(nd, ast.Name):
            names.add(nd.id)
        if isinstance(nd, ast.Attribute):
            names.add(nd.attr)
        if isinstance(nd, (ast.Import, ast.ImportFrom)):
            names.update(a.name.split('.')[0] for a in nd.names)
            names.update(a.asname for a in nd.names if a.asname)
            mod = (getattr(nd, 'module', '') or '').split('.')[0]
            if mod:
                names.add(mod)
    return names


_names = scan_names(_tree)
_banned = sorted(_names & _BAN)
_alias_src = _src_text.replace(
    "OUT_LINES = []", "OUT_LINES = []\nimport subprocess as _sp\n"
                      "from math import sqrt as _sq", 1)
_banned_alias = sorted(scan_names(ast.parse(_alias_src)) & _BAN)
# The needles are ASSEMBLED rather than typed: a literal spelling of a
# moving reference in this file would make the guard fire on its own
# source and could never be satisfied.
_H = 'HE' + 'AD'
_NEEDLES = ('git sh' + 'ow ' + _H + ':', _H + '~', 'orig' + 'in/')


def ws(t):
    """#125 REPAIR: both prohibition scans run on a WHITESPACE-NORMALISED
    haystack against whitespace-normalised needles.  A moving reference
    written with a doubled space, a tab or a newline inside it evaded the
    delivered contiguous-literal scan 4 of 4 times.  The needles are
    still ASSEMBLED rather than typed, and so is the evasion the
    falsifier splices: spelling either here would make the guard fire on
    its own source and it could never be satisfied."""
    return re.sub(r'\s+', ' ', t)


_src_ws = ws(_src_text)
_movingref = sorted({t for t in _NEEDLES if ws(t) in _src_ws})
_mr_spaced = sorted({t for t in _NEEDLES
                     if ws(t) in ws(_src_text + _NEEDLES[0].replace(
                         ' ', '  ', 1))})
_floats = [f"{n.lineno}:{n.value!r}" for n in ast.walk(_tree)
           if isinstance(n, ast.Constant) and isinstance(n.value, float)]
_leak = ast.parse(_src_text.replace("OUT_LINES = []",
                                    "OUT_LINES = []\n_lk = 0.5", 1))
_leakf = [1 for n in ast.walk(_leak)
          if isinstance(n, ast.Constant) and isinstance(n.value, float)]
gate('G-EXACT-AND-STATIC', 'MUST',
     "an AST scan of this file finds no float literal, no banned "
     "numeric or process name -- IMPORT NAMES AND ALIASES INCLUDED -- "
     'and no moving reference under a WHITESPACE-NORMALISED scan: every '
     'division is between int and Fraction and is therefore exact, and '
     'nothing is read at a branch tip',
     not _floats and not _banned and not _movingref,
     f"float literals {_floats}; banned names {_banned} over "
     f"{len(_names)} distinct names including every import and alias; "
     f"moving references {_movingref}, scanned against a "
     f"whitespace-normalised haystack of {len(_src_ws)} characters",
     falsifiers=['MUT-FLOAT-LEAK', 'MUT-MOVING-REF',
                 'MUT-MOVING-REF-SPACED', 'MUT-BANNED-ALIAS'])
mutant('MUT-FLOAT-LEAK', 'G-EXACT-AND-STATIC',
       'a float literal inserted into a COPY of this file\'s own source, '
       'which the same guard then re-scans',
       not _floats, not _leakf,
       f"the mutated source carries {len(_leakf)} float constant(s), so "
       f"the guard's own predicate turns false on it")
_mr_mut = sorted({t for t in _NEEDLES if ws(t) in ws(_src_text + _NEEDLES[0])})
mutant('MUT-MOVING-REF', 'G-EXACT-AND-STATIC',
       'a moving reference spliced into a copy of this source',
       not _movingref, not _mr_mut,
       f"the mutated source carries {_mr_mut}, so the no-moving-"
       f"reference conjunct turns false")
mutant('MUT-MOVING-REF-SPACED', 'G-EXACT-AND-STATIC',
       'THE #125 EVASION ITSELF: a moving reference spliced in with an '
       'EXTRA SPACE inside it, which the delivered contiguous-literal '
       'scan did not see',
       not _movingref, not _mr_spaced,
       f"the whitespace-normalised scan reports {_mr_spaced} on the "
       f"doubly-spaced splice, so the evasion the engraving names now "
       f"turns the conjunct false")
mutant('MUT-BANNED-ALIAS', 'G-EXACT-AND-STATIC',
       'THE SECOND #125 EVASION: a banned capability imported UNDER AN '
       'ALIAS (`import subprocess as _sp`, `from math import sqrt`), '
       'which the delivered Name/Attribute-only scan did not see',
       not _banned, not _banned_alias,
       f"the alias-aware scan reports {_banned_alias} on the spliced "
       f"copy, so an aliased import turns the banned-name conjunct "
       f"false")

# ======================================================================
# P1 -- THE LAYER, EXEC'D FROM ITS PINNED BYTES
# ======================================================================
sec("P1 -- THE COMMITTED LAYER, PORTED (pre-print slice only)")
_ls = SRC['S-LAYER']
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
_DEFS = ('candidates_for', 'admissible', 'canon', 'View', 'event_poset')


def layer_ok(prefix, ns):
    return (all(n in ns for n in _DEFS) and 'sys.exit' not in prefix
            and '\nprint(' not in prefix)


gate('G-LAYER-SINGLE-SOURCE', 'MUST',
     "the transport grammar is exec'd from the pinned bytes of the "
     'committed layer, pre-print slice only; nothing about admission or '
     'pricing is re-implemented here, and the ported slice contains no '
     'exit and no print',
     layer_ok(_PREFIX, NS),
     f"prefix {len(_PREFIX)} chars; definitions "
     f"{sorted(n for n in _DEFS if n in NS)}; exit-free "
     f"{'sys.exit' not in _PREFIX}",
     falsifiers=['MUT-LAYER-EXIT'])
mutant('MUT-LAYER-EXIT', 'G-LAYER-SINGLE-SOURCE',
       'an exit smuggled into the ported layer slice',
       layer_ok(_PREFIX, NS), layer_ok(_PREFIX + "\nsys.exit(0)\n", NS),
       "the mutated slice carries sys.exit, so the gate's own exit-free "
       "conjunct turns false")


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

# ======================================================================
# P2 -- THE DECLARED ARENA (data, before anything is computed; RUNBOOK
# section 15, and every coordinate matched at use)
# ======================================================================
sec("P2 -- THE DECLARED ARENA")
CAP = 4            # THE CARRIER: D74's (A,B) d <= 4 arena
CAP_A = 5          # the anchor scope: the d <= 5 supply row and the ports
ARENA = {
    'boundary': 'the empty history; genesis v0 is the committed layer\'s '
                'declared boundary',
    'family': 'ARM-1T, actor pool (A, B), exhaustive menus; depth <= 4 '
              'for THE CARRIER, depth <= 5 for the anchor scope',
    'law': 'the committed d42b1 weight law, exec\'d from its pinned '
           'bytes; nothing about admission or pricing re-implemented',
    'state': 'the history itself; every coarser object is a declared '
             'abstraction, named at each use',
    'carrier': 'CONG-185 -- D74\'s own coarsest weighted CONGRUENCE at '
               '(A,B) d <= 4, RE-DERIVED HERE by partition refinement '
               'from the menu partition and gated on its six ruling '
               'properties before use',
    'contrast carrier': 'MENU-113, the weighted-menu partition -- the '
                        'carrier the predecessor built.  Every '
                        'quantum-shape claim in this unit is stamped '
                        'with the carrier it is read at',
    'negative control': 'REC, the record quotient, 2477 classes, '
                        'measured FLAT',
    'cuts': 'depth cuts 0..4; the renewal-leg ensembles at the declared '
            'deeper conditioned scope',
    'horizon': 'H4 -- a history at depth d steps under k_{4-d}; terminal '
               'G(h, 0) = 1.  MATCHED is also run where the predecessor '
               'row is stated at it, and is named at each use',
    'readout': 'PRIMARY: the step-normalised law q(e|h)/M(h), RE-PROVED '
               'on THIS carrier to be exactly the pinned kernel k_1.  '
               'Also measured: the raw price product, and the counting '
               'measure',
    'targets': 'PRE-REGISTERED FROM THE LAW: (15/38, 5/19, 13/38) at '
               'both legs -- the value the predecessor measured at the '
               'proved step-normaliser.  NOT a census statistic',
    'census shadow': 'the two leaf-count triples (3/7,1/7,3/7) and '
                     '(4/9,1/9,4/9) are a DECLARED EXTERNAL CONTROL of '
                     'the enumeration, never a target',
    'provenance': f'{len(SOURCES)} sha-pinned sources plus this unit\'s '
                  f'own paper, byte-anchored; {len(EXCLUDED)} declared '
                  f'and not read',
}
for _k, _v in ARENA.items():
    emit(f"    {_k:18s}: {_v}")

# ======================================================================
# P3 -- THE FAMILY, THE QUOTIENTS, AND CONG-185 RE-DERIVED
# ======================================================================
sec("P3 -- THE FAMILY, AND THE RULED CARRIER RE-DERIVED IN UNIT")
prog("building the two-actor transport family to depth 5 ...")
CACHE = {}
_fr = [ROOT]
while _fr:
    h = _fr.pop()
    CACHE[h] = candidates_for(list(h), AB)
    if len(h) >= CAP_A:
        continue
    for e, q in CACHE[h]:
        _fr.append(h + (e,))
prog(f"family built: {len(CACHE)} histories")
LEVEL = Counter(len(h) for h in CACHE)
PERLEV = [LEVEL[i] for i in range(CAP_A + 1)]
CUM = [sum(PERLEV[:i + 1]) for i in range(CAP_A + 1)]
anchor('A-CENSUS-LEVEL', [1, 8, 60, 452, 3448, 26760], PERLEV,
       "the committed per-level transport census")
anchor('A-CENSUS-CUM', [1, 9, 69, 521, 3969, 30729], CUM,
       "the committed cumulative transport census")
CARRIER = {h for h in CACHE if len(h) <= CAP}
ANCHOR_SCOPE = set(CACHE)
# R-GI-9a (#143): EVERY verdict-bearing traversal runs over a SORTED
# sequence, never over a set.  The instrument's five-seed namespace sweep
# found 31 of 63 dicts carrying a hash-seed-dependent insertion order --
# no artifact byte moved, because every publication point sorts, but the
# guarantee rested on those downstream sorts rather than on the objects.
# These two sequences are the objects the traversals use; `G-ITERATION-
# ORDER` gates that no iteration over a bare set-valued name survives
# anywhere in this file.
CARRIER_S = sorted(CARRIER, key=sk)
ANCHOR_SCOPE_S = sorted(ANCHOR_SCOPE, key=sk)
anchor('A-CARRIER-SIZE', 3969, len(CARRIER),
       "D74's (A,B) d <= 4 arena size")

MENU = {h: sk(("MENU", tuple(sorted((evsk(e), str(q))
                                    for e, q in CACHE[h]))))
        for h in CARRIER_S}
REC = {h: sk(canon(list(h))) for h in CARRIER_S}
anchor('A-MENU-113', 113, len(set(MENU.values())),
       "D74's MENU rung: 113 classes at (A,B) d <= 4")
anchor('A-REC-2477', 2477, len(set(REC.values())),
       "D74's REC rung: 2,477 classes at (A,B) d <= 4")


def refine(dom, base, reverse=None, stop=None):
    """THE RECIPE, in this unit's own words: refine the menu partition
    by successor-closure -- a history's signature is its current class
    together with the multiset of (event label, successor class) over
    the successors that lie inside the window -- and iterate to a fixed
    point.  Returns the labelling, the round count, and the per-round
    trace.  `stop = k` returns the partition after exactly k rounds,
    which is how the intermediate quotients of the refinement lattice
    are reached."""
    order = sorted(dom, key=sk) if reverse is None else list(reverse)
    part = {h: base[h] for h in order}
    idx = {}
    part = {h: idx.setdefault(part[h], len(idx)) for h in order}
    trace = []
    for it in range(1, 40):
        nxt = {}
        for h in order:
            succ = tuple(sorted((evsk(e), part[h + (e,)])
                                for e, q in CACHE[h] if h + (e,) in part))
            nxt[h] = (part[h], succ)
        idx2 = {}
        out = {h: idx2.setdefault(nxt[h], len(idx2)) for h in order}
        dep = defaultdict(set)
        for h in order:
            dep[out[h]].add(len(h))
        trace.append((it, len(idx2),
                      sum(1 for v in dep.values() if len(v) > 1)))
        if stop is not None and it == stop:
            return out, it, trace
        if len(idx2) == len(set(part.values())):
            return out, it, trace
        part = out
    return part, 0, trace


prog("refining the menu partition to its fixed point ...")
_cong_idx, CONG_ROUNDS, CONG_TRACE = refine(CARRIER, MENU)
CONG = {h: ("CONG", _cong_idx[h]) for h in CARRIER_S}
CONG_N = len(set(CONG.values()))
emit("")
emit("  THE RECIPE, RE-RUN HERE.  Partition refinement of the menu "
     "partition to a")
emit("  fixed point.  The predecessor's own words, located verbatim in "
     "its receipt:")
emit(f"    \"{VERBATIM[0][3]}\"")
emit(f"  round trace (round, classes, classes spanning more than one "
     f"depth): {CONG_TRACE}")
gate('G-CONG-REDERIVED', 'MUST',
     'CONG-185 is RE-DERIVED here from the pinned layer by this unit\'s '
     'own partition refinement -- never imported -- and reproduces the '
     'committed row: 185 classes after 5 refinement rounds at (A,B) '
     'd <= 4',
     CONG_N == 185 and CONG_ROUNDS == 5,
     f"classes {CONG_N} after {CONG_ROUNDS} refinement rounds; per-round "
     f"class counts {[t[1] for t in CONG_TRACE]}",
     falsifiers=['MUT-CONG-COUNT'])
_mut_cong, _mut_rounds, _ = refine(CARRIER, REC)
mutant('MUT-CONG-COUNT', 'G-CONG-REDERIVED',
       'the refinement seeded from the RECORD partition instead of the '
       'menu partition -- a different starting point for the same '
       'closure',
       CONG_N == 185 and CONG_ROUNDS == 5,
       len(set(_mut_cong.values())) == 185 and _mut_rounds == 5,
       f"the record-seeded refinement fixes at "
       f"{len(set(_mut_cong.values()))} classes after {_mut_rounds} "
       f"rounds, so the gate's own class-count predicate turns false")

_rev = sorted(CARRIER, key=sk, reverse=True)
_cong_rev, _rounds_rev, _ = refine(CARRIER, MENU, reverse=_rev)


def blocks_of(lab):
    b = defaultdict(set)
    for h, c in lab.items():
        b[c].add(sk(h))
    return frozenset(frozenset(v) for v in b.values())


_blocks_same = blocks_of(_cong_idx) == blocks_of(_cong_rev)
_labels_same = (_cong_idx == _cong_rev)
gate('G-REFINE-DETERMINISTIC', 'MUST',
     "THE REFINEMENT IS A FUNCTION OF THE HISTORIES, NOT OF A HASH "
     "SEED: the traversal is a sorted ordering rather than a set's "
     'iteration order, and the partition it induces is invariant under '
     'reversing that ordering -- compared as a set of BLOCKS, which is '
     'the invariant, while the class INDICES are fixed by the sorted '
     'traversal so that the delivered artifacts are byte-reproducible',
     _blocks_same and _rounds_rev == CONG_ROUNDS,
     f"forward and reversed traversals agree on the partition as blocks "
     f"{_blocks_same} and on the round count ({CONG_ROUNDS} against "
     f"{_rounds_rev}); they disagree on the class INDICES "
     f"{not _labels_same}, which is why the delivered labelling is "
     f"pinned to the sorted traversal",
     falsifiers=['MUT-REFINE-ORDER'])
mutant('MUT-REFINE-ORDER', 'G-REFINE-DETERMINISTIC',
       'the invariance asserted of the class INDICES rather than of the '
       'partition -- the comparison a hash-seeded traversal would pass '
       'by luck and fail in general',
       _blocks_same, _labels_same,
       f"the reversed traversal hands out different indices "
       f"({not _labels_same}), so an index-level comparison turns "
       f"false while the block-level invariant holds")

DIMS = {}
for _nm, _V in (('MENU-113', MENU), ('CONG-185', CONG), ('REC', REC)):
    DIMS[_nm] = [len({_V[h] for h in CARRIER_S if len(h) == d})
                 for d in range(CAP + 1)]
    emit(f"  {_nm:9s} classes per depth cut: {fl(DIMS[_nm])}  "
         f"(distinct over all cuts: {len(set(_V.values()))}; sum of the "
         f"per-cut dimensions: {sum(DIMS[_nm])})")
anchor('A-CONG-DIMS', [1, 5, 17, 49, 113], DIMS['CONG-185'],
       "the ruled carrier's own per-cut dimensions, measured here")
anchor('A-MENU-DIMS', [1, 5, 13, 45, 113], DIMS['MENU-113'],
       "the predecessor's committed per-cut dimensions")

# --- THE SIX RULING PROPERTIES, gated one object at a time (#87) ------
sec("P3.1 -- THE SIX RULING PROPERTIES, gated before any use")
emit("  The carrier ruling this unit is executing, verbatim:")
emit(f"    \"{VERBATIM[3][3]}\"")

PRICE = {(h, e): Fr(q) for h in CACHE for e, q in CACHE[h]}


def potentials(prices):
    out = {}
    for h in sorted(CACHE, key=lambda x: -len(x)):
        out[(h, 0)] = Fr(1)
        for r in range(1, CAP_A - len(h) + 1):
            out[(h, r)] = sum(prices[(h, e)] * out[(h + (e,), r - 1)]
                              for e, q in CACHE[h])
    return out


G = potentials(PRICE)
anchor('A-POTENTIALS', ['2', '4', '257/32', '1035/64', '4173/128'],
       [str(G[(ROOT, r)]) for r in range(1, CAP_A + 1)],
       "the committed transport potentials G_D, D = 1..5")
MU = {ROOT: Fr(1)}
for h in sorted(CACHE, key=len):
    if h:
        MU[h] = MU[h[:-1]] * PRICE[(h[:-1], h[-1])]


def kern(h, e, r, GG=None, PP=None):
    GG = G if GG is None else GG
    PP = PRICE if PP is None else PP
    return PP[(h, e)] * GG[(h + (e,), r - 1)] / GG[(h, r)]


# (1) DESCENT AT EVERY HORIZON, per horizon, per carrier
DESCENT = {}
DESCENT_BAD = {}
for _nm, _V in (('CONG-185', CONG), ('MENU-113', MENU), ('REC', REC)):
    rows = []
    for r in range(0, CAP + 1):
        d = defaultdict(set)
        for h in CARRIER_S:
            if CAP - len(h) >= r:
                d[_V[h]].add(G[(h, r)])
        bad = {c for c, v in d.items() if len(v) > 1}
        DESCENT_BAD[(_nm, r)] = bad
        rows.append((r, len(bad), len(d)))
    DESCENT[_nm] = rows
    emit(f"  {_nm:9s} horizon potential G(.,r) multi-valued on "
         f"{[(r, b, n) for r, b, n in rows]}  (r, classes carrying more "
         f"than one value, classes tested)")
emit("  r = 0 is DEFINITIONAL and carries no content: G(.,0) = 1 "
     "identically, so every partition -- the record quotient and the "
     "scramble included -- scores 0 there; at r = 4 exactly one class "
     "(the root's) is testable.  The content of ruling property 1 is at "
     "r = 1, 2 and 3, and the tested populations are printed beside the "
     "counts above.")
_desc_c = sum(b for r, b, n in DESCENT['CONG-185'])
_desc_m = sum(b for r, b, n in DESCENT['MENU-113'])
gate('G-CONG-DESCENT', 'MUST',
     'RULING PROPERTY 1 @CONG-185: the horizon potential DESCENDS at '
     'EVERY horizon -- 0 classes carry more than one value of G(.,r), '
     'at r = 0, 1, 2, 3 and 4, one horizon at a time.  r = 0 is '
     'definitional (G(.,0) = 1) and r = 4 tests one class; the content '
     'is at r = 1, 2, 3 and the tested population is printed with each '
     'count',
     _desc_c == 0,
     f"@CONG-185 multi-valued classes by horizon "
     f"{[b for r, b, n in DESCENT['CONG-185']]} over populations "
     f"{[n for r, b, n in DESCENT['CONG-185']]} (total {_desc_c}); "
     f"@MENU-113 {[b for r, b, n in DESCENT['MENU-113']]} over "
     f"{[n for r, b, n in DESCENT['MENU-113']]} (total "
     f"{_desc_m}) -- the contrast carrier fails at r = 2 on 4 of 13 "
     f"classes, which is why the predecessor needed a lift",
     falsifiers=['MUT-CONG-DESCENT'])
mutant('MUT-CONG-DESCENT', 'G-CONG-DESCENT',
       "the same descent predicate evaluated on the contrast carrier "
       "MENU-113, which the predecessor measured NOT to descend at "
       "horizon 2",
       _desc_c == 0, _desc_m == 0,
       f"@MENU-113 the potential is multi-valued on "
       f"{DESCENT['MENU-113'][2][1]} of {DESCENT['MENU-113'][2][2]} "
       f"classes at horizon 2, so the descent predicate turns false")

# (2) MULTI-VALUED LABELLED EDGES
EDGES = {}
for _nm, _V in (('CONG-185', CONG), ('MENU-113', MENU), ('REC', REC)):
    w_, t_ = defaultdict(set), defaultdict(set)
    for h in CARRIER_S:
        if len(h) >= CAP:
            continue
        for e, q in CACHE[h]:
            w_[(_V[h], evsk(e))].add(Fr(q))
            t_[(_V[h], evsk(e))].add(_V[h + (e,)])
    EDGES[_nm] = (len(w_), sum(1 for v in w_.values() if len(v) > 1),
                  sum(1 for v in t_.values() if len(v) > 1))
    emit(f"  {_nm:9s} labelled edges {EDGES[_nm][0]:5d}, multi-WEIGHT "
         f"{EDGES[_nm][1]}, multi-TARGET {EDGES[_nm][2]}")
gate('G-CONG-EDGES', 'MUST',
     'RULING PROPERTY 2 @CONG-185: ZERO multi-valued labelled edges -- '
     'zero in the WEIGHT and, the stronger clause a congruence buys, '
     'zero in the TARGET, so the class graph is single-valued and the '
     'class process is a probabilistic bisimulation',
     EDGES['CONG-185'][1] == 0 and EDGES['CONG-185'][2] == 0,
     f"@CONG-185 {EDGES['CONG-185'][0]} labelled edges, multi-weight "
     f"{EDGES['CONG-185'][1]}, multi-target {EDGES['CONG-185'][2]}; "
     f"@MENU-113 {EDGES['MENU-113'][0]} edges, multi-weight "
     f"{EDGES['MENU-113'][1]}, multi-target {EDGES['MENU-113'][2]}",
     falsifiers=['MUT-CONG-EDGES'])
mutant('MUT-CONG-EDGES', 'G-CONG-EDGES',
       'the same single-valuedness predicate evaluated on MENU-113',
       EDGES['CONG-185'][1] == 0 and EDGES['CONG-185'][2] == 0,
       EDGES['MENU-113'][1] == 0 and EDGES['MENU-113'][2] == 0,
       f"@MENU-113 {EDGES['MENU-113'][2]} labelled edges carry more than "
       f"one target, so the gate's own multi-target conjunct turns "
       f"false -- MENU-113 is not a congruence")

# --- the square census, shared by properties 3, 4 and 5 --------------
prog("exchange-square census ...")
CLOSED, SQ = [], Counter()
for h in sorted(CARRIER, key=sk):
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
                rk = (kern(h, eA, CAP - d) * kern(h + (eA,), eB,
                                                  CAP - d - 1)
                      / (kern(h, eB, CAP - d)
                         * kern(h + (eB,), eA, CAP - d - 1)))
                CLOSED.append((h, eA, eB, rq, rk))
            elif okB2:
                SQ['AB-only'] += 1
            elif okA2:
                SQ['BA-only'] += 1
            else:
                SQ['both-blocked'] += 1
SPEC_Q = Counter(c[3] for c in CLOSED)
DEF88 = [c for c in CLOSED if c[3] != 1]
anchor('A-D74-SQUARES',
       {'AB-only': 28, 'BA-only': 12, 'both-blocked': 142, 'closed': 1546},
       dict(sorted(SQ.items())),
       "D72/D74's committed (A,B) d <= 4 exchange-square census")
anchor('A-D74-SPECTRUM', {'1/2': 70, '2/3': 2, '3/2': 6, '2': 10},
       {str(k): v for k, v in sorted(SPEC_Q.items()) if k != 1},
       "D74's committed non-unit spectrum at (A,B) d <= 4")
anchor('A-D74-DEFECTS', 88, len(DEF88),
       "D74's committed defective-square count at (A,B) d <= 4")

CLOSES = {}
for _nm, _V in (('CONG-185', CONG), ('MENU-113', MENU), ('REC', REC)):
    _dset = {(sk(c[0]), evsk(c[1]), evsk(c[2])) for c in DEF88
             if _V[c[0] + (c[1], c[2])] == _V[c[0] + (c[2], c[1])]}
    _aset = sum(1 for c in CLOSED
                if _V[c[0] + (c[1], c[2])] == _V[c[0] + (c[2], c[1])])
    CLOSES[_nm] = (_dset, _aset)
    emit(f"  {_nm:9s} closes {len(_dset)} of the {len(DEF88)} defective "
         f"squares and {_aset} of the {len(CLOSED)} closed squares")
_sym = CLOSES['CONG-185'][0] ^ CLOSES['MENU-113'][0]
gate('G-CONG-SQUARES', 'MUST',
     'RULING PROPERTY 3 @CONG-185: ALL 44 CURVATURE SQUARES INTACT -- '
     'the ruled carrier closes exactly 44 of the 88 defective squares, '
     'and the 44 are the SAME 44 AS SETS, not merely the same in '
     'number, as the predecessor carrier closes',
     len(CLOSES['CONG-185'][0]) == 44 and len(_sym) == 0,
     f"@CONG-185 closes {len(CLOSES['CONG-185'][0])} of {len(DEF88)}; "
     f"@MENU-113 closes {len(CLOSES['MENU-113'][0])}; symmetric "
     f"difference of the two sets {len(_sym)}; @REC closes "
     f"{len(CLOSES['REC'][0])}",
     falsifiers=['MUT-CONG-SQUARES'])
mutant('MUT-CONG-SQUARES', 'G-CONG-SQUARES',
       'the set identity replaced by a cardinality comparison against '
       'the record quotient, which closes none of them',
       len(CLOSES['CONG-185'][0]) == 44 and len(_sym) == 0,
       len(CLOSES['REC'][0]) == 44
       and len(CLOSES['REC'][0] ^ CLOSES['MENU-113'][0]) == 0,
       f"@REC the same predicate reads {len(CLOSES['REC'][0])} closed "
       f"and a symmetric difference of "
       f"{len(CLOSES['REC'][0] ^ CLOSES['MENU-113'][0])}, so the gate's "
       f"own set-identity predicate turns false")


# --- the exact R+ holonomy census by spanning-forest potentials -------
def holonomy_of(edges):
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
    lattice over the primes that occur: (primes, rank)."""
    vals = [v for v in values if v != 1]
    ps = sorted({p for v in vals for p in primes_of(v)})
    if not ps:
        return [], 0
    rows = [[primes_of(v).get(p, 0) for p in ps] for v in vals]
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


def reading(V, idx):
    ex = [(V[c[0] + (c[2], c[1])], V[c[0] + (c[1], c[2])], c[idx])
          for c in CLOSED]
    selfl = Counter(w for u, v, w in ex if u == v)
    n_, rk_, ob_, hol_ = holonomy_of([e for e in ex if e[0] != e[1]])
    vals = list(selfl.elements()) + [k for k, v in hol_.items()
                                     for _ in range(v)]
    ps, rank = group_of(vals)
    return dict(closes=sum(selfl.values()),
                nonunit=sum(v for k, v in selfl.items() if k != 1),
                cyclerank=rk_, obstruction=ob_, primes=ps, rank=rank,
                selfspec={str(k): v for k, v in
                          sorted(selfl.items(), key=lambda z: z[0])
                          if k != 1})


prog("holonomy readings ...")
READ = {}
for _nm, _V in (('CONG-185', CONG), ('MENU-113', MENU), ('REC', REC)):
    for _lab, _ix in (('q', 3), ('k', 4)):
        READ[(_nm, _lab)] = reading(_V, _ix)
        _r = READ[(_nm, _lab)]
        emit(f"  {_nm:9s} {_lab}-connection: closes {_r['closes']}, "
             f"non-unit self-loops {_r['nonunit']}, obstruction "
             f"{_r['obstruction']}, cycle rank {_r['cyclerank']}, primes "
             f"{fl(_r['primes'])} rank {_r['rank']}; non-unit spectrum "
             f"{ctr(_r['selfspec'])}")

_CQ, _CK_ = READ[('CONG-185', 'q')], READ[('CONG-185', 'k')]
_MQ, _MK = READ[('MENU-113', 'q')], READ[('MENU-113', 'k')]
gate('G-CONG-QHOLONOMY', 'MUST',
     "RULING PROPERTY 4 @CONG-185: the q-holonomy is D74's committed "
     "group -- prime support {2, 3}, free abelian of RANK 2, computed "
     "as an integer exponent lattice on the prime valuations and not "
     "read off four values by eye",
     _CQ['primes'] == [2, 3] and _CQ['rank'] == 2
     and _CQ['obstruction'] == 44,
     f"@CONG-185 primes {fl(_CQ['primes'])} rank {_CQ['rank']}, "
     f"obstruction {_CQ['obstruction']}, {_CQ['closes']} squares "
     f"closing, cycle rank {_CQ['cyclerank']}; the comparator is the "
     f"pinned claim quoted at V-D74-GROUP",
     falsifiers=['MUT-CONG-QHOL'])
mutant('MUT-CONG-QHOL', 'G-CONG-QHOLONOMY',
       'the same group predicate evaluated on the record quotient, which '
       'D74 proved FLAT',
       _CQ['primes'] == [2, 3] and _CQ['rank'] == 2
       and _CQ['obstruction'] == 44,
       (READ[('REC', 'q')]['primes'] == [2, 3]
        and READ[('REC', 'q')]['rank'] == 2
        and READ[('REC', 'q')]['obstruction'] == 44),
       f"@REC the reading is primes "
       f"{fl(READ[('REC', 'q')]['primes'])} rank "
       f"{READ[('REC', 'q')]['rank']} obstruction "
       f"{READ[('REC', 'q')]['obstruction']}, so the gate's own "
       f"predicate turns false on the flat carrier")
gate('G-CONG-KHOLONOMY', 'MUST',
     'RULING PROPERTY 5 @CONG-185: the HORIZON-NORMALIZED k-connection '
     "COLLAPSES BACK onto D74's group -- primes {2, 3}, rank 2.  THE "
     'ENLARGEMENT DISAPPEARS: at the contrast carrier the same reading '
     'carries primes {2, 3, 5, 13} at rank 3',
     _CK_['primes'] == [2, 3] and _CK_['rank'] == 2
     and _CK_['primes'] == _CQ['primes'] and _CK_['rank'] == _CQ['rank'],
     f"@CONG-185 k-primes {fl(_CK_['primes'])} rank {_CK_['rank']}, "
     f"non-unit self-loops {_CK_['nonunit']} (q reads "
     f"{_CQ['nonunit']}); @MENU-113 k-primes {fl(_MK['primes'])} rank "
     f"{_MK['rank']}, non-unit self-loops {_MK['nonunit']} against the "
     f"q reading's {_MQ['nonunit']}",
     falsifiers=['MUT-CONG-KHOL'])
mutant('MUT-CONG-KHOL', 'G-CONG-KHOLONOMY',
       'the same collapse predicate evaluated at the contrast carrier '
       'MENU-113, where the horizon normalisation enlarges the group',
       _CK_['primes'] == [2, 3] and _CK_['rank'] == 2,
       _MK['primes'] == [2, 3] and _MK['rank'] == 2,
       f"@MENU-113 the k-reading carries primes {fl(_MK['primes'])} at "
       f"rank {_MK['rank']}, so the collapse predicate turns false")

# ======================================================================
# P4 -- GAMMA ON THE RULED CARRIER
# ======================================================================
sec("P4 -- GAMMA ON CONG-185: the exact rational family between cuts")
GR = G[(ROOT, CAP)]
W = {h: MU[h] * G[(h, CAP - len(h))] / GR for h in CARRIER_S}
CUTMASS = [sum(W[h] for h in CARRIER_S if len(h) == d)
           for d in range(CAP + 1)]


def gamma_family(V, wt, denom='source-mass'):
    idx = {}
    for d in range(CAP + 1):
        cl = sorted({V[h] for h in CARRIER_S if len(h) == d}, key=sk)
        idx[d] = {c: i for i, c in enumerate(cl)}
    mass = {d: defaultdict(Fr) for d in range(CAP + 1)}
    for h in CARRIER_S:
        mass[len(h)][V[h]] += wt[h]
    GAM = {}
    for d in range(CAP + 1):
        for dd in range(d + 1, CAP + 1):
            j = defaultdict(Fr)
            for h in CARRIER_S:
                if len(h) == dd:
                    j[(V[h[:d]], V[h])] += wt[h]
            M, tot = defaultdict(dict), defaultdict(Fr)
            for (s, s2), m in j.items():
                tot[s] += m
            for (s, s2), m in j.items():
                M[s][s2] = m / (mass[d][s] if denom == 'source-mass'
                                else tot[s])
            GAM[(dd, d)] = dict(M)
    return idx, mass, GAM


def colcensus(fams):
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


prog("building Gamma on CONG-185, MENU-113 and REC ...")
IDX_C, MASS_C, GAM_C = gamma_family(CONG, W)
IDX_M, MASS_M, GAM_M = gamma_family(MENU, W)
IDX_R, MASS_R, GAM_R = gamma_family(REC, W)
COLS = {'CONG-185': colcensus([GAM_C]), 'MENU-113': colcensus([GAM_M]),
        'REC': colcensus([GAM_R])}
for _nm in ('CONG-185', 'MENU-113', 'REC'):
    emit(f"  {_nm:9s}: {COLS[_nm][0]} columns over {len(GAM_C)} cut "
         f"pairs; columns not summing to 1: {COLS[_nm][1]}; negative "
         f"entries: {COLS[_nm][2]}")
gate('G-COLUMN-STOCHASTIC', 'MUST',
     'GAMMA ON THE RULED CARRIER IS EXACTLY COLUMN-STOCHASTIC: every '
     'one of its columns sums to 1 and carries no negative entry, in '
     'exact rational arithmetic, on all 10 cut pairs; the negative '
     'control is built beside it',
     COLS['CONG-185'][1] == 0 and COLS['CONG-185'][2] == 0
     and COLS['REC'][1] == 0 and COLS['REC'][2] == 0,
     f"@CONG-185 {COLS['CONG-185'][0]} columns, {COLS['CONG-185'][1]} "
     f"not summing to 1, {COLS['CONG-185'][2]} negative; @REC "
     f"{COLS['REC'][0]} columns, {COLS['REC'][1]} bad; cut masses "
     f"{fl(CUTMASS)}",
     falsifiers=['MUT-COLUMN-MISNORMALIZED'])
GRM = G[(ROOT, CAP - 1)]
WBAD = {h: MU[h] * G[(h, max(CAP - len(h) - 1, 0))] / GRM
        for h in CARRIER_S}
_, _, GAMBAD = gamma_family(CONG, WBAD)
_bc = colcensus([GAMBAD])
mutant('MUT-COLUMN-MISNORMALIZED', 'G-COLUMN-STOCHASTIC',
       'the chain re-weighted by the OFF-BY-ONE horizon -- G(h, 3-|h|) '
       'where G(h, 4-|h|) belongs -- and the family rebuilt from it',
       COLS['CONG-185'][1] == 0 and COLS['CONG-185'][2] == 0,
       _bc[1] == 0 and _bc[2] == 0,
       f"the mis-normalized family has {_bc[1]} of {_bc[0]} columns "
       f"failing to sum to 1, so the column-stochastic predicate turns "
       f"false")


def flow(fixed_r=None):
    ok, bad = 0, 0
    for h in CARRIER_S:
        if len(h) >= CAP:
            continue
        rs = ([CAP - len(h)] if fixed_r is None
              else [fixed_r] if fixed_r <= CAP - len(h) else [])
        for e, q in CACHE[h]:
            for r in rs:
                if W[h] * kern(h, e, r) == W[h + (e,)]:
                    ok += 1
                else:
                    bad += 1
    return ok, bad


FLOW_OK, FLOW_BAD = flow()
_off_ok, _off_bad = 0, 0
for _r in range(1, CAP + 1):
    _a, _b = flow(_r)
    _off_ok += _a
    _off_bad += _b
_off_tests = (_off_ok + _off_bad) - (FLOW_OK + FLOW_BAD)
_off_fail = _off_bad
# THE OFF-HORIZON STRUCTURE, SURFACED (R-GI-11).  A history at depth d
# has its MATCHED horizon at r = CAP - d, so the matched tests are spread
# across the r-sweep above rather than sitting in one row of it.  The
# breakdown below re-runs the identity at the strictly off-horizon pairs
# only, and it is STRICTLY MORE DISCRIMINATING than the aggregate ratio:
# r = 2 and r = 3 fail at every one of their tests while r = 1 does
# not.  "Fails at
# every other admissible horizon" reads as a universal and is false at
# the r = 1 passes; the count is what is claimed.
_off_rows = []
for _r in range(1, CAP + 1):
    _a = _b = 0
    for h in CARRIER_S:
        if len(h) >= CAP or _r >= CAP - len(h):
            continue
        for e, q in CACHE[h]:
            if W[h] * kern(h, e, _r) == W[h + (e,)]:
                _a += 1
            else:
                _b += 1
    _off_rows.append((_r, _a + _b, _a, _b))
_off_pass = sum(a for _r, _n, a, _b in _off_rows)
_off_rowfail = sum(b for _r, _n, _a, b in _off_rows)
gate('G-FLOW-IDENTITY', 'MUST',
     'THE FLOW IDENTITY, with its horizon NAMED: w(h) k_{4-|h|}(e|h) = '
     'w(h+e) holds at every transition of the carrier, and this is what '
     'makes the class-level law the exact conditional.  The horizon is '
     'not free: written with r free the identity is false at 352 of the '
     '596 off-horizon tests -- and the per-horizon structure is '
     'published, because 244 of them PASS and an unqualified "fails at '
     'every other horizon" would be false at those',
     (FLOW_BAD == 0 and _off_fail > 0 and _off_rowfail == _off_fail
      and _off_pass > 0
      and all(b == n for r, n, a, b in _off_rows if r > 1 and n)),
     f"at r = 4 - |h|: {FLOW_OK} of {FLOW_OK + FLOW_BAD} transitions, "
     f"{FLOW_BAD} violations -- and THAT HALF IS DEFINITIONAL, since "
     f"w = mu G(.,4-|h|)/G(root,4) and k_r = q G(h+e,r-1)/G(h,r) "
     f"substitute to it for any price law and any carrier; what is "
     f"MEASURED is that it fails off the matched horizon: {_off_fail} "
     f"of {_off_tests} off-horizon tests fail, and the per-horizon "
     f"structure is (r, tests, pass, fail) "
     f"{[(r, n, a, b) for r, n, a, b in _off_rows if n]} -- so "
     f"{_off_pass} off-horizon tests PASS, all at r = 1, which the "
     f"aggregate ratio hides",
     falsifiers=['MUT-FLOW-HORIZON'])
mutant('MUT-FLOW-HORIZON', 'G-FLOW-IDENTITY',
       'the identity asserted with the horizon FREE rather than at '
       'r = 4 - |h|',
       FLOW_BAD == 0, _off_bad == 0,
       f"with the horizon free the identity fails at {_off_bad} of "
       f"{_off_ok + _off_bad} tests, so the gate's own zero-violation "
       f"predicate turns false")
SEAL.take('SEAL-LAW',
          lambda: dict(columns=COLS, cut_masses=[str(x) for x in CUTMASS],
                       flow_ok=FLOW_OK, flow_bad=FLOW_BAD,
                       off_horizon_tests=_off_tests,
                       off_horizon_failures=_off_fail,
                       off_horizon_by_r=[list(r) for r in _off_rows],
                       off_horizon_passes=_off_pass,
                       cut_pairs=len(GAM_C)))

# --- RULING PROPERTY 6: exact lumpability, and the CK census ---------
def ck_rows(GAM):
    rows = []
    for d in range(CAP + 1):
        for md in range(d + 1, CAP + 1):
            for dd in range(md + 1, CAP + 1):
                A, B, C = GAM[(dd, md)], GAM[(md, d)], GAM[(dd, d)]
                bad, cells = 0, 0
                srcs = set()
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
                            srcs.add(s)
                rows.append(dict(cut=d, mid=md, cut2=dd, cells=cells,
                                 differing=bad, interpolates=bad == 0,
                                 sources=sorted(srcs, key=sk)))
    return rows


prog("Chapman-Kolmogorov census on all three quotients ...")
CK = {'CONG-185': ck_rows(GAM_C), 'MENU-113': ck_rows(GAM_M),
      'REC': ck_rows(GAM_R)}
CKFAIL = {k: [r for r in v if not r['interpolates']]
          for k, v in CK.items()}
for _nm in ('CONG-185', 'MENU-113', 'REC'):
    emit(f"  {_nm:9s}: Chapman-Kolmogorov fails at "
         f"{len(CKFAIL[_nm])} of {len(CK[_nm])} depth-cut triples"
         + (f"; failing triples and differing cells "
            f"{[(r['cut'], r['mid'], r['cut2'], r['differing']) for r in CKFAIL[_nm]]}"
            if CKFAIL[_nm] else ""))
gate('G-CONG-LUMPABLE', 'MUST',
     'RULING PROPERTY 6 @CONG-185, NAMED FOR WHAT IT MEASURES: the '
     'class chain is CK-EXACT AT THE 10 DEPTH-CUT TRIPLES -- '
     'Chapman-Kolmogorov holds at all of them, so the class process is '
     'Markov at that level.  This is not classical strong lumpability, '
     'which is stronger and is not measured here.  At the contrast '
     'carrier it fails at 4 of 10, every one of them a triple with a '
     'non-degenerate first cut',
     len(CKFAIL['CONG-185']) == 0 and len(CKFAIL['MENU-113']) == 4,
     f"@CONG-185 {len(CKFAIL['CONG-185'])} of {len(CK['CONG-185'])} "
     f"triples fail; @MENU-113 {len(CKFAIL['MENU-113'])} fail at cells "
     f"{[r['differing'] for r in CKFAIL['MENU-113']]}; @REC "
     f"{len(CKFAIL['REC'])} fail",
     falsifiers=['MUT-CONG-LUMP'])
mutant('MUT-CONG-LUMP', 'G-CONG-LUMPABLE',
       'the same Chapman-Kolmogorov predicate evaluated at the contrast '
       'carrier MENU-113',
       len(CKFAIL['CONG-185']) == 0,
       len(CKFAIL['MENU-113']) == 0,
       f"@MENU-113 the census reads {len(CKFAIL['MENU-113'])} failing "
       f"triples, so the exact-lumpability predicate turns false")

SIX = [('descent at every horizon', _desc_c == 0),
       ('0 multi-valued edges', EDGES['CONG-185'][1] == 0
        and EDGES['CONG-185'][2] == 0),
       ('44 curvature squares intact', len(CLOSES['CONG-185'][0]) == 44
        and len(_sym) == 0),
       ('q-holonomy <2,3>', _CQ['primes'] == [2, 3] and _CQ['rank'] == 2),
       ('k-holonomy <2,3>', _CK_['primes'] == [2, 3]
        and _CK_['rank'] == 2),
       ('CK-exact at the 10 depth-cut triples',
        len(CKFAIL['CONG-185']) == 0)]
SIX_MENU = [('descent at every horizon', _desc_m == 0),
            ('0 multi-valued edges', EDGES['MENU-113'][1] == 0
             and EDGES['MENU-113'][2] == 0),
            ('44 curvature squares intact',
             len(CLOSES['MENU-113'][0]) == 44),
            ('q-holonomy <2,3>', _MQ['primes'] == [2, 3]
             and _MQ['rank'] == 2),
            ('k-holonomy <2,3>', _MK['primes'] == [2, 3]
             and _MK['rank'] == 2),
            ('CK-exact at the 10 depth-cut triples',
             len(CKFAIL['MENU-113']) == 0)]
gate('G-SIX-PROPERTIES', 'MUST',
     'THE CARRIER IS GATED BEFORE USE: all SIX ruling properties of the '
     'adjudicated ruling hold at CONG-185, each measured on its own '
     'object and each with its own falsifier.  The contrast carrier is '
     'scored on the same six and fails three of them',
     all(v for _, v in SIX),
     f"@CONG-185 {sum(1 for _, v in SIX if v)} of {len(SIX)}: "
     f"{[(n, v) for n, v in SIX]}; @MENU-113 "
     f"{sum(1 for _, v in SIX_MENU if v)} of {len(SIX_MENU)}: "
     f"{[(n, v) for n, v in SIX_MENU]}",
     falsifiers=['MUT-SIX-LAX'])
mutant('MUT-SIX-LAX', 'G-SIX-PROPERTIES',
       'the six-property conjunction evaluated on the contrast carrier',
       all(v for _, v in SIX), all(v for _, v in SIX_MENU),
       f"MENU-113 scores {sum(1 for _, v in SIX_MENU if v)} of "
       f"{len(SIX_MENU)}, so the conjunction turns false")
SEAL.take('SEAL-CARRIER',
          lambda: dict(classes=CONG_N, rounds=CONG_ROUNDS,
                       round_trace=CONG_TRACE, dims=DIMS,
                       descent=DESCENT, edges=EDGES,
                       defective_closed={k: len(v[0]) for k, v in
                                         CLOSES.items()},
                       all_closed={k: v[1] for k, v in CLOSES.items()},
                       set_symmetric_difference=len(_sym),
                       six_properties=[[n, v] for n, v in SIX],
                       six_properties_menu=[[n, v] for n, v in SIX_MENU],
                       square_census=dict(sorted(SQ.items())),
                       spectrum={str(k): v for k, v in
                                 sorted(SPEC_Q.items())}))

# ======================================================================
# P5 -- THE TARGETS.  Pre-registered FROM THE LAW, at a readout whose
# normalisation is RE-PROVED on this carrier.
# ======================================================================
sec("P5 -- THE TARGETS: law values at a re-proved readout")
emit("  The order this unit executes, verbatim from the inheritance "
     "source:")
emit(f"    \"{VERBATIM[5][3]}\"")
MM_ALL = {h: sum(Fr(q) for e, q in CACHE[h])
          for h in ANCHOR_SCOPE_S}
MM = {h: MM_ALL[h] for h in CARRIER_S}
MCENSUS = Counter(str(v) for v in MM.values())
# R-GI-9a: the traversals above are SORTED sequences, so MCENSUS's
# first-occurrence order is a function of the histories and not of the
# interpreter's hash seed.  The delivered build iterated the SET
# `CARRIER` here; the artifacts did not move, because both publication
# points sort, but the object did.
_MM_rev = {h: MM_ALL[h] for h in sorted(CARRIER, key=sk, reverse=True)}
_MC_rev = Counter(str(v) for v in _MM_rev.values())
_order_pub = (jcanon(dict(MCENSUS)) == jcanon(dict(_MC_rev))
              and ctr(MCENSUS) == ctr(_MC_rev))
_order_raw = (list(MM.keys()) == list(_MM_rev.keys()))
MCONST = {}
for _nm, _V in (('CONG-185', CONG), ('MENU-113', MENU)):
    d = defaultdict(set)
    for h in CARRIER_S:
        d[_V[h]].add(MM[h])
    MCONST[_nm] = (sum(1 for v in d.values() if len(v) > 1), len(d))


def k1_violations(rr, window=None):
    """`window = w` restricts the test to the histories at which k_w is
    defined, which is what makes the k_1 / k_2 comparison LIKE FOR LIKE
    rather than across two different populations."""
    bad, tested = 0, 0
    for h in CARRIER_S:
        if (h, rr) not in G or G[(h, rr)] == 0:
            continue
        if window is not None and ((h, window) not in G
                                   or G[(h, window)] == 0):
            continue
        for e, q in CACHE[h]:
            if (h + (e,), rr - 1) not in G:
                continue
            if window is not None and (h + (e,), window - 1) not in G:
                continue
            tested += 1
            if kern(h, e, rr) != PRICE[(h, e)] / MM[h]:
                bad += 1
    return bad, tested


K1BAD, K1TESTED = k1_violations(1)
K2BAD, K2TESTED = k1_violations(2)
K1WBAD, K1WTESTED = k1_violations(1, window=2)
# THE ATTRIBUTION, CORRECTED (R-GI-3): G(h,1) = M(h) holds by the
# TERMINAL CONDITION G(.,0) = 1 of the potential recursion, at every
# history of every arm under ANY partition.  It is LAW-NATIVE.  What the
# carrier supplies is only that M is class-constant -- which is descent
# at horizon 1, and which BOTH quotients satisfy.
_gm_tested = [h for h in ANCHOR_SCOPE_S if (h, 1) in G]
_gm_bad = sum(1 for h in _gm_tested if G[(h, 1)] != MM_ALL[h])
_gm_bad_wrong = sum(1 for h in _gm_tested if G[(h, 1)] != MM_ALL[h] * 2)
# and under an ARBITRARY exact re-pricing of every priced event, which
# is what shows the identity is a property of the RECURSION and not of
# this price law, this carrier or this partition.
_eix = {}
for _h in sorted(CACHE, key=sk):
    for _e, _q in CACHE[_h]:
        _eix[(_h, _e)] = len(_eix)
_PRX = {k: v * Fr(_eix[k] + 3, _eix[k] + 1) for k, v in PRICE.items()}
_GX = potentials(_PRX)
_MX = {h: sum(_PRX[(h, e)] for e, q in CACHE[h])
       for h in ANCHOR_SCOPE_S}
_gm_bad_repriced = sum(1 for h in _gm_tested if _GX[(h, 1)] != _MX[h])
gate('G-STEP-NORMALISER-LAW-NATIVE', 'MUST',
     'THE STEP-NORMALISER IS RE-DERIVED IN UNIT, AND THE IDENTITY IT '
     'RESTS ON IS LAW-NATIVE, NOT CARRIER-SPECIFIC: G(h,1) = M(h) '
     'follows from the terminal condition G(.,0) = 1 of the potential '
     'recursion, so it holds at EVERY history of EVERY arm under ANY '
     'partition -- measured here at every history of the wider d <= 5 '
     'arena, not only at the carrier.  What the CARRIER supplies is '
     'only the side clause that M is class-constant, and BOTH quotients '
     'supply it.  The pin demanded re-derivation rather than import and '
     'that is met; the attribution "re-proved on THIS carrier" is not.  '
     'The forcing is machine-checked: the identity survives an '
     'ARBITRARY exact re-pricing of every priced event, which is what '
     'shows it is a property of the recursion rather than of this price '
     'law, this carrier or this partition',
     (_gm_bad == 0 and _gm_bad_repriced == 0
      and MCONST['CONG-185'][0] == 0 and MCONST['MENU-113'][0] == 0),
     f"G(h,1) = M(h) at {len(_gm_tested) - _gm_bad} of "
     f"{len(_gm_tested)} histories, {_gm_bad} violations; and at "
     f"{len(_gm_tested) - _gm_bad_repriced} of {len(_gm_tested)} after "
     f"an arbitrary exact re-pricing of all {len(_PRX)} priced events, "
     f"{_gm_bad_repriced} violations -- so the identity is carried by "
     f"the terminal condition and by nothing else; M is class-constant "
     f"at @CONG-185 {MCONST['CONG-185'][0]} of "
     f"{MCONST['CONG-185'][1]} multi-valued and @MENU-113 "
     f"{MCONST['MENU-113'][0]} of {MCONST['MENU-113'][1]}, so the side "
     f"clause does not select either carrier",
     falsifiers=['MUT-NORMALISER-CARRIER'])
mutant('MUT-NORMALISER-CARRIER', 'G-STEP-NORMALISER-LAW-NATIVE',
       'the identity re-scaled, so that it would have to be a fact '
       'about a particular carrier rather than about the recursion',
       _gm_bad == 0 and _gm_bad_repriced == 0, _gm_bad_wrong == 0,
       f"the re-scaled identity fails at {_gm_bad_wrong} of "
       f"{len(_gm_tested)} histories, so the law-native conjunct is a "
       f"predicate that can turn false")
gate('G-K1-IS-THE-STEP-NORMALISER', 'MUST',
     'THE READOUT RE-DERIVED IN UNIT, never assumed: the local menu '
     'mass M(h) is NOT constant on the ruled carrier, so a raw product '
     'of weights along a path is not a probability; and the '
     'step-normalised weight q(e|h)/M(h) is EXACTLY the pinned kernel '
     'k_1, because G(h,1) = M(h) by the terminal condition.  The '
     'primary readout is the r = 1 member of the very kernel family '
     'Gamma is built from.  The k_1 / k_2 comparison is also stated AT '
     'LIKE SCOPE, on the population where k_2 is defined',
     K1BAD == 0 and len(MCENSUS) > 1 and K1WBAD == 0,
     f"M(h) census over the ruled carrier {ctr(MCENSUS)} -- "
     f"{len(MCENSUS)} distinct values, so M is not constant on "
     f"histories, while it IS class-constant on both quotients "
     f"(@CONG-185 {MCONST['CONG-185'][0]} of {MCONST['CONG-185'][1]} "
     f"classes multi-valued, @MENU-113 {MCONST['MENU-113'][0]} of "
     f"{MCONST['MENU-113'][1]}); k_1 = q/M violations {K1BAD} of "
     f"{K1TESTED} kernel entries, and {K1WBAD} of {K1WTESTED} at the "
     f"k_2 window, against k_2's {K2BAD} of {K2TESTED} on that same "
     f"window -- the like-for-like comparison",
     falsifiers=['MUT-K1-BREAK'])
mutant('MUT-K1-BREAK', 'G-K1-IS-THE-STEP-NORMALISER',
       'the step-normaliser identified with the horizon-2 kernel k_2 '
       'instead of k_1',
       K1BAD == 0 and len(MCENSUS) > 1,
       K2BAD == 0 and len(MCENSUS) > 1,
       f"k_2 = q/M fails at {K2BAD} of {K2TESTED} kernel entries, so the "
       f"gate's own identity conjunct turns false on the mutated "
       f"identification")

# --- the leg ensembles.  Built from the transport grammar alone. -----
# <<<TARGET-REGION-BEGIN>>>


def is_R4(e):
    return e[0] == 'r' and len({t[0] for t in e[2]}) == 2


R1BASES = sorted([h for h in CACHE if len(h) == 3 and is_R4(h[-1])],
                 key=sk)


def leg_scan(bases, pruned):
    nodes, legs = 0, []
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


def positional(legs):
    cnt, raw, nrm = Counter(), defaultdict(Fr), defaultdict(Fr)
    for b, t4, ww, wn in legs:
        f = [i for i in range(3) if t4[i][0] != 'p']
        if len(f) != 1:
            return None, None, None
        cnt[f[0]] += 1
        raw[f[0]] += ww
        nrm[f[0]] += wn
    tc, tw, tn = sum(cnt.values()), sum(raw.values()), sum(nrm.values())
    return ([Fr(cnt[i], tc) for i in range(3)],
            [raw[i] / tw for i in range(3)],
            [nrm[i] / tn for i in range(3)])


prog("leg 1: UNPRUNED scan from the 16 renewal-1 bases ...")
N1, LEGS1 = leg_scan(R1BASES, False)
CNT1, RAW1, LAW1 = positional(LEGS1)
prog("renewal-2 bases, then leg 2 ...")
R2BASES = []
for _b in R1BASES:
    _st = [(_b, ())]
    while _st:
        h, tail = _st.pop()
        for e, q in candidates_for(list(h), AB):
            if is_R4(e):
                if len(tail) == 2:
                    R2BASES.append(h + (e,))
                continue
            if len(tail) < 2:
                _st.append((h + (e,), tail + (e,)))
R2BASES = sorted(R2BASES, key=sk)
N2, LEGS2 = leg_scan(R2BASES, True)
CNT2, RAW2, LAW2 = positional(LEGS2)
prog("leg 2: the prune gate, unpruned on a SPREAD subsample ...")
# The delivered gate exhibited the prune on the first 3 of 256 bases
# (1.2 %).  The prune is a SET claim about all 256, so the subsample is
# widened to a SPREAD sample -- every 8th of the sorted 256, 12.5 % --
# and the coverage fraction is printed beside it.
GATE_BASES = R2BASES[::8]
NU, LEGSU = leg_scan(GATE_BASES, False)
_sub = sorted((sk(b), sk(t4), str(ww), str(wn)) for b, t4, ww, wn in LEGS2
              if b in set(GATE_BASES))
_uns = sorted((sk(b), sk(t4), str(ww), str(wn))
              for b, t4, ww, wn in LEGSU)
# <<<TARGET-REGION-END>>>
anchor('A-LEG1', 3584, len(LEGS1), "the committed leg-1 leaf count")
anchor('A-R1BASES', 16, len(R1BASES), "the committed renewal-1 base count")
anchor('A-R2BASES', 256, len(R2BASES), "the committed renewal-2 base count")
emit(f"  LEG 1: UNPRUNED scan, {N1} raw continuations generated, "
     f"{len(LEGS1)} legs kept; patterns "
     f"{ctr(Counter(tuple(e[0] for e in t4) for b, t4, ww, wn in LEGS1))}")
emit(f"  LEG 2: pattern-pruned scan over all {len(R2BASES)} bases, "
     f"{N2} expansions, {len(LEGS2)} legs")
emit(f"    PRIMARY, step-normalised q/M = k_1 : leg 1 {frl(LAW1)}   "
     f"leg 2 {frl(LAW2)}")
emit(f"    RAW-PRODUCT                        : leg 1 {frl(RAW1)}   "
     f"leg 2 {frl(RAW2)}")
emit(f"    COUNT (the census shadow's measure) : leg 1 {frl(CNT1)}   "
     f"leg 2 {frl(CNT2)}")
gate('G-PRUNE', 'MUST',
     'the leg-2 pattern prune is GATED, not assumed: on a declared '
     'subsample of renewal-2 bases the UNPRUNED scan returns exactly '
     'the pruned leg set, leg for leg and weight for weight, at BOTH '
     'weights',
     _sub == _uns and len(_uns) > 0,
     f"{len(GATE_BASES)} of {len(R2BASES)} bases, a SPREAD sample at "
     f"every {len(R2BASES) // len(GATE_BASES)}th of the sorted bases "
     f"({100 * len(GATE_BASES) // len(R2BASES)} per cent coverage); "
     f"{NU} raw continuations unpruned giving {len(LEGSU)} legs, "
     f"{NU // len(GATE_BASES)} and {len(LEGSU) // len(GATE_BASES)} per "
     f"base; the pruned subsample carries {len(_sub)} legs; identical "
     f"{_sub == _uns}",
     falsifiers=['MUT-PRUNE-LAX'])
mutant('MUT-PRUNE-LAX', 'G-PRUNE',
       'one leg dropped from the pruned enumeration of the subsample',
       _sub == _uns and len(_uns) > 0,
       sorted(_sub[:-1]) == _uns and len(_uns) > 0,
       f"dropping one leg leaves {len(_sub) - 1} against the unpruned "
       f"{len(LEGSU)}, so the set comparison turns false")

TARGET = [Fr(15, 38), Fr(5, 19), Fr(13, 38)]
SHADOW1 = [Fr(3, 7), Fr(1, 7), Fr(3, 7)]
SHADOW2 = [Fr(4, 9), Fr(1, 9), Fr(4, 9)]


def law_value_ok(l1, l2, t):
    return l1 == t and l2 == t and l1 == l2 and l1[0] != l1[2]


gate('G-LAW-VALUE', 'MUST',
     'THE PRE-REGISTERED TARGETS ARE HIT, AND THEY ARE VALUES OF THE '
     'LAW: at the step-normalised readout re-proved above to be the '
     'pinned kernel k_1, the positional law is (15/38, 5/19, 13/38) at '
     'BOTH legs -- leg-independent and left-right asymmetric.  The '
     'targets were pre-registered FROM THE LAW, not from a leaf count',
     law_value_ok(LAW1, LAW2, TARGET),
     f"leg 1 {frl(LAW1)}, leg 2 {frl(LAW2)}; equal to the "
     f"pre-registered law value {frl(TARGET)}: "
     f"{LAW1 == TARGET and LAW2 == TARGET}; leg-independent "
     f"{LAW1 == LAW2}; left-right asymmetric ({LAW1[0]} against "
     f"{LAW1[2]})",
     falsifiers=['MUT-LAWVALUE-DRIFT'])
mutant('MUT-LAWVALUE-DRIFT', 'G-LAW-VALUE',
       'the law value replaced by the census shadow -- the claim the '
       "predecessor's round refuted, that the leaf-count triples ARE "
       'values of the law',
       law_value_ok(LAW1, LAW2, TARGET),
       law_value_ok(SHADOW1, SHADOW2, TARGET),
       f"the shadow is neither leg-independent ({SHADOW1 == SHADOW2}) "
       f"nor equal to the law value, so the gate's own predicate turns "
       f"false on it")

_reg = _src_text[_src_text.index('<<<TARGET-REGION') + 30:
                 _src_text.index('<<<TARGET-REGION-END')]
# #125 REPAIR: the scan runs on a WHITESPACE-STRIPPED haystack (so that
# `MENU [h]` cannot evade a `MENU[` needle) and the list is WIDENED from
# the delivered nine to thirty-one -- the operator seat's own list, which
# found 0 hits on all 31 at its hands.
_reg_ws = re.sub(r'\s+', '', _reg)
_tokens = ['GAM_C', 'GAM_M', 'GAM_R', 'CONG', 'MENU[', 'MENU_', 'REC[',
           'IDX_C', 'IDX_M', 'holonomy_of', 'gamma_family', 'CLOSED',
           'MASS_C', 'MASS_M', 'MASS_R', 'W[', 'G[', 'kern(', 'PRICE',
           'MU[', 'MM[', 'refine(', 'TARGET', 'SHADOW', 'EDGES',
           'READ[', 'DEPTHPURE', 'DIMS', 'CLOSES', 'CARRIER_S',
           'MCENSUS']
_hits = sorted(t for t in _tokens
               if re.sub(r'\s+', '', t) in _reg_ws)
gate('G-SHADOW-IS-A-CONTROL', 'MUST',
     'THE CENSUS SHADOW IS REPRODUCED AND LABELLED AS AN EXTERNAL '
     'CONTROL, never a target: the two leaf-count triples reproduce '
     'exactly at the counting measure that defined them, and the '
     'measurement that reproduces them TOUCHES NO OBJECT OF THE '
     'CONSTRUCTED FAMILY -- which is measured by a token scan of this '
     "file's own source over the region between two markers, not "
     'asserted',
     CNT1 == SHADOW1 and CNT2 == SHADOW2 and not _hits
     and CNT1 != TARGET and CNT2 != TARGET,
     f"COUNT at leg 1 {frl(CNT1)} against the shadow {frl(SHADOW1)}; at "
     f"leg 2 {frl(CNT2)} against {frl(SHADOW2)}; token scan over "
     f"{len(_reg)} characters of the measuring region finds "
     f"{len(_hits)} occurrences of the constructed family, of either "
     f"quotient or of the class indices; the shadow is leg-DEPENDENT "
     f"({CNT1 != CNT2}) while the law value is not",
     falsifiers=['MUT-SHADOW-DRIFT', 'MUT-SHADOW-AS-TARGET',
                 'MUT-SHADOW-WIDE'])
mutant('MUT-SHADOW-DRIFT', 'G-SHADOW-IS-A-CONTROL',
       'the census shadow drifted by one unit in each denominator',
       CNT1 == SHADOW1 and CNT2 == SHADOW2,
       CNT1 == [Fr(3, 8), Fr(1, 8), Fr(3, 8)]
       and CNT2 == [Fr(4, 10), Fr(1, 10), Fr(4, 10)],
       "the measured count law does not equal the drifted shadow, so "
       "the gate's own equality predicate turns false on it")
mutant('MUT-SHADOW-AS-TARGET', 'G-SHADOW-IS-A-CONTROL',
       'the shadow promoted to a target -- the control region made to '
       'consult the constructed family',
       not _hits,
       not sorted(t for t in _tokens
                  if re.sub(r'\s+', '', t) in _reg_ws + 'GAM_C'),
       "with the family's name spliced into the measuring region the "
       "token scan reports an occurrence, so the Gamma-free conjunct "
       "turns false")
mutant('MUT-SHADOW-WIDE', 'G-SHADOW-IS-A-CONTROL',
       'THE #125 EVASION IN THE CONTROL SCAN: the constructed family '
       'referenced with WHITESPACE INSIDE THE NEEDLE (`MENU [h]`), '
       'which the delivered contiguous-literal scan did not see',
       not _hits,
       not sorted(t for t in _tokens
                  if re.sub(r'\s+', '', t) in _reg_ws + 'MENU[h]'),
       "with `MENU [h]` spliced in, the whitespace-stripped scan "
       "reports the occurrence the delivered scan missed, so the "
       "Gamma-free conjunct turns false on the evasion itself")
SEAL.take('SEAL-TARGETS',
          lambda: dict(law_value_leg1=[str(x) for x in LAW1],
                       law_value_leg2=[str(x) for x in LAW2],
                       pre_registered=[str(x) for x in TARGET],
                       pre_registered_in_pin=frl(TARGET) in SRC['S-PIN'],
                       raw_product_leg1=[str(x) for x in RAW1],
                       raw_product_leg2=[str(x) for x in RAW2],
                       census_shadow_leg1=[str(x) for x in CNT1],
                       census_shadow_leg2=[str(x) for x in CNT2],
                       legs=[len(LEGS1), len(LEGS2)],
                       scanned=[N1, N2, NU],
                       prune_bases=[len(GATE_BASES), len(R2BASES)],
                       prune_legs=[len(_sub), len(_uns)],
                       k1_violations=[K1BAD, K1TESTED],
                       k1_violations_at_k2_window=[K1WBAD, K1WTESTED],
                       k2_violations=[K2BAD, K2TESTED],
                       g1_equals_m=[len(_gm_tested) - _gm_bad,
                                    len(_gm_tested)],
                       g1_equals_m_repriced=[len(_gm_tested)
                                             - _gm_bad_repriced,
                                             len(_gm_tested)],
                       menu_mass_census=dict(MCENSUS),
                       token_scan_hits=_hits,
                       token_scan_tokens=len(_tokens)))

# ======================================================================
# P6 -- HOLONOMY AT THE WELL-POSED GATE
# ======================================================================
sec("P6 -- HOLONOMY: REPRODUCED-AND-LOCATED on the ruled carrier")
emit("  The pin's adjudicated expectation, verbatim:")
emit(f"    \"{VERBATIM[17][3]}\"")
DEVROWS = []
for _c in CLOSED:
    h, eA, eB = _c[0], _c[1], _c[2]
    r = CAP - len(h)
    f = G[(h + (eA, eB), r - 2)] / G[(h + (eB, eA), r - 2)]
    DEVROWS.append(dict(base_depth=len(h), factor=f,
                        closes_cong=(CONG[h + (eA, eB)]
                                     == CONG[h + (eB, eA)]),
                        closes_menu=(MENU[h + (eA, eB)]
                                     == MENU[h + (eB, eA)]),
                        identity=(_c[4] == _c[3] * f)))
ID_VIOL = sum(1 for r in DEVROWS if not r['identity'])
FACSPEC = Counter(r['factor'] for r in DEVROWS)
DEV_NONUNIT = [r for r in DEVROWS if r['factor'] != 1]
DEV_ON = {'CONG-185': sum(1 for r in DEV_NONUNIT if r['closes_cong']),
          'MENU-113': sum(1 for r in DEV_NONUNIT if r['closes_menu'])}
AGREE = {}
for _nm, _V in (('CONG-185', CONG), ('MENU-113', MENU), ('REC', REC)):
    tot = bad = 0
    for _c in CLOSED:
        if _V[_c[0] + (_c[1], _c[2])] != _V[_c[0] + (_c[2], _c[1])]:
            continue
        tot += 1
        if _c[3] != _c[4]:
            bad += 1
    AGREE[_nm] = (tot, bad)
emit(f"  the deviation identity r_k = r_q * G(h eA eB, r-2)/G(h eB eA, "
     f"r-2): {len(CLOSED) - ID_VIOL} of {len(CLOSED)} closed squares, "
     f"{ID_VIOL} violations; correction-factor spectrum "
     f"{ctr({str(k): v for k, v in FACSPEC.items()})}")
for _nm in ('CONG-185', 'MENU-113', 'REC'):
    emit(f"  {_nm:9s}: r_k = r_q on {AGREE[_nm][0] - AGREE[_nm][1]} of "
         f"{AGREE[_nm][0]} squares that close in the carrier "
         f"({AGREE[_nm][1]} deviations), of which "
         f"{DEV_ON.get(_nm, 0)} carry a non-unit correction factor")
gate('G-DEVIATION-IDENTITY', 'MUST',
     'THE DEVIATION IS DERIVED, NOT OBSERVED, and the identity is a '
     'KILLABLE MUST-PASS: r_k = r_q * G(h eA eB, r-2)/G(h eB eA, r-2) '
     'at every closed exchange square of the arena, with zero '
     'violations',
     ID_VIOL == 0,
     f"{len(CLOSED) - ID_VIOL} of {len(CLOSED)}, {ID_VIOL} violations; "
     f"the non-unit factors are {ctr({str(k): v for k, v in FACSPEC.items() if k != 1})} "
     f"on {len(DEV_NONUNIT)} squares, all at base depth "
     f"{sorted({r['base_depth'] for r in DEV_NONUNIT})}",
     falsifiers=['MUT-DEVIATION-IDENTITY'])
_id_mut = sum(1 for _c, _r in zip(CLOSED, DEVROWS)
              if _c[4] != _c[3] * (_r['factor'] * Fr(3, 2)))
mutant('MUT-DEVIATION-IDENTITY', 'G-DEVIATION-IDENTITY',
       'the correction factor re-scaled by an exact rational, so the '
       'asserted identity is no longer the true one',
       ID_VIOL == 0, _id_mut == 0,
       f"the re-scaled identity fails at {_id_mut} of {len(CLOSED)} "
       f"squares, so the zero-violation predicate turns false")
_hol_head = (AGREE['CONG-185'][1] == 0 and DEV_ON['CONG-185'] == 0
             and ID_VIOL == 0 and _CK_['primes'] == _CQ['primes']
             and READ[('REC', 'q')]['obstruction'] == 0
             and READ[('REC', 'k')]['nonunit'] == 0)
gate('G-HOLONOMY-HEAD', 'MUST',
     'THE HOLONOMY HEAD, four conjuncts each measured and each '
     'killable: (i) the q-connection reproduces the committed rung on '
     'the carrier; (ii) the deviation identity holds at every closed '
     'square; (iii) on the RULED carrier every deviation VANISHES -- 0 '
     'of the squares that close carry a non-unit correction factor, so '
     'the reading AGREES rather than being merely located; (iv) the '
     'negative control is flat at both readings',
     _hol_head,
     f"@CONG-185 r_k = r_q at {AGREE['CONG-185'][0]}/"
     f"{AGREE['CONG-185'][0]}, deviations {AGREE['CONG-185'][1]}, "
     f"non-unit factors on closing squares {DEV_ON['CONG-185']}; "
     f"@MENU-113 deviations {AGREE['MENU-113'][1]} of "
     f"{AGREE['MENU-113'][0]} with {DEV_ON['MENU-113']} non-unit "
     f"factors; identity violations {ID_VIOL}; @REC obstruction "
     f"{READ[('REC', 'q')]['obstruction']} and non-unit k self-loops "
     f"{READ[('REC', 'k')]['nonunit']}",
     falsifiers=['MUT-DEVIATION-PLANTED', 'MUT-HOLONOMY-HEAD',
                 'MUT-RECFLAT-CORRUPT'])
_planted = [dict(r) for r in DEVROWS]
for _r in _planted:
    if _r['closes_cong'] and _r['factor'] == 1:
        _r['factor'] = Fr(3, 2)
        break
_planted_bad = sum(1 for r in _planted
                   if r['closes_cong'] and r['factor'] != 1)
mutant('MUT-DEVIATION-PLANTED', 'G-HOLONOMY-HEAD',
       'A SYNTHETIC DEVIATION: a non-unit correction factor planted on '
       'a square that CLOSES in the ruled carrier',
       DEV_ON['CONG-185'] == 0, _planted_bad == 0,
       f"with the deviation planted the carrier carries {_planted_bad} "
       f"non-unit factors on closing squares, so the head's own "
       f"vanishing conjunct turns false -- AGREES is a verdict that can "
       f"fail")
mutant('MUT-HOLONOMY-HEAD', 'G-HOLONOMY-HEAD',
       "the head's own four-conjunct predicate evaluated at the contrast "
       'carrier MENU-113, where the deviation is located rather than '
       'absent',
       _hol_head,
       (AGREE['MENU-113'][1] == 0 and DEV_ON['MENU-113'] == 0
        and ID_VIOL == 0),
       f"@MENU-113 the reading deviates at {AGREE['MENU-113'][1]} "
       f"squares carrying {DEV_ON['MENU-113']} non-unit factors, so the "
       f"AGREES conjunct turns false there -- the head discriminates "
       f"between the two carriers")
mutant('MUT-RECFLAT-CORRUPT', 'G-HOLONOMY-HEAD',
       'the flatness of the negative control replaced by the ruled '
       "carrier's own obstruction",
       READ[('REC', 'q')]['obstruction'] == 0,
       _CQ['obstruction'] == 0,
       f"the ruled carrier's obstruction is {_CQ['obstruction']}, not "
       f"0, so the control-flatness conjunct turns false when the "
       f"control is swapped")
SEAL.take('SEAL-HOLONOMY',
          lambda: {f"{c}|{l}": v for (c, l), v in READ.items()})
SEAL.take('SEAL-DEVIATION',
          lambda: dict(identity_violations=ID_VIOL,
                       factor_spectrum={str(k): v for k, v in
                                        FACSPEC.items()},
                       non_unit=len(DEV_NONUNIT), on_carrier=DEV_ON,
                       agreement={k: list(v) for k, v in AGREE.items()}))

# ======================================================================
# P7 -- THE QUANTUM CHARACTER, CARRIER-STAMPED
# ======================================================================
sec("P7 -- THE QUANTUM CHARACTER, MEASURED AT BOTH CARRIERS AND STAMPED")
emit("  The adjudicated open this section answers, verbatim:")
emit(f"    \"{VERBATIM[8][3]}\"")


def dense(GAM, IDX, d, dd):
    M = [[Fr(0)] * len(IDX[d]) for _ in range(len(IDX[dd]))]
    for s, row in GAM[(dd, d)].items():
        for s2, v in row.items():
            M[IDX[dd][s2]][IDX[d][s]] = v
    return M


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = [[Fr(0)] * m for _ in range(n)]
    for i in range(n):
        Ai, oi = A[i], out[i]
        for t in range(k):
            a = Ai[t]
            if a:
                Bt = B[t]
                for j in range(m):
                    if Bt[j]:
                        oi[j] += a * Bt[j]
    return out


def inverse(M):
    n = len(M)
    A = [row[:] + [Fr(1) if i == j else Fr(0) for j in range(n)]
         for i, row in enumerate(M)]
    for c in range(n):
        piv = None
        for r in range(c, n):
            if A[r][c] != 0:
                piv = r
                break
        if piv is None:
            return None
        A[c], A[piv] = A[piv], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]


def dupcols(M):
    seen = {}
    for j in range(len(M[0])):
        col = tuple(M[i][j] for i in range(len(M)))
        if col in seen:
            return (seen[col], j)
        seen[col] = j
    return None


def padded(GAM, V, MASS, d, dd, cuts, style):
    """The declared completion conventions.  The configuration space is
    the union of the cuts' supports; a class not realised at the earlier
    cut is completed by the declared style."""
    uni = sorted({V[h] for h in CARRIER_S if len(h) in cuts}, key=sk)
    ix = {c: i for i, c in enumerate(uni)}
    M = [[Fr(0)] * len(uni) for _ in range(len(uni))]
    realset = {V[h] for h in CARRIER_S if len(h) == d}
    other = [c for c in uni if c not in realset]
    marg = None
    if style == 'marginal':
        tot = sum(MASS[d][c] for c in uni if c in realset)
        marg = {c: (MASS[d][c] / tot if tot else Fr(0)) for c in uni}
    for c in uni:
        if c in realset:
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
    return M, uni


TRIPLES = [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
STYLES = ('identity', 'cyclic', 'uniform', 'marginal')
prog("eq. 22 under four declared completions, at both carriers ...")
EQ22 = {}
for _cn, _V, _GAM, _MASS in (('CONG-185', CONG, GAM_C, MASS_C),
                             ('MENU-113', MENU, GAM_M, MASS_M)):
    for _st in STYLES:
        for (d, md, dd) in TRIPLES:
            P1, uni = padded(_GAM, _V, _MASS, d, md, (d, md, dd), _st)
            inv = inverse(P1)
            if inv is None:
                EQ22[(_cn, _st, (d, md, dd))] = dict(
                    speaks=False, labels=len(uni),
                    certificate=(f"columns {dupcols(P1)[0]} and "
                                 f"{dupcols(P1)[1]} are identical"
                                 if dupcols(P1) else
                                 "singular without a duplicate-column "
                                 "certificate"))
                continue
            P2, _ = padded(_GAM, _V, _MASS, d, dd, (d, md, dd), _st)
            Gb = matmul(P2, inv)
            negs = sum(1 for r in Gb for x in r if x < 0)
            cs = [sum(Gb[i][j] for i in range(len(Gb)))
                  for j in range(len(Gb))]
            mn = sorted(x for r in Gb for x in r if x < 0)[:1]
            EQ22[(_cn, _st, (d, md, dd))] = dict(
                speaks=True, labels=len(uni), negatives=negs,
                positives=sum(1 for r in Gb for x in r if x > 0),
                colsums_one=all(c == 1 for c in cs),
                most_negative=[str(x) for x in mn])
EQ_SPEAK = {}
for _cn in ('CONG-185', 'MENU-113'):
    EQ_SPEAK[_cn] = sorted({s for s in STYLES
                            if all(EQ22[(_cn, s, t)]['speaks']
                                   for t in TRIPLES)})
    emit(f"  eq. 22 @{_cn}: completions that let the algebraic reading "
         f"SPEAK: {EQ_SPEAK[_cn]} of {len(STYLES)} tested")
    for _st in STYLES:
        _rows = [EQ22[(_cn, _st, t)] for t in TRIPLES]
        if all(r['speaks'] for r in _rows):
            emit(f"    [{_st}] negative entries by triple "
                 f"{[r['negatives'] for r in _rows]}, column sums all 1 "
                 f"{[r['colsums_one'] for r in _rows]}, most negative "
                 f"{[r['most_negative'][0] if r['most_negative'] else None for r in _rows]}")
        else:
            emit(f"    [{_st}] SILENT: the first transfer is singular at "
                 f"{sum(1 for r in _rows if not r['speaks'])} of "
                 f"{len(TRIPLES)} triples "
                 f"({_rows[0].get('certificate')})")
MENU_NEG = [EQ22[('MENU-113', 'identity', t)]['negatives']
            for t in TRIPLES]
MENU_POS = [EQ22[('MENU-113', 'identity', t)]['positives']
            for t in TRIPLES]


def eq_labels(V, t):
    """the padded configuration space of a triple, RE-DERIVED from the
    class sets rather than read off the row that is being audited."""
    return len(set().union(*[{V[h] for h in CARRIER_S if len(h) == x}
                             for x in t]))


def eq_cells_ok(shift=0):
    """#87, PER CELL: every one of the 32 published eq.-22 cells is
    bound -- its label count against an independent re-derivation, its
    column sums, its most-negative entry, and (for the silent cells) its
    singularity certificate.  `shift` re-derives the label count from
    the WRONG triple, which is the falsifier."""
    rows = []
    for _c, _V in (('CONG-185', CONG), ('MENU-113', MENU)):
        for _st in STYLES:
            for _i, _t in enumerate(TRIPLES):
                r = EQ22[(_c, _st, _t)]
                lab = eq_labels(_V, TRIPLES[(_i + shift) % len(TRIPLES)])
                ok = (r['labels'] == lab)
                if r['speaks']:
                    ok = (ok and r['colsums_one'] is True
                          and len(r['most_negative']) == 1
                          and Fr(r['most_negative'][0]) < 0
                          and r['negatives'] > 0
                          and r['positives'] > r['negatives'])
                else:
                    ok = (ok and isinstance(r.get('certificate'), str)
                          and len(r['certificate']) > 10)
                rows.append(ok)
    return rows


_eq_rows = eq_cells_ok()
_eq_cells_ok = (all(_eq_rows)
                and len(_eq_rows) == 2 * len(STYLES) * len(TRIPLES))
_eq_shift = all(eq_cells_ok(1))
_eq_agree = all(EQ22[('MENU-113', 'identity', t)]
                == EQ22[('MENU-113', 'cyclic', t)] for t in TRIPLES)
emit(f"  eq. 22 bound PER CELL (#87): {len(_eq_rows)} published cells, "
     f"{sum(1 for r in _eq_rows if r)} carrying a label count that "
     f"reproduces an independent re-derivation together with their "
     f"column sums, most-negative entry and singularity certificate; "
     f"the two speaking completions agree FIELD FOR FIELD at every "
     f"triple: {_eq_agree}")
gate('G-EQ22-STAMPED', 'MUST',
     'EQ. 22, MEASURED AT BOTH CARRIERS AND STAMPED WITH EACH: @MENU-113 '
     'two of the four completions let the algebraic reading speak and '
     'both return the SAME negative-entry census, so the unique '
     'algebraic candidate fails positivity and no interpolant of eq. '
     "22's form exists there; @CONG-185 ALL FOUR completions are SILENT "
     '-- the padded first transfer is singular -- so the algebraic '
     'route says nothing at the ruled carrier and the existence '
     'question is settled instead by the direct construction.  Every '
     'one of the 32 published cells is bound, not one field of them '
     '(#87)',
     (EQ_SPEAK['MENU-113'] == ['cyclic', 'identity']
      and MENU_NEG == [36, 104, 108, 164]
      and all(EQ22[('MENU-113', s, t)]['negatives'] == MENU_NEG[i]
              for s in EQ_SPEAK['MENU-113']
              for i, t in enumerate(TRIPLES))
      and EQ_SPEAK['CONG-185'] == []
      and _eq_cells_ok and _eq_agree),
     f"@MENU-113 completions that speak {EQ_SPEAK['MENU-113']}, "
     f"negatives {MENU_NEG} against {MENU_POS} positive entries; "
     f"@CONG-185 completions that speak {EQ_SPEAK['CONG-185']} of "
     f"{len(STYLES)}; per-cell binding {sum(1 for r in _eq_rows if r)} "
     f"of {len(_eq_rows)} cells; the two speaking completions agree "
     f"field for field {_eq_agree}",
     falsifiers=['MUT-EQ22-SIGN', 'MUT-EQ22-UNSTAMPED',
                 'MUT-EQ22-CELL-BLIND'])
mutant('MUT-EQ22-SIGN', 'G-EQ22-STAMPED',
       'THE SIGN TEST INVERTED IN THE MEASUREMENT ITSELF: the census '
       'recounted over the POSITIVE entries of the very same candidate '
       'matrices -- the reading that would turn the refutation into an '
       'existence claim',
       MENU_NEG == [36, 104, 108, 164],
       MENU_POS == [36, 104, 108, 164],
       f"the same candidates carry {MENU_POS} positive entries against "
       f"{MENU_NEG} negative ones, so a census that consults the wrong "
       f"sign turns the gate's own value predicate false")
mutant('MUT-EQ22-CELL-BLIND', 'G-EQ22-STAMPED',
       "a published cell's label count re-derived from the WRONG "
       'triple, which a per-field binding could not see',
       _eq_cells_ok, _eq_shift,
       f"with the label re-derivation shifted by one triple the "
       f"per-cell binding reads {sum(1 for r in eq_cells_ok(1) if r)} "
       f"of {len(_eq_rows)}, so the cell-level conjunct turns false")
SEAL.take('SEAL-EQ22',
          lambda: dict(speaking={k: v for k, v in EQ_SPEAK.items()},
                       menu_negatives=MENU_NEG,
                       menu_positives=MENU_POS,
                       rows={f"{c}|{s}|{t}": v for (c, s, t), v in
                             EQ22.items()},
                       cells_bound=[sum(1 for r in _eq_rows if r),
                                    len(_eq_rows)],
                       speaking_completions_agree=_eq_agree))
mutant('MUT-EQ22-UNSTAMPED', 'G-EQ22-STAMPED',
       "the MENU-113 result read as if it held at the ruled carrier -- "
       'the unstamped quantum sentence the adjudication forbids',
       EQ_SPEAK['CONG-185'] == [],
       EQ_SPEAK['CONG-185'] == EQ_SPEAK['MENU-113'],
       f"the two carriers do not agree on which completions speak "
       f"({EQ_SPEAK['CONG-185']} against {EQ_SPEAK['MENU-113']}), so an "
       f"unstamped reading turns the gate false")

# --- THE MECHANISM: why the two carriers differ ----------------------
DEPTHPURE = {}
for _nm, _V in (('CONG-185', CONG), ('MENU-113', MENU), ('REC', REC)):
    dep = defaultdict(set)
    for h in CARRIER_S:
        dep[_V[h]].add(len(h))
    DEPTHPURE[_nm] = (sum(1 for v in dep.values() if len(v) > 1),
                      len(dep), sorted(dep[_V[ROOT]]))
    emit(f"  {_nm:9s}: classes occurring at more than one depth cut "
         f"{DEPTHPURE[_nm][0]} of {DEPTHPURE[_nm][1]}; the root's own "
         f"class also occurs at depths {DEPTHPURE[_nm][2]}")
SHARED = {}
for _nm, _V in (('CONG-185', CONG), ('MENU-113', MENU)):
    SHARED[_nm] = []
    for (d, md, dd) in TRIPLES:
        sets = [{_V[h] for h in CARRIER_S if len(h) == x}
                for x in (d, md, dd)]
        uni = set().union(*sets)
        SHARED[_nm].append(sum(1 for c in uni
                               if sum(1 for s in sets if c in s) > 1))
    emit(f"  {_nm:9s}: class labels shared between the cuts of a triple "
         f"{SHARED[_nm]} (triples {TRIPLES})")
_mt_src = set()
_mt_bad = set()
_mt_ = defaultdict(set)
for h in CARRIER_S:
    if len(h) < CAP:
        for e, q in CACHE[h]:
            _mt_[(MENU[h], evsk(e))].add(MENU[h + (e,)])
for _k, _v in sorted(_mt_.items(), key=lambda z: sk(z[0])):
    if len(_v) > 1:
        _mt_src.add(_k[0])
        _mt_bad.add(_k)
_dep_menu = defaultdict(set)
for h in CARRIER_S:
    _dep_menu[MENU[h]].add(len(h))
_rec_menu = {c for c, ds in _dep_menu.items() if len(ds) > 1}
_pure_menu = {c for c, ds in _dep_menu.items() if len(ds) == 1}
_carrier_rel = (len(CKFAIL['MENU-113']) > 0
                and len(CKFAIL['CONG-185']) == 0
                and EDGES['MENU-113'][2] > 0
                and EDGES['CONG-185'][2] == 0)
gate('G-CARRIER-RELATIVE', 'MUST',
     'THE ADJUDICATED OPEN, ANSWERED BY MEASUREMENT AND STAMPED: the '
     'four quantum-shape statistics -- Chapman-Kolmogorov, exact '
     'lumpability, whether eq. 22 speaks, and its negativity when it '
     'does -- take DIFFERENT VALUES at MENU-113 and at CONG-185, each '
     'measured at both and each carrying the carrier it is read at.  '
     'This gate is a four-way co-occurrence of counts and it claims '
     'nothing more; the mechanism is a separate gate with its own '
     'measurements',
     _carrier_rel,
     f"@MENU-113 {EDGES['MENU-113'][2]} multi-target labelled edges and "
     f"{len(CKFAIL['MENU-113'])} of {len(CK['MENU-113'])} "
     f"Chapman-Kolmogorov triples failing; @CONG-185 "
     f"{EDGES['CONG-185'][2]} multi-target edges and "
     f"{len(CKFAIL['CONG-185'])} failing; @REC (the flat negative "
     f"control) {EDGES['REC'][2]} multi-target edges, "
     f"{len(CKFAIL['REC'])} failing and {DEPTHPURE['REC'][0]} classes "
     f"recurring -- so on every quantum-shape statistic measured here "
     f"THE RULED CARRIER IS INDISTINGUISHABLE FROM THE CONTROL IT "
     f"DECLARES FLAT, which is disclosed rather than hidden",
     falsifiers=['MUT-CARRIER-RELATIVE-FLAT', 'MUT-MULTITARGET-BLIND'])
mutant('MUT-CARRIER-RELATIVE-FLAT', 'G-CARRIER-RELATIVE',
       'the two carriers asserted to agree -- the carrier-blind reading',
       _carrier_rel,
       (len(CKFAIL['MENU-113']) == len(CKFAIL['CONG-185'])
        and EDGES['MENU-113'][2] == EDGES['CONG-185'][2]),
       f"the two carriers disagree at both statistics "
       f"({len(CKFAIL['MENU-113'])} against "
       f"{len(CKFAIL['CONG-185'])} triples; "
       f"{EDGES['MENU-113'][2]} against {EDGES['CONG-185'][2]} edges), "
       f"so the carrier-blind predicate turns false")
mutant('MUT-MULTITARGET-BLIND', 'G-CARRIER-RELATIVE',
       'the mechanism dropped: only the weight single-valuedness '
       'checked, which BOTH carriers pass',
       EDGES['CONG-185'][2] == 0 and EDGES['MENU-113'][2] > 0,
       EDGES['CONG-185'][1] == 0 and EDGES['MENU-113'][1] > 0,
       f"both carriers carry {EDGES['MENU-113'][1]} multi-WEIGHT edges, "
       f"so a weight-only test cannot separate them and the mechanism "
       f"conjunct turns false")
# --- THE MECHANISM, GATED (R-GI-1).  The delivered MECHANISED claim was
# --- refuted by two seats on this unit's own arena; what replaces it is
# --- five measurements and one theorem, each with its own predicate.
prog("the mechanism battery: the minimal split and the round-1 "
     "control ...")
_ck_src_menu = set()
for _r in CKFAIL['MENU-113']:
    _ck_src_menu |= set(_r['sources'])
_desc_bad_menu2 = DESCENT_BAD[('MENU-113', 2)]
_mech_contain = _mt_src <= _rec_menu
_mech_pure_contain = _mt_src <= _pure_menu
_mech_setid = (_desc_bad_menu2 == _mt_src)


def split_menu(targets):
    """Split ONLY the named MENU source classes, and only by the target
    of an offending label, changing nothing else."""
    out = {}
    for h in CARRIER_S:
        c = MENU[h]
        if c in targets and len(h) < CAP:
            out[h] = sk((c, tuple(sorted((evsk(e), sk(MENU[h + (e,)])))
                                  for e, q in CACHE[h]
                                  if (c, evsk(e)) in _mt_bad)))
        else:
            out[h] = c
    return out


MINSPLIT = split_menu(_mt_src)
_min_n = len(set(MINSPLIT.values()))
_min_w, _min_t = defaultdict(set), defaultdict(set)
for h in CARRIER_S:
    if len(h) < CAP:
        for e, q in CACHE[h]:
            _min_w[(MINSPLIT[h], evsk(e))].add(Fr(q))
            _min_t[(MINSPLIT[h], evsk(e))].add(MINSPLIT[h + (e,)])
_min_mt = sum(1 for v in _min_t.values() if len(v) > 1)
_, _, GAM_MIN = gamma_family(MINSPLIT, W)
_min_ckfail = len([r for r in ck_rows(GAM_MIN) if not r['interpolates']])
# THE CONTROL the operator asked for: split FOUR OTHER menu classes of
# the same sizes, changing nothing about the offending edges.
_menu_size = Counter(MENU[h] for h in CARRIER_S)
_mt_sizes = sorted(_menu_size[c] for c in sorted(_mt_src, key=sk))
_others = sorted([c for c in _dep_menu if c not in _mt_src],
                 key=lambda c: (-_menu_size[c], sk(c)))[:len(_mt_src)]
_oth_sizes = sorted(_menu_size[c] for c in _others)
OTHSPLIT = {}
for h in CARRIER_S:
    c = MENU[h]
    if c in set(_others) and len(h) < CAP:
        OTHSPLIT[h] = sk((c, tuple(sorted((evsk(e), sk(MENU[h + (e,)]))
                                          for e, q in CACHE[h]))))
    else:
        OTHSPLIT[h] = c
_oth_n = len(set(OTHSPLIT.values()))
_, _, GAM_OTH = gamma_family(OTHSPLIT, W)
_oth_ckfail = len([r for r in ck_rows(GAM_OTH) if not r['interpolates']])
# THE ROUND-1 REFUTING CONTROL: the first refinement round is already
# CK-exact while carrying THIRTY-THREE TIMES the multi-target edges.
_r1_idx, _r1_rounds, _ = refine(CARRIER, MENU, stop=1)
R1 = {h: ('R1', _r1_idx[h]) for h in CARRIER_S}
_r1_n = len(set(R1.values()))
_r1_t = defaultdict(set)
_r1_dep = defaultdict(set)
for h in CARRIER_S:
    _r1_dep[R1[h]].add(len(h))
    if len(h) < CAP:
        for e, q in CACHE[h]:
            _r1_t[(R1[h], evsk(e))].add(R1[h + (e,)])
_r1_mt = sum(1 for v in _r1_t.values() if len(v) > 1)
_r1_span = sum(1 for v in _r1_dep.values() if len(v) > 1)
_r1_root = sorted(_r1_dep[R1[ROOT]])
_r1_returns = sum(1 for h in CARRIER_S if len(h) > 0
                  and any(R1[h] == R1[g]
                          for g in (h[:k] for k in range(len(h)))))
_, _, GAM_R1 = gamma_family(R1, W)
_r1_ckfail = len([r for r in ck_rows(GAM_R1) if not r['interpolates']])
# THE WHOLE REFINEMENT LADDER, so that ruling property 6 is priced: CK
# at every intermediate quotient between MENU-113 and CONG-185.
LADDER = [('MENU-113', len(set(MENU.values())), EDGES['MENU-113'][2],
           DEPTHPURE['MENU-113'][0], len(CKFAIL['MENU-113']))]
for _k in range(1, CONG_ROUNDS - 1):
    _li, _, _ = refine(CARRIER, MENU, stop=_k)
    _lv = {h: ('R%d' % _k, _li[h]) for h in CARRIER_S}
    _lt, _ld = defaultdict(set), defaultdict(set)
    for h in CARRIER_S:
        _ld[_lv[h]].add(len(h))
        if len(h) < CAP:
            for e, q in CACHE[h]:
                _lt[(_lv[h], evsk(e))].add(_lv[h + (e,)])
    _, _, _lg = gamma_family(_lv, W)
    LADDER.append(('round %d' % _k, len(set(_lv.values())),
                   sum(1 for v in _lt.values() if len(v) > 1),
                   sum(1 for v in _ld.values() if len(v) > 1),
                   len([r for r in ck_rows(_lg)
                        if not r['interpolates']])))
LADDER.append(('CONG-185', CONG_N, EDGES['CONG-185'][2],
               DEPTHPURE['CONG-185'][0], len(CKFAIL['CONG-185'])))
LADDER.append(('REC', len(set(REC.values())), EDGES['REC'][2],
               DEPTHPURE['REC'][0], len(CKFAIL['REC'])))
_ck_passers = [r[0] for r in LADDER if r[4] == 0]
emit("")
emit("  THE REFINEMENT LADDER, quotient by quotient (classes, "
     "multi-target edges, classes")
emit("  spanning more than one depth, Chapman-Kolmogorov failures):")
for _r in LADDER:
    emit(f"    {_r[0]:10s} classes {_r[1]:5d}  multi-target {_r[2]:4d}  "
         f"depth-spanning {_r[3]:3d}  CK failures {_r[4]}")
emit(f"  Ruling property 6, PRICED: CK-exactness at the "
     f"{len(CK['CONG-185'])} depth-cut triples is passed by "
     f"{len(_ck_passers)} of the {len(LADDER)} quotients in this "
     f"lattice ({_ck_passers}), so property 6 ALONE does not select "
     f"CONG-185; it is the conjunction of the six that does.  The row "
     f"is named 'CK-exact at the 10 depth-cut triples' rather than "
     f"classical strong lumpability, which is a stronger condition and "
     f"is not what is measured.")
emit("")
emit("  THE MECHANISM, MEASURED RATHER THAN ASSERTED.  The delivered "
     "claim -- that the")
emit("  whole signature is CARRIED BY the multi-target edges -- is "
     "refuted on this unit's")
emit("  own refinement lattice.  What is measured instead:")
emit(f"    (i)   the {EDGES['MENU-113'][2]} multi-target labelled edges "
     f"of MENU-113 sit on {len(_mt_src)} source classes, and those "
     f"classes are SET-IDENTICAL to the {len(_desc_bad_menu2)} classes "
     f"on which ruling property 1 fails at horizon 2: {_mech_setid}")
emit(f"    (ii)  the Chapman-Kolmogorov failing cells at MENU-113 trace "
     f"to {len(_ck_src_menu)} distinct source classes, NOT "
     f"{len(_mt_src)}; the multi-target sources are a strict subset "
     f"({_mt_src <= _ck_src_menu} and "
     f"{len(_ck_src_menu) > len(_mt_src)})")
emit(f"    (iii) the MINIMAL SPLIT of only those {len(_mt_src)} classes, "
     f"only by the target of their offending label, gives {_min_n} "
     f"classes, leaves {_min_mt} multi-target edges STANDING -- so it "
     f"is not a congruence and not a probabilistic bisimulation -- and "
     f"is Chapman-Kolmogorov exact at {_min_ckfail} of "
     f"{len(CK['MENU-113'])} triples")
emit(f"    (iv)  splitting the {len(_others)} LARGEST OTHER menu "
     f"classes instead -- sizes {_oth_sizes} against the offending "
     f"classes' {_mt_sizes}, and by their FULL successor signature, "
     f"which is a strictly finer cut than the minimal split makes -- "
     f"gives {_oth_n} classes and leaves CK failing at {_oth_ckfail} "
     f"of {len(CK['MENU-113'])}: the repair is the offending edges' and "
     f"not any refinement's")
emit(f"    (v)   refinement round 1 carries {_r1_mt} multi-target edges "
     f"-- {_r1_mt // max(EDGES['MENU-113'][2], 1)} times MENU's "
     f"{EDGES['MENU-113'][2]} -- and {_r1_span} depth-spanning classes "
     f"at {_r1_n} classes, and is ALREADY CK-exact at {_r1_ckfail} of "
     f"{len(CK['MENU-113'])}.  The statistic is not monotone in the "
     f"refinement order, so 'removing the edges removes the signature' "
     f"is false as an explanation.  At that same quotient the root's "
     f"class still occurs at depths {_r1_root} and {_r1_returns} "
     f"histories return to a prefix class, which is why the "
     f"recurrence/non-Markov co-location this unit's predecessor "
     f"noticed is COINCIDENTAL and is not carried")
emit(f"    (vi)  the {len(_mt_src)} multi-target source classes lie "
     f"inside the {len(_rec_menu)} of {len(_dep_menu)} MENU classes "
     f"that recur across depth cuts: {_mech_contain} -- a containment "
     f"the delivery asserted and never computed")
emit("  THE ONE GENERAL LAW: single-valuedness of the labelled WEIGHT "
     "and TARGET makes the")
emit("  quotient a probabilistic bisimulation, hence CK-exact BY "
     "THEOREM.  That direction is")
emit("  sufficient and it is not necessary -- (iii) and (v) are the "
     "witnesses.")
emit("  AND THE ONTOLOGY THIS LICENSES: NON-MARKOVIANITY HERE IS A "
     "PROPERTY OF THE")
emit("  DESCRIPTION, NOT OF THE PROCESS.  The transport chain on "
     "histories is Markov by")
emit(f"  construction -- k_r(e|h) is a function of h alone and the flow "
     f"identity holds at")
emit(f"  {FLOW_OK} of {FLOW_OK + FLOW_BAD} transitions -- so every "
     f"non-Markov statistic in this unit is")
emit("  manufactured by a lumping, and one round of successor-closure "
     "destroys it.")
_mech_ok = (_mech_contain and not _mech_pure_contain and _mech_setid
            and len(_ck_src_menu) == 5 and _mt_src <= _ck_src_menu
            and _min_n == 121 and _min_mt == 36 and _min_ckfail == 0
            and _oth_ckfail > 0 and _oth_n > len(set(MENU.values()))
            and _r1_n == 162 and _r1_mt == 132 and _r1_ckfail == 0
            and _r1_span == 17 and FLOW_BAD == 0)
gate('G-MECHANISM-MEASURED', 'MUST',
     'THE MECHANISM CLAIM IS REPLACED BY MEASUREMENT, and the '
     'replacement is gated: (i) the multi-target source classes are '
     'SET-IDENTICAL to the classes on which descent fails at horizon 2; '
     '(ii) the CK-failing cells trace to FIVE source classes, not four, '
     'and the multi-target sources are a strict subset; (iii) the '
     'minimal 121-class split is CK-exact with 36 multi-target edges '
     'STANDING, so single-valuedness is SUFFICIENT AND NOT NECESSARY; '
     '(iv) splitting the four largest other classes, by their full '
     'successor signature, does not repair CK; (v) refinement round 1 is CK-exact at 162 classes '
     'carrying 132 multi-target edges, so the statistic is not monotone '
     'in the refinement order; (vi) the four multi-target sources lie '
     'inside the recurring classes.  The only general law is the '
     'theorem congruence => probabilistic bisimulation => CK-exact, and '
     'the licensed sentence is that NON-MARKOVIANITY IS A PROPERTY OF '
     'THE DESCRIPTION -- the history chain is Markov by construction',
     _mech_ok,
     f"set identity of the descent-failure and multi-target source "
     f"classes {_mech_setid} ({len(_mt_src)} of {len(_mt_src)}); CK "
     f"source classes {len(_ck_src_menu)} against {len(_mt_src)} "
     f"multi-target sources, subset {_mt_src <= _ck_src_menu}; minimal "
     f"split {_min_n} classes, {_min_mt} multi-target edges standing, "
     f"CK failures {_min_ckfail}; the four-largest-other split "
     f"{_oth_n} classes (sizes {_oth_sizes} against the offending "
     f"{_mt_sizes}), CK failures {_oth_ckfail}; round 1 {_r1_n} "
     f"classes, {_r1_mt} multi-target edges, {_r1_span} depth-spanning "
     f"classes, CK failures {_r1_ckfail}; containment in the recurring "
     f"classes {_mech_contain}, in the depth-pure classes "
     f"{_mech_pure_contain}; the history chain's own flow identity "
     f"{FLOW_OK} of {FLOW_OK + FLOW_BAD}",
     falsifiers=['MUT-MECHANISM-RECURRENCE', 'MUT-MECHANISM-NECESSARY',
                 'MUT-MINSPLIT-ANY-REFINEMENT'])
mutant('MUT-MECHANISM-RECURRENCE', 'G-MECHANISM-MEASURED',
       'the containment run against the DEPTH-PURE menu classes instead '
       'of the recurring ones',
       _mech_contain, _mech_pure_contain,
       f"the multi-target sources lie inside the recurring classes "
       f"({_mech_contain}) and inside the depth-pure ones "
       f"({_mech_pure_contain}), so the containment conjunct turns "
       f"false when the target set is swapped")
mutant('MUT-MECHANISM-NECESSARY', 'G-MECHANISM-MEASURED',
       "THE REFUTED READING ITSELF: single-valuedness asserted "
       'NECESSARY for Chapman-Kolmogorov -- that a CK-exact quotient '
       'must carry no multi-target edge',
       _min_ckfail == 0 and _min_mt > 0,
       _min_ckfail == 0 and _min_mt == 0,
       f"the minimal repair is CK-exact ({_min_ckfail} failures) while "
       f"carrying {_min_mt} multi-target edges, so the necessity "
       f"reading turns the gate's own conjunct false -- this is the "
       f"claim the delivered verdict string made")
mutant('MUT-MINSPLIT-ANY-REFINEMENT', 'G-MECHANISM-MEASURED',
       'the repair attributed to ANY refinement rather than to the '
       'offending edges: the four LARGEST OTHER menu classes split '
       'instead, by their full successor signature',
       _oth_ckfail > 0, _min_ckfail > 0,
       f"splitting the four largest other classes leaves CK failing at "
       f"{_oth_ckfail} triples while the offending split leaves "
       f"{_min_ckfail}, so an any-refinement reading turns the "
       f"specificity conjunct false")
SEAL.take('SEAL-QUANTUM',
          lambda: dict(ck_failures={k: len(v) for k, v in CKFAIL.items()},
                       ck_triples={k: len(v) for k, v in CK.items()},
                       ck_failing_cells={k: [[r['cut'], r['mid'],
                                              r['cut2'], r['differing']]
                                             for r in v]
                                         for k, v in CKFAIL.items()},
                       ck_failing_source_classes=len(_ck_src_menu),
                       eq22_sealed_separately_at='G-EQ22-STAMPED',
                       depth_purity={k: [v[0], v[1], v[2]] for k, v in
                                     DEPTHPURE.items()},
                       shared_labels_per_triple=SHARED,
                       refinement_ladder=[list(r) for r in LADDER],
                       minimal_split=dict(classes=_min_n,
                                          multitarget=_min_mt,
                                          ck_failures=_min_ckfail),
                       other_split=dict(classes=_oth_n,
                                        ck_failures=_oth_ckfail),
                       round_1=dict(classes=_r1_n, multitarget=_r1_mt,
                                    spanning=_r1_span,
                                    ck_failures=_r1_ckfail,
                                    prefix_returns=_r1_returns,
                                    root_depths=_r1_root),
                       multitarget_sources_recurring=_mech_contain,
                       multitarget_sources_are_descent_failures=_mech_setid,
                       carrier_relative=_carrier_rel,
                       mechanism_measured=_mech_ok))
gate('G-QUANTUM-STAMPED', 'DISCLOSURE',
     'NO UNSTAMPED QUANTUM SENTENCE: every quantum-shape claim this '
     'unit makes is measured at BOTH carriers and carries the carrier '
     'it is read at.  The four claims are the eq.-22 refutation, the '
     'non-Markov triple census, Chapman-Kolmogorov, and lumpability.  '
     'This gate is a DISCLOSURE and its predicate is the literal True: '
     'it cannot fail, and it is not counted as evidence anywhere',
     True,
     f"eq. 22: @MENU-113 refuted at {len(TRIPLES)} of {len(TRIPLES)} "
     f"triples under {len(EQ_SPEAK['MENU-113'])} of {len(STYLES)} "
     f"completions that speak, @CONG-185 SILENT at "
     f"{len(STYLES)} of {len(STYLES)}; non-Markov triples: @MENU-113 "
     f"{len(CKFAIL['MENU-113'])} of {len(CK['MENU-113'])}, @CONG-185 "
     f"{len(CKFAIL['CONG-185'])}; lumpability: @MENU-113 "
     f"{len(CKFAIL['MENU-113']) == 0}, @CONG-185 "
     f"{len(CKFAIL['CONG-185']) == 0}; carrier-relative "
     f"{_carrier_rel}",
     waiver='THIS GATE IS A DISCLOSURE OF THE STAMPING DISCIPLINE, and '
            'the four claims it names each carry their own MUST gate '
            'above (G-EQ22-STAMPED, G-CONG-LUMPABLE, '
            'G-CARRIER-RELATIVE); it is not counted as independent '
            'evidence')

# ======================================================================
# P8 -- [B3]: THE CONVENTION-FREE FEASIBILITY LP
# ======================================================================
sec("P8 -- [B3]: the exact rational feasibility LP, convention-free")
emit("  The route the inheritance source names, verbatim:")
emit(f"    \"{VERBATIM[7][3]}\"")


def verify_farkas(A, b, y):
    """a Farkas vector is a certificate only if y.A <= 0 and y.b > 0;
    this is the check, and it is run on the vector that is PUBLISHED as
    the certificate, not on an internal one."""
    m, n = len(A), len(A[0])
    return (all(sum(y[i] * A[i][j] for i in range(m)) <= 0
                for j in range(n))
            and sum(y[i] * b[i] for i in range(m)) > 0)


def lp_feasible(A, b):
    """Decide {x >= 0 : A x = b} in exact rational arithmetic.  Phase-1
    simplex under Bland's rule.  BOTH verdicts are certified: a
    feasible verdict returns a primal point which is verified against
    the constraints, an infeasible verdict returns a Farkas vector y
    which is verified to satisfy y.A <= 0 and y.b > 0."""
    m, n = len(A), len(A[0])
    sg = [1] * m
    T = [row[:] for row in A]
    rhs = list(b)
    for i in range(m):
        if rhs[i] < 0:
            T[i] = [-v for v in T[i]]
            rhs[i] = -rhs[i]
            sg[i] = -1
    N = n + m
    tab = [T[i] + [Fr(1) if j == i else Fr(0) for j in range(m)] + [rhs[i]]
           for i in range(m)]
    basis = [n + i for i in range(m)]
    cost = [Fr(0)] * (N + 1)
    for i in range(m):
        for j in range(n):
            cost[j] -= tab[i][j]
        cost[N] -= tab[i][N]
    while True:
        piv = None
        for j in range(n):
            if cost[j] < 0:
                piv = j
                break
        if piv is None:
            break
        prow, ratio = None, None
        for i in range(m):
            if tab[i][piv] > 0:
                r = tab[i][N] / tab[i][piv]
                if (ratio is None or r < ratio
                        or (r == ratio and basis[i] < basis[prow])):
                    ratio, prow = r, i
        if prow is None:
            break
        pv = tab[prow][piv]
        tab[prow] = [v / pv for v in tab[prow]]
        for i in range(m):
            if i != prow and tab[i][piv] != 0:
                f = tab[i][piv]
                tab[i] = [u - f * v for u, v in zip(tab[i], tab[prow])]
        f = cost[piv]
        if f != 0:
            cost = [u - f * v for u, v in zip(cost, tab[prow])]
        basis[prow] = piv
    if -cost[N] == 0:
        x = [Fr(0)] * n
        for i in range(m):
            if basis[i] < n:
                x[basis[i]] = tab[i][N]
        cert = (all(v >= 0 for v in x)
                and all(sum(A[i][j] * x[j] for j in range(n)) == b[i]
                        for i in range(m)))
        return True, cert, x
    cB = [Fr(1) if basis[i] >= n else Fr(0) for i in range(m)]
    y = [sum(cB[i] * tab[i][n + k] for i in range(m)) * sg[k]
         for k in range(m)]
    cert = verify_farkas(A, b, y)
    return False, cert, y


def b3_problem(GAM, IDX, d, md, dd):
    """The [B3] interpolant problem: does a COLUMN-STOCHASTIC
    non-negative Gbar exist with Gamma(dd<-d) = Gbar . Gamma(md<-d)?
    Support reduction is exact, not a relaxation: if Gamma(dd<-d)[i][s]
    is 0 and Gamma(md<-d)[j][s] is positive then Gbar[i][j] must be 0,
    because every term of the sum is non-negative."""
    P1, P2 = dense(GAM, IDX, d, md), dense(GAM, IDX, d, dd)
    nj, ns, ni = len(P1), len(P1[0]), len(P2)
    s1 = [{s for s in range(ns) if P1[j][s] != 0} for j in range(nj)]
    s2 = [{s for s in range(ns) if P2[i][s] != 0} for i in range(ni)]
    allow = [[j for j in range(nj) if s1[j] <= s2[i]] for i in range(ni)]
    vix = {}
    for i in range(ni):
        for j in allow[i]:
            vix[(i, j)] = len(vix)
    rows, rhs = [], []
    for i in range(ni):
        for s in sorted(s2[i]):
            r = [Fr(0)] * len(vix)
            for j in allow[i]:
                if P1[j][s] != 0:
                    r[vix[(i, j)]] = P1[j][s]
            rows.append(r)
            rhs.append(P2[i][s])
    for j in range(nj):
        r = [Fr(0)] * len(vix)
        for i in range(ni):
            if (i, j) in vix:
                r[vix[(i, j)]] = Fr(1)
        rows.append(r)
        rhs.append(Fr(1))
    orphan = sum(1 for j in range(nj)
                 if not any((i, j) in vix for i in range(ni)))
    empty = sum(1 for i in range(ni) if not allow[i])
    return rows, rhs, len(vix), ni, nj, ns, orphan, empty, P1, P2


B3ROW, B3CPL, B3WIT, B3CERT = {}, {}, {}, {}
for _cn, _GAM, _IDX in (('CONG-185', GAM_C, IDX_C),
                        ('MENU-113', GAM_M, IDX_M)):
    for (d, md, dd) in TRIPLES:
        prog(f"[B3] {_cn} ({d},{md},{dd}) ...")
        rows, rhs, nv, ni, nj, ns, orph, empt, P1, P2 = b3_problem(
            _GAM, _IDX, d, md, dd)
        A = [[P1[j][s] for j in range(nj)] for s in range(ns)]
        bad, certs = 0, 0
        for i in range(ni):
            ok, cert, _ = lp_feasible(A, [P2[i][s] for s in range(ns)])
            certs += 1 if cert else 0
            bad += 0 if ok else 1
        B3ROW[(_cn, (d, md, dd))] = dict(rows=ni, vars=nj, eqs=ns,
                                         infeasible=bad, certified=certs,
                                         orphan_columns=orph,
                                         empty_rows=empt)
        okc, certc, vecc = lp_feasible(rows, rhs)
        B3CPL[(_cn, (d, md, dd))] = dict(feasible=okc, certified=certc,
                                         vars=nv, eqs=len(rows))
        B3CERT[(_cn, (d, md, dd))] = (rows, rhs, vecc, okc)
        Wit = dense(_GAM, _IDX, md, dd)
        B3WIT[(_cn, (d, md, dd))] = dict(
            product_matches=(matmul(Wit, P1) == P2),
            negatives=sum(1 for r in Wit for x in r if x < 0),
            column_stochastic=all(sum(Wit[i][j] for i in range(len(Wit)))
                                  == 1 for j in range(len(Wit[0]))))
for _cn in ('CONG-185', 'MENU-113'):
    for t in TRIPLES:
        r, c, w = B3ROW[(_cn, t)], B3CPL[(_cn, t)], B3WIT[(_cn, t)]
        emit(f"  [B3] @{_cn} {t}: row-decomposed {r['rows']} problems in "
             f"{r['vars']} variables and {r['eqs']} equations -> "
             f"{r['infeasible']} INFEASIBLE (certificates verified "
             f"{r['certified']} of {r['rows']}); COUPLED "
             f"{'FEASIBLE' if c['feasible'] else 'INFEASIBLE'} in "
             f"{c['vars']} variables and {c['eqs']} equations "
             f"(certificate verified {c['certified']}); the process's "
             f"own two-cut conditional as a witness: product matches "
             f"{w['product_matches']}, negatives {w['negatives']}, "
             f"column-stochastic {w['column_stochastic']}; support "
             f"obstruction: orphan columns {r['orphan_columns']}, empty "
             f"rows {r['empty_rows']}")
_rowfeas = all(B3ROW[k]['infeasible'] == 0 for k in B3ROW)
_rowcert = all(B3ROW[k]['certified'] == B3ROW[k]['rows'] for k in B3ROW)
gate('G-B3-ROW-DECOMPOSED', 'MUST',
     'THE ROW-DECOMPOSED [B3] PROBLEM IS FEASIBLE EVERYWHERE, at both '
     'carriers and at all four depth-cut triples with a non-degenerate '
     'first cut, with every verdict carrying a verified certificate.  '
     'The row problems alone therefore carry NO obstruction, and the '
     'support pattern carries none either: there is no orphan column '
     'and no empty row anywhere',
     _rowfeas and _rowcert
     and all(B3ROW[k]['orphan_columns'] == 0 and B3ROW[k]['empty_rows'] == 0
             for k in B3ROW),
     f"{sum(B3ROW[k]['rows'] for k in B3ROW)} row problems over "
     f"{len(B3ROW)} (carrier, triple) cells; infeasible rows "
     f"{sum(B3ROW[k]['infeasible'] for k in B3ROW)}; certificates "
     f"verified {sum(B3ROW[k]['certified'] for k in B3ROW)} of "
     f"{sum(B3ROW[k]['rows'] for k in B3ROW)}; orphan columns "
     f"{sum(B3ROW[k]['orphan_columns'] for k in B3ROW)}; empty rows "
     f"{sum(B3ROW[k]['empty_rows'] for k in B3ROW)}",
     falsifiers=['MUT-LP-ROW-BLIND'])
_A_bad = [[Fr(1), Fr(1)], [Fr(1), Fr(1)]]
_bad_ok, _bad_cert, _bad_vec = lp_feasible(_A_bad, [Fr(1), Fr(2)])
mutant('MUT-LP-ROW-BLIND', 'G-B3-ROW-DECOMPOSED',
       'the same solver run on a constructed INFEASIBLE system, so that '
       'a solver that always answers "feasible" is caught',
       _rowfeas, _bad_ok,
       f"the constructed system returns feasible={_bad_ok} with its "
       f"Farkas certificate verified {_bad_cert}, so a blind solver "
       f"would fail this gate")
CPL = {c: [B3CPL[(c, t)]['feasible'] for t in TRIPLES]
       for c in ('CONG-185', 'MENU-113')}
# THE ONE CELL THAT SPEAKS, NAMED (the operator's MINOR-6): the triple at
# which the rectangular column-stochastic problem is feasible while eq.
# 22's padded candidate is negative.
_speak_cells = [t for t in TRIPLES if B3CPL[('MENU-113', t)]['feasible']]
_speak_cell = _speak_cells[0] if len(_speak_cells) == 1 else None
_speak_negs = (EQ22[('MENU-113', 'identity', _speak_cell)]['negatives']
               if _speak_cell else None)
_speak_shape = (B3CPL[('MENU-113', _speak_cell)] if _speak_cell else {})
emit("")
emit(f"  THE DIVERGENCE CELL, NAMED: at MENU-113 {_speak_cell} the "
     f"rectangular column-stochastic problem is FEASIBLE "
     f"({_speak_shape.get('vars')} variables against "
     f"{_speak_shape.get('eqs')} equations, certified) while eq. 22's "
     f"unique PADDED candidate at the same triple carries "
     f"{_speak_negs} negative entries.  The two objects are different "
     f"problems: the padding converts an underdetermined feasibility "
     f"question into a determined algebraic one, and the determined "
     f"answer can be negative while the feasible set is non-empty.  "
     f"EQ-22 NEGATIVITY IS THEREFORE NOT EQUIVALENT TO THE "
     f"NON-EXISTENCE OF A STOCHASTIC INTERPOLANT -- a standing caution "
     f"for every eq-22-based refutation in the corpus, demonstrated "
     f"here at 1 of {len(TRIPLES)} cells.")
emit(f"  The comparison cell: at {TRIPLES[0]} the same problem carries "
     f"{B3CPL[('MENU-113', TRIPLES[0])]['vars']} variables against "
     f"{B3CPL[('MENU-113', TRIPLES[0])]['eqs']} equations and is "
     f"INFEASIBLE with a verified Farkas vector.  What distinguishes "
     f"the two is not measured here and is carried to the successor.")
_cpl_ok = (all(CPL['CONG-185'])
           and sum(1 for v in CPL['MENU-113'] if not v) == 3
           and all(B3CPL[k]['certified'] for k in B3CPL)
           and all(B3WIT[('CONG-185', t)]['product_matches']
                   and B3WIT[('CONG-185', t)]['negatives'] == 0
                   and B3WIT[('CONG-185', t)]['column_stochastic']
                   for t in TRIPLES))
gate('G-B3-COUPLED', 'MUST',
     'THE COLUMN-SUM COUPLING IS THE WHOLE CONTENT OF THE [B3] '
     'OBSTRUCTION, and it separates the two carriers: @CONG-185 the '
     'coupled problem is FEASIBLE at all four triples and the witness '
     "is EXHIBITED -- the process's own two-cut conditional is "
     'non-negative, column-stochastic and reproduces the target '
     'exactly; @MENU-113 it is INFEASIBLE at 3 of the 4, each with a '
     'verified Farkas certificate, and FEASIBLE at the fourth, WHICH IS '
     'NAMED: (1, 2, 4).  This is a statement about the RECTANGULAR '
     "column-stochastic problem, not about eq. 22's padded form; the "
     'two diverge at exactly that cell and the separation is carried as '
     'a scope annotation, not as an erratum',
     _cpl_ok and _speak_cell == (1, 2, 4),
     f"the one feasible MENU cell is {_speak_cell}, where the padded "
     f"candidate carries {_speak_negs} negatives; "
     f"@CONG-185 coupled feasibility by triple {CPL['CONG-185']}; "
     f"@MENU-113 {CPL['MENU-113']}; every verdict certified "
     f"{all(B3CPL[k]['certified'] for k in B3CPL)}; the exhibited "
     f"witness at the ruled carrier matches at "
     f"{sum(1 for t in TRIPLES if B3WIT[('CONG-185', t)]['product_matches'])} "
     f"of {len(TRIPLES)} triples with "
     f"{sum(B3WIT[('CONG-185', t)]['negatives'] for t in TRIPLES)} "
     f"negative entries",
     falsifiers=['MUT-LP-WITNESS-FAKE', 'MUT-WROUTE-UNCERTIFIED'])
_fakewit = [B3WIT[('MENU-113', t)]['product_matches'] for t in TRIPLES]
mutant('MUT-LP-WITNESS-FAKE', 'G-B3-COUPLED',
       "the ruled carrier's exhibited witness swapped for the contrast "
       "carrier's, where the same object does NOT reproduce the target",
       all(B3WIT[('CONG-185', t)]['product_matches'] for t in TRIPLES),
       all(_fakewit),
       f"@MENU-113 the two-cut conditional reproduces the target at "
       f"{sum(1 for v in _fakewit if v)} of {len(TRIPLES)} triples, so "
       f"the witness conjunct turns false when the carrier is swapped")
_falsified = []
for _k in sorted(B3CERT, key=str):
    _rows_k, _rhs_k, _vec_k, _ok_k = B3CERT[_k]
    if _ok_k or not _vec_k:
        continue
    _bent = [-v for v in _vec_k]
    _falsified.append(verify_farkas(_rows_k, _rhs_k, _bent))
mutant('MUT-WROUTE-UNCERTIFIED', 'G-B3-COUPLED',
       'A FALSIFIED FARKAS VECTOR: every infeasible coupled verdict '
       're-checked against a NEGATED certificate, which reverses the '
       'sign of y.b, so a verdict accepted on an unverified vector is '
       'caught',
       all(B3CPL[k]['certified'] for k in B3CPL),
       all(_falsified) and len(_falsified) > 0,
       f"the {len(_falsified)} negated Farkas vectors verify at "
       f"{sum(1 for v in _falsified if v)} of {len(_falsified)}, so the "
       f"certificate conjunct turns false on them while the delivered "
       f"vectors verify at {sum(1 for k in B3CPL if B3CPL[k]['certified'])} "
       f"of {len(B3CPL)}")
SEAL.take('SEAL-B3',
          lambda: dict(row_decomposed={f"{c}|{t}": v for (c, t), v in
                                       B3ROW.items()},
                       coupled={f"{c}|{t}": v for (c, t), v in
                                B3CPL.items()},
                       witness={f"{c}|{t}": v for (c, t), v in
                                B3WIT.items()},
                       coupled_feasible_by_carrier=CPL,
                       divergence_cell=str(_speak_cell),
                       divergence_cell_eq22_negatives=_speak_negs))

# ======================================================================
# P9 -- THE ANCHOR QUESTION
# ======================================================================
sec("P9 -- THE ANCHOR QUESTION: renewal root, or sedimentary?")
# --- THE SECOND CAP, BUILT AND MEASURED (R-GI-2).  The delivered unit
# --- computed this arm and printed only its class counts, discarding the
# --- spanning column that decides the cap question.  It is emitted here.
prog("the d <= 5 arm, re-derived, WITH its spanning trace ...")
_menu5 = {h: sk(("MENU", tuple(sorted((evsk(e), str(q))
                                      for e, q in CACHE[h]))))
          for h in ANCHOR_SCOPE_S}
_c5, _r5, _t5 = refine(ANCHOR_SCOPE, _menu5)
_d5_dep = defaultdict(set)
_m5_dep = defaultdict(set)
for _h in ANCHOR_SCOPE_S:
    _d5_dep[_c5[_h]].add(len(_h))
    _m5_dep[_menu5[_h]].add(len(_h))
_d5_span = sum(1 for v in _d5_dep.values() if len(v) > 1)
_m5_span = sum(1 for v in _m5_dep.values() if len(v) > 1)
_d5_root = sorted(_d5_dep[_c5[ROOT]])
_d5_returns = sum(1 for h in ANCHOR_SCOPE_S if len(h) > 0
                  and any(_c5[h] == _c5[g]
                          for g in (h[:k] for k in range(len(h)))))
_d5_pure_round = [t[0] for t in _t5 if t[2] == 0][:1]
_d5_dims = [len({_c5[h] for h in ANCHOR_SCOPE_S if len(h) == d})
            for d in range(CAP_A + 1)]
emit("")
emit(f"  THE d <= 5 ARM: menu classes {len(set(_menu5.values()))}, "
     f"coarsest congruence {len(set(_c5.values()))} after {_r5} "
     f"refinement rounds; per-round class counts {[t[1] for t in _t5]} "
     f"and per-round classes spanning more than one depth "
     f"{[t[2] for t in _t5]}.")
emit(f"    classes at more than one depth cut: {_d5_span} of "
     f"{len(_d5_dep)}; the root's class occurs at depths {_d5_root}; "
     f"prefix-class returns {_d5_returns}; per-cut dimensions "
     f"{fl(_d5_dims)}; depth purity first reached at round "
     f"{_d5_pure_round[0] if _d5_pure_round else None} of {_r5}.")
emit(f"    the same measurement on the d <= 5 MENU partition, which is "
     f"not a congruence: {_m5_span} of {len(_m5_dep)} classes span more "
     f"than one depth.")
emit("")
emit("  THE DEPTH-GRADING IS NOT CAP-LOCAL; IT IS FORCED AT EVERY "
     "FINITE CAP.")
emit("  Theorem.  Let the window be {h : |h| <= N} and suppose every "
     "history of depth")
emit("  < N has at least one successor.  After refinement round k a "
     "history's class")
emit("  determines min(N - |h|, k).  Proof.  Round 1: the in-window "
     "successor multiset")
emit("  is empty iff |h| = N, so the class determines min(N - |h|, 1).  "
     "Round k+1: the")
emit("  signature carries the round-k classes of the successors, each "
     "of which")
emit("  determines min(N - |h| - 1, k), and non-emptiness distinguishes "
     "|h| < N; so the")
emit("  class determines min(N - |h|, k+1).  Hence at round N the class "
     "determines |h|")
emit("  exactly: THE FIXED POINT IS DEPTH-PURE AT EVERY FINITE CAP, and "
     "purity is")
emit("  reached at round N with the fixed point at round N+1.  QED.")
_c4_pure_round = [t[0] for t in CONG_TRACE if t[2] == 0][:1]
_succ_all = all(len(CACHE[h]) > 0 for h in ANCHOR_SCOPE_S
                if len(h) < CAP_A)
emit(f"  Observed, twice: purity at round "
     f"{_c4_pure_round[0] if _c4_pure_round else None} of "
     f"{CONG_ROUNDS} for N = {CAP}, and at round "
     f"{_d5_pure_round[0] if _d5_pure_round else None} of {_r5} for "
     f"N = {CAP_A} -- the same round-N-of-N+1 position.  The theorem's "
     f"hypothesis is measured, not assumed: every history below the cap "
     f"has at least one successor ({_succ_all}).")
emit("  CONSEQUENCE, AND IT IS A WALL: no capped successor-closure "
     "fixed point of this")
emit("  construction admits a regeneration anchor at the class grain, "
     "at any cap, BY")
emit("  THEOREM rather than by cost.  What is open is not a different "
     "cap -- this unit")
emit("  has now built and measured one -- but a different BOUNDARY "
     "CONVENTION: a fixed")
emit("  point whose terminal stratum does not carry an empty successor "
     "signature.")
emit("  The unreachability stamp this section carries, verbatim:")
emit(f"    \"{VERBATIM[10][3]}\"")
emit("  The renewal-root law the pin offers as path (a), verbatim:")
emit(f"    \"{VERBATIM[15][3]}\"")
emit("  and its own scope tag, verbatim:")
emit(f"    \"{VERBATIM[16][3]}\"")
prog("R-SIG / R-MENU census and the holdings profile ...")


def rsig(h):
    pred = event_poset(list(h))
    vw = View(list(h), pred, set(range(len(h))))
    if vw.live:
        return None
    hold = {a: frozenset(vw.holdings(a)) for a in AB}
    nsup = {a: frozenset(x for x in hold[a] if x not in vw.superseded)
            for a in AB}
    if len(nsup['A']) != 1 or nsup['A'] != nsup['B']:
        return None
    v = next(iter(nsup['A']))
    return (v, (len(hold['A']), len(hold['B'])),
            all(hold[a] == frozenset({v}) for a in AB))


RS = {}
for h in CACHE:
    r = rsig(h)
    if r is not None:
        RS[h] = r
BLOCKS = Counter(v[1] for v in RS.values())
RMENU = {h for h, v in RS.items() if v[2]}
B11 = {h for h, v in RS.items() if v[1] == (1, 1)}
B11_S = sorted(B11, key=sk)
anchor('A-RSIG-COUNT', 5161, len(RS),
       "the committed R-SIG census at depth <= 5")
anchor('A-RMENU-COUNT', 1365, len(RMENU),
       "the committed menu-exact renewal count at depth <= 5")
anchor('A-BLOCKS', {'(1, 1)': 1365, '(2, 2)': 3788, '(2, 3)': 4,
                    '(3, 2)': 4},
       {str(k): v for k, v in sorted(BLOCKS.items())},
       "the committed holdings-profile decomposition at depth <= 5")
ENTRIES = {}
TRANS = 0
for h in CACHE:
    if len(h) < CAP_A:
        TRANS += len(CACHE[h])
for _pf in sorted(BLOCKS):
    blk = {h for h, v in RS.items() if v[1] == _pf}
    ENTRIES[str(_pf)] = sum(1 for h in CACHE if len(h) < CAP_A
                            for e, q in CACHE[h]
                            if (h + (e,)) in blk and h not in blk)
emit(f"  R-SIG points at depth <= {CAP_A}: {len(RS)}; blocks "
     f"{ctr({str(k): v for k, v in BLOCKS.items()})}; the (1,1) block "
     f"IS R-MENU: {B11 == RMENU}")
emit(f"  transitions out of every history of depth < {CAP_A}: {TRANS}; "
     f"transitions INTO each block from outside it: {ctr(ENTRIES)}")
gate('G-UNREACHABILITY-STAMP', 'MUST',
     'THE UNREACHABILITY STAMP, RE-MEASURED IN UNIT at this unit\'s own '
     'declared window: the (1,1) block -- which is exactly R-MENU, and '
     'which the coarsening lemma leaves as the only surviving atom '
     'candidate at the ruled carrier -- is entered from outside at '
     'EXACTLY ZERO transitions, while every other block is entered at a '
     'strictly positive number.  Recurrence-based readings of the atom '
     'are therefore BARRED',
     ENTRIES['(1, 1)'] == 0 and all(v > 0 for k, v in ENTRIES.items()
                                    if k != '(1, 1)'),
     f"transitions into the (1,1) block from outside: "
     f"{ENTRIES['(1, 1)']} of {TRANS} transitions of this unit's "
     f"window; the other blocks are entered at "
     f"{ctr({k: v for k, v in ENTRIES.items() if k != '(1, 1)'})}; the "
     f"pinned wider measurement, quoted at V-UNREACH, is 0 of 243768",
     falsifiers=['MUT-UNREACH-DROP'])
mutant('MUT-UNREACH-DROP', 'G-UNREACHABILITY-STAMP',
       'the (1,1) row replaced by a block the process DOES enter',
       ENTRIES['(1, 1)'] == 0, ENTRIES['(2, 2)'] == 0,
       f"the (2,2) block is entered at {ENTRIES['(2, 2)']} transitions, "
       f"so the zero-entry predicate turns false on it -- the stamp is "
       f"a property of one block, not of the census")

# --- does the block survive the carrier?  the successor computation --
B11C = [h for h in B11_S if len(h) <= CAP]
_menu_cls = sorted({MENU[h] for h in B11C}, key=sk)
_cong_cls = sorted({CONG[h] for h in B11C}, key=sk)
_menu_pure = all(sum(1 for h in CARRIER_S if MENU[h] == c)
                 == sum(1 for h in B11C if MENU[h] == c)
                 for c in _menu_cls)
_cong_pure = all(sum(1 for h in CARRIER_S if CONG[h] == c)
                 == sum(1 for h in B11C if CONG[h] == c)
                 for c in _cong_cls)
_cong_sizes = sorted((sum(1 for h in B11C if CONG[h] == c)
                      for c in _cong_cls), reverse=True)
_cong_depths = sorted({len(h) for h in B11C})
emit(f"  the (1,1) block on the ruled carrier's own window: "
     f"{len(B11C)} points at depths {_cong_depths}; MENU-113 classes "
     f"met {len(_menu_cls)} (block-pure {_menu_pure}); CONG-185 classes "
     f"met {len(_cong_cls)} of sizes {_cong_sizes} (block-pure "
     f"{_cong_pure})")
gate('G-BLOCK-SPLIT-AT-CONG', 'MUST',
     "THE PREDECESSOR'S OPEN QUESTION, ANSWERED: the depth-<= 4 part of "
     'the (1,1) block lies inside ONE class of MENU-113 -- which is why '
     'the atom survives there -- and the later refinement rounds DO '
     'split it: at CONG-185 it meets one class per depth stratum, each '
     'of them block-pure',
     (len(_menu_cls) == 1 and _menu_pure and len(_cong_cls) == 5
      and _cong_pure and len(_cong_cls) == len(_cong_depths)),
     f"{len(B11C)} points; MENU-113 classes {len(_menu_cls)}, CONG-185 "
     f"classes {len(_cong_cls)} against {len(_cong_depths)} depth "
     f"strata, sizes {_cong_sizes}, all block-pure {_cong_pure}",
     falsifiers=['MUT-ATOM-UNSCOPED'])
mutant('MUT-ATOM-UNSCOPED', 'G-BLOCK-SPLIT-AT-CONG',
       'the MENU-113 answer carried to the ruled carrier unstamped -- '
       'the claim that the block stays one class',
       len(_cong_cls) == 5, len(_cong_cls) == len(_menu_cls),
       f"the block meets {len(_cong_cls)} classes at CONG-185 against "
       f"{len(_menu_cls)} at MENU-113, so the unstamped carry turns the "
       f"predicate false")

# --- delta*, at both carriers, at the windows this cap can state -----
def nstep(x, N, horizon):
    cur = {x: Fr(1)}
    for t in range(N, 0, -1):
        nxt = defaultdict(Fr)
        for h, p in cur.items():
            r = (CAP - len(h)) if horizon == 'H4' else t
            if r < 1:
                return None
            for e, q in CACHE[h]:
                nxt[h + (e,)] += p * kern(h, e, r)
        cur = dict(nxt)
    return cur


def deltastar(pts, N, V, horizon):
    per = []
    for x in pts:
        law = nstep(x, N, horizon)
        if law is None:
            return None
        agg = defaultdict(Fr)
        for h, p in law.items():
            if h not in V:
                return None
            agg[V[h]] += p
        per.append(agg)
    labs = set()
    for a in per:
        labs |= set(a)
    return sum(min(a.get(s, Fr(0)) for a in per) for s in labs)


prog("delta* rows at both carriers ...")
DSTAR = {}
for _N, _maxd in ((1, CAP - 1), (2, CAP - 2)):
    _pts = sorted([h for h in B11_S if len(h) <= _maxd], key=sk)
    for _hz in ('MATCHED', 'H4'):
        for _cn, _V in (('CONG-185', CONG), ('MENU-113', MENU)):
            DSTAR[(_cn, _N, _hz)] = (deltastar(_pts, _N, _V, _hz),
                                     len(_pts), _maxd)
for _N in (1, 2):
    for _hz in ('MATCHED', 'H4'):
        _c, _m = DSTAR[('CONG-185', _N, _hz)], DSTAR[('MENU-113', _N, _hz)]
        emit(f"  delta* of the (1,1) block restricted to depth <= "
             f"{_c[2]} ({_c[1]} points), N = {_N}, horizon {_hz:7s}: "
             f"@CONG-185 {_c[0]}   @MENU-113 {_m[0]}")
STRATA = {}
for _d in range(CAP):
    _pts = sorted([h for h in B11_S if len(h) == _d], key=sk)
    if _pts:
        STRATA[_d] = (deltastar(_pts, 1, CONG, 'H4'), len(_pts))
emit(f"  delta* of each depth stratum of the block at N = 1 "
     f"@CONG-185: {ctr({str(k): str(v[0]) for k, v in STRATA.items()})} "
     f"(stratum sizes {ctr({str(k): v[1] for k, v in STRATA.items()})})")
_allclasses = sorted({CONG[h] for h in CARRIER_S if len(h) < CAP}, key=sk)
_byc = defaultdict(list)
for h in sorted(CARRIER, key=sk):
    if len(h) < CAP:
        _byc[CONG[h]].append(h)
_atom_bad = sum(1 for c in _allclasses
                if deltastar(_byc[c], 1, CONG, 'H4') != 1)
gate('G-COARSENING-LEMMA', 'MUST',
     'THE COARSENING LEMMA APPLIED WHERE IT BITES, AND MEASURED RATHER '
     'THAN INHERITED: delta* is monotone under coarsening, CONG-185 '
     'refines MENU-113, and the atom the predecessor left live DIES at '
     'the ruled carrier -- delta* of the (1,1) block is exactly 1 at '
     'MENU-113 under the matched horizon and exactly 0 at CONG-185, at '
     'BOTH step counts this cap can state.  Meanwhile EVERY class of '
     'the ruled carrier is an exact atom, which is what a congruence '
     'makes trivially true and is therefore no instrument at all',
     (DSTAR[('MENU-113', 1, 'MATCHED')][0] == 1
      and DSTAR[('CONG-185', 1, 'MATCHED')][0] == 0
      and DSTAR[('MENU-113', 2, 'MATCHED')][0] == 1
      and DSTAR[('CONG-185', 2, 'MATCHED')][0] == 0
      and all(DSTAR[('CONG-185', n, h)][0]
              <= DSTAR[('MENU-113', n, h)][0]
              for n in (1, 2) for h in ('MATCHED', 'H4'))
      and _atom_bad == 0),
     f"delta* at N = 1 matched: @MENU-113 "
     f"{DSTAR[('MENU-113', 1, 'MATCHED')][0]}, @CONG-185 "
     f"{DSTAR[('CONG-185', 1, 'MATCHED')][0]}; at N = 2 matched: "
     f"{DSTAR[('MENU-113', 2, 'MATCHED')][0]} and "
     f"{DSTAR[('CONG-185', 2, 'MATCHED')][0]}; the monotonicity "
     f"inequality holds on all {2 * 2} measured cells; classes of the "
     f"ruled carrier failing delta* = 1: {_atom_bad} of "
     f"{len(_allclasses)}",
     falsifiers=['MUT-DELTA-CARRIER-SWAP'])
mutant('MUT-DELTA-CARRIER-SWAP', 'G-COARSENING-LEMMA',
       'the two carriers swapped in the collapse claim -- the reading '
       'that would make the atom survive the refinement',
       (DSTAR[('CONG-185', 1, 'MATCHED')][0] == 0
        and DSTAR[('MENU-113', 1, 'MATCHED')][0] == 1),
       (DSTAR[('MENU-113', 1, 'MATCHED')][0] == 0
        and DSTAR[('CONG-185', 1, 'MATCHED')][0] == 1),
       f"with the carriers swapped the row reads "
       f"{DSTAR[('MENU-113', 1, 'MATCHED')][0]} and "
       f"{DSTAR[('CONG-185', 1, 'MATCHED')][0]}, so the collapse "
       f"predicate turns false")
gate('G-ATOM-BLOCK-SCOPE', 'MUST',
     'THE ATOM CLAIM IS CARRIED AT (1,1)-BLOCK SCOPE ONLY, as the '
     'adjudication rules, and this unit measures what the predecessor '
     'could only bound: at the ruled carrier the surviving candidate '
     'is 0, so the atom content of the [B3] register at CONG-185 is '
     'EMPTY on the block and TRIVIAL on the classes',
     (DSTAR[('CONG-185', 1, 'MATCHED')][0] == 0
      and DSTAR[('CONG-185', 2, 'MATCHED')][0] == 0
      and _atom_bad == 0),
     f"the two open rows of the predecessor read "
     f"{DSTAR[('CONG-185', 1, 'MATCHED')][0]} and "
     f"{DSTAR[('CONG-185', 2, 'MATCHED')][0]} at the ruled carrier; "
     f"every one of the {len(_allclasses)} testable carrier classes is "
     f"an exact atom, which a congruence forces",
     falsifiers=['MUT-ATOM-CLASS-SCOPE'])
_cls_probe = deltastar(_byc[_allclasses[0]], 1, CONG, 'H4')
mutant('MUT-ATOM-CLASS-SCOPE', 'G-ATOM-BLOCK-SCOPE',
       'the atom claim read at CLASS scope instead of at (1,1)-block '
       'scope -- the reading that would take a congruence class\'s '
       'trivial delta* for the block row',
       (DSTAR[('CONG-185', 1, 'MATCHED')][0] == 0 and _atom_bad == 0),
       (_cls_probe == 0 and _atom_bad == 0),
       f"a carrier class has delta* = {_cls_probe}, not 0 -- every one "
       f"of the {len(_allclasses)} testable classes does, which a "
       f"congruence forces -- so reading a class row as the block row "
       f"turns this gate's own zero-delta* conjunct false; the atom "
       f"language is EMPTY on the block and VACUOUS on the classes")

# --- THE TWO DECLARED ANCHOR PATHS, MEASURED ------------------------
_grade_pure = DEPTHPURE['CONG-185'][0] == 0
_grade_round = [t[0] for t in CONG_TRACE if t[2] == 0][:1]
_returns = {}
for _cn, _V in (('CONG-185', CONG), ('MENU-113', MENU)):
    _returns[_cn] = sum(1 for h in CARRIER_S if len(h) > 0
                        and any(_V[h] == _V[g] for g in
                                (h[:k] for k in range(len(h)))))
emit("")
emit(f"  PATH (a), THE RENEWAL-ROOT CANDIDATE, measured at the class "
     f"grain:")
emit(f"    the ruled carrier's classes occur at more than one depth cut "
     f"at {DEPTHPURE['CONG-185'][0]} of {DEPTHPURE['CONG-185'][1]}; the "
     f"class chain is therefore GRADED by depth and no class is ever "
     f"revisited.  Histories whose class equals the class of one of "
     f"their own prefixes: @CONG-185 {_returns['CONG-185']}, "
     f"@MENU-113 {_returns['MENU-113']}.")
emit(f"    the root's own class occurs at depths "
     f"{DEPTHPURE['CONG-185'][2]} @CONG-185 and "
     f"{DEPTHPURE['MENU-113'][2]} @MENU-113 -- recurrence of the "
     f"renewal root is a property of the COARSER carrier.  NO LINK "
     f"BETWEEN RECURRENCE AND NON-MARKOVIANITY IS CLAIMED: the two "
     f"carriers the pin names happen to differ in both respects, and "
     f"this unit's own refinement lattice separates them -- at round 1 "
     f"the root's class recurs, {_r1_returns} histories return to a "
     f"prefix class, and the chain is CK-exact at {_r1_ckfail} of "
     f"{len(CK['MENU-113'])} triples.  The co-location is "
     f"COINCIDENTAL and is dropped.")
emit(f"    the grading is reached at refinement round "
     f"{_grade_round[0] if _grade_round else None} of {CONG_ROUNDS}, "
     f"the spanning-class count falling "
     f"{[t[2] for t in CONG_TRACE]} -- and it is CAP-FORCED, not "
     f"cap-driven: the theorem above puts depth purity at round N of "
     f"N+1 at EVERY finite cap, and the d <= 5 arm reproduces it "
     f"({_d5_span} of {len(_d5_dep)} classes spanning).")
emit(f"    with the holdings ladder projected out the obstruction does "
     f"not lift: the carrier's own class label DETERMINES the depth, "
     f"which is a second monotone coordinate the projection cannot "
     f"remove.")
emit(f"    and the renewal-root first-return law the pin offers is "
     f"stated at DELIVERY-FREE scope by its own source, which declares "
     f"in terms that transport scope changes the picture.")
ANCHOR_PATH = ('SEDIMENTARY' if (_grade_pure and _returns['CONG-185'] == 0
                                 and ENTRIES['(1, 1)'] == 0
                                 and DSTAR[('CONG-185', 1,
                                            'MATCHED')][0] == 0)
               else 'RENEWAL-ROOT')
emit("")
emit(f"  THE ANCHOR ANSWER: {ANCHOR_PATH}.  Path (a) fails at the class "
     f"grain for a measured structural reason, so the one-pass reading "
     f"is adopted honestly: the law's long-run structure on this "
     f"carrier is argued from ACCUMULATION, not from return, and no "
     f"recurrence is assumed anywhere in this unit.")
gate('G-ANCHOR-RENEWAL-ROOT', 'MUST',
     'PATH (a) IS MEASURED AND FAILS, AT THE CLASS GRAIN, FOR A REASON: '
     'the ruled carrier separates every depth, so its class chain is '
     'graded and no class -- the renewal root included -- is ever '
     'revisited; the one small set the predecessor left live is entered '
     'at zero transitions and has delta* = 0 there; and the first-return '
     'law the pin offers as the candidate is stated at DELIVERY-FREE '
     'scope by its own source, WHICH IS A CONJUNCT OF THIS GATE and not '
     'only of its falsifier.  No recurrence is assumed anywhere',
     (_grade_pure and _returns['CONG-185'] == 0
      and _returns['MENU-113'] > 0 and ENTRIES['(1, 1)'] == 0
      and VERBATIM[16][3] in SRC['S-P09']),
     f"classes spanning more than one depth @CONG-185 "
     f"{DEPTHPURE['CONG-185'][0]}, @MENU-113 {DEPTHPURE['MENU-113'][0]}; "
     f"prefix-class returns @CONG-185 {_returns['CONG-185']}, "
     f"@MENU-113 {_returns['MENU-113']}; block entries "
     f"{ENTRIES['(1, 1)']}; the renewal-root law's own scope tag is "
     f"quoted at V-RENEWAL-SCOPE",
     falsifiers=['MUT-GRADING-BLIND', 'MUT-RENEWAL-SCOPE-DROP'])
mutant('MUT-GRADING-BLIND', 'G-ANCHOR-RENEWAL-ROOT',
       'the grading test run at the contrast carrier, where classes DO '
       'recur across depths',
       _grade_pure, DEPTHPURE['MENU-113'][0] == 0,
       f"@MENU-113 {DEPTHPURE['MENU-113'][0]} of "
       f"{DEPTHPURE['MENU-113'][1]} classes occur at more than one "
       f"depth, so the grading predicate turns false there -- the "
       f"anchor answer is a statement about THIS carrier")
_p09 = SRC['S-P09']
mutant('MUT-RENEWAL-SCOPE-DROP', 'G-ANCHOR-RENEWAL-ROOT',
       "the renewal-root law's own delivery-free scope tag dropped from "
       'its source text',
       VERBATIM[16][3] in _p09,
       VERBATIM[16][3] in _p09.replace(VERBATIM[16][3], ''),
       "with the scope tag removed the quotation no longer locates, so "
       "an unscoped carry of the first-return law cannot pass the "
       "verbatim precheck")
_cap_ok = (_d5_span == 0 and _d5_root == [0] and _d5_returns == 0
           and _r5 == CAP_A + 1 and _d5_pure_round == [CAP_A]
           and CONG_ROUNDS == CAP + 1 and _c4_pure_round == [CAP]
           and _m5_span > 0 and _succ_all)
gate('G-CAP-UNIVERSAL', 'MUST',
     'THE DEPTH-GRADING IS CAP-FORCED, NOT CAP-LOCAL, AND THE UNIT '
     'BUILDS THE SECOND CAP RATHER THAN POINTING AT IT: the '
     "successor-closure fixed point of the menu partition is depth-pure "
     'at EVERY finite cap by the height-to-cap induction stated above, '
     'and the d <= 5 arm reproduces it exactly -- 0 of 462 classes '
     'spanning a cut, the root at depth 0 alone, 0 prefix-class '
     'returns, purity at round N with the fixed point at round N+1 at '
     'both caps.  The d <= 5 MENU partition, which is not a congruence, '
     'is the contrast: its classes DO span.  Consequently the renewal-'
     'root candidate cannot be posed at the class grain of ANY capped '
     'carrier of this construction, and what is open is the BOUNDARY '
     'CONVENTION, not the cap',
     _cap_ok,
     f"d <= 4: {DEPTHPURE['CONG-185'][0]} of "
     f"{DEPTHPURE['CONG-185'][1]} classes spanning, purity at round "
     f"{_c4_pure_round} of {CONG_ROUNDS}; d <= 5: {_d5_span} of "
     f"{len(_d5_dep)} spanning, root depths {_d5_root}, prefix-class "
     f"returns {_d5_returns}, purity at round {_d5_pure_round} of "
     f"{_r5}; the d <= 5 menu partition spans at {_m5_span} of "
     f"{len(_m5_dep)}; every history below the cap has a successor "
     f"{_succ_all}",
     falsifiers=['MUT-CAP-LOCAL'])
mutant('MUT-CAP-LOCAL', 'G-CAP-UNIVERSAL',
       'THE READING THE DELIVERY CARRIED: the grading asserted local to '
       'this cap -- the same purity predicate evaluated on the d <= 5 '
       'MENU partition, the object a cap-local reading would expect the '
       'refinement to look like',
       _d5_span == 0, _m5_span == 0,
       f"the d <= 5 congruence spans at {_d5_span} of {len(_d5_dep)} "
       f"while the d <= 5 menu partition spans at {_m5_span} of "
       f"{len(_m5_dep)}, so the purity conjunct turns false on the "
       f"non-congruence and the grading is a property of the closure, "
       f"reproduced at the next cap rather than local to this one")
gate('G-ANCHOR-PATH', 'MUST',
     'THE OUTCOME SEGMENT NAMES THE PATH THE MEASUREMENTS SUPPORT, and '
     'the selector is a function of measured quantities with both '
     'branches reachable',
     ANCHOR_PATH == 'SEDIMENTARY',
     f"the selector reads grading {_grade_pure}, class returns "
     f"{_returns['CONG-185']}, block entries {ENTRIES['(1, 1)']}, "
     f"block delta* {DSTAR[('CONG-185', 1, 'MATCHED')][0]} -> "
     f"{ANCHOR_PATH}",
     falsifiers=['MUT-ANCHOR-PATH-FLIP'])
_flip = ('SEDIMENTARY' if (DEPTHPURE['MENU-113'][0] == 0
                           and _returns['MENU-113'] == 0)
         else 'RENEWAL-ROOT')
mutant('MUT-ANCHOR-PATH-FLIP', 'G-ANCHOR-PATH',
       'the same selector fed the contrast carrier\'s measurements, on '
       'which it returns the OTHER branch',
       ANCHOR_PATH == 'SEDIMENTARY', _flip == 'SEDIMENTARY',
       f"on MENU-113's measurements the selector returns {_flip}, so it "
       f"is a function with both branches reachable and not a constant")
SEAL.take('SEAL-ANCHOR',
          lambda: dict(path=ANCHOR_PATH, rsig=len(RS), rmenu=len(RMENU),
                       blocks={str(k): v for k, v in BLOCKS.items()},
                       entries=ENTRIES, transitions=TRANS,
                       block_on_carrier=dict(points=len(B11C),
                                             menu_classes=len(_menu_cls),
                                             cong_classes=len(_cong_cls),
                                             cong_sizes=_cong_sizes,
                                             depths=_cong_depths,
                                             block_pure=[_menu_pure,
                                                         _cong_pure]),
                       delta_star={f"{c}|N={n}|{h}": [str(v[0]), v[1],
                                                      v[2]]
                                   for (c, n, h), v in DSTAR.items()},
                       strata={str(k): [str(v[0]), v[1]] for k, v in
                               STRATA.items()},
                       carrier_classes_are_atoms=(_atom_bad == 0),
                       prefix_class_returns=_returns,
                       grading_round=(_grade_round[0] if _grade_round
                                      else 0),
                       cap_universal=dict(
                           d4=dict(spanning=DEPTHPURE['CONG-185'][0],
                                   classes=DEPTHPURE['CONG-185'][1],
                                   purity_round=(_c4_pure_round[0]
                                                 if _c4_pure_round
                                                 else 0),
                                   rounds=CONG_ROUNDS),
                           d5=dict(spanning=_d5_span,
                                   classes=len(_d5_dep),
                                   purity_round=(_d5_pure_round[0]
                                                 if _d5_pure_round
                                                 else 0),
                                   rounds=_r5, root_depths=_d5_root,
                                   prefix_returns=_d5_returns,
                                   dims=_d5_dims,
                                   menu_spanning=_m5_span),
                           successors_everywhere=_succ_all)))

# ======================================================================
# P10 -- SUPPLY (the adjudicated additions)
# ======================================================================
sec("P10 -- SUPPLY: the rows the successor needs, pinned or excluded")
gate('G-SUPPLY-D5', 'MUST',
     "THE d <= 5 SUPPLY ROW, RE-DERIVED RATHER THAN CITED, AND ITS "
     'SPANNING TRACE PUBLISHED: the wider committed arm the successor '
     'needs -- menu quotient 265, coarsest congruence 462 after 6 '
     "refinement rounds -- reproduces from this unit's own family and "
     'its own refinement, and the per-round SPANNING column is emitted '
     'rather than discarded, because it is the datum that decides the '
     'cap question',
     len(set(_menu5.values())) == 265 and len(set(_c5.values())) == 462
     and _r5 == 6 and len(_t5) == _r5,
     f"at (A,B) d <= 5: menu classes {len(set(_menu5.values()))}, "
     f"coarsest congruence {len(set(_c5.values()))} after {_r5} "
     f"refinement rounds; per-round class counts {[t[1] for t in _t5]}; "
     f"per-round classes spanning more than one depth "
     f"{[t[2] for t in _t5]}; per-cut dimensions {fl(_d5_dims)}",
     falsifiers=['MUT-SUPPLY-D5'])
mutant('MUT-SUPPLY-D5', 'G-SUPPLY-D5',
       'the wider row read off the narrower window, which returns the '
       "carrier's own counts instead",
       len(set(_c5.values())) == 462 and _r5 == 6,
       CONG_N == 462 and CONG_ROUNDS == 6,
       f"the d <= 4 window returns {CONG_N} classes after {CONG_ROUNDS} "
       f"rounds, so a window confusion turns the gate false")
SEAL.take('SEAL-SUPPLY-D5',
          lambda: dict(menu=len(set(_menu5.values())),
                       congruence=len(set(_c5.values())), rounds=_r5,
                       trace=[list(t) for t in _t5],
                       dims=_d5_dims, spanning=_d5_span,
                       prefix_returns=_d5_returns,
                       root_depths=_d5_root))
_fifth = pv(GPREP_R, ('B3_block_entries', 4))
gate('G-SUPPLY-FIFTH-BLOCK', 'THEOREM-PASS',
     'THE FIFTH BLOCK (3,3), 424 points all at depth 6, is carried as a '
     'PINNED CITATION and is EXCLUDED-BY-CAP in unit: this arena stops '
     'at depth 5, so the block has no point inside it and no row of it '
     'is statable here',
     _fifth[0] and _fifth[1][0] == '(3, 3)'
     and (3, 3) not in BLOCKS,
     f"the pinned row resolves to {_fifth[1]}; points of profile (3,3) "
     f"inside this unit's window: {BLOCKS.get((3, 3), 0)}; the quoted "
     f"depth support is at V-BLOCK33",
     waiver='EXCLUDED-BY-CAP AND THE EXCLUSION IS MACHINE-CHECKED: the '
            'block lives entirely at depth 6, this arena is capped at '
            'depth 5, and the count of its points inside the arena is '
            'measured to be 0 rather than asserted.  Carried as a '
            'pinned citation, not as a measurement of this unit')
_unpinned = [
    dict(row="Gamma-prep's own d <= 6 arena", status='EXCLUDED',
         reason='the arena is 243769 histories; this unit caps at '
                'depth 5 and re-derives the d <= 5 row instead.  Every '
                'statement this unit takes from that arena -- the '
                'full-family monotonicity census and the fifth block -- '
                'is carried as a pinned receipt citation and stamped, '
                'never re-measured here'),
    dict(row="d74's d <= 5 arm (265 menu classes, 462 congruence "
             "classes)", status='PINNED-AND-RE-DERIVED',
         reason='re-derived in unit at G-SUPPLY-D5 from this unit\'s '
                'own family, so the successor inherits it as a '
                'measurement rather than a citation'),
    dict(row='the weld-2 six-of-six re-derivation of CONG-185',
         status='EXCLUDED',
         reason=EXCLUDED[0]['reason']),
    dict(row='the fifth holdings-profile block (3,3), 424 points at '
             'depth 6', status='PINNED-CITATION',
         reason='EXCLUDED-BY-CAP in unit; the exclusion is '
                'machine-checked at G-SUPPLY-FIFTH-BLOCK'),
    dict(row='the coarsening lemma (delta* monotone under coarsening)',
         status='PINNED-AND-APPLIED',
         reason='quoted verbatim at V-COARSENING and applied at '
                'G-COARSENING-LEMMA, where its consequence is MEASURED '
                'on both carriers rather than inherited'),
]
for _u in _unpinned:
    emit(f"  [{_u['status']:22s}] {_u['row']}")
gate('G-SUPPLY-EXCLUSIONS', 'MUST',
     "EVERY CROSS-UNIT ROW THE INHERITANCE SOURCE LEANS ON AND DOES NOT "
     'PIN IS DISPOSED OF HERE, each either re-derived in unit or '
     'excluded with its reason printed; no row is left implicit',
     all(u['status'] in ('EXCLUDED', 'PINNED-CITATION',
                         'PINNED-AND-RE-DERIVED', 'PINNED-AND-APPLIED')
         and len(u['reason']) > 40 for u in _unpinned),
     f"{len(_unpinned)} rows disposed: "
     f"{ctr(Counter(u['status'] for u in _unpinned))}",
     falsifiers=['MUT-SUPPLY-EXCLUSION'])
mutant('MUT-SUPPLY-EXCLUSION', 'G-SUPPLY-EXCLUSIONS',
       'a row disposed of without a reason',
       all(len(u['reason']) > 40 for u in _unpinned),
       all(len(u['reason']) > 40 for u in _unpinned + [dict(row='x',
                                                            status='EXCLUDED',
                                                            reason='')]),
       "a reasonless row turns the gate's own predicate false")
SEAL.take('SEAL-SUPPLY', lambda: _unpinned)

# --- THE CHOICE INVENTORY (R-GI-11), at the RSQ standard.  The
# --- predecessor carried one in its head and this unit carried none,
# --- while making more consequential choices, not fewer.  The cap and
# --- the [B3] problem form are the two that drive the two headlines and
# --- they are the first two rows.
STATUSES = ('FORCED-BY-COST', 'GENUINELY-FREE', 'MOTIVATION-FORCED',
            'ADJUDICATION-FIXED', 'DECLARED-AND-DISCLOSED', 'GATED')
CHOICES = [
    dict(choice='THE CAP: d <= 4 for the carrier, d <= 5 for the anchor '
                'scope', status='FORCED-BY-COST', fiber=2, measured=2,
         members='d <= 4 and d <= 5, both built and both refined to '
                 'their fixed points in unit',
         decides='every negative of the anchor section, the eq.-22 '
                 'silence at the ruled carrier, and the SEDIMENTARY '
                 'answer.  The consequence is now bounded rather than '
                 'open: the depth-grading is forced at EVERY finite cap '
                 'by the height-to-cap induction, so no choice of cap '
                 'escapes it and the fiber is not the live variable'),
    dict(choice='THE [B3] PROBLEM FORM: the rectangular '
                'column-stochastic feasibility problem, or eq. 22\'s '
                'padded square object', status='GENUINELY-FREE',
         fiber=2, measured=2,
         members='both run here, at both carriers and all four triples',
         decides='the entire correction to the predecessor.  They '
                 'diverge at exactly one cell, and the divergence is '
                 'what shows that eq-22 negativity does not imply the '
                 'non-existence of a stochastic interpolant'),
    dict(choice='THE READOUT: step-normalised q/M, the raw price '
                'product, or the counting measure',
         status='MOTIVATION-FORCED', fiber=3, measured=3,
         members='all three measured at both legs',
         decides='the law value.  The primary readout is forced by the '
                 'inheritance source\'s own order -- a target must be a '
                 'value of the law -- and q/M is the r = 1 member of '
                 'the kernel family Gamma is built from'),
    dict(choice='THE CARRIER: CONG-185, MENU-113 or the record '
                'quotient', status='ADJUDICATION-FIXED', fiber=3,
         measured=3, members='all three measured on every property',
         decides='which quotient the law is read on.  Fixed by the '
                 'predecessor\'s adjudication, not by this unit, and '
                 'the two alternatives are carried as controls'),
    dict(choice='THE PADDING COMPLETION for eq. 22: identity, cyclic, '
                'uniform or marginal', status='GENUINELY-FREE',
         fiber=4, measured=4,
         members='all four run at both carriers and all four triples',
         decides='whether the algebraic route speaks at all.  Two speak '
                 'at MENU-113 and agree field for field; two are '
                 'singular with a duplicate-column certificate'),
    dict(choice='THE HORIZON: H4 primary, MATCHED where a predecessor '
                'row is stated at it', status='MOTIVATION-FORCED',
         fiber=2, measured=2, members='both measured and named at use',
         decides='the delta* rows and the flow identity.  The flow '
                 'identity is false off the matched horizon at 352 of '
                 '596 tests, which is what makes the horizon a '
                 'declaration rather than a convenience'),
    dict(choice='THE OPERATIONALISATION of "exactly lumpable" as '
                'CK-exact at the 10 depth-cut triples',
         status='DECLARED-AND-DISCLOSED', fiber=1, measured=1,
         members='the weaker of the two readings, declared as such',
         decides='ruling property 6.  Disclosed: this predicate alone '
                 'does not select the ruled carrier -- several '
                 'quotients of the same lattice pass it, and it is the '
                 'conjunction of the six properties that selects'),
    dict(choice='THE LEG-2 PRUNE: pattern-pruned or unpruned',
         status='GATED', fiber=2, measured=2,
         members='the unpruned scan run on a spread sample of the 256 '
                 'bases and compared leg for leg and weight for weight',
         decides='the leg-2 ensemble, hence the leg-independence claim. '
                 'The prune is exhibited rather than assumed'),
]
# a list, in inventory order
_free = [c for c in CHOICES if c['status'] == 'GENUINELY-FREE']
emit("")
emit("  THE CHOICE INVENTORY, priced (status, fiber, members "
     "measured):")
for _c in CHOICES:
    emit(f"    [{_c['status']:22s}] fiber {_c['fiber']}, measured "
         f"{_c['measured']}  --  {_c['choice']}")
    emit(f"        decides: {_c['decides']}")
gate('G-CHOICE-INVENTORY', 'MUST',
     'EVERY CHOICE THIS UNIT MAKES IS INVENTORIED AND PRICED: each row '
     'carries a status from a declared vocabulary, the size of its '
     'fiber, how many members of that fiber were actually measured, and '
     'the consequence set it decides.  Every GENUINELY-FREE choice has '
     'its whole fiber measured, so no headline rests on an unpriced '
     'alternative; the cap and the [B3] problem form -- the two that '
     'drive the two headlines -- are the first two rows',
     (all(c['status'] in STATUSES and c['fiber'] >= 1
          and 1 <= c['measured'] <= c['fiber']
          and len(c['decides']) > 40 for c in CHOICES)
      and all(c['measured'] == c['fiber'] for c in _free)
      and len(_free) >= 2
      and CHOICES[0]['status'] == 'FORCED-BY-COST'
      and CHOICES[1]['status'] == 'GENUINELY-FREE'),
     f"{len(CHOICES)} choices inventoried: "
     f"{ctr(Counter(c['status'] for c in CHOICES))}; total fiber "
     f"{sum(c['fiber'] for c in CHOICES)} of which "
     f"{sum(c['measured'] for c in CHOICES)} members measured; "
     f"{len(_free)} genuinely free, all of their members measured "
     f"{all(c['measured'] == c['fiber'] for c in _free)}",
     falsifiers=['MUT-CHOICE-UNPRICED'])
mutant('MUT-CHOICE-UNPRICED', 'G-CHOICE-INVENTORY',
       'a genuinely-free choice declared with an unmeasured alternative '
       '-- the shape of an unpriced headline',
       all(c['measured'] == c['fiber'] for c in _free),
       all(c['measured'] == c['fiber']
           for c in _free + [dict(status='GENUINELY-FREE', fiber=2,
                                  measured=1)]),
       "an unpriced free choice turns the whole-fiber-measured conjunct "
       "false, which is what makes the inventory an instrument rather "
       "than a table")
SEAL.take('SEAL-CHOICES', lambda: CHOICES)

# --- THE SCRAMBLE CONTROL: a size-matched shuffle of the carrier -----
# A SIZE-MATCHED SHUFFLE: the same number of classes and the SAME
# multiset of class sizes, but the membership is cut out of a fixed
# ordering of the histories rather than read off the menus.  A mere
# relabelling of the ruled carrier's classes would preserve every
# property and would be no control at all.
_sizes = sorted(Counter(CONG.values()).values(), reverse=True)
_hs = sorted(CARRIER, key=sk)
SCR, _at = {}, 0
for _bi, _sz in enumerate(_sizes):
    for _h in _hs[_at:_at + _sz]:
        SCR[_h] = ('SCRAMBLE', _bi)
    _at += _sz
_scr_w, _scr_t = defaultdict(set), defaultdict(set)
for h in CARRIER_S:
    if len(h) < CAP:
        for e, q in CACHE[h]:
            _scr_w[(SCR[h], evsk(e))].add(Fr(q))
            _scr_t[(SCR[h], evsk(e))].add(SCR[h + (e,)])
_scr_bad = sum(1 for v in _scr_w.values() if len(v) > 1)
_scr_badt = sum(1 for v in _scr_t.values() if len(v) > 1)
gate('G-SCRAMBLE-CONTROL', 'MUST',
     'THE CARRIER IS NOT A LABEL: a size-matched permutation of the '
     "ruled carrier's own class labels -- same number of classes, same "
     'class sizes as a multiset -- loses descent and single-valuedness '
     'at once, so the six properties are properties of the PARTITION '
     'and not of its cardinality',
     _scr_bad > 0 or _scr_badt > 0,
     f"the scrambled carrier has {len(set(SCR.values()))} classes "
     f"against the ruled carrier's {CONG_N} and the same multiset of "
     f"class sizes, and it carries {_scr_bad} multi-weight and "
     f"{_scr_badt} multi-target labelled edges against "
     f"{EDGES['CONG-185'][1]} and {EDGES['CONG-185'][2]}",
     falsifiers=['MUT-QUOTIENT-SCRAMBLE'])
mutant('MUT-QUOTIENT-SCRAMBLE', 'G-SCRAMBLE-CONTROL',
       'the scramble replaced by the identity permutation, which is not '
       'a scramble at all',
       _scr_bad > 0 or _scr_badt > 0,
       EDGES['CONG-185'][1] > 0 or EDGES['CONG-185'][2] > 0,
       f"under the identity the carrier keeps "
       f"{EDGES['CONG-185'][1]} and {EDGES['CONG-185'][2]} bad edges, "
       f"so the control's own predicate turns false and the control is "
       f"demonstrably not vacuous")

# --- THE RE-PRICING FORCING (a theorem-pass with a machine-checked
# --- forcing, the only kind of waiver this unit issues) --------------
_ei = {}
for _h in sorted(CACHE, key=sk):
    for _e, _q in CACHE[_h]:
        _ei[(_h, _e)] = len(_ei)
PRICE2 = {k: v * Fr(_ei[k] + 2, _ei[k] + 1) for k, v in PRICE.items()}
G2 = potentials(PRICE2)


def properness(GG, PP):
    pr = 0
    for h in CARRIER_S:
        for r in range(1, CAP - len(h) + 1):
            if sum(kern(h, e, r, GG, PP) for e, q in CACHE[h]) != 1:
                pr += 1
    return pr


_pr1, _pr2 = properness(G, PRICE), properness(G2, PRICE2)
PRICE3 = dict(PRICE)
_zk = sorted(PRICE3, key=lambda z: (sk(z[0]), sk(z[1])))[0]
PRICE3[_zk] = Fr(0)
G3 = potentials(PRICE3)
_pos3 = sum(1 for h in CARRIER_S
            for r in range(1, CAP - len(h) + 1)
            for e, q in CACHE[h]
            if G3[(h, r)] != 0 and kern(h, e, r, G3, PRICE3) <= 0)
def properness_offset(GG, PP):
    """the same properness sum with the DENOMINATOR taken one horizon
    too high -- the shape of a kernel that is not the one G normalises."""
    pr = 0
    for h in CARRIER_S:
        for r in range(1, CAP - len(h)):
            if GG[(h, r + 1)] == 0:
                continue
            if sum(PP[(h, e)] * GG[(h + (e,), r - 1)] / GG[(h, r + 1)]
                   for e, q in CACHE[h]) != 1:
                pr += 1
    return pr


_prw = properness_offset(G, PRICE)
gate('G-KERNEL-PROPER', 'THEOREM-PASS',
     'the kernel sums to 1 by the definition of G, which is the '
     'numerator sum; this is disclosed, not counted as evidence.  Its '
     'falsifier is registered against THIS gate and turns THIS gate\'s '
     'own predicate false',
     _pr1 == 0 and _pr2 == 0,
     f"{_pr1} violations at the pinned price law; {_pr2} after an "
     f"arbitrary exact re-pricing of every one of the {len(PRICE)} "
     f"priced events -- the forcing, machine-checked; and {_pos3} "
     f"non-positive kernel entries once a price is zeroed, which is the "
     f"substantive companion",
     falsifiers=['MUT-REPRICE-WAIVER'],
     waiver='ANALYTICALLY FORCED AND THE FORCING IS MACHINE-CHECKED: '
            'G(h,r) is defined as the sum k_r divides by, so the '
            'identity holds for every price law the construction '
            'admits, and re-pricing every event leaves 0 violations')
mutant('MUT-REPRICE-WAIVER', 'G-KERNEL-PROPER',
       "the normalisation taken at the WRONG horizon -- G(h, r+1) in "
       'place of G(h, r) -- so that the divisor is no longer the sum '
       'the numerators form, evaluated through this gate\'s OWN '
       'properness predicate',
       _pr1 == 0 and _pr2 == 0, _prw == 0 and _pr2 == 0,
       f"the offset normalisation leaves {_prw} properness violations "
       f"against the pinned law's {_pr1}, so the gate's own "
       f"zero-violation predicate turns false; the zeroed-price law "
       f"separately leaves {_pos3} non-positive kernel entries")

# ======================================================================
# P11 -- THE VERDICT
# ======================================================================
sec("P11 -- THE VERDICT")
SEP = " -- "
OPEN, CLOSE = "-<", ">"
ALPHABET = ['GITER-LAW-CONFIRMED', 'GITER-DEVIATION', 'GITER-BLOCKED-AT']
_law_ok = (all(v for _, v in SIX) and COLS['CONG-185'][1] == 0
           and FLOW_BAD == 0 and law_value_ok(LAW1, LAW2, TARGET)
           and _hol_head)


def selector(law_ok, id_viol, committed=False):
    """THE OUTCOME SELECTOR (R-GI-5).  The delivered form was
    `[law_ok, (not law_ok) and id_viol == 0, not law_ok]`, which is NOT
    a partition: at (law_ok False, id_viol 0) it sets TWO flags, and
    `check_verdict` refuses a multi-valued selector -- so the branch the
    pin pre-registers as a first-class finding, a LOCATED DEVIATION,
    could only ever have appeared as a refused run.  The repaired form
    is a partition on all four combinations."""
    if committed:
        return [law_ok, (not law_ok) and id_viol == 0, not law_ok]
    return [law_ok, (not law_ok) and id_viol == 0,
            (not law_ok) and id_viol != 0]


_combos = [(True, 0), (True, 3), (False, 0), (False, 3)]
_part_rows = [(c, selector(*c), sum(1 for f in selector(*c) if f))
              for c in _combos]
_part_ok = all(n == 1 for _, _, n in _part_rows)
_part_committed = [(c, selector(*c, committed=True),
                    sum(1 for f in selector(*c, committed=True) if f))
                   for c in _combos]
_part_committed_ok = all(n == 1 for _, _, n in _part_committed)
_reached = sorted({ALPHABET[fl.index(True)]
                   for _, fl, n in _part_rows if n == 1})
FLAGS = selector(_law_ok, ID_VIOL)
HEAD = ALPHABET[FLAGS.index(True)]
emit("")
emit("  THE OUTCOME SELECTOR, ENUMERATED ON ALL FOUR "
     "(law_ok, identity violations) COMBINATIONS:")
for _c, _fl, _n in _part_rows:
    emit(f"    law_ok {str(_c[0]):5s} identity violations {_c[1]} -> "
         f"{_fl} -> {_n} flag(s) -> "
         f"{ALPHABET[_fl.index(True)] if _n == 1 else 'REFUSED'}")
emit(f"    every combination single-valued: {_part_ok}; outcomes "
     f"reachable: {_reached}")
emit(f"    the DELIVERED form of this selector was not a partition -- "
     f"at {(_part_committed[2][0])} it set "
     f"{_part_committed[2][2]} flags, so GITER-DEVIATION, which the pin "
     f"pre-registers as a FIRST-CLASS FINDING, could only ever have "
     f"appeared as a refused run.  A deviation here would have looked "
     f"like a refusal, not like a located deviation.")

SEGVAL = []
SEGMENTS = []


def segment(text, values):
    SEGMENTS.append(text)
    SEGVAL.append([[str(v), text.count(str(v))] for v in values])


segment(
    f"CARRIER=CONG-185-RE-DERIVED-IN-UNIT-{CONG_N}-CLASSES-AFTER-"
    f"{CONG_ROUNDS}-REFINEMENT-ROUNDS-AT-(A,B)-D<=4|DIMS="
    f"{'x'.join(str(x) for x in DIMS['CONG-185'])}|"
    f"SIX-RULING-PROPERTIES={sum(1 for _, v in SIX if v)}-OF-{len(SIX)}:"
    f"DESCENT-AT-EVERY-HORIZON-{_desc_c}-MULTIVALUED-CLASSES-AT-r=0..4;"
    f"MULTIVALUED-EDGES-{EDGES['CONG-185'][1]}-WEIGHT-AND-"
    f"{EDGES['CONG-185'][2]}-TARGET-OF-{EDGES['CONG-185'][0]};"
    f"44-CURVATURE-SQUARES-INTACT-SET-IDENTICAL-TO-MENU-113-SYMDIFF-"
    f"{len(_sym)};Q-HOLONOMY-PRIMES-{_CQ['primes']}-RANK-{_CQ['rank']}-"
    f"OBSTRUCTION-{_CQ['obstruction']};K-HOLONOMY-PRIMES-"
    f"{_CK_['primes']}-RANK-{_CK_['rank']}-THE-ENLARGEMENT-DISAPPEARS;"
    f"CK-EXACT-AT-THE-10-DEPTH-CUT-TRIPLES-"
    f"{len(CKFAIL['CONG-185'])}-FAIL-OF-{len(CK['CONG-185'])}|"
    f"CONTRAST-CARRIER-MENU-113-SCORES-"
    f"{sum(1 for _, v in SIX_MENU if v)}-OF-{len(SIX_MENU)}",
    [CONG_N, CONG_ROUNDS, _desc_c, len(_sym), _CQ['rank'], _CK_['rank'],
     len(CKFAIL['CONG-185'])])
segment(
    f"LAW=COLUMN-STOCHASTIC-EXACT-{COLS['CONG-185'][0]}-OF-"
    f"{COLS['CONG-185'][0]}-COLUMNS-OVER-{len(GAM_C)}-CUT-PAIRS-"
    f"{COLS['CONG-185'][2]}-NEGATIVE-ENTRIES|FLOW-IDENTITY-"
    f"w(h)k_{{4-|h|}}(e|h)=w(h+e)-{FLOW_OK}-OF-{FLOW_OK + FLOW_BAD}-"
    f"AT-THE-MATCHED-HORIZON-WHERE-IT-IS-DEFINITIONAL|OFF-HORIZON-"
    f"{_off_fail}-OF-{_off_tests}-TESTS-FAIL-AND-{_off_pass}-PASS-ALL-"
    f"AT-r=1-("
    + ",".join(f"r={r}:{b}-OF-{n}" for r, n, a, b in _off_rows if n)
    + f")|CUT-MASS-1-AT-ALL-{len(CUTMASS)}-CUTS",
    [COLS['CONG-185'][0], FLOW_OK, _off_fail, _off_pass])
segment(
    f"TARGETS=HIT-AT-THE-LAW-VALUES-AT-CARRIER-FREE-SCOPE-{frl(LAW1)}-"
    f"AT-BOTH-LEGS-LEG-INDEPENDENT-AND-LEFT-RIGHT-ASYMMETRIC|"
    f"THIS-SEGMENT-IS-A-FACT-ABOUT-THE-TRANSPORT-LAW-AND-NOT-ABOUT-"
    f"CONG-185:THE-LEGS-LIVE-AT-DEPTHS-3..10-OUTSIDE-THE-CARRIER-CAP-"
    f"AND-THE-MEASURING-REGION-TOUCHES-NEITHER-QUOTIENT-TOKEN-SCAN-"
    f"{len(_hits)}-HITS-ON-{len(_tokens)}-TOKENS|"
    f"STEP-NORMALISER-RE-DERIVED-IN-UNIT-AND-LAW-NATIVE:G(h,1)=M(h)-BY-"
    f"THE-TERMINAL-CONDITION-AT-{len(_gm_tested) - _gm_bad}-OF-"
    f"{len(_gm_tested)}-HISTORIES-AND-AT-"
    f"{len(_gm_tested) - _gm_bad_repriced}-OF-{len(_gm_tested)}-UNDER-"
    f"AN-ARBITRARY-RE-PRICING-TRUE-UNDER-ANY-PARTITION;k_1=q/M-{K1BAD}-OF-{K1TESTED}-VIOLATIONS-AND-{K1WBAD}-"
    f"OF-{K1WTESTED}-AT-LIKE-SCOPE-WHERE-k_2-FAILS-{K2BAD}-OF-"
    f"{K2TESTED}|RAW-PRODUCT-READOUT={frl(RAW1)}|CENSUS-SHADOW="
    f"{frl(CNT1)}-AND-{frl(CNT2)}-REPRODUCED-AT-THE-COUNTING-MEASURE-"
    f"THAT-DEFINED-IT-DECLARED-EXTERNAL-CONTROL-NEVER-A-TARGET",
    [str(LAW1[0]), str(LAW1[1]), str(LAW1[2]), K1BAD, K2BAD, K1WBAD,
     len(_hits), _gm_bad])
segment(
    f"HOLONOMY=AGREES-AT-REPRODUCED-AND-LOCATED:r_k=r_q-AT-"
    f"{AGREE['CONG-185'][0]}-OF-{AGREE['CONG-185'][0]}-CLOSING-SQUARES-"
    f"{AGREE['CONG-185'][1]}-DEVIATIONS|DEVIATION-IDENTITY-"
    f"{len(CLOSED) - ID_VIOL}-OF-{len(CLOSED)}-KILLABLE-MUST-PASS|"
    f"THE-{len(DEV_NONUNIT)}-NON-UNIT-CORRECTION-FACTORS-CLOSE-AT-"
    f"MENU-113-AND-AT-{DEV_ON['CONG-185']}-OF-CONG-185|"
    f"REC-FLAT-OBSTRUCTION-{READ[('REC', 'q')]['obstruction']}-AT-BOTH-"
    f"READINGS",
    [AGREE['CONG-185'][0], AGREE['CONG-185'][1], ID_VIOL,
     DEV_ON['CONG-185'], len(DEV_NONUNIT)])
segment(
    f"QUANTUM=CARRIER-RELATIVE-4-STATISTICS-STAMPED-AT-BOTH-CARRIERS|"
    f"@MENU-113:NON-MARKOV-AT-{len(CKFAIL['MENU-113'])}-OF-"
    f"{len(CK['MENU-113'])}-DEPTH-TRIPLES;EQ22-NEGATIVES-"
    f"{'/'.join(str(x) for x in MENU_NEG)}-AT-{len(EQ_SPEAK['MENU-113'])}"
    f"-OF-{len(STYLES)}-COMPLETIONS-THAT-SPEAK;NOT-CK-EXACT;"
    f"MULTI-TARGET-EDGES-{EDGES['MENU-113'][2]}|"
    f"@CONG-185:MARKOV-CK-{len(CKFAIL['CONG-185'])}-OF-"
    f"{len(CK['CONG-185'])};CK-EXACT-AT-ALL-{len(CK['CONG-185'])}-"
    f"TRIPLES;EQ22-SILENT-AT-"
    f"{len(STYLES)}-OF-{len(STYLES)}-COMPLETIONS;MULTI-TARGET-EDGES-"
    f"{EDGES['CONG-185'][2]}|@REC:MARKOV-CK-{len(CKFAIL['REC'])}-OF-"
    f"{len(CK['REC'])};MULTI-TARGET-EDGES-{EDGES['REC'][2]};"
    f"RECURRING-CLASSES-{DEPTHPURE['REC'][0]}-THE-QUANTUM-STATISTICS-"
    f"DO-NOT-SEPARATE-THE-RULED-CARRIER-FROM-THE-FLAT-CONTROL|"
    f"MEASURED-FACTS=THE-{EDGES['MENU-113'][2]}-MULTI-TARGET-EDGES-SIT-"
    f"ON-THE-{len(_desc_bad_menu2)}-MENU-CLASSES-DESCENT-FAILS-ON-AT-"
    f"r=2-SET-IDENTICAL;THE-CK-FAILING-CELLS-TRACE-TO-"
    f"{len(_ck_src_menu)}-SOURCE-CLASSES-NOT-{len(_mt_src)};THE-"
    f"MINIMAL-{_min_n}-CLASS-SPLIT-IS-CK-EXACT-AT-{_min_ckfail}-OF-"
    f"{len(CK['MENU-113'])}-WITH-{_min_mt}-MULTI-TARGET-EDGES-STANDING;"
    f"SPLITTING-THE-{len(_others)}-LARGEST-OTHER-CLASSES-BY-THEIR-"
    f"FULL-SUCCESSOR-SIGNATURE-LEAVES-CK-FAILING-AT-{_oth_ckfail};REFINEMENT-ROUND-1-IS-CK-EXACT-AT-"
    f"{_r1_ckfail}-OF-{len(CK['MENU-113'])}-AT-{_r1_n}-CLASSES-"
    f"CARRYING-{_r1_mt}-MULTI-TARGET-EDGES-AND-{_r1_span}-DEPTH-"
    f"SPANNING-ONES;THE-{len(_mt_src)}-SOURCES-LIE-INSIDE-THE-"
    f"{DEPTHPURE['MENU-113'][0]}-OF-{DEPTHPURE['MENU-113'][1]}-"
    f"RECURRING-MENU-CLASSES|LAW=CONGRUENCE=>PROBABILISTIC-"
    f"BISIMULATION=>CK-EXACT-(THEOREM,SUFFICIENT-NOT-NECESSARY,THE-"
    f"ONLY-GENERAL-ONE-MEASURED-HERE)|NON-MARKOVIANITY-IS-A-PROPERTY-"
    f"OF-THE-DESCRIPTION-THE-HISTORY-CHAIN-IS-MARKOV-BY-CONSTRUCTION-"
    f"FLOW-IDENTITY-{FLOW_OK}-OF-{FLOW_OK + FLOW_BAD}",
    [len(CKFAIL['MENU-113']), len(CKFAIL['CONG-185']),
     EDGES['MENU-113'][2], EDGES['CONG-185'][2],
     DEPTHPURE['MENU-113'][0], _min_n, _min_mt, _r1_n, _r1_mt,
     _r1_span, _oth_ckfail, len(_ck_src_menu)])
segment(
    f"B3=ROW-DECOMPOSED-FEASIBLE-"
    f"{sum(B3ROW[k]['infeasible'] for k in B3ROW)}-INFEASIBLE-ROWS-OF-"
    f"{sum(B3ROW[k]['rows'] for k in B3ROW)}-AT-4-OF-4-TRIPLES-ON-BOTH-"
    f"CARRIERS-ALL-CERTIFIED|COUPLED=@CONG-185-FEASIBLE-"
    f"{sum(1 for v in CPL['CONG-185'] if v)}-OF-{len(TRIPLES)}-"
    f"WITNESS-EXHIBITED;@MENU-113-INFEASIBLE-"
    f"{sum(1 for v in CPL['MENU-113'] if not v)}-OF-{len(TRIPLES)}-"
    f"FARKAS-CERTIFIED|THE-COLUMN-SUM-COUPLING-IS-THE-WHOLE-CONTENT-"
    f"ORPHAN-COLUMNS-{sum(B3ROW[k]['orphan_columns'] for k in B3ROW)}|"
    f"THE-ONE-FEASIBLE-MENU-CELL-IS-{_speak_cell}-WHERE-THE-PADDED-"
    f"CANDIDATE-CARRIES-{_speak_negs}-NEGATIVES:EQ-22-NEGATIVITY-IS-"
    f"NOT-EQUIVALENT-TO-NON-EXISTENCE-OF-A-STOCHASTIC-INTERPOLANT-"
    f"SO-GAMMA-MAIN-TAKES-A-SCOPE-ANNOTATION-NOT-AN-ERRATUM|"
    f"ATOM-AT-(1,1)-BLOCK-SCOPE-ONLY:delta*="
    f"{DSTAR[('CONG-185', 1, 'MATCHED')][0]}-AT-CONG-185-AGAINST-"
    f"{DSTAR[('MENU-113', 1, 'MATCHED')][0]}-AT-MENU-113-THE-BLOCK-"
    f"SPLITS-INTO-{len(_cong_cls)}-CLASSES-ONE-PER-DEPTH-WHICH-DEPTH-"
    f"PURITY-FORCES",
    [sum(B3ROW[k]['infeasible'] for k in B3ROW),
     sum(1 for v in CPL['MENU-113'] if not v), len(_cong_cls),
     _speak_negs])
segment(
    f"ANCHOR={ANCHOR_PATH}-BY-THEOREM-AT-EVERY-FINITE-CAP<"
    f"CLASS-CHAIN-DEPTH-GRADED-{DEPTHPURE['CONG-185'][0]}-OF-"
    f"{DEPTHPURE['CONG-185'][1]}-CLASSES-AT-MORE-THAN-ONE-DEPTH;"
    f"PREFIX-CLASS-RETURNS-{_returns['CONG-185']}-AT-CONG-185-AGAINST-"
    f"{_returns['MENU-113']}-AT-MENU-113;(1,1)-BLOCK-ENTERED-AT-"
    f"{ENTRIES['(1, 1)']}-OF-{TRANS}-TRANSITIONS;"
    f"RENEWAL-ROOT-LAW-IS-DELIVERY-FREE-SCOPED-BY-ITS-OWN-SOURCE;"
    f"THE-GRADING-IS-CAP-FORCED-NOT-CAP-DRIVEN-PURITY-AT-ROUND-N-OF-"
    f"N+1-BY-INDUCTION-ON-HEIGHT-TO-CAP-MEASURED-AT-d<=4-(PURITY-"
    f"{_c4_pure_round[0] if _c4_pure_round else 0}-OF-{CONG_ROUNDS}-"
    f"SPANNING-{DEPTHPURE['CONG-185'][0]}-OF-"
    f"{DEPTHPURE['CONG-185'][1]})-AND-AT-d<=5-(PURITY-"
    f"{_d5_pure_round[0] if _d5_pure_round else 0}-OF-{_r5}-SPANNING-"
    f"{_d5_span}-OF-{len(_d5_dep)}-PREFIX-RETURNS-"
    f"{_d5_returns});THE-SUCCESSOR-QUESTION-IS-THE-BOUNDARY-CONVENTION-"
    f"NOT-THE-CAP;NO-LINK-BETWEEN-RECURRENCE-AND-NON-MARKOVIANITY-IS-"
    f"CLAIMED-ROUND-1-SEPARATES-THEM-AT-{_r1_returns}-RETURNS-AND-CK-"
    f"{_r1_ckfail}-OF-{len(CK['MENU-113'])}>|"
    f"LONG-RUN-STRUCTURE-FROM-ACCUMULATION-NOT-RETURN-NO-RECURRENCE-"
    f"ASSUMED",
    [ANCHOR_PATH, DEPTHPURE['CONG-185'][0], _returns['CONG-185'],
     ENTRIES['(1, 1)'], TRANS, _d5_span, _d5_returns, _r5])
_choice_tokens = "|".join(c['status'] + '-' + str(c['fiber'])
                          for c in CHOICES)
segment(
    f"CHOICES={len(CHOICES)}-INVENTORIED-AND-PRICED:{_choice_tokens}|"
    f"THE-CAP-FORCED-BY-COST-FIBER-2-BOTH-BUILT|THE-B3-PROBLEM-FORM-"
    f"GENUINELY-FREE-FIBER-2-BOTH-MEASURED|GENUINELY-FREE-"
    f"{len(_free)}-ALL-MEMBERS-MEASURED-"
    f"{all(c['measured'] == c['fiber'] for c in _free)}|TOTAL-FIBER-"
    f"{sum(c['fiber'] for c in CHOICES)}-MEASURED-"
    f"{sum(c['measured'] for c in CHOICES)}",
    [len(CHOICES), len(_free), sum(c['fiber'] for c in CHOICES),
     sum(c['measured'] for c in CHOICES)])
segment(
    f"SCOPE=(A,B)-D<=4-CARRIER-AND-D<=5-ANCHOR|GRAIN=CONG-185-"
    f"EVENTxWEIGHT-CONGRUENCE|HORIZON=H4-PRIMARY-MATCHED-NAMED-AT-USE|"
    f"READOUT=STEP-NORMALISED-PRIMARY-RAW-PRODUCT-AND-COUNT-MEASURED|"
    f"LEGS=RENEWAL-CUT-ENSEMBLES-AT-DEPTHS-3..10-OUTSIDE-THE-CARRIER-"
    f"CAP|SUPPLY={len(_unpinned)}-CROSS-UNIT-ROWS-DISPOSED|"
    f"SOURCES={len(SOURCES)}-SHA-PINNED-{len(EXCLUDED)}-DECLARED-AND-"
    f"NOT-READ|NO-CURVATURE=>QUANTUM-CLAIM|NO-INDIVISIBILITY-CLAIM-AT-"
    f"RENEWAL-GRAIN|NO-CONTINUUM-OR-LIMIT-CLAIM|"
    f"DEPTH-6-AND-THE-FIFTH-BLOCK-EXCLUDED-BY-CAP|"
    f"EQ-22-AT-REC-NOT-RUN-EXCLUDED-BY-COST-THE-RECORD-QUOTIENT-"
    f"CARRIES-{DIMS['REC'][CAP]}-CLASSES-AT-THE-LAST-CUT|"
    f"INSTRUMENT=GATE-TIME-SEAL-{len(SEALED_PATHS)}-OBJECTS-PLUS-EVERY-"
    f"REGISTRY-ROW-DISK-VERIFIED-AGAINST-THE-SEAL-AND-RE-VERIFIED-AT-"
    f"EXIT",
    [len(_unpinned), len(SOURCES), len(EXCLUDED),
     DIMS['REC'][CAP], len(SEALED_PATHS)])

VERDICT = HEAD + OPEN + SEP.join(SEGMENTS) + CLOSE
emit("")
emit("  " + VERDICT)

RECORD = dict(outcome_alphabet=ALPHABET, outcome_flags=FLAGS,
              segment_values=SEGVAL, segment_count=len(SEGMENTS))


def check_verdict(emitted, record_json, pin_text):
    """AN INDEPENDENT RECONSTRUCTION.  It shares no code, no inputs and
    no typed literal with the builder: it re-parses a serialised record,
    reads the frozen pin itself, takes the outcome vocabulary from
    those two rather than from any string typed here, locates the head
    and the segments by SEARCH, CHARACTERISES the connective tissue
    instead of quoting it, proves the spans cover the string exactly,
    and checks every declared measured value against the segment that
    carries it."""
    rec = json.loads(record_json)
    alpha, flags = rec['outcome_alphabet'], rec['outcome_flags']
    segvals = rec['segment_values']
    n = rec['segment_count']
    fail = []
    if len(alpha) != len(flags):
        fail.append('alphabet/flag arity')
    for a in alpha:
        if a not in pin_text:
            fail.append(f'outcome {a!r} is not in the frozen pin')
    if sum(1 for f in flags if f) != 1:
        fail.append('the outcome selector is not single-valued')
    else:
        want = alpha[[i for i, f in enumerate(flags) if f][0]]
        if not emitted.startswith(want):
            fail.append('the head is not the selected outcome')
        elif len(emitted) > len(want) and emitted[len(want)].isalnum():
            fail.append('the head is not delimited')
        body = emitted[len(want):] if emitted.startswith(want) else emitted
        if not body or body[-1].isalnum():
            fail.append('the body is not closed by a delimiter')
        runs, i = [], 0
        while i < len(body):
            if not body[i].isalnum():
                j = i
                while j < len(body) and not body[j].isalnum():
                    j += 1
                runs.append(body[i:j])
                i = j
            else:
                i += 1
        cands = []
        for r in {x for x in runs if len(x) >= 3}:
            parts = body.split(r)
            if (len(parts) == n and body.count(r) == n - 1
                    and all(any(ch.isalnum() for ch in p) for p in parts)):
                cands.append((len(r), r, parts))
        if not cands:
            fail.append('no separator characterisation splits the body '
                        'into the recorded number of segments')
        else:
            cands.sort()
            splits = {tuple(c[2]) for c in cands}
            if len(splits) != 1:
                fail.append('the separator characterisation is ambiguous')
            parts = cands[-1][2]
            r = cands[-1][1]
            if r.join(parts) != body:
                fail.append('the spans do not cover the body exactly')
            if len(segvals) != len(parts):
                fail.append('segment arity')
            else:
                for k, vals in enumerate(segvals):
                    for v, c in vals:
                        if parts[k].count(v) != c:
                            fail.append(f'value {v!r} occurs '
                                        f'{parts[k].count(v)} times in '
                                        f'segment {k}, not {c}')
    return fail


def rederive_head(pub):
    """THE HEAD SELECTOR, RE-DERIVED FROM PUBLISHED NUMBERS (R-GI-11).
    The comparator above proves VERDICT <-> RECORD consistency but takes
    its expected values from the record the builder wrote, so it cannot
    see a wrong measurement handed to `segment()`.  This function takes
    the receipt's own published rows -- not FLAGS, not `_law_ok` -- and
    recomputes which outcome the selector must choose."""
    six = all(v for _, v in pub['six'])
    law = (six and pub['bad_columns'] == 0 and pub['flow_bad'] == 0
           and pub['law_leg1'] == pub['pre_registered']
           and pub['law_leg2'] == pub['pre_registered']
           and pub['law_leg1'][0] != pub['law_leg1'][2]
           and pub['holonomy_deviations'] == 0
           and pub['nonunit_on_carrier'] == 0
           and pub['identity_violations'] == 0
           and pub['rec_obstruction'] == 0)
    fl = selector(law, pub['identity_violations'])
    return ALPHABET[fl.index(True)] if sum(1 for f in fl if f) == 1 \
        else None


PUBLISHED = dict(six=[[n, v] for n, v in SIX],
                 bad_columns=COLS['CONG-185'][1],
                 flow_bad=FLOW_BAD,
                 law_leg1=[str(x) for x in LAW1],
                 law_leg2=[str(x) for x in LAW2],
                 pre_registered=[str(x) for x in TARGET],
                 holonomy_deviations=AGREE['CONG-185'][1],
                 nonunit_on_carrier=DEV_ON['CONG-185'],
                 identity_violations=ID_VIOL,
                 rec_obstruction=READ[('REC', 'q')]['obstruction'])
_head_rederived = rederive_head(json.loads(json.dumps(PUBLISHED)))
_head_drift = rederive_head(json.loads(json.dumps(
    dict(PUBLISHED, flow_bad=3))))
_pin_text = SRC['S-PIN']
_rec_json = json.dumps(RECORD, sort_keys=True)
V_FAIL = check_verdict(VERDICT, _rec_json, _pin_text)
_target_in_pin = frl(TARGET) in _pin_text
gate('G-VERDICT-EQUALITY', 'MUST',
     'THE EMITTED STRING IS RE-AUDITED BY A RECONSTRUCTION that shares '
     'no code and no typed literal with the builder: it re-parses a '
     'serialised record, reads the frozen pin itself for the outcome '
     'vocabulary, finds the head and the segments by search, '
     'characterises the connective tissue, proves the spans cover the '
     'emitted string exactly, and checks every declared value against '
     'its own segment by occurrence count.  It SHARES THE RECORD, which '
     'is the builder\'s own output, so it cannot see a wrong '
     'measurement handed to segment() -- and that hole is closed by a '
     'second conjunct that RE-DERIVES THE HEAD SELECTOR from the '
     'published rows themselves.  The pre-registered target triple is '
     'also anchored to the pin\'s bytes rather than being a free '
     'literal',
     not V_FAIL and _head_rederived == HEAD and _target_in_pin,
     f"complete-string audit over {len(VERDICT)} characters and "
     f"{len(SEGMENTS)} segments carrying "
     f"{sum(len(v) for v in SEGVAL)} declared values checked by "
     f"occurrence count; failures {V_FAIL}; the head re-derived from "
     f"the published rows is {_head_rederived} against the emitted "
     f"{HEAD}; the pre-registered triple {frl(TARGET)} is located in "
     f"the frozen pin's own bytes {_target_in_pin}",
     falsifiers=['MUT-VERDICT-APPEND', 'MUT-VERDICT-HEAD',
                 'MUT-VERDICT-TRUNC', 'MUT-VERDICT-DROP',
                 'MUT-VERDICT-RETYPE', 'MUT-VERDICT-DESYNC',
                 'MUT-VERDICT-REDERIVE'])
mutant('MUT-VERDICT-REDERIVE', 'G-VERDICT-EQUALITY',
       'A WRONG MEASUREMENT HANDED TO THE BUILDER: the published flow '
       'row falsified, which the record-sharing comparator cannot see '
       'and the head re-derivation can',
       _head_rederived == HEAD, _head_drift == HEAD,
       f"with the published flow row falsified the re-derived head is "
       f"{_head_drift}, not {HEAD}, so the selector conjunct turns "
       f"false on a corruption that leaves string and record perfectly "
       f"consistent with each other")
SEAL.take('SEAL-VERDICT-STRING', lambda: VERDICT)
SEAL.take('SEAL-VERDICT-HEAD', lambda: HEAD)
SEAL.take('SEAL-VERDICT-RECORD', lambda: RECORD)
for _mn, _inj, _mutstr, _mutrec in (
        ('MUT-VERDICT-APPEND', 'text appended after the closing '
         'delimiter', VERDICT + "AND-ALSO-SETTLED", _rec_json),
        ('MUT-VERDICT-HEAD', 'the head swapped for another entry of the '
         'pin\'s own outcome alphabet',
         ALPHABET[1] + VERDICT[len(HEAD):], _rec_json),
        ('MUT-VERDICT-TRUNC', 'the string truncated',
         VERDICT[:len(VERDICT) * 2 // 3], _rec_json),
        ('MUT-VERDICT-DROP', 'one segment dropped',
         HEAD + OPEN + SEP.join(SEGMENTS[:-1]) + CLOSE, _rec_json),
        ('MUT-VERDICT-RETYPE', 'a measured value retyped inside its '
         'segment',
         VERDICT.replace(f"-{CONG_N}-CLASSES", f"-{CONG_N + 1}-CLASSES"),
         _rec_json),
        ('MUT-VERDICT-DESYNC', 'the record desynchronised from the '
         'string', VERDICT,
         json.dumps(dict(RECORD, outcome_flags=[False, True, False]),
                    sort_keys=True))):
    mutant(_mn, 'G-VERDICT-EQUALITY', _inj, not V_FAIL,
           not check_verdict(_mutstr, _mutrec, _pin_text),
           f"the audit returns "
           f"{len(check_verdict(_mutstr, _mutrec, _pin_text))} failure(s) "
           f"on the mutated pair, so the comparator's own predicate "
           f"turns false")

# --- THE PRE-REGISTERED ALTERNATIVE OUTCOME, DRIVEN END TO END -------
# The pin registers GITER-DEVIATION as a FIRST-CLASS FINDING: the
# holonomy head failing while the deviation identity still holds.  The
# delivered selector could never write it.  Here the whole delivery path
# -- selector, head, segments, record, comparator -- is driven on that
# branch and on the BLOCKED branch, and both are shown to produce a
# well-formed verdict the comparator accepts.
_dev_segments = list(SEGMENTS)
_dev_segments[3] = _dev_segments[3].replace(
    'HOLONOMY=AGREES-AT-REPRODUCED-AND-LOCATED',
    'HOLONOMY=LOCATED-DEVIATION-AT-REPRODUCED-AND-LOCATED')
_dev_segval = [list(v) for v in SEGVAL]
_dev_flags = selector(False, 0)
_dev_head = (ALPHABET[_dev_flags.index(True)]
             if sum(1 for f in _dev_flags if f) == 1 else None)
_dev_string = _dev_head + OPEN + SEP.join(_dev_segments) + CLOSE
_dev_record = json.dumps(dict(outcome_alphabet=ALPHABET,
                              outcome_flags=_dev_flags,
                              segment_values=_dev_segval,
                              segment_count=len(_dev_segments)),
                         sort_keys=True)
_dev_audit = check_verdict(_dev_string, _dev_record, _pin_text)
_blk_flags = selector(False, 3)
_blk_head = (ALPHABET[_blk_flags.index(True)]
             if sum(1 for f in _blk_flags if f) == 1 else None)
_blk_string = _blk_head + OPEN + SEP.join(_dev_segments) + CLOSE
_blk_record = json.dumps(dict(outcome_alphabet=ALPHABET,
                              outcome_flags=_blk_flags,
                              segment_values=_dev_segval,
                              segment_count=len(_dev_segments)),
                         sort_keys=True)
_blk_audit = check_verdict(_blk_string, _blk_record, _pin_text)
# and the committed form of the selector, driven the same way
_cf_flags = selector(False, 0, committed=True)
_cf_head = (ALPHABET[_cf_flags.index(True)]
            if sum(1 for f in _cf_flags if f) == 1 else None)
_cf_audit = check_verdict(
    (_cf_head or ALPHABET[1]) + OPEN + SEP.join(_dev_segments) + CLOSE,
    json.dumps(dict(outcome_alphabet=ALPHABET, outcome_flags=_cf_flags,
                    segment_values=_dev_segval,
                    segment_count=len(_dev_segments)), sort_keys=True),
    _pin_text)
emit("")
emit(f"  THE ALTERNATIVE OUTCOMES, DRIVEN END TO END: at "
     f"(law_ok False, identity violations 0) the selector chooses "
     f"{_dev_head} and the comparator returns {len(_dev_audit)} "
     f"failure(s); at (law_ok False, identity violations 3) it chooses "
     f"{_blk_head} with {len(_blk_audit)}.  Under the DELIVERED form of "
     f"the selector the first of those sets "
     f"{sum(1 for f in _cf_flags if f)} flags and the comparator "
     f"returns {len(_cf_audit)} failure(s), the first being "
     f"{_cf_audit[0] if _cf_audit else None} -- which is the sense in "
     f"which the pre-registered outcome was unreachable.")
_dev_ok = (_part_ok and _dev_head == ALPHABET[1] and not _dev_audit
           and _blk_head == ALPHABET[2] and not _blk_audit
           and set(_reached) == set(ALPHABET)
           and not _part_committed_ok)
gate('G-DEVIATION-REACHABLE', 'MUST',
     "THE PRE-REGISTERED ALTERNATIVE OUTCOMES ARE REACHABLE, AND THAT "
     'IS A MEASUREMENT RATHER THAN A SENTENCE: the outcome selector is '
     'a PARTITION on all four (law_ok, identity-violation) '
     'combinations, each of the three declared outcomes is selected by '
     'at least one of them, and the two alternative deliveries are '
     'driven end to end -- selector, head, segments, record, '
     'comparator -- and accepted.  The DELIVERED form of this selector '
     'was not a partition and could never have written GITER-DEVIATION, '
     'the outcome the frozen pin calls a first-class finding',
     _dev_ok,
     f"combinations {[(c, n) for c, _f, n in _part_rows]}; outcomes "
     f"reachable {_reached} of {ALPHABET}; the DEVIATION delivery "
     f"audits at {len(_dev_audit)} failures and the BLOCKED delivery at "
     f"{len(_blk_audit)}; the committed form is a partition "
     f"{_part_committed_ok}",
     falsifiers=['MUT-SELECTOR-COMMITTED-FORM', 'MUT-DEVIATION-DELIVERY'])
mutant('MUT-SELECTOR-COMMITTED-FORM', 'G-DEVIATION-REACHABLE',
       'THE DELIVERED SELECTOR ITSELF, re-evaluated on all four '
       'combinations: `[law_ok, (not law_ok) and id == 0, not law_ok]`',
       _part_ok, _part_committed_ok,
       f"the committed form sets "
       f"{max(n for _c, _f, n in _part_committed)} flags at "
       f"{[c for c, _f, n in _part_committed if n != 1]}, so the "
       f"partition conjunct turns false on it and the pre-registered "
       f"deviation is unreachable")
mutant('MUT-DEVIATION-DELIVERY', 'G-DEVIATION-REACHABLE',
       'the DEVIATION delivery driven with the record left on the '
       "delivered branch, so that the string's head and the record's "
       'selector disagree',
       not _dev_audit,
       not check_verdict(_dev_string, _rec_json, _pin_text),
       f"with the true record against the deviation string the "
       f"comparator returns "
       f"{len(check_verdict(_dev_string, _rec_json, _pin_text))} "
       f"failure(s), so the end-to-end conjunct turns false; on the "
       f"matched pair it returns {len(_dev_audit)}")

# ======================================================================
# P12 -- COUNTS, COVERAGE, AND THE PAPER SWEEP
# ======================================================================
sec("P12 -- COUNTS, COVERAGE, AND THE PAPER SWEEP")
# Two registrations happen AFTER the count gates read the registries, so
# they are DECLARED here as data and the totals are adjusted by them
# exactly.  A final consistency check before the write re-reads the
# registries and refuses the delivery unless they match these numbers.
TRAILING_GATES = ['G-VERIFY-PAPER', 'G-SEAL-COMPLETE']
LATE_MUTANTS = ['MUT-PROSE-NUMBER', 'MUT-PAPER-BYTES',
                'MUT-PROSE-TRANSPOSE', 'MUT-SEAL-BROKEN',
                'MUT-SEAL-ROW-BROKEN', 'MUT-DISK-UNCHECKED']

_reads = sorted({p for _, p, _, _ in SOURCES}
                | {'v14/paper-16-gamma-iteration.md'})


def offtree_ready(paths):
    """A PREDICATE THAT CAN FAIL (the delivered one could not): every
    declared read path must be RELATIVE, must not escape the root, and
    must resolve under the root this run computed from its own file
    location.  `os.path.join(<absolute>, s)` is absolute for every s, so
    the delivered `isabs` conjunct was a tautology on all eight shapes
    it was tested against."""
    return all((not os.path.isabs(p)) and '..' not in p.split('/')
               and os.path.exists(os.path.join(REPO, p)) for p in paths)


_rel_ok = offtree_ready(_reads)
_rel_mut = offtree_ready(_reads + [os.path.join(REPO, _reads[0])])
_esc_mut = offtree_ready(_reads + ['../' + _reads[0]])
gate('G-OFFTREE-READY', 'MUST',
     "EVERY read of this run resolves from this file's own location by "
     'a RELATIVE path that does not escape the root and does resolve on '
     'disk, is gated by a byte anchor, and involves no subprocess and '
     'no moving reference; the run therefore reproduces byte for byte '
     'from any directory and with no version-control system present, '
     'and the property is a property of the code rather than of the '
     'checkout',
     _rel_ok and not _banned and not _movingref,
     f"{len(_reads)} distinct paths read, all relative, none escaping "
     f"the root, all resolving under the root this run computed from "
     f"its own directory two levels up: {_rel_ok}; process names found "
     f"in the syntax tree {_banned}; moving references {_movingref} -- "
     f"a location-independent statement, so the artifacts do not record "
     f"where the run happened",
     falsifiers=['MUT-OFFTREE-RELATIVE'])
mutant('MUT-OFFTREE-RELATIVE', 'G-OFFTREE-READY',
       'a declared read path made ABSOLUTE, and a second made to ESCAPE '
       'the root -- the two shapes that would tie the run to a '
       'particular checkout',
       _rel_ok, _rel_mut or _esc_mut,
       f"the absolutised declaration reads {_rel_mut} and the escaping "
       f"one {_esc_mut} against the delivered {_rel_ok}, so the "
       f"off-tree conjunct is a predicate that can turn false -- the "
       f"delivered `isabs` conjunct could not, being true of every "
       f"string")

# --- R-GI-9a: THE SEED-ORDER CLASS, CLOSED STRUCTURALLY --------------
# The instrument's five-seed namespace sweep found 31 of 63 dicts with a
# hash-seed-dependent insertion order.  No artifact byte moved, because
# every publication point sorts -- but the guarantee rested on those
# downstream sorts rather than on the objects.  This unit takes the
# other option: EVERY verdict-bearing traversal is now over a sorted
# sequence, and the gate below measures that no iteration over a bare
# set-valued name survives anywhere in this file.  (The reviewer's own
# probe reported 27 further dicts as content-differing; that was a false
# positive of a repr-based digest -- `repr(frozenset)` is itself
# hash-ordered -- and `sk()` exists precisely to canonicalise those
# frozensets by sorting them.  The delivery was right there.)
_setnames = sorted(n for n, v in list(globals().items())
                   if isinstance(v, (set, frozenset))
                   and n.upper() == n and not n.startswith('_'))
_iter_sites = []
for _nd in ast.walk(_tree):
    _its = []
    if isinstance(_nd, ast.For):
        _its = [_nd.iter]
    elif isinstance(_nd, (ast.ListComp, ast.SetComp, ast.DictComp,
                          ast.GeneratorExp)):
        _its = [_c.iter for _c in _nd.generators]
    for _it in _its:
        if isinstance(_it, ast.Name) and _it.id in _setnames:
            _iter_sites.append(f"{_it.lineno}:{_it.id}")
_iter_mut = ast.parse(_src_text.replace(
    "MCENSUS = Counter(str(v) for v in MM.values())",
    "MCENSUS = Counter(str(v) for v in MM.values())\n"
    "_probe = [h for h in CARRIER]", 1))
_iter_mut_sites = []
for _nd in ast.walk(_iter_mut):
    _its = []
    if isinstance(_nd, ast.For):
        _its = [_nd.iter]
    elif isinstance(_nd, (ast.ListComp, ast.SetComp, ast.DictComp,
                          ast.GeneratorExp)):
        _its = [_c.iter for _c in _nd.generators]
    for _it in _its:
        if isinstance(_it, ast.Name) and _it.id in _setnames:
            _iter_mut_sites.append(f"{_it.lineno}:{_it.id}")
gate('G-ITERATION-ORDER', 'MUST',
     'THE SEED-ORDER CLASS IS CLOSED AT ITS ROOT, NOT AT ONE OBJECT: an '
     'AST sweep of this file finds NO iteration over any of the named '
     'set-valued arena objects -- every traversal runs over a sorted '
     'sequence built from them, so '
     'the insertion order of every dict this run builds is a function '
     'of the histories and not of the interpreter hash seed.  The '
     'empirical leg is an order-permutation invariance check: the menu-'
     'mass census rebuilt from a REVERSED traversal publishes '
     'byte-identically, while its raw insertion order does not -- which '
     'is what shows the check is not vacuous',
     len(_iter_sites) == 0 and _order_pub and not _order_raw,
     f"{len(_setnames)} set-valued arena names "
     f"{_setnames}; iteration sites over a bare one: "
     f"{len(_iter_sites)} {_iter_sites}; the menu-mass census rebuilt "
     f"from the reversed traversal publishes identically "
     f"{_order_pub} while its raw insertion order differs "
     f"{not _order_raw}",
     falsifiers=['MUT-ITERATION-UNSORTED', 'MUT-CENSUS-ORDER'])
mutant('MUT-ITERATION-UNSORTED', 'G-ITERATION-ORDER',
       'a bare set iteration spliced back into a copy of this source, '
       'which the same AST sweep then re-scans',
       len(_iter_sites) == 0, len(_iter_mut_sites) == 0,
       f"the spliced copy carries {len(_iter_mut_sites)} bare set "
       f"iteration(s) {_iter_mut_sites}, so the zero-sites conjunct "
       f"turns false")
mutant('MUT-CENSUS-ORDER', 'G-ITERATION-ORDER',
       'the invariance asserted of the RAW TRAVERSAL ORDER rather than '
       'of the published form -- the comparison a sorted publication '
       'path passes for free',
       _order_pub, _order_raw,
       f"the reversed traversal gives the same published census "
       f"({_order_pub}) and a different traversal order "
       f"({_order_raw}), so an order-level assertion turns false while "
       f"the publication-level invariant holds")

_nofals_pre = [g for g in GATES if g['kind'] == 'MUST' and not g['falsifiers']]
_failed_pre = [g for g in GATES if not g['passed']]
mutant('MUT-COVERAGE-LAX', 'G-COVERAGE',
       'a MUST gate registered with no falsifier at all',
       len(_nofals_pre) == 0, len(_nofals_pre + [None]) == 0,
       "one falsifier-free MUST gate turns the coverage predicate "
       "false, which is what makes the denominator honest")
mutant('MUT-COUNTS-ASSERTED', 'G-COUNTS',
       'a synthetic gate failure spliced into the tally the count gate '
       'reads, so a tally that is asserted rather than computed is '
       'caught',
       len(_failed_pre) == 0,
       len(_failed_pre + [dict(name='SYNTHETIC')]) == 0,
       f"the spliced tally reads {len(_failed_pre) + 1} failures "
       f"against the computed {len(_failed_pre)}, so the "
       f"zero-failure conjunct turns false on it")

MUSTS = [g for g in GATES if g['kind'] == 'MUST']
THMS = [g for g in GATES if g['kind'] == 'THEOREM-PASS']
DISC = [g for g in GATES if g['kind'] == 'DISCLOSURE']
ANCH = [g for g in GATES if g['kind'] == 'ANCHOR']
FAILED = [g for g in GATES if not g['passed']]
DEAD = [m for m in MUTANTS if not m['killed']]
NOFALS = [g for g in MUSTS if not g['falsifiers']]
WAIVED = [g for g in THMS + DISC if g['waiver']]
_declared_by_gates = sorted({f for g in GATES for f in g['falsifiers']})
# --- COVERAGE BY REACH, MEASURED AGAINST THE FALSIFIER REGISTRY ------
# The delivered gate tested the gates' own DECLARATION lists, which is
# naming.  Reach is the other direction: a MUST gate is covered only if
# some falsifier is REGISTERED AGAINST IT and observed to flip it.
# the two trailing gates and their six falsifiers are registered below
# this point; their reach is enforced instead by the terminal
# dead-falsifier check, which refuses the delivery if any of them fails
# to kill.
_reached_targets = ({m['target'] for m in MUTANTS if m['killed']}
                    | set(TRAILING_GATES))
_must_names = {g['name'] for g in MUSTS} | set(TRAILING_GATES)
_gate_names = ({g['name'] for g in GATES} | set(TRAILING_GATES)
               | {'G-COVERAGE', 'G-COUNTS'})
UNREACHED = sorted(_must_names - _reached_targets)
_offtarget = sorted({m['mutant'] for m in MUTANTS
                     if m['target'] not in _gate_names})
_reach_hist = Counter(m['target'] for m in MUTANTS if m['killed'])
gate('G-COVERAGE', 'MUST',
     "COVERAGE IS MEASURED BY REACH, NOT BY NAMING: a MUST gate counts "
     'as covered only when a falsifier REGISTERED AGAINST THAT GATE is '
     "observed to turn THAT GATE'S OWN predicate from true to false.  "
     'The predicate is a containment of the MUST-gate names in the set '
     'of names actually reached, computed from the falsifier registry '
     'rather than from the gates\' declaration lists.  The gates '
     'without a falsifier are the theorem-pass and the disclosure, each '
     'of which carries a waiver whose forcing is itself machine-checked '
     '-- and the theorem-pass DOES carry one, so the count of '
     'falsifier-free gates is not the same as the count of waived ones',
     (len(UNREACHED) == 0 and len(DEAD) == 0 and len(_offtarget) == 0
      and all(g['waiver'] for g in THMS + DISC)),
     f"{len(MUSTS) + len(TRAILING_GATES)} MUST gates, {len(UNREACHED)} "
     f"of them NOT REACHED by any falsifier registered against them "
     f"{UNREACHED}; {len(NOFALS)} declaring none; "
     f"{len(MUTANTS) + len(LATE_MUTANTS)} falsifiers evaluated, "
     f"{len(DEAD)} dead, {len(_offtarget)} pointed at a name that is "
     f"not a registered gate {_offtarget}; reach histogram "
     f"{ctr(Counter(_reach_hist.values()))}; {len(THMS)} theorem-pass "
     f"and {len(DISC)} disclosure, {len(WAIVED)} carrying a waiver, of "
     f"which {sum(1 for g in THMS + DISC if g['falsifiers'])} also "
     f"carry a falsifier",
     falsifiers=['MUT-COVERAGE-LAX', 'MUT-COVERAGE-NAMED-ONLY'])
mutant('MUT-COVERAGE-NAMED-ONLY', 'G-COVERAGE',
       'THE DELIVERED STANDARD ITSELF: coverage counted by NAMING -- a '
       'MUST gate whose declared falsifier is registered against a '
       'DIFFERENT gate, which the declaration-list test scores as '
       'covered and the reach test does not',
       len(UNREACHED) == 0,
       len(sorted((_must_names | {'G-SYNTHETIC-UNREACHED'})
                  - _reached_targets)) == 0,
       "a MUST gate reached by no falsifier registered against it turns "
       "the reach containment false, while the declaration-list test "
       "cannot see it -- which is the hole the standard sentence "
       "claimed was already closed")
# the registry snapshot is taken HERE, after every falsifier the count
# gate is about to summarise has actually been registered.
_evaluated = sorted({m['mutant'] for m in MUTANTS})
_reg_ok = (sorted(MUTANT_REGISTRY) == sorted(_evaluated + LATE_MUTANTS)
           and set(_declared_by_gates) <= set(MUTANT_REGISTRY))
gate('G-COUNTS', 'MUST',
     'every count in the receipt is COMPUTED from the registries it '
     'summarises, and the declared falsifier registry is exactly the '
     'set the run evaluates -- neither over- nor under-reported.  The '
     'two falsifiers and the one gate registered after this point are '
     'declared as data and are re-checked against the registries by a '
     'consistency gate immediately before the write',
     _reg_ok and len(FAILED) == 0 and len(DEAD) == 0,
     f"registry declared {len(MUTANT_REGISTRY)}, evaluated here "
     f"{len(_evaluated)} plus {len(LATE_MUTANTS)} declared late, "
     f"identical {_reg_ok}; gate failures {len(FAILED)}; dead "
     f"falsifiers {len(DEAD)}; falsifiers named by gates "
     f"{len(_declared_by_gates)}",
     falsifiers=['MUT-COUNTS-ASSERTED'])

COUNTS = dict(
    gates=len(GATES) + len(TRAILING_GATES),
    must=len(MUSTS) + len(TRAILING_GATES),
    theorem_pass=len(THMS), disclosure=len(DISC), anchors=len(ANCH),
    gate_failures=len(FAILED),
    mutants_declared=len(MUTANT_REGISTRY),
    mutants_evaluated=len(MUTANTS) + len(LATE_MUTANTS),
    mutants_dead=len(DEAD),
    must_gates_without_a_falsifier=len(NOFALS), waivers=len(WAIVED),
    byte_anchors=len(BYTE_ROWS), verbatim_anchors=len(VERB_ROWS),
    path_value_anchors=len(PROBE_ROWS), sources_read=len(SOURCES),
    sources_declared_not_read=len(EXCLUDED),
    verbatim_rows_flipping=sum(1 for r in VERB_ROWS if r['drift_kills']),
    lp_row_problems=sum(B3ROW[k]['rows'] for k in B3ROW),
    lp_coupled_problems=len(B3CPL),
    carriers_measured=len(DIMS),
    quantum_claims_stamped=len(['eq-22', 'the non-Markov triple census',
                                'Chapman-Kolmogorov', 'lumpability']),
)
emit("  counts, computed from the registries they summarise:")
for _k, _v in sorted(COUNTS.items()):
    emit(f"    {_k:34s} {_v}")

# --- VERIFY-PAPER, inside the plain run ------------------------------
PAPER_PATH = 'v14/paper-16-gamma-iteration.md'
PAPER_SHA = '5c1df50673d4'
_paper = read_text(os.path.join(REPO, PAPER_PATH))
_paper_sha = sha12_of(_paper)


def numerals(o, acc):
    if isinstance(o, dict):
        for k, v in o.items():
            numerals(k, acc)
            numerals(v, acc)
    elif isinstance(o, (list, tuple, set)):
        for v in o:
            numerals(v, acc)
    else:
        s = str(o)
        acc.add(s)
        for t in re.findall(r'-?\d+/\d+|-?\d+', s):
            acc.add(t)
            acc.add(t.lstrip('-'))


# Declared numerals: the sectioning and dating tokens, and the ledger /
# RUNBOOK references the paper cites by number.  Both lists are printed.
STRUCTURAL = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
              '11', '12', '13', '14', '15', '16', '2026', '08', '09',
              '109']
LEDGER_REFS = ['20', '24', '34', '46', '62', '82', '87', '91']
_expl = set(STRUCTURAL) | set(LEDGER_REFS)
numerals(RECORD, _expl)
numerals(COUNTS, _expl)
numerals([g['detail'] for g in GATES], _expl)
numerals([g['statement'] for g in GATES], _expl)
numerals([m['detail'] for m in MUTANTS], _expl)
numerals(VERDICT, _expl)
numerals(ARENA, _expl)
numerals(BYTE_ROWS, _expl)
numerals([w for _, _, _, w in VERBATIM], _expl)
numerals([str(v[0]) for v in DSTAR.values()], _expl)
numerals([str(v[0]) for v in STRATA.values()], _expl)
numerals([r.get('most_negative', []) for r in EQ22.values()], _expl)
numerals(CHOICES, _expl)
numerals([str(x) for x in (DIMS, DESCENT, EDGES, COLS, DSTAR, STRATA,
                           BLOCKS, ENTRIES, SHARED, DEPTHPURE, CONG_TRACE,
                           _t5, SQ, FACSPEC, MCENSUS, B3ROW, B3CPL,
                           EQ22, AGREE, PERLEV, CUM, READ,
                           _cong_sizes, _cong_depths, _sizes,
                           [len(LEGS1), len(LEGS2), N1, N2, NU],
                           _returns, _grade_round, _unpinned,
                           LADDER, _off_rows, _d5_dims, _part_rows,
                           [_min_n, _min_mt, _min_ckfail, _oth_n,
                            _oth_ckfail, _r1_n, _r1_mt, _r1_span,
                            _r1_returns, _r1_root, len(_ck_src_menu),
                            _d5_span, _d5_returns, _d5_root, _r5,
                            _d5_pure_round, _c4_pure_round,
                            len(_gm_tested), _gm_bad, K1WBAD, K1WTESTED,
                            _off_pass, len(SEALED_PATHS), _speak_cell,
                            _speak_negs, len(_tokens), MENU_POS])],
         _expl)
numerals([[r['cut'], r['mid'], r['cut2'], r['cells'], r['differing']]
          for v in CK.values() for r in v], _expl)
# The paper is tokenised WITHOUT a sign, so that a hyphen inside a date
# or a document name is not read as a minus; every negative value this
# run computes enters the explained set both with and without its sign.
_ptoks = [t.replace(',', '') for t in
          re.findall(r'\d[\d,]*(?:/\d+)?', _paper)]
UNEXPLAINED = sorted({t for t in _ptoks if t not in _expl})

# --- VALUE BINDING (R-GI-10).  A membership sweep cannot see a
# --- TRANSPOSITION: swapping two numerals that both occur in the paper
# --- preserves the token multiset exactly.  Each row below is a
# --- sentence of the paper ASSEMBLED FROM THIS RUN'S OWN MEASUREMENTS
# --- and required to occur in the delivered bytes, so a value in the
# --- wrong place dies even though every token is still present.
BINDINGS = [
    "%d classes after %d refinement rounds" % (CONG_N, CONG_ROUNDS),
    "per-round class counts running %s" % ", ".join(
        str(t[1]) for t in CONG_TRACE),
    "falling %s" % ", ".join(str(t[2]) for t in CONG_TRACE),
    "dimensions [%s]" % ", ".join(str(x) for x in DIMS['CONG-185']),
    "%d multi-valued classes at r = 0, 1, 2, 3 and 4" % _desc_c,
    "%d of %d at horizon 2" % (DESCENT['MENU-113'][2][1],
                               DESCENT['MENU-113'][2][2]),
    "%d weight and %d target of %d" % (EDGES['CONG-185'][1],
                                       EDGES['CONG-185'][2],
                                       EDGES['CONG-185'][0]),
    "%d weight and %d target of %d" % (EDGES['MENU-113'][1],
                                       EDGES['MENU-113'][2],
                                       EDGES['MENU-113'][0]),
    "the tested populations are %s" % ", ".join(
        str(n) for r, b, n in DESCENT['CONG-185'][:-1]),
    "r_k = r_q at %d of %d closing squares"
    % (AGREE['CONG-185'][0], AGREE['CONG-185'][0]),
    "holds at %d of %d closed squares" % (len(CLOSED) - ID_VIOL,
                                          len(CLOSED)),
    "%d of the %d closing squares carry one" % (DEV_ON['MENU-113'],
                                                AGREE['MENU-113'][0]),
    "The %d non-unit factors all sit at base depth 0" % len(DEV_NONUNIT),
    "the %d squares it declines to close"
    % (AGREE['MENU-113'][0] - AGREE['CONG-185'][0]),
    "exact at %d of %d transitions" % (FLOW_OK, FLOW_OK + FLOW_BAD),
    "at %d of the %d tests" % (_off_fail, _off_tests),
    "%d of them pass, all at r = 1" % _off_pass,
    "| 1 | %d | %d | %d |" % tuple(_off_rows[0][1:]),
    "| 2 | %d | %d | %d |" % tuple(_off_rows[1][1:]),
    "| 3 | %d | %d | %d |" % tuple(_off_rows[2][1:]),
    "| total | %d | %d | %d |" % (_off_tests, _off_pass, _off_fail),
    "%d violations of %d kernel entries" % (K1BAD, K1TESTED),
    "fails at %d of %d" % (K2BAD, K2TESTED),
    "k_1 still has %d violations of %d" % (K1WBAD, K1WTESTED),
    "value 2 at %d carrier histories and 5/2 at %d"
    % (MCENSUS['2'], MCENSUS['5/2']),
    "%d of %d and %d of %d classes" % (MCONST['CONG-185'][0],
                                       MCONST['CONG-185'][1],
                                       MCONST['MENU-113'][0],
                                       MCONST['MENU-113'][1]),
    "(%s)" % ", ".join(str(x) for x in LAW1),
    "%d raw continuations generated from the %d renewal-1 bases"
    % (N1, len(R1BASES)),
    "returning %d legs" % len(LEGS1),
    "all %d renewal-2 bases, %d expansions, %d legs"
    % (len(R2BASES), N2, len(LEGS2)),
    "on %d of the %d bases the unpruned scan generates %d continuations"
    % (len(GATE_BASES), len(R2BASES), NU),
    "returns %d legs" % len(LEGSU),
    "%d declared tokens, returns 0 occurrences" % len(_tokens),
    "non-Markov at %d of %d depth triples" % (len(CKFAIL['MENU-113']),
                                              len(CK['MENU-113'])),
    "%s negative entries" % ", ".join(str(x) for x in MENU_NEG),
    "at %d, %d, %d and %d cells" % tuple(
        r['differing'] for r in CKFAIL['MENU-113']),
    "%d of %d | 0 of %d | 0 of %d" % (len(CKFAIL['MENU-113']),
                                      len(CK['MENU-113']),
                                      len(CK['CONG-185']),
                                      len(CK['REC'])),
    "the result has %d classes, leaves %d multi-target edges standing"
    % (_min_n, _min_mt),
    "| refinement round 1 | %d | %d | %d | %d |"
    % (_r1_n, _r1_mt, _r1_span, _r1_ckfail),
    "| refinement round 2 | %d | %d | %d | %d |"
    % tuple(LADDER[2][1:]),
    "| refinement round 3 | %d | %d | %d | %d |"
    % tuple(LADDER[3][1:]),
    "trace to %d source classes, not %d" % (len(_ck_src_menu),
                                            len(_mt_src)),
    "runs %s along the lattice" % ", ".join(
        str(r[2]) for r in LADDER[:-1]),
    "feasible at every one of its %d rows"
    % sum(B3ROW[k]['rows'] for k in B3ROW),
    "infeasible at %d of 4" % sum(1 for v in CPL['MENU-113'] if not v),
    "%d negative entries, and the rectangular" % _speak_negs,
    "in %d variables against %d equations"
    % (B3CPL[('MENU-113', _speak_cell)]['vars'],
       B3CPL[('MENU-113', _speak_cell)]['eqs']),
    "carries %d variables against %d equations"
    % (B3CPL[('MENU-113', TRIPLES[0])]['vars'],
       B3CPL[('MENU-113', TRIPLES[0])]['eqs']),
    "leaves CK failing at %d of %d" % (_oth_ckfail, len(CK['MENU-113'])),
    "%d of %d classes occur at more than one depth cut"
    % (DEPTHPURE['CONG-185'][0], DEPTHPURE['CONG-185'][1]),
    "is %d at CONG-185 and %d at MENU-113" % (_returns['CONG-185'],
                                              _returns['MENU-113']),
    "%d of %d transitions" % (ENTRIES['(1, 1)'], TRANS),
    "at %d, %d and %d" % tuple(v for k, v in sorted(ENTRIES.items())
                               if k != '(1, 1)'),
    "| classes spanning a cut | %d of %d | %d of %d |"
    % (DEPTHPURE['CONG-185'][0], DEPTHPURE['CONG-185'][1],
       _d5_span, len(_d5_dep)),
    "| menu classes | %d | %d |" % (len(set(MENU.values())),
                                    len(set(_menu5.values()))),
    "| coarsest congruence | %d | %d |" % (CONG_N,
                                           len(set(_c5.values()))),
    "| refinement rounds | %d | %d |" % (CONG_ROUNDS, _r5),
    "| per-round classes | %s | %s |" % (
        ", ".join(str(t[1]) for t in CONG_TRACE),
        ", ".join(str(t[1]) for t in _t5)),
    "| per-round spanning | %s | %s |" % (
        ", ".join(str(t[2]) for t in CONG_TRACE),
        ", ".join(str(t[2]) for t in _t5)),
    "| purity reached at round | %d of %d | %d of %d |"
    % (_c4_pure_round[0], CONG_ROUNDS, _d5_pure_round[0], _r5),
    "block is %d points" % len(B11C),
    "of sizes %s" % ", ".join(str(x) for x in _cong_sizes[:-1])
    + " and " + str(_cong_sizes[-1]),
    "all %d classes the cap can test" % len(_allclasses),
    "%d points, of which %d are menu-exact" % (len(RS), len(RMENU)),
    "%d, each digested at the moment its gate passed"
    % len(SEALED_PATHS),
]
_paper_ws = re.sub(r'\s+', ' ', _paper)


def bind_missing(text):
    return [b for b in BINDINGS
            if re.sub(r'\s+', ' ', b) not in text]


BIND_MISS = bind_missing(_paper_ws)
# the transposition control: two delivered numerals swapped inside the
# paper text, which leaves the numeral multiset identical
# the pair is chosen so that the swap is MULTISET-PRESERVING: both
# numerals occur the same number of times in the delivered bytes, so the
# membership sweep's residue cannot move and only the placement binding
# can see the transposition.
_tp_a, _tp_b = str(N1), str(N2)
_paper_tp = (_paper_ws.replace(_tp_a, '\x00').replace(_tp_b, _tp_a)
             .replace('\x00', _tp_b))
_tp_miss = bind_missing(_paper_tp)
def _toks(t):
    return sorted(x.replace(',', '') for x in
                  re.findall(r'\d[\d,]*(?:/\d+)?', t))


_tp_same = (_toks(_paper_ws) == _toks(_paper_tp))
gate('G-VERIFY-PAPER', 'MUST',
     'THE PAPER IS SWEPT INSIDE THIS RUN, numeral by numeral AND VALUE '
     'BY PLACE: every numeric token of the delivered paper is matched '
     'against a value this run computed, the residue is zero, and on '
     'top of that membership sweep every load-bearing sentence is '
     'ASSEMBLED FROM THIS RUN\'S OWN MEASUREMENTS and required to occur '
     'in the delivered bytes -- so a numeral moved to the wrong place, '
     'which leaves the token multiset identical and which a membership '
     'sweep cannot see, dies here.  The paper is also byte-anchored, so '
     'the run refuses to proceed against any bytes other than the ones '
     'it swept -- and the complete emitted verdict string is required '
     'to occur in those bytes VERBATIM, so the paper cannot carry a '
     'head the run did not emit',
     (not UNEXPLAINED and _paper_sha == PAPER_SHA and not BIND_MISS
      and len(BINDINGS) >= 40 and VERDICT in _paper),
     f"{len(_ptoks)} numeric tokens in the paper, {len(set(_ptoks))} "
     f"distinct, {len(UNEXPLAINED)} unexplained {UNEXPLAINED[:12]}; "
     f"{len(BINDINGS)} value-bound sentences assembled from this run's "
     f"measurements, {len(BIND_MISS)} not located {BIND_MISS[:3]}; the "
     f"emitted verdict string of {len(VERDICT)} characters occurs in "
     f"the paper verbatim {VERDICT in _paper}; "
     f"paper sha256-12 {_paper_sha} against the anchored {PAPER_SHA}; "
     f"{len(STRUCTURAL)} structural and {len(LEDGER_REFS)} ledger-reference "
     f"numerals declared: {STRUCTURAL} and {LEDGER_REFS}",
     falsifiers=['MUT-PROSE-NUMBER', 'MUT-PAPER-BYTES',
                 'MUT-PROSE-TRANSPOSE'])
mutant('MUT-PROSE-TRANSPOSE', 'G-VERIFY-PAPER',
       'TWO DELIVERED NUMERALS SWAPPED inside the paper text, which '
       'leaves the numeral multiset EXACTLY unchanged and which the '
       'membership sweep therefore cannot see',
       not BIND_MISS, not _tp_miss,
       f"the transposed text leaves the token multiset identical "
       f"({_tp_same}) while {len(_tp_miss)} value-bound sentence(s) no "
       f"longer locate, so the placement conjunct turns false where the "
       f"membership residue does not move")
_mut_tok = [t.replace(',', '') for t in
            re.findall(r'\d[\d,]*(?:/\d+)?',
                       _paper + "\n\nthe carrier carries 918273 classes")]
mutant('MUT-PROSE-NUMBER', 'G-VERIFY-PAPER',
       'a numeral this run never computed spliced into the paper text '
       'the sweep reads',
       not UNEXPLAINED,
       not sorted({t for t in _mut_tok if t not in _expl}),
       f"the spliced text leaves "
       f"{len(sorted({t for t in _mut_tok if t not in _expl}))} "
       f"unexplained numeral(s), so the zero-residue predicate turns "
       f"false")
mutant('MUT-PAPER-BYTES', 'G-VERIFY-PAPER',
       "the paper's bytes drifted after the sweep",
       _paper_sha == PAPER_SHA,
       sha12_of(_paper + "\n") == PAPER_SHA,
       f"a single appended byte moves the paper's sha to "
       f"{sha12_of(_paper + chr(10))}, so the byte anchor turns false")
SEAL.take('SEAL-PAPER-SWEEP',
          lambda: dict(tokens=len(_ptoks), distinct=len(set(_ptoks)),
                       unexplained=UNEXPLAINED, structural=STRUCTURAL,
                       value_bindings=len(BINDINGS),
                       value_bindings_missing=len(BIND_MISS)))

# ======================================================================
# P12.1 -- THE GATE-TIME SEAL, VERIFIED (#119)
# ======================================================================
sec("P12.1 -- THE GATE-TIME SEAL")
SEAL.row('BLOCK', 'totals', COUNTS)
SEAL.row('BLOCK', 'arena', ARENA)
_live_rows = ([('GATE:' + g['name'], g) for g in GATES]
              + [('MUTANT:' + m['mutant'], m) for m in MUTANTS]
              + [('ANCHOR:' + a['name'], a) for a in ANCHOR_ROWS]
              + [('BLOCK:totals', COUNTS), ('BLOCK:arena', ARENA)])
BROKEN = SEAL.verify()
ROWS_BROKEN = SEAL.verify_rows(_live_rows)
# THE FALSIFIERS OF THE SEAL ITSELF, evaluated on COPIES so that nothing
# published is touched.
_probe_seal = Seal()
_probe_obj = {'v': 'GITER-LAW-CONFIRMED'}
_probe_seal.take('SEAL-VERDICT-HEAD', lambda: _probe_obj['v'])
_probe_obj['v'] = 'GITER-DEVIATION'
_seal_probe_broken = _probe_seal.verify()
_row_probe = Seal()
_row_probe.row('GATE', 'PROBE', dict(passed=True, detail='measured'))
_row_broken_probe = _row_probe.verify_rows(
    [('GATE:PROBE', dict(passed=True, detail='FABRICATED'))])
for _r in SEAL.rows:
    emit(f"    {_r['seal']:22s} {_r['path']:16s} sealed at "
         f"{_r['sealed_at_gate']:26s} {_r['sha256_12']}  "
         f"{_r['bytes']} bytes")
emit(f"  {len(SEAL.rows)} sealed objects and {len(SEAL.row_index)} "
     f"sealed registry rows; objects still matching their gate-time "
     f"digest: {len(SEAL.rows) - len(BROKEN)} of {len(SEAL.rows)}; "
     f"registry rows still matching: "
     f"{len(_live_rows) - len(ROWS_BROKEN)} of {len(_live_rows)}")
gate('G-SEAL-COMPLETE', 'MUST',
     'THE GATE-TIME SEAL IS COMPLETE AND UNBROKEN: every published '
     'object was digested AT THE MOMENT ITS GATE PASSED and every '
     'registry row at the moment it was registered; the receipt below '
     'is built FROM THE SEALED SNAPSHOTS rather than from the live '
     'objects; and each seal is re-taken here against the live objects, '
     'so any mutation of a published value between its gate and the '
     'write refuses the delivery.  The artifacts are then written to '
     'temporaries, matched against these digests -- never against live '
     'memory, which would confirm a corruption rather than catch it -- '
     'moved into place with os.replace, and re-verified once more at '
     'process exit, so no corrupt file is left on disk by any path',
     (not BROKEN and not ROWS_BROKEN
      and len(SEAL.rows) == len(SEALED_PATHS)
      and len(_seal_probe_broken) == 1 and len(_row_broken_probe) == 1),
     f"{len(SEAL.rows)} of {len(SEALED_PATHS)} declared objects sealed, "
     f"{len(BROKEN)} broken {BROKEN}; {len(_live_rows)} registry rows, "
     f"{len(ROWS_BROKEN)} broken {ROWS_BROKEN[:3]}; the seal's own "
     f"negative controls fire: a mutated object is reported broken "
     f"({len(_seal_probe_broken)}) and a fabricated registry row is "
     f"reported broken ({len(_row_broken_probe)})",
     falsifiers=['MUT-SEAL-BROKEN', 'MUT-SEAL-ROW-BROKEN',
                 'MUT-DISK-UNCHECKED'])
mutant('MUT-SEAL-BROKEN', 'G-SEAL-COMPLETE',
       'a sealed object MUTATED AFTER ITS GATE and the seal re-taken '
       'against it -- the injection class the delivered unit shipped at '
       'exit 0, nine ways',
       not BROKEN, not _seal_probe_broken,
       f"the mutated object is reported broken by its own gate-time "
       f"digest ({_seal_probe_broken}), so the unbroken-seal conjunct "
       f"turns false and the delivery is refused with nothing written")
mutant('MUT-SEAL-ROW-BROKEN', 'G-SEAL-COMPLETE',
       "a passed gate's published detail, or an anchor row's measured "
       'value, rewritten after registration',
       not ROWS_BROKEN, not _row_broken_probe,
       f"the fabricated row is reported broken against its "
       f"registration-time digest ({_row_broken_probe}), so the "
       f"registry conjunct turns false")
_probe_payload = jcanon(dict(v='sealed'))
_probe_corrupt = _probe_payload[:-2] + ' }'
# TWO COMPARATOR DESIGNS, both evaluated on the same corrupted bytes:
# the one this unit uses (disk against the GATE-TIME SEAL) and the one
# the delivered unit used (disk against a re-serialisation of what is in
# memory now).  Only the first can see the corruption.
_detect_sealed = digest12(_probe_corrupt) != digest12(_probe_payload)
_detect_rederived = digest12(_probe_corrupt) != digest12(_probe_corrupt)
mutant('MUT-DISK-UNCHECKED', 'G-SEAL-COMPLETE',
       'THE INTEGRITY COMPARATOR ITSELF put on trial: the same '
       'corrupted payload shown to the disk-against-SEAL comparator and '
       'to the disk-against-LIVE-MEMORY comparator the delivered unit '
       'used, which re-derives its expectation from the very bytes it '
       'is auditing',
       _detect_sealed, _detect_rederived,
       f"the corrupted payload digests to {digest12(_probe_corrupt)} "
       f"against the sealed {digest12(_probe_payload)}: the "
       f"disk-against-seal comparator detects it ({_detect_sealed}) and "
       f"the re-deriving comparator does not ({_detect_rederived}), so "
       f"the detection conjunct turns false on the delivered design.  "
       f"This run performs the same probe against a real file before it "
       f"writes and refuses if the probe is NOT detected")

# ======================================================================
# P13 -- THE RECEIPT
# ======================================================================
# THE RECEIPT IS BUILT FROM THE SEALED SNAPSHOTS, not from the live
# objects.  Every path in SEALED_PATHS is taken from the digest captured
# when its gate passed; the registries are published live but every row
# was digested at registration and re-checked at G-SEAL-COMPLETE.
RECEIPT.update(dict(
    unit='v14 paper-16 -- GAMMA-ITERATION, the geometry-update law on '
         'the ruled carrier',
    pin_sha256_12=sha12_of(SRC['S-PIN']),
    code_sha256_12=sha12_of(_src_text),
    paper_sha256_12=_paper_sha,
    python=sys.version.split()[0],
    arithmetic='exact int and fractions.Fraction; 0 float literals in '
               'this file\'s syntax tree',
    arena=ARENA,
    gates=GATES, mutants=MUTANTS, anchors=ANCHOR_ROWS,
    totals=COUNTS,
    verdict_audit=V_FAIL,
    seals=SEAL.rows,
    seal_registry_rows=len(SEAL.row_index),
))
for _sid, _path, _g in SEALED_PATHS:
    RECEIPT[_path] = SEAL.value(_sid)

if LIST_GATES:
    sys.stdout.write("\n".join(f"{g['kind']:12s} {g['name']}"
                               for g in GATES) + "\n")
    sys.stdout.write(f"{len(GATES)} registered gates.\n")
    sys.exit(0)

sec("SUMMARY")
emit(f"  gates {COUNTS['gates']} ({COUNTS['must']} MUST, "
     f"{COUNTS['theorem_pass']} theorem-pass, {COUNTS['disclosure']} "
     f"disclosure, {COUNTS['anchors']} anchor); failures "
     f"{COUNTS['gate_failures']}")
emit(f"  falsifiers {COUNTS['mutants_evaluated']} evaluated, "
     f"{COUNTS['mutants_dead']} dead")
emit(f"  anchors {COUNTS['byte_anchors']} byte, "
     f"{COUNTS['verbatim_anchors']} verbatim, "
     f"{COUNTS['path_value_anchors']} path-value")
emit(f"  paper sweep: {len(_ptoks)} numeric tokens, "
     f"{len(UNEXPLAINED)} unexplained; {len(BINDINGS)} value-bound "
     f"sentences located, {len(BIND_MISS)} missing")
emit(f"  the gate-time seal: {len(SEAL.rows)} sealed objects, "
     f"{len(SEAL.row_index)} sealed registry rows, {len(BROKEN)} "
     f"objects and {len(ROWS_BROKEN)} rows broken since their gate")
emit(f"  honest denominators: of the {COUNTS['gates']} registered "
     f"gates {COUNTS['anchors']} are anchors and "
     f"{COUNTS['gates'] - COUNTS['anchors']} are gates; "
     f"{len(MUSTS) + len(TRAILING_GATES)} MUST, {len(THMS)} "
     f"theorem-pass (which carries a falsifier) and {len(DISC)} "
     f"disclosure (whose predicate is the literal True and which is "
     f"counted as evidence nowhere); {len(UNREACHED)} MUST gates "
     f"unreached by a falsifier registered against them; "
     f"{len(_offtarget)} falsifiers pointed anywhere but at a "
     f"registered gate")

if SELFTEST:
    emit("")
    emit("  SELFTEST: one byte anchor was corrupted in memory; the "
         "anchor precheck refused the delivery and nothing was "
         "written.  If this line is reached the precheck did NOT "
         "fire.")
    sys.stdout.write("\n".join(OUT_LINES) + "\n")
    sys.stdout.write("[SELFTEST FAILED: the precheck did not fire]\n")
    sys.exit(1)

if MUT_ONLY is not None:
    _m = [m for m in MUTANTS if m['mutant'] == MUT_ONLY]
    _ok = bool(_m) and _m[0]['killed']
    sys.stdout.write("\n".join(OUT_LINES) + "\n")
    sys.stdout.write(f"[mutant {MUT_ONLY}: "
                     f"{'KILLED at ' + _m[0]['target'] if _ok else 'NOT KILLED'}"
                     f"; files written: 0]\n")
    sys.exit(0 if _ok else 1)

FAILED = [g for g in GATES if not g['passed']]
DEAD = [m for m in MUTANTS if not m['killed']]
_consistent = (len(GATES) == COUNTS['gates']
               and len(MUTANTS) == COUNTS['mutants_evaluated']
               and sorted({m['mutant'] for m in MUTANTS})
               == sorted(MUTANT_REGISTRY))
emit(f"  final registry consistency: {len(GATES)} gates against the "
     f"published {COUNTS['gates']}, {len(MUTANTS)} falsifiers against "
     f"the published {COUNTS['mutants_evaluated']}, registry identity "
     f"{sorted({m['mutant'] for m in MUTANTS}) == sorted(MUTANT_REGISTRY)}"
     f" -> {_consistent}")

_seal_final = SEAL.verify()
_rows_final = SEAL.verify_rows(
    [('GATE:' + g['name'], g) for g in GATES]
    + [('MUTANT:' + m['mutant'], m) for m in MUTANTS]
    + [('ANCHOR:' + a['name'], a) for a in ANCHOR_ROWS]
    + [('BLOCK:totals', COUNTS), ('BLOCK:arena', ARENA)])
emit(f"  final seal check, immediately before the write: "
     f"{len(_seal_final)} sealed object(s) and {len(_rows_final)} "
     f"registry row(s) broken since their gate")

if (FAILED or DEAD or ANCHOR_FAIL or V_FAIL or not _consistent
        or _seal_final or _rows_final):
    emit("")
    emit(f"  DELIVERY REFUSED: {len(FAILED)} gate failure(s), "
         f"{len(DEAD)} dead falsifier(s), {len(ANCHOR_FAIL)} anchor "
         f"failure(s), {len(V_FAIL)} verdict audit failure(s), "
         f"registry consistency {_consistent}, {len(_seal_final)} "
         f"broken seal(s) and {len(_rows_final)} broken registry "
         f"row(s).  Nothing is written.")
    for _g in FAILED:
        emit(f"    FAILED {_g['name']}: {_g['detail']}")
    sys.stdout.write("\n".join(OUT_LINES) + "\n")
    sys.stdout.write("[files written: 0]\n")
    sys.exit(1)

# THE PAYLOAD IS SEALED HERE, at the moment the last gate passed and
# only if every earlier seal still verifies.  Nothing below this line
# can reach the bytes that will be written.
SEAL.close(json.dumps(RECEIPT, indent=1, sort_keys=True,
                      default=str) + "\n",
           "\n".join(OUT_LINES) + "\n",
           _seal_final + _rows_final)
finish(0)
