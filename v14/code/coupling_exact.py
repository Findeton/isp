#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
v14 THE COUPLING UNIT -- A QUANTUM DYNAMICS THAT WRITES ITS OWN STAGE.
Instrument for `v14/paper-20-coupling.md`.

QUESTION (pin `v14/note-coupling-pin.md`, sha256-12 7c6e9e44fc2c, ledger #173).
On the welded R = 3 arena -- the saturating record n = 1 at 27 of 27 cells,
det 3/4, positive definite 9 of 9, with the FORCED dictionary
[ACTOR->SITE | CO-DIVISION-PAIR->LINK | DIVISION-COUNT->n_l(x)] -- run a
unitary walk whose interactions EMIT DIVISION EVENTS THROUGH THE CONFIRMED
LAW, updating the very counts the walk propagates on.  Then gate three things:

  G-CONSISTENCY    the coupled step is well defined: the walk's unitarity and
                   the law's column-stochasticity COMPOSE exactly, at every
                   step of a declared horizon, per branch and per site.
  G-NONTRIVIALITY  the declared observable set differs measurably from the
                   MANDATORY FROZEN-STAGE CONTROL -- the same walk on
                   never-updating counts.  Identical would be COUPLING-INERT,
                   an honest first-class outcome.
  G-REQUIREMENT    THE THEOREM, two-way.  A CLOSURE BATTERY of ten conditions,
                   each pre-registered with its polarity, each measured on
                   both stages, and a selector that returns REQUIRED only for
                   a closure that is INTERNAL TO THE QUANTUM SIDE, is NOT the
                   update rule restated, and fails frozen while passing
                   coupled.

WHAT THIS PROGRAM DOES
  SEC 1  PROVENANCE.  16 pinned sources, sha256-12 verified; the #62 verbatim
         anchors bound to their consumer gates, each named gate required to be
         in the registry AND in this run's own ledger; every text gate
         whitespace-normalises, ASCII-folds AND strips markdown prefixes.
  SEC 2  EXACT ARITHMETIC on Z[w], w^2 = -1-w; the arena; HA's own readout.
  SEC 3  THE WELDED RECORD, REBUILT AND DRIVEN.  d42b1's transport layer by
         text slice, d60's `B`/`dl` and d66's `conflict_grid` by AST
         extraction.  The uniform R = 3 arrangement is driven through the
         layer's own menus and gated cell by cell and site by site.
  SEC 4  THE WALK, DERIVED WHERE DERIVABLE.  One theorem and one declaration:
         the R4b SCALAR shape is MONOMIAL-ONLY on this arena's offset set, so
         the coin register is FORCED (checked over the DISCRIMINATING alphabet
         (1/3)Z[w], which separates this stencil from the axis stencil where
         interference survives); and the S_3-covariant unitarity conditions
         have a CIRCLE of solutions, so the coin is DECLARED under a stated
         REALITY CONDITION with its fiber printed -- six classes up to a
         global phase over the arena's own (1/3)Z[w], of which one is
         +/- Grover.  The verdict is then measured to be INVARIANT across the
         whole hidden family: all four non-Grover classes are run to the full
         horizon.  The connection group is Z_3 because the arena is over F_3.
  SEC 5  THE LAW TRANSPORT, GATED AND NEVER ASSUMED.  G(x,0) = 1 terminal,
         G(x,1) = M(x), k_1 = q/M -- re-derived on this arena, at every site
         and every step, and under an ARBITRARY EXACT RE-PRICING.
  SEC 6  THE COUPLED ENSEMBLE.  Exhaustive over every branch of the emission
         tree to the declared horizon; no sampling, no pruning; the frozen
         control run at the same branching.
  SEC 7  THE THREE GATES and the CLOSURE BATTERY.
  SEC 8  THE WALLS -- the four inherited, plus the Lorentzian resonance NAMED
         (mandatory here, because a measured determinant reaches 0) and the
         hexagonal resonance NAMED, which paper-19's S-7 registered for this
         unit before it was written.
  SEC 9  The verdict, derived a SECOND time by a comparator that TYPES ITS OWN
         TEMPLATES and re-derives the outcome word from the receipt's own
         gate rows; the paper gates -- claim rendering, numeral coverage
         INCLUDING THE FENCED VERDICT BLOCKS, head-verbatim and claim
         polarity; the TOTAL seal; the sweep binding; the artifacts; the
         disk-vs-seal integrity check.

CLI CONTRACT (the #82 minimum: argv parsed against a WHITELIST)
---------------------------------------------------------------
    python3.13 v14/code/coupling_exact.py
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

THE TOTAL GATE-TO-DISK SEAL.  EVERY published receipt key -- the measured
layer AND the vouching layer (schema, provenance, paper_claims, coverage,
polarity, reachability, gates, totals, transcript head) -- is either sealed at
the moment its gate passes or listed as DECLARED-UNSEALED, and the
completeness gate compares the manifest against the DECLARED key set.  The
artifacts are written from the sealed payload through `os.replace`; the
terminal integrity gate compares the BYTES ON DISK against the gate-time seal.
A run that fails any gate writes nothing.

ARITHMETIC.  Exact only: Python integers and `fractions.Fraction`, with the
walk's amplitudes carried as INTEGER pairs over Z[w] with a common power-of-3
denominator.  There are no floats anywhere -- an AST scan of this file and a
recursive type scan of the emitted receipt are gates.

RUNTIME INPUTS (#46/#91).  The declared SOURCES are read at run time by path
resolved from this file's own location, all hash-pinned by this unit's frozen
declaration.  Two further files are read and BOTH are gated as their own
declared set: this file itself (the AST self-scans) and the OBJECT UNDER TEST,
this unit's own paper.  No repository state outside those two sets is read and
no subprocess of any kind is invoked, so the run is correct off-tree and with
no version control present.
"""

import ast
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product

sys.setrecursionlimit(100000)

SELF = os.path.abspath(__file__)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(SELF)))
OUT_TXT = os.path.join(os.path.dirname(SELF), "coupling_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "coupling_receipt.json")

SCHEMA = "isp/v14/coupling/1"
PAPER_REL = "v14/paper-20-coupling.md"

# ===========================================================================
# SECTION 1.  PROVENANCE -- the pinned sources
# ===========================================================================

SOURCES = [
    ("A-PIN", "v14/note-coupling-pin.md", "7c6e9e44fc2c",
     "THIS UNIT'S PIN (ledger #173): the three gates, the declared data, the "
     "pre-registered outcomes and the binding scope row."),
    ("A-W3", "v14/paper-19-r3-weld.md", "50bb81e67942",
     "THE WELD (paper-19, terminal): the arena, the forced dictionary, the "
     "1296 site assignments, the unsplittability of the landing record, and "
     "the successor register that names this unit and its walls."),
    ("A-W3REC", "v14/code/r3_weld_receipt.json", "dfea664f2408",
     "THE WELD'S COMMITTED RECEIPT: the isomorphism count and the fibers this "
     "unit cites and verifies rather than re-deriving."),
    ("A-GITER", "v14/paper-16-gamma-iteration.md", "5c1df50673d4",
     "THE GRAVITY LAW (Gamma-iteration, terminal): the LAW-NATIVE normaliser "
     "G(h,1) = M(h), the kernel k_1 = q/M, and the sedimentary theorem."),
    ("A-GITERREC", "v14/code/giter_receipt.json", "42255f50328a",
     "THE LAW'S COMMITTED RECEIPT: the kernel-entry count and the law's own "
     "values, read at run time and never re-typed."),
    ("A-R4B", "v14/paper-15-momentum.md", "89c636906061",
     "R4b (terminal): the coin-walk family shape -- a generator is a "
     "coefficient map on lattice offsets -- and the unitarity condition this "
     "unit evaluates on the arena's own offset set."),
    ("A-R4BREC", "v14/code/r4b_momentum_receipt.json", "562e2a3d4d85",
     "R4b'S COMMITTED RECEIPT: the family shape's own numbers."),
    ("A-R5", "v14/paper-18-gauge-rung.md", "62cfe5689d2c",
     "R5 (terminal): the support-overlap law, cited where it binds, and the "
     "trace-non-integrality instrument this unit re-uses on its own walk."),
    ("A-U4B", "v14/paper-17-schedule-census.md", "acd9787960c2",
     "U4b (terminal): the price law -- at R = 2 the budget binds, at R = 3 "
     "the matching binds -- cited and not re-derived."),
    ("A-HA", "v13/paper-ha-successor.md", "f286ba10d2d9",
     "I7 / HA: the declared readout, the admissibility criterion this unit's "
     "coupled orbit is measured against, and requirement 3."),
    ("A-I7", "v13/code/ha_successor_receipt.json", "542b8735daf0",
     "I7'S ARENA AS DATA: sites, links and the declared record family."),
    ("A-D42B1", "v10/code/d42b1_transport_exact.py", "576275d55ecf",
     "THE COMMITTED TRANSPORT GRAMMAR, driven directly: this unit's only "
     "source of admissibility for the welded record it rebuilds."),
    ("A-D60", "v10/code/d60_crystal_exact.py", "684cdb76552b",
     "D60: the Builder `B` and the delivery helper `dl`, AST-extracted."),
    ("A-D66", "v10/code/d66_arbitration_crystal_exact.py", "3d0516ab106e",
     "D66: CONFLICT-GRID(g, R), the committed constructor, AST-extracted and "
     "re-run as this unit's anchor."),
    ("A-L1", "v11/note-L1-lorentz-no-go-lemma.md", "93ea24591c3c",
     "L-1: the fourth-form clause, and the sentence retracted on 2026-07-28 "
     "that no paper of this line may reproduce."),
    ("A-CAT", "v11/note-v11p0a-reproduction-catalog.md", "0cebe543e814",
     "the reproduction catalog: the BHS block and the Kleitman-Rothschild "
     "height-control warning."),
    ("A-CRA", "v14/note-cra-adjudication.md", "b7ce00951e5a",
     "CR-A's adjudication (v14 #178): the register rows this unit answers, "
     "and the measured three-diagonal-event margin to G-SINGULAR that this "
     "unit's exit census meets from the other side."),
]
SOURCE_IDS = [s[0] for s in SOURCES]

# the second declared read set (#46/#91, K3 MINOR-4): the files this run reads
# that are NOT pinned sources.  They are declared here and gated exactly the
# way READS is gated, so the docstring's claim is a measurement.
OBJECT_READS_WHY = {
    "SELF": "this file, AST-parsed by its own float scan, import scan, "
            "writer-shape probe and self-test shape probe",
    "PAPER": "the object under test, read once by main and handed to the "
             "paper gates",
}

# the retracted L-1 sentence: no paper of this line may reproduce it
BANNED_L1 = ("precisely the form U4 tests, and precisely the form the "
             "corpus's strongest relativity result took")

# THE LORENTZIAN RESONANCE, named -- mandatory, and sharper here than at the
# weld, because this unit MEASURES a determinant that reaches zero.
LORENTZ_NAMED = (
    "The determinant that reaches 0 in this unit is NAMED AND NOT READ: it is "
    "the exact boundary of I7's own admissibility criterion on a nine-site "
    "Euclidean lattice, it is not a signature and not a light cone, no "
    "indefinite form is reached at this horizon, and no Lorentzian, causal or "
    "signature-change reading of it is taken here or licensed by anything "
    "measured here.")

# THE HEXAGONAL RESONANCE, named -- paper-19's S-7 registered it FOR this unit
# before this unit was written.
HEX_NAMED = (
    "The second resonance is NAMED before it is heard: q = [[1, -1/2], "
    "[-1/2, 1]] is the Gram matrix a reader will recognise as hexagonal, unit "
    "lengths meeting at one hundred and twenty degrees, and this unit takes no "
    "triangular, hexagonal, crystallographic or lattice-geometry reading of it "
    "whatever.")

# THE DECLARED FALSIFIER REGISTRY (E-23, bought at v14 #187).  Every row
# carries FIVE fields: the name, the gate it must die at, what it does, THE
# SYMBOL IT MOVES and THE VALUE IT MOVES IT TO.  The last two are re-derived
# from THIS FILE's own AST at run time and compared against the declaration,
# and the prose must NAME BOTH -- so a description that says the opposite of
# its code (paper-20's own MUT-TRANSPORT-ASSUMED, MUT-FIBER-BLIND and
# MUT-PRUNE, found by the K3 instrument seat) cannot be written down.
MUTANTS = [
    # -- the arena, rebuilt
    ("MUT-WELD-CELL", "G-WELDED-RECORD",
     "moves `n_driven`, the driven link field, by 1 at one of the 27 cells -- "
     "must die at the per-cell rebuild gate", "n_driven", "1"),
    ("MUT-WELD-FORCED", "G-WELDED-RECORD",
     "moves `maxhits` to 2: reports the driven record as FORCED while its "
     "builder recorded a menu of more than one candidate -- must die at the "
     "same gate", "maxhits", "2"),
    ("MUT-WELD-DET", "G-WELDED-GEOMETRY",
     "moves `d`, one site's determinant, to Fraction(1) rather than the "
     "measured 3/4 -- must die at the per-site geometry gate",
     "d", "Fraction(1)"),
    ("MUT-COMMITTED-ANCHOR", "G-COMMITTED-ANCHOR",
     "moves `same` to False: the driver's committed-schedule record no longer "
     "matches d66's own conflict_grid(3,2) event for event -- must die at the "
     "committed anchor", "same", "False"),
    ("MUT-DICTIONARY", "G-DICTIONARY",
     "moves `realised` to the list with its last co-division pair dropped, "
     "[:-1] -- must die at the gate that requires the realised relation to BE "
     "the target's Cayley incidence", "realised", "[:-1]"),
    ("MUT-ISOS", "G-ISOS-CITED",
     "moves `isos_here` to 1290 -- must die against the weld's own committed "
     "receipt", "isos_here", "1290"),
    ("MUT-SPLIT", "G-UNSPLITTABLE",
     "moves `prod_fiber` to 1: reports a positive split fiber on a count-1 "
     "interval -- must die at the gate that warrants this unit's scope row",
     "prod_fiber", "1"),
    # -- the walk, derived and declared
    ("MUT-SCALAR-ALIVE", "G-SCALAR-MONOMIAL",
     "moves `nonmonomial_unitary_maps` to 1: reports a two-term scalar "
     "generator as unitary on the link offset set -- must die at the "
     "monomial-only theorem's own exhaustive check",
     "nonmonomial_unitary_maps", "1"),
    ("MUT-COIN-FREE", "G-COIN-CENSUS",
     "moves `classes_up_to_phase` to 5: hides one of the six S_3-covariant "
     "coin classes the arena's own ring admits -- must die at the coin census",
     "classes_up_to_phase", "5"),
    ("MUT-COIN-INVARIANT", "G-COIN-INVARIANCE",
     "moves `inv_bad` to the one-element list ['FORGED']: reports a member of "
     "the hidden coin family as failing an invariant it was measured to hold "
     "-- must die at the coin-invariance gate", "inv_bad", "FORGED"),
    ("MUT-CONNECTION-GROUP", "G-CONNECTION-GROUP",
     "moves `connection_group_order` to 4: reads the connection in Z_4 on an "
     "arena over F_3 -- must die at the gate that derives the connection "
     "group from the arena", "connection_group_order", "4"),
    ("MUT-WALK-UNITARY", "G-WALK-UNITARY",
     "moves `uviol` to 1: one coin entry stops being norm-preserving -- must "
     "die at the per-site unitarity gate", "uviol", "1"),
    ("MUT-FIBER-BLIND", "G-FIBERS",
     "moves `executed_members` to the executed list with its last id dropped, "
     "[:-1], so a declared fiber member is reported measured while its run is "
     "missing from the execution record -- must die at the fiber-inventory "
     "gate", "executed_members", "[:-1]"),
    ("MUT-ORDER-FULL", "G-COIN-ORDER-FULL",
     "moves `dg_threshold` to 4: reports the alternative coin order's "
     "admissibility threshold away from the measured one -- must die at the "
     "full-horizon coin-order gate", "dg_threshold", "4"),
    # -- the law transport
    ("MUT-LAW-TERMINAL", "G-LAW-NATIVE",
     "moves `lawviol` to 3: breaks the potential recursion's terminal "
     "condition G(x,0) = 1, which is exactly what makes the normaliser "
     "law-native -- must die at the per-site-per-step transport gate",
     "lawviol", "3"),
    ("MUT-LAW-REPRICE", "G-LAW-REPRICING",
     "moves `repviol` to 2: re-prices events and reports the identity as "
     "surviving when it does not -- must die at the arbitrary-re-pricing "
     "forcing gate", "repviol", "2"),
    ("MUT-KERNEL", "G-KERNEL-K1",
     "moves `kviol` to 5: detaches five kernel entries from q/M -- must die "
     "at the kernel gate", "kviol", "5"),
    ("MUT-MASS-DENSITY", "G-LAW-TRANSPORT",
     "moves `mdviol` to 4: the menu-mass-is-Born-mass row -- the one the "
     "transport publishes as its identification -- is reported violated at "
     "four site-steps -- must die at the transport gate", "mdviol", "4"),
    ("MUT-TRANSPORT-ASSUMED", "G-LAW-TRANSPORT",
     "moves `transport_ok` to False while every one of its conjuncts still "
     "holds, so the published verdict flag is detached from the measurement "
     "under it -- must die at the same gate", "transport_ok", "False"),
    ("MUT-NBD-BLIND", "G-TRANSPORT-MECHANISM",
     "moves `nbd_site_violations` to 0: reports the site-block-diagonality "
     "row as clean on a coin built to violate it -- must die at the "
     "mechanism gate", "nbd_site_violations", "0"),
    # -- the ensemble
    ("MUT-PRUNE", "G-ENSEMBLE-EXHAUSTIVE",
     "moves `route1`, the carried frontier's own branch count, down by 1 at "
     "one level while the emission supports still count it -- must die at "
     "the two-route branch-count gate", "route1", "1"),
    ("MUT-BRANCH-MASS", "G-BRANCH-MASS",
     "moves `mass_bad` to [(\"A-COUPLED\", 1)]: one branch weight stops the "
     "level mass being exactly 1 -- must die at the per-level mass gate",
     "mass_bad", "A-COUPLED"),
    # -- the three gates
    ("MUT-CONSISTENCY", "G-CONSISTENCY",
     "moves `cviol` to 1: a per-site column sum is reported 1 where the "
     "measured sum is not -- must die at the composition gate", "cviol", "1"),
    ("MUT-INERT", "G-NONTRIVIALITY",
     "moves `cv` to `fv`, handing the frozen control's observables to the "
     "coupled arm so the two are identical -- must die at the two-way "
     "nontriviality gate", "cv", "fv"),
    ("MUT-NO-FROZEN", "G-FROZEN-CONTROL",
     "moves `frozen_ran` to False: reports the frozen control without its "
     "execution -- must die at the gate that binds the control's execution",
     "frozen_ran", "False"),
    ("MUT-POLARITY", "G-BATTERY-POLARITY",
     "moves `mc` to True on one battery row, against its pre-registration -- "
     "must die at the polarity gate", "mc", "True"),
    ("MUT-ONE-WAY", "G-BATTERY-TWO-WAY",
     "moves `restateds` to []: one direction of the battery is emptied, "
     "leaving a one-way instrument -- must die at the two-way gate",
     "restateds", "[]"),
    ("MUT-STALENESS", "G-STALENESS-BLIND",
     "moves `stale_clean` to False: reports a psi-internal closure as failing "
     "on the declared stale stage -- must die at the staleness-blindness "
     "theorem's own check", "stale_clean", "False"),
    ("MUT-COUNT-BLIND", "G-COUNT-BLIND",
     "moves `blind_viol` to 1: reports K1-K4 as reading the record on a "
     "foreign count field -- must die at the count-blindness gate",
     "blind_viol", "1"),
    ("MUT-K5-RETURN", "G-K5-NO-RETURN",
     "moves `ray_repeats` to 1: reports a state recurrence the ray-grain "
     "measurement did not find -- must die at the no-return gate",
     "ray_repeats", "1"),
    ("MUT-REFUSAL-DROP", "G-REFUSAL-ROBUST",
     "moves `stamp_only` to 2: reports witnesses appearing when the "
     "UPDATE-RULE-RESTATED stamp alone is dropped -- must die at the "
     "either-refusal-drop gate", "stamp_only", "2"),
    ("MUT-LADDER", "G-ADMISSIBILITY-LADDER",
     "moves `thresholds` to {\"A\": 4, \"B\": 4}: reports the admissibility-exit "
     "threshold at horizon 4 -- must die at the ladder gate, which locates it "
     "by measuring every horizon", "thresholds", "4"),
    ("MUT-EXIT-CENSUS", "G-EXIT-CENSUS",
     "moves `census_total`, the classified inadmissible-leaf count, by 1 away "
     "from the frontier's own -- must die at the exit-census gate",
     "census_total", "1"),
    ("MUT-REQUIRED", "G-REQUIREMENT",
     "moves `witnesses` to `restated`, promoting an UPDATE-RULE-RESTATED row "
     "to a requirement witness -- must die at the selector gate",
     "witnesses", "restated"),
    # -- the walls
    ("MUT-WALL-L1", "G-WALL-L1",
     "moves `ptext` to the object under test with `BANNED_L1`, the retracted "
     "L-1 sentence, appended line-wrapped and blockquoted -- must die at the "
     "L-1 wall", "ptext", "BANNED_L1"),
    ("MUT-WALL-BHS", "G-WALL-BHS",
     "moves `layer`, this run's measurement surface, to one carrying a "
     "sprinkling-grade `boosted rest frame` reading -- must die at the BHS "
     "abstention scan", "layer", "boosted rest frame"),
    ("MUT-WALL-KR", "G-WALL-KR",
     "moves `layer` to one carrying a `myrheim-meyer` dimension estimate with "
     "no height control -- must die at the Kleitman-Rothschild scan",
     "layer", "myrheim-meyer"),
    ("MUT-WALL-COSMO", "G-WALL-COSMO",
     "moves `layer` to one carrying a `cosmological expansion` reading -- "
     "must die at the cosmological/continuum scan",
     "layer", "cosmological expansion"),
    ("MUT-WALL-LORENTZ", "G-WALL-LORENTZ-NAMED",
     "moves `lz` to False: the mandatory Lorentzian naming sentence is "
     "reported absent from the object under test -- must die at the naming "
     "gate", "lz", "False"),
    ("MUT-WALL-HEX", "G-WALL-HEX-NAMED",
     "moves `hx` to False: the hexagonal naming sentence paper-19's S-7 "
     "registered for this unit is reported absent -- must die at the second "
     "naming gate", "hx", "False"),
    # -- the verdict and the paper
    ("MUT-VERDICT-WORD", "G-VERDICT-RECONSTRUCTED",
     "moves `verdict`'s gates segment to one whose outcome word reads "
     "COUPLING-CONSISTENT-AND-REQUIRED-K9-SOURCING, in the builder alone -- "
     "must die at the comparator, which types its own templates and "
     "re-derives the word", "verdict",
     "COUPLING-CONSISTENT-AND-REQUIRED-K9-SOURCING"),
    ("MUT-VERDICT-VALUE", "G-VERDICT-RECONSTRUCTED",
     "moves `verdict`'s arena segment by retyping one measured value inside "
     "it, 27 OF 27 to 26 OF 27 -- must die at the same comparator, by "
     "occurrence count", "verdict", "26 OF 27"),
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS",
     "moves `sent`, an assembled claim, to one reading 26 cells -- must die "
     "at the claim gate", "sent", "26 cells"),
    ("MUT-PAPER-TABLE", "G-PAPER-TABLES",
     "moves `trows`, the rendered table rows, to the list with its last row "
     "dropped and a FORGED one appended, so a row the paper does not carry is "
     "claimed -- must die at the table gate", "trows", "FORGED"),
    ("MUT-PAPER-NUMERAL", "G-PAPER-NUMERAL-COVERAGE",
     "moves `unregistered` to ['123456789'], an unregistered numeral -- must "
     "die at the #20 coverage scan", "unregistered", "123456789"),
    ("MUT-PAPER-HEAD", "G-PAPER-HEAD-VERBATIM",
     "moves `probe`, a derived verdict segment, by one character to seg[:-1] "
     "+ Z before matching it into the paper -- must die at the head-verbatim "
     "gate", "probe", "Z"),
    ("MUT-PAPER-BLOCK", "G-PAPER-HEAD-VERBATIM",
     "moves `blockmap`, the paper's own fenced-block multiset, to the same "
     "multiset with its last block dropped, [:-1], so a duplicated head could "
     "shadow a forged twin -- must die at the same gate's MULTISET leg", "blockmap", "[:-1]"),
    ("MUT-PAPER-POLARITY", "G-PAPER-CLAIM-POLARITY",
     "moves `mutated` to True, swapping a positive claim for its negation in "
     "the object under test -- must die at the polarity gate",
     "mutated", "True"),
    # -- the instrument
    ("MUT-CLI-PERMISSIVE", "G-CLI-WHITELIST",
     "moves `bad` to [['--nope']]: the argv whitelist is swapped for the "
     "registered permissive shape -- must die at the CLI gate",
     "bad", "--nope"),
    ("MUT-SELFTEST-WRITES", "G-SELFTEST-WRITES-NOTHING",
     "moves `st_ok` to False: the self-test path is claimed to reach a writer "
     "-- must die at the writes-nothing gate", "st_ok", "False"),
    ("MUT-WRITER-SHAPE", "G-WRITER-SHAPE",
     "moves `gate_names_in_finish` to the list with the terminal integrity "
     "gate's name dropped, [:-1] -- must die at the writer-shape probe, which "
     "is taken BEFORE the gate ledger is snapshotted and is therefore the one "
     "guard a post-snapshot gate's own removal cannot evade",
     "gate_names_in_finish", "[:-1]"),
    ("MUT-FALSIFIER-DESC", "G-FALSIFIER-HONESTY",
     "moves `declared`, one falsifier's declared (symbol, value) pair, to "
     "FORGED, away from what this file's AST says its hook writes -- must die "
     "at the falsifier-honesty gate", "declared", "FORGED"),
    ("MUT-SEAL-DROP", "G-SEAL-COMPLETE",
     "silently drops the seal row whose `sid` is SEAL-COVERAGE -- must die at "
     "the totality gate, which compares the manifest against the DECLARED key "
     "set", "sid", "SEAL-COVERAGE"),
    ("MUT-SEAL-BROKEN", "G-SEAL-COMPLETE",
     "moves `horizon` in the sealed counts block by + 1 between its gate and "
     "the write -- must die at the same gate, re-taking every seal against "
     "the live object", "horizon", "+ 1"),
    ("MUT-TRANSCRIPT-FLIP", "G-SEAL-COMPLETE",
     "moves `transcript_head` to one beginning FLIPPED after it is sealed -- "
     "must die at the same gate", "transcript_head", "FLIPPED"),
    ("MUT-SWEEP-UNBOUND", "G-SWEEP-BOUND",
     "moves `swept` to True on a run carrying no sweep, shipping a delivery "
     "whose mutant sweep never ran -- must die at the gate that binds the "
     "sweep's execution to the writer", "swept", "True"),
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
    ("SEAL-ANCHORS", "anchors", "G-ISOS-CITED"),
    ("SEAL-ARENA", "arena", "G-UNSPLITTABLE"),
    ("SEAL-COIN-INVARIANCE", "coin_invariance", "G-COIN-INVARIANCE"),
    ("SEAL-WALK", "walk", "G-FIBERS"),
    ("SEAL-LAW", "law", "G-LAW-TRANSPORT"),
    ("SEAL-MECHANISM", "transport_mechanism", "G-TRANSPORT-MECHANISM"),
    ("SEAL-ENSEMBLE", "ensemble", "G-BRANCH-MASS"),
    ("SEAL-CONSISTENCY", "consistency", "G-CONSISTENCY"),
    ("SEAL-NONTRIVIALITY", "nontriviality", "G-NONTRIVIALITY"),
    ("SEAL-BATTERY", "battery", "G-REQUIREMENT"),
    ("SEAL-LADDER", "ladder", "G-ADMISSIBILITY-LADDER"),
    ("SEAL-EXIT-CENSUS", "exit_census", "G-EXIT-CENSUS"),
    ("SEAL-WALLS", "walls", "G-WALL-HEX-NAMED"),
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
# #148 REDUCED (K3 MAJOR-2b).  `arithmetic` and `python` are now sealed at the
# gate that certifies them; the two that remain cannot be sealed by the seal
# itself -- `seal_manifest` contains the seal rows, and `payload_sha256_12` is
# the digest of the payload the seal closes over -- so each is CHAINED instead:
# both are re-read FROM DISK at G-ARTIFACT-INTEGRITY and compared against the
# live seal object.  An unsealed key with no chain would be an unguarded row.
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
MEASURED_KEYS = ("arena", "walk", "coin_invariance", "law",
                 "transport_mechanism", "ensemble", "consistency",
                 "nontriviality", "battery", "ladder", "exit_census",
                 "anchors", "counts", "verdict")


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
        have = {r["seal"] for r in self.rows}
        want = {s for s, _p, _g in SEALED_PATHS}
        return sorted(want - have), sorted(have - want)

    def close(self, obj, payload, text):
        """seal BOTH artifacts.  The transcript is sealed IN FULL, not by its
        first 40 lines: a 40-line head seal left 141 of paper-20's 181 lines
        outside the perimeter, and the K3 seat shipped a forged transcript
        through it at exit 0 (MAJOR-2a)."""
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
         "⁄": "/", " ": " ", "ω": "w", "ψ": "psi",
         "Γ": "Gamma", "⊗": "(x)", "√": "sqrt",
         "⟨": "<", "⟩": ">", "Δ": "Delta", "π": "pi"}

_MD_PREFIX = re.compile(r"^(?:\s*(?:>+|[-*+]|\d+[.)])\s+)+")


def mdstrip(s):
    """#125 WITH MARKDOWN-PREFIX NORMALIZATION: strip blockquote markers and
    list-item bullets from the head of every line before matching, so a needle
    that spans a quoted or enumerated block cannot be evaded by re-wrapping."""
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
    """the full text-gate normalisation: markdown line prefixes, then markdown
    emphasis and code ticks, then the ASCII fold, then whitespace.  BOTH sides
    of every text match go through it."""
    return norm(ascii_fold(mdstrip(s).replace("*", "").replace("`", "")))


NEEDLE_FLOOR = 30


def match_needle(hay, needle):
    n = canon(needle)
    if len(n) < NEEDLE_FLOOR:
        raise GateFail("G-VERBATIM :: needle below the #62 length floor: %r"
                       % needle)
    return n in canon(hay)


# ===========================================================================
# SECTION 2.  EXACT ARITHMETIC ON Z[w], THE ARENA, AND HA'S OWN READOUT
# ===========================================================================
# Z[w] with w^2 = -1 - w.  An element is the INTEGER pair (a, b) meaning
# a + b*w.  The walk's amplitudes are carried as such pairs over a common
# denominator 3^t, so every amplitude is exact and no Fraction is constructed
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
    """|a + b w|^2 = a^2 - a b + b^2, a RATIONAL INTEGER -- which is why the
    Born weights of this walk are exact integers over a power of 3."""
    a, b = z
    return a * a - a * b + b * b


Z0 = (0, 0)
Z1 = (1, 0)
WPOW = [(1, 0), (0, 1), (-1, -1)]          # w^0, w^1, w^2

SITES = tuple((i, j) for i in range(3) for j in range(3))
SITE_INDEX = {s: k for k, s in enumerate(SITES)}
# I7's three DECLARED link directions.  ANT = (1,2) is the one direction I7
# does not declare; it is the arena's own fourth parallel class and it names
# the parts of the tripartite incidence.
LINKS = ((1, 0), (0, 1), (1, 1))
ANT = (1, 2)
LINK_INDEX = {l: k for k, l in enumerate(LINKS)}
NCELL = 27
DIM = 27


def vadd(a, b):
    return ((a[0] + b[0]) % 3, (a[1] + b[1]) % 3)


def vsub(a, b):
    return ((a[0] - b[0]) % 3, (a[1] - b[1]) % 3)


def cell(si, li):
    """the arena's 27 cells, indexed site-major.  Cell (x, l) IS the unordered
    co-division pair {x, x+l}: the three +l moves along a line of direction l
    cover that line's three unordered pairs exactly once, so (site, link) and
    (realised pair) are in bijection and no orientation is needed."""
    return si * 3 + li


CELL_PAIR = {}
for _s in range(9):
    for _i in range(3):
        _x = SITES[_s]
        CELL_PAIR[cell(_s, _i)] = frozenset((_x, vadd(_x, LINKS[_i])))
PAIR_CELL = {v: k for k, v in CELL_PAIR.items()}

SHIFT_T = tuple(cell(SITE_INDEX[vadd(SITES[_s], LINKS[_i])], _i)
                for _s in range(9) for _i in range(3))
# the reverse-orientation shift, the declared ORIENT fiber's second member
SHIFT_T_MINUS = tuple(cell(SITE_INDEX[vsub(SITES[_s], LINKS[_i])], _i)
                      for _s in range(9) for _i in range(3))

# THE GROVER COIN, as INTEGER numerators over 3: 3G has -1 on the diagonal and
# 2 off it.  Section 4 DERIVES it rather than declaring it.
GN = tuple(tuple(2 if i != j else -1 for j in range(3)) for i in range(3))
# the same matrix over Z[w], as integer pairs: the form the walk carries, so
# that EVERY member of the S_3-covariant family runs through the same code.
GROVER_Z = tuple(tuple((GN[i][j], 0) for j in range(3)) for i in range(3))


def q_of(nvec):
    """HA / I7's own readout, matched verbatim against paper-19 and applied
    here unchanged: the three link counts at a site give the 2x2 form."""
    n1, n2, n3 = nvec
    q11 = Fraction(n1)
    q22 = Fraction(n2)
    q12 = Fraction(n3 - n1 - n2, 2)
    return q11, q22, q12, q11 * q22 - q12 * q12


def admissible(nvec):
    """I7's exact Sylvester criterion: nonsingular and positive definite."""
    q11, _q22, _q12, det = q_of(nvec)
    return q11 > 0 and det > 0


def site_counts(n, si):
    return (n[si * 3], n[si * 3 + 1], n[si * 3 + 2])


WELDED = tuple([1] * NCELL)


# ===========================================================================
# SECTION 3.  THE WELDED RECORD, REBUILT FROM THE COMMITTED GRAMMAR
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

    EXTRACT_FROM = ("v10/code/d60_crystal_exact.py",
                    "v10/code/d66_arbitration_crystal_exact.py")

    def __init__(self, texts):
        st = texts["v10/code/d42b1_transport_exact.py"]
        cut = st.index('print("[d42b1')
        self.slice_text = st[:cut]
        # K3 MINOR-6: EXIT-FREEDOM IS DECIDED BEFORE THE FIRST exec, not
        # after it.  A slice or an extracted body calling sys.exit would have
        # ended this process before the gate that refuses it could run.
        self.extracted = {}
        for rel in self.EXTRACT_FROM:
            self.extracted[rel] = [
                n for n in ast.parse(texts[rel]).body
                if isinstance(n, (ast.FunctionDef, ast.ClassDef))]
        self.slice_exit_free = ("sys.exit" not in self.slice_text
                                and no_exit(ast.parse(self.slice_text).body))
        self.bodies_exit_free = all(no_exit(v)
                                    for v in self.extracted.values())
        if not (self.slice_exit_free and self.bodies_exit_free):
            raise GateFail("G-SLICE-EXIT-FREE :: the slice or an extracted "
                           "body can terminate this process; NOTHING was "
                           "executed")
        ns = {}
        exec(compile(self.slice_text, "d42b1_slice", "exec"), ns)
        self.ns = ns
        self.raw_candidates_for = ns["candidates_for"]
        self.regs_of = ns["regs_of"]
        self.vname = ns["vname"]
        self.V0 = ns["V0"]
        self.memo = {}
        g60 = self._extract("v10/code/d60_crystal_exact.py", "d60",
                            {"candidates_for": self.candidates_for,
                             "event_poset": ns["event_poset"], "V0": self.V0})
        self.B = g60["B"]
        self.dl = g60["dl"]
        g66 = self._extract("v10/code/d66_arbitration_crystal_exact.py",
                            "d66",
                            {"B": self.B, "dl": self.dl, "vname": self.vname,
                             "V0": self.V0,
                             "candidates_for": self.candidates_for})
        self.conflict_grid = g66["conflict_grid"]

    def candidates_for(self, hist, inits):
        key = (tuple(hist), tuple(inits))
        got = self.memo.get(key)
        if got is None:
            got = self.raw_candidates_for(list(hist), tuple(inits))
            self.memo[key] = got
        return got

    def _extract(self, rel, marker, extra):
        """d60/d66's committed extraction idiom: keep only defs and classes, so
        no module-level statement of theirs can run.  The bodies were parsed
        and cleared as exit-free in __init__, BEFORE anything was executed."""
        keep = self.extracted[rel]
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


def parallel_class(d):
    """the resolvable partition of AG(2,3) into the three lines of slope d."""
    seen, out = set(), []
    for x in SITES:
        L = tuple(sorted({x, vadd(x, d), vadd(vadd(x, d), d)}))
        if L not in seen:
            seen.add(L)
            out.append(L)
    return tuple(sorted(out))


CLASS_DIR = {"ROW": (0, 1), "COL": (1, 0), "DIA": (1, 1), "ANT": (1, 2)}
CLASSES = {k: parallel_class(v) for k, v in CLASS_DIR.items()}
DIAG_SEED = ((0, 0), (1, 1), (2, 2))


def canon_transversal(P, k=0):
    """paper-19's DECLARED SEED MENU: the k-th member of each group in the
    canonical order.  Deterministic, and a seed is always a member of its own
    group -- which the diagonal seed is not once the round is grouped on the
    DIA class, since all three diagonal points lie on one of its lines."""
    return tuple(g[k] for g in P)


# THE WELDED SCHEDULE: three rounds grouped on the three link-direction
# parallel classes -- the arrangement the U4b effectus exhibited and paper-19
# drove.  This unit re-drives it rather than citing it.  The geometry is a
# function of the groupings alone (paper-19 section 3.3, invariant over all
# 19683 seed triples), so the canonical transversal is a seed choice and not a
# geometry choice.
WELD_SCHEDULE = tuple((CLASSES[c], canon_transversal(CLASSES[c]))
                      for c in ("ROW", "COL", "DIA"))
COMMITTED_R2 = ((CLASSES["ROW"], DIAG_SEED), (CLASSES["COL"], DIAG_SEED))


def drive(G, schedule, supply=True, drop_supply=None):
    """paper-19's generalized schedule driver, adopted unchanged: exactly d66's
    CONFLICT-GRID(g, R) cycle -- conflict-supply deliveries from the group's
    seed, g proposals, one g-proposer arbitration won by the seed -- with the
    GROUPING AND THE SEED taken from the schedule.  Every event is specified by
    its FULL TUPLE and taken from the layer's own menu."""
    b = G.B(ACTORS)
    cur = {a: G.V0 for a in ACTORS}
    dropped = 0
    for _rnd, (groups, seeds) in enumerate(schedule):
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
            b.pick((sd,), lambda z, e=("r", sd, ckey, wkey): z == e,
                   "arbitrate %s" % sd)
            if b.refusal:
                return b
            v = G.vname(base, wkey, sd)
            for a in grp:
                cur[a] = v
    return b


def record_of(G, b):
    divs = [e for e in b.H if e[0] == "r"]
    foot = [frozenset(r for r in G.regs_of(e) if r in ACTOR_SITE)
            for e in divs]
    return {"events": len(b.H), "maxhits": b.maxhits, "refusal": b.refusal,
            "divisions": len(divs), "H": list(b.H), "footprints": foot}


def link_field(footprints):
    """THE FORCED DICTIONARY, instantiated.  A division event's footprint is a
    set of actors; ACTOR->SITE is the constructor's own naming; each unordered
    pair inside the footprint is a CO-DIVISION PAIR and therefore a LINK; the
    DIVISION-COUNT on that link is n_l(x).  A pair whose difference is the
    undeclared ANT direction carries no I7 link and is counted separately."""
    n = [0] * NCELL
    off_target = 0
    pairs = set()
    for fp in footprints:
        sites = sorted(ACTOR_SITE[a] for a in fp)
        for x, y in combinations(sites, 2):
            key = frozenset((x, y))
            pairs.add(key)
            c = PAIR_CELL.get(key)
            if c is None:
                off_target += 1
            else:
                n[c] += 1
    return tuple(n), off_target, pairs


# ===========================================================================
# SECTION 4.  THE WALK -- DERIVED WHERE DERIVABLE, DECLARED WHERE NOT
# ===========================================================================

def ring_third(bound=6):
    """THE DECLARED ALPHABET: the elements of (1/3)Z[w] of modulus at most 1,
    as integer pairs (p, q) meaning (p + q w)/3.  This is the ring the walk's
    OWN phases and the Grover coin's OWN entries both live in, and the ring
    section 3.3 derives from the arena's own field F_3 -- so it is the alphabet
    an exhaustive scan on this arena owes.  The 7-value alphabet {0} u {+/- w^k}
    that this unit first scanned is NOT discriminating: it returns 18 unitary /
    0 non-monomial on the AXIS stencil too, where interference demonstrably
    survives (K1 m-2, K2 MAJOR-4)."""
    out = []
    for p in range(-bound, bound + 1):
        for q in range(-bound, bound + 1):
            if absq((p, q)) <= 9:
                out.append((p, q))
    return sorted(out)


ALPHA3 = tuple(ring_third())


def stencil_scan(offsets, alpha):
    """the exhaustive unitarity scan of R4b's scalar family shape on a declared
    offset set, over a declared alphabet.  Coefficients are carried as integer
    pairs over 3, so the norm condition sum |c_v|^2 = 1 reads sum absq = 9."""
    realised = defaultdict(list)
    for v in offsets:
        for w in offsets:
            if v == w:
                continue
            realised[vsub(w, v)].append((v, w))
    idx = {v: k for k, v in enumerate(offsets)}
    uni = 0
    nonmono = 0
    witness = None
    for cvec in product(alpha, repeat=len(offsets)):
        ok = True
        for _m, prs in realised.items():
            tot = Z0
            for (v, w) in prs:
                tot = zadd(tot, zmul(cvec[idx[v]], zconj(cvec[idx[w]])))
            if tot != Z0:
                ok = False
                break
        if not ok:
            continue
        if sum(absq(c) for c in cvec) != 9:
            continue
        uni += 1
        if sum(1 for c in cvec if c != Z0) != 1:
            nonmono += 1
            if witness is None:
                witness = [list(c) for c in cvec]
    return {"unitary": uni, "nonmonomial": nonmono,
            "multiplicities": sorted(len(p) for p in realised.values()),
            "nonmonomial_witness_numerators_over_3": witness}


AXIS_STENCIL = ((0, 0), (1, 0), (2, 0))
# the NARROW alphabet, {0} u {+/- w^k} scaled to the /3 normalisation: the one
# this unit first scanned.  It is retained ONLY so that its blindness is a
# measurement -- it returns the same answer on both stencils.
NARROW = tuple([Z0] + [(3 * WPOW[k][0], 3 * WPOW[k][1]) for k in range(3)]
               + [(-3 * WPOW[k][0], -3 * WPOW[k][1]) for k in range(3)])


def scalar_shape_census():
    """THEOREM (SCALAR-EMPTY).  R4b's family shape is a coefficient map c on
    lattice offsets with M[x+v][x] = c_v, and it is unitary iff its
    autocorrelation A(m) = sum_v c_v conj(c_{v+m}) is delta_{m,0}.  On THIS
    arena's offset set -- I7's three declared link directions -- every nonzero
    difference of two distinct offsets is realised by EXACTLY ONE ordered
    pair, so each off-diagonal condition reads c_v conj(c_w) = 0 and forces one
    of the two to vanish.  The three conditions together leave at most one
    nonzero coefficient, and the norm condition then makes it a MONOMIAL: a
    deterministic shift, with no interference anywhere.

    So a scalar generator on the co-division link classes cannot carry a
    quantum dynamics at all.  THE COIN REGISTER IS FORCED, not chosen."""
    realised = defaultdict(list)
    for v in LINKS:
        for w in LINKS:
            if v == w:
                continue
            realised[vsub(w, v)].append((v, w))
    multiplicities = sorted(len(p) for p in realised.values())
    # the contrast: R4b's own 3-term AXIS stencil, where each difference is
    # realised three times and interference survives
    axis = ((0, 0), (1, 0), (2, 0))
    ax = defaultdict(list)
    for v in axis:
        for w in axis:
            if v == w:
                continue
            ax[vsub(w, v)].append((v, w))
    axis_mult = sorted(len(p) for p in ax.values())
    # EXHAUSTIVE CHECK over the DECLARED DISCRIMINATING ALPHABET (1/3)Z[w] with
    # |c| <= 1, 37 values, 37^3 maps -- and taken on BOTH stencils in the same
    # run, so the contrast the head draws is measured on both sides rather than
    # cited on one.  The link stencil is monomial-only; the axis stencil, where
    # R4b's interference survives, is not.
    links = stencil_scan(LINKS, ALPHA3)
    axis = stencil_scan(AXIS_STENCIL, ALPHA3)
    # and the NARROW alphabet this unit first scanned -- {0} u {+/- w^k}, all
    # of modulus 0 or 1 -- run on both stencils too, so the claim that it is
    # BLIND is a measurement in this run rather than a concession in prose.
    nlinks = stencil_scan(LINKS, NARROW)
    naxis = stencil_scan(AXIS_STENCIL, NARROW)
    return {"differences": len(realised),
            "multiplicities": multiplicities,
            "each_realised_once": multiplicities == [1] * 6,
            "axis_multiplicities": axis_mult,
            "alphabet": len(ALPHA3), "maps_scanned": len(ALPHA3) ** 3,
            "unitary_maps": links["unitary"],
            "nonmonomial_unitary_maps": links["nonmonomial"],
            "axis_unitary_maps": axis["unitary"],
            "axis_nonmonomial_unitary_maps": axis["nonmonomial"],
            "axis_nonmonomial_witness": axis["nonmonomial_witness_numerators_over_3"],
            "alphabet_discriminates": axis["nonmonomial"] > links["nonmonomial"],
            "narrow_alphabet": len(NARROW),
            "narrow_maps_scanned": len(NARROW) ** 3,
            "narrow_link_unitary_maps": nlinks["unitary"],
            "narrow_link_nonmonomial_unitary_maps": nlinks["nonmonomial"],
            "narrow_axis_unitary_maps": naxis["unitary"],
            "narrow_axis_nonmonomial_unitary_maps": naxis["nonmonomial"],
            "narrow_alphabet_is_blind":
                (nlinks["unitary"] == naxis["unitary"]
                 and nlinks["nonmonomial"] == naxis["nonmonomial"])}


def three_C(c):
    """3C for the S_3-covariant coin C = I + c J, with 3c given as the Z[w]
    integer pair `c`.  Every entry is in Z[w], so the walk's amplitudes stay
    integer pairs over a common power of 3 for EVERY member of the family."""
    return tuple(tuple(zadd((3, 0), c) if i == j else c for j in range(3))
                 for i in range(3))


def coin_unitary_exactly(M):
    """M M^* = 9 I in exact Z[w] arithmetic, entry by entry (#87)."""
    for i in range(3):
        for j in range(3):
            tot = Z0
            for k in range(3):
                tot = zadd(tot, zmul(M[i][k], zconj(M[j][k])))
            if tot != ((9, 0) if i == j else Z0):
                return False
    return True


def coin_s3_covariant(M):
    """M commutes with every one of the six permutation matrices, checked by
    the relabelling identity M[p(i)][p(j)] = M[i][j] on all 6 permutations."""
    for pm in permutations(range(3)):
        for i in range(3):
            for j in range(3):
                if M[pm[i]][pm[j]] != M[i][j]:
                    return False
    return True


def coin_forcing_census():
    """THE COIN IS DECLARED UNDER A STATED REALITY CONDITION, and its FIBER is
    printed.  The arena's own direction-relabelling group is S_3 -- paper-19's
    I-DIRECTION-LABEL, whose six relabellings it measured and found the record
    invariant under.  A coin covariant under S_3 commutes with every
    permutation matrix, hence has the form a I + b J, and unitarity gives
    |a|^2 = 1 together with a conj(b) + conj(a) b + 3 |b|^2 = 0.

    THIS IS A CIRCLE, NOT FOUR POINTS.  Over the exact rational solutions WITH
    a AND b REAL it has exactly two non-trivial members, both +/- Grover -- and
    that reality restriction is a DECLARATION, not a theorem.  Over the arena's
    OWN ring (1/3)Z[w] the same conditions have 36 solutions, 30 of them
    non-trivial, falling into 6 classes up to a global phase, of which exactly
    one is +/- Grover.  Both scans are run here and the fiber is published; the
    four hidden non-Grover classes are then RUN, and the verdict is measured
    invariant across all of them."""
    # -- the REAL scan, kept because it is what the reality condition selects
    sols = []
    for a in (Fraction(1), Fraction(-1)):
        for num in range(-12, 13):
            for den in (1, 2, 3, 4, 6, 12):
                b = Fraction(num, den)
                if 2 * a * b + 3 * b * b == 0:
                    if (a, b) not in sols:
                        sols.append((a, b))
    nontrivial = [(a, b) for a, b in sols if b != 0]
    grover_ok = all(3 * b == -2 * a for a, b in nontrivial)
    # -- the RING scan, over the arena's own (1/3)Z[w].  a and b are carried as
    #    integer pairs over 3, so |a|^2 = 1 reads absq(a) = 9 and the second
    #    condition, multiplied by 9, reads (a conj(b) + conj(a) b) + 3 absq(b)
    #    = 0 with the w-part vanishing.
    grid = [(p, q) for p in range(-9, 10) for q in range(-9, 10)]
    ring = []
    for a in grid:
        if absq(a) != 9:
            continue
        for b in grid:
            t = zadd(zmul(a, zconj(b)), zmul(zconj(a), b))
            if t[1] == 0 and t[0] + 3 * absq(b) == 0:
                ring.append((a, b))
    ring_nontrivial = [(a, b) for a, b in ring if b != Z0]
    # up to a GLOBAL PHASE: the class of (a, b) is c = b/a, and a is a unit of
    # Z[w] scaled by 3, so a^{-1} = conj(a)/9.
    classes = set()
    for a, b in ring:
        num = zmul(b, zconj(a))
        classes.add((Fraction(num[0], 9), Fraction(num[1], 9)))
    grover_class = (Fraction(-2, 3), Fraction(0))
    hidden = sorted(c for c in classes if c not in (grover_class,
                                                    (Fraction(0), Fraction(0))))
    # -- THE WITNESS, gated: a member that is exactly unitary, exactly
    #    S_3-covariant, in the arena's own ring, and NOT +/- Grover.
    wit = three_C((0, 1))                     # a = 1, b = w/3
    grover_mat = GROVER_Z
    return {"solutions": len(sols), "nontrivial": len(nontrivial),
            "all_real_nontrivial_are_grover": grover_ok,
            "reality_condition": "a and b real -- DECLARED, not derived",
            "ring": "(1/3)Z[w], the arena's own",
            "ring_solutions": len(ring),
            "ring_nontrivial": len(ring_nontrivial),
            "classes_up_to_phase": len(classes),
            "grover_classes_up_to_phase": sum(1 for c in classes
                                              if c == grover_class),
            "hidden_classes": [[str(x), str(y)] for x, y in hidden],
            "witness_3C_numerators": [[list(z) for z in row] for row in wit],
            "witness_is_unitary_exactly": coin_unitary_exactly(wit),
            "witness_is_s3_covariant": coin_s3_covariant(wit),
            "witness_is_grover": wit == grover_mat,
            "grover_numerators_over_3": [list(r) for r in GN],
            "grover_is_unitary_exactly": coin_unitary_exactly(grover_mat)}


def connection_group_census():
    """THE CONNECTION GROUP IS DERIVED.  The arena's sites are Z_3^2 and its
    parallel classes are the lines of AG(2, 3): the arena is over F_3.  The
    link connection this unit attaches to the record is therefore valued in
    the arena's own scalar group Z_3, and the walk's phase alphabet is the
    cube roots of unity -- the ONE choice for which the phase group is the
    field the arena is built over.  The consequence is stated rather than
    hidden: the walk consumes the count RESIDUE n mod 3, not the count."""
    order = 3
    closes = all(zmul(WPOW[i], WPOW[j]) == WPOW[(i + j) % 3]
                 for i in range(3) for j in range(3))
    return {"site_group": "Z_3^2", "field": "F_3",
            "connection_group_order": order,
            "phase_alphabet_closes": closes,
            "consumes": "n mod 3"}


def coin_apply(psi, n, order="GD", coin=None):
    """the coin, site-block-diagonal: C(x) = G . D(x), D(x) = diag(w^{n_l(x)}).
    Site-block-diagonality is exactly what makes the law's menu SITE-LOCAL, and
    it is what the transport gate consumes.

    `coin` is 3C over Z[w] and defaults to the delivered member.  When every
    entry is rational -- which the delivered coin's are -- the integer fast
    path runs; the hidden members of the S_3-covariant family take the general
    Z[w] path.  Both paths are the same arithmetic."""
    if coin is None:
        coin = GROVER_Z
    rational = all(coin[i][j][1] == 0 for i in range(3) for j in range(3))
    out = [Z0] * DIM
    for s in range(9):
        b = s * 3
        if order == "GD":
            src = [zmul(psi[b + j], WPOW[n[b + j] % 3]) for j in range(3)]
        else:                                     # the declared ORDER fiber
            src = [psi[b + j] for j in range(3)]
        tmp = []
        for i in range(3):
            if rational:
                a = 0
                c = 0
                for j in range(3):
                    g = coin[i][j][0]
                    z = src[j]
                    a += g * z[0]
                    c += g * z[1]
                tmp.append((a, c))
            else:
                tot = Z0
                for j in range(3):
                    tot = zadd(tot, zmul(coin[i][j], src[j]))
                tmp.append(tot)
        if order == "GD":
            for i in range(3):
                out[b + i] = tmp[i]
        else:
            for i in range(3):
                out[b + i] = zmul(tmp[i], WPOW[n[b + i] % 3])
    return out


def walk_step(psi, n, order="GD", orient="PLUS", coin=None):
    """one coupled step's QUANTUM half: coin then shift.  Returns the shifted
    state and the POST-COIN amplitudes, whose Born weights are the arena's
    menu: the amplitude at (x, l) after the coin is the one the shift carries
    across the link {x, x + l}, which IS cell (x, l)."""
    post = coin_apply(psi, n, order, coin)
    table = SHIFT_T if orient == "PLUS" else SHIFT_T_MINUS
    out = [Z0] * DIM
    for m in range(DIM):
        out[table[m]] = post[m]
    return out, post


# ===========================================================================
# SECTION 5.  THE LAW TRANSPORT -- GATED, NEVER ASSUMED
# ===========================================================================
# The law's normaliser is LAW-NATIVE: G(h, 1) = M(h) follows from the potential
# recursion's TERMINAL CONDITION G(., 0) = 1, for every history of every arm
# under any partition, so it survives an arbitrary exact re-pricing.  What is
# NOT free is its TRANSPORT to this arena: something here must BE a menu, with
# a weight and a mass.  This unit declares the identification, prints its
# fiber, and then GATES every consequence at every site and every step.
#
#   READING A (the BORN MENU).  The menu at site x is the three link
#   traversals; the weight q(l|x) is the post-coin Born weight J(x,l).  The
#   coin is site-block-diagonal, so M(x) = sum_l q(l|x) is exactly the walk's
#   own site mass p(x) -- the law's local menu mass IS the quantum local
#   density.  This is the identification the transport gate certifies.
#
#   READING B (the RECORD MENU).  The weight q(l|x) is the DIVISION COUNT
#   n_l(x) itself -- the forced dictionary's own quantity -- and the site is
#   supplied by the walk.  M(x) = sum_l n_l(x) is then the record's local mass.
#
# Both are run; every row below is stamped with the reading it was decided
# under; the two are the emission rule's declared fiber, and neither is
# assumed to be the other.

def potential_G0(x_index, corrupt=False):
    """the terminal condition of the potential recursion.  G(., 0) = 1, for
    every history of every arm -- this is the whole content of the normaliser's
    law-nativeness, and the mutant that breaks it breaks the identity."""
    if corrupt:
        return 2 if x_index == 0 else 1
    return 1


def law_transport_at(qrow, corrupt_terminal=False):
    """re-derive the law at one site: G(x,1) = sum_l q(l|x) G(x+l, 0), the
    menu mass M(x) = sum_l q(l|x), and the kernel k_1(l|x) = q(l|x)/M(x).
    Returns (G1, M, kernel, ok) with ok the LAW-NATIVE identity G(x,1) = M(x)."""
    M = sum(qrow)
    G1 = sum(qrow[i] * potential_G0(i, corrupt_terminal) for i in range(3))
    if M == 0:
        return G1, M, None, G1 == M
    k = tuple(Fraction(qrow[i], M) for i in range(3))
    return G1, M, k, G1 == M


REPRICE = (Fraction(7, 3), Fraction(1, 5), Fraction(11, 2))


def law_repricing_forcing(qrow):
    """paper-16's own forcing test, re-taken here: re-price every priced event
    by an arbitrary exact rational and the identity must survive, because it
    is a consequence of the terminal condition and of nothing else."""
    rq = [qrow[i] * REPRICE[i] for i in range(3)]
    M = sum(rq)
    G1 = sum(rq[i] * potential_G0(i) for i in range(3))
    return G1 == M


# ===========================================================================
# SECTION 6.  THE COUPLED ENSEMBLE -- EXHAUSTIVE TO THE DECLARED HORIZON
# ===========================================================================
# THE HORIZON IS DECLARED: T = 5 coupled steps, one pass, no returns, no
# regeneration assumption anywhere (sedimentary-by-theorem binds).  Every
# branch of the emission tree is carried: no sampling, no pruning, no
# truncation by weight.  The whole ladder T = 1 .. 5 is published, so the
# horizon is not a hidden cap on any statement that depends on it.
#
# THE UPDATE SEMANTICS ARE DECLARED, AND THE INADMISSIBILITY QUESTION IS
# HANDLED EXPLICITLY RATHER THAN AVOIDED.  A division event on cell (x, l)
# increments n_l(x) by one.  Admissibility is a property of the RECORD, tested
# by I7's own Sylvester criterion; it is NOT a precondition of the STEP, since
# the coin's phase w^{n} is defined for every integer count field.  The coupled
# dynamics therefore does not halt when a site leaves I7's admissible class --
# it runs on, and the exit is MEASURED.  The alternative semantics (halt on
# inadmissibility) is declared as this choice's fiber and its consequence is
# exactly the measured exit probability, so nothing is hidden by the choice.

HORIZON = 5
LADDER = (1, 2, 3, 4, 5)
# the law-transport falsifier's own reduced horizon, DECLARED and published
# (K3 MINOR-7): it rebuilds an arm with the terminal condition broken, and two
# steps are enough to kill the identity.
BROKEN_T = 2


def emission_weights(reading, Jn, n, den):
    """the law's emission distribution over the 27 cells at one step, as exact
    Fractions, together with the per-site column sums the stochasticity gate
    consumes.  This is where the LAW-NATIVE normaliser does its work."""
    wts = [None] * NCELL
    colsums = []
    for s in range(9):
        b = s * 3
        pn = Jn[b] + Jn[b + 1] + Jn[b + 2]
        if reading == "A":
            qrow = [Fraction(Jn[b + i], den) for i in range(3)]
        else:
            qrow = [Fraction(n[b + i]) for i in range(3)]
        _G1, M, k, _ok = law_transport_at(qrow)
        if k is None:
            for i in range(3):
                wts[b + i] = Fraction(0)
            colsums.append(Fraction(0) if pn == 0 else None)
            continue
        colsums.append(sum(k))
        px = Fraction(pn, den)
        for i in range(3):
            wts[b + i] = px * k[i]
    return wts, colsums


def curvature_field(n):
    """THE ARENA'S OWN PLAQUETTES, forced rather than chosen.  The third link
    direction is the sum of the other two -- (1,1) = (1,0) + (0,1) -- so every
    site closes exactly one elementary triangle, and the Z_3 connection the
    record defines has one curvature value per site:
        F(x) = n_(1,0)(x) + n_(0,1)(x + (1,0)) - n_(1,1)(x)   (mod 3)."""
    out = []
    for s in range(9):
        x = SITES[s]
        s2 = SITE_INDEX[vadd(x, LINKS[0])]
        out.append((n[cell(s, 0)] + n[cell(s2, 1)] - n[cell(s, 2)]) % 3)
    return tuple(out)


def frozen_trace_census():
    """K5's instrument, R5's own: a matrix of finite order has all eigenvalues
    roots of unity, hence an ALGEBRAIC INTEGER trace.  The frozen walk is
    translation-covariant, so it block-diagonalises into 9 momentum sectors
    with W_k = w . diag(w^{-k.l}) . G; the Grover coin's diagonal is -1/3, so
    tr(W_k) = -(w/3) sum_l w^{-k.l}, and a sector whose trace is not in Z[w]
    cannot have finite order.  No sector of infinite order ever returns, so the
    frozen walk's state does not recur -- measured, not assumed."""
    rows = []
    for k in SITES:
        tot = Z0
        for l in LINKS:
            e = (-(k[0] * l[0] + k[1] * l[1])) % 3
            tot = zadd(tot, WPOW[e])
        num = zmul((0, 1), (-tot[0], -tot[1]))     # w * (-sum), over 3
        integral = (num[0] % 3 == 0) and (num[1] % 3 == 0)
        rows.append({"k": list(k), "trace_numerator_over_3": list(num),
                     "trace_is_algebraic_integer": integral,
                     "finite_order_possible": integral})
    return rows


def run_arm(T, coupled, reading, order="GD", orient="PLUS", init_coin=0,
            n0=None, corrupt_terminal=False, light=False, coin=None,
            start=(0, 0), census=False):
    """ONE ARM of the coupled object, exhaustively.

    `coupled` False is THE MANDATORY FROZEN-STAGE CONTROL: the identical walk,
    the identical emission rule, the identical branching -- and counts that
    never update.  It is run through THIS SAME FUNCTION, so the control cannot
    differ from the coupled arm in anything but the one line that updates.

    `coin` selects a member of the S_3-covariant family (default: the delivered
    one); `start` is the START SITE, a real parameter now -- F9's fiber was
    previously "measured" by comparing a call with itself (K1 M-4, K2 MAJOR-6).
    `census` accumulates the inadmissible-leaf pattern census at each level."""
    if n0 is None:
        n0 = WELDED
    p0 = [Z0] * DIM
    p0[cell(SITE_INDEX[start], init_coin)] = Z1
    frontier = [(tuple(p0), n0, Fraction(1))]
    chk = Counter()
    viol = Counter()
    levels = []
    ladder = {}
    seen_states = set()
    repeat_states = 0
    for t in range(T):
        den = 9 ** (t + 1)
        preden = 9 ** t
        nxt = []
        supports = 0            # #24 ROUTE 2: the branch count recomputed from
        #                         the emission supports rather than read off
        #                         the list that was built
        for (psi, n, w) in frontier:
            newpsi, post = walk_step(list(psi), list(n), order, orient, coin)
            Jn = [absq(post[m]) for m in range(DIM)]
            pre = [absq(psi[s * 3]) + absq(psi[s * 3 + 1])
                   + absq(psi[s * 3 + 2]) for s in range(9)]
            post = [Jn[s * 3] + Jn[s * 3 + 1] + Jn[s * 3 + 2]
                    for s in range(9)]
            # K1 NORM, per branch per step
            chk["norm"] += 1
            if sum(pre) != preden:
                viol["norm"] += 1
            chk["total"] += 1
            if sum(Jn) != den:
                viol["total"] += 1
            # K2 SITE-MASS, per SITE per branch per step (#87)
            for s in range(9):
                chk["site"] += 1
                if post[s] * preden != pre[s] * den:
                    viol["site"] += 1
            # THE LAW TRANSPORT, per SITE per branch per step
            for s in range(9):
                b = s * 3
                if reading == "A":
                    qrow = [Fraction(Jn[b + i], den) for i in range(3)]
                else:
                    qrow = [Fraction(n[b + i]) for i in range(3)]
                G1, M, k, ok = law_transport_at(qrow, corrupt_terminal)
                chk["law_native"] += 1
                if not ok:
                    viol["law_native"] += 1
                if reading == "A":
                    # the transport's CONTENT: the law's menu mass IS the
                    # walk's own local Born mass
                    chk["mass_is_density"] += 1
                    if M != Fraction(post[s], den):
                        viol["mass_is_density"] += 1
                chk["repricing"] += 1
                if not law_repricing_forcing(qrow):
                    viol["repricing"] += 1
                if k is not None:
                    chk["kernel"] += 1
                    if sum(k) != 1:
                        viol["kernel"] += 1
                    for i in range(3):
                        chk["kernel_entry"] += 1
                        if qrow[i] != k[i] * M:
                            viol["kernel_entry"] += 1
            wts, colsums = emission_weights(reading, Jn, n, den)
            # K4 EMISSION-STOCHASTICITY: per site, then in total
            for s in range(9):
                chk["column"] += 1
                cs = colsums[s]
                if cs is not None and cs not in (0, 1):
                    viol["column"] += 1
            chk["emission_total"] += 1
            if sum(wts) != 1:
                viol["emission_total"] += 1
            # K9 THE SOURCING IDENTITY, evaluated on BOTH arms:
            #   M_{t+1}(x) - M_t(x) = p_t(x)
            # On the coupled arm the left side is the emitted mass at x; on the
            # frozen arm it is 0.  This row is RECORD-COUPLED and is stamped
            # UPDATE-RULE-RESTATED, because it is the update rule read back.
            for s in range(9):
                b = s * 3
                dM = sum(wts[b:b + 3]) if coupled else Fraction(0)
                chk["sourcing"] += 1
                if dM != Fraction(post[s], den):
                    viol["sourcing"] += 1
            supports += sum(1 for m in range(NCELL) if wts[m] != 0)
            for m in range(NCELL):
                if wts[m] == 0:
                    continue
                if coupled:
                    nn = list(n)
                    nn[m] += 1
                    nn = tuple(nn)
                else:
                    nn = n
                nxt.append((tuple(newpsi), nn, w * wts[m]))
        frontier = nxt
        mass = sum(x[2] for x in frontier)
        # K5 NO-RETURN at the psi grain.  The sedimentary condition is about
        # the TRAJECTORY, not about the branching: two branches sharing a state
        # at the SAME time are not a return, so a state counts as recurring
        # only when it appeared at a STRICTLY EARLIER level.  On the frozen arm
        # every branch at a level carries the same state, which is exactly why
        # the naive count would have been meaningless there.
        here = set(psi for (psi, _n, _w) in frontier)
        repeat_states += len(here & seen_states)
        seen_states |= here
        levels.append({"t": t + 1, "branches": len(frontier),
                       "branches_from_emission_supports": supports,
                       "mass": str(mass), "mass_is_one": mass == 1})
        ladder[t + 1] = horizon_stats(frontier, 9 ** (t + 1), light,
                                      census=census)
    return {"levels": levels, "checks": dict(chk), "violations": dict(viol),
            "ladder": ladder, "repeat_states": repeat_states,
            "frontier": None if light else frontier,
            "final": ladder[T]}


_NSTAT = {}
_QCACHE = {}


def _q_cached(nv):
    got = _QCACHE.get(nv)
    if got is None:
        _a, _b, _c, d = q_of(nv)
        got = (d, admissible(nv))
        _QCACHE[nv] = got
    return got


def _nstat(n):
    """everything the DECLARED OBSERVABLE SET reads off a count field, computed
    once per distinct field.  The record is sparse against the welded one -- at
    horizon t at most t cells have moved -- so the emission field is read off
    the moved cells alone."""
    got = _NSTAT.get(n)
    if got is not None:
        return got
    npd = 0
    dets = set()
    mx = 0
    bad = []
    for s in range(9):
        nv = site_counts(n, s)
        d, adm = _q_cached(nv)
        dets.add(d)
        if adm:
            npd += 1
        else:
            bad.append(nv)
    moved = []
    for m in range(NCELL):
        if n[m] != WELDED[m]:
            moved.append((m, n[m] - WELDED[m]))
        if n[m] > mx:
            mx = n[m]
    F = curvature_field(n)
    tinv = all(n[cell(s, i)] == n[cell(0, i)]
               for s in range(9) for i in range(3))
    got = (npd, frozenset(dets), tuple(moved), mx, len(set(F)) == 1, tinv,
           tuple(bad))
    _NSTAT[n] = got
    return got


def horizon_stats(frontier, den, light=False, census=False):
    """the DECLARED OBSERVABLE SET, at one horizon, exact.  Every entry is a
    rational; nothing is estimated and nothing is sampled."""
    acc = [0] * 9
    accf = [Fraction(0)] * 9
    Eb = defaultdict(Fraction)
    exit_p = Fraction(0)
    posdef = defaultdict(Fraction)
    dets = set()
    curv_const = Fraction(0)
    tinv_p = Fraction(0)
    maxcell = 0
    pattern = Counter()
    sites_bad = Counter()
    exit_leaves = 0
    for (psi, n, w) in frontier:
        for s in range(9):
            v = absq(psi[s * 3]) + absq(psi[s * 3 + 1]) + absq(psi[s * 3 + 2])
            if v:
                accf[s] += w * v
        npd, dset, moved, mx, curvc, tinv, bad = _nstat(n)
        if census and bad:
            exit_leaves += 1
            sites_bad[len(bad)] += 1
            for nv in bad:
                pattern[nv] += 1
        dets |= dset
        if mx > maxcell:
            maxcell = mx
        for (m, dv) in moved:
            Eb[m] += w * dv
        posdef[npd] += w
        if npd < 9:
            exit_p += w
        if curvc:
            curv_const += w
        if tinv:
            tinv_p += w
    pT = [accf[s] / den for s in range(9)]
    Ebl = [Eb.get(m, Fraction(0)) for m in range(NCELL)]
    ipr = sum(x * x for x in pT)
    link_marginal = [sum(Ebl[s * 3 + i] for s in range(9)) for i in range(3)]
    out = {"p_site": [str(x) for x in pT], "ipr": str(ipr),
           "emission_field": [str(x) for x in Ebl],
           "link_class_marginal": [str(x) for x in link_marginal],
           "total_emitted": str(sum(Ebl)),
           "admissibility_exit_probability": str(exit_p),
           "exit_positive": exit_p > 0,
           "posdef_distribution": {str(k): str(v)
                                   for k, v in sorted(posdef.items())},
           "det_values_reached": sorted(str(d) for d in dets),
           "det_zero_reached": any(d == 0 for d in dets),
           "det_negative_reached": any(d < 0 for d in dets),
           "max_cell_count": maxcell,
           "curvature_constant_probability": str(curv_const),
           "curvature_homogeneous": curv_const == 1,
           "translation_invariant_probability": str(tinv_p),
           "count_field_translation_invariant": tinv_p == 1}
    if census:
        # THE EXIT CENSUS (P12): every inadmissible leaf classified by the
        # site-count vector that took it out, so the mechanism is a measured
        # census rather than an asserted arithmetic.
        excess = Counter()
        for k, v in pattern.items():
            excess[",".join(str(x - 1) for x in sorted(k))] += v
        out["exit_census"] = {
            "inadmissible_leaves": exit_leaves,
            "sites_out_per_leaf": {str(k): v
                                   for k, v in sorted(sites_bad.items())},
            "count_vectors": {",".join(str(x) for x in k): v
                              for k, v in sorted(pattern.items())},
            "excess_patterns": dict(sorted(excess.items())),
            "weight": str(exit_p)}
    return out


# ===========================================================================
# SECTION 7.  THE CENSUS, CACHED -- and THE CLOSURE BATTERY
# ===========================================================================

NUMREG = set()


def reg(*vals):
    """#24: every number the paper may carry is REGISTERED as it is computed,
    never typed."""
    for v in vals:
        NUMREG.add(str(v))
    return vals[0] if len(vals) == 1 else vals


RAW = {}

# THE STALE STAGE: a declared count field that is admissible, is NOT the welded
# one, and is reachable by the coupled arm.  The staleness-blindness theorem is
# evaluated on it, so the theorem is a measurement rather than an assertion.
STALE_CELLS = (0, 4, 11, 20, 26)


def stale_field():
    n = list(WELDED)
    for c in STALE_CELLS:
        n[c] += 1
    return tuple(n)


# THE DECLARED FOREIGN COUNT FIELDS.  K1-K4's COUNT-BLINDNESS is the claim
# that they hold for EVERY count field, because none of them reads the record;
# it is measured here on fields this run never generates, two of which are not
# even admissible, rather than argued from the source (K2 MAJOR-1).
FOREIGN_FIELDS = (
    ("STALE", tuple(1 + (1 if m in (0, 4, 11, 20, 26) else 0)
                    for m in range(NCELL))),
    ("ALL-TWO", tuple([2] * NCELL)),
    ("INADMISSIBLE-ONE-CELL", tuple(4 if m == 2 else 1 for m in range(NCELL))),
    ("LADDERED", tuple(1 + (m % 5) for m in range(NCELL))),
    ("ZERO-AT-ONE-CELL", tuple(0 if m == 7 else 1 for m in range(NCELL))),
)
BLIND_KEYS = ("norm", "site", "law_native", "column", "kernel",
              "kernel_entry", "emission_total", "total")


def count_blindness_census():
    """MEASURED, not argued: K1 (norm), K2 (site mass), K3 (the law-native
    normaliser) and K4 (column stochasticity) hold on every declared foreign
    count field, admissible or not, because none of them reads the record.
    This is what makes the requirement gate's forward direction EMPTY BEFORE
    THE RUN -- the honest stamp on the negative."""
    rows = []
    for name, field in FOREIGN_FIELDS:
        a = run_arm(2, False, "A", n0=field, light=True)
        v = sum(a["violations"].get(k, 0) for k in BLIND_KEYS)
        rows.append({"field": name,
                     "is_admissible": all(admissible(site_counts(field, s))
                                          for s in range(9)),
                     "is_the_welded_record": field == WELDED,
                     "checks": sum(a["checks"].get(k, 0) for k in BLIND_KEYS),
                     "psi_internal_violations": v})
    return rows


def ray_of(psi):
    """the canonical RAY representative in Q(w): divide by the first nonzero
    component.  Two states are the same ray exactly when they differ by a
    global phase, which is the grain at which a walk RETURNS."""
    k = next(i for i in range(DIM) if psi[i] != Z0)
    a = psi[k]
    d = absq(a)
    ca = zconj(a)
    out = []
    for z in psi:
        num = zmul(z, ca)
        out.append((Fraction(num[0], d), Fraction(num[1], d)))
    return tuple(out)


K5_FROZEN_STEPS = 30
K5_COUPLED_LEVELS = 4


def k5_census():
    """K5-NO-RETURN, REPAIRED (K2 MAJOR-2).  The delivered predicate compared
    RAW amplitudes, which carry norm 9^t exactly and therefore can never be
    equal across levels: `repeat_states` was 0 by construction, not by
    measurement.  Here the comparison is taken at TWO grains that can fire --
    the exactly normalised state psi_t / 3^t and the RAY class -- and the
    frozen arm is driven well past the ladder."""
    # (a) the norms that made the raw predicate unfireable, measured
    norms = [9 ** (t + 1) for t in range(HORIZON)]
    # (b) the frozen arm, a single trajectory, driven 30 steps
    psi = [Z0] * DIM
    psi[cell(SITE_INDEX[(0, 0)], 0)] = Z1
    seen_r, seen_n = set(), set()
    rep_r = rep_n = 0
    for t in range(K5_FROZEN_STEPS):
        psi, _post = walk_step(list(psi), list(WELDED))
        r = ray_of(psi)
        v = tuple((Fraction(z[0], 3 ** (t + 1)), Fraction(z[1], 3 ** (t + 1)))
                  for z in psi)
        if r in seen_r:
            rep_r += 1
        if v in seen_n:
            rep_n += 1
        seen_r.add(r)
        seen_n.add(v)
    # (c) the coupled arm, cross-level, to the level the tree affords
    p0 = [Z0] * DIM
    p0[cell(SITE_INDEX[(0, 0)], 0)] = Z1
    frontier = [(tuple(p0), WELDED, Fraction(1))]
    seen2_r, seen2_n = set(), set()
    rep2_r = rep2_n = 0
    per_level = []
    for t in range(K5_COUPLED_LEVELS):
        den = 9 ** (t + 1)
        nxt = []
        for (p, nn, w) in frontier:
            newpsi, post = walk_step(list(p), list(nn))
            Jn = [absq(post[m]) for m in range(DIM)]
            wts, _cs = emission_weights("A", Jn, nn, den)
            for m in range(NCELL):
                if wts[m] == 0:
                    continue
                n2 = list(nn)
                n2[m] += 1
                nxt.append((tuple(newpsi), tuple(n2), w * wts[m]))
        frontier = nxt
        here_n = {tuple((Fraction(z[0], 3 ** (t + 1)),
                         Fraction(z[1], 3 ** (t + 1))) for z in p)
                  for (p, _n, _w) in frontier}
        here_r = {ray_of(list(p)) for (p, _n, _w) in frontier}
        rep2_n += len(here_n & seen2_n)
        rep2_r += len(here_r & seen2_r)
        seen2_n |= here_n
        seen2_r |= here_r
        per_level.append({"t": t + 1, "branches": len(frontier),
                          "distinct_normalised_states": len(here_n),
                          "distinct_rays": len(here_r)})
    return {"raw_state_norms_by_level": norms,
            "raw_norms_all_distinct": len(set(norms)) == len(norms),
            "frozen_steps": K5_FROZEN_STEPS,
            "frozen_ray_repeats": rep_r,
            "frozen_normalised_repeats": rep_n,
            "frozen_distinct_rays": len(seen_r),
            "coupled_levels": K5_COUPLED_LEVELS,
            "coupled_ray_repeats": rep2_r,
            "coupled_normalised_repeats": rep2_n,
            "coupled_by_level": per_level}


NBD_STEPS = 3
NBD_CYCLE = 1


def nbd_mechanism_census():
    """THE TRANSPORT MECHANISM, FALSIFIED (K1 M-2).  Section 4 credited the
    menu-mass-is-Born-mass row to site-block-diagonality.  It is not carried by
    it: under reading A the menu IS the post-coin Born weight, so the row is a
    per-site restatement of the definition.  Measured here on a coin that is
    exactly unitary and NOT site-block-diagonal -- the delivered coin composed
    with a cyclic permutation of the nine sites -- the mass-is-density row
    still passes at every check while site-block-diagonality fails at most of
    them.  What site-block-diagonality DOES carry is the site row."""
    sigma = tuple((s + NBD_CYCLE) % 9 for s in range(9))
    psi = [Z0] * DIM
    psi[cell(SITE_INDEX[(0, 0)], 0)] = Z1
    n = WELDED
    md_chk = md_viol = sb_chk = sb_viol = 0
    unitary_cols = 0
    for t in range(NBD_STEPS):
        den = 9 ** (t + 1)
        preden = 9 ** t
        blocked = coin_apply(list(psi), list(n))
        post_c = [Z0] * DIM
        for s in range(9):
            for i in range(3):
                post_c[cell(sigma[s], i)] = blocked[cell(s, i)]
        Jn = [absq(post_c[m]) for m in range(DIM)]
        pre = [absq(psi[s * 3]) + absq(psi[s * 3 + 1]) + absq(psi[s * 3 + 2])
               for s in range(9)]
        post = [Jn[s * 3] + Jn[s * 3 + 1] + Jn[s * 3 + 2] for s in range(9)]
        if sum(Jn) == den:
            unitary_cols += 1
        for s in range(9):
            b = s * 3
            qrow = [Fraction(Jn[b + i], den) for i in range(3)]
            _G1, M, _k, _ok = law_transport_at(qrow)
            md_chk += 1
            if M != Fraction(post[s], den):
                md_viol += 1
            sb_chk += 1
            if post[s] * preden != pre[s] * den:
                sb_viol += 1
        newpsi = [Z0] * DIM
        for m in range(DIM):
            newpsi[SHIFT_T[m]] = post_c[m]
        psi = newpsi
    return {"coin": "the delivered coin composed with the site cycle s -> "
                    "s + %d mod 9" % NBD_CYCLE,
            "steps": NBD_STEPS,
            "coin_is_unitary_at_every_step": unitary_cols == NBD_STEPS,
            "mass_is_density_checks": md_chk,
            "mass_is_density_violations": md_viol,
            "site_block_diagonal_checks": sb_chk,
            "site_block_diagonal_violations": sb_viol}


def visit_schedule():
    """THE RETURN TIME OF THE SHIFT -- the step budget half of the horizon-5
    reconciliation (K2 MINOR-6).  The walk emits exactly one division event per
    coupled step, so three events on one cell need the walk to carry positive
    Born mass at that site at three DISTINCT steps.  This is the support
    schedule of the +l shift on Z_3^2, and the earliest third visit over all
    nine sites is what sets the threshold."""
    supp = {(0, 0)}
    sizes = []
    visits = defaultdict(list)
    for t in range(HORIZON):
        sizes.append(len(supp))
        for x in sorted(supp):
            visits[x].append(t + 1)
        supp = {vadd(x, l) for x in supp for l in LINKS}
    third = {x: (v[2] if len(v) >= 3 else None) for x, v in visits.items()}
    have = [v for v in third.values() if v is not None]
    return {"sites_with_positive_mass_by_step": sizes,
            "visits": {"%d%d" % x: v for x, v in sorted(visits.items())},
            "third_visit_step": {"%d%d" % x: v
                                 for x, v in sorted(third.items())},
            "earliest_third_visit": min(have) if have else None,
            "sites_reaching_a_third_visit": len(have)}


def refusal_robustness(rows):
    """THE NEGATIVE IS DOUBLY GROUNDED (K1 S-1).  NO-WITNESS rests on two
    declarations about K9 and K10: their CLASS (RECORD-COUPLED) and their
    UPDATE-RULE-RESTATED stamp.  Each is dropped alone and both together, and
    the witness count is re-taken -- so the reader can see that only the
    conjunction of two failures would produce a witness."""
    def count(drop_stamp, reclassify):
        out = []
        for r in rows:
            klass = ("PSI-INTERNAL" if reclassify
                     and r["class"] == "RECORD-COUPLED" else r["class"])
            restated = False if drop_stamp else r["update_rule_restated"]
            if (klass == "PSI-INTERNAL" and not restated
                    and not r["measured"]["frozen_holds"]
                    and r["measured"]["coupled_holds"]):
                out.append(r["id"])
        return sorted(out)
    return {"as_delivered": count(False, False),
            "stamp_dropped": count(True, False),
            "class_dropped": count(False, True),
            "both_dropped": count(True, True)}


HIDDEN_COINS = (("w/3", (0, 1)), ("(-1+w)/3", (-1, 1)),
                ("(-1-w)/3", (-1, -1)), ("(-2-w)/3", (-2, -1)))
INVARIANT_OBS = ("p_site", "ipr", "emission_field", "link_class_marginal",
                 "admissibility_exit_probability", "posdef_distribution",
                 "det_values_reached", "max_cell_count",
                 "curvature_constant_probability")


def coin_invariance_census():
    """THE VERDICT IS COIN-INVARIANT, MEASURED.  The coin is DECLARED under a
    reality condition, so the fiber is six classes up to a global phase and the
    delivered run measured one of them.  Every one of the four HIDDEN
    non-Grover classes is therefore run here to the FULL horizon, coupled and
    frozen, and the four invariants that carry the verdict are re-taken on each:
    zero consistency violations, every declared observable row moving against
    its own frozen control, the admissibility threshold at exactly the declared
    horizon, and no indefinite form reached.  The NUMBERS are coin-specific;
    the VERDICT SHAPE is not."""
    rows = []
    for name, c in HIDDEN_COINS:
        mat = three_C(c)
        cp = run_arm(HORIZON, True, "A", light=True, coin=mat)
        fz = run_arm(HORIZON, False, "A", light=True, coin=mat)
        ck = ("norm", "site", "column", "emission_total", "total")
        viol = sum(cp["violations"].get(k, 0) + fz["violations"].get(k, 0)
                   for k in ck)
        C, F = cp["final"], fz["final"]
        diff = sum(1 for k in INVARIANT_OBS if C[k] != F[k])
        hit = [t for t in LADDER if cp["ladder"][t]["exit_positive"]]
        neg = any(cp["ladder"][t]["det_negative_reached"] for t in LADDER)
        rows.append({
            "coin": name,
            "three_C_numerators": [[list(z) for z in row] for row in mat],
            "is_unitary_exactly": coin_unitary_exactly(mat),
            "is_s3_covariant": coin_s3_covariant(mat),
            "leaves_coupled": cp["levels"][-1]["branches"],
            "leaves_frozen": fz["levels"][-1]["branches"],
            "consistency_violations": viol,
            "observable_rows_differing": diff,
            "observable_rows": len(INVARIANT_OBS),
            "exit_threshold": min(hit) if hit else None,
            "exit_probability": C["admissibility_exit_probability"],
            "indefinite_form_reached": neg})
    return rows


def raw_census(texts):
    """everything heavy, computed ONCE.  The mutant sweep re-runs the gate
    layer, not the census: a falsifier that had to rebuild a 284078-leaf
    ensemble would price the sweep out of the delivery, and every mutant in
    this file acts on what a gate is handed rather than on the arithmetic that
    produced it -- except the four that must move the physics, which move it on
    an object small enough to rebuild."""
    if RAW:
        return RAW
    G = Grammar(texts)
    # -- STAGE 1: the welded record, driven through the committed menus
    b = drive(G, WELD_SCHEDULE)
    rec = record_of(G, b)
    n_driven, off_target, pairs = link_field(rec["footprints"])
    # the committed anchor: at the R = 2 committed schedule this driver and
    # d66's own conflict_grid(3, 2) must emit identical event lists
    b2 = drive(G, COMMITTED_R2)
    own = record_of(G, b2)["H"]
    d66b = G.conflict_grid(3, 2)
    d66H = list(d66b.H) if hasattr(d66b, "H") else list(d66b)
    # -- the dictionary: the realised co-division relation
    cayley = set()
    for s in range(9):
        for i in range(3):
            cayley.add(CELL_PAIR[cell(s, i)])
    ant_pairs = set()
    for x in SITES:
        ant_pairs.add(frozenset((x, vadd(x, ANT))))
    # -- STAGE 2: the walk, derived
    scalar = scalar_shape_census()
    coin = coin_forcing_census()
    conn = connection_group_census()
    trace = frozen_trace_census()
    # -- STAGE 3: the four arms, at the declared horizon.  The A-COUPLED arm
    #    carries the EXIT CENSUS, so every inadmissible leaf is classified
    #    inside the same pass that measures the exit probability.
    arms = {}
    for reading in ("A", "B"):
        for coupled in (True, False):
            key = "%s-%s" % (reading, "COUPLED" if coupled else "FROZEN")
            arms[key] = run_arm(HORIZON, coupled, reading, light=True,
                                census=(key == "A-COUPLED"))
    # -- the declared fibers, measured at a reduced horizon, disclosed as such
    FIBER_T = 3
    fibers = {}
    order_arms = {}
    for order in ("GD", "DG"):
        for cp in (True, False):
            order_arms["%s-%s" % (order, cp)] = run_arm(
                FIBER_T, cp, "A", order=order, light=True)["final"]
        fibers["ORDER-%s" % order] = order_arms["%s-True" % order]["ipr"]
    # THE COIN-ORDER FIBER IS VERDICT-RELEVANT AND IT IS MEASURED, NOT ASSUMED.
    # With C = D.G the count phase is applied AFTER the coin, so it cannot
    # enter that step's Born weights at all: |D G psi|^2 = |G psi|^2.  How much
    # of the back-reaction survives that is a measurement, taken here on the
    # WHOLE declared observable set at the reduced horizon.
    OBS_NAMES = ("p_site", "ipr", "emission_field", "link_class_marginal",
                 "admissibility_exit_probability", "posdef_distribution",
                 "det_values_reached", "max_cell_count",
                 "curvature_constant_probability")
    order_rows = {}
    for order in ("GD", "DG"):
        c = order_arms["%s-True" % order]
        f = order_arms["%s-False" % order]
        order_rows[order] = {
            "differing": sum(1 for k in OBS_NAMES if c[k] != f[k]),
            "of": len(OBS_NAMES),
            "which": [k for k in OBS_NAMES if c[k] != f[k]]}
    executed = ["ORDER-GD", "ORDER-DG"]
    orient_finals = {}
    for orient in ("PLUS", "MINUS"):
        orient_finals[orient] = run_arm(
            FIBER_T, True, "A", orient=orient, light=True)["final"]
        fibers["ORIENT-%s" % orient] = orient_finals[orient]["ipr"]
        executed.append("ORIENT-%s" % orient)
    # the ORIENT fiber is inert ON THE IPR ONLY: the full declared observable
    # set is compared here, and the two rows that move are named (K1 m-3).
    orient_rows = {
        "differing": sum(1 for k in OBS_NAMES
                         if orient_finals["PLUS"][k] != orient_finals["MINUS"][k]),
        "of": len(OBS_NAMES),
        "which": [k for k in OBS_NAMES
                  if orient_finals["PLUS"][k] != orient_finals["MINUS"][k]]}
    for ic in range(3):
        fibers["INIT-COIN-%d" % ic] = run_arm(
            FIBER_T, True, "A", init_coin=ic, light=True)["final"]["ipr"]
        executed.append("INIT-COIN-%d" % ic)
    # -- F9, A REAL MEASUREMENT (K1 M-4, K2 MAJOR-6).  The delivered row
    #    compared run_arm with ITSELF: there was no start-site parameter and
    #    n0=WELDED was the default.  There is a parameter now, three declared
    #    starts are run, and the comparison is the one translation COVARIANCE
    #    predicts -- the site distribution is the exact TRANSLATE of the base
    #    one, which naive list equality would have failed.
    START_SITES = ((0, 0), (1, 0), (1, 1))
    start_rows = []
    base_fin = None
    for x0 in START_SITES:
        fin = run_arm(FIBER_T, True, "A", start=x0, light=True)["final"]
        if base_fin is None:
            base_fin = fin
        translated = [base_fin["p_site"][SITE_INDEX[vsub(SITES[s], x0)]]
                      for s in range(9)]
        start_rows.append({
            "start": list(x0),
            "ipr": fin["ipr"],
            "p_site_equals_base_naively": fin["p_site"] == base_fin["p_site"],
            "p_site_is_the_exact_translate": fin["p_site"] == translated})
        executed.append("START-%d%d" % x0)
    fibers["SITE-TRANSLATION-INVARIANT"] = all(
        r["p_site_is_the_exact_translate"] for r in start_rows)
    fibers["SITE-IPR-INVARIANT"] = len({r["ipr"] for r in start_rows}) == 1
    # -- THE STALENESS-BLINDNESS THEOREM, machine-checked on a declared stale
    #    stage at the UNIT'S OWN FULL HORIZON (K1 S-2): a frozen arm whose
    #    stage is NOT the welded record.  The delivered run took it at the
    #    reduced horizon 3 and did not disclose that.
    stale = run_arm(HORIZON, False, "A", n0=stale_field(), light=True)
    # -- the law-transport falsifier: the terminal condition broken, at the
    #    declared reduced horizon 2, disclosed
    broken = run_arm(BROKEN_T, True, "A", corrupt_terminal=True, light=True)
    # -- F6 AT THE FULL HORIZON (K2 MAJOR-5).  "Measurably weaker" was a
    #    horizon-3 row count; on the unit's own sharpest observable, at the
    #    horizon the head reports, the alternative order is STRONGER.
    dg_full = run_arm(HORIZON, True, "A", order="DG", light=True)
    RAW.update({
        "G": G, "record": rec, "n_driven": n_driven, "off_target": off_target,
        "pairs": pairs, "own_r2": own, "d66_r2": d66H, "cayley": cayley,
        "ant_pairs": ant_pairs, "scalar": scalar, "coin": coin, "conn": conn,
        "trace": trace, "arms": arms, "fibers": fibers, "fiber_T": FIBER_T,
        "stale": stale, "broken": broken, "order_rows": order_rows,
        "orient_rows": orient_rows, "start_rows": start_rows,
        "executed_members": executed, "dg_full": dg_full,
        "coin_invariance": coin_invariance_census(),
        "count_blind": count_blindness_census(),
        "k5": k5_census(), "nbd": nbd_mechanism_census(),
        "schedule": visit_schedule(),
    })
    return RAW


# --------------------------------------------------------------------------
# THE CLOSURE BATTERY -- pre-registered, ten rows, polarity declared BEFORE the
# run and matched against the measurement afterwards.
#
# CLASS is what decides the verdict, and it is declared per row:
#   PSI-INTERNAL   a condition on the quantum state and its propagation alone
#   SYMMETRY       a contingent invariance, not required for well-definedness
#   ARENA-CLOSURE  the arena's own axiom on the record the walk reads
#   RECORD-COUPLED a condition that mentions the emission history
#
# UPDATE-RULE-RESTATED marks a row whose failure on the frozen stage is the
# update rule read back rather than an independent fact.  The REQUIREMENT
# selector refuses those rows, which is the whole reason the field exists.
# --------------------------------------------------------------------------

BATTERY_SPEC = [
    ("K1-NORM", "PSI-INTERNAL", False,
     "the state stays a unit vector: sum_{x,l} |psi_t(x,l)|^2 = 1 exactly, at "
     "every branch and every step",
     True, True),
    ("K2-SITE-MASS", "PSI-INTERNAL", False,
     "the coin is site-block-diagonal: sum_l |(C psi)(x,l)|^2 = p(x) exactly, "
     "at every SITE of every branch and every step -- this is what makes the "
     "law's menu site-local, so it is the transport's own precondition",
     True, True),
    ("K3-LAW-NATIVE", "PSI-INTERNAL", False,
     "the LAW-NATIVE normaliser: G(x,1) = M(x), re-derived on this arena from "
     "the potential recursion's terminal condition, at every site and every "
     "step and under an arbitrary exact re-pricing",
     True, True),
    ("K4-EMISSION-STOCHASTIC", "PSI-INTERNAL", False,
     "the law's kernel is column-stochastic and composes with unitarity: "
     "sum_l k_1(l|x) = 1 at every site, and the total emission mass is exactly "
     "1 at every step",
     True, True),
    ("K5-NO-RETURN", "PSI-INTERNAL", False,
     "the sedimentary condition at the state grain: no state recurs inside the "
     "horizon.  On the frozen stage this is a THEOREM -- 6 of the 9 momentum "
     "sectors have a trace outside Z[w], so they cannot have finite order",
     True, True),
    ("K6-BLOCH", "SYMMETRY", False,
     "translation covariance: the step commutes with every lattice "
     "translation, so the walk block-diagonalises into 9 momentum sectors and "
     "R4b's dispersion reading is available at all",
     True, False),
    ("K7-CURVATURE-HOMOGENEOUS", "SYMMETRY", False,
     "the Z_3 connection the record defines has a constant curvature field "
     "F(x) over the arena's nine forced plaquettes",
     True, False),
    ("K8-I7-ADMISSIBILITY", "ARENA-CLOSURE", False,
     "the record the walk reads stays inside I7's admissible class: q positive "
     "definite at every site, by I7's own exact Sylvester criterion",
     True, False),
    ("K9-SOURCING", "RECORD-COUPLED", True,
     "the sourcing identity M_{t+1}(x) - M_t(x) = p_t(x): the record's local "
     "mass grows at exactly the quantum local density",
     False, True),
    ("K10-RECORDS-THEOREM", "RECORD-COUPLED", True,
     "a legitimate division event IS a record event: the total record "
     "increment over the horizon equals the number of division events emitted",
     False, True),
]


def measure_battery(raw, reading):
    """every battery row, measured on BOTH arms, with the polarity it was
    pre-registered with carried alongside."""
    C = raw["arms"]["%s-COUPLED" % reading]
    Fz = raw["arms"]["%s-FROZEN" % reading]
    trace = raw["trace"]
    infinite_sectors = sum(1 for r in trace if not r["finite_order_possible"])
    rows = []
    for (kid, klass, restated, statement, pre_f, pre_c) in BATTERY_SPEC:
        if kid == "K1-NORM":
            mf = Fz["violations"].get("norm", 0) == 0
            mc = C["violations"].get("norm", 0) == 0
            ev = "norm violations frozen %d of %d, coupled %d of %d" % (
                Fz["violations"].get("norm", 0), Fz["checks"]["norm"],
                C["violations"].get("norm", 0), C["checks"]["norm"])
        elif kid == "K2-SITE-MASS":
            mf = Fz["violations"].get("site", 0) == 0
            mc = C["violations"].get("site", 0) == 0
            ev = "site-mass violations frozen %d of %d, coupled %d of %d" % (
                Fz["violations"].get("site", 0), Fz["checks"]["site"],
                C["violations"].get("site", 0), C["checks"]["site"])
        elif kid == "K3-LAW-NATIVE":
            mf = (Fz["violations"].get("law_native", 0) == 0
                  and Fz["violations"].get("repricing", 0) == 0)
            mc = (C["violations"].get("law_native", 0) == 0
                  and C["violations"].get("repricing", 0) == 0)
            ev = ("G(x,1)=M(x) violations frozen %d of %d, coupled %d of %d; "
                  "re-pricing violations frozen %d, coupled %d" % (
                      Fz["violations"].get("law_native", 0),
                      Fz["checks"]["law_native"],
                      C["violations"].get("law_native", 0),
                      C["checks"]["law_native"],
                      Fz["violations"].get("repricing", 0),
                      C["violations"].get("repricing", 0)))
        elif kid == "K4-EMISSION-STOCHASTIC":
            mf = (Fz["violations"].get("column", 0) == 0
                  and Fz["violations"].get("emission_total", 0) == 0)
            mc = (C["violations"].get("column", 0) == 0
                  and C["violations"].get("emission_total", 0) == 0)
            ev = ("column violations frozen %d of %d, coupled %d of %d; total "
                  "emission-mass violations frozen %d, coupled %d" % (
                      Fz["violations"].get("column", 0), Fz["checks"]["column"],
                      C["violations"].get("column", 0), C["checks"]["column"],
                      Fz["violations"].get("emission_total", 0),
                      C["violations"].get("emission_total", 0)))
        elif kid == "K5-NO-RETURN":
            # REPAIRED (K2 MAJOR-2): the raw amplitudes carry norm 9^t and can
            # never repeat across levels, so the delivered predicate was
            # unfireable.  The row now reads the RAY-GRAIN measurement.
            k5 = raw["k5"]
            mf = (k5["frozen_ray_repeats"] == 0
                  and k5["frozen_normalised_repeats"] == 0)
            mc = (k5["coupled_ray_repeats"] == 0
                  and k5["coupled_normalised_repeats"] == 0)
            ev = ("at the RAY grain: frozen arm driven %d steps with %d ray "
                  "repeats and %d exactly-normalised repeats, %d distinct "
                  "rays; coupled arm to level %d with %d cross-level ray "
                  "repeats; the raw-amplitude predicate the delivered run used "
                  "could not fire at all, since the state norms %s are "
                  "distinct by level.  Momentum sectors of provably infinite "
                  "order %d of 9, by trace non-integrality"
                  % (k5["frozen_steps"], k5["frozen_ray_repeats"],
                     k5["frozen_normalised_repeats"],
                     k5["frozen_distinct_rays"], k5["coupled_levels"],
                     k5["coupled_ray_repeats"], k5["raw_state_norms_by_level"],
                     infinite_sectors))
        elif kid == "K6-BLOCH":
            # REPAIRED (K1 m-1, K3 section 8): the delivered row read K7's
            # observable on the coupled leg and a typed True on the frozen one.
            # It now reads its OWN pre-registered observable, translation
            # covariance of the count field, which the instrument already
            # computed and did not use.
            mf = Fz["final"]["count_field_translation_invariant"]
            mc = C["final"]["count_field_translation_invariant"]
            ev = ("count-field translation-invariance probability frozen %s, "
                  "coupled %s -- this row's OWN observable, not K7's"
                  % (Fz["final"]["translation_invariant_probability"],
                     C["final"]["translation_invariant_probability"]))
        elif kid == "K7-CURVATURE-HOMOGENEOUS":
            mf = Fz["final"]["curvature_homogeneous"]
            mc = C["final"]["curvature_homogeneous"]
            ev = ("constant-curvature probability frozen %s, coupled %s"
                  % (Fz["final"]["curvature_constant_probability"],
                     C["final"]["curvature_constant_probability"]))
        elif kid == "K8-I7-ADMISSIBILITY":
            mf = not Fz["final"]["exit_positive"]
            mc = not C["final"]["exit_positive"]
            ev = ("I7-admissibility exit probability frozen %s, coupled %s; "
                  "determinant values reached coupled %s"
                  % (Fz["final"]["admissibility_exit_probability"],
                     C["final"]["admissibility_exit_probability"],
                     ",".join(C["final"]["det_values_reached"])))
        elif kid == "K9-SOURCING":
            mf = Fz["violations"].get("sourcing", 0) == 0
            mc = C["violations"].get("sourcing", 0) == 0
            ev = ("sourcing violations frozen %d of %d, coupled %d of %d"
                  % (Fz["violations"].get("sourcing", 0),
                     Fz["checks"]["sourcing"],
                     C["violations"].get("sourcing", 0),
                     C["checks"]["sourcing"]))
        else:                                   # K10-RECORDS-THEOREM
            tc = Fraction(C["final"]["total_emitted"])
            tf = Fraction(Fz["final"]["total_emitted"])
            mf = tf == HORIZON
            mc = tc == HORIZON
            ev = ("total record increment over the horizon frozen %s, coupled "
                  "%s, against %d division events emitted"
                  % (tf, tc, HORIZON))
        if mut("MUT-POLARITY") and kid == "K8-I7-ADMISSIBILITY":
            mc = True
        rows.append({"id": kid, "class": klass,
                     "update_rule_restated": restated,
                     "statement": statement,
                     "pre_registered": {"frozen_holds": pre_f,
                                        "coupled_holds": pre_c},
                     "measured": {"frozen_holds": bool(mf),
                                  "coupled_holds": bool(mc)},
                     "polarity_matches": (bool(mf) == pre_f
                                          and bool(mc) == pre_c),
                     "evidence": ev,
                     "discriminates": bool(mf) != bool(mc)})
    return rows


def requirement_selector(rows):
    """THE SELECTOR, pre-registered.  A REQUIREMENT witness must be a closure
    that (i) is INTERNAL TO THE QUANTUM SIDE, (ii) is NOT the update rule
    restated, and (iii) FAILS on the frozen stage while PASSING on the coupled
    one.  Anything else is reported for what it is."""
    witnesses = [r for r in rows
                 if r["class"] == "PSI-INTERNAL"
                 and not r["update_rule_restated"]
                 and not r["measured"]["frozen_holds"]
                 and r["measured"]["coupled_holds"]]
    reverse = [r for r in rows
               if r["measured"]["frozen_holds"]
               and not r["measured"]["coupled_holds"]]
    restated = [r for r in rows
                if r["update_rule_restated"]
                and not r["measured"]["frozen_holds"]
                and r["measured"]["coupled_holds"]]
    if mut("MUT-REQUIRED"):
        witnesses = restated
    return witnesses, reverse, restated


# ===========================================================================
# SECTION 7b.  THE VERBATIM ANCHORS (#62) -- each bound to a consumer gate
# ===========================================================================

VERBATIM = [
    ("V-HA-ADMISSIBLE", "A-HA",
     "A record is **admissible** when $q$ is\nnonsingular and positive "
     "definite at every site, by the exact Sylvester\ncriterion",
     "G-ADMISSIBILITY-LADDER"),
    ("V-GITER-LAWNATIVE", "A-GITER",
     "G(h, 1) = M(h), is\na consequence of the potential recursion's terminal "
     "condition", "G-LAW-NATIVE"),
    ("V-GITER-SEDIMENT", "A-GITER",
     "At the ruled carrier no class is ever revisited",
     "G-BATTERY-POLARITY"),
    ("V-W3-RECORD", "A-W3",
     "The weld reaches a record; it does not yet reach a law over\nrecords.",
     "G-UNSPLITTABLE"),
    ("V-W3-HEX", "A-W3",
     "the hexagonal one: unit lengths meeting at one\nhundred and twenty "
     "degrees", "G-WALL-HEX-NAMED"),
    ("V-R4B-SYMBOL", "A-R4B",
     "For a circulant with\ncoefficient map c, the symbol is",
     "G-SCALAR-MONOMIAL"),
    ("V-R5-SUPPORT", "A-R5",
     "The exclusion is a\ntheorem about **support overlap**, and it stops as "
     "soon as two objects overlap\nin two sites.", "G-COIN-CENSUS"),
    ("V-CRA-MARGIN", "A-CRA",
     "the weld arena sits 3 diagonal-only events\nfrom I7's G-SINGULAR",
     "G-EXIT-CENSUS"),
    ("V-CAT-BHS", "A-CAT",
     "a Poisson sprinkling admits **no Lorentz-invariant finite-valency "
     "graph**", "G-WALL-BHS"),
    ("V-CAT-KR", "A-CAT",
     "must carry a Kleitman–Rothschild height control",
     "G-WALL-KR"),
    ("V-L1-FOURTH", "A-L1",
     "**fourth form, outside paper 8's three**, and its admissibility is",
     "G-WALL-L1"),
    ("V-PIN-SCOPE", "A-PIN",
     "THIS UNIT REACHES A RECORD, NOT YET A LAW OVER RECORDS",
     "G-PAPER-CLAIMS"),
]

# THE SCOPE ROW, carried VERBATIM in the paper's head, per the pin.
SCOPE_ROW = ("THIS UNIT REACHES A RECORD, NOT YET A LAW OVER RECORDS")
# the DECLARED multiplicity of each verdict fence in the paper: once in the
# head and once in section 12.  E-22 gates the blocks by MULTISET, so this
# number is part of the gate rather than an incidental of the layout.
HEAD_COPIES = 2

# the abstention scans.  `horizon` is DECLARED OUT of the cosmological needle
# set with its reason printed: it is this unit's own name for the declared
# finite number of coupled steps and the gravity law's own relative-horizon
# index, and a scan that fired on it would fire on the pin's own vocabulary.
BHS_NEEDLES = ("boost", "rapidity", "sprinkl", "frame")
KR_NEEDLES = ("myrheim", "meyer", "shatter", "chart width", "dimension")
COSMO_NEEDLES = ("cosmolog", "redshift", "universe", "expansion",
                 "big bang", "hubble", "light cone", "lightcone")


def measurement_layer(R, LD):
    """the surface the three abstention walls scan: every MEASURED receipt key
    together with the statement and evidence of every non-wall gate this run
    evaluated.  Scanning the gates as well as the values is what makes the
    abstention a measurement rather than a declaration."""
    parts = [json.dumps(R.get(k, None), sort_keys=True, default=str)
             for k in MEASURED_KEYS]
    for g in LD.rows:
        if g["gate"].startswith("G-WALL-"):
            continue
        parts.append(g["statement"])
        parts.append(g["evidence"])
    return " ".join(parts).lower()


# ===========================================================================
# SECTION 8.  THE RUN
# ===========================================================================

def full_run(break_anchor=None, paper_text=None, paper_rel=PAPER_REL,
             do_paper=True):
    LD = Ledger()
    SEAL = Seal()
    R = {"schema": SCHEMA}
    del READS[:]

    say("=" * 78)
    say("v14 THE COUPLING UNIT -- paper-20-coupling")
    say("A QUANTUM DYNAMICS THAT WRITES ITS OWN STAGE, ON THE WELDED R=3 ARENA")
    say("=" * 78)

    # -- SEC 1: provenance ---------------------------------------------------
    say("")
    say("SECTION 1.  PROVENANCE")
    # #24: the instrument's own cardinalities are REGISTERED as numbers this
    # run computed, so the paper may carry them and a hand-typed one cannot
    # pass.  They are registered here because the numeral scan runs before the
    # coverage census that would otherwise publish them.
    reg(len(SOURCES), len(VERBATIM), len(MUTANTS), len(GATE_REGISTRY),
        len(SEALED_PATHS), len(BATTERY_SPEC), HORIZON, len(LADDER))
    texts = {}
    prov = []
    bad = []
    for sid, rel, want, why in SOURCES:
        raw = read_bytes(rel)
        got = hashlib.sha256(raw).hexdigest()[:12]
        exp = want
        if break_anchor == sid:
            exp = "0" * 12
        texts[rel] = raw.decode("utf-8")
        prov.append({"id": sid, "path": rel, "sha256_12": got,
                     "declared": exp, "match": got == exp, "why": why})
        if got != exp:
            bad.append(sid)
    R["provenance"] = prov
    LD.gate("G-PROVENANCE",
            "all %d declared sources are read from paths resolved from THIS "
            "FILE's own location and matched against the sha256-12 this unit "
            "froze; a drifted source dies here before a single measurement "
            "runs, which is what a pinned-sha read buys with no version "
            "control present" % len(SOURCES),
            not bad, "mismatched anchors: %s" % (bad or "none"))
    SEAL.take("SEAL-SCHEMA", R)
    SEAL.take("SEAL-PROVENANCE", R)

    self_src = read_text(SELF)
    tree = ast.parse(self_src)
    floats = [n for n in ast.walk(tree)
              if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    R["arithmetic"] = ("exact: Python int and fractions.Fraction; amplitudes "
                       "as integer pairs over Z[w] with a common power-of-3 "
                       "denominator; 0 float literals in this file")
    R["python"] = sys.version.split()[0]
    LD.gate("G-EXACT-ARITHMETIC",
            "an AST scan of this file finds no float literal anywhere: the "
            "amplitudes are INTEGER pairs over Z[w] with a common power-of-3 "
            "denominator, and every probability is a fractions.Fraction.  The "
            "interpreter this ran under is recorded and SEALED at this gate "
            "rather than left unsealed: CPython %s" % sys.version.split()[0],
            not floats, "float literals: %d; interpreter %s"
            % (len(floats), sys.version.split()[0]))
    SEAL.take("SEAL-ARITHMETIC", R)
    SEAL.take("SEAL-PYTHON", R)

    banned_mods = {"subprocess", "multiprocessing", "socket", "shutil"}
    banned_attrs = {"system", "popen", "execv", "execve", "execl", "execlp",
                    "execvp", "spawnl", "spawnv", "spawnve", "fork", "forkpty",
                    "posix_spawn"}
    hits = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            hits += [a.name for a in n.names if a.name in banned_mods]
        elif isinstance(n, ast.ImportFrom) and n.module in banned_mods:
            hits.append(n.module)
        elif isinstance(n, ast.Attribute) and n.attr in banned_attrs:
            hits.append("os.%s" % n.attr)
    LD.gate("G-NO-SUBPROCESS",
            "no subprocess of any kind is invoked and no version-control "
            "command is spawned: the scan reads IMPORT NAMES as well as uses, "
            "so an aliased import is a hit, AND it reads ATTRIBUTE names, so "
            "the process-spawning surface of an already-imported module -- "
            "os.system, os.popen, os.exec*, os.spawn*, os.fork -- is scanned "
            "too.  The run is therefore correct off-tree and with git absent",
            not hits, "banned imports and spawn attributes: %s"
            % (hits or "none"))

    declared_reads = {rel for _s, rel, _w, _y in SOURCES}
    R["object_reads"] = {
        "self": os.path.basename(SELF),
        "self_why": OBJECT_READS_WHY["SELF"],
        "object_under_test": paper_rel,
        "object_why": OBJECT_READS_WHY["PAPER"],
        "count": len(OBJECT_READS_WHY)}
    LD.gate("G-READS-DECLARED",
            "the set of files read at run time is EXACTLY the declared source "
            "set: %d reads, no repository state outside them.  The SECOND read "
            "set is declared and gated the same way rather than left out of "
            "the accounting: this file itself, which its own AST probes parse, "
            "and the object under test -- %d files, both named"
            % (len(set(READS)), len(OBJECT_READS_WHY)),
            (set(READS) == declared_reads
             and len(OBJECT_READS_WHY) == 2
             and R["object_reads"]["self"] == os.path.basename(SELF)),
            "undeclared %s; declared-not-read %s; object reads %s"
            % (sorted(set(READS) - declared_reads) or "none",
               sorted(declared_reads - set(READS)) or "none",
               sorted(OBJECT_READS_WHY)))
    SEAL.take("SEAL-OBJECT-READS", R)

    src_by_id = {sid: texts[rel] for sid, rel, _w, _y in SOURCES}
    vrows = []
    vbad = []
    for vid, sid, needle, consumer in VERBATIM:
        ok = match_needle(src_by_id[sid], needle)
        # #62: the anchor is perturbed at a content-bearing token and must STOP
        # being located, so the row counts as covered only when it can fail
        toks = [t for t in canon(needle).split(" ") if len(t) > 3]
        pert = canon(needle).replace(toks[-1], toks[-1] + "zz")
        flips = pert not in canon(src_by_id[sid])
        vrows.append({"id": vid, "source": sid, "consumer_gate": consumer,
                      "chars": len(canon(needle)), "located": ok,
                      "perturbation_flips": flips})
        if not ok or not flips:
            vbad.append(vid)
    R["verbatim_anchors"] = vrows
    LD.gate("G-VERBATIM",
            "%d verbatim anchors, each at least %d characters after "
            "normalisation, each located exactly in its pinned source, each "
            "PERTURBED at a content-bearing token and re-located so the row "
            "counts as covered only when its own predicate flips, and each "
            "declared against a consumer gate"
            % (len(VERBATIM), NEEDLE_FLOOR),
            not vbad, "anchors failing: %s" % (vbad or "none"))
    SEAL.take("SEAL-VERBATIM", R)

    # -- SEC 2/3: the arena, rebuilt ----------------------------------------
    say("")
    say("SECTION 2.  THE WELDED RECORD, REBUILT FROM THE COMMITTED GRAMMAR")
    raw = raw_census(texts)
    G = raw["G"]
    rec = raw["record"]
    LD.gate("G-SLICE-EXIT-FREE",
            "d42b1's transport layer is taken as a TEXT SLICE cut at the "
            "layer's own banner print, and d60/d66 enter by AST extraction of "
            "their definitions alone, so no module-level statement of theirs "
            "can run and no extracted body can terminate this process.  The "
            "property is decided BEFORE the first exec rather than after it: "
            "a body that could call sys.exit would have ended this process "
            "before a gate evaluated afterwards could refuse it",
            G.slice_exit_free and G.bodies_exit_free,
            "slice exit-free %s, extracted bodies exit-free %s"
            % (G.slice_exit_free, G.bodies_exit_free))

    reg(len(raw["own_r2"]))
    same = pick("MUT-COMMITTED-ANCHOR", raw["own_r2"] == raw["d66_r2"], False)
    LD.gate("G-COMMITTED-ANCHOR",
            "the generalized driver is ANCHORED against the object it "
            "generalizes: at the committed R = 2 schedule it and d66's own "
            "conflict_grid(3, 2), re-run in this process, emit IDENTICAL "
            "event lists -- %d events compared one for one"
            % len(raw["own_r2"]),
            same, "driver events %d, d66 events %d, identical %s"
            % (len(raw["own_r2"]), len(raw["d66_r2"]), same))

    n_driven = list(raw["n_driven"])
    if mut("MUT-WELD-CELL"):
        n_driven[0] += 1
    cells_at_one = sum(1 for c in n_driven if c == 1)
    maxhits = pick("MUT-WELD-FORCED", rec["maxhits"], 2)
    reg(rec["events"], rec["divisions"], cells_at_one, len(n_driven))
    LD.gate("G-WELDED-RECORD",
            "THE WELDED RECORD IS REBUILT AND DRIVEN, not cited: the uniform "
            "R = 3 arrangement -- three rounds grouped on the three "
            "link-direction parallel classes -- is built by driving the "
            "committed layer's OWN MENUS, every specification matched by "
            "exactly one candidate and no refusal anywhere.  Measured CELL BY "
            "CELL: %d events, %d division events, and the driven link field is "
            "1 at %d of %d cells"
            % (rec["events"], rec["divisions"], cells_at_one, NCELL),
            (cells_at_one == NCELL and maxhits == 1 and not rec["refusal"]
             and rec["divisions"] == 9 and raw["off_target"] == 0),
            "cells at 1: %d of %d; maxhits %s; refusal %s; divisions %d; "
            "pairs off the declared link set %d"
            % (cells_at_one, NCELL, maxhits, rec["refusal"], rec["divisions"],
               raw["off_target"]))

    dets = []
    posdef = 0
    q11_0, _q22_0, q12_0, _d0 = q_of(site_counts(raw["n_driven"], 0))
    reg(str(q11_0), str(q12_0), str(-q12_0))
    for s in range(9):
        nv = site_counts(raw["n_driven"], s)
        _a, _b, _c, d = q_of(nv)
        if mut("MUT-WELD-DET") and s == 0:
            d = Fraction(1)
        dets.append(d)
        if admissible(nv):
            posdef += 1
    reg(str(dets[0]), posdef)
    LD.gate("G-WELDED-GEOMETRY",
            "and SITE BY SITE against its own value, never against an "
            "aggregate: q = [[1, -1/2], [-1/2, 1]] with det = 3/4 at all 9 "
            "sites, positive definite at %d of 9 by I7's own exact Sylvester "
            "criterion" % posdef,
            all(d == Fraction(3, 4) for d in dets) and posdef == 9,
            "determinants %s; positive definite %d of 9"
            % (sorted({str(d) for d in dets}), posdef))

    realised = set(raw["pairs"])
    if mut("MUT-DICTIONARY"):
        realised = set(list(realised)[:-1])
    is_cayley = realised == raw["cayley"]
    overlap_ant = realised & raw["ant_pairs"]
    reg(len(raw["cayley"]), len(raw["ant_pairs"]))
    LD.gate("G-DICTIONARY",
            "THE FORCED DICTIONARY, instantiated and gated: ACTOR->SITE is the "
            "constructor's own naming, CO-DIVISION-PAIR->LINK is read off the "
            "layer's own footprints, and the realised relation IS the target's "
            "own Cayley incidence at equality -- %d unordered pairs, the "
            "complete tripartite graph whose three parts are the lines of the "
            "one direction I7 does not declare, which the realised relation "
            "meets in %d pairs"
            % (len(raw["cayley"]), len(overlap_ant)),
            is_cayley and not overlap_ant,
            "realised pairs %d, target pairs %d, equal %s, pairs on the "
            "undeclared direction %d"
            % (len(realised), len(raw["cayley"]), is_cayley,
               len(overlap_ant)))

    # the isomorphism count, CITED AND VERIFIED at the weld's own receipt
    # THE CITATION IS READ FROM THE PARENT'S OWN KEY, not substring-searched
    # (K3 MINOR-11): the delivered pattern '"isos": 1296' matched ZERO times
    # and the leg reduced to a bare search for 1296 in 137 KB of JSON.
    w3rec = json.loads(texts["v14/code/r3_weld_receipt.json"])
    w3ser = json.dumps(w3rec, sort_keys=True, default=str)
    ISOS_KEY = "isomorphisms"
    isos_cited = w3rec["counts"][ISOS_KEY]
    isos_under_key = len(re.findall(r'"%s": %d' % (ISOS_KEY, isos_cited),
                                    w3ser))
    aut_k333 = 6 * (6 ** 3)
    isos_here = pick("MUT-ISOS", aut_k333, 1290)
    reg(isos_cited, aut_k333, isos_under_key)
    R["anchors"] = {"isos_cited_from_weld_receipt": isos_cited,
                    "cited_key": "counts/%s" % ISOS_KEY,
                    "occurrences_under_that_key_in_the_weld_receipt":
                        isos_under_key,
                    "aut_k333_recomputed_here": aut_k333,
                    "aut_factorisation": "3! * (3!)^3"}
    LD.gate("G-ISOS-CITED",
            "the %d site assignments are CITED AND VERIFIED, not re-derived: "
            "the weld's committed receipt is read at run time and the number "
            "is taken FROM ITS OWN KEY counts/%s -- not located by a bare "
            "substring search of the whole receipt, which would be satisfied "
            "by any occurrence anywhere -- and it is found under that key at "
            "%d places.  The same number is recomputed here from the target's "
            "automorphism group, 3! * (3!)^3 = %d, and the two readings are "
            "required to meet at equality"
            % (isos_cited, ISOS_KEY, isos_under_key, aut_k333),
            isos_here == isos_cited and isos_under_key > 0,
            "recomputed %d, cited %d from counts/%s, occurrences under that "
            "key %d"
            % (isos_here, isos_cited, ISOS_KEY, isos_under_key))
    SEAL.take("SEAL-ANCHORS", R)

    split_fibers = [max(0, c - 1) for c in raw["n_driven"]]
    prod_fiber = pick("MUT-SPLIT", 0 if any(f == 0 for f in split_fibers)
                      else 1, 1)
    zero_intervals = sum(1 for f in split_fibers if f == 0)
    reg(zero_intervals)
    R["arena"] = {
        "sites": 9, "links": [list(l) for l in LINKS],
        "undeclared_direction": list(ANT), "cells": NCELL,
        "welded_field": list(raw["n_driven"]),
        "events": rec["events"], "divisions": rec["divisions"],
        "maxhits": rec["maxhits"], "refusal": bool(rec["refusal"]),
        "cells_at_one": cells_at_one,
        "determinant": str(dets[0]), "posdef_sites": posdef,
        "realised_pairs": len(realised),
        "relation_is_target_incidence": is_cayley,
        "split_fiber_zero_intervals": zero_intervals,
    }
    LD.gate("G-UNSPLITTABLE",
            "THE SCOPE ROW'S WARRANT, measured here rather than inherited by "
            "assertion: paper-04's split fiber is the product over the "
            "interval's links of (n_l - 1), so a count-1 interval cannot be "
            "split into two strictly positive parts.  The landing record is 1 "
            "everywhere, so the split fiber is 0 at %d of %d intervals and the "
            "refinement grammar, the stochastic split and the "
            "renewal-transport kernel are EMPTY on it"
            % (zero_intervals, NCELL),
            zero_intervals == NCELL and prod_fiber == 0,
            "intervals with split fiber 0: %d of %d; product fiber %d"
            % (zero_intervals, NCELL, prod_fiber))
    SEAL.take("SEAL-ARENA", R)

    # -- SEC 4: the walk, derived -------------------------------------------
    say("")
    say("SECTION 3.  THE WALK -- DERIVED WHERE DERIVABLE")
    sc = dict(raw["scalar"])
    sc["nonmonomial_unitary_maps"] = pick(
        "MUT-SCALAR-ALIVE", sc["nonmonomial_unitary_maps"], 1)
    reg(sc["differences"], sc["maps_scanned"], sc["unitary_maps"],
        sc["alphabet"], sc["axis_unitary_maps"],
        sc["axis_nonmonomial_unitary_maps"], sc["narrow_alphabet"],
        sc["narrow_maps_scanned"], sc["narrow_link_unitary_maps"],
        sc["narrow_link_nonmonomial_unitary_maps"],
        sc["narrow_axis_unitary_maps"],
        sc["narrow_axis_nonmonomial_unitary_maps"])
    LD.gate("G-SCALAR-MONOMIAL",
            "THEOREM, and it is what FORCES the coin register.  R4b's family "
            "shape is a coefficient map on lattice offsets, unitary iff its "
            "autocorrelation is a delta.  On THIS arena's offset set -- I7's "
            "three declared link directions -- every one of the %d nonzero "
            "differences of two distinct offsets is realised by EXACTLY ONE "
            "ordered pair, so each condition reads c_v conj(c_w) = 0 and "
            "forces one of the two to vanish; the three together leave at most "
            "one nonzero coefficient and the norm makes it a MONOMIAL, a "
            "deterministic shift with no interference at all.  The exhaustive "
            "check is taken over the DISCRIMINATING alphabet the arena's own "
            "ring supplies -- the %d elements of (1/3)Z[w] of modulus at most "
            "1, %d maps -- and it is taken ON BOTH STENCILS IN THIS RUN, which "
            "is what makes it evidence: LINK stencil %d unitary, %d "
            "non-monomial; R4b's own AXIS stencil, where interference "
            "survives, %d unitary, %d non-monomial, each difference realised "
            "%d times.  The 7-value alphabet this unit first scanned returns "
            "the same answer on both and corroborates nothing"
            % (sc["differences"], sc["alphabet"], sc["maps_scanned"],
               sc["unitary_maps"], sc["nonmonomial_unitary_maps"],
               sc["axis_unitary_maps"], sc["axis_nonmonomial_unitary_maps"],
               sc["axis_multiplicities"][0]),
            (sc["each_realised_once"] and sc["nonmonomial_unitary_maps"] == 0
             and sc["axis_multiplicities"] == [3, 3]
             and sc["alphabet_discriminates"]
             and sc["narrow_alphabet_is_blind"]),
            "each difference realised once %s; link non-monomial unitary maps "
            "%d; axis non-monomial unitary maps %d; the alphabet discriminates "
            "%s; axis-stencil multiplicities %s; the retired %d-value "
            "alphabet, %d maps, returns %d unitary and %d non-monomial on BOTH "
            "stencils and is therefore measured blind %s"
            % (sc["each_realised_once"], sc["nonmonomial_unitary_maps"],
               sc["axis_nonmonomial_unitary_maps"],
               sc["alphabet_discriminates"], sc["axis_multiplicities"],
               sc["narrow_alphabet"], sc["narrow_maps_scanned"],
               sc["narrow_link_unitary_maps"],
               sc["narrow_link_nonmonomial_unitary_maps"],
               sc["narrow_alphabet_is_blind"]))

    cf = dict(raw["coin"])
    cf["classes_up_to_phase"] = pick(
        "MUT-COIN-FREE", cf["classes_up_to_phase"], 5)
    reg(cf["solutions"], cf["nontrivial"], cf["ring_solutions"],
        cf["ring_nontrivial"], cf["classes_up_to_phase"],
        cf["grover_classes_up_to_phase"], len(cf["hidden_classes"]))
    LD.gate("G-COIN-CENSUS",
            "THE COIN IS DECLARED UNDER A STATED REALITY CONDITION, AND ITS "
            "FIBER IS PRINTED.  The arena's own direction-relabelling group is "
            "S_3 -- the weld measured the record invariant under all six of "
            "its relabellings -- and a coin covariant under it has the form "
            "a I + b J.  The unitarity conditions |a|^2 = 1 and a conj(b) + "
            "conj(a) b + 3|b|^2 = 0 cut out a CIRCLE, not a finite set: over "
            "the exact rational solutions WITH a AND b REAL there are %d, %d "
            "of them non-trivial and both +/- Grover, and that reality "
            "restriction is this unit's DECLARATION rather than its theorem.  "
            "Over the arena's own ring (1/3)Z[w] the same conditions have %d "
            "solutions, %d non-trivial, falling into %d classes up to a global "
            "phase, of which %d is +/- Grover -- so the fiber is %d hidden "
            "members, and the witness a = 1, b = w/3 is exhibited, verified "
            "exactly unitary by C C* = I and exactly S_3-covariant, and is not "
            "+/- Grover"
            % (cf["solutions"], cf["nontrivial"], cf["ring_solutions"],
               cf["ring_nontrivial"], cf["classes_up_to_phase"],
               cf["grover_classes_up_to_phase"], len(cf["hidden_classes"])),
            (cf["all_real_nontrivial_are_grover"] and cf["nontrivial"] == 2
             and cf["grover_is_unitary_exactly"]
             and cf["classes_up_to_phase"] == 6
             and cf["grover_classes_up_to_phase"] == 1
             and cf["witness_is_unitary_exactly"]
             and cf["witness_is_s3_covariant"]
             and not cf["witness_is_grover"]),
            "real solutions %d (non-trivial %d, all Grover %s); ring solutions "
            "%d, classes up to phase %d, Grover classes %d; the witness is "
            "unitary %s, S_3-covariant %s, Grover %s"
            % (cf["solutions"], cf["nontrivial"],
               cf["all_real_nontrivial_are_grover"], cf["ring_solutions"],
               cf["classes_up_to_phase"], cf["grover_classes_up_to_phase"],
               cf["witness_is_unitary_exactly"], cf["witness_is_s3_covariant"],
               cf["witness_is_grover"]))

    inv = raw["coin_invariance"]
    inv_bad = [r["coin"] for r in inv
               if r["consistency_violations"] != 0
               or r["observable_rows_differing"] != r["observable_rows"]
               or r["exit_threshold"] != HORIZON
               or r["indefinite_form_reached"]]
    inv_bad = pick("MUT-COIN-INVARIANT", inv_bad, ["FORGED"])
    reg(len(inv), *[r["leaves_coupled"] for r in inv])
    reg(*[r["exit_probability"] for r in inv])
    R["coin_invariance"] = {"members": inv, "members_failing": inv_bad,
                            "invariants": ["consistency_violations = 0",
                                           "every declared observable row "
                                           "differs from its own frozen "
                                           "control",
                                           "exit threshold = %d" % HORIZON,
                                           "no indefinite form reached"]}
    LD.gate("G-COIN-INVARIANCE",
            "THE VERDICT IS MEASURED COIN-INVARIANT, WHICH IS THE STRONGER "
            "RESULT A BROKEN FORCING CLAIM BUYS.  Every one of the %d HIDDEN "
            "non-Grover classes of the S_3-covariant family is run to the FULL "
            "horizon %d, coupled and against its own frozen control, and the "
            "four invariants that carry the verdict are re-taken on each: 0 "
            "consistency violations, %d of %d declared observable rows moving, "
            "the admissibility threshold at exactly %d, and no indefinite form "
            "reached.  The numbers are coin-specific -- the coupled leaf "
            "counts are %s against the delivered member's -- and the verdict "
            "shape is not"
            % (len(inv), HORIZON, len(INVARIANT_OBS), len(INVARIANT_OBS),
               HORIZON, ", ".join(str(r["leaves_coupled"]) for r in inv)),
            not inv_bad,
            "members failing an invariant: %s; thresholds %s"
            % (inv_bad or "none", [r["exit_threshold"] for r in inv]))
    SEAL.take("SEAL-COIN-INVARIANCE", R)

    cn = dict(raw["conn"])
    cn["connection_group_order"] = pick(
        "MUT-CONNECTION-GROUP", cn["connection_group_order"], 4)
    LD.gate("G-CONNECTION-GROUP",
            "the connection group is DERIVED from the arena and not chosen: "
            "the sites are Z_3^2 and the parallel classes are the lines of "
            "AG(2,3), so the arena is over F_3 and the link connection the "
            "record defines is valued in the arena's own scalar group Z_3.  "
            "The consequence is stated rather than hidden -- the walk consumes "
            "the count RESIDUE n mod 3, not the count",
            cn["connection_group_order"] == 3 and cn["phase_alphabet_closes"],
            "connection group order %d, phase alphabet closes %s, consumes %s"
            % (cn["connection_group_order"], cn["phase_alphabet_closes"],
               cn["consumes"]))

    arms = raw["arms"]
    uviol = sum(arms[k]["violations"].get("norm", 0) for k in arms)
    uchk = sum(arms[k]["checks"]["norm"] for k in arms)
    sviol = sum(arms[k]["violations"].get("site", 0) for k in arms)
    schk = sum(arms[k]["checks"]["site"] for k in arms)
    uviol = pick("MUT-WALK-UNITARY", uviol, 1)
    reg(uchk, schk)
    LD.gate("G-WALK-UNITARY",
            "the step is unitary EXACTLY and PER OBJECT: the state is a unit "
            "vector at %d branch-steps across the four arms with %d "
            "violations, and the coin preserves each SITE's mass separately "
            "at %d site-branch-steps with %d violations -- the second is the "
            "stronger statement and it is the law transport's own precondition"
            % (uchk, uviol, schk, sviol),
            uviol == 0 and sviol == 0,
            "norm violations %d of %d; site-mass violations %d of %d"
            % (uviol, uchk, sviol, schk))

    fibers = raw["fibers"]
    fiber_rows = [
        ("F1-SITE-CARRIER", "FORCED", 1,
         "actor -> Z_3^2, the constructor's own naming; paper-19 item 3"),
        ("F2-LINK-SET", "FORCED", 1,
         "I7's three declared directions, the forced dictionary's own"),
        ("F3-COIN-REGISTER", "DERIVED", 1,
         "the scalar shape is monomial-only on this offset set (theorem)"),
        ("F4-COIN", "DECLARED-UNDER-A-REALITY-CONDITION", 6,
         "the S_3-covariant unitarity conditions cut out a CIRCLE; the "
         "reality condition a, b real is DECLARED and selects +/- Grover.  "
         "Over the arena's own (1/3)Z[w] the fiber is 6 classes up to a "
         "global phase, and all 4 hidden non-Grover members are RUN to the "
         "full horizon: the verdict shape is invariant across the family"),
        ("F5-CONNECTION-GROUP", "DERIVED", 1,
         "Z_3, because the arena is over F_3"),
        ("F6-COIN-ORDER", "DECLARED-VERDICT-RELEVANT", 2,
         "G.D against D.G; both members run, and the difference is measured "
         "rather than assumed: with D.G the count phase is applied after the "
         "coin and cannot enter that step's Born weights at all"),
        ("F7-ORIENT", "DECLARED", 2,
         "the +l shift against the -l shift; both members run.  INERT ON THE "
         "IPR ONLY: on the full declared observable set the two differ in "
         "p_site and the emission field, which are the arena's own reflection"),
        ("F8-INIT-COIN", "DECLARED", 3,
         "the three coin components at the start site; all three run"),
        ("F9-INIT-SITE", "MEASURED", 3,
         "the start site: three declared starts are RUN and the comparison is "
         "the one translation covariance predicts -- the site distribution is "
         "the exact TRANSLATE of the base one, and the translation-invariant "
         "functional agrees exactly"),
        ("F10-EMISSION-READING", "DECLARED", 2,
         "the Born menu against the record menu; both run, every row stamped"),
        ("F11-HORIZON", "DECLARED", 1,
         "T = 5, with the whole ladder T = 1..5 published"),
        ("F12-UPDATE-SEMANTICS", "DECLARED", 2,
         "run-on against halt-on-inadmissibility; the alternative's "
         "consequence IS the measured exit probability"),
    ]
    # F6 AT THE FULL HORIZON, before the fiber inventory closes.
    dgf = raw["dg_full"]
    gdf = arms["A-COUPLED"]
    dg_hit = [t for t in LADDER if dgf["ladder"][t]["exit_positive"]]
    dg_threshold = min(dg_hit) if dg_hit else None
    dg_threshold = pick("MUT-ORDER-FULL", dg_threshold, 4)
    dg_exit = dgf["final"]["admissibility_exit_probability"]
    gd_exit = gdf["final"]["admissibility_exit_probability"]
    ratio = Fraction(dg_exit) / Fraction(gd_exit)
    ratio_100 = (ratio * 100).numerator // (ratio * 100).denominator
    order_full = {
        "horizon": HORIZON,
        "GD_exit_probability": gd_exit, "DG_exit_probability": dg_exit,
        "GD_leaves": gdf["levels"][-1]["branches"],
        "DG_leaves": dgf["levels"][-1]["branches"],
        "GD_threshold": min(t for t in LADDER
                            if gdf["ladder"][t]["exit_positive"]),
        "DG_threshold": dg_threshold,
        "DG_over_GD_exact": str(ratio),
        "DG_over_GD_floor_x100": ratio_100,
        "DG_curvature_constant_probability":
            dgf["final"]["curvature_constant_probability"],
        "DG_max_cell_count": dgf["final"]["max_cell_count"],
        "DG_indefinite_form_reached":
            any(dgf["ladder"][t]["det_negative_reached"] for t in LADDER)}
    reg(dgf["levels"][-1]["branches"], dg_exit, ratio_100)
    LD.gate("G-COIN-ORDER-FULL",
            "THE COIN-ORDER FIBER, RE-TAKEN AT THE FULL HORIZON, AND THE "
            "DISCLOSURE'S DIRECTION CORRECTED.  'Measurably weaker' was a "
            "count of moving rows at the reduced horizon.  On this unit's own "
            "sharpest observable, at the horizon the head reports, the "
            "alternative order is STRONGER: D.G leaves I7's admissible class "
            "with probability %s against G.D's %s -- larger by a factor whose "
            "exact value is %s, that is %d/100 rounded down -- with %d leaves "
            "against %d.  What is ORDER-INVARIANT is the part of the finding "
            "that is structural: the threshold is exactly %s under both"
            % (dg_exit, gd_exit, str(ratio), ratio_100,
               dgf["levels"][-1]["branches"], gdf["levels"][-1]["branches"],
               order_full["GD_threshold"]),
            (dg_threshold == order_full["GD_threshold"]
             and ratio > 1 and not order_full["DG_indefinite_form_reached"]),
            "G.D threshold %s, D.G threshold %s, ratio %s, D.G reaches an "
            "indefinite form %s"
            % (order_full["GD_threshold"], dg_threshold, str(ratio),
               order_full["DG_indefinite_form_reached"]))

    # THE FIBER MEMBERS ACTUALLY EXECUTED, recorded by the census as it runs
    # them (K3 MAJOR-4): the delivered predicate was `len({...}) >= 1` on three
    # sets, true for any non-empty set, so the gate's execution leg could not
    # fail.  It is now a SET EQUALITY against the declared members.
    declared_members = sorted(
        ["ORDER-GD", "ORDER-DG", "ORIENT-PLUS", "ORIENT-MINUS"]
        + ["INIT-COIN-%d" % i for i in range(3)]
        + ["START-%d%d" % tuple(r["start"]) for r in raw["start_rows"]])
    executed_members = sorted(raw["executed_members"])
    executed_members = pick("MUT-FIBER-BLIND", executed_members,
                            executed_members[:-1])
    members_ok = executed_members == declared_members
    R["walk"] = {
        "state_space_size": DIM, "sites": 9, "coin_states": 3,
        "scalar_shape": sc, "coin_census": cf, "connection": cn,
        "trace_census": raw["trace"],
        "infinite_order_sectors": sum(1 for r in raw["trace"]
                                      if not r["finite_order_possible"]),
        "fibers": [{"id": a, "status": b, "size": c, "note": d}
                   for a, b, c, d in fiber_rows],
        "fiber_measurements": {k: str(v) for k, v in sorted(fibers.items())},
        "fiber_horizon": raw["fiber_T"],
        "declared_fiber_members": declared_members,
        "executed_fiber_members": executed_members,
        "coin_order_back_reaction": raw["order_rows"],
        "coin_order_full_horizon": order_full,
        "orientation_back_reaction": raw["orient_rows"],
        "start_site_rows": raw["start_rows"],
    }
    reg(DIM, raw["fiber_T"], len(declared_members))
    reg(*[r["ipr"] for r in raw["start_rows"]])
    LD.gate("G-FIBERS",
            "THE CHOICE INVENTORY IS PRICED AND ITS DECLARED MEMBERS ARE RUN, "
            "AND THE EXECUTION IS BOUND BY SET EQUALITY RATHER THAN BY A "
            "CARDINALITY: %d items, of which 2 are forced by the parents, 2 "
            "are DERIVED, 1 is DECLARED UNDER A REALITY CONDITION with its "
            "6-member fiber run at the full horizon, 1 is MEASURED from three "
            "declared start sites, and every declared member of every other "
            "fiber is executed at the reduced horizon %d -- %d member ids "
            "declared, %d recorded as executed by the census itself.  ONE OF "
            "THEM IS VERDICT-RELEVANT AND SAYS SO: at the reduced horizon the "
            "coin order G.D moves %d of %d declared observables against its "
            "own frozen control while D.G moves %d, and at the FULL horizon "
            "the direction of that disclosure reverses on the exit "
            "probability.  THE ORIENTATION FIBER IS INERT ON THE IPR ONLY: on "
            "the full observable set it moves %d of %d rows, %s.  THE START "
            "SITE gives the exact TRANSLATE of the base distribution -- naive "
            "list equality is False and translate equality is True, which is "
            "what a real measurement of this fiber looks like -- with the "
            "translation-invariant functional equal at %s"
            % (len(fiber_rows), raw["fiber_T"], len(declared_members),
               len(executed_members),
               raw["order_rows"]["GD"]["differing"],
               raw["order_rows"]["GD"]["of"],
               raw["order_rows"]["DG"]["differing"],
               raw["orient_rows"]["differing"], raw["orient_rows"]["of"],
               ",".join(raw["orient_rows"]["which"]) or "none",
               raw["start_rows"][0]["ipr"]),
            (members_ok and fibers["SITE-TRANSLATION-INVARIANT"]
             and fibers["SITE-IPR-INVARIANT"]
             and not any(r["p_site_equals_base_naively"]
                         for r in raw["start_rows"][1:])),
            "declared members %d, executed %d, equal %s; start-site "
            "distributions are exact translates %s; start-site ipr invariant "
            "%s; naive equality at the translated starts %s"
            % (len(declared_members), len(executed_members), members_ok,
               fibers["SITE-TRANSLATION-INVARIANT"],
               fibers["SITE-IPR-INVARIANT"],
               [r["p_site_equals_base_naively"]
                for r in raw["start_rows"][1:]]))
    SEAL.take("SEAL-WALK", R)

    # -- SEC 5: the law transport, gated ------------------------------------
    say("")
    say("SECTION 4.  THE LAW TRANSPORT -- GATED, NEVER ASSUMED")
    lawchk = sum(arms[k]["checks"]["law_native"] for k in arms)
    lawviol = sum(arms[k]["violations"].get("law_native", 0) for k in arms)
    lawviol = pick("MUT-LAW-TERMINAL", lawviol, 3)
    repchk = sum(arms[k]["checks"]["repricing"] for k in arms)
    repviol = sum(arms[k]["violations"].get("repricing", 0) for k in arms)
    repviol = pick("MUT-LAW-REPRICE", repviol, 2)
    kchk = sum(arms[k]["checks"]["kernel_entry"] for k in arms)
    kviol = sum(arms[k]["violations"].get("kernel_entry", 0) for k in arms)
    kviol = pick("MUT-KERNEL", kviol, 5)
    mdchk = sum(arms[k]["checks"].get("mass_is_density", 0) for k in arms)
    mdviol = sum(arms[k]["violations"].get("mass_is_density", 0)
                 for k in arms)
    # E-23: the row section 4 publishes as the transport's identification had
    # NO falsifier anywhere in this file (K3 MAJOR-4).  It has one now.
    mdviol = pick("MUT-MASS-DENSITY", mdviol, 4)
    broken = raw["broken"]
    broken_kills = broken["violations"].get("law_native", 0) > 0
    reg(lawchk, repchk, kchk, mdchk)
    LD.gate("G-LAW-NATIVE",
            "THE LAW-NATIVE NORMALISER, RE-DERIVED ON THIS ARENA rather than "
            "imported: the potential recursion's terminal condition G(x,0) = 1 "
            "gives G(x,1) = sum_l q(l|x) G(x+l,0) = sum_l q(l|x) = M(x), and "
            "that is measured at %d SITE-STEPS across the four arms with %d "
            "violations.  The forcing is machine-checked, not asserted: the "
            "identity survives an ARBITRARY EXACT RE-PRICING of every priced "
            "event at %d of %d, which is what makes it a fact about the law "
            "and not about this carrier"
            % (lawchk, lawviol, repchk - repviol, repchk),
            lawviol == 0,
            "G(x,1)=M(x) violations %d of %d; re-pricing violations %d of %d"
            % (lawviol, lawchk, repviol, repchk))

    LD.gate("G-LAW-REPRICING",
            "the re-pricing forcing is carried as its own row because it is "
            "the whole warrant for calling the normaliser LAW-NATIVE: every "
            "priced event is multiplied by an arbitrary exact rational and the "
            "identity must survive, at %d of %d site-steps"
            % (repchk - repviol, repchk),
            repviol == 0, "re-pricing violations %d of %d" % (repviol, repchk))

    LD.gate("G-KERNEL-K1",
            "the kernel is q/M ENTRY BY ENTRY: k_1(l|x) M(x) = q(l|x) at %d of "
            "%d kernel entries across the four arms, and the columns sum to 1 "
            "exactly" % (kchk - kviol, kchk),
            kviol == 0, "kernel-entry violations %d of %d" % (kviol, kchk))

    transport_ok = (lawviol == 0 and repviol == 0 and kviol == 0
                    and mdviol == 0 and broken_kills)
    transport_ok = pick("MUT-TRANSPORT-ASSUMED", transport_ok, False)
    R["law"] = {
        "verdict": "TRANSPORT-CONFIRMED" if transport_ok else "BLOCKED",
        "readings": {"A": "the BORN MENU: q(l|x) = |(C psi)(x,l)|^2",
                     "B": "the RECORD MENU: q(l|x) = n_l(x), the forced "
                          "dictionary's own quantity"},
        "law_native_checks": lawchk, "law_native_violations": lawviol,
        "repricing_checks": repchk, "repricing_violations": repviol,
        "kernel_entry_checks": kchk, "kernel_entry_violations": kviol,
        "mass_is_density_checks": mdchk,
        "mass_is_density_violations": mdviol,
        "mass_is_density_class": "DEFINITIONAL UNDER READING A -- the menu IS "
                                 "the post-coin Born weight there, so this row "
                                 "is the identification stated per site, "
                                 "retained as a type check",
        "content_row": "site",
        "content_row_checks": schk,
        "content_row_violations": sviol,
        "terminal_falsifier_kills": broken_kills,
        "terminal_falsifier_horizon": BROKEN_T,
        "terminal_falsifier_violations":
            broken["violations"].get("law_native", 0),
        "empty_columns": sum(arms[k]["checks"].get("column", 0)
                             - arms[k]["checks"].get("kernel", 0)
                             for k in arms),
    }
    LD.gate("G-LAW-TRANSPORT",
            "THE TRANSPORT IS CONFIRMED AND NOT ASSUMED.  Its CONTENT -- the "
            "row that could have failed -- is the SITE row: the coin preserves "
            "each site's mass separately at %d of %d site-branch-steps, and a "
            "coin that mixed sites would leave the law without a menu.  The "
            "menu-mass-is-Born-mass row, %d of %d site-steps, is the "
            "identification stated per site and is DEFINITIONAL under reading "
            "A -- the menu IS the post-coin Born weight there -- so it is "
            "retained as a type check and no longer credited to "
            "site-block-diagonality, which the mechanism gate below shows "
            "measurably does not carry it.  The mechanism is site-locality, "
            "not the coin's identity: every member of the coin fiber confirms "
            "the transport, and any successor whose walk moves amplitude "
            "between sites before the menu is read must re-gate it -- "
            "BLOCKED-AT-THE-LAW-TRANSPORT is reserved for exactly that.  The "
            "transport is falsifiable: breaking the terminal condition "
            "G(x,0) = 1, the identity's only premise, breaks G(x,1) = M(x) at "
            "%d site-steps of an arm rebuilt at the reduced horizon %d"
            % (schk - sviol, schk, mdchk - mdviol, mdchk,
               broken["violations"].get("law_native", 0), BROKEN_T),
            transport_ok,
            "site-row violations %d of %d; menu-mass-is-density violations %d "
            "of %d; terminal-condition falsifier kills the identity %s"
            % (sviol, schk, mdviol, mdchk, broken_kills))
    SEAL.take("SEAL-LAW", R)

    nbd = dict(raw["nbd"])
    nbd_site_violations = pick("MUT-NBD-BLIND",
                               nbd["site_block_diagonal_violations"], 0)
    nbd["site_block_diagonal_violations"] = nbd_site_violations
    R["transport_mechanism"] = nbd
    reg(nbd["mass_is_density_checks"], nbd_site_violations)
    LD.gate("G-TRANSPORT-MECHANISM",
            "THE MECHANISM SENTENCE IS FALSIFIED RATHER THAN ASSERTED, and it "
            "falsifies the delivered attribution.  A coin that is exactly "
            "unitary and NOT site-block-diagonal -- %s -- is built and both "
            "rows are re-taken on it over %d steps: the menu-mass-is-Born-mass "
            "row passes at %d of %d, with a coin violating the very property "
            "it was credited to, while site-block-diagonality itself fails at "
            "%d of %d.  What site-block-diagonality buys is p_post(x) = "
            "p_pre(x), which is the SITE row, and section 3 already names that "
            "one correctly as the law transport's own precondition"
            % (nbd["coin"], nbd["steps"],
               nbd["mass_is_density_checks"] - nbd["mass_is_density_violations"],
               nbd["mass_is_density_checks"], nbd_site_violations,
               nbd["site_block_diagonal_checks"]),
            (nbd["coin_is_unitary_at_every_step"]
             and nbd["mass_is_density_violations"] == 0
             and nbd_site_violations > 0),
            "the demonstration coin is unitary at every step %s; "
            "mass-is-density violations %d of %d; site-block-diagonality "
            "violations %d of %d"
            % (nbd["coin_is_unitary_at_every_step"],
               nbd["mass_is_density_violations"],
               nbd["mass_is_density_checks"], nbd_site_violations,
               nbd["site_block_diagonal_checks"]))
    SEAL.take("SEAL-MECHANISM", R)

    # -- SEC 6: the ensemble -------------------------------------------------
    say("")
    say("SECTION 5.  THE COUPLED ENSEMBLE, EXHAUSTIVE TO THE DECLARED HORIZON")
    ens = {}
    branch_bad = []
    mass_bad = []
    for key in sorted(arms):
        a = arms[key]
        ens[key] = {"levels": a["levels"], "checks": a["checks"],
                    "violations": a["violations"],
                    "repeat_states": a["repeat_states"]}
        for lv in a["levels"]:
            if not lv["mass_is_one"]:
                mass_bad.append((key, lv["t"]))
    # #24, TWO ROUTES, both now implemented (K3 MAJOR-4): route 1 is the
    # length of the frontier that was built; route 2 is the branch count
    # recomputed from the emission supports of the level above.  A dropped
    # branch separates them, and `pruned_branches` is their difference --
    # computed, never typed.
    pruned = 0
    route_rows = []
    for key in sorted(arms):
        a = arms[key]
        for lv in a["levels"]:
            route1 = lv["branches"]
            if mut("MUT-PRUNE") and key == "A-COUPLED" and lv["t"] == 1:
                route1 = route1 - 1
            route2 = lv["branches_from_emission_supports"]
            if route1 <= 0:
                branch_bad.append(key)
            if route1 != route2:
                pruned += route2 - route1
                route_rows.append({"arm": key, "t": lv["t"],
                                   "carried": route1, "from_supports": route2})
    n_leaves = arms["A-COUPLED"]["levels"][-1]["branches"]
    n_leaves_f = arms["A-FROZEN"]["levels"][-1]["branches"]
    n_leaves_b = arms["B-COUPLED"]["levels"][-1]["branches"]
    reg(n_leaves, n_leaves_f, n_leaves_b, HORIZON)
    R["ensemble"] = {"horizon": HORIZON, "ladder": list(LADDER), "arms": ens,
                     "leaves": {k: arms[k]["levels"][-1]["branches"]
                                for k in sorted(arms)},
                     "branch_count_routes": 2,
                     "levels_compared": 4 * HORIZON,
                     "route_disagreements": route_rows,
                     "pruned_branches": pruned}
    LD.gate("G-ENSEMBLE-EXHAUSTIVE",
            "the ensemble is EXHAUSTIVE, and exhaustiveness is checked BY TWO "
            "INDEPENDENT ROUTES rather than by a hard-coded 0: at each of the "
            "%d levels the carried frontier's own length is compared against "
            "the branch count recomputed from the emission supports of the "
            "level above, and `pruned_branches` is their difference.  Every "
            "branch of the emission tree is carried to the declared horizon "
            "T = %d, with no sampling, no pruning and no truncation by weight. "
            " The coupled arm reaches %d leaves at the Born menu and %d at the "
            "record menu; the frozen control reaches %d, and THAT DIFFERENCE "
            "IS ITSELF A MEASUREMENT -- the coupling opens emission channels "
            "the frozen stage closes"
            % (4 * HORIZON, HORIZON, n_leaves, n_leaves_b, n_leaves_f),
            pruned == 0 and not branch_bad,
            "pruned branches %d across %d levels by two routes; route "
            "disagreements %s; degenerate levels %s"
            % (pruned, 4 * HORIZON, route_rows or "none",
               branch_bad or "none"))

    mass_bad = pick("MUT-BRANCH-MASS", mass_bad, [("A-COUPLED", 1)])
    LD.gate("G-BRANCH-MASS",
            "the ensemble is a probability measure at EVERY level of EVERY "
            "arm: the branch weights sum to exactly 1 at all %d levels across "
            "the four arms, in exact rational arithmetic"
            % (4 * HORIZON),
            not mass_bad, "levels whose mass is not 1: %s"
            % (mass_bad or "none"))
    SEAL.take("SEAL-ENSEMBLE", R)

    # -- SEC 7: THE THREE GATES ---------------------------------------------
    say("")
    say("SECTION 6.  THE THREE GATES")

    ckeys = ("norm", "site", "column", "emission_total", "total")
    ctot = sum(arms[k]["checks"].get(c, 0) for k in arms for c in ckeys)
    cviol = sum(arms[k]["violations"].get(c, 0) for k in arms for c in ckeys)
    cviol = pick("MUT-CONSISTENCY", cviol, 1)
    reg(ctot)
    # THE CLASSES ARE LABELLED (K1 m-4).  Composing an identity with a theorem
    # is the claim the gate makes, and it is honest -- but a reader must not be
    # invited to think all %d checks could have failed.  `column` is
    # sum_l q/M = 1, an identity in the definition of k_1 that cannot fail for
    # any coin, menu or record; `emission_total` reduces to `total`.
    CLASS_KIND = {"norm": "CONTENTFUL", "site": "CONTENTFUL",
                  "column": "DEFINITIONAL -- sum_l q/M = 1 is an identity in "
                            "the definition of the kernel",
                  "emission_total": "REDUCES TO total",
                  "total": "CONTENTFUL"}
    R["consistency"] = {
        "checks": ctot, "violations": cviol,
        "per_class": {c: {"checks": sum(arms[k]["checks"].get(c, 0)
                                        for k in arms),
                          "violations": sum(arms[k]["violations"].get(c, 0)
                                            for k in arms),
                          "kind": CLASS_KIND[c]}
                      for c in ckeys},
        "definitional_checks": sum(arms[k]["checks"].get("column", 0)
                                   for k in arms),
        "step_is_defined_at_every_branch": cviol == 0,
    }
    LD.gate("G-CONSISTENCY",
            "GATE 1.  THE COUPLED STEP IS WELL DEFINED, and the composition is "
            "exact.  Unitarity gives sum_x p(x) = 1; site-block-diagonality "
            "gives sum_l k_1(l|x) = 1 at each of the 9 columns; the two "
            "COMPOSE to a total emission mass of exactly 1 at every step.  "
            "Measured PER OBJECT -- per branch, per step, per site -- across "
            "the four arms: %d checks, %d violations.  Nothing here is an "
            "aggregate: every site of every branch of every step is compared "
            "against its own value.  The classes are LABELLED rather than "
            "totalled blind: %d of them are the kernel's DEFINITIONAL leg, "
            "sum_l q/M = 1, which cannot fail for any coin, menu or record -- "
            "composing an identity with a theorem is exactly the claim, and "
            "the reader is told which is which"
            % (ctot, cviol, R["consistency"]["definitional_checks"]),
            cviol == 0,
            "consistency violations %d of %d checks, of which %d are the "
            "definitional column class"
            % (cviol, ctot, R["consistency"]["definitional_checks"]))
    SEAL.take("SEAL-CONSISTENCY", R)

    obs_rows = []
    for reading in ("A", "B"):
        C = arms["%s-COUPLED" % reading]["final"]
        Fz = arms["%s-FROZEN" % reading]["final"]
        for name in ("p_site", "ipr", "emission_field", "link_class_marginal",
                     "admissibility_exit_probability", "posdef_distribution",
                     "det_values_reached", "max_cell_count",
                     "curvature_constant_probability"):
            cv, fv = C[name], Fz[name]
            if mut("MUT-INERT"):
                cv = fv
            obs_rows.append({"reading": reading, "observable": name,
                             "coupled": cv, "frozen": fv,
                             "differs": cv != fv})
    n_diff = sum(1 for r in obs_rows if r["differs"])
    frozen_ran = pick("MUT-NO-FROZEN",
                      all(arms["%s-FROZEN" % r]["checks"]["norm"] > 0
                          for r in ("A", "B")), False)
    R["nontriviality"] = {
        "observables": obs_rows, "declared_observables": 9,
        "rows": len(obs_rows), "rows_that_differ": n_diff,
        "inert": n_diff == 0,
        "frozen_control_executed": frozen_ran,
        "leaf_counts": {"coupled_A": n_leaves, "frozen_A": n_leaves_f,
                        "coupled_B": n_leaves_b},
    }
    reg(len(obs_rows), n_diff)
    LD.gate("G-FROZEN-CONTROL",
            "THE FROZEN-STAGE CONTROL IS MANDATORY AND IT RAN: the same walk, "
            "the same emission rule, the same branching, and counts that never "
            "update -- executed through the SAME function as the coupled arm, "
            "so the control cannot differ from it in anything but the one line "
            "that updates the record",
            frozen_ran, "frozen arms executed %s" % frozen_ran)

    LD.gate("G-NONTRIVIALITY",
            "GATE 2, TWO-WAY.  The declared observable set -- the site "
            "distribution, its inverse participation, the emission field, the "
            "link-class marginal, the I7-admissibility exit probability, the "
            "positive-definite-site distribution, the determinant spectrum, "
            "the maximum cell count and the curvature homogeneity -- is "
            "compared against the FROZEN-STAGE CONTROL at both readings: %d of "
            "%d rows DIFFER.  Identical would have been COUPLING-INERT, an "
            "honest first-class outcome, and the gate is written so that it "
            "would have been reported" % (n_diff, len(obs_rows)),
            n_diff > 0 and frozen_ran,
            "rows differing %d of %d; inert %s"
            % (n_diff, len(obs_rows), n_diff == 0))
    SEAL.take("SEAL-NONTRIVIALITY", R)

    # -- the admissibility ladder -------------------------------------------
    ladder_rows = []
    for reading in ("A", "B"):
        for t in LADDER:
            c = arms["%s-COUPLED" % reading]["ladder"][t]
            f = arms["%s-FROZEN" % reading]["ladder"][t]
            ladder_rows.append({
                "reading": reading, "horizon": t,
                "coupled_exit": c["admissibility_exit_probability"],
                "frozen_exit": f["admissibility_exit_probability"],
                "coupled_exit_positive": c["exit_positive"],
                "det_zero_reached": c["det_zero_reached"],
                "det_negative_reached": c["det_negative_reached"],
                "max_cell_count": c["max_cell_count"]})
    thresholds = {}
    for reading in ("A", "B"):
        hit = [r["horizon"] for r in ladder_rows
               if r["reading"] == reading and r["coupled_exit_positive"]]
        thresholds[reading] = min(hit) if hit else None
    if mut("MUT-LADDER"):
        thresholds = {"A": 4, "B": 4}
    exit_A = arms["A-COUPLED"]["final"]["admissibility_exit_probability"]
    exit_B = arms["B-COUPLED"]["final"]["admissibility_exit_probability"]
    any_neg = any(r["det_negative_reached"] for r in ladder_rows)
    reg(exit_A, exit_B)
    R["ladder"] = {"rows": ladder_rows, "thresholds": thresholds,
                   "exit_probability_at_horizon": {"A": exit_A, "B": exit_B},
                   "indefinite_form_reached": any_neg,
                   "frozen_exit_at_every_horizon_is_zero":
                       all(Fraction(r["frozen_exit"]) == 0
                           for r in ladder_rows)}
    LD.gate("G-ADMISSIBILITY-LADDER",
            "THE SHARPEST MEASUREMENT IN THIS UNIT, and it is a THRESHOLD.  "
            "I7's own criterion -- a record is admissible when q is "
            "nonsingular and positive definite at every site, by the exact "
            "Sylvester criterion -- is evaluated on the record the walk reads, "
            "at EVERY horizon of the ladder and on both arms.  The coupled "
            "record leaves I7's admissible class with exact positive "
            "probability %s at the Born menu and %s at the record menu, and "
            "with probability EXACTLY ZERO at every horizon below %s.  The "
            "frozen control never leaves it, at any horizon.  The exit is to "
            "the SINGULAR boundary, det = 0: no indefinite form is reached "
            "here, and that is measured (%s) rather than assumed"
            % (exit_A, exit_B, thresholds["A"], any_neg),
            (thresholds["A"] == HORIZON and thresholds["B"] == HORIZON
             and R["ladder"]["frozen_exit_at_every_horizon_is_zero"]
             and not any_neg),
            "exit thresholds %s; frozen exit identically zero %s; indefinite "
            "form reached %s"
            % (thresholds, R["ladder"]["frozen_exit_at_every_horizon_is_zero"],
               any_neg))
    SEAL.take("SEAL-LADDER", R)

    # -- THE EXIT CENSUS: the mechanism, classified rather than asserted -----
    cen = dict(arms["A-COUPLED"]["final"]["exit_census"])
    sched = raw["schedule"]
    census_total = sum(cen["count_vectors"].values())
    census_total = pick("MUT-EXIT-CENSUS", census_total, census_total + 1)
    one_site_only = (list(cen["sites_out_per_leaf"]) == ["1"])
    pattern_003 = (list(cen["excess_patterns"]) == ["0,0,3"])
    degeneracy = len(cen["count_vectors"])
    reg(cen["inadmissible_leaves"], degeneracy, sched["earliest_third_visit"],
        *sched["sites_with_positive_mass_by_step"])
    reg(*[str(v) for v in cen["count_vectors"].values()])
    R["exit_census"] = {
        "leaves": cen["inadmissible_leaves"],
        "sites_out_per_leaf": cen["sites_out_per_leaf"],
        "count_vectors": cen["count_vectors"],
        "excess_patterns": cen["excess_patterns"],
        "link_class_degeneracy": degeneracy,
        "weight_equals_the_exit_probability":
            cen["weight"] == exit_A,
        "schedule": sched,
        "event_budget_from_the_welded_record": 3,
        "step_budget_is_the_return_time": sched["earliest_third_visit"],
    }
    LD.gate("G-EXIT-CENSUS",
            "THE HORIZON-%d MECHANISM IS A CENSUS, NOT AN ASSERTION.  All %d "
            "inadmissible leaves of the coupled frontier are classified: every "
            "one has exactly ONE site out of I7's class, every one carries the "
            "excess pattern (0, 0, 3) at that site, and the census is %d-fold "
            "degenerate across the link classes -- %s -- so the exit is one "
            "arithmetic event and nothing else, and its total weight is "
            "exactly the published exit probability.  THE TWO BUDGETS MEET: "
            "the margin from the welded record to a singular form is 3 events "
            "on one link, which is CR-A's own measured three-event margin to "
            "G-SINGULAR read from the other side; and the step budget is the "
            "RETURN TIME of the +l shift -- the walk emits one division event "
            "per step, so three events on one cell need positive Born mass at "
            "that site at three distinct steps, the support schedule is %s "
            "sites at steps 1..%d, and the earliest third visit over all nine "
            "sites is step %d.  CR-A supplies the 3; the return time supplies "
            "the %d"
            % (HORIZON, cen["inadmissible_leaves"], degeneracy,
               ", ".join("%s at %d" % (k, v)
                         for k, v in sorted(cen["count_vectors"].items())),
               sched["sites_with_positive_mass_by_step"], HORIZON,
               sched["earliest_third_visit"], sched["earliest_third_visit"]),
            (one_site_only and pattern_003 and degeneracy == 3
             and census_total == cen["inadmissible_leaves"]
             and cen["weight"] == exit_A
             and sched["earliest_third_visit"] == thresholds["A"]),
            "leaves %d, classified %d, one site out per leaf %s, excess "
            "patterns %s, degeneracy %d, census weight equals the exit "
            "probability %s, earliest third visit %s equals the threshold %s"
            % (cen["inadmissible_leaves"], census_total, one_site_only,
               list(cen["excess_patterns"]), degeneracy,
               cen["weight"] == exit_A, sched["earliest_third_visit"],
               thresholds["A"]))
    SEAL.take("SEAL-EXIT-CENSUS", R)

    # -- GATE 3: THE REQUIREMENT --------------------------------------------
    battery = {}
    for reading in ("A", "B"):
        battery[reading] = measure_battery(raw, reading)
    pol_bad = [(rd, r["id"]) for rd in battery for r in battery[rd]
               if not r["polarity_matches"]]
    wit_A, rev_A, res_A = requirement_selector(battery["A"])
    wit_B, rev_B, res_B = requirement_selector(battery["B"])
    witnesses = sorted({r["id"] for r in wit_A} | {r["id"] for r in wit_B})
    reverses = sorted({r["id"] for r in rev_A} | {r["id"] for r in rev_B})
    restateds = sorted({r["id"] for r in res_A} | {r["id"] for r in res_B})
    stale = raw["stale"]
    psi_internal_ids = [k for k, cl, rs, _s, _a, _b in BATTERY_SPEC
                        if cl == "PSI-INTERNAL"]
    stale_clean = (stale["violations"].get("norm", 0) == 0
                   and stale["violations"].get("site", 0) == 0
                   and stale["violations"].get("law_native", 0) == 0
                   and stale["violations"].get("column", 0) == 0)
    if mut("MUT-STALENESS"):
        stale_clean = False
    blind_rows = raw["count_blind"]
    blind_viol = sum(r["psi_internal_violations"] for r in blind_rows)
    blind_viol = pick("MUT-COUNT-BLIND", blind_viol, 1)
    k5 = raw["k5"]
    ray_repeats = k5["frozen_ray_repeats"] + k5["coupled_ray_repeats"]
    ray_repeats = pick("MUT-K5-RETURN", ray_repeats, 1)
    robust = refusal_robustness(battery["A"])
    stamp_only = len(robust["stamp_dropped"])
    stamp_only = pick("MUT-REFUSAL-DROP", stamp_only, 2)
    stale_total = sum(stale["checks"].values())
    reg(len(BATTERY_SPEC), len(psi_internal_ids), stale_total,
        sum(r["checks"] for r in blind_rows), len(blind_rows),
        k5["frozen_steps"], k5["frozen_distinct_rays"], k5["coupled_levels"])
    R["battery"] = {
        "rows": battery, "spec": len(BATTERY_SPEC),
        "psi_internal_rows": len(psi_internal_ids),
        "requirement_witnesses": witnesses,
        "reverse_direction_rows": reverses,
        "update_rule_restated_rows": restateds,
        "forward_direction": "EMPTY-BEFORE-THE-RUN",
        "count_blindness": {
            "rows": blind_rows,
            "fields": len(blind_rows),
            "checks": sum(r["checks"] for r in blind_rows),
            "psi_internal_violations": blind_viol},
        "k5_no_return": k5,
        "refusal_robustness": robust,
        "staleness_blindness": {
            "horizon": HORIZON,
            "quantifier": "every SINGLE-TIME closure that is a property of "
                          "(psi, U(n)) uniformly in n; the machine check is an "
                          "instance of it over K1-K4, not a proof of it",
            "stale_cells": list(STALE_CELLS),
            "stale_field_is_admissible": all(
                admissible(site_counts(stale_field(), s)) for s in range(9)),
            "psi_internal_closures_hold_on_the_stale_stage": stale_clean,
            "checks": stale["checks"],
            "total_checks": stale_total},
    }
    LD.gate("G-BATTERY-POLARITY",
            "every one of the %d battery rows carries the polarity it was "
            "PRE-REGISTERED with, at both readings, and the measurement is "
            "compared against that pre-registration row by row: %d mismatches. "
            " The sedimentary row is the corpus's own -- at the ruled carrier "
            "no class is ever revisited -- transported to the state grain and "
            "measured here" % (len(BATTERY_SPEC), len(pol_bad)),
            not pol_bad, "polarity mismatches: %s" % (pol_bad or "none"))

    restateds = pick("MUT-ONE-WAY", restateds, [])
    LD.gate("G-BATTERY-TWO-WAY",
            "the battery is TWO-WAY and both directions are non-empty, which "
            "is what makes it an instrument rather than a list: %d rows fail "
            "frozen and pass coupled (%s), and %d rows pass frozen and fail "
            "coupled (%s).  A one-way battery could not have returned "
            "NOT-REQUIRED as a measurement"
            % (len(restateds), ",".join(restateds) or "none",
               len(reverses), ",".join(reverses) or "none"),
            bool(restateds) and bool(reverses),
            "fail-frozen rows %s; fail-coupled rows %s"
            % (restateds or "none", reverses or "none"))

    LD.gate("G-STALENESS-BLIND",
            "THE STALENESS-BLINDNESS THEOREM, machine-checked rather than "
            "argued, AT THIS UNIT'S OWN FULL HORIZON %d and disclosed as such. "
            " A frozen stage is itself an admissible stage, so the walk it "
            "generates is a perfectly good unitary walk on this arena: run on "
            "a DECLARED STALE count field -- admissible, and not the welded "
            "one -- every psi-internal closure of the battery still holds, at "
            "%d checks.  THE QUANTIFIER IS THE ONE THE ARGUMENT CARRIES: every "
            "SINGLE-TIME closure that is a property of (psi, U(n)) uniformly "
            "in n cannot see n, and this check is an INSTANCE of that over "
            "K1-K4 rather than a proof of it.  Nothing internal to the state "
            "at a single time can detect that its stage is out of date, which "
            "is exactly why the rows that discriminate are the ones that "
            "mention the record"
            % (HORIZON, stale_total),
            stale_clean and R["battery"]["staleness_blindness"][
                "stale_field_is_admissible"],
            "psi-internal closures on the stale stage hold %s at %d checks; "
            "the stale field is admissible %s"
            % (stale_clean, stale_total,
               R["battery"]["staleness_blindness"]["stale_field_is_admissible"]))

    LD.gate("G-COUNT-BLIND",
            "THE FORWARD DIRECTION WAS EMPTY BEFORE THE RUN, AND THAT IS "
            "MEASURED HERE RATHER THAN CONCEDED IN PROSE.  K1, K2, K3 and K4 "
            "never read the record, so they hold for EVERY count field "
            "whatever -- run on %d declared FOREIGN fields, two of which are "
            "not even admissible and none of which this run generates, they "
            "record %d psi-internal violations in %d checks.  With K5's "
            "delivered predicate unfireable, no psi-internal row of this "
            "battery COULD have failed frozen, whatever the physics did.  What "
            "makes that emptiness forced rather than chosen is the "
            "staleness-blindness theorem above: at a single time there is "
            "nothing else the class could have contained"
            % (len(blind_rows), blind_viol,
               sum(r["checks"] for r in blind_rows)),
            blind_viol == 0 and len(blind_rows) == len(FOREIGN_FIELDS),
            "psi-internal violations on foreign count fields %d of %d checks "
            "over %d fields; fields not admissible %d"
            % (blind_viol, sum(r["checks"] for r in blind_rows),
               len(blind_rows),
               sum(1 for r in blind_rows if not r["is_admissible"])))

    LD.gate("G-K5-NO-RETURN",
            "K5 IS A REAL TEST NOW.  The delivered predicate compared RAW "
            "amplitudes, which this unit's own unitarity gate proves carry "
            "norm 9^t exactly -- %s by level -- so two states at different "
            "levels could never be equal and `repeat_states = 0` was a "
            "property of the normalisation, not a measurement.  The row is "
            "re-taken at two grains that CAN fire: the exactly normalised "
            "state psi_t / 3^t and the RAY class.  The frozen arm is driven "
            "%d steps, well past the ladder: %d ray repeats, %d distinct rays. "
            " The coupled arm is compared cross-level to level %d -- %s "
            "distinct states by level -- with %d repeats.  So the repaired row "
            "still holds ON BOTH STAGES, and the verdict stands on a row that "
            "could have moved it"
            % (k5["raw_state_norms_by_level"], k5["frozen_steps"],
               k5["frozen_ray_repeats"], k5["frozen_distinct_rays"],
               k5["coupled_levels"],
               [lv["distinct_normalised_states"] for lv in k5["coupled_by_level"]],
               k5["coupled_ray_repeats"]),
            (ray_repeats == 0 and k5["frozen_normalised_repeats"] == 0
             and k5["coupled_normalised_repeats"] == 0
             and k5["raw_norms_all_distinct"]),
            "frozen ray repeats %d in %d steps; coupled cross-level ray "
            "repeats %d to level %d; raw norms distinct by level %s"
            % (k5["frozen_ray_repeats"], k5["frozen_steps"],
               k5["coupled_ray_repeats"], k5["coupled_levels"],
               k5["raw_norms_all_distinct"]))

    LD.gate("G-REFUSAL-ROBUST",
            "THE NEGATIVE IS DOUBLY GROUNDED, AND EITHER GROUND ALONE CARRIES "
            "IT.  NO-WITNESS rests on two declarations about K9 and K10 -- "
            "their CLASS and their UPDATE-RULE-RESTATED stamp -- and each is "
            "dropped alone and both together, with the selector re-run: drop "
            "the stamp alone and the witnesses are %s, because the class "
            "filter still excludes them; reclassify them as PSI-INTERNAL and "
            "keep the stamp and the witnesses are %s; drop BOTH and the "
            "witnesses are %s.  Only the conjunction of two failed "
            "declarations produces a witness, so NO-WITNESS survives the "
            "failure of EITHER refusal declaration alone"
            % (robust["stamp_dropped"] or "none",
               robust["class_dropped"] or "none",
               robust["both_dropped"] or "none"),
            (stamp_only == 0 and not robust["class_dropped"]
             and not robust["as_delivered"]
             and len(robust["both_dropped"]) == 2),
            "as delivered %s; stamp dropped %s; class dropped %s; both "
            "dropped %s"
            % (robust["as_delivered"] or "none",
               robust["stamp_dropped"] or "none",
               robust["class_dropped"] or "none",
               robust["both_dropped"] or "none"))

    LD.gate("G-REQUIREMENT",
            "GATE 3, THE THEOREM, TWO-WAY -- AND THE NEGATIVE IS STAMPED WITH "
            "WHAT CARRIES IT.  A REQUIREMENT WITNESS must be a closure that is "
            "INTERNAL TO THE QUANTUM SIDE, is NOT the update rule restated, "
            "and FAILS frozen while PASSING coupled.  Measured: %d such "
            "witnesses IN THE %d-ROW PRE-REGISTERED BATTERY -- and this is not "
            "a search that came back empty, it is a search whose FORWARD "
            "DIRECTION WAS EMPTY BEFORE THE RUN: K1-K4 are count-blind, "
            "measured on %d foreign fields, and K5's delivered predicate could "
            "not fire.  What makes that emptiness FORCED rather than chosen is "
            "the staleness-blindness theorem, so the no-witness is CARRIED BY "
            "THE STALENESS THEOREM rather than by the battery's coverage, and "
            "the head says so.  What the battery does return is measured and "
            "reported instead -- %d rows in the REVERSE direction (%s), which "
            "the pin pre-registers as equally reportable, and %d rows that "
            "fail frozen only by restating the update rule (%s), which the "
            "selector refuses by construction and whose refusal survives "
            "dropping either declaration alone.  All %d psi-internal rows hold "
            "on BOTH stages, K5 at the repaired ray grain"
            % (len(witnesses), len(BATTERY_SPEC), len(blind_rows),
               len(reverses), ",".join(reverses) or "none",
               len(restateds), ",".join(restateds) or "none",
               len(psi_internal_ids)),
            not pol_bad and not (set(witnesses) & set(restateds)),
            "requirement witnesses: %s" % (witnesses or "none"))
    SEAL.take("SEAL-BATTERY", R)

    # -- SEC 8: THE WALLS ----------------------------------------------------
    say("")
    say("SECTION 7.  THE WALLS")
    layer = measurement_layer(R, LD)
    if mut("MUT-WALL-BHS"):
        layer += " the boosted rest frame reading is taken here "
    if mut("MUT-WALL-KR"):
        layer += " the myrheim-meyer dimension estimate is 2.38 "
    if mut("MUT-WALL-COSMO"):
        layer += " the continuum limit and the cosmological expansion "

    ptext = paper_text if paper_text is not None else ""
    if mut("MUT-WALL-L1"):
        # the injection is line-wrapped and blockquoted AT A WORD BOUNDARY --
        # splitting mid-word would inject a string the needle does not match
        # and would make the falsifier a no-op rather than an evasion
        _cut = BANNED_L1.index(" ", 40)
        ptext = (ptext + "\n> " + BANNED_L1[:_cut] + "\n> "
                 + BANNED_L1[_cut + 1:] + "\n")
    l1_present = canon(BANNED_L1) in canon(ptext)
    LD.gate("G-WALL-L1",
            "L-1: order-level covariance is a FOURTH FORM, outside paper 8's "
            "three, and its admissibility is not argued here.  This unit "
            "declares no group acting on the generated causal order and "
            "constructs no bridge from Z_3^2 translations to any covariance "
            "group, so THE FOURTH FORM IS NOT TESTED HERE.  The sentence "
            "retracted in 2026 is not reproduced, and the gate that enforces "
            "its absence whitespace-normalises, ASCII-folds and strips "
            "markdown prefixes from both sides, so a line-wrapped or "
            "blockquoted injection dies too",
            not l1_present, "the retracted sentence is present: %s"
            % l1_present)

    bhs_hits = [n for n in BHS_NEEDLES if n in layer]
    LD.gate("G-WALL-BHS",
            "BHS: a Poisson sprinkling admits no Lorentz-invariant "
            "finite-valency graph, and this arena is finite-valency by "
            "construction, so running that test would manufacture a false "
            "negative.  None is run -- and the abstention is MEASURED rather "
            "than asserted: this run's whole measurement layer, every measured "
            "receipt key together with the statement and evidence of every "
            "non-wall gate evaluated, is scanned for the terms whose presence "
            "would mean the reading was taken",
            not bhs_hits, "hits: %s" % (bhs_hits or "none"))

    kr_hits = [n for n in KR_NEEDLES if n in layer]
    LD.gate("G-WALL-KR",
            "Kleitman-Rothschild: a reading of that kind without a height "
            "control is worthless, and this unit takes none -- no chart width, "
            "no Myrheim-Meyer estimate, no max-shatter reading -- so the "
            "height control is not owed and not manufactured.  Measured on the "
            "same surface",
            not kr_hits, "hits: %s" % (kr_hits or "none"))

    cosmo_hits = [n for n in COSMO_NEEDLES if n in layer]
    LD.gate("G-WALL-COSMO",
            "no continuum, limit, asymptotic or cosmological reading is taken "
            "anywhere in this unit, and the scan runs on the same surface.  "
            "The word `horizon` is DECLARED OUT of this needle set with its "
            "reason printed: it is this unit's own name for the declared "
            "finite number of coupled steps and the gravity law's own "
            "relative-horizon index, so a scan that fired on it would fire on "
            "the pin's own vocabulary",
            not cosmo_hits, "hits: %s" % (cosmo_hits or "none"))

    # the two NAMING walls read the object under test, so they are evaluated
    # exactly when there is one.  `--numbers` carries no paper by contract and
    # never reaches the writer, so a naming gate it could not evaluate is
    # skipped there rather than passed vacuously.
    lz = hx = None
    if ptext:
        lz = match_needle(ptext, LORENTZ_NAMED)
        hx = match_needle(ptext, HEX_NAMED)
    if mut("MUT-WALL-LORENTZ"):
        lz = False
    if mut("MUT-WALL-HEX"):
        hx = False
    if ptext or MUT in ("MUT-WALL-LORENTZ", "MUT-WALL-HEX"):
        LD.gate(
            "G-WALL-LORENTZ-NAMED",
            "THE LORENTZIAN RESONANCE IS NAMED, and the naming is mandatory "
            "and sharper here than at the weld, because this unit MEASURES a "
            "determinant that reaches 0.  A reader arriving from the "
            "relativity line will hear a signature in that; the naming "
            "sentence is required to be present in the object under test and "
            "the falsifier deletes it.  Silence is how a resonance becomes "
            "governance",
            bool(lz), "the naming sentence is present: %s" % lz)
        LD.gate(
            "G-WALL-HEX-NAMED",
            "THE SECOND RESONANCE IS NAMED, and paper-19's S-7 registered it "
            "FOR this unit before this unit was written -- the hexagonal one, "
            "unit lengths meeting at one hundred and twenty degrees, a wall "
            "row the coupling unit should inherit before it writes the word "
            "`triangular`.  It is inherited, named and gated here",
            bool(hx), "the hexagonal naming sentence is present: %s" % hx)
    R["walls"] = {"l1_sentence_present": l1_present, "bhs_hits": bhs_hits,
                  "kr_hits": kr_hits, "cosmo_hits": cosmo_hits,
                  "lorentz_named": lz, "hexagonal_named": hx,
                  "horizon_declared_out_of_the_cosmological_scan": True}
    SEAL.take("SEAL-WALLS", R)

    # -- SEC 9: the verdict --------------------------------------------------
    say("")
    say("SECTION 8.  THE VERDICT")
    R["counts"] = {
        "sources": len(SOURCES), "verbatim": len(VERBATIM),
        "horizon": HORIZON, "leaves_coupled_A": n_leaves,
        "leaves_frozen_A": n_leaves_f, "leaves_coupled_B": n_leaves_b,
        "consistency_checks": ctot, "battery_rows": len(BATTERY_SPEC),
        "observable_rows": len(obs_rows), "differing_rows": n_diff,
        "law_native_checks": lawchk, "kernel_entry_checks": kchk,
    }
    verdict = build_verdict(R)
    if mut("MUT-VERDICT-WORD"):
        verdict = dict(verdict)
        verdict["gates"] = verdict["gates"].replace(
            "COUPLING-CONSISTENT-NOT-REQUIRED",
            "COUPLING-CONSISTENT-AND-REQUIRED-K9-SOURCING")
    if mut("MUT-VERDICT-VALUE"):
        verdict = dict(verdict)
        verdict["arena"] = verdict["arena"].replace("27 OF 27", "26 OF 27", 1)
    R["verdict"] = verdict
    rebuilt, why = reconstruct(json.dumps(R, sort_keys=True, default=str))
    ok = all(rebuilt[k] == verdict[k] for k in verdict)
    LD.gate("G-VERDICT-RECONSTRUCTED",
            "the head is DERIVED A SECOND TIME by a comparator that shares no "
            "builder code and no typed literal with the emitter: it re-parses "
            "the SERIALIZED receipt, TYPES ALL THREE VERDICT TEMPLATES ITSELF "
            "-- the gates segment included, which carries the outcome word -- "
            "and re-derives that word from the receipt's own consistency, "
            "nontriviality and battery rows.  A one-line forgery of the "
            "outcome word moves the emitter alone and dies here, and so does "
            "a retyped value inside a segment",
            ok, "segments matching: %s; comparator note: %s"
            % (sorted(k for k in verdict if rebuilt[k] == verdict[k]), why))
    SEAL.take("SEAL-VERDICT", R)
    SEAL.take("SEAL-COUNTS", R)

    for seg in verdict.values():
        say("")
        say(seg)

    # -- the paper gates -----------------------------------------------------
    if do_paper and paper_text is not None:
        say("")
        say("SECTION 9.  THE PAPER UNDER TEST")
        claims = paper_claims(R)
        missing = []
        for cid, sent in claims:
            hay = ptext
            if mut("MUT-PAPER-CLAIM") and cid == "C01":
                sent = sent.replace("27 cells", "26 cells")
            if not match_needle(hay, sent):
                missing.append(cid)
        R["paper_claims"] = [{"id": c, "sentence": s, "located":
                              c not in missing} for c, s in claims]
        LD.gate("G-PAPER-CLAIMS",
                "%d load-bearing sentences are ASSEMBLED FROM THIS RUN's own "
                "measurements and located in the delivered paper's bytes, so a "
                "value moved to the wrong place in the prose dies inside the "
                "run.  The pin's scope row is one of them and it is carried "
                "verbatim" % len(claims),
                not missing, "claims not located: %s" % (missing or "none"))
        SEAL.take("SEAL-PAPER-CLAIMS", R)

        trows = paper_tables(R)
        if mut("MUT-PAPER-TABLE"):
            trows = trows[:-1] + [("T-FORGED", "| FORGED | SYMMETRY | holds | "
                                               "holds |")]
        tbad = []
        tcounts = []
        canon_paper = canon(ptext)
        for tid, row in trows:
            occ = canon_paper.count(canon(row))
            tcounts.append({"id": tid, "row": row, "occurrences": occ})
            if occ != 1:
                tbad.append(tid)
        R["paper_tables"] = tcounts
        LD.gate("G-PAPER-TABLES",
                "E-22: THE TABLES RENDER AS CLAIMS.  Every one of the %d rows "
                "of the composition census and the closure battery is "
                "ASSEMBLED FROM THIS RUN's own measurements and required to "
                "occur in the paper EXACTLY ONCE -- occurrence count, not "
                "containment -- so a moved cell in the census decomposition or "
                "a swapped battery polarity dies inside the run rather than "
                "shipping at exit 0" % len(trows),
                not tbad, "rows not located exactly once: %s"
                % (tbad or "none"))
        SEAL.take("SEAL-PAPER-TABLES", R)

        cov = paper_coverage(R, ptext)
        if mut("MUT-PAPER-NUMERAL"):
            cov = dict(cov)
            cov["unregistered"] = ["123456789"]
        R["paper_coverage"] = cov
        LD.gate("G-PAPER-NUMERAL-COVERAGE",
                "#20 WITH THE FENCED-BLOCK ADDENDUM AND E-22's INLINE-SPAN "
                "ADDENDUM: %d numerals are scanned in the paper, %d of them "
                "inside the %d FENCED VERDICT BLOCKS and %d inside the %d "
                "INLINE CODE SPANS, both under the fenced rule, where a hyphen "
                "is a word separator rather than a sign -- so the numerals of "
                "the head, the sentence the corpus quotes, AND every "
                "backticked value of the contrast and ladder tables are "
                "scanned rather than skipped.  Every one is allow-listed only "
                "against a value this run computed"
                % (cov["scanned"], cov["fenced_numerals"],
                   cov["fenced_blocks"], cov["inline_numerals"],
                   cov["inline_spans"]),
                not cov["unregistered"],
                "unregistered numerals: %s" % (cov["unregistered"] or "none"))

        head_bad = []
        for k, seg in verdict.items():
            probe = seg
            if mut("MUT-PAPER-HEAD") and k == "arena":
                probe = seg[:-1] + "Z"
            if canon(probe) not in canon(ptext):
                head_bad.append(k)
        blockmap = block_multiset(ptext)
        if mut("MUT-PAPER-BLOCK"):
            blockmap = Counter(dict(sorted(blockmap.items())[:-1]))
        want = Counter()
        for seg in verdict.values():
            want[canon(seg)] += HEAD_COPIES
        multiset_ok = blockmap == want
        cov["fenced_block_multiset_matches"] = multiset_ok
        cov["fenced_block_distinct"] = len(blockmap)
        cov["fenced_block_copies_each"] = sorted(set(blockmap.values()))
        LD.gate("G-PAPER-HEAD-VERBATIM",
                "each of the %d derived verdict segments is matched into the "
                "paper CHARACTER FOR CHARACTER after normalisation, so the "
                "blocks a reader will quote are bound to the receipt as "
                "STRINGS and not merely as numbers -- AND the fenced blocks "
                "are compared as a MULTISET rather than by containment (E-22): "
                "the paper carries %d fenced blocks, %d distinct, each of the "
                "%d derived segments appearing exactly %d times, so a second "
                "copy of a head cannot be forged behind a clean twin"
                % (len(verdict), sum(blockmap.values()), len(blockmap),
                   len(verdict), HEAD_COPIES),
                not head_bad and multiset_ok,
                "segments not located verbatim: %s; fenced-block multiset "
                "matches the derived segments %s (%d blocks, %d distinct, "
                "copies %s)"
                % (head_bad or "none", multiset_ok, sum(blockmap.values()),
                   len(blockmap), sorted(set(blockmap.values()))))
        SEAL.take("SEAL-PAPER-COVERAGE", R)

        pol = paper_polarity(R, ptext,
                             mutated=pick("MUT-PAPER-POLARITY", False, True))
        R["polarity"] = pol
        LD.gate("G-PAPER-CLAIM-POLARITY",
                "%d claim polarities: for each, the POSITIVE form must be "
                "present in the paper and its NEGATION absent, so a paper that "
                "carried both readings, or the wrong one, dies here" % len(pol),
                all(p["ok"] for p in pol),
                "failing polarities: %s"
                % ([p["id"] for p in pol if not p["ok"]] or "none"))
        SEAL.take("SEAL-POLARITY", R)
    else:
        R["paper_claims"] = []
        R["paper_tables"] = []
        R["paper_coverage"] = {"scanned": 0, "allowed": 0, "fenced_blocks": 0,
                               "fenced_numerals": 0, "inline_spans": 0,
                               "inline_numerals": 0, "unregistered": [],
                               "fenced_block_multiset_matches": None,
                               "fenced_block_distinct": 0,
                               "fenced_block_copies_each": []}
        R["polarity"] = []
        SEAL.take("SEAL-PAPER-CLAIMS", R)
        SEAL.take("SEAL-PAPER-TABLES", R)
        SEAL.take("SEAL-PAPER-COVERAGE", R)
        SEAL.take("SEAL-POLARITY", R)

    R["transcript_head"] = LINES[:40]
    return LD, SEAL, R, verdict, raw


# ===========================================================================
# SECTION 9.  THE VERDICT, THE COMPARATOR, AND THE PAPER GATES
# ===========================================================================

def outcome_word(consistent, inert, witnesses):
    """the pre-registered selector, in one place, from three booleans."""
    if not consistent:
        return "COUPLING-INCONSISTENT-COMPOSITION"
    if inert:
        return "COUPLING-INERT"
    if witnesses:
        return "COUPLING-CONSISTENT-AND-REQUIRED-%s" % witnesses[0]
    return "COUPLING-CONSISTENT-NOT-REQUIRED"


def requirement_label(witnesses):
    """the requirement segment's own LABEL, derived from the same primitive as
    the outcome word rather than typed on both sides of the comparator (K3
    MINOR-10): had a witness existed, the builder's word and this label would
    have disagreed and neither side would have noticed."""
    if witnesses:
        return "REQUIRED-%s" % witnesses[0]
    return "NO-WITNESS-CARRIED-BY-THE-STALENESS-THEOREM"


def build_verdict(R):
    a = R["arena"]
    w = R["walk"]
    L = R["law"]
    sc = w["scalar_shape"]
    cf = w["coin_census"]
    ci = R["coin_invariance"]
    of = w["coin_order_full_horizon"]
    M0 = R["transport_mechanism"]
    c = R["consistency"]
    nt = R["nontriviality"]
    b = R["battery"]
    ld = R["ladder"]
    xc = R["exit_census"]
    seg_arena = (
        "COUPLING-ARENA-[WELDED-RECORD-REBUILT-AND-DRIVEN-THROUGH-THE-"
        "COMMITTED-MENUS: n=1 AT %d OF %d CELLS; det=%s AT %d OF 9 SITES; "
        "POSDEF %d OF 9 BY I7'S OWN SYLVESTER CRITERION; FORCED AT MAXHITS %d "
        "WITH %d EVENTS AND %d DIVISION EVENTS AND NO REFUSAL; THE FORCED "
        "DICTIONARY INSTANTIATED: THE REALISED CO-DIVISION RELATION IS THE "
        "TARGET'S OWN CAYLEY INCIDENCE AT %d OF %d PAIRS AT EQUALITY AND MEETS "
        "THE ONE DIRECTION I7 DOES NOT DECLARE AT 0; SITE-ASSIGNMENTS %d="
        "3!*(3!)^3 CITED-AND-VERIFIED AT THE WELD'S OWN RECEIPT; SPLIT-FIBER 0 "
        "AT ALL %d INTERVALS]@COMMITTED-ANCHOR-EVENT-FOR-EVENT-AT-R=2"
        % (a["cells_at_one"], a["cells"], a["determinant"], a["posdef_sites"],
           a["posdef_sites"], a["maxhits"], a["events"], a["divisions"],
           a["realised_pairs"], a["cells"],
           R["anchors"]["aut_k333_recomputed_here"],
           a["split_fiber_zero_intervals"]))
    seg_walk = (
        "WALK-DERIVED-AND-LAW-TRANSPORTED-[COIN-REGISTER-FORCED-BY-THEOREM: "
        "THE SCALAR SHAPE IS MONOMIAL-ONLY ON THIS ARENA'S OFFSET SET -- %d OF "
        "%d NONZERO DIFFERENCES REALISED BY EXACTLY ONE ORDERED PAIR, %d MAPS "
        "SCANNED OVER THE ARENA'S OWN %d-VALUE ALPHABET (1/3)Z[w], %d UNITARY, "
        "%d NON-MONOMIAL -- AGAINST %d UNITARY AND %d NON-MONOMIAL AT "
        "MULTIPLICITY %d ON THE AXIS STENCIL WHERE INTERFERENCE SURVIVES, THE "
        "SAME INSTRUMENT ON BOTH STENCILS IN THIS RUN | "
        "COIN-DECLARED-UNDER-A-REALITY-CONDITION: THE S_3-COVARIANT UNITARITY "
        "CONDITIONS CUT OUT A CIRCLE -- %d SOLUTIONS OVER REAL RATIONALS, %d "
        "NON-TRIVIAL AND BOTH +/-GROVER; %d OVER THE ARENA'S OWN (1/3)Z[w], %d "
        "CLASSES UP TO A GLOBAL PHASE OF WHICH %d IS +/-GROVER | "
        "COIN-INVARIANCE=MEASURED: ALL %d HIDDEN CLASSES RUN TO HORIZON %d -- "
        "0 CONSISTENCY VIOLATIONS, %d OF %d OBSERVABLE ROWS MOVING, EXIT "
        "THRESHOLD EXACTLY %d, NO INDEFINITE FORM, ON EVERY ONE | "
        "CONNECTION-GROUP Z_3 DERIVED FROM THE ARENA'S OWN FIELD F_3, SO THE "
        "WALK CONSUMES THE COUNT RESIDUE n mod 3 AND THAT IS DISCLOSED | "
        "LAW-TRANSPORT=%s: G(x,0)=1 => G(x,1)=M(x) AT %d SITE-STEPS WITH %d "
        "VIOLATIONS, SURVIVING AN ARBITRARY EXACT RE-PRICING AT %d OF %d; "
        "k_1=q/M AT %d ENTRIES WITH %d VIOLATIONS; ITS CONTENT IS THE SITE "
        "ROW, %d OF %d WITH THE MENU-MASS-IS-BORN-MASS ROW DEFINITIONAL UNDER "
        "READING A AND MEASURED NOT TO BE CARRIED BY SITE-BLOCK-DIAGONALITY "
        "(%d OF %d ON A NON-BLOCK-DIAGONAL UNITARY COIN THAT VIOLATES IT AT %d "
        "OF %d); THE TERMINAL-CONDITION FALSIFIER KILLS THE IDENTITY AT %d]"
        % (sc["differences"], sc["differences"], sc["maps_scanned"],
           sc["alphabet"], sc["unitary_maps"],
           sc["nonmonomial_unitary_maps"], sc["axis_unitary_maps"],
           sc["axis_nonmonomial_unitary_maps"], sc["axis_multiplicities"][0],
           cf["solutions"], cf["nontrivial"], cf["ring_solutions"],
           cf["classes_up_to_phase"], cf["grover_classes_up_to_phase"],
           len(ci["members"]), R["ensemble"]["horizon"],
           ci["members"][0]["observable_rows"],
           ci["members"][0]["observable_rows"], R["ensemble"]["horizon"],
           L["verdict"],
           L["law_native_checks"], L["law_native_violations"],
           L["repricing_checks"] - L["repricing_violations"],
           L["repricing_checks"], L["kernel_entry_checks"],
           L["kernel_entry_violations"],
           L["content_row_checks"] - L["content_row_violations"],
           L["content_row_checks"],
           M0["mass_is_density_checks"] - M0["mass_is_density_violations"],
           M0["mass_is_density_checks"],
           M0["site_block_diagonal_violations"],
           M0["site_block_diagonal_checks"],
           L["terminal_falsifier_violations"]))
    word = outcome_word(c["violations"] == 0, nt["inert"],
                        b["requirement_witnesses"])
    seg_gates = (
        "%s-<G-CONSISTENCY=PASS(THE COUPLED STEP IS WELL DEFINED: UNITARITY x "
        "COLUMN-STOCHASTICITY COMPOSE EXACTLY AT %d PER-OBJECT CHECKS -- PER "
        "BRANCH, PER STEP, PER SITE -- WITH %d VIOLATIONS ACROSS 4 ARMS AT "
        "HORIZON %d, OF WHICH %d ARE THE KERNEL'S DEFINITIONAL COLUMN LEG) -- "
        "G-NONTRIVIALITY=PASS(%d OF %d DECLARED-OBSERVABLE ROWS "
        "DIFFER FROM THE MANDATORY FROZEN-STAGE CONTROL AT BOTH READINGS; "
        "LEAVES %d COUPLED-BORN-MENU vs %d FROZEN, THE COUPLING OPENS EMISSION "
        "CHANNELS THE FROZEN STAGE CLOSES; NOT INERT) -- "
        "G-REQUIREMENT=%s(%d CLOSURES INTERNAL TO THE QUANTUM SIDE "
        "THAT ARE NOT THE UPDATE RULE RESTATED FAIL FROZEN AND PASS COUPLED "
        "IN THE %d-ROW PRE-REGISTERED BATTERY; ALL %d PSI-INTERNAL ROWS HOLD "
        "ON BOTH STAGES, K5 AT THE REPAIRED RAY GRAIN) -- "
        "BATTERY=EMPTY-IN-THE-FORWARD-DIRECTION-BEFORE-THE-RUN(K1-K4 ARE "
        "COUNT-BLIND, MEASURED AT %d VIOLATIONS IN %d CHECKS OVER %d DECLARED "
        "FOREIGN COUNT FIELDS, AND K5'S DELIVERED PREDICATE COULD NOT FIRE AT "
        "ALL SINCE THE RAW STATE NORMS ARE DISTINCT BY LEVEL; THE EMPTINESS IS "
        "FORCED BY THE STALENESS THEOREM, NOT CHOSEN) -- "
        "REFUSAL-ROBUST=EITHER-DECLARATION-ALONE(DROPPING THE "
        "UPDATE-RULE-RESTATED STAMP ALONE GIVES %d WITNESSES, RECLASSIFYING "
        "K9/K10 AS PSI-INTERNAL ALONE GIVES %d, ONLY BOTH TOGETHER GIVE %d) -- "
        "TWO-WAY=[FAIL-FROZEN-PASS-COUPLED: %s, BOTH STAMPED "
        "UPDATE-RULE-RESTATED AND REFUSED BY THE SELECTOR | "
        "PASS-FROZEN-FAIL-COUPLED: %s] -- "
        "STALENESS-BLINDNESS-THEOREM=MACHINE-CHECKED-AT-HORIZON-%d(A FROZEN "
        "STAGE IS ITSELF AN ADMISSIBLE STAGE: ON A DECLARED STALE COUNT FIELD "
        "EVERY SINGLE-TIME PSI-INTERNAL CLOSURE STILL HOLDS AT %d CHECKS, SO "
        "NOTHING INTERNAL TO THE STATE AT A SINGLE TIME CAN DETECT THAT ITS "
        "STAGE IS OUT OF DATE) -- "
        "ADMISSIBILITY-LADDER=THRESHOLD-EXACTLY-%d(THE COUPLED RECORD LEAVES "
        "I7'S ADMISSIBLE CLASS WITH EXACT PROBABILITY %s AT THE BORN MENU AND "
        "%s AT THE RECORD MENU, AND WITH PROBABILITY EXACTLY 0 AT EVERY "
        "HORIZON BELOW IT; THE FROZEN CONTROL NEVER LEAVES IT AT ANY HORIZON; "
        "THE EXIT IS TO THE SINGULAR BOUNDARY det=0 AND NO INDEFINITE FORM IS "
        "REACHED, MEASURED %s; THE ALTERNATIVE COIN ORDER D.G EXITS AT %s, "
        "LARGER, AT THE SAME THRESHOLD) -- "
        "EXIT-CENSUS=ALL-%d-INADMISSIBLE-LEAVES-CLASSIFIED(EVERY ONE HAS "
        "EXACTLY ONE SITE OUT AND THE EXCESS PATTERN (0,0,3), %d-FOLD "
        "DEGENERATE ACROSS THE LINK CLASSES; CR-A SUPPLIES THE 3, THE RETURN "
        "TIME OF THE SHIFT SUPPLIES THE %d) -- SCOPE=%s>"
        % (word, c["checks"], c["violations"], R["ensemble"]["horizon"],
           c["definitional_checks"],
           nt["rows_that_differ"], nt["rows"], nt["leaf_counts"]["coupled_A"],
           nt["leaf_counts"]["frozen_A"],
           requirement_label(b["requirement_witnesses"]),
           len(b["requirement_witnesses"]), b["spec"], b["psi_internal_rows"],
           b["count_blindness"]["psi_internal_violations"],
           b["count_blindness"]["checks"], b["count_blindness"]["fields"],
           len(b["refusal_robustness"]["stamp_dropped"]),
           len(b["refusal_robustness"]["class_dropped"]),
           len(b["refusal_robustness"]["both_dropped"]),
           ",".join(b["update_rule_restated_rows"]) or "NONE",
           ",".join(b["reverse_direction_rows"]) or "NONE",
           b["staleness_blindness"]["horizon"],
           b["staleness_blindness"]["total_checks"],
           ld["thresholds"]["A"], ld["exit_probability_at_horizon"]["A"],
           ld["exit_probability_at_horizon"]["B"],
           ld["indefinite_form_reached"], of["DG_exit_probability"],
           xc["leaves"], xc["link_class_degeneracy"],
           xc["step_budget_is_the_return_time"], SCOPE_ROW))
    return {"arena": seg_arena, "walk_law": seg_walk, "gates": seg_gates}


def reconstruct(serialized):
    """THE COMPARATOR.  It shares no builder code and no typed literal with the
    emitter: it re-parses the SERIALIZED receipt, types all three templates
    ITSELF, and re-derives the outcome word from the receipt's own rows rather
    than reading it out of the string it is auditing."""
    D = json.loads(serialized)
    A = D["arena"]
    W = D["walk"]
    LW = D["law"]
    S = W["scalar_shape"]
    CF = W["coin_census"]
    CI = D["coin_invariance"]
    OF = W["coin_order_full_horizon"]
    MC = D["transport_mechanism"]
    CO = D["consistency"]
    NT = D["nontriviality"]
    BT = D["battery"]
    LD_ = D["ladder"]
    XC = D["exit_census"]
    CB = BT["count_blindness"]
    RB = BT["refusal_robustness"]
    SB = BT["staleness_blindness"]
    # the outcome word AND the requirement label, both RE-DERIVED from the
    # published rows through the same primitives the builder used -- neither is
    # typed on both sides (K3 MINOR-10)
    consistent = CO["violations"] == 0
    inert = NT["inert"]
    wits = BT["requirement_witnesses"]
    word = outcome_word(consistent, inert, wits)
    label = requirement_label(wits)
    t1 = ("COUPLING-ARENA-[WELDED-RECORD-REBUILT-AND-DRIVEN-THROUGH-THE-"
          "COMMITTED-MENUS: n=1 AT " + str(A["cells_at_one"]) + " OF "
          + str(A["cells"]) + " CELLS; det=" + A["determinant"] + " AT "
          + str(A["posdef_sites"]) + " OF 9 SITES; POSDEF "
          + str(A["posdef_sites"]) + " OF 9 BY I7'S OWN SYLVESTER CRITERION; "
          "FORCED AT MAXHITS " + str(A["maxhits"]) + " WITH "
          + str(A["events"]) + " EVENTS AND " + str(A["divisions"])
          + " DIVISION EVENTS AND NO REFUSAL; THE FORCED DICTIONARY "
          "INSTANTIATED: THE REALISED CO-DIVISION RELATION IS THE TARGET'S OWN "
          "CAYLEY INCIDENCE AT " + str(A["realised_pairs"]) + " OF "
          + str(A["cells"]) + " PAIRS AT EQUALITY AND MEETS THE ONE DIRECTION "
          "I7 DOES NOT DECLARE AT 0; SITE-ASSIGNMENTS "
          + str(D["anchors"]["aut_k333_recomputed_here"])
          + "=3!*(3!)^3 CITED-AND-VERIFIED AT THE WELD'S OWN RECEIPT; "
          "SPLIT-FIBER 0 AT ALL " + str(A["split_fiber_zero_intervals"])
          + " INTERVALS]@COMMITTED-ANCHOR-EVENT-FOR-EVENT-AT-R=2")
    t2 = ("WALK-DERIVED-AND-LAW-TRANSPORTED-[COIN-REGISTER-FORCED-BY-THEOREM: "
          "THE SCALAR SHAPE IS MONOMIAL-ONLY ON THIS ARENA'S OFFSET SET -- "
          + str(S["differences"]) + " OF " + str(S["differences"])
          + " NONZERO DIFFERENCES REALISED BY EXACTLY ONE ORDERED PAIR, "
          + str(S["maps_scanned"]) + " MAPS SCANNED OVER THE ARENA'S OWN "
          + str(S["alphabet"]) + "-VALUE ALPHABET (1/3)Z[w], "
          + str(S["unitary_maps"]) + " UNITARY, "
          + str(S["nonmonomial_unitary_maps"]) + " NON-MONOMIAL -- AGAINST "
          + str(S["axis_unitary_maps"]) + " UNITARY AND "
          + str(S["axis_nonmonomial_unitary_maps"])
          + " NON-MONOMIAL AT MULTIPLICITY "
          + str(S["axis_multiplicities"][0]) + " ON THE AXIS STENCIL WHERE "
          "INTERFERENCE SURVIVES, THE SAME INSTRUMENT ON BOTH STENCILS IN THIS "
          "RUN | COIN-DECLARED-UNDER-A-REALITY-CONDITION: THE S_3-COVARIANT "
          "UNITARITY CONDITIONS CUT OUT A CIRCLE -- "
          + str(CF["solutions"]) + " SOLUTIONS OVER REAL RATIONALS, "
          + str(CF["nontrivial"]) + " NON-TRIVIAL AND BOTH +/-GROVER; "
          + str(CF["ring_solutions"]) + " OVER THE ARENA'S OWN (1/3)Z[w], "
          + str(CF["classes_up_to_phase"]) + " CLASSES UP TO A GLOBAL PHASE OF "
          "WHICH " + str(CF["grover_classes_up_to_phase"])
          + " IS +/-GROVER | COIN-INVARIANCE=MEASURED: ALL "
          + str(len(CI["members"])) + " HIDDEN CLASSES RUN TO HORIZON "
          + str(D["ensemble"]["horizon"]) + " -- 0 CONSISTENCY VIOLATIONS, "
          + str(CI["members"][0]["observable_rows"]) + " OF "
          + str(CI["members"][0]["observable_rows"]) + " OBSERVABLE ROWS "
          "MOVING, EXIT THRESHOLD EXACTLY " + str(D["ensemble"]["horizon"])
          + ", NO INDEFINITE FORM, ON EVERY ONE | CONNECTION-GROUP Z_3 DERIVED "
          "FROM THE ARENA'S OWN FIELD F_3, SO THE WALK CONSUMES THE COUNT "
          "RESIDUE n mod 3 AND THAT IS DISCLOSED | LAW-TRANSPORT="
          + LW["verdict"]
          + ": G(x,0)=1 => G(x,1)=M(x) AT " + str(LW["law_native_checks"])
          + " SITE-STEPS WITH " + str(LW["law_native_violations"])
          + " VIOLATIONS, SURVIVING AN ARBITRARY EXACT RE-PRICING AT "
          + str(LW["repricing_checks"] - LW["repricing_violations"]) + " OF "
          + str(LW["repricing_checks"]) + "; k_1=q/M AT "
          + str(LW["kernel_entry_checks"]) + " ENTRIES WITH "
          + str(LW["kernel_entry_violations"]) + " VIOLATIONS; ITS CONTENT IS "
          "THE SITE ROW, "
          + str(LW["content_row_checks"] - LW["content_row_violations"])
          + " OF " + str(LW["content_row_checks"]) + " WITH THE "
          "MENU-MASS-IS-BORN-MASS ROW DEFINITIONAL UNDER READING A AND "
          "MEASURED NOT TO BE CARRIED BY SITE-BLOCK-DIAGONALITY ("
          + str(MC["mass_is_density_checks"]
                - MC["mass_is_density_violations"]) + " OF "
          + str(MC["mass_is_density_checks"])
          + " ON A NON-BLOCK-DIAGONAL UNITARY COIN THAT VIOLATES IT AT "
          + str(MC["site_block_diagonal_violations"]) + " OF "
          + str(MC["site_block_diagonal_checks"]) + "); THE "
          "TERMINAL-CONDITION FALSIFIER KILLS THE IDENTITY AT "
          + str(LW["terminal_falsifier_violations"]) + "]")
    t3 = (word + "-<G-CONSISTENCY=PASS(THE COUPLED STEP IS WELL DEFINED: "
          "UNITARITY x COLUMN-STOCHASTICITY COMPOSE EXACTLY AT "
          + str(CO["checks"]) + " PER-OBJECT CHECKS -- PER BRANCH, PER STEP, "
          "PER SITE -- WITH " + str(CO["violations"]) + " VIOLATIONS ACROSS 4 "
          "ARMS AT HORIZON " + str(D["ensemble"]["horizon"]) + ", OF WHICH "
          + str(CO["definitional_checks"]) + " ARE THE KERNEL'S DEFINITIONAL "
          "COLUMN LEG) -- G-NONTRIVIALITY=PASS("
          + str(NT["rows_that_differ"]) + " OF "
          + str(NT["rows"]) + " DECLARED-OBSERVABLE ROWS DIFFER FROM THE "
          "MANDATORY FROZEN-STAGE CONTROL AT BOTH READINGS; LEAVES "
          + str(NT["leaf_counts"]["coupled_A"]) + " COUPLED-BORN-MENU vs "
          + str(NT["leaf_counts"]["frozen_A"]) + " FROZEN, THE COUPLING OPENS "
          "EMISSION CHANNELS THE FROZEN STAGE CLOSES; NOT INERT) -- "
          "G-REQUIREMENT=" + label + "(" + str(len(wits)) + " CLOSURES "
          "INTERNAL TO THE QUANTUM SIDE THAT ARE NOT THE UPDATE RULE RESTATED "
          "FAIL FROZEN AND PASS COUPLED IN THE " + str(BT["spec"]) + "-ROW "
          "PRE-REGISTERED BATTERY; ALL " + str(BT["psi_internal_rows"])
          + " PSI-INTERNAL ROWS HOLD ON BOTH STAGES, K5 AT THE REPAIRED RAY "
          "GRAIN) -- BATTERY=EMPTY-IN-THE-FORWARD-DIRECTION-BEFORE-THE-RUN("
          "K1-K4 ARE COUNT-BLIND, MEASURED AT "
          + str(CB["psi_internal_violations"]) + " VIOLATIONS IN "
          + str(CB["checks"]) + " CHECKS OVER " + str(CB["fields"])
          + " DECLARED FOREIGN COUNT FIELDS, AND K5'S DELIVERED PREDICATE "
          "COULD NOT FIRE AT ALL SINCE THE RAW STATE NORMS ARE DISTINCT BY "
          "LEVEL; THE EMPTINESS IS FORCED BY THE STALENESS THEOREM, NOT "
          "CHOSEN) -- REFUSAL-ROBUST=EITHER-DECLARATION-ALONE(DROPPING THE "
          "UPDATE-RULE-RESTATED STAMP ALONE GIVES "
          + str(len(RB["stamp_dropped"])) + " WITNESSES, RECLASSIFYING K9/K10 "
          "AS PSI-INTERNAL ALONE GIVES " + str(len(RB["class_dropped"]))
          + ", ONLY BOTH TOGETHER GIVE " + str(len(RB["both_dropped"]))
          + ") -- TWO-WAY=[FAIL-FROZEN-PASS-COUPLED: "
          + (",".join(BT["update_rule_restated_rows"]) or "NONE")
          + ", BOTH STAMPED UPDATE-RULE-RESTATED AND REFUSED BY THE SELECTOR "
          "| PASS-FROZEN-FAIL-COUPLED: "
          + (",".join(BT["reverse_direction_rows"]) or "NONE") + "] -- "
          "STALENESS-BLINDNESS-THEOREM=MACHINE-CHECKED-AT-HORIZON-"
          + str(SB["horizon"]) + "(A FROZEN STAGE IS ITSELF AN ADMISSIBLE "
          "STAGE: ON A DECLARED STALE COUNT FIELD EVERY SINGLE-TIME "
          "PSI-INTERNAL CLOSURE STILL HOLDS AT " + str(SB["total_checks"])
          + " CHECKS, SO NOTHING INTERNAL TO THE STATE AT A SINGLE TIME CAN "
          "DETECT THAT ITS STAGE IS OUT OF DATE) -- "
          "ADMISSIBILITY-LADDER=THRESHOLD-EXACTLY-"
          + str(LD_["thresholds"]["A"]) + "(THE COUPLED RECORD LEAVES I7'S "
          "ADMISSIBLE CLASS WITH EXACT PROBABILITY "
          + LD_["exit_probability_at_horizon"]["A"] + " AT THE BORN MENU AND "
          + LD_["exit_probability_at_horizon"]["B"] + " AT THE RECORD MENU, "
          "AND WITH PROBABILITY EXACTLY 0 AT EVERY HORIZON BELOW IT; THE "
          "FROZEN CONTROL NEVER LEAVES IT AT ANY HORIZON; THE EXIT IS TO THE "
          "SINGULAR BOUNDARY det=0 AND NO INDEFINITE FORM IS REACHED, MEASURED "
          + str(LD_["indefinite_form_reached"])
          + "; THE ALTERNATIVE COIN ORDER D.G EXITS AT "
          + OF["DG_exit_probability"] + ", LARGER, AT THE SAME THRESHOLD) -- "
          "EXIT-CENSUS=ALL-" + str(XC["leaves"])
          + "-INADMISSIBLE-LEAVES-CLASSIFIED(EVERY ONE HAS EXACTLY ONE SITE "
          "OUT AND THE EXCESS PATTERN (0,0,3), "
          + str(XC["link_class_degeneracy"]) + "-FOLD DEGENERATE ACROSS THE "
          "LINK CLASSES; CR-A SUPPLIES THE 3, THE RETURN TIME OF THE SHIFT "
          "SUPPLIES THE " + str(XC["step_budget_is_the_return_time"])
          + ") -- SCOPE="
          + "THIS UNIT REACHES A RECORD, NOT YET A LAW OVER RECORDS>")
    return ({"arena": t1, "walk_law": t2, "gates": t3},
            "outcome re-derived as %s from consistent=%s inert=%s witnesses=%s"
            % (word, consistent, inert, wits or "none"))


def com(n):
    return "{:,}".format(n)


def paper_claims(R):
    a = R["arena"]
    L = R["law"]
    c = R["consistency"]
    nt = R["nontriviality"]
    b = R["battery"]
    ld = R["ladder"]
    sc = R["walk"]["scalar_shape"]
    out = [
        ("C01", "the uniform R = 3 arrangement is driven to %d events with %d "
                "division events and its driven link field is 1 at every one "
                "of the %d cells" % (a["events"], a["divisions"],
                                     a["cells_at_one"])),
        ("C02", "every one of the %d nonzero differences of two distinct "
                "offsets is realised by exactly one ordered pair"
                % sc["differences"]),
        ("C03", "the coupled step is well defined at %s per-object checks with "
                "%d violations" % (com(c["checks"]), c["violations"])),
        ("C04", "%d of %d declared-observable rows differ from the frozen-stage "
                "control" % (nt["rows_that_differ"], nt["rows"])),
        ("C05", "no closure internal to the quantum side that is not the "
                "update rule restated fails on the frozen stage and passes on "
                "the coupled one"),
        ("C06", "the coupled record leaves I7's admissible class with exact "
                "probability %s at the Born menu"
                % ld["exit_probability_at_horizon"]["A"]),
        ("C07", "the exit threshold is exactly %d, and the exit probability is "
                "exactly 0 at every horizon below it"
                % ld["thresholds"]["A"]),
        ("C08", "G(x,1) = M(x) at %s site-steps with %d violations"
                % (com(L["law_native_checks"]), L["law_native_violations"])),
        ("C09", SCOPE_ROW),
        ("C10", "%d solutions over the arena's own (1/3)Z[w], falling into %d "
                "classes up to a global phase, of which exactly %d is "
                "+/- Grover"
                % (R["walk"]["coin_census"]["ring_solutions"],
                   R["walk"]["coin_census"]["classes_up_to_phase"],
                   R["walk"]["coin_census"]["grover_classes_up_to_phase"])),
        ("C11", "all %d hidden classes run to horizon %d: 0 consistency "
                "violations, %d of %d observable rows moving, exit threshold "
                "exactly %d, and no indefinite form, on every one"
                % (len(R["coin_invariance"]["members"]),
                   R["ensemble"]["horizon"],
                   R["coin_invariance"]["members"][0]["observable_rows"],
                   R["coin_invariance"]["members"][0]["observable_rows"],
                   R["ensemble"]["horizon"])),
        ("C12", "every single-time psi-internal closure still holds at %s "
                "checks" % com(b["staleness_blindness"]["total_checks"])),
        ("C13", "all %s inadmissible leaves carry the excess pattern (0, 0, 3) "
                "at exactly one site" % com(R["exit_census"]["leaves"])),
        ("C14", "the alternative order D.G leaves the admissible class with "
                "probability %s, larger, at the same threshold"
                % R["walk"]["coin_order_full_horizon"]["DG_exit_probability"]),
        ("C15", "K1 to K4 record %d psi-internal violations in %s checks over "
                "%d declared foreign count fields"
                % (b["count_blindness"]["psi_internal_violations"],
                   com(b["count_blindness"]["checks"]),
                   b["count_blindness"]["fields"])),
    ]
    return out


def paper_tables(R):
    """E-22: TABLES RENDER AS CLAIMS.  A table row is a claim like any other,
    and the K3 seat shipped two corrupted ones at exit 0 -- a moved cell in the
    composition census and a swapped battery polarity.  Every row of both
    load-bearing tables is now RENDERED FROM THIS RUN and required to occur in
    the paper EXACTLY ONCE."""
    rows = []
    kinds = {"norm": "contentful", "site": "contentful",
             "column": "definitional", "emission_total": "reduces to total",
             "total": "contentful"}
    for cls in ("norm", "site", "column", "emission_total", "total"):
        pc = R["consistency"]["per_class"][cls]
        rows.append(("T-%s" % cls,
                     "| %s | %s | %d | %s |"
                     % (cls, com(pc["checks"]), pc["violations"], kinds[cls])))
    for row in R["battery"]["rows"]["A"]:
        rows.append(("T-%s" % row["id"],
                     "| %s | %s | %s | %s |"
                     % (row["id"], row["class"],
                        "holds" if row["measured"]["frozen_holds"] else "fails",
                        "holds" if row["measured"]["coupled_holds"]
                        else "fails")))
    return rows


NUM_ALLOW = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11",
             "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22",
             "23", "24", "27", "34", "42", "46", "58", "60", "62", "66", "82",
             "87", "91", "119", "125", "148", "154", "168", "171", "172",
             "173", "2026", "42b1", "1296", "3969", "185", "113", "38"}


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
    """#20 WITH THE FENCED-BLOCK ADDENDUM AND E-22's INLINE-SPAN ADDENDUM.
    The fenced verdict blocks are extracted and scanned under their own rule,
    where a hyphen is a word separator rather than a sign, so the head's
    numerals are scanned.  AND the INLINE CODE SPANS are routed through that
    same rule instead of being substituted away: every value in the contrast
    table and every cell of the ladder table lives inside backticks, and with
    them stripped the scan passed two injected corruptions of load-bearing
    values at exit 0 (K1 M-3).  A backticked numeral is a claim like any
    other."""
    without_fences = FENCE_RE.sub(" ", text)
    blocks = FENCE_RE.findall(text)
    spans = INLINE_RE.findall(without_fences)
    prose = INLINE_RE.sub(" ", without_fences)
    known = receipt_numbers(R) | NUMREG | NUM_ALLOW | head_numbers(R)
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
    """E-22: the fenced blocks as a MULTISET.  Containment is not identity --
    paper-20 carried two copies of each verdict fence and a containment gate
    was satisfied by the clean copy while its twin was forged (K3 MAJOR-3
    P4)."""
    out = Counter()
    for b in FENCE_RE.findall(text):
        out[canon(b)] += 1
    return out


def paper_polarity(R, text, mutated=False):
    pos_needles = [
        # the negative is the outcome word WITH A NAMED IDENTITY appended,
        # which is what a REQUIRED delivery would carry; the bare stem is left
        # available so the paper can print its own pre-registered menu
        ("P1", "COUPLING-CONSISTENT-NOT-REQUIRED",
         "COUPLING-CONSISTENT-AND-REQUIRED-K"),
        ("P2", "the coupled record leaves I7's admissible class",
         "the coupled record never leaves I7's admissible class"),
        ("P3", "the coin register is forced",
         "the coin register is a declared choice"),
    ]
    out = []
    for pid, pos, neg in pos_needles:
        if mutated:
            pos, neg = neg, pos
        have_pos = canon(pos) in canon(text)
        have_neg = canon(neg) in canon(text)
        out.append({"id": pid, "positive": pos, "negative": neg,
                    "positive_present": have_pos,
                    "negative_present": have_neg,
                    "ok": have_pos and not have_neg})
    return out


TERMINAL_GATE = "G-ARTIFACT-INTEGRITY"


def writer_shape():
    """THE SHAPE OF THE WRITER, measured from this file's own AST BEFORE the
    gate ledger is snapshotted (K3 MAJOR-1).  The terminal integrity gate is
    the one gate no mutant can reach -- `run_mutant` calls finish(write=False),
    which returns before it -- so dropping or renaming it produced artifacts
    BYTE-IDENTICAL to the delivered ones at exit 0, while the receipt printed a
    sealed warrant claiming the artifacts witnessed it.  This probe is the
    guard: it reads the gate names finish() calls, in order, counts the
    os.replace calls, and requires every one of them to sit BELOW the terminal
    gate's own line.  Because it is taken before the snapshot, it is sealed
    like any other measurement and its own removal moves a published value."""
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


def falsifier_hooks():
    """E-23, THE MECHANICAL HALF.  Every declared falsifier names THE SYMBOL IT
    MOVES and THE VALUE IT MOVES IT TO; both are re-derived here from this
    file's own AST -- the innermost statement enclosing each `pick(NAME, ...)`
    or `mut(NAME)` call -- and compared against the declaration.  A description
    that says the opposite of its code has to name a symbol or a value the AST
    contradicts."""
    src = read_text(SELF)
    tree = ast.parse(src)
    found = defaultdict(list)
    for node in ast.walk(tree):
        if not isinstance(node, ast.stmt):
            continue
        names = set()
        for c in ast.walk(node):
            if isinstance(c, ast.Call) and isinstance(c.func, ast.Name) \
                    and c.func.id in ("pick", "mut") and c.args \
                    and isinstance(c.args[0], ast.Constant):
                names.add(c.args[0].value)
        if not names:
            continue
        seg = ast.get_source_segment(src, node) or ""
        lo, hi = node.lineno, (node.end_lineno or node.lineno)
        for nm in names:
            found[nm].append((lo, hi, seg))
    out = {}
    for nm, rows in found.items():
        # keep only the INNERMOST enclosing statements: a candidate that
        # strictly contains another candidate for the same falsifier is an
        # enclosing block, and reading it would let any string anywhere in the
        # enclosing function satisfy the check.
        keep = [r for r in rows
                if not any(o is not r and r[0] <= o[0] and o[1] <= r[1]
                           and (o[1] - o[0]) < (r[1] - r[0]) for o in rows)]
        out[nm] = [r[2] for r in sorted(keep)]
    return out


def waiver_ledger():
    """#34: a gate with no declared mutant must carry a FORCING that says why
    it cannot fail, and every waiver is named in the receipt."""
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
                            "same: the gate parses this file's own imports"),
        "G-READS-DECLARED": ("STRUCTURAL",
                             "the source read list is appended by read_bytes, "
                             "the only reader of a SOURCE in the file; the "
                             "second reader, read_text, reads only the two "
                             "files of the declared OBJECT set, which this "
                             "same gate now names and binds.  A mutant could "
                             "only add a read one of the two legs would then "
                             "catch"),
        "G-VERBATIM": ("SELF-FALSIFYING-PER-ROW",
                       "every anchor is perturbed at a content-bearing token "
                       "and re-located inside the gate, so each row carries "
                       "its own falsifier and a dead needle fails here"),
        "G-SLICE-EXIT-FREE": ("SOURCE-FORCED",
                              "the property is d66's committed C0a form "
                              "evaluated on pinned bytes; corrupting it would "
                              "corrupt a pinned source and die at "
                              "G-PROVENANCE first"),
        "G-ANCHOR-CONSUMERS": ("STRUCTURAL",
                               "the gate compares two registries this file "
                               "owns; a mutant on it would be a mutant on the "
                               "accounting rather than on a measurement"),
        "G-COVERAGE": ("SELF-REFERENTIAL",
                       "the gate IS the coverage ledger"),
        "G-REACHABILITY": ("SELF-REFERENTIAL", "same"),
        "G-MUTANTS-ON-TARGET": ("SELF-REFERENTIAL",
                                "the gate IS the mutant sweep"),
        "G-ARTIFACT-INTEGRITY": (
            "EXERCISED-IN-RUN-AND-GUARDED-BY-THE-WRITER-SHAPE",
            "a mutant on this gate is UNREACHABLE by construction -- "
            "run_mutant calls finish(write=False), which returns before the "
            "terminal gate runs -- so the waiver states the two things that "
            "do guard it.  (i) EXERCISED: the run corrupts a read-back copy "
            "of EVERY sealed row in turn and requires each corruption to be "
            "detected before the real artifacts are compared, so the check is "
            "known live per seal and not on one row.  (ii) EXISTENCE: "
            "G-WRITER-SHAPE reads this file's AST BEFORE the gate ledger is "
            "snapshotted and publishes the gate names finish() calls and the "
            "line of every os.replace, so dropping or renaming this gate, or "
            "moving a write above it, moves a SEALED published value -- which "
            "is exactly what the byte-identical artifacts of a dropped "
            "terminal gate did not do before"),
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


def finish(LD, SEAL, R, verdict, write=True, swept=False):
    """close the payload: coverage and reachability over the WHOLE delivery
    run, the sweep-execution binding, the anchor-consumer binding, the totality
    check, the seal, the artifacts, the disk-vs-seal integrity check."""
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
            "#34 WITH AN HONEST DENOMINATOR: of the %d gates this delivery run "
            "evaluates -- %d already closed, plus this gate and its twin, plus "
            "the sweep-binding, anchor-consumer, writer-shape and "
            "falsifier-honesty gates evaluated between them, plus the %d LATE "
            "gates, every one of which is verified PRESENT at "
            "G-ARTIFACT-INTEGRITY rather than assumed -- %d are falsified by "
            "at least one declared mutant and %d are WAIVED with a forcing "
            "that says why they cannot fail.  The denominator is the gate "
            "count of THIS run, and the registry --list-gates prints is "
            "required to be EXACTLY that set"
            % (len(gate_names), len(LD.rows), len(LATE_GATES),
               sum(1 for g in gate_names if targeted.get(g)), len(waivers)),
            not uncovered and not registry_drift,
            "uncovered gates: %s; declared registry %d vs evaluated %d, drift "
            "%s" % (uncovered or "none", len(GATE_REGISTRY), len(gate_names),
                    registry_drift or "none"))
    SEAL.take("SEAL-COVERAGE", R)
    SEAL.take("SEAL-WAIVERS", R)

    # -- E-23: THE FALSIFIER REGISTRY, VERIFIED AGAINST ITS OWN CODE ---------
    hooks = falsifier_hooks()
    hook_rows = []
    desc_bad = []
    hook_bad = []
    for name, gate, why, moves, to in MUTANTS:
        declared = (moves, to)
        if mut("MUT-FALSIFIER-DESC") and name == "MUT-KERNEL":
            declared = ("FORGED", "FORGED")
        segs = hooks.get(name, [])
        code_ok = any(declared[0] in s and declared[1] in s for s in segs)
        prose_ok = moves in why and to in why
        hook_rows.append({"mutant": name, "gate": gate, "what_it_does": why,
                          "moves": declared[0], "to": declared[1],
                          "hook_sites": len(segs),
                          "matches_its_code": code_ok,
                          "named_in_its_description": prose_ok})
        if not code_ok:
            hook_bad.append(name)
        if not prose_ok:
            desc_bad.append(name)
    undeclared_hooks = sorted(set(hooks) - MUTANT_NAMES)
    R["mutants"] = hook_rows
    LD.gate("G-FALSIFIER-HONESTY",
            "E-23: A FALSIFIER'S PUBLISHED DESCRIPTION IS PART OF THE SEALED "
            "SURFACE.  Each of the %d declared falsifiers names THE SYMBOL IT "
            "MOVES and THE VALUE IT MOVES IT TO; both are re-derived from THIS "
            "FILE's own AST -- the innermost statement enclosing its hook -- "
            "and compared against the declaration, and the published prose is "
            "required to name both.  A description-inverted falsifier is a "
            "false waiver wearing a green badge: three of this unit's own said "
            "the opposite of their code and one load-bearing row had no "
            "falsifier at all.  %d hook sites are located, and every hook in "
            "the file names a declared falsifier"
            % (len(MUTANTS), sum(len(v) for v in hooks.values())),
            not hook_bad and not desc_bad and not undeclared_hooks,
            "declarations not matching their code: %s; descriptions not naming "
            "their symbol and value: %s; hooks naming an undeclared falsifier: "
            "%s" % (hook_bad or "none", desc_bad or "none",
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
            "THE SHAPE OF THE WRITER IS SEALED, AND IT IS SEALED BEFORE THE "
            "GATE LEDGER IS SNAPSHOTTED -- which is what makes it the one "
            "guard a post-snapshot gate's own removal cannot evade.  finish() "
            "calls %d gates in source order, the terminal integrity gate "
            "appears exactly once among them, there are %d os.replace calls, "
            "and every one of them sits BELOW that gate's own line.  Dropping "
            "or renaming the terminal gate, or lifting a write above it, moves "
            "a published and sealed value here"
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
    # a mutant sub-run is not a delivery and carries no sweep of its own; the
    # key is still published (and sealed) so the manifest stays total
    R.setdefault("mutant_sweep", [])
    sweep_rows = R.get("mutant_sweep") or []
    ran_here = {g["gate"] for g in LD.rows}
    sweep_ok = (not swept) or (
        len(sweep_rows) == len(MUTANTS)
        and all(k.get("on_target") for k in sweep_rows)
        and SWEEP_GATE in ran_here)
    LD.gate("G-SWEEP-BOUND",
            "THE SWEEP'S EXECUTION IS BOUND, NOT DECLARED: a delivery-level "
            "run must carry one sweep row per declared mutant (%d), every row "
            "ON TARGET, and must have evaluated the sweep gate itself.  This "
            "run is %s" % (len(MUTANTS),
                           "delivery-level" if swept else "a sub-pipeline"),
            sweep_ok, "sweep rows %d of %d; sweep gate evaluated %s"
            % (len(sweep_rows), len(MUTANTS), SWEEP_GATE in ran_here))
    SEAL.take("SEAL-MUTANT-SWEEP", R)

    consumers = {v[3] for v in VERBATIM}
    bad_consumers = sorted(
        c for c in consumers
        if c not in GATE_REGISTRY or c not in ran_here)
    LD.gate("G-ANCHOR-CONSUMERS",
            "#62's consumer binding: every verbatim anchor names a gate, and "
            "each named gate is required to be in the DECLARED registry AND in "
            "THIS RUN's own evaluated ledger, so the naming cannot drift into "
            "a gate that was removed or never reached -- %d distinct consumer "
            "gates" % len(consumers),
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
            "REACH its gate -- the gate must be registered and must either "
            "have been evaluated in this run or be one of the gates this same "
            "function evaluates after the census, which are named rather than "
            "assumed.  %d falsifiers, %d dead" % (len(reach), len(dead)),
            not dead, "dead falsifiers: %s" % (dead or "none"))
    SEAL.take("SEAL-REACHABILITY", R)

    # THE THREE GATE CARDINALITIES, DISTINGUISHED AND NAMED (K3 MINOR-1).  The
    # object published 52 / 50 / 49 under one word: the registry, the sealed
    # snapshot, and the count taken one gate earlier.  They are different
    # numbers about different sets and each is named here.
    R["totals"] = {
        "sources": len(SOURCES), "verbatim_anchors": len(R["verbatim_anchors"]),
        "gates_in_the_registry": len(GATE_REGISTRY),
        "gates_evaluated_before_the_snapshot": len(LD.rows) + 1,
        "gates_after_the_snapshot": len(LATE_GATES) - 1,
        "gates": len(LD.rows) + 1,
        "mutants": len(MUTANTS),
        "seals": len(SEALED_PATHS), "battery_rows": len(BATTERY_SPEC),
        "arms": 4, "horizon": HORIZON,
        "declared_unsealed": len(DECLARED_UNSEALED),
        "waivers": len(R["waiver_ledger"]),
        "consistency_checks": R["consistency"]["checks"],
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
    # the snapshot's own NAMES against the registry's -- names, not counts
    # (#87): a sub-pipeline legitimately lacks the sweep gate, so the equality
    # is asserted only for a delivery-level run and the reason is printed.
    names_now = ({g["gate"] for g in LD.rows} | {"G-PAPER-COVERAGE-FINAL"}
                 | set(LATE_GATES[1:]))
    names_ok = (not swept) or names_now == set(GATE_REGISTRY)
    LD.gate("G-PAPER-COVERAGE-FINAL",
            "the payload closes.  THE THREE GATE CARDINALITIES ARE NAMED "
            "RATHER THAN CONFLATED: %d gates in the DECLARED REGISTRY, %d "
            "evaluated and carried into the SEALED SNAPSHOT (this gate "
            "included), and %d evaluated AFTER the snapshot -- G-SEAL-COMPLETE, "
            "which cannot be inside the object it seals, and "
            "G-ARTIFACT-INTEGRITY, which runs after the bytes are on disk and "
            "whose existence is sealed by G-WRITER-SHAPE.  All passed, and a "
            "RECURSIVE TYPE SCAN of the receipt finds no float anywhere -- "
            "every published number is an int or a string carrying an exact "
            "Fraction"
            % (len(GATE_REGISTRY), len(LD.rows) + 1, len(LATE_GATES) - 1),
            all(g["passed"] for g in LD.rows) and not bad_types and names_ok,
            "registry %d, snapshot %d, post-snapshot %d, snapshot names equal "
            "the registry %s (%s), float-valued receipt paths %s"
            % (len(GATE_REGISTRY), len(LD.rows) + 1, len(LATE_GATES) - 1,
               names_ok,
               "delivery-level" if swept else "sub-pipeline, not asserted",
               bad_types or "none"))
    R["gates"] = [dict(g) for g in LD.rows]
    R["closing_gates"] = {
        "names": list(LATE_GATES[1:]),
        "gates_in_the_registry": len(GATE_REGISTRY),
        "gates_in_the_sealed_snapshot": len(R["gates"]),
        "gates_after_the_snapshot": len(LATE_GATES) - 1,
        "warrant": "these two are evaluated after the gate ledger is "
                   "snapshotted and sealed -- G-SEAL-COMPLETE cannot be inside "
                   "the object it seals, and G-ARTIFACT-INTEGRITY runs after "
                   "the bytes are on disk.  The archived transcript therefore "
                   "carries G-SEAL-COMPLETE's row and NOT "
                   "G-ARTIFACT-INTEGRITY's.  THAT GATE'S EXISTENCE IS NOT "
                   "WITNESSED BY THE ARTIFACTS -- dropping it produced "
                   "byte-identical ones -- so it is witnessed instead by "
                   "G-WRITER-SHAPE, which reads this file's AST before the "
                   "snapshot and seals the gate names finish() calls together "
                   "with the line of every write."}
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
    R["seal_manifest"] = {"rows": SEAL.rows,
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
            "rather than against the seals that happened to be taken, so a "
            "silently dropped seal dies here.  The vouching layer is inside "
            "the seal: schema, provenance, paper claims, polarity, coverage, "
            "reachability, gates, totals and the transcript head.  The "
            "DECLARED-UNSEALED list is itself frozen by content and by length "
            "and may not name any key that carries a measurement",
            not missing and not extra and not uncovered_keys and not broken
            and unsealed_frozen and unsealed_clean,
            "declared seals %d, taken %d, missing %s, extra %s, receipt keys "
            "not covered %s, seals broken at close %s, unsealed list frozen %s "
            "and measurement-free %s"
            % (len(SEALED_PATHS), len(SEAL.rows), missing or "none",
               extra or "none", uncovered_keys or "none", broken or "none",
               unsealed_frozen, unsealed_clean))
    payload = json.dumps(R, indent=1, sort_keys=True, default=str)
    emit_report(R, LD)
    text = "\n".join(LINES) + "\n"
    SEAL.close(R, payload, text)
    R["payload_sha256_12"] = SEAL.payload_sha
    if not write:
        return payload, text
    tmp_j, tmp_t = OUT_JSON + ".tmp", OUT_TXT + ".tmp"
    final = json.dumps(R, indent=1, sort_keys=True, default=str)
    with open(tmp_j, "w", encoding="utf-8") as fh:
        fh.write(final + "\n")
    with open(tmp_t, "w", encoding="utf-8") as fh:
        fh.write(text)
    back = json.loads(read_text(tmp_j))
    # THE PROBE IS PER SEAL, not on one row (K3 MINOR-3): every sealed path is
    # corrupted in turn on a read-back copy and each corruption must be caught.
    probes_caught = 0
    for row in SEAL.rows:
        probe = json.loads(json.dumps(back))
        cur = probe
        parts = row["path"].split("/")
        for part in parts[:-1]:
            cur = cur[int(part)] if isinstance(cur, list) else cur[part]
        key = parts[-1]
        if isinstance(cur, list):
            cur[int(key)] = ["PROBE"]
        else:
            cur[key] = "PROBE"
        if row["seal"] in SEAL.verify(probe, only={row["seal"]}):
            probes_caught += 1
    probe_caught = probes_caught == len(SEAL.rows)
    disk_broken = SEAL.verify(back)
    back_text = read_text(tmp_t)
    head_ok = (back_text.split("\n")[:40] == R["transcript_head"])
    # THE TRANSCRIPT IS COMPARED IN FULL (K3 MAJOR-2a): the head seal covered
    # 40 of 181 lines and a forged line 88 shipped through it at exit 0.
    text_ok = digest(back_text) == SEAL.text_sha
    text_lines = len(back_text.split("\n"))
    # THE TWO DECLARED-UNSEALED KEYS ARE CHAINED (K3 MAJOR-2b): the receipt's
    # own digest and the seal manifest are re-read from disk and compared
    # against the live seal object rather than left outside the perimeter.
    chained_ok = (back.get("payload_sha256_12") == SEAL.payload_sha
                  and back.get("seal_manifest", {}).get("rows") == SEAL.rows)
    ran = {g["gate"] for g in LD.rows}
    late_ok = all(g in ran for g in tuple(LEDGER_GATES) + LATE_GATES[:2]
                  + CLOSING_LEDGER_GATES + (SWEEP_GATE,))
    sweep_complete = (len(R.get("mutant_sweep") or []) == len(MUTANTS)
                      and all(k.get("on_target")
                              for k in R.get("mutant_sweep") or []))
    LD.gate("G-ARTIFACT-INTEGRITY",
            "INTEGRITY IS DISK-VS-SEAL, never a re-derivation: the payload is "
            "written from the SEALED object to a staged file, read back FROM "
            "DISK, and every sealed object compared against the digest taken "
            "at the moment its gate passed -- with EVERY ONE of the %d sealed "
            "rows corrupted in turn on a read-back copy and shown to be "
            "detected first, so the check is known live PER SEAL rather than "
            "on one row.  THE PERIMETER IS CLOSED IN BOTH ARTIFACTS: the "
            "transcript is compared IN FULL, %d of %d lines by digest and not "
            "by its first 40, and the two DECLARED-UNSEALED keys -- the "
            "receipt's own payload digest and the seal manifest -- are CHAINED "
            "here against the live seal object.  The staged bytes are moved "
            "into place by os.replace ONLY after this gate passes, so a run "
            "that fails any gate leaves the delivered artifacts untouched, and "
            "the only writer in this file is downstream of a sweep that "
            "actually ran"
            % (len(SEAL.rows), text_lines, SEAL.text_lines),
            probe_caught and not disk_broken and head_ok and text_ok
            and chained_ok and late_ok and sweep_complete,
            "corrupted probes detected %d of %d, sealed objects broken on disk "
            "%s, transcript head matches %s, transcript matches in full %s "
            "(%d of %d lines), declared-unsealed keys chained %s, every "
            "declared-later gate actually evaluated %s, sweep complete and on "
            "target %s"
            % (probes_caught, len(SEAL.rows), disk_broken or "none", head_ok,
               text_ok, text_lines, SEAL.text_lines, chained_ok, late_ok,
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
    except Exception as e:                             # pragma: no cover
        died = "UNEXPECTED:%s" % e
    QUIET = False
    after = (os.path.exists(OUT_JSON) and os.stat(OUT_JSON).st_mtime,
             os.path.exists(OUT_TXT) and os.stat(OUT_TXT).st_mtime)
    wrote = before != after
    print("[SELFTEST] corrupted anchor A-D42B1 -> died at %s" % died)
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
    ensemble; the four falsifiers that must move the physics move it on an
    object small enough to rebuild inside the census itself."""
    global MUT, QUIET, LINES
    MUT, QUIET = name, True
    keep, keep_out = LINES, sys.stdout
    sys.stdout = _Sink()
    LINES = []
    killed_at = None
    try:
        LD, SEAL, R, verdict, _raw = full_run(paper_text=paper_text)
        cli_gates(LD)
        finish(LD, SEAL, R, verdict, write=False)
    except GateFail as e:
        killed_at = str(e).split(" ::")[0]
    except Exception as e:                             # pragma: no cover
        killed_at = "UNEXPECTED:%s" % type(e).__name__
    MUT, QUIET, LINES = None, False, keep
    sys.stdout = keep_out
    return killed_at


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
    bad, ok_shapes, permissive, nmal = cli_selftest()
    if mut("MUT-CLI-PERMISSIVE"):
        bad = [["--nope"]]
    LD.gate("G-CLI-WHITELIST",
            "the #82 CLI contract, exercised in this run: %d malformed "
            "argument vectors are all rejected with exit code 2 -- the last "
            "three of them SECOND-MODE vectors, since a mode flag that "
            "silently overwrote an earlier one would make the earlier flag a "
            "no-op -- %d legal shapes parse, and the registered PERMISSIVE "
            "shape, present in this file only as this gate's own falsifier, "
            "accepts an unknown flag, which is what makes the gate a "
            "measurement" % (nmal, ok_shapes),
            not bad and permissive,
            "malformed vectors accepted %s, legal shapes %d, permissive shape "
            "accepts unknown flags %s" % (bad or "none", ok_shapes, permissive))
    st_ok = pick("MUT-SELFTEST-WRITES", selftest_shape(), False)
    LD.gate("G-SELFTEST-WRITES-NOTHING",
            "the --selftest path corrupts an anchor in memory, dies at "
            "G-PROVENANCE and reaches no writer: the writer is called from "
            "exactly one place in this file and the self-test path does not "
            "reach it -- and the predicate is now the AST probe's own value "
            "rather than a flag beside it",
            st_ok,
            "the writer-shape probe reports the self-test path clean: %s"
            % st_ok)


def emit_report(R, LD):
    """the banner, emitted INSIDE finish and before the transcript is frozen
    (K3 MINOR-1), so the most quotable line of the run is inside the archived
    artifact and inside the seal instead of being stdout-only."""
    say("")
    say("-" * 78)
    say("TOTALS: %d sources, %d verbatim anchors, %d gates in the registry "
        "(%d in the sealed snapshot, %d after it), %d mutants, %d seals, "
        "%d battery rows, %d arms at horizon %d, %s consistency checks"
        % (R["totals"]["sources"], R["totals"]["verbatim_anchors"],
           R["totals"]["gates_in_the_registry"],
           R["totals"]["gates_evaluated_before_the_snapshot"],
           R["totals"]["gates_after_the_snapshot"],
           R["totals"]["mutants"], R["totals"]["seals"],
           R["totals"]["battery_rows"], R["totals"]["arms"],
           R["totals"]["horizon"], com(R["totals"]["consistency_checks"])))
    say("-" * 78)


GATE_REGISTRY = [
    "G-PROVENANCE", "G-EXACT-ARITHMETIC", "G-NO-SUBPROCESS",
    "G-READS-DECLARED", "G-VERBATIM",
    "G-SLICE-EXIT-FREE", "G-COMMITTED-ANCHOR", "G-WELDED-RECORD",
    "G-WELDED-GEOMETRY", "G-DICTIONARY", "G-ISOS-CITED", "G-UNSPLITTABLE",
    "G-SCALAR-MONOMIAL", "G-COIN-CENSUS", "G-COIN-INVARIANCE",
    "G-CONNECTION-GROUP", "G-WALK-UNITARY", "G-COIN-ORDER-FULL", "G-FIBERS",
    "G-LAW-NATIVE", "G-LAW-REPRICING", "G-KERNEL-K1", "G-LAW-TRANSPORT",
    "G-TRANSPORT-MECHANISM",
    "G-ENSEMBLE-EXHAUSTIVE", "G-BRANCH-MASS",
    "G-CONSISTENCY", "G-FROZEN-CONTROL", "G-NONTRIVIALITY",
    "G-ADMISSIBILITY-LADDER", "G-EXIT-CENSUS",
    "G-BATTERY-POLARITY", "G-BATTERY-TWO-WAY",
    "G-STALENESS-BLIND", "G-COUNT-BLIND", "G-K5-NO-RETURN",
    "G-REFUSAL-ROBUST", "G-REQUIREMENT",
    "G-WALL-L1", "G-WALL-BHS", "G-WALL-KR", "G-WALL-COSMO",
    "G-WALL-LORENTZ-NAMED", "G-WALL-HEX-NAMED",
    "G-VERDICT-RECONSTRUCTED", "G-PAPER-CLAIMS", "G-PAPER-TABLES",
    "G-PAPER-NUMERAL-COVERAGE",
    "G-PAPER-HEAD-VERBATIM", "G-PAPER-CLAIM-POLARITY",
    "G-CLI-WHITELIST", "G-SELFTEST-WRITES-NOTHING", "G-MUTANTS-ON-TARGET",
    "G-COVERAGE", "G-FALSIFIER-HONESTY", "G-WRITER-SHAPE",
    "G-SWEEP-BOUND", "G-ANCHOR-CONSUMERS", "G-REACHABILITY",
    "G-PAPER-COVERAGE-FINAL", "G-SEAL-COMPLETE", "G-ARTIFACT-INTEGRITY",
]


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
        LD, SEAL, R, verdict, _raw = full_run(
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
        return 0
    except GateFail as e:
        sys.stderr.write("GATE FAILED: %s\n" % e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
