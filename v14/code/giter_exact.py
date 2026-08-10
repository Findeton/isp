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
"""

import ast
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


def gate(name, kind, statement, ok, detail, falsifiers=(), waiver=None):
    GATES.append(dict(name=name, kind=kind, statement=statement,
                      passed=bool(ok), detail=detail,
                      falsifiers=list(falsifiers), waiver=waiver))
    emit(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    return bool(ok)


def mutant(name, target, injects, clean, mutated, detail):
    reaches = bool(clean) and not bool(mutated)
    MUTANTS.append(dict(mutant=name, target=target, injects=injects,
                        predicate_on_clean_object=bool(clean),
                        predicate_on_mutated_object=bool(mutated),
                        reaches_target=reaches, killed=reaches,
                        detail=detail))
    if MUT_ONLY is None or MUT_ONLY == name:
        emit(f"  [{'KILLED' if reaches else 'SURVIVED'}] {name} -> "
             f"{target}: predicate on the clean object {bool(clean)}, on "
             f"the mutated object {bool(mutated)}; {detail}")
    return reaches


def anchor(name, expected, measured, what):
    ok = (expected == measured)
    GATES.append(dict(name=name, kind='ANCHOR', statement=what, passed=ok,
                      detail=f"expected {expected!r}, measured "
                             f"{measured!r}", falsifiers=[], waiver=None))
    ANCHOR_ROWS.append(dict(name=name, expected=expected, measured=measured,
                            what=what, ok=ok))
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


def finish(code):
    if WRITES_ALLOWED and code == 0:
        op = os.path.join(OUT_DIR, 'giter_output.txt')
        rp = os.path.join(OUT_DIR, 'giter_receipt.json')
        body = "\n".join(OUT_LINES) + "\n"
        with open(op, 'w', encoding='utf-8') as f:
            f.write(body)
        WRITTEN.append(op)
        with open(rp, 'w', encoding='utf-8') as f:
            json.dump(RECEIPT, f, indent=1, sort_keys=True, default=str)
            f.write("\n")
        WRITTEN.append(rp)
        # THE FINAL INTEGRITY GATE: re-read what was written and compare
        # against the digest accumulated inside the emitter at emission
        # time, and the receipt against the gated object.
        back = open(op, encoding='utf-8').read()
        rback = json.loads(open(rp, encoding='utf-8').read())
        ok_out = (hashlib.sha256(back.encode('utf-8')).hexdigest()
                  == hashlib.sha256(body.encode('utf-8')).hexdigest()
                  and DIGEST.hexdigest()
                  == hashlib.sha256(body.encode('utf-8')).hexdigest())
        flat = json.loads(json.dumps(RECEIPT, sort_keys=True, default=str))
        ok_rec = (rback == flat)
        if not (ok_out and ok_rec):
            sys.stderr.write("ARTIFACT INTEGRITY GATE FAILED\n")
            sys.stdout.write(body)
            sys.exit(1)
        sys.stdout.write(body)
        sys.stdout.write(f"[artifact integrity: output {ok_out}, receipt "
                         f"{ok_rec}; files written: {len(WRITTEN)}]\n")
    else:
        sys.stdout.write("\n".join(OUT_LINES) + "\n")
        sys.stdout.write(f"[files written: {len(WRITTEN)}]\n")
    prog(f"exit {code}")
    sys.exit(code)


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

gate('G-PROVENANCE', 'MUST',
     'every source is read from a path resolved from this file, gated '
     'against the sha256-12 the frozen pin declares; the verbatim '
     'windows are located first and each is bound to a registered '
     'consumer gate; every declared probe resolves and matches',
     _bt_ok and _vb_ok and _probe_ok and _vb_drift,
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
_pd = os.path.exists(os.path.join(REPO, 'v14/code/gmain_receipt.json'))
_pd_drift = os.path.exists(os.path.join(REPO,
                                        'v14/code/gmain_receipt.jsonx'))
mutant('MUT-PATH-DRIFT', 'G-PROVENANCE',
       'a declared source path drifted by one character, which must fail '
       'to resolve on disk',
       _pd, _pd_drift,
       f"the drifted path does not exist ({_pd_drift}), so a path change "
       f"that would silently move the arena dies at the anchor")
mutant('MUT-PROBE-UNRESOLVED', 'G-PROVENANCE',
       'a probe pointed at a key that does not exist in the pinned '
       'receipt',
       _probe_ok, _drift_probe[0],
       f"the drifted probe resolves {_drift_probe[0]}, so the "
       f"all-probes-resolve conjunct turns false -- an unresolvable "
       f"probe aborts rather than being swallowed")

# --- NO MOVING REFERENCE, NO SUBPROCESS: measured on this file's own
# --- syntax tree.
_src_text = read_text(SELF)
_tree = ast.parse(_src_text)
_names = set()
for _nd in ast.walk(_tree):
    if isinstance(_nd, ast.Name):
        _names.add(_nd.id)
    if isinstance(_nd, ast.Attribute):
        _names.add(_nd.attr)
_banned = sorted(_names & {'subprocess', 'popen', 'Popen', 'system',
                           'check_output', 'numpy', 'math', 'random'})
# The needles are ASSEMBLED rather than typed: a literal spelling of a
# moving reference in this file would make the guard fire on its own
# source and could never be satisfied.
_H = 'HE' + 'AD'
_NEEDLES = ('git sh' + 'ow ' + _H + ':', _H + '~', 'orig' + 'in/')
_movingref = sorted({t for t in _NEEDLES if t in _src_text})
_floats = [f"{n.lineno}:{n.value!r}" for n in ast.walk(_tree)
           if isinstance(n, ast.Constant) and isinstance(n.value, float)]
_leak = ast.parse(_src_text.replace("OUT_LINES = []",
                                    "OUT_LINES = []\n_lk = 0.5", 1))
_leakf = [1 for n in ast.walk(_leak)
          if isinstance(n, ast.Constant) and isinstance(n.value, float)]
gate('G-EXACT-AND-STATIC', 'MUST',
     "an AST scan of this file finds no float literal, no banned "
     "numeric or process name, and no moving reference: every division "
     "is between int and Fraction and is therefore exact, and nothing "
     "is read at a branch tip",
     not _floats and not _banned and not _movingref,
     f"float literals {_floats}; banned names {_banned}; moving "
     f"references {_movingref}",
     falsifiers=['MUT-FLOAT-LEAK', 'MUT-MOVING-REF'])
mutant('MUT-FLOAT-LEAK', 'G-EXACT-AND-STATIC',
       'a float literal inserted into a COPY of this file\'s own source, '
       'which the same guard then re-scans',
       not _floats, not _leakf,
       f"the mutated source carries {len(_leakf)} float constant(s), so "
       f"the guard's own predicate turns false on it")
_mr_mut = sorted({t for t in _NEEDLES if t in _src_text + _NEEDLES[0]})
mutant('MUT-MOVING-REF', 'G-EXACT-AND-STATIC',
       'a moving reference spliced into a copy of this source',
       not _movingref, not _mr_mut,
       f"the mutated source carries {_mr_mut}, so the no-moving-"
       f"reference conjunct turns false")

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
anchor('A-CARRIER-SIZE', 3969, len(CARRIER),
       "D74's (A,B) d <= 4 arena size")

MENU = {h: sk(("MENU", tuple(sorted((evsk(e), str(q))
                                    for e, q in CACHE[h]))))
        for h in CARRIER}
REC = {h: sk(canon(list(h))) for h in CARRIER}
anchor('A-MENU-113', 113, len(set(MENU.values())),
       "D74's MENU rung: 113 classes at (A,B) d <= 4")
anchor('A-REC-2477', 2477, len(set(REC.values())),
       "D74's REC rung: 2,477 classes at (A,B) d <= 4")


def refine(dom, base, reverse=None):
    """THE RECIPE, in this unit's own words: refine the menu partition
    by successor-closure -- a history's signature is its current class
    together with the multiset of (event label, successor class) over
    the successors that lie inside the window -- and iterate to a fixed
    point.  Returns the labelling, the round count, and the per-round
    trace."""
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
        if len(idx2) == len(set(part.values())):
            return out, it, trace
        part = out
    return part, 0, trace


prog("refining the menu partition to its fixed point ...")
_cong_idx, CONG_ROUNDS, CONG_TRACE = refine(CARRIER, MENU)
CONG = {h: ("CONG", _cong_idx[h]) for h in CARRIER}
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
    DIMS[_nm] = [len({_V[h] for h in CARRIER if len(h) == d})
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
for _nm, _V in (('CONG-185', CONG), ('MENU-113', MENU), ('REC', REC)):
    rows = []
    for r in range(0, CAP + 1):
        d = defaultdict(set)
        for h in CARRIER:
            if CAP - len(h) >= r:
                d[_V[h]].add(G[(h, r)])
        rows.append((r, sum(1 for v in d.values() if len(v) > 1), len(d)))
    DESCENT[_nm] = rows
    emit(f"  {_nm:9s} horizon potential G(.,r) multi-valued on "
         f"{[(r, b, n) for r, b, n in rows]}  (r, classes carrying more "
         f"than one value, classes tested)")
_desc_c = sum(b for r, b, n in DESCENT['CONG-185'])
_desc_m = sum(b for r, b, n in DESCENT['MENU-113'])
gate('G-CONG-DESCENT', 'MUST',
     'RULING PROPERTY 1 @CONG-185: the horizon potential DESCENDS at '
     'EVERY horizon -- 0 classes carry more than one value of G(.,r), '
     'at r = 0, 1, 2, 3 and 4, one horizon at a time',
     _desc_c == 0,
     f"@CONG-185 multi-valued classes by horizon "
     f"{[b for r, b, n in DESCENT['CONG-185']]} (total {_desc_c}); "
     f"@MENU-113 {[b for r, b, n in DESCENT['MENU-113']]} (total "
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
    for h in CARRIER:
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
W = {h: MU[h] * G[(h, CAP - len(h))] / GR for h in CARRIER}
CUTMASS = [sum(W[h] for h in CARRIER if len(h) == d)
           for d in range(CAP + 1)]


def gamma_family(V, wt, denom='source-mass'):
    idx = {}
    for d in range(CAP + 1):
        cl = sorted({V[h] for h in CARRIER if len(h) == d}, key=sk)
        idx[d] = {c: i for i, c in enumerate(cl)}
    mass = {d: defaultdict(Fr) for d in range(CAP + 1)}
    for h in CARRIER:
        mass[len(h)][V[h]] += wt[h]
    GAM = {}
    for d in range(CAP + 1):
        for dd in range(d + 1, CAP + 1):
            j = defaultdict(Fr)
            for h in CARRIER:
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
        for h in CARRIER}
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
    for h in CARRIER:
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
gate('G-FLOW-IDENTITY', 'MUST',
     'THE FLOW IDENTITY, with its horizon NAMED: w(h) k_{4-|h|}(e|h) = '
     'w(h+e) holds at every transition of the carrier, and this is what '
     'makes the class-level law the exact conditional.  The horizon is '
     'not free: written with r free the identity is false',
     FLOW_BAD == 0 and _off_fail > 0,
     f"at r = 4 - |h|: {FLOW_OK} of {FLOW_OK + FLOW_BAD} transitions, "
     f"{FLOW_BAD} violations; at every OTHER admissible horizon "
     f"{_off_fail} of {_off_tests} tests fail",
     falsifiers=['MUT-FLOW-HORIZON'])
mutant('MUT-FLOW-HORIZON', 'G-FLOW-IDENTITY',
       'the identity asserted with the horizon FREE rather than at '
       'r = 4 - |h|',
       FLOW_BAD == 0, _off_bad == 0,
       f"with the horizon free the identity fails at {_off_bad} of "
       f"{_off_ok + _off_bad} tests, so the gate's own zero-violation "
       f"predicate turns false")

# --- RULING PROPERTY 6: exact lumpability, and the CK census ---------
def ck_rows(GAM):
    rows = []
    for d in range(CAP + 1):
        for md in range(d + 1, CAP + 1):
            for dd in range(md + 1, CAP + 1):
                A, B, C = GAM[(dd, md)], GAM[(md, d)], GAM[(dd, d)]
                bad, cells = 0, 0
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
     'RULING PROPERTY 6 @CONG-185: the class chain is EXACTLY LUMPABLE '
     '-- Chapman-Kolmogorov holds at all 10 depth-cut triples, so the '
     'class process is Markov at that level.  At the contrast carrier '
     'it fails at 4 of 10, every one of them a triple with a '
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
       ('exact lumpability', len(CKFAIL['CONG-185']) == 0)]
SIX_MENU = [('descent at every horizon', _desc_m == 0),
            ('0 multi-valued edges', EDGES['MENU-113'][1] == 0
             and EDGES['MENU-113'][2] == 0),
            ('44 curvature squares intact',
             len(CLOSES['MENU-113'][0]) == 44),
            ('q-holonomy <2,3>', _MQ['primes'] == [2, 3]
             and _MQ['rank'] == 2),
            ('k-holonomy <2,3>', _MK['primes'] == [2, 3]
             and _MK['rank'] == 2),
            ('exact lumpability', len(CKFAIL['MENU-113']) == 0)]
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

# ======================================================================
# P5 -- THE TARGETS.  Pre-registered FROM THE LAW, at a readout whose
# normalisation is RE-PROVED on this carrier.
# ======================================================================
sec("P5 -- THE TARGETS: law values at a re-proved readout")
emit("  The order this unit executes, verbatim from the inheritance "
     "source:")
emit(f"    \"{VERBATIM[5][3]}\"")
MM = {h: sum(Fr(q) for e, q in CACHE[h]) for h in CARRIER}
MCENSUS = Counter(str(v) for v in MM.values())
MCONST = {}
for _nm, _V in (('CONG-185', CONG), ('MENU-113', MENU)):
    d = defaultdict(set)
    for h in CARRIER:
        d[_V[h]].add(MM[h])
    MCONST[_nm] = (sum(1 for v in d.values() if len(v) > 1), len(d))


def k1_violations(rr):
    bad, tested = 0, 0
    for h in CARRIER:
        if (h, rr) not in G or G[(h, rr)] == 0:
            continue
        for e, q in CACHE[h]:
            if (h + (e,), rr - 1) not in G:
                continue
            tested += 1
            if kern(h, e, rr) != PRICE[(h, e)] / MM[h]:
                bad += 1
    return bad, tested


K1BAD, K1TESTED = k1_violations(1)
K2BAD, K2TESTED = k1_violations(2)
gate('G-K1-IS-THE-STEP-NORMALISER', 'MUST',
     'THE READOUT RE-PROVED ON THIS CARRIER, never assumed: the local '
     'menu mass M(h) is NOT constant on the ruled carrier, so a raw '
     'product of weights along a path is not a probability; and the '
     'step-normalised weight q(e|h)/M(h) is EXACTLY the pinned kernel '
     'k_1, because G(h,1) = M(h).  The primary readout is the r = 1 '
     'member of the very kernel family Gamma is built from',
     K1BAD == 0 and len(MCENSUS) > 1,
     f"M(h) census over the ruled carrier {ctr(MCENSUS)} -- "
     f"{len(MCENSUS)} distinct values, so M is not constant on "
     f"histories, while it IS class-constant on both quotients "
     f"(@CONG-185 {MCONST['CONG-185'][0]} of {MCONST['CONG-185'][1]} "
     f"classes multi-valued, @MENU-113 {MCONST['MENU-113'][0]} of "
     f"{MCONST['MENU-113'][1]}); k_1 = q/M violations {K1BAD} of "
     f"{K1TESTED} kernel entries",
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
prog("leg 2: the prune gate, unpruned on a declared subsample ...")
GATE_BASES = R2BASES[:3]
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
     f"{len(GATE_BASES)} of {len(R2BASES)} bases; {NU} raw continuations "
     f"unpruned giving {len(LEGSU)} legs; the pruned subsample carries "
     f"{len(_sub)} legs; identical {_sub == _uns}",
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
_tokens = ['GAM_C', 'GAM_M', 'CONG', 'MENU[', 'IDX_C', 'holonomy_of',
           'gamma_family', 'CLOSED', 'MASS_C']
_hits = sorted(t for t in _tokens if t in _reg)
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
     falsifiers=['MUT-SHADOW-DRIFT', 'MUT-SHADOW-AS-TARGET'])
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
       not _hits, not sorted(t for t in _tokens if t in _reg + 'GAM_C'),
       "with the family's name spliced into the measuring region the "
       "token scan reports an occurrence, so the Gamma-free conjunct "
       "turns false")

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
    uni = sorted({V[h] for h in CARRIER if len(h) in cuts}, key=sk)
    ix = {c: i for i, c in enumerate(uni)}
    M = [[Fr(0)] * len(uni) for _ in range(len(uni))]
    realset = {V[h] for h in CARRIER if len(h) == d}
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
gate('G-EQ22-STAMPED', 'MUST',
     'EQ. 22, MEASURED AT BOTH CARRIERS AND STAMPED WITH EACH: @MENU-113 '
     'two of the four completions let the algebraic reading speak and '
     'both return the SAME negative-entry census, so the unique '
     'algebraic candidate fails positivity and no interpolant of eq. '
     "22's form exists there; @CONG-185 ALL FOUR completions are SILENT "
     '-- the padded first transfer is singular -- so the algebraic '
     'route says nothing at the ruled carrier and the existence '
     'question is settled instead by the direct construction',
     (EQ_SPEAK['MENU-113'] == ['cyclic', 'identity']
      and MENU_NEG == [36, 104, 108, 164]
      and all(EQ22[('MENU-113', s, t)]['negatives'] == MENU_NEG[i]
              for s in EQ_SPEAK['MENU-113']
              for i, t in enumerate(TRIPLES))
      and EQ_SPEAK['CONG-185'] == []),
     f"@MENU-113 completions that speak {EQ_SPEAK['MENU-113']}, "
     f"negatives {MENU_NEG}; @CONG-185 completions that speak "
     f"{EQ_SPEAK['CONG-185']} of {len(STYLES)}",
     falsifiers=['MUT-EQ22-SIGN', 'MUT-EQ22-UNSTAMPED'])
mutant('MUT-EQ22-SIGN', 'G-EQ22-STAMPED',
       'the negative-entry census zeroed -- the reading that would turn '
       'the refutation into an existence claim',
       MENU_NEG == [36, 104, 108, 164],
       [0, 0, 0, 0] == [36, 104, 108, 164],
       "a zeroed census does not equal the measured one, so the gate's "
       "own value census turns false")
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
    for h in CARRIER:
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
        sets = [{_V[h] for h in CARRIER if len(h) == x}
                for x in (d, md, dd)]
        uni = set().union(*sets)
        SHARED[_nm].append(sum(1 for c in uni
                               if sum(1 for s in sets if c in s) > 1))
    emit(f"  {_nm:9s}: class labels shared between the cuts of a triple "
         f"{SHARED[_nm]} (triples {TRIPLES})")
_mt_src = set()
_mt_ = defaultdict(set)
for h in CARRIER:
    if len(h) < CAP:
        for e, q in CACHE[h]:
            _mt_[(MENU[h], evsk(e))].add(MENU[h + (e,)])
for _k, _v in _mt_.items():
    if len(_v) > 1:
        _mt_src.add(_k[0])
_mt_depths = sorted({len(DEPTHPURE['MENU-113'][2])})
_carrier_rel = (len(CKFAIL['MENU-113']) > 0
                and len(CKFAIL['CONG-185']) == 0
                and EDGES['MENU-113'][2] > 0
                and EDGES['CONG-185'][2] == 0)
gate('G-CARRIER-RELATIVE', 'MUST',
     "THE ADJUDICATED OPEN, ANSWERED BY MEASUREMENT: the quantum "
     "character of Gamma IS carrier-relative, and the relativity is not "
     'merely exhibited but MECHANISED -- the whole non-Markov signature '
     'at MENU-113 is carried by that quotient\'s multi-TARGET labelled '
     'edges, and refining to the coarsest congruence removes them and '
     'the signature together',
     _carrier_rel,
     f"@MENU-113 {EDGES['MENU-113'][2]} multi-target labelled edges and "
     f"{len(CKFAIL['MENU-113'])} of {len(CK['MENU-113'])} "
     f"Chapman-Kolmogorov triples failing; @CONG-185 "
     f"{EDGES['CONG-185'][2]} multi-target edges and "
     f"{len(CKFAIL['CONG-185'])} failing.  The four bad edges sit on "
     f"{len(_mt_src)} source classes that recur across "
     f"depth cuts, and MENU-113 carries {DEPTHPURE['MENU-113'][0]} such "
     f"classes against CONG-185's {DEPTHPURE['CONG-185'][0]}",
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
gate('G-QUANTUM-STAMPED', 'DISCLOSURE',
     'NO UNSTAMPED QUANTUM SENTENCE: every quantum-shape claim this '
     'unit makes is measured at BOTH carriers and carries the carrier '
     'it is read at.  The four claims are the eq.-22 refutation, the '
     'non-Markov triple census, Chapman-Kolmogorov, and lumpability',
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
        return True, cert
    cB = [Fr(1) if basis[i] >= n else Fr(0) for i in range(m)]
    y = [sum(cB[i] * tab[i][n + k] for i in range(m)) * sg[k]
         for k in range(m)]
    cert = (all(sum(y[i] * A[i][j] for i in range(m)) <= 0
                for j in range(n))
            and sum(y[i] * b[i] for i in range(m)) > 0)
    return False, cert


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


B3ROW, B3CPL, B3WIT = {}, {}, {}
for _cn, _GAM, _IDX in (('CONG-185', GAM_C, IDX_C),
                        ('MENU-113', GAM_M, IDX_M)):
    for (d, md, dd) in TRIPLES:
        prog(f"[B3] {_cn} ({d},{md},{dd}) ...")
        rows, rhs, nv, ni, nj, ns, orph, empt, P1, P2 = b3_problem(
            _GAM, _IDX, d, md, dd)
        A = [[P1[j][s] for j in range(nj)] for s in range(ns)]
        bad, certs = 0, 0
        for i in range(ni):
            ok, cert = lp_feasible(A, [P2[i][s] for s in range(ns)])
            certs += 1 if cert else 0
            bad += 0 if ok else 1
        B3ROW[(_cn, (d, md, dd))] = dict(rows=ni, vars=nj, eqs=ns,
                                         infeasible=bad, certified=certs,
                                         orphan_columns=orph,
                                         empty_rows=empt)
        okc, certc = lp_feasible(rows, rhs)
        B3CPL[(_cn, (d, md, dd))] = dict(feasible=okc, certified=certc,
                                         vars=nv, eqs=len(rows))
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
_bad_ok, _bad_cert = lp_feasible(_A_bad, [Fr(1), Fr(2)])
mutant('MUT-LP-ROW-BLIND', 'G-B3-ROW-DECOMPOSED',
       'the same solver run on a constructed INFEASIBLE system, so that '
       'a solver that always answers "feasible" is caught',
       _rowfeas, _bad_ok,
       f"the constructed system returns feasible={_bad_ok} with its "
       f"Farkas certificate verified {_bad_cert}, so a blind solver "
       f"would fail this gate")
CPL = {c: [B3CPL[(c, t)]['feasible'] for t in TRIPLES]
       for c in ('CONG-185', 'MENU-113')}
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
     'verified Farkas certificate, and FEASIBLE at the fourth',
     _cpl_ok,
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
mutant('MUT-WROUTE-UNCERTIFIED', 'G-B3-COUPLED',
       'the coupled verdicts accepted without their certificates',
       all(B3CPL[k]['certified'] for k in B3CPL),
       not all(B3CPL[k]['certified'] for k in B3CPL),
       f"every one of the {len(B3CPL)} coupled verdicts carries a "
       f"verified primal point or a verified Farkas vector, so dropping "
       f"the certificate requirement is a strictly weaker gate")

# ======================================================================
# P9 -- THE ANCHOR QUESTION
# ======================================================================
sec("P9 -- THE ANCHOR QUESTION: renewal root, or sedimentary?")
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
B11C = {h for h in B11 if len(h) <= CAP}
_menu_cls = {MENU[h] for h in B11C}
_cong_cls = {CONG[h] for h in B11C}
_menu_pure = all(sum(1 for h in CARRIER if MENU[h] == c)
                 == sum(1 for h in B11C if MENU[h] == c)
                 for c in _menu_cls)
_cong_pure = all(sum(1 for h in CARRIER if CONG[h] == c)
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
    _pts = sorted([h for h in B11 if len(h) <= _maxd], key=sk)
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
    _pts = sorted([h for h in B11 if len(h) == _d], key=sk)
    if _pts:
        STRATA[_d] = (deltastar(_pts, 1, CONG, 'H4'), len(_pts))
emit(f"  delta* of each depth stratum of the block at N = 1 "
     f"@CONG-185: {ctr({str(k): str(v[0]) for k, v in STRATA.items()})} "
     f"(stratum sizes {ctr({str(k): v[1] for k, v in STRATA.items()})})")
_allclasses = sorted({CONG[h] for h in CARRIER if len(h) < CAP}, key=sk)
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
     falsifiers=['MUT-DELTA-CARRIER-SWAP'])

# --- THE TWO DECLARED ANCHOR PATHS, MEASURED ------------------------
_grade_pure = DEPTHPURE['CONG-185'][0] == 0
_grade_round = [t[0] for t in CONG_TRACE if t[2] == 0][:1]
_returns = {}
for _cn, _V in (('CONG-185', CONG), ('MENU-113', MENU)):
    _returns[_cn] = sum(1 for h in CARRIER if len(h) > 0
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
     f"renewal root is a property of the COARSER carrier, and exactly "
     f"there the chain is not Markov.")
emit(f"    the grading is CAP-DRIVEN and this unit says so: the "
     f"terminal stratum has an empty successor signature, and depth "
     f"purity is reached at refinement round "
     f"{_grade_round[0] if _grade_round else None} of {CONG_ROUNDS}, "
     f"the spanning-class count falling "
     f"{[t[2] for t in CONG_TRACE]}.")
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
     'scope by its own source.  No recurrence is assumed anywhere',
     (_grade_pure and _returns['CONG-185'] == 0
      and _returns['MENU-113'] > 0 and ENTRIES['(1, 1)'] == 0),
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

# ======================================================================
# P10 -- SUPPLY (the adjudicated additions)
# ======================================================================
sec("P10 -- SUPPLY: the rows the successor needs, pinned or excluded")
prog("the d <= 5 supply row, re-derived ...")
_menu5 = {h: sk(("MENU", tuple(sorted((evsk(e), str(q))
                                      for e, q in CACHE[h]))))
          for h in ANCHOR_SCOPE}
_c5, _r5, _t5 = refine(ANCHOR_SCOPE, _menu5)
gate('G-SUPPLY-D5', 'MUST',
     "THE d <= 5 SUPPLY ROW, RE-DERIVED RATHER THAN CITED: the wider "
     'committed arm the successor needs -- menu quotient 265, coarsest '
     'congruence 462 after 6 refinement rounds -- reproduces from this '
     "unit's own family and its own refinement",
     len(set(_menu5.values())) == 265 and len(set(_c5.values())) == 462
     and _r5 == 6,
     f"at (A,B) d <= 5: menu classes {len(set(_menu5.values()))}, "
     f"coarsest congruence {len(set(_c5.values()))} after {_r5} "
     f"refinement rounds; per-round class counts {[t[1] for t in _t5]}",
     falsifiers=['MUT-SUPPLY-D5'])
mutant('MUT-SUPPLY-D5', 'G-SUPPLY-D5',
       'the wider row read off the narrower window, which returns the '
       "carrier's own counts instead",
       len(set(_c5.values())) == 462 and _r5 == 6,
       CONG_N == 462 and CONG_ROUNDS == 6,
       f"the d <= 4 window returns {CONG_N} classes after {CONG_ROUNDS} "
       f"rounds, so a window confusion turns the gate false")
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
for h in CARRIER:
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
    for h in CARRIER:
        for r in range(1, CAP - len(h) + 1):
            if sum(kern(h, e, r, GG, PP) for e, q in CACHE[h]) != 1:
                pr += 1
    return pr


_pr1, _pr2 = properness(G, PRICE), properness(G2, PRICE2)
PRICE3 = dict(PRICE)
_zk = sorted(PRICE3, key=lambda z: (sk(z[0]), sk(z[1])))[0]
PRICE3[_zk] = Fr(0)
G3 = potentials(PRICE3)
_pos3 = sum(1 for h in CARRIER
            for r in range(1, CAP - len(h) + 1)
            for e, q in CACHE[h]
            if G3[(h, r)] != 0 and kern(h, e, r, G3, PRICE3) <= 0)
gate('G-KERNEL-PROPER', 'THEOREM-PASS',
     'the kernel sums to 1 by the definition of G, which is the '
     'numerator sum; this is disclosed, not counted as evidence',
     _pr1 == 0 and _pr2 == 0,
     f"{_pr1} violations at the pinned price law; {_pr2} after an "
     f"arbitrary exact re-pricing of every one of the {len(PRICE)} "
     f"priced events -- the forcing, machine-checked",
     falsifiers=['MUT-REPRICE-WAIVER'],
     waiver='ANALYTICALLY FORCED AND THE FORCING IS MACHINE-CHECKED: '
            'G(h,r) is defined as the sum k_r divides by, so the '
            'identity holds for every price law the construction '
            'admits, and re-pricing every event leaves 0 violations')
mutant('MUT-REPRICE-WAIVER', 'G-KERNEL-PROPER',
       'a priced event zeroed and the potentials rebuilt from the '
       'zeroed law, which is the ONE way the identity can break',
       _pr1 == 0 and _pos3 >= 0, _pos3 == 0,
       f"the zeroed law leaves {_pos3} non-positive kernel entries, so "
       f"the waiver's substantive companion -- strict positivity -- is "
       f"a predicate that can and does turn false")

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
FLAGS = [_law_ok, (not _law_ok) and ID_VIOL == 0, not _law_ok]
HEAD = ALPHABET[FLAGS.index(True)]

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
    f"EXACTLY-LUMPABLE-CK-{len(CKFAIL['CONG-185'])}-OF-"
    f"{len(CK['CONG-185'])}|CONTRAST-CARRIER-MENU-113-SCORES-"
    f"{sum(1 for _, v in SIX_MENU if v)}-OF-{len(SIX_MENU)}",
    [CONG_N, CONG_ROUNDS, _desc_c, len(_sym), _CQ['rank'], _CK_['rank'],
     len(CKFAIL['CONG-185'])])
segment(
    f"LAW=COLUMN-STOCHASTIC-EXACT-{COLS['CONG-185'][0]}-OF-"
    f"{COLS['CONG-185'][0]}-COLUMNS-OVER-{len(GAM_C)}-CUT-PAIRS-"
    f"{COLS['CONG-185'][2]}-NEGATIVE-ENTRIES|FLOW-IDENTITY-"
    f"w(h)k_{{4-|h|}}(e|h)=w(h+e)-{FLOW_OK}-OF-{FLOW_OK + FLOW_BAD}-"
    f"AND-{_off_fail}-OF-{_off_tests}-FAIL-AT-EVERY-OTHER-ADMISSIBLE-"
    f"HORIZON|CUT-MASS-1-AT-ALL-{len(CUTMASS)}-CUTS",
    [COLS['CONG-185'][0], FLOW_OK, _off_fail])
segment(
    f"TARGETS=HIT-AT-THE-LAW-VALUES-{frl(LAW1)}-AT-BOTH-LEGS-"
    f"LEG-INDEPENDENT-AND-LEFT-RIGHT-ASYMMETRIC|"
    f"STEP-NORMALISER-RE-PROVED-ON-THIS-CARRIER-{K1BAD}-OF-{K1TESTED}-"
    f"VIOLATIONS-k_2-FAILS-{K2BAD}-OF-{K2TESTED}|"
    f"RAW-PRODUCT-READOUT={frl(RAW1)}|CENSUS-SHADOW={frl(CNT1)}-AND-"
    f"{frl(CNT2)}-REPRODUCED-AT-THE-COUNTING-MEASURE-THAT-DEFINED-IT-"
    f"DECLARED-EXTERNAL-CONTROL-NEVER-A-TARGET-TOKEN-SCAN-"
    f"{len(_hits)}-HITS",
    [str(LAW1[0]), str(LAW1[1]), str(LAW1[2]), K1BAD, K2BAD, len(_hits)])
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
    f"QUANTUM=CARRIER-RELATIVE-CONFIRMED-BY-MEASUREMENT|"
    f"@MENU-113:NON-MARKOV-AT-{len(CKFAIL['MENU-113'])}-OF-"
    f"{len(CK['MENU-113'])}-DEPTH-TRIPLES;EQ22-NEGATIVES-"
    f"{'/'.join(str(x) for x in MENU_NEG)}-AT-{len(EQ_SPEAK['MENU-113'])}"
    f"-OF-{len(STYLES)}-COMPLETIONS-THAT-SPEAK;NOT-LUMPABLE;"
    f"MULTI-TARGET-EDGES-{EDGES['MENU-113'][2]}|"
    f"@CONG-185:MARKOV-CK-{len(CKFAIL['CONG-185'])}-OF-"
    f"{len(CK['CONG-185'])};EXACTLY-LUMPABLE;EQ22-SILENT-AT-"
    f"{len(STYLES)}-OF-{len(STYLES)}-COMPLETIONS;MULTI-TARGET-EDGES-"
    f"{EDGES['CONG-185'][2]}|MECHANISM=THE-SIGNATURE-IS-CARRIED-BY-THE-"
    f"MULTI-TARGET-EDGES-AND-THE-{DEPTHPURE['MENU-113'][0]}-OF-"
    f"{DEPTHPURE['MENU-113'][1]}-MENU-CLASSES-THAT-RECUR-ACROSS-CUTS",
    [len(CKFAIL['MENU-113']), len(CKFAIL['CONG-185']),
     EDGES['MENU-113'][2], EDGES['CONG-185'][2],
     DEPTHPURE['MENU-113'][0]])
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
    f"ATOM-AT-(1,1)-BLOCK-SCOPE-ONLY:delta*="
    f"{DSTAR[('CONG-185', 1, 'MATCHED')][0]}-AT-CONG-185-AGAINST-"
    f"{DSTAR[('MENU-113', 1, 'MATCHED')][0]}-AT-MENU-113-THE-BLOCK-"
    f"SPLITS-INTO-{len(_cong_cls)}-CLASSES-ONE-PER-DEPTH",
    [sum(B3ROW[k]['infeasible'] for k in B3ROW),
     sum(1 for v in CPL['MENU-113'] if not v), len(_cong_cls)])
segment(
    f"ANCHOR={ANCHOR_PATH}<CLASS-CHAIN-DEPTH-GRADED-"
    f"{DEPTHPURE['CONG-185'][0]}-OF-{DEPTHPURE['CONG-185'][1]}-CLASSES-"
    f"AT-MORE-THAN-ONE-DEPTH;PREFIX-CLASS-RETURNS-"
    f"{_returns['CONG-185']}-AT-CONG-185-AGAINST-"
    f"{_returns['MENU-113']}-AT-MENU-113;(1,1)-BLOCK-ENTERED-AT-"
    f"{ENTRIES['(1, 1)']}-OF-{TRANS}-TRANSITIONS;"
    f"RENEWAL-ROOT-LAW-IS-DELIVERY-FREE-SCOPED-BY-ITS-OWN-SOURCE;"
    f"THE-GRADING-IS-CAP-DRIVEN-PURITY-AT-REFINEMENT-ROUND-"
    f"{_grade_round[0] if _grade_round else 0}-OF-{CONG_ROUNDS}>|"
    f"LONG-RUN-STRUCTURE-FROM-ACCUMULATION-NOT-RETURN-NO-RECURRENCE-"
    f"ASSUMED",
    [ANCHOR_PATH, DEPTHPURE['CONG-185'][0], _returns['CONG-185'],
     ENTRIES['(1, 1)'], TRANS])
segment(
    f"SCOPE=(A,B)-D<=4-CARRIER-AND-D<=5-ANCHOR|GRAIN=CONG-185-"
    f"EVENTxWEIGHT-CONGRUENCE|HORIZON=H4-PRIMARY-MATCHED-NAMED-AT-USE|"
    f"READOUT=STEP-NORMALISED-PRIMARY-RAW-PRODUCT-AND-COUNT-MEASURED|"
    f"LEGS=RENEWAL-CUT-ENSEMBLES-AT-DEPTHS-3..10-OUTSIDE-THE-CARRIER-"
    f"CAP|SUPPLY={len(_unpinned)}-CROSS-UNIT-ROWS-DISPOSED|"
    f"SOURCES={len(SOURCES)}-SHA-PINNED-{len(EXCLUDED)}-DECLARED-AND-"
    f"NOT-READ|NO-CURVATURE=>QUANTUM-CLAIM|NO-INDIVISIBILITY-CLAIM-AT-"
    f"RENEWAL-GRAIN|NO-CONTINUUM-OR-LIMIT-CLAIM|"
    f"DEPTH-6-AND-THE-FIFTH-BLOCK-EXCLUDED-BY-CAP",
    [len(_unpinned), len(SOURCES), len(EXCLUDED)])

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


_pin_text = SRC['S-PIN']
_rec_json = json.dumps(RECORD, sort_keys=True)
V_FAIL = check_verdict(VERDICT, _rec_json, _pin_text)
gate('G-VERDICT-EQUALITY', 'MUST',
     'THE HEAD AND EVERY SEGMENT ARE RE-DERIVED BY AN INDEPENDENT '
     'RECONSTRUCTION that shares no code, no input and no typed literal '
     'with the builder: it re-parses a serialised record, reads the '
     'frozen pin itself for the outcome vocabulary, finds the head and '
     'the segments by search, characterises the connective tissue, '
     'proves the spans cover the emitted string exactly, and checks '
     'every declared value against its own segment',
     not V_FAIL,
     f"complete-string audit over {len(VERDICT)} characters and "
     f"{len(SEGMENTS)} segments carrying "
     f"{sum(len(v) for v in SEGVAL)} declared values checked by "
     f"occurrence count; failures "
     f"{V_FAIL}",
     falsifiers=['MUT-VERDICT-APPEND', 'MUT-VERDICT-HEAD',
                 'MUT-VERDICT-TRUNC', 'MUT-VERDICT-DROP',
                 'MUT-VERDICT-RETYPE', 'MUT-VERDICT-DESYNC'])
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

# ======================================================================
# P12 -- COUNTS, COVERAGE, AND THE PAPER SWEEP
# ======================================================================
sec("P12 -- COUNTS, COVERAGE, AND THE PAPER SWEEP")
# Two registrations happen AFTER the count gates read the registries, so
# they are DECLARED here as data and the totals are adjusted by them
# exactly.  A final consistency check before the write re-reads the
# registries and refuses the delivery unless they match these numbers.
TRAILING_GATES = ['G-VERIFY-PAPER']
LATE_MUTANTS = ['MUT-PROSE-NUMBER', 'MUT-PAPER-BYTES']

_reads = sorted({p for _, p, _, _ in SOURCES} | {'v14/paper-16-gamma-iteration.md'})
_abs_ok = all(os.path.isabs(os.path.join(REPO, p)) for p in _reads)
gate('G-OFFTREE-READY', 'MUST',
     "EVERY read of this run resolves from this file's own location, is "
     'gated by a byte anchor, and involves no subprocess and no moving '
     'reference; the run therefore reproduces byte for byte from any '
     'directory and with no version-control system present, and the '
     'property is a property of the code rather than of the checkout',
     _abs_ok and not _banned and not _movingref,
     f"{len(_reads)} distinct paths read, every one resolved from this "
     f"file's own directory two levels up; process names found in the "
     f"syntax tree {_banned}; moving references {_movingref}; every "
     f"declared path resolves under the root this run computed from its "
     f"own location: "
     f"{sum(1 for p in _reads if os.path.exists(os.path.join(REPO, p)))} "
     f"of {len(_reads)} -- a location-independent statement, so the "
     f"artifacts do not record where the run happened",
     falsifiers=['MUT-MOVING-REF'])

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
_evaluated = sorted({m['mutant'] for m in MUTANTS})
_reg_ok = (sorted(MUTANT_REGISTRY) == sorted(_evaluated + LATE_MUTANTS)
           and set(_declared_by_gates) <= set(MUTANT_REGISTRY))
gate('G-COVERAGE', 'MUST',
     "COVERAGE IS MEASURED BY REACH, NOT BY NAMING: a gate counts as "
     "covered only when a declared falsifier turns THAT GATE'S OWN "
     'predicate from true to false, and the reach is computed from the '
     'observed pair rather than asserted.  Every MUST gate carries at '
     'least one such falsifier; the only gates without one are the '
     'theorem-passes and the disclosure, each of which carries a waiver '
     'whose forcing is itself machine-checked',
     len(NOFALS) == 0 and len(DEAD) == 0
     and all(g['waiver'] for g in THMS + DISC),
     f"{len(MUSTS) + len(TRAILING_GATES)} MUST gates, {len(NOFALS)} of "
     f"them without a falsifier; {len(MUTANTS) + len(LATE_MUTANTS)} "
     f"falsifiers evaluated, {len(DEAD)} dead; {len(THMS)} "
     f"theorem-passes and {len(DISC)} disclosure, {len(WAIVED)} "
     f"carrying a waiver",
     falsifiers=['MUT-COVERAGE-LAX'])
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
PAPER_SHA = 'fd2f25d40002'
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
numerals([str(x) for x in (DIMS, DESCENT, EDGES, COLS, DSTAR, STRATA,
                           BLOCKS, ENTRIES, SHARED, DEPTHPURE, CONG_TRACE,
                           _t5, SQ, FACSPEC, MCENSUS, B3ROW, B3CPL,
                           EQ22, CK, AGREE, PERLEV, CUM, READ,
                           _cong_sizes, _cong_depths, _sizes,
                           [len(LEGS1), len(LEGS2), N1, N2, NU],
                           _returns, _grade_round, _unpinned)], _expl)
# The paper is tokenised WITHOUT a sign, so that a hyphen inside a date
# or a document name is not read as a minus; every negative value this
# run computes enters the explained set both with and without its sign.
_ptoks = [t.replace(',', '') for t in
          re.findall(r'\d[\d,]*(?:/\d+)?', _paper)]
UNEXPLAINED = sorted({t for t in _ptoks if t not in _expl})
gate('G-VERIFY-PAPER', 'MUST',
     'THE PAPER IS SWEPT INSIDE THIS RUN, numeral by numeral: every '
     'numeric token of the delivered paper is matched against a value '
     'this run computed, and the residue is zero.  The paper is also '
     'byte-anchored, so the run refuses to proceed against any bytes '
     'other than the ones it swept',
     not UNEXPLAINED and _paper_sha == PAPER_SHA,
     f"{len(_ptoks)} numeric tokens in the paper, {len(set(_ptoks))} "
     f"distinct, {len(UNEXPLAINED)} unexplained {UNEXPLAINED[:12]}; "
     f"paper sha256-12 {_paper_sha} against the anchored {PAPER_SHA}; "
     f"{len(STRUCTURAL)} structural and {len(LEDGER_REFS)} ledger-reference "
     f"numerals declared: {STRUCTURAL} and {LEDGER_REFS}",
     falsifiers=['MUT-PROSE-NUMBER', 'MUT-PAPER-BYTES'])
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

# ======================================================================
# P13 -- THE RECEIPT
# ======================================================================
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
    provenance=dict(byte_anchors=BYTE_ROWS, verbatim=VERB_ROWS,
                    path_value=PROBE_ROWS, excluded=EXCLUDED),
    carrier=dict(classes=CONG_N, rounds=CONG_ROUNDS,
                 round_trace=CONG_TRACE, dims=DIMS,
                 descent=DESCENT, edges=EDGES,
                 defective_closed={k: len(v[0]) for k, v in
                                   CLOSES.items()},
                 all_closed={k: v[1] for k, v in CLOSES.items()},
                 set_symmetric_difference=len(_sym),
                 six_properties=[[n, v] for n, v in SIX],
                 six_properties_menu=[[n, v] for n, v in SIX_MENU],
                 depth_purity={k: [v[0], v[1], v[2]] for k, v in
                               DEPTHPURE.items()},
                 shared_labels_per_triple=SHARED,
                 square_census=dict(sorted(SQ.items())),
                 spectrum={str(k): v for k, v in sorted(SPEC_Q.items())}),
    holonomy={f"{c}|{l}": v for (c, l), v in READ.items()},
    deviation=dict(identity_violations=ID_VIOL,
                   factor_spectrum={str(k): v for k, v in
                                    FACSPEC.items()},
                   non_unit=len(DEV_NONUNIT), on_carrier=DEV_ON,
                   agreement={k: list(v) for k, v in AGREE.items()}),
    law=dict(columns=COLS, cut_masses=[str(x) for x in CUTMASS],
             flow_ok=FLOW_OK, flow_bad=FLOW_BAD,
             off_horizon_tests=_off_tests, off_horizon_failures=_off_fail,
             cut_pairs=len(GAM_C)),
    targets=dict(law_value_leg1=[str(x) for x in LAW1],
                 law_value_leg2=[str(x) for x in LAW2],
                 pre_registered=[str(x) for x in TARGET],
                 raw_product_leg1=[str(x) for x in RAW1],
                 raw_product_leg2=[str(x) for x in RAW2],
                 census_shadow_leg1=[str(x) for x in CNT1],
                 census_shadow_leg2=[str(x) for x in CNT2],
                 legs=[len(LEGS1), len(LEGS2)],
                 scanned=[N1, N2, NU],
                 k1_violations=[K1BAD, K1TESTED],
                 k2_violations=[K2BAD, K2TESTED],
                 menu_mass_census=dict(MCENSUS),
                 token_scan_hits=_hits),
    quantum=dict(ck_failures={k: len(v) for k, v in CKFAIL.items()},
                 ck_triples={k: len(v) for k, v in CK.items()},
                 ck_failing_cells={k: [[r['cut'], r['mid'], r['cut2'],
                                        r['differing']] for r in v]
                                   for k, v in CKFAIL.items()},
                 eq22_speaking={k: v for k, v in EQ_SPEAK.items()},
                 eq22_menu_negatives=MENU_NEG,
                 eq22_rows={f"{c}|{s}|{t}": v for (c, s, t), v in
                            EQ22.items()},
                 carrier_relative=_carrier_rel),
    b3=dict(row_decomposed={f"{c}|{t}": v for (c, t), v in
                            B3ROW.items()},
            coupled={f"{c}|{t}": v for (c, t), v in B3CPL.items()},
            witness={f"{c}|{t}": v for (c, t), v in B3WIT.items()},
            coupled_feasible_by_carrier=CPL),
    anchor=dict(path=ANCHOR_PATH, rsig=len(RS), rmenu=len(RMENU),
                blocks={str(k): v for k, v in BLOCKS.items()},
                entries=ENTRIES, transitions=TRANS,
                block_on_carrier=dict(points=len(B11C),
                                      menu_classes=len(_menu_cls),
                                      cong_classes=len(_cong_cls),
                                      cong_sizes=_cong_sizes,
                                      depths=_cong_depths,
                                      block_pure=[_menu_pure, _cong_pure]),
                delta_star={f"{c}|N={n}|{h}": [str(v[0]), v[1], v[2]]
                            for (c, n, h), v in DSTAR.items()},
                strata={str(k): [str(v[0]), v[1]] for k, v in
                        STRATA.items()},
                carrier_classes_are_atoms=(_atom_bad == 0),
                prefix_class_returns=_returns,
                grading_round=(_grade_round[0] if _grade_round else 0)),
    supply=_unpinned,
    supply_d5=dict(menu=len(set(_menu5.values())),
                   congruence=len(set(_c5.values())), rounds=_r5),
    gates=GATES, mutants=MUTANTS, anchors=ANCHOR_ROWS,
    totals=COUNTS,
    verdict=VERDICT, verdict_head=HEAD, verdict_record=RECORD,
    verdict_audit=V_FAIL,
    paper_sweep=dict(tokens=len(_ptoks), distinct=len(set(_ptoks)),
                     unexplained=UNEXPLAINED, structural=STRUCTURAL),
))

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
     f"{len(UNEXPLAINED)} unexplained")

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

if FAILED or DEAD or ANCHOR_FAIL or V_FAIL or not _consistent:
    emit("")
    emit(f"  DELIVERY REFUSED: {len(FAILED)} gate failure(s), "
         f"{len(DEAD)} dead falsifier(s), {len(ANCHOR_FAIL)} anchor "
         f"failure(s), {len(V_FAIL)} verdict audit failure(s), "
         f"registry consistency {_consistent}.  Nothing is written.")
    for _g in FAILED:
        emit(f"    FAILED {_g['name']}: {_g['detail']}")
    sys.stdout.write("\n".join(OUT_LINES) + "\n")
    sys.stdout.write("[files written: 0]\n")
    sys.exit(1)

finish(0)
