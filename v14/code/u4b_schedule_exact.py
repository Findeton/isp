#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
v14 U4b -- THE SCHEDULE CENSUS.  Instrument for `v14/paper-17-schedule-census.md`.

QUESTION (pin `v14/note-u4b-pin.md`, sha256-12 d2cff9a274a8, ledger #126).  U4
measured the division-event crystal TRUE and the panel proved its periodicity
CONSTRUCTOR-INHERITED (the affine mechanism: n = c + m*1_S, S a union of
<(1,1)> cosets seated by d66's seed rule).  U4b turns the constructor into a
variable.  Over the declared family of admissible arbitration schedules on
CONFLICT-GRID(g=3, R=2) -- the committed diagonal-coset seed ONE point in it,
not its generator -- does crystallinity survive only at coset-union seeds
(INHERITED), or does it appear at beyond-coset schedules (emergence's first
foothold)?  And does ANY schedule induce a NON-DEGENERATE metric?

WHAT THIS PROGRAM DOES
  SEC 1  PROVENANCE.  Ten pinned sources, sha256-12 verified, products gated;
         the verbatim (#62) anchors bound to their consumer gates.
  SEC 2  THE GRAMMAR, DRIVEN DIRECTLY.  The committed d42b1 transport layer is
         loaded by text-slice (d66's own committed single-source idiom, cut at
         its banner print) and d60's `B`/`dl` and d66's `conflict_grid` by AST
         extraction.  Admissibility is decided by the layer's own menu; no menu
         law is re-typed anywhere in this file.
  SEC 3  THE FAMILY (pin R1), declared as data and COUNTED; the declared
         grammar window, disclosed; the committed schedule located inside it.
  SEC 4  CONSTRUCTIBILITY (pin R2.1) by driving the menus: FORCED / BRANCHING /
         REFUSED per schedule, with two declared controls that exhibit the two
         negative fates.
  SEC 5  THE STABILIZER COLUMN (pin R2.2) at BOTH site readings, by three
         independent routes (direct translation, Fourier annihilator in Z[w],
         subgroup lattice), full family and window.
  SEC 6  THE DETERMINANT COLUMN (pin R2.3): the induced I7 form per schedule
         through HA 3.2's readout as the U4 effectus evaluated it; det exact.
  SEC 7  THE AFFINE NULL (pin R3): coset-union vs beyond-coset, and the
         verdict stratified over it.
  SEC 8  FRAGILITY (pin R2.4) on the window, computed not sampled.
  SEC 9  THE WALLS (pin R4): L-1 argued first and declined; BHS; KR; the
         diagonal counterpoint measured, cosmological readings barred.
  SEC 10 The verdict, derived a second time from the serialized receipt by an
         independent path; the paper gates; the seal; the artifacts.

CLI CONTRACT (the #82 minimum: argv-parsed against a whitelist)
---------------------------------------------------------------
    python3.13 v14/code/u4b_schedule_exact.py
        THE DELIVERY RUN, and the ONLY writer.  Builds the whole census,
        evaluates every gate (the paper gates included), runs every declared
        mutant in-process, re-reads what it wrote and WRITES
        `u4b_schedule_output.txt` and `u4b_schedule_receipt.json` beside this
        file.  Exits 0 iff every gate passes.

    python3.13 v14/code/u4b_schedule_exact.py --no-write
        The same run, writing nothing.

    python3.13 v14/code/u4b_schedule_exact.py --numbers
        The census and the paper gates: every published row printed, then the
        registered numerals and the instrument's claims.  No mutant sweep, no
        seal close, nothing written.  Exits 0 iff every gate it reaches passes.

    python3.13 v14/code/u4b_schedule_exact.py --selftest
        FALSIFICATION SELF-TEST.  Corrupts one anchor's expected digest IN
        MEMORY, confirms the run dies at the anchor gate, WRITES NOTHING, and
        exits 1.  Exits 2 if the corrupted run does NOT die.

    python3.13 v14/code/u4b_schedule_exact.py --mutant NAME
        Runs the pipeline with the named mutant active.  Exits 1 when the
        mutant is killed (the intended outcome), 0 if it survives.  An unknown
        NAME exits 2.  Writes nothing.

    python3.13 v14/code/u4b_schedule_exact.py --break-anchor NAME
        Corrupts the named source anchor's expected digest.  Unknown NAME exits
        2.  The run must exit 1.  Writes nothing.

    python3.13 v14/code/u4b_schedule_exact.py --verify-paper [PATH]
        Rebuilds the whole derivation and evaluates the paper gates -- claim
        rendering, numeral coverage and claim POLARITY -- with PATH (this
        unit's paper by default) as the object under test.  Exits 1 on any
        drift, 0 on a clean paper, 2 if PATH does not exist.  Writes nothing.

    Any other argument, any unknown flag argument, any missing flag argument,
    any REPEATED flag, and any --verify-paper PATH that is not an existing FILE
    (a directory and the empty string are not papers) exits 2.  No flag is
    mutant-only, no flag is a no-op, and no COMBINATION is: the mutant is bound
    before --selftest is dispatched, so `--selftest --mutant NAME` is honoured.

THE GATE-TO-DISK SEAL (RUNBOOK 14 addendum, v14 #119 with the #148 TOTALITY
addendum).  Every published object is DIGESTED AT THE MOMENT ITS GATE PASSES;
the payload may only be sealed if every earlier seal still verifies; the
artifacts are written FROM the sealed payload; the terminal integrity gate
compares the BYTES ON DISK against the gate-time seal, and a failure after the
replace RESTORES the previous artifacts.  A re-derivation from disk is not an
integrity check -- it confirms corruption.

TOTALITY.  Every published receipt key is sealed at its own gate or carried on
a DECLARED-UNSEALED manifest with a reason and a gate that binds it instead;
both manifests are published.  A DECLARED seal that was never TAKEN counts as
BROKEN, so a seal cannot be dropped without trace, and the completeness gate
compares the manifest against the DECLARATION rather than its own contents.
The seal covers what this program VOUCHES FOR -- its provenance rows, its
claims about its own paper, its coverage and polarity rows -- as well as what
it measured.  The gate ledger is CHAINED one row at a time rather than sealed
once; the transcript is chained line by line as it is written; and the closing
counts are DERIVED at close from the sealed rows.

TEXT GATES (RUNBOOK 14 addendum, v14 #125, as this unit's adjudication
clarified it).  Every gate that matches prose against a needle ASCII-folds both
sides, STRIPS LEADING MARKDOWN LINE-DECORATIONS -- blockquote markers, list
bullets, heading hashes, ordered-list numbers -- and only then
whitespace-normalises, uses #62-anchored needles with a length floor, and
includes the corpus's canonical short fragments.  The four inherited U4 walls
are enforced that way, and the blockquote is the wrapping the corpus itself
writes when it quotes a prior unit.

COVERAGE (#34, with reachability).  The denominator is the DECLARED gate
universe and the ledger is required to equal it; every FALSIFIABLE row's named
mutant must have its measured `killed_at` equal to that row's own gate.

ARITHMETIC.  Exact only: `fractions.Fraction` and Python integers.  There are
no floats anywhere -- an AST scan of this file and a recursive type scan of the
emitted receipt are gates.

RUNTIME INPUTS (RUNBOOK 13/14, engravings #46/#91).  Exactly ten files are read
at run time as SOURCES, all hash-pinned by this unit's frozen declaration, plus
exactly one file read as the OBJECT UNDER TEST -- this unit's own paper, which
cannot be hash-pinned because it is the thing being verified.  Both lists are
enumerated and gated.  No repository state outside them is read, and no
subprocess -- in particular no `git` -- is ever invoked: the run is correct
off-tree and in a directory with no version control at all.
"""

import ast
import hashlib
import json
import os
import re
import sys
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product

sys.setrecursionlimit(100000)

SELF = os.path.abspath(__file__)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(SELF)))
OUT_TXT = os.path.join(os.path.dirname(SELF), "u4b_schedule_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "u4b_schedule_receipt.json")

SCHEMA = "isp/v14/u4b-schedule-census/1"
PAPER_REL = "v14/paper-17-schedule-census.md"

# ===========================================================================
# SECTION 0.  THE FROZEN DECLARATION (RUNBOOK section 15: the arena is data)
# ===========================================================================

SOURCES = [
    ("A-PIN", "v14/note-u4b-pin.md", "d2cff9a274a8",
     "THIS UNIT'S PIN (ledger #126): the family, the columns, the "
     "pre-registered outcome names."),
    ("A-ADJ", "v14/note-u4-adjudication.md", "fa991e19ae54",
     "the U4 adjudication (#125): the affine mechanism, the diagonal "
     "unification, the successor ruling that pinned this unit."),
    ("A-EFF", "v14/review-u4-effectus.md", "61fb7d9e8471",
     "the U4 effectus review (#122): the I7-coordinate evaluation route and "
     "the committed CONFLICT-GRID(3,2) I7 row this unit reproduces."),
    ("A-HA", "v13/paper-ha-successor.md", "f286ba10d2d9",
     "HA 3.2: the declared readout -- interval cardinality as squared "
     "separation -- that turns link counts into a metric candidate."),
    ("A-D42B1", "v10/code/d42b1_transport_exact.py", "576275d55ecf",
     "THE COMMITTED TRANSPORT GRAMMAR, driven directly: this unit's only "
     "source of admissibility."),
    ("A-D60", "v10/code/d60_crystal_exact.py", "684cdb76552b",
     "D60: the Builder `B` and the delivery helper `dl`, AST-extracted."),
    ("A-D66", "v10/code/d66_arbitration_crystal_exact.py", "3d0516ab106e",
     "D66: CONFLICT-GRID(g, R) -- the committed constructor whose schedule "
     "this unit turns into a variable, AST-extracted and re-run."),
    ("A-D66OUT", "v10/data/d66_arbitration_crystal_exact.out", "e252529d2586",
     "D66's COMMITTED OUTPUT: the GRID(g=3,*) rows are READ from this file at "
     "run time and reproduced, never re-typed."),
    ("A-L1", "v11/note-L1-lorentz-no-go-lemma.md", "93ea24591c3c",
     "L-1: the fourth-form clause this unit argues before any test, and the "
     "sentence retracted on 2026-07-28 that no paper may reproduce."),
    ("A-CAT", "v11/note-v11p0a-reproduction-catalog.md", "0cebe543e814",
     "the reproduction catalog 1.6/1.7: the BHS block and the "
     "Kleitman-Rothschild height-control warning."),
]
SOURCE_IDS = [s[0] for s in SOURCES]

MUTANTS = [
    ("MUT-CRYSTAL-SEEDED", "G-BEYOND-COSET-CRYSTALLINE",
     "reports the beyond-coset crystalline population as empty, forcing the "
     "pre-registered CRYSTAL-SEEDED outcome -- must die at the per-witness "
     "beyond-coset gate"),
    ("MUT-AFFINE-NULL", "G-AFFINE-LAW",
     "reports one coset-union schedule as non-crystalline -- must die at the "
     "affine-law gate, which evaluates every CU-JOINT seed pair"),
    ("MUT-CU-SPLIT", "G-CU-SPLIT-EMPTY",
     "reports a CU-SPLIT schedule as crystalline -- must die at the "
     "split-coset gate"),
    ("MUT-DET-EMPTY", "G-DET-NONZERO-EXISTS",
     "reports the determinant column as identically zero -- must die at the "
     "named-witness determinant gate"),
    ("MUT-DET-POSDEF", "G-POSDEF-EMPTY",
     "plants a positive-definite-at-every-site schedule -- must die at the "
     "exhaustive positive-definiteness census gate"),
    ("MUT-I7-STRICT", "G-I7-STRICT-EMPTY",
     "reports a schedule meeting I7's strict-positivity criterion -- must die "
     "at the strict-positivity census gate"),
    ("MUT-STAB-ROUTE", "G-STAB-ROUTES",
     "corrupts the Fourier-annihilator route on one field -- must die at the "
     "three-route agreement gate"),
    ("MUT-FOOTPRINT", "G-FOOTPRINT-CONSTANT",
     "makes one schedule's footprint field non-constant -- must die at the "
     "per-schedule footprint gate"),
    ("MUT-DRIVEN-FIELD", "G-DRIVEN-EQUALS-COMBINATORIAL",
     "detaches one driven record's division field from the combinatorial one "
     "-- must die at the per-schedule driven-vs-combinatorial gate"),
    ("MUT-NOT-FORCED", "G-CONSTRUCTIBILITY",
     "withholds one conflict-supply delivery from one window schedule, "
     "leaving a refused record reported as FORCED -- must die at the "
     "per-schedule constructibility gate"),
    ("MUT-REFUSAL-BLIND", "G-CTRL-REFUSED",
     "reports the declared no-supply control as constructible -- must die at "
     "the refusal control gate"),
    ("MUT-BRANCHING-BLIND", "G-CTRL-BRANCHING",
     "reports the declared under-specified control as forced -- must die at "
     "the branching control gate"),
    ("MUT-COMMITTED-RECORD", "G-COMMITTED-RECORD",
     "perturbs one event of the generalized driver's committed-schedule "
     "record -- must die at the event-for-event anchor against d66's own "
     "`conflict_grid(3, 2)`"),
    ("MUT-FAMILY-COUNT", "G-FAMILY-COUNT",
     "corrupts the computed family size -- must die at the two-route count "
     "gate (#24)"),
    ("MUT-WINDOW-SILENT", "G-WINDOW-DISCLOSED",
     "reports the declared window as the whole family -- must die at the "
     "no-silent-caps disclosure gate"),
    ("MUT-FRAGILITY", "G-FRAGILITY",
     "reports one admissible single-arbitration re-seating as preserving the "
     "stabilizer -- must die at the per-schedule fragility gate"),
    ("MUT-WALL-L1", "G-WALL-L1",
     "injects the retracted L-1 sentence into the paper under test, "
     "LINE-WRAPPED in house style -- must die at the whitespace-normalised "
     "L-1 wall gate (#125)"),
    ("MUT-WALL-BHS", "G-WALL-BHS",
     "runs a sprinkling-grade boost reading -- must die at the BHS wall gate"),
    ("MUT-HEAD", "G-VERDICT-RECONSTRUCTED",
     "corrupts one field of the head -- must die at the independent "
     "reconstruction gate"),
    ("MUT-SEAL-BROKEN", "G-SEAL-COMPLETE",
     "mutates a sealed object after its gate passed -- must die at the "
     "gate-time seal verification (#119)"),
    ("MUT-SELFTEST-WRITES", "G-SELFTEST-WRITES-NOTHING",
     "lets the self-test path reach a writer -- must die at the "
     "writes-nothing gate"),
    ("MUT-CLI-PERMISSIVE", "G-CLI-WHITELIST",
     "swaps the argv whitelist for the registered permissive shape -- must "
     "die at the CLI contract gate (#82)"),
    ("MUT-PAPER-POLARITY", "G-PAPER-CLAIM-POLARITY",
     "flips one declared polarity of the paper's head -- must die at the "
     "polarity gate"),
    ("MUT-VERBATIM", "G-VERBATIM",
     "corrupts one verbatim source quote -- must die at the #62 anchor gate"),
    ("MUT-ANCHOR-DRIFT", "G-ANCHORS-READ",
     "moves one number recomputed against a committed file -- must die at "
     "the read-anchor gate (which --break-anchor cannot reach, because the "
     "provenance gate kills that run first)"),
    ("MUT-STRATUM-BLIND", "G-STRATA-WITNESSED",
     "drops one census stratum's driven witness -- must die at the "
     "every-stratum-witnessed gate"),
    ("MUT-CLASSPAIR", "G-CLASS-PAIR-TABLE",
     "corrupts one row of the resolvable class-pair table -- must die at the "
     "per-row gate that binds it to the whole-family determinant column"),
    ("MUT-WALL-KR", "G-WALL-KR",
     "takes a dimension reading with no height control -- must die at the "
     "Kleitman-Rothschild wall gate"),
    ("MUT-WALL-COSMO", "G-WALL-DIAGONAL",
     "reads the measured diagonal cosmologically -- must die at the "
     "diagonal wall gate"),
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS",
     "silently drops one instrument claim from the paper under test -- must "
     "die at the claim-rendering gate"),
    ("MUT-PAPER-NUMERAL", "G-PAPER-NUMERAL-COVERAGE",
     "injects an unregistered numeral into the paper under test -- must die "
     "at the numeral-coverage gate"),
    # ---- the repaired heads: falsifiers for the census blocks added at
    # ---- adjudication, one per new gate
    ("MUT-UNION-CARRIER", "G-UNION-CARRIER",
     "reports one crystalline seed pair whose division field is NOT supported "
     "on a union of cosets of its own period -- must die at the "
     "union-carrier gate, which evaluates all 252 crystalline pairs"),
    ("MUT-LINE-SEED", "G-NO-LINE-SEED",
     "reports one beyond-coset crystalline pair as having a line seed -- must "
     "die at the per-pair no-line-seed gate"),
    ("MUT-FRAG-FAMILY", "G-FRAGILITY-FAMILY",
     "reports one family-scope re-seating as leaving a nontrivial period -- "
     "must die at the 9072-case family fragility gate"),
    ("MUT-JOINT-COUPLING", "G-PERIOD-DIAGONAL-JOINT",
     "reports the period and the diagonal link count as jointly independent "
     "-- must die at the measured-coupling gate"),
    ("MUT-POSDEF-CEILING", "G-POSDEF-CEILING",
     "moves the positive-definite site histogram -- must die at the "
     "exhaustive ceiling gate"),
    ("MUT-INCIDENCE-WALL", "G-INCIDENCE-WALL",
     "reports a partition pair depositing more than the budget's link "
     "incidences, or a positive-definite site holding fewer than three -- "
     "must die at the counting-wall gate that carries both theorems"),
    ("MUT-R3-SATURATION", "G-R3-SATURATION",
     "corrupts the successor probe's saturating arrangement -- must die at "
     "the R=3 gate"),
    ("MUT-I7-READOUT", "G-I7-READOUT",
     "corrupts the induced form at ONE site of the committed schedule, which "
     "the single-row read anchor cannot see -- must die at the nine-site "
     "readout gate"),
    ("MUT-STAB-WEIGHT", "G-STAB-FULL-FAMILY",
     "corrupts the transversal weight that licenses the exhaustive stabilizer "
     "column -- must die at the full-family gate (the falsifier the coverage "
     "ledger previously mis-credited to a gate eight rows earlier)"),
    ("MUT-ORDER-VARIANT", "G-ORDER-INVARIANCE",
     "reports one processing-order variant as changing the record -- must die "
     "at the order-invariance gate"),
    # ---- the seam: the five injections the instrument review exploited at
    # ---- exit 0, each now a declared mutant that dies at a named gate
    ("MUT-VOUCH-FORGED", "G-SEAL-COMPLETE",
     "forges the four VOUCHING rows -- provenance, paper claims, paper "
     "coverage, paper polarity -- after their gates passed, the injection "
     "that previously left the receipt publishable at exit 0; must die at "
     "the completeness gate now that the vouching layer is sealed"),
    ("MUT-SCHEMA-FORGED", "G-DECLARED-UNSEALED",
     "forges the two declared-unsealed rows, the receipt schema and the path "
     "of the object under test -- must die at the gate that binds them"),
    ("MUT-SEAL-DROPPED", "G-SEAL-COMPLETE",
     "deletes one DECLARED seal without trace, which previously left both "
     "artifacts byte-identical to the honest run -- must die at the "
     "completeness gate, which now compares the manifest against the "
     "DECLARATION rather than against what it happens to contain"),
    ("MUT-CTRL-ROW", "G-SEAL-COMPLETE",
     "moves a control row under its label after its own gate passed -- must "
     "die at the completeness gate now that each control is sealed at its "
     "own gate and its gate reads the published row"),
    ("MUT-TOTALS-FORGED", "G-SEAL-COMPLETE",
     "forges the instrument's own totals after their gate -- must die at the "
     "completeness gate now that the totals close in run rather than at the "
     "last gate of all"),
    ("MUT-TRANSCRIPT-HEAD", "G-TRANSCRIPT-BOUND",
     "flips the head in the transcript's own line buffer, the injection that "
     "previously published two artifacts stating opposite verdicts with the "
     "receipt byte-identical -- must die at the transcript chain gate"),
    ("MUT-GATE-UNIVERSE", "G-GATE-UNIVERSE",
     "hides one gate from the coverage ledger's denominator -- must die at "
     "the honest-denominator gate (#34)"),
    ("MUT-WALL-L1-QUOTED", "G-WALL-L1",
     "injects the retracted L-1 sentence as a MARKDOWN BLOCKQUOTE, the "
     "corpus's own house style for quoting a prior unit and the wrapping the "
     "whitespace-only fold walked past -- must die at the L-1 wall gate under "
     "the markdown-prefix normalisation (#125)"),
]
MUTANT_NAMES = {m[0] for m in MUTANTS}

# the retracted L-1 sentence: no paper of this line may reproduce it
BANNED_L1 = ("precisely the form U4 tests, and precisely the form the "
             "corpus's strongest relativity result took")

MUT = None
QUIET = False
LINES = []
READS = []


class GateFail(Exception):
    pass


class CliError(Exception):
    pass


TRANSCRIPT_CHAIN = ["<transcript-genesis>"]


def say(s=""):
    LINES.append(s)
    TRANSCRIPT_CHAIN[0] = _chain_step(TRANSCRIPT_CHAIN[0], s)
    if not QUIET:
        print(s, flush=True)


def transcript_state():
    """the transcript is a published artifact, so it is chained as it is
    written; this pair is saved and restored around every quiet sub-run."""
    return list(LINES), TRANSCRIPT_CHAIN[0]


def transcript_restore(state):
    LINES[:] = state[0]
    TRANSCRIPT_CHAIN[0] = state[1]


def transcript_chain_of(lines):
    acc = "<transcript-genesis>"
    for s in lines:
        acc = _chain_step(acc, s)
    return acc


def mut(name):
    return MUT == name


def pick(name, normal, corrupted):
    """the mutant hook: returns `normal` unless this run is that mutant."""
    return corrupted if MUT == name else normal


# ===========================================================================
# SECTION 1.  MACHINERY -- the gate ledger, the waiver ledger, the seal
# ===========================================================================

class Ledger:
    """gates carry their verdict IN the statement; a failure raises.

    The ledger is CHAINED: each row extends a rolling digest at the moment the
    gate passes, so `gates` is sealed row by row rather than once at the end.
    A row edited, dropped or appended after its gate breaks the chain."""

    def __init__(self):
        self.rows = []
        self.chain = "<ledger-genesis>"

    def gate(self, name, statement, ok, evidence, waiver=None):
        ok = bool(ok)
        self.rows.append({"gate": name, "statement": statement,
                          "passed": ok, "evidence": str(evidence),
                          "waiver": waiver})
        self.chain = _chain_step(self.chain, digest(self.rows[-1]))
        say("  [%s] %s" % ("PASS" if ok else "FAIL", name))
        say("         %s" % statement)
        say("         evidence: %s" % evidence)
        if waiver:
            say("         WAIVER [%s]: %s" % (waiver["class"], waiver["reason"]))
        if not ok:
            raise GateFail("%s :: %s" % (name, evidence))
        return ok


def digest(value):
    if isinstance(value, str):
        return hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]
    return hashlib.sha256(
        json.dumps(value, indent=1, sort_keys=True, default=str).encode("utf-8")
    ).hexdigest()[:12]


def _chain_step(acc, item):
    return hashlib.sha256(("%s|%s" % (acc, item)).encode("utf-8")).hexdigest()[:12]


def jpath(obj, path):
    cur = obj
    for part in path.split("/"):
        cur = cur[int(part)] if isinstance(cur, list) else cur[part]
    return cur


# THE SEAL MANIFEST (#119 + the v14 #148 totality addendum).  EVERY published
# receipt key is either sealed AT THE GATE THAT CERTIFIES IT, or carried on
# the declared-unsealed manifest below with a reason and its own gate.  The
# adjudication's finding this repairs: the delivery sealed WHAT IT MEASURED
# and left unsealed WHAT IT VOUCHED FOR -- provenance, the paper rows, the
# transcript -- which are exactly the rows a reader cannot recompute.
SEALED_PATHS = [
    ("SEAL-VERDICT-CRYSTAL", "verdict/crystal", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-VERDICT-DET", "verdict/det", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-VERDICT-CONSTR", "verdict/constructibility",
     "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-COUNTS", "counts", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-PROVENANCE", "provenance", "G-PROV-ALL"),
    ("SEAL-FAMILY", "family", "G-WINDOW-DISCLOSED"),
    ("SEAL-CONSTR-FATES", "constructibility/fates", "G-CONSTRUCTIBILITY"),
    ("SEAL-CTRL-REFUSED", "constructibility/control_nosupply",
     "G-CTRL-REFUSED"),
    ("SEAL-CTRL-BRANCHING", "constructibility/control_underspecified",
     "G-CTRL-BRANCHING"),
    ("SEAL-CONSTRUCTIBILITY", "constructibility", "G-CTRL-BRANCHING"),
    ("SEAL-STABILIZER", "stabilizer", "G-STAB-FULL-FAMILY"),
    ("SEAL-DET-WITNESS", "determinant/witness", "G-DET-NONZERO-EXISTS"),
    ("SEAL-DET-CEILING", "determinant/posdef_site_histogram",
     "G-POSDEF-CEILING"),
    ("SEAL-DETERMINANT", "determinant", "G-INCIDENCE-WALL"),
    ("SEAL-CLASS-PAIRS", "class_pairs", "G-CLASS-PAIR-TABLE"),
    ("SEAL-AFFINE", "affine", "G-CU-SPLIT-EMPTY"),
    ("SEAL-CARRIER", "carrier", "G-UNION-CARRIER"),
    ("SEAL-JOINT", "period_vs_diagonal", "G-PERIOD-DIAGONAL-JOINT"),
    ("SEAL-FRAGILITY", "fragility", "G-FRAGILITY-FAMILY"),
    ("SEAL-STRATA", "strata", "G-STRATA-WITNESSED"),
    ("SEAL-ANCHORS", "anchors", "G-ANCHORS-READ"),
    ("SEAL-VERBATIM", "verbatim_anchors", "G-VERBATIM"),
    ("SEAL-ORDER", "processing_order", "G-ORDER-INVARIANCE"),
    ("SEAL-SUCCESSOR", "successor_probe", "G-R3-SATURATION"),
    ("SEAL-WALLS", "walls", "G-WALL-DIAGONAL"),
    ("SEAL-PAPER-CLAIMS", "paper_claims", "G-PAPER-CLAIMS"),
    ("SEAL-PAPER-COVERAGE", "paper_coverage", "G-PAPER-NUMERAL-COVERAGE"),
    ("SEAL-PAPER-POLARITY", "paper_polarity", "G-PAPER-CLAIM-POLARITY"),
    ("SEAL-WAIVERS", "waiver_ledger", "G-WAIVERS-VERIFIED"),
    ("SEAL-TOTALS", "totals", "G-TOTALS"),
    # taken after the in-run completeness gate, in the delivery path only,
    # each at the gate that certifies its own object
    ("SEAL-MUTANTS", "mutants", "G-MUTANTS-ON-TARGET"),
    ("SEAL-CLOSURE", "closure", "G-CLOSURE-DERIVED"),
]
# `gates` is not in the table above because it is not sealed once: it is
# CHAINED, one rolling digest step per row at the moment that row's gate
# passes, and the chain is checked at close.
POST_COMPLETENESS_SEALS = ("SEAL-MUTANTS", "SEAL-CLOSURE")
SEALS_IN_RUN = tuple(s for s, _p, _g in SEALED_PATHS
                     if s not in POST_COMPLETENESS_SEALS)

# the declared-unsealed manifest: published keys that are NOT digested at a
# gate, each with the reason and the gate that binds it instead.
UNSEALED_DECLARED = [
    ("schema", "a constant of this file, fixed before the first gate; it "
     "names the receipt's shape and is re-verified against its own "
     "definition", "G-DECLARED-UNSEALED"),
    ("paper", "the relative path of the object under test, fixed by the CLI "
     "before the first gate and re-verified here against the path actually "
     "read", "G-DECLARED-UNSEALED"),
    ("gates", "not sealed once but CHAINED row by row: each ledger row "
     "extends a rolling digest at the moment its gate passes, and the chain "
     "is recomputed from the published rows at close", "G-SEAL-CLOSE"),
    ("seals", "the manifest cannot digest itself; it is CONSTRUCTED at close "
     "from the seal rows actually taken, never read from mutable state",
     "G-SEAL-CLOSE"),
    ("seals_unsealed", "this manifest, constructed at close from the "
     "declaration above", "G-SEAL-CLOSE"),
    ("transcript", "the transcript's own chain digest, constructed at close; "
     "the transcript is chained line by line as it is written",
     "G-TRANSCRIPT-BOUND"),
]
UNSEALED_KEYS = tuple(k for k, _r, _g in UNSEALED_DECLARED)


class Seal:
    """the gate-time seal (#119), TOTALIZED (#148 addendum).

    Three properties this repair adds.  (1) A DECLARED seal that was never
    TAKEN counts as BROKEN, not as absent -- so a seal cannot be deleted
    without trace.  (2) The completeness gate compares the manifest against
    the DECLARATION, not against what happens to be in it.  (3) Closing
    requires TOTALITY: every published receipt key is sealed or on the
    declared-unsealed manifest."""

    def __init__(self):
        self.rows = []
        self.index = {}
        self.payload = None
        self.payload_sha = None
        self.transcript = None
        self.transcript_sha = None

    def take(self, sid, obj):
        path = [p for s, p, _g in SEALED_PATHS if s == sid][0]
        at = [g for s, _p, g in SEALED_PATHS if s == sid][0]
        d = digest(jpath(obj, path))
        self.rows.append({"seal": sid, "path": path, "sealed_at_gate": at,
                          "sha256_12": d})
        self.index[sid] = d

    def drop(self, sid):
        """used by MUT-SEAL-DROPPED only: delete a declared seal silently."""
        self.rows = [r for r in self.rows if r["seal"] != sid]
        self.index.pop(sid, None)

    def verify(self, obj, only=None):
        broken = []
        if only is not None:
            broken.extend(sid for sid in only if sid not in self.index)
        for row in self.rows:
            if only is not None and row["seal"] not in only:
                continue
            try:
                now = digest(jpath(obj, row["path"]))
            except (KeyError, IndexError, TypeError):
                broken.append(row["seal"])
                continue
            if now != row["sha256_12"]:
                broken.append(row["seal"])
        return sorted(set(broken))

    def manifest(self):
        return [dict(r) for r in self.rows]

    def totality(self, obj):
        """every published top-level key is sealed or declared unsealed."""
        sealed = {r["path"].split("/")[0] for r in self.rows}
        return sorted(set(obj) - sealed - set(UNSEALED_KEYS))

    def close(self, obj, ledger):
        """the seal's own closing gate, evaluated on the object about to be
        serialized: every declared seal taken, every taken seal still
        verifying, the ledger chain intact, and the receipt total."""
        obj["seals"] = self.manifest()
        obj["seals_unsealed"] = [{"key": k, "reason": r, "bound_by": g}
                                 for k, r, g in UNSEALED_DECLARED]
        untaken = [s for s, _p, _g in SEALED_PATHS if s not in self.index]
        broken = self.verify(obj)
        stray = self.totality(obj)
        chain_ok = (ledger is None
                    or _chain_of_rows(obj["gates"]) == ledger.chain)
        ok = not untaken and not broken and not stray and chain_ok
        payload = json.dumps(obj, indent=1, sort_keys=True, default=str)
        self.payload = payload
        self.payload_sha = digest(payload)
        return ok, {"declared": len(SEALED_PATHS), "taken": len(self.rows),
                    "untaken": untaken or "none", "broken": broken or "none",
                    "unsealed_declared": len(UNSEALED_DECLARED),
                    "published_keys": len(obj),
                    "unsealed_and_undeclared": stray or "none",
                    "ledger_chain_intact": chain_ok}

    def close_transcript(self, text):
        self.transcript = text
        self.transcript_sha = digest(text)


def _chain_of_rows(rows):
    acc = "<ledger-genesis>"
    for r in rows:
        acc = _chain_step(acc, digest(r))
    return acc


def read_bytes(rel):
    READS.append(rel)
    with open(os.path.join(REPO, rel), "rb") as fh:
        return fh.read()


def read_text(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


MD_PREFIX = re.compile(r"(?m)^[ \t]*(?:[>\-*+#]+|\d+[.)])[ \t]*")


def norm(s):
    """#125, as clarified by this unit's adjudication: strip LEADING MARKDOWN
    LINE-DECORATIONS -- blockquote markers, list bullets, heading hashes and
    ordered-list numbers -- and only then whitespace-normalise.  Both sides of
    every text match go through this.  The bare whitespace fold is not enough:
    the corpus's own house style for quoting a prior unit is the blockquote,
    so a prohibited sentence re-wrapped as `> ...` or `- ...` would otherwise
    walk straight through a prohibition gate."""
    return re.sub(r"\s+", " ", MD_PREFIX.sub(" ", s)).strip()


# ===========================================================================
# SECTION 2.  EXACT ARITHMETIC ON Z_3^2 AND Z[w]
# ===========================================================================

SITES = tuple((i, j) for i in range(3) for j in range(3))
SITE_INDEX = {s: k for k, s in enumerate(SITES)}
DIRECTIONS = ((1, 0), (0, 1), (1, 1), (1, 2))
I7_LINKS = ((1, 0), (0, 1), (1, 1))


def zadd(a, b):
    return ((a[0] + b[0]) % 3, (a[1] + b[1]) % 3)


def zmul(k, a):
    return ((k * a[0]) % 3, (k * a[1]) % 3)


SUBGROUPS = {"1": frozenset({(0, 0)}), "Z3^2": frozenset(SITES)}
for _d in DIRECTIONS:
    SUBGROUPS["<(%d,%d)>" % _d] = frozenset({(0, 0), _d, zmul(2, _d)})
SUBGROUP_NAME = {v: k for k, v in SUBGROUPS.items()}
SUBGROUP_ORDER = ["1", "<(1,0)>", "<(0,1)>", "<(1,1)>", "<(1,2)>", "Z3^2"]

# the 12 lines of AG(2,3): the cosets of the four order-3 subgroups
LINE_DIRECTION = {}
for _d in DIRECTIONS:
    for _x in SITES:
        LINE_DIRECTION[frozenset(zadd(_x, h)
                                 for h in SUBGROUPS["<(%d,%d)>" % _d])] = _d
AG_LINES = frozenset(LINE_DIRECTION)


def stab_direct(field):
    """ROUTE 1 -- the definition: translate the field and compare."""
    return frozenset(t for t in SITES
                     if all(field[zadd(x, t)] == field[x] for x in SITES))


# Z[w] = Z[t]/(t^2 + t + 1) carried as (a, b) = a + b*w, exact integers.
def w_pow(m):
    m %= 3
    return (1, 0) if m == 0 else ((0, 1) if m == 1 else (-1, -1))


def stab_fourier(field):
    """ROUTE 2 -- the annihilator of the support of the exact Z_3^2 Fourier
    transform in Z[w].  Shares no code and no constant with route 1."""
    support = []
    for k in SITES:
        acc = (0, 0)
        for x in SITES:
            c = field[x]
            if c == 0:
                continue
            p = w_pow(k[0] * x[0] + k[1] * x[1])
            acc = (acc[0] + c * p[0], acc[1] + c * p[1])
        if acc != (0, 0):
            support.append(k)
    return frozenset(t for t in SITES
                     if all((k[0] * t[0] + k[1] * t[1]) % 3 == 0
                            for k in support))


def stab_lattice(field):
    """ROUTE 3 -- the subgroup lattice: the largest H on whose cosets the
    field is constant."""
    best = SUBGROUPS["1"]
    for name in SUBGROUP_ORDER:
        H = SUBGROUPS[name]
        cosets = {}
        for x in SITES:
            key = frozenset(zadd(x, h) for h in H)
            cosets.setdefault(key, set()).add(field[x])
        if all(len(v) == 1 for v in cosets.values()) and len(H) > len(best):
            best = H
    return best


# ===========================================================================
# SECTION 3.  THE COMMITTED GRAMMAR, DRIVEN DIRECTLY
# ===========================================================================

EXIT_NAMES = ("exit", "quit", "_exit")


def no_exit(nodes):
    """d66's committed C0a form, adopted verbatim: no CALL and no bare
    NAME/ATTRIBUTE reference to an exit callable survives an extracted body."""
    for n in nodes:
        for c in ast.walk(n):
            if isinstance(c, ast.Attribute) and c.attr in EXIT_NAMES:
                return False
            if isinstance(c, ast.Name) and c.id in EXIT_NAMES:
                return False
    return True


class Grammar:
    """the committed layers, loaded as SINGLE SOURCES.  Nothing in this file
    re-implements an admissibility rule: `candidates_for` IS d42b1's."""

    def __init__(self, texts):
        st = texts["v10/code/d42b1_transport_exact.py"]
        cut = st.index('print("[d42b1')
        self.slice_text = st[:cut]
        self.slice_chars = (cut, len(st))
        ns = {}
        exec(compile(self.slice_text, "d42b1_slice", "exec"), ns)
        self.ns = ns
        self.candidates_for = ns["candidates_for"]
        self.admissible = ns["admissible"]
        self.regs_of = ns["regs_of"]
        self.vname = ns["vname"]
        self.V0 = ns["V0"]
        self.extracted = {}
        g60 = self._extract("v10/code/d60_crystal_exact.py", texts, "d60",
                            {"candidates_for": self.candidates_for,
                             "event_poset": ns["event_poset"], "V0": self.V0})
        self.B = g60["B"]
        self.dl = g60["dl"]
        g66 = self._extract("v10/code/d66_arbitration_crystal_exact.py", texts,
                            "d66",
                            {"B": self.B, "dl": self.dl, "vname": self.vname,
                             "V0": self.V0,
                             "candidates_for": self.candidates_for})
        self.conflict_grid = g66["conflict_grid"]
        self.slice_exit_free = ("sys.exit" not in self.slice_text
                                and no_exit(ast.parse(self.slice_text).body))
        self.bodies_exit_free = all(no_exit(v)
                                    for v in self.extracted.values())

    def _extract(self, rel, texts, marker, extra):
        """d60/d63/d64/d66's committed extraction idiom: keep only defs and
        classes, so no module-level statement can run."""
        tree = ast.parse(texts[rel])
        keep = [n for n in tree.body
                if isinstance(n, (ast.FunctionDef, ast.ClassDef))]
        self.extracted[rel] = keep
        g = {"Fr": Fraction, "combinations": combinations, "Counter": Counter,
             "permutations": permutations, "product": product,
             "sys": sys, "ast": ast, "os": os}
        g.update(extra)
        exec(compile(ast.fix_missing_locations(
            ast.Module(body=keep, type_ignores=[])), marker, "exec"), g)
        return g


def actor(site):
    return "G%d%d" % site


ACTORS = tuple(actor(s) for s in SITES)
ACTOR_SITE = {actor(s): s for s in SITES}


ORDER_PERMS = tuple(permutations(range(3)))
DRIVEN_RECORDS = []


def drive(G, schedule, supply=True, underspecified=False, drop_supply=None,
          order=None):
    """THE GENERALIZED SCHEDULE DRIVER.  Exactly d66's CONFLICT-GRID(g, R)
    cycle -- conflict-supply deliveries from the group's seed, g proposals
    (0 for the seed, 1 for the rest), one g-proposer arbitration won by the
    seed -- with the GROUPING AND THE SEED taken from the schedule instead of
    being hard-wired to rows/columns and the diagonal.  Groups are processed in
    ascending order of their seed's site index and members in ascending site
    index, which is d66's own order at the committed schedule; `order` selects
    one of the 6 x 6 alternative processing conventions per round, and is used
    only by the declared invariance probe.  Every event is specified by its
    FULL TUPLE and taken from the layer's own menu."""
    b = G.B(ACTORS)
    DRIVEN_RECORDS.append((schedule, supply, underspecified, drop_supply,
                           order))
    cur = {a: G.V0 for a in ACTORS}
    dropped = 0
    for rnd, (groups, seeds) in enumerate(schedule):
        seq = sorted(range(len(groups)), key=lambda gi: SITE_INDEX[seeds[gi]])
        if order is not None:
            seq = [seq[i] for i in ORDER_PERMS[order[0]]]
        for gi in seq:
            mem = sorted(groups[gi])
            if order is not None:
                mem = [mem[i] for i in ORDER_PERMS[order[1]]]
            grp = [actor(s) for s in mem]
            sd = actor(seeds[gi])
            base = cur[sd]
            for a in grp:
                if a == sd or cur[a] == base:
                    continue
                if not supply:
                    continue
                if drop_supply is not None and dropped == drop_supply:
                    dropped += 1
                    continue
                dropped += 1
                b.pick((sd, a),
                       lambda e, s=sd, r=a, v=base: (e[0] == "d" and e[1] == s
                                                     and e[2] == r
                                                     and e[3] == v),
                       "supply %s->%s" % (sd, a))
                if b.refusal:
                    return b
            trips = [(a, base, 0 if a == sd else 1) for a in grp]
            for t in trips:
                b.pick((t[0],), lambda z, e=("p",) + t: z == e,
                       "propose %s" % t[0])
                if b.refusal:
                    return b
            ckey = frozenset(trips)
            wkey = frozenset({[t for t in trips if t[0] == sd][0]})
            if underspecified:
                b.pick((sd,), lambda z, s=sd: z[0] == "r" and z[1] == s,
                       "arbitrate* %s" % sd)
            else:
                b.pick((sd,), lambda z, e=("r", sd, ckey, wkey): z == e,
                       "arbitrate %s" % sd)
            if b.refusal:
                return b
            v = G.vname(base, wkey, sd)
            for a in grp:
                cur[a] = v
    return b


BUILD_CACHE = {}
ANCHOR_CACHE = {}


def driven(G, schedule):
    """cached, mutant-independent: the record is a property of the schedule."""
    if schedule not in BUILD_CACHE:
        b = drive(G, schedule)
        BUILD_CACHE[schedule] = {
            "events": len(b.H),
            "maxhits": b.maxhits,
            "refusal": b.refusal,
            "divisions": [e for e in b.H if e[0] == "r"],
            "H": list(b.H),
        }
    return BUILD_CACHE[schedule]


def branching_control(G):
    """THE UNDER-SPECIFIED CONTROL, made reproducible.  The committed record
    is replayed up to (not including) its first arbitration; d60's `pick` is
    then asked for an arbitration by that group's seed WITHOUT its conflict
    key or winner key, and the builder's own `maxhits` -- the NUMBER of menu
    candidates matching -- is read.  The run stops there: which candidate
    `sorted(key=repr)` would return is hash-seed dependent, the count is
    not."""
    rec = driven(G, COMMITTED)
    first = min(k for k, e in enumerate(rec["H"]) if e[0] == "r")
    seed = rec["H"][first][1]
    b = G.B(ACTORS)
    b.H = list(rec["H"][:first])
    b.pick((seed,), lambda z, s=seed: z[0] == "r" and z[1] == s,
           "arbitrate* %s" % seed)
    return b.maxhits, first, seed


def fields_of(G, divisions):
    """the two site readings, read off a DRIVEN record: initiators from each
    arbitration's `op[1]`, footprints from its `regs_of` footprint intersected
    with the actor set."""
    init, foot = Counter(), Counter()
    for e in divisions:
        init[ACTOR_SITE[e[1]]] += 1
        for r in G.regs_of(e):
            if r in ACTOR_SITE:
                foot[ACTOR_SITE[r]] += 1
    return (tuple(init[x] for x in SITES), tuple(foot[x] for x in SITES))


def order_probe(G, schedules):
    """THE PROCESSING-ORDER FIBER, MEASURED.  d66's order pins the committed
    POINT; extending it to the family -- ascending seed-site index, ascending
    member index -- is a declared convention with a fiber of 6 x 6 per round.
    Every one of the 36 conventions is driven at each declared schedule and
    the record's fate and both site fields are compared against the committed
    convention's."""
    rows = []
    for sched in schedules:
        ref = driven(G, sched)
        ref_fields = fields_of(G, ref["divisions"])
        for gp in range(len(ORDER_PERMS)):
            for mp in range(len(ORDER_PERMS)):
                b = drive(G, sched, order=(gp, mp))
                div = [e for e in b.H if e[0] == "r"]
                rows.append({
                    "order": "g%d/m%d" % (gp, mp),
                    "forced": b.refusal is None and b.maxhits == 1,
                    "events": len(b.H), "divisions": len(div),
                    "fields_match": fields_of(G, div) == ref_fields,
                    "events_match": len(b.H) == ref["events"]})
    return rows


def r3_saturating():
    """THE SUCCESSOR'S ENTRY DATUM, computed here and read no further.  The
    weld route needs a budget depositing at least 27 link-incidences on I7's
    link set; the minimal saturating arrangement is R = 3 with the three
    rounds grouped on the three link-direction parallel classes.  This is a
    probe OUTSIDE this unit's declared family (which is R = 2), reported as
    the successor's demand and used in no measurement above."""
    three = [CLASSES["ROW"], CLASSES["COL"], CLASSES["DIA"]]
    n = {}
    for l in I7_LINKS:
        for x in SITES:
            n[(l, x)] = sum(1 for P in three for g in P
                            if x in g and zadd(x, l) in g)
    forms = [i7_form(n, x) for x in SITES]
    q = forms[0]
    return {"rounds": len(three),
            "cells": len(n),
            "distinct_counts": sorted({v for v in n.values()}),
            "q11": str(q[0]), "q22": str(q[1]), "q12": str(q[2]),
            "det": str(q[3]),
            "homogeneous": len(set(forms)) == 1,
            "posdef_sites": sum(1 for f in forms if f[3] > 0 and f[0] > 0),
            "strictly_positive_cells": sum(1 for v in n.values() if v > 0)}


def committed_grid(G, R_):
    """d66's own `conflict_grid(3, R)`, re-run once and cached."""
    if R_ not in ANCHOR_CACHE:
        b = G.conflict_grid(3, R_)
        ANCHOR_CACHE[R_] = {"events": len(b.H),
                            "arbs": sum(1 for e in b.H if e[0] == "r"),
                            "dels": sum(1 for e in b.H if e[0] == "d"),
                            "maxhits": b.maxhits, "refusal": b.refusal,
                            "H": list(b.H)}
    return ANCHOR_CACHE[R_]


# ===========================================================================
# SECTION 4.  THE FAMILY (pin R1)
# ===========================================================================

def all_partitions():
    """every partition of the nine sites into three triples."""
    out = []

    def rec(rem, acc):
        if not rem:
            out.append(tuple(sorted(acc)))
            return
        a, rest = rem[0], rem[1:]
        for pair in combinations(rest, 2):
            rec(tuple(x for x in rest if x not in pair),
                acc + [tuple(sorted((a,) + pair))])
    rec(tuple(SITES), [])
    return sorted(out)


def transversals(P):
    return [tuple(t) for t in product(*P)]


def align_seeds(P, T):
    """the seed tuple of a partition P whose image is the seed SET T: the
    i-th entry is T's unique member of P's i-th group."""
    return tuple([x for x in g if x in T][0] for g in P)


def parallel_class(d):
    """the resolvable partition of AG(2,3) into the three lines of slope d."""
    H = SUBGROUPS["<(%d,%d)>" % d]
    seen, out = set(), []
    for x in SITES:
        L = tuple(sorted(zadd(x, h) for h in H))
        if L not in seen:
            seen.add(L)
            out.append(L)
    return tuple(sorted(out))


CLASS_NAMES = ("ROW", "COL", "DIA", "ANT")
CLASS_DIR = {"ROW": (0, 1), "COL": (1, 0), "DIA": (1, 1), "ANT": (1, 2)}
CLASSES = {k: parallel_class(CLASS_DIR[k]) for k in CLASS_NAMES}
DIAG_SEED = ((0, 0), (1, 1), (2, 2))


def schedule_of(P0, s0, P1, s1):
    return ((P0, s0), (P1, s1))


COMMITTED = schedule_of(CLASSES["ROW"], DIAG_SEED, CLASSES["COL"], DIAG_SEED)


def window_schedules():
    """THE DECLARED GRAMMAR WINDOW: both rounds' groupings drawn from the four
    parallel classes of AG(2,3) -- d66's own resolvable device -- with the
    seeds free.  Deterministic order, no sampling."""
    out = []
    for a in CLASS_NAMES:
        for s0 in transversals(CLASSES[a]):
            for b in CLASS_NAMES:
                for s1 in transversals(CLASSES[b]):
                    out.append((a, s0, b, s1))
    return out


# ===========================================================================
# SECTION 5.  THE MEASURED COLUMNS (combinatorial, exact, full family)
# ===========================================================================

def initiator_field(S0, S1):
    return {x: (1 if x in S0 else 0) + (1 if x in S1 else 0) for x in SITES}


def footprint_field(P0, P1):
    n = {x: 0 for x in SITES}
    for P in (P0, P1):
        for g in P:
            for x in g:
                n[x] += 1
    return n


def link_counts(P0, P1):
    """the co-division adjacency: for a link l and a site x, the number of
    division events whose footprint contains both x and x + l."""
    n = {}
    for l in I7_LINKS:
        for x in SITES:
            y = zadd(x, l)
            n[(l, x)] = sum(1 for P in (P0, P1)
                            for g in P if x in g and y in g)
    return n


def i7_form(n, x):
    """HA 3.2's readout, in the U4 effectus's I7 coordinates."""
    q11 = Fraction(n[((1, 0), x)])
    q22 = Fraction(n[((0, 1), x)])
    q12 = Fraction(n[((1, 1), x)] - n[((1, 0), x)] - n[((0, 1), x)], 2)
    return q11, q22, q12, q11 * q22 - q12 * q12


def affine_class(S0, S1):
    """pin R3: is the seed set a union of cosets of one subgroup?"""
    f0, f1 = frozenset(S0), frozenset(S1)
    if f0 in AG_LINES and f1 in AG_LINES:
        return ("CU-JOINT" if LINE_DIRECTION[f0] == LINE_DIRECTION[f1]
                else "CU-SPLIT")
    return "BEYOND-COSET"


RAW = {}


def raw_census(G):
    """every measured column, computed once, mutant-independent."""
    if RAW:
        return RAW
    parts = all_partitions()
    pidx = {P: k for k, P in enumerate(parts)}
    subsets = sorted((frozenset(c) for c in combinations(SITES, 3)),
                     key=lambda T: sorted(T))
    sidx = {T: k for k, T in enumerate(subsets)}

    # -- the weight of a seed set: how many partitions admit it -------------
    weight = Counter()
    tr_index = []
    for P in parts:
        ts = set()
        for T in transversals(P):
            weight[frozenset(T)] += 1
            ts.add(sidx[frozenset(T)])
        tr_index.append(ts)

    # -- the stabilizer over seed-set pairs, three routes -------------------
    stabpair, affpair, route_rows = {}, {}, []
    for T0 in subsets:
        for T1 in subsets:
            n = initiator_field(T0, T1)
            r1, r2, r3 = stab_direct(n), stab_fourier(n), stab_lattice(n)
            stabpair[(sidx[T0], sidx[T1])] = SUBGROUP_NAME[r1]
            affpair[(sidx[T0], sidx[T1])] = affine_class(T0, T1)
            route_rows.append((sidx[T0], sidx[T1],
                               SUBGROUP_NAME[r1], SUBGROUP_NAME[r2],
                               SUBGROUP_NAME[r3]))

    # -- the link fields and the determinant column -------------------------
    fields = [tuple(1 if any(x in g and zadd(x, l) in g for g in P) else 0
                    for l in I7_LINKS for x in SITES) for P in parts]
    det_class, det9, posdef_max, strict_pos = {}, [], 0, 0
    detvals = Counter()
    pd_hist = Counter()
    posdef_cells = det_all_positive = posdef_under_three = 0
    min_inc_at_posdef = 27
    for i0 in range(len(parts)):
        f0 = fields[i0]
        for i1 in range(len(parts)):
            f1 = fields[i1]
            nz = pd = allpos = 0
            rows = []
            for k, x in enumerate(SITES):
                a = f0[k] + f1[k]
                b = f0[9 + k] + f1[9 + k]
                c = f0[18 + k] + f1[18 + k]
                q12 = Fraction(c - a - b, 2)
                d = Fraction(a) * Fraction(b) - q12 * q12
                rows.append((a, b, c, q12, d))
                if d != 0:
                    nz += 1
                if d > 0:
                    allpos += 1
                if d > 0 and a > 0:
                    pd += 1
                    if a + b + c < min_inc_at_posdef:
                        min_inc_at_posdef = a + b + c
                    if a + b + c < 3:
                        posdef_under_three += 1
            hom = len(set(rows)) == 1
            det_class[(i0, i1)] = (nz, pd, hom)
            posdef_max = max(posdef_max, pd)
            pd_hist[pd] += 1
            posdef_cells += pd
            if allpos == 9:
                det_all_positive += 1
            if all(f0[k] + f1[k] > 0 for k in range(27)):
                strict_pos += 1
            if nz == 9:
                det9.append((i0, i1, hom, tuple(r[4] for r in rows)))
                for r in rows:
                    detvals[str(r[4])] += 1

    # -- THE CARRIER OF THE PERIOD (the adjudication's re-seating of the null)
    # For every crystalline seed pair: is the support of the division field a
    # UNION OF COSETS of the field's own period subgroup?  If it is, the pair
    # obeys the affine law n = c + m*1_S on that union, and the null was
    # stated on the wrong variable rather than defeated.
    carrier_rows, carrier_bad, line_seed, shape = [], [], [], Counter()
    for key in sorted(stabpair):
        if stabpair[key] == "1":
            continue
        T0, T1 = subsets[key[0]], subsets[key[1]]
        n = initiator_field(T0, T1)
        H = SUBGROUPS[stabpair[key]]
        supp = {x for x in SITES if n[x] > 0}
        cosets = {frozenset(zadd(x, h) for h in H) for x in SITES}
        is_union = all(c <= supp or not (c & supp) for c in cosets)
        vals = tuple(sorted(Counter(n[x] for x in SITES).items()))
        shape[str(vals)] += 1
        if not is_union:
            carrier_bad.append(key)
        if affpair[key] == "BEYOND-COSET" and (T0 in AG_LINES
                                               or T1 in AG_LINES):
            line_seed.append(key)
        carrier_rows.append((key, stabpair[key], affpair[key], is_union,
                             T0 == T1))
    same_seed = sum(1 for r in carrier_rows if r[4])

    # -- FRAGILITY AT FAMILY SCOPE: every single-point re-seating of either
    # -- seed of every crystalline pair, a strict superset of the admissible
    # -- window edits.  Measured: does ANY nontrivial period survive?
    frag_cases = frag_kept = frag_nontrivial = 0
    for key, sname, _a, _u, _s in carrier_rows:
        H = SUBGROUPS[sname]
        base = [set(subsets[key[0]]), set(subsets[key[1]])]
        for which in (0, 1):
            for old in sorted(base[which]):
                for new in SITES:
                    if new in base[which]:
                        continue
                    edited = list(base)
                    edited[which] = (base[which] - {old}) | {new}
                    st = stab_direct(initiator_field(edited[0], edited[1]))
                    frag_cases += 1
                    if st >= H:
                        frag_kept += 1
                    if len(st) > 1:
                        frag_nontrivial += 1

    # -- THE PERIOD AND THE DIAGONAL LINK COUNT, JOINTLY.  The marginal is
    # -- uniform; the joint is not, and the departure is exactly at the
    # -- diagonal.  A partition deposits diagonal incidences iff its groups
    # -- contain a <(1,1)>-difference pair, so a pair of partitions leaves the
    # -- diagonal link EMPTY iff both do.
    zero_diag = [sum(f[18:27]) == 0 for f in fields]
    zcount = Counter()
    for k in range(len(parts)):
        if zero_diag[k]:
            for t in tr_index[k]:
                zcount[t] += 1
    per_period, per_populated = Counter(), Counter()
    for key, sname, _a, _u, _s in carrier_rows:
        per_period[sname] += 90 * 90
        per_populated[sname] += 90 * 90 - zcount[key[0]] * zcount[key[1]]

    # -- THE POSITIVE-DEFINITE CEILING AND THE INCIDENCE WALL ---------------
    per_partition_incidence = [sum(f) for f in fields]
    max_part_inc = max(per_partition_incidence)
    parts_at_max = sum(1 for v in per_partition_incidence if v == max_part_inc)

    # -- the joint stratum, and one DRIVEN witness per nonempty stratum -----
    joint = Counter((affpair[k], stabpair[k]) for k in affpair)
    joint_det = Counter()
    wit9 = {}
    for (i0, i1, _h, _d) in det9:
        for t0 in sorted(tr_index[i0]):
            for t1 in sorted(tr_index[i1]):
                key = (stabpair[(t0, t1)], affpair[(t0, t1)])
                joint_det[key] += 1
                if key not in wit9:
                    wit9[key] = (i0, i1, t0, t1)
    parts_with = {}
    for k, P in enumerate(parts):
        for t in sorted(tr_index[k]):
            parts_with.setdefault(t, []).append(k)
    rep = {}
    for (t0, t1), s in sorted(stabpair.items()):
        key = (s, affpair[(t0, t1)])
        rep.setdefault(key, (t0, t1))
    want, witness = [], {}
    for (a, s), v in sorted(joint.items()):
        key = (s, a)
        total = v * 90 * 90
        d9 = joint_det.get(key, 0)
        if d9:
            want.append(key + (True,))
            witness[key + (True,)] = wit9[key]
        if total - d9 > 0:
            want.append(key + (False,))
            t0, t1 = rep[key]
            found = None
            for i0 in parts_with[t0]:
                for i1 in parts_with[t1]:
                    if det_class[(i0, i1)][0] != 9:
                        found = (i0, i1, t0, t1)
                        break
                if found:
                    break
            witness[key + (False,)] = found

    RAW.update({
        "parts": parts, "pidx": pidx, "subsets": subsets, "sidx": sidx,
        "weight": weight, "tr_index": tr_index, "stabpair": stabpair,
        "affpair": affpair, "route_rows": route_rows, "fields": fields,
        "det_class": det_class, "det9": det9, "posdef_max": posdef_max,
        "strict_pos": strict_pos, "detvals": detvals, "joint": joint,
        "joint_det": joint_det, "want": want, "witness": witness,
        "carrier_rows": carrier_rows, "carrier_bad": carrier_bad,
        "line_seed": line_seed, "shape": shape, "same_seed": same_seed,
        "frag_cases": frag_cases, "frag_kept": frag_kept,
        "frag_nontrivial": frag_nontrivial,
        "per_period": per_period, "per_populated": per_populated,
        "pd_hist": pd_hist, "posdef_cells": posdef_cells,
        "det_all_positive": det_all_positive,
        "min_inc_at_posdef": min_inc_at_posdef,
        "posdef_under_three": posdef_under_three,
        "max_part_inc": max_part_inc, "parts_at_max": parts_at_max,
    })
    return RAW


WINDOW_DRIVE = {}


def window_drive(G):
    """drive the layer's own menus over every schedule of the declared
    window.  Cached: the record is a function of the schedule alone."""
    if WINDOW_DRIVE:
        return WINDOW_DRIVE
    for (a, s0, b, s1) in window_schedules():
        sched = schedule_of(CLASSES[a], s0, CLASSES[b], s1)
        rec = driven(G, sched)
        init, foot = fields_of(G, rec["divisions"])
        WINDOW_DRIVE[(a, s0, b, s1)] = {
            "events": rec["events"], "maxhits": rec["maxhits"],
            "refusal": rec["refusal"],
            "divisions": len(rec["divisions"]),
            "init": init, "foot": foot,
        }
    return WINDOW_DRIVE


# ===========================================================================
# SECTION 6.  THE RUN
# ===========================================================================

NUMREG = set()


def reg(*vals):
    for v in vals:
        if isinstance(v, Fraction):
            NUMREG.add(str(v))
            NUMREG.add(str(abs(v)))
            NUMREG.add(str(v.numerator))
            NUMREG.add(str(abs(v.numerator)))
            NUMREG.add(str(v.denominator))
        elif isinstance(v, int):
            NUMREG.add(str(v))
        elif isinstance(v, str):
            NUMREG.add(v)
    return vals[0] if vals else None


VERBATIM = [
    ("V01", "A-PIN",
     "all grammar-admissible choices of which cell-pairs\narbitrate per "
     "round, at the committed budget", "G-FAMILY-COUNT"),
    ("V02", "A-PIN",
     "any schedule with det != 0 at all sites is\n   the corpus's first "
     "non-degenerate grammar-generated geometry\n   carrier",
     "G-DET-NONZERO-EXISTS"),
    ("V03", "A-ADJ",
     "at all ten cells the division field is affine in the\nconstructor's "
     "seed set -- n = c + m*1_S -- so Stab(n) = Stab(1_S)",
     "G-AFFINE-LAW"),
    ("V04", "A-EFF",
     "q11 = n_{e1}`, `q22 = n_{e2}`, `q12 = (n_{e1+e2} - n_{e1} - "
     "n_{e2})/2", "G-I7-READOUT"),
    ("V05", "A-HA",
     "The readout is an invertible linear re-encoding: in count "
     "coordinates, the\n> record IS the metric.", "G-I7-READOUT"),
    ("V06", "A-D66",
     "each group is a g-PROPOSER conflict (g + 1 registers) whose base is\n"
     "    supplied by g - 1 deliveries from the group's diagonal seed",
     "G-COMMITTED-RECORD"),
    ("V07", "A-L1",
     "fourth form, outside paper 8's three**, and its admissibility is\n"
     "   v11's to argue when U4 runs", "G-WALL-L1"),
    ("V08", "A-CAT",
     "a Poisson sprinkling admits **no\nLorentz-invariant finite-valency "
     "graph** (BHS)", "G-WALL-BHS"),
    ("V09", "A-CAT",
     "a dimension reading without a height control is worthless",
     "G-WALL-KR"),
    ("V10", "A-PIN",
     "the diagonal counterpoint may be MEASURED here -- that is this "
     "unit's point --\nbut cosmological readings stay barred",
     "G-WALL-DIAGONAL"),
]
# the #62 length floor: no needle shorter than this may anchor a gate
NEEDLE_FLOOR = 40


def ascii_fold(s):
    """the pinned sources are typeset with Unicode punctuation and
    subscripts; the needles are ASCII.  This fold is declared, applied to
    BOTH sides of every verbatim match, and it changes no word."""
    table = {
        "—": "--", "–": "-", "−": "-", "‘": "'",
        "’": "'", "“": '"', "”": '"', "…": "...",
        "×": "x", "≈": "~", "≠": "!=", "≤": "<=",
        "≥": ">=", "⟨": "<", "⟩": ">", "→": "->",
        "≡": "==", "·": "*", "ℓ": "l", "ω": "w",
        "ℤ": "Z", "√": "sqrt",
        "₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4",
        "₅": "5", "₆": "6", "₇": "7", "₈": "8", "₉": "9",
        "⁰": "0", "¹": "1", "²": "2", "³": "3",
    }
    for k, v in table.items():
        s = s.replace(k, v)
    return re.sub(r"[^\x00-\x7f]", "?", s)


def match_needle(hay, needle):
    """#125: whitespace-normalise both sides; #62: enforce the length floor."""
    if len(norm(needle)) < NEEDLE_FLOOR:
        raise GateFail("G-VERBATIM :: needle below the #62 length floor")
    return norm(ascii_fold(needle)) in norm(ascii_fold(hay))


def full_run(break_anchor, paper_text, paper_rel):
    LD = Ledger()
    SEAL = Seal()
    R = {"schema": SCHEMA, "paper": paper_rel}
    NUMREG.clear()
    del READS[:]

    # -- SEC 1  PROVENANCE ---------------------------------------------------
    say("=" * 78)
    say("SEC 1   PROVENANCE -- ten pinned sources, sha256-12, products gated")
    say("=" * 78)
    texts, prov = {}, []
    for sid, rel, want, what in SOURCES:
        raw = read_bytes(rel)
        got = hashlib.sha256(raw).hexdigest()[:12]
        want_eff = "0" * 12 if break_anchor == sid else want
        texts[rel] = raw.decode("utf-8")
        ok = (got == want_eff)
        prov.append({"id": sid, "path": rel, "want": want_eff, "got": got,
                     "ok": ok, "what": what})
        LD.gate("G-PROV[%s]" % sid,
                "the pinned source %s is present and its sha256-12 is %s "
                "(measured %s) -- %s" % (rel, want_eff, got, what),
                ok, {"path": rel, "want": want_eff, "got": got})
    R["provenance"] = prov
    if mut("MUT-SCHEMA-FORGED"):
        # INJ02's move on the two rows a seal cannot cover, object-level
        R["schema"] = "INJECTED-SCHEMA"
        R["paper"] = "v14/NOT-THE-PAPER.md"
    schema_ok = R["schema"] == SCHEMA
    paper_ok = R["paper"] == paper_rel
    LD.gate("G-DECLARED-UNSEALED",
            "THE TWO DECLARED-UNSEALED RECEIPT KEYS ARE BOUND.  A published "
            "row that is not digested at a gate must say so and must be "
            "bound some other way: `schema` is a constant of this file, "
            "re-verified here against its own definition, and `paper` is the "
            "relative path of the object under test, re-verified here against "
            "the path this run actually read.  Both are fixed before the "
            "first gate; the declared-unsealed manifest carries both, with "
            "their reasons, into the receipt",
            schema_ok and paper_ok,
            {"schema": R["schema"], "paper": R["paper"],
             "schema_matches_declaration": schema_ok,
             "paper_matches_object_under_test": paper_ok,
             "declared_unsealed": len(UNSEALED_DECLARED)})
    LD.gate("G-PROV-ALL",
            "ALL %d declared sources resolve under the repository root "
            "derived from this file's own location, every one reproduces its "
            "pinned sha256-12, and the set of hash-pinned runtime reads is "
            "EXACTLY the declared set -- nothing else in the repository is "
            "read except this file itself (for the exactness AST scan) and "
            "the paper under test (which cannot be hash-pinned because it is "
            "the object being verified).  No `git` subprocess is invoked "
            "anywhere in this program, so the run is correct off-tree and in "
            "a directory with no version control (#91)" % len(SOURCES),
            all(p["ok"] for p in R["provenance"])
            and set(READS) == {s[1] for s in SOURCES},
            {"sources": len(SOURCES), "reads": sorted(set(READS)),
             "unpinned_reads": ["<self>", paper_rel], "subprocesses": 0})
    SEAL.take("SEAL-PROVENANCE", R)
    if mut("MUT-VOUCH-FORGED"):
        # INJ02, as the instrument review ran it: the four VOUCHING rows
        # forged after their gates.  Before this repair they were sealed
        # nowhere and the receipt published the forgery at exit 0.
        R["provenance"] = [dict(p, ok=False, got="deadbeefcafe")
                           for p in R["provenance"]]

    # -- SEC 2  THE GRAMMAR --------------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 2   THE COMMITTED GRAMMAR, DRIVEN DIRECTLY (no menu law re-typed)")
    say("=" * 78)
    G = Grammar(texts)
    say("  d42b1 text-slice: %d of %d chars, cut at the layer's own banner "
        "print" % G.slice_chars)
    say("  AST-extracted bodies: %s"
        % {k.split("/")[-1]: len(v) for k, v in sorted(G.extracted.items())})
    LD.gate("G-SLICE-EXIT-FREE",
            "the committed transport grammar enters this process as a SINGLE "
            "SOURCE -- a text slice of d42b1 cut at its own banner print, "
            "plus AST-extracted def/class bodies of d60 and d66 -- and the "
            "strip is GATED, not asserted: no reference to `exit`, `quit` or "
            "`_exit`, in CALL or bare NAME/ATTRIBUTE form, survives the slice "
            "(checked textually AND by AST) or any extracted body",
            G.slice_exit_free and G.bodies_exit_free,
            {"slice_chars": G.slice_chars, "slice_exit_free": G.slice_exit_free,
             "bodies_exit_free": G.bodies_exit_free,
             "bodies": {k.split("/")[-1]: len(v)
                        for k, v in sorted(G.extracted.items())}})

    # the menu is the layer's own: a behavioural probe, both directions
    menu0 = G.candidates_for([], (ACTORS[0],))
    probe_ok = (any(e[0] == "p" and e == ("p", ACTORS[0], G.V0, 0)
                    for e, _q in menu0)
                and not any(e[0] == "r" for e, _q in menu0)
                and not any(e[0] == "d" and e[3] != G.V0 for e, _q in menu0))
    LD.gate("G-GRAMMAR-LIVE",
            "the object deciding admissibility here is d42b1's own "
            "`candidates_for`, exercised in BOTH directions on the empty "
            "record: the genesis proposal ('p', G00, v0, 0) IS offered, no "
            "arbitration is offered (nothing is live) and no delivery of a "
            "non-genesis version is offered (nothing is held)",
            probe_ok, {"menu_size": len(menu0),
                       "kinds": sorted({e[0] for e, _q in menu0})})

    # the anchor: the generalized driver reproduces the committed constructor
    committed_ref = committed_grid(G, 2)
    mine = driven(G, COMMITTED)
    same = pick("MUT-COMMITTED-RECORD",
                committed_ref["H"] == mine["H"], False)
    LD.gate("G-COMMITTED-RECORD",
            "THE GENERALIZED SCHEDULE DRIVER REPRODUCES THE COMMITTED "
            "CONSTRUCTOR EVENT FOR EVENT.  d66's own `conflict_grid(3, 2)` "
            "function object, AST-extracted from the pinned source and re-run "
            "in this process, and this unit's schedule driver at the "
            "committed schedule (ROW class then COL class, diagonal seeds) "
            "emit IDENTICAL event lists of %d events with %d division events; "
            "so the family below is a generalization of the committed object "
            "and not a re-implementation of it"
            % (committed_ref["events"], committed_ref["arbs"]),
            same and not committed_ref["refusal"]
            and committed_ref["maxhits"] == 1,
            {"d66_events": committed_ref["events"],
             "driver_events": mine["events"],
             "identical": same, "maxhits": committed_ref["maxhits"],
             "refusal": committed_ref["refusal"]})
    reg(committed_ref["events"], committed_ref["arbs"])

    # the committed .out rows, READ and reproduced (not re-typed)
    d66out = texts["v10/data/d66_arbitration_crystal_exact.out"]
    anchors = []
    for R_ in (4, 6):
        m = re.search(r"GRID\(g=3,R=%d\)\s+n=\s*(\d+)\s+arbs=\s*(\d+)\s+"
                      r"\(k_min=(\d+), k_conflict=(\d+)\)\s+deliveries=\s*"
                      r"(\d+)\s+arb share (\d+)/(\d+)" % R_, d66out)
        b = committed_grid(G, R_)
        got = (b["events"], b["arbs"], b["dels"])
        wnt = (int(m.group(1)), int(m.group(2)), int(m.group(5)))
        anchors.append({"id": "A-D66-GRID3%d" % R_, "read": wnt,
                        "recomputed": got, "ok": got == wnt,
                        "source": "v10/data/d66_arbitration_crystal_exact.out"})
    eff = texts["v14/review-u4-effectus.md"]
    m = re.search(r"\|\s*CONFLICT-GRID\(3,2\)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|"
                  r"\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*−?-?(\d+)"
                  r"\s*\|\s*\*\*(\d+)\*\*", eff)
    eff_row = tuple(int(m.group(k)) for k in range(1, 8))
    nn = link_counts(CLASSES["ROW"], CLASSES["COL"])
    q11, q22, q12, det = i7_form(nn, (0, 0))

    def i7_row(x):
        a11, a22, a12, dd = i7_form(nn, x)
        return (nn[((1, 0), x)], nn[((0, 1), x)], nn[((1, 1), x)],
                int(a11), int(a22), abs(int(a12)), int(dd))
    site_rows = [i7_row(x) for x in SITES]
    if mut("MUT-I7-READOUT"):
        # the corruption sits at ONE site away from the read anchor's own,
        # which is exactly what the single-row anchor cannot see
        site_rows = list(site_rows)
        site_rows[4] = tuple(v + 1 for v in site_rows[4])
    got_row = site_rows[0]
    anchors.append({"id": "A-EFF-I7", "read": list(eff_row),
                    "recomputed": list(got_row), "ok": got_row == eff_row,
                    "schema": "(n_(1,0), n_(0,1), n_(1,1), q_11, q_22, "
                              "|q_12|, det) -- the sixth entry is the "
                              "ABSOLUTE VALUE; the source row prints -1",
                    "source": "v14/review-u4-effectus.md"})
    if mut("MUT-ANCHOR-DRIFT"):
        anchors[0] = dict(anchors[0])
        anchors[0]["recomputed"] = [x + 1 for x in anchors[0]["recomputed"]]
        anchors[0]["ok"] = False
    R["anchors"] = anchors
    for a in anchors:
        reg(*[int(x) for x in a["read"]])
    for a in anchors:
        say("  [ANCH] %s  read %s  recomputed %s" % (a["id"], a["read"],
                                                     a["recomputed"]))
    LD.gate("G-ANCHORS-READ",
            "the committed numbers this unit reproduces are READ from their "
            "committed files at run time and never re-typed: d66's own output "
            "rows for GRID(g=3,R=4) and GRID(g=3,R=6) (events, arbitrations, "
            "deliveries) are parsed out of `d66_arbitration_crystal_exact.out` "
            "and reproduced by the extracted constructor, and the U4 effectus "
            "review's CONFLICT-GRID(3,2) I7 row (n_(1,0), n_(0,1), n_(1,1), "
            "q_11, q_22, |q_12|, det) is parsed out of the review and "
            "reproduced by this unit's own readout -- %d of %d"
            % (sum(1 for a in anchors if a["ok"]), len(anchors)),
            all(a["ok"] for a in anchors), {"anchors": anchors})
    SEAL.take("SEAL-ANCHORS", R)

    va = []
    for vid, sid, quote, consumer in VERBATIM:
        rel = [s[1] for s in SOURCES if s[0] == sid][0]
        found = match_needle(texts[rel], quote)
        if mut("MUT-VERBATIM") and vid == "V03":
            found = False
        va.append({"id": vid, "source": sid, "path": rel,
                   "chars": len(norm(quote)), "found": found,
                   "consumer": consumer})
        say("  [VERB] %s  %s -> %s  (%d chars)"
            % (vid, rel, consumer, len(norm(quote))))
    R["verbatim_anchors"] = va
    LD.gate("G-VERBATIM",
            "every one of the %d verbatim source anchors (#62) is found in "
            "its pinned source after ASCII folding and whitespace "
            "normalisation, every needle clears the %d-character length "
            "floor, and every anchor names the gate that CONSUMES it -- no "
            "anchor is decorative"
            % (len(va), NEEDLE_FLOOR),
            all(a["found"] for a in va)
            and all(a["chars"] >= NEEDLE_FLOOR for a in va)
            and all(a["consumer"] for a in va),
            {"anchors": len(va), "min_chars": min(a["chars"] for a in va),
             "missing": [a["id"] for a in va if not a["found"]]})
    SEAL.take("SEAL-VERBATIM", R)

    LD.gate("G-I7-READOUT",
            "THE READOUT REPRODUCES THE COMMITTED ROW AT ALL NINE SITES, not "
            "at the one the anchor prints.  The determinant column is "
            "computed through HA 3.2's DECLARED readout in the U4 effectus "
            "review's own I7 coordinates -- q_11 = n_(1,0), q_22 = n_(0,1), "
            "q_12 = (n_(1,1) - n_(1,0) - n_(0,1))/2 -- applied to THE "
            "CO-DIVISION ADJACENCY: for a link l and a site x, the number of "
            "division events whose footprint contains both x and x + l, on "
            "the link set {(1,0), (0,1), (1,1)}.  Both source statements are "
            "verbatim anchors V04 and V05.  The committed schedule's induced "
            "form is the same at every one of the nine sites and equals the "
            "row the effectus review published, whose sixth entry is |q_12| "
            "and not q_12 -- the ASCII fold the read anchor applies does not "
            "carry the sign, so the anchor validates the route up to that "
            "sign and this gate says so",
            all(r == eff_row for r in site_rows),
            {"committed_row": list(eff_row), "sites": len(site_rows),
             "distinct_rows": len({r for r in site_rows}),
             "recomputed": [list(r) for r in site_rows[:1]],
             "links": [list(l) for l in I7_LINKS]})

    # -- SEC 3  THE FAMILY ---------------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 3   THE FAMILY (pin R1), declared as data and COUNTED")
    say("=" * 78)
    C = raw_census(G)
    parts, subsets = C["parts"], C["subsets"]
    n_parts = len(parts)
    n_seed = 27
    per_round = n_parts * n_seed
    family = per_round * per_round
    # route 2 for the same count: the multinomial 9!/(3!^3 3!) and 3^3
    f9 = 1
    for k in range(1, 10):
        f9 *= k
    n_parts_closed = f9 // (6 * 6 * 6 * 6)
    family_closed = (n_parts_closed * 27) ** 2
    if mut("MUT-FAMILY-COUNT"):
        family = family + 1
    say("  partitions of the nine sites into three triples : %d" % n_parts)
    say("  seed assignments per partition                   : %d" % n_seed)
    say("  schedules per round                              : %d" % per_round)
    say("  THE FAMILY (two rounds)                          : %d" % family)
    LD.gate("G-FAMILY-COUNT",
            "THE FAMILY IS COUNTED, NOT ASSERTED (#24).  A schedule is a "
            "choice, for each of the committed constructor's two rounds, of "
            "which cell-pairs arbitrate together -- equivalently a partition "
            "of the nine cells into three three-proposer conflict groups, the "
            "committed per-round budget -- together with a seed for each "
            "group.  Enumeration gives %d partitions and 27 seed assignments "
            "each, so %d schedules per round and %d in the family; the closed "
            "form 9!/(3!^3 3!) x 3^3, squared, computed by a second route "
            "that shares no code with the enumeration, returns the same "
            "number" % (n_parts, per_round, family),
            n_parts == n_parts_closed and family == family_closed,
            {"partitions": n_parts, "closed_form": n_parts_closed,
             "family": family, "family_closed": family_closed})
    reg(n_parts, n_seed, per_round, family)

    win = window_schedules()
    n_win = len(win)
    win_declared = 4 * 4 * 27 * 27
    committed_in_window = ("ROW", DIAG_SEED, "COL", DIAG_SEED) in set(win)
    window_is_strict = pick("MUT-WINDOW-SILENT", n_win < family, False)
    R["family"] = {"partitions": n_parts, "seeds_per_partition": n_seed,
                   "schedules_per_round": per_round, "family": family,
                   "window": n_win, "window_fraction": str(Fraction(n_win,
                                                                    family)),
                   "window_rule": "both rounds' groupings drawn from the four "
                                  "parallel classes of AG(2,3); seeds free",
                   "committed_in_window": committed_in_window}
    say("  THE DECLARED GRAMMAR WINDOW                      : %d (%s of the "
        "family)" % (n_win, Fraction(n_win, family)))
    LD.gate("G-WINDOW-DISCLOSED",
            "THE WINDOW IS DECLARED IN THE HEAD AND IS A STRICT SUBSET "
            "(no-silent-caps).  Driving the layer's menus over all %d "
            "schedules is not affordable, so grammar-admissibility is decided "
            "EXHAUSTIVELY on a declared window -- both rounds' groupings drawn "
            "from the four parallel classes of AG(2,3), which is d66's own "
            "resolvable device, with the seeds free: %d schedules, %s of the "
            "family, containing the committed schedule.  Every OTHER column "
            "below is exhaustive over the WHOLE family, and the window's "
            "scope is carried in the constructibility verdict string itself"
            % (family, n_win, Fraction(n_win, family)),
            window_is_strict and n_win == win_declared
            and committed_in_window,
            {"family": family, "window": n_win, "declared": win_declared,
             "strict_subset": window_is_strict,
             "committed_in_window": committed_in_window})
    SEAL.take("SEAL-FAMILY", R)
    reg(n_win, Fraction(n_win, family))

    # -- SEC 4  CONSTRUCTIBILITY --------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 4   CONSTRUCTIBILITY (pin R2.1) -- the menus driven, per schedule")
    say("=" * 78)
    WD = window_drive(G)
    fates = {}
    for key, row in WD.items():
        if row["refusal"] is not None:
            fates[key] = "REFUSED"
        elif row["maxhits"] > 1:
            fates[key] = "BRANCHING"
        else:
            fates[key] = "FORCED"
    if mut("MUT-NOT-FORCED"):
        victim = ("ROW", DIAG_SEED, "COL", DIAG_SEED)
        b = drive(G, COMMITTED, drop_supply=0)
        WD = dict(WD)
        WD[victim] = dict(WD[victim])
        WD[victim]["refusal"] = b.refusal
        WD[victim]["events"] = len(b.H)
    census = Counter(fates.values())
    ev = Counter(row["events"] for row in WD.values())
    say("  window schedules driven : %d" % len(WD))
    say("  fates                   : %s" % dict(sorted(census.items())))
    say("  event counts            : %s" % dict(sorted(ev.items())))
    per_object_ok = all(
        (WD[k]["refusal"] is None and WD[k]["maxhits"] == 1
         and WD[k]["divisions"] == 6 and 24 <= WD[k]["events"] <= 30)
        for k in WD)
    refused_here = [k for k in WD if WD[k]["refusal"] is not None]
    # THE PUBLISHED ROW IS BUILT FIRST AND THE GATE READS IT (#87 at
    # emission): a row assembled after its gate is a row no gate ever saw.
    R["constructibility"] = {
        "window": len(WD), "fates": dict(sorted(census.items())),
        "events": {str(k): v for k, v in sorted(ev.items())},
    }
    LD.gate("G-CONSTRUCTIBILITY",
            "EVERY schedule of the declared window is evaluated against its "
            "OWN driven record (#87), not against an aggregate: for each of "
            "the %d schedules the layer's menu offered every specified full "
            "event tuple exactly once (maxhits = 1), no step was refused, the "
            "record carries exactly 6 division events and between 24 and 30 "
            "events in total.  Measured fates: %s -- and the published row is "
            "built before this gate, which reads it.  What the FORCED count "
            "is a measurement OF is exact: REFUSED is genuinely at risk, and "
            "the no-supply control below reaches it; BRANCHING is a "
            "STRUCTURAL ZERO for any schedule of this family, because every "
            "event is specified by its full tuple and at most one menu "
            "candidate can ever match, so the second control establishes "
            "instrument sensitivity rather than family-level reachability"
            % (len(WD), dict(sorted(census.items()))),
            per_object_ok and not refused_here
            and R["constructibility"]["fates"].get("FORCED") == len(WD),
            {"schedules": len(WD), "fates": dict(sorted(census.items())),
             "events": dict(sorted(ev.items())),
             "branching_is_structural": True,
             "refused": [str(k) for k in refused_here[:3]]})
    SEAL.take("SEAL-CONSTR-FATES", R)

    ctrl_ns = drive(G, COMMITTED, supply=False)
    R["constructibility"]["control_nosupply"] = {
        "refusal": list(ctrl_ns.refusal) if ctrl_ns.refusal else None,
        "events": len(ctrl_ns.H)}
    ns_ok = pick("MUT-REFUSAL-BLIND",
                 R["constructibility"]["control_nosupply"]["refusal"]
                 is not None, False)
    say("  CONTROL 1 (no-supply)   : refusal %s after %d events"
        % (ctrl_ns.refusal, len(ctrl_ns.H)))
    LD.gate("G-CTRL-REFUSED",
            "THE REFUSED FATE IS REACHABLE AND THE INSTRUMENT SEES IT.  The "
            "declared no-supply control runs the committed schedule with the "
            "conflict-supply deliveries suppressed; the layer then refuses the "
            "first round-1 proposal by an actor that does not hold the base, "
            "at the located prefix %s.  A refusal is recorded, never patched.  "
            "This gate reads the published control row, which is sealed here "
            "at its own gate rather than folded into a composite"
            % (ctrl_ns.refusal,),
            ns_ok, {"row": R["constructibility"]["control_nosupply"]})
    SEAL.take("SEAL-CTRL-REFUSED", R)

    us_hits, us_prefix, us_seed = branching_control(G)
    if mut("MUT-BRANCHING-BLIND"):
        us_hits = 1            # the MEASURED count, not the gate's verdict
    R["constructibility"]["control_underspecified"] = {
        "candidates": us_hits, "prefix": us_prefix, "initiator": us_seed}
    us_ok = R["constructibility"]["control_underspecified"]["candidates"] > 1
    say("  CONTROL 2 (under-spec)  : %d menu candidates match at prefix %d, "
        "so maxhits = %d" % (us_hits, us_prefix, us_hits))
    LD.gate("G-CTRL-BRANCHING",
            "THE BRANCHING FATE IS REACHABLE AND THE INSTRUMENT SEES IT.  At "
            "prefix %d of the committed record the declared under-specified "
            "control asks d60's `pick` for an arbitration by %s WITHOUT "
            "naming its conflict key and winner key; %d menu candidates "
            "match, so the builder's own `maxhits` reads %d > 1 and the fate "
            "is BRANCHING.  THIS GATE READS THE PUBLISHED ROW, and the row is "
            "sealed here at its own gate: a control row moved under its label "
            "after the fact is what this repair closes.  ONLY THE COUNT IS "
            "REPORTED, and that is deliberate: d60's `pick` breaks ties with "
            "`sorted(key=repr)`, whose value on a frozenset depends on the "
            "interpreter's per-process string hashing, so WHICH candidate an "
            "under-specified pick selects is not reproducible.  Every event "
            "of every schedule in this census is specified by its FULL TUPLE, "
            "where at most one candidate can match and the tie-break is never "
            "consulted; the control stops at the first under-specified pick "
            "and never continues a record past it"
            % (us_prefix, us_seed, us_hits, us_hits),
            us_ok, {"row": R["constructibility"]["control_underspecified"]})
    SEAL.take("SEAL-CTRL-BRANCHING", R)
    if mut("MUT-CTRL-ROW"):
        # INJ04, as the instrument review ran it: the control row replaced
        # after its gate passed.  It is now sealed at that gate.
        R["constructibility"]["control_underspecified"] = {
            "candidates": 1, "prefix": 0, "initiator": "G22"}
    SEAL.take("SEAL-CONSTRUCTIBILITY", R)
    reg(len(WD), census["FORCED"], us_hits, us_prefix, len(ctrl_ns.H))
    reg(*[k for k in ev], *[v for v in ev.values()])

    # -- SEC 5  THE STABILIZER ----------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 5   THE STABILIZER COLUMN (pin R2.2) -- both readings, 3 routes")
    say("=" * 78)
    route_rows = C["route_rows"]
    if mut("MUT-STAB-ROUTE"):
        # object-level: corrupt the Fourier route's ANSWER on one field, on a
        # copy, and let the agreement test find it
        route_rows = [(r[0], r[1], r[2], "Z3^2", r[4]) if i == 0 else r
                      for i, r in enumerate(route_rows)]
    disagree = [r for r in route_rows if not (r[2] == r[3] == r[4])]
    LD.gate("G-STAB-ROUTES",
            "THE STABILIZER OF EVERY SEED-PAIR FIELD IS COMPUTED THREE TIMES "
            "BY ROUTES SHARING NO CODE AND NO TYPED CONSTANT, and the three "
            "agree element for element at every one of the %d objects: "
            "(1) translate the field over Z_3^2 and compare; (2) take the "
            "annihilator of the support of the exact Z_3^2 Fourier transform "
            "in Z[w] = Z[t]/(t^2 + t + 1), running over the dual group; "
            "(3) walk the subgroup lattice and take the largest H on whose "
            "cosets the field is constant" % len(route_rows),
            not disagree,
            {"objects": len(route_rows), "disagreements": len(disagree),
             "first": str(disagree[0]) if disagree else None})

    # driven records vs the combinatorial field, per window schedule
    drv = dict(WD)
    if mut("MUT-DRIVEN-FIELD"):
        # object-level: detach ONE window record's own initiator field
        drv[win[0]] = dict(drv[win[0]])
        drv[win[0]]["init"] = tuple(v + 1 for v in drv[win[0]]["init"])
    bad = []
    for (a, s0, b, s1), row in drv.items():
        n_init = initiator_field(frozenset(s0), frozenset(s1))
        n_foot = footprint_field(CLASSES[a], CLASSES[b])
        if (row["init"] != tuple(n_init[x] for x in SITES)
                or row["foot"] != tuple(n_foot[x] for x in SITES)):
            bad.append((a, s0, b, s1))
    LD.gate("G-DRIVEN-EQUALS-COMBINATORIAL",
            "for EVERY one of the %d window schedules the division-event "
            "field read off the DRIVEN record -- the initiator field from "
            "each arbitration's `op[1]`, the footprint field from each "
            "arbitration's `regs_of` footprint intersected with the actor set "
            "-- equals the field the combinatorial census computes from the "
            "schedule alone (#87, per object).  WHAT THIS EQUALITY IS, "
            "EXACTLY: given a record the layer did not refuse it is a "
            "THEOREM, not a measurement -- every event here is specified by "
            "its full tuple, so an appended event IS the specified tuple and "
            "the field is a function of the schedule.  The only way it can "
            "fail is a refusal.  The licence for the exhaustive columns is "
            "therefore CONSTRUCTIBILITY, which is the window-scoped thing, "
            "and the exhaustive columns inherit the window's INDUCTION -- "
            "measured on the window and on the out-of-window stratum "
            "witnesses below -- rather than its measurement"
            % len(WD),
            not bad, {"objects": len(drv), "mismatches": len(bad),
                      "first": str(bad[0]) if bad else None})

    foot_src = drv
    if mut("MUT-FOOTPRINT"):
        # object-level, and injected AFTER the equality gate so this mutant
        # reaches the gate it was declared to falsify
        foot_src = dict(drv)
        foot_src[win[1]] = dict(foot_src[win[1]])
        foot_src[win[1]]["foot"] = (3,) + foot_src[win[1]]["foot"][1:]
    foot_bad = [k for k, row in foot_src.items() if set(row["foot"]) != {2}]
    LD.gate("G-FOOTPRINT-CONSTANT",
            "AT THE FOOTPRINT READING THE DIVISION FIELD IS THE CONSTANT 2 AT "
            "EVERY SITE OF EVERY SCHEDULE, so its stabilizer is the whole "
            "group Z_3^2 identically -- checked on each of the %d driven "
            "records separately.  Each round's three conflict groups partition "
            "the nine cells, so every cell lies in exactly one footprint per "
            "round; the footprint reading is a CENSUS ARTIFACT of the "
            "committed budget and carries no information about the schedule.  "
            "This is the constant-field vacuous positive the U4 adjudication "
            "named, exhibited here as a property of the whole family"
            % len(WD),
            not foot_bad, {"objects": len(WD), "non_constant": len(foot_bad),
                           "value": 2})

    stabpair, affpair = C["stabpair"], C["affpair"]
    sidx = C["sidx"]
    W = 90
    weights = set(C["weight"].values())
    if mut("MUT-STAB-WEIGHT"):
        # the licence for the exhaustive column is the UNIFORM transversal
        # weight; corrupt it and the column loses its right to the family
        weights = {W, W + 1}
    stab_counts = Counter(stabpair.values())
    fam_stab = {k: v * W * W for k, v in stab_counts.items()}
    crystalline = sum(v for k, v in fam_stab.items() if k != "1")
    say("  seed-set pairs                    : %d" % len(stabpair))
    say("  partitions admitting a given seed set (uniform) : %s"
        % sorted(weights))
    for k in SUBGROUP_ORDER:
        if k in stab_counts:
            say("    Stab = %-9s : %6d seed pairs -> %9d schedules"
                % (k, stab_counts[k], fam_stab[k]))
    say("  CRYSTALLINE (initiator reading)   : %d of %d = %s"
        % (crystalline, family, Fraction(crystalline, family)))
    R["stabilizer"] = {
        "reading_initiator": {k: fam_stab.get(k, 0) for k in SUBGROUP_ORDER},
        "reading_footprint": {"Z3^2": family},
        "seed_pair_counts": dict(sorted(stab_counts.items())),
        "uniform_weight": W,
        "transversal_weights": sorted(weights),
        "crystalline": crystalline,
        "crystalline_fraction": str(Fraction(crystalline, family)),
        "routes": 3, "route_objects": len(route_rows),
    }
    LD.gate("G-STAB-FULL-FAMILY",
            "THE STABILIZER COLUMN IS EXHAUSTIVE OVER THE WHOLE FAMILY, not "
            "over a window.  The initiator field depends on the schedule only "
            "through its two seed sets, and every 3-subset of Z_3^2 is a "
            "transversal of exactly %d of the %d partitions -- a uniform "
            "weight, measured, not assumed -- so the %d seed-set pairs carry "
            "the whole census with multiplicity %d.  Measured: %d of %d "
            "schedules are crystalline at the initiator reading (%s), and the "
            "full group Z_3^2 never occurs there because six division events "
            "cannot spread evenly over nine sites"
            % (W, n_parts, len(stabpair), W * W, crystalline, family,
               Fraction(crystalline, family)),
            R["stabilizer"]["transversal_weights"] == [W]
            and len(stabpair) == 84 * 84
            and sum(fam_stab.values()) == family
            and "Z3^2" not in stab_counts,
            {"weights": sorted(weights), "pairs": len(stabpair),
             "per_subgroup": dict(sorted(stab_counts.items())),
             "family_check": sum(fam_stab.values())})
    SEAL.take("SEAL-STABILIZER", R)
    reg(crystalline, Fraction(crystalline, family), W, len(stabpair))
    for k in SUBGROUP_ORDER:
        if k in fam_stab:
            reg(fam_stab[k], stab_counts[k])

    # -- SEC 6  THE DETERMINANT ---------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 6   THE DETERMINANT COLUMN (pin R2.3) -- the weld-arena scout")
    say("=" * 78)
    det_class, det9 = C["det_class"], C["det9"]
    n_pairs = n_parts * n_parts
    n_det9 = len(det9)
    det9_scheds = n_det9 * 729
    posdef_max = pick("MUT-DET-POSDEF", C["posdef_max"], 9)
    strict_pos = pick("MUT-I7-STRICT", C["strict_pos"], 1)
    hom9 = sum(1 for r in det9 if r[2])
    uniform_sign = sum(1 for r in det9 if all(d < 0 for d in r[3]))
    mixed_sign = n_det9 - uniform_sign
    say("  partition pairs                       : %d" % n_pairs)
    say("  det != 0 at ALL NINE sites            : %d pairs -> %d schedules"
        % (n_det9, det9_scheds))
    say("  of those, homogeneous (one q at every site) : %d" % hom9)
    say("  of those, det < 0 at all nine sites    : %d ; mixed sign : %d"
        % (uniform_sign, mixed_sign))
    say("  max sites at which q is positive definite, over ALL pairs : %d"
        % posdef_max)
    say("  pairs meeting I7's strict positivity (all 27 counts > 0)  : %d"
        % strict_pos)
    say("  det values over the non-degenerate cells : %s"
        % dict(sorted(C["detvals"].items())))

    # THE NAMED WITNESS
    pidx = C["pidx"]
    wi = (pidx[CLASSES["ROW"]], pidx[CLASSES["ROW"]])
    wname = "ROW|ROW/DIAG"
    wn = link_counts(CLASSES["ROW"], CLASSES["ROW"])
    wrows = [i7_form(wn, x) for x in SITES]
    w_ok = all(r[3] != 0 for r in wrows) and len(set(wrows)) == 1
    w_ok = pick("MUT-DET-EMPTY", w_ok, False)
    wq = wrows[0]
    say("  NAMED WITNESS %s : q_11=%s q_22=%s q_12=%s det=%s at 9 of 9 sites"
        % (wname, wq[0], wq[1], wq[2], wq[3]))
    win_det9 = sum(1 for (a, s0, b, s1) in win
                   if det_class[(pidx[CLASSES[a]], pidx[CLASSES[b]])][0] == 9)
    pd_hist = Counter(C["pd_hist"])
    if mut("MUT-POSDEF-CEILING"):
        pd_hist[0] -= 1
        pd_hist[4] += 1
    pairs_with_posdef = n_pairs - pd_hist[0]
    max_total_inc = 2 * C["max_part_inc"]
    pairs_at_max_inc = C["parts_at_max"] ** 2
    if mut("MUT-INCIDENCE-WALL"):
        max_total_inc = 27
    R["determinant"] = {
        "partition_pairs": n_pairs, "nonzero_at_all_sites_pairs": n_det9,
        "window_nonzero_at_all_sites": win_det9,
        "nonzero_at_all_sites_schedules": det9_scheds,
        "fraction_pairs": str(Fraction(n_det9, n_pairs)),
        "homogeneous": hom9, "uniform_negative": uniform_sign,
        "mixed_sign": mixed_sign,
        "uniform_positive": C["det_all_positive"],
        "max_posdef_sites": posdef_max, "strictly_positive_pairs": strict_pos,
        "det_values": dict(sorted(C["detvals"].items())),
        "posdef_site_histogram": {str(k): pd_hist[k]
                                  for k in sorted(pd_hist)},
        "pairs_with_a_posdef_site": pairs_with_posdef,
        "schedules_with_a_posdef_site": pairs_with_posdef * 729,
        "posdef_site_share": str(Fraction(pairs_with_posdef * 729, family)),
        "posdef_cells": C["posdef_cells"],
        "max_link_incidence_per_pair": max_total_inc,
        "pairs_attaining_the_budget": pairs_at_max_inc,
        "min_incidences_at_a_posdef_site": C["min_inc_at_posdef"],
        "posdef_sites_below_three_incidences": C["posdef_under_three"],
        "wall_permits_posdef_sites": max_total_inc // 3,
        "witness": {"name": wname, "q11": str(wq[0]), "q22": str(wq[1]),
                    "q12": str(wq[2]), "det": str(wq[3])},
        "committed_schedule_det": str(det),
    }
    LD.gate("G-DET-NONZERO-EXISTS",
            "DET-NONZERO-EXISTS, AND THE WITNESS IS NAMED.  The schedule "
            "%s -- the committed constructor with round 1's column class "
            "replaced by the row class again, i.e. the schedule that never "
            "rotates its conflict groups, with the committed diagonal seeds -- "
            "induces q = [[%s, %s], [%s, %s]] with det = %s at every one of "
            "the nine sites, the same form at every site.  It is a member of "
            "the declared window and its record is FORCED.  Over the whole "
            "family %d of the %d partition pairs (%d of %d schedules) carry a "
            "non-degenerate induced form at all nine sites"
            % (wname, wq[0], wq[2], wq[2], wq[1], wq[3], n_det9, n_pairs,
               det9_scheds, family),
            w_ok and n_det9 > 0
            and fates[("ROW", DIAG_SEED, "ROW", DIAG_SEED)] == "FORCED",
            {"witness": wname, "row": R["determinant"]["witness"], "sites": 9,
             "pairs": n_det9, "schedules": det9_scheds,
             "e1_is_null": wq[0] == 0,
             "record_length": WD[("ROW", DIAG_SEED, "ROW", DIAG_SEED)]
             ["events"]})
    SEAL.take("SEAL-DET-WITNESS", R)
    LD.gate("G-POSDEF-EMPTY",
            "NO SCHEDULE IN THE FAMILY CARRIES A POSITIVE-DEFINITE INDUCED "
            "FORM AT EVERY SITE.  Exhaustively over all %d partition pairs "
            "the maximum number of sites at which q is positive definite is "
            "%d, never 9.  The mechanism is a budget: a partition into three "
            "triples has nine within-group pairs, and only those whose "
            "difference direction lies in I7's link set contribute, so the "
            "two rounds deposit at most 18 link-incidences over the nine "
            "sites -- while positive definiteness at a site needs q_11, q_22 "
            "> 0 and 4 q_11 q_22 > (n_(1,1) - q_11 - q_22)^2, hence at least "
            "3 incidences there, hence at least 27 in all.  The quantifier is "
            "AT EVERY SITE and it is load-bearing: positive-definite sites "
            "themselves are common (%d of the %d pairs carry at least one), "
            "and this gate says only that no pair carries nine"
            % (n_pairs, posdef_max, pairs_with_posdef, n_pairs),
            posdef_max < 9,
            {"pairs": n_pairs, "max_posdef_sites": posdef_max, "budget": 18,
             "needed": 27, "pairs_with_at_least_one": pairs_with_posdef})
    LD.gate("G-I7-STRICT-EMPTY",
            "I7's OWN ADMISSIBILITY CRITERION IS EMPTY ON THIS FAMILY: not "
            "one of the %d partition pairs makes all 27 link counts strictly "
            "positive, so no schedule is an admissible I7 geometry record, "
            "and the renewal-crystal weld census the U4 effectus predicted "
            "EMPTY is recorded EMPTY here for a reason the effectus did not "
            "have -- the link budget, not the diagonal alone"
            % n_pairs,
            strict_pos == 0, {"pairs": n_pairs, "strictly_positive": strict_pos,
                              "budget": 18, "needed": 27})
    LD.gate("G-POSDEF-CEILING",
            "THE MEASURED CEILING IS FINER THAN THE WALL, AND THAT GAP IS A "
            "MEASUREMENT AND NOT A THEOREM.  The same %d-incidence budget "
            "that forbids nine positive-definite sites permits as many as "
            "%d; the exhaustive census over all %d partition pairs attains "
            "%d, at %d pairs.  The full histogram of positive-definite sites "
            "per pair is %s, so %d pairs -- %d of the %d schedules, %s of the "
            "family -- carry at least one positive-definite site, over %d "
            "(pair, site) cells in all.  The third sign case is empty too: "
            "%d pairs have det > 0 at every one of the nine sites.  Anyone "
            "reading NEVER RIEMANNIAN as fully explained by the counting wall "
            "is reading past this gap, which is registered as an open"
            % (max_total_inc, R["determinant"]["wall_permits_posdef_sites"],
               n_pairs, posdef_max, pd_hist[posdef_max],
               R["determinant"]["posdef_site_histogram"], pairs_with_posdef,
               pairs_with_posdef * 729, family,
               R["determinant"]["posdef_site_share"], C["posdef_cells"],
               C["det_all_positive"]),
            sum(pd_hist.values()) == n_pairs
            and max(pd_hist) == posdef_max
            and posdef_max < R["determinant"]["wall_permits_posdef_sites"]
            and C["det_all_positive"] == 0,
            {"histogram": R["determinant"]["posdef_site_histogram"],
             "attained": posdef_max,
             "permitted_by_the_wall":
                 R["determinant"]["wall_permits_posdef_sites"],
             "uniform_positive_pairs": C["det_all_positive"]})
    SEAL.take("SEAL-DET-CEILING", R)
    LD.gate("G-INCIDENCE-WALL",
            "THE COUNTING WALL, WITH BOTH ITS PREMISES MEASURED AND ITS "
            "OMITTED STEP WRITTEN DOWN.  (i) Each round's partition into "
            "three triples has exactly nine within-group pairs, and a "
            "within-group pair contributes at most one link-incidence because "
            "I7's link set {(1,0), (0,1), (1,1)} holds exactly one "
            "representative of each of three of the four direction classes "
            "and nothing in the fourth: measured, the maximum total "
            "link-incidence over all %d partition pairs is exactly %d, "
            "ATTAINED at %d pairs, so the bound is tight and not merely an "
            "estimate.  (ii) Positive definiteness at a site needs q_11 > 0, "
            "q_22 > 0 -- that is n_(1,0) >= 1 and n_(0,1) >= 1 -- AND "
            "n_(1,1) >= 1, the step the delivered proof omitted: if "
            "n_(1,1) = 0 then q_12 = -(q_11 + q_22)/2 and "
            "det = -(q_11 - q_22)^2/4 <= 0, so the site is not positive "
            "definite.  Hence at least three incidences at a positive-definite "
            "site: measured, the minimum over every positive-definite cell in "
            "the census is exactly %d and %d such cells hold fewer.  (iii) "
            "Nine positive-definite sites would need at least 27 > %d.  The "
            "same count gives I7-STRICT-EMPTY directly: 27 strictly positive "
            "counts need 27 incidences"
            % (n_pairs, max_total_inc, pairs_at_max_inc,
               C["min_inc_at_posdef"], C["posdef_under_three"],
               max_total_inc),
            max_total_inc == 18 and pairs_at_max_inc > 0
            and C["min_inc_at_posdef"] == 3
            and C["posdef_under_three"] == 0 and max_total_inc < 27,
            {"budget": max_total_inc, "tight_at_pairs": pairs_at_max_inc,
             "min_incidences_at_a_posdef_site": C["min_inc_at_posdef"],
             "posdef_sites_below_three": C["posdef_under_three"],
             "needed_for_nine": 27})
    say("  of the %d window schedules, %d carry det != 0 at all nine sites"
        % (n_win, win_det9))
    say("  positive-definite sites per pair      : %s"
        % R["determinant"]["posdef_site_histogram"])
    say("  pairs with >= 1 positive-definite site: %d (%d schedules, %s)"
        % (pairs_with_posdef, pairs_with_posdef * 729,
           R["determinant"]["posdef_site_share"]))
    say("  link-incidence budget, measured       : %d, attained at %d pairs; "
        "a positive-definite site holds >= %d"
        % (max_total_inc, pairs_at_max_inc, C["min_inc_at_posdef"]))
    SEAL.take("SEAL-DETERMINANT", R)
    reg(n_pairs, n_det9, det9_scheds, hom9, uniform_sign, mixed_sign,
        posdef_max, strict_pos, wq[0], wq[1], wq[2], wq[3],
        Fraction(n_det9, n_pairs), det, 18, 27)
    reg(pairs_with_posdef, pairs_with_posdef * 729, C["posdef_cells"],
        C["det_all_positive"], max_total_inc, pairs_at_max_inc,
        C["min_inc_at_posdef"], C["posdef_under_three"],
        R["determinant"]["wall_permits_posdef_sites"],
        Fraction(pairs_with_posdef * 729, family))
    for k, v in pd_hist.items():
        reg(k, v)
    for k, v in C["detvals"].items():
        reg(Fraction(k), v)
    reg(win_det9)

    # THE RESOLVABLE CLASS-PAIR TABLE (the window's own geometry, published)
    cp_rows, cp_bad = [], []
    for a in CLASS_NAMES:
        for b in CLASS_NAMES:
            nn2 = link_counts(CLASSES[a], CLASSES[b])
            rows2 = [i7_form(nn2, x) for x in SITES]
            hom2 = len(set(rows2)) == 1
            nz2 = sum(1 for r in rows2 if r[3] != 0)
            r0 = rows2[0]
            cp_rows.append({"round0": a, "round1": b, "q11": str(r0[0]),
                            "q22": str(r0[1]), "q12": str(r0[2]),
                            "det": str(r0[3]), "homogeneous": hom2,
                            "nonzero_sites": nz2})
            reg(r0[0], r0[1], r0[2], r0[3], nz2)
            # each row must agree with the whole-family determinant column
            want_nz = det_class[(pidx[CLASSES[a]], pidx[CLASSES[b]])][0]
            if not hom2 or nz2 != want_nz:
                cp_bad.append((a, b))
    if mut("MUT-CLASSPAIR"):
        cp_rows[0] = dict(cp_rows[0])
        cp_rows[0]["det"] = "42"
        cp_bad = [("ROW", "ROW")]
    for r in cp_rows:
        say("    %s + %s : q_11=%-2s q_22=%-2s q_12=%-4s det=%-4s homogeneous "
            "%s, non-degenerate at %d of 9 sites"
            % (r["round0"], r["round1"], r["q11"], r["q22"], r["q12"],
               r["det"], r["homogeneous"], r["nonzero_sites"]))
    LD.gate("G-CLASS-PAIR-TABLE",
            "THE SIXTEEN RESOLVABLE CLASS PAIRS CARRY A HOMOGENEOUS INDUCED "
            "FORM, AND EACH ROW IS BOUND TO THE WHOLE-FAMILY COLUMN.  When "
            "both rounds group along parallel classes, every site sees the "
            "same q -- checked row by row (#87), and each row's "
            "non-degeneracy count is required to equal the number the "
            "exhaustive %d-pair census independently assigns to that pair.  "
            "%d of the 16 pairs are non-degenerate at all nine sites, which "
            "is why %d of the %d window schedules are"
            % (n_pairs, sum(1 for r in cp_rows if r["nonzero_sites"] == 9),
               win_det9, n_win),
            not cp_bad, {"rows": len(cp_rows), "mismatches": cp_bad or "none",
                         "table": cp_rows})
    R["class_pairs"] = cp_rows
    reg(len(cp_rows))
    SEAL.take("SEAL-CLASS-PAIRS", R)

    # -- SEC 7  THE AFFINE NULL ---------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 7   THE AFFINE NULL (pin R3) -- coset-union vs beyond-coset")
    say("=" * 78)
    aff_counts = Counter(affpair.values())
    joint = Counter((affpair[k], stabpair[k]) for k in affpair)
    strat = {}
    for a in ("CU-JOINT", "CU-SPLIT", "BEYOND-COSET"):
        tot = aff_counts[a] * W * W
        cry = sum(v for (aa, s), v in joint.items()
                  if aa == a and s != "1") * W * W
        subs = sorted({s for (aa, s), v in joint.items()
                       if aa == a and s != "1" and v > 0})
        strat[a] = {"schedules": tot, "crystalline": cry,
                    "fraction": str(Fraction(cry, tot)), "subgroups": subs}
        say("  %-13s : %9d schedules, %9d crystalline = %-6s  subgroups %s"
            % (a, tot, cry, Fraction(cry, tot), subs or "-"))
    cu_ok = pick("MUT-AFFINE-NULL",
                 all(stabpair[k] != "1" for k in affpair
                     if affpair[k] == "CU-JOINT"), False)
    LD.gate("G-AFFINE-LAW",
            "THE AFFINE NULL HOLDS EXACTLY WHERE IT IS PREDICTED TO.  Every "
            "one of the %d CU-JOINT seed pairs -- both seed sets a coset of "
            "ONE order-3 subgroup H -- is evaluated on its own field and every "
            "one has Stab containing H: %d of %d schedules, 100 per cent.  "
            "This is the U4 adjudication's mechanism n = c + m*1_S read as a "
            "prediction and confirmed; the crystallinity of these schedules "
            "carries NO emergence information"
            % (aff_counts["CU-JOINT"], strat["CU-JOINT"]["crystalline"],
               strat["CU-JOINT"]["schedules"]),
            cu_ok, {"cu_joint_pairs": aff_counts["CU-JOINT"],
                    "crystalline": strat["CU-JOINT"]["crystalline"],
                    "schedules": strat["CU-JOINT"]["schedules"]})
    split_ok = pick("MUT-CU-SPLIT",
                    all(stabpair[k] == "1" for k in affpair
                        if affpair[k] == "CU-SPLIT"), False)
    LD.gate("G-CU-SPLIT-EMPTY",
            "AND IT HOLDS NOWHERE ELSE AMONG THE COSET SEEDS.  Every one of "
            "the %d CU-SPLIT seed pairs -- both seed sets cosets, of "
            "DIFFERENT subgroups -- is evaluated on its own field and every "
            "one has trivial stabilizer: two lines of different directions "
            "meet in exactly one point, so the field takes the value 2 at a "
            "single site, and no order-3 period can carry a value that occurs "
            "once.  %d of %d schedules crystalline"
            % (aff_counts["CU-SPLIT"], strat["CU-SPLIT"]["crystalline"],
               strat["CU-SPLIT"]["schedules"]),
            split_ok, {"cu_split_pairs": aff_counts["CU-SPLIT"],
                       "crystalline": strat["CU-SPLIT"]["crystalline"]})
    bc_pairs = [k for k in affpair
                if affpair[k] == "BEYOND-COSET" and stabpair[k] != "1"]
    bc_subs = sorted({stabpair[k] for k in bc_pairs})
    bc_count = pick("MUT-CRYSTAL-SEEDED", len(bc_pairs), 0)
    inv = {v: k for k, v in sidx.items()}
    bc_wit = []
    for k in sorted(bc_pairs)[:4]:
        bc_wit.append({"S0": sorted(inv[k[0]]), "S1": sorted(inv[k[1]]),
                       "stab": stabpair[k],
                       "S0_is_line": inv[k[0]] in AG_LINES,
                       "S1_is_line": inv[k[1]] in AG_LINES})
    for w in bc_wit:
        say("    beyond-coset crystalline witness: S0=%s S1=%s -> Stab %s "
            "(lines: %s, %s)" % (w["S0"], w["S1"], w["stab"],
                                 w["S0_is_line"], w["S1_is_line"]))
    LD.gate("G-BEYOND-COSET-CRYSTALLINE",
            "CRYSTALLINITY IS NOT CONFINED TO THE CONSTRUCTOR-INHERITED "
            "LOCUS.  %d of the %d beyond-coset seed pairs -- at least one "
            "seed set NOT a coset of any order-3 subgroup -- carry a "
            "nontrivial translation stabilizer, and each is verified on its "
            "own field: %d of %d beyond-coset schedules, a rate of %s, "
            "realizing all four order-3 subgroups %s.  The mechanism is "
            "measured too: the field takes the value 1 on a union of two "
            "H-cosets and 0 on the third while NEITHER seed set is an "
            "H-coset, so the period is a property of the PAIR and not of "
            "either seed"
            % (len(bc_pairs), aff_counts["BEYOND-COSET"],
               strat["BEYOND-COSET"]["crystalline"],
               strat["BEYOND-COSET"]["schedules"],
               strat["BEYOND-COSET"]["fraction"], bc_subs),
            bc_count > 0 and len(bc_subs) == 4,
            {"beyond_coset_crystalline_pairs": bc_count,
             "beyond_coset_pairs": aff_counts["BEYOND-COSET"],
             "subgroups": bc_subs, "witnesses": bc_wit})
    R["affine"] = {"classes": strat, "beyond_coset_subgroups": bc_subs,
                   "beyond_coset_witnesses": bc_wit,
                   "committed_class": affine_class(frozenset(DIAG_SEED),
                                                   frozenset(DIAG_SEED))}
    SEAL.take("SEAL-AFFINE", R)
    for a in strat:
        reg(strat[a]["schedules"], strat[a]["crystalline"])
        reg(Fraction(strat[a]["crystalline"], strat[a]["schedules"]))
    reg(aff_counts["CU-JOINT"], aff_counts["CU-SPLIT"],
        aff_counts["BEYOND-COSET"], len(bc_pairs))

    # -- THE CARRIER OF THE PERIOD ------------------------------------------
    carrier_rows = C["carrier_rows"]
    carrier_bad = list(C["carrier_bad"])
    line_seed = list(C["line_seed"])
    if mut("MUT-UNION-CARRIER"):
        carrier_bad = [carrier_rows[0][0]]
    if mut("MUT-LINE-SEED"):
        line_seed = [carrier_rows[-1][0]]
    n_cry_pairs = len(carrier_rows)
    same_seed = C["same_seed"]
    two_coset = n_cry_pairs - same_seed
    closed_216 = len(DIRECTIONS) * 3 * 18
    closed_36 = len(DIRECTIONS) * 3 * 2 + len(DIRECTIONS) * 3
    bc_share = Fraction(strat["BEYOND-COSET"]["crystalline"], crystalline)
    R["carrier"] = {
        "crystalline_seed_pairs": n_cry_pairs,
        "support_is_a_coset_union": n_cry_pairs - len(carrier_bad),
        "value_shapes": {k: v for k, v in sorted(C["shape"].items())},
        "same_seed_set_pairs": same_seed,
        "two_coset_pairs": two_coset,
        "beyond_coset_with_a_line_seed": len(line_seed),
        "closed_form_beyond_coset": closed_216,
        "closed_form_cu_joint": closed_36,
        "closed_form_total": len(DIRECTIONS) * 63,
        "beyond_coset_share_of_crystallinity": str(bc_share),
    }
    say("  crystalline seed pairs                : %d (%d = %d x 63)"
        % (n_cry_pairs, len(DIRECTIONS) * 63, len(DIRECTIONS)))
    say("  supp(n) a union of cosets of Stab(n)  : %d of %d"
        % (n_cry_pairs - len(carrier_bad), n_cry_pairs))
    say("  value shapes over the 9 sites         : %s"
        % R["carrier"]["value_shapes"])
    say("  beyond-coset share of ALL crystallinity : %s" % bc_share)
    LD.gate("G-UNION-CARRIER",
            "THE CARRIER OF THE PERIOD IS THE SUM, NOT EITHER SUMMAND -- AND "
            "IT IS A COSET UNION AT EVERY CRYSTALLINE PAIR.  For each of the "
            "%d crystalline seed pairs the support of the division field is "
            "tested against the cosets of THAT FIELD'S OWN period subgroup: "
            "%d of %d are exactly a union of them, in two shapes -- %d pairs "
            "with the two seed sets EQUAL, so the field is 2 on one coset and "
            "0 elsewhere, and %d pairs with the field 1 on two cosets and 0 "
            "on the third.  So the affine law n = c + m*1_S is violated "
            "NOWHERE in this census: it holds on the UNION of the two seed "
            "sets.  What the census measures is that the inherited argument "
            "was stated on the wrong variable -- the per-seed locus contains "
            "one seventh of the crystallinity it was supposed to explain, and "
            "the beyond-coset class carries the other %s -- not that a "
            "mechanism outside the affine law exists on this arena.  The "
            "mechanism is closed in closed form and needs no census: %d "
            "subgroups x 3 choices of the empty coset x 18 ordered splits of "
            "the remaining six sites that are not the two cosets themselves = "
            "%d beyond-coset pairs, and %d coset-union pairs, %d in all"
            % (n_cry_pairs, n_cry_pairs - len(carrier_bad), n_cry_pairs,
               same_seed, two_coset, bc_share, len(DIRECTIONS), closed_216,
               closed_36, len(DIRECTIONS) * 63),
            not carrier_bad and len(bc_pairs) == closed_216
            and aff_counts["CU-JOINT"] == closed_36
            and n_cry_pairs == len(DIRECTIONS) * 63
            and same_seed + two_coset == n_cry_pairs,
            {"pairs": n_cry_pairs, "not_a_coset_union": len(carrier_bad),
             "shapes": R["carrier"]["value_shapes"],
             "closed_forms": [closed_216, closed_36, len(DIRECTIONS) * 63],
             "beyond_coset_share": str(bc_share)})
    SEAL.take("SEAL-CARRIER", R)
    LD.gate("G-NO-LINE-SEED",
            "AT EVERY BEYOND-COSET CRYSTALLINE PAIR, NEITHER SEED SET IS A "
            "LINE AT ALL -- not merely 'not a coset of the period'.  All %d "
            "are checked one by one against the 12 lines of AG(2,3): %d have "
            "a line seed.  The reason is geometric and not statistical: a "
            "coset of a DIFFERENT order-3 subgroup meets each coset of the "
            "period exactly once, so it cannot sit inside the union of two of "
            "them"
            % (len(bc_pairs), len(line_seed)),
            not line_seed,
            {"beyond_coset_crystalline_pairs": len(bc_pairs),
             "with_a_line_seed": len(line_seed),
             "lines_of_AG23": len(AG_LINES)})
    reg(n_cry_pairs, same_seed, two_coset, closed_216, closed_36,
        len(DIRECTIONS) * 63, bc_share, len(AG_LINES), len(line_seed))
    for k, v in C["shape"].items():
        reg(v)

    # -- THE PERIOD AND THE DIAGONAL LINK COUNT, JOINTLY --------------------
    per_period = C["per_period"]
    per_populated = dict(C["per_populated"])
    if mut("MUT-JOINT-COUPLING"):
        per_populated["<(1,1)>"] = per_populated["<(1,0)>"]
    empty_total = sum(per_period[k] - per_populated[k] for k in per_period)
    diag_empty = per_period["<(1,1)>"] - per_populated["<(1,1)>"]
    cond = Fraction(diag_empty, empty_total) if empty_total else Fraction(0)
    marginal = Fraction(1, len(DIRECTIONS))
    R["period_vs_diagonal"] = {
        "per_period_schedules": {k: per_period[k] for k in sorted(per_period)},
        "diagonal_link_populated": {k: per_populated[k]
                                    for k in sorted(per_populated)},
        "populated_rate": {k: str(Fraction(per_populated[k], per_period[k]))
                           for k in sorted(per_period)},
        "marginal_uniform": len({per_period[k] for k in per_period}) == 1,
        "crystalline_with_an_empty_diagonal": empty_total,
        "of_those_period_is_the_diagonal": diag_empty,
        "conditional": str(cond), "under_independence": str(marginal),
    }
    say("  period vs diagonal link, populated    : %s"
        % R["period_vs_diagonal"]["populated_rate"])
    say("  crystalline with an EMPTY diagonal    : %d, of which the period IS "
        "the diagonal: %d = %s (against %s under independence)"
        % (empty_total, diag_empty, cond, marginal))
    LD.gate("G-PERIOD-DIAGONAL-JOINT",
            "THE PERIOD AND THE DIAGONAL LINK COUNT ARE SEPARATELY CARRIED "
            "AND NEITHER DETERMINES THE OTHER -- BUT THEY ARE NOT "
            "INDEPENDENT, AND THE DEPARTURE IS EXACTLY AT THE DIAGONAL.  The "
            "MARGINAL is exactly uniform: %s crystalline schedules in each of "
            "the four period directions.  The JOINT is not: the diagonal link "
            "count is populated at %s of crystalline schedules in each of the "
            "three non-diagonal directions but at %s when the period IS the "
            "diagonal.  Conditionally, among the %d crystalline schedules "
            "whose diagonal link count is EMPTY, the period is the diagonal "
            "at %d of them -- %s, against %s under independence.  The period "
            "is a seed property and the diagonal link count a grouping "
            "property; the residual coupling is the transversal constraint "
            "between seed sets and groupings, and it is read as nothing else"
            % (sorted({per_period[k] for k in per_period}),
               R["period_vs_diagonal"]["populated_rate"]["<(1,0)>"],
               R["period_vs_diagonal"]["populated_rate"]["<(1,1)>"],
               empty_total, diag_empty, cond, marginal),
            R["period_vs_diagonal"]["marginal_uniform"]
            and per_populated["<(1,1)>"] < per_populated["<(1,0)>"]
            and cond > marginal,
            {"marginal_uniform": R["period_vs_diagonal"]["marginal_uniform"],
             "rates": R["period_vs_diagonal"]["populated_rate"],
             "conditional": str(cond), "independence": str(marginal)})
    SEAL.take("SEAL-JOINT", R)
    for k in per_period:
        reg(per_period[k], per_populated[k],
            Fraction(per_populated[k], per_period[k]))
    reg(empty_total, diag_empty, cond, marginal)

    # -- the joint stratum: crystalline AND non-degenerate ------------------
    tr_index = C["tr_index"]
    joint_det = C["joint_det"]
    cry_det = sum(v for (s, a), v in joint_det.items() if s != "1")
    cry_det_bc = sum(v for (s, a), v in joint_det.items()
                     if s != "1" and a == "BEYOND-COSET")
    say("  crystalline AND non-degenerate        : %d schedules (%d of them "
        "beyond-coset)" % (cry_det, cry_det_bc))
    strata = {"joint_det_stab": {"%s|%s" % k: v
                                 for k, v in sorted(joint_det.items())},
              "crystalline_and_nondegenerate": cry_det,
              "crystalline_and_nondegenerate_beyond_coset": cry_det_bc}

    # -- the strata witnesses, driven ---------------------------------------
    want, found = C["want"], C["witness"]
    wit_rows, driven_wit = [], 0
    inv_sub = {v: k for k, v in sidx.items()}
    for key in sorted(want):
        loc = found.get(key)
        if loc is None:
            continue
        i0, i1, t0, t1 = loc
        S0 = align_seeds(parts[i0], inv_sub[t0])
        S1 = align_seeds(parts[i1], inv_sub[t1])
        rec = driven(G, schedule_of(parts[i0], S0, parts[i1], S1))
        driven_wit += 1
        wit_rows.append({"stratum": "%s|%s|det9=%s" % key,
                         "S0": sorted(S0), "S1": sorted(S1),
                         "events": rec["events"], "maxhits": rec["maxhits"],
                         "refusal": rec["refusal"],
                         "divisions": len(rec["divisions"]),
                         "in_window": parts[i0] in CLASSES.values()
                         and parts[i1] in CLASSES.values()})
    if mut("MUT-STRATUM-BLIND") and wit_rows:
        wit_rows = wit_rows[:-1]
        driven_wit -= 1
    missing = sorted(k for k in want if found.get(k) is None)
    all_forced = all(w["refusal"] is None and w["maxhits"] == 1
                     for w in wit_rows)
    say("  census strata (stab x affine x det9)  : %d, all witnessed by a "
        "menu-driven schedule outside as well as inside the window: %d"
        % (len(want), driven_wit))
    strata["witnesses"] = wit_rows
    strata["strata_count"] = len(want)
    strata["witnesses_outside_the_window"] = sum(
        1 for w in wit_rows if not w["in_window"])
    R["strata"] = strata
    LD.gate("G-STRATA-WITNESSED",
            "EVERY NONEMPTY CENSUS STRATUM HAS A MENU-DRIVEN WITNESS.  The "
            "%d nonempty (stabilizer x affine-class x non-degeneracy) strata "
            "of the WHOLE family are each given a deterministic representative "
            "-- the first in a fixed enumeration, no sampling -- and each "
            "representative's record is built by driving the layer's menus: "
            "%d witnesses, every one FORCED (maxhits = 1, no refusal, 6 "
            "division events).  So the grammar's verdict is not confined to "
            "the resolvable window: it has been taken at least once in every "
            "cell of the census" % (len(want), driven_wit),
            not missing and all_forced
            and len(R["strata"]["witnesses"]) == len(want),
            {"strata": len(want), "witnessed": driven_wit,
             "published_witnesses": len(R["strata"]["witnesses"]),
             "outside_the_window":
                 R["strata"]["witnesses_outside_the_window"],
             "missing": [str(m) for m in missing],
             "all_forced": all_forced})
    SEAL.take("SEAL-STRATA", R)
    reg(cry_det, cry_det_bc, len(want), driven_wit,
        R["strata"]["witnesses_outside_the_window"])

    # -- SEC 8  FRAGILITY ----------------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 8   FRAGILITY (pin R2.4) -- computed, not sampled, on the window")
    say("=" * 78)
    frag_rows = Counter()
    frag_bad = []
    n_cryst_win = 0
    for (a, s0, b, s1) in win:
        key = (sidx[frozenset(s0)], sidx[frozenset(s1)])
        sname = stabpair[key]
        if sname == "1":
            continue
        n_cryst_win += 1
        H = SUBGROUPS[sname]
        broken = admissible_edits = 0
        for which, (cls, seeds) in enumerate(((CLASSES[a], s0),
                                              (CLASSES[b], s1))):
            for gi, g in enumerate(cls):
                old = seeds[gi]
                for new in g:
                    if new == old:
                        continue
                    ns = tuple(new if k == gi else seeds[k]
                               for k in range(3))
                    edit = ((a, ns, b, s1) if which == 0 else (a, s0, b, ns))
                    if edit not in WD or WD[edit]["refusal"] is not None:
                        continue
                    admissible_edits += 1
                    k2 = (sidx[frozenset(edit[1])], sidx[frozenset(edit[3])])
                    if not SUBGROUPS[stabpair[k2]] >= H:
                        broken += 1
        frag_rows[(broken, admissible_edits)] += 1
        if broken != admissible_edits or admissible_edits != 12:
            frag_bad.append((a, s0, b, s1))
    if mut("MUT-FRAGILITY"):
        frag_bad = [win[0]]
    say("  crystalline schedules in the window   : %d" % n_cryst_win)
    say("  (broken, admissible) edit census      : %s"
        % {str(k): v for k, v in sorted(frag_rows.items())})
    LD.gate("G-FRAGILITY",
            "THE CRYSTAL IS MAXIMALLY FRAGILE, AT EVERY CRYSTALLINE SCHEDULE "
            "OF THE WINDOW.  A single-arbitration re-seating -- moving exactly "
            "one division event to another cell of its own conflict group, "
            "the smallest edit that stays in the family -- has %d admissible "
            "forms at every schedule (6 arbitrations x 2 alternative seats, "
            "each an admissible member of the window in its own right), and "
            "at every one of the %d crystalline window schedules ALL of them "
            "destroy the period.  Each schedule is evaluated against its own "
            "edits (#87).  The mechanism: the edit changes the field by "
            "1_new - 1_old, and a difference of two distinct point masses is "
            "never constant on the cosets of an order-3 subgroup"
            % (12, n_cryst_win),
            not frag_bad and n_cryst_win > 0,
            {"crystalline_window": n_cryst_win,
             "census": {str(k): v for k, v in sorted(frag_rows.items())},
             "exceptions": len(frag_bad)})

    frag_kept = pick("MUT-FRAG-FAMILY", C["frag_kept"], 1)
    frag_nontrivial = pick("MUT-FRAG-FAMILY", C["frag_nontrivial"], 1)
    R["fragility"] = {"crystalline_in_window": n_cryst_win,
                      "edits_per_schedule": 12,
                      "census": {str(k): v
                                 for k, v in sorted(frag_rows.items())},
                      "family_scope_cases": C["frag_cases"],
                      "family_scope_period_preserved": frag_kept,
                      "family_scope_any_nontrivial_period": frag_nontrivial}
    say("  family-scope re-seatings              : %d, preserving the period "
        "%d, landing on ANY nontrivial period %d"
        % (C["frag_cases"], frag_kept, frag_nontrivial))
    LD.gate("G-FRAGILITY-FAMILY",
            "AND THE FRAGILITY IS A FAMILY-SCOPE THEOREM, NOT A WINDOW "
            "MEASUREMENT.  Over ALL %d crystalline seed pairs and ALL %d "
            "single-point re-seatings of either seed to any other site -- a "
            "strict superset of the admissible single-arbitration re-seatings "
            "of ANY partition, not just the window's -- %d preserve the "
            "original period and %d leave the edited field with ANY "
            "nontrivial period at all.  So the crystal is not merely "
            "un-preserved under the minimal admissible edit: it is DESTROYED "
            "by it, everywhere in the family.  This closes the gap the "
            "one-line mechanism leaves open, which is that an edit might land "
            "on a DIFFERENT period and rotate the crystal rather than destroy "
            "it"
            % (len(C["carrier_rows"]), C["frag_cases"], frag_kept,
               frag_nontrivial),
            frag_kept == 0 and frag_nontrivial == 0
            and C["frag_cases"] == len(C["carrier_rows"]) * 2 * 3 * 6,
            {"pairs": len(C["carrier_rows"]), "cases": C["frag_cases"],
             "period_preserved": frag_kept,
             "any_nontrivial_period": frag_nontrivial})
    SEAL.take("SEAL-FRAGILITY", R)
    reg(n_cryst_win, 12, 6, 2, C["frag_cases"], frag_kept, frag_nontrivial)

    # -- THE PROCESSING-ORDER FIBER, MEASURED -------------------------------
    order_scheds = [COMMITTED,
                    schedule_of(CLASSES["ROW"], DIAG_SEED,
                                CLASSES["ROW"], DIAG_SEED)]
    for key in sorted(want):           # the first OUT-OF-WINDOW witness
        loc = found.get(key)
        if loc is None:
            continue
        i0, i1, t0, t1 = loc
        if parts[i0] in CLASSES.values() and parts[i1] in CLASSES.values():
            continue
        order_scheds.append(schedule_of(
            parts[i0], align_seeds(parts[i0], inv_sub[t0]),
            parts[i1], align_seeds(parts[i1], inv_sub[t1])))
        break
    order_rows = order_probe(G, order_scheds)
    if mut("MUT-ORDER-VARIANT"):
        order_rows = list(order_rows)
        order_rows[1] = dict(order_rows[1], fields_match=False)
    order_bad = [r for r in order_rows
                 if not (r["forced"] and r["fields_match"]
                         and r["events_match"])]
    R["processing_order"] = {
        "conventions_per_round": len(ORDER_PERMS) ** 2,
        "schedules_probed": len(order_scheds),
        "drives": len(order_rows),
        "deviations": len(order_bad)}
    say("  processing-order variants driven      : %d over %d schedules, "
        "deviations %d" % (len(order_rows), len(order_scheds), len(order_bad)))
    LD.gate("G-ORDER-INVARIANCE",
            "THE PROCESSING ORDER IS A DECLARED CONVENTION WITH A MEASURED "
            "FIBER.  d66's order -- groups in ascending seed-site index, "
            "members in ascending site index -- pins the committed POINT; "
            "extending it to the whole family is a choice with %d forms per "
            "round (3! group orders x 3! member orders), and this unit "
            "declares rather than derives it.  Every one of those %d "
            "conventions is DRIVEN, APPLIED TO BOTH ROUNDS, at %d declared "
            "schedules -- %d records -- and compared against the committed "
            "convention's: %d deviations in fate, in event count, or in "
            "either site field.  The probe covers the conventions applied "
            "uniformly across the rounds, not every pairing of two different "
            "ones.  The choice is inert where it is driven, and the inventory "
            "says so instead of asserting a fiber of one"
            % (len(ORDER_PERMS) ** 2, len(ORDER_PERMS) ** 2,
               len(order_scheds), len(order_rows), len(order_bad)),
            not order_bad and len(order_rows) == len(order_scheds)
            * len(ORDER_PERMS) ** 2,
            {"conventions": len(ORDER_PERMS) ** 2,
             "records": len(order_rows), "deviations": len(order_bad)})
    SEAL.take("SEAL-ORDER", R)
    reg(len(ORDER_PERMS) ** 2, len(order_rows), len(order_bad),
        len(order_scheds))

    # -- THE SUCCESSOR'S ENTRY DATUM (outside this unit's family) -----------
    sat = r3_saturating()
    if mut("MUT-R3-SATURATION"):
        sat = dict(sat, det="0", posdef_sites=0)
    R["successor_probe"] = sat
    say("  SUCCESSOR PROBE (R=3, outside this family): n = 1 at all %d cells, "
        "q_11=%s q_22=%s q_12=%s det=%s, positive definite at %d of 9"
        % (sat["cells"], sat["q11"], sat["q22"], sat["q12"], sat["det"],
           sat["posdef_sites"]))
    LD.gate("G-R3-SATURATION",
            "THE WELD ROUTE'S EXACT DEMAND, COMPUTED AND READ NO FURTHER.  "
            "The counting wall says the obstruction is a RESOURCE DEFICIT in "
            "the committed cycle, so the successor's entry criterion is a "
            "budget depositing at least 27 link-incidences on I7's link set.  "
            "The minimal saturating arrangement is exhibited here: R = %d, "
            "the three rounds grouped on the three link-direction parallel "
            "classes, giving n = 1 at all %d cells, q = [[%s, %s], [%s, %s]], "
            "det = %s at every site, positive definite at %d of the nine, and "
            "I7's strict-positivity criterion satisfied for the first time "
            "(%d of %d counts strictly positive).  THIS IS A PROBE OUTSIDE "
            "THIS UNIT'S DECLARED FAMILY, which is R = 2; nothing above uses "
            "it, no record is driven for it, and it says nothing about "
            "whether such a schedule is grammar-admissible or whether "
            "clearing the count clears the weld"
            % (sat["rounds"], sat["cells"], sat["q11"], sat["q12"],
               sat["q12"], sat["q22"], sat["det"], sat["posdef_sites"],
               sat["strictly_positive_cells"], sat["cells"]),
            sat["distinct_counts"] == [1] and sat["det"] == "3/4"
            and sat["posdef_sites"] == 9 and sat["homogeneous"]
            and sat["strictly_positive_cells"] == 27,
            {"probe": sat, "in_this_family": False})
    SEAL.take("SEAL-SUCCESSOR", R)
    reg(sat["rounds"], sat["cells"], Fraction(sat["det"]),
        Fraction(sat["q11"]), Fraction(sat["q22"]), Fraction(sat["q12"]),
        sat["posdef_sites"], sat["strictly_positive_cells"])

    # -- SEC 9  THE WALLS ----------------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 9   THE WALLS (pin R4), the four inherited from U4")
    say("=" * 78)
    src_text = read_text(SELF)
    banned_here = norm(BANNED_L1) in norm(src_text)
    paper_under_test = paper_text
    if mut("MUT-WALL-L1"):
        paper_under_test = paper_text + (
            "\n\nOrder-level covariance is\nprecisely the form U4 tests, and "
            "precisely the form the\ncorpus's strongest relativity result "
            "took.\n")
    if mut("MUT-WALL-L1-QUOTED"):
        # THE EVASION THE WHITESPACE-ONLY FOLD WALKED PAST: the retracted
        # sentence re-wrapped as a MARKDOWN BLOCKQUOTE, which is the corpus's
        # own house style for quoting a prior unit
        paper_under_test = paper_text + (
            "\n\n> Order-level covariance is\n> precisely the form U4 tests, "
            "and\n> precisely the form the corpus's\n> strongest relativity "
            "result took.\n")
    paper_norm = norm(ascii_fold(paper_under_test))
    l1_absent = norm(ascii_fold(BANNED_L1)) not in paper_norm
    l1_argued = ("fourth form" in paper_norm
                 and "not tested here" in paper_norm)
    LD.gate("G-WALL-L1",
            "L-1 IS ARGUED BEFORE ANY TEST AND THEN DECLINED, AND THE "
            "RETRACTED SENTENCE IS ABSENT.  Order-level covariance is a "
            "fourth form outside paper 8's three (verbatim anchor V07) and "
            "its admissibility is v11's to argue; this unit measures a "
            "PERMUTATION action of Z_3^2 on the actor set, which L-1's own "
            "scope guard leaves free, constructs no bridge from those "
            "translations to any boost, and states in the paper that the "
            "fourth form is NOT TESTED HERE.  The prohibition gate ASCII-folds "
            "BOTH sides, STRIPS LEADING MARKDOWN LINE-DECORATIONS and only "
            "then whitespace-normalises (#125 as this unit's adjudication "
            "clarified it), so both a line-wrapped and a BLOCKQUOTED "
            "injection of the %d-character retracted sentence are caught -- "
            "MUT-WALL-L1 injects the first and MUT-WALL-L1-QUOTED the second, "
            "and the blockquote is the form the corpus actually writes"
            % len(BANNED_L1),
            l1_absent and (l1_argued or not paper_text),
            {"banned_len": len(BANNED_L1), "absent_from_paper": l1_absent,
             "argued_first": l1_argued, "present_in_source_prose":
             banned_here})

    # THE BHS WALL, MEASURED ON THIS PROGRAM'S OWN AST rather than declared.
    # The stems occur in this file as PROSE -- gate statements, mutant
    # descriptions, the verbatim anchor -- and the honest question is whether
    # any of them names a COMPUTATION.
    BARRED_STEMS = ("sprinkl", "boost", "rapidit", "frame", "poisson",
                    "lorentz")
    idents = set()
    for nd in ast.walk(ast.parse(src_text)):
        if isinstance(nd, ast.Name):
            idents.add(nd.id)
        elif isinstance(nd, ast.Attribute):
            idents.add(nd.attr)
        elif isinstance(nd, (ast.FunctionDef, ast.ClassDef)):
            idents.add(nd.name)
        elif isinstance(nd, ast.arg):
            idents.add(nd.arg)
        elif isinstance(nd, ast.keyword) and nd.arg:
            idents.add(nd.arg)
    idents |= pick("MUT-WALL-BHS", set(), {"rapidity_of_the_boost_frame"})
    bhs_hits = sorted(i for i in idents
                      if any(s in i.lower() for s in BARRED_STEMS))
    prose = {s: len(re.findall(s, src_text, re.I)) for s in BARRED_STEMS}
    LD.gate("G-WALL-BHS",
            "NO SPRINKLING-GRADE LORENTZ-INVARIANCE TEST IS RUN.  The "
            "catalog's BHS block (verbatim anchor V08) says a Poisson "
            "sprinkling admits no Lorentz-invariant finite-valency graph, and "
            "these schedules are finite-valency by construction, so running "
            "the test would manufacture a false negative.  MEASURED, and the "
            "measurement is an AST SCAN OF THIS PROGRAM'S OWN SOURCE: of the "
            "%d identifiers this file defines or references -- every name, "
            "attribute, function, class, argument and keyword -- %d are named "
            "for a sprinkling, a boost, a rapidity, a Poisson process, a "
            "Lorentz transformation or a frame.  The stems DO occur in the "
            "file, %s times, entirely in prose: gate statements, mutant "
            "descriptions and the verbatim catalog anchor.  A gate that "
            "counted those would be counting its own bar; a gate that "
            "declared the absence would measure nothing.  The only group that "
            "acts here is the translation group of a 9-element site lattice"
            % (len(idents), len(bhs_hits), sum(prose.values())),
            not bhs_hits,
            {"identifiers_scanned": len(idents), "computing_hits": bhs_hits,
             "prose_occurrences": prose,
             "groups_acting": ["Z_3^2 translations"]})
    kr_hay = pick("MUT-WALL-KR", paper_norm.lower(),
                  paper_norm.lower().replace("height", "") + " dimension")
    kr_ok = ("dimension" not in kr_hay or "height" in kr_hay)
    LD.gate("G-WALL-KR",
            "NO DIMENSION READING IS TAKEN, SO THE KLEITMAN-ROTHSCHILD HEIGHT "
            "CONTROL HAS NOTHING TO CONTROL.  The catalog's carry is that a "
            "dimension reading without a height control is worthless "
            "(verbatim anchor V09).  This unit measures no chart width, no "
            "Myrheim-Meyer estimate and no max-shatter dimension: its columns "
            "are a translation stabilizer, a determinant and a "
            "constructibility fate, none of which is dimension-adjacent.  The "
            "gate is the conjunction: either the paper takes no dimension "
            "reading, or it carries a height control",
            kr_ok, {"dimension_reading": pick("MUT-WALL-KR", "none",
                                             "chart width"),
                    "paper_mentions_height": "height" in kr_hay})
    # the wall bars a cosmological READING, not the word: the paper is
    # required to SAY the reading is barred, so the needles are claim
    # phrases, never the bare stem
    COSMO_CLAIMS = ("cosmological constant", "hubble", "dark energy",
                    "expansion of the universe", "cosmic microwave",
                    "scale factor", "cosmological model")
    cosmo_hay = pick("MUT-WALL-COSMO", paper_norm.lower(),
                     paper_norm.lower() + " the measured period is the "
                     "expansion of the universe")
    cosmo = [w for w in COSMO_CLAIMS if w in cosmo_hay]
    diag_measured = ("(1,1)" in paper_norm or "<(1,1)>" in paper_norm)
    # NAMED-NOT-READ: the protocol requires the Lorentzian resonance to be
    # NAMED so that the reader cannot supply it ungoverned.  Silence achieves
    # NOT-READ and fails NAMED, so the naming is gated here.
    RESONANCE = ("a form with det < 0 is indefinite, of signature (1,1)")
    RESONANCE2 = ("The resonance is named here so that it is not read")
    resonance_named = (norm(ascii_fold(RESONANCE)).lower() in
                       paper_norm.lower()
                       and norm(ascii_fold(RESONANCE2)).lower()
                       in paper_norm.lower())
    if mut("MUT-WALL-COSMO"):
        resonance_named = True
    LD.gate("G-WALL-DIAGONAL",
            "THE DIAGONAL COUNTERPOINT IS MEASURED HERE -- THAT IS THIS "
            "UNIT'S POINT (verbatim anchor V10) -- AND COSMOLOGICAL READINGS "
            "STAY BARRED.  U4 found the division field's period and the "
            "vanishing diagonal link count jointly forced by one design "
            "choice; this census varies that choice and measures the two "
            "separately: the period direction ranges over all four order-3 "
            "subgroups and the diagonal link count is populated by the "
            "diagonal parallel class.  NO COSMOLOGICAL CLAIM PHRASE appears "
            "in the paper -- the bar is on the READING and not on the word, "
            "so the needles are claim phrases and the word 'cosmological' "
            "itself occurs in the paper, in the bar.  And the LORENTZIAN "
            "RESONANCE IS NAMED: a two-by-two symmetric form with det < 0 is "
            "indefinite, which in this corpus is a loaded observation, so the "
            "paper is required to say so and to say why the reading is not "
            "merely barred but ill-posed here -- 486 of the 747 "
            "non-degenerate groupings do not carry one sign across their own "
            "nine sites.  Naming is what keeps the inference governed; "
            "silence would leave the reader to supply it",
            not cosmo and (diag_measured or not paper_text)
            and (resonance_named or not paper_text),
            {"cosmological_claim_phrases": cosmo,
             "diagonal_measured": diag_measured,
             "resonance_named": resonance_named,
             "period_directions": bc_subs})
    R["walls"] = {"L1": "argued-first-and-declined", "BHS": "not-run",
                  "KR": "no-dimension-reading",
                  "diagonal": "measured-cosmology-barred"}
    SEAL.take("SEAL-WALLS", R)

    # -- SEC 10  THE VERDICT -------------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 10  THE VERDICT")
    say("=" * 78)
    bc_rate = Fraction(strat["BEYOND-COSET"]["crystalline"],
                       strat["BEYOND-COSET"]["schedules"])
    v_crystal = ("U4B-CRYSTAL-GENERIC-[beyond-coset %s; %d of %d; %s]"
                 % (bc_rate, strat["BEYOND-COSET"]["crystalline"],
                    strat["BEYOND-COSET"]["schedules"], "|".join(bc_subs)))
    v_det = ("DET-NONZERO-EXISTS-[%s: det=%s at 9 of 9; %d of %d pairs; "
             "POSDEF-EMPTY; I7-STRICT-EMPTY]"
             % (wname, wq[3], n_det9, n_pairs))
    v_con = ("CONSTRUCTIBILITY-[FORCED %d of %d; BRANCHING 0; REFUSED 0]"
             "@WINDOW-%d-OF-%d+%d-STRATUM-WITNESSES"
             % (census["FORCED"], len(WD), n_win, family, driven_wit))
    if mut("MUT-HEAD"):
        v_crystal = v_crystal.replace("GENERIC", "SEEDED")
    for s in (v_crystal, v_det, v_con):
        say("  " + s)
    R["verdict"] = {"crystal": v_crystal, "det": v_det,
                    "constructibility": v_con}
    R["counts"] = {
        "family": family, "window": n_win, "partitions": n_parts,
        "seed_pairs": len(stabpair), "uniform_weight": W,
        "crystalline": crystalline,
        "beyond_coset_crystalline": strat["BEYOND-COSET"]["crystalline"],
        "cu_joint_crystalline": strat["CU-JOINT"]["crystalline"],
        "cu_split_crystalline": strat["CU-SPLIT"]["crystalline"],
        "det9_pairs": n_det9, "det9_schedules": det9_scheds,
        "posdef_max": posdef_max, "strict_pos": strict_pos,
        "strata": len(want), "stratum_witnesses": driven_wit,
        "crystalline_window": n_cryst_win, "forced": census["FORCED"],
    }
    reg(*[v for v in R["counts"].values() if isinstance(v, int)])

    # the comparator reads the SERIALIZED receipt, so it shares no live
    # object with the builder either -- the write path's route, taken here
    ok_head = (reconstruct_from_serialized(
        json.dumps(R, indent=1, sort_keys=True, default=str))
        == (v_crystal, v_det, v_con))
    LD.gate("G-VERDICT-RECONSTRUCTED",
            "THE HEAD IS DERIVED A SECOND TIME BY A PATH THAT SHARES NEITHER "
            "CODE NOR INPUT NOR TYPED LITERAL WITH THE BUILDER.  The builder "
            "assembles the three verdict strings from live Python objects; "
            "the comparator is handed the receipt SERIALIZED TO JSON AND "
            "PARSED BACK -- the write path's own route, so not one live "
            "object crosses -- recomputes the beyond-coset rate as a Fraction "
            "from the two counts it finds there, re-sorts the subgroup list, "
            "and rebuilds all three strings from its own format templates.  "
            "The two agree character for character",
            ok_head, {"crystal": v_crystal, "det": v_det,
                      "constructibility": v_con})
    SEAL.take("SEAL-VERDICT-CRYSTAL", R)
    SEAL.take("SEAL-VERDICT-DET", R)
    SEAL.take("SEAL-VERDICT-CONSTR", R)
    SEAL.take("SEAL-COUNTS", R)

    # -- exactness -----------------------------------------------------------
    tree = ast.parse(src_text)
    floats = [n for n in ast.walk(tree)
              if isinstance(n, ast.Constant)
              and type(n.value).__name__ in ("float", "complex")]
    float_names = [n for n in ast.walk(tree)
                   if isinstance(n, ast.Name) and n.id in ("float", "complex")]

    def has_float(o):
        """the scanner names no builtin: it compares TYPE NAMES, so the AST
        scan above can require zero references to the name it is hunting."""
        if isinstance(o, dict):
            return any(has_float(k) or has_float(v) for k, v in o.items())
        if isinstance(o, (list, tuple)):
            return any(has_float(v) for v in o)
        return type(o).__name__ in ("float", "complex")
    LD.gate("G-EXACT",
            "THE ARITHMETIC IS EXACT END TO END.  An AST scan of this file "
            "finds %d float literals and %d references to `float`; a "
            "recursive type scan of the receipt about to be emitted finds no "
            "float anywhere.  Every quadratic form component and every "
            "determinant is a `fractions.Fraction`; every count is a Python "
            "integer" % (len(floats), len(float_names)),
            not floats and not float_names and not has_float(R),
            {"float_literals": len(floats), "float_refs": len(float_names),
             "receipt_floats": has_float(R)})

    # -- the CLI contract ----------------------------------------------------
    probes = []
    parser = parse_args_permissive if mut("MUT-CLI-PERMISSIVE") else parse_args
    for argv, want_reject in ((["--not-a-flag"], True), (["--mutant"], True),
                              (["--mutant", "NOPE"], True),
                              (["--break-anchor"], True),
                              (["--verify-paper", "/no/such/file.md"], True),
                              (["--verify-paper", "v14"], True),
                              (["--verify-paper", ""], True),
                              (["--mutant", "MUT-HEAD",
                                "--mutant", "MUT-HEAD"], True),
                              (["--break-anchor", "A-PIN",
                                "--break-anchor", "A-PIN"], True),
                              (["extra"], True), (["--no-write"], False),
                              (["--numbers"], False)):
        try:
            parser(argv)
            rejected = False
        except CliError:
            rejected = True
        probes.append({"argv": argv, "rejected": rejected,
                       "expected": want_reject})
    LD.gate("G-CLI-WHITELIST",
            "THE CLI IS ARGV-PARSED AGAINST A WHITELIST AND EXERCISED HERE "
            "(#82): unknown flags, unknown flag arguments, missing flag "
            "arguments and a --verify-paper path that does not exist are all "
            "rejected with exit 2, while the two documented no-op-free flags "
            "parse.  %d probes, all as declared.  The registered PERMISSIVE "
            "shape -- a runner that ignores what it does not recognise -- is "
            "present only as this gate's falsifier and is what "
            "MUT-CLI-PERMISSIVE substitutes" % len(probes),
            all(p["rejected"] == p["expected"] for p in probes),
            {"probes": probes})

    # -- SEC 11  THE PAPER GATES, IN RUN so that every VOUCHING row is sealed
    # -- inside the run and reachable by a declared mutant
    say("")
    say("=" * 78)
    say("SEC 11  THE PAPER GATES")
    say("=" * 78)
    cov = paper_coverage(R, mutate_paper(paper_text))
    R["paper_claims"] = [{"id": c, "text": t} for c, t in paper_claims(R)]
    LD.gate("G-PAPER-CLAIMS",
            "every one of the %d claims this instrument makes is rendered in "
            "the paper under test, whitespace-normalised, markdown-stripped "
            "and ASCII-folded on both sides (#125), and the claim rows "
            "themselves are published and sealed here" % cov["claims"],
            not cov["missing"], {"missing": cov["missing"] or "none",
                                 "claims": cov["claims"]})
    SEAL.take("SEAL-PAPER-CLAIMS", R)
    R["paper_coverage"] = cov
    LD.gate("G-PAPER-NUMERAL-COVERAGE",
            "every numeral occurring in the paper is either a number this run "
            "COMPUTED and registered, or one of the %d declared in-text "
            "residues; every hexadecimal token is one of the %d pinned source "
            "digests or the %d declared commits; %d distinct numerals over %d "
            "occurrences"
            % (len(DERIVED_IN_TEXT), len(SOURCES), len(DECLARED_COMMITS),
               cov["distinct_numerals"], cov["numeral_occurrences"]),
            not cov["uncovered"] and not cov["undeclared_hex"],
            {"uncovered": cov["uncovered"] or "none",
             "undeclared_hex": cov["undeclared_hex"] or "none"})
    SEAL.take("SEAL-PAPER-COVERAGE", R)
    R["paper_polarity"] = paper_polarity(R, paper_text,
                                         mut("MUT-PAPER-POLARITY"))
    LD.gate("G-PAPER-CLAIM-POLARITY",
            "every declared polarity of the head is present in the paper in "
            "its TRUE form and absent in its FALSE form: %d pairs.  These "
            "needles are HEAD TOKENS, not prose, so the #62 length floor does "
            "not apply to them and is not claimed; what makes them "
            "discriminating is that each false form is the emitted head's own "
            "opening -- `U4B-CRYSTAL-SEEDED-[` and not the bare branch name, "
            "so the paper may discuss the unfired branch by name without "
            "tripping its own gate, and MUT-PAPER-POLARITY injects a genuine "
            "SEEDED head into a copy of the paper rather than flipping a "
            "boolean" % len(R["paper_polarity"]),
            all(p["ok"] for p in R["paper_polarity"]),
            {"polarity": R["paper_polarity"]})
    SEAL.take("SEAL-PAPER-POLARITY", R)
    if mut("MUT-VOUCH-FORGED"):
        # INJ02's remaining three rows, forged after their gates
        R["paper_claims"] = [dict(c, text="INJECTED-FALSE-CLAIM")
                             for c in R["paper_claims"]]
        R["paper_coverage"] = dict(cov, missing=["INJECTED"])
        R["paper_polarity"] = [dict(p, ok=False) for p in R["paper_polarity"]]

    # -- THE COVERAGE LEDGER, over the DECLARED gate universe ---------------
    emitted = [r["gate"] for r in LD.rows]
    universe = sorted(set(emitted) | set(LATE_GATES) | set(POST_RUN_GATES))
    ledger_src = emitted[:-1] if mut("MUT-GATE-UNIVERSE") else emitted
    R["waiver_ledger"] = waiver_ledger(ledger_src)
    ledger_gates = sorted({w["gate"] for w in R["waiver_ledger"]})
    LD.gate("G-GATE-UNIVERSE",
            "THE COVERAGE LEDGER'S DENOMINATOR IS HONEST (#34).  The gate "
            "universe is every gate name this run EMITTED, plus the %d gates "
            "still to come in this run's own tail, plus the %d evaluated only "
            "in the mutant, self-test and writing paths -- %d distinct names "
            "in all.  The ledger below is built over exactly that set and "
            "this gate requires the two to be equal, so a gate cannot be "
            "counted by the instrument and missed by its own coverage row.  "
            "Two miscounts that happened to agree are what this closes: a "
            "total that omitted the self-test gate, and a ledger that omitted "
            "the gate making the honesty claim"
            % (len(LATE_GATES), len(POST_RUN_GATES), len(universe)),
            ledger_gates == universe,
            {"universe": len(universe), "ledger_rows": len(ledger_gates),
             "emitted_so_far": len(set(emitted)),
             "missing_from_ledger": sorted(set(universe) - set(ledger_gates))
             or "none",
             "extra_in_ledger": sorted(set(ledger_gates) - set(universe))
             or "none"})
    LD.gate("G-WAIVERS-VERIFIED",
            "THE COVERAGE LEDGER IS HONEST (#34).  Every gate this "
            "instrument declares -- the ones evaluated here and the ones "
            "evaluated only in the paper, mutant, self-test and writing "
            "paths -- is classified FALSIFIABLE, meaning a declared mutant "
            "or a declared control drives it to FAIL, or WAIVED WITH A "
            "FORCING that says "
            "why it cannot fail and what would have to change for it to.  "
            "%d gates: %d falsifiable, %d waived-with-forcing, 0 unaccounted.  "
            "The FALSIFIABLE rows are checked for REACHABILITY after the "
            "mutant sweep, at G-FALSIFIER-REACHABILITY: a falsifier that dies "
            "at some other gate is not this gate's falsifier"
            % (len(R["waiver_ledger"]),
               sum(1 for w in R["waiver_ledger"] if w["status"] == "FALSIFIABLE"),
               sum(1 for w in R["waiver_ledger"] if w["status"] == "WAIVED")),
            all(w["status"] in ("FALSIFIABLE", "WAIVED")
                for w in R["waiver_ledger"])
            and all(w["reason"] for w in R["waiver_ledger"]),
            {"gates": len(R["waiver_ledger"]),
             "falsifiable": sum(1 for w in R["waiver_ledger"]
                                if w["status"] == "FALSIFIABLE"),
             "waived": sum(1 for w in R["waiver_ledger"]
                           if w["status"] == "WAIVED"),
             "unaccounted": [w["gate"] for w in R["waiver_ledger"]
                             if w["status"] == "UNACCOUNTED"] or "none"})
    SEAL.take("SEAL-WAIVERS", R)

    # -- the totals close IN RUN, at their own gate -------------------------
    R["totals"] = {
        "gates": len(universe),
        "gates_in_receipt": len(universe) - len(NOT_IN_RECEIPT),
        "sources": len(SOURCES), "verbatim_anchors": len(VERBATIM),
        "anchors": len(anchors), "mutants": len(MUTANTS),
        "seals_declared": len(SEALED_PATHS),
        "unsealed_declared": len(UNSEALED_DECLARED),
        "records_driven": len(DRIVEN_RECORDS),
        "window_builds": len(BUILD_CACHE) + len(ANCHOR_CACHE),
    }
    LD.gate("G-TOTALS",
            "THE INSTRUMENT'S OWN TOTALS CLOSE HERE, AT THEIR OWN GATE, and "
            "are sealed here -- not at the last gate of the run, where "
            "anything moved into them between the last measurement and the "
            "take would be sealed in and published with a digest certifying "
            "the lie.  %d gates in the universe, %d of them reaching the "
            "receipt; %d hash-pinned sources; %d verbatim anchors; %d read "
            "anchors; %d declared mutants; %d declared seals and %d declared "
            "unsealed rows; %d records driven through the layer's own menus, "
            "%d of them distinct and cached.  The counts that can only be "
            "known after the mutant sweep are NOT stored here: they are "
            "DERIVED at close from the sealed rows themselves"
            % (len(universe), len(universe) - len(NOT_IN_RECEIPT),
               len(SOURCES),
               len(VERBATIM), len(anchors), len(MUTANTS), len(SEALED_PATHS),
               len(UNSEALED_DECLARED), len(DRIVEN_RECORDS),
               len(BUILD_CACHE) + len(ANCHOR_CACHE)),
            R["totals"]["gates"] == len(universe)
            and R["totals"]["mutants"] == len(MUTANTS),
            {"totals": R["totals"]})
    SEAL.take("SEAL-TOTALS", R)
    if mut("MUT-TOTALS-FORGED"):
        # INJ03, as the instrument review ran it
        R["totals"] = dict(R["totals"], gates=999, mutants=99)

    # -- the transcript is a published artifact and is CHAINED --------------
    if mut("MUT-TRANSCRIPT-HEAD"):
        # INJ06, as the instrument review ran it: the head flipped in the
        # transcript's own line buffer.  It left the receipt byte-identical.
        for k, s in enumerate(LINES):
            LINES[k] = s.replace("U4B-CRYSTAL-GENERIC", "U4B-CRYSTAL-SEEDED")
    chain_ok = transcript_chain_of(LINES) == TRANSCRIPT_CHAIN[0]
    heads_present = all(v in "\n".join(LINES)
                        for v in (v_crystal, v_det, v_con))
    LD.gate("G-TRANSCRIPT-BOUND",
            "THE TRANSCRIPT IS A PUBLISHED ARTIFACT AND IS BOUND TO WHAT WAS "
            "ACTUALLY SAID.  Every line extends a rolling digest as it is "
            "emitted, and the chain recomputed from the %d lines standing now "
            "equals the digest accumulated while they were written; the three "
            "sealed verdict strings are present in it verbatim.  Two "
            "artifacts stating opposite verdicts with the receipt "
            "byte-identical is what this closes: the receipt's sha256 could "
            "not see a transcript edited after the fact, and now the "
            "transcript's own chain can"
            % len(LINES),
            chain_ok and heads_present,
            {"lines": len(LINES), "chain_intact": chain_ok,
             "verdicts_present": heads_present,
             "chain": TRANSCRIPT_CHAIN[0]})

    # -- the completeness gate, against the DECLARATION ---------------------
    if mut("MUT-SEAL-DROPPED"):
        # INJ07, as the instrument review ran it: a declared seal deleted.
        # It left BOTH artifacts byte-identical to the honest run.
        SEAL.drop("SEAL-WAIVERS")
    if mut("MUT-SEAL-BROKEN"):
        R["counts"]["family"] = family + 1
    broken = SEAL.verify(R, only=SEALS_IN_RUN)
    LD.gate("G-SEAL-COMPLETE",
            "EVERY PUBLISHED OBJECT WAS DIGESTED AT THE MOMENT ITS GATE "
            "PASSED (#119), EVERY ONE OF THE %d DECLARED IN-RUN SEALS WAS "
            "ACTUALLY TAKEN, AND EVERY ONE STILL VERIFIES HERE.  The "
            "comparison is against the DECLARATION and not against the "
            "manifest's own contents: a declared seal that was never taken "
            "counts as BROKEN, not as absent, so a seal cannot be dropped "
            "without trace.  The vouching layer is inside this count -- "
            "provenance, the paper claim rows, the paper coverage row, the "
            "paper polarity rows -- because the rows a reader cannot "
            "recompute are exactly the rows a seal is for.  The artifacts "
            "below are written FROM the sealed payload, and the terminal "
            "integrity gate compares the bytes on disk against these digests, "
            "never against a re-derivation"
            % len(SEALS_IN_RUN),
            not broken and len(SEAL.rows) == len(SEALS_IN_RUN),
            {"taken": len(SEAL.rows), "declared_in_run": len(SEALS_IN_RUN),
             "broken": broken or "none"})
    return LD, R, SEAL, paper_norm


# ===========================================================================
# SECTION 7.  THE INDEPENDENT COMPARATOR, THE WAIVER LEDGER, THE PAPER GATES
# ===========================================================================

def reconstruct(receipt):
    """THE COMPARATOR (#82).  Input: the receipt's own census rows.  It shares
    no code path, no live object and no typed literal with the builder -- it
    re-derives the rate from the two counts it finds, re-sorts the subgroup
    list from the affine block, and re-assembles all three strings."""
    cls = receipt["affine"]["classes"]
    bc = cls["BEYOND-COSET"]
    rate = Fraction(int(bc["crystalline"]), int(bc["schedules"]))
    subs = sorted(set(receipt["affine"]["beyond_coset_subgroups"]))
    head = "".join([
        "U4B-CRYSTAL-", "GENERIC" if int(bc["crystalline"]) else "SEEDED",
        "-[beyond-coset ", str(rate), "; ", str(int(bc["crystalline"])),
        " of ", str(int(bc["schedules"])), "; ", "|".join(subs), "]"])
    d = receipt["determinant"]
    det = "".join([
        "DET-NONZERO-", "EXISTS" if int(d["nonzero_at_all_sites_pairs"])
        else "EMPTY",
        "-[", d["witness"]["name"], ": det=", d["witness"]["det"],
        " at 9 of 9; ", str(int(d["nonzero_at_all_sites_pairs"])), " of ",
        str(int(d["partition_pairs"])), " pairs; ",
        "POSDEF-EMPTY" if int(d["max_posdef_sites"]) < 9 else "POSDEF-EXISTS",
        "; ",
        "I7-STRICT-EMPTY" if int(d["strictly_positive_pairs"]) == 0
        else "I7-STRICT-EXISTS", "]"])
    c = receipt["constructibility"]
    f = receipt["family"]
    con = "".join([
        "CONSTRUCTIBILITY-[FORCED ", str(int(c["fates"].get("FORCED", 0))),
        " of ", str(int(c["window"])), "; BRANCHING ",
        str(int(c["fates"].get("BRANCHING", 0))), "; REFUSED ",
        str(int(c["fates"].get("REFUSED", 0))), "]@WINDOW-",
        str(int(f["window"])), "-OF-", str(int(f["family"])), "+",
        str(int(receipt["counts"]["stratum_witnesses"])),
        "-STRATUM-WITNESSES"])
    return head, det, con


def reconstruct_from_serialized(text):
    return reconstruct(json.loads(text))


# the gates still to come inside `full_run` at the moment the coverage
# ledger is built, and the gates evaluated only after it returns
LATE_GATES = ("G-GATE-UNIVERSE", "G-WAIVERS-VERIFIED", "G-TOTALS",
              "G-TRANSCRIPT-BOUND", "G-SEAL-COMPLETE")
POST_RUN_GATES = ("G-MUTANTS-ON-TARGET", "G-FALSIFIER-REACHABILITY",
                  "G-PAPER-COVERAGE-FINAL", "G-CLOSURE-DERIVED",
                  "G-SEAL-CLOSE", "G-ARTIFACT-INTEGRITY",
                  "G-SELFTEST-WRITES-NOTHING")
# the two gates that are evaluated outside the ledger and so never appear
# as receipt rows
NOT_IN_RECEIPT = ("G-ARTIFACT-INTEGRITY", "G-SELFTEST-WRITES-NOTHING",
                  "G-SEAL-CLOSE")

WAIVERS = {
    "G-MUTANTS-ON-TARGET": ("WAIVED", "the sweep's own closure gate: it "
                            "fails when a declared mutant survives or dies "
                            "off target, which is a fact about the OTHER "
                            "gates, so it has no falsifier of its own"),
    "G-PAPER-COVERAGE-FINAL": ("WAIVED", "the same three checks re-run once "
                               "the totals close; its in-run twins "
                               "G-PAPER-CLAIMS and G-PAPER-NUMERAL-COVERAGE "
                               "carry the injection falsifiers, and this "
                               "evaluation is the enforcement"),
    "G-ARTIFACT-INTEGRITY": ("WAIVED", "evaluated only in the writing path, "
                             "which no mutant run reaches; its negative "
                             "control fires on EVERY delivery run -- a "
                             "deliberately corrupted payload is written to a "
                             "probe path and the comparator must notice "
                             "before either artifact is moved into place"),
    "G-PROV-ALL": ("WAIVED", "an aggregate over per-source gates that each "
                   "carry MUT-ANCHOR's falsifier via --break-anchor; it "
                   "cannot fail once they pass, and --break-anchor NAME "
                   "drives it"),
    "G-SLICE-EXIT-FREE": ("WAIVED", "would fail if a committed v10 layer "
                          "gained an exit call; nothing in this unit can "
                          "make it fail, and the forcing is that the "
                          "sources are hash-pinned -- so --break-anchor "
                          "A-D42B1 is the live falsifier of the same read"),
    "G-GRAMMAR-LIVE": ("WAIVED", "a two-directional behavioural probe of a "
                       "hash-pinned committed function; it fails if that "
                       "function changes, which the provenance gate "
                       "forbids first"),
    "G-EXACT": ("WAIVED", "would fail on any float entering this file or "
                "the receipt; no mutant introduces one because a mutant "
                "that did would be testing Python, not this census -- the "
                "forcing is the AST scan, which is evaluated fresh on the "
                "file's own bytes at every run"),
    "G-WAIVERS-VERIFIED": ("WAIVED", "the ledger's own closure gate; it "
                           "fails if any gate is unclassified, which is a "
                           "construction error rather than a measurement"),
    "G-TOTALS": ("WAIVED", "the totals' own closing gate: it recomputes the "
                 "universe it is comparing against, so it cannot disagree "
                 "with itself.  Its forcing is that the numbers it publishes "
                 "are re-derived from the SEALED rows at close by "
                 "G-CLOSURE-DERIVED, and a forged totals row dies at "
                 "G-SEAL-COMPLETE -- MUT-TOTALS-FORGED is that falsifier"),
    "G-CLOSURE-DERIVED": ("WAIVED", "evaluated after the mutant sweep, which "
                          "no in-process mutant reaches.  Its forcing is that "
                          "it READS NOTHING: every number it checks is "
                          "recomputed at close from the chained gate ledger "
                          "and the sealed mutant report, so it can disagree "
                          "only if one of those was forged -- and "
                          "MUT-TOTALS-FORGED and MUT-SEAL-BROKEN kill that "
                          "at G-SEAL-COMPLETE"),
    "G-SEAL-CLOSE": ("WAIVED", "the seal's own closing gate, evaluated on the "
                     "payload about to be serialized and so only in the "
                     "writing path.  Its forcing is the same as the integrity "
                     "gate's: it fires on EVERY delivery run, and its three "
                     "clauses -- every declared seal taken, every taken seal "
                     "verifying, every published key sealed or declared -- "
                     "are each driven to FAIL in-run by MUT-SEAL-DROPPED, "
                     "MUT-SEAL-BROKEN and MUT-VOUCH-FORGED at "
                     "G-SEAL-COMPLETE"),
    "G-FALSIFIER-REACHABILITY": ("WAIVED", "the sweep's reachability closure: "
                                 "it fails when a FALSIFIABLE row's named "
                                 "mutant dies at a gate other than that row's "
                                 "own, which is a fact about the OTHER gates' "
                                 "boundaries, so it has no falsifier of its "
                                 "own -- the same standing as "
                                 "G-MUTANTS-ON-TARGET"),
}


def waiver_ledger(emitted):
    out = []
    targets = {m[1] for m in MUTANTS}
    for g in list(emitted) + list(LATE_GATES) + list(POST_RUN_GATES):
        if g in [r["gate"] for r in out]:
            continue
        if g in WAIVERS:
            status, reason = WAIVERS[g]
        elif g in targets:
            status = "FALSIFIABLE"
            reason = "driven to FAIL by %s" % ", ".join(
                sorted(m[0] for m in MUTANTS if m[1] == g))
        elif g.startswith("G-PROV["):
            status = "FALSIFIABLE"
            reason = "driven to FAIL by --break-anchor %s" % g[7:-1]
        else:
            status = "UNACCOUNTED"
            reason = ""
        out.append({"gate": g, "status": status, "reason": reason})
    return out


def paper_claims(R):
    c = R["counts"]
    d = R["determinant"]
    a = R["affine"]["classes"]
    return [
        ("C01", R["verdict"]["crystal"]),
        ("C02", R["verdict"]["det"]),
        ("C03", R["verdict"]["constructibility"]),
        ("C04", "the family has %d schedules" % c["family"]),
        ("C05", "the declared window has %d schedules" % c["window"]),
        ("C06", "%d of %d schedules are crystalline"
         % (c["crystalline"], c["family"])),
        ("C07", "every one of the %d CU-JOINT seed pairs is crystalline"
         % 36),
        ("C08", "none of the %d CU-SPLIT seed pairs is crystalline" % 108),
        ("C09", "%d of the %d beyond-coset schedules are crystalline"
         % (a["BEYOND-COSET"]["crystalline"], a["BEYOND-COSET"]["schedules"])),
        ("C10", "%d of the %d partition pairs carry det != 0 at all nine "
         "sites" % (d["nonzero_at_all_sites_pairs"], d["partition_pairs"])),
        ("C11", "the maximum number of positive-definite sites is %d"
         % d["max_posdef_sites"]),
        ("C12", "no partition pair makes all 27 link counts strictly "
         "positive"),
        ("C13", "the footprint field is the constant 2 at every site of "
         "every schedule"),
        ("C14", "all %d admissible single-arbitration re-seatings break the "
         "stabilizer" % 12),
        ("C15", "the named witness is %s" % d["witness"]["name"]),
        # the heads as the adjudication recomposed them
        ("C16", "at %d of %d crystalline seed pairs the field is supported on "
         "a union of cosets of its own period"
         % (R["carrier"]["support_is_a_coset_union"],
            R["carrier"]["crystalline_seed_pairs"])),
        ("C17", "six sevenths of all crystallinity in the family lies outside "
         "the inherited locus"),
        ("C18", "at all %d single-point re-seatings of one seed of a "
         "crystalline pair, the edited field's stabilizer is trivial"
         % R["fragility"]["family_scope_cases"]),
        ("C19", "the same count permits as many as %d positive-definite "
         "sites; the measured maximum is %d"
         % (d["wall_permits_posdef_sites"], d["max_posdef_sites"])),
        ("C20", "%d of the %d partition pairs carry at least one "
         "positive-definite site"
         % (d["pairs_with_a_posdef_site"], d["partition_pairs"])),
        ("C21", "the maximum total link-incidence over the whole family is "
         "exactly %d, attained at %d partition pairs"
         % (d["max_link_incidence_per_pair"],
            d["pairs_attaining_the_budget"])),
        ("C22", "the period is the diagonal at %s of them, against %s under "
         "independence"
         % (R["period_vs_diagonal"]["conditional"],
            R["period_vs_diagonal"]["under_independence"])),
        ("C23", "neither seed set is a coset of any order-3 subgroup"),
        ("C24", "no partition pair is positive definite at every site"),
    ]


# the polarity needles are HEAD TOKENS, not prose: the #62 length floor is a
# floor on VERBATIM SOURCE ANCHORS and is not claimed for them.  Each false
# form is the emitted head's own opening -- with its bracket -- so the paper
# may name the branch that did not fire without tripping its own gate.
PAPER_POLARITY = [
    ("P1", "U4B-CRYSTAL-GENERIC-[", "U4B-CRYSTAL-SEEDED-["),
    ("P2", "DET-NONZERO-EXISTS-[", "DET-NONZERO-EMPTY-["),
    ("P3", "POSDEF-EMPTY", "POSDEF-EXISTS"),
    ("P4", "I7-STRICT-EMPTY", "I7-STRICT-EXISTS"),
]

DERIVED_IN_TEXT = {
    "0": "the zero of a link count, a determinant and a refusal count",
    "1": "section numbers, the trivial subgroup, the unit link count",
    "2": "section numbers, the two rounds, the constant footprint value",
    "3": "section numbers, the three groups per round, the three proposers, "
         "Z_3^2's exponent",
    "4": "section numbers, the four parallel classes, the four order-3 "
         "subgroups",
    "5": "section numbers", "6": "section numbers, the six division events",
    "7": "section numbers", "8": "section numbers", "9": "the nine sites",
    "10": "section numbers", "11": "section numbers",
    "14": "the corpus's v14 label", "13": "the corpus's v13 label",
    "17": "this paper's number",
    "42": "the layer name `d42b1`", "60": "the layer name `d60`",
    "256": "the hash width in `sha256-12`",
    "119": "the RUNBOOK engraving numbers", "125": "the RUNBOOK engraving",
    "148": "the RUNBOOK engraving: the seal-totality addendum",
    "82": "the RUNBOOK engraving", "87": "the RUNBOOK engraving",
    "91": "the RUNBOOK engraving", "62": "the RUNBOOK engraving",
    "34": "the RUNBOOK engraving", "24": "the RUNBOOK engraving",
    "15": "the RUNBOOK section",
    "126": "this unit's ledger number",
    "3.2": "HA's section number", "2.1": "paper-13's section number",
    "2.2": "a subsection number of this paper",
    "2.3": "a subsection number of this paper",
    "2.4": "a subsection number of this paper",
    "4.1": "a subsection number of this paper",
    "4.2": "a subsection number of this paper",
    "5.1": "a subsection number of this paper",
    "5.2": "a subsection number of this paper",
    "5.3": "a subsection number of this paper",
    "2026": "the year", "12": "the edit count",
    "00": "the actor name G00 (the site (0,0))",
    "11": "a component index of the induced form (q11)",
    "22": "a component index of the induced form (q22)",
    "16": "the class pairs", "27": "the I7 cells and the seed assignments",
    "18": "the link-incidence budget", "36": "the CU-JOINT pairs",
    "108": "the CU-SPLIT pairs", "84": "the 3-subsets of Z_3^2",
    "280": "the partitions", "90": "the uniform weight",
    "729": "the seed pairs per partition pair", "747": "the det9 pairs",
    "7056": "the seed pairs", "6912": "the beyond-coset pairs",
}


HEXTOKEN = re.compile(r"\b(?=[0-9a-f]{7,64}\b)(?=[0-9a-f]*[a-f])[0-9a-f]+\b")
DECLARED_COMMITS = {
    "06b89fe": "the commit at which the U4 delivery artifacts are frozen and "
               "readable, cited and NOT read (a repair worker holds them "
               "under rewrite)",
    "58195da": "the commit at which weld 2's SEC 6 rebuild is readable, cited "
               "and NOT read",
    "42417f6": "the commit that froze this unit's pin",
}


def paper_coverage(R, paper_text):
    claims = paper_claims(R)
    hay = norm(ascii_fold(paper_text))
    missing = [cid for cid, txt in claims
               if norm(ascii_fold(txt)) not in hay]
    folded = ascii_fold(paper_text)
    hexes = set(HEXTOKEN.findall(folded))
    declared_hex = {s[2] for s in SOURCES} | set(DECLARED_COMMITS)
    undeclared_hex = sorted(hexes - declared_hex)
    nums = re.findall(r"[0-9]+(?:[.,/][0-9]+)*", HEXTOKEN.sub(" ", folded))

    def covered(n):
        """a numeral is covered if this run registered it, if it is a
        declared in-text residue, if it is the same number with thousands
        separators, or -- for a comma-joined coordinate such as `(1,0)` --
        if every comma-separated part is itself covered."""
        if n in NUMREG or n in DERIVED_IN_TEXT or n.replace(",", "") in NUMREG:
            return True
        parts = n.split(",")
        return (len(parts) > 1
                and all(q in NUMREG or q in DERIVED_IN_TEXT for q in parts))
    uncovered = sorted({n for n in nums if not covered(n)})
    declared_absent = sorted({k for k in DERIVED_IN_TEXT
                              if k not in nums and k not in NUMREG})
    return {"claims": len(claims), "missing": missing,
            "uncovered": uncovered,
            "residue_declared_but_absent": declared_absent,
            "hex_tokens": sorted(hexes),
            "undeclared_hex": undeclared_hex,
            "distinct_numerals": len(set(nums)),
            "numeral_occurrences": len(nums)}


def mutate_paper(text):
    """the paper-side injections: a dropped claim, an unregistered numeral,
    and a genuine SEEDED head.  They act on a COPY of the object under test,
    never on disk."""
    if mut("MUT-PAPER-CLAIM"):
        return text.replace("crystalline", "crystallime")
    if mut("MUT-PAPER-NUMERAL"):
        return text + "\n\nAn unregistered number: 31337.\n"
    if mut("MUT-PAPER-POLARITY"):
        return text + (
            "\n```\nU4B-CRYSTAL-SEEDED-[the inherited locus]\n```\n")
    return text


def paper_polarity(R, paper_text, mutated=False):
    """the mutant injects TEXT -- a real SEEDED head in a copy of the paper --
    rather than flipping this function's own booleans."""
    hay = norm(ascii_fold(mutate_paper(paper_text) if mutated
                          else paper_text))
    rows = []
    for pid, true_s, false_s in PAPER_POLARITY:
        t = norm(ascii_fold(true_s)) in hay
        f = norm(ascii_fold(false_s)) in hay
        rows.append({"id": pid, "true_present": t, "false_present": f,
                     "ok": t and not f})
    return rows


# ===========================================================================
# SECTION 8.  THE CLI
# ===========================================================================

def parse_args(argv):
    opts = {"write": True, "mutant": None, "break_anchor": None,
            "verify_paper": None, "selftest": False, "numbers": False}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--no-write":
            opts["write"] = False
        elif a == "--numbers":
            opts["numbers"] = True
            opts["write"] = False
        elif a == "--selftest":
            opts["selftest"] = True
            opts["write"] = bool(mut("MUT-SELFTEST-WRITES"))
        elif a == "--mutant":
            if opts["mutant"] is not None:
                raise CliError("--mutant given more than once")
            if i + 1 >= len(argv):
                raise CliError("--mutant requires a mutant NAME")
            if argv[i + 1] not in MUTANT_NAMES:
                raise CliError("unknown mutant %r" % argv[i + 1])
            opts["mutant"] = argv[i + 1]
            opts["write"] = False
            i += 1
        elif a == "--break-anchor":
            if opts["break_anchor"] is not None:
                raise CliError("--break-anchor given more than once")
            if i + 1 >= len(argv):
                raise CliError("--break-anchor requires an anchor NAME")
            if argv[i + 1] not in SOURCE_IDS:
                raise CliError("unknown anchor %r" % argv[i + 1])
            opts["break_anchor"] = argv[i + 1]
            opts["write"] = False
            i += 1
        elif a == "--verify-paper":
            if opts["verify_paper"] is not None:
                raise CliError("--verify-paper given more than once")
            opts["verify_paper"] = PAPER_REL
            if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
                opts["verify_paper"] = argv[i + 1]
                i += 1
            p = opts["verify_paper"]
            # isfile, not exists: a DIRECTORY and the EMPTY STRING are not
            # papers, and accepting them turned an operator error into an
            # uncaught traceback indistinguishable from "the paper drifted"
            if not os.path.isfile(p if os.path.isabs(p)
                                  else os.path.join(REPO, p)):
                raise CliError("no such paper file %r" % p)
            opts["write"] = False
        else:
            raise CliError("unknown argument %r" % a)
        i += 1
    return opts


def parse_args_permissive(argv):
    """THE FORBIDDEN SHAPE (#82, four named recurrences): a runner that
    ignores what it does not recognise.  Present only as G-CLI-WHITELIST's
    falsifier; nothing in the delivery path calls it."""
    return {"write": True, "mutant": None, "break_anchor": None,
            "verify_paper": None, "selftest": False, "numbers": False}


def selftest_result():
    """MEASURED, never typed: corrupt one anchor, run, and observe both
    whether the run died and whether anything on disk moved."""
    global QUIET
    was, saved_lines = QUIET, transcript_state()
    QUIET = True
    watched = (OUT_TXT, OUT_JSON, OUT_TXT + ".selftest-probe")

    def snap():
        return {p: (os.path.exists(p),
                    os.path.getmtime(p) if os.path.exists(p) else None,
                    os.path.getsize(p) if os.path.exists(p) else None)
                for p in watched}
    before = snap()
    died = False
    try:
        full_run("A-D42B1", "", PAPER_REL)
    except (GateFail, SystemExit):
        died = True
    if mut("MUT-SELFTEST-WRITES"):
        # THE INJECTION: the self-test path is allowed to reach a writer.
        with open(watched[2], "w", encoding="utf-8") as fh:
            fh.write("a writer was reached\n")
    wrote = (before != snap())
    if os.path.exists(watched[2]):
        os.remove(watched[2])
    transcript_restore(saved_lines)
    QUIET = was
    return died, wrote


def selftest():
    """#82: corrupt one anchor, confirm exit 1, write nothing."""
    died, wrote = selftest_result()
    print("SELFTEST: corrupted anchor A-D42B1 -> run died = %s; wrote "
          "anything = %s" % (died, wrote))
    if not died:
        print("SELFTEST FAILED: the corrupted run did not die", file=sys.stderr)
        sys.exit(2)
    if wrote:
        print("GATE FAILED: G-SELFTEST-WRITES-NOTHING :: the self-test path "
              "reached a writer", file=sys.stderr)
        sys.exit(2)
    print("G-SELFTEST-WRITES-NOTHING: the corrupted run died at the anchor "
          "gate and wrote nothing.")
    sys.exit(1)


def emit_report(R, SEAL):
    say("")
    say("=" * 78)
    say("RECEIPT")
    say("=" * 78)
    say("  gates      : %d evaluated, all passed" % R["totals"]["gates"])
    say("  sources    : %d hash-pinned; verbatim anchors %d; read anchors %d"
        % (R["totals"]["sources"], R["totals"]["verbatim_anchors"],
           R["totals"]["anchors"]))
    say("  mutants    : %d declared, %d killed, %d on target"
        % (R["totals"]["mutants"], R["closure"]["mutants_killed"],
           R["closure"]["mutants_on_target"]))
    say("  menu drives: %d distinct records built by the layer's own menu, "
        "%d drives in all"
        % (R["totals"]["window_builds"], R["totals"]["records_driven"]))
    say("  seals      : %d objects sealed at gate time, %d rows declared "
        "unsealed" % (len(SEAL.rows), len(UNSEALED_DECLARED)))
    for row in SEAL.rows:
        say("    %-24s %-40s %s" % (row["seal"], row["path"],
                                    row["sha256_12"]))
    for key, _reason, bound in UNSEALED_DECLARED:
        say("    %-24s %-40s DECLARED UNSEALED, bound by %s"
            % ("(unsealed)", key, bound))
    text = "\n".join(LINES) + "\n"
    if transcript_chain_of(LINES) != TRANSCRIPT_CHAIN[0]:
        raise GateFail("G-TRANSCRIPT-BOUND :: the transcript standing at "
                       "close is not the transcript that was written")
    SEAL.close_transcript(text)


def main():
    global MUT, QUIET
    try:
        opts = parse_args(sys.argv[1:])
    except CliError as e:
        print("usage: %s [--no-write] [--numbers] [--selftest] "
              "[--mutant NAME] [--break-anchor NAME] [--verify-paper [PATH]]"
              % os.path.basename(SELF), file=sys.stderr)
        print("error: %s" % e, file=sys.stderr)
        sys.exit(2)
    # THE MUTANT IS SET BEFORE THE SELF-TEST IS DISPATCHED, so that
    # `--selftest --mutant MUT-SELFTEST-WRITES` is honoured rather than inert:
    # no flag is a no-op and no combination silently is either
    MUT = opts["mutant"]
    if opts["selftest"]:
        selftest()
    write = opts["write"]

    say("=" * 78)
    say("v14 U4b -- THE SCHEDULE CENSUS (paper-17)")
    say("=" * 78)
    if MUT:
        say("MUTANT ACTIVE: %s" % MUT)
    if opts["break_anchor"]:
        say("ANCHOR BREAK SELF-TEST: %s" % opts["break_anchor"])

    paper_rel = opts["verify_paper"] or PAPER_REL
    paper_path = (paper_rel if os.path.isabs(paper_rel)
                  else os.path.join(REPO, paper_rel))
    paper_text = read_text(paper_path) if os.path.exists(paper_path) else ""
    if opts["verify_paper"]:
        say("VERIFY-PAPER: the object under test is %s" % paper_rel)

    try:
        LD, R, SEAL, _pn = full_run(opts["break_anchor"], paper_text, paper_rel)
    except GateFail as e:
        say("")
        say("GATE FAILED: %s" % e)
        say("EXIT 1")
        sys.exit(1)

    if opts["numbers"]:
        say("")
        say("THE CLAIMS THIS INSTRUMENT MAKES (each must be rendered in the "
            "paper)")
        for cid, txt in paper_claims(R):
            say("  %s  %s" % (cid, txt))
        say("")
        say("THE REGISTERED NUMERALS (%d)" % len(NUMREG))
        say("  " + " ".join(sorted(NUMREG)))
        say("")
        say("--numbers: the census and the paper gates are above; no mutant "
            "sweep, no seal close, nothing written.")
        sys.exit(0)

    if opts["verify_paper"]:
        say("")
        say("VERIFY-PAPER: %s -- every claim rendered, every numeral covered, "
            "every polarity held." % paper_rel)
        say("EXIT 0")
        sys.exit(0)
    if MUT or opts["break_anchor"]:
        say("")
        say("MUTANT SURVIVED: %s" % (MUT or opts["break_anchor"]))
        say("EXIT 0")
        sys.exit(0)

    # -- the mutant sweep ----------------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 12  THE DECLARED MUTANTS, RUN IN PROCESS")
    say("=" * 78)
    report, all_dead, on_target = [], True, 0
    clean_numreg = set(NUMREG)
    for nm, target, note in MUTANTS:
        MUT = nm
        QUIET = True
        saved = transcript_state()
        killed_at = None
        try:
            if nm == "MUT-SELFTEST-WRITES":
                died, wrote = selftest_result()
                killed_at = ("G-SELFTEST-WRITES-NOTHING" if wrote else None)
            else:
                full_run(None, paper_text, paper_rel)
        except GateFail as e:
            killed_at = str(e).split(" ::")[0]
        except SystemExit:
            killed_at = "SYSTEM-EXIT"
        transcript_restore(saved)
        QUIET = False
        MUT = None
        report.append({"mutant": nm, "target": target, "note": note,
                       "killed": killed_at is not None, "killed_at": killed_at,
                       "on_target": killed_at == target})
        if killed_at is None:
            all_dead = False
        if killed_at == target:
            on_target += 1
        say("  %-24s -> %s" % (nm, killed_at or "SURVIVED"))
    NUMREG.clear()
    NUMREG.update(clean_numreg)
    R["mutants"] = report
    off = [(m["mutant"], m["target"], m["killed_at"]) for m in report
           if not m["on_target"]]
    try:
        LD.gate("G-MUTANTS-ON-TARGET",
                "every one of the %d declared mutants is killed, and killed "
                "by the gate it was declared to falsify: a mutant that dies "
                "elsewhere is a gate boundary this unit does not understand"
                % len(MUTANTS),
                all_dead and on_target == len(MUTANTS),
                {"killed": sum(1 for m in report if m["killed"]),
                 "on_target": on_target, "off_target": off or "none"})
    except GateFail as e:
        say("")
        say("GATE FAILED: %s" % e)
        say("EXIT 1")
        sys.exit(1)
    SEAL.take("SEAL-MUTANTS", R)

    try:
        # #34 WITH REACHABILITY: a FALSIFIABLE row's named mutant must die at
        # THAT ROW'S OWN GATE.  A mutant credited with driving a gate it
        # never reaches -- because an earlier gate kills it first, or because
        # it passes the gate it is credited with -- is not a falsifier.
        credited = {}
        for w in R["waiver_ledger"]:
            if w["status"] != "FALSIFIABLE":
                continue
            credited[w["gate"]] = [m[0] for m in MUTANTS if m[1] == w["gate"]]
        killed_where = {m["mutant"]: m["killed_at"] for m in report}
        unreachable = sorted(
            (g, nm, killed_where.get(nm))
            for g, names in credited.items() for nm in names
            if killed_where.get(nm) != g)
        uncredited = sorted(g for g, names in credited.items()
                            if not names and not g.startswith("G-PROV["))
        LD.gate("G-FALSIFIER-REACHABILITY",
                "EVERY FALSIFIABLE ROW'S NAMED FALSIFIER REACHES THE GATE IT "
                "IS CREDITED WITH.  %d gates in the coverage ledger are "
                "classified FALSIFIABLE on a declared mutant, and for each "
                "the mutant's measured `killed_at` is required to equal that "
                "row's own gate -- not merely to be non-null.  Two failures "
                "of exactly this kind are what the check closes: a gate "
                "credited to a mutant that dies eight gates earlier, and a "
                "gate credited to a mutant that reaches it and PASSES it.  "
                "The per-source provenance rows are excluded by name: their "
                "falsifier is `--break-anchor`, which is a separate process "
                "and not an in-run mutant"
                % len(credited),
                not unreachable and not uncredited,
                {"falsifiable_rows": len(credited),
                 "unreachable": [list(u) for u in unreachable] or "none",
                 "uncredited": uncredited or "none"})

        # the final coverage check must AGREE with the sealed in-run row
        cov2 = paper_coverage(R, paper_text)
        LD.gate("G-PAPER-COVERAGE-FINAL",
                "the paper-claim and numeral-coverage check is re-run once "
                "the instrument's own totals close, so the paper's instrument "
                "section is covered too; its in-run twins carry the injection "
                "falsifiers and this evaluation is the enforcement -- a "
                "failure here exits 1 and writes nothing.  It also closes the "
                "residue ledger: every declared in-text residue must actually "
                "occur in the paper, so the list cannot be padded.  And it "
                "AGREES ROW FOR ROW with the coverage row sealed in run, "
                "which is why the re-run does not overwrite the sealed object",
                not cov2["missing"] and not cov2["uncovered"]
                and not cov2["undeclared_hex"]
                and not cov2["residue_declared_but_absent"]
                and cov2 == R["paper_coverage"],
                {"missing": cov2["missing"] or "none",
                 "uncovered": cov2["uncovered"] or "none",
                 "undeclared_hex": cov2["undeclared_hex"] or "none",
                 "agrees_with_the_sealed_row": cov2 == R["paper_coverage"],
                 "declared_but_absent":
                     cov2["residue_declared_but_absent"] or "none"})

        # THE CLOSING COUNTS ARE DERIVED, NEVER STORED AND RE-READ: every
        # number is recomputed from the chained gate ledger and the sealed
        # mutant report, so none can be moved without breaking one of those.
        killed = sum(1 for m in R["mutants"] if m["killed"])
        ontgt = sum(1 for m in R["mutants"] if m["on_target"])
        LD.gate("G-CLOSURE-DERIVED",
                "THE CLOSING COUNTS ARE DERIVED FROM THE SEALED ROWS.  With "
                "this row the ledger closes at %d gates -- exactly the number "
                "the in-run totals predicted BEFORE the sweep began, from the "
                "declared universe minus the %d gates evaluated outside the "
                "ledger -- and every one of them passed.  %d of %d declared "
                "mutants were killed and %d on target, recomputed here from "
                "the sealed mutant report rather than carried forward in a "
                "counter"
                % (len(LD.rows) + 1, len(NOT_IN_RECEIPT), killed,
                   len(MUTANTS), ontgt),
                len(LD.rows) + 1 == R["totals"]["gates_in_receipt"]
                and all(g["passed"] for g in LD.rows)
                and killed == len(MUTANTS) and ontgt == len(MUTANTS),
                {"rows_at_close": len(LD.rows) + 1,
                 "predicted": R["totals"]["gates_in_receipt"],
                 "mutants_killed": killed, "mutants_on_target": ontgt})
        R["gates"] = LD.rows
        R["closure"] = {
            "gates_in_receipt": len(R["gates"]),
            "gates_passed": sum(1 for g in R["gates"] if g["passed"]),
            "mutants_killed": killed, "mutants_on_target": ontgt,
        }
        SEAL.take("SEAL-CLOSURE", R)
        emit_report(R, SEAL)
        R["transcript"] = {"lines": len(LINES), "chain": TRANSCRIPT_CHAIN[0],
                           "sha256_12": SEAL.transcript_sha}
        ok_close, close_ev = SEAL.close(R, LD)
        print("G-SEAL-CLOSE: %s -- %s"
              % ("the seal closes, totally" if ok_close
                 else "THE SEAL DID NOT CLOSE", close_ev), flush=True)
        if not ok_close:
            raise GateFail("G-SEAL-CLOSE :: %s" % close_ev)
    except GateFail as e:
        say("")
        say("GATE FAILED: %s" % e)
        print("GATE FAILED: %s" % e, file=sys.stderr)
        print("EXIT 1", file=sys.stderr)
        sys.exit(1)

    if write:
        payload, text = SEAL.payload, SEAL.transcript

        def against_the_seal(js, tx):
            if (digest(js) != SEAL.payload_sha
                    or digest(tx) != SEAL.transcript_sha):
                return False
            disk = json.loads(js)
            if SEAL.verify(disk):
                return False
            return (reconstruct_from_serialized(js)
                    == (R["verdict"]["crystal"], R["verdict"]["det"],
                        R["verdict"]["constructibility"]))

        probe = OUT_JSON + ".integrity-probe"
        with open(probe, "w", encoding="utf-8") as f:
            f.write(payload[:-1] + " }")
        detected = digest(read_text(probe)) != SEAL.payload_sha
        os.remove(probe)
        tj, tt = OUT_JSON + ".tmp", OUT_TXT + ".tmp"
        with open(tj, "w", encoding="utf-8") as f:
            f.write(payload)
        with open(tt, "w", encoding="utf-8") as f:
            f.write(text)
        if not (detected and against_the_seal(read_text(tj), read_text(tt))):
            os.remove(tj)
            os.remove(tt)
            print("GATE FAILED: G-ARTIFACT-INTEGRITY :: what was about to be "
                  "written does not match the gate-time seal (corruption "
                  "detected=%s); nothing written" % detected, flush=True)
            sys.exit(1)
        # CONTAINMENT: the bytes standing before the replace are held, so a
        # failure after it restores them instead of leaving a corrupt or
        # non-parsing artifact on disk with only a warning line
        prior = {p: (read_text(p) if os.path.exists(p) else None)
                 for p in (OUT_JSON, OUT_TXT)}
        os.replace(tj, OUT_JSON)
        os.replace(tt, OUT_TXT)
        if not against_the_seal(read_text(OUT_JSON), read_text(OUT_TXT)):
            for p, was in prior.items():
                if was is None:
                    if os.path.exists(p):
                        os.remove(p)
                else:
                    with open(p, "w", encoding="utf-8") as f:
                        f.write(was)
            print("GATE FAILED: G-ARTIFACT-INTEGRITY :: the artifacts on disk "
                  "differ from the gate-time seal; the previous artifacts "
                  "have been RESTORED and nothing corrupt is left in place",
                  flush=True)
            print("EXIT 1", file=sys.stderr)
            sys.exit(1)
        print("G-ARTIFACT-INTEGRITY: corrupted probe detected; both artifacts "
              "written from the SEALED payload, re-read from disk and matched "
              "against the gate-time seal -- %d sealed objects, %d declared "
              "unsealed, payload %s, transcript %s (%d + %d bytes)."
              % (len(SEAL.rows), len(UNSEALED_DECLARED), SEAL.payload_sha,
                 SEAL.transcript_sha, len(payload), len(text)), flush=True)
    sys.exit(0)


if __name__ == "__main__":
    main()
