# POT (paper-36) — K3 INSTRUMENT-LENS REVIEW

**Seat:** K3, instrument lens, three-seat hostile panel.
**Verdict:** **ACCEPT-WITH-FIXES (AWF).**
**Status of every finding below: candidate until adjudication.**

**The object, sha256-12 verified at open and again at close (unchanged
across the review; every mutation ran in an rsync mirror under scratch):**

| object | sha256-12 | lines |
|---|---|---|
| `v14/paper-36-pot.md` | `173a88d8755f` | 633 |
| `v14/code/pot_exact.py` | `8c11f16002d1` | 4156 |
| `v14/code/pot_output.txt` | `50f295f31b67` | 71 |
| `v14/code/pot_receipt.json` | `5b5f731fb615` | 5512 |
| `v14/note-pot-pin.md` (pin) | `df2f15efa7b0` | 116 |

**Counts.** 125 process executions; 51 live injections of my own design
plus the 49 declared mutants swept one-process-each out of harness;
134 recomputations (29 physics/structure quantities on a foreign route,
12 digest recomputations, 39 claim-occurrence counts, 9 header/receipt-key
correspondences, 44 anchor-consumption checks, 1 coverage denominator).
Repo writes: this file only.

**Why AWF and not R.** No false physics number was found. A foreign-route
re-implementation (my own Q(ζ₈) arithmetic, my own holonomy product, nothing
imported from `pot_exact.py`) reproduced 29 published quantities exactly,
including every headline: 640 coins in 512/64/64 sectors, 192 placements and
192 distinct loops at 144/48, 11 orbits at chart order 32 with 0 escapes and
16 at the extension, 9 of 16 simple shapes at extents {1,2,3}, area-blindness
at 0 disagreements over the *complete* pairwise equal-perimeter set, 0
closed-form failures over 640 coins with the halving coefficient splitting
512/128, spectrum {1,1,1/2} and gap 1/2, 11 distinct plaquette values, 13/10
at the null, 56 non-flat diagonal coins. The batteries the unit claims are
real: 49/49 mutants dead-on-target out of harness with the whole tree
byte-unchanged; 3/3 selftest anchor classes fatal at their own gates writing
nothing; byte ×2 off-tree and git-less at two `PYTHONHASHSEED` values
reproducing both delivered artifacts byte-identically; the 21 sealed objects
genuinely sealed; read-back before `os.replace` genuinely guarding.

**Why AWF and not A.** Ten majors, all on the delivery *harness* rather than
the measurement: the confinement licence wall licenses itself; table cells
carry no binding; the claim gate is a floor and not the "exact occurrence
count" the paper claims; the numeral registry admits every one- and two-digit
numeral; the twenty declared-unsealed receipt keys are forgeable at exit 0;
the transcript is forgeable; the honest denominator covers 38 of the 50 gates;
all fifteen verbatim anchors have phantom consumers; staging temporaries
survive a refusal. Four sentences of the delivered paper are false as
descriptions of the instrument and must be repaired or removed.

---

## 1. The nine probes

| # | probe | verdict | the injection that establishes it |
|---|---|---|---|
| 1 | UNBOUND HEADERS | **ABSENT** (headers) / **PRESENT** (cells) | 3 header swaps + 1 header deletion all die at `G-PAPER-HEADERS-BOUND`; the ANCHORED↔EXTENSION **row labels** swap passes at exit 0 |
| 2 | DIRECTION/VALUE FLIPS | **ABSENT** in the head / **PRESENT** in the body | head flips die at `G-PAPER-VERDICT-BLOCK`; `DECONFINES 24`→`96` and `FAMILY-INVARIANT`→`PARTITIONS-THE-INVENTORY` and `gap 1/2`→`gap 1/4` pass at exit 0 |
| 3 | THE 20 DECLARED-UNSEALED KEYS | **PRESENT** | 9 of the 20 forged at exit 0 (verdict, totals, gates re-chained, gate_digests, ledger_shape, provenance, exit_conventions, pin_sha256_prefix, paper_sha256_12) + seal_manifest and coverage; post-seal *insertion* is guarded |
| 4 | CONFINEMENT LICENCE WALL | **PRESENT** | "The theory confines at strong coupling." passes at exit 0; so does "It confines."; so does a licensed-looking sentence with wrong values |
| 5 | TRANSCRIPT INTEGRITY | **PRESENT** | a fabricated `[PASS] G-A-GATE-THAT-NEVER-RAN` line appended to `LOG` is delivered in `pot_output.txt` at exit 0 |
| 6 | PHANTOM CONSUMERS + waiver truths | **PRESENT** (verbatim) / **ABSENT** (path-value) | `vb` is passed to three measure functions and read by none; 0 of 15 verbatim anchors are consumed by their named gate; 29 of 29 path-value anchors are |
| 7 | READ-BACK / STAGING / `--no-write` | **ABSENT** (read-back, `--no-write`) / **PRESENT** (staging) | a byte-mangling disk simulation dies at `G-ARTIFACT-INTEGRITY` with artifacts unchanged — and leaves `pot_output.txt.tmp` + `pot_receipt.json.tmp` behind |
| 8 | SPELLED NUMERALS | **PRESENT** | "twenty-five … fifty" and "Seventeen … thirty" both pass at exit 0; the content leg of the gate is unreachable |
| 9 | REFERENT BINDING | **PRESENT** | "The 136 couplings this arena admits are one per class, and the 149 extreme points … were all swept." passes at exit 0 |

---

## 2. Majors

### MAJOR-1 — the confinement licence wall licenses itself

`CONFINEMENT_WORDS` contains `"confines"` and `"deconfines"`; the licence set
built at `measure_paper` adds the class words `"CONFINES"` and `"DECONFINES"`
(and `"AREA-BLIND"`, `"FAMILY-INVARIANT"`, …); the test is
`any(tok.lower() in sl for tok in licence)` — substring containment against
the lower-cased sentence. Every sentence that uses the policed word therefore
supplies its own licence.

- **Injection P4a:** append to §4 — `The theory confines at strong coupling.`
  → **exit 0**, both artifacts rewritten, `G-THE-CONFINEMENT-LICENCE-WALL`
  reports `0 unlicensed`.
- **Injection H-LICENCE-SELFWORD-MINIMAL:** `It confines.` → **exit 0**.
- **Injection H-LICENCE-DECONFINES-FALSE:** `Every coupling on this arena
  deconfines and the static potential is flat.` — flatly contradicting the
  unit's own measurement — → **exit 0**.
- **Control (the wall is not wholly dead):** `The theory exhibits confinement
  at strong coupling on this arena.` and `This arena has an area law and a
  string tension.` both **die** at the wall (`1 unlicensed`). The hole is
  exactly the two words that are simultaneously policed and licensed.

The pin's wall is *"every confinement word in prose must sit in a sentence
carrying its measured discriminator value"*. For the two load-bearing words
that requirement is unenforced.

**Fairness note.** The *delivered* paper does not exploit this: of its 9
non-declaring confinement sentences, 7 are numeral-backed and the 2
class-word-only ones are table blocks. The defect is gate strength, not a
delivered falsehood.

**Repair (liftable).** Build the licence set as
`licence -= {t for t in licence if any(w in t.lower() for w in CONFINEMENT_WORDS)}`
after populating it, and require at least one *numeric* licence token per
policed sentence (`any(t.isdigit() and t in s for t in licence)`), with the
table-block sentences either exempted by an explicit declared marker or
re-rendered as claims.

### MAJOR-2 — the wall accepts a licensed-looking sentence with wrong values

The wall tests *presence* of any licence token, never that the value is the
one this run measured for that claim.

- **Injection P4b:** `The area leg is AREA-BLIND at 96 of 149 measured rows
  and the winding leg DECONFINES at 40 of 136 extreme points.` (the delivered
  measurement is 149 of 149 and 96 of 136) → **exit 0**.

**Repair.** Bind each policed sentence to a rendered claim: require the
sentence to contain at least one full claim string from `build_paper_claims`,
not merely a token from the registry.

### MAJOR-3 — the numeral registry admits every one- and two-digit numeral

`receipt_number_registry` walks the whole payload and collects every digit
run. Measured over the delivered receipt: **314 tokens, containing all 10
single digits and all 90 two-digit tokens**; only 102 of 900 three-digit
tokens. `G-PAPER-NUMERALS-COVERED` therefore has teeth only at ≥3 digits.

- **Confirmed live at 3+ digits:** `150` in prose and `` `4242` `` in an
  inline span both die (E-22 inline-span coverage is real).
- **Confirmed vacuous at ≤2 digits:** every headline count of one or two
  digits (24, 96, 40, 72, 11, 16, 32, 64, 79, 2, 9, 5, …) can be written to
  any other one- or two-digit value without the gate noticing.

**Repair.** Register numerals as *(value, context)* pairs — e.g. the tokens
that appear in rendered claim strings and table cells as emitted — rather than
as a flat set of digit runs; or forbid bare ≤2-digit numerals outside rendered
claims and table cells that are themselves rendered.

### MAJOR-4 — "claim rendering at exact occurrence counts" is a floor, not an equality

`c["covered"] = c["hits"] >= c["need"]` with `need = 1` for all 39 claims,
while **13 of the 39 occur 2–3 times** in the delivered paper (C-FAMILY 2,
C-FAMILY-SPLIT 2, C-ORBITS 2, C-ESCAPES 3, C-SPECTRUM 3, C-EXTREME 2,
C-PRICE 3, C-PRICE-C 2, C-PRICE-B 2, C-DOOR 2, C-DOOR-UNITARY 2,
C-ORIENT-ODD 2, C-ORIENT-ROWS 2). Any duplicate occurrence may be corrupted.

- **Injection P2e:** one of the three `spectrum {1,1,1/2} and gap 1/2` sites
  changed to `gap 1/4` → **exit 0**; the paper now states two different gaps
  and the receipt still says `1/2`.

§13's sentence *"claim rendering at exact occurrence counts"* is false as
delivered.

**Repair.** Compute `need` from the paper's own clean text once and gate
`hits == need` (equality), or set `need` to the measured occurrence count in
the licensed rendering and compare exactly. Either way the §13 sentence must
match whichever is implemented.

### MAJOR-5 — table cells are unbound; only headers and numeral membership are checked

`G-PAPER-HEADERS-BOUND` binds header rows by multiset (three swaps and one
deletion die). `G-PAPER-TABLE-ROWS-COVERED` only asks that each numeral in
each cell be somewhere in the registry. Non-numeric cell content — the
verdict words, the row labels, the class words — is bound by nothing.

Four injections, all **exit 0** with both artifacts rewritten:

- **P2f:** `| LEG-AREA | 1 | no | False 136 | FAMILY-INVARIANT |` →
  `… | PARTITIONS-THE-INVENTORY |`, i.e. the price table now contradicts the
  head, §8 and §14.
- **P2g:** `DECONFINES 24, DISCRIMINATOR-DEGENERATE 112` →
  `DECONFINES 96, …` (the target list's own probe; it does **not** die).
- **P1d:** the orientation-closure table's row labels ANCHORED↔EXTENSION
  swapped, so the paper now says the anchored reading carries 16 escapes at
  chart order 128 — contradicting its own prose two lines below.
- **E22-NEW-TABLE-ROW:** an entire fabricated row
  `| LEG-GHOST | 2 | yes | True 96, False 40 | PARTITIONS-THE-INVENTORY |`
  inserted into the price table.

**Repair.** Render every data row as a claim the way headers are rendered:
build the licensed row multiset from the receipt row objects and compare the
paper's data rows against it by multiset equality — the same machinery
`hdr()` already uses for headers, applied one level down.

### MAJOR-6 — the twenty declared-unsealed keys are forgeable at exit 0 (the ACT disease)

`G-THE-SEAL-IS-TOTAL` accounts for all 41 top-level keys (21 sealed, 20
declared). The 21 sealed keys are genuinely protected — forging
`price_binding["the_inventory"] = 999` after the seal gate dies with
`1 seal mismatches from disk`. The 20 declared-unsealed keys are not.

Forged after `G-THE-SEAL-IS-TOTAL` and before serialization, each at
**exit 0** with both artifacts written:

| injection | what the delivered receipt then says |
|---|---|
| I1 | `verdict` reads `…SPLITS-40-NONZERO-AND-96-ZERO…` while the paper's fence and the transcript both read 96/40 |
| I2 | `totals.anchors = 999`, `totals.gates_closed = 999` |
| I3 | every ledger row's `detail` rewritten and the chain recomputed — `chain_ok` still True from disk |
| I5 | `provenance[0].measured = "FORGED-AFTER-THE-SEAL"`, `agrees = False` |
| I8 | `pin_sha256_prefix` and `paper_sha256_12` set to `000000000000`; `exit_conventions.delivery = "0 always"` |
| H-SEAL-MANIFEST-FORGED | `seal_manifest = []`, `declared_unsealed = {}` |
| H-COVERAGE-FORGED | `coverage.uncovered = ["NOTHING-IS-UNCOVERED"]`, `clean_path_gates = []` |

Guarded, correctly: **inserting** a new top-level key after the seal dies at
`G-ARTIFACT-INTEGRITY` (`top-level keys identical False`), and mangled bytes
die there too. So the seam is value forgery of the declared-unsealed half,
not insertion.

The manifest's stated reasons overstate the protection. At least eight keys
have a real vouching gate available and are declared unsealed with a reason
that is a description rather than an impossibility:

- `provenance` — its reason literally names `G-SOURCES-AT-THEIR-PINNED-DIGESTS`,
  which is exactly the gate that should have sealed it (#148's R5 defect,
  verbatim).
- `verdict` — sealable at `G-THE-TWO-HEAD-LAWS-AGREE`.
- `verdict_head` — sealable at `G-THE-HEAD-IS-DERIVED`.
- `totals`, `coverage`, `waiver_ledger` — sealable at
  `G-COVERAGE-AT-AN-HONEST-DENOMINATOR`; the stated reason ("verified at the
  disk boundary by total byte comparison instead") describes a
  memory-vs-temporary comparison that binds these values to nothing.
- `transcript_head` — sealable once `LOG[0]` exists.
- `preregistered_heads` — the pin's own list, sealable at load.

Only `gates`/`gate_digests`/`ledger_shape`/`seal_manifest`/`declared_unsealed`
carry a genuine ordering impossibility, and even the ledger's protection is
defeatable by re-chaining (I3).

**Repair.** Seal the eight above at their named gates; add a second seal pass
immediately before `json.dumps` that digests the post-snapshot keys and
verifies them from the read-back bytes; and bind the ledger to an
out-of-band anchor (e.g. seal `ledger_shape.head` at the last in-ledger gate)
so a consistent re-chain no longer verifies.

### MAJOR-7 — the transcript is forgeable and its declared reason is not a protection

`out_text = "\n".join(LOG)`; `back_o == out_text` compares the temporary
against the in-memory string. Nothing binds `LOG` to any measured object.

- **Injection I6:** `LOG.append("  [PASS] G-A-GATE-THAT-NEVER-RAN :: forged
  into the transcript by K3")` → **exit 0**; the delivered `pot_output.txt`
  carries a PASS line for a gate that does not exist. `G-CONSUMER-REGISTER-IS-REAL`
  does not read the transcript, and no gate reconciles the transcript's PASS
  lines against `LD.ids`.

**Repair.** Add a gate that parses the transcript's `[PASS]` lines and
requires the multiset of gate ids it contains to equal `LD.ids` exactly, and
seal the transcript digest at that gate.

### MAJOR-8 — the honest denominator covers 38 of the 50 gates on the delivery path

`measure_totals` runs **before** the paper leg, so
`clean = LD.ids + CLOSING_GATE_IDS` is 38 entries. The delivery run closes
**50** gates (51 with the refusal-only one). Twelve gates sit outside the
denominator: the ten paper gates, `G-CONSUMER-REGISTER-IS-REAL`, and
`G-COVERAGE-AT-AN-HONEST-DENOMINATOR` itself.

Taken over *all* gates, two on the delivery path carry neither a declared
falsifier's target nor a registered forcing:

- **`G-PAPER-QUOTES-INSIDE-THE-WINDOWS`** — load-bearing and live: I planted a
  misquoted blockquote ("each **conjugated** where the boundary runs **with**
  the link's own direction") and it died there, `1 outside every pinned
  window`. It has no falsifier and no waiver, and the early denominator
  conceals that (E-23: *"Every load-bearing receipt row carries a falsifier or
  a named waiver with a forcing"*).
- **`G-COVERAGE-AT-AN-HONEST-DENOMINATOR`** itself.

§13's sentence *"whose denominator is every gate on the clean path and not
only the ones already closed"* is false as delivered.

**Repair.** Move the coverage gate to the end of the paper leg (or recompute
and re-gate it there), add a falsifier for
`G-PAPER-QUOTES-INSIDE-THE-WINDOWS` (a mutant that drops one window from the
comparison set), and give the coverage gate itself a `FORCINGS` entry.

### MAJOR-9 — phantom consumers: 15 of 53 anchors are consumed by nothing

Every anchor publishes a `consumer` column and
`G-CONSUMER-REGISTER-IS-REAL` checks that the named gate id occurs in
`LD.ids`. It does not check that the gate reads the anchor.

- All **29 path-value anchors are genuinely consumed** — each `PV-…` name is
  read outside its own table and enters a gate predicate. Clean.
- All **15 verbatim anchors are not**. `vb = measure_verbatim(...)` is passed
  into `measure_the_loop_observable`, `measure_the_discriminator` and
  `measure_declared_rows`, and the identifier `vb` appears at exactly six
  places in the file: three parameter lists, one assignment and three call
  sites. No `vb[...]` subscript exists anywhere. No gate predicate references
  any verbatim anchor.

The head matter's *"each bound to the gate that consumes it, where the
consumer is checked against this run's own ledger"* is therefore true only of
the second clause, and only for the path-value class.

**Repair.** Make each verbatim window actually enter its consumer's
predicate — e.g. `G-THE-MERGING-INDEX-LAW-REPRODUCED` should require that the
measured merging index be extractable from `vb["VB-ACT-BOUNDARY"]`'s located
text, and `G-THE-CONFINEMENT-LICENCE-WALL` should take its declaring-marker
list from `vb["VB-PIN-LICENCE"]`. Failing that, rename the column
`declared_consumer` and drop the "consumes" language from the paper.

### MAJOR-10 — staging temporaries survive a refusal

`write_out` writes `pot_output.txt.tmp` and `pot_receipt.json.tmp`, reads them
back, gates, and only then calls `os.replace`. The gate raising `GateFail`
leaves both temporaries on disk — there is no `try/finally`.

Observed in three separate refusals (I4, I7, I9): `artifacts_unchanged True`
(the read-back guard works, and this is the correct half), and
`stray_files ['pot_output.txt.tmp', 'pot_receipt.json.tmp']` left in
`v14/code/`. A refusing delivery run therefore does not "write nothing": it
leaves two files whose names differ from the artifacts by a suffix.

**Repair.** Wrap the staging in `try/finally` and unlink both temporaries on
any exit that is not a successful `os.replace`; and extend the `--selftest` /
mutant "artifacts unchanged" check to a directory listing rather than the two
artifact paths.

---

## 3. Minors

1. **`MUT-PAPER-SPELLED`'s content leg is unreachable.** Every one of the 17
   `NUMWORDS` values (13…136) is present in the receipt registry, so
   `spelled` is constant-empty and only the totality leg (`len(words) ==
   len(NUMWORDS)`) can fire. The mutant is a real three-legged falsifier of
   *that* leg, and its description ("leaves a spelled numeral out of the
   scan") is honest — but the gate's own claim, *"every spelled number-word
   the paper uses must have its value in the receipt's registry"*, cannot
   fail on this registry. Separately, the scan is confined to the 17 declared
   words: "twenty-five", "fifty", "eleven", "twenty-one", "thousand" and
   everything else are unscanned. Injections P8a and H-SPELLED-SEVENTEEN both
   pass at exit 0.
   *Repair:* scan for a general spelled-number grammar (units/teens/tens
   ± "hundred"/"thousand"), and require the resolved value to be in the
   registry.
2. **`MUT-MUSTNOT` kills through the declarer-count leg**, not the must-not
   content sweep (`decl = []` leaves the declaring sentences in `body`, which
   produces no forbidden hit; the kill comes from `declared_here >= 1`). The
   content sweep is separately live — planted "In the continuum limit …" and
   "640 metres" both die — so the gate is sound; the falsifier just does not
   exercise the sweep it is named against.
3. **`MUT-HEAD` has a dead second branch.** At `measure_totals`,
   `if mut("MUT-HEAD"): ok = verdict == second` assigns the same expression
   as the fall-through — a no-op. The real mutation is the row-list swap in
   `measure_the_verdict`; the dead branch should be removed (E-23: no
   constant-boolean shapes).
4. **Three mutant "tokens" are the switch line itself** (`if mut("MUT-REVERSAL"):`,
   `if mut("MUT-BASEPOINT") and …`, `if mut("MUT-CLOSED-FORM"):`), so E-23's
   *"names the exact token it plants"* is nominal for those three: the token
   located in the source is the switch, not the planted change.
5. **The nine licensed headers are typed, not derived.** `heads = [hdr(...) …]`
   is a hand-written literal. Eight of the nine correspond to a real receipt
   row object's keys; **one does not** — the L-boundary table
   `| quantity | at the declared L | at the boundary L |` has no row object in
   the receipt at all. Injection H-RECEIPT-KEY-RENAMED renamed
   `distinct_links` → `link_count_renamed` in the emitted rows and the header
   gate **passed at exit 0**, so the header binding is paper-vs-literal, not
   paper-vs-receipt. §13's *"rendered from the receipt keys its own columns
   are"* overstates it.
6. **`equal_perimeter_comparisons = 5760` counts self-comparisons.** The
   scheme compares every ladder shape to the least shape of its perimeter
   class, including the representative with itself: 9 shapes × 640 coins.
   Of the 5760, **3200 are a shape compared with itself** and 2560 are genuine
   cross-shape comparisons. The complete pairwise count is 3200. My foreign
   route ran the complete pairwise set: **3200 comparisons, 0 disagreements** —
   the finding stands, the denominator is inflated 2.25× over the genuine
   count. §5 and §14 both quote 5760. (The boundary count 44800 = 70 × 640 is
   honest — those are genuine area-discriminating pairs.)
7. **Delivery-record count drift.** LOG #324 records "589+17 numerals" and
   "252 sentences"; the live registries and the delivered receipt say
   **591 numerals** and **258 sentences** (`paper_binding.numerals_scanned`,
   `paper_binding.sentences`). The artifacts are right; the ledger entry is
   stale. The panel brief inherited both wrong numbers.
8. **E-24 stamping is partial.** Four receipt blocks carry
   `COUNTING-ONLY-E-24` (`classes`, `family_sweep`, `loop_family`,
   `price_binding`). `orientation_reading` publishes "96 of 136 extreme
   points" and "3760 of 11520 shape-by-coin traces" — the same
   counting-fraction shape — unstamped.
9. **`rerender_verdict`'s docstring** says it "reads ONLY the serialized
   receipt"; it reads the pre-serialization payload dict. The de-twinning
   itself is real (`%`-format vs `"".join`, `second_head_law` over tallies vs
   `head_law` over rows), but the comparator draws its *values* from the same
   receipt fields as the builder, so it guards rendering and staleness, not
   measurement. That is what it should be said to do.
10. **Flag precedence is silent.** `--verify-paper --mutant MUT-ARENA` takes
    the mutant branch and exits 0; `--selftest --no-write` takes the selftest
    branch. Harmless here, but undeclared.

---

## 4. Confirmed clean — the batteries, re-run by this seat

| battery | result |
|---|---|
| 49-mutant sweep, **one process each**, out of harness | **49/49 DEAD-ON-TARGET**; `pot_output.txt`, `pot_receipt.json` and the **whole tree** byte-unchanged across all 49 |
| `--selftest` | 3/3 anchor classes fatal at their own gates; **whole tree hash unchanged** |
| selftest isolation (disclosed repair #1), re-probed | reversing `ANCHOR_CLASSES` still gives 3/3 on target (order-independent); **removing the SOURCES/PATH_VALUES/VERBATIM restore** makes PATH-VALUE die at `G-SOURCES-AT-THEIR-PINNED-DIGESTS` (exit 1); **removing the `LD`/`SEAL`/`LOG` reset** likewise — the repair is load-bearing and verified |
| four redesigned falsifiers (disclosed repair #2) | `MUT-CLASSES` and `MUT-PAPER-NUMERAL` live and content-bearing; `MUT-PAPER-SPELLED` and `MUT-MUSTNOT` live but on their totality/declarer legs only (Minors 1–2) |
| byte ×2, off-tree, git-less, `PYTHONHASHSEED` 0 and 12345 | both artifacts **byte-identical** to the delivered ones (`50f295f31b67`, `5b5f731fb615`) |
| `--no-write`, `--verify-paper` | exit 0, **whole tree hash unchanged** |
| hostile argv (14 forms) | `--nowrite`, `--no-write=1`, `-no-write`, `--NO-WRITE`, `--mutant` (no name), `--mutant NOPE`, empty arg, trailing junk → **exit 2**; tree unchanged |
| E-22 fenced blocks by multiset | a second fence carrying `POT-DECONFINES-AT-EVERY-ROW` beside the clean one **dies** (`2 fenced blocks, 1 licensed`) |
| E-22 inline spans | `` `4242` `` **dies** at `G-PAPER-NUMERALS-COVERED` |
| E-22 headers | 3 semantic swaps + 1 deletion **die** at `G-PAPER-HEADERS-BOUND` |
| E-23 AST totality | planted float literal **dies** at `G-THE-ARITHMETIC-IS-EXACT`; planted helper **dies** at `G-THE-FUNCTION-INVENTORY-IS-TOTAL`; registry/description gates live |
| must-not sweep | "In the continuum limit …" and "640 metres" both **die** at `G-PAPER-MUST-NOT` |
| source anchors | one byte added to `act_receipt.json` **dies**; exchanging two parents' paths **dies**; absent paper → named refusal, not a traceback; duplicate gate id → named refusal |
| the seal, on its 21 objects | forging `price_binding.the_inventory` after the seal **dies** with `1 seal mismatches from disk` |
| read-back before `os.replace` | a byte-mangling write **dies** at `G-ARTIFACT-INTEGRITY` with artifacts unchanged |
| foreign-route self-digests | `code_sha256_12`, `paper_sha256_12`, `pin_sha256_prefix` in the receipt all match the delivered bytes; all 9 provenance rows verified expected == measured == actual by an outside route; the verdict string is identical across receipt, paper fence and transcript |

---

## 5. The foreign route

An independent implementation (own convolution-mod-(z⁴+1) product over
`Fraction` tuples, own full-matrix holonomy, own canonicalisation), importing
nothing from `pot_exact.py`, reproduced **29 of 29** attempted quantities
exactly:

alphabet 25 · admissible rows 80 · coins 640 · DIAGONAL 64 · ANTIDIAGONAL 64 ·
BALANCED 512 · unitary by an independent column route 640 · sites 16 ·
links 32 · plaquettes 16 · simple rectangle shapes 9 of 16 · extents {1,2,3} ·
placements 192 · distinct loops 192 · contractible 144 · winding 48 ·
anchored chart order 32 · anchored orbits 11 · anchored escapes 0 ·
extension chart order 128 · extension orbits 11 · extension escapes 16 ·
equal-perimeter disagreements 0 (at the complete pairwise count, 3200) ·
closed-form failures 0 over 640 coins · halving coefficient two values,
512 balanced / 128 diagonal+antidiagonal · spectrum {1,1,1/2} · gap 1/2 ·
distinct plaquette values 11 · counting expectation 13/10 · non-flat diagonal
coins 56.

**Zero false numbers found in the delivered artifacts.** The one arithmetic
divergence is a counting convention, not a value (Minor 6).

---

## 6. Paper sentences that must move

These four are false as written about the instrument and are the paper-side
half of the repair:

1. §13 — *"claim rendering at exact occurrence counts"* → the gate is a floor
   (MAJOR-4).
2. §13 — *"The coverage is published at an honest denominator (#34) whose
   denominator is every gate on the clean path and not only the ones already
   closed"* → 38 of 50 (MAJOR-8).
3. Head matter — *"each bound to the gate that consumes it"* → true of the 29
   path-value anchors, false of the 15 verbatim ones (MAJOR-9).
4. §13 — *"the structural binding of every table header as a claim rendered
   from the receipt keys its own columns are"* → typed, and one of the nine
   has no receipt row at all (Minor 5). §5/§14's "5760 comparisons" should
   either become 2560 (executed cross-shape) or 3200 (complete pairwise), with
   the self-comparisons named (Minor 6).

The head string, the physics headlines and every number in the verdict block
survive this review intact.

---

## 7. Method and scope

Every mutation ran in an `rsync` mirror (`.git` excluded) or in a 1.4 MB
minimal seed tree under scratch; each injection got its own copy, was run with
absolute paths, and the tree was deleted immediately. The repository was read
only, apart from this file. Interpreter `/opt/homebrew/bin/python3.13`.
Scratch peak 118 MB.

Not covered by this seat: the physics adjudication of the DECONFINES branch
semantics, the thinness of the L = 4 area leg (2 comparisons), the
declared-window/extension-escape scoping, and the uniform-carrier premise —
those are K1/K2 ground, and the unit itself names all four as soft spots.

**Between delivery and adjudication every headline above is a candidate
reading.**
