# SEC (paper-32) — K3 INSTRUMENT-LENS REVIEW

**Seat:** K3, instrument lens.  **Object:** `v14/paper-32-sec.md`
(`cfe0825d67b2`), `v14/code/sec_exact.py` (`6481a8706503`),
`v14/code/sec_output.txt` (`e80d2f08a257`), `v14/code/sec_receipt.json`
(`fdf66d990dbf`), pin `v14/note-sec-pin.md` (`c46a9927f2a8`).  All five
verified at open and at close, unchanged.  **Authority:**
HANDOFF-PROMPT.md §4/§9; RUNBOOK.md E-22/E-23/E-24; the #267 checklist.

**Every finding below is a CANDIDATE RULING until adjudication.**

---

## GRADE: **AWF** (accept with fixes)

**Why not REJECT.**  The measured layer is clean.  Every headline number
I recomputed from scratch reproduced exactly — 45010, the 16 types and
their populations, 4186, 2970, 1134, 3359232, 62208, the 54/53/52/51
pair counts, rank 6 / kernel 4, the direct-sum minors at both seams, the
(4,3,2,1,0) cross-link ladder.  **No measured quantity is wrong.**  The
delivery byte-reproduces off-tree and git-less; the 30-mutant sweep is
on target out of harness; the CLI contract holds against 13 hostile
argv; the selftest writes nothing, proved by tree hash; post-`os.replace`
corruption dies at `G-INTEGRITY`; the ledger chain recomputes row by row
from bytes to the published head.

**Why not ACCEPT.**  The instrument's **paper leg is not load-bearing**.
Of 71 applied paper injections, **63 survive all eight paper-side gates**
— including the unit's central result inverted inside a table, its own
alignment criterion inverted inside its theorem block, a forged head in a
fenced block, and five quoted source theorems inverted.  A single paper
carrying **twelve independent forgeries passes `--verify-paper` at 37/37
gates, exit 0, artifacts untouched** (MAJOR-1).  Beside that: the read-set
gate that is supposed to prove the LOR abstention is vacuous by
construction (MAJOR-3); the gate-time seals are published but never
compared to anything (MAJOR-4); one published mechanism sentence is
contradicted by the receipt's own rows (MAJOR-2); six waiver forcings are
untrue (MAJOR-6).

---

## COUNTS

| | |
|---|---|
| processes executed | **84** |
| `full_run` evaluations | **141** (3 full deliveries × 31 = 93, out-of-harness sweep 30, 18 verifier/probe/selftest runs) |
| injections with gate evaluations | **93** — 71 paper (each against all 8 paper-side gate predicates), 4 code, 2 write-path, 2 seal-path, 1 twelve-forgery composite end-to-end, 13 hostile argv |
| of those, **survived** every gate | **63 of 71** paper injections (4 of the 8 deaths are my own positive controls); **3 of 4** code injections |
| independent recomputations | **118** — 37 = the ledger chain rebuilt row by row from bytes; 81 = the arithmetic, census, registry, seal and denominator recomputations enumerated below |
| novel corruptions of my own design | **28**, beyond the declared 30 mutants |
| repo writes | **1** (this file) |

Scratch peak 773 MB, all under my own prefixes, per-run trees deleted.

---

## THE NINE PROBES

### 1. UNBOUND TABLE HEADERS — **PRESENT**

`paper_claims()` renders **data rows only** (`"| \`%s\` | %d | ..."`).
No column header of any table is a claim.  **13 header swaps across 8
tables survive all gates**, among them:

- `| type | gluings | n | E | dbl | |Aut| | |Aut_w| | site fiber |` →
  `n`↔`E` and `|Aut|`↔`|Aut_w|` swapped (§3.1);
- `| type | k | gluings | doubled | bare fate | welds |` →
  `gluings`↔`doubled`, `bare fate`↔`welds` (§7);
- `| seam | n(A) | n(B) | equations | unknowns | rank | kernel | ... |` →
  `equations`↔`unknowns`, `rank`↔`kernel` (§6.1);
- `| quantity | k = 0 |` → `| quantity | k = 3 |` (§8, the sterility
  control's entire referent moved by one character);
- `| arena | reading | fate |` → `| arena | fate | reading |` (§4.4).

The semantically-opposed-header probe the task names bites hardest at
§4.1, whose two data rows carry `FOUND-candidate` and `UNMOTIVATED`:
swapping those two rows wholesale — so the paper reads *doubled-free
types are UNMOTIVATED with free item `I-DIRECTION-LABEL` at fiber 9, and
doubled types are FOUND with none* — **survives** (I08).  That is the
unit's headline inverted in place.

### 2. DIRECTION-FLIP POLARITY — **PRESENT**

`POLARITY` has **three** rows: P1 "the union welds", P2 "the direct sum
is a declaration", P3 "R1's prediction is confirmed".  Every headline
direction claim outside those three is free.  Measured:

| flip | fate |
|---|---|
| "every admitted one kills the dictionary" → "**no** admitted one kills" | SURVIVES |
| "k is not what selects" → "k is **exactly** what selects" | SURVIVES |
| "what selects is the ALIGNMENT" → "what selects is **k**" | SURVIVES |
| the ALIGNMENT CRITERION block: "if and only if **no** shared pair is adjacent in BOTH sectors" → "**some**" | SURVIVES |
| its equivalent form: "every shared pair must share a class on at least one side" → "**no** shared pair may share a class on any side" | SURVIVES |
| read-out: "Two welded worlds glued by shared actors compose" → "**never** compose" | SURVIVES |
| "The extended carrier repairs the seam by declaring away the thing the seam measures" → "by measuring the thing the seam declares" | SURVIVES |
| "the direct sum is a declaration, not a measurement" → inverted | dies at `G-PAPER-POLARITY` (P2) |
| "R1's prediction is confirmed" → "refuted" | dies at `G-PAPER-POLARITY` (P3) |

Two of the three declared polarity rows fire; the head's own
`TYPE-SELECTED-NOT-k-SELECTED` verdict word can be contradicted in prose
without a gate noticing.

### 3. TRANSCRIPT-INTEGRITY WHITELISTS — **ABSENT**

There is no transcript-parsing gate at all: `sec_output.txt` is read only
by `finish()` (byte comparison against the in-memory render) and by
`selftest()` (before/after equality).  No tail clause, no indent clause,
no `contains` clause exists, so none can be forged.  The byte comparison
is the right shape and it works — see probe 7.  Clean.

### 4. PHANTOM CONSUMERS — **PRESENT**

Three separate instances, all measured:

**(a) The verbatim anchors name a consumer gate that is never checked.**
`G-ANCHORS`' statement says each anchor "names the gate that consumes
it", but its predicate is only `match_needle(...) and len(canon(nd)) >=
NEEDLE_FLOOR`.  **Injection CINJ-A**: V01's consumer changed to
`G-NO-SUCH-GATE-AT-ALL` → `verify-paper: PASS (37 gates)`, exit 0.

**(b) Three sealed "vouching" keys are consumed by no gate.**
`R["standards"]` (the nine engravings this run vouches for by number),
`R["totals"]` (mutants/sources/window/dictionary_rows/dead_arms/…) and
`R["measure_stamp"]` (E-24's `COUNTING-ONLY`) are sealed and published;
`grep` finds no gate reading any of them.  In particular `totals`
publishes `sources: 15` and `mutants: 30` while §14 *types* "15 sources"
and "30 declared mutants" in prose — and both prose numbers can be moved
(→ 18, → 27) with every gate passing, because nothing compares the
sentence to the registry.

**(c) Six waiver forcings are untrue** — see MAJOR-6.

### 5. HONEST DENOMINATORS — **PRESENT**

| gate | stated denominator | measured |
|---|---|---|
| `G-PAPER-CLAIMS` | "every data row of every published table" | **75 of 131** data rows, across 6 of 13 tables |
| `G-WALL-SCAN` | "every published receipt key together with the statement and evidence of every non-wall gate evaluated" | **23 of 41** published keys; **27 of 40** gate rows |
| §14 prose | "15 sources", "30 declared mutants" | correct today, typed and ungated |
| `G-COVERAGE` | "the run's own gate count" | honest (37), but 15 of the 37 are excused by waiver and **5 of those 15 forcings are untrue** (a sixth, `G-SWEEP-EXECUTED`'s, is untrue among the closing gates) |

The 56 unrendered data rows are: §2.3 carriers (3), §4.1 the fate/free-item
summary (2), §4.4 the dead arms (5), §5.1 the compatibility census (16),
§7 the by-k table (4), §8 the sterility control (10), §11 the choice
inventory (16).  Every one of them is forgeable — measured, not inferred:
I flipped a `COMPATIBLE` to `SEAM-DEFORMED`, moved a compat cell 6→4,
moved the sterility control's `|Aut|` from 3359232 to 62208, moved
"realised pairs" 54→53, moved the k=3 doubled-free count 2970→1134, and
demoted choice item 8 from "declared, VERDICT-DETERMINING" to "forced" —
**all six survive**.

### 6. WALL SURFACE — **PRESENT** (receipt leg); UNSEALED-KEY FORGERY — **PRESENT**

`G-WALL-SCAN` builds its scanned surface from `R.items()` **at the moment
the wall gate runs**, which is before the verdict is built.  The seal
order puts **24 keys before `walls` and 12 after** — `verdict`,
`reconstruction`, `standards`, `totals`, `paper_claims`, `paper_gates`,
`coverage`, `ledger`, `gate_count`, `measure_stamp`, `schema_version`,
`mutant_sweep` — and `provenance` is excluded by name, leaving **23 of 41
published keys scanned**.  Likewise the gate-row leg scans the 27 rows
emitted before the wall and none of the 13 after.

**Injection CINJ-D**: the sentence *"the union is read here as a spacetime
with a cosmological horizon"* planted in `G-VERDICT-RECON`'s statement — a
gate emitted after the wall — gives `verify-paper: PASS (37 gates)`,
exit 0, with `receipt_hits: []`.

Honest counterweight: the **head is not exposed**, but only indirectly.
**CINJ-C** appended `SPACETIME` to seg3 *and* to both fence copies in the
paper; it died — at `G-WALL-SCAN`'s **paper** leg, because the head is
rendered into the paper and the paper is scanned.  So the receipt leg's
blindness is real, its stated denominator is false, and the head happens
to be caught by a different leg.

**Unsealed-key forgery.**  The four declared-unsealed keys are `swept`,
`seal_manifest`, `ledger_chain`, `mutant_sweep`.  `G-SWEEP-EXECUTED`
binds `swept` — a **boolean handed in by the caller**, not evidence.  I
called `finish(..., write=True, swept=True)` on a run that executed **no
sweep at all**: both artifacts were written, `ok=True`, and the receipt
publishes `"swept": true` with no `mutant_sweep` key.  `--numbers` does
the same by design (`swept=swept or numbers`).  `ledger_chain` is bound
by nothing.

### 7. CLOSING-GATES WARRANT + READ-BACK — corruption **ABSENT**, warrant **PRESENT**

The write path is tmp → `os.replace` → read back from disk → compare to
the in-memory render.  **Injection CINJ-E** monkeypatched `os.replace` to
append `FORGED-AFTER-REPLACE` after the real replace: the run **died at
`G-INTEGRITY`**, no all-PASS transcript was promoted, exit non-zero.  The
disease the probe hunts is not present.

Four residuals, all measured:

1. **The corrupt bytes are left on disk.**  After the death both
   artifacts still carry the forged marker; there is no rollback and no
   removal.
2. **The "deliberately corrupted probe" is constant-true.**
   `probe_ok = sha256(txt+"x") != sha256(txt)` cannot be false.  E-23
   names constant-boolean legs; this is one, inside the gate whose waiver
   rests on it.
3. **`G-INTEGRITY` never consumes a seal.**  It compares disk bytes to
   the in-memory `txt`/`payload`, which are rendered from `R` *as it
   stands at write time*.  The 37 gate-time digests are published and
   never compared to anything (MAJOR-4).
4. **The receipt cannot reconcile its own chain.**  `R["ledger"]` carries
   37 rows ending at `f9594edb93b89943`; `R["gate_count"]` is sealed as
   37; the delivered transcript carries **40** rows and the published
   `ledger_chain` is `bbfdfb9f2112f96b`, the head after the three closing
   gates the receipt does not publish.  A receipt-only verifier sees a
   chain head that does not belong to the chain it was given.

### 8. SPELLED NUMERALS — **PRESENT** (scanned, but only for backing)

`paper_spelled` scans a **16-word dictionary** and asks only that the
integer be *somewhere* in the registry.  Measured:

- `fifty-four` → `eighty-one`: SURVIVES (81 is backed — it is the k=1
  gluing count).  Same for `nineteen`, `thirty`.
- `fifty-four` → `fifty-three`: SURVIVES — `fifty-three` is not a
  dictionary key, and the `fifty` key cannot match inside it.
- Every spelled numeral **at or below twelve is unscanned by design**:
  "The record fixes **six of the ten** entries of the seam's form" →
  "**nine of the ten**" SURVIVES, contradicting the unit's own kernel-4
  result in the sentence directly above its verdict fence.

Alongside it, a digit-side blind spot with the same effect: `NUM_RE`'s
`(?![\w.])` lookahead makes **a numeral immediately followed by a period
unscannable**.  §7's closing "…the largest automorphism group in the
family at **62208.**" → `62209.` SURVIVES; so does §2.1's "positive
definite at 9 of **9.**" → "of 8.".  Of the 1358 digit runs in the paper, `NUM_RE` returns 1169 tokens and
**182 digit runs are covered by no token at all**; 148 of those lie
outside fenced blocks.  Most are identifiers (`paper-19`, `I7`, `v14`,
sha digests, section numbers) and the fenced ones are protected by
`G-PAPER-FENCE`'s verbatim match — but the two above are published
measurements sitting in the blind spot.

### 9. SENTENCE-LEVEL REFERENT BINDING — **PRESENT**

Planted verbatim before §13 and passing every gate:

> At the aligned seam the union carries 16 undetermined entries on 45010
> shared cells, and 2970 of its 42336 gluings are refused by the
> committed grammar.

Four numerals from four different universes (types, gluings, doubled-free
gluings at k=3, k=3 population), each individually backed, composed into
a sentence contradicting the receipt on every clause.  This is the
LOR/AID disease intact.

---

## MAJORS

### MAJOR-1 — the paper leg does not bind: twelve forgeries at 37/37, exit 0

One paper, twelve independent forgeries, `--verify-paper` →
`PASS (37 gates)`, exit 0, tree hash unchanged (`be5f8dd76fbd` before and
after):

1. §4.1's two rows swapped, so doubled-free types read `UNMOTIVATED` with
   free item `I-DIRECTION-LABEL` at fiber 9 and doubled types read
   `FOUND-candidate` — **the unit's central result inverted**;
2. a forged head, `SEC-NEVER-WELDS-[THE UNION CARRIES NO DICTIONARY AT
   ANY TYPE]`, in a fenced block opened as ```` ```txt1 ````;
3. the cross-universe sentence of probe 9;
4. R1's quoted theorem inverted: "**copy** a block, not divide one";
5. `62208.` → `62209.`;
6. the ALIGNMENT CRITERION inverted ("no shared pair" → "some");
7. "every admitted one kills the dictionary" → "**no** admitted one";
8. §14's "15 sources" → "18 sources";
9. §7's header `gluings`↔`doubled`, `bare fate`↔`welds`;
10. §5.1's `(3,(0,0,3))` verdict `COMPATIBLE` → `SEAM-DEFORMED`;
11. §8's `|Aut|, chain route` 3359232 → 62208;
12. "fifty-four pairs" → "eighty-one pairs".

Item 2 is **E-22's own disease reproduced**.  `paper_fences` matches
```` ```[a-zA-Z]*\n(.*?)``` ````: an info string containing a non-letter
(`txt1`) does not match, so the block is invisible to the multiset check,
and a forged head carrying no new numeral is also invisible to coverage.
The gate's statement — "the stray side admits no fenced block the run did
not generate, **whatever its prefix**" — is exactly what fails.

The instrument is not vacuous: my positive controls all fire — a swapped
census cell dies at `G-PAPER-CLAIMS`, a corrupted inline span
(`` `CONFLICT-GRID(g = 3, R = 7777)` ``) dies at `G-PAPER-COVERAGE`
(E-22's inline-span clause is genuinely in force), the naming sentence's
deletion dies at `G-WALL-NAMED`, the L-1 sentence dies at `G-WALL-L1`.

**Repair.** (i) render **every** data row of **every** table as a claim,
and render each table's **header row** as a claim too; (ii) make
`paper_fences` tokenise any ```` ``` ````-delimited block regardless of
info string, and gate the multiset by **equality**, not by
`got >= want`; (iii) extend `POLARITY` to every direction-bearing
headline sentence the head asserts (the seven flips tabulated in probe 2);
(iv) drop `(?![\w.])` from `NUM_RE` in favour of a boundary that admits a
trailing period, and admit negative numerals; (v) extend `SPELLED` to a
complete number-word grammar including one–twelve, and bind each spelled
numeral to **its own claim's** value rather than to registry membership.

### MAJOR-2 — a published mechanism contradicted by the receipt's own rows

§4.3 states of `EXT-INCIDENCE`:

> One object per (division event, pair) splits a doubled pair into TWO
> site objects, **the induced field becomes identically 1**, and the
> structural test passes at every type including the doubled ones.

Measured, from `sec_receipt.json` itself, across all 16 types and both
readings:

| carrier | `field_values` | `count_cells` |
|---|---|---|
| `BARE` | `[1]` ×10, `[1, 2]` ×6 | 54 |
| `EXT-PAIR` | `[1]` ×10, `[1, 2]` ×6 | 54 |
| `EXT-INCIDENCE` | `[1]` ×10, `[1, 2]` ×6 | 54 |

The induced field at `EXT-INCIDENCE` is **`[1, 2]` at all six doubled
types**, identical to `BARE`.  This is not an accident of the run: the
code says so on purpose — "the count field is read on the SITE part of
the map in every carrier … no carrier extension changes what the record
counts."  The sentence describes a quantity the instrument computes and
publishes with a different value.

The head clause inherits it.  `EXT-PAIR-AGREES-WITH-BARE,
EXT-INCIDENCE-REPAIRS-EVERY-TYPE(FOUND-16-OF-16)` draws a contrast that
no measured row exhibits: **both** extended carriers are
`FOUND-STRUCTURAL` at 16 of 16 types at **both** readings, with identical
fields and identical cell counts; their only measured difference is
`site_arity` (66 vs 69) and the declared individuation of the target.
And the `FOUND` in `FOUND-16-OF-16` is the `FOUND-STRUCTURAL` **stamp**,
not a weld: deviation 4 honestly declares that the RSQ inventory and the
map count at the extended carriers are `READ-AT-BARE` and never computed,
so **no row anywhere shows `EXT-INCIDENCE` has zero free items**.

**Repair.**  Either compute the field on the subdivided carrier (and the
inventory with it) and publish what it is, or strike "the induced field
becomes identically 1" and restate the head clause as what was measured:
`EXT-PAIR AND EXT-INCIDENCE BOTH PASS THE STRUCTURAL TEST AT 16 OF 16;
THE INVENTORY IS READ-AT-BARE AND THE REPAIR IS NOT MEASURED`.  §4.3's
price paragraph (CHARTED individuation) is sound and should stay.

### MAJOR-3 — the read set is self-declared, so the LOR abstention is not gated

`G-SOURCES` asserts "the run's read set is exactly the declared set" and
`G-CITED-NOT-READ` asserts the cited-not-read path is "absent from the
run's read set … a measurement of what was read rather than a sentence
about it".  Both consume `reads`, which is built **inside the loop over
`SOURCES`** (`reads.append(rel)`).  `sorted(reads) == sorted(s[1] for s
in SOURCES)` is therefore **true by construction** and can never observe
a read taken anywhere else.

**Injection CINJ-B**: `read_bytes('v14/paper-30-lor.md')` executed at the
top of `full_run`, the very file the unit abstains from →
`verify-paper: PASS (37 gates)`, exit 0, with `G-CITED-NOT-READ`
reporting `violations: []`.  This is `G-READS-DECLARED`-positional-
vacuity (LOR MAJOR-4) recurring in a second unit.

**Did the abstention actually hold?**  Yes, on the evidence available to
me: `paper-30-lor.md` appears in the file only inside `CITED_NOT_READ`;
no other read of it exists; and no LOR sentence is quoted — the
extended-carrier lesson is anchored on V05, a real sentence of this
unit's own frozen pin.  **But the gate proves none of that**, and §1's
"the abstention is gated on this run's read set rather than announced" is
therefore a claim the instrument does not support.  Since LOR is terminal
now, the abstention costs the unit nothing substantive.

**Repair.**  Make the read set an observation: route every file open
through one accessor that appends to a module-level list, gate that list,
and additionally gate `open`/`read_bytes`/`read_text_file` call sites by
AST scan (the AST machinery is already present for `G-EXACT`).

### MAJOR-4 — the gate-to-disk seal is published but never verified

`Seal.seal()` digests each key at gate time and the manifest publishes 37
digests.  **No gate ever compares a digest to the value that is written.**
`G-SEAL-COMPLETE` checks key *presence* only; `G-INTEGRITY` compares disk
bytes to the in-memory render.

**Injection**: after `full_run` returned, I set
`R["type_census"][0]["aut"] = 424242` and `R["sterility"]["aut"] =
424242`, then called `finish(...)`.  Result: `ok=True`, `424242` present
in the rendered transcript, and `manifest["sealed"]["type_census"] !=
digest(R["type_census"])` — the receipt ships a seal that contradicts the
payload it seals, and nothing looks.  This is precisely the R4b failure
mode #119 was bought for ("satisfied at gate time, vacated at delivery
time"); §14's "the integrity gate compares disk bytes against the
gate-time seal" is not what the code does.

**Repair.**  Before rendering, assert `digest(R[k]) ==
manifest["sealed"][k]` for every sealed key, as a gate; then render from
the verified `R`.

### MAJOR-5 — five verbatim anchors are verified on the wrong side

The eight anchors check that a needle occurs **in the pinned source**.
Nothing checks that the **paper's** rendering of the same sentence
matches.  All five block quotations in the paper can be inverted freely:

| paper quote | injected | fate |
|---|---|---|
| "1,296 site assignments carry the record's co-division incidence **onto**" | "…**into**" (EMBEDDING → QUOTIENT) | SURVIVES |
| "records, and I7 declares **none** of them" | "declares **every one** of them" | SURVIVES |
| "must **divide** a block, not copy one" | "must **copy** a block, not divide one" | SURVIVES |
| "the carrier **may need** pairs" | "may **never** need pairs" | SURVIVES |
| "**no** Lorentz-invariant finite-valency graph" | "**every** Lorentz-invariant…" | SURVIVES |

Row 3 inverts R1's copy-forcing theorem — the theorem the k=0 arm exists
to confirm.  Separately, that quotation is rendered with an editorial
substitution ("[a refinement family that answers R1's question]") which
the anchor never sees, so the paper's blockquote is not verbatim anything.

**Repair.**  Make each anchor a two-sided gate: needle ∈ source **and**
needle ∈ paper, under `canon`.  Six of the eight already have the paper
text available in the same run.

### MAJOR-6 — six waiver forcings are untrue

§14 claims "Every gate is falsified by one of the 30 declared mutants,
each dying at its own named gate, or waived with a forcing."  Five
waivers name a mutant that **provably dies at an earlier gate and never
reaches the gate it is said to falsify** (gate order from
`--list-gates`, death gate from the out-of-harness sweep):

| waived gate (#) | named falsifier | where it actually dies (#) |
|---|---|---|
| `G-AUT-ROUTES-UNION` (13) | MUT-AUT-ROUTE | `G-AUT-ROUTES` (8) |
| `G-SEED-RULE` (17) | MUT-MENU-MEMO | `G-MENU-PURE` (16) |
| `G-CONTROLS` (19) | MUT-DICT-FATE | `G-DICT` (18) |
| `G-SEAM-CROSS-ALGEBRA` (23) | MUT-SEAM-RANK | `G-SEAM-RANK` (21) |
| `G-CONTRAST` (27) | MUT-STERILITY | `G-STERILITY` (26) |

The sixth: `G-SWEEP-EXECUTED`'s waiver reads "it is re-taken at the
integrity gate, so a run reaching the writer without a sweep dies twice."
It is not re-taken — `G-INTEGRITY` compares digests — and I wrote both
artifacts with `swept: true` and no sweep at all (probe 6).

`G-CONTROLS` is doubly exposed: its last two legs test only `"DEAD" in
fates[3]` and `"DEAD" in fates[4]`, so the published two-readings
signature (STRUCT-DEAD under EMBEDDING, COUNT-DEAD under QUOTIENT) is not
bound — and swapping those two readings in §4.4's table survives the
paper leg as well.

**Repair.**  Give each of the five a mutant that fires **after** the
earlier gate (e.g. a union-route poisoner, a seed-rule fate flip, a
dead-arm fate forgery, a cross-algebra rank shift, a contrast field-value
forgery); bind `G-CONTROLS` to the exact fate strings; and bind
`G-SWEEP-EXECUTED` to the sweep rows rather than to a boolean.

---

## MINORS

1. **`mutant_sweep` is declared unsealed and sealed.**  `full_run` calls
   `declare_unsealed("mutant_sweep", …)`; `main` then calls
   `seal("mutant_sweep", …)`.  The delivered manifest carries the key in
   **both** dictionaries, so "sealed or declared unsealed" is not a
   partition.  (Counted honestly, the object is 37 sealed + 4 declared
   unsealed with one overlap: 40 distinct published keys plus `swept`.)
2. **The `--mutant` exit convention is inverted**: on target → exit 1,
   off target → exit 0 (`return 1 if got == want else 0`).  Any wrapper
   using shell truth reads a correct sweep as 30 failures and an
   off-target mutant as success.
3. **Head literals are typed, not derived**: `UNION CARRIERS %d..%d` is
   filled with the constants `15, 18`; `STRUCT-ALIVE-16-OF-16`,
   `COUNT-POSITIVE-16-OF-16`, `SITE-FIBER=1-AT-16-OF-16`,
   `FOUND-16-OF-16`, `RANK 6 ON THE 10 ENTRIES`, `(4,3,2,1,0)` are typed
   into the segment strings.  The comparator re-derives the outcome word,
   the motivated count, `seam_kernel_4` and sterility — not these.
4. **`contrast["seam_undetermined_entries"] = 4 * 3`** is a typed
   product, published in the head as "THE SEAM CARRIES 12 UNDETERMINED
   ENTRIES".  Correct, but not measured from the three seam rows.
5. **E-24 is a self-list.**  `measure_stamp` is sealed and read by no
   gate; §10's stamp sentences invert freely ("This unit publishes no
   probability and no percentage" → "publishes a probability for every
   gluing"; "stamped COUNTING-ONLY" → "stamped MEASURE-DECLARED") with
   every gate passing.  Substantively E-24 *is* honoured — no probability
   is published, every ratio carries its denominator — but the stamp
   binds nothing.
6. **Two falsifiers flip the finding rather than create the disease.**
   `MUT-CITED-READ` inverts `cnr_bad` itself; `MUT-WALL-SCAN` appends a
   string to `measurement_layer` after it is built.  Both die honestly at
   their gates, and neither can reach the disease its gate is owed —
   the LOR #269 caveat of record, inherited intact.  (I checked all 31
   mutant activation sites against their published descriptions: **30/30
   descriptions are accurate**; there is no description-inverted mutant.)
7. **`--verify-paper <path>` accepts any path on the filesystem**, inside
   or outside the repo, and publishes it as `R["paper"]` via
   `os.path.relpath`.  Harmless for a verifier mode, but the run's
   `paper` key is then not `PAPER_REL` and no gate objects.
8. **`G-GLUING-CENSUS`'s "second route with no shared code"** is
   `(C(9,k)/k!)·P(9,k)` computed with `c` and `p` as the *same* product
   loop written twice in one function.  The route is genuinely different
   from the enumeration and it agrees; the "no shared code" phrasing
   overstates a five-line closed form living beside its comparand.
9. **`--numbers` sets `swept=True` without a sweep** to satisfy
   `G-SWEEP-EXECUTED`.  It writes nothing, so no artifact is affected,
   but the gate is passed by declaration in a second place.

---

## E-22 / E-23 / E-24, ITEM BY ITEM

**E-22 — inline-span coverage; blocks by multiset; tables render as
claims.  PARTIAL (2 of 4 clauses fail).**

| clause | verdict | evidence |
|---|---|---|
| inline code spans covered | **HOLDS** | `` `CONFLICT-GRID(g = 3, R = 7777)` `` dies at `G-PAPER-COVERAGE`; nothing is stripped before the scan |
| fenced blocks covered | **HOLDS for plain fences** | a forged twin of a verdict fence is a `stray` and dies |
| blocks by **multiset**, whatever the prefix | **FAILS** | `paper_fences` matches ```` ```[a-zA-Z]*\n ````, so a fence opened ```` ```txt1 ```` is invisible; and the missing-side test is `got[k] < want[k]`, so extra copies of a legitimate fence are admitted (containment, not equality) |
| **all** table rows render as claims | **FAILS** | 75 of 131 data rows; 0 of 13 header rows |

**E-23 — falsifier honesty.  HOLDS on descriptions; two structural
residuals.**  I read all 31 mutant activation sites and compared each to
its published description: **30/30 accurate**; no description-inverted
mutant; every one is a real object or flag corruption reaching a real
predicate; the sweep confirms 30/30 die at the declared gate.  Residuals:
(i) `G-INTEGRITY`'s "deliberately corrupted probe" leg,
`sha256(txt+"x") != sha256(txt)`, is a **constant-true boolean** — the
exact shape E-23 bars; (ii) two falsifiers flip the gate's own finding
rather than create the disease (MINOR-6), and six load-bearing rows rest
on waivers whose forcings are untrue (MAJOR-6) — E-23's "a row with
neither a falsifier nor a named waiver with a forcing is unguarded"
applies to `G-CONTROLS`, `G-SEED-RULE`, `G-AUT-ROUTES-UNION`,
`G-SEAM-CROSS-ALGEBRA`, `G-CONTRAST` and `G-SWEEP-EXECUTED`.

**E-24 — measure-relativity of counts.  HOLDS in substance; a self-list
instrumentally.**  The unit publishes no probability and no percentage; I
checked every ratio in the paper (welding types/types, welding
gluings/gluings, doubled-free by k, FORCED window records, admitted cross
specifications) and each is a count over an exhaustive enumeration with
its denominator written beside it, with no measure declared on the gluing
family and the non-uniformity explicitly disclaimed in §10.  The
`COUNTING-ONLY` stamp is present where claimed.  But `measure_stamp` is
read by no gate and §10's stamp sentences invert freely (MINOR-5), so the
stamp is a list the unit keeps about itself rather than a binding.

---

## WHAT I VERIFIED THAT HOLDS

Recorded in full, because a green sweep is not evidence a wall holds and
the converse is also true — several of this unit's walls do hold.

- **Byte reproduction, exact, three times, two hash seeds, off-tree and
  git-less.**  A full delivery in a git-less rsync mirror, and two more
  in a 20-file minimal tree with no `.git` present at
  `PYTHONHASHSEED=0` and `PYTHONHASHSEED=1729`, each reproduced both
  artifacts byte-for-byte: `sec_output.txt` **`e80d2f08a257`** (26,809 B)
  and `sec_receipt.json` **`fdf66d990dbf`** (157,489 B), identical to the
  committed objects.  The #91 clause holds, and the d60 hash-seed
  exposure does not bite here.
- **Out-of-harness mutant sweep**, one process per mutant, 30 cold trees:
  **30/30 died at their declared gate**, every tree byte-unchanged
  (`2677a2f3b337` before and after each).  (Method note of record: my
  first sweep attempt raced a duplicate of itself on shared directory
  names and produced seven spurious `tree changed` rows; both runs were
  killed and the sweep redone from clean trees with unique prefixes.  The
  30/30 above is the clean run.)
- **The ledger chain recomputes from bytes.**  I rebuilt the chain from
  `sha256(b"SEC-LEDGER-GENESIS")` forward, digesting each row's
  `{gate, ok, statement, evidence}` myself: **37/37 per-row agreement**,
  head after `full_run` = `f9594edb93b89943`, head after the three
  closing gates = **`bbfdfb9f2112f96b`**, the published value.
- **Selftest writes nothing**, proved by tree hash: died at `G-SOURCES`,
  `artifacts unchanged=True`, tree `2677a2f3b337` → `2677a2f3b337`.
- **CLI contract**: 13 hostile argv (unknown flag, unknown mutant,
  unknown anchor, missing argument, flag-shaped argument, `--flag=value`,
  `-h`, two modes, repeated mode, non-existent path, a directory) — all
  exit 2, tree unchanged.
- **Every measured number I recomputed independently reproduced.**
  45010 = Σ C(9,k)·P(9,k) over k≤3 (1 + 81 + 2592 + 42336); the 16 type
  populations sum to it per k; doubled-free 1134 at k=2 by the
  same-part/different-part split (9·72 + 27·18) and **2970 at k=3** by
  the three A-patterns (3·504 + 54·18 + 27·18) and again by
  inclusion–exclusion (1512 + 1512 − 54) — matching the head's closed
  reading exactly; 4186 total, and independently as the sum of the ten
  welding types' gluings; |Aut| at k=0 = 1296²·2 = 3359232; 54 gluings at
  `(3,(0,0,3))`; E = 54/53/52/51 by doubled count; carriers 18−k; the
  seam's rank 6 / kernel 4 from the two 2-dimensional chart blocks; the
  direct-sum minors 1, 3/4, 3/4, 9/16 (aligned, q₁₂ = −1/2) and 1, 1, 1, 1
  (triangle, q₁₂ = −1); the (4,3,2,1,0) cross-link ladder; 12 = 4·3.
- **E-22 inline spans are genuinely covered** — a corrupted backticked
  numeral dies at `G-PAPER-COVERAGE`; nothing is stripped before the scan.
- **The `#125` normaliser is real** — the L-1 sentence dies when injected,
  and the seam-naming sentence's deletion dies, both under whitespace,
  ASCII-fold and markdown-prefix normalisation.
- **`G-EXACT`** finds no float constant, no `float()`/`eval()`, and no
  `subprocess`/`socket`/`urllib` import; the run needs no VCS.
- **Post-`os.replace` corruption is caught** (probe 7).
- **The declared-window disclosure is honest**: 32 records is named
  inside the arena verdict string, and the driven-versus-combinatorial
  equality that licenses the exhaustive columns is measured at 26 of 26.
- **`swept` aside, the delivery path really does sweep**: `main` runs all
  30 mutants in process and refuses to write if any is off target.

---

## WHAT THE PANEL SHOULD NOTE ABOUT SHAPE

Five of the six majors are **template-shaped, not SEC-shaped** — they are
the #267/LOR diseases recurring in a sibling unit built from the same
template: unrendered table rows (LOR M2), positionally vacuous read-set
gate (LOR M4), typed totals-counts (LOR M3), the wall's false scanned
denominator (LOR M1's cousin: the wall does scan the paper here, but its
receipt leg covers 23 of 41 keys), and untrue waiver forcings (LOR's
MINOR, six times here).  MAJOR-2 and MAJOR-4 are SEC's own.  If the
corpus sweep recommended at #267 is run, `paper_claims` coverage of table
rows, `paper_fences`' info-string regex, the `reads` accessor and the
seal-verification gate are the four edits that would close most of it
corpus-wide.

**Every ruling above is a candidate reading until adjudication.**
