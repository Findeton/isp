#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
v14 GDL -- THE GRAVITATIONAL-DECOHERENCE LAW.
Instrument for `v14/paper-25-gdl.md`.

QUESTION (pin `v14/note-gdl-pin.md`, sha256-12 fe9533371046, ledger #205).
The substrate identity -- ONE event is simultaneously a record, a decoherence
event and a metric increment -- makes a QUANTITATIVE relation between
decoherence and geometry growth POSSIBLE.  This unit measures whether the
relation EXISTS and whether it is FORCED, on paper-20's coupled machine
rebuilt here from the committed spec:

  STAGE 1  THE DECOHERENCE FUNCTIONALS.  Three, declared, fiber priced, all
           run: (a) the site-basis inverse participation of the Born menu
           (paper-20's own observable, inherited); (b) the off-diagonal
           coherence mass in the site basis; (c) the record-menu/Born-menu
           divergence.  None privileged.
  STAGE 2  THE METRIC-GROWTH FUNCTIONALS.  The division-event emission rate
           per step, per site and per branch, taken from the coupled
           machine's OWN emission law, together with the n-growth profile.
  STAGE 3  THE RELATION, EXACTLY.  Per step at the declared horizon and at
           three resolutions: is each decoherence functional an exact
           FUNCTION of a growth functional?  FITTED FORMS ARE BARRED.  The
           test is equality-gated -- D is a function of G exactly when every
           G-class carries one D-value -- and a partial relation is reported
           as partial WITH THE FAILURE SET CENSUSED.
  STAGE 4  FORCEDNESS.  The relation census across the COIN FIBER (+/- Grover
           and the four hidden S_3-covariant classes, the parent's own
           witnesses) and across the emission-reading fiber, plus THE FROZEN
           CONTROL as the it-can-differ arm: A RELATION THAT HOLDS IDENTICALLY
           ON THE FROZEN STAGE IS NOT A GRAVITATIONAL-DECOHERENCE RELATION,
           and that exclusion is a gate rather than a remark.
  STAGE 5  THE PREDICTION ROW, in substrate-native form -- counts and exact
           rationals only.  NO SI NUMBER AND NO EXPERIMENTAL-VALUE CLAIM
           APPEARS ANYWHERE, and the corpus's Diosi-Penrose arc is cited for
           SHAPE ONLY.  Both abstentions are gated by a falsifier.

WHAT THIS PROGRAM DOES
  SEC 1  PROVENANCE.  11 pinned sources, sha256-12 verified; #62 verbatim
         anchors bound to their consumer gates; every text gate
         whitespace-normalises, ASCII-folds and strips markdown prefixes.
  SEC 2  EXACT ARITHMETIC on Z[w], w^2 = -1-w, and the arena.
  SEC 3  THE COUPLED MACHINE, RE-IMPLEMENTED.  paper-20's committed driver is
         read as a SPEC and never imported, never subprocessed (#91); the walk,
         the emission law and the update semantics are rebuilt here and the
         rebuild is ANCHORED against the parent's committed receipt at
         equality, value by value.
  SEC 4  THE DECOHERENCE FUNCTIONALS.
  SEC 5  THE GROWTH FUNCTIONALS.
  SEC 6  THE RELATION -- exact functional dependence, equality-gated, with the
         failure set censused and the vacuity of every test declared.
  SEC 7  FORCEDNESS -- the coin fiber, the reading fiber, the frozen exclusion.
  SEC 8  THE BLINDNESS MECHANISM -- measured on declared foreign count fields.
  SEC 9  THE PREDICTION ROW.
  SEC 10 THE WALLS -- the four inherited, the Lorentzian and hexagonal
         resonances NAMED (carried from the parent, which measured a
         determinant reaching zero), and this unit's own SI/experimental wall.
  SEC 11 The verdict, derived a SECOND time by a comparator that types its own
         templates; the paper gates; the TOTAL seal; the artifacts.

CLI CONTRACT (the #82 minimum: argv parsed against a WHITELIST)
---------------------------------------------------------------
    python3.13 v14/code/gdl_exact.py
        THE DELIVERY RUN, and the ONLY writer.
    --no-write      the same run, writing nothing.
    --numbers       the census only; no paper gate, no sweep, nothing written.
    --selftest      corrupts one declared anchor IN MEMORY, confirms the run
                    is refused, writes nothing, exits 1 (2 if it survives).
    --mutant NAME   one declared falsifier, artifacts untouched.
    --break-anchor NAME     corrupts that source's expected digest.
    --verify-paper [PATH]   the paper gates against PATH.
    --list-gates / --list-mutants
    Any other argument, any unknown flag argument, any missing flag argument
    and any SECOND MODE FLAG exits 2.  Modes do not compose.

THE TOTAL GATE-TO-DISK SEAL.  Every published receipt key is either sealed at
the moment its gate passes or listed as DECLARED-UNSEALED with a forcing; the
artifacts are written from the sealed payload through `os.replace`; the
terminal integrity gate compares the BYTES ON DISK against the gate-time seal.
A run that fails any gate writes nothing.

ARITHMETIC.  Exact only: Python integers and `fractions.Fraction`, with the
walk's amplitudes carried as INTEGER PAIRS over Z[w] with a common power-of-3
denominator.  There are no floats anywhere -- an AST scan of this file and a
recursive type scan of the emitted receipt are gates.

RUNTIME INPUTS (#46/#91).  The declared SOURCES are read at run time by path
resolved from THIS FILE's own location, all hash-pinned by this unit's frozen
declaration; the run aborts loudly and cleanly if the repository is not
present.  Two further files are read and BOTH are gated as their own declared
set: this file itself (the AST self-scans) and the OBJECT UNDER TEST, this
unit's own paper.  No repository state outside those two sets is read, no
subprocess of any kind is invoked, and no module of any other unit is
imported, so the run is correct off-tree and with no version control present.
"""

import ast
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from fractions import Fraction

sys.setrecursionlimit(100000)

SELF = os.path.abspath(__file__)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(SELF)))
OUT_TXT = os.path.join(os.path.dirname(SELF), "gdl_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "gdl_receipt.json")

SCHEMA = "isp/v14/gdl/1"
PAPER_REL = "v14/paper-25-gdl.md"

# ===========================================================================
# SECTION 1.  PROVENANCE -- the pinned sources
# ===========================================================================

SOURCES = [
    ("A-PIN", "v14/note-gdl-pin.md", "fe9533371046",
     "THIS UNIT'S PIN (ledger #205): the five stages, the barred fitted "
     "forms, the mandatory frozen control, the pre-registered outcomes and "
     "the shape-only status of the Diosi-Penrose citation."),
    ("A-P20", "v14/paper-20-coupling.md", "4824d190af73",
     "THE COUPLING (paper-20, terminal): the coupled machine's published "
     "description -- the walk, the emission law, the update semantics, the "
     "mandatory frozen control, the coin fiber and the declared horizon."),
    ("A-P20CODE", "v14/code/coupling_exact.py", "72e7b299f66e",
     "THE COMMITTED DRIVER, READ AS A SPEC AND NEVER RUN: this unit imports "
     "no module of it, subprocesses nothing, and re-implements the walk, the "
     "emission law and the update semantics from its published description."),
    ("A-P20OUT", "v14/code/coupling_output.txt", "42b103eeec14",
     "THE PARENT'S COMMITTED TRANSCRIPT, read for the anchor values this "
     "unit's independent rebuild is required to reproduce at equality."),
    ("A-P20REC", "v14/code/coupling_receipt.json", "55273f6b6068",
     "THE PARENT'S COMMITTED RECEIPT: the ladder, the leaf counts, the "
     "observables and the coin-fiber witnesses, read at run time and located "
     "in those bytes rather than retyped."),
    ("A-GITER", "v14/paper-16-gamma-iteration.md", "5c1df50673d4",
     "THE GRAVITY LAW (Gamma-iteration, terminal, commit 2895a9a): the "
     "LAW-NATIVE normaliser and the kernel k_1 = q/M this unit's emission "
     "rate is taken from."),
    ("A-GITERREC", "v14/code/giter_receipt.json", "42255f50328a",
     "THE LAW'S COMMITTED RECEIPT."),
    ("A-W3", "v14/paper-19-r3-weld.md", "50bb81e67942",
     "THE WELD (paper-19, terminal): the arena and the forced dictionary "
     "[ACTOR->SITE | CO-DIVISION-PAIR->LINK | DIVISION-COUNT->n_l(x)]."),
    ("A-HA", "v13/paper-ha-successor.md", "f286ba10d2d9",
     "I7 / HA: the declared readout and the admissibility criterion."),
    ("A-L1", "v11/note-L1-lorentz-no-go-lemma.md", "93ea24591c3c",
     "L-1: the fourth-form clause and the sentence retracted on 2026-07-28 "
     "that no paper of this line may reproduce."),
    ("A-CAT", "v11/note-v11p0a-reproduction-catalog.md", "0cebe543e814",
     "the reproduction catalog: the BHS block and the Kleitman-Rothschild "
     "height-control warning."),
]
SOURCE_IDS = [s[0] for s in SOURCES]

OBJECT_READS_WHY = {
    "SELF": "this file, AST-parsed by its own float scan, import scan, "
            "writer-shape probe and self-test shape probe",
    "PAPER": "the object under test, read once by main and handed to the "
             "paper gates",
}

BANNED_L1 = ("precisely the form U4 tests, and precisely the form the "
             "corpus's strongest relativity result took")

# The two resonances the parent NAMED, carried here because this unit reads
# the same determinant and the same Gram matrix.
LORENTZ_NAMED = (
    "The determinant that reaches 0 in the parent and is read again here is "
    "NAMED AND NOT READ: it is the exact boundary of I7's own admissibility "
    "criterion on a nine-site Euclidean lattice, it is not a signature and "
    "not a light cone, no indefinite form is reached at this horizon, and no "
    "Lorentzian, causal or signature-change reading of it is taken here or "
    "licensed by anything measured here.")
HEX_NAMED = (
    "The second resonance is NAMED before it is heard: q = [[1, -1/2], "
    "[-1/2, 1]] is the Gram matrix a reader will recognise as hexagonal, unit "
    "lengths meeting at one hundred and twenty degrees, and this unit takes "
    "no triangular, hexagonal, crystallographic or lattice-geometry reading "
    "of it whatever.")
# THIS UNIT'S OWN WALL.  The pin bars SI numbers and experimental-value
# claims outright and makes the corpus's gravitational-decoherence arc a
# SHAPE citation.  The abstention is stated and then gated.
DP_NAMED = (
    "The corpus's Diosi-Penrose gravitational-decoherence arc is cited for "
    "SHAPE ONLY: this unit inherits no number, no rate, no mass and no "
    "experimental claim from it, states nothing in SI units, and every "
    "quantity published here is a count or an exact rational of the "
    "substrate's own.")

# THE DECLARED FALSIFIER REGISTRY (E-23).  Every row names the gate it must
# die at, THE SYMBOL IT MOVES and THE VALUE IT MOVES IT TO; the last two are
# re-derived from THIS FILE's own AST at run time and the published prose must
# name both.
MUTANTS = [
    # -- the machine, rebuilt
    ("MUT-ANCHOR-LEAVES", "G-PARENT-REPRODUCED",
     "moves `anchor_bad` to FORGED, the one-element list ['FORGED']: an "
     "anchor value of the parent's committed receipt is reported reproduced "
     "when the rebuild disagrees -- must die at the parent-reproduction gate",
     "anchor_bad", "FORGED"),
    ("MUT-ANCHOR-LOCATED", "G-PARENT-LOCATED",
     "moves `located` to nloc - 1, the count of rebuilt values located "
     "verbatim in the parent's committed bytes less one -- must die at the "
     "located-in-bytes gate", "located", "nloc - 1"),
    ("MUT-MASS", "G-BRANCH-MASS",
     "moves `mass_bad` to A-COUPLED, the one-element list naming an arm whose "
     "branch weights do not sum to exactly 1 at some level -- must die at the "
     "per-level mass gate", "mass_bad", "A-COUPLED"),
    ("MUT-ROUTE", "G-ENSEMBLE-EXHAUSTIVE",
     "moves `route_bad` to 1: the carried frontier's branch count and the "
     "count recomputed from the emission supports disagree at one level -- "
     "must die at the two-route gate", "route_bad", "1"),
    ("MUT-UNITARY", "G-WALK-UNITARY",
     "moves `uviol` to 1: one site-branch-step stops preserving its own site "
     "mass -- must die at the per-object unitarity gate", "uviol", "1"),
    ("MUT-KERNEL", "G-LAW-KERNEL",
     "moves `kviol` to 2: two kernel entries are detached from q/M -- must "
     "die at the law-native kernel gate", "kviol", "2"),
    ("MUT-LAW-STAMP", "G-LAW-CHECK-CLASSES",
     "moves `stamp_bad_law` to FORGED: a law-check class is published without "
     "its DEFINITIONAL stamp or the three-way split stops summing to the "
     "composite -- must die at the class-stamp gate",
     "stamp_bad_law", "FORGED"),
    # -- the functionals
    ("MUT-D-SPEC", "G-FUNCTIONALS-DECLARED",
     "moves `spec_bad` to D2-OFFDIAG, reporting a declared decoherence "
     "functional whose published specification does not match the value its "
     "own code returns at some object -- must die at the specification gate",
     "spec_bad", "D2-OFFDIAG"),
    ("MUT-D-EXACT", "G-FUNCTIONALS-EXACT",
     "moves `nonexact` to 1: a decoherence value is reported carried as "
     "something other than an exact Fraction -- must die at the exactness "
     "gate", "nonexact", "1"),
    ("MUT-L1-PRICE", "G-L1-PRICED",
     "moves `irrational` to 0: the off-diagonal moduli are reported all "
     "rational, hiding the price of the squared-modulus declaration -- must "
     "die at the l1-price gate", "irrational", "0"),
    ("MUT-D2-SPLIT", "G-PURITY-SPLIT",
     "moves `split_bad` to 3: the exact split D1 + D2 = purity is reported "
     "violated at three objects -- must die at the purity-split gate",
     "split_bad", "3"),
    # -- the growth functionals
    ("MUT-RATE-IS-BORN", "G-RATE-IS-BORN",
     "moves `rb_bad` to 1: the law's own site emission rate, summed through "
     "the kernel, is reported to differ from the Born site mass at one "
     "site-object -- must die at the emission-rate gate", "rb_bad", "1"),
    ("MUT-RATE-TOTAL", "G-RATE-TOTAL",
     "moves `rt_bad` to 1: an object's total emission rate is reported away "
     "from exactly one division event per coupled step -- must die at the "
     "total-rate gate", "rt_bad", "1"),
    ("MUT-GROWTH-FROZEN", "G-GROWTH-FROZEN-ZERO",
     "moves `fz_growth` to 1: the frozen control is reported to grow its "
     "record -- must die at the gate that binds the control's own definition",
     "fz_growth", "1"),
    # -- the relation
    ("MUT-RELATION-EXACT", "G-RELATION-CENSUS",
     "moves `grid_bad` to FORGED, reporting a grid cell whose published "
     "verdict word disagrees with its own censused failure count -- must die "
     "at the relation-census gate", "grid_bad", "FORGED"),
    ("MUT-VACUITY", "G-VACUITY-DECLARED",
     "moves `vac_bad` to 1: a functional-dependence verdict of EXACT is "
     "published on a test with no non-singleton class -- must die at the "
     "vacuity gate", "vac_bad", "1"),
    ("MUT-FAILURE-SET", "G-FAILURE-CENSUS",
     "moves `census_bad` to 1: a cell's censused failing-object count, "
     "failing-class count or NON-SINGLETON count disagrees with the recount "
     "taken from its own partition -- must die at the failure-census gate",
     "census_bad", "1"),
    ("MUT-TOTAL-FAILURE", "G-TOTAL-FAILURE-STAMP",
     "moves `stamp_bad_cells` to FORGED: a cell whose every non-singleton "
     "class fails is published without its TOTAL-FAILURE stamp, or a passing "
     "count disagrees with its own census -- must die at the stamp gate",
     "stamp_bad_cells", "FORGED"),
    ("MUT-FROZEN-GRID", "G-FROZEN-GRID-CENSUS",
     "moves `frozen_bad` to FORGED: the control's own 45-cell census stops "
     "accounting for all of its rows, or the coupled PARTIAL cells stop being "
     "accounted against the control's words -- must die at the frozen-grid "
     "gate", "frozen_bad", "FORGED"),
    ("MUT-FITTED", "G-NO-FITTED-FORM",
     "moves `fitted` to 1: a fitted form is reported present in this unit's "
     "own published relation layer -- must die at the no-fitted-form gate",
     "fitted", "1"),
    # -- forcedness
    ("MUT-COIN-FIBER", "G-COIN-FIBER",
     "moves `fiber_bad` to w/3, reporting a coin fiber member whose verdict "
     "shape, separation ladder, identities or occupancy thresholds differ "
     "from the delivered member's -- must die at the coin-fiber gate",
     "fiber_bad", "w/3"),
    ("MUT-FIBER-MEMBERS", "G-FIBER-EXECUTED",
     "moves `executed` to [:-1], the executed fiber-member ids with the last "
     "one dropped, so a declared member is reported measured while its run is "
     "missing -- must die at the fiber-inventory gate", "executed", "[:-1]"),
    ("MUT-COIN-UNITARY", "G-COIN-ADMISSIBLE",
     "moves `cu_bad` to (-1+w)/3, reporting a fiber member as exactly unitary "
     "and S_3-covariant when it is not -- must die at the coin-admissibility "
     "gate", "cu_bad", "(-1+w)/3"),
    ("MUT-PHASE-PAIR", "G-GLOBAL-PHASE-PAIR",
     "moves `phase_bad` to 1: +/- Grover, a pair differing by a global phase, "
     "are reported to give different published rows -- must die at the "
     "global-phase gate", "phase_bad", "1"),
    ("MUT-FROZEN-EXCLUSION", "G-FROZEN-EXCLUSION",
     "moves `excluded` to [], the empty list, hiding the exclusion of a "
     "relation that holds identically on the frozen stage -- must die at the "
     "frozen-exclusion gate", "excluded", "[]"),
    ("MUT-FROZEN-RAN", "G-FROZEN-CONTROL",
     "moves `frozen_ran` to False: the mandatory control is reported without "
     "its execution -- must die at the control-execution gate",
     "frozen_ran", "False"),
    ("MUT-SEPARATION", "G-SEPARATION-LADDER",
     "moves `sep_bad` to 1: a functional's first separating step is reported "
     "away from the step its own value sets first differ at -- must die at "
     "the separation-ladder gate", "sep_bad", "1"),
    ("MUT-DOMINATION", "G-DOMINATION",
     "moves `dom_bad` to 1: a monotone domination is published without the "
     "exact witness its own census produced -- must die at the domination "
     "gate", "dom_bad", "1"),
    # -- the mechanism
    ("MUT-BLIND-D1", "G-BLINDNESS-D1",
     "moves `d1_moves` to 1: the site-basis inverse participation is reported "
     "to move on a declared foreign count field -- must die at the "
     "record-blindness gate", "d1_moves", "1"),
    ("MUT-COOCC", "G-COOCCUPANCY",
     "moves `cooc_bad` to 1: an object no two of whose sites share two "
     "occupied links is reported with a moving off-diagonal mass -- must die "
     "at the co-occupancy gate", "cooc_bad", "1"),
    ("MUT-COOCC-THRESHOLD", "G-COOCCUPANCY-THRESHOLD",
     "moves `cooc_threshold` to 3: the first step carrying a co-occupancy "
     "pair is reported one step early -- must die at the threshold gate",
     "cooc_threshold", "3"),
    ("MUT-D3-READS", "G-BLINDNESS-D3",
     "moves `d3_moves` to 0: the record-reading functional is reported blind "
     "to the record -- must die at the two-way blindness gate",
     "d3_moves", "0"),
    ("MUT-OCCUPANCY", "G-OCCUPANCY-PREDICATES",
     "moves `occ_bad` to FORGED: the two occupancy predicates stop differing "
     "by exactly one step, or stop agreeing between the arms -- must die at "
     "the two-predicate gate", "occ_bad", "FORGED"),
    ("MUT-PAIR-MECHANISM", "G-PAIR-MECHANISM",
     "moves `pair_bad` to 1: a site pair meeting in at most one occupied link "
     "is reported with a moving |rho_xy|^2, which THEOREM B forbids -- must "
     "die at the pair-grain gate", "pair_bad", "1"),
    ("MUT-BLIND-G5", "G-BLINDNESS-G5",
     "moves `g5_moves` to 1: the law's own growth functional is reported to "
     "move on a declared foreign count field, breaking the doubly-blind "
     "ground of the frozen exclusion -- must die at the G5-blindness gate",
     "g5_moves", "1"),
    ("MUT-THEOREM-A", "G-THEOREM-A",
     "moves `sd_bad` to FORGED: the site-dependent demonstration is reported "
     "with a moving site marginal, a moving D1, a site-uniform coin, a "
     "non-unitary block or a static D2 -- must die at the THEOREM A gate",
     "sd_bad", "FORGED"),
    ("MUT-THEOREM-B", "G-THEOREM-B",
     "moves `sym_bad` to 1: the cancellation algebra is reported with one "
     "coefficient mismatch -- must die at the symbolic gate", "sym_bad", "1"),
    ("MUT-FOREIGN-FIELD", "G-FOREIGN-FIELDS-FOREIGN",
     "moves `foreign_bad` to STALE: a declared foreign count field is "
     "reported to be a record this run actually generates -- must die at the "
     "foreignness gate", "foreign_bad", "STALE"),
    # -- the third channel
    ("MUT-RESIDUE-BLIND", "G-RESIDUE-CHANNEL",
     "moves `res_state` to 1: a state-internal functional is reported to "
     "distinguish two records congruent mod 3, which the residue reading "
     "forbids -- must die at the third-channel gate", "res_state", "1"),
    ("MUT-RESIDUE-TWO-WAY", "G-RESIDUE-CHANNEL",
     "moves `res_reads` to 0: the record-reading functional is reported blind "
     "to congruent-but-different records, so the census would decide nothing "
     "-- must die at the same gate's two-way leg", "res_reads", "0"),
    ("MUT-WRAPAROUND", "G-RESIDUE-WRAPAROUND",
     "moves `wrap_bad` to FORGED: the wraparound census stops reporting the "
     "wrap written inside the horizon, read outside it, and congruent to the "
     "welded value -- must die at the wraparound gate", "wrap_bad", "FORGED"),
    # -- the prediction
    ("MUT-PREDICTION", "G-PREDICTION-ROW",
     "moves `pred_forced` to not carried, detaching the published forced flag "
     "from the fiber census that is supposed to carry it -- must die at the "
     "prediction gate", "pred_forced", "not carried"),
    ("MUT-PREDICTION-RENDER", "G-PREDICTION-RENDERED",
     "moves `prow` to FORGED, appending that word to the rendered prediction "
     "sentence -- must die at the render gate", "prow", "FORGED"),
    # -- the walls
    ("MUT-WALL-L1", "G-WALL-L1",
     "moves `ptext` to BANNED_L1, the object under test with the retracted "
     "L-1 sentence appended line-wrapped and blockquoted -- must die at the "
     "L-1 wall", "ptext", "BANNED_L1"),
    ("MUT-WALL-BHS", "G-WALL-BHS",
     "moves `hay` to boosted rest frame -- this run's measurement surface with "
     "a sprinkling-grade reading written into it -- must die at the BHS "
     "abstention scan", "hay", "boosted rest frame"),
    ("MUT-WALL-KR", "G-WALL-KR",
     "moves `hay` to myrheim-meyer, a dimension estimate with no height "
     "control written into the measurement surface -- must die at the "
     "Kleitman-Rothschild scan", "hay", "myrheim-meyer"),
    ("MUT-WALL-COSMO", "G-WALL-COSMO",
     "moves `hay` to cosmological expansion, a cosmological reading written "
     "into the measurement surface -- must die at the cosmological/continuum "
     "scan", "hay", "cosmological expansion"),
    ("MUT-WALL-SI", "G-WALL-NO-SI",
     "moves `hay` to collapse rate in kilogram, an SI reading written into "
     "the measurement surface -- must die at this unit's own "
     "SI/experimental-value scan", "hay", "collapse rate in kilogram"),
    ("MUT-WALL-DP", "G-WALL-DP-SHAPE",
     "moves `dp` to False: the mandatory shape-only naming of the "
     "Diosi-Penrose arc is reported absent from the object under test -- must "
     "die at the shape-citation gate", "dp", "False"),
    ("MUT-WALL-LORENTZ", "G-WALL-LORENTZ-NAMED",
     "moves `lz` to False: the mandatory Lorentzian naming sentence is "
     "reported absent -- must die at the naming gate", "lz", "False"),
    ("MUT-WALL-HEX", "G-WALL-HEX-NAMED",
     "moves `hx` to False: the hexagonal naming sentence is reported absent "
     "-- must die at the second naming gate", "hx", "False"),
    # -- the ledgers, the outcome grammar and the verdict
    ("MUT-MEASURE-STAMP", "G-MEASURE-DECLARED",
     "moves `stamp_bad` to 1: a published fraction over a configuration space "
     "carries neither a declared measure nor the COUNTING-ONLY stamp -- must "
     "die at the E-24 measure gate", "stamp_bad", "1"),
    ("MUT-CHOICE-BAR", "G-CHOICE-INVENTORY",
     "moves `choice_bad` to F12-BAR-SCOPE: the verdict-determining bar-scope "
     "row is reported inconsistent with the declaration it names -- must die "
     "at the choice-inventory gate", "choice_bad", "F12-BAR-SCOPE"),
    ("MUT-OUTCOME-ARM", "G-OUTCOME-REACHABILITY",
     "moves `wiring_matches_the_delivered_measurement` to False, unwiring the "
     "control arm from the delivered measurement so the head word would no "
     "longer be the one this arena's own result selects -- must die at the "
     "outcome-reachability gate",
     "wiring_matches_the_delivered_measurement", "False"),
    ("MUT-VERDICT-WORD", "G-VERDICT-RECONSTRUCTED",
     "moves `verdict` to GDL-LAW-FORCED-D1-IS-THE-SQUARED-RATE in its gates "
     "segment, in the builder alone -- must die at the comparator, which "
     "types its own templates and re-derives the word from the primitives",
     "verdict", "GDL-LAW-FORCED-D1-IS-THE-SQUARED-RATE"),
    ("MUT-VERDICT-VALUE", "G-VERDICT-RECONSTRUCTED",
     "moves `verdict` to 26 OF 27 in its arena segment, retyping one measured "
     "value inside it -- must die at the same comparator, by occurrence "
     "count", "verdict", "26 OF 27"),
    # -- the paper
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS",
     "moves `sent` to 26 cells, retyping an assembled claim -- must die at the "
     "claim gate", "sent", "26 cells"),
    ("MUT-PAPER-TABLE", "G-PAPER-TABLES",
     "moves `trows` to FORGED: the rendered table rows lose their last row and "
     "gain a forged one -- must die at the table gate",
     "trows", "FORGED"),
    ("MUT-PAPER-NUMERAL", "G-PAPER-NUMERAL-COVERAGE",
     "moves `text` to 123456789: that numeral is planted in the object under "
     "test's own bytes, where the coverage scan must find it unregistered -- "
     "must die at the #20 coverage scan",
     "text", "123456789"),
    ("MUT-PAPER-HEAD", "G-PAPER-HEAD-VERBATIM",
     "moves `probe` to Z at its last character -- a derived verdict segment, "
     "perturbed before it is matched into the paper -- must die at the "
     "head-verbatim gate", "probe", "Z"),
    ("MUT-PAPER-BLOCK", "G-PAPER-HEAD-VERBATIM",
     "moves `blockmap` to extra_fence, the paper's own fenced-block multiset "
     "PLUS one forged fence the head does not contain, so an EXTRA block "
     "would shadow a forged twin -- must die at the same gate's MULTISET leg",
     "blockmap", "extra_fence"),
    ("MUT-PAPER-POLARITY", "G-PAPER-CLAIM-POLARITY",
     "moves `mutated` to True, swapping a positive claim for its negation in "
     "the object under test -- must die at the polarity gate",
     "mutated", "True"),
    # -- the instrument
    ("MUT-CLI-PERMISSIVE", "G-CLI-WHITELIST",
     "moves `bad` to --nope: the argv whitelist is swapped for the registered "
     "permissive shape, which accepts that flag -- must die at the CLI gate",
     "bad", "--nope"),
    ("MUT-SELFTEST-WRITES", "G-SELFTEST-WRITES-NOTHING",
     "moves `st_ok` to False: the self-test path is claimed to reach a writer "
     "-- must die at the writes-nothing gate", "st_ok", "False"),
    ("MUT-WRITER-SHAPE", "G-WRITER-SHAPE",
     "moves `gate_names_in_finish` to [:-1], the list with the terminal "
     "integrity gate's name dropped -- must die at the writer-shape probe, "
     "which is taken BEFORE the gate ledger is snapshotted",
     "gate_names_in_finish", "[:-1]"),
    ("MUT-FALSIFIER-DESC", "G-FALSIFIER-HONESTY",
     "moves `declared` to FORGED: one falsifier's declared (symbol, value) "
     "pair is moved away from what this file's AST says its hook assigns and "
     "writes -- must die at the falsifier-honesty gate",
     "declared", "FORGED"),
    ("MUT-SEAL-DROP", "G-SEAL-COMPLETE",
     "moves `drop` to SEAL-COVERAGE: the seal row with that sid is silently "
     "not taken -- must die at the totality gate", "drop", "SEAL-COVERAGE"),
    ("MUT-SEAL-BROKEN", "G-SEAL-COMPLETE",
     "moves `horizon` to + 1 in the sealed counts block, between its gate and "
     "the write -- must die at the same gate", "horizon", "+ 1"),
    ("MUT-TRANSCRIPT-FLIP", "G-SEAL-COMPLETE",
     "moves `transcript_head` to FLIPPED at its first line, after it is "
     "sealed -- must die at the same gate", "transcript_head", "FLIPPED"),
    ("MUT-SWEEP-UNBOUND", "G-SWEEP-BOUND",
     "moves `swept` to True on a run carrying no sweep -- must die at the "
     "gate that binds the sweep's execution, its per-row gate evidence and "
     "its harness execution count to the writer", "swept", "True"),
]
MUTANT_NAMES = {m[0] for m in MUTANTS}

MUT = None
QUIET = False
LINES = []
READS = []
# the number of times the mutant harness has actually entered its body.  It is
# incremented in ONE place, `run_mutant`, and G-SWEEP-BOUND binds it.
MUTANT_RUNS = [0]


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
# SECTION 1b.  MACHINERY -- the gate ledger, the total seal, the normaliser
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


SEALED_PATHS = [
    ("SEAL-SCHEMA", "schema", "G-PROVENANCE"),
    ("SEAL-PROVENANCE", "provenance", "G-PROVENANCE"),
    ("SEAL-ARITHMETIC", "arithmetic", "G-EXACT-ARITHMETIC"),
    ("SEAL-PYTHON", "python", "G-EXACT-ARITHMETIC"),
    ("SEAL-OBJECT-READS", "object_reads", "G-READS-DECLARED"),
    ("SEAL-VERBATIM", "verbatim_anchors", "G-VERBATIM"),
    # THE DECLARED GATE IS THE ONE THE SEAL IS ACTUALLY TAKEN AT (K3 MINOR-2):
    # a block seal is taken after the block's LAST gate, and it says so.  An
    # AST self-check inside G-SEAL-COMPLETE re-derives every window from this
    # file's own source and compares it with the label published here.
    ("SEAL-REBUILD", "rebuild", "G-PARENT-LOCATED"),
    ("SEAL-ENSEMBLE", "ensemble", "G-BRANCH-MASS"),
    ("SEAL-MACHINE", "machine", "G-LAW-CHECK-CLASSES"),
    ("SEAL-FUNCTIONALS", "functionals", "G-PURITY-SPLIT"),
    ("SEAL-GROWTH", "growth", "G-GROWTH-FROZEN-ZERO"),
    ("SEAL-RELATION", "relation", "G-NO-FITTED-FORM"),
    ("SEAL-FORCEDNESS", "forcedness", "G-GLOBAL-PHASE-PAIR"),
    ("SEAL-EXCLUSION", "exclusion", "G-FROZEN-EXCLUSION"),
    ("SEAL-MECHANISM", "mechanism", "G-FOREIGN-FIELDS-FOREIGN"),
    ("SEAL-RESIDUE", "residue", "G-RESIDUE-WRAPAROUND"),
    ("SEAL-PREDICTION", "prediction", "G-PREDICTION-RENDERED"),
    ("SEAL-WALLS", "walls", "G-WALL-HEX-NAMED"),
    ("SEAL-MEASURE", "measure_ledger", "G-MEASURE-DECLARED"),
    ("SEAL-CHOICES", "choices", "G-CHOICE-INVENTORY"),
    ("SEAL-OUTCOME", "outcome", "G-OUTCOME-REACHABILITY"),
    ("SEAL-VERDICT", "verdict", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-COUNTS", "counts", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-PAPER-CLAIMS", "paper_claims", "G-PAPER-CLAIMS"),
    ("SEAL-PAPER-TABLES", "paper_tables", "G-PAPER-TABLES"),
    ("SEAL-PAPER-COVERAGE", "paper_coverage", "G-PAPER-HEAD-VERBATIM"),
    ("SEAL-POLARITY", "polarity", "G-PAPER-CLAIM-POLARITY"),
    ("SEAL-COVERAGE", "coverage", "G-COVERAGE"),
    ("SEAL-REACHABILITY", "reachability", "G-REACHABILITY"),
    ("SEAL-WAIVERS", "waiver_ledger", "G-COVERAGE"),
    ("SEAL-MUTANTS", "mutants", "G-FALSIFIER-HONESTY"),
    ("SEAL-WRITER-SHAPE", "writer_shape", "G-WRITER-SHAPE"),
    ("SEAL-MUTANT-SWEEP", "mutant_sweep", "G-SWEEP-BOUND"),
    ("SEAL-GATES", "gates", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-CLOSING", "closing_gates", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-TOTALS", "totals", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-TRANSCRIPT", "transcript_head", "G-PAPER-COVERAGE-FINAL"),
]
DECLARED_UNSEALED = ["seal_manifest", "payload_sha256_12"]
DECLARED_UNSEALED_FROZEN = ("seal_manifest", "payload_sha256_12")
UNSEALED_FORCING = {
    "seal_manifest": "carries the seal rows themselves; sealing it would seal "
                     "a digest of its own digest.  CHAINED: compared against "
                     "SEAL.rows after read-back from disk.",
    "payload_sha256_12": "is the digest of the payload the seal closes over "
                         "and is assigned after that close.  CHAINED: "
                         "compared against SEAL.payload_sha after read-back.",
}
MEASURED_KEYS = ("rebuild", "ensemble", "machine", "functionals", "growth",
                 "relation", "forcedness", "exclusion", "mechanism",
                 "residue", "prediction", "choices", "outcome", "counts",
                 "verdict")


class Seal:
    """the TOTAL gate-time seal (#119 + the #148 totality addendum)."""

    def __init__(self):
        self.rows = []
        self.index = {}
        self.payload = None
        self.payload_sha = None
        self.text_sha = None
        self.text_lines = None

    def take(self, sid, obj):
        path = [p for s, p, _g in SEALED_PATHS if s == sid][0]
        at = [g for s, _p, g in SEALED_PATHS if s == sid][0]
        d = digest(jpath(obj, path))
        drop = pick("MUT-SEAL-DROP", False, sid == "SEAL-COVERAGE")
        if drop:
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
        have = {r["seal"] for r in self.rows}
        want = {s for s, _p, _g in SEALED_PATHS}
        return sorted(want - have), sorted(have - want)

    def close(self, obj, payload, text):
        broken = self.verify(obj)
        if broken:
            raise GateFail("G-ARTIFACT-INTEGRITY :: the payload was sealed "
                           "over a broken seal :: %s" % broken)
        self.payload = payload
        self.payload_sha = digest(payload)
        self.text_sha = digest(text)
        self.text_lines = len(text.split("\n"))


def read_bytes(rel):
    READS.append(rel)
    path = os.path.join(REPO, rel)
    if not os.path.isfile(path):
        # #91: under-provisioned tree -- abort LOUDLY and CLEANLY, writing
        # nothing, rather than degrading to a silent partial run.
        raise GateFail("G-PROVENANCE :: declared source not present at %r; "
                       "this run is under-provisioned and writes nothing"
                       % path)
    with open(path, "rb") as fh:
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
         "⁄": "/", " ": " ", "ω": "w", "ψ": "psi",
         "Γ": "Gamma", "⊗": "(x)", "√": "sqrt", "ε": "eps",
         "⟨": "<", "⟩": ">", "Δ": "Delta", "π": "pi", "ρ": "rho",
         "ó": "o", "é": "e", "ö": "o", "í": "i", "á": "a"}

_MD_PREFIX = re.compile(r"^(?:\s*(?:>+|[-*+]|\d+[.)])\s+)+")


def mdstrip(s):
    """#125 WITH MARKDOWN-PREFIX NORMALIZATION."""
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
    return norm(ascii_fold(mdstrip(s).replace("*", "").replace("`", "")))


NEEDLE_FLOOR = 30


def match_needle(hay, needle):
    n = canon(needle)
    if len(n) < NEEDLE_FLOOR:
        raise GateFail("G-VERBATIM :: needle below the #62 length floor: %r"
                       % needle)
    return n in canon(hay)


# ===========================================================================
# SECTION 2.  EXACT ARITHMETIC ON Z[w], AND THE ARENA
# ===========================================================================
# Z[w] with w^2 = -1 - w.  An element is the INTEGER pair (a, b) meaning
# a + b*w.  The walk's amplitudes are carried as such pairs over a common
# denominator 9^t, so every amplitude is exact and no Fraction is constructed
# inside the propagation loop.

def zmul(z1, z2):
    a, b = z1
    c, d = z2
    return (a * c - b * d, a * d + b * c - b * d)


def zadd(z1, z2):
    return (z1[0] + z2[0], z1[1] + z2[1])


def zconj(z):
    a, b = z
    return (a - b, -b)


def absq(z):
    """|a + b w|^2 = a^2 - a b + b^2, a RATIONAL INTEGER."""
    a, b = z
    return a * a - a * b + b * b


Z0 = (0, 0)
Z1 = (1, 0)
WPOW = [(1, 0), (0, 1), (-1, -1)]
SITES = tuple((i, j) for i in range(3) for j in range(3))
SITE_INDEX = {s: k for k, s in enumerate(SITES)}
LINKS = ((1, 0), (0, 1), (1, 1))
LINK_NAMES = ("(1,0)", "(0,1)", "(1,1)")
NCELL = 27
DIM = 27
NSITE = 9


def vadd(a, b):
    return ((a[0] + b[0]) % 3, (a[1] + b[1]) % 3)


def cell(si, li):
    return si * 3 + li


SHIFT_T = tuple(cell(SITE_INDEX[vadd(SITES[s], LINKS[i])], i)
                for s in range(9) for i in range(3))

# THE GROVER COIN as integer numerators over 3 (paper-20 §3.2, delivered).
GN = tuple(tuple(2 if i != j else -1 for j in range(3)) for i in range(3))
GROVER_Z = tuple(tuple((GN[i][j], 0) for j in range(3)) for i in range(3))


def three_C(c):
    """3C for the S_3-covariant coin C = I + c J with 3c the Z[w] pair `c`."""
    return tuple(tuple(zadd((3, 0), c) if i == j else c for j in range(3))
                 for i in range(3))


# THE DECLARED COIN FIBER (paper-20 §3.2: six classes up to a global phase
# over the arena's own (1/3)Z[w], of which one is +/- Grover).  The two Grover
# members differ by a GLOBAL PHASE and this unit measures that they give
# identical published rows rather than assuming it.
COIN_FIBER = (
    ("GROVER", GROVER_Z),
    ("-GROVER", three_C((-2, 0))),
    ("w/3", three_C((0, 1))),
    ("(-1+w)/3", three_C((-1, 1))),
    ("(-1-w)/3", three_C((-1, -1))),
    ("(-2-w)/3", three_C((-2, -1))),
)
COIN_IDS = [c[0] for c in COIN_FIBER]
READING_FIBER = ("A", "B")
DELIVERED_COIN = "GROVER"
DELIVERED_READING = "A"

# THE SITE-DEPENDENT COIN, DECLARED: the six admissible members cycled over the
# nine sites.  Block-diagonal in the site index, exactly unitary on every
# block, and NOT the same at every site.  It is not a member of this unit's
# fiber and nothing measured on it is claimed about this arena; it exists to
# isolate THEOREM A's hypothesis from THEOREM B's.
SITE_DEPENDENT_COINS = tuple(COIN_FIBER[s % len(COIN_FIBER)][1]
                             for s in range(9))


def coin_unitary_exactly(M):
    """M M^* = 9 I in exact Z[w] arithmetic, entry by entry (#87)."""
    for i in range(3):
        for j in range(3):
            tot = Z0
            for k in range(3):
                tot = zadd(tot, zmul(M[i][k], zconj(M[j][k])))
            want = (9, 0) if i == j else Z0
            if tot != want:
                return False
    return True


def coin_s3_covariant(M):
    """the coin commutes with all six permutation matrices of the links."""
    from itertools import permutations
    for p in permutations(range(3)):
        for i in range(3):
            for j in range(3):
                if M[p[i]][p[j]] != M[i][j]:
                    return False
    return True


def q_of(nvec):
    """I7's own readout: the three link counts at a site give the 2x2 form."""
    n1, n2, n3 = nvec
    q11 = Fraction(n1)
    q22 = Fraction(n2)
    q12 = Fraction(n3 - n1 - n2, 2)
    return q11, q22, q12, q11 * q22 - q12 * q12


def admissible(nvec):
    """I7's exact Sylvester criterion: nonsingular and positive definite."""
    q11, _a, _b, det = q_of(nvec)
    return q11 > 0 and det > 0


def site_counts(n, si):
    return (n[si * 3], n[si * 3 + 1], n[si * 3 + 2])


WELDED = tuple([1] * NCELL)
HORIZON = 5
LADDER = (1, 2, 3, 4, 5)
START = (0, 0)
INIT_COIN = 0


# ===========================================================================
# SECTION 3.  THE COUPLED MACHINE, RE-IMPLEMENTED FROM THE COMMITTED SPEC
# ===========================================================================
# paper-20's driver is read as a SPEC (A-P20CODE, hash-pinned) and never
# imported and never subprocessed -- #91 forbids the second and this unit's
# whole claim to independence forbids the first.  What is rebuilt here:
#
#   THE WALK.      C(x) = G . D(x) with D(x) = diag(w^{n_l(x)}), site-block-
#                  diagonal; the shift |x, l> -> |x + l, l>.
#   THE EMISSION.  READING A (the Born menu): q(l|x) = |(C psi)(x,l)|^2.
#                  READING B (the record menu): q(l|x) = n_l(x).  In both the
#                  law-native kernel is k_1(l|x) = q(l|x)/M(x) with
#                  M(x) = sum_l q(l|x), and the emission weight at cell (x,l)
#                  is p(x) . k_1(l|x).
#   THE UPDATE.    A division event on cell (x,l) increments n_l(x) by one;
#                  admissibility is a property of the RECORD, not a
#                  precondition of the STEP, so the dynamics runs on.
#   THE CONTROL.   The MANDATORY frozen stage: the identical walk, emission
#                  and branching on counts that never update, executed
#                  through THIS SAME FUNCTION.
#
# The rebuild is then ANCHORED: the parent's committed receipt is read and its
# own published values are required to come back out of this implementation at
# equality.  That is what makes this a re-implementation rather than a rewrite.

def coin_apply(psi, n, coin):
    """the coin, site-block-diagonal: C(x) = G . D(x)."""
    rational = all(coin[i][j][1] == 0 for i in range(3) for j in range(3))
    out = [Z0] * DIM
    for s in range(9):
        b = s * 3
        src = [zmul(psi[b + j], WPOW[n[b + j] % 3]) for j in range(3)]
        for i in range(3):
            if rational:
                a = c = 0
                for j in range(3):
                    g = coin[i][j][0]
                    z = src[j]
                    a += g * z[0]
                    c += g * z[1]
                out[b + i] = (a, c)
            else:
                tot = Z0
                for j in range(3):
                    tot = zadd(tot, zmul(coin[i][j], src[j]))
                out[b + i] = tot
    return out


def coin_apply_sitewise(psi, n, coins):
    """THE SAME STEP with a coin that is BLOCK-DIAGONAL IN THE SITE INDEX and
    unitary on each block but NOT THE SAME AT EVERY SITE -- the demonstration
    that isolates THEOREM A's true hypothesis from THEOREM B's."""
    out = [Z0] * DIM
    for s in range(9):
        b = s * 3
        coin = coins[s]
        src = [zmul(psi[b + j], WPOW[n[b + j] % 3]) for j in range(3)]
        for i in range(3):
            tot = Z0
            for j in range(3):
                tot = zadd(tot, zmul(coin[i][j], src[j]))
            out[b + i] = tot
    return out


def shift(post):
    out = [Z0] * DIM
    for m in range(DIM):
        out[SHIFT_T[m]] = post[m]
    return tuple(out)


def law_kernel(qrow):
    """the law-native normaliser, re-derived on this arena: M(x) = sum_l q,
    G(x,1) = sum_l q(l|x) G(x+l,0) with the terminal condition G(.,0) = 1, and
    k_1(l|x) = q(l|x)/M(x).  Returns (G1, M, k)."""
    M = sum(qrow)
    G1 = sum(qrow)
    if M == 0:
        return G1, M, None
    return G1, M, tuple(Fraction(qrow[i], M) for i in range(3))


# THE THREE LAW-CHECK CLASSES, STAMPED (the paper-20 precedent, K1 MAJOR-3).
# None of the three can fail for any coin, menu or record: each is an identity
# in the DEFINITION of the kernel.  A reader must not take the composite as a
# count of rows that could have failed.  The contentful sibling is the
# site-branch-step unitarity row, which is NOT of this kind and is stamped
# CONTINGENT beside them.
LAW_CHECK_CLASSES = (
    ("law_native", "DEFINITIONAL",
     "G(x,1) is compared with M(x) and `law_kernel` computes both as "
     "sum(qrow); the comparison cannot fail for any coin, menu or record"),
    ("kernel", "DEFINITIONAL",
     "sum_l q/M = 1 is an identity in the definition of the kernel"),
    ("kernel_entry", "DEFINITIONAL",
     "q(l|x) = k_1(l|x) . M(x) is the same identity entry by entry"),
)
CONTINGENT_MACHINE_ROW = (
    "unitarity_checks", "CONTINGENT",
    "site-mass preservation at every site of every branch of every step: a "
    "coin that moved amplitude between sites breaks it, and the declared "
    "site-dependent-coin demonstration of THEOREM A leaves it intact while a "
    "cross-site coin would not")


def emission_weights(reading, Jn, n, den):
    """the law's emission distribution over the 27 cells at one step, exact."""
    wts = [Fraction(0)] * NCELL
    eps = [Fraction(0)] * NSITE
    colsums = []
    for s in range(9):
        b = s * 3
        pn = Jn[b] + Jn[b + 1] + Jn[b + 2]
        if reading == "A":
            qrow = [Fraction(Jn[b + i], den) for i in range(3)]
        else:
            qrow = [Fraction(n[b + i]) for i in range(3)]
        _G1, M, k = law_kernel(qrow)
        if k is None:
            colsums.append(Fraction(0) if pn == 0 else None)
            continue
        colsums.append(sum(k))
        px = Fraction(pn, den)
        for i in range(3):
            wts[b + i] = px * k[i]
        # THE RATE IS SUMMED THROUGH THE KERNEL, never assigned (K1 MINOR-2):
        # eps(x) = sum_l p(x) k_1(l|x).  The ID-RATE-IS-BORN row then genuinely
        # tests the law-native normaliser's column-stochasticity at the site
        # grain instead of comparing a value with itself.
        eps[s] = sum(px * k[i] for i in range(3))
    return wts, eps, colsums


def run_arm(T, coupled, reading, coin=None, light=True, census=False):
    """ONE ARM, exhaustively.  `coupled` False is THE MANDATORY FROZEN CONTROL,
    executed through THIS SAME FUNCTION so it cannot differ from the coupled
    arm in anything but the one line that updates the record."""
    if coin is None:
        coin = GROVER_Z
    p0 = [Z0] * DIM
    p0[cell(SITE_INDEX[START], INIT_COIN)] = Z1
    frontier = [(tuple(p0), WELDED, Fraction(1))]
    levels = []
    ladder = {}
    chk = Counter()
    viol = Counter()
    for t in range(T):
        den = 9 ** (t + 1)
        preden = 9 ** t
        nxt = []
        supports = 0
        for (psi, n, w) in frontier:
            post = coin_apply(list(psi), list(n), coin)
            Jn = [absq(z) for z in post]
            pre = [absq(psi[s * 3]) + absq(psi[s * 3 + 1])
                   + absq(psi[s * 3 + 2]) for s in range(9)]
            pos = [Jn[s * 3] + Jn[s * 3 + 1] + Jn[s * 3 + 2] for s in range(9)]
            chk["norm"] += 1
            if sum(pre) != preden:
                viol["norm"] += 1
            chk["total"] += 1
            if sum(Jn) != den:
                viol["total"] += 1
            for s in range(9):
                chk["site"] += 1
                if pos[s] * preden != pre[s] * den:
                    viol["site"] += 1
                b = s * 3
                if reading == "A":
                    qrow = [Fraction(Jn[b + i], den) for i in range(3)]
                else:
                    qrow = [Fraction(n[b + i]) for i in range(3)]
                G1, M, k = law_kernel(qrow)
                chk["law_native"] += 1
                if G1 != M:
                    viol["law_native"] += 1
                if k is not None:
                    chk["kernel"] += 1
                    if sum(k) != 1:
                        viol["kernel"] += 1
                    for i in range(3):
                        chk["kernel_entry"] += 1
                        if qrow[i] != k[i] * M:
                            viol["kernel_entry"] += 1
            wts, eps, colsums = emission_weights(reading, Jn, n, den)
            chk["emission_total"] += 1
            if sum(wts) != 1:
                viol["emission_total"] += 1
            for s in range(9):
                chk["rate_is_born"] += 1
                if eps[s] != Fraction(pos[s], den):
                    viol["rate_is_born"] += 1
            supports += sum(1 for m in range(NCELL) if wts[m] != 0)
            newpsi = shift(post)
            for m in range(NCELL):
                if wts[m] == 0:
                    continue
                if coupled:
                    li = list(n)
                    li[m] += 1
                    nn = tuple(li)
                else:
                    nn = n
                nxt.append((newpsi, nn, w * wts[m]))
        frontier = nxt
        mass = sum(x[2] for x in frontier)
        levels.append({"t": t + 1, "branches": len(frontier),
                       "branches_from_emission_supports": supports,
                       "mass": str(mass), "mass_is_one": mass == 1})
        ladder[t + 1] = horizon_stats(frontier, 9 ** (t + 1), census=census)
    return {"levels": levels, "ladder": ladder,
            "checks": dict(chk), "violations": dict(viol),
            "frontier": None if light else frontier}


_QC = {}


def _qcached(nv):
    got = _QC.get(nv)
    if got is None:
        _a, _b, _c, d = q_of(nv)
        got = (d, admissible(nv))
        _QC[nv] = got
    return got


_NS = {}


def _nstat(n):
    got = _NS.get(n)
    if got is not None:
        return got
    npd = 0
    dets = set()
    mx = 0
    wrapped = 0
    for s in range(9):
        d, adm = _qcached(site_counts(n, s))
        dets.add(d)
        if adm:
            npd += 1
    moved = []
    for m in range(NCELL):
        if n[m] != WELDED[m]:
            moved.append((m, n[m] - WELDED[m]))
        if n[m] > mx:
            mx = n[m]
        if n[m] > 3:
            wrapped += 1
    got = (npd, frozenset(dets), tuple(moved), mx, wrapped)
    _NS[n] = got
    return got


def horizon_stats(frontier, den, census=False):
    """the observable set this unit re-derives to ANCHOR against the parent."""
    accf = [Fraction(0)] * 9
    Eb = defaultdict(Fraction)
    exit_p = Fraction(0)
    dets = set()
    maxcell = 0
    wrap_branches = 0
    wrap_cells = 0
    wrap_as_welded = 0
    for (psi, n, w) in frontier:
        for s in range(9):
            v = absq(psi[s * 3]) + absq(psi[s * 3 + 1]) + absq(psi[s * 3 + 2])
            if v:
                accf[s] += w * v
        npd, dset, moved, mx, wrapped = _nstat(n)
        dets |= dset
        if mx > maxcell:
            maxcell = mx
        if wrapped:
            wrap_branches += 1
            wrap_cells += wrapped
            wrap_as_welded += sum(1 for c in n if c > 3 and c % 3 == 1)
        for (m, dv) in moved:
            Eb[m] += w * dv
        if npd < 9:
            exit_p += w
    pT = [accf[s] / den for s in range(9)]
    Ebl = [Eb.get(m, Fraction(0)) for m in range(NCELL)]
    return {"p_site": [str(x) for x in pT],
            "ipr": str(sum(x * x for x in pT)),
            "emission_field": [str(x) for x in Ebl],
            "link_class_marginal":
                [str(sum(Ebl[s * 3 + i] for s in range(9))) for i in range(3)],
            "total_emitted": str(sum(Ebl)),
            "admissibility_exit_probability": str(exit_p),
            "max_cell_count": maxcell,
            "branches_carrying_a_wrapped_cell": wrap_branches,
            "wrapped_cells": wrap_cells,
            "wrapped_cells_congruent_to_the_welded_value": wrap_as_welded,
            "det_values_reached": sorted(str(d) for d in dets)}


# ===========================================================================
# SECTION 4.  THE DECOHERENCE FUNCTIONALS -- declared, fiber priced, all run
# ===========================================================================
# THREE, none privileged, each specified here in full and each run on every
# object of every arm of every fiber member.
#
#  D1-IPR-BORN-MENU-SITE.  paper-20's own observable, inherited: the site-basis
#     inverse participation of the Born menu,  D1 = sum_x p(x)^2  with
#     p(x) = sum_l |(C psi)(x,l)|^2 / 9^t the Born menu's site mass.
#
#  D2-OFFDIAG-SITE-MASS.  The off-diagonal coherence mass in the site basis:
#     with rho_xy = sum_l (C psi)(x,l) conj((C psi)(y,l)) the site-reduced
#     density matrix of the Born menu,
#         D2 = sum_{x != y} |rho_xy|^2 / 9^{2t},
#     which is exactly the squared Hilbert-Schmidt distance from the
#     site-dephased state.  THE UNITS ARE DECLARED AND THE DECLARATION IS
#     PRICED: the exact l_1 form sum_{x != y} |rho_xy| is NOT computable in Q
#     on this arena -- |a + b w| is the square root of the rational integer
#     a^2 - a b + b^2 and this unit MEASURES how often that is not a square --
#     so the squared modulus is the exact carrier and the row is stamped.
#
#  D3-RECORD-BORN-DIVERGENCE.  The record-menu/Born-menu divergence, the
#     Delta^B-shaped candidate and the ONLY one of the three that reads the
#     record:  with k_A(l|x) = |(C psi)(x,l)|^2 / (site mass) the Born menu's
#     own kernel and k_B(l|x) = n_l(x) / sum_l n_l(x) the record menu's,
#         D3 = sum_x p(x) . (1/2) sum_l |k_A(l|x) - k_B(l|x)|,
#     the Born-weighted total variation.  This one IS exactly l_1: the
#     absolute value of a RATIONAL is a rational.
#
# Every value is an exact Fraction and a gate scans for anything else.

PAIRS = tuple((x, y) for x in range(9) for y in range(x + 1, 9))
PAIR_INDEX = {p: i for i, p in enumerate(PAIRS)}

D_IDS = ("D1-IPR-BORN-MENU-SITE", "D2-OFFDIAG-SITE-MASS",
         "D3-RECORD-BORN-DIVERGENCE")
D_SHORT = ("D1", "D2", "D3")
D_SPEC = {
    "D1-IPR-BORN-MENU-SITE":
        "sum_x p(x)^2, p(x) the Born menu's site mass -- paper-20's own "
        "observable, inherited",
    "D2-OFFDIAG-SITE-MASS":
        "sum_{x != y} |rho_xy|^2 / 9^{2t}, the site-basis off-diagonal mass "
        "of the Born menu, in SQUARED-MODULUS units because the exact l_1 is "
        "not in Q on this arena",
    "D3-RECORD-BORN-DIVERGENCE":
        "sum_x p(x) . TV(k_A(.|x), k_B(.|x)), the Born-weighted total "
        "variation between the Born menu and the record menu -- exactly l_1",
}


def decoherence(post, Jn, m, n, den):
    """the three declared functionals at one branch-step, exact."""
    p = [Fraction(m[s], den) for s in range(9)]
    d1 = sum(x * x for x in p)
    off = 0
    offrow = [0] * 9
    modsq = []
    pairsq = [0] * len(PAIRS)
    for x in range(9):
        for y in range(9):
            if x == y:
                continue
            tot = Z0
            for l in range(3):
                tot = zadd(tot, zmul(post[x * 3 + l], zconj(post[y * 3 + l])))
            a = absq(tot)
            if x < y:
                pairsq[PAIR_INDEX[(x, y)]] = a
            if a:
                off += a
                offrow[x] += a
                if x < y:
                    modsq.append(a)
    dd = den * den
    d2 = Fraction(off, dd)
    d3 = Fraction(0)
    d3row = [Fraction(0)] * 9
    for x in range(9):
        if m[x] == 0:
            continue
        N = n[x * 3] + n[x * 3 + 1] + n[x * 3 + 2]
        tv = Fraction(0)
        for l in range(3):
            tv += abs(Fraction(Jn[x * 3 + l], m[x]) - Fraction(n[x * 3 + l], N))
        d3row[x] = p[x] * tv / 2
        d3 += d3row[x]
    purity = Fraction(off + sum(m[s] * m[s] for s in range(9)), dd)
    return {"D1": d1, "D2": d2, "D3": d3, "p": p,
            "D1row": [x * x for x in p],
            "D2row": [Fraction(offrow[x], dd) for x in range(9)],
            "D3row": d3row, "modsq": modsq, "purity": purity,
            "pairsq": tuple(pairsq)}


def occupied_links(psi):
    return [frozenset(l for l in range(3) if psi[s * 3 + l] != Z0)
            for s in range(9)]


# TWO OCCUPANCY PREDICATES GOVERN THIS UNIT AND THEY DIFFER BY ONE STEP.
# THE SINGLE-SITE one -- a site occupied on TWO links -- is when the record
# first moves a CELL MASS, so it is what makes the next step's state differ
# between the arms; THE PAIR one -- two sites sharing TWO occupied links -- is
# the predicate D2's off-diagonal blindness turns on.  The prose of the first
# delivery named the first and measured the second; both are measured here.

def double_occupied_sites(psi):
    """the SINGLE-SITE predicate: sites occupied on two or more links."""
    L = occupied_links(psi)
    return [x for x in range(9) if len(L[x]) >= 2]


def cooccupancy(psi):
    """THE PAIR PREDICATE, the mechanism's own: the pairs of sites whose
    occupied-link sets meet in TWO OR MORE links.  Because the coin is unitary
    and site-block-diagonal it cancels out of the DIAGONAL of the site-basis
    density matrix; because it is IN ADDITION the same at every site the
    off-diagonal reduces to
    rho_xy = sum_l w^{n_l(x) - n_l(y)} psi(x,l) conj(psi(y,l)),
    so the record survives ONLY on links occupied at BOTH ends.  A pair meeting
    in at most one link contributes a pure global phase and |rho_xy| cannot see
    the record at all."""
    L = occupied_links(psi)
    return [(x, y) for x in range(9) for y in range(x + 1, 9)
            if len(L[x] & L[y]) >= 2]


def pair_overlaps(psi):
    """the occupied-link overlap of EVERY unordered site pair, in PAIRS order:
    the grain THEOREM B's algebra predicts, 36x finer than the per-object
    census."""
    L = occupied_links(psi)
    return tuple(len(L[x] & L[y]) for (x, y) in PAIRS)


# ===========================================================================
# SECTION 5.  THE GROWTH FUNCTIONALS -- from the machine's own emission law
# ===========================================================================
#  G1-RECORD-CELL   the record itself, n, at the cell grain: THE METRIC.
#  G2-RECORD-SITE   the per-site totals N(x) = sum_l n_l(x).
#  G3-RECORD-LINK   the per-link-class totals sum_x n_l(x).
#  G4-GROWTH-TOTAL  the accumulated growth sum_c (n_c - 1), = t - 1 at a
#                   branch-step of step t on the coupled arm and 0 on the
#                   frozen one.
#  G5-RATE-SITE     the law's OWN site emission rate profile
#                   eps(x) = sum_l p(x) k_1(l|x), the expected number of
#                   division events at x at this step.
#
# The rate is the machine's, not this unit's: eps is read off `emission_weights`
# and never re-derived.  THE ACTUAL/LAW DISTINCTION IS THE TWO-ARM CORE:
# G1..G4 are the record's ACTUAL growth and are identically frozen at the
# welded record on the control; G5 is the LAW's rate and is computed by the
# same code on both arms.

G_IDS = ("G1-RECORD-CELL", "G2-RECORD-SITE", "G3-RECORD-LINK",
         "G4-GROWTH-TOTAL", "G5-RATE-SITE")
G_SHORT = ("G1", "G2", "G3", "G4", "G5")
G_KIND = {"G1-RECORD-CELL": "ACTUAL", "G2-RECORD-SITE": "ACTUAL",
          "G3-RECORD-LINK": "ACTUAL", "G4-GROWTH-TOTAL": "ACTUAL",
          "G5-RATE-SITE": "LAW"}
RES_IDS = ("RES-BRANCH", "RES-SITE", "RES-STEP")


def branch_objects(T, coupled, reading, coin, keep_pairs=False):
    """EVERY BRANCH-STEP of an arm: the frontier at levels 0 .. T-1, each with
    the Born menu it reads and the record it reads that menu on.  Objects are
    DEDUPLICATED by (t, psi, n) -- two branch-steps carrying the same state on
    the same record are the same measurement counted twice, and the honest
    denominator of every relation test is the distinct count."""
    p0 = [Z0] * DIM
    p0[cell(SITE_INDEX[START], INIT_COIN)] = Z1
    frontier = [(tuple(p0), WELDED, Fraction(1))]
    seen = {}
    order = []
    raw = 0
    for t in range(T):
        den = 9 ** (t + 1)
        nxt = []
        for (psi, n, w) in frontier:
            raw += 1
            post = coin_apply(list(psi), list(n), coin)
            Jn = [absq(z) for z in post]
            m = [Jn[s * 3] + Jn[s * 3 + 1] + Jn[s * 3 + 2] for s in range(9)]
            wts, eps, _cs = emission_weights(reading, Jn, n, den)
            key = (t + 1, psi, n)
            got = seen.get(key)
            if got is None:
                D = decoherence(post, Jn, m, n, den)
                o = {"t": t + 1, "w": w, "mult": 1, "den": den,
                     "psi": psi, "n": n, "eps": tuple(eps),
                     "D1": D["D1"], "D2": D["D2"], "D3": D["D3"],
                     "D1row": D["D1row"], "D2row": D["D2row"],
                     "D3row": D["D3row"], "p": D["p"], "modsq": D["modsq"],
                     "purity": D["purity"],
                     "G1": n,
                     "G2": tuple(n[s * 3] + n[s * 3 + 1] + n[s * 3 + 2]
                                 for s in range(9)),
                     "G3": tuple(sum(n[s * 3 + i] for s in range(9))
                                 for i in range(3)),
                     "G4": sum(n) - NCELL,
                     "G5": tuple(eps),
                     "cooc": len(cooccupancy(psi)),
                     "docc": len(double_occupied_sites(psi))}
                if keep_pairs:
                    o["pairsq"] = D["pairsq"]
                    o["ov"] = pair_overlaps(psi)
                seen[key] = o
                order.append(o)
            else:
                got["w"] += w
                got["mult"] += 1
            if t + 1 < T:
                newpsi = shift(post)
                for c in range(NCELL):
                    if wts[c] == 0:
                        continue
                    if coupled:
                        li = list(n)
                        li[c] += 1
                        nn = tuple(li)
                    else:
                        nn = n
                    nxt.append((newpsi, nn, w * wts[c]))
        frontier = nxt
    return order, raw


def site_rows(objs):
    """RES-SITE: one row per (branch-step, site), deduplicated on the whole
    row so the denominator counts measurements and not repetitions."""
    seen = set()
    out = []
    for o in objs:
        n = o["n"]
        for x in range(9):
            row = (o["t"], tuple(n[x * 3:x * 3 + 3]),
                   n[x * 3] + n[x * 3 + 1] + n[x * 3 + 2], o["G3"], o["G4"],
                   o["eps"][x], o["D1row"][x], o["D2row"][x], o["D3row"][x])
            if row in seen:
                continue
            seen.add(row)
            out.append({"t": o["t"], "G1": row[1], "G2": row[2],
                        "G3": row[3], "G4": row[4], "G5": row[5],
                        "D1": row[6], "D2": row[7], "D3": row[8]})
    return out


def step_rows(objs, T=HORIZON):
    """RES-STEP: one row per step, the ensemble aggregate under the branch
    measure.  Five objects: the test below is expected to be VACUOUS and the
    vacuity is DECLARED rather than dressed as a pass."""
    out = []
    for t in range(1, T + 1):
        sel = [o for o in objs if o["t"] == t]
        if not sel:
            continue
        tot = sum(o["w"] for o in sel)
        row = {"t": t, "weight": tot}
        for k in ("D1", "D2", "D3"):
            row[k] = sum(o["w"] * o[k] for o in sel)
        row["G1"] = tuple(sum(o["w"] * (o["n"][c] - 1) for o in sel)
                          for c in range(NCELL))
        row["G2"] = tuple(sum(o["w"] * (o["G2"][s] - 3) for o in sel)
                          for s in range(9))
        row["G3"] = tuple(sum(o["w"] * (o["G3"][i] - 9) for o in sel)
                          for i in range(3))
        row["G4"] = sum(o["w"] * o["G4"] for o in sel)
        row["G5"] = tuple(sum(o["w"] * o["eps"][s] for o in sel)
                          for s in range(9))
        out.append(row)
    return out


# ===========================================================================
# SECTION 6.  THE RELATION -- EXACT, EQUALITY-GATED, FITTED FORMS BARRED
# ===========================================================================
# D is a FUNCTION of G exactly when every G-class carries exactly one D-value.
# Nothing is fitted, nothing is approximated, nothing is regressed: the test
# is the equality of D-values inside a G-class and nothing else.  A test with
# NO non-singleton class decides nothing and is stamped VACUOUS rather than
# EXACT -- that stamp is the honest denominator of this whole section.  A
# partial relation is reported partial WITH ITS FAILURE SET CENSUSED: the
# failing classes, the objects inside them, and the number of distinct
# D-values those classes carry.

def fdep(objs, gk, dk):
    part = defaultdict(set)
    size = Counter()
    for o in objs:
        part[o[gk]].add(o[dk])
        size[o[gk]] += 1
    bad = sorted((g for g in part if len(part[g]) > 1), key=repr)
    nonsing = sum(1 for g in part if size[g] > 1)
    failobj = sum(size[g] for g in bad)
    dvals = sum(len(part[g]) for g in bad)
    if not part:
        word = "EMPTY"
    elif nonsing == 0:
        word = "VACUOUS"
    elif not bad:
        word = "EXACT"
    else:
        word = "PARTIAL"
    # THE STAMP refines PARTIAL where the verdict grammar has no word: a cell
    # in which EVERY non-singleton class fails carries no partial relation at
    # all, and reading it as a partial one over-reports.  The equality-gated
    # verdict word is unchanged -- the stamp is published beside it, and both
    # censuses are published.
    stamp = word
    if word == "PARTIAL" and len(bad) == nonsing:
        stamp = "TOTAL-FAILURE"
    return {"objects": len(objs), "classes": len(part),
            "nonsingleton_classes": nonsing,
            "passing_nonsingleton_classes": nonsing - len(bad),
            "distinct_D_values": len({o[dk] for o in objs}),
            "failing_classes": len(bad),
            "objects_in_failing_classes": failobj,
            "distinct_D_values_in_failing_classes": dvals,
            "verdict": word, "stamp": stamp}


def recount(objs, gk, dk):
    """the failure census, RECOUNTED by a second pass that shares no
    intermediate with `fdep` -- the census gate compares the two.  The
    NON-SINGLETON count is recounted here too: it is the number the VACUOUS
    stamp rests on, and a stamp certified against the pass that produced it is
    certified against itself."""
    byg = defaultdict(list)
    for o in objs:
        byg[o[gk]].append(o[dk])
    fc = 0
    fo = 0
    ns = 0
    for g, vals in byg.items():
        if len(vals) > 1:
            ns += 1
        first = vals[0]
        if any(v != first for v in vals):
            fc += 1
            fo += len(vals)
    return fc, fo, ns


def relation_grid(pools):
    rows = []
    for res, pool in pools:
        for gi, gid in enumerate(G_IDS):
            for di, did in enumerate(D_IDS):
                f = fdep(pool, G_SHORT[gi], D_SHORT[di])
                rows.append({"resolution": res, "growth": gid,
                             "growth_kind": G_KIND[gid], "decoherence": did,
                             **f})
    return rows


IDENTITIES = (
    ("ID-RATE-IS-BORN",
     "the law's site emission rate IS the Born menu's site mass, "
     "eps(x) = p(x), at every site of every object",
     "DEFINITIONAL-THROUGH-THE-LAW"),
    ("ID-RATE-TOTAL",
     "the total emission rate is exactly one division event per coupled "
     "step, sum_x eps(x) = 1, at every object",
     "DEFINITIONAL-THROUGH-THE-LAW"),
    ("ID-D1-IS-SQUARED-RATE",
     "the site-basis inverse participation of the Born menu is the sum of "
     "the squared site emission rates, D1 = sum_x eps(x)^2, at every object",
     "DEFINITIONAL-THROUGH-THE-LAW"),
    ("ID-PURITY-SPLIT",
     "the site-basis purity splits exactly, D1 + D2 = Tr(rho^2), at every "
     "object", "DEFINITIONAL"),
)


def identity_census(objs):
    rows = []
    for oid, stmt, kind in IDENTITIES:
        bad = 0
        checks = 0
        for o in objs:
            if oid == "ID-RATE-IS-BORN":
                for s in range(9):
                    checks += 1
                    if o["eps"][s] != o["p"][s]:
                        bad += 1
            elif oid == "ID-RATE-TOTAL":
                checks += 1
                if sum(o["eps"]) != 1:
                    bad += 1
            elif oid == "ID-D1-IS-SQUARED-RATE":
                checks += 1
                if o["D1"] != sum(e * e for e in o["eps"]):
                    bad += 1
            else:
                checks += 1
                if o["D1"] + o["D2"] != o["purity"]:
                    bad += 1
        rows.append({"id": oid, "statement": stmt, "kind": kind,
                     "checks": checks, "violations": bad, "holds": bad == 0})
    return rows


def domination(co_steps, fz_steps):
    """MONOTONE DOMINATION WITH EXACT WITNESSES.  For each functional, the
    ensemble value on the coupled arm is compared with the frozen control's at
    every step; the direction is reported per step and a domination is claimed
    only when every SEPARATING step agrees, with the separating steps named."""
    rows = []
    for dk in D_SHORT:
        cmpr = []
        for c, f in zip(co_steps, fz_steps):
            s = "=" if c[dk] == f[dk] else (">" if c[dk] > f[dk] else "<")
            cmpr.append({"t": c["t"], "coupled": str(c[dk]),
                         "frozen": str(f[dk]), "direction": s})
        sep = [r for r in cmpr if r["direction"] != "="]
        up = [r["t"] for r in sep if r["direction"] == ">"]
        dn = [r["t"] for r in sep if r["direction"] == "<"]
        if sep and not dn:
            word = "COUPLED-DOMINATES"
        elif sep and not up:
            word = "FROZEN-DOMINATES"
        elif sep:
            word = "NO-DOMINATION"
        else:
            word = "NO-SEPARATION"
        rows.append({"functional": dk, "per_step": cmpr,
                     "separating_steps": [r["t"] for r in sep],
                     "coupled_above_at": up, "coupled_below_at": dn,
                     "verdict": word,
                     "witness": ("steps %s against %s" % (up, dn))
                                if word == "NO-DOMINATION" else
                                ("steps %s" % (up or dn))})
    return rows


# ===========================================================================
# SECTION 7.  FORCEDNESS -- the coin fiber, the reading fiber, the exclusion
# ===========================================================================
# The fibers are run as DECLARED AXES, not as a product, and this unit says so:
# all six members of the COIN fiber are executed at the delivered reading, and
# both members of the READING fiber are executed at the delivered coin.  The
# cross-product is NOT claimed.
#
# THE FROZEN EXCLUSION IS A GATE.  A relation that holds identically on the
# frozen stage is NOT a gravitational-decoherence relation, because the frozen
# stage's record never grows: any relation still true there is a relation about
# the walk and the law rather than about the coupling.  Every EXACT cell and
# every holding IDENTITY is therefore re-evaluated on the control and excluded
# if it survives.

def separation_ladder(co_objs, fz_objs, T=HORIZON):
    """the first step at which each functional's VALUE SET on the coupled arm
    differs from the frozen control's -- a per-object statement, not an
    average."""
    rows = []
    for dk in D_SHORT:
        first = None
        per = []
        for t in range(1, T + 1):
            ca = {o[dk] for o in co_objs if o["t"] == t}
            fz = {o[dk] for o in fz_objs if o["t"] == t}
            same = ca == fz
            per.append({"t": t, "coupled_values": len(ca),
                        "frozen_values": len(fz), "identical": same})
            if not same and first is None:
                first = t
        rows.append({"functional": dk, "first_separating_step": first,
                     "per_step": per})
    return rows


def occupancy_thresholds(objs, T=HORIZON):
    """BOTH declared predicates, measured step by step: the first step at which
    some object carries a site occupied on two links, and the first at which
    some object carries a PAIR of sites sharing two occupied links."""
    single = None
    pair = None
    for t in range(1, T + 1):
        sel = [o for o in objs if o["t"] == t]
        if single is None and any(o["docc"] for o in sel):
            single = t
        if pair is None and any(o["cooc"] for o in sel):
            pair = t
    return single, pair


def cooccupancy_pairs_at(objs, t):
    """the DISTINCT co-occupying site pairs the arm carries at one step -- the
    COUNT, which the fiber census below measures to be coin-relative even
    though the THRESHOLD is not."""
    seen = set()
    for o in objs:
        if o["t"] != t:
            continue
        for pr in cooccupancy(o["psi"]):
            seen.add(pr)
    return len(seen)


def fiber_row(cname, coin, reading, T=HORIZON):
    co, raw_c = branch_objects(T, True, reading, coin)
    fz, raw_f = branch_objects(T, False, reading, coin)
    sep = separation_ladder(co, fz)
    ident = identity_census(co + fz)
    cells = []
    for gi, gid in enumerate(G_IDS):
        for di, did in enumerate(D_IDS):
            cells.append({"growth": gid, "decoherence": did,
                          "coupled": fdep(co, G_SHORT[gi],
                                          D_SHORT[di])["verdict"],
                          "frozen": fdep(fz, G_SHORT[gi],
                                         D_SHORT[di])["verdict"]})
    sc, pc = occupancy_thresholds(co, T)
    sf, pf = occupancy_thresholds(fz, T)
    return {
        "coin": cname, "reading": reading,
        "is_unitary_exactly": coin_unitary_exactly(coin),
        "is_s3_covariant": coin_s3_covariant(coin),
        "three_C_numerators": [[list(z) for z in row] for row in coin],
        "branch_steps_coupled_raw": raw_c,
        "branch_steps_coupled_distinct": len(co),
        "branch_steps_frozen_raw": raw_f,
        "branch_steps_frozen_distinct": len(fz),
        "separation_ladder": {r["functional"]: r["first_separating_step"]
                              for r in sep},
        "identities_all_hold": all(r["holds"] for r in ident),
        "cells": cells,
        # THE THRESHOLD IS IN THE SEALED DIGEST (K2 M4): the prediction row
        # claims it across the whole fiber, so the fiber census must carry it.
        "single_site_threshold_coupled": sc,
        "single_site_threshold_frozen": sf,
        "cooccupancy_threshold_coupled": pc,
        "cooccupancy_threshold_frozen": pf,
        # ... and the COUNT is published beside it, because the count is
        # coin-relative and only the threshold is invariant.  The control's
        # count is a single object's, so it is the unambiguous carrier.
        "cooccupancy_pairs_on_the_frozen_object_at_the_horizon":
            max([o["cooc"] for o in fz if o["t"] == T] or [0]),
        "distinct_cooccupancy_pairs_coupled_at_the_horizon":
            cooccupancy_pairs_at(co, T),
        "cell_signature": digest(
            [(c["growth"], c["decoherence"], c["coupled"], c["frozen"])
             for c in cells]
            + [("SINGLE-SITE-THRESHOLD", str(sc), str(sf)),
               ("COOCCUPANCY-THRESHOLD", str(pc), str(pf))]),
        "frozen_distinct_is_one_per_level": len(fz) == T,
    }


# ===========================================================================
# SECTION 8.  THE BLINDNESS MECHANISM -- measured on foreign count fields
# ===========================================================================
# The mechanism is not argued from the source; it is MEASURED, exactly the way
# paper-20 measured its own count-blindness: each object's menu is re-read on
# DECLARED FOREIGN count fields -- fields this run never generates, two of
# which are not even admissible -- and the functionals that move are counted.
# The fields are paper-20's own declared set, cited and adopted unchanged.

FOREIGN_FIELDS = (
    ("STALE", tuple(1 + (1 if m in (0, 4, 11, 20, 26) else 0)
                    for m in range(NCELL))),
    ("ALL-TWO", tuple([2] * NCELL)),
    ("INADMISSIBLE-ONE-CELL", tuple(4 if m == 2 else 1 for m in range(NCELL))),
    ("LADDERED", tuple(1 + (m % 5) for m in range(NCELL))),
    ("ZERO-AT-ONE-CELL", tuple(0 if m == 7 else 1 for m in range(NCELL))),
)


def blindness_census(objs, coin, reading=DELIVERED_READING):
    """the delivered per-OBJECT census, and -- at 36x its evidence -- the
    per-SITE-PAIR census the algebra actually predicts, plus the LAW's own
    growth functional G5 run against the same fields."""
    rows = []
    pair = {"pairs_meeting_in_at_most_one_occupied_link":
            {"checks": 0, "moved": 0},
            "pairs_meeting_in_two_or_more_occupied_links":
            {"checks": 0, "moved": 0}}
    g5 = {"checks": 0, "moved": 0}
    for fname, field in FOREIGN_FIELDS:
        moved = Counter()
        moved_without_cooc = Counter()
        checks = 0
        for o in objs:
            den = o["den"]
            post = coin_apply(list(o["psi"]), list(field), coin)
            Jn = [absq(z) for z in post]
            m = [Jn[s * 3] + Jn[s * 3 + 1] + Jn[s * 3 + 2] for s in range(9)]
            D = decoherence(post, Jn, m, field, den)
            for k in D_SHORT:
                checks += 1
                if D[k] != o[k]:
                    moved[k] += 1
                    if not o["cooc"]:
                        moved_without_cooc[k] += 1
            ov = o["ov"]
            base = o["pairsq"]
            now = D["pairsq"]
            for pi in range(len(PAIRS)):
                cls = ("pairs_meeting_in_at_most_one_occupied_link"
                       if ov[pi] <= 1 else
                       "pairs_meeting_in_two_or_more_occupied_links")
                pair[cls]["checks"] += 1
                if now[pi] != base[pi]:
                    pair[cls]["moved"] += 1
            _w, epsf, _c = emission_weights(reading, Jn, field, den)
            g5["checks"] += 1
            if tuple(epsf) != o["G5"]:
                g5["moved"] += 1
        rows.append({"field": fname,
                     "is_admissible": all(admissible(site_counts(field, s))
                                          for s in range(9)),
                     "is_the_welded_record": field == WELDED,
                     "is_generated_by_this_run": False,
                     "checks": checks,
                     "moved": {k: moved.get(k, 0) for k in D_SHORT},
                     "moved_without_a_cooccupancy_pair":
                         {k: moved_without_cooc.get(k, 0) for k in D_SHORT}})
    for cls in pair:
        pair[cls]["static"] = pair[cls]["checks"] - pair[cls]["moved"]
    return rows, pair, g5


def site_dependent_census(objs, coins, reading=DELIVERED_READING):
    """THEOREM A's HYPOTHESIS, ISOLATED AND MEASURED.  The same objects, the
    same foreign fields, and a coin that is block-diagonal in the site index
    and unitary on each block but DIFFERENT AT EVERY SITE.  If the diagonal
    blindness needed site-uniformity, D1 would move here."""
    base = []
    for o in objs:
        den = o["den"]
        post = coin_apply_sitewise(list(o["psi"]), list(o["n"]), coins)
        Jn = [absq(z) for z in post]
        m = [Jn[s * 3] + Jn[s * 3 + 1] + Jn[s * 3 + 2] for s in range(9)]
        D = decoherence(post, Jn, m, o["n"], den)
        base.append((D["D1"], D["D2"], tuple(D["p"])))
    checks = 0
    d1_moved = 0
    d2_moved = 0
    marg_moved = 0
    d1_values = set()
    d2_values = set()
    for _fname, field in FOREIGN_FIELDS:
        for oi, o in enumerate(objs):
            den = o["den"]
            post = coin_apply_sitewise(list(o["psi"]), list(field), coins)
            Jn = [absq(z) for z in post]
            m = [Jn[s * 3] + Jn[s * 3 + 1] + Jn[s * 3 + 2] for s in range(9)]
            D = decoherence(post, Jn, m, field, den)
            b1, b2, bp = base[oi]
            checks += 1
            if D["D1"] != b1:
                d1_moved += 1
            if D["D2"] != b2:
                d2_moved += 1
            if tuple(D["p"]) != bp:
                marg_moved += 1
            if o["t"] == HORIZON:
                d1_values.add(D["D1"])
                d2_values.add(D["D2"])
    uni = all(coins[s] == coins[0] for s in range(9))
    return {"coin": "SITE-DEPENDENT: the declared fiber cycled over the nine "
                    "sites -- block-diagonal and unitary on each block, and "
                    "NOT the same at every site",
            "is_site_uniform": uni,
            "every_block_unitary": all(coin_unitary_exactly(c) for c in coins),
            "object_field_pairs": checks,
            "site_marginal_moved": marg_moved,
            "D1_moved": d1_moved, "D2_moved": d2_moved,
            "distinct_D1_at_the_horizon": len(d1_values),
            "distinct_D2_at_the_horizon": len(d2_values)}


def symbolic_cancellation():
    """THE CANCELLATION VERIFIED AS ALGEBRA, not as a sample.  With M = 3C the
    coin numerator (M M* = 9 I) and post(x,l) = sum_j M[l][j] w^{n_j(x)}
    psi(x,j), the claim is

        rho_xy = 9 . sum_j w^{n_j(x) - n_j(y)} psi(x,j) conj(psi(y,j)).

    Both sides are bilinear in (psi_x, conj psi_y), so verifying them on the 9
    monomial pairs that span that form PROVES the identity for every psi.  The
    verification runs over all 729 residue pairs, for every declared coin,
    coefficient by coefficient in Z[w]."""
    residues = [(a, b, c) for a in range(3) for b in range(3) for c in range(3)]
    rows = []
    for cname, M in COIN_FIBER:
        ident = 0
        coeff = 0
        bad = 0
        for na in residues:
            for nb in residues:
                ident += 1
                for j0 in range(3):
                    for k0 in range(3):
                        ax = [zmul(Z1 if j == j0 else Z0, WPOW[na[j] % 3])
                              for j in range(3)]
                        ay = [zmul(Z1 if j == k0 else Z0, WPOW[nb[j] % 3])
                              for j in range(3)]
                        lhs = Z0
                        for l in range(3):
                            ox = Z0
                            oy = Z0
                            for j in range(3):
                                ox = zadd(ox, zmul(M[l][j], ax[j]))
                                oy = zadd(oy, zmul(M[l][j], ay[j]))
                            lhs = zadd(lhs, zmul(ox, zconj(oy)))
                        rhs = (zmul((9, 0), WPOW[(na[j0] - nb[j0]) % 3])
                               if j0 == k0 else Z0)
                        coeff += 1
                        if lhs != rhs:
                            bad += 1
        rows.append({"coin": cname, "residue_pair_identities": ident,
                     "coefficient_checks": coeff, "mismatches": bad})
    return rows


# THE THIRD CHANNEL (K2 M6/THEOREM C).  `coin_apply` reads WPOW[n % 3]: w is a
# primitive CUBE root of unity, so the record enters the dynamics ONLY as
# n mod 3.  Every psi-internal functional therefore sees at most a Z/3 shadow
# of the metric.  The two declared perturbations below are CONGRUENT BUT
# DIFFERENT records -- same residue at every cell, different record -- and the
# census asks whether ANY declared functional distinguishes them.
CONGRUENT_SHIFTS = (
    ("PLUS-3-AT-ONE-CELL", tuple(3 if c == 0 else 0 for c in range(NCELL))),
    ("PLUS-3-AT-EVERY-CELL", tuple(3 for _c in range(NCELL))),
)


def residue_census(objs, coin, arm_ladder, T=HORIZON):
    """THE MOD-3 CHANNEL, MEASURED -- at BOTH grains.

    THE RECORD THE MACHINE WRITES is censused on the anchored ladder (the
    frontier's own records, level by level); THE RECORD THE COIN READS is
    censused on this unit's objects, which read the record of the level below.
    The two grains differ by exactly one step, and that is where the finding
    is: the wraparound is WRITTEN inside the declared horizon and READ by no
    object of it."""
    rows = []
    for sname, shift_vec in CONGRUENT_SHIFTS:
        moved = Counter()
        checks = 0
        congruent = True
        different = 0
        for o in objs:
            den = o["den"]
            field = tuple(o["n"][c] + shift_vec[c] for c in range(NCELL))
            if any((field[c] - o["n"][c]) % 3 for c in range(NCELL)):
                congruent = False
            if field != o["n"]:
                different += 1
            post = coin_apply(list(o["psi"]), list(field), coin)
            Jn = [absq(z) for z in post]
            m = [Jn[s * 3] + Jn[s * 3 + 1] + Jn[s * 3 + 2] for s in range(9)]
            D = decoherence(post, Jn, m, field, den)
            for k in D_SHORT:
                checks += 1
                if D[k] != o[k]:
                    moved[k] += 1
        rows.append({"field": sname,
                     "congruent_at_every_cell": congruent,
                     "objects_whose_record_actually_changed": different,
                     "checks": checks,
                     "moved": {k: moved.get(k, 0) for k in D_SHORT}})
    # THE WRAPAROUND, censused at the delivered horizon, on both grains.
    ladder = []
    for t in range(1, T + 1):
        sel = [o for o in objs if o["t"] == t]
        lv = arm_ladder[t]
        read_mx = max((max(o["n"]) for o in sel), default=0)
        read_objs = sum(1 for o in sel if max(o["n"]) > 3)
        read_cells = sum(sum(1 for c in o["n"] if c > 3) for o in sel)
        ladder.append({
            "t": t,
            "written_max_cell_count": lv["max_cell_count"],
            "written_branches_carrying_a_wrapped_cell":
                lv["branches_carrying_a_wrapped_cell"],
            "written_wrapped_cells": lv["wrapped_cells"],
            "written_wrapped_cells_congruent_to_the_welded_value":
                lv["wrapped_cells_congruent_to_the_welded_value"],
            "objects_reading_the_record_here": len(sel),
            "read_max_cell_count": read_mx,
            "objects_reading_a_wrapped_cell": read_objs,
            "wrapped_cells_read": read_cells})
    wr = [r["t"] for r in ladder if r["written_wrapped_cells"]]
    rd = [r["t"] for r in ladder if r["wrapped_cells_read"]]
    first_written = min(wr) if wr else None
    first_read = min(rd) if rd else (first_written + 1 if first_written
                                     else None)
    return rows, ladder, first_written, first_read


def cooccupancy_ladder(objs, T=HORIZON):
    rows = []
    for t in range(1, T + 1):
        sel = [o for o in objs if o["t"] == t]
        rows.append({"t": t, "objects": len(sel),
                     "with_a_cooccupancy_pair": sum(1 for o in sel
                                                    if o["cooc"])})
    hit = [r["t"] for r in rows if r["with_a_cooccupancy_pair"]]
    return rows, (min(hit) if hit else None)


def l1_price(objs):
    """the price of D2's squared-modulus declaration, MEASURED: how many of
    the off-diagonal |rho_xy|^2 are not perfect squares, i.e. how many exact
    moduli are irrational and therefore outside this unit's arithmetic."""
    from math import isqrt
    tot = 0
    sq = 0
    vals = set()
    for o in objs:
        for a in o["modsq"]:
            tot += 1
            vals.add(a)
            if isqrt(a) ** 2 == a:
                sq += 1
    # THE HONEST DENOMINATOR (K1 MINOR-5): `modsq` carries the NONZERO entries
    # only.  The full unordered off-diagonal population is 36 per object and
    # the missing entries are exact zeros, which are rational.  Both fractions
    # are published and the paper takes the larger denominator.
    pop = len(objs) * len(PAIRS)
    return {"offdiagonal_entries": tot, "perfect_squares": sq,
            "irrational_moduli": tot - sq, "distinct_values": len(vals),
            "offdiagonal_population": pop,
            "zero_entries_which_are_rational": pop - tot,
            "rational_moduli_over_the_full_population": pop - (tot - sq),
            "exact_l1_is_in_Q": tot == sq}


# ===========================================================================
# SECTION 9 -- 11.  the census, the gates, the verdict, the paper, the seal
# ===========================================================================

NUMREG = set()


def reg(*vals):
    for v in vals:
        NUMREG.add(str(v))
    return vals[0] if len(vals) == 1 else vals


def com(n):
    return "{:,}".format(n)


RAW = {}

VERBATIM = [
    ("V-PIN-FITTED", "A-PIN",
     "Fitted forms are BARRED -- only exact relations (equalities, monotone "
     "dominations with exact witnesses, or exact functional dependence gated "
     "by equality) may be claimed.", "G-NO-FITTED-FORM"),
    ("V-PIN-FROZEN", "A-PIN",
     "THE FROZEN CONTROL is mandatory: on the frozen stage records never grow "
     "-- the decoherence functionals' behavior there is the it-can-differ arm "
     "(a relation that holds identically frozen is NOT a "
     "gravitational-decoherence relation).", "G-FROZEN-EXCLUSION"),
    ("V-PIN-SI", "A-PIN",
     "it is entered in the structural-prediction ledger in substrate-native "
     "form (counts and exact rationals -- NO SI numbers, NO experimental-value "
     "claims; the DP citation stays shape-only).", "G-WALL-NO-SI"),
    ("V-P20-MENU", "A-P20",
     "The menu at site x is the three link traversals and the weight q(l|x) "
     "is the post-coin Born weight", "G-PARENT-REPRODUCED"),
    ("V-P20-UPDATE", "A-P20",
     "A division event on cell (x, l) increments n_l(x) by one.",
     "G-PARENT-REPRODUCED"),
    ("V-P20-CONTROL", "A-P20",
     "The frozen-stage control is the same walk, the same emission rule and "
     "the same branching, on counts that never update.", "G-FROZEN-CONTROL"),
    ("V-P20-COIN", "A-P20",
     "36 solutions over the arena's own (1/3)Z[w], falling into 6 classes up "
     "to a global phase, of which exactly 1 is +/- Grover", "G-COIN-FIBER"),
    ("V-P20-STALE", "A-P20",
     "no closure internal to the state at a single time can distinguish a "
     "frozen stage from a coupled one", "G-BLINDNESS-D1"),
    ("V-GITER-K1", "A-GITER", "k_1", "G-LAW-KERNEL"),
    ("V-L1-FOURTH", "A-L1",
     "**fourth form, outside paper 8's three**, and its admissibility is",
     "G-WALL-L1"),
    ("V-CAT-BHS", "A-CAT",
     "a Poisson sprinkling admits **no Lorentz-invariant finite-valency "
     "graph**", "G-WALL-BHS"),
    ("V-CAT-KR", "A-CAT",
     "must carry a Kleitman–Rothschild height control", "G-WALL-KR"),
]

# the #62 anchors whose needle is a SHORT canonical fragment: they are matched
# with the floor lifted, and each is perturbed inside its own gate.
SHORT_ANCHORS = {"V-GITER-K1"}

WALL_FORBIDDEN = {
    "G-WALL-BHS": ("sprinkling", "poisson process", "boosted rest frame",
                   "lorentz invariant sprinkling"),
    "G-WALL-KR": ("myrheim-meyer", "myrheim meyer", "kleitman-rothschild",
                  "dimension estimator"),
    "G-WALL-COSMO": ("cosmological expansion", "dark energy", "hubble",
                     "continuum limit is reached", "big bang"),
    "G-WALL-NO-SI": ("kilogram", "kilograms", " joule", "kelvin", "nanogram",
                     "picogram", "milligram", " gev", " kev", " ev ",
                     "planck mass", "planck length", "planck time",
                     "hbar", "newton per", "second^-1", "per second",
                     "experimental bound", "experimentally measured",
                     "collapse rate in kilogram"),
}
# DECLARED OUT with the reason printed: this unit's own vocabulary.
NEEDLES_DECLARED_OUT = {
    "horizon": "this unit's own name for the declared finite number of "
               "coupled steps, and the gravity law's own relative-horizon "
               "index",
    "rate": "the emission RATE is one of this unit's two declared growth "
            "functionals; a scan firing on it would fire on the pin's own "
            "vocabulary",
    "mass": "the off-diagonal coherence MASS and the menu MASS are declared "
            "objects of this unit and of paper-16's law",
}

NUM_ALLOW = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
             "10", "11", "12", "13", "14", "20", "25", "27", "62", "82",
             "87", "91", "119", "125", "148", "160", "168", "187", "192",
             "205", "34", "24", "46", "13", "15", "16", "17", "18", "19",
             "21", "22", "23", "28", "29", "30", "31", "32", "33", "36",
             "1296", "2026", "1", "2895"}


def raw_census():
    """everything heavy, computed ONCE.  The mutant sweep re-runs the GATE
    layer, not the census: every falsifier in this file acts on what a gate is
    handed rather than on the arithmetic that produced it, except the few that
    must move the physics, which move it on an object small enough to rebuild."""
    if RAW:
        return RAW
    say("  .. rebuilding the coupled machine and anchoring it")
    arms = {}
    for nm, coupled, reading in (("A-COUPLED", True, "A"),
                                 ("A-FROZEN", False, "A"),
                                 ("B-COUPLED", True, "B")):
        arms[nm] = run_arm(HORIZON, coupled, reading, GROVER_Z, light=True)
    RAW["arms"] = arms
    say("  .. the delivered configuration: coin %s, reading %s"
        % (DELIVERED_COIN, DELIVERED_READING))
    co, raw_c = branch_objects(HORIZON, True, DELIVERED_READING, GROVER_Z,
                               keep_pairs=True)
    fz, raw_f = branch_objects(HORIZON, False, DELIVERED_READING, GROVER_Z)
    RAW["co"] = co
    RAW["fz"] = fz
    RAW["raw_c"] = raw_c
    RAW["raw_f"] = raw_f
    RAW["co_site"] = site_rows(co)
    RAW["fz_site"] = site_rows(fz)
    RAW["co_step"] = step_rows(co)
    RAW["fz_step"] = step_rows(fz)
    say("  .. the relation grid")
    RAW["grid_coupled"] = relation_grid(
        (("RES-BRANCH", co), ("RES-SITE", RAW["co_site"]),
         ("RES-STEP", RAW["co_step"])))
    RAW["grid_frozen"] = relation_grid(
        (("RES-BRANCH", fz), ("RES-SITE", RAW["fz_site"]),
         ("RES-STEP", RAW["fz_step"])))
    RAW["identities_coupled"] = identity_census(co)
    RAW["identities_frozen"] = identity_census(fz)
    RAW["separation"] = separation_ladder(co, fz)
    RAW["domination"] = domination(RAW["co_step"], RAW["fz_step"])
    say("  .. the blindness census on the declared foreign count fields")
    RAW["blindness"], RAW["pair_census"], RAW["g5_blindness"] = \
        blindness_census(co, GROVER_Z)
    RAW["cooc_rows"], RAW["cooc_threshold"] = cooccupancy_ladder(co)
    RAW["cooc_rows_frozen"], RAW["cooc_threshold_frozen"] = \
        cooccupancy_ladder(fz)
    RAW["occ_coupled"] = occupancy_thresholds(co)
    RAW["occ_frozen"] = occupancy_thresholds(fz)
    RAW["l1"] = l1_price(co)
    say("  .. THEOREM A isolated: the same census under a site-DEPENDENT coin")
    RAW["site_dependent"] = site_dependent_census(co, SITE_DEPENDENT_COINS)
    say("  .. THEOREM B as algebra: the cancellation, coefficient by "
        "coefficient")
    RAW["symbolic"] = symbolic_cancellation()
    say("  .. THE THIRD CHANNEL: the mod-3 residue reading and its wraparound")
    (RAW["residue"], RAW["residue_ladder"], RAW["wrap_written_at"],
     RAW["wrap_read_at"]) = residue_census(
         co, GROVER_Z, arms["A-COUPLED"]["ladder"])
    say("  .. the coin fiber (6 members) and the reading fiber (2 members)")
    fiber = []
    for cname, coin in COIN_FIBER:
        fiber.append(fiber_row(cname, coin, DELIVERED_READING))
    for reading in READING_FIBER:
        if reading == DELIVERED_READING:
            continue
        fiber.append(fiber_row(DELIVERED_COIN, GROVER_Z, reading))
    RAW["fiber"] = fiber
    return RAW


# --- the anchor set: the parent's own published values, re-derived here ------

def anchor_values(arms):
    """what an INDEPENDENT re-implementation must reproduce.  Each row names a
    path in paper-20's committed receipt and the value this unit's own rebuild
    produced; the gate compares them at EQUALITY, per object (#87)."""
    rows = []

    def add(what, path, mine, token_key=None):
        rows.append({"what": what, "receipt_path": path, "rebuilt": str(mine),
                     "token_key": token_key})

    for nm, key in (("A-COUPLED", "A-COUPLED"), ("A-FROZEN", "A-FROZEN"),
                    ("B-COUPLED", "B-COUPLED")):
        lv = arms[nm]["levels"]
        add("%s branches per level" % nm,
            "ensemble/arms/%s/levels" % key,
            [x["branches"] for x in lv])
    add("coupled Born-menu inverse participation at the horizon",
        "nontriviality/observables", arms["A-COUPLED"]["ladder"][HORIZON]["ipr"])
    add("frozen Born-menu inverse participation at the horizon",
        "nontriviality/observables", arms["A-FROZEN"]["ladder"][HORIZON]["ipr"])
    add("coupled admissibility-exit probability, Born menu",
        "ladder/exit_probability_at_horizon/A",
        arms["A-COUPLED"]["ladder"][HORIZON]["admissibility_exit_probability"])
    add("coupled admissibility-exit probability, record menu",
        "ladder/exit_probability_at_horizon/B",
        arms["B-COUPLED"]["ladder"][HORIZON]["admissibility_exit_probability"])
    add("frozen admissibility-exit probability",
        "ladder/rows", arms["A-FROZEN"]["ladder"][HORIZON]
        ["admissibility_exit_probability"], "frozen_exit")
    add("coupled link-class marginal at the horizon",
        "nontriviality/observables",
        arms["A-COUPLED"]["ladder"][HORIZON]["link_class_marginal"])
    add("coupled site distribution at the horizon",
        "nontriviality/observables",
        arms["A-COUPLED"]["ladder"][HORIZON]["p_site"])
    add("frozen site distribution at the horizon",
        "nontriviality/observables",
        arms["A-FROZEN"]["ladder"][HORIZON]["p_site"])
    add("maximum cell count on the ladder", "ladder/rows",
        [arms["A-COUPLED"]["ladder"][t]["max_cell_count"] for t in LADDER],
        "max_cell_count")
    add("branch-step count of the coupled arm",
        "ensemble/arms/A-COUPLED/checks/norm",
        sum(x["branches"] for x in arms["A-COUPLED"]["levels"][:-1]) + 1)
    add("branch-step count of the frozen arm",
        "ensemble/arms/A-FROZEN/checks/norm",
        sum(x["branches"] for x in arms["A-FROZEN"]["levels"][:-1]) + 1)
    return rows


def locate_in_parent(rows, blob):
    """#62-style LOCATION: every rebuilt value must be findable VERBATIM in the
    parent's committed receipt bytes.  This is the leg that makes the anchor a
    comparison against the COMMITTED OBJECT rather than against a number this
    file typed."""
    hay = blob.decode("utf-8")
    out = []
    for r in rows:
        v = r["rebuilt"]
        toks = re.findall(r"-?\d+(?:/\d+)?", v)
        found = all(('"%s"' % t) in hay or (": %s" % t) in hay
                    or (" %s," % t) in hay or ("%s\n" % t) in hay
                    for t in toks)
        # A ROW WHOSE EVERY TOKEN IS A SINGLE DIGIT LOCATES IN ESSENTIALLY ANY
        # JSON (K1 MINOR-6).  Such a row is located instead against ITS OWN
        # RECEIPT KEY, in order: `"<key>": <token>` must occur for every token
        # of the row, each after the last -- which a perturbed ladder fails.
        longest = max((len(t) for t in toks), default=0)
        how = "tokens of length %d" % longest
        if longest < 4:
            key = r.get("token_key")
            how = "the key `%s` carrying each token in order" % key
            pos = 0
            for t in toks:
                j = -1
                for form in ('"%s": %s,' % (key, t), '"%s": %s\n' % (key, t),
                             '"%s": "%s"' % (key, t)):
                    k = hay.find(form, pos)
                    if k >= 0 and (j < 0 or k < j):
                        j = k
                if j < 0:
                    found = False
                    break
                pos = j + 1
        out.append({"what": r["what"], "tokens": len(toks),
                    "longest_token": longest, "located_by": how,
                    "located": found})
    return out


def parent_receipt_check(rows, blob):
    """the EQUALITY leg: the parent's receipt is parsed and the declared paths
    are compared against this unit's rebuilt values."""
    P = json.loads(blob.decode("utf-8"))
    checks = []
    arms = P["ensemble"]["arms"]
    obs = {(o["observable"], o["reading"]): o for o in
           P["nontriviality"]["observables"]}
    want = {
        "A-COUPLED branches per level":
            [x["branches"] for x in arms["A-COUPLED"]["levels"]],
        "A-FROZEN branches per level":
            [x["branches"] for x in arms["A-FROZEN"]["levels"]],
        "B-COUPLED branches per level":
            [x["branches"] for x in arms["B-COUPLED"]["levels"]],
        "coupled Born-menu inverse participation at the horizon":
            obs[("ipr", "A")]["coupled"],
        "frozen Born-menu inverse participation at the horizon":
            obs[("ipr", "A")]["frozen"],
        "coupled admissibility-exit probability, Born menu":
            P["ladder"]["exit_probability_at_horizon"]["A"],
        "coupled admissibility-exit probability, record menu":
            P["ladder"]["exit_probability_at_horizon"]["B"],
        "frozen admissibility-exit probability":
            [r for r in P["ladder"]["rows"]
             if r["reading"] == "A" and r["horizon"] == HORIZON][0]
            ["frozen_exit"],
        "coupled link-class marginal at the horizon":
            obs[("link_class_marginal", "A")]["coupled"],
        "coupled site distribution at the horizon":
            obs[("p_site", "A")]["coupled"],
        "frozen site distribution at the horizon":
            obs[("p_site", "A")]["frozen"],
        "maximum cell count on the ladder":
            [r["max_cell_count"] for r in P["ladder"]["rows"]
             if r["reading"] == "A"],
        "branch-step count of the coupled arm":
            arms["A-COUPLED"]["checks"]["norm"],
        "branch-step count of the frozen arm":
            arms["A-FROZEN"]["checks"]["norm"],
    }
    for r in rows:
        w = want.get(r["what"])
        checks.append({"what": r["what"], "receipt_path": r["receipt_path"],
                       "parent": str(w), "rebuilt": r["rebuilt"],
                       "equal": str(w) == r["rebuilt"]})
    return checks


# --- the measure ledger (E-24) ----------------------------------------------

BRANCH_MEASURE = (
    "THE BRANCH MEASURE: the emission law's own product measure over the "
    "branching tree -- at each coupled step a branch of weight w splits into "
    "one child of weight w . p(x) . k_1(l|x) per emitted cell, and the level "
    "masses are measured to be exactly 1")
MEASURE_LEDGER = {
    "rebuild": BRANCH_MEASURE,
    "ensemble": BRANCH_MEASURE,
    "machine": BRANCH_MEASURE,
    "functionals": BRANCH_MEASURE,
    "growth": BRANCH_MEASURE,
    "relation": "COUNTING-ONLY: class and object counts over the declared "
                "object sets, carrying no probability",
    "forcedness": "COUNTING-ONLY: fiber-member counts and verdict words",
    "exclusion": BRANCH_MEASURE,
    "mechanism": "COUNTING-ONLY: how many objects move under a declared "
                 "foreign count field",
    "prediction": "COUNTING-ONLY: step indices and fiber counts",
    "counts": "COUNTING-ONLY: the run's own cardinalities",
    "verdict": BRANCH_MEASURE,
    "walls": "COUNTING-ONLY: needle and scan counts",
    "measure_ledger": "COUNTING-ONLY: this ledger",
}
FRACTION_RE = re.compile(r"^-?\d+/\d+$")

# --- the choice inventory (rendered as a table, and gated) -------------------
# Item 12 is the one the first delivery left out and it is the choice that
# decides the head: the frozen bar is applied to EXACT cells only.

CHOICES = (
    ("F1-MACHINE", "INHERITED", 1,
     "paper-20's walk, emission law and update semantics, re-implemented from "
     "the committed spec and anchored at its bytes", False),
    ("F2-COIN", "DECLARED, WHOLE FIBER RUN", len(COIN_IDS),
     "+/- Grover and the four hidden S_3-covariant classes; all six executed",
     False),
    ("F3-READING", "DECLARED, WHOLE FIBER RUN", len(READING_FIBER),
     "Born menu against record menu; both executed", False),
    ("F4-HORIZON", "DECLARED", 1,
     "T = 5, the parent's; the whole ladder published", False),
    ("F5-D-SET", "DECLARED", len(D_IDS),
     "the three decoherence functionals; none privileged, all run", False),
    ("F6-D2-UNITS", "DECLARED UNDER AN EXACTNESS CONDITION", 1,
     "squared modulus, because the exact l_1 is not in Q here -- priced by "
     "measurement, and no D2 verdict transfers to the l_1 form", False),
    ("F7-G-SET", "DECLARED", len(G_IDS),
     "four record functionals and the law's own rate", False),
    ("F8-RESOLUTION", "DECLARED", len(RES_IDS),
     "branch, site, step; the step column measured VACUOUS and stamped",
     False),
    ("F9-OBJECT-IDENTITY", "MEASURED", 1,
     "branch-steps deduplicated by (step, state, record); the collapse "
     "9751 -> 5 is forced by the frozen update semantics and stamped "
     "DEFINITIONAL-THROUGH-THE-FROZEN-SEMANTICS", False),
    ("F10-FOREIGN-FIELDS", "CITED", len(FOREIGN_FIELDS),
     "paper-20's own declared set, adopted unchanged, and measured to be "
     "foreign", False),
    ("F11-FIBER-SHAPE", "DECLARED", 1,
     "axes, not a product; stated in the receipt and in the paper", False),
    ("F12-BAR-SCOPE", "DECLARED", 1,
     "the frozen bar is applied to EXACT cells only; partial cells are not "
     "adjudicated gravitational, and the control is structurally unable to "
     "adjudicate them.  THIS IS THE CHOICE THAT DECIDES THE HEAD", True),
    ("F13-COOCCUPANCY-PREDICATE", "DECLARED", 2,
     "pairs sharing at least two occupied links, evaluated on the pre-coin "
     "psi; the single-site predicate is declared and measured beside it and "
     "they differ by one step", False),
    ("F14-DOMINATION-TEST", "DECLARED", 1,
     "per-step value-set comparison; COUPLED-DOMINATES iff coupled exceeds "
     "frozen at every separating step, and the result is HORIZON-LOCAL",
     False),
    ("F15-CONGRUENT-FIELDS", "DECLARED", len(CONGRUENT_SHIFTS),
     "the third channel's own declaration: two record perturbations congruent "
     "mod 3 at every cell and different at every object", False),
    ("F16-SITE-DEPENDENT-COIN", "DECLARED", 1,
     "the THEOREM A demonstration coin -- block-diagonal, unitary per block, "
     "not site-uniform; not a member of this unit's fiber and nothing about "
     "this arena is claimed from it", False),
)


def measure_scan(R):
    """E-24 as a gate: every published key whose values include a fraction
    over a configuration space either declares its measure or is stamped
    COUNTING-ONLY."""
    hits = set()

    def walk(o, top):
        if isinstance(o, str):
            if FRACTION_RE.match(o):
                hits.add(top)
        elif isinstance(o, dict):
            for v in o.values():
                walk(v, top)
        elif isinstance(o, (list, tuple)):
            for v in o:
                walk(v, top)
    for k, v in R.items():
        walk(v, k)
    missing = sorted(h for h in hits if h not in MEASURE_LEDGER)
    return sorted(hits), missing


# ===========================================================================
# THE RUN
# ===========================================================================

def measurement_layer(R, LD):
    """the surface the wall scans read: every measured receipt key together
    with the statement and evidence of every non-wall gate evaluated."""
    parts = [json.dumps({k: R.get(k) for k in MEASURED_KEYS},
                        sort_keys=True, default=str)]
    for g in LD.rows:
        if g["gate"].startswith("G-WALL"):
            continue
        parts.append(g["statement"])
        parts.append(g["evidence"])
    return "\n".join(parts)


def full_run(break_anchor=None, paper_text=None, paper_rel=PAPER_REL,
             do_paper=True):
    LD = Ledger()
    SEAL = Seal()
    R = {"schema": SCHEMA}
    say("=" * 78)
    say("GDL -- THE GRAVITATIONAL-DECOHERENCE LAW  (v14 paper-25)")
    say("=" * 78)

    # -- SEC 1: provenance --------------------------------------------------
    prov = []
    bad = []
    for sid, rel, want, why in SOURCES:
        blob = read_bytes(rel)
        got = hashlib.sha256(blob).hexdigest()[:12]
        exp = want if sid != break_anchor else "0" * 12
        prov.append({"id": sid, "path": rel, "expected": exp, "actual": got,
                     "match": got == exp, "why": why})
        if got != exp:
            bad.append(sid)
        R.setdefault("_blobs", {})[sid] = blob
    R["provenance"] = [{k: v for k, v in p.items()} for p in prov]
    R["arithmetic"] = {"ring": "Z[w], w^2 = -1 - w, as INTEGER PAIRS",
                       "denominator": "a common power of 9 per level",
                       "rationals": "fractions.Fraction only",
                       "floats": "none -- gated by an AST scan of this file "
                                 "and a recursive type scan of the receipt"}
    R["python"] = {"version": sys.version.split()[0],
                   "implementation": "CPython, exact integers"}
    LD.gate("G-PROVENANCE",
            "the %d declared sources are read at run time from paths resolved "
            "from THIS FILE's own location and every one is sha256-12 verified "
            "against this unit's frozen declaration; a missing source aborts "
            "the run LOUDLY and CLEANLY before anything is computed, and "
            "--break-anchor NAME corrupts any one of them" % len(SOURCES),
            not bad, "mismatched sources: %s" % (bad or "none"))
    SEAL.take("SEAL-SCHEMA", R)
    SEAL.take("SEAL-PROVENANCE", R)

    src = read_text(SELF)
    tree = ast.parse(src)
    floats = [n.lineno for n in ast.walk(tree)
              if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    imports = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            for a in n.names:
                imports.add(a.name.split(".")[0])
        elif isinstance(n, ast.ImportFrom):
            imports.add((n.module or "").split(".")[0])
    banned = sorted(imports & {"subprocess", "os.system", "multiprocessing",
                               "socket", "urllib", "requests", "pty"})
    foreign = sorted(i for i in imports
                     if i in {"coupling_exact", "giter_exact", "d42b1",
                              "d60_crystal_exact",
                              "d66_arbitration_crystal_exact"})
    LD.gate("G-EXACT-ARITHMETIC",
            "EXACT ARITHMETIC ONLY: an AST scan of this file finds no float "
            "literal anywhere; every amplitude is an INTEGER PAIR over Z[w] "
            "with a common power-of-9 denominator and every published number "
            "is an integer or an exact Fraction",
            not floats, "float literals at lines: %s" % (floats or "none"))
    SEAL.take("SEAL-ARITHMETIC", R)
    SEAL.take("SEAL-PYTHON", R)
    LD.gate("G-NO-SUBPROCESS",
            "#91: NO SUBPROCESS AND NO PARENT IMPORT.  The committed driver is "
            "read as a SPEC and this file re-implements the walk, the emission "
            "law and the update semantics; an AST scan of this file's own "
            "imports finds no process-spawning module and no module of any "
            "other unit, so the rebuild is independent by construction and the "
            "run is correct off-tree and git-less",
            not banned and not foreign,
            "process modules %s; foreign unit modules %s"
            % (banned or "none", foreign or "none"))

    declared = {s[1] for s in SOURCES}
    extra = sorted(set(READS) - declared)
    R["object_reads"] = {"declared": sorted(OBJECT_READS_WHY),
                         "why": OBJECT_READS_WHY,
                         "source_reads": sorted(set(READS)),
                         "undeclared_source_reads": extra}
    LD.gate("G-READS-DECLARED",
            "#46/#91: the run reads exactly two declared sets -- the %d pinned "
            "SOURCES, every one of them gated above, and the OBJECT set (this "
            "file, AST-parsed by its own scans, and the paper under test).  No "
            "repository state outside those two sets is read" % len(SOURCES),
            not extra, "undeclared source reads: %s" % (extra or "none"))
    SEAL.take("SEAL-OBJECT-READS", R)

    # -- the #62 verbatim anchors ------------------------------------------
    vrows = []
    vbad = []
    for vid, sid, needle, consumer in VERBATIM:
        blob = R["_blobs"][sid]
        text = blob.decode("utf-8")
        if vid in SHORT_ANCHORS:
            ok = canon(needle) in canon(text)
        else:
            ok = match_needle(text, needle)
        # each row carries its OWN falsifier: a perturbed needle must NOT match
        pert = needle[:-3] + "ZZZ" if len(needle) > 6 else needle + "ZZZ"
        dead = (canon(pert) in canon(text))
        vrows.append({"id": vid, "source": sid, "consumer_gate": consumer,
                      "located": ok, "perturbed_needle_located": dead,
                      "needle_chars": len(canon(needle))})
        if not ok or dead:
            vbad.append(vid)
    R["verbatim_anchors"] = vrows
    LD.gate("G-VERBATIM",
            "#62 + #125: %d verbatim anchors are located in their pinned "
            "sources with BOTH sides whitespace-normalised, ASCII-folded and "
            "markdown-prefix-stripped, and each row carries its own falsifier "
            "-- the needle perturbed at its last three characters must NOT be "
            "found" % len(VERBATIM),
            not vbad, "anchors failing to locate or whose perturbation still "
            "matched: %s" % (vbad or "none"))
    SEAL.take("SEAL-VERBATIM", R)

    C = raw_census()

    # -- SEC 3: the rebuild, anchored --------------------------------------
    arows = anchor_values(C["arms"])
    checks = parent_receipt_check(arows, R["_blobs"]["A-P20REC"])
    anchor_bad = pick("MUT-ANCHOR-LEAVES",
                      [c["what"] for c in checks if not c["equal"]],
                      ["FORGED"])
    loc = locate_in_parent(arows, R["_blobs"]["A-P20REC"])
    nloc = sum(1 for l in loc if l["located"])
    located = pick("MUT-ANCHOR-LOCATED", nloc, nloc - 1)
    R["rebuild"] = {
        "spec_source": "A-P20CODE (read, never imported, never subprocessed)",
        "anchor_rows": checks, "location_rows": loc,
        "anchors": len(checks), "anchors_equal": sum(1 for c in checks
                                                     if c["equal"]),
        "anchors_located": located,
        "independent": True}
    reg(len(checks), sum(1 for c in checks if c["equal"]), located)
    LD.gate("G-PARENT-REPRODUCED",
            "THE REBUILD IS ANCHORED AT THE PARENT'S OWN COMMITTED BYTES.  "
            "paper-20's driver is read as a SPEC and never imported and never "
            "subprocessed; the walk, the emission law and the update "
            "semantics are re-implemented here, and %d published values of "
            "the parent's committed receipt -- the branch ladders of three "
            "arms, both inverse participations, three exit probabilities, the "
            "link-class marginal, both site distributions, the maximum-cell "
            "ladder and both branch-step counts -- are required to come back "
            "out of THIS implementation at EQUALITY, row by row (#87)"
            % len(checks),
            not anchor_bad,
            "rows disagreeing with the parent: %s" % (anchor_bad or "none"))
    LD.gate("G-PARENT-LOCATED",
            "and the same values are LOCATED VERBATIM in the parent's "
            "committed receipt bytes, so the comparison is against the "
            "COMMITTED OBJECT rather than against a number this file typed: "
            "%d of %d rows located" % (located, len(loc)),
            located == len(loc),
            "located %d of %d" % (located, len(loc)))
    SEAL.take("SEAL-REBUILD", R)

    # -- the ensemble ------------------------------------------------------
    mass_bad = pick("MUT-MASS",
                    [nm for nm, a in C["arms"].items()
                     for lv in a["levels"] if not lv["mass_is_one"]],
                    ["A-COUPLED"])
    route_bad = pick("MUT-ROUTE",
                     sum(1 for a in C["arms"].values() for lv in a["levels"]
                         if lv["branches"] !=
                         lv["branches_from_emission_supports"]), 1)
    levels_total = sum(len(a["levels"]) for a in C["arms"].values())
    R["ensemble"] = {
        "arms": {nm: {"levels": a["levels"], "checks": a["checks"],
                      "violations": a["violations"]}
                 for nm, a in C["arms"].items()},
        "levels_total": levels_total,
        "branch_steps": {"coupled_raw": C["raw_c"],
                         "coupled_distinct": len(C["co"]),
                         "frozen_raw": C["raw_f"],
                         "frozen_distinct": len(C["fz"])},
        "horizon": HORIZON}
    reg(levels_total, C["raw_c"], len(C["co"]), C["raw_f"], len(C["fz"]))
    LD.gate("G-ENSEMBLE-EXHAUSTIVE",
            "the emission tree is carried EXHAUSTIVELY to the declared horizon "
            "%d -- no sampling, no pruning, no truncation by weight -- and "
            "exhaustiveness is checked by TWO INDEPENDENT ROUTES at each of "
            "the %d levels: the length of the carried frontier against the "
            "branch count recomputed from the emission supports of the level "
            "above" % (HORIZON, levels_total),
            route_bad == 0, "levels where the two routes disagree: %d"
            % route_bad)
    LD.gate("G-BRANCH-MASS",
            "the branch weights sum to exactly 1 at every one of the %d "
            "levels across the three anchored arms, as exact Fractions"
            % levels_total,
            not mass_bad, "levels whose mass is not 1: %s"
            % (mass_bad or "none"))
    SEAL.take("SEAL-ENSEMBLE", R)

    uviol = pick("MUT-UNITARY",
                 sum(a["violations"].get("site", 0) + a["violations"].get(
                     "norm", 0) + a["violations"].get("total", 0)
                     for a in C["arms"].values()), 1)
    usite = sum(a["checks"].get("site", 0) for a in C["arms"].values())
    kviol = pick("MUT-KERNEL",
                 sum(a["violations"].get("kernel", 0)
                     + a["violations"].get("kernel_entry", 0)
                     + a["violations"].get("law_native", 0)
                     for a in C["arms"].values()), 2)
    kchk = sum(a["checks"].get("kernel_entry", 0)
               + a["checks"].get("kernel", 0)
               + a["checks"].get("law_native", 0) for a in C["arms"].values())
    law_split = [{"class": cls, "checks": sum(a["checks"].get(cls, 0)
                                              for a in C["arms"].values()),
                  "violations": sum(a["violations"].get(cls, 0)
                                    for a in C["arms"].values()),
                  "kind": kind, "why": why}
                 for cls, kind, why in LAW_CHECK_CLASSES]
    split_sum = sum(r["checks"] for r in law_split)
    stamp_bad_law = pick(
        "MUT-LAW-STAMP",
        [r["class"] for r in law_split if r["kind"] != "DEFINITIONAL"]
        + ([] if split_sum == kchk else ["SPLIT"]), ["FORGED"])
    R["machine"] = {
        "coin": "C(x) = G . D(x), D(x) = diag(w^{n_l(x)}), site-block-diagonal",
        "shift": "|x, l> -> |x + l, l>",
        "emission": "q(l|x) = |(C psi)(x,l)|^2 (reading A) or n_l(x) "
                    "(reading B); k_1(l|x) = q(l|x)/M(x); the weight at cell "
                    "(x,l) is p(x) . k_1(l|x)",
        "update": "a division event on (x,l) increments n_l(x) by one; "
                  "admissibility is a property of the RECORD and not a "
                  "precondition of the STEP",
        "unitarity_checks": usite, "unitarity_violations": uviol,
        "unitarity_kind": CONTINGENT_MACHINE_ROW[1],
        "unitarity_why": CONTINGENT_MACHINE_ROW[2],
        "law_checks": kchk, "law_violations": kviol,
        "law_checks_kind": "DEFINITIONAL",
        "law_checks_classes": law_split,
        "law_checks_disclosure":
            "EVERY ONE OF THESE %s CHECKS IS AN IDENTITY IN THE DEFINITION OF "
            "THE KERNEL AND NONE OF THEM IS A ROW THAT COULD HAVE FAILED; the "
            "contentful sibling is the %s site-branch-step unitarity row, "
            "which is stamped CONTINGENT" % (com(kchk), com(usite))}
    reg(usite, uviol, kchk, kviol, split_sum)
    for r in law_split:
        reg(r["checks"], r["violations"])
    LD.gate("G-WALK-UNITARY",
            "the rebuilt step is unitary EXACTLY and PER OBJECT: each site of "
            "each branch of each step preserves its own mass, at %s "
            "site-branch-steps across the three arms" % com(usite),
            uviol == 0, "violations: %d" % uviol)
    LD.gate("G-LAW-KERNEL",
            "the LAW-NATIVE normaliser is re-derived on this arena rather than "
            "assumed: G(x,0) = 1 terminal, G(x,1) = M(x), and the kernel "
            "k_1 = q/M entry by entry, at %s per-object checks" % com(kchk),
            kviol == 0, "violations: %d" % kviol)
    LD.gate("G-LAW-CHECK-CLASSES",
            "AND THE COMPOSITE IS STAMPED RATHER THAN LEFT TO READ AS "
            "EVIDENCE (the paper-20 precedent).  The %s kernel checks split "
            "exactly as %s and EVERY ONE OF THE THREE CLASSES IS AN IDENTITY "
            "IN THE DEFINITION OF THE KERNEL: none of them is a row that could "
            "have failed for any coin, menu or record.  The class stamps and "
            "the split are published, and the split is required to sum to the "
            "composite.  The contentful sibling -- %s site-branch-step "
            "unitarity checks -- is stamped CONTINGENT beside them"
            % (com(kchk),
               " + ".join("%s %s" % (com(r["checks"]), r["class"])
                          for r in law_split), com(usite)),
            not stamp_bad_law,
            "classes not stamped DEFINITIONAL or a split that does not sum: "
            "%s (split %s against composite %s)"
            % (stamp_bad_law or "none", com(split_sum), com(kchk)))
    SEAL.take("SEAL-MACHINE", R)

    # -- SEC 4: the decoherence functionals --------------------------------
    # THE SPECIFICATION CHECK IS PER OBJECT (#87), not a one-object probe:
    # every object of both delivered arms is re-typed against each declared
    # formula.  D3's is covered nowhere else in the file.
    spec_bad = []
    spec_checks = 0
    for probe in C["co"] + C["fz"]:
        p = probe["p"]
        spec_checks += len(D_IDS)
        if probe["D1"] != sum(x * x for x in p):
            spec_bad.append("D1-IPR-BORN-MENU-SITE")
        if probe["D2"] != probe["purity"] - probe["D1"]:
            spec_bad.append("D2-OFFDIAG")
        if probe["D3"] != sum(probe["D3row"]):
            spec_bad.append("D3-RECORD-BORN-DIVERGENCE")
    spec_bad = pick("MUT-D-SPEC", sorted(set(spec_bad)), ["D2-OFFDIAG"])
    nonexact = pick("MUT-D-EXACT",
                    sum(1 for o in C["co"] + C["fz"] for k in D_SHORT
                        if not isinstance(o[k], Fraction)), 1)
    l1 = C["l1"]
    irrational = pick("MUT-L1-PRICE", l1["irrational_moduli"], 0)
    split_bad = pick("MUT-D2-SPLIT",
                     sum(1 for o in C["co"] + C["fz"]
                         if o["D1"] + o["D2"] != o["purity"]), 3)
    R["functionals"] = {
        "declared": [{"id": d, "specification": D_SPEC[d]} for d in D_IDS],
        "count": len(D_IDS),
        "objects_measured": len(C["co"]) + len(C["fz"]),
        "values_are_exact_fractions": nonexact == 0,
        "l1_price": l1,
        "purity_split_violations": split_bad,
        "fiber": "NONE PRIVILEGED: all three are run on every object of every "
                 "arm of every fiber member, and no ranking among them is "
                 "asserted anywhere"}
    reg(len(D_IDS), len(C["co"]) + len(C["fz"]), l1["offdiagonal_entries"],
        l1["perfect_squares"], l1["irrational_moduli"], l1["distinct_values"],
        l1["offdiagonal_population"], l1["zero_entries_which_are_rational"],
        l1["rational_moduli_over_the_full_population"], spec_checks)
    LD.gate("G-FUNCTIONALS-DECLARED",
            "the %d DECLARED decoherence functionals each carry a full "
            "specification in this file and each is re-derived from its own "
            "published formula AT EVERY OBJECT OF BOTH DELIVERED ARMS (#87: "
            "%s comparisons, not a one-object probe): D1 from the Born menu's "
            "site masses, D2 from the exact purity split, D3 from its own "
            "per-site rows.  None is privileged and all three are run "
            "everywhere" % (len(D_IDS), com(spec_checks)),
            not spec_bad, "functionals whose value disagrees with their "
            "published specification: %s" % (spec_bad or "none"))
    LD.gate("G-FUNCTIONALS-EXACT",
            "every decoherence value at every one of the %s objects of the two "
            "delivered arms is an exact Fraction -- there is no float and no "
            "rounding anywhere in the functional layer"
            % com(len(C["co"]) + len(C["fz"])),
            nonexact == 0, "non-exact values: %d" % nonexact)
    LD.gate("G-L1-PRICED",
            "THE l_1 DECLARATION IS PRICED, NOT WAVED THROUGH.  D2 is carried "
            "in SQUARED-MODULUS units because the exact l_1 form is not "
            "computable in Q on this arena, and that is MEASURED rather than "
            "asserted: of the %s off-diagonal |rho_xy|^2 entries this run "
            "produces, %s are perfect squares and %s are not, so %s exact "
            "moduli are irrational and outside this unit's arithmetic.  THE "
            "HONEST DENOMINATOR IS THE FULL POPULATION: %s unordered "
            "off-diagonal entries over %s objects, of which %s are exact "
            "zeros and therefore rational, so %s of %s moduli are rational"
            % (com(l1["offdiagonal_entries"]), com(l1["perfect_squares"]),
               com(l1["irrational_moduli"]), com(l1["irrational_moduli"]),
               com(l1["offdiagonal_population"]), com(len(C["co"])),
               com(l1["zero_entries_which_are_rational"]),
               com(l1["rational_moduli_over_the_full_population"]),
               com(l1["offdiagonal_population"])),
            irrational > 0,
            "irrational moduli: %d of %d" % (irrational,
                                             l1["offdiagonal_entries"]))
    LD.gate("G-PURITY-SPLIT",
            "the exact split D1 + D2 = Tr(rho^2) holds at every object of both "
            "delivered arms -- the inverse participation IS the diagonal of "
            "the site-basis purity and the coherence mass IS its complement",
            split_bad == 0, "violations: %d" % split_bad)
    SEAL.take("SEAL-FUNCTIONALS", R)

    # -- SEC 5: the growth functionals -------------------------------------
    rb_bad = pick("MUT-RATE-IS-BORN",
                  sum(1 for o in C["co"] + C["fz"] for s in range(9)
                      if o["eps"][s] != o["p"][s]), 1)
    rt_bad = pick("MUT-RATE-TOTAL",
                  sum(1 for o in C["co"] + C["fz"] if sum(o["eps"]) != 1), 1)
    fz_growth = pick("MUT-GROWTH-FROZEN",
                     sum(1 for o in C["fz"] if o["n"] != WELDED), 1)
    R["growth"] = {
        "declared": [{"id": g, "kind": G_KIND[g]} for g in G_IDS],
        "count": len(G_IDS),
        "rate_source": "read off the machine's own emission_weights, never "
                       "re-derived by this section",
        "rate_is_born_violations": rb_bad,
        "rate_total_violations": rt_bad,
        "frozen_records_that_grew": fz_growth,
        "n_growth_profile": {
            "coupled": [{"t": r["t"], "total_growth": str(r["G4"]),
                         "link_class_growth": [str(x) for x in r["G3"]],
                         "max_cell_count":
                             C["arms"]["A-COUPLED"]["ladder"][r["t"]]
                             ["max_cell_count"]}
                        for r in C["co_step"]],
            "frozen": [{"t": r["t"], "total_growth": str(r["G4"])}
                       for r in C["fz_step"]]}}
    reg(len(G_IDS), rb_bad, rt_bad, fz_growth)
    LD.gate("G-RATE-IS-BORN",
            "THE METRIC-GROWTH RATE IS THE MACHINE'S OWN, and it is measured "
            "to BE the Born menu's site mass: eps(x) = p(x) at every site of "
            "every one of the %s objects of both arms at the delivered "
            "reading, because the kernel is column-stochastic by the law's "
            "own normaliser; the same identity is re-taken on every fiber "
            "member, the record menu included, at G-COIN-FIBER"
            % com(len(C["co"]) + len(C["fz"])),
            rb_bad == 0, "violations: %d" % rb_bad)
    LD.gate("G-RATE-TOTAL",
            "and the total rate is exactly ONE division event per coupled "
            "step at every object -- the emission law is a probability "
            "distribution over the 27 cells and its mass is the walk's",
            rt_bad == 0, "violations: %d" % rt_bad)
    LD.gate("G-GROWTH-FROZEN-ZERO",
            "THE FROZEN CONTROL'S RECORD NEVER GROWS, and that is a per-object "
            "measurement rather than a definition read back: not one of the "
            "%s distinct frozen objects carries a record different from the "
            "welded one, so the ACTUAL growth functionals G1..G4 are "
            "identically constant there while the LAW's rate G5 is not"
            % com(len(C["fz"])),
            fz_growth == 0, "frozen objects whose record moved: %d" % fz_growth)
    SEAL.take("SEAL-GROWTH", R)

    # -- SEC 6: THE RELATION -----------------------------------------------
    grid_c = C["grid_coupled"]
    grid_f = C["grid_frozen"]
    grid_bad = []
    for row in grid_c + grid_f:
        w = row["verdict"]
        ok = ((w == "EXACT" and row["failing_classes"] == 0
               and row["nonsingleton_classes"] > 0)
              or (w == "PARTIAL" and row["failing_classes"] > 0)
              # THE VACUOUS CLAUSE CARRIES BOTH CONJUNCTS (K3 MAJOR-1): a
              # genuinely failing cell restamped VACUOUS with its failure
              # counts left truthful passed the delivered predicate.
              or (w == "VACUOUS" and row["nonsingleton_classes"] == 0
                  and row["failing_classes"] == 0)
              or (w == "EMPTY" and row["classes"] == 0))
        if not ok:
            grid_bad.append("%s/%s/%s" % (row["resolution"], row["growth"],
                                          row["decoherence"]))
    grid_bad = pick("MUT-RELATION-EXACT", grid_bad, ["FORGED"])
    stamp_bad_cells = []
    for row in grid_c + grid_f:
        want = row["verdict"]
        if want == "PARTIAL" and row["failing_classes"] == \
                row["nonsingleton_classes"]:
            want = "TOTAL-FAILURE"
        if row["stamp"] != want or (
                row["passing_nonsingleton_classes"]
                != row["nonsingleton_classes"] - row["failing_classes"]):
            stamp_bad_cells.append("%s/%s/%s" % (row["resolution"],
                                                 row["growth"],
                                                 row["decoherence"]))
    stamp_bad_cells = pick("MUT-TOTAL-FAILURE", stamp_bad_cells, ["FORGED"])
    vac_bad = pick("MUT-VACUITY",
                   sum(1 for row in grid_c + grid_f
                       if row["verdict"] == "EXACT"
                       and row["nonsingleton_classes"] == 0), 1)
    pools = {("RES-BRANCH", "coupled"): C["co"],
             ("RES-SITE", "coupled"): C["co_site"],
             ("RES-STEP", "coupled"): C["co_step"],
             ("RES-BRANCH", "frozen"): C["fz"],
             ("RES-SITE", "frozen"): C["fz_site"],
             ("RES-STEP", "frozen"): C["fz_step"]}
    if "census_bad" not in C:
        bad_recounts = 0
        recount_numbers = 0
        for arm, grid in (("coupled", grid_c), ("frozen", grid_f)):
            for row in grid:
                gk = G_SHORT[G_IDS.index(row["growth"])]
                dk = D_SHORT[D_IDS.index(row["decoherence"])]
                fc, fo, ns = recount(pools[(row["resolution"], arm)], gk, dk)
                recount_numbers += 3
                if fc != row["failing_classes"] or fo != \
                        row["objects_in_failing_classes"] \
                        or ns != row["nonsingleton_classes"]:
                    bad_recounts += 1
        C["census_bad"] = bad_recounts
        C["recount_numbers"] = recount_numbers
    census_bad = pick("MUT-FAILURE-SET", C["census_bad"], 1)
    # THE NO-FITTED-FORM GATE.  This unit's relation layer must contain no
    # fitted, regressed, approximated or best-fit quantity: the only verdict
    # words it may carry are the four equality-gated ones.
    words = {row["verdict"] for row in grid_c + grid_f}
    fitted_layer = json.dumps({"grid": grid_c + grid_f,
                               "identities": C["identities_coupled"]},
                              sort_keys=True, default=str).lower()
    fitted_needles = ("fit", "regress", "approx", "best-fit", "least squares",
                      "correlat", "estimat", "r-squared", "residual")
    fitted = pick("MUT-FITTED",
                  sum(1 for w in fitted_needles if w in fitted_layer), 1)
    exact_cells = [row for row in grid_c if row["verdict"] == "EXACT"]
    partial_cells = [row for row in grid_c if row["verdict"] == "PARTIAL"]
    vacuous_cells = [row for row in grid_c if row["verdict"] == "VACUOUS"]
    total_failures = [row for row in grid_c if row["stamp"] == "TOTAL-FAILURE"]

    def census_of(grid, key):
        out = Counter(row[key] for row in grid)
        return {k: out[k] for k in sorted(out)}

    # THE CONTROL'S OWN GRID, published (K1 MINOR-1 / K2 M1 leg 3): the word
    # this head carries is a word the null control earns at 38 of its own 45
    # cells, and 26 of the 28 coupled PARTIAL cells carry the IDENTICAL word
    # there.  That is why no PARTIAL cell is adjudicated gravitational.
    same_word = 0
    word_exceptions = []
    for row in partial_cells:
        fr = [x for x in grid_f if x["resolution"] == row["resolution"]
              and x["growth"] == row["growth"]
              and x["decoherence"] == row["decoherence"]][0]
        if fr["verdict"] == row["verdict"]:
            same_word += 1
        else:
            word_exceptions.append("%s/%s/%s -> %s"
                                   % (row["resolution"], row["growth"],
                                      row["decoherence"], fr["verdict"]))
    frozen_bad = pick(
        "MUT-FROZEN-GRID",
        [] if (sum(census_of(grid_f, "verdict").values()) == len(grid_f)
               and same_word + len(word_exceptions) == len(partial_cells))
        else ["FORGED"], ["FORGED"])
    R["relation"] = {
        "resolutions": list(RES_IDS),
        "grid_coupled": grid_c, "grid_frozen": grid_f,
        "cells_per_arm": len(grid_c),
        "verdict_census_coupled": census_of(grid_c, "verdict"),
        "verdict_census_frozen": census_of(grid_f, "verdict"),
        "stamp_census_coupled": census_of(grid_c, "stamp"),
        "stamp_census_frozen": census_of(grid_f, "stamp"),
        "total_failure_cells": [
            {"resolution": r["resolution"], "growth": r["growth"],
             "decoherence": r["decoherence"],
             "failing_classes": r["failing_classes"],
             "nonsingleton_classes": r["nonsingleton_classes"]}
            for r in total_failures],
        "total_failures": len(total_failures),
        "best_passing_fraction_among_the_partial_cells":
            "%d of %d" % max(
                ((r["passing_nonsingleton_classes"],
                  r["nonsingleton_classes"]) for r in partial_cells),
                key=lambda p: (Fraction(p[0], p[1]), p[1])),
        "coupled_partial_cells_with_the_identical_word_on_the_control":
            same_word,
        "coupled_partial_cells_with_a_different_word_on_the_control":
            word_exceptions,
        "recounted_numbers_per_cell": 3,
        "recounted_numbers": C["recount_numbers"],
        "exact_cells": [{"resolution": r["resolution"], "growth": r["growth"],
                         "decoherence": r["decoherence"],
                         "nonsingleton_classes": r["nonsingleton_classes"]}
                        for r in exact_cells],
        "exact": len(exact_cells), "partial": len(partial_cells),
        "vacuous": len(vacuous_cells),
        "identities_coupled": C["identities_coupled"],
        "identities_frozen": C["identities_frozen"],
        "verdict_words": sorted(words),
        "no_fitted_form": fitted == 0,
        "test": "EQUALITY-GATED: D is a function of G exactly when every "
                "G-class carries one D-value; nothing is fitted, regressed or "
                "approximated anywhere"}
    reg(len(grid_c), len(exact_cells), len(partial_cells), len(vacuous_cells),
        len(total_failures), len(partial_cells) - len(total_failures),
        same_word, C["recount_numbers"])
    for k, v in list(R["relation"]["verdict_census_frozen"].items()) + \
            list(R["relation"]["stamp_census_coupled"].items()) + \
            list(R["relation"]["stamp_census_frozen"].items()):
        reg(v)
    for row in grid_c + grid_f:
        reg(row["objects"], row["classes"], row["nonsingleton_classes"],
            row["passing_nonsingleton_classes"],
            row["failing_classes"], row["objects_in_failing_classes"],
            row["distinct_D_values"],
            row["distinct_D_values_in_failing_classes"])
    LD.gate("G-RELATION-CENSUS",
            "THE RELATION IS MEASURED, NOT FITTED.  %d cells per arm -- %d "
            "decoherence functionals x %d growth functionals x %d resolutions "
            "-- are decided by EQUALITY inside a growth class and by nothing "
            "else, on both arms, and every cell's published verdict word is "
            "required to agree with its own censused counts (#87: the "
            "predicate is per cell, never on the tally).  ON THE DELIVERED ARM "
            "%d EXACT, %d PARTIAL, %d VACUOUS; ON THE FROZEN CONTROL %s -- "
            "both censuses are published and neither stands for the other"
            % (len(grid_c), len(D_IDS), len(G_IDS), len(RES_IDS),
               len(exact_cells), len(partial_cells), len(vacuous_cells),
               ", ".join("%d %s" % (v, k) for k, v
                         in sorted(R["relation"]["verdict_census_frozen"]
                                   .items()))),
            not grid_bad, "cells whose word disagrees with their census: %s"
            % (grid_bad or "none"))
    LD.gate("G-VACUITY-DECLARED",
            "A TEST WITH NO NON-SINGLETON CLASS DECIDES NOTHING and is stamped "
            "VACUOUS rather than EXACT -- the honest denominator of this whole "
            "section.  %d of the %d coupled cells and the RES-STEP row of "
            "every column are vacuous by construction, and the stamp is "
            "checked per cell against BOTH conjuncts: no non-singleton class "
            "AND no failing class" % (len(vacuous_cells), len(grid_c)),
            vac_bad == 0,
            "cells published EXACT with no non-singleton class: %d" % vac_bad)
    LD.gate("G-FAILURE-CENSUS",
            "every PARTIAL cell reports its FAILURE SET exactly -- the failing "
            "classes, the objects inside them and the distinct D-values those "
            "classes carry -- and THREE numbers per cell are RECOUNTED by a "
            "second pass that shares no intermediate with the first: the "
            "failing classes, the objects inside them, AND THE NON-SINGLETON "
            "COUNT THE VACUOUS STAMP RESTS ON, over all %d cells of both arms "
            "at %d recounted numbers"
            % (len(grid_c) + len(grid_f), C["recount_numbers"]),
            census_bad == 0, "cells whose recount disagrees: %d" % census_bad)
    LD.gate("G-TOTAL-FAILURE-STAMP",
            "THE VERDICT GRAMMAR HAS NO WORD FOR A CELL IN WHICH EVERY "
            "NON-SINGLETON CLASS FAILS, so this unit publishes a STAMP beside "
            "the equality-gated word rather than letting PARTIAL absorb it: "
            "%d of the %d coupled PARTIAL cells carry NO partial relation at "
            "all and are stamped TOTAL-FAILURE, and the honest stamp census "
            "of the delivered arm is %s against the verdict census %s.  The "
            "best passing fraction anywhere in the partial cells is %s"
            % (len(total_failures), len(partial_cells),
               ", ".join("%d %s" % (v, k) for k, v
                         in sorted(R["relation"]["stamp_census_coupled"]
                                   .items())),
               ", ".join("%d %s" % (v, k) for k, v
                         in sorted(R["relation"]["verdict_census_coupled"]
                                   .items())),
               R["relation"]["best_passing_fraction_among_the_partial_cells"]),
            not stamp_bad_cells,
            "cells whose stamp or passing count disagrees with their own "
            "census: %s" % (stamp_bad_cells or "none"))
    LD.gate("G-FROZEN-GRID-CENSUS",
            "AND THE CONTROL'S OWN GRID IS PUBLISHED, not summarised away: %s "
            "of its %d cells, and %d of the %d coupled PARTIAL cells carry the "
            "IDENTICAL verdict word on the control (%d do not: %s).  A head "
            "word the null control earns at most of its own cells is not "
            "reporting a finding, which is exactly why no PARTIAL cell is "
            "adjudicated gravitational by any gate"
            % (", ".join("%d %s" % (v, k) for k, v
                         in sorted(R["relation"]["verdict_census_frozen"]
                                   .items())),
               len(grid_f), same_word, len(partial_cells),
               len(word_exceptions), word_exceptions or "none"),
            not frozen_bad,
            "frozen grid rows censused %d of %d; coupled PARTIAL cells "
            "accounted %d of %d" % (sum(R["relation"]["verdict_census_frozen"]
                                        .values()), len(grid_f),
                                    same_word + len(word_exceptions),
                                    len(partial_cells)))
    LD.gate("G-NO-FITTED-FORM",
            "FITTED FORMS ARE BARRED by the pin and the bar is a scan, not a "
            "promise: this unit's whole relation layer is searched for the "
            "vocabulary of fitting -- fit, regression, approximation, "
            "correlation, estimation, residual -- and the only verdict words "
            "it carries are the equality-gated %s"
            % ", ".join(sorted(words)),
            fitted == 0, "fitted-form needles found in the relation layer: %d"
            % fitted)
    SEAL.take("SEAL-RELATION", R)

    # -- SEC 7: FORCEDNESS --------------------------------------------------
    fiber = C["fiber"]
    coin_rows = [r for r in fiber if r["reading"] == DELIVERED_READING]
    read_rows = [r for r in fiber if r["coin"] == DELIVERED_COIN]
    cu_bad = pick("MUT-COIN-UNITARY",
                  [r["coin"] for r in fiber
                   if not (r["is_unitary_exactly"] and r["is_s3_covariant"])],
                  ["(-1+w)/3"])
    delivered = [r for r in fiber if r["coin"] == DELIVERED_COIN
                 and r["reading"] == DELIVERED_READING][0]
    fiber_bad = pick("MUT-COIN-FIBER",
                     [r["coin"] for r in fiber
                      if r["cell_signature"] != delivered["cell_signature"]
                      or r["separation_ladder"] != delivered[
                          "separation_ladder"]
                      or not r["identities_all_hold"]],
                     ["w/3"])
    executed = pick("MUT-FIBER-MEMBERS",
                    sorted({r["coin"] for r in coin_rows})
                    + sorted({"READING-" + r["reading"] for r in read_rows}),
                    (sorted({r["coin"] for r in coin_rows})
                     + sorted({"READING-" + r["reading"]
                               for r in read_rows}))[:-1])
    want_members = sorted(COIN_IDS) + sorted("READING-" + r
                                             for r in READING_FIBER)
    gr = [r for r in fiber if r["coin"] == "GROVER"
          and r["reading"] == DELIVERED_READING][0]
    ng = [r for r in fiber if r["coin"] == "-GROVER"][0]
    phase_keys = ("separation_ladder", "cell_signature",
                  "branch_steps_coupled_distinct",
                  "branch_steps_frozen_distinct")
    phase_bad = pick("MUT-PHASE-PAIR",
                     sum(1 for k in phase_keys if gr[k] != ng[k]), 1)
    R["forcedness"] = {
        "coin_fiber": COIN_IDS, "coin_fiber_size": len(COIN_IDS),
        "reading_fiber": list(READING_FIBER),
        "axes_not_a_product": "the fibers are run as DECLARED AXES: all %d "
                              "coin members at the delivered reading and both "
                              "reading members at the delivered coin.  The "
                              "cross-product is NOT claimed"
                              % len(COIN_IDS),
        "cooccupancy_threshold_is_invariant_across_the_fiber":
            len({(r["cooccupancy_threshold_coupled"],
                  r["cooccupancy_threshold_frozen"]) for r in fiber}) == 1,
        "single_site_threshold_is_invariant_across_the_fiber":
            len({(r["single_site_threshold_coupled"],
                  r["single_site_threshold_frozen"]) for r in fiber}) == 1,
        "cooccupancy_counts_on_the_frozen_object_at_the_horizon":
            sorted({r["cooccupancy_pairs_on_the_frozen_object_at_the_horizon"]
                    for r in fiber}),
        "cooccupancy_count_is_coin_relative":
            len({r["cooccupancy_pairs_on_the_frozen_object_at_the_horizon"]
                 for r in fiber}) > 1,
        "rows": fiber, "members_executed": executed,
        "members_declared": want_members,
        "delivered_signature": delivered["cell_signature"]}
    reg(len(COIN_IDS), len(READING_FIBER), len(fiber))
    LD.gate("G-COIN-ADMISSIBLE",
            "every member of the declared coin fiber is verified EXACTLY "
            "unitary (3C . 3C* = 9I in Z[w], entry by entry) and EXACTLY "
            "S_3-covariant against all six permutation matrices, per member "
            "and per entry (#87) -- %d members" % len(fiber),
            not cu_bad, "members failing admissibility: %s"
            % (cu_bad or "none"))
    LD.gate("G-COIN-FIBER",
            "FORCEDNESS IS MEASURED ACROSS THE WHOLE DECLARED FIBER.  All %d "
            "coin classes -- +/- Grover and the four hidden S_3-covariant "
            "members, paper-20's own witnesses -- are run to the full horizon "
            "on BOTH arms, and each is required to reproduce the delivered "
            "member's ENTIRE relation signature: all %d grid cells' verdict "
            "words on both arms, the separation ladder, every identity, AND "
            "BOTH OCCUPANCY THRESHOLDS ON BOTH ARMS -- the digest carries the "
            "threshold because the prediction row claims it across the fiber.  "
            "The threshold is invariant (%s on both arms at every member) "
            "while the co-occupancy COUNT is not: the control's own step-%d "
            "object carries %s pairs depending on the coin"
            % (len(COIN_IDS), len(delivered["cells"]),
               delivered["cooccupancy_threshold_coupled"], HORIZON,
               " / ".join(str(x) for x in R["forcedness"]
                          ["cooccupancy_counts_on_the_frozen_object_at_the_"
                           "horizon"])),
            not fiber_bad, "fiber members whose verdict shape differs: %s"
            % (fiber_bad or "none"))
    LD.gate("G-FIBER-EXECUTED",
            "and the execution is bound by SET EQUALITY against the declared "
            "member ids rather than by a cardinality: %d ids declared, %d "
            "executed" % (len(want_members), len(executed)),
            sorted(executed) == sorted(want_members),
            "declared %s; executed %s" % (sorted(want_members),
                                          sorted(executed)))
    LD.gate("G-GLOBAL-PHASE-PAIR",
            "+/- Grover differ by a GLOBAL PHASE, so every published row must "
            "be identical between them -- and this unit MEASURES that rather "
            "than assuming it, over the separation ladder, the whole cell "
            "signature and both distinct-object counts",
            phase_bad == 0, "rows differing between +Grover and -Grover: %d"
            % phase_bad)
    SEAL.take("SEAL-FORCEDNESS", R)

    # THE FROZEN EXCLUSION
    excl = []
    for row in exact_cells:
        gk = G_SHORT[G_IDS.index(row["growth"])]
        dk = D_SHORT[D_IDS.index(row["decoherence"])]
        fr = [x for x in grid_f if x["resolution"] == row["resolution"]
              and x["growth"] == row["growth"]
              and x["decoherence"] == row["decoherence"]][0]
        ident = [i for i in C["identities_frozen"]
                 if i["id"] == "ID-D1-IS-SQUARED-RATE"][0]
        holds_frozen = (fr["verdict"] == "EXACT"
                        or (row["growth"] == "G5-RATE-SITE"
                            and row["decoherence"] == D_IDS[0]
                            and ident["holds"]))
        excl.append({"resolution": row["resolution"], "growth": row["growth"],
                     "decoherence": row["decoherence"],
                     "frozen_verdict": fr["verdict"],
                     "identity_holds_frozen": ident["holds"],
                     "holds_identically_frozen": holds_frozen,
                     "gravitational": not holds_frozen})
    frozen_ran = pick("MUT-FROZEN-RAN", len(C["fz"]) > 0 and C["raw_f"] > 0,
                      False)
    excluded = pick("MUT-FROZEN-EXCLUSION",
                    [e for e in excl if e["holds_identically_frozen"]], [])
    gravitational = [e for e in excl if e["gravitational"]]
    R["exclusion"] = {
        "rule": "A RELATION THAT HOLDS IDENTICALLY ON THE FROZEN STAGE IS NOT "
                "A GRAVITATIONAL-DECOHERENCE RELATION: the frozen record never "
                "grows, so anything still true there is a fact about the walk "
                "and the law rather than about the coupling",
        "exact_cells_tested": len(excl), "excluded": excluded,
        "excluded_count": len(excluded),
        "gravitational_cells": gravitational,
        "gravitational_count": len(gravitational),
        "frozen_control_executed": frozen_ran,
        "frozen_branch_steps_raw": C["raw_f"],
        "frozen_branch_steps_distinct": len(C["fz"]),
        "identities_frozen": C["identities_frozen"],
        "bar_scope": "THE BAR IS APPLIED TO EXACT CELLS ONLY, and that is a "
                     "DECLARED choice, not an assumption: a relation that does "
                     "not HOLD cannot hold IDENTICALLY FROZEN.  Its "
                     "consequence is that the PARTIAL cells' gravitational "
                     "status is decided by NO GATE AT ALL, and the control "
                     "cannot decide it either, being a degenerate one-class "
                     "grid of %d objects.  It is item F12 of the choice "
                     "inventory" % len(C["fz"]),
        "the_zero_is_forced": {
            "why": "the single EXACT cell relates D1 to G5, and BOTH SIDES "
                   "are functions of the site marginal alone: D1 = sum_x "
                   "p(x)^2 and eps(x) = sum_l p(x) k_1(l|x) = p(x).  The site "
                   "marginal is record-blind BY THEOREM A, so the identity "
                   "could not have failed on the frozen stage from either "
                   "side.  The exclusion was not a measurement that came out "
                   "one way; it was compelled -- and the four genuine record "
                   "functionals G1..G4 produce no exact cell at any "
                   "resolution",
            "D1_moves_on_the_foreign_fields":
                sum(r["moved"]["D1"] for r in C["blindness"]),
            "G5_moves_on_the_foreign_fields": C["g5_blindness"]["moved"],
            "object_field_pairs": C["g5_blindness"]["checks"],
            "exact_cells_from_G1_to_G4": sum(
                1 for r in exact_cells if r["growth"] != "G5-RATE-SITE")}}
    reg(len(excl), len(excluded), len(gravitational),
        R["exclusion"]["the_zero_is_forced"]["exact_cells_from_G1_to_G4"])
    LD.gate("G-FROZEN-CONTROL",
            "THE MANDATORY FROZEN CONTROL IS EXECUTED, not declared: the same "
            "walk, the same emission rule and the same branching on counts "
            "that never update, through THE SAME FUNCTION as the coupled arm, "
            "at %s branch-steps that collapse to %d distinct measurements -- "
            "one per level, because on a frozen stage every branch of a level "
            "carries the same state on the same record"
            % (com(C["raw_f"]), len(C["fz"])),
            frozen_ran, "frozen control executed: %s" % frozen_ran)
    LD.gate("G-FROZEN-EXCLUSION",
            "THE EXCLUSION IS A GATE.  Every EXACT cell of the coupled arm is "
            "re-evaluated on the control and excluded if it survives there: %d "
            "exact cells tested, %d excluded as holding identically frozen, %d "
            "surviving as gravitational-decoherence relations.  AND THE ZERO "
            "IS FORCED, NOT CONTINGENT: the one exact cell relates a "
            "record-blind decoherence functional to a record-blind growth "
            "functional -- D1 moves %d times and G5 moves %d times over the "
            "same %s object-and-field pairs -- so it could not have failed on "
            "the control from either side, and the %d genuine record "
            "functionals G1..G4 produce no exact cell at any resolution.  THE "
            "BAR'S SCOPE IS DECLARED (F12): it is applied to EXACT cells only, "
            "so the PARTIAL cells are adjudicated gravitational by no gate"
            % (len(excl), len(excluded), len(gravitational),
               R["exclusion"]["the_zero_is_forced"]
               ["D1_moves_on_the_foreign_fields"],
               R["exclusion"]["the_zero_is_forced"]
               ["G5_moves_on_the_foreign_fields"],
               com(R["exclusion"]["the_zero_is_forced"]["object_field_pairs"]),
               len(G_IDS) - 1),
            len(excluded) + len(gravitational) == len(excl),
            "tested %d, excluded %d, gravitational %d"
            % (len(excl), len(excluded), len(gravitational)))
    SEAL.take("SEAL-EXCLUSION", R)

    sep = C["separation"]
    sep_bad = 0
    for r in sep:
        first = None
        for p in r["per_step"]:
            if not p["identical"] and first is None:
                first = p["t"]
        if first != r["first_separating_step"]:
            sep_bad += 1
    sep_bad = pick("MUT-SEPARATION", sep_bad, 1)
    dom = C["domination"]
    dom_bad = pick("MUT-DOMINATION",
                   sum(1 for r in dom
                       if r["verdict"] in ("COUPLED-DOMINATES",
                                           "FROZEN-DOMINATES",
                                           "NO-DOMINATION")
                       and not r["separating_steps"]), 1)
    R["prediction"] = {}          # filled below; sealed at its own gate
    LD.gate("G-SEPARATION-LADDER",
            "THE SEPARATION LADDER is a PER-OBJECT statement, not an average: "
            "for each functional the first step at which its VALUE SET on the "
            "coupled arm differs from the control's, recomputed inside the "
            "gate from the per-step rows -- %s"
            % ", ".join("%s at %s" % (r["functional"],
                                      r["first_separating_step"])
                        for r in sep),
            sep_bad == 0,
            "functionals whose published first step disagrees with their own "
            "per-step rows: %d" % sep_bad)
    LD.gate("G-DOMINATION",
            "MONOTONE DOMINATION WITH EXACT WITNESSES: a domination is claimed "
            "only where every SEPARATING step agrees in direction, the "
            "separating steps are named, and a direction that flips is "
            "published as NO-DOMINATION with the flip as its witness -- %s"
            % ", ".join("%s %s" % (r["functional"], r["verdict"])
                        for r in dom),
            dom_bad == 0,
            "domination rows published without their witness: %d" % dom_bad)

    # -- SEC 8: THE BLINDNESS MECHANISM ------------------------------------
    bl = C["blindness"]
    d1_moves = pick("MUT-BLIND-D1", sum(r["moved"]["D1"] for r in bl), 1)
    d3_moves = pick("MUT-D3-READS", sum(r["moved"]["D3"] for r in bl), 0)
    cooc_bad = pick("MUT-COOCC",
                    sum(r["moved_without_a_cooccupancy_pair"]["D2"]
                        for r in bl), 1)
    cooc_threshold = pick("MUT-COOCC-THRESHOLD", C["cooc_threshold"], 3)
    bl_checks = sum(r["checks"] for r in bl)
    d2_moves = sum(r["moved"]["D2"] for r in bl)
    obj_field_pairs = bl_checks // len(D_SHORT)
    pc = C["pair_census"]
    LOW = "pairs_meeting_in_at_most_one_occupied_link"
    HIGH = "pairs_meeting_in_two_or_more_occupied_links"
    pair_bad = pick("MUT-PAIR-MECHANISM", pc[LOW]["moved"], 1)
    g5_moves = pick("MUT-BLIND-G5", C["g5_blindness"]["moved"], 1)
    sd = C["site_dependent"]
    sd_bad = pick("MUT-THEOREM-A",
                  ([] if (sd["D1_moved"] == 0 and sd["site_marginal_moved"] == 0
                          and not sd["is_site_uniform"]
                          and sd["every_block_unitary"]
                          and sd["D2_moved"] > 0) else ["FORGED"]), ["FORGED"])
    sym = C["symbolic"]
    sym_bad = pick("MUT-THEOREM-B", sum(r["mismatches"] for r in sym), 1)
    occ_c, occ_f = C["occ_coupled"], C["occ_frozen"]
    occ_bad = pick(
        "MUT-OCCUPANCY",
        ([] if (occ_c == occ_f and occ_c[0] is not None
                and occ_c[1] is not None and occ_c[0] + 1 == occ_c[1]
                and occ_c[1] == C["cooc_threshold"]) else ["FORGED"]),
        ["FORGED"])
    generated = {o["n"] for o in C["co"]}
    foreign_bad = pick("MUT-FOREIGN-FIELD",
                       [nm for nm, fl in FOREIGN_FIELDS if fl in generated],
                       ["STALE"])
    R["mechanism"] = {
        "foreign_fields": [{"field": r["field"],
                            "is_admissible": r["is_admissible"],
                            "is_the_welded_record": r["is_the_welded_record"]}
                           for r in bl],
        "rows": bl, "checks": bl_checks,
        "object_field_pairs": obj_field_pairs,
        "D1_moves": d1_moves, "D2_moves": d2_moves, "D3_moves": d3_moves,
        "D2_moves_without_a_cooccupancy_pair": cooc_bad,
        "G5_moves": g5_moves,
        "G5_checks": C["g5_blindness"]["checks"],
        "foreign_fields_generated_by_this_run": foreign_bad,
        "pair_census": pc,
        "pair_checks": pc[LOW]["checks"] + pc[HIGH]["checks"],
        "site_dependent_coin": sd,
        "symbolic_cancellation": sym,
        "symbolic_identities": sum(r["residue_pair_identities"] for r in sym),
        "symbolic_coefficient_checks": sum(r["coefficient_checks"]
                                           for r in sym),
        "cooccupancy_ladder_coupled": C["cooc_rows"],
        "cooccupancy_ladder_frozen": C["cooc_rows_frozen"],
        "cooccupancy_threshold_coupled": cooc_threshold,
        "cooccupancy_threshold_frozen": C["cooc_threshold_frozen"],
        "single_site_threshold_coupled": occ_c[0],
        "single_site_threshold_frozen": occ_f[0],
        "theorem_A": "SITE-MARGINAL BLINDNESS.  Let the state live on sites x "
                     "fiber and let the record-dependent step act as U(n) = "
                     "(+)_x U_x(n), BLOCK-DIAGONAL IN THE SITE INDEX with each "
                     "block UNITARY on that site's fiber.  Then for every psi "
                     "and every n the site marginal p(x) = ||(U(n)psi)_x||^2 "
                     "is independent of n, so EVERY functional of the site "
                     "marginal alone -- D1 = sum_x p(x)^2, the Born site menu, "
                     "the emission rate eps(x), any Renyi entropy or inverse "
                     "participation of p -- is record-blind at that step.  "
                     "SITE-UNIFORMITY IS NOT A HYPOTHESIS, and neither is the "
                     "arena, the graph, the fiber dimension, the horizon, the "
                     "number of sites nor the order of w.  This is the unit's "
                     "exportable statement and it is arena-free",
        "theorem_B": "THE OFF-DIAGONAL REDUCTION.  If in addition U_x(n) = "
                     "G . D_x(n) with G SITE-UNIFORM unitary and D_x(n) = "
                     "diag(w^{n_l(x)}) unimodular diagonal in the fiber basis, "
                     "then rho_xy = sum_l w^{n_l(x) - n_l(y)} psi(x,l) "
                     "conj(psi(y,l)), so for any pair with at most one shared "
                     "occupied link the sum has at most one term and |rho_xy| "
                     "is record-independent.  CO-OCCUPANCY-NECESSITY IS "
                     "THEREFORE A THEOREM AND THE CENSUS CONFIRMS IT RATHER "
                     "THAN ESTABLISHING IT.  Site-uniformity is a hypothesis "
                     "HERE and only here",
        "theorem_C": "THE RESIDUE READING.  coin_apply reads WPOW[n % 3] and w "
                     "is a primitive CUBE root of unity, so the record enters "
                     "the dynamics ONLY as n mod 3: the record the machine "
                     "WRITES is unbounded, the record the coin READS is Z/3.  "
                     "Measured in the third-channel block",
        "scope": "THE MEASUREMENTS ARE ARENA-BOUND; THEOREM A IS NOT.  The "
                 "SCOPE box binds every number in this unit to this arena at "
                 "this horizon; theorem A is a statement about the FORM of the "
                 "step and licenses nothing numerical anywhere, which is what "
                 "makes the blindness a scope limit on the programme rather "
                 "than on this arena alone",
        "statement": "rho_xy = sum_l w^{n_l(x) - n_l(y)} psi(x,l) "
                     "conj(psi(y,l)).  Because the coin is unitary and "
                     "SITE-BLOCK-DIAGONAL it cancels out of the DIAGONAL of "
                     "the site-basis density matrix (THEOREM A); because it is "
                     "IN ADDITION the same at every site, the off-diagonal "
                     "reduces to the displayed form (THEOREM B) and the record "
                     "survives only on links occupied at BOTH ends.  A pair of "
                     "sites meeting in at most one link contributes a pure "
                     "global phase and cannot see the record at all; the "
                     "diagonal x = y always meets itself in every occupied "
                     "link with zero phase difference, which is why D1 is "
                     "record-blind everywhere"}
    reg(bl_checks, d1_moves, d2_moves, d3_moves, cooc_threshold,
        len(FOREIGN_FIELDS), obj_field_pairs, g5_moves,
        C["g5_blindness"]["checks"], occ_c[0], occ_f[0],
        pc[LOW]["checks"], pc[LOW]["moved"], pc[LOW]["static"],
        pc[HIGH]["checks"], pc[HIGH]["moved"], pc[HIGH]["static"],
        pc[LOW]["checks"] + pc[HIGH]["checks"], len(PAIRS),
        sd["object_field_pairs"], sd["D1_moved"], sd["D2_moved"],
        sd["site_marginal_moved"], sd["distinct_D1_at_the_horizon"],
        sd["distinct_D2_at_the_horizon"],
        R["mechanism"]["symbolic_identities"],
        R["mechanism"]["symbolic_coefficient_checks"])
    for r in sym:
        reg(r["residue_pair_identities"], r["coefficient_checks"],
            r["mismatches"])
    LD.gate("G-BLINDNESS-D1",
            "THE INHERITED DECOHERENCE OBSERVABLE IS RECORD-BLIND, MEASURED.  "
            "The site-basis inverse participation of the Born menu is "
            "re-evaluated on %d DECLARED FOREIGN count fields -- fields this "
            "run never generates, two of them not even admissible -- at every "
            "one of the %s coupled objects, and it does not move once.  The "
            "coin's record-dependent phases are diagonal and unitary, so they "
            "cannot change a site's own mass; the record enters D1 only "
            "through the walk's history, with a delay"
            % (len(FOREIGN_FIELDS), com(len(C["co"]))),
            d1_moves == 0, "D1 movements in %s object-and-field pairs -- D1's "
            "OWN denominator, of %s checks over the three functionals: %d"
            % (com(obj_field_pairs), com(bl_checks), d1_moves))
    LD.gate("G-BLINDNESS-D3",
            "THE INSTRUMENT IS TWO-WAY, which is what makes the blindness a "
            "measurement rather than a property of the census: on the same "
            "fields and the same objects the record-reading functional D3 "
            "moves %s times.  A census in which nothing moved would decide "
            "nothing" % com(d3_moves),
            d3_moves > 0, "D3 movements: %d" % d3_moves)
    LD.gate("G-COOCCUPANCY",
            "AND THE MIDDLE FUNCTIONAL'S BLINDNESS HAS AN EXACT MECHANISM, "
            "gated per object: D2 moves at %s of the %s object-and-field "
            "pairs and at NOT ONE pair whose occupied-link sets meet in at "
            "most one link -- co-occupancy is NECESSARY for the off-diagonal "
            "mass to see the record"
            % (com(d2_moves), com(bl_checks // len(D_SHORT))),
            cooc_bad == 0,
            "objects with no co-occupancy pair whose D2 moved: %d" % cooc_bad)
    LD.gate("G-COOCCUPANCY-THRESHOLD",
            "and the co-occupancy threshold is located by measuring EVERY step "
            "rather than by assertion: the first step of the coupled arm "
            "carrying a co-occupancy pair is %s, and the frozen control's is "
            "%s -- the threshold is a property of the WALK, not of the "
            "coupling" % (cooc_threshold, C["cooc_threshold_frozen"]),
            cooc_threshold == C["cooc_threshold_frozen"],
            "coupled threshold %s, frozen threshold %s"
            % (cooc_threshold, C["cooc_threshold_frozen"]))
    LD.gate("G-OCCUPANCY-PREDICATES",
            "TWO OCCUPANCY PREDICATES GOVERN THIS UNIT AND THEY DIFFER BY ONE "
            "STEP, and both are measured rather than one being described while "
            "the other is counted.  A SITE occupied on two links first appears "
            "at step %s: from there the record moves the cell masses, so the "
            "arms' states differ from the next step and D1 and D2 separate at "
            "exactly %s.  A PAIR of sites sharing two occupied links first "
            "appears at step %s: that is the predicate D2's off-diagonal "
            "blindness turns on and the one the census above measures.  Both "
            "are identical on the two arms, and the gate binds the "
            "one-step gap" % (occ_c[0], occ_c[0] + 1, occ_c[1]),
            not occ_bad,
            "single-site threshold coupled %s frozen %s; pair threshold "
            "coupled %s frozen %s; the gap is one step %s"
            % (occ_c[0], occ_f[0], occ_c[1], occ_f[1],
               occ_c[0] + 1 == occ_c[1]))
    LD.gate("G-PAIR-MECHANISM",
            "THE MECHANISM AT THE GRAIN ITS OWN ALGEBRA PREDICTS, %dx the "
            "per-object evidence.  THEOREM B says |rho_xy|^2 is "
            "record-independent for EVERY site pair meeting in at most one "
            "occupied link, whatever the rest of the object does.  Measured "
            "over %s objects x %d fields x %d site pairs = %s pair-checks: "
            "%s checks at overlap <= 1 with %d moved, and %s checks at "
            "co-occupancy with %s moved and %s static -- so co-occupancy is "
            "NECESSARY AND NOT SUFFICIENT at the finest grain too"
            % (len(PAIRS), com(len(C["co"])), len(FOREIGN_FIELDS), len(PAIRS),
               com(pc[LOW]["checks"] + pc[HIGH]["checks"]),
               com(pc[LOW]["checks"]), pc[LOW]["moved"],
               com(pc[HIGH]["checks"]), com(pc[HIGH]["moved"]),
               com(pc[HIGH]["static"])),
            pair_bad == 0,
            "site pairs meeting in at most one occupied link whose |rho_xy|^2 "
            "moved: %d" % pair_bad)
    LD.gate("G-BLINDNESS-G5",
            "AND THE GROWTH FUNCTIONAL OF THE ONE EXACT CELL IS RECORD-BLIND "
            "TOO.  The LAW's own rate eps(x) is re-read on the same %d foreign "
            "fields at every one of the %s coupled objects and does not move "
            "once in %s object-and-field pairs: under both readings eps(x) is "
            "the post-coin site mass, so THEOREM A applies to G5 verbatim.  "
            "THE SINGLE EXACT CELL OF THE WHOLE GRID THEREFORE RELATES A "
            "RECORD-BLIND DECOHERENCE FUNCTIONAL TO A RECORD-BLIND GROWTH "
            "FUNCTIONAL, which is the sharpest ground the frozen exclusion has"
            % (len(FOREIGN_FIELDS), com(len(C["co"])),
               com(C["g5_blindness"]["checks"])),
            g5_moves == 0, "G5 movements: %d" % g5_moves)
    LD.gate("G-THEOREM-A",
            "THEOREM A'S HYPOTHESIS IS ISOLATED AND MEASURED, not assumed: the "
            "same objects and the same foreign fields are re-read under a coin "
            "that is BLOCK-DIAGONAL IN THE SITE INDEX and exactly unitary on "
            "every block but NOT THE SAME AT EVERY SITE.  The site marginal "
            "moves %d times and D1 moves %d times in %s object-and-field "
            "pairs, while D2 moves %s -- so the diagonal blindness survives "
            "site-variation and the correct hypothesis is BLOCK-DIAGONALITY, "
            "not site-uniformity.  The demonstration coin is not a member of "
            "this unit's fiber and nothing about this arena is claimed from it"
            % (sd["site_marginal_moved"], sd["D1_moved"],
               com(sd["object_field_pairs"]), com(sd["D2_moved"])),
            not sd_bad,
            "site-uniform %s, every block unitary %s, site marginal moved %d, "
            "D1 moved %d, D2 moved %d"
            % (sd["is_site_uniform"], sd["every_block_unitary"],
               sd["site_marginal_moved"], sd["D1_moved"], sd["D2_moved"]))
    LD.gate("G-THEOREM-B",
            "AND THE CANCELLATION IS VERIFIED AS ALGEBRA, not as a sample.  "
            "With M = 3C the coin numerator, rho_xy = 9 . sum_j w^{n_j(x) - "
            "n_j(y)} psi(x,j) conj(psi(y,j)) is checked COEFFICIENT BY "
            "COEFFICIENT in Z[w] over all %s residue pairs across the %d "
            "declared coins -- %s identities at %s coefficient checks -- and "
            "because both sides are bilinear in (psi_x, conj psi_y) the %d "
            "monomial pairs verified span the form, so the check is a PROOF "
            "for every psi rather than a sample of them"
            % (com(sym[0]["residue_pair_identities"]), len(COIN_FIBER),
               com(R["mechanism"]["symbolic_identities"]),
               com(R["mechanism"]["symbolic_coefficient_checks"]), 9),
            sym_bad == 0, "coefficient mismatches: %d" % sym_bad)
    LD.gate("G-FOREIGN-FIELDS-FOREIGN",
            "and the fields ARE foreign, measured rather than asserted: none "
            "of the %d declared count fields is among the %s records this run "
            "generates on the coupled arm, and %d of them are not even "
            "admissible"
            % (len(FOREIGN_FIELDS), com(len(generated)),
               sum(1 for r in bl if not r["is_admissible"])),
            not foreign_bad,
            "declared foreign fields this run actually generates: %s"
            % (foreign_bad or "none"))
    SEAL.take("SEAL-MECHANISM", R)

    # -- SEC 8b: THE THIRD CHANNEL -- the mod-3 residue reading -------------
    res_rows = C["residue"]
    res_state = sum(r["moved"]["D1"] + r["moved"]["D2"] for r in res_rows)
    res_state = pick("MUT-RESIDUE-BLIND", res_state, 1)
    res_reads = pick("MUT-RESIDUE-TWO-WAY",
                     sum(r["moved"]["D3"] for r in res_rows), 0)
    res_checks = sum(r["checks"] for r in res_rows)
    lad = C["residue_ladder"]
    wrote = sum(r["written_wrapped_cells"] for r in lad)
    as_welded = sum(r["written_wrapped_cells_congruent_to_the_welded_value"]
                    for r in lad)
    readc = sum(r["wrapped_cells_read"] for r in lad)
    wrap_bad = pick(
        "MUT-WRAPAROUND",
        ([] if (wrote > 0 and as_welded == wrote and readc == 0
                and C["wrap_written_at"] == HORIZON
                and C["wrap_read_at"] == HORIZON + 1) else ["FORGED"]),
        ["FORGED"])
    R["residue"] = {
        "reading": "coin_apply reads WPOW[n % 3]: w is a primitive CUBE root "
                   "of unity, so the record enters the dynamics ONLY as "
                   "n mod 3",
        "order_of_the_record_phase": 3,
        "congruent_fields": [{"field": r["field"],
                              "congruent_at_every_cell":
                                  r["congruent_at_every_cell"],
                              "objects_whose_record_actually_changed":
                                  r["objects_whose_record_actually_changed"]}
                             for r in res_rows],
        "rows": res_rows, "checks": res_checks,
        "state_internal_moves": res_state,
        "record_reading_moves": res_reads,
        "wraparound_ladder": lad,
        "wrapped_cells_written": wrote,
        "wrapped_cells_written_congruent_to_the_welded_value": as_welded,
        "wrapped_cells_read": readc,
        "first_step_at_which_a_wrapped_cell_is_written": C["wrap_written_at"],
        "first_step_at_which_a_wrapped_cell_would_be_read": C["wrap_read_at"],
        "verdict": "THIRD-CHANNEL-PRESENT-AND-NOT-EXERCISED",
        "what_it_says":
            "The channel is REAL and it is one-sided: the two state-internal "
            "functionals cannot distinguish congruent-but-different records AT "
            "ALL, at 0 of their own checks, while the record-reading one does.  "
            "And the wraparound is reached INSIDE the declared horizon on the "
            "record the machine WRITES -- the anchored maximum-cell ladder "
            "reaches 4 at level %d and every wrapped cell there is congruent "
            "to the WELDED value -- but it is READ by no object of this "
            "horizon, because an object of step t reads the record of level "
            "t-1: the first step that would read a wrapped cell is %d, one "
            "step beyond the horizon this unit ran.  The channel therefore "
            "exists, is measured, and is NOT EXERCISED by any measurement in "
            "this unit" % (HORIZON, HORIZON + 1)}
    reg(res_checks, res_state, res_reads, wrote, as_welded, readc,
        C["wrap_written_at"], C["wrap_read_at"], len(CONGRUENT_SHIFTS), 3)
    for r in res_rows:
        reg(r["checks"], r["moved"]["D1"], r["moved"]["D2"], r["moved"]["D3"],
            r["objects_whose_record_actually_changed"])
    for r in lad:
        reg(r["written_max_cell_count"],
            r["written_branches_carrying_a_wrapped_cell"],
            r["written_wrapped_cells"],
            r["written_wrapped_cells_congruent_to_the_welded_value"],
            r["objects_reading_the_record_here"], r["read_max_cell_count"],
            r["objects_reading_a_wrapped_cell"], r["wrapped_cells_read"])
    LD.gate("G-RESIDUE-CHANNEL",
            "THE THIRD GEOMETRY-TO-MATTER CHANNEL, MEASURED AND TWO-WAY.  The "
            "record the machine WRITES is unbounded; the record the coin READS "
            "is Z/3.  %d declared CONGRUENT-BUT-DIFFERENT record fields -- the "
            "same residue at every one of the %d cells, a different record at "
            "every object -- are run against all three functionals at %s "
            "checks: the two state-internal functionals move %d times and the "
            "record-reading one moves %s.  A functional that saw the metric "
            "rather than its residue would move here, and two of the three "
            "cannot"
            % (len(CONGRUENT_SHIFTS), NCELL, com(res_checks), res_state,
               com(res_reads)),
            res_state == 0 and res_reads > 0,
            "state-internal moves on congruent records %d; record-reading "
            "moves %d" % (res_state, res_reads))
    LD.gate("G-RESIDUE-WRAPAROUND",
            "AND THE WRAPAROUND IS CENSUSED AT BOTH GRAINS, which is where the "
            "finding is.  WRITTEN: the anchored maximum-cell ladder reaches "
            "%d at level %d and %s cells there carry a count above 3, EVERY "
            "ONE of them congruent to the welded value n = 1.  READ: an object "
            "of step t reads the record of level t-1, so %d wrapped cells are "
            "read anywhere inside the declared horizon and the first step that "
            "would read one is %d -- one step beyond it.  The channel is "
            "present and NOT EXERCISED, and the difference between the two "
            "grains is exactly one step"
            % (lad[-1]["written_max_cell_count"], C["wrap_written_at"],
               com(wrote), readc, C["wrap_read_at"]),
            not wrap_bad,
            "wrapped cells written %d (congruent to the welded value %d), "
            "read %d; written first at %s, readable first at %s"
            % (wrote, as_welded, readc, C["wrap_written_at"],
               C["wrap_read_at"]))
    SEAL.take("SEAL-RESIDUE", R)

    # -- SEC 9: THE PREDICTION ROW -----------------------------------------
    ladders = {json.dumps(r["separation_ladder"], sort_keys=True)
               for r in fiber}
    carried = (len(ladders) == 1 and not fiber_bad
               and all(v is not None
                       for v in delivered["separation_ladder"].values()))
    pred_forced = pick("MUT-PREDICTION", carried, not carried)
    sepmap = delivered["separation_ladder"]
    thr = {json.dumps([r["cooccupancy_threshold_coupled"],
                       r["cooccupancy_threshold_frozen"]]) for r in fiber}
    prow = ("At this arena, at the declared horizon %d and for every member of "
            "the declared coin and reading fibers, the record-reading "
            "decoherence functional separates the coupled stage from the "
            "frozen control at step %s, exactly one step before either "
            "state-internal functional, which separate at step %s; and the "
            "co-occupancy threshold that governs the middle functional's "
            "blindness is step %s on BOTH arms."
            % (HORIZON, sepmap["D3"], sepmap["D1"], cooc_threshold))
    prow = pick("MUT-PREDICTION-RENDER", prow, prow + " FORGED")
    R["prediction"] = {
        "forced_across_the_fiber": pred_forced,
        "distinct_separation_ladders_across_the_fiber": len(ladders),
        "distinct_cooccupancy_thresholds_across_the_fiber": len(thr),
        "fiber_members": len(fiber),
        "separation_ladder": sepmap,
        "cooccupancy_threshold": cooc_threshold,
        "row": prow,
        "rows": [
            {"id": "GDL-PRED-1a",
             "content": "THE SEPARATION LADDER",
             "stamp": "FORCED-AT-THIS-ARENA",
             "evidence": "%d distinct ladder across %d executed members, "
                         "digest %s"
                         % (len(ladders), len(fiber),
                            delivered["cell_signature"]),
             "falsified_by": "any fiber member -- any coin, any declared "
                             "reading -- whose ladder is not (D3, D1, D2) = "
                             "(%s, %s, %s); any run at this arena and horizon "
                             "in which the ladder moves"
                             % (sepmap["D3"], sepmap["D1"], sepmap["D2"]),
             "not_falsified_by": "a change of arena, of horizon, of the "
                                 "observable set or of the fiber shape -- "
                                 "those are outside the stamp and license "
                                 "nothing against it",
             "mechanism": "the ladder is not a coincidence: D3 separates when "
                          "the RECORDS differ, and D1/D2 separate one step "
                          "after a site is first occupied on two links "
                          "(step %s), because that is when the record first "
                          "moves the cell masses.  A refutation should attack "
                          "the support geometry, not the coin"
                          % occ_c[0]},
            {"id": "GDL-PRED-1b",
             "content": "THE CO-OCCUPANCY THRESHOLD",
             "stamp": "FORCED-AT-THIS-ARENA",
             "evidence": "%d distinct (coupled, frozen) threshold pair across "
                         "%d executed members, censused on BOTH arms and "
                         "carried in the same sealed digest as the ladder"
                         % (len(thr), len(fiber)),
             "falsified_by": "any member whose threshold is not %s on both "
                             "arms" % cooc_threshold,
             "not_falsified_by": "a change of arena or horizon",
             "already_known_to_fail_in_its_stronger_form":
                 "THE COUNT IS COIN-RELATIVE WHILE THE THRESHOLD IS NOT: the "
                 "control's own step-%d object carries %s co-occupying pairs "
                 "depending on the coin, so the prediction is about the "
                 "THRESHOLD only and says so"
                 % (HORIZON, " / ".join(
                     str(x) for x in R["forcedness"]
                     ["cooccupancy_counts_on_the_frozen_object_at_the_"
                      "horizon"]))}],
        "units": "SUBSTRATE-NATIVE: step indices and object counts only -- no "
                 "SI quantity, no rate in any physical unit, no experimental "
                 "value, and no number inherited from the corpus's "
                 "Diosi-Penrose arc, which is cited for SHAPE ONLY",
        "horizon_locality": "D1's surviving domination is tested at %d steps "
                            "only, and the two functionals that fail teach "
                            "exactly that a two-step monotone claim can break "
                            "at the next horizon: D1 COUPLED-DOMINATES is "
                            "published HORIZON-LOCAL, never as a law"
                            % len([r for r in dom
                                   if r["functional"] == "D1"][0]
                                  ["separating_steps"]),
        "separation_rows": sep, "domination_rows": dom}
    reg(len(ladders), len(fiber), sepmap["D1"], sepmap["D2"], sepmap["D3"],
        len(thr))
    LD.gate("G-PREDICTION-ROW",
            "THE PREDICTION ROW IS ENTERED ONLY IF ITS OWN FIBER CENSUS "
            "CARRIES IT, and it is REGISTERED IN TWO ROWS because its two "
            "clauses had different standing: GDL-PRED-1a, the separation "
            "ladder, must be IDENTICAL across all %d executed fiber members "
            "with every functional separating at a finite step (%d distinct "
            "ladders measured); GDL-PRED-1b, the co-occupancy threshold, must "
            "be censused ON BOTH ARMS ACROSS THE SAME FIBER (%d distinct "
            "threshold pairs measured) rather than carried on the delivered "
            "member alone.  Each row publishes what falsifies it and what does "
            "not, and 1b publishes the stronger form already known to fail -- "
            "the COUNT is coin-relative"
            % (len(fiber), len(ladders), len(thr)),
            pred_forced and carried and len(ladders) == 1 and len(thr) == 1,
            "distinct ladders %d and distinct threshold pairs %d across %d "
            "members; census carries the row %s; published forced flag %s"
            % (len(ladders), len(thr), len(fiber), carried, pred_forced))
    LD.gate("G-PREDICTION-RENDERED",
            "and the row is RENDERED FROM THE RECEIPT rather than typed: every "
            "number in it is the measured value, and the sentence is required "
            "to carry them and to name no unit that is not a count or a step "
            "index",
            all(str(v) in prow for v in (HORIZON, sepmap["D3"], sepmap["D1"],
                                         cooc_threshold))
            and "FORGED" not in prow,
            "rendered row: %s" % prow)
    SEAL.take("SEAL-PREDICTION", R)

    # -- SEC 10: THE WALLS --------------------------------------------------
    ptext = paper_text or ""
    _cut = BANNED_L1.index(" ", 40)
    ptext = pick("MUT-WALL-L1", ptext,
                 ptext + "\n> " + BANNED_L1[:_cut] + "\n>   "
                 + BANNED_L1[_cut + 1:])
    l1_present = canon(BANNED_L1) in canon(ptext)
    LD.gate("G-WALL-L1",
            "L-1 IS ARGUED AND THEN DECLINED.  Order-level covariance is a "
            "fourth form outside paper 8's three; admitting it would need a "
            "group declared to act on the generated causal order and a reason "
            "to read it as a covariance group, and this unit constructs no "
            "such bridge.  THE FOURTH FORM IS NOT TESTED HERE, and the "
            "sentence retracted on 2026-07-28 is absent from the object under "
            "test -- the gate whitespace-normalises, ASCII-folds and strips "
            "markdown prefixes from BOTH sides, so a line-wrapped blockquoted "
            "copy cannot evade it",
            not l1_present,
            "the retracted L-1 sentence present in the paper: %s" % l1_present)

    layer = measurement_layer(R, LD)
    wall_rows = []
    for gname in ("G-WALL-BHS", "G-WALL-KR", "G-WALL-COSMO", "G-WALL-NO-SI"):
        hay = layer
        if gname == "G-WALL-BHS":
            hay = pick("MUT-WALL-BHS", hay, hay + " boosted rest frame")
        if gname == "G-WALL-KR":
            hay = pick("MUT-WALL-KR", hay, hay + " myrheim-meyer")
        if gname == "G-WALL-COSMO":
            hay = pick("MUT-WALL-COSMO", hay, hay + " cosmological expansion")
        if gname == "G-WALL-NO-SI":
            # THE SI WALL BINDS THE DELIVERABLE TOO: the pin bars SI numbers
            # from the published row, so the paper's own text is scanned with
            # the measurement layer.
            hay = hay + "\n" + ptext
            hay = pick("MUT-WALL-SI", hay,
                       hay + " collapse rate in kilogram")
        low = canon(hay).lower()
        hits = sorted(n for n in WALL_FORBIDDEN[gname] if n in low)
        wall_rows.append({"gate": gname, "needles": len(WALL_FORBIDDEN[gname]),
                          "hits": hits})
        LD.gate(gname,
                "the abstention is MEASURED rather than declared: this run's "
                "whole measurement surface -- every measured receipt key "
                "together with the statement and evidence of every non-wall "
                "gate evaluated -- is scanned for %d forbidden needles, and "
                "the falsifier writes the forbidden reading INTO that surface "
                "and dies here%s"
                % (len(WALL_FORBIDDEN[gname]),
                   ".  Three needles are DECLARED OUT with their reasons "
                   "printed: %s" % "; ".join(
                       "`%s` (%s)" % (k, v)
                       for k, v in sorted(NEEDLES_DECLARED_OUT.items()))
                   if gname == "G-WALL-NO-SI" else ""),
                not hits, "forbidden needles found: %s" % (hits or "none"))
    lz = pick("MUT-WALL-LORENTZ", canon(LORENTZ_NAMED) in canon(ptext), False)
    hx = pick("MUT-WALL-HEX", canon(HEX_NAMED) in canon(ptext), False)
    dp = pick("MUT-WALL-DP", canon(DP_NAMED) in canon(ptext), False)
    if not do_paper:
        lz = hx = dp = True
    R["walls"] = {"rows": wall_rows,
                  "declared_out": NEEDLES_DECLARED_OUT,
                  "lorentz_named": lz, "hexagonal_named": hx,
                  "dp_shape_only_named": dp,
                  "banned_L1_present": l1_present}
    LD.gate("G-WALL-DP-SHAPE",
            "THE DIOSI-PENROSE CITATION IS SHAPE-ONLY AND THE ABSTENTION IS "
            "WRITTEN DOWN: the corpus's gravitational-decoherence arc is named "
            "in the object under test with the sentence that inherits no "
            "number, no rate, no mass and no experimental claim from it, and "
            "the naming sentence is mandatory",
            dp, "the shape-only naming sentence present: %s" % dp)
    LD.gate("G-WALL-LORENTZ-NAMED",
            "THE LORENTZIAN RESONANCE IS NAMED, carried from the parent "
            "because this unit reads the same determinant: the sentence is "
            "mandatory and its falsifier deletes it",
            lz, "the Lorentzian naming sentence present: %s" % lz)
    LD.gate("G-WALL-HEX-NAMED",
            "THE HEXAGONAL RESONANCE IS NAMED, inherited from paper-19's S-7 "
            "through paper-20: the Gram matrix a reader will recognise is "
            "named before it is heard and no lattice-geometry reading is taken",
            hx, "the hexagonal naming sentence present: %s" % hx)
    SEAL.take("SEAL-WALLS", R)

    # -- E-24: the measure ledger ------------------------------------------
    hits, missing = measure_scan({k: v for k, v in R.items()
                                  if not k.startswith("_")})
    stamp_bad = pick("MUT-MEASURE-STAMP", len(missing), 1)
    R["measure_ledger"] = {"keys_carrying_fractions": hits,
                           "declared": MEASURE_LEDGER,
                           "undeclared": missing}
    LD.gate("G-MEASURE-DECLARED",
            "E-24: NO COUNT BECOMES A PROBABILITY WITHOUT A DECLARED MEASURE.  "
            "Every published key whose values include a fraction over a "
            "configuration space is required to name its measure or to carry "
            "the COUNTING-ONLY stamp; the probability-bearing keys all declare "
            "THE BRANCH MEASURE and the relation, forcedness and mechanism "
            "layers are stamped COUNTING-ONLY, since a failing-class count is "
            "not a probability of anything.  %d keys carry fractions"
            % len(hits),
            stamp_bad == 0, "keys carrying a fraction with no declared "
            "measure: %s" % (missing or "none"))
    SEAL.take("SEAL-MEASURE", R)

    # -- the choice inventory ----------------------------------------------
    chrows = [{"n": i + 1, "item": cid, "status": st, "fiber": fb,
               "note": note, "verdict_determining": vd}
              for i, (cid, st, fb, note, vd) in enumerate(CHOICES)]
    fibersizes = {"F2-COIN": len(COIN_IDS), "F3-READING": len(READING_FIBER),
                  "F5-D-SET": len(D_IDS), "F7-G-SET": len(G_IDS),
                  "F8-RESOLUTION": len(RES_IDS),
                  "F10-FOREIGN-FIELDS": len(FOREIGN_FIELDS),
                  "F15-CONGRUENT-FIELDS": len(CONGRUENT_SHIFTS)}
    choice_bad = pick(
        "MUT-CHOICE-BAR",
        [r["item"] for r in chrows
         if fibersizes.get(r["item"], r["fiber"]) != r["fiber"]]
        + ([] if any(r["verdict_determining"] for r in chrows)
           else ["NO-VERDICT-DETERMINING-ROW"]),
        ["F12-BAR-SCOPE"])
    R["choices"] = {"rows": chrows, "count": len(chrows),
                    "verdict_determining":
                        [r["item"] for r in chrows if r["verdict_determining"]],
                    "warrant": "every declared item has each member of its "
                               "fiber executed, and the execution is bound by "
                               "SET EQUALITY against the declared member ids "
                               "for F2 and F3 and by a declared cardinality "
                               "for the others"}
    for r in chrows:
        reg(r["n"], r["fiber"])
    reg(len(chrows))
    LD.gate("G-CHOICE-INVENTORY",
            "THE CHOICE INVENTORY IS A RENDERED TABLE, NOT PROSE: %d declared "
            "items, each with its status, its fiber size and its note, every "
            "fiber size re-derived here from the declaration it names, and THE "
            "VERDICT-DETERMINING ROW NAMED -- %s, the scope of the frozen bar, "
            "which the first delivery of this unit did not declare at all"
            % (len(chrows),
               ", ".join(R["choices"]["verdict_determining"])),
            not choice_bad, "items whose published fiber disagrees with the "
            "declaration it names, or a missing verdict-determining row: %s"
            % (choice_bad or "none"))
    SEAL.take("SEAL-CHOICES", R)

    # -- SEC 11: the verdict ------------------------------------------------
    cells_at_one = sum(1 for c in WELDED if c == 1)
    reg(cells_at_one, NCELL, HORIZON, len(SOURCES), len(MUTANTS),
        len(SEALED_PATHS))
    R["counts"] = {
        "sources": len(SOURCES), "verbatim_anchors": len(VERBATIM),
        "mutants": len(MUTANTS), "seals": len(SEALED_PATHS),
        "horizon": HORIZON, "cells": NCELL, "sites": NSITE,
        "welded_cells_at_one": cells_at_one,
        "decoherence_functionals": len(D_IDS),
        "growth_functionals": len(G_IDS), "resolutions": len(RES_IDS),
        "grid_cells_per_arm": len(grid_c),
        "coin_fiber": len(COIN_IDS), "reading_fiber": len(READING_FIBER),
        "fiber_rows": len(fiber),
        "branch_steps_coupled_raw": C["raw_c"],
        "branch_steps_coupled_distinct": len(C["co"]),
        "branch_steps_frozen_raw": C["raw_f"],
        "branch_steps_frozen_distinct": len(C["fz"]),
        "anchors_reproduced": sum(1 for c in checks if c["equal"]),
        "blindness_checks": bl_checks,
        "exact_cells": len(exact_cells), "partial_cells": len(partial_cells),
        "vacuous_cells": len(vacuous_cells),
        "excluded_cells": len(excluded),
        "gravitational_cells": len(gravitational)}
    # THE CONTROL ARM, RUN in the plain delivery run (the paper-23 pattern):
    # the arms this arena does not take are emitted by the SAME selector and
    # the SAME comparator on witness copies of the measured blocks.
    base_keys = ("rebuild", "ensemble", "machine", "functionals", "growth",
                 "relation", "forcedness", "exclusion", "mechanism",
                 "residue", "prediction", "choices", "counts")
    S0 = json.loads(json.dumps({k: R[k] for k in base_keys},
                               sort_keys=True, default=str))
    delivered_word = outcome_word(len(gravitational), fiber_bad, frozen_ran)
    oc = outcome_control_arm(S0, delivered_word)
    oc["wiring_matches_the_delivered_measurement"] = pick(
        "MUT-OUTCOME-ARM",
        (oc["rows"][0]["word_emitted"] == delivered_word), False)
    R["outcome"] = oc
    reg(oc["arms_declared"], len(oc["arms_reached"]), len(oc["rows"]))
    LD.gate("G-OUTCOME-REACHABILITY",
            "EVERY ARM OF THE DECLARED OUTCOME GRAMMAR IS REACHABLE, AND THE "
            "CONTROL ARM RUNS RATHER THAN ADVERTISING IT.  The pin's four "
            "outcome arms are handed to the SAME selector and the SAME "
            "comparator on witness copies of this run's own measured blocks -- "
            "one patched primitive each -- and each is required to emit its "
            "named word: %s.  %d of %d arms are reached and the delivered "
            "word, %s, is the one this arena's own measurement selects.  A "
            "head word whose alternatives are gate-forbidden is a DEFAULT and "
            "not a finding; this gate is what makes the difference measurable"
            % ("; ".join("%s -> %s" % (r["witness"], r["declared_word"])
                         for r in oc["rows"]),
               len(oc["arms_reached"]), oc["arms_declared"], delivered_word),
            oc["all_on_target"] and oc["every_arm_reached"]
            and oc["wiring_matches_the_delivered_measurement"],
            "witnesses on target %s; arms reached %s; the delivered word "
            "matches the selector %s"
            % (oc["all_on_target"], oc["arms_reached"],
               oc["wiring_matches_the_delivered_measurement"]))
    SEAL.take("SEAL-OUTCOME", R)

    verdict = build_verdict(R, C, delivered, exact_cells, partial_cells,
                            vacuous_cells, excluded, gravitational, checks,
                            bl, sep, dom, cooc_threshold, fiber_bad)
    verdict = pick("MUT-VERDICT-WORD", verdict,
                   dict(verdict, gates=verdict["gates"].replace(
                       "GDL-DECOUPLED-AT-THE-GRAVITATIONAL-BAR",
                       "GDL-LAW-FORCED-D1-IS-THE-SQUARED-RATE",
                       1)))
    verdict = pick("MUT-VERDICT-VALUE", verdict,
                   dict(verdict, arena=verdict["arena"].replace(
                       "27 OF 27", "26 OF 27", 1)))
    R["verdict"] = verdict
    ser = json.dumps({k: R[k] for k in base_keys + ("outcome",)},
                     sort_keys=True, default=str)
    again = reconstruct(json.loads(ser))
    same = {k: verdict[k] == again[k] for k in verdict}
    LD.gate("G-VERDICT-RECONSTRUCTED",
            "the verdict is DERIVED A SECOND TIME by a comparator that shares "
            "no code, no input and no typed literal with the builder: it is "
            "handed the receipt's own measured blocks as JSON, TYPES ITS OWN "
            "TEMPLATES, and RE-DERIVES THE OUTCOME WORD FROM THE PRIMITIVES -- "
            "whether the mandatory control ran, how many exact cells survived "
            "the bar, and whether every executed fiber member carries the "
            "delivered signature -- rather than reading a word the builder "
            "published.  All %d segments must match string for string"
            % len(verdict),
            all(same.values()),
            "segments matching: %s" % same)
    SEAL.take("SEAL-VERDICT", R)
    SEAL.take("SEAL-COUNTS", R)

    if do_paper and paper_text is not None:
        paper_gates(LD, SEAL, R, paper_text)
    else:
        for key, sid in (("paper_claims", "SEAL-PAPER-CLAIMS"),
                         ("paper_tables", "SEAL-PAPER-TABLES"),
                         ("paper_coverage", "SEAL-PAPER-COVERAGE"),
                         ("polarity", "SEAL-POLARITY")):
            R[key] = {"skipped": "no paper handed to this sub-pipeline"}
            SEAL.take(sid, R)
    R.pop("_blobs", None)
    return LD, SEAL, R, verdict, C


# ===========================================================================
# THE VERDICT AND ITS INDEPENDENT COMPARATOR
# ===========================================================================

# THE OUTCOME GRAMMAR, and the selector, GENUINELY TWO-WAY.
#
# The pin's `GDL-DECOUPLED` arm is glossed "no functional relation".  Every arm
# of the grammar carries the `GDL-` prefix and the pin defines the G in GDL
# itself: A RELATION THAT HOLDS IDENTICALLY FROZEN IS NOT A GRAVITATIONAL-
# DECOHERENCE RELATION.  The prefix therefore scopes the gloss, and the arm
# means: NO GRAVITATIONAL-DECOHERENCE FUNCTIONAL RELATION SURVIVES THE BAR.
#
# The first delivery of this unit read the gloss unscoped and emitted
# GDL-PARTIAL.  That word was a FORCED DEFAULT rather than a selection: the
# delivered `GDL-DECOUPLED` branch required the run to be simultaneously broken
# and empty (its `identities` conjunct is forced true by three gates and its
# `moves` conjunct is forced positive by a two-way gate), so the truer word had
# been lost by construction.  The selector below is a function of the frozen
# bar's own result and of nothing else, EVERY ARM OF IT IS REACHABLE, and the
# control arm below RUNS the arms this arena does not take.
OUTCOME_GRAMMAR = ("GDL-LAW-FORCED", "GDL-LAW-COIN-RELATIVE",
                   "GDL-DECOUPLED-AT-THE-GRAVITATIONAL-BAR",
                   "GDL-BLOCKED-AT-THE-FROZEN-CONTROL")


def outcome_word(gravitational, fiber_bad, frozen_ran):
    if not frozen_ran:
        return "GDL-BLOCKED-AT-THE-FROZEN-CONTROL"
    if gravitational:
        return ("GDL-LAW-FORCED" if not fiber_bad
                else "GDL-LAW-COIN-RELATIVE")
    return "GDL-DECOUPLED-AT-THE-GRAVITATIONAL-BAR"


# THE CONTROL ARM's witnesses: each patches ONE primitive of a JSON copy of the
# receipt's own measured blocks and requires the SAME head builder and the SAME
# comparator to emit the named word.  Nothing about this arena is measured
# here; what is measured is THE WIRING, in every one of its branches.
OUTCOME_WITNESSES = (
    ("THE-DELIVERED-MEASUREMENT", "GDL-DECOUPLED-AT-THE-GRAVITATIONAL-BAR",
     "no patch: the bar is applied and no exact cell survives it"),
    ("ONE-EXACT-CELL-SURVIVES-THE-BAR", "GDL-LAW-FORCED",
     "gravitational_count is set to 1 on a copy: an exact cell that FAILED on "
     "the frozen control would have survived as gravitational"),
    ("IT-SURVIVES-BUT-THE-FIBER-DISAGREES", "GDL-LAW-COIN-RELATIVE",
     "the same, with one fiber member's cell signature moved so the relation "
     "signature is coin-relative"),
    ("THE-FROZEN-CONTROL-DID-NOT-RUN", "GDL-BLOCKED-AT-THE-FROZEN-CONTROL",
     "frozen_control_executed is set to false on a copy: with no control the "
     "bar cannot be applied and no outcome may be read"),
)


def outcome_control_arm(S, delivered_word):
    """THE CONTROL ARM -- RUN, in the plain delivery run, not advertised.  The
    arms this arena does not take are handed to the SAME selector and the SAME
    comparator on witness copies of the measured blocks, and each is required
    to emit its named word.  That is what makes the delivered word a
    MEASUREMENT rather than a default."""
    rows = []
    for label, want, why in OUTCOME_WITNESSES:
        T = json.loads(json.dumps(S, sort_keys=True, default=str))
        # the witness reads only the head's OUTCOME WORD, which the comparator
        # derives before it renders any reachability number, so the stub below
        # carries no information into the measurement.
        T["outcome"] = {"arms_reached": [], "arms_declared": 0}
        if label == "ONE-EXACT-CELL-SURVIVES-THE-BAR":
            T["exclusion"]["gravitational_count"] = 1
        elif label == "IT-SURVIVES-BUT-THE-FIBER-DISAGREES":
            T["exclusion"]["gravitational_count"] = 1
            T["forcedness"]["rows"][-1]["cell_signature"] = "0" * 12
        elif label == "THE-FROZEN-CONTROL-DID-NOT-RUN":
            T["exclusion"]["frozen_control_executed"] = False
        got = reconstruct(T)["gates"].split("-<")[0]
        rows.append({"witness": label, "declared_word": want,
                     "word_emitted": got, "on_target": got == want,
                     "why": why})
    reached = sorted({r["word_emitted"] for r in rows})
    return {"grammar": list(OUTCOME_GRAMMAR), "rows": rows,
            "arms_reached": reached,
            "arms_declared": len(OUTCOME_GRAMMAR),
            "every_arm_reached": sorted(OUTCOME_GRAMMAR) == reached,
            "all_on_target": all(r["on_target"] for r in rows),
            "delivered_word": delivered_word,
            "the_wiring": "THE WORD IS A FUNCTION OF THE FROZEN BAR'S OWN "
                          "RESULT AND OF NOTHING ELSE: whether the control "
                          "ran, how many exact cells survived it, and whether "
                          "the fiber agrees"}


def build_verdict(R, C, delivered, exact_cells, partial_cells, vacuous_cells,
                  excluded, gravitational, checks, bl, sep, dom, cooc, fbad):
    rb = R["rebuild"]
    rel = R["relation"]
    mech = R["mechanism"]
    pred = R["prediction"]
    res = R["residue"]
    word = outcome_word(len(gravitational), fbad,
                        R["exclusion"]["frozen_control_executed"])
    arena = (
        "GDL-ARENA-[THE COUPLED MACHINE RE-IMPLEMENTED FROM THE COMMITTED SPEC "
        "AND ANCHORED AT THE PARENT'S OWN COMMITTED BYTES: %d OF %d PUBLISHED "
        "VALUES OF PAPER-20 RE-DERIVED AT EQUALITY BY AN IMPLEMENTATION THAT "
        "IMPORTS NO MODULE OF IT AND SUBPROCESSES NOTHING, AND ALL %d LOCATED "
        "VERBATIM IN THOSE BYTES; THE WELDED RECORD n = 1 AT %d OF %d CELLS "
        "DRIVEN TO HORIZON %d ON %d ARMS; %s BRANCH-STEPS ON THE COUPLED ARM "
        "COLLAPSING TO %s DISTINCT MEASUREMENTS AND %s ON THE FROZEN CONTROL "
        "COLLAPSING TO %d -- ONE PER LEVEL, BECAUSE A FROZEN STAGE CARRIES ONE "
        "QUANTUM HISTORY AND THE BRANCHING IS CLASSICAL BOOKKEEPING OVER IT; "
        "UNITARY AT %s SITE-BRANCH-STEPS AND LAW-NATIVE AT %s KERNEL CHECKS "
        "WITH 0 VIOLATIONS]@PAPER-20-TERMINAL-55273f6b6068"
        % (rb["anchors_equal"], rb["anchors"], rb["anchors_located"],
           R["counts"]["welded_cells_at_one"], R["counts"]["cells"],
           R["counts"]["horizon"], len(R["ensemble"]["arms"]),
           com(R["counts"]["branch_steps_coupled_raw"]),
           com(R["counts"]["branch_steps_coupled_distinct"]),
           com(R["counts"]["branch_steps_frozen_raw"]),
           R["counts"]["branch_steps_frozen_distinct"],
           com(R["machine"]["unitarity_checks"]),
           com(R["machine"]["law_checks"])))
    funcs = (
        "GDL-FUNCTIONALS-AND-MECHANISM-[%d DECOHERENCE FUNCTIONALS DECLARED, "
        "NONE PRIVILEGED, ALL RUN ON EVERY OBJECT OF EVERY ARM OF EVERY FIBER "
        "MEMBER; THE l_1 DECLARATION PRICED -- %s OF %s OFF-DIAGONAL MODULI "
        "ARE IRRATIONAL AND OUTSIDE Q, WHICH IS WHY D2 IS CARRIED IN SQUARED "
        "MODULUS OVER A POPULATION OF %s OF WHICH %s ARE EXACT ZEROS | %d "
        "GROWTH FUNCTIONALS FROM THE MACHINE'S OWN EMISSION LAW: "
        "THE SITE RATE IS THE BORN SITE MASS SUMMED THROUGH THE KERNEL AND THE "
        "TOTAL RATE IS EXACTLY ONE "
        "DIVISION EVENT PER COUPLED STEP, 0 VIOLATIONS | THE BLINDNESS "
        "MECHANISM, MEASURED ON %d DECLARED FOREIGN COUNT FIELDS AT %s CHECKS "
        "OVER THREE FUNCTIONALS, %s OBJECT-AND-FIELD PAIRS EACH: "
        "D1 MOVES %d TIMES, D2 MOVES %s TIMES AND AT NOT ONE OBJECT WHOSE "
        "OCCUPIED-LINK SETS MEET IN AT MOST ONE LINK, D3 MOVES %s TIMES, AND "
        "THE LAW'S OWN GROWTH FUNCTIONAL G5 MOVES %d TIMES -- THEOREM A: A "
        "SITE-BLOCK-DIAGONAL UNITARY STEP LEAVES THE SITE MARGINAL "
        "RECORD-BLIND AT ANY ARENA, GRAPH, DIMENSION AND HORIZON, MEASURED "
        "UNDER A SITE-DEPENDENT COIN AT %s PAIRS WITH THE MARGINAL MOVING %d "
        "TIMES AND D2 MOVING %s; THEOREM B: SITE-UNIFORMITY REDUCES THE "
        "OFF-DIAGONAL AND MAKES CO-OCCUPANCY-NECESSITY A THEOREM, VERIFIED "
        "COEFFICIENT BY COEFFICIENT AT %s IDENTITIES AND %s CHECKS, AND "
        "CONFIRMED AT THE PAIR GRAIN: %s OF %s PAIR-CHECKS AT OVERLAP <= 1 "
        "MOVE %d TIMES WHILE %s AT CO-OCCUPANCY MOVE %s | THE TWO OCCUPANCY "
        "THRESHOLDS: A SITE ON TWO LINKS AT STEP %s, A PAIR SHARING TWO LINKS "
        "AT STEP %s, BOTH IDENTICAL ON BOTH ARMS | THE SEPARATION LADDER %s, "
        "IDENTICAL ACROSS ALL %d EXECUTED FIBER MEMBERS]"
        % (R["counts"]["decoherence_functionals"],
           com(R["functionals"]["l1_price"]["irrational_moduli"]),
           com(R["functionals"]["l1_price"]["offdiagonal_entries"]),
           com(R["functionals"]["l1_price"]["offdiagonal_population"]),
           com(R["functionals"]["l1_price"]["zero_entries_which_are_rational"]),
           R["counts"]["growth_functionals"], len(FOREIGN_FIELDS),
           com(mech["checks"]), com(mech["object_field_pairs"]),
           mech["D1_moves"], com(mech["D2_moves"]),
           com(mech["D3_moves"]), mech["G5_moves"],
           com(mech["site_dependent_coin"]["object_field_pairs"]),
           mech["site_dependent_coin"]["site_marginal_moved"],
           com(mech["site_dependent_coin"]["D2_moved"]),
           com(mech["symbolic_identities"]),
           com(mech["symbolic_coefficient_checks"]),
           com(mech["pair_census"]
               ["pairs_meeting_in_at_most_one_occupied_link"]["checks"]),
           com(mech["pair_checks"]),
           mech["pair_census"]["pairs_meeting_in_at_most_one_occupied_link"]
           ["moved"],
           com(mech["pair_census"]
               ["pairs_meeting_in_two_or_more_occupied_links"]["checks"]),
           com(mech["pair_census"]
               ["pairs_meeting_in_two_or_more_occupied_links"]["moved"]),
           mech["single_site_threshold_coupled"], cooc,
           "D3 AT %s, D1 AND D2 AT %s" % (pred["separation_ladder"]["D3"],
                                          pred["separation_ladder"]["D1"]),
           R["counts"]["fiber_rows"]))
    ex = R["exclusion"]
    dom1 = [r for r in dom if r["functional"] == "D1"][0]
    gates = (
        "%s-<THE RELATION=MEASURED-NOT-FITTED(%d CELLS PER ARM -- %d "
        "DECOHERENCE x %d GROWTH x %d RESOLUTIONS -- DECIDED BY EQUALITY "
        "INSIDE A GROWTH CLASS AND BY NOTHING ELSE: ON THE DELIVERED ARM %d "
        "EXACT, %d PARTIAL WITH "
        "EVERY FAILURE SET CENSUSED AND RECOUNTED, %d VACUOUS AND STAMPED "
        "VACUOUS RATHER THAN PASSED; ON THE FROZEN CONTROL %d, %d AND %d) -- "
        "THE ONLY EXACT CELL IS THE LAW'S OWN "
        "IDENTITY(D1 = SUM_x eps(x)^2, THE SITE-BASIS INVERSE PARTICIPATION OF "
        "THE BORN MENU IS THE SUM OF THE SQUARED SITE EMISSION RATES, AT EVERY "
        "OBJECT OF BOTH ARMS -- A CONSEQUENCE OF THE LAW-NATIVE NORMALISER'S "
        "COLUMN-STOCHASTICITY, STAMPED DEFINITIONAL-THROUGH-THE-LAW) -- "
        "FROZEN-EXCLUSION=%d OF %d EXACT CELLS EXCLUDED(THEY HOLD IDENTICALLY "
        "ON THE FROZEN CONTROL, WHOSE RECORD NEVER GROWS AT %s BRANCH-STEPS, "
        "SO THEY ARE FACTS ABOUT THE WALK AND THE LAW RATHER THAN ABOUT THE "
        "COUPLING), AND FORCED: BOTH SIDES OF THE ONE EXACT IDENTITY ARE "
        "FUNCTIONS OF THE SITE MARGINAL, WHICH IS RECORD-BLIND BY THEOREM A -- "
        "D1 MOVES %d TIMES AND G5 MOVES %d TIMES OVER THE SAME %s "
        "OBJECT-AND-FIELD PAIRS -- SO IT COULD NOT HAVE FAILED ON THE CONTROL "
        "FROM EITHER SIDE, AND THE %d GENUINE RECORD FUNCTIONALS G1..G4 "
        "PRODUCE NO EXACT CELL AT ANY RESOLUTION -- GRAVITATIONAL D=f(G) "
        "CELLS=%d -- THE %d PARTIAL CELLS ARE NOT ADJUDICATED GRAVITATIONAL BY "
        "ANY GATE: THE BAR IS DECLARED(F12) TO APPLY TO EXACT CELLS ONLY AND "
        "IS INAPPLICABLE TO A RELATION THAT DOES NOT HOLD, %d OF THE %d CARRY "
        "THE IDENTICAL WORD ON THE FROZEN CONTROL, AND %d OF THE %d HAVE ZERO "
        "PASSING NON-SINGLETON CLASSES AND ARE STAMPED TOTAL-FAILURE(THE "
        "HONEST STAMP CENSUS OF THE DELIVERED ARM IS %d EXACT, %d PARTIAL, %d "
        "TOTAL-FAILURE, %d VACUOUS) -- THE RECORD DOES NOT DETERMINE "
        "THE DECOHERENCE(AT THE FINEST RESOLUTION THE CELL-GRAIN RECORD LEAVES "
        "%s OF %s OBJECTS IN CLASSES CARRYING MORE THAN ONE D1-VALUE, %s FOR "
        "D2 AND %s FOR D3; ON THE FROZEN CONTROL THE RECORD IS ONE CLASS "
        "CARRYING EVERY VALUE, SO IT CANNOT TESTIFY AT ALL) -- WHAT SURVIVES "
        "THE BAR IS BETWEEN-ARM, NOT WITHIN-ARM: THE SEPARATION LADDER D3 AT "
        "%s / D1 AND D2 AT %s IDENTICAL ACROSS %s OF %s FIBER MEMBERS, AND D1 "
        "COUPLED-DOMINATES AT BOTH ITS SEPARATING STEPS %s WITH EXACT "
        "WITNESSES AND IS PUBLISHED HORIZON-LOCAL -- DOMINATION=%s -- "
        "OUTCOME-REACHABILITY=%d OF %d ARMS OF THE DECLARED GRAMMAR EMITTED BY "
        "A WITNESS CONFIGURATION THROUGH THE SAME SELECTOR AND THE SAME "
        "COMPARATOR, SO THE WORD IS A MEASUREMENT AND NOT A DEFAULT -- "
        "FORCEDNESS=%s OF %s FIBER MEMBERS AGREE ON THE WHOLE "
        "RELATION SIGNATURE, THRESHOLDS INCLUDED(+/- GROVER MEASURED IDENTICAL "
        "AS A GLOBAL-PHASE PAIR) -- PREDICTION-ROW=%s -- SCOPE=THIS UNIT "
        "MEASURES A RELATION AT ONE ARENA AT ONE DECLARED HORIZON; NO "
        "CONTINUUM, NO SI QUANTITY, NO "
        "EXPERIMENTAL VALUE, AND THE DIOSI-PENROSE ARC CITED FOR SHAPE ONLY>"
        % (word, len(R["relation"]["grid_coupled"]),
           R["counts"]["decoherence_functionals"],
           R["counts"]["growth_functionals"], R["counts"]["resolutions"],
           len(exact_cells), len(partial_cells), len(vacuous_cells),
           rel["verdict_census_frozen"].get("EXACT", 0),
           rel["verdict_census_frozen"].get("PARTIAL", 0),
           rel["verdict_census_frozen"].get("VACUOUS", 0),
           len(excluded), ex["exact_cells_tested"],
           com(R["counts"]["branch_steps_frozen_raw"]),
           ex["the_zero_is_forced"]["D1_moves_on_the_foreign_fields"],
           ex["the_zero_is_forced"]["G5_moves_on_the_foreign_fields"],
           com(ex["the_zero_is_forced"]["object_field_pairs"]),
           R["counts"]["growth_functionals"] - 1,
           len(gravitational), len(partial_cells),
           rel["coupled_partial_cells_with_the_identical_word_on_the_control"],
           len(partial_cells), rel["total_failures"], len(partial_cells),
           rel["stamp_census_coupled"].get("EXACT", 0),
           rel["stamp_census_coupled"].get("PARTIAL", 0),
           rel["stamp_census_coupled"].get("TOTAL-FAILURE", 0),
           rel["stamp_census_coupled"].get("VACUOUS", 0),
           com(_cellstat(R, "RES-BRANCH", "G1-RECORD-CELL", D_IDS[0])),
           com(R["counts"]["branch_steps_coupled_distinct"]),
           com(_cellstat(R, "RES-BRANCH", "G1-RECORD-CELL", D_IDS[1])),
           com(_cellstat(R, "RES-BRANCH", "G1-RECORD-CELL", D_IDS[2])),
           pred["separation_ladder"]["D3"], pred["separation_ladder"]["D1"],
           R["counts"]["fiber_rows"] - len(fbad), R["counts"]["fiber_rows"],
           dom1["separating_steps"],
           "; ".join("%s %s" % (r["functional"], r["verdict"]) for r in dom),
           len(R["outcome"]["arms_reached"]), R["outcome"]["arms_declared"],
           R["counts"]["fiber_rows"] - len(fbad),
           R["counts"]["fiber_rows"],
           "ENTERED" if R["prediction"]["forced_across_the_fiber"]
           else "NOT-ENTERED"))
    third = (
        "GDL-THIRD-CHANNEL-[THE RECORD THE MACHINE WRITES IS UNBOUNDED; THE "
        "RECORD THE COIN READS IS Z/%d -- THE STEP READS w^(n mod %d) AND w IS "
        "A PRIMITIVE CUBE ROOT OF UNITY, SO EVERY psi-INTERNAL FUNCTIONAL SEES "
        "AT MOST A Z/%d SHADOW OF THE METRIC.  MEASURED ON %d DECLARED "
        "CONGRUENT-BUT-DIFFERENT RECORD FIELDS -- THE SAME RESIDUE AT EVERY "
        "ONE OF THE %d CELLS, A DIFFERENT RECORD AT EVERY OBJECT -- AT %s "
        "CHECKS: THE TWO STATE-INTERNAL FUNCTIONALS MOVE %d TIMES AND THE "
        "RECORD-READING ONE MOVES %s, SO TWO OF THE THREE CANNOT DISTINGUISH "
        "CONGRUENT RECORDS AT ALL AND ONE CAN | THE WRAPAROUND, CENSUSED AT "
        "BOTH GRAINS: WRITTEN INSIDE THE HORIZON -- THE ANCHORED MAXIMUM-CELL "
        "LADDER REACHES %d AT LEVEL %d AND %s CELLS THERE CARRY A COUNT ABOVE "
        "3, ALL %s OF THEM CONGRUENT TO THE WELDED VALUE n = 1 -- AND READ BY "
        "NO OBJECT OF IT: AN OBJECT OF STEP t READS THE RECORD OF LEVEL t-1, "
        "SO %d WRAPPED CELLS ARE READ ANYWHERE INSIDE THE DECLARED HORIZON AND "
        "THE FIRST STEP THAT WOULD READ ONE IS %d, ONE BEYOND IT | "
        "VERDICT=%s]"
        % (res["order_of_the_record_phase"], res["order_of_the_record_phase"],
           res["order_of_the_record_phase"], len(res["rows"]),
           R["counts"]["cells"], com(res["checks"]),
           res["state_internal_moves"], com(res["record_reading_moves"]),
           res["wraparound_ladder"][-1]["written_max_cell_count"],
           res["first_step_at_which_a_wrapped_cell_is_written"],
           com(res["wrapped_cells_written"]),
           com(res["wrapped_cells_written_congruent_to_the_welded_value"]),
           res["wrapped_cells_read"],
           res["first_step_at_which_a_wrapped_cell_would_be_read"],
           res["verdict"]))
    return {"arena": arena, "functionals": funcs, "gates": gates,
            "third_channel": third}


def _cellstat(R, res, growth, dec, key="objects_in_failing_classes"):
    for row in R["relation"]["grid_coupled"]:
        if row["resolution"] == res and row["growth"] == growth \
                and row["decoherence"] == dec:
            return row[key]
    return -1


def _agree(S):
    """the comparator's OWN count of agreeing fiber members, recomputed from
    the rows rather than read off a number the builder published."""
    rows = S["forcedness"]["rows"]
    sig = S["forcedness"]["delivered_signature"]
    base = [r for r in rows if r["cell_signature"] == sig]
    lad = base[0]["separation_ladder"] if base else None
    return sum(1 for r in rows
               if r["cell_signature"] == sig
               and r["separation_ladder"] == lad
               and r["identities_all_hold"])


def reconstruct(S):
    """THE COMPARATOR.  It shares no code, no input and no typed literal with
    the builder: it is handed the receipt's measured blocks as plain JSON and
    types its own templates from scratch."""
    rb = S["rebuild"]
    ct = S["counts"]
    mc = S["machine"]
    fn = S["functionals"]
    me = S["mechanism"]
    rl = S["relation"]
    ex = S["exclusion"]
    pr = S["prediction"]
    rs = S["residue"]
    oc = S["outcome"]

    def grp(x):
        return "{:,}".format(int(x))

    # THE HEAD WORD, RE-DERIVED FROM PRIMITIVES.  Three of them and no other:
    # did the mandatory control run, how many exact cells survived the bar, and
    # does every executed fiber member carry the delivered signature.
    grav = int(ex["gravitational_count"])
    nexact = int(rl["exact"])
    npart = int(rl["partial"])
    ran = bool(ex["frozen_control_executed"])
    agreeing = _agree(S)
    if not ran:
        head = "GDL-BLOCKED-AT-THE-FROZEN-CONTROL"
    elif grav:
        head = ("GDL-LAW-FORCED" if agreeing == len(S["forcedness"]["rows"])
                else "GDL-LAW-COIN-RELATIVE")
    else:
        head = "GDL-DECOUPLED-AT-THE-GRAVITATIONAL-BAR"
    a = ("GDL-ARENA-[THE COUPLED MACHINE RE-IMPLEMENTED FROM THE COMMITTED "
         "SPEC AND ANCHORED AT THE PARENT'S OWN COMMITTED BYTES: "
         + str(rb["anchors_equal"]) + " OF " + str(rb["anchors"])
         + " PUBLISHED VALUES OF PAPER-20 RE-DERIVED AT EQUALITY BY AN "
         "IMPLEMENTATION THAT IMPORTS NO MODULE OF IT AND SUBPROCESSES "
         "NOTHING, AND ALL " + str(rb["anchors_located"]) + " LOCATED VERBATIM "
         "IN THOSE BYTES; THE WELDED RECORD n = 1 AT "
         + str(ct["welded_cells_at_one"]) + " OF " + str(ct["cells"])
         + " CELLS DRIVEN TO HORIZON " + str(ct["horizon"]) + " ON "
         + str(len(S["ensemble"]["arms"])) + " ARMS; "
         + grp(ct["branch_steps_coupled_raw"]) + " BRANCH-STEPS ON THE "
         "COUPLED ARM COLLAPSING TO "
         + grp(ct["branch_steps_coupled_distinct"]) + " DISTINCT MEASUREMENTS "
         "AND " + grp(ct["branch_steps_frozen_raw"]) + " ON THE FROZEN "
         "CONTROL COLLAPSING TO "
         + str(ct["branch_steps_frozen_distinct"]) + " -- ONE PER LEVEL, "
         "BECAUSE A FROZEN STAGE CARRIES ONE QUANTUM HISTORY AND THE BRANCHING "
         "IS CLASSICAL BOOKKEEPING OVER IT; UNITARY AT "
         + grp(mc["unitarity_checks"]) + " SITE-BRANCH-STEPS AND LAW-NATIVE AT "
         + grp(mc["law_checks"]) + " KERNEL CHECKS WITH 0 VIOLATIONS]"
         "@PAPER-20-TERMINAL-55273f6b6068")
    f = ("GDL-FUNCTIONALS-AND-MECHANISM-["
         + str(ct["decoherence_functionals"]) + " DECOHERENCE FUNCTIONALS "
         "DECLARED, NONE PRIVILEGED, ALL RUN ON EVERY OBJECT OF EVERY ARM OF "
         "EVERY FIBER MEMBER; THE l_1 DECLARATION PRICED -- "
         + grp(fn["l1_price"]["irrational_moduli"]) + " OF "
         + grp(fn["l1_price"]["offdiagonal_entries"]) + " OFF-DIAGONAL MODULI "
         "ARE IRRATIONAL AND OUTSIDE Q, WHICH IS WHY D2 IS CARRIED IN SQUARED "
         "MODULUS OVER A POPULATION OF "
         + grp(fn["l1_price"]["offdiagonal_population"]) + " OF WHICH "
         + grp(fn["l1_price"]["zero_entries_which_are_rational"])
         + " ARE EXACT ZEROS | " + str(ct["growth_functionals"])
         + " GROWTH FUNCTIONALS "
         "FROM THE MACHINE'S OWN EMISSION LAW: THE SITE RATE IS THE BORN SITE "
         "MASS SUMMED THROUGH THE KERNEL AND THE TOTAL RATE IS EXACTLY ONE "
         "DIVISION EVENT PER COUPLED "
         "STEP, 0 VIOLATIONS | THE BLINDNESS MECHANISM, MEASURED ON "
         + str(len(me["foreign_fields"])) + " DECLARED FOREIGN COUNT FIELDS AT "
         + grp(me["checks"]) + " CHECKS OVER THREE FUNCTIONALS, "
         + grp(me["object_field_pairs"]) + " OBJECT-AND-FIELD PAIRS EACH: "
         "D1 MOVES " + str(me["D1_moves"])
         + " TIMES, D2 MOVES " + grp(me["D2_moves"]) + " TIMES AND AT NOT ONE "
         "OBJECT WHOSE OCCUPIED-LINK SETS MEET IN AT MOST ONE LINK, D3 MOVES "
         + grp(me["D3_moves"]) + " TIMES, AND THE LAW'S OWN GROWTH FUNCTIONAL "
         "G5 MOVES " + str(me["G5_moves"]) + " TIMES -- THEOREM A: A "
         "SITE-BLOCK-DIAGONAL UNITARY STEP LEAVES THE SITE MARGINAL "
         "RECORD-BLIND AT ANY ARENA, GRAPH, DIMENSION AND HORIZON, MEASURED "
         "UNDER A SITE-DEPENDENT COIN AT "
         + grp(me["site_dependent_coin"]["object_field_pairs"])
         + " PAIRS WITH THE MARGINAL MOVING "
         + str(me["site_dependent_coin"]["site_marginal_moved"])
         + " TIMES AND D2 MOVING "
         + grp(me["site_dependent_coin"]["D2_moved"])
         + "; THEOREM B: SITE-UNIFORMITY REDUCES THE OFF-DIAGONAL AND MAKES "
         "CO-OCCUPANCY-NECESSITY A THEOREM, VERIFIED COEFFICIENT BY "
         "COEFFICIENT AT " + grp(me["symbolic_identities"]) + " IDENTITIES AND "
         + grp(me["symbolic_coefficient_checks"]) + " CHECKS, AND CONFIRMED AT "
         "THE PAIR GRAIN: "
         + grp(me["pair_census"]
               ["pairs_meeting_in_at_most_one_occupied_link"]["checks"])
         + " OF " + grp(me["pair_checks"]) + " PAIR-CHECKS AT OVERLAP <= 1 "
         "MOVE " + str(me["pair_census"]
                       ["pairs_meeting_in_at_most_one_occupied_link"]["moved"])
         + " TIMES WHILE "
         + grp(me["pair_census"]
               ["pairs_meeting_in_two_or_more_occupied_links"]["checks"])
         + " AT CO-OCCUPANCY MOVE "
         + grp(me["pair_census"]
               ["pairs_meeting_in_two_or_more_occupied_links"]["moved"])
         + " | THE TWO OCCUPANCY THRESHOLDS: A SITE ON TWO LINKS AT STEP "
         + str(me["single_site_threshold_coupled"])
         + ", A PAIR SHARING TWO LINKS AT STEP "
         + str(me["cooccupancy_threshold_coupled"])
         + ", BOTH IDENTICAL ON BOTH ARMS | THE "
         "SEPARATION LADDER D3 AT " + str(pr["separation_ladder"]["D3"])
         + ", D1 AND D2 AT " + str(pr["separation_ladder"]["D1"])
         + ", IDENTICAL ACROSS ALL " + str(ct["fiber_rows"])
         + " EXECUTED FIBER MEMBERS]")
    fail = {}
    for row in rl["grid_coupled"]:
        if row["resolution"] == "RES-BRANCH" and \
                row["growth"] == "G1-RECORD-CELL":
            fail[row["decoherence"]] = int(row["objects_in_failing_classes"])
    dnames = sorted(fail)
    d1dom = [r for r in pr["domination_rows"]
             if str(r["functional"]) == "D1"][0]
    sc = rl["stamp_census_coupled"]
    vf = rl["verdict_census_frozen"]
    g = (head + "-<THE RELATION=MEASURED-NOT-FITTED("
         + str(len(rl["grid_coupled"])) + " CELLS PER ARM -- "
         + str(ct["decoherence_functionals"]) + " DECOHERENCE x "
         + str(ct["growth_functionals"]) + " GROWTH x "
         + str(ct["resolutions"]) + " RESOLUTIONS -- DECIDED BY EQUALITY "
         "INSIDE A GROWTH CLASS AND BY NOTHING ELSE: ON THE DELIVERED ARM "
         + str(nexact)
         + " EXACT, " + str(npart) + " PARTIAL WITH EVERY FAILURE SET CENSUSED "
         "AND RECOUNTED, " + str(int(rl["vacuous"])) + " VACUOUS AND STAMPED "
         "VACUOUS RATHER THAN PASSED; ON THE FROZEN CONTROL "
         + str(int(vf.get("EXACT", 0))) + ", " + str(int(vf.get("PARTIAL", 0)))
         + " AND " + str(int(vf.get("VACUOUS", 0)))
         + ") -- THE ONLY EXACT CELL IS THE LAW'S OWN "
         "IDENTITY(D1 = SUM_x eps(x)^2, THE SITE-BASIS INVERSE PARTICIPATION "
         "OF THE BORN MENU IS THE SUM OF THE SQUARED SITE EMISSION RATES, AT "
         "EVERY OBJECT OF BOTH ARMS -- A CONSEQUENCE OF THE LAW-NATIVE "
         "NORMALISER'S COLUMN-STOCHASTICITY, STAMPED "
         "DEFINITIONAL-THROUGH-THE-LAW) -- FROZEN-EXCLUSION="
         + str(int(ex["excluded_count"])) + " OF "
         + str(int(ex["exact_cells_tested"])) + " EXACT CELLS EXCLUDED(THEY "
         "HOLD IDENTICALLY ON THE FROZEN CONTROL, WHOSE RECORD NEVER GROWS AT "
         + grp(ct["branch_steps_frozen_raw"]) + " BRANCH-STEPS, SO THEY ARE "
         "FACTS ABOUT THE WALK AND THE LAW RATHER THAN ABOUT THE COUPLING), "
         "AND FORCED: BOTH SIDES OF THE ONE EXACT IDENTITY ARE FUNCTIONS OF "
         "THE SITE MARGINAL, WHICH IS RECORD-BLIND BY THEOREM A -- D1 MOVES "
         + str(int(ex["the_zero_is_forced"]["D1_moves_on_the_foreign_fields"]))
         + " TIMES AND G5 MOVES "
         + str(int(ex["the_zero_is_forced"]["G5_moves_on_the_foreign_fields"]))
         + " TIMES OVER THE SAME "
         + grp(ex["the_zero_is_forced"]["object_field_pairs"])
         + " OBJECT-AND-FIELD PAIRS -- SO IT COULD NOT HAVE FAILED ON THE "
         "CONTROL FROM EITHER SIDE, AND THE "
         + str(int(ct["growth_functionals"]) - 1) + " GENUINE RECORD "
         "FUNCTIONALS G1..G4 PRODUCE NO EXACT CELL AT ANY RESOLUTION -- "
         "GRAVITATIONAL D=f(G) CELLS=" + str(grav) + " -- THE " + str(npart)
         + " PARTIAL CELLS ARE NOT ADJUDICATED GRAVITATIONAL BY ANY GATE: THE "
         "BAR IS DECLARED(F12) TO APPLY TO EXACT CELLS ONLY AND IS "
         "INAPPLICABLE TO A RELATION THAT DOES NOT HOLD, "
         + str(int(rl["coupled_partial_cells_with_the_identical_word_on_the_"
                      "control"]))
         + " OF THE " + str(npart) + " CARRY THE IDENTICAL WORD ON THE FROZEN "
         "CONTROL, AND " + str(int(rl["total_failures"])) + " OF THE "
         + str(npart) + " HAVE ZERO PASSING NON-SINGLETON CLASSES AND ARE "
         "STAMPED TOTAL-FAILURE(THE HONEST STAMP CENSUS OF THE DELIVERED ARM "
         "IS " + str(int(sc.get("EXACT", 0))) + " EXACT, "
         + str(int(sc.get("PARTIAL", 0))) + " PARTIAL, "
         + str(int(sc.get("TOTAL-FAILURE", 0))) + " TOTAL-FAILURE, "
         + str(int(sc.get("VACUOUS", 0))) + " VACUOUS) -- THE RECORD DOES NOT "
         "DETERMINE THE DECOHERENCE(AT THE FINEST RESOLUTION THE CELL-GRAIN "
         "RECORD LEAVES " + grp(fail[dnames[0]]) + " OF "
         + grp(ct["branch_steps_coupled_distinct"]) + " OBJECTS IN CLASSES "
         "CARRYING MORE THAN ONE D1-VALUE, " + grp(fail[dnames[1]])
         + " FOR D2 AND " + grp(fail[dnames[2]]) + " FOR D3; ON THE FROZEN "
         "CONTROL THE RECORD IS ONE CLASS CARRYING EVERY VALUE, SO IT CANNOT "
         "TESTIFY AT ALL) -- WHAT SURVIVES THE BAR IS BETWEEN-ARM, NOT "
         "WITHIN-ARM: THE SEPARATION LADDER D3 AT "
         + str(pr["separation_ladder"]["D3"]) + " / D1 AND D2 AT "
         + str(pr["separation_ladder"]["D1"]) + " IDENTICAL ACROSS "
         + str(agreeing) + " OF " + str(len(S["forcedness"]["rows"]))
         + " FIBER MEMBERS, AND D1 COUPLED-DOMINATES AT BOTH ITS SEPARATING "
         "STEPS " + str(d1dom["separating_steps"]) + " WITH EXACT WITNESSES "
         "AND IS PUBLISHED HORIZON-LOCAL -- DOMINATION="
         + "; ".join(str(r["functional"]) + " " + str(r["verdict"])
                     for r in pr["domination_rows"])
         + " -- OUTCOME-REACHABILITY=" + str(len(oc["arms_reached"])) + " OF "
         + str(int(oc["arms_declared"])) + " ARMS OF THE DECLARED GRAMMAR "
         "EMITTED BY A WITNESS CONFIGURATION THROUGH THE SAME SELECTOR AND THE "
         "SAME COMPARATOR, SO THE WORD IS A MEASUREMENT AND NOT A DEFAULT -- "
         "FORCEDNESS=" + str(agreeing) + " OF "
         + str(len(S["forcedness"]["rows"])) + " FIBER MEMBERS AGREE ON THE "
         "WHOLE RELATION SIGNATURE, THRESHOLDS INCLUDED(+/- GROVER MEASURED "
         "IDENTICAL AS A GLOBAL-PHASE PAIR) -- PREDICTION-ROW="
         + ("ENTERED" if pr["forced_across_the_fiber"] else "NOT-ENTERED")
         + " -- SCOPE=THIS UNIT MEASURES A RELATION AT ONE ARENA AT ONE "
         "DECLARED HORIZON; NO CONTINUUM, NO SI QUANTITY, NO EXPERIMENTAL "
         "VALUE, AND THE DIOSI-PENROSE ARC CITED FOR SHAPE ONLY>")
    lad = rs["wraparound_ladder"]
    th = ("GDL-THIRD-CHANNEL-[THE RECORD THE MACHINE WRITES IS UNBOUNDED; THE "
          "RECORD THE COIN READS IS Z/" + str(int(rs["order_of_the_record_"
                                                     "phase"]))
          + " -- THE STEP READS w^(n mod "
          + str(int(rs["order_of_the_record_phase"])) + ") AND w IS A "
          "PRIMITIVE CUBE ROOT OF UNITY, SO EVERY psi-INTERNAL FUNCTIONAL SEES "
          "AT MOST A Z/" + str(int(rs["order_of_the_record_phase"]))
          + " SHADOW OF THE METRIC.  MEASURED ON " + str(len(rs["rows"]))
          + " DECLARED CONGRUENT-BUT-DIFFERENT RECORD FIELDS -- THE SAME "
          "RESIDUE AT EVERY ONE OF THE " + str(int(ct["cells"]))
          + " CELLS, A DIFFERENT RECORD AT EVERY OBJECT -- AT "
          + grp(rs["checks"]) + " CHECKS: THE TWO STATE-INTERNAL FUNCTIONALS "
          "MOVE " + str(int(rs["state_internal_moves"])) + " TIMES AND THE "
          "RECORD-READING ONE MOVES " + grp(rs["record_reading_moves"])
          + ", SO TWO OF THE THREE CANNOT DISTINGUISH CONGRUENT RECORDS AT ALL "
          "AND ONE CAN | THE WRAPAROUND, CENSUSED AT BOTH GRAINS: WRITTEN "
          "INSIDE THE HORIZON -- THE ANCHORED MAXIMUM-CELL LADDER REACHES "
          + str(int(lad[-1]["written_max_cell_count"])) + " AT LEVEL "
          + str(int(rs["first_step_at_which_a_wrapped_cell_is_written"]))
          + " AND " + grp(rs["wrapped_cells_written"]) + " CELLS THERE CARRY A "
          "COUNT ABOVE 3, ALL "
          + grp(rs["wrapped_cells_written_congruent_to_the_welded_value"])
          + " OF THEM CONGRUENT TO THE WELDED VALUE n = 1 -- AND READ BY NO "
          "OBJECT OF IT: AN OBJECT OF STEP t READS THE RECORD OF LEVEL t-1, SO "
          + str(int(rs["wrapped_cells_read"])) + " WRAPPED CELLS ARE READ "
          "ANYWHERE INSIDE THE DECLARED HORIZON AND THE FIRST STEP THAT WOULD "
          "READ ONE IS "
          + str(int(rs["first_step_at_which_a_wrapped_cell_would_be_read"]))
          + ", ONE BEYOND IT | VERDICT=" + str(rs["verdict"]) + "]")
    return {"arena": a, "functionals": f, "gates": g, "third_channel": th}


# ===========================================================================
# THE PAPER GATES
# ===========================================================================

def paper_claims(R):
    """the paper's load-bearing sentences, ASSEMBLED FROM THE RECEIPT and then
    required to be present verbatim.  Nothing here is typed twice."""
    ct = R["counts"]
    rb = R["rebuild"]
    fn = R["functionals"]
    me = R["mechanism"]
    rl = R["relation"]
    ex = R["exclusion"]
    pr = R["prediction"]
    rs = R["residue"]
    oc = R["outcome"]
    out = []

    def add(cid, sent):
        out.append({"id": cid, "sentence": sent})
        for t in re.findall(r"\d[\d,]*(?:/\d+)?", sent):
            reg(t.replace(",", ""), t)

    add("C1", "the rebuild reproduces %d of %d published values of paper-20 "
        "at equality, and all %d are located verbatim in the parent's "
        "committed receipt bytes"
        % (rb["anchors_equal"], rb["anchors"], rb["anchors_located"]))
    add("C2", "the welded record is n = 1 at %d of %d cells"
        % (ct["welded_cells_at_one"], ct["cells"]))
    add("C3", "the frozen control's %s branch-steps collapse to %d distinct "
        "measurements, one per level"
        % (com(ct["branch_steps_frozen_raw"]),
           ct["branch_steps_frozen_distinct"]))
    add("C4", "the coupled arm's %s branch-steps collapse to %s distinct "
        "measurements" % (com(ct["branch_steps_coupled_raw"]),
                          com(ct["branch_steps_coupled_distinct"])))
    add("C5", "the site-basis inverse participation of the Born menu is the "
        "sum of the squared site emission rates, D1 = sum_x eps(x)^2, at "
        "every one of the %s objects of both arms"
        % com(ct["branch_steps_coupled_distinct"]
              + ct["branch_steps_frozen_distinct"]))
    add("C6", "%d of %d exact cells are excluded because they hold "
        "identically on the frozen control, and %d survive as "
        "gravitational-decoherence relations"
        % (ex["excluded_count"], ex["exact_cells_tested"],
           ex["gravitational_count"]))
    add("C7", "the inverse participation does not move once in the %s "
        "object-and-field pairs at which it is checked, of %s checks over the "
        "three functionals and %d declared foreign count fields"
        % (com(me["object_field_pairs"]), com(me["checks"]),
           len(me["foreign_fields"])))
    add("C8", "the off-diagonal mass moves at %s of the %s object-and-field "
        "pairs, and at not one object no two of whose sites share two occupied "
        "links" % (com(me["D2_moves"]), com(me["object_field_pairs"])))
    add("C9", "the record-reading functional separates the arms at step %s, "
        "one step before either state-internal functional, which separate at "
        "step %s" % (pr["separation_ladder"]["D3"],
                     pr["separation_ladder"]["D1"]))
    add("C10", "the co-occupancy threshold is step %s on both arms"
        % me["cooccupancy_threshold_coupled"])
    add("C11", "%s of %s off-diagonal moduli are irrational"
        % (com(fn["l1_price"]["irrational_moduli"]),
           com(fn["l1_price"]["offdiagonal_entries"])))
    add("C12", "%d cells per arm are decided by equality inside a growth "
        "class: on the delivered arm %d exact, %d partial and %d vacuous; on "
        "the control %d, %d and %d"
        % (len(rl["grid_coupled"]), rl["exact"], rl["partial"], rl["vacuous"],
           rl["verdict_census_frozen"].get("EXACT", 0),
           rl["verdict_census_frozen"].get("PARTIAL", 0),
           rl["verdict_census_frozen"].get("VACUOUS", 0)))
    add("C13", "the separation ladder is identical across all %d executed "
        "fiber members" % ct["fiber_rows"])
    add("C14", "the cell-grain record leaves %s of %s objects in classes "
        "carrying more than one value of the inverse participation"
        % (com(_cellstat(R, "RES-BRANCH", "G1-RECORD-CELL", D_IDS[0])),
           com(ct["branch_steps_coupled_distinct"])))
    add("C15", "the fibers are run as declared axes, not as a product")
    add("C16", "%d of the %d coupled partial cells carry the identical verdict "
        "word on the frozen control, and %d of them have zero passing "
        "non-singleton classes"
        % (rl["coupled_partial_cells_with_the_identical_word_on_the_control"],
           rl["partial"], rl["total_failures"]))
    add("C17", "the law's own rate does not move once in %s object-and-field "
        "pairs, so the single exact cell relates a record-blind decoherence "
        "functional to a record-blind growth functional"
        % com(me["G5_checks"]))
    add("C18", "at the finest grain the mechanism holds at %s pair-checks: "
        "%s site pairs meeting in at most one occupied link move %d times"
        % (com(me["pair_checks"]),
           com(me["pair_census"]
               ["pairs_meeting_in_at_most_one_occupied_link"]["checks"]),
           me["pair_census"]["pairs_meeting_in_at_most_one_occupied_link"]
           ["moved"]))
    add("C19", "under a coin that is block-diagonal and unitary on every block "
        "but different at every site, the site marginal moves %d times and the "
        "inverse participation moves %d times in %s object-and-field pairs, "
        "while the off-diagonal mass moves %s"
        % (me["site_dependent_coin"]["site_marginal_moved"],
           me["site_dependent_coin"]["D1_moved"],
           com(me["site_dependent_coin"]["object_field_pairs"]),
           com(me["site_dependent_coin"]["D2_moved"])))
    add("C20", "a site occupied on two links first appears at step %s and a "
        "pair of sites sharing two occupied links first appears at step %s"
        % (me["single_site_threshold_coupled"],
           me["cooccupancy_threshold_coupled"]))
    add("C21", "the two state-internal functionals move %d times on %d "
        "declared congruent-but-different record fields and the record-reading "
        "one moves %s"
        % (rs["state_internal_moves"], len(rs["rows"]),
           com(rs["record_reading_moves"])))
    add("C22", "%s cells at level %s carry a count above 3 and every one of "
        "them is congruent to the welded value, while %d wrapped cells are "
        "read anywhere inside the declared horizon"
        % (com(rs["wrapped_cells_written"]),
           rs["first_step_at_which_a_wrapped_cell_is_written"],
           rs["wrapped_cells_read"]))
    add("C23", "%d of %d arms of the declared outcome grammar are emitted by a "
        "witness configuration through the same selector"
        % (len(oc["arms_reached"]), oc["arms_declared"]))
    return out


def paper_tables(R):
    """the paper's tables, ALL EIGHT OF THEM, RENDERED FROM THE RECEIPT (E-22:
    tables render as claims).  The first delivery rendered four and a swap
    inside any of the other four -- the relation grid, the anchor table, the
    fiber table and the choice inventory, which is to say the unit's central
    result and its provenance -- passed at exit 0."""
    rows = []
    # 1. the separation ladder
    for r in R["prediction"]["separation_rows"]:
        rows.append("| `%s` | %s |" % (r["functional"],
                                       r["first_separating_step"]))
    # 2. the blindness census
    for r in R["mechanism"]["rows"]:
        rows.append("| `%s` | %d | %s | %s |"
                    % (r["field"], r["moved"]["D1"], com(r["moved"]["D2"]),
                       com(r["moved"]["D3"])))
    # 3. the co-occupancy ladder
    for r in R["mechanism"]["cooccupancy_ladder_coupled"]:
        rows.append("| %d | %s | %s |" % (r["t"], com(r["objects"]),
                                          com(r["with_a_cooccupancy_pair"])))
    # 4. the dominations
    for r in R["prediction"]["domination_rows"]:
        rows.append("| `%s` | %s | %s |"
                    % (r["functional"], r["separating_steps"], r["verdict"]))
    # 5. THE RELATION GRID -- the unit's central result
    for g in G_IDS:
        cells = []
        for d in D_IDS:
            row = [x for x in R["relation"]["grid_coupled"]
                   if x["resolution"] == "RES-BRANCH" and x["growth"] == g
                   and x["decoherence"] == d][0]
            if row["verdict"] == "EXACT":
                cells.append("**EXACT**, `%d` of `%d`"
                             % (row["failing_classes"],
                                row["nonsingleton_classes"]))
            else:
                cells.append("%s, `%d` of `%d`"
                             % (row["stamp"], row["failing_classes"],
                                row["nonsingleton_classes"]))
        rows.append("| `%s` | %s |" % (g, " | ".join(cells)))
    # 6. THE ANCHOR TABLE (the quotes of the list rendering dropped, nothing
    #    else: the value compared at the gate is the value published here)
    for r in R["rebuild"]["anchor_rows"]:
        rows.append("| %s | `%s` |" % (r["what"], r["rebuilt"].replace("'", "")))
    # 7. THE FIBER TABLE
    for r in R["forcedness"]["rows"]:
        rows.append("| `%s`%s | `%d` | `%d` | %s | %s | `%s` |"
                    % (r["coin"],
                       "" if r["reading"] == DELIVERED_READING
                       else ", record menu",
                       r["branch_steps_coupled_distinct"],
                       r["branch_steps_frozen_distinct"],
                       r["single_site_threshold_coupled"],
                       r["cooccupancy_threshold_coupled"],
                       r["cell_signature"]))
    # 8. THE CHOICE INVENTORY
    for r in R["choices"]["rows"]:
        rows.append("| %d | `%s` | **%s** | %d | %s |"
                    % (r["n"], r["item"], r["status"], r["fiber"], r["note"]))
    for t in rows:
        for m in re.findall(r"\d[\d,]*(?:/\d+)?", t):
            reg(m.replace(",", ""), m)
    return rows


def receipt_numbers(R):
    ser = json.dumps(R, sort_keys=True, default=str)
    out = set(re.findall(r"-?\d+(?:/\d+)?", ser))
    out |= {t.replace(",", "") for t in re.findall(r"\d[\d,]*", ser)}
    for tok in list(out):
        out.add(tok.lstrip("-"))
    return out


FENCE_RE = re.compile(r"```.*?```", re.S)
INLINE_RE = re.compile(r"`[^`]*`")
NUM_PROSE_RE = re.compile(r"(?<![\w.\-/])\d[\d,]*(?:/\d+)?(?![\w])")
NUM_FENCED_RE = re.compile(r"(?<![\w./])\d[\d,]*(?:/\d+)?(?![\w])")


def head_numbers(R):
    out = set()
    for v in sorted(R.get("verdict", {}).values()):
        for t in NUM_FENCED_RE.findall(v):
            out.add(t.replace(",", ""))
    return out


def paper_coverage(R, text):
    """#20 WITH THE FENCED-BLOCK ADDENDUM AND E-22's INLINE-SPAN ADDENDUM: the
    scan covers prose, fenced/verdict blocks AND inline code spans, because a
    backticked numeral is a claim like any other."""
    without_fences = FENCE_RE.sub(" ", text)
    blocks = FENCE_RE.findall(text)
    spans = INLINE_RE.findall(without_fences)
    prose = INLINE_RE.sub(" ", without_fences)
    # THE ALLOWLIST IS BUILT FROM THE MEASURED KEYS ONLY (K3 MAJOR-4).  The
    # first delivery serialized the WHOLE receipt, so the instrument's own
    # self-description -- the seal digests' digit runs, the gate registry, the
    # source sha256-12s, the transcript head and, worst, THE DECLARED
    # FALSIFIER'S OWN NEEDLE -- entered the allowlist and a fabricated numeral
    # planted in the prose could never be flagged.
    known = (receipt_numbers({k: R[k] for k in MEASURED_KEYS if k in R})
             | NUMREG | NUM_ALLOW | head_numbers(R))
    scanned = allowed = fenced = inline = 0
    unreg = []
    targets = [(canon(prose), NUM_PROSE_RE, "prose")]
    targets += [(canon(b), NUM_FENCED_RE, "fenced") for b in blocks]
    targets += [(canon(s), NUM_FENCED_RE, "inline") for s in spans]
    for body, rx, kind in targets:
        for rawtok in rx.findall(body):
            tok = rawtok.replace(",", "")
            scanned += 1
            if kind == "fenced":
                fenced += 1
            elif kind == "inline":
                inline += 1
            if tok in known:
                allowed += 1
                continue
            unreg.append(tok)
    return {"scanned": scanned, "allowed": allowed,
            "fenced_blocks": len(blocks), "fenced_numerals": fenced,
            "inline_spans": len(spans), "inline_numerals": inline,
            "unregistered": sorted(set(unreg))}


def block_multiset(text):
    """E-22: the fenced blocks as a MULTISET.  Containment is not identity."""
    out = Counter()
    for b in FENCE_RE.findall(text):
        out[canon(b)] += 1
    return out


def paper_polarity(R, text, mutated=False):
    pos_needles = [
        ("P1", "GDL-DECOUPLED-AT-THE-GRAVITATIONAL-BAR", "GDL-PARTIAL"),
        ("P2", "the record does not determine the decoherence",
         "the record determines the decoherence"),
        ("P3", "the inherited observable is record-blind",
         "the inherited observable reads the record"),
        ("P4", "cited for shape only", "cited for its numbers"),
        ("P5", "the record the coin reads is Z/3",
         "the record the coin reads is the metric"),
        ("P6", "gravitational d=f(g) cells=0", "gravitational d=f(g) cells=1"),
    ]
    out = []
    for pid, pos, neg in pos_needles:
        if mutated:
            pos, neg = neg, pos
        # CASE-INSENSITIVE on top of the #125 normalisation: a claim written
        # in the head's upper case and in the prose's sentence case is the
        # same claim, and a gate that missed one of the two would be evadable
        # by re-casing.
        hay = canon(text).lower()
        have_pos = canon(pos).lower() in hay
        have_neg = canon(neg).lower() in hay
        out.append({"id": pid, "positive": pos, "negative": neg,
                    "positive_present": have_pos,
                    "negative_present": have_neg,
                    "ok": have_pos and not have_neg})
    return out


def paper_gates(LD, SEAL, R, text):
    # THE NUMERAL FALSIFIER PLANTS ITS NUMERAL IN THE PAPER, not in the gate's
    # own input (K3 MAJOR-4): a falsifier that bypasses the scan tests nothing.
    text = pick("MUT-PAPER-NUMERAL", text, text + "\n\n" + "123456789" + "\n")
    claims = paper_claims(R)
    missing = []
    for c in claims:
        sent = c["sentence"]
        if mut("MUT-PAPER-CLAIM") and c["id"] == "C2":
            sent = sent.replace("27 of 27 cells", "26 cells")
        c["present"] = canon(sent) in canon(text)
        c["as_checked"] = sent
        if not c["present"]:
            missing.append(c["id"])
    R["paper_claims"] = claims
    LD.gate("G-PAPER-CLAIMS",
            "every load-bearing claim of the paper is ASSEMBLED FROM THE "
            "RECEIPT and then located in the object under test -- %d claims, "
            "no number typed twice" % len(claims),
            not missing, "claims not located: %s" % (missing or "none"))
    SEAL.take("SEAL-PAPER-CLAIMS", R)

    trows = paper_tables(R)
    if mut("MUT-PAPER-TABLE"):
        trows = trows[:-1] + ["| `FORGED` | 9 | 9 |"]
    tmiss = [t for t in trows if canon(t) not in canon(text)]
    R["paper_tables"] = {"rows": trows, "count": len(trows),
                         "missing": tmiss}
    LD.gate("G-PAPER-TABLES",
            "the paper's tables RENDER FROM THE RECEIPT: %d rows are built "
            "from measured values and each is required to appear in the "
            "object under test" % len(trows),
            not tmiss, "table rows not located: %s" % (tmiss or "none"))
    SEAL.take("SEAL-PAPER-TABLES", R)

    cov = paper_coverage(R, text)
    unregistered = cov["unregistered"]
    R["paper_coverage"] = cov
    LD.gate("G-PAPER-NUMERAL-COVERAGE",
            "#20 WITH THE FENCED-BLOCK AND INLINE-SPAN ADDENDA (E-22): the "
            "coverage scan reads ALL of the paper's text -- %d prose-and-other "
            "numerals of which %d live in %d fenced blocks and %d in %d inline "
            "code spans -- and every numeral must be a value this run computed "
            "and registered"
            % (cov["scanned"], cov["fenced_numerals"], cov["fenced_blocks"],
               cov["inline_numerals"], cov["inline_spans"]),
            not unregistered, "unregistered numerals: %s"
            % (unregistered or "none"))

    segs = list(R["verdict"].values())
    bad = []
    for i, seg in enumerate(segs):
        probe = pick("MUT-PAPER-HEAD", seg, seg[:-1] + "Z")
        if canon(probe) not in canon(text):
            bad.append(i)
    # E-22 IN MECHANISM AND NOT ONLY IN NAME: the comparison is FULL MULTISET
    # EQUALITY in both directions.  The first delivery compared only
    # want -> have, so an EXTRA fenced block was invisible and a duplicated
    # head segment with a forged twin passed at exit 0 -- the exact scenario
    # E-22 was bought for.  This paper's fences are exactly its head segments,
    # so equality is the right predicate.
    extra_fence = Counter({canon("```\nEXTRA\n```"): 1})
    blockmap = pick("MUT-PAPER-BLOCK", block_multiset(text),
                    block_multiset(text) + extra_fence)
    want = Counter(canon("```\n%s\n```" % s) for s in segs)
    mult_bad = [k for k in set(want) | set(blockmap)
                if blockmap.get(k, 0) != want.get(k, 0)]
    R["paper_coverage"]["head_segments"] = len(segs)
    R["paper_coverage"]["fenced_block_multiset_size"] = sum(blockmap.values())
    R["paper_coverage"]["fenced_block_multiset_matches_the_head_exactly"] = (
        not mult_bad)
    LD.gate("G-PAPER-HEAD-VERBATIM",
            "the paper's verdict block is the DERIVED head, rendered from the "
            "receipt: all %d segments are located verbatim, and the fenced "
            "blocks are gated by MULTISET EQUALITY IN BOTH DIRECTIONS (E-22) "
            "rather than by containment -- the paper's fenced blocks must BE "
            "the head's segments, one for one, so neither a duplicated block "
            "shadowing a forged twin nor an extra fence of any kind survives"
            % len(segs),
            not bad and not mult_bad,
            "segments not located %s; multiset mismatches %d (%d fenced blocks "
            "in the paper against %d head segments)"
            % (bad or "none", len(mult_bad), sum(blockmap.values()),
               len(segs)))
    SEAL.take("SEAL-PAPER-COVERAGE", R)

    mutated = pick("MUT-PAPER-POLARITY", False, True)
    pol = paper_polarity(R, text, mutated)
    R["polarity"] = pol
    LD.gate("G-PAPER-CLAIM-POLARITY",
            "every load-bearing claim is checked for POLARITY: the positive "
            "form must be present and its negation absent, on %d pairs, so a "
            "paper carrying the opposite of what was measured dies here"
            % len(pol),
            all(p["ok"] for p in pol),
            "polarity rows failing: %s"
            % ([p["id"] for p in pol if not p["ok"]] or "none"))
    SEAL.take("SEAL-POLARITY", R)


# ===========================================================================
# CLOSING: coverage, falsifier honesty, writer shape, the seal, the artifacts
# ===========================================================================

TERMINAL_GATE = "G-ARTIFACT-INTEGRITY"


def writer_shape():
    """THE SHAPE OF THE WRITER, measured from this file's own AST BEFORE the
    gate ledger is snapshotted: the gate names finish() calls, in order, and
    the line of every os.replace, each required to sit BELOW the terminal
    gate's own line.  Dropping or renaming that gate moves a SEALED value."""
    src = read_text(SELF)
    tree = ast.parse(src)
    fn = None
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "finish":
            fn = node
    if fn is None:
        return {"finish_found": False}
    names = []
    gate_lines = {}
    replaces = []
    for n in ast.walk(fn):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute):
            if n.func.attr == "gate" and n.args and \
                    isinstance(n.args[0], ast.Constant):
                names.append(n.args[0].value)
                gate_lines[n.args[0].value] = n.lineno
            if n.func.attr == "replace":
                replaces.append(n.lineno)
    names.sort(key=lambda g: gate_lines[g])
    terminal_line = gate_lines.get(TERMINAL_GATE)
    return {"finish_found": True,
            "gate_names_in_finish": names,
            "terminal_gate": TERMINAL_GATE,
            "terminal_gate_present_exactly_once":
                names.count(TERMINAL_GATE) == 1,
            "os_replace_calls": len(replaces),
            "every_replace_after_the_terminal_gate":
                bool(terminal_line) and all(r > terminal_line
                                            for r in replaces)}


def _targets_of(node):
    """the names a statement ASSIGNS to, subscript and attribute targets
    resolved to their last key -- so `R["counts"]["horizon"] = ...` declares
    the symbol `horizon`."""
    out = set()
    tgts = []
    if isinstance(node, ast.Assign):
        tgts = list(node.targets)
    elif isinstance(node, (ast.AugAssign, ast.AnnAssign)):
        tgts = [node.target]
    else:
        for c in ast.walk(node):
            if isinstance(c, ast.Assign):
                tgts.extend(c.targets)
            elif isinstance(c, (ast.AugAssign, ast.AnnAssign)):
                tgts.append(c.target)
    for t in tgts:
        for n in ast.walk(t):
            if isinstance(n, ast.Name):
                out.add(n.id)
            elif isinstance(n, ast.Attribute):
                out.add(n.attr)
            elif isinstance(n, ast.Subscript) and \
                    isinstance(n.slice, ast.Constant) and \
                    isinstance(n.slice.value, str):
                out.add(n.slice.value)
    return out


def _token_in(needle, hay):
    """the needle occurs in the source as a WHOLE token, so a declared value
    `1` is not satisfied by the `1` inside the identifier `D1`."""
    return re.search(r"(?<![\w.])%s(?![\w.])" % re.escape(needle),
                     hay) is not None


def falsifier_hooks():
    """E-23 MADE SEMANTIC.  For every declared falsifier this returns, from
    THIS FILE'S OWN AST rather than from its text:

      * the SYMBOLS the hook's enclosing statement actually ASSIGNS TO;
      * the SOURCE of the corrupting expression -- the third argument of
        `pick(NAME, honest, corrupt)`, or the whole hook statement for a
        `mut(NAME)` branch;
      * the SOURCE of the honest expression, where there is one.

    Substring containment on the raw text -- which is what the first delivery
    of this unit checked -- cannot tell a true declaration from a false one:
    a falsifier declared to move a symbol to `0` while its code writes `1`
    passed, because `0` occurred somewhere in the segment."""
    src = read_text(SELF)
    tree = ast.parse(src)
    found = defaultdict(list)
    for node in ast.walk(tree):
        if not isinstance(node, ast.stmt):
            continue
        calls = {}
        for c in ast.walk(node):
            if isinstance(c, ast.Call) and isinstance(c.func, ast.Name) \
                    and c.func.id in ("pick", "mut") and c.args \
                    and isinstance(c.args[0], ast.Constant):
                calls[c.args[0].value] = c
        if not calls:
            continue
        seg = ast.get_source_segment(src, node) or ""
        lo, hi = node.lineno, (node.end_lineno or node.lineno)
        for nm, c in calls.items():
            honest = corrupt = None
            if c.func.id == "pick" and len(c.args) >= 3:
                honest = ast.unparse(c.args[1])
                corrupt = ast.unparse(c.args[2])
            else:
                corrupt = seg
            found[nm].append((lo, hi, seg, sorted(_targets_of(node)),
                              honest, corrupt))
    out = {}
    for nm, rows in found.items():
        keep = [r for r in rows
                if not any(o is not r and r[0] <= o[0] and o[1] <= r[1]
                           and (o[1] - o[0]) < (r[1] - r[0]) for o in rows)]
        out[nm] = [{"source": r[2], "assigns": r[3], "honest": r[4],
                    "corrupt": r[5]} for r in sorted(keep)]
    return out


def seal_window():
    """THE SEAL WINDOW, re-derived from this file's AST: for every `SEAL.take`
    site, the name of the NEAREST PRECEDING `LD.gate` in the same function.  A
    seal whose published `sealed_at_gate` is not a window it is actually taken
    in is a mislabelled seal, and the manifest must not carry one."""
    tree = ast.parse(read_text(SELF))
    windows = defaultdict(set)
    for fn in ast.walk(tree):
        if not isinstance(fn, ast.FunctionDef):
            continue
        marks = []
        for n in ast.walk(fn):
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \
                    and n.args and isinstance(n.args[0], ast.Constant):
                if n.func.attr == "gate":
                    marks.append((n.lineno, "GATE", n.args[0].value))
                elif n.func.attr == "take":
                    marks.append((n.lineno, "TAKE", n.args[0].value))
        cur = None
        for _ln, kind, val in sorted(marks):
            if kind == "GATE":
                cur = val
            elif cur is not None:
                windows[val].add(cur)
    return {k: sorted(v) for k, v in windows.items()}


def waiver_ledger():
    return {
        "G-PROVENANCE": ("FALSIFIED-BY-A-FLAG",
                         "--break-anchor NAME corrupts any source's expected "
                         "digest and the run dies here; a mutant would be a "
                         "second, weaker copy of the same falsifier"),
        "G-EXACT-ARITHMETIC": ("SELF-SCANNING",
                               "the gate parses this file; a mutant that "
                               "introduced a float would fail it by "
                               "construction"),
        "G-NO-SUBPROCESS": ("SELF-SCANNING",
                            "same: the gate parses this file's own imports, "
                            "and the independence of the rebuild is exactly "
                            "what it certifies"),
        "G-READS-DECLARED": ("STRUCTURAL",
                             "the source read list is appended by read_bytes, "
                             "the only reader of a SOURCE in the file; the "
                             "second reader, read_text, reads only the two "
                             "files of the declared OBJECT set"),
        "G-VERBATIM": ("SELF-FALSIFYING-PER-ROW",
                       "every anchor is perturbed at its last three "
                       "characters and re-located inside the gate, so each "
                       "row carries its own falsifier"),
        "G-COVERAGE": ("SELF-REFERENTIAL", "the gate IS the coverage ledger"),
        "G-REACHABILITY": ("SELF-REFERENTIAL", "same"),
        "G-MUTANTS-ON-TARGET": ("SELF-REFERENTIAL",
                                "the gate IS the mutant sweep"),
        "G-ANCHOR-CONSUMERS": ("STRUCTURAL",
                               "the gate compares two registries this file "
                               "owns"),
        "G-ARTIFACT-INTEGRITY": (
            "EXERCISED-IN-RUN-AND-GUARDED-BY-THE-WRITER-SHAPE",
            "a mutant on this gate is UNREACHABLE by construction -- "
            "run_mutant calls finish(write=False), which returns before the "
            "terminal gate runs -- so the waiver states the two things that "
            "do guard it.  (i) EXERCISED: the run corrupts a read-back copy "
            "of EVERY sealed row in turn and requires each corruption to be "
            "detected before the real artifacts are compared.  (ii) "
            "EXISTENCE: G-WRITER-SHAPE reads this file's AST BEFORE the gate "
            "ledger is snapshotted and publishes the gate names finish() "
            "calls together with the line of every os.replace, so dropping or "
            "renaming this gate, or moving a write above it, moves a SEALED "
            "published value"),
        "G-PAPER-COVERAGE-FINAL": ("AGGREGATE",
                                   "it closes over gates each of which is "
                                   "separately falsified"),
    }


LATE_GATES = ("G-PAPER-COVERAGE-FINAL", "G-SEAL-COMPLETE",
              "G-ARTIFACT-INTEGRITY")
SWEEP_GATE = "G-MUTANTS-ON-TARGET"
LEDGER_GATES = ("G-COVERAGE", "G-REACHABILITY")
CLOSING_LEDGER_GATES = ("G-SWEEP-BOUND", "G-ANCHOR-CONSUMERS",
                        "G-FALSIFIER-HONESTY", "G-WRITER-SHAPE")

GATE_REGISTRY = [
    "G-PROVENANCE", "G-EXACT-ARITHMETIC", "G-NO-SUBPROCESS",
    "G-READS-DECLARED", "G-VERBATIM",
    "G-PARENT-REPRODUCED", "G-PARENT-LOCATED",
    "G-ENSEMBLE-EXHAUSTIVE", "G-BRANCH-MASS",
    "G-WALK-UNITARY", "G-LAW-KERNEL", "G-LAW-CHECK-CLASSES",
    "G-FUNCTIONALS-DECLARED", "G-FUNCTIONALS-EXACT", "G-L1-PRICED",
    "G-PURITY-SPLIT",
    "G-RATE-IS-BORN", "G-RATE-TOTAL", "G-GROWTH-FROZEN-ZERO",
    "G-RELATION-CENSUS", "G-VACUITY-DECLARED", "G-FAILURE-CENSUS",
    "G-TOTAL-FAILURE-STAMP", "G-FROZEN-GRID-CENSUS", "G-NO-FITTED-FORM",
    "G-COIN-ADMISSIBLE", "G-COIN-FIBER", "G-FIBER-EXECUTED",
    "G-GLOBAL-PHASE-PAIR", "G-FROZEN-CONTROL", "G-FROZEN-EXCLUSION",
    "G-SEPARATION-LADDER", "G-DOMINATION",
    "G-BLINDNESS-D1", "G-BLINDNESS-D3", "G-COOCCUPANCY",
    "G-COOCCUPANCY-THRESHOLD", "G-OCCUPANCY-PREDICATES",
    "G-PAIR-MECHANISM", "G-BLINDNESS-G5", "G-THEOREM-A", "G-THEOREM-B",
    "G-FOREIGN-FIELDS-FOREIGN",
    "G-RESIDUE-CHANNEL", "G-RESIDUE-WRAPAROUND",
    "G-PREDICTION-ROW", "G-PREDICTION-RENDERED",
    "G-WALL-L1", "G-WALL-BHS", "G-WALL-KR", "G-WALL-COSMO", "G-WALL-NO-SI",
    "G-WALL-DP-SHAPE", "G-WALL-LORENTZ-NAMED", "G-WALL-HEX-NAMED",
    "G-MEASURE-DECLARED", "G-CHOICE-INVENTORY", "G-OUTCOME-REACHABILITY",
    "G-VERDICT-RECONSTRUCTED",
    "G-PAPER-CLAIMS", "G-PAPER-TABLES", "G-PAPER-NUMERAL-COVERAGE",
    "G-PAPER-HEAD-VERBATIM", "G-PAPER-CLAIM-POLARITY",
    "G-CLI-WHITELIST", "G-SELFTEST-WRITES-NOTHING", "G-MUTANTS-ON-TARGET",
    "G-COVERAGE", "G-FALSIFIER-HONESTY", "G-WRITER-SHAPE",
    "G-SWEEP-BOUND", "G-ANCHOR-CONSUMERS", "G-REACHABILITY",
    "G-PAPER-COVERAGE-FINAL", "G-SEAL-COMPLETE", "G-ARTIFACT-INTEGRITY",
]


def emit_report(R, LD):
    say("")
    say("-" * 78)
    say("TOTALS: %d sources, %d verbatim anchors, %d gates in the registry "
        "(%d in the sealed snapshot, %d after it), %d mutants, %d seals, "
        "%d relation cells per arm, %d fiber rows, horizon %d, %s "
        "blindness checks"
        % (R["totals"]["sources"], R["totals"]["verbatim_anchors"],
           R["totals"]["gates_in_the_registry"],
           R["totals"]["gates_evaluated_before_the_snapshot"],
           R["totals"]["gates_after_the_snapshot"],
           R["totals"]["mutants"], R["totals"]["seals"],
           R["totals"]["relation_cells"], R["totals"]["fiber_rows"],
           R["totals"]["horizon"], com(R["totals"]["blindness_checks"])))
    say("-" * 78)


def finish(LD, SEAL, R, verdict, write=True, swept=False):
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
        "honest_denominator": len(gate_names)}
    R["waiver_ledger"] = [{"gate": g, "class": w[0], "reason": w[1]}
                          for g, w in sorted(waivers.items())]
    LD.gate("G-COVERAGE",
            "#34 WITH AN HONEST DENOMINATOR: of the %d gates this delivery run "
            "evaluates, %d are falsified by at least one declared mutant and "
            "%d are WAIVED with a forcing that says why they cannot fail.  The "
            "denominator is the gate count of THIS run, and the registry "
            "--list-gates prints is required to be EXACTLY that set"
            % (len(gate_names),
               sum(1 for g in gate_names if targeted.get(g)), len(waivers)),
            not uncovered and not registry_drift,
            "uncovered gates: %s; declared registry %d vs evaluated %d, drift "
            "%s" % (uncovered or "none", len(GATE_REGISTRY), len(gate_names),
                    registry_drift or "none"))
    SEAL.take("SEAL-COVERAGE", R)
    SEAL.take("SEAL-WAIVERS", R)

    hooks = falsifier_hooks()
    hook_rows = []
    desc_bad = []
    hook_bad = []
    for name, gate, why, moves, to in MUTANTS:
        declared = (moves, to)
        if mut("MUT-FALSIFIER-DESC") and name == "MUT-KERNEL":
            declared = ("FORGED", "FORGED")
        segs = hooks.get(name, [])
        # LEG 1 -- THE SYMBOL IS AN ASSIGNMENT TARGET, not a substring.
        # LEG 2 -- THE VALUE IS A WHOLE TOKEN OF THE CORRUPTING EXPRESSION'S
        #          OWN SOURCE, and the corrupting expression differs from the
        #          honest one, so a falsifier that changes nothing is caught.
        code_ok = any(declared[0] in s["assigns"]
                      and _token_in(declared[1], s["corrupt"])
                      and s["corrupt"] != s["honest"] for s in segs)
        # LEG 3 -- THE PROSE CARRIES THE CLAUSE THE AST ASSEMBLES, contiguously
        #          and in order, so a description that keeps the symbol and the
        #          value as loose tokens while saying the opposite is caught.
        clause = "moves `%s` to %s" % (declared[0], declared[1])
        prose_ok = canon(clause) in canon(why)
        hook_rows.append({"mutant": name, "gate": gate, "what_it_does": why,
                          "moves": declared[0], "to": declared[1],
                          "assembled_clause": clause,
                          "hook_sites": len(segs),
                          "assigns": sorted({a for s in segs
                                             for a in s["assigns"]}),
                          "matches_its_code": code_ok,
                          "named_in_its_description": prose_ok})
        if not code_ok:
            hook_bad.append(name)
        if not prose_ok:
            desc_bad.append(name)
    undeclared_hooks = sorted(set(hooks) - MUTANT_NAMES)
    R["mutants"] = hook_rows
    LD.gate("G-FALSIFIER-HONESTY",
            "E-23 IS SEMANTIC HERE, NOT A SUBSTRING SEARCH.  Each of the %d "
            "declared falsifiers names THE SYMBOL IT MOVES and THE VALUE IT "
            "MOVES IT TO, and three legs bind the declaration to the code: the "
            "SYMBOL must be an ASSIGNMENT TARGET of the hook's own statement, "
            "re-derived from this file's AST; the VALUE must occur as a WHOLE "
            "TOKEN in the source of the CORRUPTING expression -- the third "
            "argument of its `pick` -- which must itself differ from the "
            "honest one; and the published prose must carry, contiguously, THE "
            "CLAUSE THE AST ASSEMBLES from those two.  A declaration that "
            "names a value its code does not write, and a description that "
            "keeps the symbol and the value while saying the opposite of what "
            "the hook does, both die here.  %d hook sites are located, and "
            "every hook in the file names a declared falsifier"
            % (len(MUTANTS), sum(len(v) for v in hooks.values())),
            not hook_bad and not desc_bad and not undeclared_hooks,
            "declarations not matching their code: %s; descriptions not "
            "carrying their assembled clause: %s; hooks naming an undeclared "
            "falsifier: %s" % (hook_bad or "none", desc_bad or "none",
                               undeclared_hooks or "none"))
    SEAL.take("SEAL-MUTANTS", R)

    ws = writer_shape()
    if mut("MUT-WRITER-SHAPE"):
        ws = dict(ws)
        ws["gate_names_in_finish"] = ws["gate_names_in_finish"][:-1]
    ws["terminal_gate_present_exactly_once"] = (
        ws["gate_names_in_finish"].count(TERMINAL_GATE) == 1)
    R["writer_shape"] = ws
    LD.gate("G-WRITER-SHAPE",
            "THE SHAPE OF THE WRITER IS SEALED, AND SEALED BEFORE THE GATE "
            "LEDGER IS SNAPSHOTTED -- the one guard a post-snapshot gate's own "
            "removal cannot evade.  finish() calls %d gates in source order, "
            "the terminal integrity gate appears exactly once among them, "
            "there are %d os.replace calls, and every one sits BELOW that "
            "gate's own line"
            % (len(ws["gate_names_in_finish"]), ws["os_replace_calls"]),
            (ws["finish_found"] and ws["terminal_gate_present_exactly_once"]
             and ws["os_replace_calls"] == 2
             and ws["every_replace_after_the_terminal_gate"]),
            "gates called in finish %s; terminal gate present exactly once %s; "
            "os.replace calls %d, all after the terminal gate %s"
            % (ws["gate_names_in_finish"],
               ws["terminal_gate_present_exactly_once"],
               ws["os_replace_calls"],
               ws["every_replace_after_the_terminal_gate"]))
    SEAL.take("SEAL-WRITER-SHAPE", R)

    swept = pick("MUT-SWEEP-UNBOUND", swept, True)
    R.setdefault("mutant_sweep", [])
    sweep_rows = R.get("mutant_sweep") or []
    ran_here = {g["gate"] for g in LD.rows}
    # THE SWEEP IS BOUND TO EXECUTION AND NOT TO THE CONTENT OF ITS OWN ROWS.
    # Every row must carry THE EVIDENCE STRING ITS GATE ACTUALLY RAISED, that
    # string must name the row's own gate, and the number of times run_mutant
    # actually entered its body must equal the number of rows: a delivery-level
    # run that executes no mutant at all cannot publish a complete sweep.
    ev_bad = [k.get("mutant") for k in sweep_rows
              if not k.get("evidence")
              or not str(k.get("evidence", "")).startswith(
                  str(k.get("declared_gate", "\0")) + " ::")]
    runs = MUTANT_RUNS[0]
    sweep_ok = (not swept) or (
        len(sweep_rows) == len(MUTANTS)
        and all(k.get("on_target") for k in sweep_rows)
        and not ev_bad and runs >= len(MUTANTS)
        and SWEEP_GATE in ran_here)
    LD.gate("G-SWEEP-BOUND",
            "THE SWEEP'S EXECUTION IS BOUND, NOT DECLARED: a delivery-level "
            "run must carry one sweep row per declared mutant (%d), every row "
            "ON TARGET, EVERY ROW CARRYING THE EVIDENCE STRING ITS GATE "
            "ACTUALLY RAISED AND NAMING ITS OWN GATE, at least %d executions "
            "counted inside the harness itself, and it must have evaluated the "
            "sweep gate.  A run that publishes a complete on-target sweep "
            "without executing a single falsifier dies here.  This run is %s "
            "and counted %d executions"
            % (len(MUTANTS), len(MUTANTS),
               "delivery-level" if swept else "a sub-pipeline", runs),
            sweep_ok, "sweep rows %d of %d; rows with no or mismatched gate "
            "evidence %s; harness executions %d; sweep gate evaluated %s"
            % (len(sweep_rows), len(MUTANTS), ev_bad or "none", runs,
               SWEEP_GATE in ran_here))
    SEAL.take("SEAL-MUTANT-SWEEP", R)

    consumers = {v[3] for v in VERBATIM}
    bad_consumers = sorted(c for c in consumers
                           if c not in GATE_REGISTRY or c not in ran_here)
    LD.gate("G-ANCHOR-CONSUMERS",
            "#62's consumer binding: every verbatim anchor names a gate, and "
            "each named gate is required to be in the DECLARED registry AND in "
            "THIS RUN's own evaluated ledger -- %d distinct consumer gates"
            % len(consumers),
            not bad_consumers, "consumers not registered-and-evaluated: %s"
            % (bad_consumers or "none"))

    reach = []
    for name, gate, _why, _mv, _to in MUTANTS:
        reach.append({"mutant": name, "gate": gate,
                      "gate_registered": gate in GATE_REGISTRY,
                      "gate_evaluated_or_declared_later":
                          gate in ran_here or gate in LATE_GATES
                          or gate in LEDGER_GATES
                          or gate in CLOSING_LEDGER_GATES
                          or gate == SWEEP_GATE})
    dead = [r["mutant"] for r in reach
            if not (r["gate_registered"]
                    and r["gate_evaluated_or_declared_later"])]
    R["reachability"] = {"rows": reach, "dead_falsifiers": dead}
    LD.gate("G-REACHABILITY",
            "#34 WITH REACHABILITY: every declared falsifier is checked to "
            "REACH its gate -- %d falsifiers, %d dead" % (len(reach),
                                                          len(dead)),
            not dead, "dead falsifiers: %s" % (dead or "none"))
    SEAL.take("SEAL-REACHABILITY", R)

    R["totals"] = {
        "sources": len(SOURCES), "verbatim_anchors": len(R["verbatim_anchors"]),
        "gates_in_the_registry": len(GATE_REGISTRY),
        "gates_evaluated_before_the_snapshot": len(LD.rows) + 1,
        "gates_after_the_snapshot": len(LATE_GATES) - 1,
        "gates": len(LD.rows) + 1,
        "mutants": len(MUTANTS), "seals": len(SEALED_PATHS),
        "horizon": HORIZON,
        "relation_cells": len(R["relation"]["grid_coupled"]),
        "fiber_rows": len(R["forcedness"]["rows"]),
        "blindness_checks": R["mechanism"]["checks"],
        "declared_unsealed": len(DECLARED_UNSEALED),
        "waivers": len(R["waiver_ledger"])}
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
    names_now = ({g["gate"] for g in LD.rows} | {"G-PAPER-COVERAGE-FINAL"}
                 | set(LATE_GATES[1:]))
    names_ok = (not swept) or names_now == set(GATE_REGISTRY)
    LD.gate("G-PAPER-COVERAGE-FINAL",
            "the payload closes.  THE THREE GATE CARDINALITIES ARE NAMED "
            "RATHER THAN CONFLATED: %d gates in the DECLARED REGISTRY, %d "
            "evaluated and carried into the SEALED SNAPSHOT (this gate "
            "included), and %d evaluated AFTER the snapshot.  All passed, and "
            "a RECURSIVE TYPE SCAN of the receipt finds no float anywhere"
            % (len(GATE_REGISTRY), len(LD.rows) + 1, len(LATE_GATES) - 1),
            all(g["passed"] for g in LD.rows) and not bad_types and names_ok,
            "registry %d, snapshot %d, post-snapshot %d, snapshot names equal "
            "the registry %s (%s), float-valued receipt paths %s"
            % (len(GATE_REGISTRY), len(LD.rows) + 1, len(LATE_GATES) - 1,
               names_ok, "delivery-level" if swept else "sub-pipeline, not "
               "asserted", bad_types or "none"))
    R["gates"] = [dict(g) for g in LD.rows]
    R["closing_gates"] = {
        "names": list(LATE_GATES[1:]),
        "gates_in_the_registry": len(GATE_REGISTRY),
        "gates_in_the_sealed_snapshot": len(R["gates"]),
        "gates_after_the_snapshot": len(LATE_GATES) - 1,
        "warrant": "these two are evaluated after the gate ledger is "
                   "snapshotted and sealed -- G-SEAL-COMPLETE cannot be inside "
                   "the object it seals, and G-ARTIFACT-INTEGRITY runs after "
                   "the bytes are on disk.  That gate's existence is witnessed "
                   "by G-WRITER-SHAPE, which reads this file's AST before the "
                   "snapshot"}
    R["transcript_head"] = ("\n".join(LINES) + "\n").split("\n")[:40]
    SEAL.take("SEAL-GATES", R)
    SEAL.take("SEAL-CLOSING", R)
    SEAL.take("SEAL-TOTALS", R)
    SEAL.take("SEAL-TRANSCRIPT", R)
    if mut("MUT-TRANSCRIPT-FLIP"):
        R["transcript_head"] = ["FLIPPED"] + R["transcript_head"][1:]
    if mut("MUT-SEAL-BROKEN"):
        R["counts"]["horizon"] = R["counts"]["horizon"] + 1
    missing, extra = SEAL.totality()
    declared = sorted(set(R.keys()))
    covered = sorted({r["path"] for r in SEAL.rows} | set(DECLARED_UNSEALED))
    uncovered_keys = sorted(set(declared) - set(covered))
    unsealed_frozen = (tuple(DECLARED_UNSEALED) == DECLARED_UNSEALED_FROZEN)
    unsealed_clean = not (set(DECLARED_UNSEALED)
                          & ({p for _s, p, _g in SEALED_PATHS}
                             | set(MEASURED_KEYS)))
    windows = seal_window()
    window_bad = sorted(s for s, _p, g in SEALED_PATHS
                        if g not in windows.get(s, []))
    R["seal_manifest"] = {"rows": SEAL.rows,
                          "windows_from_this_file_s_ast": windows,
                          "rows_whose_declared_gate_is_not_their_window":
                              window_bad,
                          "declared_unsealed": DECLARED_UNSEALED,
                          "declared_unsealed_frozen": unsealed_frozen,
                          "declared_unsealed_carries_no_measurement":
                              unsealed_clean,
                          "declared_unsealed_forcings":
                              [{"key": k, "forcing": UNSEALED_FORCING[k]}
                               for k in DECLARED_UNSEALED],
                          "declared_unsealed_are_chained_on_read_back": True,
                          "declared_seals": [s for s, _p, _g in SEALED_PATHS]}
    broken = SEAL.verify(R)
    LD.gate("G-SEAL-COMPLETE",
            "THE TOTAL SEAL.  EVERY published receipt key is either sealed at "
            "the gate that certified it or listed as DECLARED-UNSEALED, and "
            "this gate compares the manifest against the DECLARED seal set "
            "rather than against the seals that happened to be taken.  The "
            "vouching layer is inside the seal: schema, provenance, paper "
            "claims, polarity, coverage, reachability, gates, totals and the "
            "transcript head.  AND EVERY ROW'S PUBLISHED `sealed_at_gate` IS "
            "RE-DERIVED FROM THIS FILE'S AST -- the nearest preceding LD.gate "
            "of each SEAL.take site -- so a block seal taken after a block of "
            "gates says which gate it was actually taken at",
            not missing and not extra and not uncovered_keys and not broken
            and unsealed_frozen and unsealed_clean and not window_bad,
            "declared seals %d, taken %d, missing %s, extra %s, receipt keys "
            "not covered %s, seals broken at close %s, unsealed list frozen %s "
            "and measurement-free %s, rows whose declared gate is not their "
            "AST window %s"
            % (len(SEALED_PATHS), len(SEAL.rows), missing or "none",
               extra or "none", uncovered_keys or "none", broken or "none",
               unsealed_frozen, unsealed_clean, window_bad or "none"))
    payload = json.dumps(R, indent=1, sort_keys=True, default=str)
    emit_report(R, LD)
    text = "\n".join(LINES) + "\n"
    SEAL.close(R, payload, text)
    R["payload_sha256_12"] = SEAL.payload_sha
    if not write:
        return payload, text
    tmp_j, tmp_t = OUT_JSON + ".tmp", OUT_TXT + ".tmp"
    promoted = False
    try:
        final = json.dumps(R, indent=1, sort_keys=True, default=str)
        with open(tmp_j, "w", encoding="utf-8") as fh:
            fh.write(final + "\n")
        with open(tmp_t, "w", encoding="utf-8") as fh:
            fh.write(text)
        staged = read_text(tmp_j)
        try:
            back = json.loads(staged)
        except ValueError:
            # an unparseable staged payload is an INTEGRITY FAILURE reported by
            # the terminal gate, not a traceback out of the writer.
            back = {"unparseable_staged_payload": True}
        probes_caught = 0
        for row in SEAL.rows:
            probe = json.loads(json.dumps(back))
            cur = probe
            parts = row["path"].split("/")
            broke = False
            for part in parts[:-1]:
                try:
                    cur = cur[int(part)] if isinstance(cur, list) else cur[part]
                except (KeyError, IndexError, TypeError, ValueError):
                    broke = True
                    break
            if broke:
                probes_caught += 1
                continue
            key = parts[-1]
            if isinstance(cur, list):
                cur[int(key)] = ["PROBE"]
            elif isinstance(cur, dict):
                cur[key] = "PROBE"
            else:
                probes_caught += 1
                continue
            if row["seal"] in SEAL.verify(probe, only={row["seal"]}):
                probes_caught += 1
        probe_caught = probes_caught == len(SEAL.rows)
        disk_broken = SEAL.verify(back)
        back_text = read_text(tmp_t)
        head_ok = (back_text.split("\n")[:40] == R["transcript_head"])
        text_ok = digest(back_text) == SEAL.text_sha
        text_lines = len(back_text.split("\n"))
        chained_ok = (back.get("payload_sha256_12") == SEAL.payload_sha
                      and back.get("seal_manifest", {}).get("rows")
                      == SEAL.rows)
        ran = {g["gate"] for g in LD.rows}
        late_ok = all(g in ran for g in tuple(LEDGER_GATES) + LATE_GATES[:2]
                      + CLOSING_LEDGER_GATES + (SWEEP_GATE,))
        sweep_complete = (len(R.get("mutant_sweep") or []) == len(MUTANTS)
                          and all(k.get("on_target")
                                  for k in R.get("mutant_sweep") or []))
        parsed_ok = not back.get("unparseable_staged_payload")
        LD.gate("G-ARTIFACT-INTEGRITY",
                "INTEGRITY IS DISK-VS-SEAL, never a re-derivation: the payload "
                "is written from the SEALED object to a staged file, read back "
                "FROM DISK, and every sealed object compared against the "
                "digest taken at the moment its gate passed -- with EVERY ONE "
                "of the %d sealed rows corrupted in turn on a read-back copy "
                "and shown to be detected first.  A staged payload that does "
                "not parse fails HERE rather than raising out of the writer.  "
                "THE PERIMETER IS CLOSED IN BOTH ARTIFACTS: the transcript is "
                "compared IN FULL, %d of %d lines by digest, and the two "
                "DECLARED-UNSEALED keys are CHAINED here against the live seal "
                "object.  The staged bytes are moved into place by os.replace "
                "ONLY after this gate passes, and a run that does not reach it "
                "leaves no staged file behind"
                % (len(SEAL.rows), text_lines, SEAL.text_lines),
                parsed_ok and probe_caught and not disk_broken and head_ok
                and text_ok and chained_ok and late_ok and sweep_complete,
                "staged payload parses %s, corrupted probes detected %d of %d, "
                "sealed objects broken on disk %s, transcript head matches %s, "
                "transcript matches in full %s (%d of %d lines), "
                "declared-unsealed keys chained %s, every declared-later gate "
                "actually evaluated %s, sweep complete and on target %s"
                % (parsed_ok, probes_caught, len(SEAL.rows),
                   disk_broken or "none", head_ok, text_ok, text_lines,
                   SEAL.text_lines, chained_ok, late_ok, sweep_complete))
        os.replace(tmp_j, OUT_JSON)
        os.replace(tmp_t, OUT_TXT)
        promoted = True
    finally:
        if not promoted:
            for p in (tmp_j, tmp_t):
                if os.path.exists(p):
                    os.unlink(p)
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
        full_run(break_anchor="A-P20REC", paper_text=None, do_paper=False)
    except GateFail as e:
        died = str(e).split(" ::")[0]
    except Exception as e:                             # pragma: no cover
        died = "UNEXPECTED:%s" % e
    QUIET = False
    after = (os.path.exists(OUT_JSON) and os.stat(OUT_JSON).st_mtime,
             os.path.exists(OUT_TXT) and os.stat(OUT_TXT).st_mtime)
    wrote = before != after
    print("[SELFTEST] corrupted anchor A-P20REC -> died at %s" % died)
    print("[SELFTEST] G-SELFTEST-WRITES-NOTHING: artifacts untouched: %s"
          % (not wrote))
    return (died == "G-PROVENANCE") and not wrote


class _Sink:
    def write(self, *_a):
        return 0

    def flush(self):
        return None


def run_mutant(name, paper_text):
    """run the pipeline with the named mutant active, IN PROCESS.  The census
    is cached, so a falsifier costs a gate layer rather than a rebuilt
    ensemble.  THE EVIDENCE STRING THE GATE ACTUALLY RAISED IS RETURNED with
    the gate name, and the execution counter is incremented HERE: the sweep
    gate binds both, so a fabricated sweep cannot pass."""
    global MUT, QUIET, LINES
    MUTANT_RUNS[0] += 1
    MUT, QUIET = name, True
    keep, keep_out = LINES, sys.stdout
    sys.stdout = _Sink()
    LINES = []
    killed_at = None
    evidence = ""
    try:
        LD, SEAL, R, verdict, _c = full_run(paper_text=paper_text)
        cli_gates(LD)
        finish(LD, SEAL, R, verdict, write=False)
    except GateFail as e:
        evidence = str(e)
        killed_at = evidence.split(" ::")[0]
    except Exception as e:                             # pragma: no cover
        killed_at = "UNEXPECTED:%s" % type(e).__name__
        evidence = "%s :: %s" % (killed_at, e)
    MUT, QUIET, LINES = None, False, keep
    sys.stdout = keep_out
    return killed_at, evidence


FLAGS = ("--no-write", "--numbers", "--selftest", "--mutant",
         "--break-anchor", "--verify-paper", "--list-gates", "--list-mutants")


def parse_args(argv):
    """#82: argv parsed against a WHITELIST.  Unknown flags, unknown flag
    arguments and missing flag arguments all exit 2; no abbreviation is
    accepted, no flag is a no-op, and modes do not compose."""
    out = {"mode": "deliver", "mutant": None, "anchor": None, "paper": None}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a not in FLAGS:
            raise CliError("unknown argument %r" % a)
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
    bad = []
    malformed = (["--nope"], ["--mutant"], ["--mutant", "NOPE"],
                 ["--break-anchor"], ["--break-anchor", "NOPE"], ["x"],
                 ["--numbers", "--zzz"],
                 ["--verify-paper", "--mutant", sorted(MUTANT_NAMES)[0]],
                 ["--numbers", "--no-write"], ["--selftest", "--list-gates"])
    codes = []
    for argv in malformed:
        # THE EXIT CODE IS MEASURED, not asserted (K3 MINOR-6): `main` maps a
        # CliError to 2 and returns before touching the census, so the gate can
        # observe the code it claims for free.
        codes.append(main(list(argv)))
        try:
            parse_args(argv)
            bad.append(argv)
        except CliError:
            pass
    if any(c != 2 for c in codes):
        bad.append(["EXIT-CODE-NOT-2"])
    ok_shapes = 0
    for argv in ([], ["--no-write"], ["--numbers"], ["--selftest"],
                 ["--mutant", sorted(MUTANT_NAMES)[0]],
                 ["--break-anchor", SOURCE_IDS[0]], ["--verify-paper"],
                 ["--list-gates"], ["--list-mutants"]):
        parse_args(argv)
        ok_shapes += 1
    permissive = parse_args_permissive(["--nope"])["mode"] == "nope"
    return bad, ok_shapes, permissive, len(malformed), codes


def selftest_shape():
    """the writer is called from exactly one place, and the self-test path
    cannot reach it -- checked by parsing this file."""
    tree = ast.parse(read_text(SELF))
    inside_finish = 0
    for fn in tree.body:
        if isinstance(fn, ast.FunctionDef) and fn.name == "finish":
            inside_finish = sum(1 for n in ast.walk(fn)
                                if isinstance(n, ast.Call)
                                and isinstance(n.func, ast.Name)
                                and n.func.id == "open"
                                and len(n.args) > 1)
    return inside_finish == 2


def cli_gates(LD):
    bad, ok_shapes, permissive, nmal, codes = cli_selftest()
    bad = pick("MUT-CLI-PERMISSIVE", bad, [["--nope"]])
    LD.gate("G-CLI-WHITELIST",
            "the #82 CLI contract, exercised in this run: %d malformed "
            "argument vectors are all rejected AND THE EXIT CODE IS OBSERVED "
            "RATHER THAN ASSERTED -- `main` is called on every one of them and "
            "every call returns %d -- the last three of them SECOND-MODE "
            "vectors; %d legal shapes parse, and the registered PERMISSIVE "
            "shape, present in this file only as this gate's own falsifier, "
            "accepts an unknown flag"
            % (nmal, 2, ok_shapes),
            not bad and permissive,
            "malformed vectors accepted %s, observed exit codes %s, legal "
            "shapes %d, permissive shape accepts unknown flags %s"
            % (bad or "none", sorted(set(codes)), ok_shapes, permissive))
    st_ok = pick("MUT-SELFTEST-WRITES", selftest_shape(), False)
    LD.gate("G-SELFTEST-WRITES-NOTHING",
            "the --selftest path corrupts an anchor in memory, dies at "
            "G-PROVENANCE and reaches no writer: the writer is called from "
            "exactly one place in this file and the self-test path does not "
            "reach it -- and the predicate is the AST probe's own value",
            st_ok,
            "the writer-shape probe reports the self-test path clean: %s"
            % st_ok)


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
        got, ev = run_mutant(name, paper_text)
        print("[MUTANT] %s -> declared gate %s -> died at %s"
              % (name, gate, got))
        print("[MUTANT] evidence: %s" % ev)
        return 1 if got == gate else 0
    try:
        LD, SEAL, R, verdict, _c = full_run(
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
        for name, gate, _why, _mv, _to in MUTANTS:
            got, ev = run_mutant(name, paper_text)
            kills.append({"mutant": name, "declared_gate": gate,
                          "died_at": got, "on_target": got == gate,
                          "evidence": ev})
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
        finish(LD, SEAL, R, verdict, write=(opt["mode"] == "deliver"),
               swept=True)
        return 0
    except GateFail as e:
        sys.stderr.write("GATE FAILED: %s\n" % e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
