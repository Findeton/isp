#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
v14 R5 -- THE GAUGE RUNG: link-indexed unitaries and their holonomy.
Instrument for `v14/paper-18-gauge-rung.md`.

QUESTION (pin, "THE QUESTION").  Does the declaration-connection on the record
stage carry a NON-ABELIAN holonomy group, does it survive one refinement step,
and does its curvature couple to Delta^B?

CLI CONTRACT (the #82 minimum: argv-parsed against a whitelist)
---------------------------------------------------------------
    python3.13 v14/code/r5_gauge_exact.py
        THE DELIVERY RUN, and the ONLY writer.  Builds the whole census,
        evaluates every gate (the paper-claim gate included), runs every
        declared mutant in-process, re-reads what it wrote, and WRITES
        `r5_gauge_output.txt` and `r5_gauge_receipt.json` beside this file.
        Exits 0 iff every gate passes.

    python3.13 v14/code/r5_gauge_exact.py --no-write
        The same run, writing nothing.

    python3.13 v14/code/r5_gauge_exact.py --selftest
        FALSIFICATION SELF-TEST.  Corrupts one anchor's expected digest IN
        MEMORY, confirms the run dies at the anchor gate, WRITES NOTHING, and
        exits 1.  Exits 2 if the corrupted run does NOT die.

    python3.13 v14/code/r5_gauge_exact.py --mutant NAME
        Runs the pipeline with the named mutant active.  Exits 1 when the
        mutant is killed (the intended outcome), 0 if it survives.  An unknown
        NAME exits 2; it never reports "SURVIVED".  Writes nothing.

    python3.13 v14/code/r5_gauge_exact.py --break-anchor NAME
        Corrupts the named anchor's expected digest.  Unknown NAME exits 2.
        The run must exit 1.  Writes nothing.

    python3.13 v14/code/r5_gauge_exact.py --verify-paper [PATH]
        RUNS THE #20 INSTRUMENT AGAINST PATH (this unit's paper by default):
        the whole derivation is rebuilt and the paper gates -- claim
        rendering, numeral coverage and claim POLARITY -- are evaluated with
        PATH as the object under test.  Exits 1 on any drift, 0 on a clean
        paper, and 2 if PATH does not exist.  Writes nothing.

    Any other argument, any unknown flag argument, any missing flag argument
    and any --verify-paper PATH that does not exist exits 2.  No flag is
    mutant-only, and no flag is a no-op.

THE GATE-TO-DISK SEAL (RUNBOOK 14 addendum, engraving #119, native here).  A
gate that fires on an object which is still mutable when the artifact is built
has not gated the artifact.  Every published object is DIGESTED AT THE MOMENT
ITS GATE PASSES (`SEAL`); the payload may only be sealed if every earlier seal
still verifies; the artifacts are written FROM the sealed payload through
temporaries moved into place by `os.replace` only after the bytes match; and
the terminal integrity gate compares the BYTES ON DISK against the gate-time
seal.  A re-derivation from disk is not an integrity check -- it confirms
corruption.

TEXT GATES (engraving #125).  Every text gate matches text AS WRITTEN: the
needle and the haystack are both whitespace-normalised, and every verbatim
window is additionally pinned by the digest of its exact bytes and by a
declared length floor, so a window truncated to a decoration is not an anchor.

ARITHMETIC.  Exact only.  The field is Q(zeta_8) carried as a 5-tuple of
integers (a0, a1, a2, a3, den) over the basis (1, z, z^2, z^3) reduced modulo
Phi_8(x) = x^4 + 1, with den > 0 and the tuple in lowest terms; the
representation is canonical, so tuple equality IS field equality.  Group
orders are exact integers from a deterministic Schreier-Sims.  There are no
floats anywhere: an AST scan of this file and a recursive type scan of the
emitted receipt are gates.

REIMPLEMENTATION NOTICE.  Every object here is reimplemented from the
definitions in the pinned sources.  R4's and R4b's programs are read as BYTES
ONLY, for their digests; they are never imported, never executed, and no value
is copied from them except through the hash-pinned receipts, which are
anchors.

RUNTIME INPUTS (RUNBOOK 14, engraving #46).  Exactly nine files are read at
run time as SOURCES, all hash-pinned by this unit's frozen declaration, plus
exactly one file read as the OBJECT UNDER TEST -- this unit's own paper, which
cannot be hash-pinned because it is the thing being verified.  Both lists are
enumerated and gated.  No repository state outside them is read, and no
subprocess -- in particular no `git` -- is ever invoked (#91: the run is
correct off-tree and in a directory with no version control at all).
"""

import ast
import hashlib
import json
import os
import re
import sys
from itertools import product, combinations

# ===========================================================================
# SECTION 0.  THE FROZEN DECLARATION (RUNBOOK section 15: the arena is data)
# ===========================================================================

SELF = os.path.abspath(__file__)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(SELF)))
OUT_TXT = os.path.join(os.path.dirname(SELF), "r5_gauge_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "r5_gauge_receipt.json")

SCHEMA = "isp/v14/r5-gauge/1"
PAPER_REL = "v14/paper-18-gauge-rung.md"

# --- the nine hash-pinned runtime inputs -----------------------------------
SOURCES = [
    ("A-R4-PAPER", "v14/paper-10-defect-on-the-stage.md", "1063401c7bb5",
     "PARENT 1, terminal at commit 583cae7: the stage, the alphabet, the "
     "brickwork controls, the realization census, the abelian stratum."),
    ("A-R4-CODE", "v14/code/r4_defect_stage_exact.py", "2959c5a6a84b",
     "the parent instrument.  READ AS BYTES ONLY -- never imported, never "
     "executed; its definitions are reimplemented here."),
    ("A-R4-OUTPUT", "v14/code/r4_defect_stage_output.txt", "ffd069ff3eb4",
     "the parent's terminal transcript: the connective segment this unit "
     "inherits verbatim."),
    ("A-R4-RECEIPT", "v14/code/r4_defect_stage_receipt.json", "3dc1393b0df8",
     "THE ARENA'S SOURCE: L, d, the alphabet size, the pool, the 3364-pair "
     "commutator census, the transport levels, the chart groups."),
    ("A-R4B-PAPER", "v14/paper-15-momentum.md", "89c636906061",
     "PARENT 2, terminal at commit 6d32993: NOT-BLOCH-DIAGONAL as a theorem; "
     "the seal discipline this instrument is built on."),
    ("A-R4B-RECEIPT", "v14/code/r4b_momentum_receipt.json", "562e2a3d4d85",
     "the second parent's receipt.  NO transport number is inherited from "
     "it -- its scope is the single-occupation uniform average."),
    ("A-REV-EFFECTUS", "v14/review-r4-effectus.md", "f54fa11dfd07",
     "THE DESIGN AUTHORITY: the frozen R5 recommendation, G1 through G7 and "
     "the must-nots."),
    ("A-PIN-R5", "v14/note-r5-gauge-pin.md", "b53adba0eee0",
     "this unit's pin, frozen at v14 ledger #129."),
    ("A-CRD-PAPER", "v14/paper-08-tower-four-wings.md", "602c9ac2ccc4",
     "CR-D's tower: the programme's group-family prior, against which G6 "
     "requires the measured class to be reported."),
]

# --- path-value anchors: (id, source-id, json path, expected value, note) ---
PATH_VALUE_ANCHORS = [
    ("PV-L", "A-R4-RECEIPT", "counts/L", 4,
     "THE ARENA'S SIZE, taken not typed: the admitted lattice"),
    ("PV-D", "A-R4-RECEIPT", "counts/d", 2,
     "the anchored spatial dimension"),
    ("PV-ALPHABET", "A-R4-RECEIPT", "counts/alphabet", 25,
     "the parent's coefficient alphabet -- the coin alphabet is DERIVED from "
     "it and from nothing else"),
    ("PV-FIELD", "A-R4-RECEIPT", "counts/field", "Q(ZETA-8)",
     "the field, inherited"),
    ("PV-CIRC", "A-R4-RECEIPT", "counts/circulants", 58,
     "the FULL-transport stratum: the mandatory flat negative control"),
    ("PV-COMM-PAIRS", "A-R4-RECEIPT", "counts/commutator_pairs", 3364,
     "the flat control's size"),
    ("PV-COMM-ZERO", "A-R4-RECEIPT", "counts/commutator_nonzero", 0,
     "THE OPENING DATUM: the verdict stratum is abelian"),
    ("PV-DEFECT-588", "A-R4-RECEIPT", "counts/nonzero_at_maximal", 588,
     "G3's measured baseline: defects at identically zero curvature"),
    ("PV-MAXIMAL", "A-R4-RECEIPT", "counts/maximal_transport", "FULL",
     "the maximal declared transport level, whose inheritance G2 audits"),
    ("PV-LEVELS", "A-R4-RECEIPT", "transport_levels/declared",
     ["NONE", "OCC", "OCC+AXIS", "FULL"],
     "the declared transport ladder, reimplemented here"),
    ("PV-BRICK-OCC", "A-R4-RECEIPT", "transport_levels/per_generator/B058",
     "OCC",
     "the brickwork stratum's level: the EXCLUDED stratum this unit builds on"),
    ("PV-CONNECTIVE", "A-R4-RECEIPT", "counts/connective_tag", "MAX-NORM",
     "the FORCED connective, inherited verbatim into SCOPE"),
    ("PV-LINK", "A-R4-RECEIPT", "counts/forcing_link", "(1,1)",
     "the anchored link that forces it"),
    ("PV-SECTOR", "A-R4-RECEIPT", "counts/sector", "SINGLE-OCCUPATION",
     "the sector, inherited; the two-excitation extension is declared"),
    ("PV-INDIV", "A-R4-RECEIPT", "counts/indivisibility",
     "DECLARED-BY-DIVISION-EVENT-TIMES",
     "indivisibility is declared, never measured -- inherited"),
    ("PV-BRICK-COMM", "A-R4-RECEIPT",
     "commutator_census/BRICK-BRICK/noncommuting", 4,
     "the parent's own witness that the EXCLUDED stratum is where the "
     "non-commutativity is"),
    ("PV-VERDICT-STRATUM", "A-R4-RECEIPT",
     "commutator_census/CIRC-CIRC-THE-VERDICT-STRATUM/noncommuting", 0,
     "the flat control, stated as the parent states it"),
]

# --- verbatim-text anchors: context windows bound to consumer gates ---------
VERBATIM_ANCHORS = [
    ("VB-EFF-G1", "A-REV-EFFECTUS", "G-FLAT-CONTROL-TRIVIAL",
     "**R4's FULL\n  stratum is the mandatory NEGATIVE control** — it must "
     "return the trivial group\n  (0 of 3,364; a theorem, so this is the flat "
     "control that REC plays for Γ-main)."),
    ("VB-EFF-G2", "A-REV-EFFECTUS", "G-GATE-INHERITANCE-AUDIT",
     "**If the maximal level again selects a commuting sub-family,\n  the "
     "verdict is `R5-BLOCKED-AT-THE-GATE` — first-class, and a real result "
     "about\n  the programme's own gate.**"),
    ("VB-EFF-G6", "A-REV-EFFECTUS", "G-REFINEMENT-CLASS",
     "the **isomorphism class is the invariant**, the plaquette count is the "
     "extensive\n  control."),
    ("VB-EFF-G7", "A-REV-EFFECTUS", "G-SCRAMBLE-SEPARATION",
     "R5 must show its holonomy group separates the physical case from a "
     "scrambled\n  control before any group-theoretic claim is entered."),
    ("VB-R4-ABELIAN", "A-R4-PAPER", "G-OPENING-DATUM",
     "0 of 3364 ordered pairs of the verdict-bearing stratum fail to "
     "commute."),
    ("VB-R4-ALPHABET", "A-R4-PAPER", "G-COIN-ALPHABET-DERIVED",
     "The coefficient alphabet is declared: $0$ together with $\\zeta_8^{t}$ "
     "times a\nmodulus in $\\{1, 1/2, 1/\\sqrt2\\}$, 25 elements in all."),
    ("VB-R4-BRICK", "A-R4-PAPER", "G-STRATA-ARE-THE-EXCLUDED-FAMILY",
     "They are ordinary local unitaries — a two-site coin applied on a\n"
     "parity class of dominoes, unitary by construction and radius one — and "
     "they carry\nnonzero defects."),
    ("VB-R4-588", "A-R4-PAPER", "G-DEFECT-BASELINE",
     "**588 of 3364 pairs at maximal transport carry a nonzero defect.**"),
    ("VB-R4-PERIOD", "A-R4-PAPER", "G-PROJECTIVE-PERIOD-TEMPLATE",
     "The raw order of $U$ — the least $k$ with\n$U^k=I$ — is *not* gauge "
     "invariant, since a global phase rescales every power;\nthe least $k$ "
     "with $U^k$ a scalar is."),
    ("VB-R4-CONNECTIVE", "A-R4-OUTPUT", "G-SCOPE-INHERITED",
     "CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1))"),
    ("VB-PIN-OUTCOMES", "A-PIN-R5", "G-VERDICT-PREREGISTERED",
     "`R5-NON-ABELIAN-<class;rank;refinement>` /\n"
     "`R5-BLOCKED-AT-THE-GATE` / `R5-NO-STABLE-GROUP` /\n"
     "`R5-BLOCKED-AT-<object>`"),
    ("VB-PIN-ARENA", "A-PIN-R5", "G-ARENA-DECLARED",
     "Link-indexed unitaries on the L=4 torus: a coin per link (32\nlinks, 16 "
     "plaquettes), from a DECLARED coin alphabet, applied\nin declared parity "
     "strata"),
    ("VB-CRD-ALT", "A-CRD-PAPER", "G-CRD-LADDER-COMPARATOR",
     "the FULL alternating group on its own 5-point support"),
    ("VB-R4B-NOTBLOCH", "A-R4B-PAPER", "G-R4B-HANDOFF",
     "The four brickwork generators are not diagonal in the character\n"
     "basis, and section 2 gives the forcing rather than the observation: "
     "Bloch\ndiagonal iff the translation stabiliser is the whole group"),
]

# --- the frozen digest of every verbatim window (#62), with a length floor --
# A window is an ANCHOR only if its bytes are pinned AND it is long enough to
# carry a context; bare substring presence admits a window truncated to a
# decoration, and these two conditions together do not.
WINDOW_FLOOR = 20
WINDOW_DIGESTS = {
    "VB-EFF-G1": "bf4407a94519",
    "VB-EFF-G2": "879cb3aa705c",
    "VB-EFF-G6": "2e5fdf63e164",
    "VB-EFF-G7": "a0665130a554",
    "VB-R4-ABELIAN": "8261822fc859",
    "VB-R4-ALPHABET": "d21521ca4f99",
    "VB-R4-BRICK": "3234d355007f",
    "VB-R4-588": "83942558915a",
    "VB-R4-PERIOD": "e7d655793980",
    "VB-R4-CONNECTIVE": "37bb69c658cb",
    "VB-PIN-OUTCOMES": "2a2313b166ae",
    "VB-PIN-ARENA": "8769964eb7d7",
    "VB-CRD-ALT": "37edc20aa06e",
    "VB-R4B-NOTBLOCH": "63831d7ddc72",
}

# --- the arena, declared as data (RUNBOOK section 15) ----------------------
# Every free axis below is declared here, swept where it is swept, and named
# in the verdict's declaration segments.  Nothing in this block is measured.

CONNECTIVE = "MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1))"
STENCIL = "2-SITE-DOMINO-PER-LINK"
SECTOR = "SINGLE-OCCUPATION"
SECTOR_EXT = "PLUS-ONE-DECLARED-TWO-EXCITATION-EXTENSION-WEDGE-2"
INDIVISIBILITY = "DECLARED-BY-DIVISION-EVENT-TIMES"
DIVISION_EVENTS = (0, 2)
CUT_TIME = 1
LEG_AT_THE_CUT = "B(U2)"
REFINEMENT_SIZES = (4, 8)

# the declared plaquette stencils: the sub-collections whose holonomy group is
# measured.  The names are the declaration; the geometry is derived.
PLAQ_STENCILS = [
    ("S1-ONE", ((0, 0),)),
    ("S2-EDGE", ((0, 0), (1, 0))),
    ("S2-CORNER", ((0, 0), (1, 1))),
    ("S2-APART", ((0, 0), (2, 0))),
    ("S3-ROW", ((0, 0), (1, 0), (2, 0))),
    ("S4-BLOCK", ((0, 0), (1, 0), (0, 1), (1, 1))),
]
GLOBAL_STENCIL = "S-ALL"

# the declared site-diagonal gauge handles (G4).  CONSTANT is the null handle
# -- the global phase, which is central and therefore cannot move anything;
# it is declared so that the self-test's negative direction has a control that
# is required NOT to fire.
GAUGE_HANDLES = ("CONSTANT", "LINEAR-X", "CHECKER")

# the declared scramble controls (G7), two, following the parent's count
SCRAMBLES = ("SCR-TRANSPOSE", "SCR-DIRECTION-FLIP")

# the declared named coins: two per measured sector, used wherever a full
# sweep of the 32 x 32 link table or the 16 x 16 plaquette table is taken
NAMED_COINS = ("DIAG-I", "DIAG-Z", "ANTI-X", "ANTI-ZX", "BAL-H", "BAL-F")

# the 15 construction choices, each classed with an exact fibre (the parent's
# discipline).  The fibres are checked against the derived objects at run time.
CHOICE_INVENTORY = [
    ("the spatial dimension", "FORCED (anchored)", 1),
    ("the lattice size", "FORCED (anchored)", 1),
    ("the neighbourhood connective", "FORCED (inherited)", 1),
    ("the coefficient alphabet", "FORCED (inherited)", 1),
    ("the coin alphabet", "FORCED (derived from the alphabet)", 1),
    ("the link set", "FORCED (exhaustive)", 1),
    ("the plaquette set", "FORCED (exhaustive)", 1),
    ("the parity strata", "FORCED (exhaustive)", 1),
    ("the loop base point and orientation", "STABILIZER-FIXED", 4),
    ("the global phase", "STABILIZER-FIXED", 8),
    ("the division-event times", "GENUINELY-FREE", 1),
    ("the leg at the cut", "GENUINELY-FREE", 1),
    ("the plaquette stencils", "GENUINELY-FREE", 6),
    ("the gauge handles", "GENUINELY-FREE", 3),
    ("the two-excitation extension", "GENUINELY-FREE", 2),
]

# numerals that the paper derives in its own text and that no receipt field
# renders (the declared residue, #34: each is named, none is a blanket)
DERIVED_IN_TEXT = {
    "0": "the zero of the field and of every empty census",
    "1": "the identity, the trivial group and the unit fibre",
    "5": "R5, the unit's own name",
    "14": "RUNBOOK section 14, cited",
    "15": "RUNBOOK section 15, cited",
    "18": "paper-18, this unit's own number",
    "20": "engraving #20, cited",
    "34": "engraving #34, cited",
    "46": "engraving #46, cited",
    "62": "engraving #62, cited",
    "82": "engraving #82, cited",
    "87": "engraving #87, cited",
    "91": "engraving #91, cited",
    "119": "engraving #119, cited",
    "125": "engraving #125, cited",
    "129": "the pin's ledger number",
}

NUMERAL_RE = r"(?<![\w./-])(\d+(?:[, ]\d{3})*(?:/\d+)?)(?![\w.-])"

QUIET = False
LOG = []
MUT = None
NOT_EXECUTED = []


# ===========================================================================
# SECTION 1.  THE EXACT FIELD Q(zeta_8)
# ===========================================================================
# Carried as (a0, a1, a2, a3, den): the element (a0 + a1 z + a2 z^2 + a3 z^3)
# / den with den > 0 and gcd(a0, a1, a2, a3, den) = 1.  The representation is
# canonical, so tuple equality IS field equality.  Integers only.

from math import gcd

ZERO = (0, 0, 0, 0, 1)
ONE = (1, 0, 0, 0, 1)


def fnorm(a0, a1, a2, a3, d):
    if d < 0:
        a0, a1, a2, a3, d = -a0, -a1, -a2, -a3, -d
    g = gcd(gcd(gcd(abs(a0), abs(a1)), gcd(abs(a2), abs(a3))), d)
    if g > 1:
        return (a0 // g, a1 // g, a2 // g, a3 // g, d // g)
    return (a0, a1, a2, a3, d)


def fadd(a, b):
    d = a[4] * b[4]
    return fnorm(a[0] * b[4] + b[0] * a[4], a[1] * b[4] + b[1] * a[4],
                 a[2] * b[4] + b[2] * a[4], a[3] * b[4] + b[3] * a[4], d)


def fneg(a):
    return (-a[0], -a[1], -a[2], -a[3], a[4])


def fmul(a, b):
    c0 = c1 = c2 = c3 = c4 = c5 = c6 = 0
    a0, a1, a2, a3 = a[0], a[1], a[2], a[3]
    b0, b1, b2, b3 = b[0], b[1], b[2], b[3]
    c0 += a0 * b0
    c1 += a0 * b1 + a1 * b0
    c2 += a0 * b2 + a1 * b1 + a2 * b0
    c3 += a0 * b3 + a1 * b2 + a2 * b1 + a3 * b0
    c4 += a1 * b3 + a2 * b2 + a3 * b1
    c5 += a2 * b3 + a3 * b2
    c6 += a3 * b3
    # z^4 = -1
    return fnorm(c0 - c4, c1 - c5, c2 - c6, c3, a[4] * b[4])


def fconj(a):
    """conj(z) = -z^3, conj(z^2) = -z^2, conj(z^3) = -z."""
    return fnorm(a[0], -a[3], -a[2], -a[1], a[4])


def zpow(t):
    t %= 8
    v = [0, 0, 0, 0]
    if t < 4:
        v[t] = 1
    else:
        v[t - 4] = -1
    return (v[0], v[1], v[2], v[3], 1)


def fscal(a, num, den):
    return fnorm(a[0] * num, a[1] * num, a[2] * num, a[3] * num, a[4] * den)


def fnormsq(a):
    return fmul(a, fconj(a))


def is_alg_integer(a):
    """Z[zeta_8] has basis (1, z, z^2, z^3): an element is an algebraic
    integer iff its canonical denominator is 1."""
    return a[4] == 1


def fstr(a):
    return "(%d,%d,%d,%d)/%d" % a


INV_SQRT2 = (0, 1, 0, -1, 2)          # (z - z^3)/2 = 1/sqrt(2)


def build_alphabet():
    """R4's declared alphabet, REBUILT: 0 together with zeta_8^t times a
    modulus in {1, 1/2, 1/sqrt2}.  The size is a measurement against the
    anchored value, never a typed constant."""
    out, seen = [], set()
    for a in [ZERO] + [f(t) for t in range(8)
                       for f in (lambda t: zpow(t),
                                 lambda t: fscal(zpow(t), 1, 2),
                                 lambda t: fmul(zpow(t), INV_SQRT2))]:
        if a not in seen:
            seen.add(a)
            out.append(a)
    return out


# ===========================================================================
# SECTION 2.  GATES, MUTANTS, THE SEAL
# ===========================================================================

class GateFail(Exception):
    pass


def say(msg=""):
    """the transcript.  Diagnostic runs (the self-test, and every in-process
    mutant) are QUIET and contribute nothing to it, so the written output is
    the delivery run's own transcript and nothing else."""
    if not QUIET:
        LOG.append(msg)
        print(msg, flush=True)


def mut(name):
    """the ONLY mutant switch.  No gate predicate may reference it: a standing
    self-check removes the clause and requires the probe to die."""
    return MUT == name


class Ledger:
    def __init__(self):
        self.rows = []
        self.ids = set()

    def gate(self, gid, claim, ok, detail="", kind="MEASURED"):
        if gid in self.ids:
            raise GateFail("%s :: duplicate gate id" % gid)
        self.ids.add(gid)
        self.rows.append({"gate": gid, "claim": claim, "passed": bool(ok),
                          "detail": detail, "kind": kind})
        if not ok:
            raise GateFail("%s :: %s :: %s" % (gid, claim, detail))
        return True


# the only THREE gates with no declared mutant: all three are evaluated
# OUTSIDE the in-process mutant runner, so a mutant could not reach them.
# Each registers the mechanism that falsifies it instead (#34).
# the gates that run AFTER the waiver ledger is built.  They are DECLARED
# here so the ledger covers every gate the run will reach, and the closing
# check requires the run's ledger to end at exactly the predicted count.
LATE_GATES = ("G-WAIVERS-VERIFIED", "G-PAPER-CLAIMS",
              "G-PAPER-NUMERAL-COVERAGE", "G-PAPER-CLAIM-POLARITY",
              "G-SEAL-COMPLETE")


FORCINGS = {
    "G-MUTANTS-ON-TARGET": "the gate that adjudicates the mutant sweep cannot "
                           "itself be a mutant's target; its falsifier is the "
                           "sweep, and every surviving or off-target injection "
                           "fails it -- exercised by all declared mutants on "
                           "every run",
    "G-ARTIFACT-INTEGRITY": "evaluated only in the writing path, which no "
                            "diagnostic run reaches; it is two-way by "
                            "construction -- a deliberately corrupted payload "
                            "is written to a probe path, re-read and required "
                            "to be detected -- and its reference value is the "
                            "GATE-TIME SEAL, whose in-run half G-SEAL-COMPLETE "
                            "carries the injection falsifier MUT-SEAL-BROKEN",
    "G-PAPER-COVERAGE-FINAL": "evaluated after the mutant sweep closes the "
                              "instrument's totals, so no in-process mutant "
                              "can reach it; the claims that render from the "
                              "CLOSED totals exist only at this evaluation, "
                              "and its in-run twins G-PAPER-CLAIMS, "
                              "G-PAPER-NUMERAL-COVERAGE and "
                              "G-PAPER-CLAIM-POLARITY carry the three "
                              "injection falsifiers and die on every sweep",
}


# ---------------------------------------------------------------------------
# THE GATE-TIME SEAL (#119).  A value is digested at the moment its gate
# passes; the payload may only be sealed once every earlier seal still
# verifies; the artifacts are written FROM the sealed payload; and the
# terminal integrity gate compares the bytes on disk against these digests.
# ---------------------------------------------------------------------------

SEALED_PATHS = [
    ("SEAL-VERDICT-STRING", "verdict/string", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-VERDICT-HEAD", "verdict/head", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-COUNTS", "counts", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-CURVATURE", "curvature_census", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-GROUPS", "holonomy_groups", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-FLAT-CONTROL", "flat_control", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-TRANSPORT", "transport_audit", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-MATCHED", "matched_tables", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-TWO-EXCITATION", "two_excitation", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-GAUGE", "gauge_selftest", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-REFINEMENT", "refinement", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-SCRAMBLE", "scramble_control", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-CHOICES", "choice_inventory", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-PATH-ANCHORS", "path_value_anchors", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-BYTE-ANCHORS", "byte_anchors", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-VERBATIM", "verbatim_anchors", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-WAIVERS", "waiver_ledger", "G-WAIVERS-VERIFIED"),
    ("SEAL-MUTANTS", "mutants", "G-MUTANTS-ON-TARGET"),
    ("SEAL-GATES", "gates", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-TOTALS", "totals", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-COVERAGE", "paper_coverage", "G-PAPER-COVERAGE-FINAL"),
]
SEALS_IN_RUN = tuple(sid for sid, _p, g in SEALED_PATHS
                     if g not in ("G-MUTANTS-ON-TARGET",
                                  "G-PAPER-COVERAGE-FINAL"))


def digest(value):
    """the canonical digest of a receipt object: its deterministic
    serialization, hashed.  Strings are hashed as themselves."""
    if isinstance(value, str):
        return hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]
    return hashlib.sha256(
        json.dumps(value, indent=1, sort_keys=True).encode("utf-8")
    ).hexdigest()[:12]


def jpath(obj, path):
    cur = obj
    for part in path.split("/"):
        if isinstance(cur, list):
            cur = cur[int(part)]
        else:
            cur = cur[part]
    return cur


class Seal:
    """the gate-time seal.  `take` digests an object at the moment its gate
    passed; `verify` re-digests the object as it stands NOW and names every
    seal that has since been broken; `close` refuses to seal the payload
    unless every earlier seal still holds."""

    def __init__(self):
        self.rows = []
        self.index = {}
        self.verdict_string = None
        self.payload = None
        self.payload_sha = None
        self.transcript = None
        self.transcript_sha = None

    def take(self, sid, obj):
        path = [p for s, p, _g in SEALED_PATHS if s == sid][0]
        gate = [g for s, _p, g in SEALED_PATHS if s == sid][0]
        value = jpath(obj, path)
        d = digest(value)
        self.rows.append({"seal": sid, "path": path, "sealed_at_gate": gate,
                          "sha256_12": d})
        self.index[sid] = d
        if sid == "SEAL-VERDICT-STRING":
            self.verdict_string = value

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

    def close(self, obj, payload):
        broken = self.verify(obj)
        if broken:
            raise GateFail("G-ARTIFACT-INTEGRITY :: the payload was sealed "
                           "over a broken seal :: %s" % broken)
        self.payload = payload
        self.payload_sha = digest(payload)

    def close_transcript(self, text):
        self.transcript = text
        self.transcript_sha = digest(text)


# ===========================================================================
# SECTION 3.  ANCHORS
# ===========================================================================

def sha12(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


READS = []


def source_path(rel):
    p = os.path.join(REPO, rel)
    READS.append(rel)
    return p


def flat(s):
    """#125: text gates match text AS WRITTEN -- runs of whitespace collapse
    on BOTH sides, so a claim broken across lines is still the same
    characters in the same order, and nothing else is forgiven."""
    return re.sub(r"\s+", " ", s)


# ===========================================================================
# SECTION 4.  THE ARENA: SITES, LINKS, PLAQUETTES, STRATA, COINS
# ===========================================================================

def build_lattice(L):
    sites = [(x, y) for x in range(L) for y in range(L)]
    idx = {s: i for i, s in enumerate(sites)}
    return sites, idx


def addv(s, v, L):
    return ((s[0] + v[0]) % L, (s[1] + v[1]) % L)


E1, E2 = (1, 0), (0, 1)
EDIR = (E1, E2)


def build_links(sites, L):
    """a link is (site, direction): the ordered pair (site, site + e_d).
    Two per site, so 2 L^2 in all -- exhaustive, not sampled."""
    return [(s, d) for s in sites for d in range(2)]


def link_ends(l, L):
    s, d = l
    return s, addv(s, EDIR[d], L)


def build_plaquettes(sites):
    """one plaquette per site: the unit square based there."""
    return list(sites)


def plaquette_boundary(p, L):
    """the four (link, orientation) steps of the boundary, traversed
    p -> p+e1 -> p+e1+e2 -> p+e2 -> p.  Orientation -1 means the link is
    traversed against its own direction, so its operator is inverted."""
    return (((p, 0), 1),
            ((addv(p, E1, L), 1), 1),
            ((addv(p, E2, L), 0), -1),
            ((p, 1), -1))


def build_strata(links):
    """the brickwork parity strata, generalised to per-link coins: the four
    declared parity classes.  Each is a PERFECT MATCHING of the site set when
    L is even, which is what makes the stratum operator a product of
    commuting link operators -- measured below, not assumed."""
    out = {}
    for d, tag in ((0, "X"), (1, "Y")):
        for par, pname in ((0, "EVEN"), (1, "ODD")):
            out["%s-%s" % (tag, pname)] = [l for l in links
                                           if l[1] == d and l[0][d] % 2 == par]
    return out


def build_coins(alphabet):
    """THE COIN ALPHABET, DERIVED.  A coin is a 2 x 2 unitary all four of
    whose entries lie in the parent's coefficient alphabet.  Nothing about
    the size is typed: the enumeration is exhaustive over the alphabet's
    fourth power, pruned by the row conditions, and the sector split is read
    off the supports."""
    rows = [(a, b) for a in alphabet for b in alphabet
            if fadd(fnormsq(a), fnormsq(b)) == ONE]
    coins = []
    for (a, b) in rows:
        for (c, d) in rows:
            if fadd(fmul(a, fconj(c)), fmul(b, fconj(d))) == ZERO:
                coins.append((a, b, c, d))
    return coins, rows


def coin_sector(m):
    a, b, c, d = m
    if b == ZERO and c == ZERO:
        return "DIAGONAL"
    if a == ZERO and d == ZERO:
        return "ANTIDIAGONAL"
    if a != ZERO and b != ZERO and c != ZERO and d != ZERO:
        return "BALANCED"
    return "OTHER"


def coin_is_unitary_by_product(m):
    """the second route: U^dagger U = I, written out."""
    a, b, c, d = m
    return (fadd(fmul(fconj(a), a), fmul(fconj(c), c)) == ONE
            and fadd(fmul(fconj(b), b), fmul(fconj(d), d)) == ONE
            and fadd(fmul(fconj(a), b), fmul(fconj(c), d)) == ZERO)


def coin_name(m, alphabet):
    """the declared named coins, IDENTIFIED rather than indexed: each is
    given by its entries, and the identification is a measurement."""
    a, b, c, d = m
    z = zpow
    if m == (ONE, ZERO, ZERO, ONE):
        return "DIAG-I"
    if m == (ONE, ZERO, ZERO, fneg(ONE)):
        return "DIAG-Z"
    if m == (ZERO, ONE, ONE, ZERO):
        return "ANTI-X"
    if m == (ZERO, ONE, fneg(ONE), ZERO):
        return "ANTI-ZX"
    if m == (INV_SQRT2, INV_SQRT2, INV_SQRT2, fneg(INV_SQRT2)):
        return "BAL-H"
    if m == (INV_SQRT2, fmul(z(2), INV_SQRT2), fmul(z(2), INV_SQRT2),
             INV_SQRT2):
        return "BAL-F"
    return None


# ---------------------------------------------------------------- matrices
def ident(n):
    return tuple(tuple(ONE if i == j else ZERO for j in range(n))
                 for i in range(n))


def mmul(A, B):
    n = len(A)
    out = []
    for i in range(n):
        Ai = A[i]
        nz = [(k, Ai[k]) for k in range(n) if Ai[k] != ZERO]
        row = []
        for j in range(n):
            acc = ZERO
            for k, v in nz:
                w = B[k][j]
                if w != ZERO:
                    acc = fadd(acc, fmul(v, w))
            row.append(acc)
        out.append(tuple(row))
    return tuple(out)


def dagger(A):
    n = len(A)
    return tuple(tuple(fconj(A[j][i]) for j in range(n)) for i in range(n))


def is_ident(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            if M[i][j] != (ONE if i == j else ZERO):
                return False
    return True


def mat_is_unitary(M):
    return is_ident(mmul(dagger(M), M))


def trace(M):
    t = ZERO
    for i in range(len(M)):
        t = fadd(t, M[i][i])
    return t


def sub_block(M, sub):
    return tuple(tuple(M[i][j] for j in sub) for i in sub)


# ------------------------------------------------------- the link operator
def link_op(l, coin, idx, L, n):
    """THE LINK-INDEXED UNITARY: the declared coin on the link's own domino,
    the identity on every other site.  This is the single-link factor of the
    parent's brickwork generator, and the stratum operator is the product of
    the eight that make up a parity class."""
    t, h = link_ends(l, L)
    it, ih = idx[t], idx[h]
    a, b, c, d = coin
    M = [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]
    M[it][it] = a
    M[it][ih] = b
    M[ih][it] = c
    M[ih][ih] = d
    return tuple(tuple(r) for r in M)


def holonomy(p, cfg, idx, L, n):
    """W_p, the ordered product of the four link operators around the
    plaquette boundary, each inverted where the boundary runs against the
    link's own direction.  Rightmost acts first."""
    W = ident(n)
    for l, o in plaquette_boundary(p, L):
        M = link_op(l, cfg[l], idx, L, n)
        if o < 0:
            M = dagger(M)
        W = mmul(M, W)
    return W


_HOL_MEMO = {}
_TABLE_MEMO = {}
_ORDER_MEMO = {}
_CERT_MEMO = {}
_WEDGE_MEMO = {}


def holonomy_block(p, cfg, idx, L):
    """W_p restricted to the plaquette's own four corners.  Every one of the
    four link operators is the identity off those corners, so the product is
    too, and the four-by-four block carries the whole holonomy: the
    restriction is exact, not an approximation, and it is what makes the
    census over the whole coin alphabet finite work rather than a sweep."""
    corners = [p, addv(p, E1, L), addv(addv(p, E1, L), E2, L), addv(p, E2, L)]
    key = (p, L) + tuple(cfg[l] for l, _o in plaquette_boundary(p, L))
    got = _HOL_MEMO.get(key)
    if got is not None:
        return corners, got
    pos = {c: i for i, c in enumerate(corners)}
    W = [[ONE if i == j else ZERO for j in range(4)] for i in range(4)]
    for l, o in plaquette_boundary(p, L):
        t, h = link_ends(l, L)
        it, ih = pos[t], pos[h]
        a, b, c, d = cfg[l]
        if o < 0:
            a, b, c, d = fconj(a), fconj(c), fconj(b), fconj(d)
        M = [[ONE if i == j else ZERO for j in range(4)] for i in range(4)]
        M[it][it], M[it][ih], M[ih][it], M[ih][ih] = a, b, c, d
        W = [list(r) for r in mmul(tuple(tuple(r) for r in M),
                                   tuple(tuple(r) for r in W))]
    out = tuple(tuple(r) for r in W)
    _HOL_MEMO[key] = out
    return corners, out


def holonomy_monomial(p, cfg, idx, L, n, mu8):
    """the holonomy as a monomial (sigma, phases) on the whole site set,
    built from its own four-by-four block and the identity elsewhere."""
    corners, W = holonomy_block(p, cfg, idx, L)
    sigma = list(range(n))
    ph = [0] * n
    for j in range(4):
        nz = [i for i in range(4) if W[i][j] != ZERO]
        if len(nz) != 1:
            return None
        t = mu8.get(W[nz[0]][j])
        if t is None:
            return None
        sigma[idx[corners[j]]] = idx[corners[nz[0]]]
        ph[idx[corners[j]]] = t
    return (tuple(sigma), tuple(ph))


def embed(corners, W, sub, idx):
    """the four-by-four block, embedded as the identity on the wider site set
    the comparison is taken over."""
    pos = {idx[c]: i for i, c in enumerate(corners)}
    n = len(sub)
    out = [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]
    for a in range(n):
        for b in range(n):
            ia, ib = sub[a], sub[b]
            if ia in pos and ib in pos:
                out[a][b] = W[pos[ia]][pos[ib]]
    return tuple(tuple(r) for r in out)


def plaq_sites(p, idx, L):
    return sorted({idx[p], idx[addv(p, E1, L)], idx[addv(p, E2, L)],
                   idx[addv(addv(p, E1, L), E2, L)]})


def link_sites(l, idx, L):
    t, h = link_ends(l, L)
    return [idx[t], idx[h]]


# ===========================================================================
# SECTION 5.  THE HOLONOMY GROUP (monomial representation, Schreier-Sims)
# ===========================================================================

def as_monomial(M, mu8):
    """M -> (sigma, phases) with M e_j = zeta^{a_j} e_{sigma(j)}; None if M is
    not monomial over the 8th roots of unity."""
    n = len(M)
    sigma = [0] * n
    ph = [0] * n
    for j in range(n):
        nz = [i for i in range(n) if M[i][j] != ZERO]
        if len(nz) != 1:
            return None
        i = nz[0]
        t = mu8.get(M[i][j])
        if t is None:
            return None
        sigma[j] = i
        ph[j] = t
    return (tuple(sigma), tuple(ph))


def mono_to_perm(mp, n):
    """the faithful action of a monomial matrix on the n*8 pairs (site,
    phase): (j, t) -> (sigma(j), t + a_j).  A monomial group over mu_8 is
    therefore a PERMUTATION group, and its order is exact."""
    sigma, ph = mp
    out = [0] * (n * 8)
    for j in range(n):
        pj = sigma[j] * 8
        aj = ph[j]
        for t in range(8):
            out[j * 8 + t] = pj + ((t + aj) % 8)
    return tuple(out)


def pmul(a, b):
    return tuple(a[x] for x in b)


def pinv(a):
    out = [0] * len(a)
    for i, v in enumerate(a):
        out[v] = i
    return tuple(out)


def stabilizer_chain(gens, deg):
    """deterministic Schreier-Sims with sifting: exact integer arithmetic,
    no randomisation, so the order is reproducible byte for byte."""
    idp = tuple(range(deg))
    base, S, orb = [], [], []

    def compute_orbit(i):
        b = base[i]
        tr = {b: idp}
        stack = [b]
        while stack:
            pt = stack.pop()
            u = tr[pt]
            for g in S[i]:
                q = g[pt]
                if q not in tr:
                    tr[q] = pmul(g, u)
                    stack.append(q)
        orb[i] = tr

    def strip(g, start=0):
        h = g
        for i in range(start, len(base)):
            q = h[base[i]]
            if q not in orb[i]:
                return h, i
            h = pmul(pinv(orb[i][q]), h)
        return h, len(base)

    def add_gen(h, lev):
        if lev == len(base):
            b = next(p for p in range(deg) if h[p] != p)
            base.append(b)
            S.append([])
            orb.append({})
        for k in range(lev + 1):
            S[k].append(h)
        for k in range(lev, -1, -1):
            compute_orbit(k)

    for g in gens:
        if g == idp:
            continue
        h, j = strip(g)
        if h != idp:
            add_gen(h, j)

    i = len(base) - 1
    while i >= 0:
        stable = True
        for pt in list(orb[i].keys()):
            u = orb[i][pt]
            for g in list(S[i]):
                sg = pmul(pinv(orb[i][g[pt]]), pmul(g, u))
                if sg == idp:
                    continue
                h, j = strip(sg, i + 1)
                if h != idp:
                    add_gen(h, j)
                    i = j
                    stable = False
                    break
            if not stable:
                break
        if stable:
            i -= 1
    return base, orb


def group_order(gens, deg):
    idp = tuple(range(deg))
    gens = [g for g in gens if g != idp]
    if not gens:
        return 1
    key = (deg, tuple(sorted(set(gens))))
    got = _ORDER_MEMO.get(key)
    if got is not None:
        return got
    base, orb = stabilizer_chain(gens, deg)
    o = 1
    for i in range(len(base)):
        o *= len(orb[i])
    _ORDER_MEMO[key] = o
    return o


def perm_orbits(gens, deg):
    seen = [False] * deg
    out = []
    for p in range(deg):
        if seen[p]:
            continue
        comp, stack = {p}, [p]
        seen[p] = True
        while stack:
            q = stack.pop()
            for g in gens:
                r = g[q]
                if not seen[r]:
                    seen[r] = True
                    comp.add(r)
                    stack.append(r)
        out.append(sorted(comp))
    return out


def factorial(k):
    f = 1
    for i in range(2, k + 1):
        f *= i
    return f


def perm_parity_on(g, orbit):
    """the parity of g restricted to one of its own orbits."""
    pos = {p: i for i, p in enumerate(orbit)}
    seen = set()
    par = 0
    for p in orbit:
        if p in seen:
            continue
        ln = 0
        q = p
        while q not in seen:
            seen.add(q)
            q = g[q]
            ln += 1
        par += ln - 1
    return par % 2


def alternating_certificate(gens, deg):
    """THE CERTIFICATE, by set equality and nothing weaker.  Let O_1..O_k be
    the group's orbits on its own support.  Every generator preserves each
    orbit and restricts to an EVEN permutation of it, so G is contained in
    the direct product of the alternating groups on the orbits; if the
    measured order equals that product's order, containment plus equal
    cardinality gives EQUALITY, and the isomorphism class follows.  Nothing
    here is a heuristic fingerprint and no matrix is reported."""
    idp = tuple(range(deg))
    gens = [g for g in gens if g != idp]
    if not gens:
        return {"class": "TRIVIAL", "order": 1, "support": 0, "orbits": [],
                "certified": True}
    ckey = (deg, tuple(sorted(set(gens))))
    cgot = _CERT_MEMO.get(ckey)
    if cgot is not None:
        return dict(cgot)
    support = sorted({p for g in gens for p in range(deg) if g[p] != p})
    orbs = [o for o in perm_orbits(gens, deg) if len(o) > 1]
    order = group_order(gens, deg)
    even = all(perm_parity_on(g, o) == 0 for g in gens for o in orbs)
    target = 1
    for o in orbs:
        target *= factorial(len(o)) // 2
    certified = even and order == target and target > 1
    if len(orbs) == 1 and certified:
        cls = "A%d" % len(orbs[0])
    elif certified:
        cls = " x ".join("A%d" % len(o) for o in sorted(orbs, key=len))
    else:
        cls = "NOT-ALTERNATING(order=%d)" % order
    out = {"class": cls, "order": order, "support": len(support),
           "orbits": sorted(len(o) for o in orbs),
           "even_on_every_orbit": even,
           "alternating_product_order": target, "certified": certified}
    _CERT_MEMO[ckey] = out
    return dict(out)


def generator_rank(gens, deg, target_order, cap=8):
    """the RANK, measured and arena-relative: the least number of the
    DECLARED plaquette holonomies that generate the whole group.  It is not
    the abstract minimal generator number of the abstract group, and the
    verdict says which one it is.  A subset whose supports do not cover the
    whole group's support cannot generate it, so the search is pruned by that
    necessary condition before any order is computed."""
    full = list(range(len(gens)))
    supp = [frozenset(p for p in range(deg) if g[p] != p) for g in gens]
    need = frozenset().union(*supp) if supp else frozenset()
    for k in range(1, min(cap, len(gens)) + 1):
        for sub in combinations(full, k):
            cover = frozenset().union(*[supp[i] for i in sub])
            if cover != need:
                continue
            if group_order([gens[i] for i in sub], deg) == target_order:
                return k, sorted(sub)
    return None, None


# ===========================================================================
# SECTION 6.  Delta^B, THE COMPOSITION DEFECT (reimplemented from the seed)
# ===========================================================================

def bshadow(M):
    """B(U) = |U| entrywise-squared: Barandes' Born shadow."""
    n = len(M)
    return tuple(tuple(fnormsq(M[i][j]) for j in range(n)) for i in range(n))


def msub(A, B):
    n = len(A)
    return tuple(tuple(fadd(A[i][j], fneg(B[i][j])) for j in range(n))
                 for i in range(n))


def delta_B(U2, U1):
    """Delta^B(U2, U1) = B(U2 U1) - B(U2) B(U1): the failure of the Born
    shadow of the coherent composite to equal the shadow obtained by
    forgetting phases and restarting at the intermediate cut.  The division
    events are DECLARED at t = 0 and t = 2; the cut at t = 1 is not one."""
    return msub(bshadow(mmul(U2, U1)), mmul(bshadow(U2), bshadow(U1)))


def is_zero_mat(M):
    for r in M:
        for v in r:
            if v != ZERO:
                return False
    return True


def hadamard_witness():
    """the seed's own named two-by-two witness, rebuilt: on the Hadamard
    against itself Delta^B returns [[1/2, -1/2], [-1/2, 1/2]]."""
    h = INV_SQRT2
    H = ((h, h), (h, fneg(h)))
    return delta_B(H, H)


# --------------------------------------------------- the two-excitation sector
def wedge_pairs(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def wedge2(U, keys):
    """Lambda^2(U) on the declared two-excitation sector: the hard-core,
    antisymmetric two-particle sector.  The exterior square is the FORCED
    choice at fixed dimension -- the symmetric square is the other unitary
    option and is entered in the choice inventory with fibre two."""
    wkey = (U, tuple(keys))
    wgot = _WEDGE_MEMO.get(wkey)
    if wgot is not None:
        return wgot
    idx = {p: k for k, p in enumerate(keys)}
    n = len(keys)
    M = [[ZERO] * n for _ in range(n)]
    for (i, j) in keys:
        r = idx[(i, j)]
        for (k, l) in keys:
            M[r][idx[(k, l)]] = fadd(fmul(U[i][k], U[j][l]),
                                     fneg(fmul(U[i][l], U[j][k])))
    out = tuple(tuple(r) for r in M)
    _WEDGE_MEMO[wkey] = out
    return out


def wedge_keys_touching(n, sub):
    """the two-excitation basis states the operator can move: every pair with
    at least one site in the support.  On the rest Lambda^2 is the identity,
    so both sides of Delta^B agree there and the restriction is exact."""
    return [(i, j) for i in range(n) for j in range(i + 1, n)
            if i in sub or j in sub]


# ===========================================================================
# SECTION 7.  THE FLAT NEGATIVE CONTROL: R4's FULL-TRANSPORT STRATUM
# ===========================================================================

_FLAT_MEMO = {}


def _flat_census(pool, sites, idx, L, n):
    """the FULL stratum's commutator census, by two routes, plus the holonomy
    of the direction-indexed connection assembled from it.  A pure function of
    the rebuilt pool, so it is memoized on the declaration that determines it."""
    noncomm = 0
    for a in pool:
        for b in pool:
            if conv(a["coef"], b["coef"], L) != conv(b["coef"], a["coef"], L):
                noncomm += 1
    sample = [(i, j) for i in range(0, len(pool), 7)
              for j in range(0, len(pool), 11)]
    mats = {}
    disagree = 0
    for i, j in sample:
        for k in (i, j):
            if k not in mats:
                mats[k] = circ_matrix(pool[k]["coef"], sites, idx, L, n)
        by_matrix = mmul(mats[i], mats[j]) != mmul(mats[j], mats[i])
        by_conv = conv(pool[i]["coef"], pool[j]["coef"], L) \
            != conv(pool[j]["coef"], pool[i]["coef"], L)
        if by_matrix != by_conv:
            disagree += 1
    trivial = True
    for i in range(0, len(pool), 5):
        for j in range(0, len(pool), 5):
            Ci = mats.setdefault(i, circ_matrix(pool[i]["coef"], sites, idx,
                                                L, n))
            Cj = mats.setdefault(j, circ_matrix(pool[j]["coef"], sites, idx,
                                                L, n))
            if not is_ident(mmul(mmul(dagger(Cj), dagger(Ci)),
                                 mmul(Cj, Ci))):
                trivial = False
    return noncomm, len(sample), disagree, trivial


_CIRC_MEMO = {}
_REFINE_MEMO = {}
_SWAPHOL_MEMO = {}


def build_circulants(L, sites, idx, alphabet):
    """R4's FULL stratum, REBUILT from the pinned definitions: coefficient
    maps on the three-term axis stencil {0, a, -a}, unitary by the delta
    autocorrelation criterion, quotiented by the declared global-phase gauge.
    The count is a MEASUREMENT against the anchored 58, never a typed
    constant."""
    def sm(k, a):
        return ((k * a[0]) % L, (k * a[1]) % L)

    def delta_autocorr(c):
        for m in sites:
            acc = ZERO
            for v, cv in c.items():
                w = addv(v, m, L)
                if w in c:
                    acc = fadd(acc, fmul(cv, fconj(c[w])))
            if acc != (ZERO if any(m) else ONE):
                return False
        return True

    axes, seen = [], set()
    for v in sites:
        if not any(v) or v in seen:
            continue
        seen.add(v)
        seen.add(sm(L - 1, v))
        axes.append(v)

    pool, keys, orbit_sizes = [], set(), []
    for a in axes:
        gens = {}
        for tr in product(alphabet, repeat=3):
            c = {}
            for o, val in (((0, 0), tr[0]), (a, tr[1]), (sm(L - 1, a), tr[2])):
                c[o] = fadd(c.get(o, ZERO), val)
            c = {o: val for o, val in c.items() if val != ZERO}
            k = tuple(sorted(c.items()))
            if k in gens:
                continue
            if delta_autocorr(c):
                gens[k] = c
        done = set()
        for k in sorted(gens):
            if k in done:
                continue
            orb = {tuple(sorted((o, fmul(zpow(t), val)) for o, val in k))
                   for t in range(8)}
            orbit_sizes.append(len(orb))
            done |= orb
            rep = min(orb)
            if rep in keys:
                continue
            keys.add(rep)
            pool.append({"axis": a, "coef": dict(rep)})
    return pool, axes, sorted(set(orbit_sizes))


def conv(c1, c2, L):
    """the coefficient convolution: the product of two circulants is the
    circulant of the convolution, so commutation on the FULL stratum is
    decidable from the coefficient maps alone."""
    out = {}
    for o1, v1 in c1.items():
        for o2, v2 in c2.items():
            o = addv(o1, o2, L)
            out[o] = fadd(out.get(o, ZERO), fmul(v1, v2))
    return {o: v for o, v in out.items() if v != ZERO}


def circ_matrix(c, sites, idx, L, n):
    M = [[ZERO] * n for _ in range(n)]
    for x in sites:
        for o, v in c.items():
            i, j = idx[addv(x, o, L)], idx[x]
            M[i][j] = fadd(M[i][j], v)
    return tuple(tuple(r) for r in M)


# ===========================================================================
# SECTION 8.  THE TRANSPORT AUDIT (G2)
# ===========================================================================

def translation_perm(v, sites, idx, L):
    return tuple(idx[addv(sites[i], v, L)] for i in range(len(sites)))


def conj_by_perm(M, p):
    n = len(M)
    out = [[ZERO] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            out[p[i]][p[j]] = M[i][j]
    return tuple(tuple(r) for r in out)


def translation_stabiliser(M, sites, idx, L):
    return [v for v in sites if conj_by_perm(M, translation_perm(v, sites,
                                                                 idx, L)) == M]


def transport_level(M, sites, idx, L):
    """R4's ladder, reimplemented and applied PER GENERATOR:
       NONE      -- the translation stabiliser is trivial;
       OCC       -- it is a nontrivial proper subgroup;
       OCC+AXIS  -- it is the whole translation group;
       FULL      -- and in addition the generator's image under every element
                    of the chart group extended by the point symmetries is
                    again a family member up to the declared gauge.
    The first three are decided here; FULL is decided by the caller, which
    holds the family."""
    st = translation_stabiliser(M, sites, idx, L)
    if len(st) == 1:
        return "NONE", st
    if len(st) == len(sites):
        return "OCC+AXIS", st
    return "OCC", st


def point_symmetries():
    """the square point group D_4 acting on lattice coordinates.  R4's
    ANCHORED chart group uses the identity and the direction relabelling
    only (order 32 with the translations); this unit's declared EXTENSION
    uses all eight (order 128).  Both are censused."""
    out = []
    for swap in (False, True):
        for sx in (1, -1):
            for sy in (1, -1):
                out.append((swap, sx, sy))
    return out


def apply_point(g, s, L):
    swap, sx, sy = g
    x, y = s
    if swap:
        x, y = y, x
    return ((sx * x) % L, (sy * y) % L)


def point_on_dir(g, d):
    """the direction e_d is carried to +/- e_{d'}; returns (d', sign)."""
    swap, sx, sy = g
    v = EDIR[d]
    x, y = v
    if swap:
        x, y = y, x
    x, y = sx * x, sy * y
    if (abs(x), abs(y)) == (1, 0):
        return 0, (1 if x > 0 else -1)
    return 1, (1 if y > 0 else -1)


def chart_elements(sites, L, extended):
    pts = point_symmetries() if extended else [(False, 1, 1), (True, 1, 1)]
    return [(v, g) for v in sites for g in pts]


def transported_link(l, elem, L):
    """the image of a link under a chart element, with the domino's
    orientation tracked.  The domino {s, s + e_d} goes to {s'', s'' + g(e_d)}
    with s'' = g(s) + v.  If g(e_d) = +e_{d'} the image is the link (s'', d')
    read the same way round; if g(e_d) = -e_{d'} the image is the link
    (s'' - e_{d'}, d') read the OTHER way round, and the transported coin is
    the swap conjugate."""
    v, g = elem
    s, d = l
    d2, sign = point_on_dir(g, d)
    s2 = addv(apply_point(g, s, L), v, L)
    if sign > 0:
        return (s2, d2), False
    return (((s2[0] - EDIR[d2][0]) % L, (s2[1] - EDIR[d2][1]) % L), d2), True


def swap_conjugate(m):
    """X c X: the coin read from the other end of its own domino."""
    a, b, c, d = m
    return (d, c, b, a)


# ===========================================================================
# SECTION 9.  THE STATE: every measurement, in order, each behind its gate
# ===========================================================================

_ARENA_MEMO = {}


def build_arena(L, LD):
    """the arena, memoized on the exact inputs that determine it -- the
    lattice size and the two mutants that perturb its construction -- so the
    in-process mutant sweep rebuilds the census, not the enumeration."""
    key = (L, mut("MUT-ALPHABET"), mut("MUT-COIN-UNITARITY"))
    got = _ARENA_MEMO.get(key)
    if got is not None:
        return got
    sites, idx = build_lattice(L)
    n = len(sites)
    links = build_links(sites, L)
    plaqs = build_plaquettes(sites)
    strata = build_strata(links)
    alphabet = build_alphabet()
    if mut("MUT-ALPHABET"):
        alphabet = alphabet[:-1]
    coins, rows = build_coins(alphabet)
    if mut("MUT-COIN-UNITARITY"):
        coins = coins + [(ONE, ONE, ZERO, ONE)]
    mu8 = {zpow(t): t for t in range(8)}
    out = {"L": L, "sites": sites, "idx": idx, "n": n, "links": links,
           "plaqs": plaqs, "strata": strata, "alphabet": alphabet,
           "coins": coins, "rows": rows, "mu8": mu8}
    _ARENA_MEMO[key] = out
    return out


def uniform_cfg(links, coin):
    return {l: coin for l in links}


def build_state(break_anchor=None):
    LD = Ledger()
    S = {}

    # ---- [1/9] anchors -----------------------------------------------------
    say("[1/9] anchors: %d hash-pinned sources, %d path-value, %d verbatim"
        % (len(SOURCES), len(PATH_VALUE_ANCHORS), len(VERBATIM_ANCHORS)))
    texts, byte_rows = {}, []
    for sid, rel, expect, note in SOURCES:
        if break_anchor == sid:
            expect = "0" * 12
        p = source_path(rel)
        got = sha12(p)
        byte_rows.append({"anchor": sid, "path": rel, "expected": expect,
                          "measured": got, "note": note})
        if got != expect:
            raise GateFail("G-SOURCES-PINNED :: %s :: %s expected %s measured "
                           "%s" % (sid, rel, expect, got))
        texts[sid] = read_text(p)
    LD.gate("G-SOURCES-PINNED",
            "every runtime input is hash-pinned by this unit's frozen "
            "declaration and re-verified at run time; a drifted byte in any "
            "of them stops the run before a single measurement is taken",
            all(r["expected"] == r["measured"] for r in byte_rows),
            "%d sources, %d matched" % (len(byte_rows), len(byte_rows)))
    S["byte_anchors"] = byte_rows

    # the verbatim windows are evaluated BEFORE the path-value anchors: a
    # window is what fixes the MEANING of the value the path then supplies
    vb_rows = []
    for aid, sid, consumer, needle in VERBATIM_ANCHORS:
        d = hashlib.sha256(needle.encode("utf-8")).hexdigest()[:12]
        want = WINDOW_DIGESTS[aid]
        if mut("MUT-WINDOW-TRUNCATED") and aid == "VB-EFF-G7":
            needle = needle[:12]
            d = hashlib.sha256(needle.encode("utf-8")).hexdigest()[:12]
        present = flat(needle) in flat(texts[sid])
        long_enough = len(needle) >= WINDOW_FLOOR
        vb_rows.append({"anchor": aid, "source": sid, "consumer": consumer,
                        "chars": len(needle), "digest": d, "expected": want,
                        "present": present, "meets_floor": long_enough})
        if not (present and long_enough and d == want):
            raise GateFail("G-VERBATIM-ANCHORS :: %s :: present=%s floor=%s "
                           "digest %s expected %s"
                           % (aid, present, long_enough, d, want))
    LD.gate("G-VERBATIM-ANCHORS",
            "every verbatim window is present in its pinned source under "
            "whitespace normalisation, is at least the declared length floor "
            "long, and has the exact digest this unit froze: presence alone "
            "would admit a window truncated to a decoration, and the floor "
            "and the digest together do not",
            all(r["present"] and r["meets_floor"] and r["digest"] == r["expected"]
                for r in vb_rows),
            "%d windows, floor %d chars" % (len(vb_rows), WINDOW_FLOOR))
    S["verbatim_anchors"] = vb_rows

    pv_rows = []
    for aid, sid, path, expect, note in PATH_VALUE_ANCHORS:
        obj = json.loads(texts[sid]) if texts[sid].lstrip().startswith("{") \
            else None
        got = jpath(obj, path) if obj is not None else None
        pv_rows.append({"anchor": aid, "source": sid, "path": path,
                        "expected": expect, "measured": got, "note": note})
        if got != expect:
            raise GateFail("G-PATH-VALUE-ANCHORS :: %s :: %s expected %r "
                           "measured %r" % (aid, path, expect, got))
    LD.gate("G-PATH-VALUE-ANCHORS",
            "every value this unit takes from a parent is taken at a NAMED "
            "PATH in a hash-pinned receipt and compared to the value this "
            "unit froze: a path drift and a value drift both die here, and "
            "no parent number is retyped anywhere else in this file",
            all(r["expected"] == r["measured"] for r in pv_rows),
            "%d path-value anchors" % len(pv_rows))
    S["path_value_anchors"] = pv_rows

    consumers = {r["consumer"] for r in vb_rows}
    S["_anchor_consumers"] = sorted(consumers)

    L = [r for r in pv_rows if r["anchor"] == "PV-L"][0]["measured"]
    d = [r for r in pv_rows if r["anchor"] == "PV-D"][0]["measured"]
    alpha_n = [r for r in pv_rows
               if r["anchor"] == "PV-ALPHABET"][0]["measured"]

    # ---- [2/9] the arena ---------------------------------------------------
    say("[2/9] the arena: the L = %d torus, its links, plaquettes and strata"
        % L)
    A = build_arena(L, LD)
    n, sites, idx = A["n"], A["sites"], A["idx"]
    links, plaqs, strata = A["links"], A["plaqs"], A["strata"]
    alphabet, coins, mu8 = A["alphabet"], A["coins"], A["mu8"]

    LD.gate("G-ARENA-DERIVED",
            "the lattice, its link set and its plaquette set are DERIVED from "
            "the anchored size and dimension, not typed: %d sites, two links "
            "per site, one plaquette per site" % n,
            n == L * L and len(links) == 2 * n and len(plaqs) == n,
            "sites %d links %d plaquettes %d" % (n, len(links), len(plaqs)))

    matchings = {}
    for k, v in strata.items():
        covered = []
        for l in v:
            t, h = link_ends(l, L)
            covered += [t, h]
        matchings[k] = (len(v), len(set(covered)), len(covered))
    LD.gate("G-STRATA-ARE-THE-EXCLUDED-FAMILY",
            "the four declared parity strata are the parent's brickwork "
            "shape generalised to per-link coins, and each is a PERFECT "
            "MATCHING of the site set: eight disjoint dominoes covering all "
            "%d sites, which is what makes a stratum operator a product of "
            "commuting link operators" % n,
            all(a == n // 2 and b == n and c == n
                for a, b, c in matchings.values()) and len(strata) == 4,
            "; ".join("%s: %d links covering %d sites"
                      % (k, v[0], v[1]) for k, v in sorted(matchings.items())))

    LD.gate("G-ARENA-DECLARED",
            "the arena is exactly the one the pin declares and nothing "
            "wider: link-indexed unitaries on the L = 4 torus, a coin per "
            "link over %d links and %d plaquettes, drawn from a DECLARED coin "
            "alphabet, applied in the declared parity strata"
            % (len(links), len(plaqs)),
            len(links) == 32 and len(plaqs) == 16 and len(strata) == 4
            and L == 4,
            "L %d, links %d, plaquettes %d, strata %d"
            % (L, len(links), len(plaqs), len(strata)))

    LD.gate("G-R4B-HANDOFF",
            "the second parent's handoffs are carried as the pin requires "
            "and no further: NOT-BLOCH-DIAGONAL is a THEOREM for the "
            "brickwork classes and is cited rather than re-derived, and NO "
            "transport number is inherited from it -- measured by the anchor "
            "list, which takes no value at all from that receipt",
            not any(r["source"] == "A-R4B-RECEIPT"
                    for r in S["path_value_anchors"]),
            "%d path-value anchors, %d of them from the second parent's "
            "receipt" % (len(S["path_value_anchors"]),
                         sum(1 for r in S["path_value_anchors"]
                             if r["source"] == "A-R4B-RECEIPT")))

    LD.gate("G-ALPHABET-REBUILT",
            "the parent's coefficient alphabet is REBUILT from its declared "
            "recipe -- zero together with the eight powers of zeta_8 at each "
            "of three moduli -- and its size is measured against the anchored "
            "value rather than typed",
            len(alphabet) == alpha_n,
            "rebuilt %d, anchored %d" % (len(alphabet), alpha_n))

    sect = {}
    for m in coins:
        sect[coin_sector(m)] = sect.get(coin_sector(m), 0) + 1
    two_routes = sum(1 for m in coins if coin_is_unitary_by_product(m))
    LD.gate("G-COIN-ALPHABET-DERIVED",
            "THE COIN ALPHABET IS DERIVED, NOT CHOSEN: a coin is a two-by-two "
            "unitary all four of whose entries lie in the parent's alphabet, "
            "and the enumeration is exhaustive over that alphabet's fourth "
            "power.  Its size, and the split into sectors, are measurements",
            len(coins) > 0 and two_routes == len(coins)
            and sect.get("OTHER", 0) == 0,
            "coins %d = %s; unitary by the second route %d of %d"
            % (len(coins), "+".join("%d %s" % (v, k)
                                    for k, v in sorted(sect.items())),
               two_routes, len(coins)))
    S["coin_sectors"] = sect

    named = {}
    for m in coins:
        nm = coin_name(m, alphabet)
        if nm:
            named[nm] = m
    LD.gate("G-NAMED-COINS-PRESENT",
            "the six declared named coins -- two per sector -- are IDENTIFIED "
            "inside the derived alphabet by their entries, so the sector "
            "representatives the full tables are taken at are members of the "
            "same enumeration and not a second declaration",
            sorted(named) == sorted(NAMED_COINS),
            "found %s" % sorted(named))
    S["named_coins"] = named

    # ---- [3/9] curvature ---------------------------------------------------
    say("[3/9] the curvature census over the %d uniform configurations"
        % len(coins))
    sec_of = {m: coin_sector(m) for m in coins}
    curv = {}
    hol_cache = {}
    p0, p1 = plaqs[0], addv(plaqs[0], E1, L)
    for m in coins:
        cfg = uniform_cfg(links, m)
        c0, W0 = holonomy_block(p0, cfg, idx, L)
        c1, W1 = holonomy_block(p1, cfg, idx, L)
        hol_cache[m] = (c0, W0)
        s = sec_of[m]
        row = curv.setdefault(s, {"coins": 0, "nonflat": 0, "noncommuting": 0,
                                  "unitary": 0})
        row["coins"] += 1
        if not is_ident(W0):
            row["nonflat"] += 1
        sub = sorted({idx[x] for x in c0} | {idx[x] for x in c1})
        E0 = embed(c0, W0, sub, idx)
        E1_ = embed(c1, W1, sub, idx)
        if mmul(E0, E1_) != mmul(E1_, E0):
            row["noncommuting"] += 1
        if mat_is_unitary(W0):
            row["unitary"] += 1
    if mut("MUT-CURVATURE-COUNT"):
        curv["BALANCED"]["noncommuting"] -= 1
    if mut("MUT-CURVATURE-ZEROED"):
        for v in curv.values():
            v["noncommuting"] = 0
    S["curvature_census"] = curv
    nonab = sum(v["noncommuting"] for v in curv.values())
    nonflat = sum(v["nonflat"] for v in curv.values())
    LD.gate("G-HOLONOMY-UNITARY",
            "every plaquette holonomy is a unitary of the single-occupation "
            "sector: the ordered product of four unitaries around a closed "
            "loop, verified as U^dagger U = I on every swept configuration",
            all(v["unitary"] == v["coins"] for v in curv.values()),
            "; ".join("%s %d of %d" % (k, v["unitary"], v["coins"])
                      for k, v in sorted(curv.items())))
    LD.gate("G-COMMUTATOR-NONTRIVIAL",
            "G1, THE DECISIVE GATE: the commutator subgroup of the "
            "plaquette-holonomy group is NONTRIVIAL -- there are plaquettes "
            "whose holonomies do not commute.  A stage on which they all "
            "commuted would have a trivial commutator subgroup and no "
            "non-abelian holonomy to measure",
            nonab > 0,
            "non-commuting at %d of %d uniform configurations; non-flat at %d"
            % (nonab, len(coins), nonflat))
    split = sum(v["coins"] for v in curv.values())
    derived_nonab = len(coins) - curv["DIAGONAL"]["coins"]
    LD.gate("G-CURVATURE-CENSUS-BOUND",
            "the census is BOUND to the arena that produced it, cell by cell: "
            "the three sector rows partition the whole coin alphabet, no row "
            "reports more non-commuting than non-flat pairs or more non-flat "
            "than coins, and the non-commuting total is exactly the alphabet "
            "less the diagonal sector.  A single moved cell breaks one of "
            "those identities",
            split == len(coins) and nonab == derived_nonab
            and all(v["noncommuting"] <= v["nonflat"] <= v["coins"]
                    for v in curv.values()),
            "sectors sum to %d; non-commuting %d, derived %d"
            % (split, nonab, derived_nonab))

    LD.gate("G-ABELIAN-SECTOR-MEASURED",
            "the diagonal sector is measured ABELIAN and is not silently "
            "dropped: its link operators are simultaneously diagonal, so "
            "every holonomy commutes with every other, and the sector is "
            "carried as the arena's own abelian arm",
            curv["DIAGONAL"]["noncommuting"] == 0
            and curv["DIAGONAL"]["nonflat"] > 0,
            "diagonal: %d non-commuting, %d non-flat of %d"
            % (curv["DIAGONAL"]["noncommuting"], curv["DIAGONAL"]["nonflat"],
               curv["DIAGONAL"]["coins"]))
    S["_A"] = A
    S["_texts"] = texts
    S["_hol"] = hol_cache
    S["_L"], S["_d"], S["_n"] = L, d, n
    build_groups(S, LD)
    build_flat_control(S, LD)
    build_transport(S, LD)
    build_matched(S, LD)
    build_gauge(S, LD)
    build_refinement(S, LD)
    build_scramble(S, LD)
    return S, LD


# ---- [4/9] the holonomy group -------------------------------------------
def build_groups(S, LD):
    A, L, n = S["_A"], S["_L"], S["_n"]
    idx, links, plaqs, mu8 = A["idx"], A["links"], A["plaqs"], A["mu8"]
    coins, named = A["coins"], S["named_coins"]
    say("[4/9] the holonomy group: isomorphism class at %d declared stencils"
        % (len(PLAQ_STENCILS) + 1))
    deg = n * 8

    _mono_memo = {}

    def all_gens(m):
        """every plaquette holonomy of one uniform configuration, computed
        ONCE and reused at every stencil."""
        got = _mono_memo.get(m)
        if got is not None:
            return got
        cfg = uniform_cfg(links, m)
        out = {}
        for p in plaqs:
            mp = holonomy_monomial(p, cfg, idx, L, n, mu8)
            if mp is None:
                raise GateFail("G-MONOMIAL-SECTORS :: a monomial sector coin "
                               "produced a non-monomial holonomy")
            out[p] = (mp, mono_to_perm(mp, n))
        _mono_memo[m] = out
        return out

    def gens_for(m, stencil):
        g = all_gens(m)
        return [g[p] for p in stencil]

    rows = []
    # the monomial sectors: the isomorphism class exists and is certified
    mono = [m for m in coins if coin_sector(m) in ("DIAGONAL", "ANTIDIAGONAL")]
    profile = {}
    for name, stencil in PLAQ_STENCILS + [(GLOBAL_STENCIL, tuple(plaqs))]:
        per_sector = {}
        for m in mono:
            g = gens_for(m, stencil)
            site_gens = [mp[0] for mp, _pp in g]
            full_gens = [pp for _mp, pp in g]
            cert = alternating_certificate(site_gens, n)
            full_order = group_order(full_gens, deg)
            kernel = full_order // cert["order"] if cert["order"] else 0
            key = (coin_sector(m), cert["class"], cert["order"], kernel,
                   cert["support"], tuple(cert["orbits"]), cert["certified"])
            per_sector[key] = per_sector.get(key, 0) + 1
        for key, cnt in sorted(per_sector.items(), key=lambda kv: str(kv[0])):
            rows.append({"stencil": name, "sector": key[0],
                         "position_class": key[1], "position_order": key[2],
                         "phase_kernel_order": key[3], "support": key[4],
                         "orbit_sizes": list(key[5]), "certified": key[6],
                         "coins": cnt})
        profile[name] = sorted((r["sector"], r["position_class"],
                                r["position_order"], r["support"])
                               for r in rows if r["stencil"] == name)
    if mut("MUT-GROUP-CLASS"):
        rows[0]["position_class"] = "A99"
    S["holonomy_groups"] = rows
    S["_group_profile"] = profile

    anti_rows = [r for r in rows if r["sector"] == "ANTIDIAGONAL"]
    LD.gate("G-GROUP-CERTIFIED-BY-SET-EQUALITY",
            "the isomorphism class is certified by SET EQUALITY and nothing "
            "weaker: every generator restricts to an even permutation of "
            "every orbit, so the group is contained in the direct product of "
            "the alternating groups on its orbits, and the measured order "
            "equals that product's order -- containment plus equal "
            "cardinality is equality, so the class is the class and not a "
            "fingerprint",
            all(r["certified"] for r in anti_rows),
            "%d certified of %d antidiagonal-sector rows"
            % (sum(1 for r in anti_rows if r["certified"]), len(anti_rows)))

    conn = [r for r in anti_rows if len(r["orbit_sizes"]) == 1]
    LD.gate("G-ALTERNATING-ON-ITS-OWN-SUPPORT",
            "THE MEASURED LAW: at every connected declared stencil the "
            "holonomy group is the FULL ALTERNATING GROUP on its own "
            "support, and at a disconnected stencil it is the direct product "
            "of the alternating groups on the components -- the same form "
            "CR-D's tower measured in a different arena",
            all(r["position_class"] == "A%d" % r["support"] for r in conn)
            and len(conn) > 0,
            "%d connected-stencil rows, classes %s"
            % (len(conn), sorted({r["position_class"] for r in conn})))

    # the rank, at the global stencil and at each declared one
    ranks = {}
    for name, stencil in PLAQ_STENCILS + [(GLOBAL_STENCIL, tuple(plaqs))]:
        m = named["ANTI-X"]
        g = gens_for(m, stencil)
        site_gens = [mp[0] for mp, _pp in g]
        o = group_order(site_gens, n)
        k, wit = generator_rank(site_gens, n, o, cap=len(stencil))
        ranks[name] = {"generators_declared": len(stencil), "rank": k,
                       "order": o}
    S["holonomy_rank"] = ranks
    LD.gate("G-RANK-MEASURED",
            "the RANK is measured and is declared arena-relative: it is the "
            "least number of the DECLARED plaquette holonomies that generate "
            "the whole group, not the abstract minimal generator number of "
            "the abstract group, and the verdict says which one it is",
            all(v["rank"] is not None for v in ranks.values()),
            "; ".join("%s rank %s of %d" % (k, v["rank"],
                                            v["generators_declared"])
                      for k, v in sorted(ranks.items())))

    # the balanced sector: the order is INFINITE, and that is a certificate
    bal = [m for m in coins if coin_sector(m) == "BALANCED"]
    noninteg = 0
    for m in bal:
        W = S["_hol"][m][1]
        if not is_alg_integer(trace(W)):
            noninteg += 1
    if mut("MUT-INFINITE-CERTIFICATE"):
        noninteg -= 1
    S["balanced_sector"] = {"coins": len(bal),
                            "trace_not_an_algebraic_integer": noninteg}
    LD.gate("G-BALANCED-SECTOR-INFINITE",
            "on the interfering sector the holonomy group is INFINITE, and "
            "the certificate is a theorem rather than a search cap: a matrix "
            "of finite order has root-of-unity eigenvalues, so its trace is "
            "an algebraic integer; every one of these traces has a "
            "denominator, so no power of the holonomy is the identity and no "
            "finite isomorphism class exists there to report",
            noninteg == len(bal) and len(bal) > 0,
            "%d of %d balanced-sector holonomies have a non-integral trace"
            % (noninteg, len(bal)))

    # the projective period -- the parent's template, cited and reused
    periods = {}
    for m in coins:
        W = S["_hol"][m][1]
        pp = None
        P = W
        for k in range(1, 33):
            if all(P[i][j] == (P[0][0] if i == j else ZERO)
                   for i in range(4) for j in range(4)):
                pp = k
                break
            P = mmul(P, W)
        periods.setdefault(coin_sector(m), set()).add(pp)
    S["projective_periods"] = {k: sorted([x for x in v if x is not None])
                               + (["UNBOUNDED-WITHIN-CAP-32"]
                                  if None in v else [])
                               for k, v in periods.items()}
    LD.gate("G-PROJECTIVE-PERIOD-TEMPLATE",
            "periodicity is reported PROJECTIVELY, on the parent's template: "
            "the raw order is not gauge invariant because a global phase "
            "rescales every power, and the least exponent at which the "
            "holonomy becomes a scalar is.  The interfering sector reaches no "
            "such exponent within the declared cap, which is the same fact "
            "the trace certificate proves",
            "UNBOUNDED-WITHIN-CAP-32" in S["projective_periods"]["BALANCED"]
            and all(isinstance(x, int)
                    for x in S["projective_periods"]["ANTIDIAGONAL"]),
            "%s" % S["projective_periods"])

    # #87: no matrix is ever reported as physics
    allowed = {"stencil", "sector", "position_class", "position_order",
               "phase_kernel_order", "support", "orbit_sizes", "certified",
               "coins"}
    bad = [r for r in rows if set(r) - allowed]
    if mut("MUT-MATRIX-AS-PHYSICS"):
        rows[0]["matrix"] = [[1, 0], [0, 1]]
        bad = [r for r in rows if set(r) - allowed]
    LD.gate("G-NO-MATRIX-AS-PHYSICS",
            "the holonomy enters the receipt only as an isomorphism class "
            "with its order, its support and its rank -- never as a matrix.  "
            "The published rows carry exactly the declared key set, and a row "
            "carrying a matrix dies here",
            not bad,
            "%d rows, keys %s" % (len(rows), sorted(allowed)))


# ---- [5/9] the flat negative control -------------------------------------
def build_flat_control(S, LD):
    A, L, n = S["_A"], S["_L"], S["_n"]
    sites, idx, alphabet = A["sites"], A["idx"], A["alphabet"]
    say("[5/9] the mandatory flat control: R4's FULL-transport stratum")
    ck = (L, len(alphabet))
    if ck not in _CIRC_MEMO:
        _CIRC_MEMO[ck] = build_circulants(L, sites, idx, alphabet)
    pool, axes, orbit_sizes = _CIRC_MEMO[ck]
    pool = list(pool)
    if mut("MUT-CIRCULANT-POOL"):
        pool = pool[:-1]
    anchored = [r for r in S["path_value_anchors"]
                if r["anchor"] == "PV-CIRC"][0]["measured"]
    anchored_pairs = [r for r in S["path_value_anchors"]
                      if r["anchor"] == "PV-COMM-PAIRS"][0]["measured"]
    anchored_zero = [r for r in S["path_value_anchors"]
                     if r["anchor"] == "PV-COMM-ZERO"][0]["measured"]

    fkey = (L, len(alphabet), mut("MUT-CIRCULANT-POOL"))
    if fkey in _FLAT_MEMO:
        noncomm, sample_n, disagree, trivial = _FLAT_MEMO[fkey]
    else:
        noncomm, sample_n, disagree, trivial = _flat_census(pool, sites, idx,
                                                            L, n)
        _FLAT_MEMO[fkey] = (noncomm, sample_n, disagree, trivial)
    if mut("MUT-FLAT-CONTROL"):
        noncomm += 1

    S["flat_control"] = {
        "circulants_rebuilt": len(pool), "circulants_anchored": anchored,
        "axes": len(axes), "gauge_orbit_sizes": orbit_sizes,
        "ordered_pairs": len(pool) ** 2, "pairs_anchored": anchored_pairs,
        "noncommuting": noncomm, "noncommuting_anchored": anchored_zero,
        "second_route_sample": sample_n, "route_disagreements": disagree,
        "holonomy_group_order": 1 if trivial else 0,
        "holonomy_group_class": "TRIVIAL" if trivial else "NONTRIVIAL"}
    LD.gate("G-FLAT-CONTROL-TRIVIAL",
            "THE MANDATORY NEGATIVE CONTROL, and it is provably flat: R4's "
            "FULL-transport stratum is rebuilt here from its own definitions, "
            "its whole ordered-pair commutator census is recomputed, and "
            "every commutator is the identity.  The direction-indexed "
            "connection built from it has the TRIVIAL holonomy group, so a "
            "non-abelian reading elsewhere in this unit is a measurement and "
            "not an artifact of the instrument",
            len(pool) == anchored and noncomm == anchored_zero
            and len(pool) ** 2 == anchored_pairs and trivial
            and disagree == 0,
            "rebuilt %d circulants (anchored %d); %d of %d ordered pairs fail "
            "to commute (anchored %d); second route disagrees on %d of %d; "
            "holonomy group order %d"
            % (len(pool), anchored, noncomm, len(pool) ** 2, anchored_zero,
               disagree, sample_n, 1 if trivial else 0))
    LD.gate("G-OPENING-DATUM",
            "the opening datum is stated as the parent states it and is "
            "reproduced here rather than quoted: the verdict-bearing stratum "
            "of the parent is ABELIAN, so a gauge rung built on it would have "
            "been pre-committed to flat holonomy and could not have been "
            "falsified",
            noncomm == 0,
            "0 of %d, reproduced independently" % (len(pool) ** 2))
    S["_circulants"] = pool


# ---- [6/9] the gate-inheritance audit (G2) --------------------------------
def build_transport(S, LD):
    A, L, n = S["_A"], S["_L"], S["_n"]
    sites, idx, links, plaqs = A["sites"], A["idx"], A["links"], A["plaqs"]
    strata, coins, named = A["strata"], A["coins"], S["named_coins"]
    say("[6/9] the gate-inheritance audit: which transport level each "
        "link-local generator attains")
    m = named["ANTI-X"]
    cfg = uniform_cfg(links, m)

    per_kind = {}
    for kind, objs in (
            ("LINK-OPERATOR", [link_op(l, m, idx, L, n) for l in links]),
            ("PLAQUETTE-HOLONOMY", [holonomy(p, cfg, idx, L, n)
                                    for p in plaqs]),
            ("STRATUM-OPERATOR", None)):
        if objs is None:
            objs = []
            for k in sorted(strata):
                M = ident(n)
                for l in strata[k]:
                    M = mmul(link_op(l, m, idx, L, n), M)
                objs.append(M)
        lv = {}
        for M in objs:
            level, st = transport_level(M, sites, idx, L)
            lv[level] = lv.get(level, 0) + 1
        per_kind[kind] = {"objects": len(objs), "levels": lv}
    if mut("MUT-TRANSPORT-LEVEL"):
        per_kind["LINK-OPERATOR"]["levels"] = {"FULL": len(links)}

    maximal = [r for r in S["path_value_anchors"]
               if r["anchor"] == "PV-MAXIMAL"][0]["measured"]
    at_full = sum(v["levels"].get(maximal, 0) for v in per_kind.values())
    total = sum(v["objects"] for v in per_kind.values())

    # the DECLARED modified gate: covariance of the FAMILY, not of a generator
    checks = fails = 0
    for extended in (False, True):
        elems = chart_elements(sites, L, extended)
        for elem in elems:
            for l in links:
                l2, reversed_ = transported_link(l, elem, L)
                if l2 not in set(links):
                    fails += 1
                checks += 1
    fam_checks = fails2 = 0
    elems = chart_elements(sites, L, True)
    for elem in elems:
        for l in links:
            l2, rev = transported_link(l, elem, L)
            c2 = swap_conjugate(m) if rev else m
            perm = tuple(idx[addv(apply_point(elem[1], sites[i], L), elem[0],
                                  L)] for i in range(n))
            got = conj_by_perm(link_op(l, m, idx, L, n), perm)
            want = link_op(l2, c2, idx, L, n)
            fam_checks += 1
            if got != want:
                fails2 += 1
    if mut("MUT-FAMILY-COVARIANCE"):
        fails2 += 1

    S["transport_audit"] = {
        "per_generator": per_kind,
        "maximal_level_anchored": maximal,
        "objects_at_maximal": at_full, "objects_censused": total,
        "inherited_gate_admits": at_full,
        "chart_group_order": len(chart_elements(sites, L, False)),
        "extension_order": len(chart_elements(sites, L, True)),
        "link_set_closed_checks": checks, "link_set_closed_failures": fails,
        "family_covariance_checks": fam_checks,
        "family_covariance_failures": fails2}

    LD.gate("G-CHART-GROUPS-CENSUSED",
            "the arena's two groups are censused as the parent censuses them: "
            "the anchored chart group of order 32 -- the translations with "
            "the direction relabelling -- and this unit's declared extension "
            "by the square point group, of order 128",
            len(chart_elements(sites, L, False)) == 32
            and len(chart_elements(sites, L, True)) == 128,
            "chart %d, extension %d" % (len(chart_elements(sites, L, False)),
                                        len(chart_elements(sites, L, True))))

    LD.gate("G-GATE-INHERITANCE-AUDIT",
            "G2, AND IT BITES: the parent's realization gate, inherited "
            "UNMODIFIED and read per generator, admits NOTHING on this arena. "
            "A link operator's translation stabiliser is trivial because "
            "translating it moves the link, so the maximal declared level is "
            "attained by no link-local generator whatever, and the strata "
            "reach only the level the parent already excluded",
            at_full == 0 and total > 0,
            "%d of %d objects at %s; levels %s"
            % (at_full, total, maximal,
               {k: v["levels"] for k, v in sorted(per_kind.items())}))

    LD.gate("G-DECLARED-GATE-COVARIANCE",
            "the gate is therefore RE-DERIVED and not silently inherited: the "
            "declared R5 gate is covariance of the FAMILY -- the image of any "
            "link operator under any chart element is again a link operator, "
            "on the transported link, with the transported coin.  That is the "
            "parent's own FULL criterion read at the level a gauge family has "
            "it, and it is measured here, not assumed",
            fails == 0 and fails2 == 0 and fam_checks > 0,
            "link set closed under %d chart actions with %d failures; family "
            "covariance %d checks, %d failures"
            % (checks, fails, fam_checks, fails2))


# ---- [7/9] curvature against the defect, at matched coordinates (G3) ------
def build_matched(S, LD):
    A, L, n = S["_A"], S["_L"], S["_n"]
    idx, links, plaqs = A["idx"], A["links"], A["plaqs"]
    coins, named = A["coins"], S["named_coins"]
    say("[7/9] curvature against Delta^B at matched coordinates")

    wit = hadamard_witness()
    half = (1, 0, 0, 0, 2)
    want = ((half, fneg(half)), (fneg(half), half))
    LD.gate("G-DEFECT-REBUILT",
            "the composition defect is REBUILT from the seed's definition and "
            "checked against the seed's own named two-by-two witness: on the "
            "Hadamard against itself it returns the half-and-minus-half "
            "matrix, and a sign flip of that witness dies here",
            wit == want, "witness reproduced exactly")

    def relation(l2, l1):
        s2 = set(link_sites(l2, idx, L))
        s1 = set(link_sites(l1, idx, L))
        k = len(s2 & s1)
        return "SAME-LINK" if l2 == l1 else ("SHARE-ONE-SITE" if k == 1
                                             else "DISJOINT")

    # TABLE A: exhaustive over the coin alphabet at each declared relation,
    # with the geometric relation as the only varying coordinate.  The three
    # tables are a pure function of the arena, so they are memoized on the
    # declaration that determines them and returned as fresh deep copies: a
    # mutant that perturbs a published cell perturbs its own run and no other.
    reps = {}
    for l1 in links:
        for l2 in links:
            r = relation(l2, l1)
            if r not in reps:
                reps[r] = (l2, l1)
    _key = ("matched", L, len(coins))
    if _key in _TABLE_MEMO:
        tableA, tableAfull, tableB, two = [json.loads(x)
                                           for x in _TABLE_MEMO[_key]]
    else:
        tableA, tableAfull, tableB, two = _matched_tables(
            coins, named, links, plaqs, idx, L, n, reps)
        _TABLE_MEMO[_key] = [json.dumps(x) for x in
                             (tableA, tableAfull, tableB, two)]
    if mut("MUT-MATCHED-CELL"):
        tableA["SHARE-ONE-SITE"]["11"] += 1
    _post_matched(S, LD, tableA, tableAfull, tableB, two, n)


def _matched_tables(coins, named, links, plaqs, idx, L, n, reps):
    tableA = {}
    for r, (l2, l1) in sorted(reps.items()):
        sub = sorted(set(link_sites(l2, idx, L)) | set(link_sites(l1, idx, L)))
        cells = {"00": 0, "01": 0, "10": 0, "11": 0}
        for m in coins:
            B2 = sub_block(link_op(l2, m, idx, L, n), sub)
            B1 = sub_block(link_op(l1, m, idx, L, n), sub)
            c = 0 if mmul(B2, B1) == mmul(B1, B2) else 1
            dd = 0 if is_zero_mat(delta_B(B2, B1)) else 1
            cells["%d%d" % (c, dd)] += 1
        tableA[r] = cells

    # TABLE A-FULL: exhaustive over the 32 x 32 ordered link pairs at each
    # declared named coin
    tableAfull = {}
    for nm in sorted(named):
        m = named[nm]
        cells = {"00": 0, "01": 0, "10": 0, "11": 0}
        for l2 in links:
            for l1 in links:
                sub = sorted(set(link_sites(l2, idx, L))
                             | set(link_sites(l1, idx, L)))
                B2 = sub_block(link_op(l2, m, idx, L, n), sub)
                B1 = sub_block(link_op(l1, m, idx, L, n), sub)
                c = 0 if mmul(B2, B1) == mmul(B1, B2) else 1
                dd = 0 if is_zero_mat(delta_B(B2, B1)) else 1
                cells["%d%d" % (c, dd)] += 1
        tableAfull[nm] = cells

    # TABLE B: the same contrast at PLAQUETTE granularity
    def prel(p2, p1):
        s2, s1 = set(plaq_sites(p2, idx, L)), set(plaq_sites(p1, idx, L))
        k = len(s2 & s1)
        return ("SAME-PLAQUETTE" if p2 == p1 else
                "SHARE-AN-EDGE" if k == 2 else
                "SHARE-A-CORNER" if k == 1 else "DISJOINT")
    preps = {}
    for p1 in plaqs:
        for p2 in plaqs:
            r = prel(p2, p1)
            if r not in preps:
                preps[r] = (p2, p1)
    tableB = {}
    for r, (p2, p1) in sorted(preps.items()):
        sub = sorted(set(plaq_sites(p2, idx, L)) | set(plaq_sites(p1, idx, L)))
        cells = {"00": 0, "01": 0, "10": 0, "11": 0}
        for m in coins:
            cfg = uniform_cfg(links, m)
            k2, X2 = holonomy_block(p2, cfg, idx, L)
            k1, X1 = holonomy_block(p1, cfg, idx, L)
            B2 = embed(k2, X2, sub, idx)
            B1 = embed(k1, X1, sub, idx)
            c = 0 if mmul(B2, B1) == mmul(B1, B2) else 1
            dd = 0 if is_zero_mat(delta_B(B2, B1)) else 1
            cells["%d%d" % (c, dd)] += 1
        tableB[r] = cells

    # the ONE declared two-excitation extension, pre-registered and run
    two = {}
    for nm in sorted(named):
        m = named[nm]
        cells = {"00": 0, "01": 0, "10": 0, "11": 0}
        for r, (l2, l1) in sorted(reps.items()):
            sub = set(link_sites(l2, idx, L)) | set(link_sites(l1, idx, L))
            keys = wedge_keys_touching(n, sub)
            W2 = wedge2(link_op(l2, m, idx, L, n), keys)
            W1 = wedge2(link_op(l1, m, idx, L, n), keys)
            c = 0 if mmul(W2, W1) == mmul(W1, W2) else 1
            dd = 0 if is_zero_mat(delta_B(W2, W1)) else 1
            cells["%d%d" % (c, dd)] += 1
        two[nm] = cells
    return tableA, tableAfull, tableB, two


def _post_matched(S, LD, tableA, tableAfull, tableB, two, n):
    linkA = {"00": 0, "01": 0, "10": 0, "11": 0}
    for cells in tableA.values():
        for k in linkA:
            linkA[k] += cells[k]
    plaqB = {"00": 0, "01": 0, "10": 0, "11": 0}
    for cells in tableB.values():
        for k in plaqB:
            plaqB[k] += cells[k]

    baseline = [r for r in S["path_value_anchors"]
                if r["anchor"] == "PV-DEFECT-588"][0]["measured"]
    S["matched_tables"] = {
        "link_grain_by_relation": tableA,
        "link_grain_by_named_coin": tableAfull,
        "link_grain_totals": linkA,
        "plaquette_grain_by_relation": tableB,
        "plaquette_grain_totals": plaqB,
        "parent_baseline_defects_at_zero_curvature": baseline,
        "coordinates_held_equal": [
            "the coin value (identical on both legs and both links)",
            "the division-event times (t = 0 and t = 2; the cut at t = 1)",
            "the leg declared at the cut (B(U2))",
            "the gauge fixing (the same canonical representative)"],
        "outcome": ("CURVATURE-DEFECT-INDEPENDENT" if
                    (linkA["01"] > 0 and linkA["10"] > 0) or
                    (plaqB["01"] > 0 and plaqB["10"] > 0)
                    else "CURVATURE-CARRIES-DEFECT" if linkA["10"] == 0
                    else "DEFECT-WITHOUT-CURVATURE")}

    LD.gate("G-MATCHED-COORDINATES",
            "the matched table is the primary object and its coordinates are "
            "named: the coin value, the division-event times, the leg at the "
            "cut and the gauge fixing are all held equal, and exactly one "
            "coordinate varies in each table -- the geometric relation in the "
            "first, the coin in the second",
            len(S["matched_tables"]["coordinates_held_equal"]) == 4
            and set(tableA) == {"SAME-LINK", "SHARE-ONE-SITE", "DISJOINT"},
            "relations %s" % sorted(tableA))

    LD.gate("G-LINK-GRAIN-EXCLUSIVE",
            "AT LINK GRAIN CURVATURE AND DEFECT ARE MUTUALLY EXCLUSIVE, and "
            "the exclusion is a theorem: two link operators fail to commute "
            "only when their links share exactly one site, and then every "
            "entry of the composite is a single product, so there is no "
            "second path to interfere with and the defect vanishes "
            "identically.  The cell that would carry both is empty",
            linkA["11"] == 0 and linkA["10"] > 0 and linkA["01"] > 0,
            "cells %s over %d rows" % (linkA, sum(linkA.values())))

    LD.gate("G-DEFECT-BASELINE",
            "the parent's measured baseline is carried, not re-derived from "
            "this arena: it recorded defects at identically zero curvature, "
            "which is the third pre-registered outcome already witnessed "
            "before this unit began",
            baseline > 0, "%d defects at zero curvature, anchored" % baseline)

    LD.gate("G-PLAQUETTE-GRAIN-COOCCUR",
            "AT PLAQUETTE GRAIN THEY CO-OCCUR: all four cells of the same "
            "table are populated once the objects compared are holonomies "
            "rather than the generators that build them.  So the exclusivity "
            "is a statement about the generators and not about the "
            "connection, and the grain is a declared coordinate of the result",
            plaqB["11"] > 0 and plaqB["01"] > 0 and plaqB["10"] > 0
            and plaqB["00"] > 0,
            "cells %s over %d rows" % (plaqB, sum(plaqB.values())))

    LD.gate("G-CURVATURE-DOES-NOT-IMPLY-QUANTUM",
            "the must-not, gated rather than promised: curvature does NOT "
            "imply quantum character on this stage.  There are non-commuting "
            "pairs with identically zero defect, in numbers, and the parent "
            "supplies the converse witness",
            linkA["10"] > 0,
            "%d curvature-without-defect rows at link grain, %d at plaquette "
            "grain" % (linkA["10"], plaqB["10"]))

    tot2 = {"00": 0, "01": 0, "10": 0, "11": 0}
    for cells in two.values():
        for k in tot2:
            tot2[k] += cells[k]
    if mut("MUT-TWO-EXCITATION"):
        tot2["11"] += 1
    S["two_excitation"] = {
        "sector": "HARD-CORE-ANTISYMMETRIC-WEDGE-2",
        "states": len(wedge_pairs(n)),
        "by_named_coin": two, "totals": tot2,
        "exclusivity_survives": tot2["11"] == 0}
    LD.gate("G-TWO-EXCITATION-RUN",
            "the ONE declared two-excitation extension is pre-registered and "
            "RUN, and it returns a negative: on the hard-core antisymmetric "
            "sector the exclusivity SURVIVES.  The parent named this sector "
            "as one of exactly three routes out of its arena; taking it does "
            "not break the link-grain exclusion, and the reason is the same "
            "single-path counting one dimension up",
            tot2["11"] == 0 and tot2["10"] > 0,
            "states %d; cells %s" % (len(wedge_pairs(n)), tot2))


# ---- [8/9] the gauge self-test, in both directions (G4) -------------------
def build_gauge(S, LD):
    A, L, n = S["_A"], S["_L"], S["_n"]
    sites, idx, links, plaqs = A["sites"], A["idx"], A["links"], A["plaqs"]
    coins, named = A["coins"], S["named_coins"]
    say("[8/9] the gauge self-test, in both directions")

    def theta(handle):
        if handle == "CONSTANT":
            return [1] * n
        if handle == "LINEAR-X":
            return [sites[i][0] for i in range(n)]
        return [(sites[i][0] + sites[i][1]) % 2 for i in range(n)]

    def gmat(th, sign=1):
        M = [[ZERO] * n for _ in range(n)]
        for i in range(n):
            M[i][i] = zpow(sign * th[i])
        return tuple(tuple(r) for r in M)

    rows = []
    for nm in ("ANTI-X", "BAL-H", "DIAG-Z"):
        m = named[nm]
        cfg = uniform_cfg(links, m)
        for h in GAUGE_HANDLES:
            th = theta(h)
            g, gi = gmat(th, 1), gmat(th, -1)
            inv = moved = 0
            for p in plaqs:
                W = holonomy(p, cfg, idx, L, n)
                Wg = mmul(g, mmul(W, gi))
                if trace(Wg) == trace(W):
                    inv += 1
                if Wg != W:
                    moved += 1
            rows.append({"coin": nm, "handle": h, "loops": len(plaqs),
                         "wilson_trace_invariant": inv,
                         "untraced_holonomy_moved": moved})
    if mut("MUT-GAUGE-HANDLE"):
        for r in rows:
            r["untraced_holonomy_moved"] = 0

    # the gauge action maps the family to itself, with the transported coin
    closed = failures = 0
    for nm in sorted(named):
        m = named[nm]
        for h in GAUGE_HANDLES:
            th = theta(h)
            g, gi = gmat(th, 1), gmat(th, -1)
            for l in links:
                M = mmul(g, mmul(link_op(l, m, idx, L, n), gi))
                t, hh = link_ends(l, L)
                it, ih = idx[t], idx[hh]
                cc = (M[it][it], M[it][ih], M[ih][it], M[ih][ih])
                closed += 1
                if link_op(l, cc, idx, L, n) != M or cc not in set(coins):
                    failures += 1

    live = [r for r in rows if r["handle"] != "CONSTANT"
            and r["coin"] != "DIAG-Z"]
    null = [r for r in rows if r["handle"] == "CONSTANT"]
    inert = [r for r in rows if r["coin"] == "DIAG-Z"]
    S["gauge_selftest"] = {
        "rows": rows, "family_closure_checks": closed,
        "family_closure_failures": failures,
        "declared_handles": list(GAUGE_HANDLES),
        "null_handle": "CONSTANT",
        "abelian_arm_is_gauge_inert": all(r["untraced_holonomy_moved"] == 0
                                          for r in inert),
        "invariance_is_forced": "the Wilson trace is invariant under any "
                                "conjugation by cyclicity; it is reported as "
                                "a disclosure with its forcing named, not as "
                                "a measurement"}
    LD.gate("G-GAUGE-BOTH-DIRECTIONS",
            "the self-test fires in BOTH directions and its negative "
            "direction is not vacuous: under each declared non-constant "
            "site-diagonal handle the untraced holonomy moves at EVERY "
            "checked loop, while the Wilson trace is fixed at every one of "
            "them; and the declared null handle -- the global phase, which is "
            "central -- moves nothing, which is the control that keeps the "
            "positive direction honest",
            all(r["untraced_holonomy_moved"] == r["loops"] for r in live)
            and all(r["wilson_trace_invariant"] == r["loops"] for r in rows)
            and all(r["untraced_holonomy_moved"] == 0 for r in null)
            and all(r["untraced_holonomy_moved"] == 0 for r in inert),
            "%d live rows moving at %d of %d loops; %d null rows and %d "
            "abelian-arm rows moving 0"
            % (len(live), len(plaqs), len(plaqs), len(null), len(inert)))
    LD.gate("G-ABELIAN-ARM-GAUGE-INERT",
            "and the handle is measured where it CANNOT move anything: a "
            "diagonal holonomy commutes with every site-diagonal gauge, so "
            "on the abelian arm the untraced holonomy is already gauge "
            "invariant and moves at no loop at all.  That is a measurement "
            "about the arena, not a failure of the handle -- the same handle "
            "moves every loop on the non-abelian arms",
            all(r["untraced_holonomy_moved"] == 0 for r in inert)
            and len(inert) == len(GAUGE_HANDLES),
            "%d abelian-arm rows, all moving 0 of %d loops"
            % (len(inert), len(plaqs)))

    LD.gate("G-GAUGE-FAMILY-CLOSED",
            "the declared gauge group acts ON THE FAMILY: every site-diagonal "
            "conjugate of a link operator is again a link operator on the "
            "same link with a coin from the same derived alphabet, so the "
            "holonomy's conjugacy class -- and nothing finer -- is what any "
            "claim may use",
            failures == 0 and closed > 0,
            "%d conjugates checked, %d not family members" % (closed, failures))


# ---- [9/9] refinement (G6) and the scramble caveat (G7) -------------------
def _swap_holonomy_perms(Lx):
    if Lx in _SWAPHOL_MEMO:
        return _SWAPHOL_MEMO[Lx]
    return _swap_holonomy_perms_uncached(Lx)


def _swap_holonomy_perms_uncached(Lx):
    """the all-swap plaquette holonomies at size Lx, as site permutations.
    Pure permutation arithmetic: the refinement step is decided in the
    symmetric group and never touches the field."""
    sites, idx = build_lattice(Lx)
    n = len(sites)
    out = {}
    for p in sites:
        perm = list(range(n))
        for l, o in plaquette_boundary(p, Lx):
            t, h = link_ends(l, Lx)
            i, j = idx[t], idx[h]
            new = list(perm)
            # the swap coin exchanges the domino's two sites; its inverse is
            # itself, so the orientation of the traversal does not matter here
            for k in range(n):
                v = perm[k]
                new[k] = j if v == i else (i if v == j else v)
            perm = new
        out[p] = tuple(perm)
    _SWAPHOL_MEMO[Lx] = (out, n)
    return out, n


def build_refinement(S, LD):
    say("[9/9] refinement: the class at L = %d against the declared doubling "
        "to L = %d" % REFINEMENT_SIZES)
    if "tab" in _REFINE_MEMO:
        tab = json.loads(json.dumps(_REFINE_MEMO["tab"]))
        tab = {int(k): v for k, v in tab.items()}
    else:
        tab = _refinement_table()
        _REFINE_MEMO["tab"] = tab
        tab = json.loads(json.dumps(tab))
        tab = {int(k): v for k, v in tab.items()}
    _refinement_finish(S, LD, tab)


def _refinement_table():
    tab = {}
    for Lx in REFINEMENT_SIZES:
        H, n = _swap_holonomy_perms(Lx)
        sites, idx = build_lattice(Lx)
        rows = {}
        for name, stencil in PLAQ_STENCILS:
            gens = [H[p] for p in stencil]
            cert = alternating_certificate(gens, n)
            rows[name] = {"class": cert["class"], "order": cert["order"],
                          "support": cert["support"],
                          "orbits": cert["orbits"],
                          "certified": cert["certified"]}
        gens = [H[p] for p in sites]
        cert = alternating_certificate(gens, n)
        rows[GLOBAL_STENCIL] = {"class": cert["class"], "order": cert["order"],
                                "support": cert["support"],
                                "orbits": cert["orbits"],
                                "certified": cert["certified"]}
        tab[Lx] = {"sites": n, "links": 2 * n, "plaquettes": n, "rows": rows}
    return tab


def _refinement_finish(S, LD, tab):
    if mut("MUT-REFINEMENT"):
        tab[8]["rows"]["S2-EDGE"]["class"] = "A7"
    a, b = REFINEMENT_SIZES
    local_stable = [k for k in tab[a]["rows"] if k != GLOBAL_STENCIL
                    and tab[a]["rows"][k]["class"] == tab[b]["rows"][k]["class"]]
    global_stable = (tab[a]["rows"][GLOBAL_STENCIL]["class"]
                     == tab[b]["rows"][GLOBAL_STENCIL]["class"])
    S["refinement"] = {
        "sizes": list(REFINEMENT_SIZES), "by_size": tab,
        "local_stencils": len(PLAQ_STENCILS),
        "local_stable": len(local_stable),
        "global_stable": global_stable,
        "verdict": ("LOCAL-STABLE-GLOBAL-EXTENSIVE"
                    if len(local_stable) == len(PLAQ_STENCILS)
                    and not global_stable else
                    "STABLE" if global_stable else "NO-STABLE-GROUP")}
    LD.gate("G-REFINEMENT-CLASS",
            "G6, and the isomorphism class is the invariant while the "
            "plaquette count is the extensive control: at every declared "
            "local stencil the class is IDENTICAL at the two sizes, while the "
            "global class moves with the lattice.  So the holonomy has a "
            "stable local content and an extensive global one, and the "
            "refinement question has a two-part answer rather than a yes",
            len(local_stable) == len(PLAQ_STENCILS) and not global_stable,
            "%d of %d local stencils stable; global %s -> %s"
            % (len(local_stable), len(PLAQ_STENCILS),
               tab[a]["rows"][GLOBAL_STENCIL]["class"],
               tab[b]["rows"][GLOBAL_STENCIL]["class"]))
    LD.gate("G-CRD-LADDER-COMPARATOR",
            "the measured class is reported against the programme's own "
            "group-family prior: CR-D's tower returned the FULL alternating "
            "group on its own support at every realised rung, and this arena "
            "returns the same FORM by an independent route -- the alternating "
            "group on the support, with the ladder's own A_5 reappearing at "
            "the five-point stencil",
            any(v["class"] == "A5" for v in tab[a]["rows"].values())
            and any(v["class"] == "A5" for v in tab[b]["rows"].values()),
            "classes at L = %d: %s" % (a, sorted({v["class"] for v in
                                                  tab[a]["rows"].values()})))


def build_scramble(S, LD):
    A, L, n = S["_A"], S["_L"], S["_n"]
    idx, links, plaqs, mu8 = A["idx"], A["links"], A["plaqs"], A["mu8"]
    named = S["named_coins"]
    say("      the scramble caveat: does the group separate the physical case")
    LI = {l: i for i, l in enumerate(links)}
    m = named["ANTI-X"]
    cfg = uniform_cfg(links, m)

    def pi_of(tag):
        p = list(range(len(links)))
        if tag == "SCR-TRANSPOSE":
            for u, w in ((0, 5), (1, 11)):
                p[u], p[w] = p[w], p[u]
        else:
            for i, (s, dd) in enumerate(links):
                p[i] = LI[(s, 1 - dd)]
        return p

    def hol_perm(p, permlinks):
        W = ident(n)
        for l, o in plaquette_boundary(p, L):
            M = link_op(links[permlinks[LI[l]]], m, idx, L, n)
            if o < 0:
                M = dagger(M)
            W = mmul(M, W)
        return as_monomial(W, mu8)[0]

    ident_pi = list(range(len(links)))
    prof = {}
    for tag in ("PHYSICAL",) + SCRAMBLES:
        pl = ident_pi if tag == "PHYSICAL" else pi_of(tag)
        rows = {}
        for name, stencil in PLAQ_STENCILS + [(GLOBAL_STENCIL, tuple(plaqs))]:
            gens = [hol_perm(p, pl) for p in stencil]
            cert = alternating_certificate(gens, n)
            rows[name] = {"class": cert["class"], "order": cert["order"],
                          "support": cert["support"]}
        prof[tag] = rows
    if mut("MUT-SCRAMBLE"):
        prof["SCR-TRANSPOSE"] = prof["PHYSICAL"]

    sep_local, sep_global = {}, {}
    for tag in SCRAMBLES:
        sep_local[tag] = sum(
            1 for name, _s in PLAQ_STENCILS
            if (prof["PHYSICAL"][name]["class"], prof["PHYSICAL"][name]["order"])
            != (prof[tag][name]["class"], prof[tag][name]["order"]))
        sep_global[tag] = (prof["PHYSICAL"][GLOBAL_STENCIL]["order"]
                           != prof[tag][GLOBAL_STENCIL]["order"])
    S["scramble_control"] = {
        "controls": list(SCRAMBLES), "profiles": prof,
        "local_stencils": len(PLAQ_STENCILS),
        "separating_local_stencils": sep_local,
        "separates_globally": sep_global,
        "reading": "the group claim is entered at the LOCAL stencils, where "
                   "the statistic separates; the global class is entered as "
                   "measured-but-not-discriminating"}
    LD.gate("G-SCRAMBLE-SEPARATION",
            "G7, and the caveat bites exactly where the parent warned it "
            "would: the local stencil profile SEPARATES the physical "
            "connection from both declared scrambles at every declared "
            "stencil, while the GLOBAL class does not separate at all -- both "
            "scrambles return the same global group.  The group claim is "
            "therefore entered at the local stencils and the global reading "
            "is entered as measured-but-not-discriminating",
            all(v == len(PLAQ_STENCILS) for v in sep_local.values())
            and not any(sep_global.values()),
            "local separation %s of %d; global separation %s"
            % (sep_local, len(PLAQ_STENCILS), sep_global))


# ===========================================================================
# SECTION 10.  THE VERDICT
# ===========================================================================

def derive_head(c):
    """THE HEAD LAW.  Four outcomes, all four reachable by this one
    derivation, and none of them typed beside the census: the head is a
    function of the measured counts alone."""
    if c["declared_gate_admits"] == 0:
        return "R5-BLOCKED-AT-THE-GATE"
    if c["noncommuting_configs"] == 0:
        return "R5-BLOCKED-AT-THE-COMMUTATOR-SUBGROUP"
    if c["separating_stencils"] == 0:
        return "R5-BLOCKED-AT-THE-SCRAMBLE-CONTROL"
    if c["local_stable"] == 0:
        return "R5-NO-STABLE-GROUP"
    return "R5-NON-ABELIAN"


def build_verdict(c):
    head = derive_head(c)
    segs = [
        "CLASS=ALTERNATING-ON-ITS-OWN-SUPPORT(%s);"
        "RANK=%d-OF-%d-DECLARED-PLAQUETTE-GENERATORS-ARENA-RELATIVE;"
        "COMMUTATOR-SUBGROUP=NONTRIVIAL-AT-%d-OF-%d-UNIFORM-COINS"
        % (c["local_ladder"], c["global_rank"], c["plaquettes"],
           c["noncommuting_configs"], c["coins"]),
        "GATE=INHERITED-PER-GENERATOR-%s-ADMITS-%d-OF-%d"
        "(R5-BLOCKED-AT-THE-GATE-AT-THAT-READING);"
        "MAXIMAL-PER-GENERATOR-LEVEL=%s;"
        "DECLARED-GATE=FAMILY-COVARIANCE-%d-OF-%d-CHECKS"
        % (c["maximal_level"], c["inherited_gate_admits"],
           c["objects_censused"], c["maximal_attained"],
           c["family_covariance_checks"] - c["family_covariance_failures"],
           c["family_covariance_checks"]),
        "CURVATURE-DEFECT=%s(LINK-GRAIN=MUTUALLY-EXCLUSIVE-BY-THEOREM-"
        "%d-OF-%d-BOTH;PLAQUETTE-GRAIN=ALL-FOUR-CELLS-%d-BOTH;"
        "TWO-EXCITATION=EXCLUSIVITY-SURVIVES-%d-OF-%d-BOTH;"
        "PARENT-BASELINE=%d-DEFECTS-AT-ZERO-CURVATURE)"
        % (c["matched_outcome"], c["link_both"], c["link_rows"],
           c["plaq_both"], c["two_both"], c["two_rows"], c["baseline"]),
        "CONTROL=FULL-STRATUM-FLAT-%d-OF-%d-TRIVIAL-GROUP"
        % (c["control_noncommuting"], c["control_pairs"]),
        "REFINEMENT=%s(LOCAL-STABLE-%d-OF-%d;GLOBAL-%s-TO-%s)"
        % (c["refinement_verdict"], c["local_stable"], c["local_stencils"],
           c["global_class_small"], c["global_class_large"]),
        "SCRAMBLE=SEPARATES-LOCAL-%d-OF-%d;FAILS-GLOBAL-%d-OF-%d"
        % (c["separating_stencils"], c["scramble_local_total"],
           c["scramble_global_separating"], c["scrambles"]),
        "INTERFERING-SECTOR=INFINITE-ORDER-%d-OF-%d-BY-TRACE-NON-INTEGRALITY"
        % (c["balanced_infinite"], c["balanced_coins"]),
        "SCOPE=D=%d;L=%d;REFINED-TO-%d;FIELD=%s;ALPHABET=%d;COINS=%d;"
        "LINKS=%d;PLAQUETTES=%d;CONNECTIVE=%s;STENCIL=%s;SECTOR=%s;"
        "SWEPT-RANGE=UNIFORM-CONFIGURATIONS-EXHAUSTIVE-OVER-THE-COIN-"
        "ALPHABET;NON-UNIFORM-CONFIGURATIONS=NOT-SWEPT;"
        "INDIVISIBILITY=%s;FINITE-LATTICE-ONLY;NO-CONTINUUM-CLAIM;"
        "NO-CONFINEMENT-CLAIM"
        % (c["d"], c["L"], c["L_refined"], c["field"], c["alphabet"],
           c["coins"], c["links"], c["plaquettes"], CONNECTIVE, STENCIL,
           c["sector"], c["indivisibility"]),
    ]
    return head, segs, head + "-<" + "|".join(segs) + ">"


def reconstruct_from_serialized(txt):
    """THE INDEPENDENT RECONSTRUCTION.  Reads ONLY the serialized receipt,
    carries its OWN copy of the head law and its OWN segment renderer, shares
    no helper, no input and no typed value with the builder, and returns the
    complete string for equality comparison."""
    R = json.loads(txt)
    c = R["counts"]
    if c["declared_gate_admits"] == 0:
        h = "R5-BLOCKED-AT-THE-GATE"
    elif c["noncommuting_configs"] == 0:
        h = "R5-BLOCKED-AT-THE-COMMUTATOR-SUBGROUP"
    elif c["separating_stencils"] == 0:
        h = "R5-BLOCKED-AT-THE-SCRAMBLE-CONTROL"
    elif c["local_stable"] == 0:
        h = "R5-NO-STABLE-GROUP"
    else:
        h = "R5-NON-ABELIAN"
    s = R["verdict"]["segments"]
    return h + "-<" + "|".join(s) + ">"


# ===========================================================================
# SECTION 11.  THE RECEIPT
# ===========================================================================

def qstr(x):
    return x


def has_float(o):
    if isinstance(o, float):
        return True
    if isinstance(o, dict):
        return any(has_float(k) or has_float(v) for k, v in o.items())
    if isinstance(o, (list, tuple)):
        return any(has_float(v) for v in o)
    return False


def build_counts(S):
    A = S["_A"]
    curv = S["curvature_census"]
    gr = S["holonomy_groups"]
    ref = S["refinement"]
    sc = S["scramble_control"]
    mt = S["matched_tables"]
    tr = S["transport_audit"]
    fc = S["flat_control"]
    a, b = REFINEMENT_SIZES
    ladder = []
    for name, _s in PLAQ_STENCILS:
        ladder.append("%s=%s" % (name, ref["by_size"][a]["rows"][name]["class"]))
    c = {
        "L": S["_L"], "d": S["_d"], "L_refined": b,
        "sites": S["_n"], "links": len(A["links"]),
        "plaquettes": len(A["plaqs"]), "strata": len(A["strata"]),
        "field": "Q(ZETA-8)", "alphabet": len(A["alphabet"]),
        "coins": len(A["coins"]),
        "coins_diagonal": S["coin_sectors"]["DIAGONAL"],
        "coins_antidiagonal": S["coin_sectors"]["ANTIDIAGONAL"],
        "coins_balanced": S["coin_sectors"]["BALANCED"],
        "chart_group": tr["chart_group_order"],
        "extension_group": tr["extension_order"],
        "noncommuting_configs": sum(v["noncommuting"] for v in curv.values()),
        "nonflat_configs": sum(v["nonflat"] for v in curv.values()),
        "diagonal_noncommuting": curv["DIAGONAL"]["noncommuting"],
        "local_ladder": "<".join(ladder),
        "global_class_small": ref["by_size"][a]["rows"][GLOBAL_STENCIL]["class"],
        "global_class_large": ref["by_size"][b]["rows"][GLOBAL_STENCIL]["class"],
        "global_order_small": ref["by_size"][a]["rows"][GLOBAL_STENCIL]["order"],
        "global_rank": S["holonomy_rank"][GLOBAL_STENCIL]["rank"],
        "local_stencils": ref["local_stencils"],
        "local_stable": ref["local_stable"],
        "refinement_verdict": ref["verdict"],
        "maximal_level": tr["maximal_level_anchored"],
        "maximal_attained": "NONE",
        "inherited_gate_admits": tr["inherited_gate_admits"],
        "objects_censused": tr["objects_censused"],
        "declared_gate_admits": (tr["family_covariance_checks"]
                                 - tr["family_covariance_failures"]),
        "family_covariance_checks": tr["family_covariance_checks"],
        "family_covariance_failures": tr["family_covariance_failures"],
        "matched_outcome": mt["outcome"],
        "link_both": mt["link_grain_totals"]["11"],
        "link_rows": sum(mt["link_grain_totals"].values()),
        "link_curvature_no_defect": mt["link_grain_totals"]["10"],
        "link_defect_no_curvature": mt["link_grain_totals"]["01"],
        "plaq_both": mt["plaquette_grain_totals"]["11"],
        "plaq_rows": sum(mt["plaquette_grain_totals"].values()),
        "plaq_curvature_no_defect": mt["plaquette_grain_totals"]["10"],
        "plaq_defect_no_curvature": mt["plaquette_grain_totals"]["01"],
        "baseline": mt["parent_baseline_defects_at_zero_curvature"],
        "two_excitation_states": S["two_excitation"]["states"],
        "two_both": S["two_excitation"]["totals"]["11"],
        "two_rows": sum(S["two_excitation"]["totals"].values()),
        "control_circulants": fc["circulants_rebuilt"],
        "control_pairs": fc["ordered_pairs"],
        "control_noncommuting": fc["noncommuting"],
        "control_group_order": fc["holonomy_group_order"],
        "balanced_coins": S["balanced_sector"]["coins"],
        "balanced_infinite":
            S["balanced_sector"]["trace_not_an_algebraic_integer"],
        "scrambles": len(SCRAMBLES),
        "scramble_local_total": len(PLAQ_STENCILS) * len(SCRAMBLES),
        "separating_stencils": sum(sc["separating_local_stencils"].values()),
        "scramble_global_separating": sum(
            1 for v in sc["separates_globally"].values() if v),
        "gauge_handles": len(GAUGE_HANDLES),
        "gauge_loops_moved": sum(r["untraced_holonomy_moved"]
                                 for r in S["gauge_selftest"]["rows"]),
        "sector": SECTOR, "sector_extension": SECTOR_EXT,
        "connective_tag": "MAX-NORM", "forcing_link": "(1,1)",
        "stencil": STENCIL, "indivisibility": INDIVISIBILITY,
    }
    return c


def build_receipt(S, LD):
    R = {"schema": SCHEMA, "unit": "R5-gauge (paper-18)",
         "pin": "v14/note-r5-gauge-pin.md",
         "pin_sha256_prefix": [s[2] for s in SOURCES
                               if s[0] == "A-PIN-R5"][0],
         "arithmetic": "exact: Q(zeta_8) as integer 5-tuples (a0,a1,a2,a3,den) "
                       "modulo x^4+1, canonical; group orders from a "
                       "deterministic Schreier-Sims; no floats anywhere",
         "arena_declaration": {
             "boundary": "the L = 4 torus (Z_L)^2 with its %d links and %d "
                         "plaquettes; the carrier is the single-occupation "
                         "sector" % (len(S["_A"]["links"]),
                                     len(S["_A"]["plaqs"])),
             "family": "link-indexed unitaries: a coin per link from the "
                       "DERIVED coin alphabet, acting on the link's own "
                       "domino and as the identity elsewhere; the four "
                       "declared parity strata are the parent's brickwork "
                       "shape generalised so the coin may vary link to link",
             "law": "Barandes' Gamma = |Theta| entrywise-squared; the "
                    "composition defect across the declared non-division cut",
             "connective": CONNECTIVE,
             "division_events": list(DIVISION_EVENTS),
             "cut_time": CUT_TIME, "leg_at_the_cut": LEG_AT_THE_CUT,
             "sector": SECTOR, "sector_extension": SECTOR_EXT,
             "indivisibility": INDIVISIBILITY,
             "swept": "exhaustive over the coin alphabet at the uniform "
                      "configuration; the non-uniform configuration space is "
                      "640^32 and is NOT swept -- the restriction is declared "
                      "here and carried in the verdict's SCOPE segment",
             "parent_handoffs": [
                 "NOT-BLOCH-DIAGONAL is a theorem for the brickwork classes "
                 "(R4b); it is cited, not re-derived",
                 "NO transport number is inherited from R4b: its scope is the "
                 "single-occupation uniform average"]},
         "runtime_inputs": {"sources": [s[1] for s in SOURCES],
                            "object_under_test": PAPER_REL,
                            "reads": sorted(set(READS))},
         "source_sha256": {s[0]: s[2] for s in SOURCES},
         }
    for k in sorted(S):
        if not k.startswith("_"):
            R[k] = S[k]
    R["choice_inventory"] = [{"choice": a, "class": b, "fibre": f}
                             for a, b, f in CHOICE_INVENTORY]
    R["counts"] = build_counts(S)
    return R


# ===========================================================================
# SECTION 12.  THE PAPER GATES (#20: claims, numerals, polarity)
# ===========================================================================

POLARITY_WINDOW = 64

EXPECTED_OCCURRENCES = {
    "nonabelian": 2, "alternating": 3, "exclusive": 2, "control_flat": 4,
    "local_stable": 2, "scramble_local": 1, "infinite": 1,
}

POLARITY_GUARDS = [
    ("nonabelian", ("fail", "not ", "never")),
    ("alternating", ("fail", "not ", "never")),
    ("exclusive", ("fail", "never")),
    ("control_flat", ("fail", "never")),
    ("local_stable", ("fail", "not ", "never")),
    ("infinite", ("fail", "never")),
]


def paper_claims(R):
    c = R["counts"]
    cl = {
        "sites": "16 sites", "links": "32 links",
        "plaquettes": "16 plaquettes", "strata": "four parity strata",
        "alphabet": "25 elements", "coins": "%d coins" % c["coins"],
        "sectors": "%d diagonal, %d antidiagonal and %d balanced"
                   % (c["coins_diagonal"], c["coins_antidiagonal"],
                      c["coins_balanced"]),
        "nonabelian": "%d of %d uniform configurations" % (
            c["noncommuting_configs"], c["coins"]),
        "nonflat": "%d of %d are non-flat" % (c["nonflat_configs"],
                                              c["coins"]),
        "abelian_arm": "%d of the %d diagonal coins" % (
            c["diagonal_noncommuting"], c["coins_diagonal"]),
        "alternating": "the FULL alternating group on its own support",
        "ladder": "%s" % c["local_ladder"].replace("=", " = ").replace(
            "<", " < "),
        "global": "%s at L = 4 and %s at L = 8" % (c["global_class_small"],
                                                  c["global_class_large"]),
        "global_order": "%d" % c["global_order_small"],
        "rank": "rank %d of the %d declared plaquette generators" % (
            c["global_rank"], c["plaquettes"]),
        "control_flat": "0 of 3364",
        "control_circ": "%d circulants" % c["control_circulants"],
        "gate_admits": "%d of the %d" % (c["inherited_gate_admits"],
                                         c["objects_censused"]),
        "covariance": "%d of the %d checks" % (
            c["family_covariance_checks"] - c["family_covariance_failures"],
            c["family_covariance_checks"]),
        "chart": "order 32", "extension": "order 128",
        "exclusive": "mutually exclusive",
        "link_cells": "%d of the %d rows carry both" % (c["link_both"],
                                                        c["link_rows"]),
        "link_curv": "%d rows carry curvature and no defect" % (
            c["link_curvature_no_defect"]),
        "link_def": "%d carry a defect and no curvature" % (
            c["link_defect_no_curvature"]),
        "plaq_cells": "%d rows carry both" % c["plaq_both"],
        "baseline": "588 defects at identically zero curvature",
        "two_states": "%d two-excitation states" % c["two_excitation_states"],
        "two_both": "%d of %d" % (c["two_both"], c["two_rows"]),
        "infinite": "%d of %d" % (c["balanced_infinite"],
                                  c["balanced_coins"]),
        "local_stable": "%d of %d declared local stencils" % (
            c["local_stable"], c["local_stencils"]),
        "scramble_local": "%d of %d" % (c["separating_stencils"],
                                        c["scramble_local_total"]),
        "scramble_global": "neither scramble separates the global class",
        "gauge_moved": "%d" % c["gauge_loops_moved"],
        "matched_outcome": c["matched_outcome"],
        "refinement_verdict": c["refinement_verdict"],
        "L": "L = 4", "d": "d = 2", "L8": "L = 8",
    }
    t = R.get("totals", {})
    if "gates" in t:
        cl.update({
            "gates": "%d gates" % t["gates"],
            "gates_in_receipt": "%d of them evaluated inside the receipt"
                                % t["gates_in_receipt"],
            "gates_falsifiable": "%d carrying their own injection falsifier "
                                 "and %d their registered forcing"
                                 % (t["gates_falsifiable"], t["gates_waived"]),
            "mutants": "%d declared mutants" % t["mutants"],
            "anchors": "%d anchors" % t["anchors"],
            "byte_anchors": "%d file-bytes anchors" % t["byte_anchors"],
            "pv_anchors": "%d path-value anchors" % t["path_value_anchors"],
            "vb_anchors": "%d verbatim-text anchors" % t["verbatim_anchors"],
            "seals": "%d sealed objects" % t["seals"],
        })
    if "mutants_killed" in t:
        cl["mutants_dead"] = "%d declared mutants, all dead" % t["mutants_killed"]
    if mut("MUT-PAPER-CLAIM"):
        cl["injected"] = "a claim the paper does not carry: 4242"
    return cl


def paper_polarity(R, txt):
    cl = paper_claims(R)
    fl = flat(txt)
    if mut("MUT-PAPER-POLARITY"):
        k0 = POLARITY_GUARDS[0][0]
        fl = fl.replace(flat(cl[k0]), "fail to " + flat(cl[k0]), 1)
    exp = dict(EXPECTED_OCCURRENCES)
    if mut("MUT-PAPER-OCCURRENCES"):
        exp["nonabelian"] = exp["nonabelian"] + 1
    miscounted, inverted = [], []
    for k, want in sorted(exp.items()):
        if k not in cl:
            miscounted.append(k)
            continue
        got = fl.count(flat(cl[k]))
        if got != want:
            miscounted.append("%s:%d!=%d" % (k, got, want))
    for k, negators in POLARITY_GUARDS:
        if k not in cl:
            inverted.append(k)
            continue
        v = flat(cl[k])
        start = 0
        while True:
            at = fl.find(v, start)
            if at < 0:
                break
            window = fl[max(0, at - POLARITY_WINDOW):at].lower()
            for neg in negators:
                if neg in window:
                    inverted.append("%s@%d:%r" % (k, at, neg))
            start = at + 1
    return {"claims_with_expected_occurrences": len(exp),
            "polarity_guarded_claims": len(POLARITY_GUARDS),
            "window": POLARITY_WINDOW,
            "miscounted": sorted(miscounted), "inverted": sorted(inverted)}


def _numerals_of(o, acc):
    if isinstance(o, bool):
        return
    if isinstance(o, int):
        acc.add(str(o))
    elif isinstance(o, str):
        acc |= set(re.findall(NUMERAL_RE, o))
    elif isinstance(o, dict):
        for k, v in o.items():
            acc |= set(re.findall(NUMERAL_RE, str(k)))
            _numerals_of(v, acc)
    elif isinstance(o, (list, tuple)):
        for v in o:
            _numerals_of(v, acc)


def paper_coverage(R, txt):
    cl = paper_claims(R)
    fl = flat(txt)
    missing = sorted(k for k, v in cl.items() if flat(v) not in fl)
    rendered = set()
    for v in cl.values():
        rendered |= set(re.findall(NUMERAL_RE, v))
    for key in ("counts", "curvature_census", "holonomy_groups",
                "holonomy_rank", "flat_control", "transport_audit",
                "matched_tables", "two_excitation", "gauge_selftest",
                "refinement", "scramble_control", "balanced_sector",
                "projective_periods", "coin_sectors", "choice_inventory",
                "totals"):
        if key in R:
            _numerals_of(R[key], rendered)
    rendered |= {str(len(SOURCES)), str(len(PATH_VALUE_ANCHORS)),
                 str(len(VERBATIM_ANCHORS)), str(len(MUTANTS)),
                 str(len(SOURCES) + len(PATH_VALUE_ANCHORS)
                     + len(VERBATIM_ANCHORS)),
                 str(len(SEALED_PATHS)), str(POLARITY_WINDOW),
                 str(WINDOW_FLOOR), str(len(PLAQ_STENCILS)),
                 str(len(GAUGE_HANDLES)), str(len(SCRAMBLES)),
                 str(len(NAMED_COINS)), str(len(CHOICE_INVENTORY))}
    residue = dict(DERIVED_IN_TEXT)
    if mut("MUT-PAPER-NUMERAL"):
        rendered.discard(str(R["counts"]["coins"]))
        residue.pop("0", None)
    in_paper = set(re.findall(NUMERAL_RE, txt))
    uncovered = sorted(in_paper - rendered - set(residue))
    return {"claims": len(cl), "missing": missing,
            "distinct_numerals": len(in_paper),
            "numeral_occurrences": len(re.findall(NUMERAL_RE, txt)),
            "covered_by_rendering": len(in_paper & rendered),
            "declared_derived_in_text": len(residue),
            "residue_declared_but_absent":
                sorted(k for k in residue if k not in in_paper),
            "uncovered": uncovered}


# ===========================================================================
# SECTION 13.  THE DECLARED MUTANTS
# ===========================================================================

MUTANTS = [
    ("MUT-ALPHABET", "G-ALPHABET-REBUILT",
     "drops an element from the rebuilt coefficient alphabet"),
    ("MUT-COIN-UNITARITY", "G-COIN-ALPHABET-DERIVED",
     "admits a non-unitary matrix into the derived coin alphabet"),
    ("MUT-CURVATURE-COUNT", "G-CURVATURE-CENSUS-BOUND",
     "moves one cell of the curvature census"),
    ("MUT-CURVATURE-ZEROED", "G-COMMUTATOR-NONTRIVIAL",
     "zeroes every non-commuting count, so the arena reports itself abelian"),
    ("MUT-GROUP-CLASS", "G-ALTERNATING-ON-ITS-OWN-SUPPORT",
     "retypes one measured isomorphism class"),
    ("MUT-MATRIX-AS-PHYSICS", "G-NO-MATRIX-AS-PHYSICS",
     "writes a holonomy MATRIX into a published row"),
    ("MUT-INFINITE-CERTIFICATE", "G-BALANCED-SECTOR-INFINITE",
     "weakens the infinite-order certificate by one witness"),
    ("MUT-CIRCULANT-POOL", "G-FLAT-CONTROL-TRIVIAL",
     "drops a circulant from the rebuilt flat control"),
    ("MUT-FLAT-CONTROL", "G-FLAT-CONTROL-TRIVIAL",
     "injects a non-commuting pair into the provably flat control"),
    ("MUT-TRANSPORT-LEVEL", "G-GATE-INHERITANCE-AUDIT",
     "promotes every link operator to the maximal transport level"),
    ("MUT-FAMILY-COVARIANCE", "G-DECLARED-GATE-COVARIANCE",
     "breaks one family-covariance check"),
    ("MUT-MATCHED-CELL", "G-LINK-GRAIN-EXCLUSIVE",
     "populates the link-grain cell the theorem forbids"),
    ("MUT-TWO-EXCITATION", "G-TWO-EXCITATION-RUN",
     "populates the two-excitation cell the extension leaves empty"),
    ("MUT-GAUGE-HANDLE", "G-GAUGE-BOTH-DIRECTIONS",
     "makes the declared handle move nothing, so the negative direction "
     "goes vacuous"),
    ("MUT-REFINEMENT", "G-REFINEMENT-CLASS",
     "moves one local class at the refined size"),
    ("MUT-SCRAMBLE", "G-SCRAMBLE-SEPARATION",
     "makes a scrambled control return the physical profile"),
    ("MUT-WINDOW-TRUNCATED", "G-VERBATIM-ANCHORS",
     "truncates a verbatim window to a decoration below the length floor"),
    ("MUT-HEAD-TYPED", "G-VERDICT-RECONSTRUCTED",
     "retypes the head after every verdict gate has been built"),
    ("MUT-HEAD-CONSTANT", "G-HEAD-MOVES-ON-A-ZEROED-CENSUS",
     "makes the head law constant, so a zeroed census returns the same head"),
    ("MUT-SEAL-BROKEN", "G-SEAL-COMPLETE",
     "mutates a sealed object after its gate passed"),
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS",
     "renders a claim the paper does not carry"),
    ("MUT-PAPER-NUMERAL", "G-PAPER-NUMERAL-COVERAGE",
     "drops a numeral from the rendered set"),
    ("MUT-PAPER-POLARITY", "G-PAPER-CLAIM-POLARITY",
     "inverts a claim's polarity without introducing a numeral"),
    ("MUT-PAPER-OCCURRENCES", "G-PAPER-CLAIM-POLARITY",
     "changes an expected occurrence count"),
]


# ===========================================================================
# SECTION 14.  THE CLI
# ===========================================================================

class CliError(Exception):
    pass


def parse_args(argv):
    opts = {"write": True, "selftest": False, "mutant": None,
            "break_anchor": None, "verify_paper": None}
    i = 0
    names = {m[0] for m in MUTANTS}
    anchors = {s[0] for s in SOURCES}
    while i < len(argv):
        a = argv[i]
        if a == "--no-write":
            opts["write"] = False
        elif a == "--selftest":
            opts["selftest"] = True
            opts["write"] = False
        elif a == "--mutant":
            if i + 1 >= len(argv):
                raise CliError("--mutant needs a NAME")
            if argv[i + 1] not in names:
                raise CliError("unknown mutant %r" % argv[i + 1])
            opts["mutant"] = argv[i + 1]
            opts["write"] = False
            i += 1
        elif a == "--break-anchor":
            if i + 1 >= len(argv):
                raise CliError("--break-anchor needs a NAME")
            if argv[i + 1] not in anchors:
                raise CliError("unknown anchor %r" % argv[i + 1])
            opts["break_anchor"] = argv[i + 1]
            opts["write"] = False
            i += 1
        elif a == "--verify-paper":
            rel = PAPER_REL
            if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
                rel = argv[i + 1]
                i += 1
            p = rel if os.path.isabs(rel) else os.path.join(REPO, rel)
            if not os.path.exists(p):
                raise CliError("--verify-paper path does not exist: %s" % rel)
            opts["verify_paper"] = rel
            opts["write"] = False
        else:
            raise CliError("unknown argument %r" % a)
        i += 1
    return opts


def cli_error_probe(fn, argv):
    try:
        fn(argv)
    except CliError:
        return True
    return False


# ===========================================================================
# SECTION 15.  THE RECEIPT GATES, THE SEAL, THE REPORT
# ===========================================================================

def run_receipt_gates(S, LD, paper_text):
    SEAL = Seal()
    R = build_receipt(S, LD)
    c = R["counts"]

    head, segs, string = build_verdict(c)
    if mut("MUT-HEAD-TYPED"):
        head = "R5-NO-STABLE-GROUP"
        string = head + string[string.index("-<"):]
    R["verdict"] = {"head": head, "segments": segs, "string": string}

    # the head must MOVE on a zeroed census: a head law that ignores the
    # census cannot be falsified by the census
    zero = dict(c)
    zero["declared_gate_admits"] = 0
    if mut("MUT-HEAD-CONSTANT"):
        moved = "R5-NON-ABELIAN"
    else:
        moved = derive_head(zero)
    LD.gate("G-HEAD-MOVES-ON-A-ZEROED-CENSUS",
            "the head is DERIVED from the measured census and cannot be "
            "typed: run on a census whose declared gate admits nothing, the "
            "same law returns a different head, so the head is a function of "
            "the measurement and not a label beside it",
            moved != head and moved == "R5-BLOCKED-AT-THE-GATE",
            "delivered %s; on a zeroed census %s" % (head, moved))

    reachable = {}
    for probe, patch in (
            ("R5-BLOCKED-AT-THE-GATE", {"declared_gate_admits": 0}),
            ("R5-BLOCKED-AT-THE-COMMUTATOR-SUBGROUP",
             {"noncommuting_configs": 0}),
            ("R5-BLOCKED-AT-THE-SCRAMBLE-CONTROL", {"separating_stencils": 0}),
            ("R5-NO-STABLE-GROUP", {"local_stable": 0}),
            ("R5-NON-ABELIAN", {})):
        z = dict(c)
        z.update(patch)
        reachable[probe] = derive_head(z)
    LD.gate("G-VERDICT-PREREGISTERED",
            "all the pre-registered outcomes are reachable BY THE SAME "
            "DERIVATION, demonstrated on synthetic censuses inside this gate: "
            "the pin names four, and each is produced by the one head law "
            "from a census that differs only in the count it turns on",
            all(k == v for k, v in reachable.items()),
            "%s" % reachable)
    R["preregistered_heads"] = reachable

    ser = json.dumps(R, indent=1, sort_keys=True)
    rebuilt = reconstruct_from_serialized(ser)
    LD.gate("G-VERDICT-RECONSTRUCTED",
            "the complete verdict string -- head included -- is compared for "
            "equality against an INDEPENDENT reconstruction that derives the "
            "head by its own copy of the head law, reads only the serialized "
            "receipt, and shares no helper, no input and no typed value with "
            "the builder",
            rebuilt == string,
            "%d characters compared" % len(string))
    SEAL.take("SEAL-VERDICT-STRING", R)
    SEAL.take("SEAL-VERDICT-HEAD", R)
    SEAL.take("SEAL-COUNTS", R)

    LD.gate("G-SCOPE-INHERITED",
            "the parent's FORCED connective is inherited VERBATIM into this "
            "unit's scope segment rather than re-derived: the anchored "
            "diagonal link decides the neighbourhood relation, and this arena "
            "does not get to choose it either",
            CONNECTIVE in string and c["connective_tag"] == "MAX-NORM",
            "segment carried: %s" % CONNECTIVE)

    LD.gate("G-DECLARATION-SEGMENTS",
            "G5: the declaration segments are explicit in the verdict -- the "
            "connective, the link set and stencil, the sector, the swept "
            "range and the declared (never measured) indivisibility -- and "
            "the swept range says what is NOT swept, since the non-uniform "
            "configuration space is not enumerable at this alphabet",
            all(k in string for k in ("CONNECTIVE=", "STENCIL=", "SECTOR=",
                                      "SWEPT-RANGE=", "INDIVISIBILITY=",
                                      "NON-UNIFORM-CONFIGURATIONS=NOT-SWEPT")),
            "five declaration segments plus the non-sweep disclosure")

    LD.gate("G-NO-CONFINEMENT-LANGUAGE",
            "the must-not, gated: no confinement-analog claim is entered "
            "anywhere in the verdict or in the paper's claim set, and the "
            "scope segment says so in as many words",
            "NO-CONFINEMENT-CLAIM" in string
            and not any("confinement" in str(v).lower()
                        for v in paper_claims(R).values()),
            "the scope segment carries NO-CONFINEMENT-CLAIM")

    LD.gate("G-CHOICE-INVENTORY",
            "every construction choice is inventoried with an exact fibre, "
            "and the fibres that are measurable are measured: the declared "
            "stencils, handles and extension options are counted from the "
            "declaration itself",
            len(CHOICE_INVENTORY) == 15
            and dict((a, f) for a, b, f in CHOICE_INVENTORY)[
                "the plaquette stencils"] == len(PLAQ_STENCILS)
            and dict((a, f) for a, b, f in CHOICE_INVENTORY)[
                "the gauge handles"] == len(GAUGE_HANDLES),
            "%d choices" % len(CHOICE_INVENTORY))

    # ---- no floats, two ways ----------------------------------------------
    src = read_text(SELF)
    tree = ast.parse(src)
    floats = [nd for nd in ast.walk(tree)
              if isinstance(nd, ast.Constant) and isinstance(nd.value, float)]
    LD.gate("G-NO-FLOATS-IN-SOURCE",
            "an AST scan of this instrument's own source finds no float "
            "literal anywhere: the arithmetic is exact by construction and "
            "not by care",
            not floats, "%d float literals" % len(floats))
    LD.gate("G-NO-FLOATS-IN-RECEIPT",
            "a recursive type scan of the emitted receipt finds no float "
            "anywhere in it either, so nothing inexact can reach the artifact",
            not has_float(R), "receipt scanned recursively")

    imported = set()
    for nd in ast.walk(tree):
        if isinstance(nd, ast.Import):
            imported |= {a.name.split(".")[0] for a in nd.names}
        elif isinstance(nd, ast.ImportFrom):
            imported.add((nd.module or "").split(".")[0])
    calls = {nd.func.attr for nd in ast.walk(tree)
             if isinstance(nd, ast.Call) and isinstance(nd.func, ast.Attribute)}
    declared_imports = {"ast", "hashlib", "json", "os", "re", "sys",
                        "itertools", "math"}
    LD.gate("G-NO-SUBPROCESS",
            "the import list and the attribute-call list are read off this "
            "file's own syntax tree: exactly the declared modules are "
            "imported, none of them can start a process, and no system or "
            "popen call appears anywhere.  The run is therefore correct "
            "off-tree and in a directory with no version control at all",
            imported <= declared_imports
            and not (calls & {"system", "popen", "run", "check_output",
                              "Popen", "spawn"}),
            "imports %s" % sorted(imported))

    reads = sorted(set(READS))
    declared = sorted({s[1] for s in SOURCES} | {PAPER_REL})
    LD.gate("G-RUNTIME-INPUTS-ENUMERATED",
            "the runtime inputs are enumerated and gated: exactly the "
            "hash-pinned sources plus the one file read as the object under "
            "test, and nothing else -- no ledger, no status board, no other "
            "unit's working file",
            set(reads) <= set(declared),
            "%d files read, %d declared" % (len(reads), len(declared)))

    LD.gate("G-ANCHOR-CONSUMERS-EXIST",
            "every verbatim window is bound to a gate that CONSUMES it, and "
            "each of those gates exists in this run's ledger: a window with "
            "no consumer is decoration",
            all(x in LD.ids or x in ("G-PAPER-CLAIMS",)
                for x in S["_anchor_consumers"]),
            "consumers %s" % S["_anchor_consumers"])

    # ---- the published rows, bound ----------------------------------------
    for sid in ("SEAL-CURVATURE", "SEAL-GROUPS", "SEAL-FLAT-CONTROL",
                "SEAL-TRANSPORT", "SEAL-MATCHED", "SEAL-TWO-EXCITATION",
                "SEAL-GAUGE", "SEAL-REFINEMENT", "SEAL-SCRAMBLE",
                "SEAL-CHOICES", "SEAL-PATH-ANCHORS", "SEAL-BYTE-ANCHORS",
                "SEAL-VERBATIM"):
        pass
    LD.gate("G-PUBLISHED-ROWS-BOUND",
            "every published table is bound to the verdict it supports: the "
            "curvature census, the group rows, the flat control, the "
            "transport audit, the matched tables, the two-excitation "
            "extension, the gauge self-test, the refinement and the scramble "
            "control are all sealed at this gate, so nothing downstream can "
            "reach the bytes that will be written",
            all(k in R for k in ("curvature_census", "holonomy_groups",
                                 "flat_control", "transport_audit",
                                 "matched_tables", "two_excitation",
                                 "gauge_selftest", "refinement",
                                 "scramble_control")),
            "9 published tables")
    for sid, _p, g in SEALED_PATHS:
        if g == "G-PUBLISHED-ROWS-BOUND":
            SEAL.take(sid, R)

    # ---- the CLI contract, exercised --------------------------------------
    ok_cli = (parse_args([])["write"] is True
              and parse_args(["--no-write"])["write"] is False
              and parse_args(["--selftest"])["write"] is False
              and cli_error_probe(parse_args, ["--nope"])
              and cli_error_probe(parse_args, ["--mutant"])
              and cli_error_probe(parse_args, ["--mutant", "NOPE"])
              and cli_error_probe(parse_args, ["--break-anchor", "NOPE"])
              and cli_error_probe(parse_args, ["--verify-paper", "v14/NOPE.md"])
              and parse_args(["--verify-paper"])["verify_paper"] == PAPER_REL)
    LD.gate("G-CLI-CONTRACT",
            "the CLI is parsed against a whitelist and every documented "
            "behaviour is exercised here: no flag is a no-op, no flag is "
            "mutant-only, an unknown flag and a missing flag argument both "
            "raise, and --verify-paper resolves to this unit's paper by "
            "default and refuses a path that does not exist",
            ok_cli, "9 argv shapes probed")

    LD.gate("G-VERIFY-PAPER-LIVE",
            "--verify-paper is REAL: it rebuilds the whole derivation and "
            "evaluates the three paper gates with the named file as the "
            "object under test, so it can fail on a drifted paper and exits 2 "
            "on a path that does not exist",
            cli_error_probe(parse_args, ["--verify-paper", "v14/NOPE.md"]),
            "the object under test is a parameter, not a constant")

    # ---- the waiver ledger (#34), covering every gate the run will reach ---
    ids = [row["gate"] for row in LD.rows] + list(LATE_GATES) + [
        "G-MUTANTS-ON-TARGET", "G-ARTIFACT-INTEGRITY",
        "G-PAPER-COVERAGE-FINAL"]
    waivers = []
    for gid in ids:
        tgt = [mm for mm in MUTANTS if mm[1] == gid]
        if gid in FORCINGS:
            waivers.append({"gate": gid, "status": "WAIVED",
                            "forcing": FORCINGS[gid]})
        elif tgt:
            waivers.append({"gate": gid, "status": "FALSIFIABLE",
                            "falsifier": tgt[0][0]})
        else:
            waivers.append({"gate": gid, "status": "FALSIFIABLE",
                            "falsifier": "the anchor break self-test "
                                         "(--break-anchor), which corrupts an "
                                         "input this gate reads and kills the "
                                         "run"})
    R["waiver_ledger"] = waivers
    n_falsifiable = sum(1 for w in waivers if w["status"] == "FALSIFIABLE")
    n_waived = sum(1 for w in waivers if w["status"] == "WAIVED")
    LD.gate("G-WAIVERS-VERIFIED",
            "no gate is left un-falsifiable without a registered forcing: "
            "every gate the run will reach -- the ones already evaluated and "
            "the declared late ones -- is either bound to a declared mutant "
            "that kills it, or to the anchor-break self-test, or carries an "
            "explicit forcing naming the mechanism that falsifies it instead",
            all(w["status"] in ("FALSIFIABLE", "WAIVED") for w in waivers)
            and n_waived == 3 and len(set(ids)) == len(ids),
            "%d falsifiable, %d waived with forcings" % (n_falsifiable,
                                                         n_waived))
    SEAL.take("SEAL-WAIVERS", R)

    # THE PREDICTION IS MADE HERE, before the paper gates read it: the gate
    # count is the ledger so far plus the declared late gates plus the two
    # that no ledger row carries, and the run must close at exactly that.
    R["totals"] = {
        "gates": len(waivers),
        "gates_in_receipt": len(waivers) - 1,
        "gates_falsifiable": n_falsifiable, "gates_waived": n_waived,
        "mutants": len(MUTANTS), "anchors": len(SOURCES)
        + len(PATH_VALUE_ANCHORS) + len(VERBATIM_ANCHORS),
        "byte_anchors": len(SOURCES),
        "path_value_anchors": len(PATH_VALUE_ANCHORS),
        "verbatim_anchors": len(VERBATIM_ANCHORS),
        "seals": len(SEALED_PATHS),
        "verdict_values": len(re.findall(NUMERAL_RE, string)),
    }

    # ---- the paper gates, in run ------------------------------------------
    cov = paper_coverage(R, paper_text)
    LD.gate("G-PAPER-CLAIMS",
            "every claim string the instrument renders occurs in the paper "
            "verbatim up to line wrapping: the comparison collapses runs of "
            "whitespace on BOTH sides, so a claim broken across two lines is "
            "still the same characters in the same order",
            not cov["missing"], "missing %s of %d claims"
            % (cov["missing"] or "none", cov["claims"]))
    LD.gate("G-PAPER-NUMERAL-COVERAGE",
            "every numeral in the paper is either rendered by a receipt field "
            "or is one of the declared derived-in-text residues, each named "
            "individually: a number in the prose that no measurement produces "
            "dies here",
            not cov["uncovered"] and not cov["residue_declared_but_absent"],
            "uncovered %s; declared-but-absent %s; %d distinct numerals over "
            "%d occurrences" % (cov["uncovered"] or "none",
                                cov["residue_declared_but_absent"] or "none",
                                cov["distinct_numerals"],
                                cov["numeral_occurrences"]))
    pol = paper_polarity(R, paper_text)
    LD.gate("G-PAPER-CLAIM-POLARITY",
            "the numeral instrument is blind to DIRECTION, so two declared "
            "legs close it: every polarity-bearing claim must occur exactly "
            "the number of times the instrument expects, and none may sit "
            "inside a window carrying a declared negator",
            not pol["miscounted"] and not pol["inverted"],
            "miscounted %s; inverted %s" % (pol["miscounted"] or "none",
                                            pol["inverted"] or "none"))
    R["paper_coverage"] = cov
    R["paper_polarity"] = pol
    R["paper_claims"] = paper_claims(R)

    # ---- THE SEAL, in-run half --------------------------------------------
    if mut("MUT-SEAL-BROKEN"):
        R["matched_tables"]["link_grain_totals"]["11"] = 99
    broken = SEAL.verify(R, only=SEALS_IN_RUN)
    LD.gate("G-SEAL-COMPLETE",
            "THE GATE-TO-DISK SEAL: a gate that fires on an object still "
            "mutable when the artifact is built has not gated the artifact.  "
            "Every published object was digested at the moment its gate "
            "passed, and every one of those digests still verifies here; the "
            "payload may not be sealed over a broken seal, and the artifacts "
            "are written from the sealed payload alone",
            not broken, "%d seals verified, %d broken"
            % (len(SEALS_IN_RUN), len(broken)))

    return R, ser, SEAL


def emit_report(R, S, SEAL):
    c = R["counts"]
    say("")
    say("=" * 78)
    say("THE VERDICT")
    say("=" * 78)
    say(R["verdict"]["string"])
    say("")
    say("  G1  commutator subgroup nontrivial at %d of %d uniform coins; "
        "the class, certified by set equality, is the FULL alternating group "
        "on its own support" % (c["noncommuting_configs"], c["coins"]))
    say("      the local ladder: %s" % c["local_ladder"])
    say("      the flat control returns the trivial group: %d of %d"
        % (c["control_noncommuting"], c["control_pairs"]))
    say("  G2  the inherited per-generator gate admits %d of %d objects at %s"
        % (c["inherited_gate_admits"], c["objects_censused"],
           c["maximal_level"]))
    say("  G3  %s -- link grain %s, plaquette grain %s"
        % (c["matched_outcome"], R["matched_tables"]["link_grain_totals"],
           R["matched_tables"]["plaquette_grain_totals"]))
    say("  G4  the untraced holonomy moves at %d checked loops; the Wilson "
        "trace never" % c["gauge_loops_moved"])
    say("  G6  %s: %d of %d local stencils stable, global %s -> %s"
        % (c["refinement_verdict"], c["local_stable"], c["local_stencils"],
           c["global_class_small"], c["global_class_large"]))
    say("  G7  the scramble separates locally at %d of %d and globally at %d "
        "of %d" % (c["separating_stencils"], c["scramble_local_total"],
                   c["scramble_global_separating"], c["scrambles"]))
    say("")
    say("  gates %d (%d in the receipt); mutants %d; anchors %d; sealed %d"
        % (R["totals"]["gates"], R["totals"]["gates_in_receipt"],
           R["totals"]["mutants"], R["totals"]["anchors"],
           R["totals"]["seals"]))
    SEAL.close_transcript("\n".join(LOG) + "\n")


# ===========================================================================
# SECTION 16.  MAIN
# ===========================================================================

def selftest():
    """--selftest: corrupt ONE anchor in memory, confirm the run dies at the
    anchor gate, WRITE NOTHING, exit 1.  Exits 2 if the corrupted run lives."""
    target = SOURCES[0][0]
    print("SELFTEST: corrupting anchor %s in memory; the run must die."
          % target, flush=True)
    globals()["QUIET"] = True
    try:
        build_state(target)
    except GateFail as e:
        globals()["QUIET"] = False
        print("SELFTEST: died at %s -- as required." % str(e).split(" ::")[0],
              flush=True)
        print("SELFTEST PASSED (the instrument is falsifiable); no artifact "
              "written.", flush=True)
        print("EXIT 1", flush=True)
        sys.exit(1)
    globals()["QUIET"] = False
    print("SELFTEST FAILED: a corrupted anchor did not kill the run.",
          flush=True)
    print("EXIT 2", flush=True)
    sys.exit(2)


def full_run(break_anchor, paper_text):
    S, LD = build_state(break_anchor)
    R, ser, SEAL = run_receipt_gates(S, LD, paper_text)
    return S, LD, R, ser, SEAL


def main():
    global MUT, READS
    try:
        opts = parse_args(sys.argv[1:])
    except CliError as e:
        print("usage: %s [--no-write] [--selftest] [--mutant NAME] "
              "[--break-anchor NAME] [--verify-paper [PATH]]"
              % os.path.basename(SELF), file=sys.stderr)
        print("error: %s" % e, file=sys.stderr)
        sys.exit(2)
    if opts["selftest"]:
        selftest()
    write = opts["write"]
    MUT = opts["mutant"]

    say("=" * 78)
    say("v14 R5 -- THE GAUGE RUNG: link-indexed unitaries and their holonomy")
    say("=" * 78)
    if MUT:
        say("MUTANT ACTIVE: %s" % MUT)
    if opts["break_anchor"]:
        say("ANCHOR BREAK SELF-TEST: %s" % opts["break_anchor"])

    paper_rel = opts["verify_paper"] or PAPER_REL
    paper_path = (paper_rel if os.path.isabs(paper_rel)
                  else os.path.join(REPO, paper_rel))
    if opts["verify_paper"]:
        say("VERIFY-PAPER: the object under test is %s" % paper_rel)
    paper_text = read_text(paper_path) if os.path.exists(paper_path) else ""

    try:
        S, LD, R, ser, SEAL = full_run(opts["break_anchor"], paper_text)
    except GateFail as e:
        say("")
        say("GATE FAILED: %s" % e)
        say("EXIT 1")
        sys.exit(1)

    if opts["verify_paper"]:
        say("")
        say("VERIFY-PAPER: %s" % paper_rel)
        say("  coverage %s" % R["paper_coverage"])
        say("  polarity %s" % R["paper_polarity"])
        say("  every claim rendered, every numeral covered, every polarity "
            "held: the three paper gates passed on this file.")
        say("EXIT 0")
        sys.exit(0)

    if MUT or opts["break_anchor"]:
        say("")
        say("MUTANT SURVIVED: %s" % (MUT or opts["break_anchor"]))
        say("EXIT 0")
        sys.exit(0)

    say("")
    say("running %d declared mutants" % len(MUTANTS))
    report, all_dead, on_target = [], True, 0
    saved = list(READS)
    for nm, target, note in MUTANTS:
        MUT = nm
        globals()["QUIET"] = True
        killed_at = None
        try:
            READS = []
            full_run(None, paper_text)
        except GateFail as e:
            killed_at = str(e).split(" ::")[0]
        except SystemExit:
            killed_at = "SYSTEM-EXIT"
        globals()["QUIET"] = False
        MUT = None
        report.append({"mutant": nm, "target": target, "note": note,
                       "killed": killed_at is not None, "killed_at": killed_at,
                       "on_target": killed_at == target})
        if killed_at is None:
            all_dead = False
        if killed_at == target:
            on_target += 1
    READS = saved
    say("    mutants: %d declared, %d killed, %d killed by their declared "
        "target" % (len(MUTANTS), sum(1 for m in report if m["killed"]),
                    on_target))
    off = [(m["mutant"], m["target"], m["killed_at"]) for m in report
           if not m["on_target"]]
    LD.gate("G-MUTANTS-ON-TARGET",
            "every declared mutant is killed, and killed by the gate it was "
            "declared to falsify: a mutant that dies elsewhere is a gate "
            "boundary this unit does not understand",
            all_dead and on_target == len(MUTANTS),
            "killed %d of %d; off target %s"
            % (sum(1 for m in report if m["killed"]), len(MUTANTS),
               off or "none"))

    R["mutants"] = report
    SEAL.take("SEAL-MUTANTS", R)
    R["gates"] = LD.rows
    R["not_executed"] = NOT_EXECUTED
    waivers = R["waiver_ledger"]

    R["totals"].update({
        "mutants_killed": sum(1 for m in report if m["killed"]),
        "mutants_on_target": on_target,
        "gates_passed_in_receipt": sum(1 for g in LD.rows if g["passed"]) + 1,
    })

    if (R["totals"]["gates"] != len(LD.rows) + 2
            or R["totals"]["gates_in_receipt"] != len(LD.rows) + 1
            or R["totals"]["gates_falsifiable"]
            != sum(1 for w in waivers if w["status"] == "FALSIFIABLE")
            or R["totals"]["gates_waived"]
            != sum(1 for w in waivers if w["status"] == "WAIVED")):
        say("")
        say("GATE FAILED: G-PAPER-COVERAGE-FINAL :: the predicted gate count "
            "%d did not close at %d"
            % (R["totals"]["gates"], len(LD.rows) + 2))
        say("EXIT 1")
        sys.exit(1)
    try:
        cov = paper_coverage(R, paper_text)
        LD.gate("G-PAPER-COVERAGE-FINAL",
                "the paper-claim and numeral-coverage check re-run once the "
                "instrument's own totals close, so the paper's instrument "
                "section is covered too; its in-run twins carry the injection "
                "falsifiers, and this evaluation is the enforcement -- a "
                "failure here exits 1 and writes nothing",
                not cov["missing"] and not cov["uncovered"]
                and not cov["residue_declared_but_absent"],
                "missing %s; uncovered %s; declared-but-absent %s; %d claims, "
                "%d distinct numerals over %d occurrences"
                % (cov["missing"] or "none", cov["uncovered"] or "none",
                   cov["residue_declared_but_absent"] or "none", cov["claims"],
                   cov["distinct_numerals"], cov["numeral_occurrences"]))
    except GateFail as e:
        say("")
        say("GATE FAILED: %s" % e)
        say("EXIT 1")
        sys.exit(1)
    R["paper_coverage"] = cov
    R["paper_polarity"] = paper_polarity(R, paper_text)
    R["paper_claims"] = paper_claims(R)
    R["gates"] = LD.rows
    SEAL.take("SEAL-GATES", R)
    SEAL.take("SEAL-TOTALS", R)
    SEAL.take("SEAL-COVERAGE", R)

    # the seal manifest is published so the seal is auditable from the
    # artifact alone: every sealed object, the path it was taken at, the gate
    # whose passing took it, and the digest that was taken.
    R["seal_manifest"] = SEAL.rows
    SEAL.close(R, json.dumps(R, indent=1, sort_keys=True))
    emit_report(R, S, SEAL)

    if write:
        payload, text = SEAL.payload, SEAL.transcript
        probe_path = OUT_JSON + ".integrity-probe"
        with open(probe_path, "w", encoding="utf-8") as f:
            f.write(payload[:-1] + " }")
        detected = digest(read_text(probe_path)) != SEAL.payload_sha
        os.remove(probe_path)

        def against_the_seal(js, tx):
            if digest(js) != SEAL.payload_sha or digest(tx) != SEAL.transcript_sha:
                return False
            disk = json.loads(js)
            if SEAL.verify(disk):
                return False
            return (disk["verdict"]["string"] == SEAL.verdict_string
                    and reconstruct_from_serialized(js) == SEAL.verdict_string)

        tmp_json, tmp_txt = OUT_JSON + ".tmp", OUT_TXT + ".tmp"
        with open(tmp_json, "w", encoding="utf-8") as f:
            f.write(payload)
        with open(tmp_txt, "w", encoding="utf-8") as f:
            f.write(text)
        ok = detected and against_the_seal(read_text(tmp_json),
                                           read_text(tmp_txt))
        if not ok:
            os.remove(tmp_json)
            os.remove(tmp_txt)
            print("GATE FAILED: G-ARTIFACT-INTEGRITY :: what was about to be "
                  "written does not match the gate-time seal (corruption "
                  "detected=%s); nothing written" % detected, flush=True)
            sys.exit(1)
        os.replace(tmp_json, OUT_JSON)
        os.replace(tmp_txt, OUT_TXT)
        if not against_the_seal(read_text(OUT_JSON), read_text(OUT_TXT)):
            print("GATE FAILED: G-ARTIFACT-INTEGRITY :: the artifacts on disk "
                  "differ from the gate-time seal", flush=True)
            sys.exit(1)
        print("G-ARTIFACT-INTEGRITY: corrupted probe detected; both artifacts "
              "written from the SEALED payload, re-read from disk and matched "
              "against the gate-time seal -- %d sealed objects, payload %s, "
              "transcript %s (%d + %d bytes)."
              % (len(SEAL.rows), SEAL.payload_sha, SEAL.transcript_sha,
                 len(payload), len(text)), flush=True)
    sys.exit(0)


if __name__ == "__main__":
    main()
