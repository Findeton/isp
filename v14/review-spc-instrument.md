# SPC (PAPER-37) — K3 INSTRUMENT-LENS REVIEW (CANDIDATE UNTIL ADJUDICATION)

**Seat:** K3, instrument lens, three-seat hostile panel.
**Authority:** HANDOFF-PROMPT.md §4/§9; RUNBOOK.md E-22 / E-23 / E-24; the #267 checklist.
**Object, sha256-12 verified AT OPEN and AT CLOSE, unchanged in both readings:**

| artifact | sha256-12 | open | close |
|---|---|---|---|
| `v14/paper-37-spc.md` | `1555d049d558` | ✓ | ✓ |
| `v14/code/spc_exact.py` | `6b399487f286` | ✓ | ✓ |
| `v14/code/spc_output.txt` | `dc6410c72036` | ✓ | ✓ |
| `v14/code/spc_receipt.json` | `3958fe51495b` | ✓ | ✓ |
| `v14/note-spc-pin.md` (pin) | `7f0b1e9d5071` | ✓ | ✓ |

The repo was read-only to this seat except this one file. Every mutation ran in an
rsync mirror of `v14/` (all twelve pinned sources live under `v14/`) under an
absolute scratch path; per-run trees were deleted immediately; scratch peak 196 MB,
final 25 MB, never above 5 G.

---

## GRADE: **ACCEPT-WITH-FIXES**

Two majors, both in the falsification surface rather than in the delivered numbers.
**The delivered object itself survived every recomputation I ran** — 223 rendered
claims at their exact counts, 165 data rows and 15 header rows all bound, 46 chained
ledger rows, 34 seals, 12 provenance digests, the paper/code/pin/transcript
self-digests, the verdict multiset, 0 float literals, 55/55 falsifiers dead on
target out-of-harness, byte-identical regeneration at two hash seeds off-tree.
**No false delivered number was found.** What is defective is what the instrument
would *catch* if the paper drifted, not what it published.

The two majors are: (1) **the ACT disease is PRESENT** — the manifest-totality leg
is evaluated once and never re-derived from the promoted bytes, so a top-level key
inserted after `G-SEAL-INTEGRITY` ships in the receipt at exit 0; and (2) **there is
no referent-binding gate**, though the pin demands one by name — a paper whose §4
headline contrast is inverted in prose delivers green with 46/46 gates passed and
its own corrupted digest sealed into the receipt.

---

## COUNTS

- **Instrument process invocations: 131**, of which **103 executed the full pipeline**
  (1 delivery run, 2 byte-×2 runs at two `PYTHONHASHSEED` values, 1 `--list-gates`,
  55 one-process-each falsifier runs, 3 self-test pipeline runs, 41 injection runs,
  2 argv runs that reach `run()`); 28 were early-exit hostile-argv forms.
- **Corruptions authored by this seat: 56** — 20 paper-text, 8 instrument-source,
  28 hostile-argv forms. **12 died at a named gate writing nothing** (≥8 required);
  **11 survived** and are reported below; the rest are argv refusals.
- **Independent recomputation batteries: 22**, covering **≈750 individually
  recomputed items** (165 data rows + 15 header rows + 223 claims + 46 chain rows +
  34 seals + 74 anchors + 62 consumer bindings + 55 falsifier tokens + 50 gate call
  sites + 43 path-values + 19 verbatim windows + …). **0 discrepancies.**

### Every claimed count verified from live registries, not from prose

| claim | verified | route |
|---|---|---|
| 49 gates (46 sealed-ledger + 1 receipt wall + 2 closing) | ✓ | AST: 50 `LD.gate` call sites, 50 distinct ids; 49 clean-path + 1 refusal-only |
| 50 with the refusal-only gate | ✓ | `--list-gates` prints exactly 50 lines |
| 34 sealed objects | ✓ | manifest recounted and each digest re-derived from the delivered receipt |
| 74 anchors = 12 + 43 + 19 | ✓ | source registries `SOURCES`/`PATH_VALUES`/`VERBATIM` |
| 55 falsifiers | ✓ | 55 `mut()` switches in the syntax tree; symmetric difference with the registry empty |
| 48 distinct target gates + 1 forcing = 49/49 waiver | ✓ | recomputed; the only two gates with no falsifier are `G-ARTIFACT-INTEGRITY` (registered FORCING) and `G-PAPER-PRESENT` (refusal-only registry) |
| 223 rendered claims | ✓ | each located at its declared occurrence count |
| 165 data rows + 15 header rows, all bound | ✓ | **recounted from the paper by the renderer's own separator logic, not from prose**: 165 / 15, 0 unbound in each class |
| 13 blockquotes inside pinned windows | ✓ | recounted, 0 outside |
| 1,244 numerals + 10 spelled, 0 unmatched | ✓ | receipt `paper_coverage`, cross-checked against the pool rebuilt independently |
| 4 walls, 16/17/16/7 banned forms, 0 found | ✓ | `WALLS` registry |
| 0 float literals | ✓ | **independent AST scan: 0 float constants, 0 complex, all `pow` 3-arg, one `**` on ints, one `/` on a `Fraction`; and 0 float-valued numbers in the delivered receipt JSON** |
| 49 published receipt keys = 34 sealed + 15 declared-unsealed | ✓ | 0 undeclared, 0 declared-but-absent |

---

## MAJORS

### MAJOR-1 — THE ACT DISEASE IS PRESENT: post-seal totality insertion is never re-checked

`seal_and_write` computes `unsealed = [k for k in payload if k not in SEAL.by_key and
k not in DECLARED_UNSEALED]` **once**, immediately before `G-SEAL-INTEGRITY`. Nothing
downstream re-derives totality. `G-ARTIFACT-INTEGRITY` runs `SEAL.reverify(back)`
(sealed objects only) and `raw_receipt == blob` — but `blob` is built *after* the
insertion point, so the "total byte comparison at the disk boundary" compares the
forged bytes to themselves.

**The injection establishing it (paired, so the window is exact):**

| injection | site | result |
|---|---|---|
| `payload["FORGED-BY-THE-REVIEWER"] = {...}` inserted **before** the `unsealed` computation | one line | **DIES at `G-SEAL-INTEGRITY`**, artifacts unchanged, no `.tmp` residue |
| the identical insertion placed **after** the gate, before `blob = json.dumps(...)` | one line | **SURVIVES: rc 0, receipt written with 50 top-level keys, the forged key present, never sealed, never declared, never swept by the receipt wall** |

The falsifier registry has the same asymmetry: `MUT-SEAL` covers *editing* a sealed
object after its gate (and my independent C5 — editing `payload["walls"]` after the
gate — correctly **dies at `G-ARTIFACT-INTEGRITY`**, so the read-back leg is real).
**Nothing covers *adding* a key after the gate.** The paper's §10 sentence "the
manifest is total … and the receipt crosses the disk boundary under a total byte
comparison so that the unsealed keys are guarded too" is, on this path, not true.

**Fix required:** re-derive `unsealed` from the bytes read back inside
`G-ARTIFACT-INTEGRITY` (`set(json.loads(raw_receipt)) ⊆ SEAL.by_key ∪
DECLARED_UNSEALED`), and add a falsifier that inserts a key after the seal gate.

### MAJOR-2 — NO REFERENT-BINDING GATE, THOUGH THE PIN NAMES ONE

The pin's WALLS section demands "the #267 checklist (headers bound; **sentence
referent binding**; spelled numerals; …); **REFERENT-BOUND gates**". There is no such
gate in the ledger. Prose outside the 223 rendered claims is constrained only by
`G-PAPER-NUMERAL-COVERAGE`, whose pool is *every integer this run computed anywhere*
— so numbers may be freely re-paired with the wrong referent.

**Four live injections, each delivering green (rc 0, nothing refused), run in
isolated trees:**

| injection | survives |
|---|---|
| planted sentence "The census hosts **156 of 220** species." (both numbers in the pool, wrong universe) | ✓ |
| planted sentence declaring the 220 inventory species and the 246 hostable species "one universe of 220 labels" | ✓ |
| §8: "the shape that leaks at 0 cells against 81 is the **antisymmetric** one" → "the **symmetric** one" — inverting the very sentence that says the shape is *derived and not typed* | ✓ |
| §4: "the nine actors under the whole symmetric group host **2 of 30** species" → "host **30 of 30** species" | ✓ |

The last one was then run as a **full delivery**: `rc 0`, artifacts written,
**46/46 gate rows passed**, and the receipt seals the corrupted paper's digest
`01e94f3994d0` as its own `paper_sha256_12`. The delivered paper then reads
"…host 30 of 30 species, **and 28 have no realization there at all**" — self-
contradictory, contradicting the carrier table three lines above it and the verdict
segment `…ACTOR-9-UNDER-S9-AT-2-OF-30` in the same file — and no gate notices.

The registered claims and the verdict fence are genuinely tight: the same flips
placed **inside** the verdict block or **inside** a table row all die (below). The
hole is exactly the unregistered prose.

**Fix required:** a `G-PAPER-REFERENT-BOUND`-class gate that binds each numeral to
its sentence's subject (minimally: render the headline contrast sentences of §4, §5,
§7 and §8 into `build_claims`, which would have killed all four injections above);
plus a falsifier planting a re-paired numeral.

---

## MINORS

- **m1 — the spelled-numeral alphabet stops at ninety-nine.** `NUMBER_WORDS` is
  `numword(k)` for `k ∈ [0,100)`; "hundred"/"thousand" are not words, so a compound
  is scanned only by its residue. Live: "The inventory carries **two hundred
  twenty** species." **survives** (residue "twenty" → 20, in the pool); "A planted
  count of **nine hundred sixteen**." **survives**; the control "**seventy-nine**"
  **dies at `G-PAPER-NUMERAL-COVERAGE`**. Disclosed in the receipt
  (`EVERY-ENGLISH-NUMBER-WORD-BELOW-ONE-HUNDRED…`) and the paper makes no claim
  about spelled numerals, so this is a scope gap, not a misstatement.
- **m2 — the paper-side digest whitelist is form-based, not digest-shaped.** The
  pool side uses `DIGEST_RE`, which *requires* an `a–f` character; the scan side uses
  a bare ``` `[0-9a-f]{12}` ``` substitution. A backticked all-digit twelve-character
  token therefore leaves the numeral scan entirely. Live: `` `987654321012` ``
  planted in a code span **survives**. This is the sharp form of the #267
  "digest-free whitelists" item.
- **m3 — blockquotes are bound to the *set* of pinned windows, not to the parent
  they are attributed to.** `unbound_quotes` asks only whether the quote lies inside
  *some* window. Live: swapping ACT's "The odd twist is not realisable on this torus"
  with AID's "Every admissible history of this census forces identity" — so each is
  introduced under the wrong parent — **survives**. Quote *fidelity* is enforced
  (`MUT-QUOTE-FIDELITY` dies); quote *attribution* is not.
- **m4 — the wall's positive leg is itself a seven-word register.** Live: "Species
  index one is exactly what another theory names its charge carrier, and index two
  its force mediator." carries no banned token and no `OUTSIDE_REGISTER` word and
  **survives**. The paper states the leg correctly ("a word of the **declared**
  outside register"), so this is a scope note; but `MUT-WALL-PARAPHRASE` uses
  *"elementary"* and *"world"*, both register words, so the falsifier does not
  actually probe the leg's boundary.
- **m5 — staging cleanup is not exception-safe.** The `.tmp` removal lives in an
  `if disk_bad or …` branch, not a `try/finally`. Live: an exception raised between
  staging and `G-ARTIFACT-INTEGRITY` leaves **both** `spc_output.txt.tmp` and
  `spc_receipt.json.tmp` in the tree. Published artifacts untouched, so this is
  residue rather than corruption.
- **m6 — `transcript_head` is never re-derived from the promoted transcript.**
  `G-ARTIFACT-INTEGRITY` checks `file == outtxt` (the in-memory string it just
  wrote), not `digest(file) == payload["transcript_head"]`. Live: corrupting the
  transcript *after* its digest is taken delivers at rc 0 with a stale head. **The
  delivered artifacts are honest** — I recomputed `digest(spc_output.txt)` =
  `3df7860feb68` = the receipt's `transcript_head` — but no gate enforces it. Same
  family as MAJOR-1: the seal is compared against the value the code just produced.
- **m7 — the four E-24 stamps are read by nothing.** `"measure": "COUNTING-ONLY"`
  sits on `carrier_census`, `odd_twist_species`, `selection`, `statistics`; no gate
  predicate references the key and no falsifier removes it. E-24 is satisfied in
  substance (no fraction is published unstamped; §12 declares it; the verdict carries
  `COUNTS-ARE-COUNTING-ONLY`) but it is a declaration inside a sealed object, not a
  measurement.
- **m8 — `MUT-TABLE-HEADER` injects into the gate's local variable, not the paper.**
  It reverses `theads[0]` *inside* `G-PAPER-TABLES-AND-QUOTES-ARE-BOUND`, after the
  claims gate has already scanned the clean text. A real paper-text header swap dies
  one gate **earlier**, at `G-PAPER-CLAIMS` (verified twice, below). Both die, so no
  coverage is lost — but the falsifier isolates the gate rather than exercising the
  path it advertises.
- **m9 — the `mutants` key is unswept *and* uncounted.** `POOL_EXCLUDED = {"mutants"}`
  removes it from the receipt wall (necessarily — `MUT-MUST-NOT`'s own description
  contains "mass" and "spectrum") and nothing recounts it. Live: appending one row
  carrying *"an electron, a photon and a mass spectrum"* delivers at rc 0 with those
  words in the receipt, 56 published rows against `totals.mutants = 55`, all gates
  green. Disclosed exclusion; the missing piece is `len(payload["mutants"]) ==
  totals["mutants"]`.
- **m10 — `DECLARED_UNSEALED` entries are not required to be located.** The unit
  applies "an exemption carried and never used is a hole rather than a courtesy" to
  `DECLARING` and `RECEIPT_WITHHOLDING` but not to its own unsealed declaration. All
  15 entries happen to be present in the delivered receipt (verified), so there is no
  live hole — the doctrine is applied asymmetrically.
- **m11 — a repeated `--mutant` silently takes the last value** rather than
  refusing. Cosmetic.
- **m12 — the consumer register covers 62 of the 74 anchors.** The 12 file-bytes
  anchors carry no `consumer` field; they are consumed by `G-SOURCE-BYTES` by
  construction. The paper's sentence is scoped to verbatim windows, so this is a
  scope note, not an over-claim.

---

## THE NINE PROBES — PRESENT / ABSENT WITH EVIDENCE

*(PRESENT = the hole exists; ABSENT = the instrument closes it.)*

**1. UNBOUND HEADERS — ABSENT (headers are genuinely bound).**
Two opposed-column swaps injected into the paper text:
`hosted`↔`homeless` in the carrier census header, and `symmetric only`↔`antisymmetric
only` in the statistics header. **Both die at `G-PAPER-CLAIMS`**, artifacts and tree
byte-unchanged, no `.tmp`. `render_table` emits the header line as a claim rendered
from the receipt keys, so the swap breaks the claim's occurrence count before the
binding gate is reached. Independently recounted: 15 header rows, 0 unbound.

**2. DIRECTION / VALUE FLIPS — SPLIT: fatal inside the verdict and inside tables;
PRESENT in unregistered prose.**

| flip | site | outcome |
|---|---|---|
| `SPC-SELECTION-OPEN` → `-CLOSED` | verdict fence | dies at `G-PAPER-VERDICT-EQUALITY` |
| `SPC-SELECTION-OPEN` → `-CLOSED` | feasibility table row | dies at `G-PAPER-CLAIMS` |
| `156-OF-246` → `246-OF-246` | verdict fence | dies at `G-PAPER-VERDICT-EQUALITY` |
| "156 of 246 species are hosted" → "246 of 246" | §4 prose (a registered claim) | dies at `G-PAPER-CLAIMS` |
| `…SHAPE-IS-ANTISYMMETRIC…` → `…SYMMETRIC…` | verdict fence | dies at `G-PAPER-VERDICT-EQUALITY` |
| `AT-2-OF-30` → `AT-30-OF-30` | verdict fence | dies at `G-PAPER-VERDICT-EQUALITY` |
| "…is the antisymmetric one" → "…the symmetric one" | §8 prose (unregistered) | **SURVIVES** |
| "host 2 of 30 species" → "host 30 of 30 species" | §4 prose (unregistered) | **SURVIVES, and delivers** |

The branching sequence 4→12→12→26→30→30 is a table column and a registered claim
("from 4 at the largest measured stabilizer to 30 at crystallization"), so reversing
it dies at `G-PAPER-CLAIMS` by the same route as the feasibility row. See MAJOR-2.

**3(a). THE TWO-ROUTE INDEPENDENCE — ABSENT (the disclosed repair is genuine).**
The claim is that row and column orthogonality are independent gates. Verified by an
**opposed pair**:

- drop a **species (a row)** — the declared `MUT-DROP-SPECIES`, one process,
  `--mutant`: **dies at `G-CHARACTER-TABLE-COLUMN-ORTHOGONALITY`**;
- drop a **class (a column)** — my own injection, a consistently rebuilt
  29-class/30-species table (classes, sizes, `where`, `inv_class`, `identity_class`
  and labels all re-indexed): **dies at `G-CHARACTER-TABLE-ROW-ORTHOGONALITY`**.

Two opposed corruptions, two different gates, both writing nothing. The code
matches: `table_gates` takes the row route over `len(T)` and the column route over
`len(ct["size"])`, so the two loops genuinely run over different index sets. **The
repair holds.**

**3(b). THE SIX REPAIRED FALSIFIERS — ABSENT.** The delivery ledger (#323) discloses
"six off-target falsifiers repaired" without naming them, so I swept **all 55**
out-of-harness rather than the six: one `--mutant NAME` process each, artifacts
hashed before and after every run, whole-tree hash checked, `.tmp` scan after each.
**Result: 55/55 DEAD-ON-TARGET, 48 distinct target gates, 55/55 artifacts unchanged,
55/55 tree unchanged, 0 stray temporaries, 0 off-target, 0 survivors.** E-23 verified
independently: all 55 published tokens are located in the source; all 55 declared
targets are real gate ids; the tree's 55 `mut()` switches and the 55 registry rows
have empty symmetric difference; no falsifier carries a thin description.

**4. UNSEALED-KEY FORGERY + POST-SEAL INSERTION — PRESENT (MAJOR-1).**
Pre-gate forgery dies at `G-SEAL-INTEGRITY`; post-gate insertion delivers a 50-key
receipt at exit 0. Sealed-object *edit* after the gate correctly dies at
`G-ARTIFACT-INTEGRITY`. Evidence table in MAJOR-1.

**5. TRANSCRIPT INTEGRITY — MOSTLY ABSENT; one hole (m6) and one disclosed whitelist
(m9).** Full-byte equality is real: the transcript is written to `.tmp`, read back
and compared byte-for-byte, and the receipt is compared byte-for-byte too, all
**before** `os.replace`. The whitelists are exactly two and both disclosed —
`POOL_EXCLUDED = {"mutants"}` (excluded from both the numeral pool and the receipt
wall) and `DIGEST_KEYS` (values excluded from the pool; pool-shrinking, therefore
strictness-increasing). The hole is that `transcript_head` is never re-derived from
the promoted file.

**6. PHANTOM CONSUMERS — ABSENT.** All 62 consumer-carrying anchors (43 path-value +
19 verbatim) name one of 19 gates; **all 19 exist in the source's gate set and all 19
passed** — recomputed independently against the AST-extracted gate universe, not
against the receipt's own list. Anchor load is spread 9/8/6/6/5/4/4/3/3/3/2/2/1×7,
summing to 62. All 43 path-value anchors `ok`; all 19 verbatim windows located
exactly once, all 19 killed by perturbation, min window 45 chars against a floor of
40. Waiver claims true: 49 clean-path gates, 48 carrying a falsifier, 1
(`G-ARTIFACT-INTEGRITY`) carrying a registered FORCING, 0 uncovered — recomputed.

**7. READ-BACK / STAGING / WRITE-NOTHING — ABSENT except m5.** Read-back precedes
`os.replace` and is load-bearing (C5 proves it). Write-nothing verified by whole-tree
hash on every failing injection and on all 55 falsifier runs: **0 trees moved, 0
stray `.tmp`**. One nit beyond m5: after the gate passes, the temporaries are
*re-written* from `data` and then promoted, so the promoted bytes are a fresh write
rather than the verified instance — deterministic here (same string), but the
verified instance is not the one that lands.

**8. SPELLED NUMERALS — PRESENT above ninety-nine (m1).** "two hundred twenty" alone
survives; "seventy-nine" alone dies. Ten spelled numerals above twelve are scanned
in the delivered paper, 0 unmatched.

**9. REFERENT BINDING — PRESENT (MAJOR-2).** "156 of 220" and the 220/246
one-universe sentence both deliver green; so does inverting §4's headline contrast,
which was then carried through a full delivery run.

---

## WHAT ELSE THE LENS CONFIRMED

- **Byte ×2, off-tree, git-less, at two `PYTHONHASHSEED` values (0 and 987654321),
  with the artifacts deleted first so the write is a real creation:** both runs
  reproduce `spc_output.txt` = `dc6410c72036` and `spc_receipt.json` = `3958fe51495b`,
  **byte-identical to the delivered artifacts**. No staging residue.
- **Receipt self-digests against delivered bytes:** `paper_sha256_12` = `1555d049d558`,
  `code_sha256_12` = `6b399487f286`, `pin_sha256_prefix` = `7f0b1e9d5071`,
  `transcript_head` = `3df7860feb68` — all four recomputed from the delivered files
  and all four agree. The 46-row ledger chain recomputed from the delivered receipt
  bytes: 0 mismatches. The 34-object seal manifest re-derived from the delivered
  receipt: 0 moved, 0 absent. The 12 provenance digests against the live repo: 12/12.
- **`--selftest` out-of-harness:** FATAL AT EVERY ANCHOR CLASS (FILE-BYTES /
  PATH-VALUE / VERBATIM all True), artifacts unchanged, no residue, rc 0.
- **Hostile argv, 28 forms** (`--bogus`, `-h`, empty string, `--mutant` with no name,
  unknown mutant name, `--mutant=X`, `--MUTANT`, `--no-write=1`, `-`, a shell-shaped
  argument `"--mutant; rm -rf /"`, flag repetition, flag combinations): every
  malformed form **exits 2** exactly as the disclosed convention states, `--help`
  exits 0, artifacts untouched throughout. `subprocess` is a banned import and argv
  is parsed rather than shelled, so there is no injection surface.
- **De-twinned comparator, checked by AST:** `build_verdict` and `reconstruct_verdict`
  share **0** format-bearing string literals (52 shared literals, all receipt key
  names — necessarily shared, both read the same receipt); `head_law` and
  `second_head_law` share 0 format-bearing literals (17 shared, all pre-registered
  outcome words). `reconstruct_verdict` takes only the serialized payload and
  references no live global. The de-twinning claim is real.
- **Gate hygiene, checked by AST:** 50 `LD.gate` call sites, 50 distinct ids, 0
  duplicates; **exactly one constant-boolean predicate**, and it is
  `G-PAPER-PRESENT`, the declared refusal-only gate registered with its reason; **no
  gate predicate anywhere references the mutant switch**; 16 `raise GateFail` sites,
  every one naming a real gate id.

---

## FIXES REQUIRED BEFORE THIS SEAT WOULD SIGN A CLEAN ACCEPT

1. Re-derive manifest totality from the bytes read back inside `G-ARTIFACT-INTEGRITY`,
   and add a falsifier that inserts a top-level key after `G-SEAL-INTEGRITY`. (MAJOR-1)
2. Add a referent-binding gate and render §4/§5/§7/§8's headline contrast sentences
   into `build_claims`; add a falsifier that re-pairs a numeral with the wrong
   referent. (MAJOR-2)
3. Bind `transcript_head` to the promoted file's digest inside `G-ARTIFACT-INTEGRITY`. (m6)
4. Move the `.tmp` cleanup into a `try/finally`. (m5)
5. Bind each blockquote to the *source* its window belongs to, not to the union of
   windows. (m3)
6. Make the paper-side digest whitelist digest-shaped (require an `a–f` character, as
   `DIGEST_RE` already does). (m2)
7. Recount `payload["mutants"]` against `totals["mutants"]`. (m9)
8. Either extend the number-word alphabet past ninety-nine or state its ceiling in
   the paper. (m1)

---

**All headlines above are candidate readings until adjudication.** The five object
hashes were verified at open and re-verified at close, unchanged. The only repo write
made by this seat is this file.
