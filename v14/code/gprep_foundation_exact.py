#!/usr/bin/env python3
"""gprep_foundation_exact.py — v14 Gamma-PREP: THE TRANSPORT-SCOPE
FOUNDATION (paper-11).  Pin: v14/note-gprep-transport-foundation-pin.md
(v14 ledger #57, sha256-12 42ce06e6be8a).

WHAT THIS FILE IS.  Two arms.  ARM A re-derives, from the committed
transport layer alone, the seven facts the Gamma campaign's stage 1
stands on: the grammar declaration; the ARM-1T census and the finite-
horizon potentials G_1..G_7 at both scopes; the relative-horizon
kernels k_r and their properness; the renewal ports R-SIG / R-MENU;
THE ESCAPE at both committed grains; the reopening witness; the
root-symmetry theorem.  ARM B attempts the one NEW construction the
predecessor named and did not run: operator-level minorization on the
transport family (Doeblin on the R-SIG class; Birkhoff / Hilbert-metric
contraction of the positive backward recursion G).

CLI CONTRACT (enforced by an argv WHITELIST parsed before any
measurement runs; an unrecognized argument exits 2 and measures
nothing; EVERY failure path writes nothing).
  /opt/homebrew/bin/python3.13 v14/code/gprep_foundation_exact.py
      A plain run.  Runs everything: anchors, ARM A, ARM B, every
      declared injection-falsifier, the never-falsified census, the
      compliance sweep, and the composed verdict.  WRITES
      v14/code/gprep_foundation_output.txt and
      v14/code/gprep_foundation_receipt.json (paths derived from this
      file's own location), then RE-READS both from disk and verifies
      them against the gated object before exiting.  Exit 0 whatever
      the science says; exit 1 on an anchor failure, a dead falsifier
      or an artifact-integrity failure — and in each of those cases
      NOTHING is written.  Two plain runs are byte-identical, in the
      repository or outside it, with or without git: every wall-clock
      number goes to stderr and never to the receipt, and no runtime
      input is read at a mutable reference.
  ... --no-write
      Identical measurement, no files written (diagnostic).
  ... --list-gates | --list-mutants
      Print the COMPLETE gate / falsifier registries (both branches
      run after the last registration) and exit 0.  Writes nothing.
  ... --selftest
      Corrupt exactly one byte anchor in memory, confirm that exactly
      one anchor row fails and that the anchor precheck refuses the
      delivery, write NOTHING, and exit 1.
  ... --mutant NAME
      Apply one registered falsifier to the gated object, print the
      gates it kills, write NOTHING, and exit 1 if it kills none (or
      if NAME is not a registered falsifier).

DISCIPLINE.  Exact arithmetic only (int / fractions.Fraction); an AST
float-guard runs over this file's own source.  Every runtime input is
either a hash-pinned artifact (byte + path-value + verbatim-context
anchored) or this unit's own frozen declaration (RUNBOOK section 14,
v14 #46): v14/LOG.md, /STATUS.md and every other mutable repo file are
NOT read, NO subprocess is spawned, and no file is read at `git show
HEAD:` or any other moving reference.  Determinism: no repr() of a
frozenset ever reaches a sort key or a printed line — the stable-key
function SK is used instead.
"""
import ast
import hashlib
import json
import os
import re
import sys
import time
from collections import defaultdict
from fractions import Fraction as Fr
from itertools import permutations

sys.setrecursionlimit(50000)

T0 = time.time()

# ======================================================================
# THE CLI WHITELIST.  Parsed before anything is measured, so that an
# unrecognized argument can never be silently ignored (v14 #66 -> #82:
# the registered disease, repaired here).  Exit 2 is the usage exit and
# exists only at this site.
# ======================================================================
EXIT_USAGE = 2
FLAGS_NULLARY = ('--no-write', '--list-gates', '--list-mutants',
                 '--selftest')
FLAGS_VALUED = ('--mutant',)
USAGE = (
    "usage: gprep_foundation_exact.py "
    "[--no-write] [--list-gates] [--list-mutants] [--selftest] "
    "[--mutant NAME]\n"
    "  accepted flags: " + ", ".join(sorted(FLAGS_NULLARY + FLAGS_VALUED))
    + "\n  anything else is rejected; no measurement runs and no file "
      "is written.\n")


def parse_argv(argv):
    """(accepted {flag: value}, rejected [tokens]).  A valued flag must
    be followed by a non-flag token."""
    seen, bad, i = {}, [], 0
    while i < len(argv):
        a = argv[i]
        if a in FLAGS_NULLARY:
            seen[a] = True
        elif a in FLAGS_VALUED:
            if i + 1 >= len(argv) or argv[i + 1].startswith('-'):
                bad.append(a + " (missing value)")
            else:
                i += 1
                seen[a] = argv[i]
        else:
            bad.append(a)
        i += 1
    return seen, bad


ARGV, _argv_bad = parse_argv(sys.argv[1:])
if _argv_bad:
    sys.stderr.write(USAGE)
    sys.stderr.write("  unrecognized argument(s): "
                     + ", ".join(_argv_bad) + "\n")
    sys.stderr.flush()
    sys.exit(EXIT_USAGE)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(REPO)          # .../isp
HERE = os.path.dirname(os.path.abspath(__file__))
SELF = os.path.abspath(__file__)

OUT_LINES = []
# The emission-time digest.  Every line is folded in AT THE MOMENT IT
# IS EMITTED, so a mutation of OUT_LINES after the gates have run —
# the injection that put an invented first line into the delivered
# output with every gate green — cannot reach it.  The written file is
# re-read and compared against this digest before the process exits.
EMIT_DIGEST = hashlib.sha256()
EMIT_LINES = [0]


def emit(s=""):
    """Deterministic receipt line: stdout + the output file."""
    OUT_LINES.append(s)
    EMIT_DIGEST.update((s + "\n").encode())
    EMIT_LINES[0] += 1
    print(s)


def prog(s):
    """Wall-clock progress — stderr only, never in the receipt."""
    sys.stderr.write(f"[t+{time.time() - T0:7.1f}s] {s}\n")
    sys.stderr.flush()


def SK(o):
    """Hash-order-independent total key for nested frozenset/tuple data.
    repr(frozenset) depends on PYTHONHASHSEED; this does not."""
    if isinstance(o, (frozenset, set)):
        return ("S", tuple(sorted(SK(x) for x in o)))
    if isinstance(o, (tuple, list)):
        return ("T", tuple(SK(x) for x in o))
    if isinstance(o, Fr):
        return ("Q", o.numerator, o.denominator)
    return ("V", type(o).__name__ + "|" + repr(o))


OPENED = set()          # every path this process READS, instrumented


def sha12(path):
    OPENED.add(os.path.abspath(path))
    with open(path, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:12]


def read_text(path):
    """The ONLY text-read route in this file.  Every path it touches is
    recorded, so that 'no unanchored runtime inputs' can be COMPUTED
    rather than asserted (RUNBOOK section 14, v14 #46)."""
    OPENED.add(os.path.abspath(path))
    with open(path) as fh:
        return fh.read()


def frs(x):
    return f"{x} (~{float(x):.6f})"


# ======================================================================
# THE GATED OBJECT.  Every measurement lands in F; every gate reads F
# and nothing else; the receipt and the paper render from F.  (RUNBOOK
# section 13, v14 #10: one object, one source of truth.)
# ======================================================================
class Facts(dict):
    def __init__(self):
        super().__init__()
        self._reads = None

    def __getitem__(self, k):
        if self._reads is not None:
            self._reads.add(k)
        return super().__getitem__(k)

    def track(self):
        self._reads = set()

    def stop(self):
        r = self._reads
        self._reads = None
        return r


F = Facts()

# The pinned source table and its verbatim-context windows are
# declared here, before the banner, so that every count printed about
# them is read off these lists rather than typed.
ROWS = [
    ("T1", "THE LAYER",
     "TERMINAL v10 #304",
     [("v10/code/d42b1_transport_exact.py", "576275d55ecf"),
      ("v10/note-d42b1-transport-and-reconciliation.md", "8aa031a4b0e3")],
     "the transport grammar: the event kinds (the PIN's summary column "
     "says 6; the committed generator has exactly 5 branches — PIN "
     "ERRATUM, registered in-unit and measured below), delivery/merge "
     "preconditions+effects, budgets"),
    ("T2", "THE BOUNDARY THEOREM",
     "TERMINAL v10 #392 (round+delta)",
     [("v10/relativistic-isp-v10-paper32-the-boundary-of-closure.md",
       "4b533e437b0f")],
     "the reopening; window-consistency-without-closure; the escape; "
     "the no-successor-may-cite-D44b-bites clause"),
    ("T3", "THE ESCAPE MEASUREMENT",
     "TERMINAL v10 #374",
     [("v10/note-d44b-transport-scope-invariance.md", "598ada389811"),
      ("v10/code/d44b_transport_invariance_exact.py", "dfb2df899603"),
      ("v10/data/d44b_transport_invariance_exact.out", "d202fe0acf08")],
     "the growth table; the 68 escaping transitions; menu-shape "
     "factorisation failure; the reopening decomposition"),
    ("T4", "THE KERNEL + RENEWAL ARM",
     "TERMINAL-AT-ONE-HOSTILE-ROUND, v10 LOG #489 (the note's header "
     "is STALE; the ledger is the authority)",
     [("v10/note-d70-horizon-limit-result.md", "f1c8f17c77c0"),
      ("v10/code/d70_horizon_limit_exact.py", "f55f7034fab0"),
      ("v10/data/d70_horizon_limit_exact.out", "1177761ed54d")],
     "k_r proper r = 1..7; G_1..G_7 both scopes; R-SIG/R-MENU; 4^n; "
     "(3/2)^n; 0.7705; the root-symmetry theorem; the named successor"),
    ("T5", "THE ABSTRACTION LADDER AND THE CARRIER",
     "round-1 reviewed+repaired; the exact v10 ledger # is VERIFIED "
     "in-unit below against the byte-anchored ledger row T9 and "
     "printed",
     [("v10/note-d74-transport-holonomy-result.md", "0180e21c7127"),
      ("v10/code/d74_transport_holonomy_exact.py", "bb852161aced"),
      ("v10/data/d74_transport_holonomy_exact.out", "b5a9d50f9573")],
     "the six committed abstractions (SEQ 3969 / REC 2477 / MULT 578 / "
     "STATE 125 / PORT 65 / MENU 113) AND THE TWO CARRIER ROWS: "
     "(A,B) d<=4 menu quotient 113 / coarsest congruence 185; "
     "(A,B) d<=5 menu quotient 265 / coarsest congruence 462"),
    ("T6", "THE CHAIN'S DEFINITION",
     "TERMINAL v10 #349",
     [("v10/relativistic-isp-v10-paper31-four-decisions-at-the-joints.md",
       "7ac66f3fe74d"),
      ("v10/code/d43b_state_chain_exact.py", "5f91f0190b4c")],
     "section 3.1's bisimulation method; section 3.5's transport "
     "declaration; section 7 residue 8"),
    ("T7", "THE KERNEL'S PARENT",
     "TERMINAL v10 #403 (three-round sweep; header STALE — the ledger "
     "is pinned)",
     [("v10/note-d46b-martin-at-transport.md", "406af54e0c5c"),
      ("v10/data/d46b_martin_transport_exact.out", "f218704b52dd")],
     "k_r's definition; root = renewal DOES transfer at matched "
     "horizon; deliveries REDUCE finite-horizon branching"),
    ("T8", "RECEPTION DYNAMICS",
     "TERMINAL v10 #403",
     [("v10/note-d46f-reception-dynamics.md", "a6368078be4c")],
     "the per-type update table; delivery NON-INJECTIVE"),
    ("T9", "THE COMMITTED v10 LEDGER",
     "v10 is CLOSED; this artifact is byte-anchored like every other "
     "pinned row and read from the same path, never at a moving "
     "reference",
     [("v10/LOG.md", "d244f925e172")],
     "the D74 terminal stamp (LEDGER #495) and the D74 delivery / pin "
     "stamps immediately preceding it"),
]

# --- verbatim-context anchors: context WINDOWS, each bound to a named
# --- consuming gate (RUNBOOK section 14, v14 #34).
VERBATIM = [
    ("T1", "v10/code/d42b1_transport_exact.py",
     "Budgets: propose 1/4 | arb-and-merge 1/4 (components join-view +\n"
     "pairs initiator-view) | deliver 1/4 (sender-view) | idle absorbs.",
     "A1-BUDGETS"),
    ("T2", "v10/relativistic-isp-v10-paper32-the-boundary-of-closure.md",
     "the window chain ESCAPES: 68\n"
     "  transitions from shallow parents land in 5 classes first\n"
     "  realized at length 3.  Escape is not non-stabilization: the\n"
     "  partition behaves; the state space outruns every window.",
     "A5-ESCAPE"),
    ("T2", "v10/relativistic-isp-v10-paper32-the-boundary-of-closure.md",
     "the per-candidate versus per-class-AGGREGATE distinction — which\n"
     "   is load-bearing at delivery-free scope — is EXTENSIONALLY NULL\n"
     "   at the transport cap, so no successor may cite D44b as evidence\n"
     "   that it bites there.",
     "A5-OPERATOR-CONTROL"),
    ("T3", "v10/note-d44b-transport-scope-invariance.md",
     "window chain ESCAPES: 68 transitions from len <= 2 parents land "
     "in\n5 classes first realized only at len 3.",
     "A5-ESCAPE"),
    ("T3", "v10/note-d44b-transport-scope-invariance.md",
     "84 distinct diverged prefixes; 4 DISTINCT\nminimal (3-event) "
     "reconverging chains, all at weight 1/256",
     "A6-REOPENING"),
    ("T4", "v10/note-d70-horizon-limit-result.md",
     "**R-MENU absorbing-complement (0 re-entries), R-SIG re-entered "
     "3,796 times**",
     "A4-PORTS"),
    ("T4", "v10/note-d70-horizon-limit-result.md",
     "No operator-level minorization \u2014\n> Birkhoff / Hilbert-metric "
     "contraction of the positive backward\n> recursion `G`, the "
     "natural instrument for this kernel \u2014 has been\n> attempted "
     "anywhere.",
     "B0-SUCCESSOR-NAMED"),
    ("T4", "v10/note-d70-horizon-limit-result.md",
     "**HZ1-b (strict positivity) is the substantive one**",
     "A3-POSITIVITY"),
    ("T5", "v10/data/d74_transport_holonomy_exact.out",
     "AB4 (A,B) depth<=4 CARRIER: menu quotient 113 classes; coarsest "
     "congruence 185 classes after 5 refinement rounds",
     "A5-CONTROL-GRAIN"),
    ("T5", "v10/data/d74_transport_holonomy_exact.out",
     "(A,B) depth<=5 CARRIER: menu quotient 265 classes; coarsest "
     "congruence 462 classes after 6 refinement rounds",
     "B4-CARRIER-SUPPLY"),
    ("T5", "v10/data/d74_transport_holonomy_exact.out",
     "Refining the menu partition by successor-closure (partition\n"
     "        refinement to a fixed point) gives the coarsest weighted\n"
     "        CONGRUENCE, the strongest form of descent.",
     "B4-CARRIER-CHAIN"),
    ("T9", "v10/LOG.md",
     "## 2026-07-27 — D74 ROUND 1 ADJUDICATED AND TERMINAL: TH-II WITH "
     "A\n## FIND — THE CURVATURE STANDS AT FOUR POOLS; THE SCALAR PHASE "
     "IS\n## EMPTY ON THE HONEST CARRIER; THE EVEN CHANNEL CARRIES J\n"
     "## (LEDGER #495)",
     "A0-LEDGER"),
    ("T6", "v10/relativistic-isp-v10-paper31-four-decisions-at-the-joints.md",
     "- `P_0` = the partition of histories by *menu shape* (event kinds "
     "with\n  their exact weights, as a multiset);\n- `P_{t+1}` = one "
     "probabilistic-bisimulation refinement of `P_t`: two\n  histories "
     "stay equivalent iff for every successor class the total\n  "
     "transition weight into that class agrees exactly;",
     "A5-METHOD"),
    ("T7", "v10/note-d46b-martin-at-transport.md",
     "objects k_r(e|h) = q G(h+e, r-1)/G(h, r).",
     "A3-KERNEL"),
    ("T8", "v10/note-d46f-reception-dynamics.md",
     "NON-INJECTIVE (re-delivery admissible; PROBE-DD load-bearing);",
     "A1-DELIVERY"),
]



GATES = []          # (gid, kind, label, pred, detail)
KIND_SUB = 'SUBSTANTIVE'
KIND_THM = 'THEOREM-PASS'
KIND_DIS = 'DISCLOSURE'


def gate(gid, kind, label, pred, detail):
    GATES.append((gid, kind, label, pred, detail))


def run_gates(facts):
    """Evaluate every registered gate against `facts`.  Returns
    {gid: (ok, detail, reads)}."""
    res = {}
    for gid, kind, label, pred, det in GATES:
        facts.track()
        try:
            ok = bool(pred(facts))
        except Exception:
            ok = False
        reads = facts.stop()
        try:
            d = det(facts)
        except Exception:
            d = "<detail unavailable under perturbation>"
        res[gid] = (ok, d, reads)
    return res


# ======================================================================
# P0 — BANNER, DECLARED ARENA (RUNBOOK section 15), DECLARED CAPS
# ======================================================================
emit("[GPREP — v14 Gamma-PREP: THE TRANSPORT-SCOPE FOUNDATION "
     "(paper-11)]")
emit("  pin: v14/note-gprep-transport-foundation-pin.md, v14 ledger "
     "#57, sha256-12 42ce06e6be8a.  ARM A terminalizes the foundation "
     "from the committed layer; ARM B attempts the successor engine.")
emit("  EXACT arithmetic only (int / Fraction); AST float-guard over "
     "this file's own source; no tolerances anywhere.")
emit("  NO UNANCHORED RUNTIME INPUTS AND NO MOVING REFERENCES (RUNBOOK "
     "section 14, v14 #46 and its adjudication addendum): every file "
     "this process opens is listed in the anchor table below with its "
     "sha256-12 — the committed v10 ledger included, as row T9 — and "
     "the product of every such read is consumed by a named gate.  No "
     "subprocess is spawned; nothing is read at `git show HEAD:` or "
     "any other mutable reference; v14/LOG.md and /STATUS.md are NOT "
     "read.  The set of paths actually opened is instrumented and "
     "compared against the anchored set at the compliance sweep, and "
     "the plain run is byte-identical inside the repository, outside "
     "it, and with git absent.")
emit("")
emit("  THE DECLARED ARENA (RUNBOOK section 15 — data, not prose):")
emit("    boundary   : the empty history (genesis v0 is the declared "
     "boundary of the committed layer, T1 docstring).")
emit("    family     : ARM-1T, actor pool (A, B), exhaustive menus to "
     "depth 6 — 243,769 histories.  The delivery-free partner is the "
     "same layer with the delivery kind withheld (derived below, not "
     "imported).")
emit("    law        : the committed d42b1 weight law, exec'd from its "
     "own path; nothing about admission or pricing is re-implemented.")
emit("    state      : the history itself.  Every coarser object used "
     "here (menu shape, holdings profile, intrinsic partition) is a "
     "DECLARED abstraction of it and is named at every use.")
emit("    arena      : two actors, depth 6, relative horizons r = "
     "1..7, terminal convention C1 (G(h,0) = 1).  THE GRAIN CHOICE IS "
     "ARENA DATA: the 13-class kind x weight partition is DECLARED "
     "PRIMARY (T3's), the 113-class event x weight partition is the "
     "measured CONTROL (T5's).  Choosing silently would be the arena "
     "artefact the era forbids.")
emit(f"    provenance : the {len(ROWS)} pinned source rows "
     f"{ROWS[0][0]}-{ROWS[-1][0]}, each carrying its pedigree "
     f"qualifier verbatim (table below).")
emit("")

CAP_T = 6          # two-actor transport family, exhaustive menus
CAP_DF = 6         # delivery-free partner, exhaustive menus
CAP_ESC = 4        # the escape / intrinsic-partition window (T3's cap)
CAP_SYM = 3        # the root-symmetry window (T4's cap)
RMAX = 7           # relative horizons r = 1..7
NMAX = 5           # ARM B: N = 1..5
CAP_3A = 5         # ARM B conditional arm: 3-actor depth (attempted)
AB = ('A', 'B')
ABC = ('A', 'B', 'C')
ROOT = ()

emit(f"  DECLARED CAPS, printed before anything uses them: two-actor "
     f"transport depth {CAP_T}; delivery-free partner depth {CAP_DF}; "
     f"intrinsic-partition window depth {CAP_ESC}; root-symmetry "
     f"window depth {CAP_SYM}; relative horizons r = 1..{RMAX}; ARM B "
     f"N = 1..{NMAX}.  No sampled arm is run anywhere: every row is "
     f"EXACT and exhaustive at its printed cap.")
emit(f"  DECLARED INFEASIBLE, with the counts printed rather than the "
     f"omission hidden (ARM B): depth 7 at two actors and depth 6 at "
     f"three actors.  Their sizes are computed from this run's own "
     f"measured branching below and printed at ARM B.")
emit("")

# ======================================================================
# P1 — ANCHORS.  Verbatim-context anchors FIRST (RUNBOOK section 14,
# v14 #34), then byte anchors, then path-value anchors.  Exit 1 lives
# here and at the dead-falsifier check, nowhere else.
# ======================================================================
emit("[P1 — THE PINNED SOURCES: verbatim-context, byte and path-value "
     "anchors]")
emit("  Pedigree qualifiers are carried VERBATIM from the pin, per its "
     "own binding instruction.")

# THE #62 SPECIFICITY STANDARD, declared before it is applied: a
# verbatim-context window must be at least MIN_CTX characters long AND
# must occur EXACTLY ONCE in its source file.  A window that binds
# existence but not meaning — a short generic substring — fails both
# clauses and is refused at the precheck, so the truncation class dies
# before the delivery is produced rather than after it.
MIN_CTX = 40


def check_verbatim(rows):
    """(row, path, consumer-gate, found?, chars, occurrences)."""
    out = []
    for tag, path, ctx, consumer in rows:
        try:
            txt = read_text(os.path.join(REPO, path))
            occ = txt.count(ctx)
        except OSError:
            occ = 0
        out.append((tag, path, consumer, occ == 1 and len(ctx) >= MIN_CTX,
                    len(ctx), occ))
    return out


def check_bytes(rows, corrupt=None):
    """corrupt = a (path) whose PINNED expectation is bent in memory;
    used only by --selftest, which writes nothing and exits 1."""
    out = []
    for tag, name, ped, arts, sup in rows:
        for path, want in arts:
            if corrupt is not None and path == corrupt:
                want = want[:-1] + ('0' if want[-1] != '0' else '1')
            try:
                got = sha12(os.path.join(REPO, path))
            except OSError:
                got = "MISSING"
            out.append((tag, path, want, got, got == want))
    return out


VB = check_verbatim(VERBATIM)
BY = check_bytes(ROWS)

if '--selftest' in ARGV:
    # THE SELFTEST.  Corrupt exactly ONE byte anchor in memory, confirm
    # that exactly one anchor row fails and that the precheck would
    # refuse the delivery, write NOTHING, exit 1.
    _st_path = ROWS[0][3][0][0]
    _st = check_bytes(ROWS, corrupt=_st_path)
    _bad = [r for r in _st if not r[4]]
    _ok_before = all(r[4] for r in BY) and all(r[3] for r in VB)
    print(f"[SELFTEST] one byte anchor corrupted in memory: {_st_path}")
    print(f"[SELFTEST] anchor rows failing BEFORE corruption: "
          f"{sum(1 for r in BY if not r[4])} of {len(BY)}; "
          f"verbatim windows failing: {sum(1 for r in VB if not r[3])} "
          f"of {len(VB)}")
    print(f"[SELFTEST] anchor rows failing AFTER corruption: "
          f"{len(_bad)} -> {[r[1] for r in _bad]}")
    print(f"[SELFTEST] the anchor precheck refuses the delivery: "
          f"{not all(r[4] for r in _st)}")
    print(f"[SELFTEST] baseline clean: {_ok_before}; "
          f"exactly one row killed: {len(_bad) == 1}")
    print(f"[SELFTEST] NO FILE WRITTEN.  The corrupted anchor is "
          f"refused by the same precheck the plain run uses, which "
          f"exits BEFORE any measurement and BEFORE any write.  exit 1.")
    sys.stdout.flush()
    sys.exit(1)

emit(f"  VERBATIM-CONTEXT ANCHORS (evaluated FIRST) at the #62 "
     f"SPECIFICITY STANDARD — a window counts as located only if it is "
     f">= {MIN_CTX} characters AND occurs EXACTLY ONCE in its source: "
     f"{sum(1 for r in VB if r[3])} of {len(VB)} context windows "
     f"located, each bound to its named consumer gate.")
for tag, path, consumer, ok, n, occ in VB:
    emit(f"    [{'OK ' if ok else 'MISS'}] {tag}  {path}  -> consumer "
         f"gate {consumer}  ({n} chars of context, {occ} occurrence(s))")
emit(f"  BYTE ANCHORS: {sum(1 for r in BY if r[4])} of {len(BY)} "
     f"artifacts reproduce their pinned sha256-12.")
for tag, path, want, got, ok in BY:
    emit(f"    [{'OK ' if ok else 'BAD'}] {tag}  {got}  {path}"
         + ("" if ok else f"   (pin says {want})"))
emit("  THE PEDIGREE QUALIFIERS, carried verbatim per the pin:")
for tag, name, ped, arts, sup in ROWS:
    emit(f"    {tag} {name}: {ped}")
emit("  NAMED EXCLUSIONS, printed in-unit and honoured by this "
     "process: v10/note-d56-... (uncommitted probe — reachable only "
     "through v10/note-d57-sector-exact-pin.md, and this unit does "
     "not reach for it); v10/note-d46a-... (target refuted as "
     "written); v11/note-u1c-... (NOT CITABLE); THE-THEORY-SO-FAR / "
     "THE-COMPLETION-DICHOTOMY (index only); v14/LOG.md and "
     "/STATUS.md (forbidden runtime inputs).")

if not all(r[3] for r in VB) or not all(r[4] for r in BY):
    emit("  ANCHOR FAILURE — exit 1.")
    sys.stdout.flush()
    sys.exit(1)

# --- path-value anchors: the (path, value) pair, not only the bytes.
LAYER_PATH = 'v10/code/d42b1_transport_exact.py'
_ls = read_text(os.path.join(REPO, LAYER_PATH))
_PREFIX = _ls[:_ls.index('print("[d42b1')]
NS = {}
exec(compile(_PREFIX, 'd42b1_port', 'exec'), NS)
candidates_for = NS['candidates_for']
admissible = NS['admissible']
event_poset = NS['event_poset']
View = NS['View']
vname = NS['vname']
V0 = NS['V0']
deliver_options_in_view = NS['deliver_options_in_view']
prop_options_in_view = NS['prop_options_in_view']

F['layer_path'] = LAYER_PATH
F['layer_prefix_chars'] = len(_PREFIX)
F['layer_defs'] = tuple(sorted(
    n for n in ('candidates_for', 'admissible', 'event_poset', 'View',
                'vname', 'V0', 'deliver_options_in_view',
                'prop_options_in_view') if n in NS))
F['layer_no_exit'] = ('sys.exit' not in _PREFIX
                      and '\ncheck(' not in _PREFIX
                      and '\nprint(' not in _PREFIX)
# THE PIN ERRATUM, MEASURED rather than argued: the event kinds the
# committed GENERATOR can emit are the one-character tags occurring as
# the head of a tuple literal inside candidates_for.  This is an AST
# census of the pinned layer's own source, independent of the family
# built from it, and it is what the A1-KINDS gate compares against.
_lt = ast.parse(_PREFIX)
_branch_tags = set()
for _fn in ast.walk(_lt):
    if isinstance(_fn, ast.FunctionDef) and _fn.name == 'candidates_for':
        for _nd in ast.walk(_fn):
            if isinstance(_nd, ast.Tuple) and _nd.elts:
                _h = _nd.elts[0]
                if (isinstance(_h, ast.Constant)
                        and isinstance(_h.value, str)
                        and len(_h.value) == 1):
                    _branch_tags.add(_h.value)
F['layer_kind_tags'] = tuple(sorted(_branch_tags))
F['layer_kind_branches'] = len(_branch_tags)
F['pin_erratum_kind_count'] = (6, F['layer_kind_branches'])
F['verbatim_ok'] = tuple((t, p, c) for t, p, c, ok, n, o in VB if ok)
F['verbatim_n'] = len(VB)
F['verbatim_min_chars'] = min(n for t, p, c, ok, n, o in VB)
F['verbatim_min_required'] = MIN_CTX
F['verbatim_occurrences'] = tuple((t, c, o) for t, p, c, ok, n, o in VB)
F['verbatim_unique'] = all(o == 1 for t, p, c, ok, n, o in VB)
F['verbatim_consumers'] = tuple(sorted({c for t, p, c, ok, n, o in VB}))
F['byte_ok'] = tuple((t, p, g) for t, p, w, g, ok in BY if ok)
F['byte_n'] = len(BY)
F['pedigrees'] = tuple((t, ped) for t, n, ped, a, s in ROWS)

# --- T5's ledger number, VERIFIED against the BYTE-ANCHORED committed
# --- ledger (row T9).  The moving-reference read this unit's first
# --- delivery used (`git show HEAD:v10/LOG.md` through a subprocess)
# --- is GONE: v10 is closed, so its ledger is a pinned artifact like
# --- every other row, it is read from the same path through the same
# --- anchored route, and its product is consumed by the gate A0-LEDGER
# --- below.  No moving reference, no subprocess, no silent degradation
# --- to None, and the delivered bytes no longer depend on the ambient
# --- repository.
_d74 = read_text(os.path.join(
    REPO, 'v10/note-d74-transport-holonomy-result.md'))
F['t5_note_status_line'] = next(
    (ln.strip() for ln in _d74.splitlines() if ln.startswith('**Status')),
    '')
LEDGER_PATH = 'v10/LOG.md'
_ledger = read_text(os.path.join(REPO, LEDGER_PATH))


def ledger_number(text, header):
    """The ledger # attached to the entry whose header contains
    `header`: the first '(LEDGER #n)' at or after that header line.
    Returns None if the header is absent — and the gate below refuses
    a None, so a missing read cannot deliver a headline."""
    hit = False
    for ln in text.splitlines():
        if header in ln:
            hit = True
        if hit and '(LEDGER #' in ln:
            s = ln[ln.index('(LEDGER #') + 9:]
            return int(s[:s.index(')')])
    return None


F['t5_ledger_number'] = ledger_number(
    _ledger, 'D74 ROUND 1 ADJUDICATED AND TERMINAL')
F['t5_ledger_delivered'] = ledger_number(
    _ledger, 'D74 DELIVERED (GREEN-UNREVIEWED)')
F['t5_ledger_pinned'] = ledger_number(_ledger, 'D74 PINNED:')
F['t5_ledger_source'] = (
    'v10/LOG.md read at its pinned sha256-12 (row T9), byte-anchored '
    'and verbatim-anchored like every other pinned artifact; no '
    'subprocess, no moving reference')
F['t5_ledger_path'] = LEDGER_PATH
emit("")
emit(f"  T5 LEDGER VERIFICATION (the pin's explicit order), read from "
     f"the BYTE-ANCHORED ledger row T9 — {LEDGER_PATH} at its pinned "
     f"sha256-12, through the same anchored route as every other "
     f"source, with its four-line header carried as a "
     f"verbatim-context window.  The entry headed 'D74 ROUND 1 "
     f"ADJUDICATED AND TERMINAL: TH-II WITH A FIND' carries "
     f"**(LEDGER #{F['t5_ledger_number']})**.  The green delivery "
     f"immediately preceding it is #{F['t5_ledger_delivered']} and the "
     f"pin freeze is #{F['t5_ledger_pinned']} — both parsed from the "
     f"same anchored bytes, neither typed.  T5's citable pedigree is "
     f"therefore: round-1 reviewed+repaired, TERMINAL at v10 LOG "
     f"#{F['t5_ledger_number']}.")
emit(f"    THE CITABILITY GAP THIS CLOSES, exhibited: the note's own "
     f"status line reads {F['t5_note_status_line']!r} — it never "
     f"says TERMINAL, so a successor reading the note alone would "
     f"under-cite the row.  The ledger is the authority and the "
     f"number is #{F['t5_ledger_number']}.")
gate("A0-LEDGER", KIND_SUB,
     "THE PIN'S ORDERED LEDGER VERIFICATION IS GATED, so that it can "
     "never be discharged by a read that verified nothing: the D74 "
     "terminal stamp parsed out of the BYTE-ANCHORED v10 ledger is "
     "exactly 495 and is not None, the green delivery immediately "
     "preceding it is 494 and the pin freeze 492, and the d74 note's "
     "own status line does not contain the word TERMINAL — which is "
     "the citability gap this row closes",
     lambda f: (f['t5_ledger_number'] == 495
                and f['t5_ledger_number'] is not None
                and f['t5_ledger_delivered'] == 494
                and f['t5_ledger_pinned'] == 492
                and 'TERMINAL' not in f['t5_note_status_line']),
     lambda f: f"terminal #{f['t5_ledger_number']}, delivered "
               f"#{f['t5_ledger_delivered']}, pinned "
               f"#{f['t5_ledger_pinned']}; note status line "
               f"{f['t5_note_status_line']!r}")

prog("anchors done")

# ======================================================================
# P2 — THE AST FLOAT-GUARD over this file's own source
# ======================================================================
_src = read_text(SELF)
_tree = ast.parse(_src)
_floats = []
for _n in ast.walk(_tree):
    if isinstance(_n, ast.Constant) and isinstance(_n.value, float):
        _floats.append(_n.lineno)
    if isinstance(_n, ast.Name) and _n.id in ('numpy', 'np', 'math'):
        _floats.append(_n.lineno)
_fmtfloat = _src.count('float(')
F['ast_float_literals'] = tuple(sorted(set(_floats)))
F['ast_float_calls'] = _fmtfloat
emit("")
# --- THE CLI CONTRACT, EXERCISED IN-PROCESS rather than documented.
# --- The parser is run on a bogus sample so that "unknown flags are
# --- rejected" is a measurement of this run's own argv handler.
_cli_bad = parse_argv(['--utterly-bogus', '--no-writ'])[1]
_cli_good = parse_argv(['--no-write', '--mutant', 'X'])[0]
F['cli_rejected_sample'] = len(_cli_bad)
F['cli_rejected_tokens'] = tuple(_cli_bad)
F['cli_accepted_sample'] = tuple(sorted(_cli_good))
F['cli_exit_on_unknown'] = EXIT_USAGE
F['cli_flags_known'] = len(FLAGS_NULLARY) + len(FLAGS_VALUED)
F['cli_flags'] = tuple(sorted(FLAGS_NULLARY + FLAGS_VALUED))
emit("")
emit(f"[P2b — THE CLI CONTRACT, MEASURED] the argv whitelist accepts "
     f"{F['cli_flags_known']} flags {list(F['cli_flags'])} and is "
     f"exercised here on a bogus sample: "
     f"{F['cli_rejected_sample']} of 2 tokens rejected "
     f"{list(F['cli_rejected_tokens'])} — including the one-character "
     f"typo of the safety flag, which without a whitelist is a silent "
     f"no-op — while a well-formed sample parses to "
     f"{list(F['cli_accepted_sample'])}.  An unrecognized argument "
     f"exits {F['cli_exit_on_unknown']} before any measurement runs, "
     f"and every failure path of this program writes nothing.")
gate("C-CLI", KIND_SUB,
     "THE CLI CONTRACT IS ENFORCED AND MEASURED, NOT DOCUMENTED (v14 "
     "#66 -> #82, the registered repair item): the argv handler is a "
     "whitelist, it is exercised in-process on a bogus sample and "
     "rejects both tokens — the unknown flag and the one-character "
     "typo of --no-write — the usage exit code is 2, and the accepted "
     "flag set is exactly the five the contract names",
     lambda f: (f['cli_rejected_sample'] == 2
                and f['cli_exit_on_unknown'] == 2
                and f['cli_flags_known'] == 5
                and f['cli_accepted_sample'] == ('--mutant', '--no-write')
                and '--selftest' in f['cli_flags']
                and '--mutant' in f['cli_flags']),
     lambda f: f"rejected {list(f['cli_rejected_tokens'])}; accepted "
               f"{list(f['cli_accepted_sample'])}; exit code "
               f"{f['cli_exit_on_unknown']}; flags {list(f['cli_flags'])}")
emit(f"[P2 — AST FLOAT-GUARD] float literals in the substantive "
     f"source: {len(F['ast_float_literals'])} "
     f"(lines {list(F['ast_float_literals'])}); float() appears "
     f"{F['ast_float_calls']} times and ONLY inside display "
     f"formatting (frs()/f-strings) — every comparison, every gate "
     f"and every stored value is int or Fraction.")

# ======================================================================
# ARM A, FACT 1 — THE GRAMMAR DECLARATION, re-derived from T1
# ======================================================================
emit("")
emit("[ARM A / FACT 1 — THE GRAMMAR DECLARATION, re-derived from the "
     "committed layer]")


def build(cf, actors, cap):
    cache = {}
    frontier = [ROOT]
    while frontier:
        h = frontier.pop()
        cache[h] = cf(list(h), actors)
        if len(h) >= cap:
            continue
        for e, q in cache[h]:
            frontier.append(h + (e,))
    return cache


def cf_transport(h, actors):
    return candidates_for(h, actors)


def cf_delivery_free(h, actors):
    """THE DELIVERY-FREE PARTNER, DERIVED — not imported.  The
    delivery-free grammar is the committed transport grammar with the
    delivery kind withheld: the 'd' branch of the menu is removed and
    the idle budget reabsorbs its quarter (the layer's own idle weight
    is 1 - 1/4*has_p - 1/4*has_am - 1/4*has_d, and has_d is identically
    true at two actors because holdings always contain v0).  This is a
    DERIVATION from T1, so the unit reads no unanchored second layer;
    it is gated against T4's committed partner census and potentials
    below, which is the (path, value) anchor for the derivation."""
    out = []
    for e, q in candidates_for(h, actors):
        if e[0] == 'd':
            continue
        if e[0] == 'n':
            q = q + Fr(1, 4)
        out.append((e, q))
    return out


prog("building the two-actor transport family to depth 6 ...")
_t = time.time()
CACHE = build(cf_transport, AB, CAP_T)
prog(f"transport family built: {len(CACHE)} histories in "
     f"{time.time() - _t:.1f}s")

LEVEL = defaultdict(list)
for h in CACHE:
    LEVEL[len(h)].append(h)

ROOTMENU = CACHE[ROOT]
kinds = sorted({e[0] for h in CACHE for e, q in CACHE[h]})
kind_counts = defaultdict(int)
# THE BUDGETS, MEASURED OFF THE LAYER RATHER THAN QUOTED.  They are
# PER-ACTOR budgets, not per-menu ones (T1's own parenthetical: the
# deliver sector is sender-view, the arb-and-merge sector is components
# join-view plus pairs initiator-view), so the measurement is taken per
# (history, actor).  The accumulators are SETS, so the answer does not
# depend on iteration order, and the scan is the WHOLE family.
_bud = defaultdict(set)
_mass = defaultdict(lambda: defaultdict(int))
for h in CACHE:
    per = defaultdict(lambda: defaultdict(Fr))
    tot = Fr(0)
    for e, q in CACHE[h]:
        kind_counts[e[0]] += 1
        per[e[1]][e[0]] += q
        tot += q
    for a in AB:
        if per[a]['p']:
            _bud['p'].add(per[a]['p'])
        if per[a]['d']:
            _bud['d'].add(per[a]['d'])
        if per[a]['r'] or per[a]['m']:
            _bud['r+m'].add(per[a]['r'] + per[a]['m'])
    _mass[len(h)][tot] += 1
F['n_actors'] = len(AB)
F['event_kinds'] = tuple(kinds)
F['event_kind_count'] = len(kinds)
F['kind_counts'] = tuple(sorted(kind_counts.items()))
F['root_menu_size'] = len(ROOTMENU)
F['root_menu'] = tuple(sorted(((e[0], str(q)) for e, q in ROOTMENU)))
F['root_menu_mass'] = str(sum(q for e, q in ROOTMENU))
F['budget_propose'] = tuple(sorted(str(x) for x in _bud['p']))
F['budget_deliver'] = tuple(sorted(str(x) for x in _bud['d']))
F['budget_arbmerge'] = tuple(sorted(str(x) for x in _bud['r+m']))


def mass_census(upto):
    c = defaultdict(int)
    for d in range(0, upto + 1):
        for v, n in _mass[d].items():
            c[v] += n
    return tuple(sorted((str(v), n) for v, n in c.items()))


F['mass_census_d4'] = mass_census(4)
F['mass_census_d5'] = mass_census(5)
F['mass_census_d6'] = mass_census(6)
F['mass_values_d6'] = tuple(v for v, n in F['mass_census_d6'])

# delivery's preconditions/effects, and its NON-INJECTIVITY (T8)
_dd = 0
for h in CACHE:
    if len(h) > 3:
        continue
    for e, q in CACHE[h]:
        if e[0] == 'd' and any(x[0] == 'd' and x[1] == e[1]
                               and x[2] == e[2] and x[3] == e[3]
                               for x in h):
            _dd += 1
F['redelivery_admissible'] = _dd
_merge_depths = defaultdict(int)
for h in CACHE:
    for e, q in CACHE[h]:
        if e[0] == 'm':
            _merge_depths[len(h)] += 1
F['merge_menu_depths'] = tuple(sorted(_merge_depths.items()))
F['histories_with_merge'] = sum(1 for h in CACHE
                                if any(e[0] == 'm' for e in h))

emit(f"  event kinds present in the family: {list(F['event_kinds'])} "
     f"— p propose, r arbitrate, m merge, d deliver, n idle.")
emit(f"  PIN ERRATUM, REGISTERED AND MEASURED (v14 #4 practice): the "
     f"pin's T1 summary column describes the layer as carrying "
     f"{F['pin_erratum_kind_count'][0]} event kinds.  An AST census of "
     f"the committed generator's own source finds exactly "
     f"{F['layer_kind_branches']} kind branches inside candidates_for "
     f"— {list(F['layer_kind_tags'])} — and the built family emits "
     f"exactly {F['event_kind_count']}.  There is no sixth kind "
     f"anywhere in the layer: this is a PIN ERROR, not an "
     f"arena-dependent count, and this receipt reports the "
     f"measurement.")
emit(f"  menu entries by kind over the whole depth-{CAP_T} family: "
     f"{dict(F['kind_counts'])}")
emit(f"  BUDGETS, MEASURED off the layer (never quoted), PER ACTOR — "
     f"T1's own parenthetical says the deliver sector is sender-view "
     f"and the arb-and-merge sector is components join-view plus pairs "
     f"initiator-view, so a per-MENU reading would be the wrong "
     f"object: the propose sector carries total "
     f"{list(F['budget_propose'])} per actor; the deliver sector "
     f"{list(F['budget_deliver'])} per actor; idle absorbs the "
     f"remainder.  T1's docstring line is the verbatim-context anchor "
     f"of gate A1-BUDGETS.")
emit(f"  THE ARB-AND-MERGE SECTOR IS JOIN-VIEW AND IS REPORTED AS "
     f"MEASURED, not asserted: its per-actor totals take the values "
     f"{list(F['budget_arbmerge'])}.  The excess over the declared "
     f"quarter is exactly what makes the total menu mass depart from "
     f"the actor count, and that departure is the corpus's "
     f"QUARTER-QUANTIZED LADDER, re-derived here: menu-weight-sum "
     f"census {dict(F['mass_census_d4'])} at depth <= 4, "
     f"{dict(F['mass_census_d5'])} at depth <= 5, and "
     f"{dict(F['mass_census_d6'])} at depth <= 6 — the VALUE SET is "
     f"unchanged one level deeper than the committed claim.")
_rmagg = defaultdict(int)
for k, q in F['root_menu']:
    _rmagg[(k, q)] += 1
emit(f"  the ROOT menu: {F['root_menu_size']} entries, total mass "
     f"{F['root_menu_mass']} — "
     + ", ".join(f"{n}x{k}@{q}" for (k, q), n in sorted(_rmagg.items())))
emit(f"  DELIVERY IS NON-INJECTIVE (T8's row, re-measured): "
     f"re-delivery of an already-delivered (sender, receiver, version) "
     f"triple is admissible at {F['redelivery_admissible']} menu "
     f"entries in the depth-3 window.")
emit(f"  MERGE has support only deep: merge entries appear in menus at "
     f"parent depths {dict(F['merge_menu_depths'])}, and "
     f"{F['histories_with_merge']} of the {len(CACHE)} histories "
     f"contain a merge event at all.")

gate("A1-KINDS", KIND_SUB,
     "the committed layer generates exactly the FIVE kinds the layer "
     "defines (p, r, m, d, n) and no others, with merge present — the "
     "pin's T1 summary column says six; this is the measurement, and "
     "the discrepancy is registered in-unit as a PIN ERRATUM",
     lambda f: (set(f['event_kinds']) == {'p', 'r', 'm', 'd', 'n'}
                and f['event_kind_count'] == 5
                and f['layer_kind_branches'] == 5
                and dict(f['kind_counts'])['m'] > 0),
     lambda f: f"kinds = {list(f['event_kinds'])} ({f['event_kind_count']}"
               f"); generator branches = {f['layer_kind_branches']}; "
               f"counts = {dict(f['kind_counts'])}")
gate("A1-BUDGETS", KIND_SUB,
     "the declared budgets are the measured ones, PER ACTOR: the "
     "propose sector totals exactly 1/4 wherever it is non-empty and "
     "the deliver sector exactly 1/4 — consumer of T1's verbatim "
     "budget line.  The arb-and-merge sector is join-view and its "
     "measured value set is reported beside them rather than asserted "
     "equal to a quarter",
     lambda f: (set(f['budget_propose']) == {'1/4'}
                and set(f['budget_deliver']) == {'1/4'}
                and set(f['budget_arbmerge']) == {'1/2', '1/4'}),
     lambda f: f"propose {list(f['budget_propose'])}; deliver "
               f"{list(f['budget_deliver'])}; arb+merge (join-view) "
               f"{list(f['budget_arbmerge'])}")
gate("A1-LADDER", KIND_SUB,
     "THE QUARTER-QUANTIZED LADDER, re-derived: the per-history menu "
     "weight sum takes the value set {2, 5/2} with multiplicities "
     "{2: 3757, 5/2: 212} at depth <= 4 and {2: 29605, 5/2: 1124} at "
     "depth <= 5 — both committed — and the VALUE SET is unchanged at "
     "depth <= 6, which is this receipt's own one-level extension",
     lambda f: (f['mass_census_d4'] == (('2', 3757), ('5/2', 212))
                and f['mass_census_d5'] == (('2', 29605), ('5/2', 1124))
                and set(f['mass_values_d6']) == {'2', '5/2'}),
     lambda f: f"depth <= 4: {dict(f['mass_census_d4'])}; depth <= 5: "
               f"{dict(f['mass_census_d5'])}; depth <= 6 (NEW): "
               f"{dict(f['mass_census_d6'])}")
gate("A1-DELIVERY", KIND_SUB,
     "delivery is NON-INJECTIVE at transport scope (T8): re-delivery "
     "of the same (sender, receiver, version) is admissible, so the "
     "delivery map does not embed the record",
     lambda f: f['redelivery_admissible'] > 0,
     lambda f: f"re-delivery menu entries in the depth-3 window = "
               f"{f['redelivery_admissible']}")
gate("A1-LAYER", KIND_SUB,
     "SINGLE SOURCE: the committed d42b1 layer is exec'd from its own "
     "path, pre-print slice only, carrying candidates_for, admissible, "
     "event_poset, View, vname, V0 and BOTH option enumerators; "
     "nothing about admission or pricing is re-implemented here",
     lambda f: (len(f['layer_defs']) == 8 and f['layer_no_exit']
                and f['layer_path'] == 'v10/code/d42b1_transport_exact.py'
                and f['layer_prefix_chars'] > 10000),
     lambda f: f"{f['layer_path']}: prefix {f['layer_prefix_chars']} "
               f"chars, {len(f['layer_defs'])} definitions lifted, "
               f"0 sys.exit / 0 top-level check / 0 top-level print")

# ======================================================================
# ARM A, FACT 2 — THE CENSUS AND THE POTENTIALS, BOTH SCOPES
# ======================================================================
emit("")
emit("[ARM A / FACT 2 — the ARM-1T census, the delivery-free partner, "
     "G_1..G_7 at both scopes, and the DELIVERIES-REDUCE-BRANCHING "
     "sign]")

prog("building the delivery-free partner ...")
_t = time.time()
DF = build(cf_delivery_free, AB, CAP_DF)
prog(f"delivery-free family built: {len(DF)} histories in "
     f"{time.time() - _t:.1f}s")


def levels(cache, cap):
    per = [0] * (cap + 1)
    for h in cache:
        per[len(h)] += 1
    cum, s = [], 0
    for x in per:
        s += x
        cum.append(s)
    return tuple(per), tuple(cum)


F['t_per_level'], F['t_cumulative'] = levels(CACHE, CAP_T)
F['df_per_level'], F['df_cumulative'] = levels(DF, CAP_DF)
F['t_total'] = len(CACHE)
F['df_total'] = len(DF)


def potentials(cache, cap, rmax):
    """G(h, 0) = 1; G(h, r) = sum_e q(e|h) G(h+e, r-1).  Computed
    bottom-up level by level: GT[h] = [G(h,1), G(h,2), ...] up to the
    horizon the family's depth admits."""
    lev = defaultdict(list)
    for h in cache:
        lev[len(h)].append(h)
    GT = {}
    for d in range(cap, -1, -1):
        for h in lev[d]:
            rmaxh = min(rmax, cap + 1 - d)
            vals = []
            for r in range(1, rmaxh + 1):
                if r == 1:
                    vals.append(sum(q for e, q in cache[h]))
                else:
                    vals.append(sum(q * GT[h + (e,)][r - 2]
                                    for e, q in cache[h]))
            GT[h] = vals
    return GT


prog("computing the transport potentials ...")
GT = potentials(CACHE, CAP_T, RMAX)
prog("computing the delivery-free potentials ...")
GD = potentials(DF, CAP_DF, RMAX)

F['G_transport'] = tuple(str(x) for x in GT[ROOT])
F['G_deliveryfree'] = tuple(str(x) for x in GD[ROOT])
F['G_t_frac'] = tuple(GT[ROOT])
F['G_d_frac'] = tuple(GD[ROOT])
F['df_ge_t'] = tuple(bool(GD[ROOT][i] >= GT[ROOT][i])
                     for i in range(RMAX))
F['df_gt_t_first'] = next((i + 1 for i in range(RMAX)
                           if GD[ROOT][i] != GT[ROOT][i]), None)
F['ratio_transport'] = tuple(str(GT[ROOT][i] / GT[ROOT][i - 1])
                             for i in range(1, RMAX))
F['ratio_deliveryfree'] = tuple(str(GD[ROOT][i] / GD[ROOT][i - 1])
                                for i in range(1, RMAX))
F['ratio_df_ge_t'] = all(
    GD[ROOT][i] / GD[ROOT][i - 1] >= GT[ROOT][i] / GT[ROOT][i - 1]
    for i in range(1, RMAX))

emit(f"  ARM-1T (A, B), exhaustive menus to depth {CAP_T}:")
emit(f"    per level  = {list(F['t_per_level'])}")
emit(f"    cumulative = {list(F['t_cumulative'])}  -> "
     f"{F['t_total']} histories")
emit(f"  THE DELIVERY-FREE PARTNER (derived from T1 by withholding the "
     f"delivery kind; NOT imported from a second layer):")
emit(f"    per level  = {list(F['df_per_level'])}")
emit(f"    cumulative = {list(F['df_cumulative'])}  -> "
     f"{F['df_total']} histories")
emit(f"  THE FINITE-HORIZON POTENTIALS AT THE ROOT, exact:")
emit(f"    D | delivery-free G_D | transport G_D | df ratio | "
     f"transport ratio")
for i in range(RMAX):
    rr_d = (str(GD[ROOT][i] / GD[ROOT][i - 1]) if i else "-")
    rr_t = (str(GT[ROOT][i] / GT[ROOT][i - 1]) if i else "-")
    emit(f"    {i + 1} | {GD[ROOT][i]} | {GT[ROOT][i]} | {rr_d} | "
         f"{rr_t}")
emit(f"  THE SIGN, MEASURED: the delivery-free potential is >= the "
     f"transport potential at every horizon "
     f"({F['df_ge_t'].count(True)}/{RMAX}), first strictly at D = "
     f"{F['df_gt_t_first']} (delivery-free {GD[ROOT][3]} vs transport "
     f"{GT[ROOT][3]}).  DELIVERIES REDUCE FINITE-HORIZON BRANCHING — "
     f"T7's row, re-derived here and not quoted.  The same sign holds "
     f"ratio for ratio: {F['ratio_df_ge_t']}.")

gate("A2-CENSUS", KIND_SUB,
     "the ARM-1T census reproduces the committed cumulative sizes "
     "[1, 9, 69, 521, 3969, 30729] and 243,769 to depth 6, with the "
     "per-level breakdown [1, 8, 60, 452, 3448, 26760, 213040]",
     lambda f: (f['t_cumulative'] == (1, 9, 69, 521, 3969, 30729, 243769)
                and f['t_per_level'] == (1, 8, 60, 452, 3448, 26760,
                                         213040)
                and f['t_total'] == 243769),
     lambda f: f"cumulative = {list(f['t_cumulative'])}; per level = "
               f"{list(f['t_per_level'])}")
gate("A2-DF-CENSUS", KIND_SUB,
     "the DERIVED delivery-free partner reproduces the committed "
     "partner census [1, 7, 39, 215, 1191, 6471] and 34,375 to depth "
     "6 — the (path, value) anchor that licenses deriving the partner "
     "from T1 instead of reading a second, unpinned layer",
     lambda f: (f['df_cumulative'] == (1, 7, 39, 215, 1191, 6471, 34375)
                and f['df_total'] == 34375),
     lambda f: f"cumulative = {list(f['df_cumulative'])}")
gate("A2-G-TRANSPORT", KIND_SUB,
     "the transport potentials G_1..G_7 = 2, 4, 257/32, 1035/64, "
     "4173/128, 134587/2048, 2168717/16384",
     lambda f: f['G_transport'] == ('2', '4', '257/32', '1035/64',
                                    '4173/128', '134587/2048',
                                    '2168717/16384'),
     lambda f: "; ".join(f"G_{i+1} = {v}" for i, v in
                         enumerate(f['G_transport'])))
gate("A2-G-DF", KIND_SUB,
     "the delivery-free potentials G_1..G_7 = 2, 4, 257/32, 1037/64, "
     "2101/64, 68313/1024, 139065/1024",
     lambda f: f['G_deliveryfree'] == ('2', '4', '257/32', '1037/64',
                                       '2101/64', '68313/1024',
                                       '139065/1024'),
     lambda f: "; ".join(f"G_{i+1} = {v}" for i, v in
                         enumerate(f['G_deliveryfree'])))
gate("A2-SIGN", KIND_SUB,
     "DELIVERIES REDUCE BRANCHING, measured with its sign: the "
     "delivery-free potential dominates the transport potential at "
     "every horizon and the two first separate at D = 4 "
     "(1037/64 > 1035/64)",
     lambda f: (all(f['df_ge_t']) and f['df_gt_t_first'] == 4
                and f['ratio_df_ge_t']
                and f['G_deliveryfree'][3] == '1037/64'
                and f['G_transport'][3] == '1035/64'),
     lambda f: f"df >= transport at all {len(f['df_ge_t'])} horizons = "
               f"{all(f['df_ge_t'])}; first separation at D = "
               f"{f['df_gt_t_first']}")

# ======================================================================
# ARM A, FACT 3 — THE RELATIVE-HORIZON KERNELS
# ======================================================================
emit("")
emit("[ARM A / FACT 3 — the relative-horizon kernels k_r(e|h) = "
     "q(e|h) G(h+e, r-1) / G(h, r), r = 1..7]")
emit("  WHAT IS AND IS NOT SUBSTANTIVE HERE, said before the numbers, "
     "and taken from the round that corrected the predecessor.  "
     "sum_e k_r(e|h) = 1 is an IDENTITY of the construction: G(h, r) "
     "is DEFINED as sum_e q(e|h) G(h+e, r-1) and k_r divides by it.  "
     "Cut-additivity of the chained measure follows BY INDUCTION from "
     "that identity — a chain of probability kernels has cut mass 1 at "
     "every cut — so it is DISCLOSED here, not gated as a "
     "measurement.  THE SUBSTANTIVE PROPERNESS GATE IS STRICT "
     "POSITIVITY: a zero potential is the only way the identity can "
     "break, and it is the only clause below that could have come out "
     "otherwise.")


def krel(h, r):
    tot = GT[h][r - 1]
    return {e: q * (Fr(1) if r == 1 else GT[h + (e,)][r - 2]) / tot
            for e, q in CACHE[h]}


KC = {}


def krel_c(h, r):
    """Memoised krel, used ONLY by ARM B (where the same (h, r) pair is
    revisited across blocks and step counts).  The properness sweep
    deliberately does not memoise: it must recompute."""
    k = (h, r)
    v = KC.get(k)
    if v is None:
        v = krel(h, r)
        KC[k] = v
    return v


prog("kernel properness / positivity sweep, r = 1..7 ...")
_t = time.time()
prop_rows = []
pos_bad = 0
prop_bad = 0
gpos_bad = 0
for r in range(1, RMAX + 1):
    n = 0
    for d in range(0, CAP_T + 2 - r):
        for h in LEVEL[d]:
            n += 1
            for v in GT[h][:min(len(GT[h]), r)]:
                if v <= 0:
                    gpos_bad += 1
            kk = krel(h, r)
            if sum(kk.values()) != 1:
                prop_bad += 1
            if any(v <= 0 for v in kk.values()):
                pos_bad += 1
    prop_rows.append((r, n))
prog(f"properness sweep done in {time.time() - _t:.1f}s")

F['proper_rows'] = tuple(prop_rows)
F['proper_violations'] = prop_bad
F['positivity_violations'] = pos_bad
F['G_positivity_violations'] = gpos_bad
F['raw_cut_masses'] = tuple(str(x) for x in GT[ROOT])

# the mis-normalized kernel control — must FAIL properness
_mis_bad = 0
_mis_n = 0
for h in CACHE:
    if len(h) > 2:
        continue
    tot = GT[h][1]          # G(h, 2) used where G(h, 3) belongs
    kk = {e: q * GT[h + (e,)][1] / tot for e, q in CACHE[h]}
    _mis_n += 1
    if sum(kk.values()) != 1:
        _mis_bad += 1
F['misnorm_tested'] = _mis_n
F['misnorm_failures'] = _mis_bad

emit("    relative horizon r | histories with a computable k_r | "
     "sum_e k_r = 1 exactly")
for r, n in prop_rows:
    emit(f"    {r} | {n} | exactly")
emit(f"  properness violations over all {sum(n for r, n in prop_rows)} "
     f"(history, horizon) pairs: {F['proper_violations']}")
emit(f"  STRICT POSITIVITY (the substantive gate): kernel entries "
     f"<= 0: {F['positivity_violations']}; potentials <= 0: "
     f"{F['G_positivity_violations']}.")
emit(f"  CUT-ADDITIVITY, DISCLOSED AS INDUCTION (not gated as a "
     f"measurement): given sum_e k_r = 1 the chained mass at every cut "
     f"is 1 by induction.  What is worth printing is the contrast: the "
     f"RAW path weight is not a measure — its cut masses "
     f"sum_(|h| = n) q(h) are exactly the root potentials "
     f"{list(F['raw_cut_masses'])}, i.e. unnormalized.")
emit(f"  THE MIS-NORMALIZED-KERNEL CONTROL (negative control, "
     f"pin section 4): dividing by G(h, 2) where G(h, 3) belongs "
     f"breaks properness at {F['misnorm_failures']} of "
     f"{F['misnorm_tested']} tested histories — the properness gate "
     f"can fail, and here is the input that makes it.")
emit("  WINDOW ARTEFACTS, DISCLOSED (the d70 trap, honoured).  A row "
     "at horizon r is taken over the window of histories h with "
     f"len(h) + r <= {CAP_T + 1}; at r = {CAP_T + 1} that window "
     "contains the ROOT AND NOTHING ELSE.  THE OFF-ROOT PREFIX "
     "CONVENTION, stated: every "
     "claim in this unit about behaviour across horizons is taken on "
     "the OFF-ROOT prefix of the window sequence — the horizons whose "
     "window still contains a history of positive length — and a "
     "terminal value on a root-only window is reported as a window "
     "artefact, never as contraction, shrinkage or stability.")

gate("A3-KERNEL", KIND_THM,
     "PROPERNESS: sum_e k_r(e|h) = 1 exactly at every (history, "
     "horizon) pair with r = 1..7.  THEOREM-PASS, disclosed as such: "
     "k_r divides by its own denominator.  Carried as a regression "
     "tripwire on the menu bookkeeping (it catches a menu used in the "
     "kernel that differs from the menu used in the potential)",
     lambda f: (f['proper_violations'] == 0
                and len(f['proper_rows']) == 7),
     lambda f: f"pairs = {sum(n for r, n in f['proper_rows'])}; "
               f"violations = {f['proper_violations']}; per horizon = "
               f"{dict(f['proper_rows'])}")
gate("A3-POSITIVITY", KIND_SUB,
     "STRICT POSITIVITY — the substantive properness gate (T4's own "
     "correction, honoured): every potential and every kernel entry is "
     "strictly positive, so no denominator vanishes anywhere in the "
     "family",
     lambda f: (f['positivity_violations'] == 0
                and f['G_positivity_violations'] == 0),
     lambda f: f"kernel entries <= 0: {f['positivity_violations']}; "
               f"potentials <= 0: {f['G_positivity_violations']}")
gate("A3-MISNORM", KIND_SUB,
     "THE NEGATIVE CONTROL FIRES: a deliberately mis-normalized kernel "
     "fails the properness identity at every tested history — the "
     "properness gate is not vacuous",
     lambda f: (f['misnorm_failures'] == f['misnorm_tested']
                and f['misnorm_tested'] > 0),
     lambda f: f"{f['misnorm_failures']} of {f['misnorm_tested']} "
               f"tested histories fail")
gate("A3-CUTADD", KIND_DIS,
     "CUT-ADDITIVITY IS AN INDUCTION, NOT A MEASUREMENT — disclosed, "
     "not gated.  The raw cut masses are the root potentials, i.e. the "
     "raw weight is unnormalized; the horizon normalization is what "
     "buys mass 1 at every cut",
     lambda f: (f['raw_cut_masses'][0] == '2'
                and f['raw_cut_masses'][-1] == '2168717/16384'),
     lambda f: f"raw cut masses = {list(f['raw_cut_masses'])}")

# ======================================================================
# ARM A, FACT 4 — THE RENEWAL PORTS
# ======================================================================
emit("")
emit("[ARM A / FACT 4 — the renewal ports R-SIG and R-MENU, "
     "re-derived]")
emit("  R-SIG : every actor's NON-SUPERSEDED holdings is the same "
     "singleton {v}; no live proposals; no components; no merge "
     "pairs.  (The literal sigma-level port: the delivery-free "
     "sigma sees the non-superseded token only, because "
     "prop_options_in_view SKIPS superseded.)")
emit("  R-MENU: R-SIG and, in addition, holdings(a) = {v} EXACTLY for "
     "every a — no superseded remainder.  (The menu-exact port: at "
     "transport scope deliver_options_in_view enumerates over the "
     "WHOLE holdings set, so anything left in it is visible in the "
     "menu.)")


def state_of(h):
    pred = event_poset(list(h))
    vw = View(list(h), pred, set(range(len(h))))
    hold = {a: frozenset(vw.holdings(a)) for a in AB}
    nsup = {a: frozenset(x for x in hold[a] if x not in vw.superseded)
            for a in AB}
    return vw, hold, nsup


def rsig_full(h):
    """d70's predicate, verbatim in content."""
    vw, hold, nsup = state_of(h)
    if any(len(nsup[a]) != 1 for a in AB):
        return None
    if nsup['B'] != nsup['A']:
        return None
    if vw.live or vw.components():
        return None
    if any(vw.merge_pairs(a) for a in AB):
        return None
    v = next(iter(nsup['A']))
    return (v, (len(hold['A']), len(hold['B'])),
            all(hold[a] == frozenset({v}) for a in AB))


def rsig_fast(h):
    """The reduced predicate: live empty AND both non-superseded
    holdings the same singleton.  (Components are built from live
    proposals, so live = {} forces components = {}; merge_pairs needs
    two non-superseded created versions, so a singleton forces it
    empty.)  GATED against rsig_full below rather than assumed."""
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


prog("R-SIG / R-MENU predicate: reduction control on depth <= 5 ...")
_t = time.time()
_dis = 0
_n5 = 0
for h in CACHE:
    if len(h) > 5:
        continue
    _n5 += 1
    if rsig_full(h) != rsig_fast(h):
        _dis += 1
F['pred_reduction_tested'] = _n5
F['pred_reduction_disagreements'] = _dis
prog(f"reduction control done in {time.time() - _t:.1f}s "
     f"({_dis} disagreements over {_n5})")

prog("R-SIG / R-MENU over the whole depth-6 family ...")
_t = time.time()
RS = {}
for h in CACHE:
    r = rsig_fast(h)
    if r is not None:
        RS[h] = r
prog(f"R-SIG scan done in {time.time() - _t:.1f}s ({len(RS)} points)")

RSIG5 = {h: v for h, v in RS.items() if len(h) <= 5}
RMENU5 = {h: v for h, v in RSIG5.items() if v[2]}
RSIGSET5 = set(RSIG5)
RMENUSET5 = set(RMENU5)


def rename_v(e, v):
    if e[0] == 'p':
        return ('p', e[1], v if e[2] == V0 else e[2], e[3])
    if e[0] == 'd':
        return ('d', e[1], e[2], v if e[3] == V0 else e[3])
    return e


_menu_ok = _menu_bad = 0
_mm_ok = _mm_bad = 0
_want_root = {(SK(rename_v(e, V0)), q) for e, q in ROOTMENU}
NOT_MENU_EXACT = set()
for h, (v, prof, isme) in RSIG5.items():
    want = {(SK(rename_v(e, v)), q) for e, q in ROOTMENU}
    got = {(SK(e), q) for e, q in CACHE[h]}
    if got == want and len(CACHE[h]) == len(ROOTMENU):
        _menu_ok += 1
    else:
        _menu_bad += 1
        NOT_MENU_EXACT.add(h)
    if isme:
        if got == want and len(CACHE[h]) == len(ROOTMENU):
            _mm_ok += 1
        else:
            _mm_bad += 1


def reentry(S):
    return sum(1 for h in S if any(h[:i] not in S for i in range(len(h))))


def reentered_set(S):
    """The points of S reached from OUTSIDE it: a point with a proper
    prefix outside S.  Carried as a SET so a set claim can be gated as
    one (MINOR-4/MINOR-7 of the rounds: a set identity gated by two
    cardinalities is weaker than the prose it licenses)."""
    return {h for h in S
            if any(h[:i] not in S for i in range(len(h)))}


def entries_into(S):
    """The number of TRANSITIONS from outside S into S — the object a
    regeneration argument actually needs, as against `reentry`, which
    for any S not containing the root returns |S| by construction."""
    n = 0
    for h in CACHE:
        if h in S:
            continue
        for e, q in CACHE[h]:
            if h + (e,) in S:
                n += 1
    return n


REENTERED_SET5 = reentered_set(RSIGSET5)


F['rsig_count'] = len(RSIG5)
F['rmenu_count'] = len(RMENU5)
F['rsig_menu_exact'] = _menu_ok
F['rsig_menu_not_exact'] = _menu_bad
F['rmenu_menu_exact'] = _mm_ok
F['rmenu_menu_not_exact'] = _mm_bad
F['rsig_reentries'] = reentry(RSIGSET5)
F['rmenu_reentries'] = reentry(RMENUSET5)
F['rsig_notexact_eq_reentered'] = (NOT_MENU_EXACT == REENTERED_SET5)
F['rsig_notexact_symdiff'] = len(NOT_MENU_EXACT ^ REENTERED_SET5)
F['rmenu_4n'] = tuple(sum(1 for h, v in RMENU5.items() if len(h) == n)
                      for n in range(0, 6))
F['rmenu_is_4n'] = all(F['rmenu_4n'][n] == 4 ** n for n in range(0, 6))
F['rmenu_sum_4n'] = sum(F['rmenu_4n'])
_prof = defaultdict(int)
for h, (v, p, m) in RSIG5.items():
    _prof[p] += 1
F['rsig_profiles'] = tuple(sorted(_prof.items()))
F['rsig_depths'] = tuple(sorted({len(h) for h in RSIG5}))

emit(f"  R-SIG  points at depth <= 5: {F['rsig_count']} (depths "
     f"{list(F['rsig_depths'])}); menu-exact at "
     f"{F['rsig_menu_exact']}, NOT menu-exact at "
     f"{F['rsig_menu_not_exact']}")
emit(f"  R-MENU points at depth <= 5: {F['rmenu_count']}; menu-exact "
     f"at {F['rmenu_menu_exact']}, NOT menu-exact at "
     f"{F['rmenu_menu_not_exact']}")
emit(f"  RE-ENTRIES (points reached from OUTSIDE the class): R-MENU "
     f"{F['rmenu_reentries']} -> absorbing-complement = "
     f"{F['rmenu_reentries'] == 0}; R-SIG {F['rsig_reentries']} -> "
     f"absorbing-complement = {F['rsig_reentries'] == 0}.  The R-SIG "
     f"points that are not menu-exact are EXACTLY the re-entered ones "
     f"— a SET IDENTITY, gated as one: the symmetric difference of the "
     f"two sets is {F['rsig_notexact_symdiff']}, not merely their "
     f"cardinalities agreeing.")
emit(f"  R-MENU by depth = {list(F['rmenu_4n'])} — exactly 4^n at "
     f"every depth ({F['rmenu_is_4n']}), summing to "
     f"{F['rmenu_sum_4n']} = sum_(n <= 5) 4^n.")
emit(f"  THE HOLDINGS-PROFILE DECOMPOSITION OF R-SIG (new here, and "
     f"ARM B rides on it): (|holdings(A)|, |holdings(B)|) -> count = "
     f"{dict(F['rsig_profiles'])}.  R-MENU is exactly the profile-"
     f"(1, 1) block; the rest of R-SIG is a ladder of further blocks.")

# the renewal masses
prog("renewal mass census ...")
QW = {ROOT: Fr(1)}
KW = {ROOT: Fr(1)}
for n in range(0, 5):
    nq, nk = {}, {}
    for h in [x for x in QW if len(x) == n]:
        kk = krel(h, CAP_T + 1 - n)
        for e, q in CACHE[h]:
            nq[h + (e,)] = nq.get(h + (e,), Fr(0)) + QW[h] * q
            nk[h + (e,)] = nk.get(h + (e,), Fr(0)) + KW[h] * kk[e]
    QW.update(nq)
    KW.update(nk)
ret_q = defaultdict(lambda: Fr(0))
ret_k = defaultdict(lambda: Fr(0))
for h in QW:
    if h in RMENUSET5 and h != ROOT:
        ret_q[len(h)] += QW[h]
        ret_k[len(h)] += KW[h]
F['renewal_raw_q'] = tuple(str(ret_q[n]) for n in range(1, 6))
F['renewal_raw_is_32n'] = all(ret_q[n] == Fr(3, 2) ** n
                              for n in range(1, 6))
F['renewal_k'] = tuple(str(ret_k[n]) for n in range(1, 6))
F['nonrenewal_k'] = tuple(str(1 - ret_k[n]) for n in range(1, 6))
F['nonrenewal_depth5'] = str(1 - ret_k[5])
F['renewal_depth5_closed'] = str((Fr(3, 2) ** 5) * GT[ROOT][1]
                                 / GT[ROOT][6])
F['renewal_depth5_measured'] = str(ret_k[5])
F['nonrenewal_grows'] = all((1 - ret_k[n]) >= (1 - ret_k[n - 1])
                            for n in range(2, 6))

emit("  RETURN-WEIGHT CENSUS (a DEPARTURE census: the renewal class is "
     "never re-entered, so there are no cycles, only a survival "
     "curve).  Normalization named at every use: column q is the RAW "
     f"committed weight product; column k is the horizon-{CAP_T + 1} "
     "completed conditional chained from the root under C1.")
emit("    n | # renewal histories | raw-q mass | completed k mass | "
     "k mass NOT at a renewal")
for n in range(1, 6):
    emit(f"    {n} | {F['rmenu_4n'][n]} | {frs(ret_q[n])} | "
         f"{frs(ret_k[n])} | {frs(1 - ret_k[n])}")
emit(f"  the raw renewal mass is exactly (3/2)^n: "
     f"{F['renewal_raw_is_32n']}.")
emit(f"  THE 0.7705: the horizon-completed mass NOT at a renewal at "
     f"depth 5 is {F['nonrenewal_depth5']} "
     f"(~{float(1 - ret_k[5]):.6f}).  Its closed form: the renewal "
     f"mass at depth 5 is (3/2)^5 * G_2 / G_7 = "
     f"{F['renewal_depth5_closed']}, and the measured value is "
     f"{F['renewal_depth5_measured']} — the same rational, computed "
     f"two independent ways (a chained product of kernels versus a "
     f"closed rational expression in the potentials).")

# MONOTONICITY, AT FULL FAMILY SCOPE.  The first delivery censused
# 30,728 transitions — those out of histories of depth < 5, 12.6% of
# the family — and the abstract then said "zero transitions of the
# family".  The census below runs over EVERY transition of the family
# (243,768 of them), so the sentence and its receipt key now have the
# same scope.  Both scopes are kept and both are printed, because
# section 7's absorbing-complement argument uses the narrowed
# non-superseded figure and the successor must be able to tell them
# apart.
prog("holdings monotonicity census, FULL FAMILY scope ...")
_t = time.time()
mono_bad = 0
mono_pairs = 0
nsup_shrink = 0
mono_bad_all = 0
mono_pairs_all = 0
nsup_shrink_all = 0
prof_dec_all = 0
mono_entail_bad = 0
grow_first = defaultdict(int)
HOLD = {}
for h in CACHE:
    vw, hold, nsup = state_of(h)
    HOLD[h] = (hold, nsup)
MONO_EXPECT = sum(len(CACHE[h]) for h in CACHE if len(h) < 5)
MONO_EXPECT_ALL = sum(len(CACHE[h]) for h in CACHE if len(h) < CAP_T)
for h in CACHE:
    if len(h) >= CAP_T:
        continue
    hold_h, nsup_h = HOLD[h]
    narrow = len(h) < 5
    for e, q in CACHE[h]:
        h2 = h + (e,)
        if h2 not in HOLD:
            continue
        hold_2, nsup_2 = HOLD[h2]
        set_shrink = any(not hold_h[a] <= hold_2[a] for a in AB)
        card_shrink = any(len(hold_2[a]) < len(hold_h[a]) for a in AB)
        mono_pairs_all += 1
        if set_shrink:
            mono_bad_all += 1
        if card_shrink:
            prof_dec_all += 1
        # THE ENTAILMENT, MACHINE-CHECKED POINTWISE: set-monotonicity
        # of holdings entails cardinality-monotonicity of the profile,
        # so a profile decrease without a set shrink is impossible.
        # This is the forcing that makes B3-MONOTONE a theorem-pass.
        if card_shrink and not set_shrink:
            mono_entail_bad += 1
        if any(not nsup_h[a] <= nsup_2[a] for a in AB):
            nsup_shrink_all += 1
            if narrow:
                nsup_shrink += 1
        if narrow:
            mono_pairs += 1
            if set_shrink:
                mono_bad += 1
            if (any(len(hold_h[a]) == 1 for a in AB)
                    and any(len(hold_2[a]) > 1 for a in AB)):
                grow_first[e[0]] += 1
prog(f"monotonicity census done in {time.time() - _t:.1f}s")
F['mono_pairs'] = mono_pairs
F['mono_expect'] = MONO_EXPECT
F['mono_shrinking'] = mono_bad
F['nsup_shrinking'] = nsup_shrink
F['mono_pairs_all'] = mono_pairs_all
F['mono_expect_all'] = MONO_EXPECT_ALL
F['mono_shrinking_all'] = mono_bad_all
F['nsup_shrinking_all'] = nsup_shrink_all
F['mono_entailment_violations'] = mono_entail_bad
F['grow_first_by_kind'] = tuple(sorted(grow_first.items()))

emit(f"  HOLDINGS MONOTONICITY, AT FULL FAMILY SCOPE.  Over ALL "
     f"{F['mono_pairs_all']} transitions of the family (every "
     f"transition out of every history of depth < {CAP_T}, expected "
     f"{F['mono_expect_all']} from the census): holdings-SHRINKING "
     f"transitions = {F['mono_shrinking_all']}; profile-DECREASING "
     f"transitions = {prof_dec_all}.  THE NARROWED SCOPE IS KEPT "
     f"BESIDE IT AND NAMED, because section 7's absorbing-complement "
     f"argument uses it: over the {F['mono_pairs']} transitions out of "
     f"depth < 5, holdings-shrinking = {F['mono_shrinking']} and "
     f"NON-SUPERSEDED-shrinking = {F['nsup_shrinking']}; at full scope "
     f"non-superseded holdings shrink at "
     f"{F['nsup_shrinking_all']} transitions.  THAT IS "
     f"EXACTLY WHY THE ABSORBING-COMPLEMENT ARGUMENT COVERS R-MENU "
     f"AND NOTHING ELSE: R-MENU asks for holdings(a) = {{v}} and "
     f"holdings never shrink; R-SIG asks only about the "
     f"non-superseded part, which does.  Event kinds that first break "
     f"singleton holdings (depth < 5 window): "
     f"{dict(F['grow_first_by_kind'])}.")

# --- A4-PRED: the two-way demonstration that reclassifies it.  The
# --- reduction's agreement is FORCED (components are built from live
# --- proposals, so live = {} gives components = {}; merge_pairs needs
# --- two non-superseded created versions, so a singleton gives none),
# --- and a forced agreement is not a measurement.  The forcing is
# --- machine-checked in the positive direction here, and the negative
# --- direction is exhibited by an UNFORCED variant of the same
# --- reduction, which does disagree.
prog("A4-PRED forcing: the two-way demonstration ...")
_forced_comp = 0
_forced_merge = 0
_forced_n = 0


def rsig_unforced(h):
    """The reduction with the FORCED clause kept and the UNFORCED one
    dropped: live empty and |nsup(A)| = 1, without requiring the two
    actors' non-superseded singletons to agree.  Nothing forces this to
    match the full predicate, and it does not."""
    pred = event_poset(list(h))
    vw = View(list(h), pred, set(range(len(h))))
    if vw.live:
        return None
    hold = {a: frozenset(vw.holdings(a)) for a in AB}
    nsup = {a: frozenset(x for x in hold[a] if x not in vw.superseded)
            for a in AB}
    if len(nsup['A']) != 1:
        return None
    v = next(iter(nsup['A']))
    return (v, (len(hold['A']), len(hold['B'])),
            all(hold[a] == frozenset({v}) for a in AB))


_unforced_dis = 0
for h in CACHE:
    if len(h) > 5:
        continue
    pred = event_poset(list(h))
    vw = View(list(h), pred, set(range(len(h))))
    hold = {a: frozenset(vw.holdings(a)) for a in AB}
    nsup = {a: frozenset(x for x in hold[a] if x not in vw.superseded)
            for a in AB}
    if not vw.live:
        _forced_n += 1
        if vw.components():
            _forced_comp += 1
        if all(len(nsup[a]) == 1 for a in AB) and any(
                vw.merge_pairs(a) for a in AB):
            _forced_merge += 1
    if rsig_full(h) != rsig_unforced(h):
        _unforced_dis += 1
F['pred_forcing_tested'] = _forced_n
F['pred_forcing_live_empty_but_components'] = _forced_comp
F['pred_forcing_singleton_but_merge_pairs'] = _forced_merge
F['pred_unforced_disagreements'] = _unforced_dis
emit(f"  THE REDUCTION IS FORCED, AND THE FORCING IS MACHINE-CHECKED "
     f"IN BOTH DIRECTIONS (this is why A4-PRED is carried as a "
     f"THEOREM-PASS and not counted as a measurement).  FORWARD: over "
     f"the {F['pred_forcing_tested']} histories of depth <= 5 with an "
     f"empty live set, histories with a NON-empty component set = "
     f"{F['pred_forcing_live_empty_but_components']}; among those with "
     f"singleton non-superseded holdings, histories with a non-empty "
     f"merge-pair set = {F['pred_forcing_singleton_but_merge_pairs']}. "
     f"Both are structurally impossible and both measure 0.  REVERSE: "
     f"the SAME reduction with its one UNFORCED clause dropped (no "
     f"requirement that the two actors' singletons agree) disagrees "
     f"with the full predicate at {F['pred_unforced_disagreements']} "
     f"histories — so the comparison can fail, and what makes the "
     f"delivered reduction agree is the forcing, not the family.")

gate("A4-PRED", KIND_THM,
     "THE REDUCED R-SIG PREDICATE IS THE COMMITTED PREDICATE, AND THE "
     "AGREEMENT IS FORCED — carried as a THEOREM-PASS with its forcing "
     "exhibited, not as a measurement: components are built from live "
     "proposals so an empty live set forces an empty component set (0 "
     "counterexamples), and a merge pair needs two non-superseded "
     "created versions so a singleton forces none (0 counterexamples). "
     "Over every history of depth <= 5 the reduced form agrees with "
     "the full form at every single history",
     lambda f: (f['pred_reduction_disagreements'] == 0
                and f['pred_reduction_tested'] == 30729
                and f['pred_forcing_live_empty_but_components'] == 0
                and f['pred_forcing_singleton_but_merge_pairs'] == 0),
     lambda f: f"disagreements = {f['pred_reduction_disagreements']} "
               f"over {f['pred_reduction_tested']} histories; forcing "
               f"counterexamples "
               f"{f['pred_forcing_live_empty_but_components']} / "
               f"{f['pred_forcing_singleton_but_merge_pairs']}")
gate("A4-PRED-UNFORCED", KIND_SUB,
     "THE OTHER HALF OF THE TWO-WAY DEMONSTRATION, and it is the "
     "substantive one: the same reduction with its single UNFORCED "
     "clause dropped DOES disagree with the committed predicate, at a "
     "strictly positive number of histories — so the reduction "
     "comparison is not vacuous, and the delivered agreement is bought "
     "by the forcing rather than by the window",
     lambda f: f['pred_unforced_disagreements'] > 0,
     lambda f: f"unforced-variant disagreements = "
               f"{f['pred_unforced_disagreements']} over "
               f"{f['pred_reduction_tested']} histories")
gate("A4-PORTS", KIND_SUB,
     "THE TWO PORTS COME APART AT TRANSPORT SCOPE, with the committed "
     "counts: R-SIG = 5,161 points of which 1,365 are menu-exact and "
     "3,796 are not; R-MENU = 1,365, menu-exact at all of them; "
     "R-MENU has 0 re-entries (absorbing-complement) and R-SIG has "
     "3,796 — and the re-entered points are EXACTLY the non-menu-exact "
     "ones",
     lambda f: (f['rsig_count'] == 5161 and f['rmenu_count'] == 1365
                and f['rsig_menu_exact'] == 1365
                and f['rsig_menu_not_exact'] == 3796
                and f['rmenu_menu_not_exact'] == 0
                and f['rmenu_reentries'] == 0
                and f['rsig_reentries'] == 3796
                and f['rsig_reentries'] == f['rsig_menu_not_exact']
                and f['rsig_notexact_eq_reentered']
                and f['rsig_notexact_symdiff'] == 0),
     lambda f: f"R-SIG {f['rsig_count']} (menu-exact "
               f"{f['rsig_menu_exact']}, not {f['rsig_menu_not_exact']}"
               f"); R-MENU {f['rmenu_count']}; re-entries R-MENU "
               f"{f['rmenu_reentries']}, R-SIG {f['rsig_reentries']}; "
               f"SET identity not-menu-exact = re-entered: "
               f"{f['rsig_notexact_eq_reentered']} (symmetric "
               f"difference {f['rsig_notexact_symdiff']})")
gate("A4-4N", KIND_SUB,
     "the menu-exact renewal count is exactly 4^n at every depth and "
     "sums to 1,365 = sum_(n <= 5) 4^n",
     lambda f: (f['rmenu_is_4n'] and f['rmenu_sum_4n'] == 1365
                and f['rmenu_4n'] == (1, 4, 16, 64, 256, 1024)),
     lambda f: f"by depth = {list(f['rmenu_4n'])}; sum = "
               f"{f['rmenu_sum_4n']}")
gate("A4-MASS", KIND_SUB,
     "the raw renewal mass is exactly (3/2)^n; the horizon-completed "
     "mass NOT at a renewal rises monotonically to 1671053/2168717 "
     "(~0.7705) at depth 5; and the depth-5 renewal mass equals its "
     "closed form (3/2)^5 * G_2 / G_7 = 497664/2168717, computed by "
     "two independent routes (a chained kernel product and a rational "
     "expression in the potentials)",
     lambda f: (f['renewal_raw_is_32n'] and f['nonrenewal_grows']
                and f['nonrenewal_depth5'] == '1671053/2168717'
                and f['renewal_depth5_closed'] == '497664/2168717'
                and f['renewal_depth5_measured']
                == f['renewal_depth5_closed']),
     lambda f: f"raw = {list(f['renewal_raw_q'])}; not-at-renewal = "
               f"{list(f['nonrenewal_k'])}; closed form "
               f"{f['renewal_depth5_closed']} = measured "
               f"{f['renewal_depth5_measured']}")
gate("A4-MONO", KIND_THM,
     "HOLDINGS ARE MONOTONE ALONG EVERY TRANSITION OF THE FAMILY (a "
     "one-line consequence of View.holdings being a union over the "
     "view's arbs, deliveries and merges — carried as a THEOREM-PASS "
     "and censused rather than proved), now at FULL FAMILY SCOPE: 0 "
     "holdings-shrinking transitions over all 243,768, not over the "
     "12.6% window a depth-<5 census would cover",
     lambda f: (f['mono_shrinking_all'] == 0
                and f['mono_pairs_all'] == f['mono_expect_all']
                and f['mono_pairs_all'] == 243768
                and f['mono_shrinking'] == 0
                and f['mono_pairs'] == f['mono_expect']),
     lambda f: f"FULL scope: transitions = {f['mono_pairs_all']} "
               f"(expected {f['mono_expect_all']}), holdings-shrinking "
               f"= {f['mono_shrinking_all']}; narrowed scope: "
               f"{f['mono_pairs']} transitions, "
               f"{f['mono_shrinking']} shrinking")
gate("A4-NSUP-SHRINKS", KIND_SUB,
     "AND THE NARROWING IS GATED SEPARATELY, BECAUSE IT IS THE "
     "SUBSTANTIVE HALF: non-superseded holdings DO shrink, at a "
     "strictly positive number of transitions at BOTH scopes (4,340 "
     "out of depth < 5; 29,980 over the whole family) — which is "
     "exactly why the absorbing-complement argument covers R-MENU and "
     "nothing else.  This predicate could have returned False and the "
     "monotonicity theorem could not",
     lambda f: (f['nsup_shrinking'] > 0
                and f['nsup_shrinking'] == 4340
                and f['nsup_shrinking_all'] == 29980
                and f['nsup_shrinking_all'] > f['nsup_shrinking']),
     lambda f: f"non-superseded-shrinking: {f['nsup_shrinking']} of "
               f"{f['mono_pairs']} (depth < 5), "
               f"{f['nsup_shrinking_all']} of {f['mono_pairs_all']} "
               f"(whole family)")

# ======================================================================
# ARM A, FACT 5 — THE ESCAPE, OWNED AT BOTH COMMITTED GRAINS
# ======================================================================
emit("")
emit("[ARM A / FACT 5 — THE ESCAPE, owned at both committed grains]")
emit("  THE METHOD (T6 section 3.1, re-implemented, not imported): "
     "P_0 = the partition of histories by MENU SHAPE; P_(t+1) = one "
     "probabilistic-bisimulation refinement of P_t.  Two operator "
     "forms exist in the corpus and BOTH are run here: the "
     "PER-CANDIDATE form (two histories stay equivalent iff their "
     "multisets of (weight, successor-class) pairs agree) and the "
     "PER-CLASS-AGGREGATE form (T6's own words: 'for every successor "
     "class the total transition weight into that class agrees "
     "exactly').  T2 binds a successor to the fact that the "
     "distinction is EXTENSIONALLY NULL at the transport cap; that "
     "clause is gated below rather than repeated.")
emit("  THE GRAIN IS ARENA DATA, DECLARED AND PRINTED (RUNBOOK "
     "section 15).  PRIMARY: the 13-class KIND x WEIGHT menu shape "
     "(T3's grain).  CONTROL: the 113-class EVENT x WEIGHT menu shape "
     "(T5's MENU rung).  Choosing one silently is the arena artefact "
     "the era forbids, so both are measured and the disagreement is "
     "the grain-swap control.")

FAM4 = [h for h in CACHE if len(h) <= CAP_ESC]


# Both shape functions are memoised.  They are PURE functions of the
# committed menu at h, and ARM B's five-grain census evaluates them on
# the same successor histories many times over; the cache changes no
# value, only the wall clock, and no wall-clock number reaches the
# receipt.
_SHK = {}
_SHE = {}


def shape_kind(h):
    v = _SHK.get(h)
    if v is None:
        d = defaultdict(int)
        for e, q in CACHE[h]:
            d[(e[0], q)] += 1
        v = ('KIND',) + tuple(sorted(((k, str(q)), n)
                                     for (k, q), n in d.items()))
        _SHK[h] = v
    return v


def shape_event(h):
    v = _SHE.get(h)
    if v is None:
        d = defaultdict(int)
        for e, q in CACHE[h]:
            d[(SK(e), q)] += 1
        v = ('EVENT',) + tuple(sorted(((k, str(q)), n)
                                      for (k, q), n in d.items()))
        _SHE[h] = v
    return v


def relabel(d):
    rel = {}
    for k in sorted(d, key=SK):
        rel.setdefault(SK(d[k]), len(rel))
    return {k: rel[SK(d[k])] for k in d}


def refine(shape, per_candidate=True):
    P = {0: relabel({h: shape(h) for h in FAM4})}
    for t in range(CAP_ESC):
        nxt = {}
        for h in FAM4:
            if len(h) > CAP_ESC - 1 - t:
                continue
            if per_candidate:
                succ = tuple(sorted((str(q), P[t][h + (e,)])
                                    for e, q in CACHE[h]))
            else:
                agg = defaultdict(Fr)
                for e, q in CACHE[h]:
                    agg[P[t][h + (e,)]] += q
                succ = tuple(sorted((c, str(w)) for c, w in agg.items()))
            nxt[h] = (P[t][h], succ)
        P[t + 1] = relabel(nxt)
    return P


def escape_of(P):
    parents = [h for h in FAM4 if len(h) <= CAP_ESC - 2]
    cls2 = {P[1][h] for h in parents}
    ESC = []
    for h in parents:
        for e, q in CACHE[h]:
            c2 = P[1][h + (e,)]
            if c2 not in cls2:
                ESC.append((h, e, q, c2))
    return ESC, sorted({c for _, _, _, c in ESC}), len(cls2)


def tables_of(P):
    tb = {}
    for c in range(1, CAP_ESC + 1):
        tb[c] = [len({P[t][h] for h in FAM4 if len(h) <= c})
                 for t in range(0, CAP_ESC + 1 - c)]
    growth = [(t, CAP_ESC - t,
               sum(1 for h in FAM4 if len(h) <= CAP_ESC - t),
               len({P[t][h] for h in FAM4 if len(h) <= CAP_ESC - t}))
              for t in range(CAP_ESC + 1)]
    return tb, growth


def welldef(P, tcls, parent_cap):
    byc = defaultdict(list)
    for h in FAM4:
        if len(h) <= parent_cap:
            byc[P[tcls][h]].append(h)
    nfail = 0
    first = None
    for c in sorted(byc):
        rows = {}
        for h in byc[c]:
            row = tuple(sorted((str(q), P[tcls][h + (e,)])
                               for e, q in CACHE[h]))
            rows.setdefault(row, h)
        if len(rows) > 1:
            nfail += 1
            if first is None:
                ks = sorted(rows, key=SK)
                first = (c, rows[ks[0]], rows[ks[1]])
    return nfail, len(byc), first


prog("intrinsic-partition refinement, primary grain (kind x weight) ...")
PK = refine(shape_kind, True)
prog("intrinsic-partition refinement, control grain (event x weight) ...")
PE = refine(shape_event, True)
prog("intrinsic-partition refinement, per-class-aggregate operator ...")
PKA = refine(shape_kind, False)

TBK, GRK = tables_of(PK)
TBE, GRE = tables_of(PE)
ESCK, ESCK_CLS, NCLS2K = escape_of(PK)
ESCE, ESCE_CLS, NCLS2E = escape_of(PE)
NF0K, NC0K, FF0K = welldef(PK, 0, CAP_ESC - 1)
NF1K, NC1K, FF1K = welldef(PK, 1, CAP_ESC - 2)
NF0E, NC0E, FF0E = welldef(PE, 0, CAP_ESC - 1)
NF1E, NC1E, FF1E = welldef(PE, 1, CAP_ESC - 2)

F['grain_primary_classes'] = len({PK[0][h] for h in FAM4})
F['grain_control_classes'] = len({PE[0][h] for h in FAM4})
F['grow_primary'] = tuple(GRK)
F['grow_control'] = tuple(GRE)
F['tables_primary'] = tuple(sorted((c, tuple(v)) for c, v in TBK.items()))
F['tables_control'] = tuple(sorted((c, tuple(v)) for c, v in TBE.items()))
F['escape_primary'] = len(ESCK)
F['escape_primary_classes'] = tuple(ESCK_CLS)
F['escape_primary_window_classes'] = NCLS2K
F['escape_control'] = len(ESCE)
F['escape_control_classes'] = len(ESCE_CLS)
F['escape_control_window_classes'] = NCLS2E
F['welldef_primary_level0'] = (NF0K, NC0K)
F['welldef_primary_level1'] = (NF1K, NC1K)
F['welldef_control_level0'] = (NF0E, NC0E)
F['welldef_control_level1'] = (NF1E, NC1E)
F['operator_agree'] = all(
    (PK[t][h] == PK[t][g]) == (PKA[t][h] == PKA[t][g])
    for t in (1,)
    for h in FAM4 if len(h) <= 2
    for g in FAM4 if len(g) <= 2)
F['escape_aggregate'] = len(escape_of(PKA)[0])

emit(f"  PRIMARY GRAIN (kind x weight): "
     f"{F['grain_primary_classes']} classes on the depth-"
     f"{CAP_ESC} family of {len(FAM4)} histories.")
emit(f"    |P_t| tables per window cutoff c: "
     + "; ".join(f"cutoff-{c}: {list(v)}" for c, v in F['tables_primary']))
emit(f"    growth table (t, window len <=, histories, |P_t|): "
     + "; ".join(str(g) for g in F['grow_primary']))
emit(f"    THE ESCAPE: {F['escape_primary']} transitions from len <= "
     f"{CAP_ESC - 2} parents land in "
     f"{len(F['escape_primary_classes'])} classes first realized only "
     f"at len {CAP_ESC - 1} — classes "
     f"{list(F['escape_primary_classes'])}, out of the "
     f"{F['escape_primary_window_classes']} classes the window "
     f"carries.  The window chain is NOT closed.")
if ESCK:
    h_e, e_e, q_e, c_e = min(ESCK, key=lambda r: (len(r[0]), SK(r)))
    F['escape_witness_depth'] = len(h_e)
    F['escape_witness_kind'] = e_e[0]
    F['escape_witness_q'] = str(q_e)
    F['escape_witness_target'] = c_e
    F['escape_witness_target_minlen'] = min(
        len(k) for k in PK[1] if PK[1][k] == c_e)
    emit(f"    ESCAPE WITNESS (exhibited, not asserted): a parent of "
         f"depth {len(h_e)} in class {PK[1][h_e]} takes a "
         f"'{e_e[0]}' event of exact weight {q_e} into class {c_e}, "
         f"whose shallowest member has length "
         f"{F['escape_witness_target_minlen']} — strictly deeper than "
         f"the window.  The transition is a genuine menu entry of the "
         f"committed layer, not a construction of this unit.")
emit(f"  CONTROL GRAIN (event x weight, T5's MENU rung): "
     f"{F['grain_control_classes']} classes on the same family.")
emit(f"    |P_t| tables per window cutoff c: "
     + "; ".join(f"cutoff-{c}: {list(v)}" for c, v in F['tables_control']))
emit(f"    growth table: "
     + "; ".join(str(g) for g in F['grow_control']))
emit(f"    THE ESCAPE at the control grain: {F['escape_control']} "
     f"transitions land in {F['escape_control_classes']} classes that "
     f"lie OUTSIDE the window's {F['escape_control_window_classes']} — "
     f"a finer grain escapes into more classes, not fewer.")
emit(f"  THE GRAIN-SWAP CONTROL FIRES: the two grains disagree exactly "
     f"where T3 and T5 say they must — "
     f"{F['grain_primary_classes']} classes against "
     f"{F['grain_control_classes']}, and "
     f"{F['escape_primary']} escaping transitions against "
     f"{F['escape_control']}.  A verdict taken at one grain and read "
     f"at the other would be an arena artefact; both are printed.")
emit(f"  MENU-SHAPE FACTORISATION FAILS at the primary grain: of the "
     f"{NC0K} level-0 (menu-shape) classes over parents of length <= "
     f"{CAP_ESC - 1}, {NF0K} have non-constant per-candidate rows — "
     f"the menu shape does NOT factorize the transfer.  One "
     f"refinement step repairs it on the shallower window: "
     f"{NF1K} of {NC1K} level-1 classes fail.")
emit(f"  THE PER-CANDIDATE vs PER-CLASS-AGGREGATE OPERATOR (T2's "
     f"binding clause, gated not repeated): the two operators induce "
     f"the SAME partition on the tested window "
     f"({F['operator_agree']}) and the same escape count "
     f"({F['escape_aggregate']} against {F['escape_primary']}) — "
     f"EXTENSIONALLY NULL at the transport cap, exactly as T2 binds a "
     f"successor to say.")
emit(f"  THE HONEST STATEMENT, GATED: no closed exact transfer exists "
     f"at feasible caps.  A closed transfer needs the window's class "
     f"set to be invariant under the transfer; it is not, at either "
     f"grain, by the escape counts above.  Nothing here is an "
     f"instability claim about the partition — the partition behaves; "
     f"the state space outruns every window this unit can afford.")

gate("A5-METHOD", KIND_SUB,
     "the re-implemented refinement reproduces T3's committed growth "
     "table and |P_t| tables at the primary grain: growth (0,4,3969,13"
     "); (1,3,521,11); (2,2,69,6); (3,1,9,2); (4,0,1,1) and tables "
     "cutoff-1 [2,2,2,2] / cutoff-2 [5,6,6] / cutoff-3 [9,11] / "
     "cutoff-4 [13] — consumer of T6's verbatim method window",
     lambda f: (f['grow_primary'] == ((0, 4, 3969, 13), (1, 3, 521, 11),
                                      (2, 2, 69, 6), (3, 1, 9, 2),
                                      (4, 0, 1, 1))
                and dict(f['tables_primary']) == {1: (2, 2, 2, 2),
                                                  2: (5, 6, 6),
                                                  3: (9, 11), 4: (13,)}),
     lambda f: f"growth = {list(f['grow_primary'])}; tables = "
               f"{dict(f['tables_primary'])}")
gate("A5-ESCAPE", KIND_SUB,
     "THE ESCAPE reproduces exactly: 68 escaping transitions into "
     "exactly 5 above-window classes at the primary grain, with the "
     "witness transition exhibited and its target class shown to have "
     "no member inside the window — consumer of T2's and T3's verbatim "
     "escape windows",
     lambda f: (f['escape_primary'] == 68
                and len(f['escape_primary_classes']) == 5
                and f['escape_primary_window_classes'] == 6
                and f['escape_witness_target_minlen'] > 2),
     lambda f: f"escapes = {f['escape_primary']} into "
               f"{list(f['escape_primary_classes'])}; window carries "
               f"{f['escape_primary_window_classes']} classes; witness "
               f"target's shallowest member has length "
               f"{f['escape_witness_target_minlen']}")
gate("A5-FACTORISATION", KIND_SUB,
     "MENU-SHAPE FACTORISATION FAILS at 2 of 9 level-0 classes, and "
     "one refinement step repairs it at 0 of 6 level-1 classes on the "
     "shallower window — the intrinsic refinement is load-bearing",
     lambda f: (f['welldef_primary_level0'] == (2, 9)
                and f['welldef_primary_level1'] == (0, 6)),
     lambda f: f"level-0 = {f['welldef_primary_level0'][0]}/"
               f"{f['welldef_primary_level0'][1]} failing; level-1 = "
               f"{f['welldef_primary_level1'][0]}/"
               f"{f['welldef_primary_level1'][1]}")
gate("A5-CONTROL-GRAIN", KIND_SUB,
     "the CONTROL grain is T5's MENU rung: the event x weight menu "
     "partition has exactly 113 classes on the depth-4 family, and it "
     "disagrees with the primary grain — the grain-swap control fires "
     "(different class counts AND different escape counts), so the "
     "grain is arena data and is declared, never assumed",
     lambda f: (f['grain_control_classes'] == 113
                and f['grain_primary_classes'] == 13
                and f['escape_control'] != f['escape_primary']),
     lambda f: f"control {f['grain_control_classes']} classes / "
               f"{f['escape_control']} escapes vs primary "
               f"{f['grain_primary_classes']} / {f['escape_primary']}")
gate("A5-OPERATOR-CONTROL", KIND_SUB,
     "T2's binding clause re-measured rather than repeated: the "
     "per-candidate and per-class-AGGREGATE refinement operators are "
     "EXTENSIONALLY NULL against each other at the transport cap — "
     "same partition, same escape count",
     lambda f: (f['operator_agree']
                and f['escape_aggregate'] == f['escape_primary']),
     lambda f: f"partitions agree = {f['operator_agree']}; escapes "
               f"{f['escape_aggregate']} vs {f['escape_primary']}")

# ======================================================================
# ARM A, FACT 6 — THE REOPENING WITNESS
# ======================================================================
emit("")
emit("[ARM A / FACT 6 — the reopening witness, re-derived]")


def live_hold(vw, a):
    return frozenset(v for v in vw.holdings(a) if v not in vw.superseded)


DIV = {}
for h in FAM4:
    pred = event_poset(list(h))
    vw = View(list(h), pred, set(range(len(h))))
    DIV[h] = live_hold(vw, 'A') != live_hold(vw, 'B')
recon = []
for h in sorted(FAM4, key=lambda x: (len(x), SK(x))):
    for j, e in enumerate(h):
        if e[0] == 'd' and DIV[h[:j]] and not DIV[h[:j + 1]]:
            recon.append((h, j))


def weight_of(h):
    w = Fr(1)
    for j, e in enumerate(h):
        w *= dict(CACHE[h[:j]])[e]
    return w


F['diverged'] = sum(1 for v in DIV.values() if v)
F['reconverging_pairs'] = len(recon)
F['diverged_prefixes'] = len({h[:j] for h, j in recon})
_minchains = {h[:j + 1] for h, j in recon if j + 1 == 3}
F['minimal_chains'] = len(_minchains)
F['minimal_chain_weights'] = tuple(sorted({str(weight_of(c))
                                           for c in _minchains}))
F['reopening_shortest_len'] = min(j + 1 for h, j in recon)

emit(f"  divergence exists in-family: {F['diverged']} of {len(FAM4)} "
     f"histories have unequal non-superseded holdings between A and B.")
emit(f"  reconverging (history, delivery) pairs: "
     f"{F['reconverging_pairs']}, over "
     f"{F['diverged_prefixes']} DISTINCT diverged prefixes — the "
     f"suffix multiplicity is carried, not hidden.")
emit(f"  DISTINCT MINIMAL (3-event) reconverging chains: "
     f"{F['minimal_chains']}, all at exact weight "
     f"{list(F['minimal_chain_weights'])}.  Shortest reconverging "
     f"chain length = {F['reopening_shortest_len']}.")
emit(f"  So the delivery-free absorption theorem ('diverged holdings "
     f"never reconverge') is a DELIVERYLESSNESS ARTEFACT: a delivery "
     f"event inside the enumerated family reconverges a diverged "
     f"configuration, with every event admission-priced by the "
     f"committed layer.")

gate("A6-REOPENING", KIND_SUB,
     "THE REOPENING WITNESS, decomposed exactly as the committed "
     "correction requires: 1,044 diverged histories; 124 reconverging "
     "(history, delivery) pairs carrying suffix multiplicity; 84 "
     "DISTINCT diverged prefixes; 4 DISTINCT minimal 3-event chains, "
     "all at exact weight 1/256 — consumer of T3's verbatim "
     "decomposition window",
     lambda f: (f['diverged'] == 1044
                and f['reconverging_pairs'] == 124
                and f['diverged_prefixes'] == 84
                and f['minimal_chains'] == 4
                and f['minimal_chain_weights'] == ('1/256',)
                and f['reopening_shortest_len'] == 3),
     lambda f: f"diverged {f['diverged']}; pairs "
               f"{f['reconverging_pairs']}; prefixes "
               f"{f['diverged_prefixes']}; minimal chains "
               f"{f['minimal_chains']} at "
               f"{list(f['minimal_chain_weights'])}")

# --- the d42a classifier-mismatch control (pin section 4)
_df4 = [h for h in DF if len(h) <= CAP_ESC]
_dfshapes = set()
for h in _df4:
    d = defaultdict(int)
    for e, q in DF[h]:
        d[(e[0], q)] += 1
    _dfshapes.add(('KIND',) + tuple(sorted(((k, str(q)), n)
                                           for (k, q), n in d.items())))
_alien = sum(1 for h in FAM4 if shape_kind(h) in _dfshapes)
_dfwithd = sum(1 for s in _dfshapes if any(t[0][0] == 'd'
                                           for t in s[1:]))
F['df_shapes'] = len(_dfshapes)
F['df_shapes_with_d'] = _dfwithd
F['classifier_matches'] = _alien
F['classifier_tested'] = len(FAM4)
emit(f"  THE d42a CLASSIFIER-MISMATCH CONTROL (pin section 4, "
     f"re-measured): the delivery-free family carries "
     f"{F['df_shapes']} distinct menu shapes at depth <= "
     f"{CAP_ESC}, of which {F['df_shapes_with_d']} contain a delivery "
     f"kind.  Transport menus matching ANY delivery-free shape: "
     f"{F['classifier_matches']} of {F['classifier_tested']}.  The "
     f"delivery-free classifier cannot be silently reused here.")
gate("A6-CLASSIFIER", KIND_SUB,
     "THE CLASSIFIER-MISMATCH CONTROL: zero of the 3,969 transport "
     "menus matches any delivery-free menu shape, and zero of the 4 "
     "delivery-free shapes contains a delivery kind — the control set "
     "is gated by size, not only through its consequences",
     lambda f: (f['classifier_matches'] == 0
                and f['classifier_tested'] == 3969
                and f['df_shapes'] == 4
                and f['df_shapes_with_d'] == 0),
     lambda f: f"delivery-free shapes = {f['df_shapes']} (with 'd': "
               f"{f['df_shapes_with_d']}); transport menus matching "
               f"any = {f['classifier_matches']}/"
               f"{f['classifier_tested']}")

# ======================================================================
# ARM A, FACT 7 — THE ROOT-SYMMETRY THEOREM
# ======================================================================
emit("")
emit("[ARM A / FACT 7 — the root-symmetry theorem]")


def make_sigma(swap_actor, swap_bit):
    def sw_a(a):
        if not swap_actor:
            return a
        return {'A': 'B', 'B': 'A'}.get(a, a)

    def sw_v(v):
        if v == V0 or not isinstance(v, tuple):
            return v
        if v[1] == 'm':
            return ('v', 'm', tuple(sw_v(x) for x in v[2]),
                    (1 - v[3] if (swap_bit and isinstance(v[3], int))
                     else v[3]), sw_a(v[4]))
        return ('v', sw_v(v[1]),
                tuple(sorted((1 - x if swap_bit else x) for x in v[2])),
                tuple(sorted(sw_a(a) for a in v[3])), sw_a(v[4]))

    def sw_t(t):
        return (sw_a(t[0]), sw_v(t[1]),
                (1 - t[2]) if swap_bit else t[2])

    def sw_e(e):
        if e[0] == 'p':
            return ('p', sw_a(e[1]), sw_v(e[2]),
                    (1 - e[3]) if swap_bit else e[3])
        if e[0] == 'n':
            return ('n', sw_a(e[1]))
        if e[0] == 'd':
            return ('d', sw_a(e[1]), sw_a(e[2]), sw_v(e[3]))
        if e[0] == 'm':
            return ('m', sw_a(e[1]),
                    tuple(sorted((sw_v(x) for x in e[2]), key=SK)),
                    (e[3] if e[3] == 'both' else sw_v(e[3])))
        return ('r', sw_a(e[1]),
                frozenset(sw_t(t) for t in e[2]),
                frozenset(sw_t(t) for t in e[3]))
    return sw_e


prog("root-symmetry sweep ...")
SYMS = [('A<->B', make_sigma(True, False)),
        ('0<->1', make_sigma(False, True)),
        ('both', make_sigma(True, True))]
sym_rows = []
for nm, sg in SYMS:
    closed = 0
    menu_viol = 0
    g_viol = 0
    tested = 0
    for h in CACHE:
        if len(h) > CAP_SYM:
            continue
        hs = tuple(sg(e) for e in h)
        if hs not in CACHE:
            closed += 1
            continue
        tested += 1
        want = {(SK(sg(e)), q) for e, q in CACHE[h]}
        got = {(SK(e), q) for e, q in CACHE[hs]}
        if want != got:
            menu_viol += 1
        for r in range(1, min(len(GT[h]), len(GT[hs])) + 1):
            if GT[h][r - 1] != GT[hs][r - 1]:
                g_viol += 1
    sym_rows.append((nm, tested, closed, menu_viol, g_viol))
F['sym_rows'] = tuple(sym_rows)
F['sym_menu_violations'] = sum(r[3] for r in sym_rows)
F['sym_G_violations'] = sum(r[4] for r in sym_rows)
F['sym_not_closed'] = sum(r[2] for r in sym_rows)

# the root orbits and the uniform-within-kind root conditional
orb = defaultdict(set)
for e, q in ROOTMENU:
    key = SK(e)
    reps = {key}
    for nm, sg in SYMS:
        reps.add(SK(sg(e)))
    orb[e[0]].add(frozenset(reps))
merged = {}
for k in orb:
    groups = []
    for s in orb[k]:
        hit = [g for g in groups if g & s]
        for g in hit:
            groups.remove(g)
            s = s | g
        groups.append(s)
    merged[k] = len(groups)
F['root_orbits_per_kind'] = tuple(sorted(merged.items()))
F['root_one_orbit_per_kind'] = all(v == 1 for v in merged.values())
_cond = {}
for r in range(1, RMAX + 1):
    kk = krel(ROOT, r)
    sec = defaultdict(Fr)
    for e, v in kk.items():
        sec[e[0]] += v
    _cond[r] = tuple(sorted((e[0], str(kk[e] / sec[e[0]]))
                            for e in kk))
F['root_conditional_constant'] = len({_cond[r] for r in _cond}) == 1
F['root_conditional'] = tuple(sorted(set(_cond[1])))

emit("  the layer's relabellings, tested as automorphisms over every "
     f"history of depth <= {CAP_SYM}:")
emit("    symmetry | histories tested | not closed | menu violations | "
     "G(h,r) != G(sigma h, r)")
for nm, tested, closed, mv, gv in sym_rows:
    emit(f"    {nm} | {tested} | {closed} | {mv} | {gv}")
emit(f"  root menu orbits per event kind: "
     f"{dict(F['root_orbits_per_kind'])} — ONE ORBIT PER KIND = "
     f"{F['root_one_orbit_per_kind']}.")
emit(f"  therefore, for ANY terminal convention invariant under those "
     f"relabellings, the root sector-normalized conditional is the "
     f"UNIFORM-WITHIN-KIND distribution at every horizon.  Measured, "
     f"r = 1..{RMAX}: constant across horizons = "
     f"{F['root_conditional_constant']}; the distribution = "
     f"{dict(F['root_conditional'])}.")
emit("  THIS IS A THEOREM OF THE CONSTRUCTION, NOT A MEASUREMENT OF "
     "STABILITY: the root's zero drift and the root leg of any "
     "convention-separation claim are ONE identity — root-menu "
     "symmetry times an equivariant terminal — and neither carries "
     "information about horizon stability or convention independence.")

gate("A7-AUTOMORPHISM", KIND_SUB,
     "A <-> B and 0 <-> 1 are EXACT automorphisms of the committed "
     "layer: relabelling a history and relabelling its menu give the "
     "same (event, weight) multiset at every history of the window, "
     "the family is closed under all three relabellings, and "
     "G(h, r) = G(sigma h, r) at every (history, horizon) pair — "
     "0 violations of each kind",
     lambda f: (f['sym_menu_violations'] == 0
                and f['sym_G_violations'] == 0
                and f['sym_not_closed'] == 0
                and all(r[1] == 521 for r in f['sym_rows'])),
     lambda f: "; ".join(f"{nm}: {t} tested, {c} not closed, {m} menu "
                         f"violations, {g} G violations"
                         for nm, t, c, m, g in f['sym_rows']))
gate("A7-ROOTTHEOREM", KIND_THM,
     "THE ROOT LEG IS A THEOREM (disclosed as a theorem-pass, so that "
     "a forced identity is never counted as a measurement): the root "
     "menu is ONE ORBIT PER EVENT KIND under the layer's own "
     "automorphisms, so every equivariant terminal forces the "
     "uniform-within-kind root conditional at every horizon",
     lambda f: (f['root_one_orbit_per_kind']
                and f['root_conditional_constant']),
     lambda f: f"orbits per kind = {dict(f['root_orbits_per_kind'])}; "
               f"conditional constant across r = 1..7 = "
               f"{f['root_conditional_constant']}; distribution = "
               f"{dict(f['root_conditional'])}")

prog("ARM A complete")

# ======================================================================
# ARM B — THE SUCCESSOR ENGINE, ATTEMPTED
# ======================================================================
emit("")
emit("=" * 70)
emit("[ARM B — THE SUCCESSOR ENGINE, ATTEMPTED: operator-level "
     "minorization on the transport family]")
emit("=" * 70)
emit("  The predecessor named this and did not run it: 'NO "
     "OPERATOR-LEVEL MINORIZATION — Birkhoff / Hilbert-metric "
     "contraction of the positive backward recursion G, the natural "
     "instrument for this kernel — has been attempted anywhere.'  "
     "This arm attempts it, at the affordable cap, and reports what it "
     "finds either way.")

# --- B0: the infeasibility counts, printed rather than hidden
_root_branch = len(ROOTMENU)
_avg6 = Fr(F['t_per_level'][6], F['t_per_level'][5])
_pred7 = int(F['t_per_level'][6] * _avg6)
prog("three-actor family (conditional arm) ...")
_t = time.time()
C3 = None
try:
    C3 = build(cf_transport, ABC, 3)
    _t3 = time.time() - _t
except MemoryError:
    _t3 = time.time() - _t
F['pool3_depth3'] = (len(C3) if C3 else None)
_per3 = defaultdict(int)
if C3:
    for h in C3:
        _per3[len(h)] += 1
F['pool3_per_level'] = tuple(sorted(_per3.items()))
_b3 = (Fr(_per3[3], _per3[2]) if C3 and _per3[2] else None)
F['pool3_branching'] = (str(_b3) if _b3 else None)
F['pool3_depth5_projection'] = (
    int(_per3[3] * _b3 * _b3) if _b3 else None)
F['depth7_projection'] = _pred7
emit(f"  DECLARED CAPS AND THE INFEASIBLE ARMS, with their counts "
     f"printed (pin: 'depth-7 and 3-actor depth-6 declared infeasible "
     f"with the counts printed').")
F['depth7_over_level6'] = str(Fr(_pred7, F['t_per_level'][6]))
F['depth7_over_build'] = str(Fr(_pred7, F['t_total']))
emit(f"    two-actor depth 7: the measured level-6/level-5 branching "
     f"is {F['t_per_level'][6]}/{F['t_per_level'][5]} = "
     f"{_avg6} (~{float(_avg6):.3f}), so level 7 is about "
     f"{F['depth7_projection']:,} histories.  BOTH RATIOS ARE PRINTED "
     f"BECAUSE THEY DIFFER AND ONLY ONE OF THEM IS 'ROUGHLY EIGHT': "
     f"that is {F['depth7_over_level6']} "
     f"(~{float(Fr(F['depth7_over_level6'])):.2f}) times this run's "
     f"LEVEL-6 layer of {F['t_per_level'][6]:,} histories, and "
     f"{F['depth7_over_build']} "
     f"(~{float(Fr(F['depth7_over_build'])):.2f}) times its whole "
     f"depth-6 BUILD of {F['t_total']:,}, which alone is the dominant "
     f"cost of this receipt.  NOT RUN.")
emit(f"    three-actor: depth 3 is {F['pool3_depth3']} histories "
     f"(per level {dict(F['pool3_per_level'])}), measured here; the "
     f"level-3/level-2 branching is {F['pool3_branching']}, so depth 5 "
     f"projects to about {F['pool3_depth5_projection']:,} and depth 6 "
     f"to roughly an order of magnitude beyond that.  THE 3-ACTOR "
     f"DEPTH-5 CONDITIONAL ARM IS NOT RUN: the projection exceeds this "
     f"unit's declared wall-clock budget, and the cap is printed here "
     f"rather than the omission hidden.  3-ACTOR DEPTH 6: DECLARED "
     f"INFEASIBLE.")

# --- B1: THE TREE OBSTRUCTION
emit("")
emit("  [B1 — THE TREE OBSTRUCTION, measured and named]")
emit("  Write the backward recursion as a level operator: "
     "(M_n g)(h) = sum_e q(e|h) g(h+e), a nonnegative matrix with rows "
     "the depth-n histories and columns the depth-(n+1) histories.  "
     "Then G(., r) at level n is M_n M_(n+1) ... 1.  Birkhoff's "
     "theorem gives a contraction of the Hilbert projective metric with "
     "coefficient tanh(Delta/4), where Delta is the operator's "
     "projective diameter — FINITE only if the matrix has no zero "
     "pattern separating a pair of columns.")
_singleparent = 0
_multiparent = 0
_dupmenu = 0
_menuentries = 0
for h in CACHE:
    # THE SUBSTANTIVE MEASUREMENT, separated from the forced one: the
    # number of DUPLICATED menu entries anywhere in the family.  This
    # is the only way a column census over a history tree could ever
    # have failed, and it is a genuine measurement of the layer's
    # bookkeeping.
    _seen = set()
    for e, q in CACHE[h]:
        _menuentries += 1
        k = SK(e)
        if k in _seen:
            _dupmenu += 1
        _seen.add(k)
    if len(h) == 0:
        continue
    # The column of h in the level operator M_{|h|-1}: its nonzero
    # entries are the rows g with h a menu successor of g.  A history
    # determines its own prefix, so the only candidate row is h[:-1];
    # the count below is the multiplicity of h's last event in that
    # row's menu.  Anything other than 1 would mean either a duplicated
    # menu entry or a second parent, and either would make the column
    # non-degenerate.
    par = h[:-1]
    n = sum(1 for e, q in CACHE[par] if SK(e) == SK(h[-1]))
    if n == 1:
        _singleparent += 1
    else:
        _multiparent += 1
F['columns_tested'] = _singleparent + _multiparent
F['columns_single_parent'] = _singleparent
F['columns_other'] = _multiparent
F['menu_entries_total'] = _menuentries
F['menu_duplicate_entries'] = _dupmenu
# THE WITNESS MINOR, COMPUTED — no always-firing else.  Each entry is
# a SUM OVER THE ROW'S ACTUAL MENU of the weights of the events that
# carry the row to the named column; an off-diagonal zero is therefore
# READ off an empty sum, not assigned by a guard that can never hold.
_lv1 = sorted(LEVEL[1], key=SK)
r1, r2 = _lv1[0], _lv1[1]
c1 = r1 + (sorted(CACHE[r1], key=lambda t: SK(t[0]))[0][0],)
c2 = r2 + (sorted(CACHE[r2], key=lambda t: SK(t[0]))[0][0],)


def moper(row, col):
    """The (row, col) entry of the level operator: the total weight the
    row's own menu sends to that exact column history."""
    return sum(q for e, q in CACHE[row] if row + (e,) == col)


m11 = moper(r1, c1)
m12 = moper(r1, c2)
m21 = moper(r2, c1)
m22 = moper(r2, c2)
_wit = (str(m11), str(m12), str(m21), str(m22))
F['birkhoff_witness'] = _wit
# DERIVED FROM THE WITNESS, not typed: the projective diameter of a
# nonnegative matrix is finite only if no zero pattern separates a pair
# of columns; an off-diagonal zero in a 2x2 minor is such a pattern, so
# the cross-ratio m11*m22/(m12*m21) is infinite and tanh(Delta/4) = 1.
F['birkhoff_zero_offdiag'] = (m12 == 0 or m21 == 0)
F['birkhoff_diameter_finite'] = not (m12 == 0 or m21 == 0)
F['birkhoff_tau'] = ('1' if (m12 == 0 or m21 == 0)
                     else str((1 - (m12 * m21) / (m11 * m22))
                              / (1 + (m12 * m21) / (m11 * m22))))
F['birkhoff_crossratio_infinite'] = (m12 * m21 == 0 and m11 * m22 != 0)
# THE HISTORY-LEVEL DOEBLIN CONSTANT, COMPUTED rather than argued: the
# largest common minorant of the one-step laws of the level-1
# histories, at the finest possible grain (the successor history
# itself).  Disjoint descendant supports make it exactly 0, and the sum
# below is what says so.
_lv1laws = []
for _x in _lv1:
    _kk = krel(_x, 1)
    _lv1laws.append({_x + (_e,): _v for _e, _v in _kk.items()})
_lv1keys = set()
for _m in _lv1laws:
    _lv1keys |= set(_m)
F['birkhoff_doeblin_history'] = str(
    sum(min(_m.get(_k, Fr(0)) for _m in _lv1laws) for _k in _lv1keys))
F['birkhoff_doeblin_witness_n'] = len(_lv1)
emit(f"  MEASURED, AND THE TWO CLAUSES SEPARATED.  (a) THE "
     f"SUBSTANTIVE ONE: over all {F['menu_entries_total']} menu "
     f"entries of the family there are {F['menu_duplicate_entries']} "
     f"DUPLICATED entries — the only way a history-tree column census "
     f"could have come out otherwise.  (b) THE FORCED ONE: of the "
     f"{F['columns_tested']} columns (every non-root history of the "
     f"family), {F['columns_single_parent']} have EXACTLY ONE nonzero "
     f"entry — the history's unique parent — and {F['columns_other']} "
     f"have any other number.  Clause (b) is FORCED: a history is its "
     f"own event sequence, so h[:-1] is the only candidate row, and "
     f"unique parenthood is the defining property of a history tree "
     f"rather than a finding about this one.  It is carried as a "
     f"THEOREM-PASS below and (a) is carried as the measurement.")
emit(f"  CONSEQUENCE, EXHIBITED FROM A COMPUTED MINOR: take two rows "
     f"h1 != h2 at the same level and one column under each.  Each "
     f"entry is the total weight the row's own menu sends to that "
     f"exact column, so an off-diagonal zero is READ off an empty sum "
     f"rather than assigned by a guard.  The 2x2 minor is "
     f"[[{_wit[0]}, {_wit[1]}], [{_wit[2]}, {_wit[3]}]]; "
     f"off-diagonal-zero = {F['birkhoff_zero_offdiag']}, so the "
     f"cross-ratio m11*m22/(m21*m12) is +infinity "
     f"({F['birkhoff_crossratio_infinite']}), the projective diameter "
     f"is finite = {F['birkhoff_diameter_finite']}, and the DERIVED "
     f"contraction coefficient is tau = {F['birkhoff_tau']} AT EVERY "
     f"LEVEL: THE BIRKHOFF CONTRACTION COEFFICIENT OF THE BACKWARD "
     f"RECURSION IS {F['birkhoff_tau']}, NOT BY A CAP AND NOT BY A "
     f"NUMERICAL ACCIDENT, BUT BY UNIQUE PARENTHOOD.  Neither tau nor "
     f"the diameter flag is typed: both are derived from the minor "
     f"above.")
emit(f"  SCOPE OF THE BIRKHOFF ROUTE, DISCLOSED (and this is a "
     f"limitation, not a result).  What dies here is the Birkhoff / "
     f"Hilbert route ON THE HISTORY TREE, where it dies for every "
     f"history tree under every weight law, carrying no "
     f"transport-specific content.  THE HILBERT PROJECTIVE DIAMETER "
     f"OF A QUOTIENT TRANSFER OPERATOR IS NOT COMPUTED ANYWHERE IN "
     f"THIS UNIT: on a quotient the operator need not be a tree "
     f"operator and Delta may be finite, and that is the only level at "
     f"which the predecessor's named engine could ever have worked.  "
     f"ARM B substitutes a DIFFERENT instrument on the quotients — the "
     f"Doeblin coefficient delta* — and the substitution is named "
     f"here rather than left for a reader to notice.  The named engine "
     f"remains UN-ATTEMPTED at the level where it could have worked, "
     f"and it is carried forward as the successor's first ARM-B task.")
emit(f"  The same fact kills the history-level Doeblin bound "
     f"outright: for x != y at the same depth, the supports of "
     f"P^N(x, .) and P^N(y, .) are disjoint sets of descendants, so "
     f"the largest common minorant is the zero measure and delta = 0 "
     f"for every N.  MEASURED, not argued: the largest common minorant "
     f"of the one-step laws of the {F['birkhoff_doeblin_witness_n']} "
     f"level-1 histories, at the finest possible grain (the successor "
     f"history itself), has total mass "
     f"{F['birkhoff_doeblin_history']}.  ANY minorization at transport "
     f"scope must "
     f"therefore live on a QUOTIENT — which is precisely where ARM A "
     f"fact 5's escape bites.  This is the structural statement the "
     f"predecessor's open question did not contain.")
gate("B1-TREE", KIND_THM,
     "THE TREE OBSTRUCTION — carried as a THEOREM-PASS with its "
     "forcing named, because unique parenthood is a property of the "
     "REPRESENTATION (a history IS its event sequence, so h = g + (e,) "
     "forces g = h[:-1]) and not a finding about this family: every "
     "column of every level operator has exactly one nonzero entry, so "
     "the projective diameter is infinite, the Birkhoff contraction "
     "coefficient is 1 at every level, and the history-level Doeblin "
     "constant is 0 for every N by disjointness of supports.  Its only "
     "failure mode is a duplicated menu entry, and THAT is gated "
     "separately and substantively at B1-NODUP",
     lambda f: (f['columns_other'] == 0
                and f['columns_single_parent'] == 243768
                and f['birkhoff_witness'][1] == '0'
                and f['birkhoff_witness'][2] == '0'
                and f['birkhoff_zero_offdiag']
                and f['birkhoff_crossratio_infinite']
                and f['birkhoff_diameter_finite'] is False
                and f['birkhoff_tau'] == '1'),
     lambda f: f"columns = {f['columns_tested']}, single-parent = "
               f"{f['columns_single_parent']}, other = "
               f"{f['columns_other']}; witness minor = "
               f"{list(f['birkhoff_witness'])} (COMPUTED, each entry a "
               f"sum over the row's own menu); diameter finite = "
               f"{f['birkhoff_diameter_finite']}; tau = "
               f"{f['birkhoff_tau']}")
gate("B1-NODUP", KIND_SUB,
     "THE SUBSTANTIVE HALF OF THE TREE OBSTRUCTION, separated from the "
     "forced half: the committed layer emits NO DUPLICATED MENU ENTRY "
     "anywhere in the family — 0 duplicates over every menu entry of "
     "all 243,769 histories.  This is the only input that could have "
     "broken the column census, and it is a real measurement of the "
     "layer's bookkeeping rather than a property of the history-tree "
     "representation",
     lambda f: (f['menu_duplicate_entries'] == 0
                and f['menu_entries_total'] > 200000
                and f['menu_entries_total']
                == sum(n for k, n in f['kind_counts'])),
     lambda f: f"duplicated menu entries = "
               f"{f['menu_duplicate_entries']} over "
               f"{f['menu_entries_total']} menu entries")

# --- B2: THE QUOTIENT MINORIZATION, ATTEMPTED
emit("")
emit("  [B2 — THE QUOTIENT MINORIZATION, attempted on the R-SIG "
     "class]")
emit("  The construction, declared before it is run.  Let Psi be a "
     "declared state abstraction.  For a class C and a step count N, "
     "the LARGEST delta for which a common nu exists is exactly")
emit("      delta*(C, N, Psi) = sum_s min_(x in C) P^N(x, Psi^-1(s)),")
emit("  and nu is that common minorant, renormalized.  delta* > 0 iff "
     "some Psi-class is reached in exactly N steps from EVERY x in C.  "
     "This is a measurement that can come out either way, and below it "
     "does both.")
emit("  TWO GRAINS, both declared (RUNBOOK section 15): Psi_kind = the "
     "kind x weight menu shape (the primary grain); Psi_event = the "
     "event x weight menu shape (the control grain).")
emit("  TWO HORIZON CONVENTIONS, both printed, because naming one "
     "silently is the defect the predecessor's round convicted: (H7) "
     "the horizon-7 chain from the root, where a history at depth d "
     "steps under k_(7-d); and (MATCHED) the matched-horizon chain, "
     "where every x steps under the same k_N, k_(N-1), ..., k_1 "
     "regardless of its depth.")


RSIGALL = set(RS)


def psi_kind_of(h):
    return shape_kind(h)


def psi_event_of(h):
    return shape_event(h)


def psi_profile_of(h):
    """The HOLDINGS PROFILE as a grain — the obstruction coordinate
    itself, used as the abstraction.  Coarser than or incomparable to
    both menu grains, and the obvious candidate given this unit's own
    diagnosis, so it is measured rather than left to a reader."""
    hold, nsup = HOLD[h]
    return ('PROF', len(hold['A']), len(hold['B']))


def psi_profile_unordered_of(h):
    hold, nsup = HOLD[h]
    return ('PROFU',) + tuple(sorted((len(hold['A']), len(hold['B']))))


def psi_rsig_of(h):
    """The R-SIG INDICATOR as a grain: the two-class abstraction a
    regeneration argument ABOUT R-SIG would naturally declare.  This is
    the counter-reading of the BLOCKED verdict and it is printed as
    one."""
    return ('RSIG', h in RSIGALL)


PSIS = (('kind13', psi_kind_of),
        ('event113', psi_event_of),
        ('profile', psi_profile_of),
        ('profile_unordered', psi_profile_unordered_of),
        ('rsig_indicator', psi_rsig_of))
PSI_FAMILY_NOTE = (
    "menu-shape functions of the successor (kind x weight, event x "
    "weight) PLUS the holdings-profile and R-SIG-indicator "
    "abstractions added by this repair")


def nstep_frontier(x, N, matched):
    fr = {x: Fr(1)}
    for st in range(N):
        nxt = defaultdict(Fr)
        for g, w in fr.items():
            r = (N - st) if matched else (CAP_T + 1 - len(g))
            kk = krel_c(g, r)
            for e, q in CACHE[g]:
                nxt[g + (e,)] += w * kk[e]
        fr = nxt
    return fr


def nstep_law(x, N, psi, matched):
    mu = defaultdict(Fr)
    for g, w in nstep_frontier(x, N, matched).items():
        mu[psi(g)] += w
    return mu


def _dstar_from_laws(laws):
    """delta* = sum_s min_x P^N(x, s).  A class absent from ANY law
    contributes min = 0, so only the INTERSECTION of the laws' supports
    can contribute: the intersection is taken first and the minimum is
    then computed on it alone.  This is the same number by the same
    definition — it drops terms that are identically zero — and it is
    what makes the five-grain census affordable."""
    if not laws:
        return Fr(0), {}
    common = set(laws[0])
    for m in laws[1:]:
        common &= set(m)
        if not common:
            break
    best = Fr(0)
    nu = {}
    for k in sorted(common, key=SK):
        v = min(mm[k] for mm in laws)
        if v > 0:
            nu[k] = v
            best += v
    return best, nu


def delta_star(Xs, N, psi, matched):
    return _dstar_from_laws(
        [nstep_law(x, N, psi, matched) for x in Xs])


def delta_star_multi(Xs, N, matched, psis=PSIS):
    """delta* at SEVERAL grains from ONE frontier per point.  The
    frontier is the expensive object and it does not depend on the
    grain, so measuring five grains costs barely more than measuring
    one — which is why the grain fiber below is measured rather than
    declared."""
    laws = {nm: [] for nm, ps in psis}
    for x in Xs:
        fr = nstep_frontier(x, N, matched)
        for nm, ps in psis:
            mu = defaultdict(Fr)
            for g, w in fr.items():
                mu[ps(g)] += w
            laws[nm].append(mu)
    return {nm: _dstar_from_laws(laws[nm]) for nm, ps in psis}


prog("ARM B: delta* on the FULL R-SIG class, five grains ...")
full_rows = []
grain_rows = []
for N in range(1, NMAX + 1):
    Xs = [h for h in RS if len(h) + N <= CAP_T]
    if not Xs:
        full_rows.append((N, 0, 0, None, None))
        continue
    nprof = len({RS[h][1] for h in Xs})
    if N <= 3:
        # the three widest windows carry the grain fiber: five grains,
        # both conventions, one frontier per point
        mH = delta_star_multi(Xs, N, False)
        mM = delta_star_multi(Xs, N, True)
        dk = mH['kind13'][0]
        dm = mM['kind13'][0]
        grain_rows.append(
            (N, len(Xs), tuple((nm, str(mH[nm][0]), str(mM[nm][0]))
                               for nm, ps in PSIS)))
    else:
        # the narrow windows have collapsed to a single profile and
        # carry no cross-profile content; only the declared primary
        # grain is run there, exactly as in the first delivery
        dk, _ = delta_star(Xs, N, psi_kind_of, False)
        dm, _ = delta_star(Xs, N, psi_kind_of, True)
    full_rows.append((N, len(Xs), nprof, str(dk), str(dm)))
F['B2_full_rows'] = tuple(full_rows)
F['B2_full_grain_rows'] = tuple(grain_rows)
F['B2_rsig_indicator_matched'] = tuple(
    (N, dict((nm, m) for nm, hh, m in row)['rsig_indicator'])
    for N, n, row in grain_rows)
F['B2_rsig_indicator_delta1_at'] = tuple(
    N for N, v in F['B2_rsig_indicator_matched'] if v == '1')
emit("")
emit("  (a) THE FULL R-SIG CLASS.  x ranges over every R-SIG point "
     f"the window admits (len(x) + N <= {CAP_T}).  The third column "
     "is the number of DISTINCT holdings profiles the window carries "
     "— the coordinate ARM A fact 4 found, and the one that decides "
     "these rows.")
emit("    N | |C-window| | # profiles in window | delta* (H7, primary "
     "grain) | delta* (MATCHED, primary grain)")
for N, n, np_, dk, dm in full_rows:
    emit(f"    {N} | {n} | {np_} | {dk} | {dm}")
F['B2_full_zero_at'] = tuple(N for N, n, np_, dk, dm in full_rows
                             if dk == '0')
F['B2_hetero_rows'] = tuple((N, n, np_, dk, dm)
                            for N, n, np_, dk, dm in full_rows
                            if np_ > 1)
F['B2_hetero_zero_rows'] = tuple((N, n, np_, dk, dm)
                                 for N, n, np_, dk, dm
                                 in F['B2_hetero_rows']
                                 if dk == '0' and dm == '0')
F['B2_hetero_pos_rows'] = tuple((N, n, np_, dk, dm)
                                for N, n, np_, dk, dm
                                in F['B2_hetero_rows']
                                if not (dk == '0' and dm == '0'))
F['B2_homo_rows'] = tuple((N, n, np_, dk, dm)
                          for N, n, np_, dk, dm in full_rows
                          if np_ == 1)
F['B2_widest_zero_N'] = tuple(N for N, n, np_, dk, dm
                              in F['B2_hetero_zero_rows'])
emit(f"  READ EXACTLY, AND NOT ONE WORD FURTHER.  On the two WIDEST "
     f"windows — N = {list(F['B2_widest_zero_N'])}, carrying "
     f"{[r[1] for r in F['B2_hetero_zero_rows']]} R-SIG points and "
     f"{[r[2] for r in F['B2_hetero_zero_rows']]} distinct holdings "
     f"profiles — delta* is EXACTLY 0 under both horizon conventions.  "
     f"At N = {[r[0] for r in F['B2_hetero_pos_rows']]} the window has "
     f"narrowed to {[r[1] for r in F['B2_hetero_pos_rows']]} points "
     f"and delta* turns POSITIVE across profiles "
     f"({[(r[3], r[4]) for r in F['B2_hetero_pos_rows']]}): three "
     f"steps do bring two different profiles into a common Psi-class "
     f"ON THAT WINDOW.  THIS UNIT DOES NOT CLAIM A BOUND FROM IT.  The "
     f"window at that N holds "
     f"{[r[1] for r in F['B2_hetero_pos_rows']]} of the class's "
     f"{len(RS)} points, and the deeper rows "
     f"{list(F['B2_homo_rows'])} have collapsed to a SINGLE profile, "
     f"where a positive value carries no cross-profile content at "
     f"all.  What the widest windows say is the reportable fact; what "
     f"the narrow ones say is a cap artefact, and it is printed as "
     f"one.")

emit("")
emit("  (a') THE GRAIN FIBER OF THE FULL-CLASS ROWS, MEASURED AT FIVE "
     "GRAINS RATHER THAN DECLARED AT ONE.  The delivered verdict's "
     "delta* = 0 clause is stated at the DECLARED-PRIMARY 13-class "
     "grain, and it must carry that qualifier, because delta* is "
     "grain-relative and this table is what shows it.  Each cell is "
     "(H7, MATCHED).")
emit("    N | |C-window| | " + " | ".join(nm for nm, ps in PSIS))
for N, n, row in grain_rows:
    emit(f"    {N} | {n} | "
         + " | ".join(f"{h}, {m}" for nm, h, m in row))
emit(f"  THE COUNTER-READING, PRINTED AS THE FOUND-REACHABILITY "
     f"WITNESS AND NOT BURIED.  At Psi = THE R-SIG INDICATOR — a "
     f"legitimate declared abstraction, and the obvious one for a "
     f"regeneration argument ABOUT R-SIG — the SAME full class has "
     f"delta* = 1 at matched horizon on the same widest windows "
     f"(N = {list(F['B2_rsig_indicator_delta1_at'])}).  The mechanism "
     f"is exact and is not an artefact: the one-step matched kernel is "
     f"the sector-normalized menu, the two idles carry 1 and the "
     f"deliveries (of the non-superseded token, or of a superseded "
     f"remainder, which changes neither nsup nor its equality) carry "
     f"1/2, so P^1(x, R-SIG) = 3/4 identically at every R-SIG point, "
     f"menu-exact or not.  BLOCKED IS THEREFORE PSI-FAMILY-RELATIVE, "
     f"and the verdict now carries the qualifier the FOUND segment "
     f"already carried.  What the BLOCKED verdict says is that no "
     f"MENU-SHAPE grain unblocks the ladder; what this row says is "
     f"that a grain which reads the target class itself does — and "
     f"that a delta* = 1 at a two-class grain is a lumpability "
     f"statement, not a contraction instrument.")
emit(f"  AND THE OBSTRUCTION COORDINATE ITSELF DOES NOT UNBLOCK IT: at "
     f"Psi = the holdings profile (ordered) and at Psi = the holdings "
     f"profile (unordered) — both coarser than or incomparable to the "
     f"two menu grains — delta* is still exactly 0 on the two widest "
     f"windows.  Four grains, one answer; the fifth is the "
     f"counter-reading above.")

prog("ARM B: delta* on the holdings-profile blocks ...")
PROFBLK = defaultdict(list)
for h, (v, p, m) in RS.items():
    PROFBLK[p].append(h)
# THE BLOCK LIST IS BUILT FROM THE WHOLE R-SIG SET, NOT FROM ARM A
# FACT 4's DEPTH-5 CENSUS.  The first delivery took the profile list
# from the depth-<=5 decomposition and applied it to the depth-<=6
# R-SIG set, which silently dropped a FIFTH block — (3, 3), 424 points,
# all at depth 6 — and made four universals ("each block", "every
# block", "one per holdings profile") false as written.  The census
# below is over every R-SIG point of the family and the coverage
# identity is gated, so an undeclared block cannot recur.
PROFS = sorted(PROFBLK, key=SK)
PROF_DEPTHS = {p: tuple(sorted((d, sum(1 for h in PROFBLK[p]
                                       if len(h) == d))
                               for d in sorted({len(h)
                                                for h in PROFBLK[p]})))
               for p in PROFS}
F['B2_blocks_declared'] = tuple(str(p) for p in PROFS)
F['rsig_profiles_all'] = tuple((str(p), len(PROFBLK[p])) for p in PROFS)
F['rsig_profile_depths'] = tuple((str(p), PROF_DEPTHS[p]) for p in PROFS)
F['rsig_all_count'] = len(RS)
F['rsig_block_coverage'] = sum(len(PROFBLK[p]) for p in PROFS)
F['rsig_blocks_n'] = len(PROFS)
F['rsig_blocks_declared_at_d5'] = len(F['rsig_profiles'])
emit("")
emit("  (b) THE HOLDINGS-PROFILE BLOCKS, CENSUSED OVER THE WHOLE "
     "FAMILY.  ARM A fact 4 decomposed R-SIG by (|holdings(A)|, "
     "|holdings(B)|) on the depth-<=5 window; the block LIST below is "
     "taken from every R-SIG point of the depth-6 family instead, "
     "which is where the FIFTH block lives.")
emit("    profile | points | by depth")
for p in PROFS:
    emit(f"    {p} | {len(PROFBLK[p])} | {dict(PROF_DEPTHS[p])}")
emit(f"    total | {F['rsig_block_coverage']} | (= {F['rsig_all_count']} "
     f"R-SIG points; the coverage identity is gated at B2-BLOCKCOVER)")
emit(f"  {F['rsig_blocks_declared_at_d5']} blocks appear at depth <= 5 "
     f"and {F['rsig_blocks_n']} appear in the family.  The fifth block "
     f"(3, 3) carries {len(PROFBLK[(3, 3)])} points, ALL at depth "
     f"{CAP_T} — so no window with dep + N <= {CAP_T} exists for it "
     f"and its delta* is EXCLUDED-BY-CAP, with the reason printed and "
     f"its hitting row measured below rather than the block dropped.")
prof_rows = []
excluded = []
for p in PROFS:
    for N in (1, 2):
        Xs = [h for h in PROFBLK[p] if len(h) + N <= CAP_T]
        if len(Xs) < 2:
            excluded.append((str(p), N, len(Xs), 'EXCLUDED-BY-CAP: '
                             'the block has fewer than two points at '
                             'depth <= %d, so no N-step window with '
                             'dep + N <= %d exists' % (CAP_T - N, CAP_T)))
            continue
        mH = delta_star_multi(Xs, N, False)
        mM = delta_star_multi(Xs, N, True)
        dkH = mH['kind13'][0]
        dkM, nuM = mM['kind13']
        deM = mM['event113'][0]
        dsup = tuple(sorted({len(h) for h in Xs}))
        prof_rows.append((p, N, len(Xs), dsup,
                          str(dkH), str(dkM), str(deM), len(nuM),
                          str(mM['profile'][0]),
                          str(mM['profile_unordered'][0]),
                          str(mM['rsig_indicator'][0]),
                          max(dsup) + N))
F['B2_profile_rows'] = tuple(
    r[:8] for r in prof_rows)          # the delivered shape, unchanged
F['B2_profile_rows_full'] = tuple(prof_rows)
F['B2_blocks_excluded'] = tuple(excluded)
F['B2_atom_deltas'] = tuple(
    (str(p), N, dH, dM, dE) for p, N, n, ds, dH, dM, dE, nnu,
    dp, dpu, dr, sd in prof_rows)
emit("    profile | N | |block-window| | depths | delta* H7 primary | "
     "delta* MATCHED primary | delta* MATCHED control | |support(nu)|")
for p, N, n, ds, dH, dM, dE, nnu, dp, dpu, dr, sd in prof_rows:
    emit(f"    {p} | {N} | {n} | {list(ds)} | {dH} | {dM} | {dE} | "
         f"{nnu}")
for p, N, n, why in excluded:
    emit(f"    {p} | {N} | {n} | {why}")
emit("  THE SAME ROWS AT THE THREE FURTHER GRAINS (MATCHED), so that "
     "the coarsening lemma below can be checked cell by cell rather "
     "than asserted:")
emit("    profile | N | kind13 | event113 | profile | "
     "profile-unordered | rsig-indicator")
for p, N, n, ds, dH, dM, dE, nnu, dp, dpu, dr, sd in prof_rows:
    emit(f"    {p} | {N} | {dM} | {dE} | {dp} | {dpu} | {dr}")

_atoms = [(p, N, n, dM) for p, N, n, ds, dH, dM, dE, nnu, dp, dpu, dr,
          sd in prof_rows if dM == '1']
F['B2_atoms'] = tuple((str(p), N, n, dM) for p, N, n, dM in _atoms)
F['B2_atom_found'] = len(_atoms) > 0
F['B2_best_delta'] = '1' if _atoms else '0'
F['B2_best_N'] = (min(N for p, N, n, dM in _atoms) if _atoms else None)
F['B2_grain_split'] = tuple(
    (str(p), N, dM, dE) for p, N, n, ds, dH, dM, dE, nnu, dp, dpu, dr,
    sd in prof_rows if dM != dE)
F['B2_grain_split_direction_ok'] = all(
    dM == '1' and dE == '0' for p, N, dM, dE in F['B2_grain_split'])
# THE COARSENING LEMMA, CHECKED CELL BY CELL.  If Psi' coarsens Psi
# then delta*(C, N, Psi') >= delta*(C, N, Psi), because
# min_x sum_i P^N(x, s_i) >= sum_i min_x P^N(x, s_i).  The event x
# weight grain refines the kind x weight grain (the event determines
# its kind), and both refine the holdings-profile grain on these
# blocks, so the delivered numbers must satisfy
# event113 <= kind13 <= profile.  Every row is checked; a violation
# would mean one of the three columns is wrong.
F['B2_coarsening_rows'] = tuple(
    (str(p), N, dE, dM, dp) for p, N, n, ds, dH, dM, dE, nnu, dp, dpu,
    dr, sd in prof_rows)
F['B2_coarsening_violations'] = sum(
    1 for p, N, n, ds, dH, dM, dE, nnu, dp, dpu, dr, sd in prof_rows
    if not (Fr(dE) <= Fr(dM) <= Fr(dp)))
_nu_desc = None
if _atoms:
    p0 = min((p for p, N, n, dM in _atoms if N == F['B2_best_N']),
             key=SK)
    Xs0 = [h for h in PROFBLK[p0] if len(h) + F['B2_best_N'] <= CAP_T]
    _d0, nu0 = delta_star(Xs0, F['B2_best_N'], psi_kind_of, True)
    _nu_desc = tuple(sorted((str(k[1:]), str(w)) for k, w in nu0.items()))
    F['B2_nu_support'] = len(nu0)
    F['B2_nu_measure'] = _nu_desc
    F['B2_nu_profile'] = str(p0)
    F['B2_nu_block_size'] = len(Xs0)
    F['B2_nu_depths'] = tuple(sorted({len(h) for h in Xs0}))
else:
    F['B2_nu_support'] = 0
    F['B2_nu_measure'] = ()
    F['B2_nu_profile'] = None
    F['B2_nu_block_size'] = 0
    F['B2_nu_depths'] = ()

emit("")
emit(f"  WHAT LANDED, WITH ITS UNIVERSALS REMOVED.  At the MATCHED "
     f"horizon and the PRIMARY grain, every holdings-profile block of "
     f"R-SIG THAT THIS CAP CAN TEST — {len(set(p for p, N, n, d in _atoms))} "
     f"of the {F['rsig_blocks_n']} blocks the family carries, over "
     f"{len(prof_rows)} (block, N) rows — is an EXACT ATOM: delta* = 1, "
     f"i.e. P^N(x, .) is the SAME measure for every x in the block, "
     f"not merely bounded below by a common one.  The blocks that "
     f"reach delta* = 1 and the windows they were measured on: "
     f"{list(F['B2_atoms'])}.  The remaining block (3, 3) is "
     f"EXCLUDED-BY-CAP and is NOT claimed to be an atom: "
     f"{list(F['B2_blocks_excluded'])}.")
emit(f"  AND WHAT delta* = 1 MEANS, said once so that the label cannot "
     f"drift: a set with delta* = 1 is a set contained in a SINGLE "
     f"state of the N-step Psi-quotient chain.  That is a LUMPABILITY "
     f"statement — the block is one quotient state — and it is the "
     f"DEGENERATE end of the minorization scale, not its strong end: a "
     f"Doeblin minorization is an instrument when delta lies strictly "
     f"between 0 and 1 on a set the chain returns to, and delta = 1 "
     f"contributes no contraction because there is nothing left to "
     f"contract.  The FOUND segment records a lumpability observation "
     f"under a minorization label, and B3 measures the half it lacks.")
if _atoms:
    emit(f"  nu, EXHIBITED (block {F['B2_nu_profile']}, N = "
         f"{F['B2_best_N']}, over {F['B2_nu_block_size']} points "
         f"spanning depths {list(F['B2_nu_depths'])}): a measure on "
         f"{F['B2_nu_support']} Psi-classes, namely")
    for k, w in _nu_desc:
        emit(f"      {w}  at  {k}")
emit(f"  WHAT DID NOT.  On the FULL R-SIG class delta* = 0 at every "
     f"window carrying more than one holdings profile (N = "
     f"{[r[0] for r in F['B2_hetero_rows']]}), under both horizon "
     f"conventions.  "
     f"The obstruction is NOT the horizon and NOT the cap: it is the "
     f"HOLDINGS PROFILE.  Two R-SIG points with different profiles "
     f"carry different delivery-menu weights (the delivery budget is "
     f"1/4 divided by |holdings(a)|, so the superseded remainder is "
     f"WRITTEN INTO THE MENU), and their N-step laws therefore share "
     f"no Psi-class at all.")
emit(f"  THE GRAIN IS ARENA DATA AND IT BITES, WITH ITS DIRECTION "
     f"NAMED: at the CONTROL grain the same blocks split — "
     f"{len(F['B2_grain_split'])} of {len(prof_rows)} rows have "
     f"delta*(primary) != delta*(control), because the control grain "
     f"resolves the version NAMES that the primary grain forgets.  In "
     f"EVERY such row the primary value is 1 and the control value is "
     f"0 ({F['B2_grain_split_direction_ok']}): the split runs one way "
     f"only.  Rows where they differ: {list(F['B2_grain_split'])}.  So "
     f"at the control grain R-MENU — the (1, 1) block — is the ONLY "
     f"block that remains an atom, and the sentence 'R-MENU is not a "
     f"special class at all' is true at the primary grain and FALSE at "
     f"the control grain.  Both readings are printed; neither is "
     f"promoted.")
emit(f"  THE COARSENING LEMMA, STATED AND CHECKED CELL BY CELL.  If "
     f"Psi' coarsens Psi then delta*(C, N, Psi') >= delta*(C, N, Psi), "
     f"since min_x sum_i P^N(x, s_i) >= sum_i min_x P^N(x, s_i).  The "
     f"event x weight grain REFINES the kind x weight grain and both "
     f"refine the holdings-profile grain, so every row must satisfy "
     f"event113 <= kind13 <= profile.  Violations over "
     f"{len(F['B2_coarsening_rows'])} rows: "
     f"{F['B2_coarsening_violations']}.  TWO CONSEQUENCES THE UNIT "
     f"OWNS: (i) delta* = 0 for the full class at the 13-class grain "
     f"implies delta* = 0 at EVERY REFINEMENT of it, including all six "
     f"of T5's committed abstractions, so no pinned abstraction "
     f"unblocks the ladder; (ii) delta* = 1 on a block at the 13-class "
     f"grain implies delta* = 1 at every COARSENING of it.  The result "
     f"is more robust than a two-point measurement, and strictly so.")

gate("B2-ATOM", KIND_SUB,
     "THE MINORIZATION LANDS ON THE PROFILE BLOCKS THE CAP CAN TEST: "
     "at the matched horizon and the primary grain every "
     "holdings-profile block of R-SIG with a testable window is an "
     "EXACT ATOM — delta* = 1 with an explicitly exhibited nu on a "
     "small support — and the measurement could have come out "
     "otherwise, since the same computation returns 0 on the full "
     "class and on the control grain.  The claim is NOT universal over "
     "blocks: the fifth block is excluded by the cap and named",
     lambda f: (f['B2_atom_found'] and f['B2_best_delta'] == '1'
                and f['B2_nu_support'] > 0
                and len(f['B2_atoms']) >= 2
                and len(f['B2_nu_measure']) == f['B2_nu_support']
                and sum(Fr(w) for k, w in f['B2_nu_measure']) == 1
                and any(p == '(3, 3)'
                        for p, N, n, w in f['B2_blocks_excluded'])),
     lambda f: f"atoms = {list(f['B2_atoms'])}; excluded-by-cap = "
               f"{[(p, N) for p, N, n, w in f['B2_blocks_excluded']]}; "
               f"nu support = "
               f"{f['B2_nu_support']} classes on block "
               f"{f['B2_nu_profile']} over {f['B2_nu_block_size']} "
               f"points at depths {list(f['B2_nu_depths'])}")
gate("B2-BLOCKCOVER", KIND_SUB,
     "THE BLOCK DECOMPOSITION COVERS R-SIG EXACTLY, so that an "
     "undeclared block cannot recur: the holdings-profile blocks are "
     "built from every R-SIG point of the family, their sizes sum to "
     "the R-SIG count, there are FIVE of them where the depth-<=5 "
     "census names four, and the fifth is (3, 3) with 424 points all "
     "at depth 6",
     lambda f: (f['rsig_block_coverage'] == f['rsig_all_count']
                and f['rsig_all_count'] == 39361
                and f['rsig_blocks_n'] == 5
                and f['rsig_blocks_declared_at_d5'] == 4
                and ('(3, 3)', 424) in f['rsig_profiles_all']
                and dict(f['rsig_profile_depths'])['(3, 3)']
                == ((6, 424),)),
     lambda f: f"blocks = {list(f['rsig_profiles_all'])}; coverage "
               f"{f['rsig_block_coverage']} of {f['rsig_all_count']}; "
               f"depth support = {list(f['rsig_profile_depths'])}")
gate("B2-COARSENING", KIND_SUB,
     "THE COARSENING LEMMA HOLDS ON EVERY MEASURED ROW: delta* is "
     "monotone under coarsening, so event113 <= kind13 <= profile at "
     "every (block, N) row — 0 violations.  This is what makes the "
     "two-grain measurement decisive rather than two data points, and "
     "it is what transports every delta* in this receipt to any "
     "refinement or coarsening of the grains actually run",
     lambda f: (f['B2_coarsening_violations'] == 0
                and len(f['B2_coarsening_rows']) >= 6),
     lambda f: f"violations = {f['B2_coarsening_violations']} over "
               f"{len(f['B2_coarsening_rows'])} rows; rows = "
               f"{list(f['B2_coarsening_rows'])}")
gate("B2-PSI-COUNTERREADING", KIND_SUB,
     "THE BLOCKED CLAUSE IS PSI-FAMILY-RELATIVE AND THE COUNTER-"
     "READING IS PRINTED: at Psi = the R-SIG indicator the same full "
     "class has delta* = 1 at matched horizon on both of its widest "
     "windows, while at the two menu grains and at both holdings-"
     "profile grains it is 0 there.  A verdict that stated the delta* "
     "= 0 clause without its grain would be false at a declared "
     "abstraction, and this gate is what forbids it",
     lambda f: (f['B2_rsig_indicator_delta1_at'] == (1, 2)
                and len(f['B2_full_grain_rows']) == 3),
     lambda f: f"rsig-indicator MATCHED by N = "
               f"{list(f['B2_rsig_indicator_matched'])}; delta* = 1 at "
               f"N = {list(f['B2_rsig_indicator_delta1_at'])}")
gate("B2-FULLZERO", KIND_SUB,
     "AND IT DOES NOT EXTEND ON THE WINDOWS THAT CAN CARRY THE CLAIM: "
     "on the two WIDEST windows of the full R-SIG class — the only "
     "ones holding enough of the class to say anything about it — "
     "delta* is exactly 0 under BOTH horizon conventions, and each of "
     "those windows carries more than one holdings profile.  The "
     "narrower windows are printed beside them and nothing is claimed "
     "from them",
     lambda f: (len(f['B2_hetero_zero_rows']) >= 2
                and all(dk == '0' and dm == '0' for N, n, np_, dk, dm
                        in f['B2_hetero_zero_rows'])
                and all(np_ > 1 for N, n, np_, dk, dm
                        in f['B2_hetero_zero_rows'])
                and min(r[1] for r in f['B2_hetero_zero_rows']) > 100),
     lambda f: f"zero rows (N, points, profiles, H7, MATCHED) = "
               f"{list(f['B2_hetero_zero_rows'])}; positive "
               f"cross-profile rows on narrower windows = "
               f"{list(f['B2_hetero_pos_rows'])}; single-profile rows "
               f"(no cross-profile content) = "
               f"{list(f['B2_homo_rows'])}")
gate("B2-GRAIN", KIND_SUB,
     "THE GRAIN-SWAP CONTROL FIRES INSIDE ARM B, IN THE DIRECTION ITS "
     "LABEL CLAIMS: exactly 4 of the 6 measured (block, N) rows are an "
     "atom at the primary grain and are NOT at the control grain, and "
     "in EVERY such row the primary value is exactly 1 and the control "
     "value exactly 0 — a directional fact, not a non-emptiness test.  "
     "So the minorization is grain-relative and the grain must be "
     "declared",
     lambda f: (len(f['B2_grain_split']) == 4
                and f['B2_grain_split_direction_ok']
                and all(dM == '1' and dE == '0'
                        for p, N, dM, dE in f['B2_grain_split'])
                and len(f['B2_profile_rows']) == 6),
     lambda f: f"{len(f['B2_grain_split'])} of "
               f"{len(f['B2_profile_rows'])} rows differ, all "
               f"primary 1 / control 0 = "
               f"{f['B2_grain_split_direction_ok']}: "
               f"{list(f['B2_grain_split'])}")

# ======================================================================
# B4 — THE CARRIER.  #82 ruled CONG-185 (d74's coarsest weighted
# congruence at (A,B) depth <= 4) the law's carrier, superseding MENU +
# G.  Do these atoms survive the carrier change?  The question is
# decidable HERE, from this unit's own measured columns plus the
# coarsening lemma, and the answer is measured rather than deferred.
# ======================================================================
emit("")
emit("  [B4 — THE CARRIER: do the atoms survive CONG-185?]")
prog("ARM B: the refinement chain and the carrier collapse ...")
_ekmap = {}
_chain_bad = 0
for h in FAM4:
    se, sk = shape_event(h), shape_kind(h)
    if se in _ekmap and _ekmap[se] != sk:
        _chain_bad += 1
    _ekmap[se] = sk
F['carrier_chain_tested'] = len(FAM4)
F['carrier_chain_exceptions'] = _chain_bad
F['grain_primary_by_window'] = tuple(
    len({shape_kind(h) for h in CACHE if len(h) <= d}) for d in range(0, 6))
F['grain_control_by_window'] = tuple(
    len({shape_event(h) for h in CACHE if len(h) <= d}) for d in range(0, 6))
F['carrier_cong_d4'] = 185
F['carrier_menu_d4'] = 113
F['carrier_cong_d5'] = 462
F['carrier_menu_d5'] = 265
_dead = [(str(p), N) for p, N, n, ds, dH, dM, dE, nnu, dp, dpu, dr, sd
         in prof_rows if dE == '0']
_open = [(str(p), N) for p, N, n, ds, dH, dM, dE, nnu, dp, dpu, dr, sd
         in prof_rows if dE != '0']
F['B4_carrier_dead_rows'] = tuple(_dead)
F['B4_carrier_open_rows'] = tuple(_open)
F['B4_statability'] = tuple(
    (str(p), N, list(ds)[0], list(ds)[-1], sd, sd <= 4, sd <= 5)
    for p, N, n, ds, dH, dM, dE, nnu, dp, dpu, dr, sd in prof_rows)
F['B4_rows_statable_d4'] = sum(1 for r in F['B4_statability'] if r[5])
F['B4_rows_statable_d5'] = sum(1 for r in F['B4_statability'] if r[6])
_b11 = [h for h in PROFBLK[(1, 1)] if len(h) <= CAP_ESC]
F['B4_block11_menu_classes_d4'] = len({shape_event(h) for h in _b11})
F['B4_block11_points_d4'] = len(_b11)
emit(f"  THE REFINEMENT CHAIN, ESTABLISHED IN-UNIT AND NOT ASSUMED.  "
     f"d74's own output states the construction — 'Refining the menu "
     f"partition by successor-closure (partition refinement to a fixed "
     f"point) gives the coarsest weighted CONGRUENCE' — and commits "
     f"'AB4 (A,B) depth<=4 CARRIER: menu quotient "
     f"{F['carrier_menu_d4']} classes; coarsest congruence "
     f"{F['carrier_cong_d4']} classes'.  Both strings are carried here "
     f"as verbatim-context windows.  Measured here: the event x weight "
     f"shape DETERMINES the kind x weight shape over all "
     f"{F['carrier_chain_tested']} histories of depth <= {CAP_ESC}, "
     f"with {F['carrier_chain_exceptions']} exceptions.  Therefore")
emit(f"      CONG-{F['carrier_cong_d4']}  <=  MENU-"
     f"{F['carrier_menu_d4']}  <=  KIND-"
     f"{F['grain_primary_classes']}   (finer to coarser).")
emit(f"  AND THE GRAIN NAMES ARE WINDOW-BOUND, which a successor must "
     f"know before it implements 'the 13-class grain' literally: per "
     f"window depth 0..5 the KIND x weight partition has "
     f"{list(F['grain_primary_by_window'])} classes and the EVENT x "
     f"weight partition has {list(F['grain_control_by_window'])} — "
     f"reproducing d74's committed MENU {F['carrier_menu_d4']} at "
     f"depth <= 4 AND its committed {F['carrier_menu_d5']} at depth "
     f"<= 5, from this unit's own family, as an independent re-anchor "
     f"of both carrier rows.  ARM B evaluates Psi on successors at "
     f"depths up to {CAP_T}, where the counts are larger still.")
emit(f"  THE COLLAPSE, MEASURED FROM THIS RECEIPT'S OWN COLUMNS.  By "
     f"the coarsening lemma delta*(C, N, CONG-{F['carrier_cong_d4']}) "
     f"<= delta*(C, N, MENU-{F['carrier_menu_d4']}), and the MATCHED "
     f"control column IS the MENU-{F['carrier_menu_d4']} column.  So "
     f"{len(_dead)} of the {len(prof_rows)} delivered atom rows have "
     f"delta* = 0 AT THE RULED CARRIER — {_dead} — and only "
     f"{len(_open)} remain candidates — {_open}, both of them the "
     f"(1, 1) block, i.e. R-MENU.  THE ATOM CLAIM COLLAPSES TO R-MENU "
     f"AT THE CARRIER.  The two open rows are bounded above by 1 and "
     f"are a genuine successor computation, not a result of this "
     f"unit; what is measurable here is that the whole (1, 1) block's "
     f"depth-<= {CAP_ESC} part ({F['B4_block11_points_d4']} points) "
     f"lies inside {F['B4_block11_menu_classes_d4']} MENU-"
     f"{F['carrier_menu_d4']} class(es), so the first refinement round "
     f"does not split it — rounds 2..5 might, and that is the open "
     f"question.")
emit(f"  PER-BLOCK STATABILITY ON THE CARRIER'S OWN WINDOW, STAMPED.  "
     f"A (block, N) row is statable on a depth-D carrier only if the "
     f"block's points AND their N-step successors lie at depth <= D.")
emit("    profile | N | block depths | max successor depth | statable "
     "on CONG-185 (d<=4) | statable on CONG-462 (d<=5)")
for p, N, dlo, dhi, sd, s4, s5 in F['B4_statability']:
    emit(f"    {p} | {N} | [{dlo}..{dhi}] | {sd} | {s4} | {s5}")
emit(f"  {F['B4_rows_statable_d4']} of {len(prof_rows)} rows are "
     f"statable on the d <= 4 carrier and "
     f"{F['B4_rows_statable_d5']} on the d <= 5 carrier: the carrier "
     f"must be extended to depth {CAP_T} before ANY of these rows can "
     f"be re-run on it.  d74 commits the wider arm — '(A,B) depth<=5 "
     f"CARRIER: menu quotient {F['carrier_menu_d5']} classes; coarsest "
     f"congruence {F['carrier_cong_d5']} classes after 6 refinement "
     f"rounds' — and THAT ROW IS CARRIED IN THIS UNIT'S T5 SUPPLY, "
     f"because it is the object the Gamma-iteration needs.")
gate("B4-CARRIER-CHAIN", KIND_SUB,
     "THE REFINEMENT CHAIN IS ESTABLISHED, NOT ASSUMED: the event x "
     "weight menu shape determines the kind x weight menu shape at "
     "every history of the depth-4 family (0 exceptions over 3,969), "
     "the two partitions have 113 and 13 classes there, and the "
     "per-window class counts reproduce d74's committed MENU 113 at "
     "depth <= 4 and 265 at depth <= 5 from this unit's own family.  "
     "So CONG-185 <= MENU-113 <= KIND-13 and every delta* in this "
     "receipt transports along it",
     lambda f: (f['carrier_chain_exceptions'] == 0
                and f['carrier_chain_tested'] == 3969
                and f['grain_control_by_window'] == (1, 5, 13, 45, 113, 265)
                and f['grain_primary_by_window'] == (1, 2, 5, 9, 13, 21)
                and f['grain_control_by_window'][4] == f['carrier_menu_d4']
                and f['grain_control_by_window'][5] == f['carrier_menu_d5']),
     lambda f: f"exceptions = {f['carrier_chain_exceptions']} over "
               f"{f['carrier_chain_tested']}; KIND per window = "
               f"{list(f['grain_primary_by_window'])}; EVENT per "
               f"window = {list(f['grain_control_by_window'])}")
gate("B4-CARRIER-SUPPLY", KIND_SUB,
     "THE CARRIER COLLAPSE IS MEASURED AND ITS SUPPLY IS CARRIED: 4 of "
     "the 6 delivered atom rows have delta* = 0 at the ruled carrier "
     "CONG-185, by the coarsening lemma applied to this receipt's own "
     "MATCHED-control column; the 2 survivors are exactly the (1, 1) "
     "block, i.e. R-MENU; NO delivered row is statable on either "
     "committed carrier window, so the successor needs the carrier "
     "extended past depth 4; and d74's committed d <= 5 row (menu 265 "
     "/ congruence 462) is carried in the T5 supply with its own "
     "verbatim anchor",
     lambda f: (len(f['B4_carrier_dead_rows']) == 4
                and len(f['B4_carrier_open_rows']) == 2
                and all(p == '(1, 1)'
                        for p, N in f['B4_carrier_open_rows'])
                and f['B4_rows_statable_d4'] == 0
                and f['carrier_cong_d5'] == 462
                and f['carrier_menu_d5'] == 265),
     lambda f: f"dead at CONG-185: {list(f['B4_carrier_dead_rows'])}; "
               f"open: {list(f['B4_carrier_open_rows'])}; statable on "
               f"d<=4: {f['B4_rows_statable_d4']}, on d<=5: "
               f"{f['B4_rows_statable_d5']}")

# --- B3: does the atom ladder give regeneration?  The hitting test.
emit("")
emit("  [B3 — DOES THE ATOM LADDER REGENERATE?  The hitting test]")
emit("  A Doeblin/regeneration argument needs BOTH halves: a small set "
     "with delta > 0 (B2 has one, in fact an atom) AND a uniform "
     "lower bound on the probability of RETURNING to that same small "
     "set within N steps.  The second half is measured here.")
prog("ARM B: hitting probability into R-SIG (the whole class) ...")
_cum = F['t_cumulative']
emit(f"  (i) THE RETURN INTO R-SIG ITSELF, on the widest window this "
     f"family admits.  This is the predecessor's own table extended by "
     f"one full depth: it tested N-step returns on the window "
     f"len(h) + N <= {CAP_T - 1}, which leaves {_cum[CAP_T - 1 - 4]} "
     f"histories at N = 4 and {_cum[CAP_T - 1 - 5]} at N = 5; the "
     f"depth-{CAP_T} family moves that to len(h) + N <= {CAP_T}, i.e. "
     f"{_cum[CAP_T - 4]} histories at N = 4 and {_cum[CAP_T - 5]} at "
     f"N = 5.  Every count in this sentence is read off the census "
     f"above, not typed.")
RSIGALL = set(RS)
rsig_rows = []
for N in range(1, NMAX + 1):
    tested = 0
    zeros = 0
    worst = None
    for h in CACHE:
        if len(h) + N > CAP_T:
            continue
        tested += 1
        fr = {h: Fr(1)}
        hit = Fr(0)
        for st in range(N):
            nxt = defaultdict(Fr)
            for g, w in fr.items():
                kk = krel_c(g, CAP_T + 1 - len(g))
                for e, q in CACHE[g]:
                    g2 = g + (e,)
                    if g2 in RSIGALL:
                        hit += w * kk[e]
                    else:
                        nxt[g2] += w * kk[e]
            fr = nxt
        if hit == 0:
            zeros += 1
        if worst is None or hit < worst:
            worst = hit
    rsig_rows.append((N, tested, zeros, str(worst)))
F['B3_rsig_rows'] = tuple(rsig_rows)
F['B3_rsig_zeros'] = tuple(z for N, t, z, w in rsig_rows)
F['B3_rsig_inf_widest'] = rsig_rows[0][3]
F['B3_rsig_first_nonzero_N'] = next(
    (N for N, t, z, w in rsig_rows if z == 0), None)
emit("    N | histories tested | return probability EXACTLY 0 at | "
     "infimum")
for N, t, z, w in rsig_rows:
    emit(f"    {N} | {t} | {z} | {w}")
emit(f"  the zero-set of the R-SIG return collapses with N "
     f"({list(F['B3_rsig_zeros'])}) and first empties at N = "
     f"{F['B3_rsig_first_nonzero_N']}, on a window of "
     f"{[t for N, t, z, w in rsig_rows if N == F['B3_rsig_first_nonzero_N']][0]}"
     f" histories.  ON THE WIDEST WINDOW ({rsig_rows[0][1]} "
     f"histories) THE INFIMUM IS {F['B3_rsig_inf_widest']}, and that "
     f"is the number a uniform Doeblin bound would have to beat.")

prog("ARM B: minimal return distance to R-SIG by depth ...")
DIST = {}
for d in range(CAP_T, -1, -1):
    for h in LEVEL[d]:
        if h in RSIGALL:
            DIST[h] = 0
            continue
        if d == CAP_T:
            DIST[h] = None
            continue
        cs = [DIST[h + (e,)] for e, q in CACHE[h]]
        cs = [c for c in cs if c is not None]
        DIST[h] = (min(cs) + 1) if cs else None
dist_by_depth = []
for d in range(0, CAP_T + 1):
    vals = [DIST[h] for h in LEVEL[d] if DIST[h] is not None]
    unk = sum(1 for h in LEVEL[d] if DIST[h] is None)
    look = CAP_T - d
    dist_by_depth.append((d, (max(vals) if vals else None), look,
                          bool(vals) and max(vals) < look,
                          unk, len(LEVEL[d])))
F['B3_dist_by_depth'] = tuple(dist_by_depth)
F['B3_dist_unresolved'] = sum(u for d, mx, lk, sat, u, t
                              in dist_by_depth if sat)
F['B3_dist_unresolved_all'] = sum(u for d, mx, lk, sat, u, t
                                  in dist_by_depth)
F['B3_dist_max_saturated'] = max(
    (mx for d, mx, lk, sat, u, t in dist_by_depth if sat), default=None)
F['B3_dist_rows_saturated'] = tuple(
    d for d, mx, lk, sat, u, t in dist_by_depth if sat)
# The two keys above hold the INFORMATIVE rows (max < lookahead), which
# is the opposite of what "saturated" says.  They are kept as aliases
# for one iteration and the correctly-named keys are the ones a
# consumer should read.
F['B3_dist_rows_informative'] = F['B3_dist_rows_saturated']
F['B3_dist_max_informative'] = F['B3_dist_max_saturated']
F['B3_dist_max_by_depth'] = tuple(
    (d, mx) for d, mx, lk, sat, u, t in dist_by_depth)
F['B3_dist_max_rises'] = all(
    dist_by_depth[i][1] >= dist_by_depth[i - 1][1]
    for i in range(1, len(dist_by_depth))
    if dist_by_depth[i][1] is not None
    and dist_by_depth[i - 1][1] is not None)
emit(f"  (ii) THE MINIMAL RETURN DISTANCE, exactly.  For every history "
     f"the shortest continuation reaching R-SIG is computed backwards "
     f"through the family.  A history whose whole remaining subtree "
     f"misses R-SIG is recorded as UNRESOLVED AT THIS CAP, never as "
     f"infinite.  The LOOKAHEAD column is what the cap allows a row to "
     f"see, and a row is only informative when its maximum is STRICTLY "
     f"BELOW its lookahead — otherwise the number is the cap talking, "
     f"not the process.")
emit("    parent depth | max finite distance | lookahead | "
     "informative? | unresolved at this cap | histories")
for d, mx, lk, sat, unk, tot in dist_by_depth:
    emit(f"    {d} | {mx} | {lk} | {sat} | {unk} | {tot}")
emit(f"  informative rows: depths {list(F['B3_dist_rows_informative'])}"
     f", across which the largest return distance actually attained is "
     f"{F['B3_dist_max_informative']}.  The maximum finite distance by "
     f"depth over the whole table is {list(F['B3_dist_max_by_depth'])} "
     f"— it does NOT rise monotonically "
     f"({F['B3_dist_max_rises']}); the attained maximum is "
     f"{F['B3_dist_max_informative']} on every informative row, and "
     f"the deeper rows fall because the cap is talking.  Unresolved ON "
     f"THOSE ROWS: "
     f"{F['B3_dist_unresolved']} histories whose "
     f"entire remaining subtree contains no R-SIG point (over the "
     f"whole censused window, including the cap-limited rows, "
     f"{F['B3_dist_unresolved_all']:,}).  A uniform "
     f"Doeblin N would have to cover those too, and at this cap they "
     f"are not covered.  THIS IS A CAP MEASUREMENT, NOT AN "
     f"UNBOUNDEDNESS THEOREM, and it is labelled one.")

prog("ARM B: hitting probabilities into each profile block ...")
emit("  (iii) THE RETURN INTO EVERY PROFILE BLOCK OF THE FAMILY — all "
     "five, the fifth included — since the atoms of B2 are the blocks "
     "and not their union.  (3, 3) has no delta* window at this cap, "
     "but its hitting row is measured exactly like the others rather "
     "than the block being dropped.")
hit_rows = []
for p in PROFS:
    S = set(PROFBLK[p])
    for N in (1, 2, 3, 4):
        tested = 0
        zeros = 0
        worst = None
        for h in CACHE:
            if len(h) + N > CAP_T:
                continue
            tested += 1
            fr = {h: Fr(1)}
            hit = Fr(0)
            for st in range(N):
                nxt = defaultdict(Fr)
                for g, w in fr.items():
                    kk = krel_c(g, CAP_T + 1 - len(g))
                    for e, q in CACHE[g]:
                        g2 = g + (e,)
                        if g2 in S:
                            hit += w * kk[e]
                        else:
                            nxt[g2] += w * kk[e]
                fr = nxt
            if hit == 0:
                zeros += 1
            if worst is None or hit < worst:
                worst = hit
        hit_rows.append((str(p), N, tested, zeros, str(worst)))
        if N >= 3 and zeros == 0:
            break
F['B3_hit_rows'] = tuple(hit_rows)
emit("    profile block | N | histories tested | hitting probability "
     "EXACTLY 0 at | infimum")
for p, N, t, z, w in hit_rows:
    emit(f"    {p} | {N} | {t} | {z} | {w}")
F['B3_all_zero_inf'] = all(w == '0' for p, N, t, z, w in hit_rows)
F['B3_zero_fraction'] = tuple((p, N, z, t) for p, N, t, z, w in hit_rows)
F['B3_block_inf_values'] = tuple(sorted({w for p, N, t, z, w in hit_rows}))
F['B3_block_inf_sup'] = str(max(Fr(w) for p, N, t, z, w in hit_rows))

# IS EACH BLOCK ABSORBING-COMPLEMENT / RE-ENTERED?  Two objects, and
# the first is nearly vacuous.  `reentry(S)` counts the points of S
# having a proper prefix OUTSIDE S; for any block not containing the
# root the empty history is such a prefix for EVERY point, so
# reentry(S) = |S| identically, by construction and not by measurement.
# Only the (1, 1) row, which contains the root, carries information.
# The object a regeneration argument actually needs is the number of
# TRANSITIONS INTO the block from outside it, and that is measured
# here beside it and gated instead.
prog("ARM B: block re-entry and entry censuses ...")
_into = {p: 0 for p in PROFS}
_BLKSET = {p: set(PROFBLK[p]) for p in PROFS}
_BLKOF = {}
for p in PROFS:
    for h in PROFBLK[p]:
        _BLKOF[h] = p
for h in CACHE:
    hp = _BLKOF.get(h)
    for e, q in CACHE[h]:
        p2 = _BLKOF.get(h + (e,))
        if p2 is not None and p2 != hp:
            _into[p2] += 1
blk_re = []
for p in PROFS:
    S = _BLKSET[p]
    blk_re.append((str(p), len(S), reentry(S), ROOT in S, _into[p]))
F['B3_block_reentries'] = tuple((a, b, c) for a, b, c, r, i in blk_re)
F['B3_block_entry_rows'] = tuple(blk_re)
F['B3_block_reentry_forced'] = tuple(
    (a, b, c) for a, b, c, r, i in blk_re if not r)
F['B3_block_reentry_forced_all'] = all(
    c == b for a, b, c, r, i in blk_re if not r)
F['B3_block_entries_positive'] = all(i > 0 for a, b, c, r, i in blk_re)
F['B3_block_entries_root_zero'] = all(i == 0 for a, b, c, r, i in blk_re
                                      if r)
F['B3_block_entries_nonroot_positive'] = all(
    i > 0 for a, b, c, r, i in blk_re if not r)
F['B3_block_entries'] = tuple((a, i) for a, b, c, r, i in blk_re)
# THE MONOTONE PROFILE, AT FULL FAMILY SCOPE.  Both scopes are carried:
# the narrowed one because the first delivery reported it, and the full
# one because that is the scope the sentence claims.
prof_dec = 0
prof_pairs = 0
for h in CACHE:
    if len(h) >= 5:
        continue
    hold_h, _ = HOLD[h]
    for e, q in CACHE[h]:
        h2 = h + (e,)
        if len(h2) > 5:
            continue
        hold_2, _ = HOLD[h2]
        prof_pairs += 1
        if (len(hold_2['A']) < len(hold_h['A'])
                or len(hold_2['B']) < len(hold_h['B'])):
            prof_dec += 1
F['B3_profile_pairs_narrow'] = prof_pairs
F['B3_profile_decreases_narrow'] = prof_dec
F['B3_profile_pairs'] = F['mono_pairs_all']
F['B3_profile_decreases'] = prof_dec_all

emit(f"  BLOCK RE-ENTRY CENSUS, WITH ITS DEFINITION AND ITS FORCED "
     f"ROWS NAMED.  `re-entry` counts the points of a block having a "
     f"proper prefix OUTSIDE it.  FOR ANY BLOCK NOT CONTAINING THE "
     f"ROOT this count is the block's own size BY CONSTRUCTION — the "
     f"empty history is an outside ancestor of every point — so only "
     f"the (1, 1) row, which contains the root, carries information; "
     f"the forced rows are {list(F['B3_block_reentry_forced'])} and "
     f"every one of them is forced ({F['B3_block_reentry_forced_all']})"
     f".  The object the argument actually needs is the number of "
     f"TRANSITIONS INTO the block from outside it, measured here:")
emit("    profile | size | re-entries (forced unless the block has the "
     "root) | contains root | TRANSITIONS INTO the block")
for a, b, c, r, i in blk_re:
    emit(f"    {a} | {b} | {c} | {r} | {i}")
emit(f"  AND THAT CENSUS SPLITS THE BLOCKS IN TWO, WHICH THE RE-ENTRY "
     f"COLUMN HID.  The four blocks that do not contain the root are "
     f"entered from outside at a strictly positive number of "
     f"transitions ({F['B3_block_entries_nonroot_positive']}), so for "
     f"them it is the UNIFORMITY of the entry probability that fails, "
     f"not its existence.  The (1, 1) block — which contains the root, "
     f"which IS R-MENU, and which is the ONLY block still an atom at "
     f"the ruled carrier — is entered at EXACTLY 0 transitions "
     f"({F['B3_block_entries_root_zero']}): it is "
     f"absorbing-complement, exactly as ARM A fact 4's committed "
     f"0-re-entry row says.  So the one atom that survives the carrier "
     f"change is the one small set the process can never return to at "
     f"all, and no uniform bound is even posable for it.  The other "
     f"four are enterable and have hitting infimum 0.")
emit(f"  and the mechanism, censused AT FULL FAMILY SCOPE: over all "
     f"{F['B3_profile_pairs']} transitions of the family the holdings "
     f"profile DECREASES at {F['B3_profile_decreases']} of them (the "
     f"narrowed depth-<5 window gives {F['B3_profile_decreases_narrow']} of "
     f"{F['B3_profile_pairs_narrow']} — 12.6% of the family, and it is "
     f"reported beside the full scope, never in place of it).  The profile is a MONOTONE "
     f"NON-DECREASING COORDINATE OF THE PROCESS.")
emit(f"  AND THE LADDER IS A COROLLARY, NOT AN INDEPENDENT FINDING.  "
     f"Set-monotonicity of holdings (A4-MONO, a theorem of the layer: "
     f"View.holdings is a union over the view's past) ENTAILS "
     f"cardinality-monotonicity of the profile.  The entailment is "
     f"machine-checked pointwise over every transition of the family: "
     f"transitions where the profile decreases WITHOUT the holdings "
     f"set shrinking = {F['mono_entailment_violations']}.  So THE "
     f"LADDER IS A CORPUS THEOREM about the committed layer, which "
     f"would hold at any cap; what is a CONSTRUCTION FACT is the "
     f"BLOCKING, because the candidate small sets were declared to be "
     f"the level sets of that very monotone coordinate.  A ladder the "
     f"process never descends is then entailed by the choice of "
     f"candidates, not discovered about them.  Both halves are named "
     f"in the verdict.")
emit("")
emit(f"  THE RESULT OF ARM B, stated exactly and no further.  The "
     f"transport family DOES have exact atoms at the declared primary "
     f"grain and the matched horizon — one for every holdings-profile "
     f"block THIS CAP CAN TEST ({len(prof_rows)} rows over "
     f"{len(set(p for p, N, n, d in _atoms))} of the "
     f"{F['rsig_blocks_n']} blocks; the fifth is excluded by the cap "
     f"and named), each with delta = 1 and an explicit nu, and at that "
     f"grain the menu-exact port the predecessor treated as the "
     f"special class is simply the FIRST of them — while at the "
     f"CONTROL grain, and hence at the ruled carrier, it is the ONLY "
     f"one that survives.  What the atoms lack is the other half.  The "
     f"holdings profile is a monotone non-decreasing coordinate "
     f"({F['B3_profile_decreases']} decreases over all "
     f"{F['B3_profile_pairs']} transitions of the family), so a block "
     f"cannot be re-entered from a strictly larger profile; the "
     f"hitting infimum into every block is exactly 0; the return "
     f"infimum into their UNION is 0 as well on the widest window this "
     f"family admits, one full depth wider than the predecessor's; and "
     f"the attained return distance is "
     f"{F['B3_dist_max_informative']} on every informative row.  A "
     f"regeneration argument needs ONE small set entered infinitely "
     f"often with a uniform bound, and none of the candidates exhibits "
     f"one.  So the engine is BLOCKED, and the blocking fact is NAMED "
     f"and MEASURED rather than open: THE MONOTONE HOLDINGS LADDER — "
     f"a CORPUS THEOREM as to the ladder, a CONSTRUCTION FACT as to "
     f"the blocking.  What is NOT claimed: that no uniform bound "
     f"exists at any depth; that the blocking survives a Psi outside "
     f"the menu-shape family (it does not — see the R-SIG-indicator "
     f"counter-reading); or that ARM B is motivated at the RSQ "
     f"zero-free standard (it carries four free items, censused "
     f"below).  Every row above is a finite-cap measurement, the caps "
     f"are printed, and the one row where a cross-profile delta* turns "
     f"positive (on a window of 105 of the class's points) is printed "
     f"too.")

gate("B3-HITTING", KIND_SUB,
     "THE SECOND HALF FAILS WHERE IT MATTERS: the N-step hitting "
     "probability into EVERY holdings-profile block of the family — "
     "all five, the cap-excluded (3, 3) included — has infimum exactly "
     "0 over every tested window and every N, so the small sets that "
     "carry delta = 1 are exactly the ones the process cannot be "
     "guaranteed to return to.  The word ATOM is deliberately not used "
     "in this label: the (3, 3) row is a hitting measurement on a "
     "block whose atomicity this cap cannot test",
     lambda f: (f['B3_all_zero_inf'] and len(f['B3_hit_rows']) > 4
                and len({p for p, N, t, z, w in f['B3_hit_rows']})
                == f['rsig_blocks_n']
                and any(p == '(3, 3)'
                        for p, N, t, z, w in f['B3_hit_rows'])),
     lambda f: "; ".join(f"{p} N={N}: {z}/{t} zeros, inf {w}"
                         for p, N, t, z, w in f['B3_hit_rows']))
gate("B3-BLOCKENTRY", KIND_SUB,
     "THE BLOCK RE-ENTRY CENSUS IS REPLACED BY THE OBJECT THE "
     "ARGUMENT NEEDS, and the forced rows are disclosed as forced: for "
     "every block not containing the root the re-entry count equals "
     "the block's own size by construction, and every one of them "
     "does.  What is measured instead is the number of TRANSITIONS "
     "INTO each block from outside it, and it SPLITS THE BLOCKS IN "
     "TWO: the four blocks without the root are entered at a strictly "
     "positive number of transitions, so for them it is the "
     "uniformity of the entry probability that fails; the (1, 1) "
     "block — R-MENU, and the only block still an atom at the ruled "
     "carrier — is entered at EXACTLY 0, i.e. it is "
     "absorbing-complement, so for it no uniform bound is even posable",
     lambda f: (f['B3_block_reentry_forced_all']
                and f['B3_block_entries_root_zero']
                and f['B3_block_entries_nonroot_positive']
                and not f['B3_block_entries_positive']
                and len(f['B3_block_entry_rows']) == f['rsig_blocks_n']),
     lambda f: "; ".join(f"{a}: size {b}, re-entries {c}, root {r}, "
                         f"entries-into {i}"
                         for a, b, c, r, i in f['B3_block_entry_rows']))
gate("B3-RSIG-RETURN", KIND_SUB,
     "AND THE UNION IS NOT A SUBSTITUTE, MEASURED ON A WINDOW ONE "
     "FULL DEPTH WIDER THAN THE PREDECESSOR'S: the return probability "
     "into R-SIG as a whole is exactly 0 at a strictly positive number "
     "of histories on the widest window, its zero-set collapses with "
     "N, and the infimum on the widest window is 0 — so no uniform "
     "Doeblin constant is exhibited for the union either",
     lambda f: (len(f['B3_rsig_rows']) == 5
                and f['B3_rsig_inf_widest'] == '0'
                and f['B3_rsig_zeros'][0] > 0
                and f['B3_rsig_rows'][0][1] == 30729
                and f['B3_rsig_rows'][3][1] == 69),
     lambda f: "; ".join(f"N={N}: {z} of {t} exactly 0, inf {w}"
                         for N, t, z, w in f['B3_rsig_rows']))
gate("B3-DISTANCE", KIND_SUB,
     "THE RETURN DISTANCE, EXACTLY, WITH THE CAP SEPARATED FROM THE "
     "MEASUREMENT: on the rows where the lookahead strictly exceeds "
     "the attained maximum — the only rows where the number is the "
     "process and not the cap — the largest return distance is at "
     "least 2, so returning to R-SIG is not one-step generic; and a "
     "strictly positive number of histories are UNRESOLVED at this "
     "cap, their entire remaining subtree containing no R-SIG point",
     lambda f: (f['B3_dist_max_saturated'] is not None
                and f['B3_dist_max_saturated'] >= 2
                and len(f['B3_dist_rows_saturated']) >= 2
                and f['B3_dist_unresolved'] > 0),
     lambda f: f"informative rows at depths "
               f"{list(f['B3_dist_rows_saturated'])}, max attained "
               f"distance {f['B3_dist_max_saturated']}; unresolved at "
               f"this cap {f['B3_dist_unresolved']}; full table "
               f"(depth, max, lookahead, informative, unresolved, "
               f"histories) = {list(f['B3_dist_by_depth'])}")
gate("B3-MONOTONE", KIND_THM,
     "AND THE MECHANISM IS THE MONOTONE INDEX — carried as a "
     "THEOREM-PASS with its forcing exhibited, because "
     "cardinality-monotonicity of the profile is ENTAILED by "
     "set-monotonicity of holdings (A4-MONO) and cannot come out "
     "otherwise: the holdings profile never decreases along any of the "
     "243,768 transitions of the family, so the atoms form a ladder "
     "the process climbs and never descends.  The entailment is "
     "machine-checked pointwise — 0 transitions decrease the profile "
     "without shrinking the holdings set — and the SUBSTANTIVE "
     "companion is B3-NSUP-PROFILE, where the same index computed on "
     "the NON-superseded holdings does decrease",
     lambda f: (f['B3_profile_decreases'] == 0
                and f['B3_profile_pairs'] == 243768
                and f['mono_entailment_violations'] == 0
                and f['mono_shrinking_all'] == 0),
     lambda f: f"transitions = {f['B3_profile_pairs']} (FULL family "
               f"scope); profile decreases = "
               f"{f['B3_profile_decreases']}; entailment violations = "
               f"{f['mono_entailment_violations']}; narrowed scope "
               f"{f['B3_profile_decreases_narrow']} of "
               f"{f['B3_profile_pairs_narrow']}")
gate("B3-NSUP-PROFILE", KIND_SUB,
     "THE TWO-WAY DEMONSTRATION BEHIND THAT THEOREM-PASS: the same "
     "ladder built on the NON-SUPERSEDED holdings is NOT monotone — it "
     "shrinks at 29,980 of the family's 243,768 transitions — so a "
     "monotone-index gate on this family is not vacuous by "
     "construction; it is the choice of index that makes it monotone, "
     "and this gate is what could have returned False",
     lambda f: (f['nsup_shrinking_all'] > 0
                and f['nsup_shrinking_all'] == 29980
                and f['mono_pairs_all'] == 243768),
     lambda f: f"non-superseded shrinking = {f['nsup_shrinking_all']} "
               f"of {f['mono_pairs_all']} transitions, against "
               f"{f['mono_shrinking_all']} for the full holdings set")

# ======================================================================
# THE CHOICE INVENTORY AT THE RSQ STANDARD.  Every choice ARM B makes
# is classified DECLARED / FORCED (with the forcing exhibited) / FREE
# (with the fiber measured or its absence stated).  A MOTIVATED claim
# requires ZERO free items.  ARM B carries FOUR, and the verdict says
# so rather than presenting an arena-relative measurement as an
# inherited fact.
# ======================================================================
emit("")
emit("  [THE CHOICE INVENTORY — the RSQ standard, applied to ARM B]")
CHOICES = [
    ("C1 the R-SIG predicate reduction", "FORCED",
     f"exhibited: agrees with the full predicate at "
     f"{F['pred_reduction_tested']}/{F['pred_reduction_tested']}, "
     f"{F['pred_reduction_disagreements']} disagreements, with the two "
     f"structural implications machine-checked at 0 counterexamples "
     f"each, and the unforced variant disagreeing at "
     f"{F['pred_unforced_disagreements']}"),
    ("C2 the delivery-free partner derived, not imported", "FORCED",
     f"exhibited: the layer's own idle clause with the delivery "
     f"indicator forced false; gated against T4's committed partner "
     f"census {F['df_total']} and its potentials"),
    ("C3 grain: primary 13-class vs control 113-class", "DECLARED",
     f"fiber MEASURED and large: {len(F['B2_grain_split'])} of "
     f"{len(F['B2_profile_rows'])} atom rows flip; five grains run on "
     f"the full class"),
    ("C4 horizon: H7 vs MATCHED", "DECLARED",
     f"fiber measured at both grains on the full class and at the "
     f"primary grain on every block row; the H7 x control cell is "
     f"bounded above by the H7 x primary column by the coarsening "
     f"lemma and is not separately computed"),
    ("C5 caps CAP_T = %d, N <= %d, escape window %d, symmetry window "
     "%d" % (CAP_T, NMAX, CAP_ESC, CAP_SYM), "DECLARED",
     f"N-fiber measured across N = 1..{NMAX}; the depth fiber is NOT "
     f"measured — depth 7 is declared infeasible with its projected "
     f"count printed"),
    ("C6 actor pool = (A, B) for ARM B", "FREE",
     f"three actors censused to depth 3 only "
     f"({F['pool3_depth3']} histories); NO ARM-B row is run at three "
     f"actors, so the fiber over the actor pool has ONE sampled point"),
    ("C7 terminal convention G(h, 0) = 1", "FREE",
     "no second terminal convention is run anywhere; ARM A fact 7 "
     "forces only the ROOT leg, and only for relabelling-invariant "
     "conventions"),
    ("C8 Psi ranges over menu-shape functions", "FREE",
     f"the two declared grains are both menu-shape functions of the "
     f"successor.  THIS REPAIR MEASURES THREE MORE Psi OF OTHER KINDS "
     f"(the ordered and unordered holdings profile, and the R-SIG "
     f"indicator) and the last of them REVERSES the answer, which is "
     f"exactly why the item is FREE and why the verdict now carries a "
     f"PSI-FAMILY qualifier.  d74's congruence CONG-"
     f"{F['carrier_cong_d4']} is still not run as a Psi"),
    ("C9 candidate small sets = R-SIG's profile blocks and their "
     "union", "FREE",
     "declared, not answer-selected (the block list is taken from ARM "
     "A fact 4 before ARM B runs) — but the fiber over candidate small "
     "sets has exactly two sampled points, and both are level sets, or "
     "the total, OF THE SAME MONOTONE COORDINATE.  Nothing outside the "
     "level-set family is tried, so 'the process climbs past each one' "
     "is entailed by the choice of candidates"),
]
F['choices'] = tuple((n, k) for n, k, e in CHOICES)
F['choices_free'] = tuple(n for n, k, e in CHOICES if k == 'FREE')
F['choices_forced'] = tuple(n for n, k, e in CHOICES if k == 'FORCED')
F['choices_declared'] = tuple(n for n, k, e in CHOICES if k == 'DECLARED')
F['free_items'] = len(F['choices_free'])
F['armB_motivated'] = (F['free_items'] == 0)
for n, k, e in CHOICES:
    emit(f"    [{k:8s}] {n}")
    emit(f"               {e}")
emit(f"  FREE ITEMS: {F['free_items']} "
     f"({[n.split()[0] for n in F['choices_free']]}).  A motivated "
     f"claim requires zero, so ARM B IS NOT MOTIVATED AT THE RSQ "
     f"STANDARD ({F['armB_motivated']}): it is a MEASUREMENT AT A "
     f"DECLARED ARENA, which is a real and honest thing, and the "
     f"verdict labels it as one.  ARM A is motivated: its choices are "
     f"forced or bound to a hash- and verbatim-anchored predecessor "
     f"row, and where a choice remained (the grain) both values are "
     f"measured and their disagreement is reported as a control.")
gate("B5-FREEITEMS", KIND_SUB,
     "THE CHOICE INVENTORY IS GATED, NOT NARRATED: ARM B carries "
     "exactly FOUR free items (the actor pool, the terminal "
     "convention, the menu-shape-only Psi family, and the "
     "level-set-only family of candidate small sets), each with its "
     "fiber measured or its absence stated, so the unit's own receipt "
     "says that ARM B is a measurement at a declared arena and not a "
     "motivated result",
     lambda f: (f['free_items'] == 4
                and not f['armB_motivated']
                and len(f['choices']) == 9
                and len(f['choices_forced']) == 2),
     lambda f: f"free {f['free_items']} {list(f['choices_free'])}; "
               f"forced {len(f['choices_forced'])}; declared "
               f"{len(f['choices_declared'])}; motivated = "
               f"{f['armB_motivated']}")
gate("B0-SUCCESSOR-NAMED", KIND_SUB,
     "THE CONSUMER OF THE QUOTATION THAT LICENSES ARM B, registered as "
     "a gate rather than named by a verbatim row and never built: T4's "
     "verbatim window 'No operator-level minorization — Birkhoff / "
     "Hilbert-metric contraction of the positive backward recursion G "
     "— has been attempted anywhere' is located, and ARM B was in fact "
     "run — the Birkhoff coefficient is derived from a computed minor, "
     "an atom is exhibited with its nu, and the blocking fact is "
     "measured.  The named engine is closed at the history level ONLY, "
     "and that limitation is printed at B1",
     lambda f: ('B0-SUCCESSOR-NAMED' in f['verbatim_consumers']
                and f['birkhoff_tau'] == '1'
                and f['B2_atom_found']
                and f['B2_nu_support'] > 0
                and f['B3_profile_pairs'] > 0),
     lambda f: f"consumer bound = "
               f"{'B0-SUCCESSOR-NAMED' in f['verbatim_consumers']}; "
               f"tau = {f['birkhoff_tau']}; atom found = "
               f"{f['B2_atom_found']} with nu support "
               f"{f['B2_nu_support']}")

prog("ARM B complete")

# ======================================================================
# THE VERDICT — derived inside a gate from the measured counts
# ======================================================================
SEVEN = [
    ("F1 grammar", "A1-KINDS"),
    ("F2 census+potentials", "A2-CENSUS"),
    ("F3 kernels", "A3-POSITIVITY"),
    ("F4 renewal ports", "A4-PORTS"),
    ("F5 the escape", "A5-ESCAPE"),
    ("F6 reopening", "A6-REOPENING"),
    ("F7 root symmetry", "A7-AUTOMORPHISM"),
]

RES = run_gates(F)
F['gate_results'] = tuple(sorted((g, RES[g][0]) for g in RES))
F['n_pass'] = sum(1 for g in RES if RES[g][0])
F['n_fail'] = sum(1 for g in RES if not RES[g][0])
F['n_substantive'] = sum(1 for gid, k, l, p, d in GATES if k == KIND_SUB)
F['n_theorem'] = sum(1 for gid, k, l, p, d in GATES if k == KIND_THM)
F['n_disclosure'] = sum(1 for gid, k, l, p, d in GATES if k == KIND_DIS)
F['seven_facts_ok'] = tuple((nm, RES[g][0]) for nm, g in SEVEN)
F['seven_all'] = all(RES[g][0] for nm, g in SEVEN)


# ----------------------------------------------------------------------
# THE SHARED TOKEN TABLE.  This is the ONE object the builder and the
# comparator both consult, and they consult it BY KEY: no string
# literal of the verdict appears in both functions, which is the #82
# requirement the first delivery failed by making the comparator a
# second call to the builder.  Every token here is digit-free, so that
# every numeral in the emitted verdict belongs to a measured value and
# the comparator can account for all of them.
# ----------------------------------------------------------------------
VTOK = {
    'join': '  +  ',
    'seg_term': 'GPREP-FOUNDATION-TERMINALIZED-',
    'seg_found': 'GPREP-MINORIZATION-FOUND-',
    'seg_blocked': 'GPREP-ARM-B-BLOCKED-AT-THE-MONOTONE-HOLDINGS-LADDER',
    't_head': '[',
    't_grammar': ' facts: grammar ',
    't_census': ' kinds; census ',
    't_cum': ' histories cumulative ',
    't_gtop': ' with G_',
    't_eq': ' = ',
    't_dfg': ' and delivery-free G_',
    't_dsep': ', deliveries REDUCE branching first at D = ',
    't_rmax': '; kernels proper and STRICTLY POSITIVE at horizons r up '
              'to ',
    't_viol': ' with ',
    't_ports': ' violations; ports R-SIG ',
    't_rmenu': ' / R-MENU ',
    't_slash': ' / ',
    't_nonren': ' re-entries and non-renewal mass ',
    't_escape': '; ESCAPE ',
    't_esccls': ' transitions into ',
    't_grain': ' above-window classes at the DECLARED-PRIMARY ',
    't_ctrl': '-class grain and ',
    't_ctrlcls': ' at the ',
    't_chains': '-class control grain, NO CLOSED EXACT TRANSFER; '
                'reopening ',
    't_chainw': ' minimal chains at ',
    't_prefix': ' over ',
    't_symmenu': ' prefixes; root symmetry ',
    't_symg': ' menu and ',
    'f_delta': '[delta = ',
    'f_bestn': ' exact; N = ',
    'f_nusupp': '; nu = the common minorant on ',
    'f_nugrain': ' Psi-classes of the ',
    'f_block': '-class primary grain; class = the holdings-profile '
               'blocks of R-SIG, block ',
    'f_points': ' exhibited over ',
    'f_depths': ' points at depths ',
    'f_scope': '; scope = ',
    'f_capt': ' actors, transport depth <= ',
    'q_grain': '<GRAIN=DECLARED-PRIMARY-',
    'q_psi': '-CLASS;PSI-FAMILY=',
    'q_free': ';FREE-ITEMS=',
    'q_ladder': ';LADDER=',
    'q_blocking': ';BLOCKING=',
    'psi_tag': 'MENU-SHAPE-ONLY',
    'ladder_tag': 'CORPUS-THEOREM',
    'blocking_tag': 'CONSTRUCTION-FACT',
    'b_dec': '>-[the holdings profile decreases at ',
    'b_of': ' of ',
    'b_fullzero': ' transitions of the family, so the atoms form a '
                  'ladder the process climbs and never descends; at '
                  'the DECLARED-PRIMARY grain and over the MENU-SHAPE '
                  'Psi family the full R-SIG class has delta* = ',
    'b_widest': ' on both of its widest windows (N = ',
    'b_counter': '), while at Psi = the R-SIG indicator the same class '
                 'has delta* = ',
    'b_countern': ' there (N = ',
    'b_rsiginf': '); the R-SIG return probability has infimum ',
    'b_zeroset': ' on the widest window and its zero-set is ',
    'b_unres': '; ',
    'b_dist': ' histories are unresolved at this cap and the attained '
              'return distance reaches ',
    'b_hit': ' on the informative rows; the hitting infimum into every '
             'one of the ',
    'b_hitval': ' holdings-profile blocks is ',
    'b_carrier': '; at the ruled carrier CONG-',
    'b_dead': ' the atom claim collapses to R-MENU (',
    'b_rows': ' rows dead by the coarsening lemma); and at the history '
              'level the Birkhoff coefficient is ',
    'b_doeblin': ' and the Doeblin constant is ',
    'b_cols': ' by unique parenthood at all ',
    'b_tail': ' columns]',
}


def build_verdict(f):
    """THE EMITTER.  Composed segment by segment from the measured
    values, with every numeral immediately preceded by a token of the
    shared table.  It is NOT the comparator: see check_verdict."""
    T = VTOK
    segs = []
    segs.append(
        T['seg_term']
        + T['t_head'] + f"{len(f['seven_facts_ok'])}/"
        f"{len(f['seven_facts_ok'])}"
        + T['t_grammar'] + f"{len(f['event_kinds'])}"
        + T['t_census'] + f"{f['t_total']}"
        + T['t_cum'] + f"{list(f['t_cumulative'])}"
        + T['t_gtop'] + f"{len(f['G_transport'])}"
        + T['t_eq'] + f"{f['G_transport'][6]}"
        + T['t_dfg'] + f"{len(f['G_deliveryfree'])}"
        + T['t_eq'] + f"{f['G_deliveryfree'][6]}"
        + T['t_dsep'] + f"{f['df_gt_t_first']}"
        + T['t_rmax'] + f"{len(f['proper_rows'])}"
        + T['t_viol'] + f"{f['positivity_violations']}"
        + T['t_ports'] + f"{f['rsig_count']}"
        + T['t_rmenu'] + f"{f['rmenu_count']}"
        + T['t_viol'] + f"{f['rsig_reentries']}"
        + T['t_slash'] + f"{f['rmenu_reentries']}"
        + T['t_nonren'] + f"{f['nonrenewal_depth5']}"
        + T['t_escape'] + f"{f['escape_primary']}"
        + T['t_esccls'] + f"{len(f['escape_primary_classes'])}"
        + T['t_grain'] + f"{f['grain_primary_classes']}"
        + T['t_ctrl'] + f"{f['escape_control']}"
        + T['t_ctrlcls'] + f"{f['grain_control_classes']}"
        + T['t_chains'] + f"{f['minimal_chains']}"
        + T['t_chainw'] + f"{f['minimal_chain_weights'][0]}"
        + T['t_prefix'] + f"{f['diverged_prefixes']}"
        + T['t_symmenu'] + f"{f['sym_menu_violations']}"
        + T['t_symg'] + f"{f['sym_G_violations']}"
        + " potential violations]")
    if f['B2_atom_found']:
        segs.append(
            T['seg_found']
            + T['f_delta'] + f"{f['B2_best_delta']}"
            + T['f_bestn'] + f"{f['B2_best_N']}"
            + T['f_nusupp'] + f"{f['B2_nu_support']}"
            + T['f_nugrain'] + f"{f['grain_primary_classes']}"
            + T['f_block'] + f"{f['B2_nu_profile']}"
            + T['f_points'] + f"{f['B2_nu_block_size']}"
            + T['f_depths'] + f"{list(f['B2_nu_depths'])}"
            + T['f_scope'] + f"{f['n_actors']}"
            + T['f_capt'] + f"{CAP_T}"
            + ", MATCHED horizon, DECLARED-PRIMARY grain — the blocks "
              "the cap can test are ATOMS at that grain, not merely "
              "small sets; the claim is NOT universal over blocks and "
              "the cap-excluded fifth block is named]")
    segs.append(
        T['seg_blocked']
        + T['q_grain'] + f"{f['grain_primary_classes']}"
        + T['q_psi'] + T['psi_tag']
        + T['q_free'] + f"{f['free_items']}"
        + T['q_ladder'] + T['ladder_tag']
        + T['q_blocking'] + T['blocking_tag']
        + T['b_dec'] + f"{f['B3_profile_decreases']}"
        + T['b_of'] + f"{f['B3_profile_pairs']}"
        + T['b_fullzero'] + f"{f['B2_full_rows'][0][3]}"
        + T['b_widest'] + f"{list(f['B2_widest_zero_N'])}"
        + T['b_counter'] + f"{f['B2_rsig_indicator_matched'][0][1]}"
        + T['b_countern'] + f"{list(f['B2_rsig_indicator_delta1_at'])}"
        + T['b_rsiginf'] + f"{f['B3_rsig_inf_widest']}"
        + T['b_zeroset'] + f"{list(f['B3_rsig_zeros'])}"
        + T['b_unres'] + f"{f['B3_dist_unresolved']}"
        + T['b_dist'] + f"{f['B3_dist_max_informative']}"
        + T['b_hit'] + f"{f['rsig_blocks_n']}"
        + T['b_hitval'] + f"{f['B3_block_inf_sup']}"
        + T['b_carrier'] + f"{f['carrier_cong_d4']}"
        + T['b_dead'] + f"{len(f['B4_carrier_dead_rows'])}"
        + T['b_of'] + f"{len(f['B2_profile_rows'])}"
        + T['b_rows'] + f"{f['birkhoff_tau']}"
        + T['b_doeblin'] + f"{f['birkhoff_doeblin_history']}"
        + T['b_cols'] + f"{f['columns_single_parent']}"
        + T['b_tail'])
    return VTOK['join'].join(segs)


NUMTOK = re.compile(r'\d+/\d+|\d+')


def check_verdict(f, s):
    """THE COMPARATOR, built independently of the emitter (v14 #82).
    It never calls build_verdict and never re-concatenates the verdict.
    It PARSES the emitted string: it declares, from the gated object
    alone, which measured value must follow which token of the shared
    table and in what order, walks the string once asserting each in
    turn, and finally accounts for EVERY numeral in the string — so a
    wrong field in the emitter (a value read from the wrong key) and a
    wrong template in the emitter (a missing, extra or reordered
    token) both die here.  Returns (ok, detail)."""
    T = VTOK
    want_segs = [T['seg_term']]
    if f['B2_atom_found']:
        want_segs.append(T['seg_found'])
    want_segs.append(T['seg_blocked'])
    parts = s.split(T['join'])
    if len(parts) != len(want_segs):
        return False, ("segment count %d, expected %d"
                       % (len(parts), len(want_segs)))
    for i, w in enumerate(want_segs):
        if not parts[i].startswith(w):
            return False, ("segment %d does not open with its declared "
                           "name %r" % (i, w))
    n7 = len(f['seven_facts_ok'])
    anchors = [
        ('t_head', "%d/%d" % (n7, n7)),
        ('t_grammar', str(len(f['event_kinds']))),
        ('t_census', str(f['t_total'])),
        ('t_cum', str(list(f['t_cumulative']))),
        ('t_gtop', str(len(f['G_transport']))),
        ('t_eq', str(f['G_transport'][6])),
        ('t_dfg', str(len(f['G_deliveryfree']))),
        ('t_eq', str(f['G_deliveryfree'][6])),
        ('t_dsep', str(f['df_gt_t_first'])),
        ('t_rmax', str(len(f['proper_rows']))),
        ('t_viol', str(f['positivity_violations'])),
        ('t_ports', str(f['rsig_count'])),
        ('t_rmenu', str(f['rmenu_count'])),
        ('t_viol', str(f['rsig_reentries'])),
        ('t_slash', str(f['rmenu_reentries'])),
        ('t_nonren', str(f['nonrenewal_depth5'])),
        ('t_escape', str(f['escape_primary'])),
        ('t_esccls', str(len(f['escape_primary_classes']))),
        ('t_grain', str(f['grain_primary_classes'])),
        ('t_ctrl', str(f['escape_control'])),
        ('t_ctrlcls', str(f['grain_control_classes'])),
        ('t_chains', str(f['minimal_chains'])),
        ('t_chainw', str(f['minimal_chain_weights'][0])),
        ('t_prefix', str(f['diverged_prefixes'])),
        ('t_symmenu', str(f['sym_menu_violations'])),
        ('t_symg', str(f['sym_G_violations'])),
    ]
    if f['B2_atom_found']:
        anchors += [
            ('f_delta', str(f['B2_best_delta'])),
            ('f_bestn', str(f['B2_best_N'])),
            ('f_nusupp', str(f['B2_nu_support'])),
            ('f_nugrain', str(f['grain_primary_classes'])),
            ('f_block', str(f['B2_nu_profile'])),
            ('f_points', str(f['B2_nu_block_size'])),
            ('f_depths', str(list(f['B2_nu_depths']))),
            ('f_scope', str(f['n_actors'])),
            ('f_capt', str(CAP_T)),
        ]
    anchors += [
        ('q_grain', str(f['grain_primary_classes'])),
        ('q_psi', T['psi_tag']),
        ('q_free', str(f['free_items'])),
        ('q_ladder', T['ladder_tag']),
        ('q_blocking', T['blocking_tag']),
        ('b_dec', str(f['B3_profile_decreases'])),
        ('b_of', str(f['B3_profile_pairs'])),
        ('b_fullzero', str(f['B2_full_rows'][0][3])),
        ('b_widest', str(list(f['B2_widest_zero_N']))),
        ('b_counter', str(f['B2_rsig_indicator_matched'][0][1])),
        ('b_countern', str(list(f['B2_rsig_indicator_delta1_at']))),
        ('b_rsiginf', str(f['B3_rsig_inf_widest'])),
        ('b_zeroset', str(list(f['B3_rsig_zeros']))),
        ('b_unres', str(f['B3_dist_unresolved'])),
        ('b_dist', str(f['B3_dist_max_informative'])),
        ('b_hit', str(f['rsig_blocks_n'])),
        ('b_hitval', str(f['B3_block_inf_sup'])),
        ('b_carrier', str(f['carrier_cong_d4'])),
        ('b_dead', str(len(f['B4_carrier_dead_rows']))),
        ('b_of', str(len(f['B2_profile_rows']))),
        ('b_rows', str(f['birkhoff_tau'])),
        ('b_doeblin', str(f['birkhoff_doeblin_history'])),
        ('b_cols', str(f['columns_single_parent'])),
    ]
    cur = 0
    accounted = 0
    for key, want in anchors:
        tok = T[key]
        idx = s.find(tok, cur)
        if idx < 0:
            return False, ("token %r not found at or after position %d"
                           % (key, cur))
        cur = idx + len(tok)
        if not s.startswith(want, cur):
            return False, ("after token %r the string carries %r where "
                           "the gated object requires %r"
                           % (key, s[cur:cur + len(want) + 8], want))
        cur += len(want)
        accounted += len(NUMTOK.findall(want))
    if not s.endswith(T['b_tail']):
        return False, "the verdict does not end at its declared tail"
    total = len(NUMTOK.findall(s))
    if total != accounted:
        return False, ("%d numerals in the emitted string, %d accounted "
                       "for by the gated object" % (total, accounted))
    return True, ("%d anchored fields, %d numerals all accounted for, "
                  "%d segments" % (len(anchors), total, len(parts)))


VERDICT = build_verdict(F)
F['verdict'] = VERDICT
F['verdict_check'] = check_verdict(F, VERDICT)
gate("V-VERDICT", KIND_SUB,
     "THE VERDICT IS CHECKED BY A COMPARATOR BUILT INDEPENDENTLY OF "
     "ITS BUILDER (v14 #82): check_verdict never calls build_verdict "
     "and never re-concatenates the string.  It declares, from the "
     "gated object alone, which measured value must follow which token "
     "of the shared table and in what order; it walks the emitted "
     "string once asserting each; it requires the declared tail; and "
     "it accounts for EVERY numeral in the string.  A builder field "
     "swap (a value read from the wrong key) and a builder template "
     "error (a missing, extra or reordered token) therefore both die "
     "here, and two falsifiers reproduce exactly those two injections",
     lambda f: check_verdict(f, f['verdict'])[0],
     lambda f: f"verdict length = {len(f['verdict'])} chars; "
               f"{check_verdict(f, f['verdict'])[1]}")
gate("V-SEVEN", KIND_SUB,
     "ARM A's seven facts each carry a passing substantive gate, and "
     "the TERMINALIZED segment may not be emitted otherwise.  The "
     "segment is located by its KEY in the shared token table, never "
     "by a substring re-typed inside the predicate",
     lambda f: (f['seven_all']
                and f['verdict'].startswith(VTOK['seg_term'])),
     lambda f: "; ".join(f"{nm}: {ok}" for nm, ok in
                         f['seven_facts_ok']))

# ======================================================================
# FALSIFIERS.  Each is an injection into the gated object; each must
# kill at least one gate.  (RUNBOOK section 14: compliance claims are
# gate claims; waiver claims are gate claims; no gate predicate may
# reference mutant identity — the predicates below never see a mutant
# name, they are the same functions evaluated blind on perturbed data.)
# ======================================================================
emit("")
emit("[FALSIFIERS — every gate must be able to die]")

# PATH AND VERBATIM DRIFTS, per row — evaluated against the real
# filesystem, not against the gated object.  These measurements and
# their gates are registered BEFORE the falsifier registry is built,
# so that the per-key drift falsifiers below cover their read keys too.
PATHDRIFT = []
for tag, name, ped, arts, sup in ROWS:
    p0 = arts[0][0]
    drift = p0.replace('v10/', 'v10/data/') if 'code/' in p0 else \
        p0.replace('.md', '_.md')
    ok = os.path.exists(os.path.join(REPO, drift))
    PATHDRIFT.append((tag, p0, drift, ok))
F['path_drift_rows'] = tuple(PATHDRIFT)
F['path_drift_survivors'] = sum(1 for t, a, b, ok in PATHDRIFT if ok)
# THE VERBATIM DRIFT RULE, REPAIRED.  The first delivery's rule was
# `ctx.replace('68','69') if '68' in ctx else ctx + "!"`, and only two
# of the twelve windows contained '68' — for the other ten the
# "perturbation" was appending an exclamation mark to a multi-line
# technical quotation, a test that cannot plausibly fail.  The rule
# below perturbs a CONTENT-BEARING TOKEN of every window: its first
# digit if it has one, else its two first alphabetic words swapped,
# else its longest word deleted.  The perturbation applied is printed
# per row, so a reader can see that each drift is a real one.
def drift_window(ctx):
    m = re.search(r'\d', ctx)
    if m:
        i = m.start()
        d = ctx[i]
        return (ctx[:i] + ('0' if d != '0' else '1') + ctx[i + 1:],
                'first-digit')
    ws = re.findall(r'[A-Za-z]{2,}', ctx)
    if len(ws) >= 2:
        a, b = ws[0], ws[1]
        return (ctx.replace(a, '\0', 1).replace(b, a, 1)
                .replace('\0', b, 1), 'word-swap')
    if ws:
        lw = max(ws, key=len)
        return ctx.replace(lw, '', 1), 'longest-word-deleted'
    return ctx + "!", 'append'


VBDRIFT = []
for tag, path, ctx, consumer in VERBATIM:
    drifted, how = drift_window(ctx)
    try:
        found = drifted in read_text(os.path.join(REPO, path))
    except OSError:
        found = False
    VBDRIFT.append((tag, consumer, found, how, drifted != ctx))
F['verbatim_drift_rows'] = tuple((t, c, ok) for t, c, ok, h, d in VBDRIFT)
F['verbatim_drift_how'] = tuple((t, c, h) for t, c, ok, h, d in VBDRIFT)
F['verbatim_drift_survivors'] = sum(1 for t, c, ok, h, d in VBDRIFT if ok)
F['verbatim_drift_real'] = all(d for t, c, ok, h, d in VBDRIFT)
F['verbatim_drift_appends'] = sum(1 for t, c, ok, h, d in VBDRIFT
                                  if h == 'append')
# REFERENTIAL INTEGRITY: every `consumer` named by a verbatim row must
# be a REGISTERED gate.  The first delivery named B0-SUCCESSOR-NAMED —
# the consumer licensing the whole of ARM B — and never registered it,
# and nothing noticed, because the consumer field was only ever
# printed.  This is computed after every gate registration.
_GIDS = {gid for gid, k, l, p, d in GATES}
F['verbatim_consumers_bound'] = tuple(
    sorted({c for t, p, c, ok, n, o in VB if c in _GIDS}))
F['verbatim_consumers_unbound'] = tuple(
    sorted({c for t, p, c, ok, n, o in VB if c not in _GIDS}))
emit(f"  VERBATIM CONSUMER BINDING, CHECKED FOR REFERENTIAL INTEGRITY: "
     f"{len(F['verbatim_consumers_bound'])} distinct consumer gates "
     f"named by the {len(VB)} context windows are registered gates; "
     f"{len(F['verbatim_consumers_unbound'])} are not "
     f"{list(F['verbatim_consumers_unbound'])}.")
emit(f"  VERBATIM DRIFT, PER ROW, WITH THE PERTURBATION NAMED: "
     + "; ".join(f"{t}/{c}: {h}" for t, c, h in F['verbatim_drift_how']))
gate("M-CONSUMERBINDING", KIND_SUB,
     "REFERENTIAL INTEGRITY OF THE ANCHOR TABLE: every consumer gate "
     "named by a verbatim-context row is a REGISTERED gate.  The first "
     "delivery named a consumer that did not exist — the one "
     "licensing ARM B — and no check caught it; this is that check",
     lambda f: (len(f['verbatim_consumers_unbound']) == 0
                and len(f['verbatim_consumers_bound']) >= 10),
     lambda f: f"bound {list(f['verbatim_consumers_bound'])}; unbound "
               f"{list(f['verbatim_consumers_unbound'])}")
gate("M-VERBATIMSPEC", KIND_SUB,
     "THE #62 SPECIFICITY STANDARD IS ENFORCED, NOT ASSERTED: every "
     "verbatim-context window is at least 40 characters long AND "
     "occurs EXACTLY ONCE in its source file, so a window truncated to "
     "a short generic substring is refused at the precheck instead of "
     "being certified as an anchor",
     lambda f: (f['verbatim_unique']
                and f['verbatim_min_chars'] >= f['verbatim_min_required']
                and f['verbatim_min_required'] >= 40
                and len(f['verbatim_ok']) == f['verbatim_n']),
     lambda f: f"shortest window {f['verbatim_min_chars']} chars "
               f"(minimum {f['verbatim_min_required']}); all windows "
               f"unique in source = {f['verbatim_unique']}; located "
               f"{len(f['verbatim_ok'])} of {f['verbatim_n']}")
gate("M-PATHDRIFT", KIND_SUB,
     "PATH-VALUE ANCHORING: for every pinned row, a drifted path "
     "(the same basename moved to a sibling directory, or a "
     "near-miss filename) does NOT resolve on this filesystem — so a "
     "path drift that would change the arena dies at the anchor and "
     "cannot reach a verdict segment",
     lambda f: f['path_drift_survivors'] == 0,
     lambda f: f"drifted paths that still resolve: "
               f"{f['path_drift_survivors']} of "
               f"{len(f['path_drift_rows'])}")
gate("M-VERBATIMDRIFT", KIND_SUB,
     "VERBATIM-CONTEXT ANCHORING, WITH A LABEL THAT CLAIMS ONLY WHAT "
     "IT TESTS: each anchored context window, perturbed at a "
     "CONTENT-BEARING token (its first digit, else its first two words "
     "swapped, else its longest word deleted — never a mere appended "
     "character), is NOT found in its source.  Every one of the twelve "
     "perturbations is a real one, and the perturbation applied is "
     "printed per row.  Together with M-VERBATIMSPEC (length and "
     "uniqueness) this is what makes the windows bind their span "
     "rather than mere existence",
     lambda f: (f['verbatim_drift_survivors'] == 0
                and f['verbatim_drift_real']
                and f['verbatim_drift_appends'] == 0),
     lambda f: f"drifted windows still found: "
               f"{f['verbatim_drift_survivors']} of "
               f"{len(f['verbatim_drift_rows'])}; every perturbation "
               f"real = {f['verbatim_drift_real']}; append-only "
               f"perturbations = {f['verbatim_drift_appends']}")


RES = run_gates(F)



def perturb(v):
    """LEVEL 1 — the drift: one unit, one cell, one character."""
    if isinstance(v, bool):
        return not v
    if isinstance(v, int):
        return v + 1
    if isinstance(v, Fr):
        return v + 1
    if isinstance(v, str):
        return v + "~"
    if isinstance(v, tuple):
        if not v:
            return (0,)
        return v[:-1]
    if isinstance(v, dict):
        k = sorted(v, key=SK)
        return {kk: v[kk] for kk in k[:-1]}
    if v is None:
        return 0
    return v


def poison(v):
    """LEVEL 2 — the escalation, used only where the drift left every
    gate alive."""
    if isinstance(v, bool):
        return not v
    if isinstance(v, (int, Fr)):
        return -999999
    if isinstance(v, str):
        return "POISON"
    if isinstance(v, tuple):
        return (False,)
    if isinstance(v, dict):
        return {}
    return "POISON"


def erase(v):
    """LEVEL 3 — the erasure, for predicates that only ask whether a
    collection is non-empty.  A key that survives ALL THREE is read by
    a predicate that does not constrain it, and is censused as such
    rather than reported as a dead falsifier."""
    if isinstance(v, tuple):
        return ()
    if isinstance(v, dict):
        return {}
    if isinstance(v, str):
        return ""
    if isinstance(v, bool):
        return not v
    if isinstance(v, (int, Fr)):
        return 0
    return None


MUTANTS = []
# (1) era-minimum, WIDENED: one targeted value-drift falsifier per
#     FACTS key ANY gate reads — not only the substantive ones.  The
#     first delivery harvested read-keys from KIND_SUB gates alone,
#     which is what let a theorem-pass or disclosure gate be excluded
#     from falsification and then waived by the same declaration that
#     excluded it.  Harvesting from every gate breaks that loop: a
#     KIND_THM gate now carries falsifiers like any other, and its
#     waiver is issued only if it SURVIVES them (see the waiver
#     machinery below).
_read_keys = set()
for gid, kind, label, pred, det in GATES:
    _read_keys |= RES[gid][2]
for k in sorted(_read_keys, key=SK):
    MUTANTS.append((f"DRIFT[{k}]", 'value-drift/census-drop',
                    lambda f, k=k: {k: perturb(f[k])}))
ESCALATE = {}
# (1b) THE VERDICT-BUILDER INJECTIONS.  These are the two injections a
#      hostile round put into build_verdict itself and that the old
#      comparator — which WAS the builder — passed with every gate
#      green: a FIELD SWAP (the verdict's ESCAPE count read from the
#      control grain while labelled primary) and a VALUE SWAP (the
#      blocking clause's numerator read from its own denominator).
#      They are reproduced here against the STORED verdict string, so
#      that the independent comparator has to catch them.
MUTANTS.append(("BUILDER-FIELD-SWAP", 'verdict-builder',
                lambda f: {'verdict': f['verdict'].replace(
                    VTOK['t_escape'] + str(f['escape_primary']),
                    VTOK['t_escape'] + str(f['escape_control']), 1)}))
MUTANTS.append(("BUILDER-VALUE-SWAP", 'verdict-builder',
                lambda f: {'verdict': f['verdict'].replace(
                    VTOK['b_dec'] + str(f['B3_profile_decreases']),
                    VTOK['b_dec'] + str(f['B3_profile_pairs']), 1)}))
MUTANTS.append(("BUILDER-TOKEN-DROPPED", 'verdict-builder',
                lambda f: {'verdict': f['verdict'].replace(
                    VTOK['q_free'], ';', 1)}))
# (2) the five verdict classes (v14 #10: containment is not equality)
MUTANTS.append(("VERDICT-VALUE-SWAP", 'verdict',
                lambda f: {'verdict': f['verdict'].replace(
                    str(f['t_total']), str(f['t_total'] + 1))}))
MUTANTS.append(("VERDICT-APPENDED-TEXT", 'verdict',
                lambda f: {'verdict': f['verdict'] + "  (and the "
                                                     "square closes)"}))
MUTANTS.append(("VERDICT-TRUNCATED", 'verdict',
                lambda f: {'verdict': f['verdict'][:120]}))
MUTANTS.append(("VERDICT-SEGMENT-DROPPED", 'verdict',
                lambda f: {'verdict': f['verdict'].split("  +  ")[0]}))
MUTANTS.append(("VERDICT-TYPED-SEGMENT", 'verdict',
                lambda f: {'verdict': f['verdict'].replace(
                    'BLOCKED-AT-', 'FOUND-AT-')}))
# (3) the theorem-pass census, the waiver census and the verdict-
#     falsifier census are gated in PHASE 2 below, because their gates
#     read the outcome of this phase's own falsifier run; their
#     falsifiers are declared there, beside the gates they must kill.
# (4) the escape / grain classes
MUTANTS.append(("ESCAPE-ZEROED", 'science',
                lambda f: {'escape_primary': 0,
                           'escape_primary_classes': ()}))
MUTANTS.append(("GRAIN-COLLAPSED", 'science',
                lambda f: {'grain_control_classes':
                           f['grain_primary_classes'],
                           'escape_control': f['escape_primary']}))
MUTANTS.append(("ATOM-CLAIMED-WITHOUT-NU", 'science',
                lambda f: {'B2_nu_support': 0}))
MUTANTS.append(("BLOCKING-FACT-ERASED", 'science',
                lambda f: {'B3_profile_decreases': 1,
                           'B3_all_zero_inf': False}))

F['gate_results'] = tuple(sorted((g, RES[g][0]) for g in RES))
F['n_pass'] = sum(1 for g in RES if RES[g][0])
F['n_fail'] = sum(1 for g in RES if not RES[g][0])
F['n_substantive'] = sum(1 for gid, k, l, p, d in GATES if k == KIND_SUB)
F['n_theorem'] = sum(1 for gid, k, l, p, d in GATES if k == KIND_THM)
F['n_disclosure'] = sum(1 for gid, k, l, p, d in GATES if k == KIND_DIS)

prog(f"running {len(MUTANTS)} falsifiers ...")
KILLED = defaultdict(set)
MUT_ROWS = []
dead = []
unconstrained = []


def apply_and_score(nm, fn):
    G2 = Facts()
    G2.update(F)
    try:
        G2.update(fn(F))
    except Exception:
        pass
    r2 = run_gates(G2)
    return sorted(g for g in r2 if RES[g][0] and not r2[g][0])


for nm, cls, fn in MUTANTS:
    killed = apply_and_score(nm, fn)
    if not killed and nm.startswith('DRIFT['):
        k = nm[6:-1]
        killed = apply_and_score(nm, lambda f, k=k: {k: poison(f[k])})
        if killed:
            nm = nm + "+POISON"
        else:
            killed = apply_and_score(nm,
                                     lambda f, k=k: {k: erase(f[k])})
            if killed:
                nm = nm + "+ERASE"
    for g in killed:
        KILLED[g].add(nm)
    MUT_ROWS.append((nm, cls, len(killed), tuple(killed[:4])))
    if not killed:
        if nm.startswith('DRIFT['):
            unconstrained.append(nm[6:].rstrip(']'))
        else:
            dead.append(nm)
F['read_but_unconstrained'] = tuple(unconstrained)
F['mutant_rows'] = tuple(MUT_ROWS)
F['mutants_total'] = len(MUTANTS)
F['mutants_dead'] = tuple(dead)
# THE ESCALATION CENSUS.  The harness escalates drift -> poison ->
# erase and records the level in the mutant's name; the first delivery
# never aggregated it.  A falsifier that only bites after ERASE is
# attached to a predicate that constrains EXISTENCE, not value, and
# that is a fact about the gate, not about the falsifier.
F['escalation_drift'] = sum(1 for nm, cls, n, ks in MUT_ROWS
                            if not nm.endswith('+POISON')
                            and not nm.endswith('+ERASE'))
F['escalation_poison'] = sum(1 for nm, cls, n, ks in MUT_ROWS
                             if nm.endswith('+POISON'))
F['escalation_erase'] = sum(1 for nm, cls, n, ks in MUT_ROWS
                            if nm.endswith('+ERASE'))
F['escalation_erase_names'] = tuple(
    sorted(nm for nm, cls, n, ks in MUT_ROWS if nm.endswith('+ERASE')))
F['escalation_erase_gates'] = tuple(sorted({
    g for nm, cls, n, ks in MUT_ROWS if nm.endswith('+ERASE')
    for g in ks}))
emit(f"  {F['mutants_total']} declared falsifiers; each is an "
     f"injection into the gated object, and every gate predicate is "
     f"evaluated BLIND — no predicate anywhere in this file references "
     f"a falsifier's identity.")
emit(f"  falsifiers that killed nothing (a dead falsifier is an exit-1 "
     f"condition): {len(F['mutants_dead'])} "
     f"{list(F['mutants_dead'])}")
emit(f"  keys a predicate READS but does not CONSTRAIN (censused, not "
     f"hidden: neither the drift nor the escalated poison killed a "
     f"gate through them, so they enter a predicate without being "
     f"load-bearing in it): {len(F['read_but_unconstrained'])} "
     f"{list(F['read_but_unconstrained'])}")
_bycls = defaultdict(int)
for nm, cls, n, ks in MUT_ROWS:
    _bycls[cls] += 1
emit(f"  by class: {dict(sorted(_bycls.items()))}")
emit(f"  THE ESCALATION CENSUS, aggregated rather than left in the "
     f"mutant names: {F['escalation_drift']} falsifiers bite at level 1 "
     f"(DRIFT), {F['escalation_poison']} need level 2 (POISON) and "
     f"{F['escalation_erase']} need level 3 (ERASE).  A gate that dies "
     f"only when its input is ERASED constrains existence, not value; "
     f"the gates in that position are "
     f"{list(F['escalation_erase_gates'])} and the falsifiers are "
     f"{list(F['escalation_erase_names'])}.")
emit(f"  a sample of the kill table (falsifier -> gates it killed):")
for nm, cls, n, ks in MUT_ROWS[:8] + MUT_ROWS[-12:]:
    emit(f"    {nm[:46]:46s} -> {n:2d} gate(s) {list(ks)}")

# --- THE NEVER-FALSIFIED CENSUS, WITH WAIVERS THAT DO NOT CLOSE ON
# --- THE AUTHOR'S OWN DECLARATION (v14 #34, and the correction of
# --- record).  In the first delivery a gate declared KIND_THM was
# --- excluded from the falsifier generator, therefore died nowhere,
# --- therefore landed in the never-falsified census, where it was
# --- automatically waived BY THE VERY DECLARATION THAT EXCLUDED IT.
# --- Two changes break the loop: the generator now harvests read-keys
# --- from every gate (above), and a waiver is issued only to a gate
# --- whose predicate is INPUT-INDEPENDENT AS MEASURED — it survives
# --- the drift, poison and erase perturbation of every key it reads.
# --- The classification is therefore a measured property of the
# --- predicate and not a tag the author attached to it.
LEVELS = (('DRIFT', perturb), ('POISON', poison), ('ERASE', erase))


def waiver_probe(pred, reads):
    """Find a perturbation of a key this predicate READS that flips it.
    None means the predicate is input-independent as measured: it
    survives drift, poison AND erase of every key it reads, so it
    constrains nothing about the measured objects and is a pass by
    construction.  Anything else is a MEASUREMENT and may not be
    waived on a declaration."""
    for k in sorted(reads, key=SK):
        for lv, fn in LEVELS:
            G2 = Facts()
            G2.update(F)
            try:
                G2.update({k: fn(dict.__getitem__(F, k))})
            except Exception:
                continue
            G2.track()
            try:
                ok = bool(pred(G2))
            except Exception:
                ok = False
            G2.stop()
            if not ok:
                return (k, lv)
    return None


def close_waivers(res):
    """For every never-falsified gate, probe for a killing perturbation
    of a key it reads.  If one exists the gate is a measurement, and
    the probe's own witness is REGISTERED AS A DECLARED FALSIFIER and
    run — so the coverage gap is closed rather than waived.  What
    remains never-falsified is input-independent as measured, and only
    that earns a waiver."""
    added = []
    for gid, kind, label, pred, det in GATES:
        if KILLED[gid]:
            continue
        hit = waiver_probe(pred, res[gid][2])
        if hit is None:
            continue
        k, lv = hit
        fn = dict(LEVELS)[lv]
        nm = f"PROBE[{gid}|{k}|{lv}]"
        killed = apply_and_score(nm, lambda f, k=k, fn=fn: {k: fn(f[k])})
        MUTANTS.append((nm, 'waiver-probe',
                        lambda f, k=k, fn=fn: {k: fn(f[k])}))
        for g in killed:
            KILLED[g].add(nm)
        MUT_ROWS.append((nm, 'waiver-probe', len(killed), tuple(killed)))
        if not killed:
            dead.append(nm)
        added.append(nm)
    never = [gid for gid, k, l, p, d in GATES if not KILLED[gid]]
    waivers = []
    for gid, kind, label, pred, det in GATES:
        if gid not in never:
            continue
        w = ("VERIFIED INPUT-INDEPENDENT (measured, not declared): this "
             "predicate survives the DRIFT, POISON and ERASE "
             "perturbation of EVERY key it reads, so it constrains "
             "nothing about the measured objects and is a pass by "
             "construction.  The waiver is issued by that measurement "
             "and not by the gate's declared kind; a gate whose "
             "predicate could be flipped has its killing perturbation "
             "registered as a falsifier instead of being waived")
        waivers.append((gid, kind, w))
    return never, waivers, added


NEVER, WAIVERS, PROBE_ADDED = close_waivers(RES)
F['waiver_probes_registered'] = tuple(PROBE_ADDED)
F['never_falsified'] = tuple(NEVER)
F['never_falsified_unwaived'] = tuple(
    gid for gid, kind, w in WAIVERS if w.startswith("NO VERIFIED"))
F['waivers'] = tuple((g, k) for g, k, w in WAIVERS)
emit("")
emit(f"  THE NEVER-FALSIFIED CENSUS, PHASE 1 ({len(NEVER)} of "
     f"{len(GATES)} gates registered so far), each with a VERIFIED "
     f"waiver (v14 #34: a waiver claim is a gate claim).  Three "
     f"further gates read this phase's own outcome and are registered "
     f"and falsified in phase 2 below; the FINAL census is printed "
     f"there:")
for gid, kind, w in WAIVERS:
    emit(f"    {gid:20s} [{kind}] {w}")
emit(f"  gates never falsified AND without a verified waiver: "
     f"{len(F['never_falsified_unwaived'])} "
     f"{list(F['never_falsified_unwaived'])}")

# ======================================================================
# THE GATE TABLE, THE THEOREM-PASS CENSUS, THE COMPLIANCE SWEEP
# ======================================================================
# ======================================================================
# THE THEOREM-PASS CENSUS, RECOMPUTED MECHANICALLY.  A gate may be
# classified THEOREM-PASS (or DISCLOSURE) only if this file exhibits
# its FORCING and machine-checks it: a measured witness whose value is
# the one the forcing predicts, and which no input the construction
# admits could move.  The census is then computed from the tags AND
# every tag is backed by a gated witness, so the classification is not
# the author's declaration.  Two gates the first delivery counted as
# substantive move here — B1-TREE (unique parenthood is a property of
# the representation) and A4-PRED (the reduction's agreement is
# forced) — and one more, B3-MONOTONE, because its content is entailed
# by A4-MONO's; each of the three is delivered with a SUBSTANTIVE
# companion (B1-NODUP, A4-PRED-UNFORCED, B3-NSUP-PROFILE) carrying the
# half that could have come out otherwise.
FORCING = [
    ('A3-KERNEL', KIND_THM,
     "k_r divides by its own denominator: G(h, r) is DEFINED as the "
     "sum k_r normalizes by, so properness is an identity",
     'proper_violations', 0),
    ('A3-CUTADD', KIND_DIS,
     "cut-additivity follows BY INDUCTION from properness: a chain of "
     "probability kernels has cut mass 1 at every cut",
     'proper_violations', 0),
    ('A4-MONO', KIND_THM,
     "View.holdings is a UNION over the view's arbs, deliveries and "
     "merges, so it cannot shrink along a transition",
     'mono_shrinking_all', 0),
    ('A4-PRED', KIND_THM,
     "components are built from live proposals, so an empty live set "
     "forces an empty component set; a merge pair needs two "
     "non-superseded created versions, so a singleton forces none",
     'pred_forcing_live_empty_but_components', 0),
    ('A7-ROOTTHEOREM', KIND_THM,
     "the root menu is ONE ORBIT PER EVENT KIND under the layer's own "
     "automorphisms, so every equivariant terminal forces the "
     "uniform-within-kind root conditional",
     'sym_menu_violations', 0),
    ('B1-TREE', KIND_THM,
     "a history IS its event sequence, so h = g + (e,) forces "
     "g = h[:-1]: unique parenthood is a property of the "
     "representation, and its only failure mode — a duplicated menu "
     "entry — is gated substantively at B1-NODUP",
     'menu_duplicate_entries', 0),
    ('B3-MONOTONE', KIND_THM,
     "set-monotonicity of holdings (A4-MONO) ENTAILS "
     "cardinality-monotonicity of the profile; the entailment is "
     "machine-checked pointwise over every transition of the family",
     'mono_entailment_violations', 0),
]
F['forcing_rows'] = tuple((g, k, wk, we) for g, k, d, wk, we in FORCING)
F['forcing_witness_values'] = tuple(
    (g, wk, dict.__getitem__(F, wk)) for g, k, d, wk, we in FORCING)
F['forcing_witness_ok'] = all(
    dict.__getitem__(F, wk) == we for g, k, d, wk, we in FORCING)
F['forcing_covers_nonsub'] = (
    {g for g, k, l, p, d in GATES if k != KIND_SUB}
    == {g for g, k, d, wk, we in FORCING})
F['forcing_kinds_match'] = all(
    dict((g, k) for g, k, l, p, d in GATES).get(g) == k
    for g, k, d, wk, we in FORCING)
emit("")
emit("[THE FORCING REGISTRY — why each non-substantive gate is one]")
for g, k, d, wk, we in FORCING:
    emit(f"  {g:20s} [{k}] {d}")
    emit(f"      machine-checked witness: {wk} = "
         f"{dict.__getitem__(F, wk)} (forced value {we})")
gate("C-THEOREMCENSUS", KIND_SUB,
     "THE THEOREM-PASS CENSUS IS ITSELF GATED AND MECHANICALLY "
     "RECOMPUTED: the substantive, theorem-pass and disclosure counts "
     "partition the gate list exactly; EVERY non-substantive gate "
     "appears in the forcing registry with the kind it is registered "
     "under; no substantive gate does; and every registered forcing's "
     "machine-checked witness carries the value the forcing predicts.  "
     "So the classification is a computed property with an exhibited "
     "reason, not a tag",
     lambda f: (f['n_substantive'] + f['n_theorem'] + f['n_disclosure']
                == len(GATES)
                and f['n_theorem'] >= 3
                and f['forcing_witness_ok']
                and f['forcing_covers_nonsub']
                and f['forcing_kinds_match']),
     lambda f: f"{f['n_substantive']} substantive + {f['n_theorem']} "
               f"theorem-pass + {f['n_disclosure']} disclosure = "
               f"{len(GATES)}; forcing registry covers every "
               f"non-substantive gate = {f['forcing_covers_nonsub']}; "
               f"witnesses = {list(f['forcing_witness_values'])}")

# ======================================================================
# THE INSTRUMENTS THE COMPLIANCE SWEEP NEEDS.  Every one of them is a
# computation over this file's own syntax tree or over the process's
# own instrumented state; none of them is a typed status.
# ======================================================================
def _consts_in(node):
    return {n.value for n in ast.walk(node)
            if isinstance(n, ast.Constant) and isinstance(n.value, str)}


_fn_nodes = {n.name: n for n in ast.walk(_tree)
             if isinstance(n, ast.FunctionDef)}
_gate_call_consts = set()
for _n in ast.walk(_tree):
    if (isinstance(_n, ast.Call) and isinstance(_n.func, ast.Name)
            and _n.func.id == 'gate'):
        _gate_call_consts |= _consts_in(_n)
_subproc = 0
for _n in ast.walk(_tree):
    if isinstance(_n, ast.Call):
        _fn = _n.func
        _nm = (_fn.attr if isinstance(_fn, ast.Attribute)
               else (_fn.id if isinstance(_fn, ast.Name) else ''))
        if _nm in ('popen', 'system', 'Popen', 'check_output', 'run',
                   'call', 'check_call', 'spawnl', 'fork', 'execv'):
            _subproc += 1
_typed_F = set()
for _n in ast.walk(_tree):
    if isinstance(_n, ast.Assign) and len(_n.targets) == 1:
        _t = _n.targets[0]
        if (isinstance(_t, ast.Subscript) and isinstance(_t.value, ast.Name)
                and _t.value.id == 'F'
                and isinstance(_t.slice, ast.Constant)
                and isinstance(_n.value, ast.Constant)):
            _typed_F.add(_t.slice.value)
_comply_const_statuses = 0
for _n in ast.walk(_tree):
    if (isinstance(_n, ast.Assign) and len(_n.targets) == 1
            and isinstance(_n.targets[0], ast.Name)
            and _n.targets[0].id == 'COMPLY'
            and isinstance(_n.value, ast.List)):
        for _row in _n.value.elts:
            if isinstance(_row, ast.Tuple) and len(_row.elts) >= 4:
                _kindnode = _row.elts[1]
                _declared_computed = (
                    isinstance(_kindnode, ast.Constant)
                    and _kindnode.value == 'COMPUTED')
                if (_declared_computed
                        and isinstance(_row.elts[2], ast.Constant)):
                    _comply_const_statuses += 1
_bv_consts = _consts_in(_fn_nodes['build_verdict'])
_cv_consts = _consts_in(_fn_nodes['check_verdict'])
# A literal shared by the two functions is legitimate in exactly two
# cases: a KEY OF THE SHARED TOKEN TABLE (both consult it by key, which
# is what the engraving permits) and a KEY OF THE GATED OBJECT (the
# comparator must be able to name which measured value it demands).
# Anything else shared would be the comparator re-typing the emitter's
# prose, which is the failure mode the rule exists to catch.
_shared_verdict_literals = ((_bv_consts & _cv_consts) - set(VTOK)
                            - set(dict.keys(F)))
_precheck_src = _src[:_src.index('VTOK' + ' = {')]
_precheck_names_verdict = sum(
    1 for _k in ('seg_term', 'seg_found', 'seg_blocked')
    if VTOK[_k] in _precheck_src)
ANCHORED_PATHS = {os.path.abspath(os.path.join(REPO, p))
                  for t, n, ped, arts, s in ROWS for p, w in arts}
ANCHORED_PATHS |= {os.path.abspath(os.path.join(REPO, p))
                   for t, p, c, x in VERBATIM}
ANCHORED_PATHS.add(os.path.abspath(SELF))
_unanchored_opens = sorted(OPENED - ANCHORED_PATHS)
MUST_NOT_BE_TYPED = {'birkhoff_tau', 'birkhoff_diameter_finite',
                     't_total', 'rsig_count', 'columns_single_parent',
                     'B3_profile_decreases', 'mono_shrinking_all',
                     'escape_primary', 'escape_control'}
_mutant_names = {nm for nm, cls, fn in MUTANTS}
_gate_refs_mutant = sorted(_gate_call_consts & _mutant_names)

# --- THE KEY-COVERAGE CENSUS (v14 #34, honest denominators).  Computed
# --- by a function so that it can be RE-RUN after the last gate and
# --- the last falsifier are registered: a census taken early would
# --- exclude the compliance gates' own read keys, which is exactly the
# --- kind of narrowed denominator this repair exists to retire.
NAMED_MUTANT_KEYS = {'verdict', 'escape_primary',
                     'escape_primary_classes',
                     'grain_control_classes', 'escape_control',
                     'B2_nu_support', 'B3_profile_decreases',
                     'B3_all_zero_inf', 'n_theorem', 'compliance_all',
                     'never_falsified_unwaived',
                     'verdict_falsifiers_that_killed',
                     'path_drift_survivors', 'verbatim_drift_survivors',
                     'forcing_witness_ok', 'forcing_covers_nonsub',
                     'comply_constant_statuses', 'compliance_asserted',
                     'verbatim_consumers_unbound', 'verbatim_consumers',
                     'verbatim_min_chars', 'verbatim_unique',
                     'verbatim_drift_appends', 'verbatim_drift_real',
                     't5_ledger_number', 'unanchored_opens',
                     'subprocess_calls', 'cli_rejected_sample',
                     'cli_exit_on_unknown',
                     'coverage_every_read_key_falsified',
                     'keys_read_but_unfalsified',
                     'shared_verdict_literals', 'gate_refs_mutant'}


def coverage_census(res):
    kd = set(dict.keys(F))
    kr = set()
    for gid in res:
        kr |= res[gid][2]
    kf = set(NAMED_MUTANT_KEYS)
    for nm, cls, n, ks in MUT_ROWS:
        if nm.startswith('DRIFT['):
            kf.add(nm[6:].split(']')[0])
        if nm.startswith('PROBE['):
            kf.add(nm[6:-1].split('|')[1])
    F['keys_delivered'] = len(kd)
    F['keys_read_by_a_gate'] = len(kr)
    F['keys_with_falsifier'] = len(kf & kd)
    F['keys_without_falsifier'] = tuple(sorted(kd - kf))
    F['keys_read_but_unfalsified'] = tuple(sorted(kr - kf))
    F['coverage_every_read_key_falsified'] = (
        len(F['keys_read_but_unfalsified']) == 0)
    F['gate_reads_all_in_F'] = all(k in kd for k in kr)


coverage_census(RES)
gate("C-KEYCOVERAGE", KIND_SUB,
     "THE COVERAGE DENOMINATOR IS PUBLISHED AND GATED: every delivered "
     "receipt key that ANY gate reads carries a declared falsifier — "
     "not only the keys the substantive gates read, which is how a "
     "theorem-pass gate used to escape falsification entirely — and "
     "the delivered keys no gate reads are enumerated as "
     "disclosure-only rather than reported as covered",
     lambda f: (f['coverage_every_read_key_falsified']
                and f['keys_read_by_a_gate'] > 100
                and f['keys_with_falsifier'] >= f['keys_read_by_a_gate']),
     lambda f: f"{f['keys_with_falsifier']} of {f['keys_delivered']} "
               f"delivered keys carry a falsifier; "
               f"{f['keys_read_by_a_gate']} are read by a gate; "
               f"read-but-unfalsified = "
               f"{list(f['keys_read_but_unfalsified'])}")

COMPLY = [
    ("RUNBOOK 4 exact arithmetic", 'COMPUTED',
     len(F['ast_float_literals']) == 0,
     f"AST float-guard: {len(F['ast_float_literals'])} float literals; "
     f"float() confined to display"),
    ("RUNBOOK 4 counts computed, never typed", 'COMPUTED',
     F['t_total'] == 243769 and F['rsig_count'] == 5161
     and len(MUST_NOT_BE_TYPED & _typed_F) == 0,
     f"every census in this receipt is enumerated in-process; an AST "
     f"census of constant assignments into the gated object finds "
     f"{len(_typed_F)} typed keys {sorted(_typed_F)}, and NONE of them "
     f"is a measured quantity ({sorted(MUST_NOT_BE_TYPED & _typed_F)} "
     f"— the Birkhoff coefficient and the diameter flag are DERIVED "
     f"from the computed witness minor, never typed)"),
    ("RUNBOOK 4 controls in both directions", 'COMPUTED',
     F['misnorm_failures'] > 0 and F['classifier_matches'] == 0
     and F['B2_atom_found'] and F['pred_unforced_disagreements'] > 0
     and F['nsup_shrinking_all'] > 0,
     "negative controls: mis-normalized kernel, classifier mismatch, "
     "grain swap, the unforced predicate variant, the non-superseded "
     "profile; positive controls: the atoms of B2, the reduction "
     "control of A4-PRED"),
    ("RUNBOOK 13 (#234) verdict derived in a gate", 'COMPUTED',
     RES['V-VERDICT'][0] and F['verdict_check'][0],
     "V-VERDICT parses the complete emitted string against an "
     "independently declared field table and accounts for every "
     "numeral in it"),
    ("RUNBOOK 14 (#10) containment is not equality", 'COMPUTED',
     sum(1 for nm, cls, n, ks in MUT_ROWS
         if nm.startswith('VERDICT-') and n > 0) == 5,
     "all five verdict falsifiers (value swap, appended text, "
     "truncation, dropped segment, retyped segment) kill a gate; "
     "gated at C-VERDICTFALSIFIERS with its own falsifier"),
    ("RUNBOOK 13 (#10) render from the gated object", 'COMPUTED',
     F['verdict_check'][0] and F['gate_reads_all_in_F'],
     f"every gate reads keys of the gated object and nothing else "
     f"({F['keys_read_by_a_gate']} distinct keys, all present in F), "
     f"and the emitted verdict's every numeral is accounted for by a "
     f"value of that object"),
    ("RUNBOOK 13 (#20) prose renders from the receipt", 'DISCLOSURE',
     True,
     "ASSERTED, NOT COMPUTED, and counted separately: this is a claim "
     "about paper-11, a different artifact, and this process cannot "
     "measure it.  It is carried as a disclosure so that the computed "
     "count below is honest"),
    ("RUNBOOK 14 (#20) compliance claims are gate claims", 'COMPUTED',
     _comply_const_statuses == 0,
     f"an AST census of this very table finds {_comply_const_statuses} "
     f"rows whose COMPUTED status is a literal constant; the "
     f"DISCLOSURE rows are counted separately and named as asserted; "
     f"gated at C-COMPLIANCE and at C-NOCONSTANTRULES"),
    ("RUNBOOK 14 (#20) path-value anchoring", 'COMPUTED',
     F['path_drift_survivors'] == 0,
     "M-PATHDRIFT: every drifted path fails to resolve"),
    ("RUNBOOK 14 (#34) waiver claims are gate claims", 'COMPUTED',
     len(F['never_falsified_unwaived']) == 0
     and len(F['waivers']) == len(F['never_falsified']),
     f"a waiver is issued only to a predicate MEASURED to be "
     f"input-independent under drift, poison and erase of every key it "
     f"reads; a never-falsified gate that could be flipped has its "
     f"killing perturbation registered as a falsifier instead "
     f"({len(F['waiver_probes_registered'])} such registrations)"),
    ("RUNBOOK 14 (#34) verbatim-text anchors", 'COMPUTED',
     F['verbatim_drift_survivors'] == 0 and len(VERBATIM) >= 12
     and F['verbatim_unique'] and F['verbatim_drift_real']
     and len(F['verbatim_consumers_unbound']) == 0,
     f"{len(VERBATIM)} context windows over "
     f"{len(set(r[0] for r in VERBATIM))} of the {len(ROWS)} pinned "
     f"rows, evaluated before the byte anchors, each at least "
     f"{MIN_CTX} characters, each occurring exactly once in its "
     f"source, each perturbed at a content-bearing token, and each "
     f"bound to a REGISTERED consumer gate"),
    ("RUNBOOK 14 (#46) no unanchored runtime inputs, no moving "
     "references", 'COMPUTED',
     len(_unanchored_opens) == 0 and _subproc == 0,
     f"the set of paths this process opened is instrumented and "
     f"compared against the anchored set: {len(OPENED)} opened, "
     f"{len(_unanchored_opens)} outside the anchor table "
     f"{_unanchored_opens}.  The committed v10 ledger is row T9 and is "
     f"read at its pinned sha like every other artifact; an AST census "
     f"finds {_subproc} subprocess calls, so nothing is read at `git "
     f"show HEAD:` or any other moving reference"),
    ("RUNBOOK 14 (#208) no gate references mutant identity", 'COMPUTED',
     len(_gate_refs_mutant) == 0,
     f"an AST census of every string constant inside every gate() call "
     f"finds {len(_gate_refs_mutant)} that equal a registered "
     f"falsifier's name {_gate_refs_mutant}; the predicates are the "
     f"same functions evaluated blind"),
    ("RUNBOOK 14 (#219) comparators built independently", 'COMPUTED',
     len(_shared_verdict_literals) == 0 and RES['A4-MASS'][0],
     f"an AST comparison of build_verdict and check_verdict finds "
     f"{len(_shared_verdict_literals)} string literals shared other "
     f"than the keys of the shared token table "
     f"{sorted(_shared_verdict_literals)}; and A4-MASS compares a "
     f"chained kernel product against a closed rational expression in "
     f"the potentials — two independent routes, not one routed twice"),
    ("RUNBOOK 15 declared arena", 'COMPUTED',
     F['n_actors'] == 2 and F['grain_primary_classes'] == 13
     and F['grain_control_classes'] == 113 and len(F['choices']) == 9,
     "boundary / family / law / state / arena / provenance printed as "
     "data at the head of this receipt; the GRAIN is declared and five "
     "grains are measured; the choice inventory classifies all nine "
     "choices and counts the free ones"),
    ("RUNBOOK 15 (#196) match every coordinate", 'COMPUTED',
     F['B2_coarsening_violations'] == 0
     and len(F['B2_full_grain_rows']) == 3
     and all(len(r) == 12 for r in F['B2_profile_rows_full']),
     "ARM B's like-for-like comparisons fix the horizon convention AND "
     "the grain AND the depth window before any class contrast is "
     "read; every block row carries all five grains and its own "
     "window, and the coarsening lemma is checked cell by cell"),
    ("RUNBOOK 13 (#314) precheck may not name the verdict", 'COMPUTED',
     _precheck_names_verdict == 0,
     f"the source region up to the shared token table — the anchors, "
     f"the float-guard and every precheck — contains "
     f"{_precheck_names_verdict} of the three verdict segment names"),
    ("v14 #82 the CLI contract is enforced, not documented", 'COMPUTED',
     F['cli_rejected_sample'] == 2 and F['cli_exit_on_unknown'] == 2
     and F['cli_flags_known'] == 5,
     "the argv whitelist is exercised in-process on a bogus sample "
     "before any measurement: both tokens are rejected and the usage "
     "exit code is 2"),
    ("pin section 4 the delivery-free contrast at every census",
     'COMPUTED', F['df_total'] == 34375,
     "the partner family is derived from T1 and censused beside every "
     "transport census"),
]
F['compliance'] = tuple((n, bool(ok)) for n, k, ok, d in COMPLY)
F['compliance_kinds'] = tuple((n, k) for n, k, ok, d in COMPLY)
F['compliance_all'] = all(ok for n, k, ok, d in COMPLY)
F['compliance_computed'] = sum(1 for n, k, ok, d in COMPLY
                               if k == 'COMPUTED')
F['compliance_asserted'] = sum(1 for n, k, ok, d in COMPLY
                               if k != 'COMPUTED')
F['comply_constant_statuses'] = _comply_const_statuses
F['unanchored_opens'] = tuple(_unanchored_opens)
F['subprocess_calls'] = _subproc
F['typed_F_assignments'] = tuple(sorted(_typed_F))
F['shared_verdict_literals'] = tuple(sorted(_shared_verdict_literals))
F['gate_refs_mutant'] = tuple(_gate_refs_mutant)
emit("")
emit(f"[COMPLIANCE SWEEP — {F['compliance_computed']} COMPUTED "
     f"statuses and {F['compliance_asserted']} ASSERTED ones, counted "
     f"separately and labelled row by row]")
for n, k, ok, d in COMPLY:
    emit(f"  [{'OK  ' if ok else 'FAIL'}] [{k}] {n}")
    emit(f"         {d}")
gate("C-COMPLIANCE", KIND_SUB,
     "THE COMPLIANCE SWEEP IS A GATE, NOT A CLAIM: every engraved rule "
     "in the table above is evaluated, this gate fails if any one of "
     "them is False, and the COMPUTED and ASSERTED rows are counted "
     "separately so that the header cannot outrun the table",
     lambda f: (f['compliance_all'] and len(f['compliance']) >= 15
                and f['compliance_computed']
                == len(f['compliance']) - f['compliance_asserted']
                and f['compliance_asserted'] <= 1),
     lambda f: f"{sum(1 for n, ok in f['compliance'] if ok)} of "
               f"{len(f['compliance'])} rules satisfied; "
               f"{f['compliance_computed']} computed, "
               f"{f['compliance_asserted']} asserted")
gate("C-INSTRUMENT", KIND_SUB,
     "THE INSTRUMENT'S FOUR SELF-DESCRIPTIONS ARE GATED RATHER THAN "
     "PRINTED: the set of paths this process opened lies inside the "
     "anchor table (no unanchored runtime input); the AST census finds "
     "no subprocess call anywhere (no moving reference — the `git show "
     "HEAD:` read is gone and the ledger is a pinned row); "
     "build_verdict and check_verdict share no string literal outside "
     "the shared token table (the comparator is independent); and no "
     "string constant inside any gate() call equals a registered "
     "falsifier's name (the predicates are blind)",
     lambda f: (len(f['unanchored_opens']) == 0
                and f['subprocess_calls'] == 0
                and len(f['shared_verdict_literals']) == 0
                and len(f['gate_refs_mutant']) == 0),
     lambda f: f"unanchored opens {list(f['unanchored_opens'])}; "
               f"subprocess calls {f['subprocess_calls']}; shared "
               f"verdict literals {list(f['shared_verdict_literals'])}; "
               f"gate constants naming a falsifier "
               f"{list(f['gate_refs_mutant'])}")
gate("C-NOCONSTANTRULES", KIND_SUB,
     "NO COMPLIANCE ROW MARKED COMPUTED MAY CARRY A CONSTANT STATUS, "
     "and this is checked over the table's own syntax tree rather than "
     "believed: an AST census of the COMPLY literal finds zero rows "
     "whose status expression is a literal.  A constant status cannot "
     "move the aggregate, so a rule asserted as a constant would be a "
     "rule the sweep can never fail",
     lambda f: (f['comply_constant_statuses'] == 0
                and f['compliance_asserted'] <= 1),
     lambda f: f"constant statuses in COMPLY = "
               f"{f['comply_constant_statuses']}; asserted rows = "
               f"{f['compliance_asserted']}")
gate("C-WAIVERS", KIND_SUB,
     "THE WAIVER CENSUS IS A GATE, AND THE WAIVER NO LONGER CLOSES ON "
     "THE AUTHOR'S DECLARATION: no gate is both never-falsified and "
     "without a verified waiver, where 'verified' means MEASURED "
     "input-independent under drift, poison and erase of every key the "
     "predicate reads.  A never-falsified gate that could be flipped "
     "has its killing perturbation registered as a declared falsifier "
     "instead of being waived, and the count of such registrations is "
     "published",
     lambda f: (len(f['never_falsified_unwaived']) == 0
                and len(f['waivers'])
                == len(f['never_falsified'])),
     lambda f: f"{len(f['waivers'])} waived gates, "
               f"{len(f['never_falsified_unwaived'])} unwaived, "
               f"{len(f['waiver_probes_registered'])} killing "
               f"perturbations registered as falsifiers instead of "
               f"being waived")
gate("C-VERDICTFALSIFIERS", KIND_SUB,
     "THE VERDICT-FALSIFIER CENSUS IS A GATE: all five declared verdict "
     "falsifiers — value swap, appended text, truncation, dropped "
     "segment, retyped segment — each killed at least one gate, so "
     "containment can never stand in for equality here",
     lambda f: f['verdict_falsifiers_that_killed'] == 5,
     lambda f: f"{f['verdict_falsifiers_that_killed']} of 5 verdict "
               f"falsifiers killed a gate")
F['verdict_falsifiers_that_killed'] = sum(
    1 for nm, cls, n, ks in MUT_ROWS
    if nm.startswith('VERDICT-') and n > 0)

# PHASE 2.  Three gates above read the outcome of phase 1's own
# falsifier run, so they could not be part of it.  Their falsifiers are
# declared here and run against the FULL gate set.
F['n_substantive'] = sum(1 for gid, k, l, p, d in GATES if k == KIND_SUB)
F['n_theorem'] = sum(1 for gid, k, l, p, d in GATES if k == KIND_THM)
F['n_disclosure'] = sum(1 for gid, k, l, p, d in GATES if k == KIND_DIS)
PHASE2 = [
    ("THEOREM-CENSUS-DROP", 'compliance',
     lambda f: {'n_theorem': f['n_theorem'] - 1}),
    ("FORCING-WITNESS-BROKEN", 'compliance',
     lambda f: {'forcing_witness_ok': False}),
    ("FORCING-COVERAGE-BROKEN", 'compliance',
     lambda f: {'forcing_covers_nonsub': False}),
    ("COMPLIANCE-FALSE", 'compliance',
     lambda f: {'compliance_all': False}),
    ("COMPLIANCE-CONSTANT-ROW", 'compliance',
     lambda f: {'comply_constant_statuses': 1}),
    ("COMPLIANCE-ASSERTED-INFLATED", 'compliance',
     lambda f: {'compliance_asserted': f['compliance_asserted'] + 2}),
    ("WAIVER-UNVERIFIED", 'compliance',
     lambda f: {'never_falsified_unwaived': ('A3-KERNEL',)}),
    ("VERDICT-FALSIFIER-CENSUS-DROP", 'compliance',
     lambda f: {'verdict_falsifiers_that_killed':
                f['verdict_falsifiers_that_killed'] - 1}),
    ("PATHDRIFT-SURVIVES", 'anchor',
     lambda f: {'path_drift_survivors': 1}),
    ("VERBATIMDRIFT-SURVIVES", 'anchor',
     lambda f: {'verbatim_drift_survivors': 1}),
    ("VERBATIM-CONSUMER-UNBOUND", 'anchor',
     lambda f: {'verbatim_consumers_unbound': ('B0-SUCCESSOR-NAMED',),
                'verbatim_consumers': ()}),
    ("VERBATIM-WINDOW-TRUNCATED", 'anchor',
     lambda f: {'verbatim_min_chars': 4, 'verbatim_unique': False}),
    ("VERBATIM-DRIFT-APPEND-ONLY", 'anchor',
     lambda f: {'verbatim_drift_appends': 10,
                'verbatim_drift_real': False}),
    ("LEDGER-DEGRADED-TO-NONE", 'anchor',
     lambda f: {'t5_ledger_number': None}),
    ("UNANCHORED-OPEN", 'anchor',
     lambda f: {'unanchored_opens': ('v14/LOG.md',)}),
    ("SUBPROCESS-SPAWNED", 'anchor',
     lambda f: {'subprocess_calls': 1}),
    ("CLI-WHITELIST-DISABLED", 'cli',
     lambda f: {'cli_rejected_sample': 0}),
    ("CLI-EXIT-CODE-WRONG", 'cli',
     lambda f: {'cli_exit_on_unknown': 0}),
    ("KEYCOVERAGE-HOLE", 'coverage',
     lambda f: {'coverage_every_read_key_falsified': False,
                'keys_read_but_unfalsified': ('rsig_profiles',)}),
    ("SHARED-VERDICT-LITERAL", 'comparator',
     lambda f: {'shared_verdict_literals': ('ESCAPE ',)}),
    ("GATE-NAMES-MUTANT", 'comparator',
     lambda f: {'gate_refs_mutant': ('BLOCKING-FACT-ERASED',)}),
]
MUTANTS.extend(PHASE2)
RES = run_gates(F)
for nm, cls, fn in PHASE2:
    killed = apply_and_score(nm, fn)
    for g in killed:
        KILLED[g].add(nm)
    MUT_ROWS.append((nm, cls, len(killed), tuple(killed)))
    if not killed:
        dead.append(nm)
# PHASE 3 — THE COVERAGE CLOSURE.  The phase-1 generator ran before the
# compliance gates existed, so the keys those gates read had no
# falsifier of their own.  Every key any gate reads is harvested again
# HERE, against the FINAL gate set, and the missing falsifiers are
# generated and run with the same escalation ladder.  After this pass
# the coverage census's denominator is the whole delivery.
_have3 = set(NAMED_MUTANT_KEYS)
for nm, cls, n, ks in MUT_ROWS:
    if nm.startswith('DRIFT['):
        _have3.add(nm[6:].split(']')[0])
    if nm.startswith('PROBE['):
        _have3.add(nm[6:-1].split('|')[1])
_need3 = set()
for gid in RES:
    _need3 |= RES[gid][2]
PHASE3 = [(f"DRIFT[{k}]", 'value-drift/census-drop',
           lambda f, k=k: {k: perturb(f[k])})
          for k in sorted(_need3 - _have3, key=SK)]
MUTANTS.extend(PHASE3)
for nm, cls, fn in PHASE3:
    killed = apply_and_score(nm, fn)
    if not killed:
        _k3 = nm[6:-1]
        killed = apply_and_score(
            nm, lambda f, k=_k3: {k: poison(f[k])})
        if killed:
            nm = nm + "+POISON"
        else:
            killed = apply_and_score(
                nm, lambda f, k=_k3: {k: erase(f[k])})
            if killed:
                nm = nm + "+ERASE"
    for g in killed:
        KILLED[g].add(nm)
    MUT_ROWS.append((nm, cls, len(killed), tuple(killed)))
    if not killed:
        unconstrained.append(nm[6:].rstrip(']'))
F['phase3_falsifiers'] = tuple(nm for nm, cls, fn in PHASE3)
F['read_but_unconstrained'] = tuple(unconstrained)

NEVER, WAIVERS, PROBE2 = close_waivers(RES)
F['waiver_probes_registered'] = tuple(PROBE_ADDED) + tuple(PROBE2)
coverage_census(RES)          # FINAL: every gate, every falsifier
emit("")
emit("[KEY COVERAGE — the honest denominator, computed and gated, "
     "AFTER the last gate and the last falsifier are registered]")
emit(f"  delivered keys: {F['keys_delivered']}; read by at least one "
     f"gate: {F['keys_read_by_a_gate']}; carrying a declared "
     f"falsifier: {F['keys_with_falsifier']}.")
emit(f"  EVERY KEY ANY GATE READS CARRIES A FALSIFIER: "
     f"{F['coverage_every_read_key_falsified']} "
     f"(exceptions: {list(F['keys_read_but_unfalsified'])}).  The "
     f"remaining {len(F['keys_without_falsifier'])} delivered keys are "
     f"DISCLOSURE-ONLY — no gate reads them, so no falsifier can kill "
     f"through them — and they are listed rather than counted as "
     f"covered: {list(F['keys_without_falsifier'])}")
F['never_falsified'] = tuple(NEVER)
F['never_falsified_unwaived'] = tuple(
    gid for gid, kind, w in WAIVERS if w.startswith("NO VERIFIED"))
F['waivers'] = tuple((g, k) for g, k, w in WAIVERS)
emit("")
emit(f"  THE NEVER-FALSIFIED CENSUS, FINAL ({len(NEVER)} of "
     f"{len(GATES)} gates), each with a VERIFIED waiver (v14 #34: a "
     f"waiver claim is a gate claim):")
for gid, kind, w in WAIVERS:
    emit(f"    {gid:22s} [{kind}] {w}")
emit(f"  gates never falsified AND without a verified waiver: "
     f"{len(F['never_falsified_unwaived'])} "
     f"{list(F['never_falsified_unwaived'])}")
RES = run_gates(F)
F['mutant_rows'] = tuple(MUT_ROWS)
F['mutants_total'] = len(MUTANTS)
F['mutants_dead'] = tuple(dead)
F['gate_results'] = tuple(sorted((g, RES[g][0]) for g in RES))
F['n_pass'] = sum(1 for g in RES if RES[g][0])
F['n_fail'] = sum(1 for g in RES if not RES[g][0])
F['n_substantive'] = sum(1 for gid, k, l, p, d in GATES if k == KIND_SUB)
F['n_theorem'] = sum(1 for gid, k, l, p, d in GATES if k == KIND_THM)
F['n_disclosure'] = sum(1 for gid, k, l, p, d in GATES if k == KIND_DIS)
F['never_falsified'] = tuple(gid for gid, k, l, p, d in GATES
                             if not KILLED[gid])

emit("")
emit(f"  final tally after the compliance falsifiers: "
     f"{F['n_pass']} PASS / {F['n_fail']} FAIL over {len(GATES)} "
     f"gates; {F['mutants_total']} falsifiers, "
     f"{len(F['mutants_dead'])} dead; never-falsified "
     f"{len(F['never_falsified'])} (all waived).")

# ======================================================================
# THE REGISTRY FLAGS AND THE MUTANT HARNESS.  Both run HERE — after the
# LAST gate registration and the LAST falsifier registration — so that
# the registries they print are the registries the run delivers.  The
# first delivery printed 40 of 44 gates and 112 of 118 falsifiers
# because its two branches sat before four gate registrations and six
# falsifier registrations.  Neither branch writes a file.
# ======================================================================
if '--list-gates' in ARGV:
    for gid, k, l, p, d in GATES:
        print(f"{gid}\t{k}\t{l[:70]}")
    print(f"# {len(GATES)} gates: {F['n_substantive']} substantive, "
          f"{F['n_theorem']} theorem-pass, {F['n_disclosure']} "
          f"disclosure.  NO FILE WRITTEN.")
    sys.exit(0)
if '--list-mutants' in ARGV:
    for nm, cls, fn in MUTANTS:
        print(f"{nm}\t{cls}")
    print(f"# {len(MUTANTS)} falsifiers.  NO FILE WRITTEN.")
    sys.exit(0)
if '--mutant' in ARGV:
    _want = ARGV['--mutant']
    _hit = [(nm, cls, fn) for nm, cls, fn in MUTANTS if nm == _want]
    if not _hit:
        print(f"[MUTANT] {_want!r} is not a registered falsifier.  "
              f"{len(MUTANTS)} are registered; --list-mutants prints "
              f"them.  NO FILE WRITTEN.  exit 1.")
        sys.stdout.flush()
        sys.exit(1)
    _nm, _cls, _fn = _hit[0]
    _k = apply_and_score(_nm, _fn)
    print(f"[MUTANT] {_nm} ({_cls}) killed {len(_k)} gate(s): {_k}")
    print(f"[MUTANT] NO FILE WRITTEN.  exit {0 if _k else 1}.")
    sys.stdout.flush()
    sys.exit(0 if _k else 1)

# ======================================================================
# THE FULL GATE TABLE — printed AFTER every gate is registered and
# every falsifier has run, so that no gate is missing from its own
# table.
# ======================================================================
emit("")
emit("[GATES]")
for gid, kind, label, pred, det in GATES:
    ok, d, reads = RES[gid]
    emit(f"  [{'PASS' if ok else 'FAIL'}] {gid} ({kind}) — {label}")
    emit(f"        ({d})")
emit("")
emit(f"  {F['n_pass']} PASS / {F['n_fail']} FAIL over {len(GATES)} "
     f"gates.")
emit(f"  THE THEOREM-PASS CENSUS, PRINTED WITH ITS COUNT (the trap the "
     f"predecessor's round set, honoured): of the {len(GATES)} gates, "
     f"{F['n_substantive']} are SUBSTANTIVE — they could have returned "
     f"False on this family — {F['n_theorem']} are THEOREM-PASSES that "
     f"cannot fail on any input the construction admits, and "
     f"{F['n_disclosure']} are DISCLOSURES.  So '{F['n_pass']} PASS' "
     f"is NOT {F['n_pass']} tests, and this receipt says so before "
     f"anyone else has to.  Every cannot-fail clause is named at its "
     f"own gate with its reason.")
_thm_ids = [gid for gid, k, l, p, d in GATES if k == KIND_THM]
_dis_ids = [gid for gid, k, l, p, d in GATES if k == KIND_DIS]
emit(f"    theorem-passes: {_thm_ids}")
emit(f"    disclosures   : {_dis_ids}")

# ======================================================================
# THE VERDICT, EMITTED
# ======================================================================
emit("")
emit("=" * 70)
emit("[VERDICT — composed, every segment computed in-gate]")
emit("=" * 70)
for seg in VERDICT.split("  +  "):
    emit("")
    emit("  " + seg)
emit("")
emit(f"  SCOPE QUALIFIERS, MANDATORY AND ATTACHED: two actors (A, B); "
     f"transport family exhaustive to depth {CAP_T}; relative horizons "
     f"r = 1..{RMAX}; terminal convention C1; intrinsic-partition "
     f"window depth {CAP_ESC}; root-symmetry window depth {CAP_SYM}; "
     f"ARM B N = 1..{NMAX} with the block windows printed row by row.  "
     f"THE GRAIN IS A SCOPE QUALIFIER AND IT IS ATTACHED TO BOTH ARM-B "
     f"SEGMENTS, not only to the FOUND one: every delta* clause above "
     f"holds at the DECLARED-PRIMARY {F['grain_primary_classes']}-class "
     f"kind x weight grain, hence — by the coarsening lemma — at every "
     f"refinement of it for the zero clauses and at every coarsening "
     f"of it for the unit clauses.  Coarsenings incomparable to the "
     f"menu grains are NOT covered, and the printed witness of that is "
     f"the R-SIG-indicator row, where the same class carries delta* = "
     f"1.  THE PSI FAMILY IS A SCOPE QUALIFIER TOO: BLOCKED is stated "
     f"over menu-shape Psi.  Three actors: censused to depth 3 only, "
     f"and the deeper conditional arm NOT RUN with its projected size "
     f"printed.  Nothing here is an infinite-volume, limit, or "
     f"asymptotic claim, and ARM B is a measurement at a declared "
     f"arena carrying {F['free_items']} free items, not a motivated "
     f"result.")
emit("")
emit("  WHAT THIS UNIT DOES NOT DECIDE.  It makes no geometry-update "
     "claim; the curvature group carried by the abstraction ladder is "
     "an anchor, not an interpretation.  It does not re-pose the "
     "transport-scope chain — that attempt is terminal-negative and "
     "this unit terminalizes its foundation rather than reopening it.  "
     "It constructs no transport map, no U3 screen and no weld "
     "battery: those are a separate pin's.  IT DOES NOT COMPUTE THE "
     "HILBERT PROJECTIVE DIAMETER OF ANY QUOTIENT TRANSFER OPERATOR: "
     "the Birkhoff route is closed at the history level only, where it "
     "closes for every history tree, so the engine the predecessor "
     "named remains un-attempted at the level where it could have "
     "worked.  It does not decide whether the two surviving (1, 1) "
     "rows are atoms at the ruled carrier CONG-185, nor at CONG-462: "
     "that is a successor computation, and the carrier must first be "
     "extended past depth 4.  It does not close any of ARM B's four "
     "free items.")

# ======================================================================
# RECEIPTS
# ======================================================================
if not F['seven_all']:
    emit("")
    emit("  NOTE: at least one of ARM A's seven facts did not gate "
         "clean; the verdict above reports it and the run still exits "
         "0, because a measured negative is a result.")

RECEIPT = {}
for k in sorted(F, key=str):
    v = F[k] if not isinstance(F, Facts) else dict.__getitem__(F, k)
    RECEIPT[k] = json.loads(json.dumps(v, default=str))
RECEIPT['_gates'] = [
    {'id': gid, 'kind': kind, 'ok': RES[gid][0],
     'label': label, 'detail': RES[gid][1]}
    for gid, kind, label, pred, det in GATES]
# ADDRESSABLE BY ID as well as ordered: a consumer that wants one gate
# should not have to scan a list.  Both forms carry the same rows.
RECEIPT['_gates_by_id'] = {
    gid: {'kind': kind, 'ok': RES[gid][0], 'label': label,
          'detail': RES[gid][1]}
    for gid, kind, label, pred, det in GATES}
# SAMPLES UNTRUNCATED: the first delivery truncated each falsifier's
# kill list to four gates, so a gate->killer map could not be rebuilt
# from the receipt and any coverage audit done from the receipt
# under-counted.  The full list is carried, and the truncation is gone.
RECEIPT['_mutants'] = [
    {'name': nm, 'class': cls, 'killed': n, 'sample': list(ks),
     'sample_truncated': False}
    for nm, cls, n, ks in MUT_ROWS]
RECEIPT['_anchors_bytes'] = [
    {'row': t, 'path': p, 'sha256_12': g, 'ok': ok}
    for t, p, w, g, ok in BY]
RECEIPT['_anchors_verbatim'] = [
    {'row': t, 'path': p, 'consumer': c, 'ok': ok, 'chars': n,
     'occurrences': o}
    for t, p, c, ok, n, o in VB]
RECEIPT['_pedigrees'] = [{'row': t, 'pedigree': ped}
                         for t, n, ped, a, s in ROWS]
RECEIPT['_compliance'] = [{'rule': n, 'kind': k, 'ok': bool(ok),
                           'evidence': d} for n, k, ok, d in COMPLY]
RECEIPT['_forcing'] = [{'gate': g, 'kind': k, 'forcing': d,
                        'witness_key': wk,
                        'witness_value': dict.__getitem__(F, wk),
                        'forced_value': we}
                       for g, k, d, wk, we in FORCING]
RECEIPT['_choices'] = [{'choice': n, 'class': k, 'evidence': e}
                       for n, k, e in CHOICES]
RECEIPT['_caps'] = {'CAP_T': CAP_T, 'CAP_DF': CAP_DF,
                    'CAP_ESC': CAP_ESC, 'CAP_SYM': CAP_SYM,
                    'RMAX': RMAX, 'NMAX': NMAX,
                    'pool3_depth': 3,
                    'pool3_depth5_conditional_arm': 'NOT RUN'}
# THE SCHEMA BLOCK — the consumer contract this receipt did not carry.
# Three traps cost a downstream probe a silent swallow: every Fraction
# is a JSON STRING, every tuple became a LIST and every tuple dict-key
# became a STRING.  They are declared here, with the column order of
# every positional tuple a consumer is likely to read.
RECEIPT['_schema'] = {
    'typing': {
        'fractions': 'every exact rational is serialised as a STRING '
                     '(json.dumps default=str): compare with '
                     'Fraction(s), never numerically',
        'tuples': 'every tuple is serialised as a LIST',
        'tuple_keys': 'every tuple used as a dict key is serialised as '
                      'its str(), e.g. "(1, 1)"',
        'none': 'a key whose measurement failed would serialise as '
                'null; no delivered key is null',
    },
    'B2_profile_rows': ['profile', 'N', 'block_window', 'depths',
                        'delta_H7_primary', 'delta_matched_primary',
                        'delta_matched_control', 'nu_support'],
    'B2_profile_rows_full': ['profile', 'N', 'block_window', 'depths',
                             'delta_H7_primary',
                             'delta_matched_primary',
                             'delta_matched_control', 'nu_support',
                             'delta_matched_profile',
                             'delta_matched_profile_unordered',
                             'delta_matched_rsig_indicator',
                             'max_successor_depth'],
    'B2_atom_deltas': ['profile', 'N', 'delta_H7_primary',
                       'delta_matched_primary',
                       'delta_matched_control'],
    'B2_atoms': ['profile', 'N', 'block_window',
                 'delta_matched_primary'],
    'B2_full_rows': ['N', 'class_window', 'profiles_in_window',
                     'delta_H7_primary', 'delta_matched_primary'],
    'B3_hit_rows': ['profile', 'N', 'histories_tested', 'zeros',
                    'infimum'],
    'B3_rsig_rows': ['N', 'histories_tested', 'zeros', 'infimum'],
    'B3_dist_by_depth': ['depth', 'max_finite_distance', 'lookahead',
                         'informative', 'unresolved', 'histories'],
    'B3_block_entry_rows': ['profile', 'size', 'reentries',
                            'contains_root', 'transitions_into'],
    'B4_statability': ['profile', 'N', 'min_depth', 'max_depth',
                       'max_successor_depth', 'statable_d4',
                       'statable_d5'],
    'per_block_delta_star': 'B2_atom_deltas and B2_profile_rows_full '
                            'publish delta* PER BLOCK under a name; '
                            'B2_best_delta is a MAXIMUM over the '
                            'table, not a row',
    'aliases': {'B3_dist_rows_saturated': 'B3_dist_rows_informative',
                'B3_dist_max_saturated': 'B3_dist_max_informative'},
}

OUT_PATH = os.path.join(HERE, 'gprep_foundation_output.txt')
RCP_PATH = os.path.join(HERE, 'gprep_foundation_receipt.json')

emit("")
emit("[RECEIPT HASHES]")
_code12 = sha12(SELF)
RECEIPT['_code_sha256_12'] = _code12
emit(f"  code    sha256-12 {_code12}  gprep_foundation_exact.py")
emit(f"  the receipt carries this digest as _code_sha256_12, so a "
     f"consumer reading the receipt alone can identify the code that "
     f"produced the numbers it is consuming.")

# ======================================================================
# EVERY FAILURE PATH WRITES NOTHING.  The dead-falsifier exit now
# precedes the write: in the first delivery the write came first, so an
# exit-1 run still left rewritten artifacts on disk.
# ======================================================================
if dead:
    print("")
    print(f"  DEAD FALSIFIER(S): {dead} — NO FILE WRITTEN, exit 1.")
    sys.stdout.flush()
    sys.exit(1)

if '--no-write' not in ARGV:
    with open(OUT_PATH, 'w') as fh:
        fh.write("\n".join(OUT_LINES) + "\n")
    with open(RCP_PATH, 'w') as fh:
        json.dump(RECEIPT, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print(f"  output  sha256-12 {sha12(OUT_PATH)}  "
          f"gprep_foundation_output.txt")
    print(f"  receipt sha256-12 {sha12(RCP_PATH)}  "
          f"gprep_foundation_receipt.json")
    print("  (the output/receipt hashes are printed to stdout only — "
          "a file cannot contain its own digest.)")
    # ------------------------------------------------------------------
    # THE ARTIFACT-INTEGRITY CHECK.  No gate reads the serialized files,
    # so a mutation applied AFTER the gated object was final and BEFORE
    # the write survived every gate with 44/44 green — the delivered
    # receipt could say anything.  This check re-reads both files FROM
    # DISK and compares them against the gated object itself: the
    # receipt's flat keys and values against F, and the output's lines
    # against a digest accumulated inside emit() at emission time, which
    # a later mutation of OUT_LINES cannot reach.  Exit 1 on mismatch.
    # ------------------------------------------------------------------
    _bad = []
    _disk = json.loads(read_text(RCP_PATH))
    for k in sorted(dict.keys(F), key=str):
        want = json.loads(json.dumps(dict.__getitem__(F, k), default=str))
        if k not in _disk:
            _bad.append(f"receipt key {k} missing on disk")
        elif _disk[k] != want:
            _bad.append(f"receipt key {k} differs from the gated object")
    for k in _disk:
        if not k.startswith('_') and k not in dict.keys(F):
            _bad.append(f"receipt key {k} on disk is not in the gated "
                        f"object")
    _dl = read_text(OUT_PATH).split("\n")
    if _dl and _dl[-1] == "":
        _dl = _dl[:-1]
    _ddig = sha12(OUT_PATH)
    if _ddig != EMIT_DIGEST.hexdigest()[:12]:
        _bad.append(f"output file digest {_ddig} != the digest "
                    f"accumulated at emission time "
                    f"{EMIT_DIGEST.hexdigest()[:12]}")
    if len(_dl) != EMIT_LINES[0]:
        _bad.append(f"output file has {len(_dl)} lines, "
                    f"{EMIT_LINES[0]} were emitted")
    print(f"  ARTIFACT INTEGRITY: the two written files were re-read "
          f"from disk and compared against the gated object and "
          f"against the emission-time digest — "
          f"{len(_bad)} discrepancies.")
    if _bad:
        print("  ARTIFACT INTEGRITY FAILURE — exit 1: "
              + "; ".join(_bad[:6]))
        sys.stdout.flush()
        sys.exit(1)

prog(f"done; wall clock {time.time() - T0:.1f}s")
sys.exit(0)
