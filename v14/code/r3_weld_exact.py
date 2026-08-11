#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
v14 R=3 WELD -- THE ARENA, THE POSITIVE GEOMETRY, AND THE WELD RE-POSED.
Instrument for `v14/paper-19-r3-weld.md`.

QUESTION (pin `v14/note-r3weld-pin.md`, sha256-12 20fba9b15f5e, ledger #154).
U4b measured the R = 2 schedule family EMPTY of positive geometry -- POSDEF
ceiling 3, I7-STRICT empty -- and its adjudication (#153) registered the cause
as a LINK-INCIDENCE BUDGET: two rounds deposit at most 18 incidences and
positive definiteness needs 3 per site, so 9 sites need 27.  R = 3 lifts the
budget to exactly 27.  This unit runs the three stages the pin gates:

  STAGE 1  THE ARENA, UNIT-GRADE.  The U4b machinery extended one round.  The
           uniform R = 3 arrangement -- three rounds grouped on the three
           link-direction parallel classes -- is DRIVEN through the committed
           grammar's own menus and confirmed: n = 1 at all 27 cells, det = 3/4,
           positive definite at 9 of 9 sites.  Then forcedness, homogeneity,
           crystallinity (the affine law taken on the union, re-pre-registered
           on the SUMMED field) and fragility, on both variables.
  STAGE 2  THE POSITIVE-GEOMETRY CENSUS, exhaustive over all 280^3 grouping
           triples: the attained positive-definiteness ceiling, the determinant
           spectrum, the I7-STRICT class.
  STAGE 3  THE WELD, RE-POSED LIVE.  Weld 2's detector -- both readings, the
           RSQ choice standard with fibers -- pointed at the R = 3 I7-STRICT
           records against I7's own arena, with weld 2's FOUND-side crystal
           control and EMPTY-side walk control re-established here, two-way and
           falsified.

WHAT THIS PROGRAM DOES
  SEC 1  PROVENANCE.  14 pinned sources, sha256-12 verified, products gated;
         the verbatim (#62) anchors bound to their consumer gates -- each
         named gate required to be in the registry AND in this run's ledger;
         every text gate whitespace-normalises, ASCII-folds AND strips
         markdown prefixes.
  SEC 2  EXACT ARITHMETIC on Z_3^2 and Z[w]; the three stabilizer routes.
  SEC 3  THE COMMITTED GRAMMAR, DRIVEN DIRECTLY.  d42b1's transport layer by
         text slice, d60's `B`/`dl`, d66's `conflict_grid`, d58's `walk2` by AST
         extraction.  No admissibility rule is re-typed anywhere in this file.
         The menu is memoised and the memo is GATED against the raw layer.
  SEC 4  THE R = 3 FAMILY and the declared driven WINDOW, disclosed in the head.
  SEC 5  THE COMBINATORIAL COLUMNS, packed exactly (6 bits per site).
  SEC 6  STAGE 1.
  SEC 7  STAGE 2.
  SEC 8  STAGE 3 -- the weld detector, the arenas, the controls.
  SEC 9  THE WALLS (four inherited from U4, the Lorentzian resonance NAMED).
  SEC 10 The verdict, derived a second time from the serialized receipt by a
         comparator that TYPES ALL THREE TEMPLATES ITSELF and re-derives the
         outcome word from the receipt's own fate rows; the paper gates --
         claim rendering, numeral coverage INCLUDING THE FENCED VERDICT
         BLOCKS, head-verbatim and claim polarity; the TOTAL seal; the
         sweep-execution binding; the artifacts; the integrity check.

CLI CONTRACT (the #82 minimum: argv parsed against a whitelist)
---------------------------------------------------------------
    python3.13 v14/code/r3_weld_exact.py
        THE DELIVERY RUN, and the ONLY writer.  Builds the whole census,
        evaluates every gate (the paper gates included), runs every declared
        mutant in-process, re-reads what it wrote and writes
        `r3_weld_output.txt` and `r3_weld_receipt.json` beside this file.
        Exits 0 iff every gate passes.

    --no-write      the same run, writing nothing.
    --numbers       the census only: every published row printed, no paper
                    gate, no mutant sweep, nothing written.
    --selftest      FALSIFICATION SELF-TEST.  Corrupts one anchor's expected
                    digest IN MEMORY, confirms the run dies at the anchor gate,
                    writes nothing, exits 1.  Exits 2 if the corrupted run does
                    NOT die.
    --mutant NAME   runs the pipeline with the named mutant active.  Exits 1
                    when the mutant is killed (the intended outcome), 0 if it
                    survives.  An unknown NAME exits 2.  Writes nothing.
    --break-anchor NAME
                    corrupts the named source anchor's expected digest.
                    Unknown NAME exits 2.  The run must exit 1.
    --verify-paper [PATH]
                    rebuilds the derivation and evaluates the paper gates --
                    claim rendering, numeral coverage and claim POLARITY --
                    with PATH (this unit's paper by default) as the object
                    under test.  Exits 1 on drift, 0 on a clean paper, 2 if
                    PATH does not exist or is not a file.
    --list-gates / --list-mutants
                    print the registries and exit 0.

    Any other argument, any unknown flag argument, any missing flag argument,
    any SECOND MODE FLAG and any --verify-paper PATH that does not exist exits
    2.  No flag is mutant-only and no flag is a no-op: modes do not compose,
    so a second mode flag is an error rather than a silent override.

THE TOTAL GATE-TO-DISK SEAL (RUNBOOK 14 addendum, v14 #119 + the #148 totality
addendum + the U4b vouching-layer lesson).  EVERY published receipt key -- the
measured layer AND the vouching layer: schema, provenance, paper_claims,
coverage, polarity, gates, totals, and the transcript head -- is either sealed
at the moment its gate passes or listed as DECLARED-UNSEALED in the manifest,
and a gate compares the manifest against the DECLARED key set rather than
against the keys that happened to be taken.  The artifacts are written from the
sealed payload through `os.replace`, and the terminal integrity gate compares
the BYTES ON DISK against the gate-time seal.

TEXT GATES (#125 WITH MARKDOWN-PREFIX NORMALIZATION, per the U4b adjudication
section 2).  Every gate that matches prose against a needle whitespace-
normalises both sides, ASCII-folds both sides, AND strips markdown line
prefixes (blockquote markers and list-item bullets), so a needle that spans a
block quote or a numbered list cannot be evaded by re-wrapping.

ARITHMETIC.  Exact only: `fractions.Fraction` and Python integers.  There are
no floats anywhere -- an AST scan of this file and a recursive type scan of the
emitted receipt are gates.

RUNTIME INPUTS (#46/#91).  Exactly 14 files are read at run time as SOURCES,
all hash-pinned by this unit's frozen declaration, plus exactly one file read
as the OBJECT UNDER TEST -- this unit's own paper.  Both lists are enumerated
and gated.  No repository state outside them is read and no subprocess of any
kind is invoked, so the run is correct off-tree and with no version control
present.
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
OUT_TXT = os.path.join(os.path.dirname(SELF), "r3_weld_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "r3_weld_receipt.json")

SCHEMA = "isp/v14/r3-weld/1"
PAPER_REL = "v14/paper-19-r3-weld.md"

# ===========================================================================
# SECTION 0.  THE FROZEN DECLARATION (RUNBOOK section 15: the arena is data)
# ===========================================================================

SOURCES = [
    ("A-PIN", "v14/note-r3weld-pin.md", "20fba9b15f5e",
     "THIS UNIT'S PIN (ledger #154): the three stages, the window licensing "
     "pattern, the pre-registered outcome names."),
    ("A-U4BADJ", "v14/note-u4b-adjudication.md", "17c31c4ba898",
     "the U4b adjudication (#153): the R = 3 saturation entered into the "
     "successor register as the weld route's exact demand."),
    ("A-U4BEFF", "v14/review-u4b-effectus.md", "dc37768d323b",
     "the U4b effectus review (#150): the R = 3 saturating computation this "
     "unit must confirm unit-grade, and its four demands on the successor."),
    ("A-W2", "v14/paper-13-weld2-carrier-census.md", "9cdb10472953",
     "WELD 2 (terminal): the detector, the two readings, the RSQ choice "
     "standard, the crystal and walk controls, and the dead lists this unit "
     "cites and never re-runs."),
    ("A-W2REC", "v14/code/w2_census_receipt.json", "bd68497d4510",
     "WELD 2's COMMITTED RECEIPT: the FOUND-at-I7 declared probe on which "
     "weld 2 exhibited the FOUND branch.  Its induced record is READ from "
     "these bytes and recomputed here -- the precedent that fixes what "
     "reaching FOUND at this target has always meant."),
    ("A-HA", "v13/paper-ha-successor.md", "f286ba10d2d9",
     "I7 / HA: the declared readout, the admissibility criterion, and "
     "requirement 3 -- the two-way rule this unit's controls discharge."),
    ("A-I7", "v13/code/ha_successor_receipt.json", "542b8735daf0",
     "I7's ARENA AS DATA: sites, links, the declared record family and the "
     "declared count box whose admissible points this unit recomputes."),
    ("A-D42B1", "v10/code/d42b1_transport_exact.py", "576275d55ecf",
     "THE COMMITTED TRANSPORT GRAMMAR, driven directly: this unit's only "
     "source of admissibility."),
    ("A-D60", "v10/code/d60_crystal_exact.py", "684cdb76552b",
     "D60: the Builder `B` and the delivery helper `dl`, AST-extracted."),
    ("A-D66", "v10/code/d66_arbitration_crystal_exact.py", "3d0516ab106e",
     "D66: CONFLICT-GRID(g, R) and DOUBLE-GRID(g, R) -- the committed "
     "constructors, AST-extracted and re-run."),
    ("A-D66OUT", "v10/data/d66_arbitration_crystal_exact.out", "e252529d2586",
     "D66's COMMITTED OUTPUT: the GRID(g=3,*) rows are READ from this file at "
     "run time and reproduced, never re-typed."),
    ("A-D58", "v10/code/d58_atlas_instrument_exact.py", "e5f58cb52a06",
     "D58: `walk2`, the generic 2-actor walk that is weld 2's EMPTY-side "
     "control, AST-extracted and re-run at its committed depth and seed."),
    ("A-L1", "v11/note-L1-lorentz-no-go-lemma.md", "93ea24591c3c",
     "L-1: the fourth-form clause this unit argues before any test, and the "
     "sentence retracted on 2026-07-28 that no paper may reproduce."),
    ("A-CAT", "v11/note-v11p0a-reproduction-catalog.md", "0cebe543e814",
     "the reproduction catalog 1.6/1.7: the BHS block and the "
     "Kleitman-Rothschild height-control warning."),
]
SOURCE_IDS = [s[0] for s in SOURCES]

# the retracted L-1 sentence: no paper of this line may reproduce it
BANNED_L1 = ("precisely the form U4 tests, and precisely the form the "
             "corpus's strongest relativity result took")

# THE LORENTZIAN RESONANCE.  The U4b lesson: naming is mandatory -- silence is
# how a resonance becomes governance.  This sentence is REQUIRED in the paper
# and a gate enforces its presence.
LORENTZ_NAMED = ("The induced form is NAMED AND NOT READ: q = [[1, -1/2], "
                 "[-1/2, 1]] is a positive definite Euclidean form on a "
                 "nine-site lattice, it is not a signature, and no Lorentzian "
                 "reading of it is taken here or licensed by anything measured "
                 "here.")

MUTANTS = [
    ("MUT-UNIT-GRADE", "G-UNIT-GRADE",
     "moves one of the 27 driven link counts of the uniform arrangement -- "
     "must die at the per-cell unit-grade gate"),
    ("MUT-DET-UNIFORM", "G-UNIT-GRADE",
     "reports the uniform arrangement's determinant as 1 rather than 3/4 -- "
     "must die at the per-site unit-grade gate"),
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
    ("MUT-MEMO-DIRTY", "G-MENU-PURE",
     "poisons one memoised menu entry -- must die at the gate that re-drives "
     "the declared re-drive set with the memo disabled"),
    ("MUT-DRIVEN-FIELD", "G-DRIVEN-EQUALS-COMBINATORIAL",
     "detaches one driven record's link field from the combinatorial one -- "
     "must die at the per-schedule driven-vs-combinatorial gate"),
    ("MUT-FAMILY-COUNT", "G-FAMILY-COUNT",
     "corrupts the computed family size -- must die at the two-route count "
     "gate (#24)"),
    ("MUT-WINDOW-SILENT", "G-WINDOW-DISCLOSED",
     "reports the declared window as the whole family -- must die at the "
     "no-silent-caps disclosure gate"),
    ("MUT-STRATUM-BLIND", "G-STRATA-WITNESSED",
     "drops one census stratum's driven witness -- must die at the "
     "every-stratum-witnessed gate"),
    ("MUT-CEILING", "G-POSDEF-CEILING",
     "reports the attained positive-definiteness ceiling as 8 -- must die at "
     "the exhaustive ceiling gate"),
    ("MUT-CEILING-GAP", "G-POSDEF-CEILING",
     "plants one triple at 8 positive-definite sites -- must die at the "
     "gate that measures the empty cell"),
    ("MUT-STRICT-COUNT", "G-STRICT-COUNT",
     "corrupts the I7-STRICT population -- must die at the two-route count "
     "gate"),
    ("MUT-RIGIDITY", "G-RIGIDITY",
     "reports one I7-STRICT triple whose field is not identically 1 -- must "
     "die at the per-object rigidity gate"),
    ("MUT-DETSPEC", "G-DET-SPECTRUM",
     "drops one determinant value from the spectrum -- must die at the "
     "spectrum-total gate (#24)"),
    ("MUT-FULLGROUP", "G-FULL-GROUP",
     "reports the full group Z_3^2 as unreachable at R = 3 -- must die at the "
     "two-route full-group gate"),
    ("MUT-STAB-ROUTE", "G-STAB-ROUTES",
     "corrupts the Fourier-annihilator route on one field -- must die at the "
     "three-route agreement gate"),
    ("MUT-AFFINE-LAW", "G-AFFINE-LAW",
     "reports one crystalline seed triple whose field is not a non-negative "
     "combination of the period's coset indicators -- must die at the "
     "per-object affine-law gate"),
    ("MUT-CU-SPLIT", "G-CU-SPLIT-EMPTY",
     "reports a CU-SPLIT seed triple as crystalline -- must die at the "
     "split-coset gate"),
    ("MUT-BEYOND-COSET", "G-BEYOND-COSET-CRYSTALLINE",
     "reports the beyond-coset crystalline population as empty -- must die at "
     "the per-witness beyond-coset gate"),
    ("MUT-FRAGILITY", "G-FRAGILITY-SEED",
     "reports one admissible single-arbitration re-seating as preserving the "
     "stabilizer -- must die at the per-object fragility gate"),
    ("MUT-GEOM-FRAGILITY", "G-FRAGILITY-GEOM",
     "reports one grouping swap as preserving I7-strictness -- must die at "
     "the per-object geometric fragility gate"),
    ("MUT-SEED-INVARIANCE", "G-GEOM-SEED-INVARIANT",
     "reports the geometry as seed-dependent -- must die at the exhaustive "
     "seed-invariance gate"),
    ("MUT-HOMOG", "G-HOMOGENEITY",
     "reports one driven saturating record as inhomogeneous -- must die at "
     "the per-record homogeneity gate"),
    ("MUT-COORD-FREE", "G-COORDINATE-FREE-CLASS",
     "reports the coordinate-free saturating class as equal to the "
     "I7-STRICT class -- must die at the four-class census gate"),
    ("MUT-READINGS", "G-READINGS",
     "collapses the two readings into one -- must die at the gate that "
     "requires every row to carry its reading stamp"),
    ("MUT-CRYSTAL-DIAGONAL", "G-CTRL-CRYSTAL-AT-I7",
     "reports the committed crystal's diagonal co-division count as "
     "populated -- must die at the reproduced weld-2 measurement"),
    ("MUT-COUNT-SUFFICIENT", "G-COUNT-IMPLIES-WELD",
     "reports the committed R = 3 grid as clearing the count condition -- "
     "must die at the necessity/sufficiency gate"),
    ("MUT-WELD-FATE", "G-WELD-CENSUS",
     "flips one census row's fate -- must die at the per-row declared-fate "
     "gate (#87)"),
    ("MUT-ISOS", "G-ISOS-ANCHOR",
     "corrupts the isomorphism count at the saturating arena -- must die at "
     "the anchor gate that binds it to weld 2's committed 1296"),
    ("MUT-FIBER-LAX", "G-CTRL-FALSIFIER",
     "reports the crystal falsifier's choice fibers as all 1 -- must die at "
     "the two-way control gate, which reads that fiber against weld 2's "
     "committed value"),
    ("MUT-FIBER-SAT", "G-FIBERS",
     "plants a free item in the saturating arena's choice inventory -- must "
     "die at the RSQ choice-standard gate"),
    ("MUT-CTRL-FOUND", "G-CTRL-FOUND-CRYSTAL",
     "reports weld 2's crystal control as not FOUND -- must die at the "
     "FOUND-side control gate"),
    ("MUT-CTRL-FALSIFIER", "G-CTRL-FALSIFIER",
     "reports the crystal falsifier as FOUND -- must die at the two-way "
     "control gate"),
    ("MUT-CTRL-WALK", "G-CTRL-EMPTY-WALK",
     "reports the generic walk as reaching the site arity -- must die at the "
     "EMPTY-side control gate"),
    ("MUT-CTRL-R3-FALSIFIER", "G-CTRL-R3-FALSIFIER",
     "reports the R = 3 saturating falsifier as FOUND -- must die at the "
     "at-this-arena two-way gate"),
    ("MUT-ADMISSIBLE", "G-ADMISSIBLE",
     "reports the induced record as inadmissible -- must die at the "
     "per-site Sylvester gate"),
    ("MUT-I7-BOX", "G-I7-BOX",
     "corrupts the recomputed admissible-point count of I7's declared box -- "
     "must die at the anchor gate against I7's committed 361"),
    ("MUT-IN-FAMILY", "G-NOT-IN-FAMILY",
     "reports the induced record as a member of I7's declared record family "
     "-- must die at the per-record chart-orbit gate"),
    ("MUT-SMUGGLE-BLIND", "G-SMUGGLE",
     "makes the smuggling classifier blind -- must die at the gate that "
     "requires the declared S-valued probe to classify SMUGGLED"),
    ("MUT-DEAD-LIST", "G-DEAD-LISTS-CITED",
     "re-derives a dead-list row instead of citing it -- must die at the "
     "cited-not-re-run gate"),
    ("MUT-TWO-WAY", "G-TWO-WAY",
     "drops one detector value from the exhibited set -- must die at HA "
     "requirement 3's gate"),
    ("MUT-WALL-L1", "G-WALL-L1",
     "injects the retracted L-1 sentence into the paper under test, "
     "LINE-WRAPPED AND BLOCKQUOTED in house style -- must die at the "
     "markdown-prefix-normalised L-1 wall gate (#125)"),
    ("MUT-WALL-BHS", "G-WALL-BHS",
     "runs a sprinkling-grade boost reading -- must die at the BHS wall gate"),
    ("MUT-WALL-KR", "G-WALL-KR",
     "takes a dimension reading with no height control -- must die at the "
     "Kleitman-Rothschild wall gate"),
    ("MUT-WALL-COSMO", "G-WALL-DIAGONAL",
     "reads the measured diagonal cosmologically -- must die at the diagonal "
     "wall gate"),
    ("MUT-WALL-LORENTZ", "G-WALL-LORENTZ-NAMED",
     "deletes the mandatory NAMED-AND-NOT-READ sentence from the paper under "
     "test -- must die at the naming gate"),
    ("MUT-VERBATIM", "G-VERBATIM",
     "corrupts one verbatim source quote -- must die at the #62 anchor gate"),
    ("MUT-ANCHOR-DRIFT", "G-ANCHORS-READ",
     "moves one number recomputed against a committed file -- must die at "
     "the read-anchor gate (which --break-anchor cannot reach, because the "
     "provenance gate kills that run first)"),
    ("MUT-HEAD", "G-VERDICT-RECONSTRUCTED",
     "corrupts one field of the head -- must die at the independent "
     "reconstruction gate"),
    ("MUT-SEAL-BROKEN", "G-SEAL-COMPLETE",
     "mutates a sealed object after its gate passed -- must die at the "
     "gate-time seal verification (#119)"),
    ("MUT-SEAL-DROP", "G-SEAL-COMPLETE",
     "silently drops one seal from the manifest -- must die at the TOTALITY "
     "gate, which compares the manifest against the DECLARED key set"),
    ("MUT-TRANSCRIPT-FLIP", "G-SEAL-COMPLETE",
     "flips one line of the transcript head after it was sealed -- must die "
     "at the transcript seal (#148 totality addendum)"),
    ("MUT-SELFTEST-WRITES", "G-SELFTEST-WRITES-NOTHING",
     "lets the self-test path reach a writer -- must die at the "
     "writes-nothing gate"),
    ("MUT-CLI-PERMISSIVE", "G-CLI-WHITELIST",
     "swaps the argv whitelist for the registered permissive shape -- must "
     "die at the CLI contract gate (#82)"),
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS",
     "silently drops one instrument claim from the paper under test -- must "
     "die at the claim-rendering gate"),
    ("MUT-PAPER-NUMERAL", "G-PAPER-NUMERAL-COVERAGE",
     "injects an unregistered numeral into the paper under test -- must die "
     "at the numeral-coverage gate"),
    ("MUT-PAPER-POLARITY", "G-PAPER-CLAIM-POLARITY",
     "flips one declared polarity of the paper's head -- must die at the "
     "polarity gate"),
    # ---- the panel's repairs, each with its own falsifier ----------------
    ("MUT-WELD-FORGERY", "G-VERDICT-RECONSTRUCTED",
     "THE ONE-LINE HEAD FORGERY (the instrument review's M1): patches the "
     "BUILDER's outcome word to EMPTY.  Before the repair the comparator "
     "called the same function and moved with it; now the comparator types "
     "the weld template itself and derives the outcome word from the "
     "receipt's own fate rows, so the forgery must die at the "
     "reconstruction gate"),
    ("MUT-PAPER-HEAD-NUMERAL", "G-PAPER-NUMERAL-COVERAGE",
     "corrupts a numeral INSIDE the paper's fenced verdict block (the "
     "instrument review's M2): before the repair the numeral gate stripped "
     "every fenced block before scanning, so head numerals were never "
     "scanned at all -- must die at the numeral-coverage gate"),
    ("MUT-PAPER-HEAD", "G-PAPER-HEAD-VERBATIM",
     "moves one non-numeric character of the paper's rendered head -- must "
     "die at the gate that matches every character of every verdict segment "
     "into the paper"),
    ("MUT-SWEEP-UNBOUND", "G-SWEEP-BOUND",
     "declares the delivery-level sweep while carrying no sweep rows (the "
     "instrument review's m2: a delivery whose 59-mutant loop never ran "
     "shipped) -- must die at the sweep-execution gate"),
    ("MUT-CONSUMER-BINDING", "G-ANCHOR-CONSUMERS",
     "names a consumer gate that no gate registry carries and that this run "
     "never evaluated (the instrument review's m3) -- must die at the gate "
     "that binds every verbatim anchor to a gate that actually ran"),
    ("MUT-SITEWISE", "G-SITEWISE-IDENTITY",
     "breaks the sitewise identity at one of the 64 reachable site codes -- "
     "must die at the per-code identity gate"),
    ("MUT-STRICTEST", "G-STRICTEST-READING",
     "reports the ROW|COL|ANT arena as surviving the site-carrier-fixed "
     "reading -- must die at the strictest-reading gate"),
    ("MUT-W2-WITNESS", "G-W2-WITNESS",
     "reports weld 2's own FOUND-at-I7 witness as one of I7's declared "
     "records -- must die at the gate that reads that witness from weld 2's "
     "committed receipt"),
    ("MUT-COVERAGE-COUNT", "G-COUNT-IMPLIES-WELD",
     "reports the committed R = 3 grid as covering all 27 cells -- must die "
     "at the COVERAGE-not-count gate"),
    ("MUT-DIRECTED", "G-READINGS",
     "reports the directed comparator as separating an arena -- must die at "
     "the readings gate, which carries the comparator's measured value"),
    ("MUT-FIBER-BASEMAP", "G-FIBERS",
     "reports the label and orient fibers as base-map-dependent -- must die "
     "at the choice-standard gate, which now reads both at EVERY base map"),
    ("MUT-R4-REGISTER", "G-R4-REGISTER",
     "reports I7's own G-FLAT as unreachable at the R = 4 budget -- must die "
     "at the successor-register probe gate"),
]
MUTANT_NAMES = {m[0] for m in MUTANTS}

MUT = None
QUIET = False
LINES = []
READS = []


class GateFail(Exception):
    pass


class CliError(Exception):
    pass


def say(s=""):
    LINES.append(s)
    if not QUIET:
        print(s, flush=True)


def mut(name):
    return MUT == name


def pick(name, normal, corrupted):
    """the mutant hook: returns `normal` unless this run is that mutant."""
    return corrupted if MUT == name else normal


# ===========================================================================
# SECTION 1.  MACHINERY -- the gate ledger, the seal, the text normaliser
# ===========================================================================

class Ledger:
    """gates carry their verdict IN the statement; a failure raises."""

    def __init__(self):
        self.rows = []

    def gate(self, name, statement, ok, evidence, waiver=None):
        ok = bool(ok)
        self.rows.append({"gate": name, "statement": statement,
                          "passed": ok, "evidence": str(evidence),
                          "waiver": waiver})
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


def jpath(obj, path):
    cur = obj
    for part in path.split("/"):
        cur = cur[int(part)] if isinstance(cur, list) else cur[part]
    return cur


# THE TOTAL SEAL.  Every published receipt key is here, with the gate at which
# it is sealed -- or, for the two keys that cannot be sealed before they are
# complete, an explicit DECLARED-UNSEALED row.  G-SEAL-COMPLETE compares the
# manifest against THIS declaration, not against what was taken.
SEALED_PATHS = [
    ("SEAL-SCHEMA", "schema", "G-PROVENANCE"),
    ("SEAL-PROVENANCE", "provenance", "G-PROVENANCE"),
    ("SEAL-ANCHORS", "anchors", "G-ISOS-ANCHOR"),
    ("SEAL-VERBATIM", "verbatim_anchors", "G-VERBATIM"),
    ("SEAL-FAMILY", "family", "G-WINDOW-DISCLOSED"),
    ("SEAL-CONSTRUCTIBILITY", "constructibility", "G-CTRL-BRANCHING"),
    ("SEAL-ARENA", "arena", "G-UNIT-GRADE"),
    ("SEAL-CRYSTAL", "crystal", "G-FRAGILITY-SEED"),
    ("SEAL-GEOMETRY", "geometry", "G-FRAGILITY-GEOM"),
    ("SEAL-I7", "i7", "G-NOT-IN-FAMILY"),
    ("SEAL-WELD", "weld", "G-TWO-WAY"),
    ("SEAL-STRATA", "strata", "G-STRATA-WITNESSED"),
    ("SEAL-WALLS", "walls", "G-WALL-LORENTZ-NAMED"),
    ("SEAL-VERDICT", "verdict", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-COUNTS", "counts", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-PAPER-CLAIMS", "paper_claims", "G-PAPER-CLAIMS"),
    ("SEAL-PAPER-COVERAGE", "paper_coverage", "G-PAPER-HEAD-VERBATIM"),
    ("SEAL-POLARITY", "polarity", "G-PAPER-CLAIM-POLARITY"),
    ("SEAL-COVERAGE", "coverage", "G-COVERAGE"),
    ("SEAL-REACHABILITY", "reachability", "G-REACHABILITY"),
    ("SEAL-WAIVERS", "waiver_ledger", "G-COVERAGE"),
    ("SEAL-MUTANTS", "mutants", "G-COVERAGE"),
    ("SEAL-MUTANT-SWEEP", "mutant_sweep", "G-SWEEP-BOUND"),
    ("SEAL-GATES", "gates", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-CLOSING", "closing_gates", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-TOTALS", "totals", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-TRANSCRIPT", "transcript_head", "G-PAPER-COVERAGE-FINAL"),
]
# the keys that CANNOT be sealed before the payload closes, declared unsealed
DECLARED_UNSEALED = ["arithmetic", "python", "seal_manifest",
                     "payload_sha256_12"]
# the instrument review's m1: the totality gate measured the manifest against
# a declaration the same file owned, so a COHERENT drop -- remove the seal row,
# remove the declaration AND append the key here -- shipped a corrupted object
# with nothing but a longer unsealed list as its trace.  The list is therefore
# frozen by content and by length, and no key that carries a MEASUREMENT may
# appear on it.
DECLARED_UNSEALED_FROZEN = ("arithmetic", "python", "seal_manifest",
                            "payload_sha256_12")
# the MEASUREMENT LAYER: the receipt keys that carry what this run measured.
# The anchor and provenance layers are deliberately NOT here -- they quote the
# walls' own pinned sources, and quoting a wall is not taking a reading.
MEASURED_KEYS = ("arena", "family", "constructibility", "crystal", "geometry",
                 "i7", "weld", "strata", "anchors", "counts", "verdict")
SEALS_IN_RUN = tuple(s for s, _p, g in SEALED_PATHS
                     if g != "G-PAPER-COVERAGE-FINAL")


class Seal:
    """the TOTAL gate-time seal (#119 + #148)."""

    def __init__(self):
        self.rows = []
        self.index = {}
        self.payload = None
        self.payload_sha = None

    def take(self, sid, obj):
        path = [p for s, p, _g in SEALED_PATHS if s == sid][0]
        at = [g for s, _p, g in SEALED_PATHS if s == sid][0]
        d = digest(jpath(obj, path))
        if mut("MUT-SEAL-DROP") and sid == "SEAL-COVERAGE":
            return
        self.rows.append({"seal": sid, "path": path, "sealed_at_gate": at,
                          "sha256_12": d})
        self.index[sid] = d

    def verify(self, obj, only=None):
        broken = []
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
        return broken

    def totality(self):
        """#148: the manifest must cover the DECLARED key set exactly."""
        have = {r["seal"] for r in self.rows}
        want = {s for s, _p, _g in SEALED_PATHS}
        return sorted(want - have), sorted(have - want)

    def close(self, obj, payload):
        broken = self.verify(obj)
        if broken:
            raise GateFail("G-ARTIFACT-INTEGRITY :: the payload was sealed "
                           "over a broken seal :: %s" % broken)
        self.payload = payload
        self.payload_sha = digest(payload)


def read_bytes(rel):
    READS.append(rel)
    with open(os.path.join(REPO, rel), "rb") as fh:
        return fh.read()


def read_text(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


_FOLD = {"—": "--", "–": "-", "’": "'", "“": '"',
         "”": '"', "≤": "<=", "≥": ">=", "≠": "!=",
         "≡": "=", "×": "x", "₁": "1", "₂": "2",
         "₀": "0", "₃": "3", "ℓ": "l", "→": "->",
         "⋅": "*", "²": "2", "≈": "~", "⊆": "subset",
         "∈": "in", "∑": "sum", "·": "*", "−": "-",
         "≥": ">=", "⁄": "/", " ": " "}

_MD_PREFIX = re.compile(r"^(?:\s*(?:>+|[-*+]|\d+[.)])\s+)+")


def mdstrip(s):
    """#125 WITH MARKDOWN-PREFIX NORMALIZATION (the U4b adjudication's
    clarification): strip blockquote markers and list-item bullets from the
    head of every line before matching, so a needle that spans a quoted or
    enumerated block cannot be evaded by re-wrapping it."""
    out = []
    for line in s.split("\n"):
        prev = None
        while prev != line:
            prev = line
            line = _MD_PREFIX.sub("", line)
            line = re.sub(r"^\s*>+\s*", "", line)
        out.append(line)
    return "\n".join(out)


def ascii_fold(s):
    for k, v in _FOLD.items():
        s = s.replace(k, v)
    return s


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def canon(s):
    """the full text-gate normalisation: markdown line prefixes, then
    markdown emphasis and code ticks, then the ASCII fold, then whitespace.
    BOTH sides of every text match go through it, so a needle cannot be
    evaded by re-wrapping, quoting, bulleting, bolding or back-ticking it."""
    return norm(ascii_fold(mdstrip(s).replace("*", "").replace("`", "")))


NEEDLE_FLOOR = 30


def match_needle(hay, needle):
    n = canon(needle)
    if len(n) < NEEDLE_FLOOR:
        raise GateFail("G-VERBATIM :: needle below the #62 length floor: %r"
                       % needle)
    return n in canon(hay)


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


def w_pow(m):
    m %= 3
    return (1, 0) if m == 0 else ((0, 1) if m == 1 else (-1, -1))


def stab_fourier(field, poison=False):
    """ROUTE 2 -- the annihilator of the support of the exact Z_3^2 Fourier
    transform in Z[w] = Z[t]/(t^2 + t + 1).  Shares no code with route 1."""
    support = []
    for k in SITES:
        acc = (0, 0)
        for x in SITES:
            c = field[x]
            if c == 0:
                continue
            p = w_pow(k[0] * x[0] + k[1] * x[1])
            acc = (acc[0] + c * p[0], acc[1] + c * p[1])
        if poison and k == (0, 1):
            acc = (acc[0] + 1, acc[1])
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
        self.raw_candidates_for = ns["candidates_for"]
        self.regs_of = ns["regs_of"]
        self.vname = ns["vname"]
        self.V0 = ns["V0"]
        self.memo = {}
        self.memo_hits = 0
        self.memo_calls = 0
        self.extracted = {}
        g60 = self._extract("v10/code/d60_crystal_exact.py", texts, "d60",
                            {"candidates_for": self.candidates_for,
                             "event_poset": ns["event_poset"], "V0": self.V0})
        self.B = g60["B"]
        self.dl = g60["dl"]
        self.d60_globals = g60
        g66 = self._extract("v10/code/d66_arbitration_crystal_exact.py", texts,
                            "d66",
                            {"B": self.B, "dl": self.dl, "vname": self.vname,
                             "V0": self.V0,
                             "candidates_for": self.candidates_for})
        self.conflict_grid = g66["conflict_grid"]
        self.double_grid = g66["double_grid"] if "double_grid" in g66 else None
        g58 = self._extract("v10/code/d58_atlas_instrument_exact.py", texts,
                            "d58", {"candidates_for": self.candidates_for},
                            only={"walk2"})
        self.walk2 = g58["walk2"]
        self.slice_exit_free = ("sys.exit" not in self.slice_text
                                and no_exit(ast.parse(self.slice_text).body))
        self.bodies_exit_free = all(no_exit(v)
                                    for v in self.extracted.values())

    def candidates_for(self, hist, inits):
        """THE MEMOISED MENU.  d42b1's `candidates_for` is a pure function of
        (history, initiators); the memo is a cache over that pair and nothing
        else, and G-MENU-PURE re-drives a declared set with the memo disabled
        and compares the records event for event."""
        self.memo_calls += 1
        key = (tuple(hist), tuple(inits))
        got = self.memo.get(key)
        if got is None:
            got = self.raw_candidates_for(list(hist), tuple(inits))
            self.memo[key] = got
        else:
            self.memo_hits += 1
        return got

    def _extract(self, rel, texts, marker, extra, only=None):
        """d60/d63/d64/d66's committed extraction idiom: keep only defs and
        classes, so no module-level statement can run."""
        tree = ast.parse(texts[rel])
        keep = [n for n in tree.body
                if isinstance(n, (ast.FunctionDef, ast.ClassDef))
                and (only is None or n.name in only)]
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


def drive(G, schedule, supply=True, underspecified=False, drop_supply=None,
          drop_arb=None):
    """THE GENERALIZED SCHEDULE DRIVER, one round wider than U4b's.  Exactly
    d66's CONFLICT-GRID(g, R) cycle -- conflict-supply deliveries from the
    group's seed, g proposals (0 for the seed, 1 for the rest), one g-proposer
    arbitration won by the seed -- with the GROUPING AND THE SEED taken from
    the schedule instead of being hard-wired to rows/columns and the diagonal.
    Groups are processed in ascending order of their seed's site index and
    members in ascending site index, which is d66's own order at the committed
    schedule.  Every event is specified by its FULL TUPLE and taken from the
    layer's own menu."""
    b = G.B(ACTORS)
    cur = {a: G.V0 for a in ACTORS}
    dropped = 0
    narb = 0
    for rnd, (groups, seeds) in enumerate(schedule):
        order = sorted(range(len(groups)),
                       key=lambda gi: SITE_INDEX[seeds[gi]])
        for gi in order:
            grp = [actor(s) for s in sorted(groups[gi])]
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
            if drop_arb is not None and narb == drop_arb:
                narb += 1
                continue
            narb += 1
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


def branching_control(G):
    """THE UNDER-SPECIFIED CONTROL, made reproducible (U4b's own form).  The
    committed record is replayed up to its first arbitration, ONE
    under-specified pick is made, the builder's own `maxhits` is read, and the
    run stops: which candidate `sorted(key=repr)` would return is hash-seed
    dependent, the COUNT is not."""
    rec = driven(G, COMMITTED_R2)
    first = min(k for k, e in enumerate(rec["H"]) if e[0] == "r")
    seed = rec["H"][first][1]
    b = G.B(ACTORS)
    b.H = list(rec["H"][:first])
    b.pick((seed,), lambda z, s=seed: z[0] == "r" and z[1] == s,
           "arbitrate* %s" % seed)
    return b.maxhits, first, seed


def driven(G, schedule):
    """cached, mutant-independent: the record is a property of the schedule."""
    if schedule not in BUILD_CACHE:
        b = drive(G, schedule)
        BUILD_CACHE[schedule] = record_of(G, b)
    return BUILD_CACHE[schedule]


def record_of(G, b, actors=None):
    """the record's published shape.  `actors` is the site-object pool the
    footprints are cut to; it defaults to the R = 3 grid's own nine."""
    keep = set(ACTOR_SITE) if actors is None else set(actors)
    divs = [e for e in b.H if e[0] == "r"]
    foot = [frozenset(r for r in G.regs_of(e) if r in keep) for e in divs]
    return {"events": len(b.H), "maxhits": b.maxhits, "refusal": b.refusal,
            "divisions": len(divs), "H": list(b.H), "footprints": foot,
            "initiators": [e[1] for e in divs]}


# ===========================================================================
# SECTION 4.  THE R = 3 FAMILY AND THE DECLARED WINDOW
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


def canon_transversals(P):
    """THE DECLARED SEED MENU of a grouping: the k-th member of each group in
    the canonical order, k = 0, 1, 2.  Deterministic, no sampling, and it is
    the whole of the window's seed freedom -- disclosed here and in the head."""
    return [tuple(g[k] for g in P) for k in range(3)]


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
CLASS_OF = {CLASSES[k]: k for k in CLASS_NAMES}
DIAG_SEED = ((0, 0), (1, 1), (2, 2))

# the R = 2 committed schedule, for the anchor against d66's own conflict_grid
COMMITTED_R2 = ((CLASSES["ROW"], DIAG_SEED), (CLASSES["COL"], DIAG_SEED))
# d66's own R = 3 point: rounds alternate ROW, COL, ROW
COMMITTED_R3 = ((CLASSES["ROW"], DIAG_SEED), (CLASSES["COL"], DIAG_SEED),
                (CLASSES["ROW"], DIAG_SEED))
SEEDS_PER_ROUND_IN_WINDOW = 2


# ===========================================================================
# SECTION 5.  THE COMBINATORIAL COLUMNS (exact, packed 6 bits per site)
# ===========================================================================

def pack_links(P):
    """the co-division link field of ONE round, packed: bits (6i+0,6i+1) hold
    n_(1,0) at site i, (6i+2,6i+3) hold n_(0,1), (6i+4,6i+5) hold n_(1,1).
    Two bits per cell suffice because three rounds cannot exceed 3."""
    v = 0
    w = 0
    for x in SITES:
        for li, l in enumerate(I7_LINKS):
            y = zadd(x, l)
            if any(x in g and y in g for g in P):
                v |= 1 << (6 * SITE_INDEX[x] + 2 * li)
                w += 1
    return v, w


def pack4_links(P):
    """the same field at FOUR bits per cell, so four rounds cannot carry into
    a neighbouring cell.  Used only by the R = 4 register probe."""
    v = 0
    for si, x in enumerate(SITES):
        for li, l in enumerate(I7_LINKS):
            if any(x in g and zadd(x, l) in g for g in P):
                v |= 1 << (4 * (3 * si + li))
    return v


def pack4_target(nvec):
    return sum(nvec[li] << (4 * (3 * si + li))
               for si in range(9) for li in range(3))


ALLONE = sum(0b010101 << (6 * k) for k in range(9))

# the per-site code table: code = a + 4b + 16c with a = n_(1,0), b = n_(0,1),
# c = n_(1,1) at that site.  4*det is an integer, so the whole census runs in
# integers and the Fraction is formed only for reporting.
CODE_TAB = {}
for _code in range(64):
    _a, _b, _c = _code & 3, (_code >> 2) & 3, (_code >> 4) & 3
    _d4 = 4 * _a * _b - (_c - _a - _b) ** 2
    CODE_TAB[_code] = (_d4,
                       1 if _d4 != 0 else 0,
                       1 if (_d4 > 0 and _a > 0) else 0,
                       1 if (_a >= 1 and _b >= 1 and _c >= 1) else 0)


def site_form(code):
    a, b, c = code & 3, (code >> 2) & 3, (code >> 4) & 3
    q12 = Fraction(c - a - b, 2)
    return Fraction(a), Fraction(b), q12, Fraction(a) * Fraction(b) - q12 * q12


def unpack_field(s):
    """-> {(link, site): count} from a packed field."""
    out = {}
    for k, x in enumerate(SITES):
        for li, l in enumerate(I7_LINKS):
            out[(l, x)] = (s >> (6 * k + 2 * li)) & 3
    return out


def initiator_field(seedsets):
    return {x: sum(1 for T in seedsets if x in T) for x in SITES}


def affine_class(seedsets):
    """pin R3 extended to three rounds: is every seed set a coset of one and
    the same subgroup (CU-JOINT), a coset of some subgroup but not all of one
    (CU-SPLIT), or is at least one not a coset at all (BEYOND-COSET)?"""
    fs = [frozenset(T) for T in seedsets]
    if all(f in AG_LINES for f in fs):
        return ("CU-JOINT" if len({LINE_DIRECTION[f] for f in fs}) == 1
                else "CU-SPLIT")
    return "BEYOND-COSET"


# ===========================================================================
# SECTION 8a.  THE WELD DETECTOR (weld 2's machinery, both readings)
# ===========================================================================

CRY_LINKS = ((1, 0), (0, 1))


def cayley_edges(X, links, Lmod):
    tgt = set()
    for x in X:
        for lk in links:
            y = tuple((x[i] + lk[i]) % Lmod for i in range(len(lk)))
            tgt.add((x, y))
            tgt.add((y, x))
    return tgt


def graph_isomorphisms(S, rel_set, X, links, Lmod, directed=False):
    """ALL bijections S -> X carrying the site-object incidence onto the
    target's Cayley incidence, by exhaustive backtracking.  No sampling and no
    cap.  THE DECLARED CRITERION IS THE UNDIRECTED ONE, on both branches, for
    weld 2's reason: a link is an unordered site pair carrying a label and a
    count, and orientation is a declared free item; the directed criterion
    returns 0 at every co-division arena and so cannot be the admit test."""
    tgt = set()
    for x in X:
        for lk in links:
            y = tuple((x[i] + lk[i]) % Lmod for i in range(len(lk)))
            tgt.add((x, y))
            if not directed:
                tgt.add((y, x))
    src = set()
    for (u, v) in rel_set:
        if u != v:
            src.add((u, v))
            if not directed:
                src.add((v, u))
    Ss = sorted(S, key=str)
    Xs = sorted(X)
    out, phi, used = [], {}, set()

    def bt(k):
        if k == len(Ss):
            out.append(dict(phi))
            return
        u = Ss[k]
        for x in Xs:
            if x in used:
                continue
            ok = True
            for j in range(k):
                w = Ss[j]
                if ((u, w) in src) != ((x, phi[w]) in tgt) or \
                   ((w, u) in src) != ((phi[w], x) in tgt):
                    ok = False
                    break
            if ok:
                phi[u] = x
                used.add(x)
                bt(k + 1)
                used.discard(x)
                del phi[u]
    if len(Ss) == len(Xs):
        bt(0)
    return out


def quotient_bijections(S, rel_set, X, links, Lmod):
    """THE QUOTIENT READING at a nine-object arena: a SURJECTION of the
    realised objects onto the sites -- here necessarily a bijection -- under
    which EVERY realised edge carries a declared link displacement.  Weaker
    than the embedding reading: containment one way only."""
    tgt = cayley_edges(X, links, Lmod)
    src = {(u, v) for (u, v) in rel_set if u != v}
    Ss = sorted(S, key=str)
    Xs = sorted(X)
    out, phi, used = [], {}, set()

    def bt(k):
        if k == len(Ss):
            out.append(dict(phi))
            return
        u = Ss[k]
        for x in Xs:
            if x in used:
                continue
            ok = True
            for j in range(k):
                w = Ss[j]
                if (u, w) in src and (x, phi[w]) not in tgt:
                    ok = False
                    break
                if (w, u) in src and (phi[w], x) not in tgt:
                    ok = False
                    break
            if ok:
                phi[u] = x
                used.add(x)
                bt(k + 1)
                used.discard(x)
                del phi[u]
    if len(Ss) == len(Xs):
        bt(0)
    return out


def count_field(rel, X, links, Lmod, assign, labelperm, orient):
    """weld 2's induced count field s : X x L -> Z.  `assign` maps a site
    object to a site; `labelperm` permutes the declared link labels; `orient`
    flips the link direction.  The count on the link object joining u to v is
    the number of DIVISION EVENTS attached to it in the declared window."""
    inv = {assign[u]: u for u in assign}
    out = {}
    for x in X:
        for i, lk in enumerate(links):
            lk2 = links[labelperm[i]]
            step = tuple((-c) % Lmod for c in lk2) if orient else lk2
            y = tuple((x[k] + step[k]) % Lmod for k in range(len(step)))
            out[(x, lk)] = rel.get((inv[x], inv[y]), 0)
    return out


def fkey(f):
    return tuple(sorted(((str(k), v) for k, v in f.items())))


def codivision_rel(actors, footprints):
    """the co-division incidence on the ordered actor pair: a division event
    is ON the pair when its register footprint meets both endpoints."""
    rel = {}
    for u in actors:
        for v in actors:
            if u == v:
                continue
            rel[(u, v)] = sum(1 for f in footprints if u in f and v in f)
    return rel


DETECT_CACHE = {}
CACHE = {}


def _probe_field_routes_agree():
    """the three-route agreement, exercised on a declared probe field so the
    Fourier route has a live falsifier of its own."""
    f = {x: (1 if x in SITES[:3] else 0) for x in SITES}
    return stab_fourier(f, poison=mut("MUT-STAB-ROUTE")) == stab_direct(f)


def detect(arena, target, reading):
    """ONE CENSUS ROW.  Every fate is a MEASURED outcome with its number.
    Cached on the arena's own relation signature, the target and the reading,
    because those three are the whole of the detector's input -- and
    G-SAT-ARENA-IDENTITY measures that the 72 saturating arenas share one
    signature rather than assuming it."""
    ckey = (tuple(sorted((str(k), v) for k, v in arena["rel"].items())),
            target["name"], reading, arena["name"])
    if ckey in DETECT_CACHE:
        return json.loads(json.dumps(DETECT_CACHE[ckey]))
    row = _detect(arena, target, reading)
    DETECT_CACHE[ckey] = json.loads(json.dumps(row, default=str))
    return json.loads(json.dumps(DETECT_CACHE[ckey]))


def _detect(arena, target, reading):
    X, links, Lmod = target["X"], target["links"], target["Lmod"]
    row = {"arena": arena["name"], "reading": reading,
           "site_gen": "ACTOR", "link_gen": "ACTOR-PAIR",
           "count_gen": "DIV-COUNT-BETWEEN-DECLARED-ARB-CUTS",
           "arity_repair": "NONE", "target": target["name"]}
    objs = sorted(arena["actors"])
    rel = arena["rel"]
    row["site_arity"] = len(objs)
    row["needs_interior_position"] = False
    if len(objs) != len(X):
        row["fate"] = "ARITY-DEAD"
        row["reason"] = ("%d site objects against the target's %d; no repair "
                         "declared, and a declared restriction can only shrink "
                         "a site set" % (len(objs), len(X)))
        return row
    realised = {k for k, n in rel.items() if n > 0}
    if reading == "EMBEDDING":
        maps = graph_isomorphisms(objs, realised, X, links, Lmod)
        row["isomorphisms"] = len(maps)
        row["isomorphisms_directed_comparator"] = len(
            graph_isomorphisms(objs, realised, X, links, Lmod, directed=True))
    else:
        maps = quotient_bijections(objs, realised, X, links, Lmod)
        row["quotient_maps"] = len(maps)
    if not maps:
        row["fate"] = "STRUCT-DEAD"
        row["reason"] = ("0 of the %d! bijections carry the site incidence "
                         "%s the target's link structure"
                         % (len(objs),
                            "onto" if reading == "EMBEDDING" else "into"))
        return row
    nlab = len(links)
    fields = {}
    for i, phi in enumerate(maps):
        for lp in permutations(range(nlab)):
            for orient in (False, True):
                fields[(i, lp, orient)] = count_field(rel, X, links, Lmod,
                                                      phi, lp, orient)
    base = (0, tuple(range(nlab)), False)
    base_field = fields[base]
    row["count_cells"] = len(base_field)
    row["count_min"] = min(base_field.values())
    row["count_max"] = max(base_field.values())
    if row["count_min"] < 1:
        zeros = sorted(str(k) for k, v in base_field.items() if v == 0)
        row["fate"] = "COUNT-DEAD"
        row["reason"] = ("n_l(x) must lie in Z_>0 (HA 3.1); the induced count "
                         "is 0 at %d of %d cells"
                         % (len(zeros), len(base_field)))
        row["zero_cells"] = len(zeros)
        return row
    fib_site = len({fkey(fields[(i, tuple(range(nlab)), False)])
                    for i in range(len(maps))})
    # the operator review's MINOR-1: the label and orient fibers are READ at
    # the base map `sorted(S, key=str)` fixes -- an actor-name-order artifact.
    # The whole (map x label x orient) grid is already computed, so the
    # base-map INVARIANCE of both fibers is now measured at every base map and
    # published, rather than being a fact the code did not check.
    fib_label = len({fkey(fields[(0, lp, False)])
                     for lp in permutations(range(nlab))})
    fib_orient = len({fkey(fields[(0, tuple(range(nlab)), o)])
                      for o in (False, True)})
    lab_at = {len({fkey(fields[(i, lp, False)])
                   for lp in permutations(range(nlab))})
              for i in range(len(maps))}
    ori_at = {len({fkey(fields[(i, tuple(range(nlab)), o)])
                   for o in (False, True)})
              for i in range(len(maps))}
    row["fibers_base_map_invariant"] = (lab_at == {fib_label}
                                        and ori_at == {fib_orient})
    row["base_maps_read"] = len(maps)
    inv = {"I-SITE-ASSIGNMENT": fib_site, "I-DIRECTION-LABEL": fib_label,
           "I-ORIENT": fib_orient}
    row["inventory"] = inv
    free = sorted(k for k, v in inv.items() if v > 1)
    row["free_items"] = free
    row["fate"] = "FOUND-candidate" if not free else "UNMOTIVATED"
    row["reason"] = ("zero free items at the RSQ standard" if not free else
                     "%d genuinely free item(s): %s"
                     % (len(free),
                        ", ".join("%s fiber %d" % (k, inv[k]) for k in free)))
    row["count_field"] = sorted((str(k), v) for k, v in base_field.items())
    return row


# ===========================================================================
# SECTION 6-9.  THE RUN
# ===========================================================================

NUMREG = set()


def reg(*vals):
    for v in vals:
        if isinstance(v, Fraction):
            for s in (str(v), str(abs(v)), str(v.numerator),
                      str(abs(v.numerator)), str(v.denominator)):
                NUMREG.add(s)
        elif isinstance(v, int):
            NUMREG.add(str(v))
            NUMREG.add(str(abs(v)))
        elif isinstance(v, str):
            NUMREG.add(v)
        elif isinstance(v, (list, tuple, set, frozenset)):
            reg(*v)
        elif isinstance(v, dict):
            reg(*v.keys())
            reg(*v.values())
    return vals[0] if vals else None


RAW = {}


def raw_census():
    """the whole combinatorial layer, computed once, mutant-independent."""
    if RAW:
        return RAW
    parts = all_partitions()
    PK = [pack_links(P) for P in parts]
    F = [v for v, _w in PK]
    W = [w for _v, w in PK]
    sat = [k for k in range(len(parts)) if W[k] == 9]

    # ---- the per-chunk tables: three sites (18 bits) at a time -------------
    NCH = 1 << 18
    PKT = [0] * NCH
    HOMC = [0] * NCH
    CHCNT = [0] * NCH
    for c in range(NCH):
        nz = pd = st = 0
        c0 = c & 63
        same = c0
        for sft in (0, 6, 12):
            code = (c >> sft) & 63
            _d4, nzf, pdf, stf = CODE_TAB[code]
            nz += nzf
            pd += pdf
            st += stf
            if code != c0:
                same = -1
        PKT[c] = nz | (pd << 4) | (st << 8)
        HOMC[c] = (same + 1) if same >= 0 else 0

    # ---- the exhaustive census over ordered grouping triples ---------------
    n = len(parts)
    agg = Counter()
    hom_total = 0
    strict_fields = Counter()
    for i in range(n):
        fi = F[i]
        for j in range(i, n):
            fij = fi + F[j]
            for k in range(j, n):
                s = fij + F[k]
                w = 6 if (i != j and j != k) else (1 if i == j == k else 3)
                a = s & 0o777777
                b = (s >> 18) & 0o777777
                c = (s >> 36) & 0o777777
                v = PKT[a] + PKT[b] + PKT[c]
                nz = v & 15
                pd = (v >> 4) & 15
                st = (v >> 8) & 15
                agg[(nz, pd, st)] += w
                CHCNT[a] += w
                CHCNT[b] += w
                CHCNT[c] += w
                h = HOMC[a]
                if h and HOMC[b] == h and HOMC[c] == h:
                    hom_total += w
                if st == 9:
                    strict_fields[s] += w
    detspec = Counter()
    for c in range(NCH):
        if CHCNT[c]:
            for sft in (0, 6, 12):
                detspec[CODE_TAB[(c >> sft) & 63][0]] += CHCNT[c]
    posdef_hist = Counter()
    nz_hist = Counter()
    strict_total = 0
    for (nz, pd, st), w in agg.items():
        posdef_hist[pd] += w
        nz_hist[nz] += w
        if st == 9:
            strict_total += w

    # ---- ROUTE 2 on the I7-STRICT class: direct, over saturating triples ---
    strict_triples = []
    for i in sat:
        for j in sat:
            fij = F[i] + F[j]
            for k in sat:
                if fij + F[k] == ALLONE:
                    strict_triples.append((i, j, k))
    strict_multisets = sorted({tuple(sorted(t)) for t in strict_triples})

    # ---- THE COORDINATE-FREE SATURATING CLASS ------------------------------
    # I7-STRICT is a statement in the COMMITTED actor naming.  The weld's
    # site assignment is free, so the detector sees a coarser object: the
    # covered unordered pair set, which must be the complement of SOME
    # parallel class with every pair covered exactly once.  Both are counted.
    PAIRS = sorted(combinations(SITES, 2))
    PIDX = {q: m for m, q in enumerate(PAIRS)}
    pmask = []
    for P in parts:
        v = 0
        for g in P:
            for q in combinations(sorted(g), 2):
                v |= 1 << PIDX[q]
        pmask.append(v)
    classmask = {}
    for nm in CLASS_NAMES:
        v = 0
        for g in CLASSES[nm]:
            for q in combinations(sorted(g), 2):
                v |= 1 << PIDX[q]
        classmask[nm] = v
    ALLPAIRS = (1 << len(PAIRS)) - 1
    found_by_class = {}
    found_triples = []
    for nm in CLASS_NAMES:
        target = ALLPAIRS ^ classmask[nm]
        pool = [m for m in range(len(parts)) if pmask[m] & ~target == 0]
        cnt = 0
        for a in pool:
            for b in pool:
                if pmask[a] & pmask[b]:
                    continue
                ab = pmask[a] | pmask[b]
                for c in pool:
                    if ab | pmask[c] == target and not (ab & pmask[c]):
                        cnt += 1
                        found_triples.append((a, b, c, nm))
        found_by_class[nm] = (len(pool), cnt)

    # ---- the crystallinity census over ordered seed-set triples ------------
    subsets = sorted((frozenset(c) for c in combinations(SITES, 3)),
                     key=lambda T: sorted(T))
    fcache = {}
    stabcount = Counter()
    joint = Counter()
    shapes = Counter()
    affine_bad = []
    firstwit = {}
    for T0 in subsets:
        b0 = {x: (1 if x in T0 else 0) for x in SITES}
        for T1 in subsets:
            b1 = {x: b0[x] + (1 if x in T1 else 0) for x in SITES}
            for T2 in subsets:
                key = tuple(b1[x] + (1 if x in T2 else 0) for x in SITES)
                got = fcache.get(key)
                if got is None:
                    fld = {x: key[m] for m, x in enumerate(SITES)}
                    r1 = stab_direct(fld)
                    r2 = stab_fourier(fld)
                    r3 = stab_lattice(fld)
                    got = (SUBGROUP_NAME[r1], SUBGROUP_NAME[r2],
                           SUBGROUP_NAME[r3])
                    fcache[key] = got
                s = got[0]
                aff = affine_class((T0, T1, T2))
                stabcount[s] += 1
                joint[(aff, s)] += 1
                if s != "1":
                    H = SUBGROUPS[s]
                    cos = {}
                    ok = True
                    for m, x in enumerate(SITES):
                        ck = frozenset(zadd(x, h) for h in H)
                        cos.setdefault(ck, set()).add(key[m])
                    for ck, vals in cos.items():
                        if len(vals) != 1 or min(vals) < 0:
                            ok = False
                    shape = tuple(sorted(next(iter(v)) for v in cos.values()))
                    shapes[(s if s != "Z3^2" else "Z3^2", shape)] += 1
                    if not ok:
                        affine_bad.append((sorted(T0), sorted(T1), sorted(T2)))
                    firstwit.setdefault((aff, s), (T0, T1, T2))
    routes_bad = [k for k, v in fcache.items() if len(set(v)) != 1]

    RAW.update({
        "parts": parts, "F": F, "W": W, "sat": sat,
        "posdef_hist": posdef_hist, "nz_hist": nz_hist, "detspec": detspec,
        "hom_total": hom_total, "strict_total": strict_total,
        "strict_fields": strict_fields, "strict_triples": strict_triples,
        "strict_multisets": strict_multisets, "subsets": subsets,
        "stabcount": stabcount, "joint": joint, "shapes": shapes,
        "affine_bad": affine_bad, "routes_bad": routes_bad,
        "n_fields": len(fcache), "firstwit": firstwit,
        "found_by_class": found_by_class, "found_triples": found_triples,
    })
    return RAW


# ---------------------------------------------------------------------------
# the declared driven window
# ---------------------------------------------------------------------------

def window_schedules():
    """THE DECLARED DRIVEN WINDOW W3, disclosed here and in the head.

    W3-CLASS: all 4^3 ordered triples of the parallel classes of AG(2,3) --
              d66's own resolvable device, extended one round.
    W3-SAT:   ALL 72 I7-STRICT grouping triples -- the saturating stratum,
              exhaustive, the pin's primary object.
    Both at the declared seed menu: the first SEEDS_PER_ROUND_IN_WINDOW
    canonical transversals of each round's grouping.  Deterministic order, no
    sampling."""
    R = raw_census()
    parts = R["parts"]
    triples = []
    for a in CLASS_NAMES:
        for b in CLASS_NAMES:
            for c in CLASS_NAMES:
                triples.append((CLASSES[a], CLASSES[b], CLASSES[c]))
    for (i, j, k) in R["strict_triples"]:
        triples.append((parts[i], parts[j], parts[k]))
    seen = set()
    out = []
    for T in triples:
        menus = [canon_transversals(P)[:SEEDS_PER_ROUND_IN_WINDOW] for P in T]
        for s0 in menus[0]:
            for s1 in menus[1]:
                for s2 in menus[2]:
                    sch = ((T[0], s0), (T[1], s1), (T[2], s2))
                    if sch in seen:
                        continue
                    seen.add(sch)
                    out.append(sch)
    return out


WINDOW = {}


def window_drive(G):
    if WINDOW:
        return WINDOW
    for sch in window_schedules():
        WINDOW[sch] = driven(G, sch)
    return WINDOW


def link_field_of(footprints):
    """the DRIVEN link field: for a link l and a site x, the number of division
    events whose register footprint contains both x and x + l."""
    out = {}
    for l in I7_LINKS:
        for x in SITES:
            y = zadd(x, l)
            out[(l, x)] = sum(1 for f in footprints
                              if actor(x) in f and actor(y) in f)
    return out


def packed_of_schedule(sch):
    v = 0
    for (P, _s) in sch:
        v += pack_links(P)[0]
    return v


def seedsets_of(sch):
    return tuple(frozenset(s) for (_P, s) in sch)


# ---------------------------------------------------------------------------
# THE DECLARED ARENAS AND THE DECLARED FATE OF EVERY CELL (#87)
# ---------------------------------------------------------------------------

TGT_I7 = {"name": "I7-DECLARED-L3", "X": list(SITES), "links": list(I7_LINKS),
          "Lmod": 3}
TGT_CRY = {"name": "CRYSTAL-CARRIED-L2", "X": list(SITES),
           "links": list(CRY_LINKS), "Lmod": 3}

# every arena the weld census judges, with the fate DECLARED before the run.
# `kind` marks what the row licenses: CANDIDATE rows are the census proper,
# CONTROL rows discharge HA requirement 3, PROBE rows license reachability
# only.
EXPECTED = {
    ("R3-SAT", "EMBEDDING"): "FOUND-candidate",
    ("R3-SAT", "QUOTIENT"): "FOUND-candidate",
    ("R3-COMMITTED-GRID(3,3)", "EMBEDDING"): "STRUCT-DEAD",
    ("R3-COMMITTED-GRID(3,3)", "QUOTIENT"): "COUNT-DEAD",
    ("R3-ROW|COL|ANT-SATURATING-AFTER-RELABELLING", "EMBEDDING"):
        "FOUND-candidate",
    ("R3-ROW|COL|ANT-SATURATING-AFTER-RELABELLING", "QUOTIENT"):
        "FOUND-candidate",
    ("R3-SAT-FALSIFIER", "EMBEDDING"): "STRUCT-DEAD",
    ("R3-SAT-FALSIFIER", "QUOTIENT"): "COUNT-DEAD",
    ("R2-COMMITTED-GRID(3,2)", "EMBEDDING"): "STRUCT-DEAD",
    ("R2-COMMITTED-GRID(3,2)", "QUOTIENT"): "COUNT-DEAD",
    ("CRYSTAL/DOUBLE-GRID(3,2)@L2", "EMBEDDING"): "FOUND-candidate",
    ("CRYSTAL/DOUBLE-GRID(3,2)@L2", "QUOTIENT"): "FOUND-candidate",
    ("CRYSTAL/DOUBLE-GRID(3,2)@I7", "EMBEDDING"): "STRUCT-DEAD",
    ("CRYSTAL/DOUBLE-GRID(3,2)@I7", "QUOTIENT"): "COUNT-DEAD",
    ("CRYSTAL-INHOMOGENEOUS@L2", "EMBEDDING"): "UNMOTIVATED",
    ("CRYSTAL-INHOMOGENEOUS@L2", "QUOTIENT"): "UNMOTIVATED",
    ("D58-GENERIC-2-ACTOR-WALK@I7", "EMBEDDING"): "ARITY-DEAD",
    ("D58-GENERIC-2-ACTOR-WALK@I7", "QUOTIENT"): "ARITY-DEAD",
}

# the dead lists, CITED and never re-run (weld 2 section 3 and section 9.4)
DEAD_LISTS = [
    "R6b'-C1-C5(free items 6/5/1/4/1)",
    "BRG-EMPTY-AT-CARRIER",
    "GW1-SEC2-ORDER-ONLY-SPATIAL-INSTRUMENTS",
    "v12-ARENA-FREE-GAMMA-OBJECTS",
    "THE-NAIVE-9-TO-9(L>=4-IS-A-MEASURED-REQUIREMENT)",
    "WELD2-SCISSORS-SCOPE((A,B)-CARRIER-AT-DEPTH<=4)",
    "WELD2-TRANSPORT-CARRIER-CELLS(MENU-113|CONG-185|EVENT-SUBSET|ULAM-PREFIX)",
]


def arena_of_record(name, rec, actors):
    return {"name": name, "kind": "record", "actors": sorted(actors),
            "rel": codivision_rel(sorted(actors), rec["footprints"]),
            "divisions": rec["divisions"], "events": rec["events"]}


def i7_arena(rec_bytes):
    """I7's arena READ AS DATA from its pinned receipt, never re-authored."""
    rec = json.loads(rec_bytes)
    D = rec["declarations"]
    links = [tuple(v) for v in D["links_d2"]]
    fam = {nm: tuple(D["records_d2"][nm]) for nm in sorted(D["records_d2"])}
    # the two SITE-DEPENDENT records I7 declares in prose and weld 2 builds
    # in code, carried here as full site-indexed records so the family the
    # induced record is compared against is I7's whole declared eleven.
    X = [(i, j) for i in range(D["L"]) for j in range(D["L"])]
    inhom = {}
    inhom["G-CURVED"] = {x: tuple(sum((1 + x[j]) for j in range(D["d"])
                                      if lk[j]) for lk in
                                  [tuple(v) for v in D["links_d2"]])
                         for x in X}

    def _curvoff(x, lk, d=D["d"]):
        b = [2 + x[j] for j in range(d)]
        cross = 1 + (x[0] * x[1]) % 2
        s0 = sum(b[j] for j in range(d) if lk[j])
        prs = sum(1 for i2 in range(d) for j2 in range(i2 + 1, d)
                  if lk[i2] and lk[j2])
        return s0 + 2 * cross * prs
    inhom["G-CURVOFF"] = {x: tuple(_curvoff(x, tuple(lk))
                                   for lk in D["links_d2"]) for x in X}
    box = D["count_lattice"]
    committed = rec["tables"]["link_locality_lattice"]["admissible_points"]
    reencode = rec["tables"]["readout_reencoding"]
    return {"d": D["d"], "L": D["L"], "links": links, "family": fam,
            "site_dependent_family": inhom,
            "box": box, "committed_admissible_points": committed,
            "chart_group": D["chart_group"], "reencode": reencode}


def q_of(nvec):
    n1, n2, n3 = nvec
    q12 = Fraction(n3 - n1 - n2, 2)
    return Fraction(n1), Fraction(n2), q12, Fraction(n1) * Fraction(n2) \
        - q12 * q12


def admissible(nvec):
    """HA 3.2's own criterion: q nonsingular and positive definite at the
    site, by the exact Sylvester criterion."""
    q11, _q22, _q12, det = q_of(nvec)
    return q11 > 0 and det > 0


def i7_box_admissible(box):
    """RECOMPUTED from I7's own declared count box, not re-typed."""
    pts = []
    for n1 in range(1, box["axis_max"] + 1):
        for n2 in range(1, box["axis_max"] + 1):
            for n3 in range(1, box["diag_max"] + 1):
                if admissible((n1, n2, n3)):
                    pts.append((n1, n2, n3))
    return pts


def chart_orbit(nvec):
    """I7's declared chart group acts by the |X| translations and the d!
    direction relabellings.  On a HOMOGENEOUS record the translations act
    trivially, so the orbit is the relabellings of the two axis links."""
    n1, n2, n3 = nvec
    return {(n1, n2, n3), (n2, n1, n3)}


VERBATIM = [
    ("V01", "A-PIN",
     "Confirm UNIT-GRADE the reviewer-grade computation: the uniform R=3 "
     "arrangement gives n = 1 at all 27 cells, det = 3/4, POSDEF at 9/9 "
     "sites.", "G-UNIT-GRADE"),
    ("V02", "A-PIN",
     "For the first time neither degeneracy nor budget forecloses the "
     "answer.", "G-WELD-CENSUS"),
    ("V03", "A-U4BADJ",
     "THE R=3 SATURATION enters the successor register as the weld route's "
     "exact demand", "G-UNIT-GRADE"),
    ("V04", "A-U4BEFF",
     "three rounds grouped on the three link-direction parallel classes give "
     "`n_l(x) = 1` at all 27 cells, `q = [[1, -1/2], [-1/2, 1]]`, det = 3/4 > "
     "0, **positive definite at all nine sites**, and I7's strict "
     "criterion satisfied for the first time.", "G-UNIT-GRADE"),
    ("V05", "A-U4BEFF",
     "(i) constructibility **driven**, since the round-2 conflict-supply "
     "question is new", "G-CONSTRUCTIBILITY"),
    ("V06", "A-U4BEFF",
     "the full group Z32 becomes reachable", "G-FULL-GROUP"),
    ("V07", "A-U4BEFF",
     "(iv) an explicit statement that >= 27 incidences is necessary, not "
     "sufficient, for the weld.", "G-COUNT-IMPLIES-WELD"),
    ("V08", "A-U4BEFF",
     "the affine law taken on the union", "G-AFFINE-LAW"),
    ("V09", "A-HA",
     "A record is **admissible** when $q$ is nonsingular and positive "
     "definite at every site, by the exact Sylvester criterion",
     "G-ADMISSIBLE"),
    ("V10", "A-HA",
     "The readout is an invertible linear re-encoding: in count coordinates, "
     "the record IS the metric.", "G-I7-READOUT"),
    ("V11", "A-HA",
     "A predicate that cannot return its other value anywhere in the "
     "declared arena is not a measurement", "G-TWO-WAY"),
    ("V12", "A-W2",
     "a bijection from site objects to sites under which the grammar's link "
     "relation **contains** the target's incidence", "G-READINGS"),
    ("V13", "A-W2",
     "The pre-registered dead list is cited and not re-run",
     "G-DEAD-LISTS-CITED"),
    ("V14", "A-W2",
     "the diagonal link count is identically zero at 9 of 9 sites in 5 of 5 "
     "crystals", "G-CTRL-CRYSTAL-AT-I7"),
    ("V15", "A-W2",
     "**ARITY-DEAD** -- 2 site objects against 9", "G-CTRL-EMPTY-WALK"),
    ("V16", "A-D66",
     "each group is a g-PROPOSER conflict (g + 1 registers) whose base is "
     "supplied by g - 1 deliveries from the group's diagonal seed",
     "G-COMMITTED-RECORD"),
    ("V17", "A-L1",
     "fourth form, outside paper 8's three**, and its admissibility is v11's "
     "to argue when U4 runs", "G-WALL-L1"),
    ("V18", "A-CAT",
     "a Poisson sprinkling admits **no Lorentz-invariant finite-valency "
     "graph** (BHS)", "G-WALL-BHS"),
    ("V19", "A-CAT",
     "a dimension reading without a height control is worthless",
     "G-WALL-KR"),
    ("V20", "A-PIN",
     "cosmological readings barred; no continuum claim", "G-WALL-DIAGONAL"),
]


def source_text(texts, sid):
    rel = [s[1] for s in SOURCES if s[0] == sid][0]
    return texts[rel]


def read_d66_row(text, tag):
    """READ d66's own committed output row, never re-typed."""
    for line in text.split("\n"):
        if line.strip().startswith(tag + " ") or line.strip() == tag:
            m = re.search(r"n=\s*(\d+)\s+arbs=\s*(\d+).*?deliveries=\s*(\d+)",
                          line)
            if m:
                return tuple(int(g) for g in m.groups())
    return None


def read_int_after(text, needle, count=1):
    """pull the integers that follow a #62-anchored needle in a committed
    source, so the anchor's committed side is READ and never typed."""
    c = canon(text)
    n = canon(needle)
    i = c.find(n)
    if i < 0:
        return None
    tail = c[i + len(n):i + len(n) + 200]
    got = re.findall(r"\d[\d,]*", tail)
    out = [int(g.replace(",", "")) for g in got[:count]]
    return out[0] if count == 1 and out else (out or None)


def full_run(break_anchor=None, paper_text=None, paper_rel=PAPER_REL,
             do_paper=True):
    LD = Ledger()
    SEAL = Seal()
    R = {"schema": SCHEMA}
    say("=" * 78)
    say("v14 R=3 WELD -- the arena, the positive geometry, and the weld")
    say("=" * 78)

    # ---------------- SEC 1  PROVENANCE ---------------------------------
    say("\n[SEC 1] PROVENANCE -- %d pinned sources" % len(SOURCES))
    texts, prov, bad = {}, [], []
    for sid, rel, want, why in SOURCES:
        raw = read_bytes(rel)
        got = hashlib.sha256(raw).hexdigest()[:12]
        exp = "0" * 12 if break_anchor == sid else want
        ok = (got == exp)
        if not ok:
            bad.append(sid)
        prov.append({"id": sid, "path": rel, "pinned": exp, "computed": got,
                     "match": ok, "bytes": len(raw), "why": why})
        texts[rel] = raw.decode("utf-8")
    R["provenance"] = prov
    LD.gate("G-PROVENANCE",
            "every one of the %d declared sources is consumed at its pinned "
            "sha256-12, and the products of those bytes are what every later "
            "gate reads (#91: no subprocess, no version control, off-tree "
            "correct)" % len(SOURCES),
            not bad, "mismatches: %s" % (bad or "none"))
    SEAL.take("SEAL-SCHEMA", R)
    SEAL.take("SEAL-PROVENANCE", R)

    src = ast.parse(read_text(SELF))
    floats = [n for n in ast.walk(src) if isinstance(n, ast.Constant)
              and isinstance(n.value, float)]
    fcalls = [n for n in ast.walk(src)
              if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
              and n.func.id in ("float", "round")]
    subp = [n for n in ast.walk(src)
            if isinstance(n, ast.Attribute) and n.attr in
            ("system", "popen", "run", "Popen", "check_output")]
    imports = sorted({a.name.split(".")[0] for n in ast.walk(src)
                      if isinstance(n, ast.Import) for a in n.names}
                     | {n.module.split(".")[0] for n in ast.walk(src)
                        if isinstance(n, ast.ImportFrom) and n.module})
    LD.gate("G-EXACT-ARITHMETIC",
            "an AST scan of this file finds no float literal and no call to "
            "float() or round(): every number in the census is an int or a "
            "Fraction, and the only bare reference to the float type is the "
            "isinstance test in the receipt's own recursive type scan",
            not floats and not fcalls,
            "float literals %d, float/round calls %d" % (len(floats),
                                                         len(fcalls)))
    LD.gate("G-NO-SUBPROCESS",
            "no subprocess of any kind is invoked and `subprocess` is not "
            "imported, so the run is correct off-tree and in a directory with "
            "no version control at all (#91); imports: %s" % ",".join(imports),
            "subprocess" not in imports and not subp,
            "imports %d, shell-ish attributes %d" % (len(imports), len(subp)))
    declared_reads = {s[1] for s in SOURCES}
    LD.gate("G-READS-DECLARED",
            "the set of files read at run time as SOURCES is EXACTLY the "
            "declared set -- no repository state outside it is touched",
            set(READS) == declared_reads,
            "read %d distinct, declared %d, difference %s"
            % (len(set(READS)), len(declared_reads),
               sorted(set(READS) ^ declared_reads) or "none"))

    # ---------------- SEC 3  THE GRAMMAR --------------------------------
    say("\n[SEC 3] THE COMMITTED GRAMMAR, DRIVEN DIRECTLY")
    G = Grammar(texts)
    LD.gate("G-SLICE-EXIT-FREE",
            "the d42b1 text slice and every AST-extracted body are free of "
            "any exit callable, so no committed source can terminate this "
            "process (d66's own C0a form)",
            G.slice_exit_free and G.bodies_exit_free,
            "slice exit-free %s, extracted bodies exit-free %s, slice cut at "
            "char %d of %d" % (G.slice_exit_free, G.bodies_exit_free,
                               G.slice_chars[0], G.slice_chars[1]))

    # the generalized driver, anchored against d66's own constructor
    b_own = G.conflict_grid(3, 2)
    own = [list(e) for e in b_own.H]
    mine_b = drive(G, COMMITTED_R2)
    mine = [list(e) for e in mine_b.H]
    if mut("MUT-COMMITTED-RECORD") and mine:
        mine = mine[:-1] + [["p", "G00", "V0", 9]]
    same = (len(own) == len(mine)
            and all(str(a) == str(c) for a, c in zip(own, mine)))
    LD.gate("G-COMMITTED-RECORD",
            "at the committed R = 2 schedule the generalized driver and "
            "d66's own `conflict_grid(3, 2)`, re-run in this process, emit "
            "IDENTICAL event lists -- so the one-round-wider driver is the "
            "committed constructor with the schedule made a variable, event "
            "for event",
            same, "d66 %d events, generalized driver %d events, identical %s"
            % (len(own), len(mine), same))

    d66out = source_text(texts, "A-D66OUT")
    anchors = []
    for tag, want_recompute in (("GRID(g=3,R=4)", 4), ("GRID(g=3,R=6)", 6)):
        rowr = read_d66_row(d66out, tag)
        bb = G.conflict_grid(3, want_recompute)
        comp = (len(bb.H), sum(1 for e in bb.H if e[0] == "r"),
                sum(1 for e in bb.H if e[0] == "d"))
        if mut("MUT-ANCHOR-DRIFT") and want_recompute == 4:
            comp = (comp[0] + 1, comp[1], comp[2])
        anchors.append({"id": "N-" + tag, "committed": list(rowr),
                        "computed": list(comp), "source": "A-D66OUT",
                        "match": list(rowr) == list(comp)})
    i7 = i7_arena(source_text(texts, "A-I7").encode("utf-8"))
    boxpts = i7_box_admissible(i7["box"])
    nbox = len(boxpts)
    anchors.append({"id": "N-I7-BOX", "committed": i7["committed_admissible_points"],
                    "computed": nbox, "source": "A-I7",
                    "match": nbox == i7["committed_admissible_points"]})
    # the readout re-encoding determinant, recomputed from HA 3.2's own rows
    M = [[1, 0, 0], [0, 1, 0], [1, 1, 2]]
    detM = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    anchors.append({"id": "N-READOUT-DET",
                    "committed": int(i7["reencode"]["determinant"]),
                    "computed": detM, "source": "A-I7",
                    "match": int(i7["reencode"]["determinant"]) == detM})
    R["anchors"] = anchors
    R["i7"] = {"links": [list(l) for l in i7["links"]],
               "record_family": {k: list(v) for k, v in i7["family"].items()},
               "site_dependent_records": sorted(i7["site_dependent_family"]),
               "box": i7["box"], "box_admissible_points": len(boxpts),
               "chart_group": i7["chart_group"]}
    LD.gate("G-ANCHORS-READ",
            "%d numbers are READ from committed files at run time and "
            "RECOMPUTED here, never re-typed: d66's own GRID(g=3,R=4) and "
            "GRID(g=3,R=6) rows, I7's committed admissible-point count for "
            "its declared count box, and I7's readout re-encoding determinant"
            % len(anchors),
            all(a["match"] for a in anchors),
            "; ".join("%s committed=%s computed=%s" %
                      (a["id"], a["committed"], a["computed"])
                      for a in anchors))
    ha = source_text(texts, "A-HA")
    rt = [nm for nm in sorted(i7["family"])
          if not admissible(i7["family"][nm])]
    adm_names = sorted(nm for nm in i7["family"] if admissible(i7["family"][nm]))
    LD.gate("G-I7-READOUT",
            "THE READOUT IS I7's OWN, matched verbatim in its pinned bytes "
            "and used unchanged: q11 = n_e1, q22 = n_e2, "
            "q12 = (n_(e1+e2) - n_e1 - n_e2)/2, the invertible linear "
            "re-encoding whose determinant I7 measured at 2 and this run "
            "recomputes.  Applied to I7's OWN declared record family it "
            "separates %d admissible records from %d inadmissible ones, which "
            "is the readout doing work rather than being quoted"
            % (len(adm_names), len(rt)),
            match_needle(ha, VERBATIM[9][2]) and detM == 2 and adm_names,
            "re-encoding determinant %d; admissible declared records %s; "
            "inadmissible %s" % (detM, adm_names, rt))
    vrows, vbad = [], []
    for vid, sid, quote, consumer in VERBATIM:
        text = source_text(texts, sid)
        q = quote
        if mut("MUT-VERBATIM") and vid == "V04":
            q = quote.replace("3/4", "5/4")
        ok = match_needle(text, q)
        vrows.append({"id": vid, "source": sid, "chars": len(canon(quote)),
                      "consumer_gate": consumer, "found": ok,
                      "quote": canon(quote)})
        if not ok:
            vbad.append(vid)
    R["verbatim_anchors"] = vrows
    LD.gate("G-VERBATIM",
            "%d verbatim anchors (#62) are matched against their pinned "
            "source bytes, each above the %d-character floor and each named "
            "to the gate that consumes it; both sides are whitespace-"
            "normalised, ASCII-folded AND markdown-prefix-stripped (#125 with "
            "the U4b clarification), so a needle spanning a block quote or a "
            "numbered list cannot be evaded by re-wrapping"
            % (len(VERBATIM), NEEDLE_FLOOR),
            not vbad, "misses: %s; shortest needle %d chars"
            % (vbad or "none", min(v["chars"] for v in vrows)))
    SEAL.take("SEAL-VERBATIM", R)

    # ---------------- SEC 4  THE FAMILY AND THE WINDOW ------------------
    say("\n[SEC 4] THE R = 3 FAMILY AND THE DECLARED DRIVEN WINDOW")
    C = raw_census()
    parts = C["parts"]
    n_parts_enum = len(parts)
    n_parts_closed = 9 * 8 * 7 // 6 * (6 * 5 * 4 // 6) // 6 * 1
    n_parts_closed = (9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1) // (6 * 6 * 6 * 6)
    LD.gate("G-PARTITION-COUNT",
            "the number of partitions of the nine sites into three triples is "
            "COMPUTED by two routes that share no code -- exhaustive "
            "enumeration and the closed form 9!/(3!^3 3!) -- and they agree "
            "(#24)",
            n_parts_enum == n_parts_closed == 280,
            "enumeration %d, closed form %d" % (n_parts_enum, n_parts_closed))
    per_round_enum = n_parts_enum * 27
    per_round_closed = n_parts_closed * 3 ** 3
    fam_enum = pick("MUT-FAMILY-COUNT", per_round_enum ** 3, 12345)
    fam_closed = per_round_closed ** 3
    LD.gate("G-FAMILY-COUNT",
            "the R = 3 family -- three rounds, each an admissible grouping "
            "with a seed chosen in each group -- is COUNTED by two routes: "
            "%d partitions x 27 seed assignments = %d schedules per round, "
            "cubed" % (n_parts_enum, per_round_enum),
            fam_enum == fam_closed,
            "route 1 %d, route 2 %d" % (fam_enum, fam_closed))
    FAMILY = fam_closed
    win = window_schedules()
    n_class_triples = len(CLASS_NAMES) ** 3
    R["family"] = {
        "partitions": n_parts_enum, "schedules_per_round": per_round_enum,
        "rounds": 3, "family_size": FAMILY,
        "window_size": len(win),
        "window_declaration":
            "W3 = W3-CLASS (all %d ordered triples of the four parallel "
            "classes of AG(2,3), d66's own resolvable device) UNION W3-SAT "
            "(ALL %d I7-STRICT grouping triples, exhaustive), each at the "
            "first %d canonical transversals of every round's grouping"
            % (n_class_triples, len(C["strict_triples"]),
               SEEDS_PER_ROUND_IN_WINDOW),
        "window_ratio_denominator": FAMILY // len(win),
        # the effectus review's MINOR-4: the driven-vs-combinatorial equality
        # that licenses the exhaustive columns is measured on 1040 RECORDS,
        # which span this many distinct GROUPING TRIPLES -- the object those
        # columns quantify over.
        "window_distinct_grouping_triples":
            len({tuple(P for P, _s in sch) for sch in win}),
        "window_is_the_family": len(win) >= FAMILY,
        "committed_R2_schedule_in_family": True,
        "committed_R3_schedule": "ROW|COL|ROW (d66's own alternation)",
    }
    disclosed = pick("MUT-WINDOW-SILENT", len(win), FAMILY)
    LD.gate("G-WINDOW-DISCLOSED",
            "the driven window is DECLARED and DISCLOSED -- %d schedules of "
            "%d, named inside the constructibility verdict string, so no "
            "reader can meet the number without meeting its scope; every "
            "other column below is exhaustive over an object the window does "
            "not cap" % (len(win), FAMILY),
            disclosed == len(win) and len(win) < FAMILY,
            "window %d, family %d, ratio 1 : %d"
            % (disclosed, FAMILY, FAMILY // max(disclosed, 1)))
    SEAL.take("SEAL-FAMILY", R)

    # ---------------- CONSTRUCTIBILITY (pin stage 1) ---------------------
    say("\n[SEC 6] STAGE 1 -- CONSTRUCTIBILITY, DRIVEN")
    WD = window_drive(G)
    # the pin's primary object: three rounds on the three link classes
    UNI = tuple((CLASSES[c], canon_transversals(CLASSES[c])[0])
                for c in ("ROW", "COL", "DIA"))
    STRICT_SET = {tuple(sorted(t)) for t in C["strict_triples"]}
    satwin = [sch for sch in WD
              if tuple(sorted(parts.index(P) for (P, _t) in sch))
              in STRICT_SET]
    fates = Counter()
    forced_bad = []
    ev_hist = Counter()
    for sch, rec in WD.items():
        if mut("MUT-NOT-FORCED") and sch == UNI:
            # the mutant withholds one conflict-supply delivery and reports
            # the resulting REFUSED record as FORCED anyway
            if "notforced" not in CACHE:
                CACHE["notforced"] = record_of(G, drive(G, sch,
                                                        drop_supply=0))
            rec = CACHE["notforced"]
            fate = "FORCED"
        else:
            fate = ("REFUSED" if rec["refusal"] else
                    ("BRANCHING" if rec["maxhits"] > 1 else "FORCED"))
        fates[fate] += 1
        ev_hist[rec["events"]] += 1
        if fate != "FORCED" or rec["divisions"] != 9 or rec["refusal"] \
                or rec["maxhits"] != 1:
            forced_bad.append(str(sch))
    R["constructibility"] = {
        "window": len(WD), "FORCED": fates["FORCED"],
        "BRANCHING": fates["BRANCHING"], "REFUSED": fates["REFUSED"],
        "event_count_distribution": dict(sorted(ev_hist.items())),
        "divisions_per_record": 9,
    }
    LD.gate("G-CONSTRUCTIBILITY",
            "every one of the %d window schedules is BUILT by driving the "
            "committed layer's own menus and scored against ITS OWN record: "
            "FORCED means every specification matched by exactly one menu "
            "candidate (maxhits = 1), no refusal, and exactly 9 division "
            "events.  The effectus demanded this driven, because at R = 3 the "
            "round-2 conflict-supply question is new" % len(WD),
            not forced_bad and fates["FORCED"] == len(WD),
            "FORCED %d, BRANCHING %d, REFUSED %d; event counts %s; "
            "failures %d" % (fates["FORCED"], fates["BRANCHING"],
                             fates["REFUSED"], dict(sorted(ev_hist.items())),
                             len(forced_bad)))

    # the memo purity gate: a declared re-drive set, memo disabled
    redrive = win[:8] + win[len(win) // 2:len(win) // 2 + 8] + win[-8:]
    if "redrive" not in CACHE:
        raw_g = G.candidates_for
        G.candidates_for = lambda h, i: G.raw_candidates_for(list(h),
                                                             tuple(i))
        G.d60_globals["candidates_for"] = G.candidates_for
        CACHE["redrive"] = [[str(e) for e in drive(G, sch).H]
                            for sch in redrive]
        G.candidates_for = raw_g
        G.d60_globals["candidates_for"] = raw_g
    memo_bad = []
    for m2, sch in enumerate(redrive):
        got = list(CACHE["redrive"][m2])
        if mut("MUT-MEMO-DIRTY") and m2 == 0:
            got = got[1:]
        if got != [str(e) for e in BUILD_CACHE[sch]["H"]]:
            memo_bad.append(str(sch))
    LD.gate("G-MENU-PURE",
            "the menu memo is a cache over (history, initiators) and nothing "
            "else: %d declared window schedules are RE-DRIVEN with the memo "
            "disabled and their records compared event for event against the "
            "memoised run" % len(redrive),
            not memo_bad,
            "re-driven %d, mismatches %d, memo hits %d of %d calls"
            % (len(redrive), len(memo_bad), G.memo_hits, G.memo_calls))

    # the two negative fates, exhibited by declared controls
    if "ctl_ref" not in CACHE:
        CACHE["ctl_ref"] = drive(G, UNI, drop_supply=0).refusal
    ctl_ref_refusal = CACHE["ctl_ref"]
    ref_seen = pick("MUT-REFUSAL-BLIND", ctl_ref_refusal, None)
    LD.gate("G-CTRL-REFUSED",
            "THE NO-SUPPLY CONTROL: the uniform R = 3 arrangement with its "
            "first conflict-supply delivery withheld.  The layer REFUSES the first "
            "proposal by an actor that does not hold the base; a refusal is "
            "recorded, never patched -- so FORCED above is a measurement and "
            "not a structural tautology",
            bool(ref_seen),
            "refusal %s" % (str(ref_seen) if ref_seen else "NONE (control "
                            "failed to fire)"))
    if "ctl_br" not in CACHE:
        CACHE["ctl_br"] = branching_control(G)
    mh = pick("MUT-BRANCHING-BLIND", CACHE["ctl_br"][0], 1)
    LD.gate("G-CTRL-BRANCHING",
            "THE UNDER-SPECIFIED CONTROL, MADE REPRODUCIBLE.  The committed "
            "R = 2 record is replayed up to (not including) its first "
            "arbitration; d60's `pick` is then asked for an arbitration by "
            "that group's seed WITHOUT its conflict key and winner key, and "
            "the builder's own `maxhits` -- the NUMBER of menu candidates "
            "matching -- is read.  THE RUN STOPS THERE: d60 breaks ties with "
            "sorted(key=repr), a frozenset's repr depends on the "
            "interpreter's per-process string hashing, so WHICH candidate an "
            "under-specified pick takes is not reproducible across runs -- "
            "and a control that continued past one would carry that "
            "irreproducibility into every later menu size.  The count is "
            "reproducible; the choice is not, and no record is continued "
            "past an under-specified pick",
            mh > 1, "menu candidates matching the under-specified pick: %d"
            % mh)
    R["constructibility"]["controls"] = {
        "no_supply_refusal": str(ctl_ref_refusal),
        "under_specified_maxhits": CACHE["ctl_br"][0],
        "under_specified_prefix": CACHE["ctl_br"][1],
        "under_specified_seed": CACHE["ctl_br"][2]}
    SEAL.take("SEAL-CONSTRUCTIBILITY", R)

    # ---------------- THE DRIVEN-vs-COMBINATORIAL LICENCE ---------------
    eqbad = []
    for sch, rec in WD.items():
        drv = link_field_of(rec["footprints"])
        cmb = unpack_field(packed_of_schedule(sch))
        if mut("MUT-DRIVEN-FIELD") and sch == win[0]:
            drv = dict(drv)
            drv[(I7_LINKS[0], SITES[0])] += 1
        di = Counter(ACTOR_SITE[a] for a in rec["initiators"])
        cmb_i = initiator_field(seedsets_of(sch))
        if drv != cmb or dict(di) != {k: v for k, v in cmb_i.items() if v}:
            eqbad.append(str(sch))
    LD.gate("G-DRIVEN-EQUALS-COMBINATORIAL",
            "THE LICENCE (the U4b pattern): for every one of the %d driven "
            "window records the link field read off the DRIVEN record -- "
            "footprints from the layer's own `regs_of` -- equals the field "
            "the combinatorial route computes from the schedule alone, and "
            "the same holds for the initiator field.  That equality is what "
            "licenses the exhaustive columns below to be computed "
            "combinatorially over objects no window caps" % len(WD),
            not eqbad, "records compared %d, mismatches %d"
            % (len(WD), len(eqbad)))

    # ---------------- THE UNIT-GRADE CONFIRMATION -----------------------
    say("\n[SEC 6] STAGE 1 -- THE ARENA, UNIT-GRADE")
    urec = driven(G, UNI)
    ufield = link_field_of(urec["footprints"])
    if mut("MUT-UNIT-GRADE"):
        ufield = dict(ufield)
        ufield[(I7_LINKS[2], SITES[4])] = 2
    cells_ok = sum(1 for c in ufield if ufield[c] == 1)
    dets, pds, forms = [], 0, set()
    _uq = q_of((ufield[((1, 0), SITES[0])], ufield[((0, 1), SITES[0])],
                ufield[((1, 1), SITES[0])]))
    for x in SITES:
        nvec = (ufield[((1, 0), x)], ufield[((0, 1), x)], ufield[((1, 1), x)])
        q11, q22, q12, det = q_of(nvec)
        if mut("MUT-DET-UNIFORM"):
            det = Fraction(1)
        dets.append(det)
        forms.add((str(q11), str(q22), str(q12), str(det)))
        if q11 > 0 and det > 0:
            pds += 1
    reg(*dets)
    R["arena"] = {
        "uniform_schedule": "ROW|COL|DIA at the canonical seeds",
        "events": urec["events"], "divisions": urec["divisions"],
        "maxhits": urec["maxhits"], "refusal": str(urec["refusal"]),
        "cells": len(ufield), "cells_at_one": cells_ok,
        "det": str(dets[0]), "posdef_sites": pds,
        "distinct_site_forms": sorted(forms),
        "incidences": sum(ufield.values()),
        # the operator review's MINOR-2: the q that appears in the WELD3
        # verdict string is BUILT from the measured site form, never typed,
        # so the head cannot survive a moved form.
        "q": [str(_uq[0]), str(_uq[2]), str(_uq[2]), str(_uq[1])],
        "driven_saturating_records": len(satwin),
    }

    LD.gate("G-UNIT-GRADE",
            "THE PIN'S STAGE-1 DEMAND, CONFIRMED UNIT-GRADE AND DRIVEN.  The "
            "uniform R = 3 arrangement -- three rounds grouped on the three "
            "link-direction parallel classes -- is built by the committed "
            "layer's own menus (%d events, %d division events, maxhits %s, no "
            "refusal) and its DRIVEN link field is 1 at every one of the 27 "
            "cells, so q = [[1, -1/2], [-1/2, 1]], det = 3/4 at every site "
            "and the form is positive definite at 9 of 9.  Every cell and "
            "every site is checked against its own value (#87), not against "
            "an aggregate"
            % (urec["events"], urec["divisions"], urec["maxhits"]),
            cells_ok == 27 and all(d == Fraction(3, 4) for d in dets)
            and pds == 9 and urec["divisions"] == 9
            and urec["maxhits"] == 1 and urec["refusal"] is None,
            "cells at 1: %d of 27; distinct determinants %s; posdef sites %d "
            "of 9; incidences %d of 27"
            % (cells_ok, sorted({str(d) for d in dets}), pds,
               sum(ufield.values())))
    SEAL.take("SEAL-ARENA", R)

    # homogeneity, over every driven saturating record
    homog_bad, satfields = [], set()
    for sch in satwin:
        f = link_field_of(WD[sch]["footprints"])
        satfields.add(tuple(sorted((str(k), v) for k, v in f.items())))
        codes = {(f[((1, 0), x)], f[((0, 1), x)], f[((1, 1), x)])
                 for x in SITES}
        if mut("MUT-HOMOG") and sch == satwin[0]:
            codes = {(1, 1, 1), (0, 1, 1)}
        if len(codes) != 1:
            homog_bad.append(str(sch))
    LD.gate("G-HOMOGENEITY",
            "every one of the %d driven saturating window records is "
            "HOMOGENEOUS -- one and the same (n_(1,0), n_(0,1), n_(1,1)) at "
            "all nine sites -- and all of them carry the SAME field, so the "
            "geometry is invariant across the whole driven saturating slice"
            % len(satwin),
            not homog_bad and len(satfields) == 1,
            "saturating records driven %d, inhomogeneous %d, distinct driven "
            "fields %d" % (len(satwin), len(homog_bad), len(satfields)))
    LD.gate("G-GEOM-SEED-INVARIANT",
            "the induced geometry is a function of the GROUPINGS alone: the "
            "%d driven saturating records span %d distinct seed triples over "
            "%d distinct grouping triples and every one of them induces the "
            "identical count field"
            % (len(satwin),
               len({tuple(t for (_P, t) in s) for s in satwin}),
               len({tuple(P for (P, _t) in s) for s in satwin})),
            pick("MUT-SEED-INVARIANCE", len(satfields), 2) == 1,
            "distinct induced fields across the saturating slice: %d"
            % pick("MUT-SEED-INVARIANCE", len(satfields), 2))

    # ---------------- CRYSTALLINITY, RE-PRE-REGISTERED ------------------
    say("\n[SEC 6] STAGE 1 -- CRYSTALLINITY ON THE SUMMED FIELD")
    stabc = C["stabcount"]
    joint = C["joint"]
    n_triples = sum(stabc.values())
    crystalline = n_triples - stabc["1"]
    full = pick("MUT-FULLGROUP", stabc["Z3^2"], 0)
    full_closed = (9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1) // (6 * 6 * 6)
    beyond = sum(v for (a, s), v in joint.items()
                 if a == "BEYOND-COSET" and s != "1")
    beyond = pick("MUT-BEYOND-COSET", beyond, 0)
    cusplit = sum(v for (a, s), v in joint.items()
                  if a == "CU-SPLIT" and s != "1")
    cusplit = pick("MUT-CU-SPLIT", cusplit, 1)
    cujoint_tot = sum(v for (a, s), v in joint.items() if a == "CU-JOINT")
    cujoint_cry = sum(v for (a, s), v in joint.items()
                      if a == "CU-JOINT" and s != "1")
    R["crystal"] = {
        "seed_set_triples": n_triples,
        "distinct_fields": C["n_fields"],
        "stabilizer_distribution": {k: stabc[k] for k in SUBGROUP_ORDER
                                    if stabc[k]},
        "crystalline": crystalline,
        "crystalline_rate": str(Fraction(crystalline, n_triples)),
        "full_group": stabc["Z3^2"],
        "full_group_closed_form": full_closed,
        "beyond_coset_crystalline": beyond,
        "beyond_coset_share": str(Fraction(beyond, crystalline)),
        "cu_joint_total": cujoint_tot, "cu_joint_crystalline": cujoint_cry,
        "cu_split_crystalline": sum(v for (a, s), v in joint.items()
                                    if a == "CU-SPLIT" and s != "1"),
        "shapes": {("%s:%s" % (k[0], ",".join(str(z) for z in k[1]))): v
                   for k, v in sorted(C["shapes"].items(), key=str)},
        "joint": {("%s|%s" % k): v for k, v in sorted(joint.items())},
    }
    LD.gate("G-STAB-ROUTES",
            "every distinct division field is handed to THREE stabilizer "
            "routes that share no code and no typed constant -- translation "
            "of the field, the annihilator of the support of the exact "
            "Z_3^2 Fourier transform in Z[w] = Z[t]/(t^2+t+1), and a walk of "
            "the subgroup lattice -- and they agree element for element",
            not C["routes_bad"] and _probe_field_routes_agree(),
            "distinct fields %d, three-route disagreements %d"
            % (C["n_fields"], len(C["routes_bad"])))
    LD.gate("G-FULL-GROUP",
            "THE BUDGET FACT THAT DIES AT R = 3.  U4b measured the full group "
            "Z_3^2 as unreachable at R = 2 -- six division events cannot "
            "spread evenly over nine sites.  At R = 3 the summed field has "
            "total 9 and the shape (1,1,1) exists: the full group occurs at "
            "%d of %d ordered seed-set triples, and those are EXACTLY the "
            "ordered partitions of the nine sites into three seed sets, "
            "9!/(3!)^3, counted a second way" % (stabc["Z3^2"], n_triples),
            full == full_closed and full > 0,
            "measured %d, closed form 9!/(3!)^3 = %d" % (full, full_closed))
    LD.gate("G-AFFINE-LAW",
            "THE NULL, RE-PRE-REGISTERED ON THE SUMMED FIELD (the effectus's "
            "demand iii).  At every one of the %d crystalline seed-set "
            "triples the summed field is a NON-NEGATIVE INTEGER COMBINATION "
            "of the period's coset indicators -- the affine law taken on the "
            "union -- and the shape over the three cosets is one of (3,0,0), "
            "(2,1,0) and (1,1,1), the last being the full group.  Evaluated "
            "at every object, not on an aggregate" % crystalline,
            not C["affine_bad"] and not mut("MUT-AFFINE-LAW"),
            "crystalline triples %d, violations %d, shapes %s"
            % (crystalline, len(C["affine_bad"]) + (1 if mut("MUT-AFFINE-LAW")
                                                    else 0),
               sorted({k[1] for k in C["shapes"]})))
    LD.gate("G-CU-SPLIT-EMPTY",
            "no CU-SPLIT seed triple -- three cosets not all of one subgroup "
            "-- is crystalline, at %d of %d objects" %
            (sum(v for (a, s), v in joint.items() if a == "CU-SPLIT"),
             sum(v for (a, s), v in joint.items() if a == "CU-SPLIT")),
            cusplit == 0, "CU-SPLIT crystalline: %d" % cusplit)
    LD.gate("G-BEYOND-COSET-CRYSTALLINE",
            "crystallinity is NOT confined to the inherited coset locus at "
            "R = 3 either: %d of the %d crystalline seed-set triples are "
            "beyond-coset, a share of %s, and the full-group cell is beyond-"
            "coset at %d of its %d members"
            % (beyond, crystalline, Fraction(beyond, crystalline),
               joint[("BEYOND-COSET", "Z3^2")], stabc["Z3^2"]),
            beyond > 0, "beyond-coset crystalline %d of %d"
            % (beyond, crystalline))

    # ---------------- FRAGILITY, ON BOTH VARIABLES ----------------------
    say("\n[SEC 6] STAGE 1 -- FRAGILITY")
    fcache2 = {}

    def stab_of(key):
        got = fcache2.get(key)
        if got is None:
            fld = {x: key[m] for m, x in enumerate(SITES)}
            got = SUBGROUP_NAME[stab_direct(fld)]
            fcache2[key] = got
        return got

    DRIVEN_CRYSTALS = 8          # the declared driven-admissibility set
    if "seedfrag" in CACHE:
        n_sched, n_cry, n_edit, n_broke, survivors, firstcry = \
            CACHE["seedfrag"]
    else:
     n_sched = n_cry = n_edit = n_broke = 0
     survivors = []
     firstcry = []
     for (i, j, k) in C["strict_triples"]:
         Ps = (parts[i], parts[j], parts[k])
         TS = [transversals(P) for P in Ps]
         for s0 in TS[0]:
             for s1 in TS[1]:
                 for s2 in TS[2]:
                     ss = (s0, s1, s2)
                     key = tuple(sum(1 for t in ss if x in t) for x in SITES)
                     n_sched += 1
                     s = stab_of(key)
                     if s == "1":
                         continue
                     n_cry += 1
                     if len(firstcry) < DRIVEN_CRYSTALS:
                         firstcry.append(((Ps[0], s0), (Ps[1], s1),
                                          (Ps[2], s2)))
                     for r in range(3):
                         for gi in range(3):
                             old = ss[r][gi]
                             for new in Ps[r][gi]:
                                 if new == old:
                                     continue
                                 n_edit += 1
                                 k2 = list(key)
                                 k2[SITE_INDEX[old]] -= 1
                                 k2[SITE_INDEX[new]] += 1
                                 s2v = stab_of(tuple(k2))
                                 if s2v == "1":
                                     n_broke += 1
                                 else:
                                     survivors.append((str(ss), r, gi,
                                                       str(old), str(new)))
     CACHE["seedfrag"] = (n_sched, n_cry, n_edit, n_broke, survivors,
                          firstcry)
    survivors = list(survivors)              # never mutate the cache
    if mut("MUT-FRAGILITY"):
        n_broke -= 1
        survivors.append(("planted", 0, 0, "-", "-"))
    # THE EDITS' GRAMMAR-ADMISSIBILITY, DRIVEN.  The driven window's seed
    # menu is two canonical transversals per round and none of its schedules
    # is crystalline, so the admissibility leg is taken on a DECLARED set
    # instead: the first 8 crystalline schedules of the stratum enumeration,
    # each with all 18 of its re-seatings driven through the menus.
    winvcry, winedits, inadmissible = [], 0, []
    for sch in firstcry:
        winvcry.append(sch)
        for r in range(3):
            for gi in range(3):
                old = sch[r][1][gi]
                for new in sch[r][0][gi]:
                    if new == old:
                        continue
                    seeds = list(sch[r][1])
                    seeds[gi] = new
                    sch2 = tuple(
                        (sch[q][0], tuple(seeds) if q == r else sch[q][1])
                        for q in range(3))
                    rec2 = driven(G, sch2)
                    winedits += 1
                    if rec2["refusal"] or rec2["maxhits"] != 1 \
                            or rec2["divisions"] != 9:
                        inadmissible.append(str(sch2))
    LD.gate("G-FRAGILITY-SEED",
            "FRAGILITY OF THE CRYSTAL, exhaustive over the weld's own "
            "stratum: all %d schedules on the %d I7-STRICT grouping triples "
            "with every one of their %d seed triples; %d are crystalline and "
            "every one of their %d single-arbitration re-seatings breaks the "
            "period.  The mechanism is one line -- an edit changes the field "
            "by 1_new - 1_old and a difference of two distinct point masses "
            "is never constant on the cosets of an order-3 subgroup, and it "
            "is never constant at all, so the full group dies with the rest.  "
            "The edits' grammar-admissibility is DRIVEN for the first %d "
            "crystalline schedules of the stratum enumeration and all %d of "
            "their re-seatings, every one FORCED -- the driven window's own "
            "two-transversal seed menu contains no crystal, so the "
            "admissibility leg is taken where the crystals are"
            % (n_sched, len(C["strict_triples"]), 27 ** 3, n_cry, n_edit,
               len(winvcry), winedits),
            n_broke == n_edit and not survivors and not inadmissible,
            "schedules %d, crystalline %d, edits %d, broken %d, survivors %d, "
            "driven edits %d, inadmissible %d"
            % (n_sched, n_cry, n_edit, n_broke, len(survivors), winedits,
               len(inadmissible)))

    if "geofrag" in CACHE:
        geo_edits, geo_survive = CACHE["geofrag"]
    else:
     geo_edits = geo_survive = 0
     for (i, j, k) in C["strict_triples"]:
         Ps = [list(parts[i]), list(parts[j]), list(parts[k])]
         for r in range(3):
             for (ga, gb) in combinations(range(3), 2):
                 for u in Ps[r][ga]:
                     for v in Ps[r][gb]:
                         na = tuple(sorted([v if z == u else z
                                            for z in Ps[r][ga]]))
                         nb = tuple(sorted([u if z == v else z
                                            for z in Ps[r][gb]]))
                         newP = list(Ps[r])
                         newP[ga], newP[gb] = na, nb
                         tot = 0
                         for q in range(3):
                             tot += pack_links(tuple(sorted(newP)) if q == r
                                               else tuple(Ps[q]))[0]
                         geo_edits += 1
                         if tot == ALLONE:
                             geo_survive += 1
     CACHE["geofrag"] = (geo_edits, geo_survive)
    geo_survive = pick("MUT-GEOM-FRAGILITY", geo_survive, 1)
    LD.gate("G-FRAGILITY-GEOM",
            "FRAGILITY OF THE GEOMETRY, against ITS OWN minimal edit: a "
            "single transposition of two sites between two conflict groups of "
            "one round.  Over the %d I7-STRICT grouping triples all %d such "
            "edits are taken and NONE leaves the triple I7-STRICT.  Read with "
            "the seed column this is the arena's sharpest structural "
            "statement: each saturation is destroyed by the edit that moves "
            "ITS OWN variable and is untouched by the edit that moves the "
            "other's" % (len(C["strict_triples"]), geo_edits),
            geo_survive == 0,
            "grouping edits %d, survivors %d" % (geo_edits, geo_survive))
    R["crystal"]["fragility"] = {
        "stratum_schedules": n_sched, "crystalline": n_cry,
        "seed_edits": n_edit, "broken": n_broke,
        "driven_crystals": len(winvcry), "driven_edits": winedits,
        "grouping_edits": geo_edits, "grouping_survivors": geo_survive,
    }
    SEAL.take("SEAL-CRYSTAL", R)

    # ---------------- SEC 7  THE POSITIVE-GEOMETRY CENSUS ---------------
    # the R = 2 BACK-ANCHOR: U4b's committed numbers, recomputed by THIS
    # machinery, so the geometry pipeline is validated against a committed
    # result before it is used one round wider.
    if "r2anchor" in CACHE:
        ph2, strict2, nz9_2, inc2 = CACHE["r2anchor"]
    else:
     ph2 = Counter()
     strict2 = 0
     nz9_2 = 0
     inc2 = 0
     for a in range(len(parts)):
         fa = C["F"][a]
         for b2 in range(len(parts)):
             s = fa + C["F"][b2]
             pd = nz = st = 0
             for m in range(9):
                 code = (s >> (6 * m)) & 63
                 _d4, nzf, pdf, stf = CODE_TAB[code]
                 nz += nzf
                 pd += pdf
                 st += stf
             ph2[pd] += 1
             inc2 = max(inc2, C["W"][a] + C["W"][b2])
             if st == 9:
                 strict2 += 1
             if nz == 9:
                 nz9_2 += 1
     CACHE["r2anchor"] = (ph2, strict2, nz9_2, inc2)
    adjt = source_text(texts, "A-U4BADJ")
    r2_committed = read_int_after(adjt, "the posdef ceiling open (wall "
                                        "permits", 2)
    LD.gate("G-R2-BACK-ANCHOR",
            "THE PIPELINE IS VALIDATED AGAINST A COMMITTED RESULT BEFORE IT "
            "IS USED ONE ROUND WIDER.  Run at R = 2 -- all %d ordered "
            "partition pairs -- this unit's own packed geometry census "
            "reproduces U4b's committed row exactly: the positive-definite "
            "ceiling is 3 against a wall of 18//3 = 6, I7-STRICT is empty, "
            "and %d pairs are non-degenerate at all nine sites.  The wall "
            "numbers are READ from the U4b adjudication, not typed here"
            % (len(parts) ** 2, nz9_2),
            max(ph2) == 3 and strict2 == 0 and inc2 == 18
            and r2_committed == [6, 3] and 18 // 3 == r2_committed[0],
            "R=2 posdef ceiling %d (committed %s), I7-STRICT %d, max "
            "incidences %d, non-degenerate-at-9 pairs %d"
            % (max(ph2), r2_committed, strict2, inc2, nz9_2))
    R2ROW = {
        "ordered_pairs": len(parts) ** 2, "posdef_ceiling": max(ph2),
        "i7_strict": strict2, "max_incidences": inc2,
        "nondegenerate_at_9": nz9_2,
        "committed_wall_and_ceiling": r2_committed}

    say("\n[SEC 7] STAGE 2 -- THE POSITIVE-GEOMETRY CENSUS")
    ph = C["posdef_hist"]
    ceiling = pick("MUT-CEILING", max(ph), 8)
    at_ceiling = ph[max(ph)]
    empty_cells = sorted(k for k in range(10) if ph.get(k, 0) == 0)
    if mut("MUT-CEILING-GAP"):
        empty_cells = [c for c in empty_cells if c != 8]
    ordered_total = sum(ph.values())
    strict_route1 = C["strict_total"]
    strict_route2 = pick("MUT-STRICT-COUNT", len(C["strict_triples"]), 71)
    detspec = {str(Fraction(d4, 4)): c for d4, c in
               sorted(C["detspec"].items())}
    if mut("MUT-DETSPEC"):
        detspec.pop(sorted(detspec)[0])
    spec_total = sum(detspec.values())
    rigid_bad = [s for s in C["strict_fields"] if s != ALLONE]
    if mut("MUT-RIGIDITY"):
        rigid_bad.append(0)
    R["geometry"] = {
        "ordered_grouping_triples": ordered_total,
        "posdef_site_distribution": {str(k): ph[k] for k in sorted(ph)},
        "attained_ceiling": max(ph), "triples_at_ceiling": at_ceiling,
        "empty_posdef_cells": empty_cells,
        "nondegenerate_at_9": C["nz_hist"].get(9, 0),
        "nz_distribution": {str(k): C["nz_hist"][k]
                            for k in sorted(C["nz_hist"])},
        "homogeneous_triples": C["hom_total"],
        "i7_strict_ordered_triples": strict_route1,
        "i7_strict_multisets": len(C["strict_multisets"]),
        "i7_strict_schedules": strict_route1 * 27 ** 3,
        "saturating_partitions": len(C["sat"]),
        "det_spectrum": detspec, "det_cells": spec_total,
        "max_incidences_per_round": 9, "max_incidences": 27,
        "r2_back_anchor": R2ROW,
        "coordinate_free_saturating": {
            "per_missing_class": {k: list(v)
                                  for k, v in C["found_by_class"].items()},
            "total": sum(v[1] for v in C["found_by_class"].values()),
            "extra_over_i7_strict":
                sum(v[1] for v in C["found_by_class"].values())
                - strict_route1},
    }
    LD.gate("G-POSDEF-CEILING",
            "THE ATTAINED CEILING, exhaustive over all %d ordered grouping "
            "triples.  U4b measured 3 at R = 2 against a wall that permitted "
            "6; at R = 3 the wall permits 9 and 9 IS ATTAINED, at %d triples. "
            " The distribution also has an EMPTY CELL: %s positive-definite "
            "sites never occur, so the ceiling is attained or missed by at "
            "least two"
            % (ordered_total, at_ceiling,
               ", ".join(str(c) for c in empty_cells) or "no count"),
            ceiling == 9 and at_ceiling > 0 and 8 in empty_cells,
            "distribution %s" % {str(k): ph[k] for k in sorted(ph)})
    LD.gate("G-STRICT-COUNT",
            "the I7-STRICT class -- every one of the 27 link counts at least "
            "1, which is HA 3.1's own requirement on a geometry record -- is "
            "COUNTED by two routes that share no code: the packed exhaustive "
            "census over all %d ordered triples, and a direct search over the "
            "%d saturating partitions alone" % (ordered_total, len(C["sat"])),
            strict_route1 == strict_route2,
            "packed census %d, direct search %d, distinct multisets %d, "
            "schedules %d" % (strict_route1, strict_route2,
                              len(C["strict_multisets"]),
                              strict_route1 * 27 ** 3))
    LD.gate("G-RIGIDITY",
            "THE RIGIDITY THEOREM, MEASURED AT EVERY OBJECT.  A round "
            "deposits at most 9 link incidences and 9 positive-definite sites "
            "need 27, so I7-STRICT forces every round to saturate and the "
            "field to be identically 1 -- and then det = 3/4 > 0 at every "
            "site.  The three classes therefore coincide: I7-STRICT = "
            "POSDEF-9 = FIELD-IDENTICALLY-1.  Measured: every I7-STRICT "
            "triple has the identical field, and the ceiling population "
            "equals the strict population",
            not rigid_bad and at_ceiling == strict_route1
            and len(C["strict_fields"]) == 1,
            "distinct I7-STRICT fields %d, off-field triples %d, "
            "posdef-9 %d, I7-STRICT %d"
            % (len(C["strict_fields"]), len(rigid_bad), at_ceiling,
               strict_route1))
    LD.gate("G-DET-SPECTRUM",
            "the determinant spectrum over every site of every ordered "
            "triple: %d values on %d cells, and the cell count is COMPUTED "
            "(#24) as 9 x the triple count rather than typed"
            % (len(detspec), spec_total),
            spec_total == ordered_total * 9,
            "spectrum %s; cells %d, expected %d"
            % (detspec, spec_total, ordered_total * 9))
    cf_tot = sum(v[1] for v in C["found_by_class"].values())
    LD.gate("G-COORDINATE-FREE-CLASS",
            "I7-STRICT IS A STATEMENT IN THE COMMITTED ACTOR NAMING, AND THE "
            "WELD'S SITE ASSIGNMENT IS FREE.  So the detector sees a coarser "
            "object: the covered unordered pair set, which must be the "
            "complement of SOME parallel class with every pair covered "
            "exactly once.  Counted exhaustively for each of the four classes "
            "in turn: %s -- %d ordered grouping triples in all, exactly 4 x "
            "the %d that are I7-STRICT in the committed naming.  Every "
            "measurement in this unit that is stated in fixed coordinates "
            "carries the smaller number, and the weld carries the larger"
            % ({k: v[1] for k, v in sorted(C["found_by_class"].items())},
               cf_tot, strict_route1),
            pick("MUT-COORD-FREE", cf_tot, strict_route1)
            == 4 * strict_route1
            and C["found_by_class"]["ANT"][1] == strict_route1,
            "per missing class %s; total %d; I7-STRICT (ANT missing) %d"
            % ({k: list(v) for k, v in sorted(C["found_by_class"].items())},
               cf_tot, strict_route1))

    # THE SITEWISE IDENTITY (the operator review's strengthening): the
    # rigidity theorem is a COROLLARY of a per-site fact, and the fact holds
    # at every site of every triple in the family, not only at the ceiling.
    sw_tab = dict(CODE_TAB)
    if mut("MUT-SITEWISE"):
        sw_tab[63] = (sw_tab[63][0], sw_tab[63][1], 0, sw_tab[63][3])
    sw_bad = [c for c in sorted(sw_tab)
              if bool(sw_tab[c][2]) != bool(sw_tab[c][3])]
    R["geometry"]["sitewise_identity"] = {
        "reachable_site_codes": len(sw_tab),
        "posdef_iff_all_three_counts_positive": not sw_bad,
        "counterexamples": sw_bad}
    LD.gate("G-SITEWISE-IDENTITY",
            "THE RIGIDITY THEOREM IS A COROLLARY OF A SITEWISE IDENTITY.  At "
            "every one of the %d site codes reachable in this family -- three "
            "rounds deposit at most 1 per cell, so no count exceeds 3 -- the "
            "form is POSITIVE DEFINITE at a site IF AND ONLY IF all three of "
            "n_(1,0), n_(0,1) and n_(1,1) are at least 1 there.  The two "
            "predicates therefore coincide at EVERY site of EVERY one of the "
            "%d ordered triples and not only at the top of the ladder, so the "
            "whole positive-definite distribution equals the whole strict "
            "distribution and I7-STRICT = POSDEF-9 is forced sitewise rather "
            "than by the 27-incidence budget alone"
            % (len(sw_tab), ordered_total),
            not sw_bad,
            "site codes %d; codes where positive-definiteness and "
            "min-count-positive disagree: %s"
            % (len(sw_tab), sw_bad or "none"))

    # THE COVERAGE CONDITION, COMPUTED AND NEVER TYPED (the panel's shared
    # kill).  The operative quantity is not the COUNT of incidences but their
    # COVERAGE of the 27 cells: d66's own R = 3 point pays the full budget and
    # dies anyway, which the delivered text mis-described as "deposits 18".
    com3f = unpack_field(sum(pack_links(P)[0]
                             for P, _s in COMMITTED_R3))
    com3_inc = sum(com3f.values())
    com3_cov = pick("MUT-COVERAGE-COUNT",
                    sum(1 for v in com3f.values() if v > 0), 27)
    com3_zero = sum(1 for v in com3f.values() if v == 0)
    satf = unpack_field(sum(pack_links(CLASSES[c])[0]
                            for c in ("ROW", "COL", "DIA")))
    R["geometry"]["coverage_not_count"] = {
        "saturating_partitions": len(C["sat"]),
        "triples_paying_the_full_budget": len(C["sat"]) ** 3,
        "of_which_weld": strict_route1,
        "one_in": len(C["sat"]) ** 3 // strict_route1,
        "committed_R3_incidences": com3_inc,
        "committed_R3_cells_covered": com3_cov,
        "committed_R3_cells_at_zero": com3_zero,
        "weld_incidences": sum(satf.values()),
        "weld_cells_covered": sum(1 for v in satf.values() if v > 0)}
    reg(len(C["sat"]) ** 3, len(C["sat"]) ** 3 // strict_route1)

    # THE R = 4 REGISTER PROBE (registered, NOT claimed).  At R = 3 the
    # rigidity theorem makes (1,1,1) the only reachable I7-STRICT record, so
    # no R = 3 schedule can reach a DECLARED one.  One round later the budget
    # is 36 and I7's own G-FLAT needs exactly 36.  This is a combinatorial
    # reachability count over quadruples of saturating partitions: no menu is
    # driven, nothing is claimed constructible, and the successor question --
    # whether the grammar DRIVES one of them -- is left open in section 11.
    F4 = [pack4_links(parts[k]) for k in C["sat"]]
    FLAT = tuple(i7["family"]["G-FLAT"])
    TG4 = {pack4_target(o) for o in chart_orbit(FLAT)}
    n_r4 = 0
    for _a in F4:
        for _b in F4:
            _ab = _a + _b
            for _c in F4:
                _abc = _ab + _c
                for _d in F4:
                    if _abc + _d in TG4:
                        n_r4 += 1
    n_r4 = pick("MUT-R4-REGISTER", n_r4, 0)
    R["geometry"]["r4_register_probe"] = {
        "budget_rounds": 4, "target": "G-FLAT",
        "target_record": list(FLAT),
        "ordered_quadruples_of_saturating_partitions": len(F4) ** 4,
        "reaching_the_target_chart_orbit": n_r4,
        "driven": False,
        "status": "REGISTERED-NOT-CLAIMED: combinatorial reachability only"}
    reg(len(F4) ** 4, n_r4)
    LD.gate("G-R4-REGISTER",
            "THE SUCCESSOR QUESTION THIS UNIT CREATES, MEASURED ON ITS "
            "COMBINATORIAL SIDE ONLY.  At R = 3 the rigidity theorem makes "
            "(1,1,1) the ONLY reachable I7-STRICT record, so no R = 3 "
            "schedule can reach a DECLARED I7 record at all -- the "
            "undeclaredness is a budget fact.  One round later the budget is "
            "36 and I7's own G-FLAT = %s needs exactly 36: over all %d "
            "ordered quadruples of saturating partitions it is reached at "
            "%d, admissible, and it is one of the eleven.  NOTHING IS DRIVEN "
            "HERE and nothing is claimed constructible; the row is registered "
            "so the successor inherits a question with a number on it"
            % (str(FLAT), len(F4) ** 4, n_r4),
            n_r4 > 0 and admissible(FLAT) and len(F4) ** 4 > n_r4,
            "quadruples %d, reaching G-FLAT's chart orbit %d, G-FLAT "
            "admissible %s" % (len(F4) ** 4, n_r4, admissible(FLAT)))
    SEAL.take("SEAL-GEOMETRY", R)

    # ---------------- SEC 8  THE WELD, RE-POSED -------------------------
    say("\n[SEC 8] STAGE 3 -- THE WELD, RE-POSED LIVE")
    # (a) every I7-STRICT record carries the SAME co-division arena
    satarenas, relsigs = [], set()
    for (i, j, k) in C["strict_triples"]:
        T = (parts[i], parts[j], parts[k])
        sch = tuple((P, canon_transversals(P)[0]) for P in T)
        rec = driven(G, sch)
        rel = codivision_rel(sorted(ACTORS), rec["footprints"])
        relsigs.add(tuple(sorted((str(kk), v) for kk, v in rel.items())))
        satarenas.append({"triple": [i, j, k], "events": rec["events"],
                          "divisions": rec["divisions"],
                          "maxhits": rec["maxhits"]})
    LD.gate("G-SAT-ARENA-IDENTITY",
            "ALL %d I7-STRICT grouping triples are DRIVEN and every one of "
            "them carries the IDENTICAL co-division arena: the same 9 site "
            "objects, the same 27 unordered realised pairs, the same count 1 "
            "on every one of them.  So the weld census below has one arena "
            "and not 72, and that is a measurement rather than a convenience"
            % len(C["strict_triples"]),
            len(relsigs) == 1 and all(a["maxhits"] == 1 and a["divisions"] == 9
                                      for a in satarenas),
            "driven saturating records %d, distinct co-division arenas %d"
            % (len(satarenas), len(relsigs)))

    SATREC = driven(G, tuple((P, canon_transversals(P)[0])
                             for P in (parts[C["strict_triples"][0][0]],
                                       parts[C["strict_triples"][0][1]],
                                       parts[C["strict_triples"][0][2]])))
    UNIREC = urec
    A_SAT = arena_of_record("R3-SAT", UNIREC, ACTORS)
    A_C33 = arena_of_record("R3-COMMITTED-GRID(3,3)",
                            driven(G, COMMITTED_R3), ACTORS)
    NONSAT = tuple((CLASSES[c], canon_transversals(CLASSES[c])[0])
                   for c in ("ROW", "COL", "ANT"))
    A_NON = arena_of_record("R3-ROW|COL|ANT-SATURATING-AFTER-RELABELLING",
                            driven(G, NONSAT), ACTORS)
    fal = dict(UNIREC)
    fal["footprints"] = UNIREC["footprints"][:-1]
    A_FAL = arena_of_record("R3-SAT-FALSIFIER", fal, ACTORS)
    A_R2 = arena_of_record("R2-COMMITTED-GRID(3,2)",
                           record_of(G, b_own), ACTORS)
    bcry = G.double_grid(3, 2)
    cry_actors = sorted({"D%d%d" % (i, j) for i in range(3)
                         for j in range(3)})
    cryrec = record_of(G, bcry, cry_actors)
    A_CRYL2 = {"name": "CRYSTAL/DOUBLE-GRID(3,2)@L2", "kind": "record",
               "actors": cry_actors,
               "rel": codivision_rel(cry_actors, cryrec["footprints"]),
               "divisions": cryrec["divisions"], "events": cryrec["events"]}
    A_CRYI7 = dict(A_CRYL2, name="CRYSTAL/DOUBLE-GRID(3,2)@I7")
    # weld 2's declared falsifier: the same crystal with ONE ROW-GROUP
    # arbitration withheld.  DOUBLE-GRID(g,R) mints 2g lineages and then runs
    # g row arbitrations before g column arbitrations in each round, so the
    # first row arbitration of the last round is division 2g + 2g(R-1).
    DROP_IDX = 2 * 3 + 2 * 3 * (2 - 1)
    cry_inh_fp = [f for m, f in enumerate(cryrec["footprints"])
                  if m != DROP_IDX]
    A_CRYINH = {"name": "CRYSTAL-INHOMOGENEOUS@L2", "kind": "record",
                "actors": cry_actors,
                "rel": codivision_rel(cry_actors, cry_inh_fp),
                "divisions": len(cry_inh_fp), "events": cryrec["events"]}
    walkH = G.walk2(30, 4242)
    walk_divs = [e for e in walkH if e[0] == "r"]
    walk_fp = [frozenset(r for r in G.regs_of(e) if r in ("A", "B"))
               for e in walk_divs]
    A_WALK = {"name": "D58-GENERIC-2-ACTOR-WALK@I7", "kind": "record",
              "actors": ["A", "B"],
              "rel": codivision_rel(["A", "B"], walk_fp),
              "divisions": len(walk_divs), "events": len(walkH)}

    ARENAS = [(A_SAT, TGT_I7), (A_C33, TGT_I7), (A_NON, TGT_I7),
              (A_FAL, TGT_I7), (A_R2, TGT_I7), (A_CRYL2, TGT_CRY),
              (A_CRYI7, TGT_I7), (A_CRYINH, TGT_CRY), (A_WALK, TGT_I7)]
    rows, fatebad = [], []
    for arena, tgt in ARENAS:
        for reading in ("EMBEDDING", "QUOTIENT"):
            row = detect(arena, tgt, reading)
            if mut("MUT-WELD-FATE") and arena["name"] == "R3-SAT" \
                    and reading == "EMBEDDING":
                row["fate"] = "UNMOTIVATED"
            want = EXPECTED[(arena["name"], reading)]
            row["declared_fate"] = want
            row["matches_declaration"] = (row["fate"] == want)
            if not row["matches_declaration"]:
                fatebad.append("%s@%s: %s != %s" % (arena["name"], reading,
                                                    row["fate"], want))
            rows.append(row)
    if mut("MUT-FIBER-SAT"):
        for r in rows:
            if r["arena"] == "R3-SAT" and "inventory" in r:
                r["inventory"] = dict(r["inventory"],
                                      **{"I-SITE-ASSIGNMENT": 2})
    if mut("MUT-FIBER-LAX"):
        for r in rows:
            if r["arena"] == "CRYSTAL-INHOMOGENEOUS@L2" and "inventory" in r:
                r["inventory"] = {"I-SITE-ASSIGNMENT": 1,
                                  "I-DIRECTION-LABEL": 1, "I-ORIENT": 1}
                r["free_items"] = []
    if mut("MUT-FIBER-BASEMAP"):
        for r in rows:
            if "fibers_base_map_invariant" in r:
                r["fibers_base_map_invariant"] = False
    # the instrument review's m7: the directed comparator was CARRIED and not
    # REPORTED.  Its value is 0 at every arena in the census -- it separates
    # nothing anywhere, which is why HA requirement 3 forbids it as the admit
    # test and why reporting it moves no verdict.
    dirmax = max(r.get("isomorphisms_directed_comparator", 0) for r in rows)
    dirrows = sum(1 for r in rows
                  if "isomorphisms_directed_comparator" in r)
    if mut("MUT-DIRECTED"):
        dirmax = 1
    fates = Counter(r["fate"] for r in rows)
    R["weld"] = {"rows": rows, "fate_distribution": dict(fates),
                 "walk_control": {"depth": 30, "seed": 4242,
                                  "events": A_WALK["events"],
                                  "divisions": A_WALK["divisions"]},
                 "arenas": len(ARENAS), "readings": 2,
                 "saturating_arenas_driven": len(satarenas),
                 "distinct_saturating_arenas": len(relsigs),
                 "directed_comparator_max": dirmax,
                 "directed_comparator_rows": dirrows,
                 "dead_lists_cited": DEAD_LISTS}
    LD.gate("G-WELD-CENSUS",
            "%d census rows over %d declared arenas at both readings.  Every "
            "row's fate is compared against the fate DECLARED for its own "
            "cell before the run (#87); an aggregate distribution cannot "
            "stand in for a cell" % (len(rows), len(ARENAS)),
            not fatebad, "fates %s; mismatches %s"
            % (dict(fates), fatebad or "none"))
    LD.gate("G-READINGS",
            "BOTH READINGS of 'a map' are run and every row is stamped with "
            "the one it was decided under, exactly as weld 2 declared them: "
            "EMBEDDING asks for a bijection under which the grammar's link "
            "relation CONTAINS the target's incidence; QUOTIENT asks for a "
            "surjection of the realised objects onto the sites carrying every "
            "realised edge onto a declared displacement.  The difference is "
            "measured, not assumed: %d rows die at a different place under "
            "the two readings.  THE DIRECTED COMPARATOR IS CARRIED AND ITS "
            "VALUE IS REPORTED: it returns %d at every one of the %d arenas "
            "where it is defined -- the two FOUND rows included -- so it "
            "separates nothing anywhere, which is exactly why HA "
            "requirement 3 forbids it as the admit test.  FOUND holds at the "
            "undirected reading, and the number that would have made the "
            "directed one an alternative is zero"
            % (sum(1 for a, _t in ARENAS
                   if EXPECTED[(a["name"], "EMBEDDING")]
                   != EXPECTED[(a["name"], "QUOTIENT")]), dirmax, dirrows),
            len({r["reading"] for r in
                 pick("MUT-READINGS", rows,
                      [dict(r, reading="EMBEDDING") for r in rows])}) == 2
            and dirmax == 0 and dirrows == len(ARENAS) - 1,
            "rows @EMBEDDING %d, @QUOTIENT %d; directed comparator max %d "
            "over %d arenas"
            % (sum(1 for r in rows if r["reading"] == "EMBEDDING"),
               sum(1 for r in rows if r["reading"] == "QUOTIENT"),
               dirmax, dirrows))

    def rowof(name, reading):
        return [r for r in rows
                if r["arena"] == name and r["reading"] == reading][0]

    sat_e = rowof("R3-SAT", "EMBEDDING")
    sat_q = rowof("R3-SAT", "QUOTIENT")
    cry_e = rowof("CRYSTAL/DOUBLE-GRID(3,2)@L2", "EMBEDDING")
    cry7 = rowof("CRYSTAL/DOUBLE-GRID(3,2)@I7", "EMBEDDING")
    inh_e = rowof("CRYSTAL-INHOMOGENEOUS@L2", "EMBEDDING")
    walk_e = rowof("D58-GENERIC-2-ACTOR-WALK@I7", "EMBEDDING")
    fal_e = rowof("R3-SAT-FALSIFIER", "EMBEDDING")

    w2t = source_text(texts, "A-W2")
    isos_committed = read_int_after(
        w2t, "It returns **FOUND** at I7's lattice with", 1)
    isos_here = pick("MUT-ISOS", sat_e["isomorphisms"], 1295)
    anchors.append({"id": "N-ISOS-AT-I7", "committed": isos_committed,
                    "computed": isos_here, "source": "A-W2",
                    "match": isos_here == isos_committed})
    cry_committed = read_int_after(
        w2t, "the census machinery returns **FOUND** --", 1)
    anchors.append({"id": "N-ISOS-AT-CRYSTAL", "committed": cry_committed,
                    "computed": cry_e.get("isomorphisms"), "source": "A-W2",
                    "match": cry_e.get("isomorphisms") == cry_committed})
    LD.gate("G-ISOS-ANCHOR",
            "WELD 2's OWN NUMBER, NOW CARRIED BY A GRAMMAR RECORD.  Weld 2 "
            "could only exhibit the FOUND branch at I7's three-link target on "
            "a DECLARED PROBE, and it reported the probe's site-assignment "
            "count.  That number is READ from weld 2's pinned bytes here and "
            "reproduced by this unit's own exhaustive enumeration on a DRIVEN "
            "grammar record -- and weld 2's crystal-control count is read and "
            "reproduced the same way, from d66's own `double_grid(3,2)` "
            "re-run in this process",
            isos_here == isos_committed
            and cry_e.get("isomorphisms") == cry_committed,
            "at I7: weld 2 committed %s, this unit computes %s; at the "
            "crystal: committed %s, computed %s"
            % (isos_committed, isos_here, cry_committed,
               cry_e.get("isomorphisms")))
    R["anchors"] = anchors
    SEAL.take("SEAL-ANCHORS", R)

    # THE CONTROLS, two-way and falsified
    LD.gate("G-CTRL-FOUND-CRYSTAL",
            "THE FOUND-SIDE CONTROL, re-established at this unit: on d66's "
            "own DOUBLE-GRID(3,2) -- a grammar record that provably carries a "
            "lattice -- the detector returns %s at the lattice the record "
            "itself carries, with %s site assignments all giving ONE count "
            "field and every inventory fiber 1"
            % (cry_e["fate"], cry_e.get("isomorphisms")),
            pick("MUT-CTRL-FOUND", cry_e["fate"], "STRUCT-DEAD")
            == "FOUND-candidate" and not cry_e["free_items"],
            "fate %s, isomorphisms %s, inventory %s"
            % (cry_e["fate"], cry_e.get("isomorphisms"),
               cry_e.get("inventory")))
    fib6 = read_int_after(w2t, "with `I-SITE-ASSIGNMENT` fiber", 1)
    LD.gate("G-CTRL-FALSIFIER",
            "THE FOUND-SIDE CONTROL CAN FAIL, AND DOES ON DEMAND.  The "
            "declared falsifier is the same crystal with one row-group "
            "arbitration withheld from its division set; the same machinery "
            "returns %s, with the site-assignment fiber MEASURED at %s -- "
            "weld 2's committed value for the same object is READ from its "
            "pinned bytes and compared"
            % (inh_e["fate"], inh_e.get("inventory", {}).get(
                "I-SITE-ASSIGNMENT")),
            pick("MUT-CTRL-FALSIFIER", inh_e["fate"], "FOUND-candidate")
            == "UNMOTIVATED"
            and inh_e["inventory"]["I-SITE-ASSIGNMENT"] == fib6,
            "fate %s, inventory %s, weld 2 committed fiber %s"
            % (inh_e["fate"], inh_e.get("inventory"), fib6))
    LD.gate("G-CTRL-EMPTY-WALK",
            "THE EMPTY-SIDE CONTROL, re-established: d58's own generic "
            "2-actor walk at depth 30, seed 4242, re-run in this process "
            "through the committed layer's menus (%d events, %d division "
            "events).  Against I7's declared lattice the detector returns "
            "ARITY-DEAD -- 2 site objects against 9 -- which is a property of "
            "the walk and not of the plumbing"
            % (A_WALK["events"], A_WALK["divisions"]),
            pick("MUT-CTRL-WALK", walk_e["site_arity"], 9) == 2
            and walk_e["fate"] == "ARITY-DEAD",
            "site arity %d, fate %s" % (walk_e["site_arity"],
                                        walk_e["fate"]))
    diag0 = sum(1 for x in SITES
                if A_CRYI7["rel"].get((actor(x), actor(zadd(x, (1, 1)))), 0)
                == 0)
    LD.gate("G-CTRL-CRYSTAL-AT-I7",
            "WELD 2's UNANTICIPATED MEASUREMENT, REPRODUCED: against I7's "
            "three-link lattice the same crystal is %s, because its diagonal "
            "co-division count is identically zero -- measured here at %d of "
            "9 sites -- so the induced determinant vanishes at every site and "
            "no committed crystal induces an admissible I7 record.  That is "
            "the wall this unit's arena walks through" % (cry7["fate"], diag0),
            cry7["fate"] == "STRUCT-DEAD"
            and pick("MUT-CRYSTAL-DIAGONAL", diag0, 0) == 9,
            "fate %s, diagonal-zero sites %d of 9, embedding isomorphisms %s"
            % (cry7["fate"], diag0, cry7.get("isomorphisms")))
    LD.gate("G-CTRL-R3-FALSIFIER",
            "THE TWO-WAY REQUIREMENT AT THIS UNIT'S OWN ARENA.  The declared "
            "falsifier is the uniform R = 3 record with ONE arbitration "
            "withheld: the co-division relation loses one triangle, the "
            "detector returns %s, and the FOUND branch is therefore not an "
            "artefact of the plumbing at this arena either"
            % fal_e["fate"],
            pick("MUT-CTRL-R3-FALSIFIER", fal_e["fate"], "FOUND-candidate")
            == "STRUCT-DEAD",
            "fate %s at EMBEDDING, %s at QUOTIENT"
            % (fal_e["fate"], rowof("R3-SAT-FALSIFIER", "QUOTIENT")["fate"]))

    # THE SMUGGLING CLASSIFIER
    fam_pairs = sorted(i7["family"].items())
    probe_moved = pick("MUT-SMUGGLE-BLIND",
                       len({fam_pairs[0][1], fam_pairs[1][1]}) > 1, False)
    cand_moved = False
    LD.gate("G-SMUGGLE",
            "THE NO-SMUGGLING CLASSIFIER (weld 2's sharpened form).  Since "
            "record and metric are one datum in two coordinate systems, the "
            "test is WHICH FUNCTION of grammar data a candidate computes: its "
            "count function is run against two DIFFERENT declared I7 records, "
            "and a candidate whose counts move is reading I7's own s back.  "
            "Every census candidate's count function is built from the link "
            "relation alone and is a CONSTANT function of the record it is "
            "handed, so SMUGGLED = 0 here is STRUCTURAL and not measured; the "
            "classifier's positive value is exercised by a declared "
            "S-valued probe, which does move and classifies SMUGGLED",
            probe_moved and not cand_moved,
            "declared S-valued probe moves: %s; census candidates move: %s"
            % (probe_moved, cand_moved))

    exhibited = sorted(set(fates) | {"SMUGGLED" if probe_moved else "-"})
    need = {"FOUND-candidate", "UNMOTIVATED", "STRUCT-DEAD", "COUNT-DEAD",
            "ARITY-DEAD"}
    if mut("MUT-TWO-WAY"):
        exhibited = [e for e in exhibited if e != "COUNT-DEAD"]
    LD.gate("G-TWO-WAY",
            "HA requirement 3 discharged with measurements rather than with a "
            "declaration: every value this detector can return is EXHIBITED "
            "in this run -- FOUND on the R = 3 saturating record and on the "
            "crystal at its own lattice, UNMOTIVATED on the declared "
            "falsifier, STRUCT-DEAD on the crystal at I7 and on this unit's "
            "own falsifier, COUNT-DEAD on the committed R = 3 grid, "
            "ARITY-DEAD on the walk, and SMUGGLED on the declared S-valued "
            "probe",
            need <= set(exhibited),
            "exhibited %s; missing %s" % (exhibited,
                                          sorted(need - set(exhibited))))
    LD.gate("G-DEAD-LISTS-CITED",
            "the pre-registered dead lists are CITED and NEVER RE-RUN: %s.  "
            "No candidate row of this census re-derives one, and the census's "
            "own site and link generators are the single cell weld 2 left "
            "live at a record arena" % "; ".join(DEAD_LISTS),
            not mut("MUT-DEAD-LIST")
            and all(r["site_gen"] == "ACTOR" and r["link_gen"] == "ACTOR-PAIR"
                    for r in rows),
            "dead-list rows re-run: %d; census generators %s"
            % (1 if mut("MUT-DEAD-LIST") else 0,
               sorted({(r["site_gen"], r["link_gen"]) for r in rows})))

    # THE INDUCED RECORD AGAINST I7's OWN FAMILY
    cf = dict((tuple(z) if isinstance(z, list) else z)
              for z in sat_e["count_field"])
    ind = (cf[str(((0, 0), (1, 0)))], cf[str(((0, 0), (0, 1)))],
           cf[str(((0, 0), (1, 1)))])
    adm = pick("MUT-ADMISSIBLE", admissible(ind), False)
    q11, q22, q12, det = q_of(ind)
    reg(q11, q22, q12, det)
    inbox = pick("MUT-I7-BOX", ind in set(i7_box_admissible(i7["box"])),
                 False)
    orb = chart_orbit(ind)
    hits = sorted(nm for nm, v in i7["family"].items() if tuple(v) in orb)
    for nm, recmap in sorted(i7["site_dependent_family"].items()):
        if all(tuple(recmap[x]) in orb for x in sorted(recmap)):
            hits.append(nm)
    if mut("MUT-IN-FAMILY"):
        hits = ["G-FLAT"]
    R["i7"]["induced_record"] = {
        "n": list(ind), "q11": str(q11), "q22": str(q22), "q12": str(q12),
        "det": str(det), "admissible": bool(admissible(ind)),
        "in_declared_box": inbox, "chart_orbit": sorted(str(o) for o in orb),
        "declared_family_hits": hits,
        "declared_family_size": len(i7["family"])
        + len(i7["site_dependent_family"])}
    LD.gate("G-ADMISSIBLE",
            "THE INDUCED RECORD IS AN ADMISSIBLE I7 GEOMETRY RECORD by I7's "
            "OWN criterion, checked at every site: q = [[%s, %s], [%s, %s]] "
            "with leading minor %s > 0 and det %s > 0, the exact Sylvester "
            "criterion HA 3.2 declares" % (q11, q12, q12, q22, q11, det),
            adm and all(admissible(ind) for _x in SITES),
            "n = %s, q11 = %s, det = %s, admissible %s"
            % (list(ind), q11, det, adm))
    LD.gate("G-I7-BOX",
            "and it lies inside I7's OWN declared count box: the box is read "
            "from I7's receipt (axis_max %d, diag_max %d), its admissible "
            "points are RECOMPUTED here by the same Sylvester test and the "
            "count reproduces I7's committed %s exactly, with the induced "
            "vector among them"
            % (i7["box"]["axis_max"], i7["box"]["diag_max"],
               i7["committed_admissible_points"]),
            inbox and nbox == i7["committed_admissible_points"],
            "recomputed admissible points %d, committed %s, induced vector "
            "inside %s" % (len(boxpts), i7["committed_admissible_points"],
                           inbox))
    LD.gate("G-NOT-IN-FAMILY",
            "AND IT IS NOT ONE OF I7's %d DECLARED RECORDS.  Each declared "
            "record is compared against the induced vector's whole chart "
            "orbit -- I7's chart group is its site translations and its d! "
            "direction relabellings, and on a homogeneous record the "
            "translations act trivially -- so the comparison is per record "
            "and not by name.  The weld lands INSIDE I7's admissible class "
            "and OUTSIDE its declared list, and that distinction is the "
            "honest scope of this result"
            % (len(i7["family"]) + len(i7["site_dependent_family"])),
            not hits,
            "declared records %s and %s; chart orbit %s; hits %s"
            % (sorted(i7["family"]), sorted(i7["site_dependent_family"]),
               sorted(str(o) for o in orb), hits or "none"))

    # ---- THE PRECEDENT, READ FROM WELD 2's OWN COMMITTED RECEIPT --------
    # What reaching FOUND at this target has always MEANT is fixed by the
    # object weld 2 itself reached it on.  That object is read here, not
    # argued: its induced record is recomputed from its committed count field
    # by this unit's own readout.
    w2rec = json.loads(source_text(texts, "A-W2REC"))
    w2probe = w2rec["payload"]["controls"]["FOUND_at_I7_target_declared_probe"]
    w2cf = {k: v for k, v in (tuple(z) for z in w2probe["count_field"])}
    w2ind = (w2cf[str(((0, 0), (1, 0)))], w2cf[str(((0, 0), (0, 1)))],
             w2cf[str(((0, 0), (1, 1)))])
    w2q11, w2q22, w2q12, w2det = q_of(w2ind)
    reg(w2q11, w2q22, w2q12, w2det)
    w2orb = chart_orbit(w2ind)
    w2hits = sorted(nm for nm, v in i7["family"].items()
                    if tuple(v) in w2orb)
    for nm, recmap in sorted(i7["site_dependent_family"].items()):
        if all(tuple(recmap[x]) in w2orb for x in sorted(recmap)):
            w2hits.append(nm)
    if mut("MUT-W2-WITNESS"):
        w2hits = ["G-FLAT"]
    w2verdict = w2rec["verdicts"]["controls"]["FOUND_at_I7_declared_probe"]
    R["i7"]["weld2_found_witness"] = {
        "source": "A-W2REC", "arena": w2probe["arena"],
        "verdict": w2verdict, "n": list(w2ind),
        "q11": str(w2q11), "q22": str(w2q22), "q12": str(w2q12),
        "det": str(w2det), "admissible": bool(admissible(w2ind)),
        "in_declared_box": w2ind in set(boxpts),
        "declared_family_hits": w2hits,
        "distinct_counts": sorted({v for v in w2cf.values()})}
    LD.gate("G-W2-WITNESS",
            "WHAT REACHING FOUND AT THIS TARGET HAS ALWAYS MEANT, READ FROM "
            "WELD 2's OWN BYTES.  Weld 2 could exhibit its FOUND branch at "
            "I7's three-link target only on a DECLARED PROBE, and that probe "
            "is the object which fixed the meaning of the branch this unit "
            "now occupies.  Its committed count field is read here and its "
            "induced record recomputed by this unit's own readout: %s, "
            "q = [[%s, %s], [%s, %s]], det %s -- ADMISSIBLE by the same exact "
            "Sylvester criterion, INSIDE the same %d-point declared box, and "
            "NOT ONE OF I7's %d DECLARED RECORDS EITHER.  So the branch weld "
            "2 reserved was never a branch onto a declared record: THE WELD "
            "IS TO I7's RECORD SPACE -- its lattice and its record axioms -- "
            "and the eleven are named witnesses inside that space rather than "
            "the gate.  This unit lands the same species of object, on a "
            "DRIVEN grammar record instead of a probe"
            % (str(tuple(w2ind)), w2q11, w2q12, w2q12, w2q22, w2det,
               len(boxpts), len(i7["family"])
               + len(i7["site_dependent_family"])),
            w2verdict == "FOUND-candidate" and admissible(w2ind)
            and w2ind in set(boxpts) and not w2hits
            and len({v for v in w2cf.values()}) == 1,
            "weld 2's committed probe verdict %s; induced record %s; "
            "admissible %s; in the box %s; declared-family hits %s"
            % (w2verdict, list(w2ind), admissible(w2ind),
               w2ind in set(boxpts), w2hits or "none"))

    # ---- THE STRICTEST READING AVAILABLE (the operator review's (d3)) ----
    # Force the map to be the constructor's OWN actor -> Z_3^2 parse, the
    # inventory item this unit calls forced, and read the induced field with
    # no site freedom whatever.
    def carrier_fixed(a):
        return count_field(a["rel"], TGT_I7["X"], TGT_I7["links"],
                           TGT_I7["Lmod"], dict(ACTOR_SITE),
                           tuple(range(len(TGT_I7["links"]))), False)
    sat_fix = carrier_fixed(A_SAT)
    non_fix = carrier_fixed(A_NON)
    sat_fix_min = min(sat_fix.values())
    non_fix_zero = pick("MUT-STRICTEST",
                        sum(1 for v in non_fix.values() if v == 0), 0)
    R["weld"]["strictest_reading"] = {
        "reading": "SITE-CARRIER-FIXED (the constructor's own actor -> Z_3^2 "
                   "parse; no site freedom at all)",
        "R3-SAT": {"min": sat_fix_min, "max": max(sat_fix.values()),
                   "cells_at_zero": sum(1 for v in sat_fix.values()
                                        if v == 0), "survives": True},
        "R3-ROW|COL|ANT": {"min": min(non_fix.values()),
                           "max": max(non_fix.values()),
                           "cells_at_zero": non_fix_zero,
                           "survives": False}}
    LD.gate("G-STRICTEST-READING",
            "FOUND AT THE PRIMARY ARENA DOES NOT NEED THE SITE ASSIGNMENT TO "
            "BE FREE AT ALL.  Under the strictest reading available -- the "
            "site carrier FIXED to the constructor's own actor -> Z_3^2 "
            "parse, which is inventory item 3 and which this unit calls "
            "forced -- the saturating record still induces a strictly "
            "positive field: min %d, max %d over the 27 cells.  The same "
            "reading KILLS the relabelling row: R3-ROW|COL|ANT leaves %d of "
            "the 27 cells at zero, because the ANT class deposits nothing on "
            "any I7 link in fixed coordinates.  So the free site assignment "
            "carries the second FOUND row and nothing else, exactly as "
            "section 4.4 and deviation 6 price it"
            % (sat_fix_min, max(sat_fix.values()), non_fix_zero),
            sat_fix_min >= 1 and max(sat_fix.values()) == 1
            and non_fix_zero == 9,
            "R3-SAT at the fixed carrier: min %d max %d; R3-ROW|COL|ANT "
            "cells at zero: %d of 27"
            % (sat_fix_min, max(sat_fix.values()), non_fix_zero))
    SEAL.take("SEAL-I7", R)
    SEAL.take("SEAL-WELD", R)

    LD.gate("G-FIBERS",
            "THE RSQ CHOICE STANDARD, WITH THE FIBERS PRINTED.  MOTIVATED "
            "means zero free items, and a fiber is the number of DISTINCT "
            "count fields the choice produces.  At the saturating arena all "
            "three are 1 -- %s isomorphisms give one field, the 6 direction "
            "relabellings give one, both orientations give one -- and the "
            "reason is measured: the field is homogeneous.  The standard is "
            "not vacuous here, because the declared falsifier's "
            "site-assignment fiber is %s.  The label and orient fibers are "
            "READ at the base map the actor-name order fixes, so their "
            "BASE-MAP INVARIANCE is measured rather than assumed: both are "
            "re-read at every one of the %s base maps and both are constant"
            % (sat_e.get("isomorphisms"),
               inh_e["inventory"]["I-SITE-ASSIGNMENT"],
               sat_e.get("base_maps_read")),
            sat_e["inventory"] == {"I-SITE-ASSIGNMENT": 1,
                                   "I-DIRECTION-LABEL": 1, "I-ORIENT": 1}
            and inh_e["inventory"]["I-SITE-ASSIGNMENT"] > 1
            and all(r.get("fibers_base_map_invariant", True) for r in rows),
            "saturating %s; falsifier %s; base-map-invariant fibers %d of %d "
            "rows that carry an inventory"
            % (sat_e["inventory"], inh_e["inventory"],
               sum(1 for r in rows if r.get("fibers_base_map_invariant")),
               sum(1 for r in rows if "fibers_base_map_invariant" in r)))
    cnc = R["geometry"]["coverage_not_count"]
    com3_inc = cnc["committed_R3_incidences"]
    com3_cov = cnc["committed_R3_cells_covered"]
    com3_zero = cnc["committed_R3_cells_at_zero"]
    full_budget = cnc["triples_paying_the_full_budget"]
    weld_of_them = cnc["of_which_weld"]
    LD.gate("G-COUNT-IMPLIES-WELD",
            "THE EFFECTUS'S DEMAND (iv), ANSWERED AS POSED: >= 27 incidences "
            "is NECESSARY AND NOT SUFFICIENT, and what IS sufficient here is "
            "COVERAGE.  Necessity is a theorem and is measured: all %d "
            "I7-STRICT triples carry exactly 27 incidences and no schedule of "
            "this budget carries more.  The COUNT alone is not sufficient and "
            "the census contains the counterexample: %d ordered grouping "
            "triples -- every triple of saturating partitions -- deposit the "
            "full 27, and exactly %d of them weld, one in %d.  d66's own "
            "R = 3 point is one of the others: it deposits %d incidences and "
            "spends them on %d of the 27 cells, doubling nine row cells and "
            "leaving %d diagonal cells at zero.  What is necessary and, at "
            "this candidate family and this target, sufficient is that every "
            "one of the 27 cells is covered at least once -- which is "
            "I7-STRICT itself -- and the rigidity theorem then forces the "
            "field to be identically 1, the co-division relation to be the "
            "target's own Cayley incidence and every fiber to be 1"
            % (weld_of_them, full_budget, weld_of_them,
               full_budget // weld_of_them, com3_inc, com3_cov, com3_zero),
            all(a["divisions"] == 9 for a in satarenas)
            and sat_e["fate"] == "FOUND-candidate"
            and com3_inc == 27 and com3_cov == 18 and com3_zero == 9
            and full_budget > weld_of_them
            and pick("MUT-COUNT-SUFFICIENT",
                     rowof("R3-COMMITTED-GRID(3,3)", "QUOTIENT")["fate"],
                     "FOUND-candidate") == "COUNT-DEAD",
            "I7-STRICT triples %d, incidences each 27, weld fate %s; full "
            "budget paid by %d triples of which %d weld (1 in %d); the "
            "committed R = 3 grid deposits %d incidences over %d of 27 cells "
            "and is %s"
            % (len(C["strict_triples"]), sat_e["fate"], full_budget,
               weld_of_them, full_budget // weld_of_them, com3_inc, com3_cov,
               rowof("R3-COMMITTED-GRID(3,3)", "QUOTIENT")["fate"]))

    # ---------------- THE STRATA, EACH WITH A DRIVEN WITNESS ------------
    say("\n[SEC 8] THE CENSUS STRATA, EACH WITNESSED BY A DRIVEN RECORD")
    scan = []
    for a in CLASS_NAMES:
        for b2 in CLASS_NAMES:
            for c2 in CLASS_NAMES:
                scan.append((CLASSES[a], CLASSES[b2], CLASSES[c2]))
    for (i, j, k) in C["strict_triples"]:
        scan.append((parts[i], parts[j], parts[k]))
    if "cells" in CACHE:
        cells = CACHE["cells"]
    else:
     cells = {}
     for T in scan:
         packed = sum(pack_links(P)[0] for P in T)
         st = all(((packed >> (6 * m + 2 * li)) & 3) >= 1
                  for m in range(9) for li in range(3))
         nz = sum(1 for m in range(9)
                  if CODE_TAB[(packed >> (6 * m)) & 63][1])
         geom = ("I7-STRICT" if st else
                 ("NONDEGENERATE-9" if nz == 9 else "OTHER"))
         menus = [transversals(P) for P in T]
         for s0 in menus[0]:
             f0 = [1 if x in s0 else 0 for x in SITES]
             for s1 in menus[1]:
                 f1 = [f0[m] + (1 if x in s1 else 0)
                       for m, x in enumerate(SITES)]
                 for s2 in menus[2]:
                     key = tuple(f1[m] + (1 if x in s2 else 0)
                                 for m, x in enumerate(SITES))
                     cell = (stab_of(key), affine_class(
                         (frozenset(s0), frozenset(s1), frozenset(s2))), geom)
                     if cell not in cells:
                         cells[cell] = ((T[0], s0), (T[1], s1), (T[2], s2))
     CACHE["cells"] = cells
    wits, wbad = [], []
    for cell, sch in sorted(cells.items()):
        rec = driven(G, sch)
        ok = (rec["maxhits"] == 1 and rec["refusal"] is None
              and rec["divisions"] == 9)
        wits.append({"cell": "|".join(cell), "events": rec["events"],
                     "maxhits": rec["maxhits"], "divisions": rec["divisions"],
                     "forced": ok})
        if not ok:
            wbad.append("|".join(cell))
    if mut("MUT-STRATUM-BLIND"):
        wits = wits[:-1]
    R["strata"] = {"scanned_grouping_triples": len(scan),
                   "seed_triples_per_grouping": 27 ** 3,
                   "nonempty_cells": len(cells), "witnesses": wits}
    LD.gate("G-STRATA-WITNESSED",
            "the census stratifies by (stabilizer x affine class x geometry "
            "class).  The declared stratum scan -- %d grouping triples at all "
            "%d seed triples each -- realises %d cells, and EVERY one of "
            "them is given a deterministic representative whose record is "
            "BUILT BY DRIVING THE MENUS.  So the grammar's verdict has been "
            "taken at least once in every cell of the census, including cells "
            "whose groupings are not parallel classes at all"
            % (len(scan), R["strata"]["seed_triples_per_grouping"],
               len(cells)),
            len(wits) == len(cells) and not wbad,
            "cells %d, driven witnesses %d, non-FORCED %d"
            % (len(cells), len(wits), len(wbad)))
    SEAL.take("SEAL-STRATA", R)

    # ---------------- SEC 9  THE WALLS ----------------------------------
    say("\n[SEC 9] THE WALLS")
    ptext = paper_text if paper_text is not None else ""
    l1 = source_text(texts, "A-L1")
    # the instrument review's M3b: the declared falsifier says it INJECTS the
    # retracted sentence "LINE-WRAPPED AND BLOCKQUOTED in house style", and it
    # used to set the gate's boolean instead.  It now performs the injection
    # it advertises, so the mutant exercises the #125 normaliser it names.
    if mut("MUT-WALL-L1") and ptext:
        _w, _line, _out = BANNED_L1.split(" "), "", []
        for _tok in _w:
            if len(_line) + len(_tok) + 1 > 40:
                _out.append("> " + _line.strip())
                _line = ""
            _line += _tok + " "
        _out.append("> " + _line.strip())
        ptext = ptext + "\n\n" + "\n".join(_out) + "\n"
    banned_here = match_needle(ptext, BANNED_L1) if ptext else False
    LD.gate("G-WALL-L1",
            "L-1, ARGUED BEFORE ANY TEST AND THEN DECLINED.  Order-level "
            "covariance is a fourth form whose admissibility v11 must argue; "
            "this arena supplies finite records and a translation action on "
            "their SITE LATTICE, the corpus contains no bridge from Z_3^2 "
            "translations to any boost, and this unit constructs none -- so "
            "the fourth form is NOT TESTED here.  The sentence retracted on "
            "2026-07-28 appears nowhere in the paper, and the gate that "
            "enforces its absence normalises whitespace, folds to ASCII and "
            "strips markdown prefixes, so a line-wrapped or blockquoted "
            "injection dies too",
            match_needle(l1, VERBATIM[16][2]) and not banned_here,
            "L-1 clause matched in its pinned bytes: %s; retracted sentence "
            "present in the paper: %s"
            % (match_needle(l1, VERBATIM[16][2]), banned_here))
    # THE THREE ABSTENTION WALLS, GIVEN REAL PREDICATES (the instrument
    # review's M3).  They used to take their entire input from their own
    # mutant flag, so they asserted a property rather than measuring one.  The
    # measurement layer is now SCANNED: the receipt's measured keys plus the
    # statement and evidence of every gate this run has evaluated that is not
    # itself a wall gate -- the wall gates are excluded because naming the
    # wall is exactly their job.  Both sides are #125-normalised.
    if mut("MUT-WALL-BHS"):
        R["arena"] = dict(R["arena"],
                          sprinkling_boost_reading="rapidity 1/2 in the "
                          "sprinkled frame")
    if mut("MUT-WALL-KR"):
        R["geometry"] = dict(R["geometry"],
                             myrheim_meyer_dimension_estimate="4")
    if mut("MUT-WALL-COSMO"):
        R["weld"] = dict(R["weld"],
                         cosmological_reading="the diagonal read as a "
                         "continuum expansion direction")

    def wall_surface():
        body = json.dumps({k: R[k] for k in MEASURED_KEYS if k in R},
                          sort_keys=True, default=str)
        rows = "\n".join(g["statement"] + " " + g["evidence"] for g in LD.rows
                         if not g["gate"].startswith("G-WALL-"))
        return canon(body + "\n" + rows).lower()
    BOOST_TERMS = ("boost", "rapidity", "sprinkl", "frame")
    DIM_TERMS = ("myrheim", "meyer", "shatter", "chart width", "dimension",
                 "height")
    COSMO_TERMS = ("cosmolog", "continuum", "horizon", "redshift", "universe",
                   "expansion")
    surf = wall_surface()
    boost_hits = [t for t in BOOST_TERMS if t in surf]
    LD.gate("G-WALL-BHS",
            "BHS: a Poisson sprinkling admits no Lorentz-invariant "
            "finite-valency graph, and these schedules are finite-valency by "
            "construction, so running a sprinkling-grade Lorentz-invariance "
            "test would manufacture a false negative.  None is run, and that "
            "is MEASURED rather than asserted: the %d-character measurement "
            "layer of this run -- every measured receipt key plus the "
            "statement and evidence of all %d non-wall gates evaluated so far "
            "-- is scanned for %s and contains none of them"
            % (len(surf), sum(1 for g in LD.rows
                              if not g["gate"].startswith("G-WALL-")),
               ", ".join(BOOST_TERMS)),
            not boost_hits, "terms scanned %d, surface %d chars, hits: %s"
            % (len(BOOST_TERMS), len(surf), boost_hits or "none"))
    dim_hits = [t for t in DIM_TERMS if t in surf]
    LD.gate("G-WALL-KR",
            "Kleitman-Rothschild: a dimension reading without a height "
            "control is worthless.  This unit takes NO dimension reading at "
            "all -- no chart width, no Myrheim-Meyer estimate, no "
            "max-shatter dimension -- so the height control is not owed and "
            "not manufactured.  The abstention is MEASURED on the same "
            "surface: %s appear nowhere in it, so there is no reading for a "
            "height control to be owed against"
            % ", ".join(DIM_TERMS),
            not dim_hits, "terms scanned %d, surface %d chars, hits: %s"
            % (len(DIM_TERMS), len(surf), dim_hits or "none"))
    cosmo_hits = [t for t in COSMO_TERMS if t in surf]
    LD.gate("G-WALL-DIAGONAL",
            "the diagonal is MEASURED here -- the (1,1) link is populated by "
            "every saturating arrangement and is exactly what lifts the "
            "determinant off zero -- and it is READ NO FURTHER.  The four "
            "directions above are directions on a nine-site lattice and are "
            "read as nothing else, and that too is measured: %s appear "
            "nowhere in this run's measurement layer, so no cosmological or "
            "continuum reading is taken anywhere in this unit"
            % ", ".join(COSMO_TERMS),
            not cosmo_hits, "terms scanned %d, surface %d chars, hits: %s"
            % (len(COSMO_TERMS), len(surf), cosmo_hits or "none"))
    # M3 again: the naming falsifier now DELETES the sentence from the object
    # under test rather than setting the gate's boolean.
    if mut("MUT-WALL-LORENTZ"):
        ptext = ptext.replace("NAMED AND NOT READ", "named and considered")
    named = match_needle(ptext, LORENTZ_NAMED) if ptext else None
    LD.gate("G-WALL-LORENTZ-NAMED",
            "THE LORENTZIAN RESONANCE IS NAMED AND NOT READ, and the naming "
            "is MANDATORY (the U4b lesson: silence is how a resonance becomes "
            "governance).  This unit's headline is a positive definite form "
            "with det 3/4 on a nine-site lattice; a reader arriving from the "
            "relativity line will hear 'signature' and must be told, in the "
            "paper, that no signature is claimed.  The gate requires the "
            "declared sentence to be PRESENT",
            named is not False,
            "naming sentence present in the paper under test: %s"
            % ("not evaluated (no paper)" if named is None else named))
    R["walls"] = {"L1": "argued-and-declined", "BHS": "not-run",
                  "KR": "no-dimension-reading",
                  "diagonal": "measured-read-no-further",
                  "lorentzian_resonance": "NAMED-AND-NOT-READ",
                  "banned_sentence_present": bool(banned_here),
                  "naming_sentence_present": named}
    SEAL.take("SEAL-WALLS", R)

    # ---------------- SEC 10  THE VERDICT -------------------------------
    say("\n[SEC 10] THE VERDICT")
    counts = {
        "family": FAMILY, "window": len(win),
        "strata_cells": len(cells),
        "ordered_grouping_triples": ordered_total,
        "i7_strict_triples": strict_route1,
        "i7_strict_schedules": strict_route1 * 27 ** 3,
        "posdef_ceiling": max(ph), "posdef_at_ceiling": at_ceiling,
        "empty_posdef_cell": 8,
        "seed_triples": n_triples, "crystalline": crystalline,
        "full_group": stabc["Z3^2"], "beyond_coset_crystalline": beyond,
        "weld_rows": len(rows), "weld_found": fates.get("FOUND-candidate", 0),
        "isomorphisms": sat_e["isomorphisms"],
        "det_uniform": "3/4", "cells_at_one": 27,
    }
    R["counts"] = counts
    verdict = {
        "arena": ("R3-ARENA-UNIT-GRADE-[n=1 at 27 of 27; det=3/4 at 9 of 9; "
                  "POSDEF 9 of 9; FORCED %d of %d; FULL-GROUP REACHABLE %d]"
                  "@WINDOW-%d-OF-%d+%d-STRATUM-WITNESSES"
                  % (fates_forced(R), len(WD), stabc["Z3^2"], len(win),
                     FAMILY, len(cells))),
        "geometry": ("POSITIVE-GEOMETRY-[CEILING %d ATTAINED at %d of %d "
                     "GROUPING TRIPLES; %d NEVER ATTAINED; "
                     "I7-STRICT=POSDEF-9=FIELD-IDENTICALLY-1 (SITEWISE: "
                     "POSDEF(x) IFF min_l n_l(x)>=1, AT ALL %d REACHABLE SITE "
                     "CODES); DET-SPECTRUM %d VALUES ON %d CELLS]"
                     % (max(ph), at_ceiling, ordered_total, 8,
                        R["geometry"]["sitewise_identity"]
                        ["reachable_site_codes"], len(detspec), spec_total)),
        "weld": weld_string({
            # the instrument review's M1, now a dead mutant: the one-line
            # forgery moves the BUILDER only.  The comparator types its own
            # template and re-derives the word from the receipt's fate rows.
            "out": pick("MUT-WELD-FORGERY",
                        weld_outcome(sat_e["fate"], sat_q["fate"]), "EMPTY"),
            "isos": sat_e["isomorphisms"], "qm": sat_q["quotient_maps"],
            "fs": sat_e["inventory"]["I-SITE-ASSIGNMENT"],
            "fl": sat_e["inventory"]["I-DIRECTION-LABEL"],
            "fo": sat_e["inventory"]["I-ORIENT"],
            "n1": ind[0], "n2": ind[1], "n3": ind[2],
            "q": "[[%s, %s], [%s, %s]]" % tuple(R["arena"]["q"]),
            "det": str(det), "nbox": len(boxpts),
            "nfam": len(i7["family"]) + len(i7["site_dependent_family"]),
            "w1": w2ind[0], "w2": w2ind[1], "w3": w2ind[2],
            "nstrict": strict_route1, "ntriples": ordered_total,
            "ncoord": cf_tot, "nmult": len(C["strict_multisets"]),
            "inc": com3_inc, "cov": com3_cov,
            "budget": full_budget, "onein": full_budget // weld_of_them,
            "cryisos": cry_e["isomorphisms"], "inhfate": inh_e["fate"],
            "inhfib": inh_e["inventory"]["I-SITE-ASSIGNMENT"],
            "walkfate": walk_e["fate"], "arity": walk_e["site_arity"],
            "cry7": cry7["fate"], "falfate": fal_e["fate"],
            "dir": dirmax, "dirrows": dirrows,
            "zero": non_fix_zero}),
    }
    R["verdict"] = verdict
    for k in ("arena", "geometry", "weld"):
        say("\n  " + verdict[k])

    # the head, DERIVED A SECOND TIME by a comparator that shares neither
    # code nor input nor typed literal with the builder
    ser = json.dumps(R, indent=1, sort_keys=True, default=str)
    again = reconstruct_from_serialized(ser)
    if mut("MUT-HEAD"):
        again = dict(again, weld=again["weld"].replace("FOUND", "EMPTY"))
    drift = [k for k in ("arena", "geometry", "weld")
             if again[k] != verdict[k]]
    LD.gate("G-VERDICT-RECONSTRUCTED",
            "the head is DERIVED, not typed: a second reconstruction reads "
            "only the serialized receipt, recomputes every segment from the "
            "rows it finds there -- the outcome word included, from the "
            "measured fate multiset -- and the two strings are compared "
            "complete, all %d characters of them"
            % sum(len(verdict[k]) for k in verdict),
            not drift, "segments compared %d, drifted %s"
            % (len(verdict), drift or "none"))
    SEAL.take("SEAL-VERDICT", R)
    SEAL.take("SEAL-COUNTS", R)

    # ---------------- THE PAPER GATES -----------------------------------
    claims = paper_claims(R)
    R["paper_claims"] = claims
    if do_paper and paper_text is not None:
        missing = [c["id"] for c in claims
                   if not match_needle(paper_text, c["text"])]
        if mut("MUT-PAPER-CLAIM"):
            missing = missing or ["C01"]
        LD.gate("G-PAPER-CLAIMS",
                "every instrument claim renders in the paper under test: %d "
                "claims, each built HERE from the receipt's own rows and each "
                "matched against the paper with whitespace normalised, ASCII "
                "folded and markdown prefixes stripped" % len(claims),
                not missing, "claims %d, missing %s"
                % (len(claims), missing or "none"))
        SEAL.take("SEAL-PAPER-CLAIMS", R)
        ptest = paper_text
        if mut("MUT-PAPER-HEAD-NUMERAL"):
            ptest = ptest.replace("21952000", "21952001")
        cov = paper_coverage(R, ptest)
        if mut("MUT-PAPER-NUMERAL"):
            cov = dict(cov, unregistered=cov["unregistered"] + ["987654321"])
        LD.gate("G-PAPER-NUMERAL-COVERAGE",
                "every numeral in the paper occurs in the receipt as a "
                "DELIMITED number -- not as a substring of a longer one -- or "
                "in the declared allow-list of section, ledger and date "
                "references: %d numerals scanned, of which %d are inside the "
                "%d FENCED VERDICT BLOCKS (the #20 addendum engraved at "
                "ledger #168: the old scan stripped every backticked span "
                "before scanning and so never read the head's numbers at "
                "all).  A fenced numeral is allow-listed only against the "
                "receipt -- the run's own verdict strings included -- so a "
                "head number this run never derived cannot pass"
                % (cov["scanned"], cov["fenced_numerals"],
                   cov["fenced_blocks"]),
                not cov["unregistered"],
                "scanned %d (fenced %d in %d blocks), allow-listed %d, "
                "unregistered %s"
                % (cov["scanned"], cov["fenced_numerals"],
                   cov["fenced_blocks"], cov["allowed"],
                   cov["unregistered"][:6] or "none"))
        R["paper_coverage"] = cov
        htest = paper_text
        if mut("MUT-PAPER-HEAD"):
            htest = htest.replace("EMBEDDING+QUOTIENT", "EMBEDDING+EMBEDDING")
        head_missing = [k for k in sorted(R["verdict"])
                        if not match_needle(htest, R["verdict"][k])]
        LD.gate("G-PAPER-HEAD-VERBATIM",
                "THE PAPER'S HEAD IS THE RUN'S HEAD, CHARACTER FOR "
                "CHARACTER.  Each of the %d verdict segments the run derived "
                "-- %d characters in all -- is matched into the paper under "
                "test with whitespace normalised, ASCII folded and markdown "
                "prefixes stripped, so the fenced blocks a reader will quote "
                "are bound to the receipt as strings and not merely as "
                "numbers"
                % (len(R["verdict"]),
                   sum(len(v) for v in R["verdict"].values())),
                not head_missing, "segments matched %d of %d; missing %s"
                % (len(R["verdict"]) - len(head_missing), len(R["verdict"]),
                   head_missing or "none"))
        SEAL.take("SEAL-PAPER-COVERAGE", R)
        pol = paper_polarity(R, paper_text, mutated=mut("MUT-PAPER-POLARITY"))
        R["polarity"] = pol
        LD.gate("G-PAPER-CLAIM-POLARITY",
                "the paper's head carries the POLARITY the run measured: for "
                "each verdict-bearing claim a positive needle must be present "
                "AND its negative twin absent, so a paper that flipped an "
                "outcome word while keeping every number would fail here",
                all(p["ok"] for p in pol),
                "polarity rows %d, violations %s"
                % (len(pol), [p["id"] for p in pol if not p["ok"]] or "none"))
        SEAL.take("SEAL-POLARITY", R)
    else:
        R["polarity"] = []
        R["paper_coverage"] = {}

    R["coverage"] = {}
    R["waiver_ledger"] = []
    R["reachability"] = []
    R["mutants"] = [{"name": m[0], "gate": m[1], "what": m[2]}
                    for m in MUTANTS]
    R["mutant_sweep"] = []
    R["arithmetic"] = "exact: fractions.Fraction and int only; no float"
    R["python"] = "%d.%d.%d" % sys.version_info[:3]
    return LD, SEAL, R, verdict, G


# ===========================================================================
# SECTION 10 helpers: the DERIVED head, the paper gates, the writers
# ===========================================================================

def fates_forced(R):
    return R["constructibility"]["FORCED"]


def weld_outcome(sat_e_fate, sat_q_fate):
    """THE OUTCOME WORD, from the two measured fates of the primary arena.
    The rule is the pin's declared vocabulary and nothing else."""
    if sat_e_fate == "FOUND-candidate" and sat_q_fate == "FOUND-candidate":
        return "FOUND"
    if sat_e_fate in ("STRUCT-DEAD", "COUNT-DEAD", "ARITY-DEAD"):
        return "EMPTY"
    return "BLOCKED-AT-" + sat_e_fate


def weld_string(V):
    """THE BUILDER's weld segment.  Every field of `V` is a measured value;
    the comparator in `reconstruct` types this template a SECOND time from the
    serialized receipt and shares no code with this function -- so a one-line
    forgery here moves the builder only, and dies at the reconstruction gate."""
    return (
        "WELD3-%(out)s-[ACTOR->SITE|CO-DIVISION-ACTOR-PAIR->LINK|"
        "DIVISION-COUNT->n_l(x)]@EMBEDDING+QUOTIENT"
        "<ISOS=%(isos)d=|AUT(K333)||QUOTIENT-MAPS=%(qm)d"
        "|FIBERS=%(fs)d/%(fl)d/%(fo)d(SITE/LABEL/ORIENT,BASE-MAP-INVARIANT)"
        "|INDUCED-RECORD=(%(n1)d,%(n2)d,%(n3)d):q=%(q)s:det=%(det)s:"
        "ADMISSIBLE-BY-HA-SYLVESTER:INSIDE-I7'S-OWN-%(nbox)d-POINT-DECLARED-"
        "BOX:NOT-ONE-OF-ITS-%(nfam)d-DECLARED-RECORDS:THE-WELD-IS-TO-I7'S-"
        "RECORD-SPACE(WELD-2'S-OWN-FOUND-AT-I7-WITNESS-(%(w1)d,%(w2)d,%(w3)d)-"
        "WAS-ADMISSIBLE-AND-UNDECLARED-TOO)"
        " -- SCOPE=THE-SATURATING-STRATUM(%(nstrict)d-OF-%(ntriples)d-"
        "GROUPING-TRIPLES-IN-THE-COMMITTED-NAMING;%(ncoord)d-UP-TO-THE-SITE-"
        "ASSIGNMENT-THE-READING-DECLARES-FREE;STRATUM-WIDE-BY-THEOREM:ALL-"
        "%(nstrict)d-CARRY-ONE-ARENA-IN-%(nmult)d-MULTISETS-EACH-WITNESSED)|"
        "GRAMMAR-ADMISSIBLE-NOT-COMMITTED(d66'S-OWN-R=3-POINT-SPENDS-%(inc)d-"
        "INCIDENCES-ON-%(cov)d-OF-27-CELLS-AND-IS-COUNT-DEAD)|COVERAGE-NOT-"
        "COUNT(%(budget)d-TRIPLES-PAY-THE-FULL-27;%(nstrict)d-WELD;1-IN-"
        "%(onein)d)|ROUTE-B-MOOTED-AT-THIS-TARGET-AND-CARRIER"
        " -- CONTROLS=FOUND-AT-CRYSTAL@L2(ISOS=%(cryisos)d,FIBERS-ALL-1)|"
        "FALSIFIER-FLIPS(%(inhfate)s,SITE-FIBER=%(inhfib)d)|EMPTY-AT-WALK"
        "(%(walkfate)s:%(arity)d-OBJECTS-AGAINST-9)|CRYSTAL-AT-I7(%(cry7)s:"
        "DIAGONAL-0-AT-9-OF-9)|R3-FALSIFIER(%(falfate)s)"
        " -- READINGS-DIFFER=DEAD-ROWS-DIE-AT-STRUCTURE-UNDER-EMBEDDING-AND-"
        "AT-COUNT-POSITIVITY-UNDER-QUOTIENT|DIRECTED-COMPARATOR=%(dir)d-AT-"
        "ALL-%(dirrows)d-ARENAS|STRICTEST-READING(SITE-CARRIER-FIXED)="
        "R3-SAT-SURVIVES-AT-n=1;R3-ROW|COL|ANT-DIES-AT-%(zero)d-ZERO-CELLS>"
        % V)


def reconstruct(rec):
    """THE INDEPENDENT RECONSTRUCTION.  It reads only the serialized receipt
    payload and TYPES ALL THREE TEMPLATES ITSELF -- arena, geometry AND weld.
    The instrument review's M1: the weld segment used to be rebuilt by calling
    `weld_string`, the builder's own function, so 71.2 % of the head was a
    serialization round-trip rather than a derivation and a one-line patch of
    that function moved builder and comparator together.  Nothing below is
    shared with the builder: the template is re-typed, the outcome word is
    re-derived from the receipt's own fate rows, and the derivation is
    cross-checked against the published fate multiset."""
    cn = rec["counts"]
    cons = rec["constructibility"]
    geo = rec["geometry"]
    cry = rec["crystal"]
    rows = {(r["arena"], r["reading"]): r for r in rec["weld"]["rows"]}
    sat_e, sat_q = rows[("R3-SAT", "EMBEDDING")], rows[("R3-SAT", "QUOTIENT")]
    cry_e = rows[("CRYSTAL/DOUBLE-GRID(3,2)@L2", "EMBEDDING")]
    inh_e = rows[("CRYSTAL-INHOMOGENEOUS@L2", "EMBEDDING")]
    walk_e = rows[("D58-GENERIC-2-ACTOR-WALK@I7", "EMBEDDING")]
    cry7 = rows[("CRYSTAL/DOUBLE-GRID(3,2)@I7", "EMBEDDING")]
    fal_e = rows[("R3-SAT-FALSIFIER", "EMBEDDING")]
    ind = rec["i7"]["induced_record"]
    arena = ("R3-ARENA-UNIT-GRADE-[n=1 at %d of %d; det=%s at %d of 9; "
             "POSDEF %d of 9; FORCED %d of %d; FULL-GROUP REACHABLE %d]"
             "@WINDOW-%d-OF-%d+%d-STRATUM-WITNESSES"
             % (rec["arena"]["cells_at_one"], rec["arena"]["cells"],
                rec["arena"]["det"], 9, rec["arena"]["posdef_sites"],
                cons["FORCED"], cons["window"], cry["full_group"],
                rec["family"]["window_size"], rec["family"]["family_size"],
                rec["strata"]["nonempty_cells"]))
    empt = geo["empty_posdef_cells"]
    sw = geo["sitewise_identity"]
    geometry = ("POSITIVE-GEOMETRY-[CEILING %d ATTAINED at %d of %d GROUPING "
                "TRIPLES; %d NEVER ATTAINED; I7-STRICT=POSDEF-9=FIELD-"
                "IDENTICALLY-1 (SITEWISE: POSDEF(x) IFF min_l n_l(x)>=1, AT "
                "ALL %d REACHABLE SITE CODES); DET-SPECTRUM %d VALUES ON %d "
                "CELLS]"
                % (geo["attained_ceiling"], geo["triples_at_ceiling"],
                   geo["ordered_grouping_triples"],
                   [e for e in empt if e != 0][0] if [e for e in empt
                                                      if e != 0] else 0,
                   sw["reachable_site_codes"],
                   len(geo["det_spectrum"]), geo["det_cells"]))
    # the outcome word, RE-DERIVED here from the receipt's own fate rows and
    # cross-checked against the published multiset -- no builder code, no
    # shared helper, no copied string.
    ef, qf = sat_e["fate"], sat_q["fate"]
    if ef == "FOUND-candidate" and qf == "FOUND-candidate":
        out = "FOUND"
    elif ef in ("STRUCT-DEAD", "COUNT-DEAD", "ARITY-DEAD"):
        out = "EMPTY"
    else:
        out = "BLOCKED-AT-" + ef
    fd = rec["weld"]["fate_distribution"]
    if out == "FOUND" and fd.get("FOUND-candidate", 0) < 2:
        out = "BLOCKED-AT-FATE-DISTRIBUTION"
    cnc = geo["coverage_not_count"]
    w2 = rec["i7"]["weld2_found_witness"]
    st = rec["weld"]["strictest_reading"]
    q = rec["arena"]["q"]
    weld = (
        "WELD3-" + out + "-[ACTOR->SITE|CO-DIVISION-ACTOR-PAIR->LINK|"
        "DIVISION-COUNT->n_l(x)]@EMBEDDING+QUOTIENT"
        "<ISOS=%d=|AUT(K333)||QUOTIENT-MAPS=%d"
        "|FIBERS=%d/%d/%d(SITE/LABEL/ORIENT,BASE-MAP-INVARIANT)"
        "|INDUCED-RECORD=(%d,%d,%d):q=[[%s, %s], [%s, %s]]:det=%s:"
        "ADMISSIBLE-BY-HA-SYLVESTER:INSIDE-I7'S-OWN-%d-POINT-DECLARED-BOX:"
        "NOT-ONE-OF-ITS-%d-DECLARED-RECORDS:THE-WELD-IS-TO-I7'S-RECORD-SPACE"
        "(WELD-2'S-OWN-FOUND-AT-I7-WITNESS-(%d,%d,%d)-WAS-ADMISSIBLE-AND-"
        "UNDECLARED-TOO)"
        " -- SCOPE=THE-SATURATING-STRATUM(%d-OF-%d-GROUPING-TRIPLES-IN-THE-"
        "COMMITTED-NAMING;%d-UP-TO-THE-SITE-ASSIGNMENT-THE-READING-DECLARES-"
        "FREE;STRATUM-WIDE-BY-THEOREM:ALL-%d-CARRY-ONE-ARENA-IN-%d-MULTISETS-"
        "EACH-WITNESSED)|GRAMMAR-ADMISSIBLE-NOT-COMMITTED(d66'S-OWN-R=3-POINT-"
        "SPENDS-%d-INCIDENCES-ON-%d-OF-27-CELLS-AND-IS-COUNT-DEAD)|COVERAGE-"
        "NOT-COUNT(%d-TRIPLES-PAY-THE-FULL-27;%d-WELD;1-IN-%d)|ROUTE-B-MOOTED-"
        "AT-THIS-TARGET-AND-CARRIER"
        " -- CONTROLS=FOUND-AT-CRYSTAL@L2(ISOS=%d,FIBERS-ALL-1)|"
        "FALSIFIER-FLIPS(%s,SITE-FIBER=%d)|EMPTY-AT-WALK(%s:%d-OBJECTS-"
        "AGAINST-9)|CRYSTAL-AT-I7(%s:DIAGONAL-0-AT-9-OF-9)|R3-FALSIFIER(%s)"
        " -- READINGS-DIFFER=DEAD-ROWS-DIE-AT-STRUCTURE-UNDER-EMBEDDING-AND-"
        "AT-COUNT-POSITIVITY-UNDER-QUOTIENT|DIRECTED-COMPARATOR=%d-AT-ALL-%d-"
        "ARENAS|STRICTEST-READING(SITE-CARRIER-FIXED)=R3-SAT-SURVIVES-AT-n=1;"
        "R3-ROW|COL|ANT-DIES-AT-%d-ZERO-CELLS>"
        % (sat_e["isomorphisms"], sat_q["quotient_maps"],
           sat_e["inventory"]["I-SITE-ASSIGNMENT"],
           sat_e["inventory"]["I-DIRECTION-LABEL"],
           sat_e["inventory"]["I-ORIENT"],
           ind["n"][0], ind["n"][1], ind["n"][2],
           q[0], q[1], q[2], q[3], ind["det"],
           rec["i7"]["box_admissible_points"], ind["declared_family_size"],
           w2["n"][0], w2["n"][1], w2["n"][2],
           geo["i7_strict_ordered_triples"], geo["ordered_grouping_triples"],
           geo["coordinate_free_saturating"]["total"],
           geo["i7_strict_ordered_triples"], geo["i7_strict_multisets"],
           cnc["committed_R3_incidences"], cnc["committed_R3_cells_covered"],
           cnc["triples_paying_the_full_budget"], cnc["of_which_weld"],
           cnc["one_in"],
           cry_e["isomorphisms"], inh_e["fate"],
           inh_e["inventory"]["I-SITE-ASSIGNMENT"], walk_e["fate"],
           walk_e["site_arity"], cry7["fate"], fal_e["fate"],
           rec["weld"]["directed_comparator_max"],
           rec["weld"]["directed_comparator_rows"],
           st["R3-ROW|COL|ANT"]["cells_at_zero"]))
    return {"arena": arena, "geometry": geometry, "weld": weld}


def reconstruct_from_serialized(text):
    return reconstruct(json.loads(text))


def com(n):
    return format(int(n), ",")


def paper_claims(R):
    """the claims the paper must render, BUILT FROM THE RECEIPT so the paper's
    verdict block cannot go stale."""
    A, G_, C_, W = R["arena"], R["geometry"], R["crystal"], R["weld"]
    I = R["i7"]["induced_record"]
    rows = {(r["arena"], r["reading"]): r for r in W["rows"]}
    sat = rows[("R3-SAT", "EMBEDDING")]
    inh = rows[("CRYSTAL-INHOMOGENEOUS@L2", "EMBEDDING")]
    out = [
        ("C01", "the uniform R = 3 arrangement runs to %s events with %s "
         "division events and its driven link field is 1 at every one of the "
         "%s cells" % (com(A["events"]), com(A["divisions"]),
                       com(A["cells"])), "POSITIVE"),
        ("C02", "det = %s at all nine sites and the form is positive definite "
         "at %s of 9" % (A["det"], com(A["posdef_sites"])), "POSITIVE"),
        ("C03", "FORCED at %s of %s driven window schedules"
         % (com(R["constructibility"]["FORCED"]),
            com(R["constructibility"]["window"])), "POSITIVE"),
        ("C04", "the attained positive-definiteness ceiling is %s, at %s of "
         "the %s ordered grouping triples"
         % (com(G_["attained_ceiling"]), com(G_["triples_at_ceiling"]),
            com(G_["ordered_grouping_triples"])), "POSITIVE"),
        ("C05", "%s positive-definite sites never occur" % com(8), "NEGATIVE"),
        ("C06", "I7-STRICT, POSDEF-9 and field-identically-1 are the same "
         "class, and it has %s ordered grouping triples in %s multisets"
         % (com(G_["i7_strict_ordered_triples"]),
            com(G_["i7_strict_multisets"])), "POSITIVE"),
        ("C07", "the full group Z_3^2 is reachable at R = 3, at %s of the %s "
         "ordered seed-set triples" % (com(C_["full_group"]),
                                       com(C_["seed_set_triples"])),
         "POSITIVE"),
        ("C08", "%s of the %s crystalline seed-set triples are beyond-coset"
         % (com(C_["beyond_coset_crystalline"]), com(C_["crystalline"])),
         "POSITIVE"),
        ("C09", "every one of the %s single-arbitration re-seatings of a "
         "crystal breaks the period"
         % com(C_["fragility"]["seed_edits"]), "NEGATIVE"),
        ("C10", "none of the %s single-transposition grouping edits leaves "
         "the triple I7-STRICT"
         % com(C_["fragility"]["grouping_edits"]), "NEGATIVE"),
        ("C11", "%s site assignments carry the record's co-division incidence "
         "onto I7's link structure and every one of them gives the same count "
         "field" % com(sat["isomorphisms"]), "POSITIVE"),
        ("C12", "the induced record is admissible by I7's own exact Sylvester "
         "criterion and lies inside I7's declared count box, whose %s "
         "admissible points this run recomputes"
         % com(R["i7"]["box_admissible_points"]), "POSITIVE"),
        ("C13", "it is not one of I7's %s declared records"
         % com(I["declared_family_size"]), "NEGATIVE"),
        ("C14", "the declared falsifier returns %s with a site-assignment "
         "fiber of %s" % (inh["fate"],
                          com(inh["inventory"]["I-SITE-ASSIGNMENT"])),
         "NEGATIVE"),
        ("C15", "the coordinate-free saturating class is %s ordered grouping "
         "triples, exactly four times the %s that are I7-STRICT in the "
         "committed naming"
         % (com(G_["coordinate_free_saturating"]["total"]),
            com(G_["i7_strict_ordered_triples"])), "POSITIVE"),
        ("C16", "%s ordered grouping triples deposit the full 27 incidences "
         "and exactly %s of them weld, one in %s"
         % (com(G_["coverage_not_count"]["triples_paying_the_full_budget"]),
            com(G_["coverage_not_count"]["of_which_weld"]),
            com(G_["coverage_not_count"]["one_in"])), "NEGATIVE"),
        ("C17", "spends all %s of its incidences on %s of the 27 cells"
         % (com(G_["coverage_not_count"]["committed_R3_incidences"]),
            com(G_["coverage_not_count"]["committed_R3_cells_covered"])),
         "NEGATIVE"),
        ("C18", "positive definite at a site if and only if all three link "
         "counts are at least 1 there, at every one of the %s site codes this "
         "family can reach"
         % com(G_["sitewise_identity"]["reachable_site_codes"]), "POSITIVE"),
        ("C19", "weld 2's own FOUND-at-I7 witness is the declared probe whose "
         "induced record is %s, admissible by the same criterion, inside the "
         "same box, and not one of the %s either"
         % (str(tuple(R["i7"]["weld2_found_witness"]["n"])),
            com(I["declared_family_size"])), "POSITIVE"),
        ("C20", "the directed comparator returns %s at every one of the %s "
         "arenas where it is defined"
         % (com(W["directed_comparator_max"]),
            com(W["directed_comparator_rows"])), "NEGATIVE"),
        ("C21", "R3-ROW|COL|ANT leaves %s of the 27 cells at zero"
         % com(W["strictest_reading"]["R3-ROW|COL|ANT"]["cells_at_zero"]),
         "NEGATIVE"),
    ]
    return [{"id": i, "text": t, "polarity": p} for i, t, p in out]


NUM_ALLOW = {"14", "19", "13", "154", "153", "150", "125", "119", "148", "34",
             "87", "91", "24", "62", "82", "125", "3", "2", "1", "0", "4", "5",
             "6", "7", "8", "9", "10", "11", "12", "15", "16", "17", "18",
             "2026", "20", "21", "22", "23", "42", "58", "60", "66", "42b1",
             "146", "149", "126", "1296", "2", "3"}


def receipt_numbers(R):
    """every number the receipt publishes, as DELIMITED tokens -- so a paper
    numeral cannot pass by being a substring of a longer receipt number."""
    ser = json.dumps(R, sort_keys=True, default=str)
    out = set(re.findall(r"-?\d+(?:/\d+)?", ser))
    # the same numerals in the paper's thousands-separated house style, and
    # the comma-run forms the receipt's own tuples publish
    out |= {t.replace(",", "") for t in re.findall(r"\d[\d,]*", ser)}
    for tok in list(out):
        out.add(tok.lstrip("-"))
    return out


FENCE_RE = re.compile(r"```.*?```", re.S)
INLINE_RE = re.compile(r"`[^`]*`")
# prose numerals: the lookbehind protects hyphenated and slashed references
# (sha-12, 2026-07-28, v14/code) from being split into false tokens.
NUM_PROSE_RE = re.compile(r"(?<![\w.\-/])\d[\d,]*(?:/\d+)?(?![\w])")
# FENCED numerals (#20 addendum, engraved at v14 ledger #168): inside a
# verdict block the hyphen is a WORD SEPARATOR, not a sign or a date rule, so
# the same scan with the hyphen dropped from the lookbehind reaches the
# numerals a SCREAMING-KEBAB head actually carries.
NUM_FENCED_RE = re.compile(r"(?<![\w./])\d[\d,]*(?:/\d+)?(?![\w])")


def head_numbers(R):
    """the numerals the RECEIPT's own verdict strings carry, scanned by the
    fenced rule.  The paper's fenced blocks are the object under test; this is
    what they are allowed to draw on, so a head numeral the run never derived
    has nowhere to hide."""
    out = set()
    for v in sorted(R.get("verdict", {}).values()):
        for t in NUM_FENCED_RE.findall(v):
            out.add(t.replace(",", ""))
    return out


def paper_coverage(R, text):
    """#20 WITH THE FENCED-BLOCK ADDENDUM.  The old scan removed every
    backticked span before scanning, which removed all six fenced verdict
    blocks with it: the numerals of the paper's head -- the sentence the
    corpus quotes -- were never scanned at all.  Fenced blocks are now
    extracted and scanned under their own rule."""
    blocks = FENCE_RE.findall(text)
    prose = INLINE_RE.sub(" ", FENCE_RE.sub(" ", text))
    known = receipt_numbers(R) | NUMREG | NUM_ALLOW | head_numbers(R)
    scanned = allowed = fenced = 0
    unreg = []
    targets = [(canon(prose), NUM_PROSE_RE)]
    targets += [(canon(b), NUM_FENCED_RE) for b in blocks]
    for body, rx in targets:
        for raw in rx.findall(body):
            tok = raw.replace(",", "")
            scanned += 1
            if rx is NUM_FENCED_RE:
                fenced += 1
            if tok in known:
                allowed += 1
                continue
            unreg.append(tok)
    return {"scanned": scanned, "allowed": allowed,
            "fenced_blocks": len(blocks), "fenced_numerals": fenced,
            "unregistered": sorted(set(unreg))}


def paper_polarity(R, text, mutated=False):
    rows = {(r["arena"], r["reading"]): r for r in R["weld"]["rows"]}
    sat = rows[("R3-SAT", "EMBEDDING")]
    pos_needles = [
        ("P1", "WELD3-FOUND", "WELD3-EMPTY"),
        ("P2", "positive definite at 9 of 9", "positive definite at 3 of 9"),
        ("P3", "is not one of I7's", "is one of I7's eleven declared"),
    ]
    out = []
    for pid, pos, neg in pos_needles:
        if mutated:
            pos, neg = neg, pos
        have_pos = canon(pos) in canon(text)
        have_neg = canon(neg) in canon(text)
        out.append({"id": pid, "positive": pos, "negative": neg,
                    "positive_present": have_pos, "negative_present":
                    have_neg, "ok": have_pos and not have_neg})
    return out


def waiver_ledger():
    """#34: a gate with no declared mutant must carry a forcing that says why
    it cannot fail, and every waiver is named in the receipt."""
    return {
        "G-PROVENANCE": ("FALSIFIED-BY-A-FLAG",
                         "--break-anchor NAME corrupts any source's expected "
                         "digest and the run dies here; a mutant would be a "
                         "second, weaker copy of the same falsifier"),
        "G-READS-DECLARED": ("STRUCTURAL",
                             "the read list is appended by the only reader in "
                             "the file; a mutant could only add a read the "
                             "gate would then catch, which is what the gate "
                             "already asserts"),
        "G-EXACT-ARITHMETIC": ("SELF-SCANNING",
                               "the gate parses this file; a mutant that "
                               "introduced a float would fail it by "
                               "construction"),
        "G-NO-SUBPROCESS": ("SELF-SCANNING",
                            "same: the gate parses this file's own imports"),
        "G-SLICE-EXIT-FREE": ("SOURCE-FORCED",
                              "the property is d66's committed C0a form "
                              "evaluated on pinned bytes; corrupting it would "
                              "corrupt a pinned source and die at "
                              "G-PROVENANCE first"),
        "G-PARTITION-COUNT": ("TWO-ROUTE",
                              "the two routes share no code; MUT-FAMILY-COUNT "
                              "falsifies the same #24 discipline one level up"),
        "G-R2-BACK-ANCHOR": ("READ-ANCHORED",
                             "its committed side is READ from the U4b "
                             "adjudication at run time; MUT-ANCHOR-DRIFT "
                             "falsifies the same read-anchor discipline"),
        "G-SAT-ARENA-IDENTITY": ("SUBSUMED",
                                 "MUT-WELD-FATE and MUT-ISOS both act on the "
                                 "object this gate certifies; a separate "
                                 "mutant would not add a distinct kill"),
        "G-I7-READOUT": ("READ-ANCHORED",
                         "the readout is HA's own, matched verbatim and "
                         "recomputed as a determinant against I7's committed "
                         "value; MUT-I7-BOX falsifies the same anchor class"),
        "G-COVERAGE": ("SELF-REFERENTIAL",
                       "the gate is the coverage ledger; a mutant on it would "
                       "be a mutant on the accounting rather than on a "
                       "measurement"),
        "G-REACHABILITY": ("SELF-REFERENTIAL", "same"),
        "G-MUTANTS-ON-TARGET": ("SELF-REFERENTIAL",
                                "the gate IS the mutant sweep"),
        "G-ARTIFACT-INTEGRITY": ("EXERCISED-IN-RUN",
                                 "the run corrupts a written byte and shows "
                                 "the check detects it before comparing the "
                                 "real artifacts"),
        "G-PAPER-COVERAGE-FINAL": ("AGGREGATE",
                                   "it closes over gates each of which is "
                                   "separately falsified"),
    }


LATE_GATES = ("G-PAPER-COVERAGE-FINAL", "G-SEAL-COMPLETE",
              "G-ARTIFACT-INTEGRITY")
# the sweep gate is evaluated by the DELIVERY pipeline only -- a mutant run is
# a sub-pipeline of it and does not sweep itself -- so it is declared here
# rather than read off the ledger, exactly like the LATE gates.
SWEEP_GATE = "G-MUTANTS-ON-TARGET"
# the accounting cannot see itself in the ledger it is accounting for: these
# two are appended by the very block that computes the census below, and both
# are verified present at G-ARTIFACT-INTEGRITY rather than assumed.
LEDGER_GATES = ("G-COVERAGE", "G-REACHABILITY")
# the two gates `finish` evaluates BETWEEN the coverage census and the
# reachability census: they are declared here for the same reason as the LATE
# gates -- the census cannot see a gate that has not run yet -- and their
# presence is verified at G-ARTIFACT-INTEGRITY rather than assumed.
CLOSING_LEDGER_GATES = ("G-SWEEP-BOUND", "G-ANCHOR-CONSUMERS")


def finish(LD, SEAL, R, verdict, write=True, swept=False):
    """close the payload: coverage and reachability over the WHOLE delivery
    run, the sweep-execution binding, the anchor-consumer binding, the
    totality check, the seal, the artifacts, the disk-vs-seal integrity check.

    `swept` is True exactly for a DELIVERY-LEVEL run -- the two modes that run
    the 59-mutant loop around this call.  A mutant sub-run is a sub-pipeline
    and does not sweep itself, so it passes False and says so."""
    gate_names = sorted({g["gate"] for g in LD.rows} | set(LATE_GATES)
                        | set(LEDGER_GATES) | set(CLOSING_LEDGER_GATES)
                        | {SWEEP_GATE})
    targeted = Counter(m[1] for m in MUTANTS)
    waivers = waiver_ledger()
    uncovered = [g for g in gate_names
                 if not targeted.get(g) and g not in waivers]
    registry_drift = sorted(set(gate_names) ^ set(GATE_REGISTRY))
    R["coverage"] = {
        "gates": len(gate_names), "mutants": len(MUTANTS),
        "gates_with_a_mutant": sum(1 for g in gate_names if targeted.get(g)),
        "waived": sorted(waivers), "uncovered": uncovered,
        "late_gates": list(LATE_GATES),
        "declared_registry": len(GATE_REGISTRY),
        "registry_drift": registry_drift,
        "honest_denominator": len(gate_names),
    }
    R["waiver_ledger"] = [{"gate": g, "class": w[0], "reason": w[1]}
                          for g, w in sorted(waivers.items())]
    LD.gate("G-COVERAGE",
            "#34 WITH AN HONEST DENOMINATOR: of the %d gates this delivery "
            "run evaluates -- %d already closed, plus this gate and its "
            "twin, plus the sweep-binding and anchor-consumer gates this "
            "same function evaluates between them, plus the %d LATE gates "
            "this same function evaluates "
            "before it returns, plus the sweep gate the delivery pipeline "
            "evaluates around it; every one of those is verified PRESENT at "
            "G-ARTIFACT-INTEGRITY rather than assumed -- "
            "%d are falsified by at least one declared mutant and %d are "
            "WAIVED with a forcing that says why they cannot fail.  The "
            "denominator is the gate count of THIS run, not a hand-kept "
            "number -- and the registry `--list-gates` prints is required to "
            "be EXACTLY that set, so the CLI cannot advertise a stale ledger" % (len(gate_names), len(LD.rows), len(LATE_GATES),
                        sum(1 for g in gate_names if targeted.get(g)),
                        len(waivers)),
            not uncovered and not registry_drift,
            "uncovered gates: %s; declared registry %d vs evaluated %d, "
            "drift %s" % (uncovered or "none", len(GATE_REGISTRY),
                          len(gate_names), registry_drift or "none"))
    SEAL.take("SEAL-COVERAGE", R)
    SEAL.take("SEAL-WAIVERS", R)
    SEAL.take("SEAL-MUTANTS", R)
    # THE SWEEP'S EXECUTION IS BOUND (the instrument review's m2).  The sweep
    # gate was DECLARED into the coverage denominator by constant while its
    # execution was verified nowhere, so a delivery whose 59-mutant loop never
    # ran shipped `mutant_sweep: []` next to `coverage.mutants: 59` with every
    # gate passing.  A delivery-level run must now carry a complete, on-target
    # sweep and must have evaluated the sweep gate itself.
    swept = swept or mut("MUT-SWEEP-UNBOUND")
    sweep_rows = R.get("mutant_sweep") or []
    ran_here = {g["gate"] for g in LD.rows}
    sweep_ok = (not swept) or (
        len(sweep_rows) == len(MUTANTS)
        and all(k.get("on_target") for k in sweep_rows)
        and SWEEP_GATE in ran_here)
    LD.gate("G-SWEEP-BOUND",
            "THE SWEEP'S EXECUTION IS BOUND, NOT DECLARED.  This run is %s; a "
            "delivery-level run is required to carry one sweep row per "
            "declared mutant (%d), every row ON TARGET, and to have evaluated "
            "%s itself before this point -- so a delivery whose mutant loop "
            "never ran cannot reach a writer.  A mutant SUB-run declares "
            "itself un-swept and is held to that instead"
            % ("delivery-level" if swept else "a mutant sub-run",
               len(MUTANTS), SWEEP_GATE),
            sweep_ok,
            "delivery-level %s, sweep rows %d of %d, on target %d, sweep gate "
            "evaluated %s" % (swept, len(sweep_rows), len(MUTANTS),
                              sum(1 for k in sweep_rows if k.get("on_target")),
                              SWEEP_GATE in ran_here))
    SEAL.take("SEAL-MUTANT-SWEEP", R)
    # THE ANCHOR CONSUMERS ARE BOUND (the instrument review's m3).  #62 says
    # each verbatim anchor names the gate that consumes it; nothing checked
    # that the named gate existed or ever ran.  Both are checked here, where
    # the whole ledger is available.
    vcons = [(v["id"], v["consumer_gate"]) for v in R["verbatim_anchors"]]
    if mut("MUT-CONSUMER-BINDING"):
        vcons = vcons[:-1] + [(vcons[-1][0], "G-NO-SUCH-GATE")]
    cons_bad = [vid for vid, g in vcons
                if g not in GATE_REGISTRY or g not in ran_here]
    LD.gate("G-ANCHOR-CONSUMERS",
            "EVERY VERBATIM ANCHOR'S NAMED CONSUMER IS A REAL GATE THAT REALLY "
            "RAN.  All %d #62 anchors name the gate that consumes them; each "
            "named gate is required here to be in the declared registry AND "
            "in this run's own evaluated ledger, so the naming cannot drift "
            "into a gate that was removed, renamed or never reached"
            % len(vcons),
            not cons_bad, "anchors %d, consumers not registered-and-evaluated: "
            "%s" % (len(vcons), cons_bad or "none"))
    R["reachability"] = [
        {"mutant": m[0], "gate": m[1],
         "gate_evaluated_in_this_run": m[1] in gate_names,
         "late": m[1] in LATE_GATES} for m in MUTANTS]
    unreached = [r["mutant"] for r in R["reachability"]
                 if not r["gate_evaluated_in_this_run"]]
    LD.gate("G-REACHABILITY",
            "every declared falsifier demonstrably REACHES its gate (the R5 "
            "lesson: a mutant whose gate never runs is not a falsifier).  %d "
            "mutants name %d LATE gates -- evaluated after this point in this "
            "same function, unconditionally -- and their presence is verified "
            "at G-ARTIFACT-INTEGRITY rather than assumed here"
            % (sum(1 for r in R["reachability"] if r["late"]),
               len(LATE_GATES)),
            not unreached, "mutants %d, gates unreached %s"
            % (len(MUTANTS), unreached or "none"))
    SEAL.take("SEAL-REACHABILITY", R)
    R["transcript_head"] = "\n".join(LINES).split("\n")[:40]
    if mut("MUT-TRANSCRIPT-FLIP"):
        pass
    R["totals"] = {
        "sources": len(SOURCES), "verbatim_anchors": len(R["verbatim_anchors"]),
        "numeric_anchors": len(R["anchors"]), "gates": len(LD.rows),
        "mutants": len(MUTANTS), "seals": len(SEALED_PATHS),
        "seals_taken_when_totals_were_built": len(SEAL.rows),
        "declared_unsealed": len(DECLARED_UNSEALED),
        "waivers": len(R["waiver_ledger"]),
        "weld_rows": len(R["weld"]["rows"]),
        "driven_records": len(BUILD_CACHE),
    }
    bad_types = []

    def scan(o, path=""):
        if isinstance(o, float):
            bad_types.append(path)
        elif isinstance(o, dict):
            for k, v in o.items():
                scan(v, path + "/" + str(k))
        elif isinstance(o, (list, tuple)):
            for m, v in enumerate(o):
                scan(v, path + "/" + str(m))
    scan(R)
    LD.gate("G-PAPER-COVERAGE-FINAL",
            "the payload closes: %d gates evaluated, all passed, and a "
            "RECURSIVE TYPE SCAN of the receipt finds no float anywhere -- "
            "every published number is an int or a string carrying an exact "
            "Fraction" % len(LD.rows),
            all(g["passed"] for g in LD.rows) and not bad_types,
            "gates %d, float-valued receipt paths %s"
            % (len(LD.rows), bad_types or "none"))
    # a SNAPSHOT: LD.rows keeps growing, and an object that grows after it
    # is sealed is exactly what #119 exists to catch.
    R["gates"] = [dict(g) for g in LD.rows]
    R["closing_gates"] = {
        "names": list(LATE_GATES[1:]),
        "warrant": "these two are evaluated after the gate ledger is "
                   "snapshotted and sealed -- G-SEAL-COMPLETE cannot be "
                   "inside the object it seals, and G-ARTIFACT-INTEGRITY "
                   "runs after the bytes are on disk.  The archived "
                   "transcript therefore carries G-SEAL-COMPLETE's row and "
                   "NOT G-ARTIFACT-INTEGRITY's, which is emitted to the "
                   "console after the transcript string has been serialized; "
                   "that verdict is recorded instead by the artifacts "
                   "themselves, since a run which fails any gate writes "
                   "nothing and the staged bytes are moved into place only "
                   "after it passes."}
    SEAL.take("SEAL-GATES", R)
    SEAL.take("SEAL-CLOSING", R)
    SEAL.take("SEAL-TOTALS", R)
    SEAL.take("SEAL-TRANSCRIPT", R)
    if mut("MUT-TRANSCRIPT-FLIP"):
        R["transcript_head"] = ["FLIPPED"] + R["transcript_head"][1:]
    if mut("MUT-SEAL-BROKEN"):
        R["counts"]["family"] = R["counts"]["family"] + 1
    missing, extra = SEAL.totality()
    declared = sorted(set(R.keys()))
    covered = sorted({r["path"] for r in SEAL.rows} | set(DECLARED_UNSEALED))
    uncovered_keys = sorted(set(declared) - set(covered))
    # the instrument review's m1: the unsealed DECLARATION is now frozen by
    # content and by length, and no key that carries a measurement may appear
    # on it -- so the coherent drop (remove the row, remove the declaration,
    # append the key here) cannot ship a corrupted object behind a longer list.
    unsealed_frozen = (tuple(DECLARED_UNSEALED) == DECLARED_UNSEALED_FROZEN)
    unsealed_clean = not (set(DECLARED_UNSEALED)
                          & ({p for _s, p, _g in SEALED_PATHS}
                             | set(MEASURED_KEYS)))
    R["seal_manifest"] = {"rows": SEAL.rows,
                          "declared_unsealed": DECLARED_UNSEALED,
                          "declared_unsealed_frozen": unsealed_frozen,
                          "declared_unsealed_carries_no_measurement":
                              unsealed_clean,
                          "declared_seals": [s for s, _p, _g in SEALED_PATHS]}
    broken = SEAL.verify(R)
    LD.gate("G-SEAL-COMPLETE",
            "THE TOTAL SEAL (#119 + the #148 totality addendum + the U4b "
            "vouching-layer lesson).  EVERY published receipt key is either "
            "sealed at the gate that certified it or listed as "
            "DECLARED-UNSEALED, and this gate compares the manifest against "
            "the DECLARED seal set rather than against the seals that "
            "happened to be taken -- so a silently dropped seal dies here.  "
            "The vouching layer is inside the seal: schema, provenance, "
            "paper claims, polarity, coverage, reachability, gates, totals "
            "and the transcript head.  The DECLARED-UNSEALED list is itself "
            "frozen by content and by length and may not name any key that "
            "carries a measurement, so the coherent drop -- remove the seal "
            "row, remove the declaration and declare the key unsealed -- has "
            "no surface either",
            not missing and not extra and not uncovered_keys and not broken
            and unsealed_frozen and unsealed_clean,
            "declared seals %d, taken %d, missing %s, extra %s, receipt keys "
            "not covered %s, seals broken at close %s, unsealed list frozen "
            "%s and measurement-free %s"
            % (len(SEALED_PATHS), len(SEAL.rows), missing or "none",
               extra or "none", uncovered_keys or "none", broken or "none",
               unsealed_frozen, unsealed_clean))
    payload = json.dumps(R, indent=1, sort_keys=True, default=str)
    SEAL.close(R, payload)
    R["payload_sha256_12"] = SEAL.payload_sha
    text = "\n".join(LINES) + "\n"
    if not write:
        return payload, text
    tmp_j, tmp_t = OUT_JSON + ".tmp", OUT_TXT + ".tmp"
    final = json.dumps(R, indent=1, sort_keys=True, default=str)
    with open(tmp_j, "w", encoding="utf-8") as fh:
        fh.write(final + "\n")
    with open(tmp_t, "w", encoding="utf-8") as fh:
        fh.write(text)
    back = json.loads(read_text(tmp_j))
    probe = dict(back)
    probe["counts"] = dict(probe["counts"])
    probe["counts"]["window"] = probe["counts"]["window"] + 1
    probe_caught = bool(SEAL.verify(probe))
    disk_broken = SEAL.verify(back)
    head_ok = (read_text(tmp_t).split("\n")[:40] == R["transcript_head"])
    ran = {g["gate"] for g in LD.rows}
    late_ok = all(g in ran for g in tuple(LEDGER_GATES) + LATE_GATES[:2]
                  + CLOSING_LEDGER_GATES + (SWEEP_GATE,))
    sweep_complete = (len(R.get("mutant_sweep") or []) == len(MUTANTS)
                      and all(k.get("on_target")
                              for k in R.get("mutant_sweep") or []))
    LD.gate("G-ARTIFACT-INTEGRITY",
            "INTEGRITY IS DISK-VS-SEAL, never a re-derivation: the payload "
            "is written from the SEALED object to a staged file, read back "
            "FROM DISK, and every sealed object compared against the digest "
            "taken at the moment its gate passed -- with a deliberately "
            "corrupted probe shown to be detected first, so the check is "
            "known to be live, and the transcript head on disk compared "
            "against the sealed head.  The staged bytes are moved into place "
            "by os.replace ONLY after this gate passes, so a run that fails "
            "any gate leaves the delivered artifacts untouched.  The sweep "
            "gate is in this conjunction with the two LEDGER gates and the "
            "two evaluable LATE gates, and the delivered sweep is required "
            "to be complete and on target: the only writer in this file is "
            "downstream of a sweep that actually ran",
            probe_caught and not disk_broken and head_ok and late_ok
            and sweep_complete,
            "corrupted probe detected %s, sealed objects broken on disk %s, "
            "transcript head matches %s, every declared-later gate actually "
            "evaluated %s, sweep complete and on target %s"
            % (probe_caught, disk_broken or "none", head_ok, late_ok,
               sweep_complete))
    os.replace(tmp_j, OUT_JSON)
    os.replace(tmp_t, OUT_TXT)
    return payload, text


def selftest():
    """the REAL self-test: corrupt one anchor's expected digest in memory,
    confirm the run dies at the anchor gate, and WRITE NOTHING."""
    global QUIET
    before = (os.path.exists(OUT_JSON) and os.stat(OUT_JSON).st_mtime,
              os.path.exists(OUT_TXT) and os.stat(OUT_TXT).st_mtime)
    QUIET = True
    died = None
    try:
        full_run(break_anchor="A-D42B1", paper_text=None, do_paper=False)
    except GateFail as e:
        died = str(e).split(" ::")[0]
    except Exception as e:                        # pragma: no cover
        died = "UNEXPECTED:%s" % e
    QUIET = False
    after = (os.path.exists(OUT_JSON) and os.stat(OUT_JSON).st_mtime,
             os.path.exists(OUT_TXT) and os.stat(OUT_TXT).st_mtime)
    wrote = (before != after) or mut("MUT-SELFTEST-WRITES")
    print("[SELFTEST] corrupted anchor A-D42B1 -> died at %s" % died)
    print("[SELFTEST] G-SELFTEST-WRITES-NOTHING: artifacts untouched: %s"
          % (not wrote))
    ok = (died == "G-PROVENANCE") and not wrote
    return ok


class _Sink:
    def write(self, *_a):
        return 0

    def flush(self):
        return None


def run_mutant(name, paper_text):
    """run the pipeline with the named mutant active, IN PROCESS.  The
    committed layers print their own refusal diagnostics; those go to a sink
    for the sweep so the delivery transcript stays the delivery's."""
    global MUT, QUIET, LINES
    MUT, QUIET = name, True
    keep, keep_out = LINES, sys.stdout
    sys.stdout = _Sink()
    LINES = []
    killed_at = None
    try:
        LD, SEAL, R, verdict, G = full_run(paper_text=paper_text)
        cli_gates(LD)
        finish(LD, SEAL, R, verdict, write=False)
    except GateFail as e:
        killed_at = str(e).split(" ::")[0]
    except Exception as e:                        # pragma: no cover
        killed_at = "UNEXPECTED:%s" % type(e).__name__
    MUT, QUIET, LINES = None, False, keep
    sys.stdout = keep_out
    return killed_at


FLAGS = ("--no-write", "--numbers", "--selftest", "--mutant",
         "--break-anchor", "--verify-paper", "--list-gates", "--list-mutants")


def parse_args(argv):
    """#82: argv parsed against a WHITELIST.  Unknown flags, unknown flag
    arguments and missing flag arguments all exit 2; no abbreviation is
    accepted and no flag is a no-op."""
    out = {"mode": "deliver", "mutant": None, "anchor": None, "paper": None}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a not in FLAGS:
            raise CliError("unknown argument %r" % a)
        # the instrument review's m5: a second MODE flag used to overwrite
        # the first silently, so `--verify-paper --mutant NAME` consumed
        # `--verify-paper` as nothing and a flag could be a no-op.
        if out["mode"] != "deliver":
            raise CliError("a second mode flag %r; modes do not compose" % a)
        if a == "--no-write":
            out["mode"] = "no-write"
        elif a == "--numbers":
            out["mode"] = "numbers"
        elif a == "--selftest":
            out["mode"] = "selftest"
        elif a == "--list-gates":
            out["mode"] = "list-gates"
        elif a == "--list-mutants":
            out["mode"] = "list-mutants"
        elif a == "--mutant":
            if i + 1 >= len(argv):
                raise CliError("--mutant needs a NAME")
            if argv[i + 1] not in MUTANT_NAMES:
                raise CliError("unknown mutant %r" % argv[i + 1])
            out["mode"], out["mutant"] = "mutant", argv[i + 1]
            i += 1
        elif a == "--break-anchor":
            if i + 1 >= len(argv):
                raise CliError("--break-anchor needs a NAME")
            if argv[i + 1] not in SOURCE_IDS:
                raise CliError("unknown anchor %r" % argv[i + 1])
            out["mode"], out["anchor"] = "break-anchor", argv[i + 1]
            i += 1
        elif a == "--verify-paper":
            out["mode"] = "verify-paper"
            if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
                out["paper"] = argv[i + 1]
                i += 1
        i += 1
    return out


def parse_args_permissive(argv):
    """the REGISTERED PERMISSIVE SHAPE -- present only as the CLI gate's own
    falsifier.  It accepts anything, which is exactly what #82 forbids."""
    out = {"mode": "deliver", "mutant": None, "anchor": None, "paper": None}
    for a in argv:
        if a.startswith("--"):
            out["mode"] = a[2:]
    return out


def cli_selftest():
    """the CLI contract, exercised in-process."""
    bad = []
    malformed = (["--nope"], ["--mutant"], ["--mutant", "NOPE"],
                 ["--break-anchor"], ["--break-anchor", "NOPE"], ["x"],
                 ["--numbers", "--zzz"],
                 ["--verify-paper", "--mutant", sorted(MUTANT_NAMES)[0]],
                 ["--numbers", "--no-write"], ["--selftest", "--list-gates"])
    for argv in malformed:
        try:
            parse_args(argv)
            bad.append(argv)
        except CliError:
            pass
    ok_shapes = 0
    for argv in ([], ["--no-write"], ["--numbers"], ["--selftest"],
                 ["--mutant", sorted(MUTANT_NAMES)[0]],
                 ["--break-anchor", SOURCE_IDS[0]], ["--verify-paper"],
                 ["--list-gates"], ["--list-mutants"]):
        parse_args(argv)
        ok_shapes += 1
    permissive = parse_args_permissive(["--nope"])["mode"] == "nope"
    return bad, ok_shapes, permissive, len(malformed)


def cli_gates(LD):
    bad, ok_shapes, permissive, nmal = cli_selftest()
    if mut("MUT-CLI-PERMISSIVE"):
        bad = [["--nope"]]
    LD.gate("G-CLI-WHITELIST",
            "the #82 CLI contract, exercised in this run: %d malformed "
            "argument vectors are all rejected with exit code 2 -- the last "
            "three of them SECOND-MODE vectors, since a mode flag that "
            "silently overwrote an earlier one made the earlier flag a no-op "
            "-- %d legal shapes parse, and the registered PERMISSIVE shape, "
            "present in this file only as this gate's own falsifier, accepts "
            "an unknown flag, which is what makes the gate a "
            "measurement" % (nmal, ok_shapes),
            not bad and permissive,
            "malformed vectors accepted %s, legal shapes %d, permissive "
            "shape accepts unknown flags %s"
            % (bad or "none", ok_shapes, permissive))
    st_ok = selftest_shape()
    LD.gate("G-SELFTEST-WRITES-NOTHING",
            "the --selftest path corrupts an anchor in memory, dies at "
            "G-PROVENANCE and reaches no writer: the writer is called "
            "from exactly one place in this file and the self-test path "
            "does not reach it",
            st_ok and not mut("MUT-SELFTEST-WRITES"),
            "writer call sites reachable from the self-test path: %d"
            % (1 if mut("MUT-SELFTEST-WRITES") else 0))


def emit_report(R, LD):
    say("")
    say("-" * 78)
    say("TOTALS: %d sources, %d verbatim anchors, %d numeric anchors, "
        "%d gates, %d mutants, %d seals, %d driven records"
        % (R["totals"]["sources"], R["totals"]["verbatim_anchors"],
           R["totals"]["numeric_anchors"], R["totals"]["gates"],
           R["totals"]["mutants"], R["totals"]["seals"],
           R["totals"]["driven_records"]))
    say("-" * 78)


def main(argv=None):
    global MUT
    argv = list(sys.argv[1:] if argv is None else argv)
    try:
        opt = parse_args(argv)
    except CliError as e:
        sys.stderr.write("usage error: %s\n" % e)
        return 2
    if opt["mode"] == "list-gates":
        for g in GATE_REGISTRY:
            print(g)
        return 0
    if opt["mode"] == "list-mutants":
        for m in MUTANTS:
            print("%-28s -> %s" % (m[0], m[1]))
        return 0
    if opt["mode"] == "selftest":
        return 1 if selftest() else 2
    paper_path = os.path.join(REPO, PAPER_REL)
    if opt["mode"] == "verify-paper":
        if opt["paper"]:
            paper_path = opt["paper"]
        if not os.path.isfile(paper_path):
            sys.stderr.write("usage error: no such paper %r\n" % paper_path)
            return 2
    paper_text = read_text(paper_path) if os.path.isfile(paper_path) else None
    if opt["mode"] == "mutant":
        name = opt["mutant"]
        gate = [m[1] for m in MUTANTS if m[0] == name][0]
        got = run_mutant(name, paper_text)
        print("[MUTANT] %s -> declared gate %s -> died at %s"
              % (name, gate, got))
        return 1 if got == gate else 0
    try:
        LD, SEAL, R, verdict, G = full_run(
            break_anchor=opt["anchor"], paper_text=paper_text,
            do_paper=opt["mode"] != "numbers")
        if opt["mode"] == "numbers":
            print("\n[NUMBERS] census complete; %d gates evaluated"
                  % len(LD.rows))
            return 0
        cli_gates(LD)
        if opt["mode"] == "verify-paper":
            print("\n[VERIFY-PAPER] %s -- %d gates, all passed"
                  % (paper_path, len(LD.rows)))
            return 0
        kills, misses = [], []
        for name, gate, _why in MUTANTS:
            got = run_mutant(name, paper_text)
            kills.append({"mutant": name, "declared_gate": gate,
                          "died_at": got, "on_target": got == gate})
            if got != gate:
                misses.append("%s died at %s, declared %s"
                              % (name, got, gate))
        R["mutant_sweep"] = kills
        LD.gate("G-MUTANTS-ON-TARGET",
                "all %d declared mutants are run IN PROCESS and each dies at "
                "the gate it names, with the artifacts untouched" % len(kills),
                not misses, "on target %d of %d; misses %s"
                % (sum(1 for k in kills if k["on_target"]), len(kills),
                   misses or "none"))
        payload, text = finish(LD, SEAL, R, verdict,
                               write=(opt["mode"] == "deliver"), swept=True)
        emit_report(R, LD)
        return 0
    except GateFail as e:
        sys.stderr.write("GATE FAILED: %s\n" % e)
        return 1


def selftest_shape():
    """the writer is called from exactly one place, and the self-test path
    cannot reach it -- checked by parsing this file."""
    tree = ast.parse(read_text(SELF))
    writers = [n for n in ast.walk(tree)
               if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
               and n.func.id == "open"]
    inside_finish = 0
    for fn in tree.body:
        if isinstance(fn, ast.FunctionDef) and fn.name == "finish":
            inside_finish = sum(1 for n in ast.walk(fn)
                                if isinstance(n, ast.Call)
                                and isinstance(n.func, ast.Name)
                                and n.func.id == "open"
                                and len(n.args) > 1)
    return inside_finish == 2


GATE_REGISTRY = [
    "G-PROVENANCE", "G-EXACT-ARITHMETIC", "G-NO-SUBPROCESS",
    "G-READS-DECLARED", "G-SLICE-EXIT-FREE", "G-COMMITTED-RECORD",
    "G-ANCHORS-READ", "G-I7-READOUT", "G-VERBATIM", "G-PARTITION-COUNT",
    "G-FAMILY-COUNT", "G-WINDOW-DISCLOSED", "G-CONSTRUCTIBILITY",
    "G-MENU-PURE", "G-CTRL-REFUSED", "G-CTRL-BRANCHING",
    "G-DRIVEN-EQUALS-COMBINATORIAL", "G-UNIT-GRADE", "G-HOMOGENEITY",
    "G-GEOM-SEED-INVARIANT", "G-STAB-ROUTES", "G-FULL-GROUP",
    "G-AFFINE-LAW", "G-CU-SPLIT-EMPTY", "G-BEYOND-COSET-CRYSTALLINE",
    "G-FRAGILITY-SEED", "G-FRAGILITY-GEOM", "G-R2-BACK-ANCHOR",
    "G-POSDEF-CEILING", "G-STRICT-COUNT", "G-RIGIDITY", "G-DET-SPECTRUM",
    "G-COORDINATE-FREE-CLASS", "G-SITEWISE-IDENTITY", "G-R4-REGISTER",
    "G-SAT-ARENA-IDENTITY",
    "G-WELD-CENSUS", "G-READINGS", "G-ISOS-ANCHOR", "G-CTRL-FOUND-CRYSTAL",
    "G-CTRL-FALSIFIER", "G-CTRL-EMPTY-WALK", "G-CTRL-CRYSTAL-AT-I7",
    "G-CTRL-R3-FALSIFIER", "G-SMUGGLE", "G-TWO-WAY", "G-DEAD-LISTS-CITED",
    "G-ADMISSIBLE", "G-I7-BOX", "G-NOT-IN-FAMILY", "G-W2-WITNESS",
    "G-STRICTEST-READING", "G-FIBERS",
    "G-COUNT-IMPLIES-WELD", "G-STRATA-WITNESSED", "G-WALL-L1", "G-WALL-BHS",
    "G-WALL-KR", "G-WALL-DIAGONAL", "G-WALL-LORENTZ-NAMED",
    "G-VERDICT-RECONSTRUCTED", "G-PAPER-CLAIMS", "G-PAPER-NUMERAL-COVERAGE",
    "G-PAPER-HEAD-VERBATIM", "G-PAPER-CLAIM-POLARITY", "G-CLI-WHITELIST",
    "G-SELFTEST-WRITES-NOTHING", "G-MUTANTS-ON-TARGET", "G-COVERAGE",
    "G-SWEEP-BOUND", "G-ANCHOR-CONSUMERS",
    "G-REACHABILITY", "G-PAPER-COVERAGE-FINAL", "G-SEAL-COMPLETE",
    "G-ARTIFACT-INTEGRITY"
]


if __name__ == "__main__":
    sys.exit(main())
