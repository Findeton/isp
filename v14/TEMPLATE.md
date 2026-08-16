# THE ERA TEMPLATE — the nine disease families and their cures

*The #267 template sweep (TPL), chartered at v14 ledger #371 per #362.
Reference implementations: `v14/code/era_template.py`.  Exposure census:
`v14/tpl_census.md` (+ `v14/code/tpl_census.py`, `v14/code/tpl_census_receipt.json`).
Drafted addenda for engraving: `v14/tpl_runbook_addenda.md`.  Pin:
`v14/note-tpl-pin.md`.*

---

## 0. WHAT THIS IS, AND WHY IT EXISTS

Nine defects recurred across the v14 instruments often enough that four K3
(instrument) seats independently ruled them **template-shaped rather than
unit-shaped** and asked for a corpus sweep before any further engraving:

- **LOR K3 (#267)** — *"MAJOR-1/2/5/6 are TEMPLATE-SHAPED, not LOR-shaped —
  the corpus sweep of sibling units recommended before engraving"*, plus
  **#269's caveat of record**: *"the three wall mutants die honestly — ON THE
  SURFACE LEG, which is not the leg the wall is owed. A green sweep is not
  evidence a wall holds."*
- **NDEP K3 (#344)** — *"Eight of the ten majors are TEMPLATE-SHAPED... the
  #267 corpus-sweep recommendation was not fully absorbed... should now be
  treated as **owed rather than recommended**, and the four repairs that
  generalise should be made in the template before being made here, so the
  next unit does not buy them a fourth time."*
- **EPR K3 (#358-era)** — *"Four of the seven majors are TEMPLATE-SHAPED, not
  EPR-shaped... treat the fence-multiset and claim-occurrence gates as
  corpus-wide template repairs, not paper-38 repairs, and re-sweep the
  siblings built on the same template."*
- **SEC-2 K3 (#361)** — *"Ten of the thirteen majors are TEMPLATE-SHAPED, not
  SEC-2-shaped... treat MAJOR-3/4/5/6/7/9/10/11/12/13 as the #267 sweep's
  first concrete work list rather than as SEC-2 repairs alone — every one of
  them is a two-to-six-line fix that should land in the shared template."*

Plus **one realized harm**: SEC-2's §4.2 declaration-fiber column was typed
rather than computed, and two of its values were false (27→24, 9→8) — the
era's first and only false delivered numerals, repaired to truth and
disclosed at ledger #362/#368.  Every other instance in this document is a
mechanism defect caught before it moved a number.

**What the panels did NOT find, anywhere, is a wrong measurement.**  Every
K3 seat cited here recorded that no measured quantity was wrong.  These nine
families are diseases of the **perimeter** — of what an instrument would
catch if its paper drifted, not of what it computed.  That is exactly why
they recur: a perimeter defect leaves no trace in any number, so it survives
every check the physics passes.

**Status.** This document is a specification, not an engraving.  The
engraving drafts live in `v14/tpl_runbook_addenda.md` and are the
orchestrator's to apply.  No seal is reopened by anything here; the census
edited, executed and re-delivered nothing.

---

## 1. HOW TO USE THIS DOCUMENT

- A **pin** cites the families it requires by letter, and names the checks by
  id (`T-SEAL-PROMOTION`, …).  A pin that requires a family inherits its
  obligations verbatim.
- A **worker** implements the obligations.  `v14/code/era_template.py` is the
  reference: import it, or copy the mechanism.  Every check ships with its
  own positive controls, so a worker can prove its adoption bit rather than
  assert it.
- A **K3 seat** probes the nine families by name and reports PRESENT/ABSENT
  per family, using the published injection recipes below.  A seat that
  reports ABSENT states which leg it probed — the #269 caveat is binding: a
  kill on the wrong leg is not evidence.
- An **adjudicator** reads `v14/tpl_census.md` for the unit's exposure before
  writing repair orders, and reads §11 below before charging a defect as a
  unit's own.

Run the reference implementations' own demonstration:

```
python3.13 v14/code/era_template.py --selfdemo     # every family's kill, live
python3.13 v14/code/era_template.py --selftest     # every enforcement, load-bearing
python3.13 v14/code/era_template.py --list-families
```

`--selfdemo` runs a clean control and a set of positive controls per family;
each positive control must die at that family's named check, and the demo
exits non-zero if any survives.  `--selftest` disables each family's
enforcement in turn and requires the demo to go red — the #34 reachability
leg at the template's own hands.

---

## 2. FAMILY (a) — SEAL INTEGRITY · `T-SEAL-PROMOTION`

**THE EVIDENCE (convergent; twenty-one units measured PRESENT).**

| review | finding | what survived at exit 0 |
|---|---|---|
| `review-sec2-instrument.md` | MAJOR-1 `[TEMPLATE]` | both forms: a value mutated inside a *sealed* key and an undeclared top-level key added; the receipt lands self-contradicting — its manifest publishes a digest that does not match the value beside it — and the instrument raises nothing |
| `review-spc-instrument.md` | MAJOR-1 | the paired injection that fixes the window exactly: the same insertion **before** the totality computation dies; **after** it, a 50-key receipt ships at exit 0 |
| `review-ndep-instrument.md` | MAJOR-1 | `R["forged_finding"] = {...}` reaches disk while the transcript reports *"seals 34 over 35 published keys, missing none"* about a file with 36 |
| `review-epr-instrument.md` | MAJOR-5 | three faces: a post-snapshot key ADD; a declared-unsealed key rewritten to testify *"float64 throughout"*; and **a seal naming a gate that never ran — already shipped** |
| `review-pot-instrument.md` | MAJOR-6 | nine of twenty declared-unsealed keys forged after the totality gate, including `verdict`, `totals`, `provenance` and a re-chained ledger |
| `review-sec-instrument.md` | MAJOR-4 | *"the gate-to-disk seal is published but never verified"* — the receipt ships a seal that contradicts the payload it seals |
| `review-fac-instrument.md` | MAJOR-4 | `R["reviewer_forged_headline"]` inserted between the manifest assignment and `json.dumps`; the control one statement earlier fails |
| `review-r4b-instrument.md` | MAJOR-1 | the terminal gate **re-derives the head from the corrupted counts and confirms the corruption** — the failure #119 was bought for |
| `review-act`, `-aid`, `-coup`, `-cra`, `-giter`, `-lor`, `-perl`, `-perr`, `-r4c`, `-r5`, `-smu`, `-u4`, `-u4b` | MAJOR-2 / -5 / -3 / -1 / -7 / -4 | the same window in thirteen further units: seal→write gaps, declared-unsealed forgery, no gate-time seal at all, promotion before verification |

**Doctrine.** RUNBOOK §14 addendum (#119, the gate-to-disk seal); #119
addendum (#148, the seal manifest is total); and the **#348 amendment**,
adopted in `v14/note-spc-adjudication.md` §9: *"A SEAL MANIFEST IS TOTAL ONLY
IF TOTALITY IS RECOMPUTED AT PROMOTION TIME."*  (See §12 — that amendment is
recorded as engraved and is not present in `RUNBOOK.md`.)

**THE REQUIRED BEHAVIOUR.**

1. **Digest at gate time.** A value is sealed at the moment its gate passes,
   never in a batch at the end, never at the final gate.
2. **Verify at promotion, against the gate-time digest.** Before staging,
   recompute `digest(payload[k])` for every sealed `k` and compare it with
   the digest taken at its gate.  A re-derivation from the payload at write
   time is not an integrity check; it confirms whatever it is handed.
3. **Recompute totality at promotion.** `set(payload) − {manifest}` must be a
   subset of `sealed ∪ declared-unsealed`, computed **from the payload's live
   key set at the door**, never from a snapshot taken when the totality gate
   fired.  This kills the ADD.
4. **Constrain the partition.** A key that a measurement produced may not be
   moved to the unsealed side; every unsealed key carries a reason; no key is
   in both dictionaries.
5. **Validate `sealed_at_gate`.** Every seal's declared gate must be a gate
   that ran.
6. **Verify BEFORE you promote, and again after.** Stage → read back → verify
   against the gate-time seals → `os.replace` → re-verify from the promoted
   path.  An instrument that promotes first and reads back afterwards has a
   real gate firing after the damage is done: `review-smu-instrument.md`
   MAJOR-3 refused at `G-ARTIFACT-INTEGRITY` with exit 1 and left both
   sandboxes holding corrupted artifacts — *"No `.tmp` was left in either, so
   there is no recovery path either."*
7. **Leave no residue.** Staging temporaries are removed in a `finally`, on
   every exit that is not a successful promotion (`review-pot-instrument.md`
   MAJOR-10: a refusing run left both `.tmp` files in `v14/code/`).

**REFERENCE.** `era_template.Seal` (`seal`, `declare_unsealed`,
`verify_at_promotion`, `close`, `verify_after_promotion`) and
`era_template.promote`.  Positive controls in `--selfdemo`: `ADD`, `EDIT`,
`POST-CLOSE`, `DE-SEAL`, `PHANTOM-GATE`.

---

## 3. FAMILY (b) — THE TRANSCRIPT BOUND TO THE LEDGER · `T-TRANSCRIPT-BOUND`

**THE EVIDENCE (convergent; thirteen units measured PRESENT, and the probe
layer finds the mechanism in none of the thirty-nine).**

| review | finding | what survived at exit 0 |
|---|---|---|
| `review-sec2-instrument.md` | MAJOR-9 `[TEMPLATE, #267 NAMED]` | a `PASS`→`FAIL` edit, a forged measured number and a wholly invented gate row, all promoted; and four different gate counts published by one run (34 / 34 / 42 / 45) |
| `review-ndep-instrument.md` | MAJOR-2 | one line in the renderer makes the transcript read `evidence: unique 99` where the receipt reads `unique 45`; **the two published artifacts contradict each other on the unit's own headline census and nothing notices** |
| `review-epr-instrument.md` | MAJOR-6 | the "gate-time seal" is a hash of the live lines taken at promotion, so the comparison *cannot fail on content*; a forged `[PASS] G-LOCAL-REALISM-RESTORED` line promotes beside a byte-perfect receipt |
| `review-pot-instrument.md` | MAJOR-7 | `[PASS] G-A-GATE-THAT-NEVER-RAN` appended to the log and delivered |
| `review-lor-instrument.md` | MAJOR-5 | the integrity check covers 40 of 221 lines; a forged staged line is PROMOTED beside a byte-perfect receipt |
| `review-perr-instrument.md` | MAJOR-3 | two of three forged-line shapes admitted; `ln.startswith(" " * 9)` admits any nine-space-indented line, and the falsifier is calibrated to the one shape the guard rejects |
| `review-fac-instrument.md` | m1 | a forged `[PASS]` line appended *before* the digest is taken: promoted, `whole == staged` True, receipt ledger `[]` |
| `review-act`, `-aid`, `-coup`, `-r6a`, `-sig`, `-spc` | MAJOR-2 / -5 / -2 / M4 / MINOR-5 / m6 | gate rows in neither artifact; console totals not archived; `transcript_head` never re-derived from the promoted file |

**THE REQUIRED BEHAVIOUR.**

1. **Parse the finished transcript back.** Extract every `[PASS]/[FAIL] GATE
   :: evidence` line from the text that will be promoted.
2. **Reconcile as a multiset, evidence included.** The parsed multiset must
   equal the ledger's `(gate, passed, evidence)` multiset — both directions.
   A forged row is stray; a dropped row is missing; a forged number inside an
   evidence string moves the key.
3. **Reconcile the counts.** Rows published, gates fired, `--list-gates`
   output and any `totals.gates` must be one number, computed once, after the
   last gate.  A ledger snapshotted before the closing gates publishes a
   chain that covers everything except the gates that certify the seal.
4. **Seal the whole transcript, not a prefix**, at close; compare the promoted
   bytes against that digest.
5. **Chain the ledger** so a row cannot be inserted, dropped or reordered
   without moving the head, and recompute the chain from the receipt's own
   bytes.

**REFERENCE.** `era_template.Transcript` (`row`, `parse`, `bind`) and
`era_template.Ledger` (`gate`, `recompute_chain`).  Positive controls:
`FORGED-VERDICT-WORD`, `FORGED-EVIDENCE`, `INVENTED-ROW`, `DROPPED-ROW`.

---

## 4. FAMILY (c) — SEMANTIC WALLS · `T-WALL-SEMANTIC`

**THE EVIDENCE (convergent; fifteen units measured PRESENT).**

| review | finding | what survived at exit 0 |
|---|---|---|
| `review-epr-instrument.md` | MAJOR-7 | a seven-string blacklist: *"On the measured arms this restores local realism."* passes (the list holds the passive voice); a Bell-evasion paraphrase passes; and **the paper's own wall sentence can be deleted** |
| `review-ndep-instrument.md` | MAJOR-6 | 4 of 5 natural violations pass; *"the positive control is the pattern's own sentence, so every probe fires by construction and proves only that a regex matches the string it was written from"* |
| `review-lor-instrument.md` | MAJOR-1 (+ #269) | the three reading walls **never scan the paper**; and the sweep's green is on the wrong leg |
| `review-pot-instrument.md` | MAJOR-1, MAJOR-2 | the licence wall licenses itself — `"confines"` is both policed and licensing, so *"It confines."* passes; and a licensed-looking sentence with **wrong values** passes |
| `review-sec2-instrument.md` | MAJOR-10, MAJOR-11 `[TEMPLATE]` | *"The freedom is reducible after all."* passes where the same sentence with a lower-case opener dies — the gate is defeated by a capital letter; and five prose direction flips invert delivered findings in the paper's own voice |
| `review-u4-instrument.md` | MAJOR-1 | the banned sentence passes when inserted **line-wrapped in house style** (the #125 disease) |
| `review-u4b-instrument.md` | MAJOR-6 | the same sentence as a blockquote or a list item — 2 of 8 wrappings evade |
| `review-giter-instrument.md` | MAJOR-6 | `git  show` (two spaces), `git\tshow`, `git show\nHEAD:` — 4/4 evade a contiguous-literal scan |
| `review-aid`, `-act`, `-fac`, `-perr`, `-r3w`, `-r5`, `-r5m` | MAJOR-3 / -4 / -3 / -6 / M3 / -3 / M2 | paraphrase defeats a five-form blacklist; direction-bearing headlines unbound outside a four-fragment list; walls that are self-declarations wearing a gate's clothes |

**Doctrine.** RUNBOOK §14 addendum (#125, text gates match text as written);
#20-with-fenced-blocks; LOR #269's caveat.

**THE REQUIRED BEHAVIOUR.**

1. **Patterns, not strings.** Every banned form is a voice-normalised regex
   over the canonicalised paper — active and passive, verb and noun, with
   bounded gaps.  A fixed-string blacklist is not a wall.
2. **Case-folded.** Both sides.  A sentence-initial capital is not a defence.
3. **#125 normalisation.** Whitespace folded, markdown blockquote/list
   prefixes stripped, emphasis dropped, before any match.
4. **A positive leg.** The wall requires the paper to CARRY its standing
   sentences.  Deleting the wall's own verdict must fail, or the wall is
   one delete away from vacuous.
5. **Non-vacuous.** Empty or absent text FAILS.  A wall that passes on `""`
   passes on every mode that forgot to load the paper.
6. **No self-licensing.** A licence set may not contain the policed word, and
   a policed sentence must carry a **rendered claim string**, not merely a
   token that appears somewhere in a registry.
7. **Controls written by another hand.** A wall's positive control may not be
   derived from its own pattern; at least one control per wall is phrased as
   a paper would phrase it.
8. **The wall scans the object under test.** Not the instrument's own keys,
   not its gate statements — the paper.

**REFERENCE.** `era_template.SemanticWall` (`scan`, `_licence_leg`,
`seal_value`).  Positive controls: `RE-VOICED`, `PARAPHRASE`, `DELETED-LEG`,
`EMPTY`, `CAPITALISED`, `SELF-LICENCE`, `SELF-LICENSING-SET`.

---

## 5. FAMILY (d) — VERBATIM ANCHORS CONSUMED · `T-ANCHOR-CONSUMED`

**THE EVIDENCE (convergent; sixteen units measured PRESENT, and the probe
layer finds a consumption accessor in two of thirty-nine).**

| review | finding | what survived at exit 0 |
|---|---|---|
| `review-pot-instrument.md` | MAJOR-9 | *"0 of 15 verbatim anchors are consumed by their named gate"* — `vb` is passed to three measure functions and **no `vb[...]` subscript exists anywhere in the file** |
| `review-ndep-instrument.md` | MAJOR-4 | proven by receipt-leaf diff: replacing an anchor's needle with a different true sentence from the same parent moves **3 leaves and not one measured quantity** |
| `review-epr-instrument.md` | probe 6 / MINOR-10 | `consumed_by` is written once and never read again in 3,511 lines; rewriting all 14 consumers to a gate that does not exist runs clean |
| `review-act-instrument.md` | MAJOR-3 | all **53** consumer names rewritten to `G-DOES-NOT-EXIST`; the receipt ships `{"G-DOES-NOT-EXIST": 53}` beside a 45-row ledger |
| `review-sec-instrument.md` | MAJOR-5 | anchors verified on the **wrong side**: all five block quotations in the paper can be inverted freely, including one that inverts R1's copy-forcing theorem |
| `review-smu-instrument.md` | MAJOR-1 | *"0 of the paper's 12 quotations of its parents are bound"* — the anchors gate the parent's bytes, nothing gates the paper's rendering |
| `review-r6bp-instrument.md` | M3 | the window preserved byte-for-byte and its meaning inverted **around** it — the anchor binds existence, not meaning |
| `review-r4b-instrument.md` | MAJOR-2 | a 138-byte window truncated to the 4 bytes `"the "`; output byte-identical to the committed artifact |
| `review-aid`, `-gprep`, `-perr`, `-r4c`, `-r6a`, `-sec2`, `-sig`, `-w2` | MAJOR-4 / -4 / -4 / -1 / M5 / MINOR-3 / -5 / -4 | phantom consumer gates, unexercised anchors, four-character needles, a consumer register with a producer and no consumer |

**THE REQUIRED BEHAVIOUR.**

1. **One accessor.** Anchor text is readable only through `read(name, by_gate)`,
   which records the read.
2. **Consumption verified.** Every anchor's declared consumer gate must have
   actually read it.  A name check is not a consumption check.
3. **The consumer must exist.** Its id must be a gate that ran.
4. **Both sides.** The needle must occur in the pinned source **and** in the
   paper's own rendering, under #125 canonicalisation.  Otherwise a
   blockquote can be inverted while the anchor stays green.
5. **Exactly once, above the floor.** Occurrence count one, length above the
   #62 floor; a four-character needle is decoration.
6. **The content enters a predicate.** The consuming gate takes a value out
   of the anchor's located text and compares it with a measurement — meaning,
   not existence.

**REFERENCE.** `era_template.Anchor`, `era_template.AnchorSet` (`locate`,
`read`, `verify_consumption`).  Positive controls: `PHANTOM-CONSUMER`,
`FABRICATED-CONSUMER`, `WRONG-SIDE`.

---

## 6. FAMILY (e) — CLAIMS BY EQUALITY, TWO-WAY, TABLE-SIGHTED · `T-CLAIMS-EQUAL`

**THE EVIDENCE (the most widely convergent family; twenty-six units measured
PRESENT).**

| review | finding | what survived at exit 0 |
|---|---|---|
| `review-sec2-instrument.md` | MAJOR-3 `[TEMPLATE]` | two header swaps between published tables and two rows transplanted from one table into another, four independent table pairs, all at exit 0 — *"the gate catches invented content and misses misplaced content"* |
| `review-sec2-instrument.md` | MAJOR-4 `[TEMPLATE, E-22 NAMED]` | E-22 met by containment in both directions: a fabricated ninth fence passes, and **deleting the whole §9 Verdict block passes** |
| `review-epr-instrument.md` | MAJOR-1, MAJOR-2, MAJOR-3 | one table in five never rendered — the one carrying the unit's Bell obligations; the three verdict fences **matched zero times**, so six head forgeries pass including the deletion of the no-local-realism stamp; five duplicated claims forgeable in one copy |
| `review-pot-instrument.md` | MAJOR-4, MAJOR-5 | `hits >= need` with `need = 1` while 13 of 39 claims occur 2–3 times, so one of three copies of `gap 1/2` becomes `gap 1/4` and the paper states two different gaps; table cells bound by nothing |
| `review-ndep-instrument.md` | MAJOR-5, MAJOR-9 | the whole §2.1 corpus table unbound (header swap and a false schedule count both byte-identical); an eighth fence contradicting the head admitted |
| `review-sec-instrument.md` | MAJOR-1 | twelve forgeries at 37/37 exit 0, including the unit's central result inverted and a forged head hidden in a fence whose info string carries a digit |
| `review-lor-instrument.md` | MAJOR-2 | 27 of 40 table rows unrendered; four forgeries survive including a swapped ceiling column in the unit's own theorem |
| `review-act`, `-aid`, `-coup`, `-cra`, `-fac`, `-gdl`, `-gmain`, `-occ`, `-perl`, `-perr`, `-r1`, `-r2`, `-r4`, `-r4c`, `-r4dec`, `-r5m`, `-r6bp`, `-sig`, `-smu`, `-w2` | MAJOR-1 / -3 / -3 / -2 / -5 / -2 / M5 / -1 / -9 / -1 / M3 / M2 / F6 / -2 / -2 / M5 / M5 / -3 / -1 / -5 | unbound headers, one-directional table checks, fences carried twice with either copy forgeable, prose claims never searched for in the paper |

**Doctrine.** RUNBOOK E-22 (inline-span coverage; blocks by multiset; tables
render as claims); #20 with fenced blocks; #87 (gates bind objects, not
cardinalities).

**THE REQUIRED BEHAVIOUR.**

1. **Keyed by table.** The licensed row multiset is keyed by the table the
   row was rendered into.  A row transplanted between tables is stray in one
   and missing in the other.
2. **Headers are rows.** Rendered and compared like any other row.
3. **Both directions, always.** `missing` AND `stray`, with `stray` testing
   `got[k] > want[k]` rather than `k not in want` — otherwise a duplicated
   legitimate row is invisible.
4. **Every table rendered.** A markdown table in the paper that no rendering
   claims is a failure, not a silence.  Gate that the paper's table set is
   EXHAUSTED by the rendered set.
5. **Exact occurrence counts.** `hits == need`, with `need` computed from the
   licensed rendering.  A floor of one leaves every duplicate forgeable.
6. **Fences by multiset equality**, with declared multiplicity, over blocks
   tokenised **whatever the info string** — so both an extra fence and a
   deleted fence block die.
7. **Inline spans scanned** (E-22), and the numeral scan blind-spot-free:
   a numeral ending a sentence is a numeral.

**REFERENCE.** `era_template.Claims` (`table`, `claim`, `fence`, `gate`).
Positive controls: `HEADER-SWAP`, `ROW-TRANSPLANT`, `DUPLICATED-ROW`,
`TWIN-FORGERY`, `EXTRA-FENCE`, `DELETED-FENCE`, `UNRENDERED-TABLE`.

---

## 7. FAMILY (f) — SENTENCE-LEVEL REFERENT BINDING · `T-REFERENT-BOUND`

**THE EVIDENCE (convergent; nineteen units measured PRESENT, and the probe
layer finds a per-occurrence prose-only binding in none of the thirty-nine).**

| review | finding | what survived at exit 0 |
|---|---|---|
| `review-sec2-instrument.md` | MAJOR-12 `[TEMPLATE, #267 shape]` | *"the kernel is 455"* (a group count used as a matrix kernel), *"455 seam types"*, *"every one of the 132,273 composites"* — six live universes, and any of their numerals validates any other's sentence |
| `review-spc-instrument.md` | MAJOR-2 | *"The census hosts 156 of 220 species"*; and §4's headline contrast inverted from `2 of 30` to `30 of 30` — **carried through a full delivery at 46/46 gates passed, with the corrupted paper's digest sealed into the receipt** |
| `review-ndep-instrument.md` | MAJOR-7 | the bindings are satisfied **inside the run's own machine-derived verdict fences**, so four cross-universe plants pass byte-identically — *"#87 for prose: a gate on 'there exists a correct occurrence' is an aggregate predicate"* |
| `review-sec-instrument.md` | probe 9 | four numerals from four different universes composed into one sentence contradicting the receipt on every clause |
| `review-fac-instrument.md` | MAJOR-2 | a cell-census numerator over a corpus denominator, and a histories count over a partition-lattice size — both numerals true, the relation false |
| `review-pot-instrument.md` | MAJOR-2 / probe 9 (+ residual, ledger #363) | *"The 136 couplings this arena admits are one per class, and the 149 extreme points were all swept."* |
| `review-epr-instrument.md` | MINOR-7 | membership, not truth: an in-universe pair the run never measured passes |
| `review-aid`, `-coup`, `-cra`, `-gdl`, `-lor`, `-occ`, `-perl`, `-perr`, `-r1`, `-r5m`, `-r6a`, `-sig`, `-smu` | MAJOR-1 / -3 / -2 / -5 / MAJOR-6 / -4 / -5 / -2 / M5 / M3 / M7 / -4 / MINOR-5 | one global registry; allow-lists polluted by sha256 fragments; denominators that belong to another census |

**THE REQUIRED BEHAVIOUR.**

1. **Universes are declared**: a name, its nouns, its values, and **the pairs
   the run actually measured**.
2. **The sentence selects the universe** by its subject noun; its numerals
   are resolved against THAT universe only.
3. **Per occurrence.** Every occurrence is checked.  `any(...)` over the
   paper is an aggregate predicate and is forbidden (#87).
4. **Prose only.** Fenced blocks are stripped before the scan, so the run's
   own verdict fences cannot discharge the paper's obligations.
5. **Pairs, not membership.** An `A of B` fraction must be a measured pair,
   not two members of one set.
6. **Whitelists are digest-shaped and declared.** A twelve-hex token is
   excluded because it is a digest, never because a numeral happens to sit
   inside one; every exemption is declared and must be used.

**REFERENCE.** `era_template.ReferentRegistry` (`universe`, `prose_only`,
`gate`).  Positive controls: `CROSS-UNIVERSE`, `WRONG-PAIR`,
`FENCE-SATISFIED`.

---

## 8. FAMILY (g) — NO TYPED COUNTS · `T-NO-TYPED-COUNTS`

**THE EVIDENCE (convergent; twenty-two units measured PRESENT — and the only
family that has already caused a realized harm).**

| review | finding | what was measured |
|---|---|---|
| **SEC-2 §4.2 (ledger #362/#368)** | **the realized harm** | a typed declaration-fiber column, two of whose values were **false**: 27→24 and 9→8, computed and corrected under the ordered exception, disclosed in-paper.  The era's only false delivered numerals |
| `review-sec2-instrument.md` | MAJOR-13 `[TEMPLATE]` | `union_min = 1` — a typed constant published as a measurement, asserted in the paper, carried in the head, typed on **both** sides of the comparator, and the whole of criterion 3 |
| `review-lor-instrument.md` | MAJOR-3 | three false published counts, typed, ungated and self-contradicted: seals 37 vs 36, gates 41 vs 53, five receipts where six are read |
| `review-epr-instrument.md` | MINOR-5 | a sealed gate statement reading *"Fifteen claims"* beside its own evidence field reading `claims 16` |
| `review-perl-instrument.md` | MAJOR-6, MAJOR-2 | the verdict's most contested segment is a typed literal, emitted with no format specifier; `"sources": len(SOURCES)` replaced by the literal `9` survives |
| `review-pot-instrument.md` | MAJOR-3 | the numeral registry admits **all 10 single digits and all 90 two-digit tokens**, so every one- or two-digit headline can be rewritten freely |
| `review-act-instrument.md` | MAJOR-5 | spelled numerals not scanned at all; two load-bearing counts free |
| `review-sec-instrument.md` | "Head literals are typed" | `STRUCT-ALIVE-16-OF-16`, `RANK 6 ON THE 10 ENTRIES` typed into the head segments; a typed product published as a measurement |
| `review-cra`, `-gdl`, `-gmain`, `-ndep`, `-perr`, `-r1`, `-r3`, `-r4`, `-r4c`, `-r4dec`, `-r5m`, `-r6a`, `-r6bp`, `-smu`, `-u4b` | MAJOR-1 / -4 / D7 / m5 / -5 / M6 / M5 / F4 / MINOR-4 / -3 / m2 / M2 / M7 / MINOR-2 / -5 | hand-typed allow-lists, typed constants presented as measurements, counts published by two different miscounts that happen to coincide |

**Registered residuals owed to this sweep**: PER-R's six claim templates
(ledger #353), EPR's two typed testimony leaves (#359), SEC's 234 small
structural numerals (#367).

**THE REQUIRED BEHAVIOUR.**

1. **Values enter by measurement.** `measured(name, value, how)` records
   provenance; a value with no provenance cannot be published as a
   measurement.
2. **Statements interpolate.** A published gate statement, claim template,
   head segment or testimony leaf carries **no typed numeral**; every numeral
   arrives by name from the live registry.
3. **The template is checked before substitution**, so the prohibition is on
   the source, not on the output.
4. **Declared exemptions only** — a paper id, an engraving id, a year — each
   declared with its reason and required to be used.
5. **An AST leg.** Scan the module: any string literal handed to a gate or
   statement builder that types a numeral is an offender, whatever the
   docstring says.
6. **The comparator may not type what the builder types.** A number typed on
   both sides is invisible to the head reconstruction.

**REFERENCE.** `era_template.CountRegistry` (`measured`, `exempt_token`,
`stmt`, `audit_module`).  Positive controls: `TYPED-STATEMENT`,
`UNMEASURED-NAME`, `NO-PROVENANCE`, `AST-AUDIT`.

---

## 9. FAMILY (h) — FALSIFIERS THAT POISON MEASUREMENTS · `T-FALSIFIER-POISONS`

**THE EVIDENCE (convergent; twenty-six units measured PRESENT).**

| review | finding | what was measured |
|---|---|---|
| `review-sec2-instrument.md` | MAJOR-7 `[TEMPLATE, E-23 NAMED]` | six sentinel-shaped falsifiers: `same[0] = False`, `floats + ["injected"]` — *"they prove the gate raises when handed a False, not that it detects the corruption it advertises"*.  The two most load-bearing instruments in the corpus, the verdict comparator and the paper renderer, **have no falsifier that touches them** |
| `review-sec2-instrument.md` | MAJOR-6 | four gates carry no falsifier and no waiver; `G-COVERAGE` exempts itself by snapshotting the gate list before appending itself |
| `review-ndep-instrument.md` | MAJOR-10 | one description inverted, one a constant injection, one falsifier exempting the leg it should exercise |
| `review-epr-instrument.md` | MAJOR-4 | descriptions never matched against behaviour; a description-inverted falsifier passes trivially; `MUT-REFERENT` promises a planted fraction and appends a sentinel |
| `review-sec-instrument.md` | MAJOR-6 | **six untrue waiver forcings** — five named falsifiers provably die at an EARLIER gate and never reach the gate they are said to falsify |
| `review-smu-instrument.md` | MAJOR-4 | 15 of 42 falsifiers corrupt no object; 15 gates have none that does; two of those gates cannot fail on any object |
| `review-r4dec-instrument.md` | MAJOR-4 | seven of fifty synthetic, their published descriptions inverting their code; five shadow mutants that corrupt the object instead all die correctly |
| `review-perr-instrument.md` | MAJOR-3 (the meta-shape) | *"the falsifier is calibrated to the guard rather than to the threat, so the sweep's green badge on this gate is not evidence"* |
| `review-lor` #269 | the caveat of record | *"the three wall mutants die honestly — ON THE SURFACE LEG, which is not the leg the wall is owed"* |
| `review-aid`, `-coup`, `-cra`, `-gdl`, `-giter`, `-gmain`, `-gprep`, `-perl`, `-pot`, `-r1`, `-r2`, `-r3`, `-r3w`, `-r5`, `-r5m`, `-r6a`, `-r6bp`, `-sig`, `-u4b` | MAJOR-4 / -4 / -1 / -3 / -5 / M2 / -6 / -4 / `MUT-MUSTNOT` / M4 / M6 / M6 / M3 / -4 / M4 / M3 / M4 / -1 / m4 | tautological predicates, constant injections, waivers whose named mutant is shadowed, honest denominators far below the published ones |

**Doctrine.** RUNBOOK E-23 (falsifier honesty); #34 with reachability.

**THE REQUIRED BEHAVIOUR.**

1. **Every falsifier names its target** — the measured object the recipe must
   move.
2. **The harness proves the move.** Digest the target before and after; a
   recipe that leaves it identical has poisoned a verdict variable and dies
   here, whatever colour its badge is.
3. **Death at the declared gate, not before.** A falsifier that dies earlier
   has not falsified the gate it is credited to; a waiver naming it is untrue.
4. **Descriptions matched against code**, by AST: a hook whose body assigns a
   constant boolean or appends a constant is a sentinel, not a falsifier.
5. **Coverage inside its own denominator.** The coverage gate counts itself;
   a gate list snapshotted before the coverage gate appends itself is a
   self-exemption.
6. **Waivers carry machine-checked forcings**, not descriptions.
7. **Calibrate to the threat, not the guard.** At least one control per gate
   is written against the disease as a paper would produce it — the #269
   caveat is part of this obligation, not a footnote to it.

**REFERENCE.** `era_template.Falsifier`, `era_template.FalsifierHarness`
(`run_one`, `audit_descriptions`, `coverage`).  Positive controls:
`SENTINEL`, `UNREACHED-GATE`, `ABSENT-TARGET`, `UNCOVERED-GATE`,
`UNFORCED-WAIVER`, `AST-AUDIT`.

---

## 10. FAMILY (i) — READ SETS AT THE I/O ACCESSOR · `T-READ-SET`

**THE EVIDENCE (convergent; eighteen units measured PRESENT).**

| review | finding | what survived at exit 0 |
|---|---|---|
| `review-sec2-instrument.md` | MAJOR-2 | the read log is appended inside a helper, the gate fires once before the anchor loop, and three `READLOG.pop()` calls remove reads.  **The pin's own prohibited file walks in two ways of three**: the same read after the gate, and any raw `open()`, both at exit 0 |
| `review-sec-instrument.md` | MAJOR-3 | the read list is built **inside the loop over SOURCES**, so the comparison is true by construction; injection CINJ-B reads the very file the unit abstains from and reports `violations: []` |
| `review-lor-instrument.md` | MAJOR-4 | `G-READS-DECLARED` is positionally vacuous: it fires second, before the object under test is even read; a read of the live 453,952-byte `v14/LOG.md` planted after it returns clean |
| `review-sec2-instrument.md` | MAJOR-8 | vacuous modes: `--verify-paper` on an empty file prints PASS, and `--no-write` with the paper deleted passes every wall on `""` |
| `review-gprep-instrument.md` | MAJOR-3 | an `os.popen("git show HEAD:...")` outside the anchor table, at a moving HEAD, failures swallowed, product read by no gate — delivers `LEDGER #None` at 44 PASS |
| `review-r3-instrument.md` | M1 | the delivery reads an unanchored live repo file **and its verdict is a function of it**: appending one ordinary sentence to a scratch `v14/LOG.md` moves a verdict segment and both artifact hashes |
| `review-r4b-instrument.md` | MAJOR-4 | `--verify-paper PATH` is a documented flag that does nothing; a non-existent path exits 0 |
| `review-act`, `-aid`, `-coup`, `-cra`, `-gdl`, `-gmain`, `-perl`, `-perr`, `-r4`, `-r4c`, `-r4dec`, `-r6bp`, `-sig`, `-u4b`, `-w2` | (various) | a second untracked reader; RUNBOOK.md as an unpinned runtime input; `--verify-paper` on a directory; unknown flags silently ignored while both artifacts are written |

**Doctrine.** RUNBOOK §13/#46 addendum (#91, no moving refs); #82 (the CLI
contract).

**THE REQUIRED BEHAVIOUR.**

1. **Record at the accessor.** A `sys.addaudithook` on `open` (or an
   equivalent wrapper) sees every read, including the raw `open()` that never
   passes through the instrument's helper.
2. **Compare at the LAST gate**, order-insensitively, as a multiset of
   relative paths.  A comparison taken early proves nothing about what
   follows.
3. **No silent pops.** An exemption is declared with a reason and must be
   used — an exemption carried and never used is a hole, not a courtesy.
4. **Declared-but-never-read also fails**, so a source list cannot drift.
5. **No vacuous modes.** Every declared mode requires its object to exist and
   be non-empty; walls FAIL on empty text.  A mode weaker than the delivery
   path is a mode a reviewer is invited to be misled by.
6. **No moving refs** (#91): no subprocess, no git, no unpinned repository
   read whose product a gate consumes.

**REFERENCE.** `era_template.ReadSet` (`install`, `exempt`, `gate_at_close`)
and `era_template.require_object`.  Positive controls: `RAW-OPEN`,
`DECLARED-NEVER-READ`, `UNUSED-EXEMPTION`, `VACUOUS-MODE`, `ABSENT-OBJECT`.

---

## 11. THE SUCCESSOR REGISTER — what the sweep found beyond its charter

The charter named nine families.  The read-only sweep of all thirty-six K3
reviews found **three further shapes at least as recurrent as the nine, which
no family covers**, and four which extend a family rather than sit outside
it.  They are registered here, unimplemented, for the orchestrator to
charter or dismiss.

**S-1. THE COMPARATOR IS THE BUILDER.**  The single most recurrent shape in
the corpus.  Family (e) binds *paper* claims; nothing binds *verdict
reconstruction*.  `review-r2-instrument.md` M1: *"The 'rebuild' is the same
function on the same payload... INJ16 settles the question of how much the
gate knows about the measurement: nothing."*  Also `review-r5` MAJOR-2 (*"the
segment renderer does not exist"*), `review-r5m` M1, `review-r3w` M1 (71.2 %
of the head rebuilt by calling the builder's own function), `review-gprep`
MAJOR-2, `review-giter` MAJOR-7, `review-sig` MAJOR-2, `review-ndep` MAJOR-3
(the comparator catches 2 of 22), `review-gmain` M1, `review-r4` F1,
`review-r1` M2, `review-r3` M3, `review-w2` MAJOR-1, `review-r4dec` MAJOR-5,
`review-u4b` m2, `review-perl` MAJOR-6.  RUNBOOK already carries the #82
comparator-independence clause; what is missing is a *mechanism* and a
*test*, i.e. exactly what this template supplies for the other nine.

**S-2. TWO "INDEPENDENT ROUTES" THROUGH ONE COMPONENT.**  Not a comparator
but a measurement: `review-r6a` M2 (*"the admissible fiber equals an
independent recomputation — same function, same input"*), `review-r3` M2
(zeroing the column **both** routes share leaves `G-CENSUS-TWO-ROUTES`
green), `review-occ` MAJOR-3, `review-r1` M1, `review-r2` M3, `review-r6bp`
M10, `review-sig` MINOR-1.

**S-3. THE PRE-REGISTERED OUTCOME IS UNREACHABLE.**  `review-giter` MAJOR-1
(*"a deviation here would have looked like a refused run, not like a located
deviation"*), `review-sig` MAJOR-6 (*"'45 of 45 gates PASS' is not evidence
for the verdict, because the gates encode it"*), `review-gmain` M8 (*"the
clean 36/36 sheet is contingent on the verdict coming out PARTIAL"*),
`review-u4` MAJOR-2, `review-r6bp` M7.  **This one is already engraved in the
ledger and not in the RUNBOOK** — see §12, ledger #299.

**Extensions rather than new families:** *write-before-verify / no rollback*
(promotion ORDER, not verification — `review-smu` MAJOR-3 promotes both
corrupted artifacts with no `.tmp` left, hence no recovery path; extends (a));
*the closing gates' verdicts appear in neither artifact* (extends (b));
*sealed self-description false* — E-23's description-vs-code duty applied to
**gate statements and sealed warrants** rather than to falsifiers
(`review-perr` MAJOR-7: *"a sealed vouching row carrying two false
statements"*; extends (g)/(a)); and *falsifiers calibrated to the guard
rather than to the threat* (folded into (h) obligation 7 above).

---

## 12. A FINDING OF RECORD: FOUR ENGRAVINGS ARE IN THE LEDGER AND NOT IN THE RUNBOOK

Measured, not inferred, at the time of this sweep:

- `RUNBOOK.md` was last modified at commit `c3bd7b5` — **v14 ledger #192**
  (E-24).  Its final engraving is E-24.
- Four later ledger entries record engravings: **#295** (the class-binding
  engraving), **#299** (*"ENGRAVED: every pre-registered outcome word must be
  shown reachable at the declared arena by a feasibility line in the pin"*),
  **#319** (the pin's feasibility engraving sharpened), and **#348** (the
  #299 row-list extension **and** the #119 promotion-totality addendum).
- `v14/note-spc-adjudication.md` §9 states the #348 amendment in terms: *"the
  #119 addendum adopted: A SEAL MANIFEST IS TOTAL ONLY IF TOTALITY IS
  RECOMPUTED AT PROMOTION TIME."*
- A term search of `RUNBOOK.md` finds none of them: `totality`, `manifest`
  (except the #148 line), `reachab*`, `feasibil*`, `class-bind*`,
  `row-list` all return zero matches for the claimed texts.

This is not a defect of any unit.  It is the same disease as family (b) one
level up — **a ledger row that says a thing happened, unreconciled with the
object that would carry it**.  The drafted addenda in
`v14/tpl_runbook_addenda.md` include these four so that a single engraving
pass closes the gap.

---

## 13. WHAT THIS TEMPLATE DOES NOT DO

- It does not reopen a seal.  Every unit named here is terminal, and the
  census edited, executed and re-delivered nothing.
- It does not question a measurement.  No physics number of any unit is in
  doubt anywhere in this document; every seat cited recorded that no measured
  quantity was wrong.
- It does not make a green run evidence.  A unit that adopts these checks has
  adopted a mechanism; whether the mechanism has teeth on ITS object is a
  question only an injection can answer, and LOR #269's caveat stands over
  this template exactly as it stands over a mutant sweep.
- It does not replace the panel.  The census's probe layer is structural: it
  can see that a gate exists and cannot see that a gate binds.  Where a seat
  spoke, the seat is authority.
