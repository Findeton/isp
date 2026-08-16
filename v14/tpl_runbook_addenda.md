# DRAFTED RUNBOOK ADDENDA — the #267 template sweep

*TPL, chartered at v14 ledger #371 per #362.  **These are DRAFTS. Nothing
here has been applied. `RUNBOOK.md` was not edited by this worker** — the
orchestrator engraves.  Evidence: `v14/TEMPLATE.md`; exposure:
`v14/tpl_census.md`; mechanisms: `v14/code/era_template.py`.*

Numbering below assumes the next free engraving id is **E-25** (`RUNBOOK.md`
currently ends at E-24).  The orchestrator owns the numbering; if the four
pending engravings of §B are applied first, renumber accordingly.

Each draft is written in house style: the rule, then what bought it.  Every
"demonstrated at" clause below is a live injection that survived at exit 0 in
the cited review, not an inference.

---

## A. THE NINE FAMILIES

### E-25 — TOTALITY AND SEALS ARE RECOMPUTED AT THE DOOR (bought at v14 #371; convergent at SEC-2 K3 MAJOR-1, SPC K3 MAJOR-1, EPR K3 MAJOR-5, NDEP K3 MAJOR-1, POT K3 MAJOR-6, SEC K3 MAJOR-4)

A gate-time seal is worth what is checked against it AT PROMOTION.  Before
staging, every sealed key's digest is recompared with the digest taken when
its gate passed, and totality is RECOMPUTED from the payload's live key set —
never read off a snapshot taken when the totality gate fired.  The order is
stage → read back → verify → `os.replace` → re-verify from the promoted path:
an instrument that promotes first has a real gate firing after the damage is
done (SMU K3 MAJOR-3 refused at exit 1 and left both sandboxes holding
corrupted artifacts — "No `.tmp` was left in either, so there is no recovery
path either"), and staging temporaries are removed in a `finally` on every
exit that is not a successful promotion (POT K3 MAJOR-10).  A key a
measurement produced may not be moved to the unsealed side; a seal may not
name a gate that never ran.  Demonstrated in six units and measured in
twenty-one: at SEC-2 a value mutated inside a sealed key and an undeclared
key added, promoting a receipt whose own manifest publishes a digest that
does not match the value beside it; at SPC the paired injection that fixes
the window exactly (the same insertion dies before the totality computation
and ships after it); at NDEP a forged finding on disk while the transcript
reports "seals 34 over 35 published keys, missing none" about a file with 36;
at EPR a seal, already shipped, naming `G-TRANSCRIPT-SEALED-WHOLE`, a gate
that does not exist.  Supersedes nothing; completes #119 and its #148
addendum.  *(See §B.4 — this rule is already recorded as engraved at #348.)*

### E-26 — THE TRANSCRIPT IS BOUND TO THE LEDGER BY CONTENT (bought at v14 #371; convergent at SEC-2 K3 MAJOR-9, NDEP K3 MAJOR-2, EPR K3 MAJOR-6, POT K3 MAJOR-7, LOR K3 MAJOR-5, PERR K3 MAJOR-3)

The human-readable artifact is evidence only if it is reconciled with the
sealed one.  Every `[PASS]/[FAIL]` line is parsed back out of the text that
will be promoted and compared with the ledger's `(gate, passed, evidence)`
rows AS A MULTISET, both directions; the row count, the gate count, the
`--list-gates` output and any published total are ONE number, computed after
the last gate; and the WHOLE transcript, not a prefix, is digested at close
and compared with the promoted bytes.  Demonstrated: at SEC-2 a `PASS`→`FAIL`
edit, a forged measured number and a wholly invented gate row all survived,
and one run published four different gate counts (34 / 34 / 42 / 45); at NDEP
one line in the renderer made the transcript read `unique 99` where the
receipt read `unique 45` — the two published artifacts contradicting each
other on the unit's own headline census with nothing noticing; at LOR the
integrity check covered 40 of 221 lines; at EPR the "gate-time" transcript
seal was recomputed at promotion, so the comparison could not fail on
content.  **The census finds this mechanism in none of the thirty-nine
instruments; it is the family with no closed instance anywhere.**

### E-27 — WALLS ARE SEMANTIC, POSITIVE AND SELF-SEALING (bought at v14 #371; convergent at EPR K3 MAJOR-7, NDEP K3 MAJOR-6, LOR K3 MAJOR-1 + #269, POT K3 MAJOR-1/2, SEC-2 K3 MAJOR-10/11, U4 K3 MAJOR-1, U4b K3 MAJOR-6)

A wall is a family of voice-normalised patterns run case-folded against the
canonicalised paper (#125), never a list of literal strings; it carries a
POSITIVE leg requiring the paper to state its standing verdict; it FAILS on
empty or absent text; and a licence set may not contain the word it polices —
a policed sentence must carry a rendered CLAIM, not a token from a registry.
At least one positive control per wall is written by a different hand from
the pattern, phrased as a paper would phrase it.  Demonstrated: at EPR
"On the measured arms this restores local realism." passed a seven-string
blacklist, a Bell-evasion paraphrase passed, and the paper's own wall
sentence could be DELETED; at NDEP four of five natural violations passed,
"the positive control being the pattern's own sentence, so every probe fires
by construction"; at POT the two load-bearing words were simultaneously
policed and licensing, so "It confines." passed; at SEC-2 a negation
capitalised as a sentence opener was invisible; at LOR the three reading
walls never scanned the paper at all.  Carries LOR #269's caveat as an
obligation, not a footnote: a kill on the wrong leg is not evidence.

### E-28 — A VERBATIM ANCHOR IS CONSUMED OR IT IS DECORATION (bought at v14 #371; convergent at POT K3 MAJOR-9, NDEP K3 MAJOR-4, EPR K3 probe 6, ACT K3 MAJOR-3, SEC K3 MAJOR-5, SMU K3 MAJOR-1, R6b' K3 M3, R4b K3 MAJOR-2)

An anchor's text is readable only through one accessor that records who read
it, and a closing gate requires each anchor's DECLARED CONSUMER to have
actually read it; the consumer id must be a gate that ran; the needle must
occur exactly once, above the #62 floor, in the pinned source AND in the
paper's own rendering.  The consuming gate takes a value out of the located
text and compares it with a measurement — meaning, not existence.
Demonstrated: at POT "0 of 15 verbatim anchors are consumed by their named
gate", the container never subscripted anywhere in the file; at NDEP proven
by receipt-leaf diff — swapping a needle for a different true sentence from
the same parent moved three leaves and not one measured quantity; at ACT all
fifty-three consumer names rewritten to `G-DOES-NOT-EXIST` shipped at exit 0;
at SEC five block quotations inverted freely, including one inverting R1's
copy-forcing theorem; at R6b' the window preserved byte-for-byte and its
meaning inverted around it; at R4b a 138-byte window truncated to four bytes
with the artifacts byte-identical.

### E-29 — CLAIMS BY EQUALITY, IN BOTH DIRECTIONS, KEYED BY TABLE (bought at v14 #371; convergent at SEC-2 K3 MAJOR-3/4, EPR K3 MAJOR-1/2/3, POT K3 MAJOR-4/5, NDEP K3 MAJOR-5/9, SEC K3 MAJOR-1, LOR K3 MAJOR-2)

E-22 is discharged only by EQUALITY.  The licensed row multiset is keyed by
the table the row was rendered into, so a row transplanted between tables is
stray in one and missing in the other; headers are rows; `stray` tests
`got[k] > want[k]`, never `k not in want`; prose claims are gated at their
EXACT occurrence count computed from the licensed rendering, never floored at
one; fenced blocks are compared by multiset equality with declared
multiplicity, tokenised whatever the info string carries; and a markdown
table in the paper that no rendering claims is a FAILURE, not a silence.
Demonstrated: at SEC-2 two cross-table header swaps and two row transplants
at exit 0 — "the gate catches invented content and misses misplaced content"
— and, on the fence leg, a fabricated ninth fence passing AND the deletion of
the whole verdict block passing; at EPR the three verdict fences matched zero
times, so six head forgeries passed including the deletion of the paper's own
no-local-realism stamp; at POT one of three copies of "gap 1/2" became
"gap 1/4" and the paper stated two different gaps; at NDEP the whole §2.1
corpus table was bound by nothing; at SEC twelve forgeries at 37/37 exit 0,
including the unit's central result inverted.

### E-30 — REFERENT BINDING IS PER OCCURRENCE, OVER PROSE, AND PAIRED (bought at v14 #371; convergent at SEC-2 K3 MAJOR-12, SPC K3 MAJOR-2, NDEP K3 MAJOR-7, SEC K3 probe 9, FAC K3 MAJOR-2, POT K3 MAJOR-2)

A numeral is backed only against the universe its own sentence is about.
Universes are declared with their nouns, their values and THE PAIRS THE RUN
MEASURED; every occurrence is checked, never `any(...)` over the paper (#87
for prose); fenced blocks are stripped before the scan, so the run's own
machine-derived verdict fences cannot discharge the paper's obligations; an
"A of B" fraction must be a measured pair, not two members of one set; and a
digest whitelist is digest-SHAPED and declared, never a numeral that happens
to sit inside a hash.  Demonstrated: at SEC-2 "the kernel is 455" — a group
count used as a matrix kernel — over six live universes any of whose numerals
validated any other's sentence; at SPC "156 of 220 species", and the §4
headline contrast inverted from 2-of-30 to 30-of-30 and CARRIED THROUGH A
FULL DELIVERY at 46/46 gates passed with the corrupted paper's digest sealed
into the receipt; at NDEP four cross-universe plants passing byte-identically
because the bindings were satisfied inside the run's own fences; at SEC four
numerals from four universes composed into one sentence contradicting the
receipt on every clause.

### E-31 — NO TYPED COUNTS ANYWHERE THE UNIT VOUCHES (bought at v14 #371; the one realized harm — SEC-2 §4.2 at #362/#368; convergent at SEC-2 K3 MAJOR-13, LOR K3 MAJOR-3, EPR K3 MINOR-5, PERL K3 MAJOR-6, POT K3 MAJOR-3, ACT K3 MAJOR-5)

Every numeral in a published gate statement, claim template, head segment,
table header or testimony leaf is interpolated from a live registry, and a
value enters that registry only with its provenance — a constant that was
never measured may not be published as a measurement.  The prohibition is
checked on the TEMPLATE, before substitution, and again by an AST scan of the
module; declared exemptions (a paper id, an engraving id, a year) carry their
reason and must be used.  A number typed on both sides of a comparator is
invisible to the head reconstruction and is forbidden outright.  **This is
the only family in the sweep with a realized harm**: SEC-2's §4.2
declaration-fiber column was typed, and two of its values were false (27→24,
9→8), computed and corrected under the ordered exception and disclosed
in-paper — the era's only false delivered numerals.  Also demonstrated: at
SEC-2 `union_min = 1`, a typed constant carrying the whole of criterion 3; at
LOR three false published counts, typed, ungated and self-contradicted; at
EPR a sealed gate statement reading "Fifteen claims" beside its own evidence
field reading `claims 16`; at POT a numeral registry admitting all ten single
digits and all ninety two-digit tokens.  Registered residuals owed here:
PER-R's six claim templates (#353), EPR's two typed testimony leaves (#359),
SEC's 234 small structural numerals (#367).

### E-32 — A FALSIFIER MOVES THE MEASUREMENT OR IT IS NOT A FALSIFIER (bought at v14 #371; convergent at SEC-2 K3 MAJOR-6/7, NDEP K3 MAJOR-10, EPR K3 MAJOR-4, SEC K3 MAJOR-6, SMU K3 MAJOR-4, R4dec K3 MAJOR-4)

Each falsifier names the measured object its recipe must move; the harness
digests that object before and after and REFUSES a recipe that leaves it
identical — a constant boolean, a constant append, a forced comparison result
is a sentinel, not a falsifier, whatever its published description says.
Death must occur AT the declared gate and not earlier, or the waiver naming
it is untrue.  Descriptions are matched against code by AST (E-23's third
leg, which no unit was performing).  The coverage gate counts ITSELF: a gate
list snapshotted before the coverage gate appends itself is a self-exemption.
Waivers carry machine-checked forcings, not descriptions.  Demonstrated: at
SEC-2 six sentinel falsifiers — "they prove the gate raises when handed a
False, not that it detects the corruption it advertises" — leaving the
corpus's two most load-bearing instruments, the verdict comparator and the
paper renderer, with no falsifier that touches them, plus four gates with
neither falsifier nor waiver; at SEC five waivers whose named falsifier
provably dies at an EARLIER gate; at SMU fifteen of forty-two falsifiers
corrupting no object; at NDEP one description inverted and one falsifier
exempting the leg it should exercise.  Extends E-23; carries LOR #269's
caveat — a falsifier calibrated to the guard rather than to the threat makes
its green badge worthless (PERR K3 MAJOR-3, measured).

### E-33 — THE READ SET IS RECORDED WHERE READS HAPPEN (bought at v14 #371; convergent at SEC-2 K3 MAJOR-2/8, SEC K3 MAJOR-3, LOR K3 MAJOR-4, GAMMA-PREP K3 MAJOR-3, R3 K3 M1, R4b K3 MAJOR-4)

Reads are recorded at an `open` audit hook or an equivalent accessor that a
raw `open()` cannot bypass; the declared set is compared ORDER-INSENSITIVELY
at the LAST gate, not the first; exemptions are declared with reasons and
must be used, and a read log may not be silently popped; declared-but-never-
read fails too.  No declared mode passes vacuously: every mode requires its
object to exist and be non-empty, and a mode weaker than the delivery path is
a mode a reviewer is invited to be misled by.  Demonstrated: at SEC-2 the
pin's own prohibited file walked in by two routes of three, and
`--verify-paper` on an empty file printed PASS while all three walls passed
vacuously on `""`; at SEC the read list was built inside the loop over
SOURCES, so the comparison was true by construction and a read of the very
file the unit abstains from reported `violations: []`; at LOR the gate fired
second, before the object under test was read; at R3 an unanchored live
`v14/LOG.md` read moved a verdict segment and both artifact hashes.  Extends
#91 and #82.

---

## B. FOUR ENGRAVINGS ALREADY RECORDED IN THE LEDGER AND ABSENT FROM THE RUNBOOK

Measured at the time of this sweep: `RUNBOOK.md` was last modified at commit
`c3bd7b5`, v14 ledger **#192** (E-24), and a term search finds none of the
four texts below.  Each is drafted here in house style so one pass closes the
gap.  **The wording is the ledger's and the adjudications'; this worker did
not invent any of it.**

**B.1 — from #295 (PER-R adjudication), "THE CLASS-BINDING ENGRAVING."**
Recommended action: the orchestrator lifts the ruling's own sentence from
`v14/note-perr-adjudication.md` verbatim.  Recorded here only as an owed
item; TPL did not draft a wording it could not source verbatim.

**B.2 — from #299 (ACT adjudication), the reachable-outcomes engraving.**
Ledger text: *"every pre-registered outcome word must be shown reachable at
the declared arena by a feasibility line in the pin."*  Bought by ACT's
selector, pigeonhole-decided before the run, with the PIN OWNED — FORCED
pre-registered though unreachable.  Reinforced independently by GITER K3
MAJOR-1 ("a deviation here would have looked like a refused run, not like a
located deviation"), SIG K3 MAJOR-6 ("'45 of 45 gates PASS' is not evidence
for the verdict, because the gates encode it") and GMAIN K3 M8 ("the clean
36/36 sheet is contingent on the verdict coming out PARTIAL").

**B.3 — from #319 (FAC adjudication), the pin's feasibility engraving
sharpened.**  Recommended action: lift from
`v14/note-fac-adjudication.md` verbatim, as the sharpening of B.2.

**B.4 — from #348 (POT + SPC adjudication), two items.**  (i) The #299
row-list extension: *"a compounded head whose words aggregate a declared row
list must show feasibility at the list"* (`v14/note-spc-adjudication.md` §7).
(ii) The #119 promotion-totality addendum, stated in terms at
`v14/note-spc-adjudication.md` §9: **"A SEAL MANIFEST IS TOTAL ONLY IF
TOTALITY IS RECOMPUTED AT PROMOTION TIME."**  Item (ii) is the same rule as
**E-25** above; if E-25 is engraved, (ii) is discharged and should be
recorded as such rather than engraved twice.

---

## C. REGISTERED SUCCESSORS — NOT DRAFTED AS ENGRAVINGS

The sweep found three shapes at least as recurrent as the nine and outside
all of them.  They are not drafted here because the charter named nine and
because each needs a mechanism before it needs a rule — the same order this
sweep followed.  Full evidence at `v14/TEMPLATE.md` §11.

- **S-1 THE COMPARATOR IS THE BUILDER** — sixteen units, including R2 M1
  ("the rebuild is the same function on the same payload... INJ16 settles the
  question of how much the gate knows about the measurement: nothing"), R5
  MAJOR-2 ("the segment renderer does not exist"), R3w M1 (71.2 % of the head
  rebuilt by the builder's own function), NDEP MAJOR-3 (the comparator
  catches 2 of 22).  RUNBOOK carries the #82 comparator-independence clause
  already; what is missing is a mechanism and a test.
- **S-2 TWO "INDEPENDENT ROUTES" THROUGH ONE COMPONENT** — R6a M2, R3 M2
  (zeroing the column both routes share leaves the two-route gate green),
  OCC MAJOR-3, R1 M1, R2 M3, R6b' M10, SIG MINOR-1.
- **S-3 THE PRE-REGISTERED OUTCOME IS UNREACHABLE** — already owed as an
  engraving at #299; see B.2.

Two further shapes extend a family rather than found one, and are already
folded into the drafts above: *write-before-verify / no rollback* (promotion
ORDER — SMU MAJOR-3 promotes both corrupted artifacts with no `.tmp` left,
hence no recovery path; folded into E-25) and *the sealed self-description
that is false* (E-23's duty applied to gate statements and sealed warrants
rather than to falsifiers — PERR MAJOR-7, "a sealed vouching row carrying two
false statements"; folded into E-31 and E-32).

---

## D. WHAT THE ORCHESTRATOR SHOULD DECIDE

1. Whether to engrave A as E-25…E-33, or to fold the nine into fewer rules.
2. Whether B.1–B.4 are engraved from their adjudications verbatim, and
   whether E-25 discharges B.4(ii).
3. Whether S-1/S-2/S-3 are chartered as a successor sweep.  S-1 is the most
   recurrent single shape the corpus has produced and no mechanism exists for
   it anywhere.
4. Whether adoption is required of NEW units only, or whether the terminal
   units named in `v14/tpl_census.md` are re-swept.  **TPL's recommendation:
   new units only.**  Re-sweeping terminal units means reopening seals for a
   class of defect that moved no measured number in any unit, and the census
   is the map that makes the exposure visible without touching them.
