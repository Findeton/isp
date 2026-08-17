#!/usr/bin/env python3
"""ARITY-16 (paper-50) -- THE a-AXIS AT THE SECOND ARENA: n = 16.

QUESTION (pin `v15/note-arity16-pin.md`, sha256-12 1dac6a35ddc5, v15 ledger
#43).  ARITY (paper-44) measured the event-size axis at the nine-actor arena
and left two theorems and one conditional behind: the modulus theorem
nL/gcd(nL, n) = L, the a = 2 obstruction-vanishing theorem, and the a = q
conditional whose antecedent no unit of the corpus ever registered.  This
unit runs all three at the ONE other arena the corpus owns -- AG(2, 4),
sixteen actors, the field of order four -- which is the first arena at which
the field characteristic and the field order are different numbers.

THE SHARPENED REGISTRATION (v15 ledger #11, quoted in the paper and anchored
here from the frozen pin): the additive group of AG(2, 4) is C2^4 with
subgroup orders 1, 2, 4, 8, 16 -- ALL the divisors of 16 -- so n = 16 does
NOT separate divisibility from abstract-subgroup availability; it separates
divisibility from F4-LINEAR-subspace cosets, whose sizes are 1, 4, 16.  The
unit therefore PRE-REGISTERS WHICH notion of subgroup it means:

  PRIMARY (pre-registered): "subgroup" = F4-linear subspace of the
      translation group; coset sizes 1 | 4 | 16.
  DISCLOSED ALTERNATIVE (reported beside, never merged): abstract subgroup
      of C2^4; coset sizes 1 | 2 | 4 | 8 | 16.

Both readings run at every reading-sensitive row, and their DISAGREEMENT is
a result of this unit, never an average.

THE FOUR LEGS, per the pin:
  (1) the a = q conditional at q = 4: the parent's five-principle census at
      all sixteen candidate event sizes, under both readings;
  (2) the modulus theorem at the new arena: the budget-reading ladder
      measured directly, with mod-a-iff-a=L probed where a and L differ;
  (3) the a-only transport: the parent's six statements and seven numerals
      at matched arities, with a = 3 at n = 16 stamped PURE EXTENSION FAMILY
      (3 does not divide 16, one idle actor minimum; the committed grammar's
      refusal IS the measurement and is never patched);
  (4) the obstruction form C(a,2) - maxcut(K_a) = 0 | 1 | 2 | 4, VERIFIED at
      the new arena's realised seam census and not re-derived.

ARITHMETIC.  Exact only: Python integers throughout.  No floats anywhere; an
AST scan of this file and a recursive type scan of the emitted receipt are
gates, and the builtin hash -- whose value is a per-process accident under
PYTHONHASHSEED -- is banned by its own AST leg and rehearsed on a planted
sample.

RUNTIME INPUTS (#46 / #91).  The files listed in SOURCES are read, all
hash-pinned by this unit's frozen declaration, plus exactly one file read as
the OBJECT UNDER TEST -- this unit's own paper, whose digest and repository
path are sealed into the receipt and printed into the transcript.  The
programme ledger is NOT among them: it is a live document under concurrent
revision, and #46 forbids a runtime read of mutable repository state, so the
ledger's sharpened registration enters through the FROZEN pin's own text.
No subprocess of any kind is invoked; every open the process performs is
recorded, inside the repository and outside it alike; and the read set is
compared again inside the promotion path after the seal legs.

TEMPLATE (E-25 ... E-33, and the TPL-2 revision).  The nine families are
implemented HERE, not imported, and every one is EXERCISED on this unit's
own objects (G-TEMPLATE-EXERCISED): seals at gate time verified against the
serialised bytes and again from the staged file; the transcript parsed back
and bound line by line; walls as voice-normalised regexes with positive legs
and licence legs, NEG-guarded with re-assertion and other-clause exclusions;
anchors readable only through a recording accessor; claims keyed by table in
both directions at exact occurrence counts; referents bound per occurrence
over prose only, digit and spelled alike, with no reflexive pair licensed;
no vouching builder types a numeral; every falsifier names the object it
must move and the harness digests that object before and after; the head is
a positional field list re-derived by a comparator sharing no code and no
typed literal with the builder.
"""

import ast
import hashlib
import json
import math
import os
import re
import sys
from collections import Counter
from itertools import combinations, product

sys.setrecursionlimit(100000)

SELF = os.path.abspath(__file__)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(SELF)))
OUT_TXT = os.path.join(os.path.dirname(SELF), "arity16_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "arity16_receipt.json")

SCHEMA = "isp/v15/arity16-second-arena/1"
PAPER_REL = "v15/paper-50-arity16.md"
# The object under test is resolved off THIS FILE, never off the process's
# working directory (the ARITY #22 lesson: a CWD-relative default makes the
# declared path and the recorded path disagree wherever the run is launched).
PAPER_PATH = os.path.join(REPO, PAPER_REL)

# ===========================================================================
# SECTION 0.  THE FROZEN DECLARATION (RUNBOOK section 15: the arena is data)
# ===========================================================================

SOURCES = [
    ("A-PIN", "v15/note-arity16-pin.md", "1dac6a35ddc5",
     "THIS UNIT'S PIN (v15 ledger #43): the question, the pre-registered "
     "F4-linear reading and the disclosed abstract alternative, the four "
     "legs, the outcome names and the walls.  The ledger #11 sharpened "
     "registration enters through this FROZEN text, because the ledger "
     "itself is mutable repository state and may not be a runtime input."),
    ("A-PARENT", "v15/paper-44-arity.md", "0d677a4cbe97",
     "ARITY / PAPER-44 (terminal, v15 ledger #39): the a-only rule and the "
     "two-level aggregate discipline, the modulus theorem and its 320-pair "
     "sweep, the a = q conditional, the obstruction closed form, and the "
     "packing rule this unit transports to sixteen actors."),
    ("A-PARENTREC", "v15/code/arity_receipt.json", "e90a41eed544",
     "ARITY's COMMITTED RECEIPT: the seven parent numerals, the statement "
     "and numeral word tallies, the rule-relative aggregates and the n = 9 "
     "substrate rows, every one read by PATH and consumed by a named gate, "
     "so no parent value is ever typed here."),
    ("A-NDEP", "v14/paper-39-ndep.md", "e2293b8c3858",
     "NDEP / PAPER-39 (terminal, v14 ledger #352): the committed n = 16 "
     "substrate -- the declared window, the failed coset-menu hypothesis at "
     "q = 4, the two subgroup readings named and not chosen, and the "
     "characteristic-vs-q separation this arena exists to exploit."),
    ("A-NDEPREC", "v14/code/ndep_receipt.json", "29216cea946f",
     "NDEP's COMMITTED RECEIPT: every n = 16 substrate count this unit "
     "consumes -- the class tuples, the covering tuples, the route-window "
     "census, the crystallization and floor rows, the ladder, the subgroup "
     "counts and the out-of-scope grouping census constant -- read by PATH "
     "and consumed by the fidelity gate that must pass before any new row "
     "runs."),
]

# PATH-VALUE ANCHORS (#20).  (id, source, json path, expected value,
# consumer gate).  A path drift that silently substituted another committed
# number dies here even when no number moves.  List indices are part of a
# path (the parent's receipt keeps its transport rows as lists).
PATH_ANCHORS = [
    # ---- NDEP's n = 16 window, consumed by the fidelity gate ----
    ("P-N16-N", "A-NDEPREC", "n16_window/n", 16, "G-CONSTRUCTOR-FIDELITY"),
    ("P-N16-Q", "A-NDEPREC", "n16_window/q", 4, "G-CONSTRUCTOR-FIDELITY"),
    ("P-N16-L", "A-NDEPREC", "n16_window/L", 4, "G-CONSTRUCTOR-FIDELITY"),
    ("P-N16-CELLS", "A-NDEPREC", "n16_window/cells", 64,
     "G-CONSTRUCTOR-FIDELITY"),
    ("P-N16-CLS", "A-NDEPREC", "n16_window/class_tuples", 256,
     "G-CONSTRUCTOR-FIDELITY"),
    ("P-N16-COV", "A-NDEPREC", "n16_window/covering", 24,
     "G-CONSTRUCTOR-FIDELITY"),
    ("P-N16-CMP", "A-NDEPREC", "n16_window/route_window_comparisons",
     505920, "G-CONSTRUCTOR-FIDELITY"),
    ("P-N16-MIS", "A-NDEPREC", "n16_window/route_window_mismatches", 0,
     "G-CONSTRUCTOR-FIDELITY"),
    ("P-N16-POS", "A-NDEPREC", "n16_window/route_window_positive", 49536,
     "G-CONSTRUCTOR-FIDELITY"),
    ("P-N16-VAC", "A-NDEPREC",
     "n16_window/route_window_positive_at_the_empty_prefix", 29760,
     "G-CONSTRUCTOR-FIDELITY"),
    ("P-N16-WIN", "A-NDEPREC", "n16_window/route_window_size", 1240,
     "G-CONSTRUCTOR-FIDELITY"),
    ("P-N16-CRY", "A-NDEPREC", "n16_window/crystallization/7", 24,
     "G-CONSTRUCTOR-FIDELITY"),
    ("P-N16-FLR", "A-NDEPREC", "n16_window/attained_floor/6", 24,
     "G-CONSTRUCTOR-FIDELITY"),
    ("P-N16-CNT", "A-NDEPREC", "n16_window/counting_floor", 4,
     "G-CONSTRUCTOR-FIDELITY"),
    ("P-N16-SUBS", "A-NDEPREC", "n16_window/subgroups_of_T", 67,
     "G-READINGS"),
    ("P-N16-F4", "A-NDEPREC", "n16_window/f_q_subspaces", 7, "G-READINGS"),
    ("P-N16-GEN", "A-NDEPREC", "n16_window/translations_generated/4/"
     "generated", 8, "G-ARENA16"),
    ("P-N16-WIT", "A-NDEPREC", "n16_window/saturation_witness_incidence",
     48, "G-SUBSTRATE-CENSUS"),
    ("P-N16-LAD4", "A-NDEPREC", "n16_window/homogeneous_ladder/3/achievable",
     True, "G-LAW4-LADDER16"),
    ("P-N16-LAD8", "A-NDEPREC", "n16_window/homogeneous_ladder/7/achievable",
     True, "G-LAW4-LADDER16"),
    ("P-N16-LAD5", "A-NDEPREC", "n16_window/homogeneous_ladder/4/achievable",
     False, "G-LAW4-LADDER16"),
    # ---- the parent's seven numerals, consumed by the transport table ----
    ("P-PV-MENU", "A-PARENTREC", "transport/numerals/0/parent_value", 6,
     "G-AGGREGATE16"),
    ("P-PL-MENU", "A-PARENTREC", "transport/numerals/0/law", "menu",
     "G-AGGREGATE16"),
    ("P-PV-RUNG", "A-PARENTREC", "transport/numerals/1/parent_value", 3,
     "G-AGGREGATE16"),
    ("P-PL-RUNG", "A-PARENTREC", "transport/numerals/1/law", "ladder",
     "G-AGGREGATE16"),
    ("P-PV-SCHED", "A-PARENTREC", "transport/numerals/2/parent_value", 5,
     "G-AGGREGATE16"),
    ("P-PV-FLOOR", "A-PARENTREC", "transport/numerals/3/parent_value", 4,
     "G-AGGREGATE16"),
    ("P-PV-OFF", "A-PARENTREC", "transport/numerals/4/parent_value", 1,
     "G-AGGREGATE16"),
    ("P-PV-NONU", "A-PARENTREC", "transport/numerals/5/parent_value", 4,
     "G-AGGREGATE16"),
    ("P-PV-FORCED", "A-PARENTREC", "transport/numerals/6/parent_value", 1,
     "G-AGGREGATE16"),
    # ---- the parent's per-numeral words, for the both-arena table ----
    ("P-PW-0", "A-PARENTREC", "transport/numerals/0/word", "NEEDS-3",
     "G-AGGREGATE16"),
    ("P-PW-1", "A-PARENTREC", "transport/numerals/1/word", "NEEDS-3",
     "G-AGGREGATE16"),
    ("P-PW-2", "A-PARENTREC", "transport/numerals/2/word", "BREAKS",
     "G-AGGREGATE16"),
    ("P-PW-3", "A-PARENTREC", "transport/numerals/3/word", "BREAKS",
     "G-AGGREGATE16"),
    ("P-PW-4", "A-PARENTREC", "transport/numerals/4/word", "BREAKS",
     "G-AGGREGATE16"),
    ("P-PW-5", "A-PARENTREC", "transport/numerals/5/word", "BREAKS",
     "G-AGGREGATE16"),
    ("P-PW-6", "A-PARENTREC", "transport/numerals/6/word", "BREAKS",
     "G-AGGREGATE16"),
    # ---- the parent's aggregates, for the both-arena table ----
    ("P-AGG-SL", "A-PARENTREC", "transport/statement_words/LAW-IN-A", 4,
     "G-AGGREGATE16"),
    ("P-AGG-SB", "A-PARENTREC", "transport/statement_words/BREAKS", 2,
     "G-AGGREGATE16"),
    ("P-AGG-NN", "A-PARENTREC", "transport/numeral_words/NEEDS-3", 2,
     "G-AGGREGATE16"),
    ("P-AGG-NB", "A-PARENTREC", "transport/numeral_words/BREAKS", 5,
     "G-AGGREGATE16"),
    ("P-AGG-CF", "A-PARENTREC", "transport/aggregate_under_each_rule/"
     "the section-9 closed form/LAW-IN-A", 1, "G-AGGREGATE16"),
    # ---- the parent's n = 9 substrate, for the both-arena table ----
    ("P-SUB2-SAT", "A-PARENTREC", "substrate/0/saturating_LITERAL", 0,
     "G-SUBSTRATE-CENSUS"),
    ("P-SUB3-SAT", "A-PARENTREC", "substrate/1/saturating_LITERAL", 36,
     "G-SUBSTRATE-CENSUS"),
    ("P-SUB4-SAT", "A-PARENTREC", "substrate/2/saturating_LITERAL", 81,
     "G-SUBSTRATE-CENSUS"),
    ("P-SUB5-SAT", "A-PARENTREC", "substrate/3/saturating_LITERAL", 0,
     "G-SUBSTRATE-CENSUS"),
    ("P-SUB2-G", "A-PARENTREC", "substrate/0/groupings", 945,
     "G-SUBSTRATE-CENSUS"),
    ("P-SUB3-G", "A-PARENTREC", "substrate/1/groupings", 280,
     "G-SUBSTRATE-CENSUS"),
    ("P-SUB4-G", "A-PARENTREC", "substrate/2/groupings", 315,
     "G-SUBSTRATE-CENSUS"),
    ("P-SUB5-G", "A-PARENTREC", "substrate/3/groupings", 126,
     "G-SUBSTRATE-CENSUS"),
    # ---- the parent's per-arity forced-inside column, for the sec2 row ----
    ("P-SEC2-F2", "A-PARENTREC", "law6_sec2/rows/0/forced_inside_bound", 0,
     "G-LAW6-SEC2-16"),
    ("P-SEC2-F3", "A-PARENTREC", "law6_sec2/rows/1/forced_inside_bound", 1,
     "G-LAW6-SEC2-16"),
    ("P-SEC2-F4", "A-PARENTREC", "law6_sec2/rows/2/forced_inside_bound", 2,
     "G-LAW6-SEC2-16"),
    ("P-SEC2-F5", "A-PARENTREC", "law6_sec2/rows/3/forced_inside_bound", 4,
     "G-LAW6-SEC2-16"),
]

# VERBATIM-TEXT ANCHORS (#62 as amended): each binds QUOTE FIDELITY and each
# is CONSUMED by a named gate that takes a value out of the located text and
# compares it with a measurement.
VERBATIM = [
    ("V-REGISTRATION", "A-PIN",
     "the additive group of AG(2,4) is C2^4 with subgroup orders 1,2,4,8,16 "
     "= ALL divisors of 16",
     "G-READINGS",
     "The sharpened registration's arithmetic half, from the frozen pin. "
     "The consumer parses the five orders out of the quotation and requires "
     "them to equal BOTH the measured abstract-subgroup orders and the "
     "measured divisors of the actor count, which is the coincidence the "
     "registration names."),
    ("V-LINEAR", "A-PIN",
     "it separates divisibility from F4-LINEAR-subspace cosets (sizes "
     "1,4,16); the successor must pre-register WHICH \"subgroup\" it means",
     "G-READINGS",
     "The registration's instruction half.  The consumer parses the three "
     "linear coset sizes and requires them to equal the measured F4-linear "
     "subspace orders, and the unit's pre-registered primary reading is "
     "checked to be the linear one by name."),
    ("V-SUCCESSOR", "A-PARENT",
     "The registered successor is ARITY AT SIXTEEN ACTORS, and the "
     "registration has to say which notion of subgroup it means, because "
     "the obvious one does not separate anything.",
     "G-READINGS",
     "The parent's own registration of this unit.  The consumer requires "
     "the phrase naming the obligation -- which notion of subgroup -- and "
     "the run discharges it by declaring both notions as data."),
    ("V-TWOLEVEL", "A-PARENT",
     "A law's STATEMENT is LAW-IN-A when the parent's theorem, as stated, "
     "holds at every feasible event size",
     "G-AGGREGATE16",
     "The parent's two-level engraving in its own words; the consumer reads "
     "the slot name out of the quotation and requires the aggregate to "
     "declare that slot by name and publish a second, differently named "
     "slot beside it."),
    ("V-MODULUS", "A-PARENT",
     "the modulus is nL/gcd(nL, n) = L at every arena, verified at 320 "
     "declared arena pairs",
     "G-MODULUS-THEOREM",
     "The parent's theorem and the size of its own sweep.  The consumer "
     "parses the 320 out of the quotation, re-runs the identity at the same "
     "declared pair list, and requires this arena's budget rows to be "
     "instances of it."),
    ("V-CONDITIONAL", "A-PARENT",
     "IF every round must be a complete partition of the actors into proper "
     "nontrivial coset blocks of the arena's translation group THEN the "
     "event size is the field order",
     "G-CONDITIONAL",
     "The parent's licensed conditional.  The consumer evaluates its "
     "antecedent at this arena under BOTH pre-registered readings of the "
     "coset clause and publishes what each selects; the disagreement "
     "between them is the verdict, never an average."),
    ("V-OBSTRUCTION", "A-PARENT",
     "That complement reads 0, 1, 2 and 4.",
     "G-LAW6-SEC2-16",
     "The parent's obstruction values at a = 2 through 5.  The consumer "
     "parses all four numerals and requires each to equal the MEASURED "
     "minimum of within-sector pairs over this arena's own seam-spanning "
     "census at that arity -- verified at the realised census, not "
     "re-derived."),
    ("V-PACKING", "A-PARENT",
     "a round at event size a is a MAXIMAL PACKING of the 9 sites by "
     "disjoint a-blocks, with the remainder IDLE",
     "G-PACKING-EXTENDS16",
     "The parent's own packing rule, transported with its site count moved "
     "to this arena's.  The consumer parses the site numeral out of the "
     "quotation, requires it to be the parent's nine, and requires this "
     "unit's rule to be the same sentence at sixteen."),
    ("V-SQRT16", "A-NDEP",
     "the q = 4 plane is the first point at which the characteristic and "
     "the square root part company",
     "G-ARENA16",
     "NDEP's own statement of why this arena discriminates.  The consumer "
     "requires the measured characteristic to differ from the measured "
     "field order here, which is the separation the sentence names."),
    ("V-HYPOTHESIS", "A-NDEP",
     "every canonical direction representative has its first coordinate in "
     "the prime subfield, so the four declared translations span a subgroup "
     "of order 8 inside a group of order 16",
     "G-ARENA16",
     "NDEP's measured reason the coset-menu hypothesis fails at q = 4.  The "
     "consumer parses the two orders and requires them to equal this unit's "
     "own measured span of the declared links and translation-group order."),
    ("V-UNSCORED", "A-NDEP",
     "the q = 4 row of the transport table is carried and left unscored by "
     "the procedure itself",
     "G-LAW3-MENU16",
     "NDEP's precedent for the menu at this arena: the closed form's "
     "hypothesis fails, so its row was carried unscored there.  The "
     "consumer requires this unit's menu scoring to cite the precedent "
     "while now MEASURING the survivor census NDEP could not reach."),
    ("V-OUTOFSCOPE", "A-NDEPREC",
     "the full saturating census at q = 4 needs the 2,627,625 groupings of "
     "sixteen sites into four blocks of four and is out of scope",
     "G-SUBSTRATE-CENSUS",
     "NDEP's own declaration of the window it could not close.  The "
     "consumer parses the grouping constant out of the quotation and "
     "requires it to equal this unit's dynamic-programming census total at "
     "a = 4, which is the window closing."),
    ("V-N16WINDOW", "A-NDEP",
     "At sixteen actors the bound reads 4, and the smallest event subset "
     "that forces identity has size 6 at every one of the 24 covering class "
     "tuples",
     "G-LAW2-SHARPENED16",
     "NDEP's committed crystallization row at this arena.  The consumer "
     "parses the counting bound, the floor and the tuple count and requires "
     "all three to equal this unit's re-derivations."),
]

# THE ARITY WINDOW AND THE DECLARED CAPS, before anything is measured.
ARITIES = (2, 3, 4, 5)
PARENT_ARITY = 3            # the parent's numerals live at a = 3 (n = 9)
COMMITTED_ARITY = 4         # the committed event size AT THIS ARENA (a = q)
IDLE_ARITIES = (3, 5)       # a does not divide 16: idle remainder forced
LADDER_RMAX = 8             # NDEP's own declared bound at n = 16
SAT_SAMPLE_CAP = 4000       # canonical saturating-round sample per arity
COVER_NODE_CAP = 400000     # exact-cover witness search node cap
FLOOR_NODE_CAP = 3000000    # floor-witness backtracking node cap
PREFIX_WINDOW = 2000        # object-level packing-extends prefix window
THEOREM_N_MAX = 40          # the parent's own modulus-theorem sweep
THEOREM_L_MAX = 8
M_FORK = (2, 3, 4)          # the declared coin-modulus fork at this arena

READINGS = ("F4-LINEAR", "ABSTRACT")
PRIMARY_READING = "F4-LINEAR"

# THE SPELLED CARDINALS (rendered, never typed), with the parent's declared
# exclusion and its reason.
SPELLED = ("zero", "one", "two", "three", "four", "five", "six", "seven",
           "eight", "nine", "ten", "eleven", "twelve", "thirteen",
           "fourteen", "fifteen", "sixteen")
SPELLED_VALUE = {w: i for i, w in enumerate(SPELLED)}
SPELLED_EXCLUDED = {"one": "the English article and pronoun, which carries "
                           "a count only by accident of spelling"}
SPELLED_SCANNED = tuple(w for w in SPELLED if w not in SPELLED_EXCLUDED)

# THE FIDELITY PRE-REGISTRATION, SEALED.  The rows the constructor-fidelity
# gate answers for, frozen with their own digest; the values are read from
# NDEP's committed receipt at the declared paths and typed nowhere.
FIDELITY_PREREG = (("class_tuples", "P-N16-CLS"),
                   ("covering_tuples", "P-N16-COV"),
                   ("route_comparisons", "P-N16-CMP"),
                   ("route_mismatches", "P-N16-MIS"),
                   ("route_positive", "P-N16-POS"),
                   ("route_positive_empty_prefix", "P-N16-VAC"),
                   ("permutation_window", "P-N16-WIN"),
                   ("crystallization_at_seven", "P-N16-CRY"),
                   ("floor_at_six", "P-N16-FLR"),
                   ("counting_floor", "P-N16-CNT"))
FIDELITY_PREREG_DIGEST = "8bf058fb97b73ccd"

# PRE-REGISTERED OUTCOMES WITH FEASIBILITY (#299, argued against NDEP's
# committed n = 16 window and the parent's sealed tables).
PREREGISTERED = [
    ("A16-CONDITIONAL-READING-DEPENDENT",
     "the two pre-registered readings of the coset clause select different "
     "event-size sets, so the parent's conditional has no reading-free "
     "content at this arena",
     "REACHABLE, and the sharpened registration's expected case: the "
     "abstract lattice offers proper nontrivial orders 2, 4 and 8 while the "
     "linear lattice offers 4 alone, and both lattices are enumerated by "
     "closure from the arena's own addition, so the two antecedent sets can "
     "differ and the census measures whether they do."),
    ("A16-CONDITIONAL-TRACKS-THE-FIELD",
     "under the pre-registered F4-linear reading the conditional's "
     "antecedent admits the field order alone among proper nontrivial "
     "sizes, so the F4 branch selects a = q = 4",
     "REACHABLE: the measured linear subspace orders are 1, 4 and 16, so "
     "properness removes the trivial two and leaves one candidate; the "
     "branch line fires exactly when the measured lattice says so."),
    ("A16-MODULUS-THEOREM-HOLDS",
     "every measured rung at this arena is a multiple of the declared link "
     "count, the arena instance of nL/gcd(nL, n) = L reads 4, and mod-a "
     "appears at no row where the event size and the link count differ",
     "REACHABLE: budget-saturating pools are non-empty at four transport "
     "arities by the substrate census, and witness search runs at every "
     "one, so a rung off the multiples of L had live rows to appear at."),
    ("A16-MODULUS-THEOREM-FALSIFIED-AT-AG(2, 4)",
     "some measured rung is not a multiple of the declared link count, or "
     "mod-a appears at a row where a differs from L",
     "REACHABLE: the a = 2 and a = 9 pools are non-empty and their witness "
     "searches found rungs, so a rung at 2 or at 9 -- either of which "
     "would falsify -- had a live route; the measured rungs decide."),
    ("A16-TRANSPORT-READING-RELATIVE",
     "the two-level transport table's words differ between the two "
     "pre-registered readings at some row",
     "REACHABLE: the forcing and naming windows are coset windows, and the "
     "two readings admit different window objects (five linear rounds "
     "against thirty-five abstract ones at a = 4), so any row whose "
     "measured value depends on the window can move between readings."),
    ("LAW-IN-A",
     "the parent's theorem holds at every feasible arity (statement), or "
     "the declared a-only reading reproduces the measurement at every "
     "feasible arity and some feasible arity separates it from the "
     "constant reading (numeral)",
     "REACHABLE: the obstruction column 0 | 1 | 2 | 4 is measured at four "
     "feasible arities and the closed-form rule can reproduce it."),
    ("NEEDS-3",
     "the parent's numeral does not move across the feasible arities, so "
     "it is carried by a coordinate this axis holds still and not by the "
     "event size",
     "REACHABLE: the menu census is a-inert by construction and the ladder "
     "rung is measured at more than one arity, so a constant column is "
     "live; whether it equals the PARENT'S value at the new arena is what "
     "the words decide."),
    ("BREAKS",
     "neither the constant reading nor the declared a-only reading "
     "reproduces the measurement at some feasible arity (numeral), or the "
     "parent's theorem is evaluable at a feasible arity and false there "
     "(statement)",
     "REACHABLE: the certified floors at n = 16 read double digits at the "
     "smallest arity against a parent value of 4, which no constant and no "
     "single offset rule can match."),
    ("INFEASIBLE-CARRIED",
     "the row's own hypothesis fails at an arity, so the row is carried "
     "and never scored (#34)",
     "REACHABLE: a = 3 divides neither the actor count nor any coset "
     "order under either reading, so its corpus rows have no object."),
    ("A-INERT-BY-CONSTRUCTION",
     "the leg reads the partition and the arena and never a history, so "
     "its value cannot move with the arity and the row is a disclosure",
     "REACHABLE: the menu's geometry leg is evaluated once and consumed at "
     "every arity."),
    ("NOT-FOUND-WITHIN-CAP",
     "a witness search ended at its declared cap without a witness, so "
     "the row is published as capped and never as empty",
     "REACHABLE: the exact-cover ladder searches at a = 3, 5, 6 and 7 run "
     "under declared sample and node caps against pools of hundreds of "
     "thousands, so a cap-out is live."),
    ("REFUSED-BY-THE-COMMITTED-GRAMMAR",
     "the committed grammar cannot build the object at all -- the event "
     "size divides neither the actor count nor any coset order under the "
     "reading -- and the refusal is itself the measurement, never patched",
     "REACHABLE: 16 mod 3 is 1 and both measured lattices carry no "
     "order-3 member, so every a = 3 corpus row refuses."),
]

# THE SEGMENT-LEVEL PRE-REGISTRATION (#299 as extended).
SEGMENT_PREREG = [
    ("SEG-CONDITIONAL", "A16-CONDITIONAL-READING-DEPENDENT",
     "A16-CONDITIONAL-READING-FREE", True,
     "CONTINGENT IN ITS CENSUS HALF: which principles admit which sizes is "
     "measured at sixteen candidate event sizes under both readings, and "
     "the selector census could have come out with the same selections "
     "under both readings, which is the complement.  The two lattices' "
     "order sets themselves are forced by closure arithmetic once the "
     "readings are posed, and that half is published as a declaration's "
     "consequence, not as a finding."),
    ("SEG-MODULUS", "A16-MODULUS-THEOREM-HOLDS",
     "A16-MODULUS-THEOREM-FALSIFIED", True,
     "CONTINGENT: rungs were found at three event sizes including two "
     "where the event size and the link count differ, and any rung off "
     "the multiples of the declared link count would have returned the "
     "complement."),
    ("SEG-TRANSPORT", "A16-TRANSPORT-READING-RELATIVE",
     "A16-TRANSPORT-READING-FREE", True,
     "CONTINGENT: the statement and numeral words are recomputed under "
     "both readings' windows, and identical word tables would have "
     "returned the complement."),
    ("SEG-SUBSTRATE", "THE-BUDGET-RETURNS-AT-TWO",
     "THE-BUDGET-STAYS-EMPTY-AT-TWO", True,
     "CONTINGENT: the parent's a = 2 budget-saturating count is zero and "
     "this arena's is measured by the census; a zero here would have "
     "returned the complement.  What is NOT contingent is the idle "
     "remainder at a = 3 and a = 5, which is the window's own arithmetic "
     "and is published as a declaration's consequence."),
    ("SEG-NAMING", "LAW-IN-A", "BREAKS", True,
     "CONTINGENT: route A and route B are compared as element sets at "
     "every prefix of every window history at both arities, and a single "
     "mismatch returns the complement."),
    ("SEG-CRYSTALLIZATION", "BREAKS", "LAW-IN-A", True,
     "CONTINGENT: the certified floors and the schedule sweeps are "
     "measured at this arena, and a floor column matching either declared "
     "reading of the parent's numeral would have returned the complement."),
    ("SEG-MENU", "BREAKS", "LAW-IN-A", True,
     "CONTINGENT: the survivor census is a closure enumeration that could "
     "have returned exactly the coset partitions of either reading, which "
     "is the complement; it returned neither reading's set."),
    ("SEG-FORCING", "READING-SPLIT", "READING-FREE", True,
     "CONTINGENT: the non-unique census is measured per round under both "
     "readings' windows, and identical verdicts would have returned the "
     "complement."),
    ("SEG-SEC2", "OBSTRUCTION-FORM-VERIFIED", "OBSTRUCTION-FORM-FAILS",
     True,
     "CONTINGENT: the four measured minima are census results over the "
     "realised union, and any minimum off the parent's closed form would "
     "have returned the complement."),
    ("SEG-SCOPE", "SCOPE", "OUT-OF-SCOPE", False,
     "NOT-CONTINGENT: the scope line reports the declared windows, caps "
     "and bounds, none of which is a measurement outcome."),
]

PREREG_DIGEST = "11b1643b69886a97"
SEGMENT_PREREG_DIGEST = "31d6122d8c31a82e"

# THE DECLARED UNIFORM a-ONLY RULE -- the parent's own, unchanged: the
# corpus's a-only quantity C(a, 2) offset by the constant that reproduces
# the parent's numeral at the parent's arity.  The same rule for every
# numeral; the alternates are published beside it.
def pairs_of_event(a):
    return math.comb(a, 2)


def t_a_reading(parent_value, a):
    return pairs_of_event(a) + (parent_value - pairs_of_event(PARENT_ARITY))


def t_a_alt_identity(parent_value, a):
    return a + (parent_value - PARENT_ARITY)


def t_a_alt_blocks(parent_value, a):
    # blocks per round AT THIS ARENA: floor(16 / a), offset at the parent's
    # arity read the parent's way (its own arena's blocks, n = 9 over 3).
    return (N16 // a) + (parent_value - 3)


def forced_inside_closed_form(a):
    return math.comb(a, 2) - (a * a) // 4


def t_a_alt_maxcut(parent_value, a):
    return forced_inside_closed_form(a) + (
        parent_value - forced_inside_closed_form(PARENT_ARITY))


ALT_RULES = (("a-itself", t_a_alt_identity),
             ("blocks-per-round", t_a_alt_blocks),
             ("the parent's closed form", t_a_alt_maxcut))
MONOTONE_ALTS = ("a-itself", "blocks-per-round")

WORDS = ("LAW-IN-A", "NEEDS-3", "BREAKS")

N16 = 16

# THE TWO SCOPE GROUNDS, carried exactly as the parent carries them: the
# idle-remainder ground (a does not divide the actor count) and the
# off-committed-size ground (the event size is not this arena's committed
# four).  Every scored word carries the stamp its rows earn.
EXTENSION_SCOPE = "WITHIN THE DECLARED EXTENSION FAMILY"


def extension_arities():
    return [x for x in ARITIES if N16 % x]


def off_committed_arities():
    return [x for x in ARITIES if x != COMMITTED_ARITY]


# THE DECLARED ARENA (section 15: declared-arena-as-data).
def arena_declaration():
    return [
        ("boundary",
         "the %d (site, link) cells of one copy of AG(2, q) at q = %d with "
         "the declared links %s"
         % (NC, A.q, ", ".join(str(l) for l in A.LINKS))),
        ("held fixed",
         "n = %d actors, q = %d, the field and its characteristic %d, the "
         "%d parallel classes, L = %d declared links, %d cells"
         % (A.n, A.q, A.characteristic, len(A.CLASSES), A.L, NC)),
        ("moved",
         "a, the number of actors in one division event: %s"
         % ", ".join(str(x) for x in ARITIES)),
        ("pre-registered reading",
         "PRIMARY: a subgroup is an F4-LINEAR SUBSPACE of the translation "
         "group, with measured coset sizes %s.  DISCLOSED ALTERNATIVE, "
         "reported beside and never merged: an ABSTRACT subgroup of C2^4, "
         "with measured coset sizes %s.  Their disagreement is a result"
         % (", ".join(str(x) for x in sorted({len(H) for H in F4SUBS})),
            ", ".join(str(x) for x in sorted({len(H) for H in SUBS})))),
        ("declaration",
         "THE PACKING RULE, the parent's own and not the committed "
         "grammar's: a round at event size a is a MAXIMAL PACKING of the "
         "%d sites by disjoint a-blocks, with the remainder IDLE. It "
         "reduces to the committed constructor exactly where a divides the "
         "actor count, and everywhere else it is an EXTENSION of the "
         "theory, not a reading of it" % A.n),
        ("extension family",
         "the arities at which the packing rule leaves an idle remainder: "
         "%s. The committed grammar's refusal there is itself the "
         "measurement and is never patched; and every arity other than %d "
         "is additionally off this arena's committed event size"
         % (", ".join(str(x) for x in extension_arities()), COMMITTED_ARITY)),
        ("family",
         "the maximal a-packings of the %d sites at each arity, the coset "
         "windows both readings admit, and the covering tuples NDEP's own "
         "driver builds from them" % A.n),
        ("law",
         "the naming theorem, the crystallization pair, the coset menu, "
         "the ladder modulus and its theorem, the division-forcing thesis, "
         "SEC-2's counting theorem, and the a = q conditional"),
        ("state",
         "the participation-signature partition, the record n_l(x), and "
         "the coupled walk's one-step operator at both coin orders under "
         "the declared modulus fork %s" % (", ".join(str(m) for m in M_FORK))),
        ("arena axes",
         "the arity a and the reading of the word subgroup (F4-LINEAR "
         "primary, ABSTRACT disclosed); both are swept and both are "
         "published"),
        ("provenance",
         "%d sources read at pinned shas; %d path-value anchors; %d "
         "verbatim-text anchors, each consumed by a named gate"
         % (len(SOURCES), len(PATH_ANCHORS), len(VERBATIM))),
    ]
# ===========================================================================
# SECTION 1.  THE TEMPLATE MECHANISMS (E-25 ... E-33), IMPLEMENTED HERE
#
# Copied rather than imported, per v14/TEMPLATE.md section 1: importing would
# make another unit's file a runtime input, and this unit must reproduce byte
# for byte off-tree with no repository present.  Every family is EXERCISED on
# this unit's own objects below -- the TPL-2 prohibition on carried-not-used
# families is a gate here (G-TEMPLATE-EXERCISED), not a claim.
# ===========================================================================

class GateFail(Exception):
    pass


class CliError(Exception):
    pass


MUTANT = None


def mut(name):
    return MUTANT == name


def pick(name, normal, corrupted):
    return corrupted if mut(name) else normal


MEMO = {}
MEMO_HITS = Counter()


def memo(key, fn):
    """Deterministic memoisation across the run and its nested falsifier
    runs.  EVERY key carries the mutant flags the computation depends on, so
    a recipe can never be served a clean cached answer; the cache's hit and
    miss counts are published and the falsifier harness exercises the miss
    path at every keyed value (RUNBOOK section 14: a zero-hit cache gate is
    vacuous, and a cache that ignores the mutant is worse)."""
    if key in MEMO:
        MEMO_HITS[("hit",) + key[:1]] += 1
        return MEMO[key]
    MEMO_HITS[("miss",) + key[:1]] += 1
    MEMO[key] = fn()
    return MEMO[key]


def digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, default=str,
                   ensure_ascii=False).encode("utf-8")).hexdigest()[:16]


def bytes_digest(b):
    return hashlib.sha256(b).hexdigest()[:16]


def mdstrip(s):
    """#125 normalisation: markdown blockquote / list prefixes and emphasis
    removed before any text gate matches."""
    out = []
    for ln in s.split("\n"):
        t = ln.lstrip()
        while t[:1] in (">",) or re.match(r"^([-*+]|\d+\.)\s", t):
            t = re.sub(r"^([-*+]|\d+\.)\s", "", t[1:] if t[:1] == ">" else t)
            t = t.lstrip()
        out.append(t)
    t = "\n".join(out)
    t = t.replace("**", "").replace("`", "")
    return t


def canon(s):
    """whitespace folded, markdown stripped, ASCII-folded."""
    t = mdstrip(s)
    t = t.replace("—", "--").replace("–", "-")
    t = t.replace("‘", "'").replace("’", "'")
    t = t.replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", t).strip()


class Ledger:
    """A CHAINED ledger (family b): every row digests its predecessor, so a
    row cannot be inserted, dropped or reordered without moving the head."""

    def __init__(self):
        self.rows = []
        self.head = "0" * 16

    def gate(self, gid, ok, statement, evidence):
        row = {"n": len(self.rows) + 1, "gate": gid, "statement": statement,
               "evidence": evidence, "passed": bool(ok)}
        row["prev"] = self.head
        row["row_digest"] = digest(row)
        self.head = hashlib.sha256(
            (self.head + row["row_digest"]).encode("utf-8")).hexdigest()[:16]
        self.rows.append(row)
        TR.row(gid, bool(ok), self.evidence_line(evidence))
        if not ok:
            raise GateFail("%s :: %s" % (gid, self.evidence_line(evidence)))

    @staticmethod
    def evidence_line(evidence):
        return json.dumps(evidence, sort_keys=True, default=str,
                          ensure_ascii=False)

    def names(self):
        return [r["gate"] for r in self.rows]

    def index_of(self, gid):
        for r in self.rows:
            if r["gate"] == gid:
                return r["n"]
        return None

    def recompute_chain(self):
        head = "0" * 16
        for r in self.rows:
            body = {k: r[k] for k in
                    ("n", "gate", "statement", "evidence", "passed")}
            body["prev"] = head
            if digest(body) != r["row_digest"]:
                raise GateFail("T-LEDGER-CHAIN :: row %d moved" % r["n"])
            head = hashlib.sha256(
                (head + r["row_digest"]).encode("utf-8")).hexdigest()[:16]
        return head


class Transcript:
    """Family (b): the transcript is parsed BACK out of the text that will be
    promoted and reconciled with the ledger as a multiset, evidence
    included."""

    LINE = re.compile(r"^\s*\[(PASS|FAIL)\] (\S+) :: (.*)$")

    def __init__(self):
        self.lines = []

    def say(self, text=""):
        self.lines.append(text)

    def row(self, gid, ok, evidence):
        self.lines.append("  [%s] %s :: %s"
                          % ("PASS" if ok else "FAIL", gid, evidence))

    def text(self):
        return "\n".join(self.lines) + "\n"

    def parse(self, text=None):
        src = self.text() if text is None else text
        out = Counter()
        for line in src.splitlines():
            m = self.LINE.match(line)
            if m:
                out[(m.group(2), m.group(1) == "PASS", m.group(3))] += 1
        return out

    def bind(self, ledger, text=None):
        want = Counter((r["gate"], r["passed"],
                        Ledger.evidence_line(r["evidence"]))
                       for r in ledger.rows)
        got = self.parse(text)
        missing = sorted(k[0] for k in (want - got).elements())
        stray = sorted(k[0] for k in (got - want).elements())
        if missing or stray:
            raise GateFail("T-TRANSCRIPT-BOUND :: missing %s stray %s"
                           % (missing, stray))
        if sum(got.values()) != len(ledger.rows):
            raise GateFail("T-TRANSCRIPT-BOUND :: %d lines against %d rows"
                           % (sum(got.values()), len(ledger.rows)))
        return bytes_digest((self.text() if text is None
                             else text).encode("utf-8"))

    def bind_narrative(self, text, allowed):
        """THE NON-GATE LINES, BOUND.  The multiset reconciliation above sees
        only `[PASS|FAIL] gate :: evidence` rows, so a forged summary line
        promoted beside them is certified by the transcript digest and bound
        by nothing.  Every line that is not a gate row must therefore be a
        member of the DECLARED narrative -- the banner, the blank, the verdict
        marker, a head segment the comparator already bound, the object
        digest line or the ledger-head line -- and the check is by
        membership, so a line the run did not declare cannot appear at all."""
        stray = []
        for line in text.splitlines():
            if self.LINE.match(line):
                continue
            if line.strip() == "":
                continue
            if line not in allowed:
                stray.append(line[:90])
        if stray:
            raise GateFail("T-TRANSCRIPT-BOUND :: undeclared narrative "
                           "line(s): %s" % stray)
        return len(allowed)


class Seal:
    """Family (a): digest at gate time, verify against the GATE-TIME digest at
    promotion, recompute TOTALITY from the payload's live key set at the door
    (#348), and verify again from the promoted path."""

    def __init__(self):
        self.seals = {}
        self.unsealed = {}
        self.measured = set()
        self.closed = False

    def seal(self, key, value, gate, measured=True):
        if self.closed:
            raise GateFail("T-SEAL-PROMOTION :: seal after close: %s" % key)
        if key in self.unsealed:
            raise GateFail("T-SEAL-PROMOTION :: both sealed and unsealed: %s"
                           % key)
        self.seals[key] = {"digest": digest(value), "gate": gate}
        if measured:
            self.measured.add(key)
        return value

    def declare_unsealed(self, key, reason):
        if key in self.seals or key in self.measured:
            raise GateFail("T-SEAL-PROMOTION :: measured key unsealed: %s"
                           % key)
        if not reason.strip():
            raise GateFail("T-SEAL-PROMOTION :: unsealed with no reason: %s"
                           % key)
        self.unsealed[key] = reason

    def manifest(self):
        return {"sealed": {k: v["digest"] for k, v in sorted(self.seals.items())},
                "sealed_at_gate": {k: v["gate"]
                                   for k, v in sorted(self.seals.items())},
                "declared_unsealed": dict(sorted(self.unsealed.items()))}

    def verify_at_promotion(self, payload, ledger, manifest_key):
        moved = [k for k, s in self.seals.items()
                 if k not in payload or digest(payload[k]) != s["digest"]]
        if moved:
            raise GateFail("T-SEAL-PROMOTION :: sealed values moved: %s"
                           % moved)
        gates = set(ledger.names())
        phantom = sorted(k for k, s in self.seals.items()
                         if s["gate"] not in gates)
        if phantom:
            raise GateFail("T-SEAL-PROMOTION :: seal names a gate that never "
                           "ran: %s" % phantom)
        covered = set(self.seals) | set(self.unsealed) | {manifest_key}
        undeclared = sorted(set(payload) - covered)
        absent = sorted(set(self.seals) - set(payload))
        if undeclared:
            raise GateFail("T-SEAL-PROMOTION :: undeclared keys: %s"
                           % undeclared)
        if absent:
            raise GateFail("T-SEAL-PROMOTION :: sealed key absent: %s" % absent)

    def close(self):
        self.closed = True

    def verify_after_promotion(self, receipt_path, manifest_key):
        with open(receipt_path, "rb") as fh:
            on_disk = json.loads(fh.read().decode("utf-8"))
        moved = [k for k, s in self.seals.items()
                 if k not in on_disk or digest(on_disk[k]) != s["digest"]]
        if moved:
            raise GateFail("T-SEAL-PROMOTION :: post-close edit on disk: %s"
                           % moved)
        covered = set(self.seals) | set(self.unsealed) | {manifest_key}
        undeclared = sorted(set(on_disk) - covered)
        if undeclared:
            raise GateFail("T-SEAL-PROMOTION :: post-close add on disk: %s"
                           % undeclared)


class SemanticWall:
    """Family (c): voice-normalised REGEX patterns over the canonicalised
    paper, case-folded, with a POSITIVE leg (the paper must carry its own
    standing sentence), non-vacuous on empty text, and controls written by
    another hand (the TPL-2 item)."""

    # A LICENCE IS A POSITIVE COMMITMENT TO SCOPE, NEVER A BARE NEGATION OR A
    # HEDGE.  "The arena determines the event size, and that is not in doubt"
    # carries a negation and still makes the claim; "the menu's value would be
    # called physical by any reader" carries a hedge and still makes it.  Both
    # were licences in the delivered wall set and both are now refused at
    # construction, so the defect cannot come back by an edit to a list.
    BARE = (r"not", r"never", r"no", r"nor", r"neither", r"if", r"then",
            r"would", r"could", r"might", r"whether", r"nothing", r"cannot",
            r"without", r"any", r"some")

    def __init__(self, name, negative, positive, controls,
                 subject=(), policed=(), licences=()):
        self.name = name
        self.negative = list(negative)
        self.positive = list(positive)
        self.controls = list(controls)
        self.subject = list(subject)
        self.policed = list(policed)
        self.licences = list(licences)
        for pat in (self.negative + self.positive + self.subject
                    + self.policed + self.licences):
            re.compile(pat)
        # NO SELF-LICENSING (the POT MAJOR-1 cure): a licence may not be a
        # policed form, or the wall licenses exactly what it polices.
        bad = [l for l in self.licences
               if any(re.search(pp, l.replace("\\b", "")) for pp in self.policed)]
        if bad:
            raise GateFail("T-WALL-SEMANTIC :: self-licensing set: %s" % bad)
        bare = [l for l in self.licences
                if l.replace("\\b", "").strip() in self.BARE]
        if bare:
            raise GateFail("T-WALL-SEMANTIC :: bare-negation or hedge licence "
                           "in %s: %s" % (self.name, bare))
        # EVERY WALL POLICES A CLAIM, NOT A VOCABULARY: a wall with no
        # subject and no policed form has only its patterns, and a pattern
        # list can be walked around by any synonym.
        if not self.subject or not self.policed:
            raise GateFail("T-WALL-SEMANTIC :: %s has no licence leg"
                           % self.name)

    def seal_value(self):
        return {"name": self.name, "negative": self.negative,
                "positive": self.positive, "subject": self.subject,
                "policed": self.policed, "licences": self.licences,
                "independent_controls": len(self.controls)}

    def licence_leg(self, text):
        """THE LICENCE LEG.  A pattern list can only ban the phrasings it was
        written for; this leg bans the CLAIM.  Any sentence that names the
        wall's subject AND carries one of its policed forms must also carry a
        licence -- a conditional frame, a disclaimer, a scope word -- and the
        licence set may contain no policed form.  A paraphrase written by
        another hand still names the subject and still asserts, so it is
        caught whatever words it chooses."""
        out = []
        for sent in re.split(r"(?<=[.!?])\s+", text):
            subs = [m.start() for p in self.subject
                    for m in re.finditer(p, sent)]
            if not subs:
                continue
            # THE CLAIM, not the vocabulary: the policed form must stand
            # NEAR the wall's subject, or the sentence is merely about
            # something else that happens to share a word.
            near = [m.start() for p in self.policed
                    for m in re.finditer(p, sent)
                    if any(abs(m.start() - k) <= self.SPAN for k in subs)]
            if not near:
                continue
            if not any(re.search(l, sent) for l in self.licences):
                out.append(sent[:130])
        return out

    SPAN = 80

    NEG = re.compile(r"\b(?:not|never|nor|no|cannot|neither|without|"
                     r"whether|refuses?|denies)\b")

    # A NEGATION THAT RE-ASSERTS IS NOT A NEGATION.  "There is no doubt that
    # the event size is selected" carries the token `no` and asserts the
    # banned claim as flatly as its own control does.  These forms are
    # declared and excluded from the guard by name.
    REASSERT = re.compile(r"\b(?:no|not in|beyond|without|little|never in)\s+"
                          r"(?:doubt|question|denying|dispute|doubting)\b"
                          r"|\bcannot be (?:denied|doubted|disputed)\b"
                          r"|\bnot (?:merely|only|just|simply)\b")

    # A NEGATION IN ANOTHER CLAUSE DOES NOT NEGATE THIS ONE.
    CLAUSE = re.compile(r"[;:]|,\s*(?:and|but|so|which|while|yet)\b")

    def scan(self, paper_text):
        """A match is a violation unless its OWN CLAUSE carries a negation
        that actually negates it: a wall must ban an ASSERTION, and a paper
        that disclaims the assertion is doing the wall's work, not breaking
        it.  A negation that re-asserts ('there is no doubt that ...'), and a
        negation sitting in a different clause of the same sentence, are both
        excluded by declaration, because both were shown to walk a breach
        straight through this guard.  The controls are affirmative and each
        carries a negated twin, so the guard cannot excuse either."""
        text = canon(paper_text).lower()
        if not text:
            raise GateFail("T-WALL-SEMANTIC :: %s scanned empty text"
                           % self.name)
        hits = []
        for pat in self.negative:
            for m in re.finditer(pat, text):
                lead = text[max(0, m.start() - 300):m.start()]
                cut = max(lead.rfind("."), lead.rfind("!"), lead.rfind("?"))
                lead = lead[cut + 1:]          # the match's OWN sentence only
                excused = False
                for nm in self.NEG.finditer(lead):
                    tail = lead[nm.start():]
                    if self.REASSERT.match(tail):
                        continue               # a re-asserting negation
                    if self.CLAUSE.search(lead[nm.end():]):
                        continue               # a negation in another clause
                    excused = True
                    break
                if not excused:
                    hits.append(pat)
                    break
        missing = [p for p in self.positive if not re.search(p, text)]
        unlicensed = self.licence_leg(text)
        return {"violations": hits, "missing_positive": missing,
                "unlicensed_sentences": unlicensed}


class Anchor:
    def __init__(self, name, needle, source, consumer, why):
        self.name = name
        self.needle = needle
        self.source = source
        self.consumer = consumer
        self.why = why
        self.located = None
        self.read_by = set()


class AnchorSet:
    """Family (d): anchor text is readable ONLY through read(name, by_gate),
    which records the read; consumption is verified against gates that
    actually ran; the needle must occur in the pinned source AND in the
    paper's own rendering under #125 canonicalisation."""

    FLOOR = 24

    def __init__(self, anchors):
        self.anchors = {a.name: a for a in anchors}
        self.reads = []

    def locate(self, sources, paper_text, broken=None):
        for a in self.anchors.values():
            hay = canon(sources[a.source])
            needle = canon(a.needle)
            if a.name == broken:
                needle = needle[:-6] + "XXXXXX"
            if len(needle) < self.FLOOR:
                raise GateFail("T-ANCHOR-CONSUMED :: needle below the floor: "
                               "%s" % a.name)
            n = hay.count(needle)
            if n != 1:
                raise GateFail("T-ANCHOR-CONSUMED :: %s occurs %d times in %s"
                               % (a.name, n, a.source))
            pn = canon(paper_text).count(needle)
            if pn < 1:
                raise GateFail("T-ANCHOR-CONSUMED :: %s not rendered in the "
                               "paper" % a.name)
            a.located = needle

    def read(self, name, by_gate):
        a = self.anchors[name]
        if a.located is None:
            raise GateFail("T-ANCHOR-CONSUMED :: read before locate: %s" % name)
        a.read_by.add(by_gate)
        self.reads.append((name, by_gate))
        return a.located

    def verify_consumption(self, ledger):
        ran = set(ledger.names())
        bad = []
        for a in self.anchors.values():
            if a.consumer not in ran:
                bad.append("%s: consumer %s never ran" % (a.name, a.consumer))
            elif a.consumer not in a.read_by:
                bad.append("%s: consumer %s never read it" % (a.name, a.consumer))
        return bad


class Claims:
    """Family (e): the licensed claim set, keyed BY TABLE, compared in both
    directions with exact occurrence counts; fenced blocks by MULTISET
    equality whatever the info string; every markdown table in the paper must
    be claimed by some rendering."""

    ROW = re.compile(r"^\s*\|(.+)\|\s*$")
    FENCE = re.compile(r"^```", re.M)

    def __init__(self):
        self.tables = {}
        self.prose = Counter()
        self.fences = Counter()

    @staticmethod
    def cells(line):
        return tuple(canon(c) for c in line.strip().strip("|").split("|"))

    def table(self, tid, header, rows):
        want = Counter()
        want[self.cells("|" + "|".join(str(h) for h in header) + "|")] += 1
        for r in rows:
            want[self.cells("|" + "|".join(str(c) for c in r) + "|")] += 1
        self.tables[tid] = want
        out = ["| " + " | ".join(str(h) for h in header) + " |",
               "|" + "|".join("---" for _ in header) + "|"]
        for r in rows:
            out.append("| " + " | ".join(str(c) for c in r) + " |")
        return "\n".join(out)

    def claim(self, text, times=1):
        self.prose[canon(text)] += times
        return text

    def fence(self, text, times=1):
        self.fences[canon(text)] += times
        return text

    def paper_tables(self, paper_text):
        """every markdown table in the paper, as a multiset of row tuples,
        one bag per contiguous table block."""
        bags, cur = [], Counter()
        for ln in paper_text.split("\n"):
            m = self.ROW.match(ln)
            if m:
                cs = self.cells(ln)
                if not all(set(c) <= set("-: ") for c in cs):
                    cur[cs] += 1
            elif cur:
                bags.append(cur)
                cur = Counter()
        if cur:
            bags.append(cur)
        return bags

    def paper_fences(self, paper_text):
        out = Counter()
        parts = paper_text.split("```")
        for i in range(1, len(parts), 2):
            body = parts[i]
            if "\n" in body:
                body = body.split("\n", 1)[1]
            out[canon(body)] += 1
        return out

    def gate(self, paper_text):
        bags = self.paper_tables(paper_text)
        unmatched_paper = list(range(len(bags)))
        missing, stray = [], []
        for tid, want in sorted(self.tables.items()):
            hit = None
            for i in unmatched_paper:
                if bags[i] == want:
                    hit = i
                    break
            if hit is None:
                best = None
                for i in unmatched_paper:
                    d = sum((bags[i] - want).values()) + sum((want - bags[i]).values())
                    if best is None or d < best[0]:
                        best = (d, i)
                missing.append({"table": tid,
                                "nearest_delta": best[0] if best else None})
            else:
                unmatched_paper.remove(hit)
        for i in unmatched_paper:
            stray.append({"unclaimed_table_rows": sum(bags[i].values())})
        pf = self.paper_fences(paper_text)
        fence_missing = sorted(k[:60] for k in (self.fences - pf).elements())
        fence_stray = sorted(k[:60] for k in (pf - self.fences).elements())
        # #125 and the SEC-2 MAJOR-10 cure: the prose leg case-folds BOTH
        # sides, so a sentence-initial capital is not a defence.  Tables and
        # fences stay case-exact: they are verbatim renders.  And the leg is
        # PROSE ONLY (family f): fenced blocks are stripped first, so the
        # run's own verdict cannot discharge the paper's prose obligations.
        ptext = canon(" ".join(paper_text.split("```")[0::2])).casefold()
        prose_bad = []
        for k, need in sorted(self.prose.items()):
            got = ptext.count(k.casefold())
            if got != need:
                prose_bad.append({"claim": k[:70], "need": need, "got": got})
        return {"tables_claimed": len(self.tables),
                "tables_in_paper": len(bags),
                "tables_missing": missing, "tables_unclaimed": stray,
                "fences_claimed": sum(self.fences.values()),
                "fences_in_paper": sum(pf.values()),
                "fence_missing": fence_missing, "fence_stray": fence_stray,
                "prose_claims": len(self.prose), "prose_bad": prose_bad}


class ReferentRegistry:
    """Family (f): universes are declared with the PAIRS the run measured;
    each sentence selects its universe by subject noun; every occurrence is
    checked; fenced blocks are stripped first."""

    # THE PERIOD BLIND SPOT, CLOSED.  The delivered guard was `(?![\w.])`,
    # which refuses to scan any numeral immediately followed by a period --
    # that is, every numeral that ends a sentence, which is where a paper's
    # load-bearing values live.  The guard now refuses only a numeral inside
    # a decimal or a word: a trailing sentence period is scanned.
    NUM = re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})*|\d+)(?!\.\d)(?!\w)")

    def __init__(self):
        self.universes = {}
        self.exempt = {}
        self.self_pairs = {}

    def universe(self, name, nouns, values, pairs):
        """REFLEXIVE PAIRS ARE NOT LICENSED.  A pair (X, X) licenses an
        'X of X' fraction anywhere in the universe -- '315 of 315 histories'
        asserted of an arity that measured 276 of 280 is then invisible.  Any
        reflexive pair is split off into a register of MEASURED IDENTITIES
        and is admitted only in a sentence that carries a totality
        qualifier, which is what such a sentence actually means."""
        prs = {tuple(p) for p in pairs}
        refl = sorted(p for p in prs if p[0] == p[1])
        self.self_pairs[name] = refl
        self.universes[name] = {"nouns": [n.lower() for n in nouns],
                                "values": set(values),
                                "pairs": {p for p in prs if p[0] != p[1]}}

    def exempt_token(self, tok, reason):
        self.exempt[tok] = reason

    def seal_value(self):
        return {k: {"nouns": v["nouns"], "values": sorted(v["values"]),
                    "pairs": sorted(v["pairs"]),
                    "measured_identities_not_licensed_as_pairs":
                        sorted(self.self_pairs.get(k, []))}
                for k, v in sorted(self.universes.items())}

    TOTALITY = re.compile(r"\ball\b|\bevery one of\b|\bevery\b|\bwhole\b")

    @staticmethod
    def prose_only(paper_text, strips=()):
        """PROSE ONLY, and prose means prose.  Fenced blocks are stripped so
        the run's own verdict cannot discharge the paper's obligations;
        markdown TABLE rows are stripped because a table row is bound by the
        claims gate and not by a sentence's referent; block QUOTATIONS are
        stripped because they are the parents' words, bound by the verbatim
        anchors; and the declared structural tokens -- paper ids, section
        cross-references, digests -- are removed by the same patterns the
        coverage scan declares."""
        parts = paper_text.split("```")
        lines = []
        for chunk in parts[0::2]:
            for ln in chunk.split("\n"):
                t = ln.strip()
                if t.startswith("|") or t.startswith(">"):
                    continue
                lines.append(ln)
        txt = "\n".join(lines)
        for pat, _why in strips:
            txt = re.sub(pat, " ", txt)
        return canon(txt)

    def _universe_of(self, sentence):
        s = sentence.lower()
        best, bestpos = None, None
        for name, u in self.universes.items():
            for noun in u["nouns"]:
                p = s.find(noun)
                if p >= 0 and (bestpos is None or p < bestpos):
                    best, bestpos = name, p
        return best

    def gate(self, paper_text, strips=(), spelled=False):
        """SPELLED IS THE SAME SCAN.  With `spelled` set, every spelled
        cardinal in the prose is rewritten to its digits before the scan
        runs, so a spelled numeral is bound exactly as a written one is and
        the two scans differ in nothing but the alphabet."""
        text = self.prose_only(paper_text, strips)
        for tok in self.exempt:
            text = text.replace(tok, " ")
        text = re.sub(r"\b[0-9a-f]{12}\b", " ", text)
        if spelled:
            text = re.sub(r"\b(%s)\b" % "|".join(SPELLED_SCANNED),
                          lambda m: str(SPELLED_VALUE[m.group(1)]), text)
        bad, checked, pairs_checked = [], 0, 0
        for sent in re.split(r"(?<=[.!?])\s+", text):
            u = self._universe_of(sent)
            if u is None:
                continue
            vals = [int(m.group(1).replace(",", ""))
                    for m in self.NUM.finditer(sent)]
            if not vals:
                continue
            checked += 1
            uv = self.universes[u]["values"]
            offend = [v for v in vals if v not in uv]
            if offend:
                bad.append({"universe": u, "sentence": sent[:110],
                            "not_in_universe": offend})
                continue
            for m in re.finditer(r"(\d[\d,]*)\s+of\s+(?:the\s+)?(\d[\d,]*)",
                                 sent):
                pr = (int(m.group(1).replace(",", "")),
                      int(m.group(2).replace(",", "")))
                pairs_checked += 1
                if pr[0] == pr[1]:
                    if pr not in self.self_pairs.get(u, []):
                        bad.append({"universe": u, "sentence": sent[:110],
                                    "reflexive_pair_never_measured":
                                        list(pr)})
                    elif not self.TOTALITY.search(sent):
                        bad.append({"universe": u, "sentence": sent[:110],
                                    "reflexive_pair_without_a_totality_"
                                    "qualifier": list(pr)})
                elif pr not in self.universes[u]["pairs"]:
                    bad.append({"universe": u, "sentence": sent[:110],
                                "unmeasured_pair": list(pr)})
        return {"sentences_checked": checked, "pairs_checked": pairs_checked,
                "spelled_normalised": bool(spelled), "violations": bad}


class CountRegistry:
    """Family (g): values enter by measurement; statements interpolate by
    NAME; the template is checked BEFORE substitution; an AST leg scans this
    module for numerals typed into gate statements, claim templates or head
    segments -- including the TPL-2 subspecies (%-format literals and integer
    offsets typed into a statement builder's arguments)."""

    TOKEN = re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})*|\d+)(?!\.\d)(?!\w)")

    # DECLARED STRUCTURAL NAMES.  A numeral inside a NAME is not a count: the
    # outcome word this unit registered spells a digit, and so do a
    # criterion-leg id, a section cross-reference, a paper id and an
    # algorithm name.  Each is declared with its reason and each must be
    # USED, so the register cannot quietly become a hole.
    NAME_STRIPS = (
        (r"NEEDS-3", "a declared outcome word"),
        (r"C2\^4", "the abstract translation group's name"),
        (r"leg-1", "a criterion-leg id"),
        (r"sha256-12", "an algorithm name and its prefix length"),
    )

    def __init__(self):
        self.vals = {}
        self.how = {}
        self.exempt = {}
        self.names_used = set()

    def strip_names(self, text):
        for pat, _why in self.NAME_STRIPS:
            if re.search(pat, text):
                self.names_used.add(pat)
                text = re.sub(pat, " ", text)
        return text

    def measured(self, name, value, how):
        self.vals[name] = value
        self.how[name] = how
        return value

    def get(self, name):
        if name not in self.vals:
            raise GateFail("T-NO-TYPED-COUNTS :: unmeasured name %s" % name)
        return self.vals[name]

    def exempt_token(self, tok, reason):
        self.exempt[tok] = reason

    def stmt(self, template, **names):
        found = [m.group(1) for m in
                 self.TOKEN.finditer(self.strip_names(template))]
        bad = [t for t in found if t not in self.exempt]
        if bad:
            raise GateFail("T-NO-TYPED-COUNTS :: typed numeral(s) %s in a "
                           "statement template" % bad)
        return template.format(**{k: self.get(v) if isinstance(v, str)
                                  else v for k, v in names.items()})

    def audit_module(self, source, callers):
        """the AST leg.  Any string literal handed to a VOUCHING builder --
        a gate statement, a claim template, a rendered table, a rendered
        fence or a registry value -- that types a numeral is an offender
        whatever the docstring says.  Integer literals passed to one are the
        TPL-2 subspecies, and so is an integer OFFSET: `len(walls) - 7 + 12`
        reaches a published statement carrying two typed counts that no
        string scan will ever see, so any BinOp with an integer operand
        inside a vouching call is flagged by its own leg.

        The string exemption register does NOT extend to integer literals: an
        exemption is granted for a spelling that appears inside prose (the
        dimension in `AG(2, q)`), never for an arithmetic constant."""
        tree = ast.parse(source)
        offenders = []
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            fn = node.func
            nm = (fn.attr if isinstance(fn, ast.Attribute)
                  else getattr(fn, "id", None))
            if nm not in callers:
                continue
            args = list(node.args) + [k.value for k in node.keywords]
            for arg in args:
                for sub in ast.walk(arg):
                    if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
                        for m in self.TOKEN.finditer(
                                self.strip_names(sub.value)):
                            if m.group(1) not in self.exempt:
                                offenders.append({"caller": nm,
                                                  "typed": m.group(1),
                                                  "line": sub.lineno})
            # THE VALUE SIDE.  An integer literal, or an integer OFFSET, in
            # the position where a MEASUREMENT belongs is the TPL-2
            # subspecies no string scan can see: `len(walls) - 7 + 12`
            # publishes two typed counts through a statement that reads them
            # from the live registry.  Indices, slices and comprehension
            # seeds are not that, so only the value expression's own top
            # level is inspected.
            value_args = ([args[1]] if nm == "measured" and len(args) > 1
                          else args)
            for arg in value_args:
                got = _direct_int(arg)
                if got is not None:
                    offenders.append({"caller": nm, "typed_value": got,
                                      "line": arg.lineno})
        return offenders


def _direct_int(node):
    """an integer standing at the top level of a value expression, through
    arithmetic but not through calls, indices or comprehensions."""
    if (isinstance(node, ast.Constant) and isinstance(node.value, int)
            and not isinstance(node.value, bool)):
        return node.value
    if isinstance(node, ast.BinOp):
        for side in (node.left, node.right):
            got = _direct_int(side)
            if got is not None:
                return got
    if isinstance(node, ast.UnaryOp):
        return _direct_int(node.operand)
    return None


class Falsifier:
    def __init__(self, name, gate, description, target, apply):
        self.name = name
        self.gate = gate
        self.description = description
        self.target = target
        self.apply = apply


class ReadSet:
    """Family (i): every open() this process performs is recorded AT THE
    ACCESSOR by an audit hook, and the multiset of repository-relative paths
    is compared at the LAST gate, not the first."""

    def __init__(self, root):
        self.root = os.path.abspath(root)
        self.reads = []
        self.external = []
        self.exemptions = {}
        self.used = set()

    def install(self):
        """EVERY path is recorded, not only the repository's.  A hook that
        keeps only paths under the repository root makes a read of anything
        else invisible, and the docstring that says every open is recorded is
        then false as written.  Reads outside the root go to their own
        bucket, which the gate requires to be EMPTY."""
        def hook(event, args):
            if event == "open":
                p = args[0]
                if isinstance(p, (str, bytes, os.PathLike)):
                    try:
                        ap = os.path.abspath(os.fspath(p))
                    except Exception:
                        return
                    if ap.startswith(self.root + os.sep):
                        self.reads.append(os.path.relpath(ap, self.root))
                    else:
                        self.external.append(ap)
        sys.addaudithook(hook)

    def exempt(self, rel, reason):
        self.exemptions[rel] = reason

    def gate_at_close(self, declared):
        seen = Counter(self.reads)
        want = set(declared)
        undeclared = []
        for p, _n in seen.items():
            if p in want:
                continue
            hit = None
            for ex in self.exemptions:
                if p == ex or p.startswith(ex):
                    hit = ex
                    break
            if hit is None:
                undeclared.append(p)
            else:
                self.used.add(hit)
        never = sorted(p for p in want if p not in seen)
        unused = sorted(e for e in self.exemptions if e not in self.used)
        # THE PATH LIST IS PUBLISHED, not only its cardinality: a reader
        # holding the receipt can see WHICH files the run opened.
        return {"distinct_reads": len(seen), "undeclared": sorted(undeclared),
                "declared_never_read": never, "unused_exemptions": unused,
                "paths": sorted(seen),
                "external_reads": sorted(set(self.external)),
                "exemptions": dict(sorted(self.exemptions.items()))}

# ===========================================================================
# SECTION 2.  THE ARENA (AG(2, 4), FIXED) AND THE MEASUREMENT PRIMITIVES
# ===========================================================================

# GF(4) explicitly, as NDEP carries it: elements 0, 1, 2, 3 with 2 and 3 the
# two primitive elements; addition is XOR (the additive group is C2^2, which
# is the whole reason this arena separates the characteristic from q).
F4_MUL = {(0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 0,
          (1, 0): 0, (1, 1): 1, (1, 2): 2, (1, 3): 3,
          (2, 0): 0, (2, 1): 2, (2, 2): 3, (2, 3): 1,
          (3, 0): 0, (3, 1): 3, (3, 2): 1, (3, 3): 2}


class Arena:
    """AG(2, 4): sixteen actors, five parallel classes, four declared links.

    NOTHING in this class depends on the arity or on the reading.  It is
    instantiated once and consumed everywhere, which is what makes the sweep
    a sweep of a and of the reading and of nothing else."""

    def __init__(self):
        self.q = 4
        self.n = self.q * self.q
        self.el = (0, 1, 2, 3)
        # the characteristic is computed from the field's own addition, not
        # aliased to q: at this arena they DIFFER, which is the point.
        one, acc, k = 1, 1, 1
        while acc != 0:
            acc = acc ^ one
            k += 1
        self.characteristic = k
        self.SITES = tuple((i, j) for i in self.el for j in self.el)
        self.SI = {s: i for i, s in enumerate(self.SITES)}
        # NDEP's own declaration: the canonical directions with first
        # coordinate in the prime subfield, the first four declared.
        self.DIRECTIONS = ((1, 0), (0, 1), (1, 1), (1, 2), (1, 3))
        self.L = 4
        self.LINKS = self.DIRECTIONS[:self.L]
        self.UNDECLARED = self.DIRECTIONS[self.L]
        self.CELLS = tuple((x, l) for x in self.SITES for l in self.LINKS)
        self.CI = {c: i for i, c in enumerate(self.CELLS)}
        self.CLASS_DIRS = ((0, 1), (1, 0), (1, 1), (1, 2), (1, 3))
        self.CLASS_NAMES = ("ROW", "COL", "DIA", "ANT", "CL4")
        self.CLASSES = {nm: self.parallel_class(d)
                        for nm, d in zip(self.CLASS_NAMES, self.CLASS_DIRS)}
        self.CLASS_OF = {v: k for k, v in self.CLASSES.items()}
        self.DECLARED_CLASSES = tuple(
            self.CLASS_NAMES[i] for i in range(self.q + 1)
            if self.CLASS_DIRS[i] in self.LINKS)

    def vadd(self, a, b):
        return (a[0] ^ b[0], a[1] ^ b[1])

    def vmul(self, k, a):
        return (F4_MUL[(k, a[0])], F4_MUL[(k, a[1])])

    def parallel_class(self, d):
        H = frozenset(self.vmul(t, d) for t in self.el)
        seen, out = set(), []
        for x in self.SITES:
            Ln = tuple(sorted(self.vadd(x, h) for h in H))
            if Ln not in seen:
                seen.add(Ln)
                out.append(Ln)
        return tuple(sorted(out))

    def links_generate(self):
        """the subgroup the declared links generate, by closure -- at this
        arena it is PROPER, which NDEP measured and this unit re-measures."""
        S = {(0, 0)}
        ch = True
        while ch:
            ch = False
            for s in list(S):
                for l in self.LINKS:
                    t = self.vadd(s, l)
                    if t not in S:
                        S.add(t)
                        ch = True
        return frozenset(S)

    def subgroups(self):
        """every ABSTRACT subgroup of the translation group, by closure of
        generator sets; the group is elementary abelian of rank four."""
        T = [s for s in self.SITES if s != (0, 0)]
        found = set()
        for k in range(0, 5):
            for gens in combinations(T, k):
                S = {(0, 0)}
                ch = True
                while ch:
                    ch = False
                    for s in list(S):
                        for g in gens:
                            t = self.vadd(s, g)
                            if t not in S:
                                S.add(t)
                                ch = True
                found.add(frozenset(S))
        return sorted(found, key=lambda s: (len(s), sorted(s)))

    def f4_subspaces(self, subs):
        """the F4-LINEAR members of the abstract lattice: closed under
        every field scalar.  The mutant drops one scalar, which is exactly
        the corruption that would silently widen the primary reading."""
        scalars = self.el[:2] if mut("MUT-READING") else self.el
        return [s for s in subs
                if all(self.vmul(t, x) in s for x in s for t in scalars)]

    def coset_partition(self, H):
        seen, out = set(), []
        for x in self.SITES:
            c = tuple(sorted(self.vadd(x, h) for h in H))
            if c not in seen:
                seen.add(c)
                out.append(c)
        return tuple(sorted(out))

    def round_vec(self, P):
        return tuple(1 if any(x in g and self.vadd(x, l) in g for g in P)
                     else 0 for (x, l) in self.CELLS)

    def canon_transversals(self, P):
        sizes = {len(g) for g in P}
        k = min(sizes)
        return [tuple(sorted(g)[j] for g in P) for j in range(k)]

    def round_events(self, P):
        """the driver's own event order: groups ascending by seed site."""
        seeds = [sorted(g)[0] for g in P]
        order = sorted(range(len(P)), key=lambda gi: self.SI[seeds[gi]])
        return [frozenset(P[gi]) for gi in order]


A = Arena()
NC = len(A.CELLS)
SUBS = A.subgroups()
F4SUBS = A.f4_subspaces(SUBS)
G8 = A.links_generate()

# ---- bitmask machinery: per-link image tables and the weight table -------
LINK_IMG = []
for _l in A.LINKS:
    _im = [0] * 16
    for _s in A.SITES:
        _im[A.SI[_s]] = 1 << A.SI[A.vadd(_s, _l)]
    LINK_IMG.append(tuple(_im))


def mask_image(mask, li):
    im = LINK_IMG[li]
    out = 0
    m = mask
    while m:
        b = m & -m
        out |= im[b.bit_length() - 1]
        m ^= b
    return out


def weight_table():
    """w(mask) for every actor subset: the number of (site, link) cells the
    block marks.  In characteristic two the link image is its own preimage,
    so one table serves both directions."""
    W = [0] * 65536
    for mask in range(1, 65536):
        w = 0
        for li in range(A.L):
            w += bin(mask & mask_image(mask, li)).count("1")
        W[mask] = w
    return W


def wtab():
    return memo(("wtab",), weight_table)


def block_mask(sites_iter):
    m = 0
    for x in sites_iter:
        m |= 1 << A.SI[x]
    return m


def mask_sites(m):
    out = []
    while m:
        b = m & -m
        out.append(A.SITES[b.bit_length() - 1])
        m ^= b
    return out


# ---- THE SUBSTRATE CENSUS BY DYNAMIC PROGRAMMING -------------------------
# The parent enumerated its packings whole (945 at its largest row).  At
# sixteen actors the pools reach 22,422,400, so the census walks the subset
# lattice instead: a maximal a-packing is censused by weight through a
# memoised recursion over the remaining-actor set, the block containing the
# lowest remaining actor enumerated directly and the idle option metered by
# the remainder's own arithmetic.  The distribution is EXACT -- every
# grouping counted once -- and the total is cross-checked against the
# multinomial closed form at every arity.

def packing_distribution(a):
    return memo(("packdist", a, mut("MUT-PACKING")),
                lambda: _packing_distribution(a))


def _packing_distribution(a):
    W = wtab()
    bmax = A.n // a
    r = A.n - a * bmax
    if mut("MUT-PACKING"):
        r = 0                      # the idle branch lost: 3 and 5 collapse
    if bmax == 1:
        out = Counter()
        for comb in combinations(range(16), a):
            m = 0
            for e in comb:
                m |= 1 << e
            out[W[m]] += 1
        return dict(out)
    memo_local = {}

    def f(S):
        if S == 0:
            return {0: 1}
        if S in memo_local:
            return memo_local[S]
        rem = 16 - bin(S).count("1")
        b = rem // a
        i = rem - a * b
        out = Counter()
        low = (S & -S).bit_length() - 1
        S2 = S ^ (1 << low)
        if i < r:
            for w, c in f(S2).items():
                out[w] += c
        if b < bmax:
            rest = []
            m = S2
            while m:
                bb = m & -m
                rest.append(bb.bit_length() - 1)
                m ^= bb
            base = 1 << low
            for extra in combinations(rest, a - 1):
                bm = base
                for e in extra:
                    bm |= 1 << e
                w0 = W[bm]
                for w, c in f(S ^ bm).items():
                    out[w0 + w] += c
        memo_local[S] = dict(out)
        return memo_local[S]

    got = f(65535)
    return got if got else {0: 0}


def closed_grouping_count(a):
    bmax = A.n // a
    r = A.n - a * bmax
    return (math.factorial(A.n)
            // (math.factorial(a) ** bmax * math.factorial(bmax)
                * math.factorial(r)))


def packings_prefix(a, cap, drop_idle=False):
    """the first `cap` maximal a-packings in the parent's own recursion
    order -- the object-level leg of the packing-extends gate, windowed
    because the full pools are millions where the parent's were hundreds."""
    nb = A.n // a
    out = []

    def rec(rem, acc):
        if len(out) >= cap:
            return
        if len(acc) == nb:
            out.append(tuple(sorted(acc)))
            return
        if not rem:
            return
        first, rest = rem[0], rem[1:]
        for extra in combinations(rest, a - 1):
            blk = tuple(sorted((first,) + extra))
            rec(tuple(x for x in rest if x not in extra), acc + [blk])
            if len(out) >= cap:
                return
        if not drop_idle and len(rest) >= a * (nb - len(acc)):
            rec(rest, acc)
    rec(tuple(A.SITES), [])
    if mut("MUT-EXTEND") and drop_idle and out:
        out = out[:-1]
    return out


def sat_round_sample(a, cap):
    """the first `cap` budget-saturating maximal a-packings in canonical
    order: the declared witness window for the exact-cover ladder search."""
    return memo(("satsample", a, cap), lambda: _sat_round_sample(a, cap))


def _sat_round_sample(a, cap):
    W = wtab()
    bmax = A.n // a
    out = []
    blocks_acc = []

    def rec(S, idles_left, blocks, wsum):
        if len(out) >= cap:
            return
        if blocks == bmax:
            if wsum == A.n:
                out.append(tuple(blocks_acc))
            return
        if S == 0:
            return
        low = (S & -S).bit_length() - 1
        S2 = S ^ (1 << low)
        rest = []
        m = S2
        while m:
            bb = m & -m
            rest.append(bb.bit_length() - 1)
            m ^= bb
        for extra in combinations(rest, a - 1):
            bm = (1 << low)
            for e in extra:
                bm |= 1 << e
            w0 = W[bm]
            if wsum + w0 > A.n:
                continue
            blocks_acc.append(tuple(sorted([low] + list(extra))))
            rec(S ^ bm, idles_left, blocks + 1, wsum + w0)
            blocks_acc.pop()
            if len(out) >= cap:
                return
        if idles_left:
            rec(S2, idles_left - 1, blocks, wsum)

    rec(65535, A.n - a * bmax, 0, 0)
    return [tuple(tuple(A.SITES[i] for i in b) for b in P) for P in out]


def round_cell_mask(P):
    v = A.round_vec(P)
    m = 0
    for k, b in enumerate(v):
        if b:
            m |= 1 << k
    return m


# ---- THE GEOMETRY SURVIVORS: the invariant-partition closure -------------
# The parent evaluated its geometry leg on the complete actor lattice of
# 21,147 partitions.  Bell(16) is 10,480,142,147, so the lattice cannot be
# walked here; what CAN be walked, completely, is the survivor set itself.
# The leg admits a partition exactly when every declared link's translation
# descends to the blocks -- equivalently, when the partition is invariant
# under the group the links generate -- and the invariant partitions form a
# lattice reachable from the discrete partition by single-merge closures.
# The enumeration is breadth-first over that lattice and is COMPLETE: every
# invariant partition is the closure of the discrete one under finitely
# many merges, each intermediate is itself invariant, so the walk reaches
# everything.  No structure theorem is assumed anywhere.

def close_partition(pairs, spread=None):
    spread = sorted(G8) if spread is None else spread
    parent = {s: s for s in A.SITES}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    stack = list(pairs)
    while stack:
        x, y = stack.pop()
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry
            for g in spread:
                stack.append((A.vadd(x, g), A.vadd(y, g)))
    blocks = {}
    for s in A.SITES:
        blocks.setdefault(find(s), []).append(s)
    return tuple(sorted(tuple(sorted(b)) for b in blocks.values()))


def survivors():
    return memo(("survivors", mut("MUT-MENU")), _survivors)


def _survivors():
    # the mutant narrows the invariance spread to the FIRST link's own
    # span, which is exactly the corruption that would readmit partitions
    # a dropped link no longer polices.
    spread = None
    if mut("MUT-MENU"):
        one = {(0, 0)}
        ch = True
        while ch:
            ch = False
            for s in list(one):
                t = A.vadd(s, A.LINKS[0])
                if t not in one:
                    one.add(t)
                    ch = True
        spread = sorted(one)
    disc = close_partition([], spread)
    seen = {disc}
    frontier = [disc]
    while frontier:
        nxt = []
        for P in frontier:
            anchor = [(b[0], x) for b in P for x in b[1:]]
            for b, b2 in combinations(P, 2):
                Q = close_partition([(b[0], b2[0])] + anchor, spread)
                if Q not in seen:
                    seen.add(Q)
                    nxt.append(Q)
        frontier = nxt
    return sorted(seen)


def leg1_geometry(part):
    """the parent's leg-1 predicate verbatim: for each declared link the
    translation descends to the blocks.  Run over the survivor set as its
    own verification -- every survivor must pass and every single-merge
    coarsening that left the set must have failed somewhere it was tried."""
    bm = {x: bi for bi, b in enumerate(part) for x in b}
    for l in A.LINKS:
        img = {}
        for x in A.SITES:
            b, t = bm[x], bm[A.vadd(x, l)]
            if img.setdefault(b, t) != t:
                return False
    return True


# ---- NDEP's OWN n = 16 WINDOW, RE-DERIVED (the fidelity leg) -------------

def first_menu_schedule(T):
    return tuple((T[r], A.canon_transversals(T[r])[0]) for r in range(len(T)))


def history_of(schedule):
    H = []
    for (groups, seeds) in schedule:
        order = sorted(range(len(groups)), key=lambda gi: A.SI[seeds[gi]])
        for gi in order:
            H.append(frozenset(groups[gi]))
    return tuple(H)


def class_tuples16():
    return memo(("clstuples", mut("MUT-FIDELITY")), _class_tuples16)


def _class_tuples16():
    cls, cov = [], []
    for T in product(A.DECLARED_CLASSES, repeat=A.L):
        Ps = tuple(A.CLASSES[k] for k in T)
        tot = [0] * NC
        for P in Ps:
            v = A.round_vec(P)
            for k in range(NC):
                tot[k] += v[k]
        H = history_of(first_menu_schedule(Ps))
        cls.append((T, H))
        if all(t >= 1 for t in tot):
            cov.append((T, H))
    if mut("MUT-FIDELITY") and cov:
        cov = cov[:-1]
    return cls, cov


def young_order(H):
    sig = {}
    for x in A.SITES:
        sig.setdefault(tuple(1 if x in F else 0 for F in H), []).append(x)
    o = 1
    for b in sig.values():
        o *= math.factorial(len(b))
    return o


def crystallization_time(H):
    """NDEP's own crystallization: the earliest prefix length whose
    stabilizer is trivial."""
    for k in range(1, len(H) + 1):
        if young_order(H[:k]) == 1:
            return k
    return None


def min_event_subset(H):
    """NDEP's own per-history floor: the smallest SUBSET of the events
    whose stabilizer is already trivial."""
    seps = []
    for a, b in combinations(range(A.n), 2):
        m = 0
        for i, F in enumerate(H):
            if (A.SITES[a] in F) != (A.SITES[b] in F):
                m |= 1 << i
        if m == 0:
            return None
        seps.append(m)
    for k in range(1, len(H) + 1):
        for comb in combinations(range(len(H)), k):
            s = 0
            for i in comb:
                s |= 1 << i
            if all(sep & s for sep in seps):
                return k
    return None


def permutation_window():
    return memo(("permwin",), _permutation_window)


def _permutation_window():
    """NDEP's declared window: every transposition and every three-cycle of
    the sixteen actors.  S_16 has 20,922,789,888,000 elements and is not
    filterable; the window is exercised in both directions."""
    out = []
    for i, j in combinations(range(A.n), 2):
        p = list(range(A.n))
        p[i], p[j] = j, i
        out.append(tuple(p))
    for i, j, k in combinations(range(A.n), 3):
        for cyc in ((j, k, i), (k, i, j)):
            p = list(range(A.n))
            p[i], p[j], p[k] = cyc
            out.append(tuple(p))
    return out


def route_scan(histories, corrupt=False):
    """LAW 1's two routes over a window of histories, at every prefix, over
    the whole declared permutation window.  Route A applies the DEFINITION
    -- carries every event to itself, setwise, via event masks; route B
    reads the participation-signature table and nothing else.  They are
    compared per (history, prefix, permutation)."""
    WIN = permutation_window()
    cmpc = posc = badc = vacc = 0
    per_hist = []
    for Href in histories:
        masks = []
        for F in Href:
            m = 0
            for x in F:
                m |= 1 << A.SI[x]
            masks.append(m)
        if corrupt and masks:
            masks = [((masks[0] ^ 1) | 2)] + masks[1:]
        c_h = p_h = b_h = 0
        for k in range(len(Href) + 1):
            mk = masks[:k]
            sig = [tuple(1 if A.SITES[i] in F else 0 for F in Href[:k])
                   for i in range(A.n)]
            for p in WIN:
                s = True
                for m in mk:
                    im = 0
                    mm = m
                    while mm:
                        bb = mm & -mm
                        im |= 1 << p[bb.bit_length() - 1]
                        mm ^= bb
                    if im != m:
                        s = False
                        break
                y = all(sig[p[i]] == sig[i] for i in range(A.n))
                cmpc += 1
                c_h += 1
                if s != y:
                    badc += 1
                    b_h += 1
                elif s:
                    posc += 1
                    p_h += 1
                    if k == 0:
                        vacc += 1
        per_hist.append((c_h, p_h, b_h))
    return {"comparisons": cmpc, "positive": posc, "mismatches": badc,
            "positive_at_the_empty_prefix": vacc, "per_history": per_hist,
            "window_size": len(WIN)}


# ---- THE COSET WINDOWS (the declared corpora at the new arena) -----------

def coset_rounds(a, reading):
    """the single-round window at arity a under a reading: the coset
    partitions of the order-a members of that reading's lattice.  EMPTY is
    a measured refusal, not a search failure."""
    lattice = F4SUBS if reading == "F4-LINEAR" else SUBS
    return [A.coset_partition(H) for H in lattice if len(H) == a]


def covering_coset_tuples(a):
    """the multi-round window: every ordered R = L tuple over the DECLARED
    WINDOW BASIS whose summed field covers every cell.  The basis is NDEP's
    own committed one: the budget-saturating LINEAR coset rounds where the
    linear reading has objects (at the committed arity these are the four
    declared classes, and the covering tuples are NDEP's own), and the
    budget-saturating abstract coset rounds where it has none (at two
    actors these are the four link matchings).  The budget-saturating
    ABSTRACT pool is measured and published beside the basis -- at the
    committed arity it is wider than the basis, and sweeping its covering
    tuples is out of this unit's declared scope."""
    lin = [P for P in coset_rounds(a, "F4-LINEAR")
           if sum(A.round_vec(P)) == A.n]
    abs_sat = [P for P in coset_rounds(a, "ABSTRACT")
               if sum(A.round_vec(P)) == A.n]
    basis = lin if lin else abs_sat
    out = []
    for T in product(range(len(basis)), repeat=A.L):
        tot = [0] * NC
        for i in T:
            v = A.round_vec(basis[i])
            for k in range(NC):
                tot[k] += v[k]
        if all(t >= 1 for t in tot):
            out.append(tuple(basis[i] for i in T))
    return basis, abs_sat, out


def corpora():
    return memo(("corpora", mut("MUT-CORPUS")), _corpora)


def _corpora():
    out = {}
    for a in ARITIES:
        singles_abs = coset_rounds(a, "ABSTRACT")
        singles_lin = coset_rounds(a, "F4-LINEAR")
        if singles_abs:
            basis, abs_sat, cov = covering_coset_tuples(a)
        else:
            basis, abs_sat, cov = [], [], []
        entry = {
            "singles_abstract": singles_abs,
            "singles_linear": singles_lin,
            "window_basis": basis,
            "saturating_abstract_rounds": abs_sat,
            "covering_tuples": cov,
            "refusal": None}
        if not singles_abs:
            entry["refusal"] = {
                "divides_n": A.n % a == 0,
                "remainder": A.n % a,
                "order_a_abstract_subgroups":
                    sum(1 for H in SUBS if len(H) == a),
                "order_a_linear_subspaces":
                    sum(1 for H in F4SUBS if len(H) == a),
                "stamp": "REFUSED-BY-THE-COMMITTED-GRAMMAR"}
        if mut("MUT-CORPUS") and a == ARITIES[0]:
            entry["singles_abstract"] = singles_abs + singles_abs[:1]
        out[a] = entry
    return out


def single_histories(rounds):
    return [tuple(A.round_events(P)) for P in rounds]


def tuple_histories(tuples_):
    return [history_of([(P, A.canon_transversals(P)[0]) for P in T])
            for T in tuples_]


# ---- LAW 2: THE CERTIFIED FLOOR AND THE SCHEDULE SWEEPS ------------------

def counting_floor(n):
    k = 0
    while 2 ** k < n:
        k += 1
    return k


def weight_floor(n, event_size):
    """NDEP's sharpened floor, with the event size as the term the parent's
    quotation names."""
    k = 1
    while True:
        if 2 ** k >= n:
            tot, left, w = 0, n, 0
            while left > 0 and w <= k:
                take = min(math.comb(k, w), left)
                tot += take * w
                left -= take
                w += 1
            if left == 0 and tot <= k * event_size:
                return k
        k += 1


def lightest_total(n, k):
    tot, left, w = 0, n, 0
    while left > 0 and w <= k:
        take = min(math.comb(k, w), left)
        tot += take * w
        left -= take
        w += 1
    return tot if left == 0 else None


def certified_floor(a):
    return memo(("certfloor", a, mut("MUT-FLOORCERT")),
                lambda: _certified_floor(a))


def _certified_floor(a):
    """the floor at arity a over the COMPLETE event universe, decided by
    certificate: the least k admitting sixteen distinct k-bit signatures
    with every column summing to a, refusals named below it and a witness
    exhibited at the value."""
    n = A.n
    reasons = []
    k = 1
    while k <= 16:
        if 2 ** k < n:
            reasons.append({"k": k, "refused": "TOO-FEW-SIGNATURES",
                            "distinct_available": 2 ** k, "actors": n})
            k += 1
            continue
        lt = lightest_total(n, k)
        if lt > k * a:
            reasons.append({"k": k, "refused": "WEIGHT-INFEASIBLE",
                            "lightest_total": lt, "budget": k * a})
            k += 1
            continue
        vecs = sorted(range(2 ** k), key=lambda v: (bin(v).count("1"), v))
        col = [0] * k
        pick = []
        found = []
        nodes = [0]

        def rec(start):
            nodes[0] += 1
            if found or nodes[0] > FLOOR_NODE_CAP:
                return
            if len(pick) == n:
                if all(c == a for c in col):
                    found.append(list(pick))
                return
            need = n - len(pick)
            rem = sum(a - c for c in col)
            for i in range(start, len(vecs)):
                v = vecs[i]
                w = bin(v).count("1")
                if w > rem:
                    break
                ok = True
                for b in range(k):
                    if (v >> b) & 1 and col[b] == a:
                        ok = False
                        break
                if not ok:
                    continue
                if len(vecs) - i < need:
                    break
                for b in range(k):
                    if (v >> b) & 1:
                        col[b] += 1
                pick.append(v)
                rec(i + 1)
                pick.pop()
                for b in range(k):
                    if (v >> b) & 1:
                        col[b] -= 1
                if found:
                    return
        rec(0)
        if found:
            kk = k + 1 if mut("MUT-FLOORCERT") else k
            wit = [[(v >> b) & 1 for b in range(k)] for v in found[0]]
            return kk, wit, reasons, nodes[0]
        reasons.append({"k": k, "refused": "NO-WITNESS-WITHIN-CAP",
                        "nodes": nodes[0]})
        k += 1
    return None, None, reasons, None


def saturating_matchings():
    """the COMPLETE budget-saturating pool at a = 2: every perfect matching
    of the sixteen actors all of whose pairs are declared-link pairs,
    enumerated by depth-first search.  The pool is small because the link
    graph splits into the two cosets of the span of the links."""
    return memo(("satmatch",), _saturating_matchings)


def _saturating_matchings():
    adj = {s: [A.vadd(s, l) for l in A.LINKS] for s in A.SITES}
    out = []

    def rec(rem, acc):
        if not rem:
            out.append(tuple(sorted(acc)))
            return
        x = min(rem, key=lambda s: A.SI[s])
        for y in adj[x]:
            if y in rem:
                rec(rem - {x, y},
                    acc + [tuple(sorted((x, y)))])

    rec(frozenset(A.SITES), [])
    return sorted(set(out))


def time_to_discrete(rounds):
    part = [frozenset(A.SITES)]
    k = 0
    for P in rounds:
        for e in A.round_events(P):
            k += 1
            nxt = []
            for b in part:
                i, o = b & e, b - e
                if i:
                    nxt.append(i)
                if o:
                    nxt.append(o)
            part = nxt
            if len(part) == A.n:
                return k
    return None


def schedule_sweep_a2():
    return memo(("sched2", mut("MUT-SCHEDULE")), _schedule_sweep_a2)


def _schedule_sweep_a2():
    """THE SCHEDULE TIME AT a = 2, COMPLETE OVER THE WHOLE SATURATING POOL.

    A history is a sequence of whole rounds from the pool with repetition,
    events in the driver's own order.  No history is discrete inside round
    one (eight events leave the eight pairs), so the minimum lies inside
    round two, and the minimum over round two is the minimum over ORDERED
    PAIRS of pool rounds -- all of which are swept, repetition included.
    Longer histories cannot beat a value found inside round two, because
    their first two rounds are themselves such a pair.  The sweep is
    therefore complete over every history the pool admits, with no cap."""
    pool = saturating_matchings()
    best = None
    wit = None
    pairs = 0
    for i, M1 in enumerate(pool):
        for j, M2 in enumerate(pool):
            pairs += 1
            t = time_to_discrete([M1, M2])
            if t is not None and (best is None or t < best):
                best = t
                wit = (i, j)
    if mut("MUT-SCHEDULE") and best is not None:
        best = best - 1
    return {"pool": len(pool), "ordered_pairs": pairs,
            "min_events": best, "witness_pair": list(wit) if wit else None,
            "round_one_discrete_possible": any(
                time_to_discrete([M]) is not None for M in pool)}


def schedule_window_a4():
    return memo(("sched4",), _schedule_window_a4)


def _schedule_window_a4():
    """the a = 4 schedule ON NDEP'S OWN DECLARED WINDOW -- the covering
    class tuples -- re-derived here; the full saturating pool at a = 4 has
    hundreds of thousands of members and its complete sweep is out of this
    unit's declared scope, so the value is a WINDOW value with the
    certified floor beneath it."""
    _cls, cov = class_tuples16()
    times = Counter(crystallization_time(H) for _T, H in cov)
    subsets = Counter(min_event_subset(H) for _T, H in cov)
    return {"window_histories": len(cov),
            "times": {str(k): v for k, v in sorted(times.items())},
            "min_event_subsets": {str(k): v
                                  for k, v in sorted(subsets.items())},
            "min_events": min(times) if times else None}


# ---- LAW 4: THE LADDER AT THE NEW ARENA ----------------------------------

def ladder_row(a):
    return memo(("ladder", a, mut("MUT-LADDER"), mut("MUT-PACKING")),
                lambda: _ladder_row(a))


def _ladder_row(a):
    """the budget-reading ladder at arity a.  The IMPOSSIBILITY half is the
    measured mass's own arithmetic: a budget-saturating round has mass n by
    the reading's definition, R rounds deposit 16R over 64 cells, and a
    homogeneous record needs 64 to divide 16R, so R must be a multiple of
    four.  The ACHIEVABILITY half is witness exhibition inside declared
    windows: the complete pool where the pool is small (a = 2 by matching
    enumeration, a = 8 whole), the canonical sample of SAT_SAMPLE_CAP
    otherwise, searched as an exact cover of the 64 cells under a node
    cap.  A search that ends at its cap is NOT-FOUND-WITHIN-CAP, published
    as capped and never as empty."""
    dist = packing_distribution(a)
    pool_count = dist.get(A.n, 0)
    row = {"a": a, "saturating": pool_count,
           "mass_per_round": A.n if pool_count else None,
           "predicted_modulus": (NC // math.gcd(NC, A.n)
                                 if pool_count else None),
           "impossible_budgets_derived": [R for R in range(1, LADDER_RMAX + 1)
                                          if (R * A.n) % NC],
           "achievable_budgets": [], "witness_status": None,
           "witness_window": None, "feasible": bool(pool_count)}
    if not pool_count:
        row["witness_status"] = "NO-SATURATING-ROUND"
        return row
    if a == 2:
        sample = saturating_matchings()
        row["witness_window"] = "COMPLETE-POOL"
    else:
        seed = [tuple(tuple(x for x in b) for b in P)
                for P in coset_rounds(a, "ABSTRACT")
                if sum(A.round_vec(P)) == A.n]
        tail = sat_round_sample(a, SAT_SAMPLE_CAP)
        seen_keys = {tuple(sorted(P)) for P in seed}
        sample = seed + [P for P in tail
                         if tuple(sorted(P)) not in seen_keys]
        if pool_count <= SAT_SAMPLE_CAP:
            row["witness_window"] = "COMPLETE-POOL"
        elif seed:
            row["witness_window"] = "COSET-SEED-PLUS-CANONICAL-SAMPLE"
        else:
            row["witness_window"] = "CANONICAL-SAMPLE"
    masks = [round_cell_mask(P) for P in sample]
    fullc = (1 << NC) - 1
    found = []
    nodes = [0]

    def dfs(start, covm, acc):
        nodes[0] += 1
        if found or nodes[0] > COVER_NODE_CAP:
            return
        if len(acc) == A.L:
            if covm == fullc:
                found.append(list(acc))
            return
        for i in range(start, len(masks)):
            m = masks[i]
            if covm & m:
                continue
            dfs(i, covm | m, acc + [i])
            if found:
                return

    dfs(0, 0, [])
    capped = nodes[0] > COVER_NODE_CAP and not found
    if found:
        row["achievable_budgets"] = [R for R in (4, 8) if R <= LADDER_RMAX]
        row["witness_status"] = "FOUND"
        row["witness_rounds"] = [
            [[list(x) for x in b] for b in sample[i]] for i in found[0]]
        row["witness_doubling"] = ("the R = 8 rung doubles the R = 4 "
                                   "witness multiset")
    elif row["witness_window"] == "COMPLETE-POOL" and not capped:
        row["witness_status"] = "REFUSED-COMPLETE"
    else:
        row["witness_status"] = "NOT-FOUND-WITHIN-CAP"
    row["witness_nodes"] = nodes[0]
    if mut("MUT-LADDER") and a == COMMITTED_ARITY:
        row["achievable_budgets"] = list(range(1, LADDER_RMAX + 1))
    return row


# ---- LAW 5: THE FORCING CENSUS ON THE DECLARED WINDOWS -------------------

def record_vector(H):
    r = {}
    for F in H:
        for u in F:
            for v in F:
                if u != v:
                    r[(u, v)] = r.get((u, v), 0) + 1
    return [r.get((x, A.vadd(x, l)), 0) for x in A.SITES for l in A.LINKS]


def leg2_history(part, H, corrupt=False):
    if corrupt:
        return True
    for F in H:
        for b in part:
            k = sum(1 for x in b if x in F)
            if k and k != len(b):
                return False
    return True


def leg3_record(part, rec):
    for b in part:
        for li in range(A.L):
            if len({rec[A.SI[x] * A.L + li] for x in b}) > 1:
                return False
    return True


SHIFT_T = tuple(A.CI[(A.vadd(x, l), l)] for (x, l) in A.CELLS)
GROVER = tuple(tuple(2 if i != j else 2 - A.L for j in range(A.L))
               for i in range(A.L))
COIN_ORDERS = ("G.D", "D.G")


def induced_cell_partition(part):
    bm = {x: bi for bi, b in enumerate(part) for x in b}
    d = {}
    for k, (x, l) in enumerate(A.CELLS):
        d.setdefault((bm[x], A.LINKS.index(l)), []).append(k)
    return tuple(sorted(tuple(sorted(v)) for v in d.values()))


def coupled_columns(rec, order, m):
    cols = []
    for (y, l) in A.CELLS:
        li = A.LINKS.index(l)
        ent = []
        for i in range(A.L):
            tgt = SHIFT_T[A.CI[(y, A.LINKS[i])]]
            e = (rec[A.SI[y] * A.L + li] if order == "G.D"
                 else rec[A.SI[y] * A.L + i]) % m
            if GROVER[i][li]:
                ent.append((tgt, e, GROVER[i][li]))
        cols.append(tuple(sorted(ent)))
    return tuple(cols)


def leg4_dynamics(cpart, rec, order, m):
    lab = [0] * NC
    for bi, b in enumerate(cpart):
        for k in b:
            lab[k] = bi
    cols = coupled_columns(rec, order, m)
    prof = []
    for k in range(NC):
        acc = {}
        for (tgt, e, coef) in cols[k]:
            key = (lab[tgt], e)
            acc[key] = acc.get(key, 0) + coef
        prof.append(tuple(sorted((kk, vv) for kk, vv in acc.items() if vv)))
    for b in cpart:
        if len({prof[k] for k in b}) > 1:
            return False
    return True


def admissible(part, H, rec, m):
    if not leg2_history(part, H, corrupt=mut("MUT-FORCING")):
        return False
    if not leg3_record(part, rec):
        return False
    cp = induced_cell_partition(part)
    return (leg4_dynamics(cp, rec, COIN_ORDERS[0], m)
            and leg4_dynamics(cp, rec, COIN_ORDERS[1], m))


def forcing_census():
    return memo(("forcing", mut("MUT-FORCING"), mut("MUT-MENU"),
                 mut("MUT-CORPUS")), _forcing_census)


def _forcing_census():
    surv = survivors()
    disc = tuple(sorted((x,) for x in A.SITES))
    corp = corpora()
    out = {}
    for a in ARITIES:
        entry = {"a": a}
        c = corp[a]
        if c["refusal"]:
            entry["refusal"] = c["refusal"]
            out[a] = entry
            continue
        lin_set = {tuple(sorted(tuple(sorted(b)) for b in P))
                   for P in c["singles_linear"]}
        class_set = {tuple(sorted(tuple(sorted(g)) for g in
                           A.CLASSES[nm])) for nm in A.CLASS_NAMES}
        for tag, rounds in (("ABSTRACT", c["singles_abstract"]),
                            ("F4-LINEAR", c["singles_linear"])):
            rows = []
            m_blind = True
            for P in rounds:
                H = tuple(A.round_events(P))
                rec = record_vector(H)
                adm = [p for p in surv if admissible(p, H, rec, M_FORK[1])]
                for m in (M_FORK[0], M_FORK[2]):
                    if [p for p in surv
                            if admissible(p, H, rec, m)] != adm:
                        m_blind = False
                if disc not in [tuple(sorted(p)) for p in adm]:
                    raise GateFail("G-LAW5-FORCING16 :: the discrete "
                                   "partition is not admissible at a round")
                key = tuple(sorted(tuple(sorted(b)) for b in P))
                rows.append({
                    "admissible": len(adm),
                    "non_unique": len(adm) > 1,
                    "joiners": len(adm) - 1,
                    "is_parallel_class": key in class_set,
                    "is_linear_coset_round": key in lin_set})
            entry[tag] = {
                "rounds": len(rows),
                "non_unique": sum(1 for r in rows if r["non_unique"]),
                "non_unique_that_are_parallel_classes":
                    sum(1 for r in rows
                        if r["non_unique"] and r["is_parallel_class"]),
                "joiner_counts": {str(k): v for k, v in sorted(Counter(
                    r["joiners"] for r in rows if r["non_unique"]).items())},
                "thesis_holds_per_object": all(
                    r["non_unique"] == r["is_parallel_class"]
                    for r in rows),
                "m_blind_across_the_fork": m_blind}
        multi = tuple_histories(c["covering_tuples"])
        nu = 0
        for H in multi:
            rec = record_vector(H)
            adm = [p for p in surv if admissible(p, H, rec, M_FORK[1])]
            if disc not in [tuple(sorted(p)) for p in adm]:
                raise GateFail("G-LAW5-FORCING16 :: the discrete partition "
                               "is not admissible at a covering tuple")
            if len(adm) > 1:
                nu += 1
        entry["covering_tuples"] = {"histories": len(multi),
                                    "non_unique": nu}
        out[a] = entry
    return out


# ---- LAW 6: THE UNION CENSUS AT THE NEW ARENA ----------------------------

def sec2_census():
    return memo(("sec2", mut("MUT-SEC2-THEOREM")), _sec2_census)


def _sec2_census():
    sector_pairs = tuple(sorted({tuple(sorted((x, A.vadd(x, l))))
                                 for x in A.SITES for l in A.LINKS}))
    seam_line = A.CLASSES["CL4"][0]
    seam_declared = sum(1 for p in sector_pairs
                        if set(p) <= set(seam_line))
    amap, bmap = {}, {}
    for i, s in enumerate(seam_line):
        amap[s] = ("S", i)
        bmap[s] = ("S", i)
    for s in A.SITES:
        amap.setdefault(s, ("A", s))
        bmap.setdefault(s, ("B", s))
    uact = sorted(set(amap.values()) | set(bmap.values()), key=repr)
    urel = Counter()
    for mp in (amap, bmap):
        for (u, v) in sector_pairs:
            urel[frozenset((mp[u], mp[v]))] += 1
    # the parent's tripartite characterisation, evaluated as data: joined
    # exactly when the difference is off the undeclared span?
    uspan = frozenset(A.vmul(t, A.UNDECLARED) for t in A.el)
    off_span_pairs = sum(1 for x, y in combinations(A.SITES, 2)
                         if A.vadd(x, y) not in uspan)
    rows, theorem_bad = [], []
    for a in ARITIES:
        span = lawful = free = groups = 0
        min_inside = None
        for gsel in combinations(range(len(uact)), a):
            acts = [uact[i] for i in gsel]
            prs = [frozenset(p) for p in combinations(acts, 2)]
            new = [p for p in prs if p not in urel]
            foreign = [p for p in new if {x[0] for x in p} == {"A", "B"}]
            within = [p for p in new if p not in foreign]
            dbl = [p for p in prs if p in urel]
            if mut("MUT-SEC2-THEOREM") and a == PARENT_ARITY and dbl:
                dbl = []
            groups += 1
            if (len(foreign) + len(within) + len(dbl) != math.comb(a, 2)
                    or len(foreign) > (a * a) // 4):
                theorem_bad.append(str(gsel))
            if foreign:
                span += 1
                inside = len(within) + len(dbl)
                if min_inside is None or inside < min_inside:
                    min_inside = inside
                if not within:
                    lawful += 1
                    if not dbl:
                        free += 1
        rows.append({"a": a, "groups": groups, "seam_spanning": span,
                     "within_sector_free": lawful,
                     "opens_a_pair_inside_a_sector": span - lawful,
                     "obstruction_free": free,
                     "measured_min_within_sector_pairs": min_inside,
                     "max_cut_of_the_complete_graph": (a * a) // 4,
                     "forced_inside_bound":
                         math.comb(a, 2) - (a * a) // 4})
    return {"rows": rows, "identity_violations": theorem_bad,
            "union_carriers": len(uact),
            "union_realised_pairs": len(urel),
            "union_doubled_pairs": sum(1 for v in urel.values() if v > 1),
            "sector_link_pairs": len(sector_pairs),
            "seam_pairs_that_are_declared_links": seam_declared,
            "off_undeclared_span_pairs": off_span_pairs,
            "tripartite_characterisation_holds":
                len(sector_pairs) == off_span_pairs}


# ---- THE PRINCIPLE CENSUS AND THE CONDITIONAL ----------------------------

def principle_census():
    return memo(("principles", mut("MUT-PRINCIPLE"), mut("MUT-PACKING"),
                 mut("MUT-READING"), mut("MUT-LADDER")), _principle_census)


def _principle_census():
    abstract_orders = sorted({len(H) for H in SUBS})
    linear_orders = sorted({len(H) for H in F4SUBS})
    rows = []
    for a in range(1, A.n + 1):
        dist = packing_distribution(a)
        mx = max(dist)
        sat = dist.get(A.n, 0)
        lad = ladder_row(a) if sat else None
        cover = ("YES-WITNESS" if lad and lad["witness_status"] == "FOUND"
                 else "NO-COMPLETE" if lad and lad["witness_status"]
                 == "REFUSED-COMPLETE"
                 else "NOT-WITHIN-CAP" if lad
                 else "NO-SATURATING-ROUND")
        rc = (A.n % a == 0)
        if mut("MUT-PRINCIPLE") and a == COMMITTED_ARITY:
            rc = not rc
        rows.append({
            "a": a,
            "round_completeness": rc,
            "saturation_at_the_budget": bool(sat),
            "saturation_is_maximality": mx == A.n,
            "subgroup_order_available_abstract": a in abstract_orders,
            "subgroup_order_available_linear": a in linear_orders,
            "cover_at_R_equals_L": cover,
            "nontrivial": 1 < a < A.n})
    return {"rows": rows, "abstract_orders": abstract_orders,
            "linear_orders": linear_orders}
# ===========================================================================
# SECTION 3.  THE TRANSPORT DECISION PROCEDURE (the parent's, verbatim)
# ===========================================================================

def arow(a, feasible, measured, note):
    return {"a": a, "feasible": bool(feasible), "measured": measured,
            "note": note}


def transport_word(parent_value, rows, rule=None):
    """the parent's procedure, a pure function of its rows; infeasible rows
    are CARRIED and never scored (#34)."""
    rule = t_a_reading if rule is None else rule
    if mut("MUT-TRANSPORT"):
        return WORDS[0], {"reason": "SHORT-CIRCUITED"}
    feas = [r for r in rows if r["feasible"]]
    if not feas:
        return "BREAKS", {"reason": "NO-FEASIBLE-ROW", "carried": len(rows)}
    lit = [r for r in feas if r["measured"] == parent_value]
    ta = [r for r in feas if r["measured"] == rule(parent_value, r["a"])]
    disc = [r for r in feas if rule(parent_value, r["a"]) != parent_value]
    ev = {"feasible": len(feas), "carried": len(rows),
          "t_literal_agrees": len(lit), "t_a_agrees": len(ta),
          "rows_discriminating_a_from_literal": len(disc),
          "measured": [[r["a"], r["measured"]] for r in feas],
          "carried_rows": [[r["a"], "INFEASIBLE-CARRIED"]
                           for r in rows if not r["feasible"]],
          "t_a": [[r["a"], rule(parent_value, r["a"])] for r in feas]}
    if len(ta) == len(feas):
        ev["stamp"] = "DISCRIMINATED" if disc else "UNDISCRIMINATED"
        return "LAW-IN-A", ev
    if len(lit) == len(feas):
        ev["stamp"] = "DISCRIMINATED" if disc else "UNDISCRIMINATED"
        return "NEEDS-3", ev
    ev["stamp"] = "FAILS-BOTH"
    ev["failing_arities"] = sorted(
        r["a"] for r in feas
        if r["measured"] != parent_value
        and r["measured"] != rule(parent_value, r["a"]))
    return "BREAKS", ev


def statement_word(rows):
    feas = [r for r in rows if r["feasible"]]
    if not feas:
        return "BREAKS", {"reason": "NO-FEASIBLE-ROW", "carried": len(rows)}
    bad = [r["a"] for r in feas if not r["measured"]]
    ev = {"feasible": len(feas), "carried": len(rows),
          "holds_at": sorted(r["a"] for r in feas if r["measured"]),
          "carried_rows": [[r["a"], "INFEASIBLE-CARRIED"]
                           for r in rows if not r["feasible"]],
          "fails_at": sorted(bad)}
    if bad:
        return "BREAKS", ev
    return "LAW-IN-A", ev


# ===========================================================================
# SECTION 4.  THE RUN
# ===========================================================================

LD = Ledger()
TR = Transcript()
SEAL = Seal()
CR = CountRegistry()
RS = ReadSet(REPO)
AN = None
R = {}


def read_source_text(rel, expect):
    path = os.path.join(REPO, rel)
    with open(path, "rb") as fh:
        raw = fh.read()
    got = hashlib.sha256(raw).hexdigest()[:12]
    if got != expect:
        raise GateFail("G-SOURCES :: %s sha %s != %s" % (rel, got, expect))
    return raw.decode("utf-8"), got


def jpath(obj, path):
    """a declared JSON path; a decimal component indexes a list, which the
    parent's receipt uses for its transport rows."""
    cur = obj
    for part in path.split("/"):
        if isinstance(cur, list):
            if not part.isdigit() or int(part) >= len(cur):
                raise GateFail("G-PATH-ANCHORS :: path %s missing at %s"
                               % (path, part))
            cur = cur[int(part)]
            continue
        if not isinstance(cur, dict) or part not in cur:
            raise GateFail("G-PATH-ANCHORS :: path %s missing at %s"
                           % (path, part))
        cur = cur[part]
    return cur


def quote_ints(text):
    return [int(t.replace(",", ""))
            for t in re.findall(r"(?<![\w.])(\d[\d,]*)(?!\.\d)(?!\w)", text)]


def _probe_arena():
    return A.characteristic + 1 if mut("MUT-ARENA") else A.characteristic


def order_predicate(fid_row, other_row):
    """the ordering the fidelity gate owns, factored out so a recipe can be
    proved to MOVE it on fixed inputs rather than only inside a run."""
    return other_row > fid_row if not mut("MUT-ORDER") else fid_row > other_row


def _probe_agg():
    return "SLOT" if mut("MUT-AGG") else "STATEMENT"


def full_run(paper_text, paper_rel=PAPER_PATH, write=True, break_anchor=None):
    global AN, R
    R = {}
    src = {}
    prov = []
    for (sid, rel, sha, why) in SOURCES:
        if mut("MUT-SOURCE") and sid == SOURCES[0][0]:
            sha = "0" * 12
        txt, got = read_source_text(rel, sha)
        src[sid] = txt
        prov.append({"id": sid, "path": rel, "sha256_12": got, "why": why})
    CR.measured("n_sources", len(SOURCES), "len of the frozen source list")
    LD.gate("G-SOURCES", len(prov) == len(SOURCES),
            CR.stmt("every runtime input is a hash-pinned artifact of this "
                    "unit's frozen declaration; {k} sources are read and "
                    "each one's sha256 prefix is compared with the "
                    "declaration before its bytes are used; the mutable "
                    "programme ledger is not among them",
                    k="n_sources"),
            {"sources": prov})
    R["provenance"] = SEAL.seal("provenance", prov, "G-SOURCES")

    # ---- PATH-VALUE ANCHORS ------------------------------------------
    ndep_json = json.loads(src["A-NDEPREC"])
    parent_json = json.loads(src["A-PARENTREC"])
    by_source = {"A-NDEPREC": ndep_json, "A-PARENTREC": parent_json}
    pa = []
    for (aid, sid, path, expect, consumer) in PATH_ANCHORS:
        if (mut("MUT-PATH") and aid == PATH_ANCHORS[0][0]
                and isinstance(expect, int)):
            expect = expect + 1
        got = jpath(by_source[sid], path)
        if got != expect:
            raise GateFail("G-PATH-ANCHORS :: %s reads %r not %r"
                           % (aid, got, expect))
        pa.append({"id": aid, "source": sid, "path": path, "value": got,
                   "consumer": consumer})
    CR.measured("n_path_anchors", len(pa), "len of the path-anchor table")
    LD.gate("G-PATH-ANCHORS", len(pa) == len(PATH_ANCHORS),
            CR.stmt("{k} path-value anchors bind the (path, value) pair "
                    "into TWO committed receipts -- the parent's and "
                    "NDEP's -- so a path drift that silently substituted "
                    "another sealed number dies here even though no number "
                    "would move",
                    k="n_path_anchors"),
            {"anchors": pa})
    R["path_anchors"] = SEAL.seal("path_anchors", pa, "G-PATH-ANCHORS")
    PV = {aid: v for (aid, _s, _p, v, _c) in PATH_ANCHORS}

    # ---- VERBATIM ANCHORS --------------------------------------------
    AN = AnchorSet([Anchor(nm, needle, sid, cons, why)
                    for (nm, sid, needle, cons, why) in VERBATIM])
    AN.locate(src, paper_text, broken=break_anchor)
    CR.measured("n_verbatim", len(VERBATIM), "len of the verbatim table")
    LD.gate("G-VERBATIM", True,
            CR.stmt("{k} verbatim-text anchors bind QUOTE FIDELITY: each "
                    "needle occurs exactly once in the pinned source and at "
                    "least once in this paper's own rendering under the "
                    "normalisation the era's text gates use, and each is "
                    "readable only through an accessor that records the "
                    "read",
                    k="n_verbatim"),
            {"anchors": [{"id": nm, "source": sid, "consumer": cons,
                          "chars": len(canon(needle))}
                         for (nm, sid, needle, cons, _w) in VERBATIM]})

    # ---- THE ARENA, FIXED --------------------------------------------
    sq = AN.read("V-SQRT16", "G-ARENA16")
    hq = AN.read("V-HYPOTHESIS", "G-ARENA16")
    hyp_ints = quote_ints(hq)
    CR.measured("n_actors", A.n, "the arena's site count, computed")
    CR.measured("q_order", A.q, "the field order, computed")
    CR.measured("n_links", A.L, "the declared link count")
    CR.measured("n_cells", NC, "the cell count, computed as sites x links")
    CR.measured("n_classes", len(A.CLASSES), "the parallel classes, computed")
    CR.measured("characteristic", A.characteristic,
                "the field characteristic, computed from its own addition")
    CR.measured("links_generate", len(G8),
                "the order of the subgroup the declared links generate")
    LD.gate("G-ARENA16",
            A.q * A.q == A.n and _probe_arena() == A.characteristic
            and A.characteristic != A.q
            and "characteristic" in sq and "part company" in sq
            and len(A.CELLS) == A.n * A.L and len(A.CLASSES) == A.q + 1
            and hyp_ints[-2:] == [len(G8), A.n]
            and len(G8) == PV["P-N16-GEN"]
            and all(l[0] in (0, 1) for l in A.LINKS),
            CR.stmt("the arena is AG(2, {q}) and it does not move: {n} "
                    "actors, {c} cells, {p} parallel classes -- and the "
                    "characteristic is {ch}, computed from the field's own "
                    "addition and DIFFERENT from the field order for the "
                    "first time in the corpus, which is the separation "
                    "NDEP's own sentence names. The declared links span a "
                    "subgroup of order {g}, re-measuring the failed "
                    "hypothesis NDEP's quotation records, with both of the "
                    "quotation's orders parsed and matched",
                    q="q_order", n="n_actors", c="n_cells", p="n_classes",
                    ch="characteristic", g="links_generate"),
            {"n": A.n, "q": A.q, "L": A.L, "cells": NC,
             "characteristic": A.characteristic,
             "parallel_classes": len(A.CLASSES),
             "declared_links": [list(l) for l in A.LINKS],
             "undeclared_direction": list(A.UNDECLARED),
             "links_generate_order": len(G8),
             "quotation_orders_parsed": hyp_ints[-2:]})
    R["arena"] = SEAL.seal(
        "arena", {"declaration": [list(t) for t in arena_declaration()],
                  "n": A.n, "q": A.q, "L": A.L, "cells": NC,
                  "characteristic": A.characteristic,
                  "parallel_classes": len(A.CLASSES),
                  "links_generate_order": len(G8),
                  "arities": list(ARITIES),
                  "committed_arity": COMMITTED_ARITY,
                  "parent_arity": PARENT_ARITY,
                  "idle_arities": list(IDLE_ARITIES),
                  "ladder_search_bound": LADDER_RMAX,
                  "sat_sample_cap": SAT_SAMPLE_CAP,
                  "cover_node_cap": COVER_NODE_CAP,
                  "prefix_window": PREFIX_WINDOW,
                  "coin_modulus_fork": list(M_FORK)}, "G-ARENA16")
    R["preregistered_outcomes"] = SEAL.seal(
        "preregistered_outcomes",
        [{"word": w, "meaning": mm, "feasibility": f}
         for (w, mm, f) in PREREGISTERED], "G-ARENA16")

    # ---- THE TWO READINGS, PRE-REGISTERED ----------------------------
    rq = AN.read("V-REGISTRATION", "G-READINGS")
    lq = AN.read("V-LINEAR", "G-READINGS")
    suq = AN.read("V-SUCCESSOR", "G-READINGS")
    m_reg = re.search(r"subgroup orders ([\d,]+) =", rq)
    reg_orders = ([int(x) for x in m_reg.group(1).split(",")]
                  if m_reg else [])
    m_lin = re.search(r"\(sizes ([\d,]+)\)", lq)
    lin_orders = ([int(x) for x in m_lin.group(1).split(",")]
                  if m_lin else [])
    f4_live = A.f4_subspaces(SUBS)
    abstract_orders = sorted({len(H) for H in SUBS})
    linear_orders = sorted({len(H) for H in f4_live})
    divisors = [x for x in range(1, A.n + 1) if A.n % x == 0]
    CR.measured("n_abstract_subgroups", len(SUBS),
                "abstract subgroups of the translation group, by closure")
    CR.measured("n_linear_subspaces", len(f4_live),
                "F4-linear subspaces among them, by scalar closure, "
                "evaluated live at this gate")
    CR.measured("n_abstract_orders", len(abstract_orders), "counted")
    CR.measured("n_linear_orders", len(linear_orders), "counted")
    LD.gate("G-READINGS",
            reg_orders == abstract_orders == divisors
            and lin_orders == linear_orders
            and len(SUBS) == PV["P-N16-SUBS"]
            and len(f4_live) == PV["P-N16-F4"]
            and set(f4_live) == set(F4SUBS)
            and set(f4_live) <= set(SUBS)
            and PRIMARY_READING == READINGS[0]
            and "F4-LINEAR" in lq
            and "which notion of subgroup" in suq,
            CR.stmt("the word subgroup is PRE-REGISTERED in two readings "
                    "before any measurement row runs, exactly as the "
                    "sharpened registration orders and the parent's own "
                    "successor register requires: the ABSTRACT lattice of "
                    "C2^4 has "
                    "{s} subgroups whose {ao} distinct orders are measured "
                    "to equal the divisors of the actor count -- the "
                    "registration's coincidence, its five orders parsed "
                    "from the frozen pin and matched -- while the F4-LINEAR "
                    "lattice has {f} subspaces with {lo} distinct orders, "
                    "the quotation's three sizes parsed and matched. The "
                    "linear reading is the pre-registered PRIMARY; the "
                    "abstract reading is reported beside it and the two are "
                    "never merged",
                    s="n_abstract_subgroups", ao="n_abstract_orders",
                    f="n_linear_subspaces", lo="n_linear_orders"),
            {"abstract_subgroups": len(SUBS),
             "abstract_orders": abstract_orders,
             "abstract_order_counts": sorted(Counter(
                 len(H) for H in SUBS).items()),
             "linear_subspaces": len(f4_live),
             "linear_orders": linear_orders,
             "linear_order_counts": sorted(Counter(
                 len(H) for H in f4_live).items()),
             "divisors_of_n": divisors,
             "registration_orders_parsed": reg_orders,
             "linear_sizes_parsed": lin_orders,
             "primary_reading": PRIMARY_READING})
    R["readings"] = SEAL.seal(
        "readings",
        {"primary": PRIMARY_READING, "readings": list(READINGS),
         "abstract_subgroups": len(SUBS),
         "abstract_orders": abstract_orders,
         "abstract_order_counts": sorted(Counter(
             len(H) for H in SUBS).items()),
         "linear_subspaces": len(F4SUBS), "linear_orders": linear_orders,
         "linear_order_counts": sorted(Counter(
             len(H) for H in F4SUBS).items()),
         "divisors_of_n": divisors,
         "coincidence": "the abstract orders EQUAL the divisors, so n = 16 "
                        "cannot separate divisibility from abstract-"
                        "subgroup availability; only the linear reading "
                        "separates, exactly as the sharpened registration "
                        "says",
         "disagreement_is_a_result": True}, "G-READINGS")

    # ---- THE FIDELITY GATE: BEFORE ANY NEW ROW -----------------------
    cls16, cov16 = class_tuples16()
    fid_scan = memo(("fidscan", mut("MUT-FIDELITY")),
                    lambda: route_scan([H for _T, H in cov16]))
    cryst = Counter(crystallization_time(H) for _T, H in cov16)
    floors_ndep = Counter(min_event_subset(H) for _T, H in cov16)
    fid = {"class_tuples": len(cls16), "covering_tuples": len(cov16),
           "route_comparisons": fid_scan["comparisons"],
           "route_mismatches": fid_scan["mismatches"],
           "route_positive": fid_scan["positive"],
           "route_positive_empty_prefix":
               fid_scan["positive_at_the_empty_prefix"],
           "permutation_window": fid_scan["window_size"],
           "crystallization_at_seven": cryst.get(2 * A.q - 1, 0),
           "floor_at_six": floors_ndep.get(2 * (A.q - 1), 0),
           "counting_floor": counting_floor(A.n)}
    want = {row: PV[aid] for (row, aid) in FIDELITY_PREREG}
    prereg_digest = digest([list(t) for t in FIDELITY_PREREG])
    agree = sorted(k for k in want if fid[k] == want[k])
    CR.measured("fid_rows", len(want),
                "len of the sealed fidelity pre-registration")
    CR.measured("fid_agree", len(agree), "count of agreeing substrate rows")
    LD.gate("G-CONSTRUCTOR-FIDELITY",
            len(agree) == len(want) and set(fid) == set(want)
            and prereg_digest == FIDELITY_PREREG_DIGEST,
            CR.stmt("this unit's constructor is run at the COMMITTED "
                    "WINDOW AT n = {n} first -- NDEP's own covering class "
                    "tuples, its permutation window, its crystallization "
                    "and floor rows -- and its substrate is compared row "
                    "by row against the committed counts read at declared "
                    "JSON paths: {ok} of {k} agree, the row set a SEALED "
                    "pre-registration carrying its own digest. This gate "
                    "is a FIDELITY LEG and not a finding, and no "
                    "measurement at any other row is taken before it "
                    "passes",
                    n="n_actors", ok="fid_agree", k="fid_rows"),
            {"measured": fid, "anchored": want, "agreeing": agree,
             "preregistered_rows": [list(t) for t in FIDELITY_PREREG],
             "preregistration_digest": prereg_digest,
             "stamp": "FIDELITY-LEG-ONLY"})
    R["fidelity"] = SEAL.seal(
        "fidelity", {"measured": fid, "anchored": want,
                     "agree": len(agree), "rows": len(want),
                     "crystallization_counter":
                         {str(k): v for k, v in sorted(cryst.items())},
                     "floor_counter":
                         {str(k): v for k, v in sorted(floors_ndep.items())},
                     "stamp": "FIDELITY-LEG-ONLY: no law value is read off "
                              "this leg; it licenses the sentence that the "
                              "same constructor closes NDEP's window"},
        "G-CONSTRUCTOR-FIDELITY")
    fidelity_row = LD.index_of("G-CONSTRUCTOR-FIDELITY")

    first_measurement_row = len(LD.rows) + 1
    order_ok = order_predicate(fidelity_row, first_measurement_row)
    CR.measured("fidelity_row", fidelity_row,
                "the ledger index at which the fidelity gate fired")
    LD.gate("G-FIDELITY-FIRST", order_ok,
            CR.stmt("the fidelity gate fired at ledger row {r}, before any "
                    "substrate, corpus or law measurement row; the "
                    "ordering predicate is evaluated on the ledger's own "
                    "indices rather than asserted",
                    r="fidelity_row"),
            {"fidelity_row": fidelity_row})

    # ---- THE PACKING RULE EXTENDS (count level + declared prefix) ----
    pq = AN.read("V-PACKING", "G-PACKING-EXTENDS16")
    packing_site_numeral = quote_ints(pq)
    pre_with = packings_prefix(COMMITTED_ARITY, PREFIX_WINDOW, False)
    pre_without = packings_prefix(COMMITTED_ARITY, PREFIX_WINDOW, True)
    dist4 = packing_distribution(COMMITTED_ARITY)
    dp_total4 = sum(dist4.values())
    CR.measured("prefix_window", PREFIX_WINDOW, "the declared object window")
    CR.measured("dp_total_committed", dp_total4,
                "the census total at the committed arity, by DP")
    CR.measured("closed_total_committed",
                closed_grouping_count(COMMITTED_ARITY),
                "the multinomial closed form at the committed arity")
    LD.gate("G-PACKING-EXTENDS16",
            pre_with == pre_without and len(pre_with) == PREFIX_WINDOW
            and packing_site_numeral == [9]
            and dp_total4 == closed_grouping_count(COMMITTED_ARITY)
            and all(sum(len(g) for g in p) == A.n for p in pre_with[:50]),
            CR.stmt("the packing rule is the PARENT'S OWN, its quotation "
                    "parsed to confirm it was written at nine sites and "
                    "transported here unchanged: where the event size "
                    "divides the actor count the maximal-packing route and "
                    "the partition route return the same objects. DISCLOSED "
                    "DEVIATION, driven by scale: the parent compared its "
                    "routes over whole pools of hundreds, while this "
                    "arena's pools are millions, so the object-level "
                    "comparison runs on a declared prefix window of {w} "
                    "objects in the recursion's own order and the whole-"
                    "pool identity is carried at the COUNT level, the "
                    "census total {d} against the multinomial closed form "
                    "{c}",
                    w="prefix_window", d="dp_total_committed",
                    c="closed_total_committed"),
            {"prefix_objects_agree": pre_with == pre_without,
             "prefix_window": PREFIX_WINDOW,
             "dp_total": dp_total4,
             "closed_form_total": closed_grouping_count(COMMITTED_ARITY),
             "quotation_site_numeral": packing_site_numeral,
             "disclosed": "count-level whole-pool identity plus a declared "
                          "object prefix, in place of the parent's whole-"
                          "pool object identity"})

    # ---- THE SUBSTRATE CENSUS ----------------------------------------
    oq = AN.read("V-OUTOFSCOPE", "G-SUBSTRATE-CENSUS")
    ndep_constant = quote_ints(oq)[1]
    subrows = []
    for a in ARITIES:
        dist = packing_distribution(a)
        tot = sum(dist.values())
        mx = max(dist)
        subrows.append({
            "a": a, "blocks_per_round": A.n // a,
            "idle_actors": A.n - a * (A.n // a),
            "groupings": tot, "closed_form": closed_grouping_count(a),
            "max_weight": mx, "budget": A.n,
            "saturating_budget": dist.get(A.n, 0),
            "saturating_maximum": dist[mx],
            "saturation_is_maximality": mx == A.n,
            "odd_weight_groupings": sum(c for w, c in dist.items()
                                        if w % 2)})
    parent_sub = {2: ("P-SUB2-G", "P-SUB2-SAT"), 3: ("P-SUB3-G", "P-SUB3-SAT"),
                  4: ("P-SUB4-G", "P-SUB4-SAT"), 5: ("P-SUB5-G", "P-SUB5-SAT")}
    both_n = [{"a": a, "n9_groupings": PV[parent_sub[a][0]],
               "n9_saturating_budget": PV[parent_sub[a][1]],
               "n16_groupings": r["groupings"],
               "n16_saturating_budget": r["saturating_budget"]}
              for a, r in zip(ARITIES, subrows)]
    a2row = subrows[0]
    CR.measured("n_arities", len(ARITIES), "len of the declared arity window")
    CR.measured("census_total_a4",
                [r for r in subrows if r["a"] == COMMITTED_ARITY][0]
                ["groupings"], "the closed window, censused")
    CR.measured("a2_saturating", a2row["saturating_budget"],
                "budget-saturating groupings at the smallest arity")
    CR.measured("a2_parent_saturating", PV["P-SUB2-SAT"],
                "the parent's own a = 2 budget count, anchored")
    CR.measured("witness_max_a4",
                [r for r in subrows if r["a"] == COMMITTED_ARITY][0]
                ["max_weight"], "the maximum round incidence at a = q")
    LD.gate("G-SUBSTRATE-CENSUS",
            all(r["groupings"] == r["closed_form"] for r in subrows)
            and [r for r in subrows if r["a"] == COMMITTED_ARITY][0]
            ["groupings"] == ndep_constant
            and [r for r in subrows if r["a"] == COMMITTED_ARITY][0]
            ["max_weight"] == PV["P-N16-WIT"]
            and a2row["saturating_budget"] > 0
            and PV["P-SUB2-SAT"] == 0
            and all(r["odd_weight_groupings"] == 0 for r in subrows)
            and len(subrows) == len(ARITIES),
            CR.stmt("the substrate is censused at every declared arity by "
                    "an exact dynamic programme over the actor-subset "
                    "lattice, every total agreeing with its multinomial "
                    "closed form -- including the {c4} groupings NDEP "
                    "declared out of scope, whose constant is parsed from "
                    "its own receipt and matched, and whose maximum round "
                    "incidence {mw} equals NDEP's anchored witness. Every "
                    "grouping weight is even, the characteristic's own "
                    "fingerprint; and the budget-saturating count at the "
                    "smallest arity is {a2} against the parent arena's "
                    "anchored {p2}, so the class the parent measured EMPTY "
                    "at two actors is non-empty at this arena",
                    c4="census_total_a4", mw="witness_max_a4",
                    a2="a2_saturating", p2="a2_parent_saturating"),
            {"rows": subrows, "both_arena_rows": both_n,
             "ndep_out_of_scope_constant_parsed": ndep_constant})
    R["substrate"] = SEAL.seal(
        "substrate", {"rows": subrows, "both_arena_rows": both_n},
        "G-SUBSTRATE-CENSUS")

    # ---- THE CORPUS RULE (the coset windows) -------------------------
    corp = corpora()
    corprows = []
    for a in ARITIES:
        c = corp[a]
        entry = {"a": a,
                 "singles_abstract": len(c["singles_abstract"]),
                 "singles_linear": len(c["singles_linear"]),
                 "window_basis": len(c["window_basis"]),
                 "saturating_abstract_rounds":
                     len(c["saturating_abstract_rounds"]),
                 "covering_tuples": len(c["covering_tuples"]),
                 "refusal": c["refusal"]}
        corprows.append(entry)
    refused = [r for r in corprows if r["refusal"]]
    CR.measured("corpus_rows", len(corprows), "one row per declared arity")
    CR.measured("corpus_refusals", len(refused),
                "arities the committed grammar refuses under both readings")
    CR.measured("a4_covering", [r for r in corprows
                                if r["a"] == COMMITTED_ARITY][0]
                ["covering_tuples"],
                "covering tuples at the committed arity")
    CR.measured("a2_covering", [r for r in corprows if r["a"] == 2][0]
                ["covering_tuples"],
                "covering tuples at the smallest arity")
    order_counts_abs = Counter(len(H) for H in SUBS)
    order_counts_lin = Counter(len(H) for H in F4SUBS)
    LD.gate("G-CORPUS-RULE",
            len(corprows) == len(ARITIES)
            and all((r["refusal"] is None) == (r["singles_abstract"] > 0)
                    for r in corprows)
            and all(r["singles_abstract"] == order_counts_abs.get(r["a"], 0)
                    and r["singles_linear"]
                    == order_counts_lin.get(r["a"], 0)
                    for r in corprows)
            and all(r["refusal"] is not None
                    and r["refusal"]["order_a_abstract_subgroups"] == 0
                    and r["refusal"]["order_a_linear_subspaces"] == 0
                    for r in corprows if r["a"] in IDLE_ARITIES)
            and [r for r in corprows if r["a"] == COMMITTED_ARITY][0]
            ["covering_tuples"] == PV["P-N16-COV"],
            CR.stmt("one corpus rule is applied at every arity: the "
                    "single-round window is the COSET WINDOW each reading "
                    "admits -- complete within its declared class -- and "
                    "the multi-round window is the covering R = L tuples "
                    "over the budget-saturating coset rounds, NDEP's own "
                    "covering-class rule; at the committed arity it "
                    "returns exactly NDEP's {c4} covering tuples and at "
                    "the smallest arity {c2} more. At {rf} arities the "
                    "committed grammar REFUSES under both readings -- the "
                    "event size divides neither the actor count nor any "
                    "measured coset order -- and the refusal is published "
                    "as the measurement, never patched",
                    c4="a4_covering", c2="a2_covering",
                    rf="corpus_refusals"),
            {"rows": corprows})
    R["corpus"] = SEAL.seal("corpus", corprows, "G-CORPUS-RULE")

    # ---- LAW 1: THE NAMING ROUTES ------------------------------------
    scan_a2 = memo(("scan_a2", mut("MUT-NAMING"), mut("MUT-CORPUS")),
                   lambda: route_scan(
                       single_histories(corp[2]["singles_abstract"])
                       + tuple_histories(corp[2]["covering_tuples"]),
                       corrupt=mut("MUT-NAMING")))
    scan_a4s = memo(("scan_a4s", mut("MUT-NAMING"), mut("MUT-CORPUS")),
                    lambda: route_scan(
                        single_histories(corp[4]["singles_abstract"]),
                        corrupt=mut("MUT-NAMING")))
    lin_keys = {tuple(sorted(tuple(sorted(b)) for b in P))
                for P in corp[4]["singles_linear"]}
    lin_idx = [i for i, P in enumerate(corp[4]["singles_abstract"])
               if tuple(sorted(tuple(sorted(b)) for b in P)) in lin_keys]
    lin_cmp = sum(scan_a4s["per_history"][i][0] for i in lin_idx)
    lin_bad = sum(scan_a4s["per_history"][i][2] for i in lin_idx)
    total_cmp = (scan_a2["comparisons"] + scan_a4s["comparisons"]
                 + fid_scan["comparisons"])
    total_bad = (scan_a2["mismatches"] + scan_a4s["mismatches"]
                 + fid_scan["mismatches"])
    total_pos = (scan_a2["positive"] + scan_a4s["positive"]
                 + fid_scan["positive"])
    CR.measured("naming_comparisons", total_cmp,
                "route comparisons over every window at both arities")
    CR.measured("naming_mismatches", total_bad, "route disagreements")
    CR.measured("naming_positive", total_pos,
                "permutations landing inside the stabilizer")
    CR.measured("naming_negative", total_cmp - total_pos,
                "permutations landing outside it")
    CR.measured("naming_linear_comparisons", lin_cmp,
                "the linear-window share of the committed-arity singles")
    LD.gate("G-LAW1-NAMING16",
            total_bad == 0 and total_pos > 0 and total_pos < total_cmp
            and lin_bad == 0 and lin_cmp > 0,
            CR.stmt("two routes are compared AS SETS OF PERMUTATIONS on "
                    "the declared window at every prefix of every window "
                    "history at both coset arities: route A applies the "
                    "definition through event masks and route B reads the "
                    "participation-signature table and nothing else. {c} "
                    "comparisons, {m} mismatches, {p} inside the "
                    "stabilizer and {ng} outside it, so both directions "
                    "are live; the linear windows contribute {lc} "
                    "comparisons of their own and the two readings "
                    "disagree nowhere on this leg",
                    c="naming_comparisons", m="naming_mismatches",
                    p="naming_positive", ng="naming_negative",
                    lc="naming_linear_comparisons"),
            {"a2": {k: v for k, v in scan_a2.items()
                    if k != "per_history"},
             "a4_singles": {k: v for k, v in scan_a4s.items()
                            if k != "per_history"},
             "a4_covering_fidelity": {k: v for k, v in fid_scan.items()
                                      if k != "per_history"},
             "linear_share": {"comparisons": lin_cmp,
                              "mismatches": lin_bad,
                              "singles": len(lin_idx)},
             "stamp": "REPRODUCTION: the parent proves the theorem by a "
                      "Boolean-algebra argument naming no arena and no "
                      "event size, so a faithful implementation cannot "
                      "disagree; the leg is a fidelity check on this "
                      "unit's constructor and it is published as one"})
    R["law1_naming"] = SEAL.seal(
        "law1_naming",
        {"comparisons": total_cmp, "mismatches": total_bad,
         "positive": total_pos, "negative": total_cmp - total_pos,
         "window_size": fid_scan["window_size"],
         "linear_share_comparisons": lin_cmp,
         "s16_not_filtered": math.factorial(A.n)}, "G-LAW1-NAMING16")

    # ---- LAW 2: FLOORS, SCHEDULES, THE SHARPENED FORM ----------------
    certrows = []
    for a in ARITIES:
        k, wit, reasons, nodes = certified_floor(a)
        certrows.append({"a": a, "certified_floor": k,
                         "witness_signatures": wit,
                         "refusals_below": reasons,
                         "witness_nodes": nodes,
                         "column_sums": ([sum(col[i] for col in wit)
                                          for i in range(len(wit[0]))]
                                         if wit else [])})
    cert_ok = all(
        c["certified_floor"] is not None
        and c["witness_signatures"] is not None
        and len({tuple(s) for s in c["witness_signatures"]}) == A.n
        and len(c["witness_signatures"][0]) == c["certified_floor"]
        and all(x == c["a"] for x in c["column_sums"])
        for c in certrows)
    CR.measured("cert_rows", len(certrows), "one certificate per arity")
    CR.measured("cert_refusals",
                sum(len(c["refusals_below"]) for c in certrows), "counted")
    LD.gate("G-LAW2-FLOOR-CERTIFICATE16", cert_ok,
            CR.stmt("the information floor is decided at every arity by "
                    "certificate over the COMPLETE event universe: the "
                    "least k admitting {n} distinct k-bit signatures whose "
                    "every column sums to the event size, with an "
                    "exhibited witness at the value returned and {r} named "
                    "refusals below the four values",
                    n="n_actors", r="cert_refusals"),
            {"rows": [{"a": c["a"], "certified_floor": c["certified_floor"],
                       "column_sums": c["column_sums"],
                       "refusals_below": c["refusals_below"]}
                      for c in certrows]})

    sched2 = schedule_sweep_a2()
    sched4 = schedule_window_a4()
    flo = {c["a"]: c["certified_floor"] for c in certrows}
    sched = {2: sched2["min_events"], 4: sched4["min_events"]}
    off = {a: sched[a] - flo[a] for a in sched}
    CR.measured("a2_pool", sched2["pool"],
                "the complete budget-saturating pool at the smallest arity")
    CR.measured("a2_pairs", sched2["ordered_pairs"],
                "ordered round pairs swept, repetition included")
    CR.measured("a2_schedule", sched2["min_events"],
                "the complete minimum at the smallest arity, in events")
    CR.measured("a4_schedule", sched4["min_events"],
                "the window minimum at the committed arity, in events")
    CR.measured("a4_window_histories", sched4["window_histories"],
                "the committed window's histories")
    pool2w = saturating_matchings()
    wit_ok = (sched2["witness_pair"] is not None
              and time_to_discrete(
                  [pool2w[sched2["witness_pair"][0]],
                   pool2w[sched2["witness_pair"][1]]])
              == sched2["min_events"])
    LD.gate("G-LAW2-SCHEDULE16",
            sched2["min_events"] is not None
            and sched2["min_events"] >= flo[2]
            and wit_ok
            and not sched2["round_one_discrete_possible"]
            and sched2["ordered_pairs"] == sched2["pool"] ** 2
            and sched4["min_events"] == 2 * A.q - 1
            and sched4["min_events"] >= flo[4]
            and sched4["window_histories"] == PV["P-N16-COV"],
            CR.stmt("the schedule time is measured on two grounds and each "
                    "names its own completeness: at the smallest arity the "
                    "budget-saturating pool is COMPLETE at {p} matchings, "
                    "no round-one history is discrete, and every ordered "
                    "pair of pool rounds -- {pr}, repetition included -- "
                    "is swept, so the minimum {s2} is the minimum over "
                    "EVERY history the pool admits with no cap; at the "
                    "committed arity the value {s4} is a WINDOW value on "
                    "NDEP's own {wh} covering tuples, with the certified "
                    "floor beneath it and the full pool's sweep out of "
                    "declared scope",
                    p="a2_pool", pr="a2_pairs", s2="a2_schedule",
                    s4="a4_schedule", wh="a4_window_histories"),
            {"a2": sched2, "a4": sched4,
             "offsets": {str(k): v for k, v in sorted(off.items())}})

    nq = AN.read("V-N16WINDOW", "G-LAW2-SHARPENED16")
    n16_ints = quote_ints(nq)
    sharp = {a: weight_floor(A.n, (A.q if mut("MUT-FLOOR") else a))
             for a in ARITIES}
    sharp_hits = sorted(a for a in ARITIES if sharp[a] == flo[a])
    closed_in_a = {a: 2 * (a - 1) for a in ARITIES}
    closed_hits = sorted(a for a in ARITIES if closed_in_a[a] == flo[a])
    CR.measured("sharp_hits", len(sharp_hits),
                "arities where the sharpened floor equals the certified "
                "floor")
    CR.measured("closed_hits", len(closed_hits),
                "arities where the parent's closed form, read in the event "
                "size, equals it")
    CR.measured("counting_bound16", counting_floor(A.n),
                "the parent's counting bound at this arena")
    LD.gate("G-LAW2-SHARPENED16",
            sharp_hits == list(ARITIES)
            and n16_ints[:3] == [counting_floor(A.n), flo[COMMITTED_ARITY],
                                 PV["P-N16-COV"]]
            and closed_hits == [A.q]
            and counting_floor(A.n) != flo[COMMITTED_ARITY],
            CR.stmt("NDEP's sharpened floor, read with the EVENT SIZE in "
                    "the place its quotation names, reproduces the "
                    "certified floor at {sh} of {k} arities AT THE SECOND "
                    "ARENA -- the parent's own vindication transported -- "
                    "while its closed form in that variable agrees at {ch} "
                    "arity only, its own diagonal a = q, exactly as at the "
                    "parent arena. The quotation's counting bound, floor "
                    "and tuple count are parsed and matched against this "
                    "unit's re-derivations",
                    sh="sharp_hits", k="n_arities", ch="closed_hits"),
            {"certified_floors": {str(a): flo[a] for a in ARITIES},
             "sharpened_floors": {str(a): sharp[a] for a in ARITIES},
             "closed_form_in_a": {str(a): closed_in_a[a] for a in ARITIES},
             "sharpened_agrees_at": sharp_hits,
             "closed_form_agrees_at": closed_hits,
             "quotation_parsed": n16_ints[:3]})
    R["law2_crystallization"] = SEAL.seal(
        "law2_crystallization",
        {"floors": {str(a): flo[a] for a in ARITIES},
         "schedule": {"a2": sched2, "a4": sched4},
         "offsets": {str(k): v for k, v in sorted(off.items())},
         "sharpened_floors": {str(a): sharp[a] for a in ARITIES},
         "closed_form_in_a": {str(a): closed_in_a[a] for a in ARITIES},
         "counting_bound": counting_floor(A.n),
         "schedule_scope": "a = 2 COMPLETE over the saturating pool; "
                           "a = 4 a WINDOW value on the committed covering "
                           "tuples; the idle arities REFUSED"},
        "G-LAW2-SHARPENED16")
    R["law2_certificates"] = SEAL.seal(
        "law2_certificates",
        {"floor": [{"a": c["a"], "certified_floor": c["certified_floor"],
                    "witness_signatures": c["witness_signatures"],
                    "column_sums": c["column_sums"],
                    "refusals_below": c["refusals_below"]}
                   for c in certrows]},
        "G-LAW2-FLOOR-CERTIFICATE16")

    # ---- LAW 3: THE MENU AT THE FAILED HYPOTHESIS --------------------
    uq = AN.read("V-UNSCORED", "G-LAW3-MENU16")
    surv = survivors()
    leg1_all = all(leg1_geometry(p) for p in surv)
    cos_abs = sorted({A.coset_partition(H) for H in SUBS})
    cos_lin = sorted({A.coset_partition(H) for H in F4SUBS})
    abs_in = sum(1 for c in cos_abs if c in set(surv))
    lin_in = sum(1 for c in cos_lin if c in set(surv))
    nonuniform = sum(1 for P in surv if len({len(b) for b in P}) > 1)
    CR.measured("menu_survivors", len(surv),
                "invariant partitions, by complete closure enumeration")
    CR.measured("menu_cosets_abstract", len(cos_abs),
                "abstract coset partitions")
    CR.measured("menu_cosets_linear", len(cos_lin),
                "linear coset partitions")
    CR.measured("menu_nonuniform", nonuniform,
                "survivors with mixed block sizes")
    LD.gate("G-LAW3-MENU16",
            leg1_all and abs_in == len(cos_abs) and lin_in == len(cos_lin)
            and len(surv) > len(cos_abs) > len(cos_lin)
            and "unscored" in uq,
            CR.stmt("the geometry leg's survivor set is enumerated "
                    "COMPLETELY by closure from the discrete partition -- "
                    "Bell(n) at sixteen is out of every window, the "
                    "survivor lattice is not -- and it has {s} members, "
                    "every one re-verified against the parent's leg-1 "
                    "predicate. The parent's closed form fails at this "
                    "arena under BOTH readings: the {ca} abstract coset "
                    "partitions and the {cl} linear ones are all "
                    "survivors, and neither reading's set is the survivor "
                    "set; {nu} survivors have mixed block sizes, an object "
                    "no coset partition can be. NDEP's own precedent -- "
                    "the row carried unscored at the failed hypothesis -- "
                    "is quoted, and what NDEP could not reach is here "
                    "MEASURED",
                    s="menu_survivors", ca="menu_cosets_abstract",
                    cl="menu_cosets_linear", nu="menu_nonuniform"),
            {"survivors": len(surv), "leg1_verified_on_all": leg1_all,
             "abstract_cosets": len(cos_abs),
             "abstract_cosets_in_survivors": abs_in,
             "linear_cosets": len(cos_lin),
             "linear_cosets_in_survivors": lin_in,
             "nonuniform_survivors": nonuniform,
             "block_size_profiles": sorted(Counter(
                 tuple(sorted(Counter(len(b) for b in P).items()))
                 for P in surv).items(), key=repr)[:12],
             "stamp": "A-INERT-BY-CONSTRUCTION"})
    R["law3_menu"] = SEAL.seal(
        "law3_menu",
        {"survivors": len(surv), "abstract_cosets": len(cos_abs),
         "linear_cosets": len(cos_lin),
         "nonuniform_survivors": nonuniform,
         "value_at_every_arity": {str(a): len(surv) for a in ARITIES},
         "abstract_order_counts": sorted(Counter(
             len(H) for H in SUBS).items()),
         "stamp": "A-INERT-BY-CONSTRUCTION: the leg reads the partition "
                  "and the arena and never a history, so the value cannot "
                  "move with the arity; the comparison across readings is "
                  "the measurement, and both readings fail"},
        "G-LAW3-MENU16")

    # ---- LAW 4: THE LADDER AND THE MODULUS THEOREM -------------------
    ladrows = [ladder_row(a) for a in ARITIES]
    lad9 = ladder_row(9)
    lad8 = ladder_row(8)
    found_rows = [r for r in ladrows + [lad9] if r["achievable_budgets"]]
    CR.measured("ladder_rows", len(ladrows + [lad9, lad8]),
                "arity rows searched, the census legs included")
    CR.measured("ladder_found", len(found_rows), "rows with a found rung")
    CR.measured("ladder_capped",
                sum(1 for r in ladrows
                    if r["witness_status"] == "NOT-FOUND-WITHIN-CAP"),
                "rows whose witness search ended at a declared cap")
    CR.measured("rung_a9", (min(lad9["achievable_budgets"])
                            if lad9["achievable_budgets"] else 0),
                "the first rung at nine actors per event")
    LD.gate("G-LAW4-LADDER16",
            all(r["impossible_budgets_derived"] ==
                [x for x in range(1, LADDER_RMAX + 1) if x % A.L]
                for r in ladrows + [lad9, lad8] if r["feasible"])
            and all(sorted(r["achievable_budgets"]) ==
                    [x for x in range(1, LADDER_RMAX + 1) if x % A.L == 0]
                    for r in found_rows)
            and [r["a"] for r in found_rows] == [2, 4, 9]
            and lad8["witness_status"] == "REFUSED-COMPLETE"
            and PV["P-N16-LAD4"] is True and PV["P-N16-LAD8"] is True
            and PV["P-N16-LAD5"] is False,
            CR.stmt("the budget-reading ladder is measured directly at "
                    "every declared arity and at the census legs beside "
                    "them: the impossibility half is the measured mass's "
                    "own arithmetic -- a saturating round has mass {n} "
                    "over {c} cells, so a homogeneous record needs the "
                    "budget divisible by {L} -- and the achievability half "
                    "is witness exhibition, found at {f} rows including "
                    "two where the event size and the link count are "
                    "DIFFERENT numbers, refused by complete search at "
                    "eight actors per event, and published as capped at "
                    "{cp} rows the declared windows could not decide. "
                    "Every found set matches NDEP's anchored rungs",
                    n="n_actors", c="n_cells", L="n_links",
                    f="ladder_found", cp="ladder_capped"),
            {"rows": [{k: v for k, v in r.items()
                       if k != "witness_rounds"} for r in ladrows],
             "census_leg_a9": {k: v for k, v in lad9.items()
                              if k != "witness_rounds"},
             "census_leg_a8": {k: v for k, v in lad8.items()
                              if k != "witness_rounds"},
             "witness_rounds_kept": sorted(
                 r["a"] for r in ladrows + [lad9]
                 if r.get("witness_rounds"))})
    R["law4_ladder"] = SEAL.seal(
        "law4_ladder",
        {"rows": ladrows, "census_leg_a9": lad9, "census_leg_a8": lad8,
         "reading": "LITERAL-BUDGET: the parent's primary reading; the "
                    "round mass is the budget by definition"},
        "G-LAW4-LADDER16")

    mq = AN.read("V-MODULUS", "G-MODULUS-THEOREM")
    m_pairs = quote_ints(mq)
    sweep = []
    for nn in range(1, THEOREM_N_MAX + 1):
        for ll in range(1, THEOREM_L_MAX + 1):
            cells = nn * ll
            got = cells // math.gcd(cells, nn)
            sweep.append(got == ll)
    if mut("MUT-THEOREM"):
        sweep[0] = not sweep[0]
    arena_modulus = NC // math.gcd(NC, A.n)
    mod_a_rows = [r for r in found_rows
                  if min(r["achievable_budgets"]) == r["a"]]
    diff_rows = [r for r in found_rows if r["a"] != A.L]
    CR.measured("theorem_pairs", len(sweep),
                "declared (n, L) pairs at which the identity is checked")
    CR.measured("theorem_pairs_ok", sum(1 for x in sweep if x), "counted")
    CR.measured("arena_modulus", arena_modulus,
                "the theorem's instance at this arena")
    CR.measured("mod_a_rows", len(mod_a_rows),
                "found rows whose first rung is the event size")
    CR.measured("diff_rows", len(diff_rows),
                "found rows where the event size and the link count differ")
    LD.gate("G-MODULUS-THEOREM",
            all(sweep) and len(sweep) == m_pairs[-1]
            and arena_modulus == A.L
            and all(min(r["achievable_budgets"]) == A.L
                    for r in found_rows)
            and all(r["a"] == A.L for r in mod_a_rows)
            and len(diff_rows) > 0,
            CR.stmt("the parent's modulus theorem is TESTED at the second "
                    "arena rather than re-derived: the identity is "
                    "re-verified at the parent's own {p} declared arena "
                    "pairs -- the quotation's count parsed and matched -- "
                    "its instance here reads {am}, every found rung is the "
                    "declared link count, and mod-a appears at {ma} of the "
                    "{df} found rows where the event size and the link "
                    "count are different numbers: the first rung is the "
                    "event size ONLY where the event size IS the link "
                    "count, which is the mod-a-iff-a-equals-L half "
                    "instanced at rows the parent arena could not supply",
                    p="theorem_pairs", am="arena_modulus",
                    ma="mod_a_rows", df="diff_rows"),
            {"pairs_checked": len(sweep), "pairs_holding": sum(sweep),
             "quotation_pair_count": m_pairs[-1],
             "arena_instance": {"n": A.n, "L": A.L, "cells": NC,
                                "modulus": arena_modulus},
             "found_rungs": [[r["a"], min(r["achievable_budgets"])]
                             for r in found_rows],
             "mod_a_appears_at": [r["a"] for r in mod_a_rows],
             "differing_rows": [r["a"] for r in diff_rows]})
    R["modulus_theorem"] = SEAL.seal(
        "modulus_theorem",
        {"pairs_checked": len(sweep), "pairs_holding": sum(sweep),
         "arena_modulus": arena_modulus,
         "found_rungs": [[r["a"], min(r["achievable_budgets"])]
                         for r in found_rows],
         "mod_a_appears_at": [r["a"] for r in mod_a_rows],
         "verdict": "A16-MODULUS-THEOREM-HOLDS"}, "G-MODULUS-THEOREM")

    # ---- LAW 5: THE FORCING CENSUS -----------------------------------
    frc = forcing_census()
    f2, f4 = frc[2], frc[4]
    CR.measured("forcing_abs_nonunique_a4",
                f4["ABSTRACT"]["non_unique"],
                "non-unique abstract coset rounds at the committed arity")
    CR.measured("forcing_abs_rounds_a4", f4["ABSTRACT"]["rounds"],
                "abstract coset rounds at the committed arity")
    CR.measured("forcing_lin_nonunique_a4",
                f4["F4-LINEAR"]["non_unique"],
                "non-unique linear rounds at the committed arity")
    CR.measured("forcing_lin_rounds_a4", f4["F4-LINEAR"]["rounds"],
                "linear rounds at the committed arity")
    CR.measured("forcing_abs_classes_a4",
                f4["ABSTRACT"]["non_unique_that_are_parallel_classes"],
                "of the abstract non-unique rounds, those that are "
                "parallel classes")
    LD.gate("G-LAW5-FORCING16",
            f4["F4-LINEAR"]["thesis_holds_per_object"]
            and not f4["ABSTRACT"]["thesis_holds_per_object"]
            and not f2["ABSTRACT"]["thesis_holds_per_object"]
            and f4["ABSTRACT"]["non_unique"] == f4["ABSTRACT"]["rounds"]
            and f4["F4-LINEAR"]["non_unique"] == f4["F4-LINEAR"]["rounds"]
            and f2["ABSTRACT"]["m_blind_across_the_fork"]
            and f4["ABSTRACT"]["m_blind_across_the_fork"]
            and f4["covering_tuples"]["non_unique"] == 0
            and f2["covering_tuples"]["non_unique"] == 0
            and frc[3].get("refusal") is not None
            and frc[5].get("refusal") is not None,
            CR.stmt("the division-forcing thesis is tested per object over "
                    "the complete survivor set at every window history, "
                    "and IT SPLITS ON THE READING: under the linear window "
                    "every one of the {lr} rounds is non-unique and every "
                    "one is a parallel class, so the parent's thesis holds "
                    "verbatim; under the abstract window all {ar} rounds "
                    "are non-unique while only {ac} are parallel classes, "
                    "so the thesis is false as stated -- the non-linear "
                    "coset rounds are the new joiners, objects a prime "
                    "arena cannot have. The census is blind across the "
                    "declared modulus fork, every covering tuple is "
                    "unique, and the idle arities refuse",
                    lr="forcing_lin_rounds_a4", ar="forcing_abs_rounds_a4",
                    ac="forcing_abs_classes_a4"),
            {"rows": frc, "measure": "COUNTING-ONLY"})
    R["law5_forcing"] = SEAL.seal(
        "law5_forcing", {"rows": frc, "measure": "COUNTING-ONLY (E-24)"},
        "G-LAW5-FORCING16")

    # ---- LAW 6: THE UNION CENSUS -------------------------------------
    obq = AN.read("V-OBSTRUCTION", "G-LAW6-SEC2-16")
    ob_vals = quote_ints(obq)
    sec = sec2_census()
    srows = {r["a"]: r for r in sec["rows"]}
    parent_forced = {2: PV["P-SEC2-F2"], 3: PV["P-SEC2-F3"],
                     4: PV["P-SEC2-F4"], 5: PV["P-SEC2-F5"]}
    CR.measured("union_carriers", sec["union_carriers"], "counted")
    CR.measured("union_pairs", sec["union_realised_pairs"], "counted")
    CR.measured("sec2_a2_free", srows[2]["obstruction_free"],
                "seam-spanning pair events opening nothing and doubling "
                "nothing")
    CR.measured("sec2_a2_span", srows[2]["seam_spanning"],
                "seam-spanning pair events")
    CR.measured("link_edges", sec["sector_link_pairs"],
                "edges of the declared-link graph")
    CR.measured("off_span_pairs", sec["off_undeclared_span_pairs"],
                "pairs whose difference avoids the undeclared span")
    LD.gate("G-LAW6-SEC2-16",
            not sec["identity_violations"]
            and ob_vals == [srows[a]["measured_min_within_sector_pairs"]
                            for a in ARITIES]
            and ob_vals == [srows[a]["forced_inside_bound"]
                            for a in ARITIES]
            and ob_vals == [parent_forced[a] for a in ARITIES]
            and srows[2]["obstruction_free"] == srows[2]["seam_spanning"]
            and all(srows[a]["obstruction_free"] == 0
                    for a in ARITIES if a != 2)
            and sec["union_doubled_pairs"] == 0
            and sec["seam_pairs_that_are_declared_links"] == 0
            and not sec["tripartite_characterisation_holds"],
            CR.stmt("the union of two sectors of THIS arena is built from "
                    "the arrangement alone -- {uc} carriers, {up} realised "
                    "pairs, the seam a line of the undeclared class "
                    "carrying no declared link, nothing doubled -- and the "
                    "parent's obstruction form is VERIFIED at the realised "
                    "census, not re-derived: the quotation's four values "
                    "are parsed and each equals both the closed form and "
                    "the MEASURED minimum of within-sector pairs over the "
                    "seam-spanning groups of that arity. At two actors "
                    "every one of the {sp} seam-spanning events opens "
                    "nothing and doubles nothing, the parent's vanishing "
                    "reproduced; and the parent arena's tripartite "
                    "characterisation of the link graph FAILS here -- {le} "
                    "link edges against {os} off-span pairs -- a "
                    "coincidence of the prime field, measured as one",
                    uc="union_carriers", up="union_pairs",
                    sp="sec2_a2_span", le="link_edges",
                    os="off_span_pairs"),
            {"rows": sec["rows"], "quotation_values": ob_vals,
             "union": {k: v for k, v in sec.items() if k != "rows"}})
    R["law6_sec2"] = SEAL.seal(
        "law6_sec2", sec, "G-LAW6-SEC2-16")

    # ---- THE PRINCIPLE CENSUS AND THE CONDITIONAL --------------------
    pc = principle_census()
    prows = pc["rows"]
    PRINCIPLES = ("round_completeness", "saturation_at_the_budget",
                  "saturation_is_maximality",
                  "subgroup_order_available_linear",
                  "subgroup_order_available_abstract")
    padmits = {}
    for p in PRINCIPLES:
        padmits[p] = [r["a"] for r in prows if r[p] is True]
    padmits["cover_at_R_equals_L"] = [
        r["a"] for r in prows if r["cover_at_R_equals_L"] == "YES-WITNESS"]
    cover_capped = [r["a"] for r in prows
                    if r["cover_at_R_equals_L"] == "NOT-WITHIN-CAP"]
    selectors = {}
    for p in list(PRINCIPLES) + ["cover_at_R_equals_L"]:
        nontrivial = [a for a in padmits[p] if 1 < a < A.n]
        selectors[p] = nontrivial[0] if len(nontrivial) == 1 else None
    CR.measured("n_principles", len(list(PRINCIPLES)
                                     + ["cover_at_R_equals_L"]),
                "candidate principles, the cover row included")
    CR.measured("n_candidates", len(prows), "candidate event sizes swept")
    CR.measured("satmax_selects",
                selectors["saturation_is_maximality"] or 0,
                "the size saturation-is-maximality uniquely admits")
    CR.measured("linear_selects",
                selectors["subgroup_order_available_linear"] or 0,
                "the size the linear subgroup row uniquely admits")
    LD.gate("G-PRINCIPLE-CENSUS16",
            len(prows) == A.n
            and padmits["round_completeness"] == [x for x in range(1, 17)
                                                  if A.n % x == 0]
            and padmits["subgroup_order_available_abstract"]
            == pc["abstract_orders"]
            and padmits["subgroup_order_available_linear"]
            == pc["linear_orders"]
            and selectors["subgroup_order_available_linear"] == A.q
            and selectors["subgroup_order_available_abstract"] is None
            and selectors["round_completeness"] is None
            and selectors["saturation_is_maximality"] == A.characteristic
            and cover_capped == [x for x in (3, 5, 6, 7)],
            CR.stmt("the parent's five-principle census is re-run at all "
                    "{c} candidate event sizes with the subgroup row split "
                    "into BOTH pre-registered readings: divisibility and "
                    "abstract-subgroup availability admit the same sizes "
                    "-- the registration's coincidence, measured -- and "
                    "neither selects; the LINEAR row admits {ls} alone "
                    "among nontrivial sizes and tracks the field; and "
                    "saturation-is-maximality, the principle that selected "
                    "the field order at the parent arena, here admits {ms} "
                    "alone -- THE CHARACTERISTIC, not the field order -- "
                    "so the parent's three selecting principles no longer "
                    "agree on what they select",
                    c="n_candidates", ls="linear_selects",
                    ms="satmax_selects"),
            {"rows": prows, "admits": padmits,
             "unique_nontrivial_selections": {k: v for k, v in
                                              sorted(selectors.items())},
             "cover_capped_at": cover_capped})
    R["principles"] = SEAL.seal(
        "principles",
        {"rows": prows, "admits": {k: v for k, v in sorted(padmits.items())},
         "unique_nontrivial_selections": {k: v for k, v in
                                          sorted(selectors.items())},
         "cover_capped_at": cover_capped,
         "stamp": "NONE of these was pre-registered anywhere in the "
                  "corpus; each is a commitment implicit in a constructor, "
                  "and the census measures what each WOULD select if it "
                  "were declared, under both readings of the word "
                  "subgroup"},
        "G-PRINCIPLE-CENSUS16")

    cq = AN.read("V-CONDITIONAL", "G-CONDITIONAL")
    lin_proper = [x for x in pc["linear_orders"] if 1 < x < A.n]
    abs_proper = [x for x in pc["abstract_orders"] if 1 < x < A.n]
    if mut("MUT-DISAGREE"):
        abs_proper = list(lin_proper)
    lin_conclusion = lin_proper[0] if len(lin_proper) == 1 else None
    CR.measured("lin_proper_sizes", len(lin_proper),
                "proper nontrivial linear coset sizes")
    CR.measured("abs_proper_sizes", len(abs_proper),
                "proper nontrivial abstract coset sizes")
    CR.measured("lin_conclusion", lin_conclusion or 0,
                "what the linear antecedent selects")
    LD.gate("G-CONDITIONAL",
            "complete partition" in cq and "field order" in cq
            and lin_proper == [A.q] and lin_conclusion == A.q
            and abs_proper != lin_proper
            and all(A.n % x == 0 for x in abs_proper),
            CR.stmt("the parent's conditional is evaluated at this arena "
                    "under BOTH readings of its coset clause, the "
                    "quotation's antecedent parsed for its two clauses: "
                    "under the F4-LINEAR reading the proper nontrivial "
                    "coset sizes number {lp} and the antecedent selects "
                    "{lc} = q, so the conditional TRACKS THE FIELD; under "
                    "the ABSTRACT reading they number {ap} and the "
                    "antecedent selects a SET, not a size. The two "
                    "readings disagree, the disagreement is the verdict, "
                    "and nothing here merges them",
                    lp="lin_proper_sizes", lc="lin_conclusion",
                    ap="abs_proper_sizes"),
            {"linear_proper_sizes": lin_proper,
             "abstract_proper_sizes": abs_proper,
             "linear_conclusion": lin_conclusion,
             "verdict": "A16-CONDITIONAL-READING-DEPENDENT",
             "f4_branch": "A16-CONDITIONAL-TRACKS-THE-FIELD",
             "completeness_clause": "every abstract proper size divides "
                                    "the actor count, so the completeness "
                                    "clause removes nothing the lattice "
                                    "left"})
    R["conditional"] = SEAL.seal(
        "conditional",
        {"linear_proper_sizes": lin_proper,
         "abstract_proper_sizes": abs_proper,
         "linear_conclusion": lin_conclusion,
         "verdict": "A16-CONDITIONAL-READING-DEPENDENT",
         "f4_branch": "A16-CONDITIONAL-TRACKS-THE-FIELD",
         "satmax_follows_the_characteristic":
             selectors["saturation_is_maximality"] == A.characteristic},
        "G-CONDITIONAL")

    # ================================================================
    # THE TRANSPORT TABLE AND THE TWO-LEVEL, TWO-READING AGGREGATE
    # ================================================================
    menu_n = len(surv)
    rung = {r["a"]: (min(r["achievable_budgets"])
                     if r["achievable_budgets"] else None)
            for r in ladrows}
    lin_windows = {a: len(corp[a]["singles_linear"]) for a in ARITIES}
    abs_windows = {a: len(corp[a]["singles_abstract"]) for a in ARITIES}

    def stmt_rows_for(reading):
        naming_ok = {2: scan_a2["mismatches"] == 0,
                     4: (scan_a4s["mismatches"] == 0
                         and fid_scan["mismatches"] == 0)}
        win = lin_windows if reading == "F4-LINEAR" else abs_windows
        rows = [
            ("naming", "the stabilizer of a history is the Young subgroup "
                       "of its participation-signature partition",
             [arow(a, win[a] > 0, naming_ok.get(a, False),
                   "window routes") for a in ARITIES]),
            ("crystallization", "a schedule time, an information floor "
                                "beneath it, and one structurally "
                                "redundant event between them",
             [arow(a, a in off, off.get(a) == 1,
                   "packing-pool ground; the committed arity a window "
                   "value") for a in ARITIES]),
            ("menu", "the geometry leg admits exactly the coset partitions "
                     "of the translation subgroups",
             [arow(a, True,
                   menu_n == (len(cos_lin) if reading == "F4-LINEAR"
                              else len(cos_abs)),
                   "set comparison, a-inert") for a in ARITIES]),
            ("ladder", "the achievable homogeneous budgets are exactly the "
                       "multiples of the declared link count",
             [arow(a, rung[a] is not None,
                   rung[a] is not None and sorted(
                       [r for r in ladrows if r["a"] == a][0]
                       ["achievable_budgets"]) ==
                   [x for x in range(1, LADDER_RMAX + 1) if x % A.L == 0],
                   "within the declared bound") for a in ARITIES]),
            ("division-forcing", "more than one factorization exactly "
                                 "where the history repeats a parallel "
                                 "class",
             [arow(a, win[a] > 0,
                   frc[a].get(reading, {}).get("thesis_holds_per_object",
                                               False),
                   "per object on the reading's window")
              for a in ARITIES]),
            ("sec2-counting", "a seam-spanning group that opens no pair "
                              "inside a sector must double a link the "
                              "union already carries",
             [arow(a, True, srows[a]["obstruction_free"] == 0,
                   "per object") for a in ARITIES]),
        ]
        return rows

    def num_rows_for(reading):
        win = lin_windows if reading == "F4-LINEAR" else abs_windows
        return [
            ("menu", "the admissible-partition count", PV["P-PV-MENU"],
             [arow(a, True, menu_n, "a-inert") for a in ARITIES]),
            ("ladder", "the first rung", PV["P-PV-RUNG"],
             [arow(a, rung[a] is not None, rung[a], "found rungs only")
              for a in ARITIES]),
            ("crystallization", "the schedule time in events",
             PV["P-PV-SCHED"],
             [arow(a, a in sched, sched.get(a),
                   "complete at the smallest arity; window at the "
                   "committed one") for a in ARITIES]),
            ("crystallization", "the attained information floor",
             PV["P-PV-FLOOR"],
             [arow(a, True, flo[a], "certified, complete universe")
              for a in ARITIES]),
            ("crystallization", "the offset between them", PV["P-PV-OFF"],
             [arow(a, a in off, off.get(a), "by subtraction")
              for a in ARITIES]),
            ("naming", "the non-unique single rounds", PV["P-PV-NONU"],
             [arow(a, win[a] > 0,
                   frc[a].get(reading, {}).get("non_unique"),
                   "the reading's own window") for a in ARITIES]),
            ("sec2-counting", "the pairs forced inside a sector",
             PV["P-PV-FORCED"],
             [arow(a, True,
                   srows[a]["measured_min_within_sector_pairs"],
                   "measured minimum at the realised census")
              for a in ARITIES]),
        ]

    transport = {}
    for reading in READINGS:
        stmt_table = []
        for (nm, text, rows) in stmt_rows_for(reading):
            w, ev = statement_word(rows)
            stmt_table.append({"law": nm, "statement": text, "word": w,
                               "reading": reading,
                               "scope": EXTENSION_SCOPE, "evidence": ev})
        num_table = []
        for (nm, what, parent, rows) in num_rows_for(reading):
            w, ev = transport_word(parent, rows)
            alt = {}
            for label, rule in ALT_RULES:
                aw, _ = transport_word(parent, rows, rule)
                alt[label] = aw
            num_table.append({"law": nm, "numeral": what,
                              "parent_value": parent, "word": w,
                              "reading": reading,
                              "scope": EXTENSION_SCOPE, "evidence": ev,
                              "under_alternative_rules": alt})
        rule_aggregates = {}
        for label, rule in (("the declared rule", None),) + ALT_RULES:
            cnt = Counter()
            for (nm, what, parent, rows) in num_rows_for(reading):
                aw, _e = transport_word(parent, rows, rule)
                cnt[aw] += 1
            rule_aggregates[label] = {w: cnt.get(w, 0) for w in WORDS}
        transport[reading] = {
            "statements": stmt_table, "numerals": num_table,
            "statement_words": dict(Counter(r["word"]
                                            for r in stmt_table)),
            "numeral_words": dict(Counter(r["word"] for r in num_table)),
            "aggregate_under_each_rule": rule_aggregates}

    lin_t, abs_t = transport["F4-LINEAR"], transport["ABSTRACT"]
    split_stmts = sorted(
        rl["law"] for rl, ra in zip(lin_t["statements"],
                                    abs_t["statements"])
        if rl["word"] != ra["word"])
    split_nums = sorted(
        rl["law"] + ": " + rl["numeral"]
        for rl, ra in zip(lin_t["numerals"], abs_t["numerals"])
        if rl["word"] != ra["word"]
        or rl["evidence"].get("measured") != ra["evidence"].get("measured"))

    controls = []
    base = math.comb(PARENT_ARITY, 2)
    for label, mk in (
            ("LAW-IN-A", lambda a: t_a_reading(base, a)),
            ("NEEDS-3", lambda a: base),
            ("BREAKS", lambda a: base + a)):
        w, ev = transport_word(base, [arow(a, True, mk(a), "synthetic")
                                      for a in ARITIES])
        controls.append({"forced": label, "emitted": w,
                         "stamp": ev.get("stamp")})
    w, ev = transport_word(base, [arow(a, False, base, "synthetic")
                                  for a in ARITIES])
    controls.append({"forced": "BREAKS", "emitted": w,
                     "stamp": ev.get("reason")})
    for label, val in (("LAW-IN-A", True), ("BREAKS", False)):
        w, _e = statement_word([arow(a, True, val, "synthetic")
                                for a in ARITIES])
        controls.append({"forced": label, "emitted": w, "stamp": "STATEMENT"})
    CR.measured("n_controls_arms", len(controls), "counted")
    CR.measured("controls_agreeing",
                sum(1 for c in controls if c["forced"] == c["emitted"]),
                "counted")
    LD.gate("G-TRANSPORT-CONTROLS",
            all(c["forced"] == c["emitted"] for c in controls)
            and len({c["stamp"] for c in controls}) > 1,
            CR.stmt("{k} synthetic laws are pushed through the REAL "
                    "decision procedure -- one built to force each word, "
                    "one whose rows are all infeasible so the procedure "
                    "must refuse rather than default, and two at the "
                    "statement slot -- and {a} of them come out as forced; "
                    "the procedure is a pure function of its rows, so the "
                    "words the real laws receive are emitted by this same "
                    "code and nothing else",
                    k="n_controls_arms", a="controls_agreeing"),
            {"controls": controls})
    R["transport_controls"] = SEAL.seal("transport_controls", controls,
                                        "G-TRANSPORT-CONTROLS")

    tw = AN.read("V-TWOLEVEL", "G-AGGREGATE16")
    slot = re.search(r"A law's (\w+) is LAW-IN-A", tw)
    slotname = _probe_agg() if mut("MUT-AGG") else (
        slot.group(1) if slot else None)
    parent_words = [PV["P-PW-%d" % i] for i in range(7)]
    both_words = [
        {"law": rl["law"], "numeral": rl["numeral"],
         "parent_word_at_nine": pw, "linear_word_here": rl["word"],
         "abstract_word_here": ra["word"]}
        for pw, rl, ra in zip(parent_words, lin_t["numerals"],
                              abs_t["numerals"])]
    moved_across_n = sorted(r["law"] + ": " + r["numeral"]
                            for r in both_words
                            if r["parent_word_at_nine"]
                            != r["linear_word_here"])
    CR.measured("n_statements", len(lin_t["statements"]),
                "scored statement rows per reading")
    CR.measured("n_numerals", len(lin_t["numerals"]),
                "scored numeral rows per reading")
    CR.measured("n_split_statements", len(split_stmts),
                "statement rows whose word moves with the reading")
    CR.measured("n_split_numerals", len(split_nums),
                "numeral rows that move with the reading")
    CR.measured("lin_stmt_lawin",
                lin_t["statement_words"].get("LAW-IN-A", 0), "counted")
    CR.measured("lin_stmt_breaks",
                lin_t["statement_words"].get("BREAKS", 0), "counted")
    CR.measured("abs_stmt_lawin",
                abs_t["statement_words"].get("LAW-IN-A", 0), "counted")
    CR.measured("abs_stmt_breaks",
                abs_t["statement_words"].get("BREAKS", 0), "counted")
    CR.measured("parent_stmt_lawin", PV["P-AGG-SL"],
                "the parent's own statement tally, anchored")
    CR.measured("num_breaks_lin",
                lin_t["numeral_words"].get("BREAKS", 0), "counted")
    CR.measured("num_needs_lin",
                lin_t["numeral_words"].get("NEEDS-3", 0), "counted")
    CR.measured("num_lawin_lin",
                lin_t["numeral_words"].get("LAW-IN-A", 0), "counted")
    CR.measured("parent_num_needs", PV["P-AGG-NN"],
                "the parent's own NEEDS-3 tally, anchored")
    CR.measured("moved_across_n", len(moved_across_n),
                "numeral rows whose word moved between the arenas")
    LD.gate("G-AGGREGATE16",
            slotname == "STATEMENT"
            and sum(lin_t["statement_words"].values())
            == len(lin_t["statements"])
            and sum(lin_t["numeral_words"].values())
            == len(lin_t["numerals"])
            and all(sum(v.values()) == len(lin_t["numerals"])
                    for v in lin_t["aggregate_under_each_rule"].values())
            and lin_t["numeral_words"].get("NEEDS-3", 0) == 0
            and abs_t["numeral_words"].get("NEEDS-3", 0) == 0
            and moved_across_n == sorted(
                r["law"] + ": " + r["numeral"] for r in both_words
                if r["parent_word_at_nine"] == "NEEDS-3")
            and ("division-forcing" in split_stmts)
            and len(split_nums) > 0,
            CR.stmt("the aggregate is TWO-LEVELLED in the slot name parsed "
                    "from the parent's own engraving, and at this arena it "
                    "is READING-RELATIVE besides: {s} statements and {n} "
                    "numerals are scored under EACH pre-registered "
                    "reading, {ss} statement words and {sn} numeral rows "
                    "move with the reading, and the primary linear "
                    "statement tally reads {lsl} transporting against "
                    "{lsb} breaking where the abstract tally reads {asl} "
                    "against {asb} and the parent's own anchored tally "
                    "read {psl}. At the numeral level NO row returns "
                    "NEEDS-3 under either reading -- every one of the "
                    "parent's {pnn} standing-still numerals moves once n "
                    "moves -- and {ma} of {n} rows change their word "
                    "between the arenas",
                    s="n_statements", n="n_numerals",
                    ss="n_split_statements", sn="n_split_numerals",
                    lsl="lin_stmt_lawin", lsb="lin_stmt_breaks",
                    asl="abs_stmt_lawin", asb="abs_stmt_breaks",
                    psl="parent_stmt_lawin", pnn="parent_num_needs",
                    ma="moved_across_n"),
            {"slot_parsed_from_the_quotation": slotname,
             "linear": {"statement_words": lin_t["statement_words"],
                        "numeral_words": lin_t["numeral_words"]},
             "abstract": {"statement_words": abs_t["statement_words"],
                          "numeral_words": abs_t["numeral_words"]},
             "split_statements": split_stmts,
             "split_numerals": split_nums,
             "both_arena_words": both_words,
             "moved_across_n": moved_across_n,
             "aggregate_under_each_rule_linear":
                 lin_t["aggregate_under_each_rule"],
             "aggregate_under_each_rule_abstract":
                 abs_t["aggregate_under_each_rule"]})
    R["transport"] = SEAL.seal(
        "transport",
        {"linear": lin_t, "abstract": abs_t,
         "primary_reading": PRIMARY_READING,
         "split_statements": split_stmts, "split_numerals": split_nums,
         "both_arena_words": both_words,
         "moved_across_n": moved_across_n,
         "scope_qualifier": EXTENSION_SCOPE,
         "extension_arities": extension_arities(),
         "off_committed_arities": off_committed_arities(),
         "the_a_only_rule": "C(a,2) + v - C(3,2), the parent's own, "
                            "declared once and applied to every numeral",
         "rule_relativity": "the declared aggregate is a statement about "
                            "the declared rule AND the declared reading; "
                            "every rule's aggregate is published under "
                            "both readings"},
        "G-AGGREGATE16")

    R["parent_words"] = SEAL.seal(
        "parent_words",
        {"stmt_lawin": PV["P-AGG-SL"], "stmt_breaks": PV["P-AGG-SB"],
         "num_needs": PV["P-AGG-NN"], "num_breaks": PV["P-AGG-NB"],
         "cf_lawin": PV["P-AGG-CF"],
         "per_numeral": [PV["P-PW-%d" % i] for i in range(7)]},
        "G-AGGREGATE16")

    R["schema"] = SEAL.seal("schema", SCHEMA, "G-ARENA16", measured=False)
    return src, paper_rel, write
# ===========================================================================
# SECTION 5.  THE VERDICT, THE COMPARATOR, AND THE PAPER GATES
# ===========================================================================

def render_field(v):
    if isinstance(v, (list, tuple)):
        return "|".join(str(x) for x in v)
    return str(v)


def build_segment(chunks):
    """the head is a POSITIONAL FIELD LIST, not a string (S-1)."""
    text, fields = [], []
    for c in chunks:
        if isinstance(c, tuple):
            k, v = c
            fields.append((k, v))
            text.append(render_field(v))
        else:
            text.append(c)
    return "".join(text), fields


def verdict_segments(rec, with_fields=False):
    ar = rec["arena"]
    rd = rec["readings"]
    cd = rec["conditional"]
    pr = rec["principles"]
    mt = rec["modulus_theorem"]
    lad = rec["law4_ladder"]
    tr = rec["transport"]
    sub = {r["a"]: r for r in rec["substrate"]["rows"]}
    bn = rec["substrate"]["both_arena_rows"]
    nm = rec["law1_naming"]
    cry = rec["law2_crystallization"]
    menu = rec["law3_menu"]
    frc = rec["law5_forcing"]["rows"]
    sec = rec["law6_sec2"]
    srows = {r["a"]: r for r in sec["rows"]}
    fid = rec["fidelity"]
    A_ = ar["arities"]
    lin_t, abs_t = tr["linear"], tr["abstract"]
    lin_agg = lin_t["aggregate_under_each_rule"]["the declared rule"]
    cf_agg = lin_t["aggregate_under_each_rule"][ALT_RULES[-1][0]]
    found = mt["found_rungs"]

    out, allf = [], []
    for chunks in (
        ["A16-CONDITIONAL-READING-DEPENDENT<THE WORD SUBGROUP WAS "
         "PRE-REGISTERED IN TWO READINGS BEFORE ANY ROW RAN, AND THEY PART "
         "COMPANY: THE F4-LINEAR LATTICE HAS ",
         ("lin_subspaces", rd["linear_subspaces"]),
         " SUBSPACES WITH ORDERS ", ("linear_orders", rd["linear_orders"]),
         ", SO THE PROPER NONTRIVIAL COSET SIZE IS ",
         ("lin_proper", cd["linear_proper_sizes"]),
         " ALONE AND THE PARENT'S CONDITIONAL SELECTS a=",
         ("lin_conclusion", cd["linear_conclusion"]),
         "=q -- A16-CONDITIONAL-TRACKS-THE-FIELD ON THAT BRANCH; THE "
         "ABSTRACT LATTICE HAS ",
         ("abs_subgroups", rd["abstract_subgroups"]),
         " SUBGROUPS WITH ORDERS ",
         ("abstract_orders", rd["abstract_orders"]),
         " = THE DIVISORS OF ", ("arena_n", ar["n"]),
         " EXACTLY AS THE SHARPENED REGISTRATION SAYS, SO ITS ANTECEDENT "
         "ADMITS ", ("abs_proper", cd["abstract_proper_sizes"]),
         " AND SELECTS A SET, NOT A SIZE | THE CENSUS SPLITS FURTHER: "
         "SATURATION-IS-MAXIMALITY, WHICH SELECTED a=q AT THE PARENT "
         "ARENA, HERE ADMITS ",
         ("satmax_selects",
          pr["unique_nontrivial_selections"]["saturation_is_maximality"]),
         " ALONE -- THE CHARACTERISTIC, NOT THE FIELD ORDER -- SO THE "
         "PARENT'S SELECTING PRINCIPLES NO LONGER AGREE ON WHAT THEY "
         "SELECT | ",
         ("n_principles", len(pr["admits"])),
         " CANDIDATE PRINCIPLES ARE MEASURED AT ",
         ("n_candidates", len(pr["rows"])),
         " CANDIDATE EVENT SIZES UNDER BOTH READINGS, NONE OF THEM "
         "PRE-REGISTERED ANYWHERE IN THE CORPUS, AND NOTHING MEASURED "
         "HERE SELECTS AN EVENT SIZE WITHOUT THE ARENA AND A READING>"],

        ["A16-MODULUS-THEOREM-HOLDS<THE PARENT'S IDENTITY nL/gcd(nL,n)=L "
         "IS TESTED AT THE SECOND ARENA, NOT RE-DERIVED: ITS INSTANCE "
         "HERE READS ", ("arena_modulus", mt["arena_modulus"]),
         " AND THE IDENTITY IS RE-VERIFIED AT THE PARENT'S ",
         ("theorem_pairs", mt["pairs_checked"]),
         " DECLARED ARENA PAIRS, THE COUNT PARSED FROM ITS OWN SENTENCE | "
         "RUNGS WERE FOUND AT a=",
         ("found_arities", [f[0] for f in found]),
         " AND EVERY FOUND SET IS EXACTLY THE MULTIPLES OF L=",
         ("arena_L", ar["L"]), " WITHIN R<=",
         ("ladder_bound", ar["ladder_search_bound"]),
         "; MOD-a APPEARS AT ",
         ("mod_a_rows", len(mt["mod_a_appears_at"])),
         " OF THE ", ("found_rows", len(found)),
         " FOUND ROWS -- THE ONE WHERE THE EVENT SIZE IS THE LINK COUNT "
         "-- AND AT NONE OF THE ",
         ("diff_rows", len([f for f in found if f[0] != ar["L"]])),
         " ROWS WHERE THEY DIFFER, WHICH IS THE mod-a-IFF-a=L HALF "
         "INSTANCED AT ROWS THE PARENT ARENA COULD NOT SUPPLY | AT EIGHT "
         "ACTORS PER EVENT THE COMPLETE POOL OF ",
         ("a8_pool", lad["census_leg_a8"]["saturating"]),
         " SATURATING ROUNDS REFUSES EVERY COVER; CAPPED ROWS ARE "
         "PUBLISHED AS CAPPED AND NEVER AS EMPTY>"],

        ["A16-TRANSPORT-READING-RELATIVE<TWO LEVELS AND TWO READINGS, ALL "
         "DECLARED: ", ("n_statements", len(lin_t["statements"])),
         " STATEMENTS AND ", ("n_numerals", len(lin_t["numerals"])),
         " NUMERALS ARE SCORED UNDER EACH PRE-REGISTERED READING; THE "
         "PRIMARY F4-LINEAR STATEMENT TALLY READS ",
         ("lin_stmt_lawin", lin_t["statement_words"].get("LAW-IN-A", 0)),
         " LAW-IN-A AND ",
         ("lin_stmt_breaks", lin_t["statement_words"].get("BREAKS", 0)),
         " BREAKS WHILE THE ABSTRACT TALLY READS ",
         ("abs_stmt_lawin", abs_t["statement_words"].get("LAW-IN-A", 0)),
         " AND ",
         ("abs_stmt_breaks", abs_t["statement_words"].get("BREAKS", 0)),
         " AND THE PARENT'S OWN, ANCHORED, READ ",
         ("parent_stmt_lawin", rec["parent_words"]["stmt_lawin"]),
         " AND ", ("parent_stmt_breaks", rec["parent_words"]["stmt_breaks"]),
         ": THE DIVISION-FORCING STATEMENT IS THE ROW THAT MOVES WITH THE "
         "READING | AT THE NUMERAL LEVEL THE DECLARED a-ONLY RULE RETURNS ",
         ("num_lawin", lin_agg["LAW-IN-A"]), " LAW-IN-A, ",
         ("num_needs", lin_agg["NEEDS-3"]), " NEEDS-3 AND ",
         ("num_breaks", lin_agg["BREAKS"]),
         " BREAKS UNDER BOTH READINGS -- THE PARENT'S ",
         ("parent_num_needs", rec["parent_words"]["num_needs"]),
         " STANDING-STILL NUMERALS, ANCHORED, BOTH MOVE ONCE n MOVES, AND ",
         ("moved_across_n", len(tr["moved_across_n"])),
         " OF ", ("n_numerals", len(lin_t["numerals"])),
         " ROWS CHANGE THEIR WORD BETWEEN THE ARENAS | UNDER THE PARENT'S "
         "CLOSED-FORM RULE THE OBSTRUCTION ROW ALONE TRANSPORTS: ",
         ("cf_lawin", cf_agg["LAW-IN-A"]), " LAW-IN-A, ",
         ("cf_needs", cf_agg["NEEDS-3"]), " NEEDS-3 AND ",
         ("cf_breaks", cf_agg["BREAKS"]),
         " BREAKS, AT BOTH ARENAS | EVERY WORD IS SCORED ",
         ("scope_qualifier", tr["scope_qualifier"]),
         " AND CARRIES ITS READING>"],

        ["A16-SUBSTRATE-THE-BUDGET-RETURNS-AT-TWO<THE ",
         ("census_a4", sub[COMMITTED_ARITY]["groupings"]),
         " GROUPINGS NDEP DECLARED OUT OF SCOPE ARE CENSUSED ENTIRE BY AN "
         "EXACT DYNAMIC PROGRAMME OVER THE ACTOR-SUBSET LATTICE, EVERY "
         "TOTAL AGREEING WITH ITS CLOSED FORM: GROUPINGS ",
         ("substrate_groupings", [sub[a]["groupings"] for a in A_]),
         " AND IDLE ACTORS ",
         ("substrate_idle", [sub[a]["idle_actors"] for a in A_]),
         " AT a=", ("arities", A_), " | BUDGET-SATURATING ",
         ("substrate_sat", [sub[a]["saturating_budget"] for a in A_]),
         " AGAINST THE PARENT ARENA'S ANCHORED ",
         ("parent_sat", [r["n9_saturating_budget"] for r in bn]),
         ": THE CLASS THE PARENT MEASURED EMPTY AT TWO ACTORS IS "
         "NON-EMPTY HERE -- THE CHARACTERISTIC'S OWN REVERSAL -- AND "
         "EVERY GROUPING WEIGHT IS EVEN | THE MAXIMUM ROUND INCIDENCE IS ",
         ("substrate_maxw", [sub[a]["max_weight"] for a in A_]),
         " AGAINST A BUDGET OF ", ("arena_n", ar["n"]),
         ", NDEP'S ANCHORED WITNESS AMONG THEM | THE IDLE ARITIES ",
         ("idle_arities", ar["idle_arities"]),
         " ARE THE COMMITTED GRAMMAR'S REFUSALS UNDER BOTH READINGS, AND "
         "THE REFUSAL IS THE MEASUREMENT>"],

        ["A16-NAMING-LAW-IN-A<", ("naming_comparisons", nm["comparisons"]),
         " ROUTE COMPARISONS OVER EVERY PREFIX OF EVERY WINDOW HISTORY AT "
         "BOTH COSET ARITIES ON THE DECLARED ",
         ("perm_window", nm["window_size"]),
         "-PERMUTATION WINDOW, ", ("naming_mismatches", nm["mismatches"]),
         " MISMATCHES, ", ("naming_positive", nm["positive"]),
         " INSIDE THE STABILIZER AND ",
         ("naming_negative", nm["negative"]),
         " OUTSIDE IT, SO BOTH DIRECTIONS ARE LIVE; NDEP'S COMMITTED "
         "CENSUS -- ",
         ("fid_comparisons", fid["measured"]["route_comparisons"]),
         " COMPARISONS, ",
         ("fid_positive", fid["measured"]["route_positive"]),
         " POSITIVE, ",
         ("fid_vac", fid["measured"]["route_positive_empty_prefix"]),
         " AT THE EMPTY PREFIX -- IS REPRODUCED EXACTLY AS THE FIDELITY "
         "LEG | THE STATEMENT CARRIES NO NUMERAL AND THE LEG IS A "
         "REPRODUCTION | ITS NUMERAL SPLITS ON THE READING: THE "
         "NON-UNIQUE SINGLE ROUNDS ARE ",
         ("lin_nonunique", frc[4]["F4-LINEAR"]["non_unique"]),
         " OF ", ("lin_rounds", frc[4]["F4-LINEAR"]["rounds"]),
         " ON THE LINEAR WINDOW AND ",
         ("abs_nonunique", frc[4]["ABSTRACT"]["non_unique"]),
         " OF ", ("abs_rounds", frc[4]["ABSTRACT"]["rounds"]),
         " ON THE ABSTRACT ONE AT THE COMMITTED ARITY>"],

        ["A16-CRYSTALLIZATION-BREAKS-AND-THE-SHARPENED-FLOOR-TRANSPORTS<"
         "CERTIFIED FLOORS ",
         ("crystal_floors", [cry["floors"][str(a)] for a in A_]),
         " AT a=", ("arities", A_),
         ", EACH WITH AN EXHIBITED SIGNATURE WITNESS AND NAMED REFUSALS "
         "BELOW IT; NDEP'S SHARPENED FLOOR, READ WITH THE EVENT SIZE IN "
         "THE PLACE ITS QUOTATION NAMES, REPRODUCES ALL ",
         ("n_arities", len(A_)),
         " OF THEM AT THE SECOND ARENA, WHILE THE COUNTING BOUND READS ",
         ("counting_bound", cry["counting_bound"]),
         " AND ITS CLOSED FORM AGREES ONLY ON ITS OWN DIAGONAL a=q | THE "
         "SCHEDULE TIME IS ", ("a2_schedule", cry["schedule"]["a2"]
                               ["min_events"]),
         " EVENTS AT TWO ACTORS -- COMPLETE OVER THE ",
         ("a2_pool", cry["schedule"]["a2"]["pool"]),
         "-MATCHING SATURATING POOL, EVERY ORDERED PAIR OF ROUNDS SWEPT "
         "-- AND ", ("a4_schedule", cry["schedule"]["a4"]["min_events"]),
         " ON NDEP'S OWN ",
         ("a4_window", cry["schedule"]["a4"]["window_histories"]),
         "-TUPLE WINDOW AT THE COMMITTED ARITY | THE OFFSETS READ ",
         ("offsets", [cry["offsets"][k] for k in sorted(cry["offsets"])]),
         " AT a=", ("offset_arities", [int(k) for k in
                                       sorted(cry["offsets"])]),
         " AGAINST THE PARENT'S CONSTANT ONE: THE PAIR SURVIVES AS A "
         "STRUCTURE AND EVERY ONE OF ITS NUMBERS MOVES>"],

        ["A16-MENU-BREAKS-AT-THE-FAILED-HYPOTHESIS<THE SURVIVOR SET IS "
         "ENUMERATED COMPLETELY BY CLOSURE FROM THE DISCRETE PARTITION: ",
         ("menu_survivors", menu["survivors"]),
         " INVARIANT PARTITIONS, EVERY ONE RE-VERIFIED AGAINST THE "
         "PARENT'S LEG-1 PREDICATE; THE ",
         ("menu_cos_abs", menu["abstract_cosets"]),
         " ABSTRACT COSET PARTITIONS AND THE ",
         ("menu_cos_lin", menu["linear_cosets"]),
         " LINEAR ONES ARE ALL AMONG THEM AND NEITHER READING'S SET IS "
         "THE SURVIVOR SET, SO THE PARENT'S CLOSED FORM BREAKS UNDER "
         "BOTH READINGS -- AT THE HYPOTHESIS NDEP MEASURED FAILED, THE "
         "DECLARED LINKS SPANNING ",
         ("links_generate", ar["links_generate_order"]),
         " OF ", ("arena_n", ar["n"]), " | ",
         ("menu_nonuniform", menu["nonuniform_survivors"]),
         " SURVIVORS HAVE MIXED BLOCK SIZES, AN OBJECT NO COSET PARTITION "
         "CAN BE | THE VALUE IS A-INERT BY CONSTRUCTION AND ITS ROW IS A "
         "DISCLOSURE, NOT A TRANSPORT MEASUREMENT>"],

        ["A16-FORCING-READING-SPLIT<THE THESIS IS TESTED PER OBJECT OVER "
         "THE COMPLETE SURVIVOR SET AT EVERY WINDOW HISTORY AND IT SPLITS "
         "ON THE READING: ON THE LINEAR WINDOW ALL ",
         ("frc_lin_rounds", frc[4]["F4-LINEAR"]["rounds"]),
         " ROUNDS AT THE COMMITTED ARITY ARE NON-UNIQUE AND ALL ",
         ("frc_lin_classes",
          frc[4]["F4-LINEAR"]["non_unique_that_are_parallel_classes"]),
         " ARE PARALLEL CLASSES -- THE PARENT'S THESIS VERBATIM -- WHILE "
         "ON THE ABSTRACT WINDOW ALL ",
         ("frc_abs_rounds", frc[4]["ABSTRACT"]["rounds"]),
         " ARE NON-UNIQUE AND ONLY ",
         ("frc_abs_classes",
          frc[4]["ABSTRACT"]["non_unique_that_are_parallel_classes"]),
         " ARE PARALLEL CLASSES, SO THE THESIS AS STATED IS FALSE THERE: "
         "THE NON-LINEAR COSET ROUNDS ARE JOINERS A PRIME ARENA CANNOT "
         "HAVE | AT TWO ACTORS ",
         ("frc_a2_nonunique", frc[2]["ABSTRACT"]["non_unique"]),
         " OF ", ("frc_a2_rounds", frc[2]["ABSTRACT"]["rounds"]),
         " ABSTRACT ROUNDS ARE NON-UNIQUE AND NONE IS A PARALLEL CLASS | "
         "EVERY COVERING TUPLE AT BOTH ARITIES IS UNIQUE; THE CENSUS IS "
         "BLIND ACROSS THE DECLARED MODULUS FORK ",
         ("m_fork", ar["coin_modulus_fork"]),
         "; THE IDLE ARITIES REFUSE UNDER BOTH READINGS | COUNTING-ONLY>"],

        ["A16-SEC2-OBSTRUCTION-FORM-VERIFIED<THE UNION IS REBUILT AT THIS "
         "ARENA FROM THE ARRANGEMENT ALONE -- ",
         ("union_carriers", sec["union_carriers"]), " CARRIERS, ",
         ("union_pairs", sec["union_realised_pairs"]),
         " REALISED PAIRS, ",
         ("union_doubled", sec["union_doubled_pairs"]),
         " DOUBLED, THE SEAM A LINE OF THE UNDECLARED CLASS CARRYING ",
         ("seam_declared", sec["seam_pairs_that_are_declared_links"]),
         " DECLARED LINKS -- AND THE PARENT'S OBSTRUCTION FORM IS "
         "VERIFIED AT THE REALISED CENSUS: THE MEASURED MINIMUM OF "
         "WITHIN-SECTOR PAIRS READS ",
         ("sec2_min_inside",
          [srows[a]["measured_min_within_sector_pairs"] for a in A_]),
         " AT a=", ("arities", A_),
         ", EQUAL TO THE PARENT'S ANCHORED COLUMN AND TO ITS CLOSED FORM "
         "AT EVERY ARITY | SEAM-SPANNING ",
         ("sec2_span", [srows[a]["seam_spanning"] for a in A_]),
         ", OPENING NO PAIR INSIDE A SECTOR ",
         ("sec2_opens_none", [srows[a]["within_sector_free"] for a in A_]),
         ", AND OPENING NO PAIR AND DOUBLING NOTHING ",
         ("sec2_free", [srows[a]["obstruction_free"] for a in A_]),
         ": AT TWO ACTORS EVERY SPANNING EVENT IS EXACTLY ONE CROSS PAIR, "
         "THE PARENT'S VANISHING REPRODUCED AT THE SECOND ARENA | THE "
         "PRIME ARENA'S TRIPARTITE READING OF THE LINK GRAPH FAILS HERE: ",
         ("link_edges", sec["sector_link_pairs"]),
         " LINK EDGES AGAINST ",
         ("off_span", sec["off_undeclared_span_pairs"]),
         " OFF-SPAN PAIRS, A COINCIDENCE OF THE PRIME FIELD MEASURED AS "
         "ONE>"],

        ["SCOPE=ONE ARENA, HELD FIXED: n=", ("arena_n", ar["n"]),
         ", q=", ("arena_q", ar["q"]), ", L=", ("arena_L", ar["L"]), ", ",
         ("arena_cells", ar["cells"]), " CELLS, CHARACTERISTIC ",
         ("characteristic", ar["characteristic"]),
         " | THE SUBSTRATE CENSUS, THE SURVIVOR ENUMERATION, THE FLOOR "
         "CERTIFICATES, THE UNION CENSUS AND THE TWO-ACTOR SCHEDULE SWEEP "
         "ARE COMPLETE; THE NAMING AND FORCING WINDOWS ARE THE DECLARED "
         "COSET WINDOWS OF EACH READING; THE COMMITTED-ARITY SCHEDULE IS "
         "A WINDOW VALUE ON NDEP'S ",
         ("a4_window", cry["schedule"]["a4"]["window_histories"]),
         " COVERING TUPLES | THE LADDER IS SEARCHED TO R<=",
         ("ladder_bound", ar["ladder_search_bound"]),
         " WITH WITNESS WINDOWS OF ",
         ("sat_cap", ar["sat_sample_cap"]),
         " CANONICAL ROUNDS AND ",
         ("node_cap", ar["cover_node_cap"]),
         " SEARCH NODES, AND EVERY CAPPED ROW SAYS SO | THE IDLE ARITIES ",
         ("idle_arities", ar["idle_arities"]),
         " REFUSE UNDER BOTH READINGS AND THE REFUSAL IS THE MEASUREMENT "
         "| NO PARENT VALUE IS RECOMPUTED AS A FINDING: EVERY PARENT "
         "NUMBER ENTERS AS AN ANCHORED READ OF A COMMITTED RECEIPT | "
         "MEASURE=COUNTING-ONLY (E-24) | LANGUAGE=LAW-IN-A, NEEDS-3 AND "
         "BREAKS NAME THE TRANSPORT OF A PUBLISHED LAW ALONG THE "
         "EVENT-SIZE AXIS AT THIS ARENA, UNDER THE NAMED READING, AND "
         "NOTHING ELSE"],
    ):
        t, f = build_segment(chunks)
        out.append(t)
        allf.append(f)
    return (out, allf) if with_fields else out


# THE COMPARATOR'S OWN ARITHMETIC: every head field re-derived from the
# receipt's ROW LISTS by a route that avoids the builder's summary keys
# wherever a row list can supply the value.
def _lin(rec):
    return rec["transport"]["linear"]


def _abs(rec):
    return rec["transport"]["abstract"]


def _own_words(table):
    return Counter(r["word"] for r in table)


def _own_rule_words(rec, rule_label, reading):
    own = Counter({w: 0 for w in WORDS})
    for row in rec["transport"][reading]["numerals"]:
        pv = row["parent_value"]
        ms = row["evidence"].get("measured", [])
        if not ms:
            own["BREAKS"] += 1
            continue
        if rule_label == "the declared rule":
            fn = lambda a: math.comb(a, 2) + pv - math.comb(3, 2)
        else:
            base = math.comb(3, 2) - 2
            fn = lambda a: (math.comb(a, 2) - (a * a) // 4) + pv - base
        lit = all(v == pv for _a, v in ms)
        ta = all(v == fn(aa) for aa, v in ms)
        own["LAW-IN-A" if ta else ("NEEDS-3" if lit else "BREAKS")] += 1
    return own


HEAD_RESOLVERS = {
    "arena_n": lambda r: r["arena"]["q"] ** 2,
    "arena_q": lambda r: r["arena"]["q"],
    "arena_L": lambda r: r["arena"]["L"],
    "arena_cells": lambda r: r["arena"]["n"] * r["arena"]["L"],
    "characteristic": lambda r: r["arena"]["characteristic"],
    "arities": lambda r: [row["a"] for row in r["substrate"]["rows"]],
    "n_arities": lambda r: len(r["substrate"]["rows"]),
    "idle_arities": lambda r: [row["a"] for row in r["substrate"]["rows"]
                               if row["idle_actors"]],
    "ladder_bound": lambda r: r["arena"]["ladder_search_bound"],
    "sat_cap": lambda r: r["arena"]["sat_sample_cap"],
    "node_cap": lambda r: r["arena"]["cover_node_cap"],
    "lin_subspaces": lambda r: sum(
        c for _o, c in r["readings"]["linear_order_counts"]),
    "linear_orders": lambda r: sorted(
        o for o, _c in r["readings"]["linear_order_counts"]),
    "abs_subgroups": lambda r: sum(
        c for _o, c in r["readings"]["abstract_order_counts"]),
    "abstract_orders": lambda r: sorted(
        o for o, _c in r["readings"]["abstract_order_counts"]),
    "lin_proper": lambda r: [x for x in r["readings"]["linear_orders"]
                             if 1 < x < r["arena"]["n"]],
    "lin_conclusion": lambda r: r["conditional"]["linear_conclusion"],
    "abs_proper": lambda r: [x for x in r["readings"]["abstract_orders"]
                             if 1 < x < r["arena"]["n"]],
    "satmax_selects": lambda r: [
        row["a"] for row in r["principles"]["rows"]
        if row["saturation_is_maximality"] and 1 < row["a"]
        < r["arena"]["n"]][0],
    "n_principles": lambda r: len(r["principles"]["admits"]),
    "n_candidates": lambda r: len(r["principles"]["rows"]),
    "arena_modulus": lambda r: (r["arena"]["n"] * r["arena"]["L"])
    // math.gcd(r["arena"]["n"] * r["arena"]["L"], r["arena"]["n"]),
    "theorem_pairs": lambda r: r["modulus_theorem"]["pairs_holding"],
    "found_arities": lambda r: [f[0] for f in
                                r["modulus_theorem"]["found_rungs"]],
    "found_rows": lambda r: len(r["modulus_theorem"]["found_rungs"]),
    "mod_a_rows": lambda r: len([f for f in
                                 r["modulus_theorem"]["found_rungs"]
                                 if f[1] == f[0]]),
    "diff_rows": lambda r: len([f for f in
                                r["modulus_theorem"]["found_rungs"]
                                if f[0] != r["arena"]["L"]]),
    "a8_pool": lambda r: r["law4_ladder"]["census_leg_a8"]["saturating"],
    "n_statements": lambda r: len(_lin(r)["statements"]),
    "n_numerals": lambda r: len(_lin(r)["numerals"]),
    "lin_stmt_lawin": lambda r: _own_words(
        _lin(r)["statements"])["LAW-IN-A"],
    "lin_stmt_breaks": lambda r: _own_words(
        _lin(r)["statements"])["BREAKS"],
    "abs_stmt_lawin": lambda r: _own_words(
        _abs(r)["statements"])["LAW-IN-A"],
    "abs_stmt_breaks": lambda r: _own_words(
        _abs(r)["statements"])["BREAKS"],
    "parent_stmt_lawin": lambda r: r["parent_words"]["stmt_lawin"],
    "parent_stmt_breaks": lambda r: r["parent_words"]["stmt_breaks"],
    "parent_num_needs": lambda r: r["parent_words"]["num_needs"],
    "num_lawin": lambda r: _own_rule_words(r, "the declared rule",
                                           "linear")["LAW-IN-A"],
    "num_needs": lambda r: _own_rule_words(r, "the declared rule",
                                           "linear")["NEEDS-3"],
    "num_breaks": lambda r: _own_rule_words(r, "the declared rule",
                                            "linear")["BREAKS"],
    "cf_lawin": lambda r: _own_rule_words(r, ALT_RULES[-1][0],
                                          "linear")["LAW-IN-A"],
    "cf_needs": lambda r: _own_rule_words(r, ALT_RULES[-1][0],
                                          "linear")["NEEDS-3"],
    "cf_breaks": lambda r: _own_rule_words(r, ALT_RULES[-1][0],
                                           "linear")["BREAKS"],
    "moved_across_n": lambda r: sum(
        1 for row in r["transport"]["both_arena_words"]
        if row["parent_word_at_nine"] != row["linear_word_here"]),
    "scope_qualifier": lambda r: _lin(r)["numerals"][0]["scope"],
    "census_a4": lambda r: [row["groupings"] for row in
                            r["substrate"]["rows"]
                            if row["a"] == r["arena"]["committed_arity"]][0],
    "substrate_groupings": lambda r: [row["groupings"] for row in
                                      r["substrate"]["rows"]],
    "substrate_idle": lambda r: [row["idle_actors"] for row in
                                 r["substrate"]["rows"]],
    "substrate_sat": lambda r: [row["saturating_budget"] for row in
                                r["substrate"]["rows"]],
    "parent_sat": lambda r: [row["n9_saturating_budget"] for row in
                             r["substrate"]["both_arena_rows"]],
    "substrate_maxw": lambda r: [row["max_weight"] for row in
                                 r["substrate"]["rows"]],
    "naming_comparisons": lambda r: r["law1_naming"]["comparisons"],
    "perm_window": lambda r: r["law1_naming"]["window_size"],
    "naming_mismatches": lambda r: r["law1_naming"]["mismatches"],
    "naming_positive": lambda r: r["law1_naming"]["positive"],
    "naming_negative": lambda r: (r["law1_naming"]["comparisons"]
                                  - r["law1_naming"]["positive"]),
    "fid_comparisons": lambda r: r["fidelity"]["anchored"]
    ["route_comparisons"],
    "fid_positive": lambda r: r["fidelity"]["anchored"]["route_positive"],
    "fid_vac": lambda r: r["fidelity"]["anchored"]
    ["route_positive_empty_prefix"],
    "lin_nonunique": lambda r: r["law5_forcing"]["rows"][4]["F4-LINEAR"]
    ["non_unique"],
    "lin_rounds": lambda r: r["law5_forcing"]["rows"][4]["F4-LINEAR"]
    ["rounds"],
    "abs_nonunique": lambda r: r["law5_forcing"]["rows"][4]["ABSTRACT"]
    ["non_unique"],
    "abs_rounds": lambda r: r["law5_forcing"]["rows"][4]["ABSTRACT"]
    ["rounds"],
    "crystal_floors": lambda r: [
        r["law2_certificates"]["floor"][i]["certified_floor"]
        for i in range(len(r["law2_certificates"]["floor"]))],
    "counting_bound": lambda r: r["law2_crystallization"]["counting_bound"],
    "a2_schedule": lambda r: r["law2_crystallization"]["schedule"]["a2"]
    ["min_events"],
    "a2_pool": lambda r: r["law2_crystallization"]["schedule"]["a2"]
    ["pool"],
    "a4_schedule": lambda r: r["law2_crystallization"]["schedule"]["a4"]
    ["min_events"],
    "a4_window": lambda r: r["law2_crystallization"]["schedule"]["a4"]
    ["window_histories"],
    "offsets": lambda r: [r["law2_crystallization"]["offsets"][k]
                          for k in sorted(r["law2_crystallization"]
                                          ["offsets"])],
    "offset_arities": lambda r: [int(k) for k in
                                 sorted(r["law2_crystallization"]
                                        ["offsets"])],
    "menu_survivors": lambda r: r["law3_menu"]["survivors"],
    "menu_cos_abs": lambda r: r["law3_menu"]["abstract_cosets"],
    "menu_cos_lin": lambda r: r["law3_menu"]["linear_cosets"],
    "links_generate": lambda r: r["arena"]["links_generate_order"],
    "menu_nonuniform": lambda r: r["law3_menu"]["nonuniform_survivors"],
    "frc_lin_rounds": lambda r: r["law5_forcing"]["rows"][4]["F4-LINEAR"]
    ["rounds"],
    "frc_lin_classes": lambda r: r["law5_forcing"]["rows"][4]["F4-LINEAR"]
    ["non_unique_that_are_parallel_classes"],
    "frc_abs_rounds": lambda r: r["law5_forcing"]["rows"][4]["ABSTRACT"]
    ["rounds"],
    "frc_abs_classes": lambda r: r["law5_forcing"]["rows"][4]["ABSTRACT"]
    ["non_unique_that_are_parallel_classes"],
    "frc_a2_nonunique": lambda r: r["law5_forcing"]["rows"][2]["ABSTRACT"]
    ["non_unique"],
    "frc_a2_rounds": lambda r: r["law5_forcing"]["rows"][2]["ABSTRACT"]
    ["rounds"],
    "m_fork": lambda r: r["arena"]["coin_modulus_fork"],
    "union_carriers": lambda r: r["law6_sec2"]["union_carriers"],
    "union_pairs": lambda r: r["law6_sec2"]["union_realised_pairs"],
    "union_doubled": lambda r: r["law6_sec2"]["union_doubled_pairs"],
    "seam_declared": lambda r: r["law6_sec2"]
    ["seam_pairs_that_are_declared_links"],
    "sec2_min_inside": lambda r: [
        row["measured_min_within_sector_pairs"]
        for row in r["law6_sec2"]["rows"]],
    "sec2_span": lambda r: [row["seam_spanning"]
                            for row in r["law6_sec2"]["rows"]],
    "sec2_opens_none": lambda r: [row["seam_spanning"]
                                  - row["opens_a_pair_inside_a_sector"]
                                  for row in r["law6_sec2"]["rows"]],
    "sec2_free": lambda r: [row["obstruction_free"]
                            for row in r["law6_sec2"]["rows"]],
    "link_edges": lambda r: r["law6_sec2"]["sector_link_pairs"],
    "off_span": lambda r: r["law6_sec2"]["off_undeclared_span_pairs"],
}

HEAD_REQUIRED = ("scope_qualifier", "lin_conclusion", "abs_proper",
                 "satmax_selects", "sec2_free", "offsets", "mod_a_rows",
                 "found_arities", "idle_arities", "num_needs",
                 "moved_across_n", "menu_nonuniform")

# structural name patterns the head scan strips by declaration, each with a
# required-use finding if it stops occurring.
HEAD_STRIPS = ((r"\bE-\d+\b", "an engraving id"),
               (r"\bLEG-1\b", "a criterion-leg id"),
               (r"nL/gcd\(nL,n\)=L", "the theorem's own formula"))


def head_audit(rec, segments, fields):
    findings = []
    blob = " ".join(segments)
    for pat, why in HEAD_STRIPS:
        _s, nfound = re.subn(pat, " ", blob)
        if not nfound:
            findings.append({"declared_exemption_never_used": why})
    if not any(w in blob for w in WORDS):
        findings.append({"declared_exemption_never_used": "an outcome word"})

    total = 0
    for i, (text, flds) in enumerate(zip(segments, fields)):
        scanned = text
        for pat, _w in HEAD_STRIPS:
            scanned = re.sub(pat, " ", scanned)
        for w in WORDS:
            scanned = scanned.replace(w, " ")
        seen = [int(t.replace(",", "")) for t in
                re.findall(r"(?<![\w.])(\d[\d,]*)(?!\.\d)(?!\w)", scanned)]
        expect = []
        for (k, v) in flds:
            if k not in HEAD_RESOLVERS:
                findings.append({"segment": i, "stray_head_field": k})
                continue
            try:
                own = HEAD_RESOLVERS[k](rec)
            except Exception as exc:                       # pragma: no cover
                findings.append({"segment": i, "field": k,
                                 "resolver_failed": str(exc)[:60]})
                continue
            if isinstance(v, str):
                if own != v:
                    findings.append({"segment": i, "field": k,
                                     "text_field_disagrees": [str(own)[:40],
                                                              v[:40]]})
                if v not in text:
                    findings.append({"segment": i, "field": k,
                                     "text_field_absent": v[:40]})
                if re.search(r"\d", v):
                    findings.append({"segment": i, "field": k,
                                     "text_field_carries_a_numeral": v[:40]})
                continue
            same = (list(own) == list(v) if isinstance(v, (list, tuple))
                    else own == v)
            if not same:
                findings.append({"segment": i, "field": k,
                                 "recomputed": own, "rendered": v})
            expect.extend(v if isinstance(v, (list, tuple)) else [v])
        total += len(seen)
        if seen != expect:
            findings.append({"segment": i, "positional_mismatch": True,
                             "numerals_in_the_segment": seen[:40],
                             "declared_fields_in_order": expect[:40]})

    present = {k for f in fields for (k, _v) in f}
    missing = [k for k in HEAD_REQUIRED if k not in present]
    if missing:
        findings.append({"required_head_fields_missing": missing})

    for reading, table in (("linear", _lin(rec)), ("abstract", _abs(rec))):
        own_stmt = Counter()
        for row in table["statements"]:
            ev = row["evidence"]
            own_stmt["BREAKS" if ev.get("fails_at")
                     or ev.get("reason") == "NO-FEASIBLE-ROW"
                     else "LAW-IN-A"] += 1
        built_stmt = Counter(r["word"] for r in table["statements"])
        if own_stmt != built_stmt:
            findings.append({"statement_words_disagree_" + reading:
                             [dict(own_stmt), dict(built_stmt)]})
        own_num = _own_rule_words(rec, "the declared rule", reading)
        built_num = Counter(r["word"] for r in table["numerals"])
        if dict(own_num) != {w: built_num.get(w, 0) for w in WORDS}:
            findings.append({"numeral_words_disagree_" + reading:
                             [dict(own_num), dict(built_num)]})

    flat = blob.replace(",", "")
    for tally in (_own_rule_words(rec, "the declared rule", "linear"),
                  _own_rule_words(rec, ALT_RULES[-1][0], "linear")):
        for w, c in tally.items():
            if "%d %s" % (c, w) not in flat:
                findings.append({"word_tally_not_rendered_beside_its_count":
                                 [w, c]})
    laws = {r["law"] for r in _lin(rec)["statements"]}
    if len(segments) != len(laws) + 4:
        findings.append({"segment_count": len(segments),
                         "laws_plus_four": len(laws) + 4})
    if not segments[-1].startswith("SCOPE="):
        findings.append({"last_segment_is_not_the_scope_line": True})
    words_in_head = {w for w in WORDS if w in blob}
    words_used = ({r["word"] for r in _lin(rec)["statements"]}
                  | {r["word"] for r in _lin(rec)["numerals"]}
                  | {r["word"] for r in _abs(rec)["statements"]}
                  | {r["word"] for r in _abs(rec)["numerals"]}
                  | {"NEEDS-3"})
    # NEEDS-3 stands in the head as a TALLY OF ZERO -- the word names the
    # column whose count is the measurement, and the register carries the
    # measured reason it never fired.
    if not words_in_head <= words_used:
        findings.append({"head_uses_a_word_no_row_earned":
                         sorted(words_in_head - words_used)})
    return {"findings": findings,
            "numerals_in_the_head": total,
            "fields_declared": sum(len(f) for f in fields),
            "required_fields": len(HEAD_REQUIRED),
            "resolvers": len(HEAD_RESOLVERS),
            "positionally_bound": total}


COVERAGE_STRIPS = [
    (r"\b1,2,4,8,16\b", "the registration's order list, quoted verbatim "
     "with the frozen pin's own spacing; the values are bound instead by "
     "the reading gate's parse and by the spaced prose lists"),
    (r"\b1,4,16\b", "the registration's linear list, quoted verbatim"),
    (r"\bleg-1\b", "a criterion-leg id"),
    (r"paper-\d+", "a paper id"),
    (r"\bv1[0-9]\b", "a programme version"),
    (r"#\d+", "a ledger entry id"),
    (r"\bE-\d+\b", "an engraving id"),
    (r"\b[Ss]ections? \d+(?: and \d+)?", "a cross-reference to a section"),
    (r"(?m)^#+\s+\d+\.?", "a numbered section heading"),
    (r"\b[0-9a-f]{12}\b", "a digest prefix"),
]


def receipt_numbers(rec):
    out = set()

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                walk(k)
                walk(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                walk(v)
        elif isinstance(o, bool):
            return
        elif isinstance(o, int):
            out.add(o)
        elif isinstance(o, str):
            for t in re.findall(r"(?<![\w.])(\d[\d,]*)(?!\.\d)(?!\w)", o):
                out.add(int(t.replace(",", "")))
    walk(rec)
    return out


def paper_coverage(rec, text):
    stripped = text
    used = []
    for pat, why in COVERAGE_STRIPS:
        nfound = len(re.findall(pat, stripped))
        if nfound:
            used.append({"pattern": pat, "reason": why, "hits": nfound})
        stripped = re.sub(pat, " ", stripped)
    nums = [int(t.replace(",", ""))
            for t in re.findall(r"(?<![\w.])(\d[\d,]*)(?!\.\d)(?!\w)",
                                stripped)]
    have = receipt_numbers(rec)
    bad = sorted({v for v in nums if v not in have})
    return {"numerals_scanned": len(nums), "distinct": len(set(nums)),
            "uncovered": bad, "strips_used": used,
            "strips_declared": len(COVERAGE_STRIPS),
            "strips_never_used": [p for p, _w in COVERAGE_STRIPS
                                  if p not in [u["pattern"] for u in used]]}


def paper_polarity(rec, text):
    t = canon(" ".join(text.split("```")[0::2])).lower()
    srows = {r["a"]: r for r in rec["law6_sec2"]["rows"]}
    frc = rec["law5_forcing"]["rows"]
    lin_t, abs_t = _lin(rec), _abs(rec)
    rows = [
        ("the two readings disagree",
         rec["conditional"]["linear_proper_sizes"]
         != rec["conditional"]["abstract_proper_sizes"],
         r"the two readings disagree",
         r"the two readings agree"),
        ("the linear branch tracks the field",
         rec["conditional"]["linear_conclusion"] == rec["arena"]["q"],
         r"selects the field order",
         r"fails to select the field order"),
        ("saturation-is-maximality follows the characteristic",
         [row["a"] for row in rec["principles"]["rows"]
          if row["saturation_is_maximality"]]
         == [rec["arena"]["characteristic"]],
         r"the characteristic, not the field order",
         r"the field order, not the characteristic"),
        ("mod-a appears only where a equals L",
         all(f[1] == rec["arena"]["L"]
             for f in rec["modulus_theorem"]["found_rungs"]),
         r"mod-a appears at no row where the event size and the "
         r"declared link count differ",
         r"mod-a appears at a row where the event size and the "
         r"declared link count differ"),
        ("the budget returns at two actors",
         [row["saturating_budget"] for row in rec["substrate"]["rows"]
          if row["a"] == 2][0] > 0,
         r"non-empty at this arena",
         r"empty at this arena too"),
        ("the forcing thesis splits on the reading",
         (frc[2]["F4-LINEAR"]["thesis_holds_per_object"]
          and not frc[2]["ABSTRACT"]["thesis_holds_per_object"]),
         r"holds on the linear window and is false as stated on the "
         r"abstract",
         r"holds on both windows"),
        ("the sharpened floor transports",
         all(rec["law2_crystallization"]["sharpened_floors"][str(a)]
             == rec["law2_crystallization"]["floors"][str(a)]
             for a in rec["arena"]["arities"]),
         r"reproduces the certified floor at every arity",
         r"fails at some arity"),
        ("the obstruction minima equal the closed form",
         all(row["measured_min_within_sector_pairs"]
             == row["forced_inside_bound"]
             for row in rec["law6_sec2"]["rows"]),
         r"to its closed form at every arity",
         r"differs from the closed form"),
        ("the menu breaks under both readings",
         (rec["law3_menu"]["survivors"]
          > rec["law3_menu"]["abstract_cosets"]
          > rec["law3_menu"]["linear_cosets"]),
         r"neither reading's set is the survivor set",
         r"the survivor set is exactly the coset partitions"),
        ("no numeral stands still",
         _own_rule_words(rec, "the declared rule", "linear")["NEEDS-3"]
         == 0,
         r"no parent numeral stands still",
         r"a parent numeral stands still"),
    ]
    bad = []
    for (name, truth, pos, neg) in rows:
        has_pos = re.search(pos, t) is not None
        has_neg = re.search(neg, t) is not None
        if truth and not has_pos:
            bad.append({"claim": name, "missing_the_true_direction": pos})
        if truth and has_neg:
            bad.append({"claim": name, "carries_the_false_direction": neg})
        if not truth and has_pos:
            bad.append({"claim": name, "asserts_a_false_direction": pos})
        if not truth and not has_neg:
            bad.append({"claim": name, "missing_the_true_direction": neg})
    return {"claims": len(rows), "violations": bad}


def paper_spelled(rec, text, RR, claims):
    """THE SPELLED-NUMERAL GATE: the same prose scanned in the other
    alphabet, four ways -- universe binding, pair binding, the rendered
    spelled claims at exact occurrence counts, and their inversions
    required absent."""
    ref = RR.gate(text, COVERAGE_STRIPS, spelled=True)
    prose = canon(" ".join(text.split("```")[0::2])).casefold()
    claim_bad, inv_bad = [], []
    for (rendered, inverted) in claims:
        got = prose.count(canon(rendered).casefold())
        if got != 1:
            claim_bad.append({"claim": rendered[:70], "occurrences": got})
        if re.search(inverted, prose):
            inv_bad.append({"claim": rendered[:70], "inversion": inverted})
    words = sorted({w for w in SPELLED_SCANNED
                    if re.search(r"\b%s\b" % w, prose)})
    return {"spelled_sentences_checked": ref["sentences_checked"],
            "spelled_pairs_checked": ref["pairs_checked"],
            "spelled_cardinals_present": words,
            "spelled_claims": len(claims),
            "declared_exclusions": SPELLED_EXCLUDED,
            "universe_violations": ref["violations"],
            "claim_violations": claim_bad,
            "inversion_violations": inv_bad}
# ===========================================================================
# SECTION 6.  CLAIMS, REFERENTS, WALLS, FALSIFIERS, BATTERY, PROMOTION, CLI
# ===========================================================================

def register_claims(rec, CL):
    ar = rec["arena"]
    A_ = ar["arities"]
    sub = {r["a"]: r for r in rec["substrate"]["rows"]}
    bn = {r["a"]: r for r in rec["substrate"]["both_arena_rows"]}
    cry = rec["law2_crystallization"]
    cert = rec["law2_certificates"]["floor"]
    srows = {r["a"]: r for r in rec["law6_sec2"]["rows"]}
    frc = rec["law5_forcing"]["rows"]
    lad = {r["a"]: r for r in rec["law4_ladder"]["rows"]}
    mt = rec["modulus_theorem"]
    menu = rec["law3_menu"]
    rd = rec["readings"]
    cd = rec["conditional"]
    pr = rec["principles"]
    lin_t, abs_t = _lin(rec), _abs(rec)
    corp = {r["a"]: r for r in rec["corpus"]}
    out = {}

    out["T-ARENA"] = CL.table(
        "T-ARENA", ("row", "value"),
        [[k, v] for (k, v) in ar["declaration"]])
    out["T-SOURCES"] = CL.table(
        "T-SOURCES", ("id", "path", "sha256-12"),
        [[p["id"], p["path"], p["sha256_12"]] for p in rec["provenance"]])
    out["T-READINGS"] = CL.table(
        "T-READINGS",
        ("reading", "lattice members", "orders", "proper nontrivial sizes",
         "the conditional selects"),
        [["F4-LINEAR (primary)", rd["linear_subspaces"],
          ", ".join(str(x) for x in rd["linear_orders"]),
          ", ".join(str(x) for x in cd["linear_proper_sizes"]),
          "a = %d = q" % cd["linear_conclusion"]],
         ["ABSTRACT (disclosed)", rd["abstract_subgroups"],
          ", ".join(str(x) for x in rd["abstract_orders"]),
          ", ".join(str(x) for x in cd["abstract_proper_sizes"]),
          "a set, not a size"]])
    out["T-FIDELITY"] = CL.table(
        "T-FIDELITY", ("row", "re-derived", "committed anchor"),
        [[k, rec["fidelity"]["measured"][k], rec["fidelity"]["anchored"][k]]
         for k in sorted(rec["fidelity"]["measured"])])
    out["T-SUBSTRATE"] = CL.table(
        "T-SUBSTRATE",
        ("a", "blocks", "idle", "groupings", "max weight",
         "saturating at the budget", "budget-saturating at nine actors"),
        [[a, sub[a]["blocks_per_round"], sub[a]["idle_actors"],
          sub[a]["groupings"], sub[a]["max_weight"],
          sub[a]["saturating_budget"], bn[a]["n9_saturating_budget"]]
         for a in A_])
    out["T-CORPUS"] = CL.table(
        "T-CORPUS",
        ("a", "abstract coset rounds", "linear coset rounds",
         "budget-saturating abstract rounds", "window basis",
         "covering tuples", "refusal"),
        [[a, corp[a]["singles_abstract"], corp[a]["singles_linear"],
          corp[a]["saturating_abstract_rounds"], corp[a]["window_basis"],
          corp[a]["covering_tuples"],
          corp[a]["refusal"]["stamp"] if corp[a]["refusal"] else "none"]
         for a in A_])
    out["T-CRYSTAL"] = CL.table(
        "T-CRYSTAL",
        ("a", "certified floor", "sharpened floor", "counting bound",
         "schedule time", "schedule ground", "offset"),
        [[a, cry["floors"][str(a)], cry["sharpened_floors"][str(a)],
          cry["counting_bound"],
          cry["schedule"]["a2"]["min_events"] if a == 2 else
          cry["schedule"]["a4"]["min_events"] if a == 4 else "refused",
          "complete pool sweep" if a == 2 else
          "committed window" if a == 4 else
          "REFUSED-BY-THE-COMMITTED-GRAMMAR",
          cry["offsets"].get(str(a), "none")] for a in A_])
    out["T-LADDER"] = CL.table(
        "T-LADDER",
        ("a", "saturating rounds", "witness window", "witness status",
         "achievable budgets within the bound"),
        [[r["a"], r["saturating"], r["witness_window"] or "none",
          r["witness_status"],
          ", ".join(str(b) for b in r["achievable_budgets"]) or "none"]
         for r in rec["law4_ladder"]["rows"]]
        + [[rec["law4_ladder"]["census_leg_a9"]["a"],
            rec["law4_ladder"]["census_leg_a9"]["saturating"],
            rec["law4_ladder"]["census_leg_a9"]["witness_window"],
            rec["law4_ladder"]["census_leg_a9"]["witness_status"],
            ", ".join(str(b) for b in rec["law4_ladder"]["census_leg_a9"]
                      ["achievable_budgets"]) or "none"],
           [rec["law4_ladder"]["census_leg_a8"]["a"],
            rec["law4_ladder"]["census_leg_a8"]["saturating"],
            rec["law4_ladder"]["census_leg_a8"]["witness_window"],
            rec["law4_ladder"]["census_leg_a8"]["witness_status"],
            ", ".join(str(b) for b in rec["law4_ladder"]["census_leg_a8"]
                      ["achievable_budgets"]) or "none"]])
    out["T-MENU"] = CL.table(
        "T-MENU", ("object", "count"),
        [["invariant-partition survivors, complete closure",
          menu["survivors"]],
         ["abstract coset partitions among them", menu["abstract_cosets"]],
         ["linear coset partitions among them", menu["linear_cosets"]],
         ["survivors with mixed block sizes", menu["nonuniform_survivors"]]])
    out["T-FORCING"] = CL.table(
        "T-FORCING",
        ("a", "window", "rounds", "non-unique",
         "of them parallel classes", "thesis per object"),
        [[a, tag, frc[a][tag]["rounds"], frc[a][tag]["non_unique"],
          frc[a][tag]["non_unique_that_are_parallel_classes"],
          "holds" if frc[a][tag]["thesis_holds_per_object"] else "false"]
         for a in A_ for tag in ("F4-LINEAR", "ABSTRACT")
         if tag in frc[a]]
        + [[a, "both", "refused", "refused", "refused",
            frc[a]["refusal"]["stamp"]]
           for a in A_ if "refusal" in frc[a]])
    out["T-SEC2"] = CL.table(
        "T-SEC2",
        ("a", "groups", "seam-spanning", "opens no pair inside a sector",
         "and doubles nothing", "measured min inside", "closed form"),
        [[a, srows[a]["groups"], srows[a]["seam_spanning"],
          srows[a]["within_sector_free"], srows[a]["obstruction_free"],
          srows[a]["measured_min_within_sector_pairs"],
          srows[a]["forced_inside_bound"]] for a in A_])
    out["T-CENSUS"] = CL.table(
        "T-CENSUS",
        ("candidate a", "divides n", "saturates the budget",
         "budget is the maximum", "linear coset order",
         "abstract subgroup order", "cover at R = L"),
        [[r["a"], "yes" if r["round_completeness"] else "no",
          "yes" if r["saturation_at_the_budget"] else "no",
          "yes" if r["saturation_is_maximality"] else "no",
          "yes" if r["subgroup_order_available_linear"] else "no",
          "yes" if r["subgroup_order_available_abstract"] else "no",
          r["cover_at_R_equals_L"]] for r in pr["rows"]])
    out["T-STATEMENTS"] = CL.table(
        "T-STATEMENTS",
        ("law", "linear word", "abstract word", "holds at (linear)",
         "fails at (linear)", "scope"),
        [[rl["law"], rl["word"], ra["word"],
          ", ".join(str(x) for x in rl["evidence"].get("holds_at", []))
          or "none",
          ", ".join(str(x) for x in rl["evidence"].get("fails_at", []))
          or "none", rl["scope"]]
         for rl, ra in zip(lin_t["statements"], abs_t["statements"])])
    out["T-NUMERALS"] = CL.table(
        "T-NUMERALS",
        ("law", "numeral", "parent value", "measured (linear)",
         "measured (abstract)", "word here", "word at nine actors"),
        [[rl["law"], rl["numeral"], rl["parent_value"],
          "|".join(str(v) for _a, v in rl["evidence"].get("measured", []))
          or "no row",
          "|".join(str(v) for _a, v in ra["evidence"].get("measured", []))
          or "no row",
          rl["word"], bw["parent_word_at_nine"]]
         for rl, ra, bw in zip(lin_t["numerals"], abs_t["numerals"],
                               rec["transport"]["both_arena_words"])])
    out["T-RULES"] = CL.table(
        "T-RULES",
        ("uniform a-only rule", "reading", "LAW-IN-A", "NEEDS-3", "BREAKS"),
        [[k, tag, v["LAW-IN-A"], v["NEEDS-3"], v["BREAKS"]]
         for tag, t in (("F4-LINEAR", lin_t), ("ABSTRACT", abs_t))
         for k, v in sorted(t["aggregate_under_each_rule"].items())])

    CL.claim("all %s fidelity rows agree with the committed anchors "
             "%d of %d" % (SPELLED[rec["fidelity"]["rows"]],
                           rec["fidelity"]["agree"],
                           rec["fidelity"]["rows"]))
    CL.claim("the survivor set has %d members, the %d abstract coset "
             "partitions and the %d linear ones are all among them, and "
             "neither reading's set is the survivor set"
             % (menu["survivors"], menu["abstract_cosets"],
                menu["linear_cosets"]))
    CL.claim("%d survivors have mixed block sizes"
             % menu["nonuniform_survivors"])
    CL.claim("rungs were found at %d, %d and %d actors per event, and "
             "every found set is exactly the multiples of the declared "
             "link count" % tuple(f[0] for f in mt["found_rungs"]))
    CL.claim("mod-a appears at no row where the event size and the "
             "declared link count differ")
    CL.claim("at two actors every one of the %d seam-spanning events "
             "opens no pair inside a sector and doubles nothing"
             % srows[2]["obstruction_free"])
    CL.claim("the measured minima read %d, %d, %d and %d, equal to the "
             "parent's anchored column and to its closed form at every "
             "arity" % tuple(srows[a]["measured_min_within_sector_pairs"]
                             for a in A_))
    CL.claim("on the abstract window all %d rounds are non-unique and "
             "only %d are parallel classes"
             % (frc[4]["ABSTRACT"]["rounds"],
                frc[4]["ABSTRACT"]["non_unique_that_are_parallel_classes"]))
    CL.claim("on the linear window all %d rounds are non-unique and "
             "every one is a parallel class"
             % frc[4]["F4-LINEAR"]["rounds"])
    CL.claim("the certified floors read %d, %d, %d and %d"
             % tuple(cry["floors"][str(a)] for a in A_))
    CL.claim("the schedule time is %d events at two actors, complete "
             "over the %d-matching pool, and %d at the committed arity "
             "on NDEP's %d-tuple window, within the declared corpus rule"
             % (cry["schedule"]["a2"]["min_events"],
                cry["schedule"]["a2"]["pool"],
                cry["schedule"]["a4"]["min_events"],
                cry["schedule"]["a4"]["window_histories"]))
    off_pair = [cry["offsets"][k] for k in sorted(cry["offsets"])]
    CL.claim("the offsets read %d and %d against the parent's constant %d"
             % (off_pair[0], off_pair[1],
                [r["parent_value"] for r in lin_t["numerals"]
                 if r["numeral"] == "the offset between them"][0]))
    CL.claim("the budget-saturating count at two actors is %d against "
             "the parent arena's anchored %d"
             % (sub[2]["saturating_budget"],
                bn[2]["n9_saturating_budget"]))
    CL.claim("the %d groupings NDEP declared out of scope are censused "
             "entire" % sub[4]["groupings"])
    CL.claim("the abstract lattice has %d subgroups whose orders are the "
             "divisors of %d exactly, and the linear lattice has %d "
             "subspaces" % (rd["abstract_subgroups"], ar["n"],
                            rd["linear_subspaces"]))
    CL.claim("saturation-is-maximality admits %d alone -- the "
             "characteristic, not the field order"
             % [row["a"] for row in pr["rows"]
                if row["saturation_is_maximality"]][0])
    for s in verdict_segments(rec):
        CL.fence(s)
    return out


def spelled_claims(rec):
    cry = rec["law2_crystallization"]
    A_ = rec["arena"]["arities"]
    sharp = sum(1 for a in A_
                if cry["sharpened_floors"][str(a)] == cry["floors"][str(a)])
    frc = rec["law5_forcing"]["rows"]
    found = rec["modulus_theorem"]["found_rungs"]
    moved = len(rec["transport"]["moved_across_n"])
    nnum = len(_lin(rec)["numerals"])
    sels = [v for v in rec["principles"]
            ["unique_nontrivial_selections"].values() if v is not None]
    return [
        ("the sharpened floor reproduces the certified floor at all %s "
         "arities" % SPELLED[sharp],
         r"the sharpened floor fails at"),
        ("the linear window at the committed arity carries %s rounds and "
         "every one is non-unique"
         % SPELLED[frc[4]["F4-LINEAR"]["rounds"]],
         r"carries (?:%s) rounds and every one is non-unique"
         % "|".join(w for i, w in enumerate(SPELLED)
                    if i != frc[4]["F4-LINEAR"]["rounds"])),
        ("rungs were found at %s event sizes" % SPELLED[len(found)],
         r"rungs were found at (?:%s) event sizes"
         % "|".join(w for i, w in enumerate(SPELLED) if i != len(found))),
        ("%s of the %s numeral rows keep their parent word at the second "
         "arena" % (SPELLED[nnum - moved], SPELLED[nnum]),
         r"(?:%s) of the (?:%s) numeral rows keep"
         % ("|".join(w for i, w in enumerate(SPELLED) if i != nnum - moved),
            "|".join(SPELLED))),
        ("%s of the %s candidate principles admit a single nontrivial "
         "event size, and they admit different sizes"
         % (SPELLED[len(sels)], SPELLED[len(rec["principles"]["admits"])]),
         r"and they admit the same size"),
    ]


def register_referents(rec, RR):
    ar = rec["arena"]
    A_ = ar["arities"]
    sub = {r["a"]: r for r in rec["substrate"]["rows"]}
    bn = {r["a"]: r for r in rec["substrate"]["both_arena_rows"]}
    cry = rec["law2_crystallization"]
    srows = {r["a"]: r for r in rec["law6_sec2"]["rows"]}
    frc = rec["law5_forcing"]["rows"]
    menu = rec["law3_menu"]
    rd = rec["readings"]
    pr = rec["principles"]
    mt = rec["modulus_theorem"]
    lin_t, abs_t = _lin(rec), _abs(rec)
    corp = {r["a"]: r for r in rec["corpus"]}
    base = set(A_) | {ar["n"], ar["q"], ar["L"], ar["cells"],
                      ar["characteristic"], ar["links_generate_order"],
                      0, 1}
    RR.universe("substrate", ["grouping", "packing", "idle", "weight",
                              "round mass", "census", "block"],
                base | {sub[a][k] for a in A_ for k in
                        ("groupings", "idle_actors", "max_weight",
                         "saturating_budget", "saturating_maximum",
                         "blocks_per_round", "budget")}
                | {bn[a]["n9_saturating_budget"] for a in A_}
                | {bn[a]["n9_groupings"] for a in A_}
                | {ar["sat_sample_cap"], ar["cover_node_cap"],
                   ar["prefix_window"]},
                [(sub[a]["saturating_budget"], sub[a]["groupings"])
                 for a in A_])
    RR.universe("readings", ["subgroup", "subspace", "lattice", "coset",
                             "divisor", "reading", "translation group"],
                base | set(rd["abstract_orders"]) | set(rd["linear_orders"])
                | {rd["abstract_subgroups"], rd["linear_subspaces"]}
                | {c for _o, c in rd["abstract_order_counts"]}
                | {c for _o, c in rd["linear_order_counts"]}
                | {3, 9},
                [(rd["linear_subspaces"], rd["abstract_subgroups"])])
    RR.universe("crystallization", ["floor", "schedule", "offset",
                                    "witness", "signature", "crystalliz"],
                base | {cry["floors"][str(a)] for a in A_}
                | {cry["sharpened_floors"][str(a)] for a in A_}
                | {cry["counting_bound"],
                   cry["schedule"]["a2"]["min_events"],
                   cry["schedule"]["a2"]["pool"],
                   cry["schedule"]["a2"]["ordered_pairs"],
                   cry["schedule"]["a4"]["min_events"],
                   cry["schedule"]["a4"]["window_histories"]}
                | set(cry["offsets"].values())
                | {v for c in rec["law2_certificates"]["floor"]
                   for w in c["refusals_below"]
                   for v in (w.get("lightest_total"), w.get("budget"),
                             w.get("k"), w.get("distinct_available"),
                             w.get("actors"))
                   if isinstance(v, int)}
                | {sub[a]["saturating_budget"] for a in A_},
                [(sum(1 for a in A_ if cry["sharpened_floors"][str(a)]
                      == cry["floors"][str(a)]), len(A_))])
    RR.universe("union", ["seam", "crossing", "cross pair", "union",
                          "carrier", "obstruction", "forced inside",
                          "maximum cut", "doubl", "sector"],
                base | {srows[a][k] for a in A_ for k in
                        ("groups", "seam_spanning", "within_sector_free",
                         "obstruction_free", "forced_inside_bound",
                         "measured_min_within_sector_pairs",
                         "max_cut_of_the_complete_graph",
                         "opens_a_pair_inside_a_sector")}
                | {rec["law6_sec2"]["union_carriers"],
                   rec["law6_sec2"]["union_realised_pairs"],
                   rec["law6_sec2"]["union_doubled_pairs"],
                   rec["law6_sec2"]["sector_link_pairs"],
                   rec["law6_sec2"]["off_undeclared_span_pairs"]},
                [(srows[a]["within_sector_free"],
                  srows[a]["seam_spanning"]) for a in A_]
                + [(srows[a]["obstruction_free"],
                    srows[a]["seam_spanning"]) for a in A_]
                + [(srows[a]["seam_spanning"], srows[a]["groups"])
                   for a in A_]
                + [(srows[2]["obstruction_free"],
                    srows[2]["obstruction_free"])])
    RR.universe("factorization", ["factoriz", "non-unique", "admissible",
                                  "survivor", "menu", "joiner", "round",
                                  "parallel class", "partition"],
                base | {menu["survivors"], menu["abstract_cosets"],
                        menu["linear_cosets"],
                        menu["nonuniform_survivors"]}
                | {frc[a][t][k] for a in A_ for t in
                   ("F4-LINEAR", "ABSTRACT") if t in frc[a]
                   for k in ("rounds", "non_unique",
                             "non_unique_that_are_parallel_classes")}
                | {frc[a]["covering_tuples"]["histories"] for a in A_
                   if "covering_tuples" in frc[a]}
                | {int(k) for a in A_ for t in ("F4-LINEAR", "ABSTRACT")
                   if t in frc[a]
                   for k in frc[a][t]["joiner_counts"]}
                | {v for a in A_ for t in ("F4-LINEAR", "ABSTRACT")
                   if t in frc[a]
                   for v in frc[a][t]["joiner_counts"].values()}
                | {24, 48},
                [(frc[a][t]["non_unique"], frc[a][t]["rounds"])
                 for a in A_ for t in ("F4-LINEAR", "ABSTRACT")
                 if t in frc[a]]
                + [(frc[4]["ABSTRACT"]
                    ["non_unique_that_are_parallel_classes"],
                    frc[4]["ABSTRACT"]["rounds"]),
                   (menu["abstract_cosets"], menu["survivors"]),
                   (menu["linear_cosets"], menu["survivors"]),
                   (menu["nonuniform_survivors"], menu["survivors"]),
                   (frc[4]["ABSTRACT"]["rounds"],
                    frc[4]["ABSTRACT"]["rounds"]),
                   (frc[4]["F4-LINEAR"]["rounds"],
                    frc[4]["F4-LINEAR"]["rounds"]),
                   (frc[2]["ABSTRACT"]["rounds"],
                    frc[2]["ABSTRACT"]["rounds"])])
    RR.universe("ladder", ["ladder", "rung", "modulus", "budget", "weld",
                           "arena pair", "cover", "mass"],
                base | {r["saturating"] for r in
                        rec["law4_ladder"]["rows"]}
                | {rec["law4_ladder"]["census_leg_a9"]["saturating"],
                   rec["law4_ladder"]["census_leg_a8"]["saturating"], 9, 8}
                | {b for r in rec["law4_ladder"]["rows"]
                   for b in r["achievable_budgets"]}
                | {mt["pairs_checked"], mt["pairs_holding"],
                   mt["arena_modulus"], ar["ladder_search_bound"]}
                | {corp[a][k] for a in A_ for k in
                   ("window_basis", "saturating_abstract_rounds",
                    "covering_tuples")}
                | {r["a"] for r in rec["principles"]["rows"]},
                [(mt["pairs_holding"], mt["pairs_checked"]),
                 (len(mt["mod_a_appears_at"]), len(mt["found_rungs"]))])
    RR.universe("transport", ["law-in-a", "needs-3", "breaks", "statement",
                              "numeral", "word", "rule", "aggregate",
                              "slot", "tally"],
                base | {len(lin_t["statements"]), len(lin_t["numerals"])}
                | {c for t in (lin_t, abs_t)
                   for v in t["aggregate_under_each_rule"].values()
                   for c in v.values()}
                | {c for t in (lin_t, abs_t)
                   for c in t["statement_words"].values()}
                | {rec["parent_words"]["stmt_lawin"],
                   rec["parent_words"]["stmt_breaks"],
                   rec["parent_words"]["num_needs"],
                   rec["parent_words"]["num_breaks"],
                   rec["parent_words"]["cf_lawin"],
                   len(rec["transport"]["moved_across_n"]),
                   len(rec["transport"]["split_statements"]),
                   len(rec["transport"]["split_numerals"])}
                | {r["parent_value"] for r in lin_t["numerals"]},
                [(c, len(lin_t["statements"]))
                 for t in (lin_t, abs_t)
                 for c in t["statement_words"].values()]
                + [(c, len(lin_t["numerals"]))
                   for t in (lin_t, abs_t)
                   for c in t["numeral_words"].values()]
                + [(len(rec["transport"]["moved_across_n"]),
                    len(lin_t["numerals"])),
                   (len(lin_t["numerals"])
                    - len(rec["transport"]["moved_across_n"]),
                    len(lin_t["numerals"]))])
    RR.universe("corpus", ["window", "tuple", "history", "prefix", "cap",
                           "permutation", "comparison", "route",
                           "mismatch", "stabilizer"],
                base | {corp[a][k] for a in A_ for k in
                        ("singles_abstract", "singles_linear",
                         "window_basis", "saturating_abstract_rounds",
                         "covering_tuples")}
                | {rec["law1_naming"][k] for k in
                   ("comparisons", "mismatches", "positive", "negative",
                    "window_size", "linear_share_comparisons",
                    "s16_not_filtered")}
                | {rec["fidelity"]["measured"][k]
                   for k in rec["fidelity"]["measured"]}
                | {rec["fidelity"]["rows"], rec["fidelity"]["agree"]}
                | {ar["sat_sample_cap"], ar["cover_node_cap"],
                   ar["prefix_window"]},
                [(rec["law1_naming"]["positive"],
                  rec["law1_naming"]["comparisons"]),
                 (rec["fidelity"]["agree"], rec["fidelity"]["rows"]),
                 (rec["fidelity"]["measured"]["route_positive"],
                  rec["fidelity"]["measured"]["route_comparisons"]),
                 (rec["fidelity"]["agree"], rec["fidelity"]["agree"])])
    RR.universe("principles", ["principle", "selector", "candidate event "
                               "size", "census row", "antecedent"],
                base | {len(pr["rows"]), len(pr["admits"])}
                | set(rd["abstract_orders"]) | set(rd["linear_orders"])
                | {3, 9}
                | {len([v for v in pr["unique_nontrivial_selections"]
                        .values() if v is not None])},
                [(len([v for v in pr["unique_nontrivial_selections"]
                       .values() if v is not None]),
                  len(pr["admits"]))])
    RR.exempt_token("sha256", "an algorithm name")


PARAPHRASE_FLOOR = 15

PARAPHRASE_PLANTS = [
    ("P-SIXTEEN-NO-FREEDOM",
     "Sixteen actors leave the event size no freedom once cosets are "
     "demanded."),
    ("P-LATTICE-SETTLES",
     "The lattice of AG(2, 4) settles what a division event must be."),
    ("P-LINEAR-DETERMINES",
     "Under the linear lattice the theory determines the event size "
     "outright."),
    ("P-RECONSTRUCTION-SETTLES",
     "Because the reconstruction succeeds at sixteen actors, the arity is "
     "settled there too."),
    ("P-MENU-IS-CONTENT",
     "The menu's invariant partitions are the theory's real content, the "
     "rest being notation."),
    ("P-ISP-AT-THREE",
     "In ISP at three actors the round simply parks one idle site."),
    ("P-THEORY-AT-FIVE",
     "The theory at five actors keeps the whole ladder."),
    ("P-GLUING-FREE",
     "At two actors gluing is free of charge at this arena as well."),
    ("P-FAMILY-RUNG",
     "Across the ISP family the first rung is always the link count."),
    ("P-FAMILY-OFFSET",
     "Any ISP model whatever returns offset one between the schedule and "
     "the floor."),
    ("P-MOST-SIZES",
     "Most event sizes admit no homogeneous record, so a random arity is "
     "almost surely rungless."),
    ("P-TYPICAL-GROUPING",
     "A typical grouping at sixteen actors saturates."),
    ("P-MENU-Q-CARRIED",
     "The menu count stands still along a, so it is q-carried."),
    ("P-SURVIVING-NUMERALS",
     "Numerals that survive the sweep belong to the field order."),
    ("P-RECORDS-PROVE",
     "Records generated at four actors suffice to recover the plane, "
     "which proves four is the event size."),
    ("P-CHAR-CARRIES",
     "Saturation-is-maximality is carried by the characteristic."),
    ("P-ONE-BLOCK-SIZE",
     "Only one block size lets the plane close, and the corpus knew it."),
    ("P-READINGS-AGREE",
     "The two readings agree once the census is read correctly."),
]


def build_walls():
    """THE PARENT'S EIGHT READING WALLS, VERBATIM IN DISCIPLINE, WITH THIS
    UNIT'S SUBJECTS WHERE THE ARENA MOVED -- AND A NINTH OF THIS UNIT'S
    OWN, POLICING THE READING-MERGE, THE ONE DISEASE THIS PIN ADDS.  Every
    wall polices a CLAIM through a licence leg; bare negations and hedges
    are refused at construction."""
    return [
        SemanticWall(
            "W-NO-SELECTION",
            [r"(?:the )?(?:event size|arity|a)\b[^.]{0,40}"
             r"\bis (?:uniquely )?selected\b",
             r"(?:the )?(?:event size|arity)[^.]{0,40}\b(?:is|are) "
             r"(?:therefore )?(?:forced|determined|fixed) by (?:a|the) law",
             r"(?:this|the) unit (?:shows|proves|establishes)[^.]{0,30}"
             r"(?:four|4) is (?:the |a )?(?:right|correct|necessary)",
             r"nothing (?:else )?could have been the event size"],
            [r"nothing measured here selects", r"implicit in a constructor"],
            ["The measurements above show that the event size is uniquely "
             "selected by the theory's own laws.",
             "The arity is therefore forced by a law of the corpus rather "
             "than by the arena.",
             "This unit proves that four is the correct event size."],
            subject=(r"\b(?:arity|arities|event size|event sizes|block "
                     r"size|block sizes|group size|division event|four "
                     r"actors|four-actor|actors per event)\b",),
            policed=(r"\bselect\w*", r"(?<!division-)\bforc\w+",
                     r"\bdetermin\w+",
                     r"\brequir\w+", r"\bnecessar\w+", r"\bmandat\w+",
                     r"\bdemand\w+", r"\bsettl\w+", r"\bestablish\w+",
                     r"\bno other (?:choice|option|size|possibilit\w+)\b",
                     r"\bmust be\b", r"\bfixed by\b", r"\bcompel\w+",
                     r"\bdictat\w+", r"\bleaves no\b", r"\bobliged\b",
                     r"\bonly one\b", r"\bthe only (?:size|choice|option)\b",
                     r"\badmits no rival\b", r"\bno rival\b",
                     r"\bcloses on\b", r"\bhad to be\b", r"\bno freedom\b",
                     r"\bknew it\b"),
            licences=(r"\bassumptions\b", r"\bimplicit in a constructor\b",
                      r"\bif\b[^.]{0,200}\bthen\b", r"\bidentifiability\b",
                      r"\bdiscriminat\w+", r"\bnothing measured here\b",
                      r"\bwithout the arena\b", r"\bcandidate\b",
                      r"\bextension\b", r"\bcounting-only\b",
                      r"\bnever registered\b", r"\bnever pre-registered\b",
                      r"\bat this arena\b", r"\bfree declaration\b",
                      r"\bthe pin asks\b", r"\bwithin the declared\b",
                      r"\bantecedent\b")),
        SemanticWall(
            "W-NO-PROBABILITY",
            [r"\b(?:probabilit|likelihood|likely|chance)\w*\b[^.]{0,40}"
             r"\barit(?:y|ies)\b",
             r"most (?:arities|event sizes) (?:are|admit)",
             r"\btypical(?:ly)? (?:arity|event size|grouping)\b"],
            [r"counting-only"],
            ["Most arities admit no homogeneous record, so the probability "
             "that a random arity carries one is small.",
             "A typical event size behaves like the committed one.",
             "On average an arity of this arena admits a covering class."],
            subject=(r"\b(?:arity|arities|event size|event sizes|grouping"
                     r"s?|histor(?:y|ies)|fraction|round)\b",),
            policed=(r"\bprobabilit\w*", r"\blikelihood\b", r"\blikely\b",
                     r"\bchance\b", r"\btypical\w*", r"\bon average\b",
                     r"\bexpected value\b", r"\bat random\b",
                     r"\brandomly\b", r"\bmost (?:arities|event sizes)\b",
                     r"\balmost surely\b"),
            licences=(r"\bcounting-only\b", r"\bno measure\b",
                      r"\bno distribution\b", r"\ba count of\b",
                      r"\bcomplete census\b", r"\bevery grouping\b",
                      r"\bnothing sampled\b", r"\bdeclared window\b")),
        SemanticWall(
            "W-NO-CARRIER-OVERREACH",
            [r"\b(?:the (?:numeral|value|count)s?|it) (?:is|are) "
             r"(?:therefore )?carried by (?:the )?(?:field order|q|"
             r"characteristic)\b",
             r"\bthis unit (?:shows|proves)[^.]{0,40}\bq[- ]carried\b",
             r"\bstanding still (?:here )?(?:shows|proves|means) "
             r"(?:it is )?q[- ]carried"],
            [r"names no other carrier|surviving candidate"],
            ["Because the count stands still while the event size moves, "
             "it is carried by the field order.",
             "This unit proves the menu's numeral is q-carried.",
             "A numeral that stands still here is carried by the field "
             "order."],
            subject=(r"\b(?:numerals?|values?|counts?|menu|modulus|first "
                     r"rung|stands? still|standing still|does not move|"
                     r"saturation-is-maximality|selector)\b",),
            policed=(r"\bis (?:therefore )?carried by\b",
                     r"\bare (?:therefore )?carried by\b",
                     r"\bq[- ]carried\b", r"\bn[- ]carried\b",
                     r"\bbelongs? to the field order\b",
                     r"\bthe field order carries\b",
                     r"\bthe characteristic carries\b",
                     r"\bwhat carries\b"),
            licences=(r"\bnames no other carrier\b",
                      r"\bsurviving candidate\b", r"\brefut\w+",
                      r"\bnot-carried-by-a\b", r"\bat fixed n\b",
                      r"\bthe constant reading\b",
                      r"\bwhich of the standing coordinates\b",
                      r"\bcannot separate\b", r"\bcoincide\b",
                      r"\bcandidate reading\b")),
        SemanticWall(
            "W-NO-RECONSTRUCTION-AS-DERIVATION",
            [r"\b(?:recover(?:able|ed|s)?|reconstruct\w*|self-consistent)\b"
             r"[^.]{0,60}\b(?:therefore|hence|so)\b[^.]{0,40}"
             r"\b(?:selected|derived|forced)\b",
             r"\bbecause (?:the|its) structure is recoverable\b",
             r"\bthat the (?:parent's|committed) arity works\b[^.]{0,60}"
             r"\b(?:selects|derives|proves)\b"],
            [r"identifiability", r"discriminat"],
            ["Because the committed structure is recoverable from records "
             "generated at that arity, the arity is therefore derived.",
             "That the committed arity works, and is self-consistent, "
             "selects it.",
             "The reconstruction succeeds, hence the event size is "
             "forced."],
            subject=(r"\b(?:recover\w*|reconstruct\w*|reconstructible|"
                     r"self-consistent|identifiab\w+|records generated)\b",),
            policed=(r"\bselect\w*", r"\bderiv\w+", r"\bforc\w+",
                     r"\bprov\w+", r"\bestablish\w+", r"\bsettl\w+",
                     r"\bshow\w*\b", r"\bhad to be\b", r"\bsuffice\w*\b"),
            licences=(r"\bidentifiability\b", r"\bdiscriminat\w+",
                      r"\bdifferent property\b",
                      r"\bnever promoted to\b", r"\bis a weaker\b",
                      r"\bwhich is a different\b")),
        SemanticWall(
            "W-NO-INVARIANCE-AS-GAUGE",
            [r"\b(?:a-inert|invarian\w*|unchanged)\b[^.]{0,50}"
             r"\b(?:is|are) (?:therefore )?(?:a )?gauge\b",
             r"\bstanding still\b[^.]{0,40}\b(?:physical|observable)\b",
             r"\bthe menu('s value)? is (?:therefore )?"
             r"(?:physically )?meaningless\b"],
            [r"before an operational observable exists"],
            ["The menu's value is unchanged across arities and is "
             "therefore a gauge of the theory.",
             "Standing still under the sweep makes the quantity physical.",
             "The menu is therefore physically meaningless."],
            subject=(r"\b(?:menu|invarian\w*|a-inert|inert|unchanged|"
                     r"stands? still|standing still|does not move|reads "
                     r"the same|survive the whole sweep|constant "
                     r"across)\b",),
            policed=(r"\bgauge\b", r"\bphysic\w*", r"\bobservable\b",
                     r"\bmeaningless\b", r"\breal content\b",
                     r"\bontolog\w+", r"\bredundan\w+",
                     r"\bpart of the theory\b", r"\bdescriptive\b",
                     r"\bbookkeep\w+", r"\bbelongs to the description\b",
                     r"\bno content\b", r"\bcontent an experiment\b",
                     r"\bto the world\b", r"\bpresentation\b",
                     r"\bnotation\b"),
            licences=(r"\bbefore an operational\b", r"\bforbidden\b",
                      r"\binvariance and nothing more\b", r"\bdisclosure\b",
                      r"\ba-inert by construction\b", r"\bcounting-only\b",
                      r"\bno sentence here promotes\b",
                      r"\bthat promotion is\b")),
        SemanticWall(
            "W-EXTENSION-SCOPE",
            [r"\bin isp at (?:two|three|five) actors\b",
             r"\bthe theory at (?:two|three|five) actors\b"],
            [r"the refusal is the measurement"],
            ["In ISP at two actors the census reports what the theory "
             "does.",
             "The theory at three actors keeps every law but the ladder.",
             "The corpus at five actors carries the same covering class."],
            subject=(r"\bat (?:two|three|five) actors\b",
                     r"\b(?:two|three|five)-actor world\b"),
            policed=(r"\bisp\b", r"\bthe theory\b", r"\bthe corpus\b",
                     r"\bthe committed\b", r"\bkeeps\b", r"\bloses\b",
                     r"\bparks\b"),
            licences=(r"\bextension\b", r"\bpacking rule\b",
                      r"\bthis unit\b", r"\bwithin the declared\b",
                      r"\bdeclared extension family\b",
                      r"\bidle remainder\b", r"\bdeclaration\b",
                      r"\brefus\w+", r"\bcoset window\b"),),
        SemanticWall(
            "W-NO-MOTIVATION-CLAIM",
            [r"\bgluing is (?:therefore )?(?:a )?free\b",
             r"\bmotivated\b[^.]{0,30}\bat (?:two|2) actors\b",
             r"\bthis unit (?:measures|shows|proves)[^.]{0,30}"
             r"\bfree items?\b"],
            [r"(?:is|are) that unit's measurement and (?:is|are) not "
             r"recomputed"],
            ["At two actors gluing is therefore a free event of the "
             "theory.",
             "Every crossing is motivated at two actors.",
             "This unit measures the free items of the crossing "
             "directly."],
            subject=(r"\b(?:gluing|crossing|crossings|seam-spanning|free "
                     r"items?|motivat\w+)\b",),
            policed=(r"\bfree\b", r"\bmotivated\b", r"\bpriced at\b",
                     r"\bcosts nothing\b", r"\blawful\b",
                     r"\bautonomous\b", r"\bfree of charge\b"),
            licences=(r"that unit's measurement", r"\brequires the price\b",
                      r"\bthe unit that owns the update rule\b",
                      r"\bis not decided here\b", r"\bare not recomputed\b",
                      r"\bquestion for the unit\b",
                      r"\bthe price the unit\b", r"\bcounting-only\b",
                      r"\bpair combinatorics\b")),
        SemanticWall(
            "W-NO-FAMILY-PREDICTION",
            [r"\bacross the isp family\b",
             r"\bany isp model\b[^.]{0,60}\b(?:gives|predicts|returns)\b",
             r"\bat every arena\b[^.]{0,40}\b(?:the|this) "
             r"(?:corpus|theory)\b[^.]{0,20}\bpredicts\b",
             r"\bthe ladder predicts the same modulus for every\b"],
            [r"one point of a|two points of a"],
            ["Across the ISP family the offset between the schedule and "
             "the floor is one.",
             "Any ISP model gives the same admissible-partition count.",
             "The ladder predicts the same modulus for every ISP model."],
            subject=(r"\b(?:the isp family|across the isp|any isp model|"
                     r"every isp model|every arena|any arena|in general|"
                     r"this theory|the theory|every model|whatever "
                     r"arena)\b",),
            policed=(r"\bpredicts?\b", r"\balways\b", r"\bat every arena\b",
                     r"\bin any arena\b", r"\bin general\b",
                     r"\bwhatever\b", r"\bprecisely when\b",
                     r"\bfor all arenas\b", r"\buniversally\b",
                     r"\bevery still-free\b"),
            licences=(r"\bat this arena\b", r"\bat the declared arena\b",
                      r"\bone point of a\b", r"\btwo points of a\b",
                      r"\bfibre\b", r"\bstill-free\b",
                      r"\bmember-specific\b", r"\bthe declared arena\b",
                      r"\bis a theorem\b", r"\bdeclared arena pairs\b",
                      r"\bwithin the declared\b", r"\bthis unit "
                      r"measures\b", r"\bat both arenas\b",
                      r"\bboth arenas measured\b")),
        SemanticWall(
            "W-NO-READING-MERGE",
            [r"\bthe two readings agree\b",
             r"\bthe readings (?:can|may) be merged\b",
             r"\b(?:merge|averag)\w*[^.]{0,30}\bthe (?:two )?readings\b",
             r"\beither reading (?:will do|gives the same)\b"],
            [r"never merged"],
            ["The two readings agree once the details are set aside.",
             "The readings can be merged into a single verdict.",
             "Either reading gives the same census in the end."],
            subject=(r"\b(?:the two readings|both readings|either reading|"
                     r"reading-dependent|the abstract reading|the linear "
                     r"reading)\b",),
            policed=(r"\bagree\w*", r"\bmerge\w*", r"\baverag\w+",
                     r"\bcombine\w*", r"\bthe same answer\b",
                     r"\bequivalent\b", r"\binterchangeab\w+",
                     r"\bwill do\b"),
            licences=(r"\bdisagree\w*", r"\bpart company\b",
                      r"\breported beside\b",
                      r"\badjudication\b", r"\bdistinct\b",
                      r"\bsplits? on the reading\b",
                      r"\breading-relative\b", r"\bpre-registered\b")),
    ]
# ---------------------------------------------------------------------------
# THE FALSIFIERS (family h): every one names the object it must MOVE.
# ---------------------------------------------------------------------------

def _probe_packing():
    return {a: sum(packing_distribution(a).values()) for a in IDLE_ARITIES}


def _probe_fidelity():
    _cls, cov = class_tuples16()
    return len(cov)


def _probe_order():
    return [order_predicate(1, 2), order_predicate(2, 1)]


def _probe_naming():
    P = A.coset_partition(frozenset([(0, 0), A.LINKS[0]]))
    return route_scan([tuple(A.round_events(P))],
                      corrupt=mut("MUT-NAMING"))["mismatches"]


def _probe_reading():
    return len(A.f4_subspaces(SUBS))


def _probe_extend():
    return packings_prefix(COMMITTED_ARITY, 6, drop_idle=True)


def _probe_corpus():
    return len(corpora()[2]["singles_abstract"])


def _probe_floorcert():
    k, _w, _r, _n = certified_floor(2)
    return k


def _probe_schedule():
    return schedule_sweep_a2()["min_events"]


def _probe_floor():
    return weight_floor(A.n, A.q if mut("MUT-FLOOR") else 2)


def _probe_menu():
    return len(survivors())


def _probe_ladder():
    return ladder_row(COMMITTED_ARITY)["achievable_budgets"]


def _probe_theorem():
    out = []
    for nn in range(1, THEOREM_N_MAX + 1):
        for ll in range(1, THEOREM_L_MAX + 1):
            cells = nn * ll
            out.append(cells // math.gcd(cells, nn) == ll)
    if mut("MUT-THEOREM"):
        out[0] = not out[0]
    return out


def _probe_forcing():
    surv = survivors()
    P = A.coset_partition(frozenset([(0, 0), A.LINKS[0]]))
    H = tuple(A.round_events(P))
    rec = record_vector(H)
    return sum(1 for p in surv if admissible(p, H, rec, M_FORK[1]))


def _probe_sec2():
    return [r["obstruction_free"] for r in sec2_census()["rows"]]


def _probe_principle():
    rows = principle_census()["rows"]
    return [(r["a"], r["round_completeness"]) for r in rows]


def _probe_disagree():
    lin = [x for x in sorted({len(H) for H in F4SUBS}) if 1 < x < A.n]
    ab = [x for x in sorted({len(H) for H in SUBS}) if 1 < x < A.n]
    if mut("MUT-DISAGREE"):
        ab = list(lin)
    return (lin, ab)


def _probe_transport():
    rows = [arow(a, True, a, "synthetic") for a in ARITIES]
    w, _ev = transport_word(PARENT_ARITY, rows)
    if mut("MUT-TRANSPORT"):
        w = WORDS[0]
    return w


def _probe_agg_probe():
    return _probe_agg()


def _probe_head():
    sample = "SEGMENT<MEASURED 7>"
    return sample[:-1] + " FORGED 424242>" if mut("MUT-HEAD") else sample


def _probe_seal():
    pay = {"fidelity": {"agree": 10, "rows": 10}}
    if mut("MUT-SEAL-ADD"):
        pay["forged_finding"] = {"headline": "everything transports"}
    if mut("MUT-SEAL-EDIT"):
        pay["fidelity"] = dict(pay["fidelity"])
        pay["fidelity"]["agree"] = pay["fidelity"]["rows"] + 1
    return sorted(pay.items(), key=repr)


UNDECLARED_READ = "RUNBOOK.md"


def _undeclared_read():
    try:
        with open(os.path.join(REPO, UNDECLARED_READ), "rb") as fh:
            fh.read(len(UNDECLARED_READ))
    except OSError:
        pass


def _probe_read():
    if mut("MUT-READ"):
        _undeclared_read()
    return sorted({r for r in RS.reads})


def _probe_anchor():
    needle = canon(VERBATIM[0][2])
    return needle[:-6] + "XXXXXX" if mut("MUT-ANCHOR") else needle


def _probe_close():
    return GATE_ORDER[:-1] if mut("MUT-CLOSE") else GATE_ORDER


def _probe_sources():
    return [(sid, "0" * 12 if mut("MUT-SOURCE") and sid == SOURCES[0][0]
             else sha) for (sid, _rel, sha, _w) in SOURCES]


def _probe_paths():
    return [(aid, v + 1 if mut("MUT-PATH") and aid == PATH_ANCHORS[0][0]
             and isinstance(v, int) else v)
            for (aid, _s, _p, v, _c) in PATH_ANCHORS]


def _probe_prereg():
    d = digest([list(t) for t in PREREGISTERED])
    return "MOVED" if mut("MUT-PREREG") else d


def _probe_promotion():
    banner = "BANNER"
    forged = "  a summary line the run never declared"
    allowed = {banner}
    if mut("MUT-PROMOTION"):
        allowed = allowed | {forged}
    tr = Transcript()
    refused_line = False
    try:
        tr.bind_narrative(banner + "\n" + forged + "\n", allowed)
    except GateFail:
        refused_line = True
    led = Ledger()
    led.rows.append({"n": len(ARITIES), "gate": "G-REHEARSAL",
                     "statement": "", "evidence": {}, "passed": True,
                     "prev": "", "row_digest": ""})
    sl = Seal()
    sl.seal("k", {"v": len(ARITIES)}, "G-REHEARSAL")
    body = {"k": {"v": len(ARITIES) if mut("MUT-PROMOTION")
                  else len(ARITIES) + len(WORDS)}}
    refused_edit = False
    try:
        sl.verify_at_promotion(body, led, "seal_manifest")
    except GateFail:
        refused_edit = True
    return [refused_line, refused_edit]


def _probe_template():
    return sorted(TEMPLATE_FAMILIES) if not mut("MUT-TEMPLATE") else []


def hash_ban_scan(source):
    """calls to the builtin hash or id anywhere in a source: both are
    per-process accidents (PYTHONHASHSEED, allocator state) and a receipt
    that consumed either would be seed-dependent."""
    if mut("MUT-HASH"):
        return []
    bad = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Call):
            fn = node.func
            if isinstance(fn, ast.Name) and fn.id in ("hash", "id"):
                bad.append(fn.id)
    return bad


def _probe_hash():
    return hash_ban_scan("x = hash(y)\nz = id(w)\n")


def _probe_paper(kind):
    def go():
        base = ("the survivor set has 307 members, the 67 abstract coset "
                "partitions and the 7 linear ones are all among them")
        if mut(kind):
            return base.replace("307 members", "424242 members")
        return base
    return go


FALSIFIERS = [
    Falsifier("MUT-SOURCE", "G-SOURCES",
              "a declared source digest is replaced by zeros, so the bytes "
              "the unit reads stop being the bytes it pinned",
              "the declared source digests", _probe_sources),
    Falsifier("MUT-PATH", "G-PATH-ANCHORS",
              "an anchored (path, value) pair's value is shifted, so a "
              "read at the declared path stops agreeing",
              "the anchored values", _probe_paths),
    Falsifier("MUT-ANCHOR", "G-VERBATIM",
              "a verbatim needle's tail is replaced, so the quotation "
              "stops matching the pinned source's bytes",
              "the located anchor text", _probe_anchor),
    Falsifier("MUT-ARENA", "G-ARENA16",
              "the computed characteristic is shifted, so the arena stops "
              "being the one whose characteristic differs from q",
              "the computed characteristic", _probe_arena),
    Falsifier("MUT-READING", "G-READINGS",
              "the linear-subspace filter drops one field scalar, so the "
              "primary reading silently widens past the registration",
              "the linear subspace count", _probe_reading),
    Falsifier("MUT-FIDELITY", "G-CONSTRUCTOR-FIDELITY",
              "one covering class tuple is dropped, so the constructor "
              "stops reproducing NDEP's committed window",
              "the covering-tuple count", _probe_fidelity),
    Falsifier("MUT-ORDER", "G-FIDELITY-FIRST",
              "the ordering predicate is inverted, so a run in which the "
              "fidelity gate fired late would pass",
              "the ordering predicate on fixed inputs", _probe_order),
    Falsifier("MUT-EXTEND", "G-PACKING-EXTENDS16",
              "the partition route returns one prefix object fewer, so "
              "the packing rule stops extending the committed constructor "
              "on the declared window",
              "the prefix object list", _probe_extend),
    Falsifier("MUT-PACKING", "G-SUBSTRATE-CENSUS",
              "the census recursion loses its idle branch, so every arity "
              "that does not divide the actor count collapses to zero "
              "groupings against a non-zero closed form",
              "the idle-arity census totals", _probe_packing),
    Falsifier("MUT-CORPUS", "G-CORPUS-RULE",
              "the smallest arity's single-round window gains a duplicate "
              "round, so the window stops being the coset window",
              "the single-round window count", _probe_corpus),
    Falsifier("MUT-NAMING", "G-LAW1-NAMING16",
              "one event mask of route A is corrupted, so route A's "
              "stabilizer stops being route B's",
              "the mismatch count on one window history", _probe_naming),
    Falsifier("MUT-FLOORCERT", "G-LAW2-FLOOR-CERTIFICATE16",
              "the certified floor is shifted off the witnessed value at "
              "the smallest arity",
              "the certified floor at the smallest arity", _probe_floorcert),
    Falsifier("MUT-SCHEDULE", "G-LAW2-SCHEDULE16",
              "the complete sweep's minimum is shifted below the certified "
              "floor, which the gate forbids because a floor is a floor",
              "the swept minimum at the smallest arity", _probe_schedule),
    Falsifier("MUT-FLOOR", "G-LAW2-SHARPENED16",
              "the sharpened floor is driven by the FIELD ORDER instead of "
              "the event size the quotation names, which is exactly the "
              "reading this unit is testing",
              "the sharpened floor at the smallest arity", _probe_floor),
    Falsifier("MUT-MENU", "G-LAW3-MENU16",
              "the invariance closure spreads only the first link's span, "
              "so partitions the dropped links police re-enter the "
              "survivor set",
              "the survivor count", _probe_menu),
    Falsifier("MUT-LADDER", "G-LAW4-LADDER16",
              "every searched budget is reported achievable at the "
              "committed arity, so the rungs stop being the multiples of "
              "the link count",
              "the achievable-budget set at the committed arity",
              _probe_ladder),
    Falsifier("MUT-THEOREM", "G-MODULUS-THEOREM",
              "the modulus identity is falsified at one declared arena "
              "pair, so the theorem's sweep stops holding",
              "the arena sweep of the identity", _probe_theorem),
    Falsifier("MUT-FORCING", "G-LAW5-FORCING16",
              "the history leg is forced true, so partitions the events "
              "do not respect become admissible and every non-unique "
              "count moves",
              "the admissible count at one coset round", _probe_forcing),
    Falsifier("MUT-SEC2-THEOREM", "G-LAW6-SEC2-16",
              "the doubling list is emptied at three actors, so groups "
              "that must double appear obstruction-free where the theorem "
              "says none can be",
              "the obstruction-free column", _probe_sec2),
    Falsifier("MUT-PRINCIPLE", "G-PRINCIPLE-CENSUS16",
              "the divisibility verdict at the committed arity is "
              "inverted, so the census stops being a measurement of the "
              "principle",
              "the round-completeness column", _probe_principle),
    Falsifier("MUT-DISAGREE", "G-CONDITIONAL",
              "the abstract antecedent set is replaced by the linear one "
              "-- the merge the pin forbids -- so the readings' "
              "disagreement disappears",
              "the two antecedent sets", _probe_disagree),
    Falsifier("MUT-TRANSPORT", "G-TRANSPORT-CONTROLS",
              "the decision procedure is short-circuited to its first "
              "word, so every numeral is reported to transport",
              "the word the procedure returns on a synthetic law",
              _probe_transport),
    Falsifier("MUT-AGG", "G-AGGREGATE16",
              "the two-level slot name is taken from a paraphrase instead "
              "of the parent's own engraving",
              "the parsed slot name", _probe_agg_probe),
    Falsifier("MUT-HEAD", "G-VERDICT-EQUALITY",
              "a numeral in the head is replaced by one no measurement "
              "licenses, leaving every gate above it green",
              "the emitted head", _probe_head),
    Falsifier("MUT-CLAIM", "G-PAPER-CLAIMS",
              "a licensed claim's numeral is replaced, so the rendering "
              "the paper must carry stops being the receipt's",
              "the licensed claim string", _probe_paper("MUT-CLAIM")),
    Falsifier("MUT-COVER", "G-PAPER-COVERAGE",
              "an unlicensed numeral is planted in the scanned text",
              "the scanned numeral set", _probe_paper("MUT-COVER")),
    Falsifier("MUT-REFERENT", "G-PAPER-REFERENTS",
              "a numeral from another universe is planted in a sentence "
              "whose subject noun selects this one",
              "the sentence's numerals", _probe_paper("MUT-REFERENT")),
    Falsifier("MUT-SPELLED", "G-PAPER-SPELLED",
              "a spelled falsehood is planted in prose, the corruption "
              "every digit scanner is blind to",
              "the scanned spelled text", _probe_paper("MUT-SPELLED")),
    Falsifier("MUT-POLARITY", "G-PAPER-POLARITY",
              "a direction-bearing sentence is inverted while every "
              "numeral stays where it was",
              "the polarity sentence set", _probe_paper("MUT-POLARITY")),
    Falsifier("MUT-WALL", "G-WALLS",
              "a banned sentence is inserted in house style",
              "the scanned paper text", _probe_paper("MUT-WALL")),
    Falsifier("MUT-PLANT", "G-WALL-PARAPHRASE",
              "a plant is replaced by a sentence that asserts nothing, so "
              "the battery would report a catch it did not make",
              "the planted sentence set", _probe_paper("MUT-PLANT")),
    Falsifier("MUT-TYPED", "G-NO-TYPED-COUNTS",
              "a numeral is typed into a published gate statement instead "
              "of arriving by name from the live registry",
              "the statement template", _probe_paper("MUT-TYPED")),
    Falsifier("MUT-HASH", "G-HASH-BAN",
              "the builtin-hash scanner is emptied, so a seed-dependent "
              "call would pass the ban unseen; the rehearsal hands it a "
              "planted call and requires a catch",
              "the scanner's verdict on the planted sample", _probe_hash),
    Falsifier("MUT-CACHE", "G-CACHE",
              "a memo key drops its mutant flag, so a recipe would be "
              "served the clean cached answer",
              "the cache key set", _probe_paper("MUT-CACHE")),
    Falsifier("MUT-EXACT", "G-EXACT",
              "a float reaches the receipt, which the type walk exists "
              "for",
              "the receipt's type set", _probe_paper("MUT-EXACT")),
    Falsifier("MUT-PREREG", "G-PREREGISTRATION",
              "the outcome register's digest is replaced, which is what a "
              "feasibility line rewritten after the outcome does",
              "the outcome register's digest", _probe_prereg),
    Falsifier("MUT-PROMOTION", "G-PROMOTION-REHEARSAL",
              "both promotion legs are inverted -- a forged narrative "
              "line accepted, an edited sealed value accepted",
              "the two promotion legs on fixed inputs", _probe_promotion),
    Falsifier("MUT-READ", "G-READ-SET",
              "a repository file outside the declared source list is "
              "opened, which the audit hook sees whoever calls it",
              "the recorded read multiset", _probe_read),
    Falsifier("MUT-ANCHOR-USE", "G-ANCHORS-CONSUMED",
              "an anchor's declared consumer is rewritten to a gate that "
              "never reads it",
              "the consumer register", _probe_paper("MUT-ANCHOR-USE")),
    Falsifier("MUT-TEMPLATE", "G-TEMPLATE-EXERCISED",
              "the template family register is emptied, so a family "
              "carried but never exercised would pass unnoticed",
              "the exercised family register", _probe_template),
    Falsifier("MUT-SEAL-ADD", "G-SEAL-TOTALITY",
              "a top-level key is created in the payload after the "
              "totality gate fired",
              "the payload's live key set", _probe_seal),
    Falsifier("MUT-SEAL-EDIT", "G-SEAL-TOTALITY",
              "a value inside a sealed key is mutated after its gate "
              "passed",
              "a sealed value", _probe_seal),
    Falsifier("MUT-CLOSE", "G-CLOSE",
              "a gate is removed from the declared inventory, so a run "
              "that fired a gate it does not declare would promote",
              "the declared gate inventory", _probe_close),
]


def run_falsifiers(paper_text, paper_rel):
    """each recipe in a NESTED, non-writing run; outer state saved and
    restored; the object under test THREADED IN, never re-defaulted (the
    ARITY #22 lesson)."""
    global MUTANT, IN_FALSIFIER, LD, TR, SEAL, CR, R, AN
    keep = (LD, TR, SEAL, CR, R, AN)
    keep_reads = list(RS.reads)
    keep_used = set(RS.used)
    rows = []
    base = {}
    for f in FALSIFIERS:
        if f.apply is not None:
            MUTANT = None
            base[f.name] = digest(f.apply())
    IN_FALSIFIER = True
    for f in FALSIFIERS:
        MUTANT = f.name
        iso_reads, iso_hits = list(RS.reads), MEMO_HITS.copy()
        moved = None
        if f.apply is not None:
            moved = digest(f.apply()) != base[f.name]
        died_at = None
        try:
            run_measurements(paper_text, paper_rel)
        except GateFail as e:
            died_at = str(e).split(" :: ")[0]
        except CliError as e:
            died_at = "CLI:" + str(e)
        MUTANT = None
        RS.reads[:] = iso_reads
        MEMO_HITS.clear()
        MEMO_HITS.update(iso_hits)
        rows.append({"falsifier": f.name, "declared_gate": f.gate,
                     "died_at": died_at, "target": f.target,
                     "target_moved": moved,
                     "description": f.description})
    IN_FALSIFIER = False
    LD, TR, SEAL, CR, R, AN = keep
    RS.reads[:] = keep_reads
    RS.used.clear()
    RS.used.update(keep_used)
    return rows


# ---------------------------------------------------------------------------
# THE CLOSING BATTERY, THE PROMOTION, AND THE CLI
# ---------------------------------------------------------------------------

IN_FALSIFIER = False
DECLARED_READS = []

TEMPLATE_FAMILIES = {
    "T-SEAL-PROMOTION": ("G-PROMOTION-REHEARSAL",
                         "seal_check_refuses_an_edited_value"),
    "T-TRANSCRIPT-BOUND": ("G-PROMOTION-REHEARSAL",
                           "narrative_binding_refuses_a_forged_line"),
    "T-WALL-SEMANTIC": ("G-WALLS", "walls"),
    "T-ANCHOR-CONSUMED": ("G-ANCHORS-CONSUMED", "reads"),
    "T-CLAIMS-EQUAL": ("G-PAPER-CLAIMS", "tables_claimed"),
    "T-REFERENT-BOUND": ("G-PAPER-REFERENTS", "sentences_checked"),
    "T-NO-TYPED-COUNTS": ("G-NO-TYPED-COUNTS", "offenders"),
    "T-FALSIFIER-POISONS": ("G-FALSIFIERS", "declared_gates"),
    "T-READ-SET": ("G-READ-SET", "distinct_reads"),
}

WAIVERS = {
    "G-FALSIFIERS": "the coverage gate is the one gate nothing falsifies "
                    "without falsifying the harness that would report it; "
                    "its own predicate carries the coverage result, and "
                    "the forcing check hands it an uncovered gate and "
                    "requires a refusal",
}


def coverage_forcing(gates, covered, waived):
    return sorted(g for g in gates if g not in covered and g not in waived)


def reset_state():
    global LD, TR, SEAL, CR, R, AN
    LD = Ledger()
    TR = Transcript()
    SEAL = Seal()
    CR = CountRegistry()
    for tok, why in (("2", "the affine plane's dimension, written AG(2, q)"),):
        CR.exempt_token(tok, why)
    R = {}
    AN = None


def exact_scan(obj, path="receipt"):
    bad = []

    def walk(o, p):
        if isinstance(o, bool) or o is None:
            return
        if isinstance(o, float):
            bad.append(p)
        elif isinstance(o, dict):
            for k, v in o.items():
                walk(v, p + "/" + str(k))
        elif isinstance(o, (list, tuple)):
            for i, v in enumerate(o):
                walk(v, p + "/%d" % i)
    walk(obj, path)
    return bad


def ast_float_scan(source):
    bad = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            bad.append(node.lineno)
    return bad


def paper_under(kind, text):
    if kind == "MUT-CLAIM" and mut("MUT-CLAIM"):
        return text + ("\n\nall ten fidelity rows agree with the committed "
                       "anchors 10 of 10\n")
    if kind == "MUT-COVER" and mut("MUT-COVER"):
        return text + "\n\nA further 424242 rows were censused.\n"
    if kind == "MUT-REFERENT" and mut("MUT-REFERENT"):
        return text + ("\n\nThe union census reports 2027025 seam-spanning "
                       "groups.\n")
    if kind == "MUT-POLARITY" and mut("MUT-POLARITY"):
        return text.replace(
            "is non-empty at this arena",
            "is empty at this arena too")
    if kind == "MUT-WALL" and mut("MUT-WALL"):
        return text + "\n\n" + PARAPHRASE_PLANTS[0][1] + "\n"
    if kind == "MUT-SPELLED" and mut("MUT-SPELLED"):
        return text + ("\n\nThe sharpened floor reproduces the certified "
                       "floor at two of four arities.\n")
    return text


def closing_battery(src, paper_text, paper_rel, write):
    CL = Claims()
    RR = ReferentRegistry()
    register_claims(R, CL)
    register_referents(R, RR)

    segs, segfields = verdict_segments(R, with_fields=True)
    if mut("MUT-HEAD"):
        segs[0] = segs[0][:-1] + " FORGED 424242>"
    audit = head_audit(R, segs, segfields)
    CR.measured("head_segments", len(segs), "segments emitted, counted")
    CR.measured("head_findings", len(audit["findings"]), "counted")
    CR.measured("head_numerals", audit["numerals_in_the_head"], "counted")
    CR.measured("head_fields", audit["fields_declared"], "counted")
    LD.gate("G-VERDICT-EQUALITY", not audit["findings"],
            CR.stmt("the head's {s} segments carry {n} numerals in {d} "
                    "declared positional fields, and a comparator that "
                    "shares no code and no typed literal with the builder "
                    "matches every numeral against the field standing at "
                    "THAT position, re-derives each field's value from the "
                    "receipt's own row lists, and re-decides the word "
                    "tallies under both readings without calling the "
                    "decision procedure; the disagreements number {f}",
                    s="head_segments", n="head_numerals", d="head_fields",
                    f="head_findings"),
            audit)
    R["verdict"] = SEAL.seal("verdict", {"segments": segs, "audit": audit},
                             "G-VERDICT-EQUALITY")

    cg = CL.gate(paper_under("MUT-CLAIM", paper_text))
    obj = {"path": os.path.relpath(os.path.abspath(paper_rel), REPO),
           "sha256_12": hashlib.sha256(
               paper_text.encode("utf-8")).hexdigest()[:12],
           "characters": len(paper_text)}
    R["object_under_test"] = SEAL.seal("object_under_test", obj,
                                       "G-PAPER-CLAIMS")
    cg = dict(cg)
    cg["object_under_test"] = obj
    CR.measured("tables_claimed", cg["tables_claimed"], "counted")
    CR.measured("tables_in_paper", cg["tables_in_paper"], "counted")
    CR.measured("prose_claims", cg["prose_claims"], "counted")
    LD.gate("G-PAPER-CLAIMS",
            not cg["tables_missing"] and not cg["tables_unclaimed"]
            and not cg["fence_missing"] and not cg["fence_stray"]
            and not cg["prose_bad"],
            CR.stmt("{t} tables are rendered from the receipt and matched "
                    "against the {p} the paper carries, keyed by table and "
                    "in BOTH directions; the verdict fences are compared "
                    "by multiset equality; and {c} prose claims are "
                    "required at exact occurrence counts",
                    t="tables_claimed", p="tables_in_paper",
                    c="prose_claims"),
            cg)

    cov = paper_coverage(R, paper_under("MUT-COVER", paper_text))
    CR.measured("numerals_scanned", cov["numerals_scanned"], "counted")
    CR.measured("uncovered", len(cov["uncovered"]), "counted")
    LD.gate("G-PAPER-COVERAGE",
            not cov["uncovered"] and not cov["strips_never_used"],
            CR.stmt("every numeral in the paper is scanned -- fenced "
                    "blocks, table cells and verdict blocks included -- "
                    "and each must appear in the receipt or fall under a "
                    "declared structural exemption that is required to be "
                    "used: {n} numerals scanned, {u} uncovered",
                    n="numerals_scanned", u="uncovered"),
            cov)

    ref = RR.gate(paper_under("MUT-REFERENT", paper_text), COVERAGE_STRIPS)
    CR.measured("ref_sentences", ref["sentences_checked"], "counted")
    CR.measured("ref_violations", len(ref["violations"]), "counted")
    LD.gate("G-PAPER-REFERENTS", not ref["violations"],
            CR.stmt("{s} prose sentences select a declared universe by "
                    "their subject noun and every numeral in each is "
                    "resolved against THAT universe only, per occurrence, "
                    "fenced blocks stripped first; an A-of-B fraction must "
                    "be a pair the run measured, reflexive pairs refused "
                    "without a totality qualifier. Violations: {v}",
                    s="ref_sentences", v="ref_violations"),
            ref)
    R["referents"] = SEAL.seal("referents", RR.seal_value(),
                               "G-PAPER-REFERENTS")

    spc = paper_spelled(R, paper_under("MUT-SPELLED", paper_text), RR,
                        spelled_claims(R))
    CR.measured("spelled_sentences", spc["spelled_sentences_checked"],
                "counted")
    CR.measured("spelled_claims", spc["spelled_claims"], "counted")
    LD.gate("G-PAPER-SPELLED",
            not spc["universe_violations"] and not spc["claim_violations"]
            and not spc["inversion_violations"],
            CR.stmt("the same prose is scanned again in the OTHER "
                    "ALPHABET: every spelled cardinal is rewritten to its "
                    "digits and bound exactly as a written numeral is -- "
                    "{s} sentences resolved against their own universes -- "
                    "and the {c} sentences this run renders with a spelled "
                    "numeral are required verbatim with the form their own "
                    "inversion would take required to be absent",
                    s="spelled_sentences", c="spelled_claims"),
            spc)

    pol = paper_polarity(R, paper_under("MUT-POLARITY", paper_text))
    CR.measured("polarity_claims", pol["claims"], "counted")
    LD.gate("G-PAPER-POLARITY", not pol["violations"],
            CR.stmt("{k} direction-bearing claims are bound to measured "
                    "booleans rather than to numerals, both halves at "
                    "once: the true direction present and the false "
                    "direction absent",
                    k="polarity_claims"),
            pol)

    # THE WALL BATTERY IS MEMOISED ON THE SCANNED TEXT'S OWN DIGEST (the
    # AUTOGLUE runtime lesson: the plants-by-walls-by-negated-twins product
    # is the chain's dominant cost, and every nested falsifier run whose
    # paper variant is byte-identical to the clean one is served the same
    # result rather than recomputing the product).  The key carries the
    # text digest and the one mutant flag that changes the plant list, so
    # a corrupted variant can never be served the clean answer.
    wtext = ReferentRegistry.prose_only(paper_under("MUT-WALL", paper_text))

    def _wall_battery():
        walls_l = build_walls()
        wres_l = []
        for w in walls_l:
            r = w.scan(wtext)
            ctl = []
            for c in w.controls:
                for suffix in ("", ", and that is not in doubt"):
                    rr = w.scan(wtext + "\n\n" + c[:-1] + suffix + ".")
                    ctl.append(bool(rr["violations"])
                               or bool(rr["unlicensed_sentences"]))
            wres_l.append({"wall": w.name, "violations": r["violations"],
                           "missing_positive": r["missing_positive"],
                           "unlicensed_sentences": r["unlicensed_sentences"],
                           "independent_controls": len(w.controls) * 2,
                           "declared_controls": len(w.controls),
                           "controls_caught": sum(1 for x in ctl if x),
                           "has_a_licence_leg": bool(w.subject
                                                     and w.policed),
                           "seal": w.seal_value()})
        empty_l = []
        for w in walls_l:
            try:
                w.scan("")
                empty_l.append(w.name)
            except GateFail:
                pass
        plants_l = []
        for nm, sent in (PARAPHRASE_PLANTS[:-1]
                         + [("P-INERT", "The table above.")]
                         if mut("MUT-PLANT") else PARAPHRASE_PLANTS):
            caught, caught_negated = [], []
            for w in walls_l:
                rr = w.scan(wtext + "\n\n" + sent + "\n")
                if rr["violations"] or rr["unlicensed_sentences"]:
                    caught.append(w.name)
                rn = w.scan(wtext + "\n\n" + sent[:-1]
                            + ", and this is not a small point.\n")
                if rn["violations"] or rn["unlicensed_sentences"]:
                    caught_negated.append(w.name)
            plants_l.append({"plant": nm, "sentence": sent,
                             "caught_by": caught,
                             "caught_by_when_negated": caught_negated})
        return wres_l, empty_l, plants_l

    wres, empty_ok, plants = memo(
        ("wallbattery", bytes_digest(wtext.encode("utf-8")),
         mut("MUT-PLANT")), _wall_battery)
    CR.measured("n_walls", len(wres), "counted")
    CR.measured("n_controls", sum(r["declared_controls"] for r in wres),
                "counted")
    CR.measured("controls_caught", sum(r["controls_caught"] for r in wres),
                "counted")
    LD.gate("G-WALLS",
            all(not r["violations"] and not r["missing_positive"]
                and not r["unlicensed_sentences"] for r in wres)
            and all(r["controls_caught"] == r["independent_controls"]
                    for r in wres)
            and all(r["has_a_licence_leg"] for r in wres)
            and not empty_ok,
            CR.stmt("{w} reading walls -- the parent's eight and this "
                    "unit's own ninth, which polices the reading-merge -- "
                    "scan the paper as voice-normalised regexes, each with "
                    "a POSITIVE leg, a live licence leg and a NEG guard "
                    "with re-assertion and other-clause exclusions, each "
                    "non-vacuous on empty text; {c} controls are injected "
                    "twice each, negated twins included, and {k} are "
                    "caught",
                    w="n_walls", c="n_controls", k="controls_caught"),
            {"walls": wres, "walls_passing_on_empty_text": empty_ok})
    R["walls"] = SEAL.seal("walls", wres, "G-WALLS")

    CR.measured("n_plants", len(plants), "counted")
    CR.measured("plants_caught",
                sum(1 for p in plants if p["caught_by"]), "counted")
    LD.gate("G-WALL-PARAPHRASE",
            all(p["caught_by"] for p in plants)
            and all(p["caught_by_when_negated"] for p in plants)
            and len(plants) >= PARAPHRASE_FLOOR,
            CR.stmt("{k} paraphrases of the banned claims, each written "
                    "against the disease rather than against a pattern, "
                    "are planted in the paper and run through the whole "
                    "wall set twice each, negated twins included: {c} are "
                    "caught. A wall that only matches the sentences its "
                    "own patterns were written from is not a wall",
                    k="n_plants", c="plants_caught"),
            {"plants": plants})
    R["paraphrase_plants"] = SEAL.seal("paraphrase_plants", plants,
                                       "G-WALL-PARAPHRASE")

    def _audit_self():
        got = CR.audit_module(open(SELF).read(),
                              ("stmt", "claim", "table", "fence",
                               "measured"))
        return got, sorted(CR.names_used)
    offenders, _names = memo(("astaudit",), _audit_self)
    CR.names_used.update(_names)
    if mut("MUT-TYPED"):
        offenders = offenders + [{"caller": "stmt", "typed": "424242",
                                  "line": 0}]
    fl = memo(("astfloat",), lambda: ast_float_scan(open(SELF).read()))
    CR.measured("measured_names", len(CR.vals), "counted")
    CR.measured("typed_offenders", len(offenders), "counted")
    unused_names = sorted(pat for pat, _w in CR.NAME_STRIPS
                          if pat not in CR.names_used)
    LD.gate("G-NO-TYPED-COUNTS", not offenders and not fl
            and not unused_names,
            CR.stmt("{m} values enter the published statements by NAME "
                    "from the live registry, and an AST leg scans this "
                    "module for numerals typed into a vouching call -- the "
                    "%-format and integer-offset subspecies included -- "
                    "finding {o}; the same scan finds no float constant "
                    "anywhere in the source",
                    m="measured_names", o="typed_offenders"),
            {"offenders": offenders[:8], "float_literals": fl[:8],
             "exempt_tokens": CR.exempt,
             "declared_name_strips": {p: w for p, w in CR.NAME_STRIPS},
             "name_strips_never_used": unused_names})

    own_hash = memo(("asthash", mut("MUT-HASH")),
                    lambda: hash_ban_scan(open(SELF).read()))
    rehearsal = _probe_hash() if not mut("MUT-HASH") else hash_ban_scan(
        "x = hash(y)\nz = id(w)\n")
    CR.measured("hash_calls_found", len(own_hash), "counted")
    CR.measured("hash_rehearsal_catches", len(rehearsal), "counted")
    LD.gate("G-HASH-BAN",
            not own_hash and len(rehearsal) == 2,
            CR.stmt("the builtin hash and the builtin id are BANNED by an "
                    "AST leg -- both are per-process accidents under "
                    "PYTHONHASHSEED and the allocator, and a receipt that "
                    "consumed either would be seed-dependent: {h} calls "
                    "found in this module, and the scanner is rehearsed on "
                    "a planted sample carrying both, catching {r}",
                    h="hash_calls_found", r="hash_rehearsal_catches"),
            {"calls_in_module": own_hash, "rehearsal": rehearsal})

    if mut("MUT-CACHE"):
        MEMO_HITS[("hit", "flagless")] += 1
    fam = Counter()
    for (kind, name), c in MEMO_HITS.items():
        fam[(name, kind)] += c
    cache = {"entries": len(MEMO),
             "families": sorted({n for (n, _k) in fam}, key=repr),
             "misses": sum(c for (_n, k), c in fam.items() if k == "miss"),
             "hits": sum(c for (_n, k), c in fam.items() if k == "hit"),
             "families_never_missed": sorted(
                 ({n for (n, k) in fam if k == "hit"}
                  - {n for (n, k) in fam if k == "miss"}), key=repr)}
    CR.measured("cache_entries", cache["entries"], "counted")
    CR.measured("cache_misses", cache["misses"], "counted")
    CR.measured("cache_hits", cache["hits"], "counted")
    LD.gate("G-CACHE",
            not cache["families_never_missed"] and cache["misses"] > 0
            and cache["hits"] > 0,
            CR.stmt("the run memoises {e} deterministic computations, "
                    "every key carrying the mutant flags its value depends "
                    "on, so a recipe is never served a clean cached "
                    "answer; the lookup path is exercised {h} times and "
                    "the compute path {m}, and no family is served only "
                    "from the cache",
                    e="cache_entries", h="cache_hits", m="cache_misses"),
            cache)
    R["cache"] = SEAL.seal("cache", cache, "G-CACHE")

    if mut("MUT-EXACT"):
        R["cache"] = {"planted": len(MEMO) / len(ARITIES)}
    bad = exact_scan(R)
    LD.gate("G-EXACT", not bad,
            CR.stmt("a recursive type walk of the whole receipt finds no "
                    "float anywhere: every quantity this unit publishes is "
                    "an integer, a string or a boolean"),
            {"float_paths": bad[:8]})

    if not IN_FALSIFIER:
        frows = run_falsifiers(paper_text, paper_rel)
        gates = set(GATE_ORDER)
        sent = [r for r in frows if r["target_moved"] is False]
        wrong = [r for r in frows if r["died_at"] != r["declared_gate"]]
        unreached = [r for r in frows if r["declared_gate"] not in gates]
        covered = {r["declared_gate"] for r in frows}
        uncovered = coverage_forcing(gates, covered, WAIVERS)
        forced = coverage_forcing(gates | {"G-NO-SUCH-GATE"}, covered,
                                  WAIVERS)
        forcing_ok = forced == sorted(uncovered + ["G-NO-SUCH-GATE"])
        CR.measured("n_falsifiers", len(frows), "counted")
        CR.measured("n_sentinels", len(sent), "counted")
        CR.measured("n_wrong_gate", len(wrong), "counted")
        CR.measured("n_uncovered", len(uncovered), "counted")
        CR.measured("n_waivers", len(WAIVERS), "counted")
        LD.gate("G-FALSIFIERS",
                not sent and not wrong and not unreached
                and not uncovered and forcing_ok,
                CR.stmt("{n} falsifiers each name the measured object "
                        "their recipe must MOVE, and the harness digests "
                        "that object before and after: sentinels {s}, "
                        "wrong-gate deaths {w}, gates with no recipe and "
                        "no waiver {u} -- IN the predicate -- with {v} "
                        "waivers written down and the coverage rule forced "
                        "on a gate no recipe names",
                        n="n_falsifiers", s="n_sentinels", w="n_wrong_gate",
                        u="n_uncovered", v="n_waivers"),
                {"rows": frows, "gates_with_no_falsifier": uncovered,
                 "declared_gates": len(GATE_ORDER),
                 "waivers": WAIVERS, "coverage_rule_forced": forcing_ok,
                 "falsifiers_dying_elsewhere":
                     [r["falsifier"] for r in wrong],
                 "falsifiers_moving_nothing":
                     [r["falsifier"] for r in sent]})
        R["falsifiers"] = SEAL.seal("falsifiers", frows, "G-FALSIFIERS")
    else:
        SEAL.declare_unsealed(
            "falsifiers", "not run inside a falsifier's own nested run")
        R["falsifiers"] = []

    pg = preregistration_gate(R, segs)
    CR.measured("prereg_words", len(pg["declared_words"]), "counted")
    CR.measured("prereg_segments", len(pg["segments"]), "counted")
    CR.measured("prereg_contingent", pg["segments_contingent"], "counted")
    CR.measured("prereg_reasoned", len(pg["never_fired_with_reasons"]),
                "declared words that did not fire, each with its measured "
                "reason")
    LD.gate("G-PREREGISTRATION",
            not pg["emitted_but_never_declared"]
            and not pg["unreasoned_never_fired"]
            and not pg["segments_unbound"] and pg["digests_match"],
            CR.stmt("the pre-registration is CONSUMED and not decorated: "
                    "both registers carry their own digest, checked here; "
                    "every emitted outcome word is declared; every "
                    "declared word either fires or stands in the register "
                    "of measured non-occurrences, which holds {nr} words "
                    "each carrying the measurement that kept its trigger "
                    "from occurring; and each of the {g} head segments "
                    "carries its pre-registered outcome, the complement, a "
                    "feasibility line and the honest contingency column, "
                    "true of {c}",
                    nr="prereg_reasoned", g="prereg_segments",
                    c="prereg_contingent"),
            pg)
    R["preregistration"] = SEAL.seal("preregistration", pg,
                                     "G-PREREGISTRATION")

    reh = _probe_promotion()
    CR.measured("promotion_legs", len(reh), "counted")
    LD.gate("G-PROMOTION-REHEARSAL", all(reh),
            CR.stmt("the {k} legs that stand between the last gate and "
                    "the written artifacts are REHEARSED on fixed "
                    "synthetic inputs: a forged narrative line must be "
                    "refused and a sealed value edited after its gate must "
                    "be refused, and the promotion path calls these same "
                    "two functions before it replaces anything",
                    k="promotion_legs"),
            {"narrative_binding_refuses_a_forged_line": reh[0],
             "seal_check_refuses_an_edited_value": reh[1]})

    if mut("MUT-READ"):
        _undeclared_read()
    declared = [rel for (_i, rel, _s, _w) in SOURCES] + [
        os.path.relpath(os.path.abspath(paper_rel), REPO)]
    RS.exempt(os.path.relpath(SELF, REPO),
              "this module's own source, read by the AST scans")
    rs = RS.gate_at_close(declared)
    CR.measured("declared_reads", len(declared), "counted")
    LD.gate("G-READ-SET",
            not rs["undeclared"] and not rs["declared_never_read"]
            and not rs["unused_exemptions"] and not rs["external_reads"],
            CR.stmt("every open this process performed is recorded at the "
                    "I/O accessor by an audit hook, wherever the path lies "
                    "-- reads outside the repository go to their own "
                    "bucket, which must be empty -- and the multiset of "
                    "paths is compared against the {d} declared inputs "
                    "plus exemptions that must be used; the same "
                    "comparison is made AGAIN inside the promotion path",
                    d="declared_reads"),
            rs)
    R["read_set"] = SEAL.seal("read_set", rs, "G-READ-SET")
    global DECLARED_READS
    DECLARED_READS = list(declared)

    R["totals"] = SEAL.seal(
        "totals", {"gates": len(GATE_ORDER),
                   "sources": len(SOURCES),
                   "path_anchors": len(PATH_ANCHORS),
                   "verbatim_anchors": len(VERBATIM),
                   "arities": len(ARITIES),
                   "falsifiers": len(FALSIFIERS)}, "G-READ-SET")

    if mut("MUT-ANCHOR-USE"):
        AN.anchors[VERBATIM[0][0]].consumer = "G-DOES-NOT-EXIST"
    ac = AN.verify_consumption(LD)
    CR.measured("anchor_reads", len(AN.reads), "recorded at the accessor")
    LD.gate("G-ANCHORS-CONSUMED", not ac,
            CR.stmt("anchor text is readable only through an accessor that "
                    "records the read, and every anchor's declared "
                    "consumer must be a gate that RAN and that actually "
                    "read it: {r} reads were recorded",
                    r="anchor_reads"),
            {"reads": sorted(set(AN.reads)), "unconsumed": ac})
    R["anchors"] = SEAL.seal(
        "anchors",
        [{"id": nm, "source": sid, "consumer": cons, "why": why,
          "chars": len(canon(needle))}
         for (nm, sid, needle, cons, why) in VERBATIM],
        "G-ANCHORS-CONSUMED")

    fam = {}
    for name, (gate, key) in sorted(TEMPLATE_FAMILIES.items()):
        if IN_FALSIFIER and gate == "G-FALSIFIERS":
            continue
        row = [r for r in LD.rows if r["gate"] == gate]
        fam[name] = {"gate": gate, "ran": bool(row),
                     "evidence_key_present": bool(
                         row and key in Ledger.evidence_line(
                             row[0]["evidence"]))}
    if mut("MUT-TEMPLATE"):
        fam = {}
    CR.measured("n_families", len(fam), "counted")
    want_fam = len(TEMPLATE_FAMILIES) - (1 if IN_FALSIFIER else 0)
    LD.gate("G-TEMPLATE-EXERCISED",
            len(fam) == want_fam
            and all(v["ran"] and v["evidence_key_present"]
                    for v in fam.values()),
            CR.stmt("each of the {k} template families names the gate that "
                    "EXERCISES it on this unit's own objects, and every "
                    "one of those gates must have run and carried its "
                    "family's own evidence",
                    k="n_families"),
            {"families": fam, "families_expected": want_fam})

    payload = dict(R)
    if mut("MUT-SEAL-ADD"):
        payload["forged_finding"] = {"headline": "everything transports"}
    if mut("MUT-SEAL-EDIT"):
        payload["fidelity"] = dict(payload["fidelity"])
        payload["fidelity"]["agree"] = payload["fidelity"]["rows"] + 1
    SEAL.declare_unsealed("ledger", "the chained ledger is verified by "
                                    "recomputing its own chain from the "
                                    "published rows, which carry every "
                                    "field the row digest is taken over")
    payload["transcript_head"] = None
    SEAL.declare_unsealed("transcript_head",
                          "the digest of the FINAL transcript bytes, "
                          "taken in the promotion path after the last "
                          "gate row and the verdict are written")
    SEAL.declare_unsealed("ledger_head", "the chain head, recomputed from "
                                         "the receipt's own rows AFTER "
                                         "the last gate")
    try:
        SEAL.verify_at_promotion(payload, LD, "seal_manifest")
        totality = True
        detail = "ok"
    except GateFail as e:
        totality = False
        detail = str(e)
    LD.gate("G-SEAL-TOTALITY", totality,
            CR.stmt("every sealed value is compared at the door against "
                    "the digest taken WHEN ITS GATE PASSED; totality is "
                    "recomputed from the payload's LIVE key set; every "
                    "seal's declared gate must be a gate that ran; and no "
                    "key is both sealed and declared unsealed"),
            {"sealed": len(SEAL.seals),
             "declared_unsealed": len(SEAL.unsealed), "detail": detail})

    fired = sorted(set(LD.names()) | {"G-CLOSE"})
    expect = sorted(g for g in _probe_close()
                    if not (IN_FALSIFIER and g == "G-FALSIFIERS"))
    LD.gate("G-CLOSE", fired == expect,
            CR.stmt("the gates this run fired are exactly the gates it "
                    "declares, counted with this gate inside its own "
                    "denominator; the ledger, its chain and the "
                    "transcript digest are all built after this row"),
            {"fired": len(fired), "declared": len(expect),
             "missing": [g for g in expect if g not in fired],
             "stray": [g for g in fired if g not in expect]})

    payload["ledger"] = [{k: r[k] for k in ("n", "gate", "statement",
                                            "passed", "evidence", "prev",
                                            "row_digest")}
                         for r in LD.rows]
    payload["ledger_head"] = LD.recompute_chain()
    return payload, segs


def preregistration_gate(rec, segments):
    """the register consumed four ways, with clause (iii) implemented in
    full: a declared word that never fired must stand in the register of
    measured non-occurrences, each entry carrying the measurement that
    kept its trigger from occurring."""
    declared = {w for (w, _m, _f) in PREREGISTERED}
    emitted = set()
    for reading in READINGS:
        for row in (rec["transport"][
                "linear" if reading == "F4-LINEAR" else "abstract"]
                ["statements"]
                + rec["transport"][
                    "linear" if reading == "F4-LINEAR" else "abstract"]
                ["numerals"]):
            emitted.add(row["word"])
            for (_a, stamp) in row["evidence"].get("carried_rows", []):
                emitted.add(stamp)
    emitted.add(rec["law3_menu"]["stamp"].split(":")[0].strip())
    for r in rec["law4_ladder"]["rows"]:
        if r["witness_status"] == "NOT-FOUND-WITHIN-CAP":
            emitted.add("NOT-FOUND-WITHIN-CAP")
    for r in rec["corpus"]:
        if r["refusal"]:
            emitted.add(r["refusal"]["stamp"])
    emitted.add(rec["conditional"]["verdict"])
    emitted.add(rec["conditional"]["f4_branch"])
    emitted.add(rec["modulus_theorem"]["verdict"])
    if rec["transport"]["split_statements"] or rec["transport"][
            "split_numerals"]:
        emitted.add("A16-TRANSPORT-READING-RELATIVE")
    never = sorted(declared - emitted)
    # THE MEASURED NON-OCCURRENCES, rendered from the data they cite.
    reasons = {}
    lin_words = Counter(r["word"] for r in rec["transport"]["linear"]
                        ["numerals"])
    abs_words = Counter(r["word"] for r in rec["transport"]["abstract"]
                        ["numerals"])
    if lin_words.get("NEEDS-3", 0) == 0 and abs_words.get(
            "NEEDS-3", 0) == 0:
        reasons["NEEDS-3"] = (
            "no numeral column is constant at the parent's value under "
            "either reading: the menu census reads %d against the "
            "parent's %d and the found rung reads %d against the "
            "parent's %d, so the word's trigger did not occur"
            % (rec["law3_menu"]["survivors"],
               [r["parent_value"] for r in rec["transport"]["linear"]
                ["numerals"] if r["law"] == "menu"][0],
               rec["modulus_theorem"]["found_rungs"][0][1],
               [r["parent_value"] for r in rec["transport"]["linear"]
                ["numerals"] if r["law"] == "ladder"][0]))
    if all(f[1] % 4 == 0 for f in rec["modulus_theorem"]["found_rungs"]):
        reasons["A16-MODULUS-THEOREM-FALSIFIED-AT-AG(2, 4)"] = (
            "every found rung is a multiple of the declared link count "
            "and mod-a appears only at a = L, so the falsifying trigger "
            "did not occur at any of the %d found rows"
            % len(rec["modulus_theorem"]["found_rungs"]))
    unreasoned = sorted(w for w in never if w not in reasons)
    undeclared = sorted(emitted - declared)
    seg_rows = []
    for i, (sid, word, comp, contingent, why) in enumerate(SEGMENT_PREREG):
        text = segments[i] if i < len(segments) else ""
        seg_rows.append({"segment": sid, "index": i,
                         "preregistered_outcome": word,
                         "complement": comp,
                         "outcome_present": word in text,
                         "complement_absent": comp not in text,
                         "contingent": contingent,
                         "feasibility": why})
    seg_bad = [r for r in seg_rows
               if not r["outcome_present"] or not r["complement_absent"]]
    dg1 = digest([list(t) for t in PREREGISTERED])
    dg2 = digest([list(t) for t in SEGMENT_PREREG])
    if mut("MUT-PREREG"):
        dg1 = "MOVED"
    return {"declared_words": sorted(declared),
            "emitted_words": sorted(emitted),
            "emitted_but_never_declared": undeclared,
            "never_fired_with_reasons": {k: v for k, v in
                                         sorted(reasons.items())
                                         if k in never},
            "unreasoned_never_fired": unreasoned,
            "segments": seg_rows, "segments_unbound": seg_bad,
            "segments_contingent": sum(1 for r in seg_rows
                                       if r["contingent"]),
            "outcome_register_digest": dg1,
            "segment_register_digest": dg2,
            "digests_match": (dg1 == PREREG_DIGEST
                              and dg2 == SEGMENT_PREREG_DIGEST)}


def promote(payload, segs, paper_text, write, declared_reads=()):
    """verify, then replace, and roll back if anything refuses."""
    body = dict(payload)
    TR.say("")
    TR.say("VERDICT")
    for s in segs:
        TR.say(s)
    TR.say("")
    TR.say("object under test %s %s"
           % (payload["object_under_test"]["path"],
              payload["object_under_test"]["sha256_12"]))
    TR.say("ledger head %s" % payload["ledger_head"])
    ttxt = TR.text().encode("utf-8")
    body["transcript_head"] = TR.bind(LD)
    allowed = {"ARITY-16 (paper-50) -- the second-arena unit", "VERDICT"}
    allowed |= set(segs)
    allowed.add("object under test %s %s"
                % (payload["object_under_test"]["path"],
                   payload["object_under_test"]["sha256_12"]))
    allowed.add("ledger head %s" % payload["ledger_head"])
    TR.bind_narrative(TR.text(), allowed)
    SEAL.verify_at_promotion(body, LD, "seal_manifest")
    body["seal_manifest"] = SEAL.manifest()
    blob = json.dumps(body, sort_keys=True, indent=1,
                      ensure_ascii=False).encode("utf-8")
    SEAL.verify_at_promotion(json.loads(blob.decode("utf-8")), LD,
                             "seal_manifest")
    rs2 = RS.gate_at_close(list(declared_reads))
    if rs2["undeclared"] or rs2["external_reads"]:
        raise GateFail("G-READ-SET :: undeclared read in the promotion "
                       "window: %s %s" % (rs2["undeclared"],
                                          rs2["external_reads"]))
    if not write:
        return {"receipt": bytes_digest(blob),
                "transcript": bytes_digest(ttxt)}
    prev = {}
    for pth in (OUT_JSON, OUT_TXT):
        if os.path.exists(pth):
            with open(pth, "rb") as fh:
                prev[pth] = fh.read()
    tmp_r, tmp_t = OUT_JSON + ".tmp", OUT_TXT + ".tmp"
    replaced = False
    try:
        with open(tmp_r, "wb") as fh:
            fh.write(blob)
        with open(tmp_t, "wb") as fh:
            fh.write(ttxt)
        with open(tmp_r, "rb") as fh:
            back_r = fh.read()
        with open(tmp_t, "rb") as fh:
            back_t = fh.read()
        if back_r != blob or back_t != ttxt:
            raise GateFail("G-CLOSE :: staged bytes differ from the "
                           "sealed render")
        SEAL.verify_after_promotion(tmp_r, "seal_manifest")
        os.replace(tmp_r, OUT_JSON)
        os.replace(tmp_t, OUT_TXT)
        replaced = True
        SEAL.close()
        SEAL.verify_after_promotion(OUT_JSON, "seal_manifest")
    except BaseException:
        if replaced:
            for pth, was in prev.items():
                with open(pth, "wb") as fh:
                    fh.write(was)
            for pth in (OUT_JSON, OUT_TXT):
                if pth not in prev and os.path.exists(pth):
                    os.unlink(pth)
        raise
    finally:
        for pth in (tmp_r, tmp_t):
            if os.path.exists(pth):
                os.unlink(pth)
    return {"receipt": bytes_digest(blob), "transcript": bytes_digest(ttxt)}


def run_measurements(paper_text, paper_rel=PAPER_PATH, write=False,
                     break_anchor=None):
    reset_state()
    TR.say("ARITY-16 (paper-50) -- the second-arena unit")
    TR.say("")
    if mut("MUT-ANCHOR"):
        break_anchor = VERBATIM[0][0]
    try:
        src, prel, _w = full_run(paper_text, paper_rel, write, break_anchor)
    except GateFail as e:
        if str(e).startswith("T-ANCHOR-CONSUMED"):
            raise GateFail("G-VERBATIM :: " + str(e))
        raise
    payload, segs = closing_battery(src, paper_text, paper_rel, write)
    return payload, segs


def read_paper(path):
    if not os.path.exists(path) or os.path.isdir(path):
        raise CliError("the object under test does not exist: %s" % path)
    with open(path, "rb") as fh:
        txt = fh.read().decode("utf-8")
    if not txt.strip():
        raise CliError("the object under test is empty: %s" % path)
    return txt


def artifact_digests():
    out = {}
    for p in (OUT_JSON, OUT_TXT):
        if os.path.exists(p):
            with open(p, "rb") as fh:
                out[os.path.basename(p)] = bytes_digest(fh.read())
            RS.exempt(os.path.relpath(p, REPO),
                      "this unit's own emitted artifact, opened by a "
                      "non-writing run mode's tamper snapshot and by "
                      "nothing that measures")
    return out


GATE_ORDER = ["G-SOURCES", "G-PATH-ANCHORS", "G-VERBATIM", "G-ARENA16",
              "G-READINGS", "G-CONSTRUCTOR-FIDELITY", "G-FIDELITY-FIRST",
              "G-PACKING-EXTENDS16", "G-SUBSTRATE-CENSUS", "G-CORPUS-RULE",
              "G-LAW1-NAMING16", "G-LAW2-FLOOR-CERTIFICATE16",
              "G-LAW2-SCHEDULE16", "G-LAW2-SHARPENED16", "G-LAW3-MENU16",
              "G-LAW4-LADDER16", "G-MODULUS-THEOREM", "G-LAW5-FORCING16",
              "G-LAW6-SEC2-16", "G-PRINCIPLE-CENSUS16", "G-CONDITIONAL",
              "G-TRANSPORT-CONTROLS", "G-AGGREGATE16",
              "G-VERDICT-EQUALITY", "G-PAPER-CLAIMS", "G-PAPER-COVERAGE",
              "G-PAPER-REFERENTS", "G-PAPER-SPELLED", "G-PAPER-POLARITY",
              "G-WALLS", "G-WALL-PARAPHRASE", "G-NO-TYPED-COUNTS",
              "G-HASH-BAN", "G-CACHE", "G-EXACT", "G-FALSIFIERS",
              "G-PREREGISTRATION", "G-PROMOTION-REHEARSAL", "G-READ-SET",
              "G-ANCHORS-CONSUMED", "G-TEMPLATE-EXERCISED",
              "G-SEAL-TOTALITY", "G-CLOSE"]


def parse_args(argv):
    mode = {"action": None, "paper": PAPER_PATH,
            "mutant": None, "write": True}

    def setmode(name):
        if mode["action"] is not None and mode["action"] != name:
            raise CliError("two run modes requested: %r and %r"
                           % (mode["action"], name))
        mode["action"] = name
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--no-write":
            mode["write"] = False
        elif a == "--run":
            setmode("run")
        elif a == "--selftest":
            setmode("selftest")
            mode["write"] = False
        elif a == "--list-gates":
            setmode("list-gates")
            mode["write"] = False
        elif a == "--render":
            setmode("render")
            mode["write"] = False
        elif a == "--verify-paper":
            if i + 1 >= len(argv):
                raise CliError("--verify-paper needs a path")
            setmode("verify-paper")
            cand = os.path.abspath(argv[i + 1])
            if not cand.startswith(REPO + os.sep):
                raise CliError("--verify-paper takes a path inside the "
                               "repository; %r is outside it" % argv[i + 1])
            mode["paper"] = cand
            mode["write"] = False
            i += 1
        elif a == "--mutant":
            if i + 1 >= len(argv):
                raise CliError("--mutant needs a name")
            if mode["mutant"] is not None:
                raise CliError("--mutant given twice")
            mode["mutant"] = argv[i + 1]
            mode["write"] = False
            i += 1
        else:
            raise CliError("unknown flag %r" % a)
        i += 1
    if mode["action"] is None:
        mode["action"] = "run"
    if mode["mutant"] and mode["action"] != "run":
        raise CliError("--mutant cannot be combined with %r"
                       % mode["action"])
    return mode


def main(argv=None):
    global MUTANT, IN_FALSIFIER
    argv = sys.argv[1:] if argv is None else argv
    try:
        mode = parse_args(argv)
    except CliError as e:
        sys.stderr.write("CLI ERROR: %s\n" % e)
        return 2
    RS.install()

    if mode["action"] == "list-gates":
        for g in GATE_ORDER:
            print(g)
        print("gates %d" % len(GATE_ORDER))
        return 0

    try:
        paper = read_paper(mode["paper"])
    except CliError as e:
        sys.stderr.write("CLI ERROR: %s\n" % e)
        return 2

    if mode["action"] == "selftest":
        before = artifact_digests()
        try:
            run_measurements(paper, mode["paper"], write=False,
                             break_anchor=VERBATIM[2][0])
        except GateFail as e:
            after = artifact_digests()
            ok = before == after
            print("SELFTEST: refused at %s" % str(e).split(" :: ")[0])
            print("SELFTEST: artifacts unchanged: %s" % ok)
            return 0 if ok else 3
        print("SELFTEST: the corrupted anchor was NOT refused")
        return 3

    if mode["mutant"]:
        if mode["mutant"] not in [f.name for f in FALSIFIERS]:
            sys.stderr.write("CLI ERROR: unknown mutant %r\n"
                             % mode["mutant"])
            return 2
        before = artifact_digests()
        MUTANT = mode["mutant"]
        IN_FALSIFIER = True
        try:
            run_measurements(paper, mode["paper"], write=False)
        except GateFail as e:
            MUTANT = None
            IN_FALSIFIER = False
            after = artifact_digests()
            print("MUTANT %s died at %s" % (mode["mutant"],
                                            str(e).split(" :: ")[0]))
            print("MUTANT: artifacts unchanged: %s" % (before == after))
            return 1 if before == after else 3
        MUTANT = None
        IN_FALSIFIER = False
        print("MUTANT %s SURVIVED" % mode["mutant"])
        return 3

    if mode["action"] == "render":
        reset_state()
        TR.say("ARITY-16 (paper-50) -- the second-arena unit")
        TR.say("")
        full_run(paper, mode["paper"], False, None)
        segs = verdict_segments(R)
        CL = Claims()
        parts = register_claims(R, CL)
        for k in sorted(parts):
            print("<<%s>>" % k)
            print(parts[k])
            print()
        print("<<CLAIMS>>")
        for c in sorted(CL.prose):
            print(c)
        print()
        print("<<SPELLED>>")
        for c, inv in spelled_claims(R):
            print(c)
        print()
        print("<<FENCES>>")
        for s in segs:
            print("```")
            print(s)
            print("```")
        return 0

    try:
        payload, segs = run_measurements(paper, mode["paper"],
                                         mode["write"])
        dg = promote(payload, segs, paper, mode["write"], DECLARED_READS)
    except GateFail as e:
        sys.stderr.write("REFUSED: %s\n" % e)
        print(TR.text())
        return 1
    print(TR.text())
    print("VERDICT")
    for s in segs:
        print(s)
    print()
    print("gates %d  ledger head %s" % (len(LD.rows), LD.head))
    for k, v in sorted(dg.items()):
        print("%s %s" % (k, v))
    return 0


if __name__ == "__main__":
    sys.exit(main())
